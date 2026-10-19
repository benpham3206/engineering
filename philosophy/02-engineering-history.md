# Learning from history and failure

**Type:** philosophy

**Engineering history** is a record of people solving real problems and, often, learning hard lessons from failures. An engineer studies it because the same mistakes repeat when people forget the past, and because many current safety rules exist only because someone was hurt.

**Prerequisites:** [What engineering is](01-what-engineering-is.md)
**Time:** 3-5 h

## Core ideas

- People have built to meet needs for thousands of years: shelter, water, transport, and defense. Early builders worked from rules of thumb and experience, long before formal physics.
- Early written rules show that society has always linked builders to safety. The Code of Hammurabi, from about 1750 BCE in ancient Babylon, includes laws that held builders responsible if a house they built collapsed and killed the owner. The idea that the builder answers for the design is very old.
- Formal engineering grew in the 1700s and 1800s. Mathematics, mechanics, and materials science let designers calculate loads and stresses before building. Professional societies and licensing followed.
- Each major advance came with new failures. Bridges, boilers, ships, and aircraft all failed in ways that the designers had not expected. Investigations of those failures produced new knowledge.
- A **failure investigation** has a standard shape:
  - Gather the facts: what happened, when, and under what conditions.
  - Find the **physical cause**, such as a material fault or a force that was not counted.
  - Find the **root cause**, meaning the decision or process that allowed the physical cause to happen.
  - Recommend changes to design, testing, rules, or training.
- Stopping at the broken part is common, but it misses the design, testing, or management decisions that let the part fail.

### Case: Tacoma Narrows Bridge (1940)

The Tacoma Narrows Bridge in Washington State opened in July 1940. It was a suspension bridge with a narrow, shallow, and flexible deck. In November 1940, in moderate winds, the deck began twisting strongly and then broke apart. The collapse is famous and is often used to teach aeroelastic flutter.

What the record shows, based on the Washington State Department of Transportation history of the bridge:

- The collapse is attributed mainly to **self-excited aeroelastic torsional flutter**, a twisting motion in which the deck's own movement changed the wind forces so they fed the motion. This differs from ordinary vortex-shedding resonance, where an outside vortex frequency drives the structure.
- The deck's design resisted twisting poorly. Its shallow, narrow shape and flexibility let the motion grow until the structure could not survive it.
- The WSDOT account also notes that a slipped cable band at mid-span had unbalanced the main cables, which started the motion.
- Expert boards studied the failure. Their work and the later university research changed how bridge engineers account for wind. Wind is now treated as a design load, and wind tunnel testing became standard for long-span bridges.

The lesson for engineers: a structure can meet its strength calculations and still fail because a physical effect was not modeled. Wind is a load that acts with motion, not just a steady push.

### Other turning points

- Steam boilers and pressure vessels in the 1800s led to codes, inspections, and licensing.
- Aircraft accidents in the 1900s led to standard testing, better records, and independent accident investigation agencies.
- Software failures in medical and transport systems in the 1980s and later led to modern software safety practice. See [Safety and risk](03-safety-and-risk.md).

## Checklist

When you study a historical failure, ask:

- [ ] What was the goal of the design, and what did its designers expect?
- [ ] What physical effect or load caused the failure?
- [ ] What assumption was wrong, missing, or untested?
- [ ] Which decision, rule, or process allowed the flaw to reach the public?
- [ ] What standard, test, or practice changed as a result?
- [ ] Which of those changes still protects people today?

## Example

Apply the checklist to the Tacoma Narrows Bridge.

- Goal: a long, low-cost crossing that carries traffic over a water channel.
- Expected behavior: the designers analyzed the bridge as a static structure under steady loads and modest dynamic effects.
- Physical cause: wind-driven torsional flutter. Wind interacted with the deck shape so that the twisting motion fed on the wind.
- Assumption that failed: that the deck was stiff enough, and that wind effects could be handled by static rules for the design. The deck's narrow, flexible profile did not resist twisting.
- Process gap: the bridge was built without wind tunnel testing of the deck shape, which was not yet standard practice for suspension bridges of that kind.
- Change that followed: bridges are now tested for aerodynamic stability, and designs use deep, stiff, or aerodynamically shaped decks when wind is a concern.
- Check: any new long-span bridge should show its wind analysis. If it does not, that is a flag, even if the static strength numbers look fine.

The bridge was not simply badly built. The design process did not include a physical effect that mattered, and the change made the field safer.

## Practice

1. Name one thing that engineers learned from a historical failure that now appears in everyday codes or practice.
   - Key points: a specific example (for example, wind testing for bridges, boiler inspection, or aircraft certification), the failure that prompted it, and the rule or practice it created.
2. Why is the "physical cause" not the same as the "root cause"? Give a short example.
   - Key points: the physical cause is what broke or moved; the root cause is the decision or process that allowed it; a good example names both.
3. The Code of Hammurabi made builders responsible for collapses. Why might a rule like that make builders more careful?
   - Key points: personal responsibility creates incentives for checking work, the rule ties consequences to the decision maker, and the rule is one early form of accountability.
4. A bridge passes all static load tests but shows large motion in strong wind. What historical lesson applies?
   - Key points: Tacoma Narrows; dynamic and aerodynamic effects must be analyzed and tested; static strength is not the whole story.

<details><summary>Answers</summary>

Answers are key points a good answer covers. See each question above.

1. A specific rule or practice tied to a named failure.
2. Physical cause is what broke; root cause is the process decision; a clear example.
3. Personal accountability creates incentives to check work and ties consequences to decisions.
4. Tacoma Narrows; test dynamic and wind effects; static checks are not enough.

</details>

## Common mistakes

- Telling history as a list of dates. The useful part is the cause and the change that followed.
- Blaming a single person without looking at the process, testing, and rules around them.
- Assuming old designs were foolish. Many were the best available at the time, based on the knowledge of that era.
- Forgetting that new designs can repeat old failures in a new form, such as a new material or a new kind of control software.
- Treating a failure investigation as finished when the report is published. The useful test is whether the lesson changed later practice.

## Go deeper

- [Tacoma Narrows Bridge history and lessons from failure](https://wsdot.wa.gov/tnbhistory/bridges-failure.htm) by the Washington State Department of Transportation: the state agency's account of the collapse and its causes.
- [NIST Disaster and Failure Studies](https://www.nist.gov/topics/disaster-failure-studies) by the National Institute of Standards and Technology: a list of federal investigations of building and infrastructure failures, with a path into the reports.
- [MIT OpenCourseWare](https://ocw.mit.edu/) by MIT: free course materials. Search for history of technology or structural engineering courses.
- [history](../history/README.md): the full story of engineering, era by era, with its people and great projects.
- [Philosophy failure cases](reference.md): the lookup sheet for this topic.
