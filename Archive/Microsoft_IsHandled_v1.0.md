
---
status: draft
version: 1.0
project: Behavior Change Review Framework
type: reference
depends-on:
  - ISO_42010
  - ISO_42020
  - ISO_42030
  - Microsoft_Extensibility_Overview
  - Microsoft_Event_Types
---

# Microsoft_IsHandled

> Reference document describing Microsoft's guidance on the **IsHandled**
> pattern and its architectural interpretation within the Behavior Change
> Review Framework research.

# Purpose

This document consolidates Microsoft's official guidance regarding the
**IsHandled** pattern into a single research reference.

Its scope is intentionally limited to **IsHandled**. It does not attempt
to describe interfaces, workflow, strategy, or architecture evaluation
in general; those topics are documented in their own reference files.

The objective is to answer four questions:

1. What does Microsoft explicitly recommend?
2. Why has Microsoft's guidance evolved?
3. Which architectural concerns repeatedly appear?
4. How does this influence the proposed Behavior Change Review Framework?

---

# Scope

Included:

- Historical evolution of the Handled pattern
- Current Microsoft guidance
- Architectural interpretation
- Representative empirical validation
- Candidate implications for the framework

Excluded:

- Complete empirical catalogue of IsHandled usage
- Detailed ISO explanations (see [[ISO_42010]], [[ISO_42020]], [[ISO_42030]])
- General interface guidance (see [[Microsoft_Interfaces]])
- General extensibility guidance (see [[Microsoft_Extensibility_Overview]])

---

# Historical Context

## NAV era

The Handled pattern became widely adopted when Microsoft Dynamics NAV
offered limited extensibility mechanisms. It enabled partners to replace
standard behaviour without modifying Microsoft objects.

## Community Evolution

### Mark Brummel

Historically associated with early promotion of the Handled pattern.
Included here as historical context only.

### Vjekoslav Babić

Articles such as *Gentleman's Agreement Pattern* and *Codeunit
Interfaces in AL* document the community's transition from convention-
based extensibility toward explicit contracts.

These articles are valuable historical context but are not normative.

---

# Microsoft's Current Position

## Microsoft Position

Across current Microsoft Learn documentation the direction is
consistent:

- avoid creating new broad IsHandled events where practical;
- prefer explicit contracts (interfaces, focused events);
- require additional justification before introducing new handled events;
- encourage extensibility requests where existing extension points are
  insufficient.

## Evidence

Primary Microsoft Learn references:

- Using the IsHandled pattern for events
- Using IsHandled minimum requirements
- Create an extensibility request
- Types of events for extensibility

## Analysis

Microsoft does not declare the pattern obsolete. Instead it evaluates
its architectural consequences and promotes alternatives that preserve
composability and long-term evolution.

## Research Implications

The framework should evaluate **architectural consequences**, not merely
the selected extensibility mechanism.

## Findings

Accepted.

---

# Analysis of Microsoft's Criticisms

## Turning Off Parts of the Code

### Microsoft Position

Skipping large portions of standard implementation may also skip future
logic and downstream events.

### Analysis

The underlying concern is **responsibility transfer**. Replacing
behaviour transfers ownership of validation, event publication,
transactions, telemetry and future evolution to the extension.

### Research Implications

Review questions:

- Which responsibilities are transferred?
- Which responsibilities remain with the platform?

### Findings

Accepted.

---

## Fragile Evolution

### Microsoft Position

Future Base Application improvements may not participate in replaced
execution paths.

### Analysis

The concern is **evolution ownership**, not upgrade mechanics.

### Findings

Accepted.

---

## Low Readability

### Microsoft Position

Distributed behaviour becomes harder to understand.

### Analysis

This is more accurately interpreted as **architectural discoverability**:
maintainers must reconstruct effective behaviour from multiple extension
points.

### Findings

Accepted.

---

## Single Subscriber Assumption

### Microsoft Position

Replacement assumes one effective owner of execution.

### Analysis

The concern is architectural **composition**. Independent extensions
must coexist without implicit ordering assumptions.

### Findings

Accepted.

---

## Coding by Convention

### Microsoft Position

Correct behaviour depends on convention rather than explicit contracts.

### Analysis

Implicit contracts scale poorly across organizations and releases.

### Findings

Accepted.

---

## Extensibility Degradation

### Microsoft Position

Broad replacement reduces future extensibility.

### Analysis

Technical extension points may remain available while becoming
architecturally ineffective.

### Findings

Candidate.

---

# Architectural Interpretation

## Microsoft Position

Microsoft evaluates IsHandled through consequences affecting
maintainability, composability, readability and evolution.

## Project Interpretation

These concerns are **mechanism-independent**.

IsHandled is treated as a representative case study demonstrating
behaviour-changing customization.

This document intentionally avoids claiming that these concerns are
unique to IsHandled.

---

# Representative Empirical Validation

Representative analysis of BC280 Czech localization applications
supports Microsoft's published concerns.

Observed recurring patterns include:

- responsibility transfer,
- competing subscribers,
- dead-end events,
- reduced effective extensibility,
- discoverability problems.

Detailed evidence is intentionally maintained in separate empirical
study documents so this reference remains stable across Business Central
releases.

---

# Relationship to the Behavior Change Review Framework

The document supports the framework by identifying candidate review
themes:

- Responsibility
- Composition
- Explicit Contracts
- Discoverability
- Evolution
- Extensibility

The framework itself is documented separately and is not defined here.

---

# Findings

## Accepted

- Microsoft discourages new broad IsHandled events.
- Microsoft's guidance targets architectural consequences.
- Representative empirical evidence supports Microsoft's observations.

## Candidate

- Effective Extensibility as a Business Central evaluation concern.
- Mechanism-independent review questions.

## Rejected

- The claim that IsHandled alone requires a unique architecture theory.

## Open

- Validation across additional Microsoft applications.
- Validation across ISV ecosystems.
- Objective review thresholds.

---

# References

## Primary

- Microsoft Learn – Using the IsHandled pattern for events
- Microsoft Learn – Using IsHandled minimum requirements
- Microsoft Learn – Types of events for extensibility
- Microsoft Learn – Create an extensibility request

## Related Repository References

- [[ISO_42010]]
- [[ISO_42020]]
- [[ISO_42030]]
- [[Microsoft_Extensibility_Overview]]
- [[Microsoft_Event_Types]]
- [[Microsoft_Interfaces]]

---

# Revision History

## 1.0

First consolidated reference edition. Reorganized previous iterative
drafts into a single topic-focused document following the philosophy of
the ISO reference documents while keeping empirical studies and broader
framework material separate.
