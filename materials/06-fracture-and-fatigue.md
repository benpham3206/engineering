# Failure: fracture and fatigue

**Type:** lesson

Most structures do not fail because the load is too big on day one. They fail because a small crack grows, slowly or suddenly, until the remaining material cannot carry the load. Fracture is the sudden case. Fatigue is the case where repeated loading grows a crack over many cycles.

**Prerequisites:** [Mechanical properties](03-mechanical-properties.md), [Material classes](05-material-classes.md)
**Time:** 8-10 h

## Core ideas

- A **flaw** is any crack, void, inclusion, or scratch in a material. Real parts always have flaws.
- A **stress concentration** is a spot where the stress is much higher than the average, such as near a sharp corner or hole. Flaws and sharp corners act as stress concentrators.
- **Brittle fracture** happens with little plastic deformation. The crack runs fast, and the part breaks suddenly. Ceramics, glass, and some cold steels fail this way.
- **Ductile fracture** happens after significant yielding. The part necks, tears, and absorbs energy. Most structural metals at room temperature fail this way.
- **Fracture toughness** ($K_{IC}$) is the material's resistance to crack growth. A high value means the material tolerates bigger flaws.

### Fracture mechanics in plain words

- The **stress intensity factor** $K$ measures how strongly the stress near a crack tip is amplified. It depends on the applied stress, the crack size, and the part geometry.
- A crack grows when $K$ reaches $K_{IC}$. So, for a given material and stress, there is a **critical crack size**. Cracks smaller than this are safe, and cracks larger than this grow.
- This is why inspection matters. A part can be safe with small flaws and fail with the same stress on a large one.

### Fatigue

- **Fatigue** is failure under repeated or fluctuating stress, often at stress levels well below the yield strength.
- Fatigue has three stages: crack **initiation** (often at a surface scratch or pore), slow crack **propagation** over many cycles, and sudden **final fracture** when the remaining section is too small.
- Fatigue life is often shown as an S-N curve, a plot of stress amplitude against the number of cycles to failure. Many steels and titanium alloys have an endurance limit, a stress below which they last indefinitely. Aluminum alloys usually do not have a clear endurance limit.
- Surface finish, corrosion, residual stress, and notches all lower fatigue life a lot.

## Key equations

The stress intensity factor for an edge or center crack of length $a$ in a plate under tensile stress $\sigma$ is

$$K = Y \sigma \sqrt{\pi a}$$

where:

- $K$ is the stress intensity factor (MPa $\sqrt{\text{m}}$)
- $Y$ is a geometry factor (dimensionless; about 1.12 for an edge crack in a wide plate)
- $\sigma$ is the applied stress (MPa)
- $a$ is the crack length (m)

Fracture occurs when $K = K_{IC}$. Solving for the critical crack length gives

$$a_c = \frac{1}{\pi}\left(\frac{K_{IC}}{Y \sigma}\right)^2$$

Fatigue stress range and ratio, for a cyclic load that swings between $\sigma_{\max}$ and $\sigma_{\min}$:

$$\sigma_a = \frac{\sigma_{\max} - \sigma_{\min}}{2}, \qquad R = \frac{\sigma_{\min}}{\sigma_{\max}}$$

where $\sigma_a$ is the stress amplitude (MPa) and $R$ is the stress ratio (dimensionless).

## Worked example

**Given:** An edge crack of length $a = 2$ mm sits in a wide steel plate under a tensile stress of $\sigma = 200$ MPa. Geometry factor $Y = 1.12$. The fracture toughness of this steel is $K_{IC} = 40$ MPa $\sqrt{\text{m}}$.

**Find:** (a) the stress intensity factor $K$, and (b) whether the crack will grow.

**Assumptions:** Linear elastic fracture mechanics, plane strain, and a wide plate. Typical textbook values.

**Solution:**

1. Convert the crack length: $a = 0.002$ m.
2. Compute $\sqrt{\pi a} = \sqrt{0.0062832} = 0.07927$ m$^{1/2}$.
3. Compute $K = 1.12 \times 200 \times 0.07927 = 17.8$ MPa $\sqrt{\text{m}}$.
4. Compare with the toughness: $17.8 < 40$, so the crack does not grow fast.
5. Critical crack length at this stress: $a_c = \frac{1}{\pi}\left(\frac{40}{1.12 \times 200}\right)^2 = 0.01015$ m $\approx 10.2$ mm.

**Answer:** (a) $K \approx 17.8$ MPa $\sqrt{\text{m}}$. (b) The crack is stable. It would only become critical at a length of about 10 mm.

**Sanity check:** A 2 mm crack is small compared with a 10 mm critical length, so a stable result makes sense. A 10 mm crack at the same stress would sit right at the edge of fracture.

## Practice

1. Find $K$ for $Y = 1.12$, $\sigma = 150$ MPa, and $a = 2$ mm. Use the worked example method.
2. Using $K_{IC} = 40$ MPa $\sqrt{\text{m}}$, $Y = 1.12$, and $\sigma = 200$ MPa, find the critical crack length in mm.
3. A part cycles between $\sigma_{\max} = 300$ MPa and $\sigma_{\min} = 100$ MPa. Find the stress amplitude $\sigma_a$ in MPa and the ratio $R$.
4. Why can a fatigue crack form in a part whose peak stress is below the yield strength?
5. Name the three stages of fatigue failure in order.

<details><summary>Answers</summary>

1. about 13.3 MPa $\sqrt{\text{m}}$
2. about 10.2 mm
3. $\sigma_a = 100$ MPa, $R = 0.33$
4. Repeated stress can grow a small crack over many cycles, and the stress concentration at the crack tip is much higher than the average stress.
5. Initiation, propagation, final fracture

</details>

## Common mistakes

- Using the crack length in mm inside the $K$ formula. Convert to metres first, so $\sqrt{\pi a}$ comes out in m$^{1/2}$.
- Forgetting the geometry factor $Y$. Results without it can be off by tens of percent.
- Treating fatigue as a stress problem only. Surface finish, corrosion, and notches can matter more than the average stress.
- Assuming that a material with high yield strength has high fracture toughness. Strength and toughness are separate properties.
- Assuming an endurance limit exists for every metal. Many non-ferrous alloys do not have one.

## Go deeper

- [Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) by MIT OpenCourseWare: stress, strain, and the mechanical behavior of materials under load.
- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: how microstructure and defects control failure.
- [Mechanical properties](03-mechanical-properties.md): the basic tests and definitions behind this lesson.
