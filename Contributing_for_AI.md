---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: CG-001
  title: AI Contribution Guidelines
  type: Contribution Guide
  version: 0.3.1
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

quality:
  review: Self Reviewed
  evidence: N/A
  editorial: Reviewed

purpose: >
  Defines the operational workflow that AI assistants SHALL follow when
  contributing to the Orden repository.

audience:
  - AI Assistants

depends_on:
  - Repository_Standards.md
  - Reasoning_Standard.md
  - Governance_Principles.md

related_documents:
  - Repository_Taxonomy.md
  - Editorial_Style_Guide.md
  - AGENTS.md

tags:
  - governance
  - ai
  - workflow
  - contribution
---

# AI Contribution Guidelines

## Preamble

The **Orden** repository is governed by a collection of documents that define
its architecture, terminology, editorial standards and research methodology.

Those documents establish **what** the repository is and **which rules apply**.

This document serves a different purpose.

It defines **how an AI assistant SHALL operate** within that governance
framework.

Rather than introducing additional repository rules, this document specifies
the operational workflow by which AI assistants interpret repository
governance, resolve applicable standards, perform research, produce
contributions and validate their own work before delivery.

It therefore complements, rather than replaces, the repository governance
documents.

---

# Purpose

The purpose of this document is to establish a consistent operational model for
AI-assisted contributions throughout the Orden repository.

Every AI assistant contributing to the repository SHALL follow the workflow
defined herein regardless of the model, provider or execution environment.

The objective is to ensure that repository contributions remain technically
consistent, reproducible and maintainable over time.

This document intentionally focuses on **process**.

Repository policies, terminology, editorial conventions and architectural
principles are defined elsewhere and SHALL be referenced rather than duplicated.

---

## Scope

This document applies to all AI-assisted creation, modification and review of
repository artifacts.

# AI Contribution Workflow

## Part I — Thinking

1. AI Role
2. Decision Hierarchy
3. Operational Workflow
4. Execution Context Resolution
5. Knowledge Model Construction
6. Reasoning

## Part II — Execution

7. Artifact Realization
8. Validation
9. Delivery
10. Governance Evolution

Workflow

Task
 |
 v
Execution Context Resolution
 |
 v
Knowledge Sources
 |
 v
Knowledge Model
 |
 v
Reasoning
 |
 v
Artifact Realization
 |
 v
Validation
 |
 v
Delivery
 |
 v
Governance Evolution

# 1. AI Role

An AI assistant acts as a repository contributor.

Its responsibility is to assist the human maintainer in researching,
organizing, analysing and documenting knowledge contained within the
repository.

The AI contributes content but does not own the repository.

Final authority always remains with the human maintainer.

Accordingly, the AI SHALL:

- interpret repository governance before beginning work;
- preserve repository consistency;
- distinguish evidence from interpretation;
- operate transparently;
- avoid unsupported assumptions.

The AI SHALL NOT:

- redefine repository philosophy;
- silently alter established terminology;
- fabricate evidence;
- override repository governance;
- replace human review.

# 2. Decision Hierarchy

## 2.1 Purpose

An AI assistant operates within a governed repository rather than an isolated
conversation.

Every contribution SHALL therefore be based on repository governance before
task-specific instructions or conversational context.

Whenever multiple instructions apply simultaneously, the AI SHALL resolve them
according to the hierarchy defined in this chapter.

This hierarchy ensures repository-wide consistency while allowing individual
documents and conversations to introduce additional requirements where
appropriate.

---

## 2.2 Governance Hierarchy

Unless explicitly instructed otherwise by the repository owner, applicable
guidance SHALL be interpreted in the following order of precedence:

Priority:

1. Governance_Principles.md
2. Repository_Standards.md
3. Repository_Taxonomy.md
4. Editorial_Style_Guide.md
5. Reasoning_Standard.md
6. Document-specific guidance
7. Current task instructions

Higher-level governance documents SHALL always take precedence over lower-level
documents.

Lower-level documents MAY refine higher-level guidance but SHALL NOT contradict
it.

---

## 2.3 Conflict Resolution

When two or more instructions appear to conflict, the AI SHALL attempt to
resolve the conflict using the established governance hierarchy.

Conflicts SHALL NOT be resolved by averaging, combining or selectively applying
rules from multiple sources.

Instead, the AI SHALL determine which document has higher authority and follow
that document.

Whenever the conflict cannot be resolved unambiguously, the AI SHALL stop the
decision process and request clarification from the repository owner.

The AI SHALL NOT silently choose an interpretation.

---

## 2.4 Repository Consistency

Repository consistency SHALL take precedence over local optimization.

An individual document SHALL NOT introduce terminology, document structures or
editorial conventions that reduce consistency across the repository unless such
changes are explicitly approved.

Whenever repository-wide consistency conflicts with local stylistic preference,
repository consistency SHALL prevail.

---

## 2.5 Human Authority

The repository owner remains the final authority for every repository decision.

AI assistants support repository development but do not establish repository
policy.

Explicit instructions from the repository owner MAY override repository
governance when the purpose is to intentionally evolve repository standards.

Such changes SHOULD subsequently be reflected within the corresponding
governance documents to preserve long-term consistency.


# 3. Operational Workflow

## 3.1 Purpose

This chapter defines the operational lifecycle that every AI assistant SHALL
follow when contributing to the repository.

The workflow establishes a consistent sequence of activities from receiving a
task to delivering the final result.

Each stage produces information required by subsequent stages.

Stages SHALL NOT be skipped unless explicitly authorized by the repository
owner.

---

## 3.2 Workflow Overview

Thinking SHALL complete before execution.
Validation SHALL precede delivery.
Every contribution SHALL progress through the following operational states:

1. Task Received
2. Context Resolved
3. Governance Resolved
4. Research Completed
5. Reasoning Completed
6. Document Authored
7. Self Review Completed
8. Ready for Delivery

Progression through these states SHALL be sequential.

The output of each state becomes the input for the following state.

---

## 3.3 State Transition Principles

The AI SHALL complete the objectives of the current state before advancing to
the next one.

If required information is unavailable, the AI SHALL remain in the current
state until the missing information has been obtained or clarification has been
requested.

The AI SHALL NOT bypass intermediate states by making unsupported assumptions.

---

## 3.4 State Ownership

Each operational state has a single responsibility.

No state SHALL duplicate responsibilities assigned to another state.

This separation ensures that repository governance, research, reasoning,
authoring and validation remain independent activities.

---

## 3.5 Exceptional Flow

Normal workflow assumes sufficient repository context and unambiguous
instructions.

Whenever ambiguity prevents further progress, the AI SHALL suspend workflow
execution and request clarification.

The AI SHALL NOT substitute assumptions for missing repository governance.

After clarification has been obtained, workflow SHALL continue from the last
completed state rather than restarting from the beginning.

# 4. Execution Context Resolution

## 4.1 Purpose

Before beginning research, analysis or authoring, the AI SHALL establish an
execution context for the current task.

The execution context defines the repository environment in which the task is
performed and determines which repository standards, methodologies and
constraints apply.

No subsequent workflow state SHALL begin before the execution context has been
resolved.

---

## 4.2 Required Context

The AI SHALL determine, at minimum, the following characteristics of the
current task:

- repository project;
- document identity;
- document classification;
- repository layer;
- operating mode;
- applicable governance documents;
- applicable research methodology;
- intended audience;
- expected output artifact.

If any required context cannot be determined with reasonable confidence, the AI
SHALL request clarification before continuing.

---

## 4.3 Document Classification

The AI SHALL identify whether the task concerns:

- creation of a new document;
- revision of an existing document;
- repository governance;
- reference documentation;
- research documentation;
- publication material;
- repository maintenance.

Different document categories MAY require different governance documents,
editorial conventions and validation procedures.

---

## 4.4 Operating Mode

Based on the resolved context, the AI SHALL determine the primary operating
mode.

Typical operating modes include:

- Governance
- Research
- Reference
- Editorial
- Publication
- Maintenance

An operating mode determines which repository standards are applicable during
subsequent workflow stages.

---

## 4.5 Governance Resolution

After determining the operating mode, the AI SHALL identify all repository
governance documents applicable to the current task.

Applicable governance SHALL be resolved according to the Decision Hierarchy
defined in Chapter 2.

The AI SHALL apply repository governance before interpreting document-specific
requirements.

---

## 4.6 Context Validation

Before entering the Research state, the AI SHALL verify that the execution
context is internally consistent.

Validation SHOULD confirm that:

- document classification matches repository taxonomy;
- operating mode matches document purpose;
- applicable governance has been identified;
- repository terminology has been resolved;
- required dependencies have been identified.

Any unresolved inconsistency SHALL suspend workflow execution until clarified.

---

## 4.7 Execution Environment Failure Scope

A failure observed within one tool, container, process, virtual environment, connector, or network namespace SHALL initially be treated as a limitation of that execution path only.

The AI SHALL NOT infer that an external resource, repository, service, host, file, or capability is globally unavailable solely because one execution environment cannot access it.

Before declaring a required resource unavailable, the AI SHALL evaluate other available execution paths, including where applicable:

- repository connectors;
    
- provider APIs;
    
- alternate network-enabled tools;
    
- previously retrieved authoritative content;
    
- repository blobs or file-fetch operations;
    
- host-side tools;
    
- local reconstruction from verified source objects;
    
- deterministic generation executed within the repository owner's checkout.
    

For example, a DNS or network failure reported by an isolated container establishes only that the container could not reach the resource. It does not establish that the resource is unavailable through the wider tool environment.

### 4.7.1 Fallback Obligation

When the preferred execution path fails, the AI SHALL:

1. identify the scope of the observed failure;
    
2. inventory materially different available access paths;
    
3. select the path that can still produce verifiable evidence;
    
4. continue the task through that path when feasible.
    

The AI SHALL stop only when all materially relevant available paths have been exhausted or when proceeding would require unsupported assumptions.

### 4.7.2 Reporting

Environment limitations SHALL be reported precisely.

Preferred form:

> The current container cannot resolve github.com.

Prohibited escalation without further evidence:

> GitHub is unavailable.

The AI SHALL distinguish:

- resource unavailability;
    
- connector unavailability;
    
- container network isolation;
    
- missing credentials;
    
- unsupported tool operations;
    
- incomplete local checkout;
    
- failure of one specific command.
    

A local execution failure SHALL NOT be used to lower the validation standard.

---

## Rationale

Repository tasks often appear similar while requiring different governance,
different methodologies and different editorial standards.

Resolving the execution context before beginning substantive work minimizes
incorrect assumptions, reduces inconsistency across documents and improves the
reproducibility of AI-assisted contributions.

For this reason, execution context resolution is treated as an independent
workflow state rather than an implicit preparation step.

# 5. Knowledge Model Construction

## 5.1 Purpose

Before performing reasoning or authoring activities, the AI SHALL construct a
Knowledge Model representing the information required to complete the current
task.

The Knowledge Model is a structured internal representation derived from
relevant Knowledge Sources.

Reasoning SHALL operate on the Knowledge Model rather than directly on
individual documents.

---

## 5.2 Knowledge Sources

Knowledge Sources represent authoritative inputs available to the AI.

Depending on the execution context, Knowledge Sources MAY include:

- repository governance documents;
- repository documentation;
- repository terminology;
- research documents;
- architecture documents;
- external standards;
- Microsoft Learn documentation;
- academic literature;
- empirical observations;
- validated evidence.

Knowledge Sources SHALL remain distinguishable throughout the workflow.

---

## 5.3 Knowledge Model

The AI SHALL integrate information obtained from Knowledge Sources into a
single coherent Knowledge Model.

The Knowledge Model SHOULD contain:

- applicable governance;
- repository terminology;
- established facts;
- relevant evidence;
- known assumptions;
- identified uncertainties;
- dependencies;
- unresolved questions.

The Knowledge Model SHALL preserve the provenance of significant information
whenever practical.

---

## 5.4 Source Evaluation

The AI SHALL evaluate Knowledge Sources according to their authority,
relevance and reliability.

Higher-authority sources SHALL take precedence over lower-authority sources.

Conflicting information SHALL remain explicitly represented within the
Knowledge Model until resolved.

The AI SHALL distinguish:

- facts;
- observations;
- interpretations;
- hypotheses;
- assumptions.

---

## 5.5 Knowledge Sufficiency

The AI SHALL determine whether the Knowledge Model is sufficient to support the
requested task.

If significant uncertainty remains, the AI SHALL either:

- continue gathering Knowledge Sources, or
- request clarification.

The AI SHALL NOT replace missing knowledge with unsupported assumptions.

---

## Rationale

Separating Knowledge Sources from the Knowledge Model distinguishes information
collection from information organization.

This enables subsequent reasoning to operate on a coherent representation of
the problem rather than repeatedly interpreting individual documents.

The resulting workflow improves consistency, traceability and reproducibility
throughout repository contributions.

# 6. Reasoning

## 6.1 Purpose

The purpose of this stage is to transform the established Knowledge Model into
a contribution-ready understanding of the current task.

Reasoning SHALL be performed in accordance with
`Reasoning_Standard.md`.

This document defines when reasoning is performed within the repository
workflow but does not define the reasoning methodology itself.

---

## 6.2 Preconditions

Reasoning SHALL begin only after all of the following conditions have been
satisfied:

- the Execution Context has been resolved;
- the applicable repository governance has been identified;
- the Knowledge Model has been established;
- significant knowledge gaps have been addressed or explicitly documented.

If these conditions are not met, workflow SHALL return to the appropriate
previous stage.

---

## 6.3 Workflow Responsibility

During this stage the AI SHALL:

- apply the repository Reasoning Standard;
- preserve repository governance;
- maintain evidence traceability;
- identify remaining uncertainty;
- prepare information for authoring.

The AI SHALL NOT redefine repository governance during reasoning.

---

## 6.4 Outputs

Successful completion of the Reasoning stage SHALL produce:

- validated understanding of the task;
- identified conclusions;
- unresolved questions;
- documented assumptions;
- authoring-ready information.

These outputs become the input for the Authoring stage.

---

## Rationale

Separating reasoning methodology into an independent governance document
ensures that repository reasoning principles remain reusable across AI
assistants, human contributors and future automated validation systems.

This document therefore references the Reasoning Standard instead of
duplicating its contents.


# 7. Artifact Realization

## 7.1 Purpose

The purpose of this stage is to transform the validated reasoning outcome into
a repository artifact that complies with repository governance.

Artifact realization is an implementation activity.

Architectural decisions, reasoning and evidence evaluation SHALL already have
been completed before entering this stage.

---

## 7.2 Inputs

Artifact Realization SHALL operate on the outputs produced by previous workflow
stages.

Typical inputs include:

- Execution Context;
- applicable repository governance;
- Knowledge Model;
- Reasoning outcome;
- document-specific requirements.

This stage SHALL NOT introduce new architectural decisions unless explicitly
requested by the repository owner.

---

## 7.3 Artifact Integrity

The resulting artifact SHALL preserve:

- repository terminology;
- repository metadata;
- document identity;
- established conclusions;
- evidence references;
- governance consistency.

The AI SHALL NOT modify established conclusions during artifact realization.

---

## 7.4 Repository Consistency

Every artifact SHALL remain consistent with the repository as a whole.

The AI SHALL preserve:

- approved terminology;
- document taxonomy;
- metadata conventions;
- editorial conventions;
- repository architecture.

Local improvements SHALL NOT reduce repository-wide consistency.

---

## 7.5 Metadata

Repository metadata SHALL be preserved throughout artifact realization.

Required metadata SHALL remain:

- complete;
- internally consistent;
- compatible with Repository Standards;
- appropriate for the document classification.

Metadata SHALL NOT be silently removed or restructured.

---

## 7.6 Traceability

Whenever repository conclusions depend upon external evidence,
the resulting artifact SHOULD preserve traceability.

Traceability MAY include:

- citations;
- repository references;
- document dependencies;
- cross references;
- rationale references.

The AI SHALL preserve meaningful relationships between repository artifacts
whenever practical.

---

## 7.7 Completeness

Before artifact realization is considered complete, the AI SHALL verify that
the resulting artifact:

- satisfies the requested scope;
- preserves repository governance;
- contains no unresolved placeholders;
- contains no duplicated sections;
- maintains internal consistency;
- is suitable for repository review.

Partial artifacts SHALL be produced only when explicitly requested.

---
## 7.8 Repository Patch Realization

When repository changes are delivered as a Git patch, the AI SHALL prefer the
following realization workflow:

1. obtain the current authoritative repository state;
2. perform the requested edits against that state;
3. run the applicable focused validations;
4. let Git generate the patch from the actual working-tree or index difference;
5. restore or create a clean copy of the intended target baseline;
6. verify the exact generated patch against that baseline;
7. deliver the verified patch together with the application wrapper and delivery
   evidence.

The preferred patch-generation command is:

```text
git diff --binary > <patch-file>
```

or, when the intended change is staged:

```text
git diff --cached --binary > <patch-file>
```

The patch SHALL be generated from an actual Git difference. It SHALL NOT be  
constructed manually from remembered source fragments, reconstructed hunks, or  
partial excerpts unless the repository owner explicitly requests diagnostic  
patch repair.

The preferred workflow SHALL always be the simplest workflow that provides the required evidence. Additional defensive mechanisms SHALL only be introduced when they solve a demonstrated problem that cannot be addressed within the simpler workflow.

### 7.8.1 Preferred Simplicity

The default workflow SHALL remain as simple as the task permits.

Additional mechanisms such as transformation generators, three-way application,  
file fingerprints, embedded source copies, or baseline reconstruction SHALL be  
used only when the normal repository-diff workflow cannot be executed.

Fallback mechanisms SHALL NOT replace the preferred workflow merely because they  
appear more defensive.

### 7.8.2 Failed-Patch Recovery

When a generated patch fails structural application against its intended  
baseline, the AI SHALL return to the authoritative repository state and  
regenerate the patch from an actual Git diff.

The AI SHALL NOT repeatedly modify patch hunks, remove context, relax whitespace  
matching, or add application flags in an attempt to make an incorrectly  
generated patch appear applicable.

### 7.8.3 Text-File Fingerprints and Line Endings

Working-copy byte hashes SHALL NOT be used as a default prerequisite for
applying Git patches to repository text files.

Text-file bytes may differ between execution environments because of Git line
ending conversion, `.gitattributes`, editor behavior, byte-order marks, or final
newline normalization.

For ordinary repository patch delivery, baseline identity SHALL be established
primarily through:

- the target branch and commit;
- a clean Git working tree;
- the actual Git-generated diff;
- successful `git apply --check`.

When object-level identity is required, the AI SHOULD use Git object identity
such as:

```text
git rev-parse HEAD:<path>
```

rather than hashing the checked-out working-tree bytes.

Working-copy fingerprints MAY be used only when byte-for-byte identity is an  
explicit requirement and line-ending behavior has been defined and validated.

---

## Rationale

Separating artifact realization from reasoning ensures that implementation
activities do not alter previously validated conclusions.

This distinction improves reproducibility, simplifies review and establishes a
clear boundary between intellectual work and artifact production.Transform validated reasoning into repository artifacts.

No new architectural decisions SHALL be introduced.

# 8. Validation

## 8.1 Purpose

The purpose of the Validation stage is to determine whether the completed
repository artifact satisfies all applicable governance, quality and
consistency requirements before delivery.

Validation represents the final quality gate prior to repository submission.

No repository artifact SHALL be delivered without completing validation unless
explicitly requested by the repository owner.

---

## 8.2 Validation Scope

Validation SHALL evaluate the artifact against all applicable requirements.

These MAY include:

- Repository Standards;
- Editorial Style Guide;
- Repository Taxonomy;
- Reasoning Standard;
- document-specific requirements;
- repository architecture.

Validation SHALL be proportional to the scope of the artifact.

---

## 8.3 Validation Categories

The AI SHALL verify, where applicable:

### Governance Validation

- repository policies followed;
- applicable standards respected;
- document classification correct.

### Structural Validation

- document organization;
- section hierarchy;
- metadata completeness;
- internal references.

### Editorial Validation

- terminology consistency;
- writing quality;
- formatting consistency;
- repository conventions.

### Technical Validation

- factual consistency;
- citation integrity;
- reference validity;
- dependency consistency.

---

## 8.4 Self Review

The AI SHALL perform an independent self-review before delivery.

The self-review SHALL verify that:

- no contradictory conclusions remain;
- no duplicated content remains;
- no placeholder content remains;
- unresolved uncertainty is identified;
- repository consistency has been preserved.

Self-review SHALL be performed independently of the authoring process.

---

## 8.5 Validation Outcome

Validation SHALL result in one of the following outcomes:

### Accepted

The artifact satisfies repository requirements.

### Accepted with Limitations

Minor issues remain but do not materially reduce repository quality.

Remaining limitations SHALL be explicitly documented.

### Revision Required

The artifact requires additional work before delivery.

Workflow SHALL return to the appropriate previous stage.

---

## 8.6 Validation Independence

Validation SHALL evaluate the completed artifact rather than defend previous
reasoning.

The AI SHALL be willing to reject its own previous work whenever validation
reveals deficiencies.

Validation SHALL prioritize repository quality over completion speed.

---
## 8.7 Executable Artifact Delivery Gate

This section applies to executable or mechanically applicable delivery artifacts, including:

* Git patches;
* shell, batch, or PowerShell application scripts;
* migration scripts;
* repository transformation scripts;
* generated data-repair scripts;
* commands represented as ready-to-run repository procedures.

Such an artifact SHALL NOT be described as verified, applicable, ready, safe to apply, or successfully tested unless the exact delivered artifact has passed the applicable execution gate against the exact intended repository state.

### 8.7.1 Required Evidence

For a Git patch, the minimum application evidence is a successful execution of:

```text
git apply --check <delivered-patch>
```

against the intended clean repository baseline.

When the delivery includes an application wrapper, the wrapper and the exact patch it references SHALL be tested together whenever the execution environment permits.

Syntax validation, patch statistics, manual inspection, inferred applicability, matching line numbers, matching file hashes, or successful application of a different intermediate artifact SHALL NOT be represented as evidence that the delivered patch applies.

### 8.7.2 Exact-Artifact Requirement

Validation SHALL apply to the exact bytes delivered to the repository owner.

An artifact SHALL be revalidated after any modification, including:

* line-ending conversion;
* whitespace normalization;
* hunk reconstruction;
* context-line changes;
* filename changes;
* wrapper-script changes;
* regeneration or re-export.

Validation of a source representation, intermediate patch, transformed patch, or logically equivalent artifact SHALL NOT be transferred to the delivered artifact.

### 8.7.3 Baseline Requirement

The validation baseline SHALL be identified explicitly.

For repository changes, the baseline SHOULD be the current clean target branch after an explicit update from its configured remote.

When the current baseline cannot be reproduced, the AI SHALL state that applicability has not been verified. It SHALL NOT replace missing execution evidence with reasoning or confidence language.

### 8.7.4 Failure Policy

A patch that fails structural application against the intended baseline SHALL be rejected as a delivery candidate.

After the first structural application failure, the AI SHALL return to the authoritative source files and regenerate the patch from an actual repository diff.

The AI SHALL NOT continue repairing or weakening the same patch through speculative hunk edits, zero-context conversion, whitespace relaxation, recounting, or three-way application unless the repository owner explicitly requests diagnostic recovery of that specific patch.

### 8.7.5 Delivery Language

The following statements require successful execution evidence:

* verified;
* applies cleanly;
* tested against current main;
* ready to apply;
* safe to run;
* validated end to end.

When the required evidence is unavailable, the AI SHALL use explicit limitation language, such as:

> The artifact has been generated but its application has not been executed against the target repository baseline.

The AI SHALL NOT use reassuring or predictive language as a substitute for evidence.

---

## Rationale

Separating validation from artifact realization establishes an independent
quality assurance stage.

This separation reduces confirmation bias, improves repository consistency and
encourages objective assessment of completed work before publication.Verify governance, structural, editorial and technical consistency.


# 9. Delivery

## 9.1 Purpose

The purpose of the Delivery stage is to present the completed repository
artifact in a form suitable for its intended audience and delivery channel.

Delivery SHALL preserve the integrity of the validated artifact.

No additional reasoning or architectural decisions SHALL occur during
delivery.

---

## 9.2 Delivery Inputs

Delivery SHALL operate only on artifacts that have successfully completed the
Validation stage.

The delivered artifact SHALL preserve:

- validated conclusions;
- repository metadata;
- document identity;
- repository terminology;
- evidence traceability.

---

## 9.3 Delivery Principles

During delivery the AI SHALL:

- preserve artifact integrity;
- avoid introducing undocumented changes;
- clearly communicate known limitations;
- preserve repository consistency.

The AI SHALL NOT:

- modify validated conclusions;
- silently restructure the artifact;
- introduce additional assumptions;
- remove identified uncertainty.

---

## 9.4 Delivery Completeness

Unless explicitly requested otherwise, delivered repository artifacts SHOULD
be complete.

Complete artifacts SHOULD include:

- required metadata;
- complete document structure;
- referenced dependencies;
- repository cross references;
- appropriate revision information.

Incremental or partial artifacts SHALL be produced only when explicitly
requested.

---

## 9.5 Communication

The AI SHOULD accompany each delivered artifact with a concise summary of:

- completed work;
- significant changes;
- remaining limitations;
- recommended next steps.

Communication SHALL distinguish between:

- completed work;
- future recommendations;
- optional improvements.

---

## 9.6 Repository Delivery Package 

Whenever repository modifications are delivered for external application, the
AI SHALL deliver a Repository Delivery Package.

Unless explicitly agreed otherwise, the package SHALL contain:

- a Git patch;
- an application wrapper (for example BAT or PowerShell);
- a review document describing the change;
- a Delivery Evidence declaration.

Each component serves an independent purpose.

Omitting one component SHALL require explicit agreement from the repository
owner.

### 9.6.1 Review Document

The review document SHALL summarize:

- objective
- motivation
- implementation overview
- affected files
- validation performed
- compatibility considerations
- remaining limitations
- recommended reviewer focus

## 9.7 Delivery Evidence Declaration

Every delivery containing an executable or mechanically applicable repository
artifact SHALL include a concise Delivery Evidence declaration.

The declaration SHALL identify:

- the intended repository baseline;
- the exact delivered artifact;
- the application validation performed;
- the focused tests performed;
- the repository validations performed;
- any validation that could not be performed.

For a Git patch, the declaration SHOULD use the following form:

```text
Delivery evidence:
- Baseline: <branch and commit>
- Artifact: <exact delivered filename>
- Patch application check: PASS | NOT RUN | FAIL
- Focused tests: <commands or summarized result>
- Repository validation: <commands or summarized result>
- Limitations: None | <explicit limitation>
```

A PASS result SHALL be reported only when the stated command was executed
successfully against the stated baseline and exact delivered artifact.

The declaration SHALL distinguish executed evidence from inferred confidence.

Statements such as "should apply", "appears correct", "syntactically valid", or
"expected to pass" SHALL NOT be reported as validation evidence.

---

## 9.8 Delivery Outcome

Successful delivery concludes the operational workflow.

Subsequent modifications SHALL initiate a new workflow beginning with
Execution Context Resolution.

Previously completed workflow states SHALL NOT be assumed to remain valid if
the task scope has materially changed.

---

## Rationale

Delivery represents the transfer of a validated repository artifact rather than
the continuation of reasoning or implementation.

Separating delivery from validation preserves the integrity of reviewed
artifacts and ensures that repository outputs remain stable once they have
passed quality assurance.

# 10. Governance Evolution

## 10.1 Purpose

The purpose of Governance Evolution is to ensure that repository governance
continues to improve while preserving long-term consistency, maintainability
and architectural integrity.

Repository governance SHALL evolve deliberately rather than through
incremental, undocumented change.

---

## 10.2 Evolution Principles

Repository governance SHALL evolve according to observed repository needs.

Evolution SHOULD:

- improve clarity;
- reduce duplication;
- simplify governance;
- increase consistency;
- improve maintainability.

Governance SHALL NOT evolve solely for stylistic preference.

---

## 10.3 Identifying Improvement Opportunities

The AI SHOULD identify opportunities for governance improvement whenever
repeated patterns are observed.

Examples include:

- duplicated repository rules;
- recurring terminology;
- repeated validation procedures;
- recurring reasoning patterns;
- reusable workflow components.

Observed patterns SHOULD be reported as recommendations rather than
implemented automatically.

---

## 10.4 Separation of Responsibilities

Whenever recurring responsibilities emerge within operational documents, the
AI SHOULD recommend extracting them into independent governance standards.

Potential candidates MAY include:

- reasoning;
- validation;
- terminology;
- metadata;
- evidence management.

Repository governance SHOULD remain modular.

---

## 10.5 Governance Refactoring

Repository governance MAY be reorganized to improve maintainability.

Typical governance refactoring includes:

- removing duplicated requirements;
- consolidating related guidance;
- separating independent responsibilities;
- simplifying document dependencies.

Governance refactoring SHALL preserve repository meaning.

Refactoring SHALL NOT silently modify repository policy.

---

## 10.6 Backward Consistency

Governance evolution SHOULD preserve compatibility with existing repository
documents whenever practical.

Whenever incompatible governance changes become necessary, the AI SHALL
identify:

- affected documents;
- affected standards;
- required repository updates;
- expected consequences.

Breaking governance changes SHALL be explicit.

---

## 10.7 Human Authority

Only the repository owner may approve governance evolution.

The AI MAY recommend:

- new governance documents;
- governance refactoring;
- repository restructuring;
- workflow improvements.

The AI SHALL NOT introduce governance changes autonomously.

---

## Rationale

Repository governance represents a long-term architectural asset.

Treating governance as an evolving system encourages continuous refinement
while preventing uncontrolled growth of duplicated rules and inconsistent
practices.

Separating governance evolution from operational workflow ensures that the
repository improves intentionally rather than accidentally.

# References

- Governance_Principles.md
- Repository_Standards.md
- Repository_Taxonomy.md
- Editorial_Style_Guide.md
- Reasoning_Standard.md
