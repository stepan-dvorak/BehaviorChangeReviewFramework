
---
status: working-draft
target: Microsoft_IsHandled_v2.0
iteration: 2.0-alpha-01
---

# Microsoft_IsHandled

> Working draft toward version 2.0.
> This iteration establishes the complete document skeleton and fully
> develops the introductory chapters. Later iterations will expand each
> analytical chapter without changing the overall structure.

# Table of Contents

1. Purpose
2. Scope
3. Research Method
4. Terminology
5. Historical Evolution
6. Microsoft's Current Position
7. Detailed Analysis of Microsoft's Criticisms
   7.1 Turning Off Parts of the Code
   7.2 Fragile Evolution
   7.3 Low Readability
   7.4 Single Subscriber Assumption
   7.5 Coding by Convention
   7.6 Extensibility Degradation
8. Cross-cutting Architectural Themes
9. Representative Empirical Validation
10. Relationship to Behavior Change Review Framework
11. Threats to Validity
12. Conclusions
13. References

---

# 1. Purpose

The purpose of this reference is to analyse Microsoft's published guidance
for the IsHandled pattern, distinguish documented recommendations from
research interpretation, and identify architectural concerns that remain
relevant independently of IsHandled itself.

This document deliberately studies a single extensibility mechanism. It
does not attempt to define the complete Behavior Change Review Framework.
Instead it provides one thoroughly documented case study from which more
general review principles may later be derived.

---

# 2. Scope

Included:

- official Microsoft guidance,
- historical evolution,
- architectural interpretation,
- representative empirical validation,
- implications for architecture review.

Excluded:

- complete empirical catalogues,
- framework definition,
- interface design,
- workflow modelling,
- general ISO architecture theory.

These topics are maintained as independent reference documents.

---

# 3. Research Method

This document intentionally separates four layers of evidence.

## Layer 1 — Microsoft Guidance

Normative recommendations published by Microsoft Learn.

## Layer 2 — Empirical Observation

Representative observations from analysed Business Central applications.

## Layer 3 — Research Interpretation

Architectural interpretation derived from Layers 1 and 2.

## Layer 4 — Framework Implication

Candidate review questions that may later become part of the Behavior
Change Review Framework.

Maintaining these layers separately prevents Microsoft guidance,
empirical evidence and research conclusions from becoming unintentionally
mixed.

---

# 4. Terminology

Throughout this document the following distinction is maintained.

**Mechanism**

A technical implementation technique (for example IsHandled).

**Architectural Concern**

A quality or property affected by the mechanism (composition,
discoverability, evolution, responsibility...).

**Behavior Change**

A customization that changes effective runtime behaviour.

The research focuses on architectural concerns rather than mechanisms.

---

# 5. Historical Evolution

The Handled pattern originated as a practical response to limited
extensibility options in Microsoft Dynamics NAV. Compared with source-code
modifications it represented a significant architectural improvement,
allowing behaviour to be replaced through events instead of direct object
changes.

As Business Central evolved, Microsoft introduced richer extensibility
mechanisms including interfaces, focused integration events and explicit
contracts. Rather than prohibiting IsHandled, Microsoft gradually narrowed
the circumstances in which new handled events should be introduced.

This evolution is important because it demonstrates a shift from enabling
behaviour replacement toward governing architectural consequences.

> Remaining chapters intentionally left as structured placeholders for
> subsequent iterations.

# 6. Microsoft's Current Position

Placeholder.

# 7. Detailed Analysis of Microsoft's Criticisms

Each subsection will follow this fixed structure:

- Microsoft Position
- Microsoft Evidence
- Representative Empirical Evidence
- Research Interpretation
- Counterarguments
- Framework Implication
- Threats to Validity
- Confidence Assessment

## 7.1 Turning Off Parts of the Code

Placeholder.

## 7.2 Fragile Evolution

Placeholder.

## 7.3 Low Readability

Placeholder.

## 7.4 Single Subscriber Assumption

Placeholder.

## 7.5 Coding by Convention

Placeholder.

## 7.6 Extensibility Degradation

Placeholder.

# 8–13

Reserved for later iterations.
