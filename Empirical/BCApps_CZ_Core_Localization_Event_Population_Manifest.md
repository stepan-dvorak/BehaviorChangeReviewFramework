---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-EVENT-POP-001
  title: BCApps Czech Core Localization Event Population Manifest
  type: Empirical Study
  version: 0.4.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Records the reproducible syntactic extraction of the fixed event-subscriber
  population used by the BCApps Czech Core Localization event pilot and the
  correction of an invalid application-wide marker inventory.

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
  - Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md

study:
  method: Deterministic Static Source Inventory Extraction
  subject: Microsoft Core Localization Pack for Czech application
  data_access: Public GitHub Repository at Fixed Commit
  reproducibility: Full for the Recorded Subscriber Population

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
  `393f8306c753f229dd67c3059777a1bbfee1fa776001b29c68e11061d042465c`;

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
- Publisher raise sites are not resolved in this discovery step. Publisher
  contracts, binding lifetime, mutable effects, transactions, error behavior,
  and preserved responsibilities require later source analysis.
- One application at one commit cannot represent BCApps or Business Central
  extension practice generally.

## 8. Interpretation and Next Step

The reproduced inventory establishes a stable candidate frame, but it is not
sufficient by itself to begin the pre-registered coarse screen. It provides no
evidence that any row satisfies the Behavioral Change Impact Review trigger.

The dependency-aware source search boundary and one-record-per-subscriber
context protocol are now fixed [P4]. The next step is to implement and
technically validate the resolver, then create one context record for each of
the 448 retained population rows. Coarse screening, prior-knowledge labeling,
case IDs, and the full checklist remain untouched until context resolution is
complete and its limitations are recorded.

## 9. Method Correction

Version 0.2.0 added application-wide publisher and lexical-marker inventories.
That procedure was invalid for the intended pilot because it mixed CZL event
publishers and ordinary implementation markers with the CZL event subscribers
that form the candidate population. For example, a mutable `IsHandled`
parameter on a CZL-published integration event described a publisher contract,
not a CZL subscriber's modification of an established dependency flow.

The invalid extractor and its three generated datasets have been removed. Their
raw counts are retained only in revision history and the research log as a
withdrawn methodological observation; they must not be used for screening or
case selection. The 448-row subscriber population and 782-row source-file
inventory remain valid because both are bounded directly to the intended CZL
subscriber population and its source boundary.

## 10. References

- **[P1]** Microsoft. Core Localization Pack for Czech production source,
  BCApps commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/tree/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/Src>.
- **[P2]** Microsoft. `app.json`, Core Localization Pack for Czech, BCApps
  commit `397d01199c321e774edaf23a7290fee40f75c6a6`.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/app.json>.
- **[P3]** Microsoft. "The Microsoft_Application.app file." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-application-app-file>.
- **[P4]** Orden. "BCApps Czech Subscriber Context Resolution Protocol."
  `Empirical/BCApps_CZ_Subscriber_Context_Resolution_Protocol.md`.

## 11. Revision History

### 0.4.0 — 2026-07-19

- Linked the fixed dependency boundary and subscriber-context record protocol.
- Deferred resolver implementation, technical validation, population-wide
  context resolution, coarse screening, and case selection.

### 0.3.0 — 2026-07-19

- Withdrew the application-wide publisher and marker discovery procedure
  because it did not preserve the CZL subscriber as the unit of analysis.
- Removed its extractor and generated datasets while retaining the valid
  subscriber population and complete CZL source-file inventory.
- Required dependency-aware, per-subscriber publisher and runtime-context
  resolution before coarse screening or case selection.

### 0.2.0 — 2026-07-18

- Retained publisher, binding, transaction, obsolescence, mutable-control, and
  multi-subscriber-target marker inventories.
- Recorded raw counts, checksums, repeatability checks, and nonsemantic status
  labels for the completed mechanical discovery layer.
- Deferred raise-site resolution, runtime interpretation, coarse screening,
  case selection, trigger classification, and impact analysis.
- **Withdrawn on 2026-07-19:** these outputs mixed publisher and implementation
  markers with the intended subscriber population and are not valid screening
  inputs.

### 0.1.0 — 2026-07-18

- Recorded the fixed source, extractor, commands, versions, checksums, and
  verified syntactic population counts.
- Preserved all reviewer-dependent and analytical statuses as unperformed.
- Documented lexical and scope limitations and deferred discovery work.
