# CAD: SolidWorks and free alternatives

**Type:** lesson

**CAD**, short for computer-aided design, is software that builds 3D models of parts and assemblies on a computer and produces drawings and mass properties. Engineers use it to test a design before anything is cut or cast, so a mistake shows up on screen instead of in metal.

SolidWorks is a paid, widely used parametric CAD program, so many employers and courses expect it. You can learn the same ideas in free tools, and the skills carry over.

**Prerequisites:** [Starter kit](01-starter-kit.md), [Python](02-python.md) (for mass checks), and [measurement tools](07-measurement-tools.md) (for dimensions). Also see the [design folder](../design/README.md).
**Time:** 15-25 h to model simple parts confidently

## Core ideas

- A **parametric model** stores dimensions and constraints. Change a dimension and the part updates.
- A **sketch** is a 2D profile on a plane. Fully define a sketch with dimensions and relations so it does not move unexpectedly.
- An **extrude** pulls a sketch into 3D to a given depth. A **cut** removes material. A **fillet** rounds an edge.
- A **feature tree** lists the steps in order. A later step can depend on an earlier one, so rebuild errors often come from ordering.
- An **assembly** places parts together with **mates** (such as coincident faces or concentric holes).
- **Mass properties** give volume, mass, and center of gravity. They depend on the density you assign to the material.

Free alternatives:

- **FreeCAD**, free and open source, is a parametric 3D modeler. Download it from [freecad.org](https://www.freecad.org/). Its Part and Sketcher workbenches cover sketch, extrude, fillet, and mass properties.
- **Onshape**, a browser-based CAD tool, has a free plan. Its [pricing page](https://www.onshape.com/en/pricing) says the free plan is for non-commercial use and that all documents on it are public. Use it for practice models only.

The same extrude and fillet workflow works in all three programs. Learn one well, then pick up the others.

## Key equations

Mass of a solid part with density $\rho$ (kg/m$^3$) and volume $V$ (m$^3$):

$$m = \rho V$$

For a rectangular plate of length $L$, width $W$, and thickness $t$ (all m):

$$V = L W t$$

Typical densities: aluminum about 2700 kg/m$^3$, steel about 7850 kg/m$^3$.

## Worked example

**Given:** An aluminum bracket plate, 200 mm long, 100 mm wide, and 6 mm thick. Take aluminum density as 2700 kg/m$^3$ (typical).

**Find:** The mass of the plate. Then check the mass the CAD tool reports.

**Assumptions:** A flat rectangular plate. No holes, fillets, or chamfers. The model uses the density you set.

**Solution (run in Python):**

```python
rho_al = 2700.0                   # kg/m^3, typical aluminum
L, W, T = 0.200, 0.100, 0.006     # m
vol = L * W * T
mass = rho_al * vol
print("volume =", vol, "m^3, mass =", mass, "kg")
```

Output:

```
volume = 0.00012000000000000003 m^3, mass = 0.32400000000000007 kg
```

**Answer:** $V = 1.20 \times 10^{-4}$ m$^3$ and $m = 0.324$ kg.

**Sanity check:** $200 \times 100 \times 6 = 120\,000$ mm$^3$, which is $120$ cm$^3$. Aluminum is about $2.7$ g/cm$^3$, so $120 \times 2.7 = 324$ g, or $0.324$ kg. That matches the calculation.

## Practice

1. Model a 300 mm by 200 mm by 10 mm aluminum plate in FreeCAD or Onshape. Check its volume in the tool and compare it with $0.3 \times 0.2 \times 0.01$ m$^3$.
2. Compute the mass of that plate in aluminum, using 2700 kg/m$^3$. Give the answer in kg.
3. Repeat the calculation for steel at 7850 kg/m$^3$. Give the answer in kg to two decimals.
4. Add a 10 mm fillet to one vertical edge of the plate. Explain why the volume changes only slightly.
5. Name two constraints that fully define a rectangle sketch.

<details><summary>Answers</summary>

1. Volume $6.0 \times 10^{-4}$ m$^3$ (600 000 mm$^3$). Check that the tool agrees.
2. 1.62 kg
3. 4.71 kg
4. The fillet removes a tiny triangle-like sliver of material. Answers will vary in wording.
5. Answers will vary. Examples: two side lengths, plus a corner position relative to the origin.

</details>

## Common mistakes

- Leaving the density at the tool's default instead of the real material value.
- Under-constraining a sketch, so a dimension moves when you did not expect.
- Building features in an order that makes a later edit fail.
- Forgetting units. Confirm the tool's unit setting before you enter numbers.
- Trusting the model without checking one dimension and one mass by hand.

## Go deeper

- [FreeCAD](https://www.freecad.org/) by the FreeCAD project: free open-source parametric CAD. Start with its download and tutorial pages.
- [Onshape pricing](https://www.onshape.com/en/pricing) by Onshape: the free plan terms and the public-document rule.
- [*NIST Special Publication 811*](https://www.nist.gov/pml/special-publication-811) by NIST: the SI guide for consistent units in models and drawings.
- Related: [Measurement tools](07-measurement-tools.md), [shop tools](08-shop-tools.md), [design folder](../design/README.md).
- [Tools reference](reference.md): the lookup sheet for this topic.
