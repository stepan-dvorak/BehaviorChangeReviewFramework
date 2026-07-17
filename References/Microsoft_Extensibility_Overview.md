---
metadata_schema: "1.0"
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: REF-MS-EXT-001
  title: Microsoft Extensibility Overview Analysis
  type: Reference Analysis
  version: 0.2.0
  status: Active
classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Review
owner: Štěpán Dvořák
purpose: >
  Analyzes Microsoft's documented Business Central extensibility philosophy and
  separates explicit guidance from architectural implications and open gaps.
quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft
audience:
  - Researchers
  - Contributors
  - AI Assistants
depends_on:
  - 00_Project_Charter.md
  - 01_Terminology.md
  - 02_Research_Methodology.md
  - 03_Related_Work.md
related_documents:
  - References/Microsoft_IsHandled_v2.0.md
evidence:
  source_authority: Official Vendor Documentation
  source_access: Full
  verification: Partial
  limitations: >
    The analysis is limited to the cited Microsoft Learn material and its
    architectural interpretation has not yet received independent review.
tags:
  - reference
  - Microsoft
  - Business-Central
  - extensibility
  - platform-architecture
---

# Microsoft_Extensibility_Overview.md

# Purpose

This document analyzes Microsoft's official concept of **extensibility** in Dynamics 365 Business Central.

The objective is **not** to explain AL extensibility mechanisms individually.

The objective is to determine:

* Microsoft's architectural philosophy regarding extensibility.
* Which architectural principles are explicitly documented.
* Which principles are only implied.
* Which aspects remain undocumented and may justify this research project.

---

# Microsoft Position

## Extensibility is a platform capability

Microsoft presents extensibility as a fundamental capability of the Business Central platform rather than as a feature of individual AL language constructs.

The official overview states that developers can extend:

* tables
* pages
* reports
* enumerations
* application areas
* security model
* AL code flows (events)

The platform is intentionally designed around extension rather than source modification.

### Evidence

Microsoft Learn — **Extensibility overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

---

## Business Central is architecturally layered

Microsoft explicitly describes Business Central as consisting of multiple architectural layers.

At minimum:

* System Application
* Base Application
* Extensions

The System Application is open source and intended as reusable platform functionality.

The Base Application contains business functionality.

Customer and partner extensions are expected to build on these layers.

### Evidence

Microsoft Learn — **Extensibility overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

---

## Extensibility is intended to support evolution

The purpose of extensibility is not only customization.

It is also intended to support:

* maintainability
* modularity
* future upgrades
* separation of concerns
* independent evolution

### Evidence

Microsoft Learn — **Extension objects overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extension-object-overview

Runtime 13 introduced extension objects within the same application specifically to support **separation of concerns** and non-disruptive refactoring.

---

## Events extend code flow

Microsoft explicitly identifies events as the mechanism for extending existing AL code flows.

Events allow custom functionality to remain outside the original implementation.

### Evidence

Microsoft Learn — **Extensibility overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

Section:

> Extending AL code flows: events

---

# Architectural Principles Found

## Principle 1

### Prefer extension over modification

Business Central is designed around extending existing functionality instead of modifying Microsoft source code.

### Evidence

Microsoft Learn — Extensibility overview

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

---

## Principle 2

### Preserve upgradeability

The architectural model assumes that customer customizations should survive future platform evolution.

Extensibility mechanisms exist primarily to support long-term upgrade compatibility.

### Evidence

Microsoft Learn — Extensibility overview

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

---

## Principle 3

### Separation of concerns

Runtime 13 allows extension objects to coexist with their targets inside one application.

Microsoft explicitly states this supports separation of concerns and non-disruptive refactoring.

### Evidence

Microsoft Learn — Extension objects overview

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extension-object-overview

---

## Principle 4

### Multiple extensibility mechanisms coexist

Microsoft intentionally provides different mechanisms.

Examples include:

* Events
* Interfaces
* Extension objects
* Enums
* Permission extensions

The documentation does not present one universal mechanism.

### Evidence

Microsoft Learn — Extensibility overview

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

---

# What Microsoft Explicitly Documents

The documentation clearly explains:

* how extensibility works;
* available mechanisms;
* platform architecture;
* supported extension points;
* modularity;
* upgrade model.

---

# What Microsoft Only Implicitly States

Across the documentation Microsoft consistently encourages:

* extensibility preservation;
* composability;
* separation of concerns;
* maintainability;
* future evolution.

However these recommendations are distributed across many articles.

No single architectural document unifies them.

---

# What Is Not Explicitly Documented

At the time of writing, no Microsoft Learn article has been identified that explicitly defines a general review methodology for behavior-changing customizations.

Specifically, no guidance has yet been found describing:

* when a behavior change becomes architecturally significant;
* when architectural review should be triggered;
* how behavior-changing customizations should be reviewed independently of implementation mechanism;
* how architectural concerns should be evaluated after replacing established behavior.

This observation is provisional and must remain subject to revision if additional Microsoft guidance is discovered.

---

# Relationship to IsHandled

This document intentionally avoids treating `IsHandled` as the primary subject.

`IsHandled` is one extensibility mechanism.

The architectural principles identified here apply equally to:

* interfaces,
* event subscribers,
* workflow customization,
* strategy implementations,
* other extensibility techniques.

---

# Analysis

The official Microsoft documentation consistently presents extensibility as an architectural capability.

It also promotes modularity, upgradeability and separation of concerns.

However, these principles are documented individually rather than as one coherent architectural review methodology.

Current evidence suggests that Microsoft's documentation answers:

> **How should Business Central be extended?**

It answers less explicitly:

> **How should architecturally significant behavior-changing customizations be reviewed?**

Whether this constitutes a genuine documentation gap remains an open research question.

---

# Relevance to the Project

This document provides evidence that:

* extensibility is already treated architecturally by Microsoft;
* behavior modification occurs within an extensible architectural model;
* the proposed research should complement Microsoft's guidance rather than replace it.

The potential contribution therefore shifts from inventing new architectural concepts to integrating existing guidance into a mechanism-independent review framework.

---

# Open Questions

1. Does Microsoft define architectural review elsewhere outside Microsoft Learn?
2. Is architectural significance discussed under another terminology?
3. Can Microsoft's event-quality guidance be generalized into a mechanism-independent review process?
4. Which documented architectural concerns should become mandatory review categories?

---

# Primary Sources

1. Microsoft Learn — **Extensibility overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensibility-overview

2. Microsoft Learn — **Extension objects overview**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extension-object-overview

3. Microsoft Learn — **Types of events for extensibility**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/types-of-events-for-extensibility

4. Microsoft Learn — **Create an extensibility request**

https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/create-extensibility-request

---

# Revision History

## 0.1

Initial analytical draft.

```
```
