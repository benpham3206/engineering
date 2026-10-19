# Piping and valves

**Type:** lesson

**Piping and valves** are the pipes, fittings, and valves that carry water, steam, oil, gas, and chemicals from one place to another and start, stop, or regulate the flow. An engineer sizes the pipe so the pressure loss stays acceptable, and sizes the valves and relief devices so that a sudden stop or an overpressure does not break the system.

**Prerequisites:** [Fluid systems](02-fluid-systems.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md)
**Time:** 6-10 h

## Core ideas

### How it works

A pipe carries a volume flow $Q$ from a source to a load. Continuity fixes the mean velocity from the diameter. Friction at the wall takes pressure along every metre of pipe. Each fitting and valve adds a local loss, because it narrows or turns the flow.

A valve that closes faster than a pressure wave can travel the pipe stops the moving liquid in a short time. The liquid's momentum then becomes a pressure spike at the valve. Engineers call this **water hammer**.

> [!WARNING]
> The spike can reach many times the normal working pressure.

Pumps add energy to the flow, and a pump that stops or trips also changes the flow suddenly. Surge protection devices absorb the momentum change so that the pressure rise stays within the pipe rating.

### Main parts

- Pipe: carries the fluid. The material sets the pressure rating, the roughness, and the speed at which pressure waves travel.
- Fittings: elbows, tees, and reducers. Each adds a local loss.
- Valves: isolate a section, throttle the flow, or prevent backflow.
- Supports and thrust restraints: carry the pipe weight, and resist the force that a flow change pushes on each bend.
- Relief devices: safety valves or rupture discs open when the pressure passes a set value.
- Surge protection: air chambers, surge tanks, and slow-closing valve actuators.

### Variants of valves

- Gate valve: a wedge or disk slides across the flow. It has little loss when fully open, but it is slow to operate and does not throttle well.
- Globe valve: a plug moves toward a seat. It throttles well, and it has a high loss.
- Ball valve: a rotating ball with a bore. A quarter turn opens or closes it. Its full-bore version has a very low loss, so it suits on-off service.
- Butterfly valve: a rotating disk. It is compact and cheap for large pipes, and it throttles reasonably.
- Check valve: lets flow pass in one direction only. Swing, lift, and wafer types are common.
- Pressure relief valve: a spring holds a disk closed until the fluid pressure overcomes the spring force.

## Key equations

**Continuity**, the basis of pipe sizing:

$$Q = A v = \frac{\pi D^2}{4} v \qquad \Rightarrow \qquad D = \sqrt{\frac{4Q}{\pi v}}$$

Here $Q$ is the volume flow in m$^3$/s, $A$ is the pipe area in m$^2$, $v$ is the mean velocity in m/s, and $D$ is the inside diameter in m.

Friction loss along a straight pipe, the Darcy-Weisbach form:

$$\Delta p_f = f \, \frac{L}{D} \, \frac{\rho v^2}{2}, \qquad h_f = \frac{\Delta p_f}{\rho g}$$

Here $\Delta p_f$ is the pressure drop in Pa, $f$ is the friction factor (dimensionless), $L$ is the pipe length in m, $\rho$ is the fluid density in kg/m$^3$, and $h_f$ is the head loss in m. For water, $\rho \approx 1000$ kg/m$^3$ (typical).

**Local loss** through a valve or fitting:

$$\Delta p_m = K \, \frac{\rho v^2}{2}$$

Here $K$ is the loss coefficient (dimensionless). Typical values run from about 0.1 for a full-bore ball valve to about 10 for a globe valve.

**Wave speed** in a pipe with elastic walls:

$$a = \frac{\sqrt{K_b / \rho}}{\sqrt{1 + \dfrac{K_b D}{E e}}}$$

Here $a$ is the pressure wave speed in m/s, $K_b$ is the bulk modulus of water (about $2.2 \times 10^9$ Pa, typical), $E$ is the elastic modulus of the pipe wall in Pa (about $2.0 \times 10^{11}$ Pa for steel, typical), and $e$ is the wall thickness in m.

**Joukowsky equation**, the pressure rise from a sudden change in velocity:

$$\Delta p = \rho \, a \, \Delta v \qquad \text{or, as head,} \qquad \Delta h = \frac{a \, \Delta v}{g}$$

Here $\Delta p$ is the surge pressure rise in Pa, $\Delta v$ is the change in velocity in m/s, $\Delta h$ is the surge head in m, and $g = 9.81$ m/s$^2$ (Earth surface). The equation assumes the closure is rapid, meaning the closing time $t_c$ is no longer than the round trip of the wave:

$$t_c \le t_{\mathrm{crit}} = \frac{2L}{a}$$

Here $L$ is the pipe length from the valve to the source in m. Friction and reflections are neglected, so the result is a first estimate for the valve end.

**Slow closure**, the Michaud estimate, for $t_c > 2L/a$:

$$\Delta p \approx \frac{2 \rho L v}{t_c}$$

Here $v$ is the initial velocity in m/s, and $t_c$ is the closing time in s.

## Worked example

**Part A, sizing.**

**Given:** A water main carries $Q = 0.01571$ m$^3$/s. The design velocity is $v = 2.0$ m/s. The water is at about 20 C, with kinematic viscosity $\nu = 1.0 \times 10^{-6}$ m$^2$/s (typical).

**Find:** The inside diameter $D$ and the Reynolds number.

**Solution:**

1. $D = \sqrt{4 \times 0.01571 / (\pi \times 2.0)} = 0.100$ m.
2. $\mathrm{Re} = v D / \nu = 2.0 \times 0.100 / (1.0 \times 10^{-6}) = 2.0 \times 10^{5}$.

**Answer:** $D = 0.100$ m (a 100 mm pipe). The flow is turbulent, since $\mathrm{Re}$ is far above 4000.

**Part B, water hammer.**

**Given:** The same pipe is $L = 1000$ m long and made of steel with $E = 2.0 \times 10^{11}$ Pa and wall thickness $e = 5$ mm. Water has $K_b = 2.2 \times 10^{9}$ Pa. A valve at the downstream end closes in $t_c = 0.5$ s. The steady pressure is 0.5 MPa, and the pipe is rated for 4.0 MPa. Use $g = 9.81$ m/s$^2$ (Earth surface).

**Find:** The wave speed, the surge pressure, the surge head, and whether the pipe survives.

**Solution:**

1. Wave speed: $a = \dfrac{\sqrt{2.2 \times 10^9 / 1000}}{\sqrt{1 + (2.2 \times 10^9 \times 0.100) / (2.0 \times 10^{11} \times 0.005)}} = \dfrac{1483}{\sqrt{1.22}} = 1343$ m/s.
2. Critical time: $2L/a = 2 \times 1000 / 1343 = 1.49$ s. The closing time of 0.5 s is shorter, so the closure is rapid and the Joukowsky equation applies.
3. Surge pressure: $\Delta p = 1000 \times 1343 \times 2.0 = 2.69 \times 10^{6}$ Pa, or 2.69 MPa.
4. Surge head: $\Delta h = 1343 \times 2.0 / 9.81 = 274$ m.
5. Peak pressure: $0.5 + 2.69 = 3.19$ MPa, which is below the 4.0 MPa rating.

**Answer:** The wave speed is 1343 m/s. The surge is 2.69 MPa, or 274 m of head. The peak pressure is 3.19 MPa, so the pipe holds with a margin of $4.0 / 3.19 = 1.25$.

**Sanity check:** One megapascal of water pressure is about 102 m of head, so 2.69 MPa is about 274 m. That matches step 4. If the valve closes in 3.0 s instead, the Michaud estimate gives $2 \times 1000 \times 1000 \times 2.0 / 3.0 = 1.33$ MPa, about half the rapid-closure surge. Closing time controls the surge.

## Design trade-offs

- Pipe diameter: a larger pipe lowers friction loss and velocity, which cuts noise and erosion. It also costs more and takes more space. Water designs often keep velocities near 1 to 2 m/s (typical).
- Wall thickness and pressure rating: thicker or stronger pipe raises the rating but costs more. Surge protection lowers the peak without adding wall thickness.
- Valve type: a gate valve has little loss when open, but a globe valve throttles better. The loss coefficient $K$ puts a number on that difference.
- Closing speed: a slow close reduces the surge, but a fast shutoff may be needed for safety. Engineers often choose a closing time that is longer than $2L/a$.
- Relief valve or rupture disc: a relief valve reseals after it opens and protects the system. A rupture disc does not reseal, but it can handle fluids that would stick a valve shut.
- Material: plastic pipe resists corrosion and is light, but its pressure rating falls as temperature rises. Steel is strong but needs protection from corrosion.

## How it fails

- Water hammer: a valve closes fast, or a pump trips. The warning signs are banging pipes, gauges that jump, and failing supports. Slow-closing actuators, surge tanks, air chambers, and pump check valves reduce the surge.
- Overpressure: a pump runs against a closed valve, or a relief valve fails to open. The warning sign is a gauge that climbs. Relief valves and minimum-flow protection for pumps prevent it.
- Stuck relief valve: scale or debris holds the disk closed, or the disk seizes open. The warning signs are leaking seats and valves that pop or weep. Regular testing catches both.
- Column separation: the pressure falls below the vapor pressure, and vapor cavities form in the liquid. When the cavities collapse, they can produce a spike larger than the Joukowsky estimate.
- Unrestrained bends: a flow change pushes on each bend with a large force. Thrust blocks or restraints hold the bend in place. Without them, joints can pull apart.
- Erosion and corrosion: high velocity wears elbows and tees, and scale narrows the bore. Velocity limits and water treatment reduce both.

## History

Denis Papin fitted a safety valve to a steam digester in the late 1600s, which makes it one of the earliest pressure relief devices. Nikolai Zhukovsky, also written Joukowsky, developed the theory of water hammer in the late 1890s, and his name is attached to the pressure-rise equation used here. The first edition of the ASME Boiler and Pressure Vessel Code, issued in 1914, set rules for boilers and their safety valves in the United States.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

1. Water flows at 1.5 m/s in a pipe of diameter 0.050 m. Find the volume flow $Q$ in m$^3$/s.
2. A fully open ball valve has $K = 0.1$. Water flows through it at $v = 2.0$ m/s. Find the pressure loss in pascals.
3. Find the inside diameter of a pipe that carries 0.010 m$^3$/s at a design velocity of 2.0 m/s.
4. A 100 m pipe has diameter 0.10 m and friction factor $f = 0.020$. Water flows at 2.0 m/s. Find the friction head loss in metres.
5. A pressure wave travels at $a = 1200$ m/s. The velocity drops by $\Delta v = 1.0$ m/s in a rapid closure. Find the surge pressure in MPa.

<details><summary>Answers</summary>

1. $A = \pi (0.050)^2 / 4 = 0.0019635$ m$^2$, so $Q = 0.0019635 \times 1.5 = 0.0029$ m$^3$/s.
2. $\Delta p = K \rho v^2 / 2 = 0.1 \times 1000 \times 2.0^2 / 2 = 200$ Pa.
3. $D = \sqrt{4 \times 0.010 / (\pi \times 2.0)} = 0.080$ m.
4. $h_f = f (L/D) v^2 / (2g) = 0.020 \times (100/0.10) \times 2.0^2 / (2 \times 9.81) = 4.1$ m.
5. $\Delta p = 1000 \times 1200 \times 1.0 = 1.2 \times 10^{6}$ Pa, or 1.2 MPa.

</details>

## Common mistakes

- Using the nominal pipe size as the inside diameter. Nominal sizes often differ from the real inside diameter, and the area depends on the inside diameter.
- Adding the surge to zero, instead of to the steady pressure. The peak pressure is the steady pressure plus the surge.
- Applying the Joukowsky equation to a slow closure. For a closing time longer than $2L/a$, the surge is smaller, and the Joukowsky value overstates it.
- Confusing the loss coefficient $K$ with the friction factor $f$. $K$ applies to a valve or fitting, and $f$ applies to a straight pipe.
- Using a pipe rating without checking temperature. The allowable pressure of plastic pipe falls as the temperature rises.

## Go deeper

- [*University Physics Volume 1*, Chapter 14](https://openstax.org/books/university-physics-volume-1/pages/14-introduction) by OpenStax: Bernoulli's equation, fluid dynamics, and viscosity, the base for pipe flow and losses.
- [NIST Chemistry WebBook, fluid properties](https://webbook.nist.gov/chemistry/fluid/): density, viscosity, and other property data for water at the temperature of your system.
- Related lessons: [Fluid systems](02-fluid-systems.md), [Pumps](09-pumps.md), [Compressors and fans](10-compressors-and-fans.md), [HVAC and buildings](11-hvac-and-buildings.md), [Hydraulics and pneumatics](../machines-robots/07-hydraulics-and-pneumatics.md), [Toilets and plumbing](../everyday/06-toilets-and-plumbing.md), [Pressure vessels and tanks](../structures/03-pressure-vessels-and-tanks.md).
- Related fundamentals: [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md), [Units and dimensional analysis](../../measurement/01-units-and-dimensional-analysis.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
