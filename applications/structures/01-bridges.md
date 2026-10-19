# Bridges

**Type:** lesson

A **bridge** is a structure that carries a road, rail line, or path across a gap. A bridge that fails can cut off a town's road or railway, so an engineer must get the design right before the first load crosses.

Engineers choose a bridge type from the span, the ground, the traffic, and the budget, then check that every member carries its load without bending too far, buckling, or breaking.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Bending and buckling](../../physics/05-bending-and-buckling.md), [Mechanics reference](../../physics/reference-mechanics.md)
**Time:** 8-12 h

## Core ideas

### How it works

A bridge has one job: move loads along a path to the ground. The deck carries vehicles and people. The deck passes its load to girders or trusses. The girders or trusses pass it to piers or abutments, and the piers push into soil or rock. Statics says the forces on the whole bridge sum to zero, and it says the same for each support and each joint. Once the load path is clear, the engineer knows which members carry tension, which carry compression, and which bend.

A simply supported beam shows the idea. The load pushes the beam down, and the two supports push up. The beam bends into a shallow curve. The top fibers shorten and the bottom fibers stretch. The middle of the beam has the largest bending moment, and the ends carry the largest shear. **Stiffness**, the resistance to bending, depends on the material and on the shape of the cross-section. Depth matters most, because stiffness grows with the cube of the depth for a rectangular section.

### Main parts

- **Deck.** The surface that carries traffic. It spreads wheel loads to the girders.
- **Girders or trusses.** The main load-carrying members that span between supports.
- **Bearings.** Pads or pins that carry the vertical load and let the deck move with temperature. Without them, thermal growth cracks the deck or the supports.
- **Piers and abutments.** Vertical supports. Abutments also hold back the soil at the ends of the bridge.
- **Foundations.** Spread footings, piles, or caissons that spread the load into the ground.
- **Cables, towers, and hangers.** In suspension and cable-stayed bridges, the cables carry the deck loads and the towers carry the cable forces down to the ground.

### Variants

- **Beam (girder) bridges.** The deck bends. Concrete or steel girders cover spans of tens of metres. This is the most common type because it is simple and cheap to build.
- **Truss bridges.** Members form triangles. In an **ideal truss**, each member carries only axial force, either tension or compression. Steel trusses cover spans from about 50 m to 200 m, typically.
- **Arch bridges.** The arch carries mostly compression, and it pushes outward at the ends. The abutments must resist that thrust. Stone and concrete arches suit this shape, and Roman builders used it widely.
- **Suspension bridges.** The main cables carry tension, the hangers carry tension, and the towers carry compression. This type gives the longest spans. The Akashi Kaikyo Bridge in Japan has a main span of 1,991 m and opened in 1998.
- **Cable-stayed bridges.** Straight cables run from the towers to the deck. The deck carries compression and bending. This type covers spans of several hundred metres and suits medium-long crossings.

## Key equations

For a simply supported beam with uniform load $w$ in N/m over span $L$ in m:

- Maximum shear force at the supports: $V_{\mathrm{max}} = \dfrac{wL}{2}$, in N.
- Maximum bending moment at midspan: $M_{\mathrm{max}} = \dfrac{wL^2}{8}$, in N m.
- Bending stress at the extreme fiber: $\sigma = \dfrac{Mc}{I}$, in Pa, where $c$ is the distance in m from the neutral axis to the outer fiber and $I$ is the second moment of area in m$^4$.
- Midspan deflection: $\delta = \dfrac{5wL^4}{384\,EI}$, in m, where $E$ is the elastic modulus in Pa (about $200\times10^9$ Pa for structural steel, typical).

For a parabolic cable under uniform load with span $L$ in m and sag $s$ in m:

- Horizontal tension: $H = \dfrac{wL^2}{8s}$, in N. The cable tension at the tower is larger than $H$ because of the vertical component.

## Worked example

**Given:** A simply supported steel girder spans $L = 30\ \text{m}$. It carries a uniform load of $w = 40\ \text{kN/m}$, which includes the girder's own weight. The section has a second moment of area $I = 0.020\ \text{m}^4$ and a depth of $1.2\ \text{m}$, so $c = 0.6\ \text{m}$. The elastic modulus is $E = 200\ \text{GPa}$.

**Find:** the maximum shear, the maximum bending moment, the maximum bending stress, and the midspan deflection.

**Assumptions:** The girder is simply supported at both ends. The section is uniform along the span. The steel behaves elastically. The load is uniform and static.

**Solution:**

1. Total load: $wL = 40 \times 10^3 \times 30 = 1.2\times10^6\ \text{N}$.
2. Maximum shear: $V = wL/2 = 600\ \text{kN}$.
3. Maximum moment: $M = wL^2/8 = 40\,000 \times 30^2 / 8 = 4.5\times10^6\ \text{N m}$.
4. Bending stress: $\sigma = Mc/I = 4.5\times10^6 \times 0.6 / 0.020 = 135\ \text{MPa}$.
5. Deflection: $\delta = 5wL^4/(384EI) = 0.105\ \text{m} = 105\ \text{mm}$.

**Answer:** $V = 600\ \text{kN}$, $M = 4.5\ \text{MN m}$, $\sigma = 135\ \text{MPa}$, and $\delta = 105\ \text{mm}$, which is $L/284$.

**Sanity check:** The total load of 1.2 MN splits evenly between two supports, so each support carries 600 kN. That matches step 2. The stress of 135 MPa sits below the yield strength of structural steel, which is about 250 MPa (typical). A deflection of $L/284$ is large for a service check. Design codes set a deflection limit for vehicle loads, often a span divided by several hundred, so this girder needs more depth or stiffness before it passes.

## Design trade-offs

- **Span against depth.** A deeper girder is stiffer and carries more moment, but it adds weight, adds dead load, and raises the approach grades. Doubling the depth of a rectangular girder cuts the deflection to one-eighth for the same load.
- **Material.** Steel is strong and light, and it suits long spans and fast erection. Concrete is cheap and needs little maintenance, but it is heavy and cracks in tension unless it has prestressing steel.
- **Corrosion and maintenance.** Road salt and wet air attack steel. Paint systems, drainage, and inspection access all add cost over the life of the bridge.
- **Fatigue.** Trucks load and unload the bridge thousands of times a year. Welded details fail from repeated stress well below the static strength, so designers limit the stress range at each detail.
- **Wind.** Long, light decks can move in the wind. The shape of the deck and its stiffness both control whether the motion stays small.
- **Construction method.** Cantilever erection, falsework, and launching each suit a different site and span. The method can drive the choice of type.

Bridge design in the United States follows the AASHTO specifications. Those specifications set the load combinations, the factors, and the limits that a designer checks.

## How it fails

- **Fatigue cracking.** Repeated loading grows a crack at a weld or a bolt hole until the member breaks suddenly. The Silver Bridge over the Ohio River, between Ohio and West Virginia, collapsed in December 1967 when an eyebar fractured. The collapse killed 46 people. Inspection programs and fatigue-rated details now exist because of this failure.
- **Aeroelastic flutter.** Wind interacts with the deck and feeds energy into the motion. The Tacoma Narrows Bridge in Washington state twisted in a steady wind and collapsed in November 1940, about four months after it opened. Wind tunnel tests and deck shapes that shed wind now guard against this.
- **Undersized connections.** The I-35W bridge in Minneapolis collapsed in August 2007. A gusset plate at a truss joint failed. The collapse killed 13 people. Today, connection design checks each plate against its full load path.
- **Scour.** Fast river water removes soil from around a pier foundation. The pier then loses its support. Scour is one of the most common causes of bridge failure, so engineers monitor pier depth and design foundations below the expected scour depth.
- **Failure during construction.** The first Quebec Bridge collapsed in 1907 while under construction. A compression member buckled under its own weight and the weight of the partly built span. The collapse killed 75 workers. Erection analysis now checks each stage, not only the finished bridge.

Warning signs include cracks at welds, rust that flakes off steel in layers, deck movement that changes with traffic, and new cracks at bearings or joints.

## History

The Romans built stone arch bridges that still stand, and their designs spread across Europe. Iron and then steel replaced stone in the 1800s. The Brooklyn Bridge in New York, a steel-wire suspension bridge, was designed by John A. Roebling and completed in 1883 under his son Washington Roebling after John died in 1869. The Forth Bridge in Scotland, a steel cantilever truss, opened in 1890. The Golden Gate Bridge in San Francisco opened in 1937 with a main span of about 1,280 m.

## Practice

1. A simply supported beam spans 12 m and carries a uniform load of 20 kN/m. Find the maximum bending moment and the maximum shear force.
2. A parabolic cable spans 100 m with a sag of 4 m and carries a uniform load of 20 kN/m. Find the horizontal tension in the cable.
3. The span in the worked example doubles, and the load per metre and the section stay the same. How many times larger does the midspan moment become? How many times larger does the deflection become?
4. In the worked example, the second moment of area doubles to 0.040 m$^4$. Find the new midspan deflection in mm.
5. Explain in one or two sentences why the top fibers of a simply supported beam are in compression and the bottom fibers are in tension.

<details><summary>Answers</summary>

1. $M_{\mathrm{max}} = wL^2/8 = 20\,000 \times 12^2 / 8 = 360\ \text{kN m}$. $V_{\mathrm{max}} = wL/2 = 120\ \text{kN}$.
2. $H = wL^2/(8s) = 20\,000 \times 100^2 / (8 \times 4) = 6.25\times10^6\ \text{N}$, which is $6250\ \text{kN}$.
3. Moment grows with $L^2$, so it becomes 4 times larger. Deflection grows with $L^4$, so it becomes 16 times larger.
4. Deflection is inversely proportional to $I$, so it halves to $105/2 = 53\ \text{mm}$, about $52.7\ \text{mm}$.
5. Sagging bends the beam into a curve that is concave up. The top fibers shorten (compression) and the bottom fibers stretch (tension).

</details>

## Common mistakes

- Treating truss members as if they bend. An ideal truss member carries only axial force, so its stress is $F/A$.
- Leaving out the self-weight of the deck and girders. On long spans, the dead load often exceeds the live load.
- Checking strength and forgetting deflection, vibration, and fatigue. A bridge can pass the strength check and still feel unsafe or crack at a detail.
- Assuming a cable can carry compression. A cable carries tension only, and it goes slack under compression.
- Fixing the bearings so the deck cannot move. The deck grows and shrinks with temperature, and a locked deck cracks at its supports.

## Go deeper

- [*University Physics Volume 1*, Chapter 12 (static equilibrium and elasticity)](https://openstax.org/books/university-physics-volume-1/pages/12-introduction) by OpenStax: force balance, torque, and stress and strain in beams and rods.
- Related lessons: [Buildings and skyscrapers](02-buildings-and-skyscrapers.md), [Pressure vessels and tanks](03-pressure-vessels-and-tanks.md), [Aircraft structures](04-aircraft-structures.md), [Dams](05-dams.md), [Towers and cables](06-towers-and-cables.md).
- Background on the forces: [Statics](../../physics/01-statics.md) and [Bending and buckling](../../physics/05-bending-and-buckling.md).
