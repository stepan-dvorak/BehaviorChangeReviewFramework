---
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: RS-001
  title: Repository Standards
  filename: Repository_Standards.md
  type: Standard
  version: 2.0.0
  status: Active
classification:
  domain: Governance
  layer: Repository
  maturity: Stable
owner: Štěpán Dvořák
created: 2026-07-17
last_updated: 2026-07-17
quality:
  review: Approved
  evidence: Verified
  editorial: Reviewed
purpose: |
  Defines the governance model, metadata standard, document lifecycle and repository-wide conventions used throughout the Orden project.
audience:
  - Contributors
  - AI Assistants
  - Researchers
related_documents:
  - AGENTS.md
  - CONTRIBUTING_FOR_AI.md
  - Repository_Architecture.md
  - Repository_Taxonomy.md
  - Editorial_Style_Guide.md
tags:
  - governance
  - standards
  - repository
  - metadata
---

# Repository Standards

## 1. Purpose

This document defines the mandatory repository-wide standards used by every document within the Orden project.

It serves as the constitutional document governing repository structure, metadata, document lifecycle and knowledge organization.

---

# 2. Repository Principles

The repository is governed by the following principles:

- Evidence before opinion.
- Explicit assumptions.
- Architectural neutrality.
- Reproducibility.
- Transparency.
- Evolution instead of replacement.
- Human-reviewed AI collaboration.

---

# 3. Repository Architecture

The repository is organized as a structured knowledge base rather than a document collection.

Every document must:

- have a unique identity,
- define explicit relationships,
- be independently understandable,
- remain versionable.

---

# 4. Metadata Standard

Every document SHALL begin with YAML Front Matter.

Metadata is divided into four logical groups:

## Project

Defines repository identity.

```yaml
project:
```

---

## Document

Defines the identity of the document.

```yaml
document:
```

---

## Classification

Defines the role of the document.

```yaml
classification:
```

Recommended fields:

- domain
- layer
- maturity

---

## Quality

Defines repository review status.

Recommended fields:

```yaml
quality:
```

Possible values include:

- Draft
- Reviewed
- Approved
- Verified

---

# 5. Document Identification

Every document receives a permanent identifier.

Identifiers never change.

Examples:

RS
Repository Standard

CG
Contribution Guide

ADR
Architecture Decision Record

RD
Research Document

ES
Empirical Study

CS
Case Study

TR
Terminology

RW
Related Work

---

# 6. Classification Model

## Domain

Examples:

- Governance
- Research
- Architecture
- Evidence
- Templates
- Terminology
- Experiments

---

## Layer

Defines repository scope.

Possible values:

- Repository
- Project
- Study
- Document

---

## Maturity

Possible values:

- Draft
- Review
- Stable
- Deprecated
- Archived

---

# 7. Quality Model

Repository quality is evaluated independently from maturity.

Typical attributes include:

- review
- evidence
- editorial

---

# 8. Relationship Model

Documents should explicitly reference related knowledge.

Possible relationships include:

- depends_on
- related_documents
- references
- supersedes
- superseded_by

Together these relationships form the repository knowledge graph.

---

# 9. Versioning

Semantic Versioning SHALL be used.

MAJOR

Structural changes.

MINOR

New repository capabilities.

PATCH

Editorial improvements.

---

# 10. Repository Lifecycle

Document lifecycle typically follows:

Draft

↓

Review

↓

Approved

↓

Stable

↓

Deprecated

↓

Archived

---

# 11. AI Contributions

AI-generated content is welcome.

However:

- AI never replaces evidence.
- AI never invents citations.
- AI follows repository terminology.
- AI preserves metadata.
- Human review is mandatory.

Detailed workflow is defined in:

CONTRIBUTING_FOR_AI_v2.0.md

---

# 12. Repository Philosophy

The purpose of Orden is not merely to publish documentation.

Its purpose is to establish a reproducible methodology for evaluating software architecture through evidence-based reasoning and transparent decision making.

Repository standards therefore prioritize long-term consistency over short-term convenience.