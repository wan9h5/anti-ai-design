# Verify proportionately

Select checks from the actual change and risk. Evidence can come from source, a browser, tests, measurements, or users; report the method and boundary. A screenshot-only review has an inspection result, not a behavior test result.

## Task and functionality

Use representative content and at least the main requested task. Confirm that controls produce the promised effect and the result remains linked to the current inputs. Relevant checks include validation, no results, service error, permission denial, partial success, cancellation, retry, persistence after reload, and stale output after changes.

For a demo, verify that simulated data and execution are visibly labeled where users act and interpret results. Confirm links/downloads resolve and file content corresponds to the displayed run where tools allow. Do not transmit real datasets just to validate a mock.

## Accessibility and content resilience

Load [accessibility](../references/accessibility.md) for precise criteria and exceptions. Use automated checks as diagnostics, then manually inspect the changed task:
- keyboard access, focus visibility/order, modal behavior, and escape/recovery; after filtering, claiming, deleting, or rerendering a selected item, verify the actual active element remains a useful existing target, including no-result states;
- when comparison tables or charts need horizontal scrolling, test reaching the scroll container with Tab and scrolling it with arrow keys; reachable row buttons alone do not prove keyboard access to all comparison content;
- names, roles, states, labels, error association, and status announcements;
- text/background and meaningful non-text contrast, with actual colors;
- color-independent state interpretation;
- pointer target size or applicable spacing/other exception;
- text resizing, reflow, long content, localization, and assistive technology as available;
- reduced-motion and other relevant preferences.

Report browser, viewport/zoom, relevant assistive technology, method, and result when tested. If a criterion was not checked, mark it untested. A component library or automated scan does not establish conformance.

## Visualization and performance

For charts, check the question, population/time range/units, source/recency, aggregation/denominators, scales, missing data, limits, and an equivalent text/data representation. Test filter effects and tooltip alternatives.

Inspect the rendered chart, not only its data and accessible description. For stroke-only SVG axes, grids and lines, explicitly suppress fill and check that open paths do not produce unintended filled areas that change the apparent encoding.

For performance changes, distinguish a reproducible lab diagnostic from field experience. Record device/network/test method and relevant loading, input responsiveness, or stability measures. Never infer Web Vitals from a still image, substitute a Lighthouse score for field evidence, or attribute a slowdown to an effect without profiling. See [performance and integrity](../references/performance-integrity.md).

## Completion record

Report completed checks, failures addressed, skipped checks with reasons, and important remaining uncertainties. If representative user testing has not occurred, describe expected benefits as hypotheses. Do not broaden testing indefinitely after appropriate checks pass; add checks when new changes, failures, or unresolved risks justify them.
