# Interaction and state

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP025: Control promises an unavailable action

- **Signal:** Filters, downloads, tabs, or buttons are styled as working but do nothing.
- **Risk:** Affordance and capability diverge.
- **Repair:** Implement the effect or give an explicit prototype/unavailable explanation at the action.
- **Exception:** Static design comps can show future behavior if their status is clear.
- **Check:** Activate the control and inspect the promised effect.
- **Basis:** Synthesis; [S33](evidence.md#s33).

## AP026: Success is only a cosmetic toast

- **Signal:** UI says saved/complete before persistence or processing is established.
- **Risk:** Users may rely on work that never happened.
- **Repair:** Tie success to confirmed effect; distinguish local draft, queued work, and completed work.
- **Exception:** An explicitly labeled simulation may animate a demo success.
- **Check:** Reload/retrieve the output or inspect execution/persistence evidence.
- **Basis:** Synthesis; [S04](evidence.md#s04).

## AP027: Changing inputs leaves an apparently current result

- **Signal:** A prior output remains after plan/filter/data changes without a stale indicator.
- **Risk:** Users may interpret output for the wrong configuration.
- **Repair:** Bind results to an input/plan version; mark stale and allow rerun/review.
- **Exception:** A historical result can remain if its scope/version is explicit.
- **Check:** Change a consequential input and inspect result labeling.
- **Basis:** Synthesis; [S33](evidence.md#s33).

## AP028: State distinctions collapse into one green dot

- **Signal:** Planned, running, skipped, and successful steps share the same appearance.
- **Risk:** The user cannot tell what actually occurred.
- **Repair:** Use named states with redundant cues and relevant evidence/status detail.
- **Exception:** A decorative dot can be valid when text conveys full state.
- **Check:** Ask what is running/completed/skipped without color alone.
- **Basis:** Synthesis; [S30](evidence.md#s30).

## AP029: Consequential action lacks scope or recovery

- **Signal:** Delete/replace/run controls omit target, effect, or recovery information.
- **Risk:** Mistakes can be expensive or irreversible.
- **Repair:** Clarify scope and provide undo/review/confirmation proportional to consequence.
- **Exception:** Safe, reversible actions may benefit from immediate execution.
- **Check:** Trigger a reversible mistake and follow the recovery path.
- **Basis:** Synthesis; [S04](evidence.md#s04).

## AP030: Validation discards work or conflates service failure

- **Signal:** Errors clear input or describe outage/permission denial as a field problem.
- **Risk:** Users re-enter work or try to fix something they cannot control.
- **Repair:** Preserve entered information and separate input repair from service recovery.
- **Exception:** A genuinely unrecoverable session may require a new start with explanation.
- **Check:** Submit a valid/invalid mix and a service error; inspect retained data.
- **Basis:** Guidance; [S10](evidence.md#s10).

## AP031: Unexplained disabled controls hide prerequisites

- **Signal:** A button is unavailable with no route to become eligible.
- **Risk:** Users cannot discover the next step.
- **Repair:** Explain the unmet prerequisite nearby or allow activation to surface useful validation.
- **Exception:** Disabled state can prevent invalid/unavailable actions when context is clear.
- **Check:** Ask what the user must do to proceed.
- **Basis:** Guidance; [S11](evidence.md#s11).

## AP032: Progress feedback invents completion certainty

- **Signal:** A percentage/timeline advances independently of actual processing.
- **Risk:** The user may misjudge wait, failure, or completion.
- **Repair:** Report real progress when known; otherwise describe current work, wait, and cancellation/retry.
- **Exception:** Labeled demo animation may intentionally simulate progress.
- **Check:** Interrupt/fail processing and verify the displayed state.
- **Basis:** Synthesis; [S29](evidence.md#s29).
