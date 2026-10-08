# Worked review example: synthetic analysis workbench

This example is synthetic and contains no original screenshot, dataset, product/run identifier, or scientific claim.

## Supplied evidence

A static mock screen has three regions: describe a job, review a fixed plan, and inspect a completed result. It visibly labels demo data and deterministic processing. A small message says prose cannot change the workflow. The main action says “Generate analysis plan.” Results show percentages, a short list, downloads, and a provenance area. Source, live interaction, viewport behavior, and computed styles are unavailable.

## Findings

| Finding | Basis/confidence | Change | Discriminating check |
| --- | --- | --- | --- |
| “Generate” can suggest a flexible plan while the available workflow is fixed. | Observed label mismatch; interpretation hypothesis, medium confidence. | Name “Prepare this fixed workflow” or explain what the text actually controls beside the action. | Ask target users to predict what changes after editing the description. |
| Output is shown beside editable inputs, but the screenshot cannot establish version binding. | Unverified capability concern, provisional. | If output persists after changes, mark its input/plan version and stale state. | Change a consequential input in the prototype. |
| Percentage metrics need their defined population and sample mode to be interpreted correctly. | Scope is not visible beside every value; product concern. | Provide concise definitions and shared mode context at the result. | Ask users what the denominator is and what the result demonstrates. |
| Small bilingual result text may impose reading effort. | Visual observation; user effect and contrast remain unknown. | Establish primary UI language, retain technical terms, inspect actual type/color values and enlargement. | Measure contrast/size and test reading/comprehension with relevant users. |

## Preserve

The explicit demo/deterministic disclosures, staged task model, supporting result data, and provenance are useful design choices. Do not remove them to make the screen look more polished. A dark result area or a three-region desktop composition is not inherently defective.

## Limits and next checks

A screenshot cannot establish keyboard semantics, download integrity, backend truth, performance, text zoom, or narrow-view behavior. It also cannot establish whether the displayed analytical conclusion is scientifically valid. The next useful check is the actual input → plan → execution → output path, including stale output, failure, and demo scope.
