---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-EVENT-POP-001
  title: BCApps Czech Core Localization Event Population Manifest
  type: Empirical Study
  version: 0.2.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records the reproducible syntactic extraction of the fixed event-subscriber
  population, publisher declarations, and discovery markers used by the
  BCApps Czech Core Localization event pilot.

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
  reproducibility: Full for the Recorded Syntactic Discovery Outputs

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
| `Scripts/Discover_BCApps_CZ_Event_Markers.py` | Generates publisher, marker, and multi-subscriber-target inventories |
| `Empirical/Data/BCApps_CZ_Core_Localization_Event_Publishers.csv` | One row per detected event publisher declaration |
| `Empirical/Data/BCApps_CZ_Core_Localization_Discovery_Markers.csv` | One row per detected binding, transaction, obsolescence, or mutable-control marker |
| `Empirical/Data/BCApps_CZ_Core_Localization_Multi_Subscriber_Targets.csv` | Subscriber targets with syntactic multiplicity in the bounded application |

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
python Scripts\Discover_BCApps_CZ_Event_Markers.py --bcapps-root C:\Research\BCApps --population Empirical\Data\BCApps_CZ_Core_Localization_Event_Population.csv --publishers-output Empirical\Data\BCApps_CZ_Core_Localization_Event_Publishers.csv --markers-output Empirical\Data\BCApps_CZ_Core_Localization_Discovery_Markers.csv --targets-output Empirical\Data\BCApps_CZ_Core_Localization_Multi_Subscriber_Targets.csv
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
| Integration event publisher declarations | 289 |
| Business event publisher declarations | 0 |
| Internal event publisher declarations | 0 |
| Publisher declarations with a recorded isolated argument | 0 |
| Manual subscriber-instance declarations | 8 |
| Bind and unbind calls | 9 and 7 |
| Mutable `IsHandled`, `Handled`, and `Skip` parameters | 146, 2, and 0 |
| `Commit` calls and `TryFunction` attributes | 19 and 16 |
| `CommitBehavior` and `Obsolete` attributes | 0 and 20 |
| Targets with two or more bounded subscribers | 21 |

These counts reproduce the pilot's preliminary subscriber inventory. They are
repository observations produced from the fixed source, not claims made by
Microsoft and not semantic case counts.

SHA-256 checksums at generation time:

- discovery script:
  `677fec48335aadf78732b90d8add24c1eb4acd9977b074b2da9cf391cf8146c0`;
- generated CSV:
  `c18156d853fcfb5808e55e5756efea398c9c0beef911b743865248dbbd8a32da`;
- ordered source-file CSV:
  `393f8306c753f229dd67c3059777a1bbfee1fa776001b29c68e11061d042465c`;
- marker discovery script:
  `80a6e4de85a8fa2d93f5b23fb7de81b41d9ef1c38c321d0b6ea3a46f15e698ae`;
- publisher CSV:
  `4713bc2b834559fbc473334219485dbc5898d16d6d9e9c759ac2b600c4bb78b4`;
- discovery-marker CSV:
  `aafcd40d20823971771021ec4c1a9fb66ace9ac73945d12386f5743f16b1bac3`;
- multi-subscriber-target CSV:
  `3805183dd5be6fa6296c13d6fe40d48aee73f6efddba6ad83c4934d7280c5a1e`.

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

Publisher and marker rows preserve lexical source context. Every marker has
`interpretation_status` set to `Not Evaluated`. Multi-subscriber targets record
only bounded syntactic multiplicity and have `composition_status` set to
`Syntactic Multiplicity Only`.

## 6. Verification Checks

The retained result was checked for:

- exact BCApps HEAD equality with the pre-registered commit;
- exact existence of the fixed production-source path;
- deterministic lexical source traversal and row ordering;
- six syntactic arguments for every detected subscriber attribute;
- a following procedure declaration for every detected attribute;
- sequential unique inventory IDs from `CZPOP-0001` through `CZPOP-0448`;
- 448 data rows and 116 distinct subscriber source paths; and
- 782 sequential unique source-file rows;
- 289 publisher rows, 227 marker rows, and 21 multi-subscriber-target rows; and
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
- The presence of manual binding, a mutable control parameter, `Commit`,
  `TryFunction`, obsolescence, or multiple bounded subscribers does not prove
  reachability, interaction, control effect, risk, or defect.
- Publisher raise sites are not resolved in this discovery step. Publisher
  contracts, binding lifetime, mutable effects, transactions, error behavior,
  and preserved responsibilities require later source analysis.
- Multi-subscriber counts include only subscriber attributes in the bounded
  application and do not represent complete runtime composition.
- One application at one commit cannot represent BCApps or Business Central
  extension practice generally.

## 8. Interpretation and Next Step

The reproduced inventory establishes a stable candidate frame from which the
pre-registered coarse screen can proceed. It provides no evidence that any row
satisfies the Behavioral Change Impact Review trigger.

The next step is the pre-registered coarse evidence-availability and stratum
screen. Reviewer prior-knowledge labels must be supplied before bucket
assignment. Case IDs and the full checklist remain untouched until the
selection register is frozen.

## 9. References

- **[P1]** Microsoft. Core Localization Pack for Czech production source,
  BCApps commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/Src>.

## 10. Revision History

### 0.2.0 — 2026-07-18

- Retained publisher, binding, transaction, obsolescence, mutable-control, and
  multi-subscriber-target marker inventories.
- Recorded raw counts, checksums, repeatability checks, and nonsemantic status
  labels for the completed mechanical discovery layer.
- Deferred raise-site resolution, runtime interpretation, coarse screening,
  case selection, trigger classification, and impact analysis.

### 0.1.0 — 2026-07-18

- Recorded the fixed source, extractor, commands, versions, checksums, and
  verified syntactic population counts.
- Preserved all reviewer-dependent and analytical statuses as unperformed.
- Documented lexical and scope limitations and deferred discovery work.
