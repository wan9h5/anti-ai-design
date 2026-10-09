# Analysis preview demo

Artifact: `truthful-demo.html` (self-contained; inline styles and JavaScript).

The assumed user is inspecting a small sample before analysis. The useful task is to select one of the two supplied synthetic fixtures and inspect the actual arithmetic. A focused input-and-result composition keeps the chosen sample, its values, and its summary together. Notebook typography and a restrained green action provide a deliberate visual direction without implying a larger monitoring product.

The requested AI analysis button is labeled **AI analysis · preview**. Adjacent copy explicitly states that no model or backend exists. Activating it computes only local mean and range, and reveals a proposed future handoff. The result repeats **Local fixture · no AI execution**, identifies the selected fixture, shows its values and formulas, and states that AI analysis was not run. Future model and review steps are marked unavailable/planned, never completed. There is no fabricated model narrative, confidence percentage, loading animation, or server response.

The fixtures are exactly SYN-01 = [2, 4, 6] and SYN-02 = [3, 3, 3]. Mean is sum divided by count; range is maximum minus minimum. No units, scientific meaning, or additional samples were invented. Changing the input clears the previous result and future flow; rerunning binds the summary to the new selection. Reload discards results. No data is transmitted or persisted.

## Checks completed

A Node VM executed the actual embedded script against a minimal mock DOM. Assertions passed for SYN-01 mean 4/range 4, SYN-02 mean 3/range 0, source labeling, clearing results after sample change, revealing the future flow after activation, and recovery from an unknown input. A source check found unique IDs and no external script/style asset, network call, or storage API. No packages were installed and nothing was published.

## Verification limits

The mock DOM check verifies script effects, not browser behavior. Browser rendering, keyboard interaction, focus visibility, mobile reflow, text enlargement, contrast measurement, screen-reader announcements, and representative user comprehension remain untested here. Native button/select controls, explicit labels, visible focus styling, a polite status region, and a single-column narrow-screen rule are implemented, but do not establish accessibility conformance or improved task performance. The parent agent will verify the browser. A useful later user check is whether someone can distinguish the calculated local summary from the unexecuted future AI flow.

Skill used: the supplied `anti-ai-design` skill, including its create and verify workflows and relevant interaction/capability-integrity references. No other task outputs were inspected.
