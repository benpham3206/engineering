# Software solvers

**Type:** lesson

Software does the arithmetic so you can focus on the model. The hard part is still setting up the problem correctly, checking units, and knowing whether the answer is reasonable. This lesson shows how to hand the earlier lessons' problems to Python with NumPy and SciPy, and what to check afterward.

**Prerequisites:** [Linear algebra](05-linear-algebra.md), [Numerical methods](08-numerical-methods.md), [Differential equations](06-differential-equations.md)
**Time:** 10-20 h (plus setup)

## Core ideas

- Python is free and widely used in engineering. NumPy provides arrays and linear algebra. SciPy provides integration, root finding, optimization, ODE solvers, and statistics.
- Install with `pip install numpy scipy`. Check the versions you have, because function names occasionally change between releases.
- A solver is only as good as the model you give it. Write the equations on paper first, list the units, and only then type them in.
- Keep units in comments or variable names, for example `F_N` for newtons and `L_m` for meters. Most engineering software errors are unit errors.
- Verify every software result against a simple case you can solve by hand. The worked examples in the earlier lessons are good test cases.
- Other tools work for the same jobs. MATLAB is common in industry and uses matrix notation close to the math. Spreadsheets are good for tables and quick checks. Scientific calculators are fine for single formulas. The snippets below are Python because they are the ones this folder has verified.

## Key equations

The snippets solve these, from earlier lessons:

- Linear system: $\mathbf{K}\mathbf{u} = \mathbf{F}$ (see [Linear algebra](05-linear-algebra.md))
- Root of $f(x) = 0$ (see [Numerical methods](08-numerical-methods.md))
- Integral $\int_0^L P(L-x)^2/(EI)\,dx$ for beam deflection (see [Single-variable calculus](03-single-variable-calculus.md))
- Cooling ODE $dT/dt = -k(T - T_a)$ (see [Differential equations](06-differential-equations.md))

## Worked example

**Given:** The four problems from the earlier lessons, with the values used there.

**Find:** Solve each one in Python and compare with the hand results.

**Assumptions:** The same as in the source lessons.

**Solution:** This script was run in this folder. It uses NumPy 2.5.1 and SciPy 1.18.0.

```python
import numpy as np
from scipy import integrate, optimize
from scipy.integrate import solve_ivp

# 1. Linear system: two-mass spring chain (stiffness in N/m)
K = np.array([[200.0, -100.0],
              [-100.0, 200.0]])
F = np.array([10.0, 0.0])
u = np.linalg.solve(K, F)
print("displacements (m):", np.round(u, 4))
print("eigenvalues:", np.round(np.linalg.eigvalsh(K), 2))

# 2. Root finding: x^3 - 2x - 5 = 0
root = optimize.newton(lambda x: x**3 - 2*x - 5, x0=2.0,
                       fprime=lambda x: 3*x**2 - 2)
print("root:", round(root, 7))

# 3. Integral: tip deflection of a cantilever, P=1000 N, L=2 m, E=200 GPa, I=bh^3/12
P, L, E = 1000.0, 2.0, 200e9
I = 0.05 * 0.10**3 / 12
delta, _ = integrate.quad(lambda x: P * (L - x)**2 / (E * I), 0, L)
print("tip deflection (mm):", round(delta * 1000, 3))

# 4. ODE: cooling from 180 C in 25 C air, k = 0.04895 1/min
k = 0.04895
sol = solve_ivp(lambda t, T: -k * (T - 25.0), [0, 47.7], [180.0],
                rtol=1e-10, atol=1e-10)
print("temperature at 47.7 min (C):", round(sol.y[0, -1], 2))
```

Output from that run:

```
displacements (m): [0.0667 0.0333]
eigenvalues: [100. 300.]
root: 2.0945515
tip deflection (mm): 3.2
temperature at 47.7 min (C): 40.01
```

**Answer:** The results match the hand solutions: $u = (0.0667, 0.0333)$ m, eigenvalues $100$ and $300$, root $2.0945515$, tip deflection $3.2$ mm.

The cooling check gives $40.01^\circ\mathrm{C}$, not $40.00$. The difference comes from rounding $k$ to $0.04895$ in the script. With the unrounded $k = \ln(155/95)/10$, the result is $40.00^\circ\mathrm{C}$. Keep full precision inside a calculation and round only at the end.

**Sanity check:** Compare each output with a hand estimate before you trust it. Here each value matched the lesson in which it was derived. When a new model gives a result you cannot check by hand, test the code on one of these known cases first.

## Practice

1. Change the spring stiffness in the linear system to $k = 150\ \mathrm{N/m}$ for all three springs. Predict the new $u_1$ by scaling the old result, then check it in Python. (Hint: the displacement scales as $1/k$.)
2. Use `optimize.brentq` to find the root of $\cos x - x = 0$ on $[0, 1]$. Give the root to four decimal places.
3. Use `integrate.quad` to evaluate $\int_0^{\pi} \sin x\,dx$. Give the result.
4. Run `solve_ivp` for $y' = -2y$ with $y(0) = 5$ from $t = 0$ to $t = 1$. Give $y(1)$ to four decimal places.

<details><summary>Answers</summary>

1. $u_1 \approx 0.0444\ \mathrm{m}$ (scale $0.0667 \times 100/150$)
2. $x \approx 0.7391$
3. $2.0$
4. $y(1) \approx 0.6767$

</details>

## Common mistakes

- Typing a formula with the wrong power or missing parentheses, such as `x**3 - 2*x - 5` written as `x^3`. In Python, `^` is bitwise XOR, not exponent.
- Mixing mm and m in the same script. Pick SI units and convert inputs once.
- Rounding a constant too early, which changes the answer in the fourth digit.
- Trusting a solver's output without a sanity check. Solvers return numbers even for a wrong model.
- Using `np.linalg.inv` to solve a system when `np.linalg.solve` is faster and more accurate.

## Go deeper

- [SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/index.html) by the SciPy project: integration, optimization, linear algebra, and ODE solvers with examples.
- [NumPy linear algebra routines](https://numpy.org/doc/stable/reference/routines.linalg.html) by the NumPy project: reference for `solve`, `eig`, `inv`, and `det`.
- Next: return to [Algebra](01-algebra.md) or the [math folder README](README.md) to choose the next topic.
