# Quantum technologies

**Type:** lesson
**Verify:** strict

Quantum technology is hardware that uses the quantum states of single atoms, ions, electrons, or photons as its working medium to compute, to communicate, or to measure. It matters to an engineer for two reasons. It is the first hardware class whose physics forces extreme cooling, isolation, and error correction into the design, and it changes which public-key cryptography can be trusted, so even engineers who never build a qubit must plan for the change.

**Prerequisites:** [Modern physics and quantum mechanics](../../physics/18-modern-physics-and-quantum.md), [Semiconductors: diodes and transistors](03-semiconductors-diodes-and-transistors.md), [Digital logic and computers](07-digital-logic-and-computers.md), [Probability and statistics](../../math/07-probability-and-statistics.md)
**Time:** 6-8 h

## Core ideas

### How it works

A **qubit** is a two-level quantum system used to carry information. Its state is a combination of the two basis states $|0\rangle$ and $|1\rangle$ with complex amplitudes $\alpha$ and $\beta$. A measurement returns 0 with probability $|\alpha|^2$ and 1 with probability $|\beta|^2$, and afterward the state is the one that was read. The amplitudes satisfy $|\alpha|^2 + |\beta|^2 = 1$.

**Superposition** is a state with both amplitudes nonzero. It is an engineering resource because amplitudes can add or cancel. An algorithm arranges its operations so that paths to wrong answers cancel and paths to the right answer reinforce. This is **interference**, and it is where the advantage over a classical computer comes from. Superposition alone, like a coin spinning in the air, is not enough.

**Entanglement** is a joint state of two or more qubits that cannot be written as a separate state for each. For example, $(|00\rangle + |11\rangle)/\sqrt{2}$ gives each qubit a random result of 0 or 1 with equal probability, yet the two results always agree. Entanglement cannot carry a message faster than light, because each side alone sees only random bits. It is a resource for computation, for secure key distribution, and for sensors that beat the noise of independent particles.

Two limits shape every design. The **no-cloning theorem** says an unknown quantum state cannot be copied, so a quantum state cannot be backed up or amplified like a classical signal. **Decoherence** is the loss of a qubit's quantum behaviour as its surroundings disturb it. The time it takes is the **coherence time**, and every operation must finish well inside it.

### Main parts

| Part | What it does | Example |
|---|---|---|
| Qubit | Holds the quantum state | A superconducting circuit, a trapped ion, a neutral atom, a photon, a spin in a solid |
| Control | Applies gates with precisely shaped microwave, laser, or voltage pulses | Pulse generators, lasers, and modulators |
| Readout | Converts the final state to a classical bit | Microwave resonator readout, fluorescence detection, single-photon detectors |
| Isolation and cooling | Keeps the qubit away from heat and stray fields | A dilution refrigerator, a vacuum chamber, magnetic shielding |
| Classical computer | Compiles programs, decodes error syndromes, and feeds corrections back in real time | Control software and fast digital logic |

The cooling requirement follows from one comparison. A qubit has an energy gap $h f$ between its two states. If the thermal energy $k T$ is comparable to $h f$, the environment keeps flipping the qubit at random. Cooling until $k T \ll h f$ leaves the qubit in its lowest state and lets gates be applied to a known starting point. For a qubit whose gap lies at microwave frequency, that means temperatures a small fraction of a kelvin. Qubits built from isolated atoms or ions have gaps at optical frequency, so the atoms do not need a cold chip, but they need a high vacuum and laser cooling to hold them still.

### Variants

- **Quantum computing** runs a program as a sequence of gates on entangled qubits. Useful applications include simulating quantum systems for chemistry and materials, and a few mathematical problems with proven algorithmic speedups.
- **Quantum key distribution (QKD)** uses single photons to set up a shared secret key between two parties. In the standard scheme, a sender encodes bits in one of two measurement bases chosen at random, and the receiver measures in a randomly chosen basis. The two compare only their basis choices, publicly, and keep the bits where the bases matched. An eavesdropper who measures in the wrong basis disturbs the photon, so about one quarter of the kept bits then disagree, and the parties detect the intrusion by comparing a sample.
- **Quantum sensing** uses the sensitivity of a quantum state to its surroundings. Magnetometers based on defects in diamond or on atomic vapours, and gravimeters and gyroscopes based on interfering atom waves, read fields and accelerations as shifts in a measured phase.
- **Atomic clocks** use a fixed energy gap between two states of an atom as the reference. Every atom of one isotope is identical, and the gap depends only on physics. The SI second is defined as exactly 9 192 631 770 periods of the caesium hyperfine transition, listed in [constants](../../data/constants.md).

### Public-key cryptography and the quantum threat

**Public-key cryptography** lets two parties set up a shared secret over a public channel, or sign a message, using a pair of keys. The common schemes depend on problems believed hard for ordinary computers, namely factoring large integers and computing discrete logarithms, including on elliptic curves.

A large, error-corrected quantum computer running **Shor's algorithm** would solve both problems in a time that grows only polynomially with key size. That would break RSA and elliptic-curve schemes at any practical key length. **Grover's algorithm** gives only a quadratic speedup for searching, so a symmetric key of $n$ bits behaves like a key of about $n/2$ bits, and doubling the key length restores the margin. Secure hashes are affected the same way.

**Post-quantum cryptography (PQC)** is classical cryptography, running on ordinary hardware, built on problems with no known efficient quantum attack, such as problems about lattices or about hash functions. It is the practical response, because it needs no quantum hardware at the endpoints. The risk has a time dimension. An adversary can record encrypted traffic today and decrypt it once a capable machine exists, so data that must stay secret for decades needs protection now. Engineers design for **cryptographic agility**: algorithms are chosen through a replaceable interface, so a scheme can be swapped without redesigning the product. The current standards and migration guidance are published by NIST, linked in Go deeper.

QKD addresses key exchange by physics rather than by hard math problems, but it needs dedicated optical hardware, trusted devices at the ends, and a separate scheme to authenticate the channel. PQC and QKD are complementary tools, and PQC is the one that scales to the internet.

## Key equations

Symbols: $\alpha, \beta$ = complex amplitudes (dimensionless), $h$ = Planck constant (J s), $f$ = qubit transition frequency (Hz), $k$ = Boltzmann constant (J/K), $T$ = temperature (K), $p$ = probability of an error on one physical qubit per operation, $N$ = number of items in a search space.

Measurement probabilities for a single qubit:

$$
P(0) = |\alpha|^2, \qquad P(1) = |\beta|^2, \qquad |\alpha|^2 + |\beta|^2 = 1
$$

Thermal population of a two-level system at equilibrium, with $P_1$ the probability of the upper state:

$$
\frac{P_1}{P_0} = e^{-h f / (k T)}, \qquad P_1 = \frac{r}{1 + r} \ \text{ with } r = e^{-h f/(kT)}
$$

This holds for a qubit in thermal equilibrium with an environment at one temperature and breaks for a qubit driven out of equilibrium or coupled to a hotter local source such as stray radiation.

Logical error rate of the three-qubit repetition code, which corrects a single bit flip by majority vote, when each physical qubit flips independently with probability $p$:

$$
p_L = 3 p^2 - 2 p^3
$$

It reduces errors only when $p < 1/2$ and covers bit flips only. Codes that protect a quantum state against all error types need more qubits, but follow the same idea of spreading information over many noisy parts and correcting the pattern. The independence assumption breaks when errors are correlated.

Grover search, number of oracle queries to find one marked item among $N$:

$$
Q \approx \frac{\pi}{4}\sqrt{N}
$$

Optical fiber transmission over length $L$ (km) with attenuation $a$ (dB/km), the fraction of photons that arrive:

$$
\eta = 10^{-a L / 10}
$$

Fractional clock error $\varepsilon$ (dimensionless) accumulates a time error $\Delta t = \varepsilon\,t$ over an interval $t$, which becomes a range error $c\,\Delta t$ in a ranging system.

## Worked example

**Why a microwave qubit needs a dilution refrigerator.** A superconducting qubit has a transition frequency of 5.0 GHz. Find the probability that it is in the excited state at thermal equilibrium at 300 K and at 20 mK.

**Given:** $f = 5.0$ GHz, $T_1 = 300$ K (room temperature), $T_2 = 20$ mK (an assumed operating temperature), $h$ and $k$ from the constants table.

**Find:** the equilibrium excited-state probability $P_1$ at each temperature.

**Assumptions:** an ideal two-level system in thermal equilibrium with its surroundings.

**Solution:**

1. The gap expressed as a temperature: $h f / k = 0.2400$ K.
2. At 300 K: $h f/(kT) = 7.999 \times 10^{-4}$, so $r = e^{-h f/(kT)} = 0.9992$ and $P_1 = r/(1+r) = 0.4998$.
3. At 20 mK: $h f/(kT) = 11.998$, so $r = 6.156 \times 10^{-6}$ and $P_1 = 6.156 \times 10^{-6}$.

**Answer:** at room temperature the qubit is excited half the time, so it carries no usable information. At 20 mK it is in the ground state with a probability of nearly 1, with an excited-state residue of about 6 parts in a million.

**Sanity check:** the gap in temperature units, 0.24 K, is far below 300 K and far above 20 mK, which matches the two outcomes. The 5 GHz gap corresponds to a photon energy of about 21 $\mu\text{eV}$, tiny against the roughly 26 meV of thermal energy at 300 K.

<details><summary>Verification</summary>

```verify
h = const("h_planck")
k = const("k_boltzmann")
f = q(5.0, "GHz")
T1 = q(300, "K")
T2 = q(20, "mK")
x0 = h * f / k
expect(x0, "0.2400 K")
x1 = h * f / (k * T1)
expect(x1 * 1e4, "7.999")
r1 = exp(-x1)
expect(r1, "0.9992")
P1 = r1 / (1 + r1)
expect(P1, "0.4998")
x2 = h * f / (k * T2)
expect(x2, "11.998")
r2 = exp(-x2)
expect(r2 * 1e6, "6.156")
P2 = r2 / (1 + r2)
expect(P2 * 1e6, "6.156")
expect(h * f, "21 ueV")
expect(k * T1, "26 meV")
check(P1 > 0.4 and P2 < 1e-4, "room temperature mixes the states and 20 mK leaves the qubit in its ground state")
```

</details>

## Design trade-offs

Designers balance the number of qubits against the quality of each. Error rates per gate and coherence times set how many operations a qubit can take part in before the state decays. As an illustration, not a device, a coherence time of 100 $\mu\text{s}$ with 50 ns gates allows about 2000 operations. Longer programs need error correction.

Error correction trades qubits for reliability. A logical qubit is built from many physical qubits, and the overhead grows steeply as the physical error rate nears the correction threshold. Lower physical error rates cut that overhead sharply, so improving qubit quality saves more than adding qubits.

Superconducting circuits operate fast and are built with the fabrication methods of the chip industry, but they need millikelvin cooling and have short coherence times. Trapped ions and neutral atoms have long coherence times and identical qubits, but their gates are slower and they need lasers, vacuum, and complex optics. Photons travel well and suit communication, but they interact weakly, which makes two-qubit gates hard.

For communication, QKD range is limited by fiber loss because a single photon cannot be amplified. Every extra 10 dB of loss cuts the arriving photons by a factor of 10. Practical long links use trusted relay nodes, which put a trusted device in the middle of the link. For cryptography, PQC schemes carry larger keys, signatures, or computation than the schemes they replace, which matters in constrained devices.

## How it fails

- Decoherence. Heat, stray electromagnetic fields, and vibration disturb the state. Warning sign is a coherence time shorter than the spec.
- Gate errors from imperfect pulses. Calibration drifts with temperature and time, so the machines are recalibrated routinely.
- Crosstalk, where driving one qubit disturbs its neighbours.
- Leakage, where a qubit leaves its two intended levels and the error-correction scheme can no longer see it.
- Photon loss and detector noise in a QKD link, which raise the measured error rate. A rate above the protocol's threshold means the key is discarded.
- Attacks on real QKD devices that bypass the physics, for instance by blinding a detector. The protocol is secure on paper, and the hardware must be too.
- PQC failures that come from implementation, such as timing side channels or poor random numbers, and from algorithms later found to be weaker than believed.

> [!WARNING]
> Cryogenic systems hold liquid helium, which expands about 700 times when it boils off. In a closed room it displaces air and causes asphyxiation, and a blocked vent line over-pressurizes a vessel. Handle cryogens only with the training, ventilation, and relief devices the system requires.

## History

Quantum technology grew from two older lines of work. One was precision measurement with atoms, which led to clocks and magnetic sensors. The other was the study of how quantum states carry and process information, which led to proposals for quantum computers and secure key exchange. This lesson gives no qubit counts, device records, company names, or standard numbers, because those change faster than a reference can track and cannot be taken as timeless. Current figures belong on the NIST pages linked in Go deeper.

## Practice

1. A qubit has amplitudes $\alpha = 0.6$ and $\beta = 0.8$. Check that the state is normalized, and find the probability of reading 1.
2. A three-qubit repetition code is used when each physical qubit flips with probability $p = 0.010$. Find the logical error rate.
3. A 128-bit symmetric key is attacked by Grover's algorithm. Estimate the number of queries and the number of key bits of security it leaves, expressed as $\log_2$ of the query count.
4. A QKD link uses fiber with attenuation 0.20 dB/km. Find the fraction of photons that survive 100 km, and explain why a longer link needs a different design instead of an amplifier.
5. A clock has a fractional frequency error of $1.0 \times 10^{-15}$. Find the time error after one day in ps, and the range error this would cause in a ranging system, in cm.

<details><summary>Answers</summary>

1. $0.36 + 0.64 = 1.00$, so the state is normalized. The probability of reading 1 is 0.64.
2. $p_L = 3 p^2 - 2 p^3 = 2.98 \times 10^{-4}$, a reduction by a factor of about 34 from $p$.
3. About $1.45 \times 10^{19}$ queries, which is about $2^{64}$, so the key behaves like a 64-bit key against this attack. Doubling the key length to 256 bits restores 128 bits of security.
4. The fraction is 0.010, that is 1 percent. A photon in an unknown state cannot be amplified or copied (no-cloning), so extra length needs trusted relay nodes or other designs.
5. 86.4 ps after one day, and a range error of about 2.59 cm.

```verify
c = const("c")
expect(0.6**2 + 0.8**2, "1.00", ans=1)
expect(0.6**2, "0.36", ans=1)
expect(0.8**2, "0.64", ans=1)
p = 0.010
pl = 3 * p**2 - 2 * p**3
expect(pl * 1e4, "2.98", ans=2)
expect(p / pl, "34", ans=2, rel=0.02)
given("128", "256")
Q = pi / 4 * 2**64
expect(Q / 1e19, "1.45", ans=3)
expect(log(Q) / log(2), "64", ans=3, rel=0.01)
eta = 10 ** (-(0.20 * 100) / 10)
expect(eta, "0.010", ans=4)
dt = 1.0e-15 * q(1, "d")
expect(dt, "86.4 ps", ans=5)
expect(c * dt, "2.59 cm", ans=5)
```

</details>

## Common mistakes

- Saying a quantum computer tries every answer at once. It prepares amplitudes over many answers, and a measurement returns one. Only an algorithm that makes wrong answers cancel gives an advantage.
- Believing entanglement sends information faster than light. Each side sees random results, and only a classical comparison reveals the correlation.
- Quoting a qubit count as a measure of power. Error rate, coherence time, connectivity, and gate speed decide what a machine can run.
- Treating QKD as a replacement for all cryptography. It exchanges keys only, needs authentication from another scheme, and has range limits.
- Waiting for a working quantum computer before migrating to PQC, even though recorded traffic can be decrypted later.

## Go deeper

- [Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography) by NIST: the standards, the selection process, and migration guidance, kept current.
- [Time and Frequency Division](https://www.nist.gov/pml/time-and-frequency-division) by NIST: atomic clocks and how time is realized and distributed.
- [Quantum Information Science](https://www.nist.gov/quantum-information-science) by NIST: overview of quantum computing, communication, and sensing at NIST.
- [Quantum Physics I (8.04)](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/) by MIT OpenCourseWare: the physics of states, measurement, and wave behaviour behind qubits.
- [University Physics Volume 3](https://openstax.org/details/books/university-physics-volume-3) by OpenStax: free textbook chapters on quantum mechanics.
- Related lessons: [Modern physics and quantum mechanics](../../physics/18-modern-physics-and-quantum.md), [Digital logic and computers](07-digital-logic-and-computers.md).
- Previous: [Digital logic and computers](07-digital-logic-and-computers.md).
- [Fields, waves, and space reference](../../physics/reference-fields-waves-space.md): the physics lookup sheet.
