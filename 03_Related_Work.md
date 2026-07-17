---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RW-001
  title: Related Work
  type: Related Work
  version: 0.2.0
  status: Active

classification:
  domain: Research
  layer: Project
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Surveys existing bodies of knowledge to identify reusable concepts,
  established terminology, and research gaps relevant to the Orden project.

quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft

audience:
  - Researchers
  - Contributors
  - AI Assistants

depends_on:
  - 00_Project_Charter.md
  - 00_Research_Log.md
  - 01_Terminology.md
  - 02_Research_Methodology.md

related_documents:
  - References/ISO_42010.md
  - References/ISO_42020.md
  - References/ISO_42030.md
  - References/SEI_Documenting_Behavior.md
  - References/Microsoft_Extensibility_Overview.md

tags:
  - research
  - related-work
  - literature-review
  - research-gap
  - architecture
---

# 03_Related_Work.md

# Purpose

This document surveys existing bodies of knowledge that may already
describe the phenomenon investigated by this project.

The objective is **not** to prove originality.

The objective is to determine:

-   what already exists,
-   under which terminology,
-   what can be reused,
-   what appears to remain uncovered.

------------------------------------------------------------------------

# Research Strategy

Every candidate field is evaluated using four questions.

1.  Which concepts resemble the observed phenomenon?
2.  Which terminology is already established?
3.  Which parts can be reused without modification?
4.  What remains outside the documented scope?

No new terminology should be introduced before completing this review.

------------------------------------------------------------------------

# Candidate Domains

## Software Architecture

### Existing concepts

Potentially relevant:

-   Architectural decisions
-   Quality attributes
-   Architectural views
-   Behavioral architecture
-   Architecture evaluation (ATAM, SAAM)

### Observations

Architecture literature clearly recognizes that behavior is part of
software architecture.

Architecture reviews already evaluate changes affecting quality
attributes.

### Open question

Do existing architecture review methods define behavior modification
itself as a review trigger?

Status: Open.

------------------------------------------------------------------------

## Software Design

Potentially relevant:

-   Design Patterns (GoF)
-   Refactoring
-   SOLID
-   Dependency Injection
-   Strategy
-   Template Method

### Observations

These explain *how* behavior can be varied.

They do not appear to define a mechanism-independent review methodology
for behavior-changing customizations.

Status: Under investigation.

------------------------------------------------------------------------

## Domain-Driven Design

Potentially relevant:

-   Domain behavior
-   Invariants
-   Aggregate consistency
-   Domain events

### Observations

DDD provides rich guidance about preserving business correctness.

Open question:

Does DDD address architectural review of behavior modification itself?

Status: Open.

------------------------------------------------------------------------

## Workflow Systems & BPM

Potentially relevant:

-   Process modification
-   Orchestration
-   Compensation
-   State transitions

### Observations

Workflow literature studies process evolution extensively.

However, it usually assumes the workflow itself is the primary artifact.

Business Central customizations frequently modify behavior without
introducing explicit workflow definitions.

Status: Under investigation.

------------------------------------------------------------------------

## Plugin & Framework Architecture

Potentially relevant:

-   Extension points
-   Hooks
-   Plugins
-   Middleware
-   Inversion of Control

### Observations

These domains provide guidance for designing extensible systems.

Open question:

Do they define a review methodology once an extension changes
established platform behavior?

Status: Open.

------------------------------------------------------------------------

## Microsoft Business Central

Relevant sources include:

-   Microsoft Learn
-   AL Guidelines
-   Base Application
-   System Application
-   Microsoft localizations

### Initial observations

Microsoft documents:

-   extensibility mechanisms,
-   event taxonomy,
-   interface usage,
-   IsHandled limitations,
-   event quality,
-   minimum requirements.

Open question:

Does existing guidance integrate these topics into a single review
methodology?

Current assessment:

No explicit mechanism-independent framework has yet been identified.

Status: Under investigation.

------------------------------------------------------------------------

# Preliminary Comparison

  Domain                      Behavior   Extensibility   Review    Gap to investigate
  --------------------------- ---------- --------------- --------- ------------------------------
  Software Architecture       ✓          Partial         ✓         Review trigger
  Design Patterns             ✓          ✓               Limited   Mechanism-independent review
  DDD                         ✓          Partial         Partial   Architectural consequences
  Workflow/BPM                ✓          Limited         ✓         Non-workflow customizations
  Plugin Architecture         ✓          ✓               Limited   Behavioral review
  Business Central Guidance   ✓          ✓               Partial   Unified methodology

------------------------------------------------------------------------

# Working Assessment

Current evidence suggests that:

-   the individual concepts already exist,
-   multiple review practices already exist,
-   Business Central already documents many mechanism-specific
    recommendations.

The potential contribution of this project therefore appears to be
**integration**, not invention.

This conclusion remains provisional until the literature review is
completed.

------------------------------------------------------------------------

# Evidence Collection Plan

For every candidate source record:

-   citation
-   relevant terminology
-   reusable concepts
-   conflicting concepts
-   remaining gaps

Each finding should be linked from this document to detailed notes
stored under the References folder.

------------------------------------------------------------------------

# Open Questions

1.  Is there already a recognized term equivalent to "Behavioral Change
    Review"?
2.  Is "Execution Flow" an existing architectural concept under another
    name?
3.  Which architecture review methods are explicitly triggered by
    behavioral change?
4.  Can Business Central guidance be viewed as a specialization of
    existing architecture practices?

------------------------------------------------------------------------

# Revision History

## 0.1

Initial survey structure created before detailed literature analysis.
