# War, nuclear, and space

**Type:** lesson

Between about 1935 and 1957, radar, jet engines, nuclear reactors, rockets, and electronic computers moved from research into working machines, driven largely by war and the cold war that followed. Many of today's power plants, aircraft, satellites, and computers still rely on the physics, design methods, and safety rules these programs created.

**Prerequisites:** [Electrical age](06-electrical-age.md), [Flight, cars, and mass production](07-flight-cars-and-mass-production.md), [Waves, light, and heat](../physics/07-waves-light-heat.md), [Thermodynamics II](../physics/09-thermo-second-law-cycles.md), [Orbital mechanics and rockets](../physics/15-orbital-mechanics-and-rockets.md)
**Time:** 3-4 h

## Core ideas

### Radar

Radar sends radio waves and listens for their echoes. The time delay of an echo gives range, and the direction of the antenna gives bearing. In February 1935, Robert Watson-Watt and Arnold Wilkins showed at Daventry, England, that radio waves reflected from an aircraft could be detected. Britain then built a chain of coastal radar stations, known as Chain Home, before the war.

Good radar needs short wavelengths. Short wavelengths allow small antennas that make sharp beams, but early transmitters could not make much power at those wavelengths. In 1940, John Randall and Harry Boot at Birmingham University built the cavity magnetron, which produced high power at centimetre wavelengths. That made radar small enough for aircraft and ships. The Massachusetts Institute of Technology's Radiation Laboratory, set up in 1940, developed radar systems on top of the magnetron. Germany and the United States also developed radar, largely in parallel with Britain.

### Jet engines

A jet engine is a gas turbine that makes thrust from its exhaust. It compresses air, mixes in fuel and burns it, and expands the hot gas through a turbine. The turbine drives the compressor, and the fast exhaust leaves the nozzle as thrust. Frank Whittle patented a jet engine design in Britain in 1930, and his first engine ran in April 1937. Hans von Ohain, working for Heinkel in Germany, flew the He 178 on 27 August 1939, which was the first jet-powered flight. A Whittle engine powered the Gloster E.28/39 in 1941. The Messerschmitt Me 262 entered service with the German air force in 1944.

### Nuclear power

On 2 December 1942, Enrico Fermi and a team at the University of Chicago started Chicago Pile-1. It was the first self-sustaining nuclear chain reaction. The pile made almost no power, and control rods kept it at a low, safe output. Reactors then moved toward producing electricity. The Obninsk reactor in the Soviet Union sent electricity to a grid in 1954. In 1957, the Shippingport station in Pennsylvania began producing power as one of the first full-size pressurized water reactors in the United States.

A reactor must control its chain reaction, remove its heat, and contain its radioactive material. These three tasks still set the basic design of every commercial reactor.

### Rockets

Konstantin Tsiolkovsky published the rocket equation in 1903. Robert Goddard launched the first liquid-fuel rocket on 16 March 1926 in Auburn, Massachusetts. In Germany, the V-2 rocket was developed at Peenemunde by a team led by Wernher von Braun. It entered use in 1944 as the first long-range ballistic missile. After the war, the Soviet Union used its R-7 rocket to launch Sputnik 1 on 4 October 1957, the first artificial satellite. Yuri Gagarin flew Vostok 1 on 12 April 1961, the first human spaceflight.

The Saturn V was designed under von Braun at the Marshall Space Flight Center in Huntsville, Alabama. It flew for the first time in November 1967. It had three stages and carried the Apollo spacecraft. Apollo 11 landed on the Moon on 20 July 1969.

### Early computers

Konrad Zuse completed the Z3 in Berlin in 1941. It was a programmable computer built from electromechanical relays, and it worked in binary. At Bletchley Park in Britain, the Colossus machines from 1943 helped break German teleprinter codes. ENIAC, built by J. Presper Eckert and John Mauchly at the University of Pennsylvania, was completed in 1945. The Harvard Mark I, built with IBM and led by Howard Aiken, began operation in 1944. These machines used thousands of electrical parts and needed large teams to program and maintain them.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| 1903 | Rocket equation | Konstantin Tsiolkovsky, Russia | Gave the basic physics of how much speed a rocket can gain from its propellant. |
| 1926 | First liquid-fuel rocket | Robert Goddard, Auburn, Massachusetts | Showed that liquid propellants could drive a rocket. |
| 1935 | Radar detection of an aircraft | Robert Watson-Watt and Arnold Wilkins, Daventry, England | Showed that radio echoes could find aircraft at long range. |
| 1939 | First jet-powered flight, He 178 | Hans von Ohain, Heinkel, Germany | Proved that a jet engine could fly an aircraft. |
| 1940 | Cavity magnetron | John Randall and Harry Boot, Birmingham, England | Made high-power, short-wavelength radar small enough for aircraft and ships. |
| 1941 | Z3 programmable computer | Konrad Zuse, Berlin | An early working programmable digital computer. |
| 1942 | Chicago Pile-1 | Enrico Fermi and team, University of Chicago | First self-sustaining nuclear chain reaction. |
| 1944 | V-2 rocket in use | Peenemunde, Germany, under Wernher von Braun's team | The first long-range ballistic missile. |
| 1945 | ENIAC completed | J. Presper Eckert and John Mauchly, University of Pennsylvania | An early large electronic general-purpose computer. |
| 1954 | Nuclear power on an electric grid | Obninsk, Soviet Union | Showed that a reactor could supply electricity to a grid. |
| 1957 | Sputnik 1 | Soviet Union, R-7 rocket | The first artificial satellite. |
| 1969 | Apollo 11 lunar landing | NASA, Saturn V launch vehicle | The first crewed landing on the Moon. |

## Key equations

The rocket equation gives the ideal speed change a rocket can achieve:

$$\Delta v = v_e \ln\frac{m_0}{m_f}$$

Here $\Delta v$ is the speed change in metres per second (m/s), $v_e$ is the effective exhaust speed in m/s, $m_0$ is the starting mass in kilograms (kg), and $m_f$ is the mass after the propellant burns, in kg. The exhaust speed is $v_e = I_{sp} g_0$, where $I_{sp}$ is specific impulse in seconds (s) and $g_0 = 9.81\ \text{m/s}^2$. The equation ignores gravity and drag, so it gives an upper limit.

The radar range equation gives the maximum range of a radar that detects a target at a given power:

$$R_{\max} = \left[\frac{P_t\, G^2\, \lambda^2\, \sigma}{(4\pi)^3\, P_{\min}}\right]^{1/4}$$

Here $R_{\max}$ is the maximum range in metres (m), $P_t$ is transmitted power in watts (W), $G$ is antenna gain (no units), $\lambda$ is wavelength in m, $\sigma$ is the target's radar cross section in square metres (m$^2$), and $P_{\min}$ is the smallest echo power the receiver can detect, in W. Range grows with the fourth root of power, so the radar must gain 16 times the power to double its range.

## Worked example

The Saturn V weighed about 2 970 t at liftoff, a commonly cited figure. Assume the first stage ends its burn at 800 t, a rounded figure chosen for this example and not a published value. Assume the first stage has a sea-level specific impulse of 263 s, close to the typical figure for its F-1 engines. Find the ideal speed change of the first stage.

The exhaust speed is $v_e = 263 \times 9.81 = 2580\ \text{m/s}$. The mass ratio is $m_0 / m_f = 2970 / 800 = 3.71$. The rocket equation gives

$$\Delta v = 2580 \times \ln(3.71) = 2580 \times 1.312 = 3384\ \text{m/s}$$

The ideal speed change is about 3.4 km/s. The real stage reaches less, because gravity and drag take part of its speed.

Check the liftoff thrust. The five F-1 engines together produced about 7.5 million lbf, or about 33.4 MN. The weight is $2.97 \times 10^6 \times 9.81 = 29.1\ \text{MN}$. The thrust-to-weight ratio is $33.4 / 29.1 = 1.15$, so the vehicle lifted off. The check passes.

Now try the same rocket with one stage. Orbit needs a speed change of about 9.4 km/s from the ground, including losses. With $v_e = 2580$ m/s, the mass ratio must satisfy $\ln(m_0/m_f) = 9400 / 2580 = 3.64$, so $m_0 / m_f = 38$. That would leave 97 percent of the starting mass as propellant, which no structure can carry. The answer is that rockets need stages. Each stage gives a smaller mass ratio, and the speed changes add.

## Lessons for engineers today

Wartime deadlines bought engineering effort. Radar, jets, reactors, and rockets each had a clear target and a large budget, and the tight schedules forced design choices that still shape the field.

The rocket equation is still the first check on any launch vehicle. Before running a detailed simulation, an engineer checks the mass ratio and specific impulse against the target speed change.

Safety rules came from failures. Early reactors, rockets, and aircraft taught engineers to design redundancy, containment, and tests that catch faults on the ground. Those practices carry into every modern program.

Computing grew from wartime problems. Ballistic tables, code breaking, and nuclear design needed fast calculation, and those needs helped drive early computer development. Today's engineers use the same kind of machine to run simulations.

## Practice

1. A rocket stage has $I_{sp} = 300$ s and a mass ratio of 4. Find its ideal speed change in m/s.
2. A radar increases its transmitted power by a factor of 16, and nothing else changes. By what factor does its maximum range change?
3. Short answer: why did the cavity magnetron matter for radar?
4. Using $\Delta v = 9.4$ km/s and $I_{sp} = 263$ s, find the mass ratio that a single-stage rocket to orbit would need. Use $g_0 = 9.81\ \text{m/s}^2$.
5. Short answer: name two design tasks every nuclear reactor must handle to stay safe.

<details><summary>Answers</summary>

1. $\Delta v = 300 \times 9.81 \times \ln 4 = 4080\ \text{m/s}$, about 4.1 km/s.
2. The range scales as $R \propto P_t^{1/4}$. A factor of $16^{1/4} = 2$, so the range doubles.
3. The magnetron produced high power at short wavelengths. Short wavelengths make small antennas that form sharp beams, which suits aircraft and ships.
4. $m_0/m_f = e^{\Delta v / v_e}$ with $v_e = 263 \times 9.81 = 2580\ \text{m/s}$. Then $e^{9400/2580} = e^{3.64} = 38$.
5. A reactor must control its chain reaction, remove its heat, and contain its radioactive material.

</details>

## Common mistakes

- Radar was invented in one country. Britain, Germany, and the United States developed it at about the same time.
- Frank Whittle invented the jet and Hans von Ohain only copied it. Both designed working jet engines independently, and von Ohain's He 178 made the first jet-powered flight in 1939.
- Chicago Pile-1 produced electricity. It produced almost no power and ran at a very low output.
- Rockets and jet engines work the same way. A jet engine takes oxygen from the air, while a rocket carries its own oxidizer and works in a vacuum.
- Apollo's launch vehicle was one big rocket. The Saturn V had three stages.

## Go deeper

- [NASA History, NASA](https://www.nasa.gov/history/). Histories of the space program, including Apollo.
- [National Air and Space Museum, Smithsonian](https://airandspace.si.edu/). Collections on aircraft, jet engines, and rockets.
- [MIT OpenCourseWare](https://ocw.mit.edu/). Free course materials from MIT, including classical mechanics and related engineering courses.
- Related lessons: [Radar and sonar](../applications/waves-and-communication/07-radar-and-sonar.md), [Nuclear reactors](../applications/energy/04-nuclear-reactors.md), [Gas turbines and jet engines](../applications/thermal-fluid/07-gas-turbines-and-jet-engines.md), [Rockets](../applications/vehicles-aerospace/07-rockets.md), [Digital logic and computers](../applications/electronics/07-digital-logic-and-computers.md), and [Lesson 09, semiconductors and computing](09-semiconductors-and-computing.md).
