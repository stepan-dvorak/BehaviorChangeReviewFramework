---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: GOV-EVH-001
  title: Evidence Hierarchy
  type: Governance Standard
  version: 0.1.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Defines the relative authority of evidence used throughout the repository.

quality:
  review: Self Reviewed
  evidence: N/A
  editorial: Reviewed

audience:
  - Contributors
  - AI Assistants
  - Researchers

depends_on:
  - Repository_Standards.md

related_documents:
  - Reasoning_Standard.md
  - 02_Research_Methodology.md
  - Editorial_Style_Guide.md

tags:
  - governance
  - evidence
  - authority
  - research
---

# Evidence Hierarchy

## Purpose
Defines the authority of evidence used throughout the repository.

## Evidence Levels

1. ISO standards
2. Peer-reviewed literature
3. SEI publications
4. Microsoft Learn
5. Official Microsoft source code
6. Microsoft product behavior
7. Community publications
8. Repository interpretation
9. Hypotheses

## Rules
- Distinguish evidence from interpretation.
- Every conclusion must reference supporting evidence.
- Candidate concepts require validation from multiple independent sources.
- Negative evidence must be recorded, not discarded.
