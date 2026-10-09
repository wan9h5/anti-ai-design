# Monthly incident trend: rationale and verification

## Task and supplied facts

Users need to see the January–June 2026 trend and retrieve exact monthly counts without a mouse. Supplied synthetic counts are January 18, February 25, March 21, April 30, May 24, and June 16, in incidents/month. The fixture is generated for the demo and contains no production data. No organization, severity, exposure denominator, refresh schedule, or broader reporting period was supplied.

Assumption: this is a read-only six-month trend view, so filtering, downloads, and data editing are unnecessary. The cost of error is a mistaken comparison or treating a fixture as operational evidence.

## Design rationale

A labeled line chart shows the temporal pattern; a permanently visible semantic table supplies the same six exact values. A short prose summary gives a third interpretation route. Users do not need hover, color discrimination, or JavaScript to obtain any count. All three representations identify April as the peak and June as the minimum.

The chart uses evenly spaced months and a linear vertical scale from 0 to 35 incidents/month. Points map to `y = 300 − 7 × count`; straight segments connect observations without inventing intermediate measurements. There are no missing months. A single teal series needs no color legend. Text labels, units, time range, source, and demo provenance are explicit.

The visual direction is a restrained reporting sheet: warm neutral page, dark type, aligned numeric table cells, and one teal chart line. The wide chart has a locally scrollable, keyboard-focusable container on narrow screens; surrounding prose and the two-column table are fluid. A static SVG has a title and description, and the table uses a caption and scoped headers. These choices implement the supplied skill's AP033–AP038 guidance and applicable accessibility guidance; they are design proposals, not evidence of measured usability improvement.

## Functionality boundary

Self-contained HTML/CSS/SVG; no dependencies, scripts, network calls, backend, persistence, or production feed. All data and calculations are fixed. Synthetic provenance is shown above the chart, in the table caption, and beside source details. Counts are not rates and cannot establish causes. No controls imply unavailable actions.

## Completed checks

- Python HTML parsing confirmed the six table values exactly match the supplied fixture.
- XML parsing confirmed six SVG points and their coordinates match the stated linear scale.
- Source inspection confirmed the month/value labels, zero baseline, units, time range, accessible SVG title/description, table header scopes, source and synthetic labels, and absence of external resources or scripts.
- Arithmetic checked the summary: peak 30 in April, minimum 16 in June, and June minus January = −2.
- Calculated specified solid-color contrast: dark text on white 14.22:1; muted text on page 6.51:1; teal line on white 5.79:1. These are token calculations, not rendered accessibility results.

## Limits and next validation

Actual browser inspection was unavailable and prohibited for this task. No browser, installation, publishing, or agent delegation occurred. Root will perform DOM logic verification. Keyboard scrolling, actual focus appearance, rendered label positioning, 320 CSS-pixel reflow, 200% text enlargement, screen-reader output, and printed appearance remain untested. No claim of WCAG conformance or improved task completion is made.

The focused next validation is to inspect the page at desktop and 320 CSS pixels, enlarge text to 200%, read the trend and table with a screen reader, and check keyboard scrolling/focus. Confirm users can find April's count and June's count without a pointer.
