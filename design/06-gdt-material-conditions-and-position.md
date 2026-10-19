# GD&T material conditions and position

**Type:** lesson

Position is the most used geometric tolerance, and it is the one most often misread. Adding material conditions (MMC and LMC) lets the allowed position error grow when the feature is made away from its tightest size. That growth is called bonus tolerance.

The rules come from ASME Y14.5, a paid standard. This lesson describes the common practice in plain words. Check the standard for any case that is not covered here.

**Prerequisites:** [Tolerancing and stack-up](04-tolerancing-and-stack-up.md), [GD&T symbols and frames](05-gdt-symbols-and-frames.md)
**Time:** 8-12 h

## Core ideas

- **Position** controls the location of a feature's center or axis relative to its true (basic) position, which is set by basic dimensions and datums.
- **Position tolerance** is a diameter zone around the true position for a round feature. The actual axis must stay inside it.
- **Maximum material condition (MMC)** is the size at which a feature contains the most material. For a hole, that is its smallest allowed size. For a shaft or pin, it is its largest allowed size.
- **Least material condition (LMC)** is the opposite: the size with the least material. For a hole, the largest size. For a shaft, the smallest.
- **Regardless of feature size (RFS)** means the zone does not change with the size of the feature. RFS is the default when no modifier is shown in current editions of the standard.
- **Bonus tolerance** is the extra position error allowed when a feature is away from its MMC. It is the difference between the actual size and the MMC size.
- **Virtual condition** is the worst combined size and position a feature can have, and it is used to design a gauge.

## Why material conditions matter

Imagine a bolt going through a hole. If the hole is at its smallest allowed size, it is hardest to fit a bolt through, and its position must be most accurate. If the hole is larger, there is more room, so the position can be a bit less accurate. Bonus tolerance captures that trade-off.

An RFS callout does not give bonus. The position zone is the same no matter what size the hole is. This is stricter and sometimes needed, but it can cost more to make.

## Key equations

Maximum material condition size for a hole of nominal $N$ and tolerance $t_s$ (plus and minus):

$$
\text{MMC}_{\text{hole}} = N - t_s, \qquad \text{LMC}_{\text{hole}} = N + t_s
$$

For a shaft:

$$
\text{MMC}_{\text{shaft}} = N + t_s, \qquad \text{LMC}_{\text{shaft}} = N - t_s
$$

Bonus tolerance, for a feature at actual size $A$ with a MMC modifier:

$$
B = |A - \text{MMC}|
$$

For a hole, $B = A - \text{MMC}$. For a shaft, $B = \text{MMC} - A$. Bonus is zero at MMC and grows as the feature moves toward LMC. It is never negative.

Total allowable position tolerance at MMC:

$$
t_{\text{total}} = t_{\text{pos}} + B
$$

where $t_{\text{pos}}$ is the position zone diameter written in the frame.

Virtual condition at MMC:

$$
V_{\text{hole}} = \text{MMC}_{\text{hole}} - t_{\text{pos}}, \qquad V_{\text{shaft}} = \text{MMC}_{\text{shaft}} + t_{\text{pos}}
$$

Position deviation from the true position, measured as offsets $x$ and $y$ in the datum frame:

$$
d = 2\sqrt{x^2 + y^2}
$$

Here $d$ is the diameter of the deviation zone. A feature passes when $d \le t_{\text{total}}$.

Units: all lengths in mm (or in). Bonus, tolerance, and position are all in the same unit.

## Worked example

A plate has a hole specified as $\varnothing 10.00 \pm 0.10$ mm, with a position tolerance of $\varnothing 0.25$ mm at MMC to datums A, B, and C. The hole is measured at actual diameter 9.95 mm, and its axis is found to be offset by $x = 0.11$ mm and $y = 0.09$ mm from the true position. Does it pass?

**Given.** Nominal $N = 10.00$ mm, size tolerance $\pm 0.10$ mm, position $t_{\text{pos}} = 0.25$ mm at MMC. Actual size $A = 9.95$ mm. Offsets $x = 0.11$ mm, $y = 0.09$ mm.

**Find.** Whether the hole passes, with the bonus tolerance and the total allowed position.

**Assumptions.** The datums are set correctly. The offsets are measured in the datum frame. Measurement error is ignored.

**Solution.**

Step 1. MMC for a hole: $\text{MMC} = 10.00 - 0.10 = 9.90$ mm.

Step 2. Bonus: $B = A - \text{MMC} = 9.95 - 9.90 = 0.05$ mm.

Step 3. Total allowed position: $t_{\text{total}} = 0.25 + 0.05 = 0.30$ mm.

Step 4. Position deviation: $d = 2\sqrt{0.11^2 + 0.09^2} = 2\sqrt{0.0202} = 0.284$ mm.

Step 5. Compare: $0.284 \le 0.30$, so the hole passes.

Step 6. Check under RFS: the allowed zone is 0.25 mm, and $0.284 > 0.25$, so the same hole would fail if the callout were RFS.

**Answer.** Bonus 0.05 mm, total allowed position 0.30 mm, deviation 0.284 mm. The hole passes at MMC, and it would fail at RFS.

**Sanity check.** The bonus is positive because 9.95 mm is larger than the smallest allowed hole (9.90 mm). The total grows as the hole gets larger, which matches the idea that a looser fit gives more room. The deviation is less than the total, so there is a small margin of 0.016 mm.

## Checklist

- Is the MMC size found from the right side: smallest for a hole, largest for a shaft?
- Is bonus calculated as actual size minus MMC for a hole, and MMC minus actual for a shaft?
- Does the total position include the bonus, and only when there is a modifier?
- Is the position deviation a diameter, found as twice the radial offset?
- Is RFS checked when the drawing shows no modifier?

## Practice

1. A hole is $\varnothing 8.00 \pm 0.05$ mm with a position tolerance of $\varnothing 0.20$ mm at MMC. The actual size is 7.98 mm. Find the bonus tolerance in mm.
2. For the same hole, find the total allowed position in mm if the actual size is 8.05 mm.
3. A shaft is $\varnothing 20.00 \pm 0.10$ mm with a position tolerance of $\varnothing 0.10$ mm at MMC. The actual size is 19.95 mm. Find the total allowed position in mm.
4. For the hole in question 1, find the virtual condition in mm.

<details><summary>Answers</summary>

1. 0.03
2. 0.30
3. 0.25
4. 7.75

</details>

## Common mistakes

- Using the nominal size as the MMC instead of the size at the tight end of the tolerance.
- Applying bonus to a callout that has RFS, which does not allow it.
- Flipping the sign of bonus between holes and shafts.
- Using the radial offset as the deviation. The deviation is the diameter, which is twice the radial offset.
- Forgetting the bonus when a feature is measured at an actual size away from MMC, which makes a good part look bad.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: a free engineering hub where tolerancing and fit topics appear.
- [MIT OpenCourseWare, 2.017J Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) by MIT: a free course where tolerance and fit decisions affect real assemblies.
- The position and material condition rules are defined in ASME Y14.5, a paid standard, named here for reference only.
- [Design reference](reference.md): the lookup sheet for this topic.
