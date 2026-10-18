# MATLAB and GNU Octave

**Type:** lesson

MATLAB is a paid numerical computing language used across engineering for matrices, simulations, signal processing, and control. Engineers use it because the matrix syntax is short and the toolboxes are deep. GNU Octave is a free program that runs most of the same basic code, so you can learn the core skills without a license.

**Prerequisites:** [Python for engineering calculations](02-python.md) (recommended), [algebra and functions](../math/README.md), [linear algebra](../math/README.md)
**Time:** 8-12 h for core matrix and plotting skills

## Core ideas

- MATLAB and Octave work on **matrices** first. A scalar is a 1 by 1 matrix.
- Use `A*b` for matrix multiplication and `A\b` to solve $A\mathbf{x} = \mathbf{b}$.
- Use `.*` and `./` for element-by-element operations on vectors.
- Indices start at 1, not 0.
- A semicolon at the end of a line hides the output.
- Scripts (`.m` files) hold a sequence of commands. Functions take inputs and return outputs.
- Octave is free. Its base language covers most homework. Some MATLAB toolboxes have no free equivalent, so check what your course needs.

Read the [GNU Octave manual](https://docs.octave.org/latest/). Its early chapters, "A Brief Introduction to Octave" and "Getting Started", cover the basics.

## Key equations

For a linear system with $n$ unknowns:

$$A\mathbf{x} = \mathbf{b}$$

Here $A$ is an $n \times n$ coefficient matrix, $\mathbf{x}$ is the unknown vector, and $\mathbf{b}$ is the known right-hand side. Units follow the rows of $\mathbf{b}$. If $\mathbf{b}$ is a force in N, then $\mathbf{x}$ is in N as well, and $A$ is dimensionless.

## Worked example

**Given:** A joint has two member forces $F_1$ and $F_2$ (N). The vertical balance is $F_1 + F_2 = 1000$ N. A simplified horizontal balance gives $0.5 F_1 - 0.8 F_2 = 0$.

**Find:** $F_1$ and $F_2$.

**Assumptions:** Simplified geometry as given. Forces are positive in tension.

**Solution (run in Python with NumPy, which uses the same solver idea as Octave):**

```python
import numpy as np
A = np.array([[1.0, 1.0], [0.5, -0.8]])
b = np.array([1000.0, 0.0])
x = np.linalg.solve(A, b)
print("x =", x)
print("check A@x =", A @ x)
```

Output:

```
x = [615.38461538 384.61538462]
check A@x = [1.00000000e+03 5.68434189e-14]
```

The Octave equivalent is `x = A\b`. This lesson did not run it, because Octave is not installed on the machine used to prepare it.

**Answer:** $F_1 \approx 615$ N and $F_2 \approx 385$ N.

**Sanity check:** The two forces add to 1000 N ($615.4 + 384.6 = 1000.0$). Check the second equation: $0.5 \times 615.4 - 0.8 \times 384.6 = 307.7 - 307.7 = 0$. The residual in the check vector is about $10^{-14}$, which is rounding.

## Practice

1. Solve $2x + y = 5$ and $x - y = 1$. Give $x$ and $y$.
2. Change the right-hand side to $[1000; 100]$ and solve again. Report $F_1$ and $F_2$ to the nearest newton.
3. Write an Octave or MATLAB line that prints $A \cdot x$ and compares it with $b$. Explain why the check matters.
4. Plot $y = \sin(x)$ for $x$ from 0 to $2\pi$ with 200 points. Label both axes with units.
5. Explain in one sentence why `A\b` is preferred to `inv(A)*b`.

<details><summary>Answers</summary>

1. $x = 2$, $y = 1$
2. $F_1 \approx 692$ N and $F_2 \approx 308$ N. Substituting $F_2 = 1000 - F_1$ into the second equation gives $1.3 F_1 = 900$. Check that $F_1 + F_2 = 1000$.
3. Check the residual is near zero.
4. Plot check: one full sine wave.
5. Answers will vary. A key point: `A\b` is faster and more accurate.

</details>

## Common mistakes

- Using `*` when you need `.*` for element-by-element products.
- Forgetting that indices start at 1.
- Solving a system with a matrix that is singular or nearly singular, and not checking the result.
- Forgetting to label plots with units.
- Leaving out the semicolon, then reading a wall of output.

## Go deeper

- [GNU Octave manual](https://docs.octave.org/latest/) by the GNU Octave project: free official reference.
- [MIT 6.0001 Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) by MIT OpenCourseWare: a free course on the programming ideas that carry over to MATLAB.
- [Paul's Online Math Notes, Algebra](https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx) by Paul Dawkins, Lamar University: review for the algebra behind each system.
- Related: [Python](02-python.md), [spreadsheets](03-spreadsheets.md), [HP Prime](05-hp-prime.md).
