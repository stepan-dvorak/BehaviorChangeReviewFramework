---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-EVENT-POP-001
  title: BCApps Czech Core Localization Event Population Manifest
  type: Empirical Study
  version: 0.1.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records the reproducible syntactic extraction of the fixed event-subscriber
  population used by the BCApps Czech Core Localization event pilot.

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
  - 02_Research_Methodology.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md

related_documents:
  - Empirical/BCApps_Event_Pattern_Analysis.md
  - References/Microsoft_Event_Types.md

study:
  method: Deterministic Static Source Inventory Extraction
  subject: Microsoft Core Localization Pack for Czech application
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Full for the Recorded Syntactic Population

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - event-subscribers
  - population-inventory
  - reproducibility
---

# BCApps Czech Core Localization Event Population Manifest

## 1. Purpose and Boundary

This manifest records the first execution step of the pre-registered Czech
localization event pilot: reproduction of its event-subscriber population. The
retained CSV is a syntactic inventory, not a set of behavioral change cases.
It does not select `CZP-001` through `CZP-016`, apply the candidate trigger,
evaluate checklist impacts, identify defects, or support prevalence claims.

The fixed source is Microsoft's public `microsoft/BCApps` repository at commit
`397d01199c321e774edaf23a7290fee40f75c6a6`. The production boundary is
`src/Apps/CZ/CoreLocalizationPack/app/Src` [P1].

## 2. Retained Artifacts

| Artifact | Purpose |
|---|---|
| `Scripts/Discover_BCApps_CZ_Event_Population.py` | Validates the checkout commit, scans the fixed boundary, and deterministically generates the CSV |
| `Empirical/Data/BCApps_CZ_Core_Localization_Event_Population.csv` | One ordered row per detected, uncommented `[EventSubscriber(...)]` attribute |
| `Empirical/Data/BCApps_CZ_Core_Localization_Source_Files.csv` | Complete ordered list of AL files in the fixed production boundary |

The script uses only the Python standard library. It fails if the BCApps
checkout is not at the fixed commit or if the source boundary is absent.

## 3. Reproduction Procedure

Commands were executed from the root of this repository:

```text
git clone --filter=blob:none --no-checkout https://github.com/microsoft/BCApps.git C:\Research\BCApps
git -C C:\Research\BCApps sparse-checkout init --cone
git -C C:\Research\BCApps sparse-checkout set src/Apps/CZ/CoreLocalizationPack/app
git -C C:\Research\BCApps checkout 397d01199c321e774edaf23a7290fee40f75c6a6
python Scripts\Discover_BCApps_CZ_Event_Population.py --bcapps-root C:\Research\BCApps --output Empirical\Data\BCApps_CZ_Core_Localization_Event_Population.csv --files-output Empirical\Data\BCApps_CZ_Core_Localization_Source_Files.csv
```

Recorded execution environment:

- Python: `3.12.13`;
- Git: `2.51.1`;
- operating system: Linux-based isolated workspace; and
- extraction date: `2026-07-18`.

The operating system is not encoded into the output. Paths are stored as
repository-relative POSIX paths, and rows are sorted by path, source line, and
subscriber procedure before stable IDs are assigned.

## 4. Verified Inventory Results

The extractor reported:

| Observation | Count |
|---|---:|
| AL files in the fixed production boundary | 782 |
| Detected event-subscriber attributes | 448 |
| Source files containing a detected subscriber | 116 |
| CSV data rows | 448 |

These counts reproduce the pilot's preliminary subscriber inventory. They are
repository observations produced from the fixed source, not claims made by
Microsoft and not semantic case counts.

SHA-256 checksums at generation time:

- discovery script:
  `677fec48335aadf78732b90d8add24c1eb4acd9977b074b2da9cf391cf8146c0`;
- generated CSV:
  `c18156d853fcfb5808e55e5756efea398c9c0beef911b743865248dbbd8a32da`;
- ordered source-file CSV:
  `393f8306c753f229dd67c3059777a1bbfee1fa776001b29c68e11061d042465c`.

## 5. Dataset Fields and Status Values

Each row retains source identity, line, containing codeunit, subscriber
instance, procedure, publisher arguments, procedure signature, parameter
names, selected mechanical parameter-name markers, and conditional-compilation
context. Source values are normalized only for whitespace and AL quoting.

The three workflow fields deliberately preserve the boundary between discovery
and analysis:

- `prior_known` is `Unknown` in every row because it requires reviewer input;
- `coarse_screen_status` is `Not Screened`; and
- `selection_status` is `Unselected`.

The `has_ishandled_parameter`, `has_handled_parameter`, and
`has_skip_parameter` fields report exact case-insensitive parameter-name
matches. They do not determine subscriber effect or trigger classification.

## 6. Verification Checks

The retained result was checked for:

- exact BCApps HEAD equality with the pre-registered commit;
- exact existence of the fixed production-source path;
- deterministic lexical source traversal and row ordering;
- six syntactic arguments for every detected subscriber attribute;
- a following procedure declaration for every detected attribute;
- sequential unique inventory IDs from `CZPOP-0001` through `CZPOP-0448`;
- 448 data rows and 116 distinct subscriber source paths; and
- 782 sequential unique source-file rows; and
- byte-identical CSV outputs on a second execution in the recorded workspace.

## 7. Limitations and Threats to Validity

- The extractor is a purpose-built lexical scanner, not the AL compiler or a
  complete AL parser.
- It removes comments and balances quoted and nested expressions, but it does
  not evaluate preprocessor conditions. Conditional context is recorded as
  text rather than classified as active or inactive.
- A subscriber attribute is an inventory unit, not necessarily an independent
  behavior, reachable runtime participant, or behavioral change case.
- Publisher objects and events are copied from attribute arguments; they are
  not resolved to declarations or raise sites in this step.
- Default and manual binding, publisher composition, mutable effects,
  transactions, error behavior, and preserved responsibilities require later
  source analysis.
- The CSV does not yet retain separate inventories for publisher declarations,
  binding calls, or other discovery markers required by the broader pilot
  protocol. Those are legitimate deferred discovery work.
- One application at one commit cannot represent BCApps or Business Central
  extension practice generally.

## 8. Interpretation and Next Step

The reproduced inventory establishes a stable candidate frame from which the
pre-registered coarse screen can proceed. It provides no evidence that any row
satisfies the Behavioral Change Impact Review trigger.

The next step is to complete the remaining discovery-marker inventories and
then perform the coarse evidence-availability and stratum screen. Reviewer
prior-knowledge labels must be supplied before bucket assignment. Case IDs and
the full checklist remain untouched until the selection register is frozen.

## 9. References

- **[P1]** Microsoft. Core Localization Pack for Czech production source,
  BCApps commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/Src>.

## 10. Revision History

### 0.1.0 — 2026-07-18

- Recorded the fixed source, extractor, commands, versions, checksums, and
  verified syntactic population counts.
- Preserved all reviewer-dependent and analytical statuses as unperformed.
- Documented lexical and scope limitations and deferred discovery work.
