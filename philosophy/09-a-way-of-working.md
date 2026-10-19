# A way of working

**Type:** philosophy

A way of working is a consistent approach to carrying a problem from its start to a finished answer. Engineers need one because early decisions shape every step that follows.

This is one way, and it is not the only way. Think of a project like a factory-building game: every early decision about layout, flow, and connections shapes everything built after it. A belt placed badly at the start has to be torn out later, along with everything that depends on it.

**Prerequisites:** [Principles that last](07-principles-that-last.md) and [The engineering method](08-the-engineering-method.md).

## The mindset

- **Be curious.** There is always something new to learn or rediscover, in every project and every field.
- **Think bigger than the brief.** Whatever the vision is, plan for a larger one. What ultimately matters is that the problem is solved and that the person who uses the result finds it works and is a pleasure to use.
- **Build a mental model of the whole system** before you change any part of it: what it does, how energy and material and information flow through it, and what depends on what.
- **Understand the intent.** Ask who, what, when, where, why, and how before starting the task.
- **Understand the fundamentals and the dependencies.** A design that works for reasons you cannot explain will fail for reasons you cannot predict.
- **Take pride in the small details.** A chamfer on an edge, a clear label on a drawing, and a well-named variable are what separate work that is finished from work that is done.
- **Experiment and combine fields.** Many of the best solutions come from borrowing an idea from another field: biology, music, games, or another branch of engineering.

## Before you build

- **Sketch the form first.** Wireframes, layout sketches, a consistent set of design motifs, and a color palette or finish scheme settle the shape of a thing before effort goes into details.
- **Define success, constraints, and failure conditions before building.** Check the result against all three before you call it done.
- **Test assumptions early and cheaply.** Prefer reversible experiments before irreversible decisions. A cardboard mockup costs less than a machined part.
- **Design interfaces and boundaries explicitly.** Each component should have clear inputs, outputs, guarantees, and ways it can fail.
- **Prefer the simplest system that meets the requirements.** Complexity must earn its place.
- **Integrate vertically.** Understand the architecture, the system, and its dependencies as one whole, from the raw material to the user.

## While you work

- **Automate repetitive work**, once you understand it and it has stopped changing.
- **Build tools and logs to measure against reality** before assuming. A data logger on a test rig beats an argument about what the rig is doing.
- **Organize tools by how often you use them.** The tools you reach for daily belong closest at hand.
- **Document inspiration, decisions, changes, fixes, and new insights**, so anyone can pick up the work with full context.
- **Explain the quirks.** Leave a note wherever something works in a way a newcomer would not expect. Work should be understandable on the first read, with no outside context.
- **Give context before instructions.** A document should tell the reader what something is and why it matters before asking them to use it.
- **Build for the next person,** including yourself in a year.
- **Shorten the feedback loop.** The less time between making a change and learning whether it worked, the faster everything improves.

## When things go wrong

- **Anticipate bad actors, edge cases, and worst-case scenarios.** Ask how someone could misuse it, what happens at the limits, and what the worst outcome is.
- **Plan workarounds in proportion to how irreversible they are.** A temporary fix that is easy to undo can be quick. One that is hard to undo needs the same care as the real design.
- **Make failures observable, recoverable, and safe by default.**
- **Deliver urgent warnings immediately, with a fallback.** An alarm that nobody hears is not an alarm.
- **Find the root cause of every failure.** Fix the cause, not just the symptom.

## Keeping it healthy

- **Keep facts, assumptions, estimates, and decisions separate.** Never let one quietly become another. Label which is which.
- **Preserve traceability** from intent to requirement to decision to implementation to verification.
- **Periodically delete, consolidate, and simplify.** Tools, processes, and automations become liabilities when they stop paying for themselves.

## Deciding

A good decision maximizes:

$$\text{decision quality} = \text{expected value} + \text{information gained} - \text{downside risk} - \text{irreversibility cost}$$

In practice:

| Situation | Action |
|---|---|
| Low cost, reversible | Move quickly. |
| Expensive, irreversible | Investigate deeply first. |
| High uncertainty, cheap experiment available | Run the experiment. |
| High uncertainty, irreversible consequence | Do not guess. Reduce the uncertainty first. |
| Strong evidence, reversible | Execute. |

## Checklist

- [ ] Do I understand the intent, and could I answer who, what, when, where, why, and how?
- [ ] Have I defined success, constraints, and failure conditions?
- [ ] Have I tested the riskiest assumption in the cheapest way available?
- [ ] Are facts, assumptions, estimates, and decisions labeled as such?
- [ ] Is every interface defined, including how it fails?
- [ ] Have I recorded the decisions and the reasons for them?
- [ ] Could the next person pick this up without asking me anything?

## Example

**Designing a bike rack for a building lobby.**

- Mindset: the brief says "hold ten bikes". Thinking bigger, the real goal is that people choose to cycle to work. So the rack should also be easy to use with a heavy e-bike, secure against theft, and good looking enough that the building wants it in the lobby.
- Before building: success is ten bikes, any frame size, locked in under 30 seconds each. Constraints: floor anchors only, no wall drilling, a fixed budget. Failure: a bike tips over, scratches, or can be stolen with hand tools. A cardboard and plywood mockup tested with five real bikes in an afternoon shows that the planned spacing is too tight for wide handlebars. That is cheap to learn now and expensive after welding.
- While working: a log of lock-up times from the mockup tests becomes the evidence in the design review.
- When things go wrong: anticipating bad actors means asking how a thief would attack it. The answer moves the anchor bolts under a welded cover.
- Deciding: the steel tube supplier is a reversible choice, so pick one quickly. The floor anchor pattern is irreversible once drilled, so measure the slab and check for embedded services first.

## Practice

1. Take a task you are about to start. Write its intent and the answers to who, what, when, where, why, and how in five minutes.
2. Name the most irreversible decision in a current project. What cheap experiment could reduce its uncertainty first?
3. Find one recurring task in your work that you understand well and do every week. Sketch how you would automate it, and what it would cost to maintain.

<details><summary>What a good answer includes</summary>

1. An intent stated as an outcome for a person, not as an activity, and a "why" that would change the design if it were different.
2. A specific decision, why it cannot be undone, and an experiment that costs a small fraction of getting it wrong.
3. A task that has stopped changing, a time saving that is larger than the maintenance cost, and a plan for what happens when the automation breaks.

</details>

## Common mistakes

- Thinking bigger by adding features, instead of by understanding the real goal better.
- Treating every decision with the same care. Reversible ones deserve speed; irreversible ones deserve depth.
- Automating a process before it is understood, which makes a bad process fast.
- Letting an estimate turn into a fact because it was written in a spreadsheet.
- Skipping the documentation because the work is fresh in your mind. It will not be in six months.

## Go deeper

- [The engineering method](08-the-engineering-method.md): the gate, plan, build, and refine.
- [Principles that last](07-principles-that-last.md): the laws and habits that never expire.
- [Problem-solving](../problem-solving/README.md): estimation, sanity checks, and root cause tools.
- [Philosophy failure cases](reference.md): the lookup sheet for this topic.
