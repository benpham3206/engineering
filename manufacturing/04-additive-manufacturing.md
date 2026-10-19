# Additive manufacturing

**Type:** lesson

**Additive manufacturing (AM)**, commonly called 3D printing, is the family of processes that builds a part one thin layer at a time, adding material only where the part needs it. Engineers use it because it makes shapes that are hard or impossible to machine. Its layer-by-layer build also brings its own limits on strength, surface finish, and speed. An engineer who designs for AM must design for the way the part is built, not only for its final shape.

**Prerequisites:** [Shop safety](01-shop-safety.md)
**Time:** 4-6 h

## Core ideas

- **Slicing**: software cuts the 3D model into horizontal layers and writes the path for each one. Each layer is called a slice.
- **Layer thickness**: the height of one layer, often 0.05 to 0.3 mm in polymer printing. Thinner layers look smoother and take longer.
- **Build direction**: the direction the layers stack. The part is usually weaker across layers than along them, because the bonds between layers are the weak points.
- **Support**: material printed under overhangs so the upper layers have something to rest on. Remove supports after the build.
- **Overhang**: a part of the model that sticks out past the layer below. Steep overhangs need supports or a different orientation.

Common processes include:

- **Fused deposition modeling (FDM)**: the printer melts plastic filament and extrudes it through a nozzle. It is cheap and common, but layers are visible and parts are often weaker across layers.
- **Stereolithography (SLA) and DLP**: a light source cures liquid resin one layer at a time. It gives fine detail and a smooth surface.
- **Selective laser sintering (SLS)**: a laser fuses powder, usually nylon. The unfused powder supports the part, so supports are rarely needed.
- **Metal powder bed fusion**: a laser or electron beam melts metal powder layer by layer. It makes strong metal parts but needs careful control of heat and stress.

Design rules that help:

- Orient the part so the load runs along the layers, not across them.
- Avoid overhangs steeper than the process can handle without supports.
- Add fillets and chamfers to reduce stress at sharp corners.
- Leave clearance in holes and moving joints, because the printed size can differ from the model.
- Allow room to remove support and powder.

## Key equations

The number of layers $n$ in a part of height $h$ with layer thickness $t$:

$$n = \frac{h}{t}$$

Units: $h$ and $t$ must be in the same length unit (mm in SI, inches in US form). $n$ is a count with no units.

## Worked example

**Given:** A bracket is 40 mm tall and is printed with FDM at a layer thickness of $t = 0.2$ mm.

**Find:** The number of layers, and how many layers would be needed at $t = 0.1$ mm.

**Assumptions:** The part height equals the build height, with no extra raft or support in the count.

**Solution:**

1. At $t = 0.2$ mm:
$$n = \frac{40}{0.2} = 200 \text{ layers}$$
2. At $t = 0.1$ mm:
$$n = \frac{40}{0.1} = 400 \text{ layers}$$

**Answer:** 200 layers at 0.2 mm, or 400 layers at 0.1 mm.

**Sanity check:** Halving the layer thickness doubles the layer count. A 2x change in layers means roughly a 2x change in build time for the layer-driven part of the job, so the finer print will take noticeably longer.

## Practice

1. A part is 60 mm tall with $t = 0.2$ mm. How many layers?
2. A part is 40 mm tall with $t = 0.1$ mm. How many layers?
3. A bracket is printed with its strongest direction along the build axis, but its load is across the layers. Is that a good orientation? Answer yes or no.
4. A printed part has a 90 degree overhang with no support. Name one design fix.
5. A part is 25 mm tall with $t = 0.25$ mm. How many layers?

<details><summary>Answers</summary>

1. 300 layers
2. 400 layers
3. No
4. Reorient the part, add a chamfer or a gusset, or add support material.
5. 100 layers

</details>

## Common mistakes

- Printing with the load across the layers. Layer bonds are the weakest path in many processes.
- Forgetting that a printed hole is often smaller or rougher than the model. Design for finishing.
- Leaving out clearance for moving parts, so they bind when printed.
- Assuming a 3D print has the same strength as a machined or cast part of the same material.
- Judging print time from layer count alone. Speed, path length, and support volume all matter.

## Go deeper

- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: national manufacturing research, including additive manufacturing standards work.
- [Paul's Online Math Notes: Algebra](https://tutorial.math.lamar.edu/classes/alg/alg.aspx) by Paul Dawkins, Lamar University: solving simple formulas such as $n = h/t$.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
