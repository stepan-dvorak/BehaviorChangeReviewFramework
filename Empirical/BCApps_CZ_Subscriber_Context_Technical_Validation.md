---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-CONTEXT-VALIDATION-001
  title: BCApps Czech Subscriber Context Resolver Technical Validation
  type: Empirical Study Validation Record
  version: 0.1.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records implementation-level evidence for the bounded CZL subscriber-context
  resolver while preserving owner source review, full context generation,
  coarse screening, and case selection as separate pending steps.

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
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md

related_documents:
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - 00_Research_Log.md

study:
  method: Deterministic Static Resolver Technical Validation
  subject: Fixed CZL subscriber population and five-application source boundary
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Automated Checks Passed; Owner Source Review Pending

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - context-resolution
  - technical-validation
---

# BCApps Czech Subscriber Context Resolver Technical Validation

## 1. Status and Scope

The bounded static resolver is implemented and its automated technical checks
pass. The protocol-required owner review of each retained validation record is
pending. Full 448-record context generation is therefore not yet authorized by
the protocol's acceptance criteria.

This validation performs no coarse screening, prior-knowledge labeling, case
selection, trigger classification, impact analysis, defect assessment, or
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
- retains publisher application identity, declaration, raise sites, peer
  `CZPOP` subscribers, procedure boundaries, direct calls, mutable-parameter
  reads and writes, transaction markers, error markers, and bounded manual
  binding locations;
- emits explicit ambiguous, missing-source, parse-failure, and unresolved
  raise-site statuses rather than silently repairing or expanding the boundary;
  and
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

An AI-assisted comparison confirmed that their subscriber identities, body
boundaries, publisher or platform classification, mechanical body markers, and
unchanged workflow fields correspond to the fixed source. This comparison does
not satisfy the protocol's separate owner-review requirement.

## 5. Failure-Path Tests

The fixed population did not naturally produce an ambiguous or missing-source
status. Focused synthetic regression fixtures therefore verify that:

- no compatible publisher produces `Source Not in Boundary` and `Unresolved`;
- two compatible declarations produce `Ambiguous Target` and `Partially
  Resolved`;
- failure records retain an explanation;
- mutable-parameter writes retain their source line; and
- validation selection remains deterministic and does not alter screening
  state.

Synthetic fixtures validate control behavior only. They are not empirical
BCApps cases and are not included in the population or validation dataset.

## 6. Reproduction

```text
python Scripts\Test_BCApps_CZ_Subscriber_Context_Resolver.py
python Scripts\Resolve_BCApps_CZ_Subscriber_Context.py --bcapps-root C:\Research\BCApps --population Empirical\Data\BCApps_CZ_Core_Localization_Event_Population.csv --boundary Empirical\Data\BCApps_CZ_Core_Localization_Dependency_Boundary.csv --output Empirical\Data\BCApps_CZ_Subscriber_Context_Technical_Validation.jsonl --mode validation
```

Checksums:

- resolver:
  `d76ac1bf620b068ea5c40efddc9e0267c275889877b8230a251c8f3f9ecfdeee`;
- regression tests:
  `897c5adb949d3fe706b0b002e40d6b0e5fce7092ff12e4b18f135db68777db1d`;
- retained validation JSON Lines:
  `4ee46fd6010f808f89b256bc6af49a423353f92d0c3cb4c2e24b42bb65bb7dbc`.

Two independent resolver runs produced byte-identical retained validation
output. All three records validate against
`Schemas/BCApps_CZ_Subscriber_Context.schema.json`.

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

Automated implementation validation is complete. The protocol's full-execution
gate remains closed until the repository owner compares all three retained
records with the fixed source and records acceptance or corrections.

After that review, the next operation is generation and retention of exactly
one context record for each of the 448 `CZPOP` rows. Coarse screening and case
selection remain later, separate operations.

## 9. Revision History

### 0.1.0 — 2026-07-19

- Recorded the first bounded resolver implementation and dry-run diagnostics.
- Retained the deterministic three-record technical-validation dataset.
- Verified failure paths with synthetic regression fixtures.
- Kept the owner-review gate and every analytical operation open.
