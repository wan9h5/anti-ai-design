# Night of Print — design handoff

This self-contained page follows the supplied Anti-AI Design create workflow. Only the skill and supplied task were read. The event is synthetic: Night of Print, 14 November 2026, 18:00–21:00, Studio Hall, printmaking exhibition and workshop, free registration, capacity 30.

## Task and structure

A prospective visitor needs to understand the evening, decide whether its date/location/price suit them, and try the registration interaction. The prominent date, fact strip, concise program, and direct registration link support that sequence. There is no dashboard or unrelated content. Assumptions: English interface, one attendee per sample registration; the name and email are illustrative fields. Audience research, address, timezone, accessibility arrangements, artist names, workshop timing, and live availability were not supplied and are not invented.

## Visual direction and exception

The warm peach-to-coral gradient and large Georgia serif headlines preserve the established brand requested in the brief. AP017 explicitly permits expressive marketing/editorial treatment; AP018 does not classify gradients or serif type as AI authorship. The poster-like title and original inline abstract graphic connect expression to a printmaking event. Solid paper surfaces keep the form readable. The graphic is decorative brand artwork, not an exhibition artwork or factual asset. Familiar native fields/buttons serve registration rather than being removed for novelty.

The visual choice is a proposal grounded in the supplied brand, not evidence that this treatment improves conversion or usability. There are no user-research claims.

## Actual capability

The registration link moves to the form. The form validates a nonblank name and browser email syntax, retaining values after errors. Valid input produces a preview with the exact submitted name/email and event details. Editing hides the prior result, retaining the values; clearing removes both input and result values and returns focus to the name field. No external resources, network calls, backend, storage, capacity decrement, or email transmission are used. Details reside in the current document memory and disappear on reload. Capacity is presented as a supplied event limit, never as a live seats-remaining count.

The synthetic/local boundary appears beside the action and again in the result. “Preview my registration” describes the actual effect. No success message claims a booking has occurred. There is no loading state because no asynchronous work occurs. JavaScript-disabled users see an explanation that the prototype cannot book.

## Checks and limits

Source inspection confirmed persistent labels, native form/button semantics, explicit field-error associations, inline actionable errors, useful focus destinations after preview/edit/clear, keyboard focus styles, status regions, a skip link, responsive single-column styling, and reduced-motion handling. The markup and extracted JavaScript were checked locally without dependencies. Calendar weekday was checked from the supplied date.

No browser was used in this agent's work, as instructed. Rendered contrast, 320px reflow, 200% text resizing, full keyboard completion, screen-reader announcements, browser email validation behavior, and visual composition remain unverified. These source provisions do not establish WCAG conformance. Parent browser verification should exercise invalid and valid submission, edit after preview, clear, reload, narrow viewport, keyboard navigation, and absence of transmission. No user testing or field performance measurement was performed. No publishing or installation occurred.
