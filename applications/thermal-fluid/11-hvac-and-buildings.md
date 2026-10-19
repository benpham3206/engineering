# Heating, ventilation, and air conditioning

**Type:** lesson

**Heating, ventilation, and air conditioning**, known as HVAC, are the systems that heat, cool, and bring fresh air into a building. An engineer who sizes them must balance heat losses, moisture, and airflow to keep occupants comfortable and safe.

A building needs heat in winter, cooling in summer, and fresh air all year.

**Prerequisites:** [Thermal systems](01-thermal-systems.md), [Thermodynamics: properties, work, heat, and the first law](../../physics/08-thermo-first-law.md), [Heat transfer](../../physics/12-heat-transfer.md)
**Time:** 8-12 h

## Core ideas

### How it works

Heat flows from hot to cold. A building loses heat through its walls, roof, windows, and floor. It gains heat from people, lights, equipment, and sunlight. Ventilation adds a second flow. Outdoor air enters the building, and the system must heat or cool it to indoor conditions.

Engineers size equipment for the peak load, the largest heating or cooling demand the building sees under design conditions. The design conditions are a cold or hot day chosen for the location. The peak load sets the size of the furnace, boiler, or cooling coil.

Air carries the heat. A fan pushes supply air through ducts to each room. Return air flows back to the unit, passes over coils that heat or cool it, and mixes with fresh outdoor air. The fan must overcome the resistance of filters, coils, and ducts, so fan power depends on duct design as much as on the heat load.

Moisture adds a second problem. Air holds water vapor, and the **relative humidity** is the ratio of the vapor pressure to the saturation pressure at the same temperature. When air cools below its dew point, water condenses out. That is why a cooling coil drips, and it is also how an air conditioner removes humidity.

### Main parts

- Heat source: a furnace burns fuel, a boiler heats water, or a heat pump moves heat from outdoor air or ground.
- Heat exchangers and coils: transfer heat between the working fluid and the air.
- Fan or air handler: moves air through the duct system.
- Ducts: sheet metal or flexible channels that carry air to each room.
- Dampers and grilles: adjust the flow to each room or zone.
- Filters: remove dust and pollen. They add pressure drop, so a clogged filter cuts airflow.
- Outdoor air intake and exhaust: bring fresh air in and send stale air out.
- Controls: a thermostat or building controller sets the supply temperature and fan speed.
- Humidifier or dehumidifier: adds or removes water vapor where the climate needs it.

### Variants

- Forced-air systems: a furnace or heat pump heats or cools air, and a fan carries it through ducts. This is the common system in North American homes.
- Hydronic systems: hot or chilled water flows through radiators, baseboards, floor loops, or fan coils. Water carries far more heat per unit volume than air, so the pipes stay small.
- Packaged rooftop units: one outdoor unit holds the fan, coil, and compressor for a commercial space.
- Split and mini-split systems: an outdoor unit connects to one or more indoor units through refrigerant lines. They need no ducts. See [Refrigeration and air conditioning](03-refrigeration-and-air-conditioning.md).
- **Variable air volume (VAV)**: the system varies the airflow to each zone to hold its temperature, instead of supplying a fixed flow.

## Key equations

Conduction through a wall, window, or roof:

$$\dot{Q} = U A \, \Delta T$$

Here $\dot{Q}$ is heat flow in watts (W), $U$ is the overall heat transfer coefficient in W/(m$^2$ K), $A$ is the area in m$^2$, and $\Delta T$ is the temperature difference in kelvin (K). A difference in kelvin equals a difference in degrees Celsius.

**Sensible heat** to warm or cool ventilation air:

$$\dot{Q} = \rho \, \dot{V} \, c_p \, \Delta T$$

Here $\rho$ is air density in kg/m$^3$ (about 1.2 kg/m$^3$ near 20 C at sea level on Earth, typical), $\dot{V}$ is the volume flow of air in m$^3$/s, and $c_p$ is the specific heat of air in J/(kg K) (about 1005 J/(kg K), typical).

**Latent heat** to evaporate or condense water:

$$\dot{Q}_{\text{lat}} = \dot{m}_w \, h_{\mathrm{fg}}$$

Here $\dot{m}_w$ is the mass flow of water vapor in kg/s, and $h_{\mathrm{fg}}$ is the latent heat of vaporization of water in J/kg (about $2.45 \times 10^6$ J/kg near 20 C, typical).

**Humidity ratio**, the mass of water per mass of dry air:

$$W = 0.622 \, \frac{p_v}{P - p_v}$$

Here $W$ is in kg/kg, $p_v$ is the partial pressure of the water vapor in Pa, and $P$ is the total pressure in Pa (about $101\,325$ Pa at sea level on Earth, typical).

Relative humidity:

$$\phi = \frac{p_v}{p_{\mathrm{sat}}(T)}$$

Here $\phi$ is a fraction from 0 to 1, and $p_{\mathrm{sat}}(T)$ is the saturation pressure at temperature $T$. The Tetens form approximates it between about 0 C and 50 C:

$$p_{\mathrm{sat}}(T) \approx 610.78 \exp\!\left(\frac{17.27\,T}{T + 237.3}\right) \ \text{Pa}, \qquad T \text{ in C}$$

Air velocity in a duct:

$$v = \frac{\dot{V}}{A}$$

Here $v$ is the mean air velocity in m/s, and $A$ is the duct cross-section in m$^2$.

## Worked example

**Given:** A winter room of 20 m$^2$ (4 m by 5 m, 2.5 m ceiling). Indoor design temperature is 21 C, and outdoor design temperature is -5 C, so $\Delta T = 26$ K. The exterior wall is 12 m$^2$ with $U = 0.35$ W/(m$^2$ K). The window is 4 m$^2$ with $U = 2.8$ W/(m$^2$ K). Outdoor ventilation air is 30 L/s, or $\dot{V} = 0.030$ m$^3$/s. Air density is 1.2 kg/m$^3$ (sea level on Earth), and $c_p = 1005$ J/(kg K).

**Find:** The peak heating load.

**Assumptions:** Steady state. The roof and floor are neglected, so the total is a lower bound for this room. No internal gains from people or equipment, and no solar gain. The ventilation air leaves at indoor temperature, so the whole outdoor flow is heated by $\Delta T$.

**Solution:**

1. Wall conduction: $\dot{Q}_w = 0.35 \times 12 \times 26 = 109$ W.
2. Window conduction: $\dot{Q}_g = 2.8 \times 4 \times 26 = 291$ W.
3. Ventilation: $\dot{Q}_v = 1.2 \times 0.030 \times 1005 \times 26 = 941$ W.
4. Total: $109 + 291 + 941 = 1341$ W.

**Answer:** The peak heating load is about 1.34 kW.

**Sanity check:** Divided by the floor area, 1341 W over 20 m$^2$ gives 67 W/m$^2$. That is a plausible load for a room in a cold climate. The ventilation term makes up 70 percent of the total. A better window would cut only the 291 W term, so heat recovery on the ventilation air would save more energy than a window upgrade in this room.

## Design trade-offs

- Ventilation and energy: more outdoor air improves indoor air quality and raises the load. ASHRAE Standard 62.1 sets minimum outdoor air rates for many building types in the United States.
- Duct size and noise: larger ducts carry the same air at lower velocity. That cuts fan power and noise, but it takes ceiling and wall space.
- Oversizing: a unit larger than the peak load turns on and off often. It removes less moisture, because the coil runs for short periods, and its efficiency drops.
- Duct location: ducts in an attic or crawl space lose heat through their walls. Running ducts inside the conditioned space avoids most of that loss.
- Water or air: water carries about 3500 times as much heat per unit volume as air does at the same temperature change. Hydronic systems use small pipes, and forced-air systems need large ducts.
- Equipment cost and running cost: a higher-efficiency heat pump or furnace costs more to buy. The payback depends on the fuel price and the hours of use.

## How it fails

- Undersized equipment: rooms stay cold on the design day. The usual cause is a load calculation that leaves out ventilation or air leakage. The warning sign is a system that runs at full output all day and still falls short.
- Oversized equipment: short cycling. The unit switches on and off every few minutes, humidity stays high, and wear rises. The warning sign is frequent starts.
- Frozen evaporator coil: a blocked filter, closed dampers, or low refrigerant charge cuts the airflow over the coil, and the coil drops below 0 C. The warning sign is ice on the coil and weak airflow. Airflow sensors and freeze protection stop the compressor before the damage builds.
- Legionella: warm water in cooling towers and humidifiers can carry the bacteria that cause Legionnaires' disease. A 1976 outbreak in Philadelphia was linked to a building's cooling system. Water treatment and regular cleaning reduce the risk.
- Poor ventilation: carbon dioxide and humidity build up. High humidity encourages mold. The safeguard is a minimum outdoor air rate and humidity control.
- Duct leakage: unsealed joints pull air from attics and crawl spaces and leave rooms far from the unit underheated. The warning signs are dust in the house and uneven room temperatures.

> [!WARNING]
> Carbon monoxide: a cracked heat exchanger or a blocked flue sends combustion gas into the building. Safety measures include a flue that holds draft, a sealed combustion chamber in modern furnaces, carbon monoxide alarms, and yearly inspection.

## History

Roman baths used hypocausts, which warmed floors and walls with hot air from a furnace below. In 1902, Willis Carrier designed a system for a printing plant in Brooklyn, New York, that controlled humidity so that paper and ink stayed aligned. Carrier published his rational psychrometric formulae in 1911, and those formulas became the basis for modern moisture calculations. Heating and cooling loads are still calculated from the same kinds of terms used in the worked example.

## Practice

1. A wall of area 10 m$^2$ has $U = 0.50$ W/(m$^2$ K). Indoor air is 20 C, and outdoor air is 0 C. Find the heat flow through the wall in watts.
2. A rectangular duct is 0.30 m by 0.20 m, and it carries 0.20 m$^3$/s of air. Find the air velocity in m/s.
3. Outdoor air at 0 C is heated to 10 C at a flow of 0.050 m$^3$/s. Use $\rho = 1.2$ kg/m$^3$ and $c_p = 1005$ J/(kg K). Find the heating power in watts.
4. Air at 20 C and 50 percent relative humidity is at sea-level pressure, 101 325 Pa. Use $p_{\mathrm{sat}}(20\ \text{C}) \approx 2338$ Pa. Find the humidity ratio in kg/kg.

<details><summary>Answers</summary>

1. $\dot{Q} = 0.50 \times 10 \times 20 = 100$ W.
2. $A = 0.30 \times 0.20 = 0.060$ m$^2$, so $v = 0.20 / 0.060 = 3.3$ m/s.
3. $\dot{Q} = 1.2 \times 0.050 \times 1005 \times 10 = 603$ W.
4. The vapor pressure is $p_v = 0.50 \times 2338 = 1169$ Pa. Then $W = 0.622 \times 1169 / (101\,325 - 1169) = 0.00726$ kg/kg, or 7.3 g of water per kg of dry air.

</details>

## Common mistakes

- Sizing equipment from floor area alone. Two rooms of the same area can need very different loads, because their windows, walls, and ventilation rates differ.
- Leaving ventilation out of the load. In the worked example, ventilation is 70 percent of the total.
- Confusing relative humidity with humidity ratio. Relative humidity changes with temperature even when the water content stays the same. The humidity ratio does not change with temperature until water condenses or evaporates.
- Ignoring duct losses. Ducts in an attic or crawl space can lose a large share of the heat the equipment produces.
- Oversizing to be safe. A unit that is too large cycles on and off, and it fails to remove humidity.

## Go deeper

- [*University Physics Volume 1*, Chapter 14](https://openstax.org/books/university-physics-volume-1/pages/14-introduction) by OpenStax: fluids, pressure, Bernoulli's equation, and viscosity. These underlie air flow in ducts.
- [NIST Chemistry WebBook, fluid properties](https://webbook.nist.gov/chemistry/fluid/): thermophysical property data for water and other fluids, useful for checking values in psychrometric and hydronic calculations.
- Related lessons: [Thermal systems](01-thermal-systems.md), [Refrigeration and air conditioning](03-refrigeration-and-air-conditioning.md), [Heat pumps](04-heat-pumps.md), [Heat exchangers](05-heat-exchangers.md), [Compressors and fans](10-compressors-and-fans.md), [Piping and valves](12-piping-and-valves.md).
- Related fundamentals: [Heat transfer](../../physics/12-heat-transfer.md), [Units and dimensional analysis](../../measurement/01-units-and-dimensional-analysis.md), [Safety and risk](../../philosophy/03-safety-and-risk.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
