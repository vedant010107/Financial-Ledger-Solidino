# Stage 2 design session and evaluation

Day 2 started on main revision 7e14388. Work items are #10 (API), #11 (storage) and #12 (skills and health). The session translated the reviewed SRS into a contract and design and exercised the health slice. [[knowledge-provenance]] links these artifacts to the existing research.

On Windows with Java 21, python tools/local_check.py packaged the Spring Boot jar, ran two passing Java tests, started the service on an ephemeral loopback port and verified HTTP 200, JSON status, no-store and nosniff. An invalid JDK path produced a nonzero result. The health unit test initially failed to compile before the controller existed. The five existing Python ingestion tests passed. The vault and skill checks validated eleven notes and four skills.

For SK-2, a disposable vault copy contained a duplicate of the exact-money note and a misspelled link. Validation detected the link. The evaluation moved the canonical page to resources, retained the duplicate and its provenance in archive, fixed the reference and logged the operations. The resulting vault passed and an unrelated note remained byte-identical.

For SK-3, the retry question led to [[retry-identity]] and FR-2: a committed request with matching normalized fields replays the saved status/body after restart. Searching the vault for measured production throughput yielded no evidence; the SRS specifies a future reference workload. For SK-4 the successful live check and invalid-toolchain case are recorded above. Day 2 verification uses Windows only by team direction. The reviewed SRS retains its Windows and Linux portability requirement for the project. Hosted CI and human review remain pending until submission.

The architecture walkthrough established where the write lock is acquired, which writes roll back together and how a committed response survives restart. The health slice provides an early test of the HTTP boundary. Product posting and reconciliation tests remain later-stage work.

## Windows verification and API contract recheck

On 28 November 2026 the Java 21 local check packaged the service, passed both Java tests, started it on loopback and verified the health response and headers. Five Python tests passed. Vault validation covered eleven notes and skill validation covered four skills. Gitleaks scanned five reachable Git commits and reported zero findings.

The OpenAPI 3.0.3 document passed openapi-spec-validator and its examples passed openapi-schema-validator. Comparison with SRS IR-4 through IR-10, FR-1 through FR-5 and Appendix C covered all nine methods and paths, access roles, required request fields, success statuses, response shapes and error cases. The check resolved 476 reference occurrences and performed 382 example validations across route uses, including shared headers and errors. The three monetary operations have identical first-success and replay bodies with distinct replay headers. Reconciliation examples cover both clean and inconsistent snapshots.
