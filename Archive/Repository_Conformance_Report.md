---
project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: GOV-CR-001
  title: Repository Conformance Report
  filename: Repository_Conformance_Report.md
  type: Conformance Report
  version: 0.1.0
  status: Draft

classification:
  domain: Governance
  layer: Repository
  maturity: Draft

owner: Štěpán Dvořák

created: 2026-07-17
last_updated: 2026-07-17

quality:
  review: Draft
  evidence: Repository Inspection
  editorial: Draft

purpose: >
  Evaluates the structural conformance of active root documents and reference
  documents against the current Orden repository governance baseline, and
  defines a prioritized normalization backlog before further research proceeds.

audience:
  - Repository Owner
  - Contributors
  - AI Assistants

depends_on:
  - Governance_Principles.md
  - Repository_Standards.md
  - Repository_Taxonomy.md
  - EDITORIAL_STYLE_GUIDE.md
  - Reasoning_Standard.md
  - CONTRIBUTING_FOR_AI.md
  - Repository_Index.yaml

related_documents:
  - AGENTS.md
  - Repository_Map.md
  - Terminology_Index.md

tags:
  - governance
  - conformance
  - normalization
  - repository
  - quality
---

# Repository Conformance Report

## 1. Purpose

This report evaluates the current structural conformance of the active Orden
repository before further research continues in `References/`.

Its purpose is to:

- identify differences between current documents and `Repository_Standards.md`;
- distinguish structural normalization from substantive research revision;
- identify governance gaps that must be resolved before large-scale normalization;
- classify reference documents by actual maturity rather than file size alone;
- establish a safe and reproducible normalization order;
- prevent formatting work from silently changing research claims.

This is a diagnostic report. It does not modify, supersede, or normalize any
evaluated document.

---

## 2. Scope

### 2.1 Included

The inspection covers:

- all active Markdown documents in the repository root;
- `Repository_Index.yaml` as a repository-level machine-readable artifact;
- all Markdown documents directly under `References/`;
- relationships among governance documents where they affect conformance;
- filename and path consistency where references are case-sensitive.

### 2.2 Excluded

The following are outside this report's document-by-document assessment:

- `Archive/`, except where an active document incorrectly resolves to it;
- `Empirical/`;
- `Historical_References/`;
- `Ideas/`;
- `Templates/`;
- `.obsidian/` configuration;
- substantive verification of external sources;
- validation of the truth of research findings;
- editorial rewriting of document content.

These areas may require later conformance reviews after the root governance and
active reference baseline has been normalized.

---

## 3. Inspection Baseline

### 3.1 Repository State

The report is based on:

- repository: `stepan-dvorak/BehaviorChangeReviewFramework`;
- branch: `main`;
- inspected commit: `36e1e8bf999ba2e3d7cf5e75a8bb612598de5f25`;
- inspection date: 2026-07-17.

The inspected commit includes `Repository_Index.yaml`, merged through pull
request #1.

### 3.2 Applicable Governance

The following active documents were treated as the current governance baseline:

1. `Governance_Principles.md`
2. `Repository_Standards.md`
3. `Repository_Taxonomy.md`
4. `EDITORIAL_STYLE_GUIDE.md`
5. `Reasoning_Standard.md`
6. `CONTRIBUTING_FOR_AI.md`
7. `AGENTS.md`

The precedence is derived from current governance and
`Repository_Index.yaml`. The intended `Repository_Architecture.md` could not be
applied because it does not exist.

### 3.3 Conformance Limitation

`Repository_Standards.md` defines the expected metadata groups and repository
principles, but it does not yet provide a complete machine-testable schema.

In particular, it does not unambiguously define:

- which front matter fields are mandatory for every document;
- which document types may use reduced metadata;
- whether `README.md`, `AGENTS.md`, indexes, and maps are exceptions;
- how non-Markdown artifacts represent equivalent metadata;
- the complete controlled vocabulary for `type`, `domain`, and `layer`;
- whether status belongs under `document.status`, at the top level, or both;
- the required relationship-key spelling convention;
- whether filenames must use title case, uppercase, or another convention.

Therefore, this report distinguishes **clear nonconformance** from
**baseline ambiguity**. It does not invent missing requirements.

---

## 4. Assessment Model

### 4.1 Conformance Ratings

| Rating | Meaning |
|---|---|
| Conformant | Satisfies the current applicable structural requirements with no material issue identified. |
| Substantially conformant | Uses the current model but has limited omissions or inconsistencies. |
| Partially conformant | Contains some required structures but uses a legacy or incomplete metadata model. |
| Nonconformant | Lacks the structural elements required by the current standard. |
| Baseline exception required | The artifact does not fit the current standard and requires an explicit governance decision. |
| Research stub | Structurally incomplete research placeholder; must not be interpreted as a completed analysis. |

### 4.2 Assessment Dimensions

Each document is evaluated against the following dimensions:

| Code | Dimension | Assessment question |
|---|---|---|
| M | Metadata | Does the artifact provide current YAML front matter or an explicitly permitted equivalent? |
| I | Identity | Does it have a stable document ID, filename, type, version, and status? |
| C | Classification | Does it declare domain, layer, and maturity consistently? |
| Q | Quality | Does it declare independent review, evidence, and editorial status where applicable? |
| R | Relationships | Are dependencies and related documents explicit and resolvable? |
| S | Structure | Does the document structure match its actual purpose and repository conventions? |
| T | Terminology | Does it use canonical terminology and preserve Candidate status? |
| E | Evidence | Are evidence, interpretation, uncertainty, and conclusions appropriately separated? |
| P | Path integrity | Do filenames and referenced paths resolve with exact case? |
| A | Actual maturity | Does the declared or implied status reflect the actual completeness of the artifact? |

### 4.3 Normalization Types

Two different operations are required and SHALL remain separate.

#### Structural normalization

May change:

- YAML front matter;
- document identity;
- classification;
- relationship metadata;
- section organization;
- filename references;
- formatting;
- explicit maturity labeling.

It SHALL NOT silently change:

- claims;
- findings;
- definitions;
- hypothesis status;
- confidence assessments;
- interpretation of sources;
- research conclusions.

#### Substantive revision

May change research content, but only after source verification and an explicit
reasoning review. It should be performed separately from structural
normalization so that the origin of every changed conclusion remains traceable.

---

## 5. Executive Findings

### 5.1 Overall Assessment

The repository is conceptually governed but not yet structurally normalized.
The newest governance documents demonstrate a substantially more complete
metadata model than the earlier core and reference documents. As a result, the
repository currently contains three generations of document structure:

1. current grouped metadata used by the newest governance documents;
2. legacy minimal front matter used by early core research documents;
3. documents with no front matter, including completed analyses and research
   stubs.

No inspected Markdown document can be declared unconditionally conformant to a
fully specified repository schema because such a complete schema does not yet
exist. `Repository_Standards.md` itself is the closest example of the intended
model.

### 5.2 Quantitative Summary

The inspected set contains:

- 16 Markdown documents in the repository root;
- 1 root YAML artifact;
- 14 Markdown documents under `References/`;
- 30 Markdown documents in total;
- 31 artifacts when `Repository_Index.yaml` is included.

Front matter coverage:

- 8 of 30 inspected Markdown documents contain YAML front matter;
- 22 of 30 contain no YAML front matter;
- only 3 use the current grouped governance metadata model with most expected
  fields;
- 5 use partial or legacy front matter;
- none of the 14 reference documents uses the full current grouped model;
- 1 reference document uses legacy front matter;
- 11 reference documents have no front matter.

### 5.3 Principal Findings

1. Governance must be stabilized before mass normalization.
2. `Repository_Architecture.md` is a high-impact missing dependency.
3. Mandatory and optional metadata fields are not defined precisely enough for
   deterministic validation.
4. Root governance documents vary substantially in their own conformance.
5. The five early core research documents use a legacy metadata model.
6. Substantive ISO, SEI, and Microsoft analyses lack current repository
   metadata.
7. Several small reference files are research stubs, not short completed
   studies.
8. File size is a useful discovery signal but not a valid maturity criterion.
9. `Repository_Map.md` is incomplete and must not be used as the authoritative
   inventory.
10. `Repository_Index.yaml` improves retrieval but requires an explicit
    non-Markdown artifact policy and routine regeneration rules.

---

## 6. Governance-Level Blocking Issues

### GOV-BLOCK-001 — Missing Repository Architecture

**Severity:** High  
**Status:** Open

`Repository_Architecture.md` is referenced by several governance documents but
does not exist.

Affected documents include:

- `CONTRIBUTING_FOR_AI.md`;
- `Governance_Principles.md`;
- `Repository_Standards.md`.

**Impact:** The repository defines architecture as a governance dependency
without providing its authoritative content. Classification, document
relationships, directory responsibilities, and artifact roles therefore lack
one intended source of authority.

**Required decision:** Either create `Repository_Architecture.md` or remove and
replace every dependency on it.

### GOV-BLOCK-002 — Incomplete Metadata Contract

**Severity:** High  
**Status:** Open

The standard presents metadata groups and recommended fields but does not define
a complete required schema.

**Impact:** Conformance cannot be deterministically validated. Two contributors
may normalize the same document differently while both plausibly follow the
standard.

**Required decision:** Define:

- mandatory fields for every document;
- conditional fields by document type;
- controlled values;
- date format;
- version format;
- relationship-key naming;
- allowed exceptions.

### GOV-BLOCK-003 — Non-Markdown Artifact Policy

**Severity:** Medium  
**Status:** Open

`Repository_Index.yaml` is a repository artifact, but the current rule that
every document begins with YAML front matter cannot apply literally to a YAML
file.

**Impact:** The index cannot be evaluated consistently against the current
document standard.

**Required decision:** Define an artifact category with either:

- native top-level metadata equivalent to front matter;
- a companion metadata record;
- an explicit exemption.

### GOV-BLOCK-004 — Filename Canonicalization

**Severity:** Medium  
**Status:** Open

Governance references use `Editorial_Style_Guide.md`, while the actual file is
`EDITORIAL_STYLE_GUIDE.md`.

**Impact:** References fail on case-sensitive systems and reduce retrieval
reliability.

**Required decision:** Select one canonical filename and update every active
reference atomically.

### GOV-BLOCK-005 — Relationship-Key Convention

**Severity:** Medium  
**Status:** Open

Documents use both `depends_on` and `depends-on`.

**Impact:** Automated relationship resolution requires special cases and may
miss dependencies.

**Required decision:** Adopt one canonical key. The current grouped governance
documents favor `depends_on`.

### GOV-BLOCK-006 — Authority and Maturity Semantics

**Severity:** Medium  
**Status:** Open

The repository uses overlapping values such as `Active`, `Draft`, `Stable`,
`Approved`, `Verified`, `current`, and `research_stub` across different fields
and artifacts.

**Impact:** An active document may still be a draft, but current structures do
not always make this distinction visible.

**Required decision:** Preserve separate dimensions for:

- lifecycle status;
- maturity;
- review status;
- evidence status;
- editorial status;
- retrieval authority.

---

## 7. Root Document Conformance Matrix

| Document | Size | Current metadata | Rating | Priority | Principal action |
|---|---:|---|---|---|---|
| `README.md` | 270 B | None | Baseline exception required | P2 | Define reduced metadata or explicit README exemption; improve navigation after governance stabilizes. |
| `AGENTS.md` | 543 B | None | Baseline exception required | P1 | Define agent-instruction exception or add compact governed metadata; validate precedence. |
| `Governance_Principles.md` | 5.2 kB | Grouped, incomplete | Substantially conformant | P0 | Add owner, dates, quality; resolve missing architecture and filename references. |
| `Repository_Standards.md` | 4.1 kB | Grouped, broad | Substantially conformant | P0 | Complete the normative metadata contract and artifact exceptions before other normalization. |
| `CONTRIBUTING_FOR_AI.md` | 25.9 kB | Grouped, broad | Substantially conformant | P0 | Resolve invalid paths; reconcile hierarchy with actual files; review metadata consistency. |
| `Reasoning_Standard.md` | 4.8 kB | Grouped, incomplete | Substantially conformant | P0 | Add owner, dates, quality; resolve filename references. |
| `EDITORIAL_STYLE_GUIDE.md` | 698 B | None | Nonconformant | P0 | Assign permanent identity and full metadata; decide canonical filename; expand only where required. |
| `Evidence_Hierarchy.md` | 574 B | None | Nonconformant | P0 | Assign identity, metadata, scope, relationship to methodology, and authority semantics. |
| `Repository_Taxonomy.md` | 796 B | None | Nonconformant | P0 | Assign identity and metadata; align categories with actual repository and index values. |
| `Repository_Map.md` | 538 B | None | Nonconformant | P2 | Add metadata; regenerate after architecture and taxonomy are stable; mark as navigational. |
| `Terminology_Index.md` | 710 B | None | Nonconformant | P1 | Add metadata; correct the IsHandled definition path; align statuses with terminology sources. |
| `00_Project_Charter.md` | 4.5 kB | Legacy minimal | Partially conformant | P1 | Migrate metadata without changing scope, hypothesis, or success criteria. |
| `00_Research_Log.md` | 3.2 kB | Legacy minimal | Partially conformant | P1 | Migrate metadata; preserve chronological and rejected-idea content. |
| `01_Terminology.md` | 5.7 kB | Legacy minimal | Partially conformant | P1 | Migrate metadata and relationship keys; reconcile with `Terminology_Index.md` without prematurely validating candidates. |
| `02_Research_Methodology.md` | 5.3 kB | Legacy minimal | Partially conformant | P1 | Migrate metadata; reconcile its evidence hierarchy with `Evidence_Hierarchy.md` and `Reasoning_Standard.md`. |
| `03_Related_Work.md` | 6.1 kB | Legacy minimal | Partially conformant | P1 | Migrate metadata; preserve provisional assessments and open questions. |
| `Repository_Index.yaml` | 30.2 kB | Native YAML metadata | Baseline exception required | P1 | Define artifact policy; update source commit and regenerate after normalization. |

Priority meanings:

- **P0:** governance prerequisite;
- **P1:** normalize before substantive reference research;
- **P2:** normalize after canonical governance and core documents;
- **P3:** defer until the relevant research task begins.

---

## 8. Root Document Findings

### 8.1 `Repository_Standards.md`

**Role:** Constitutional repository standard  
**Rating:** Substantially conformant  
**Priority:** P0

Strengths:

- current grouped front matter;
- permanent document ID;
- explicit type, version, status, classification, owner, dates, quality,
  purpose, audience, relationships, and tags;
- clear separation of maturity from quality in the body.

Gaps:

- required versus recommended metadata remains ambiguous;
- examples do not form a complete schema;
- exception rules are absent;
- controlled vocabularies are illustrative rather than exhaustive;
- the relationship model does not fix a canonical key naming convention;
- references include missing or case-mismatched files;
- no validation algorithm is specified.

Normalization action:

Treat this as the first governance document to revise. Changes should clarify
existing intent rather than expand the project's research scope.

### 8.2 `Governance_Principles.md`

**Role:** Foundational governance philosophy  
**Rating:** Substantially conformant  
**Priority:** P0

Gaps:

- no owner;
- no created or last-updated date;
- no quality group;
- references include missing `Repository_Architecture.md` and a
  case-mismatched editorial guide;
- `document.status` and `classification.maturity` both use Draft, but their
  distinct meanings are not explained locally.

Substantive caution:

The principles themselves should not be rewritten during metadata
normalization. Any change to principle meaning requires a separate governance
decision.

### 8.3 `CONTRIBUTING_FOR_AI.md`

**Role:** Normative AI operating workflow  
**Rating:** Substantially conformant  
**Priority:** P0

Strengths:

- broad current metadata;
- explicit dependencies and audience;
- complete workflow covering context, knowledge, reasoning, realization,
  validation, and delivery.

Gaps:

- references to missing `Repository_Architecture.md`;
- references to `Editorial_Style_Guide.md` do not match the actual filename;
- hierarchy includes files whose roles have not yet been structurally
  normalized;
- document is Active while maturity and quality remain Draft, which is
  defensible but should be explicitly supported by lifecycle semantics.

### 8.4 `Reasoning_Standard.md`

**Role:** Normative reasoning standard  
**Rating:** Substantially conformant  
**Priority:** P0

Gaps:

- no owner, dates, or quality group;
- case-mismatched editorial reference;
- evidence classification overlaps with `Evidence_Hierarchy.md` and
  `02_Research_Methodology.md`; authoritative responsibility boundaries need
  explicit confirmation.

### 8.5 `EDITORIAL_STYLE_GUIDE.md`

**Role:** Normative editorial standard  
**Rating:** Nonconformant  
**Priority:** P0

Gaps:

- no front matter;
- no permanent ID;
- no version, status, classification, quality, owner, dates, or relationships;
- filename differs from active references;
- concise content may be sufficient, but its normative responsibility and
  applicability require metadata.

### 8.6 `Evidence_Hierarchy.md`

**Role:** Normative evidence ranking  
**Rating:** Nonconformant  
**Priority:** P0

Gaps:

- no metadata or permanent identity;
- no explicit scope;
- relationship to the methodology and reasoning standard is implicit;
- ordering Microsoft Learn above official source code may require rationale;
- evidence authority and evidence relevance are not distinguished.

Substantive caution:

Any change to evidence ordering is a research-governance decision, not
structural normalization.

### 8.7 `Repository_Taxonomy.md`

**Role:** Canonical repository classification  
**Rating:** Nonconformant  
**Priority:** P0

Gaps:

- no metadata or identity;
- categories do not fully describe all current directories and artifact types;
- `Repository_Index.yaml` uses classifications not explicitly governed here;
- no mapping from taxonomy category to metadata `classification.domain`;
- no placement rules for indexes, maps, historical references, ideas, or
  machine-readable artifacts.

### 8.8 Early Core Research Documents

Affected documents:

- `00_Project_Charter.md`;
- `00_Research_Log.md`;
- `01_Terminology.md`;
- `02_Research_Methodology.md`;
- `03_Related_Work.md`.

**Rating:** Partially conformant  
**Priority:** P1

Shared strengths:

- all contain parseable YAML front matter;
- all declare project, status, and version;
- the three dependent documents identify dependencies;
- all remain explicitly Draft.

Shared gaps:

- legacy project metadata is a scalar rather than the grouped current form;
- no document IDs;
- no document type or filename metadata;
- no classification group;
- no owner or dates;
- no quality group;
- no audience, purpose metadata, related documents, or tags;
- relationship key uses `depends-on`, unlike current `depends_on`;
- status is top-level rather than under document identity.

Normalization caution:

These files contain the research project's foundational uncertainty. Structural
normalization must preserve:

- Draft status;
- Candidate terminology;
- open questions;
- rejected directions;
- unverified hypotheses;
- recorded research evolution.

### 8.9 Navigational and Entry Documents

Affected documents:

- `README.md`;
- `AGENTS.md`;
- `Repository_Map.md`;
- `Terminology_Index.md`.

All lack front matter, but they have different roles. Applying the same full
metadata blindly may make small entry documents noisy and harder to use.

Required governance decision:

Define whether each role uses:

- full standard metadata;
- a reduced mandatory profile;
- an explicit exception linked from the repository index.

`Terminology_Index.md` additionally contains a resolvable content defect: it
points several concepts to `Microsoft_IsHandled.md`, while the current canonical
document is `References/Microsoft_IsHandled_v2.0.md`.

---

## 9. Reference Document Conformance Matrix

| Document | Size | Actual maturity | Metadata | Rating | Priority | Principal action |
|---|---:|---|---|---|---|---|
| `References/ISO_42010.md` | 26.7 kB | Substantive analysis | None | Nonconformant | P1 | Add full metadata, dependencies, source status, quality, and traceability without changing findings. |
| `References/ISO_42020.md` | 15.1 kB | Substantive analysis | None | Nonconformant | P1 | Add full metadata and explicit relationship to 42010/42030; preserve source limitations. |
| `References/ISO_42030.md` | 17.8 kB | Substantive analysis | None | Nonconformant | P1 | Add full metadata; preserve accepted, candidate, and open findings. |
| `References/SEI_Documenting_Behavior.md` | 7.7 kB | Substantive analysis | None | Nonconformant | P1 | Add full metadata and explicit evidence limitations. |
| `References/Microsoft_Extensibility_Overview.md` | 8.3 kB | Substantive analysis | None | Nonconformant | P1 | Add full metadata and source/evidence status; retain Microsoft-versus-interpretation separation. |
| `References/Microsoft_IsHandled_v2.0.md` | 49.8 kB | Substantive canonical study | Legacy partial | Partially conformant | P1 | Migrate metadata to current model; preserve layered method and confidence assessments. |
| `References/ATAM.md` | 916 B | Research stub | None | Research stub | P3 | Add metadata identifying it explicitly as a stub; complete later as research. |
| `References/SAAM.md` | 843 B | Research stub | None | Research stub | P3 | Add stub metadata; complete after ATAM or according to research plan. |
| `References/DDD.md` | 865 B | Research stub | None | Research stub | P3 | Add stub metadata; do not present planned headings as findings. |
| `References/Fowler.md` | 875 B | Research stub | None | Research stub | P3 | Add stub metadata and identify intended source scope before research. |
| `References/Workflow_BPM.md` | 856 B | Research stub | None | Research stub | P3 | Add stub metadata; define literature scope before substantive work. |
| `References/Plugin_Architectures.md` | 884 B | Research stub | None | Research stub | P3 | Add stub metadata; define primary-source selection criteria. |
| `References/Microsoft_Event_Types.md` | 864 B | Research stub | None | Research stub | P2 | Add stub metadata, then complete as an early Microsoft research task. |
| `References/Microsoft_Interfaces.md` | 881 B | Research stub | None | Research stub | P2 | Add stub metadata, then complete as an early Microsoft research task. |

## 10. Reference Document Findings

### 10.1 Substantive Standards Analyses

Affected documents:

- `References/ISO_42010.md`;
- `References/ISO_42020.md`;
- `References/ISO_42030.md`;
- `References/SEI_Documenting_Behavior.md`.

These are not stubs. They contain extensive analysis, findings, limitations,
counterarguments, and implications. Their absence of metadata is therefore a
high-priority structural defect.

Required normalization:

- assign stable IDs;
- declare document type and version;
- classify domain, layer, and maturity;
- record source status and evidence limitations;
- declare quality dimensions independently;
- record dependencies and related documents;
- add tags and purpose metadata;
- preserve each finding's current status;
- preserve uncertainty concerning access to full standards text.

No finding should be promoted from Candidate or Open during this pass.

### 10.2 Substantive Microsoft Analyses

Affected documents:

- `References/Microsoft_Extensibility_Overview.md`;
- `References/Microsoft_IsHandled_v2.0.md`.

`Microsoft_Extensibility_Overview.md` has no front matter despite containing a
developed evidence-and-interpretation structure.

`Microsoft_IsHandled_v2.0.md` has legacy front matter containing:

- status;
- version;
- type;
- title;
- project;
- source type;
- dependencies.

It lacks the current grouped identity, classification, quality, owner, dates,
audience, explicit purpose metadata, related documents, and tags.

Because `Microsoft_IsHandled_v2.0.md` is the canonical active synthesis for its
subject, it should be normalized before additional mechanism-specific research
is integrated into the framework.

### 10.3 Research Stubs

Affected documents:

- `References/ATAM.md`;
- `References/SAAM.md`;
- `References/DDD.md`;
- `References/Fowler.md`;
- `References/Workflow_BPM.md`;
- `References/Plugin_Architectures.md`;
- `References/Microsoft_Event_Types.md`;
- `References/Microsoft_Interfaces.md`.

These files share a generic planned structure:

- Purpose;
- Summary;
- Relevance to the Research;
- Concepts to Extract;
- Potential Contribution;
- Open Research Questions;
- Action Items;
- References.

The headings describe intended research, not completed evidence. Their small
size is correlated with stub status, but the status is established from their
content, not from a fixed size threshold.

Required immediate action:

- add metadata identifying `maturity: Draft` and an explicit research-stub
  status;
- avoid assigning evidence quality such as Verified;
- identify intended primary sources where already known;
- retain open questions;
- do not fill sections with unsupported summary text merely to achieve visual
  completeness.

Substantive completion belongs to the next research phase.

---

## 11. Cross-Document Consistency Findings

### CONS-001 — Evidence Governance Overlap

Evidence handling is distributed across:

- `Evidence_Hierarchy.md`;
- `Reasoning_Standard.md`;
- `02_Research_Methodology.md`;
- `EDITORIAL_STYLE_GUIDE.md`;
- `CONTRIBUTING_FOR_AI.md`.

The responsibilities are related but not fully delineated. Normalization should
reference a single authoritative rule rather than duplicate it.

Recommended responsibility split:

- `Evidence_Hierarchy.md`: source authority and evidence ranking;
- `Reasoning_Standard.md`: inference categories and conclusion formation;
- `02_Research_Methodology.md`: research procedure and acceptance criteria;
- `EDITORIAL_STYLE_GUIDE.md`: presentation of evidence and interpretation;
- `CONTRIBUTING_FOR_AI.md`: operational workflow applying the other standards.

### CONS-002 — Terminology Sources

Terminology is distributed across:

- `Terminology_Index.md`;
- `01_Terminology.md`;
- `References/Microsoft_IsHandled_v2.0.md`;
- the whitepaper draft outside this report's direct scope.

Recommended responsibility split:

- `Terminology_Index.md`: canonical registry and lookup;
- `01_Terminology.md`: complete project definitions and term relationships;
- reference studies: source-specific candidate concepts and evidence;
- whitepaper: contextual use, not independent redefinition.

### CONS-003 — Status Vocabulary

Current artifacts use multiple status dimensions without a fully enforced
mapping. Examples include:

- `Active`;
- `Draft`;
- `Stable`;
- `current`;
- `research_draft`;
- `research_stub`;
- `Approved`;
- `Verified`;
- `Reviewed`.

These values are not necessarily contradictory, but they must belong to
separate named dimensions.

### CONS-004 — Planned Versus Existing Documents

The charter plans documents that do not yet exist under their intended names:

- `04_Existing_BC_Guidance.md`;
- `05_Framework.md`;
- `06_BC_Pattern_Catalog.md`;
- `07_Example_Catalog.md`;
- `08_Decision_Tree.md`;
- `Whitepaper.md`.

Some planned responsibilities are partially represented by current documents,
but planned paths must not be treated as existing sources.

### CONS-005 — Map and Index Roles

`Repository_Map.md` is a short human-oriented map. `Repository_Index.yaml` is a
machine-oriented semantic retrieval index. Their roles should remain distinct:

- the map explains repository organization to humans;
- the index routes retrieval and records machine-readable status;
- neither overrides normative governance;
- both must be updated when canonical paths change.

---

## 12. Recommended Normalization Programme

### Phase 0 — Governance Baseline Decision

Before modifying the wider repository:

1. complete the metadata contract in `Repository_Standards.md`;
2. define reduced profiles or exceptions for special artifacts;
3. decide the canonical editorial-guide filename;
4. standardize `depends_on` or another relationship-key convention;
5. define lifecycle, maturity, quality, and authority as separate dimensions;
6. decide whether to create `Repository_Architecture.md`;
7. record these decisions in an ADR or an equivalent approved governance
   change.

**Exit criterion:** Two independent contributors can classify and normalize the
same document to the same metadata structure without inventing values.

### Phase 1 — Normalize Normative Governance

Recommended order:

1. `Repository_Standards.md`
2. `Governance_Principles.md`
3. `Repository_Taxonomy.md`
4. `Repository_Architecture.md`, if approved
5. `EDITORIAL_STYLE_GUIDE.md`
6. `Evidence_Hierarchy.md`
7. `Reasoning_Standard.md`
8. `CONTRIBUTING_FOR_AI.md`
9. `AGENTS.md`

**Exit criterion:** Every active normative rule has one authoritative source,
valid metadata, and resolvable relationships.

### Phase 2 — Normalize Core Research

Recommended order:

1. `00_Project_Charter.md`
2. `00_Research_Log.md`
3. `01_Terminology.md`
4. `Terminology_Index.md`
5. `02_Research_Methodology.md`
6. `03_Related_Work.md`

This phase should be metadata-first. Any discovered substantive conflict should
be logged for a later research revision rather than silently resolved.

**Exit criterion:** Core documents use current metadata and relationships while
preserving all uncertainty and research status.

### Phase 3 — Normalize Completed Reference Analyses

Recommended order:

1. `References/ISO_42010.md`
2. `References/ISO_42020.md`
3. `References/ISO_42030.md`
4. `References/SEI_Documenting_Behavior.md`
5. `References/Microsoft_Extensibility_Overview.md`
6. `References/Microsoft_IsHandled_v2.0.md`

The order may be grouped into separate standards and Microsoft commits, but
each commit should remain structurally focused.

**Exit criterion:** Every substantive reference analysis has stable identity,
classification, quality status, source limitations, and explicit relationships.

### Phase 4 — Classify Research Stubs

Add current metadata without pretending that research is complete:

1. `References/Microsoft_Event_Types.md`
2. `References/Microsoft_Interfaces.md`
3. `References/ATAM.md`
4. `References/SAAM.md`
5. `References/Plugin_Architectures.md`
6. `References/Workflow_BPM.md`
7. `References/DDD.md`
8. `References/Fowler.md`

**Exit criterion:** Retrieval systems and readers can distinguish every stub
from a completed analysis.

### Phase 5 — Regenerate Navigation

After canonical documents are stable:

1. update `Repository_Map.md`;
2. update `README.md`;
3. regenerate `Repository_Index.yaml`;
4. update `source_commit` or replace it with a less fragile generation model;
5. validate all indexed paths and relationships.

**Exit criterion:** Human and AI navigation reflects the same repository state.

### Phase 6 — Resume Research

Recommended research sequence:

1. `References/Microsoft_Event_Types.md`
2. `References/Microsoft_Interfaces.md`
3. `References/ATAM.md`
4. `References/SAAM.md`
5. `References/Plugin_Architectures.md`
6. `References/Workflow_BPM.md`
7. `References/DDD.md`
8. `References/Fowler.md`

This sequence prioritizes direct Business Central guidance and architecture
evaluation methods before more distant related-work domains.

---

## 13. Proposed Commit Strategy

Normalization should not be delivered as one repository-wide commit.

Recommended commit groups:

1. **Define conformance baseline**  
   Metadata schema, artifact profiles, path conventions, and architecture
   decision.

2. **Normalize governance documents**  
   Structural changes only.

3. **Normalize core research metadata**  
   Preserve all existing research content.

4. **Normalize standards reference metadata**  
   ISO and SEI analyses.

5. **Normalize Microsoft reference metadata**  
   Microsoft extensibility and IsHandled analyses.

6. **Classify reference research stubs**  
   Metadata and status only.

7. **Regenerate repository navigation**  
   Map, README, terminology index paths, and machine index.

Each pull request should state explicitly whether it is:

- structural only;
- substantive research revision;
- mixed by deliberate owner approval.

---

## 14. Validation Requirements

After every normalization phase, validate:

### 14.1 Metadata

- YAML parses successfully;
- required groups and fields are present;
- document IDs are unique;
- versions follow the approved convention;
- dates use the approved format;
- controlled values are valid;
- actual maturity matches declared maturity.

### 14.2 Relationships

- every dependency path exists with exact case;
- no current document depends on an archived version when a canonical version
  exists;
- related documents are not used as a substitute for dependencies;
- circular governance dependencies are reported and justified.

### 14.3 Content Preservation

- Candidate concepts remain Candidate unless separately reviewed;
- hypotheses are not converted into conclusions;
- open questions remain visible;
- rejected ideas remain recorded;
- source limitations remain present;
- no reference is invented;
- substantive text is byte-identical where the change is declared
  metadata-only, except for explicitly listed structural adjustments.

### 14.4 Retrieval

- `Repository_Index.yaml` resolves all current paths;
- archived families point to correct replacements;
- planned documents remain marked planned until created;
- research stubs cannot be retrieved as completed evidence without a warning;
- governance precedence matches the approved baseline.

---

## 15. Threats to Validity

### 15.1 Incomplete Standard

The current standard is not a complete executable conformance specification.
Some ratings therefore identify governance ambiguity rather than document
failure.

### 15.2 Structural Inspection

This report primarily evaluates repository structure and declared document
roles. It does not independently verify research claims or external references.

### 15.3 Maturity Inference

Actual maturity was inferred from document structure and content. Where no
formal status exists, the rating remains an assessment rather than repository
authority.

### 15.4 Scope Boundary

Directories outside the root and `References/` may contain additional
relationship or terminology inconsistencies not captured here.

### 15.5 Repository Evolution

The report represents one commit. Later changes may resolve or introduce
findings. The inspected commit must remain recorded for reproducibility.

---

## 16. Conclusions

The proposed normalization is justified and should precede further substantive
research. However, immediate mass editing would be premature because the
governance baseline still contains unresolved structural decisions.

The next logical action is not to normalize every document directly. It is to
complete a small governance-baseline decision that makes normalization
deterministic.

After that decision, the correct order is:

1. normalize normative governance;
2. normalize core research metadata;
3. normalize substantive reference analyses;
4. classify incomplete reference documents explicitly as research stubs;
5. regenerate repository navigation and the machine index;
6. resume research in Microsoft guidance and architecture evaluation methods.

File size should remain a discovery aid only. Actual content, authority,
dependency role, and maturity should determine normalization priority.

The most important immediate blockers are:

- the missing `Repository_Architecture.md`;
- the incomplete mandatory metadata contract;
- undefined special-artifact profiles;
- filename and relationship-key inconsistencies;
- unclear separation of lifecycle, maturity, quality, and retrieval authority.

Resolving these blockers will allow later normalization to be mechanical,
reviewable, and unlikely to alter research knowledge accidentally.

---

## 17. Findings Register

| ID | Finding | Severity | Recommended phase |
|---|---|---|---|
| GOV-BLOCK-001 | `Repository_Architecture.md` is referenced but missing. | High | Phase 0 |
| GOV-BLOCK-002 | Mandatory metadata contract is incomplete. | High | Phase 0 |
| GOV-BLOCK-003 | Non-Markdown artifact policy is undefined. | Medium | Phase 0 |
| GOV-BLOCK-004 | Editorial guide filename references are case-inconsistent. | Medium | Phase 0–1 |
| GOV-BLOCK-005 | Relationship keys use inconsistent spelling. | Medium | Phase 0–2 |
| GOV-BLOCK-006 | Lifecycle, maturity, quality, and authority overlap. | Medium | Phase 0 |
| ROOT-001 | Several normative root documents lack metadata. | High | Phase 1 |
| ROOT-002 | Core research documents use legacy metadata. | Medium | Phase 2 |
| ROOT-003 | `Repository_Map.md` is not a complete inventory. | Medium | Phase 5 |
| ROOT-004 | `Terminology_Index.md` contains an obsolete IsHandled path. | Medium | Phase 2 |
| REF-001 | Completed ISO and SEI analyses lack metadata. | High | Phase 3 |
| REF-002 | Microsoft extensibility analysis lacks metadata. | High | Phase 3 |
| REF-003 | Canonical IsHandled study uses legacy metadata. | High | Phase 3 |
| REF-004 | Eight reference documents are research stubs without explicit metadata status. | Medium | Phase 4 |
| IDX-001 | Repository index requires regeneration after normalization. | Medium | Phase 5 |

---

## 18. Revision History

### 0.1.0 — 2026-07-17

- Initial structural conformance assessment.
- Covered all active root Markdown documents, `Repository_Index.yaml`, and all
  Markdown documents directly under `References/`.
- Established governance blockers, document matrices, normalization phases,
  commit strategy, validation requirements, and findings register.
