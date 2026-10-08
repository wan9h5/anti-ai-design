# Anti-AI Design

An open-source agent skill for creating and reviewing purposeful product interfaces.

[简体中文](README.zh-CN.md) · [Skill entry point](SKILL.md) · [Evidence](references/evidence.md) · [Evaluation cases](tests/scenarios.json) · [Initial results](tests/evaluation-report.md)

The skill supports **create**, **review**, and **refactor** workflows. It addresses product reasoning, information architecture, density, layout, visual sameness, microcopy, interaction, data visualization, accessibility, performance, and capability integrity.

“Anti-AI” names a concern about ungrounded defaults. The skill does not detect AI authorship, blacklist colors/components, promise universal usability, or produce an aesthetic score. Familiar controls, dense expert tables, expressive brands, and sparse forms can all be appropriate.

## Install

This repository's root is the skill folder. Copy or clone the full repository as `anti-ai-design` into the skills directory supported by your agent. For Codex, use `$CODEX_HOME/skills/anti-ai-design` or `~/.codex/skills/anti-ai-design` when CODEX_HOME is unset. Preserve the relative `references/` and `workflows/` paths. Do not copy only SKILL.md.

Core use requires no Python, network connection, GitHub connection, or particular frontend framework. Python 3.10+ is needed only for repository maintenance checks. Source browsing is useful when the task needs current guidance.

## Try it

- “Use $anti-ai-design to build a responsive incident triage console for on-call engineers. Include a working local prototype with clearly marked synthetic data.”
- “Use $anti-ai-design to review this screenshot. Separate visible facts from behavior hypotheses, preserve useful domain conventions, and prioritize concrete changes.”
- “Use $anti-ai-design to refactor this reconciliation table. Preserve comparison efficiency and verify the changed task.”

The agent should deliver the requested artifact/changes, not stop at discussion. It should ask only consequential missing questions and label assumptions.

## Structure

```text
SKILL.md                  Compact entry point and selective routing
agents/openai.yaml        Codex UI metadata
references/               52 diagnostics, evidence and output contracts
workflows/                Create, review/refactor and verification
examples/                 Synthetic worked cases and counterexamples
tests/                    Rubric, regression tests and synthetic evaluated artifacts
scripts/validate.py       Offline package/evidence/reference/publication checks
LICENSE                   MIT for original repository content
```

## Maintain and evaluate

From the repository root:

```sh
python scripts/validate.py .
python -m unittest discover -s tests -p "test_*.py"
```

The validator checks packaging, internal references, source IDs, pattern completeness, suspicious secret-like content, and forbidden private artifacts. It is not a usability, accessibility, or comprehensive security audit. See [testing](tests/README.md) for behavioral evaluation and [contributing](CONTRIBUTING.md) for evidence changes.


Initial publication: package/regression checks passed locally. Automatic GitHub CI is not enabled because the current publishing credentials cannot write workflow files. The offline ZIP includes the workflow definition; the public branch excludes it.

## Research status and limits

The initial release is a structured synthesis of primary design standards, original design-system guidance, and author-published usability/AI-interaction research, reviewed on 2026-10-08. Sources differ in strength and scope; [the register](references/evidence.md) states what each supports.

There is no evaluated benchmark establishing the prevalence of these patterns in AI-generated UI, no reliable origin detector, and no measured claim that this skill improves user outcomes. Local package checks and scenario evaluation are different from representative user studies.

Public examples are synthetic. Original/private product screenshots, raw conversations, real run identifiers or datasets, and credentials are excluded from this repository.

## License

Original instructions, code, and synthetic examples are [MIT licensed](LICENSE). Linked guidelines remain owned by their publishers. This repository paraphrases and cites them; it does not sublicense their websites, fonts, imagery, or components.
