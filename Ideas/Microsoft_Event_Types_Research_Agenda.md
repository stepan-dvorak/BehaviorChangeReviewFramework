---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RD-IDEA-EVENTS-001
  title: Microsoft Event Types Research Agenda
  type: Research Agenda
  version: 0.1.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Idea
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Preserves non-canonical hypotheses, source tensions, candidate models, and
  future research branches discovered while extending the Microsoft event
  types analysis.

quality:
  review: Self Reviewed
  evidence: Partial
  editorial: Reviewed

audience:
  - Researchers
  - Contributors
  - AI Assistants

depends_on:
  - References/Microsoft_Event_Types.md

related_documents:
  - Empirical/BCApps_Event_Pattern_Analysis.md
  - References/Microsoft_IsHandled_v2.0.md
  - References/Microsoft_Interfaces.md
  - References/SAAM.md
  - References/ATAM.md

tags:
  - ideas
  - research-agenda
  - events
  - runtime-participation
  - responsibility-preservation
  - source-tension
---

# Microsoft Event Types Research Agenda

## 1. Status and Use

This is a non-canonical Ideas artifact. It preserves directions that are not
ready for the terminology document, framework, or accepted conclusions.

The contents may guide research and case selection. They must not be retrieved
as Microsoft guidance, validated findings, or normative review rules.

## 2. Inputs Preserved

The agenda was assembled from:

- verified Microsoft Learn event documentation;
- Microsoft-layer BCQuality event-review files;
- the public scope of the Microsoft BCApps repository;
- selected community guidance in ALGuidelines.dev;
- repository interpretation developed in
  `References/Microsoft_Event_Types.md`; and
- four AI-generated Business Central pattern inventories supplied as discovery
  aids.

The AI-generated inventories are not evidence. They are retained only through
the questions and candidate searches they prompted. Their broad pattern lists,
recommendations, and claimed sources require independent verification.

## 3. Candidate Multidimensional Model

One event participation case may require at least four separately recorded
dimensions:

1. **Publisher contract:** event attribute or runtime source, accessibility,
   signature, attribute flags, and intended stability.
2. **Subscriber effect:** notification, augmentation, validation, mutation,
   suppression, substitution, selection, or another observed effect.
3. **Runtime participation:** static or manual binding, activation site,
   instance lifetime, session scope, permissions, licensing, and ordering.
4. **Preserved responsibility:** default work, later events, validation,
   integrity, permissions, telemetry, transaction behavior, and error
   propagation that remain effective after participation.

This is a candidate analytical model, not approved terminology. Existing
architecture, plugin, control-flow, and responsibility concepts must be
researched before new repository terms are introduced.

## 4. Source Tensions to Preserve

### 4.1 Handled events

- Microsoft Learn assigns handled events low value and emphasizes poor
  scalability, single-handler convention, hidden control flow, and event-chain
  disruption.
- BCQuality includes a positive rule for an `IsHandled` seam when AL code must
  expose genuine substitution of default behavior.
- Other BCQuality files constrain that seam by excluding critical operations,
  preserving paired `OnAfter` behavior, resetting flags, and protecting shipped
  contracts.
- Some community and AI-generated guidance describes handled events too
  broadly as a default extensibility mechanism.

Research question: can a bounded substitution case be defined without turning
an exception into a general recommendation?

### 4.2 Static, manual, and single-instance subscribers

- Microsoft documentation defines static and manual subscriber lifetimes.
- BCQuality recommends deliberate selection and warns about leaked bindings.
- ALGuidelines.dev includes performance-motivated `SingleInstance` advice but
  also acknowledges shared session state.
- AI-generated guidance warned against using `SingleInstance` as a dependency
  injection container.

Research question: which concerns belong to participation, state ownership,
performance, testing, or architecture, and which combinations create material
review risks?

### 4.3 Implemented code versus recommended design

BCApps can show that a mechanism exists in shipped Microsoft code. It cannot by
itself show that the mechanism is preferred for new development, universally
safe, or representative of the ecosystem.

Research question: what additional evidence is required to move from an
implementation observation to design guidance?

## 5. Candidate Research Branches

### 5.1 Event contract evolution

Investigate compatibility across:

- business, integration, and internal event attributes;
- publisher procedure access modifiers;
- parameter names, types, subtypes, order, and `var` modes;
- added parameters and external publisher callers;
- `IncludeSender`, `GlobalVarAccess`, and `Isolated`; and
- deprecation, replacement, and parallel event versions.

This branch should reconcile Microsoft Learn, AppSourceCop rules, BCQuality,
and representative source changes.

### 5.2 Runtime participation model

Investigate whether established terminology can represent:

- always-bound and manually activated subscribers;
- multiple bound instances of one subscriber codeunit;
- local, global, and `SingleInstance` lifetimes;
- session boundaries;
- missing-license and missing-permission behavior;
- test-only binding and mocks; and
- unspecified ordering among active subscribers.

The goal is evidence collection, not immediate creation of a framework model.

### 5.3 Responsibility preservation

Test cases in which a subscriber suppresses or replaces default behavior while
the publisher may still own:

- paired `OnAfter` publication;
- validation and authorization;
- posting and ledger integrity;
- number-series consumption;
- telemetry and audit evidence;
- transaction completion or rollback; and
- downstream extension points.

Research should determine whether established responsibility, obligation,
postcondition, invariant, or middleware terminology already covers the
phenomenon.

### 5.4 Error and transaction boundaries

Compare ordinary, isolated, and `TryFunction`-bounded events. Include external
side effects, mutable parameters, single-instance state, partial commits,
subscriber errors, continuation, and installation or upgrade contexts.

Quality-specific conclusions should remain in dedicated transaction,
reliability, observability, and upgrade-compatibility research.

### 5.5 Performance and event granularity

Investigate event publication inside loops, generic record-trigger
subscriptions, bulk-operation degradation, subscriber initialization cost,
and the difference between an operation boundary and a line-level hook.

Presence of a potential multiplier should initiate measurement or scoped
analysis, not an automatic performance finding.

### 5.6 Event Bridge and interfaces

Test whether a dedicated event-publisher codeunit preserves a useful contract
across interface implementations. Compare it with events published by each
implementation and with an explicit interface-level orchestration boundary.

Coordinate this branch with future development of
`References/Microsoft_Interfaces.md` to avoid duplicating interface research.

### 5.7 Pattern provenance and obsolescence

Trace discovery, observer, hooks, handled, switch, skip, verify, collector, and
registration patterns across NAV, AL, Microsoft Learn, ALGuidelines.dev,
BCQuality, and BCApps.

The purpose is to distinguish current mechanisms, historical patterns,
community labels, and obsolete designs. A comprehensive pattern catalog should
not be added to the event-types reference unless it directly answers the
reference research question.

### 5.8 Review entry and proportionality

Determine which event facts merely describe mechanism and which provide
evidence that architecture-level review may be proportionate. Keep this work
separate from consequence analysis and coordinate it with the ATAM, SAAM, and
ISO 42030 research.

## 6. Candidate BCApps Case Strata

The empirical study should seek cases from:

- application foundations and core layers;
- first-party integrations;
- posting and validation;
- localizations;
- external or business events;
- manually bound production and test subscribers;
- event-driven discovery or registration;
- interface implementations with shared events;
- trigger-event subscribers; and
- obsolete compatibility paths as a separate comparison class.

This list is a sampling aid. It does not assert that every stratum contains a
case or that selected cases represent prevalence.

## 7. AI-Generated Pattern Inventory Triage

The supplied inventories suggested many patterns beyond event types. They
should be routed as follows:

| Candidate | Research route |
|---|---|
| Observer, publish-subscribe, before/after, verify, switch, skip, handled, discovery | Event reference or BCApps empirical study after verification |
| Strategy, enum implementation, provider, factory, resolver | Microsoft Interfaces research |
| Pipeline, chain of responsibility, template method, command | Workflow, plugin, or general architecture related work |
| Adapter, facade, bridge, anti-corruption layer | Architecture and integration related work |
| State machine, rules engine, specification | Workflow, BPM, or domain-design research |
| Queue and outbox | Integration and distributed-systems research |
| Feature toggles and configuration | Review-entry and runtime-participation research |
| Companion tables, table extensions, page extensions | Data and UI extensibility research, outside this event reference |

This routing prevents the Microsoft event-types reference from becoming an
unbounded Business Central pattern catalog.

## 8. Questions That Should Not Be Lost

1. Can multiple subscriber effects be composed safely without relying on
   execution order?
2. When does a mutable parameter constitute collaboration, implicit return,
   shared control state, or responsibility transfer?
3. Can SAAM scenario interaction identify event-composition risk, or is a
   runtime participation model additionally required?
4. Which event facts should trigger deeper review, and which are only context?
5. How should test-only manual subscribers influence conclusions about
   production architecture?
6. Can event contracts remain stable across interface implementation changes?
7. How should failed subscribers and external side effects be represented when
   rollback semantics differ?
8. Which guidance conflicts are version differences, purpose differences, or
   genuine disagreements?
9. Which candidate categories remain usable when the mechanism changes from an
   event to an interface, workflow, delegate, or plugin?
10. What evidence would falsify the proposed multidimensional model?

## 9. Promotion Criteria

An item may leave this Ideas artifact only when:

- its source authority and access are recorded;
- source claims are separated from repository interpretation;
- relevant counterevidence is preserved;
- terminology has been checked against existing literature;
- empirical claims have a reproducible method; and
- the destination artifact has a clear, non-duplicative responsibility.

Promotion does not imply acceptance into the final framework.

## 10. Revision History

### 0.1.0 — 2026-07-18

- Preserved the candidate multidimensional event model and source tensions.
- Routed broader AI-generated pattern suggestions to appropriate future
  research areas.
- Recorded BCApps sampling candidates, unresolved questions, and promotion
  criteria without establishing conclusions.
