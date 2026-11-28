---
name: local-check
description: Build the Java 21 ledger, run its tests and check the packaged Spring service over loopback using disposable state.
---

From the repository root select a JDK 21 via JAVA_HOME and run python tools/local_check.py. Read the separate build, test, startup and GET results and the exit status. On failure use the first failing step and process output for diagnosis. The script owns the temporary data directory and service process and cleans them on exit. Archive actual output with the tested revision and OS in the stage review. Implements SK-4. See [[knowledge-provenance]] and the verification-fixtures note.
