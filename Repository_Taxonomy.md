---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: GOV-TAX-001
  title: Repository Taxonomy
  type: Governance Standard
  version: 1.0.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Defines the canonical classification and placement of artifacts in the Orden
  repository.

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
  - Decisions/ADR-001_Repository_Artifact_Profiles_and_Metadata.md

related_documents:
  - Repository_Index.yaml
  - README.md

tags:
  - governance
  - taxonomy
  - classification
  - repository-structure
---

# Repository Taxonomy

## 1. Purpose

This document defines the canonical classification and placement of repository
artifacts.

It determines where an artifact belongs. Metadata requirements and artifact
profiles are defined in `Repository_Standards.md`. Actual artifact inventory and
retrieval routing are defined in `Repository_Index.yaml`.

---

## 2. Classification Principles

- Classify an artifact by its primary responsibility, not by filename or size.
- Assign one primary category.
- Record cross-category relationships through metadata.
- Do not classify a research stub as completed evidence.
- Do not place superseded material among active canonical sources.
- Prefer an existing category unless a new responsibility cannot be represented.

---

## 3. Categories

### 3.1 Repository Entrypoints

Conventional human or agent entrypoints.

Location: repository root.

Current examples:

- `README.md`;
- `AGENTS.md`.

These artifacts use the `repository_entrypoint` profile.

### 3.2 Governance

Repository-wide principles, standards, operational workflows, editorial rules,
terminology indexes, and conformance governance.

Location: repository root unless a dedicated governed collection is defined.

Current examples:

- `Governance_Principles.md`;
- `Repository_Standards.md`;
- `Repository_Taxonomy.md`;
- `Editorial_Style_Guide.md`;
- `Evidence_Hierarchy.md`;
- `Reasoning_Standard.md`;
- `Contributing_for_AI.md`;
- `Terminology_Index.md`.

### 3.3 Decisions

Architecture decision records that preserve the context, decision, rationale,
consequences, and reopening criteria of accepted or proposed repository
decisions.

Location: `Decisions/`.

Current example:

- `Decisions/ADR-001_Repository_Artifact_Profiles_and_Metadata.md`.

### 3.4 Core Research

Long-lived documents defining research scope, evolution, terminology,
methodology, and related work.

Location: repository root.

Current examples:

- `00_Project_Charter.md`;
- `00_Research_Log.md`;
- `01_Terminology.md`;
- `02_Research_Methodology.md`;
- `03_Related_Work.md`.

### 3.5 Reference Analyses

Substantive source-specific analyses of standards, official documentation,
literature, source code, product behavior, and relevant community publications.

Location: `References/`.

Examples include completed ISO, SEI, and Microsoft analyses.

These artifacts use the `reference_analysis` profile.

### 3.6 Research Stubs

Intentional placeholders that scope planned reference research but do not
contain conclusions.

Location: `References/`.

These artifacts use the `research_stub` profile and remain clearly
distinguishable from substantive reference analyses.

### 3.7 Empirical Studies

Evidence collected from Business Central applications, repositories, product
behavior, or experiments.

Location: `Empirical/`.

These artifacts use the `empirical_study` profile.

### 3.8 Historical References

Historical publications, provenance records, and contextual material relevant
to the evolution of the investigated mechanisms.

Location: `Historical_References/`.

Historical authority SHALL remain distinguishable from current official
guidance and repository conclusions.

### 3.9 Ideas

Non-canonical proposals, unresolved directions, external discussion links, and
future-work notes.

Location: `Ideas/`.

Ideas MAY inform hypotheses but SHALL NOT be retrieved as validated conclusions
or normative rules.

### 3.10 Templates

Governed structures for creating new repository artifacts.

Location: `Templates/`.

Templates use the `governed_document` profile with an appropriate
`document.type`.

### 3.11 Framework and Whitepaper

Mechanism-independent synthesis and publication-oriented research outputs.

Location: `Whitepaper/` for current publication drafts. Additional framework
paths MAY be introduced when an approved deliverable requires them.

These documents synthesize research; they SHALL not independently redefine
evidence or canonical terminology.

### 3.12 Machine-Readable Artifacts

Native machine-readable inventory, retrieval, validation, or generated
artifacts.

Current location: repository root unless a future tooling directory is
approved.

Current example:

- `Repository_Index.yaml`.

These artifacts use their native format and the applicable machine profile.

### 3.13 Archive

Superseded, historical, or retired repository artifacts.

Location: `Archive/`.

Archived artifacts are excluded from ordinary retrieval and SHALL NOT override
active governance or canonical research.

---

## 4. Placement Decision

When introducing an artifact, determine placement in this order:

1. Is it a conventional repository or agent entrypoint?
2. Does it define repository rules or decisions?
3. Does it define long-lived core research state?
4. Does it analyze a source or collect empirical evidence?
5. Is it intentionally incomplete future research?
6. Is it synthesis, a template, an idea, or historical context?
7. Is it machine-readable or generated?
8. Is it superseded or retired?

If no category fits, the contributor SHALL propose a taxonomy change before
creating a new directory category.

---

## 5. Lifecycle and Movement

Lifecycle status and maturity are defined in `Repository_Standards.md`.

An artifact MAY move between categories when its primary responsibility
changes. Examples:

- a research stub becomes a reference analysis while remaining in
  `References/`;
- an active analysis moves to `Archive/` after replacement;
- an idea becomes a governed decision after owner approval and relocation to
  `Decisions/`.

Moves SHALL update active relationships and `Repository_Index.yaml` atomically.

---

## 6. Excluded Classification Signals

The following SHALL NOT determine category or maturity by themselves:

- file size;
- number of headings;
- age;
- writing polish;
- presence in a retrieval result;
- confidence of an AI-generated summary.

Classification SHALL follow actual purpose, evidence state, and content
maturity.

---

## 7. Revision History

### 1.0.0 — 2026-07-17

- Implemented the taxonomy consequences of ADR-001.
- Added entrypoints, decisions, research stubs, historical references, ideas,
  templates, whitepaper, and machine-readable categories.
- Distinguished taxonomy from metadata profiles and actual inventory.
- Added placement and movement rules.
