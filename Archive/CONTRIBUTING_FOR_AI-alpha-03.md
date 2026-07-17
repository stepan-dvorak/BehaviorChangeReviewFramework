---
project:
  id: Orden
document:
  title: AI Contribution Guidelines
  filename: CONTRIBUTING_FOR_AI-alpha-03.md
  version: 0.3-alpha03
  status: Draft
classification:
  layer: Operational
  domain: Governance
---

# AI Contribution Guidelines

> Alpha 03 – Reasoning Integration

## Purpose

This document defines the operational workflow that AI assistants SHALL follow
when contributing to the Orden repository.

Repository policy is defined by governance standards. This document defines how
those standards are operationally applied.

# AI Contribution Workflow

Part I — Thinking
1. AI Role
2. Decision Hierarchy
3. Operational Workflow
4. Execution Context Resolution
5. Knowledge Model Construction
6. Reasoning

Part II — Execution
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

The AI SHALL operate as an implementation assistant within repository governance.

# 2. Decision Hierarchy

1. Governance_Principles.md
2. Repository_Standards.md
3. Repository_Architecture.md
4. Repository_Taxonomy.md
5. Editorial_Style_Guide.md
6. Reasoning_Standard.md
7. Document-specific guidance
8. Current task

# 3. Operational Workflow

Thinking SHALL complete before execution.
Validation SHALL precede delivery.

# 4. Execution Context Resolution

The execution context SHALL define repository layer, artifact type,
dependencies, governing standards, intended audience and expected deliverable.

# 5. Knowledge Model Construction

Reasoning SHALL operate on an internal Knowledge Model constructed from
authoritative Knowledge Sources.

The model SHALL preserve:

- evidence;
- terminology;
- uncertainty;
- traceability.

# 6. Reasoning

## Purpose

Reasoning transforms the Knowledge Model into validated conclusions suitable
for repository implementation.

This document intentionally delegates reasoning methodology to
Reasoning_Standard.md.

## Inputs

Reasoning SHALL operate on:

- the resolved execution context;
- the constructed Knowledge Model;
- applicable repository governance.

## Responsibilities

The AI SHALL:

- distinguish evidence from interpretation;
- preserve uncertainty until resolved;
- avoid unsupported assumptions;
- identify conflicting evidence;
- maintain traceability;
- derive conclusions from evidence.

## Separation of Responsibilities

This document defines WHEN reasoning occurs.

Reasoning_Standard.md defines HOW reasoning is performed.

The operational workflow SHALL reference rather than duplicate reasoning rules.

## Outputs

Reasoning SHALL produce:

- validated conclusions;
- identified uncertainty;
- documented assumptions;
- implementation-ready decisions.

Only validated conclusions SHALL proceed to Artifact Realization.

# 7. Artifact Realization

Transform validated conclusions into repository artifacts.

No new architectural decisions SHALL be introduced.

# 8. Validation

Verify governance, structural, editorial and technical compliance.

# 9. Delivery

Deliver validated artifacts without additional reasoning.

# 10. Governance Evolution

Recommend governance improvements based on recurring patterns.
Governance changes require repository owner approval.

# References

- Governance_Principles.md
- Repository_Standards.md
- Repository_Architecture.md
- Repository_Taxonomy.md
- Editorial_Style_Guide.md
- Reasoning_Standard.md
