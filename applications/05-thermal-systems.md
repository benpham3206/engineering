# Thermal systems: conduction, convection, and thermal resistance

Thermal engineers keep parts cool, keep rooms warm, and move heat from one place to another. A
processor needs a heat sink, a building needs insulation, and a heat exchanger moves heat from hot
fluid to cold fluid. The same few ideas cover all three.

**Prerequisites:** [Circuit basics](01-circuit-basics.md) (the thermal analogy uses the same
voltage-and-resistance pattern), [Mathematics folder](../math/README.md)
**Time:** 8-12 h

## Core ideas

- **Temperature difference** $\Delta T$: heat flows from hot to cold. The heat rate is set by how big
  the temperature difference is and how easily heat passes through the path.
- **Heat rate** $\dot{Q}$ (watts, W): energy per second moving through a path.
- **Conduction**: heat moves through a solid by atom-to-atom transfer. The material property is the
  thermal conductivity $k$ in W/(m K). Metals have high $k$, and foams and air have low $k$.
- **Convection**: heat moves from a solid surface into a moving fluid such as air or water. The
  convection coefficient $h$ in W/(m$^2$ K) depends on the fluid, its speed, and the surface shape.
  Typical $h$ is about 5-25 W/(m$^2$ K) for natural air convection and higher for forced air.
- **Radiation**: heat carried by electromagnetic waves. It matters at high temperature or in vacuum.
  This lesson uses conduction and convection only.
- **Thermal resistance** $R_{th}$ (kelvin per watt, K/W): a path's resistance to heat flow. Layers in
  series add their resistances, just like resistors in series.
- **Thermal analogy**: temperature difference plays the role of voltage, heat rate plays the role of
  current, and thermal resistance plays the role of electrical resistance.
- **Heat sink**: a metal part with fins that increases surface area so convection can carry more heat
  to the air.
- **Units note**: a temperature difference is the same in kelvin and degrees Celsius. Use kelvin
  for absolute temperatures in gas laws, but differences can use either.

## Key equations

- Conduction through a plane wall of area $A$ (m$^2$) and thickness $L$ (m):
  $\dot{Q} = \dfrac{k A \Delta T}{L}$
- Thermal resistance of conduction: $R_{cond} = \dfrac{L}{k A}$ (K/W)
- Convection: $\dot{Q} = h A \Delta T$, with $h$ in W/(m$^2$ K).
- Thermal resistance of convection: $R_{conv} = \dfrac{1}{h A}$ (K/W)
- Layers in series: $R_{tot} = \sum R_i$, and $\dot{Q} = \dfrac{\Delta T_{total}}{R_{tot}}$.

## Worked example

**Given:** A brick-like wall of area $A = 10\ \text{m}^2$, thickness $L = 0.20\ \text{m}$, and
conductivity $k = 0.80\ \text{W/(m K)}$ separates a room at $25\ \text{C}$ from outdoor air at $5\ \text{C}$.
Assume the inside surface is at room temperature. The outside convection coefficient is
$h = 10\ \text{W/(m}^2\text{K)}$. Ignore the inside convection and the outer surface resistance.

**Find:** (a) the total thermal resistance, (b) the heat rate through the wall, and (c) the outer
surface temperature.

**Solution:**

1. Conduction resistance: $R_{cond} = L / (kA) = 0.20 / (0.80 \times 10) = 0.025\ \text{K/W}$.
2. Convection resistance outside: $R_{conv} = 1 / (hA) = 1 / (10 \times 10) = 0.010\ \text{K/W}$.
3. Total: $R_{tot} = 0.025 + 0.010 = 0.035\ \text{K/W}$.
4. Temperature difference: $\Delta T = 25 - 5 = 20\ \text{K}$.
5. Heat rate: $\dot{Q} = 20 / 0.035 = 571\ \text{W}$.
6. Outer surface temperature: the drop across the outer convection layer is $\dot{Q} R_{conv}$, which is
   $571 \times 0.010 = 5.7\ \text{K}$. The outer surface is therefore at $5 + 5.7 = 10.7\ \text{C}$.

Check the drop: $\dot{Q} R_{cond} = 571 \times 0.025 = 14.3\ \text{K}$. Adding that to the convection drop,
$14.3 + 5.7 = 20.0\ \text{K}$, which matches the total.

**Answer:** (a) $R_{tot} = 0.035\ \text{K/W}$. (b) $\dot{Q} = 571\ \text{W}$. (c) The outer surface is at
about $10.7\ \text{C}$.

**Sanity check:** A $20\ \text{K}$ difference across a wall of this size losing hundreds of watts is
plausible for a room, given $10\ \text{m}^2$ of area. The two drops, $14.3\ \text{K}$ and $5.7\ \text{K}$, add up to
the full $20\ \text{K}$.

## Practice

1. Aluminum, $k = 205\ \text{W/(m K)}$, $A = 0.002\ \text{m}^2$, $L = 0.010\ \text{m}$, $\Delta T = 30\ \text{K}$.
   Find $\dot{Q}$.
2. A surface with $h = 15\ \text{W/(m}^2\text{K)}$ and $A = 0.20\ \text{m}^2$ sees $\Delta T = 40\ \text{K}$.
   Find $\dot{Q}$.
3. A wall has $R_{th} = 0.05\ \text{K/W}$ and $\Delta T = 10\ \text{K}$. Find $\dot{Q}$.
4. Insulation with $k = 0.040\ \text{W/(m K)}$, $A = 10\ \text{m}^2$, $L = 0.10\ \text{m}$, and $\Delta T = 20\ \text{K}$.
   Find $\dot{Q}$.
5. A path carries $\dot{Q} = 100\ \text{W}$ across $\Delta T = 20\ \text{K}$. Find the total thermal resistance.

<details><summary>Answers</summary>

1. $1230\ \text{W}$
2. $120\ \text{W}$
3. $200\ \text{W}$
4. $80\ \text{W}$
5. $0.20\ \text{K/W}$

</details>

## Common mistakes

- Forgetting that heat flows from hot to cold, so the temperature difference must be the hot side minus
  the cold side.
- Mixing up the thickness and area in the conduction formula. $A$ is the cross-section the heat passes
  through, and $L$ is the length of the path.
- Adding thermal resistances in parallel as if they were in series. Layers that heat must cross one after
  another are in series.
- Forgetting the convection layer at a surface. Air films on both sides of a wall often matter more than
  the wall itself.
- Using a single textbook value of $h$ for every case. Convection coefficients depend strongly on airflow.

## Go deeper

- [University Physics Volume 2, Chapter 1 (thermodynamics, heat transfer)](https://openstax.org/books/university-physics-volume-2/pages/1-introduction)
  by OpenStax: heat transfer by conduction, convection, and radiation, with worked examples.
- [University Physics Volume 2, Chapter 3 (temperature and heat)](https://openstax.org/books/university-physics-volume-2/pages/3-introduction)
  by OpenStax: the definitions of heat and temperature that this lesson builds on.
- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: a free library that includes heat
  transfer textbooks.
- Next: [Lesson 06, fluid systems](06-fluid-systems.md).
