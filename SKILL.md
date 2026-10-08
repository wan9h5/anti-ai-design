---
name: anti-ai-design
description: Generate product UI from a brief, or review and refactor an existing screen or flow for task fit, information architecture, usable density, interaction quality, and truthful capabilities. Use for requests to remove generic AI UI patterns or make an interface more purposeful. Does not detect AI authorship.
---

# Anti-AI Design

Turn a product brief or existing interface into a concrete, task-fit design. “Anti-AI” is a diagnostic lens for ungrounded defaults, not a style classifier. Purple, gradients, rounded cards, dark themes, whitespace, serif type, and familiar components are not defects by themselves.

## Choose the mode and load selectively

- **Create** a screen or feature: read [workflows/create.md](workflows/create.md).
- **Review** screenshots, prototypes, live UI, or code: read [workflows/review.md](workflows/review.md).
- **Refactor**: use the review workflow to establish the problem, then the create workflow for the affected task. Preserve useful domain conventions and working capabilities.
- Read [workflows/verify.md](workflows/verify.md) for checks appropriate to the actual change and available tools.
- Select relevant subject files from [references/index.md](references/index.md). Do not load the whole catalog for a narrow request.
- Use [references/evidence.md](references/evidence.md) when citing a design rule, explaining an exception, or making a standards claim. Use [references/output-contracts.md](references/output-contracts.md) for an audit or handoff.

## Establish the task before composing the screen

Identify who is acting, the trigger, the decision or outcome, the object being worked on, the cost of error, the available data, and device/input constraints. Use supplied research and product rules. Ask only consequential missing questions; for reversible choices, proceed with explicit assumptions.

Choose structure from the task: comparison, triage, editing, monitoring, exploration, explanation, or sequential submission. Every prominent section should support an identifiable decision or action. A dashboard is a candidate only when monitoring is a real need. Do not invent research, user segments, product rules, or a backend to justify a template.

Make the information architecture, content hierarchy, relevant states, and capability boundary concrete before polishing tokens. When the user asks for an interface or implementation, deliver the artifact and requested changes, not only a critique or a plan.

## Diagnose with evidence and exceptions

For each finding, connect an observation to a task consequence. Separate:
- **Observed**: visible in supplied evidence or reproduced with tools.
- **Standard**: an applicable normative criterion, named precisely.
- **Guidance**: a platform/design-system recommendation or heuristic.
- **Hypothesis**: a plausible effect requiring measurement or user research.

The catalog's evidence label describes the basis of its advice; it does not prove a defect in the current product. A screenshot supports visual observations, not claims about keyboard behavior, live data, latency, semantics, or persistence. Preserve valid counterexamples. Do not count pattern matches as an “AI score.”

Use qualitative priorities: blocker for demonstrated task failure or serious misleading behavior; major for materially impaired work; moderate for recoverable friction; minor for polish. Confidence and priority are separate. Unverified concerns stay provisional, even if their potential impact is serious.

## Build a coherent, honest interface

Fit density and layout to work: expert comparison may need compact tables; focused onboarding may need a sparse form. Provide readable content, usable targets, and adaptation to supported viewports and text enlargement. Do not remove necessary information to create a minimalist appearance.

Create distinctiveness through domain content, task hierarchy, and deliberate brand choices. Use existing design systems when they fit. Change only the parts whose user value can be explained.

For controls and claims, specify input, effect, relevant states, data source, persistence, and recovery. A real control must produce the promised effect; a simulation must be visibly labeled at the point of use. Show unavailable capability truthfully. Preserve explicit demo/fallback labels and useful provenance when refactoring. Do not imply AI analysis or tool execution that did not occur.

Use real content where authorized; otherwise coherent, marked synthetic examples. Do not embed private screenshots, personal identifiers, datasets, or conversation history into a reusable/public artifact.

## Finish at the appropriate depth

Use the user's language in the result. For a small edit, deliver the edit and relevant checks briefly. For substantial creation, include a short task rationale, the concrete artifact, functionality boundaries, and verification. For an audit, show prioritized findings with evidence, fixes, exceptions, and unresolved checks; implement changes when requested.

Report what was actually inspected or tested and what remains unknown. Automated checks, a polished screenshot, or using an accessible component library do not establish whole-product WCAG conformance or improved usability. Recommend a focused next validation when a consequential hypothesis remains.
