---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-VALIDATION-001
  title: BCApps Czech Coarse Screen Preparation Technical Validation
  type: Empirical Study Validation Record
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records automated validation of deterministic coarse-screen preparation,
  structured publisher-activity prefill, and preservation of accepted screening
  decisions during upstream context refresh.

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

The worksheet-preparation generator and focused regression checks pass. The
initial technical validation and owner review authorized population-wide
screening, and the separate B01 checkpoint was later accepted after citation
correction.

After the resolver added structured enclosing-activity context, the six-record
technical-validation dataset was regenerated twice with byte-identical output.
The complete worksheet was refreshed through the preservation procedure. All 16
accepted B01 records retained their screening decisions and reviewer evidence;
the 432 later records remain `Not Screened`.

The preservation operation performs no prior-knowledge labeling, case
selection, `CZP` assignment, trigger result, checklist result, quality judgment,
or impact finding.

## 2. Implemented Preparation Behavior

`Scripts/Prepare_BCApps_CZ_Coarse_Screen.py`:

- rejects a context dataset whose SHA-256 differs from the fixed input;
- requires 448 unique context identities and rejects a non-resolved context
  input;
- creates one worksheet template per context record without modifying context;
- pre-fills subscriber, publisher or platform, raise or trigger, composition,
  test, and runtime evidence fields from named context fields;
- pre-fills `established_flow = Available` when structured source
  `raise_site_contexts` are present and otherwise retains `Targeted Search
  Required`;
- records a deterministic publisher-activity observation for each structured
  raise-site context;
- adds a specific binding-search question for manual subscribers without linked
  binding evidence;
- derives controlled stratum indicators in fixed order;
- fixes every workflow and analysis field to its pre-screen value; and
- supports deterministic validation and full-template modes.

`full-template` creates 448 `Not Screened` worksheet templates. Updating the
active retained worksheet after screening has begun requires the separate
preservation procedure; the template must not overwrite accepted screening
fields.

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

- six focused preparation tests pass, including retained mechanical-structure
  and protected-state assertions;
- five batch-execution tests pass, including B01 preservation and exact
  established-activity boundaries;
- two validation generations are byte-identical;
- all six validation records validate against the current coarse-screen schema;
- every validation ID resolves to the current context dataset;
- indicator order and mechanical derivation are deterministic;
- manual binding-present and binding-not-linked paths remain distinct;
- all six validation records remain `Not Screened`; and
- no context or later-workflow field is mutated.

Current checksums:

- worksheet generator:
  `902eeb069670300a9e73f49ad2cb4a0a149af3ad3641454663cc80aeec25b244`;
- preparation regression tests:
  `a2f3836aed28f6024221409afc778642f41c05fd1e7e8ae3ecd7898c01e9a910`;
- batch-execution regression tests:
  `c4b553e4c6453d27852bc1e4bccce534535449271609ebc241f6c4f7c0f0e6bb`;
- coarse-screen schema:
  `296fb8ef928c12c18489887e17b159bce73792c4ee5c933bfa9ea899d5a3657b`;
- retained technical-validation JSON Lines:
  `b73d0a860e71db9aa366c3d16fb81c74a467163135b9702bc5d5658916413148`;
  and
- current preserved 448-record worksheet:
  `ff368978fa8ae921fed1419bf069f5b954d9846bed8f84c635231a780bca6a0b`.

The pristine initial worksheet remains preserved in Git history and remains the
historical source of the fixed batch membership manifest.

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

Automated preparation, preservation validation, and the accepted B01 checkpoint
are complete. The preservation report established that all 16 B01 records
changed only in `context_dataset_sha256`; 432 unscreened records were regenerated
from the repaired context; and no protected-field error occurred.

The current worksheet contains 448 ordered, schema-valid records: 16
`Ready for Prior-Knowledge Labeling` and 432 `Not Screened`. This technical
acceptance does not classify behavior, quality, impact, or selection.

The next permitted screening action is `CZCS-B02` (`CZPOP-0017` through
`CZPOP-0032`). Prior-knowledge labeling and every downstream analytical
operation remain separate.

## 9. Revision History

### 0.4.0 — 2026-07-27

- Regenerated the six-record validation dataset from the repaired context
  baseline.
- Recorded structured publisher-activity prefill and current checksums.
- Added regression evidence for preservation of the accepted B01 checkpoint.
- Accepted the 448-record preserved worksheet with 16 ready and 432 unscreened
  records.


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
