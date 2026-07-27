---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-CONTEXT-VALIDATION-001
  title: BCApps Czech Subscriber Context Resolver Technical Validation
  type: Empirical Study Validation Record
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records implementation-level evidence for the bounded CZL subscriber-context
  resolver, including enclosing-activity repair and deterministic regeneration,
  while preserving screening decisions and later analysis as separate steps.

quality:
  review: Reviewed
  evidence: Partial
  editorial: Reviewed

audience:
  - Researchers
  - Business Central Architects
  - Business Central Developers
  - Contributors
  - AI Assistants

depends_on:
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md

related_documents:
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/BCApps_CZ_Subscriber_Context_Manifest.md
  - 00_Research_Log.md

study:
  method: Deterministic Static Resolver Technical Validation
  subject: Fixed CZL subscriber population and five-application source boundary
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Automated Checks Passed; Owner Source Review Accepted

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - context-resolution
  - technical-validation
---

# BCApps Czech Subscriber Context Resolver Technical Validation

## 1. Status and Scope

The bounded static resolver and its focused regression checks pass. The original
technical validation and owner review established the retained subscriber unit,
publisher or platform classification, and protected workflow state.

After `CZCS-B01`, the resolver was repaired to distinguish the source event
declaration from the executable procedure or trigger enclosing each raise site.
The three-record technical-validation dataset and complete 448-record context
dataset were regenerated twice from the unchanged fixed BCApps commit. The
outputs were byte-identical, schema-valid, and consistent with the accepted B01
source boundaries.

This validation performs no coarse-screening decision, prior-knowledge label,
case selection, trigger classification, impact analysis, defect assessment, or
framework synthesis.

## 2. Implemented Resolution Boundary

`Scripts/Resolve_BCApps_CZ_Subscriber_Context.py`:

- rejects a BCApps checkout or retained input at another source commit;
- requires the 448 unique retained `CZPOP` IDs and five fixed `CZDEP` IDs;
- indexes event publishers by object type, object name or numeric ID, and event
  name;
- resolves namespace-qualified targets and events published by table or page
  extensions against their base objects;
- distinguishes source-published events from recognized database and page
  trigger events;
- indexes executable AL procedures and triggers across the retained boundary;
- maps every source raise site to one unique enclosing executable activity and
  retains its kind, name, declaration, body bounds, and raise line;
- returns `Raise Site Unresolved` when the enclosing activity cannot be mapped
  uniquely;
- retains publisher application identity, declaration, peer `CZPOP`
  subscribers, subscriber body boundaries, direct calls, mutable-parameter
  reads and writes, transaction markers, error markers, and bounded manual
  binding locations;
- emits explicit ambiguous, missing-source, parse-failure, and unresolved
  statuses rather than silently repairing or expanding the boundary; and
- fixes workflow values to `Unknown`, `Not Screened`, and `Unselected`.

Caller and test paths remain empty unless the current implementation can link
them mechanically. Empty arrays do not claim that callers or tests are absent.

## 3. Dry-Run Observation

An initial dry run processed all 448 retained rows only to establish event
classes, resolution statuses, and the deterministic validation set. Its full
context output was not retained as a study dataset.

| Mechanical resolution status | Rows |
|---|---:|
| `Resolved Source Publisher` | 339 |
| `Publisher in Subject Application` | 4 |
| `Resolved Platform or Trigger Event` | 105 |
| Other status | 0 |
| **Total** | **448** |

**Repository observation:** the current resolver returned a successful static
publisher or platform classification for every retained row.

**Interpretation limitation:** this is parser behavior at one fixed source
commit. It does not establish runtime reachability, semantic completeness,
evidence sufficiency, behavior change, impact, quality, or absence of defects.

## 4. Deterministic Validation Records

The fixed protocol selects the first `inventory_id` for every event class
actually returned by the dry run and the first row for each non-success status.
The dry run returned three classes and no non-success status:

| Inventory ID | Event class | Resolution mechanism |
|---|---|---|
| `CZPOP-0001` | Integration Event | Base Application source publisher and raise site |
| `CZPOP-0009` | Database Trigger Event | Microsoft-documented platform trigger semantics |
| `CZPOP-0386` | Page Trigger Event | Microsoft-documented platform trigger semantics |

The retained JSON Lines file contains only these three technical-validation
records. They have no `CZP` IDs and are not selected pilot cases.

The repository owner confirmed that subscriber identity, body boundary,
publisher or platform classification, publisher declaration or applicable
absence, raise sites or applicable absence, mechanical markers, composition
subscribers, and protected workflow fields were correct for all three records.
No correction or additional note was recorded.

## 5. Failure-Path Tests

The fixed population did not naturally produce an ambiguous or missing-source
status. Focused synthetic regression fixtures therefore verify that:

- no compatible publisher produces `Source Not in Boundary` and `Unresolved`;
- two compatible declarations produce `Ambiguous Target` and `Partially
  Resolved`;
- failure records retain an explanation;
- mutable-parameter writes retain their source line;
- validation selection remains deterministic and does not alter screening
  state;
- balanced `begin`, `case`, and `end` blocks stop an executable body before
  comments or declarations belonging to the next object member; and
- procedure, trigger, and unresolved raise-site mappings retain or reject
  structured enclosing-activity context as required.

Synthetic fixtures validate control behavior only. They are not empirical
BCApps cases and are not included in the population or validation dataset.

## 6. Reproduction

```text
python Scripts\Test_BCApps_CZ_Subscriber_Context_Resolver.py
python Scripts\Resolve_BCApps_CZ_Subscriber_Context.py --bcapps-root C:\Research\BCApps --population Empirical\Data\BCApps_CZ_Core_Localization_Event_Population.csv --boundary Empirical\Data\BCApps_CZ_Core_Localization_Dependency_Boundary.csv --output Empirical\Data\BCApps_CZ_Subscriber_Context_Technical_Validation.jsonl --mode validation
```

Current checksums:

- resolver:
  `dcd2748df3536b2d741a06fcdd971c008427685bc314d38578991ee291839630`;
- regression tests:
  `13a695dfd8ca11091483d8caf74d799db5bb558480b458be10ed70035926195e`;
- subscriber-context schema:
  `92f643dfe3e0695a91de7c79e51144b5d5e13bf2a4c3f1796f494649d43570e9`;
- retained technical-validation JSON Lines:
  `898dd35f6c20069e398c6965cfaf6b571e8e7b650966abef44c405e0d94e8539`;
  and
- retained complete context JSON Lines:
  `3267f7ffb1e3adbfff789169d328d44ab4a116eaa1d322121bd897086e6edfc9`.

Two independent resolver runs produced byte-identical validation output. The
complete full-mode runs were also byte-identical. All retained records validate
against `Schemas/BCApps_CZ_Subscriber_Context.schema.json`.

## 7. Threats and Known Limitations

- The resolver is purpose-built for the frozen AL source and is not a complete
  AL compiler or semantic model.
- Object aliases, future syntax, indirect invocations, and dependency content
  outside the fixed source boundary can defeat static matching.
- Qualified calls with the same procedure name can overapproximate raise-site
  candidates when type identity cannot be proven lexically.
- Manual binding locations are bounded lexical evidence, not proof of runtime
  instance lifetime or reachability.
- Direct calls and mutable-parameter access are syntactic observations, not
  behavioral effects.
- Caller and test context are not yet comprehensively resolved.
- The validation set covers the three event classes returned by this fixed
  population; it does not exercise business or internal events as retained CZL
  subscriber targets.
- Human interpretation may identify parser errors not detected by automated
  checks or AI-assisted comparison.

## 8. Acceptance Status and Next Step

The repaired resolver produced 448 schema-valid, resolved context records in
exact retained population order. Every source-published record has a structured
enclosing-activity context corresponding to its retained raise-site paths.
Platform-trigger records retain no invented AL publisher activity.

The B01 golden-oracle comparison confirmed the eight owner-corrected enclosing
activity ranges. Preservation regenerated the unscreened worksheet records from
the repaired context while changing each accepted B01 record only in
`context_dataset_sha256`. All prior-knowledge, selection, trigger, and checklist
fields remain protected.

This technical result accepts the regenerated context dataset as the current
mechanical screening input. It does not re-open the accepted B01 checkpoint or
perform screening for `CZPOP-0017` onward. The next permitted screening action
is `CZCS-B02`.

## 9. Revision History

### 0.4.0 — 2026-07-27

- Recorded the post-merge enclosing-activity resolver repair.
- Regenerated the technical-validation and complete context datasets twice with
  byte-identical results.
- Recorded the current resolver, test, schema, validation, and full-dataset
  checksums.
- Accepted the regenerated context as the preservation input without changing
  B01 screening decisions or downstream protected fields.


### 0.3.0 — 2026-07-21

- Recorded the conditionally accepted coarse-screen preparation review and its
  upstream boundary defect.
- Added a balanced-block regression fixture.
- Recorded the complete 10-record regeneration impact.
- Kept population-wide coarse screening unauthorized pending focused re-review.

### 0.2.0 — 2026-07-19

- Recorded owner acceptance of all three validation records without correction.
- Recorded explicit authorization for population-wide context generation.
- Linked the completed 448-record context dataset manifest.

### 0.1.0 — 2026-07-19

- Recorded the first bounded resolver implementation and dry-run diagnostics.
- Retained the deterministic three-record technical-validation dataset.
- Verified failure paths with synthetic regression fixtures.
- Kept the owner-review gate and every analytical operation open.
