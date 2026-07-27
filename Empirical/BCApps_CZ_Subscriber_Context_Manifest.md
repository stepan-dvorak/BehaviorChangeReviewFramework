---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-CONTEXT-MANIFEST-001
  title: BCApps Czech Subscriber Context Dataset Manifest
  type: Empirical Study Manifest
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records reproducible generation, integrity checks, mechanical summary,
  preservation, and limitations of the current 448-record CZL subscriber-context
  baseline supporting the active coarse-screen workflow.

quality:
  review: Self Reviewed
  evidence: Verified
  editorial: Reviewed

audience:
  - Researchers
  - Business Central Architects
  - Business Central Developers
  - Contributors
  - AI Assistants

depends_on:
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md
  - Empirical/BCApps_CZ_Subscriber_Context_Technical_Validation.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md

related_documents:
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/BCApps_CZ_Coarse_Evidence_Availability_Screening_Protocol.md
  - 00_Research_Log.md

study:
  method: Deterministic Static Subscriber-Context Resolution
  subject: Complete retained CZL event-subscriber population
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Complete for the Retained Static Context Dataset

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - event-subscribers
  - context-resolution
  - dataset-manifest
---

# BCApps Czech Subscriber Context Dataset Manifest

## 1. Status and Scope

The protocol-required owner review originally accepted `CZPOP-0001`,
`CZPOP-0009`, and `CZPOP-0386` and authorized full generation. The resolver
subsequently generated one retained context record for every fixed population
row.

A later tooling repair added structured executable activity context for source
raise sites. The complete dataset was regenerated twice from the unchanged
BCApps commit. Both outputs were byte-identical and all 448 records remain
resolved and schema-valid.

This dataset is preparatory static-source evidence. `CZCS-B01` has been screened
and accepted in the separate coarse-screen worksheet, but this context dataset
contains no prior-knowledge label, selected case, BCIR trigger result, checklist
analysis, defect claim, or prevalence conclusion.

## 2. Fixed Inputs and Output

- BCApps commit: `397d01199c321e774edaf23a7290fee40f75c6a6`;
- population: 448 rows in
  `Empirical/Data/BCApps_CZ_Core_Localization_Event_Population.csv`;
- source boundary: five rows in
  `Empirical/Data/BCApps_CZ_Core_Localization_Dependency_Boundary.csv`;
- schema: `Schemas/BCApps_CZ_Subscriber_Context.schema.json`; and
- output: `Empirical/Data/BCApps_CZ_Subscriber_Context.jsonl`.

The JSON Lines output is ordered by the retained population's `inventory_id`
order and contains one JSON object per line.

## 3. Reproduction

```text
python Scripts\Resolve_BCApps_CZ_Subscriber_Context.py --bcapps-root C:\Research\BCApps --population Empirical\Data\BCApps_CZ_Core_Localization_Event_Population.csv --boundary Empirical\Data\BCApps_CZ_Core_Localization_Dependency_Boundary.csv --output Empirical\Data\BCApps_CZ_Subscriber_Context.jsonl --mode full
```

Current retained checksums:

- resolver:
  `dcd2748df3536b2d741a06fcdd971c008427685bc314d38578991ee291839630`;
- resolver regression tests:
  `13a695dfd8ca11091483d8caf74d799db5bb558480b458be10ed70035926195e`;
- schema:
  `92f643dfe3e0695a91de7c79e51144b5d5e13bf2a4c3f1796f494649d43570e9`;
- technical-validation dataset:
  `898dd35f6c20069e398c6965cfaf6b571e8e7b650966abef44c405e0d94e8539`;
  and
- complete context dataset:
  `3267f7ffb1e3adbfff789169d328d44ab4a116eaa1d322121bd897086e6edfc9`.

Two independent validation executions and two independent complete executions
produced byte-identical output.

## 4. Integrity Results

| Check | Result |
|---|---|
| Output records | 448 |
| Unique `inventory_id` values | 448 |
| Population IDs missing from context | 0 |
| Context IDs absent from population | 0 |
| Population and context order | Exact match |
| JSON Schema-valid records | 448 |
| `context_resolution_status = Resolved` | 448 |
| Source-published records with complete enclosing-activity context | 343 |
| Platform-trigger records without invented AL activity | 105 |
| `prior_known = Unknown` | 448 |
| `coarse_screen_status = Not Screened` | 448 |
| `selection_status = Unselected` | 448 |
| Invalid composition references | 0 |

Successful `context_resolution_status` means that the required subscriber
identity and publisher or platform context resolved under the protocol. For a
source publisher, every retained raise-site path also maps to one structured
enclosing procedure or trigger. Resolution does not mean that every caller,
test, binding, runtime path, or semantic effect is known.

## 5. Mechanical Dataset Description

### 5.1 Event classes

| Event class | Records |
|---|---:|
| Integration Event | 343 |
| Database Trigger Event | 100 |
| Page Trigger Event | 5 |
| **Total** | **448** |

### 5.2 Publisher resolution

| Publisher resolution status | Records |
|---|---:|
| `Resolved Source Publisher` | 339 |
| `Publisher in Subject Application` | 4 |
| `Resolved Platform or Trigger Event` | 105 |
| **Total** | **448** |

Resolved source publishers occur in Base Application for 336 records and
System Application for 3 records. Four publishers occur in the CZL subject
application. The 105 platform-trigger records have no AL publisher application.

These counts describe resolver classifications. They do not measure behavioral
change, architectural significance, implementation quality, or defects.

### 5.3 Composition and manual binding context

- 43 records identify at least one other retained CZL subscriber with the same
  event target;
- 23 records belong to manual subscriber codeunits;
- 17 of those manual records contain at least one bounded lexical binding path;
  and
- 6 manual records contain no mechanically linked binding path.

The six records without a retained binding path are `CZPOP-0125`,
`CZPOP-0200`, `CZPOP-0201`, `CZPOP-0202`, `CZPOP-0203`, and `CZPOP-0245`.
An empty binding array means only that the resolver did not establish a bounded
lexical link. It is not evidence that runtime binding never occurs.

## 6. Repository Observation and Interpretation

**Repository observation:** The bounded resolver produced schema-valid static
publisher or platform context for all retained subscribers. For 343
source-published records, the dataset now distinguishes the event declaration
from the executable procedure or trigger containing each raise site.

**Interpretation:** The repaired dataset is fit to serve as the current
mechanical input to the separately governed coarse evidence-availability
screen. Structured enclosing-activity context can reduce repeated source
navigation, but it does not itself complete human screening or establish
behavioral significance.

**Preservation observation:** Refreshing the active worksheet changed each
accepted B01 record only in its context checksum. The 432 unscreened records were
regenerated mechanically; all downstream protected values remained unchanged.

**Unresolved question:** Caller and test context remain empty unless a direct
mechanical link was established by the current implementation. Later screening
must treat empty fields as unavailable static evidence, not as proof of absence.

## 7. Threats and Limitations

- The source boundary does not reproduce the complete distributed Application
  package or runtime environment.
- The resolver is a bounded static parser rather than the AL compiler.
- Qualified calls with the same name may overapproximate raise-site evidence
  when lexical analysis cannot prove receiver type.
- Binding paths do not prove runtime lifetime, configuration, license,
  permission, ordering, or reachability.
- Mechanical calls and parameter access do not establish behavioral effects.
- Composition IDs include only the retained CZL population, not every Microsoft,
  partner, customer, or dynamically bound subscriber.
- A resolved record may still lack enough evidence for coarse screening.

## 8. Next Research Step

Context regeneration, validation, and worksheet preservation are complete. The
accepted `CZCS-B01` checkpoint remains unchanged, and records
`CZPOP-0017` through `CZPOP-0448` remain `Not Screened`.

The next permitted screening action is `CZCS-B02` (`CZPOP-0017` through
`CZPOP-0032`) under the fixed evidence-availability and execution rules.
Prior-knowledge labeling, case selection, trigger classification, checklist
analysis, and synthesis remain unperformed.

## 9. Revision History

### 0.4.0 — 2026-07-27

- Regenerated all 448 records with structured enclosing executable activity
  context for source raise sites.
- Recorded byte-identical validation and complete-generation runs and current
  checksums.
- Accepted the regenerated dataset as the active coarse-screen context baseline.
- Preserved the accepted B01 checkpoint and all downstream protected fields.


### 0.3.0 — 2026-07-21

- Replaced next-member boundary inference with balanced AL block detection.
- Regenerated all 448 records and recorded 10 corrected body end lines.
- Preserved all resolution classifications and protected workflow fields.
- Kept population-wide coarse screening unauthorized pending focused review.

### 0.2.0 — 2026-07-19

- Linked the pre-registered coarse evidence-availability protocol and schema.
- Preserved this dataset as immutable screening input.
- Kept screening, prior-knowledge labeling, and case selection unperformed.

### 0.1.0 — 2026-07-19

- Recorded owner acceptance of the technical-validation records.
- Retained the byte-identical 448-record static context dataset.
- Recorded integrity checks, mechanical summaries, limitations, and six manual
  records without mechanically linked binding paths.
- Kept coarse screening and all later analytical operations out of scope.
