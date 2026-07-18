# Behavior Change Review Framework

This public research repository investigates a mechanism-independent framework
for reviewing architecturally significant behavior-changing customizations in
Microsoft Dynamics 365 Business Central.

The project integrates software architecture standards, Microsoft guidance,
technical literature, and empirical evidence. Its intended contribution is a
practical Business Central specialization of established architecture concepts,
not a new extensibility mechanism or architecture style.

## Research Status

The project is active research. The central hypothesis, terminology, and
framework remain subject to evidence-based validation. Documents explicitly
marked as research stubs identify planned work and do not contain established
conclusions.

## Scope

The research examines architectural consequences when a customization changes,
suppresses, replaces, or redirects established system behavior. The review
question is independent of whether the change is implemented through
`IsHandled`, events, interfaces, Strategy implementations, delegation,
workflows, or another extensibility mechanism.

The repository does not provide a general catalog of AL patterns, prescribe a
single extensibility mechanism, or claim that every behavior change is
architecturally significant.

## Recommended Reading Order

1. [Project Charter](00_Project_Charter.md) — research purpose, scope, and
   intended contribution.
2. [Research Methodology](02_Research_Methodology.md) — evidence and validation
   method.
3. [Working Terminology](01_Terminology.md) — current concepts and their status.
4. [Related Work](03_Related_Work.md) — adjacent standards, methods, and
   literature.
5. [ISO, SEI, and Microsoft analyses](References/) — source-specific research.
6. [Empirical studies](Empirical/) — case evidence and its limitations.
7. [Research draft](Whitepaper/Behavior_Change_Review_Framework_for_Business_Central_Research_Draft.md)
   — current synthesis, not a final framework.

## Repository Guidance

- [Repository Standards](Repository_Standards.md) define artifact profiles,
  metadata, lifecycle, language, naming, and maintenance rules.
- [Repository Taxonomy](Repository_Taxonomy.md) defines artifact categories and
  directory responsibilities.
- [Repository Index](Repository_Index.yaml) is the machine-readable inventory
  and retrieval router.
- [AI Contribution Guidelines](Contributing_for_AI.md) define the workflow for
  AI-assisted changes.

Repository navigation does not override governance, evidence, canonical
terminology, or human review.

## Local Metadata Validation

Install the validation dependencies and run the baseline check:

```text
python -m pip install -r requirements-validation.txt
python Scripts/Validate_Repository_Metadata.py
```

The baseline check reports approved migration gaps as warnings. Use
`python Scripts/Validate_Repository_Metadata.py --strict` to require every active
Markdown artifact to conform immediately.
