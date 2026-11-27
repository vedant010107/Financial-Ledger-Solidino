---
id: "retry-identity"
title: "Recover a transfer whose response was lost"
owner: "vedant010107"
verification_assigned_to: "macwandarell"
verified_by: "macwandarell"
issue: 1
summary: "HTTP POST alone gives the client no assurance that a second debit is safe. Scope a stored success to caller, operation and key and compare normalized parameters. If the client retries after commit and restart, replay the saved status and body. Reject a changed amount under that key, and verify only one debit exists."
sources: ["https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2", "Reviewed Financial Ledger SRS, FR-2"]
requirements: ["FR-2"]
links: ["integer-money"]
---

# Recover a transfer whose response was lost

HTTP POST alone gives the client no assurance that a second debit is safe. Scope a stored success to caller, operation and key and compare normalized parameters. If the client retries after commit and restart, replay the saved status and body. Reject a changed amount under that key, and verify only one debit exists.

[[integer-money]]

- https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2
- Reviewed Financial Ledger SRS, FR-2
