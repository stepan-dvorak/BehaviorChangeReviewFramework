---
project:
  id: Orden
document:
  title: AI Contribution Guidelines
  filename: CONTRIBUTING_FOR_AI-alpha-03-revised.md
  version: 0.3-alpha03-revised
  status: Draft
classification:
  layer: Operational
  domain: Governance
---

# AI Contribution Guidelines

> **Alpha 03 (Revised)** – Reasoning Integration

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

The AI SHALL:
- follow repository standards;
- preserve architectural consistency;
- distinguish evidence from conclusions;
- recommend governance improvements without applying them autonomously.

The AI SHALL NOT define repository policy.

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

Conflicts SHALL be reported explicitly.

# 3. Operational Workflow

Thinking SHALL complete before execution.
Validation SHALL precede delivery.

# 4. Execution Context Resolution

## Purpose

Before performing repository work, the AI SHALL establish an execution context.

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

The AI SHALL resolve execution context before reasoning begins.
Missing context SHALL be identified explicitly.
Material ambiguity SHOULD be resolved before implementation.

# 5. Knowledge Model Construction

## Purpose

The AI SHALL construct an internal Knowledge Model from authoritative
Knowledge Sources.

Reasoning SHALL operate on the Knowledge Model rather than directly on source
documents.

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

Contradictory sources SHALL remain distinguishable until resolved by reasoning.

# 6. Reasoning

## Purpose

Reasoning transforms the Knowledge Model into validated conclusions suitable
for repository implementation.

This document defines WHEN reasoning occurs.

Reasoning_Standard.md defines HOW reasoning is performed.

## Inputs

Reasoning SHALL operate on:
- resolved execution context;
- constructed Knowledge Model;
- applicable repository governance.

## Responsibilities

The AI SHALL:
- distinguish evidence from interpretation;
- preserve uncertainty until resolved;
- avoid unsupported assumptions;
- identify conflicting evidence;
- maintain traceability;
- derive conclusions from evidence.

## Outputs

Reasoning SHALL produce:
- validated conclusions;
- identified uncertainty;
- documented assumptions;
- implementation-ready decisions.

Only validated conclusions SHALL proceed to Artifact Realization.

# 7. Artifact Realization

Transform validated reasoning into repository artifacts.

No new architectural decisions SHALL be introduced.

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
