---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: TOOL-OWNER-REVIEW-EXAMPLE-001
  title: Owner Review Report Test-Data Example
  type: Tool Output Example
  version: 1.0.0
  status: Active

classification:
  domain: Tooling
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Demonstrates the Markdown report format with synthetic data without claiming
  that an empirical owner review occurred.

related_documents:
  - Tools/OwnerReview/README.md

tags:
  - tooling
  - owner-review
  - example
---

# Owner Review Report — Test Data Example

> Example output derived from synthetic test data. This is not evidence that an
> owner review of any retained empirical record was performed.

## Session

- Input file: `synthetic-test.jsonl`
- Input SHA-256: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- BCApps ref: `397d01199c321e774edaf23a7290fee40f75c6a6`
- Records in scope: 2

## Summary

- Accepted: 1
- Correction Required: 1
- Not Reviewed: 0

## Required Corrections

| Inventory ID | Area | Issue | Expected correction | Note |
|---|---|---|---|---|
| TEST-0002 | Subscriber body | Cited range ends before the procedure body. | Extend the citation through the closing `end;`. | Synthetic example only. |

## Checkpoint

Owner review: Correction Required
