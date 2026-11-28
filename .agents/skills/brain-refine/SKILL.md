---
name: brain-refine
description: Refine Financial Ledger vault notes into PARA, merge duplicate research and repair note links while preserving provenance.
---

Work from the repository root. Read brain/index.md, brain/log.md, ai_author.txt and the candidate notes. For each candidate choose inbox for undecided material, projects for deliverable-specific work, areas for ongoing responsibilities, resources for reusable research and archive for retired records. Preserve stable IDs when moving a page. Use [[knowledge-provenance]] for the provenance rules (SK-2, NFR-10).

For overlapping notes, choose a canonical ID. Merge distinct findings, sources, requirement IDs and attribution into the canonical record. Keep the retired ID as an archive page linking to the canonical ID, and retain its central attribution and historical ingestion log. Update referring wikilinks and metadata links together. Repair a dangling link only when the intended target is supported by the note text; otherwise report the unresolved reference. Preserve unrelated files.

Record old/new paths, IDs, merge decisions and evidence in brain/log.md. Run python tools/brain.py and inspect the diff including preservation of source URLs and unrelated notes. Evaluate moves and merges on a disposable copy first. Record results in the stage review.
