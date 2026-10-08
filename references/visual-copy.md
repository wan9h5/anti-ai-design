# Visual design and microcopy

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP017: Decoration dominates the decision

- **Signal:** Glow, gradients, glass, textures, or illustrations compete with task content.
- **Risk:** The salient visual cue may be unrelated to user work.
- **Repair:** Align emphasis with decisions; keep useful expression and measure contrast/performance where relevant.
- **Exception:** An expressive marketing/editorial brief can legitimately prioritize visual experience.
- **Check:** Ask what draws attention first and whether it helps the task.
- **Basis:** Hypothesis; [S07](evidence.md#s07).

## AP018: Familiar styling substitutes for brand reasoning

- **Signal:** Unrelated product briefs receive the same decorative composition without a task/brand rationale, or a review labels a color/font inherently AI-generated.
- **Risk:** Domain priorities and intended brand expression may be lost; taste can become a false evidence claim.
- **Repair:** Use authorized brand traits, domain content, task hierarchy, and audience expectations to explain visual choices. Compare brief-led directions when those choices are unsettled; do not invent brand research.
- **Exception:** A shared design system and familiar controls can serve many products well. An explicit user preference to avoid a style is a valid constraint.
- **Check:** Trace prominent choices to the brief; test recognition/comprehension where consequential. Do not infer authorship from appearance.
- **Basis:** Hypothesis; [S07](evidence.md#s07). The source supports task-relevant emphasis, not a causal claim about brand distinctiveness or AI prevalence.

## AP019: Styling changes with no semantic reason

- **Signal:** Repeated states/actions use unrelated color, shape, or type treatments.
- **Risk:** Users may infer distinctions that do not exist.
- **Repair:** Define shared semantic tokens and intentional exceptions.
- **Exception:** Different content types or brand subcontexts can need distinct treatment.
- **Check:** Map each visual difference to a documented meaning or purpose.
- **Basis:** Synthesis; [S04](evidence.md#s04).

## AP020: Hierarchy depends on tiny, faint secondary text

- **Signal:** Essential limits and labels receive decorative microtype treatment.
- **Risk:** Decision-changing information can be overlooked or hard to read.
- **Repair:** Retain hierarchy through placement/weight/spacing while checking actual contrast and enlargement.
- **Exception:** Truly decorative/inactive text has different normative treatment.
- **Check:** Measure colors and inspect enlarged text; test comprehension.
- **Basis:** Synthesis; [S21](evidence.md#s21).

## AP021: Vague microcopy replaces an action

- **Signal:** Labels promise to unlock, optimize, or transform without naming the effect.
- **Risk:** Users cannot predict what clicking does.
- **Repair:** Use a concrete verb/object and meaningful consequence where needed.
- **Exception:** Expressive headlines can sit alongside concrete operational labels.
- **Check:** Ask a user to predict the action outcome from the label.
- **Basis:** Synthesis; [S09](evidence.md#s09).

## AP022: Placeholders or icons carry all meaning

- **Signal:** Field identity disappears on input, or an icon's action is ambiguous.
- **Risk:** Entry and navigation require memory or guessing.
- **Repair:** Provide persistent labels and accessible names; explain unfamiliar icons.
- **Exception:** Well-understood icon-only controls can fit constrained space with discoverability.
- **Check:** Inspect accessible names and test recognition with target users.
- **Basis:** Synthesis; [S20](evidence.md#s20).

## AP023: Bilingual copy switches without purpose

- **Signal:** One workflow alternates language for headings, actions, warnings, and explanation.
- **Risk:** Comprehension may require unnecessary translation.
- **Repair:** Choose a primary UI language, preserve useful domain terms, and mark real language changes in markup.
- **Exception:** Technical terms/proper names can be appropriate and have WCAG language exceptions.
- **Check:** Check terminology comprehension and language semantics; do not treat mixing alone as failure.
- **Basis:** Synthesis; [S28](evidence.md#s28).

## AP024: Error prose blames instead of supporting recovery

- **Signal:** A message says 'invalid' or blames users without the remedy.
- **Risk:** Users repeat failed attempts or lose confidence.
- **Repair:** Identify the affected input and actionable correction in familiar language.
- **Exception:** Security/privacy can justify withholding sensitive failure details while giving a safe next step.
- **Check:** Can a user correct the error without guessing?
- **Basis:** Synthesis; [S10](evidence.md#s10).
