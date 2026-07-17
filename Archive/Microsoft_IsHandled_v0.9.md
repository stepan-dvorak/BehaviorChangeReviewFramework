# Microsoft_IsHandled.md

Version: 0.9

This iteration introduces an explicit evidence model separating normative (Microsoft Learn), architectural (ISO 42010/42020/42030), and empirical evidence.

## Scope
This document intentionally uses representative empirical examples rather than becoming a catalogue of IsHandled occurrences. Detailed empirical studies should remain in separate documents tied to specific BC releases.

## Evidence Model
1. Microsoft Learn (normative)
2. ISO standards (architectural)
3. Representative empirical observations from BC280 Czech localization packs.

## Representative Empirical Validation
The analyzed Czech localization applications exhibit recurring architectural concerns matching Microsoft's guidance:
- Responsibility transfer through full overrides.
- Composition problems caused by competing subscribers.
- Architectural discoverability issues due to distributed behavior.
- Extensibility degradation (dead-end events).
- Candidate observation: Discovery misuse.

These observations are treated as representative validation, not statistical proof.

## Architectural Interpretation
The empirical evidence supports Microsoft's architectural concerns rather than extending them. The proposed Behavior Change Review Framework should therefore remain mechanism-independent and use IsHandled only as one case study.

## Research Limitation
Only two localization applications have been analyzed. Broader empirical studies belong in separate versioned documents so the framework remains stable while evidence evolves.

## Findings
Accepted:
- Empirical evidence supports Microsoft's principal concerns.
- Framework and empirical studies should remain separate.

Candidate:
- Effective Extensibility.
- Discovery Misuse.

Open:
- Validation across additional Microsoft applications.
- Validation across ISV extensions.
