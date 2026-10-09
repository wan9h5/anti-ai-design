# Incident desk handoff

Artifact: `create-triage.html` (self-contained HTML, CSS and JavaScript; no dependencies or network requests).

The on-call operator needs to identify the next incident to own without overlooking existing ownership. Severity, owner and fixed sample age are aligned in one comparison table. Critical incidents come first, then unowned incidents within a severity, then older incidents. INC-01 therefore appears first and exposes the primary Claim action. Existing Ada and Lin assignments remain visible and cannot be overwritten.

The visual direction is a restrained operational desk: dark masthead, warm neutral workspace, compact aligned rows, monospace incident identifiers and red reserved for critical severity and unowned work. Counts show whole-queue totals; the queue heading separately reports the filtered count. This hierarchy is intended to support scanning, but improved triage speed has not been measured.

Severity and owner filters combine immediately. Claim changes an unowned record to You; Release provides immediate recovery. Reset sample restores original owners while retaining filters. A filtered-out claim moves focus to the owner filter; an action remaining in the table receives focus on its replacement control. Empty results provide a working Clear filters action. Filter and action updates announce status through a polite live region.

Synthetic data and local effects are disclosed near the work area, the action column says Local action, and footer/help text explain that changes last only until reset or reload. Ages do not advance. There is no production connection, persistence, incident resolution or reassignment of others' records.

Checks completed: Node syntax check and a DOM-stub execution covering initial order, severity/owner filters, claim, release, no-result state, focus fallback, replacement focus, reset and protection of assigned owners. All passed. Source inspection confirms native labeled selects/buttons, table headers, explicit severity labels, visible keyboard focus styling and no external assets.

Not checked: real browser layout, actual keyboard sequence, zoom/reflow, rendered contrast, assistive technology announcements or representative operator usability. The root evaluator will perform browser verification. Source and stub checks do not establish accessibility conformance.
