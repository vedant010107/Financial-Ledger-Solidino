---
id: "bearer-ownership"
title: "A token identifies a caller, ownership authorizes a debit"
owner: "vedant010107"
verification_assigned_to: "macwandarell"
verified_by: "macwandarell"
issue: 1
summary: "Possession of a bearer token is sufficient to present it. The ledger must separately check that the caller owns the source wallet. Test a valid user token against another owner’s wallet and expect 403. Per the SRS, return the token once, persist its digest and keep the raw credential out of logs."
sources: ["https://www.rfc-editor.org/rfc/rfc6750#section-1.2", "Reviewed Financial Ledger SRS, NFR-5"]
requirements: ["NFR-5"]
links: ["http-outcomes"]
---

# A token identifies a caller, ownership authorizes a debit

Possession of a bearer token is sufficient to present it. The ledger must separately check that the caller owns the source wallet. Test a valid user token against another owner’s wallet and expect 403. Per the SRS, return the token once, persist its digest and keep the raw credential out of logs.

[[http-outcomes]]

- https://www.rfc-editor.org/rfc/rfc6750#section-1.2
- Reviewed Financial Ledger SRS, NFR-5
