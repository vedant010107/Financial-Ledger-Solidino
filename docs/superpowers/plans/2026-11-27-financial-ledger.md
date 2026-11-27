# Financial Ledger five-day implementation plan

Build the reviewed Financial Ledger REST API with Java 21, Spring Boot and SQLite. The course SDLC workflow defines the four stage submissions, the project brief defines FR-1 through FR-5, and the reviewed SRS defines the detailed contract and acceptance criteria. Days 3 and 4 together deliver Stage 3. A, B and C are assignment placeholders.

**Submission rule for every day.** Track work in GitHub Issues. Give each workstream one actual contributing author per feature branch and PR so that exactly two teammates are eligible to review. At day end, commit meaningful increments and push using each contributor’s individually authorized and verified session. For every PR, draw one of the two eligible reviewers uniformly at random, record the selection, request their review and wait for their actual decision. Resolve comments, rerun affected checks and obtain approval on the final changes before merging. Retain authorship and issue links. A day remains open until its deliverables pass, all three people’s contributions are committed and pushed, and its PRs clear review and CI. Review delays move the submission date.

**Daily report.** For each person record the work actually contributed, branch, commit SHAs and push result. For each PR record the linked issue, reviewer, decision and merge status. List commands, environment, results, hosted run links, failures, fixes and pending items. Record significant AI sessions and their outcomes in the vault. Each member authors their own notes and can explain their changes.

## Day 1 — Requirements and repository foundation · Stage 1

**Dependency.** Wait for the team’s start instruction. Before the first commit, obtain each person’s GitHub username, commit email (noreply is fine), explicit individual authorization and their own approved interactive GitHub sign-in. Verify all three accounts, push access and intended attribution. Verify remote state. For a genuinely empty remote establish the minimal common base needed to open PRs and record the bootstrap commit separately. Route all substantive work through reviewed PRs.

- **A:** Preserve the reviewed SRS, map its identifiers and acceptance criteria to issues, write the development plan and author four sourced notes on the API, authentication, exact money and retry semantics.
- **B:** Create the Obsidian vault in brain/ with inbox, projects, areas, resources, archive, index and operation log. Author brain-ingest/SKILL.md and three sourced notes on SQLite, concurrency and recovery. Make ingestion validate IDs, reject duplicate and unsafe IDs and create linked notes.
- **C:** Set up the Java 21 Maven wrapper, Spring Boot build skeleton, README, root AGENTS.md, changelog and CI on pushes and PRs. Author three sourced notes on verification, audit integrity and CI. Implement skill metadata, note schema and wikilink checks alongside build, lint, tests and secret scanning.

**Deliverables and checks.** Each author ingests their own notes once the skill is available. Verify at least ten distinct sourced notes with IDs, titles, summaries, authors, requirement links and wikilinks. Inspect the ingest log and commit authorship. Exercise success, duplicate ID and confined-path cases on temporary data. Capture real local and hosted scaffold results, Stage 1 skill evaluation and retrospective. Mark product acceptance as planned.

## Day 2 — Design, contracts and first local check · Stage 2

**Dependency.** Reviewed Stage 1 baseline, validated vault and working build. Agree on service and repository interfaces before splitting implementation.

- **A:** Write the nine-operation OpenAPI contract, role matrix, strict JSON and HTTP rules, status/error examples and transfer/reversal sequence diagrams. Document how Spring MVC, Jackson and the embedded server will enforce framing, byte limits, headers and timeouts at the correct layer.
- **B:** Deliver architecture and UML diagrams, ER diagram, physical SQLite schema, indexes, constraints and ADRs for the JDBC boundary, WAL, bounded write-lock waiting, atomic replay records, immutable rows, recovery and SHA-256 chain encoding. Specify canonical fields, ordering, genesis digest and trust boundary. Pin compatible dependency versions before product implementation.
- **C:** Deliver brain-refine, brain-query and local-check SKILL.md files, evaluation fixtures and a runnable loopback health slice. Automate build, tests, start, one read-only HTTP call, per-step results and cleanup on Windows and Linux.

**Deliverables and checks.** Compare OpenAPI with IR-1–IR-11 and the SRS route table. Walk a successful transfer, duplicate key, concurrent spend and rollback through the diagrams and schema. Verify every ADR and skill cites a distilled note. Exercise refine on duplicates/broken links, query on supported and missing evidence, and local-check on success and failure. Save actual results and the Stage 2 retrospective.

## Day 3 — Wallets, atomic posting and concurrent transfers · Stage 3 implementation

**Dependency.** Approved API, transaction and persistence contracts. Build the schema and posting interface first so HTTP and integration work can proceed against the same contract. For each behavior, write the failing test, observe the failure, implement and rerun.

- **A:** Implement registration, token handling, wallet creation, owner reads and ordered entry history. Implement the shared strict HTTP contract, loopback binding and startup validation. Own wallet, authentication and validation tests.
- **B:** Implement SQLite migrations, clearing accounts and the transaction boundary for funding and transfers. Write balanced entries, cached balances, audit digest and successful retry response in one commit. Enforce positive integer minor units, checked balance arithmetic, immutable records and normalized request fingerprints.
- **C:** Integrate funding and transfer endpoints with the posting service. Own real loopback and independent-connection tests for replay, changed payload, shared-key races, conflicting spends, lock exhaustion, injected failures, restart and lost responses.

**Deliverables and checks.** Pass AC-1–AC-3 on fresh databases. Fund 10,000 paise, transfer 3,000 and replay after restart with the original status and body. In the separate AC-3 fixture starting at 7,000 and 0, race two 5,000 transfers and verify exactly one commits, leaving 2,000 and 5,000. Check the five-second cumulative lock-wait bound, rollback at each posting step, and absence of partial entries, balances or retry records. Record actual results against issue and PR links.

## Day 4 — Reversals, reconciliation and verification · Stage 3 submission

**Dependency.** Integrated Day 3 build with durable sequencing, digest creation, retry storage and concurrent posting.

- **A:** Implement authorized, linked, once-only reversals with replay. Verify balanced inverse entries, preserved original history, competing reversals, reversal-of-reversal rejection and rejection when funds have been spent. Complete endpoint authorization and strict HTTP contract coverage.
- **B:** Implement read-only reconciliation on one consistent snapshot. Independently recompute balances, per-currency totals and the digest chain. Verify references, posting amounts, sequence continuity and reversal relationships. Test valid and deliberately corrupted disposable fixtures, wide totals, consistent backup and restored state.
- **C:** Deliver simulate-transfer/SKILL.md with executable assertions and captured output. Run the concurrency and benchmark suites, coordinate Windows/Linux CI, maintain the defect log and add a regression test for each significant defect.

**Deliverables and checks.** Pass AC-4–AC-5 and run all FR, IR, NFR and testing requirements from the trace matrix. A completed check of a corrupted fixture returns HTTP 200 with ok=false and identifies the affected record. Run at least 100 simultaneous shared-wallet attempts and account for every outcome. Separately benchmark the reconciled 10,000-transaction INR dataset, using the SRS starting balances, 20 warm-ups and 10 clients issuing 10 timed transfers each. At least 95 of 100 must succeed within two seconds and reconciliation must pass. Record hardware, latency percentiles, exact arithmetic/overflow, sanitized errors, rollback/restart and isolated database cleanup results. Deliver the CI/test plan and results, skill evaluations, defect log, updated trace links and Stage 3 retrospective.

## Day 5 — Live demonstration, traceability and release · Stage 4

**Dependency.** Approved Stage 3 build with passing acceptance tests, hosted CI evidence and a reproducible synthetic demo dataset.

- **A:** Lead the client demonstration for registration, wallets, funding, transfer, retry and concurrent spending. Use the Appendix C journey to show the final user balances of 2,000 and 8,000 paise against the clearing balance of −10,000. Demonstrate a reversal afterward and explain its linked entries.
- **B:** Run simulate-transfer and reconciliation live, explain the digest chain and recovery boundary, and trace one requirement from sourced note through ADR, issue, PR, code, test and result. Complete the trace matrix for all requirements.
- **C:** Run local-check and brain-query live. Verify setup on a clean checkout, finalize the user/API guide and changelog, capture demo and skill evidence, and coordinate final release tagging after review.

**Deliverables and checks.** Demonstrate all five FRs through a client and verify the live skill outputs. Each member explains their contribution. Complete the Stage 4 retrospective, final skill evaluations and daily submission checks. Tag and push the exact reviewed commit after its hosted checks pass. Record the tag, SHA, PRs, CI runs and demo evidence in the final report.
