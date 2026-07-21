---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-EXECUTION-001
  title: BCApps Czech Coarse Screen Execution Protocol
  type: Empirical Study Protocol
  version: 0.1.0
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
- corrected context dataset SHA-256:
  `381d476096615b757fecd92e52e3325b65b20384adfa8e9ae1bac792a99c8dfb`;
- initial worksheet canonical LF SHA-256:
  `0a60f6a24466195fd2cd94d98fd3d4f1518ac24f2bc84f00c7435059d0219729`;
- 448 ordered records in `Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl`;
- batch manifest `Empirical/Data/BCApps_CZ_Coarse_Screen_Batches.json`; and
- schema `Schemas/BCApps_CZ_Coarse_Screen.schema.json`.

The initial worksheet is preserved in Git history. Screening edits update the
retained file; a new parallel results file must not be introduced.

## 3. Batch Plan

The population is divided mechanically into 28 contiguous batches of 16
records. Batch membership follows lexical `inventory_id` order and is not
stratified or chosen for expected results. The batch manifest is generated from
the pristine worksheet and contains no screening result.

`CZCS-B01` contains `CZPOP-0001` through `CZPOP-0016`. It is the initial process
calibration batch. Calibration concerns consistent application and recording
of the fixed rules; it must not tune the rules to obtain a preferred readiness
rate or case population.

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

`Not Screened` remains mandatory outside completed batches. A batch may contain
temporary `Targeted Context Required` records. Such records are not skipped:
their exact question and bounded search disposition remain visible.

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

## 7. Subsequent Sessions

After owner acceptance of `CZCS-B01`, process later batches in manifest order.
One commit should contain one completed batch unless a targeted-search
resolution is intentionally recorded as a separate follow-up. At each commit:

- all earlier accepted records remain unchanged except for documented
  corrections;
- the active batch contains no `Not Screened` records;
- later batches remain `Not Screened`;
- the complete worksheet is schema-valid; and
- the research log records the batch ID, range, disposition counts, reviewer,
  date, unresolved targeted searches, and validation result.

Unexpected ambiguity, extraction defects, or evidence outside the fixed
boundary are results, not reasons to omit a record. An upstream extraction
defect stops the active batch until corrected and revalidated.

## 8. Completion Gate

Population screening is complete only when all 28 batches are accepted, all
448 records have a non-`Not Screened` status, the file is schema-valid, and the
final counts reconcile to 448. The completion summary reports only evidence
readiness and retained limitations.

Prior-knowledge labeling begins afterward as a separate owner-controlled
operation. Selection, trigger classification, checklist analysis, and
synthesis remain deferred.

## 9. Current State and Next Action

The execution plan is prepared; no batch has been screened. The next action is
to review `CZCS-B01` (`CZPOP-0001` through `CZPOP-0016`) and submit its complete
16-record result for the initial owner checkpoint.

## 10. Revision History

### 0.1.0 — 2026-07-21

- Fixed 28 contiguous 16-record batches in lexical order.
- Defined the per-record execution procedure and protected boundaries.
- Required an owner checkpoint after the first batch.
- Kept all screening decisions and downstream operations unperformed.
