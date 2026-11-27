---
id: "integer-money"
title: "Why wallet balances use minor units"
owner: "vedant010107"
verification_assigned_to: "1Vedansh"
verified_by: "1Vedansh"
issue: 1
summary: "SQLite binary floating point approximates many decimal fractions. Represent INR 1.25 as 125 paise from the JSON boundary through storage. For a destination already holding the maximum signed 64-bit balance, adding one must reject the whole posting and preserve both balances. Reconciliation may need wider exact totals."
sources: ["https://www.sqlite.org/floatingpoint.html", "Reviewed Financial Ledger SRS, NFR-3"]
requirements: ["NFR-3"]
links: ["bearer-ownership"]
---

# Why wallet balances use minor units

SQLite binary floating point approximates many decimal fractions. Represent INR 1.25 as 125 paise from the JSON boundary through storage. For a destination already holding the maximum signed 64-bit balance, adding one must reject the whole posting and preserve both balances. Reconciliation may need wider exact totals.

[[bearer-ownership]]

- https://www.sqlite.org/floatingpoint.html
- Reviewed Financial Ledger SRS, NFR-3
