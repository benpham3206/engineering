# Joining: welding, fastening, and adhesives

**Type:** lesson

Joining is the making of a connection between two or more parts so they act as one assembly. Every assembly is only as strong as its joints, so a weak or poorly inspected joint can cause a whole machine to fail. The three main families are welding (fusing the base metal, usually with heat), mechanical fastening (bolts, screws, rivets, and pins), and adhesive bonding (glues and epoxies). Each has different strength, cost, inspection, and reversibility. Engineers choose a joint by asking what load it carries, whether it must come apart later, and how it will be checked.

**Prerequisites:** [Shop safety](01-shop-safety.md)
**Time:** 5-7 h

## Core ideas

- **Weld**: a joint where the base metal melts and fuses, often with added filler metal. Common types include MIG (wire-fed), TIG (tungsten electrode), and stick (shielded metal arc). Welds are permanent.
- **Fillet weld**: a triangular weld in a corner joint. Its size is given by the leg length (the two equal sides of the triangle).
- **Throat**: the shortest distance from the root of the weld to its face. For a standard 45 degree fillet weld, the throat is about 0.707 times the leg length.
- **Heat-affected zone (HAZ)**: the region next to a weld that is heated but does not melt. Its properties can change, so welded parts can lose strength near the weld.
- **Bolt**: a threaded fastener that clamps parts together. You usually tighten a bolt to a set preload, which is the clamping force. Preload matters more than the torque number alone.
- **Adhesive**: a material that bonds surfaces by filling and gripping them. Surface preparation (cleaning and roughening) decides most of the bond strength.
- **Clearance hole**: a hole a little larger than the bolt, so the bolt passes through. A tapped hole has threads cut into it so a bolt screws in directly.

Choosing a joint:

- Use welding for permanent, high-strength joints in structures and frames.
- Use bolts and screws when the joint must be serviced, adjusted, or replaced.
- Use adhesives to join dissimilar materials, spread load over a wide area, or seal a joint.
- Combine methods when it makes sense. An adhesive bond plus a few bolts is common in aircraft and cars.

Inspection differs too. A bolt can be torqued and checked. A weld needs visual checks and often ultrasonic or dye penetrant tests. An adhesive joint is hard to inspect after cure, so the process must be controlled.

Hot work (welding, cutting, and brazing) brings fire, fumes, UV light, and burns. OSHA's guidance on welding, cutting, and brazing is listed in lesson 01 and below.

## Key equations

The throat thickness $t$ of a standard 45 degree fillet weld with leg length $a$ is:

$$t = 0.707\,a$$

Units: $a$ and $t$ must be in the same unit (mm in SI, inches in US form). The factor 0.707 is $\sqrt{2}/2$, from the geometry of a right isosceles triangle.

## Worked example

**Given:** A fillet weld on a steel bracket has a leg length of $a = 6$ mm.

**Find:** The throat thickness of the weld.

**Assumptions:** The weld is a standard 45 degree fillet with equal legs.

**Solution:**

$$t = 0.707 \times 6 = 4.24 \text{ mm}$$

**Answer:** The throat is about 4.24 mm.

**Sanity check:** The throat is always smaller than the leg, because the throat is the short side of a triangle with two legs of length 6 mm. The computed throat of 4.24 mm is shorter than the 6 mm leg, as it must be.

## Practice

1. A fillet weld has a leg length of $a = 8$ mm. What is the throat thickness in mm? Round to two decimal places.
2. A fillet weld has a leg length of $a = 1/4$ in. What is the throat in inches? Round to three decimal places.
3. Name one reason a bolted joint is preferred over a welded joint in a machine that needs servicing.
4. What does the heat-affected zone describe?
5. Why does surface cleaning matter for an adhesive bond?

<details><summary>Answers</summary>

1. 5.66 mm
2. 0.177 in
3. Bolts can be removed and reinstalled without damaging the parts.
4. The region next to a weld that is heated but does not melt, and whose properties can change.
5. Contamination such as oil or dust stops the adhesive from wetting and gripping the surface, so the bond is weak.

</details>

## Common mistakes

- Using the leg length as the strength. Strength depends on the throat, not the leg.
- Ignoring the heat-affected zone, so a weld fails next to the weld instead of in it.
- Torquing a bolt to a number without considering the preload, the friction, and the thread condition.
- Bonding without cleaning and roughening the surface, which causes weak or peel failures.
- Skipping inspection. Joints that cannot be checked after assembly need a controlled process.

## Go deeper

- [Welding, cutting, and brazing](https://www.osha.gov/welding-cutting-brazing) by OSHA (U.S. Department of Labor): hot-work hazards, standards, and controls.
- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: solving formulas, including the throat calculation.
- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: manufacturing quality and joining research.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
