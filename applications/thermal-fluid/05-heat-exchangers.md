# Heat exchangers

**Type:** lesson

A heat exchanger moves heat from one fluid to another without mixing them. Radiators, car engine coolers,
air conditioner coils, boilers, and chemical plants all depend on one. Engineers size an exchanger by
asking how much heat must move, how hot each stream gets, and how much surface the job needs.

**Prerequisites:** [Thermal systems](01-thermal-systems.md), [Fluid systems](02-fluid-systems.md),
[Heat transfer](../../physics/12-heat-transfer.md), [Mathematics folder](../../math/README.md)
**Time:** 8-12 h

## Core ideas

### How it works

Heat flows from the hot fluid, through a wall, into the cold fluid. Three resistances sit in series along
the path: the hot-side convection, the wall conduction, and the cold-side convection. Fouling deposits add
a fourth. The overall coefficient $U$ combines all of them into one number per unit area.

The temperatures of the two streams change along the exchanger. Heat moves only where one fluid is hotter
than the other, so the temperature difference between the streams sets the rate. That difference shrinks
toward the outlet, which is why sizing needs an average temperature difference instead of one value.

### Flow arrangements

In parallel flow, both fluids enter at the same end and move in the same direction. The outlet temperatures
approach each other, and the cold fluid can never get hotter than the outlet of the hot fluid.

In counterflow, the fluids move in opposite directions. The cold fluid can leave hotter than the hot fluid
leaves, as long as the heat capacities allow it. Counterflow gives the same heat transfer with less area,
so most designs use it.

### Main types

Shell-and-tube exchangers hold a bundle of tubes inside a cylindrical shell. One fluid flows through the
tubes and the other around them, guided by baffles. They handle high pressure and high temperature, and
they are the standard in oil refineries and chemical plants.

Plate heat exchangers stack thin corrugated plates with gaskets. The corrugations create turbulence at low
flow rates, which raises the heat transfer coefficient. They give a high $U$ in a small volume. Gaskets limit
their pressure and temperature, and they are common in food and district heating.

Finned-tube exchangers use fins on the outside of tubes to increase the area on the air side. Air has a low
convection coefficient, so the fins are essential. Air conditioner condensers, car radiators, and home
heating coils are finned-tube units.

A home radiator is a heat exchanger between hot water inside tubes and air outside. Its heat leaves mostly
by natural convection and radiation. The water side has a high coefficient, but the air side limits the
rate, so fins and large surfaces are used.

## Key equations

- Heat rate: $\dot{Q} = U A \Delta T_{lm}$, where $\dot{Q}$ is in watts (W), $U$ is the overall heat transfer
  coefficient in W/(m$^2$ K), $A$ is the heat transfer area in square metres (m$^2$), and $\Delta T_{lm}$ is the
  log mean temperature difference in kelvin (K).
- Log mean temperature difference: $\Delta T_{lm} = \dfrac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$,
  where $\Delta T_1$ and $\Delta T_2$ are the temperature differences between the two fluids at the two ends of
  the exchanger, in kelvin (K).
- Heat capacity rate: $C = \dot{m}\, c_p$, where $\dot{m}$ is the mass flow in kg/s and $c_p$ is the specific
  heat in J/(kg K). The smaller of the two values, $C_{min}$, sets the maximum heat rate.
- Maximum heat rate: $\dot{Q}_{max} = C_{min}\,(T_{h,in} - T_{c,in})$, in watts (W).
- Effectiveness: $\varepsilon = \dot{Q} / \dot{Q}_{max}$, a dimensionless number between 0 and 1.
- Number of transfer units: $NTU = \dfrac{UA}{C_{min}}$, dimensionless.
- Capacity ratio: $C_r = C_{min} / C_{max}$, dimensionless.
- Counterflow effectiveness: $\varepsilon = \dfrac{1 - \exp[-NTU(1 - C_r)]}{1 - C_r \exp[-NTU(1 - C_r)]}$.
- Fouling: $\dfrac{1}{U} = \dfrac{1}{U_{clean}} + R_f$, where $R_f$ is the fouling resistance in m$^2$ K/W.

For a counterflow exchanger with $C_r = 1$, the effectiveness formula reduces to $NTU / (1 + NTU)$.

## Worked example

**Given:** A counterflow water-to-water exchanger has hot water at $\dot{m}_h = 0.10\ \text{kg/s}$, entering
at $90\ \text{C}$ and leaving at $50\ \text{C}$. Cold water enters at $20\ \text{C}$ with $\dot{m}_c = 0.12\ \text{kg/s}$.
Take $c_p = 4190\ \text{J/(kg K)}$ for both streams, and assume $U = 800\ \text{W/(m}^2\text{K)}$ for the clean
exchanger.

**Find:** (a) the heat rate, (b) the cold outlet temperature, (c) the log mean temperature difference, (d)
the required area, (e) the effectiveness and NTU, and (f) the area needed if fouling adds
$R_f = 0.0002\ \text{m}^2\text{K/W}$.

**Assumptions:** Steady flow. Negligible heat loss to the surroundings. The specific heat is constant over
the range. The fouling resistance acts on the same area as $U$.

**Solution:**

1. Heat rate from the hot side: $\dot{Q} = 0.10 \times 4190 \times (90 - 50) = 16\,760\ \text{W}$, or 16.76 kW.
2. Cold outlet: $T_{c,out} = 20 + 16\,760 / (0.12 \times 4190) = 53.3\ \text{C}$.
3. Temperature differences at the ends: $\Delta T_1 = 90 - 53.3 = 36.7\ \text{K}$ and $\Delta T_2 = 50 - 20 =
   30.0\ \text{K}$. Then $\Delta T_{lm} = (36.7 - 30.0) / \ln(36.7 / 30.0) = 33.2\ \text{K}$.
4. Area: $A = \dot{Q} / (U \Delta T_{lm}) = 16\,760 / (800 \times 33.2) = 0.631\ \text{m}^2$.
5. Capacity rates: $C_h = 419\ \text{W/K}$ and $C_c = 503\ \text{W/K}$. So $C_{min} = 419\ \text{W/K}$, and $C_r =
   0.833$.
6. Maximum heat rate: $\dot{Q}_{max} = 419 \times (90 - 20) = 29\,330\ \text{W}$. Effectiveness: $\varepsilon =
   16\,760 / 29\,330 = 0.571$.
7. NTU: $UA / C_{min} = 800 \times 0.631 / 419 = 1.20$. Check with the counterflow formula: $\varepsilon = 0.571$,
   which matches step 6.
8. Fouling: $1/U = 1/800 + 0.0002 = 0.00145$, so $U = 690\ \text{W/(m}^2\text{K)}$. The new area is $16\,760 /
   (690 \times 33.2) = 0.732\ \text{m}^2$, which is 16 percent more.

**Answer:** (a) $\dot{Q} = 16.8\ \text{kW}$. (b) $T_{c,out} = 53.3\ \text{C}$. (c) $\Delta T_{lm} = 33.2\ \text{K}$.
(d) $A = 0.631\ \text{m}^2$. (e) $\varepsilon = 0.571$ and $NTU = 1.20$. (f) With fouling, $A = 0.732\ \text{m}^2$.

**Sanity check:** The heat rate is below the maximum of 29.3 kW, as it must be. The cold stream gains
$0.12 \times 4190 \times 33.33 = 16.76$ kW, the same as the hot stream loses. Fouling raises the area needed,
which is why designers add margin to the area for it.

## Design trade-offs

Designers balance heat transfer, pressure drop, size, cost, and cleaning. A higher flow speed raises the
coefficient and lowers fouling, but it raises pumping power, because pressure drop grows roughly with the
square of velocity in the pipe. A larger area lowers the outlet temperature gap, but it costs more.

Typical overall coefficients differ by orders of magnitude. Water-to-water exchangers often reach about
850 to 1700 W/(m$^2$ K), while gas-to-water exchangers such as air-side coils reach only about 10 to 100
W/(m$^2$ K) on the bare surface (typical textbook ranges). Fins on the gas side recover much of that gap.

Plate exchangers are compact and easy to open for cleaning, but gaskets limit their temperature and
pressure. Shell-and-tube units handle high pressure and dirty fluids, but they are bulky and costly per
unit of area. Finned coils are light and cheap, but they collect dust and are hard to clean.

Materials matter. Copper and aluminum conduct heat well, but seawater or acid attacks them. Stainless steel
resists corrosion at higher cost.

## How it fails

- Fouling. Scale, biofilm, dust, or oil builds on the surfaces and adds resistance. The heat rate falls
  while the pump works harder.
- Corrosion. Pitting or erosion thins the tube or plate wall until it leaks, and mixed streams can
  contaminate each other.
- Freezing. Water in an exchanger that reaches $0\ \text{C}$ expands and cracks the tubes. Antifreeze and drain
  valves protect against this.
- Thermal stress. Large temperature differences between the tubes and the shell cause movement and cracks,
  so floating-head or expansion joints are used.
- Gasket failure in a plate exchanger leads to leakage between the two fluids.
- Flow-induced vibration in tube bundles can wear tubes through over time.

Safety measures exist because of these faults. Pressure relief valves protect the shell and tubes. Shells
are designed to pressure codes and tested before use. Plate units have leak detection and gasket
inspection. Freeze protection uses glycol mixtures or heat tracing.

## History

James Watt's separate condenser, patented in 1769, is an early heat exchanger. It cooled the steam from a
cylinder in a separate vessel, which kept the cylinder hot and saved fuel. Joseph Fourier published his
theory of heat conduction in 1822, and it gave engineers the basic equation for heat flow through a wall.
Sadi Carnot's 1824 work on heat engines set the limits on how much of the heat can become work.
## Practice

1. An exchanger has $U = 500\ \text{W/(m}^2\text{K)}$, $A = 2.0\ \text{m}^2$, and $\Delta T_{lm} = 20\ \text{K}$.
   Find $\dot{Q}$.
2. A counterflow exchanger has $C_{min} = 200\ \text{W/K}$, hot inlet at $90\ \text{C}$, cold inlet at $20\ \text{C}$,
   and $\varepsilon = 0.75$. Find $\dot{Q}$.
3. A clean exchanger has $U = 1000\ \text{W/(m}^2\text{K)}$, and fouling adds $R_f = 0.0005\ \text{m}^2\text{K/W}$. Find
   the fouled $U$.
4. The two ends of an exchanger have temperature differences of $40\ \text{K}$ and $10\ \text{K}$. Find
   $\Delta T_{lm}$.
5. An exchanger has $UA = 5000\ \text{W/K}$ and $C_{min} = 2000\ \text{W/K}$. Find the NTU.

<details><summary>Answers</summary>

1. $\dot{Q} = 500 \times 2.0 \times 20 = 20\,000\ \text{W}$, or 20 kW
2. $\dot{Q} = 0.75 \times 200 \times (90 - 20) = 10\,500\ \text{W}$, or 10.5 kW
3. $U = 1 / (1/1000 + 0.0005) = 667\ \text{W/(m}^2\text{K)}$
4. $\Delta T_{lm} = (40 - 10) / \ln(40/10) = 21.6\ \text{K}$
5. $NTU = 5000 / 2000 = 2.5$

</details>

## Common mistakes

- Using the arithmetic mean temperature difference instead of the log mean for a sizing calculation. The
  arithmetic mean is only a rough check when the two ends differ by a small amount.
- Mixing up $C_{min}$ and $C_{max}$ in the effectiveness calculation. The smaller capacity rate sets the
  maximum heat rate.
- Adding fouling as a multiplier on $U$. It adds to the resistance: $1/U$ rises by $R_f$.
- Treating the overall $U$ as the same on both sides. A gas-side coefficient is often far lower than a
  liquid-side one, and the smaller one dominates.
- Assuming a counterflow exchanger and a parallel-flow exchanger give the same outlet temperatures. They do
  not, and the formulas differ.

## Go deeper

- [University Physics Volume 2, Chapter 1 (thermodynamics and heat transfer)](https://openstax.org/books/university-physics-volume-2/pages/1-introduction)
  by OpenStax: the heat transfer mechanisms that set each resistance in the heat exchanger.
- Next: [Internal combustion engines](06-internal-combustion-engines.md), where the radiator and charge air
  cooler are heat exchangers.
- Related: [Heat transfer](../../physics/12-heat-transfer.md) for the thermal resistance network,
  [Refrigeration and air conditioning](03-refrigeration-and-air-conditioning.md) for the evaporator and
  condenser coils, and [Heat pumps](04-heat-pumps.md) for heat exchangers on the source side.
