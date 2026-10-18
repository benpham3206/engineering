# Hydrostatics and Bernoulli

Fluids push, float, and speed up or slow down in predictable ways. Hydrostatics explains why pressure grows with depth and why things float. Bernoulli's equation links pressure and speed along a flow line, and it is the first tool engineers use to size pumps, nozzles, dams, and pipes.

**Prerequisites:** [Statics](01-statics.md), [Particle dynamics and energy](02-particle-dynamics.md)
**Time:** 6-8 h

## Core ideas

- A **fluid** is a substance that deforms continuously when a shear force acts on it. Liquids and gases are both fluids.
- **Density** ($\rho$) is mass per unit volume. Typical value for fresh water: $\rho = 1000\ \text{kg/m}^3$. Typical value for air at sea level: $\rho \approx 1.2\ \text{kg/m}^3$.
- **Pressure** ($p$) is force per unit area, acting equally in all directions at a point in a fluid at rest. SI unit: pascal (Pa = N/m$^2$). US customary: psi (lbf/in$^2$). 1 psi = 6895 Pa.
- **Gauge pressure** is pressure measured relative to the local atmosphere. **Absolute pressure** is measured relative to a perfect vacuum. Absolute = gauge + atmospheric. Most tire and tank gauges read gauge pressure.
- **Hydrostatic** means the fluid is at rest. Inside a resting fluid, pressure rises with depth and does not change sideways at the same depth.
- **Pascal's principle**: a pressure change applied to an enclosed fluid is transmitted undiminished to every part of the fluid and to the container walls. This is why hydraulic presses multiply force.
- **Buoyancy**: a body in a fluid feels an upward force equal to the weight of the fluid it displaces (Archimedes' principle). The body floats if its average density is less than the fluid density. The fraction submerged equals $\rho_\text{body}/\rho_\text{fluid}$ for a floating body.
- **Steady flow** means the velocity at any fixed point does not change with time.
- **Streamline**: an imaginary line everywhere tangent to the flow velocity. In steady flow, particles travel along streamlines.
- **Incompressible** flow means density stays constant. Water is almost always treated as incompressible. Air at speeds well below about 100 m/s (Mach 0.3) is usually treated as incompressible too.
- **Inviscid** flow means we neglect friction. Bernoulli's equation assumes this, so it is only a first estimate for real pipes. Lesson 11 adds friction back in.

Engineers use these ideas to answer questions like: how deep can a dam wall be before it fails, how much force does a gate feel, how fast does water leave a hole in a tank, and how much does a pressure drop when a pipe narrows.

### Pressure in a resting fluid

Take a column of fluid with cross-section $A$ and height $h$ above a point. Its weight is $\rho g h A$. The pressure at the bottom must hold up that weight plus whatever pressure sits on top. This gives the **hydrostatic law**: the pressure increases linearly with depth.

Two points at the same depth in the same connected fluid have the same pressure. This is why a U-tube with the same fluid on both sides settles with equal levels.

### Pressure on a plane surface

The force on a submerged flat surface is the average pressure times the area. For a vertical gate whose top edge is at the free surface, the average pressure is half the bottom pressure, so the force is one half of $\rho g h_\text{bottom}$ times the area. The line of action sits below the centroid. Engineers call that offset the center of pressure. For this lesson, know the average-pressure rule and that the force acts below the centroid.

### Buoyancy

Imagine replacing the submerged part of a body with fluid. That fluid is in equilibrium, so the pressure field around it holds it up. The buoyant force equals the weight of the displaced fluid. The body's weight pulls down. A floating body sits where the two balance.

- Fully submerged body: buoyant force is $\rho_f g V$, where $V$ is the body's volume.
- Floating body: displaced volume is smaller than the body's total volume. Only the submerged volume counts.

### Bernoulli's equation

Bernoulli's equation is an energy balance written per unit volume along one streamline. For steady, incompressible, inviscid flow with no work or heat exchange:

- Pressure energy plus kinetic energy plus potential energy stays constant along a streamline.
- Faster flow means lower pressure, if height is the same.
- Higher elevation means lower pressure, if speed is the same.

Bernoulli does not give you the flow rate. It tells you how pressure and speed trade off once you know the flow.

### Limits to remember

- Bernoulli needs one streamline, or a region where all streamlines start from the same total energy.
- It ignores friction, so it overpredicts speed and underpredicts pressure drop in long pipes.
- It does not apply across pumps, turbines, or heat exchangers unless you add those energy terms.

## Key equations

Symbols: $p$ = pressure (Pa), $\rho$ = density (kg/m$^3$), $g$ = gravitational acceleration, 9.81 m/s$^2$ (32.2 ft/s$^2$), $h$ = depth or height (m), $V$ = velocity (m/s), $z$ = elevation above a reference (m), $p_\text{atm}$ = atmospheric pressure, 101 325 Pa at sea level (14.7 psi).

Hydrostatic pressure at depth $h$ below a free surface:

$$
p = p_\text{atm} + \rho g h
$$

Gauge pressure (drops $p_\text{atm}$):

$$
p_\text{gauge} = \rho g h
$$

Buoyant force on a body with submerged volume $V_\text{sub}$ in a fluid of density $\rho_f$:

$$
F_b = \rho_f g V_\text{sub}
$$

Bernoulli's equation along a streamline between points 1 and 2:

$$
p_1 + \tfrac{1}{2}\rho V_1^2 + \rho g z_1 = p_2 + \tfrac{1}{2}\rho V_2^2 + \rho g z_2
$$

Speed from a free-surface jet draining through a small hole at depth $h$ (Torricelli's result):

$$
V = \sqrt{2 g h}
$$

Continuity for incompressible flow in a pipe of area $A$ (introduced here, used in lesson 11):

$$
A_1 V_1 = A_2 V_2
$$

## Worked example

**Venturi section in a water line.** A horizontal pipe carries water. It narrows from diameter 0.10 m to 0.05 m. The flow rate is 0.010 m$^3$/s. Find the pressure drop between the wide and narrow sections.

**Given:** $D_1 = 0.10$ m, $D_2 = 0.05$ m, $Q = 0.010$ m$^3$/s, $\rho = 1000$ kg/m$^3$, pipe horizontal ($z_1 = z_2$).

**Find:** $p_1 - p_2$.

**Assumptions:** steady, incompressible, inviscid flow along one streamline from section 1 to section 2. Horizontal, so the potential energy terms cancel.

**Solution:**

1. Areas: $A_1 = \pi D_1^2/4 = \pi(0.10)^2/4 = 7.854 \times 10^{-3}$ m$^2$.
   $A_2 = \pi(0.05)^2/4 = 1.963 \times 10^{-3}$ m$^2$.
2. Velocities from $V = Q/A$:
   $V_1 = 0.010 / 7.854\times10^{-3} = 1.273$ m/s.
   $V_2 = 0.010 / 1.963\times10^{-3} = 5.093$ m/s.
3. Bernoulli with $z_1 = z_2$:
   $p_1 - p_2 = \tfrac{1}{2}\rho(V_2^2 - V_1^2) = 0.5 \times 1000 \times (5.093^2 - 1.273^2)$.
4. $5.093^2 = 25.94$ and $1.273^2 = 1.621$, so the difference is $24.32$ m$^2$/s$^2$.
   $p_1 - p_2 = 500 \times 24.32 = 1.216 \times 10^4$ Pa.

**Answer:** $p_1 - p_2 \approx 12.2$ kPa (about 1.8 psi). The wide section is at higher pressure.

**Sanity check:** Speed went up by a factor of 4, since $V_2/V_1 = (D_1/D_2)^2 = 4$. The pressure drop should be on the order of $\rho V_2^2 / 2 \approx 13$ kPa, which matches 12.2 kPa. The pressure drop is in the right range and in the right direction.

## Practice

1. Find the gauge pressure in fresh water 10.0 m below the free surface. Give the answer in kPa.
2. Find the absolute pressure at the same depth, with $p_\text{atm} = 101.3$ kPa. Give the answer in kPa.
3. Water drains from a hole 5.00 m below the free surface of an open tank. Find the exit speed in m/s, ignoring losses.
4. A wood block of density 500 kg/m$^3$ and volume 0.0100 m$^3$ floats in fresh water. Find the submerged volume in m$^3$.
5. In the worked example, the narrow section diameter is halved again to 0.025 m with the same flow rate. Find the new pressure drop between the 0.10 m and 0.025 m sections in kPa.

<details><summary>Answers</summary>

1. 98.1 kPa
2. 199.4 kPa
3. 9.90 m/s
4. 0.00500 m$^3$
5. 206.7 kPa

</details>

## Common mistakes

- Using total depth instead of depth below the free surface, or forgetting to add $p_\text{atm}$ when the problem asks for absolute pressure.
- Mixing gauge and absolute pressures in the same Bernoulli balance. Use one consistently.
- Applying Bernoulli across a pump, turbine, or a long pipe where friction matters.
- Using $\rho_\text{body}$ instead of $\rho_\text{fluid}$ in the buoyancy formula, or using the total volume of a floating body instead of the submerged volume.
- Forgetting that a narrow section means higher speed, which means lower pressure, not higher.

## Go deeper

- [Bernoulli's Equation](https://www.grc.nasa.gov/www/k-12/airplane/bern.html) by NASA Glenn Research Center: a plain-language explanation of pressure, speed, and the Bernoulli relation.
- [Advanced Fluid Mechanics (2.25, Fall 2013)](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/) by MIT OpenCourseWare: a free MIT fluid mechanics course with problem sets and solutions for after you finish this lesson.
- Next: [Control volumes and pipe flow](11-control-volumes-pipe-flow.md) adds friction and mass and energy balances to what you learned here.
