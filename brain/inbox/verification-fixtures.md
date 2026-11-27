---
id: "verification-fixtures"
title: "Give concurrent clients the same disposable database"
owner: "1Vedansh"
verification_assigned_to: "vedant010107"
verified_by: "vedant010107"
issue: 3
summary: "JUnit provides temporary directories for isolated tests. Allocate a new file-backed SQLite database per case and point both concurrent clients at that same file through independent connections. Assert committed rows, balances and reconciliation, then close every connection so cleanup also works on Windows."
sources: ["https://docs.junit.org/current/writing-tests/annotations.html", "Reviewed Financial Ledger SRS, NFR-11"]
requirements: ["NFR-11"]
links: ["snapshot-recovery"]
---

# Give concurrent clients the same disposable database

JUnit provides temporary directories for isolated tests. Allocate a new file-backed SQLite database per case and point both concurrent clients at that same file through independent connections. Assert committed rows, balances and reconciliation, then close every connection so cleanup also works on Windows.

[[snapshot-recovery]]

- https://docs.junit.org/current/writing-tests/annotations.html
- Reviewed Financial Ledger SRS, NFR-11
