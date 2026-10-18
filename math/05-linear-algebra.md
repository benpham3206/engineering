# Linear algebra

**Type:** lesson

Linear algebra organizes many equations into one matrix equation, $\mathbf{K}\mathbf{u} = \mathbf{F}$. Engineers use it to solve truss and frame structures, circuit networks, and multi-degree-of-freedom vibration, and eigenvalues tell you natural frequencies and the stability of a system.

**Prerequisites:** [Algebra](01-algebra.md)
**Time:** 30-40 h

## Core ideas

- A vector is an ordered list of numbers. A matrix is a rectangular grid of numbers. A matrix times a vector gives a new vector.
- A system of linear equations, such as $2x + y = 5$ and $x - y = 1$, can be written as $\mathbf{A}\mathbf{x} = \mathbf{b}$. Solving it means finding $\mathbf{x}$.
- The determinant $\det(\mathbf{A})$ is a single number that tells you whether $\mathbf{A}$ can be inverted. If $\det(\mathbf{A}) = 0$, the system has no unique solution. For a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the determinant is $ad - bc$.
- Gaussian elimination is the standard hand method: use row operations to reach an upper-triangular form, then back-substitute. Software uses a close relative (LU decomposition).
- An eigenvector $\mathbf{v}$ of a square matrix $\mathbf{A}$ is a direction that the matrix only stretches, not rotates. The stretch factor $\lambda$ is the eigenvalue: $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$.
- Eigenvalues give natural frequencies in vibration. For a system with mass matrix $\mathbf{M}$ and stiffness matrix $\mathbf{K}$, the natural frequencies $\omega$ satisfy $\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$.
- Stiffness matrices in structures are symmetric. Symmetric matrices have real eigenvalues, which is why natural frequencies come out real.
- Structural rule of thumb: the stiffness matrix is built from element stiffnesses, and forces are the right-hand side. Fix the supports (remove rows and columns for fixed degrees of freedom) before solving.

## Key equations

Matrix form of a linear system:

$$\mathbf{A}\mathbf{x} = \mathbf{b}$$

Solution, when $\mathbf{A}$ is invertible:

$$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$$

Eigenvalue problem:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

Natural frequencies of an undamped system with stiffness $\mathbf{K}$ (N/m) and mass $\mathbf{M}$ (kg):

$$\det(\mathbf{K} - \omega^2\mathbf{M}) = 0$$

Symbols: $\mathbf{u}$ is the displacement vector (m), $\mathbf{F}$ is the force vector (N), $\omega$ is circular frequency (rad/s).

## Worked example

**Given:** Two masses, each $m = 1\ \mathrm{kg}$, sit in a chain: a wall, spring $k_1$, mass 1, spring $k_2$, mass 2, spring $k_3$, wall. All springs have $k = 100\ \mathrm{N/m}$. A force $F_1 = 10\ \mathrm{N}$ pushes on mass 1.

**Find:** (a) The static displacements $u_1$ and $u_2$. (b) The natural frequencies of the system.

**Assumptions:** Linear springs, no damping, small motions.

**Solution:**

Stiffness matrix for this chain, with $k_1 = k_2 = k_3 = 100$:

$$\mathbf{K} = \begin{pmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 + k_3 \end{pmatrix} = \begin{pmatrix} 200 & -100 \\ -100 & 200 \end{pmatrix}\ \mathrm{N/m}$$

(a) Solve $\mathbf{K}\mathbf{u} = \mathbf{F}$ with $\mathbf{F} = (10, 0)$ N. Solving by hand gives $200u_1 - 100u_2 = 10$ and $-100u_1 + 200u_2 = 0$, so $u_2 = u_1/2$ and $u_1 = 10/150$. The result is $u_1 = 0.0667\ \mathrm{m}$ and $u_2 = 0.0333\ \mathrm{m}$. In Python, `numpy.linalg.solve(K, F)` returns the same values.

(b) With $\mathbf{M} = \mathbf{I}$ (unit masses), the eigenvalues of $\mathbf{K}$ are $\lambda = 100$ and $300\ \mathrm{(N/m)/kg}$. The natural frequencies are $\omega = \sqrt{\lambda} = 10.00$ and $17.32\ \mathrm{rad/s}$. `numpy.linalg.eig` gives the same eigenvalues.

**Answer:** $u_1 \approx 66.7\ \mathrm{mm}$, $u_2 \approx 33.3\ \mathrm{mm}$. Natural frequencies $10.0$ and $17.3\ \mathrm{rad/s}$ (about 1.6 Hz and 2.8 Hz).

**Sanity check:** The second mass moves less than the first, which is expected because it is farther from the load. The stiffness matrix is symmetric, so its eigenvalues must be real and positive, and they are.

## Practice

1. Solve $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}\mathbf{x} = \begin{pmatrix} 9 \\ 8 \end{pmatrix}$.
2. Find the determinant of $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$.
3. Find the eigenvalues of $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
4. Find the determinant of $\begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$.

<details><summary>Answers</summary>

1. $x = 2$, $y = 3$
2. $5$
3. $1$ and $3$
4. $10$

</details>

## Common mistakes

- Forgetting that matrix multiplication is not commutative: $\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$ in general.
- Taking the determinant of a non-square matrix.
- Leaving the fixed-support degrees of freedom in the system. The stiffness matrix is singular until supports are applied.
- Solving $\mathbf{K}\mathbf{u} = \mathbf{F}$ by computing $\mathbf{K}^{-1}$ explicitly. Software solvers are more accurate and faster.
- Confusing the eigenvalue $\lambda = \omega^2$ with the frequency $\omega$. Take the square root.

## Go deeper

- [Linear Algebra (18.06)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) by MIT OpenCourseWare, taught by Gilbert Strang: full course with lectures and problem sets.
- [Linear algebra routines](https://numpy.org/doc/stable/reference/routines.linalg.html) by the NumPy project: reference for `solve`, `eig`, `inv`, and `det`.
- Next: [Differential equations](06-differential-equations.md).
