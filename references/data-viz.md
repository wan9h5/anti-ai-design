# Data visualization

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP033: Chart has no question

- **Signal:** A visualization is added to make a screen look analytical.
- **Risk:** Complexity has no decision value.
- **Repair:** Identify comparison, trend, distribution, or other question before choosing encoding.
- **Exception:** A visualization can support exploration if its scope is clear.
- **Check:** Ask what a user can decide from this chart.
- **Basis:** Synthesis; [S13](evidence.md#s13).

## AP034: Metric lacks scope or denominator

- **Signal:** A percentage/count omits unit, population, time range, aggregation, or recency.
- **Risk:** Meaning can be overstated or misunderstood.
- **Repair:** Expose definition/source and relevant denominator/filter context.
- **Exception:** A compact metric can rely on clear nearby shared context.
- **Check:** Explain the value and reproduce it from the stated data.
- **Basis:** Synthesis; [S13](evidence.md#s13).

## AP035: Encoding distorts magnitude or relationship

- **Signal:** Bars start above zero; 3D/area or dual axes imply misleading differences.
- **Risk:** Visual comparison can diverge from underlying values.
- **Repair:** Use a truthful encoding; bar magnitude needs a meaningful zero baseline, or choose another chart.
- **Exception:** Line/dot charts can use a non-zero range when clearly disclosed and appropriate.
- **Check:** Compare the visual conclusion to the underlying numbers and scale.
- **Basis:** Guidance; [S16](evidence.md#s16).

## AP036: Color/hover is the only interpretation route

- **Signal:** Legend/color or mouse-only tooltip contains essential distinctions.
- **Risk:** Some users cannot access the chart's meaning.
- **Repair:** Provide redundant labels/encodings and keyboard/touch-accessible detail or equivalent data.
- **Exception:** Additional hover detail can supplement information already available.
- **Check:** Interpret the chart without color or a mouse.
- **Basis:** Synthesis; [S15](evidence.md#s15).

## AP037: Sample, missing, capped, or uncertain data looks definitive

- **Signal:** Mock series, absent observations, result caps, or uncertainty are not explained.
- **Risk:** Users infer completeness or precision not supported by data.
- **Repair:** Mark synthetic data, gaps, limits, and relevant uncertainty where results are interpreted.
- **Exception:** A simple teaching example can be exact within its declared synthetic scope.
- **Check:** Check if readers identify what is unknown, excluded, or simulated.
- **Basis:** Synthesis; [S16](evidence.md#s16).

## AP038: Interactivity hides the main message

- **Signal:** Filters/tooltips are required before any useful initial interpretation.
- **Risk:** Users must discover both the controls and the insight.
- **Repair:** Provide a useful default and stable context; use interaction for an actual exploration need.
- **Exception:** Expert analysis can prioritize open-ended exploration over a single narrative.
- **Check:** Test first arrival and changed filters with equivalent text/data access.
- **Basis:** Guidance; [S13](evidence.md#s13).
