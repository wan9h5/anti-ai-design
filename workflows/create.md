# Create a new interface

Use this when generating a screen or feature, or replacing a diagnosed part of an existing interface. Scale the effort to scope: do not force a long workshop for a small UI request.

## Frame a decision brief

Capture the primary user/task, starting conditions, object, desired outcome, constraints, data availability, and important failure consequence. Keep facts, assumptions, and unanswered questions distinct. A decision brief can be one paragraph.

If the missing answer changes permissions, destructive behavior, business correctness, or capability claims, resolve it before implementing that part. For reversible layout and styling choices, make a reasonable assumption and continue. A user-supplied screenshot is useful design evidence, not a specification for unobservable behavior.

## Shape information and content

Model the objects, relations, task order, and information needed to make decisions. Prioritize by task relevance, frequency, urgency, and consequence rather than equal component counts. Show navigation labels in domain language. Include a clear way to reach uncommon but necessary capabilities.

Choose a composition suited to the job:
- **Compare/triage**: consistent rows, aligned attributes, filters, ownership/status, and drilldown.
- **Complete a task**: a focused form or sequence with clear dependencies and review/recovery.
- **Monitor**: an overview whose signals support a decision and whose freshness is visible.
- **Explore**: flexible views with controls and a useful initial state.
- **Understand a result**: conclusion, supporting evidence, uncertainty, then provenance/detail.

Explain a consequential choice briefly. For a complex, uncertain composition, compare two plausible structures at wireframe/content level before polishing one. Do not generate cosmetic alternatives when the task structure is settled.

Load [product and IA](../references/product-ia.md) or [layout and density](../references/layout-density.md) when those decisions need deeper guidance.

## Set a capability and state model

For important controls, establish:
- input and validation;
- action and side effect;
- loading/progress, success, failure, empty/no-result, permission/unavailable states as relevant;
- what is saved and when;
- cancellation, retry, undo, or review where warranted;
- connection between changed inputs and displayed results.

A result must belong to a known input/plan version. Mark an old result as stale after relevant changes. Planned, running, successful, failed, and skipped steps must have distinct semantics.

If implementation is a prototype, make its scope legible near the action/result. Choose a labeled simulation, an explained unavailable action, or a smaller real capability. Do not make a success toast stand in for execution.

## Establish the visual system

Use the existing platform/component system when suitable. Define a small coherent set of semantic color, type, spacing, border, surface, and motion choices. Choose density with realistic content and supported input methods.

Make a compact visual direction concrete: intended tone, typographic hierarchy, spatial rhythm, semantic emphasis, and one or two content-led choices that give the screen character. Treat these as design proposals, not user-research findings. If no brand brief exists, infer a reversible direction from the task and state it briefly; do not require the user to become a designer before proceeding. Avoid repeating an unrelated project's composition by habit, and avoid novelty that harms recognition or maintainability.

Check the direction with realistic labels, long values, empty/error states, and the main work area. For an existing product, preserve its coherent language unless a change is requested or a concrete problem warrants it.

Before adding ornament, check reading order, grouping, action hierarchy, and the balance of work area and supporting detail. Brand expression can be restrained or expressive; justify it through the user's brief and product. Familiar typefaces or common components are not failures.

For content/brand issues, load [visual design and copy](../references/visual-copy.md). For interactive behavior, load [interaction](../references/interaction.md). For charts, load [data visualization](../references/data-viz.md).

## Make and check the artifact

When implementation is requested, use the actual repository conventions and available tools. Deliver working local behavior or explicitly labeled boundaries. Use authorized real data or coherent synthetic data, clearly marked.

Run checks proportionate to the change using [verification](verify.md). Do not install dependencies, publish, or send user data solely because this workflow mentions them; follow the actual task authorization and environment permissions.

Finish with the artifact, the key rationale, consequential assumptions, actual verification, and unresolved product decisions. Do not claim that a stylistic change improved task completion until measured.
