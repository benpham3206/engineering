# Heat transfer

**Type:** lesson

**Heat transfer** is the movement of thermal energy caused by a temperature difference, through conduction, convection, and radiation. Engineers use it to keep buildings warm, electronics cool, and engines within their material limits.

**Prerequisites:** [Oscillations, waves, light, and heat](07-waves-light-heat.md), [Thermodynamics: properties, work, heat, and the first law](08-thermo-first-law.md)
**Time:** 8-10 h

## Core ideas

- **Heat** ($Q$, or $q$ for a rate) is energy that moves because of a temperature difference. Heat transfer rate is measured in watts ($\mathrm{W} = \mathrm{J/s}$).
- **Heat flux** $q''$ is heat rate per unit area ($\text{W/m}^2$). It is often easier to work with than the total rate.
- There are three modes:
  - **Conduction**: energy moves through a solid or stationary fluid by molecular motion and electron motion. Metals conduct well. Foam and air conduct poorly.
  - **Convection**: energy is carried by fluid motion. Forced convection uses a fan or pump. Natural convection uses buoyancy from warm, less dense fluid.
  - **Radiation**: energy travels as electromagnetic waves. It needs no medium, so it works across vacuum. Sunlight reaching Earth is radiation.
- **Thermal conductivity** $k$ describes how well a material conducts heat (W/m K). Typical values: copper about 400 W/m K, concrete about 1 W/m K, fiberglass insulation about 0.04 W/m K.
- **Convection coefficient** $h$ describes how well a fluid carries heat away from a surface ($\text{W/m}^2$ K). Typical values: still air about 5-10, moving air 25-250, moving water 500-10 000.
- **Emissivity** $\varepsilon$ is a number from 0 to 1 that says how well a surface radiates compared with a perfect black body. Dull black paint is close to 0.9. Polished aluminum is often around 0.05.
- **Steady state** means temperatures do not change with time. Most design problems assume this.
- **Thermal resistance** $R$ (K/W) is the temperature difference needed to drive one watt through a path. Heat flow is $\Delta T / R$. This is the same idea as Ohm's law for electrical resistance.

### Conduction

For steady one-dimensional conduction through a flat plate (a plane wall), the heat rate is proportional to area and temperature difference and inversely proportional to thickness. The thermal resistance of a plane wall is $L/(kA)$.

Conduction tells you how fast heat moves through a material, not how fast it moves from air into the material. That job belongs to convection.

### Convection

Newton's law of cooling says heat leaving a surface is proportional to the surface area and the temperature difference between the surface and the fluid. The constant of proportionality is $h$. The thermal resistance of a convective boundary is $1/(hA)$.

The convection coefficient depends on the fluid, its speed, the surface shape, and whether the flow is laminar or turbulent. Lessons on fluid flow and boundary layers give you the tools to estimate it. In this lesson, use a given $h$.

### Radiation

Radiation from a surface at absolute temperature $T$ into surroundings at $T_\text{sur}$ follows the **Stefan-Boltzmann law**. The net flux depends on the fourth powers of absolute temperature, so it is strongly nonlinear. Two points to remember:

- Use absolute temperature (kelvin). Degrees Celsius will give wrong answers.
- Radiation is often comparable to convection for hot surfaces in still air, and small for surfaces near room temperature.

For design, engineers often write a **radiation coefficient** $h_r$ so that radiation looks like a convection term. This works only near the chosen temperature and is an approximation.

### Thermal resistance networks

A chain of layers in series works like a series electrical circuit. For one-dimensional steady heat flow through a composite wall with convection on both sides:

- Each layer adds a resistance.
- Total resistance is the sum.
- Heat rate is the total temperature difference divided by the total resistance.
- The temperature at any interface can be found by stepping down from one side, using $\Delta T = q R$ for each element.

This method is quick. Use it first before attempting a full solution with differential equations.

### Common assumptions

- Steady state.
- One-dimensional heat flow (no sideways variation).
- Uniform properties within each layer.
- Constant $h$ over each surface.
- Radiation neglected unless the problem gives you emissivity and temperatures.

## Key equations

Symbols: $q$ $=$ heat rate (W), $q''$ $=$ heat flux ($\text{W/m}^2$), $k$ $=$ thermal conductivity (W/m K), $A$ $=$ area ($\text{m}^2$), $L$ $=$ thickness (m), $h$ $=$ convection coefficient ($\text{W/m}^2$ K), $\varepsilon$ $=$ emissivity (dimensionless), $\sigma$ $=$ Stefan-Boltzmann constant, $5.670 \times 10^{-8}$ $\text{W/m}^2$ $\text{K}^4$, $T$ and $T_\text{sur}$ $=$ absolute temperatures (K), $\Delta T$ $=$ temperature difference (K), $R$ $=$ thermal resistance (K/W).

Fourier's law for conduction through a plane wall:

$$
q = \frac{k A \,\Delta T}{L}, \qquad R_\text{cond} = \frac{L}{kA}
$$

Newton's law of cooling for convection:

$$
q = h A \,\Delta T, \qquad R_\text{conv} = \frac{1}{hA}
$$

Net radiation from a gray surface to a large enclosure:

$$
q = \varepsilon \sigma A \left(T^4 - T_\text{sur}^4\right)
$$

Series resistance network for a wall with convection on both sides:

$$
q = \frac{T_{\infty,1} - T_{\infty,2}}{\dfrac{1}{h_1 A} + \dfrac{L_1}{k_1 A} + \dfrac{L_2}{k_2 A} + \dfrac{1}{h_2 A}}
$$

Here $T_{\infty,1}$ and $T_{\infty,2}$ are the fluid temperatures on each side.

## Worked example

**Insulated exterior wall section.** A wall section is 1.0 $\text{m}^2$ in area. From inside to outside it has:

- Inside air convection, $h_i = 8$ $\text{W/m}^2$ K (typical value for still indoor air).
- Brick, thickness 0.10 m, $k = 0.72$ W/m K (typical value).
- Mineral wool insulation, thickness 0.05 m, $k = 0.04$ W/m K (typical value).
- Outside air convection, $h_o = 25$ $\text{W/m}^2$ K (typical value for a windy outside).

Inside air is at 21 °C, outside air at $-5$ °C. Find the heat rate through the wall, and find the temperature at the brick-insulation interface and at the insulation's outer surface.

**Given:** $A = 1.0$ $\text{m}^2$, $T_\text{in} = 21$ °C, $T_\text{out} = -5$ °C, layers as above.

**Find:** $q$, $T_1$ (inside surface of the brick), $T_2$ (brick-insulation interface), and $T_3$ (outer surface of the insulation).

**Assumptions:** steady, one-dimensional, uniform properties, radiation neglected.

**Solution:**

1. Resistances (per unit area, $A = 1$ $\text{m}^2$):
   - Inside convection: $R_i = 1/(8 \times 1) = 0.125$ K/W.
   - Brick: $R_b = 0.10/(0.72 \times 1) = 0.1389$ K/W.
   - Insulation: $R_\text{ins} = 0.05/(0.04 \times 1) = 1.250$ K/W.
   - Outside convection: $R_o = 1/(25 \times 1) = 0.040$ K/W.
   - Total: $R_\text{tot} = 0.125 + 0.1389 + 1.250 + 0.040 = 1.554$ K/W.
2. Heat rate: $q = (21 - (-5)) / 1.554 = 26 / 1.554 = 16.7$ W.
3. Step down through the layers, using $\Delta T = qR$:
   - Inside surface of the brick: $T_1 = 21 - 16.7 \times 0.125 = 18.9$ °C.
   - Brick-insulation interface: $T_2 = 18.9 - 16.7 \times 0.1389 = 16.6$ °C.
   - Outer surface of the insulation: $T_3 = 16.6 - 16.7 \times 1.250 = -4.3$ °C.

**Answer:** $q = 16.7$ W through the 1.0 $\text{m}^2$ section, so the heat flux is 16.7 $\text{W/m}^2$. $T_1 = 18.9$ °C, $T_2 = 16.6$ °C, $T_3 = -4.3$ °C.

**Sanity check:** The outer air-to-surface drop is $q/(h_o A) = 16.7 / 25 = 0.67$ K, and $T_3 - T_\text{out} = -4.33 - (-5) = 0.67$ K. They agree. Most of the temperature drop (about 21 K of the total 26 K) happens across the insulation, which has the largest resistance.

## Practice

1. A concrete wall is 0.20 m thick, with $k = 1.0$ W/m K, area 10 $\text{m}^2$, and temperature difference 15 K across it. Find the heat rate in W.
2. A surface with $h = 10$ $\text{W/m}^2$ K and area 2.0 $\text{m}^2$ is at 20 K above the air. Find the heat rate in W.
3. A surface with $\varepsilon = 0.8$ at 350 K radiates to surroundings at 300 K. Find the net radiative flux in $\text{W/m}^2$.
4. A wall has $h_\text{in} = 10$ $\text{W/m}^2$ K, a layer of $L = 0.10$ m with $k = 0.5$ W/m K, and $h_\text{out} = 20$ $\text{W/m}^2$ K. Its area is 1.0 $\text{m}^2$, the inside air is at 30 °C, and the outside air is at 0 °C. Find the heat rate in W.

<details><summary>Answers</summary>

1. 750 W
2. 400 W
3. 313.3 $\text{W/m}^2$
4. 85.7 W

</details>

## Common mistakes

- Using Celsius in the radiation formula. Always convert to kelvin before taking the fourth power.
- Forgetting one resistance in a series network, usually one of the convection films.
- Mixing per-unit-area and total resistances in the same sum. Either divide everything by $A$ or use total values throughout.
- Assuming a large $k$ means a large heat rate. Heat rate depends on $\Delta T$ and the total resistance, not on $k$ alone.
- Treating a surface as a black body when its emissivity is much less than 1, such as polished metal.

## Go deeper

- [*A Heat Transfer Textbook*](https://ahtt.mit.edu/) by John H. Lienhard IV and John H. Lienhard V, MIT: a free, full heat transfer textbook covering conduction, convection, and radiation.
- [*A Heat Transfer Textbook*, table of contents](https://ahtt.mit.edu/table-of-contents) by the same authors: the chapter list, including conduction (chapters 2, 4, and 5), convection (chapters 6 to 8), and radiation (chapter 10).
- Previous: [Control volumes and pipe flow](11-control-volumes-pipe-flow.md) covers the convection boundary conditions and fluid flow ideas you need before the convection chapters of the textbook.
- [Thermal-fluids reference](reference-thermofluids.md): the lookup sheet for this topic.
