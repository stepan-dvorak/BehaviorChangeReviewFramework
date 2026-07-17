---
status: draft
version: 0.6
project: Behavior Change Review Framework
source-type: Microsoft Learn
depends-on:
  - 03_Related_Work
  - ISO_42010
  - ISO_42020
  - ISO_42030
---

# Microsoft_IsHandled.md

> Iteration **0.6** – Evidence-Oriented Research Draft

# Purpose

This document analyses Microsoft's official guidance regarding the
`IsHandled` pattern as a Business Central case study for the proposed
Behavior Change Review Framework.

Unlike Microsoft Learn, this document does not teach the pattern itself.
Instead, it evaluates the architectural reasoning behind Microsoft's
recommendations.

Every major section follows the structure:

- Microsoft Position
- Evidence
- Analysis
- Research Implications
- Findings

---

# Executive Assessment

## Microsoft Position

Microsoft no longer recommends broad `IsHandled` events as the preferred
extensibility mechanism. New handled events should satisfy explicit
minimum requirements and richer alternatives should be considered first.

## Evidence

Primary Microsoft Learn articles:

- Using the IsHandled pattern for events
- Using IsHandled minimum requirements
- Types of events for extensibility
- Create an extensibility request

## Analysis

Microsoft consistently evaluates consequences affecting architecture
rather than AL syntax.

The recurring concerns are:

- composition,
- maintainability,
- discoverability,
- upgradeability,
- extensibility,
- behavioral correctness.

## Research Implications

This strongly supports treating IsHandled as one observable instance of a
broader class of behavior-changing customizations.

## Findings

Status: Accepted.

---

# Historical Evolution

## NAV Era

Handled events provided an alternative to object modifications when
explicit substitution mechanisms were unavailable.

## Transition to AL

The introduction of interfaces and richer event taxonomy gradually
reduced the need for broad behavioral replacement.

## Community Perspective

Historical discussions by Mark Brummel and Vjekoslav Babić document this
transition but are treated strictly as historical context.

Finding:

Microsoft Learn remains the normative source.

---

# Detailed Analysis of Microsoft Criticisms

## Single Subscriber Assumption

### Microsoft Position

Replacement assumes one subscriber becomes responsible for continuation.

### Evidence

Microsoft Learn identifies composition difficulties when behavior is
replaced rather than extended.

### Analysis

This concern is fundamentally about architectural composition.

### Research Implications

Possible review criteria:

- Can independent extensions coexist?
- Is execution deterministic?
- Does one extension monopolize behavior?

### Findings

Candidate.

---

## Coding by Convention

### Microsoft Position

Behavior depends upon conventions instead of explicit language contracts.

### Evidence

Microsoft recommends interfaces and explicit extensibility mechanisms.

### Analysis

The architectural issue is implicit contracts.

### Research Implications

Review should evaluate whether assumptions are machine-verifiable.

### Findings

Accepted.

---

## Turning Off Parts of the Code

### Microsoft Position

Microsoft warns that bypassing standard implementation may bypass future
logic and downstream events.

### Evidence

Short quotation:

> "The main problem is skipping large parts of code..."

### Analysis

The issue is transfer of architectural responsibilities.

Examples of potentially affected responsibilities:

- validation,
- telemetry,
- transaction handling,
- event publication,
- security checks,
- future platform improvements.

### Research Implications

Candidate review questions:

- Which responsibilities disappear?
- Which become extension-owned?
- Which stakeholder concerns change?

### Findings

Accepted.

---

## Low Readability

### Microsoft Position

Effective behavior becomes increasingly difficult to understand.

### Analysis

Behavior is distributed across subscribers and runtime conditions.

### Research Implications

Review should assess architectural discoverability rather than source
code size alone.

### Findings

Accepted.

---

## Fragile Evolution

### Microsoft Position

Replacement prevents automatic participation in future Base Application
improvements.

### Analysis

Every behavioral replacement introduces long-term synchronization debt.

### Research Implications

Review should explicitly record ownership of future synchronization.

### Findings

Accepted.

---

## Extensibility Degradation

### Microsoft Position

Broad replacement reduces extensibility opportunities.

### Analysis

An extension point may remain technically available while becoming
behaviorally ineffective.

### Research Implications

This observation directly motivates the candidate concept of
**Effective Extensibility**.

### Findings

Candidate.

---

# Architectural Interpretation

## What Microsoft Explicitly States

Microsoft recommends:

- explicit contracts,
- interfaces,
- focused events,
- minimizing handled events,
- evaluating alternatives first.

## Project Interpretation

The documented concerns are not inherently tied to IsHandled.

Equivalent concerns can arise whenever established behavior is replaced
through any extensibility mechanism.

Therefore the proposed framework should evaluate consequences rather than
mechanisms.

Status: Candidate.

---

# Mapping to ISO Standards

| Microsoft concern | ISO 42010 | ISO 42020 | ISO 42030 |
|---|---|---|---|
| Readability | Concern / View | Evaluation activity | Evaluation criterion |
| Composition | Stakeholder concern | Governance | Architecture quality |
| Evolution | Architecture decision | Elaboration | Risk assessment |
| Extensibility | Concern | Conceptualization | Stakeholder value |
| Upgradeability | Concern | Evaluation | Architecture objective |

Analysis:

The ISO standards provide the generic architecture vocabulary while
Microsoft provides Business Central-specific operational guidance.

---

# Candidate Behavior Change Review Questions

1. Which established behavior changes?
2. Which stakeholder concerns are affected?
3. Which architectural responsibilities move?
4. Which contracts become implicit?
5. Can multiple extensions still participate?
6. What is the upgrade strategy?
7. Which events become behaviorally ineffective?
8. Is an interface-based alternative available?

---

# Current Research Position

Current evidence suggests the project should not claim:

"A new architecture evaluation framework."

A more defensible claim is:

"A lightweight Business Central specialization of existing architecture
evaluation practices for architecturally significant behavior-changing
customizations."

---

# Planned Evidence Integration

Future iterations should add:

- exact Microsoft Learn section references,
- Base Application evidence,
- Czech Localization evidence,
- comparison with interface implementations,
- comparison with strategy implementations,
- evidence matrix.

---

# Findings

## Accepted

- Microsoft evaluates architectural consequences.
- Existing ISO standards already define architecture description,
  process and evaluation.
- The project should specialize existing practice.

## Candidate

- Effective Extensibility is a useful Business Central evaluation
  concern.
- Microsoft guidance can be generalized into a mechanism-independent
  review methodology.

## Open

- Objective trigger thresholds.
- Review proportionality.
- Formal validation using Base Application evidence.

# Revision History

## 0.6

Restructured around evidence-oriented analysis. Added explicit
Evidence/Analysis/Research Implications sections, ISO mapping, candidate
Behavior Change Review questions, and refined the project's originality
claim.
