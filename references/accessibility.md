# Accessibility and precise standards

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP039: Meaningful content or graphics fail contrast

- **Signal:** Actual colors make task text or essential component/graphic information insufficiently distinct.
- **Risk:** Low-vision users may miss essential information.
- **Repair:** Check text under 1.4.3 and required non-text information under 1.4.11, with their respective exceptions.
- **Exception:** Decorative/inactive elements and some essential/user-agent presentations are scoped exceptions.
- **Check:** Measure rendered foreground/background combinations, including state/image overlays.
- **Basis:** Standard; [S21](evidence.md#s21), [S22](evidence.md#s22).

## AP040: Critical operation lacks keyboard and clear focus

- **Signal:** Custom controls require a pointer, trap focus, or focus is hidden by overlays.
- **Risk:** Users can lose position or fail the task.
- **Repair:** Use native semantics where appropriate; check keyboard, focus visibility, and obscuration separately.
- **Exception:** Path-dependent functions have a limited keyboard exception; pointer preference is not one.
- **Check:** Complete the task by keyboard and inspect focus across overlays.
- **Basis:** Standard; [S26](evidence.md#s26), [S25](evidence.md#s25).

## AP041: Pointer targets are small and crowded

- **Signal:** Actual hit regions are undersized with neighboring targets.
- **Risk:** Accidental activation can increase.
- **Repair:** Evaluate AA 2.5.8 size or a valid exception; enlarge important controls where useful.
- **Exception:** Inline/equivalent/spacing/unmodified-UA/essential cases can be excepted.
- **Check:** Measure CSS hit regions and spacing; do not measure only icon artwork.
- **Basis:** Standard; [S24](evidence.md#s24).

## AP042: Text enlargement or reflow loses necessary work

- **Signal:** Content overlaps, disappears, or forces unnecessary two-dimensional reading.
- **Risk:** Users requiring enlarged text lose information/function.
- **Repair:** Check 200% text resizing and scoped reflow requirements; adapt surrounding controls/prose.
- **Exception:** Necessary two-dimensional tables/maps have scoped reflow exceptions, not a whole-page exemption.
- **Check:** Inspect long content at equivalent 320 CSS px width and enlarged text.
- **Basis:** Standard; [S31](evidence.md#s31), [S23](evidence.md#s23).

## AP043: Programmatic names/states/status disagree with visuals

- **Signal:** A visible label/state is absent or misleading to assistive technology.
- **Risk:** Users receive a different task or no update.
- **Repair:** Inspect names/roles/states and defined status updates; avoid announcing every change aggressively.
- **Exception:** A focused context change is treated differently from an unfocused status update.
- **Check:** Inspect semantics and execute the changed task with relevant assistive technology.
- **Basis:** Synthesis; [S20](evidence.md#s20), [S29](evidence.md#s29).

## AP044: Motion or dragging is the only route

- **Signal:** Meaning relies on animation or a drag action lacks an alternative.
- **Risk:** Some users cannot perceive or perform the operation.
- **Repair:** Honor motion preferences and provide required non-drag pointer operation; keyboard access is a separate check.
- **Exception:** Essential dragging or unmodified user-agent behavior has specific exceptions.
- **Check:** Try reduced motion and the operation with a single pointer without dragging.
- **Basis:** Synthesis; [S19](evidence.md#s19), [S27](evidence.md#s27).

## AP045: Language handling ignores real passage changes

- **Signal:** A mixed-language interface exposes passages under the wrong programmatic language.
- **Risk:** Assistive pronunciation/interpretation can suffer.
- **Repair:** Check 3.1.2 language-of-parts semantics and page language; preserve useful technical terminology.
- **Exception:** Proper names, technical terms, indeterminate language, and vernacular words have named exceptions.
- **Check:** Inspect markup and actual screen-reader pronunciation in relevant language support.
- **Basis:** Standard; [S28](evidence.md#s28).


## Numeric criteria and common misstatements

These are scoped web criteria, not a complete accessibility checklist. Verify current normative text in [S01](evidence.md#s01).

| Check | Correct scope | Important exception/limit |
| --- | --- | --- |
| Text contrast, 1.4.3 AA | 4.5:1 normally; 3:1 for large text | Large means at least 18 pt, or 14 pt bold; incidental/inactive/decorative and logotype exceptions. See [S21](evidence.md#s21). |
| Non-text contrast, 1.4.11 AA | 3:1 for required visual information identifying controls/states and graphical objects | Does not apply to every decorative border; evaluate the actual required information. See [S22](evidence.md#s22). |
| Text resizing, 1.4.4 AA | 200% without content/function loss | Captions and images of text have exceptions; this is not a universal 16 px minimum-font rule. See [S31](evidence.md#s31). |
| Reflow, 1.4.10 AA | Equivalent 320 CSS px width for vertical content, or 256 CSS px height for horizontal content | Necessary two-dimensional content is scoped; surrounding content still needs reflow. See [S23](evidence.md#s23). |
| Targets, 2.5.8 AA | At least 24 × 24 CSS px, or a named exception | Spacing, equivalent, inline, unmodified UA, essential. 44 × 44 is enhanced AAA 2.5.5, not this AA criterion. See [S24](evidence.md#s24). |
| Focus not obscured, 2.4.11 AA | Focused component is not entirely hidden by author-created content | Not the same as full visibility or indicator appearance. See [S25](evidence.md#s25). |
| Focus appearance, 2.4.13 AAA | Enhanced indicator area/contrast requirements | Do not mislabel the 2 CSS px perimeter-area and 3:1 change-of-contrast requirements as AA. See [S32](evidence.md#s32). |

For semantic/keyboard patterns consult [S20](evidence.md#s20). This guide deliberately does not enumerate every WCAG criterion: full conformance requires a complete applicable evaluation.
