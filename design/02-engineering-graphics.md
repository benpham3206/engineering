# Engineering graphics

**Type:** lesson

Engineering graphics is the language of drawings. A sketch or drawing must show a three-dimensional part in flat views so that someone else can make it without guessing. Engineers use it to think, to communicate, and to write down exactly what a part is.

**Prerequisites:** [01 Design process](01-design-process.md)
**Time:** 6-10 h

## Core ideas

- **Sketching** is fast, freehand drawing. It is for thinking, not for final dimensions. Use it to explore shapes and check proportions.
- **Orthographic projection** shows an object through several flat views, each taken along a direction that is perpendicular to the view plane. The usual set is the front, top, and right side views.
- **Projection angle.** In first-angle projection the object sits between the viewer and the projection plane. In third-angle projection the plane sits between the viewer and the object. The two systems produce different layouts of the same views. Check the symbol on the drawing so you read it correctly.
- **Isometric view** shows three faces of a part in one picture. It is not to scale in the usual sense, but it helps a reader see the shape.
- **Dimensioning** puts sizes on the views. Each feature is dimensioned once, in the view where it is clearest.
- **Sections** cut the part with an imaginary plane and show the inside. Hatch lines mark the cut surface. Sections reveal hidden holes and wall thickness.
- **Hidden lines** are dashed. They show edges behind a surface. Use them only when a view would be unclear without them.
- **Center lines** are thin lines with long and short dashes. They mark the axis of a hole or cylinder.

## Line types

Drawings use line types with fixed meanings. Learn the common ones:

- Visible outline: thick, continuous.
- Hidden edge: medium, short dashes.
- Center line: thin, long and short dashes.
- Dimension and extension lines: thin, continuous, with arrowheads at the dimension ends.
- Cutting plane line: thick, with long dashes and two dots at each end, with arrows showing the viewing direction.
- Section hatch: thin, angled, equally spaced lines on the cut surface.

Consistent line weights make a drawing easy to read. If every line looks the same, the reader cannot see what is an edge and what is a hidden feature.

## Views and their choice

Choose the fewest views that describe the part completely.

- Start with the view that shows the most shape. That is the front view.
- Add a top view or side view only when it shows a feature the front view hides.
- Use a section when the inside matters.
- Use a detail view, an enlarged view of a small area, when a feature is too small to dimension clearly.

Too many views confuse the reader. Too few leave gaps. Aim for a drawing that a machinist can read without asking questions.

## Dimensioning rules

Dimensions tell the shop what to make. A poorly placed dimension can be as harmful as a wrong one.

- Place dimensions outside the outline when the view is crowded. Keep them neat and aligned in rows or columns.
- Show each dimension with its extension line and arrowheads. Do not let a dimension line cross another dimension line if you can avoid it.
- Dimension to visible features where possible. Dimensioning to hidden features forces the reader to look twice.
- Put the most important dimensions on the view that shows the feature most clearly.
- Do not give a dimension that the machinist can calculate from others. If the sum of all the parts is given, one of them is redundant and may conflict.
- Use chain dimensions only when the error stack does not matter. For a precise location, dimension from one datum surface instead. Chain dimensions build up error, which is the subject of [04 Tolerancing and stack-up](04-tolerancing-and-stack-up.md).

## Reading a drawing

When you read a drawing, follow this order:

1. Read the title block: part name, material, scale, units, and revision.
2. Look at the overall shape in the main view.
3. Trace each view against the others. A line in one view must match a feature in another.
4. Find the section views and read the hatch to see solid and empty areas.
5. Read the dimensions and notes. Check the units.

## Common drawing conventions

- Units are shown in the title block. Most SI drawings use millimetres with the unit omitted from each number.
- Radius is written with R. Diameter is written with the symbol that looks like a circle with a slash.
- Chamfers and fillets have their own notation. Read the note for the size.
- A dimension should be placed once and only once. Repeating a dimension creates a conflict when you change the design.

## Checklist

- Are the views chosen so that every feature is visible at least once?
- Is the projection angle stated or shown on the drawing?
- Do the views line up, so that a feature shows the same height in each view?
- Are hidden lines used only where needed?
- Is every feature dimensioned once, in the clearest view?
- Are sections labeled with the cutting plane letter and the viewing direction?
- Does the title block have the units, scale, and revision?

## Example

A simple block with a through hole is drawn for a machinist.

- **Given.** A rectangular block 60 mm (2.36 in) long, 40 mm (1.57 in) wide, and 20 mm (0.79 in) high. A round through hole of diameter 10 mm (0.39 in) is centered 30 mm (1.18 in) from the left end and 20 mm from the front.
- **Views.** A top view shows the rectangle and the hole as a circle with its center line. A front view shows the rectangle with the hole as two hidden lines running through it. A section view A-A cuts through the hole to show the bore clearly.
- **Dimensions.** 60, 40, and 20 on the outline. The hole diameter 10 is placed on the circle in the top view. The hole position is given as 30 from the left edge and 20 from the front edge, measured to the center line.
- **Check.** The hidden lines in the front view must match the circle in the top view. The hole width in the front view must equal 10 mm. The section cut must show the same hole.

If the hidden lines did not match the circle, the reader would see two different holes. The consistency between views is the check.

## Practice

1. Which projection symbol shows a third-angle drawing: the one with the object drawn beyond the plane, or the one with the plane between viewer and object? Answer in words.
2. A part has a hole that you cannot see in the front view. Which line type shows it? Answer with the line type name.
3. A block is 50 mm long. How many views are minimum to show a block with a hole through the top? Answer with a number.
4. A feature is 2 mm (0.08 in) across and hard to read at full size. What view do you add? Answer with the view name.

<details><summary>Answers</summary>

1. The one with the plane between viewer and object (third-angle).
2. Hidden line (dashed).
3. Two.
4. Detail view.

</details>

## Common mistakes

- Dimensioning the same feature in two views, which creates conflicting numbers when one is changed.
- Forgetting that hidden lines are needed for internal holes when no section is drawn.
- Mixing up first-angle and third-angle projection, which flips where the side view appears.
- Drawing a section without labeling the cutting plane, so the reader cannot tell where the cut was made.
- Making every line the same weight, so the drawing becomes hard to scan.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: a free hub that includes engineering graphics and design material.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) by Paul Dawkins: free algebra and geometry refreshers that support reading scaled views.
- ASME Y14.3 covers multiview and sectional view drawings. It is a paid standard, named here for reference only.
- [Design reference](reference.md): the lookup sheet for this topic.
