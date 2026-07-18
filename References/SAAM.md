---
metadata_schema: "1.0"

project:
  id: Orden
  name: Behavior Change Review Framework

document:
  id: REF-SAAM-001
  title: Software Architecture Analysis Method
  type: Reference Analysis
  version: 0.3.0
  status: Active

classification:
  domain: Software Architecture
  layer: Study
  maturity: Draft

owner: Štěpán Dvořák

purpose: >
  Analyzes the Software Architecture Analysis Method as evidence for using
  scenarios to examine how architectures support behavior and anticipated
  change without treating SAAM as the project's final framework.

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
  - References/ATAM.md
  - References/ISO_42030.md

evidence:
  source_authority: Mixed Sources
  source_access: Full
  verification: Verified
  limitations: >
    The core evidence consists of complete public copies of the original 1994
    ICSE paper and the authors' 1996 scenario-based analysis paper, both hosted
    by the Software Engineering Institute. The analysis does not claim access
    to the complete 2001 book treatment of SAAM.

tags:
  - SAAM
  - architecture-analysis
  - scenarios
  - modifiability
  - change-impact
  - scenario-interaction
---

# Software Architecture Analysis Method

## 1. Purpose and Research Question

This document evaluates the Software Architecture Analysis Method (SAAM) as
evidence for the Orden project. It does not adopt SAAM as the Behavior Change
Review Framework and does not establish normative review rules.

The research question is:

> How does SAAM use scenarios to evaluate architectural support for current
> behavior and anticipated change, and which parts can inform review of
> behavior-changing customizations without exceeding the method's demonstrated
> scope?

## 2. Source Scope and Access

### 2.1 Sources examined

The principal sources are complete public copies of two original publications:

- *SAAM: A Method for Analyzing the Properties of Software Architectures*,
  published in the proceedings of the 16th International Conference on Software
  Engineering in 1994 and republished in the SEI digital library; and
- *Scenario-Based Analysis of Software Architecture*, published in *IEEE
  Software* in 1996 and made publicly available by the SEI.

The 1994 paper introduces a five-activity method and demonstrates it by
comparing three user-interface architectures for modifiability. The 1996 paper
reports the evolved, stable set of SAAM activities, distinguishes direct and
indirect scenarios, and draws lessons from several applications.

Current SEI historical material was used to corroborate SAAM's place as the
SEI's first architecture analysis method and its relationship to ATAM. A 1996
SAAMtool paper was used only to contextualize scenario traceability and tool
support.

### 2.2 Access and historical limitations

The SEI catalog dates its copy of the original SAAM paper to 2007, while the
paper itself is the 1994 ICSE publication. This analysis cites the original
publication year and records both its DOI and the stable public SEI copy.

The sources describe an early and evolving method. The 1994 paper lists five
domain-oriented activities; the 1996 paper explicitly says that the prescribed
steps evolved through experience and presents a different stable five-step
form. This document reports that evolution rather than silently combining the
two formulations.

## 3. Verified Source Claims

The following statements report source positions rather than repository
conclusions.

### 3.1 Purpose and evaluation basis

The 1994 paper proposes SAAM to describe and analyze architectures with respect
to organizational life-cycle concerns such as maintainability, portability,
modularity, and reusability. Its case study evaluates modifiability, not every
quality attribute [S1, pp. 81-82, 87-89].

The authors argue that an architecture is not intrinsically good or bad. It can
only be judged relative to the needs and goals of the organization using it.
Abstract qualities such as modifiability must therefore be made concrete
through representative tasks or scenarios [S1, pp. 87-88].

The 1996 paper describes scenarios as brief narratives of expected or
anticipated system use from development-time and end-user viewpoints. Scenarios
represent context-dependent instances of qualities and focus analysis on how
well an architecture satisfies each instance [S2, pp. 1-4].

### 3.2 The original five activities

The 1994 formulation lists five activities [S1, pp. 81-82]:

1. Characterize a canonical functional partitioning for the domain.
2. Map that functional partitioning onto the architecture's structural
   decomposition.
3. Select the quality attributes against which to assess the architecture.
4. Select concrete tasks that test the desired attributes.
5. Evaluate how well each architecture supports each task.

The paper describes architecture through functionality, structure, and the
allocation of function to structure. It uses that common characterization to
compare architectural alternatives [S1, pp. 81-83].

### 3.3 The evolved scenario-based activities

The 1996 paper states that SAAM evolved through application and presents the
following stable set of activities [S2, pp. 4-6]:

1. Describe the candidate architecture or architectures.
2. Develop scenarios covering important activities and anticipated changes
   from relevant stakeholder roles.
3. Evaluate each scenario against the architecture.
4. Reveal interactions among indirect scenarios.
5. Weight scenarios and interactions to produce an overall, context-dependent
   evaluation.

Architecture description and scenario development are interdependent. The
appropriate architectural granularity depends on the scenarios, while scenario
development depends on the activities the architecture must support [S2, pp.
5-6].

### 3.4 Direct and indirect scenarios

The 1996 paper calls a scenario **direct** when the architecture can support it
without modification. It calls a scenario **indirect** when supporting it
requires an architectural change, such as changing or adding a component or
connection [S2, pp. 4-5].

For each indirect scenario, SAAM identifies the affected components and
connections and estimates the cost or difficulty of the necessary changes. The
authors allow simple impact counts or more sophisticated cost functions [S2,
pp. 5, 8-9].

Direct scenarios can also help expose static connections and describe dynamic
behavior. The sources therefore do not restrict direct scenarios to
requirements confirmation or indirect scenarios to maintenance planning [S2,
pp. 5-6].

### 3.5 Scenario interaction

Indirect scenarios interact when they require changes to the same architectural
component or connection. SAAM uses these interactions to examine separation of
concerns, coupling, and cohesion relative to the selected scenarios [S2, pp.
5, 9, 12-13].

The 1996 paper warns, in effect, that interaction requires interpretation. If
interacting scenarios belong to the same class, their concentration may
indicate appropriate cohesion. If they belong to different classes, interaction
may reveal an architectural description at the wrong level of detail or a
component that does not adequately separate concerns [S2, pp. 12-13].

Accordingly, a high count of interacting scenarios is not, without examining
scenario classes and architectural granularity, a universal defect metric.

### 3.6 Evaluation outputs and limits

SAAM produces per-scenario analyses rather than one universal architecture
metric. Stakeholders determine the relative importance of scenarios and
interactions according to organizational requirements [S2, pp. 5-6].

The 1994 paper characterizes its assessment as qualitative and states that it
does not provide predictive metrics. It also distinguishes architectural
support from language or tool support, which may affect the practical cost of a
change without being visible in the architectural description [S1, pp. 82,
89].

The 1996 paper states that not every scenario has architecture-level
implications and that some concerns cannot be evaluated from architectural
information alone. It also compares scenario sufficiency to test sufficiency:
complete coverage cannot be proved merely by generating scenarios [S2, pp. 4,
13].

### 3.7 Human and organizational role

The reported applications emphasize SAAM's social and communicative effects.
Scenario elicitation forces stakeholders to discuss current and future uses,
reach agreement on relevant concerns, and refine architectural descriptions
[S2, pp. 7, 11-13].

The SAAMtool paper shows that scenarios were also treated as reusable and
traceable design rationale: they could be stored, related to architectural
views, reused for coverage or regression analysis, and connected to other
scenarios [S4, pp. 1-2]. This describes tool support associated with SAAM; it is
not a mandatory property established by the original method paper.

## 4. Repository Observations

The following observations concern Orden and are not claims made by the SAAM
authors.

1. A behavior-changing customization may correspond to an indirect scenario
   when the desired behavior is not supported by the architecture without a
   change. The concepts are not equivalent: indirectness is relative to one
   scenario and one architecture.
2. A customization may make a previously indirect scenario direct by adding an
   extension or configuration capability. That change can still have
   architectural consequences not measured by the original scenario.
3. Mapping affected behavior to components, connections, and architectural
   views could expose impact that mechanism-specific review misses.
4. Multiple changes affecting the same component do not automatically prove
   poor design. Their scenario classes, shared responsibility, and the level of
   architectural description must be examined.
5. The repository does not yet contain evidence that SAAM defines behavioral
   change itself as a review trigger.

## 5. Research Interpretation

### 5.1 What SAAM contributes

SAAM provides direct precedent for replacing an abstract question such as "Is
this architecture modifiable?" with contextual questions about how the
architecture supports specific current uses and anticipated changes. This is
highly relevant to Orden because it connects a proposed change to explicit
architectural impact rather than to the extension mechanism used.

The direct/indirect distinction can help establish a baseline: first determine
whether the current architecture already supports the desired scenario; if not,
identify which architectural elements must change. The affected elements and
estimated change effort are evidence for impact analysis, not a complete
judgment about architectural significance.

Scenario interaction provides a candidate way to investigate whether multiple
behavioral changes accumulate in architectural hotspots or reveal cross-cutting
responsibilities. The source's nuanced treatment is essential: interactions
within one coherent scenario class can indicate appropriate cohesion rather
than a defect.

### 5.2 What SAAM does not establish

The examined sources do not establish that:

- every behavior-changing customization requires a formal SAAM analysis;
- every indirect scenario is architecturally significant;
- every direct scenario is risk-free or preserves existing contracts;
- scenario interaction is always harmful;
- modifiability analysis covers security, reliability, transaction behavior,
  observability, extensibility, or upgrade compatibility;
- a component-change count is a universal measure of change cost; or
- SAAM defines a mechanism-independent review trigger for customization work.

SAAM consequently offers a strong method for contextual change-impact
analysis, but not a complete review of all architectural consequences carried
by changed behavior.

## 6. Relationship to ATAM

SEI historical material identifies SAAM as the precursor that introduced
quality-attribute scenarios and led to ATAM [S3]. The methods overlap but
should not be collapsed.

SAAM's distinctive contribution to Orden is its explicit focus on direct and
indirect scenarios, anticipated modifications, affected architectural
elements, and scenario interaction. ATAM broadens architecture evaluation to
business drivers, multiple quality attributes, risks, sensitivity points, and
tradeoff points. The detailed ATAM analysis is maintained separately in
`References/ATAM.md`.

This comparison suggests a possible sequence, not a source-defined combined
method: SAAM-style scenario impact mapping may identify where a change reaches
the architecture, while ATAM-style reasoning may examine risks and interactions
among affected quality attributes. That integration remains a repository
hypothesis.

## 7. Relevance to the Main Research Question

SAAM is negative evidence against claiming that scenario-based architectural
review of anticipated change is novel. It already connects concrete change
scenarios to affected architectural elements and organizationally relevant
quality concerns.

The remaining candidate contribution for Orden is narrower: determine when a
behavior-changing customization warrants architecture-level analysis, preserve
relevant current behavior and constraints while formulating scenarios, include
Business Central-specific concerns, and scale the analysis to extension work.
SAAM does not supply those decisions by itself.

## 8. Candidate Implications for the Framework

The following are non-normative candidates for later synthesis:

1. Describe the relevant current architecture and behavior before evaluating a
   proposed customization.
2. Formulate scenarios from the perspectives of customers, users,
   administrators, maintainers, platform owners, extension developers, and
   other affected parties as applicable.
3. Determine whether each scenario is already supported and, when it is not,
   map the required changes to components, connections, responsibilities, and
   relevant architectural views.
4. Record the impact and estimated difficulty of each required change without
   treating a simple element count as a universal cost metric.
5. Examine interactions among scenarios, while distinguishing cohesive
   scenario classes from unrelated concerns concentrated in the same element.
6. Let scenarios refine the necessary level of architectural description.
7. Treat incomplete scenario coverage and non-architectural implementation
   support as explicit limitations.

These candidates adapt SAAM concepts but do not define framework rules.

## 9. Limitations and Threats to Validity

- **Source age:** The principal sources are from 1994 and 1996. They document
  the origin and evolution of SAAM but do not demonstrate current adoption.
- **Method evolution:** The original and evolved five-step formulations differ.
  Later summaries sometimes present other step counts; this analysis relies on
  the complete primary publications rather than harmonizing them artificially.
- **Case-study scope:** The 1994 demonstration concerns user-interface
  architectures and modifiability. The 1996 paper reports broader applications
  but does not provide controlled validation for every quality attribute.
- **Scenario selection:** Results depend on stakeholder participation, scenario
  completeness, classification, weighting, and the chosen architectural
  granularity.
- **Architectural boundary:** Some scenario consequences arise at code,
  hardware, language, tool, or operational levels and cannot be inferred from
  architecture alone.
- **Transferability:** No Business Central case has yet been evaluated using the
  candidate mapping in this document.
- **Coverage:** SAAM's modification focus does not independently establish
  adequate treatment of contracts, transactions, security, extensibility,
  observability, or upgrade compatibility.

## 10. Unresolved Questions and Future Research

1. Can direct and indirect scenarios be applied consistently when Business
   Central provides several extension mechanisms for the same desired behavior?
2. How should existing behavior, suppressed behavior, and replacement behavior
   be represented without treating a scenario as a complete behavioral
   specification?
3. Which architectural views are necessary to map a Business Central scenario
   beyond components and event connections?
4. Can scenario interaction reveal extension-composition risks, or does that
   require a separate model of runtime participation and contracts?
5. How should the review distinguish architectural support from support
   supplied by AL language features, platform tooling, or operational controls?
6. What stopping criteria and stakeholder set are proportionate for a
   lightweight customization review?
7. Does empirical application to existing Business Central cases produce
   stable scenario classes and repeatable impact judgments?

## 11. References

- **[S1]** Kazman, Rick, Len Bass, Gregory Abowd, and Mike Webb. "SAAM: A
  Method for Analyzing the Properties of Software Architectures." In
  *Proceedings of the 16th International Conference on Software Engineering*,
  81-90. IEEE Computer Society Press, 1994.
  <https://doi.org/10.1109/ICSE.1994.296768>. Public copy:
  <https://www.sei.cmu.edu/documents/150/2007_019_001_29297.pdf>.
- **[S2]** Abowd, Gregory, Len Bass, Paul Clements, and Rick Kazman.
  "Scenario-Based Analysis of Software Architecture." *IEEE Software* 13,
  no. 6 (1996): 47-55.
  <https://www.sei.cmu.edu/documents/213/1996_019_001_29912.pdf>.
- **[S3]** Software Engineering Institute. "Evaluating System Architecture."
  Carnegie Mellon University.
  <https://www.sei.cmu.edu/history-of-innovation/evaluating-system-architecture/>.
- **[S4]** Kazman, Rick. "Tool Support for Architecture Analysis and Design."
  In *Proceedings of the Second International Software Architecture Workshop*,
  94-97. ACM, 1996.
  <https://www.sei.cmu.edu/documents/222/1996_019_001_29993.pdf>.

## 12. Revision History

### 0.3.0 — 2026-07-18

- Replaced the research stub with a substantive reference analysis.
- Verified the original and evolved SAAM activities, scenario types, scenario
  interaction, evaluation outputs, and method limitations against primary
  publications.
- Distinguished source claims, repository observations, interpretation,
  candidate implications, limitations, and unresolved questions.

### 0.2.0

- Established the governed research-stub structure and permanent document ID.
