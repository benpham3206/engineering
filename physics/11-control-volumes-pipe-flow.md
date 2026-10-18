# Control volumes and pipe flow

**Type:** lesson

Real pipes carry water to homes, fuel to engines, and cooling fluid through plants. A control volume is a fixed region of space that you draw around a piece of a system so you can balance mass, momentum, and energy across its edges. Pipe flow is the most common case where friction matters, so this lesson ends with the Darcy-Weisbach head-loss equation and an explicit formula for the friction factor.

**Prerequisites:** [Hydrostatics and Bernoulli](10-hydrostatics-and-bernoulli.md)
**Time:** 8-10 h

## Core ideas

- A **control volume** (CV) is a chosen region with a boundary called the **control surface**. Mass, momentum, and energy can enter or leave through the control surface. Everything inside is what you analyze.
- A **system** is a fixed quantity of matter. A control volume is usually easier for engineers because devices like pumps, valves, and pipes stay in one place.
- **Steady flow** means nothing inside the control volume changes with time. The mass, momentum, and energy inside stay constant, so what enters must equal what leaves.
- **Volume flow rate** $Q$ is the volume of fluid passing a section per second (m$^3$/s). **Mean velocity** $V$ is $Q$ divided by the cross-section area $A$.
- **Mass flow rate** $\dot m$ is mass per second (kg/s). For incompressible flow, $\dot m = \rho Q$.
- **Laminar** flow is smooth and layered. **Turbulent** flow is mixed and chaotic. The **Reynolds number** $Re$ tells you which regime you are in. Below about 2300, pipe flow is laminar. Above about 4000, it is turbulent. Between them is a transition zone that engineers usually avoid in design.
- **Head loss** $h_f$ is energy per unit weight lost to friction along a pipe, expressed as a height of fluid (m of water). It is the friction term Bernoulli's equation was missing.
- **Major losses** come from wall friction along straight pipe. **Minor losses** come from fittings like elbows, valves, and entrances. Minor losses are described with a loss coefficient $K$.
- **Relative roughness** $\varepsilon/D$ is the wall roughness divided by the pipe diameter. Roughness matters only in turbulent flow.

### Mass balance (continuity)

For steady flow through a control volume with one inlet and one outlet, the mass entering each second equals the mass leaving. For incompressible flow in a pipe whose area changes, this becomes a simple rule: velocity goes up where area goes down. If you halve the diameter, the area drops by a factor of 4, so the speed goes up by a factor of 4.

### Momentum balance (in brief)

Momentum balances tell you the net force a flow puts on a bend, nozzle, or pipe support. The idea is that the net force on the fluid in the control volume equals the rate at which momentum leaves minus the rate at which it enters, including the pressure forces on the surface. In this lesson, you only need to know that a bend in a pipe pushes on its support. You will not solve a momentum problem here.

### Energy balance and head loss

Bernoulli's equation from lesson 10 holds only for frictionless flow. A real pipe adds a head-loss term. For steady, incompressible flow between two sections of a pipe:

- Start from the Bernoulli balance.
- Add the friction loss $h_f$ and any pump head $h_p$ or turbine head $h_t$ that sits between the sections.
- The pressure, speed, and elevation all still trade off, but some energy is turned into heat in the fluid and walls.

Engineers write this as an **energy equation with losses**. You will see it in every pump and pipe design problem.

### Reynolds number

The Reynolds number compares inertia to viscous forces:

$$
Re = \frac{\rho V D}{\mu}
$$

Here $\mu$ is dynamic viscosity. Typical value for water at 20 °C: $\mu = 1.00 \times 10^{-3}$ Pa s.

### Darcy-Weisbach equation

The head loss in a straight pipe depends on the friction factor $f$ (Darcy friction factor, dimensionless), the pipe length $L$, diameter $D$, and velocity $V$:

- Laminar flow: $f = 64/Re$. This depends only on $Re$.
- Turbulent flow: $f$ depends on both $Re$ and $\varepsilon/D$. The classic chart is the Moody diagram. The **Colebrook equation** is the implicit formula the chart comes from, and it has to be solved by iteration.
- The **Swamee-Jain** formula gives $f$ explicitly for turbulent flow, so you can compute it with a calculator and no iteration. In the worked example below, it agrees with the iterated Colebrook value to under 1 percent.

Use Swamee-Jain for turbulent design work. It is valid for $5 \times 10^3 \le Re \le 10^8$ and $10^{-6} \le \varepsilon/D \le 10^{-2}$. Use $f = 64/Re$ for laminar flow.

### Minor losses

Each fitting adds a loss:

- $h_m = K \dfrac{V^2}{2g}$, with $K$ found from tables for each fitting.
- Typical value: $K \approx 0.5$ for a sharp-edged pipe entrance. Use tables or your instructor's values for real design.

### Choosing the right tool

- Flow rate known, find head loss: use Darcy-Weisbach with Swamee-Jain.
- Diameter unknown, given head loss and flow: iterate on $D$, because $V$ and $Re$ both depend on $D$.
- Flow rate unknown, given head loss and diameter: solve for $V$ with iteration or a spreadsheet.

## Key equations

Symbols: $Q$ = volume flow rate (m$^3$/s), $\dot m$ = mass flow rate (kg/s), $A$ = area (m$^2$), $V$ = mean velocity (m/s), $\rho$ = density (kg/m$^3$), $D$ = pipe diameter (m), $\mu$ = dynamic viscosity (Pa s), $L$ = pipe length (m), $g$ = 9.81 m/s$^2$ (32.2 ft/s$^2$), $\varepsilon$ = wall roughness (m), $h_f$ = friction head loss (m), $f$ = Darcy friction factor (dimensionless), $K$ = minor loss coefficient (dimensionless).

Volume and mass flow rate:

$$
Q = A V, \qquad \dot m = \rho Q
$$

Continuity for a pipe with two sections:

$$
A_1 V_1 = A_2 V_2
$$

Reynolds number:

$$
Re = \frac{\rho V D}{\mu}
$$

Darcy-Weisbach head loss:

$$
h_f = f \frac{L}{D} \frac{V^2}{2g}
$$

Swamee-Jain friction factor (turbulent, explicit):

$$
f = \frac{0.25}{\left[\log_{10}\!\left(\dfrac{\varepsilon}{3.7 D} + \dfrac{5.74}{Re^{0.9}}\right)\right]^2}
$$

Minor loss:

$$
h_m = K \frac{V^2}{2g}
$$

Pressure drop from head loss (horizontal pipe, same diameter):

$$
\Delta p = \rho g h_f
$$

## Worked example

**Water pipeline section.** Water at 20 °C flows through 60 m of commercial steel pipe with inside diameter 0.050 m. The volume flow rate is 0.0020 m$^3$/s. Find the mean velocity, the Reynolds number, the friction factor, the head loss, and the pressure drop.

**Given:** $L = 60$ m, $D = 0.050$ m, $Q = 0.0020$ m$^3$/s, $\rho = 998$ kg/m$^3$, $\mu = 1.00 \times 10^{-3}$ Pa s, $\varepsilon = 0.045$ mm (typical value for commercial steel).

**Find:** $V$, $Re$, $f$, $h_f$, and $\Delta p$ along the pipe.

**Assumptions:** steady, fully developed, incompressible flow. Horizontal pipe, so the pressure drop is entirely due to friction. Minor losses ignored for this section.

**Solution:**

1. Area and velocity:
   $A = \pi D^2 / 4 = \pi (0.050)^2 / 4 = 1.963 \times 10^{-3}$ m$^2$.
   $V = Q / A = 0.0020 / 1.963 \times 10^{-3} = 1.019$ m/s.
2. Reynolds number:
   $Re = \rho V D / \mu = 998 \times 1.019 \times 0.050 / 1.00\times10^{-3} = 5.08 \times 10^4$.
   Turbulent, since $Re > 4000$.
3. Relative roughness: $\varepsilon / D = 0.045 / 50 = 9.0 \times 10^{-4}$. This is in the valid range for Swamee-Jain.
4. Swamee-Jain friction factor:
   Inside the log: $\varepsilon/(3.7D) = 2.43 \times 10^{-4}$ and $5.74/Re^{0.9} = 3.34 \times 10^{-4}$. Their sum is $5.77 \times 10^{-4}$. Then $\log_{10}(5.77 \times 10^{-4}) = -3.239$, and $f = 0.25 / (3.239)^2 = 0.0238$.
5. Head loss:
   $h_f = f (L/D) V^2 / (2g) = 0.0238 \times (60/0.050) \times 1.019^2 / (2 \times 9.81) = 1.51$ m of water.
6. Pressure drop: $\Delta p = \rho g h_f = 998 \times 9.81 \times 1.51 = 1.48 \times 10^4$ Pa.

**Answer:** $V = 1.02$ m/s, $Re = 5.08 \times 10^4$ (turbulent), $f = 0.0238$, $h_f = 1.51$ m, $\Delta p \approx 14.8$ kPa.

**Sanity check:** The Colebrook equation, solved by iteration on the same inputs, gives $f = 0.0237$. The Swamee-Jain value is 0.6 percent higher, which is well inside the formula's accuracy. Doubling the flow would roughly quadruple the head loss, since $h_f$ scales with $V^2$. A 1.5 m loss over 60 m of pipe is a gradient of 2.5 percent, a reasonable value for a small water main.

## Practice

1. Water flows at 2.0 m/s in a pipe with inside diameter 0.030 m. Find the mass flow rate in kg/s, using $\rho = 998$ kg/m$^3$.
2. Water at 20 °C flows at 1.0 m/s in a 0.020 m pipe. Find the Reynolds number.
3. Laminar oil flow has $Re = 1500$, $L = 30$ m, $D = 0.020$ m, and $V = 1.0$ m/s. Find the friction factor and the head loss in m.
4. A sharp-edged entrance with $K = 0.5$ carries water at 2.0 m/s. Find the minor head loss in m.

<details><summary>Answers</summary>

1. 1.41 kg/s
2. 19 960
3. 0.0427 and 3.06 m
4. 0.102 m

</details>

## Common mistakes

- Using the diameter when the formula needs the radius, or the reverse, in $A = \pi D^2/4$.
- Using Swamee-Jain for laminar flow. Below $Re$ about 2300, use $f = 64/Re$.
- Forgetting that head loss is a height of fluid. To get a pressure drop, multiply by $\rho g$.
- Mixing units, such as roughness in mm and diameter in m. Convert everything to SI before you plug in.
- Treating every fitting as negligible. In short pipes with many elbows and valves, minor losses can be larger than the friction along the straight pipe.

## Go deeper

- [Applied Fluid Mechanics Lab Manual, Experiment 4: Energy Loss in Pipes](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Applied_Fluid_Mechanics_Lab_Manual_(Ahmari_and_Kabir)/01%3A_Lab_Manual/01.4%3A_Experiment_%234%3A_Energy_Loss_in_Pipes) by Habib Ahmari and Shah Md Imran Kabir, LibreTexts: the Darcy-Weisbach equation and friction losses, with a hands-on lab.
- [Advanced Fluid Mechanics (2.25, Fall 2013)](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/) by MIT OpenCourseWare: a free MIT course with problem sets and solutions on control volumes and internal flow.
- Previous: [Hydrostatics and Bernoulli](10-hydrostatics-and-bernoulli.md) covers the frictionless energy balance this lesson extends.
