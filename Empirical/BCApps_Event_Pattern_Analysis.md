---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-EVENTS-001
  title: BCApps Event Pattern Analysis
  type: Empirical Study Protocol
  version: 0.2.0
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
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
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

The study also tests a candidate **Behavioral Change Impact Review** entry
condition and checklist. The candidate is mechanism-independent: event-specific
facts are evidence supplied to the review, not the definition of the reviewed
phenomenon.

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
6. Can the candidate Behavioral Change Impact Review entry condition
   distinguish materially behavior-changing cases from local or nonmaterial
   event participation?
7. Does the candidate checklist identify relevant architectural consequences
   without depending on event-specific terminology?

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

## 5. Candidate Behavioral Change Impact Review

### 5.1 Candidate status

Behavioral Change Impact Review is a working label used for empirical testing.
It is not canonical repository terminology, an accepted framework component,
or a Microsoft-defined method.

The working definition is:

> A review initiated when a customization materially augments, redirects,
> suppresses, replaces, reorders, or delegates established behavior or
> execution responsibility.

The wording deliberately includes augmentation. An added action can change
outcomes, side effects, transactions, failure behavior, or other architectural
properties even when default behavior remains reachable.

For this study, a change is **material** when available evidence indicates that
it can alter an observable outcome, side effect, invariant, responsibility,
interaction, failure mode, or quality-relevant execution property. This is an
operational coding rule, not a canonical definition of materiality.

### 5.2 Trigger screening

Before applying the impact checklist, classify the case as:

- **Triggered:** direct source evidence supports both an established behavior
  or responsibility and a material augmentation, redirection, suppression,
  replacement, reordering, or delegation.
- **Not Triggered:** the subscriber participates, but available evidence does
  not show a material behavioral change under the operational rule.
- **Uncertain:** essential publisher, caller, runtime, configuration, or
  behavioral evidence is unavailable or ambiguous.

The trigger result is a study classification, not a quality judgment. A
triggered case is not automatically defective, and a not-triggered case is not
automatically well designed.

Record separately:

1. the established behavior or responsibility;
2. the source evidence for the customization effect;
3. the candidate change type;
4. the material consequence that supports or fails to support entry; and
5. missing evidence or competing interpretations.

Do not infer materiality from `IsHandled`, an event name, a `var` parameter, or
manual binding alone.

### 5.3 Behavioral Change Impact Checklist

Apply the checklist to `Triggered` cases. Apply it provisionally to `Uncertain`
cases when doing so clarifies the missing evidence. Do not force every row to
produce an impact.

| Area | Mechanism-independent review question |
|---|---|
| Affected flow | What established behavior or execution flow is changed? |
| Change type | Is the flow augmented, redirected, suppressed, replaced, reordered, or delegated? |
| Outcomes | Which outcomes and side effects change, and which must remain preserved? |
| Invariants | Which domain, data, security, and process invariants did the original flow enforce? |
| Ordering and transaction semantics | Does the change affect operation order, atomicity, rollback, locking, retry, or idempotence? |
| Integration and extensibility | Does it change the reachability, ordering, contract, or behavioral significance of integration and extension points? |
| Observability | Are audit evidence, telemetry, diagnostics, and business events preserved? |
| Failure behavior | Does error, partial-completion, compensation, or retry behavior change? |
| Ownership | Who now owns the changed behavior and the responsibilities previously carried by the original flow? |
| Evolution | How will the customization respond when the original implementation evolves? |

The checklist separates extensibility from the general research subject.
Changed extensibility semantics are one possible consequence of behavioral
change, not the name or complete scope of the review.

### 5.4 Relationship to event evidence

For an event-based case, collect the mechanism-specific evidence before or
alongside the general checklist:

| Event evidence dimension | Primary checklist use |
|---|---|
| Publisher contract | Affected flow; integration and extensibility; evolution |
| Subscriber effect | Change type; outcomes |
| Runtime participation | Ordering and transaction semantics; failure behavior; ownership |
| Preserved responsibility | Outcomes; invariants; observability; ownership |

This mapping is a candidate analytical aid. The study must retain facts that do
not fit it and must not treat the mapping as proof that the four event
dimensions are sufficient.

## 6. Unit of Analysis

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

## 7. Sampling Strategy

### 7.1 Population discovery

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

### 7.2 Strata

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

### 7.3 Selection

Use a two-stage selection:

1. Select cases purposively to ensure every available stratum has at least one
   pilot example.
2. Select additional cases from the generated population using a recorded
   deterministic or random method.

Purely convenient or visually interesting examples may be used for pilot
calibration but must not be represented as prevalence evidence.

Include negative controls, uncertain cases, and cases expected not to trigger
the review. A pilot that contains only suspected defects cannot evaluate the
entry condition or its false-positive tendency.

Record whether a case was known to the reviewer before selection. Domain
familiarity may improve interpretation but must not silently determine the
sample.

## 8. Inclusion and Exclusion Criteria

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

## 9. Classification Record

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
| Trigger evidence | Established behavior, candidate change type, material consequence, and missing evidence |
| Trigger result | Triggered, Not Triggered, or Uncertain |
| Checklist applicability | Applicable rows, not-applicable rows, and unresolved rows |
| Evidence status | Direct observation, interpretation, missing context, or unresolved question |

Unclassifiable cases are evidence against the candidate model and must not be
forced into the nearest category.

## 10. Pilot and Reliability

Pilot the record on at least one case from each available major effect category
before fixing the main sample. Revise ambiguous definitions explicitly and
retain the earlier wording in revision history.

When two reviewers are available, both should classify an overlapping subset
independently and reconcile disagreements. When only one reviewer is available,
repeat classification after an interval and record changed judgments. No
reliability statistic is required until the sample size and coding scheme make
one meaningful.

The pilot must allow revision or rejection of the trigger, checklist, event
dimensions, or their mapping. Classification disagreement and unclassifiable
cases are study results, not editorial defects to be removed.

## 11. Planned Analysis

The study should produce:

- a case table with source-backed observations;
- a separate interpretation for each case;
- counterexamples and unclassified cases;
- within-stratum comparisons without unsupported population estimates;
- an assessment of whether the candidate dimensions are independent and
  sufficient; and
- trigger outcomes, including negative controls and uncertain cases;
- checklist omissions, duplication, and mechanism-dependent wording; and
- narrowly scoped implications for later framework synthesis.

Counts may describe the selected sample. They must not be presented as BCApps
prevalence unless the population and sampling design support that inference.

## 12. Threats to Validity

### 12.1 Internal validity

- Subscriber behavior may depend on setup, license, permissions, runtime
  version, or code outside the inspected path.
- Static source analysis may not reveal actual binding, event reachability, or
  transaction behavior.
- Mutable state and external effects may be hidden behind called procedures.
- Prior knowledge of a case may bias trigger and impact classification.

### 12.2 External validity

- Microsoft application code does not represent every partner or customer
  extension.
- First-party apps and localizations may follow different constraints from
  independently distributed extensions.
- One repository commit cannot establish historical or future practice.

### 12.3 Construct validity

- Candidate effect and responsibility categories may overlap or omit relevant
  phenomena.
- Event names may imply patterns that surrounding control flow does not
  implement.
- Presence in shipped code does not measure architectural quality or Microsoft
  recommendation.
- The terms *material*, *established behavior*, and *execution responsibility*
  may be applied inconsistently or may duplicate established concepts not yet
  identified by the repository research.
- Checklist coverage may appear complete because the same researchers proposed
  and applied it.

### 12.4 Reproducibility

- The repository is large and evolves continuously.
- Tooling that parses AL may produce incomplete or version-sensitive results.
- A fixed commit and retained discovery method are required to reproduce the
  population.

## 13. Findings

No findings are available. Study execution is pending.

## 14. Candidate Implications for the Framework

No framework implication is accepted by this protocol. The study is designed
to test, refine, or reject the candidate review trigger, checklist, and event
dimensions recorded in this protocol and
`References/Microsoft_Event_Types.md`.

## 15. Future Work

1. Implement and retain the population-discovery procedure.
2. Fix the execution baseline and generate raw population counts.
3. Select and classify the pilot cases.
4. Refine the coding record without concealing failed classifications.
5. Execute the main sample and document counterexamples.
6. Compare event cases with interface-based substitution after
   `References/Microsoft_Interfaces.md` is developed.

## 16. References

- **[B1]** Microsoft. "BCApps — the home of Business Central application
  development." GitHub repository, planning baseline commit
  `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6>.

## 17. Revision History

### 0.2.0 — 2026-07-18

- Added the candidate Behavioral Change Impact Review working definition.
- Added operational materiality and three-state trigger-screening rules.
- Added the mechanism-independent impact checklist and mapped event evidence to
  it without accepting the mapping as sufficient.
- Required negative controls, uncertain cases, prior-knowledge disclosure, and
  explicit construct-validity testing.

### 0.1.0 — 2026-07-18

- Established the empirical study protocol before case selection.
- Defined the unit of analysis, sampling strata, classification record,
  validity threats, and reproducibility requirements.
- Recorded that execution and findings remain pending.
