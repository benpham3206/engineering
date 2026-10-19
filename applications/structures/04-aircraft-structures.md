# Aircraft structures

**Type:** lesson

An aircraft structure is the thin shell of skin, frames, and stringers that carries an aircraft's flight, pressure, and landing loads. An engineer must keep that shell within stress limits for its whole life, because fatigue and damage grow over thousands of flights.

The shell must also weigh as little as possible, which is why it is thin.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Bending and buckling](../../physics/05-bending-and-buckling.md), [Mechanical properties](../../materials/03-mechanical-properties.md), [Single-variable calculus](../../math/03-single-variable-calculus.md)
**Time:** 8-10 h

## Core ideas

### How it works

Most transport aircraft use a semi-monocoque structure. The skin is a thin sheet that carries shear and pressure. Longitudinal stringers stiffen the skin and carry axial load along the fuselage. Circumferential frames hold the cross-section round and transfer pressure loads into the skin. The skin and stringers share the bending load, and the frames keep the skin from buckling under compression.

A wing works the same way. Spars carry bending. The spar caps take axial load, and the web takes shear. Ribs hold the airfoil shape and pass lift loads into the skin. The skin and spars together form a torsion box, which resists twisting.

The load path follows a chain from the source to the ground:

1. Air pressure acts on the skin, and the cabin pressure pushes outward on the fuselage.
2. The skin carries that pressure as hoop stress around the frames and as axial stress along the fuselage.
3. The frames and stringers carry the load to the bulkheads and the wing attachment fittings.
4. The wing carries lift to the fuselage through the wing box, and the landing gear carries the weight to the ground.

The design uses limit loads, which are the largest loads expected in service. Ultimate loads are limit loads multiplied by a factor of 1.5, which is the standard margin for transport aircraft. The structure must not fail at limit load and must not fail at ultimate load.

### Main parts

- Skin: a thin aluminum or composite sheet. It carries shear and pressure, and its thickness is usually a few millimetres.
- Stringers: longitudinal stiffeners attached to the skin. They carry axial load and raise the buckling strength of the skin.
- Frames: circumferential rings at regular spacing. They hold the cross-section shape and carry pressure loads.
- Spars and ribs: the main beams and chordwise members of a wing. Spar caps take bending, and the web takes shear.
- Bulkheads: pressure bulkheads at the nose and tail seal the cabin.
- Fasteners and joints: rivets, bolts, and bonded joints. Joints often control fatigue life because they hold stress concentrations.
- Doublers and cutouts: reinforcement plates around windows, doors, and access panels.

### Variants

- Aluminum semi-monocoque: the standard construction for most transport aircraft since the 1930s.
- Carbon fibre composite: used for large parts of modern airliners, such as the fuselage and wings of the Boeing 787 and the Airbus A350. Composites save weight and resist fatigue cracking, but damage from impacts can be hard to see.
- Monocoque shell: a shell that carries all the load without internal stringers. Some sailplanes use this form.
- Truss and fabric: light general aviation aircraft and early machines used welded steel tubes or wood frames covered with fabric. The Wright Flyer of 1903 used wood and fabric.

## Key equations

Thin-wall hoop stress in the skin, with $p$ the internal pressure difference in pascals, $r$ the radius in metres, and $t$ the wall thickness in metres:

$$\sigma_h = \frac{p\,r}{t}$$

This assumes a closed circular cylinder with uniform internal pressure, a thin wall ($t/r < 0.1$), linear elastic material, and it ignores the stiffening effect of stringers and frames.

Axial stress in the same thin shell:

$$\sigma_a = \frac{p\,r}{2t}$$

This assumes the same thin closed cylinder with end caps that carry the axial load, and the same linear elastic, uniform-pressure conditions.

The thin-wall formulas hold when the wall is thin compared with the radius, which is $t/r$ below about 0.1.

Bending stress in a stringer or spar cap, with $M$ the bending moment in N m, $y$ the distance from the neutral axis in metres, and $I$ the second moment of area in m$^4$:

$$\sigma = \frac{M\,y}{I}$$

This assumes a straight beam with a constant cross-section, plane sections that stay plane, linear elastic material, and small deflections, so the moment arm does not change.

Margin of safety against yield, with $\sigma_y$ the yield strength in pascals and $\sigma$ the applied stress:

$$\text{MS} = \frac{\sigma_y}{\sigma} - 1$$

This assumes a single static load case, a uniform stress field at the point checked, and that yield is the failure criterion. It does not cover fatigue or buckling.

Crack growth in fatigue, the Paris law, with $a$ the crack length in metres, $N$ the number of load cycles, $\Delta K$ the stress intensity range in Pa$\sqrt{\text{m}}$, and $C$ and $m$ material constants:

$$\frac{da}{dN} = C\,(\Delta K)^m, \qquad \Delta K = \Delta\sigma\sqrt{\pi a}$$

Here $\Delta\sigma$ is the stress range in pascals. These assume constant-amplitude loading, a crack that grows in the stable Paris regime (not near the threshold or the fracture limit), a geometry factor of 1 for a crack in a wide plate, and $C$ and $m$ determined from tests in the same material and environment.

## Worked example

A fuselage has radius $r = 2.8$ m (a typical wide-body value) and skin thickness $t = 1.6$ mm. The cabin pressure difference at cruise is $p = 57$ kPa (typical, about 8.3 psi). The skin is aluminum 2024-T3 with a minimum yield strength of $\sigma_y = 345$ MPa (typical value). Find (a) the hoop stress, (b) the axial stress, and (c) the margin against yield at limit load and at ultimate load.

Solution for (a): $\sigma_h = p r / t = 57\,000 \times 2.8 / 0.0016 = 99.8$ MPa, or about 100 MPa.

Solution for (b): $\sigma_a = \sigma_h / 2 = 49.9$ MPa, or about 50 MPa.

Solution for (c): at limit load, the yield strength is $345 / 99.8 = 3.46$ times the applied stress, so the margin of safety is $\text{MS} = 3.46 - 1 = 2.46$. At ultimate load, the pressure is 1.5 times larger, so the hoop stress is $1.5 \times 99.8 = 149.6$ MPa, the strength ratio is $345 / 149.6 = 2.31$, and the margin of safety is $\text{MS} = 2.31 - 1 = 1.31$.

Answers: (a) about 100 MPa, (b) about 50 MPa, (c) margin of safety about 2.5 at limit load and about 1.3 at ultimate load.

Sanity check: the hoop stress is twice the axial stress, which matches the formulas. The thin-wall ratio $t/r = 0.0016 / 2.8 = 0.00057$ is far below 0.1, so the thin-wall formulas are valid. Static strength is not the limiting factor here. Fatigue, which depends on the number of pressurization cycles, usually governs the skin design.

## Design trade-offs

- Skin thickness against weight: a thicker skin resists pressure and buckling, but every extra kilogram costs fuel and payload.
- Frame and stringer spacing against weight and inspection: closer spacing stiffens the skin and shortens the crack path between frames, but it adds parts to build and inspect.
- Aluminum against composite: aluminum is cheap, easy to inspect, and repairs well. Composites save weight and resist fatigue, but impact damage can hide inside the laminate, and they cost more to make.
- Cabin pressure against structure: a lower cabin pressure difference reduces hoop stress and weight, but it limits the cabin altitude passengers can tolerate.
- Joint type against fatigue: riveted joints are reliable and easy to inspect, but each hole is a stress concentrator. Bonded joints spread load more evenly, but they are harder to inspect and repair.

## How it fails

- Fatigue cracks: repeated pressurization and flight loads grow cracks from rivet holes and corners. Stress concentration at a circular hole in tension is about 3, so the local stress is about three times the nominal value.
- Corrosion: moisture and salt trap in joints and cause pitting. Warning signs include bubbling paint, white powder, and loose rivets.
- Impact damage in composites: a dropped tool or a bird strike can cause delamination that a visual check misses.
- Skin buckling: thin skin under compression or shear buckles before it reaches its yield stress.

The most famous fatigue failures include the de Havilland Comet jet airliner breakups in 1953 and 1954, which led to a much better understanding of cracks around square windows. In 1988, the upper fuselage of Aloha Airlines Flight 243, a Boeing 737-200, tore away in flight because of fatigue cracks at lap joints.

Safety measures include damage tolerance design, which requires that a crack must grow slowly enough that inspections find it before it reaches critical length. The FAA sets this requirement in 14 CFR 25.571. Designers also use fail-safe load paths, so that one broken member does not collapse the structure, and they set inspection intervals based on crack growth data.

## History

The Wright Flyer of 1903 used a wood and fabric structure. Alfred Wilm in Germany developed the aluminum alloy duralumin in about 1909, which made strong, light metal structures practical. Hugo Junkers built the all-metal J 1 in 1915 in Germany. The Boeing 247 of 1933 and the Douglas DC-3 of 1935 brought the stressed-skin aluminum monocoque to commercial airliners. The Comet and Aloha accidents later showed that fatigue design needed its own rules and inspection programs. Dates in this section are approximate where sources differ.

## Practice

1. A thin-wall fuselage has radius $r = 2.0$ m, skin thickness $t = 2.0$ mm, and pressure difference $p = 50$ kPa. Find the hoop stress in MPa.
2. Using the same data as problem 1, find the axial stress in MPa.
3. Explain why the hoop stress is about twice the axial stress in a pressurized cylinder.
4. A skin has a yield strength of 345 MPa and an applied stress of 75 MPa. Find the margin of safety against yield, using $\text{MS} = \sigma_y/\sigma - 1$.
5. Explain why a crack at a rivet hole grows faster than a crack in plain skin of the same length.

<details><summary>Answers</summary>

1. $\sigma_h = p r / t = 50\,000 \times 2.0 / 0.002 = 50.0$ MPa.
2. $\sigma_a = \sigma_h / 2 = 25.0$ MPa.
3. The axial stress comes from the end caps. They carry the load $p\pi r^2$ over a wall area of $2\pi r t$, which gives $pr/(2t)$. The hoop stress has no end caps to share the load, so it carries the full $pr$ per unit length over one wall thickness, which gives $pr/t$.
4. $\text{MS} = 345 / 75 - 1 = 3.6$.
5. The hole is a stress concentrator. In tension, a circular hole raises the local stress to about three times the nominal value, so the crack tip sees a much higher stress intensity and grows faster.

</details>

## Common mistakes

- Using diameter where the formula needs radius. Hoop stress uses $r$, and the diameter gives twice the stress.
- Using the thin-wall formulas for thick sections. Check $t/r$ first, and use thick-wall theory when the ratio is larger than about 0.1.
- Ignoring the 1.5 factor between limit and ultimate load when checking static strength.
- Treating a design as safe because static stress is low. Fatigue governs many skin and joint designs.
- Assuming composites never crack. They can delaminate from impacts that leave no visible mark on the surface.

## Go deeper

- [Bending and buckling](../../physics/05-bending-and-buckling.md): the beam and column theory behind stringers and spars.
- [Fracture and fatigue](../../materials/06-fracture-and-fatigue.md): crack growth and stress concentration in detail.
- [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md): how designers choose margins.
- [Pressure vessels and tanks](03-pressure-vessels-and-tanks.md): the thin-wall and hoop-stress background in a non-aircraft setting.
- [Aircraft and wings](../vehicles-aerospace/05-aircraft-and-wings.md): the forces and loads that the structure must carry.
- [Reference: mechanics](../../physics/reference-mechanics.md): equation sheet for stress, bending, and related quantities.
- [Reference: materials](../../materials/reference.md): equation sheet for mechanical properties, fracture, and fatigue.
- [Reference: design](../../design/reference.md): equation sheet for factors of safety and failure criteria.
</content>
