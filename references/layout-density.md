# Layout and density

Each entry is a candidate diagnosis. Its trigger is evidence to inspect, not proof of harm or AI authorship. Check the exception and the actual task before changing the interface. Sources and labels are defined in [evidence.md](evidence.md).

## AP009: Card grid weakens comparison

- **Signal:** Repeated records use differently positioned fields in separate cards.
- **Risk:** Scanning and comparing like attributes become harder.
- **Repair:** Use aligned rows or consistent card fields based on the comparison task.
- **Exception:** Heterogeneous browseable summaries can suit cards.
- **Check:** Compare two records on the same attributes with representative content.
- **Basis:** Guidance; [S05](evidence.md#s05).

## AP010: Low density pushes routine work away

- **Signal:** Large spacing/headings consume the working area while key data scrolls out.
- **Risk:** Frequent tasks may require extra navigation.
- **Repair:** Allocate space to relevant work; consider deliberate compact/comfortable variants.
- **Exception:** Focused novice or sensitive forms may benefit from a sparse composition.
- **Check:** Measure scroll/context switches on the supported task and viewport.
- **Basis:** Synthesis; [S03](evidence.md#s03).

## AP011: High density shrinks meaning and control

- **Signal:** Labels, data, and controls overlap or become hard to read/activate.
- **Risk:** More visible data may produce less usable information.
- **Repair:** Reduce unnecessary content and improve hierarchy before shrinking text/targets.
- **Exception:** Dense expert tables are valid when readability, input access, and comparison remain sound.
- **Check:** Try realistic long values and target-input tasks; inspect actual sizes.
- **Basis:** Synthesis; [S12](evidence.md#s12).

## AP012: Equal-height panels create an arbitrary hierarchy

- **Signal:** A short input panel reserves unused height while evidence is constrained.
- **Risk:** Allocation follows geometry rather than current work.
- **Repair:** Let content and task priority guide area; consider resize/collapse for interdependent work.
- **Exception:** Persistent spatial positions can help expert orientation.
- **Check:** Test the longest meaningful result, not just the demo state.
- **Basis:** Hypothesis; [S03](evidence.md#s03).

## AP013: Nested surfaces fragment related content

- **Signal:** Every group gets a card, border, shadow, and inner card.
- **Risk:** Visual boundaries imply separation that the task does not need.
- **Repair:** Use proximity, type, alignment, and a few meaningful boundaries.
- **Exception:** Independent interactive units may require strong containment.
- **Check:** Ask whether each boundary denotes a real group or interaction.
- **Basis:** Synthesis; [S07](evidence.md#s07).

## AP014: Fixed desktop composition loses narrow/zoom access

- **Signal:** Panels clip or critical controls disappear when space decreases.
- **Risk:** Users cannot read or complete the supported task.
- **Repair:** Design responsive priorities and inspect reflow; keep necessary two-dimensional regions scoped.
- **Exception:** Tables/maps may retain two-dimensional layout where essential to meaning.
- **Check:** Check equivalent 320 CSS px width and surrounding prose/control reflow.
- **Basis:** Standard; [S23](evidence.md#s23).

## AP015: Removing information creates cosmetic simplicity

- **Signal:** Units, context, labels, or recovery disappear to make a cleaner screen.
- **Risk:** Apparent simplicity hides necessary work.
- **Repair:** Restore required task information and move optional detail deliberately.
- **Exception:** A distraction-free mode can be valid if essential controls remain reachable.
- **Check:** Complete the task without relying on removed explanations.
- **Basis:** Guidance; [S07](evidence.md#s07).

## AP016: Responsive stacking ignores task relationships

- **Signal:** A narrow view mechanically stacks every panel, separating coupled controls/results.
- **Risk:** Users may lose context or action/evidence connections.
- **Repair:** Order and group by the narrow-screen task; preserve state across view changes.
- **Exception:** Simple independent reading sections often stack successfully.
- **Check:** Repeat the task at narrow width with long/expanded content.
- **Basis:** Synthesis; [S23](evidence.md#s23).
