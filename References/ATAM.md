---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: REF-ATAM-001
  title: Architecture Tradeoff Analysis Method
  type: Reference Analysis
  version: 0.3.0
  status: Active

classification:
  domain: Software Architecture
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Analyzes the Architecture Tradeoff Analysis Method as evidence for evaluating
  quality-attribute consequences of architecturally significant behavioral
  changes without treating ATAM as the project's final framework.

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
  - References/SAAM.md
  - References/ISO_42030.md

evidence:
  source_authority: SEI Publication
  source_access: Full
  verification: Verified
  limitations: >
    The core analysis uses public SEI reports and current SEI collection
    material. The 2001 book Evaluating Software Architectures was identified
    bibliographically but was not treated as fully accessed evidence.

tags:
  - ATAM
  - architecture-evaluation
  - quality-attributes
  - scenarios
  - architectural-risk
  - tradeoffs
---

# Architecture Tradeoff Analysis Method

## 1. Purpose and Research Question

This document evaluates the Architecture Tradeoff Analysis Method (ATAM) as
evidence for the Orden project. It does not adopt ATAM as the Behavior Change
Review Framework and does not define normative review rules.

The research question is:

> Which ATAM concepts can support evaluation of the quality-attribute
> consequences of architecturally significant behavioral changes, and what
> remains outside ATAM's demonstrated scope?

## 2. Source Scope and Access

### 2.1 Sources examined

The principal source is the complete public SEI technical report *ATAM: Method
for Architecture Evaluation* (CMU/SEI-2000-TR-004). The earlier complete report
*The Architecture Tradeoff Analysis Method* (CMU/SEI-98-TR-008) was used to
confirm the method's original tradeoff-analysis purpose. Current SEI collection
material was used to verify the maintained description and nine-step outline.

Two additional SEI publications provide bounded corroboration:

- *Applicability of General Scenarios to the Architecture Tradeoff Analysis
  Method* reports a comparison of scenarios from five ATAM evaluations with
  general quality-attribute scenarios.
- *SEI Architecture Analysis Techniques and When to Use Them* distinguishes
  ATAM, which assumes a developed software architecture, from the earlier-stage
  Quality Attribute Workshop.

The SEI catalog entry for the 2001 book *Evaluating Software Architectures:
Methods and Case Studies* was located, but the book text was not publicly
verified and is not used for substantive claims here.

### 2.2 Access limitations

The evidence base is authoritative for the stated ATAM method, but it is not a
systematic review of all ATAM research or industrial use. The principal method
report dates from 2000. Current SEI material confirms the method's continuing
description, not the prevalence or effectiveness of its present-day use.

## 3. Verified Source Claims

The following statements report source positions rather than repository
conclusions.

### 3.1 Purpose and evaluation target

The 2000 SEI report defines ATAM's purpose as assessing the consequences of
architectural decisions in light of quality-attribute requirements. It presents
ATAM primarily as a risk-identification method, not as a precise predictor of
runtime quality or as a complete design method [S1, pp. 1-3].

ATAM evaluates a software architecture against business-driven quality goals.
It seeks architectural risks, non-risks, sensitivity points, and tradeoff
points, while also making assumptions and reasoning more explicit [S1, pp.
21-24; S3].

### 3.2 Inputs and prerequisites

The method requires quality-attribute requirements and an architectural
description that articulates architectural decisions. Because these inputs are
often incomplete or ambiguous, ATAM also elicits and refines them [S1, pp.
3-5]. A separate SEI technical note places ATAM after a software architecture
has been developed and presents the Quality Attribute Workshop as an earlier
complement [S5].

Business goals lead to quality-attribute goals. Architectural approaches are
then examined for their contribution to, or inhibition of, those goals [S1,
pp. 7-8].

### 3.3 Scenarios and prioritization

ATAM uses scenarios to make quality-attribute requirements concrete. A
well-formed scenario identifies a stimulus, relevant environmental conditions,
and a measurable or observable response [S1, pp. 13-15].

The report distinguishes three scenario types [S1, pp. 13-16]:

- use case scenarios, which describe current uses of the system;
- growth scenarios, which describe anticipated changes;
- exploratory scenarios, which stress the design and expose boundaries or
  implicit assumptions.

The quality-attribute utility tree connects business drivers to prioritized
quality-attribute scenarios. Stakeholders also brainstorm and vote on a wider
set of scenarios, and highly ranked scenarios become test cases for analyzing
architectural approaches [S1, pp. 16-18, 29-36].

The later SEI study compared scenario evidence from five ATAM evaluations with
general quality-attribute scenarios. Its stated purpose included testing the
coverage of those general scenarios and analyzing risk trends [S4]. This
supports the use of scenarios as empirical evaluation inputs, but it does not
establish that every relevant concern will be elicited.

### 3.4 Outputs and depth of analysis

The 2000 report describes:

- a **risk** as an architecturally important decision that is absent or whose
  consequences are not sufficiently understood;
- a **sensitivity point** as an architectural parameter to which a measurable
  quality-attribute response is highly correlated; and
- a **tradeoff point** as a property that is a sensitivity point for multiple
  quality attributes affected differently by changes to that property [S1, pp.
  3, 21-23].

ATAM does not require extensive formal modeling. Its reasoning may be
qualitative or quantitative, but the report requires it to be predictive,
repeatable, explicit, and recorded. Areas identified by the method are
candidates for deeper modeling, prototyping, design, or analysis [S1, pp.
23-24].

### 3.5 The nine-step method

The maintained SEI description and the 2000 report identify nine steps [S1,
pp. 7-8; S3]:

1. Present ATAM.
2. Present business drivers.
3. Present the architecture.
4. Identify architectural approaches.
5. Generate the quality-attribute utility tree.
6. Analyze architectural approaches against the high-priority concerns.
7. Brainstorm and prioritize scenarios with stakeholders.
8. Analyze architectural approaches against the prioritized scenarios.
9. Present the results.

These steps organize a stakeholder-intensive architecture evaluation. They do
not constitute a lightweight code-review checklist without adaptation.

## 4. Repository Observations

The following observations concern the current Orden research problem rather
than claims made by the ATAM sources.

1. A behavior-changing customization can embody or alter architectural
   decisions relevant to multiple quality attributes, even when the code change
   appears local.
2. Current project examples and Microsoft analyses raise concerns such as
   modifiability, security, reliability, observability, and extensibility. These
   are potential evaluation concerns, but not every one is a term or output
   defined by ATAM.
3. ATAM's scenario model provides a way to express an observable response to a
   stimulus and environment. This is compatible with examining changed
   behavior, but compatibility is not equivalence.
4. The repository does not yet contain evidence that a behavioral change, by
   itself, is an ATAM-defined evaluation trigger.

## 5. Research Interpretation

### 5.1 What ATAM contributes

ATAM provides strong precedent for evaluating architecture by tracing from
business drivers and concrete scenarios through architectural decisions to
quality-attribute consequences. Its contribution to Orden is therefore
methodological: it demonstrates a structured way to expose risk and cross-
attribute interaction without reducing evaluation to the implementation
mechanism.

Growth scenarios are particularly relevant when a customization changes how a
system accommodates future modifications. Use case scenarios can express
current behavioral expectations. Exploratory scenarios can probe failure,
scale, upgrade, concurrency, or composition conditions that reveal hidden
assumptions. This mapping is a repository interpretation; ATAM does not define
Business Central-specific scenario categories.

Sensitivity and tradeoff analysis may also help distinguish a merely local
change from a change whose architectural parameters affect several qualities.
However, ATAM does not provide a ready-made threshold for "architectural
significance" in the sense currently under investigation by Orden.

### 5.2 What ATAM does not establish

The examined sources do not establish that:

- every behavior-changing customization requires a full ATAM evaluation;
- behavioral change is a named ATAM trigger;
- execution flow is an ATAM architectural entity;
- ATAM supplies Business Central-specific quality models or mechanisms;
- scenario analysis alone proves preservation of contracts, invariants, or
  extension participation; or
- ATAM predicts exact runtime outcomes from incomplete architecture evidence.

Consequently, ATAM narrows the research gap but does not close it. It supports
evaluation of consequences once relevant decisions, qualities, and scenarios
are in scope; it does not determine when every customization must enter that
evaluation or how the evaluation should be scaled for routine extension work.

## 6. Relevance to the Main Research Question

The project's main question asks whether a mechanism-independent review method
already exists and what integration may still be required for Business
Central. ATAM supplies a mature architecture-evaluation backbone for
quality-attribute consequences and tradeoffs. This is negative evidence against
claiming that Orden invents architecture evaluation itself.

The remaining candidate contribution is narrower: identify defensible review
entry conditions for behavior-changing customizations, translate affected
behavior into evaluable scenarios and architectural decisions, select relevant
quality concerns, and scale the depth of review to the evidence and risk. That
integration remains a hypothesis until it is tested against other literature
and Business Central evidence.

## 7. Candidate Implications for the Framework

The following are non-normative candidates for later synthesis:

1. Trace a proposed change from its business driver to affected
   quality-attribute concerns rather than beginning with its extension
   mechanism.
2. Express important current, anticipated, and boundary behavior as scenarios
   with an explicit stimulus, environment, and observable response.
3. Identify the architectural decisions or parameters changed by the
   customization before judging consequences.
4. Look for risks, sensitivity points, and tradeoff points across multiple
   quality concerns.
5. Record qualitative reasoning explicitly and escalate identified hotspots to
   deeper analysis where the available evidence is insufficient.
6. Adapt the ceremony and participant model rather than assuming that a full
   multi-day ATAM evaluation is proportionate to every customization.

These candidates reuse ATAM concepts but do not yet define framework rules.

## 8. Limitations and Threats to Validity

- **Source age:** The principal method specification is from 2000. Current SEI
  material confirms the method description but does not independently validate
  all original claims.
- **Selection bias:** This analysis concentrates on official SEI sources and
  does not systematically compare independent evaluations or criticisms.
- **Transferability:** ATAM was designed for architecture evaluation. Applying
  selected concepts to extension-level review may omit organizational and
  analytical conditions on which the full method relies.
- **Granularity:** The sources do not prescribe how to scale ATAM concepts to a
  single Business Central customization.
- **Evidence gap:** No Business Central case has yet been evaluated using the
  candidate ATAM mapping in this document.
- **Coverage:** Security, extensibility, transaction behavior, upgrade
  compatibility, and observability require quality-specific evidence beyond a
  generic ATAM process.

## 9. Unresolved Questions and Future Research

1. Which observable properties of a Business Central behavioral change can be
   expressed adequately as quality-attribute scenarios?
2. What evidence justifies initiating architectural review before the affected
   quality attributes are already known?
3. Can a lightweight, repeatable subset of ATAM preserve useful traceability
   without implying equivalence to a formal ATAM evaluation?
4. Which quality-specific analyses are required for transaction boundaries,
   security, extensibility, observability, and upgrade compatibility?
5. How should stakeholder roles be represented when a platform vendor,
   extension publisher, customer, and other extensions influence the same
   behavior?
6. What does SAAM add for modification-oriented scenarios, and where would an
   ATAM-derived mapping duplicate it?
7. Does empirical application to existing Business Central cases expose risks
   that the current mechanism-specific guidance does not reveal?

## 10. References

- **[S1]** Kazman, Rick, Mark Klein, and Paul Clements. *ATAM: Method for
  Architecture Evaluation*. CMU/SEI-2000-TR-004, Software Engineering
  Institute, Carnegie Mellon University, 2000.
  <https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf>
- **[S2]** Kazman, Rick, Mark Klein, Mario Barbacci, Thomas Longstaff, Howard
  Lipson, and Jeromy Carriere. *The Architecture Tradeoff Analysis Method*.
  CMU/SEI-98-TR-008, Software Engineering Institute, Carnegie Mellon
  University, 1998.
  <https://www.sei.cmu.edu/documents/1186/1998_005_001_16646.pdf>
- **[S3]** Software Engineering Institute. *Architecture Tradeoff Analysis
  Method Collection*. Carnegie Mellon University.
  <https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/>
- **[S4]** Bass, Len, Mark Klein, and Gabriel Moreno. *Applicability of General
  Scenarios to the Architecture Tradeoff Analysis Method*.
  CMU/SEI-2001-TR-014, Software Engineering Institute, Carnegie Mellon
  University, 2001. <https://doi.org/10.1184/R1/6571970.v1>
- **[S5]** Barbacci, Mario R. *SEI Architecture Analysis Techniques and When to
  Use Them*. CMU/SEI-2002-TN-005, Software Engineering Institute, Carnegie
  Mellon University, 2002. <https://doi.org/10.1184/R1/6583727.v1>

## 11. Revision History

### 0.3.0 — 2026-07-18

- Replaced the research stub with a substantive reference analysis.
- Verified ATAM purpose, inputs, scenarios, outputs, steps, and analytical
  limits against primary SEI sources.
- Distinguished source claims, repository observations, interpretation,
  candidate implications, limitations, and unresolved questions.

### 0.2.0

- Established the governed research-stub structure and permanent document ID.
