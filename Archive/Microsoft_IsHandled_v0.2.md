---
status: draft
version: 0.2
project: Behavior Change Review Framework
source-type: Microsoft Learn
---

# Microsoft_IsHandled.md

> **Iteration 0.2** – Expanded analytical draft

# Purpose

This document evaluates Microsoft's official guidance on the **IsHandled** pattern as one case study within the broader *Behavior Change Review Framework* research project.

Unlike Microsoft Learn, this document does **not** attempt to teach developers how to implement `IsHandled`.

Instead, it investigates:

- Microsoft's architectural concerns,
- the historical evolution of the pattern,
- what Microsoft explicitly states,
- what can reasonably be inferred,
- and what remains an open research question.

---

# Source Status

This document is based primarily on Microsoft Learn.

Historical community articles are included only to explain the evolution of the pattern and are **not** treated as normative guidance.

---

# Primary Sources

## Microsoft Learn

1. *Using the IsHandled pattern for events*

2. *Using IsHandled minimum requirements*

3. *Create an extensibility request*

4. *Types of events for extensibility*

---

# Executive Assessment

## Microsoft Position

Microsoft does **not** ban the IsHandled pattern.

Instead, Microsoft:

- discourages creation of new broad IsHandled events,
- recommends explicit extensibility mechanisms where possible,
- requires additional justification before introducing new handled events.

## Analysis

The official guidance consistently evaluates consequences rather than syntax.

The recurring concerns include:

- readability,
- extensibility,
- composability,
- future evolution,
- upgrade compatibility.

These concerns appear largely independent of the specific implementation mechanism.

---

# Historical Context

## NAV Era

The Handled pattern emerged during Microsoft Dynamics NAV when extensibility options were significantly more limited than today.

At that time:

- interfaces did not exist,
- dependency injection was unavailable,
- event infrastructure was less mature.

The pattern therefore became an important mechanism for replacing standard behavior.

## Community Evolution

### Mark Brummel

Mark Brummel is generally credited within the NAV community as an early promoter of the Handled pattern.

His original blog is no longer publicly available.

Historical references therefore rely primarily on later community discussions.

Status:

Historical context only.

### Vjekoslav Babić

Two articles are particularly relevant:

- Gentleman's Agreement Pattern
- Codeunit Interfaces in AL

These articles document how community thinking evolved as richer language constructs became available.

They are valuable historical evidence but are not normative over Microsoft Learn.

---

# Microsoft's Current Position

## Observation

Microsoft's recent documentation consistently moves toward:

- explicit contracts,
- interfaces,
- focused events,
- contribution instead of replacement.

This represents an architectural evolution rather than a simple coding recommendation.

---

# Microsoft Criticism 1 – Single Subscriber Assumption

## Microsoft Position

Handled events frequently assume that one subscriber becomes responsible for replacing standard behavior.

## Evidence

Microsoft Learn:
Using the IsHandled pattern for events.

## Analysis

The concern is architectural composition rather than syntax.

A replacement model makes independent extensions difficult to compose safely.

## Research Implications

Candidate review question:

> Can multiple independent customizations participate correctly?

## Findings

Status: Candidate

---

# Microsoft Criticism 2 – Coding by Convention

## Microsoft Position

Correct behavior depends upon informal agreements.

## Analysis

Implicit conventions are harder to validate than explicit contracts.

Interfaces improve discoverability because expectations become part of the type system.

## Research Implications

Candidate review question:

> Is the extension contract explicit and verifiable?

---

# Microsoft Criticism 3 – Turning Off Parts of the Code

## Microsoft Position

"The main problem is skipping large parts of code..."

(Short quotation intentionally limited.)

## Analysis

This is arguably Microsoft's strongest architectural criticism.

The issue is not bypassing statements.

The issue is bypassing responsibilities that may later evolve.

## Research Implications

Candidate review questions:

- Which responsibilities are intentionally bypassed?
- Which downstream events disappear?
- Which invariants become extension-owned?

Status: Accepted

---

# Architectural Interpretation

## Microsoft Position

Microsoft consistently argues for better extensibility mechanisms.

## Analysis

Our interpretation is intentionally broader.

The documented concerns appear applicable whenever established behavior is replaced, regardless of whether the implementation uses:

- IsHandled
- Interfaces
- Strategy
- Delegation
- Workflow
- Future mechanisms

This remains a working hypothesis requiring validation against additional literature.

---

# Preliminary Mapping

| Microsoft Observation | Candidate Review Question |
|---|---|
| Single subscriber | Can independent extensions coexist? |
| Coding by convention | Is the contract explicit? |
| Turning off code | Which responsibilities are bypassed? |
| Low readability | Can effective behavior be understood? |
| Fragile evolution | Will upstream improvements participate? |

---

# Findings

## Accepted

- Microsoft discourages broad IsHandled usage.
- Microsoft prefers explicit extensibility mechanisms.
- Microsoft's concerns extend beyond coding style.

## Candidate

- The review criteria appear mechanism-independent.
- The documented concerns may form the basis of a generalized Behavior Change Review Framework.

## Open

- Can every Microsoft concern be generalized beyond IsHandled?
- Does existing architecture literature already define an equivalent review process?

---

# Planned Expansion (Version 0.3)

- Complete analysis of every Microsoft criticism.
- Detailed references to Microsoft Learn sections.
- Expanded historical timeline.
- Mapping to ISO 42010/42020/42030 concepts.
- Base Application examples.
- Czech Localization examples.
- Comparison with interfaces and strategy.
- Consolidated evidence tables.

# Revision History

## 0.2

Expanded from the initial draft into a structured analytical reference aligned with the style used by ISO reference documents.
