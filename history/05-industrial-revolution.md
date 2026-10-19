# The industrial revolution

**Type:** lesson

Between about 1760 and 1840, British engineers began replacing work done by muscle, water, and wood with steam engines, iron parts, and machines that cut metal to measured sizes. These changes made factories, railways, and steamships practical. They also set habits that engineers still use. Measure the part, standardize its size, and build it to a tolerance.

**Prerequisites:** [Scientific revolution](04-scientific-revolution.md), [Thermodynamics: properties, work, heat, and the first law](../physics/08-thermo-first-law.md), [Thermodynamics: entropy, the second law, and cycles](../physics/09-thermo-second-law-cycles.md)
**Time:** 2-3 h

## Core ideas

### Pumping water out of mines

Coal mines flooded as they went deeper. Pumps driven by horses or water wheels could not lift enough water from deep shafts. In about 1712, Thomas Newcomen built an atmospheric engine in England that pumped water. Steam filled a cylinder above a piston. Cold water sprayed into the cylinder condensed the steam, and the pressure inside dropped. Atmospheric pressure then pushed the piston down and did work. The work per stroke equals atmospheric pressure times the swept volume. The engine worked, but it wasted heat, because the cylinder cooled and reheated on every stroke.

### Watt's separate condenser

James Watt made scientific instruments at the University of Glasgow. In the 1760s he repaired a model Newcomen engine and saw the waste clearly. His fix was to condense the steam in a separate vessel, so the main cylinder stayed hot. He patented the separate condenser in 1769. In 1775 he and Matthew Boulton formed a business at Soho, near Birmingham, that built and sold engines. Watt later added a double-acting cylinder, which pushed the piston on both strokes, and a sun and planet gear that turned the reciprocating motion into rotation for mills. The worked example below shows why keeping the cylinder hot saves fuel.

### Iron and coal

Engines and machines needed far more iron than the old charcoal furnaces could supply. Coke, made by heating coal, replaced charcoal as the smelting fuel, and furnaces made iron in larger amounts at lower cost. Abraham Darby III completed the Iron Bridge at Coalbrookdale, Shropshire, in 1779. It was one of the first large structures made from cast iron, and it showed that iron could carry loads in a new form. Coal also fueled the engines that pumped the mines, so the coal and iron industries grew together.

### Machine tools and interchangeable parts

Engines needed accurate cylinders and pistons, and the existing tools could not make them well. Henry Maudslay, working in London, built a screw-cutting lathe about 1800 that cut accurate threads. Accurate threads let makers build parts to a common standard, so a nut from one shop fit a bolt from another. Through the 19th century, makers used gauges and tolerances to hold parts to a stated size.

### Railways and steel

Early railways needed locomotives that ran reliably and rails that lasted. The *Rocket*, designed by Robert Stephenson with his father George and built by Robert Stephenson and Company, won the Rainhill Trials in Lancashire in 1829. The Liverpool and Manchester Railway opened in 1830 and used steam locomotives for passengers and freight. Iron rails wore out quickly under heavy trains. Henry Bessemer patented a converter in 1856 that blew air through molten pig iron and made steel in bulk. Cheap steel then went into rails, ships, and bridges.

### How it spread

Engineers moved ideas with drawings, workers, and machines. A machine tool built in London or Birmingham could be copied in France, Germany, or the United States. The change took decades, and it came unevenly. Coal, iron ore, canals, and later railways set where factories grew. The pattern was not a single invention followed by a sudden shift.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| about 1712 | Atmospheric steam engine for pumping | Thomas Newcomen, England | Pumped water from deep mines with steam and atmospheric pressure |
| 1769 | Separate condenser | James Watt, Glasgow | Kept the cylinder hot, which cut fuel per unit of work |
| 1775 | Boulton and Watt engine business | Watt and Matthew Boulton, Soho near Birmingham | Built and sold engines with machined parts |
| 1781 | Sun and planet gear for rotary motion | James Watt, England | Let a steam engine turn a mill wheel |
| 1782 | Double-acting cylinder | James Watt, England | Used steam on both sides of the piston |
| about 1800 | Screw-cutting lathe | Henry Maudslay, London | Cut accurate threads, which supported standard parts |
| 1829 | *Rocket* wins the Rainhill Trials | George Stephenson, Lancashire | Showed that a locomotive could run reliably enough for railways |
| 1830 | Liverpool and Manchester Railway opens | George Stephenson and partners, England | An early public railway that used steam locomotives for passengers and freight |
| 1856 | Bessemer steelmaking process | Henry Bessemer, England | Made steel cheap enough for rails, ships, and bridges |

## Key equations

Carnot efficiency, the ideal limit for a heat engine that runs between two temperatures:

$$\eta_C = 1 - \frac{T_c}{T_h}$$

Here $T_h$ is the hot temperature in kelvin (K), $T_c$ is the cold temperature in kelvin (K), and $\eta_C$ is the dimensionless efficiency. Real engines always fall below this limit.

Work per stroke of an atmospheric engine:

$$W = p_{atm} V_s$$

Here $p_{atm}$ is atmospheric pressure, about $101\ \text{kPa}$ at sea level, and $V_s$ is the swept volume in cubic metres (m$^3$). The work $W$ is in joules (J).

Horsepower, the unit that came from comparing engine output with the work that horses did:

$$1\ \text{hp} = 550\ \text{ft lbf/s} = 745.7\ \text{W}$$

## Worked example: why a separate condenser saved fuel

**Given:** Steam is available at $373\ \text{K}$ (100 C). The cold sink is cooling water at $303\ \text{K}$ (30 C).

**Find:** The ideal efficiency of each engine, and how much more heat the Newcomen engine needs for the same ideal work.

**Assumptions:**

1. Watt's cylinder stays at the steam temperature, $T_h = 373\ \text{K}$.
2. In the Newcomen engine, cold spray cools the cylinder wall between strokes, and steam reheats it. Assume the wall acts at an average effective hot temperature of $340\ \text{K}$. This value is an illustrative assumption, not a measured number.
3. Both engines reject heat to the same $303\ \text{K}$ sink.
4. Both engines run at their Carnot limit, so the comparison reflects temperature alone.

**Solution:**

1. Watt engine: $\eta_W = 1 - 303/373 = 0.188$, which is 18.8 percent.
2. Newcomen engine: $\eta_N = 1 - 303/340 = 0.109$, which is 10.9 percent.
3. Heat needed per unit of ideal work scales as $1/\eta$. The ratio is $\eta_W / \eta_N = 0.188 / 0.109 = 1.7$.

**Answer:** Under these assumptions, the Newcomen engine needs about 1.7 times as much heat for the same ideal work as Watt's engine.

**Sanity check:** Both efficiencies sit below 1, and the Watt value is higher, as expected. The ratio measures only the temperature effect. Real Newcomen engines also lost heat through leaks, friction, and steam that never condensed properly, so the true fuel ratio differs from this number. The example shows the direction and rough size of the gain from keeping the hot part hot.

## Lessons for engineers today

- A heat engine is limited by its hot and cold temperatures. Estimate the Carnot limit before you tune losses.
- Keep the working fluid at the highest safe temperature where it does work, and reject heat at a separate cold sink. Power-plant condensers and heat-recovery systems follow this rule.
- Standard threads, gauges, and tolerances let separate shops build parts that fit. A drawing with a tolerance is a contract that any shop can check.
- Material choice limits what a machine can do. Iron allowed the first engines, and cheap steel allowed railways and large bridges.
- Early machines improved by testing and measurement, not by one insight. Watt's condenser came from a repair and a measurement of wasted fuel.

## Practice

1. A boiler runs at 500 K and the condenser runs at 300 K. Find the Carnot efficiency.
2. Convert 1 horsepower (550 ft lbf/s) to watts, using 1 ft = 0.3048 m and 1 lbf = 4.448 N.
3. A cylinder is cooled by spray each stroke. Explain in two sentences why this lowers the effective hot temperature, and why a separate condenser avoids the loss.
4. An engine runs between 360 K and 300 K. Find its Carnot efficiency, and compare it with the 500 K and 300 K engine in problem 1.
5. Name two reasons standard threads helped the factories of the 19th century, and explain why each reason matters to a maintenance crew.

<details><summary>Answers</summary>

1. $\eta_C = 1 - 300/500 = 0.40$, which is 40 percent.
2. $550 \times 0.3048 \times 4.448 = 745.7\ \text{W}$, so 1 hp is about 746 W.
3. The spray cools the cylinder wall, so each new stroke starts with steam meeting a cold surface, and the wall must be reheated. The average temperature where heat enters the work cycle falls. A separate condenser keeps the cylinder at the steam temperature, so the cylinder does not need reheating.
4. $\eta_C = 1 - 300/360 = 0.167$, which is 16.7 percent. The 500 K engine gives 40 percent, so the hotter boiler gives the larger limit.
5. Any two of these work. Standard threads allow a replacement part from another shop to fit. Standard threads also let a crew stock fewer part types. Both matter because a machine stays out of service until its broken part is replaced.

</details>

## Common mistakes

- James Watt invented the steam engine. Thomas Savery and Thomas Newcomen built earlier engines. Watt's main contribution was the separate condenser, which raised fuel efficiency.
- Eli Whitney invented interchangeable parts. Historians debate how far his 1798 musket contract achieved this. Standard parts grew from many workshops and from the machine tools that made precise cuts.
- The industrial revolution happened in a few years. The changes took decades and spread unevenly across countries.
- The Carnot efficiency predicts what a real engine delivers. It is a ceiling, and real engines run well below it.

## Go deeper

- [Lives of Boulton and Watt](https://www.gutenberg.org/ebooks/52069), Samuel Smiles, free on Project Gutenberg. A 19th-century biography that describes the Soho partnership and early engines.
- [Reflections on the motive power of heat](https://www.gutenberg.org/ebooks/78610), Sadi Carnot, free on Project Gutenberg. The 1824 work that introduced the efficiency limit.
- [University Physics Volume 2, Chapter 1](https://openstax.org/books/university-physics-volume-2/pages/1-introduction), OpenStax, free. Heat, temperature, and the basics of thermodynamics.
- Related lessons: [Thermal systems](../applications/thermal-fluid/01-thermal-systems.md), [Thermodynamics II](../physics/09-thermo-second-law-cycles.md), [Steam power plants](../applications/thermal-fluid/08-steam-power-plants.md), and [Electrical age](06-electrical-age.md).
- [History of engineering reference](reference.md): the lookup sheet for this topic.
