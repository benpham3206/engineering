# Flight, cars, and mass production

**Type:** lesson

**Flight, cars, and mass production** is the story of how the internal combustion engine, the airplane, and the production line moved from workshops into daily life between about 1876 and about 1914. Engineers still design every vehicle around the trade-offs these inventors first faced: power against weight, efficiency against cost, and a design that can be built many times over.

**Prerequisites:** [Industrial revolution](05-industrial-revolution.md), [Electrical age](06-electrical-age.md), [Thermodynamics II](../physics/09-thermo-second-law-cycles.md), [Hydrostatics and Bernoulli](../physics/10-hydrostatics-and-bernoulli.md)
**Time:** 2-3 h

## Core ideas

### The engine

Before 1880, most engines were steam engines or early gas engines. Steam engines were large and slow to start, and early gas engines wasted much of their fuel. Nicolaus Otto built a **four-stroke engine** at Deutz, near Cologne, in 1876. Its cycle has four strokes: intake, compression, power, and exhaust. The engine fires once every two turns of the crankshaft, and the same four-stroke pattern still runs in most car engines.

In 1885, Gottlieb Daimler and Wilhelm Maybach fitted a small, fast engine to a wooden frame at Cannstatt, near Stuttgart. The machine was a motorcycle-like device, and it showed that a light engine could drive a vehicle. In 1886, Karl Benz patented a three-wheeled car in Mannheim. It was one of the first vehicles designed as a complete car, not a carriage with an engine added later.

Rudolf Diesel took a different route. A **diesel engine** compresses air so hard that it heats above the fuel's ignition point, so the fuel lights without a spark plug. The first working diesel engine ran in 1897 at Augsburg. Diesel engines run hotter and more efficiently than petrol engines, which made them useful for trucks, ships, and later for trains.

### The airplane

Orville and Wilbur Wright ran a bicycle business in Dayton, Ohio. Earlier gliders had flown, and some powered flights had left the ground, but none had been controlled reliably in all three axes. The Wrights solved control with three parts: wing warping for roll, a forward elevator for pitch, and a rudder for yaw. They also saw that the lift tables published by earlier researchers were not reliable enough for design. In 1901, they built a wind tunnel and tested about 200 wing shapes.

Their 1903 *Flyer* had a four-cylinder engine of about 12 horsepower, built with their mechanic Charlie Taylor. On 17 December 1903, at Kitty Hawk, North Carolina, the *Flyer* flew for 12 seconds and covered 36.6 m (120 ft). The longest flight that day lasted 59 seconds and covered about 260 m (852 ft). It was the first powered, controlled, sustained flight by a heavier-than-air machine with a pilot.

### The assembly line

Early cars were built by small teams of craftsmen working at one bench. Each car cost a lot, and few people could buy one. Henry Ford's Model T appeared in 1908. In 1913, the Ford plant at Highland Park, Michigan, began building cars on a **moving line**. Each worker repeated one task while the car moved past, and the work was faster than building a car at a fixed bench. Ford drew on earlier ideas, including the disassembly lines of meatpacking plants. Model T production ran from 1908 to 1927, with about 15 million cars built.

In 1911, Frederick Winslow Taylor published *The Principles of Scientific Management*. He argued that managers should time each task and set one standard method for it. Engineers used this kind of time study to plan the line and to balance the work at each station.

### Standards

A moving line only works when every part fits every car. **Interchangeable parts**, which the nineteenth century had developed, made this possible. Later, engineering societies wrote the sizes, threads, and test methods down as shared standards. The Society of Automobile Engineers was founded in 1905. The International Organization for Standardization was founded in Geneva in 1947. Standards let many suppliers make parts that fit one design.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| 1876 | Four-stroke engine | Nicolaus Otto, Deutz, Germany | Gave a practical, efficient engine that most car engines still follow. |
| 1885 | Light gasoline-engined motorcycle (*Reitwagen*) | Gottlieb Daimler and Wilhelm Maybach, Cannstatt, Germany | Showed that a small, fast engine could drive a vehicle. |
| 1886 | Patented three-wheeled car (Motorwagen) | Karl Benz, Mannheim, Germany | An early design for a complete car, not just an engine. |
| 1897 | First working diesel engine | Rudolf Diesel, Augsburg, Germany | Compression ignition gave high efficiency without a spark. |
| 1903 | Powered, controlled, sustained flight | Orville and Wilbur Wright, Kitty Hawk, North Carolina | Showed that control in all three axes was the key problem of flight. |
| 1908 | Model T | Henry Ford, Detroit, Michigan | Made a reliable car cheap enough for ordinary buyers. |
| 1911 | *The Principles of Scientific Management* | Frederick Winslow Taylor, United States | Made task timing and standard methods a core tool of production planning. |
| 1913 | Moving assembly line for Model T | Ford Motor Company, Highland Park, Michigan | Cut the labor per car and made high volume possible. |
| 1947 | International Organization for Standardization founded | Geneva, Switzerland | Set shared standards for parts and tests across countries. |

## Key equations

The lift equation gives the lift force on a wing in steady flight:

$$L = \tfrac{1}{2}\,\rho\, v^2\, S\, C_L$$

Here $L$ is lift in newtons (N), $\rho$ is air density in kilograms per cubic metre (kg/m$^3$), $v$ is airspeed in metres per second (m/s), $S$ is wing area in square metres (m$^2$), and $C_L$ is the **lift coefficient**, which has no units. Standard sea-level air on Earth at 15 °C has $\rho \approx 1.225\ \text{kg/m}^3$ (typical value).

The **ideal Otto cycle** gives an upper limit on engine efficiency:

$$\eta = 1 - r^{\,1-\gamma}$$

Here $\eta$ is efficiency (no units), $r$ is the compression ratio (no units), and $\gamma$ is the ratio of specific heats, about 1.4 for air (typical value). Real engines fall below this limit because of friction, heat loss, and incomplete burning.

## Worked example

The *Wright Flyer* of 1903 weighed about 340 kg with the pilot. This is a rounded figure used here. Its wing area was about 47 m$^2$. Take a steady, level flight at an airspeed of 13 m/s, about 30 mph, with sea-level air at $\rho = 1.225\ \text{kg/m}^3$. Find the lift coefficient the wing must reach.

The assumptions are these. Lift balances weight in steady, level flight. One lift coefficient applies across the whole wing. Thrust and drag do not enter the lift balance, and the air is still. Gravity is Earth's surface value, $g = 9.81\ \text{m/s}^2$.

The weight is $W = mg = 340 \times 9.81 = 3335\ \text{N}$. Setting $L = W$ and solving the lift equation for $C_L$ gives

$$C_L = \frac{2W}{\rho v^2 S} = \frac{2 \times 3335}{1.225 \times 13^2 \times 47} = 0.69$$

The answer is $C_L \approx 0.69$, with no units. At 10 m/s, the same wing would need $C_L \approx 1.16$. At 15 m/s, it would need $C_L \approx 0.52$.

Slow flight demands a high lift coefficient, which is why stall at low speed is the main danger for a light aircraft.

For a sanity check, a lift coefficient of 0.5 at 13 m/s gives $L = 0.5 \times \tfrac{1}{2} \times 1.225 \times 13^2 \times 47 = 2430\ \text{N}$. That is less than the 3335 N weight, so a wing with $C_L = 0.5$ could not carry the *Flyer* at that speed. A value near 0.7 is a plausible figure for a cambered wing at a moderate angle of attack. It explains why the Wrights tested so many wing shapes.

## Lessons for engineers today

Test the shape before you commit to it. The Wrights built a wind tunnel and measured their own lift data instead of trusting published tables. Engineers still use wind tunnels and computational fluid dynamics the same way.

Control matters as much as power. The *Flyer*'s engine was modest, but its three-axis control made it fly. Modern aircraft design still starts with stability and control, then sizes the engine.

Design the product for the factory. The Model T line worked because the car was built around standard parts and simple repeated tasks. A product that is hard to build in volume will be expensive, whatever its design merits.

Standards turn one shop's parts into a supply chain. A part that matches a written standard can come from any supplier who meets it.

## Practice

1. Compute the ideal Otto efficiency for a compression ratio of 10, using $\gamma = 1.4$.
2. The *Flyer*'s wing needs $C_L = 0.686$ at 13 m/s. If the speed rises to 15 m/s with the same mass and wing area, what lift coefficient is needed?
3. The first flight of 1903 covered 36.6 m in 12 s. Find the average speed in metres per second and in kilometres per hour.
4. Short answer: at fixed weight and fixed $C_L$, why does a larger wing area lower the speed needed to fly?
5. Short answer: name two gains and two costs of the moving assembly line.

<details><summary>Answers</summary>

1. $\eta = 1 - 10^{-0.4} = 0.602$, about 60 percent. Real engines run lower.
2. $C_L = 0.52$. The lift coefficient scales with $1/v^2$, so $0.686 \times (13/15)^2 = 0.515$.
3. $36.6 / 12 = 3.05\ \text{m/s}$, which is $3.05 \times 3.6 = 11.0\ \text{km/h}$.
4. Lift is $L = \tfrac{1}{2}\rho v^2 S C_L$. At fixed weight and fixed $C_L$, the lift must stay constant, so $v^2 S$ must stay constant. A larger $S$ therefore allows a lower $v$, in proportion to $1/\sqrt{S}$.
5. Gains: lower cost per car and high output. Costs: a fixed design that is hard to change, a whole line that stops when one station fails, and repetitive work for each person on the line.

</details>

## Common mistakes

- Henry Ford invented the car. Benz and Daimler built the first practical cars. Ford made a cheap car that many people could buy.
- The Wright brothers' 1903 flight was a long flight. The first flight lasted 12 seconds, and the longest flight that day lasted 59 seconds.
- Ford invented the assembly line from nothing. Ford borrowed ideas from the disassembly lines of meatpacking plants.
- The Otto efficiency is what a real engine achieves. It is an ideal upper limit, and real engines reach less.
- Lift depends only on speed. The lift equation also needs air density, wing area, and the lift coefficient.

## Go deeper

- [*The Principles of Scientific Management*, Frederick Winslow Taylor, Project Gutenberg](https://www.gutenberg.org/ebooks/6435). Taylor's 1911 book, free to read online.
- [Wright Brothers National Memorial, National Park Service](https://www.nps.gov/wrbr/). Historical material on the 1903 flights from a U.S. federal agency.
- [National Air and Space Museum, Smithsonian](https://airandspace.si.edu/). Aviation and spaceflight collections.
- Related lessons: [Aircraft and wings](../applications/vehicles-aerospace/05-aircraft-and-wings.md), [Internal combustion engines](../applications/thermal-fluid/06-internal-combustion-engines.md), [Cars](../applications/vehicles-aerospace/02-cars.md), and [Lesson 08, war, nuclear, and space](08-war-nuclear-and-space.md).
- [History of engineering reference](reference.md): the lookup sheet for this topic.
