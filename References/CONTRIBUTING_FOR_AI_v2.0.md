# CONTRIBUTING_FOR_AI.md

> Repository-wide contribution guide for AI assistants working on the
> **Behavior Change Review Framework**.

Version: **2.0**

------------------------------------------------------------------------

# Purpose

This document defines mandatory repository conventions for every AI
model that contributes to this repository.

Its purpose is to ensure that future conversations produce documents
that remain stylistically, structurally and conceptually consistent
regardless of the model used.

When repository guidance conflicts with temporary conversational
wording, this document takes precedence unless explicitly overridden.

------------------------------------------------------------------------

# Repository Mission

The repository investigates **architecturally significant
behavior-changing customizations** in Microsoft Dynamics 365 Business
Central.

The expected contribution is **not** a new architectural theory.

The expected contribution is a **Business Central specialization** that
integrates:

-   international software architecture standards;
-   Microsoft guidance;
-   empirical evidence from Business Central;
-   practical review guidance.

The repository complements existing guidance rather than replacing it.

------------------------------------------------------------------------

# Repository Philosophy

Always:

-   follow evidence before intuition;
-   prefer integration over invention;
-   value negative results;
-   narrow claims when evidence becomes stronger;
-   refine hypotheses instead of defending them.

Never attempt to manufacture originality.

------------------------------------------------------------------------

# Canonical Reference Order

Repository decisions should be guided in this order:

1.  Project Charter
2.  Research Methodology
3.  Terminology
4.  Related Work
5.  ISO 42010
6.  ISO 42020
7.  ISO 42030
8.  SEI Behavior Documentation
9.  Microsoft Architecture & Extensibility guidance
10. Empirical Business Central evidence
11. Framework documents
12. Whitepaper

Framework documents consume reference material.

Reference documents must not be rewritten to fit later framework ideas.

------------------------------------------------------------------------

# Evidence Hierarchy

Highest confidence:

1.  ISO / IEEE
2.  Academic literature
3.  SEI
4.  Microsoft Learn
5.  Official AL guidance
6.  Microsoft source code
7.  Community sources
8.  Personal observations

Never elevate lower evidence above higher evidence.

------------------------------------------------------------------------

# Separation of Evidence

Always distinguish:

## Microsoft Position

Official recommendations.

## Empirical Evidence

Observed Business Central behaviour.

## Research Interpretation

Repository analysis.

## Conclusions

Statements supported by available evidence.

Do not merge these layers.

------------------------------------------------------------------------

# Mechanism Independence

The repository studies the architectural phenomenon, not one language
feature.

Every conclusion should remain valid for:

-   IsHandled
-   Interfaces
-   Events
-   Strategy
-   Workflow
-   Delegation
-   Plugin architectures
-   Future extensibility mechanisms

IsHandled is a representative case study.

------------------------------------------------------------------------

# Terminology Rules

Prefer established terminology.

Only introduce repository terminology when:

-   no established equivalent exists;
-   it improves precision;
-   it is mechanism-independent;
-   literature has been investigated first.

Candidate terms must remain explicitly identified as research concepts.

------------------------------------------------------------------------

# Required Structure for Reference Documents

Reference documents should normally contain:

-   YAML front matter
-   Purpose
-   Source Status (if applicable)
-   Executive Assessment
-   Core Concepts / Analysis
-   Research Implications
-   Counterarguments or Limitations
-   Findings
-   Impact on Repository
-   Open Questions
-   References
-   Revision History

Not every document requires every section, but this structure is the
default.

------------------------------------------------------------------------

# Writing Style

Reference documents are long-lived technical documentation.

Prefer:

-   concise technical prose;
-   explicit scope;
-   neutral tone;
-   stable terminology;
-   repository-wide consistency.

Avoid:

-   blog style;
-   persuasive writing;
-   unnecessary academic wording;
-   marketing language;
-   conversational explanations.

------------------------------------------------------------------------

# Update Rules

When revising an existing document:

-   integrate changes into the complete document;
-   eliminate duplicated wording;
-   harmonize terminology;
-   preserve document identity;
-   avoid delta files;
-   avoid editorial notes;
-   avoid "next iteration" sections.

If output limits are reached:

continue the same document instead of restarting.

------------------------------------------------------------------------

# Citation Rules

Prefer official Microsoft Learn references.

Use representative Business Central examples.

Do not attribute repository conclusions to Microsoft.

Differentiate:

-   citation,
-   observation,
-   interpretation.

------------------------------------------------------------------------

# Repository Lifecycle

Document maturity:

draft → detailed-draft → review → stable

Hypothesis maturity:

Proposed → Under Investigation → Accepted → Adapted → Rejected

Never silently promote hypotheses.

------------------------------------------------------------------------

# Naming Conventions

Reference notes:

ISO\_*.md SEI\_*.md Microsoft\_\*.md

Core repository:

00\_* 01\_* 02\_\*

Framework outputs:

05\_* 06\_* 07\_* 08\_* Whitepaper.md

Use descriptive names.

------------------------------------------------------------------------

# AI Self-Review Checklist

Before completing work verify:

-   Existing terminology preferred?
-   Evidence layers separated?
-   Microsoft guidance distinguished from interpretation?
-   Mechanism-independent?
-   Repository terminology consistent?
-   Duplicates removed?
-   Unsupported originality avoided?
-   Findings supported?
-   References complete?
-   Style matches repository reference documents?

If any answer is "No", revise before finishing.

------------------------------------------------------------------------

# Long-Term Objective

Every document should strengthen a coherent repository.

The repository should read as though written by one architect over many
years, even when produced by different AI models.

------------------------------------------------------------------------

# Revision History

## 2.0

Expanded into a repository constitution covering writing style,
terminology, evidence hierarchy, document lifecycle, repository
structure, update policy, citation rules and AI self-review.
