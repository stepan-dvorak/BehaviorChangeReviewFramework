---
status: draft
version: 0.5
project: Behavior Change Review Framework
source-type: Microsoft Learn
depends-on:
  - 03_Related_Work
  - ISO_42010
  - ISO_42020
  - ISO_42030
---

# Microsoft_IsHandled.md

> Iteration **0.5** – Integrated Research Draft

# Purpose

This document evaluates Microsoft's official guidance on the **IsHandled**
pattern as a representative case of architecturally significant
behavior-changing customization.

Its objective is **not** to determine whether IsHandled is "good" or
"bad", but to understand what Microsoft's guidance reveals about the
architectural evaluation of behavior-changing customizations.

The document follows the same analytical style as the ISO reference
notes by clearly separating:

- Microsoft Position
- Evidence
- Analysis
- Research Implications
- Findings

---

# Position of this Document within the Research

Following analysis of ISO 42010, ISO 42020 and ISO 42030, this document
should no longer be interpreted as an isolated review of one AL pattern.

Instead, it represents the Business Central case study used to validate
whether Microsoft's practical guidance can be interpreted as a
specialized architecture-evaluation process.

Current hypothesis:

> Microsoft's IsHandled guidance is not merely coding guidance. It is an
implicit architecture evaluation guideline specialized for one
behavior-changing extensibility mechanism.

Status: Candidate.

---

# Relationship to ISO Standards

## ISO 42010

Provides concepts such as:

- stakeholders
- concerns
- architecture views
- architecture decisions
- correspondences

It does **not** define IsHandled review.

## ISO 42020

Defines architecture processes including governance,
conceptualization, evaluation and enablement.

Research implication:

The project should not claim to invent architecture review.

Instead it may define a lightweight Business Central specialization.

## ISO 42030

Provides a generic architecture evaluation framework.

Research implication:

Behavior Change Review is best positioned as a derived
Business Central evaluation framework rather than a new evaluation
theory.

---

# Historical Context

## Early NAV

Handled events emerged when object customization was the dominant
extension technique and alternative extensibility mechanisms were
limited.

## Community Evolution

Historical context:

- Mark Brummel
- Vjekoslav Babić
- transition from convention-based extensibility toward explicit
  contracts and interfaces.

Community sources explain historical evolution only.

---

# Microsoft's Architectural Evolution

Observed progression:

1. Enable extensibility.
2. Improve event quality.
3. Discourage broad replacement.
4. Introduce interfaces.
5. Encourage explicit contracts.
6. Require justification before adding new handled events.
7. Recommend extensibility requests when existing mechanisms are
   insufficient.

Analysis:

Microsoft's trajectory consistently reduces implicit behavioral
replacement and increases explicit architectural contracts.

---

# Detailed Analysis of Microsoft Criticisms

Each subsection follows the same analytical template.

## Single Subscriber Assumption

### Microsoft Position

Replacement assumes one subscriber controls continuation.

### Analysis

Primary concern:

Behavior composition.

### Research Implication

Potential review trigger:

Does the customization prevent independent composition?

Status: Candidate.

---

## Coding by Convention

### Microsoft Position

Correct behavior depends on convention rather than explicit language
constructs.

### Analysis

Architectural contracts should be explicit whenever practical.

### Candidate Review Question

Can another developer determine expected behavior from contracts rather
than documentation?

---

## Turning Off Parts of the Code

### Microsoft Position

Microsoft warns against bypassing significant portions of standard code
because future changes and downstream events may also be skipped.

### Analysis

This criticism concerns preservation of architectural responsibilities,
not merely skipped statements.

Potentially affected concerns:

- invariants
- telemetry
- transactions
- extension participation
- upgrade behavior

Status: Accepted.

---

## Low Readability

### Microsoft Position

Effective behavior becomes difficult to understand.

### Analysis

Execution is fragmented across subscribers.

### Candidate Review Question

Can effective behavior be reconstructed with reasonable effort?

---

## Fragile Evolution

### Microsoft Position

Future Base Application improvements may no longer execute.

### Analysis

Replacement creates ownership of future synchronization.

### Candidate Review Question

Who owns long-term behavioral synchronization?

---

## Extensibility Degradation

### Microsoft Position

Broad replacement reduces future extensibility.

### Analysis

Technical extension points may remain reachable while practical
participation disappears.

Research relationship:

This observation strongly motivates the project's candidate concept of
Effective Extensibility.

Status: Candidate.

---

# Architectural Interpretation

## Microsoft Explicitly States

- Prefer interfaces.
- Prefer explicit contracts.
- Limit broad IsHandled events.
- Evaluate alternatives before introducing new handled events.

## Project Interpretation

Microsoft already evaluates architecture-related concerns including:

- composition
- maintainability
- evolution
- extensibility
- upgrade compatibility

The project hypothesis is therefore refined:

Rather than inventing new review criteria, the framework should unify
Microsoft's mechanism-specific guidance into a mechanism-independent
review methodology.

Status: Candidate.

---

# Mapping to Behavior Change Review

| Microsoft Observation | Architectural Concern | Candidate Review Question |
|---|---|---|
| Single subscriber | Composition | Can multiple solutions coexist? |
| Coding by convention | Explicit contract | Is the contract verifiable? |
| Turning off code | Behavioral completeness | Which responsibilities are bypassed? |
| Low readability | Maintainability | Can effective behavior be understood? |
| Fragile evolution | Evolution | Who owns future synchronization? |
| Extensibility degradation | Ecosystem | Does effective extensibility remain? |

---

# Relationship to Extensibility Requests

Microsoft's Extensibility Request process asks developers to justify why
existing mechanisms are insufficient.

Analysis:

This resembles an architectural decision process rather than a coding
review.

Candidate interpretation:

An Extensibility Request may be viewed as an upstream architecture
review, whereas the proposed Behavior Change Review Framework evaluates
downstream solution-specific behavior changes.

---

# Planned Evidence Catalogue

Future iterations will associate each Microsoft observation with:

- Microsoft Learn references
- Base Application examples
- Czech Localization examples
- Interface-based alternative
- Strategy-based alternative

---

# Findings

## Accepted

- Microsoft discourages broad IsHandled usage.
- Microsoft increasingly recommends explicit extensibility mechanisms.
- General architecture description, process and evaluation frameworks
already exist (ISO 42010, 42020, 42030).

## Candidate

- Microsoft's IsHandled guidance represents a Business Central-specific
architecture evaluation practice.
- The proposed framework should specialize existing standards rather
than replace them.

## Open

- Which review questions should be mandatory?
- What proportionality model should be applied?
- Can Effective Extensibility be objectively assessed?

---

# Planned Expansion (Version 0.6)

- Clause-level Microsoft Learn references.
- Short quotations with section mapping.
- Cross-reference matrix:
  Microsoft ↔ ISO 42010 ↔ ISO 42020 ↔ ISO 42030.
- Behavior Change Review checklist.
- Detailed case studies from Base Application and Czech Localization.

# Revision History

## 0.5

Integrated conclusions from ISO 42010, ISO 42020 and ISO 42030.
Refined the originality claim from a new evaluation framework toward a
Business Central-specific specialization of existing architecture
evaluation principles.
