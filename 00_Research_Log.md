---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RD-LOG-001
  title: Research Log
  type: Research Log
  version: 0.4.0
  status: Active

classification:
  domain: Research
  layer: Project
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records research evolution, hypotheses, rejected directions, terminology
  questions, decisions, and unresolved questions for the Orden project.

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

related_documents:
  - 01_Terminology.md
  - 02_Research_Methodology.md
  - 03_Related_Work.md

tags:
  - research
  - research-log
  - hypotheses
  - decisions
  - open-questions
---

# Research_Log.md

# Purpose

This document is the research backbone of the project. It records
hypotheses, rejected ideas, terminology decisions and open questions. It
is intended for Obsidian and is **not** part of the final whitepaper.

# Principles

-   Record hypotheses before accepting them.
-   Record why hypotheses were rejected.
-   Distinguish observations from conclusions.
-   Separate Business Central observations from general software
    architecture.
-   Reuse existing terminology whenever possible.

# Research Goals

1.  Determine whether a mechanism-independent review methodology already
    exists.
2.  Identify existing terminology before proposing new terminology.
3.  Build a rigorous conceptual foundation.
4.  Derive Business Central guidance from general architectural
    principles.

# Current Working Hypothesis

A significant change to an established effective execution flow may also
modify architectural properties carried by that flow.

Those impacts should be reviewed independently of the mechanism used.

Status: **Open**

# Evolution

## Phase 1 -- Initial Observation

Origin: Business Central IsHandled pattern.

Observation: Subscribers frequently replace standard behavior.

Initial assumption: The main problem is loss of extensibility.

Status: Incomplete.

## Phase 2 -- Broader View

Observation:

-   Interfaces
-   Strategy
-   Workflow
-   Middleware
-   Plugins
-   IsHandled

can all modify established behavior.

Conclusion:

The research subject is behavior-changing customization, not IsHandled
itself.

Status: Accepted.

## Phase 3 -- Execution Flow

Execution Flow and Effective Execution Flow appear useful.

Open question:

Should they be formally defined or mapped to existing literature?

Status: Open.

## Phase 4 -- Review Trigger

Candidate hypothesis:

Architecturally significant behavioral changes should trigger
architectural review.

Status: Open.

# Rejected Directions

## "This is an IsHandled problem."

Rejected because IsHandled is only one implementation mechanism.

## "A completely new architectural entity exists."

Rejected until literature review proves otherwise.

# Terminology Under Investigation

-   Execution Flow
-   Effective Execution Flow
-   Behavior
-   Behavioral Contract
-   Effective Extensibility
-   Architectural Significance
-   Behavioral Change Review
-   Behavioral Change Review Trigger

# Related Work

-   Microsoft Learn
-   AL Guidelines
-   SEI
-   ISO/IEC/IEEE 42010
-   ATAM
-   SAAM
-   DDD
-   Fowler
-   BPM
-   Workflow Systems
-   Plugin Architectures

# BC Evidence Catalogue

Collect examples from:

-   Base Application
-   System Application
-   Localizations
-   Open-source AL repositories

For each example capture:

-   mechanism
-   affected flow
-   architectural consequences
-   review implications

# Open Questions

1.  What is an architecturally significant behavioral change?
2.  Which architectural properties are carried by execution flow?
3.  Which are already documented by Microsoft?
4.  Which remain undocumented?
5.  Can one review framework cover all behavior-changing mechanisms?

# Decisions

## 2026-07-16

Project scope expanded beyond IsHandled because the observed problem is
mechanism-independent.

## 2026-07-18 — ATAM Reference Analysis

**Source claim:** ATAM evaluates the consequences of architectural decisions
against quality-attribute requirements and identifies risks, sensitivity
points, and tradeoff points through prioritized scenarios and stakeholder
analysis.

**Repository observation:** The examined ATAM sources do not define behavioral
change itself as an architecture-evaluation trigger and do not provide a
Business Central-specific review scale.

**Interpretation:** ATAM is evidence for a mechanism-independent method of
evaluating quality-attribute consequences. It reduces the plausible novelty of
Orden to integration and specialization rather than invention of architecture
evaluation.

**Candidate implication:** A future framework may reuse scenario
characterization, architectural-decision analysis, and risk and tradeoff
identification, provided that the adaptation is not represented as a full ATAM
evaluation.

**Status:** Under Investigation

See `References/ATAM.md` for evidence, limitations, and unresolved questions.

## 2026-07-18 — SAAM Reference Analysis

**Source claim:** SAAM uses stakeholder scenarios to evaluate how an
architecture supports current activities and anticipated changes. Indirect
scenarios require architectural changes; interactions among indirect scenarios
help examine separation of concerns relative to the selected scenario classes.

**Repository observation:** The examined SAAM sources do not define behavioral
change itself as a review trigger. Direct and indirect scenarios describe the
relationship between a scenario and a particular architecture, not universal
categories of customizations.

**Interpretation:** SAAM provides established precedent for contextual
change-impact analysis and reduces the plausible novelty of Orden. It does not
cover all quality-attribute consequences or determine when extension work
warrants architecture-level review.

**Candidate implication:** A future framework may reuse scenario development,
support classification, affected-element mapping, and scenario-interaction
analysis, provided that interactions are interpreted by scenario class and
architectural granularity rather than treated as automatic defects.

**Status:** Under Investigation

See `References/SAAM.md` for evidence, limitations, and unresolved questions.
