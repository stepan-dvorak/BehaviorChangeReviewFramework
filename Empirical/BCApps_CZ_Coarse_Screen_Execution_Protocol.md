---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-EXECUTION-001
  title: BCApps Czech Coarse Screen Execution Protocol
  type: Empirical Study Protocol
  version: 0.2.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Defines the auditable session, batching, checkpoint, and disposition rules
  for executing the authorized 448-record evidence-availability screen without
  entering prior knowledge, case selection, or behavioral analysis.

quality:
  review: Self Reviewed
  evidence: Partial
  editorial: Reviewed

audience:
  - Researchers
  - Business Central Architects
  - Business Central Developers
  - AI Assistants

depends_on:
  - Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md
  - Empirical/BCApps_CZ_Coarse_Screen_Technical_Validation.md
  - Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl

related_documents:
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/Data/BCApps_CZ_Coarse_Screen_Batches.json
  - 00_Research_Log.md

study:
  method: Ordered Human Evidence-Availability Screening
  subject: Complete 448-record CZL coarse-screen worksheet
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Fixed Batch Manifest and Per-Record Source Citations

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - coarse-screening
  - execution-protocol
  - reviewer-checkpoint
---

# BCApps Czech Coarse Screen Execution Protocol

## 1. Purpose and Authority

This document operationalizes the authorized screen defined by
`Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md`. The
screening protocol remains authoritative for evidence fields, targeted-search
limits, status decisions, and deferred work. This document adds only execution
controls.

No step in this protocol may assign prior knowledge, a selection bucket, a
`CZP` identifier, a trigger result, a checklist result, materiality, quality,
or defect status.

## 2. Fixed Execution Inputs

- fixed BCApps commit: `397d01199c321e774edaf23a7290fee40f75c6a6`;
- current corrected context dataset SHA-256:
  `3267f7ffb1e3adbfff789169d328d44ab4a116eaa1d322121bd897086e6edfc9`;
- pristine initial worksheet canonical LF SHA-256:
  `0a60f6a24466195fd2cd94d98fd3d4f1518ac24f2bc84f00c7435059d0219729`;
- accepted B01 worksheet before context preservation:
  `f53e70313c334e28b05ece9f9893c139ad8c01968a52f04c49dc52a19b3e5915`;
- pre-execution preserved worksheet canonical LF SHA-256:
  `0e138671c16d2b976e30f4160a7e584d45ec7339d548c3a2941c916a7a9bd68d`;
- completed population-wide worksheet canonical LF SHA-256:
  `f5fd8b7332fdee1baaf1b294f8ba9f1144ee01e6502d7ea484b4c82d139da8c9`;
- 448 ordered records in `Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl`;
- batch manifest `Empirical/Data/BCApps_CZ_Coarse_Screen_Batches.json`; and
- schema `Schemas/BCApps_CZ_Coarse_Screen.schema.json`.

The pristine initial worksheet is preserved in Git history. The batch manifest
continues to fingerprint that historical planning baseline and defines only
membership and order. Screening edits and explicit preservation refreshes update
the single retained worksheet; a parallel results file must not be introduced.

## 3. Batch Plan

The population is divided mechanically into 28 contiguous batches of 16
records. Batch membership follows lexical `inventory_id` order and is not
stratified or chosen for expected results. The batch manifest is generated from
the pristine worksheet and contains no screening result.

`CZCS-B01` contains `CZPOP-0001` through `CZPOP-0016`. It is the initial process
calibration batch. Calibration concerns consistent application and recording
of the fixed rules; it must not tune the rules to obtain a preferred readiness
rate or case population.

### 3.1 Owner-Authorized Population-Wide Execution

After B01 owner acceptance and the pre-B02 evidence-usability correction, the
repository owner authorized `CZCS-B02` through `CZCS-B28` to be screened in one
population-wide change set on 2026-07-29. Batch boundaries remain fixed planning
and audit partitions. They are used for traceability and count reconciliation,
not as separate delivery gates and not to tune decisions by observed results.

## 4. Record Review Procedure

For each record in the active batch:

1. confirm the `inventory_id`, context checksum, subscriber path, and body;
2. inspect the resolved publisher or platform evidence and raise or trigger;
3. identify the bounded established activity and cite exact source paths and
   symbols in `screening_observations`;
4. resolve the prefilled targeted question or retain a narrower unanswered
   question;
5. for a manual subscriber, inspect the recorded binding evidence or perform
   only the permitted bounded search;
6. assess all eight evidence-availability fields;
7. apply exactly one screening status under the parent protocol;
8. set `screened_by` and `screened_on` for every reviewed record;
9. confirm the four protected downstream fields; and
10. validate the complete 448-record file, not only the edited batch.

Observations must distinguish source fact from reviewer interpretation. A path
without a concise statement of what it establishes is insufficient. An empty
mechanical array is not a missing-evidence decision.

## 5. Allowed Batch Outcomes

Every reviewed record ends as one of:

- `Ready for Prior-Knowledge Labeling`;
- `Targeted Context Required`; or
- `Unavailable for Selection`.

During batch-isolated execution, `Not Screened` remains mandatory outside
completed batches. Under the owner-authorized population-wide execution, all
records in `CZCS-B02` through `CZCS-B28` are active in the same change set and
must reach a terminal status together. Temporary `Targeted Context Required`
records are not skipped; their exact question and bounded-search disposition
remain visible until resolved or retained.

No summary count may be interpreted as behavioral, defect, or quality
prevalence.

## 6. Initial Calibration Checkpoint

After all 16 records in `CZCS-B01` have been reviewed, stop before
`CZPOP-0017`. The repository owner reviews:

- every changed field in the 16 records;
- exact support for each established-flow decision;
- consistency of status rules across similar records;
- whether targeted searches remained within the fixed boundary;
- whether observations avoided trigger, materiality, and quality language;
- schema validity and the continued presence of all 448 records; and
- unchanged protected downstream fields.

The checkpoint decision is `Accepted` or `Correction Required`. Corrections are
applied to the first batch and re-reviewed. Changes to the governing screening
rules require an explicit protocol revision and reassessment of all already
screened records; they must not be introduced as silent calibration notes.

## 7. Population-Wide Execution Session

The authorized population-wide session reviews `CZPOP-0017` through
`CZPOP-0448` while preserving accepted B01 byte-for-byte. The implementation
must:

- retain the fixed manifest order and batch membership as audit partitions;
- apply the record procedure in Section 4 to every active record;
- resolve only bounded targeted searches allowed by the parent protocol;
- leave no active record as `Not Screened`;
- preserve all four protected downstream fields and all stratum indicators;
- validate the complete 448-record worksheet and repository; and
- record final disposition counts, reviewer, date, resolved searches, checksum,
  and validation results in one completion checkpoint.

Unexpected ambiguity, extraction defects, or evidence outside the fixed
boundary remain results, not reasons to omit a record. A systematic upstream
defect stops the population session until corrected and revalidated.

## 8. Completion Gate

Population screening is complete only when all 28 batches are accepted, all
448 records have a non-`Not Screened` status, the file is schema-valid, and the
final counts reconcile to 448. The completion summary reports only evidence
readiness and retained limitations.

Prior-knowledge labeling begins afterward as a separate owner-controlled
operation. Selection, trigger classification, checklist analysis, and
synthesis remain deferred.

## 9. Current State and Next Action

Population-wide evidence-availability screening is complete. All 448 records are
`Ready for Prior-Knowledge Labeling`: 16 accepted B01 records dated 2026-07-21
and 432 population-session records dated 2026-07-29. The completed worksheet
canonical LF SHA-256 is `f5fd8b7332fdee1baaf1b294f8ba9f1144ee01e6502d7ea484b4c82d139da8c9`.

Accepted B01 is byte-identical. Six manual-subscriber runtime questions
(`CZPOP-0125`, `CZPOP-0200` through `CZPOP-0203`, and `CZPOP-0245`) were resolved
from bounded binding or activation evidence at the fixed BCApps revision. No
record remains `Not Screened`, `Targeted Context Required`, or `Unavailable for
Selection`. Protected downstream fields and stratum indicators remain unchanged.

The next operation is a separate owner-review checkpoint for the population-wide
AI-assisted decisions. Prior-knowledge labeling and every downstream analytical
operation remain deferred until separately authorized.

## 10. Revision History

### 0.2.0 — 2026-07-29

- Recorded owner authorization for one population-wide B02-through-B28 execution
  change set.
- Retained fixed batches as planning and audit partitions rather than delivery
  gates.
- Completed all 448 evidence-readiness dispositions while preserving B01 and all
  protected downstream fields.
- Kept owner review, prior knowledge, selection, trigger, checklist, and
  synthesis work separate.


### 0.1.4 — 2026-07-29

- Recorded the pre-B02 evidence-usability correction.
- Preserved accepted B01 byte-for-byte.
- Updated the worksheet checksum after deterministic regeneration of 432
  unscreened records.
- Kept B02 membership and execution rules unchanged.


### 0.1.3 — 2026-07-27

- Updated the active context and worksheet checksums after resolver repair and
  controlled preservation.
- Distinguished the historical pristine worksheet fingerprint from the current
  retained screening worksheet.
- Recorded preservation of every accepted B01 decision and protected field.
- Kept `CZCS-B02` as the next permitted screening action.


### 0.1.2 — 2026-07-25

- Recorded owner-required citation corrections for eight source-published
  records in `CZCS-B01`.
- Accepted the initial owner checkpoint after correction.
- Determined that no recalibration or calibration-range extension is required.
- Authorized continuation with `CZCS-B02` under the unchanged screening rules.


### 0.1.1 — 2026-07-21

- Recorded completion of the 16-record calibration batch and its evidence-
  readiness disposition.
- Opened the initial owner checkpoint and kept every later batch unscreened.

### 0.1.0 — 2026-07-21

- Fixed 28 contiguous 16-record batches in lexical order.
- Defined the per-record execution procedure and protected boundaries.
- Required an owner checkpoint after the first batch.
- Kept all screening decisions and downstream operations unperformed.
