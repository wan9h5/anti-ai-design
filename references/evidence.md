# Evidence register

## How to read the catalog

- **Standard**: a normative requirement within its stated scope, with criterion/level. WAI Understanding pages explain requirements; the WCAG Recommendation is the normative source.
- **Guidance**: a direct design-system/platform recommendation or original-author usability heuristic. Context and exceptions matter.
- **Synthesis**: our inference applying one or more sources to a product situation. The source supports the principle, not necessarily the exact proposed change.
- **Hypothesis**: a concern about visual sameness or user behavior without direct causal/prevalence evidence. Validate it.

Source strength and finding confidence are independent. A strong standard does not establish that a screenshot fails it. A user study about one domain does not prove a rule for every domain.

## Research method and limits

This is a targeted, source-traceable review across the requested design dimensions, not a systematic review with exhaustive search/inclusion screening. We preferred normative standards, publisher-owned design systems, original usability guidance, and author-published research. Pages/excerpts were inspected on 2026-10-08; evolving metrics and living guidance should be rechecked for future work.

Searches support a practical catalog, not a prevalence estimate for AI-generated UI. We have not established that any color, font, component, or layout reliably identifies AI authorship. Visual sameness is context-dependent and needs product/audience evidence.

We have no representative-user or cross-model benchmark showing this skill improves usability. Repository checks test packaging and evidence integrity. Synthetic scenario evaluation checks reasoning behavior. Neither establishes real product outcomes, WCAG conformance, or biological/clinical validity.

Apple HIG content was only accessible as an index; Material 3 typography was accessible as an indexed excerpt. These limited sources are recorded for follow-up and cannot support uninspected detailed rules. Dense-table guidance uses the readable Carbon source instead of importing a legacy Material density rule.

External materials are cited and paraphrased, not copied as reusable licensed assets. Catalog examples are original and synthetic.

## Sources

The machine-readable register is [sources.json](sources.json). “Verified” means the referenced page/content was readable for the listed claim, not that every linked fact was independently validated.

### S01

[W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/)

- Type: standard; access: verified; checked: 2026-10-08.
- Supports: Normative web accessibility success criteria and conformance framework.
- Limit: A scoped check is not a complete conformance evaluation; does not prescribe a visual style.

### S02

[GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Research user goals and treat stakeholder-only opinions as assumptions.
- Limit: Written for government services; does not establish this product's user needs.

### S03

[GOV.UK Service Manual: Services for government users](https://www.gov.uk/service-manual/design/services-for-government-users)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Expert internal work can require rapid switching and information together.
- Limit: Domain example supports an exception; does not justify any dense screen.

### S04

[Nielsen Norman Group: 10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/)

- Type: heuristic; access: verified; checked: 2026-10-08.
- Supports: General inspection principles including consistency, status, recovery, and user language.
- Limit: Rules of thumb, not a validated score or product-specific defect proof.

### S05

[Nielsen Norman Group: Cards: UI-Component Definition](https://www.nngroup.com/articles/cards-component/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Cards suit summaries/heterogeneous browsing; consistent lists can aid search and comparison.
- Limit: 2016 guidance; neither bans cards nor proves all tables better.

### S06

[Nielsen Norman Group: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Defer uncommon detail; staged sequences can fail for interdependent steps.
- Limit: 2006 guidance; the split needs task evidence, not a universal feature limit.

### S07

[Nielsen Norman Group: Aesthetic and Minimalist Design](https://www.nngroup.com/articles/aesthetic-minimalist-design/)

- Type: heuristic; access: verified; checked: 2026-10-08.
- Supports: Retain necessary task information and reduce irrelevant competition.
- Limit: Minimalism as a heuristic is not a requirement for sparse visual styling.

### S08

[Nielsen Norman Group: Information Scent: How Users Decide Where to Go Next](https://www.nngroup.com/articles/information-scent/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Labels, context, and prior experience help people choose routes.
- Limit: Does not supply the right vocabulary for an unknown audience.

### S09

[GOV.UK Service Manual: Writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Use user language, purposeful labels, and understandable questions.
- Limit: Specific government-service conventions are not universal interface rules.

### S10

[GOV.UK Design System: Error message](https://design-system.service.gov.uk/components/error-message/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Associate validation with fields and preserve entered information.
- Limit: Service/eligibility failures need different recovery communication.

### S11

[GOV.UK Design System: Button](https://design-system.service.gov.uk/components/button/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Action hierarchy and caution around unexplained disabled buttons.
- Limit: A design-system recommendation, not a prohibition for every product.

### S12

[IBM Carbon Design System: Data table guidelines](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Tables have deliberate density variants and need sufficient usable space.
- Limit: Carbon row dimensions are system-specific tokens, not WCAG guarantees.

### S13

[GOV.UK Brand Guidelines: Charts](https://brand.design-system.service.gov.uk/data/charts/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Chart purpose, labels, units, sources, and justified interactivity.
- Limit: Editorial conventions need adapting for analytical/exploratory tools.

### S14

[GOV.UK Brand Guidelines: Dashboards](https://brand.design-system.service.gov.uk/data/dashboards/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Dashboards suit recurring high-level monitoring with maintainable data.
- Limit: An overview can be unsuitable for explanation or detailed insight.

### S15

[U.S. Web Design System: Data visualizations](https://designsystem.digital.gov/components/data-visualizations/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Readable familiar charts, equivalent data access, and clear intent.
- Limit: Guidance-only examples are not guaranteed production components.

### S16

[UK Government Analysis Function: Data visualisation: charts](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Bar baseline, line-axis exceptions, discontinuities, and dual-axis risks.
- Limit: Expert analytical needs can differ; explain transformations and alternatives.

### S17

[Google web.dev: Web Vitals](https://web.dev/articles/vitals)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Field metrics for loading, responsiveness, stability, and p75 thresholds.
- Limit: Metrics evolve and do not measure every task or backend wait.

### S18

[Google web.dev: User-centric performance metrics](https://web.dev/articles/user-centric-performance-metrics)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Performance varies by user/device; lab and field evidence differ.
- Limit: A still image and load event cannot establish user performance.

### S19

[Google web.dev: prefers-reduced-motion](https://web.dev/articles/prefers-reduced-motion)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Honor motion preferences through alternative animation treatments.
- Limit: Reduced motion is broader than globally setting all durations to zero.

### S20

[W3C WAI: ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)

- Type: guidance; access: verified; checked: 2026-10-08.
- Supports: Accessible names, roles/states, keyboard patterns, and landmarks.
- Limit: Informative guidance; examples need browser/assistive-technology validation.

### S21

[W3C WAI: Understanding 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Text contrast thresholds, large-text definition, and exceptions.
- Limit: Understanding is informative; apply the normative criterion in S01.

### S22

[W3C WAI: Understanding 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Contrast for required component and graphical information.
- Limit: Not every border, decorative shape, or chart color requires this ratio.

### S23

[W3C WAI: Understanding 1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Narrow-view reflow and scoped essential two-dimensional exceptions.
- Limit: A table exception does not exempt surrounding headings or prose.

### S24

[W3C WAI: Understanding 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: 24 CSS px AA minimum plus spacing/equivalent/inline/UA/essential exceptions.
- Limit: 44 CSS px is enhanced AAA, not the universal AA threshold.

### S25

[W3C WAI: Understanding 2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: AA prevents author content entirely hiding a focused component.
- Limit: Full visibility is a stronger target; distinguish focus-indicator criteria.

### S26

[W3C WAI: Understanding 2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Keyboard operation with exception for path-dependent functionality.
- Limit: Exception concerns the function, not a preference for pointer input.

### S27

[W3C WAI: Understanding 2.5.7 Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Single-pointer non-drag alternative unless essential or unmodified UA.
- Limit: Keyboard access alone does not satisfy this pointer requirement.

### S28

[W3C WAI: Understanding 3.1.2 Language of Parts](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Programmatic language of passages/phrases with named exceptions.
- Limit: Technical terms/proper names may be excepted; mixed language is not inherently failure.

### S29

[W3C WAI: Understanding 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Defined status updates should be programmatically available without taking focus.
- Limit: Does not require every dynamic content change to be a live region.

### S30

[W3C WAI: Understanding 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Meaning should not depend on color alone.
- Limit: Does not ban color as an additional visual cue.

### S31

[W3C WAI: Understanding 1.4.4 Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: 200% text resizing without content/function loss, with exceptions.
- Limit: Do not treat a universal minimum font size as a WCAG rule.

### S32

[W3C WAI: Understanding 2.4.13 Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

- Type: explanation; access: verified; checked: 2026-10-08.
- Supports: Enhanced AAA focus indicator area and change-of-contrast requirements.
- Limit: Separate this AAA criterion from AA focus visibility/obscuration checks.

### S33

[Microsoft Research / Amershi et al.: Guidelines for Human-AI Interaction, CHI 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)

- Type: research; access: verified; checked: 2026-10-08.
- Supports: Guideline development/evaluation for capability, fallibility, correction, and control in AI interaction.
- Limit: Guideline validation does not prove this skill or detect AI-generated interfaces.

### S34

[Google Material Design: Material 3: Applying typography](https://m3.material.io/styles/typography/applying-type)

- Type: guidance; access: partial; checked: 2026-10-08.
- Supports: Indexed official excerpt supports platform/density/resizing-aware type decisions.
- Limit: Full page extraction unavailable; do not attribute uninspected details or exact token values.

### S35

[Apple Developer: Human Interface Guidelines: Foundations](https://developer.apple.com/design/human-interface-guidelines/foundations)

- Type: guidance; access: limited; checked: 2026-10-08.
- Supports: Official index establishes relevant foundations/platform topics.
- Limit: Only the index was readable; not substantive evidence for specific Apple layout rules.


## Open empirical questions

- How frequently do these patterns occur across generators, prompts, frameworks, and domains?
- Does task-first prompting reduce observed failures compared with a visual-template baseline?
- What expert/novice density tradeoffs arise for a particular product?
- Which capability disclosures actually change user interpretation at the action/result point?
- What does a distinctive brand treatment improve, and for which audience?

A useful study would compare matched tasks/content/capabilities with and without the skill, randomize order where feasible, include disabled participants and relevant expert/novice groups, and measure completion, errors, recovery, and comprehension. Record generator/model, prompts, artifacts, counterexamples, and limitations. Do not publish private participant/product evidence without appropriate authorization.
