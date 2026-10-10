# Page analysis report and modification recommendations

Produce a complete report when asked for an AI page analysis report, 页面分析报告, AI 页面分析报告, or structured modification recommendations. Use the user's language. Support screenshots, written descriptions, source, prototypes, and live pages; review only the evidence actually supplied or inspected. Do not infer AI authorship or an “AI percentage” from style.

## Inspect and scope

Read [review](review.md) and the [output contracts](../references/output-contracts.md). Establish the page, primary users/task, evidence type, inspected states/viewports and important assumptions. If the task is unknown, state a provisional task interpretation and keep dependent recommendations conditional. Missing behavior does not prevent a useful visual report. If no page evidence is supplied, ask for the page/screenshot/code instead of fabricating findings.

Trace the primary task and recovery path. Load relevant subjects from [the index](../references/index.md); check valid exceptions before recommending removal. For timing/slowdown concerns, load [performance integrity](../references/performance-integrity.md). Cite applicable sources when asserting a standard or guideline; do not attach normative certainty to aesthetic preferences.

## Write the report

Use the [page analysis report contract](../references/output-contracts.md#page-analysis-report). Scale detail to scope, but include the overview, strengths, findings, recommendations and verification status. If there are no substantiated issues, say so; never manufacture a minimum number of problems.

1. Lead with the page's primary task and the most consequential supported conclusion.
2. Identify choices worth preserving: task-fit density, comparison structure, brand, domain terms, data/provenance and honest capability disclosures.
3. Assign stable finding IDs such as F01. Pair each issue with its evidence/location, task consequence, evidence basis, confidence, priority, considered exception, concrete modification and acceptance check. Separate observed facts from inferred harm or untested behavior within the same finding.
4. Make recommendations implementable: specify what to move, group, label, resize or change; give replacement copy or a small before/after example where useful. “Improve hierarchy”, “reduce AI feel” or “make it cleaner” alone is insufficient. Distinguish repairs from optional visual exploration; preserve necessary information and tasks.
5. Order the modification plan by task impact, with finding IDs, dependencies and acceptance checks. Mark confirmed priorities separately from provisional investigations. Estimate effort only when source/stack evidence supports it; otherwise leave effort unknown.
6. End with checks actually performed, outcomes and focused unverified checks. A suggested acceptance check is not a passed test. Static screenshots/descriptions cannot establish keyboard behavior, hit-area geometry, persistence, performance or whole-product WCAG conformance.

Deliver Markdown in the conversation by default. Save a report file when requested or appropriate for a substantial handoff, following the host's persistence rules. Use a document/PDF skill only for an explicitly requested export format. Do not automatically modify the page, execute destructive actions, or publish private page evidence; implement recommendations only when asked. If changes are also requested, deliver the report plus implementation and distinguish proposed, implemented and verified changes.
