---
metadata_schema: "1.0"
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: REF-SEI-BEH-001
  title: SEI Documenting Behavior Analysis
  type: Reference Analysis
  version: 0.3.0
  status: Active
classification:
  domain: Software Architecture
  layer: Study
  maturity: Review
owner: Štěpán Dvořák
purpose: >
  Evaluates SEI guidance on architectural behavior and distinguishes behavior
  documentation from evaluation of behavior-changing customizations.
quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft
audience:
  - Researchers
  - Contributors
  - AI Assistants
depends_on:
  - References/ISO_42010.md
  - References/ISO_42020.md
  - References/ISO_42030.md
related_documents:
  - 01_Terminology.md
  - 03_Related_Work.md
evidence:
  source_authority: SEI Publication
  source_access: Partial
  verification: Partial
  limitations: >
    The note summarizes publicly accessible SEI material and does not replace
    verification against the original publications.
tags:
  - reference
  - software-architecture
  - behavior-documentation
  - behavioral-views
  - SEI
---

# SEI_Documenting_Behavior.md

# Purpose

This note evaluates the SEI guidance on documenting software architecture behavior, primarily the
*Documenting Software Architecture: Documenting Behavior* report and the broader *Views and Beyond*
approach.

The objective is to determine:

1. how SEI defines architectural behavior;
2. how behavior should be represented;
3. whether SEI already defines review practices for behavior-changing customizations;
4. what can be reused by the Business Central research project.

> This note summarizes publicly available SEI material and should not be considered a replacement for the original publications.

# Executive Assessment

SEI treats **behavior as an architectural concern**, not merely an implementation detail.

Its primary contribution is **how behavior should be documented** through architectural views and models.

It does **not** appear to define a mechanism-independent trigger for reviewing source-code behavior changes.

Therefore the SEI material complements rather than replaces the proposed framework.

# Position Within Existing Literature

| Source | Primary focus |
|---|---|
| ISO 42010 | Architecture description concepts |
| ISO 42020 | Architecture processes |
| ISO 42030 | Architecture evaluation framework |
| SEI – Documenting Behavior | Behavioral architecture views and documentation |
| Proposed project | Business Central specialization for reviewing behavior-changing customizations |

# Views and Beyond

The central SEI idea is that architecture cannot be represented by one universal diagram.

Instead it is documented using multiple complementary views.

Behavior is therefore **one architectural view among several**, not the architecture itself.

## Research implication

This strongly supports treating Execution Flow as one possible **behavior model**, not as the definition of architecture.

# What SEI Means by Behavior

Across the Views and Beyond literature, behavior generally describes the observable runtime interaction of architectural elements.

Typical concerns include:

- ordering
- interaction
- message exchange
- synchronization
- concurrency
- sequencing
- state evolution
- externally visible effects

## Important observation

Behavior is discussed at an architectural level.

The emphasis is not on individual methods or algorithms but on interactions between architectural elements.

# Recommended Behavioral Representations

SEI discusses several complementary modeling techniques.

Typical examples include:

- sequence diagrams
- state-machine models
- activity diagrams
- interaction scenarios
- message-flow models
- timing-oriented representations (where appropriate)

No single notation is presented as universally correct.

## Research implication

The future Business Central framework should not require one mandatory notation.

Instead it should define which architectural questions each model answers.

# Documentation Rather Than Evaluation

The strongest conclusion from the SEI material is the distinction between:

- documenting behavior;
- evaluating architectural consequences of behavior changes.

SEI primarily addresses the first problem.

Our project investigates the second.

# Mapping to Business Central

Possible architectural behavior views include:

- posting pipeline
- event participation
- extension interaction
- interface delegation
- transaction boundaries
- replacement responsibility
- workflow interaction

These are behavior views, not implementation listings.

# Relationship to Execution Flow

Earlier project hypothesis:

Execution Flow might represent a new architectural entity.

Current assessment after ISO + SEI:

Execution Flow is better interpreted as:

- a behavior model;
- or one model kind within a Behavior View.

This is more consistent with existing literature.

# Effective Execution Flow

The project still distinguishes:

Execution Flow
: intended logical progression.

Effective Execution Flow
: runtime path actually taken.

SEI discusses runtime behavior and scenarios but does not appear to introduce this exact terminology.

Therefore the term remains a **candidate project abstraction**, pending further literature review.

# Architectural Concerns Addressed by Behavior Views

Behavior views commonly help reason about:

- correctness
- interaction
- ordering
- synchronization
- responsibility
- failure propagation
- concurrency
- externally visible effects

Business Central adds additional domain concerns:

- posting integrity
- localization correctness
- extension composability
- transaction semantics
- effective extensibility
- upgrade compatibility

# What SEI Does Not Provide

Publicly available material does not appear to define:

- a review trigger;
- proportional review levels;
- Business Central extensibility guidance;
- IsHandled alternatives;
- architectural review checklists for code changes.

These remain potential contributions of the project.

# Candidate Contribution After SEI Review

The project should avoid claiming:

> "Behavior has not been recognized by software architecture."

Instead it should claim:

> "Behavior is already recognized and documented as an architectural view. This project investigates when significant behavior-changing customizations should trigger architecture evaluation in Business Central and how such reviews can be performed consistently."

# Relationship to ISO Standards

The documents now appear complementary.

ISO 42010
: describes architecture description.

ISO 42020
: describes architecture processes.

ISO 42030
: describes architecture evaluation.

SEI
: explains practical architectural documentation of behavior.

The remaining project gap is therefore increasingly narrow and better defined.

# Counterarguments

## Existing architecture teams may already perform such reviews

True.

The project must demonstrate added value specifically for Business Central development teams.

## Behavior documentation may already be sufficient

Possibly for some systems.

However, documenting behavior is not identical to deciding when behavior changes deserve review.

## Execution Flow terminology may be unnecessary

Still possible.

The project should retain existing terminology whenever adequate.

# Findings

## Accepted

Behavior is an architectural concern.

## Accepted

Behavior should be documented through dedicated architectural views and models.

## Accepted

Execution Flow is probably a behavior model rather than a new architectural entity.

## Open

Is Effective Execution Flow a useful specialization or an unnecessary new term?

## Open

What objective criteria should trigger architecture evaluation after behavior changes?

# Impact on Project Documents

## 01_Terminology

Strengthen:

- Behavior
- Behavior View
- Behavior Model

Downgrade emphasis on Execution Flow as a central concept.

## 03_Related_Work

Add SEI as primary evidence that architectural behavior documentation already exists.

## Whitepaper

Shift emphasis from inventing concepts toward integrating:

- architecture description;
- architecture process;
- architecture evaluation;
- behavior documentation;
- Business Central operational guidance.

# References

Primary SEI resources:

- Documenting Software Architecture: Documenting Behavior.
- Views and Beyond collection.
- Software Engineering Institute (Carnegie Mellon University).

# Source Limitations

This draft is based on publicly available SEI descriptions and the documented Views and Beyond approach.

Full publication analysis should be performed before quoting detailed definitions.

# Revision History

## 0.2

Expanded analytical draft following review of ISO 42010/42020/42030.
