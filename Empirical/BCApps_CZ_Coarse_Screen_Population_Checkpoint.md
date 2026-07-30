---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-COARSE-SCREEN-POPULATION-001
  title: BCApps Czech Population-Wide Coarse Screen Checkpoint
  type: Empirical Study
  version: 0.1.0
  status: Active

classification:
  domain: Empirical Research
  layer: Evidence
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Records completion, disposition counts, bounded manual-subscriber searches,
  preservation guarantees, and validation results for the population-wide
  BCApps Czech coarse evidence-availability screen.

quality:
  review: Self Reviewed
  evidence: Verified
  editorial: Reviewed

audience:
  - Researchers
  - Reviewers
  - AI Assistants

depends_on:
  - Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md
  - Empirical/BCApps_CZ_Coarse_Screen_Execution_Protocol.md
  - Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl

related_documents:
  - Empirical/BCApps_CZ_Coarse_Screen_Owner_Review_CZCS_B01.md
  - Empirical/BCApps_CZ_Coarse_Screen_Technical_Validation.md

study:
  method: Structured AI-Assisted Population Evidence-Availability Screening
  subject: Complete 448-record BCApps Czech Core Localization EventSubscriber population
  data_access: Retained Repository Dataset and Fixed Public BCApps Source Revision
  reproducibility: Fixed Inputs, Per-Record Evidence, Regression Tests, and Git Patch

tags:
  - empirical
  - coarse-screen
  - population
  - evidence-readiness
  - BCApps
---

# BCApps Czech Population-Wide Coarse Screen Checkpoint

## 1. Scope and Authority

The repository owner authorized `CZCS-B02` through `CZCS-B28` to be executed in
one population-wide change set after acceptance of calibration batch `CZCS-B01`.
The fixed 28 batches remain planning and audit partitions; they were not used as
separate decision or delivery gates.

This checkpoint records evidence availability only. It does not assign prior
knowledge, selection, trigger, checklist, materiality, quality, defect, or BCIR
results.

## 2. Fixed Inputs

- Orden baseline: `4be61a8831e1aa2bd0738326c8ea370bd1256d33`;
- BCApps source revision: `397d01199c321e774edaf23a7290fee40f75c6a6`;
- subscriber-context SHA-256: `3267f7ffb1e3adbfff789169d328d44ab4a116eaa1d322121bd897086e6edfc9`;
- pre-execution worksheet canonical LF SHA-256:
  `0e138671c16d2b976e30f4160a7e584d45ec7339d548c3a2941c916a7a9bd68d`;
- completed worksheet canonical LF SHA-256: `f5fd8b7332fdee1baaf1b294f8ba9f1144ee01e6502d7ea484b4c82d139da8c9`;
- reviewer: `OpenAI Codex`;
- population-session date: `2026-07-29`.

## 3. Disposition

| Evidence-readiness status | Count |
|---|---:|
| Ready for Prior-Knowledge Labeling | 448 |
| Targeted Context Required | 0 |
| Unavailable for Selection | 0 |
| Not Screened | 0 |
| Total | 448 |

The 16 B01 records retain their accepted 2026-07-21 reviewer metadata. Records
`CZPOP-0017` through `CZPOP-0448` were screened on 2026-07-29. The newly screened
population contains 333 source-published records and
99 platform-trigger records.

## 4. Bounded Manual-Subscriber Searches

Six mechanical runtime-participation questions required bounded source review:

| Inventory IDs | Resolution evidence |
|---|---|
| `CZPOP-0125` | `G/L Entry as Correction CZL` binds itself in `Enable`, unbinds itself in `Disable`, and is activated around the deferral G/L-entry insertion path. |
| `CZPOP-0200`–`CZPOP-0203` | `Install Application CZL` binds `Install Applications Mgt. CZL` during first-time per-company installation, performs the data operations, and unbinds it. |
| `CZPOP-0245` | `Sales Shipment CZL` binds `Item Tracking Doc. Handler CZL` around `RetrieveDocumentItemTracking` when lot or serial tracking is shown. |

All other manual subscribers already retained binding-context evidence. The
population session therefore ended with no unresolved targeted question.

## 5. Preservation and Workflow Boundaries

- accepted B01 JSON Lines are byte-identical to the fixed input;
- all 448 records retain `prior_known: Unknown`;
- all 448 records retain `selection_status: Unselected`;
- all 448 records retain `trigger_status: Not Evaluated`;
- all 448 records retain `checklist_status: Not Evaluated`;
- stratum indicators are unchanged; and
- no parallel results file was introduced.

## 6. Validation

The completed change set passes:

- the complete repository unit-test discovery suite;
- JSON Schema validation of all 448 worksheet records;
- population order and count reconciliation;
- exact B01 preservation assertions;
- manual-runtime resolution assertions;
- baseline and strict repository metadata validation;
- `git diff --check`; and
- Git patch application checking against the fixed index baseline.

The authoritative patch and command outputs are retained in the delivery
evidence package generated with this change set.

## 7. Threats and Limitations

- The population session is AI-assisted and is not equivalent to owner acceptance
  of records `CZPOP-0017` through `CZPOP-0448`.
- Evidence readiness does not establish runtime reachability, behavioral impact,
  quality, materiality, or defect prevalence.
- `No Linked Evidence` and `No CZL Peer Recorded` remain bounded dataset values,
  not proof of absence.
- The conclusions apply to the fixed BCApps revision and retained source
  boundary.

## 8. Next Operation

A separate owner-review checkpoint may inspect the population-wide AI decisions.
Prior-knowledge labeling and every downstream analytical operation remain
separate and require explicit authorization.
