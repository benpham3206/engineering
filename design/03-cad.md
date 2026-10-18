# CAD (computer-aided design)

CAD is the software used to model parts, put them together into assemblies, and produce drawings. A good CAD model is a clear recipe: anyone can open it, change one dimension, and get a correct result. A bad model breaks the moment one thing moves.

**Prerequisites:** [01 Design process](01-design-process.md), [02 Engineering graphics](02-engineering-graphics.md)
**Time:** 6-10 h

## Core ideas

- **Parametric modeling** builds a shape from sketches and features, where each dimension is a parameter. Changing a parameter updates the whole model. Most mechanical CAD uses this approach.
- **Direct modeling** pushes and pulls faces without a history. It is fast for quick changes but harder to edit systematically.
- **Part.** One solid body made from a sequence of features. A part is what a machine shop makes or buys.
- **Assembly.** A collection of parts placed in their final relative positions. Mates (also called constraints) define how parts touch, slide, or rotate relative to each other.
- **Drawing.** A set of views, sections, and dimensions generated from a part or assembly. A drawing is what goes to the shop. Views in the drawing update when the model changes.
- **Feature tree.** The ordered list of features in a part. It shows what was made first, second, and so on.

## Sketches

A sketch is a flat profile drawn on a plane, then used to make a 3D feature. The habits below prevent most problems.

- **Fully define the sketch.** Every line should be fixed by dimensions or relations (horizontal, tangent, coincident). A sketch that can still move is called under-defined. Under-defined sketches change unexpectedly when parents change.
- **Use relations first, then dimensions.** Relations keep geometry in the right shape. Dimensions set the size.
- **Dimension the design intent.** If a hole must be 10 mm from an edge, dimension it from that edge, not from some arbitrary origin.
- **Do not over-define.** A sketch with conflicting constraints will refuse to solve. Remove the redundant one.

## Features

Common features build a part step by step:

- **Extrude** pulls a sketch straight out to a depth.
- **Revolve** spins a sketch around an axis. Good for shafts and round parts.
- **Hole** makes a drilled or tapped hole using standard sizes.
- **Fillet** rounds an edge. Fillets reduce stress concentration in many parts.
- **Chamfer** cuts an edge at an angle, which helps assembly and removes sharp edges.
- **Pattern** repeats a feature in a line or a circle. Use a pattern rather than copying by hand.

Order matters. Put the big shapes first and the small details later. Put patterns after the feature they repeat.

## Parameters and design intent

- Keep the driving dimensions in one place, such as a parameter table or a configuration file.
- Give features clear names, such as "mounting holes" rather than "Cut-Extrude7".
- Build from a reference: a datum plane or an origin that matches how the part mounts or locates.

## Assemblies

- Start with the part that does not move. This is the fixed or grounded part.
- Mate each new part to a known face, edge, or axis. Avoid mates to tiny features that may change.
- Use mates that match the real joint: a coincident face for a flat seat, a concentric mate for a shaft in a bore.
- Check interference. Two solid parts must not occupy the same space unless the joint is a press fit.
- Run a motion study or drag a part to see if it moves in the way the design expects.

## Drawings from CAD

- Generate views from the model rather than drawing them by hand. This keeps the drawing in step with the model.
- Use model dimensions where they make sense, and add drawing dimensions only for the features the shop must check.
- Put tolerance notes on the drawing. Tolerance is covered in [04 Tolerancing and stack-up](04-tolerancing-and-stack-up.md) and [05 GD&T symbols and frames](05-gdt-symbols-and-frames.md).
- Keep the title block current: part number, revision, material, and scale.

## Version control and file hygiene

- Save with a clear revision letter or number, and keep older versions.
- Keep an assembly and its parts in a folder that does not change names.
- Do not rely on the computer's auto-save as a backup.
- Export neutral formats, such as STEP, for sharing with other software. STEP keeps the geometry but not the design history.

## Checklist

- Is every sketch fully defined and free of conflicts?
- Are the main dimensions parametric and written in one place?
- Does the feature tree read in a logical order from big to small?
- Are patterns used instead of copied features?
- Does the assembly have a fixed part, and are the mates tied to real features?
- Do interference checks pass, and does motion match the design?
- Do the drawing views update from the model, and is the title block complete?

## Example

A bracket holds a motor. It is 60 mm (2.36 in) long, 40 mm wide, and 5 mm (0.20 in) thick, with four mounting holes on a 40 mm by 30 mm rectangle.

- **Sketch.** Draw the 60 by 40 mm rectangle with its lower-left corner at the origin. Add relations so the sides stay horizontal and vertical. Dimension the sides 60 and 40.
- **Extrude.** Extrude the sketch 5 mm. The bracket is now a solid block.
- **Holes.** Sketch four circles on the top face, centered on a 40 by 30 mm rectangle. Dimension each center from the origin edges. Cut them with a hole feature of diameter 5 mm.
- **Pattern.** Instead of drawing four circles by hand, you could sketch one hole and use a rectangular pattern. This keeps the spacing editable from one dimension.
- **Check.** Change the rectangle width from 40 mm to 45 mm. Holes dimensioned from the origin edge stay in place. Holes dimensioned from the far edge move with it. Either can be right, but the model must match the intent you chose, and the drawing must show it.

The example shows why parametric habits matter. A change should move only what it should move.

## Practice

1. A sketch line can still slide when you drag it. What is the sketch called? Answer in one or two words.
2. Which feature rounds a sharp edge to reduce stress concentration? Answer with the feature name.
3. Four holes are spaced 10 mm apart in a row. Should they be copied by hand or made with a pattern? Answer with one word.
4. Two parts overlap when placed in an assembly. What is the problem called? Answer with one word.

<details><summary>Answers</summary>

1. Under-defined.
2. Fillet.
3. Pattern.
4. Interference.

</details>

## Common mistakes

- Leaving sketches under-defined, so a small change in one feature moves the whole part.
- Dimensioning from arbitrary origins instead of from the feature that controls the joint.
- Building the model with copied features, so each one must be edited separately.
- Using a single large feature tree with no order, which makes errors hard to trace.
- Forgetting to check interference, so the first real fit happens on the shop floor.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering references that cover drawing and design practice.
- [MIT OpenCourseWare, 2.017J Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) by MIT: a free course where students design and model real machines in CAD.
- Your CAD vendor's free learning pages are useful. Check the license terms of any student or trial edition before relying on it.
