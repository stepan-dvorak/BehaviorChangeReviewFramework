---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-PROTOCOL-001
  title: BCApps Czech Coarse Evidence-Availability Screening Protocol
  type: Empirical Study Protocol
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Pre-registers a one-record-per-subscriber screen for source-evidence
  availability and descriptive strata before prior-knowledge labeling, case
  selection, trigger classification, or impact analysis.

quality:
  review: Self Reviewed
  evidence: Partial
  editorial: Reviewed

audience:
  - Researchers
  - Business Central Architects
  - Business Central Developers
  - Contributors
  - AI Assistants

depends_on:
  - 02_Research_Methodology.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/BCApps_CZ_Subscriber_Context_Manifest.md
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md

related_documents:
  - Empirical/BCApps_Event_Pattern_Analysis.md
  - Empirical/BCApps_CZ_Coarse_Screen_Technical_Validation.md
  - 00_Research_Log.md

study:
  method: Pre-registered Coarse Evidence-Availability Screening
  subject: Complete 448-record CZL subscriber-context dataset
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Automated Worksheet Validation and Owner Review Passed

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - coarse-screening
  - evidence-availability
  - pre-registration
---

# BCApps Czech Coarse Evidence-Availability Screening Protocol

## 1. Status and Boundary

This protocol is fixed before screening begins. It defines a preparatory
evidence-availability operation over all 448 retained `CZPOP` units. It does not
perform the screen and contains no prior-knowledge label, `CZP` case ID,
selection bucket, trigger classification, checklist result, quality judgment,
defect claim, or prevalence conclusion.

The screen answers whether enough bounded source context is available to carry
a subscriber into later reviewer labeling and selection. It does not answer
whether the subscriber changes behavior materially.

## 2. Research Question

> For each retained CZL event subscriber, is the bounded source evidence
> sufficient to support later case interpretation, and which descriptive
> strata can be recorded without evaluating behavioral change or selecting the
> case?

An evidence gap is retained as a result. It must not be converted into evidence
of no behavior, no impact, or poor implementation.

## 3. Unit and Fixed Inputs

The unit remains one retained `CZPOP-NNNN` subscriber. Publisher declarations,
raise sites, callers, tests, bindings, mechanical markers, and other subscribers
remain context attached to that unit.

Fixed inputs are:

- BCApps commit `397d01199c321e774edaf23a7290fee40f75c6a6`;
- `Empirical/Data/BCApps_CZ_Core_Localization_Event_Population.csv`;
- `Empirical/Data/BCApps_CZ_Subscriber_Context.jsonl` with SHA-256
  `381d476096615b757fecd92e52e3325b65b20384adfa8e9ae1bac792a99c8dfb`;
- the five-application source boundary; and
- `Schemas/BCApps_CZ_Coarse_Screen.schema.json`.

The context dataset is immutable input. Screening corrections must be recorded
in the screen record. A discovered context-extraction defect requires correction
and revalidation of the upstream resolver and dataset rather than silent repair
inside screening output.

## 4. Separation from Later Operations

The following sequence is mandatory:

1. context resolution;
2. coarse evidence-availability screening;
3. prior-knowledge labeling by the repository owner;
4. selection-bucket assignment and deterministic tie-breaking;
5. frozen `CZP` register; and
6. trigger and checklist analysis.

The coarse screen must not perform or anticipate steps 3–6. In particular:

- `Ready for Prior-Knowledge Labeling` is not `Eligible`, `Triggered`, or
  `Selected`;
- a missing evidence path is not `Not Triggered`;
- an `IsHandled`, `Handled`, `Skip`, mutable write, `Commit`, error marker,
  manual subscriber, or composition peer is not an automatic selection rule;
- source-published and platform-trigger events have equal standing in the
  readiness decision; and
- reviewer familiarity must not be recorded until the separate prior-knowledge
  operation.

## 5. Screening Record Contract

The JSON Schema is the field authority. Screening creates exactly one separate
record for every context record and leaves the context dataset unchanged.

Schema SHA-256:
`9698581c03ae663e5288a03719f6df759ebe35f378d4e3ee5e95f88c9fc31047`.

Every record contains:

- the `CZPOP` foreign key and fixed context-dataset checksum;
- one screening status;
- eight evidence-availability fields;
- zero or more descriptive stratum indicators;
- explicit targeted-search questions and observations;
- reviewer identity and date when screened; and
- protected later-workflow fields.

The schema fixes:

```text
prior_known = Unknown
selection_status = Unselected
trigger_status = Not Evaluated
checklist_status = Not Evaluated
```

## 6. Evidence-Availability Fields

### 6.1 Subscriber identity and body

`subscriber_identity` and `subscriber_body` record whether the retained
attribute, symbol, exact path, and body boundary can be inspected. Mechanical
markers may describe the body but are not required for body availability. An
empty calls or writes array is not missing body evidence.

### 6.2 Publisher or platform and raise or trigger

For source-published events, retain the compatible object identity, declaration,
owning boundary application, and at least one bounded raise-site candidate. For
database or page trigger events, retain the platform class and applicable event
semantics. The combined `raise_or_trigger` field is `Available` when those
platform semantics are available; the absent AL publisher path is not treated
as missing evidence.

A qualified-call match is bounded lexical evidence. The screen may require a
targeted type check when same-named procedures make a raise-site candidate
ambiguous.

### 6.3 Established flow

`established_flow` is `Available` only when the reviewer can identify the
bounded activity in which the event is raised or the platform trigger occurs.
This requires a concise source-backed description and paths sufficient for
later case analysis. It does not require a judgment that the subscriber changes
that flow materially.

Use `Targeted Search Required` when the existing context record locates the
event but not enough surrounding caller or control-flow context. Use `Outside
Boundary` when essential source is unavailable under the fixed protocol.

### 6.4 Runtime participation

Static subscribers record `Static Automatic`. A manual subscriber records
`Binding Evidence Available` only when the bounded source connects the relevant
subscriber codeunit or instance to binding or unbinding. Otherwise use
`Targeted Search Required`, `Ambiguous`, or `Outside Boundary`.

Binding evidence does not prove runtime reachability, lifetime, ordering,
configuration, license, or permission behavior.

### 6.5 Composition and tests

Composition records whether same-target peers exist in the retained CZL
population. `No CZL Peer Recorded` does not claim that no subscriber exists
elsewhere.

Test context is recorded as linked or not linked. Linked tests may help later
interpretation, but test evidence is not required for coarse readiness. No
linked test is not evidence of absent test coverage.

## 7. Descriptive Stratum Indicators

Indicators are copied or derived only from the retained context record:

- event class and publisher mechanism;
- static or manual subscriber instance;
- presence of mutable-parameter reads or writes;
- presence of transaction or error/exit markers;
- presence of same-target CZL peers; and
- presence of mechanically linked test context.

Indicators describe observable syntax and bounded context. They do not assign a
primary selection bucket or predict trigger outcome. Every indicator must be
reproducible from named context fields.

## 8. Targeted Search Rules

A targeted search is permitted only to decide evidence availability. It must:

1. begin with a specific unanswered question recorded in
   `targeted_search_questions`;
2. remain within the fixed source boundary;
3. record exact paths and symbols in `screening_observations`;
4. stop when the readiness question is answered or the boundary is exhausted;
5. preserve conflicting or ambiguous evidence; and
6. avoid trigger, materiality, defect, impact, or bucket language.

Typical questions include:

- Which bounded caller supplies the surrounding established activity?
- Does this qualified call invoke the resolved publisher procedure?
- Where is this manual subscriber instance bound and unbound?
- Is a directly linked test or test handler available?

Screening must not recursively analyze every transitive call. A search that
becomes case-level behavioral analysis stops and records the remaining question.

## 9. Screening Status Decision Rules

### 9.1 `Ready for Prior-Knowledge Labeling`

Use only when:

- subscriber identity and body are `Available`;
- publisher or platform evidence is `Available`;
- raise or trigger evidence is `Available`;
- established-flow evidence is `Available`;
- runtime participation is `Static Automatic` or `Binding Evidence Available`;
- every material ambiguity for later case interpretation is resolved; and
- `unavailability_reason` is null.

Tests and same-target CZL peers are not readiness requirements.

### 9.2 `Targeted Context Required`

Use when essential evidence appears obtainable within the fixed boundary but
one or more specific searches remain. At least one targeted question is
required. This status is temporary but remains retained in every intermediate
output and must not be treated as selection failure.

### 9.3 `Unavailable for Selection`

Use when essential identity, body, publisher or platform, established-flow, or
manual-participation evidence is missing, irreducibly ambiguous, or outside the
fixed boundary after permitted searches. `unavailability_reason` is required.
The record remains in the 448-unit screening dataset and is not deleted.

### 9.4 `Not Screened`

Use only before screening work begins for that record. Reviewer and date may be
null, and no readiness inference is permitted.

## 10. Execution Order and Checkpoints

Process records in lexical `inventory_id` order. Retain intermediate output at
the end of every session so that unresolved work is visible.

For each record:

1. verify the context checksum and `CZPOP` identity;
2. populate mechanically derivable stratum indicators;
3. assess the eight evidence fields;
4. write bounded observations and targeted questions;
5. apply the status rule without consulting prior familiarity or bucket needs;
6. confirm protected fields; and
7. record reviewer identity and date.

The output must always contain exactly 448 unique records in context order,
including not-screened and unavailable records.

## 11. Technical Validation Before Full Screening

Before population-wide execution, implement the screen generator or worksheet
and retain a technical-validation set containing, when available:

- the first record for every event class;
- the first static and first manual subscriber;
- the first manual subscriber with binding evidence;
- the first manual subscriber without linked binding evidence;
- the first record with same-target CZL peers;
- the first record without same-target CZL peers; and
- the first record for every non-ready screening status produced by a dry run.

Deduplicate by `inventory_id` and preserve lexical order. These records receive
no `CZP` IDs and no prior-knowledge labels.

Validation must demonstrate:

- schema validity and exact context referential integrity;
- deterministic, byte-identical output;
- exact reproduction of every stratum indicator;
- explicit missing, ambiguous, and outside-boundary behavior;
- enforcement of status preconditions;
- unchanged protected workflow fields; and
- human review of every retained validation record before full screening.

## 12. Acceptance Criteria

Full screening may begin only when:

- the context dataset checksum matches the fixed value;
- the screening schema is valid;
- the implementation cannot mutate context records or protected fields;
- technical validation and human review pass;
- all targeted searches are bounded and auditable; and
- a failed or unavailable record is retained rather than omitted.

Screening completion requires 448 unique schema-valid records, no `Not
Screened` status, and an explicit summary of readiness, targeted-context, and
unavailable counts without treating them as behavior or defect prevalence.

## 13. Threats and Limitations

- Evidence readiness requires reviewer judgment and may be applied
  inconsistently.
- Source availability can be mistaken for behavioral understanding.
- Familiar code may receive less explicit evidence recording even when prior
  knowledge is intentionally hidden from this operation.
- Static source cannot establish runtime configuration, reachability, ordering,
  license, permission, or data-dependent behavior.
- A targeted search may drift into case analysis or preferentially enrich an
  interesting candidate.
- Missing linked tests or peers can be mistaken for their actual absence.
- The fixed source boundary can make an otherwise analyzable case unavailable.
- Readiness counts cannot support behavioral, quality, defect, or ecosystem
  prevalence claims.

## 14. Authorized Execution State and Deferred Work

The worksheet-preparation implementation, automated technical validation, and
owner review are complete. Owner review accepted corrected `CZPOP-0270` with
body range `22-33` and authorized population-wide coarse screening. The
complete retained worksheet contains 448 records in lexical order, all in the
initial `Not Screened` state.

Human evidence-availability screening is now the active next operation. After
screening is complete, prior-knowledge labels must be supplied in a separate
owner-controlled step before bucket assignment.

Case selection, trigger classification, checklist analysis, and framework
synthesis remain explicitly deferred.

## 15. References

- **[S1]** Orden. "Research Methodology." `02_Research_Methodology.md`.
- **[S2]** Orden. "BCApps Czech Core Localization Event Pilot."
  `Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md`.
- **[S3]** Orden. "BCApps Czech Subscriber Context Dataset Manifest."
  `Empirical/BCApps_CZ_Subscriber_Context_Manifest.md`.
- **[S4]** Orden. "BCApps Czech Subscriber Context Resolution Protocol."
  `Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md`.
- **[S5]** Orden. "Reasoning Standard." `Reasoning_Standard.md`.
- **[S6]** Orden. "BCApps Czech Coarse Screen Preparation Technical
  Validation." `Empirical/BCApps_CZ_Coarse_Screen_Technical_Validation.md`.

## 16. Revision History

### 0.4.0 — 2026-07-21

- Recorded focused owner acceptance of corrected `CZPOP-0270`.
- Opened the population-wide coarse-screening gate.
- Retained the complete 448-record worksheet in its initial `Not Screened`
  state without making any screening decision.
- Updated the schema checksum after the corrective change.

### 0.3.0 — 2026-07-21

- Updated the immutable context checksum after corrective regeneration.
- Recorded conditional owner review and focused `CZPOP-0270` re-review.
- Kept population-wide screening and all downstream operations pending.

### 0.2.0 — 2026-07-19

- Implemented deterministic preparation of protected `Not Screened`
  worksheets for all 448 context records.
- Retained six validation records covering the pre-registered mechanical
  strata and passed automated schema, determinism, integrity, and workflow
  protection checks.
- Kept owner review, coarse-screen decisions, and all later operations pending.

### 0.1.0 — 2026-07-19

- Fixed the one-record-per-subscriber screening unit and immutable inputs.
- Separated evidence readiness and descriptive strata from prior knowledge,
  selection buckets, trigger classification, and impact analysis.
- Defined controlled evidence fields, statuses, targeted-search limits,
  technical validation, acceptance criteria, and threats to validity.
- Kept all screening records and classifications unperformed.
