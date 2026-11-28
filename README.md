# Financial-Ledger-Solidino

## Stage 2 design and local verification

Read the [architecture decisions and diagrams](docs/design/design.md) and [nine-operation OpenAPI contract](docs/design/openapi.json). The Stage 2 executable exposes the public loopback health operation. With JAVA_HOME pointing to JDK 21, run `python tools/local_check.py` to package the jar, run tests, start it on an ephemeral loopback port and check its JSON response. The check generates its own temporary administrator credential and stops its service.

Java 21 and Spring Boot scaffold for an educational double-entry wallet API backed by SQLite. Stage 1 contains requirements, development tooling and a research vault. The remaining wallet and ledger operations are scheduled for Days 3 and 4.

## Run the local scaffold checks

With a JDK 21 installation selected through JAVA_HOME and Python 3.12 available, run these commands from the repository root. On Windows use `.\mvnw.cmd -B clean verify` for the first command.

```sh
bash mvnw -B clean verify
python -m unittest discover -s tests -v
python tools/brain.py
python tools/check_skills.py
```

The Maven build starts a Spring application context during its scaffold test and creates a runnable jar under target/. Product acceptance tests and SQLite integration follow in later stages. The GitHub workflow also scans history for secrets.

Open brain/ as an Obsidian vault. Begin with [the index](brain/index.md). See [the requirements PDFs](docs/requirements/), [the five-day plan](docs/superpowers/plans/2026-11-27-financial-ledger.md) and [the Stage 1 traceability table](docs/day-1/issue-drafts.md).
