# Failure: creep and corrosion

**Type:** lesson

Two slow failure modes often decide how long a part lasts. Creep is the slow deformation of a material under steady load, mostly at high temperature. Corrosion is the chemical or electrochemical attack that eats a material away. Both work over months or years, so they are easy to miss in short tests.

**Prerequisites:** [Mechanical properties](03-mechanical-properties.md), [Failure: fracture and fatigue](06-fracture-and-fatigue.md)
**Time:** 6-8 h

## Core ideas

### Creep

- **Creep** is time-dependent deformation under a constant load. The part keeps stretching or sagging even though the stress does not change.
- Creep matters when the operating temperature is above about 0.4 times the absolute melting temperature (in kelvin). Turbine blades, steam pipes, and bolts in hot engines are typical cases.
- A creep curve has three stages. **Primary creep** starts fast and slows down. **Secondary creep** (steady-state) runs at a nearly constant rate. **Tertiary creep** speeds up as the part thins and cavities form, and ends in rupture.
- Creep rate rises steeply with temperature and with stress. A small rise in temperature can cut the life of a part a lot.
- Polymers creep at much lower temperatures than metals. Their glass transition temperature is a useful warning level.

### Corrosion

- **Corrosion** is the loss of material by a chemical or electrochemical reaction with the environment.
- Corrosion is electrochemical in most metals. An **anode** (where the metal dissolves) and a **cathode** (where a reduction reaction happens) are joined through an electrolyte such as water, which lets current flow.
- **Galvanic corrosion** happens when two different metals touch in an electrolyte. The less noble metal corrodes faster. Aluminum bolts in steel plates are a classic case.
- **Pitting** is local, deep attack that can perforate thin walls even when the average loss is small.
- **Crevice corrosion** happens in gaps, under gaskets, and at lap joints, where the local chemistry becomes aggressive.
- **Stress corrosion cracking** combines a tensile stress with a corrosive environment, and it can crack a part at stresses well below its yield strength.

### Ways to fight both

- For creep: choose a material with a high melting point, use alloys with fine precipitates, and design for lower stress or temperature.
- For corrosion: choose a resistant alloy (such as stainless steel), add coatings, use cathodic protection, avoid dissimilar metal contact, and design to drain water and avoid crevices.

## Key equations

Steady-state creep rate is often modeled with an Arrhenius-type law:

$$\dot{\varepsilon} = A\, \sigma^{n} \exp\!\left(-\frac{Q}{R T}\right)$$

where:

- $\dot{\varepsilon}$ is the steady-state creep strain rate (1/s)
- $A$ is a material constant
- $\sigma$ is the applied stress (MPa)
- $n$ is the stress exponent (dimensionless, often 3 to 8 for metals)
- $Q$ is the activation energy (J/mol)
- $R = 8.314$ J/(mol K) is the gas constant
- $T$ is the absolute temperature (K)

For two temperatures at the same stress, the ratio of creep rates is

$$\frac{\dot{\varepsilon}_2}{\dot{\varepsilon}_1} = \exp\!\left[\frac{Q}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$

Corrosion mass loss rate from Faraday's law, for a uniform corrosion current density $i$ (A/cm$^2$) on a metal of molar mass $M$ (g/mol) and valence $n$:

$$\text{mass rate} = \frac{i\, M}{n\, F}, \qquad \text{penetration rate} = \frac{\text{mass rate}}{\rho}$$

where $F = 96\,485$ C/mol is the Faraday constant and $\rho$ is the density (g/cm$^3$).

## Worked example

**Given:** Iron (molar mass $M = 55.85$ g/mol, valence $n = 2$, density $\rho = 7.87$ g/cm$^3$) corrodes uniformly in water with a corrosion current density of $i = 1.0 \times 10^{-5}$ A/cm$^2$. This value is an assumed example.

**Find:** (a) the mass loss rate in g/(cm$^2$ year), and (b) the penetration rate in mm/year.

**Assumptions:** Uniform corrosion, all current from iron dissolving as Fe to Fe$^{2+}$, and a constant current over one year.

**Solution:**

1. Mass rate per second: $\dfrac{i M}{n F} = \dfrac{(1.0 \times 10^{-5})(55.85)}{(2)(96\,485)} = 2.90 \times 10^{-9}$ g/(cm$^2$ s).
2. Seconds per year: $365.25 \times 24 \times 3600 = 3.156 \times 10^{7}$ s.
3. Mass loss per year: $2.90 \times 10^{-9} \times 3.156 \times 10^{7} = 0.0913$ g/(cm$^2$ year).
4. Penetration rate: $0.0913 / 7.87 = 0.0116$ cm/year $= 0.116$ mm/year.

**Answer:** (a) about 0.091 g/(cm$^2$ year). (b) about 0.12 mm/year.

**Sanity check:** Iron wall loss of about 0.1 mm per year means a 3 mm plate lasts about 26 years under this uniform attack (3 / 0.116). That is the right order of magnitude for mild steel in mild water, so the result is plausible. Pitting would make the local loss much deeper.

## Practice

1. Using the worked example, what is the penetration rate in mm/year if the corrosion current density doubles to $2.0 \times 10^{-5}$ A/cm$^2$?
2. A creep rate at 900 K is $\dot{\varepsilon}_1$. With $Q = 200$ kJ/mol, what is the ratio $\dot{\varepsilon}_2 / \dot{\varepsilon}_1$ when the temperature rises to 1000 K at the same stress? (Use $R = 8.314$ J/(mol K).)
3. Name the three stages of a typical creep curve in order.
4. Two metals touch in seawater. Which one will corrode faster, the anode or the cathode?
5. Give one design change that reduces crevice corrosion.

<details><summary>Answers</summary>

1. about 0.23 mm/year
2. about 14.5
3. Primary, secondary (steady-state), tertiary
4. The anode (the less noble metal that dissolves)
5. Any one of: seal or fill the gap, use a welded joint instead of a lap joint, design to drain water

</details>

## Common mistakes

- Using Celsius instead of kelvin in the Arrhenius term. Always use absolute temperature.
- Forgetting the sign of $Q/RT$ or flipping the temperature ratio. Higher temperature gives a larger creep rate.
- Treating corrosion rate as a fixed number. It depends on temperature, pH, oxygen, chlorides, and flow.
- Assuming average corrosion is the whole story. Pitting can fail a thin wall long before the average loss looks serious.
- Mixing up mass rate and penetration rate. Dividing by density converts between them.

## Go deeper

- [Fundamentals of Materials Science](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/) by MIT OpenCourseWare: thermal activation, diffusion, and the energetics behind creep and corrosion.
- [Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/) by MIT OpenCourseWare: the chemical basis of reactions at material surfaces.
- [Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) by MIT OpenCourseWare: the stress and strain background needed for creep.
