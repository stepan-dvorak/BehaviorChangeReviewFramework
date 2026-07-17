# CONTRIBUTING_FOR_AI.md

> Repository-wide guidance for AI assistants contributing to the
> **Behavior Change Review Framework**.

------------------------------------------------------------------------

# Purpose

This document defines the repository conventions that every AI assistant
should follow when generating, reviewing or updating repository content.

Its goal is to keep the repository internally consistent regardless of
which model, conversation or session is used.

This document is authoritative for repository style and should be
treated as higher priority than conversation-specific preferences unless
explicitly overridden.

------------------------------------------------------------------------

# Repository Mission

The repository investigates **architecturally significant
behavior-changing customizations** in Microsoft Dynamics 365 Business
Central.

The long-term objective is to develop a **mechanism-independent** review
methodology grounded in existing software architecture literature,
international standards and Microsoft guidance.

The repository does **not** attempt to:

-   replace Microsoft Learn,
-   redefine software architecture,
-   invent unnecessary terminology,
-   promote one implementation mechanism,
-   argue against Microsoft guidance.

------------------------------------------------------------------------

# Repository Structure

The repository follows a layered structure.

1.  Project Charter
2.  Research Log
3.  Terminology
4.  Research Methodology
5.  Related Work
6.  International Standards
7.  Microsoft Guidance
8.  Business Central Evidence
9.  Framework
10. Pattern Catalog
11. Example Catalog
12. Decision Tree
13. Whitepaper

Reference documents define terminology and methodology.

Framework documents define practical guidance.

Whitepapers summarize conclusions.

------------------------------------------------------------------------

# Primary Writing Principles

Always:

-   prefer precision over persuasion;
-   prefer evidence over intuition;
-   distinguish facts from interpretation;
-   distinguish Microsoft's guidance from research conclusions;
-   distinguish repository conclusions from hypotheses.

Avoid:

-   marketing language;
-   blog style;
-   unnecessary repetition;
-   exaggerated originality claims;
-   unsupported assumptions.

------------------------------------------------------------------------

# Evidence Hierarchy

Prefer evidence in the following order:

1.  ISO / IEEE standards
2.  Academic literature
3.  SEI and established architecture references
4.  Microsoft Learn
5.  Official AL guidance
6.  Microsoft source code
7.  Community sources
8.  Personal observations

Lower-level evidence must never be presented as stronger than
higher-level evidence.

------------------------------------------------------------------------

# Terminology Rules

Always prefer existing terminology.

Only introduce a repository-specific term when:

-   no suitable established term exists,
-   the distinction is useful,
-   the distinction is supported by evidence,
-   the term remains mechanism-independent.

Candidate terminology must be explicitly identified as a research
concept.

------------------------------------------------------------------------

# Mechanism Independence

The repository is **not about IsHandled**.

IsHandled is treated as one representative case study.

Every conclusion should remain valid for:

-   IsHandled
-   Interfaces
-   Strategy
-   Event Subscribers
-   Delegation
-   Workflow
-   Plugin architectures
-   Future extensibility mechanisms

------------------------------------------------------------------------

# Separation of Evidence Layers

Keep these layers separate.

## Microsoft Guidance

What Microsoft explicitly recommends.

## Empirical Evidence

What is observed in Business Central code.

## Research Interpretation

Repository analysis.

## Conclusions

Only statements supported by available evidence.

Never merge these layers.

------------------------------------------------------------------------

# Consistency Rules

Generated documents should remain consistent with:

-   00_Project_Charter.md
-   00_Research_Log.md
-   01_Terminology.md
-   02_Research_Methodology.md
-   03_Related_Work.md
-   ISO_42010.md
-   ISO_42020.md
-   ISO_42030.md

When conflicts exist, repository reference documents take precedence
over temporary wording from previous conversations.

------------------------------------------------------------------------

# Writing Style

Repository documents are reference documentation.

Write using:

-   concise technical prose;
-   stable terminology;
-   explicit scope boundaries;
-   reusable structure;
-   long-term maintainability.

Avoid:

-   conversational explanations;
-   academic paper formatting;
-   persuasive writing;
-   excessive repetition.

------------------------------------------------------------------------

# Document Evolution

When updating an existing document:

-   preserve the established structure;
-   integrate new material into the existing document;
-   remove duplicated text;
-   harmonize terminology;
-   avoid creating delta documents;
-   avoid creating "next iteration" sections;
-   avoid editorial notes.

If the output limit is reached:

continue the same document in the following response rather than
restarting it.

------------------------------------------------------------------------

# Microsoft Reference Documents

When Microsoft Learn is available:

-   cite representative official guidance;
-   avoid paraphrasing beyond available evidence;
-   distinguish recommendations from repository interpretation.

------------------------------------------------------------------------

# Business Central Examples

Examples should:

-   be reproducible;
-   identify affected mechanisms;
-   identify affected stakeholder concerns;
-   distinguish observation from interpretation;
-   explain architectural implications without overstating conclusions.

------------------------------------------------------------------------

# Repository Philosophy

The repository values negative results.

If existing literature already solves a problem:

record that finding instead of inventing novelty.

The intended contribution is integration, specialization and operational
guidance, not unnecessary invention.

------------------------------------------------------------------------

# Revision History

## 1.0

Initial repository-wide AI contribution guidelines.
