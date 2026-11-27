---
id: "writer-contention"
title: "Two spenders and one balance"
owner: "macwandarell"
verification_assigned_to: "1Vedansh"
verified_by: "1Vedansh"
issue: 2
summary: "SQLite serializes writers and WAL allows readers to see a stable snapshot. Read the spendable balance inside the write transaction. With 7,000 available, two independent requests for 5,000 can fund one transfer. Test lock exhaustion separately from insufficient funds so a busy result is correctly accounted for."
sources: ["https://www.sqlite.org/isolation.html", "Reviewed Financial Ledger SRS, FR-3"]
requirements: ["FR-3"]
links: ["posting-transaction"]
---

# Two spenders and one balance

SQLite serializes writers and WAL allows readers to see a stable snapshot. Read the spendable balance inside the write transaction. With 7,000 available, two independent requests for 5,000 can fund one transfer. Test lock exhaustion separately from insufficient funds so a busy result is correctly accounted for.

[[posting-transaction]]

- https://www.sqlite.org/isolation.html
- Reviewed Financial Ledger SRS, FR-3
