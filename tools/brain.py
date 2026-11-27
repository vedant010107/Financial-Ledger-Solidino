"""Ingest a sourced note or validate the Financial Ledger vault."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

ID = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def disclosure(root):
    path = root.parent / "ai_author.txt"
    if not path.exists():
        return []
    return [line.split(" | ", 3) for line in path.read_text(encoding="utf-8").splitlines()]


def fields(note, records):
    for key in ("id", "owner", "verification_assigned_to", "title", "summary"):
        if not isinstance(note.get(key), str) or not note[key].strip():
            raise ValueError(f"Missing {key}")
    if not ID.fullmatch(note["id"]):
        raise ValueError("Unsafe note ID")
    author = note.get("author")
    if not (isinstance(author, str) and author.strip()) and not any(
        len(row) == 3 and row[:2] == ["note", note["id"]] and row[2].strip()
        for row in records
    ):
        raise ValueError("Missing authorship record")
    checker = note["verification_assigned_to"]
    if checker == note["owner"]:
        raise ValueError("Assign verification to another teammate")
    if "verified_by" not in note:
        raise ValueError("Missing verification status")
    verified = note["verified_by"]
    if verified is not None and (verified != checker or not any(
        len(row) == 4 and row[:3] == ["verified", note["id"], verified] and row[3].strip()
        for row in records
    )):
        raise ValueError("Missing matching verification evidence")
    for key in ("sources", "requirements", "links"):
        values = note.get(key)
        if not isinstance(values, list) or not values or not all(
            isinstance(v, str) and v.strip() for v in values
        ):
            raise ValueError(f"Invalid {key}")


def pages(root):
    result = {}
    for path in root.rglob("*.md"):
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"External vault path: {path}")
        if path.stem in result:
            raise ValueError(f"Duplicate ID: {path.stem}")
        result[path.stem] = path
    return result


def ingest(root, note):
    fields(note, disclosure(root))
    known = pages(root)
    key = note["id"]
    if key in known:
        raise ValueError(f"Duplicate ID: {key}")
    if set(note["links"]) - known.keys():
        raise ValueError("Unknown linked note")
    inbox = root / "inbox"
    log = known["log"]
    if inbox.resolve() != root.resolve() / "inbox":
        raise ValueError("Inbox must be inside the vault")
    body = ["---", *(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in note.items()),
            "---", "", "# " + note["title"], "", note["summary"], "",
            " ".join(f"[[{link}]]" for link in note["links"]), "",
            *("- " + source for source in note["sources"])]
    path = inbox / (key + ".md")
    with path.open("x", encoding="utf-8") as out:
        out.write("\n".join(body) + "\n")
    try:
        with log.open("a", encoding="utf-8") as out:
            stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
            out.write(f"| {stamp} | Ingested [[{key}]] |\n")
    except OSError:
        path.unlink()
        raise


def validate(root):
    known = pages(root)
    records = disclosure(root)
    count = 0
    for key, path in known.items():
        content = path.read_text(encoding="utf-8")
        if path.parent.name in ("inbox", "resources"):
            if not content.startswith("---\n"):
                raise ValueError(f"{key}: missing metadata")
            header, content = content[4:].split("\n---\n", 1)
            note = {}
            for line in header.splitlines():
                field, value = line.split(": ", 1)
                note[field] = json.loads(value)
            fields(note, records)
            if note["id"] != key or set(note["links"]) - known.keys():
                raise ValueError(f"{key}: inconsistent metadata")
            count += 1
        for target in LINK.findall(content):
            if target not in known:
                raise ValueError(f"{key}: broken link to {target}")
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path("brain"))
    parser.add_argument("--ingest", type=Path, help="JSON note input")
    args = parser.parse_args()
    if args.ingest:
        ingest(args.vault, json.loads(args.ingest.read_text(encoding="utf-8-sig")))
    print(f"Validated {validate(args.vault)} research notes")
