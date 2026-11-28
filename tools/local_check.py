"""Build, test, launch and check the packaged service on a private ephemeral port."""
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import sys
import tempfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    java = Path(os.environ["JAVA_HOME"]) / "bin" / ("java.exe" if os.name == "nt" else "java")
    version = subprocess.check_output([java, "-version"], stderr=subprocess.STDOUT, text=True)
    if not re.search(r'version "21(?:\.|")', version):
        raise ValueError("Select a JDK 21 installation with JAVA_HOME")
    wrapper = ["cmd.exe", "/d", "/c", "mvnw.cmd"] if os.name == "nt" else ["sh", "mvnw"]
    for label, args in (("build", ["clean", "package", "-DskipTests"]), ("tests", ["test"])):
        subprocess.run(wrapper + ["-B"] + args, cwd=ROOT, check=True)
        print(f"PASS {label}", flush=True)
    jar, = (ROOT / "target").glob("*.jar")
    with tempfile.TemporaryDirectory() as scratch:
        log = Path(scratch) / "startup.log"
        env = dict(os.environ, LEDGER_ADMIN_TOKEN=secrets.token_urlsafe(32))
        with log.open("wb") as output:
            service = subprocess.Popen([java, "-jar", jar, "--server.port=0"],
                                       env=env, cwd=scratch, stdout=output, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 60
            while time.monotonic() < deadline:
                content = log.read_text(encoding="utf-8", errors="replace")
                if service.poll() is not None:
                    raise RuntimeError("Service exited during startup: " + content[-1500:])
                port = re.search(r"Tomcat started on port (\d+)", content)
                if port:
                    break
                time.sleep(0.2)
            else:
                raise TimeoutError("Service startup timed out")
            print("PASS startup", flush=True)
            with urllib.request.urlopen(f"http://127.0.0.1:{port[1]}/health", timeout=5) as response:
                if (response.status != 200 or json.load(response) != {"status": "ok"}
                        or response.headers.get_content_type() != "application/json"
                        or response.headers.get("Cache-Control") != "no-store"
                        or response.headers.get("X-Content-Type-Options") != "nosniff"):
                    raise ValueError("Health response differs from contract")
            print("PASS GET /health")
        finally:
            if service.poll() is None:
                service.terminate()
                try:
                    service.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    service.kill()
                    service.wait()


if __name__ == "__main__":
    try:
        main()
    except (KeyError, OSError, ValueError, RuntimeError, subprocess.SubprocessError) as failure:
        sys.exit(f"FAIL {failure}")
