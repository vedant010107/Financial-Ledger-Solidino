---
id: "digest-continuity"
title: "What the posting digest proves"
owner: "1Vedansh"
verification_assigned_to: "macwandarell"
verified_by: "macwandarell"
issue: 3
summary: "SHA-256 hashes bytes, so the design must define exactly how posting fields and both entries become bytes. Per SRS Appendix B.4, start with 64 zero characters and include the previous digest. Test a changed entry and a broken link. Detecting removal of a valid suffix requires a separately trusted head."
sources: ["https://csrc.nist.gov/pubs/fips/180-4/upd1/final", "Reviewed Financial Ledger SRS, NFR-7"]
requirements: ["NFR-7"]
links: ["verification-fixtures"]
---

# What the posting digest proves

SHA-256 hashes bytes, so the design must define exactly how posting fields and both entries become bytes. Per SRS Appendix B.4, start with 64 zero characters and include the previous digest. Test a changed entry and a broken link. Detecting removal of a valid suffix requires a separately trusted head.

[[verification-fixtures]]

- https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- Reviewed Financial Ledger SRS, NFR-7
