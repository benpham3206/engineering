# Networks that connect the world

**Type:** lesson

Networks that connect the world are the shared systems that carry power, messages, people, and time across the planet. Engineers today should know them because they work inside these networks and need to know their physical limits. Each one replaced a slow or local system with a shared one that engineers could scale, and each one still depends on choices made in its first decades. This lesson covers six projects.

**Prerequisites:** [Electrical age](../06-electrical-age.md), [Semiconductors and computing](../09-semiconductors-and-computing.md), [Waves, light, and heat](../../physics/07-waves-light-heat.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md)
**Time:** 3 hours

## Core ideas

### The transatlantic telegraph cable

The problem. In the 1850s, a message between Europe and North America traveled by ship and took about ten days. Engineers wanted a wire under the Atlantic Ocean that could carry messages in minutes.

The engineering. The cable connected Valentia Island, Ireland, to Trinity Bay, Newfoundland, a route of about 3200 km. Its copper conductor sat inside gutta-percha insulation and steel armour. William Thomson, later Lord Kelvin, developed the **mirror galvanometer** that could detect faint signals and analyzed how signals slow down along a long cable. His analysis showed that the delay grows with the square of the cable length, so long cables need slow signalling or better design.

The scale. The first cable in 1858 carried a message of roughly 100 words, which took about 16 hours to send. The cable failed within about three weeks after an operator applied excessive voltage. The *Great Eastern* steamship laid a durable cable in 1866, and that cable worked reliably.

What went wrong. The 1858 failure came from an operator who used too high a voltage, which broke down the insulation. Engineers also learned that the cable's electrical behavior differed from what the early designers had assumed, and the lesson shaped later cable design.

How it changed the world. Messages crossed the Atlantic in minutes rather than weeks. Newspapers, markets, and governments began to run on near-instant communication across the ocean.

### The electric grid

The problem. Early power stations served only nearby customers. Direct current could not be stepped up to high voltage efficiently, so the power could not travel far without heavy losses.

The engineering. Alternating current solved the voltage problem because transformers change the voltage with little loss. The Adams Power Plant at Niagara Falls started in 1895 and sent power to Buffalo, New York, in 1896. The grid links generators, high-voltage transmission lines, substations, and local distribution. Each generator must match the others in frequency and phase, so the grid runs as one synchronous machine. North America uses 60 Hz, and most other regions use 50 Hz.

The scale. Large interconnected grids cover entire continents. A single grid can carry many gigawatts across thousands of kilometres.

What went wrong. On 14 August 2003, a failure in the control room of a northeast North American grid, combined with tree contacts on high-voltage lines, started a cascade. The blackout affected about 50 million people in the United States and Canada. Investigators found that an alarm software fault had hidden the problem from operators.

How it changed the world. Electric power reaches most homes, hospitals, and factories. The grid made refrigeration, electric lighting, and modern communications possible on a large scale.

### The U.S. Interstate Highway System

The problem. Before 1956, roads in the United States were built by states, with uneven standards and frequent intersections. Military planners and freight operators wanted fast, limited-access routes between cities.

The engineering. The Federal-Aid Highway Act of 1956, signed by President Dwight Eisenhower, authorized a national system of limited-access roads. The federal government paid 90 percent of the cost, and the states paid 10 percent. Designers set standards for grades, sight distance, lane width, and interchanges. Concrete and asphalt pavements were designed for heavy trucks.

The scale. The original plan called for about 41 000 miles, roughly 66 000 km. The finished system covers about 48 000 miles, roughly 77 000 km.

What went wrong. Highways were routed through many urban neighborhoods, and the route displaced residents, especially in Black communities. In Miami, Interstate 95 cut through the Overtown neighborhood. Traffic fatalities also remained high on the national road network.

How it changed the world. The system changed freight shipping, suburban growth, and the pattern of cities. Long-distance trucking and car travel depend on its design rules.

### ARPANET and the internet

The problem. In the late 1960s, the U.S. Department of Defense wanted to share costly research computers across distant sites. Circuit switching tied up a whole line for each conversation, and that approach did not suit bursty computer traffic.

The engineering. ARPANET used **packet switching**. Messages split into packets, and each packet found its own route through a network of interface message processors. The first four nodes were at UCLA, the Stanford Research Institute, UC Santa Barbara, and the University of Utah. The links ran at 50 kbit/s. The network did not start as a nuclear survivability system, though the redundancy of packet routing was an influence on early designers. In 1974, Vint Cerf and Robert Kahn published the design of the **Transmission Control Protocol**. The network switched to the TCP/IP suite on 1 January 1983.

The scale. The 1988 Morris worm infected about 6000 machines, roughly ten percent of the internet at that time. Today, more than 5 billion people use the internet.

What went wrong. The first message on 29 October 1969 attempted to send LOGIN. The system crashed after the first two letters, so the first message was LO. Early security was weak, and the Morris worm exploited known software flaws.

How it changed the world. Packet switching and open protocols became the basis of the modern internet, and the internet became the infrastructure for commerce, science, and social life.

### GPS

The problem. Navigation at sea and in the air relied on radio beacons, star sights, and dead reckoning. The U.S. Department of Defense wanted a worldwide position and timing system for military use.

The engineering. GPS uses satellites in medium Earth orbit at about 20 200 km altitude. Each satellite carries an atomic clock and broadcasts its time and position. A receiver measures the travel time from at least four satellites. It solves for three position coordinates and its own clock error. The orbit period is about 11 hours 58 minutes, half a sidereal day.

The scale. The first satellite launched in February 1978. Full operational capability was declared in April 1995. The nominal constellation is 24 satellites, and the system now has more than 30 in orbit as spares and replacements.

What went wrong. On 22 August 1999, the first GPS week-number rollover caused some receivers to show dates a thousand weeks off. Selective availability, which degraded civilian accuracy, was turned off on 1 May 2000. GPS signals remain open to jamming and spoofing, which are serious threats near conflict zones.

How it changed the world. Civilian positioning and precise timing now support aviation, shipping, mapping, banking time stamps, and power-grid synchronization. Phones use GPS for navigation and ride-sharing.

### Undersea fiber-optic cables

The problem. Copper cables carried only a limited number of telephone calls and lost signal over long distances. Engineers needed a medium with far more bandwidth and lower loss.

The engineering. Light travels through a glass fiber by **total internal reflection**, which confines the light to the core. Silica fiber has a refractive index near 1.47, so light moves at about $2.04 \times 10^8\ \mathrm{m/s}$ inside it. **Erbium-doped fiber amplifiers** boost the light without converting it to electricity, which made long undersea spans practical. The first transatlantic fiber cable, TAT-8, opened in 1988.

The scale. TAT-8 carried tens of thousands of telephone circuits. Today, the global network of undersea cables exceeds 1 million km in length, and it carries most intercontinental internet traffic.

What went wrong. Ship anchors and fishing gear cut cables, and earthquakes damage cables on the seabed. Repairs require specialized ships and can take weeks.

How it changed the world. Undersea fiber carries the bulk of international data. Financial transactions, cloud services, and cross-border communication all depend on these cables.

## Key inventions

| Years | Project | Place | What it changed |
|---|---|---|---|
| 1858 to 1866 | Transatlantic telegraph cable | Ireland to Newfoundland | Messages crossed the Atlantic in minutes instead of weeks |
| 1882 to 1896 | Electric grid | New York City; Niagara Falls | Alternating current carried power over long distances |
| 1956 onward | Interstate Highway System | United States | Limited-access national road network for freight and travel |
| 1969 to 1983 | ARPANET and the internet | United States | Packet switching and the TCP/IP protocol suite |
| 1978 to 1995 | GPS | Global, from orbit | Worldwide positioning and precise timing |
| 1988 to present | Undersea fiber cables | Atlantic, Pacific, and global routes | Bulk international data and internet backbone |

## Key equations

Propagation delay in a medium. The one-way time for a signal over a path is

$$t = \frac{L}{v}, \qquad v = \frac{c}{n}$$

where $t$ is the delay in seconds, $L$ is the path length in metres, $v$ is the signal speed in metres per second, $c = 2.998 \times 10^8$ m/s is the speed of light in vacuum, and $n$ is the **refractive index** of the medium, which is dimensionless. The equation assumes a uniform medium, a straight path, and no processing delay. For silica fiber, $n \approx 1.47$.

Range from timing error. A receiver that measures a travel time with error $\Delta t$ places the satellite at a distance error of

$$\Delta d = c\,\Delta t$$

where $\Delta d$ is the range error in metres and $\Delta t$ is the timing error in seconds. The equation assumes the signal travels at $c$ in vacuum along the line of sight, and it ignores the geometry that scales the effect into position error.

Resistive power loss on a line. For a three-phase line carrying power $P$ at line voltage $V$ and power factor $\text{pf}$, the line current is

$$I = \frac{P}{\sqrt{3}\, V\, \text{pf}}$$

and the resistive loss is $P_{\text{loss}} = I^2 R$, where $R$ is the line resistance in ohms. The equation assumes balanced loads, a constant power factor, and a fixed resistance. Raising the voltage tenfold cuts the current tenfold and the loss a hundredfold.

Interstate distance conversion. Converting a length from miles to kilometres uses $1\ \text{mile} = 1.609344$ km exactly. This is a unit conversion and needs no assumptions beyond that definition.

## Worked example

**Given:** A GPS receiver's clock is off by 10 ns. The receiver is at a location where the satellite geometry gives a geometric dilution of one. The orbit of each satellite has a clock that would drift by about 38 microseconds per day relative to the ground clock if the relativistic effects were left uncorrected.

**Find:** (a) the range error caused by the 10 ns timing error, and (b) the range error that accumulates in one day if the satellite clock drift is left uncorrected.

**Assumptions:**
1. The signal travels at $c = 2.998 \times 10^8$ m/s through vacuum along the line of sight.
2. The timing error is the full error on the measured travel time.
3. Geometric dilution is one, so the range error equals the time error times $c$.
4. The clock drift is constant over one day.

**Solution:**

1. Range error for part (a): $\Delta d = c\,\Delta t = (2.998\times10^8)(10\times10^{-9}) = 2.998$ m.
2. Range error for part (b): the drift of 38 microseconds is already the offset after one day, so $\Delta t = 38\times10^{-6}$ s. Then $\Delta d = (2.998\times10^8)(38\times10^{-6}) = 1.14\times10^4$ m.

**Answer:** (a) A 10 ns timing error gives a range error of about 3.0 m. (b) An uncorrected relativistic drift of about 38 microseconds per day gives a range error of about 11.4 km after one day.

**Sanity check:** A 1 microsecond error maps to about 300 m, so a clock that drifts by tens of microseconds per day would wreck navigation in hours without correction. Engineers therefore correct the satellite clocks and feed the correction into the broadcast message. The 38 microsecond figure is the commonly quoted net value, and the rate is close enough to use for this estimate.

## Design trade-offs

Grid engineers trade voltage against insulation and equipment cost. Higher voltage lowers current and loss, but transformers, insulators, and clearances cost more and grow in size.

Cable designers trade bandwidth against repeater spacing and cost. A long fiber span needs amplifiers at intervals, and each amplifier must survive decades on the seabed.

Highway designers trade grade and curvature against cost and land use. Gentle grades save fuel and time for trucks but require more earthwork and more land.

GPS designers trade satellite count against coverage and cost. Each satellite carries an atomic clock, which costs far more than a quartz oscillator, because the navigation solution depends on clock accuracy.

## How it fails

Cables fail from anchors, fishing gear, and earthquakes. Operators reroute traffic, and repairs take weeks. Physical protection, burial, and route planning reduce the risk.

Power grids fail in cascades. A single line trip can overload its neighbors. Protection relays, load shedding, and better operator alarms limit how far a failure spreads.

Satellite navigation fails from jamming, spoofing, and receiver software faults such as the 1999 week-number rollover. Receivers now check the broadcast data against independent sources, and some systems use multiple frequencies to resist interference.

Packet networks fail from software bugs, worms, and misconfigured routers. Security standards, patching, and routing filters address the most common causes.

## History

The networks in this lesson came from separate efforts across more than a century. The telegraph cable, the grid, and the highway each arose from a need for distance or speed, and each one needed standards for shared equipment. The packet network and GPS arose from defense research, and the fiber cable built on physics from the twentieth century. Their histories overlap in the people and institutions that designed them.

## Lessons for engineers today

Networks are shared assets, so their designs must handle failure at every point. The 2003 blackout and the 1988 worm both showed that one fault can spread when the system has no firewall or no independent check.

Physical limits set the budget. Signal speed in fiber, timing precision in GPS, and resistive loss in lines are fixed by physics. Engineers who know these limits can predict performance before they build.

Standards matter more than the first design. The TCP/IP switchover and the GPS interface document both let independent makers build compatible equipment.

## Practice

1. A GPS receiver has a timing error of 1 microsecond. Find the range error.
2. A fiber link runs 1000 km with silica fiber of refractive index $n = 1.47$. Find the one-way delay.
3. A 1 GW load at power factor 0.95 is served by a three-phase line with resistance 1 ohm per conductor. Compare the loss at 110 kV and at 1100 kV.
4. An ARPANET packet of 1000 bytes crosses four links at 50 kbit/s each. Ignore propagation and processing delay and find the total transmission time under store-and-forward.
5. Short answer. A highway designer records a route of 41 000 miles. Convert that to kilometres using $1\ \text{mile} = 1.609344$ km.

<details><summary>Answers</summary>

1. $\Delta d = c\,\Delta t = 2.998\times10^8 \times 1\times10^{-6} = 300$ m. The calculation assumes line-of-sight travel at $c$ in vacuum.
2. $v = c/n = 2.04\times10^8$ m/s, so $t = 1\times10^6 / 2.04\times10^8 = 4.90$ ms. The calculation assumes a straight, uniform fiber with no repeater delay.
3. At 110 kV, $I = 10^9 / (\sqrt{3}\times 1.1\times10^5 \times 0.95) = 5525$ A and $P_{\text{loss}} = 3 I^2 R = 9.16\times10^7$ W, about 91.6 MW across the three conductors. At 1100 kV, the current is 552 A and the loss is about 0.916 MW. The loss falls by a factor of 100. The calculation assumes constant load, constant power factor, and fixed resistance.
4. Each hop takes $8000 / 50\,000 = 0.16$ s, so four hops take 0.64 s. The calculation assumes each node waits for the full packet before forwarding it.
5. $41\,000 \times 1.609344 = 65\,983$ km, about 66 000 km. The conversion is exact by definition.

</details>

## Common mistakes

Confusing bits and bytes. A network rated at 50 kbit/s moves 6.25 kB per second, not 50 kB per second.

Believing GPS needs only one satellite. A receiver needs four satellites to solve three position coordinates and its own clock error.

Saying the ARPANET was built to survive nuclear war. Packet switching drew on distributed-network ideas, but the ARPANET's purpose was to share research computers.

Assuming the internet and the World Wide Web are the same system. The web runs on top of the internet, and it began in 1989 as a separate project.

## Go deeper

[OpenStax, *University Physics Volume 3*](https://openstax.org/books/university-physics-volume-3/pages/1-introduction) covers optics, including total internal reflection, which guides light in fiber.

[NIST, Time and Frequency Division](https://www.nist.gov/pml/time-and-frequency-division) maintains the U.S. standard for frequency and time, and it links to GPS time transfer services.

Related reading in this repo: [Electrical age](../06-electrical-age.md), [Semiconductors and computing](../09-semiconductors-and-computing.md), [Electromagnetic fields, waves, and space reference](../../physics/reference-fields-waves-space.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [The power grid](../../applications/electrical/08-the-power-grid.md), [Fiber optics](../../applications/waves-and-communication/04-fiber-optics.md), [GPS](../../applications/waves-and-communication/08-gps.md), [Applications reference](../../applications/reference.md), and [History reference](../reference.md).
