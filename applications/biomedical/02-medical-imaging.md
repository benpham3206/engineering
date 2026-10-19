# Medical imaging

**Type:** lesson

Medical imaging makes pictures of the inside of the body without opening it. Each modality uses a different physical signal, such as X-ray attenuation, radio-frequency signals from spinning protons, or echoes of sound, and engineers must understand that signal to size the hardware and control the risks.

**Prerequisites:** [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Electricity and magnetism](../../physics/06-electricity-and-magnetism.md), [Algebra](../../math/01-algebra.md)
**Time:** 6-8 h

## Core ideas

### How it works

**X-ray imaging and CT.** An X-ray tube sends photons through the body. Tissues absorb and scatter photons in proportion to their density and atomic makeup, so a detector behind the body records a shadow of the transmitted intensity. CT takes many such projections from different angles and reconstructs a cross-section of the body from them.

**Ultrasound.** A piezoelectric transducer turns a short voltage pulse into a pressure wave. The wave travels into tissue and reflects at boundaries between tissues. The same transducer listens for the echoes. The time between a pulse and its echo gives the depth of the boundary, and the echo strength shows how strongly the boundary reflects. The Doppler effect measures the frequency shift from moving blood.

**MRI.** A strong static magnetic field, usually 1.5 T or 3 T, aligns the spins of hydrogen protons in the body. A radio-frequency pulse at the Larmor frequency tips those spins. As they relax, they emit a radio signal that receiver coils detect. Gradient coils add small, linear changes to the field, so each position in the body has a different frequency and phase. A Fourier transform of the recorded signal gives the image.

### Main parts

- X-ray tube: a heated cathode, a rotating or fixed anode, and a vacuum envelope. A high-voltage generator sets the electron energy and tube current.
- Collimator and filters: shape the beam and remove low-energy photons that add dose but little image information.
- Detector: a scintillator with photodiodes, or a flat-panel digital detector, converts X-rays to electrical signals.
- CT gantry: a rotating frame that carries the tube and detector around the patient.
- Ultrasound transducer: an array of piezoelectric elements, a pulser, a receiver, and a beamformer that steers and focuses the beam electronically.
- MRI magnet: superconducting coils of niobium-titanium wire, cooled by liquid helium. Shim coils trim field uniformity.
- MRI gradient and RF coils: gradient coils encode position, and RF coils transmit the excitation pulse and receive the signal.

### Variants

- Radiography takes a single projection image. Fluoroscopy shows moving X-ray images. Mammography uses low-energy X-rays for soft tissue.
- CT takes many projections and reconstructs cross-sections, so it gives 3D information at a higher dose than a single projection.
- Ultrasound uses B-mode imaging for structure and Doppler for flow. Frequencies in the range of about 2 to 15 MHz are common in diagnostic work.
- MRI at 1.5 T is a long-established clinical field strength. Scanners at 3 T give more signal and suffer more from artifacts and radio-frequency heating. Low-field systems trade signal for lower cost and smaller magnets.
- Nuclear imaging, such as PET and SPECT, uses injected radioactive tracers. It is outside this lesson's scope.

## Key equations

- X-ray attenuation: $I = I_0 e^{-\mu x}$. Here $I_0$ is incident intensity, $I$ is transmitted intensity (both in the same units), $\mu$ is the linear attenuation coefficient in $\text{cm}^{-1}$, and $x$ is thickness in cm. Assumes a narrow monoenergetic beam, no scatter reaching the detector, and a uniform material.
- Linear attenuation from mass attenuation: $\mu = \rho \, (\mu/\rho)$. Here $\rho$ is density in $\text{g/cm}^3$ and $\mu/\rho$ is the mass attenuation coefficient in $\text{cm}^2/\text{g}$. Assumes the same material and energy throughout.
- Half-value layer: $\text{HVL} = \ln 2 / \mu$. It is the thickness in cm that halves the intensity. Assumes the same monoenergetic beam as above.
- Larmor frequency: $f = \dfrac{\gamma}{2\pi} B_0$. Here $f$ is in hertz, $\gamma/2\pi = 42.577\ \text{MHz/T}$ for hydrogen protons (a standard value), and $B_0$ is the static field in tesla. Assumes the spins sit in a uniform static field.
- Echo depth: $d = c\,t/2$. Here $c$ is the sound speed in m/s, $t$ is the round-trip time in s, and $d$ is depth in m. Assumes a constant sound speed along the path.
- Ultrasound two-way attenuation: $A = 2\,\alpha\, f\, d$, in dB. Here $\alpha$ is the attenuation coefficient in $\text{dB/(cm MHz)}$, $f$ is frequency in MHz, and $d$ is depth in cm. Assumes attenuation is linear in frequency and depth, which is a common approximation.
- CT number: $\text{HU} = 1000\,(\mu - \mu_w)/\mu_w$. Here $\mu$ is the tissue attenuation coefficient and $\mu_w$ is that of water at the same beam energy. This is a definition for scaling the image, and it assumes the same beam energy for both values.

## Worked example

**Given:** A 10 cm thick slab of water at a beam energy of 100 keV. The typical mass attenuation coefficient of water at 100 keV is $\mu/\rho = 0.1707\ \text{cm}^2/\text{g}$. Water density is $\rho = 1.0\ \text{g/cm}^3$. Assume a narrow monoenergetic beam and no scatter at the detector. A separate 1.5 T MRI scanner is also considered.

**Find:** (a) the fraction of the beam transmitted, (b) the half-value layer of water, and (c) the Larmor frequency of protons at 1.5 T.

**Solution:**

1. Linear coefficient: $\mu = 1.0 \times 0.1707 = 0.1707\ \text{cm}^{-1}$.
2. Transmission: $I/I_0 = e^{-0.1707 \times 10} = 0.181$.
3. Half-value layer: $\text{HVL} = \ln 2 / 0.1707 = 4.06\ \text{cm}$.
4. Larmor frequency: $f = 42.577 \times 1.5 = 63.87\ \text{MHz}$.

**Answer:** (a) $I/I_0 = 0.181$, about 18 percent of the beam passes. (b) $\text{HVL} = 4.06\ \text{cm}$. (c) $f = 63.9\ \text{MHz}$.

**Sanity check:** The slab is 10 cm, or about 2.5 half-value layers. Halving 2.5 times gives $(1/2)^{2.5} = 0.177$, which matches the 0.181 result within rounding. A 1.5 T scanner runs near 64 MHz, which is a radio-frequency band, as expected for proton resonance.

## Design trade-offs

- X-ray dose against image quality. Higher tube voltage and current give more photons and less noise, but they raise the dose. Filtration and detector efficiency trade one against the other.
- CT scan time against resolution. Faster rotation reduces motion blur but needs more power and a stronger detector readout.
- Ultrasound frequency against penetration. At 5 MHz, the two-way attenuation over 6 cm is about 30 dB, with $\alpha = 0.5\ \text{dB/(cm MHz)}$ (typical soft tissue). Higher frequency sharpens the image but reaches less depth.
- MRI field strength against cost and safety. Higher field gives more signal, but the magnet costs more, and radio-frequency energy deposition rises with field strength.
- MRI acoustic noise. Gradient coils switch currents in the presence of a strong field, which produces loud knocking. Designers add damping and mounting isolation to reduce it.
- Helium use. Superconducting magnets rely on liquid helium. Sealed, low-loss designs reduce refills and the risk of a quench.

## How it fails

- X-ray tube wear. Anode heat load and cathode aging reduce output. Warning signs include tube overheating alarms and falling output.
- Detector and electronics faults. Dead pixels and drift cause artifacts and wrong dose readings.
- Ultrasound cable and element damage. A cracked cable or a dead transducer element creates lines or dropouts in the image.
- MRI quench. A superconducting magnet can lose superconductivity, and the stored energy boils off helium. Warning signs include a rising helium pressure or a magnet temperature alarm. A vent pipe carries the boil-off out of the room.
- Projectile hazard. A strong static field pulls ferromagnetic objects toward the magnet.
- Radio-frequency heating. Energy absorbed in tissue or implants raises temperature. Limits on specific absorption rate (SAR) control this.
- Ionizing exposure above design. Repeated or high-dose X-ray and CT scans add to the cumulative dose.

**Risk management.** ISO 14971 governs these hazards, with severity and probability estimated for each one, and residual risk verified after controls. The hierarchy of controls applies as follows.

- Elimination: keep ferromagnetic objects out of the magnet zone with zone design and screening. Use the lowest dose that answers the clinical question.
- Substitution: use ultrasound or non-ionizing MRI where it answers the question, instead of X-ray, and use lower-dose protocols.
- Engineering controls: lead shielding and collimation, dose display, exposure interlocks, SAR monitoring, and a quench vent pipe with helium pressure relief.
- Administrative controls: screening questionnaires, room access rules, training, dose reference levels, and service records.
- Personal protective equipment: lead aprons and thyroid shields for staff who stay in the X-ray room, and hearing protection for staff in the MRI room.

**Regulation and standards.** The FDA classifies devices by risk into Class I, II, and III, and X-ray and CT systems are usually Class II. The product's classification must be checked in the FDA database. IEC 60601-1 covers basic safety of medical electrical equipment. IEC 60601-1-2 covers electromagnetic compatibility. IEC 60601-1-3 covers radiation protection in diagnostic X-ray equipment. IEC 60601-2-33 covers MR equipment, IEC 60601-2-44 covers CT equipment, and IEC 60601-2-37 covers diagnostic ultrasound equipment. ISO 14971 governs risk management.

## History

Wilhelm Conrad Röntgen discovered X-rays in Würzburg, Germany, in 1895, and he received the first Nobel Prize in Physics in 1901. Felix Bloch and Edward Purcell observed nuclear magnetic resonance in 1946, and they shared the 1952 Nobel Prize in Physics. Paul Lauterbur published an early MR image in 1973 by adding magnetic field gradients to localize the signal. Godfrey Hounsfield at EMI in England built the first clinical CT head scanner, and it scanned its first patient in 1971. Allan Cormack independently developed the reconstruction mathematics, and the two shared the 1979 Nobel Prize in Physiology or Medicine. Ian Donald and colleagues in Glasgow reported obstetric ultrasound in about 1958.

## Practice

1. Find the half-value layer of a material with $\mu = 0.30\ \text{cm}^{-1}$.
2. Find the Larmor frequency of protons in a field of $1.0\ \text{T}$.
3. An ultrasound echo returns $65\ \mu\text{s}$ after the pulse. Find the depth of the reflector, assuming $c = 1540\ \text{m/s}$.
4. An ultrasound beam at $3\ \text{MHz}$ travels $4\ \text{cm}$ to a reflector and returns. Using $\alpha = 0.5\ \text{dB/(cm MHz)}$, find the two-way attenuation in dB.

<details><summary>Answers</summary>

1. $\text{HVL} = \ln 2 / 0.30 = 2.31\ \text{cm}$
2. $f = 42.577 \times 1.0 = 42.58\ \text{MHz}$
3. $d = c\,t/2 = 1540 \times 65\times10^{-6} / 2 = 0.050\ \text{m}$, or $5.0\ \text{cm}$
4. $A = 2 \times 0.5 \times 3 \times 4 = 12\ \text{dB}$

</details>

## Common mistakes

- Mixing the two forms of the attenuation coefficient. $\mu$ is in $\text{cm}^{-1}$, and $\mu/\rho$ is in $\text{cm}^2/\text{g}$. Multiply by density to convert.
- Using the echo time as the one-way travel time. Depth uses half the round-trip time.
- Assuming ultrasound attenuation does not depend on frequency. Higher frequency attenuates more, so the depth limit falls as frequency rises.
- Applying the proton Larmor frequency to every nucleus. Other nuclei have different gyromagnetic ratios.
- Saying that MRI uses X-rays. MRI uses static and radio-frequency magnetic fields, not ionizing radiation.

## Go deeper

- [Magnetic Resonance Imaging, National Institute of Biomedical Imaging and Bioengineering](https://nibib.nih.gov/science-education/science-topics/magnetic-resonance-imaging-mri): the physics of MRI, its uses, and its safety risks.
- [Medical X-rays, National Institute of Biomedical Imaging and Bioengineering](https://nibib.nih.gov/science-education/science-topics/medical-x-rays): the physics of X-ray imaging and CT, with radiation risks.
- [XCOM: Element/Compound/Mixture, National Institute of Standards and Technology](https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html): photon cross-section data. Select the compound option and enter the material to look up mass attenuation coefficients.
- [Classify Your Medical Device, U.S. Food and Drug Administration](https://www.fda.gov/medical-devices/overview-device-regulation/classify-your-medical-device): device classes and premarket pathways.
- [Fields, waves, and space reference](../../physics/reference-fields-waves-space.md) for the wave and field background.
- [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md) for the wave equations behind ultrasound.
