---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: TR-IDX-001
  title: Terminology Index
  type: Terminology Index
  version: 0.1.0
  status: Active

classification:
  domain: Terminology
  layer: Repository
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Provides the canonical index of repository terminology, validation status,
  and definition sources.

quality:
  review: Self Reviewed
  evidence: Partial
  editorial: Reviewed

audience:
  - Contributors
  - AI Assistants
  - Researchers

depends_on:
  - 01_Terminology.md
  - References/Microsoft_IsHandled_v2.0.md

related_documents:
  - Repository_Standards.md
  - 03_Related_Work.md

tags:
  - terminology
  - index
  - canonical-concepts
---

# Terminology Index

## Purpose
Single canonical index of repository terminology.

## Priority
1. ISO terminology
2. Microsoft terminology
3. Repository terminology

## Repository Concepts
| Term | Status | Defined In |
|------|--------|------------|
| Behavior-changing customization | Stable | 01_Terminology.md |
| Responsibility Transfer | Candidate | References/Microsoft_IsHandled_v2.0.md |
| Evolution Ownership | Candidate | References/Microsoft_IsHandled_v2.0.md |
| Discoverability | Candidate | References/Microsoft_IsHandled_v2.0.md |
| Explicit Contract | Candidate | References/Microsoft_IsHandled_v2.0.md |
| Effective Extensibility | Candidate | References/Microsoft_IsHandled_v2.0.md |

No alternative spelling or synonyms should be introduced without updating this index.
