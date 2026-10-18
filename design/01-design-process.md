# Design process

**Type:** lesson

Design is the work of turning a need into something that works, can be built, and can be explained. Engineers use a repeatable process so that decisions are traceable and mistakes are caught early, when they are cheap to fix.

**Prerequisites:** none
**Time:** 3-5 h

## Core ideas

Engineering design is rarely a straight line. It is a loop: you learn something, change the design, and test again. The stages below are a common pattern. Real projects repeat them many times.

- **Need.** A customer, user, or problem that someone cares about. A need is stated in plain words, such as "a bicycle rack must hold two bikes on a standard car hitch."
- **Requirements.** Measurable statements that define what "works" means. A requirement is a test you can check. "Holds 30 kg (66 lb) without permanent bending" is a requirement. "Feels sturdy" is not, until it is measured.
- **Constraints.** Limits you cannot break, such as budget, size, power source, or legal rules. Constraints are different from requirements because they limit the design space rather than describe a goal.
- **Concepts.** Several different ways to meet the requirements. Good teams generate more than one idea before choosing. The first idea is usually not the best.
- **Selection.** A structured comparison of concepts against the requirements. A decision matrix is a common tool: list criteria, give each a weight, score each concept, and multiply.
- **Embodiment and detail design.** Turning the chosen concept into real geometry, materials, and dimensions. This is where [CAD](03-cad.md), drawings, and [tolerances](04-tolerancing-and-stack-up.md) come in.
- **Prototype and test.** Building something real, or a model of it, and measuring it against the requirements.
- **Iteration.** Using test results to change the design. Each loop should answer a specific question.

## Requirements, functions, and metrics

- A **function** says what the device does, in verbs and nouns: "hold load," "transfer torque," "stop motion."
- A **metric** is a number that tells you how well a function is performed. For a bracket, the metric might be deflection under load.
- A **target** is the value you aim for. A **limit** is the value you must not exceed. Keep them separate on a requirements list.

Write requirements so that a second engineer could test them without asking you what you meant.

## Trade studies

Most design decisions are trade-offs. Making a part stronger often makes it heavier or more expensive. A trade study makes the trade-off visible.

- Pick the criteria that matter most (cost, mass, strength, ease of assembly, reliability).
- Weight each criterion from 1 to 5, with 5 meaning very important.
- Score each concept from 1 to 5 on each criterion.
- Multiply weight times score and add the results for each concept.

The highest total is not always the right answer. If one concept fails a hard requirement, it is out no matter what its total is. Always check the pass or fail requirements first.

## Iteration and risk

Early in a project, changes are cheap. A sketch costs minutes. A cast part costs weeks. Designers try to find the biggest risks first, then test them. A risk is a thing that could fail badly and that you do not yet know how to handle.

- Ask, "What is the riskiest assumption in this design?"
- Build the smallest test that can prove or disprove it.
- Record what you learned, even when the test fails. A failed test is useful data.

## Design reviews

A design review is a planned meeting where the design is checked against the requirements before the next stage starts. Reviews are sometimes called gates. They stop a weak design from moving forward on momentum.

- Hold a review at the end of each major stage, such as after concepts, after detail design, and after the first prototype test.
- Bring the requirements list, the decisions made so far, and the test results.
- Ask a reviewer who was not on the design team to read the requirements before the meeting. Fresh eyes find gaps in the wording.
- Record each action item, its owner, and its due date. A review with no written actions is not useful.
- A review can end in one of three ways: proceed, proceed with actions, or return to an earlier stage.

Reviews work best when they focus on the requirements, not on personal choices. The question is always, "Does this meet the need?"

## Documentation

A design is only as good as its record. Keep these up to date:

- The requirement list and its version number.
- The reason each major decision was made.
- Test data with dates, equipment used, and the person who ran the test.
- Known open issues.

Future you will forget why a dimension is 14.3 mm. A short note saves hours later.

## Checklist

- Is the need written in one sentence?
- Does every requirement have a measurement and a pass value?
- Are constraints listed separately from requirements?
- Did you consider at least three concepts before choosing one?
- Did you use a trade study or a decision matrix to choose?
- Is the riskiest assumption named, with a test planned for it?
- Are the decisions and test results written down?

## Example

A team must design a clamp that holds a 20 mm (0.79 in) thick workpiece in a bench vise while a hole is drilled.

- **Need.** Hold the workpiece steady during drilling, so the hole is in the right place.
- **Requirements.** Clamping force of at least 300 N (67 lbf). Opens to at least 25 mm (1 in). Total mass under 0.5 kg (1.1 lb). Costs under US$15 in parts.
- **Concepts.** (1) A C-clamp from a purchased part. (2) A cam lever clamp. (3) A toggle clamp.
- **Trade study.** Weights: force 5, cost 3, mass 2, ease of use 4. The team scores each concept and finds the toggle clamp has the highest weighted total, but only if it meets the 25 mm opening. The toggle clamp opens to 22 mm, so it fails a hard requirement and is removed. The cam lever clamp is chosen.
- **Risk.** The lever might slip under vibration. The test plan is to drill 20 holes with the clamp and check the workpiece for movement.
- **Result.** The first prototype slipped. A rubber pad was added to the jaw, and the second test passed. Both test results are recorded.

The example shows the loop at work: a hard requirement removed a concept, a risk was identified early, and a test drove a change.

## Practice

1. Write one measurable requirement for a shelf that must hold books. Name the metric and the pass value.
2. A team has three concepts scored as follows, with weights 4 for cost and 2 for mass. Concept A has cost score 4 and mass score 3. Concept B has cost score 2 and mass score 5. Which has the higher weighted total?
3. A concept fails a hard requirement but has the highest total score. Should it be chosen? Yes or no.
4. Name the riskiest assumption in a design for a hand-powered coffee grinder.

<details><summary>Answers</summary>

1. Any measurable requirement with a metric and a pass value, for example "holds 15 kg (33 lb) with 2 mm (0.08 in) maximum sag."
2. Concept A: 4 x 4 + 2 x 3 = 22. Concept B: 4 x 2 + 2 x 5 = 18. Concept A is higher.
3. No.
4. Answers vary. A good answer names a specific uncertainty, such as grind consistency or handle strength.

</details>

## Common mistakes

- Writing vague requirements such as "strong" or "easy to use" and then not being able to test them.
- Choosing the first concept without comparing alternatives.
- Mixing up constraints and requirements, so a limit is treated as a goal.
- Adding up weighted scores without checking the hard requirements first.
- Changing the design without recording why, so the same mistake comes back later.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: a free hub of engineering textbooks, useful for design and mechanics background.
- [Beginner's Guide to Aeronautics](https://www.grc.nasa.gov/www/k-12/airplane/) by NASA Glenn Research Center: an accessible free guide that shows how engineers trade lift, weight, and power in real vehicles.
- The ASME Y14.5 standard and the ASME Y14 drawing series cover drawing rules. Those are paid standards, so read them through a library or employer.
