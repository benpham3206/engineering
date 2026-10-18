# Factor of safety and failure

**Type:** lesson

A part fails when the stress in it is too high for the material. Engineers do not design to the edge of failure. They design with a factor of safety (FoS), a margin that covers unknown loads, material variation, and manufacturing error. This lesson defines stress, shows how to compare it with a material strength, and introduces two failure checks, the maximum shear and von Mises criteria, for parts under more than one stress.

**Prerequisites:** [01 Design process](01-design-process.md), and the force and equilibrium lessons in [physics](../physics/README.md) and the stress-strain basics in [materials](../materials/README.md)
**Time:** 6-10 h

## Core ideas

- **Stress** is force per unit area inside a material, written $\sigma$ for normal stress (pulling or pushing) and $\tau$ for shear stress (sliding one layer past another). Stress is what the material feels, not the load on the outside of the part.
- **Yield strength** $S_y$ is the stress at which a ductile material starts to deform permanently. Typical steel values are a few hundred megapascals.
- **Ultimate strength** $S_u$ is the highest stress the material reaches before breaking in a tension test.
- **Ductile** materials, such as most structural steels, yield and stretch before breaking. **Brittle** materials, such as cast iron and glass, break with little warning.
- **Factor of safety** is the ratio of a material's strength to the stress in the part. A design with FoS 2 can carry twice the stress before the chosen strength limit is reached.
- **Failure criterion** is the rule that combines several stresses into one number to compare with a strength. Simple parts use one stress. Real parts often need a criterion.

## Choosing a factor of safety

FoS is not a fixed number. It depends on how well you know the loads, the material, and the consequence of failure. Higher FoS is used when loads are uncertain, when the material varies, when failure is dangerous, or when inspection is hard. A common starting range for static steel design is around 1.5 to 3, but codes, industries, and client requirements set the real value. Always state the FoS and the reason for it on the drawing or calculation.

A large FoS is not automatically a good design. Extra material costs money and adds mass. Choose the lowest FoS that you can justify.

## Key equations

Normal stress in a rod or bar under axial load $F$ and cross-sectional area $A$:

$$
\sigma = \frac{F}{A}
$$

Area of a round bar of diameter $d$:

$$
A = \frac{\pi d^2}{4}
$$

Factor of safety for a ductile material with yield strength $S_y$:

$$
n = \frac{S_y}{\sigma}
$$

Maximum shear stress for a plane state with principal stresses $\sigma_1$ and $\sigma_3$ (Tresca criterion):

$$
\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2}
$$

Von Mises equivalent stress for plane stress with normal stresses $\sigma_x$, $\sigma_y$ and shear $\tau_{xy}$:

$$
\sigma_{vm} = \sqrt{\sigma_x^2 - \sigma_x \sigma_y + \sigma_y^2 + 3\tau_{xy}^2}
$$

Factor of safety using von Mises (ductile):

$$
n = \frac{S_y}{\sigma_{vm}}
$$

Principal stresses for plane stress:

$$
\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}
$$

Units: stress and strength in MPa (megapascals, equal to N/mm$^2$). US customary: psi or ksi (1 MPa is about 145 psi). Force in N (or lbf), area in mm$^2$ (or in$^2$).

Typical yield strength used in this lesson: $S_y = 350$ MPa (about 51 ksi). This is a typical value for a plain carbon steel, not a guarantee. Use the data sheet for the real material.

## Worked example

A steel rod of diameter 12 mm is pulled by an axial load of 20 kN. The steel has yield strength 350 MPa. Find the stress, the factor of safety, and whether the load is safe at FoS 2.

**Given.** $d = 12$ mm, $F = 20$ kN $= 20\,000$ N, $S_y = 350$ MPa.

**Find.** $\sigma$, $n$, and the largest load allowed at $n = 2$.

**Assumptions.** Load is steady, uniform across the section, and purely axial. The rod has no notches or holes. Yield is the failure limit.

**Solution.**

Step 1. Area: $A = \dfrac{\pi (12)^2}{4} = 113.1$ mm$^2$.

Step 2. Stress: $\sigma = \dfrac{20\,000}{113.1} = 176.8$ MPa.

Step 3. Factor of safety: $n = \dfrac{350}{176.8} = 1.98$.

Step 4. Largest load at $n = 2$: $F_{\text{allow}} = \dfrac{S_y}{n} A = \dfrac{350}{2} \times 113.1 = 19\,790$ N $\approx 19.8$ kN.

**Answer.** Stress 176.8 MPa (about 25.6 ksi). FoS 1.98. At a required FoS of 2, the load must stay below about 19.8 kN (4.45 kip), so 20 kN is slightly too high.

**Sanity check.** The stress is about half of yield, which should give FoS near 2, and it does. The result is just under 2, so the rod is marginal. A slightly thicker rod, such as 13 mm, would give more margin.

## Second worked example: von Mises

A point in a machine frame has $\sigma_x = 120$ MPa, $\sigma_y = 40$ MPa, and $\tau_{xy} = 30$ MPa. The material has $S_y = 350$ MPa. Find the von Mises stress and FoS.

**Solution.**

$\sigma_{vm} = \sqrt{120^2 - 120 \times 40 + 40^2 + 3 \times 30^2} = \sqrt{13\,900} = 117.9$ MPa.

$n = \dfrac{350}{117.9} = 2.97$.

**Answer.** Von Mises stress 117.9 MPa, FoS 2.97.

**Sanity check.** The von Mises stress (117.9 MPa) is close to the largest normal stress (120 MPa), which is reasonable because the shear adds to the effect while the 40 MPa stress partly offsets it. Check the principal stresses from the equation above: they are 130 and 30 MPa, so the Tresca shear is $(130 - 30)/2 = 50$ MPa. The two criteria give different numbers, and the difference is expected.

## Checklist

- Is the stress computed from the actual load and the correct area?
- Is the material strength the yield strength for a ductile part, or the ultimate strength for a brittle one?
- Is FoS stated and justified, not picked by habit?
- For a part under several stresses, is a failure criterion used instead of one stress?
- Are units consistent: N and mm$^2$ give MPa?

## Practice

1. A round rod of diameter 10 mm carries an axial load of 15 kN. Find the stress in MPa to one decimal place.
2. Using the stress from question 1 and $S_y = 350$ MPa, find FoS to two decimal places.
3. In plane stress, $\sigma_x = 80$ MPa, $\sigma_y = 20$ MPa, $\tau_{xy} = 40$ MPa. Find the larger principal stress in MPa.
4. For the state in question 3, find the maximum shear stress (Tresca) in MPa.

<details><summary>Answers</summary>

1. 191.0
2. 1.83
3. 100.0
4. 50.0

</details>

## Common mistakes

- Using the load as if it were the stress. Stress needs the area.
- Using the wrong area, such as the outside diameter of a hollow part, without subtracting the bore.
- Comparing a ductile part's stress with ultimate strength instead of yield.
- Applying a single-stress check to a part that has shear and normal stress together.
- Quoting an FoS without saying what the strength is based on.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: a free hub that includes mechanics of materials and stress analysis.
- [OpenStax University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/1-introduction) by OpenStax at Rice University: free physics text for forces, equilibrium, and the basics behind stress.
- [NIST, Metric (SI) program](https://www.nist.gov/pml/owm/metric-si) by NIST: official SI unit guidance, useful for keeping MPa, N, and mm consistent.
