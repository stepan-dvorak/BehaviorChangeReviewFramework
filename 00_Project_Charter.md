---
project: Behavior Change Review Framework
status: draft
version: 0.1
---

# 00_Project_Charter.md

# Vision

Create a rigorous, research-based framework for reviewing
architecturally significant behavior-changing customizations in
Microsoft Dynamics 365 Business Central.

The project does **not** aim to replace Microsoft's extensibility
guidance. Instead, it aims to complement existing guidance with a
mechanism-independent review methodology.

------------------------------------------------------------------------

# Background

The research originated from practical experience with the `IsHandled`
extensibility pattern.

During the investigation it became clear that the observed architectural
questions are **not specific to IsHandled**.

The same class of problems appears whenever an established behavior is
modified through mechanisms such as:

-   IsHandled
-   Interfaces
-   Strategy implementations
-   Event subscribers
-   Workflow customization
-   Delegation
-   Plugin architectures

Therefore, IsHandled is treated as an initial case study rather than the
subject of the research.

------------------------------------------------------------------------

# Primary Research Question

Can a mechanism-independent review framework be defined for
architecturally significant behavior-changing customizations in Business
Central?

------------------------------------------------------------------------

# Secondary Research Questions

-   Does existing software architecture literature already define this
    framework?
-   Which terminology already exists?
-   Which parts are already documented by Microsoft?
-   Which guidance is currently missing?
-   How can general architectural principles be applied consistently to
    Business Central?

------------------------------------------------------------------------

# Scope

The project investigates:

-   behavior-changing customizations,
-   execution-flow modifications,
-   architectural review,
-   behavioral contracts,
-   extensibility implications,
-   practical review methodology.

------------------------------------------------------------------------

# Out of Scope

The project does not attempt to:

-   replace Microsoft Learn,
-   redesign Business Central extensibility,
-   deprecate IsHandled,
-   introduce unnecessary terminology,
-   define a new software architecture style.

------------------------------------------------------------------------

# Working Hypothesis

A significant change to an established effective execution flow may also
modify architectural properties carried by that flow.

Those impacts should be reviewed independently of the implementation
mechanism.

Status: **Unverified**

------------------------------------------------------------------------

# Expected Contribution

The intended contribution is not a new extensibility mechanism.

The intended contribution is a practical review framework that:

-   complements existing Microsoft guidance,
-   is independent of implementation mechanism,
-   is grounded in established architectural literature,
-   is validated against real Business Central code.

------------------------------------------------------------------------

# Deliverables

Research documents:

-   00_Project_Charter.md
-   00_Research_Log.md
-   01_Terminology.md
-   02_Research_Methodology.md
-   03_Related_Work.md
-   04_Existing_BC_Guidance.md
-   05_Framework.md
-   06_BC_Pattern_Catalog.md
-   07_Example_Catalog.md
-   08_Decision_Tree.md
-   Whitepaper.md

Supporting artifacts:

-   Example repository
-   Review checklist
-   Pull request template
-   Analyzer ideas

------------------------------------------------------------------------

# Success Criteria

The project will be considered successful if it demonstrates one of the
following:

1.  Existing literature already contains a complete solution (valuable
    negative result).
2.  Existing concepts can be integrated into a coherent Business Central
    methodology.
3.  A defensible mechanism-independent review framework can be justified
    and supported with evidence.

------------------------------------------------------------------------

# Guiding Principles

-   Follow evidence before intuition.
-   Prefer existing terminology.
-   Distinguish observations from conclusions.
-   Validate hypotheses against literature and real code.
-   Keep Business Central examples practical and reproducible.

------------------------------------------------------------------------

# Revision History

## 0.1

Initial project charter.
