# Principles that last

**Type:** philosophy

Principles that last are the laws of physics and the habits of good engineers that stay true across decades and generations. Engineers return to them because tools and materials keep changing while these do not.

Tools change every few years. Materials change every few decades. These principles held for the people who built aqueducts, and they hold for the people building rockets now.

**Prerequisites:** none. Read this first, and read it again every few years.

## The laws do not negotiate

- **Energy is conserved.** No design, however clever, creates energy. If your answer does, your answer is wrong.
- **Mass is conserved** in every machine you will ever build. Count what goes in and what comes out.
- **Entropy increases.** Every real process loses something. Perfect efficiency, perpetual motion, and free lunches do not exist.
- **Forces come in pairs.** Whatever pushes on your structure, your structure pushes back. Every load has a path to the ground, or to the reaction mass.
- **Nature does not read your drawings.** The part does what physics says, not what the model says. When they disagree, the model is wrong.

## Know what you know

- **Every number has a unit and an uncertainty.** A number without a unit is not a measurement. A measurement without an uncertainty is a guess dressed up.
- **Every model has assumptions, and every assumption has a limit.** Write down where your equations stop being true. Most failures happen just past that line.
- **Estimate before you calculate.** If you cannot guess the answer within a factor of ten, you do not understand the problem yet.
- **Check the answer a second way.** A hand calculation against a simulation. A test against a prediction. Two independent paths that agree are worth more than one precise path.
- **Test what you fly.** Analysis says a design should work. Only a test says it does.

## Design for the real world

- **Simple beats clever.** Every part you remove can never fail, never wear, and never cost anything.
- **Margins exist because you are uncertain.** A factor of safety is a measure of what you do not know about loads, materials, and use. Do not spend it on convenience.
- **Design for how it will fail.** Everything fails eventually. Good designs fail slowly, visibly, and safely, and give warning first.
- **Design for the people who build, use, and fix it.** A design that cannot be made, inspected, or repaired is not finished.
- **Changes need the same rigor as the original.** Many famous failures were not in the original design but in a small change that nobody re-analyzed.

## Be honest

- **Report what happened, not what you hoped.** Bad data you tell people about is useful. Data you invent, however good it looks, causes a failure later.
- **Say "I don't know" early.** It is cheap at the start of a project and very expensive at the end.
- **Safety outranks schedule, cost, and pride.** If you believe something is unsafe, say so in writing, and do not sign work you believe is unsafe.
- **Write it down so someone else can check it.** Work that cannot be reviewed cannot be trusted, including your own work six months later.

## Keep your work alive

- **Use open, plain formats.** Plain text, SI units, open file standards. The work should outlive the software that made it.
- **Explain why, not just what.** Future engineers can recompute a number. They cannot recover the reasoning unless you leave it.
- **Learn the principle, not the button.** Every tool in this repo will be replaced. The physics behind it will not.

## Checklist

Before you release a design, a calculation, or a report, ask:

- [ ] Does it conserve energy and mass?
- [ ] Are all units consistent, and are the uncertainties stated?
- [ ] Have I written down every assumption, and checked that the design stays inside them?
- [ ] Did I check the key result a second, independent way?
- [ ] Have I tested it, or said clearly that it is untested?
- [ ] How does it fail, and is that failure safe?
- [ ] Could someone else follow and check my work from what I wrote?

## Example

In 1999, the Mars Climate Orbiter was lost because one team's software produced thruster impulse in pound-force seconds while the navigation software expected newton seconds. The physics was right. The engineers were capable. A unit was missing from an interface, and nobody checked the number a second way. Nearly every principle on this page would have caught it: units on every number, an independent check, and honest reporting of the small trajectory discrepancies that appeared before the loss.

## Practice

1. Pick a product you use every day. Find one place where its designers chose simple over clever, and one where they did not.
2. Take a calculation you did recently. Write down every assumption it makes and where each one breaks.
3. Find a documented engineering failure. Which principle on this page, applied earlier, would have prevented it?

<details><summary>What a good answer includes</summary>

1. A specific part or feature, and what it would cost (in parts, failure modes, or repair) to make it more complex.
2. At least three assumptions, each with a condition under which it stops being true (for example "small deflection: fails above a few percent of the span").
3. A specific principle tied to a specific decision in the failure, not a general lesson like "be careful".

</details>

## Common mistakes

- Treating these as slogans instead of checks. Each principle should change a decision you make.
- Believing a simulation because it looks precise. Precision is not accuracy.
- Thinking principles slow you down. They are faster than redoing the work.

## Go deeper

- [Failure cases and decision frameworks](reference.md): the failures behind these principles, in one table.
- [Safety and risk](03-safety-and-risk.md) and [Ethics and professional responsibility](04-ethics-and-professional-responsibility.md) in this folder.
- [Report of the Presidential Commission on the Space Shuttle Challenger Accident](https://www.nasa.gov/history/rogersrep/genindex.htm) by NASA, Volume 1: the official findings. Richard Feynman's appendix on reliability ends with one of the most quoted lines in engineering, about reality taking precedence over public relations.
