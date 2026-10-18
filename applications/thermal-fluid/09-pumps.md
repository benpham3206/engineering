# Pumps

**Type:** lesson

A pump adds energy to a liquid so that it flows through pipes, up a tower, or into a pressurized system. Engineers pick a pump by matching its curve to the system it serves, and a poor match wastes energy or destroys the pump.

**Prerequisites:** [Fluid systems](02-fluid-systems.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md)
**Time:** 6-8 h

## Core ideas

### How it works

A pump moves liquid by one of two principles. A centrifugal pump spins an impeller. Liquid enters near the center, the vanes throw it outward, and it leaves the rim at high speed. A volute or diffuser then slows the liquid, and the lost kinetic energy turns into pressure. A positive displacement pump traps a fixed volume of liquid and pushes it forward. Gears, pistons, diaphragms, and peristaltic rollers all work this way.

For a centrifugal pump, the head the impeller can add depends on the speed of the rim. The rim speed is $u = \omega r$, where $\omega$ is the shaft speed in rad/s and $r$ is the impeller radius in metres. The ideal head rises with the square of rim speed, so doubling the shaft speed quadruples the ideal head. Real head is lower because of friction, slip in the vanes, and leakage.

A positive displacement pump delivers a flow set almost entirely by its speed. Each revolution moves a fixed volume $V_d$, so $Q = V_d N$, with $N$ the rotation rate in revolutions per second. The pressure it makes depends on the load, not on the pump. If the outlet is blocked, the pressure rises until something breaks. A relief valve prevents that.

### Pump curves and the operating point

A pump curve plots head against flow at one speed. For a centrifugal pump, head falls as flow rises. Efficiency rises from zero at zero flow to a peak, then falls. The peak is the best efficiency point, and the pump should run near it.

The system has its own curve. Static lift $z$ is the height the liquid must climb, and friction adds a loss that grows with the square of flow:

$$H_{sys} = z + k Q^2$$

Here $k$ in s$^2$/m$^5$ lumps the pipe length, diameter, and fittings into one number. The pump runs where its curve crosses the system curve. Closing a valve moves the system curve up, so the operating point moves to lower flow and higher head.

### Cavitation and NPSH

Cavitation happens when the local pressure in the liquid falls below its vapour pressure. Vapour bubbles form, then collapse violently in higher-pressure regions. The collapse causes noise, vibration, pitting of the impeller, and a drop in head.

The net positive suction head available is the head that the system gives at the pump inlet above the vapour pressure:

$$NPSH_a = \frac{p_a - p_v}{\rho g} + z_s - h_{fs}$$

Here $p_a$ is the pressure on the liquid surface in pascals, $p_v$ is the vapour pressure at the liquid temperature in pascals, $z_s$ is the height of the liquid surface above the pump centerline in metres (negative for a suction lift), and $h_{fs}$ is the friction loss in the suction line in metres. The pump needs its own minimum, $NPSH_r$, which the manufacturer measures. The rule is $NPSH_a > NPSH_r$, with a margin that the designer sets, commonly 1 m or more.

### Affinity laws

Affinity laws predict how a pump changes when its speed or impeller changes, with the same liquid and the same efficiency:

$$\frac{Q_2}{Q_1} = \frac{N_2}{N_1}, \qquad \frac{H_2}{H_1} = \left(\frac{N_2}{N_1}\right)^2, \qquad \frac{P_2}{P_1} = \left(\frac{N_2}{N_1}\right)^3$$

Trimming an impeller diameter $D$ at fixed speed gives approximate ratios $Q \propto D$, $H \propto D^2$, and $P \propto D^3$. These hold for small trims. Large trims change the vane geometry, so the laws stop being accurate.

### Main parts

- **Impeller.** It adds energy to the liquid. Open, semi-open, and closed impellers suit different solids content.
- **Volute or diffuser.** It collects the flow and turns speed into pressure.
- **Shaft and bearings.** They carry the impeller and the radial and axial loads.
- **Seal.** A packed stuffing box leaks slowly and needs adjustment. A mechanical seal leaks almost nothing but needs clean liquid and cooling.
- **Casing.** It holds the pressure and takes the suction and discharge nozzles.
- **Drive.** A motor and coupling, or a variable speed drive that changes the shaft speed.

### Variants

Centrifugal pumps are the most common. They are cheap for large flow, and they deliver a smooth, steady flow. Their head falls with flow, so a centrifugal pump cannot make high pressure at low flow without many stages.

Gear, lobe, and vane pumps suit viscous fluids and steady metering. Piston and plunger pumps make very high pressure, used in high-pressure cleaners and oilfield injection. Diaphragm pumps handle corrosive and slurry duty without a shaft seal. Peristaltic pumps squeeze a tube and keep the liquid away from all moving parts, which suits sterile and dosing work.

## Key equations

- Hydraulic power: $P = \rho g Q H$ in W, from the fluid systems lesson.
- Shaft power: $P_{shaft} = \rho g Q H / \eta$ in W, where $\eta$ is dimensionless efficiency.
- Positive displacement flow: $Q = V_d N$, with $V_d$ in m$^3$ per revolution and $N$ in rev/s.
- System curve: $H_{sys} = z + k Q^2$, with $z$ in m, $k$ in s$^2$/m$^5$, and $Q$ in m$^3$/s.
- Net positive suction head available: $NPSH_a = (p_a - p_v)/(\rho g) + z_s - h_{fs}$, in m.
- Affinity laws for speed: $Q \propto N$, $H \propto N^2$, $P \propto N^3$, with $N$ in rev/min.

## Worked example

**Given:** A centrifugal pump runs at $N_1 = 1450$ rev/min and delivers $Q_1 = 0.020\ \text{m}^3/\text{s}$ of water against $H_1 = 25\ \text{m}$. Its efficiency is $\eta = 0.72$. Water density is $\rho = 1000\ \text{kg/m}^3$. The motor slows the pump to $N_2 = 1160$ rev/min, and the efficiency stays at 0.72.

**Find:** (a) the shaft power at full speed, (b) the flow, head, and shaft power at the new speed.

**Solution:**

1. Hydraulic power at full speed: $P_h = 1000 \times 9.81 \times 0.020 \times 25 = 4905\ \text{W}$.
2. Shaft power at full speed: $P_1 = 4905 / 0.72 = 6812\ \text{W}$, which is about $6.81\ \text{kW}$.
3. Speed ratio: $N_2/N_1 = 1160/1450 = 0.80$.
4. New flow: $Q_2 = 0.80 \times 0.020 = 0.016\ \text{m}^3/\text{s}$.
5. New head: $H_2 = 0.80^2 \times 25 = 16.0\ \text{m}$.
6. New shaft power: $P_2 = 0.80^3 \times 6812 = 3488\ \text{W}$, which is about $3.49\ \text{kW}$.

**Answer:** (a) $6.81\ \text{kW}$. (b) $Q_2 = 0.016\ \text{m}^3/\text{s}$, $H_2 = 16\ \text{m}$, and $P_2 = 3.49\ \text{kW}$.

**Sanity check:** Slowing the pump by 20 percent cut the power to 0.512 of its full-speed value. The head fell to 0.64 of its value, which matches the square law. The affinity laws assume constant efficiency, so the real power at the new speed may differ by a few percent.

## Design trade-offs

Efficiency is the first concern, because a pump runs for years and its energy use often costs more than the pump itself. Choosing a pump whose best efficiency point sits near the normal duty point saves more energy than any other single choice.

Speed sets the size and the cost. A higher speed gives more head from a smaller impeller, but it raises wear, noise, and the NPSH the pump needs. Low speed suits liquids that cavitate easily.

Throttling a valve wastes energy, because the pump still makes the full head and the valve drops it. A variable speed drive matches the flow with less energy. At 80 percent speed the shaft power falls to about half, as the worked example shows.

Material choice trades cost against corrosion and abrasion. Cast iron and bronze are common for water. Stainless steel and duplex steels handle seawater and acids. Slurries need hardened or rubber-lined parts.

## How it fails

**Cavitation.** A pump that sounds like gravel is cavitating. The warning signs are noise, vibration, falling discharge pressure, and pitting on the impeller. The cause is low $NPSH_a$, often from a clogged suction strainer, a hot liquid, or a suction lift that is too high. The fix is more submergence, a larger suction pipe, or a lower speed.

**Dead heading.** A centrifugal pump with a closed discharge valve keeps running at zero flow. The energy it adds heats the liquid inside the casing, and the liquid can boil. Most designs add a minimum flow bypass for this reason.

**Dry running.** A pump with no liquid overheats its mechanical seal in seconds. Level switches and a run dry interlock prevent it.

**Overpressure in positive displacement pumps.** These pumps push against any blockage. A relief valve on the discharge, sized for the pump, limits the pressure. Without one, a pipe or the pump casing can burst.

**Air and vapour entrainment.** Air drawn through a suction leak or a vortex at a low tank level reduces the flow and causes cavitation. Vortex breakers and sealed suction lines prevent it.

## History

Archimedes and the Alexandrian engineer Ctesibius both described water-lifting machines in the third century BC. The screw of Archimedes lifts water by turning, and Ctesibius built a force pump with a piston. Denis Papin described a centrifugal pump in about 1689. Centrifugal pumps became common in the late nineteenth century, when electric motors and steam engines could drive them at high speed. Their design rules matured through the twentieth century.

## Practice

1. A pump moves $Q = 0.012\ \text{m}^3/\text{s}$ of water against $H = 18\ \text{m}$ with $\eta = 0.70$. Find the shaft power in watts.
2. A pump runs at 1450 rev/min and delivers $Q = 0.020\ \text{m}^3/\text{s}$ against $H = 25\ \text{m}$. Find the flow and head when it runs at 1000 rev/min, and find the ratio of its new shaft power to its old one.
3. A pump sits $2.5\ \text{m}$ above the surface of a tank of water at 20 C. The atmosphere presses at $101.3\ \text{kPa}$, the vapour pressure is $2.34\ \text{kPa}$, and the suction line loses $0.8\ \text{m}$. Find $NPSH_a$. The manufacturer gives $NPSH_r = 3.0\ \text{m}$. Find the margin.
4. A pump makes $H_1 = 30\ \text{m}$ with a full-diameter impeller. The impeller is trimmed by 10 percent in diameter at the same speed. Find the new head, using the approximate trim law.
5. A gear pump displaces $12\ \text{cm}^3$ per revolution and runs at 1200 rev/min. Find its theoretical flow in litres per second.

<details><summary>Answers</summary>

1. $P_{shaft} = 1000 \times 9.81 \times 0.012 \times 18 / 0.70 = 3027\ \text{W}$, which is about $3.03\ \text{kW}$.
2. $Q_2 = 0.020 \times 1000/1450 = 0.0138\ \text{m}^3/\text{s}$. $H_2 = 25 \times (1000/1450)^2 = 11.9\ \text{m}$. The power ratio is $(1000/1450)^3 = 0.33$.
3. $NPSH_a = (101\,325 - 2340)/(1000 \times 9.81) - 2.5 - 0.8 = 6.8\ \text{m}$. The margin is $6.8 - 3.0 = 3.8\ \text{m}$, so the design is safe.
4. $H_2 = 30 \times 0.90^2 = 24.3\ \text{m}$. Flow falls to 0.90 of its value, and power falls to $0.90^3 = 0.73$ of its value.
5. $Q = 12 \times 10^{-6}\ \text{m}^3 \times 20\ \text{rev/s} = 2.4 \times 10^{-4}\ \text{m}^3/\text{s} = 0.24\ \text{L/s}$.

</details>

## Common mistakes

- Using the affinity laws for a change of fluid. They assume the same liquid, so a change in density or viscosity needs a new curve.
- Reading the NPSH margin backwards. $NPSH_a$ is what the system provides, and $NPSH_r$ is what the pump needs.
- Forgetting the sign of the suction height. A pump above the liquid surface has a negative $z_s$, and that reduces $NPSH_a$.
- Sizing the motor from the hydraulic power alone. Divide by efficiency, and add a margin for the curve shifting.
- Choosing a pump from its maximum head without checking the system curve. The pump runs where the two curves cross, not at its maximum.

## Go deeper

- [University Physics Volume 1, Chapter 14 (fluid mechanics)](https://openstax.org/books/university-physics-volume-1/pages/14-introduction) by OpenStax: fluid pressure, buoyancy, and Bernoulli's equation, the physics behind head and suction pressure.
- [Fluid Mechanics, Wikibooks](https://en.wikibooks.org/wiki/Fluid_Mechanics) by Wikibooks contributors: an open text on fluid statics and control-volume analysis.
- Related: [Fluid systems](02-fluid-systems.md) for the power and head basics, and [Compressors and fans](10-compressors-and-fans.md) for the same affinity logic applied to gas.
- Related: [Hydraulics and pneumatics](../machines-robots/07-hydraulics-and-pneumatics.md) for pumps as they drive machine actuators.
