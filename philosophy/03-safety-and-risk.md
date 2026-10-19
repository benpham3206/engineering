# Safety and risk

**Type:** philosophy

Safety and risk are the two ideas engineers use to judge whether a design can harm people. Engineers need them to decide what is acceptably safe before anyone uses the product.

Safety means that a design keeps people from harm across the conditions it will meet. Risk is the chance of harm multiplied by how bad the harm would be.

**Prerequisites:** [What engineering is](01-what-engineering-is.md), [Learning from history and failure](02-engineering-history.md), [Axial and torsion](../physics/04-axial-and-torsion.md), [Factor of safety and failure](../design/07-factor-of-safety-and-failure.md)
**Time:** 5-8 h

## Core ideas

- A hazard is a condition that could cause harm, such as a heavy load, high voltage, or a fast-moving part. A risk is the combination of how likely a hazard is to cause harm and how severe the harm would be.
- Safety is designed in. Good designers find hazards early, remove them when possible, guard against the rest, and warn users about what remains.
- A common order of protection, from strongest to weakest:
  - Eliminate the hazard (remove the source).
  - Substitute a less hazardous material or process.
  - Engineering controls (guards, barriers, interlocks, ventilation, automatic shutoffs).
  - Administrative controls (procedures, training, warnings, labels, alarms, scheduling).
  - Personal protective equipment (PPE) such as glasses, gloves, and hearing protection.
  The weakest layers depend most on human behavior, so they fail most often in practice.
- Safety factor is the ratio of the strength of a part to the load it will carry. A part with a capacity of 10 kN carrying a load of 5 kN has a safety factor of 2. Safety factors cover uncertain loads, material variation, and manufacturing error.
- Defense in depth means stacking independent protections, so one failure does not cause harm by itself.
- Failure modes and effects analysis (FMEA) is a method where the team lists each part or step, asks how it could fail, what the effect would be, and how likely and detectable the failure is. The result ranks what to fix first.
- Risk is never zero. Engineers set an acceptable level, and that decision belongs to people and society, not to the designer alone. Engineers must report risks honestly so that the decision is informed.

### Worked terms

- $\text{Safety factor} = \text{strength} / \text{load}$. Use the same units for both.
- Typical values: structural steel yield strength about 250 MPa (36 ksi) for mild steel. Safety factors for building structures are often in the range of 1.5 to 3, depending on the code and the load type.

### Case: Hyatt Regency walkway collapse (1981)

On July 17, 1981, two suspended walkways in the lobby of the Hyatt Regency hotel in Kansas City, Missouri, collapsed onto a crowded dance below. The collapse killed 114 people and injured many more.

What the official investigation found, published by the National Bureau of Standards (now NIST):

- The walkways were hung from the ceiling by rods. In the design as first approved, a long rod ran through both walkways, supporting the upper walkway's connection.
- During construction the connection was changed, and the single long rod became two shorter rods, with the lower walkway hung from the upper one. This change roughly doubled the load on the connection that failed.
- The change was not properly reviewed for its effect on the connection, and the original design analysis did not capture the revised load path.
- The lesson is about process as well as physics. A change to a structure must be checked against the forces it creates, not just the shape it looks like on paper.

### Case: Therac-25 radiation therapy machine (1985-1987)

The Therac-25 was a radiation therapy machine that delivered high-energy X-rays or electron beams to patients. Between 1985 and 1987, several patients received massive overdoses. Some died, and others were seriously injured.

The investigation by Nancy Leveson and Clark Turner (published in IEEE Computer, 1993) found several contributing causes:

- The Therac-25 relied on software for safety functions instead of independent hardware interlocks that earlier models had.
- Software errors, including a timing (race condition) error, allowed the machine to be set in an unsafe mode when an operator made a fast sequence of edits.
- The manufacturer did not do a thorough safety analysis, and some reports of problems were dismissed or explained away.
- The article's central point is that most accidents are system accidents. The failure came from how the whole system was designed, operated, and reviewed, not from one bad line of code.

The lesson: software is part of the safety system. It needs the same independent checks, testing, and documentation as hardware, and reports of failure must be taken seriously.

## Key equations

Safety factor:

$$
\mathrm{SF} = \frac{\sigma_y}{\sigma_{\text{actual}}}
$$

where $\mathrm{SF}$ is the safety factor (unitless), $\sigma_y$ is the yield strength of the material (Pa, or psi), and $\sigma_{\text{actual}}$ is the stress in the part under the design load (Pa, or psi). Stress is found from:

$$
\sigma = \frac{F}{A}
$$

where $F$ is the force (N, or lbf) and $A$ is the cross-sectional area (m$^2$, or in$^2$).

## Worked example

**Given:** A round steel rod, diameter $d = 20$ mm (0.020 m), carries a tensile load $F = 12$ kN (12,000 N). The steel has a yield strength of $\sigma_y = 250$ MPa (typical mild steel).

**Find:** The stress in the rod, and the safety factor against yielding.

**Assumptions:** The load is steady and pure tension. The rod is uniform and free of cracks. The yield strength is the typical value, not a tested value for this batch.

**Solution:**

1. Area: $A = \pi (d/2)^2 = \pi (0.010\ \text{m})^2 = 3.142 \times 10^{-4}\ \text{m}^2$.
2. Stress: $\sigma = F / A = 12{,}000 / 3.142 \times 10^{-4} = 3.82 \times 10^{7}\ \text{Pa} = 38.2\ \text{MPa}$.
3. Safety factor: $\mathrm{SF} = 250 / 38.2 = 6.54$.

**Answer:** The stress is 38.2 MPa (about 5,540 psi). The safety factor against yielding is about 6.5.

**Sanity check:** The stress is far below yield, which means the rod is strong for this load. The number makes sense: a 20 mm rod is a fairly thick rod for a 12 kN load (about 1.2 metric tons). The safety factor is high, so the design is safe but may be heavier than needed. An engineer might check whether a smaller rod meets a safety factor closer to 2 to 3, given the code and the uncertainty in the load.

## Practice

1. Name the four layers of protection in order from strongest to weakest, and give one example of each for a kitchen blender.
   - Key points: eliminate (design with no exposed blades), guard (lid interlock that stops the motor when open), warn (label and manual), train (instruct users to unplug before cleaning).
2. A rope carries a 2 kN load and has a breaking strength of 10 kN. What is its safety factor, and is that enough for a lifting rope?
   - Key points: safety factor is 5; lifting codes and the uncertainty of loads, wear, and knots decide adequacy; a good answer says the number alone is not enough without the code.
3. Why did the Hyatt Regency collapse happen even though each rod was designed for the original load?
   - Key points: the connection was changed, the load path changed, and the change was not analyzed again.
4. Why is "eliminate the hazard" usually the strongest protection?
   - Key points: it removes the source, so no protection can fail; other layers depend on people or devices working correctly.

<details><summary>Answers</summary>

Answers are key points a good answer covers. See each question above.

1. Eliminate, guard, warn, train; with a correct example for each.
2. Safety factor 5; codes and load uncertainty decide adequacy.
3. Load path changed; change not reanalyzed.
4. Removes the source; other layers can fail.

</details>

## Common mistakes

- Treating safety factor as a magic number. A factor of 2 is not automatically safe; the right value depends on the load, the material, and the consequence of failure.
- Reviewing a part but not the change to it. Most failures in investigations come from changes that were not analyzed.
- Trusting a single protection layer, especially a warning label or a single sensor.
- Forgetting software and human factors. Software can fail in the same ways hardware does, and users make predictable errors.
- Confusing hazard and risk. A hazard without exposure or likelihood is less of a risk than one that people meet every day.

## Go deeper

- [Hyatt Regency walkways collapse investigation (NBS BSS 143)](https://www.nist.gov/publications/investigation-kansas-city-hyatt-regency-walkways-collapse-nbs-bss-143) by NIST: the official federal investigation; the full report PDF is linked from this page.
- [An Investigation of the Therac-25 Accidents](https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_1.html) by Nancy Leveson and Clark Turner, reprinted by MIT: the full article in readable form, first of three parts.
- [NIST Disaster and Failure Studies](https://www.nist.gov/topics/disaster-failure-studies) by NIST: federal investigations of structural and building failures.
- [MIT OpenCourseWare](https://ocw.mit.edu/) by MIT: free course materials on reliability and safety engineering.
- [Philosophy failure cases](reference.md): the lookup sheet for this topic.
