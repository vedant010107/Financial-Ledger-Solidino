# Stage 1 issue drafts

GitHub issues are assigned to [A, vedant010107, #1](https://github.com/vedant010107/Financial-Ledger-Solidino/issues/1), [B, macwandarell, #2](https://github.com/vedant010107/Financial-Ledger-Solidino/issues/2) and [C, 1Vedansh, #3](https://github.com/vedant010107/Financial-Ledger-Solidino/issues/3). Link PRs and hosted verification evidence as each becomes available.

## A — Baseline requirements and development plan

Preserve the reviewed SRS and link the development plan to its Appendix D. Use the following groups when opening the implementation and verification issues. Product acceptance is planned.

| Requirements | Assigned verification |
| --- | --- |
| FR-1, AC-1 | Wallet uniqueness, ownership and balanced funding |
| FR-2, AC-2 | Normalized retry, changed request conflict and replay after restart |
| FR-3, AC-3, NFR-2, NFR-4, NFR-8 | Competing spends, shared keys, bounded contention and rollback |
| FR-4, AC-4, NFR-7 | Immutable entries, reversal rules and hash-chain integrity |
| FR-5, AC-5 | Snapshot reconciliation of both correct and deliberately inconsistent test data |
| IR-1–IR-11, NFR-5–NFR-6 | Local startup, nine-route HTTP contract, authorization and safe errors |
| NFR-1, NFR-3, TQ-S | Timed workload, exact arithmetic, limits and input validation |
| NFR-9–NFR-11, SK-1–SK-5 | Java 21, portability, evidence quality, isolated tests and skill evaluations |
| SE-1–SE-7, SB-1–SB-6, TQ-1–TQ-8 | Development artifacts, knowledge records, team reviews and regression evidence |

Author four sourced notes on API behavior, authentication, exact money and retry semantics. Link requirements and related notes. Check the coverage against the reviewed PDF.

## B — Obsidian vault and brain-ingest

Set up the PARA vault, index and operation log. Implement the ingest skill with ID validation, duplicate rejection, path confinement and a recorded operation for each successful ingest. Author three sourced notes on SQLite, concurrency and recovery. Evaluate ingestion against a disposable vault and preserve the observed results.

## C — Build, CI and repository guidance

Set up a Java 21 Spring Boot Maven wrapper build and a scaffold test. Add the README, AGENTS.md and changelog. Configure push and PR checks for build, lint, tests, secrets, note schema, links and skill metadata. Author three sourced notes on verification, audit integrity and CI. Attach local results and actual hosted run links separately.
