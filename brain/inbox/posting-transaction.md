---
id: "posting-transaction"
title: "Define the atomic posting boundary"
owner: "macwandarell"
verification_assigned_to: "vedant010107"
verified_by: "vedant010107"
issue: 2
summary: "SQLite can autocommit statements individually. Enclose the debit, credit, cached balances, audit data and retry result in one explicit write transaction on one connection. Inject a failure between debit and credit and verify both the financial state and key remain available for a clean retry."
sources: ["https://www.sqlite.org/lang_transaction.html", "Reviewed Financial Ledger SRS, NFR-4"]
requirements: ["NFR-4"]
links: ["retry-identity"]
---

# Define the atomic posting boundary

SQLite can autocommit statements individually. Enclose the debit, credit, cached balances, audit data and retry result in one explicit write transaction on one connection. Inject a failure between debit and credit and verify both the financial state and key remain available for a clean retry.

[[retry-identity]]

- https://www.sqlite.org/lang_transaction.html
- Reviewed Financial Ledger SRS, NFR-4
