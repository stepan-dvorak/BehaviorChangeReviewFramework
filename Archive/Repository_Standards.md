---
project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RS-001
  title: Repository Standards
  type: Standard
  status: Active
  version: 1.0.0

owner: Štěpán Dvořák
created: 2026-07-17
last_updated: 2026-07-17

review_status: Approved

related_documents:
  - README.md
  - AGENTS.md
  - Repository_Architecture.md
  - Repository_Taxonomy.md
  - Editorial_Style_Guide.md

tags:
  - governance
  - standards
  - repository
  - methodology
---

# Repository Standards

## Purpose

This document defines the mandatory standards governing the **Orden – Behavior Change Review Framework** repository.

Its purpose is to ensure that every contribution—whether created by a human author or an AI assistant—follows the same architectural, editorial, and methodological principles.

This document acts as the constitutional document of the repository.

---

# Core Principles

Every document SHALL satisfy the following principles.

## 1. Reproducibility

Claims must be supported by traceable evidence.

Readers should always be able to understand:

- where a statement originated,
- why it is included,
- what evidence supports it.

---

## 2. Transparency

Opinions, interpretations and verified facts must never be mixed.

Documents should clearly distinguish:

- Facts
- Interpretation
- Hypothesis
- Future Work

---

## 3. Architectural Neutrality

The repository does not advocate technologies.

It evaluates architectural decisions using explicit criteria.

No technology shall be considered "good" or "bad" without supporting evidence.

---

## 4. Evolution

Documents are expected to evolve.

Historical conclusions are preserved.

New evidence extends—not rewrites—the research.

---

## 5. AI Collaboration

AI is considered a research assistant.

Human review remains the final authority.

Every AI-generated contribution should be understandable, reviewable and verifiable.

---

# Metadata Standard

Every repository document SHALL begin with YAML Front Matter.

Minimum metadata:

```yaml
project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id:
  title:
  type:
  status:
  version:

owner:

created:
last_updated:

review_status:

tags:
```

Optional metadata:

```yaml
related_documents:

depends_on:

supersedes:

superseded_by:

references:

keywords:
```

---

# Document Identification

Each document receives a stable identifier.

Examples:

```
RS-001 Repository Standards
RM-001 Research Methodology
ADR-001 Architecture Decision Record
ES-001 Empirical Study
MS-001 Microsoft Study
TR-001 Terminology
RW-001 Related Work
```

Identifiers are immutable.

Titles may change.

Identifiers never change.

---

# Relationship Standard

Documents should explicitly describe relationships.

Possible relationships include:

- depends_on
- related_documents
- supersedes
- superseded_by
- references

These relationships should form a navigable knowledge graph.

---

# Evidence Hierarchy

Evidence shall be classified according to the repository Evidence Hierarchy.

Typical order:

1. Standards (ISO, RFC)
2. Peer-reviewed publications
3. Official vendor documentation
4. Source code
5. Empirical experiments
6. Community articles
7. Personal observations

Lower levels may support—but should not replace—higher levels.

---

# Editorial Standard

Documents should:

- prefer precise language
- avoid unnecessary marketing language
- avoid emotional wording
- separate observation from conclusion
- remain understandable to future readers

---

# Terminology Standard

Each technical term should have one preferred definition.

Alternative terminology may be documented.

Definitions should not silently change over time.

---

# Templates

All repository documents should be created using the appropriate template.

Examples include:

- Research Document
- Architecture Decision Record
- Empirical Study

---

# Versioning

Version numbers follow Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Major

: Breaking structural changes.

Minor

: New content or sections.

Patch

: Editorial corrections.

---

# AI Contribution Policy

AI-generated content should:

- preserve evidence
- avoid inventing citations
- maintain repository terminology
- follow repository templates
- preserve metadata

AI must never remove evidence to improve readability.

---

# Future Extensions

This standard intentionally remains concise.

Additional standards may later define:

- Citation Standard
- Naming Convention
- Review Workflow
- Research Workflow
- Release Process
- Contribution Rules
- Quality Gates

without modifying the core philosophy established by this document.

---

# Closing Statement

The purpose of the **Orden** project is not merely to collect information.

Its purpose is to cultivate a reproducible, evidence-based way of thinking about software architecture, enabling architectural decisions to be examined, challenged and improved through transparent reasoning.