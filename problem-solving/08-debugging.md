# Debugging when it does not work

**Type:** lesson

**Debugging** is the process of finding the one step in a chain that causes a wrong answer or failed build, and fixing only that step. Engineers need it because guessing and changing several things at once slows the search and hides the real cause.

When an answer is wrong, or a calculation or build fails, the cause is almost never a
mystery. Find it by shrinking the problem until you can see which part breaks, then fix only
that part.

**Prerequisites:** [Sanity-check the answer](06-sanity-check-the-answer.md), [Check units and limiting cases](05-units-and-limiting-cases.md)
**Time:** 4-6 h

## Core ideas

- A **symptom** is what you observe: a number that is too large, a result with the wrong sign,
  a build that stops with an error. A **cause** is the step that produces the symptom.
- A **chain** is the ordered list of steps from inputs to answer: inputs, unit conversions,
  each formula, the final arithmetic. Any link can break.
- **Isolation** means narrowing the chain until one link is responsible. The methods below do it.
- Reproduce first. Write down the exact inputs that give the bad answer. If you cannot
  reproduce it, you cannot tell whether a fix worked.

### The isolation method

1. Reproduce the failure. Write the inputs, the expected result, and the actual result.
2. Find a case you know the answer to. A limiting case (lesson 05) or a textbook value works.
   Run it through the same chain. If the known case passes, the bug is in the input handling
   for your case. If it fails, the bug is in the formula or code.
3. Print or write each intermediate value. Compare each to what you expect.
4. Check units at every link. Most wrong engineering answers are units errors.
5. Change one thing at a time and rerun. Stop as soon as the symptom changes in the expected
   way, then confirm the cause.
6. Fix the cause, not the symptom. If you multiply the final answer by 10 to match a reference,
   you have hidden the bug, not fixed it.
7. Check the fix on the original failing input and on a second, independent input.

### Common causes, most frequent first

- Units not converted (centimeters entered as meters, minutes as hours, degrees as radians).
- A formula copied with a wrong symbol or a missing factor (such as a forgotten $\sqrt{\ }$ or
  a factor of 2).
- A sign error from a wrong positive direction.
- Rounding too early, so a small error grows.
- Inputs in the wrong place: swapped arguments or wrong row in a table.
- For a build or program: a stale file, a missing dependency, or a path that points to an old copy.

### Stop when the bug is clear

Once you can say, "the cause is step 3, because its output is 600 when 6000 is expected," you
have isolated it. You do not need to understand the whole system first.

## Key equations

Debugging does not add a new equation. It uses the one already in the solution and checks each
link against the formula. For the glass example in lesson 05:

$$
Q = \frac{k\,A\,\Delta T}{L}
$$

If the output differs from the expected value by exactly a power of 10, look first at the
unit of $L$ (or $A$ or $k$). A factor of 10 is the signature of a unit prefix error, and a
factor of 2 is often a missing or extra factor.

## Worked example

**Problem.** A student computes the heat conducted through a window pane, with $\Delta T$ the temperature difference across the glass, and reports $Q = 600\ \text{W}$.
A reference calculation for the same pane gives about 6000 W. Find the cause and fix it.

**Given:** $A = 1.5\ \text{m}^2$, $\Delta T = 20\ \text{K}$, $k = 0.8\ \text{W/(m}\cdot\text{K)}$,
and the student's entry $L = 0.04$ (the pane is 4 mm thick).

**Find:** the step that causes the factor of 10 error, and the corrected value.

**Step 1, reproduce.** Run the formula with the stated inputs:

$$
Q = \frac{0.8 \times 1.5 \times 20}{0.04} = \frac{24}{0.04} = 600\ \text{W}
$$

The bad answer reproduces, so the cause is in the inputs or the formula.

**Step 2, known case.** The earlier lesson Check units and limiting cases gives the correct answer for $L = 0.0040\ \text{m}$:
$Q = 6000\ \text{W}$. Run it with the same formula. It gives 6000 W, so the formula and
arithmetic are correct. The bug is in the input.

**Step 3, check each input's units.** $A$ is 1.5 m$^2$, correct. $\Delta T$ is 20 K, correct.
$k$ is W/(m $\cdot$ K), correct. The student entered $L$ as $0.04\ \text{m}$, which is 4 cm, not 4 mm.
The pane is 0.0040 m thick.

**Step 4, isolate.** Change only $L$ from $0.04$ to $0.0040$ and rerun. The output changes from
600 W to 6000 W, a factor of 10, exactly the change expected from the unit slip.

**Step 5, fix and confirm.** The fix is to enter the thickness in meters. Rerun with the correct
value: 6000 W. As a second, independent check, double the thickness: 3000 W, half the answer,
as the formula predicts.

**Answer:** $Q = 6.0 \times 10^3\ \text{W}$. The cause was entering $L$ in centimeters instead of
meters, a factor of 10 error.

**Sanity check:** 6 kW matches the estimate from lesson 05. The corrected value passes both the
units test and the limit test.

## Practice

1. A student enters the glass thickness as 4 cm instead of 4 mm. By what factor is the
   reported heat loss wrong?
2. A student computes $v = 2gh$ for $h = 20\ \text{m}$ and forgets the square root. What value
   do they get, in m$^2$/s$^2$?
3. A student on Earth uses $g = 9.8$ instead of $9.81$ for $h = 20\ \text{m}$. The speed changes by how
   much, in m/s? Give the difference of $\sqrt{2gh}$ for the two values.

<details><summary>Answers</summary>

1. 10
2. 392.4
3. 0.010

</details>

## Common mistakes

- Changing several things at once. You will not know which change fixed the bug.
- Fixing the symptom. Multiplying the answer by 10 is not debugging.
- Trusting the code or formula without a known-good case to compare. Without one, you cannot
  separate a formula error from an input error.
- Ignoring a small discrepancy. A 2 % error can be a rounding choice, or it can be the first
  symptom of a larger missing factor. Check which.
- Declaring the bug fixed after one run. Confirm on a second input.

## Go deeper

- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: the measurement and units chapters give the unit checks used here.
- [SI units](https://www.nist.gov/pml/owm/metric-si/si-units) by NIST: the reference for the prefixes and base units to check during debugging.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: problem sets where checking a wrong answer is part of the exercise.
- Polya, *How to Solve It* (1945), a printed book on checking a solution and looking back at it. No link is given.
- [Problem-solving reference](reference.md): the lookup sheet for this topic.
