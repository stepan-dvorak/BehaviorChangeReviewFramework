---
status: draft
version: 0.3
project: Behavior Change Review Framework
source-type: Microsoft Learn
depends-on:
  - 03_Related_Work
  - Microsoft_Extensibility_Overview
---

# Microsoft_IsHandled.md

> Iteration **0.3** – Expanded analytical reference

# Purpose

This document evaluates Microsoft's official guidance regarding the
`IsHandled` pattern and investigates how that guidance can inform a
mechanism-independent **Behavior Change Review Framework**.

The document intentionally distinguishes:

- Microsoft's documented position,
- supporting evidence,
- architectural interpretation,
- research implications,
- current findings.

It is an analytical research note rather than a replacement for
Microsoft Learn.

---

# Executive Assessment

Microsoft does **not** prohibit the `IsHandled` pattern.

Instead, Microsoft has gradually shifted from presenting `IsHandled` as a
practical extensibility mechanism toward recommending explicit,
contract-based extensibility mechanisms whenever feasible.

The criticism published by Microsoft consistently concerns architectural
properties such as readability, composability, maintainability,
discoverability and long-term evolution rather than the AL syntax itself.

**Working hypothesis**

These concerns may apply to any architecturally significant
behavior-changing customization, regardless of implementation mechanism.

Status: **Candidate**

---

# Primary Microsoft Sources

1. Using the IsHandled pattern for events
2. Using IsHandled minimum requirements
3. Create an extensibility request
4. Types of events for extensibility

These remain the primary normative references.

---

# Historical Context

## Origin

The Handled pattern emerged during the Microsoft Dynamics NAV era when
today's interface-based extensibility model did not yet exist.

It allowed partners to replace portions of standard behavior without
modifying Microsoft's application objects.

## Community Evolution

### Mark Brummel

Mark Brummel is widely recognized as an early advocate of the Handled
pattern. The original article is no longer publicly available, therefore
its influence is treated as historical context only.

### Vjekoslav Babić

Articles such as *Gentleman's Agreement Pattern* and *Codeunit
Interfaces in AL* document the transition from convention-based
extensibility toward explicit contracts using interfaces.

These articles provide valuable historical context but do not supersede
Microsoft Learn.

---

# Microsoft's Architectural Direction

Recent Microsoft guidance consistently promotes:

- explicit contracts,
- interfaces,
- focused integration events,
- contribution instead of replacement,
- reducing reliance on broad IsHandled events.

This should be viewed as an architectural evolution rather than a simple
coding-style recommendation.

---

# Detailed Analysis of Microsoft Criticisms

## Single Subscriber Assumption

### Microsoft Position

Handled events frequently assume that a single subscriber replaces the
standard implementation.

### Analysis

The architectural concern is composition rather than event syntax.

### Candidate Review Question

Can multiple independent extensions participate safely?

---

## Coding by Convention

### Microsoft Position

Correct behavior depends on unwritten conventions.

### Analysis

Implicit contracts are difficult to verify and evolve.

### Candidate Review Question

Is the extension contract explicit and enforceable?

---

## Turning Off Parts of the Code

### Microsoft Position

Microsoft warns against skipping large sections of standard code because
future behavior and events may also be skipped.

### Short quotation

> "The main problem is skipping large parts of code..."

### Analysis

The architectural issue is loss of responsibilities previously provided
by the standard implementation.

### Candidate Review Questions

- Which responsibilities are bypassed?
- Which events no longer execute?
- Which invariants become extension-owned?

Status: Accepted

---

## Low Readability

### Microsoft Position

Large numbers of handled events make execution harder to understand.

### Analysis

Readability is closely related to architectural discoverability.

### Candidate Review Question

Can the effective behavior be reconstructed by another developer?

---

## Fragile Evolution

### Microsoft Position

Future improvements to the Base Application may no longer participate in
the customized execution path.

### Analysis

The replacement creates a long-term maintenance obligation.

### Candidate Review Question

How will upstream changes be evaluated after upgrades?

---

# Architectural Interpretation

## Microsoft Position

Microsoft evaluates IsHandled primarily through the consequences it has
for extensibility and evolution.

## Project Interpretation

The identified concerns appear independent of the implementation
mechanism.

Equivalent consequences may arise from:

- interfaces,
- strategies,
- workflow replacement,
- delegation,
- future extensibility mechanisms.

This interpretation remains a research hypothesis requiring validation
against software architecture literature.

---

# Mapping to Behavior Change Review Framework

| Microsoft Observation | Architectural Concern | Candidate Review Question |
|---|---|---|
| Single subscriber | Composition | Can independent extensions coexist? |
| Coding by convention | Explicit contracts | Is the contract explicit? |
| Turning off code | Behavioral completeness | Which responsibilities disappear? |
| Low readability | Maintainability | Can effective behavior be understood? |
| Fragile evolution | Evolution | Will future platform improvements participate? |

---

# Findings

## Accepted

- Microsoft discourages broad IsHandled usage.
- Microsoft prefers explicit extensibility mechanisms.
- The criticism targets architectural consequences.

## Candidate

- Microsoft's review concerns appear largely mechanism-independent.
- They may be reusable within a generalized Behavior Change Review Framework.

## Open

- Which concerns should become mandatory review criteria?
- Does ISO 42030 already provide equivalent evaluation guidance?

---

# Planned Expansion (Version 0.4)

- Detailed evidence for every Microsoft criticism.
- Direct links to individual Microsoft Learn sections.
- ISO 42010/42020/42030 mapping.
- Extensibility Request process analysis.
- Base Application examples.
- Czech Localization examples.
- Comprehensive references.

# Revision History

## 0.3

Expanded analytical structure, deeper treatment of Microsoft's
architectural criticisms, explicit Architectural Interpretation section,
and initial mapping toward the Behavior Change Review Framework.
