---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-CONTEXT-MANIFEST-001
  title: BCApps Czech Subscriber Context Dataset Manifest
  type: Empirical Study Manifest
  version: 0.2.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records the reproducible generation, integrity checks, mechanical summary,
  and limitations of the complete 448-record CZL subscriber-context dataset
  before coarse screening or case selection.

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

The protocol-required owner review accepted `CZPOP-0001`, `CZPOP-0009`, and
`CZPOP-0386` without corrections and explicitly authorized full generation.
The resolver subsequently generated one retained context record for every one
of the 448 fixed population rows.

This dataset is preparatory static-source evidence. It contains no coarse
screen, prior-knowledge label, selected case, Behavioral Change Impact Review
trigger result, checklist analysis, defect claim, or prevalence conclusion.

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

Retained checksums:

- resolver:
  `234a0cf28aa7559f9515afe79f85893b9f787451935e9cc5d91f51b659633e23`;
- full context dataset:
  `2cbeb7a45b46f937f5749e73caad6167c5604ffa100ca4f084ca77ac5a2df4eb`.

Two independent executions produced byte-identical output.

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
| `prior_known = Unknown` | 448 |
| `coarse_screen_status = Not Screened` | 448 |
| `selection_status = Unselected` | 448 |
| Invalid composition references | 0 |

Successful `context_resolution_status` means that the required subscriber
identity and publisher or platform context resolved under the protocol. It does
not mean that every possible caller, test, binding, or runtime path is known.

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
publisher or platform context for all retained subscribers and preserved the
population unit and all protected workflow fields.

**Interpretation:** The dataset is fit to serve as the mechanical input to a
separately defined coarse evidence-availability screen. Its successful
generation does not validate the later screen, the candidate review trigger,
or the Behavioral Change Impact Checklist.

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

Population-wide context generation is complete. The separate coarse
evidence-availability protocol and record contract are now fixed, but screening
has not begun. The future screen must consume these records without treating
resolution status, event class, mechanical markers, or composition count as
automatic trigger or case-selection decisions.

Prior-knowledge labeling, case selection, trigger classification, checklist
analysis, and synthesis remain unperformed.

## 9. Revision History

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
