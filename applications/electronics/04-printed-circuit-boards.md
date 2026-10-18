# Printed circuit boards

**Type:** lesson

A printed circuit board (PCB) is a laminated sheet that holds copper traces and connects the parts on it. Almost every electronic product uses one, and its layout sets how well the product carries current, handles noise, dissipates heat, and survives assembly. An engineer who understands layers, trace current, and layout rules can avoid the failures that show up only after the board is built.

**Prerequisites:** [Circuit basics](01-circuit-basics.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Heat transfer](../../physics/12-heat-transfer.md), [Material classes](../../materials/05-material-classes.md)
**Time:** 8-12 h

## Core ideas

### How it works

A typical board starts as a core of glass-reinforced epoxy laminate, usually FR-4, with a copper foil bonded to one or both faces. Etching removes the unwanted copper and leaves traces, which are thin copper paths that carry current between parts. Parts sit on pads, which are copper areas that solder joins to the leads or terminals. Holes called vias connect copper on different layers.

Multilayer boards stack several copper layers with insulating layers between them. Inner layers often hold ground and power planes, which are large copper sheets. Planes carry return current with low resistance and give signals a short return path. Copper weight describes the foil thickness. One ounce of copper per square foot is about 35 µm thick (nominal value), and 2 oz is about 70 µm.

The laminate matters too. FR-4 has a glass transition temperature Tg of roughly 130 to 180 °C (typical range), above which it softens and expands more. Higher-Tg materials cost more and tolerate lead-free reflow soldering better.

### Main parts

| Part | Role |
|---|---|
| Laminate (core and prepreg) | Electrical insulation and mechanical support. Prepreg is uncured resin that bonds the layers together. |
| Copper layers and planes | Traces carry signals and power. Planes carry return current and shield signals. |
| Vias | Plated holes that connect layers. Through vias, blind vias, buried vias, and microvias are the main types. |
| Pads and lands | Copper areas where parts solder. Their size and shape set the joint strength and the assembly yield. |
| Solder mask | A polymer coating that keeps solder off the traces and bridges between pads. |
| Silkscreen | Printed text and outlines for part identification. It is not conductive. |
| Surface finish | A coating over exposed copper pads, such as HASL, ENIG, or immersion silver, that protects copper and makes solder wet well. |

### Variants

- **Single-sided boards** have copper on one face. They are cheap and suit simple circuits with few crossings.
- **Double-sided boards** have copper on both faces and vias between them.
- **Multilayer boards** have four or more copper layers, and they are common for dense digital designs. Dense server and telecom boards can exceed ten layers.
- **Flexible and rigid-flex boards** use a polyimide base. They bend in products such as hinges and cameras.
- **Metal-core boards** have an aluminum base that carries heat out of LED and power parts.
- **High-frequency laminates** have a lower and more stable dielectric constant and loss, which suit radio and high-speed signals.

## Key equations

- Trace resistance: $R = \dfrac{\rho L}{w t}$, where $R$ is the resistance in ohms, $\rho$ is the copper resistivity in $\Omega\,\text{m}$, $L$ is the trace length in metres, $w$ is the trace width in metres, and $t$ is the copper thickness in metres.
- Copper resistivity at 20 °C: $\rho_{20} = 1.68 \times 10^{-8}\ \Omega\,\text{m}$, from standard reference tables.
- Temperature dependence of copper: $\rho(T) = \rho_{20}\left[1 + \alpha (T - 20\ \text{°C})\right]$, where $\alpha = 0.00393\ \text{K}^{-1}$ (typical value for copper).
- Ohm's law for the trace voltage drop: $V = I R$, where $V$ is in volts and $I$ is in amperes.
- Joule heating: $P = I^2 R$, where $P$ is the power in watts that heats the trace.
- Temperature rise from a thermal resistance: $\Delta T = P R_{th}$, where $\Delta T$ is the rise in kelvin above ambient and $R_{th}$ is the thermal resistance from the trace to ambient in K/W.
- Trace cross-section: $A = w t$, in square metres.

The current capacity of a trace is set by the temperature rise it can tolerate. IPC-2152, the 2009 standard for determining current-carrying capacity in printed board design, gives the relation between current, trace cross-section, internal or external position, and the board's thermal environment. It replaced the older IPC-2221 current charts. Use the standard's own equations or curves for a design decision. The worked example below uses a stated thermal resistance instead of a value from the standard.

## Worked example

**Given:** A 0.5 mm wide, 50 mm long trace of 1 oz copper (35 µm thick) on the outer layer of a board carries $I = 2\ \text{A}$. Assume the ambient temperature is 20 °C, copper resistivity is $\rho_{20} = 1.68 \times 10^{-8}\ \Omega\,\text{m}$, and $\alpha = 0.00393\ \text{K}^{-1}$. Assume a thermal resistance from trace to ambient of $R_{th} = 80\ \text{K/W}$. This value is an assumption chosen for the example, not a number taken from IPC-2152.

**Find:** (a) the trace resistance at 20 °C, (b) the steady temperature of the trace, and (c) the voltage drop along the trace at that temperature.

**Solution:**

1. Cross-section: $A = w t = (0.5 \times 10^{-3})(35 \times 10^{-6}) = 1.75 \times 10^{-8}\ \text{m}^2$.
2. Resistance at 20 °C: $R_{20} = \dfrac{\rho_{20} L}{A} = \dfrac{(1.68 \times 10^{-8})(0.050)}{1.75 \times 10^{-8}} = 0.048\ \Omega$.
3. Heat generated at 20 °C: $P = I^2 R_{20} = 4 \times 0.048 = 0.192\ \text{W}$. This gives $\Delta T \approx 80 \times 0.192 = 15.4\ \text{K}$.
4. Resistance rises with temperature, so iterate. At $T \approx 36\ \text{°C}$, $\rho = \rho_{20}[1 + 0.00393 \times 16] = 1.79 \times 10^{-8}\ \Omega\,\text{m}$, and $R = 0.051\ \Omega$. Then $P = 4 \times 0.051 = 0.204\ \text{W}$ and $\Delta T = 80 \times 0.204 = 16.4\ \text{K}$. The result settles at $T \approx 36\ \text{°C}$.
5. Voltage drop at 36 °C: $V = I R = 2 \times 0.051 = 0.10\ \text{V}$.

**Answer:** (a) $0.048\ \Omega$ at 20 °C. (b) About 36 °C, a rise of about 16 K above ambient. (c) About $0.10\ \text{V}$.

**Sanity check:** The trace dissipates about 0.2 W, and a 16 K rise is a plausible result for that power at an assumed 80 K/W. The voltage drop is 0.10 V. On a 5 V rail that is 2 percent, which is a sensible size for a short power trace. If the trace were on an inner layer, where heat escapes more slowly, the same current would give a larger rise. The thermal resistance drives the answer, so the value must come from the board's real thermal environment.

## Design trade-offs

- **Trace width against board area.** Wider traces lower resistance and temperature rise, but they take space that other signals need. Copper pours or planes carry high current when the routing is dense.
- **Copper weight against cost and etch accuracy.** Heavier copper carries more current, but thick copper is harder to etch cleanly, so fine lines need thinner copper.
- **Layer count against cost.** Each added layer costs money, but it gives room for routing, planes, and shielding. Designers often choose the fewest layers that still meet the signal and power needs.
- **External against internal traces.** External traces cool by air and by the board surface. Internal traces sit inside the laminate, which conducts heat poorly, so they carry less current for the same temperature rise.
- **Via count against space and reliability.** Several vias in parallel share current and lower the heat in each barrel. Vias take area on every layer they cross.
- **Density against manufacturability.** Smaller traces and spacings and smaller vias raise fabrication cost and lower yield. The fab's capability sheet sets the limits.

## How it fails

- **Trace overheating and fusing.** A trace that carries more current than its width allows heats up, discolors the laminate, and can open. Warning signs are brown or black marks around a trace and a trace that is hot to the touch.
- **Delamination.** Overheating or trapped moisture can separate the copper or the layers. A blister or a lifted pad is the warning sign.
- **Cracked solder joints.** Copper, laminate, and component materials expand by different amounts when they heat and cool. The mismatch cracks joints over many thermal cycles. Large parts and parts with long leads are most at risk.
- **Via barrel cracks.** A thin plating layer in a via can crack from thermal stress. Thicker plating and a suitable laminate reduce the risk.
- **Solder defects.** Tombstoning (one end of a small chip part lifts during reflow), bridges between fine pads, and voids under parts all come from paste volume, pad design, or the reflow profile.
- **Electrical noise.** A gap in a ground plane forces the return current into a long loop, which picks up noise and radiates it. Crosstalk between long parallel traces adds to the problem.

Design measures reduce these risks. Sizing traces for temperature rise, using planes and thermal vias, keeping creepage and clearance distances for high voltage, and following the assembler's reflow profile all help.

## History

Paul Eisler, an Austrian engineer working in England, built a radio with printed circuits in about 1936. Printed circuits spread through the 1950s as they replaced hand wiring in radios, instruments, and early computers. Surface-mount assembly, which places parts on the board surface instead of through holes, became common in the 1980s. Automated design, fabrication, and assembly then made boards with thousands of parts routine.

## Practice

1. A trace is 0.25 mm wide, 35 µm thick, and 100 mm long. Find its resistance at 20 °C, using $\rho_{20} = 1.68 \times 10^{-8}\ \Omega\,\text{m}$.
2. Find the voltage drop along that trace when it carries 1 A at 20 °C.
3. A 50 mm long, 0.5 mm wide trace of 35 µm copper carries 0.5 A at 20 °C. Find the power it dissipates.
4. The 50 mm trace in problem 3 must have half its resistance at 20 °C. What width is needed?
5. A trace has a thermal resistance of 80 K/W to ambient and dissipates $P$ watts. What power gives a 10 K rise above ambient?

<details><summary>Answers</summary>

1. $R = \dfrac{(1.68 \times 10^{-8})(0.100)}{(0.25 \times 10^{-3})(35 \times 10^{-6})} = 0.192\ \Omega$.
2. $V = IR = 1 \times 0.192 = 0.192\ \text{V}$.
3. $R = 0.048\ \Omega$, so $P = I^2 R = 0.25 \times 0.048 = 0.012\ \text{W}$, or 12 mW.
4. Resistance is inversely proportional to width. Half the resistance needs twice the width: $w = 1.0\ \text{mm}$.
5. $P = \Delta T / R_{th} = 10 / 80 = 0.125\ \text{W}$.

</details>

## Common mistakes

- Sizing a trace from its room-temperature resistance alone. Check the temperature rise, which depends on the thermal environment as well as the current.
- Using the wrong copper thickness. A 0.5 oz layer is about half as thick as a 1 oz layer, so its resistance is about twice as high for the same width and length.
- Treating an internal trace like an external one. Internal traces run hotter for the same current, so they need more width or more copper.
- Relying on a single via for high current. Use several vias in parallel, and check the barrel plating against the current.
- Cutting a ground plane under a signal. The return current takes a long detour, which creates a noise loop.

## Go deeper

- [The Art and Science of PCB Design, MIT IAP 2026 course](https://pcb.mit.edu/): a free MIT course on layout, lecture slides, and design practice.
- [Table of resistivity, HyperPhysics, Georgia State University](https://hyperphysics.gsu.edu/hbase/Tables/rstiv.html): reference values for copper and other conductors at 20 °C.
- Related lessons: [Semiconductors: diodes and transistors](03-semiconductors-diodes-and-transistors.md), [RC circuits and op-amps](02-rc-circuits-and-op-amps.md), [Mechatronics](06-mechatronics.md), [Design for manufacturing and assembly](../../design/10-design-for-manufacturing-and-assembly.md).
- Previous: [Circuit basics](01-circuit-basics.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
