---
status: final-draft
version: 2.0
type: reference
title: Microsoft_IsHandled
project: Behavior Change Review Framework
source-type:
  - Microsoft Learn
  - empirical-analysis
depends-on:
  - 00_Project_Charter
  - 01_Terminology
  - 02_Research_Methodology
  - 03_Related_Work
  - ISO_42010
  - ISO_42020
  - ISO_42030
  - SEI_Documenting_Behavior
  - Microsoft_Extensibility_Overview
---

# Microsoft_IsHandled

> Reference analysis of Microsoft's guidance on the `IsHandled` pattern in
> Dynamics 365 Business Central.
>
> This document examines one extensibility mechanism as a representative case
> study. It does not define the Behavior Change Review Framework and does not
> treat `IsHandled` as the research subject.

# 1. Purpose

The purpose of this reference is to:

- document Microsoft's current guidance for the `IsHandled` pattern;
- distinguish official Microsoft guidance from empirical observation and
  repository interpretation;
- compare Microsoft's stated concerns with representative evidence from
  Business Central 2025 release wave 2 (BC280) localization applications;
- identify architectural concerns that remain relevant independently of the
  `IsHandled` mechanism;
- provide traceable inputs for the future Behavior Change Review Framework.

The document deliberately studies a single implementation mechanism in depth.
The intended contribution is not another catalogue of AL patterns. It is a
structured analysis of what happens architecturally when an extension replaces,
suppresses or redirects established application behaviour.

# 2. Scope

## 2.1 Included

This document includes:

- the historical role of the Handled pattern;
- Microsoft's current published position;
- Microsoft's documented disadvantages and alternatives;
- representative empirical validation from BC280 Czech localization
  applications;
- architectural interpretation of recurring concern categories;
- mechanism-independent candidate review questions;
- limitations and threats to validity.

## 2.2 Excluded

This document does not include:

- a complete catalogue of all `IsHandled` occurrences;
- statistical claims about the entire Business Central ecosystem;
- a complete design-pattern replacement guide;
- the definition of the Behavior Change Review Framework;
- a general treatment of interfaces, workflows or event architecture;
- a full ISO or SEI architecture analysis.

Those subjects remain in separate repository documents.

# 3. Research Method

The analysis separates four evidence layers.

## 3.1 Layer 1 — Microsoft Guidance

Statements explicitly documented in Microsoft Learn.

These statements are treated as normative within the Business Central
development context, but they are not generalized beyond that context without
additional evidence.

## 3.2 Layer 2 — Empirical Observation

Representative observations from the following BC280 Microsoft localization
applications:

- Core Localization Pack for Czech (CZL);
- Fixed Asset Localization for Czech (CZF).

The empirical reports identify subscribers with a `var IsHandled: Boolean`
parameter that assign `IsHandled := true`, and classify their behavioural
effects.

## 3.3 Layer 3 — Research Interpretation

Architectural interpretation derived from Microsoft guidance and empirical
observations.

Repository-specific concepts are explicitly marked as candidate concepts
rather than attributed to Microsoft.

## 3.4 Layer 4 — Framework Implication

Mechanism-independent questions that may later become review criteria in the
Behavior Change Review Framework.

The questions are outputs of this reference, not yet accepted framework rules.

# 4. Evidence Classification

| Classification | Meaning |
|---|---|
| Normative | Explicitly documented Microsoft guidance. |
| Empirically Supported | Observed in the analysed BC280 applications. |
| Candidate | Plausible repository interpretation requiring broader validation. |
| Open | Not yet resolved by available evidence. |

Empirical evidence validates the presence of concern categories. It does not
prove Microsoft's recommendations universally and does not establish
prevalence across all Business Central extensions.

# 5. Terminology

## 5.1 Mechanism

A technical implementation technique used to alter or extend behaviour.

Examples include:

- `IsHandled`;
- regular integration events;
- interfaces;
- strategy selection;
- workflow interception;
- delegation;
- replacement modules.

## 5.2 Behaviour-changing customization

A customization that changes the effective runtime behaviour of an existing
business capability.

A behaviour-changing customization may:

- replace an execution path;
- suppress validation;
- redirect processing;
- change a decision;
- alter ordering;
- prevent existing participants from executing.

## 5.3 Effective behaviour

The behaviour that actually executes in a deployed environment after all
platform, application and extension participation is considered.

## 5.4 Responsibility Transfer

A candidate repository concept describing the transfer of responsibility from
the replaced implementation to the replacing implementation.

Transferred responsibility can include:

- business rules;
- validation;
- side effects;
- transaction semantics;
- event publication;
- telemetry;
- error behaviour;
- future behavioural evolution.

## 5.5 Evolution Ownership

A candidate repository concept describing responsibility for tracking and
incorporating future changes after a replacement implementation diverges from
the Base Application.

## 5.6 Discoverability

The ability to reconstruct effective behaviour, identify participating
components and determine where behavioural decisions are made.

Microsoft uses the term *readability*. This document uses *discoverability*
when the concern extends beyond local source-code readability.

## 5.7 Explicit Contract

An explicit representation of permitted participation, responsibilities,
inputs, outputs and behavioural expectations.

Interfaces are one implementation of an explicit contract, but the concept is
mechanism-independent.

## 5.8 Effective Extensibility

A candidate repository concept distinguishing technical availability of an
extension point from the practical ability of additional extensions to
participate meaningfully in the effective behaviour.

Technical extensibility asks:

> Can another extension subscribe or implement the mechanism?

Effective Extensibility asks:

> Can another extension still influence or extend the behaviour that actually
> executes?

# 6. Historical Evolution

The Handled pattern emerged as a practical response to limited extensibility
options in Microsoft Dynamics NAV and early Business Central application
architecture.

The original pattern enabled code to request an implementation that did not
exist in the publisher. An event was raised and the publisher could fail when
no subscriber supplied the implementation. In that role, the pattern provided
interface-like behaviour before AL supported interfaces directly.

Over time, usage shifted. The Boolean flag increasingly became a means of
overriding existing code:

```al
OnBeforeOperation(IsHandled);
if IsHandled then
    exit;

StandardOperation();
```

A subscriber could execute replacement logic and stop the publisher:

```al
if IsHandled then
    exit;

ExecuteReplacement();
IsHandled := true;
```

Compared with direct source modification, this was an important improvement.
Customer or localization behaviour could remain outside the Base Application,
which supported upgrades and separated extension code from Microsoft code.

The mechanism nevertheless retained an implicit winner-takes-all contract.
Only one subscriber was expected to handle the operation, and all other
subscribers were expected to observe the Boolean and exit.

Business Central later gained richer extensibility mechanisms:

- focused integration events;
- interfaces;
- enum-based implementation selection;
- extension objects;
- explicit feature and service abstractions;
- formal extensibility requests;
- code contributions to the open-source applications.

Microsoft's current guidance therefore does not simply reverse the earlier
design. It narrows the circumstances in which a new handled event is justified.
The architectural direction has shifted from enabling replacement at almost
any point toward defining explicit, maintainable and composable extension
contracts.

# 7. Microsoft's Current Position

Microsoft describes `IsHandled` as widely used and popular for overriding
code, but recommends limiting it to a bare minimum and using it only where no
better pattern is available.

The official guidance makes several points explicit:

- the original goal was to supply a missing implementation;
- current usage frequently overrides existing code;
- the pattern assumes a single effective subscriber;
- its rules are enforced only by convention;
- handled events often lack a clear semantic purpose;
- they introduce nesting and additional code paths;
- they can turn off large portions of code;
- skipped code may contain events, validation or future improvements;
- better alternatives usually include proper concepts, interfaces, focused
  events, redesigned flows, extension objects or separate functionality;
- new handled-event requests must justify why those alternatives are
  insufficient;
- any unavoidable handled event should be narrowly scoped and leave a minimal,
  predictable remaining code path.

Microsoft's position is therefore stronger than a stylistic preference.
`IsHandled` is a last-resort extensibility mechanism whose introduction now
requires explicit architectural justification.

## 7.1 Normative sources

- [Using the IsHandled pattern for events](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-pattern)
- [Minimum requirements for new IsHandled events](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-min-req)
- [Create an extensibility request](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/create-extensibility-request)
- [Types of events for extensibility](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/types-of-events-for-extensibility)

## 7.2 Research interpretation

Microsoft frames the guidance around one programming pattern, but the stated
risks concern architectural qualities:

- responsibility;
- evolution;
- discoverability;
- composition;
- explicitness of contracts;
- preservation of extensibility.

The actual review target is therefore broader than the Boolean parameter. It is
the architectural consequence of replacing established behaviour.

Confidence: **Candidate**, supported by normative guidance and representative
empirical evidence.

# 8. Analysis of Microsoft's Criticisms

# 8.1 Turning Off Parts of the Code

## Microsoft Position

Using `IsHandled` as an override mechanism can turn off large portions of
standard code and produce fragile solutions.

Microsoft specifically identifies three recurring risks:

- refactoring around the event can break subscribers;
- events inside the skipped code may no longer be raised;
- skipped validation may permit unsupported or inconsistent data.

Microsoft recommends not turning off validation and, when replacement cannot
be avoided, turning off as little code as possible.

## Microsoft Evidence

The official guidance distinguishes broad replacement from narrowly scoped
extension points. Its preferred alternative is a positive event with a clear
purpose that changes a specific input, decision or operation without removing
the surrounding standard behaviour.

Microsoft's example replaces a generic handled event that could skip an entire
uniqueness validation with an event that only adds filters. Required filters
remain protected and the validation still executes.

The architectural intent is clear:

- retain the standard responsibility where possible;
- expose the smallest meaningful variation point;
- keep skipped behaviour visible and bounded;
- preserve downstream events and validations.

## Representative BC280 Example

**CZF Finding #13**

- Application: Fixed Asset Localization for Czech.
- Object: `Codeunit 31235 "FA Disposal Handler CZF"`.
- Publisher event: `OnBeforeFAInsertGLAccount`.
- Observed behaviour: the subscriber completely replaces part of the
  FA Insert G/L Account flow, including disposal correction and book-value
  correction, and then sets `IsHandled := true`.
- Classification: **FULL OVERRIDE**.
- Reported impact: extensibility break and high regression risk.

This is a representative example of substantial standard processing being
replaced by one subscriber. The example may be functionally justified by
localization requirements, but the replacing extension becomes responsible
for the complete effective flow that it executes.

## Research Interpretation

The architectural concern is **Responsibility Transfer**, not merely skipped
lines.

When a subscriber replaces a non-trivial execution path, it also assumes
responsibility for whatever the original path provided:

- correct account selection;
- disposal corrections;
- book-value corrections;
- validation;
- ordering;
- transaction behaviour;
- publication of downstream events;
- compatibility with future Base Application changes.

The relevant review question is therefore:

> Which responsibilities changed owner when the standard path was replaced?

This question applies equally to interface replacement, workflow replacement
or a new posting module. The risk is caused by behavioural replacement, not by
the syntax of `IsHandled`.

## Counterarguments

Complete replacement can be legitimate.

Localization law, incompatible accounting rules or a fundamentally different
business process can require an implementation that cannot be expressed as a
small extension of standard behaviour.

Microsoft's guidance recognizes this possibility by retaining the pattern,
supporting separate implementations and providing an extensibility request
process.

The architectural issue is proportionality:

- Is the replaced scope larger than necessary?
- Is the boundary explicit?
- Are transferred responsibilities documented and tested?
- Does the replacement preserve suitable participation points?

## Framework Implication

Candidate review questions:

- What standard behaviour is no longer executed?
- Which responsibilities transfer to the extension?
- Are validation and side effects preserved intentionally?
- Which downstream events stop being raised?
- Is the replacement boundary the smallest viable boundary?
- Is replacement behaviour independently testable?
- Does the replacement preserve further extensibility?

## Threats to Validity

The representative example comes from a Microsoft localization application,
where legal requirements can justify stronger replacement than in ordinary
customer extensions.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft concern | Normative |
| BC280 occurrence | Empirically Supported |
| Responsibility Transfer | Candidate |

# 8.2 Fragile Evolution

## Microsoft Position

A handled subscriber can depend on the exact context before and after an event.
Refactoring the Base Application can therefore break the subscriber even if
the event signature remains unchanged.

Broad replacement also prevents new standard behaviour from reaching the
effective execution path.

## Microsoft Evidence

Microsoft recommends explicit concepts and focused extension points because
they allow the platform to evolve while retaining controlled extension
participation.

The minimum requirements for a new handled event demand an explanation of why
future evolution will not be hindered, which alternatives were evaluated and
how multi-extension risks are mitigated.

This places evolution directly inside the design review of the extension
point.

## Representative BC280 Example

**CZF Finding #13** is also representative of fragile evolution.

The fixed-asset disposal subscriber reproduces a substantial portion of
posting behaviour. If Microsoft later changes:

- account-resolution rules;
- insertion order;
- disposal correction behaviour;
- book-value correction behaviour;
- validation or telemetry;
- events inside the standard flow;

the replacement path does not inherit those changes automatically.

The extension author must compare each relevant Base Application change with
the replacement implementation and decide whether equivalent behaviour is
required.

## Research Interpretation

This is broader than an upgrade problem. The architectural concern is
**Evolution Ownership**.

Before replacement, Microsoft owns evolution of the standard behaviour.
After replacement, two behavioural lines exist:

- the evolving Base Application path;
- the independently evolving extension path.

Divergence may remain invisible until a new feature, regulatory change, error
condition or interacting extension exposes it.

The review question becomes:

> Who owns future evolution of the effective behaviour?

rather than only:

> Will the code compile after an upgrade?

Compilation compatibility is insufficient. The effective behaviour can remain
syntactically valid while becoming semantically outdated.

## Counterarguments

Not every replacement is highly evolution-sensitive.

A small deterministic operation with a stable explicit contract can remain
independent for many releases. A separate implementation may even be safer
than many invasive extension points.

Review should therefore assess:

- size of the replaced responsibility;
- coupling to standard internal context;
- rate of change of the Base Application area;
- regulatory and transactional significance;
- availability of behavioural regression tests.

## Framework Implication

Candidate review questions:

- Which Base Application changes must be monitored?
- Who is responsible for behavioural comparison after upgrades?
- Is the replacement coupled to internal sequencing or local variables?
- What event triggers reassessment?
- Can divergence be detected through automated tests or telemetry?
- Is the replacement versioned as an explicit implementation?

## Threats to Validity

The current evidence is structural. A longitudinal comparison of the same
subscribers across multiple Business Central releases has not yet been
completed.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft concern | Normative |
| Independent evolution requirement | Empirically Supported |
| Evolution Ownership | Candidate |

# 8.3 Low Readability and Discoverability

## Microsoft Position

`IsHandled` introduces nesting and additional code paths. When many handled
events exist, it becomes difficult to understand which code will execute and
how.

Microsoft also criticizes handled events whose names describe a code location
or skipped line rather than a clear business purpose.

## Microsoft Evidence

Microsoft's preferred event designs use semantically positive names and narrow
purposes. A focused event should make clear:

- what operation is being extended;
- what subscribers are permitted to change;
- what behaviour remains guaranteed;
- where refactoring is safe.

The current guidance explicitly connects unclear purpose with difficult
troubleshooting, instability and difficult refactoring.

## Representative BC280 Example

**CZF Finding #13**

Understanding the effective fixed-asset disposal behaviour requires reading:

1. the Base Application publisher and its surrounding code;
2. the event contract;
3. the localization subscriber;
4. the disposal correction branch;
5. the book-value correction branch;
6. the point where `IsHandled` becomes true;
7. any downstream events omitted by the replacement.

No single source artifact expresses the complete effective posting path.

A second representative form appears in CZL posting handlers, where business
logic is distributed across multiple subscribers to `Inventory Posting To G/L`
events. Reconstructing behaviour requires examining publisher context,
subscriber conditions and competing localization responsibilities.

## Research Interpretation

*Readability* understates the architectural concern.

Individual AL procedures may remain readable while the effective behaviour is
difficult to discover. The broader concern is **Discoverability**.

Architecture review requires answers to questions such as:

- Where does the effective behaviour execute?
- Which component makes the replacement decision?
- Which implementation owns the result?
- Which standard stages remain active?
- Which extension events remain reachable?

If those answers require manual reconstruction across applications, the
system has a discoverability problem even when each individual method is
locally clear.

This interpretation aligns with SEI guidance that behaviour should be
represented through appropriate architectural views and models. A source-code
listing is not necessarily a sufficient behavioural description.

## Counterarguments

Distributed behaviour is normal in event-driven architecture.

Low locality is not automatically a defect. Multiple independent subscribers
can provide valuable modularity when the event contract is clear and
participation is additive.

The review issue is whether effective behaviour remains discoverable through:

- explicit contracts;
- naming;
- architecture documentation;
- behaviour views;
- tests;
- diagnostic tooling;
- traceable orchestration.

## Framework Implication

Candidate review questions:

- Can effective behaviour be reconstructed without reverse engineering?
- Is the replacement boundary visible?
- Does the event name express business intent rather than code location?
- Which architecture artifact documents the effective behaviour?
- Can debugging identify the authoritative implementation?
- Are omitted standard stages and events documented?

## Threats to Validity

Discoverability is partly affected by repository structure, tooling and team
knowledge. The same implementation may be easier to understand in a small
coordinated team than in a multi-vendor environment.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft readability concern | Normative |
| Distributed behaviour in BC280 | Empirically Supported |
| Discoverability interpretation | Candidate |

# 8.4 Single Subscriber Assumption

## Microsoft Position

The pattern assumes that only one subscriber handles the event.

Every subscriber is expected to:

1. check whether `IsHandled` is already true;
2. exit when another subscriber has handled the operation;
3. perform the implementation only when still unhandled;
4. set `IsHandled := true` after handling.

This behaviour conflicts with the normal event model, where all subscribers
are notified and may react independently.

## Microsoft Evidence

Microsoft states that handled subscribers are optional and should allow
another subscriber to perform the task. It also requires new event requests to
describe risks when multiple extensions subscribe and explain how ordering or
conflicts are mitigated.

The official alternatives prefer event types that support additive
participation or explicit selection of one implementation.

## Representative BC280 Example

The CZL analysis identified three critical collisions in
`Inventory Posting To G/L`:

1. `OnBeforeBufferPurchPosting`
   - `CorrectionsPostingMgtCZL`
   - `InventoryPostingHandlerCZL`

2. `OnBeforeBufferSalesPosting`
   - `CorrectionsPostingMgtCZL`
   - `InventoryPostingHandlerCZL`

3. `OnBeforeBufferOutputPosting`
   - `CorrectionsPostingMgtCZL`
   - `InventoryPostingHandlerCZL`

Each pair represents two legitimate localization responsibilities targeting
the same handled event:

- expected-cost correction;
- localization-specific rounding or posting behaviour.

The report identifies risks including order-dependent execution, hidden
coupling, skipped logic and variable accounting outcomes.

The purchase-posting collision is used here as the representative example.

## Research Interpretation

The architectural concern is **Composition**, not the numerical count of
subscribers.

A Business Central tenant may include:

- Microsoft Base and System Applications;
- country and feature localizations;
- AppSource applications;
- ISV vertical solutions;
- customer-specific extensions.

Several independently developed participants may legitimately need to affect
one business process.

An architecture that communicates exclusive ownership through a mutable
Boolean and subscriber convention cannot reliably express:

- whether participation is additive or exclusive;
- which implementation has priority;
- whether implementations can be combined;
- how conflicts are resolved;
- whether ordering matters;
- who is authoritative.

The important distinction is between:

- **intentional exclusivity**, where exactly one selected implementation is a
  defined architectural rule; and
- **accidental exclusivity**, where the first subscriber effectively wins
  because of event execution and convention.

## Counterarguments

Some operations genuinely require one authoritative implementation.

Examples include selecting one posting strategy, one provider or one
calculation algorithm. Multiple execution could be incorrect.

In those cases, exclusivity should be explicit through a resolver, interface,
factory, setup selection or orchestrator. The criticism is not that only one
implementation runs; it is that exclusivity and selection are implicit.

## Framework Implication

Candidate review questions:

- Is participation additive, competitive or exclusive?
- Is exclusive ownership intentional and documented?
- How is one implementation selected?
- Does outcome depend on subscriber order?
- Can independently developed extensions compose safely?
- Is conflict detection possible?
- Can multiple responsibilities be orchestrated rather than made mutually
  exclusive?

## Threats to Validity

The critical collisions were observed inside one Microsoft localization
application. Cross-application composition in large AppSource tenant stacks
may introduce additional patterns not represented here.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft single-subscriber concern | Normative |
| CZL competing subscribers | Empirically Supported |
| Composition interpretation | Candidate |

# 8.5 Coding by Convention

## Microsoft Position

The `IsHandled` contract is enforced by convention rather than by the AL type
system or runtime.

A subscriber can:

- ignore an already true value;
- change `true` back to `false`;
- set the value before completing its responsibility;
- execute side effects without claiming ownership;
- claim ownership without implementing the full expected behaviour.

Microsoft notes that such violations are difficult to troubleshoot and can
produce unexpected behaviour.

## Microsoft Evidence

Microsoft increasingly recommends explicit concepts, interfaces and event
contracts with a clear purpose.

The minimum requirements for a new handled event require documentation of:

- the functional gap;
- alternatives evaluated;
- intended use;
- multi-extension interaction;
- performance;
- data sensitivity;
- expected effect on future evolution.

These requirements compensate for information that the Boolean contract does
not express.

## Representative BC280 Example

**CZF Finding #7**

- Object: `Codeunit 31236 "FA Acquisition Handler CZF"`.
- Event: `OnIsFAAcquisitionAsCustom2CZL`.
- Observed behaviour: the subscriber returns a feature decision and sets
  `IsHandled := true`.
- Reported problem: `IsHandled` acts as a single source-of-truth mechanism.
- Reported impact: hidden coupling in a multi-application environment.

The event name asks a capability or policy question, but the handled
convention introduces an implicit winner. The Boolean pair communicates both a
result and authority to stop considering other implementations.

The intended semantics cannot be fully derived from the AL signature:

- Is the answer cumulative?
- May more than one extension answer?
- Does `false` mean disabled or unanswered?
- Which subscriber is authoritative?
- May a later subscriber revise the result?

## Research Interpretation

The architectural concern is an **Explicit Contract**.

The mutable `IsHandled` convention combines several meanings:

- participation;
- completion;
- ownership;
- cancellation;
- override;
- short-circuiting.

Because those meanings are not represented explicitly, correctness depends on
shared assumptions among independently evolving components.

An explicit contract can instead define:

- one selected implementation;
- an additive collection of contributions;
- a cumulative Boolean result;
- a veto;
- a validation policy;
- a strategy resolver;
- a pipeline stage.

Interfaces are one option, but not the only option. The architectural
requirement is semantic explicitness.

## Counterarguments

Conventions are not inherently invalid.

Within a small coordinated codebase, a stable convention can be efficient,
familiar and easy to implement. Formal abstractions can add unnecessary
complexity for a very small extension point.

The risk rises when:

- applications evolve independently;
- the event has many subscribers;
- the event controls critical behaviour;
- the semantics are ambiguous;
- ordering influences the outcome;
- the contract must survive long-term evolution.

## Framework Implication

Candidate review questions:

- What meanings are encoded in the Boolean?
- Which behavioural assumptions are implicit?
- Can the contract distinguish unanswered, false, vetoed and completed states?
- Is implementation selection explicit?
- Can contract violations be detected?
- Would a named policy, interface, resolver or positive event communicate the
  intent more precisely?

## Threats to Validity

The representative example concerns a feature-policy or discovery-style event,
not a full posting replacement. More mechanism types should be examined before
generalizing a single preferred replacement design.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft convention concern | Normative |
| Implicit authority in BC280 | Empirically Supported |
| Explicit Contract interpretation | Candidate |

# 8.6 Extensibility Degradation

## Microsoft Position

Turning off standard code can prevent events inside that code from being
raised, thereby breaking other extensions.

Microsoft recommends:

- proper extensibility concepts;
- focused regular events;
- separate implementations with clear boundaries;
- minimal skipped code;
- explicit consideration of multi-extension interaction.

## Microsoft Evidence

Microsoft's summary states that handled patterns do not allow many extensions
to subscribe to the same event in the normal additive sense. It also warns
that skipped events can break extensions that depend on the overridden code.

This establishes that extensibility quality is not measured only by the
presence of a publisher. It depends on whether extension participation remains
available in the effective execution path.

## Representative BC280 Example

**CZL Finding #29**

- Object: `Codeunit NavigateHandlerCZL`.
- Publisher event: `Navigate.OnBeforeShowRecords`.
- Observed behaviour: the subscriber replaces record display behaviour and
  sets the handled flag.
- Classification: **DEAD-END EVENT (EXTENSIBILITY BREAK)**.
- Reported problem: the flow is captured without re-exposing further hooks.
- Reported impact: later extensions cannot meaningfully participate in the
  custom navigation flow.

The standard publisher remains technically extensible: another subscriber can
still be invoked. Once the localization subscriber takes effective ownership,
however, the standard continuation and its extension points no longer define
the executed behaviour.

## Research Interpretation

This observation motivates the candidate concept of **Effective
Extensibility**.

Technical reachability is not equivalent to behavioural participation.

An extension point may still exist and subscribers may still run, while the
behaviour they intended to extend is no longer the behaviour that executes.

The distinction can be represented as follows:

| Property | Question |
|---|---|
| Publisher availability | Does an event or interface exist? |
| Subscriber reachability | Is the extension invoked? |
| Behavioural participation | Can it influence the effective process? |
| Effective Extensibility | Can future extensions participate meaningfully and predictably? |

A replacement extension that assumes ownership of a non-trivial flow may
therefore also assume responsibility for preserving suitable extension points
inside the replacement flow.

This is a candidate principle, not an established Microsoft rule.

## Counterarguments

Not every replacement flow should expose additional hooks.

Security-sensitive, atomic or tightly controlled behaviour can require a
closed boundary. Excessive extensibility can weaken invariants and increase
support costs.

The review should therefore ask whether closure is:

- intentional;
- justified;
- documented;
- proportional to the responsibility;
- compatible with the platform's expected extension model.

## Framework Implication

Candidate review questions:

- Which existing extension points become unreachable or irrelevant?
- Can another extension participate in the behaviour that actually executes?
- Does the replacement expose suitable before, after, policy or strategy
  participation points?
- Is a closed extension boundary intentional?
- Does the replacement become an architectural dead end?
- Who owns preservation of extensibility after responsibility transfer?

## Threats to Validity

Effective Extensibility remains a repository candidate concept. Broader
validation across AppSource applications, non-event mechanisms and future
Business Central versions is required.

## Confidence Assessment

| Layer | Confidence |
|---|---|
| Microsoft skipped-event concern | Normative |
| CZL dead-end event | Empirically Supported |
| Effective Extensibility | Candidate |

# 9. Additional Microsoft Concerns

The six principal analyses above consolidate the alpha drafts, but Microsoft's
current guidance also makes two related concerns explicit.

## 9.1 Clear Purpose

Handled events are often named after the line, method or block to be skipped.
Such names describe implementation location rather than extension intent.

A clearer event contract states the permitted operation positively, for
example:

- add filters;
- transfer a difference;
- provide an implementation;
- validate a policy;
- contribute a pipeline stage.

Clear purpose supports refactoring because the publisher can change its
internal implementation while preserving the semantic contract.

This concern contributes primarily to:

- Discoverability;
- Explicit Contracts;
- Evolution Ownership.

## 9.2 Validation Suppression

Microsoft explicitly recommends not turning off validation.

The BC280 analysis contains representative validation bypasses, including:

- CZL Finding #14:
  `Gen. Jnl.-Post Batch.OnBeforeIfCheckBalance`;
- CZL Finding #32:
  `Purch.-Post.OnBeforeTestPurchLineItemCharge`;
- CZL Finding #35:
  `Sales-Post.OnBeforeTestSalesLineItemCharge`.

These cases do not necessarily prove incorrect business behaviour. They show
that an extension can assume responsibility for invariants previously enforced
by the standard flow.

Validation suppression should therefore trigger explicit review of:

- the invariant being changed;
- all other code paths that assume the invariant;
- persisted data states;
- downstream calculations;
- error and recovery behaviour;
- replacement validation ownership.

# 10. Cross-cutting Architectural Themes

The Microsoft criticisms converge on a small set of recurring architectural
concerns.

| Microsoft criticism | Architectural concern | Primary risk | Candidate review question |
|---|---|---|---|
| Turning off parts of code | Responsibility Transfer | Hidden responsibility | Who owns the replaced behaviour? |
| Fragile evolution | Evolution Ownership | Behavioural divergence | Who owns future evolution? |
| Low readability / unclear purpose | Discoverability | Hidden effective behaviour | Can effective behaviour be reconstructed? |
| Single subscriber assumption | Composition | Accidental exclusivity | Can independent participants compose safely? |
| Coding by convention | Explicit Contract | Implicit semantics | Which behavioural expectations are unenforced? |
| Events not raised / extensibility loss | Effective Extensibility | Architectural dead end | Can future extensions still participate meaningfully? |
| Validation suppression | Invariant Ownership | Invalid or inconsistent states | Who preserves the affected invariant? |

## 10.1 Architectural synthesis

None of these concerns is inherently tied to `IsHandled`.

The pattern makes them visible because it combines three operations:

1. an extension participates;
2. it may replace or suppress existing behaviour;
3. a mutable Boolean communicates whether execution should stop.

Equivalent concerns can arise through:

- interface selection that replaces an entire implementation;
- strategy replacement;
- middleware short-circuiting;
- workflow interception;
- plugin precedence;
- feature toggles;
- custom posting modules;
- copied and independently maintained business logic.

The mechanism is therefore an architectural marker, not the architecture
review subject.

## 10.2 Relationship to architectural behaviour

SEI guidance treats behaviour as an architectural concern represented through
behaviour views and models.

The `IsHandled` analysis reinforces that position:

- publisher source alone does not define effective behaviour;
- subscribers alter ordering, responsibility and reachability;
- replacement changes the runtime interaction among architectural elements;
- behaviour documentation and behaviour evaluation are related but distinct.

This document contributes to evaluation: it identifies concern categories that
may justify architecture review when effective behaviour changes.

# 11. Representative Empirical Validation

The empirical studies were designed as representative validation, not
statistical measurement.

## 11.1 CZL scope

The Core Localization Pack for Czech analysis reported:

- 44 unique event-subscriber methods with `var IsHandled: Boolean` that assign
  `IsHandled := true`;
- 10 full overrides;
- 23 partial logic modifications;
- 8 validation or side-effect cases;
- 3 direct dead-end events, with additional high-risk cases;
- 3 critical competing-subscriber collisions in
  `Inventory Posting To G/L`.

## 11.2 CZF scope

The Fixed Asset Localization for Czech analysis reported:

- 15 subscriber methods with `var IsHandled: Boolean`;
- all 15 assigning `IsHandled := true`;
- no duplicate competing subscribers inside that extension;
- several full overrides, partial modifications, validation cases and
  dead-end events;
- a candidate additional category: discovery or capability-query misuse.

## 11.3 Mapping of representative examples

| Microsoft concern | Representative BC280 example |
|---|---|
| Turning off parts of code | CZF Finding #13 — complete FA G/L insertion and correction replacement |
| Fragile evolution | CZF Finding #13 — independently maintained replacement posting path |
| Low readability / discoverability | CZF Finding #13 — effective flow distributed across publisher and replacement implementation |
| Single subscriber assumption | CZL critical collision on `OnBeforeBufferPurchPosting` |
| Coding by convention | CZF Finding #7 — feature-policy result combined with handled authority |
| Extensibility degradation | CZL Finding #29 — custom navigation flow without re-exposed hooks |
| Validation suppression | CZL Finding #14 — conditional journal balance-check bypass |

The examples demonstrate that the concern categories described by Microsoft
occur in production Microsoft applications.

They do not establish:

- that every occurrence is incorrectly designed;
- that every `IsHandled` event should be removed;
- that one replacement mechanism is always preferable;
- that the observed frequency applies to the wider ecosystem.

# 12. What Microsoft Recommends Instead

Microsoft does not prescribe one universal replacement for `IsHandled`.

The appropriate design depends on the missing concept and the intended
participation model.

## 12.1 Implement the missing concept

Where the application lacks a durable domain abstraction, add the concept
rather than a generic skip point.

Possible mechanisms include:

- setup and implementation selection;
- interfaces;
- extensible enums;
- services;
- providers;
- policies;
- pipelines.

This is the preferred solution when several implementations of a stable
business concept are expected.

## 12.2 Use focused regular events

Use a positive event that describes the permitted contribution.

Examples:

- add additional filters;
- adjust a defined value;
- contribute data;
- react before or after an operation;
- verify a condition without suppressing the surrounding process.

Focused events preserve standard orchestration and support additive
participation.

## 12.3 Reimplement as separate functionality

Where behaviour is fundamentally different, create a separate action, field,
module or implementation with a clear boundary.

A clear replacement boundary can be safer than injecting many handled events
throughout the standard flow.

## 12.4 Use narrowly scoped skipping

When no better design is viable:

- skip as little code as possible;
- avoid validation suppression;
- avoid wrapping large blocks;
- keep the remaining path minimal and predictable;
- document the reason;
- evaluate multi-extension interaction;
- explain future-evolution implications.

## 12.5 Request proper extensibility

When existing mechanisms cannot support the scenario, submit an extensibility
request with:

- a precise functional gap;
- proposed code and placement;
- alternatives evaluated;
- justification for `IsHandled`;
- performance and data considerations;
- multi-extension interaction;
- expected test impact;
- future-evolution reasoning.

# 13. Relationship to the Behavior Change Review Framework

This reference does not define the framework.

It provides one evidence chain:

1. Microsoft documents risks in a specific mechanism.
2. Representative BC280 applications exhibit the same concern categories.
3. Architectural interpretation identifies mechanism-independent concerns.
4. Candidate questions can be tested against additional mechanisms.
5. Only after broader validation should they become framework criteria.

| This reference provides | Future framework should provide |
|---|---|
| Microsoft guidance | Mechanism-independent review trigger |
| Representative evidence | Proportional review levels |
| Architectural concern categories | Review process |
| Candidate review questions | Actionable checklist |
| Threats and limitations | Evidence and decision recording method |

`IsHandled` should remain a primary case study because its effects are explicit
and empirically accessible. It should not become the definition of
behaviour-changing customization.

# 14. Findings

## 14.1 Accepted

- Microsoft recommends limiting `IsHandled` to a bare minimum and treating it
  as a last resort.
- Microsoft prefers proper extensibility concepts, focused events, explicit
  implementations and narrowly scoped variation.
- The pattern assumes a single effective subscriber and relies on convention.
- Broad replacement can skip validation, events and future standard behaviour.
- Representative BC280 applications contain full overrides, competing
  subscribers, validation bypasses and dead-end flows matching Microsoft's
  concern categories.
- Behaviour is the relevant architectural subject; `IsHandled` is one
  mechanism that changes it.

## 14.2 Candidate

- Responsibility Transfer is a useful interpretation of broad behavioural
  replacement.
- Evolution Ownership is more precise than treating divergence only as an
  upgrade issue.
- Discoverability better describes the architectural consequence behind low
  readability.
- Explicit Contract captures the concern behind coding by convention.
- Effective Extensibility distinguishes extension-point existence from
  meaningful participation in effective behaviour.
- Replacement of a non-trivial execution path may transfer responsibility for
  preserving suitable extensibility.

## 14.3 Open

- Which concern categories objectively trigger architecture evaluation?
- How should review depth scale with replacement scope and business
  criticality?
- Can Effective Extensibility be operationalized and measured?
- Can static analysis detect Responsibility Transfer or architectural
  dead ends?
- How do the findings change in large AppSource application stacks?
- Which concepts remain useful after evaluating non-event mechanisms?
- Should discovery and capability-query misuse become an independent concern
  category?

# 15. Threats to Validity

## 15.1 Source scope

Microsoft Learn guidance applies specifically to Dynamics 365 Business
Central. Generalization to other platforms is an interpretation.

## 15.2 Temporal scope

Microsoft guidance evolves. The primary pages referenced in this version were
reviewed as published in 2025–2026 and should be revalidated when the
repository updates this reference.

## 15.3 Empirical scope

Only two Microsoft Czech localization applications were used for the current
representative validation.

The sample is not statistically representative of:

- all Microsoft applications;
- AppSource;
- ISV solutions;
- customer extensions;
- other localization architectures.

## 15.4 Classification bias

The empirical categories were assigned through architectural analysis.
Different reviewers may classify borderline cases differently.

## 15.5 Intent uncertainty

Source code demonstrates behaviour but does not always document original
design intent. A subscriber classified as a dead end may intentionally enforce
a closed responsibility boundary.

## 15.6 Architectural interpretation

Responsibility Transfer, Evolution Ownership, Discoverability, Explicit
Contract and Effective Extensibility are repository interpretations. They are
not presented as Microsoft terminology.

## 15.7 Alternative-design uncertainty

A concern does not prove that a proposed interface, factory, bridge or pipeline
would be superior in the actual product context. Replacement designs require
their own trade-off evaluation.

# 16. Conclusions

## Conclusion 1 — Microsoft's position is architectural

Microsoft's criticism is not primarily about Boolean syntax. It concerns
maintainability, composition, behavioural clarity, evolution and preservation
of extension participation.

## Conclusion 2 — `IsHandled` is neither universally invalid nor a default design

The mechanism remains supported for exceptional cases, but Microsoft requires
alternatives to be evaluated first and replacement scope to be minimized.

## Conclusion 3 — Replacement transfers more than implementation

When an extension replaces established behaviour, it can also assume
responsibility for invariants, side effects, downstream events, evolution and
extensibility.

## Conclusion 4 — Production evidence validates the concern categories

The BC280 CZL and CZF analyses contain representative full overrides,
subscriber collisions, implicit contracts, validation bypasses and dead-end
flows.

## Conclusion 5 — The concerns appear mechanism-independent

Equivalent architectural consequences can arise through interfaces,
strategies, workflows and other replacement mechanisms. The future framework
should review behaviour-changing customizations, not search only for
`IsHandled`.

## Conclusion 6 — The remaining research gap is narrower

Software architecture literature already recognizes behaviour as an
architectural concern. Microsoft already documents extensibility principles
and `IsHandled` risks.

The repository's potential contribution is therefore a Business Central
specialization that determines:

- when a behaviour-changing customization deserves architecture evaluation;
- which concerns should be reviewed;
- how review depth should be proportional to risk;
- how evidence and decisions should be recorded consistently.

# 17. References

## 17.1 Microsoft Learn

1. Microsoft. **Using the IsHandled pattern for events**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-pattern

2. Microsoft. **Minimum requirements for new IsHandled events**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-min-req

3. Microsoft. **Create an extensibility request**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/create-extensibility-request

4. Microsoft. **Types of events for extensibility**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/types-of-events-for-extensibility

5. Microsoft. **Extensibility overview**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

6. Microsoft. **Extension objects overview**.  
   https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extension-object-overview

## 17.2 Historical community context

7. Vjekoslav Babić. **Gentleman's Agreement Pattern, or Handling the Handled Pattern**. 2016.  
   https://vjeko.com/2016/10/04/gentlemens-agreement-pattern-or-handling-the-handled-pattern/

8. Vjekoslav Babić. **Codeunit Interfaces in AL**. 2019.  
   https://vjeko.com/2019/02/02/codeunit-interfaces-in-al/

These community sources provide historical context only. They are not treated
as normative Microsoft guidance.

## 17.3 Repository references

- `00_Project_Charter.md`
- `00_Research_Log.md`
- `01_Terminology.md`
- `02_Research_Methodology.md`
- `03_Related_Work.md`
- `ISO_42010.md`
- `ISO_42020.md`
- `ISO_42030.md`
- `SEI_Documenting_Behavior.md`
- `Microsoft_Extensibility_Overview.md`

## 17.4 Empirical studies

- `MS-CZL-IsHandled-Refactoring-Analysis-Report.md`
- `MS-CZF-IsHandled-Refactoring-Analysis-cs.md`

# Revision History

## 2.0 — Final Draft

- Consolidated `2.0-alpha-01` through `2.0-alpha-05`.
- Removed placeholders, iteration notes and duplicated wording.
- Harmonized terminology across all chapters.
- Added current Microsoft Learn references.
- Added one representative BC280 example for every principal Microsoft
  criticism.
- Separated Microsoft guidance, empirical observation, research
  interpretation and framework implication.
- Added clear findings, threats to validity and relationship to the wider
  repository.
