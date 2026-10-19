# Sanity-check the answer

**Type:** lesson

Before you report a number, ask whether it could be true. A sanity check does not prove the
answer is right, but it catches most arithmetic slips, misplaced decimal points, and sign
errors. Three quick checks cover most cases: order of magnitude, sign, and physical intuition.

**Prerequisites:** [Check units and limiting cases](05-units-and-limiting-cases.md), [Particle dynamics](../physics/02-particle-dynamics.md)
**Time:** 2-3 h

## Core ideas

- An **order-of-magnitude estimate** rounds every input to one significant figure and gets the
  answer within a factor of about 3 to 10. If your careful answer is far from the estimate, find
  out why before you trust it.
- A **sign check** asks whether the direction is right. A force that should pull should not
  point the other way. A cooling process should not show a heat gain.
- An **intuition check** asks whether the answer is plausible for an object you know. A 5 kg
  bag should weigh tens of newtons, not thousands.
- Run the check before the final write-up, not after. If a check fails, do not explain it away.
  Look for the error (lesson 08).

### Three checks, in order

1. Quick estimate. Round inputs to one figure and compute in your head or on paper.
2. Sign and direction. Do the forces, velocities, and heat flows point the right way?
3. Intuition. Compare to a familiar object or number. Does the answer match experience?

### What a good check looks like

- Stated as a range, not a point: "about 300 N, somewhere between 200 N and 400 N."
- Uses numbers you already know: 1 kg weighs about 10 N, a car travels about 30 m/s in town.
- Ends in a decision: "The answer is plausible, so I accept it" or "The answer is ten times too
  big, so I recheck the units."

## Key equations

The common quick estimate of weight is:

$$
W \approx 10\ \text{N per kg}
$$

This is $mg$ with Earth's surface $g$ rounded from $9.81\ \text{m/s}^2$ to $10\ \text{m/s}^2$. It is good to
within 2 %, which is enough for a sanity check.

For a freely falling object from rest, a quick speed estimate is:

$$
v \approx \sqrt{2 \times 10 \times h}
$$

with $h$ in meters, $v$ in m/s, and $g$ rounded to $10\ \text{m/s}^2$.

## Worked example

**Problem.** A ball is dropped from rest from a height of $h = 20\ \text{m}$. A classmate reports
the impact speed as $v = 198\ \text{m/s}$. Check the answer, then state the correct value.

**Given:** $h = 20\ \text{m}$, $v_0 = 0$, ignore air drag.

**Find:** the impact speed $v$ in m/s, and whether the reported value is plausible.

**Assumptions:** no air drag; gravity is Earth's surface value, $9.81\ \text{m/s}^2$.

**Step 1, quick estimate.** $v \approx \sqrt{2 \times 10 \times 20} = \sqrt{400} = 20\ \text{m/s}$.
The estimate is about 20 m/s.

**Step 2, careful calculation.** $v = \sqrt{2gh} = \sqrt{2 \times 9.81 \times 20} = 19.81\ \text{m/s}$.
The careful answer agrees with the estimate.

**Step 3, check the reported value.** $198\ \text{m/s}$ is ten times the careful value of
$19.8\ \text{m/s}$. A factor of exactly 10 usually points to a misplaced decimal point or a
unit slip. The number alone does not say which one. It does say the report fails the
order-of-magnitude check, so find the error and redo the calculation (lesson 08 shows how).

**Step 4, sign check.** The speed is a magnitude, so the sign is not in question here. The
direction is down, and the speed is positive.

**Answer:** $v = 19.8\ \text{m/s}$ (about 71 km/h). The reported 198 m/s is rejected.

**Sanity check (intuition):** 198 m/s is about 713 km/h, roughly airliner cruise speed. A ball
dropped from a building does not reach airliner speed. Air drag would limit a real ball well
below that. Intuition says the 198 m/s value is wrong, and the estimate agrees.

## Practice

1. Estimate the weight of a 3.0 kg backpack in newtons, then compute it with $g = 9.81\ \text{m/s}^2$ (Earth surface).
   Give the careful value.
2. A window pane has $A = 3.0\ \text{m}^2$, $\Delta T = 20\ \text{K}$, $L = 0.0040\ \text{m}$, and
   $k = 0.8\ \text{W/(m}\cdot\text{K)}$. Find $Q$ in W.
3. A ball is dropped from 80 m, ignoring air drag. Find its impact speed in m/s.

<details><summary>Answers</summary>

1. 29.43 N
2. 12000 W
3. 39.6 m/s

</details>

## Common mistakes

- Accepting the first number the calculator shows. Estimate first, so you know what to expect.
- Skipping the sign check because the magnitude looks right. A force pointing the wrong way
  is still a wrong answer.
- Rejecting a correct surprising answer without checking. Surprise is a reason to look, not a
  reason to reject.
- Using the sanity check as proof. A plausible answer can still be wrong by a factor of 2.
- Comparing to an object you do not really know. Choose a reference you can picture or measure.

## Go deeper

- [Units and standards](https://openstax.org/books/university-physics-volume-1/pages/1-2-units-and-standards) by OpenStax: the metric scale and the size of common quantities.
- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: the measurement chapter covers order-of-magnitude estimates.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: problem sets with checks on signs and sizes.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
