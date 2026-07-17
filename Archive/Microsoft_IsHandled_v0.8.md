---
status: draft
version: 0.8
project: Behavior Change Review Framework
source-type: Microsoft Learn
depends-on:
  - 03_Related_Work
  - ISO_42010
  - ISO_42020
  - ISO_42030
---

# Microsoft_IsHandled.md

> Iteration **0.8** – Deep Analytical Draft (Part II)

# Purpose

This iteration continues the deep architectural analysis started in v0.7.
Rather than introducing new topics, it expands the remaining major
Microsoft criticisms using the common research structure:

- Microsoft Position
- Evidence
- Analysis
- Research Implications
- Current Findings

The objective is to determine whether Microsoft's guidance can be
generalized into a mechanism-independent Behavior Change Review process.

---

# Deep Analysis — Single Subscriber Assumption

## Microsoft Position

The `IsHandled` pattern implicitly assumes that one subscriber becomes
responsible for replacing the standard implementation.

## Evidence

Microsoft recommends explicit extensibility models because replacement
patterns compose poorly when multiple independent extensions attempt to
change the same behavior.

## Analysis

This criticism is frequently interpreted as a limitation of events.

Architecturally it is better understood as a **composition problem**.

The original execution model implicitly assumes:

- one owner,
- one replacement,
- one effective continuation.

Modern Business Central ecosystems instead consist of:

- Microsoft applications,
- localization layers,
- ISV solutions,
- customer extensions.

Multiple independent architectural decisions therefore coexist.

The architectural question becomes:

> Can independently developed behavior changes compose without prior
coordination?

This question remains meaningful regardless of whether composition uses
events, interfaces, strategies or workflow orchestration.

## Research Implications

Behavior Change Review should evaluate:

- composition assumptions;
- ordering assumptions;
- ownership conflicts;
- deterministic behavior.

## Current Finding

**Accepted**

The Single Subscriber criticism is fundamentally about architectural
composition rather than event mechanics.

---

# Deep Analysis — Coding by Convention

## Microsoft Position

Correct behavior depends upon conventions rather than explicit language
constructs.

## Evidence

Microsoft increasingly recommends interfaces and explicit contracts.

## Analysis

Conventions work well inside stable teams.

Architectures, however, evolve across:

- time,
- organizations,
- partner ecosystems,
- platform releases.

Conventions therefore become difficult to discover, validate and review.

Interfaces convert many behavioral assumptions into explicit contracts
that are visible to both developers and tools.

The architectural distinction is therefore:

Implicit expectation

↓

Explicit architectural contract

This aligns naturally with ISO 42010's emphasis on architecture
descriptions and documented decisions.

## Research Implications

Candidate review questions:

- Which assumptions remain undocumented?
- Which assumptions are enforced only socially?
- Can automated tooling validate the contract?

## Current Finding

**Accepted**

The concern is better interpreted as architectural explicitness rather
than coding style.

---

# Deep Analysis — Extensibility Degradation

## Microsoft Position

Broad behavioral replacement reduces extensibility opportunities for
future extensions.

## Evidence

Microsoft repeatedly recommends narrower extension points and explicit
variation mechanisms.

## Analysis

This criticism appears especially important for the current research.

An event may remain:

- technically reachable,
- publicly documented,
- syntactically correct,

while no longer influencing the effective runtime behavior.

The extension capability still exists.

Its practical architectural value has changed.

This distinction motivated the candidate term:

**Effective Extensibility**

The term should not yet be presented as new software architecture
terminology.

Instead it may first be treated as a Business Central-specific evaluation
concern derived from Microsoft's observations.

## Research Implications

Candidate review questions:

- Does another extension still participate meaningfully?
- Is the extension point only technically reachable?
- Has semantic participation changed?

## Current Finding

**Candidate**

The concept requires validation using Base Application evidence.

---

# Synthesis of Microsoft Criticisms

The six criticisms analysed across versions 0.7 and 0.8 can be grouped
into higher-level architectural themes.

| Microsoft criticism | Candidate architectural theme |
|---|---|
| Turning off parts of the code | Responsibility transfer |
| Fragile evolution | Evolution ownership |
| Low readability | Architectural discoverability |
| Single subscriber | Composition |
| Coding by convention | Explicit contracts |
| Extensibility degradation | Effective extensibility |

A notable observation is that none of these themes is inherently tied to
the IsHandled mechanism.

---

# Candidate Behavior Change Review Categories

The emerging review categories are therefore:

1. Responsibility
2. Composition
3. Contracts
4. Discoverability
5. Evolution
6. Extensibility

These categories may eventually replace the current mechanism-oriented
discussion.

---

# Relationship to ISO Research

ISO 42010 provides the vocabulary for:

- concerns,
- stakeholders,
- decisions,
- views.

ISO 42020 provides the process context.

ISO 42030 provides the generic evaluation framework.

Microsoft Learn contributes practical Business Central concerns.

The proposed framework therefore appears to integrate these sources
rather than compete with them.

---

# Current Assessment

The accumulated evidence increasingly supports the following statement:

> Microsoft's guidance surrounding IsHandled can be interpreted as an
implicit architecture evaluation specialized for one extensibility
mechanism.

The proposed contribution of this research is to extract those concerns,
generalize them beyond IsHandled and organize them into a reusable
Business Central review methodology.

Status: **Candidate – requires validation with real code examples.**

---

# Planned Version 0.9

The next iteration should focus on evidence rather than theory by adding:

- Base Application case studies,
- Czech Localization examples,
- comparison with interface-based implementations,
- comparison with strategy-based implementations,
- evidence matrix linking each example to Microsoft guidance and ISO
concepts.

# Revision History

## 0.8

Completed deep architectural analysis of the remaining principal
Microsoft criticisms and synthesized them into six candidate
architecture-evaluation categories.
