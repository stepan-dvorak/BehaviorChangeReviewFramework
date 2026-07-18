---
metadata_schema: "1.0"
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: RD-IDEA-001
  title: IsHandled Pattern Missing Extensibility Preservation Rule
  type: Research Idea
  version: 0.1.0
  status: Active
classification:
  domain: Business Central Extensibility
  layer: Exploration
  maturity: Draft
owner: Štěpán Dvořák
purpose: >
  Preserves the publicly published precursor to the Orden project: a candidate
  proposal for preserving downstream extensibility when an IsHandled subscriber
  replaces established behavior.
quality:
  review: Not Reviewed
  evidence: Pending
  editorial: Draft
audience:
  - Researchers
  - Contributors
  - AI Assistants
depends_on:
  - References/Microsoft_IsHandled_v2.0.md
  - 02_Research_Methodology.md
related_documents:
  - 00_Project_Charter.md
  - 00_Research_Log.md
  - 01_Terminology.md
  - Whitepaper/Behavior_Change_Review_Framework_for_Business_Central_Research_Draft.md
publication:
  platform: GitHub Discussions
  repository: microsoft/alguidelines
  discussion_number: 289
  url: https://github.com/microsoft/alguidelines/discussions/289
  published_on: "2026-06-14"
  author_username: stedvo-kmits
  role: Project Precursor
  provenance_status: Verified
tags:
  - research-idea
  - IsHandled
  - extensibility-preservation
  - candidate-rule
  - project-origin
---

🧩 Title
IsHandled Pattern: Missing Extensibility Preservation Rule

📄 Full Technical Article (GitHub / AL Guidelines ready)



## Context

The IsHandled pattern is a fundamental extensibility mechanism in Dynamics 365 Business Central.

It is:
- widely used in the base application
- consistently used in localization layers
- formally documented by Microsoft

Reference:
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-pattern  
https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-min-req  

This clearly indicates that:

> The IsHandled pattern is not deprecated and is not going away.

---

## Problem Statement

Current guidance around IsHandled focuses on:

- Correct usage of `if IsHandled then exit;`
- Avoiding unintended override conflicts
- Ensuring predictable execution order where possible

However, one critical aspect is not explicitly addressed:

> What happens to extensibility after a subscriber sets `IsHandled := true`?

---

## Observation

In real-world codebases (base app, localization, partner solutions), three recurring patterns emerge:

### 1. Competing overrides
Multiple subscribers set `IsHandled := true`

→ Non-deterministic behavior

---

### 2. Monolithic override
One subscriber owns the full logic

→ No extensibility remains

---

### 3. Controlled override (most subtle case)

Single subscriber:
- correct business logic
- deterministic behavior
- clear ownership

BUT:

> The extensibility chain is terminated with no alternative extension points

---

## Root Cause

The IsHandled pattern acts as a **hard execution boundary**:

```al
if IsHandled then
    exit;
```	
	
	
When a subscriber sets:

```al
IsHandled := true;  
```

it does not only override logic. It also:
*   skips base behavior ✅
*   prevents other subscribers from executing ❌
*   removes further extensibility ❌

* * *

Gap in Current Guidelines
-------------------------

Existing documentation explains **how to override behavior safely**.
It does not define:

> **how extensibility must be preserved after an override**

This leads to a widespread implicit pattern:

```al
// custom logic  
IsHandled := true;  
```

which creates an **extensibility dead-end**.

* * *

Proposal: Extensibility Preservation Rule
-----------------------------------------

### ✅ New Rule

> **If a subscriber sets `IsHandled := true`, it must preserve extensibility by re-exposing alternative integration events.**

* * *

Minimal Implementation
----------------------

### ❌ Current pattern

```al
// custom logic  
IsHandled := true;  
```

* * *

### ✅ Improved pattern

```al
OnBeforeCustomX(...);  
// custom logic  
OnAfterCustomX(...);  
IsHandled := true;  
```

* * *

Characteristics of This Approach
--------------------------------

*   Does not require refactoring existing logic
*   Preserves backward compatibility
*   Maintains deterministic override behavior
*   Restores extensibility chain
*   Provides explicit extension points
*   Re-exposed events must be placed inside the same condition that controls IsHandled := true.

* * *

Relation to Method Pattern
--------------------------

This proposal is strongly inspired by the **Method pattern**:
https://alguidelines.dev/docs/patterns/generic-method-pattern/
The Method pattern introduces:
*   explicit orchestration
*   clear execution flow
*   controlled extension points

* * *

### Important distinction

This proposal:
*   does **not replace** the Method pattern
*   does **not introduce orchestration**
Instead, it extracts the **minimal essential property**:

> **explicit extensibility contract**

* * *

### Interpretation

| Approach | Extensibility | Orchestration |
| --- | --- | --- |
| Raw IsHandled | ❌ | ❌ |
| IsHandled + hooks (this proposal) | ✅ | ❌ |
| Method pattern | ✅ | ✅ |

* * *

This makes it a **transitional pattern**, not a target architecture.

* * *

Why Not Always Use Method Pattern?
----------------------------------

In ideal scenarios, Method pattern or Strategy/Factory pattern should be preferred.
However, in practice:
*   IsHandled is deeply embedded in the ecosystem
*   Base application relies on it
*   AppSource compatibility limits changes
*   Full refactoring is often not feasible
Therefore:

> A minimal, compatible improvement is required

* * *

Practical Impact
----------------

Applying this rule eliminates:
*   extensibility dead-ends
*   hidden termination of event chains
*   implicit ownership without extension capability
Without:
*   rewriting logic
*   restructuring architecture
*   breaking compatibility

* * *

Example Scenario
----------------

### Approval Override (real-world pattern)

```al
if InputRecordRef.Number() = Database::"Custom Table" then begin  
   
   // custom logic  
   
   IsHandled := true;  
end;  
```

* * *

### Problem

*   Logic is correct
*   Ownership is clear
But:

> No extension point exists for further customization

* * *

### Improved version

```al
if InputRecordRef.Number() = Database::"Custom Table" then begin
    OnBeforeCustomApproval(InputRecordRef, Variant);

    // custom logic

    OnAfterCustomApproval(InputRecordRef, Variant);

    IsHandled := true;
end;
```

* * *

Key Insight
-----------

> **The problem is not overriding behavior.  
> The problem is terminating extensibility without replacement.**

* * *

Summary
-------

*   IsHandled is a valid and necessary mechanism
*   Current guidance addresses correctness of override
*   It does not address preservation of extensibility

* * *

Final Rule
----------

> **Override is allowed.  
> Closing the system is not.**

* * *

Proposed Addition to Guidelines
-------------------------------

Add a section under IsHandled usage:

* * *

### Extensibility Preservation

When implementing full override using IsHandled:
*   The subscriber MUST expose alternative integration events
*   These events SHOULD allow further extensions to participate in the flow
*   The override MUST NOT create a dead-end in the extensibility chain

* * *

Final Thought
-------------

This is not a new pattern.
It is a **minimal extraction of principles already present in the Method pattern**, applied to the most widely used extensibility mechanism in Business Central.
The goal is not to redesign the ecosystem, but to:

> Prevent creation of non-extensible code in an extensible platform.
