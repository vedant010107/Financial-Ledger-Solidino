---
name: brain-ingest
description: Add sourced Financial Ledger research to the Obsidian vault with a unique ID, trace links and an operation log entry.
---

Prepare a JSON object with id (lowercase hyphenated words), title, owner, verification_assigned_to, verified_by, summary, sources, requirements and links. The last three fields are nonempty lists. Link existing vault page IDs. Record the assigned work item. Use author for an actual writer or identify the writer in the root ai_author.txt using the note ID. Assign a checker other than the owner. Set verified_by to null until the checker supplies a statement recorded in ai_author.txt.

From the repository root run `python tools/brain.py --ingest <note.json>`. Check the new page in brain/inbox and the appended entry in brain/log.md. Use `python tools/brain.py --vault <temporary-vault> --ingest <fixture.json>` for evaluation. A duplicate, invalid ID or broken link fails the operation. See [[knowledge-provenance]] for the source and authorship convention. Implements SK-1 and NFR-10.
