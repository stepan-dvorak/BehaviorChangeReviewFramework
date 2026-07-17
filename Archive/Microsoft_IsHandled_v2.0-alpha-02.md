
---
status: working-draft
target: Microsoft_IsHandled_v2.0
iteration: 2.0-alpha-02
---

# Microsoft_IsHandled

> Working draft toward version 2.0.

# 1–5

(Identical to alpha-01; omitted here for brevity in this working iteration.)

---

# 6. Microsoft's Current Position

## Overview

Microsoft's current documentation presents a remarkably consistent message.
The IsHandled pattern remains a supported extensibility mechanism, but it is
no longer treated as the preferred solution for introducing new extension
points.

Instead, Microsoft promotes explicit architectural contracts through focused
events, interfaces and extensibility requests.

The guidance is evolutionary rather than revolutionary: existing handled
events continue to exist, while new ones are expected to satisfy much higher
architectural expectations.

## Normative Evidence

Across the Microsoft Learn articles *Using the IsHandled pattern for events*,
*IsHandled minimum requirements*, *Types of events* and *Extensibility
Requests*, several recommendations recur:

- avoid introducing broad IsHandled events whenever possible;
- prefer explicit extension points;
- prefer interfaces when selecting behaviour;
- submit extensibility requests instead of introducing generic overrides;
- justify every new IsHandled event against explicit criteria.

Although phrased differently, these recommendations consistently discourage
using IsHandled as the default extensibility mechanism.

## Research Interpretation

A superficial reading suggests Microsoft is discouraging a programming
pattern.

A deeper architectural reading suggests something different.

The recommendations consistently address qualities such as:

- maintainability,
- composability,
- discoverability,
- long-term evolution,
- extensibility.

These are architectural quality attributes rather than implementation
details.

Consequently, the real review target appears to be **architectural
consequences of behaviour replacement**, not the IsHandled mechanism itself.

## Confidence Assessment

| Statement | Confidence |
|-----------|------------|
| Microsoft discourages new broad IsHandled events. | Normative |
| Microsoft prefers explicit contracts. | Normative |
| The underlying concern is architectural rather than syntactic. | Empirically Supported / Candidate |

---

# 7. Detailed Analysis

## 7.1 Turning Off Parts of the Code

### Microsoft Position

Replacing standard execution may bypass future platform behaviour.

### Microsoft Evidence

Microsoft repeatedly warns that setting `IsHandled := true` may prevent the
remaining implementation from executing. This includes not only today's
business logic but also future additions to the Base Application.

The warning is intentionally broader than "skipping code"; it includes every
future responsibility attached to the skipped execution path.

### Representative Empirical Evidence

The BC280 localization analyses contain multiple examples classified as FULL
OVERRIDE.

These implementations replace substantial portions of standard posting or
processing logic. The resulting extensions become responsible for preserving
behaviour that would otherwise be inherited automatically from Microsoft.

Representative observations include:

- replacement of posting behaviour,
- replacement of disposal processing,
- replacement of validation sequences.

These examples demonstrate the architectural situation described by
Microsoft, regardless of whether the customization itself is justified.

### Research Interpretation

The key architectural observation is **responsibility transfer**.

When execution is replaced, responsibility also moves.

This includes responsibility for:

- business rules,
- validation,
- transaction boundaries,
- event publication,
- telemetry,
- future platform evolution.

Therefore, the review question is not:

> Was code skipped?

Instead it becomes:

> Which architectural responsibilities changed ownership?

This interpretation generalizes beyond IsHandled and may therefore become a
candidate review principle for other behaviour-changing mechanisms.

### Counterarguments

Some scenarios legitimately require complete replacement because no suitable
extension point exists.

Microsoft explicitly acknowledges such situations by continuing to support
the IsHandled pattern and by providing an extensibility request process.

The architectural issue is therefore proportionality rather than prohibition.

### Framework Implication

Candidate review questions:

- Which responsibilities are transferred?
- Are transferred responsibilities documented?
- Can they be tested independently?
- Does the replacement preserve future extensibility?

### Threats to Validity

Current empirical validation is based primarily on Microsoft localization
applications. Behaviour in independent ISV products may differ.

### Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Responsibility Transfer concept | Candidate |

---

## 7.2 Fragile Evolution

### Microsoft Position

Future Base Application improvements may never execute through replaced
execution paths.

### Microsoft Evidence

Microsoft encourages explicit extension points because they allow future
behaviour to remain inside the platform while enabling controlled
customization.

Broad execution replacement interrupts this evolution.

### Representative Empirical Evidence

Representative override implementations observed in BC280 require developers
to monitor Microsoft changes independently after every platform upgrade.

Whenever Microsoft extends the original execution path, extension authors
must manually determine whether equivalent behaviour should also be added to
their replacement implementation.

### Research Interpretation

This concern is frequently described as an upgrade problem.

The evidence suggests a broader interpretation.

The architectural issue is ownership of behavioural evolution.

Once execution diverges, Microsoft and the extension evolve independently.

This divergence may remain invisible until new functionality, regulations or
business rules expose behavioural differences.

The review question therefore becomes:

> Who owns future behaviour?

rather than:

> Who owns today's implementation?

### Counterarguments

Not every replacement becomes fragile.

Small, deterministic replacements with clearly bounded scope may remain
stable across many releases.

Framework reviews should therefore evaluate degree of coupling instead of
assuming every override is equally risky.

### Framework Implication

Candidate review questions:

- How tightly coupled is the replacement?
- Who reviews behavioural divergence?
- What triggers reassessment after upgrades?
- Can divergence be measured?

### Threats to Validity

Longitudinal studies across several Business Central versions have not yet
been completed.

### Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Evolution Ownership concept | Candidate |

---

# Next Iteration

alpha-03 will complete:

- 7.3 Low Readability
- 7.4 Single Subscriber Assumption
- 7.5 Coding by Convention
- 7.6 Extensibility Degradation

using the same analytical structure established in this iteration.
