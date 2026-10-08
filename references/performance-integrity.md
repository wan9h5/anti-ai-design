# Performance and capability integrity

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP046: Visual polish spends performance without measurement

- **Signal:** Heavy effects/assets are added without understanding the target device/workload.
- **Risk:** Loading or interaction may slow, but the cause remains unknown.
- **Repair:** Profile representative usage and spend asset/effect cost on user value.
- **Exception:** Useful imagery, visualization, or motion can justify cost when measured.
- **Check:** Compare the relevant bottleneck with/without the feature in target conditions.
- **Basis:** Hypothesis; [S18](evidence.md#s18).

## AP047: Lab score is claimed as real-user speed

- **Signal:** A single desktop load or Lighthouse score stands in for field experience.
- **Risk:** User/device variation and post-load interactions disappear.
- **Repair:** Report lab diagnostics and field measurements separately with conditions.
- **Exception:** Pre-release work legitimately relies on lab diagnostics, with clear limits.
- **Check:** Check interaction/stability during the task and available p75 field data.
- **Basis:** Guidance; [S17](evidence.md#s17).

## AP048: Loading/resizing shifts the action target

- **Signal:** Late content/font/asset dimensions unexpectedly move controls.
- **Risk:** Users may misclick or lose position.
- **Repair:** Reserve predictable space and inspect layout stability under realistic loading.
- **Exception:** Intentional user-requested layout change has different interpretation from unexpected shifting.
- **Check:** Load slowly, interact, and observe unexpected movement.
- **Basis:** Synthesis; [S17](evidence.md#s17).

## AP049: Capability claim exceeds actual execution

- **Signal:** The UI says AI analyzed/integrated/live while only a fixed parser or fixture ran.
- **Risk:** Users may rely on an unsupported capability.
- **Repair:** Name the actual mode and limits near action/output; document what really ran.
- **Exception:** A fixed or mock workflow is valid when clearly disclosed.
- **Check:** Match each capability claim to code/execution/output evidence.
- **Basis:** Synthesis; [S33](evidence.md#s33).

## AP050: Provenance becomes decoration

- **Signal:** A run badge/ID exists without useful access to inputs, versions, parameters, or artifacts.
- **Risk:** Trust language has no practical verification path.
- **Repair:** Provide relevant traceability and an inspectable relationship between input, plan, execution, and output.
- **Exception:** A simple local demo may need only a small explicit provenance record.
- **Check:** Reconstruct one output's configuration and retrieve its stated artifacts.
- **Basis:** Synthesis; [S33](evidence.md#s33).

## AP051: AI confidence replaces decision support

- **Signal:** A fluent summary or precise confidence badge lacks meaning, limits, or correction routes.
- **Risk:** Users can over-rely on an uncertain answer.
- **Repair:** Explain applicable uncertainty and enable inspection/correction proportional to the task.
- **Exception:** Reliable deterministic calculations can be precise within their stated assumptions.
- **Check:** Ask users to distinguish model suggestion, evidence, and confirmed execution.
- **Basis:** Synthesis; [S33](evidence.md#s33).

## AP052: Review mistakes appearance for truth

- **Signal:** An audit declares dead buttons, fast performance, WCAG failure, or real data from a still image.
- **Risk:** Unsupported findings can drive wrong refactors.
- **Repair:** State observable evidence and test the relevant behavior before concluding.
- **Exception:** Screenshot-only visual review is legitimate with bounded claims.
- **Check:** For each assertion, identify the observation or test that supports it.
- **Basis:** Synthesis; [S18](evidence.md#s18).


## Measurement limits

The checked [Web Vitals guidance](evidence.md#s17) uses good-experience targets of LCP ≤ 2.5 s, INP ≤ 200 ms, and CLS ≤ 0.1 at the 75th percentile, with mobile/desktop segmentation. These are dated guidance targets, not guarantees of task quality. Recheck evolving definitions before future measurement.

INP concerns input-to-next-paint responsiveness, not completion of a long server/analysis job. A fast acknowledgement can coexist with a long wait; assess the actual job's feedback, outcome, and recovery separately. Lab diagnostics and field evidence answer different questions.
