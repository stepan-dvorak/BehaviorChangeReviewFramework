# Toward a Mechanism-Independent Review Framework for Behavior-Changing Customizations in Microsoft Dynamics 365 Business Central

**Status:** Research Draft (Working Paper)\
**Author:** Štěpán Dvořák (working draft)\
**Date:** July 2026

------------------------------------------------------------------------

# Abstract

This paper proposes a research direction rather than a finalized design
guideline.

Microsoft has published extensive guidance on individual extensibility
mechanisms such as interfaces, integration events, and the `IsHandled`
pattern. However, the guidance is largely **mechanism-specific**.

This paper explores whether Business Central would benefit from an
additional **mechanism-independent review framework** focused on
**behavior-changing customizations**.

The central hypothesis is **not** that `IsHandled` is inherently wrong.
Instead:

> Whenever a customization significantly changes an established
> effective execution flow, the architectural consequences of that
> change should be reviewed independently of the mechanism used to
> introduce it.

The goal is to complement---not replace---existing Microsoft guidance.

------------------------------------------------------------------------

# Motivation

Microsoft documents several concerns regarding the `IsHandled` pattern:

-   reduced readability,
-   difficult-to-understand execution paths,
-   large numbers of `IsHandled` events,
-   fragile extensibility,
-   recommendation to prefer alternative extensibility mechanisms.

These recommendations are valuable but are attached to individual
mechanisms.

In practice, Business Central partners maintain solutions that combine:

-   Base Application,
-   System Application,
-   localizations,
-   ISV extensions,
-   customer-specific extensions.

Behavior can be altered by many techniques:

-   `IsHandled`,
-   interfaces,
-   strategy implementations,
-   event subscribers,
-   workflow customization,
-   dependency injection,
-   plugin-style delegation.

From an architectural perspective these techniques often produce similar
consequences.

------------------------------------------------------------------------

# Problem Statement

Changing behavior is not unique to `IsHandled`.

Different mechanisms may:

-   redirect execution,
-   suppress standard processing,
-   replace algorithms,
-   introduce new branches,
-   reorder operations,
-   delegate responsibility.

Current guidance explains *how* to use each mechanism.

It provides significantly less guidance for reviewing the architectural
consequences of changing established behavior.

------------------------------------------------------------------------

# Working Terminology

## Execution Flow

The logical progression of execution defined by the software design.

## Effective Execution Flow

The concrete runtime path selected according to runtime conditions.

## Behavior

The externally observable effects produced by execution.

## Behavioral Change

A customization that modifies an established effective execution flow.

## Architectural Significance

A behavioral change becomes architecturally significant when it may
affect properties beyond the immediate implementation.

Examples include:

-   invariants,
-   transaction boundaries,
-   extensibility,
-   observability,
-   security,
-   failure semantics,
-   upgrade compatibility.

------------------------------------------------------------------------

# Existing Microsoft Guidance

Existing documentation already provides valuable guidance on:

-   avoiding unnecessary `IsHandled`,
-   preferring interfaces,
-   designing high-quality events,
-   multi-extension interaction,
-   future evolution,
-   minimum requirements for new `IsHandled` events.

This paper does **not** replace these recommendations.

Instead it attempts to provide a common review framework applicable
regardless of mechanism.

------------------------------------------------------------------------

# Proposed Principle

> A customization that significantly changes an established effective
> execution flow may also change the architectural properties carried by
> that flow.

Therefore:

> Such changes should trigger an architectural review independent of the
> mechanism used.

------------------------------------------------------------------------

# Behavioral Change Review

## Step 1 --- Identify the affected execution flow

What existing behavior is modified?

## Step 2 --- Determine the modification type

Examples:

-   augmentation,
-   interception,
-   substitution,
-   suppression,
-   delegation,
-   reordering.

## Step 3 --- Review architectural properties

Review at least:

-   functional outcome,
-   behavioral contract,
-   data invariants,
-   transaction semantics,
-   security,
-   side effects,
-   observability,
-   extensibility,
-   upgrade compatibility.

## Step 4 --- Document intentional differences

Not every property must remain identical.

Intentional changes should be documented explicitly.

------------------------------------------------------------------------

# Why IsHandled Is Only One Example

`IsHandled` remains an important example because it makes behavioral
replacement highly visible.

However, the same review process should apply to:

-   interface replacement,
-   workflow customization,
-   middleware,
-   plugin architectures,
-   strategy implementations,
-   alternative orchestration mechanisms.

------------------------------------------------------------------------

# Practical Checklist

Before accepting a behavior-changing customization, review:

-   Which execution flow is affected?
-   Which architectural properties does the original flow provide?
-   Which properties remain preserved?
-   Which are intentionally changed?
-   Which extension capabilities remain meaningful?
-   What are the upgrade implications?

------------------------------------------------------------------------

# Future Work

Potential future work includes:

-   precise terminology,
-   formal definition of architecturally significant behavioral change,
-   analyzer support,
-   pull-request templates,
-   reference implementations,
-   real-world examples from Base Application and localization apps.

------------------------------------------------------------------------

# Conclusion

The contribution proposed here is **not** a replacement for Microsoft's
extensibility guidance.

Instead, it proposes a missing integration layer:

A mechanism-independent review methodology for architecturally
significant behavior-changing customizations.

If validated through further research and practical examples, such a
framework could complement existing Business Central guidance while
remaining compatible with current extensibility recommendations.
