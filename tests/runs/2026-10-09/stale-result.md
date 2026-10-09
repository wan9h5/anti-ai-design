# Threshold report refactor

The task is to edit a threshold and understand which configuration produced the visible count. The supplied input has a real local calculation over synthetic values `[5,12,20]` and an original saved run `DEMO-01` at threshold `10`. I assume fractional and negative finite thresholds are allowed because the source supplies no business restriction. The comparison remains strictly greater than, as in the source.

## Inspection and rationale

**Observed in source, major priority, high confidence:** the number input can change while `#result` continues to show `Items above threshold: 2`. Only the Run button updates that output, and the report itself has no threshold attribution or stale indication. That creates an ambiguous association between an edited threshold and the displayed count. Actual user error was not measured. The anti-ai-design interaction reference AP027 calls for binding the result to inputs; this is synthesis rather than a product-specific standard.

The valid exception is retaining a historical report. The fix preserves it and makes its scope explicit rather than clearing it on edits. The latest result always names its calculated threshold, matching values, and run ID. Editing to a different valid threshold immediately marks it **Previous result**, names the draft threshold, and gives the next action. An invalid/empty draft also marks the report previous and shows a field error. Returning to the latest run's threshold restores **Current result** without requiring a redundant calculation.

The original saved run remains in the history table after subsequent calculations. Each completed calculation adds a session run with its own threshold and count. The fixed fixture source and strict comparison rule are visible beside the action and in provenance. The typography and restrained teal/amber treatment establish hierarchy; state meaning is conveyed in words as well as color. A small aligned table supports comparing thresholds without creating a dashboard or hiding provenance in decorative panels.

## Capability and state contract

- Finite number input → local JavaScript filters the three fixed synthetic values using `value > threshold` → count, matching values, run ID, and history row.
- Changing input never silently recomputes or removes the latest report. Invalid submission retains both the entered input and historical result, focuses the field, and adds no run.
- Initial saved snapshot: `DEMO-01`, threshold `10`, count `2 of 3`. Original provenance remains intact.
- New runs use IDs `DEMO-02` onward and exist only in page memory. Reloading restores the original saved snapshot and clears session additions. This limitation is stated in the history caption. No server, network call, external saving, or generated execution progress is implied.
- Covered states: current original result, changed input/previous result, exact revert, completed local calculation, invalid/empty input, zero matches, and history retention. The tiny synchronous calculation has no meaningful loading state or service failure state.

## Actual checks and limits

Read the supplied HTML and the applicable anti-ai-design review/create/verification, interaction, accessibility, evidence, and handoff instructions. No other supplied prototypes or other agents' outputs were read.

Executed the embedded JavaScript in Node with a minimal DOM stub. Assertions passed for: edit `10 → 15` marks prior threshold `10`; exact revert restores current; running at `15` produces `1 of 3` and `DEMO-02`; blank and invalid input preserve history and output; `20` produces zero matches; `-1` includes all three; `12` excludes equality; original saved-row markup and synthetic source disclosure remain present. These are logic-level checks, not rendered browser tests.

Source inspection confirms native label/form/button semantics, an associated inline error and `aria-invalid`, a polite status region, visible-focus CSS, responsive wrapping, and no external dependencies. Browser rendering, actual number-input behavior, keyboard focus, live-region announcements, narrow viewport/200% text resizing, computed contrast, and assistive technology remain unverified. No whole-product accessibility conformance or measured usability improvement is claimed.

Recommended browser check: edit the threshold without submitting and confirm both the old count and its threshold remain legible with a previous-result notice; run again and inspect the original and new history rows; clear the field; check zero matches at `20`; revert to the latest threshold. Inspect at 320 CSS px and enlarged text, then perform the edit/run flow by keyboard. The root agent will perform browser verification separately.
