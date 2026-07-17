---
depends-on:
- 00_Research_Log
- 01_Terminology
project: Behavior Change Review Framework
status: draft
version: 0.1
---

# 02_Research_Methodology.md

# Purpose

This document defines the research methodology used throughout the
project.

It intentionally separates:

-   observations,
-   hypotheses,
-   evidence,
-   conclusions.

The objective is to prevent the project from drifting toward unsupported
terminology or assumptions.

------------------------------------------------------------------------

# Research Philosophy

This project is exploratory.

The objective is **not** to prove a predefined idea.

The objective is to determine:

-   whether the observed phenomenon already exists,
-   whether existing terminology is sufficient,
-   whether Business Central lacks practical guidance,
-   whether a genuine contribution can be made.

Negative results are considered valuable outcomes.

------------------------------------------------------------------------

# Research Principles

## 1. Prefer existing terminology

Existing terminology should always be preferred over creating new terms.

New terminology is introduced only when existing literature cannot
adequately describe the observed concept.

------------------------------------------------------------------------

## 2. Separate mechanism from phenomenon

Business Central mechanisms (IsHandled, Interfaces, Events, Workflow...)
are evidence.

They are **not** the research subject.

The research subject is the architectural phenomenon they demonstrate.

------------------------------------------------------------------------

## 3. Separate observation from interpretation

Observation:

> A customization replaced part of the standard posting behavior.

Interpretation:

> The customization changed architectural properties.

Only observations may be treated as facts until supported by evidence.

------------------------------------------------------------------------

## 4. Reject mechanism-specific conclusions

Any proposed principle should remain valid regardless of whether the
implementation uses:

-   IsHandled
-   Interface
-   Event Subscriber
-   Strategy
-   Workflow
-   Delegation
-   Middleware

If a principle depends on one mechanism, it is considered incomplete.

------------------------------------------------------------------------

# Evidence Hierarchy

Highest confidence:

1.  International standards (ISO / IEEE)
2.  Academic literature
3.  SEI and established architecture references
4.  Microsoft Learn
5.  Official AL Guidelines
6.  Base Application and Microsoft code
7.  Community examples
8.  Personal observations

Lower levels may inspire hypotheses but should not establish
terminology.

------------------------------------------------------------------------

# Hypothesis Lifecycle

Every hypothesis follows the same lifecycle.

## Proposed

Initial idea.

## Under Investigation

Evidence is being collected.

## Accepted

Supported by literature and practical evidence.

## Adapted

Accepted after refinement.

## Rejected

Contradicted or unnecessary.

------------------------------------------------------------------------

# Decision Criteria

A concept should only become part of the framework if:

-   it cannot already be expressed by existing terminology,
-   it improves understanding,
-   it applies independently of implementation mechanism,
-   it is supported by practical Business Central examples,
-   it does not contradict established architecture literature.

------------------------------------------------------------------------

# Literature Review Strategy

Every important concept should be investigated in:

-   Software Architecture
-   Microsoft Learn
-   AL Guidelines
-   Framework Design
-   Plugin Architectures
-   Workflow Systems
-   Business Process Management
-   Distributed Systems (where applicable)

Each review should answer:

-   Does the concept already exist?
-   Under which name?
-   Is the meaning identical or only similar?
-   What remains uncovered?

------------------------------------------------------------------------

# Business Central Validation

General architectural conclusions should be validated against real
examples.

Candidate sources include:

-   Base Application
-   System Application
-   Microsoft localizations
-   Open-source AL repositories

Each example should document:

-   implementation mechanism,
-   affected behavior,
-   architectural consequences,
-   applicable review questions.

------------------------------------------------------------------------

# Research Artifacts

This project consists of:

-   Research Log
-   Terminology
-   Methodology
-   Related Work
-   Existing BC Guidance
-   Framework
-   Pattern Catalog
-   Example Catalog
-   Decision Tree
-   Whitepaper

The whitepaper is considered the final synthesis, not the primary
research artifact.

------------------------------------------------------------------------

# Success Criteria

The project is considered successful if it demonstrates one of the
following:

1.  Existing literature already contains the complete solution (valuable
    negative result).

2.  Existing concepts exist but require integration for Business
    Central.

3.  A previously undocumented mechanism-independent review framework can
    be justified.

------------------------------------------------------------------------

# Revision History

## 0.1

Initial research methodology.
