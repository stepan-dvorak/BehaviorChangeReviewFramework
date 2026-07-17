---
project: Behavior Change Review Framework
status: draft
version: 0.1
---

# Research_Log.md

# Purpose

This document is the research backbone of the project. It records
hypotheses, rejected ideas, terminology decisions and open questions. It
is intended for Obsidian and is **not** part of the final whitepaper.

# Principles

-   Record hypotheses before accepting them.
-   Record why hypotheses were rejected.
-   Distinguish observations from conclusions.
-   Separate Business Central observations from general software
    architecture.
-   Reuse existing terminology whenever possible.

# Research Goals

1.  Determine whether a mechanism-independent review methodology already
    exists.
2.  Identify existing terminology before proposing new terminology.
3.  Build a rigorous conceptual foundation.
4.  Derive Business Central guidance from general architectural
    principles.

# Current Working Hypothesis

A significant change to an established effective execution flow may also
modify architectural properties carried by that flow.

Those impacts should be reviewed independently of the mechanism used.

Status: **Open**

# Evolution

## Phase 1 -- Initial Observation

Origin: Business Central IsHandled pattern.

Observation: Subscribers frequently replace standard behavior.

Initial assumption: The main problem is loss of extensibility.

Status: Incomplete.

## Phase 2 -- Broader View

Observation:

-   Interfaces
-   Strategy
-   Workflow
-   Middleware
-   Plugins
-   IsHandled

can all modify established behavior.

Conclusion:

The research subject is behavior-changing customization, not IsHandled
itself.

Status: Accepted.

## Phase 3 -- Execution Flow

Execution Flow and Effective Execution Flow appear useful.

Open question:

Should they be formally defined or mapped to existing literature?

Status: Open.

## Phase 4 -- Review Trigger

Candidate hypothesis:

Architecturally significant behavioral changes should trigger
architectural review.

Status: Open.

# Rejected Directions

## "This is an IsHandled problem."

Rejected because IsHandled is only one implementation mechanism.

## "A completely new architectural entity exists."

Rejected until literature review proves otherwise.

# Terminology Under Investigation

-   Execution Flow
-   Effective Execution Flow
-   Behavior
-   Behavioral Contract
-   Effective Extensibility
-   Architectural Significance
-   Behavioral Change Review
-   Behavioral Change Review Trigger

# Related Work

-   Microsoft Learn
-   AL Guidelines
-   SEI
-   ISO/IEC/IEEE 42010
-   ATAM
-   SAAM
-   DDD
-   Fowler
-   BPM
-   Workflow Systems
-   Plugin Architectures

# BC Evidence Catalogue

Collect examples from:

-   Base Application
-   System Application
-   Localizations
-   Open-source AL repositories

For each example capture:

-   mechanism
-   affected flow
-   architectural consequences
-   review implications

# Open Questions

1.  What is an architecturally significant behavioral change?
2.  Which architectural properties are carried by execution flow?
3.  Which are already documented by Microsoft?
4.  Which remain undocumented?
5.  Can one review framework cover all behavior-changing mechanisms?

# Decisions

## 2026-07-16

Project scope expanded beyond IsHandled because the observed problem is
mechanism-independent.
