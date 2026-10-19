# Heat pumps

**Type:** lesson

A heat pump is a machine that moves heat from a cold source, such as outdoor air or the ground, into a warm building. Engineers use heat pumps because one delivers more heat than the electricity it consumes, so it heats a building with less energy than a resistance heater.

It uses the same refrigeration cycle as an air conditioner, run in the other direction.

**Prerequisites:** [Refrigeration and air conditioning](03-refrigeration-and-air-conditioning.md), [Thermodynamics: entropy, the second law, and cycles](../../physics/09-thermo-second-law-cycles.md), [Thermal systems](01-thermal-systems.md)
**Time:** 6-8 h

## Core ideas

### How it works

A heat pump is a refrigerator whose useful output is the hot side. The refrigerant absorbs heat from the
cold source in an evaporator, a compressor raises its pressure and temperature, and a condenser releases
that heat into the building. An expansion valve then drops the pressure, and the cycle repeats.

The heat delivered to the building is the heat taken from the source plus the compressor work. Work
adds energy, so the delivered heat is larger than the work used.

In cooling mode, a reversing valve swaps the roles of the two coils. The indoor coil becomes the
evaporator and the outdoor coil becomes the condenser. Many heat pumps can cool a house in summer and heat
it in winter for this reason.

### Air-source and ground-source

An air-source heat pump takes heat from outdoor air. It is cheap to install and common in mild climates.
Its COP falls as the outdoor air gets colder, because the evaporator must boil the refrigerant at a
lower temperature and the compressor has to lift the refrigerant through a larger pressure gap.

A ground-source (geothermal) heat pump takes heat from a loop of buried pipe carrying water or antifreeze
solution. Below a few metres, ground temperature stays close to the annual average air temperature for
the site. The loop works at a steadier temperature than outside air, so the COP changes less through the
winter. The cost is in drilling or trenching the loop.

### Coefficient of performance and outdoor temperature

Heating COP is the heat delivered per unit of work. Typical air-source units have a rated COP near 3 at
mild conditions, and it falls to about 2 or 2.5 near freezing. Ground-source units often rate near 3.5 to
4.5 (typical manufacturer values under standard rating conditions).

The ideal limit depends on the temperatures alone. As the outdoor air gets colder, the Carnot limit drops
steadily. The real COP follows the same trend, below that limit.

### Defrost

When outdoor air is near or below freezing and humid, moisture freezes on the outdoor coil. The frost
blocks airflow and cuts heat transfer. A typical air-source unit senses this and reverses briefly to
cycle hot refrigerant through the outdoor coil. The indoor fan usually pauses, and the building cools a
little during the cycle. Defrost wastes some energy, so its frequency is a real cost in cold, wet
weather. A ground-source unit has no outdoor coil to frost.

### Balance point

A heat pump's heating capacity falls as the outdoor temperature drops, while the building's heat loss rises.
The outdoor temperature where the two meet is the balance point. Below it, the heat pump cannot keep up
alone, and a backup electric heater or a fossil-fuel furnace makes up the difference. Designers size the
heat pump for a design temperature, and the balance point depends on that choice.

## Key equations

- Heating COP: $\mathrm{COP}_{\mathrm{HP}} = \dfrac{\dot{Q}_H}{\dot{W}_c}$, where $\dot{Q}_H$ is the heat delivered to
  the building in watts (W) and $\dot{W}_c$ is the electrical input in watts (W).
- Relation to cooling COP: $\mathrm{COP}_{\mathrm{HP}} = \mathrm{COP}_R + 1$ for the same cycle, where $\mathrm{COP}_R$ is
  the cooling COP.
- Carnot heating limit: $\mathrm{COP}_{\mathrm{HP},\mathrm{max}} = \dfrac{T_H}{T_H - T_L}$, where $T_H$ is the building
  temperature and $T_L$ the source temperature, both in kelvin (K).
- Electrical input: $\dot{W}_c = \dot{Q}_H / \mathrm{COP}_{\mathrm{HP}}$.
- Electric resistance heater: $\dot{W} = \dot{Q}_H$, so its COP is 1.
- Seasonal performance factor (SPF): the total heat delivered over a season divided by the total electrical
  energy used. It is the honest figure for a whole winter, because COP changes with temperature.

## Worked example

**Given:** A house loses heat at $\dot{Q}_H = 8.0\ \text{kW}$ on a design day when the outdoor air is at
$-5\ \text{C}$. The indoor setpoint is $20\ \text{C}$. The air-source heat pump has a measured COP of 2.5 at
these conditions.

**Find:** (a) the electrical power the heat pump draws, (b) the Carnot heating limit at these
temperatures, and (c) the electrical power a resistance heater would need, and the saving.

**Assumptions:** Steady conditions on the design day. The COP is the measured value at $-5\ \text{C}$. The
building loses the heat through its envelope, and the heat pump delivers the whole load.

**Solution:**

1. Convert temperatures to kelvin: $T_H = 20 + 273.15 = 293.15\ \text{K}$, and $T_L = -5 + 273.15 =$
   $268.15\ \text{K}$.
2. Electrical power: $\dot{W}_c = 8.0 / 2.5 = 3.2\ \text{kW}$.
3. Carnot limit: $\mathrm{COP}_{\mathrm{max}} = 293.15 / (293.15 - 268.15) = 11.7$.
4. Fraction of Carnot reached: $2.5 / 11.7 = 0.21$.
5. Resistance heater power: $\dot{W} = 8.0\ \text{kW}$, since its COP is 1.
6. Saving: $8.0 - 3.2 = 4.8\ \text{kW}$, which is $4.8 / 8.0 = 60$ percent of the resistance heater's input.

**Answer:** (a) $\dot{W}_c = 3.2\ \text{kW}$. (b) The Carnot limit is 11.7. (c) A resistance heater would
draw 8.0 kW, so the heat pump saves 4.8 kW, or 60 percent of the input, on that day.

**Sanity check:** The COP of 2.5 is below the Carnot limit of 11.7, as the second law requires. A fraction
of 0.21 is low, which reflects the large temperature lift and the frost and defrost losses on a cold day.
The heat pump draws less power than the load, because it delivers more heat than it consumes.

## Design trade-offs

Designers balance cost, efficiency, noise, and climate. A larger outdoor coil lowers the condensing
temperature and raises COP, but it costs more and needs room. Variable-speed compressors match output to
the load, which keeps COP high at part load.

A higher supply water temperature suits radiators poorly and reduces COP. Under-floor heating works at
lower temperatures, so the heat pump runs more efficiently. Retrofits to existing radiator systems often
need larger radiators or higher flow temperatures.

Ground-source systems cost more to install, because of drilling or trenching, but they have higher seasonal
COP and no outdoor fan or coil to frost. Air-source systems are cheap and simple, but their seasonal
performance depends on the local climate.

Noise comes mainly from the outdoor fan and compressor. Units are placed away from bedrooms, and the outdoor
fan is often a large, slow-turning type to reduce noise.

## How it fails

- Refrigerant leak. The system loses capacity and COP falls. Leaks are checked by pressure tests, and the
  system is refilled only after repair.
- Frost buildup. The outdoor coil frosts faster than the defrost cycle clears it, which cuts heat transfer
  and can trip the low-pressure switch.
- Fan or coil fouling. Leaves, dust, and snow block airflow, which raises condensing pressure or lowers
  evaporating pressure.
- Compressor overheating from low airflow or overcharge.
- Ground loop problems. A leak in the loop or a loop that is too short cools the ground over years. The
  COP drops slowly as the ground loses heat.

Safety measures exist because of these faults. High- and low-pressure switches stop the compressor outside
safe pressures. Defrost controls prevent frost from blocking airflow. A pressure relief valve protects
the refrigerant circuit. Ground loops are tested for leaks before they are filled, and the fluid used is
usually a non-toxic antifreeze solution.

## History

Lord Kelvin, then William Thomson, described the heat pump principle in 1852, and he proposed that
heat from cold sources could warm buildings. Jacob Perkins's 1834 vapor-compression machine in London
supplied the cycle that heat pumps still use. Sadi Carnot's 1824 limit on heat engine efficiency also sets the upper bound on heat pump COP.

## Practice

1. A heat pump is run as a refrigerator and has $\mathrm{COP}_R = 3.2$. Find its heating COP, assuming
   the same cycle.
2. A building needs $\dot{Q}_H = 6.0\ \text{kW}$ of heat from a heat pump with COP 3.0. Find the
   electrical power drawn.
3. Find the Carnot heating limit for a building at $20\ \text{C}$ with an outdoor temperature of
   $-10\ \text{C}$.
4. A ground-source heat pump has COP 4.0 and must deliver $12\ \text{kW}$. Find its electrical input.

<details><summary>Answers</summary>

1. $\mathrm{COP}_{\mathrm{HP}} = 3.2 + 1 = 4.2$
2. $\dot{W}_c = 6.0 / 3.0 = 2.0\ \text{kW}$
3. $\mathrm{COP}_{\mathrm{max}} = 293.15 / (293.15 - 263.15) = 9.8$
4. $\dot{W}_c = 12 / 4.0 = 3.0\ \text{kW}$

</details>

## Common mistakes

- Using the cooling COP directly as the heating COP. The heating COP is one higher for the same cycle.
- Using degrees Celsius in the Carnot formula. Both temperatures must be in kelvin.
- Quoting a single COP for a whole winter. COP changes with outdoor temperature, so use a seasonal figure
  for energy use.
- Sizing the heat pump only for average temperatures. The design day sets the capacity, and the balance
  point sets when backup heat runs.
- Assuming a heat pump is always more efficient than a furnace. Its advantage depends on the COP at the
  local temperatures.

## Go deeper

- [University Physics Volume 2, Chapter 4 (second law of thermodynamics)](https://openstax.org/books/university-physics-volume-2/pages/4-introduction)
  by OpenStax: heat engines and refrigerators, and the limits on their performance.
- Next: [Heat exchangers](05-heat-exchangers.md), for the coils that move heat between refrigerant and air or
  water.
- Related: [Refrigeration and air conditioning](03-refrigeration-and-air-conditioning.md) for the cycle, and
  [Thermal systems](01-thermal-systems.md) for the conduction and convection losses a heat pump must cover.
- [Applications reference](../reference.md): the lookup sheet for this topic.
