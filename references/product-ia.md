# Product reasoning and information architecture

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP001: Invented users become product requirements

- **Signal:** A brief names no audience, yet the design asserts detailed personas and preferences.
- **Risk:** Wrong assumptions harden into navigation and features.
- **Repair:** Record supplied facts; ask about consequential task differences and label reversible assumptions.
- **Exception:** A clearly labeled speculative concept can deliberately explore an audience.
- **Check:** Ask a representative user to describe their task before showing the proposal.
- **Basis:** Synthesis; [S02](evidence.md#s02).

## AP002: Dashboard chosen before a decision

- **Signal:** KPI tiles and charts appear without a monitoring question or action.
- **Risk:** An overview can delay the actual task.
- **Repair:** Name the recurring decision and relevant signal; choose a focused task surface if monitoring is incidental.
- **Exception:** Frequently revisited, automatically updated high-level monitoring can justify a dashboard.
- **Check:** Trace a real alert/change to the next user action.
- **Basis:** Guidance; [S14](evidence.md#s14).

## AP003: Feature inventory substitutes for hierarchy

- **Signal:** Every feature occupies an equally weighted section.
- **Risk:** Urgent work and supporting detail compete.
- **Repair:** Rank content by the current task and consequence; give secondary capabilities discoverable routes.
- **Exception:** A neutral catalog may appropriately avoid editorial ranking.
- **Check:** Can a user locate the task's next action without reading every section?
- **Basis:** Synthesis; [S07](evidence.md#s07).

## AP004: Navigation mirrors internal organization

- **Signal:** Labels name internal modules, departments, or abstractions unfamiliar to users.
- **Risk:** Users must translate before finding work.
- **Repair:** Use recognizable domain objects/actions and test route labels in context.
- **Exception:** Specialist users may share precise technical vocabulary.
- **Check:** Run a small tree/findability task with target users.
- **Basis:** Synthesis; [S08](evidence.md#s08).

## AP005: One role or audience silently stands for all

- **Signal:** The interface assumes the same expertise, data access, and job for everyone.
- **Risk:** Critical information may be inaccessible or irrelevant.
- **Repair:** Map materially different tasks and permissions; keep a shared model where needs overlap.
- **Exception:** A genuinely single-role tool needs no role switching.
- **Check:** Check key tasks for each supported role and access state.
- **Basis:** Synthesis; [S02](evidence.md#s02).

## AP006: Staged wizard splits interdependent work

- **Signal:** Users must navigate back and forth to compare inputs and outcomes.
- **Risk:** Repeated context switching burdens iteration.
- **Repair:** Keep closely coupled controls/evidence together; stage independent or committed steps.
- **Exception:** Low-frequency sequential submissions can benefit from guided stages.
- **Check:** Observe whether users repeatedly revisit earlier steps.
- **Basis:** Guidance; [S06](evidence.md#s06).

## AP007: Progressive disclosure hides essential evidence

- **Signal:** Decision-changing limits, totals, or dependencies sit behind obscure links.
- **Risk:** Users can act without necessary context.
- **Repair:** Expose decision-critical information; make optional detail routes explicit.
- **Exception:** Rare diagnostic logs can remain in a secondary detail view.
- **Check:** Ask what changes a user's decision and locate that information.
- **Basis:** Synthesis; [S06](evidence.md#s06).

## AP008: Workflow is a picture of work only

- **Signal:** Step cards have no inspectable inputs, consequences, or relation to current output.
- **Risk:** The process appears more explainable than it is.
- **Repair:** Show actionable plan details and meaningful state; connect output to the reviewed plan.
- **Exception:** A clearly labeled static process illustration is legitimate.
- **Check:** Follow one step from input through actual effect to evidence.
- **Basis:** Synthesis; [S33](evidence.md#s33).
