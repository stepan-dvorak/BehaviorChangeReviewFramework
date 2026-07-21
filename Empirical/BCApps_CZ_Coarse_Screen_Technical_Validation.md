---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-VALIDATION-001
  title: BCApps Czech Coarse Screen Preparation Technical Validation
  type: Empirical Study Validation Record
  version: 0.3.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records automated validation of deterministic coarse-screen worksheet
  preparation while preserving human review and every screening decision as
  pending operations.

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
  - Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md
  - Empirical/BCApps_CZ_Subscriber_Context_Manifest.md

related_documents:
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - 00_Research_Log.md

study:
  method: Deterministic Worksheet Preparation Technical Validation
  subject: Fixed 448-record CZL subscriber-context dataset
  data_access: Retained Repository Dataset
  reproducibility: Automated Checks and Owner Review Passed

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - coarse-screening
  - technical-validation
  - worksheet-preparation
---

# BCApps Czech Coarse Screen Preparation Technical Validation

## 1. Status and Scope

The worksheet-preparation generator is implemented and its automated checks
pass. Owner review accepted five records and conditionally accepted the set
after finding an upstream body-boundary error in `CZPOP-0270`. The context
resolver and derived records were corrected. Focused owner re-review then
confirmed body range `22-33`, the regenerated worksheet observation, and
workflow protection. Population-wide screening is authorized.

Every retained record remains `Not Screened`. The output contains no readiness
decision, reviewer identity, review date, prior-knowledge label, selection
status change, `CZP` ID, trigger result, checklist result, or impact finding.

## 2. Implemented Preparation Behavior

`Scripts/Prepare_BCApps_CZ_Coarse_Screen.py`:

- rejects a context dataset whose SHA-256 differs from the fixed input;
- requires 448 unique context identities and rejects a non-resolved context
  input;
- creates one worksheet record per context record without modifying context;
- pre-fills subscriber, publisher or platform, raise or trigger, composition,
  test, and runtime evidence fields from named context fields;
- keeps `established_flow` as `Targeted Search Required` because its readiness
  requires bounded human review;
- adds a specific binding-search question for manual subscribers without linked
  binding evidence;
- derives controlled stratum indicators in fixed order;
- fixes every workflow and analysis field to its pre-screen value; and
- supports deterministic validation and full-template modes.

`full-template` creates 448 `Not Screened` worksheet records. The complete
initial worksheet is retained as
`Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl`. It does not constitute executed
screening.

## 3. Mechanical Prefill Mapping

| Worksheet field | Context source |
|---|---|
| Event-class indicator | `target_event_class` |
| Publisher-mechanism indicator | `publisher_resolution_status` |
| Static or manual indicator | `subscriber_instance` |
| Mutable-read or write indicator | Non-empty control-parameter arrays |
| Transaction or error indicator | Non-empty marker arrays |
| Composition field and indicator | `composition_subscriber_ids` |
| Test field and indicator | `test_context_paths` |
| Manual binding availability | `binding_context_paths` |
| Subscriber body observation | Retained path and body line fields |

The mapping records syntax and bounded context only. It does not evaluate
subscriber effect, established behavior, materiality, case bucket, impact, or
quality.

## 4. Deterministic Validation Set

The protocol rule produced six deduplicated records:

| Inventory ID | Validation coverage |
|---|---|
| `CZPOP-0001` | First Integration Event; first static subscriber; first same-target CZL peer |
| `CZPOP-0002` | First record without same-target CZL peers after deduplication needs |
| `CZPOP-0009` | First Database Trigger Event |
| `CZPOP-0125` | First manual subscriber and first manual subscriber without binding evidence |
| `CZPOP-0270` | First manual subscriber with binding evidence |
| `CZPOP-0386` | First Page Trigger Event |

All six records remain `Not Screened`, have null reviewer and date, and retain
`Unknown`, `Unselected`, and `Not Evaluated` protected values. They receive no
`CZP` IDs.

## 5. Automated Validation

- five focused regression tests pass, including retained full-template
  reproduction and protected-state assertions;
- two validation generations are byte-identical;
- all six records validate against
  `Schemas/BCApps_CZ_Coarse_Screen.schema.json`;
- every validation ID resolves to the fixed context dataset;
- indicator order and mechanical derivation are deterministic;
- manual binding-present and binding-not-linked paths remain distinct;
- all records remain `Not Screened`; and
- no context or later-workflow field is mutated.

Checksums:

- worksheet generator:
  `3633ec834ecc589b232c59198e7bbd4755ef0f6fa3ad82d68bdb08e865e4029a`;
- regression tests:
  `030519d5f590656c8ad48c136a132d47c21c6154f080aa44d745053041fc355b`;
- retained technical-validation JSON Lines:
  `87bb7580adcf144f8daa13a77baf00c65bac9ff4603476a307afba684e5627c3`.
- retained 448-record initial worksheet:
  `0a60f6a24466195fd2cd94d98fd3d4f1518ac24f2bc84f00c7435059d0219729`.

## 6. Required Owner Review

For each retained record, compare the worksheet with its context record and
confirm:

1. exact `CZPOP` identity;
2. correct event, publisher, runtime, mutable, marker, composition, and test
   indicators;
3. correct static or manual runtime prefill;
4. an additional binding question only when manual binding is not linked;
5. correct body-path observation;
6. `Not Screened` status and null reviewer/date; and
7. unchanged protected workflow and analysis fields.

This review validates preparation only. The owner must not answer the targeted
questions or assign readiness during validation.

## 7. Threats and Limitations

- A correct mechanical prefill does not make an evidence-readiness decision.
- Non-empty binding or test arrays do not prove runtime participation or test
  sufficiency.
- Empty arrays do not prove absence.
- A mutable, transaction, error, manual, or composition indicator can appear
  important and bias later screening.
- The validation set covers actual fixed-data variants but cannot exercise a
  future parser error not present in the current dataset.
- Human reviewers may inadvertently begin behavioral interpretation while
  checking preparation.

## 8. Acceptance Status and Next Step

Automated technical validation and owner review are complete. The repository
owner confirmed that regenerated `CZPOP-0270` cites body range `22-33`, that its
worksheet observation is correct, and that protected workflow fields remain
unchanged. The full-screening gate is open.

The retained 448-record worksheet is the authorized initial screening dataset.
Screening may proceed in lexical order under the pre-registered protocol.
Prior-knowledge labeling and case selection remain later operations.

## 9. Revision History

### 0.3.0 — 2026-07-21

- Recorded focused owner acceptance of corrected `CZPOP-0270`.
- Authorized population-wide coarse screening.
- Retained the deterministic 448-record initial worksheet and its checksum.
- Preserved all 448 records as `Not Screened` with protected downstream fields.

### 0.2.0 — 2026-07-21

- Recorded conditional owner acceptance and the upstream `CZPOP-0270` defect.
- Regenerated the retained validation set from the corrected context dataset.
- Limited follow-up owner review to the corrected `CZPOP-0270` record.
- Kept population-wide coarse screening unauthorized.

### 0.1.0 — 2026-07-19

- Recorded deterministic worksheet-preparation implementation and mapping.
- Retained six validation records without executing screening.
- Recorded automated checks, owner-review instructions, limitations, and the
  closed full-screening gate.
