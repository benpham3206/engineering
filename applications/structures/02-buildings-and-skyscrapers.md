# Buildings and skyscrapers

**Type:** lesson

A building must hold up its own weight, the weight of its occupants and contents, and the sideways forces from wind and earthquakes. Engineers design a frame, a set of walls, and a foundation so that every load reaches the ground and the building stays within safe stress and sway limits.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Bending and buckling](../../physics/05-bending-and-buckling.md), [Mechanics reference](../../physics/reference-mechanics.md)
**Time:** 8-12 h

## Core ideas

### How it works

Gravity loads flow downward. Each floor slab carries its load to beams. The beams carry it to columns, the columns carry it to the foundation, and the foundation spreads it into the soil. Each column in a multi-storey building carries the load from every floor above it, so the axial force grows from the roof down to the base.

Lateral loads push sideways. Wind pushes on the faces of the building, and an earthquake shakes the ground under it, which sets the building moving. Those forces create shear between floors and overturning moments at the base. The frame, the walls, or the core resists them. A tall, slender building must resist sway as well as strength. Sway that is too large cracks the partitions, makes occupants uncomfortable, and in extreme cases damages the structure.

### Main parts

- **Floor slabs and beams.** Carry the floor loads to the columns. Concrete slabs on steel beams are common in office towers.
- **Columns.** Carry the axial load from above. Steel columns are often wide-flange sections, and concrete columns are often reinforced.
- **Lateral system.** Moment frames, braced frames, shear walls, or a central core resist wind and earthquake forces. The core often holds stairs, elevators, and service shafts, so it also serves as a spine for the building.
- **Foundation.** Spread footings, mats, or piles carry the column loads into the soil. Soil bearing capacity and settlement decide the choice.
- **Cladding and partitions.** These are non-structural in most designs, but they must accept the building's movement without cracking or falling.

### Variants

- **Moment frames.** Beams and columns are rigidly joined. The joints resist sway through bending. They suit low- to mid-rise buildings with open floor plans.
- **Braced frames.** Diagonal braces turn the frame into trusses that resist sway. They stiffen the building efficiently but block some openings.
- **Shear walls.** Concrete walls in the plane of the building resist sideways loads. They suit residential and hotel buildings where walls already divide the rooms.
- **Core and outrigger systems.** A central core carries most of the lateral load. Outriggers connect the core to perimeter columns, so the perimeter columns help resist overturning. This is common in tall towers.
- **Framed tube.** Closely spaced columns on the perimeter act like a tube that resists overturning. This layout suits very tall, slender towers.

## Key equations

For a column carrying tributary area $A_t$ in m$^2$ over $n$ floors, with dead load $q_D$ and live load $q_L$, both in Pa:

- Service axial load: $P = n\,A_t\,(q_D + q_L)$, in N.
- Factored axial load using the load combination $1.2D + 1.6L$: $P_u = n\,A_t\,(1.2\,q_D + 1.6\,q_L)$, in N.

Wind pressure on a face: $q = \tfrac{1}{2}\rho V^2$, where $\rho = 1.225\ \text{kg}/\text{m}^3$ is the density of air at sea level on Earth (typical) and $V$ is the design wind speed in m/s. Base moment from a uniform lateral load $F$ in N on a building of height $h$ in m: $M_{\mathrm{base}} = F h / 2$, in N m.

Column axial stress: $\sigma = P/A$, in Pa, where $A$ is the column cross-section in m$^2$.

Interstorey drift: the sideways displacement of one floor relative to the floor below, $u_i - u_{i-1}$, divided by that storey's height. The overall drift ratio is the top displacement $\Delta$ divided by the building height $H$. Designers compare these ratios to limits, often about $H/400$ to $H/500$ for wind (typical, depends on the code and use).

## Worked example

**Given:** A 12-storey office column carries floors on a grid of 6 m by 9 m. The tributary area is $A_t = 54\ \text{m}^2$. Dead load on each floor is $q_D = 3.5\ \text{kPa}$, including partitions and the slab. Live load is $q_L = 2.5\ \text{kPa}$.

**Find:** the service axial load and the factored axial load at the base of the column.

**Assumptions:** No live load reduction is applied. Real codes allow a reduction for upper floors, so this result is conservative. The column self-weight is ignored because it is small against the floor loads.

**Solution:**

1. Dead load per floor: $3.5\times10^3 \times 54 = 189\ \text{kN}$.
2. Live load per floor: $2.5\times10^3 \times 54 = 135\ \text{kN}$.
3. Service dead load for 12 floors: $12 \times 189 = 2268\ \text{kN}$.
4. Service live load for 12 floors: $12 \times 135 = 1620\ \text{kN}$.
5. Factored load: $1.2 \times 2268 + 1.6 \times 1620 = 2721.6 + 2592 = 5313.6\ \text{kN}$.

**Answer:** The service load is $3888\ \text{kN}$ (about $3.9\ \text{MN}$). The factored load is $5314\ \text{kN}$ (about $5.3\ \text{MN}$). The designer sizes the column for the factored load.

**Sanity check:** The ratio of factored to service load is $5314 / 3888 = 1.37$. The combination weights dead load by 1.2 and live load by 1.6, so the ratio falls between 1.2 and 1.6, and 1.37 fits. At a working stress of 150 MPa (typical), a 3.9 MN service load needs a steel area of about 260 cm$^2$, which is a realistic column size for a building of this height.

## Design trade-offs

- **Height against lateral stiffness.** Under a uniform wind load, the top sway of a cantilever-like tower grows with the fourth power of height, so each doubling of height multiplies sway by about 16 for the same stiffness. Tall buildings need a core, outriggers, or a tube to keep sway in check.
- **Steel against concrete.** Steel is light and erects fast, so it suits tall, slender frames. Concrete is heavier but stiffer, damps vibration well, and resists fire better without added coatings.
- **Floor area against structure.** Columns and shear walls take space. A column-free plan costs more steel or depth in the beams.
- **Foundation cost.** Deep foundations such as piles or caissons cost more, but a tall building on weak soil can need them. Settlement often controls the design more than strength.
- **Earthquake detailing.** Ductile joints absorb energy by yielding. The cost of extra steel and careful detailing grows with the seismic hazard at the site.
- **Serviceability.** Designers limit drift so partitions, glazing, and elevators work. Wind-induced motion at the top of a tall tower can reach hundreds of millimetres, so the limit on drift often controls the stiffness.

The structural design of buildings in the United States follows ASCE 7 for loads, with material standards for steel and concrete.

## How it fails

- **Progressive collapse.** A local failure spreads to the rest of the building. Ronan Point, a 22-storey tower block in London, partly collapsed in 1968 after a gas explosion removed one load-bearing panel. Four people died. Modern codes require the structure to resist an accidental local loss without a disproportionate collapse.
- **Connection failure.** The Hyatt Regency walkways in Kansas City collapsed in 1981 during a dance. A change to the way the walkways were hung doubled the load on one set of connections. The collapse killed 114 people. Connections now receive the same care as members, and independent checks review the design.
- **Foundation settlement.** Uneven settlement tilts the frame, cracks the walls, and jams doors and windows. Soil tests and monitoring during construction catch the problem early.
- **Overturning and uplift.** Strong wind can lift one side of a light building and turn the foundation. Anchorage and dead weight resist uplift.
- **Earthquake damage.** Shaking that exceeds the design level can yield columns and walls. Ductile detailing keeps the building standing so that people can leave.

Warning signs include diagonal cracks in masonry or concrete walls, doors that stick, floors that slope, and cracks at the base of columns.

## History

Early tall buildings used load-bearing masonry walls, and thick lower walls limited how high they could rise. The Home Insurance Building in Chicago, completed about 1885 by William Le Baron Jenney, used a steel skeleton to carry the floors, which freed the walls. Elisha Otis demonstrated a safety brake for elevators in New York in 1854, and that brake made tall buildings usable. The Empire State Building in New York opened in 1931, and it stood as the tallest building in the world for about four decades. The Burj Khalifa in Dubai, completed in 2010 at 828 m, uses a buttressed central core.

## Practice

1. A column supports a tributary area of 40 m$^2$ over 10 floors. The dead load is 4.0 kPa per floor and the live load is 2.0 kPa per floor. Find the service axial load.
2. For the column in problem 1, find the factored axial load using $1.2D + 1.6L$.
3. A 150 m tower sways at its top by 300 mm under wind. Find the drift ratio $\Delta / H$ and compare it with a limit of $H/500$.
4. A building is twice as tall. Its lateral stiffness per unit height stays the same, and it carries a uniform wind load. How many times larger does the top sway become? Assume a cantilever-like model.
5. Name two lateral systems that use a central core or walls, and state one reason an architect might prefer each.

<details><summary>Answers</summary>

1. $D = 10 \times 40 \times 4.0 = 1600\ \text{kN}$. $L = 10 \times 40 \times 2.0 = 800\ \text{kN}$. Service load $= 1600 + 800 = 2400\ \text{kN}$.
2. $P_u = 1.2 \times 1600 + 1.6 \times 800 = 1920 + 1280 = 3200\ \text{kN}$.
3. $\Delta / H = 0.300\ \text{m} / 150\ \text{m} = 0.0020 = 1/500$. This matches the limit exactly.
4. Under a uniform load on a cantilever, tip sway scales with $H^4$, so doubling height makes it $2^4 = 16$ times larger.
5. Shear walls suit residential buildings because walls already divide the rooms. A central core suits offices and towers because it holds stairs, elevators, and shafts in one place. Accept any two correct systems with one valid reason each.

</details>

## Common mistakes

- Adding live loads without reducing them, or the reverse. Codes allow some reduction on upper floors, and the rules depend on the occupancy and tributary area.
- Sizing columns for the service load alone. Design uses the factored load, which weights dead and live load differently.
- Ignoring sway. A frame that is strong enough can still be too flexible, and partitions crack long before the structure fails.
- Treating the foundation as an afterthought. Settlement, bearing capacity, and groundwater often decide the foundation type before the superstructure is designed.
- Assuming lateral loads act only in the wind direction. Earthquakes shake the building in every direction, and torsion from an off-centre core adds to the stress in the outer columns.

## Go deeper

- [University Physics Volume 1, Chapter 12 (static equilibrium and elasticity)](https://openstax.org/books/university-physics-volume-1/pages/12-introduction) by OpenStax: force balance and stress in columns and beams.
- Related lessons: [Bridges](01-bridges.md), [Towers and cables](06-towers-and-cables.md), [Pressure vessels and tanks](03-pressure-vessels-and-tanks.md), [Aircraft structures](04-aircraft-structures.md).
- Background on the forces: [Statics](../../physics/01-statics.md) and [Bending and buckling](../../physics/05-bending-and-buckling.md).
