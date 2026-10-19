# Spacecraft and satellites

**Type:** lesson

Spacecraft and satellites are vehicles that operate in space, where there is no air to carry heat away and no grid to supply power. A satellite that fails in orbit usually cannot be repaired, so engineers must get every system right before launch.

A spacecraft must make its own electrical power, keep its electronics within a narrow temperature band, and point its antennas and sensors with precision. Engineers design these three systems together, because each one changes the mass, area, and heat load of the others.

**Prerequisites:** [Heat transfer](../../physics/12-heat-transfer.md), [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 8-12 h

## Core ideas

### How it works

A satellite is a body in orbit. Its speed and altitude set the orbit, and its orbit sets how much sunlight, eclipse, and radiation it sees.

The Sun delivers energy to the spacecraft as sunlight. The spacecraft has two ways to shed heat: it emits thermal radiation into space, and it conducts heat through its structure to radiators. The spacecraft is warm when it absorbs more power than it emits. It settles to a steady temperature when the two match. This is the thermal balance.

Power comes from solar arrays while the spacecraft is sunlit. During eclipse, when the Earth or Moon blocks the Sun, batteries supply the load. The array must produce enough energy to run the spacecraft and recharge the batteries over each orbit.

Attitude control keeps the antennas, cameras, and solar arrays pointed where they must be. Reaction wheels, thrusters, and magnetic torque rods change the orientation. Communications use radio links to a ground station, and the link budget sets the antenna size and transmitter power.

### Main parts

- **Structure**: the frame that holds the mass and carries launch loads.
- **Solar arrays**: panels of photovoltaic cells that turn sunlight into electricity.
- **Batteries**: store energy for eclipse periods and peak loads. Lithium-ion cells are common today.
- **Power electronics**: regulate the bus voltage and route power between the array, batteries, and loads.
- **Thermal control**: multilayer insulation blankets, paints or coatings with set absorptance and emittance, heaters, and radiator panels.
- **Attitude control**: sensors such as star trackers, sun sensors, and gyroscopes, plus actuators such as reaction wheels and thrusters.
- **Propulsion**: thrusters that change orbit, correct drift, and dump momentum from the reaction wheels.
- **Payload and communications**: the instruments, the antenna, and the transmitter and receiver.

### Variants

- **Low Earth orbit (LEO)**: about 200 to 2000 km altitude. Short orbital period, frequent eclipse, and fast ground passes. Used for Earth imaging and the International Space Station.
- **Medium Earth orbit (MEO)**: about 2000 to 35 000 km. Used for navigation constellations such as GPS.
- **Geostationary orbit (GEO)**: about 35 786 km altitude above the equator. The period matches the Earth's rotation, so the satellite stays over one point. Used for weather and broadcast communication.
- **Deep space probes**: far from the Sun, with small solar arrays or radioisotope generators. Their power and temperature change with distance from the Sun.

## Key equations

The solar constant $S$ is the solar power per unit area at a given distance from the Sun. At 1 AU, the Earth's mean distance from the Sun, a typical value is $S_0 \approx 1361\ \text{W}/\text{m}^2$. Farther out, the flux falls with the square of the distance:

$$S(r) = S_0 \left(\frac{1\ \text{AU}}{r}\right)^2$$

where $r$ is the distance from the Sun in astronomical units. A spacecraft at 1.52 AU, the distance of Mars, sees about $589\ \text{W}/\text{m}^2$. The values in this lesson use 1 AU unless stated otherwise.

For a flat plate facing the Sun, the absorbed power per unit area is $\alpha S$, where $\alpha$ is the solar absorptance (dimensionless). The plate emits thermal radiation at the Stefan-Boltzmann rate:

$$q_{\text{emit}} = \varepsilon \sigma T^4$$

where $\varepsilon$ is the infrared emittance (dimensionless), $\sigma = 5.670 \times 10^{-8}\ \text{W/(m}^2\ \text{K}^4)$ is the Stefan-Boltzmann constant, and $T$ is the absolute temperature in kelvin (K).

For a plate sunlit on one face and radiating from both faces with no internal power, the balance per unit area is:

$$\alpha S = 2 \varepsilon \sigma T^4 \quad\Rightarrow\quad T = \left(\frac{\alpha S}{2 \varepsilon \sigma}\right)^{1/4}$$

Solar array area for a steady electrical load $P_{\text{load}}$ in watts:

$$A = \frac{P_{\text{load}}}{\eta \, S \, f_{\text{deg}} \, \cos\theta}$$

where $A$ is the array area in square metres (m$^2$), $\eta$ is the cell efficiency (dimensionless), $f_{\text{deg}}$ is the fraction of beginning-of-life output left at end of life (dimensionless), and $\theta$ is the angle between the Sun and the array normal in degrees.

## Worked example

**Given:** A flat plate in orbit at 1 AU has solar absorptance $\alpha = 0.25$ and infrared emittance $\varepsilon = 0.85$, typical of a white thermal coating. The plate faces the Sun squarely. It radiates from both faces, has no internal heat source, and gets no Earth albedo or Earth infrared. Solar constant $S_0 = 1361\ \text{W}/\text{m}^2$.

**Find:** (a) the equilibrium temperature of the plate at 1 AU, (b) the equilibrium temperature at 1.52 AU, and (c) the solar array area for a 500 W load with cell efficiency $\eta = 0.30$, end-of-life factor $f_{\text{deg}} = 0.80$, and incidence $\cos\theta = 0.95$ at both distances.

**Assumptions:** Steady state. Uniform plate temperature. Constant $\alpha$ and $\varepsilon$.

**Solution:**

1. Absorbed flux at 1 AU: $\alpha S_0 = 0.25 \times 1361 = 340\ \text{W}/\text{m}^2$.
2. Balance with two radiating faces: $T = (340 / (2 \times 0.85 \times 5.670 \times 10^{-8}))^{1/4} = 244\ \text{K}$, which is $-29\ ^\circ\text{C}$.
3. Solar constant at 1.52 AU: $S = 1361 / 1.52^2 = 589\ \text{W}/\text{m}^2$.
4. Balance at 1.52 AU: $T = (0.25 \times 589 / (2 \times 0.85 \times 5.670 \times 10^{-8}))^{1/4} = 198\ \text{K}$, which is $-75\ ^\circ\text{C}$.
5. Array area at 1 AU: $A = 500 / (0.30 \times 1361 \times 0.80 \times 0.95) = 1.61\ \text{m}^2$.
6. Array area at 1.52 AU: $A = 500 / (0.30 \times 589 \times 0.80 \times 0.95) = 3.72\ \text{m}^2$.

**Answer:** (a) 244 K, about $-29\ ^\circ\text{C}$. (b) 198 K, about $-75\ ^\circ\text{C}$. (c) 1.61 m$^2$ at 1 AU and 3.72 m$^2$ at 1.52 AU.

**Sanity check:** The farther plate sees $1/2.31$ of the sunlight, so its temperature falls, and the array area grows by the same factor $2.31$. The ratio $3.72 / 1.61 = 2.31$ matches. A plate in full sun with no coating would run far hotter, so the low absorptance is what keeps it cool.

## Design trade-offs

- **Coating choice**: a low $\alpha / \varepsilon$ ratio keeps the spacecraft cool. Optical solar reflectors and white paints both use this idea. The coating must also survive ultraviolet light and atomic oxygen in low orbit, which change $\alpha$ over the mission.
- **Array size and mass**: a larger array gives more power but adds mass and drag in low orbit. Mass is the main cost of launch, so designers size the array to the mission, not to the largest possible load.
- **Battery size against eclipse**: a long eclipse needs more battery energy. A battery adds mass, and its life falls when it cycles deeply every orbit.
- **Radiator area against heat load**: radiators reject heat by emission, so a hotter electronics box needs a larger radiator. Heaters keep cold parts warm during eclipse or at large distances from the Sun.
- **Pointing accuracy against cost**: a precise pointing system uses better sensors and stronger actuators. Cameras and radars need tight pointing, and a communication dish often needs less.

## How it fails

- **Overheating**: a radiator blocked by a mis-oriented panel, a coating degraded by ultraviolet light, or a stuck louver raises temperatures. Electronics and batteries have upper temperature limits. Louvers and thermostatically controlled heaters are the safety measures.
- **Freezing**: a long eclipse or a large distance from the Sun drops parts below their lower limit. Heaters, insulation blankets, and a survival mode that shuts off nonessential loads are the protection.
- **Power loss**: solar array damage, a degraded cell string, or a battery fault reduces the energy budget. Designers include margin, and operators can shed loads.
- **Attitude loss**: a failed gyroscope, a stuck reaction wheel, or a bad sensor can point the spacecraft in the wrong direction. Safe modes point the arrays at the Sun and the antenna at the ground.
- **Radiation damage**: charged particles upset memory and damage solar cells over time. Shielding, error-correcting memory, and radiation-hardened parts reduce the risk.
- **Micrometeoroids and debris**: small impacts can puncture panels or radiators. Shielding and placing sensitive parts behind structure reduce the damage.

## History

The Soviet Union launched Sputnik 1 on 4 October 1957, the first artificial satellite. The United States launched Explorer 1 on 31 January 1958, which discovered the Van Allen radiation belts. Telstar 1, launched on 10 July 1962, relayed the first live transatlantic television pictures and was built by Bell Telephone Laboratories. Josef Stefan published the law of thermal radiation in 1879, and Ludwig Boltzmann derived it from theory in 1884. The law that bears both names is the basis of every spacecraft thermal calculation.

## Practice

1. The solar constant at 1 AU is 1361 W/m$^2$. Find the solar flux at 2 AU.
2. A 0.50 m$^2$ panel faces the Sun squarely at 1 AU. Find the solar power it intercepts.
3. A black plate with $\alpha = \varepsilon = 1$ faces the Sun at 1 AU and radiates from one face only. Find its equilibrium temperature in kelvin.
4. A 1 kW load needs an array with cell efficiency 0.28, end-of-life factor 0.75, and normal incidence at 1 AU. Find the array area.
5. A plate with $\alpha = 0.25$ and $\varepsilon = 0.85$ radiates from both faces at 1.52 AU. Find its equilibrium temperature in kelvin and in degrees Celsius.

<details><summary>Answers</summary>

1. $S = 1361 / 4 = 340\ \text{W}/\text{m}^2$
2. $P = 1361 \times 0.50 = 680\ \text{W}$
3. $T = (1361 / 5.670 \times 10^{-8})^{1/4} \approx 394\ \text{K}$, which is about 121 $^\circ$C
4. $A = 1000 / (0.28 \times 1361 \times 0.75) \approx 3.5\ \text{m}^2$
5. $T \approx 198\ \text{K}$, which is about $-75\ ^\circ\text{C}$

</details>

## Common mistakes

- Using the solar constant at 1 AU for a spacecraft near Mars or Jupiter. The flux falls with the square of distance, so scale it first.
- Setting absorptance equal to emittance for a coated surface. Coatings have very different solar and infrared properties, and the ratio $\alpha / \varepsilon$ controls the temperature.
- Forgetting that the array only sees the Sun for part of each orbit. Eclipse energy must come from the batteries.
- Sizing the array from beginning-of-life output and ignoring degradation, incidence angle, and efficiency loss over time.
- Treating a radiator as if it absorbs heat from the Sun. A radiator is sized to emit heat to cold space, and sunlight on it raises its temperature.

## Go deeper

- [University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax: a free introductory textbook on mechanics, gravitation, and fluids. It is licensed CC BY-NC-SA.
- [MIT OpenCourseWare](https://ocw.mit.edu/): free lecture notes, exams, and videos from MIT, with no registration required. Search for courses on orbital mechanics and spacecraft design.
- Related: [Rockets](07-rockets.md), [Photovoltaics](../energy/01-solar-photovoltaics.md), [Batteries](../electrical/06-batteries.md), [Thermal systems](../thermal-fluid/01-thermal-systems.md), [Orbital mechanics and rockets](../../physics/15-orbital-mechanics-and-rockets.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
