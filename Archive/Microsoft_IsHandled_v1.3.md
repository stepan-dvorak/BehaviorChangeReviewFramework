
---
status: draft
version: 1.3
type: reference
title: Microsoft_IsHandled
---

# Microsoft_IsHandled

> Reference analysis of Microsoft's guidance on the **IsHandled** pattern.

## Purpose

This document records Microsoft's current guidance on the IsHandled pattern,
distinguishes normative statements from research interpretation, and provides
representative empirical evidence supporting (or challenging) those statements.
The document intentionally remains focused on **IsHandled** as a single case
study rather than attempting to define the complete Behavior Change Review
Framework.

---

# Evidence Confidence Model

Every conclusion in this document is classified according to its evidence.

| Level | Meaning |
|-------|---------|
| **Normative** | Explicitly documented by Microsoft Learn. |
| **Empirically Supported** | Observed in representative Business Central applications. |
| **Candidate** | Plausible interpretation requiring broader validation. |
| **Hypothesis** | Research direction without sufficient evidence yet. |

---

# Microsoft's Current Direction

Microsoft's current guidance consistently promotes:

- avoiding new broad IsHandled events,
- preferring explicit extension points,
- preferring interfaces when behaviour selection is intentional,
- creating extensibility requests instead of introducing generic override hooks.

## Research Interpretation

Rather than rejecting IsHandled, Microsoft narrows its acceptable usage by
evaluating architectural consequences.

**Confidence:** Normative

---

# Analysis of Individual Criticisms

## Turning Off Parts of the Code

### Microsoft Position

Replacing execution may bypass future platform behaviour.

### Representative Empirical Evidence

The analysed Czech localization applications contain several complete
execution overrides in posting and disposal logic, illustrating the exact
category of replacement discussed by Microsoft. These examples demonstrate
that ownership of behaviour moves from the platform to the extension without
claiming that every override is necessarily incorrect.

### Research Interpretation

The primary architectural concern is **responsibility transfer** rather than
the skipped source code itself.

### Limitations

The current empirical sample covers only two Microsoft localization
applications.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Empirically Supported**

---

## Fragile Evolution

### Microsoft Position

Future platform improvements may not execute through replaced code paths.

### Representative Empirical Evidence

The analysed overrides are tightly coupled to current Base Application
behaviour, implying that future Microsoft changes require independent review
inside the extension.

### Research Interpretation

The architectural problem concerns ownership of behavioural evolution.

### Limitations

Longitudinal evidence across multiple BC releases has not yet been collected.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Empirically Supported**

---

## Low Readability

### Microsoft Position

Handled patterns reduce readability.

### Representative Empirical Evidence

Representative subscribers contain substantial business processes whose
effective runtime behaviour can only be reconstructed by following multiple
publishers and subscribers.

### Research Interpretation

"Readability" is interpreted as the broader architectural quality of
**discoverability**.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Candidate**

---

## Single Subscriber Assumption

### Microsoft Position

Broad replacement assumes a single effective implementation.

### Representative Empirical Evidence

The analysed localization code contains competing subscribers targeting
identical posting events, demonstrating Microsoft's composition concern.

### Research Interpretation

The architectural issue is composability between independently developed
extensions.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Empirically Supported**

---

## Coding by Convention

### Microsoft Position

Correct behaviour depends on conventions.

### Representative Empirical Evidence

Representative implementations rely on implicit behavioural assumptions
rather than explicit contracts or declared orchestration.

### Research Interpretation

Interfaces and explicit contracts reduce governance risk by making
architectural decisions visible.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Candidate**

---

## Extensibility Degradation

### Microsoft Position

Broad overrides may reduce future extensibility.

### Representative Empirical Evidence

Several analysed patterns classified as DEAD-END EVENT or EXTENSIBILITY BREAK
show technically available extension points becoming practically ineffective.

### Research Interpretation

This motivates the working concept of **Effective Extensibility**.

### Limitations

The concept requires validation outside Czech localization applications.

### Confidence

- Microsoft Position: **Normative**
- Interpretation: **Candidate**

---

# Cross-cutting Findings

The empirical studies do **not** prove Microsoft's guidance.

Instead, they demonstrate that the architectural concerns described in the
documentation recur in representative production code.

This distinction is important:

- Microsoft provides the normative guidance.
- Empirical studies validate that the same concern types occur in practice.
- The Behavior Change Review Framework generalizes these concerns beyond
  IsHandled.

---

# Research Limitations

Current empirical evidence intentionally remains representative rather than
exhaustive.

Future studies should analyse:

- remaining Microsoft localization applications,
- AppSource extensions,
- independent ISV applications,
- future Business Central releases,
- additional behaviour-change markers beyond IsHandled.

---

# Summary

Current evidence supports three conclusions:

1. Microsoft's guidance is primarily architectural.
2. Representative production code reflects the same concern categories.
3. IsHandled serves as an excellent validation case but should not define the
   scope of the future Behavior Change Review Framework by itself.

# Revision History

## 1.3

Introduced explicit evidence confidence levels, representative empirical
evidence beside each Microsoft criticism, separate limitation sections, and
clearer separation between Microsoft guidance and research interpretation.
