# Graphing calculators: what the HP Prime does for engineering

**Type:** lesson

A graphing calculator such as the HP Prime handles algebra, solving, plotting, and unit conversion in your hand. It is useful in class and on exams, and it is a fast check on paper work. It does not replace understanding, and many courses limit which models you may use.

This lesson stays general. It explains the jobs a calculator like this does well, and gives a free alternative for each job. The exact menus differ by model, so read your model's manual for button steps.

**Prerequisites:** [Algebra and functions](../math/README.md)
**Time:** 4-6 h to learn the core functions

## Core ideas

- A **CAS** (computer algebra system) works with symbols. It can expand $(x+2)(x-3)$ or solve for a variable in a formula.
- A **numeric solver** finds a root of an equation $f(x) = 0$ from a starting guess. Use it when no clean algebraic answer exists.
- A **units** feature converts between systems, such as inches and millimeters, and can keep track of units through arithmetic.
- A **programming** mode lets you write short routines. Keep them simple, and check every result by hand the first time.
- **Plotting** shows a function or data set so you can check its shape, roots, and maxima.
- Exams often limit the calculator to certain functions. Check your course rules before you buy.

Free alternatives for each job:

- CAS: Python with SymPy, or GNU Octave's symbolic tools. Desmos, a free web graphing tool, covers plotting and root finding for many simple cases.
- Numeric solving: SciPy's solvers (`scipy.optimize`), in the [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/index.html).
- Units: a unit table in a notebook or a spreadsheet cell with a conversion factor.
- Plotting: Octave or Python.

See the [Python lesson](02-python.md) for a code route, and the [Octave lesson](04-matlab.md) for a free MATLAB-style route.

## Key equations

For a quadratic $ax^2 + bx + c = 0$ with $a \neq 0$:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Here $a$, $b$, and $c$ are dimensionless when $x$ is dimensionless. If $x$ carries units, $a$, $b$, and $c$ must carry units that make each term consistent.

## Worked example

**Given:** A roots problem $x^2 - 5x + 6 = 0$, where $x$ is a dimensionless ratio.

**Find:** Both roots.

**Assumptions:** Real roots only.

**Solution (run in Python with NumPy):**

```python
import numpy as np
print(np.roots([1, -5, 6]))
```

Output:

```
[3. 2.]
```

Check with the quadratic formula: $b^2 - 4ac = 25 - 24 = 1$, so $x = (5 \pm 1)/2$, giving $3$ and $2$.

**Answer:** $x = 2$ or $x = 3$.

**Sanity check:** Substitute $x = 2$: $4 - 10 + 6 = 0$. Substitute $x = 3$: $9 - 15 + 6 = 0$. Both work.

## Practice

1. Solve $x^2 - 7x + 12 = 0$ by hand. Then check it with a calculator or Python.
2. Find the root of $x^2 + 2x - 8 = 0$ with the quadratic formula. Give both roots.
3. Convert 2.5 in to millimeters. Use 1 in = 25.4 mm.
4. Plot $y = x^2 - 5x + 6$ for $x$ from 0 to 5. Mark where the curve crosses zero.
5. Explain in one sentence when a numeric solver is better than a symbolic answer.

<details><summary>Answers</summary>

1. $x = 3$ and $x = 4$
2. $x = 2$ and $x = -4$
3. 63.5 mm
4. Crossings at $x = 2$ and $x = 3$.
5. Answers will vary. A key case: the equation has no clean closed form.

</details>

## Common mistakes

- Trusting a calculator answer without substituting it back into the equation.
- Setting the calculator to the wrong angle mode (degrees vs radians) and getting a wrong trig result.
- Using a stored variable from an earlier problem without checking it.
- Forgetting that the solver finds only one root near the starting guess.
- Ignoring units in a converted answer. Write the unit beside every number.

## Go deeper

- [Paul's Online Math Notes, Algebra](https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx) by Paul Dawkins, Lamar University: solving equations by hand, which you need to check any calculator.
- [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/index.html) by the SciPy project: free root-finding and optimization tools.
- [GNU Octave manual](https://docs.octave.org/latest/) by the GNU Octave project: free numeric and plotting environment.
- Related: [Python](02-python.md), [GNU Octave and MATLAB](04-matlab.md), [starter kit](01-starter-kit.md).
