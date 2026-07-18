---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: REF-MS-EVENTS-001
  title: Microsoft Business Central Event Types Analysis
  type: Reference Analysis
  version: 0.3.0
  status: Active

classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Analyzes Microsoft's Business Central event taxonomies, design guidance, and
  runtime semantics as evidence for reviewing event-based behavior changes
  without treating an event type as a complete statement of architectural
  effect or quality.

quality:
  review: Self Reviewed
  evidence: Verified
  editorial: Reviewed

audience:
  - Researchers
  - Contributors
  - AI Assistants

depends_on:
  - 02_Research_Methodology.md
  - 03_Related_Work.md

related_documents:
  - 00_Research_Log.md
  - 01_Terminology.md
  - References/Microsoft_Extensibility_Overview.md
  - References/Microsoft_Interfaces.md
  - References/Microsoft_IsHandled_v2.0.md
  - References/ATAM.md
  - References/SAAM.md

evidence:
  source_authority: Official Vendor Documentation
  source_access: Full
  verification: Verified
  limitations: >
    The analysis is limited to the cited public Microsoft Learn documentation
    as available on 2026-07-18. It does not establish the prevalence or runtime
    effect of event patterns across the complete Business Central application
    or third-party extension ecosystem.

tags:
  - Microsoft
  - Business-Central
  - events
  - event-contracts
  - event-subscribers
  - extensibility
  - behavior-change
---

# Microsoft Business Central Event Types Analysis

## 1. Purpose and Research Question

This document analyzes Microsoft's official Business Central event
documentation as evidence for the Orden project. It does not define the
Behavior Change Review Framework and does not assume that using an event makes
a customization architecturally sound.

The research question is:

> What semantics and intended uses does Microsoft assign to Business Central
> event types and event patterns, and what does that taxonomy establish—or
> leave unresolved—about reviewing subscribers that change behavior?

## 2. Source Scope and Access

### 2.1 Sources examined

The principal sources are current Microsoft Learn articles covering:

- the language and runtime event types;
- Microsoft's extensibility-oriented event patterns and quality rankings;
- event publishers, raising, and subscribers;
- isolated event transaction behavior;
- manual subscriber binding;
- event extensibility requests and design guidance; and
- AppSource compatibility rules for changing event types.

All cited sources were publicly accessible in full on 2026-07-18. Source
claims are limited to the content of those pages and their stated applicability.

### 2.2 Two overlapping taxonomies

Microsoft documentation presents two related but distinct classifications:

1. **Language and runtime event types**, including business, integration,
   internal, global, database trigger, and page trigger events [M1].
2. **Extensibility event patterns**, including business events,
   `OnBefore`/`OnAfter` placements, verify, isolated, switch, `OnSkip`, handled,
   and discovery events [M2].

The second classification evaluates intended use and maintainability of event
placements or patterns. Several entries in it are implemented as integration
events. Therefore, an event's AL attribute and its extensibility pattern are
not interchangeable classifications.

## 3. Verified Microsoft Claims

This section reports Microsoft's documented position. Repository
interpretation begins in Section 4.

### 3.1 Event model

Microsoft describes events as a way for one piece of code to communicate with
another, either to notify other objects that something occurred or to allow
other objects to influence code behavior [M1].

The event model has three participants [M3]:

- an **event**, declared by an event publisher method;
- a **publisher**, which exposes and raises the event; and
- a **subscriber**, which contains the business logic executed when the event
  is raised.

Publishing a business or integration event only declares the subscription
point. Application code must also raise it. Trigger events are declared and
raised automatically by the runtime [M3].

Microsoft states that a publisher has no knowledge of whether subscribers
exist and that subscribers may reside elsewhere in the application [M3]. A
single event may have multiple subscribers. Subscriber methods execute one at
a time in no particular order, and their order cannot be specified [M4].

### 3.2 Business events

A `BusinessEvent` is a custom event raised by AL code. Microsoft describes it
as a formal contract with an implicit promise not to change in future releases
and compares it to a publicly released API [M1].

Microsoft states that business events typically reflect process state changes
and are suited to workflow. They should not be tied to implementation details,
and their documentation should include the before-state and after-state [M1].

The extensibility guidance assigns business events "Very High Value" when they
notify subscribers that a specific business event occurred [M2].

### 3.3 Integration events

An `IntegrationEvent` is also a custom event raised by AL code, but Microsoft
states that it does not carry the same promise of stability as a business event
and may expose implementation details [M1]. Its principal purpose is to enable
other solutions to integrate with Business Central without traditional code
modification [M1].

Microsoft documents that an integration event can later become a business
event, subject to the stronger contract. AppSourceCop permits that conversion
only under compatibility conditions. It prohibits conversions from business to
integration or internal, and from integration to internal, because dependent
subscribers could break [M8].

### 3.4 Internal events

An `InternalEvent` can be subscribed to only from within the same module [M7].
Microsoft allows an internal event to become an integration or business event,
thereby expanding its availability to dependent extensions [M8].

The internal scope is an accessibility boundary. Microsoft explicitly warns
that using `InternalEvent` is not a security control: event requests must still
consider whether an event exposes sensitive data [M6].

### 3.5 Global and trigger events

Microsoft describes global events as predefined events raised by Base
Application codeunits for operations such as company open and close, login,
printing, and global database handling. The listed global events are
implemented as integration-event publishers [M1].

Trigger events are predefined runtime events and cannot be raised
programmatically. Database trigger events are raised for operations such as
insert, modify, delete, rename, and field validation. Page trigger events are
associated with page operations [M1].

The fact that a trigger event is raised by the runtime describes its source and
lifecycle. Microsoft does not characterize every trigger-event subscriber as a
business-level contract or a high-value extensibility point.

### 3.6 `OnBefore` and `OnAfter` placement quality

Microsoft's extensibility guidance ranks `OnBefore` and `OnAfter` events by
their placement [M2]:

- before or after a large operation: high value;
- before or after a specific procedure: medium value because the event is tied
  to a procedure that may be changed or removed; and
- before or after a specific line: low value in general because the event is
  fragile and has little reuse between extensions.

Microsoft notes that `OnBefore`/`OnAfter` events may add logic to a flow without
allowing existing behavior to be overridden [M2]. Consequently, the naming
pattern alone does not state whether a subscriber augments, validates,
influences, or replaces behavior.

### 3.7 Verify events

Microsoft assigns verify events medium value and describes their purpose as
checking whether business logic is correct before or after an operation [M2].
It warns that verify events should not create transactions and that their
placement must avoid partial-commit risks [M2].

This guidance connects event placement with transaction behavior, but it does
not claim that a verify subscriber is side-effect free merely because the
publisher was intended for verification.

### 3.8 Isolated events

Business, integration, and internal events can be marked isolated [M5]. An
isolated event normally invokes each subscriber in its own transaction. If a
subscriber fails, its supported table changes are rolled back and execution
continues to the next subscriber or returns to the caller [M5].

Microsoft records important qualifications [M5]:

- write transactions should commit before invoking an isolated event;
- otherwise, the event can execute like a normal event;
- rollback applies to normal-table changes, not necessarily HTTP calls,
  variables, or single-instance state;
- a `var` parameter changed by a failing subscriber can retain that change; and
- installation and upgrade operations do not run isolated events in isolated
  transactions.

The extensibility guidance therefore says isolated events require detailed
review and notes testing limitations [M2].

### 3.9 Switch events and manual binding

Microsoft describes switch events as events intended for manually bound
subscribers. A subscriber can be activated for a specific scope or call to
change the behavior of that invocation [M2].

With `EventSubscriberInstance = Manual`, the caller controls which subscriber
instance is active by using `BindSubscription`. If no binding is established,
the subscriber does not run. The binding is session-specific and its lifetime
depends on the bound codeunit instance [M9].

Manual binding changes participation deterministically at runtime, but it does
not by itself define the semantic contract of the replacement or influence.

### 3.10 `OnSkip` events

Microsoft characterizes `OnSkip` events as similar to handled events but with
multiple skip parameters for more granular control. The documented intent is
to support multiple subscribers and allow several extensions to influence
which parts of an operation execute [M2].

This pattern can alter effective behavior without transferring the entire
operation to one subscriber. Its granularity does not remove the need to
consider interactions among subscribers and skipped steps.

### 3.11 Handled events

Microsoft assigns handled events low value. It states that subscribers must
exit when another subscriber has already handled the event, that the pattern
does not scale, and that only one subscriber can process the request under its
convention [M2].

Microsoft also warns that introducing a handled event can break events raised
by the existing code and make it unclear whether or why code was handled [M2].
Its separate guidance recommends limiting `IsHandled` to cases where it is
absolutely necessary [M6].

The detailed repository analysis of this pattern remains in
`References/Microsoft_IsHandled_v2.0.md` and is not duplicated here.

### 3.12 Discovery events

Microsoft describes discovery events as mostly obsolete. They historically
allowed subscribers to register possible implementations in a temporary table,
after which one implementation could be selected. Microsoft now states that
enums and interfaces can provide better designs [M2].

This is evidence of mechanism evolution. It does not demonstrate that every
event-based discovery design should be replaced without analyzing compatibility
and behavior.

### 3.13 Event request design guidance

For proposed events, Microsoft advises contributors to [M6]:

- avoid exposing implementation-specific or unstable parameter shapes;
- preserve signature compatibility when adding parameters;
- consider manual binding where appropriate;
- avoid exposing sensitive data because anyone with access can subscribe;
- consider whether and how multiple extensions can use the event
  simultaneously; and
- consider error handling.

These are explicit publisher and extension-point design concerns. Microsoft
does not present them as a complete architecture-review method for subscriber
implementations.

## 4. Repository Observations

The following are observations about how the verified documentation relates to
Orden. They are not Microsoft claims.

1. Event classification has at least three independent dimensions: publisher
   attribute or runtime source, placement or design pattern, and subscriber
   effect on behavior.
2. An `IntegrationEvent` can implement a high-value operation boundary, a
   low-value line-level hook, a verify point, a switch, an `OnSkip` pattern, or
   an `IsHandled` pattern. The attribute alone does not identify architectural
   significance.
3. A subscriber can notify, augment, validate, mutate data, suppress a step,
   replace behavior, or select an implementation. Event type does not fully
   describe that effect.
4. Business-event stability concerns the published contract. It does not prove
   that every subscriber preserves business invariants or composes safely with
   other subscribers.
5. Trigger-event availability does not imply that the trigger is the correct
   semantic boundary for a customization.
6. Unspecified subscriber order and multiple-extension participation are
   direct composition constraints for behavior-changing subscribers.
7. Isolated execution changes failure propagation and transaction boundaries
   but does not isolate every side effect.

## 5. Research Interpretation

### 5.1 Event type is not behavioral effect

Microsoft's taxonomies describe contracts, accessibility, runtime publication,
placement quality, and common patterns. They do not provide a single
classification of what a subscriber does to effective behavior.

This distinction is important for mechanism independence. Two subscribers to
the same integration event can have materially different consequences, while
subscribers using different event types can produce the same behavioral
change. A review that begins and ends with the event attribute would therefore
miss relevant architectural effects.

### 5.2 Event quality is publisher-side evidence

Microsoft's value rankings are useful evidence about extension-point design.
Operation-level events are generally more stable and reusable than events tied
to a procedure or line. However, a high-value publisher does not guarantee a
high-quality subscriber, and a low-value publisher does not determine the
severity of every subscriber.

The quality ranking can inform evidence collection: a subscriber tied to an
implementation detail may face greater evolution risk. It cannot substitute
for analysis of the subscriber's actual behavior, dependencies, side effects,
and composition.

### 5.3 Composition is an explicit concern

Microsoft's documentation confirms that subscribers can be multiple,
distributed, and unordered. Its event-request guidance explicitly asks how
multiple extensions use an event simultaneously. These facts support reviewing
composition rather than assuming an isolated extension.

The SAAM concept of scenario interaction may help locate subscribers that
affect common responsibilities. It does not by itself model runtime order,
shared mutable parameters, skip flags, or responsibility transfer. Additional
runtime participation evidence may therefore be necessary.

### 5.4 Transaction and failure semantics are part of behavior

Verify and isolated event guidance demonstrates that event-based customization
can affect commit behavior, rollback, error propagation, and continuation.
These consequences are not secondary implementation details when they alter
observable outcomes or system guarantees.

The isolated-event qualifications also show why labels such as "isolated" must
not be interpreted more broadly than the documented runtime semantics.

## 6. What Microsoft Guidance Does Not Establish

The examined documentation does not establish that:

- every event subscriber changes established behavior;
- every `BusinessEvent` subscriber is architecturally safe;
- every `IntegrationEvent` is unstable or low quality;
- every trigger event is an appropriate business extension point;
- event subscriber execution order can be relied upon;
- isolated events roll back all subscriber side effects;
- `OnSkip` automatically composes correctly across extensions;
- an event value ranking measures subscriber consequence or risk; or
- event use alone determines whether architectural review is required.

The documentation provides strong mechanism-specific design evidence but not a
complete, mechanism-independent review trigger or consequence model.

## 7. Relevance to the Main Research Question

Microsoft's event guidance already recognizes several concerns central to
Orden: contract stability, implementation coupling, multiple-extension use,
error handling, transaction behavior, discoverability, and evolution risk.
This is negative evidence against claiming those concerns as new discoveries.

The unresolved integration problem is narrower. A Business Central review must
connect the event's declared contract and runtime semantics to the subscriber's
actual behavioral effect and then evaluate consequences that may cross event
types. Microsoft documents the inputs, but the examined sources do not combine
them into that review process.

## 8. Candidate Implications for the Framework

The following are non-normative candidates for later synthesis:

1. Record the event's language/runtime type separately from its placement or
   extensibility pattern.
2. Describe the subscriber's actual effect: notify, augment, validate, mutate,
   suppress, replace, select, or otherwise influence behavior.
3. Identify whether the event represents a business contract, an integration
   hook, a module-internal collaboration, or a runtime trigger.
4. Review reliance on implementation details and the publisher's expected
   evolution boundary.
5. Evaluate multiple-subscriber composition without assuming execution order.
6. Trace mutable parameters, skip or handled flags, and responsibility for
   behavior that no longer executes.
7. Review transaction, rollback, error-propagation, and external-side-effect
   semantics, especially for verify and isolated events.
8. Treat manual binding as an explicit runtime participation decision.
9. Record sensitive-data exposure and permission or licensing skip behavior
   where relevant.
10. Scale review depth to actual consequences rather than to the event name or
    attribute alone.

These candidates organize evidence from Microsoft guidance. They do not yet
define accepted framework rules.

## 9. Relationship to SAAM and ATAM

SAAM suggests mapping scenarios to affected architectural elements and
examining scenario interactions. For event-based customization, publisher,
subscriber, mutable parameters, and affected business responsibilities are
candidate elements for that mapping. Whether the desired scenario is already
supported cannot be inferred from the event's existence alone.

ATAM suggests examining quality-attribute risks and tradeoffs. Microsoft event
guidance identifies possible inputs to such analysis, including stability,
maintainability, transactions, security, error handling, and composition. The
event documentation does not perform that multi-attribute evaluation for a
subscriber.

This relationship is a repository interpretation, not a Microsoft-defined use
of SAAM or ATAM.

## 10. Limitations and Threats to Validity

- **Documentation change:** Microsoft Learn is continuously maintained. The
  analysis represents the cited pages as available on 2026-07-18.
- **Taxonomy overlap:** Microsoft uses "event types" for both AL/runtime types
  and extensibility patterns. This analysis separates them, but future
  documentation may revise either classification.
- **Example dependence:** The value rankings include examples from Microsoft
  application code, but this document did not independently audit their current
  implementation or prevalence.
- **Publisher emphasis:** Much of the guidance concerns designing or requesting
  publishers. Subscriber-side architectural consequences require additional
  evidence.
- **No ecosystem prevalence claim:** The sources do not establish how often
  each pattern appears or fails in Microsoft or third-party applications.
- **No empirical pilot:** The candidate classification has not yet been tested
  across representative Business Central subscribers.
- **Mechanism boundary:** Interfaces, workflow, direct procedure calls, and
  other mechanisms require separate analysis before conclusions can be called
  mechanism-independent.

## 11. Unresolved Questions and Future Research

1. Can event subscribers be classified consistently by behavioral effect
   independently of publisher type?
2. Which event characteristics predict architectural significance, if any,
   once subscriber behavior is considered?
3. How should shared `var` parameters, skip flags, and multiple subscribers be
   represented in an effective runtime participation model?
4. Can SAAM-style scenario interaction distinguish compatible subscriber
   composition from conflicting behavior changes?
5. Which transaction and external-side-effect scenarios should be mandatory
   when isolated events are involved?
6. How should publisher contract stability and subscriber evolution ownership
   be evaluated together?
7. Does interface-based behavior substitution expose the same concerns through
   a more explicit contract?
8. Which representative event cases should be selected for the first
   cross-mechanism empirical study?

## 12. References

- **[M1]** Microsoft. "Event types." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-event-types>.
- **[M2]** Microsoft. "Types of events for extensibility." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/types-of-events-for-extensibility>.
- **[M3]** Microsoft. "Events in Microsoft Dynamics 365 Business Central."
  Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-events-in-al>.
- **[M4]** Microsoft. "Subscribing to events." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-subscribing-to-events>.
- **[M5]** Microsoft. "Isolated Events in AL." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-events-isolated>.
- **[M6]** Microsoft. "Create an extensibility request." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/create-extensibility-request>.
- **[M7]** Microsoft. "InternalEvent attribute." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/attributes/devenv-internalevent-attribute>.
- **[M8]** Microsoft. "AppSourceCop Error AS0020." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/analyzers/appsourcecop-as0020>.
- **[M9]** Microsoft. "EventSubscriberInstance property." Microsoft Learn.
  <https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/properties/devenv-eventsubscriberinstance-property>.

## 13. Revision History

### 0.3.0 — 2026-07-18

- Replaced the research stub with a substantive reference analysis.
- Distinguished language/runtime event types from extensibility event
  patterns and value rankings.
- Verified contract, subscription, ordering, transaction, binding,
  compatibility, and event-request claims against official Microsoft sources.
- Separated Microsoft claims, repository observations, interpretation,
  candidate implications, limitations, and unresolved questions.

### 0.2.0

- Established the governed research-stub structure and permanent document ID.
