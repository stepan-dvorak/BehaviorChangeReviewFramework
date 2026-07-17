---
status: draft
version: 0.4
project: Behavior Change Review Framework
source-type: Microsoft Learn
depends-on:
  - 03_Related_Work
  - ISO_42010
  - ISO_42020
  - ISO_42030
---

# Microsoft_IsHandled.md

> Iteration **0.4** – Research Reference Draft

# Purpose

This note analyzes Microsoft's current guidance on the **IsHandled**
pattern as a representative case of architecturally significant
behavior-changing customization.

It intentionally distinguishes between:

- **Microsoft Position**
- **Evidence**
- **Analysis**
- **Research Implications**
- **Findings**

The objective is not to evaluate `IsHandled` itself, but to determine
whether Microsoft's guidance can be generalized into a
mechanism-independent **Behavior Change Review Framework**.

---

# Executive Assessment

## Microsoft Position

Microsoft discourages creating new broad `IsHandled` events and
recommends explicit extensibility mechanisms such as interfaces and
well-designed events whenever practical.

## Analysis

Microsoft's criticism consistently targets architectural consequences
rather than AL syntax.

Recurring concerns include:

- composability,
- readability,
- discoverability,
- evolution,
- upgrade compatibility,
- maintainability.

## Working Research Hypothesis

These concerns may characterize **behavior-changing customizations in
general**, regardless of whether they are implemented using IsHandled,
interfaces, strategies, workflow engines or future extensibility
mechanisms.

Status: **Candidate**

---

# Historical Context

## NAV Era

The Handled pattern originated when NAV provided limited extensibility.
Replacing behavior through handled events was often the only practical
alternative to object modifications.

## Community Evolution

### Mark Brummel

Historically associated with early promotion of the Handled pattern.

**Research note**

Historical context only. Not treated as normative evidence.

### Vjekoslav Babić

Important historical articles:

- Gentleman's Agreement Pattern
- Codeunit Interfaces in AL

These document the transition from convention-based extensibility to
contract-based extensibility.

---

# Microsoft's Architectural Evolution

A chronological reading of Microsoft Learn suggests a gradual shift:

1. Enable extensibility.
2. Improve event quality.
3. Reduce broad replacement events.
4. Prefer explicit contracts.
5. Encourage extensibility requests instead of new generic handled events.

This appears to be an architectural evolution rather than a language
feature evolution.

---

# Detailed Analysis of Microsoft Criticisms

## 1. Single Subscriber Assumption

### Microsoft Position

Replacement assumes one subscriber owns the continuation.

### Architectural Interpretation

Composition becomes increasingly difficult as independent extensions are
introduced.

### Candidate Review Questions

- Can independent extensions coexist?
- Is execution deterministic?

Status: Candidate

---

## 2. Coding by Convention

### Microsoft Position

Correct behavior depends on convention rather than explicit contracts.

### Analysis

Interfaces move behavioral expectations into the type system.

### Candidate Review Question

Can the expected behavior be verified without documentation?

---

## 3. Turning Off Parts of the Code

### Microsoft Position

> "The main problem is skipping large parts of code..."

(Short quotation reproduced for discussion.)

### Analysis

This criticism concerns **responsibility transfer** rather than merely
skipping statements.

Potentially affected concerns:

- invariants,
- downstream events,
- telemetry,
- transactions,
- extension participation.

### Candidate Review Questions

- Which responsibilities disappear?
- Which responsibilities become extension-owned?
- Are replacement responsibilities documented?

Status: Accepted

---

## 4. Low Readability

### Microsoft Position

Effective execution becomes difficult to understand.

### Analysis

Behavior becomes distributed across subscribers.

### Candidate Review Question

Can another maintainer reconstruct effective behavior with reasonable
effort?

---

## 5. Fragile Evolution

### Microsoft Position

Future Base Application improvements may no longer execute.

### Analysis

Every replacement increases long-term synchronization effort.

### Candidate Review Question

What is the upgrade strategy after Microsoft modifies the original flow?

---

## 6. Extensibility Degradation

### Microsoft Position

Broad replacement reduces opportunities for later extension.

### Analysis

Technical extension points may remain available while practical
participation disappears.

### Research Note

This observation aligns with the project's candidate concept of
**Effective Extensibility**.

Status: Candidate

---

# Architectural Interpretation

## What Microsoft Explicitly States

Microsoft recommends replacing broad handled events with richer
extensibility mechanisms whenever practical.

Microsoft also documents review criteria before introducing new handled
events.

## What This Project Concludes

Current evidence suggests Microsoft already performs an implicit
architectural evaluation.

The published criteria appear suitable for generalization beyond
IsHandled.

This remains a research hypothesis until validated against ISO
architecture standards and additional Business Central mechanisms.

---

# Candidate Behavior Change Review Mapping

| Microsoft Observation | Architectural Concern | Candidate Review Question |
|---|---|---|
| Single subscriber | Composition | Can extensions coexist safely? |
| Coding by convention | Explicit contracts | Is expected behavior formally expressed? |
| Turning off code | Behavioral completeness | Which responsibilities disappear? |
| Low readability | Understandability | Can effective behavior be reconstructed? |
| Fragile evolution | Evolution | How are future Microsoft changes inherited? |
| Extensibility degradation | Ecosystem extensibility | Does the extension remain effectively extensible? |

---

# Relationship to ISO Research

Current assessment after reviewing ISO 42010:

Microsoft guidance appears operational.

ISO standards provide general architectural concepts such as:

- stakeholders,
- concerns,
- architecture views,
- decisions,
- correspondences.

The project hypothesis is that Microsoft guidance can become a Business
Central specialization of these broader concepts.

Status: Under Investigation.

---

# Planned Base Application Evidence

Future iterations should attach examples illustrating each criticism:

- Base Application
- System Application
- Czech Localization
- Alternative interface implementations

This section intentionally remains a placeholder until evidence has been
reviewed.

---

# Findings

## Accepted

- Microsoft discourages broad IsHandled usage.
- Microsoft evaluates architectural consequences.
- Microsoft's recommendations increasingly favor explicit contracts.

## Candidate

- Microsoft guidance can be generalized into mechanism-independent review
  questions.
- Effective Extensibility may become an important architectural concern.

## Open

- Which review questions should be mandatory?
- Does ISO 42030 already cover part of the evaluation process?
- Which Business Central mechanisms require additional review criteria?

---

# Planned Expansion (Version 0.5)

- Complete Microsoft Learn section references.
- Evidence tables with exact article sections.
- Historical timeline.
- Base Application examples.
- Czech Localization examples.
- Direct comparison:
  - IsHandled
  - Interfaces
  - Strategy
  - Delegation
- Candidate review checklist.

# Revision History

## 0.4

Expanded into a structured analytical research note with explicit
architectural interpretation, six analyzed Microsoft criticisms,
candidate mapping toward the Behavior Change Review Framework, and
preparation for evidence-driven case studies.
