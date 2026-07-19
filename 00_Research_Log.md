---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RD-LOG-001
  title: Research Log
  type: Research Log
  version: 0.12.0
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

## 2026-07-18 — Behavioral Change Impact Review Pilot Pre-registration

**Candidate working definition:** Behavioral Change Impact Review is a review
initiated when a customization materially augments, redirects, suppresses,
replaces, reorders, or delegates established behavior or execution
responsibility.

**Operational assumption:** For the pilot, a change is material when available
evidence indicates that it can alter an observable outcome, side effect,
invariant, responsibility, interaction, failure mode, or quality-relevant
execution property. This is a coding rule, not canonical terminology.

**Candidate checklist:** Review affected flow, change type, outcomes,
invariants, ordering and transaction semantics, integration and extensibility,
observability, failure behavior, ownership, and evolution. Extensibility is one
possible impact rather than the name or complete scope of the review.

**Empirical decision:** Begin with a bounded 16-case pilot in Microsoft's Core
Localization Pack for Czech application at BCApps commit
`397d01199c321e774edaf23a7290fee40f75c6a6`. Freeze selection rules before case
classification, disclose prior case knowledge, and include negative controls
and uncertain cases.

**Uncertainty:** The trigger, materiality rule, checklist, event-evidence
dimensions, and their mapping remain candidates. The pilot may refine or reject
them and cannot establish defect prevalence.

**Status:** Under Investigation; pilot execution pending

See `Empirical/BCApps_Event_Pattern_Analysis.md` and
`Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md`.

## 2026-07-18 — BCApps Czech Subscriber Population Reproduction

**Repository observation:** A deterministic lexical extraction at the fixed
BCApps commit reproduced 448 event-subscriber attributes in 116 of 782 AL files
within the Core Localization Pack for Czech production-source boundary.

**Interpretation:** The retained rows provide a stable syntactic candidate
frame for later coarse screening. They are not independent behavioral cases and
do not demonstrate trigger satisfaction, runtime participation, or defects.

**Method decision:** Preserve each detected attribute with a stable inventory
ID, source identity, subscriber and publisher arguments, signature markers,
and explicit `Unknown`, `Not Screened`, and `Unselected` workflow states.

**Deferred work:** Publisher declarations, binding calls, other discovery
markers, prior-knowledge labeling, coarse screening, and case selection remain
open. No `CZP` case was selected or classified during population extraction.

**Status:** Subscriber population reproduced; discovery incomplete

See `Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md`.

## 2026-07-18 — BCApps Czech Discovery-Marker Reproduction

**Repository observation:** The fixed production boundary contains 289
integration-event publisher declarations and no detected business-event or
internal-event declarations. Mechanical discovery also retained 8 manual
subscriber-instance declarations, 9 bind calls, 7 unbind calls, 148 mutable
control-name parameters, 19 commit calls, 16 try-function attributes, 20
obsolete attributes, and 21 subscriber targets with bounded syntactic
multiplicity.

**Interpretation:** These occurrences identify source context for coarse
screening. Their presence does not demonstrate runtime participation,
interaction, behavioral change, architectural impact, or defect.

**Method decision:** Preserve raw occurrences and explicit nonsemantic statuses
before screening. Do not use a marker as an automatic selection rule.

**Deferred work:** Resolve evidence availability during coarse screening and
obtain reviewer prior-knowledge labels before assigning selection buckets. No
case, trigger result, impact, or framework implication was recorded.

**Status:** Withdrawn on 2026-07-19; not valid for screening or selection

See `Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md`.

## 2026-07-19 — BCApps Czech Discovery-Scope Correction

**Contradicting observation:** The application-wide marker inventory included
mutable control parameters declared by CZL integration-event publishers. Such
rows described publisher contracts or ordinary CZL implementation details, not
CZL subscribers extending or deviating from behavior supplied by a dependency.

**Interpretation:** The discovery procedure changed the unit of analysis from a
CZL event subscriber to any selected lexical occurrence in CZL. Its publisher,
marker, and multi-target datasets therefore cannot support the intended coarse
screen or case selection, even though their raw occurrence counts were
reproducible.

**Corrective decision:** Retain the 448 CZL event-subscriber rows as the sole
candidate population and retain the 782-file boundary inventory. Remove the
invalid second extractor and its three outputs. Resolve publisher, raise-site,
established-flow, binding, composition, and test context only in relation to a
specific retained subscriber.

**Dependency boundary:** Use the fixed CZL source, its explicit `EU 3-Party
Trade Purchase` dependency, and the dependency closure represented by
`application` version `29.0.0.0` at the same BCApps commit. Record the exact
source application or platform-event classification for each resolution rather
than assuming current packaging.

**Deferred work:** Define and validate the dependency-aware subscriber-context
resolver before coarse screening. Prior-knowledge labeling, `CZP` selection,
trigger classification, checklist analysis, and framework implications remain
unperformed.

**Status:** Method corrected; subscriber-context resolution pending

See `Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md` and
`Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md`.

## 2026-07-19 — BCApps Czech Dependency Boundary and Context Protocol

**Source claim:** Microsoft documents `application` as a dependency on the
Application app and distinguishes application, business, integration, internal,
trigger, and platform events. The fixed BCApps manifests expose the CZL subject,
its EU 3-Party Trade Purchase dependency, Base Application, Business Foundation,
and System Application source at the selected commit.

**Repository observation:** The retained population has 448 subscriber rows,
but it does not identify publisher declarations, raise sites, binding mode,
subscriber-local effects, or runtime participation for those rows.

**Interpretation:** The five applications form a reproducible source search
boundary for this pilot. They must not be represented as a verified copy of the
complete distributed Application package or as a complete runtime closure.

**Method decision:** Require exactly one context record per retained `CZPOP`
row. Resolve target event class, publisher source, raise-site evidence,
subscriber-local mechanics, and bounded runtime/composition evidence while
preserving explicit unresolved states and source locations. Freeze workflow
fields as `Unknown`, `Not Screened`, and `Unselected`.

**Deferred work:** Implement and technically validate the resolver, then create
448 context records. Coarse screening, prior-knowledge labeling, `CZP` case
selection, trigger classification, and checklist analysis remain unperformed.

**Status:** Dependency boundary and resolution protocol fixed; execution pending

See `Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md`.

## 2026-07-19 — BCApps Czech Context Resolver Technical Validation

**Repository observation:** The bounded resolver processed all 448 retained
subscriber identities in a non-retained dry run. It returned 339 dependency
source publishers, 4 subject-application publishers, and 105 recognized
database or page trigger events. The deterministic validation rule retained
the first Integration Event, Database Trigger Event, and Page Trigger Event
records. No non-success status occurred in the fixed population dry run.

**Interpretation:** These counts describe static resolver output, not evidence
availability, runtime participation, behavioral change, impact, quality, or
defects. Successful static resolution does not establish semantic completeness.

**Method decision:** Retain only the three technical-validation records, with
no `CZP` IDs. Use synthetic regression fixtures to exercise ambiguous and
missing-source failure paths without adding them to the empirical population.
Keep workflow values fixed as `Unknown`, `Not Screened`, and `Unselected`.

**Validation:** Two executions produced byte-identical JSON Lines output; all
three records passed the context schema; focused failure-path tests passed; and
an AI-assisted source comparison found no mismatch in the retained records.

**Deferred work:** Owner review of all three records remains required by the
protocol. Full 448-record context generation, coarse screening,
prior-knowledge labeling, `CZP` selection, and impact analysis remain
unperformed.

**Status:** Automated technical validation passed; owner review pending

See `Empirical/BCApps_CZ_Subscriber_Context_Technical_Validation.md`.
