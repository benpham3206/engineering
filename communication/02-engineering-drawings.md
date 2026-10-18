# Engineering drawings

**Type:** lesson

An engineering drawing is the set of instructions a machinist, inspector, or supplier uses to make a part. It has to say the same thing to everyone who reads it, so it follows strict conventions for layout, lines, and dimensions. For how to model and draw parts in CAD and how to use geometric dimensioning and tolerancing, see [the design folder](../design/README.md).

**Prerequisites:** none. Helpful first: [01-technical-writing.md](01-technical-writing.md) for the habit of stating things precisely.
**Time:** 8-12 h

## Core ideas

- **A drawing is the binding specification.** If a dimension or note is missing, the maker has to guess. Every feature the part needs must be defined on the drawing or in a document it refers to.
- **Views show the shape.** A single view cannot show a three-dimensional part. Standard views (front, top, right side) show the part from directions that line up with each other.
- **Lines carry meaning.** Each line style means something specific. A reader should be able to tell a visible edge from a hidden one at a glance.
- **Dimensions give size.** Every size on the drawing comes from a dimension, not from scaling the picture. Drawings are not drawn to scale for the reader.
- **The title block identifies the drawing.** It holds the part name and number, the material, the units, the scale, the revision, and the signatures or approvals.

### Title block

The title block is usually in the lower-right corner. Common entries:

- Part name and part number
- Drawing number and revision letter (any change to the part changes the revision)
- Material and finish
- Units (millimetres or inches) and a note on the default tolerance
- Scale, for example 1:2 or "NTS" (not to scale)
- Drawn by, checked by, and date
- Sheet number, for example "1 of 2"
- Projection symbol (first angle or third angle)

### Views and projection

- **Orthographic projection** shows the part as flat views taken along perpendicular directions.
- **Third-angle projection** is the standard in the United States (ASME Y14.3). The top view sits above the front view, and the right-side view sits to the right of the front view. Imagine the views on the faces of a glass box around the part, then unfold the box.
- **First-angle projection** is common in Europe and ISO drawings. The views sit on the opposite sides, so the top view goes below the front view. Always check the projection symbol before you read a drawing.
- Use the fewest views that define the part completely. Add a section view when internal features are hidden.
- An **isometric view** (a single angled picture) helps the reader see the part but does not replace the orthographic views.

### Line types

- **Visible edge line:** a thick, continuous line. This is the outline of the part as seen from that view.
- **Hidden line:** a medium, short-dash line. It shows edges behind the surface.
- **Center line:** a thin line made of long and short dashes. It marks the axis of a hole, shaft, or symmetric feature.
- **Dimension line:** a thin continuous line with arrowheads at each end, placed between extension lines.
- **Extension line:** a thin line that leaves a gap from the object and extends past the dimension line.
- **Section line (cutting plane):** a thick line with arrows at its ends showing the direction of view. Cross-hatching inside a section shows cut material.
- **Phantom line:** a thin line with a long dash followed by two short dashes. It shows an alternate position or an adjacent part.

Line weights should be consistent: thick for visible edges, thin for everything else.

### Dimensioning rules

- Give each feature a size and a location. A hole needs its diameter, its position relative to a datum or edge, and its depth if it is not through.
- Dimension each feature once. Repeated dimensions create conflicts when someone changes one value and forgets the other.
- Place dimensions on the view that shows the feature most clearly. Keep them outside the outline where you can.
- Do not use a dimension that the reader must add or subtract to find a size. Give the size directly, unless it is a reference dimension, which is marked "(REF)".
- Put the units in the title block and do not repeat them on every dimension.
- Include tolerances where the fit matters. A plus-minus value on every dimension is not required, but the default tolerance note must be present.
- Give a datum or reference edge for location dimensions, so the reader knows what each distance is measured from.

## Checklist

Use this to review a drawing before release.

- [ ] Title block is complete: part name, number, revision, material, units, scale, and projection symbol.
- [ ] Views are the fewest needed to define every feature, and they are aligned using the projection rules.
- [ ] Visible, hidden, center, and section lines use the standard styles and weights.
- [ ] Every feature has a size and a location.
- [ ] No feature is dimensioned twice.
- [ ] Each location dimension has a datum or reference edge.
- [ ] Default tolerance note is present.
- [ ] Notes cover finish, heat treatment, or other specifications not shown by the geometry.
- [ ] Someone else has checked the drawing against the CAD model.

## Example

**Task.** You need a drawing for a rectangular aluminum bracket with two through holes and one blind hole. The bracket has a front view, a top view, and a right-side view. Write a list of what the drawing must show.

**Solution outline.**

1. **Title block.** Part name "Bracket, mounting," part number, revision A, material "6061-T6 aluminum," units millimetres, scale 1:1, projection symbol third-angle, default tolerance note.
2. **Views.** Front view shows the outline and the two through holes as visible circles. The top view shows the hole positions from above and the hole depth as hidden lines through the body. The right-side view shows the thickness.
3. **Line types.** Hole centers marked with center lines. The hidden line for the blind hole appears in the front section, not in the top view if the hole is not visible there.
4. **Dimensions.** Overall length, width, and thickness. Hole diameter callouts. Each hole located from the left edge and the bottom edge, with those edges labeled as datums.
5. **Notes.** "Break all sharp edges," if the design calls for it.

**Sanity check.** Could a machinist make the part from this drawing alone, without asking you a question? Walk through each feature and confirm it has a size, a location, and a line style that shows where it is.

## Practice

1. Sketch, by hand, the front, top, and right views of a simple L-bracket in third-angle projection. Label which view is which.
2. Dimension that bracket so every feature is defined exactly once. Count your dimensions, then look for any that are duplicated or missing.
3. Fill in a title block for it: part name, part number, material, units, scale, default tolerance, drawn by, date, revision.
4. Find a free drawing online (a product manual or a CAD tutorial) and list three things it does well and one rule from this lesson it breaks.

<details><summary>What a good answer includes</summary>

1. The top view sits above the front view and the right view sits to the right of it. Hidden edges are dashed.
2. Each length, width, height, hole size, and hole location appears once. No chain of dimensions closes on itself.
3. Every field is filled in, the units are stated once, and a default tolerance note such as "+/-0.1 mm unless noted" is present.
4. Common faults: missing units, duplicate dimensions, dimensions to hidden lines, no default tolerance.

</details>

## Common mistakes

- Dimensioning the same distance two ways, which can create conflicting values.
- Leaving out the projection symbol, so the reader cannot tell which side each view is on.
- Using dashed lines for visible edges, or thick lines for center lines.
- Adding views that repeat information already shown in another view.
- Forgetting the revision letter after a change, which lets the shop build the old design.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts, a free engineering library. Search the mechanical engineering shelf for graphics or design texts.
- [Design folder](../design/README.md) by this repository, covering engineering graphics, CAD, and GD&T topics that build on this lesson.
