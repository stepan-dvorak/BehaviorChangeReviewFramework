---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-EVENT-PILOT-001
  title: BCApps Czech Core Localization Event Pilot
  type: Empirical Study
  version: 0.13.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Pre-registers a bounded pilot of event participation in Microsoft's Core
  Localization Pack for Czech application, records its frozen case-selection
  boundary and owner-reviewed evidence checkpoint, and tests the candidate
  Behavioral Change Impact Review trigger, checklist, and event-evidence
  dimensions before interpretive case findings are recorded.

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
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md
  - Empirical/BCApps_CZ_Subscriber_Context_Technical_Validation.md
  - Empirical/BCApps_CZ_Subscriber_Context_Manifest.md
  - Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md
  - Empirical/BCApps_CZ_Coarse_Screen_Technical_Validation.md
  - Empirical/BCApps_CZ_Coarse_Screen_Execution_Protocol.md
  - Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl

study:
  method: Bounded Stratified Repository Code Audit Pilot
  subject: Microsoft Core Localization Pack for Czech application
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Baseline, Population, Context Protocol, Selection Protocol, and Evidence Checkpoint Fixed

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

This document records the pre-registered pilot, its frozen 16-case selection
register, and the owner-reviewed evidence checkpoint. The repository owner
accepted the complete selection register on 2026-08-08 and completed
evidence-sufficiency review of all sixteen frozen cases on 2026-08-30.

All sixteen cases are recorded as `Evidence sufficient`; no targeted evidence
request, correction requirement, or evidence-unavailable disposition remains
open before interpretation. Trigger classification has not started. The
document contains no trigger results, checklist findings, defect claims,
prevalence claims, or framework conclusions.

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

The context protocol records five physically available source applications at
the fixed commit: the subject, its explicit dependency, Base Application,
Business Foundation, and System Application [C6]. This is an operational source
search boundary, not a claim that those five repositories reproduce the full
contents or runtime closure of the distributed `Microsoft_Application.app`.

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
subscriber population. Dependency-aware, per-subscriber context resolution was
subsequently completed under the retained context protocol [C4][C6].

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

`Prior Known` records case-specific familiarity with the concrete subscriber
occurrence before its first targeted inspection within the Orden pilot. The
reference boundary is activity-based rather than date-based. General Business
Central expertise, familiarity with the functional area, or knowledge acquired
during population preparation, coarse screening, owner review, or case
selection does not by itself constitute prior knowledge.

Use the values as follows:

- `Yes`: the reviewer knew the concrete subscriber occurrence or its specific
  behavior independently of the Orden pilot;
- `No`: the reviewer may have known the area or pattern but did not know this
  concrete occurrence before its targeted inspection in the pilot; and
- `Uncertain`: the reviewer cannot reliably reconstruct whether the familiarity
  predates the pilot or was acquired during the pilot.

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

## 10. Frozen Selection Register

The repository owner supplied all sixteen `Prior Known` values before formal
primary-bucket assignment and accepted the complete register on 2026-08-08.
Case IDs follow the pre-registered bucket order and, within each bucket, lexical
subscriber source path and procedure name.

| Case ID | Population ID | Primary bucket | Source path | Subscriber symbol | Prior known | Inclusion evidence | Status |
|---|---|---|---|---|---|---|---|
| CZP-001 | CZPOP-0002 | Suppression or substitution | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/AccScheduleManagementCZL.Codeunit.al` | `Acc. Schedule Management CZL.PrintAccScheduleByType` | No | Runs a CZL report path and writes `IsHandled` in `Financial Report Mgt..OnBeforePrint`. | Frozen — Owner Accepted |
| CZP-002 | CZPOP-0308 | Suppression or substitution | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ReconciliationHandlerCZL.Codeunit.al` | `Reconciliation Handler CZL.OnBeforeSaveNetChange` | No | Writes `IsHandled := true` before BaseApp `SaveNetChange`; companion CZL logic populates net-change records. | Frozen — Owner Accepted |
| CZP-003 | CZPOP-0097 | Validation or invariant influence | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/DimensionMgtHandlerCZL.Codeunit.al` | `Dimension Mgt. Handler CZL.UserChecksAllowedOnCheckDimValuePostingOnBeforeExit` | No | Runs user-specific dimension-value checks and writes `IsChecked` and `IsHandled`. | Frozen — Owner Accepted |
| CZP-004 | CZPOP-0129 | Validation or invariant influence | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GenJnlCheckLineHandlerCZL.Codeunit.al` | `Gen.Jnl.Check Line Handler CZL.IsCheckDimensionsEnabledOnCheckDimensionsOnAfterAssignDimTableIDs` | No | Writes `CheckDone` from the CZL dimension-check enablement state. | Frozen — Owner Accepted |
| CZP-005 | CZPOP-0146 | Posting or transaction behavior | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GenJnlPostLineHandlerCZL.Codeunit.al` | `Gen.Jnl. Post Line Handler CZL.CorrectPmtDiscLCYOnCalcPmtDiscIfAdjVATOnAfterCalcPmtDiscVATBases` | No | Recalculates payment-discount VAT-base data inside general-journal posting. | Frozen — Owner Accepted |
| CZP-006 | CZPOP-0209 | Posting or transaction behavior | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/InventoryPostingHandlerCZL.Codeunit.al` | `Inventory Posting Handler CZL.RoundingDateOnPostItemJnlLineOnAfterSetPostingDate` | No | Rewrites item-journal posting date inside inventory-adjustment posting. | Frozen — Owner Accepted |
| CZP-007 | CZPOP-0125 | Manual runtime participation | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GLEntryasCorrectionCZL.Codeunit.al` | `G/L Entry as Correction CZL.SetCorrectionOnBeforeInsertGlEntry` | No | Manual subscriber mutates `GenJnlLine` before G/L entry insertion. | Frozen — Owner Accepted |
| CZP-008 | CZPOP-0245 | Manual runtime participation | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ItemTrackingDocHandlerCZL.Codeunit.al` | `Item Tracking Doc. Handler CZL.FillExpirationDateOnAfterFillTrackingSpecBufferFromItemLedgEntry` | Uncertain | Manual subscriber updates tracking-specification expiration data. | Frozen — Owner Accepted |
| CZP-009 | CZPOP-0001 | Mutable influence without demonstrated full replacement | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/AccScheduleManagementCZL.Codeunit.al` | `Acc. Schedule Management CZL.CalcCZLOnAfterCalcCellValue` | No | Mutates the calculated account-schedule result after standard calculation. | Frozen — Owner Accepted |
| CZP-010 | CZPOP-0081 | Mutable influence without demonstrated full replacement | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CorrectionsPostingMgtCZL.Codeunit.al` | `Corrections Posting Mgt. CZL.PurchLineSetNegativeOnAfterInitOutstandingQty` | Uncertain | Mutates `Purchase Line."Negative CZL"` after outstanding quantities are initialized. | Frozen — Owner Accepted |
| CZP-011 | CZPOP-0017 | Workflow, reporting, integration, or delegated behavior | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CNBCurrExchRateMgtCZL.Codeunit.al` | `CNB Curr. Exch. Rate Mgt. CZL.SetupCurrencyExchangeRateServiceOnBeforeSetupCurrencyExchRateService` | Uncertain | Configures the CNB exchange-rate service and contains an explicit `Commit`. | Frozen — Owner Accepted |
| CZP-012 | CZPOP-0257 | Workflow, reporting, integration, or delegated behavior | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/NavigateHandlerCZL.Codeunit.al` | `Navigate Handler CZL.OnAfterNavigateFindRecords` | Uncertain | Adds CZL EET records to Navigate results. | Frozen — Owner Accepted |
| CZP-013 | CZPOP-0048 | Negative controls | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ContactHandlerCZL.Codeunit.al` | `Contact Handler CZL.SaveRegistrationNoOnBeforeCustCopyFieldsFromCont` | No | Delegates localized registration-number propagation during contact-to-customer copy. | Frozen — Owner Accepted |
| CZP-014 | CZPOP-0401 | Negative controls | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/VATDateHandlerCZL.Codeunit.al` | `VAT Date Handler CZL.UpdateVatDateOnAfterCopyGenJnlLineFromGLEntry` | Yes | Copies VAT reporting date from a general-journal line to a G/L entry. | Frozen — Owner Accepted |
| CZP-015 | CZPOP-0033 | Borderline or uncertain cases | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CompanyBankAccHandlerCZL.Codeunit.al` | `Company Bank Acc. Handler CZL.FinanceChargeMemoUpdateBankAccountCodeCZLOnAfterValidateCompanyBankAccountCode` | Uncertain | Platform validation event updates the localized bank-account field; no AL publisher raise site exists. | Frozen — Owner Accepted |
| CZP-016 | CZPOP-0353 | Borderline or uncertain cases | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ServiceHeaderHandlerCZL.Codeunit.al` | `Service Header Handler CZL.UpdateVATCurrencyfactorCZLOnBeforeCurrencyFactorValidate` | No | Platform pre-validation event updates VAT currency factor; no AL publisher raise site exists. | Frozen — Owner Accepted |

Selection-control reconciliation:

- 16 unique population records fill all eight buckets with two cases each;
- 15 subscriber codeunits and 15 subscriber source files are represented;
- only `Acc. Schedule Management CZL` appears twice, and no codeunit exceeds the
  two-case limit;
- `Prior Known` counts are one `Yes`, five `Uncertain`, and ten `No`; even a
  conservative `Yes` plus `Uncertain` count is six and remains below eight;
- `CZPOP-0033`, `CZPOP-0048`, `CZPOP-0353`, and `CZPOP-0401` were retained for
  negative-control or evidence-boundary coverage without a prior defect
  expectation; and
- no trigger, checklist, materiality, quality, defect, or framework conclusion
  was assigned during selection.

The register is frozen. A case may be replaced only for a documented inclusion
failure, duplicate unit, or unavailable essential context. The completed coarse-
screen worksheet remains unchanged.

## 11. Owner-Reviewed Case Evidence Checkpoint

Evidence acquisition is complete for all sixteen frozen cases. The repository
owner completed evidence-sufficiency review on 2026-08-30. Every case received
the disposition `Evidence sufficient`; no case requires targeted evidence,
correction, or an `Evidence unavailable` qualification before interpretation.

The four temporary owner-review worksheets were working aids used to verify the
source-bound evidence. This section consolidates their accepted evidence into
the authoritative pilot record. The worksheets do not become parallel
authoritative study artifacts.

The checkpoint is intentionally evidence-only:

- selection identities and prior-knowledge labels remain frozen;
- source and platform observations are recorded below;
- retained evidence gaps remain described as absence of retained evidence,
  not evidence of absence;
- owner contextual inference is explicitly separated from fixed-commit source
  evidence;
- trigger screening remains `Unclassified`;
- event-evidence dimensions remain `Pending`;
- all Behavioral Change Impact Checklist rows remain `Pending`; and
- no defect, materiality, architectural-quality, prevalence, or framework
  conclusion is introduced.

### Case `CZP-001` — Financial report print path

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0002` |
| Primary selection bucket | Suppression or substitution |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Acc. Schedule Management CZL.PrintAccScheduleByType` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/AccScheduleManagementCZL.Codeunit.al` |
| Publisher | `Financial Report Mgt..OnBeforePrint` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/FinancialReports/FinancialReportMgt.Codeunit.al` |
| Raise site | `FinancialReportMgt.Codeunit.al:378` |
| Enclosing publisher activity | `Financial Report Mgt..Print`, declaration line 372, body lines 376–384 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Financial Report Mgt..Print` initializes `IsHandled := false`, raises `OnBeforePrint(FinancialReport, IsHandled)`, and exits if `IsHandled` is true.

If execution continues, the standard path sets the financial-report name on the `Account Schedule` report and runs that report.

The publisher event passes `FinancialReport` and `IsHandled` by reference. The event documentation identifies `IsHandled = true` as the mechanism for skipping the standard print processing.

##### Subscriber behavior

`PrintAccScheduleByType` first raises the localization-owned `OnBeforePrintAccScheduleByType(FinancialReport, IsHandled)` event and exits if `IsHandled` is already true.

It then loads the `Acc. Schedule Name` identified by `FinancialReport."Financial Report Row Group"`.

For `Acc. Schedule Type CZL` of `Balance Sheet`, it configures and runs `Balance Sheet CZL` and writes `IsHandled := true`.

For `Acc. Schedule Type CZL` of `Income Statement`, it configures and runs `Income Statement CZL` and writes `IsHandled := true`.

No `IsHandled` assignment is present in the other visible `case` outcomes.

##### Bounded-context evidence

The retained subscriber-context record classifies the subscriber instance as `StaticAutomatic (default)`.

No caller, binding, or test path was retained for `CZPOP-0002`.

This is absence of retained bounded evidence; it is not evidence that no caller, binding, or test context exists.

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

---

### Case `CZP-002` — Reconciliation net-change path

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0308` |
| Primary selection bucket | Suppression or substitution |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Reconciliation Handler CZL.OnBeforeSaveNetChange` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ReconciliationHandlerCZL.Codeunit.al` |
| Publisher | `Reconciliation.OnBeforeSaveNetChange` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/GeneralLedger/Journal/Reconciliation.Page.al` |
| Raise site | `Reconciliation.Page.al:107` |
| Enclosing publisher activity | `Reconciliation.SaveNetChange`, declaration line 102, body lines 105–140 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Reconciliation.SaveNetChange` initializes `IsHandled := false`, raises `OnBeforeSaveNetChange(...)`, and exits immediately when `IsHandled` is true.

If execution continues, the standard path checks the account number, resolves G/L-account or bank-account handling, updates `"Net Change in Jnl."` and `"Balance after Posting"`, raises `OnSaveNetChangeOnBeforeModify`, and modifies the temporary record used as the page source table.

##### Subscriber behavior

The selected subscriber body contains one executable statement:

`IsHandled := true;`

It makes no direct call and does not inspect another event parameter.

##### Companion localization evidence

A separate subscriber in the same localization codeunit, retained as `CZPOP-0307`, subscribes to `Reconciliation.OnAfterSetGenJnlLine`.

That companion subscriber:

- clears the temporary `G/L Account Net Change` records;
- iterates journal lines;
- calls `SaveNetChangeCZL`;
- runs `Exchange Acc. G/L Journal Line`;
- calls `SaveNetChangeCZL` again;
- processes journal allocations; and
- resets and rekeys the temporary records.

`G/L Account Net Change CZL.SaveNetChangeCZL` calculates localized net changes and updates or inserts localized reconciliation records.

This companion evidence comes from a different publisher event. It is surrounding source evidence, not composition evidence recorded for `CZPOP-0308`.

##### Bounded-context evidence

The retained subscriber-context record classifies the selected subscriber as `StaticAutomatic (default)`.

Its `composition_subscriber_ids`, caller paths, binding paths, and test paths are empty.

This is absence of retained bounded evidence, not evidence that no such context exists.

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

---

### Case `CZP-003` — User-specific dimension-value checks

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0097` |
| Primary selection bucket | Validation or invariant influence |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Dimension Mgt. Handler CZL.UserChecksAllowedOnCheckDimValuePostingOnBeforeExit` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/DimensionMgtHandlerCZL.Codeunit.al` |
| Publisher | `DimensionManagement.OnCheckDimValuePostingOnBeforeExit` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/Dimension/DimensionManagement.Codeunit.al` |
| Raise site | `DimensionManagement.Codeunit.al:601` |
| Enclosing publisher activity | `DimensionManagement.CheckDimValuePosting`, declaration line 543, body lines 551–606 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`DimensionManagement.CheckDimValuePosting` performs its standard dimension checks before raising `OnCheckDimValuePostingOnBeforeExit`.

Before the event, the publisher:

- checks blocked dimensions and values;
- collects default dimensions to check;
- evaluates `Code Mandatory`, `Same Code`, and `No Code` value-posting rules;
- checks per-account allowed dimension values; and
- may return `false` in non-collect-errors mode when a new error is recorded.

Immediately before the selected event, the publisher sets `IsHandled := false`.

If the event returns with `IsHandled = true`, the procedure returns `IsChecked`.

Otherwise, it returns the result of comparing the current last error ID with the error ID recorded before the default-dimension checks.

##### Subscriber behavior

The subscriber first calls `IsUserDimCheckAllowed(UserSetup)` and exits if that returns false. It does not read the incoming `IsHandled` value before applying its own logic. If `IsUserDimCheckAllowed(UserSetup)` returns true, it proceeds with the user-specific checks and later writes IsHandled := true.

When user-specific checking is enabled:

- it builds a temporary `Dimension Buffer` for a nonzero dimension-set ID;
- records the current last dimension-error ID;
- calls `CheckUserDimensionValues`;
- sets `IsChecked` according to whether that call produced a new error; and
- sets `IsHandled := true`.

`CheckUserDimensionValues` checks `Selected Dimension` records belonging to the current user setup. It verifies that configured dimensions are present and, when a dimension-value filter exists, that the selected value matches that filter.

Failed checks are recorded through the local `LogError` helper.

##### Runtime condition visible in source

`IsUserDimCheckAllowed` requires:

- `User Setup Adv. Management CZL.IsCheckAllowed()` to return true;
- a nonempty `UserId`;
- an existing `User Setup` record for that user; and
- `"Check Dimension Values CZL"` enabled on that user setup.

##### Failure-context evidence

In the inspected source, `LogError` does not call `Error(...)` directly.

When `ErrorMessageManagement` is active, it calls `LogContextFieldError`.

Otherwise, it initializes and updates the `LastErrorMessage` record.

##### Bounded-context evidence

The retained context classifies the subscriber as `StaticAutomatic (default)`.

No composition-subscriber ID, caller path, binding path, or test path was retained for `CZPOP-0097`.

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

---

### Case `CZP-004` — Conditional dimension-value posting check

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0129` |
| Primary selection bucket | Validation or invariant influence |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Gen.Jnl.Check Line Handler CZL.IsCheckDimensionsEnabledOnCheckDimensionsOnAfterAssignDimTableIDs` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GenJnlCheckLineHandlerCZL.Codeunit.al` |
| Publisher | `Gen. Jnl.-Check Line.OnCheckDimensionsOnAfterAssignDimTableIDs` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/GeneralLedger/Journal/GenJnlCheckLine.Codeunit.al` |
| Raise site | `GenJnlCheckLine.Codeunit.al:925` |
| Enclosing publisher activity | `Gen. Jnl.-Check Line.CheckDimensions`, declaration line 900, body lines 905–930 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Gen. Jnl.-Check Line.CheckDimensions` first raises `OnBeforeCheckDimensions` and exits if its earlier `CheckDone` becomes true.

It then calls `DimMgt.CheckDimIDComb`. A failed dimension combination calls `ThrowGenJnlLineError` before the selected event is reached.

The procedure then fills `TableID` and `No` arrays for:

- account;
- balancing account;
- job;
- salesperson/purchaser; and
- campaign.

It sets `CheckDone := false` and raises `OnCheckDimensionsOnAfterAssignDimTableIDs`.

After that event, `DimMgt.CheckDimValuePosting(...)` is executed only when `CheckDone` remains false.

A false result from `CheckDimValuePosting` calls `ThrowGenJnlLineError`.

##### Subscriber behavior

The subscriber contains one assignment:

`CheckDone := not GenJournalLine.IsCheckDimensionsEnabledCZL();`

##### Source-visible enablement logic

`Gen. Journal Line CZL.IsCheckDimensionsEnabledCZL()` returns true immediately when `"Posting Date" = 0D`.

Otherwise it loads `General Ledger Setup` and returns:

`(ClosingDate("Posting Date") <> "Posting Date") or not GeneralLedgerSetup."Do Not Check Dimensions CZL"`

The selected subscriber assigns the inverse of this result to `CheckDone`.

##### Important flow boundary

The selected `CheckDone` write occurs **after** the standard `CheckDimIDComb` check.

At this event location it directly guards the subsequent `CheckDimValuePosting` call.

This statement records source ordering only. It does not classify whether the case changes an established invariant or triggers BCIR.

##### Bounded-context evidence

The retained context classifies the subscriber as `StaticAutomatic (default)`.

No composition-subscriber ID, caller path, binding path, or test path was retained for `CZPOP-0129`.

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

---

### Case `CZP-005` — Payment-discount VAT-base calculation context

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0146` |
| Primary selection bucket | Posting or transaction behavior |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Gen.Jnl. Post Line Handler CZL.CorrectPmtDiscLCYOnCalcPmtDiscIfAdjVATOnAfterCalcPmtDiscVATBases` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GenJnlPostLineHandlerCZL.Codeunit.al` |
| Publisher | `Gen. Jnl.-Post Line.OnCalcPmtDiscIfAdjVATOnAfterCalcPmtDiscVATBases` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/GeneralLedger/Posting/GenJnlPostLine.Codeunit.al` |
| Raise site | `GenJnlPostLine.Codeunit.al:2845` |
| Enclosing publisher activity | `Gen. Jnl.-Post Line.CalcPmtDiscIfAdjVAT`, declaration line 2746, body lines 2772–2931 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and surrounding posting flow

`Gen. Jnl.-Post Line.CalcPmtDiscIfAdjVAT` exits before the selected event when `OldCVLedgEntryBuf."Original Amt. (LCY)" = 0`.

The procedure establishes payment-discount factors, selects VAT entries for the current transaction, and processes the VAT entries in a loop.

Within the `"Adjust for Payment Discount"` path, the publisher calculates VAT bases, applies its payment-discount calculation and rounding, derives the additional-currency values, and then raises `OnCalcPmtDiscIfAdjVATOnAfterCalcPmtDiscVATBases`.

After the selected raise site, the current `VATBase` is used when initializing `DtldCVLedgEntryBuf2."Amount (LCY)"`.

This records the source ordering and data flow around the selected event only. It does not classify the architectural or behavioral significance of that location.

##### Subscriber behavior

The subscriber first calls `IsAdjustPmtDiscFactorEnabled(OldCVLedgEntryBuf)` and exits when that helper returns false.

When enabled, it:

- calculates `PmtDiscFactorLCY` from `OldCVLedgEntryBuf."Orig. Pmt. Disc. (LCY) CZL"` and `"Original Amt. (LCY)"`;
- calls the localization helper `CalcPmtDiscVATBases(VATEntry, VATBase2)` to calculate a separate `VATBase2`; and
- updates `OldCVLedgEntryBuf."Corr. Pmt. Disc. (LCY) CZL"` by adding `Round(VATBase2 * PmtDiscFactorLCY) - VATBase`.

The subscriber does not assign a new value to the publisher's `VATBase` parameter in the inspected body. Its source-visible mutation is the localized `"Corr. Pmt. Disc. (LCY) CZL"` field on the by-reference `OldCVLedgEntryBuf`.

##### Source-visible enablement condition

`IsAdjustPmtDiscFactorEnabled` returns true when either:

- `OldCVLedgEntryBuf."Orig. Pmt. Disc. CZL"` is nonzero; or
- `OldCVLedgEntryBuf."Orig. Pmt. Disc. (LCY) CZL"` is nonzero.

The publisher's earlier zero-original-amount exit is reached before the selected event, so the inspected event location is not reached through this publisher activity when `"Original Amt. (LCY)" = 0`.

##### Companion localization evidence

The same localization codeunit contains related payment-discount subscribers around the same publisher calculation sequence:

- `CalcPmtDiscFactorLCYOnCalcPmtDiscIfAdjVATOnBeforeVATEntryFind` uses the same enablement helper and can write `PmtDiscFactorLCY`;
- `CorrectPmtDiscLCYOnCalcPmtDiscIfAdjVATOnAfterCalcPmtDiscVATAmounts` uses the same correction field for a VAT-amount calculation; and
- `CorrectPmtDiscLCYOnAfterCalcPmtDiscIfAdjVAT` later adds `"Corr. Pmt. Disc. (LCY) CZL"` to `PmtDiscLCY2`.

These are separate event subscriptions. They are surrounding source evidence for the localized payment-discount calculation sequence and are not recorded as same-target composition subscribers for `CZPOP-0146`.

##### Transaction and failure context

The selected subscriber contains no explicit `Commit`, `Error`, or direct record insert/modify/delete call.

The retained context record contains no transaction marker or error marker for the selected subscriber body.

The publisher activity is part of `Gen. Jnl.-Post Line` processing and reads VAT entries with `ReadIsolation := IsolationLevel::ReadUncommitted` before the selected event. This records source-visible context only and does not establish a transaction-boundary conclusion.

##### Bounded-context evidence

The retained context classifies the subscriber as `StaticAutomatic (default)`.

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no linked test evidence; and
- no same-target CZL peer recorded.

No caller, binding, or test path was retained in the subscriber-context record for `CZPOP-0146`.

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

---

### Case `CZP-006` — Inventory-adjustment posting date

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0209` |
| Primary selection bucket | Posting or transaction behavior |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Inventory Posting Handler CZL.RoundingDateOnPostItemJnlLineOnAfterSetPostingDate` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/InventoryPostingHandlerCZL.Codeunit.al` |
| Publisher | `Inventory Adjustment.OnPostItemJnlLineOnAfterSetPostingDate` |
| Publisher path | `src/Layers/W1/BaseApp/Inventory/Costing/InventoryAdjustment.Codeunit.al` |
| Raise site | `InventoryAdjustment.Codeunit.al:2056` |
| Enclosing publisher activity | `Inventory Adjustment.PostItemJnlLine`, declaration line 2038, body lines 2042–2097 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Inventory Adjustment.PostItemJnlLine` first permits an earlier `OnBeforePostItemJnlLine` event to handle the complete activity.

If execution continues, it copies item, location, and variant information from `OrigValueEntry`.

For the posting date, the publisher:

- uses `OrigValueEntry."Posting Date"` when `GLSetup.IsPostingAllowed(...)` is true and `InventoryPeriod.IsValidDate(...)` is true; otherwise
- assigns `PostingDateForClosedPeriod`.

It then raises `OnPostItemJnlLineOnAfterSetPostingDate`.

After the selected event, the publisher continues populating the item journal line with entry type, document data, source code, posting groups, order/job context, and other values.

##### Subscriber behavior

The subscriber loads `General Ledger Setup` and requires `"Closed Per. Entry Pos.Date CZL"` to be populated through `TestField`.

It then assigns `ItemJournalLine."Posting Date"` in one of two source-visible branches.

For a rounding value entry when `"Rounding Date CZL" <> 0D`:

- if `ValueEntry."Posting Date" >= GeneralLedgerSetup."Rounding Date CZL"`, it assigns the value-entry posting date;
- otherwise it assigns `"Rounding Date CZL"`.

For all other cases:

- if `ValueEntry."Posting Date" >= GeneralLedgerSetup."Closed Per. Entry Pos.Date CZL"`, it assigns the value-entry posting date;
- otherwise it assigns `"Closed Per. Entry Pos.Date CZL"`.

The helper `IsPostingAllowedCZL(ValueEntryPostingDate, ClosingDate)` consists of the comparison `ValueEntryPostingDate >= ClosingDate`.

##### Source-visible flow boundary

The publisher has already selected a posting date before the selected event is raised.

The selected subscriber receives `ItemJournalLine` by reference and assigns its `"Posting Date"` after that standard selection but before the publisher continues populating the remaining posting line fields.

This is a source-ordering observation only. It does not classify whether the resulting date assignment is a replacement, invariant change, transaction change, or defect.

##### Failure and transaction context

`GeneralLedgerSetup.TestField("Closed Per. Entry Pos.Date CZL")` can stop execution when the required setup value is not populated.

The selected subscriber contains no explicit `Commit`.

The retained context record contains no transaction marker or explicit error marker for the subscriber body; the `TestField` call is nevertheless directly visible in the inspected source.

##### Bounded-context evidence

The retained context classifies the subscriber as `StaticAutomatic (default)`.

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no linked test evidence; and
- no same-target CZL peer recorded.

No caller, binding, or test path was retained in the subscriber-context record for `CZPOP-0209`.

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

---

### Case `CZP-007` — Manually bound G/L-entry correction subscriber

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0125` |
| Primary selection bucket | Manual runtime participation |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `G/L Entry as Correction CZL.SetCorrectionOnBeforeInsertGlEntry` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/GLEntryasCorrectionCZL.Codeunit.al` |
| Publisher | `Gen. Jnl.-Post Line.OnBeforeInsertGlEntry` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/GeneralLedger/Posting/GenJnlPostLine.Codeunit.al` |
| Raise site | `GenJnlPostLine.Codeunit.al:2327` |
| Enclosing publisher activity | `Gen. Jnl.-Post Line.InsertGLEntry`, declaration line 2322, body lines 2325–2364 |
| Subscriber instance | `Manual` |
| Retained caller paths | None retained in the subscriber-context record |
| Retained binding paths | None retained in the subscriber-context record |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Gen. Jnl.-Post Line.InsertGLEntry` initializes a local `IsHandled := false` and raises `OnBeforeInsertGlEntry(GenJnlLine, GLEntry, IsHandled)` near the start of the activity.

If `IsHandled` remains false, the publisher proceeds with:

- G/L-account validation;
- amount-rounding checks;
- balance-check updates;
- `GLEntry.UpdateDebitCredit(GenJnlLine.Correction)`;
- preparation of `TempGLEntryBuf`; and
- insertion into the temporary G/L-entry buffer.

`OnAfterInsertGLEntry` is raised after the handled block.

The selected subscriber accepts only the by-reference `GenJnlLine` parameter in its subscriber signature and does not set the publisher's `IsHandled` variable.

##### Subscriber behavior

`G/L Entry as Correction CZL` is:

- `Access = Internal`;
- `SingleInstance = true`; and
- `EventSubscriberInstance = Manual`.

When the selected subscriber runs, it first checks whether the elapsed time since `EnableTime` exceeds `EnableDuration`.

If the binding has timed out, it:

- calls `Disable()`;
- logs warning telemetry with `Session.LogMessage`; and
- exits.

Otherwise it assigns:

`GenJnlLine.Correction := true;`

The publisher later reads `GenJnlLine.Correction` in `GLEntry.UpdateDebitCredit(GenJnlLine.Correction)`.

##### Manual binding mechanism

The codeunit exposes:

- `Enable()`, which delegates to `Enable(DefaultDuration())`;
- `Enable(Duration)`, which records the current time and duration and calls `BindSubscription(this)`; and
- `Disable()`, which calls `ClearAll()` and `UnbindSubscription(this)`.

`DefaultDuration()` returns `5000`.

The source therefore explicitly defines both the manual binding mechanism and a timeout guard for the selected subscriber.

##### Bounded runtime-participation evidence

The completed coarse screen records `runtime_participation = "Binding Evidence Available"`.

It identifies two subscribers in `Gen.Jnl. Post Line Handler CZL` that bracket a deferral G/L-entry insertion:

1. `OnPostDeferralPostBufferOnBeforeInsertGLEntryForDeferralAccount` calls `GLEntryasCorrectionCZL.Enable()` only when:
   - `GLEntry.Amount < 0`;
   - `GLEntry."Posting Date" = GenJournalLine."Posting Date"`; and
   - `GLEntry."G/L Account No." = GenJournalLine."Account No."`.

2. `OnPostDeferralPostBufferOnAfterInsertGLEntry` calls `GLEntryasCorrectionCZL.Disable()`.

In the fixed BaseApp source, `OnPostDeferralPostBufferOnBeforeInsertGLEntryForDeferralAccount(...)` is raised immediately before `InsertGLEntry(...)`, and `OnPostDeferralPostBufferOnAfterInsertGLEntry(...)` is raised immediately after that call.

This establishes a bounded source path in which the manual subscription is enabled before the selected publisher activity and disabled after it. It does not establish that every call to `InsertGLEntry` has this binding active.

##### Failure and transaction context

The selected subscriber's timeout path logs a warning and exits rather than directly raising an error.

No explicit `Commit` is present in the selected subscriber, `Enable`, or `Disable`.

The publisher activity itself contains validation and buffering operations that may fail, but this worksheet does not infer transaction semantics from those operations.

##### Bounded-context evidence

The earlier retained subscriber-context record has empty caller and binding path arrays for `CZPOP-0125`.

The later completed coarse screen supplements that mechanical context with the source-verified manual binding evidence described above and records no linked test evidence and no same-target CZL peer.

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

---

### Case `CZP-008` — Manually bound item-tracking expiration-date subscriber

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0245` |
| Primary selection bucket | Manual runtime participation |
| Prior known | Uncertain |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Item Tracking Doc. Handler CZL.FillExpirationDateOnAfterFillTrackingSpecBufferFromItemLedgEntry` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ItemTrackingDocHandlerCZL.Codeunit.al` |
| Publisher | `Item Tracking Doc. Management.OnAfterFillTrackingSpecBufferFromItemLedgEntry` |
| Publisher path | `src/Layers/W1/BaseApp/Inventory/Tracking/ItemTrackingDocManagement.Codeunit.al` |
| Raise site | `ItemTrackingDocManagement.Codeunit.al:140` |
| Enclosing publisher activity | `Item Tracking Doc. Management.FillTrackingSpecBufferFromILE`, declaration line 126, body lines 129–143 |
| Subscriber instance | `Manual` |
| Retained caller paths | None retained in the subscriber-context record |
| Retained binding paths | None retained in the subscriber-context record |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Item Tracking Doc. Management.FillTrackingSpecBufferFromILE` iterates the supplied temporary item-ledger entries.

For each entry where `TrackingExists()` is true, it:

- copies item-tracking setup from the item-ledger entry;
- calls `FillTrackingSpecBuffer(...)` to create or update a temporary `Tracking Specification` record; and
- raises `OnAfterFillTrackingSpecBufferFromItemLedgEntry(TempTrackingSpecBuffer, TempItemLedgEntry)`.

The selected event therefore occurs after the standard tracking-specification buffer has been filled for that item-ledger entry and before the procedure advances to the next item-ledger entry.

##### Subscriber behavior

`Item Tracking Doc. Handler CZL` declares `EventSubscriberInstance = Manual`.

The selected subscriber:

- copies tracking setup from `TempItemLedgerEntry`;
- calls `ItemTrackingManagement.ExistingExpirationDate(...)` using the item number, variant code, copied tracking setup, `false`, and an `EntriesExist` output parameter;
- assigns the returned date to `TempTrackingSpecification."Expiration Date"`; and
- calls `TempTrackingSpecification.Modify()`.

The subscriber therefore directly updates the temporary tracking-specification record supplied by the publisher event.

##### Bounded runtime-participation evidence

The completed coarse screen records `runtime_participation = "Binding Evidence Available"`.

In `Sales Shipment CZL`, when `ShowLotSN` is true, the fixed source:

1. sets `ItemTrackingDocManagement.SetRetrieveAsmItemTracking(true)`;
2. calls `BindSubscription(ItemTrackingDocHandlerCZL)`;
3. calls `ItemTrackingDocManagement.RetrieveDocumentItemTracking(...)` for `Database::"Sales Shipment Header"`;
4. calls `UnbindSubscription(ItemTrackingDocHandlerCZL)`; and
5. resets `SetRetrieveAsmItemTracking(false)`.

Within the fixed BaseApp source, `RetrieveDocumentItemTracking` routes `Database::"Sales Shipment Header"` to `RetrieveTrackingSalesShipment`.

`RetrieveTrackingSalesShipment` calls `FindShptRcptEntries(...)` for qualifying shipment lines.

`FindShptRcptEntries(...)` retrieves item-ledger entries and calls `FillTrackingSpecBufferFromILE(...)`, which contains the selected raise site.

This provides a source-visible route from the bounded manual binding in `Sales Shipment CZL` to the selected publisher event.

##### Runtime boundary

The source-visible binding described above exists only inside the `ShowLotSN` branch of `Sales Shipment CZL`.

The selected codeunit itself contains no `Enable` or `Disable` wrapper; the binding and unbinding are performed by the report that holds the codeunit variable.

This worksheet records the demonstrated sales-shipment route only. It does not assume that this is the only possible binding path in BCApps.

##### Failure and transaction context

The selected subscriber contains no explicit `Commit` or direct `Error` call.

It invokes `ExistingExpirationDate(...)` and then `Modify()` on a temporary tracking-specification record.

The retained context record contains no transaction marker or error marker for the selected subscriber body.

No conclusion about transaction boundaries, database persistence, or failure propagation is made here.

##### Bounded-context evidence

The earlier retained subscriber-context record has empty caller and binding path arrays for `CZPOP-0245`.

The later completed coarse screen supplements that mechanical context with the source-verified `Sales Shipment CZL` binding path described above and records no linked test evidence and no same-target CZL peer.

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

---

### Case `CZP-009` — Account-schedule result mutation

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0001` |
| Primary selection bucket | Mutable influence without demonstrated full replacement |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Acc. Schedule Management CZL.CalcCZLOnAfterCalcCellValue` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/AccScheduleManagementCZL.Codeunit.al` |
| Publisher | `AccSchedManagement.OnAfterCalcCellValue` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/FinancialReports/AccSchedManagement.Codeunit.al` |
| Raise site | `AccSchedManagement.Codeunit.al:838` |
| Enclosing publisher activity | `AccSchedManagement.CalcCellValue`, declaration line 700, body lines 710–849 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |
| Same-target CZL composition evidence | `CZPOP-0004` |

#### 11.2 Source observations

##### Publisher and default flow

`AccSchedManagement.CalcCellValue` calculates a decimal `Result` for an account-schedule cell.

Before the selected event, the publisher may obtain the result from the temporary cell-value cache or calculate it according to the account-schedule line's totaling type. The inspected source includes standard branches for formulas, posting or total accounts, cost types, cash-flow accounts, account categories, and an extensibility `else` branch.

When a value is newly calculated, the publisher raises:

`OnAfterCalcCellValue(AccSchedLine, ColumnLayout, Result, AccountScheduleLine, GLAcc)`

after the standard calculation and before assigning `Result` into `TempAccSchedCellValue.Value` and inserting that temporary cache record.

After the enclosing handled block, the publisher later raises `OnCalcCellValueOnBeforeExit(...)`.

This records the source ordering around the selected event. It does not classify whether a subscriber mutation replaces, corrects, filters, or otherwise materially changes an established responsibility.

##### Subscriber behavior

`CalcCZLOnAfterCalcCellValue` receives `AccSchedLine` and `Result` by reference.

For totaling types `Posting Accounts` and `Total Accounts`, it evaluates the localized `"Calc CZL"` setting:

- `"When Positive"` — if `Result < 0`, it assigns `Result := 0`;
- `"When Negative"` — if `Result > 0`, it assigns `Result := 0`;
- `Never` — it assigns `Result := 0`.

For totaling type `"Constant CZL"`, it calls:

`Evaluate(Result, AccSchedLine.Totaling)`

and leaves the body without an explicit error action when `Evaluate` returns false.

The selected subscriber therefore reads and may write the publisher's by-reference `Result`.

##### Source-visible data-flow boundary

When the publisher has calculated a new cell value, the selected event occurs before:

`TempAccSchedCellValue.Value := Result;`

The result value visible after all subscribers to this event return is therefore the value copied into the temporary cell-value buffer at this source location.

This is a direct source observation only. No statement is made here about which subscriber, if any, determines the final value when more than one subscriber participates.

##### Same-target CZL composition evidence

The retained context record identifies `CZPOP-0004` as a same-target CZL peer.

That subscriber, `ExtendedOnAfterCalcCellValue`, also subscribes to `AccSchedManagement.OnAfterCalcCellValue`.

For totaling type `"Custom CZL"`, the peer:

- copies filters from `SourceAccScheduleLine`;
- obtains the date-filter range; and
- assigns `Result := AccSChedExtensionMgtCZL.CalcCustomFunc(...)`.

The selected subscriber and the same-target peer operate on different source-visible totaling-type conditions in the inspected bodies.

No subscriber execution-order guarantee is inferred from source order in this worksheet.

##### Failure and transaction context

The selected subscriber contains no explicit `Commit`, `Error`, insert, modify, or delete call.

Its only direct call is `Evaluate(...)` in the `"Constant CZL"` branch.

The retained context contains no transaction marker or error marker for the selected body.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- same-target CZL peers recorded; and
- no linked test evidence.

No caller, binding, or test path was retained in the subscriber-context record for `CZPOP-0001`.

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

---

### Case `CZP-010` — Purchase-line negative correction marker

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0081` |
| Primary selection bucket | Mutable influence without demonstrated full replacement |
| Prior known | Uncertain |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Corrections Posting Mgt. CZL.PurchLineSetNegativeOnAfterInitOutstandingQty` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CorrectionsPostingMgtCZL.Codeunit.al` |
| Publisher | `Purchase Line.OnAfterInitOutstandingQty` |
| Publisher path | `src/Layers/W1/BaseApp/Purchases/Document/PurchaseLine.Table.al` |
| Raise site | `PurchaseLine.Table.al:4275` |
| Enclosing publisher activity | `Purchase Line.InitOutstanding`, declaration line 4254, body lines 4257–4279 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Purchase Line.InitOutstanding` first raises `OnBeforeInitOutstanding` with an `IsHandled` parameter and exits when that earlier event handles the activity.

If execution continues, the publisher calculates outstanding quantity fields differently for credit-document and non-credit-document cases.

After those quantity calculations, it raises:

`OnAfterInitOutstandingQty(Rec, xRec)`

at the selected raise site.

After the selected event, the publisher calculates `"Completely Received"`, raises `OnInitOutstandingOnBeforeInitOutstandingAmount`, and calls `InitOutstandingAmount()`.

##### Subscriber behavior

`PurchLineSetNegativeOnAfterInitOutstandingQty` loads `General Ledger Setup`.

When `GeneralLedgerSetup."Mark Neg. Qty as Correct. CZL"` is true, it assigns:

`PurchaseLine."Negative CZL" := (PurchaseLine.Quantity < 0);`

When the setup field is false, the inspected subscriber performs no assignment to `"Negative CZL"`.

The selected subscriber does not modify the outstanding quantity fields calculated immediately before the event in the inspected body.

##### Source-visible data-flow boundary

The selected subscriber receives the current `Purchase Line` by reference after the publisher has initialized outstanding-quantity values and before `"Completely Received"` and outstanding-amount initialization are processed.

The source-visible mutation is the localized `"Negative CZL"` field.

This worksheet does not infer how that localized field is consumed elsewhere or whether it changes posting behavior; those questions belong to later interpretation unless additional evidence is explicitly requested.

##### Surrounding localization pattern

The inspected localization codeunit contains analogous subscribers for sales and service lines.

The adjacent sales subscriber loads the same setup and assigns `"Negative CZL"` from `Quantity < 0` after sales-line outstanding initialization.

This surrounding pattern is recorded only as localization source context. It is not same-target composition evidence for `Purchase Line.OnAfterInitOutstandingQty`.

##### Failure and transaction context

The selected subscriber contains no explicit `Commit`, `Error`, insert, modify, or delete call.

`GeneralLedgerSetup.Get()` is the only direct call recorded by the retained context.

The retained record contains no transaction marker or error marker for this subscriber body.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

No caller, binding, or test path was retained for `CZPOP-0081`.

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

---

### Case `CZP-011` — CNB currency-exchange service setup

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0017` |
| Primary selection bucket | Workflow, reporting, integration, or delegated behavior |
| Prior known | Uncertain |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `CNB Curr. Exch. Rate Mgt. CZL.SetupCurrencyExchangeRateServiceOnBeforeSetupCurrencyExchRateService` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CNBCurrExchRateMgtCZL.Codeunit.al` |
| Publisher | `Curr. Exch. Rate Update Setup.OnBeforeSetupCurrencyExchRateService` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/Currency/CurrExchRateUpdateSetup.Table.al` |
| Raise site | `CurrExchRateUpdateSetup.Table.al:366` |
| Enclosing publisher activity | `Curr. Exch. Rate Update Setup.SetupService`, declaration line 364, body lines 365–372 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |
| Retained transaction marker | Subscriber `Commit` at line 36 |

#### 11.2 Source observations

##### Publisher and default flow

`Curr. Exch. Rate Update Setup.SetupService` raises:

`OnBeforeSetupCurrencyExchRateService(Rec)`

at the beginning of the activity.

After the event returns, the publisher checks `IsEmpty()` on the exchange-rate update setup table.

If the table is still empty, the publisher:

- calls `Commit()`;
- runs codeunit `"Set Up Curr Exch Rate Service"` through `CODEUNIT.Run`; and
- logs error telemetry when that codeunit run returns false.

If the table is not empty after the event, this inspected `if IsEmpty()` body is not executed.

This is a source-visible control-flow statement only. It does not classify the selected subscriber as a replacement or suppression mechanism.

##### Subscriber behavior

The selected subscriber receives `CurrExchRateUpdateSetup` by reference and returns early when any of the following is true:

- the `Currency` table is empty;
- `CurrExchRateUpdateSetup` is not empty; or
- `CurrExchRateUpdateSetup.WritePermission()` is false.

When those guards pass, it loads `General Ledger Setup`.

If `GeneralLedgerSetup."LCY Code" = 'CZK'`, it calls:

`SetupCNBDataExchange(GetCNB_URI());`

After that conditional block, the subscriber calls `Commit()`.

Therefore, for an invocation that passes the three early-exit guards, the outer subscriber's `Commit()` is source-visible whether or not the LCY code equals `CZK`.

##### Delegated CNB setup behavior

`SetupCNBDataExchange(PathToCNBService)` first exits when a `Curr. Exch. Rate Update Setup` record with the CNB code already exists.

Otherwise the inspected helper:

- locates an existing CNB data-exchange line definition when present;
- calls `CreateCurrencyExchangeSetup(...)`, which initializes and inserts a `Curr. Exch. Rate Update Setup` record;
- sets a web-service URL when the supplied path begins with `http`;
- when no data-exchange definition exists, creates line-definition data, invokes XML column-definition generation, and maps CNB exchange data; and
- calls `Commit()` at the end.

The selected subscriber can therefore call a helper that contains its own persistent record writes and `Commit`, and the selected subscriber then contains a separate outer `Commit`.

This records source-visible operations only; no assessment of transaction appropriateness or architectural impact is made here.

##### Source-visible publisher interaction

The publisher decides whether to run the standard `"Set Up Curr Exch Rate Service"` codeunit by checking whether the setup table is empty after all subscribers to the selected event return.

When `SetupCNBDataExchange` inserts a setup record, that source-visible table state can be observed by the publisher's subsequent `IsEmpty()` check.

The worksheet does not infer the final runtime outcome for all configurations, because the selected subscriber contains guards and the event may have other subscribers outside the bounded CZL evidence.

##### Failure and transaction context

The retained subscriber-context record explicitly records `Commit` at subscriber line 36.

`SetupCNBDataExchange` contains another explicit `Commit`.

The helper also performs record insert/modify operations and invokes `Suggest Col. Definition - XML.GenerateDataExchColDef(...)`.

The publisher contains its own `Commit()` immediately before running the standard setup codeunit when the table remains empty.

No claim is made here about transaction correctness, rollback expectations, external-call behavior, or failure propagation.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- a transaction marker;
- no same-target CZL peer recorded; and
- no linked test evidence.

No caller, binding, or test path was retained for `CZPOP-0017`.

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

---

### Case `CZP-012` — EET records in Navigate results

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0257` |
| Primary selection bucket | Workflow, reporting, integration, or delegated behavior |
| Prior known | Uncertain |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Navigate Handler CZL.OnAfterNavigateFindRecords` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/NavigateHandlerCZL.Codeunit.al` |
| Publisher | `Navigate.OnAfterNavigateFindRecords` |
| Publisher path | `src/Layers/W1/BaseApp/Foundation/Navigate/Navigate.Page.al` |
| Raise site | `Navigate.Page.al:822` |
| Enclosing publisher activity | `Navigate.FindRecords`, declaration line 786, body lines 796–854 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`Navigate.FindRecords` can exit before the selected event when an earlier `OnBeforeFindRecordsProcedure` handles the activity or when all document/posting-date filters are empty.

If execution continues, the publisher:

- optionally opens a progress window;
- resets and clears the temporary `Document Entry` records;
- searches posted documents;
- searches ledger entries;
- searches multiple unposted purchase and sales document types; and
- searches unposted general journal lines.

It then raises:

`OnAfterNavigateFindRecords(...)`

at the selected raise site.

After that event, the publisher evaluates:

`DocExists := Rec.FindFirst();`

and uses the resulting document-entry set when deriving source information or deciding whether to show a no-records message.

The publisher later raises `OnAfterFindRecords(...)`, optionally updates the form, and closes the progress window.

##### Subscriber behavior

The selected subscriber delegates its body to:

`FindEETEntries(DocumentEntry, DocNoFilter);`

It does not directly assign another event parameter in the inspected body.

##### Delegated EET lookup behavior

`FindEETEntries` executes only when `EETEntryCZL.ReadPermission()` is true.

When permission is available, it:

- resets `EETEntryCZL`;
- uses the `"Document No."` key;
- applies `DocNoFilter` to `"Document No."`; and
- calls `DocumentEntry.InsertIntoDocEntry(...)` with:
  - table `Database::"EET Entry CZL"`;
  - document type `Quote`;
  - the EET table caption; and
  - `EETEntryCZL.Count()`.

The `EETEntryCZL` variable is declared with:

`[SecurityFiltering(SecurityFilter::Filtered)]`

The helper therefore uses the current read-permission/security-filter context when deriving the source-visible EET count.

##### Source-visible data-flow boundary

The publisher raises the selected event after its standard document searches and before `DocExists := Rec.FindFirst()`.

The selected helper receives `DocumentEntry` by reference and can call `InsertIntoDocEntry(...)` before the publisher tests whether the resulting temporary document-entry set contains a record.

This records source ordering and mutation access only. It does not classify whether the EET entry is an extension, replacement, workflow change, reporting change, or defect.

##### Companion localization evidence

The same localization codeunit also subscribes to `Navigate.OnBeforeShowRecords`.

When the selected `TempDocumentEntry."Table ID"` is `Database::"EET Entry CZL"`, that companion subscriber:

- filters EET entries by the current document-number filter;
- runs `"EET Entry Card CZL"` when the recorded count is one, otherwise runs the default page for the EET record; and
- sets `IsHandled := true`.

This is a different publisher event and is recorded as surrounding workflow evidence, not same-target composition evidence for `CZPOP-0257`.

##### Failure and transaction context

The selected subscriber and `FindEETEntries` contain no explicit `Commit` or direct `Error` call.

`ReadPermission()` acts as a source-visible guard; when it returns false, the helper performs no EET lookup or `DocumentEntry` insertion.

The retained context contains no transaction marker or error marker for the selected body.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

No caller, binding, or test path was retained for `CZPOP-0257`.

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

---

### Case `CZP-013` — Preserving customer registration-number state during contact copy

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0048` |
| Primary selection bucket | Negative controls |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Contact Handler CZL.SaveRegistrationNoOnBeforeCustCopyFieldsFromCont` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ContactHandlerCZL.Codeunit.al` |
| Publisher | `CustVendBank-Update.OnBeforeCustCopyFieldsFromCont` |
| Publisher path | `src/Layers/W1/BaseApp/CRM/BusinessRelation/CustVendBankUpdate.Codeunit.al` |
| Raise site | `CustVendBankUpdate.Codeunit.al:93` |
| Enclosing publisher activity | `CustVendBank-Update.CustCopyFieldsFromCont`, declaration line 88, body lines 91–98 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`CustVendBank-Update.CustCopyFieldsFromCont` initializes `IsHandled := false` and raises:

`OnBeforeCustCopyFieldsFromCont(Cust, Cont, IsHandled)`

before the standard contact-to-customer field copy.

If `IsHandled` remains false, the publisher executes:

`Cust.TransferFields(Cont);`

The selected subscriber does not receive or write the publisher's `IsHandled` parameter.

The enclosing `UpdateCustomer` activity loads the existing customer before calling `CustCopyFieldsFromCont`, then restores selected identity/audit fields, raises `OnAfterUpdateCustomer`, modifies the customer record, performs standard VAT-registration logging when applicable, and finally raises `OnAfterUpdateCustomerProcedure`.

##### Subscriber behavior

The selected subscriber contains one direct call:

`Customer.SaveRegistrationNoCZL();`

`Customer CZL.SaveRegistrationNoCZL()` assigns the table-extension variable:

`RegistrationNo := GetRegistrationNoTrimmedCZL();`

`GetRegistrationNoTrimmedCZL()` returns the current customer `"Registration Number"` truncated to 20 characters.

The selected subscriber therefore does not directly write a Customer table field in its inspected body. Its delegated helper captures the current registration-number value in the `Customer CZL` record instance's extension state before the publisher's subsequent `Cust.TransferFields(Cont)` call.

##### Source-visible companion behavior

The same localization codeunit separately subscribes to `CustVendBank-Update.OnAfterUpdateCustomerProcedure`.

That companion subscriber, `RegNoLogInitOnAfterUpdateCustomer`, checks whether:

- the resulting customer `"Registration Number"` is nonempty; and
- `Customer.GetSavedRegistrationNoCZL()` differs from the resulting `"Registration Number"`.

When both conditions hold, it calls `RegistrationLogMgtCZL.LogCustomer(Customer)`.

`GetSavedRegistrationNoCZL()` returns the `RegistrationNo` value previously held by the `Customer CZL` table-extension instance.

This is surrounding workflow evidence from a different publisher event. It is not same-target composition evidence for `CZPOP-0048`.

##### Source-visible data-flow boundary

Within the inspected `UpdateCustomer` path, the selected event occurs after `Cust.Get(...)` has loaded the existing customer and before `Cust.TransferFields(Cont)` copies contact fields into that customer record.

The companion `OnAfterUpdateCustomerProcedure` event occurs later, after `Cust.Modify()` and after the standard VAT-registration logging condition in `UpdateCustomer`.

This records ordering and state use only. It does not classify the selected subscriber as preservation, augmentation, bookkeeping, or material behavioral change.

##### Failure and transaction context

The selected subscriber and `SaveRegistrationNoCZL()` contain no explicit `Commit`, `Error`, insert, modify, or delete call.

The enclosing BaseApp `UpdateCustomer` activity later calls `Cust.Modify()`.

The companion localization subscriber may call `RegistrationLogMgtCZL.LogCustomer(...)`.

No transaction-boundary or failure-propagation conclusion is made here.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

No caller, binding, or test path was retained for `CZPOP-0048`.

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

---

### Case `CZP-014` — VAT reporting date after G/L-entry field copy

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0401` |
| Primary selection bucket | Negative controls |
| Prior known | Yes |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `VAT Date Handler CZL.UpdateVatDateOnAfterCopyGenJnlLineFromGLEntry` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/VATDateHandlerCZL.Codeunit.al` |
| Publisher | `G/L Entry.OnAfterCopyGLEntryFromGenJnlLine` |
| Publisher path | `src/Layers/W1/BaseApp/Finance/GeneralLedger/Ledger/GLEntry.Table.al` |
| Raise site | `GLEntry.Table.al:1035` |
| Enclosing publisher activity | `G/L Entry.CopyFromGenJnlLine`, declaration line 993, body lines 994–1036 |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Publisher and default flow

`G/L Entry.CopyFromGenJnlLine` begins by calling:

`SetVATDate(GenJnlLine);`

It then copies a sequence of standard journal-line values into the G/L entry, including posting/document metadata, dimensions, source information, job number, quantity, journal template/batch information, reason code, user ID, number series, IC partner code, and production order number.

At the end of that copy sequence, it raises:

`OnAfterCopyGLEntryFromGenJnlLine(Rec, GenJnlLine);`

The selected event is therefore raised after the publisher's own `SetVATDate` call and after the other inspected standard field assignments.

##### Publisher `SetVATDate` behavior

The fixed BaseApp source defines `SetVATDate` as follows:

- when `GenJnlLine."VAT Reporting Date" = 0D`, it assigns the G/L entry `"VAT Reporting Date"` from `GeneralLedgerSetup.GetVATDate(GenJnlLine."Posting Date", GenJnlLine."Document Date")`;
- otherwise, it assigns the G/L entry `"VAT Reporting Date"` directly from `GenJnlLine."VAT Reporting Date"`.

This source-visible distinction occurs before the selected event.

##### Subscriber behavior

The selected subscriber contains one assignment:

`GLEntry."VAT Reporting Date" := GenJournalLine."VAT Reporting Date";`

Both records are supplied to the event, and the selected subscriber writes the by-reference `GLEntry`.

It performs no direct call and contains no condition in the inspected body.

##### Source-visible data-flow boundary

The selected assignment occurs after `SetVATDate`.

Therefore:

- when `GenJournalLine."VAT Reporting Date"` is nonzero, both inspected source paths assign that explicit journal VAT reporting date; and
- when `GenJournalLine."VAT Reporting Date" = 0D`, the publisher first calls `GeneralLedgerSetup.GetVATDate(...)`, while the selected subscriber later assigns `0D` to `GLEntry."VAT Reporting Date"`.

The actual date returned by `GeneralLedgerSetup.GetVATDate(...)` is not evaluated in this worksheet.

This is a direct source/data-flow observation. It does not classify the selected subscriber as redundant, corrective, destructive, material, or defective.

##### Failure and transaction context

The selected subscriber contains no explicit `Commit`, `Error`, direct call, insert, modify, or delete operation.

The publisher activity shown here copies values into the `G/L Entry` record but does not itself insert the record in the inspected activity.

The retained context contains no transaction marker or error marker for the selected subscriber body.

##### Bounded-context evidence

The completed coarse screen records:

- publisher evidence available;
- raise-site evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

No caller, binding, or test path was retained for `CZPOP-0401`.

##### Owner contextual inference (not fixed-commit source evidence)

Owner historical/context note: Based on prior familiarity with Czech localization evolution, I suspect that this subscriber may be residual code from the period when Czech localization maintained a localization-specific VAT date field before VAT Reporting Date became available in the broader application model.
My working hypothesis is that an earlier version of this subscriber may have copied the former CZL-specific VAT-date value to the G/L entry. During later migration/refactoring to the application-wide VAT Reporting Date field, the assignment may have been mechanically adapted to the new standard field even though BaseApp G/L Entry.CopyFromGenJnlLine had by then acquired its own SetVATDate(GenJnlLine) logic.
This historical origin has not been verified against earlier BCApps commits and must therefore be treated as owner inference, not source evidence for the fixed pilot commit. The fixed source independently demonstrates the current behavior: BaseApp calls SetVATDate(GenJnlLine) and the selected subscriber subsequently assigns GenJournalLine."VAT Reporting Date" to GLEntry."VAT Reporting Date".
The possibility that the subscriber is obsolete or residual does not affect its inclusion in the frozen sample and must not predetermine its later trigger, materiality, correctness, or defect classification.

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

---

### Case `CZP-015` — Finance-charge company bank-account validation event

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0033` |
| Primary selection bucket | Borderline or uncertain cases |
| Prior known | Uncertain |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Company Bank Acc. Handler CZL.FinanceChargeMemoUpdateBankAccountCodeCZLOnAfterValidateCompanyBankAccountCode` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/CompanyBankAccHandlerCZL.Codeunit.al` |
| Platform target | `Finance Charge Memo Header.Company Bank Account Code` |
| Target event | `OnAfterValidateEvent` |
| Event class | `Database Trigger Event` |
| AL publisher path | Not applicable — runtime-published database trigger event |
| AL raise site | Not applicable — runtime-published database trigger event |
| Platform semantics reference | Microsoft Learn, `Event types - Business Central` |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Platform event contract

The retained context resolves this target as a `Database Trigger Event`, not an AL source publisher.

Microsoft documents database trigger events as predefined events published by the runtime rather than events raised programmatically in AL. They do not appear as publisher methods in a table object.

For a table field, `OnAfterValidateEvent` is executed after the field is validated when its value has changed.

The selected target is:

`Finance Charge Memo Header.Company Bank Account Code`

No AL publisher method or AL raise site exists for this runtime-published event.

##### Target field source

The BaseApp `Finance Charge Memo Header` field `"Company Bank Account Code"`:

- is a `Code[20]` field;
- has a table relation to `Bank Account` filtered by the header `"Currency Code"`; and
- has no source-defined field `OnValidate` trigger in the inspected BaseApp field declaration.

The same BaseApp table contains `SetCompanyBankAccount()`, which calls:

`Validate("Company Bank Account Code", BankAccount.GetDefaultBankAccountNoForCurrency("Currency Code"));`

This is one source-visible AL path that can validate the target field. It is not recorded as the only possible validation path.

##### Subscriber behavior

The selected subscriber runs on `OnAfterValidateEvent` for `"Company Bank Account Code"` and contains one statement:

`Rec.Validate("Bank Account Code CZL", Rec."Company Bank Account Code");`

The subscriber therefore initiates validation of the localized `"Bank Account Code CZL"` field using the current standard `"Company Bank Account Code"` value.

##### Delegated localized-field validation

`Finance Charge Memo Header CZL."Bank Account Code CZL"` has its own table-extension `OnValidate` trigger.

When the localized bank-account code is blank, that trigger clears the localized bank-information fields through `UpdateBankInfoCZL(...)` and exits.

When nonblank, it:

- gets the corresponding `Bank Account`; and
- calls `UpdateBankInfoCZL(...)` with bank account number, branch number, name, transit number, IBAN, and SWIFT code.

`UpdateBankInfoCZL(...)` assigns the localized bank-information fields and raises `OnAfterUpdateBankInfoCZL(Rec)`.

##### Source-visible validation boundary

Microsoft's platform semantics place the selected `OnAfterValidateEvent` after validation of `"Company Bank Account Code"` when that field value changes.

The selected subscriber then performs a second, explicit `Validate(...)` on the localized `"Bank Account Code CZL"` field, whose table-extension `OnValidate` logic is source-visible.

This records event ordering and delegated validation only. It does not classify the behavior as synchronization, propagation, augmentation, duplication, or material change.

##### Failure and transaction context

The selected subscriber contains no explicit `Commit` or `Error`.

The delegated localized field validation can execute `BankAccount.Get(...)` when the localized bank-account code is nonblank.

The target standard field's table relation and the localized field's own table relation/validation remain part of the surrounding validation context.

No transaction-boundary or failure-propagation conclusion is made here.

##### Bounded-context evidence

The completed coarse screen records:

- publisher or platform evidence available;
- raise or trigger evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

The subscriber-context record contains:

- `publisher_resolution_status = "Resolved Platform or Trigger Event"`;
- no publisher path;
- no publisher procedure;
- no AL raise-site path; and
- the Microsoft Learn platform-semantics reference.

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

---

### Case `CZP-016` — Service-header currency-factor pre-validation event

#### 11.1 Selection and identity

| Field | Value |
|---|---|
| Population ID | `CZPOP-0353` |
| Primary selection bucket | Borderline or uncertain cases |
| Prior known | No |
| BCApps commit | `397d01199c321e774edaf23a7290fee40f75c6a6` |
| Evidence sufficiency | Owner reviewed — Evidence sufficient |
| Targeted evidence before interpretation | None requested |
| Subscriber | `Service Header Handler CZL.UpdateVATCurrencyfactorCZLOnBeforeCurrencyFactorValidate` |
| Subscriber path | `src/Apps/CZ/CoreLocalizationPack/app/Src/Codeunits/ServiceHeaderHandlerCZL.Codeunit.al` |
| Platform target | `Service Header.Currency Factor` |
| Target event | `OnBeforeValidateEvent` |
| Event class | `Database Trigger Event` |
| AL publisher path | Not applicable — runtime-published database trigger event |
| AL raise site | Not applicable — runtime-published database trigger event |
| Platform semantics reference | Microsoft Learn, `Event types - Business Central` |
| Retained caller paths | None retained |
| Retained binding paths | None retained |
| Retained test paths | None retained |

#### 11.2 Source observations

##### Platform event contract

The retained context resolves this target as a `Database Trigger Event`, not an AL source publisher.

Microsoft documents `OnBeforeValidateEvent` for table fields as executing before a field is validated when its value has changed.

The selected target is:

`Service Header.Currency Factor`

Because the event is runtime-published, there is no AL publisher method and no explicit AL raise-site statement to inspect.

##### Standard target-field validation

The BaseApp `Service Header."Currency Factor"` field is a decimal field with an `OnValidate` trigger.

That trigger checks whether:

`"Currency Factor" <> xRec."Currency Factor"`

and, when changed, calls:

`UpdateServLinesByFieldNo(FieldNo("Currency Factor"), false);`

Under the Microsoft-documented trigger-event semantics, the selected `OnBeforeValidateEvent` occurs before this table-field validation behavior when the field value changes.

##### Subscriber behavior

The selected subscriber contains one direct call:

`Rec.UpdateVATCurrencyFactorCZL();`

It does not directly assign another event parameter in the subscriber body.

##### Delegated VAT-currency-factor behavior

`Service Header CZL.UpdateVATCurrencyFactorCZL()` first checks `"Currency Code"`.

When `"Currency Code" = ''`, it assigns:

`"VAT Currency Factor CZL" := 0;`

and exits.

Otherwise, when:

- `"Currency Factor" <> xRec."Currency Factor"`; and
- `"Currency Factor" <> "VAT Currency Factor CZL"`

the helper evaluates two branches.

If:

`xRec."Currency Factor" = "VAT Currency Factor CZL"`

it validates:

`"VAT Currency Factor CZL"` with the current `"Currency Factor"` and exits.

Otherwise, it asks through `ConfirmManagement.GetResponseOrDefault(...)` whether `"VAT Currency Factor CZL"` should be updated and, when confirmed, validates that field with the current `"Currency Factor"`.

The localized `"VAT Currency Factor CZL"` field's own `OnValidate` trigger requires `"Currency Code"` to be populated through `TestField("Currency Code")`.

##### Source-visible validation boundary

The selected subscriber is invoked through the platform `OnBeforeValidateEvent` for `"Currency Factor"`.

Its delegated helper can therefore inspect the new/current `"Currency Factor"`, compare it with `xRec."Currency Factor"` and the localized VAT currency factor, and potentially validate the localized field before the BaseApp `"Currency Factor"` field `OnValidate` trigger executes.

After the platform before-event completes, the BaseApp field `OnValidate` can call `UpdateServLinesByFieldNo(...)` when the currency factor changed.

This records ordering and delegated validation only. It does not classify the selected behavior as synchronization, reordering, validation influence, augmentation, or material change.

##### Failure and interaction context

The selected subscriber contains no explicit `Commit` or direct `Error`.

`UpdateVATCurrencyFactorCZL()` can invoke a confirmation response and can validate `"VAT Currency Factor CZL"`.

That localized field's `OnValidate` contains `TestField("Currency Code")`, which can stop validation when its required condition is not met; however, the helper's explicit blank-currency branch exits before those `Validate(...)` calls.

The BaseApp target-field `OnValidate` can update service lines after the selected before-event.

No conclusion about user interaction appropriateness, failure propagation, transaction boundaries, or line-update semantics is made here.

##### Bounded-context evidence

The completed coarse screen records:

- publisher or platform evidence available;
- raise or trigger evidence available;
- established-flow evidence available;
- runtime participation as `Static Automatic`;
- no same-target CZL peer recorded; and
- no linked test evidence.

The subscriber-context record contains:

- `publisher_resolution_status = "Resolved Platform or Trigger Event"`;
- no publisher path;
- no publisher procedure;
- no AL raise-site path; and
- the Microsoft Learn platform-semantics reference.

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

No interpretive case findings are available. The selection register remains
frozen and owner-accepted, and evidence acquisition plus evidence-sufficiency
owner review are complete for all sixteen cases. Trigger classification,
event-evidence interpretation, and checklist analysis remain pending.

## 15. Candidate Framework Implications

None. The pilot is designed to test candidate concepts, not to accept them.

## 16. Execution Checklist

- [x] Reproduce and retain the event-subscriber population inventory.
- [x] Record its discovery command, tool versions, checksum, and limitations.
- [x] Freeze the dependency-aware source boundary and context record protocol.
- [x] Implement and automatically validate the subscriber-context resolver.
- [x] Complete owner source review of the retained validation records.
- [x] Resolve publisher and static runtime context for every retained CZL
      subscriber.
- [x] Freeze the coarse evidence-availability screening protocol and schema.
- [x] Implement and automatically validate coarse-screen worksheet preparation.
- [x] Complete focused owner re-review of corrected `CZPOP-0270`.
- [x] Retain the complete 448-record initial coarse-screen worksheet.
- [x] Complete coarse evidence-availability screening.
- [x] Mark prior-known status before bucket assignment.
- [x] Fill and freeze the 16-case selection register.
- [x] Copy the empty case record for every selected case.
- [x] Inspect publisher, raise site, subscriber, binding, caller, and test
      context for each case.
- [x] Complete owner evidence-sufficiency review for all sixteen frozen cases.
- [ ] Complete trigger screening before recording impact conclusions.
- [ ] Apply the checklist without forcing unsupported rows.
- [ ] Preserve counterevidence, uncertain cases, and failed classifications.
- [ ] Compare cases only after all records are complete.
- [x] Synchronize repository-index metadata for the selection-freeze checkpoint.
- [ ] Update findings, limitations, and the research log only after study
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
- **[C6]** Orden. "BCApps Czech Subscriber Context Resolution Protocol."
  `Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md`.

## 18. Revision History

### 0.13.0 — 2026-08-30

- Consolidated owner-reviewed evidence-only records for all sixteen frozen cases
  into the authoritative pilot document.
- Recorded `Evidence sufficient` for all sixteen cases, with no targeted
  evidence request, correction requirement, or evidence-unavailable disposition
  remaining before interpretation.
- Preserved source-visible manual binding, composition, delegated-helper,
  transaction-marker, and runtime-published platform-event evidence where
  applicable without introducing trigger or checklist conclusions.
- Preserved the CZP-014 historical explanation as owner contextual inference,
  explicitly separate from fixed-commit source evidence.
- Marked evidence acquisition and evidence-sufficiency owner review complete
  while keeping trigger screening, event-evidence interpretation, checklist
  analysis, materiality, defect, and framework conclusions pending.

### 0.12.0 — 2026-08-08

- Operationalized `Prior Known` as case-specific familiarity predating the
  concrete subscriber's first targeted inspection within the Orden pilot.
- Recorded the owner-provided prior-knowledge values for all sixteen selected
  population records.
- Filled, reconciled, owner-accepted, and froze the complete 16-case selection
  register with two cases in each pre-registered bucket.
- Preserved the immutable coarse-screen worksheet and kept trigger,
  checklist, materiality, quality, defect, and framework conclusions pending.

### 0.11.0 — 2026-07-21

- Recorded focused owner acceptance of corrected `CZPOP-0270`.
- Authorized population-wide coarse screening.
- Retained 448 ordered worksheets in the initial `Not Screened` state.
- Kept screening decisions, prior-knowledge labeling, and selection pending.

### 0.10.0 — 2026-07-21

- Recorded conditional owner review of the six coarse-screen validation records.
- Corrected the upstream procedure-body boundary rule and regenerated all
  context and validation records.
- Limited re-review to corrected `CZPOP-0270` while keeping screening closed.

### 0.9.0 — 2026-07-19

- Implemented and automatically validated deterministic coarse-screen
  worksheet preparation.
- Retained six protected `Not Screened` validation records for owner review.
- Kept coarse screening, prior-knowledge labeling, and case selection pending.

### 0.8.0 — 2026-07-19

- Fixed a separate one-record-per-subscriber coarse evidence-availability
  screening protocol and machine-readable record contract.
- Separated readiness and descriptive strata from prior knowledge, selection,
  trigger classification, and impact analysis.
- Kept screening execution and all subsequent operations pending.

### 0.7.0 — 2026-07-19

- Recorded owner acceptance of the technical-validation records.
- Completed reproducible generation of one schema-valid static context record
  for each retained subscriber.
- Kept coarse screening, prior-knowledge labeling, and case selection pending.

### 0.6.0 — 2026-07-19

- Recorded the implemented resolver and passing automated technical checks.
- Retained owner review as the remaining gate before population-wide context
  generation.
- Kept coarse screening and case selection unperformed.

### 0.5.0 — 2026-07-19

- Fixed a five-application source search boundary for dependency-aware
  subscriber-context resolution.
- Added the context record and resolution protocol without executing coarse
  screening or case selection.
- Deferred resolver implementation, technical validation, and population-wide
  context resolution.

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
