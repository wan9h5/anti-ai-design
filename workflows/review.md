# Review and refactor

Use this for screenshots, source, prototypes, or live interfaces. Match scope to the user request. A screenshot review is valuable even when behavior is unavailable, provided its limits are explicit.

## Establish what the evidence can show

Identify the user/task if known, the supplied surface, and requested depth. Classify available evidence: static screenshot, design spec, source inspection, executable prototype, or live product. Record important missing context without making the review depend on unnecessary questions.

If evidence is only a written screenshot description, review the described claims and relationships. Do not imply that actual colors, spacing, text size, or the image itself were inspected.

Describe the existing design's useful choices as well as problems. Preserve honest demo/fallback labels, task-aligned structure, useful data, accessible conventions, and domain vocabulary.

## Trace the primary task

Follow the expected sequence from arrival to outcome and recovery. Inspect:
- what users need to recognize, compare, enter, approve, or retrieve;
- where each action/decision gets its supporting information;
- whether changes, status, data recency, errors, and outputs remain coherent;
- which claims are visually prominent and which limitations are easy to miss.

A workflow illustration does not prove a functioning workflow. A green indicator does not prove successful execution. A static download tile does not prove the file exists.

## Select and test candidate patterns

Use [the subject index](../references/index.md), then load only the relevant files. For every candidate:
1. Describe the concrete evidence and affected task.
2. Identify the basis: normative standard, guidance, synthesis, or hypothesis.
3. Check the exception: does this product legitimately need the pattern?
4. Propose a fix and a discriminating validation.

For example, “three columns” is not a finding. “The result needed for reviewing a changed plan is clipped at the supported viewport” is testable. “Text appears small in this screenshot; confirm computed size, zoom resilience, and readability” is a provisional concern.

Use the finding shape in [output contracts](../references/output-contracts.md) for substantial audits. Do not invent CSS pixel values, contrast ratios, usage frequencies, severity scores, or test outcomes from a screenshot.

For a performance question, load [performance and capability integrity](../references/performance-integrity.md) before answering, even for a short screenshot review. Separate controlled lab diagnostics from field measurements on users' devices. Separate input-to-feedback/paint responsiveness from completion of a network or analysis job. State which evidence is available for each; do not infer either timing or a causal bottleneck from appearance. Recommend a controlled comparison tied to the user's slow operation.

## Prioritize and refactor

Qualitative priority depends on harm, exposure, recovery, and confidence. Fix reproduced task failures, misleading capabilities/results, and inaccessible critical paths before visual polish. Keep uncertain hypotheses visibly provisional.

Refactoring should address the diagnosed task: reorder/group information, strengthen labels and state semantics, align comparison data, revise copy, or adjust responsive layout and density. Avoid deleting functionality or replacing every table with cards to satisfy a visual ideal.

If the user asks for implementation, make concrete changes and check them. Use [create](create.md) for the revised portion and [verify](verify.md) for actual validation. Check content and behavior after the visual change, including result freshness and preserved capability disclosures.

## Deliver

Present the most consequential findings first, with evidence, impact, exception considered, fix, and validation. Keep taste preferences separate from task/standards issues. Include positive choices worth preserving and untested behavior. A short review may need only a few paragraphs; do not manufacture findings to fill a quota.
