# Kitchen appliances

**Type:** lesson

Kitchen appliances turn electrical energy into heat or motion inside a box that people touch every day. Engineers size the heating element, the motor, and the controls so that the appliance is fast, safe, and cheap to run. Four appliances cover most of the physics: the kettle, the toaster, the blender, and the induction cooktop.

**Prerequisites:** [Thermal systems](../thermal-fluid/01-thermal-systems.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Circuit basics](../electronics/01-circuit-basics.md), [DC motors](../electrical/01-dc-motors.md)
**Time:** 4-6 h

## Core ideas

### How it works

A resistive heater turns electrical power into heat. A current $I$ through a resistance $R$ dissipates power $P = I^2 R$, and every joule of that power appears as heat in the element. The kettle and the toaster both work this way. The heat then moves into the water or the bread by conduction and convection.

A kettle heats 1 L of water from room temperature to boiling in a few minutes. The element sits in a metal base plate or in the water itself. A thermostat or steam-operated switch turns the element off when the water boils. A bimetallic strip bends with heat and opens the circuit at a set temperature.

A toaster passes current through a nickel-chromium wire until the wire glows and heats the bread on both sides. A spring-loaded carriage holds the bread down. A timer or a bimetallic strip releases a latch when the toast is done, and the spring lifts the carriage. Browning comes from Maillard reactions and caramelization, which need surface temperatures well above the boiling point of water.

A blender uses a universal motor, a series-wound motor that runs on AC or DC. Blade speeds reach tens of metres per second at the tips. The motor spins the blade shaft at tens of thousands of revolutions per minute, typically about 20 000 rpm in a kitchen blender.

An induction cooktop passes high-frequency alternating current, typically tens of kilohertz, through a coil under a glass ceramic top. The changing magnetic field induces eddy currents in the base of a magnetic pan. The pan's electrical resistance turns those currents into heat. The glass stays cool because the heat forms in the pan itself.

### Main parts

- **Kettle:** a sheathed heating element, a thermostat or steam switch, a bimetallic cut-out, a lid with a steam vent, a water-level window, and a base with electrical contacts.
- **Toaster:** nichrome heating elements on both sides of each slot, a spring-loaded carriage, an electromagnet or latch, a timer, a darkness control, and a crumb tray.
- **Blender:** a motor base with a universal motor, a drive coupling, a jar with a blade assembly, a seal under the blade, and a lid interlock switch that stops the motor when the jar is removed.
- **Induction cooktop:** a coil array, an inverter that makes the high-frequency current, temperature sensors, a pan-detection circuit, and a glass ceramic top.

### Variants

Kettles come as corded jugs with the element in the base, as concealed-element kettles, and as stovetop kettles that rely on a flame or a hob. Toasters come as two-slot and four-slot pop-up toasters and as toaster ovens with a convection fan. Blenders come as countertop jars, as immersion (stick) blenders, and as high-speed blenders with larger motors. Induction cooktops come as built-in cooktops with several zones and as portable single-burner units.

## Key equations

Assumptions for every equation below: the supply voltage is steady, the element is purely resistive, water is a liquid with a constant specific heat between 20 and 100 $^\circ$C, and the efficiency $\eta$ lumps together all heat that does not reach the water.

- Electrical power: $P = V I$, in watts (W), where $V$ is voltage in volts (V) and $I$ is current in amperes (A).
- Resistive power: $P = V^2 / R$, with $R$ the element resistance in ohms ($\Omega$).
- Heat to raise water: $Q = m c \, \Delta T$, where $Q$ is energy in joules (J), $m$ is mass in kilograms (kg), $c = 4186\ \text{J/(kg K)}$ is the specific heat of liquid water (typical value), and $\Delta T$ is the temperature rise in kelvin (K).
- Latent heat of vaporization: $Q = m L_v$, where $L_v \approx 2.26\ \text{MJ/kg}$ is the heat needed to turn water at 100 $^\circ$C into steam (typical value).
- Time to heat: $t = Q / (P \eta)$, where $\eta$ is the fraction of the appliance's power that reaches the water. This is dimensionless.

## Worked example

**Given:** A kettle holds 1.0 kg of water at 20 $^\circ$C. The water boils at 100 $^\circ$C at sea level. The kettle is rated at $P = 2200\ \text{W}$, and its efficiency is $\eta = 0.85$.

**Find:** (a) the heat that the water needs, (b) the electrical energy the kettle draws, and (c) the time to boil.

**Solution:**

1. Heat for the water: $Q = m c \, \Delta T = 1.0 \times 4186 \times 80 = 334\,880\ \text{J}$, which is $335\ \text{kJ}$ or $0.093\ \text{kWh}$.
2. Electrical energy drawn: $E = Q / \eta = 334\,880 / 0.85 = 394\,000\ \text{J}$, which is $394\ \text{kJ}$ or $0.109\ \text{kWh}$.
3. Time to boil: $t = Q / (P \eta) = 334\,880 / (2200 \times 0.85) = 179\ \text{s}$.

**Answer:** (a) $335\ \text{kJ}$. (b) $394\ \text{kJ}$. (c) $179\ \text{s}$, about 3.0 min.

A kettle rated at $1500\ \text{W}$ with $\eta = 0.80$ takes $279\ \text{s}$, about 4.7 min, for the same water. The power rating sets the time, and the efficiency sets how much of the power reaches the water.

**Sanity check:** The energy drawn is larger than the heat delivered, as efficiency demands. The time of 179 s is consistent with the energy divided by the power: $394\,000 / 2200 = 179\ \text{s}$. Boiling a litre in about three minutes at 2.2 kW is a plausible figure for a kettle. Some water also turns to steam. Evaporating 5 percent of the mass would take about $0.05 \times 2.26\ \text{MJ/kg} = 113\ \text{kJ}$ more, which is a real but smaller share of the total.

## Design trade-offs

- **Power and the electrical circuit.** A 120 V circuit on a 15 A breaker supplies at most $120 \times 15 = 1800\ \text{W}$. A 1500 W kettle draws $1500 / 120 = 12.5\ \text{A}$ and leaves little room for other loads. In many countries, a 230 V supply lets a kettle draw 2 to 3 kW.
- **Element design.** A sheathed element tolerates water and resists scale, but a dry boil can overheat the sheath. Designers balance element watt density against life.
- **Safety cut-outs.** A steam switch or bimetallic cut-out stops the kettle when the water boils. A dry-boil cut-out adds a second safety layer, and it costs more.
- **Blender speed and noise.** Higher blade speed cuts food faster but makes more noise and needs a larger motor. A universal motor is small and fast, but its brushes wear.
- **Induction efficiency.** Induction heats the pan directly and reaches efficiencies near 85 to 90 percent (typical values). It needs magnetic cookware, and it costs more to build than a resistance cooktop.
- **Life.** Nichrome oxidizes over thousands of heat cycles. Blender seals and bearings wear, and the blade must stay sharp and balanced.

## How it fails

- **Scale on a kettle element.** Limescale insulates the element. The element runs hotter and the sheath can fail. Warning signs are slow boiling and a white crust on the element.
- **Dry boil.** A kettle with no water can overheat. The steam switch and the dry-boil cut-out exist to stop this.
- **Water in electrical parts.** A cracked base or a wet contact can cause a shock or a short. Insulation, double insulation, and ground-fault protection reduce that risk.
- **Toaster jam.** Crumbs and a stuck carriage can keep the latch from releasing. A fire can start when crumbs touch the element. Crumb trays and thermal fuses reduce that risk.
- **Blender seal and lid failure.** A worn seal leaks, and a bypassed lid interlock lets the blades run with the lid open. Interlock switches and motor thermal protectors exist for these failures.
- **Induction faults.** An unmagnetic pan does not heat. A cracked glass top can fail from impact or thermal shock. The control electronics need cooling, so a blocked vent leads to a shutdown.

## Safety and the hierarchy of controls

Kitchen appliances carry electrical, thermal, and mechanical hazards. Designers and users apply these controls in order, starting with the most effective.

- **Elimination.** Remove the hazard entirely. A cordless kettle with a sealed base removes the risk of a cord pulled into water. A blender cannot drop its blades, because cutting is its purpose, so the blender relies on the lower controls.
- **Substitution.** Replace a hazard with a lower one. Induction heating removes the open flame of a gas burner and the hot glowing coil of a resistance cooktop. The surface stays cooler where no pan sits.
- **Engineering controls.** Build the protection into the appliance. Examples are the steam switch and dry-boil cut-out on a kettle, the thermal fuse in a toaster, the lid interlock on a blender, and the pan-detection circuit on an induction cooktop. Double insulation and a ground connection reduce shock risk.
- **Administrative controls.** Set rules for use and maintenance. The manual says to keep the kettle off the base when empty, to clear crumbs from the toaster tray, and to descale the kettle regularly.
- **Personal protective equipment.** Oven gloves and a splash guard are the last layer. They protect the user only after the layers above have failed.

## History

Charles Strite patented a pop-up toaster in 1919, and the Waters Genter Company built the first commercial version. Earlier toasters held bread against a wire grid by hand. The spring-loaded carriage and the timed release made toast without supervision.

Induction heating was used in industry before it reached home kitchens. Furnaces used induction to melt and harden metal in the early twentieth century. Home induction cooktops came later, after cheap power electronics made the high-frequency supply small enough.

Fred Waring's company introduced the Waring Blendor in 1937. The high-speed blender became a kitchen tool after that.

## Practice

1. A 1500 W kettle runs for 2.0 min. Find the energy it uses in kilojoules.
2. The same kettle runs on a 120 V supply. Find the current and the element resistance.
3. A 0.5 kg batch of water heats from 20 $^\circ$C to 100 $^\circ$C in a 2200 W kettle with $\eta = 0.85$. Find the time to boil.
4. A 1000 W toaster runs for 2.5 min. Find the energy in kilojoules and in kilowatt-hours.

<details><summary>Answers</summary>

1. $E = P t = 1500 \times 120 = 180\ \text{kJ}$.
2. $I = P / V = 1500 / 120 = 12.5\ \text{A}$, and $R = V^2 / P = 120^2 / 1500 = 9.6\ \Omega$.
3. $Q = 0.5 \times 4186 \times 80 = 167\,440\ \text{J}$, and $t = Q / (P \eta) = 167\,440 / (2200 \times 0.85) = 90\ \text{s}$.
4. $E = 1000 \times 150 = 150\ \text{kJ}$, which is $0.042\ \text{kWh}$.

</details>

## Common mistakes

- Treating a rated power as the energy delivered to the food. Efficiency removes a share of it.
- Sizing a circuit to its full rated current for a long-running load. Continuous loads need a margin in most codes.
- Using a non-magnetic pan on an induction cooktop, then concluding the cooktop is broken.
- Reading watts as energy. A watt is a joule per second, so the energy depends on the time.
- Assuming the steam switch measures the water temperature. It senses the steam, so the switch trips near the boiling point.

## Go deeper

- [OpenStax University Physics Volume 2, Chapter 3](https://openstax.org/books/university-physics-volume-2/pages/3-introduction): free textbook on heat, specific heat, and energy transfer.

Related lessons and reference sheets in this repo:

- [Thermal systems](../thermal-fluid/01-thermal-systems.md) for heat, temperature, and energy balances.
- [Heat transfer](../../physics/12-heat-transfer.md) for conduction, convection, and radiation from the heater to the food.
- [Reference: thermofluids](../../physics/reference-thermofluids.md) for the heat and fluid equations used here.
- [DC motors](../electrical/01-dc-motors.md) for the torque and speed of the blender's motor.
- [Digital logic and computers](../electronics/07-digital-logic-and-computers.md) for the timers and controllers in modern appliances.
