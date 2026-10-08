# Output contracts

Use these fields when they make a substantial audit or handoff reviewable. They are a flexible content contract, not mandatory headings or a required output length.

## Brief

- User and task; trigger and desired outcome.
- Known constraints/data; consequential assumptions.
- Primary decision and supporting information.
- Capability boundary and state coverage.

## Finding

- **Location / evidence**: observed text, component, flow, source lines, or reproduced behavior.
- **Concern and task effect**: what becomes harder, ambiguous, inaccessible, or misleading.
- **Basis**: normative criterion with level and applicability; guidance/source ID; or hypothesis.
- **Confidence**: high, medium, or low with a reason.
- **Priority**: blocker, major, moderate, minor; provisional if unverified.
- **Exception considered**: why the pattern is appropriate here, or why the exception does not apply.
- **Change**: a concrete fix preserving relevant work.
- **Validation**: an action or measurement that can confirm/refute the concern.

Observed evidence and a hypothesis may coexist in a finding. “Text appears small” is observed; “experts cannot read it efficiently” requires testing. An untested possible blocker is not a reproduced blocker.

## Change handoff

Describe the revised task/IA, relevant visual decisions, control effects, data/source/mode, state coverage, and actual checks. Record prototype/production boundaries and unresolved dependencies. For refactors, note meaningful removed/relocated information and why users can still reach it.

## Capability contract

For consequential UI claims/actions: input → actual processing/side effect → output → persistence → failure/recovery. Record whether the capability is live, simulated, unavailable, or unverified. Do not treat a cosmetic success state as evidence that processing or saving happened.
