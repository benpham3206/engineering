# Fabrication drawings

**Type:** lesson

A **fabrication drawing** is the set of instructions a machine shop, sheet metal shop, or welding shop builds a part from. The goal is that the people in the shop never need to call the designer. An engineer cares because every unanswered question on a drawing becomes a phone call, a guess, or a wrong part.

**Prerequisites:** [02-engineering-drawings.md](02-engineering-drawings.md) (title block, views, line types), [../design/02-engineering-graphics.md](../design/02-engineering-graphics.md) (orthographic views and sections), [../design/05-gdt-symbols-and-frames.md](../design/05-gdt-symbols-and-frames.md) (datums and feature control frames), [../design/reference.md](../design/reference.md) (fastener and thread reference), and [Trigonometry](../math/02-trigonometry.md) (bend allowance angles)
**Time:** 6-10 h

## Core ideas

- **The reader is the fabricator.** The person reading the drawing is a machinist, a press brake operator, or a welder. They have the drawing, the material, and their tools. They do not have you, your sketches, or your memory of why the design is the way it is.
- **Build from the drawing alone.** A good test is to hand the drawing to someone who has never seen the part and ask them to quote and make it. Every question they ask is a gap on the drawing.
- **Say each thing once, in the right place.** Material goes in the title block or the notes, not scattered over the views. Each feature has one size and one location.
- **Read it in the shop's order.** A fabricator usually reads the title block first, then the material and stock size, then the general notes, then the views, then the dimensions and callouts. The drawing should work in that order.
- **Basic drawing rules still apply.** Views, line types, and title block rules are in [`02-engineering-drawings.md`](02-engineering-drawings.md). This lesson adds what the shop needs on top of them.

### Checklist: what every fabrication drawing needs

Put these on every drawing, even a simple one.

- **Material and stock size.** The alloy, temper or grade, and the size of the raw stock. For example, "6061-T6 aluminum plate, 6 mm thick, cut to $200 \times 120$ mm." A material with no standard code, such as "steel," is not enough.
- **Finish and coating.** What the surface should look like at the end. "As machined," "deburred," "anodize Type II, clear," or "no coating" are all valid. Leaving it blank forces a guess.
- **Heat treatment.** Say "none" if there is none. If a heat treatment is required, give the process and the hardness range. Purchased tempers such as T6 are already heat treated by the supplier.
- **General tolerance note.** The default tolerance for dimensions that have no tolerance of their own, for example "linear $\pm 0.1$ mm unless noted." Angles usually get their own default.
- **Units.** Stated once in the title block or notes. Most metric shops work in millimetres.
- **Scale.** Usually 1:1 for parts a shop builds. State it anyway, and use "NTS" if the views are not to scale.
- **Revision.** A letter or number that changes with every change to the part. The shop checks this before they cut.
- **Quantity.** How many to make, or "quantity per assembly" on a sub-part. Shops price and schedule from this.

Keep the title block and notes complete, but do not repeat the same fact in five places. One source per fact is easier to keep correct.

### Dimensioning for manufacture

Dimensioning for the shop asks a different question than dimensioning for the designer. The designer asks, "What size must this be for the function?" The machinist asks, "Where do I put the edge of the tool, and what do I measure to check it?"

- **Dimension from datums the machinist uses.** A **datum** is the face, edge, or bore that the part is held against in the vise, fixture, or brake. Dimension from those surfaces, not from a random edge. The datum structure should match the setup order. The GD&T meaning of datums is in [`05-gdt-symbols-and-frames.md`](../design/05-gdt-symbols-and-frames.md).
- **Mark functional dimensions.** A **functional dimension** controls fit, alignment, or function, such as a bore that takes a bearing. Give it a tight tolerance and make it easy to inspect. Dimensions that do not affect function can use the general tolerance.
- **Avoid closed chains.** A **closed chain** is a loop of dimensions that all meet at the same point, for example a row of holes with a total length and each spacing given. The shop cannot hold all of them, and the stack-up of the tolerances may not close. Leave one dimension in the chain off, or dimension every feature from the same datum.
- **Use reference dimensions carefully.** A **reference dimension** is marked "(REF)" and shows a size for information only. The shop does not cut to it. Use it for a total length that is the sum of other dimensions, so the reader can check the math, but never let the shop build to a reference value.
- Do not repeat a hole diameter in two views.

### Hole callouts and hole tables

Holes are the most common source of shop questions. A complete hole callout gives the type, the size, the depth if it is not through, and the thread if it is tapped.

- **Through hole.** A diameter with "THRU," for example "$\text{Ø}6.6$ THRU." The hole goes all the way through the part.
- **Blind hole.** A diameter and a depth, for example "$\text{Ø}5.0 \times 8$ DEEP." If the depth matters, state whether it is the drilled depth or the full depth including the point. Precise depth also requires the drill point angle.
- **Counterbore.** A pocket for a socket head screw head. Give the through diameter, the counterbore diameter, the counterbore depth, and the symbol that marks a counterbore. Check the fastener head size before you set the number.
- **Countersink.** A cone that lets a flat head screw sit flush. Give the through diameter, the countersink diameter at the surface, and the included angle. For most flat head screws the angle is 90 degrees, but check the fastener data.
- **Tapped hole.** A thread size, pitch, and class, for example "$\mathrm{M6} \times 1.0\text{-6H}$." Give the thread depth and the drilled depth separately, because the tap drill goes deeper than the thread. The metric thread designation and tolerance classes follow ISO 965. The **tap drill** is the hole diameter you drill before tapping.
- **Hole table.** When there are many holes, put them in a table. One row per hole type, with columns for the ID, the quantity, the feature and size, the depth, and the $x$ and $y$ position from the datums. Each hole gets a letter or number that matches a label on the view.

Rules of thumb for holes:

- Prefer standard drill and tap sizes. A shop will not stop for a special drill.
- Keep the thread depth at least about one and a half times the diameter in aluminum and similar soft materials. The reference sheet in [`../design/reference.md`](../design/reference.md) gives the same rule for fasteners.
- A through tapped hole in a thin plate gives little thread. Check the engagement before you release the drawing.

### General notes block

The notes block is the place for every instruction that the geometry cannot show. Keep it short, numbered, and specific.

- **Break sharp edges.** "Break all sharp edges" is the usual default. If the size matters, state it, for example "$0.5 \times 45$ degrees chamfer where noted."
- **Deburr.** Remove burrs from all machined and cut edges and holes.
- **Default surface finish.** Give one default, for example "Ra 3.2 um unless noted." Call out tighter finishes on the specific surface.
- **Default tolerances.** Linear, angular, and hole position defaults, in one place.
- **Material and treatment.** Repeated here in words if the title block is full.
- **Inspection and marking.** Part number or serial to be marked, or "no marking" if none.

Avoid notes that say "per standard" with no standard named. The reader then has to find it. Name the standard, for example ASME Y14.5 for geometric tolerancing or ASME Y14.100 for engineering drawing practice, and link to the revision if you can.

### Part drawings and assembly drawings

- **Part drawing.** Shows one part with all its features, dimensions, and notes. The shop makes that part from this drawing. Each part has its own drawing number.
- **Assembly drawing.** Shows several parts together and how they fit. It does not repeat every dimension of every part. It shows the assembly sequence where it matters, the fasteners, and the torque or fit notes.
- **Balloons.** Numbered circles on an assembly drawing that point to each part. Each balloon number matches one row in the bill of materials.
- **Bill of materials (BOM).** A table with one row per part. Common columns are item number, part number, description, material, and quantity per assembly. The BOM is what purchasing and the stockroom use.

Pick the right drawing set. A shop that receives only an assembly drawing has to guess at the dimensions of each part. A shop that receives only part drawings has to guess how they fit together.

### Sheet metal drawings

Sheet metal parts are cut flat and then bent. The drawing has to describe both the flat shape and the bends.

- **Flat pattern.** The unfolded shape of the part, with the bend lines drawn on it. The laser or punch cuts this shape. It includes a dimension for each flange and the overall flat size.
- **Bend lines.** Each bend is shown as a labeled line on the flat pattern. The label usually gives the bend angle.
- **Bend direction.** State whether each bend goes up or down, measured from a view you name. A bend that goes the wrong way ruins the part.
- **Bend radius.** The inside radius of the bend. A common default is a radius equal to the material thickness, but the shop's tooling decides what is practical. State the radius on the drawing.
- **K-factor.** The K-factor locates the **neutral axis**, the layer in the sheet that does not stretch or compress during a bend. It is a ratio between 0 and 0.5 that depends on the material, the radius, and the tooling. Put the K-factor or the bend allowance table on the drawing, or state that the shop's own table governs.
- **Hole-to-bend and edge-to-bend spacing.** Holes and slots near a bend move when the part is bent. Give the minimum distance the shop expects, or ask the shop for its rule before you dimension close to a bend.

#### Bend allowance formula

**Bend allowance** is the length of the neutral axis through the bend. It is used to build the flat pattern.

$$
\mathrm{BA} = \theta\,(R + K\,T)
$$

where $\mathrm{BA}$ is the bend allowance (mm), $\theta$ is the bend angle in radians, $R$ is the inside bend radius (mm), $K$ is the K-factor (no units, between 0 and 0.5), and $T$ is the material thickness (mm). Typical K-factor values run from about 0.33 to 0.5, but the shop's tooling and material decide the right value.

Worked check of the form: a 90 degree bend with $R = 2.0$ mm, $K = 0.40$, and $T = 1.5$ mm has $\theta = \pi/2$, so $\mathrm{BA} = 4.08$ mm.

### Weldment drawings

A **weldment** is a welded assembly built from cut and formed pieces. The drawing shows the pieces, the joints, and the welds.

- **Cut list.** A table of every piece to be cut, with its length, quantity, material, and any angle or end cut. The cutting shop uses it directly.
- **Weld symbols.** Welds are shown with a standard symbol on a reference line, not drawn as a picture. The full symbol set is in AWS A2.4. In words, the common parts of a weld symbol are these:
  - An arrow at one end of the reference line points to the joint.
  - A weld symbol below the reference line means the weld is on the arrow side of the joint. A symbol above the line means it is on the other side.
  - A fillet weld symbol is a small right triangle. The weld size, usually the leg length, goes on the left of the symbol. Length and spacing for intermittent welds go on the right.
  - A circle at the junction of the arrow and the reference line means "weld all around": the weld goes around the whole joint. A flag at that junction means a field weld, made at the install site instead of in the shop.
- **Welding notes.** The welding process, filler material, and any inspection requirement. Say which welds need inspection and what kind.
- **Distortion and sequence.** The drawing states what the weld must achieve. The shop decides the sequence and the fixture unless the design needs a specific order.

Read each weld symbol from the reference line outward, one joint at a time. Confirm the arrow side and the other side for every joint before you start.

### Machined part checklist

Read the drawing as the machinist. Before you release a machined part, check these points.

- Can the part be held? Is there a flat, accessible datum face for the vise or fixture?
- How many setups does the part need? Each setup from a new side adds time and error. Group features by setup.
- Can the cutting tools reach each feature? Deep, narrow pockets need long, thin tools, which chatter and deflect.
- Do internal corners have a radius? A square internal corner needs a tool that does not exist in normal sizes. Give a radius at least as large as a standard end mill.
- Are holes drillable? Blind holes need clearance at the bottom for the drill point. Through holes are easier to clear.
- Are tapped holes given a tap drill size and a depth?
- Are the tolerances tighter only where the function needs them? Every tight tolerance adds inspection and scrap risk.
- Is the surface finish specified only where it matters?
- Are the thin walls and thin webs thick enough to hold through machining and clamping?

### Revision control and engineering change notes

A drawing is a controlled document. The shop must build the current revision and nothing else.

- **Revision letter.** Increase the letter with every released change. Do not reuse letters. Use a revision block on the drawing that lists each change, its date, and who approved it.
- **Engineering change notice (ECN).** A short record of what changed, why, and what the change affects. It names the parts, the assemblies, and any stock or tooling that must be used up, reworked, or scrapped.
- **Effectivity.** State from which serial number, date, or lot the change applies. A part in process when the change is released may need a decision.
- **Superseded drawings.** Mark the old revision as superseded and keep it on file. Do not delete it, because the old parts are still in the field.

## Key equations

Tap drill and thread minor diameter, for metric threads. The bend allowance formula is in the sheet metal section above.

For a metric coarse thread with nominal diameter $D$ and pitch $P$, the internal minor diameter is

$$
D_1 = D - 1.082532\,P
$$

where $D$ and $P$ are in millimetres. The tap drill for a common metric coarse thread is close to the minor diameter. The shortcut $D - P$ gives the usual drill size for many sizes, for example 5.0 mm for $\mathrm{M6} \times 1.0$. Always check a tap drill chart for the exact drill, because the chart value sets the thread percentage the shop gets.

## Worked example: aluminum mounting plate

**Task.** Write the complete fabrication drawing content for a simple mounting plate. The plate is 200 mm long, 120 mm wide, and 6 mm thick, made of 6061-T6 aluminum. It has four M6 tapped holes near the corners and one 20 mm H7 bore at the center. List every callout and note the drawing needs, and compute the numbers the shop uses.

**Given.**

- Plate: $200\ \mathrm{mm} \times 120\ \mathrm{mm} \times 6\ \mathrm{mm}$, 6061-T6 aluminum.
- Four $\mathrm{M6} \times 1.0$ tapped holes, one near each corner.
- One 20 mm H7 through bore at the center.
- Quantity: 10 pieces.

**Assumptions.**

- Datum A is the left edge, datum B is the bottom edge. Datum A-B sets the origin.
- Corner holes are 15 mm from both adjacent edges. This is a design choice, made here for the example.
- Bore center is at the middle of the plate.
- Density of 6061 aluminum is about 2.70 g/cm$^3$ (typical value).

**Solution.**

Hole layout, measured from datum A and datum B to hole centers:

| ID | Feature | $x$ (mm) | $y$ (mm) |
|---|---|---|---|
| H1 | $\mathrm{M6} \times 1.0$ tapped | 15 | 15 |
| H2 | $\mathrm{M6} \times 1.0$ tapped | 185 | 15 |
| H3 | $\mathrm{M6} \times 1.0$ tapped | 15 | 105 |
| H4 | $\mathrm{M6} \times 1.0$ tapped | 185 | 105 |
| H5 | 20 H7 bore | 100 | 60 |

Calculated values:

- Tap drill: $D - P = 6.0 - 1.0 = 5.0$ mm.
- Minor diameter of the internal thread: $D_1 = 6.0 - 1.082532 \times 1.0 = 4.917$ mm.
- Bore limits for 20 H7 (ISO hole tolerance, typical values for this size range): $20.000$ mm to $20.021$ mm.
- Smallest edge distance for any hole: 15 mm.
- Nearest hole to the bore center: 96.2 mm.
- Hole spacing: 170 mm in $x$ and 90 mm in $y$. The corner-to-corner diagonal is 192.4 mm.
- Net plate volume after holes: $144\,000 - 1885 - 471 = 141\,644$ mm$^3$.
- Mass: $141\,644 \times 2.70 \times 10^{-3} = 382$ g (about 0.38 kg).

**Drawing content.**

Title block:

- Part name: "Plate, mounting." Part number: placeholder such as PL-0001.
- Material: 6061-T6 aluminum. Stock: 6 mm plate, cut to $200 \times 120$ mm.
- Units: millimetres. Scale: 1:1. Projection: third-angle symbol.
- Revision: A. Quantity: 10 pieces.
- Sheet: 1 of 1.

Views:

- Front view showing the plate outline, the four tapped holes as hidden or through symbols with center lines, and the bore with its center lines.
- Top view showing the outline and the hole positions dimensioned from datums A and B.
- Datum symbols A on the left edge and B on the bottom edge.

Hole table (copied from the layout above):

- H1 to H4: $\mathrm{M6} \times 1.0\text{-6H}$, THRU, tap drill 5.0 mm through, positions as above.
- H5: 20 H7 bore, THRU, $20.000\ {}^{+0.021}_{0}$, position as above, surface finish Ra 1.6 um on the bore.

General notes:

1. Material: 6061-T6 aluminum plate. Supplier temper T6. No heat treatment after machining.
2. Finish: as machined, unless noted. No coating unless stated.
3. Break all sharp edges, $0.5\ \mathrm{mm} \times 45$ degrees max.
4. Deburr all holes and edges.
5. Default tolerances: linear $\pm 0.1$ mm, angles $\pm 0.5$ degrees, unless noted.
6. Default surface finish: Ra 3.2 um unless noted.
7. Hole positions are to datum A and datum B, $\pm 0.1$ mm.
8. Thread engagement: see the note below and the designer decision.

**Sanity check.** Walk the reader through the drawing as a machinist. Hold the plate against datum A and datum B. Can every hole be found from those two edges? Is there a tap drill for each hole? Is the bore size readable? Can the reader make the part without asking a question?

> [!WARNING]
> **Problem found by the check.** The M6 holes go through a 6 mm plate. Aluminum needs about 1.5 times the diameter in thread engagement, which is 9 mm. A 6 mm through thread gives only 1.0 times the diameter, so the threads may strip under load. The drawing must not release as is. The designer must choose one of three fixes and write it down: thicken the plate to 9 mm or more, add a thread insert, or accept the lower engagement with a stated load limit.

## Practice

Each item is a review exercise. Read the drawing or description, find what a fabricator would need to ask, and write the fix.

1. **Title block and notes.** A drawing shows a 150 mm long steel bar with four holes. The title block says "Steel bar, scale 1:1, rev A" and nothing else. List every missing item from the fabrication checklist, and give a sample entry for each.
2. **Hole callouts.** A hole is labeled "M8" with a depth of "10" and no other text. Rewrite it as a full callout. Compute the tap drill size using the minor diameter for $\mathrm{M8} \times 1.25$ and state the value to two decimals.
3. **Sheet metal bend.** A bracket is 1.5 mm thick with three 90 degree bends. The inside radius is 2.0 mm, and the K-factor is 0.40. Compute the bend allowance for one bend to two decimals, then list what the drawing must show beyond the flat size.
4. **Dimension review.** A plate has holes at 25, 75, and 150 mm from the left edge, with an overall length of 175 mm. Check whether every hole is located, and whether any dimension is missing or redundant. Say what, if anything, to change.

<details><summary>What a good answer includes</summary>

1. Material code, stock size, finish, heat treatment, general tolerance note, units, projection symbol, revision entry, quantity. Each entry is specific, for example "Steel, mild, $150 \times 25 \times 6$ mm bar, as cut, no heat treatment, $\pm 0.1$ mm default."
2. A full callout such as "$\mathrm{M8} \times 1.25\text{-6H}$, tap drill 6.75 mm, depth 10 mm thread and drill depth stated separately." The minor diameter for $\mathrm{M8} \times 1.25$ is 6.65 mm, and the answer must reach that number and say which drill is used.
3. Bend allowance of 4.08 mm for one 90 degree bend. The drawing must show the flat size, bend lines, bend direction, inside radius, K-factor or the shop's table, and any hole-to-bend spacing.
4. The three dimensions 25, 75, and 150 are measured from the same datum. Every hole is located by its own dimension from that datum, so there is no missing dimension and no closed chain. The gap from the last hole to the right edge ($175 - 150 = 25$ mm) is derived. Do not add a right-edge dimension for that last hole as well, because it would be redundant; if the shop needs it, show it as a reference dimension in parentheses.

</details>

## Common mistakes

- Leaving out the stock material size, so the shop orders the wrong raw material.
- Dimensioning from edges that the machinist cannot use to set up the part.
- Putting a closed chain of dimensions on a row of holes, so the tolerances cannot all be met.
- Writing a tapped hole with a thread size but no depth, or with a depth but no tap drill.
- Releasing a drawing with no revision change record after a change was made to the geometry.

## Go deeper

- [MIT OpenCourseWare](https://ocw.mit.edu/) by MIT, free course materials. Search the site for machining, manufacturing, or mechanical design courses.
- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project, a free engineering library. Browse the bookshelves for manufacturing and drawing texts.
- [Engineering drawings](02-engineering-drawings.md) in this folder, covering the title block, views, and line types that every fabrication drawing uses.
- Standards named for reference only, and paid: ASME Y14.5 (geometric dimensioning and tolerancing), ASME Y14.100 (engineering drawing practices), ISO 128 (technical drawings, general principles), and AWS A2.4 (welding symbols). Look them up through a library or your employer.
