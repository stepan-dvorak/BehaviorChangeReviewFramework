---
project:
  id: Orden
document:
  title: AI Contribution Guidelines
  filename: CONTRIBUTING_FOR_AI-alpha-02.md
  version: 0.2-alpha02
  status: Draft
classification:
  layer: Operational
  domain: Governance
---

# AI Contribution Guidelines

> **Alpha 02** – Execution Context & Knowledge Model

## Purpose

This document defines the operational workflow that AI assistants SHALL follow
when contributing to the Orden repository.

Repository policy is defined by governance standards. This document defines how
those standards are applied during execution.

## Scope

This document applies to all AI-assisted creation, modification and review of
repository artifacts.

# AI Contribution Workflow

## Part I — Thinking

1. AI Role
2. Decision Hierarchy
3. Operational Workflow
4. Execution Context Resolution
5. Knowledge Model Construction
6. Reasoning

## Part II — Execution

7. Artifact Realization
8. Validation
9. Delivery
10. Governance Evolution

Workflow

Task
 |
 v
Execution Context Resolution
 |
 v
Knowledge Sources
 |
 v
Knowledge Model
 |
 v
Reasoning
 |
 v
Artifact Realization
 |
 v
Validation
 |
 v
Delivery
 |
 v
Governance Evolution

# 1. AI Role

The AI acts as an implementation assistant within repository governance.
It SHALL follow repository standards and SHALL NOT redefine governance.

# 2. Decision Hierarchy

Priority:

1. Governance_Principles.md
2. Repository_Standards.md
3. Repository_Architecture.md
4. Repository_Taxonomy.md
5. Editorial_Style_Guide.md
6. Reasoning_Standard.md
7. Document-specific guidance
8. Current task

Conflicts SHALL be reported.

# 3. Operational Workflow

Thinking SHALL complete before execution.

Validation SHALL precede delivery.

# 4. Execution Context Resolution

## Purpose

Before performing any repository work, the AI SHALL establish an execution
context describing the environment in which the task is performed.

## Required Context

The execution context SHALL identify:

- repository layer;
- artifact type;
- intended audience;
- document classification;
- governing standards;
- document dependencies;
- expected deliverable.

## Context Resolution Principles

The AI SHALL resolve the execution context before reasoning begins.

Missing context SHALL be identified explicitly rather than assumed.

Material ambiguity SHOULD be resolved before implementation.

# 5. Knowledge Model Construction

## Purpose

The AI SHALL construct an internal Knowledge Model from authoritative
Knowledge Sources.

Reasoning SHALL operate on the Knowledge Model rather than directly on
individual source documents.

## Knowledge Sources

Knowledge Sources MAY include:

- governance documents;
- repository standards;
- architecture documents;
- research;
- evidence;
- referenced specifications.

## Knowledge Model Principles

The Knowledge Model SHALL:

- preserve source meaning;
- separate evidence from interpretation;
- maintain traceability;
- record uncertainty where appropriate.

Contradictory sources SHALL remain distinguishable until resolved by
reasoning.

# 6. Reasoning

Reasoning SHALL follow Reasoning_Standard.md.

# 7. Artifact Realization

Transform validated reasoning into repository artifacts.

# 8. Validation

Verify governance, structural, editorial and technical consistency.

# 9. Delivery

Deliver validated artifacts without introducing additional reasoning.

# 10. Governance Evolution

Recommend governance improvements based on recurring patterns.
Repository governance SHALL only change with repository owner approval.

# References

- Governance_Principles.md
- Repository_Standards.md
- Repository_Architecture.md
- Repository_Taxonomy.md
- Editorial_Style_Guide.md
- Reasoning_Standard.md
