# Shop tools

Shop tools cut, drill, bend, and finish material. Basic shop skill is hands-on and needs supervision and training. This lesson gives the concepts you need before you use a machine: surface speed, feed, safety guards, and the habits of a careful machinist.

Do not use a machine you have not been trained on. Use the school or community shop, or a qualified instructor. Read the [OSHA machine guarding overview](https://www.osha.gov/machine-guarding), which says any part of a machine that could injure a worker must be guarded.

**Prerequisites:** [Measurement tools](07-measurement-tools.md), [Python](02-python.md) (for speed calculations)
**Time:** 10-20 h of supervised practice, plus reading

## Core ideas

- **Surface speed** $V$ is how fast the cutting edge moves across the material, in surface feet per minute (sfm) in US customary units.
- **Spindle speed** (RPM) is set from surface speed and the tool diameter. A larger tool turns slower at the same surface speed.
- **Feed** is how fast the tool advances into the material. Too little feed rubs and dulls the tool. Too much feed breaks it.
- **Coolant and lubricant** reduce heat and friction. Choose the fluid for the material.
- **Chip control** matters. Long stringy chips are a hazard. Break them with the right feed and depth.
- **Guards and safety** come first. Wear safety glasses at all times. Remove loose sleeves and jewelry. Keep hands away from rotating parts.
- **Measure before and after** every cut. Use the calipers from the [measurement lesson](07-measurement-tools.md).

Ask your instructor for the shop's own safety rules. They override anything written here.

## Key equations

Spindle speed from surface speed:

$$N = \frac{3.82 \, V}{D}$$

Here $N$ is spindle speed in RPM, $V$ is surface speed in sfm, and $D$ is tool diameter in inches. The number 3.82 is $12/\pi$, which converts feet to inches and turns the circumference into RPM.

## Worked example

**Given:** A 1/4 in (0.25 in) drill bit in aluminum. The recommended surface speed for this material and tool is 300 sfm.

**Find:** The spindle speed in RPM.

**Assumptions:** Use the typical surface speed given. Check the tool and material supplier's recommendation for your job.

**Solution (run in Python):**

```python
import math
V = 300.0   # sfm
D = 0.25    # in
rpm = 3.82 * V / D
print("rpm =", rpm)
print("rpm with 12/pi:", (12 / math.pi) * V / D)
```

Output:

```
rpm = 4584.0
rpm with 12/pi: 4583.662361046586
```

**Answer:** About 4580 RPM. Round to the nearest value your machine can set.

**Sanity check:** The 3.82 factor is $12/\pi \approx 3.8197$. Using the exact factor gives 4583.7 RPM, which rounds to the same 4580 RPM. A small drill spinning at a few thousand RPM is typical.

## Practice

1. A 3/8 in drill runs in steel at 80 sfm. Find the RPM to the nearest whole number.
2. A 1/2 in drill runs in aluminum at 300 sfm. Find the RPM to the nearest whole number.
3. Which bit runs faster at the same surface speed, the 1/4 in or the 1/2 in? Explain in one sentence.
4. Name three guards or safety items you must have before you start a drill press.
5. Your chips come off as long, unbroken ribbons. Name one adjustment to try, and state the reason.

<details><summary>Answers</summary>

1. 815 RPM (814.9 before rounding)
2. 2292 RPM
3. The 1/4 in bit. Smaller diameter needs higher RPM at the same surface speed.
4. Answers will vary. Examples: safety glasses, a secured workpiece, and a guard or clear area around the spindle.
5. Answers will vary. Example: increase feed to break the chip, with the reason that it reduces the chip length.

</details>

## Common mistakes

- Running a tool at the RPM of a different material. Check the speed for each material.
- Using a large bit at high RPM. Surface speed rises with diameter.
- Clamping the workpiece loosely, so it spins or lifts.
- Taking too deep a cut, which overloads the tool.
- Skipping a measurement after the cut, then finding the part is wrong at the end.

## Go deeper

- [OSHA: Machine guarding](https://www.osha.gov/machine-guarding) by the U.S. Department of Labor: the guarding requirement that applies to every machine.
- [NIST Special Publication 811](https://www.nist.gov/pml/special-publication-811) by NIST: units and conversions for the dimensions you cut to.
- [Measurement tools](07-measurement-tools.md): reading the tools you check the part with.
- Related: [CAD](06-cad-solidworks.md), [starter kit](01-starter-kit.md), [design folder](../design/README.md).
