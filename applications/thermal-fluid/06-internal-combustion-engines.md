# Internal combustion engines

**Type:** lesson

An internal combustion engine burns fuel inside its own cylinders and turns the heat from that burning into shaft work. Engineers use it to size power and torque, to predict fuel use, and to meet emissions limits in cars, trucks, generators, and small tools.

**Prerequisites:** [First law of thermodynamics](../../physics/08-thermo-first-law.md), [Second law and cycles](../../physics/09-thermo-second-law-cycles.md)
**Time:** 8-12 h

## Core ideas

### How it works

Most engines on the road use a four-stroke cycle. The piston makes four strokes, and the crankshaft turns two revolutions for each power stroke.

1. Intake. The intake valve opens and the piston moves down, drawing air (and fuel, in port-injected and carbureted engines) into the cylinder.
2. Compression. Both valves close and the piston moves up, squeezing the charge. The compression ratio is the ratio of the largest cylinder volume to the smallest.
3. Power. The fuel ignites near the top of the stroke. The hot gas pushes the piston down, and the connecting rod turns the crankshaft.
4. Exhaust. The exhaust valve opens and the piston moves up, pushing the burned gas out.

A spark plug ignites the charge in a spark-ignition engine. A compression-ignition (Diesel) engine injects fuel into air that is hot from compression, and the fuel ignites on its own.

The ideal air-standard Otto cycle has four processes: isentropic compression, constant-volume heat addition, isentropic expansion, and constant-volume heat rejection. Real engines differ from this cycle because the gas has changing properties, the combustion takes time, heat escapes through the walls, and friction and pumping losses take energy.

### Main parts

- The cylinder block and head contain the combustion. The head also holds the valves and the spark plug or injector.
- The piston, piston rings, and connecting rod carry the gas force to the crankshaft.
- The crankshaft converts the reciprocating motion of the pistons into rotation.
- The camshaft and valve train open and close the valves at set crank angles.
- The fuel system delivers fuel at the pressure the injectors need. Diesel injection pressures are far higher than gasoline pressures.
- The intake and exhaust systems carry air in and gas out. The exhaust carries a catalytic converter that cleans the gas.
- The flywheel stores rotational energy and smooths the torque between power strokes.
- The cooling and lubrication systems remove heat and reduce friction at the bearings and rings.

### Variants

- Spark-ignition gasoline engines use compression ratios of about 8 to 12 in most cars. A higher ratio gives more efficiency but raises the risk of knock.
- Diesel engines use compression ratios of about 15 to 22. The high ratio makes the air hot enough to ignite the fuel, and the engine runs lean, so it is efficient at part load. The parts must be heavier to hold the higher pressures.
- Two-stroke engines produce one power stroke per revolution. They are simple and light, so they appear in chainsaws, small motorcycles, and outboard motors. Their scavenging, which clears the burned gas through ports, wastes some fresh charge and makes them harder to clean up.

## Key equations

Symbols are in SI units unless marked dimensionless.

- Displacement of one cylinder: $V_d = \dfrac{\pi}{4} B^2 S$, where $B$ is the bore in metres, $S$ is the stroke in metres, and $V_d$ is in cubic metres.
- Power from brake mean effective pressure: $P = \dfrac{p_{mep} \, V_{d,total} \, N}{c}$, where $p_{mep}$ is the brake mean effective pressure in pascals, $V_{d,total}$ is the total displacement in cubic metres, $N$ is the crankshaft speed in revolutions per second, $c = 2$ for a four-stroke engine or $c = 1$ for a two-stroke engine, and $P$ is in watts.
- Torque: $T = \dfrac{P}{2\pi N}$, with $T$ in newton metres and $P$ in watts.
- Ideal Otto efficiency: $\eta_{Otto} = 1 - r^{1-\gamma}$, where $r$ is the compression ratio (dimensionless) and $\gamma \approx 1.4$ is the ratio of specific heats for air (typical value, dimensionless).
- Ideal Diesel efficiency: $\eta_{Diesel} = 1 - \dfrac{1}{r^{\gamma-1}} \cdot \dfrac{r_c^{\gamma} - 1}{\gamma (r_c - 1)}$, where $r_c$ is the cut-off ratio (dimensionless), the ratio of cylinder volume at the end of fuel injection to the volume at its start.
- Brake thermal efficiency: $\eta_b = \dfrac{P}{\dot m_f \, LHV}$, where $\dot m_f$ is the fuel mass flow in kilograms per second and $LHV$ is the lower heating value of the fuel in joules per kilogram.

## Worked example

**Given:** A four-cylinder four-stroke engine with a bore of $B = 86\ \text{mm}$ and a stroke of $S = 86\ \text{mm}$. It runs at $N_{rpm} = 4000\ \text{rpm}$ with a brake mean effective pressure of $p_{mep} = 1.0\ \text{MPa}$. The brake thermal efficiency is $\eta_b = 0.30$, and the gasoline lower heating value is $LHV = 44\ \text{MJ/kg}$ (typical value).

**Find:** (a) the total displacement, (b) the power, (c) the torque, and (d) the fuel use in kilograms per hour.

**Solution:**

1. Displacement per cylinder: $V_d = \tfrac{\pi}{4}(0.086)^2(0.086) = 5.00 \times 10^{-4}\ \text{m}^3$. Total: $4 \times 5.00 \times 10^{-4} = 2.00 \times 10^{-3}\ \text{m}^3$, which is 1.998 L, about 2.0 L.
2. Speed: $N = 4000 / 60 = 66.7\ \text{rev/s}$.
3. Power: $P = (1.0 \times 10^{6})(1.998 \times 10^{-3})(66.7) / 2 = 6.66 \times 10^{4}\ \text{W}$, which is 66.6 kW.
4. Torque: $T = 66\,608 / (2\pi \times 66.7) = 159\ \text{N m}$.
5. Fuel flow: $\dot m_f = 66\,608 / (0.30 \times 44 \times 10^{6}) = 5.05 \times 10^{-3}\ \text{kg/s}$, which is $18.2\ \text{kg/h}$.

**Answer:** (a) 2.0 L. (b) 66.6 kW. (c) 159 N m. (d) 18.2 kg/h.

**Sanity check:** The ideal Otto efficiency at $r = 9$ is 0.585, and the real brake efficiency of 0.30 sits below it, as it must. The power formula gives watts when pressure is in pascals and displacement is in cubic metres, so the units check. The torque and power agree with $P = T\omega$.

## Design trade-offs

- Compression ratio: a higher ratio raises efficiency, but gasoline engines need fuel with a higher octane rating to avoid knock. Diesels run at higher ratios because they ignite the fuel by compression.
- Displacement and boost: a smaller engine with a turbocharger can match a larger engine's power and use less fuel at part load. Boost raises peak cylinder pressure, which needs stronger parts.
- Emissions: the flame temperature drives nitrogen oxide (NOx) formation. A gasoline engine with a three-way catalytic converter needs an air-fuel ratio near 14.7:1 by mass, which is the stoichiometric ratio for gasoline. A diesel runs lean, so it needs separate NOx treatment and a particulate filter.
- Speed: piston speed is limited, typically to about 15 to 20 m/s in road engines, by the inertia loads on the rods and bearings.
- Heat: roughly a third of the fuel energy leaves in the exhaust and about another third goes to the coolant in a typical gasoline engine (typical values). Better heat recovery and cooling designs trade cost and size against these losses.
- Noise and vibration: more cylinders run smoother, and balance shafts cancel some of the rocking forces.

## How it fails

- Knock (or detonation): the unburned end gas ignites on its own before the flame front reaches it, sending a pressure spike through the cylinder. Warning signs are a metallic pinging under load. Causes include a high compression ratio, low octane fuel, lean mixture, and a hot intake. Knock can crack pistons, so engines use knock sensors that retard the ignition timing.
- Overheating: a leak or a failed pump lets the coolant drop, and the cylinder head warps or the head gasket fails. Engines carry temperature gauges and warning lights, and the engine control unit can cut power when the temperature is too high.
- Low oil pressure: oil starvation destroys bearings within minutes. Engines carry oil-pressure warning lamps and a pump sized for the lowest expected oil level.
- Timing belt or chain failure: in an interference engine, the valves hit the pistons when the timing fails. Manufacturers set replacement intervals for this reason.
- Misfire: a bad spark plug, a clogged injector, or a weak coil leaves unburned fuel. The fuel can overheat and damage the catalytic converter.
- Safety: exhaust carries carbon monoxide, which is lethal in a closed space, so engines should not run in an enclosed garage. Fuel systems carry pressure relief and vent systems, and fuel tanks have filler and vapor controls.

## History

Nicolaus Otto and Eugen Langen built a practical four-stroke gas engine in Cologne in 1876. Rudolf Diesel patented the compression-ignition engine in 1892 in Germany, and the first working engine ran in 1897 in Augsburg. In the 1880s in Germany, Gottlieb Daimler and Wilhelm Maybach built a fast gasoline engine, which made the engine practical for road vehicles. Two-stroke engines appeared in the same era as small, simple engines.

## Practice

1. An ideal Otto cycle has a compression ratio of 10 and $\gamma = 1.4$. Find its ideal efficiency.
2. A single cylinder has a bore of 80 mm and a stroke of 90 mm. Find its displacement in cubic centimetres.
3. An engine delivers a torque of 150 N m at 3000 rpm. Find its power in kilowatts.
4. An engine delivers 50 kW at the shaft with a brake thermal efficiency of 0.25. The fuel has a lower heating value of 42.5 MJ/kg. Find the fuel use in kilograms per hour.

<details><summary>Answers</summary>

1. $\eta = 1 - 10^{-0.4} = 0.602$, or 60.2 percent.
2. $V_d = \tfrac{\pi}{4}(0.080)^2(0.090) = 4.52 \times 10^{-4}\ \text{m}^3 = 452\ \text{cm}^3$.
3. $P = T \cdot 2\pi N = 150 \times 2\pi \times 50 = 47\,124\ \text{W} = 47.1\ \text{kW}$.
4. $\dot m_f = 50\,000 / (0.25 \times 42.5 \times 10^6) = 4.71 \times 10^{-3}\ \text{kg/s} = 16.9\ \text{kg/h}$.

</details>

## Common mistakes

- Using bore and stroke in millimetres in the power formula. Convert to metres first, or the result is off by a factor of a million.
- Dropping the factor of 2 in the four-stroke power formula. Each cylinder fires once every two revolutions.
- Treating the ideal Otto or Diesel efficiency as the efficiency of a real engine. Real brake efficiency is much lower, often near 0.25 to 0.35 for road engines (typical values).
- Reading a high torque figure as high power. Power is torque times speed, so a low-speed engine can have high torque and low power.
- Assuming that a higher compression ratio always helps. It helps until knock or peak pressure limits it.

## Go deeper

- [University Physics Volume 2, section 4.2, Heat Engines](https://openstax.org/books/university-physics-volume-2/pages/4-2-heat-engines) by OpenStax: how a heat engine turns heat into work and defines its efficiency.
- [University Physics Volume 2, chapter 4 introduction, The Second Law of Thermodynamics](https://openstax.org/books/university-physics-volume-2/pages/4-introduction) by OpenStax: why no engine can convert all its heat into work.
- Related lessons: [Gas turbines and jet engines](07-gas-turbines-and-jet-engines.md), [Steam power plants](08-steam-power-plants.md), [Thermal systems](01-thermal-systems.md).
