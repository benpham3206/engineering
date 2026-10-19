# Thermodynamics: entropy, the second law, and cycles

**Type:** lesson

The first law says energy is conserved. The second law says some energy conversions are impossible, and it sets the best efficiency any engine can reach.

**Prerequisites:** [Thermodynamics: properties, work, heat, and the first law](08-thermo-first-law.md) (work, heat, the first law, and ideal gas air), [Single-variable calculus](../math/03-single-variable-calculus.md) (entropy as an integral, natural logarithm)
**Time:** 8-12 h

## Core ideas

### Why the first law is not enough

- The first law allows any energy conversion that conserves total energy. It does not say which direction a process runs.
- Heat flows from hot to cold on its own. It does not flow from cold to hot unless work is supplied.
- A hot object left alone cools down. The reverse, a cold object spontaneously heating a hot one, never happens. The second law explains this direction.

### Reversible and irreversible processes

- A **reversible process** can be reversed with no net change to the system or its surroundings. It happens slowly, with no friction and no large temperature differences. It is an idealization.
- An **irreversible process** cannot be undone without leaving a change behind. Friction, unrestrained expansion, and heat flow across a large temperature difference are irreversible.
- Every real process is irreversible to some degree. Reversible processes are useful because they set the limits.

### Entropy

- **Entropy** $S$ is a property that measures how energy is spread out or how many microscopic arrangements are possible. It is measured in joules per kelvin (J/K).
- In general, $\Delta S = \int \delta Q_\text{rev}/T$, where $\delta Q_\text{rev}$ is heat added along a reversible path. When heat $Q$ moves reversibly at one constant temperature $T$ (in kelvin), such as with a reservoir, this reduces to $\Delta S = Q/T$.
- The **entropy of an isolated system never decreases**. It stays the same for reversible processes and increases for irreversible ones. This is one common form of the second law.
- Entropy can decrease inside a part of the universe, such as a refrigerator cooling its inside. The total entropy of the system plus surroundings still does not decrease.

### Statements of the second law

- **Kelvin-Planck statement.** No device can convert heat from a single reservoir completely into work in a repeating cycle.
- **Clausius statement.** No device can move heat from a cold body to a hot body without work supplied from outside.
- Both statements are equivalent. Breaking one breaks the other.

### Heat engines and efficiency

- A **heat engine** takes heat $Q_H$ from a hot reservoir, produces work $W$, and rejects heat $Q_C$ to a cold reservoir.
- The **thermal efficiency** is $\eta = W/Q_H$. It is dimensionless and often written as a percentage.
- The **Carnot cycle** is a reversible cycle between two reservoirs. No engine working between the same two temperatures can be more efficient.

### Refrigerators and heat pumps

- A **refrigerator** moves heat from a cold space to a warmer one, using work. Its performance is measured by the **coefficient of performance** $\text{COP}_R = Q_L/W$.
- A **heat pump** does the same job, but its goal is heating the warm side. Its coefficient is $\text{COP}_{HP} = Q_H/W$.

### Ideal cycles

- An **ideal cycle** is a model that replaces real processes with simpler ones. It shows the main effects of compression, heat addition, expansion, and heat rejection.
- The **Otto cycle** is the ideal model of a spark-ignition engine. It has two adiabatic strokes and two constant-volume heat steps. Its efficiency depends only on the compression ratio $r$.
- The **Brayton cycle** is the ideal model of a gas turbine. It has two adiabatic steps and two constant-pressure steps. Its efficiency depends only on the pressure ratio.
- The **Rankine cycle** is the ideal model of a steam power plant. It uses a liquid and vapor working fluid. It needs steam table data, so this lesson does not work a Rankine example. To study it further, get water and steam properties from a steam table or from the free [CoolProp](http://www.coolprop.org/) library in Python, which replaces steam tables in code (see [Free engineering software](../tools/09-free-software.md)).

## Key equations

In general, $\Delta S = \int \delta Q_\text{rev}/T$. For heat transfer at one constant temperature $T$, such as with a reservoir:

$$
\Delta S = \frac{Q}{T}
$$

- $\Delta S$ is the entropy change (J/K).
- $Q$ is the heat transferred (J), positive when added to the substance at that temperature.
- $T$ is the absolute temperature (K).

Carnot efficiency for an engine between a hot reservoir at $T_H$ and a cold reservoir at $T_C$:

$$
\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}
$$

- $T_H$ and $T_C$ are absolute temperatures (K). Both must be in kelvin.

Ideal Otto cycle efficiency (cold air standard):

$$
\eta_{\text{Otto}} = 1 - \frac{1}{r^{\,k-1}}
$$

- $r$ is the compression ratio, the ratio of maximum to minimum cylinder volume.
- $k = 1.4$ for air.

Ideal Brayton cycle efficiency (cold air standard):

$$
\eta_{\text{Brayton}} = 1 - \left(\frac{1}{r_p}\right)^{(k-1)/k}
$$

- $r_p$ is the pressure ratio of the compressor.

Carnot refrigerator coefficient of performance:

$$
\text{COP}_R = \frac{Q_L}{W} = \frac{T_L}{T_H - T_L}
$$

- $Q_L$ is the heat removed from the cold space (J).
- $T_L$ is the cold space temperature (K).
- $T_H$ is the warm space temperature (K).

## Worked example

**Problem.** A reversible heat engine operates between a hot reservoir at $T_H = 800$ K and a cold reservoir at $T_C = 300$ K. It absorbs $Q_H = 1000$ J from the hot reservoir each cycle. Find the efficiency, the work per cycle, the heat rejected to the cold reservoir, and the net entropy change of the two reservoirs.

**Given:**

- $T_H = 800$ K
- $T_C = 300$ K
- $Q_H = 1000$ J per cycle

**Find:** $\eta$, $W$, $Q_C$, and the net entropy change of the two reservoirs.

**Assumptions:** The engine is reversible, so it is a Carnot engine. Each cycle is steady.

**Solution.**

1. Efficiency: $\eta = 1 - T_C/T_H = 1 - 300/800 = 0.625$, or 62.5%.
2. Work per cycle: $W = \eta\,Q_H = 0.625(1000) = 625$ J.
3. Heat rejected: $Q_C = Q_H - W = 1000 - 625 = 375$ J.
4. Entropy change of the hot reservoir (it loses heat): $\Delta S_H = -Q_H/T_H = -1000/800 = -1.25$ J/K.
5. Entropy change of the cold reservoir (it gains heat): $\Delta S_C = Q_C/T_C = 375/300 = 1.25$ J/K.
6. Net entropy change: $\Delta S_{\text{net}} = -1.25 + 1.25 = 0$ J/K.

**Answer.** The efficiency is 62.5%. The work per cycle is 625 J. The heat rejected is 375 J. The net entropy change is 0 J/K.

**Sanity check.** $Q/T$ applies here because each reservoir stays at constant temperature. The net entropy change is zero, as expected for a reversible engine. If you replace the engine with a real one, the net change becomes positive. The efficiency is also less than 1, as the second law requires.

## Practice

1. A Carnot engine works between $T_H = 600$ K and $T_C = 300$ K. Find its efficiency.
2. An ideal Otto cycle has a compression ratio $r = 8$ and uses air with $k = 1.4$. Find its efficiency.
3. A reversible refrigerator keeps a space at $270$ K in surroundings at $300$ K. Find its COP.
4. In a heat transfer, $1000$ J of heat leaves a reservoir at $500$ K and enters a reservoir at $300$ K. Find the net entropy change, in J/K.
5. An ideal Brayton cycle has a pressure ratio of $10$ and uses air with $k = 1.4$. Find its efficiency.

<details><summary>Answers</summary>

1. $50\%$
2. $56.5\%$
3. $9.0$
4. $+1.33$ J/K
5. $48.2\%$

</details>

## Common mistakes

- Using Celsius temperatures in the Carnot formula. The ratio $T_C/T_H$ needs absolute temperatures in kelvin.
- Writing the Carnot efficiency as $T_H/T_C$ or as $1 - T_H/T_C$. The cold temperature goes on top.
- Thinking entropy must go down because a fridge cools its inside. The surroundings gain more entropy than the inside loses.
- Using the Otto or Brayton formula with a steam or real-gas working fluid. Those formulas assume the cold air standard model.
- Forgetting that the efficiency of any real engine is lower than the Carnot value between the same two reservoirs.

## Go deeper

- [Introduction to the Second Law of Thermodynamics and Entropy (Chapter 4), University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/4-introduction) by OpenStax: reversibility, heat engines, refrigerators, the Carnot cycle, and entropy, free to read.
- [The Second Law of Thermodynamics and Entropy](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/second-law-entropy/) by NASA Glenn Research Center: reversible and irreversible processes, and entropy with a worked heat-flow example.
- [Introduction to Thermodynamics (Chapter 3), University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/3-introduction) by OpenStax: the first law and ideal gas processes, which this lesson builds on.
- [Thermal-fluids reference](reference-thermofluids.md): the lookup sheet for this topic.
