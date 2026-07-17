---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: RS-001
  title: Repository Standards
  type: Governance Standard
  version: 3.0.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Stable

owner: Štěpán Dvořák

purpose: >
  Defines the repository architecture, artifact profiles, metadata contract,
  lifecycle, language, naming, relationship, versioning, and contribution
  standards used throughout the Orden project.

quality:
  review: Approved
  evidence: N/A
  editorial: Approved

audience:
  - Contributors
  - AI Assistants
  - Researchers

depends_on:
  - Governance_Principles.md
  - Decisions/ADR-001_Repository_Artifact_Profiles_and_Metadata.md

related_documents:
  - AGENTS.md
  - Contributing_for_AI.md
  - Repository_Taxonomy.md
  - Editorial_Style_Guide.md
  - Reasoning_Standard.md
  - Repository_Index.yaml

tags:
  - governance
  - standards
  - repository
  - metadata
  - artifact-profile
---

# Repository Standards

## 1. Purpose

This document defines the mandatory repository-wide standards for the Orden
project.

It is the authoritative source for:

- repository architecture and artifact responsibilities;
- document and artifact profiles;
- mandatory and optional metadata;
- lifecycle, maturity, and quality semantics;
- repository language and filename conventions;
- document identity, relationships, and versioning;
- treatment of entrypoints, machine-readable artifacts, and archives.

The rationale for the current artifact and metadata model is recorded in
`Decisions/ADR-001_Repository_Artifact_Profiles_and_Metadata.md`.

---

## 2. Repository Principles

Repository work SHALL follow these principles:

- Evidence before conclusions.
- Explicit assumptions.
- Architectural neutrality.
- Reproducibility.
- Transparency.
- Uncertainty preservation.
- Reference over duplication.
- Evolution rather than silent replacement.
- Human-reviewed AI collaboration.
- Repository-wide consistency over local convenience.

The philosophical foundation of these requirements is defined in
`Governance_Principles.md`.

---

## 3. Repository Architecture

### 3.1 Architectural Model

The repository is a governed research knowledge base rather than an
undifferentiated document collection.

Every active artifact SHALL have one primary responsibility. Overlapping
responsibilities SHALL be resolved by reference to one authoritative source
rather than by duplicating rules or conclusions.

### 3.2 Responsibility Allocation

| Artifact or area | Primary responsibility |
|---|---|
| `README.md` | Human-facing project entrypoint and reading guidance. |
| `AGENTS.md` | Concise operational instructions discovered by AI agents. |
| `Governance_Principles.md` | Foundational governance philosophy. |
| `Repository_Standards.md` | Normative repository-wide structural rules. |
| `Repository_Taxonomy.md` | Canonical artifact categories and placement. |
| `Editorial_Style_Guide.md` | Editorial conventions for repository-authored content. |
| `Evidence_Hierarchy.md` | Relative authority of evidence sources. |
| `Reasoning_Standard.md` | Rules for deriving conclusions from evidence. |
| `Contributing_for_AI.md` | Operational workflow for AI-assisted contributions. |
| `Decisions/` | Accepted and proposed architecture decision records. |
| Root core research documents | Long-lived research scope, terminology, method, log, and related work. |
| `References/` | Source-specific research stubs and substantive reference analyses. |
| `Empirical/` | Evidence derived from applications, repositories, product behavior, or experiments. |
| `Historical_References/` | Historical sources and provenance. |
| `Ideas/` | Non-canonical future work and unvalidated proposals. |
| `Templates/` | Governed structures for new artifacts. |
| `Whitepaper/` | Research synthesis intended for publication. |
| `Archive/` | Superseded or historical artifacts excluded from ordinary retrieval. |
| `Repository_Index.yaml` | Machine-readable inventory, authority classification, and retrieval routing. |

### 3.3 Architecture Documentation Boundary

A separate `Repository_Architecture.md` is not required at the current
repository scale. Repository architecture is defined by this section,
`Repository_Taxonomy.md`, and the actual inventory in `Repository_Index.yaml`.

A dedicated architecture document MAY be introduced only when repository
complexity can no longer be represented concisely by these sources.

### 3.4 Navigation and Authority

`Repository_Index.yaml` and `README.md` are navigational artifacts. They SHALL
not override normative governance, canonical terminology, evidence, or owner
decisions.

---

## 4. Artifact Profiles

Every active artifact SHALL be assigned one profile.

| Profile | Purpose |
|---|---|
| `governed_document` | Governance, core research, terminology, framework, whitepaper, ADR, or governed template. |
| `reference_analysis` | Substantive analysis of a standard, publication, documentation, source code, or community source. |
| `empirical_study` | Evidence collected from applications, repositories, product behavior, or experiments. |
| `research_stub` | Intentional placeholder that scopes future research without conclusions. |
| `repository_entrypoint` | Conventional tool-defined entrypoint exempt from front matter. |
| `machine_index` | Native machine-readable inventory and retrieval artifact. |
| `archived_artifact` | Superseded or historical artifact excluded from ordinary retrieval. |

Templates use the `governed_document` profile with an appropriate
`document.type`. A separate template profile is not currently required.

---

## 5. Core Metadata Contract

### 5.1 Applicability

Every active Markdown artifact except an approved `repository_entrypoint` SHALL
begin with YAML front matter conforming to metadata schema `1.0`.

Native machine-readable artifacts SHALL expose the equivalent metadata defined
by their profile.

### 5.2 Mandatory Fields

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

The mandatory core fields are:

- `metadata_schema`;
- `project.id`;
- `project.name`;
- `document.id`;
- `document.title`;
- `document.type`;
- `document.version`;
- `document.status`;
- `classification.domain`;
- `classification.layer`;
- `classification.maturity`;
- `owner`;
- `purpose`.

Document IDs SHALL be permanent and unique. A rename or move SHALL NOT change a
document ID.

### 5.3 Conditional Fields

The `quality` group is mandatory for:

- normative governance documents;
- core research documents;
- reference analyses;
- empirical studies;
- framework and whitepaper syntheses.

```yaml
quality:
  review: Reviewed
  evidence: Partial
  editorial: Reviewed
```

Additional fields are mandatory when their condition applies:

| Field | Condition |
|---|---|
| `audience` | Normative or user-directed document. |
| `depends_on` | One or more documents are required to interpret or apply the artifact. |
| `supersedes` | The artifact replaces a previous active or archived artifact. |
| `evidence` | `reference_analysis` profile. |
| `study` | `empirical_study` profile. |
| `research_status` | `research_stub` profile. |

### 5.4 Optional Fields

The following MAY be included when they add real retrieval or governance value:

- `related_documents`;
- `tags`;
- `aliases`;
- `created`;
- `last_updated`;
- export-specific provenance fields.

`document.filename`, `created`, and `last_updated` SHALL NOT be required. The
filesystem and Git history are authoritative for filename and modification
history.

Aliases SHALL NOT introduce unauthorized terminology synonyms.

### 5.5 Relationship Keys

Metadata keys SHALL use `snake_case`.

The canonical relationship keys are:

- `depends_on`;
- `related_documents`;
- `supersedes`;
- `superseded_by`.

The legacy key `depends-on` SHALL NOT be used in new or normalized documents.

---

## 6. Lifecycle, Maturity, and Quality

### 6.1 Lifecycle Status

`document.status` records whether an artifact belongs to the current repository
baseline.

Allowed values are:

- `Proposed`;
- `Active`;
- `Deprecated`;
- `Archived`.

### 6.2 Maturity

`classification.maturity` records actual content completeness.

Allowed values are:

- `Stub`;
- `Draft`;
- `Review`;
- `Stable`.

Lifecycle and maturity are independent. An artifact MAY be both `Active` and
`Draft`.

### 6.3 Quality

Allowed `quality.review` values are:

- `Not Reviewed`;
- `Self Reviewed`;
- `Reviewed`;
- `Approved`;
- `N/A`.

Allowed `quality.evidence` values are:

- `Pending`;
- `Partial`;
- `Verified`;
- `N/A`.

Allowed `quality.editorial` values are:

- `Draft`;
- `Reviewed`;
- `Approved`;
- `N/A`.

Editorial quality SHALL NOT imply evidence verification or approval of
conclusions.

---

## 7. Profile-Specific Requirements

### 7.1 Governed Document

A governed document SHALL use the core contract. Normative or research-bearing
documents SHALL include `quality`. Normative documents SHALL include
`audience`.

### 7.2 Reference Analysis

A reference analysis SHALL include:

```yaml
evidence:
  source_authority: Official Vendor Documentation
  source_access: Full
  verification: Verified
```

Allowed `source_authority` values are:

- `Primary Standard`;
- `Peer-Reviewed Publication`;
- `SEI Publication`;
- `Official Vendor Documentation`;
- `Official Source Code`;
- `Official Product Behavior`;
- `Community Publication`;
- `Mixed Sources`.

Allowed `source_access` values are:

- `Full`;
- `Partial`;
- `Public Summary`;
- `Secondary Only`;
- `Mixed`.

Allowed `verification` values are:

- `Verified`;
- `Partial`;
- `Pending`.

Known source limitations SHOULD be recorded under `evidence.limitations`.

The document body SHALL distinguish source position, observation, research
interpretation, framework implication, uncertainty, and threats to validity.

### 7.3 Empirical Study

An empirical study SHALL include:

```yaml
study:
  method: Repository Code Audit
  subject: Anonymized Business Central Application
  data_access: Private Source Snapshot
  reproducibility: Restricted
```

The body SHALL identify threats to validity and SHALL NOT generalize a single
case as universal evidence.

### 7.4 Research Stub

A research stub SHALL include:

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

A research stub SHALL NOT establish conclusions, canonical terminology, or
verified evidence. It remains a valid active planning artifact.

### 7.5 Repository Entrypoint

The following conventional entrypoints are exempt from YAML front matter:

- `README.md`;
- `AGENTS.md`;
- `AGENTS.override.md`, if introduced.

Their role and authority SHALL be recorded in `Repository_Index.yaml`.

`README.md` SHALL provide concise human orientation and SHALL not duplicate the
full repository inventory or governance standards.

`AGENTS.md` SHALL contain concise operational instructions, required pre-reading,
and non-negotiable rules. It SHALL reference authoritative governance rather
than duplicate it.

### 7.6 Machine Index

`Repository_Index.yaml` SHALL use native top-level YAML metadata:

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

Machine artifacts SHALL NOT require companion Markdown metadata documents.

`source_commit` SHALL not be stored in the index. Git is authoritative for the
version containing the index. If a future generator requires an input boundary,
it MAY use `indexed_through_commit` with explicitly different semantics.

### 7.7 Archived Artifact

Artifacts under `Archive/`:

- are excluded from ordinary retrieval;
- SHALL NOT override active governance or canonical research;
- MAY retain historical metadata unchanged;
- SHALL NOT be normalized solely for current conformance;
- MAY be used for provenance, recovery, and historical comparison.

---

## 8. Repository Language

All repository-authored normative, research, navigational, and machine-readable
content SHALL use professional US English.

Repository-authored content SHALL use consistent forms such as `behavior`,
`analyze`, `catalog`, and `organization`.

Non-English content MAY appear only when necessary to preserve original
evidence, including source-code identifiers, localized labels or messages,
source quotations, and historical artifacts.

Original-language evidence SHALL:

- be identified as evidence;
- remain distinguishable from repository interpretation;
- include sufficient English explanation;
- include an English translation when required for understanding.

Document-level `language` metadata is not used for ordinary repository
documents because US English is the repository-wide default.

---

## 9. Filename and Path Rules

### 9.1 Conventional Filenames

Tool-defined conventional filenames retain their exact form:

- `README.md`;
- `AGENTS.md`;
- `AGENTS.override.md`, if introduced.

### 9.2 Repository-Authored Filenames

Repository-authored Markdown filenames SHALL:

- separate words with underscores;
- capitalize principal words;
- keep minor connecting words such as `for`, `and`, `of`, and `to` lowercase;
- preserve uppercase abbreviations such as `AI`, `ISO`, `SEI`, and `ADR`;
- use `.md`;
- avoid spaces and unnecessary full-uppercase naming.

Examples:

- `Repository_Standards.md`;
- `Editorial_Style_Guide.md`;
- `Contributing_for_AI.md`;
- `Repository_Conformance_Report.md`.

### 9.3 Path Integrity

Paths in metadata and active documents SHALL:

- be relative to the repository root;
- use `/` as the separator;
- use exact filename case;
- identify the active canonical artifact unless historical context is explicit;
- include the directory when the artifact is not in the root.

---

## 10. Document Identification

Every governed document SHALL receive a permanent unique ID.

Recommended prefixes include:

| Prefix | Artifact |
|---|---|
| `RS` | Repository Standard |
| `GOV` | Governance Document |
| `ADR` | Architecture Decision Record |
| `RD` | Research Document |
| `ES` | Empirical Study |
| `CS` | Case Study |
| `TR` | Terminology Document |
| `RW` | Related Work |
| `REF` | Reference Analysis or Stub |

New prefixes SHALL be documented before use. Existing permanent IDs SHALL not
be changed solely to match a preferred prefix.

---

## 11. Relationship Model

Documents SHOULD reference related knowledge explicitly without duplicating its
authority.

`depends_on` means the referenced artifact is required to interpret or apply
the current artifact.

`related_documents` means the referenced artifact provides useful context but
is not required.

`supersedes` and `superseded_by` record replacement relationships.

Every active relationship path SHALL resolve with exact case. References to
planned or missing artifacts SHALL be marked explicitly and SHALL not appear as
normative dependencies.

---

## 12. Versioning

Repository documents SHALL use Semantic Versioning.

- MAJOR: incompatible normative, structural, or scope change;
- MINOR: backward-compatible capability or substantive addition;
- PATCH: backward-compatible correction or editorial improvement.

For documents below `1.0.0`, structural metadata normalization SHOULD increment
the minor version. For stable documents at or above `1.0.0`, metadata-only
corrections SHOULD increment the patch version.

Version changes SHALL reflect the document, not the repository release.

---

## 13. Repository Index Maintenance

`Repository_Index.yaml` is the machine-readable inventory and retrieval router.
It SHALL be reviewed or regenerated when:

- an active artifact is added, renamed, moved, deprecated, or archived;
- authority, type, or maturity changes;
- a research stub becomes a substantive analysis;
- a canonical definition source changes;
- a planned artifact is created;
- a query route or governance precedence changes;
- an archived family gains an active replacement.

Validation SHALL include exact paths, unique IDs, dependency resolution,
archive replacements, stub warnings, and planned-versus-existing status.

Manual maintenance is acceptable until automation provides demonstrated value.

---

## 14. AI Contributions

AI-assisted contributions are permitted, subject to these rules:

- AI SHALL follow repository governance before task-specific instructions.
- AI SHALL not replace evidence or invent references.
- AI SHALL preserve canonical terminology and uncertainty.
- AI SHALL distinguish structural normalization from substantive revision.
- AI SHALL preserve or correctly migrate metadata.
- Human authority and review remain mandatory.

The detailed operational workflow is defined in `Contributing_for_AI.md`.

---

## 15. Conformance and Migration

Documents created after this standard becomes active SHALL conform immediately.

Existing active documents MAY be migrated in controlled phases. Temporary
nonconformance during an approved migration does not invalidate their content,
but SHALL remain visible in the normalization backlog.

Structural normalization SHALL NOT silently alter claims, findings,
definitions, hypothesis status, confidence, source interpretation, threats to
validity, or recorded uncertainty.

Archived artifacts are exempt from migration unless reactivated.

Machine-readable validation SHOULD be introduced after the first normalized
artifact set confirms that metadata schema `1.0` is practical.

---

## 16. Governance Change

Changes to mandatory fields, artifact profiles, controlled values, language,
or special-file exceptions require:

- an accepted ADR or an explicit amendment to an existing ADR;
- a compatibility assessment;
- a migration plan when existing artifacts are affected;
- coordinated updates to this standard and `Repository_Index.yaml`.

Preference alone is not sufficient reason to reopen an accepted decision.

---

## 17. Revision History

### 3.0.0 — 2026-07-17

- Implemented ADR-001.
- Defined repository architecture and responsibility allocation.
- Established artifact profiles and the mandatory metadata contract.
- Added lifecycle, maturity, and quality vocabularies.
- Established professional US English.
- Defined conventional and repository-authored filename rules.
- Added profile-specific requirements for analyses, studies, stubs, entrypoints,
  machine indexes, and archives.
- Removed the dependency on a separate repository architecture document.
- Defined repository index maintenance and phased migration.

### 2.0.0 — 2026-07-17

- Established the initial grouped repository metadata and governance model.
