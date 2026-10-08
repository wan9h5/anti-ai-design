# Testing this skill

## Offline checks

`python scripts/validate.py .` validates package/frontmatter, internal links/anchors, source/pattern integrity, and obvious publication hazards. `python -m unittest discover -s tests -p "test_*.py"` checks that real corruptions are detected and valid exceptions in the package model remain accepted.

The scanner is a narrow pre-publication aid. It does not establish absence of all sensitive information, nor does it test external URL availability, UI accessibility, or UX outcomes.

## Behavioral evaluation

Use [scenarios.json](scenarios.json) as tasks for an agent with this skill loaded. Give the evaluator the prompt/context and minimum synthetic input needed; do not supply the expected answer. Score against the scenario's observable “must” and “must_not” behaviors after execution, using pass/partial/fail with reasons rather than an invented quality percentage.

For creation prompts, inspect the generated artifact or implementation; an elegant plan alone is partial/fail when an implementation was requested. For screenshot-only prompts, test whether uncertainty is preserved. Include the counterexamples so evaluation catches mechanical stylistic prohibitions.

Record skill revision, model/tool environment when known, inputs, produced artifacts, evaluator, outcomes, failures, and limitations. An independent evaluation gives additional confidence when available and authorized; do not treat a single model run as a cross-model benchmark.

## Recorded initial evaluation

See [evaluation-report.md](evaluation-report.md) for actual tasks, generated synthetic HTML artifacts, named browser checks, failure history, instruction clarifications, and untested boundaries. The 12 scenarios are a reusable rubric; the initial evaluation did not run all 12. The provided workflow runs offline package/regression checks, not the browser scenarios. It is included in the offline package but excluded from the initial public branch because the current publishing credentials lack workflow write access; automatic CI is not enabled.

## Representative product validation

For a real product, test the actual task with realistic content and relevant users, including disabled participants where applicable. Measure task completion, errors, recovery, and comprehension. A package pass and synthetic scenario review cannot substantiate a usability-improvement or conformance claim.
