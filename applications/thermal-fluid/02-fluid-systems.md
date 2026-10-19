# Fluid systems: continuity, Bernoulli, pumps, and pipe losses

**Type:** lesson

A **fluid system** is a set of pipes, ducts, and pumps that moves water, air, or oil from one place to another. A fluid system sized wrongly delivers too little flow or wastes pump power. Engineers size the pipe,
choose the pump, and check that the pressure stays in range. Three ideas cover most of the work:
mass is conserved, energy is conserved along a streamline, and friction takes energy away.

**Prerequisites:** [Thermal systems](01-thermal-systems.md), [Algebra](../../math/01-algebra.md)
**Time:** 10-14 h

## Core ideas

- **Fluid**: a substance that flows and takes the shape of its container. Liquids are nearly
  incompressible, and gases are compressible. This lesson treats water as incompressible.
- **Density** $\rho$ (kg/m$^3$): mass per unit volume. Water is about $1000\ \text{kg}/\text{m}^3$.
- **Pressure** $p$ (pascals, Pa): force per unit area. Hydrostatic pressure grows with depth.
- **Volume flow rate** $Q$ (m$^3$/s): the volume of fluid passing a point per second.
- **Velocity** $v$ (m/s): the average speed of the fluid across a pipe.
- **Continuity** (conservation of mass): for an incompressible fluid in a pipe, the flow rate is the same
  everywhere. A narrow section must be faster than a wide one.
- **Bernoulli's equation**: along a streamline with no friction, pressure plus kinetic energy per volume
  plus potential energy per volume stays constant. Faster flow means lower pressure, when height is the
  same.
- **Head**: energy per unit weight, expressed as a height in metres. Pump head is the height the
  pump can lift the fluid, equal to the energy it adds per unit weight.
- **Friction and head loss**: fluid rubbing on a pipe wall loses energy. The loss depends on pipe length,
  diameter, velocity, and wall roughness.
- **Laminar and turbulent flow**: the Reynolds number $\mathrm{Re} = \rho v D / \mu$ tells you which. Low $\mathrm{Re}$ is
  smooth, layered flow, and high $\mathrm{Re}$ is mixed, turbulent flow. Above about 4000 in a pipe, the flow is
  usually turbulent.
- **Pump power**: the pump must add energy at the rate of flow times head. Its efficiency $\eta$ says how
  much of its input power reaches the fluid.

## Key equations

- Continuity: $Q = A_1 v_1 = A_2 v_2$, where $A$ is the pipe cross-section in square metres (m$^2$).
- Circular pipe area: $A = \pi D^2 / 4$, with $D$ the diameter in metres.
- Bernoulli (no friction), in pascals: $p_1 + \tfrac{1}{2}\rho v_1^2 + \rho g z_1 = p_2 + \tfrac{1}{2}\rho v_2^2 + \rho g z_2$,
  where $g$ is the local gravitational acceleration (9.81 m/s$^2$ at Earth's surface) and $z$ is height in metres.
- Pump power (hydraulic): $P = \rho g Q H$, in watts, where $H$ is head in metres.
- Shaft (input) power: $P_{\mathrm{in}} = \rho g Q H / \eta$.
- Reynolds number: $\mathrm{Re} = \rho v D / \mu$, with dynamic viscosity $\mu$ in Pa s. For water at about 20 C,
  $\mu / \rho \approx 1.0 \times 10^{-6}\ \text{m}^2/\text{s}$ (typical value), so $\mathrm{Re} \approx v D / (1.0 \times 10^{-6})$.
- Darcy-Weisbach head loss: $h_f = f \dfrac{L}{D} \dfrac{v^2}{2g}$, with $f$ the friction factor (dimensionless)
  and $L$ the pipe length in metres.

## Worked example

**Given:** A pump moves water at $Q = 0.005\ \text{m}^3/\text{s}$ (5 L/s) against a head of $H = 15\ \text{m}$. Gravity is $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).
Water density is $\rho = 1000\ \text{kg}/\text{m}^3$, and the pump efficiency is $\eta = 0.60$. A second pipe
of diameter $D = 0.025\ \text{m}$ carries water at $v = 1.0\ \text{m/s}$.

**Find:** (a) the hydraulic power delivered to the water, (b) the input power the motor must supply,
and (c) the Reynolds number in the $25\ \text{mm}$ pipe.

**Solution:**

1. Hydraulic power: $P = \rho g Q H = 1000 \times 9.81 \times 0.005 \times 15 = 736\ \text{W}$.
2. Input power: $P_{\mathrm{in}} = 736 / 0.60 = 1226\ \text{W}$, which is about $1.23\ \text{kW}$.
3. Reynolds number: $\mathrm{Re} = v D / (1.0\times10^{-6}) = 1.0 \times 0.025 / 1.0\times10^{-6} = 25\,000$.

**Answer:** (a) $736\ \text{W}$. (b) $1.23\ \text{kW}$. (c) $\mathrm{Re} = 25\,000$, which is turbulent.

**Sanity check:** Efficiency means the input must be larger than the hydraulic power. $1226 > 736$, so
that holds. The Reynolds number of $25\,000$ is well above 4000, so turbulent flow is expected for a
water pipe at this speed.

## How it fails

- **Cavitation.** When the local pressure drops below the vapor pressure, bubbles form and collapse against metal. The signs are a gravel noise, vibration, and pitted impellers. Keep the net positive suction head available above what the pump requires, with a margin, by raising the supply level, lowering suction losses, or reducing the temperature.
- **Water hammer.** A valve that closes quickly stops a moving column of liquid, and the pressure spike can burst pipes or break supports. The signs are a bang and shaking pipes. Close valves slowly, add surge tanks or accumulators, and fit relief valves.

- **Leaks.** Gaskets, seals, and threaded joints wear, corrode, and loosen. The sign is a drip, a stain, or a falling pressure. Choose compatible materials, tighten to specification, and inspect on schedule. A small leak can grow, so find it early.
- **Erosion and corrosion.** High velocity, solids, and bubbles wear the pipe wall, especially at elbows and throttle points. Chemical attack thins the wall as well. The sign is thin walls on inspection. Limit the velocity, use harder or lined materials, and add a corrosion allowance.
- **Blockage and clogging.** Debris, scale, or a closed valve restricts the flow, so the pressure drop rises and the flow falls. A strainer upstream of pumps and valves catches debris, and a differential pressure gauge across it shows when it needs cleaning.
- **Air in the line.** Trapped air reduces flow, causes noise, and can lock a pump. Vents at high points and sloped pipes let air escape.
- **Overpressure.** A closed valve, a blocked line, or heating of trapped liquid raises pressure past the pipe rating. A relief valve set below the maximum allowable working pressure protects the system, and it must discharge to a safe place.
- **Freezing.** Water expands when it freezes and splits pipes. Insulation, heat tracing, drains, and antifreeze prevent it.
- **Stored pressure and spilled fluid.** A pressurized line can release a jet that injures or injects fluid through skin. Eliminate the hazard by depressurizing, substitute lower pressure or a safer fluid, add guards, relief valves, and shielding as engineering controls, then use procedures and training, and wear eye and face protection last. For maintenance, apply lockout/tagout: close and lock the isolation valves, bleed the pressure, drain the line, and verify zero pressure at a gauge before opening any joint.


## Practice

1. A pipe narrows from $D_1 = 0.050\ \text{m}$ to $D_2 = 0.025\ \text{m}$. The flow in the wide pipe is
   $v_1 = 2.0\ \text{m/s}$. Find $v_2$.
2. A pump moves $Q = 0.010\ \text{m}^3/\text{s}$ against $H = 20\ \text{m}$ with $\eta = 0.75$. Find its
   input power in watts.
3. Water flows at $v = 0.50\ \text{m/s}$ in a $0.020\ \text{m}$ pipe. Find the Reynolds number, using
   $\nu = 1.0\times10^{-6}\ \text{m}^2/\text{s}$.
4. A $50\ \text{m}$ pipe of diameter $0.10\ \text{m}$ has $f = 0.025$ and carries water at $v = 2.0\ \text{m/s}$.
   Find the head loss.
5. Water at $1.0\ \text{m/s}$ in a horizontal pipe speeds up to $2.0\ \text{m/s}$ at a constriction. Ignoring
   friction, find the pressure drop in pascals.

<details><summary>Answers</summary>

1. $v_2 = 8.0\ \text{m/s}$
2. $2620\ \text{W}$
3. $10\,000$
4. $2.55\ \text{m}$
5. $1500\ \text{Pa}$

</details>

## Common mistakes

- Using diameter where the formula needs radius, or the reverse. Area uses $D^2$ with $\pi/4$.
- Forgetting that pump power must be divided by efficiency to get the motor input.
- Applying Bernoulli across a pump or a valve, where energy is added or lost. Bernoulli needs a
  streamline with no added energy and no friction.
- Mixing units for viscosity and density. Use $\nu = \mu / \rho$ in $\text{m}^2/\text{s}$ for quick checks.
- Believing a faster pipe always has lower pressure. Bernoulli compares two points at the same height.

## Go deeper

- [*Fluid Mechanics*, Wikibooks](https://en.wikibooks.org/wiki/Fluid_Mechanics) by Wikibooks contributors:
  an open text on fluid statics and turbulent flow.
- [*University Physics Volume 1*, Chapter 14 (fluid mechanics)](https://openstax.org/books/university-physics-volume-1/pages/14-introduction)
  by OpenStax: fluids, Pascal's principle, buoyancy, Bernoulli's equation, and viscosity.
- Next: [Lesson 07, projects](../projects/01-project-ladder.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
