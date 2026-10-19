# Vacuum cleaners: airflow, suction, fan laws, cyclones, and filtration

**Type:** lesson

A vacuum cleaner is an appliance that uses a fan to pull dusty air through a hose and a filter. A cleaner that moves too little air or lacks suction fails its user even when its motor is powerful, so the balance between the two matters.

The suction at the nozzle is the pressure difference the fan creates. The useful output is the air power, which is the airflow times the pressure difference, and most of the electrical input is lost in the motor and fan. Engineers who size fans, hoses, cyclones, and filters use these relations to predict performance and to pick a filter that traps the dust that matters.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md)
**Time:** 3-4 h

## Core ideas

### How it works

A motor spins a fan that pushes air out of the cleaner. The fan lowers the pressure at its inlet, so the higher atmospheric pressure at the nozzle pushes air in through the hose. The air carries dust with it. The dust must pass a separator, such as a cyclone or a bag, and then a filter before the air leaves the cleaner.

The suction is the pressure difference, measured in pascals (Pa) or as a water column. A cleaner with a high suction lifts heavy debris, and a cleaner with high airflow carries more air through the hose. Both matter, and the air power combines them.

### Main parts

- **Motor and fan**: the motor turns the fan. The fan sets both airflow and pressure.
- **Nozzle and hose**: the nozzle sets the velocity at the floor. The hose sets the pressure loss between nozzle and cleaner.
- **Cyclone or dust bag**: separates dust from air. A cyclone uses spin, and a bag uses fabric.
- **Filter**: traps fine particles before the air leaves. Many cleaners use a HEPA filter, which is rated at 99.97% efficiency for particles of 0.3 µm (US Department of Energy standard definition).
- **Airflow path**: the duct and housing that connect the parts. Sharp bends and small openings add pressure loss.

### Variants

- **Upright with bag**: a fabric bag traps dust, and the bag fills and slowly blocks airflow.
- **Canister with cyclone**: a cyclone separator keeps dust out of the fan, which keeps suction steady.
- **Stick vacuum**: a battery motor and a small fan. Lower airflow, but compact and light.
- **Robot vacuum**: a low-power fan with a sensor-based control system. Suction is lower than a canister.

## Key equations

Assumptions for all equations below: air behaves as an incompressible fluid at about 20 °C, with density $\rho \approx 1.2\ \text{kg}/\text{m}^3$ (typical value), and the flow is steady.

Volume flow rate through a hose of uniform diameter:

$$Q = v\,A, \qquad A = \frac{\pi D^{2}}{4}$$

where $Q$ is the volume flow rate in cubic metres per second (m$^3$/s), $v$ is the mean velocity in metres per second (m/s), $A$ is the cross-section area in square metres (m$^2$), and $D$ is the hose inner diameter in metres (m).

Air power, the useful output of the fan:

$$P_{\mathrm{air}} = Q\,\Delta P$$

where $P_{\mathrm{air}}$ is in watts (W) and $\Delta P$ is the suction pressure difference in pascals (Pa). This assumes the pressure difference acts across the full airflow.

Efficiency of the motor and fan together:

$$\eta = \frac{P_{\mathrm{air}}}{P_{\mathrm{in}}}$$

where $\eta$ is dimensionless and $P_{\mathrm{in}}$ is the electrical input power in watts (W).

Dynamic (velocity) pressure in the hose:

$$p_{v} = \tfrac{1}{2}\rho v^{2}$$

where $p_{v}$ is in pascals (Pa). This assumes the flow is steady and incompressible.

Fan affinity laws, for a fan at speed $N$ with air density held constant:

$$\frac{Q_2}{Q_1} = \frac{N_2}{N_1}, \qquad \frac{\Delta P_2}{\Delta P_1} = \left(\frac{N_2}{N_1}\right)^{2}, \qquad \frac{P_2}{P_1} = \left(\frac{N_2}{N_1}\right)^{3}$$

These assume geometric similarity and a fixed fan design.

Centripetal acceleration of a particle moving on a circle of radius $r$ in a cyclone, assuming a uniform tangential speed $v_t$:

$$a = \frac{v_t^{2}}{r}$$

where $a$ is in metres per second squared (m/s$^2$), $v_t$ is in metres per second (m/s), and $r$ is in metres (m). This is the idealized acceleration that drives dust outward.

## Worked example

**Given:** A canister vacuum has airflow $Q = 0.035\ \text{m}^3/\text{s}$, suction $\Delta P = 6.0\ \text{kPa}$, and electrical input $P_{\mathrm{in}} = 1000\ \text{W}$. The hose has an inner diameter $D = 32\ \text{mm}$.

**Find:** (a) the air power, (b) the efficiency, (c) the hose velocity, and (d) the velocity pressure.

**Solution:**

1. Air power: $P_{\mathrm{air}} = 0.035 \times 6000 = 210\ \text{W}$.
2. Efficiency: $\eta = 210 / 1000 = 0.21$, which is 21%.
3. Hose area: $A = \pi (0.032)^2 / 4 = 8.04 \times 10^{-4}\ \text{m}^2$. Velocity: $v = 0.035 / 8.04 \times 10^{-4} = 43.5\ \text{m/s}$.
4. Velocity pressure: $p_v = \tfrac{1}{2} \times 1.2 \times 43.5^2 = 1136\ \text{Pa}$.

**Answer:** (a) 210 W. (b) 21%. (c) About 43.5 m/s. (d) About 1.1 kPa.

**Sanity check:** A 6 kPa suction is about 612 mm of water (1 mm of water is 9.80665 Pa), which fits a canister vacuum. An efficiency of 21% is plausible for a small fan-driven cleaner, since much of the input becomes heat in the motor. The hose velocity of 43.5 m/s, about 157 km/h, is high, and it is what lets the hose carry debris.

**Fan speed example.** Raising the fan speed 10% gives $1.10^3 = 1.331$, so the power rises about 33% while the airflow rises only 10%. Raising fan speed therefore costs power out of proportion to the airflow gained.

**Cyclone example.** With a tangential speed of $v_t = 15\ \text{m/s}$ at a radius of $r = 0.06\ \text{m}$, $a = 15^2 / 0.06 = 3750\ \text{m}/\text{s}^2$, which is about $382\ \text{g}$. Dust particles experience a large outward force, which is why the cyclone separates them.

## Design trade-offs

- **Suction versus airflow**: a narrow nozzle raises velocity and suction at the floor, but it reduces airflow. Designers balance the two for the target debris.
- **Filtration versus pressure loss**: a finer filter traps more dust but raises the pressure loss and reduces airflow over time. Bags and filters clog, so suction falls as dust builds up.
- **Noise and power**: the fan affinity laws show that power rises with the cube of speed, which makes small speed gains costly in power and noise.
- **Size and weight**: a battery stick vacuum trades suction for weight and runtime.
- **Cost**: a cyclone separator costs more than a bag but holds suction steady as it fills.

## How it fails

- **Clogged hose or filter**: airflow drops and suction falls. Warning signs are weaker pickup and a sound change.
- **Motor overheating**: blocked airflow cools the motor less, and the motor overheats and may trip a thermal cutoff. Electrical hazards include overheating, damaged cords, and water near the motor.
- **Fine dust passing a worn filter**: a torn or damaged filter lets fine particles through into the room.
- **Fire from hot ash or sparks**: hot ash in a bag or canister can ignite the bag or the plastic.
- **Fan imbalance**: a damaged fan blade vibrates and wears the bearings.

## Hierarchy of controls for hazards of dust and electricity

- **Elimination**: avoid vacuuming hot ash or liquids. Do not vacuum a wet floor with a dry-only cleaner.
- **Substitution**: use a wet-and-dry cleaner rated for liquids in place of a dry-only model. Use a HEPA filter in place of a basic filter when fine dust matters.
- **Engineering controls**: a thermal cutoff on the motor, double insulation, and a ground-fault circuit interrupter in the outlet reduce electrical risk. A sealed filter housing keeps dust in.
- **Administrative controls**: empty the dust container before it fills, replace filters on schedule, and keep the cord and nozzle undamaged.
- **Personal protective equipment**: a dust mask (rated for fine particles) when emptying the cleaner or changing a filter, especially in dusty work such as drywall or mould cleanup.

## History

Electric vacuum cleaners appeared in the early twentieth century. Hubert Cecil Booth patented a suction cleaner in England around 1901. Cyclone separators, which spin dust out of the airflow, reached household cleaners much later, after industry had used them for decades. The exact dates for that step are not certain, so this lesson gives none.

## Practice

1. A cleaner has airflow $Q = 0.02\ \text{m}^3/\text{s}$ and suction $\Delta P = 4\ \text{kPa}$. Find the air power.
2. A fan speeds up 20%. By what percentage does its power rise, assuming the affinity laws?
3. The airflow in question 1 passes a 25 mm hose. What is the velocity?
4. A cyclone has a tangential speed of 20 m/s at a radius of 0.05 m. What is the centripetal acceleration, in m/s$^2$ and in multiples of $g$?

<details><summary>Answers</summary>

1. $P_{\mathrm{air}} = 0.02 \times 4000 = 80\ \text{W}$.
2. $1.20^3 = 1.728$, so the power rises about 73%.
3. $A = \pi (0.025)^2 / 4 = 4.91 \times 10^{-4}\ \text{m}^2$, so $v = 0.02 / 4.91 \times 10^{-4} = 40.7\ \text{m/s}$.
4. $a = 20^2 / 0.05 = 8000\ \text{m}/\text{s}^2$, which is about $815\ \text{g}$.

</details>

## Common mistakes

- Using the hose diameter where the radius is needed in the area formula. Area uses $D^2$ with $\pi/4$.
- Reading suction as airflow, or the reverse. The air power needs both.
- Assuming the affinity laws hold when the fan design or air density changes. They hold only for similar fans at similar conditions.
- Believing a HEPA filter stops all particles. Its rating is for 0.3 µm particles, and it is not a guarantee for every size.
- Ignoring filter maintenance. A clogged filter cuts suction and can overheat the motor.

## Go deeper

- [OpenStax University Physics Volume 1, fluid mechanics](https://openstax.org/books/university-physics-volume-1/pages/14-introduction): pressure, density, and flow for air and fluids.
- [Thermofluids reference sheet](../../physics/reference-thermofluids.md): pipe flow, pressure loss, and fan relations.
- [Fluid systems](../../applications/thermal-fluid/02-fluid-systems.md): continuity and pipe losses, the same physics the hose follows.
- [Compressors and fans](../../applications/thermal-fluid/10-compressors-and-fans.md): fan laws and fan design in more depth.
- Related lessons: [Washing machines and dryers](03-washing-machines-and-dryers.md), [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md).
