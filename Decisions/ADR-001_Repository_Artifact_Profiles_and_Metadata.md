---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ADR-001
  title: Repository Artifact Profiles and Metadata Contract
  type: Architecture Decision Record
  version: 1.0.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Stable

owner: Štěpán Dvořák

purpose: >
  Defines the repository artifact profiles, mandatory and optional metadata,
  special-file exceptions, maturity semantics, and machine-index maintenance
  rules used by the Orden repository.

quality:
  review: Approved
  evidence: N/A
  editorial: Approved

audience:
  - Repository Owner
  - Contributors
  - AI Assistants

depends_on:
  - Governance_Principles.md

related_documents:
  - Repository_Standards.md
  - Repository_Taxonomy.md
  - Reasoning_Standard.md
  - Contributing_for_AI.md
  - Editorial_Style_Guide.md
  - AGENTS.md
  - README.md
  - Repository_Index.yaml
  - Archive/Repository_Conformance_Report.md

tags:
  - governance
  - metadata
  - artifact-profile
  - architecture-decision
  - repository-normalization
---

# ADR-001: Repository Artifact Profiles and Metadata Contract

## Status

**Accepted**

Accepted by the repository owner, Štěpán Dvořák, on 2026-07-17.

This decision is normative. `Repository_Standards.md` implements its artifact
profiles, metadata contract, language, naming, architecture, and index
maintenance requirements.

---

## 1. Context

The Orden repository evolved concurrently with its governance model.

As a result, active artifacts currently use several generations of structure:

1. current grouped metadata used by newer governance documents;
2. legacy minimal front matter used by early core research documents;
3. completed research analyses without front matter;
4. intentional research stubs without explicit machine-readable maturity;
5. conventional repository entrypoints such as `README.md` and `AGENTS.md`;
6. machine-readable artifacts such as `Repository_Index.yaml`.

`Repository_Standards.md` establishes the general metadata model but does not
yet define:

- a minimal mandatory field set;
- conditional requirements by artifact type;
- explicit profiles for special artifacts;
- a complete distinction between lifecycle status, maturity and quality;
- rules for non-Markdown artifacts;
- whether conventional repository entrypoints require front matter;
- the maintenance model of `Repository_Index.yaml`.

Without these decisions, repository-wide normalization would require repeated
interpretation and could produce inconsistent results.

The repository also references `Repository_Architecture.md`, which does not
exist, and contains `Repository_Map.md`, whose responsibilities overlap with
`README.md`, `Repository_Taxonomy.md`, and `Repository_Index.yaml`.

---

## 2. Problem Statement

The repository requires a metadata and artifact model that:

- is deterministic enough for automated validation;
- remains simple enough for a small research repository;
- preserves the distinct purposes of governance, research and machine files;
- makes incomplete research clearly distinguishable from completed analysis;
- avoids metadata that duplicates information already maintained reliably by
  Git or the filesystem;
- supports AI retrieval without turning every repository entrypoint into a
  governed research document;
- prevents recurring reconsideration of already settled structural questions.

---

## 3. Decision Drivers

The decision is guided by the following priorities:

1. Minimal necessary complexity.
2. Deterministic conformance.
3. Evidence and uncertainty preservation.
4. Stable document identity.
5. Clear distinction between lifecycle, maturity and quality.
6. Compatibility with GitHub and AI tooling conventions.
7. Machine-readable retrieval.
8. Low maintenance burden.
9. Explicit exceptions instead of implicit inconsistency.
10. Evolution through deliberate versioned change.

---

## 4. Considered Options

### Option A — Require identical front matter for every repository file

All Markdown files would use the same complete metadata block. Non-Markdown
files would require companion metadata documents.

Advantages:

- superficially uniform;
- simple single-schema validation.

Disadvantages:

- adds irrelevant metadata to `README.md` and `AGENTS.md`;
- conflicts with the tool-defined role of special files;
- creates companion-file overhead for machine artifacts;
- encourages meaningless values such as `N/A`;
- increases maintenance without improving research quality.

### Option B — Keep metadata informal and document-specific

Every document would contain only the metadata its author considers useful.

Advantages:

- no migration cost;
- maximum local flexibility.

Disadvantages:

- conformance cannot be tested deterministically;
- retrieval requires special cases;
- document status remains ambiguous;
- inconsistencies are likely to recur.

### Option C — Define a small core contract with artifact profiles

All governed documents share a minimal core contract. Conditional metadata is
defined by artifact profile. Conventional entrypoints receive explicit
exceptions, and native machine artifacts expose equivalent top-level metadata.

Advantages:

- deterministic without requiring irrelevant fields;
- supports validation;
- reflects actual artifact responsibilities;
- preserves conventional tool behavior;
- scales to future research artifacts;
- minimizes unnecessary complexity.

Disadvantages:

- requires several related schemas or conditional validation rules;
- requires an initial repository migration;
- contributors must select the correct profile.

---

## 5. Decision

**Option C is adopted.**

The Orden repository SHALL use a small mandatory metadata contract combined
with explicit artifact profiles.

The following profiles are established:

1. `governed_document`
2. `reference_analysis`
3. `empirical_study`
4. `research_stub`
5. `repository_entrypoint`
6. `machine_index`
7. `archived_artifact`

Templates are governed documents whose `document.type` identifies their
template role. A separate template profile is not required at this time.

---

## 6. Core Metadata Contract

### 6.1 Applicability

The core metadata contract applies to all active Markdown documents except
files explicitly classified as `repository_entrypoint`.

The same semantic fields apply to native machine artifacts, but their physical
representation follows the `machine_index` profile.

### 6.2 Mandatory Core Metadata

Every governed Markdown document SHALL begin with YAML front matter containing
at least:

```yaml
---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: EXAMPLE-001
  title: Example Document
  type: Research Document
  version: 0.1.0
  status: Active

classification:
  domain: Research
  layer: Project
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  States the single primary purpose of the document.
---
```

Mandatory core fields are:

| Field | Requirement | Rationale |
|---|---|---|
| `metadata_schema` | Mandatory | Identifies the metadata contract used by the artifact. |
| `project.id` | Mandatory | Preserves repository context if the document is retrieved independently. |
| `project.name` | Mandatory | Provides a meaningful human-readable project identity while the stable code name remains unchanged. |
| `document.id` | Mandatory | Provides permanent identity independent of path or title. |
| `document.title` | Mandatory | Provides a stable human-readable and retrieval title. |
| `document.type` | Mandatory | Selects the artifact profile and expected structure. |
| `document.version` | Mandatory | Records semantic evolution of the document. |
| `document.status` | Mandatory | Records repository lifecycle state. |
| `classification.domain` | Mandatory | Identifies the knowledge or governance domain. |
| `classification.layer` | Mandatory | Identifies the scope at which the artifact applies. |
| `classification.maturity` | Mandatory | Identifies actual content maturity. |
| `owner` | Mandatory | Identifies responsibility for review and approval. |
| `purpose` | Mandatory | Enables correct retrieval and prevents responsibility drift. |

### 6.3 Metadata Intentionally Not Mandatory

The following fields SHALL NOT be mandatory:

- `document.filename`;
- `created`;
- `last_updated`.

Rationale:

- filename is derived from the filesystem and may become stale after a rename;
- Git provides authoritative creation and change history;
- manually maintained modification dates frequently diverge from repository
  history.

These fields MAY be used when export outside Git requires them, but validators
SHALL NOT require them.

### 6.4 Optional Core Metadata

The following fields MAY be included when they add retrieval or governance
value:

```yaml
audience:
  - Researchers
  - AI Assistants

depends_on:
  - Repository_Standards.md

related_documents:
  - 02_Research_Methodology.md

supersedes:
  - Archive/Example_v0.9.md

aliases:
  - Alternative Retrieval Name

tags:
  - architecture
  - evidence
```

Rules:

- `depends_on` SHALL be used only for a true interpretive or normative
  dependency;
- `related_documents` SHALL be used for non-required contextual relationships;
- `supersedes` SHALL be used when an active artifact replaces a prior artifact;
- `aliases` SHALL not introduce unauthorized terminology synonyms;
- `tags` SHALL improve retrieval rather than repeat every word in the title.

### 6.5 Canonical Relationship-Key Spelling

Metadata keys SHALL use `snake_case`.

The canonical dependency key is:

```yaml
depends_on:
```

The legacy key `depends-on` SHALL be migrated and SHALL NOT be used in new
documents.

---

## 7. Repository Language

### 7.1 Authoring Language

All repository-authored normative, research, navigational and machine-readable
content SHALL be written in professional US English.

US English is selected because:

- the project name uses `Behavior` rather than `Behaviour`;
- Microsoft documentation predominantly uses US English;
- one defined variant prevents inconsistent spelling and terminology;
- the public repository should remain understandable without private project
  context.

Repository-authored content SHALL use consistent forms such as:

- `behavior`, not `behaviour`;
- `analyze`, not `analyse`;
- `catalog`, not `catalogue`;
- `organization`, not `organisation`.

Document metadata, headings, descriptions, findings, comments and
machine-readable retrieval text are subject to this rule.

### 7.2 Original-Language Evidence

Non-English text MAY appear only when preservation of the original form is
necessary as evidence, including:

- source-code identifiers;
- localized captions, labels and error messages;
- text extracted from an analyzed source artifact;
- direct quotations whose original wording is relevant;
- historical evidence for which translation would reduce accuracy.

Original-language evidence SHALL:

- be clearly identified as evidence;
- remain distinguishable from repository-authored interpretation;
- include sufficient English explanation;
- include an English translation when necessary for understanding;
- preserve the original wording when exact comparison or traceability matters.

Non-English evidence does not make the containing document multilingual. The
document's analysis, conclusions and navigation SHALL remain in US English.

### 7.3 Language Metadata

Document-level `language` metadata SHALL NOT be used for ordinary repository
documents because US English is the repository-wide default.

If a future artifact consists primarily of preserved source evidence in another
language, its treatment SHALL require an explicit profile extension or a new
architecture decision. Such an exception SHALL NOT be inferred from incidental
non-English evidence.

---

## 8. Lifecycle, Maturity and Quality

### 8.1 Lifecycle Status

`document.status` describes whether the artifact is part of the active
repository baseline.

Allowed values are:

| Value | Meaning |
|---|---|
| `Proposed` | Submitted for owner decision and not yet normative or canonical. |
| `Active` | Current artifact used by the repository. |
| `Deprecated` | Still available but scheduled for replacement or removal. |
| `Archived` | Historical artifact excluded from ordinary retrieval. |

### 8.2 Maturity

`classification.maturity` describes content completeness and stabilization.

Allowed values are:

| Value | Meaning |
|---|---|
| `Stub` | Future work is scoped, but substantive research or content is unavailable. |
| `Draft` | Substantive content exists but is incomplete or has not completed review. |
| `Review` | Content is complete for its stated scope and awaits or is undergoing approval. |
| `Stable` | Content has been approved as the current baseline. |

Lifecycle and maturity are independent.

For example:

```yaml
document:
  status: Active

classification:
  maturity: Draft
```

means that the document is current and applicable but not yet stable.

### 8.3 Quality

The `quality` group is mandatory for:

- normative governance documents;
- core research documents;
- reference analyses;
- empirical studies;
- whitepapers and framework syntheses.

It is optional for simple templates unless the template itself contains
normative guidance.

```yaml
quality:
  review: Reviewed
  evidence: Partial
  editorial: Reviewed
```

Allowed review values:

- `Not Reviewed`
- `Self Reviewed`
- `Reviewed`
- `Approved`
- `N/A`

Allowed evidence values:

- `Pending`
- `Partial`
- `Verified`
- `N/A`

Allowed editorial values:

- `Draft`
- `Reviewed`
- `Approved`
- `N/A`

A high editorial quality SHALL NOT imply verified evidence or approved
conclusions.

---

## 9. Artifact Profiles

### 9.1 Governed Document

The `governed_document` profile applies to:

- governance principles and standards;
- repository taxonomy;
- editorial guidance;
- core research documents;
- terminology documents;
- framework and whitepaper documents;
- architecture decision records;
- templates containing governed structure.

Requirements:

- complete core metadata;
- `quality` when the artifact is normative or contains research conclusions;
- `audience` for normative documents;
- explicit dependencies when applicable;
- canonical terminology;
- repository-standard versioning.

### 9.2 Reference Analysis

The `reference_analysis` profile applies to substantive analysis of standards,
official documentation, literature, source code, or community publications.

In addition to the core contract and `quality`, it SHALL include:

```yaml
evidence:
  source_authority: Primary Standard
  source_access: Partial
  verification: Partial
```

Allowed `source_authority` values are:

- `Primary Standard`
- `Peer-Reviewed Publication`
- `SEI Publication`
- `Official Vendor Documentation`
- `Official Source Code`
- `Official Product Behavior`
- `Community Publication`
- `Mixed Sources`

Allowed `source_access` values are:

- `Full`
- `Partial`
- `Public Summary`
- `Secondary Only`
- `Mixed`

Allowed `verification` values are:

- `Verified`
- `Partial`
- `Pending`

Known limitations SHOULD be recorded explicitly:

```yaml
evidence:
  source_authority: Primary Standard
  source_access: Partial
  verification: Partial
  limitations:
    - Full normative text was not available for every assessed provision.
```

The profile SHALL preserve separation among:

- source position;
- repository observation;
- research interpretation;
- framework implication;
- uncertainty and threats to validity.

### 9.3 Empirical Study

The `empirical_study` profile applies to evidence collected from Business
Central applications, repositories, product behavior, or experiments.

In addition to the core contract and `quality`, it SHALL include:

```yaml
study:
  method: Repository Code Audit
  subject: Anonymized Business Central Application
  data_access: Private Source Snapshot
  reproducibility: Restricted
```

Required `study` fields are:

- `method`;
- `subject`;
- `data_access`;
- `reproducibility`.

The document body SHALL identify threats to validity and SHALL not generalize a
single case as universal evidence.

### 9.4 Research Stub

The `research_stub` profile applies to intentionally created placeholders for
future investigation.

It SHALL use:

```yaml
document:
  type: Research Stub
  status: Active

classification:
  maturity: Stub

quality:
  review: Not Reviewed
  evidence: Pending
  editorial: Draft

research_status:
  state: Planned
  conclusions_available: false
```

The following are mandatory for this profile:

- the core metadata contract;
- `classification.maturity: Stub`;
- the complete `quality` group;
- `research_status.state`;
- `research_status.conclusions_available: false`.

A research stub SHALL NOT:

- be represented as a completed analysis;
- use `quality.evidence: Verified`;
- contain invented summaries to appear complete;
- establish canonical terminology or conclusions.

Research stubs are valid active artifacts and SHALL remain retrievable for
planning and future-work queries.

### 9.5 Repository Entrypoint

The `repository_entrypoint` profile applies only to conventional files whose
format or behavior is defined by repository or agent tooling.

The following files are initially assigned this profile:

- `README.md`;
- `AGENTS.md`;
- `AGENTS.override.md`, if introduced later.

These files are exempt from YAML front matter.

Their identity, role, authority and retrieval behavior SHALL be recorded in
`Repository_Index.yaml`.

#### README requirements

`README.md` SHALL remain concise and human-oriented. It SHOULD provide:

- project purpose;
- research status;
- scope summary;
- recommended reading order;
- links to governance and research entrypoints;
- contribution or contact direction when applicable.

It SHALL NOT duplicate repository standards or the full repository inventory.

#### AGENTS requirements

`AGENTS.md` SHALL contain only operational instructions required by AI agents.

It SHALL:

- remain concise;
- identify required pre-reading;
- state non-negotiable repository rules;
- reference authoritative governance instead of duplicating it;
- avoid research exposition and document metadata overhead.

### 9.6 Machine Index

The `machine_index` profile applies to `Repository_Index.yaml` and any future
machine-readable artifact whose native serialization is not Markdown.

It SHALL expose metadata as native top-level YAML rather than Markdown front
matter.

Required structure:

```yaml
schema_version: "1.0.0"

project:
  id: Orden
  name: Behavior Change Review Framework

artifact:
  id: ORDEN-REPOSITORY-INDEX-001
  title: Orden Repository Retrieval Index
  type: Machine Index
  version: 1.0.0
  status: Active
  owner: Štěpán Dvořák
  maintenance: Generated

generation:
  generated_on: 2026-07-17
```

Required fields are:

- `schema_version`;
- `project.id`;
- `project.name`;
- `artifact.id`;
- `artifact.title`;
- `artifact.type`;
- `artifact.version`;
- `artifact.status`;
- `artifact.owner`;
- `artifact.maintenance`;
- `generation.generated_on`.

Machine artifacts SHALL NOT require companion Markdown metadata documents.

### 9.7 Archived Artifact

Artifacts under `Archive/` are assigned the `archived_artifact` profile.

Archived artifacts:

- are excluded from ordinary retrieval;
- SHALL NOT override active governance or canonical research;
- MAY retain their historical metadata unchanged;
- SHALL NOT be normalized solely for current conformance;
- MAY be used for provenance, evolution analysis, recovery and historical
  comparison.

Current replacements SHALL be recorded in `Repository_Index.yaml` when one
exists.

---

## 10. Repository Architecture Decision

A separate `Repository_Architecture.md` SHALL NOT be created at the current
repository scale.

Instead:

- `Repository_Standards.md` SHALL contain a concise `Repository Architecture`
  section defining artifact responsibilities and directory roles;
- `Repository_Taxonomy.md` SHALL define canonical classification and placement;
- `Repository_Index.yaml` SHALL record actual artifacts, authority and retrieval
  routes.

All active references to the nonexistent `Repository_Architecture.md` SHALL be
removed or redirected to the appropriate active document.

This decision MAY be revisited only if one or more of the following occurs:

- multiple independently governed research modules are introduced;
- directory responsibilities can no longer be expressed concisely;
- ownership boundaries require architectural documentation;
- generated and source artifacts develop non-trivial dependency flows;
- a separate architecture view demonstrably reduces maintenance or retrieval
  ambiguity.

---

## 11. Repository Map Decision

`Repository_Map.md` SHALL be archived after its useful reading-order content has
been incorporated into `README.md` or another appropriate active entrypoint.

Rationale:

- `README.md` provides human orientation;
- `Repository_Taxonomy.md` defines categories and placement;
- `Repository_Index.yaml` provides the authoritative machine inventory and
  retrieval routes;
- a separately maintained map duplicates these responsibilities and has already
  become incomplete.

No generated replacement is required at the current repository scale.

If a human-readable map becomes necessary later, it SHOULD be generated from
`Repository_Index.yaml` rather than maintained independently.

---

## 12. Repository Index Maintenance

### 12.1 Authority

`Repository_Index.yaml` is navigational and retrieval-oriented.

It SHALL NOT override:

- governance standards;
- canonical terminology documents;
- research evidence;
- human owner decisions.

### 12.2 Update Triggers

The index SHALL be regenerated or reviewed when:

- an active artifact is added, renamed, moved, deprecated or archived;
- an artifact changes authority, type or maturity;
- a research stub becomes a substantive analysis;
- a canonical definition source changes;
- a planned document is created;
- a query route changes;
- governance precedence changes;
- an archived family gains a new active replacement.

### 12.3 Source Commit

`source_commit` SHALL be removed from the index.

Rationale:

- Git already provides the authoritative version history;
- an index cannot reliably contain the SHA of the commit that is simultaneously
  updating the index;
- the field becomes stale immediately after the regeneration commit.

If future tooling requires an input boundary, it MAY use the explicitly named
field `indexed_through_commit`, whose meaning SHALL be the last commit inspected
before generation, not the commit containing the generated index.

### 12.4 Regeneration Method

Initially, regeneration MAY be manual but SHALL include validation of:

- exact path existence and case;
- unique document IDs;
- current authority and maturity;
- dependency resolution;
- archive replacement paths;
- research-stub warnings;
- planned-versus-existing status;
- query routes.

Automated generation SHOULD be introduced only when manual maintenance becomes
error-prone or materially expensive.

---

## 13. Filename and Path Rules

Repository references SHALL resolve on case-sensitive filesystems.

### 13.1 Conventional Tool-Defined Filenames

Conventional filenames whose capitalization has repository-host or agent-tool
meaning SHALL retain their conventional uppercase form.

The current conventional filenames are:

```text
README.md
AGENTS.md
```

`AGENTS.override.md` SHALL retain this exact form if introduced later.

These names are exceptions to the repository-authored document filename
convention. Their capitalization is functional rather than editorial.

### 13.2 Repository-Authored Document Filenames

Repository-authored Markdown filenames SHALL:

- use descriptive words separated by underscores;
- capitalize principal words;
- keep minor connecting words such as `for`, `and`, `of`, and `to` lowercase;
- preserve established uppercase abbreviations such as `AI`, `ISO`, `SEI`, and
  `ADR`;
- use the `.md` extension;
- avoid spaces;
- avoid full-uppercase naming unless required by an external convention.

Examples:

```text
Repository_Standards.md
Governance_Principles.md
Reasoning_Standard.md
Editorial_Style_Guide.md
Contributing_for_AI.md
Repository_Conformance_Report.md
```

### 13.3 Canonical Governance Filenames

The historical filenames SHALL be migrated as follows:

```text
CONTRIBUTING_FOR_AI.md
→ Contributing_for_AI.md

EDITORIAL_STYLE_GUIDE.md
→ Editorial_Style_Guide.md
```

The rename SHALL be performed atomically with updates to all active references,
dependencies, reading orders, and index paths.

The uppercase historical names SHALL not remain as duplicate active files.

### 13.4 Path Integrity

Paths in metadata SHALL:

- be relative to the repository root;
- use `/` as the separator;
- use exact filename case;
- identify the active canonical artifact unless historical context is explicit;
- avoid unqualified filenames when the artifact resides in a subdirectory.

---

## 14. Metadata Schema and Validation

A machine-readable schema SHOULD be created after this ADR is approved and
incorporated into `Repository_Standards.md`.

Recommended path:

```text
Schemas/Repository_Document_Metadata.schema.json
```

The initial validator SHOULD check:

- YAML parsing;
- mandatory core fields;
- profile-specific conditional fields;
- allowed controlled values;
- semantic version format;
- unique document IDs;
- exact dependency paths;
- forbidden legacy key `depends-on`;
- `maturity: Stub` consistency with `conclusions_available: false`;
- absence of governed front matter requirements for approved entrypoints;
- machine-index native metadata.

Validation SHOULD initially run locally.

Continuous integration SHALL be introduced only if repeated manual omissions
demonstrate a need. This avoids adding operational complexity before the schema
has stabilized.

---

## 15. Migration Rules

### 15.1 Structural-Only Migration

The first normalization pass SHALL be structural only.

It MAY change:

- metadata;
- relationship-key spelling;
- resolvable paths;
- heading consistency;
- explicit artifact classification;
- explicit maturity labels.

It SHALL NOT silently change:

- research claims;
- findings;
- definitions;
- hypothesis status;
- conclusion status;
- confidence assessments;
- source interpretations;
- threats to validity;
- recorded uncertainty;
- rejected directions.

### 15.2 Version Changes

Metadata-only normalization SHALL increment the minor version while the
document remains below version `1.0.0`.

Examples:

- `0.1.0` becomes `0.2.0`;
- legacy `0.1` becomes `0.2.0`.

For stable documents at or above `1.0.0`, metadata corrections that do not
change normative meaning SHOULD increment the patch version.

Substantive changes SHALL follow semantic versioning based on compatibility and
scope.

### 15.3 Migration Order

Repository normalization SHALL proceed in this order:

1. approve this ADR;
2. update `Repository_Standards.md`;
3. normalize normative governance documents;
4. normalize core research documents;
5. normalize substantive reference analyses;
6. classify research stubs;
7. update entrypoints;
8. archive `Repository_Map.md`;
9. regenerate `Repository_Index.yaml`;
10. run repository conformance validation;
11. resume substantive research.

### 15.4 Recommended Commit Boundaries

Normalization SHOULD be divided into reviewable commits:

1. governance contract and path decisions;
2. governance metadata normalization;
3. core research metadata normalization;
4. standards and SEI analysis metadata;
5. Microsoft analysis metadata;
6. research-stub classification;
7. entrypoint and navigation updates;
8. index regeneration and validation.

Each pull request SHALL state whether it is:

- structural only;
- substantive research revision;
- deliberately mixed with explicit owner approval.

---

## 16. Initial Artifact Classification

### 16.1 Repository Entrypoints

- `README.md`
- `AGENTS.md`

### 16.2 Governed Governance Documents

- `Governance_Principles.md`
- `Repository_Standards.md`
- `Repository_Taxonomy.md`
- `Editorial_Style_Guide.md`
- `Evidence_Hierarchy.md`
- `Reasoning_Standard.md`
- `Contributing_for_AI.md`
- `Terminology_Index.md`
- architecture decision records

### 16.3 Governed Core Research Documents

- `00_Project_Charter.md`
- `00_Research_Log.md`
- `01_Terminology.md`
- `02_Research_Methodology.md`
- `03_Related_Work.md`
- framework and whitepaper documents

### 16.4 Reference Analyses

- `References/ISO_42010.md`
- `References/ISO_42020.md`
- `References/ISO_42030.md`
- `References/SEI_Documenting_Behavior.md`
- `References/Microsoft_Extensibility_Overview.md`
- `References/Microsoft_IsHandled_v2.0.md`

### 16.5 Research Stubs

- `References/ATAM.md`
- `References/SAAM.md`
- `References/DDD.md`
- `References/Fowler.md`
- `References/Workflow_BPM.md`
- `References/Plugin_Architectures.md`
- `References/Microsoft_Event_Types.md`
- `References/Microsoft_Interfaces.md`

### 16.6 Machine Index

- `Repository_Index.yaml`

### 16.7 Artifact to Archive

- `Repository_Map.md`

---

## 17. Consequences

### 17.1 Positive Consequences

- Metadata becomes deterministic and testable.
- Research stubs remain useful without appearing complete.
- Lifecycle, maturity and quality no longer conflict semantically.
- Special repository files retain their conventional form.
- Machine artifacts no longer require artificial Markdown wrappers.
- Git remains the authority for file history and modification dates.
- Duplicate navigation responsibilities are reduced.
- Missing `Repository_Architecture.md` no longer blocks conformance.
- AI retrieval gains explicit status and authority signals.
- Structural normalization can proceed without altering research conclusions.
- Previously settled governance questions gain a recorded decision and reopening
  criteria.

### 17.2 Negative Consequences

- Existing active documents require migration.
- Several controlled vocabularies must be maintained.
- Profile selection introduces limited initial learning cost.
- A validator will eventually require implementation and maintenance.
- Archiving `Repository_Map.md` changes the current human navigation path.
- Metadata remains duplicated across documents to the extent needed for
  independent retrieval.

### 17.3 Risks

#### Risk: Metadata becomes bureaucratic

Mitigation:

- keep the mandatory core small;
- make derived dates and filenames optional;
- use conditional profiles;
- exempt conventional entrypoints.

#### Risk: Structural migration changes research meaning

Mitigation:

- use structural-only commits;
- preserve substantive text;
- review diffs by artifact class;
- record substantive conflicts separately.

#### Risk: Controlled values become too restrictive

Mitigation:

- add values only through a reviewed standards change;
- use `Mixed Sources` and explicit limitations where a single category is
  insufficient;
- revisit the profile only when a real artifact cannot be represented.

#### Risk: Index becomes stale

Mitigation:

- define update triggers;
- validate paths after structural changes;
- regenerate at the end of every normalization phase;
- automate only when justified by observed maintenance cost.

---

## 18. Alternatives Rejected

The following alternatives are rejected:

- requiring identical metadata for every repository file;
- requiring manually maintained `last_updated` dates;
- requiring `document.filename` despite filesystem authority;
- creating companion Markdown metadata for YAML artifacts;
- creating `Repository_Architecture.md` before the repository complexity
  justifies it;
- maintaining `Repository_Map.md` independently of the index;
- classifying documents by file size;
- filling research stubs with unverified content;
- normalizing archived documents to current standards;
- introducing CI before the metadata schema stabilizes.

---

## 19. Reopening Criteria

This decision SHALL NOT be reopened solely because a contributor prefers a
different metadata style.

Reconsideration is justified only when one or more of the following is
demonstrated:

- a new artifact type cannot be represented by an existing profile;
- the mandatory metadata creates measurable maintenance burden without
  retrieval or governance value;
- an AI or repository tool requires a conflicting conventional format;
- repository restructuring invalidates the current layer or domain model;
- automated validation exposes an ambiguity in the contract;
- multiple governed research modules require a dedicated repository
  architecture document;
- an existing controlled vocabulary cannot accurately represent a real state.

Any revision SHALL:

- identify the triggering evidence;
- preserve compatibility where practical;
- update `metadata_schema` when the contract changes incompatibly;
- include a migration plan;
- update `Repository_Standards.md` and `Repository_Index.yaml` together.

---

## 20. Implementation Plan

After approval:

1. Change this ADR to `document.status: Active`.
2. Incorporate the decision into `Repository_Standards.md`.
3. Add a concise repository architecture section to
   `Repository_Standards.md`.
4. Remove references to `Repository_Architecture.md`.
5. Rename `CONTRIBUTING_FOR_AI.md` to `Contributing_for_AI.md` and
   `EDITORIAL_STYLE_GUIDE.md` to `Editorial_Style_Guide.md`, updating all active
   references atomically.
6. Normalize governance document metadata.
7. Normalize core research metadata.
8. Normalize completed reference analyses.
9. Mark all intentional research stubs explicitly.
10. Update `README.md` with the human reading order.
11. Archive `Repository_Map.md`.
12. Migrate `Repository_Index.yaml` to the machine-index profile.
13. Remove `source_commit` from the index.
14. Validate paths, IDs, maturity and relationships.
15. Create the metadata schema after the first normalized set confirms the
    contract is practical.

---

## 21. Decision Outcome

If approved, this ADR establishes the repository baseline for artifact
classification and metadata normalization.

It does not validate research conclusions, promote candidate terminology, or
change the substantive content of existing studies.

Its purpose is to make subsequent normalization consistent, finite and
reviewable so that substantive research can continue without repeatedly
reopening foundational repository-structure questions.

---

## 22. Revision History

### 0.2.0 — 2026-07-17

- Established professional US English as the exclusive repository authoring
  language.
- Restricted non-English content to clearly identified original-language
  evidence accompanied by sufficient English context.
- Added mandatory `project.name` alongside the stable `project.id`.
- Removed ordinary document-level language metadata.
- Preserved conventional uppercase filenames for `README.md` and `AGENTS.md`.
- Defined the repository-authored filename convention.
- Proposed renaming `CONTRIBUTING_FOR_AI.md` to `Contributing_for_AI.md`.
- Proposed renaming `EDITORIAL_STYLE_GUIDE.md` to
  `Editorial_Style_Guide.md`.
- Added project identity to the native machine-index metadata profile.

### 0.1.0 — 2026-07-17

- Initial proposal.
- Defined the mandatory core metadata contract.
- Defined conditional artifact profiles.
- Exempted conventional repository entrypoints from front matter.
- Established native metadata for machine-readable artifacts.
- Defined lifecycle, maturity and quality semantics.
- Decided against creating `Repository_Architecture.md` at the current scale.
- Proposed archiving `Repository_Map.md`.
- Defined index maintenance and normalization rules.
- Added explicit reopening criteria.
