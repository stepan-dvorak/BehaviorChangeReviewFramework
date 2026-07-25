---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: TOOL-OWNER-REVIEW-001
  title: Orden OwnerReview
  type: Tool Guide
  version: 1.0.0
  status: Active

classification:
  domain: Tooling
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Explains how to run and safely use the local OwnerReview application for
  non-mutating review of JSONL worksheets.

audience:
  - Repository Owner
  - Contributors

related_documents:
  - Empirical/BCApps_CZ_Coarse_Screen_Execution_Protocol.md

tags:
  - tooling
  - owner-review
  - JSONL
---

# Orden OwnerReview

OwnerReview is a local browser tool for human review of prepared JSON Lines
worksheets. It keeps owner-review data separate from source research records and
does not write to GitHub or modify the selected JSONL file.

## Requirements

- Windows with `python` available on `PATH`;
- current Chrome or Edge;
- no Node.js or package installation is required for normal use.

## Start

1. Run `Start_OwnerReview.bat`.
2. Open the displayed local URL if the browser does not open automatically.
3. Select the source `.jsonl` with **Load JSONL**.
4. Optionally load `Empirical/Data/BCApps_CZ_Coarse_Screen_Batches.json` and
   select a batch, or enter an inclusive inventory-ID range.
5. Review each area, then set the overall result. The browser saves changes
   locally against the input file's SHA-256 fingerprint.
6. Export the Markdown report and JSON session before moving the review to
   another browser or computer.

The default BCApps reference is the fixed pilot commit. Select `main (latest)`
only when intentionally comparing the current source. The selected reference
is retained in the session and report.

Arrow Left and Arrow Right navigate records unless focus is inside an input,
text area, or select control.

## Data and Safety

The application has no external dependencies, analytics, or network requests.
The local Python process only serves static application files. Source files are
read through explicit browser file selection. Dynamic content is rendered with
DOM text nodes or `textContent`; only validated `src/` citations generate
GitHub links.

**Clear session** permanently removes the current dataset's saved browser
session after confirmation. Export the JSON session first if it may be needed.

## Automated Tests

Node.js is used only for repository development tests:

```text
node --test Tools/OwnerReview/tests/owner-review.test.mjs
```

No packages need to be installed.
