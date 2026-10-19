# Linear algebra and differential equations reference

**Type:** reference
**Verify:** strict

Lookup sheet for matrix algebra, linear systems, eigenvalue problems, ordinary differential equations, the Laplace and Fourier transforms, and the standard partial differential equations, for an engineer who needs a formula, a method, or a check in the middle of a job.

## Principles

- A linear system has no solution, exactly one, or infinitely many. It never has exactly two. Rank decides which.
- Solve $\mathbf{A}\mathbf{x} = \mathbf{b}$ by factoring, never by forming $\mathbf{A}^{-1}$. A factorization is cheaper, and it is more accurate.
- A small determinant does not mean a nearly singular matrix. Scaling every entry changes the determinant but not the conditioning. Use the condition number.
- Eigenvalues of a real symmetric matrix are real, and its eigenvectors can be chosen orthogonal. Nonsymmetric matrices can have complex eigenvalues and too few eigenvectors.
- A linear constant-coefficient system is stable when every eigenvalue (or characteristic root, or pole) has a negative real part.
- Superposition is the reason linear problems are solvable. The general solution is a particular solution plus the homogeneous solution.
- A differential equation without initial or boundary conditions describes a family of functions. State the conditions before reporting a number.
- A transform turns calculus into algebra on a restricted class of functions. State the convention, the region of validity, and the conditions before using a theorem.
- The type of a partial differential equation (elliptic, parabolic, hyperbolic) decides which boundary and initial conditions make the problem well posed.
- The variables tables in this sheet give an SI unit where physics fixes one (time in s, length in m, a rate in 1/s) and list generic matrix entries, functions, and coefficients as dimensionless. In an application each takes the unit of the quantity it represents, and every equation must be dimensionally consistent.

## Vectors and matrices

A **matrix** is a rectangular array of numbers that represents a linear map; a **vector** is a matrix with one column. Engineers use matrices to write many coupled linear equations as one statement.

### Dot product and norm

The dot product of two vectors measures how much one points along the other, and the norm is the length.

$$\mathbf{u}\cdot\mathbf{v} = \sum_{i} u_i v_i = \lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\theta \qquad \lVert\mathbf{u}\rVert = \sqrt{\mathbf{u}\cdot\mathbf{u}}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{u}$, $\mathbf{v}$ | vectors with the same number of components | dimensionless |
| $u_i$, $v_i$ | components of the vectors | dimensionless |
| $\theta$ | angle between the vectors | rad |

Holds when: both vectors are in the same Euclidean space and components are on orthonormal axes with the same units.
Breaks when: the axes are not orthonormal (use the metric matrix) or the components mix units (the dot product then has no meaning).
Source and basis: derived from the law of cosines; taught in [Linear algebra](05-linear-algebra.md).

Example: $\mathbf{u} = (3, 4)$ and $\mathbf{v} = (4, -3)$ have $\mathbf{u}\cdot\mathbf{v} = 0$, so they are perpendicular, and $\lVert\mathbf{u}\rVert = 5$.

<details><summary>Verification</summary>

```verify
u1 = q(3, "")
u2 = q(4, "")
v1 = q(4, "")
v2 = q(-3, "")
expect(u1 * v1 + u2 * v2, "0")
expect(sqrt(u1**2 + u2**2), "5")
```

</details>

### Matrix product, transpose, and inverse

The product of an $n \times r$ matrix and an $r \times p$ matrix is the $n \times p$ matrix whose entry is a row of the first dotted with a column of the second. The **transpose** swaps rows and columns, and the **inverse** undoes the matrix.

$$(\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^{r} A_{ik}B_{kj} \qquad (\mathbf{A}\mathbf{B})^{\mathsf{T}} = \mathbf{B}^{\mathsf{T}}\mathbf{A}^{\mathsf{T}} \qquad (\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | matrix with $n$ rows and $r$ columns | dimensionless |
| $\mathbf{B}$ | matrix with $r$ rows and $p$ columns | dimensionless |
| $A_{ik}$, $B_{kj}$ | entries of $\mathbf{A}$ and $\mathbf{B}$ | dimensionless |
| $i$, $j$, $k$ | row, column, and summation indices | dimensionless |

Holds when: the inner sizes match. The inverse rule needs both $\mathbf{A}$ and $\mathbf{B}$ square and invertible.
Breaks when: you assume $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$ (it fails in general) or cancel a matrix that has no inverse.
Source and basis: derived from the definition of composition of linear maps; taught in [Linear algebra](05-linear-algebra.md).

Example: with $\mathbf{A} = \begin{pmatrix}2&1\\1&3\end{pmatrix}$ and $\mathbf{x} = (1, 2)^{\mathsf T}$, the product $\mathbf{A}\mathbf{x} = (4, 7)^{\mathsf T}$. The reversed product $\mathbf{x}^{\mathsf T}\mathbf{A}$ is the transpose of $\mathbf{A}^{\mathsf T}\mathbf{x}$, which equals $\mathbf{A}\mathbf{x}$ here because $\mathbf{A}$ is symmetric.

<details><summary>Verification</summary>

```verify
a11 = q(2, "")
a12 = q(1, "")
a21 = q(1, "")
a22 = q(3, "")
x1 = q(1, "")
x2 = q(2, "")
expect(a11 * x1 + a12 * x2, "4")
expect(a21 * x1 + a22 * x2, "7")
check(a12 == a21, "A is symmetric")
```

</details>

### Determinant and inverse

The **determinant** is the factor by which a square matrix scales volume, and it is zero exactly when the matrix has no inverse.

$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc \qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $a$, $b$, $c$, $d$ | entries of a $2 \times 2$ matrix | dimensionless |

Holds when: the matrix is $2 \times 2$ and $ad - bc \ne 0$ for the inverse.
Breaks when: the matrix is larger (use cofactor expansion for $3 \times 3$ by hand, and factorization beyond that) or the determinant is near zero compared with the size of the entries (the inverse then amplifies error, see conditioning below).
Source and basis: derived from the definition of the determinant as signed area; taught in [Linear algebra](05-linear-algebra.md).

Rules that hold for any square matrices of the same size:

- $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$, and $\det\mathbf{A}^{\mathsf{T}} = \det\mathbf{A}$.
- Swapping two rows flips the sign. Adding a multiple of one row to another changes nothing. Scaling one row scales the determinant by the same factor.
- $\det\mathbf{A}$ equals the product of the eigenvalues, and it equals the product of the pivots of Gaussian elimination, times $(-1)$ for each row swap.
- $\mathbf{A}$ is invertible if and only if $\det\mathbf{A} \ne 0$.

Example: for $\mathbf{A} = \begin{pmatrix}2&1\\1&3\end{pmatrix}$, $\det\mathbf{A} = 5$ and $\mathbf{A}^{-1} = \tfrac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$, whose first row is $(0.6, -0.2)$. The first row of $\mathbf{A}$ times the first column of $\mathbf{A}^{-1}$ is $2(0.6) + 1(-0.2) = 1$.

<details><summary>Verification</summary>

```verify
a = q(2, "")
b = q(1, "")
c = q(1, "")
d = q(3, "")
det = a * d - b * c
expect(det, "5")
expect(d / det, "0.6")
expect(-b / det, "-0.2")
expect(a * (d / det) + b * (-c / det), "1")
```

</details>

### Rank and null space

The **rank** of a matrix is the number of linearly independent columns (equal to the number of independent rows), and its **null space** is the set of vectors it sends to zero.

$$\operatorname{rank}(\mathbf{A}) + \dim\operatorname{null}(\mathbf{A}) = n$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | matrix with $n$ columns | dimensionless |
| $n$ | number of columns of $\mathbf{A}$ | dimensionless |

Holds when: $\mathbf{A}$ is any matrix with $n$ columns, over the real or complex numbers.
Breaks when: rank is computed in floating point by counting nonzero pivots. Rounding makes a tiny pivot nonzero, so count singular values above a stated tolerance instead.
Source and basis: derived from the rank-nullity theorem for linear maps; taught in [Linear algebra](05-linear-algebra.md).

- For $\mathbf{A}\mathbf{x} = \mathbf{b}$ with $\mathbf{A}$ of size $n \times n$: if rank is $n$, there is one solution for every $\mathbf{b}$. If rank is below $n$, a solution exists only when $\mathbf{b}$ lies in the column space, and then there are infinitely many.
- The rank equals the number of pivots after elimination.

Example: the rows $(2, 0, 1)$, $(1, 3, 2)$, $(1, 1, 1)$ satisfy row 2 $= -1\,(\text{row }1) + 3\,(\text{row }3)$, so the determinant is 0 and the rank is 2, which leaves a null space of dimension 1.

<details><summary>Verification</summary>

```verify
r1a = q(2, "")
r1b = q(0, "")
r1c = q(1, "")
r2a = q(1, "")
r2b = q(3, "")
r2c = q(2, "")
r3a = q(1, "")
r3b = q(1, "")
r3c = q(1, "")
det = r1a * (r2b * r3c - r2c * r3b) - r1b * (r2a * r3c - r2c * r3a) + r1c * (r2a * r3b - r2b * r3a)
expect(det, "0")
check(r2a == -r1a + 3 * r3a, "column 1 dependency")
check(r2b == -r1b + 3 * r3b, "column 2 dependency")
check(r2c == -r1c + 3 * r3c, "column 3 dependency")
```

</details>

## Linear systems and factorizations

A **factorization** writes a matrix as a product of simpler matrices, so that a hard solve becomes a few easy ones. Triangular systems solve by substitution in about $n^2$ operations, so every method below reduces to them.

| Factorization | Form | Applies to | Use it for | Cost (square, $n \times n$) |
|---|---|---|---|---|
| LU with partial pivoting | $\mathbf{P}\mathbf{A} = \mathbf{L}\mathbf{U}$ | any square invertible matrix | general linear solves, determinants, many right-hand sides | $\tfrac{2}{3}n^3$ |
| Cholesky | $\mathbf{A} = \mathbf{L}\mathbf{L}^{\mathsf{T}}$ | symmetric positive definite | stiffness and covariance matrices, least squares by normal equations | $\tfrac{1}{3}n^3$ |
| QR | $\mathbf{A} = \mathbf{Q}\mathbf{R}$ | any matrix | least squares, orthogonal bases, eigenvalue algorithms | $\tfrac{4}{3}n^3$ (Householder) |
| SVD | $\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\mathsf{T}}$ | any matrix | rank, conditioning, pseudo-inverse, rank-deficient least squares | several times QR |

Costs are leading terms in multiply-add operations counted as 2 floating-point operations each, so they set the scaling with $n$ and not an exact count on a given machine.

### LU factorization and Gaussian elimination

**Gaussian elimination** subtracts multiples of one row from the rows below to make zeros under each pivot. Recording the multipliers gives the lower triangle $\mathbf{L}$, and what is left is the upper triangle $\mathbf{U}$.

$$\mathbf{P}\mathbf{A} = \mathbf{L}\mathbf{U}, \qquad \mathbf{L}\mathbf{y} = \mathbf{P}\mathbf{b}, \qquad \mathbf{U}\mathbf{x} = \mathbf{y}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | square coefficient matrix | dimensionless |
| $\mathbf{P}$ | permutation matrix that records row swaps | dimensionless |
| $\mathbf{L}$ | lower triangular matrix with unit diagonal | dimensionless |
| $\mathbf{U}$ | upper triangular matrix | dimensionless |
| $\mathbf{b}$, $\mathbf{x}$, $\mathbf{y}$ | right-hand side, solution, intermediate vector | dimensionless |

Holds when: $\mathbf{A}$ is square and invertible. Partial pivoting (swap in the largest available entry in the column) keeps the multipliers at or below 1 in size and makes the method reliable in practice.
Breaks when: $\mathbf{A}$ is singular (a pivot is zero for every swap), or the matrix is badly scaled so that pivot choice no longer reflects size. Without pivoting a tiny pivot destroys accuracy.
Source and basis: derived from row operations as multiplication by elementary matrices; taught in [Linear algebra](05-linear-algebra.md).

Factor once, then solve each new $\mathbf{b}$ for the cost of two triangular solves. Example: $\mathbf{A} = \begin{pmatrix}2&1\\4&5\end{pmatrix}$ gives the multiplier $4/2 = 2$, so $\mathbf{L} = \begin{pmatrix}1&0\\2&1\end{pmatrix}$ and $\mathbf{U} = \begin{pmatrix}2&1\\0&3\end{pmatrix}$. For $\mathbf{b} = (3, 9)^{\mathsf{T}}$, forward substitution gives $\mathbf{y} = (3, 3)^{\mathsf{T}}$, and back substitution gives $x_2 = 1$ and $x_1 = 1$. The determinant is the product of the pivots, $2 \times 3 = 6$.

<details><summary>Verification</summary>

```verify
a11 = q(2, "")
a12 = q(1, "")
a21 = q(4, "")
a22 = q(5, "")
b1 = q(3, "")
b2 = q(9, "")
m = a21 / a11
expect(m, "2")
u22 = a22 - m * a12
expect(u22, "3")
y1 = b1
y2 = b2 - m * y1
expect(y2, "3")
x2 = y2 / u22
x1 = (y1 - a12 * x2) / a11
expect(x2, "1")
expect(x1, "1")
expect(a11 * u22, "6")
check(a21 * x1 + a22 * x2 == b2, "residual closes")
```

</details>

### Cholesky factorization

The **Cholesky factorization** writes a symmetric positive definite matrix as a lower triangular matrix times its own transpose. It is the cheapest factorization and needs no pivoting.

$$\mathbf{A} = \mathbf{L}\mathbf{L}^{\mathsf{T}}, \qquad L_{jj} = \sqrt{A_{jj} - \sum_{k<j} L_{jk}^2}, \qquad L_{ij} = \frac{1}{L_{jj}}\Big(A_{ij} - \sum_{k<j} L_{ik}L_{jk}\Big)\ \ (i > j)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | symmetric positive definite matrix | dimensionless |
| $\mathbf{L}$ | lower triangular factor with positive diagonal | dimensionless |
| $A_{ij}$, $L_{ij}$ | entries of $\mathbf{A}$ and $\mathbf{L}$ | dimensionless |
| $i$, $j$, $k$ | row, column, and summation indices | dimensionless |

Holds when: $\mathbf{A}$ is symmetric and every eigenvalue is positive. The factorization succeeds exactly when that is true, so a failed Cholesky is a test for positive definiteness.
Breaks when: $\mathbf{A}$ is only positive semidefinite or indefinite (a square root of zero or of a negative number appears), or $\mathbf{A}$ is not symmetric.
Source and basis: derived from LU factorization of a symmetric positive definite matrix; taught in [Linear algebra](05-linear-algebra.md).

Example: $\mathbf{A} = \begin{pmatrix}4&2\\2&5\end{pmatrix}$ gives $L_{11} = 2$, $L_{21} = 2/2 = 1$, and $L_{22} = \sqrt{5 - 1} = 2$. Then $\mathbf{L}\mathbf{L}^{\mathsf{T}}$ has top-left entry $4$ and off-diagonal entry $2$, matching $\mathbf{A}$.

<details><summary>Verification</summary>

```verify
a11 = q(4, "")
a21 = q(2, "")
a22 = q(5, "")
l11 = sqrt(a11)
l21 = a21 / l11
l22 = sqrt(a22 - l21**2)
expect(l11, "2")
expect(l21, "1")
expect(l22, "2")
expect(l11**2, "4")
expect(l21 * l11, "2")
expect(l21**2 + l22**2, "5")
```

</details>

### QR factorization

The **QR factorization** writes a matrix as an orthogonal matrix $\mathbf{Q}$ (columns of length 1 and mutually perpendicular) times an upper triangular matrix $\mathbf{R}$. Orthogonal matrices do not amplify error, so QR is the stable way to solve least squares.

$$\mathbf{A} = \mathbf{Q}\mathbf{R}, \qquad \mathbf{Q}^{\mathsf{T}}\mathbf{Q} = \mathbf{I}, \qquad R_{ij} = \mathbf{q}_i\cdot\mathbf{a}_j\ \ (i < j), \qquad R_{jj} = \Big\lVert \mathbf{a}_j - \sum_{i<j} R_{ij}\mathbf{q}_i \Big\rVert$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | matrix with linearly independent columns | dimensionless |
| $\mathbf{Q}$ | matrix with orthonormal columns | dimensionless |
| $\mathbf{R}$ | upper triangular matrix | dimensionless |
| $\mathbf{a}_j$, $\mathbf{q}_i$ | columns of $\mathbf{A}$ and $\mathbf{Q}$ | dimensionless |
| $R_{ij}$ | entry of $\mathbf{R}$ | dimensionless |

Holds when: the columns of $\mathbf{A}$ are independent. The formula shown is Gram-Schmidt, which explains the structure; production software uses Householder reflections for accuracy.
Breaks when: columns are nearly dependent (classical Gram-Schmidt then loses orthogonality, so use Householder reflections), or $\mathbf{A}$ has dependent columns (a diagonal entry $R_{jj}$ is zero; use pivoted QR or the SVD).
Source and basis: derived from Gram-Schmidt orthogonalization; taught in [Linear algebra](05-linear-algebra.md).

Example: the columns $\mathbf{a}_1 = (3, 4)$ and $\mathbf{a}_2 = (1, 2)$ give $R_{11} = 5$, $\mathbf{q}_1 = (0.6, 0.8)$, $R_{12} = 0.6 + 1.6 = 2.2$, and the remainder $\mathbf{a}_2 - 2.2\,\mathbf{q}_1 = (-0.32, 0.24)$ has length $R_{22} = 0.4$. The product $R_{11}R_{22} = 2$ equals $\lvert\det\mathbf{A}\rvert = \lvert 3(2) - 1(4)\rvert$.

<details><summary>Verification</summary>

```verify
a1x = q(3, "")
a1y = q(4, "")
a2x = q(1, "")
a2y = q(2, "")
r11 = sqrt(a1x**2 + a1y**2)
expect(r11, "5")
q1x = a1x / r11
q1y = a1y / r11
expect(q1x, "0.6")
expect(q1y, "0.8")
expect(q1x * a2x, "0.6")
expect(q1y * a2y, "1.6")
r12 = q1x * a2x + q1y * a2y
expect(r12, "2.2")
ex = a2x - r12 * q1x
ey = a2y - r12 * q1y
expect(ex, "-0.32")
expect(ey, "0.24")
r22 = sqrt(ex**2 + ey**2)
expect(r22, "0.4")
expect(r11 * r22, "2")
expect(abs(a1x * a2y - a2x * a1y), "2")
```

</details>

## Least squares and SVD

**Least squares** finds the $\mathbf{x}$ that makes $\mathbf{A}\mathbf{x}$ closest to $\mathbf{b}$ when there are more equations than unknowns and no exact solution exists. It is how a line or curve is fit to measured data.

### Normal equations

The best fit makes the residual perpendicular to every column of $\mathbf{A}$.

$$\mathbf{A}^{\mathsf{T}}\mathbf{A}\,\hat{\mathbf{x}} = \mathbf{A}^{\mathsf{T}}\mathbf{b}, \qquad \mathbf{A}^{\mathsf{T}}(\mathbf{b} - \mathbf{A}\hat{\mathbf{x}}) = \mathbf{0}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | model matrix with more rows than columns | dimensionless |
| $\mathbf{b}$ | measured data vector | dimensionless |
| $\hat{\mathbf{x}}$ | least-squares parameter vector | dimensionless |
| $\mathbf{r} = \mathbf{b} - \mathbf{A}\hat{\mathbf{x}}$ | residual vector | dimensionless |

Holds when: the columns of $\mathbf{A}$ are independent, so $\mathbf{A}^{\mathsf{T}}\mathbf{A}$ is invertible, and the data errors are roughly equal in size and independent.
Breaks when: the columns are nearly dependent, because forming $\mathbf{A}^{\mathsf{T}}\mathbf{A}$ squares the condition number and can lose half the digits. Use QR or the SVD instead. Outliers also dominate the fit, and unequal errors need weights.
Source and basis: derived from minimizing $\lVert\mathbf{b} - \mathbf{A}\mathbf{x}\rVert^2$ by setting its gradient to zero; taught in [Linear algebra](05-linear-algebra.md).

Example: fit $y = c_0 + c_1 x$ to the points $(0, 1)$, $(1, 2)$, $(2, 2)$. Then $\mathbf{A}^{\mathsf{T}}\mathbf{A} = \begin{pmatrix}3&3\\3&5\end{pmatrix}$ and $\mathbf{A}^{\mathsf{T}}\mathbf{b} = (5, 6)^{\mathsf{T}}$, with determinant 6. The solution is $c_0 = 7/6 = 1.1667$ and $c_1 = 0.5$. The residuals $(-0.1667, 0.3333, -0.1667)$ sum to zero, and the residuals weighted by $x$ also sum to zero, as orthogonality requires.

<details><summary>Verification</summary>

```verify
n = q(3, "")
sx = q(3, "")
sxx = q(5, "")
sy = q(5, "")
sxy = q(6, "")
det = n * sxx - sx * sx
expect(det, "6")
c0 = (sxx * sy - sx * sxy) / det
c1 = (n * sxy - sx * sy) / det
expect(c0, "1.1667")
expect(c1, "0.5")
r0 = 1 - c0
r1 = 2 - (c0 + c1)
r2 = 2 - (c0 + 2 * c1)
expect(r0, "-0.1667")
expect(r1, "0.3333")
expect(r2, "-0.1667")
check(abs(r0 + r1 + r2) < 1e-9, "residuals sum to zero")
check(abs(r1 + 2 * r2) < 1e-9, "residuals orthogonal to x")
```

</details>

### Singular value decomposition and pseudo-inverse

The **singular value decomposition (SVD)** writes any matrix as a rotation, a stretch along perpendicular axes, and another rotation. The stretch factors are the **singular values**. The **pseudo-inverse** uses them to give the minimum-norm least-squares solution for any matrix, including rank-deficient ones.

$$\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\mathsf{T}}, \qquad \mathbf{A}^{+} = \mathbf{V}\boldsymbol{\Sigma}^{+}\mathbf{U}^{\mathsf{T}}, \qquad \hat{\mathbf{x}} = \mathbf{A}^{+}\mathbf{b}, \qquad \sigma_i = \sqrt{\lambda_i(\mathbf{A}^{\mathsf{T}}\mathbf{A})}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{U}$, $\mathbf{V}$ | orthogonal matrices of left and right singular vectors | dimensionless |
| $\boldsymbol{\Sigma}$ | diagonal matrix of singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$ | dimensionless |
| $\boldsymbol{\Sigma}^{+}$ | diagonal matrix with $1/\sigma_i$ for each nonzero $\sigma_i$ and zero otherwise | dimensionless |
| $\mathbf{A}^{+}$ | Moore-Penrose pseudo-inverse | dimensionless |
| $\lambda_i(\mathbf{A}^{\mathsf{T}}\mathbf{A})$ | eigenvalues of $\mathbf{A}^{\mathsf{T}}\mathbf{A}$ | dimensionless |

Holds when: $\mathbf{A}$ is any real matrix. The rank $r$ is the number of singular values above a tolerance. For a full-rank matrix the 2-norm condition number is $\sigma_1/\sigma_{\min(m,n)}$. For a rank-deficient matrix, $\sigma_1/\sigma_r$ is the condition number of the truncated problem that $\mathbf{A}^{+}$ solves, not of $\mathbf{A}$ itself.
Breaks when: singular values are not well separated from zero (the rank is then a judgment, so state the tolerance), or the columns of $\mathbf{A}$ have unlike units so that the singular values mix them. Scale the columns first.
Source and basis: derived from the spectral theorem applied to $\mathbf{A}^{\mathsf{T}}\mathbf{A}$; taught in [Linear algebra](05-linear-algebra.md).

Example: for the line-fit matrix above, $\mathbf{A}^{\mathsf{T}}\mathbf{A}$ has trace 8 and determinant 6, so its eigenvalues are $7.162$ and $0.8377$. The singular values are $2.676$ and $0.9153$, and the 2-norm condition number is $2.924$.

<details><summary>Verification</summary>

```verify
tr = q(8, "")
det = q(6, "")
disc = sqrt(tr**2 / 4 - det)
l1 = tr / 2 + disc
l2 = tr / 2 - disc
s1 = sqrt(l1)
s2 = sqrt(l2)
expect(l1, "7.162")
expect(l2, "0.8377")
expect(s1, "2.676")
expect(s2, "0.9153")
expect(s1 / s2, "2.924")
expect(l1 * l2, "6")
```

</details>

## Eigenvalue problems

An **eigenvector** of a square matrix is a direction the matrix only stretches, and the stretch factor is the **eigenvalue**. They give natural frequencies, principal stresses, and the modes in which a linear system moves.

### Characteristic equation

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}, \qquad \det(\mathbf{A} - \lambda\mathbf{I}) = 0, \qquad \sum_i \lambda_i = \operatorname{tr}\mathbf{A}, \qquad \prod_i \lambda_i = \det\mathbf{A}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{A}$ | square matrix | dimensionless |
| $\mathbf{v}$ | eigenvector (nonzero) | dimensionless |
| $\lambda$ | eigenvalue | dimensionless |
| $\mathbf{I}$ | identity matrix | dimensionless |

Holds when: $\mathbf{A}$ is square. The characteristic polynomial has degree $n$, so there are $n$ eigenvalues counted with multiplicity, real or complex.
Breaks when: $n$ is large (finding roots of the polynomial is unstable; use QR iterations), or eigenvalues are repeated (the number of independent eigenvectors can be fewer than the multiplicity).
Source and basis: derived from requiring $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ to have a nonzero solution; taught in [Linear algebra](05-linear-algebra.md).

For a $2 \times 2$ matrix the equation is $\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0$. For a generalized problem $\mathbf{K}\mathbf{v} = \lambda\mathbf{M}\mathbf{v}$ with $\mathbf{M}$ positive definite, the eigenvalues are the squares of the angular natural frequencies, $\lambda = \omega_n^2$ in $\text{rad}^2/\text{s}^2$, so $f_n = \sqrt{\lambda}/(2\pi)$ in Hz; see [Vibrations reference](../physics/reference-vibrations.md).

Example: for $\mathbf{A} = \begin{pmatrix}2&1\\1&3\end{pmatrix}$, the trace is 5 and the determinant is 5, so $\lambda = (5 \pm \sqrt{5})/2$, which is $3.618$ and $1.382$. The eigenvector for $\lambda_1$ has $v_2 = (\lambda_1 - 2)v_1 = 1.618\,v_1$, and the first row check $2(1) + 1(1.618) = 3.618$ equals $\lambda_1 v_1$.

<details><summary>Verification</summary>

```verify
tr = q(5, "")
det = q(5, "")
disc = sqrt(tr**2 - 4 * det)
l1 = (tr + disc) / 2
l2 = (tr - disc) / 2
expect(l1, "3.618")
expect(l2, "1.382")
expect(l1 + l2, "5")
expect(l1 * l2, "5")
v2 = l1 - 2
expect(v2, "1.618")
expect(2 * 1 + 1 * v2, "3.618")
```

</details>

### Diagonalization and symmetric matrices

A matrix with $n$ independent eigenvectors can be **diagonalized**, which makes powers and functions of the matrix easy. A real symmetric matrix always can be, with orthogonal eigenvectors.

$$\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}, \qquad \mathbf{A}^{k} = \mathbf{V}\boldsymbol{\Lambda}^{k}\mathbf{V}^{-1}, \qquad \mathbf{A} = \mathbf{A}^{\mathsf{T}} \Rightarrow \mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\mathsf{T}}, \qquad \lambda_{\min} \le \frac{\mathbf{x}^{\mathsf{T}}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\mathsf{T}}\mathbf{x}} \le \lambda_{\max}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{V}$ | matrix whose columns are eigenvectors | dimensionless |
| $\boldsymbol{\Lambda}$ | diagonal matrix of eigenvalues | dimensionless |
| $\mathbf{Q}$ | orthogonal matrix of unit eigenvectors of a symmetric matrix | dimensionless |
| $k$ | integer power | dimensionless |
| $\mathbf{x}$ | any nonzero vector | dimensionless |

Holds when: $\mathbf{A}$ has a full set of independent eigenvectors. A symmetric matrix has real eigenvalues, and a symmetric matrix is positive definite exactly when all its eigenvalues are positive.
Breaks when: $\mathbf{A}$ is defective (fewer than $n$ independent eigenvectors, as for $\begin{pmatrix}1&1\\0&1\end{pmatrix}$; use the Jordan form or the SVD), or $\mathbf{A}$ is nonsymmetric with nearly parallel eigenvectors, where small perturbations move eigenvalues a great deal.
Source and basis: derived from the spectral theorem; taught in [Linear algebra](05-linear-algebra.md).

Example: for $\mathbf{A} = \begin{pmatrix}2&1\\1&3\end{pmatrix}$, the square of its eigenvalues must sum to $\operatorname{tr}(\mathbf{A}^2)$. With $\mathbf{A}^2 = \begin{pmatrix}5&5\\5&10\end{pmatrix}$ the trace is 15, and $3.618^2 + 1.382^2 = 15$. The Rayleigh quotient at $\mathbf{x} = (1, 1)^{\mathsf{T}}$ is $3.5$, between the two eigenvalues, as the bound requires.

<details><summary>Verification</summary>

```verify
l1 = (5 + sqrt(5)) / 2
l2 = (5 - sqrt(5)) / 2
expect(l1, "3.618")
expect(l2, "1.382")
expect(l1**2 + l2**2, "15")
a2_11 = 2 * 2 + 1 * 1
a2_22 = 1 * 1 + 3 * 3
expect(a2_22, "10")
expect(a2_11 + a2_22, "15")
rq = (2 + 1 + 1 + 3) / 2
expect(rq, "3.5")
check(l2 <= rq and rq <= l1, "Rayleigh quotient bounded by the eigenvalues")
```

</details>

## Conditioning

The **condition number** of a matrix measures how much a relative error in the data can be amplified into a relative error in the solution. It is a property of the problem, not of the algorithm.

### Condition number and loss of digits

$$\kappa(\mathbf{A}) = \lVert\mathbf{A}\rVert\,\lVert\mathbf{A}^{-1}\rVert, \qquad \frac{\lVert\delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} \le \kappa(\mathbf{A})\,\frac{\lVert\delta\mathbf{b}\rVert}{\lVert\mathbf{b}\rVert}, \qquad \text{digits lost} \approx \log_{10}\kappa(\mathbf{A})$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\kappa(\mathbf{A})$ | condition number in a stated norm | dimensionless |
| $\lVert\cdot\rVert$ | matrix or vector norm (state which) | dimensionless |
| $\delta\mathbf{b}$ | perturbation of the right-hand side | dimensionless |
| $\delta\mathbf{x}$ | resulting perturbation of the solution | dimensionless |

Holds when: $\mathbf{A}$ is invertible and the same family of norms is used throughout. In the 2-norm, $\kappa(\mathbf{A}) = \sigma_{\max}/\sigma_{\min}$, which equals $\lvert\lambda_{\max}\rvert/\lvert\lambda_{\min}\rvert$ for a symmetric matrix. Always $\kappa \ge 1$.
Breaks when: the bound is read as an estimate (it is a worst case, and a particular error can be far smaller), or the matrix has rows or columns of very different scale (rescale first, since the condition number then overstates the difficulty).
Source and basis: derived from the norm inequality $\lVert\mathbf{A}\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert\lVert\mathbf{x}\rVert$ applied to the perturbed system; taught in [Numerical methods](08-numerical-methods.md).

Solve conditioning problems with this rule of thumb: if the data are good to $d$ significant digits, expect about $d - \log_{10}\kappa$ digits in the answer. For floating-point limits and algorithm choices see [Probability and numerical methods reference](reference-probability-numerical-methods.md).

Example: $\mathbf{A} = \begin{pmatrix}1&1\\1&1.0001\end{pmatrix}$ has $\det\mathbf{A} = 0.0001$. Its infinity-norm is $2.0001$, the norm of its inverse is $2.0001/0.0001 = 20001$, so $\kappa_\infty = 40004$ and about $4.6$ digits are lost.

<details><summary>Verification</summary>

```verify
a = q(1, "")
b = q(1, "")
c = q(1, "")
d = q(1.0001, "")
det = a * d - b * c
expect(det, "0.0001")
na = abs(c) + abs(d)
expect(na, "2.0001")
ninv = (abs(d) + abs(b)) / det
expect(ninv, "20001")
kap = na * ninv
expect(kap, "40004")
expect(log10(kap), "4.6")
```

</details>

## First-order ODEs

An **ordinary differential equation (ODE)** relates a function of one variable to its derivatives. A first-order equation involves only the first derivative; it needs one initial condition.

### Separable equations

$$\frac{dy}{dt} = g(t)\,h(y) \quad\Rightarrow\quad \int\frac{dy}{h(y)} = \int g(t)\,dt + C$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y$ | unknown function | dimensionless |
| $t$ | independent variable (time) | s |
| $g(t)$, $h(y)$ | given functions of one variable each | dimensionless |
| $C$ | constant of integration, set by the initial condition | dimensionless |

Holds when: the right side factors as a function of $t$ times a function of $y$, and $h(y) \ne 0$ along the path.
Breaks when: $h(y_0) = 0$ at some constant $y_0$ (that constant is also a solution and the division loses it), or the integrals cannot be done in closed form (integrate numerically).
Source and basis: derived from the chain rule and integration of both sides; taught in [Differential equations](06-differential-equations.md).

Example: decay $dy/dt = -k y$ with $k = 0.2\ \text{1/s}$ and $y(0) = y_0$ gives $y = y_0 e^{-kt}$. At $t = 5\ \text{s}$ the factor is $e^{-1} = 0.3679$.

<details><summary>Verification</summary>

```verify
k = q(0.2, "1/s")
t = q(5, "s")
expect(k * t, "1")
expect(exp(-k * t), "0.3679")
```

</details>

### Linear first-order equations and the integrating factor

$$y' + P(t)\,y = Q(t) \quad\Rightarrow\quad y = \frac{1}{\mu}\Big(\int \mu\,Q\,dt + C\Big), \qquad \mu = e^{\int P\,dt}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y$ | unknown function | dimensionless |
| $t$ | time | s |
| $P(t)$ | coefficient of $y$ | 1/s |
| $Q(t)$ | forcing term | 1/s |
| $\mu(t)$ | integrating factor | dimensionless |
| $C$ | constant of integration | dimensionless |

Holds when: the equation is linear in $y$ and $y'$ with the coefficient of $y'$ equal to 1 (divide through first).
Breaks when: the equation is nonlinear in $y$ (for example $y' + y^2 = Q$; try a substitution, or solve numerically).
Source and basis: derived from the product rule, since $(\mu y)' = \mu(y' + P y)$ when $\mu' = P\mu$; taught in [Differential equations](06-differential-equations.md).

Example: $y' + 2y = 6$ with $y(0) = 0$. Here $\mu = e^{2t}$, so $y = 3 + C e^{-2t}$, and $y(0) = 0$ gives $C = -3$. At $t = 1\ \text{s}$, $y = 3(1 - e^{-2}) = 2.594$. The steady value is $Q/P = 3$.

<details><summary>Verification</summary>

```verify
p = q(2, "1/s")
qq = q(6, "1/s")
t = q(1, "s")
yss = qq / p
expect(yss, "3")
y = yss * (1 - exp(-p * t))
expect(y, "2.594")
```

</details>

### Exact equations

$$M(x,y)\,dx + N(x,y)\,dy = 0 \ \text{ is exact when } \ \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}, \qquad \psi(x,y) = C \ \text{ with } \ \psi_x = M,\ \psi_y = N$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $M$, $N$ | coefficient functions of the differential form | dimensionless |
| $\psi$ | potential function whose level curves are the solutions | dimensionless |
| $x$, $y$ | independent variable and unknown function | dimensionless |
| $C$ | constant fixed by the initial condition | dimensionless |

Holds when: $M$ and $N$ have continuous first partial derivatives on a simply connected region and the mixed partial test passes.
Breaks when: the test fails (look for an integrating factor that depends on $x$ alone or $y$ alone), or the region has a hole.
Source and basis: derived from equality of mixed partial derivatives of a potential; taught in [Differential equations](06-differential-equations.md).

Example: $(2xy + 1)\,dx + x^2\,dy = 0$ has $M_y = 2x = N_x$. Integrating $M$ in $x$ gives $\psi = x^2 y + x$. With $y(1) = 2$, $C = 3$, so at $x = 2$ the solution is $y = (3 - 2)/4 = 0.25$.

<details><summary>Verification</summary>

```verify
x0 = q(1, "")
y0 = q(2, "")
c = x0**2 * y0 + x0
expect(c, "3")
x = q(2, "")
expect((c - x) / x**2, "0.25")
```

</details>

## Second-order linear ODEs

A second-order linear ODE with constant coefficients models a mass, spring, and damper, or a series RLC circuit. It needs two initial conditions.

### Characteristic equation and homogeneous solutions

$$a\,y'' + b\,y' + c\,y = 0, \qquad a r^2 + b r + c = 0, \qquad r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y$ | unknown function | dimensionless |
| $a$ | constant coefficient of $y''$ | dimensionless |
| $b$ | constant coefficient of $y'$ | 1/s |
| $c$ | constant coefficient of $y$ | $1/\text{s}^{2}$ |
| $r$ | characteristic root | 1/s |
| $t$ | independent variable, time | s |

Holds when: the coefficients are constants and the equation is homogeneous. The solution form depends on the discriminant.

| Discriminant $b^2 - 4ac$ | Roots | General solution |
|---|---|---|
| positive | two real, $r_1 \ne r_2$ | $C_1 e^{r_1 t} + C_2 e^{r_2 t}$ |
| zero | one repeated real, $r$ | $(C_1 + C_2 t)\,e^{r t}$ |
| negative | complex pair $\alpha \pm j\beta$ | $e^{\alpha t}(C_1\cos\beta t + C_2\sin\beta t)$ |

Breaks when: the coefficients vary with $t$ (use series or a special-function solution), or the equation is nonlinear.
Source and basis: derived from substituting $y = e^{rt}$; taught in [Differential equations](06-differential-equations.md). For the mass-spring-damper reading of $\omega_n$ and $\zeta$ see [Vibrations reference](../physics/reference-vibrations.md).

Example: $y'' + 2y' + 5y = 0$ has $b^2 - 4ac = -16$ and $r = -1 \pm 2j$. With $y(0) = 1$ and $y'(0) = 0$, $C_1 = 1$ and $-C_1 + 2C_2 = 0$ gives $C_2 = 0.5$. At $t = 1\ \text{s}$, $y = e^{-1}(\cos 2 + 0.5\sin 2) = 0.01416$.

<details><summary>Verification</summary>

```verify
a = q(1, "")
b = q(2, "1/s")
c = q(5, "1/s^2")
disc = b**2 - 4 * a * c
expect(disc, "-16 1/s^2")
alpha = -b / (2 * a)
beta = sqrt(-disc) / (2 * a)
expect(alpha, "-1 1/s")
expect(beta, "2 1/s")
c1 = q(1, "")
c2 = -alpha * c1 / beta
expect(c2, "0.5")
t = q(1, "s")
y = exp(alpha * t) * (c1 * cos(beta * t) + c2 * sin(beta * t))
expect(y, "0.01416")
```

</details>

### Undetermined coefficients

For a particular solution, guess a form that matches the forcing term, with unknown constants.

| Forcing $f(t)$ | Trial $y_p$ |
|---|---|
| polynomial of degree $m$ | polynomial of degree $m$ with all lower terms |
| $e^{st}$ | $A e^{st}$ |
| $\cos\omega t$ or $\sin\omega t$ | $A\cos\omega t + B\sin\omega t$ |
| product of the above | product of the trial forms |

If a trial term already solves the homogeneous equation, multiply the whole trial by $t$ (by $t^2$ for a repeated root). The general solution is $y = y_h + y_p$, and the constants $C_1$, $C_2$ are fixed only after adding $y_p$.

$$y'' - 3y' + 2y = e^{3t} \ \Rightarrow\ y_p = A e^{3t}, \qquad (9 - 9 + 2)A = 1$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y_p$ | particular solution | dimensionless |
| $A$ | unknown coefficient | dimensionless |
| $s$ | exponent in the forcing term | 1/s |

Holds when: the forcing is a sum of polynomials, exponentials, sines, and cosines, and the coefficients are constant.
Breaks when: the forcing is $\tan t$, $1/t$, or another function with infinitely many independent derivatives (use variation of parameters), or the equation has variable coefficients.
Source and basis: derived from linearity and the closure of the trial families under differentiation; taught in [Differential equations](06-differential-equations.md).

Example: substituting gives $2A = 1$, so $A = 0.5$ and $y_p(0) = 0.5$. The homogeneous roots are 1 and 2, neither equal to 3, so no extra factor of $t$ is needed.

<details><summary>Verification</summary>

```verify
s = q(3, "1/s")
lhs = s**2 - 3 * s * q(1, "1/s") + 2 * q(1, "1/s^2")
expect(lhs, "2 1/s^2")
forcing = q(1, "1/s^2")
expect(forcing / lhs, "0.5")
```

</details>

### Variation of parameters

$$y'' + p\,y' + q\,y = f(t) \ \Rightarrow\ y_p = -y_1\int\frac{y_2 f}{W}\,dt + y_2\int\frac{y_1 f}{W}\,dt, \qquad W = y_1 y_2' - y_1' y_2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y_1$, $y_2$ | independent homogeneous solutions | dimensionless |
| $W$ | Wronskian of $y_1$ and $y_2$ | 1/s |
| $f(t)$ | forcing term, with the coefficient of $y''$ equal to 1 | $1/\text{s}^{2}$ |
| $p$ | coefficient of $y'$ (function of $t$ allowed) | 1/s |
| $q$ | coefficient of $y$ (function of $t$ allowed) | $1/\text{s}^{2}$ |

Holds when: two independent homogeneous solutions are known and the coefficient of $y''$ is 1. It works for variable coefficients.
Breaks when: the Wronskian is zero (the two solutions are not independent), or the integrals have no closed form.
Source and basis: derived from letting the constants of the homogeneous solution vary and imposing one extra condition; taught in [Differential equations](06-differential-equations.md).

Example: $y'' - y = e^{t}$ has $y_1 = e^{t}$, $y_2 = e^{-t}$, and $W = -2$. The formula gives $y_p = \big(\tfrac{t}{2} - \tfrac{1}{4}\big)e^{t}$. At $t = 2$, $y_p'' - y_p = e^{2} = 7.389$. The term $-\tfrac14 e^{t}$ solves the homogeneous equation and can be absorbed into $C_1$.

<details><summary>Verification</summary>

```verify
y1 = q(1, "")
y2 = q(1, "")
w = y1 * (-y2) - y1 * y2
expect(w, "-2")
t = q(2, "")
yp = (t / 2 - 0.25) * exp(t)
ypp = (t / 2 - 0.25) * exp(t) + exp(t)
expect(ypp - yp, "7.389")
expect(exp(t), "7.389")
```

</details>

## Systems and state space

A **state-space model** writes a system of ODEs as one first-order matrix equation. Any higher-order linear ODE converts to it by taking the value and each derivative below the highest as states.

### Matrix exponential and eigen solution

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \qquad \mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}_0 + \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau)\,d\tau, \qquad e^{\mathbf{A}t} = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{x}$ | state vector | dimensionless |
| $\mathbf{x}_0$ | initial state | dimensionless |
| $\mathbf{u}$ | input vector | dimensionless |
| $\mathbf{A}$ | state matrix | 1/s |
| $\mathbf{B}$ | input matrix | dimensionless |
| $\tau$ | dummy time variable in the convolution | s |
| $t$ | time | s |

Holds when: $\mathbf{A}$ and $\mathbf{B}$ are constant (linear time-invariant system). The last form needs $\mathbf{A}$ diagonalizable. The system is asymptotically stable when every eigenvalue of $\mathbf{A}$ has negative real part.
Breaks when: $\mathbf{A}$ is defective (use the Jordan form, which adds terms like $t e^{\lambda t}$), the coefficients vary in time, or the system is nonlinear (linearize about an operating point first).
Source and basis: derived from the series definition $e^{\mathbf{A}t} = \sum_k (\mathbf{A}t)^k/k!$ and the integrating-factor method; taught in [Differential equations](06-differential-equations.md). The control reading (poles, transfer functions) is in [Controls reference](../physics/reference-controls.md).

Solve an unforced system with $\mathbf{x}(t) = \sum_i c_i \mathbf{v}_i e^{\lambda_i t}$, where the constants $c_i$ come from $\mathbf{x}(0) = \sum_i c_i\mathbf{v}_i$.

Example: $\mathbf{A} = \begin{pmatrix}0&1\\-2&-3\end{pmatrix}$ has trace $-3$ and determinant 2, so $\lambda = -1$ and $\lambda = -2$ with eigenvectors $(1, -1)$ and $(1, -2)$. For $\mathbf{x}_0 = (1, 0)$, $c_1 = 2$ and $c_2 = -1$. At $t = 1\ \text{s}$, $x_1 = 2e^{-1} - e^{-2} = 0.6004$ and $x_2 = -2e^{-1} + 2e^{-2} = -0.4651$. Both eigenvalues are negative, so the system is stable.

<details><summary>Verification</summary>

```verify
tr = q(-3, "")
det = q(2, "")
disc = sqrt(tr**2 - 4 * det)
l1 = (tr + disc) / 2
l2 = (tr - disc) / 2
expect(l1, "-1")
expect(l2, "-2")
c2 = q(-1, "")
c1 = 1 - c2
expect(c1, "2")
check(abs(-c1 - 2 * c2) < 1e-9, "second component of x0 is zero")
t = q(1, "")
x1 = c1 * exp(l1 * t) + c2 * exp(l2 * t)
x2 = -c1 * exp(l1 * t) - 2 * c2 * exp(l2 * t)
expect(x1, "0.6004")
expect(x2, "-0.4651")
```

</details>

## Boundary-value problems

A **boundary-value problem** fixes conditions at the two ends of an interval instead of at one starting point. Solutions may fail to exist or may not be unique, and that is the point, because it selects special values of a parameter.

### Sturm-Liouville problems

$$-\frac{d}{dx}\Big(p(x)\frac{dy}{dx}\Big) + q(x)\,y = \lambda\,w(x)\,y, \qquad \int_a^b y_m\,y_n\,w\,dx = 0\ \ (m \ne n)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $y$ | eigenfunction | dimensionless |
| $x$ | position | m |
| $p$, $q$, $w$ | coefficient functions, with $p > 0$ and weight $w > 0$ | dimensionless |
| $\lambda$ | eigenvalue | $1/\text{m}^{2}$ |
| $a$, $b$ | ends of the interval | m |

Holds when: $p$, $p'$, $q$, $w$ are continuous on $[a,b]$, $p$ and $w$ are positive, and each end has a Dirichlet, Neumann, or Robin condition. Then the eigenvalues are real, can be ordered $\lambda_1 < \lambda_2 < \dots$ without upper limit, and eigenfunctions of different eigenvalues are orthogonal with weight $w$. Any reasonable function on the interval is a series in the eigenfunctions.
Breaks when: $p$ vanishes at an end (a singular problem such as Bessel's equation needs its own boundedness condition), or the boundary conditions are not of the separated form.
Source and basis: derived from integration by parts and self-adjointness of the operator; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

Example: $y'' + \lambda y = 0$ with $y(0) = y(L) = 0$ has $\lambda_n = (n\pi/L)^2$ and $y_n = \sin(n\pi x/L)$. For $L = 2\ \text{m}$ and $n = 1$, $\lambda_1 = (\pi/2)^2 = 2.467\ \text{1/m}^2$. Neumann ends ($y'(0) = y'(L) = 0$) give the same $\lambda_n$ with $y_n = \cos(n\pi x/L)$ and an extra $\lambda_0 = 0$.

<details><summary>Verification</summary>

```verify
l = q(2, "m")
n = q(1, "")
lam = (n * pi / l)**2
expect(lam, "2.467 1/m^2")
```

</details>

## Laplace transform

The **Laplace transform** turns a linear constant-coefficient ODE in time into an algebraic equation in $s$, with the initial conditions built in. This sheet uses the one-sided transform with lower limit $0^-$, as in [Notation](../data/notation.md#transform-conventions).

### Transform pairs

| $f(t)$ for $t \ge 0$ | $F(s)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $H(t)$ (unit step) | $1/s$ |
| $t$ | $1/s^2$ |
| $t^n$, $n = 1, 2, \dots$ | $n!/s^{n+1}$ |
| $e^{-at}$ | $1/(s + a)$ |
| $t e^{-at}$ | $1/(s + a)^2$ |
| $\sin\omega t$ | $\omega/(s^2 + \omega^2)$ |
| $\cos\omega t$ | $s/(s^2 + \omega^2)$ |
| $e^{-at}\sin\omega t$ | $\omega/((s + a)^2 + \omega^2)$ |
| $e^{-at}\cos\omega t$ | $(s + a)/((s + a)^2 + \omega^2)$ |

Each pair follows from the definition by direct integration for $\mathrm{Re}\,s$ large enough, and it is derived from that definition.

### Transform rules

$$\mathcal{L}\{f'\} = sF(s) - f(0^-), \qquad \mathcal{L}\{f''\} = s^2F(s) - s f(0^-) - f'(0^-), \qquad \mathcal{L}\{e^{-at}f\} = F(s + a), \qquad \mathcal{L}\{f(t-\tau_d)H(t-\tau_d)\} = e^{-s\tau_d}F(s), \qquad \mathcal{L}\{f * g\} = F(s)\,G(s)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f(t)$, $g(t)$ | time functions, zero for $t < 0$ | dimensionless |
| $F(s)$, $G(s)$ | their Laplace transforms | dimensionless |
| $s$ | complex frequency variable | 1/s |
| $a$ | decay rate in the exponential shift | 1/s |
| $\tau_d$ | time delay | s |
| $f * g$ | convolution of $f$ and $g$ | dimensionless |

Holds when: the integrals converge, that is, $f$ is of exponential order and $\mathrm{Re}\,s$ exceeds its growth rate. The derivative rules use the initial values at $0^-$.
Breaks when: $f$ grows faster than any exponential (such as $e^{t^2}$, which has no transform), or the initial values are taken at $0^+$ for a signal with a jump or impulse at the origin (the two differ).
Source and basis: derived from the definition and integration by parts; taught in [Differential equations](06-differential-equations.md). The use of $F(s)$ as a transfer function is in [Controls reference](../physics/reference-controls.md).

Example: solve $y' + 2y = 6$ with $y(0^-) = 0$. The transform is $sY + 2Y = 6/s$, so $Y = 6/(s(s+2))$. Partial fractions below give $y = 3(1 - e^{-2t})$, which matches the integrating-factor result, and at $t = 1\ \text{s}$ it is $2.594$.

<details><summary>Verification</summary>

```verify
s = q(1, "")
a = q(2, "")
expect(6 / (s * (s + a)), "2")
expect(3 / s - 3 / (s + a), "2")
t = q(1, "")
expect(3 * (1 - exp(-a * t)), "2.594")
```

</details>

### Partial fractions

To invert a ratio of polynomials with the numerator of lower degree than the denominator, split it into terms that appear in the table.

$$F(s) = \frac{N(s)}{(s - p_1)(s - p_2)\cdots(s - p_n)} = \sum_{k}\frac{A_k}{s - p_k}, \qquad A_k = \Big[(s - p_k)F(s)\Big]_{s = p_k}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $N(s)$ | numerator polynomial of degree below $n$ | dimensionless |
| $p_k$ | distinct poles (roots of the denominator) | 1/s |
| $A_k$ | residue at pole $p_k$ | dimensionless |

Holds when: the poles are distinct and the numerator has lower degree than the denominator. Each term then inverts to $A_k e^{p_k t}$.
Breaks when: poles repeat (a pole of multiplicity $m$ needs terms in $1/(s - p)^j$ for $j = 1, \dots, m$, with the top coefficient from the cover-up rule and the others from derivatives), the degrees are equal (divide first and keep a constant, which inverts to an impulse), or poles are complex (combine each conjugate pair into a sine and cosine term).
Source and basis: derived from the algebraic identity for rational functions over the complex numbers; taught in [Differential equations](06-differential-equations.md).

Example: $F(s) = 6/(s(s+2))$ has poles $0$ and $-2$. The residue at $0$ is $6/2 = 3$, and at $-2$ it is $6/(-2) = -3$. The time function is $3 - 3e^{-2t}$. At $t = 0$ it is $0$, as it must be.

<details><summary>Verification</summary>

```verify
p1 = q(0, "")
p2 = q(-2, "")
a1 = 6 / (p1 - p2)
a2 = 6 / (p2 - p1)
expect(a1, "3")
expect(a2, "-3")
expect(a1 + a2, "0")
```

</details>

### Initial and final value theorems

$$\lim_{t\to\infty} f(t) = \lim_{s\to 0} sF(s), \qquad \lim_{t\to 0^+} f(t) = \lim_{s\to\infty} sF(s)$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $f(t)$ | time function | dimensionless |
| $F(s)$ | its Laplace transform | dimensionless |
| $s$ | complex frequency variable | 1/s |

Holds when: for the final value theorem, every pole of $sF(s)$ lies strictly in the left half-plane (so $F(s)$ has at most a simple pole at the origin and all other poles have negative real part). For the initial value theorem, $F(s)$ is strictly proper (numerator degree below denominator degree, so $f$ has no impulse at the origin) and the limit of $f$ at $0^+$ exists.
Breaks when: the conditions fail. The theorem returns a number that means nothing. For $f = \sin t$, $F = 1/(s^2 + 1)$ and $s F(s) \to 0$ as $s \to 0$, but $f$ has no limit. For $f = e^{t}$, $sF(s) = s/(s - 1) \to 0$ at $s = 0$, but $f$ grows without bound.
Source and basis: derived from the derivative rule $\mathcal{L}\{f'\} = sF - f(0^-)$ and letting $s$ go to 0 or to infinity; taught in [Differential equations](06-differential-equations.md).

Example: $F(s) = 6/(s(s+2))$ has a simple pole at $0$ and one at $-2$, so the final value theorem applies. $sF(s) = 6/(s+2)$ gives $3$ at $s = 0$. The initial value is $0$, since $6/(s+2) \to 0$ as $s \to \infty$. Both agree with $y = 3(1 - e^{-2t})$.

<details><summary>Verification</summary>

```verify
s0 = q(0, "")
expect(6 / (s0 + 2), "3")
big = q(1000000, "")
check(6 / (big + 2) < 1e-4, "initial value tends to zero")
```

</details>

## Fourier series and transform

This sheet uses the conventions in [Notation](../data/notation.md#transform-conventions). The Fourier series uses the period $T_0$ and $\omega_0 = 2\pi/T_0$. The Fourier transform uses ordinary frequency $f$ in Hz, with no $2\pi$ outside the exponent. A formula copied from a source that uses angular frequency $\omega$ has factors of $2\pi$ that must be converted before use.

### Fourier series

A **Fourier series** writes a periodic signal as a sum of sines and cosines at the fundamental frequency and its multiples.

$$x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n\omega_0 t}, \quad c_n = \frac{1}{T_0}\int_{T_0} x(t)\,e^{-jn\omega_0 t}\,dt, \quad x(t) = a_0 + \sum_{n=1}^{\infty}\big(a_n\cos n\omega_0 t + b_n\sin n\omega_0 t\big), \quad \frac{1}{T_0}\int_{T_0}\lvert x\rvert^2\,dt = \sum_n \lvert c_n\rvert^2$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x(t)$ | periodic signal | dimensionless |
| $T_0$ | period | s |
| $\omega_0$ | fundamental angular frequency, $2\pi/T_0$ | rad/s |
| $c_n$ | complex coefficient of harmonic $n$ | dimensionless |
| $a_0$, $a_n$, $b_n$ | real-form coefficients, with $a_0 = c_0$, $a_n = 2\,\mathrm{Re}\,c_n$, $b_n = -2\,\mathrm{Im}\,c_n$ | dimensionless |
| $n$ | harmonic number | dimensionless |
| $t$ | time | s |

Holds when: the signal is periodic with finite energy per period, and has finitely many jumps and extrema per period (Dirichlet conditions). The series converges to the signal at points of continuity and to the mean of the two one-sided limits at a jump. The last equation is Parseval's relation: mean power equals the sum of the coefficient powers.
Breaks when: the signal is not periodic (use the transform), or you truncate a series for a signal with a jump. Near a jump the partial sums overshoot by about 9 percent of the jump size, and adding terms narrows the overshoot without removing it (the Gibbs phenomenon).
Source and basis: derived from orthogonality of complex exponentials over one period; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

Example: the square wave of amplitude 1 ($+1$ for the first half period, $-1$ for the second) has $a_n = 0$ and $b_n = 4/(n\pi)$ for odd $n$ and zero for even $n$. The fundamental has amplitude $4/\pi = 1.273$, and $\lvert c_1\rvert = 2/\pi = 0.6366$. Parseval gives $1 = 2\sum_{n\ \text{odd}} \lvert c_n\rvert^2$, and the first three odd harmonics ($n = 1, 3, 5$) already carry $(8/\pi^2)(1 + 1/9 + 1/25) = 0.9331$ of the total.

<details><summary>Verification</summary>

```verify
n = q(1, "")
b1 = 4 / (n * pi)
expect(b1, "1.273")
expect(b1 / 2, "0.6366")
n5 = q(25, "")
frac = 8 / pi**2 * (1 + 1 / 9 + 1 / n5)
expect(frac, "0.9331")
```

</details>

### Fourier transform

The **Fourier transform** gives the frequency content of a non-periodic signal as a function of ordinary frequency.

$$X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi f t}\,dt, \qquad x(t) = \int_{-\infty}^{\infty} X(f)\,e^{j2\pi f t}\,df, \qquad \int_{-\infty}^{\infty}\lvert x\rvert^2\,dt = \int_{-\infty}^{\infty}\lvert X\rvert^2\,df$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $x(t)$ | time signal | dimensionless |
| $X(f)$ | its Fourier transform | dimensionless |
| $t$ | time | s |
| $f$ | frequency | Hz |

Holds when: $x$ is absolutely integrable (or square integrable), which covers decaying transients. Useful rules, all in this convention: differentiation maps to $x' \to j2\pi f\,X(f)$, a delay $t_0$ multiplies $X$ by $e^{-j2\pi f t_0}$, and convolution in time maps to a product in frequency. For $x(t) = 0$ when $t < 0$, $X(f) = F(s)$ at $s = j2\pi f$ when the Laplace transform converges on the imaginary axis.
Breaks when: the signal does not decay (a steady sinusoid or a step needs distributions, giving delta functions), the system is unstable (the integral diverges while the Laplace transform still exists), or another source's $\omega$ or $1/\sqrt{2\pi}$ convention is mixed in.
Source and basis: derived from the Fourier series in the limit of infinite period; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

| $x(t)$ | $X(f)$ |
|---|---|
| $e^{-at}H(t)$, $a > 0$ | $1/(a + j2\pi f)$ |
| rectangular pulse of height 1 and width $\tau_p$, centered at 0 | $\tau_p\,\mathrm{sinc}(\pi f\tau_p)$ with $\mathrm{sinc}(u) = \sin u/u$ |
| $e^{-\pi t^2}$ | $e^{-\pi f^2}$ |
| $\delta(t)$ | $1$ |

Example: for $x = e^{-at}H(t)$ with $a = 3\ \text{1/s}$, the magnitude at $f = 1\ \text{Hz}$ is $1/\sqrt{a^2 + (2\pi f)^2} = 1/\sqrt{9 + 39.48} = 0.1436\ \text{s}$. At $f = 0$ it is $1/a = 0.3333\ \text{s}$, the area under the signal.

<details><summary>Verification</summary>

```verify
a = q(3, "1/s")
f = q(1, "Hz")
w = 2 * pi * f
expect(w**2, "39.48 1/s^2")
expect(1 / sqrt(a**2 + w**2), "0.1436 s")
expect(1 / a, "0.3333 s")
```

</details>

## PDE types and boundary conditions

A **partial differential equation (PDE)** relates a function of several variables to its partial derivatives. The three standard linear second-order types behave differently, and the right boundary conditions depend on the type. The heat and wave equations as physics are in [PDEs and Fourier series](10-pdes-and-fourier-series.md); this section keeps the mathematics.

### Classification

$$A\,u_{xx} + B\,u_{xy} + C\,u_{yy} + \text{lower-order terms} = 0, \qquad B^2 - 4AC \ \begin{cases} < 0 & \text{elliptic} \\ = 0 & \text{parabolic} \\ > 0 & \text{hyperbolic} \end{cases}$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | unknown field | dimensionless |
| $A$, $B$, $C$ | coefficients of the second derivatives | dimensionless |
| $x$, $y$ | independent variables (a second variable may be time) | m |

Holds when: the PDE is linear in the second derivatives, and the type is judged at each point (coefficients that vary can change the type across the domain).
Breaks when: the equation is a system, is of higher order, or is nonlinear, where the type may depend on the solution.

| Type | Standard form | Behavior | Data needed |
|---|---|---|---|
| Elliptic | $u_{xx} + u_{yy} = 0$ (Laplace), $= g$ (Poisson) | steady state, smooth, no waves | condition on the whole boundary |
| Parabolic | $u_t = \alpha\,u_{xx}$ (heat, diffusion) | smoothing, irreversible, infinite signal speed | initial profile and boundary conditions |
| Hyperbolic | $u_{tt} = c^2 u_{xx}$ (wave) | finite speed $c$, signals and discontinuities persist; shocks form only in nonlinear hyperbolic equations | initial $u$ and $u_t$, and boundary conditions |

Source and basis: derived from the characteristics of the equation; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

Example: the wave equation $c^2u_{xx} - u_{tt} = 0$ with $c = 2\ \text{m/s}$ has $A = c^2$, $B = 0$, $C = -1$, so $B^2 - 4AC = 16$, positive and therefore hyperbolic. The Laplace equation has $A = C = 1$, so $B^2 - 4AC = -4$, elliptic. The heat equation has $A = \alpha$ and $B = C = 0$, so the discriminant is $0$, parabolic.

<details><summary>Verification</summary>

```verify
c = q(2, "")
a = c**2
cc = q(-1, "")
expect(0 * 0 - 4 * a * cc, "16")
expect(0 - 4 * 1 * 1, "-4")
```

</details>

### Boundary conditions

A **boundary condition** states what happens at the edge of the domain. With $\mathbf{n}$ the outward normal:

$$\text{Dirichlet: } u = g, \qquad \text{Neumann: } \frac{\partial u}{\partial n} = g, \qquad \text{Robin: } \frac{\partial u}{\partial n} + h\,u = g$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | unknown field on the boundary | dimensionless |
| $\partial u/\partial n$ | derivative along the outward normal | 1/m |
| $g$ | given boundary data | dimensionless |
| $h$ | Robin coefficient (a ratio of transfer coefficient to conductivity in heat flow) | 1/m |

Holds when: the data are given on the whole boundary, one condition per boundary point. A fixed temperature, a clamped end, or a fixed potential is Dirichlet. An insulated wall, a free end, or a prescribed flux is Neumann. Convection to a surrounding fluid is Robin.
Breaks when: pure Neumann data on an elliptic problem are applied without compatibility (the solution then exists only if the net flux is zero, and is then unique only up to a constant), or when data are imposed that conflict with the type (for example, Dirichlet data on all sides for a hyperbolic problem in time).
Source and basis: derived from the physical statements of fixed value, fixed flux, and flux proportional to the difference from a surrounding value; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

### Separation of variables

Assume the solution is a product of functions of one variable each. The PDE splits into ODEs linked by a separation constant, and the boundary conditions turn one of them into a Sturm-Liouville problem.

$$u_t = \alpha\,u_{xx},\ u(0,t) = u(L,t) = 0 \ \Rightarrow\ u(x,t) = \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{L}\,e^{-\alpha(n\pi/L)^2 t}, \qquad b_n = \frac{2}{L}\int_0^L u(x,0)\sin\frac{n\pi x}{L}\,dx$$

Variables:

| Symbol | Meaning | SI unit |
|---|---|---|
| $u$ | field (temperature or concentration) | dimensionless |
| $x$ | position | m |
| $t$ | time | s |
| $L$ | length of the domain | m |
| $\alpha$ | diffusivity | $\text{m}^{2}$/s |
| $b_n$ | coefficient of mode $n$ from the initial profile | dimensionless |
| $n$ | mode number | dimensionless |

Holds when: the PDE and boundary conditions are linear and homogeneous, and the domain is a coordinate-aligned shape (a bar, a rectangle, a disk, a sphere). Nonhomogeneous boundary data are handled by subtracting a steady solution first.
Breaks when: the geometry is irregular, the coefficients depend on position or on $u$, or the boundary conditions mix coordinates. Use a numerical method; see [Probability and numerical methods reference](reference-probability-numerical-methods.md).
Source and basis: derived from the product ansatz, Sturm-Liouville orthogonality, and the Fourier series; taught in [PDEs and Fourier series](10-pdes-and-fourier-series.md).

Mode $n$ decays with time constant $\tau_n = L^2/(\alpha n^2\pi^2)$, so the higher modes die out $n^2$ times faster and the profile smooths toward the lowest mode. For the wave equation, $u_{tt} = c^2u_{xx}$ with the same ends has natural frequencies $f_n = nc/(2L)$, which do not decay.

Example: a bar with $L = 0.1\ \text{m}$ and $\alpha = 1 \times 10^{-4}\ \text{m}^2/\text{s}$ has $\tau_1 = 10.13\ \text{s}$. Mode 3 decays with $\tau_3 = \tau_1/9 = 1.126\ \text{s}$.

<details><summary>Verification</summary>

```verify
l = q(0.1, "m")
alpha = q(1e-4, "m^2/s")
tau1 = l**2 / (alpha * pi**2)
expect(tau1, "10.13 s")
expect(tau1 / 9, "1.126 s")
```

</details>

## Checklists

Before trusting a linear-algebra result:

- Is the matrix square and invertible? Check the rank, or the smallest singular value against the size of the largest.
- Did you solve by factorization rather than by an explicit inverse?
- Is the condition number small enough for the digits you need? Are the columns scaled to comparable size?
- For a symmetric matrix, did you use a symmetric method, and are the eigenvalues real and the vectors orthogonal?
- Does the residual $\lVert\mathbf{A}\hat{\mathbf{x}} - \mathbf{b}\rVert$ come out small, and for least squares is it perpendicular to the columns?

Before trusting an ODE or transform result:

- Are the initial or boundary conditions stated and applied after adding the particular solution?
- Does the solution satisfy the equation when substituted back, and each initial condition?
- Is the sign of the real part of each root or eigenvalue what you expect for the physics (stable or unstable)?
- For a Laplace result, were the initial values taken at $0^-$, and were the final and initial value theorem conditions checked before use?
- For a Fourier result, is the convention (ordinary frequency, or angular) the same as in the formula you used?
- For a PDE, does the boundary data match the type, and are the modes orthogonal under the stated weight?

## Sanity checks

- Trace and determinant: the eigenvalues must sum to the trace and multiply to the determinant.
- A residual that is small does not prove an accurate solution. The error can be up to $\kappa$ times the relative residual.
- A decaying exponential falls to about 37 percent after one time constant $1/k$ and to about 5 percent after three. A step response of a first-order system reaches about 63 percent of its final value after one time constant.
- A stable second-order system with positive coefficients has characteristic roots with negative real parts. Both roots of $a r^2 + b r + c$ lie in the open left half-plane if and only if $a$, $b$, $c$ are all nonzero and of one sign. A zero coefficient, or a sign change among them, means at least one root is not in the open left half-plane.
- Undamped resonance appears when the forcing frequency equals a homogeneous natural frequency. The particular solution then grows like $t$, which is a sign that the guess needed the extra factor of $t$.
- The mean of a Fourier series is $c_0$. At a jump the series gives the midpoint, not either side.
- Mode $n$ of a diffusion problem decays $n^2$ times faster than mode 1. A wave problem has modes at integer multiples of the lowest frequency.
- Units: the exponent of every $e^{\cdot}$ and the argument of every sine or cosine must be dimensionless. The product $st$ and the product $2\pi f t$ are.

## Further reference

- Strang, *Introduction to Linear Algebra*, and *Linear Algebra and Its Applications*, for matrix theory with applications.
- Trefethen and Bau, *Numerical Linear Algebra*, for factorizations, conditioning, and stability.
- Golub and Van Loan, *Matrix Computations*, the standard handbook of algorithms.
- Boyce and DiPrima, *Elementary Differential Equations and Boundary Value Problems*, for ODEs and Sturm-Liouville problems.
- Haberman, *Applied Partial Differential Equations*, for separation of variables and boundary conditions.
- Oppenheim and Willsky, *Signals and Systems*, for the Laplace and Fourier transforms.
- Free: [MIT OpenCourseWare 18.06, Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) and [MIT OpenCourseWare 18.03SC, Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/).
- In this repo: [Linear algebra](05-linear-algebra.md), [Differential equations](06-differential-equations.md), [PDEs and Fourier series](10-pdes-and-fourier-series.md), and the general [mathematics reference](reference.md).
