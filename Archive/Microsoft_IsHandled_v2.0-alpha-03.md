
---
status: working-draft
target: Microsoft_IsHandled_v2.0
iteration: 2.0-alpha-03
---

# Microsoft_IsHandled

> Working draft toward version 2.0.

This iteration completes the analysis of Microsoft's remaining published
criticisms of the IsHandled pattern using the analytical structure
established in alpha-02.

---

# 7.3 Low Readability

## Microsoft Position

Microsoft identifies reduced readability as one of the principal
disadvantages of the IsHandled pattern.

The concern appears repeatedly throughout Microsoft's recommendations to
prefer explicit extension points over broad execution replacement.

## Microsoft Evidence

The official guidance explains that understanding the final execution
becomes increasingly difficult once multiple subscribers participate in
behaviour selection.

The effective implementation is no longer represented by the publisher
alone.

## Representative Empirical Evidence

The analysed BC280 localization applications contain subscribers that
replace or significantly modify standard execution.

Understanding effective runtime behaviour requires developers to examine:

- the original publisher,
- subscriber ordering,
- additional event publishers,
- extension-specific implementation,
- skipped standard execution.

No single source describes the complete behavioural flow.

## Research Interpretation

The term *readability* appears to understate Microsoft's actual concern.

From an architectural perspective the more fundamental issue is
**discoverability**.

Architecture should enable reviewers to answer questions such as:

- Where does behaviour actually execute?
- Which component owns the decision?
- Which execution path becomes effective?

When those questions require manual reconstruction across multiple
applications, discoverability decreases even if the individual source code
remains readable.

The concern therefore extends beyond programming style.

It affects:

- maintenance,
- debugging,
- architecture reviews,
- onboarding,
- behavioural documentation.

## Counterarguments

Large event-driven systems naturally distribute behaviour.

Reduced locality is therefore not automatically an architectural defect.

The review question becomes whether the resulting behaviour remains
discoverable through explicit contracts, documentation or tooling.

## Framework Implication

Candidate review questions:

- Can effective behaviour be reconstructed?
- Which architectural artifacts document runtime behaviour?
- Can ownership be identified without source-code exploration?

## Threats to Validity

Current empirical observations originate primarily from Microsoft
applications.

Different discoverability characteristics may exist in smaller extensions.

## Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Discoverability interpretation | Candidate |

---

# 7.4 Single Subscriber Assumption

## Microsoft Position

Broad handled events frequently assume one effective implementation.

## Microsoft Evidence

Microsoft recommends avoiding broad IsHandled events because multiple
independent extensions cannot reliably coordinate ownership through
implicit subscriber behaviour.

## Representative Empirical Evidence

The BC280 localization studies identified several situations where
independent subscribers target identical posting pipelines.

Although each implementation is individually correct, architectural
composition becomes increasingly dependent upon execution ordering and
behavioural assumptions.

These observations correspond directly to Microsoft's concern.

## Research Interpretation

The architectural issue is **composition**, not subscriber count.

Modern Business Central environments frequently contain:

- Microsoft applications,
- localization applications,
- AppSource applications,
- customer extensions.

Each may legitimately participate in one business process.

Consequently architecture should evaluate whether independently developed
behaviour can compose without implicit ownership assumptions.

## Counterarguments

Some business processes intentionally require one authoritative decision.

The architectural review should therefore distinguish exclusive ownership
from accidental exclusivity.

## Framework Implication

Candidate review questions:

- Can multiple extensions participate?
- Is behavioural ownership explicit?
- Does execution depend upon ordering?

## Threats to Validity

Representative empirical evidence currently focuses on Microsoft
localizations rather than large AppSource ecosystems.

## Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Composition interpretation | Candidate |

---

# 7.5 Coding by Convention

## Microsoft Position

Correct behaviour should not depend upon undocumented conventions between
extensions.

## Microsoft Evidence

Microsoft increasingly recommends interfaces and explicit extension points
instead of convention-based behavioural replacement.

## Representative Empirical Evidence

Several analysed subscribers rely upon assumptions such as:

- who sets IsHandled,
- who executes first,
- which subscriber becomes authoritative,
- which downstream behaviour remains available.

These assumptions are rarely represented explicitly.

## Research Interpretation

This criticism extends beyond coding style.

The underlying architectural concern is **explicit behavioural contracts**.

Explicit contracts improve:

- reviewability,
- discoverability,
- governance,
- compatibility,
- evolution.

Interfaces represent one implementation of explicit contracts, but the
architectural concern itself is mechanism-independent.

## Counterarguments

Conventions remain valuable within small coordinated teams.

Problems emerge primarily when independently evolving applications must
cooperate.

## Framework Implication

Candidate review questions:

- Which behavioural assumptions remain implicit?
- Can contracts be expressed explicitly?
- Can contract violations be detected?

## Threats to Validity

Current observations focus primarily on event-based architecture.

Additional mechanisms should be investigated.

## Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Explicit Contract interpretation | Candidate |

---

# 7.6 Extensibility Degradation

## Microsoft Position

Broad execution replacement may reduce future extensibility.

## Microsoft Evidence

Microsoft explicitly recommends requesting new extension points instead of
introducing increasingly generic IsHandled events.

This recommendation implies that extensibility quality depends not merely
on the existence of extension points but also on their architectural
effectiveness.

## Representative Empirical Evidence

The BC280 studies identified several situations classified as:

- DEAD-END EVENT
- FULL OVERRIDE
- EXTENSIBILITY BREAK

In these situations additional subscribers become technically possible but
architecturally impractical because previous behaviour replacement has
already assumed effective ownership.

## Research Interpretation

These observations motivated the working concept of
**Effective Extensibility**.

Technical extensibility answers:

> Can another extension subscribe?

Effective extensibility asks:

> Can another extension still participate meaningfully?

This distinction may become one of the most significant architectural
findings emerging from the IsHandled research.

## Counterarguments

The Effective Extensibility concept currently remains a research proposal.

Broader validation is required before treating it as an established
architectural property.

## Framework Implication

Candidate review questions:

- Does extensibility remain practically usable?
- Which extension points become architectural dead ends?
- Can future behaviour still compose?

## Threats to Validity

Current evidence originates from representative Microsoft localization
applications.

Cross-validation with AppSource applications remains future work.

## Confidence Assessment

| Layer | Confidence |
|------|------------|
| Microsoft guidance | Normative |
| Empirical recurrence | Empirically Supported |
| Effective Extensibility | Candidate |

---

# Next Iteration

alpha-04 will complete the synthesis chapters:

- Cross-cutting Architectural Themes
- Representative Empirical Validation
- Relationship to Behavior Change Review Framework
- Threats to Validity
- Conclusions
- References

These chapters will integrate all previous analyses into a coherent
reference approaching the final 2.0 document.
