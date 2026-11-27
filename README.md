# Financial-Ledger-Solidino

Java 21 and Spring Boot scaffold for an educational double-entry wallet API backed by SQLite. Stage 1 contains requirements, development tooling and a research vault. The nine product operations are scheduled for later stages.

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
