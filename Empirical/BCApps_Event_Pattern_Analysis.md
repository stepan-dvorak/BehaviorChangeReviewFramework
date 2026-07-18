---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-EVENTS-001
  title: BCApps Event Pattern Analysis
  type: Empirical Study Protocol
  version: 0.1.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Defines a reproducible repository-code audit for testing the candidate event
  classification and review concerns against representative Microsoft BCApps
  publishers and subscribers without treating implemented patterns as
  automatically preferred designs.

quality:
  review: Self Reviewed
  evidence: Pending
  editorial: Reviewed

audience:
  - Researchers
  - Business Central Architects
  - Contributors
  - AI Assistants

depends_on:
  - 02_Research_Methodology.md
  - References/Microsoft_Event_Types.md

related_documents:
  - References/Microsoft_IsHandled_v2.0.md
  - References/Microsoft_Interfaces.md
  - References/SAAM.md
  - References/ATAM.md
  - Ideas/Microsoft_Event_Types_Research_Agenda.md

study:
  method: Planned Stratified Repository Code Audit
  subject: Microsoft BCApps repository event publishers and subscribers
  data_access: Public GitHub Repository
  reproducibility: Protocol Defined; Execution Pending

tags:
  - empirical-study
  - BCApps
  - events
  - event-subscribers
  - source-code-audit
  - study-protocol
---

# BCApps Event Pattern Analysis

## 1. Study Status

This artifact is an empirical study protocol. The study has not yet been
executed, no cases have been classified, and no empirical findings are
available. Its purpose is to preserve the intended method before code examples
are selected so that selection does not follow a preferred conclusion.

The protocol may be refined during a pilot. Any material change to sampling,
classification, or exclusion criteria must be recorded before the main sample
is evaluated.

## 2. Objective

Test whether the event dimensions proposed in
`References/Microsoft_Event_Types.md` can describe representative Microsoft
Business Central application cases consistently and whether additional runtime
participation or responsibility-preservation evidence is required.

The study is not intended to rank all BCApps code, measure Microsoft-wide
quality, or infer that a pattern is recommended merely because it is present.

## 3. Research Questions

1. Can event publisher type, extension-point pattern, subscriber effect,
   runtime participation, and preserved responsibility be classified
   independently and consistently?
2. Which event characteristics expose architecturally relevant consequences
   that are not visible from the AL event attribute alone?
3. How do multiple subscribers, mutable parameters, `IsHandled` or skip flags,
   manual binding, and error boundaries affect effective participation?
4. Which cases exhibit interaction between extensions or application modules,
   and can SAAM-style scenario interaction describe that interaction without a
   separate runtime model?
5. Which cases provide counterexamples to the candidate classifications or
   implications in the reference analysis?

## 4. Data Source and Baseline

The study subject is the public `microsoft/BCApps` GitHub repository. The
planning baseline verified on July 18, 2026, was commit
`397d01199c321e774edaf23a7290fee40f75c6a6` [B1].

Before execution, the researcher must either:

- retain this commit as the fixed study baseline; or
- record a newer immutable commit and explain why the baseline changed.

Branch names alone are insufficient for reproducibility. Source paths, commit
identifiers, and relevant line or symbol locations must be recorded for every
selected case.

## 5. Unit of Analysis

The primary unit is an **event participation case**, consisting of:

- the publisher declaration;
- the raise site and surrounding control flow;
- one selected subscriber;
- any activation or binding site required for that subscriber to participate;
- downstream default work and events affected by participation; and
- tests or callers needed to interpret observable behavior.

A publisher or subscriber in isolation is insufficient when its effect depends
on surrounding control flow. Multiple subscribers to the same event may be
grouped as a composition case while retaining separate subscriber records.

## 6. Sampling Strategy

### 6.1 Population discovery

Create a machine-generated inventory of relevant AL declarations and calls,
including at minimum:

- `[BusinessEvent]`, `[IntegrationEvent]`, and `[InternalEvent]` publishers;
- `[EventSubscriber]` methods;
- database and page trigger subscribers;
- `BindSubscription` and `UnbindSubscription` calls;
- `EventSubscriberInstance` values;
- event parameters containing `IsHandled`, `Handled`, `Skip`, or mutable
  records and values; and
- isolated event declarations.

The inventory script, command, tool version, and raw counts must be retained or
recorded so another reviewer can reproduce the candidate population.

### 6.2 Strata

The sample should cover, when available:

- System Application;
- Business Foundation;
- Base Application or application layers;
- first-party worldwide apps;
- at least one localization;
- production code and test-support code as separate strata;
- business, integration, internal, and runtime trigger events;
- notification or augmentation, validation, mutation, suppression,
  substitution, selection, and discovery effects;
- static and manual subscribers;
- ordinary, isolated, and `TryFunction`-bounded execution; and
- single-subscriber and multi-subscriber cases.

### 6.3 Selection

Use a two-stage selection:

1. Select cases purposively to ensure every available stratum has at least one
   pilot example.
2. Select additional cases from the generated population using a recorded
   deterministic or random method.

Purely convenient or visually interesting examples may be used for pilot
calibration but must not be represented as prevalence evidence.

## 7. Inclusion and Exclusion Criteria

Include a case when the required publisher, raise site, subscriber, and
relevant control-flow context are available at the fixed commit.

Record but analyze separately:

- obsolete compatibility code;
- test-only mocks and handlers;
- localization-specific behavior;
- generated code; and
- code whose publisher is outside the selected repository baseline.

Exclude a case from consequence analysis when essential dependencies are
unavailable. The exclusion and its reason remain part of the study record.

## 8. Classification Record

Each case should record:

| Field | Required observation |
|---|---|
| Identity | Commit, source paths, symbols, and application layer |
| Publisher type | Business, integration, internal, global, database trigger, or page trigger |
| Extension-point pattern | Operation boundary, procedure boundary, line hook, verify, isolated, switch, skip, handled, discovery, or unclassified |
| Subscriber effect | Notify, augment, validate, mutate, suppress, substitute, select, or other observed effect |
| Participation | Static or manual binding, activation site, lifetime, session scope, and unbinding |
| Mutable influence | `var` records, flags, return surrogates, or shared state |
| Default behavior | Work executed, skipped, replaced, or conditionally retained |
| Preserved responsibility | Later events, validation, posting, integrity, permissions, telemetry, and error propagation |
| Transaction context | Commit boundary, isolation, `TryFunction`, rollback, and external side effects where observable |
| Composition | Other known subscribers, ordering assumptions, and shared-control interaction |
| Scenario | Intended current activity or anticipated change represented by the case |
| Evidence status | Direct observation, interpretation, missing context, or unresolved question |

Unclassifiable cases are evidence against the candidate model and must not be
forced into the nearest category.

## 9. Pilot and Reliability

Pilot the record on at least one case from each available major effect category
before fixing the main sample. Revise ambiguous definitions explicitly and
retain the earlier wording in revision history.

When two reviewers are available, both should classify an overlapping subset
independently and reconcile disagreements. When only one reviewer is available,
repeat classification after an interval and record changed judgments. No
reliability statistic is required until the sample size and coding scheme make
one meaningful.

## 10. Planned Analysis

The study should produce:

- a case table with source-backed observations;
- a separate interpretation for each case;
- counterexamples and unclassified cases;
- within-stratum comparisons without unsupported population estimates;
- an assessment of whether the candidate dimensions are independent and
  sufficient; and
- narrowly scoped implications for later framework synthesis.

Counts may describe the selected sample. They must not be presented as BCApps
prevalence unless the population and sampling design support that inference.

## 11. Threats to Validity

### 11.1 Internal validity

- Subscriber behavior may depend on setup, license, permissions, runtime
  version, or code outside the inspected path.
- Static source analysis may not reveal actual binding, event reachability, or
  transaction behavior.
- Mutable state and external effects may be hidden behind called procedures.

### 11.2 External validity

- Microsoft application code does not represent every partner or customer
  extension.
- First-party apps and localizations may follow different constraints from
  independently distributed extensions.
- One repository commit cannot establish historical or future practice.

### 11.3 Construct validity

- Candidate effect and responsibility categories may overlap or omit relevant
  phenomena.
- Event names may imply patterns that surrounding control flow does not
  implement.
- Presence in shipped code does not measure architectural quality or Microsoft
  recommendation.

### 11.4 Reproducibility

- The repository is large and evolves continuously.
- Tooling that parses AL may produce incomplete or version-sensitive results.
- A fixed commit and retained discovery method are required to reproduce the
  population.

## 12. Findings

No findings are available. Study execution is pending.

## 13. Candidate Implications for the Framework

No framework implication is accepted by this protocol. The study is designed
to test, refine, or reject candidate dimensions recorded in
`References/Microsoft_Event_Types.md`.

## 14. Future Work

1. Implement and retain the population-discovery procedure.
2. Fix the execution baseline and generate raw population counts.
3. Select and classify the pilot cases.
4. Refine the coding record without concealing failed classifications.
5. Execute the main sample and document counterexamples.
6. Compare event cases with interface-based substitution after
   `References/Microsoft_Interfaces.md` is developed.

## 15. References

- **[B1]** Microsoft. "BCApps — the home of Business Central application
  development." GitHub repository, planning baseline commit
  `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6>.

## 16. Revision History

### 0.1.0 — 2026-07-18

- Established the empirical study protocol before case selection.
- Defined the unit of analysis, sampling strata, classification record,
  validity threats, and reproducibility requirements.
- Recorded that execution and findings remain pending.
