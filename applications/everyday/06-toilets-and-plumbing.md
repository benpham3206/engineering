# Toilets and plumbing

**Type:** lesson

A toilet moves waste with a short burst of water, and the plumbing around it keeps sewer gas out of the room and water flowing at a usable pressure. Engineers size the tank, the trap, and the vent so that each flush clears the bowl and the trap keeps its water seal. Water pressure in a building comes from the utility supply or a pump, and every fixture must work at the pressure it receives.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md), [Pumps](../thermal-fluid/09-pumps.md)
**Time:** 4-6 h

## Core ideas

### How it works

A gravity flush uses the height of stored water. The tank sits above the bowl. When the flush valve opens, water drops into the bowl through the rim jets, and the bowl fills. The water pushes into the trap, which is a U-shaped pipe. When the water in the trap reaches the top of the bend, the trap starts to siphon. The siphon pulls the bowl and the trap empty, and it does so with less water than a plain drain would need.

The trap holds a water seal, typically about 50 mm (2 in) deep in building codes. That seal blocks sewer gas from rising into the room. A vent pipe connects the drain system to outdoor air. The vent keeps the air pressure in the drain near atmospheric pressure. Without a vent, a large flow can pull the seal out of the trap.

Water pressure depends on height. Water at rest at depth $h$ below a free surface has gauge pressure $\rho g h$. A tank 3 m above the bowl gives about 29 kPa at the bowl, and a fixture 6 m above the supply meter sees about 59 kPa less than the meter pressure.

### Main parts

- **Tank (cistern):** holds the flush water and includes a float-operated fill valve and an overflow tube.
- **Flush valve:** a rubber flapper that opens to start the flush and closes to stop it.
- **Fill valve:** refills the tank to a set level, and its float shuts the valve off.
- **Rim and jets:** spread the water around the bowl.
- **Bowl and trap:** the bowl holds the waste, and the trap holds the seal and forms the siphon.
- **Drain and soil stack:** carry waste away, sized so that flow runs without blocking.
- **Vent stack:** admits air to the drain system.
- **Supply line and shutoff:** bring water to the fill valve. A pressure regulator limits the pressure where the supply is too high.

### Variants

Gravity toilets are the most common in homes. Pressure-assisted toilets use a pressurized tank, so they flush with more force for a given volume. Dual-flush toilets offer a short flush for liquids and a full flush for solids. Vacuum-assisted toilets, used in aircraft and some ships, pull waste with air pressure rather than gravity. Composting toilets separate waste and handle little or no water.

## Key equations

Assumptions for every equation below: the water is incompressible at 1000 kg/m$^3$, the fluid is at a steady temperature, gravity is uniform at $g = 9.81\ \text{m/s}^2$ (Earth surface, true near sea level and mid latitudes), and the flow is steady in each pipe section.

- Static pressure: $p = \rho g h$, where $p$ is gauge pressure in pascals (Pa), $\rho$ is water density in kg/m$^3$, $g$ is gravitational acceleration in m/s$^2$, and $h$ is depth below the free surface in metres (m). The assumption is that the water is at rest.
- Pressure change with height: $p_2 = p_1 - \rho g \, \Delta z$, where $\Delta z$ is the height gain in metres. The assumption is that the water is at rest between the two points.
- Volume flow: $Q = A v$, where $Q$ is volume flow rate in cubic metres per second (m$^3$/s), $A$ is the pipe cross-section in m$^2$, and $v$ is the mean velocity in m/s. The assumption is that the flow is steady and incompressible.
- Trap seal pressure: $\Delta p = \rho g h_s$, where $h_s$ is the seal depth in metres. This gives the pressure that the seal can hold against gas pressure from the drain. The assumption is that the seal is a column of still water.

## Worked example

**Given:** A house has a supply at a meter at $p_1 = 350\ \text{kPa}$ gauge. A second-floor bathroom fixture sits $\Delta z = 6\ \text{m}$ above the meter, with the water at rest. A 20 mm supply pipe carries $Q = 0.5\ \text{L/s}$ to the fixture. The trap seal is $h_s = 50\ \text{mm}$ deep. Gravity is $g = 9.81\ \text{m/s}^2$ (Earth surface).

**Find:** (a) the static pressure at the fixture, (b) the mean velocity in the 20 mm pipe, and (c) the pressure that the trap seal can hold.

**Solution:**

1. Static pressure at the fixture: $p_2 = p_1 - \rho g \Delta z = 350\,000 - 1000 \times 9.81 \times 6 = 291\,140\ \text{Pa}$, which is about $291\ \text{kPa}$ or $42\ \text{psi}$.
2. Pipe area: $A = \pi D^2 / 4 = \pi (0.020)^2 / 4 = 3.14 \times 10^{-4}\ \text{m}^2$.
3. Mean velocity: $v = Q / A = 0.0005 / 3.14 \times 10^{-4} = 1.59\ \text{m/s}$.
4. Trap seal pressure: $\Delta p = \rho g h_s = 1000 \times 9.81 \times 0.050 = 490\ \text{Pa}$.

**Answer:** (a) $291\ \text{kPa}$. (b) $1.59\ \text{m/s}$. (c) $490\ \text{Pa}$.

**Sanity check:** Lifting the fixture 6 m costs about 59 kPa, which is a fifth of the supply pressure. The velocity of 1.6 m/s is moderate for a water pipe. The seal of 490 Pa is small, so a drain that pulls more than that vacuum loses its seal. The vent exists for that reason.

## Design trade-offs

- **Water per flush.** The United States federal standard set a 1.6 gallon (about 6 L) maximum per flush from 1994. The EPA WaterSense label marks newer toilets that use at most 1.28 gallons (about 4.8 L) per flush. Less water saves water but gives less flush force, so the bowl shape and the jet layout must do more work.
- **Trap seal depth.** A deeper seal blocks more gas but raises the risk of a clog and needs more water to refill.
- **Vent size.** A small vent gives a gurgling drain. A large vent costs more pipe and roof penetrations.
- **Supply pressure.** High pressure makes fill valves hiss and pipes leak. Many building codes require a pressure regulator when the supply is above about 80 psi (about 550 kPa). Low pressure makes a weak flush and a slow refill.
- **Pipe velocity.** Faster drain flow carries solids along. Slow flow lets solids settle and block the pipe.

## Safety and the hierarchy of controls

Plumbing hazards include sewer gas, contaminated drinking water, scalding, and flooding. The controls apply in this order.

- **Elimination.** Remove the hazard. A gravity toilet with no tank needs no tank water. A composting toilet removes the water-borne waste stream, although it adds handling of solid waste.
- **Substitution.** Replace a hazard with a lower one. A thermostatic mixing valve replaces an unregulated hot supply, so the outlet temperature stays near a safe set point.
- **Engineering controls.** Build the protection in. Examples are the trap seal, the vent, the anti-siphon fill valve whose inlet sits above the overflow line, the backflow preventer or air gap that stops fixture water from reaching the drinking supply, and the pressure regulator.
- **Administrative controls.** Set rules for work and use. Plumbers follow the local code, a licensed inspector checks the work, and owners do not connect unlicensed fixtures.
- **Personal protective equipment.** Gloves and eye protection protect the worker during repair and cleaning. They are the last line and apply only after the layers above.

## How it fails

- **Running toilet.** A worn flapper leaks water from the tank into the bowl, and the fill valve runs. The sound and a rising water bill are the warning signs.
- **Slow or weak flush.** Clogged rim jets, low tank water, or a partial blockage in the trap reduce the flush. A clear jet and a full tank fix most cases.
- **Trap siphonage.** A drain flow with no vent pulls the seal out of the trap, and sewer gas enters the room. A bad smell and a gurgling sound are the warning signs.
- **Cross-connection.** A fixture or hose connected below the water level can draw waste water back into the drinking supply. Backflow preventers and air gaps stop this path.
- **Water hammer.** A valve that closes quickly makes a pressure spike in the supply. Air chambers and pipe supports reduce the shock.
- **Freezing.** Water in an exposed pipe expands on freezing and can split the pipe. Insulation and drainage prevent it.

## History

Sir John Harington described a water closet with a flush valve in 1596. Alexander Cumming patented an S-shaped trap in London in 1775, and the trap seal became a standard way to keep gas out of the room. Joseph Bazalgette designed London's main sewer system after the Great Stink of 1858, a public health crisis that pushed the city to rebuild its drainage.

Thomas Crapper was a sanitary plumber in London in the late nineteenth century, and he held patents for toilet parts. He did not invent the flush toilet, and the word "crap" does not come from his name.

## Practice

Where a problem needs gravitational acceleration, use $g = 9.81\ \text{m/s}^2$ (Earth surface).

1. A tank sits 2.0 m above a bowl. Find the gauge pressure at the bowl in kilopascals.
2. A flush releases 6 L of water in 4.0 s. Find the mean volume flow rate in litres per second.
3. A trap seal is 50 mm deep. Find the pressure the seal can hold in pascals.
4. A 25 mm drain pipe carries 1.5 L/s. Find the mean velocity in metres per second.

<details><summary>Answers</summary>

1. $p = \rho g h = 1000 \times 9.81 \times 2.0 = 19.6\ \text{kPa}$.
2. $Q = 6\ \text{L} / 4.0\ \text{s} = 1.5\ \text{L/s}$.
3. $\Delta p = \rho g h_s = 1000 \times 9.81 \times 0.050 = 490\ \text{Pa}$.
4. $A = \pi (0.0125)^2 = 4.91 \times 10^{-4}\ \text{m}^2$, so $v = 0.0015 / 4.91 \times 10^{-4} = 3.06\ \text{m/s}$.

</details>

## Common mistakes

- Thinking the flush empties the bowl by gravity alone. The siphon does most of the work once the trap fills.
- Assuming the trap seal lasts forever. A floor drain that no one uses dries out, and its seal disappears.
- Forgetting that pressure falls with height. A fixture 10 m above the supply sees about 98 kPa less.
- Connecting a hose or a fixture below the water level without a backflow device. This can contaminate the drinking supply.
- Repeating the Thomas Crapper myth. He was a plumber and a patent holder, not the inventor of the toilet.

## Go deeper

- [EPA WaterSense: residential toilets](https://www.epa.gov/watersense/residential-toilets): the U.S. Environmental Protection Agency page on water use per flush for newer toilets.
- [Reference: thermofluids](../../physics/reference-thermofluids.md): the pressure, flow, and energy equations used in this lesson.
- [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md) for pressure at depth and the energy balance along a streamline.
- [Piping and valves](../thermal-fluid/12-piping-and-valves.md) for pipe sizing, valve types, and water hammer.
- [Pumps](../thermal-fluid/09-pumps.md) for the pumps that raise pressure in buildings with high fixtures.
