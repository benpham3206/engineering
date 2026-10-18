# Refrigeration and air conditioning

**Type:** lesson

A refrigerator and an air conditioner move heat from a cold space to a warm one. They do this with a
refrigerant that boils at low pressure, absorbs heat, is squeezed to high pressure, and releases heat.
Engineers use the same vapor-compression cycle in kitchens, offices, cars, and cold stores, so it is
worth understanding once.

**Prerequisites:** [Thermodynamics I](../../physics/08-thermo-first-law.md),
[Thermodynamics II](../../physics/09-thermo-second-law-cycles.md),
[Thermal systems](01-thermal-systems.md), [Mathematics folder](../../math/README.md)
**Time:** 8-10 h

## Core ideas

### How it works

Heat does not flow uphill on its own. A refrigerator needs work to move heat from cold to hot. The
vapor-compression cycle does this in four steps.

1. The evaporator sits inside the cold space. Liquid refrigerant at low pressure boils there and absorbs
   heat from the air or food around it.
2. The compressor draws in the vapor and raises its pressure and temperature. This step takes electrical
   work.
3. The condenser sits outside, or at the back of the unit. The hot vapor gives its heat to the room air
   and condenses back into liquid.
4. The expansion device, a capillary tube or an expansion valve, drops the pressure of the liquid. Part of
   it flashes into vapor, and the mixture cools to the evaporator temperature. The cycle then repeats.

The cycle moves more heat than the compressor power alone. The compressor adds work, and the total heat
rejected at the condenser equals the heat absorbed in the evaporator plus that work.

### Main parts

- The compressor, usually hermetic (sealed in a steel shell with its motor), is the only moving part that
  adds energy. Its power sets how fast heat can be moved.
- The evaporator is a coil with a large surface area. Its job is to let the refrigerant boil at a low
  temperature while it absorbs heat.
- The condenser is a coil that rejects heat to a larger, cooler body of air. A fan usually moves that air.
- The expansion device controls the flow of refrigerant from high pressure to low pressure. It also keeps
  the evaporator fed.
- The refrigerant is the working fluid. It must boil and condense at useful pressures and temperatures in
  the working range.
- The thermostat or controller starts and stops the compressor to hold the cold space at a set
  temperature.

### Refrigerants

The refrigerant sets the pressures, the safety rules, and the environmental effect of the system.

- R-12 was a chlorofluorocarbon (CFC) used in household refrigerators for decades. Its chlorine destroys
  stratospheric ozone, and the Montreal Protocol of 1987 phased it out.
- R-22 was a hydrochlorofluorocarbon (HCFC) used in many air conditioners. Its ozone effect is smaller
  than that of CFCs, but it is also being phased out.
- R-134a is a hydrofluorocarbon (HFC) with no ozone effect. It is common in cars and older household
  systems. Its global warming potential is about 1,400 times that of carbon dioxide over 100 years.
- R-600a (isobutane) is a hydrocarbon used in many modern household refrigerators. It has a very small
  warming effect, but it burns, so the charge is kept small.
- R-32 and R-1234yf are newer refrigerants used in many new air conditioners and car systems. Both have
  far lower warming effects than R-134a. R-32 is mildly flammable.

The Kigali Amendment of 2016 to the Montreal Protocol extended controls to HFCs. Equipment makers are
moving to lower-warming refrigerants because of it.

### Coefficient of performance

Refrigeration is judged by its coefficient of performance (COP), the heat moved per unit of work put in.
A COP above 1 is normal. A COP of 3 means the cold space gains 3 J of cooling for each 1 J of electrical
work.

Household refrigerators and room air conditioners usually land between about 2 and 3.5. Their COP is set
by the temperatures, the compressor and heat exchanger design, and the refrigerant.

Air conditioners in some countries are rated in the seasonal energy efficiency ratio (SEER), in Btu of
cooling per watt-hour of electricity over a season. The conversion to a COP is simple, as shown in the
equations below.

## Key equations

- Refrigeration COP: $\mathrm{COP}_R = \dfrac{\dot{Q}_L}{\dot{W}_c}$, where $\dot{Q}_L$ is the heat rate
  removed from the cold space in watts (W) and $\dot{W}_c$ is the compressor power in watts (W).
- Heat pump COP for the same cycle: $\mathrm{COP}_{HP} = \dfrac{\dot{Q}_H}{\dot{W}_c} = \mathrm{COP}_R + 1$,
  where $\dot{Q}_H$ is the heat rate delivered to the warm space in watts (W).
- Energy balance on the cycle: $\dot{Q}_H = \dot{Q}_L + \dot{W}_c$.
- Evaporator heat rate: $\dot{Q}_L = \dot{m}\,(h_1 - h_4)$, where $\dot{m}$ is the refrigerant mass flow in
  kilograms per second (kg/s) and $h$ is specific enthalpy in kilojoules per kilogram (kJ/kg).
- Compressor power: $\dot{W}_c = \dot{m}\,(h_2 - h_1)$, with $h_2$ the enthalpy leaving the compressor.
- Condenser heat rate: $\dot{Q}_H = \dot{m}\,(h_2 - h_3)$, with $h_3$ the enthalpy of liquid leaving the
  condenser.
- Throttling: $h_4 = h_3$. The expansion device keeps enthalpy constant.
- Carnot upper bound: $\mathrm{COP}_{R,max} = \dfrac{T_L}{T_H - T_L}$, with $T_L$ the cold temperature and
  $T_H$ the warm temperature, both in kelvin (K).
- SEER to COP: $\mathrm{COP} = \dfrac{\mathrm{SEER}}{3.412}$, because 1 W = 3.412 Btu/h.

The enthalpy values in the worked example are typical saturated R-134a properties, taken from standard
refrigerant property tables in the IIR reference state, where saturated liquid at 0 C has
$h = 200\ \text{kJ/kg}$. They are rounded to one decimal place. Other refrigerants need their own tables.

## Worked example

**Given:** A small refrigerator runs R-134a at a mass flow of $\dot{m} = 0.010\ \text{kg/s}$. The
evaporator is at $0\ \text{C}$, and the condenser is at $40\ \text{C}$. Leaving the evaporator, the
refrigerant is saturated vapor with $h_1 = 398.6\ \text{kJ/kg}$. Leaving the condenser, it is saturated
liquid with $h_3 = 256.4\ \text{kJ/kg}$. The compressor draws $\dot{W}_c = 0.50\ \text{kW}$. Ignore pressure
drop in the piping.

**Find:** (a) the refrigeration effect $\dot{Q}_L$, (b) the COP, (c) the heat rejected $\dot{Q}_H$, and
(d) the Carnot COP for the same two temperatures, and how the actual COP compares with it.

**Assumptions:** Steady flow. The throttling process is isenthalpic, so $h_4 = h_3$. Temperatures for
the Carnot bound are $T_L = 273.15\ \text{K}$ and $T_H = 313.15\ \text{K}$.

**Solution:**

1. Refrigeration effect per kilogram: $h_1 - h_4 = 398.6 - 256.4 = 142.2\ \text{kJ/kg}$.
2. Evaporator heat rate: $\dot{Q}_L = 0.010 \times 142.2 = 1.422\ \text{kW}$.
3. COP: $\mathrm{COP}_R = 1.422 / 0.50 = 2.84$.
4. Heat rejected: $\dot{Q}_H = \dot{Q}_L + \dot{W}_c = 1.422 + 0.50 = 1.922\ \text{kW}$.
5. Check with the condenser balance. The compressor exit enthalpy is $h_2 = h_1 + \dot{W}_c/\dot{m} =
   398.6 + 50.0 = 448.6\ \text{kJ/kg}$, so $\dot{Q}_H = 0.010 \times (448.6 - 256.4) = 1.922\ \text{kW}$.
6. Carnot COP: $273.15 / (313.15 - 273.15) = 6.83$. The actual COP is $2.84 / 6.83 = 0.42$ of the Carnot
   value.

**Answer:** (a) $\dot{Q}_L = 1.42\ \text{kW}$. (b) $\mathrm{COP}_R = 2.84$. (c) $\dot{Q}_H = 1.92\ \text{kW}$.
(d) The Carnot bound is 6.83, so the real cycle reaches about 42 percent of it.

**Sanity check:** The COP is above 1, as expected for a refrigerator. The heat rejected is larger than the
heat removed by exactly the compressor work, $1.922 - 1.422 = 0.50\ \text{kW}$. The actual COP sits below
the Carnot bound, as the second law requires.

## Design trade-offs

Designers balance efficiency, size, noise, and cost. A larger evaporator and condenser raise COP because
the refrigerant runs closer to the air temperatures, but they cost more and take more space. A
variable-speed compressor matches the cooling load and often improves seasonal efficiency, at a higher
price.

Household refrigerators are sized for a compressor that runs for part of each hour. Their rated power is
often in the low hundreds of watts, and the average draw is much lower. Noise comes mainly from the
compressor and fan. A quiet unit usually has a larger, slower compressor.

Split air conditioners put the noisy compressor outside. Window units hold everything in one box, which
is cheaper to install but louder in the room. Central systems move air through ducts, which adds fan
power and duct losses.

Refrigerant choice is a trade-off too. A refrigerant with a low warming effect may be mildly flammable or
operate at higher pressure. Designers must decide the charge size and the safety measures to match.

## How it fails

- Refrigerant leak. The system loses charge, so the evaporator runs cold and frost appears on the coil,
  while cooling drops. Leaks are the most common fault. A technician finds them with a detector or a
  pressure test.
- Blocked expansion device. Moisture freezes or dirt clogs a capillary tube or valve. The evaporator
  starves, and pressures are wrong.
- Dirty condenser. Dust and lint block airflow, so condensing pressure rises, COP falls, and the
  compressor overheats.
- Compressor failure. Overheating, low oil, liquid slugging (liquid entering the compressor), or an
  electrical fault can burn out the motor.
- Overpressure. A blocked condenser or overcharge raises pressure until the unit trips.

Safety measures exist because of these faults. A high-pressure switch stops the compressor if condensing
pressure gets too high. A low-pressure switch stops it if the suction side collapses from a leak. A
pressure relief valve protects the high side. Crankcase heaters keep liquid out of the compressor oil.
In many countries, only certified technicians may handle refrigerant, because venting it harms the
climate and some refrigerants burn.

## History

Jacob Perkins patented a vapor-compression machine in London in 1834. John Gorrie built an ice-making
machine in Florida around 1851, to cool patients in a hospital. Carl von Linde in Germany developed
practical refrigeration machines in the 1870s and later used them to liquefy air. Thomas Midgley Jr.
developed R-12 in the late 1920s, and it became the standard household refrigerant for decades. Sadi
Carnot's 1824 analysis of ideal heat engines set the limit that still bounds the COP of any cycle.

## Practice

1. A refrigerator removes $\dot{Q}_L = 300\ \text{W}$ from its cold box with a compressor power of
   $\dot{W}_c = 100\ \text{W}$. Find $\mathrm{COP}_R$.
2. A cooler removes $\dot{Q}_L = 1.0\ \text{kW}$ and uses $\dot{W}_c = 0.40\ \text{kW}$. Find $\mathrm{COP}_R$
   and the heat rejected $\dot{Q}_H$.
3. An air conditioner is rated at SEER 14. Find its equivalent COP.
4. A freezer holds $-18\ \text{C}$ and sits in a kitchen at $25\ \text{C}$. Find the Carnot COP.
5. Using the worked-example enthalpies, $h_1 = 398.6\ \text{kJ/kg}$ and $h_4 = 256.4\ \text{kJ/kg}$, find
   $\dot{Q}_L$ for $\dot{m} = 0.020\ \text{kg/s}$.

<details><summary>Answers</summary>

1. $\mathrm{COP}_R = 300 / 100 = 3.0$
2. $\mathrm{COP}_R = 1.0 / 0.40 = 2.5$, and $\dot{Q}_H = 1.0 + 0.40 = 1.4\ \text{kW}$
3. $\mathrm{COP} = 14 / 3.412 = 4.10$
4. $\mathrm{COP}_{R,max} = 255.15 / (298.15 - 255.15) = 5.93$
5. $\dot{Q}_L = 0.020 \times (398.6 - 256.4) = 2.84\ \text{kW}$

</details>

## Common mistakes

- Using degrees Celsius in the Carnot formula. The temperatures must be in kelvin.
- Reading COP as efficiency that cannot pass 100 percent. A refrigerator's COP is normally 2 to 4, and it
  is not capped at 1.
- Forgetting that the condenser releases the compressor work as well as the heat from the cold space.
  The condenser load is always larger than the evaporator load.
- Treating the expansion device as a turbine that makes work. The throttling step adds no work, and its
  enthalpy stays constant.
- Comparing SEER and COP directly. SEER uses Btu per watt-hour over a season, so convert it with the
  factor 3.412 before comparing with a COP.

## Go deeper

- [University Physics Volume 2, Chapter 4 (second law of thermodynamics)](https://openstax.org/books/university-physics-volume-2/pages/4-introduction)
  by OpenStax: heat engines and refrigerators, the second law, and the limits on their performance.
- Next: [Heat pumps](04-heat-pumps.md), which use the same cycle to heat a building.
- Related: [Thermodynamics II](../../physics/09-thermo-second-law-cycles.md) for the second law and COP
  limits, and [Heat exchangers](05-heat-exchangers.md) for the coils in the evaporator and condenser.
