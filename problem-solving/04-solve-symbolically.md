# Solve symbolically before plugging in numbers

**Type:** lesson

Carry letters, not numbers, through the algebra for as long as you can. A symbolic answer
shows how each input affects the result, lets you check units and limits (lesson 05), and
catches errors before the arithmetic hides them. Plug in numbers only at the end.

**Prerequisites:** [Define the problem](01-define-the-problem.md), [Pick the governing principles](03-governing-principles.md)
**Time:** 3-5 h

## Core ideas

- A **symbolic solution** is an equation that gives the unknown in terms of the symbols you
  defined: $T = \dfrac{mg}{2\sin\theta}$, not $T = 283.2\ \text{N}$.
- Rearrange first, then substitute. Isolate the unknown on one side, with the knowns on the other.
- Keep the symbols until the final line. Do not round in the middle.
- The symbolic form is a formula you can reuse. Change $m$ or $\theta$ and the answer updates
  without rewriting the whole solution.
- If the algebra gets messy, stop and check your principles. A messy symbolic answer often
  means the wrong principle or a missing assumption.

### Steps

1. Write the governing equations with symbols only.
2. Solve for the unknown symbolically. Check each line.
3. Check the symbolic result with units and limits (lesson 05) before using numbers.
4. Substitute numbers with units, and compute the result.
5. Round to a sensible number of significant figures, usually two or three for engineering
   estimates.

### Why not plug in early

- Numbers hide structure. Once you have $283.2$, you cannot tell whether it depends on
  $\sin\theta$ or on $\cos\theta$.
- Rounding errors pile up. Carry full precision on a calculator, then round at the end.
- Symbolic results are easy to check. A formula that returns zero when the load is zero
  passes a basic test.

## Key equations

For the sign hung from two cables at angle $\theta$, equilibrium gives:

$$
2T\sin\theta = mg \quad\Longrightarrow\quad T = \frac{mg}{2\sin\theta}
$$

For a ball dropped from rest, with no losses:

$$
v = \sqrt{2gh}, \qquad t = \sqrt{\frac{2h}{g}}
$$

Symbols: $T$ tension (N), $m$ mass (kg), $g = 9.81\ \text{m/s}^2$, $\theta$ angle to horizontal,
$h$ height (m), $v$ speed (m/s), $t$ time (s).

## Worked example

**Problem.** A sign of mass $m = 50\ \text{kg}$ hangs from two cables, each at $\theta = 60^\circ$
to the horizontal. Find the tension $T$ in one cable.

**Given:** $m = 50\ \text{kg}$, $\theta = 60^\circ$, $g = 9.81\ \text{m/s}^2$.

**Find:** $T$ in N.

**Assumptions:** cables are massless, the load is shared equally, and the sign is at rest.

**Solution (symbolic first).**

Vertical equilibrium: the two cables each contribute $T\sin\theta$ upward, and weight $mg$ acts
down.

$$
2T\sin\theta = mg
$$

Solve for $T$:

$$
T = \frac{mg}{2\sin\theta}
$$

**Solution (now substitute).**

$$
T = \frac{50 \times 9.81}{2 \times \sin 60^\circ} = \frac{490.5}{2 \times 0.8660} = \frac{490.5}{1.732} = 283.2\ \text{N}
$$

**Answer:** $T \approx 283\ \text{N}$ in each cable.

**Sanity check:** The two cables together hold the weight, 490.5 N. Each carries 283 N, and
$2 \times 283 \times \sin 60^\circ = 490.5$ N. The check passes, and each cable carries a bit
more than half the weight because they are not vertical.

### Why the symbolic form helps

The formula $T = \dfrac{mg}{2\sin\theta}$ shows at once that $T$ grows as $\theta$ shrinks. A
shallow cable takes much more load. You get that insight without any numbers.

## Practice

1. A ball is dropped from rest from $h = 5.0\ \text{m}$. Find its speed at impact, in m/s.
   Use $v = \sqrt{2gh}$.
2. The same ball. Find the time of fall, in s. Use $t = \sqrt{2h/g}$.
3. A 50 kg sign hangs from two cables at $45^\circ$ to the horizontal. Find the tension in
   one cable, in N. Use $T = mg/(2\sin\theta)$.

<details><summary>Answers</summary>

1. 9.9 m/s
2. 1.01 s
3. 346.8 N

</details>

## Common mistakes

- Substituting numbers too early and then being unable to reuse the formula.
- Rounding intermediate values, then carrying the rounded numbers into the answer.
- Dividing by $\sin\theta$ when $\theta$ is measured from the vertical. Check which angle the
  sketch uses (lesson 02).
- Writing $\sqrt{a}\,b$ when you mean $\sqrt{ab}$. Use brackets.
- Forgetting the factor of 2 when two supports share a load.

## Go deeper

- [University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) by OpenStax: worked examples that solve for symbols before numbers.
- [Classical Mechanics (8.01SC)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) by MIT OpenCourseWare: lecture notes that derive results symbolically.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: free engineering texts, including statics chapters with symbolic solutions.
- Polya, *How to Solve It* (1945), a printed book on problem-solving steps. No link is given.
