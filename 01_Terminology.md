---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: TR-001
  title: Working Terminology
  type: Terminology
  version: 0.2.0
  status: Active

classification:
  domain: Terminology
  layer: Project
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Defines the project's working terminology and records the validation status,
  boundaries, relationships, and open questions associated with each term.

quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft

audience:
  - Researchers
  - Contributors
  - AI Assistants

depends_on:
  - 00_Research_Log.md

related_documents:
  - Terminology_Index.md
  - 02_Research_Methodology.md
  - 03_Related_Work.md

tags:
  - terminology
  - behavior
  - execution-flow
  - architectural-significance
  - candidate-concepts
---

# 01_Terminology.md

# Purpose

This document defines the project's working terminology.

**Important:** These are research definitions, not final definitions.
Every term may evolve as the literature review progresses.

Each term records:

-   Working definition
-   What it is not
-   Relationship to other terms
-   Current research status

------------------------------------------------------------------------

# Status Legend

-   **Existing** -- Established terminology in software engineering.
-   **Adapted** -- Existing term used with project-specific precision.
-   **Candidate** -- Working term requiring validation.
-   **Rejected** -- No longer considered suitable.

------------------------------------------------------------------------

# Behavior

**Status:** Existing

## Working definition

The externally observable effects produced by a software system.

## Not

-   Source code
-   Control flow
-   Algorithm
-   Business process

## Notes

Behavior may be realized by many different implementations.

------------------------------------------------------------------------

# Execution Flow

**Status:** Candidate

## Working definition

The logical progression of execution intended by a software design.

It describes how execution may proceed through cooperating behavioral
units.

## Not

-   Call stack
-   Sequence diagram
-   Single runtime execution
-   Business workflow

## Open questions

-   Is an existing term already sufficient?
-   Is this merely a view of behavior?

------------------------------------------------------------------------

# Effective Execution Flow

**Status:** Candidate

## Working definition

The concrete execution path selected during a particular execution
according to runtime conditions.

## Relationship

Execution Flow → many possible paths

Effective Execution Flow → one realized path

## Open questions

Should this map directly to existing concepts such as execution trace?

------------------------------------------------------------------------

# Behavioral Change

**Status:** Adapted

## Working definition

Any customization that intentionally changes an established behavior.

Behavioral changes may:

-   augment,
-   suppress,
-   substitute,
-   reorder,
-   delegate,
-   intercept behavior.

------------------------------------------------------------------------

# Architectural Significance

**Status:** Candidate

## Working definition

A behavioral change is architecturally significant when its consequences
extend beyond local implementation details.

Possible indicators include effects on:

-   contracts,
-   invariants,
-   transactions,
-   security,
-   extensibility,
-   observability,
-   upgrade compatibility.

## Open question

Can this be objectively identified?

------------------------------------------------------------------------

# Behavioral Contract

**Status:** Existing

## Working definition

The observable expectations associated with a behavior.

Examples:

-   expected outcomes
-   side effects
-   guarantees
-   constraints

------------------------------------------------------------------------

# Extensibility

**Status:** Existing

## Working definition

The ability of software to be extended without modifying existing
implementations.

## Notes

The project intentionally distinguishes extensibility from effective
participation in modified behavior.

------------------------------------------------------------------------

# Effective Extensibility

**Status:** Candidate

## Working definition

The practical ability of another customization to participate
meaningfully in the effective execution flow.

## Motivation

An extension point may remain technically available while no longer
influencing relevant behavior.

## Open question

Does existing literature already describe this concept?

------------------------------------------------------------------------

# Behavioral Change Review

**Status:** Candidate

## Working definition

A mechanism-independent architectural review performed after an
architecturally significant behavioral change.

## Goal

Review consequences rather than implementation technique.

------------------------------------------------------------------------

# Behavioral Change Review Trigger

**Status:** Candidate

## Working definition

A condition indicating that a behavioral modification should initiate
architectural review.

## Open question

Is execution-flow modification the trigger, or only one observable
symptom?

------------------------------------------------------------------------

# Relationships

Behavior ├── Execution Flow (candidate) │ └── Effective Execution Flow
(candidate) ├── Behavioral Contract ├── Behavioral Change │ └──
Behavioral Change Review └── Extensibility └── Effective Extensibility
(candidate)

------------------------------------------------------------------------

# Terms Explicitly Avoided

At the current stage the project intentionally avoids introducing new
umbrella terms unless existing terminology proves insufficient.

------------------------------------------------------------------------

# Open Terminology Questions

1.  Can Execution Flow be mapped to an established architectural term?
2.  Is Effective Execution Flow equivalent to execution trace?
3.  Is Effective Extensibility already defined elsewhere?
4.  What distinguishes behavior from orchestration?
5.  What distinguishes behavioral change from implementation change?

------------------------------------------------------------------------

# Revision History

## 0.1

Initial working terminology derived from early research discussions.
