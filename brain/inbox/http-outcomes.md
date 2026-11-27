---
id: "http-outcomes"
title: "HTTP results a client can act on"
owner: "vedant010107"
verification_assigned_to: "1Vedansh"
verified_by: "1Vedansh"
issue: 1
summary: "A client needs to distinguish a missing credential (401), insufficient permission (403) and a conflict with current wallet state (409). For an unsupported method on an existing route, verify the 405 response includes Allow. Exercise the routes through HTTP so Spring’s default errors cannot silently replace the SRS JSON envelope."
sources: ["https://www.rfc-editor.org/rfc/rfc9110#section-15", "Reviewed Financial Ledger SRS, IR-7"]
requirements: ["IR-7"]
links: ["knowledge-provenance"]
---

# HTTP results a client can act on

A client needs to distinguish a missing credential (401), insufficient permission (403) and a conflict with current wallet state (409). For an unsupported method on an existing route, verify the 405 response includes Allow. Exercise the routes through HTTP so Spring’s default errors cannot silently replace the SRS JSON envelope.

[[knowledge-provenance]]

- https://www.rfc-editor.org/rfc/rfc9110#section-15
- Reviewed Financial Ledger SRS, IR-7
