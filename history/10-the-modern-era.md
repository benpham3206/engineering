# The modern era

**Type:** lesson

From about 1970 onward, engineers gained tools that changed how they design, test, and build: computer simulation, satellite navigation, networked data, additive manufacturing, and modern batteries and solar cells. These tools form the working environment of engineers today, and each one brings a new way to fail, such as trusting a precise-looking simulation.

**Prerequisites:** [Semiconductors and computing](09-semiconductors-and-computing.md), [War, nuclear, and space](08-war-nuclear-and-space.md), [Principles that last](../philosophy/07-principles-that-last.md)
**Time:** 3-4 h

## Core ideas

### Computer-aided design and simulation

In 1963, Ivan Sutherland showed Sketchpad at MIT. A user drew lines and shapes on a screen with a light pen, and the computer stored them as objects that could be copied and changed. Sketchpad was the ancestor of computer-aided design, which replaced the drafting table with a model that could be measured, shared, and revised.

Analysis followed the drawing. In 1956, M. J. Turner and his colleagues at Boeing published a matrix method for the stiffness of aircraft structures. Ray Clough named the approach finite element analysis in 1960. The method cuts a structure into small pieces, writes a force-displacement relation for each one, and solves the combined set with a computer. Problems too large for hand calculation became routine. The answer is only as good as the model, though, and a model with the wrong boundary conditions gives a clean-looking wrong answer.

### Networks and the internet

The first ARPANET link carried a message between the University of California, Los Angeles and the Stanford Research Institute in October 1969. The network used packet switching, which splits data into small blocks that can take different routes. In 1983, ARPANET switched to the TCP/IP protocols designed by Vint Cerf and Bob Kahn. That common protocol became the base of the internet.

The World Wide Web is a separate layer that runs on the internet. Tim Berners-Lee proposed it at CERN in Geneva in 1989, and a working web was public by 1991. For engineers, the network changed daily work. Test data, design files, standards, and firmware now move between sites in seconds, and a team on three continents can review the same model.

### Satellite navigation

The Global Positioning System is a United States satellite system. The first satellite launched in 1978, and the system was declared fully operational in 1995. A receiver finds its position by timing signals from several satellites. Each signal gives a distance, and the receiver solves for three position coordinates and its own clock error, so it needs signals from four satellites.

GPS depends on relativity. Clocks in orbit run faster than clocks on the ground by about 38 microseconds per day. Without a correction, the position error would grow by kilometres each day. Engineers who design timing systems now treat relativity as a normal input, not as a curiosity.

### Additive manufacturing

In 1986, Chuck Hull patented stereolithography, a process that cures a liquid resin layer by layer with ultraviolet light. Hull also co-founded 3D Systems. Additive manufacturing builds a part from thin layers, so it can make shapes that a cutter cannot reach. Its limits are speed, surface finish, and the strength of the layer bonds, and those limits decide which parts it should make.

### Batteries and solar cells

Bell Labs built a silicon solar cell in 1954 with an efficiency of about 6 percent. Solar cells improved steadily after that, and they are now a common source of electricity. Batteries followed a similar path. In 2019, the Nobel Prize in Chemistry went to John Goodenough, M. Stanley Whittingham, and Akira Yoshino for the lithium-ion battery, which stores the energy in phones, laptops, and electric vehicles.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| 1963 | Sketchpad | Ivan Sutherland, MIT | Interactive drawing on a computer, the ancestor of computer-aided design |
| 1956 | Matrix stiffness method for aircraft structures | M. J. Turner and colleagues, Boeing | Made structural analysis too large for hand calculation practical |
| 1969 | First ARPANET link | UCLA and Stanford Research Institute | Packet-switched network, the start of the internet |
| 1978 | First GPS satellite launched | United States Department of Defense | Began satellite navigation, fully operational in 1995 |
| 1983 | TCP/IP adopted on ARPANET | Vint Cerf and Bob Kahn | A common protocol that became the base of the internet |
| 1986 | Stereolithography patent | Chuck Hull, 3D Systems | An early commercial 3D printing process |
| 1989 | World Wide Web proposal | Tim Berners-Lee, CERN, Geneva | Linked documents shared across the internet |

## Key equations

A GPS receiver measures the distance to each satellite $i$ with the range equation:

$$\rho_i = \sqrt{(x - x_i)^2 + (y - y_i)^2 + (z - z_i)^2} + c\,\delta t$$

Here $\rho_i$ is the measured pseudorange in metres, $(x, y, z)$ is the receiver position in metres, $(x_i, y_i, z_i)$ is the satellite position in metres, $c = 2.998 \times 10^{8}$ m/s is the speed of light, and $\delta t$ is the receiver clock error in seconds. The four unknowns are $x$, $y$, $z$, and $\delta t$, so four satellites give four equations.

A structural finite element model reduces to a linear system:

$$K u = f$$

Here $K$ is the stiffness matrix in newtons per metre, $u$ is the displacement vector in metres, and $f$ is the force vector in newtons.

## Worked example

**Given:** A GPS satellite clock runs about $38\ \mu\text{s}$ per day faster than a ground clock because of relativity. The speed of light is $c = 2.998 \times 10^8$ m/s.

**Find:** The position error that would build up in one day if no correction were applied.

**Solution:**

1. Range error per day: $\Delta\rho = c \, \Delta t = 2.998 \times 10^8 \times 38 \times 10^{-6} = 1.14 \times 10^4$ m.

**Answer:** About $11$ km of range error per day.

**Sanity check:** Light travels about 300 km in one millisecond, and 38 microseconds is about 4 percent of a millisecond. That gives roughly 11 km, which matches the result. Error that builds to kilometres within a day cannot be ignored in navigation, so the correction is required.

A second example uses the structural model. A bracket with stiffness $K = 2.0 \times 10^6$ N/m under a load $f = 5.0 \times 10^3$ N moves $u = f / K = 2.5 \times 10^{-3}$ m, or 2.5 mm. A finite element solver does the same division for thousands of coupled nodes at once.

## Lessons for engineers today

The modern tools make it easy to produce a result that looks exact. A simulation prints numbers to many digits, and a GPS position shows metres of detail. Those digits say nothing about accuracy unless someone checks them. The principles in [Principles that last](../philosophy/07-principles-that-last.md) apply directly. Write the units and the uncertainty on every number. Check a simulation against a test, and check the test against a second measurement. Report a mismatch when it appears, because a small discrepancy found early is cheap to fix.

The same principles apply to engineering that has not been invented yet. Engineers will work with tools, materials, and energy sources that do not exist in this repo, and the physics that governs them will still be conservation of energy and mass, entropy, and forces that come in pairs. Future engineers will need to state their assumptions and the limits of their models, because a new technology will also have a range where its equations stop being true, and failures tend to happen just past that range. They will need open formats so that a design outlives the software that made it, since the software of this era will be replaced. They will need designs that fail slowly and visibly, because a new machine will also break. And they will need to write the reasoning down, because the next engineer to read the work will have to check it, and that engineer may work in a field that did not exist when the work was done. None of this requires knowing what the new tools are. It requires keeping the checks that every earlier era needed.

## Practice

1. Name two things a GPS receiver must solve to find its position. How many satellites does it need, and why?
2. A GPS satellite clock drifts by 38 microseconds per day. Using $c = 2.998 \times 10^8$ m/s, find the range error after one day and after one week.
3. A bracket has stiffness $K = 2.0 \times 10^6$ N/m. Under a load of $5.0$ kN, what is the displacement?
4. A finite element model prints a stress with eight digits. Why does that not prove the stress is correct? Name one check that would give confidence.
5. Name two ways that a networked team can share engineering data, and one risk that comes with each.

<details><summary>Answers</summary>

1. The receiver solves for three position coordinates and its own clock error. It needs four satellites, because each gives one equation and there are four unknowns.
2. One day: $2.998 \times 10^8 \times 38 \times 10^{-6} = 1.14 \times 10^4$ m, about 11 km. One week: $7 \times 11.4$ km, about 80 km.
3. $u = f / K = 5.0 \times 10^3 / 2.0 \times 10^6 = 2.5 \times 10^{-3}$ m, or 2.5 mm.
4. Digits show how the answer was printed, not whether the model is right. A model with wrong boundary conditions or a coarse mesh gives a precise, wrong stress. A check against a simple hand calculation, or against a test of a real part, gives confidence.
5. Shared cloud storage and version control both keep one copy of each file that the whole team can review. The risks are overwriting another person's change and leaking confidential data to a server that the company does not control.

</details>

## Common mistakes

- Treating the internet, the World Wide Web, and ARPANET as one thing. ARPANET came first in 1969, the TCP/IP protocols followed in 1983, and the Web was proposed in 1989. The Web runs on the internet.
- Assuming GPS needs only three satellites. A receiver with an unknown clock error needs four.
- Treating simulation output as measured data. A model gives a prediction, and only a test or an independent check confirms it.
- Thinking additive manufacturing replaces all machining. It has limits in speed, surface finish, and layer strength, and many parts still need cutting or forming.
- Forgetting relativity in timing systems. Satellite clocks run at a different rate than clocks on the ground, and the error grows fast without a correction.

## Go deeper

- [GPS.gov](https://www.gps.gov/): the official United States information site for the Global Positioning System, free to read.
- [Digital logic and computers](../applications/electronics/07-digital-logic-and-computers.md) and [GPS](../applications/waves-and-communication/08-gps.md): how the chips and the satellite signals work in this repo.
- [Semiconductors and computing](09-semiconductors-and-computing.md): the chips that made the modern era possible.
- [History of engineering reference](reference.md): the lookup sheet for this topic.
