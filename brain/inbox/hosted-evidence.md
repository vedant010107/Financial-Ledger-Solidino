---
id: "hosted-evidence"
title: "Connect CI evidence to the submitted revision"
owner: "1Vedansh"
verification_assigned_to: "macwandarell"
verified_by: "macwandarell"
issue: 3
summary: "Configure push and pull_request events and inspect the actual run, commit and job conclusions. For the scaffold, record the individual build, lint, tests, secret and vault checks. A workflow file proves configuration; the hosted run and tested revision establish what ran. Record product behavior separately in later stages."
sources: ["https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows", "Reviewed Financial Ledger SRS, NFR-11"]
requirements: ["NFR-11"]
links: ["digest-continuity"]
---

# Connect CI evidence to the submitted revision

Configure push and pull_request events and inspect the actual run, commit and job conclusions. For the scaffold, record the individual build, lint, tests, secret and vault checks. A workflow file proves configuration; the hosted run and tested revision establish what ran. Record product behavior separately in later stages.

[[digest-continuity]]

- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- Reviewed Financial Ledger SRS, NFR-11
