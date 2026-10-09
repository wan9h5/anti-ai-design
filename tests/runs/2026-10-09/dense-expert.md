# Expert reconciliation refactor

The intended user is an expert reviewer performing frequent comparisons and row actions with keyboard or pointer. The supplied task explicitly requires retaining columns and tasks. The deliverable keeps all seven columns, both accounts, assigned reviewers, the received-minus-expected delta, AC-01 resolution, and AC-02 invoice inspection. No data values were altered; monetary values use two decimal places and thousands separators.

## Source findings and decisions

| Evidence observed in supplied source | Priority / basis / confidence | Change and exception considered |
| --- | --- | --- |
| Cells, headers and buttons use 10px text; cells have 1px padding. | Moderate, provisional task friction; AP011 synthesis; high confidence in CSS, unmeasured readability impact. | Use compact 14px data with 30px minimum button height and 7px cell padding. Experts still need density; retaining the table and its shared column axes matters more than making sparse cards. |
| Amounts are unformatted and share default left alignment. | Moderate; comparison guidance, expected scan benefit remains a hypothesis. | Align three monetary columns on the right and use tabular digits and consistent decimals. Currency and delta definition remain explicit. |
| Resolve modifies the status but offers no recovery. | Moderate; AP029 synthesis; high confidence from source. | Immediate local resolution with Undo in the same button. Status and amounts stay distinct: resolving review does not erase or settle the negative delta. No confirmation is needed for this reversible demo change. |
| Details uses a blocking alert containing the synthetic invoice reference. | Moderate; interaction guidance; high confidence from source. | Inline invoice-reference section, retaining INV-02 and AC-02. Native buttons expose expanded state, close/Escape return focus to the opener. No document contents are invented. |
| Synthetic local data is already disclosed in the title. | Useful existing choice, high confidence. | Preserve prominent synthetic/local disclosure and state that reload resets changes. Reinforce the absence of an invoice document next to invoice details. |

The visual direction is a restrained accounting work surface: one aligned table, light column header strip, stable account identifiers, muted borders and text labels for every status. Color supports Review/Matched/Resolved without carrying meaning alone. The account column remains sticky within the horizontally scrollable table. Narrow layouts retain all fields and scope horizontal scrolling to the comparison area; surrounding instructions wrap.

## Capability contract

- **Resolve AC-01:** activation toggles Review → Resolved in memory; amounts and −20.00 USD delta remain unchanged. A polite status message announces the result. The existing action button becomes Undo resolve and retains its DOM identity and focus. Undo restores Review. Reload restores the original source data. No financial processing or backend persistence occurs.
- **Inspect AC-02 invoice:** activation reveals INV-02 and the existing row's amounts/reviewer in an inline section. No invoice document is available. Close or Escape hides the section and restores focus to the same inspect button. This is a nonmodal disclosure, so there is no focus trap.
- **Table access:** semantic table with column and row headers, labeled scroll region, all seven columns intact. Native keyboard button activation is preserved. Status changes do not filter/remove the row or alter the monetary comparison.

## Inspection and limits

Read the supplied HTML, the skill entry, review/create/verify workflows, reference index, layout/density, interaction, accessibility and output-contract references. Inspected the refactored source for data preservation, semantic headers, action scope, native controls, focus-return code, local-only state, and responsive scroll containment. Per task constraints, no browser was used, no dependencies installed and nothing published.

Static checks confirm exactly seven column headers and two data rows; expected/received values and the original synthetic invoice identifier remain present. Inline JavaScript syntax was checked with the available Node executable. These checks do not establish rendered geometry, actual keyboard behavior or accessibility conformance.

Remaining browser checks: activate Resolve then Undo with keyboard and pointer; verify focus remains on the existing button and the status/delta distinction is clear; open/close invoice with Enter, Space, Close and Escape and inspect activeElement; check focus outlines, scroll-region keyboard behavior and all-column access at desktop, 320 CSS px equivalent width, and 200% text enlargement; measure actual target sizes and contrast in all states; inspect screen-reader table navigation and polite announcements. No usability study, screen-reader run or rendering measurement has been performed. Faster expert comparison is an intended benefit requiring representative task validation, not a measured result.
