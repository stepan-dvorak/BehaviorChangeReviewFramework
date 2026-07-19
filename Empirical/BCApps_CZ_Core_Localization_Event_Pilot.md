---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-EVENT-PILOT-001
  title: BCApps Czech Core Localization Event Pilot
  type: Empirical Study
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Pre-registers a bounded pilot of event participation in Microsoft's Core
  Localization Pack for Czech application to test the candidate Behavioral
  Change Impact Review trigger, checklist, and event-evidence dimensions before
  any case findings are recorded.

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
  - Empirical/BCApps_Event_Pattern_Analysis.md
  - References/Microsoft_Event_Types.md

related_documents:
  - 00_Research_Log.md
  - References/Microsoft_IsHandled_v2.0.md
  - References/SAAM.md
  - References/ATAM.md
  - Ideas/Microsoft_Event_Types_Research_Agenda.md

study:
  method: Bounded Stratified Repository Code Audit Pilot
  subject: Microsoft Core Localization Pack for Czech application
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Baseline, Subscriber Population, and Selection Protocol Fixed

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - event-subscribers
  - behavioral-change
  - pilot
  - pre-registration
---

# BCApps Czech Core Localization Event Pilot

## 1. Study Status

This document pre-registers the pilot before case selection and classification.
It contains no evaluated cases, behavioral findings, defect claims, prevalence
claims, or framework conclusions.

The pilot tests candidate concepts. Behavioral Change Impact Review remains a
working label, and the trigger, checklist, event dimensions, and materiality
rule may be refined or rejected after the pilot.

## 2. Objective

Evaluate whether the candidate Behavioral Change Impact Review entry condition
and mechanism-independent checklist can identify and structure architecturally
relevant consequences across a bounded, diverse set of event participation
cases in one Microsoft Business Central localization application.

The pilot also tests whether publisher contract, subscriber effect, runtime
participation, and preserved responsibility provide sufficient
mechanism-specific evidence for the general review.

## 3. Research Questions

1. Can the candidate trigger distinguish material behavioral changes from
   local or nonmaterial event participation?
2. Can independent cases be classified as augmentation, redirection,
   suppression, replacement, reordering, delegation, or no demonstrated
   material change using direct source evidence?
3. Which checklist areas are applicable, unsupported, duplicated, or missing
   across the selected cases?
4. Do the four event-evidence dimensions capture the information needed by the
   mechanism-independent checklist?
5. Which cases remain uncertain or unclassifiable after publisher, subscriber,
   caller, binding, and relevant test context are inspected?
6. How does reviewer familiarity with the application affect selection and
   interpretation?

## 4. Fixed Source Baseline

### 4.1 Repository and commit

- Repository: `microsoft/BCApps`
- Commit: `397d01199c321e774edaf23a7290fee40f75c6a6`
- Application path:
  `src/Apps/CZ/CoreLocalizationPack/app`
- Production source boundary:
  `src/Apps/CZ/CoreLocalizationPack/app/Src`

The commit is immutable and remains the pilot baseline even if the BCApps
`main` branch advances. Changing it requires a protocol revision before any
case is classified.

### 4.2 Application identity

The baseline `app.json` declares [C1]:

- application ID `267b59d3-7302-44c5-ba77-c87000380514`;
- name `Core Localization Pack for Czech`;
- publisher `Microsoft`;
- version `29.0.0.0`;
- target `Cloud`; and
- application and platform version `29.0.0.0`.

The manifest also declares one explicit application dependency, `EU 3-Party
Trade Purchase` version `29.0.0.0`, and `application` version `29.0.0.0` [C1].
Microsoft documents that the `application` property references the Application
app, which logically encapsulates the apps that make up the solution and
resolves their dependencies implicitly [C5]. The exact dependency closure used
for publisher resolution must be recorded from the fixed BCApps commit rather
than inferred from current product packaging.

This identifies the empirical subject. It does not establish the quality,
intent, or representativeness of any event implementation.

### 4.3 Reproduced syntactic inventory

A retained deterministic extraction of the fixed production source boundary
found [C4]:

| Search result | Count |
|---|---:|
| AL source files | 782 |
| `[EventSubscriber(` attribute occurrences | 448 |
| Source files containing at least one subscriber | 116 |

The 448 subscriber rows and their source identities are retained in the
population CSV. These are syntactic inventory observations, not semantic case
counts. The extractor is not an AL compiler, does not evaluate conditional
compilation, and does not establish runtime participation or subscriber effect.
The manifest records the commands, versions, checksums, validation, and
limitations. A later application-wide marker inventory was withdrawn because
it mixed CZL publishers and ordinary implementation markers with the CZL
subscriber population. Dependency-aware, per-subscriber context resolution is
therefore still pending [C4].

## 5. Scope

### 5.1 Included

- AL files under the fixed production source boundary;
- subscriber declarations and bodies;
- publisher declarations and raise sites available at the fixed BCApps commit;
- binding and activation code required to interpret participation;
- directly relevant callers, downstream events, and tests available at the
  same commit; and
- standard, System Application, Business Foundation, or other BCApps source
  needed to interpret the selected publisher.

### 5.2 Excluded from the pilot population

- the separate Core Localization Pack for Czech test application as a source
  of subscriber candidates;
- other Czech applications and localizations;
- third-party extensions;
- runtime observations not reproduced and recorded separately;
- historical commits; and
- a complete quality assessment of the application.

Tests may be consulted as contextual evidence for selected production cases.
They are not pilot subscriber candidates and must not be treated as proof that
all relevant behavior is covered.

Microsoft documents that multiple subscribers to one event execute one at a
time in no specified order [C3]. The pilot therefore includes other known
subscribers and ordering assumptions when composition affects interpretation;
it does not infer runtime participation from the bounded application alone.

## 6. Unit of Analysis

One **behavioral change case** contains, where available:

1. the subscriber declaration and body;
2. the publisher declaration;
3. the event raise site and surrounding default control flow;
4. activation or binding context;
5. relevant calls made by the subscriber;
6. later events, checks, side effects, and responsibilities affected by
   participation;
7. directly relevant tests; and
8. configuration, permissions, licensing, or conditional-compilation context
   required for interpretation.

One subscriber method may yield no behavioral change case if material change
cannot be demonstrated. Multiple subscriber methods may form one composition
case when their interaction is the subject of analysis.

## 7. Reviewer Position and Bias Controls

The repository owner has prior development experience with the application and
expects the population to include both diverse patterns and possible
shortcomings. This knowledge is valuable for functional interpretation but
creates confirmation and selection risks.

Apply these controls:

- freeze this protocol before selecting case symbols;
- label every selected case as `Prior Known: Yes`, `No`, or `Uncertain`;
- include no more than eight prior-known cases in the 16-case pilot;
- include negative controls and cases expected not to trigger review;
- include at least four cases chosen without a prior defect expectation;
- use no more than two cases from one subscriber codeunit;
- retain cases that contradict the working hypothesis or expose checklist
  redundancy; and
- separate source observation from reviewer interpretation in every record.

The pilot does not estimate defect prevalence. Prior knowledge and purposive
sampling make such an estimate invalid.

## 8. Population Discovery

### 8.1 Required retained outputs

Before selection, retain or record:

- the fixed commit identifier;
- the complete ordered list of AL files;
- every detected subscriber attribute with source path and symbol;
- the commands and tool versions used; and
- parse failures, conditional-compilation limitations, and manual corrections.

Publisher and runtime-context discovery must be joined to a retained CZL
subscriber. Application-wide publisher declarations or control markers are not
candidate cases and must not be used as independent screening inputs.

For each subscriber taken forward to screening, resolve or explicitly mark as
unresolved:

- the target publisher application or platform event class;
- the publisher declaration and raise site where source exists;
- the surrounding established flow;
- the subscriber body boundary, direct calls, and mechanical control writes;
- manual binding or activation context for that subscriber; and
- relevant dependency, caller, composition, and test context.

### 8.2 Minimum subscriber-context searches

When resolving a retained subscriber, the procedure must cover at least:

- the subscriber declaration, body, parameters, and direct calls;
- its target integration, business, internal, database, or page event;
- the publisher declaration, raise site, and surrounding default flow where
  source exists;
- `EventSubscriberInstance`, `BindSubscription`, and `UnbindSubscription`
  context applicable to that subscriber;
- writes or reads involving `IsHandled`, `Handled`, `Skip`, mutable records,
  or other control values in that subscriber;
- `Commit`, `TryFunction`, isolated-event, and obsolete-state context relevant
  to that subscriber and publisher; and
- other subscribers to the same target in the available dependency scope.

Discovery markers generate candidates. They do not establish trigger results,
change types, impacts, or defects.

## 9. Pilot Selection Rules

### 9.1 Target size

Select 16 unique cases. If fewer than 16 cases meet the required evidence and
diversity conditions, retain the smaller sample and record the shortfall rather
than weakening the criteria.

### 9.2 Pre-registered selection buckets

Fill the following buckets when qualifying cases exist:

| Bucket | Target | Selection purpose |
|---|---:|---|
| Suppression or substitution | 2 | Test handled or skip behavior and responsibility transfer |
| Validation or invariant influence | 2 | Test preservation of domain, data, security, or process checks |
| Posting or transaction behavior | 2 | Test ordering, atomicity, rollback, locking, and side effects |
| Manual runtime participation | 2 | Test activation, binding lifetime, and ownership |
| Mutable influence without demonstrated full replacement | 2 | Test augmentation, redirection, and ambiguous control sharing |
| Workflow, reporting, integration, or delegated behavior | 2 | Test mechanism-independent applicability beyond posting |
| Negative controls | 2 | Test cases expected not to satisfy the material-change rule |
| Borderline or uncertain cases | 2 | Test missing evidence and classification limits |

A case may exhibit multiple properties, but it occupies only one primary
selection bucket. Record secondary properties separately.

### 9.3 Selection order

1. Generate the ordered candidate population from the fixed source boundary.
2. Perform a coarse evidence-availability and stratum screen without completing
   the impact checklist.
3. Mark prior-known status before assigning a case to a bucket.
4. Assign qualifying cases to the least-filled applicable bucket.
5. Within equivalent candidates, prefer broader source-file coverage, then use
   lexical source path and procedure name as deterministic tie-breakers.
6. Enforce the two-case-per-codeunit and eight-prior-known limits.
7. Freeze the selection register before full case classification.

Do not replace a selected case because its result is favorable, unfavorable,
not triggered, or uncertain. Replacement is permitted only for a documented
inclusion failure, duplicate unit, or unavailable essential context.

## 10. Empty Selection Register

Complete this table and freeze it before applying the full checklist.

| Case ID | Primary bucket | Source path | Subscriber symbol | Prior known | Inclusion evidence | Status |
|---|---|---|---|---|---|---|
| CZP-001 |  |  |  |  |  | Unselected |
| CZP-002 |  |  |  |  |  | Unselected |
| CZP-003 |  |  |  |  |  | Unselected |
| CZP-004 |  |  |  |  |  | Unselected |
| CZP-005 |  |  |  |  |  | Unselected |
| CZP-006 |  |  |  |  |  | Unselected |
| CZP-007 |  |  |  |  |  | Unselected |
| CZP-008 |  |  |  |  |  | Unselected |
| CZP-009 |  |  |  |  |  | Unselected |
| CZP-010 |  |  |  |  |  | Unselected |
| CZP-011 |  |  |  |  |  | Unselected |
| CZP-012 |  |  |  |  |  | Unselected |
| CZP-013 |  |  |  |  |  | Unselected |
| CZP-014 |  |  |  |  |  | Unselected |
| CZP-015 |  |  |  |  |  | Unselected |
| CZP-016 |  |  |  |  |  | Unselected |

## 11. Empty Case Record Template

Copy this complete structure once for each frozen case ID. Do not remove empty
or not-applicable fields; their status is part of checklist evaluation.

### Case `CZP-NNN` — Unclassified

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Primary selection bucket | Not recorded |
| Prior known | Not recorded |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Subscriber path and symbol | Not recorded |
| Publisher path and symbol | Not recorded |
| Raise site | Not recorded |
| Relevant caller, binding, and test paths | Not recorded |

#### 11.2 Source observations

- Publisher contract: Not recorded.
- Subscriber body and direct calls: Not recorded.
- Surrounding default behavior: Not recorded.
- Runtime participation: Not recorded.
- Mutable influence: Not recorded.
- Downstream events and responsibilities: Not recorded.
- Transaction and failure context: Not recorded.
- Other subscribers or composition evidence: Not recorded.

#### 11.3 Trigger screening

| Field | Classification and evidence |
|---|---|
| Established behavior or responsibility | Not evaluated |
| Candidate change type | Not evaluated |
| Material consequence | Not evaluated |
| Missing or conflicting evidence | Not evaluated |
| Trigger result | Unclassified |

Permitted trigger results are `Triggered`, `Not Triggered`, and `Uncertain`.

#### 11.4 Event-evidence dimensions

| Dimension | Observation | Interpretation status |
|---|---|---|
| Publisher contract | Not evaluated | Pending |
| Subscriber effect | Not evaluated | Pending |
| Runtime participation | Not evaluated | Pending |
| Preserved responsibility | Not evaluated | Pending |

#### 11.5 Behavioral Change Impact Checklist

| Area | Evidence-backed assessment | Status |
|---|---|---|
| Affected flow | Not evaluated | Pending |
| Change type | Not evaluated | Pending |
| Outcomes | Not evaluated | Pending |
| Invariants | Not evaluated | Pending |
| Ordering and transaction semantics | Not evaluated | Pending |
| Integration and extensibility | Not evaluated | Pending |
| Observability | Not evaluated | Pending |
| Failure behavior | Not evaluated | Pending |
| Ownership | Not evaluated | Pending |
| Evolution | Not evaluated | Pending |

Permitted row statuses are `Supported`, `No Demonstrated Impact`, `Not
Applicable`, `Missing Evidence`, and `Conflicting Evidence`.

#### 11.6 Reasoning record

- Source claim: None recorded.
- Repository observation: None recorded.
- Interpretation: None recorded.
- Candidate implication: None recorded.
- Counterevidence or alternative interpretation: None recorded.
- Unresolved question: None recorded.

#### 11.7 Case result

| Field | Result |
|---|---|
| Trigger classification | Unclassified |
| Demonstrated impacts | None recorded |
| Plausible but unverified risks | None recorded |
| Checklist omissions or duplication | None recorded |
| Event-model fit | Not evaluated |
| Confidence | Not evaluated |

## 12. Analysis Plan

After all frozen cases are recorded:

1. Report trigger classifications without converting them into defect counts.
2. Compare checklist applicability and missing evidence across selection
   buckets.
3. Identify cases that contradict, escape, or duplicate the candidate model.
4. Compare prior-known and not-prior-known cases for visible interpretation
   differences without claiming statistical significance.
5. Separate demonstrated impacts from plausible risks and unresolved questions.
6. Assess whether event-specific evidence was necessary and whether the final
   impact reasoning remained mechanism-independent.
7. Propose protocol changes only after preserving the original classifications.

The pilot may justify a larger study design. It cannot establish application,
BCApps, Microsoft, or ecosystem prevalence.

## 13. Threats to Validity

### 13.1 Internal validity

- Reviewer familiarity may improve functional interpretation while biasing
  selection and severity judgments.
- Static source may omit runtime setup, data, license, permission, and
  environment conditions.
- Publisher or test context may span BCApps applications outside the bounded
  candidate population.
- Event reachability and subscriber composition may differ at runtime.

### 13.2 External validity

- One Czech localization application does not represent BCApps, Microsoft
  engineering practice, partner extensions, or customer customizations.
- Version 29.0.0.0 and one commit cannot establish historical or future
  behavior.
- Regulatory localization code may have responsibilities unlike other
  application domains.

### 13.3 Construct validity

- The candidate trigger may overclassify any mutable or handled subscriber as
  material.
- Materiality and established responsibility may be interpreted circularly.
- The checklist was proposed by the same research project evaluating it.
- Event attributes and names may be mistaken for behavioral effects.
- The ten checklist areas may overlap or omit relevant quality concerns.

### 13.4 Conclusion validity

- The purposive 16-case sample does not support prevalence or comparative
  defect-rate claims.
- Counts from syntactic discovery do not measure independent behavioral cases.
- Missing evidence must not be converted into evidence of no impact.

## 14. Findings

No case findings are available. Selection and study execution are pending.

## 15. Candidate Framework Implications

None. The pilot is designed to test candidate concepts, not to accept them.

## 16. Execution Checklist

- [x] Reproduce and retain the event-subscriber population inventory.
- [x] Record its discovery command, tool versions, checksum, and limitations.
- [ ] Resolve dependency-aware publisher and runtime context per CZL subscriber.
- [ ] Complete coarse evidence-availability screening.
- [ ] Mark prior-known status before bucket assignment.
- [ ] Fill and freeze the 16-case selection register.
- [ ] Copy the empty case record for every selected case.
- [ ] Inspect publisher, raise site, subscriber, binding, caller, and test
      context for each case.
- [ ] Complete trigger screening before recording impact conclusions.
- [ ] Apply the checklist without forcing unsupported rows.
- [ ] Preserve counterevidence, uncertain cases, and failed classifications.
- [ ] Compare cases only after all records are complete.
- [ ] Update findings, limitations, research log, and index only after study
      execution.

## 17. References

- **[C1]** Microsoft. `app.json`, Core Localization Pack for Czech, BCApps
  commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/app.json>.
- **[C2]** Microsoft. Core Localization Pack for Czech production source,
  BCApps commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/Src>.
- **[C3]** Microsoft. "Subscribing to events." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-subscribing-to-events>.
- **[C4]** Orden. "BCApps Czech Core Localization Event Population Manifest."
  `Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md`.
- **[C5]** Microsoft. "The Microsoft_Application.app file." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-application-app-file>.

## 18. Revision History

### 0.4.0 — 2026-07-19

- Restored the CZL event subscriber as the sole candidate-population unit.
- Withdrew application-wide publisher and marker discovery as a screening
  input because it mixed publisher design with subscriber behavior.
- Required dependency-aware publisher, raise-site, established-flow, and
  runtime-context resolution per subscriber before coarse screening.

### 0.3.0 — 2026-07-18

- Completed and retained the mechanical publisher and discovery-marker
  inventories required before coarse screening.
- Preserved marker interpretations, prior-knowledge fields, case selection,
  trigger classifications, and checklist rows as unperformed.
- **Withdrawn on 2026-07-19:** the retained marker inventories were not valid
  inputs for this subscriber-centered pilot.

### 0.2.0 — 2026-07-18

- Replaced preliminary subscriber counts with a retained, reproducible
  448-row population inventory.
- Linked the extraction manifest and separated completed subscriber discovery
  from deferred publisher, binding, and other marker inventories.
- Left coarse screening, prior-knowledge labeling, case selection, trigger
  classification, and checklist analysis unperformed.

### 0.1.0 — 2026-07-18

- Fixed the BCApps repository, application, and production-source baseline.
- Recorded preliminary syntactic population observations with explicit limits.
- Pre-registered the 16-case stratified selection and reviewer-bias controls.
- Added an empty selection register and complete empty case record.
- Preserved the candidate status of the trigger, checklist, and event model.
