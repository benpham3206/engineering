# Wind turbines

**Type:** lesson

**Wind turbines** are machines that take kinetic energy from moving air and turn it into electricity. A turbine's output is set by the wind speed and the size of its rotor, so every design starts from those two numbers.

Engineers need to understand them because the power in the wind rises with the cube of the wind speed, and no rotor can capture all of it.

**Prerequisites:** [Hydrostatics and Bernoulli](../../physics/10-hydrostatics-and-bernoulli.md), [Control volumes and pipe flow](../../physics/11-control-volumes-pipe-flow.md), [Fluid systems](../thermal-fluid/02-fluid-systems.md)
**Time:** 6-8 h

## Core ideas

### How it works

Moving air carries kinetic energy. A rotor in the wind slows the air, and the slowed air gives up some of its energy to the blades. The blades turn a shaft. The shaft drives a generator, either directly or through a gearbox that raises the speed. The generator converts the mechanical rotation into electricity.

The steps run in order:

1. Wind strikes the blades. Each blade is an airfoil, so lift pulls it sideways and drag pushes it downwind. The lift part turns the rotor.
2. The rotor turns the main shaft at low speed, often 10 to 20 revolutions per minute (typical value for a large turbine).
3. A gearbox or a multipole generator raises the speed to the level the generator needs.
4. The generator makes alternating current. Power electronics convert it to the frequency and voltage of the grid.
5. A controller adjusts the blade pitch and the yaw angle. It keeps the rotor facing the wind and limits the power in strong gusts.

The air cannot stop completely behind the rotor. If it did, it would block the flow and the rotor would extract no power. The limit on how much power a rotor can take from the wind is the **Betz limit**, derived below.

### Main parts

- **Blades.** Usually three, made from fibreglass or carbon-fibre composite. Blade length sets the swept area.
- **Hub and pitch system.** The hub holds the blades. Pitch motors turn each blade about its long axis to change its angle to the wind.
- **Nacelle.** The housing on top of the tower. It holds the shaft, gearbox, generator, converter, and controls.
- **Gearbox.** Steps up the rotor speed for a conventional generator. Direct-drive machines use a large, slow generator and no gearbox.
- **Generator.** A permanent-magnet or electrically excited synchronous machine, or an induction machine.
- **Yaw system.** Motors that turn the nacelle to face the wind.
- **Tower and foundation.** Steel tubes, usually 60 to 120 m tall for utility machines, on a reinforced concrete foundation. Height matters because wind speed rises with height.

### Variants

- **Horizontal-axis turbines.** The rotor spins about a horizontal shaft. Nearly all utility turbines use this design, usually with three blades and the rotor facing upwind.
- **Vertical-axis turbines.** The rotor spins about a vertical shaft. The Darrieus type uses curved airfoil blades, and the Savonius type uses cups. They work in turbulent wind near buildings, but they have lower efficiency in open sites.
- **Onshore and offshore.** Offshore turbines sit on steady, strong winds at sea. They are larger, and their foundations cost more.
- **Geared and direct-drive.** Geared machines use a smaller generator at higher speed. Direct-drive machines avoid the gearbox, which fails often, but their generators are heavier.

## Key equations

Kinetic power in the wind, in watts, for air with cross-sectional area $A$ in square metres (m$^2$) moving at speed $v$ in metres per second (m/s):

$$P_{\mathrm{wind}} = \frac{1}{2} \rho A v^3$$

where $\rho$ is the air density in kilograms per cubic metre (kg/m$^3$). At sea level on Earth and 15 °C, $\rho \approx 1.225\ \text{kg}/\text{m}^3$ (standard value). The **swept area** of a rotor of diameter $D$ in metres is $A = \pi D^2 / 4$.

Turbine output, in watts, with power coefficient $C_p$:

$$P_{\mathrm{turbine}} = \frac{1}{2} \rho A v^3 \, C_p$$

where $C_p$ is the fraction of the wind power the rotor extracts (dimensionless).

Betz limit, the largest possible power coefficient for an ideal actuator disk:

$$C_{p,\mathrm{max}} = \frac{16}{27} \approx 0.593$$

**Tip speed ratio**, a dimensionless measure of rotor speed:

$$\lambda = \frac{\omega R}{v}$$

where $\omega$ is the rotor angular speed in radians per second (rad/s) and $R$ is the rotor radius in metres (m). Modern turbines run at $\lambda$ of about 6 to 9 (typical value).

**Capacity factor**, a dimensionless ratio of actual energy to the energy at full rated power for a year:

$$\mathrm{CF} = \frac{E}{P_{\mathrm{rated}} \times 8760\ \text{h}}$$

where $E$ is the annual energy in watt-hours (Wh) or kilowatt-hours (kWh), $P_{\mathrm{rated}}$ is the rated power in the same unit scale, and 8760 is the number of hours in a year.

Derivation of the Betz limit. Let $a$ be the **axial induction factor** (dimensionless), the fractional slowdown of the air at the rotor. The air at the rotor moves at $v(1-a)$, and the wake far behind moves at $v(1-2a)$. The power extracted is $P = 2\rho A v^3 a (1-a)^2$. Setting $dP/da = 0$ gives $a = 1/3$. Then $P = \frac{8}{27} \rho A v^3$, and $C_p = P / (\frac{1}{2} \rho A v^3) = \frac{16}{27}$.

## Worked example

**Given:** A turbine with rotor diameter $D = 80\ \text{m}$. The wind speed is $v = 10\ \text{m/s}$ at hub height. Air density is $\rho = 1.225\ \text{kg}/\text{m}^3$ (standard value). A second turbine has rated power $P_{\mathrm{rated}} = 3\ \text{MW}$ and produces $E = 7\ \text{GWh}$ in a year.

**Find:** (a) the power in the wind through the rotor, (b) the largest power any rotor could extract at this speed, and (c) the capacity factor of the second turbine.

**Assumptions:** The wind speed is steady and uniform across the rotor. The air density is the standard value.

**Solution:**

1. Swept area: $A = \pi (80)^2 / 4 = 5027\ \text{m}^2$.
2. Wind power: $P_{\mathrm{wind}} = \frac{1}{2} (1.225)(5027)(10)^3 = 3.08 \times 10^6\ \text{W}$, which is $3.08\ \text{MW}$.
3. Betz maximum: $P_{\mathrm{max}} = \frac{16}{27} \times 3.08\ \text{MW} = 1.82\ \text{MW}$.
4. Capacity factor: $\mathrm{CF} = \frac{7 \times 10^6\ \text{kWh}}{3000\ \text{kW} \times 8760\ \text{h}} = 0.266$.

**Answer:** (a) $3.08\ \text{MW}$ in the wind. (b) At most $1.82\ \text{MW}$ can be extracted. (c) $\mathrm{CF} = 0.266$, or 26.6 percent.

**Sanity check:** The Betz maximum is less than the wind power, as expected. A capacity factor of 0.266 means the turbine averages about a quarter of its rated output over the year. That is typical for onshore wind (typical range 0.25 to 0.45). Doubling the wind speed would raise the wind power by $2^3 = 8$ times, which shows why siting matters so much.

## Design trade-offs

- **Rotor size and tower height.** A larger rotor sweeps more area and captures more energy. It also needs a taller tower to clear ground turbulence, and it carries heavier loads at the root of each blade.
- **Rated speed and cut-in.** A turbine starts to produce power at a cut-in speed of about 3 to 4 m/s (typical value). It reaches rated power at about 11 to 13 m/s (typical value), and it shuts down at a cut-out speed near 25 m/s (typical value) to protect the structure.
- **Tip speed and noise.** Faster tips raise the efficiency but also the noise. Designers balance tip speed against the noise limits near homes.
- **Cost per kilowatt-hour.** Taller towers and larger rotors cost more to build. They lower the cost per kilowatt-hour only if the wind is strong enough to use them.
- **Gearbox or direct drive.** A gearbox is light and cheap to build, but it wears out and needs maintenance. A direct-drive generator is heavy and expensive, but it has fewer moving parts.
- **Wildlife and land use.** Turbines can harm birds and bats, and they affect land use. Sites and curtailment rules reduce these effects.

## How it fails

- **Blade fatigue.** Each blade bends about once per revolution, and gusts add stress cycles. Fatigue cracks grow at the root and at bond lines. Inspection and blade load limits prevent most failures.
- **Gearbox bearing failure.** Gearboxes often fail at the bearings or gear teeth. Warning signs include rising vibration and debris in the oil. Oil analysis and vibration monitoring detect them early.
- **Lightning.** Blades are struck often. Receptors in the blade tip and a conductor down the blade carry the current to the hub and then to ground.
- **Ice.** Ice on blades unbalances the rotor and throws ice pieces. Ice detectors stop the turbine until the ice clears.
- **Overspeed.** A grid fault or a loss of control can let the rotor spin too fast. Aerodynamic braking by pitching the blades to feather, and a mechanical disc brake, stop the rotor.
- **Tower or foundation failure.** Extreme gusts and corrosion stress the tower base. Engineers design to standards for wind class and extreme loads.

The safety measures that exist because of these failures include blade pitch braking, a mechanical brake that acts when power is lost, lightning protection systems, ice detection, and load-based shutdown in strong wind.

## History

Poul la Cour in Denmark used wind turbines to generate electricity in the 1890s. The Gedser turbine, built in Denmark around 1957 and designed by Johannes Juul, was an early grid-connected machine. Albert Betz published his limit on the power coefficient in 1919 in Germany. Wind energy grew rapidly from the 1980s, led by programs in Denmark, Germany, and the United States. Modern utility turbines use the same basic principles, with larger rotors and better controls.

## Practice

1. A turbine produces power in proportion to $v^3$. Find the ratio of wind power at $12\ \text{m/s}$ to wind power at $6\ \text{m/s}$.
2. A rotor has diameter $50\ \text{m}$. The wind speed is $9\ \text{m/s}$ and the air density is $1.225\ \text{kg}/\text{m}^3$. Find the wind power through the rotor in kilowatts.
3. Using the result from problem 2, find the largest power a rotor could extract at that speed, in kilowatts.
4. A $2\ \text{MW}$ turbine produces $3.5\ \text{GWh}$ in a year. Find its capacity factor.

<details><summary>Answers</summary>

1. $(12/6)^3 = 8$.
2. $P_{\mathrm{wind}} = \frac{1}{2}(1.225)(\pi \cdot 25^2)(9^3) = 877\ \text{kW}$.
3. $P_{\mathrm{max}} = \frac{16}{27} \times 877 = 520\ \text{kW}$.
4. $\mathrm{CF} = \frac{3.5 \times 10^6\ \text{kWh}}{2000\ \text{kW} \times 8760\ \text{h}} = 0.20$.

</details>

## Common mistakes

- Using $v^2$ instead of $v^3$. Power in the wind scales with the cube of the speed, so a $10\ \%$ speed increase adds about $33\ \%$ more power.
- Treating the Betz limit as the actual output. Real rotors reach power coefficients well below $16/27$ after losses from blade drag, tip losses, and generator and converter losses.
- Using the rated power to estimate annual energy. Annual energy depends on the wind speed distribution, so use the capacity factor instead.
- Forgetting the air density. Air is less dense at high altitude and in hot weather, so the same wind gives less power.
- Assuming the rotor can stop the wind. Air must leave the rotor, so only part of its energy can be taken.

## Go deeper

- [How do wind turbines work](https://www.energy.gov/eere/wind/how-do-wind-turbines-work), U.S. Department of Energy: how lift turns the rotor and how the generator makes electricity.
- [Wind energy basics](https://www.energy.gov/eere/wind/wind-energy-basics), U.S. Department of Energy: an overview of the rotor, generator, gearbox, lift, and drag in wind turbines.
- Related lessons: [Solar photovoltaics](01-solar-photovoltaics.md), [Hydroelectric power](03-hydroelectric-power.md), [Energy storage](06-energy-storage.md), [Aircraft and wings](../vehicles-aerospace/05-aircraft-and-wings.md), [Generators and alternators](../electrical/04-generators-and-alternators.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
