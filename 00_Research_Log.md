---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RD-LOG-001
  title: Research Log
  type: Research Log
  version: 0.6.0
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

## 2026-07-18 — Microsoft Event Types Reference Analysis

**Source claim:** Microsoft distinguishes language and runtime event types from
an extensibility-oriented taxonomy of placements and patterns. Its guidance
addresses contract stability, implementation coupling, multiple subscribers,
unspecified execution order, transactions, error handling, and extension
composition.

**Repository observation:** An event attribute or pattern does not fully state
what a subscriber does to effective behavior. Integration events in particular
can implement operation boundaries, line-level hooks, verification, switching,
skipping, handling, or discovery.

**Interpretation:** Microsoft provides substantial mechanism-specific evidence
for event review, but the examined sources do not combine publisher contract,
runtime semantics, and subscriber behavioral effect into a
mechanism-independent review method.

**Candidate implication:** A future framework may classify event type,
placement pattern, and subscriber effect separately, then review composition,
mutable parameters, responsibility transfer, transaction semantics, and
evolution risk according to demonstrated consequences.

**Status:** Under Investigation

See `References/Microsoft_Event_Types.md` for evidence, limitations, and
unresolved questions.

## 2026-07-18 — Event Guidance Expansion and BCApps Study Protocol

**Source claim:** The Microsoft-layer BCQuality event corpus adds atomic review
guidance for subscriber binding, event contract evolution, error boundaries,
handled control flow, and preservation of critical operations. Selected
ALGuidelines.dev sources add community pattern guidance, while BCApps provides
official source code suitable for empirical observation.

**Repository observation:** These sources have different purposes and authority.
Microsoft Learn documents platform semantics and design guidance, BCQuality
encodes agent-review knowledge, BCApps records implemented product choices, and
ALGuidelines.dev includes community and historical material.

**Interpretation:** Event review may require four separately observed
dimensions: publisher contract, subscriber effect, runtime participation, and
responsibilities that remain effective after participation. The fourth
dimension is especially relevant when handling or skipping default behavior
also suppresses later events, validation, integrity checks, or other work.

**Candidate implication:** Test the dimensions through a predefined,
stratified BCApps repository audit rather than selecting convenient examples or
inferring preferred design from occurrence in shipped code.

**Unresolved tension:** Microsoft Learn's low-value assessment of handled events
coexists with narrowly scoped BCQuality guidance for exposing substitutable
behavior. The contextual boundary has not been established.

**Status:** Under Investigation

See `References/Microsoft_Event_Types.md`,
`Empirical/BCApps_Event_Pattern_Analysis.md`, and
`Ideas/Microsoft_Event_Types_Research_Agenda.md`.
