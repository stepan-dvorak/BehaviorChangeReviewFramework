---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: GOV-RSN-001
  title: Reasoning Standard
  type: Governance Standard
  version: 0.2.0
  status: Active

classification:
  domain: Governance
  layer: Repository
  maturity: Review

owner: Štěpán Dvořák

purpose: >
  Defines the normative reasoning principles that govern how conclusions are
  derived from evidence throughout the Orden repository.

quality:
  review: Self Reviewed
  evidence: N/A
  editorial: Reviewed

audience:
  - Human Contributors
  - AI Assistants

depends_on:
  - Repository_Standards.md

related_documents:
  - Contributing_for_AI.md
  - Editorial_Style_Guide.md
  - Repository_Taxonomy.md
  - Evidence_Hierarchy.md

tags:
  - reasoning
  - governance
  - evidence
  - research
---

# Reasoning Standard

## 1. Purpose

This standard defines the repository-wide principles governing
reasoning. It specifies **how conclusions SHALL be derived from
evidence** regardless of whether the contributor is a human reviewer or
an AI assistant.

This standard is normative. Operational workflows are defined separately
in `Contributing_for_AI.md`.

------------------------------------------------------------------------

# 2. Scope

This standard applies to:

-   repository governance;
-   research documents;
-   reference documentation;
-   whitepapers;
-   architectural analyses;
-   editorial reviews.

------------------------------------------------------------------------

# 3. Core Principles

Reasoning SHALL:

-   be evidence-based;
-   be reproducible;
-   be transparent;
-   distinguish fact from interpretation;
-   preserve uncertainty;
-   preserve conflicting evidence until resolved.

Reasoning SHALL NOT:

-   fabricate evidence;
-   hide uncertainty;
-   rely on circular reasoning;
-   present hypotheses as facts;
-   omit contradictory observations without explanation.

------------------------------------------------------------------------

# 4. Reasoning Inputs

Reasoning SHALL operate on a previously established **Knowledge Model**.

The Knowledge Model is constructed from **Knowledge Sources** and SHALL
contain, where applicable:

-   repository governance;
-   established terminology;
-   verified evidence;
-   assumptions;
-   dependencies;
-   unresolved questions;
-   identified uncertainty.

Reasoning SHALL NOT operate directly on isolated Knowledge Sources.

------------------------------------------------------------------------

# 5. Evidence Classification

The following categories SHALL remain distinguishable throughout
reasoning:

-   Fact
-   Observation
-   Interpretation
-   Assumption
-   Hypothesis
-   Conclusion

A conclusion SHALL be traceable to supporting evidence.

------------------------------------------------------------------------

# 6. Uncertainty

Whenever certainty cannot be established, uncertainty SHALL be
classified.

Typical categories include:

-   Missing Evidence
-   Conflicting Evidence
-   Ambiguous Terminology
-   Incomplete Knowledge
-   Open Research Question

Uncertainty SHALL be reported explicitly rather than concealed by
confident language.

------------------------------------------------------------------------

# 7. Hypothesis Formation

Hypotheses MAY be created when available evidence is insufficient.

Each hypothesis SHOULD identify:

-   supporting evidence;
-   contradicting evidence;
-   assumptions;
-   estimated confidence.

Hypotheses SHALL remain distinguishable from validated conclusions.

------------------------------------------------------------------------

# 8. Conclusion Formation

A conclusion SHOULD satisfy all of the following:

-   supported by available evidence;
-   logically consistent;
-   compatible with repository governance;
-   reproducible by an independent reviewer.

If these conditions cannot be met, the remaining limitations SHALL be
reported.

------------------------------------------------------------------------

# 9. Traceability

Every significant conclusion SHOULD be traceable to one or more elements
of the Knowledge Model.

The chain

Evidence → Interpretation → Hypothesis → Conclusion

SHALL remain reconstructable during review.

------------------------------------------------------------------------

# 10. Relationship to Other Standards

This document defines **how reasoning is performed**.

It does not define:

-   repository governance;
-   editorial style;
-   contribution workflow;
-   document taxonomy.

Those responsibilities belong to their respective governance documents.

------------------------------------------------------------------------

# Rationale

Separating reasoning into its own governance standard allows the same
reasoning principles to be reused by AI assistants, human contributors
and future automated validation tools. This avoids duplicating reasoning
rules across multiple operational documents and establishes a single
authoritative source for evidence-based decision making within the Orden
repository.
