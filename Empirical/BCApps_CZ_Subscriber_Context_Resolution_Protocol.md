---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ES-BCAPPS-CZ-CLP-CONTEXT-PROTOCOL-001
  title: BCApps Czech Subscriber Context Resolution Protocol
  type: Empirical Study Protocol
  version: 0.3.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Freezes the source dependency boundary, record contract, resolution statuses,
  and validation rules for joining publisher and runtime context to each
  retained CZL event subscriber before coarse screening or case selection.

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
  - 02_Research_Methodology.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Population_Manifest.md
  - References/Microsoft_Event_Types.md

related_documents:
  - Empirical/BCApps_Event_Pattern_Analysis.md
  - Empirical/BCApps_CZ_Subscriber_Context_Technical_Validation.md
  - Empirical/BCApps_CZ_Subscriber_Context_Manifest.md
  - 00_Research_Log.md

study:
  method: Dependency-Aware Static Source Context Resolution Protocol
  subject: Retained CZL event-subscriber population at fixed BCApps commit
  data_access: Public GitHub Repository with Packaged Application Limitation
  reproducibility: Full Static Context Dataset Reproduced and Retained

tags:
  - empirical-study
  - BCApps
  - Czech-localization
  - event-subscribers
  - dependency-boundary
  - context-resolution
  - study-protocol
---

# BCApps Czech Subscriber Context Resolution Protocol

## 1. Status and Purpose

This protocol freezes the inputs and outputs for the next stage of the Czech
localization pilot. The resolver and automated technical validation are now
implemented, owner review is accepted, and full 448-record context generation
is complete. This document contains no coarse-screen result, prior-knowledge label, case
selection, trigger classification, impact assessment, defect claim, or
framework conclusion.

The unit invariant is:

> Every context record belongs to exactly one retained `CZPOP-NNNN` event
> subscriber declared in the Core Localization Pack for Czech application.

Publisher declarations, raise sites, binding calls, control parameters, and
other subscribers are context attached to that unit. They are not independent
candidate cases.

## 2. Research Question

> Can the source context required for later coarse screening be resolved
> reproducibly for each retained CZL event subscriber without interpreting a
> publisher or lexical marker as subscriber behavior?

The protocol also records where static source is insufficient. An unresolved
record is a valid result and must not be converted into evidence of no effect.

## 3. Fixed Inputs

- BCApps repository: `microsoft/BCApps`;
- commit: `397d01199c321e774edaf23a7290fee40f75c6a6`;
- subject application: Core Localization Pack for Czech;
- retained population:
  `Empirical/Data/BCApps_CZ_Core_Localization_Event_Population.csv`;
- population size: 448 subscriber attributes; and
- context-record schema:
  `Schemas/BCApps_CZ_Subscriber_Context.schema.json`.

The resolver must reject a BCApps checkout at any other commit and must reject
an input record whose `inventory_id`, source commit, subscriber path, procedure,
or event target differs from the retained population.

## 4. Source Claims and Repository Observations

### 4.1 Source claims

Microsoft documents that the `application` property references the Application
app. That app logically encapsulates the applications making up a solution and
allows their dependencies to resolve implicitly [D1]. Microsoft also separates
published application events from database and page trigger events supplied by
the runtime [D2].

These claims explain why target resolution cannot be limited to explicit
entries in the CZL `dependencies` array and why some subscriber targets will
not have an AL publisher declaration or explicit raise site.

### 4.2 Fixed-source observations

The five retained physical application manifests at the fixed commit establish
the initial source-resolution boundary [D3]–[D7]:

| Boundary ID | Application | Relationship used by this protocol |
|---|---|---|
| `CZDEP-0001` | Core Localization Pack for Czech | Subject containing the subscriber population |
| `CZDEP-0002` | EU 3-Party Trade Purchase | Explicit CZL dependency |
| `CZDEP-0003` | Base Application | Application resolution layer with propagated dependencies |
| `CZDEP-0004` | Business Foundation | Fixed Base Application dependency |
| `CZDEP-0005` | System Application | Fixed Base Application and Business Foundation dependency |

The generated boundary CSV retains IDs, versions, paths, relationships, and
evidence bases. The generator verifies that:

- all five physical manifests identify Microsoft version `29.0.0.0`;
- CZL explicitly depends on EU 3-Party Trade Purchase and declares
  `application` version `29.0.0.0`;
- Base Application declares `propagateDependencies: true` and depends on
  Business Foundation and System Application; and
- Business Foundation depends on System Application.

### 4.3 Interpretation and access limitation

The five applications form a documented and reproducible **source search
boundary** for this pilot. They are not claimed to be a complete reconstruction
of the packaged Microsoft Application dependency graph. The distributed
`Microsoft_Application.app` package used by the product is not present as a
physical application manifest in the examined BCApps source tree.

If a subscriber target cannot be resolved inside the retained boundary, the
resolver must return `Source Not in Boundary` and record the missing source. It
must not silently expand the boundary. Adding another physical application
requires a protocol revision with direct fixed-commit evidence before its
source is searched.

## 5. Retained Boundary Artifacts

| Artifact | Role |
|---|---|
| `Scripts/Discover_BCApps_CZ_Dependency_Boundary.py` | Validates the commit, manifests, versions, and fixed relationships and generates the boundary CSV |
| `Empirical/Data/BCApps_CZ_Core_Localization_Dependency_Boundary.csv` | Five-row ordered physical source boundary |
| `Schemas/BCApps_CZ_Subscriber_Context.schema.json` | Machine-readable contract for one future subscriber-context record |
| `Scripts/Resolve_BCApps_CZ_Subscriber_Context.py` | Implements bounded dry-run and technical-validation resolution |
| `Scripts/Test_BCApps_CZ_Subscriber_Context_Resolver.py` | Exercises explicit failure statuses and deterministic validation selection |
| `Empirical/Data/BCApps_CZ_Subscriber_Context_Technical_Validation.jsonl` | Three retained records selected by the protocol rule |
| `Empirical/Data/BCApps_CZ_Subscriber_Context.jsonl` | Complete one-record-per-subscriber static context dataset |
| `Empirical/BCApps_CZ_Subscriber_Context_Manifest.md` | Generation, integrity, summary, and limitation record |

Reproduction command:

```text
python Scripts\Discover_BCApps_CZ_Dependency_Boundary.py --bcapps-root C:\Research\BCApps --output Empirical\Data\BCApps_CZ_Core_Localization_Dependency_Boundary.csv
```

Generation checksums:

- boundary generator:
  `e3217709c8c232b733ace2d8d2ae9757969e03e1140dde6cd6b62ef7dcd67333`;
- dependency-boundary CSV:
  `b45db9af153dc327d418119a0b9f8fb89b0cdc75876a88bf12742c91d1a615f7`;
- subscriber-context schema:
  `bac8eb28ad3ef4f07ec3cf04dd63ec0682457ed0069a20b791007c2da9be8a25`.

## 6. Subscriber-Context Record Contract

The JSON Schema is the field authority. A future tabular representation may
flatten array fields using a documented lossless convention, but it must not
change field meaning or allowed statuses.

The record groups fields into six responsibilities:

| Group | Required evidence responsibility |
|---|---|
| Subscriber identity | Preserve the `CZPOP` foreign key, fixed commit, path, codeunit, procedure, and body boundary |
| Target identity | Preserve object type, object, event, element, and event class from the retained subscriber |
| Publisher context | Record resolution status, owning boundary application, declaration, raise sites, or platform semantics |
| Runtime context | Record subscriber instance and binding paths applicable to this subscriber |
| Mechanical subscriber context | Record direct calls, exact control reads and writes, transaction markers, and error markers inside the subscriber body |
| Supporting context | Record composition subscriber IDs, callers, tests, unresolved reason, and any auditable manual correction |

The schema fixes `prior_known` to `Unknown`, `coarse_screen_status` to `Not
Screened`, and `selection_status` to `Unselected`. A context resolver must not
change those values.

## 7. Resolution Procedure

### 7.1 Input identity

1. Read one row from the retained subscriber population.
2. Verify its fixed commit, exact source path, source line, codeunit, procedure,
   target object, event, and element against source.
3. Establish the subscriber body boundary without interpreting its purpose.
4. On mismatch, return `Parse Failure`; do not repair the population silently.

### 7.2 Target event class

Classify only the source mechanism needed for lookup:

- `Integration Event`;
- `Business Event`;
- `Internal Event`;
- `Database Trigger Event`;
- `Page Trigger Event`;
- `Platform Event`; or
- `Unknown`.

This classification is not an extensibility-quality or behavioral-change
classification.

### 7.3 Publisher resolution

1. Resolve the target object identity rather than matching only event text.
2. Search the retained boundary using its recorded order as a deterministic
   traversal order, not as authority precedence.
3. Require compatible object type, object identity, event name, and element
   where applicable.
4. For a source-published event, retain the publisher declaration and every
   discovered raise site in the owning application.
5. For a database, page, or other runtime event, record `Resolved Platform or
   Trigger Event` and cite the applicable platform semantics instead of
   inventing an AL publisher path.
6. If multiple compatible targets remain, return `Ambiguous Target` and retain
   every candidate location.
7. If the declaration resolves but no raise site is found, return `Raise Site
   Unresolved` rather than assuming the event is unused.
8. A CZL-published event is recorded as `Publisher in Subject Application`; it
   remains context for the CZL subscriber and is not a new candidate case.

### 7.4 Subscriber-local mechanical context

Inspect only the retained subscriber body for:

- direct call symbols;
- exact reads and writes of mutable control parameters;
- `Commit`, commit-behavior, and try-function context;
- error, exit, or other failure-control markers; and
- conditional-compilation or obsolete context.

Presence of a marker does not establish change type, materiality, impact, risk,
or defect. The resolver must retain source locations for every reported marker.

### 7.5 Runtime and composition context

- Determine the containing codeunit's `EventSubscriberInstance` value.
- Search bind and unbind calls only for that subscriber codeunit or instance.
- Record other retained `CZPOP` subscribers with the same resolved target.
- Search other boundary applications for composition only after the target is
  resolved; those subscribers are context, not additions to the CZL population.
- Record directly relevant caller and test paths when they are mechanically
  linked. Do not infer test coverage from path proximity or naming alone.

### 7.6 Record completion

Set one context status:

- `Resolved`: required identity and publisher or platform context are resolved;
- `Partially Resolved`: some context is retained but an explicitly required
  source element remains missing or ambiguous;
- `Unresolved`: the target cannot be resolved within the fixed boundary; or
- `Not Attempted`: no resolution work has been performed.

Every non-resolved record requires `unresolved_reason`. Manual corrections must
identify the original value, corrected value, source evidence, and reviewer.

## 8. Technical Validation Before Full Execution

The resolver must be tested before it writes the 448-row context dataset. The
technical validation set is not a pilot sample and receives no `CZP` IDs.

After an initial dry run, choose the first row in lexical `inventory_id` order
for every target class actually present, plus the first row producing each
non-success resolution status. This deterministic rule prevents selecting
convenient examples. Preserve all attempted validation rows, including failures.

Validation must demonstrate:

- stable byte-identical output across two runs;
- referential integrity against all 448 retained `CZPOP` IDs;
- no additional candidate-population rows;
- exact-case path resolution;
- schema validity for every context record;
- source locations for every extracted body marker;
- correct separation of source-published and platform-trigger events;
- explicit ambiguity and missing-source behavior; and
- unchanged `Unknown`, `Not Screened`, and `Unselected` workflow values.

At least one human review must compare each technical validation record with
the fixed source before full execution. Validation success establishes parser
fitness for this bounded task, not semantic correctness of later analysis.

The repository owner completed this review for all three retained records,
accepted them without correction, and authorized population-wide generation.

## 9. Acceptance Criteria for Resolver Execution

Full execution may begin only when:

- the generator validates the five-row source boundary;
- the context schema passes JSON Schema validation;
- the technical validation set passes the checks in Section 8;
- parse failures and manual corrections are retained rather than suppressed;
- rerunning the resolver cannot overwrite prior-knowledge, screening, or
  selection fields; and
- the generated dataset contains exactly one record for every retained
  `CZPOP` ID, including unresolved records.

Coarse screening remains a separate later operation. Resolution status is not
a screening result and must not be used as an automatic selection bucket.

All full-execution criteria were satisfied for the retained dataset. It contains
448 schema-valid records in exact population order and preserves every protected
workflow value.

## 10. Threats to Validity

- The Application package is not directly inspectable in the retained source,
  so the source boundary may omit a packaged dependency.
- AL object names, aliases, namespaces, and moved modules can make lexical
  target resolution ambiguous.
- Runtime trigger events do not have ordinary source publisher declarations.
- An event declaration may have multiple raise sites or no discoverable raise
  site in the retained boundary.
- Static binding evidence may not establish runtime lifetime, configuration,
  license, permission, or reachability.
- Direct-call extraction does not establish transitive behavior.
- Available tests are contextual evidence and cannot prove complete behavior.
- A mechanically resolved context may still be insufficient for coarse
  evidence-availability screening.

## 11. Candidate Implications and Deferred Work

No candidate framework implication is introduced. This protocol is study
infrastructure created to prevent publisher or marker evidence from replacing
the subscriber-centered unit of analysis.

Resolver implementation, technical validation, owner review, and generation of
one context record for each retained subscriber are complete. Deferred work is
now limited to defining the separate coarse-screen operation before executing
it.

Prior-knowledge labeling, case selection, trigger classification, checklist
analysis, and synthesis remain explicitly deferred.

## 12. References

- **[D1]** Microsoft. "The Microsoft_Application.app file." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-application-app-file>.
- **[D2]** Microsoft. "Event types." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-event-types>.
- **[D3]** Microsoft. Core Localization Pack for Czech `app.json`, fixed
  BCApps commit.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/CZ/CoreLocalizationPack/app/app.json>.
- **[D4]** Microsoft. EU 3-Party Trade Purchase `app.json`, fixed BCApps commit.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Apps/W1/EU3PartyTradePurchase/app/app.json>.
- **[D5]** Microsoft. Base Application `app.json`, fixed BCApps commit.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Layers/W1/BaseApp/app.json>.
- **[D6]** Microsoft. Business Foundation `app.json`, fixed BCApps commit.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/Business%20Foundation/App/app.json>.
- **[D7]** Microsoft. System Application `app.json`, fixed BCApps commit.
  <https://github.com/microsoft/BCApps/blob/397d01199c321e774edaf23a7290fee40f75c6a6/src/System%20Application/App/app.json>.

## 13. Revision History

### 0.3.0 — 2026-07-19

- Recorded owner acceptance of all technical-validation records and explicit
  authorization for full generation.
- Linked the reproducible, schema-valid 448-record context dataset and manifest.
- Preserved coarse screening, prior-knowledge labeling, case selection, and
  impact analysis as unperformed operations.

### 0.2.0 — 2026-07-19

- Linked the bounded resolver, focused regression tests, and deterministic
  three-record technical-validation output.
- Recorded successful automated validation while retaining owner source review
  as a mandatory gate before full execution.
- Preserved full context generation, coarse screening, and case selection as
  unperformed operations.

### 0.1.0 — 2026-07-19

- Fixed the five-application physical source-resolution boundary.
- Defined the one-record-per-subscriber contract and controlled statuses.
- Defined deterministic resolution, validation, acceptance, and failure rules.
- Kept coarse screening and every analytical classification out of scope.
