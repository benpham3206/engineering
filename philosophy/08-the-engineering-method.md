# The engineering method

**Type:** philosophy

A method for doing engineering work of any size, from choosing a bolt to building a spacecraft. It is adapted for physical engineering from the author's [engineering standard](https://github.com/benpham3206/agent-engineering/blob/main/standards/engineering.md), which states it in full.

**Prerequisites:** [Principles that last](07-principles-that-last.md).

## Axioms

1. **Reality is authoritative.** Models, drawings, plans, and assumptions are approximations. When the test and the analysis disagree, the analysis is what changes.
2. **Engineering is achieving an intended outcome under constraints and reality.** Not activity, not effort, not elegance for its own sake.
3. **Everything you add has a cost.** Every part, interface, joint, and dependency can fail, must be made, and must be maintained.
4. **Rigor scales with consequence, uncertainty, and irreversibility.** A shelf bracket and a pressure vessel do not get the same process.
5. **Claims of correctness require evidence.** "It should work" is a hypothesis.
6. **Simpler wins** when it meets the same requirements.

## The gate

Before starting, ask: is this work low consequence, low uncertainty, and easy to reverse, all three?

- **Yes:** take the fast path. Build it, check it, iterate. A jig for the shop, a test fixture, a first prototype.
- **No:** take the full path below. A part that carries people, holds pressure, spins fast, flies, or costs a lot to remake.

A clear goal alone does not open the fast path. Cutting expensive stock, pouring concrete, and releasing a drawing to a supplier are irreversible, so they always get constraints checked and consequences traced first.

## Plan

1. **Intent:** why does this need to exist?
2. **Goal and definition of done:** what exactly must it do, stated so a test can say yes or no.
3. **Metrics:** how will you know? Load, deflection, temperature, life, mass, cost. Build the test rig if you need one.
4. **Constraints:** what cannot be violated. Safety, codes, envelope, interfaces, budget, schedule.
5. **Assumptions and dependencies:** what you are taking as true, and what depends on what. Each assumption gets a limit and a way to check it.
6. **First principles:** strip the problem to the physics and the requirement. What is actually necessary?
7. **Architecture:** the concept, the load paths, the interfaces between parts.
8. **Consequences:** trace second- and third-order effects. What is the worst that can happen, and then ten times worse? Design for how it fails.

## Build

1. **Question every requirement.** Each one should trace to a person and a reason. Requirements from unknown sources are often wrong.
2. **Delete what does not need to exist.** The best part is no part. Use the first option that works: no part at all, an existing part of the design, a standard catalog part, then a custom part. Never delete safety, margin you need, or anything that prevents a failure.
3. **Integrate.** Combine parts where it removes joints and failure points, and keep separate the parts that need to be serviced or replaced separately.
4. **Simplify** what remains.
5. **Make it,** in order: break the system into subsystems, define the interfaces (loads, fits, signals, units), sequence the work by dependency, and build and integrate one piece at a time.
6. **Verify.** Check against the requirements and metrics, with tests where failure matters. Check every interface the change reaches: mating parts, assemblies, drawings, the bill of materials, the manual, and the way it is taken apart again.
7. **Optimize only when measured.** Default: do not. Make it lighter or cheaper only when a measured metric misses its target, the part you are optimizing is the real bottleneck, and the design is already verified.
8. **Shorten the feedback loop.** Faster test cycles beat cleverer analysis.
9. **Automate** only processes you understand and that have stopped changing.

## Refine

1. **Measure:** reproduce the problem and record the actual state.
2. **Compare:** expected against actual.
3. **Find the bottleneck:** what is limiting the goal right now?
4. **Diagnose the root cause:** ask why, backing each answer with evidence, up to five times for small problems and ten for serious or repeated ones. Then ask which requirement, constraint, or assumption let the problem through. If one did, go back to Plan, not just Build.
5. **Correct** it, routing back to Plan or Build.
6. **Verify the fix.** The test that caught the problem should fail if the fix is removed.
7. **Clean up:** remove temporary parts, obsolete drawings, and stale notes.
8. **Stress test** when the consequence warrants it.
9. **Repeat** until the definition of done holds.

## Checklist

- [ ] Did I run the gate honestly, and pick the path that matches the consequence?
- [ ] Is the definition of done testable?
- [ ] Is every requirement traced to a reason?
- [ ] Did I delete before adding?
- [ ] Is every claim of "it works" backed by a test or a checked calculation?
- [ ] Did I check every interface the change touches?
- [ ] Did I trace the worst case?

## Example

**A replacement bracket for a ceiling-mounted projector.** The fast path tempts: it is one small part. Run the gate. Consequence: it hangs over people's heads. Not low. So take the full path.

- Plan: the goal is to hold the projector for ten years with no creep or loosening. Constraint: a falling load must not be possible. Assumption: the ceiling anchor is sound, which is checked by a pull test. Worst case times ten: the bracket fails and the projector falls; so add a secondary safety cable, a second, independent load path.
- Build: delete the decorative cover plate (no requirement traces to it). Use a standard steel angle instead of a custom part. Verify by hand calculation against [the mechanics reference](../physics/reference-mechanics.md) and a proof load test at several times the projector's weight.
- Refine: in testing, a screw loosens under vibration from the projector fan. Root cause, after asking why: the joint had no preload requirement. Correct it with a specified torque and a locking method, and add "preload specified" to the design checklist so the whole class of failure is prevented next time.

## Practice

1. Run the gate on three things you might build this month. Which get the full path, and why?
2. Take a design you have made and apply Build step 2. List every part you could delete, and what deleting each would cost.
3. Pick a failure from [the failure cases](reference.md). Walk it through Refine step 4. Which constraint or assumption let it through?

<details><summary>What a good answer includes</summary>

1. Each verdict names the specific consequence, uncertainty, or irreversibility that decided it.
2. At least one deletion that removes a failure mode, and one you rejected because it would remove safety or a needed margin.
3. A chain of whys, each supported by the investigation findings, ending at a requirement, constraint, or assumption, not at a person.

</details>

## Common mistakes

- Taking the fast path because the part is small, when the consequence is large.
- Optimizing before verifying. A light part that fails is not light, it is broken.
- Adding parts to fix problems that deleting parts would remove.
- Treating a successful test of one configuration as proof for all of them.
- Stopping at "operator error". Ask why the design allowed the error.

## Go deeper

- [Engineering standard](https://github.com/benpham3206/agent-engineering/blob/main/standards/engineering.md) by Ben Pham: the full method, including modularity, outcome over activity, and the project lifecycle.
- [Principles that last](07-principles-that-last.md) and [Safety and risk](03-safety-and-risk.md) in this folder.
- [Problem-solving](../problem-solving/README.md): the same discipline applied to a single problem.
