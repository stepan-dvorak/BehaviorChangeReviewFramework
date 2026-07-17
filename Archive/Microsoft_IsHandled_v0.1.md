# Microsoft_IsHandled.md

---
status: draft
version: 0.1
project: Behavior Change Review Framework
source-type: Microsoft Learn
---

# Purpose

This document analyzes Microsoft's official guidance regarding the `IsHandled` pattern and evaluates its relevance to the Behavior Change Review Framework.

# Primary Sources

1. Use the IsHandled pattern
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-pattern

2. Use IsHandled minimum requirements
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-min-req

3. Create an extensibility request
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/create-extensibility-request

4. Types of events for extensibility
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/types-of-events-for-extensibility

# Microsoft Position

## IsHandled is no longer the preferred extensibility mechanism

Microsoft recommends avoiding new IsHandled events where practical and instead using explicit extensibility mechanisms such as interfaces, concepts and well-designed events.

## Historical Context

Microsoft explains that IsHandled originated before richer extensibility constructs such as interfaces were available.

## Problems Identified by Microsoft

### Low readability

Microsoft states that IsHandled introduces additional code paths and makes it difficult to understand which code will execute. It also notes that the Base Application contains more than 8,000 IsHandled events.

### Hidden execution paths

Microsoft states:

> "The main problem is skipping large parts of code that might change in the future, and then risk that other events aren't raised."

### Fragile evolution

Skipping standard implementation increases the risk that future platform improvements are not inherited.

### Extensibility degradation

Microsoft recommends replacing broad overrides with explicit extensibility concepts whenever possible.

# Event Taxonomy

Microsoft classifies Handled Events as low-value compared to Business Events and recommends better extensibility models where feasible.

# Minimum Requirements

Microsoft requires consideration of:

- problem statement
- alternatives considered
- justification
- performance
- data sensitivity
- multi-extension interaction
- future evolution
- testing impact

These criteria resemble a lightweight architecture review.

# Analysis

Microsoft consistently argues against IsHandled because it reduces readability, weakens extensibility and complicates long-term evolution.

The review criteria documented for new IsHandled events are largely independent of the mechanism itself and appear applicable to many behavior-changing customizations.

# Research Implications

The project should not present IsHandled as the problem.

Instead, IsHandled serves as a case study exposing a broader architectural question:

How should architecturally significant behavior-changing customizations be reviewed regardless of implementation mechanism?

# Findings

- Microsoft discourages new IsHandled usage.
- Microsoft already evaluates architectural consequences.
- Microsoft does not currently publish a unified mechanism-independent review framework.

# Revision History

## 0.1

Initial analytical draft.
