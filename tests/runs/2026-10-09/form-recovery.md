# Form recovery refactor

Artifact: `form-recovery.html` is a self-contained local simulation with no external dependencies or network requests.

## Inspection and rationale

Read the supplied `inputs/form.html` and the Anti-AI Design skill, its review/create/verify workflows, and the interaction/accessibility references. No other outputs were read. Source inspection established two major recovery problems with high confidence: the submit handler clears both name and email when email fails its `@` check, and the same “Invalid entry” message represents both invalid email and the simulated outage. Clearing unrelated valid information causes re-entry; the outage message directs users toward field repair even though retrying the service is the relevant action. These observations match AP030's guidance, rather than establishing a broader usability or standards claim. No legitimate unrecoverable-session exception applies to this local demo.

Preserved the focused name/email form, Available/Outage selector, and honest local-demo scope. Name remains optional because the supplied implementation never validated it. Email remains required; the browser's email validity now replaces the permissive `includes('@')` test. No additional business requirement was invented.

The revised form keeps every value on validation failure, outage, retry, and success. Invalid or missing email gets specific inline repair text, an associated description, `aria-invalid`, and focus. A simulated outage gets separate service-recovery copy and a retry action without marking email invalid. Field validation precedes the simulated service call: invalid email during Outage first asks for an email correction; the next valid submission exposes the outage. Changing inputs clears the prior result so a success message cannot describe edited details.

The restrained single-column layout gives labels, inputs, recovery feedback, and the submit action a clear reading order. Borders and spacing group the simulation setting separately from entered details. State descriptions convey meaning in text independently of border color. These are reversible visual choices, not claims of measured improvement.

## Capability boundaries

The selector controls a synchronous local simulation, not a real service. The page says so near the form and selector; success also states that no data reached a server. Outage repeats on retry until the selector is changed to Available. There is no fabricated progress or backend. Retention lasts only while the current page is open; no local storage, reload persistence, or remote persistence is implemented. The visible note explains this limit. A real service integration would need confirmed responses and appropriate request-in-flight behavior.

## Checks performed

- Parsed and executed the script with Node's VM and a small mocked DOM; JavaScript syntax passed.
- Exercised invalid email with a valid name, missing email, valid email during Outage, repeated retry, switching to Available, and local success. Checked retained name/email values, distinct validation/service/success state, email error focus and attributes, retry label, and stale-status clearing after edits. All assertions passed.
- Inspected source for label associations, native controls, error association, live status, viewport declaration, responsive CSS, and explicit simulation/persistence disclosures.

## Check limits and next validation

No browser, installation, publishing, or assistive technology was used. The mocked DOM test supplies simplified validity values; it does not test native browser email validation, real focus behavior, event ordering, or announcements. Visual layout, contrast measurements, keyboard traversal, 320 CSS px reflow, 200% text enlargement, and screen-reader behavior remain untested. No full WCAG conformance or measured usability improvement is claimed.

Next, open the HTML in a browser and run the invalid-email → corrected-email/outage → Available/success sequence by keyboard, checking retained values and focus; inspect narrow and enlarged layouts and status announcements. Browser verification is assigned to the parent agent.
