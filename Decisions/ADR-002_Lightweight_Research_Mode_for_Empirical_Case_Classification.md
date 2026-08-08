---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: ADR-002
  title: Lightweight Research Mode for Empirical Case Classification
  type: Architecture Decision Record
  version: 1.0.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Stable

owner: Štěpán Dvořák

purpose: >
  Defines a narrowly scoped, temporary, proportional workflow for
  prior-knowledge recording, case selection, and case classification in the
  BCApps Czech Core Localization Event Pilot while preserving the pilot's
  evidence, ordering, traceability, and synthesis requirements.

quality:
  review: Self Reviewed
  evidence: N/A
  editorial: Reviewed

audience:
  - Repository Owner
  - Contributors
  - AI Assistants

depends_on:
  - Governance_Principles.md
  - Contributing_for_AI.md

related_documents:
  - 00_Research_Log.md
  - 02_Research_Methodology.md
  - Decisions/ADR-001_Repository_Artifact_Profiles_and_Metadata.md
  - Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md
  - Empirical/BCApps_CZ_Coarse_Screen_Population_Checkpoint.md
  - Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl

tags:
  - governance
  - architecture-decision
  - research-process
  - empirical-study
  - lightweight-mode
---

# ADR-002: Lightweight Research Mode for Empirical Case Classification

## Status

**Accepted**

Accepted by the repository owner, Štěpán Dvořák, on 2026-07-31, by explicit
conversational directive.

This decision is normative only within the bounded scope defined in Section 5.
It does not amend `Contributing_for_AI.md`, the Executable Artifact Delivery
Gate, the pilot pre-registration, the coarse-screen schema, or any empirical
protocol. It defines a proportional operating mode authorized under Section 2.5
of `Contributing_for_AI.md` for one temporary phase of one pre-registered pilot.

---

## 1. Context

The BCApps Czech Core Localization Event Pilot has completed population-wide
coarse evidence-availability screening. All 448 retained subscriber records are
`Ready for Prior-Knowledge Labeling`, and none remain `Not Screened` (see
`Empirical/BCApps_CZ_Coarse_Screen_Population_Checkpoint.md`).

The pilot pre-registration
(`Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md`) requires the following
remaining operations before framework-relevant findings can be produced:

1. record prior knowledge before selection decisions or outcome evaluation;
2. select and freeze 16 `CZP` cases under the pre-registered bucket and bias
   controls;
3. classify the Behavioral Change Impact Review (BCIR) trigger for each selected
   case; and
4. apply the candidate checklist and record per-case analytical findings.

These operations are evidence-generating content and analytical-judgment work
performed against a validated, schema-stable coarse-screen baseline. They are
not resolver, generator, validator, schema, or protocol changes.

`Contributing_for_AI.md` defines a complete contribution workflow whose stages
remain applicable to repository work. It also defines an Executable Artifact
Delivery Gate in Section 8.7. That gate already applies only to executable or
mechanically applicable delivery artifacts, such as Git patches and scripts; it
does not apply merely because a direct repository commit edits research prose or
manual classifications. This ADR therefore does not waive or narrow Section
8.7. When a Git patch or another mechanically applicable artifact is delivered,
the gate continues to apply to that delivered artifact.

The practical problem is instead proportionality and cadence. Repeating the
complete workflow, document-version maintenance, index maintenance, and
checkpoint ceremony for every individual prior-knowledge or case-classification
entry would fragment one coherent analytical phase and repeatedly re-verify a
stable evidence baseline.

## 2. Problem Statement

Define a bounded, explicit, and reversible workflow profile that permits the
pilot to progress efficiently through prior-knowledge recording, case selection,
trigger classification, and checklist analysis without weakening:

- the pre-registered ordering and selection controls;
- source-evidence traceability;
- separation of observation from interpretation;
- preservation of uncertainty;
- the immutability of completed coarse-screen evidence; or
- the full rigor required for tooling, schemas, governance, delivery artifacts,
  and later synthesis.

## 3. Decision Drivers

1. Preserve forward research momentum toward the first classified cases.
2. Preserve the pre-registered controls against selection and confirmation bias.
3. Keep the completed coarse-screen dataset as an immutable evidence-readiness
   baseline.
4. Use one existing authoritative pilot document rather than introduce a
   parallel classification dataset without demonstrated need.
5. Apply validation and repository maintenance at meaningful checkpoints rather
   than after every individual entry.
6. Keep the reduction explicit, bounded, and reversible in accordance with
   Governance Principles GP-04 and GP-07.
7. Preserve full rigor before any case findings are synthesized into broader
   repository claims.

## 4. Considered Options

### Option A — Apply the complete contribution cycle to every individual entry

Advantages:

- maximal procedural uniformity;
- every small edit receives an independent delivery checkpoint.

Disadvantages:

- fragments one coherent analytical operation into many low-value delivery
  cycles;
- repeatedly re-checks a stable dataset and unchanged tooling chain;
- delays the first test of the pilot's trigger and checklist.

### Option B — Relax the workflow informally

Advantages:

- fastest immediate start;
- no additional governance artifact.

Disadvantages:

- violates GP-04 (Explicit Over Implicit) and GP-07 (Preserve Traceability);
- obscures which safeguards remain mandatory;
- creates an informal precedent that is difficult to delimit or reverse.

### Option C — Define a bounded Lightweight Research Mode

Advantages:

- preserves the pre-registered research controls while reducing only process
  cadence and delivery ceremony;
- keeps the coarse-screen baseline immutable;
- uses the existing pilot selection register and case records as the
  authoritative classification artifact;
- creates one auditable rule set with explicit expiration.

Disadvantages:

- requires an additional ADR and repository-index update;
- checkpoint commits contain more analytical change than single-entry commits.

## 5. Decision

**Option C is adopted.**

### 5.1 Scope — Applies Only To

Lightweight Research Mode applies only to the following activities within the
currently pre-registered BCApps Czech Core Localization Event Pilot:

- recording `prior_known` for a candidate before bucket assignment, `CZP`
  selection, or outcome evaluation;
- documenting inclusion evidence and assigning selected cases to the
  pre-registered selection buckets;
- freezing the 16-case `CZP` selection register;
- recording source observations for selected cases;
- BCIR trigger classification of selected cases;
- event-evidence-dimension assessment;
- checklist analysis and per-case analytical notes; and
- iterative content edits to the selection register and case records in
  `Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md` during this phase.

### 5.2 Authoritative Artifact Boundary

`Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl` remains the immutable,
population-wide evidence-readiness baseline produced by the completed coarse
screen. Lightweight Research Mode does not authorize changes to that file, its
schema, its screening decisions, its evidence-availability values, its strata,
or its protected downstream placeholder fields.

The selection register and per-case records in
`Empirical/BCApps_CZ_Core_Localization_Event_Pilot.md` are the authoritative
repository record for prior knowledge, `CZP` selection, trigger classification,
and checklist analysis during this phase.

A new parallel dataset or schema SHALL NOT be introduced under Lightweight
Research Mode. If a demonstrated need arises for structured classification data,
that need SHALL be handled as a separate schema and tooling change under the
full contribution workflow.

### 5.3 Required Analytical Sequence

For each candidate taken forward toward selection, the following order SHALL be
preserved:

1. identify the candidate from the completed screened population;
2. record `prior_known` as `Yes`, `No`, or `Uncertain` before assigning a bucket,
   selecting a `CZP` case, or evaluating an expected trigger or checklist
   outcome;
3. record the bounded inclusion evidence and any uncertainty;
4. apply the pre-registered bucket, diversity, two-case-per-codeunit, and
   eight-prior-known constraints;
5. assign the case to the least-filled applicable bucket using the fixed
   tie-breakers where candidates are equivalent;
6. freeze the complete 16-case selection register; and
7. only then perform trigger classification and checklist analysis.

A selected case SHALL NOT be replaced because its classification is favorable,
unfavorable, `Not Triggered`, or `Uncertain`. Replacement remains limited to the
reasons already permitted by the pilot pre-registration.

### 5.4 What Is Relaxed

During Lightweight Research Mode:

- the complete sequential contribution workflow need not be repeated for every
  individual prior-knowledge, selection, trigger, or checklist entry;
- one coherent analytical pass may cover a bounded group of candidates or
  cases, followed by one proportional self-review and checkpoint commit;
- double-run byte-identical regeneration evidence is not required for manual
  prose, selection-register, or case-classification edits;
- document-version and `Repository_Index.yaml` maintenance may be batched at
  meaningful checkpoints rather than performed after every individual case;
- a separate delivery package is not required for a direct content commit that
  introduces no executable or mechanically applicable artifact.

### 5.5 What Remains Mandatory

The following requirements are not relaxed:

- the sequence in Section 5.3;
- every selected case SHALL cite the specific source evidence it relies on,
  including repository, file path, and line range where available;
- source observation SHALL remain distinguishable from interpretation in
  accordance with `02_Research_Methodology.md`;
- uncertainty, missing evidence, and conflicting evidence SHALL be recorded
  rather than resolved by assumption;
- the fixed source revision, population, selection buckets, limits, and
  tie-breakers SHALL remain unchanged;
- the completed coarse-screen dataset SHALL remain unchanged;
- Governance Principles GP-05 (Evidence Before Conclusions), GP-06 (Preserve
  Uncertainty), and GP-07 (Preserve Traceability) remain fully in force;
- a proportional self-review SHALL verify ordering, selection constraints,
  citation completeness, observation-versus-interpretation separation, status
  consistency, and absence of changes to the coarse-screen baseline;
- the repository owner retains final authority and SHALL accept the frozen
  selection register before full case classification proceeds;
- the repository owner SHALL review the completed case-classification set before
  its findings are cited outside the pilot document.

### 5.6 Full Workflow Still Required

The full applicable `Contributing_for_AI.md` workflow remains mandatory for:

- changes to scripts, schemas, protocols, resolvers, generators, or validators;
- changes to the coarse-screen or subscriber-context datasets or their
  governing documents;
- creation of a new structured classification dataset;
- governance documents, ADRs, and `Repository_Index.yaml` when those artifacts
  are updated at a checkpoint;
- the Whitepaper and any future Framework, Pattern Catalog, or Decision Tree
  deliverable; and
- every delivered Git patch, application wrapper, script, or other executable
  or mechanically applicable artifact, which remains subject to Section 8.7.

## 6. Checkpoints and Validation

Lightweight Research Mode replaces per-entry delivery ceremony with two
mandatory content checkpoints:

1. **Selection checkpoint:** the 16-case register is complete, all
   `prior_known` values were recorded in the required order, all selection
   constraints pass, and the repository owner accepts the frozen register.
2. **Classification checkpoint:** all selected cases have complete evidence,
   trigger, event-dimension, checklist, uncertainty, and limitation records, and
   the repository owner reviews the complete set before synthesis.

Additional intermediate commits are permitted when they preserve a coherent
state. They do not create additional methodological gates unless the owner
explicitly designates one.

At each checkpoint, validation SHALL be proportional to the content change and
SHALL include at least:

- Markdown and metadata conformance for the modified governed document;
- selection-register completeness and constraint checks where applicable;
- source-citation and line-range review;
- observation-versus-interpretation review;
- uncertainty and status consistency review;
- confirmation that the coarse-screen JSON Lines file is unchanged; and
- repository diff hygiene.

If delivery is made through a Git patch or another mechanically applicable
artifact, Section 8.7 validation applies in addition to these content checks.

## 7. Consequences

Positive consequences:

- the pilot can advance through one coherent selection and classification phase
  without repeated low-value delivery cycles;
- prior knowledge remains temporally separated from bucket assignment and
  outcome evaluation;
- the completed coarse-screen evidence remains immutable;
- authoritative classification content remains in the pilot document already
  pre-registered for that purpose;
- full rigor resumes before broader research claims are produced.

Negative consequences:

- individual entries may not each correspond to a standalone repository commit;
- checkpoint reviews must inspect a larger coherent change set;
- the pilot document temporarily carries both its pre-registration and its
  accumulating empirical results, requiring careful preservation of the fixed
  protocol sections.

## 8. Expiration and Reopening Criteria

Lightweight Research Mode applies only to prior-knowledge recording, selection,
and case classification for the currently pre-registered BCApps Czech Core
Localization Event Pilot.

It expires automatically after the classification checkpoint is accepted and
before findings from the classified cases are synthesized into
`00_Research_Log.md`, the Whitepaper, or any other framework-level or normative
deliverable. The Research Log entry that records adoption of this ADR is a
governance-history entry and does not itself trigger expiration.

After expiration, the normal contribution workflow applies without further
action to synthesis, terminology changes, framework claims, and deliverable
updates.

This mode MAY be extended to a future comparable empirical pilot only through an
explicit new or amended ADR. It SHALL NOT be invoked by informal precedent.

## 9. Rationale

The integrity of prior-knowledge labeling and case classification depends
primarily on temporal ordering, direct evidence, transparent uncertainty,
selection discipline, and independent owner review. Mechanical delivery
verification protects a different concern: whether an executable or applicable
artifact works against its intended baseline.

This decision keeps both protections in their proper scope. It reduces only the
cadence and ceremony of content-authoring work, leaves Section 8.7 unchanged,
preserves the completed coarse-screen evidence, and restores the complete
repository workflow before any pilot findings become broader claims.
