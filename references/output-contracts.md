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

## Page analysis report

For an explicitly requested report, include these sections in the user's language; the finding fields above supply the detailed evidence contract.

- **Overview**: page/task, intended audience, evidence inspected, assumptions and short conclusion. Name a description as a description rather than a inspected screenshot.
- **Keep**: useful choices and why they serve the task. Avoid gratuitous redesign.
- **Findings and modifications**: use a table or numbered findings. Include ID, location/evidence, issue/task impact, basis/confidence, priority (provisional where needed), exception, concrete modification and acceptance check. Split details into prose if a wide table becomes unreadable.
- **Modification plan**: ordered steps linked to finding IDs; dependencies and what counts as completion. Separate necessary fixes, provisional checks and optional style changes.
- **Verification and limits**: actual inspections/tests and results, unverified behavior and focused validation actions. Never describe a planned check as executed.

Keep the report complete but proportionate. No invented AI/aesthetic/UX score, authorship verdict, measured values, defect quota or test results. A report can contain no substantiated defects and still give conditional improvement options.
