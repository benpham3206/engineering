# Tools reference

**Type:** reference

This sheet covers how to choose, check, and keep engineering software and measuring tools: the file formats that keep work readable for decades, a side-by-side numerical cheat sheet (Python and MATLAB/Octave), the Git commands engineering work needs, and hand and measuring tool selection. It is for any engineer who needs a formula, a format, a command, or a checklist in the middle of a task.

## Principles

- Tools change; the test of a tool is whether you can check its answer. A result you cannot verify is not yet yours.
- Prefer open, documented formats. A file you can read from a published spec, or with a text editor, outlives the program that wrote it.
- Scripts beat clicks. A script reruns the same steps; a sequence of clicks leaves no record of what was done.
- Keep the source with the result. A number without its model, input data, and tool version cannot be audited or reproduced.
- Own your data. Keep a copy you can open without a license, a subscription, or an online account.
- Every number carries units. A tool or file that drops units is how a mm-for-m error gets built in.
- Resolution is not accuracy. A display with five digits can be wrong in the second digit.
- Calibrate against a reference before you trust a measurement. Instruments drift without warning.
- Match the tool to the question. The simplest tool that answers correctly, with a stated error bound, is the right one.

## Choosing tools

| Question | Prefer | Avoid |
|---|---|---|
| Will someone open this in ten years? | Open format (STEP, PDF/A, CSV, plain text, SVG, PNG) | Proprietary binary that needs one version of one program |
| Will I repeat or audit it? | Script or version-controlled text | One-off clicks with no record |
| Can the answer be checked? | Tool with a published test case or a hand-calculable answer | Black-box output with no check |
| Must it be shared or exported? | Neutral export next to the native file | Screenshots as the only record |
| Is the license a constraint? | Open source, or a license your organization holds | Free trial or student terms on a critical project |

- **Holds when:** the work must last years, be reviewed by others, or be regenerated.
- **Breaks when:** the sketch will be thrown away tomorrow. Do not spend a day on formats for a throwaway.
- **Rule:** if it cannot be regenerated from its inputs, export a neutral copy. Basis: native files are version-locked and get corrupted; neutral exports survive. Limit: an export loses feature history and design intent, so keep the native file too.

## File format longevity

Longevity is a judgment about how likely a format is to be readable in a decade or more. Re-check the status of any standard before relying on it for a regulated deliverable.

| Format | Standard or owner | What it stores | Future-proofing |
|---|---|---|---|
| STEP AP242 | ISO 10303-242 | Solid and surface geometry in a neutral boundary representation, plus product and manufacturing information (tolerances, notes) | High. Text-based, vendor-neutral, built for exchange and archive. Check that your exporter writes the annotations you need. |
| IGES | ANSI-published legacy standard | Curves, surfaces, and basic solids in text or binary | Medium to low. Many tools still read it, but it handles modern solids poorly and often loses topology. Use STEP for new work. |
| STL | No formal standard; de facto since stereolithography | Triangle mesh only. No units, color, or material. ASCII or binary | High for readability, low for fidelity. Lossy. Good for printing and quick meshes, not for design intent. |
| 3MF | Open specification from the 3MF Consortium (zipped XML) | Mesh plus units, color, materials, and build data | Good and growing. Open, with fewer independent long-term readers than STEP or STL. |
| OBJ | Wavefront format, open ASCII | Polygon or triangle mesh, normals, texture coordinates. No units | High for visual interchange. Units are ambiguous, so state them in the file name or a readme. |
| DXF | Autodesk, published ASCII and binary | 2D entities and layers, some simple 3D | Good for 2D interchange. Many versions exist; older simpler versions are read by the most tools. |
| PDF/A | ISO 19005 series | Fixed-layout pages with fonts and images embedded | Very high for archive. Self-contained by design. Use it for drawings and reports you must keep. |
| CSV | RFC 4180 (informal) | Rows and columns of text values, comma-separated | Very high. No types and no units, so put units in the header row. |
| Plain text (UTF-8) | Unicode | Any text, including source code and notes | Very high. Reads on every platform. Use UTF-8 consistently. |
| Markdown | No single standard; flavors differ | Text with light formatting | High as raw text. Rendered appearance varies by tool. |
| PNG | ISO/IEC 15948 | Lossless raster image | High. Good for screenshots and plots. Not for line drawings you may scale. |
| SVG | W3C standard | Vector graphics written as XML text | High. Scales without loss and stays readable as text. Strip scripts from files you did not create. |
| HDF5 | HDF Group | Hierarchical, self-describing binary arrays with metadata | High for large numerical data, but reading needs the HDF5 library. Store units as attributes. |
| JSON | ECMA-404 and RFC 8259 | Nested keys, arrays, and values as text | High. No comments, no units. Put units in key names, such as `"length_mm"`. |

- **Rule:** keep one native file plus one neutral export (STEP for solids, PDF/A for drawings, CSV or HDF5 for data) for anything that matters. Basis: native formats are version-locked. Limit: STEP can drop feature history, and PDF/A is a picture of the drawing, not its model.

## Numerical computing cheat sheet

Python lines were run on this machine (Python 3.14, NumPy 2.5.1, SciPy 1.18.0, as of 2026-10-17). MATLAB and Octave lines are the standard equivalents and were **not** run here, because Octave is not installed. The plot lines use matplotlib, which is not installed here, so they were not run either.

Python setup:

```python
import numpy as np
from scipy import integrate, optimize, signal
```

| Task | Python (NumPy / SciPy) | MATLAB / GNU Octave |
|---|---|---|
| Solve $A\mathbf{x} = \mathbf{b}$ | `x = np.linalg.solve(A, b)` | `x = A \ b` |
| Residual check | `np.linalg.norm(A @ x - b)` | `norm(A*x - b)` |
| Condition number | `np.linalg.cond(A)` | `cond(A)` |
| Polynomial roots (highest power first) | `np.roots([1, -6, 11, -6])` | `roots([1 -6 11 -6])` |
| Scalar root in a bracket | `optimize.brentq(f, a, b)` | `fzero(f, [a b])` |
| ODE $y' = f(t, y)$ | `solve_ivp(f, (t0, t1), y0, rtol=1e-10, atol=1e-12, t_eval=t)` | `[t, y] = ode45(f, [t0 t1], y0)` |
| Stiff ODE | `solve_ivp(f, (t0, t1), y0, method="BDF")` | `[t, y] = ode15s(f, [t0 t1], y0)` |
| Definite integral | `val, err = integrate.quad(f, a, b)` | `val = integral(f, a, b)` |
| Straight-line fit | `p = np.polyfit(x, y, 1)`, returns `[slope, intercept]` | `p = polyfit(x, y, 1)`, returns `[slope intercept]` |
| Nonlinear fit | `popt, pcov = optimize.curve_fit(model, x, y, p0=[...])` | `lsqcurvefit(model, p0, x, y)` (Optimization Toolbox in MATLAB, optim package in Octave; with base MATLAB use `fminsearch` on the sum of squared errors) |
| FFT of real signal | `Y = np.fft.rfft(y)`, `f = np.fft.rfftfreq(N, 1/fs)` | `Y = fft(y)`, `f = (0:N-1)*fs/N` |
| Labeled plot | `plt.plot(t, y); plt.xlabel("t (s)"); plt.ylabel("y (V)")` | `plot(t, y); xlabel("t (s)"); ylabel("y (V)")` |
| Save figure | `plt.savefig("fig.png", dpi=150)` | `print -dpng -r150 fig.png` |

Verified Python output (run this session):

```
solve    x = [0.09090909 0.63636364], residual = 0.0
roots    [1. 2. 3.]
ODE      y(4) = 0.13533528, exact = 0.13533528, max error = 6.9e-12
quad     0.33333333 (exact 1/3)
polyfit  slope 1.99, intercept 1.04
curve_fit a = 1.9947, c = 0.5012
FFT      peak at 5.0 Hz, amplitude 1.0 (5 Hz sine, fs = 100 Hz, N = 100)
```

Default tolerances: `solve_ivp` (RK45) and `ode45` both default to a relative tolerance near $10^{-3}$ and absolute near $10^{-6}$. Set them explicitly when you need accuracy. Octave `fft` is unnormalized, as in NumPy's `rfft`.

### Linear systems

- Equation: $A\mathbf{x} = \mathbf{b}$, with $A$ an $n \times n$ matrix. Units: if $\mathbf{b}$ is in N and $A$ is in N/m, then $\mathbf{x}$ is in m.
- Error bound: $\dfrac{\|\delta\mathbf{x}\|}{\|\mathbf{x}\|} \lesssim \kappa(A)\,\varepsilon$, where $\kappa(A) = \|A\|\,\|A^{-1}\|$ is the condition number (dimensionless) and $\varepsilon \approx 2.2 \times 10^{-16}$ is double-precision machine epsilon (dimensionless).
- **Holds when:** $A$ is square and nonsingular, and its entries are known to the precision you need.
- **Breaks when:** $\kappa$ is large, or $A$ is singular. The bound is a worst case, so rounding can dominate without warning.
- Typical: $\kappa \approx 2$ for $\begin{bmatrix}4&1\\1&3\end{bmatrix}$. $\kappa \approx 4\times10^4$ for $\begin{bmatrix}1&1\\1&1.0001\end{bmatrix}$, which loses about four to five digits.
- **Rule:** use `solve` (or `A \ b`), not `inv(A) @ b`. Basis: it is faster and more accurate. Limit: it still needs a sound $A$.
- **Rule:** if $\log_{10}\kappa$ is close to the number of digits you need subtracted from 16, the answer is not trustworthy at that precision. Basis: the bound above. Limit: a rough guide, not a guarantee.

### Roots

- Polynomial roots are eigenvalues of the companion matrix (what `roots` computes). Coefficients go highest power first.
- **Holds when:** the polynomial is known exactly and not very high degree.
- **Breaks when:** roots are repeated. A double root is only found to about $\sqrt{\varepsilon} \approx 1.5 \times 10^{-8}$ relative. Also breaks when coefficients span many orders of magnitude.
- **Rule:** substitute each root back into $p(x)$. The result should be near zero relative to the size of the terms. Basis: direct check. Limit: near-zero values can hide a wrong root in a flat region.
- **Rule:** for a scalar equation $f(x) = 0$ with a sign change on $[a, b]$, use a bracketing method (`brentq`, `fzero`). Basis: a bracket guarantees a root. Limit: it cannot find a pair of roots that do not change sign. Newton's method is faster but can diverge.

### Initial value ODEs

- Problem: $y' = f(t, y)$, $y(t_0) = y_0$. Example: $y' = -ky$, $y = e^{-kt}$, with $k$ in s$^{-1}$ and $t$ in s.
- Default method: explicit Runge-Kutta 4(5), Dormand-Prince (`RK45`, `ode45`). Local error per step scales as $h^5$, global error as $h^4$.
- **Holds when:** $f$ is smooth and the solution is not stiff.
- **Breaks when:**
  - The problem is stiff (fast decay alongside slow dynamics). Use an implicit method: `BDF` or `Radau` in SciPy, `ode15s` in MATLAB and Octave. Explicit methods then need tiny steps.
  - $f$ is discontinuous. Use event detection or split the interval at the switch.
  - The system is chaotic. Error grows exponentially with time, so no tolerance keeps a long run accurate.
- Check: the run above gave a maximum error of $6.9 \times 10^{-12}$ with $\text{rtol} = 10^{-10}$.
- **Rule:** halve the tolerance and rerun. If the answer changes by more than your target, tighten further or change method. Basis: convergence test. Limit: the test shows consistency, not correctness; compare with a closed form where one exists.

### Numerical integration

- Definite integral: $\int_a^b f(x)\,dx$. `quad` uses adaptive Gauss-Kronrod rules and returns an error estimate.
- Trapezoid rule error: $E \le \dfrac{(b-a)\,h^2}{12}\max|f''|$, with step $h$ (units of x). Simpson's rule error scales as $h^4$.
- **Holds when:** the integrand is smooth on a finite interval, or has a known endpoint singularity.
- **Breaks when:** the integrand is oscillatory, has an interior singularity, or the step is too coarse for its features. Split the interval at the singularity.
- Check: $\int_0^1 x^2\,dx = 1/3$ returned $0.3333333333$. $\int_0^1 x^{-1/2}\,dx = 2$ returned $2.0000000000000$ with error $\approx 6 \times 10^{-15}$.
- **Rule:** compare results with two grid spacings or two methods. If they disagree beyond your tolerance, the result is not converged. Basis: a consistency test. Limit: two methods can share a blind spot.

### Least-squares curve fitting

- Linear model: minimize $\sum_i (y_i - p_1 x_i - p_0)^2$. Units of $p_1$ are units of y over units of x, and $p_0$ has the units of y.
- Nonlinear model, such as $y = a e^{bx}$: minimize the same sum over $a$ and $b$ with an iterative solver (`curve_fit` uses Levenberg-Marquardt for unbounded problems).
- Check: the run gave a straight-line fit with slope 1.99 and intercept 1.04 on the test data, and an exponential fit with $a = 1.995$ and $b = 0.501$ on its own test data.
- **Holds when:** the model is right, errors are independent with roughly equal scatter, and you have more points than parameters. Standard errors from `pcov` assume this.
- **Breaks when:**
  - You linearize $y = ae^{bx}$ by taking $\ln y$. This weights small y values too heavily and biases $a$. Fit the nonlinear form directly.
  - The starting guess `p0` is poor. The solver may converge to a local minimum or not at all.
  - Points are fewer than parameters, or you extrapolate far outside the data.
- **Rule:** plot residuals against x. A pattern means the model is wrong, however high $R^2$ looks. Basis: residuals should be patternless. Limit: a random scatter alone does not prove the model.
- **Rule:** report parameters with their standard errors from the covariance matrix. Basis: a fit without uncertainty is incomplete. Limit: standard errors assume the noise model above.

### Fourier transform (FFT)

- Discrete transform: $X_k = \sum_{n=0}^{N-1} x_n\,e^{-2\pi i kn/N}$, with $x_n$ sampled at rate $f_s$ (Hz).
- Frequency of bin $k$: $f_k = k f_s / N$. Frequency resolution: $\Delta f = f_s / N = 1/T$, where $T$ is the record length (s).
- Nyquist frequency: $f_N = f_s / 2$. Components above it fold back as aliases.
- Single-sided amplitude: $A_k = 2|X_k|/N$ for $0 < k < N/2$. The DC and Nyquist bins are not doubled.
- **Holds when:** samples are uniform, you know $f_s$, and the signal is reasonably steady over the record.
- **Breaks when:**
  - Aliasing: sampling below twice the highest component. In practice, sample at five to ten times the highest frequency you care about.
  - Leakage: the record does not hold a whole number of cycles. Apply a window (`signal.get_window("hann", N)`, Octave `hanning(N)`) and correct the amplitude for the window's gain.
  - Zero padding interpolates the spectrum. It adds no new information about the signal.
- Check: a 5 Hz sine sampled at $f_s = 100$ Hz with $N = 100$ gave a peak at 5.0 Hz with amplitude 1.0.
- **Rule:** predict the peak frequency before you compute it, then compare. Basis: catches wrong $f_s$, wrong units on time, and mislabeled bins. Limit: a prediction does not catch leakage errors in amplitude.

### Plots

- Label every axis with a quantity and its unit, for example `"t (s)"`, `"F (N)"`.
- Use a log axis when data spans more than about two decades. Say so in the axis label.
- Show raw data points, not only a smoothed curve, and show the fit or model as a separate line.
- Export vector formats (SVG, PDF/A) for documents and PNG at a stated DPI for screenshots.
- Basis: an unlabeled plot cannot be checked. Limit: a plot shows shape, not uncertainty; add error bars where you have them.

## Git essentials for engineering work

Reference only. These commands are listed for use in your own repositories.

| Task | Command |
|---|---|
| Start a repository | `git init` |
| See what changed | `git status`, `git diff`, `git diff --staged` |
| Stage specific files | `git add path/to/file` (avoid `git add .` on a shared folder) |
| Commit with a message | `git commit -m "Short imperative summary, with units if relevant"` |
| Read history, one line each | `git log --oneline --graph` |
| Compare a file between two versions | `git diff v1.1 v1.2 -- path/to/file` |
| New branch for a design change | `git switch -c change-name` |
| Return to the main branch | `git switch main` |
| Merge a reviewed branch | `git merge change-name` (run on the target branch) |
| Tag a release | `git tag -a v1.2 -m "Release 1.2: bracket rev C"` |
| Undo local edits to one file | `git restore path/to/file` (discards unsaved edits; check first) |
| Undo a shared commit safely | `git revert <commit>` (adds a new commit; does not rewrite history) |
| Keep generated files out | Add patterns to `.gitignore`, such as `exports/`, `*.tmp`, `__pycache__/` |
| Track large binaries | Git LFS: `git lfs track "*.SLDPRT"` (then commit the `.gitattributes` file) |

- **Holds when:** the content is text (scripts, notes, data, exported CSV) or small binaries.
- **Breaks when:** the content is a binary CAD model. Git stores it but cannot diff or merge it. For diffable geometry, keep a text source (OpenSCAD, CadQuery, or a script that rebuilds the model) next to the native file.
- **Rules:**
  - One logical change per commit. The message states what changed and why, with units where they apply.
  - Never rewrite shared history. Do not use `git push --force` or `git reset --hard` on commits others have. Use `git revert`.
  - Commit the script, the input data, and a pinned environment file (for example `requirements.txt` with versions) together with the results they produced.
  - Never commit secrets, such as API keys, passwords, or license files.
  - Run `git status` before every commit.

## Hand tool and measuring tool selection

Resolution values are typical. Check the stated accuracy of the tool you own.

### Measuring tools

| Task | Right tool | Resolution (typical) | Common misuse |
|---|---|---|---|
| Rough length | Steel rule | 0.5 mm (read to half a 1 mm mark) | Measuring from a worn end; reading with the eye off square over the mark (parallax) |
| Outside dimension | Digital or dial caliper | 0.01 mm (some dial calipers 0.02 mm) | Clamping hard; jaws tilted; not zeroed before use |
| Outside diameter, precise | Outside micrometer (vernier or digital) | 0.01 mm graduation; 0.001 mm vernier or digital | Not using the ratchet stop; gripping the frame so hand heat expands it; one reading on an out-of-round part |
| Inside diameter | Bore gauge, or telescoping gauge read with a micrometer | Set to a master ring; the micrometer sets the resolution | Measuring with caliper inside jaws at an angle, which reads less than the true diameter |
| Depth of a hole or step | Depth gauge or caliper depth rod | 0.01 mm | Rod not square to the surface |
| Flatness or runout | Dial indicator on a surface plate or spindle | 0.01 mm | Plunger not perpendicular to the surface; the cosine error makes the reading too small |
| Angle | Protractor, bevel protractor, or sine bar with gauge blocks | About 1 degree (protractor); finer with a sine bar | Trusting a protractor to fractions of a degree |
| Pass or fail for a hole or thread | Plug gauge or thread gauge | Pass or fail only | Forcing a gauge through; using a worn gauge |
| Reference for setting comparators | Gauge blocks, reference rings | Set by grade; use the certificate | Wringing blocks with dirt on the faces; storing them unprotected |

### Hand tools

| Task | Right tool | Common misuse |
|---|---|---|
| Tighten to a specified torque | Torque wrench, used at its stated accuracy | Used as a breaker bar; left at a high setting after use; wrong unit (N m vs ft lb) |
| Tighten a fastener with no torque spec | Fitted hand wrench or socket | Worn wrench that slips; adjustable wrench on hex fasteners |
| Drive a hex socket fastener | Hex (Allen) key of the right size | Short key on a long bolt; cam-out from a worn key; added cheater pipe |
| Mark a drilling center | Center punch | Striking hard on a hardened part; punch not square to the surface |
| Cut a thin line in metal | Hacksaw with correct blade and tension | Blade installed with teeth backward; no tension |
| Remove burrs or shape | File with a handle | Using on hardened steel without checking; no handle |
| Set a part or drive a pin | Soft-faced mallet | Hard hammer on a hardened or machined surface |

- **Rules:**
  - Read to the resolution of the tool. A digital display shows more digits than the tool is right to.
  - Zero or check the tool before each use, and check its jaws, anvils, and frame for damage.
  - For round or flat parts, measure at several positions and report the spread, not one reading.
  - Record the tool's ID and last calibration date with each measurement.

## Checklists

### Verify your tools

- **Instruments**
  - [ ] Calibrated against a traceable standard (gauge blocks, reference rings, certified masses) within its calibration interval
  - [ ] Certificate and due date on file
  - [ ] Zeroed or checked before use
  - [ ] Inspected for damage: bent jaws, worn anvils, cracked display or lens
  - [ ] Part and tool at the same temperature for precision work
- **Software**
  - [ ] Run one case with a known hand-calculated answer and match within a stated tolerance
  - [ ] Check units by dimensional analysis on every output
  - [ ] Reproduce a published textbook or standard example
  - [ ] Check convergence: refine the mesh or step, and confirm the answer changes less than your target
  - [ ] Record the software name, version, and settings with each result
- **Models**
  - [ ] Version-control the source: the script, or the native model plus a text source
  - [ ] Export a neutral copy (STEP for solids) and compare mass or volume with a hand value
  - [ ] Tag the revision that a drawing or test refers to
  - [ ] Keep the input data file with the output file

### Before trusting a number

- [ ] Units are stated and consistent
- [ ] Order of magnitude matches a rough estimate
- [ ] Error bound, residual, or uncertainty is reported
- [ ] A second method or a hand check agrees within tolerance
- [ ] Assumptions (load, material, regime, temperature) are written beside the result

## Sanity checks

- **Linear solve:** the residual $\|A\mathbf{x} - \mathbf{b}\|$ should be near machine precision relative to $\|\mathbf{b}\|$ when $A$ is well conditioned. A large residual means the solve failed or $A$ is nearly singular.
- **Conditioning:** if $\kappa \approx 10^k$, expect to lose about $k$ digits of the answer.
- **ODE:** halving the tolerance should change the answer by less than the tolerance. Compare with a closed form when one exists.
- **Integral:** the error estimate should be below your target, and two methods should agree.
- **Fit:** residuals should show no trend. A fit with fewer points than parameters is not a fit.
- **FFT:** the peak should land where you predicted. Any peak above $f_s/2$ is an alias. Summed power in the time and frequency domains should match (Parseval's theorem).
- **Units:** a steel cube 10 mm on a side has volume $10^{-6}$ m$^3$, so mass is $7850 \times 10^{-6} = 7.85\times10^{-3}$ kg, or 7.85 g. Typical density basis.
- **Tolerance stack:** the root-sum-square total is never larger than the worst-case total.
- **Area scaling:** doubling a round diameter quadruples its area. Stress from the same force falls to one quarter.
- **Surface speed:** a 1/4 in drill at 300 sfm needs about 4580 RPM, from $N = 12V/(\pi D)$ with $V$ in ft/min and $D$ in in.
- **Earth values are one case.** Where gravity, temperature, or pressure matter, write the general form first (for example $W = mg$ with $g$ for the local body) and then substitute a value.

## Further reference

Named standards and books. Paid items are named only. Free items are not linked here because their URLs were not checked in this session.

- Golub and Van Loan, *Matrix Computations* (Johns Hopkins University Press). Standard text for linear algebra methods, including conditioning.
- Trefethen and Bau, *Numerical Linear Algebra* (SIAM). Clear treatment of stability and conditioning.
- Press, Teukolsky, Vetterling, and Flannery, *Numerical Recipes* (Cambridge University Press). Broad practical methods with code.
- Taylor, *An Introduction to Error Analysis* (University Science Books). Uncertainty propagation for measurements.
- JCGM 200:2012, *International vocabulary of metrology (VIM)*. Shared meanings for accuracy, resolution, traceability, and calibration. Check for the current edition.
- ISO 10303 (STEP) series, including ISO 10303-242 for AP242. The neutral CAD exchange standard.
- ISO 19005 (PDF/A) series. Archival PDF.
- NIST Special Publication 811, *Guide for the Use of the International System of Units (SI)*. Free from NIST; the unit rules in this sheet follow it.
