---
id: "snapshot-recovery"
title: "Verify the recovered ledger"
owner: "macwandarell"
verification_assigned_to: "vedant010107"
verified_by: "vedant010107"
issue: 2
summary: "The SQLite backup API provides a consistent database snapshot. Use a supported snapshot or stop the service, checkpoint and close its database connections before a manual copy. Reopen the restored file, reconcile it, then replay a previously successful key to verify both financial history and its saved response survived."
sources: ["https://www.sqlite.org/backup.html", "Reviewed Financial Ledger SRS, NFR-4"]
requirements: ["NFR-4"]
links: ["writer-contention"]
---

# Verify the recovered ledger

The SQLite backup API provides a consistent database snapshot. Use a supported snapshot or stop the service, checkpoint and close its database connections before a manual copy. Reopen the restored file, reconcile it, then replay a previously successful key to verify both financial history and its saved response survived.

[[writer-contention]]

- https://www.sqlite.org/backup.html
- Reviewed Financial Ledger SRS, NFR-4
