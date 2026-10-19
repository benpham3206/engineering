# Design for manufacturing and assembly

**Type:** lesson

Design for manufacturing and assembly (DFMA) is the practice of shaping a part so it can be produced and assembled with the least cost and risk. Engineers need it because a design that works on paper can still be expensive, slow, or error-prone to make and put together. The main rules are simple: fewer parts, parts that are easy to locate and fasten, and features that match the process that will make them.

**Prerequisites:** [CAD (computer-aided design)](03-cad.md), [Tolerancing and stack-up](04-tolerancing-and-stack-up.md), [Machining processes](../manufacturing/03-machining-processes.md), [Casting, forming, and molding](../manufacturing/05-casting-forming-molding.md)
**Time:** 6-10 h

## Core ideas

- **Design for manufacturing (DFM)** asks whether a part can be made by the chosen process at a reasonable cost and tolerance. The shape must fit the process, such as casting, machining, sheet metal, or injection molding.
- **Design for assembly (DFA)** asks how many steps it takes to put the product together, and whether each step is easy and hard to get wrong.
- **Part count.** Every extra part adds cost, stock, handling, and a place for error. Combining parts is often the biggest saving.
- **Self-locating features** such as pins, slots, and chamfers guide a part into place without measurement. A chamfer on a hole entrance is a cheap way to make assembly easier.
- **Access.** A tool or hand must reach each fastener. A fastener that cannot be reached is a design error, even if it looks fine in CAD.
- **Process fit.** A feature that is easy in one process can be impossible in another. A sharp inside corner in a milled pocket is impossible, because the round cutter leaves a radius, and a cast or molded part also needs a radius. A deep thin hole is hard to drill.
- **Standard parts.** Use standard sizes for fasteners, bearings, and stock. A custom part costs more to buy and to check.

## Rules of thumb

These rules are a starting point. Confirm them with the process owner, since shops differ.

- Reduce the number of parts. Ask for each part, "Could this be part of another?"
- Use one direction of assembly where possible. Parts that go in from the top are easier than parts that need flipping.
- Add lead-in chamfers to pins and holes that must mate blindly.
- Keep wall thickness even in cast and molded parts, so the material cools and fills evenly.
- Give machined parts generous inside radii that match standard tool sizes.
- Make holes and threads a standard size where the process allows.
- Avoid features that need special tooling or a second setup when a simpler option works.
- Tolerance only what the function needs. Loose tolerances on non-critical features cut cost. Tight tolerances on critical features should be checked with [GD&T](05-gdt-symbols-and-frames.md).

## Choosing a process

The process sets the rules for the shape. A few common choices and their usual limits:

- **Machining** (milling, turning, drilling) makes precise features from solid stock. It is slow per part, and internal shapes and undercuts are hard. Good for low volumes and tight tolerances.
- **Casting** pours liquid metal into a mold. It makes complex shapes in one piece, but walls must be thick enough to fill, drafts are needed to remove the part, and surfaces are rougher than machined ones.
- **Sheet metal** bends and cuts flat stock. It is cheap for thin parts. Bends that are too tight for the material crack, and holes placed too close to a bend will distort. Check the shop's minimum bend radius.
- **Injection molding** forces plastic into a steel mold. It is cheap per part at high volume and expensive to set up. Walls must be even, and ribs are used instead of thick sections.
- **Additive manufacturing** builds parts layer by layer. It suits one-off and complex shapes, but strength can depend on build direction, and surface finish varies.

Decide the process early. A part designed for one process is often expensive in another, and changing late means redrawing the part.

## Assembly thinking

When you plan an assembly, picture the build in order.

1. Start with the base part, which is usually the largest and most stable.
2. Add each part in a direction that the hands or a robot can reach.
3. Check that each part locates itself before it is fastened.
4. Count the fasteners, and ask whether any can be replaced by a snap fit or a press fit.
5. Check the last step. If the last part cannot be reached, the design fails.

A useful test is to build a rough mockup, even from cardboard or foam, and time the assembly. The time reveals problems that a drawing hides.

## Checklist

- Has every part been asked whether it can be combined with another?
- Do features that guide assembly (chamfers, pins, slots) exist where needed?
- Can every fastener be reached by the tool that will tighten it?
- Is the part made by a process that suits its shape?
- Are standard sizes used for holes, threads, fasteners, and stock?
- Are tolerances tight only on the features that need them?
- Has the assembly sequence been walked through, step by step?

## Example

A small pump housing has a cover held in place with three screws. The base has four screws, two brackets, and a gasket. In total it has 12 parts: a base plate, a cover, two brackets, a gasket, and seven screws. The team redesigns it to reduce assembly work.

- **Combine parts.** The two brackets are cast into the base plate. This removes two parts, so the count falls from 12 to 10.
- **Replace fasteners with a snap fit.** The cover is held by snap tabs instead of its three screws. This removes three parts and their tapping and tightening steps, so the count falls to 7.
- **Add locating features.** A pin cast into the base lines up the cover, so the cover no longer needs measurement to be placed.
- **Keep access.** The four remaining screws are on the top face, so an electric driver can reach each one from one direction.
- **Result.** The part count falls from 12 to 7. The screw count falls from 7 to 4, a reduction of 42.9 percent. The assembly sequence has one direction, from top to bottom.

The team does not check the savings on cost alone. They also check that the snap tabs still meet the force needed to hold the cover against vibration, and that the cast base meets the wall-thickness rule. A saving that fails the function is not a saving.

## Practice

1. A product went from 12 parts to 7. What is the percentage reduction in part count, to one decimal place?
2. A through hole is 3 mm in diameter and 6 mm deep. Find the depth-to-diameter ratio as a number.
3. A design goes from 7 screws to 4 screws. What is the percentage reduction in screws, to one decimal place?

<details><summary>Answers</summary>

1. 41.7
2. 2.0
3. 42.9

</details>

## Common mistakes

- Optimizing one part's cost and ignoring the cost of assembly.
- Designing a part that cannot be made by the chosen process, such as a sharp inside corner in a molded part.
- Leaving out a tool path or hand reach, so the last fastener cannot be tightened.
- Choosing custom sizes for fasteners and holes when standard sizes would work.
- Tolerancing everything tightly, which raises cost without improving function.

## Go deeper

- [MIT OpenCourseWare, 2.017J Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) by MIT: a free course where design and build decisions are tested in real hardware.
- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering textbooks with design and manufacturing background.
- Published DFA guidelines from manufacturers and universities are useful, but check that each source is free and reliable before relying on it.
- [Design reference](reference.md): the lookup sheet for this topic.
