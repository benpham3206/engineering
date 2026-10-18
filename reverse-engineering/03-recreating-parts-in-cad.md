# Recreating parts in CAD

**Type:** lesson

Recreating a part in CAD (computer-aided design) means building a digital model of it from your measurements and photos. The goal is not just to match the shape. The goal is to rebuild the design intent: the reasons the features are where they are, so that the model still makes sense when a dimension changes.

**Prerequisites:** [Teardowns](01-teardowns.md), [Measuring existing parts](02-measuring-existing-parts.md)
**Time:** 8-12 h

## Core ideas

- **Geometry** is the shape: where the surfaces are. **Design intent** is why the shape is what it is: which surface must stay parallel, which hole must line up with a mating part, which dimension is set by a fastener.
- A **parametric model** stores features and their relationships, not just the final shape. Change a driving dimension and the rest of the model updates.
- A **sketch** is a 2D profile drawn on a plane. An **extrude** pushes a sketch into 3D. A **revolve** spins a sketch around an axis. A **hole** feature cuts a standard hole into a face.
- A **constraint** is a rule in a sketch, such as "this line is horizontal" or "these two circles share a center." A **dimension** sets a size. A fully constrained sketch does not move unless you change a dimension on purpose.
- A **reference plane** or **datum** is a flat or axis used as the starting point for measuring. Mating parts usually agree on datums, so the datums are a clue to the original design.
- Build from the most important feature first. For a plate with holes, start with the plate outline and the hole pattern that locates it, then add small details like fillets and chamfers.
- A **fillet** rounds an inside or outside corner. Fillets reduce stress concentration, so they often show up where a part flexes. Missing fillets in a model are a sign of missed design intent.
- Check your model against the original. Compare volumes, weights, and key distances. A mass check is a simple way to catch a wrong thickness.

### Design intent checklist for each feature

- [ ] What does this feature mate with, and what dimension does that mating part set?
- [ ] Which surfaces must be parallel or square to each other?
- [ ] Which dimension is the driving one, and which ones follow from it?
- [ ] Does the feature sit on a standard size (hole diameter, thread, bolt circle)?
- [ ] Would a designer have added a fillet or chamfer here, and why?

## Key equations

Volume of a solid made from simple shapes, where $V$ is the total volume in cubic millimeters, $V_i$ is the volume of each piece added, and $V_j$ is the volume of each hole or cut removed:

$$V = \sum_i V_i - \sum_j V_j$$

Volume of a cylinder hole, where $r$ is the radius in millimeters and $h$ is the depth in millimeters:

$$V_{\text{hole}} = \pi r^2 h$$

Mass from volume, where $m$ is mass in grams, $\rho$ is density in grams per cubic centimeter (g/cm$^3$), and $V$ is volume in cubic centimeters:

$$m = \rho V$$

Typical densities (standard textbook values, which vary a little by alloy):

- Low-carbon steel: about 7.85 g/cm$^3$
- Aluminum alloy (such as 6061): about 2.70 g/cm$^3$

Unit note: 1 cm$^3$ = 1000 mm$^3$.

## Worked example

**Given:** A flat mounting plate is 60 mm long, 40 mm wide, and 5 mm thick. It has four through holes of 6 mm diameter, all through the thickness.

**Find:** (a) the net volume of the plate in cubic centimeters, and (b) the mass if the plate is steel, and if it is aluminum.

**Assumptions:** The plate is a solid rectangle with four plain through holes and no fillets. The holes pass fully through the 5 mm thickness. Typical densities apply.

**Solution:**

(a) Plate volume, before holes:

$$V_{\text{plate}} = 60 \times 40 \times 5 = 12000 \text{ mm}^3$$

Each hole has radius $r = 3$ mm, so the volume of one hole is:

$$V_{\text{hole}} = \pi (3)^2 (5) = 141.37 \text{ mm}^3$$

Four holes remove $4 \times 141.37 = 565.49$ mm$^3$. Net volume:

$$V = 12000 - 565.49 = 11434.51 \text{ mm}^3 = 11.43 \text{ cm}^3$$

(b) Steel mass:

$$m_{\text{steel}} = 7.85 \times 11.43 = 89.76 \text{ g}$$

Aluminum mass:

$$m_{\text{Al}} = 2.70 \times 11.43 = 30.87 \text{ g}$$

**Answer:** The net volume is 11.43 cm$^3$. The mass is about 89.8 g as steel and about 30.9 g as aluminum.

**Sanity check:** A 5 mm thick plate is about 0.5 cm thick, and its footprint is 24 cm$^2$ before holes. Volume should be near $24 \times 0.5 = 12$ cm$^3$, which matches 11.43 cm$^3$ after removing four small holes. A mass near 90 g for steel is in the right range for a plate that size.

If the measured mass of the real part is 89 g, the steel answer fits. If it is 31 g, the material is probably aluminum. This is how a mass check helps you choose between material guesses.

## Practice

1. A plate is 80 mm by 50 mm by 4 mm with no holes. What is its volume in cubic millimeters?
2. A 10 mm diameter hole goes 4 mm deep through a part. What is its volume in cubic millimeters, rounded to 0.1 mm$^3$?
3. A solid part has a net volume of 42.0 cm$^3$. What is its mass in grams as low-carbon steel?
4. A part has a net volume of 18.5 cm$^3$. What is its mass in grams as aluminum?
5. A part weighs 81.0 g as steel. What is its volume in cubic centimeters, rounded to 0.01 cm$^3$?

<details><summary>Answers</summary>

1. 16000
2. 314.2
3. 329.7
4. 49.95
5. 10.32

</details>

## Common mistakes

- Modeling the shape without any dimension relationships, so a single change breaks the whole part.
- Using a rounded measurement from a steel rule as a design dimension without checking against a standard size.
- Forgetting to subtract holes from the volume when checking mass, which overstates the weight.
- Mixing units, such as cubic millimeters with grams per cubic centimeter. Convert to cm$^3$ before multiplying by density.
- Leaving out fillets and chamfers because they look small. They often explain where a part was machined or molded.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by LibreTexts: a free library of engineering bookshelves for drawing, mechanics, and design.
- [Mechanical Engineering bookshelf](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering) by LibreTexts: free books on design and machine elements.
- [SI units and the metric system](https://www.nist.gov/pml/owm/metric-si) by NIST: the official guide to SI units, useful when you convert between mm, cm, and grams.
- See also the [design folder](../design/README.md) for the design process that sits behind the features you rebuild.
