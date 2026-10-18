# Automation and robotics

Automation uses machines, controls, and sensors to do work with little or no human hands on the task. A robot is one kind of automated machine: a programmable arm or mechanism that moves and acts. Automation makes sense when a task is repeatable, dangerous, precise, or needs to run for long hours. An engineer who designs for automation must think about the process, the sensors, the controls, and the safety of the cell, not only the part.

**Prerequisites:** [Shop safety](01-shop-safety.md), [Tolerances, fits, and surface finish](08-tolerances-fits-finish.md)
**Time:** 5-7 h

## Core ideas

- **Automation cell**: a workspace with one or more machines, a robot or handler, sensors, and controls. Parts come in, are processed, and leave.
- **PLC (programmable logic controller)**: an industrial computer that reads inputs (sensors and switches) and sets outputs (motors, valves, and lights) using a fixed scan cycle. Most factory machines are controlled by PLCs.
- **Sensor**: a device that turns a physical state into a signal. Common types are proximity switches, photoelectric sensors, encoders (which measure position or rotation), and vision cameras.
- **Degrees of freedom (DOF)**: the number of independent ways a mechanism can move. A typical industrial arm has six DOF, so it can place a tool at any point and at any angle within its reach.
- **Accuracy**: how close a position is to the commanded target. **Repeatability**: how close the robot returns to the same position each time. A robot can be very repeatable but not very accurate, and that matters for fits and calibration.
- **Payload**: the maximum mass the robot can carry at its tool flange while still meeting its specifications.
- **Cycle time**: the time to complete one full cycle of the process, from part in to part out.
- **Collaborative robot (cobot)**: a robot designed to work near people. Cobots limit speed and force, and they use sensors to stop when they touch something. Limits are not the same as guarding, so a cobot still needs a risk assessment.
- **OEE (overall equipment effectiveness)**: a common measure of how well a machine is used. It multiplies three ratios: availability, performance, and quality.

Automation design habits:

- Design parts that feed and locate easily. A part with a clear datum and a self-centering shape is much easier for a robot to pick.
- Use sensors to confirm each step. A cell that does not check for a part can keep cutting air or crashing.
- Plan for faults. Every cell needs a clear state for jams, missing parts, and emergency stops.
- Keep humans and robots apart by design where you can. Fixed guards and light curtains are common tools.

## Key equations

Overall equipment effectiveness, where $A$ is availability (run time divided by planned time), $P$ is performance (actual output rate divided by ideal rate), and $Q$ is quality (good parts divided by total parts):

$$\text{OEE} = A \times P \times Q$$

Units: each ratio is a dimensionless fraction between 0 and 1. The result is also a fraction, often written as a percent.

Time to produce $n$ parts with a cycle time $t_c$ (seconds per part):

$$T = n \, t_c$$

Units: $T$ is in seconds when $t_c$ is in seconds. Divide by 3600 to convert to hours.

## Worked example

**Given:** A cell is planned for 8 h. It is stopped for 0.8 h, so the run time is 7.2 h. The ideal rate is 1 part every 40 s. In the run time it makes 550 parts, and 540 of them are good.

**Find:** The OEE for the cell.

**Assumptions:** The ideal rate is the cell's proven best speed, and all times are measured the same way.

**Solution:**

1. Availability, run time divided by planned time:
$$A = \frac{7.2}{8} = 0.90$$
2. Ideal output in the run time: $7.2 \times 3600 / 40 = 648$ parts. Performance is actual output divided by ideal output:
$$P = \frac{550}{648} = 0.849 \approx 0.85$$
3. Quality, good parts divided by total parts:
$$Q = \frac{540}{550} = 0.982 \approx 0.98$$
4. OEE:
$$\text{OEE} = 0.90 \times 0.85 \times 0.98 = 0.750$$

**Answer:** The OEE is 0.750, or 75.0 percent.

**Sanity check:** Each factor is between 0 and 1, so the product must be smaller than the smallest factor. Here the smallest factor is 0.85, and 0.750 is below it. The result is consistent.

## Practice

1. A cell has $A = 0.95$, $P = 0.80$, and $Q = 0.99$. What is OEE? Round to three decimal places.
2. A robot takes 18 s per part. How many seconds does 200 parts take?
3. A robot repeats to within 0.02 mm but is off by 0.3 mm from the target on average. Is it repeatable? Is it accurate? Answer in one sentence.
4. A PLC reads a proximity switch. Name what the switch is detecting, in one sentence.
5. Why does a cobot still need a risk assessment even though it is designed to work near people?

<details><summary>Answers</summary>

1. 0.752
2. 3600 seconds
3. Yes, it is repeatable (small spread), but not accurate (the average is off by 0.3 mm).
4. The presence or absence of an object (for example a part or a fixture) at the switch.
5. Speed and force limits and touch sensing reduce risk but do not remove all hazards, so the whole cell still needs assessment.

</details>

## Common mistakes

- Confusing accuracy with repeatability. A robot that repeats well may still miss the target every time.
- Using OEE from one bad shift to judge the whole machine. Measure over a representative period.
- Assuming a cobot is safe in every case without assessment, guarding, or checks.
- Designing parts that are hard to grip, locate, or feed, then blaming the robot.
- Leaving out fault handling. A cell that stops in an unknown state is slow to recover and can be dangerous.

## Go deeper

- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: national research on manufacturing, including automation and robotics.
- [NIST: Weights and measures](https://www.nist.gov/pml/weights-and-measures) by NIST: measurement standards that underpin accuracy claims.
- [OSHA: Machine guarding](https://www.osha.gov/machine-guarding) by OSHA (U.S. Department of Labor): guarding principles that apply to automated cells.
