# Working out the design intent

**Type:** lesson

Design intent is the reason an engineer made each choice: why this material, why this wall thickness, why this hole is here and not there. Measuring and modeling tell you what a part is. Design intent tells you why it is that way, and that is what you need to change it, repair it, or design something better.
**Prerequisites:** [Teardowns](01-teardowns.md), [Measuring existing parts](02-measuring-existing-parts.md), [Recreating parts in CAD](03-recreating-parts-in-cad.md)
**Time:** 4-8 h

## Core ideas

- Every feature answers a question. The question might be about function (what does it do?), cost (why this process?), safety (what does it protect against?), or assembly (how does it get put together?).
- Look for the **load path**: the route a force takes from where it is applied to where it is held. Parts on the load path are usually thicker, stiffer, or better supported. Parts off the load path are often thinner or cheaper.
- Look for the **user path**: the way a person uses the product. Surfaces a hand touches, levers a finger presses, and places a user looks at all show the intent behind the layout.
- Look for **assembly logic**: parts that snap in from one direction, screws placed where a tool can reach, and features that set the position of another part. Assembly logic often explains odd-looking shapes.
- Look for **cost logic**: fewer parts, simpler tooling, and one process for many features. A molded clip that replaces a screw is a cost decision.
- Look for **failure logic**: where the product is designed to break first. A shear pin, a thin hinge, or a breakaway tab is a deliberate weak point.
- Read the design in the order a designer would have. Start with the requirement (what must the product do?), then the concept (what general approach?), then the detail (what exact size?).
- Write down each guess about intent with the evidence for it. A guess without evidence is a hypothesis, and you should label it as one.

### Design intent checklist

- [ ] What problem does the product solve, and what must it do well?
- [ ] Which forces act on the part, and where do they go?
- [ ] What does a user touch, press, or look at?
- [ ] Which features exist only to hold another part in place?
- [ ] Which parts look over-built, and what might they be protecting against?
- [ ] Which features look like cost-cutting, and what do they save?
- [ ] Where is the designed weak point, if there is one?
- [ ] For each guess, what observation supports it?

## Checklist for an intent note

Write one note per feature you care about. Use this layout.

```
Feature:
Where it is:
What it appears to do:
Evidence (photo, measurement, test):
Alternative explanation:
Confidence (low / medium / high):
```

## Example

A desktop stapler has a flat base, a spring-loaded body, a hinged top, and a small metal anvil under the staple path. The goal is to explain why the base is heavy and why the anvil is made of a separate part.

1. **Function:** The stapler must drive a staple through several sheets of paper with a single press. The force on the top arm is high, and the base takes the reaction.
2. **Load path:** The force goes from the hand, through the top arm and hinge, through the staple driver, and into the anvil, then into the base. The base takes the full reaction, so it needs mass and stiffness.
3. **Intent for the heavy base:** The base is heavy on purpose. A light base would lift off the desk during the press. Evidence: the base has a rubber pad on the underside, and the mass is roughly 400 g. Confidence: high.
4. **Intent for the separate anvil:** The anvil is a hardened steel part, not molded plastic. The staple bends against it, and plastic would wear down quickly. Evidence: the anvil is a different color and has a bright, ground face where the staples bend. Confidence: medium, because the material test was not run.
5. **Intent for the hinge:** The top arm pivots on a pin in two molded bosses. The bosses are thick, so the pin does not pull out under repeated presses. Alternative explanation: the bosses might be there only for assembly. Confidence: medium.
6. **Result:** The design intent is a rigid base for reaction force, a hardened anvil for wear, and a hinge sized for repeated loads. A redesign that made the base lighter would need a stronger anchor, such as a rubber pad with more grip.

## Practice

1. A product has 3 features on the load path and 5 off it. How many features are on the load path?
2. A part has 4 snap-fit clips and 2 screws. How many of the fasteners are clips?
3. A stapler base weighs 400 g and a designer doubles its mass to stop it lifting. What is the new mass in grams?
4. A product has 12 parts, and a redesign that replaces 3 screws with 1 snap-fit feature removes 3 parts. How many parts are left?
5. You have 7 feature notes, and 4 of them are rated high confidence. How many are not rated high?

<details><summary>Answers</summary>

1. 3
2. 4
3. 800
4. 9
5. 3

</details>

## Common mistakes

- Treating every feature as deliberate. Some features are leftovers from an older design or a tooling choice, so test each guess.
- Judging intent from one photo. Look at the part from several angles and check the wear pattern.
- Writing "for strength" without saying which load it resists. Name the force and the direction.
- Ignoring the user path. Many odd shapes exist only to fit a hand or to guide a finger.
- Forgetting to write down alternative explanations. A guess with no rival is usually overconfident.

## Go deeper

- [Design and manufacturing topics in Mechanical Engineering](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering) by LibreTexts: free books that cover design and machine elements.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: a free library to browse for statics and load paths.
- [e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) by NIST and SEMATECH: free reference on evidence and variation, useful when you weigh how strong a clue is.
- See also the [design folder](../design/README.md) for how designers make these choices on purpose.
