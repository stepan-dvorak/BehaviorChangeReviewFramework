# AGENTS

## Mission

Support research into a mechanism-independent framework for reviewing architecturally significant behavior-changing customizations.

## Before Editing

Read:

- Repository_Standards.md
- Governance_Principles.md
- Contributing_for_AI.md
- Editorial_Style_Guide.md
- Reasoning_Standard.md
- 00_Project_Charter.md
- 01_Terminology.md
- 02_Research_Methodology.md

## Rules

- Follow Repository_Standards.md and the applicable artifact profile.
- Treat Microsoft guidance as evidence, not conclusions.
- Never invent references.
- Separate structural normalization from substantive research changes.
- Preserve permanent document IDs, canonical terminology, uncertainty, and
  evidence limitations.
- Use exact root-relative paths and update Repository_Index.yaml when its
  maintenance triggers apply.
- Treat research stubs as planned work without conclusions.
- Exclude Archive/ from ordinary retrieval unless provenance or historical
  comparison is required.
- When drafting or replacing a document, produce the complete artifact rather
  than a delta document.
- Preserve canonical terminology.
- Mark repository concepts as Candidate until validated.
- Do not describe an executable delivery artifact as verified unless the exact delivered bytes have passed the applicable execution gate against the intended repository baseline.
- Reject a Git patch after its first structural application failure and regenerate it from authoritative source files and an actual repository diff; do not repair failed hunks speculatively.
- Treat a tool, container, process, or network failure as local to that execution path until materially different available access paths have been evaluated.
- Generate repository patches from an actual Git working-tree or staged
  difference; do not construct or repair patch hunks manually.
- Verify the exact delivered patch with `git apply --check` against the intended
  clean baseline before describing it as verified or ready.
- Include a concise Delivery Evidence declaration with executable repository
  artifacts.
- Do not use checked-out text-file hashes as a default patch gate; prefer Git
  baseline identity and Git application validation to avoid cross-platform line
  ending failures.
- Treat `.gitattributes` as the authoritative repository line-ending policy;
  do not perform independent EOL conversion in delivery tooling.
- Validate canonical Git-index line endings with
  `python Scripts/Validate_Line_Endings.py --root .`.
- Verify Git patch applicability against the canonical index with
  `git apply --cached --check <patch>` before relying on worktree application.
- Treat advanced generators, fingerprints, and three-way recovery as fallback
  mechanisms, not the default patch-delivery workflow.

