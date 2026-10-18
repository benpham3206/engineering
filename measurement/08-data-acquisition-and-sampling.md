# Data acquisition and sampling

**Type:** lesson

Data acquisition (DAQ) is the chain that turns a sensor's analog voltage into numbers a computer can store. Each step, from conditioning the signal to choosing a sample rate and bit depth, limits what the data can show. Get the sampling wrong and the data can show frequencies that are not in the physical system at all.

**Prerequisites:** [05 - Sensors and transducers](05-sensors-and-transducers.md), [07 - Thermocouples and accelerometers](07-thermocouples-and-accelerometers.md)
**Time:** 6-8 h

## Core ideas

- **Signal conditioning** prepares the raw sensor signal for digitizing. It includes amplification (gain), filtering, excitation for resistive sensors, and isolation. The goal is a clean signal that fills the ADC input range without clipping.
- An **analog-to-digital converter (ADC)** measures the voltage at fixed times and maps it to a binary number. A 12-bit ADC has $2^{12} = 4096$ possible codes.
- **Sampling rate** $f_s$ is how many samples per second the ADC takes, in hertz (Hz).
- The **Nyquist frequency** $f_N = f_s / 2$ is the highest frequency you can represent without error. A signal above $f_N$ cannot be recorded correctly.
- **Aliasing** is what happens when a signal above $f_N$ is sampled anyway. It folds back into the range below $f_N$ and looks like a lower-frequency signal that is not there. Once sampled, aliases cannot be removed from the data.
- An **anti-alias filter** is a low-pass filter placed before the ADC. It removes content above $f_N$ so it cannot fold back. Set its cutoff below $f_N$.
- A practical rule is to sample at 5 to 10 times the highest frequency you care about, which leaves margin for the filter roll-off. The Nyquist rate (twice the highest frequency) is the strict minimum.
- **Resolution** of an ADC is the smallest voltage step it can detect, the **least significant bit (LSB)**. For an ADC with full span $V_{\text{span}}$ and $n$ bits, $\text{LSB} = V_{\text{span}} / 2^n$.
- **Quantization error** is the rounding error from snapping the true voltage to the nearest code. It is at most $\pm\text{LSB}/2$, and its RMS value is $\text{LSB}/\sqrt{12}$.

## Key equations

Nyquist frequency:

$$f_N = \frac{f_s}{2}$$

Alias frequency for a tone at $f$ (Hz) sampled at $f_s$, when $f$ is between $f_N$ and $f_s$:

$$f_{\text{alias}} = |f - f_s|$$

ADC step size:

$$\text{LSB} = \frac{V_{\text{span}}}{2^n}$$

RMS quantization noise:

$$e_{\text{rms}} = \frac{\text{LSB}}{\sqrt{12}}$$

Ideal signal-to-quantization-noise ratio for a full-scale sine wave (a standard result):

$$\text{SNR} \approx 6.02\,n + 1.76\ \text{dB}$$

## Worked example

**Given:** A bearing housing vibrates with content up to about 800 Hz. Its sensor has a faint 2.4 kHz harmonic that matters for diagnosis. The DAQ card uses a 12-bit ADC with a 10 V full span (from -5 V to +5 V).

**Find:** (a) a sample rate that avoids aliasing the 800 Hz content, (b) what the 2.4 kHz harmonic would appear as if left unfiltered at 4 kHz sampling, (c) the ADC LSB and RMS quantization noise.

**Assumptions:** The sensor output is already conditioned to the ADC range. The anti-alias filter is a good low-pass with cutoff near 1 kHz.

**Solution (a):** Choose $f_s = 5 \times 800 = 4000$ Hz. The Nyquist frequency is $f_N = 2000$ Hz, which is well above 800 Hz.

**Solution (b):** The 2.4 kHz harmonic is above $f_N = 2000$ Hz, so it aliases:

$$f_{\text{alias}} = |2400 - 4000| = 1600\ \text{Hz}$$

Without a filter, the 2.4 kHz harmonic would appear as a false 1.6 kHz tone in the data. The fix is an anti-alias filter with cutoff near 1 kHz, which removes the 2.4 kHz content before sampling.

**Solution (c):**

- LSB: $10\ \text{V} / 2^{12} = 10 / 4096 = 2.441\ \text{mV}$
- RMS quantization noise: $2.441\ \text{mV} / \sqrt{12} = 0.705\ \text{mV}$
- Ideal SNR: $6.02 \times 12 + 1.76 = 74.0\ \text{dB}$

**Answer:** (a) $f_s = 4000$ Hz. (b) The 2.4 kHz harmonic would alias to 1.6 kHz, so an anti-alias filter is required. (c) LSB = 2.44 mV; quantization noise is 0.705 mV RMS.

**Sanity check:** The sample rate gives 5 samples per cycle at 800 Hz, which is a reasonable margin. The LSB at 2.44 mV is well below the 0.1 V range of a typical vibration signal at that gain, so quantization is not the limit. The alias calculation agrees with the rule that any frequency above 2 kHz at this sample rate folds back.

## Practice

1. A system is sampled at 2 kHz. Find the Nyquist frequency.
2. A 2400 Hz tone is sampled at 4000 Hz with no filter. Find the alias frequency.
3. A 10-bit ADC has a 3.3 V full span. Find its LSB in mV.
4. You need to capture a 500 Hz signal with 10 samples per cycle. Find the sample rate in Hz.

<details><summary>Answers</summary>

1. 1000 Hz
2. 1600 Hz
3. 3.22 mV
4. 5000 Hz

</details>

## Common mistakes

- Choosing a sample rate equal to the highest frequency, which gives aliasing at the Nyquist limit and no margin.
- Thinking a higher ADC bit depth can fix aliasing. Bits control resolution; only sample rate and filtering control aliasing.
- Forgetting that the anti-alias filter must come before the ADC. Filtering the digital data afterward is too late.
- Using full span instead of the actual input range, which wastes resolution. Choose gain so the signal fills most of the range.
- Mixing up $V_{\text{span}}$ and the full-scale peak voltage. A $\pm 5$ V range spans 10 V, not 5 V.

## Go deeper

- [Signal Processing and Modeling (Engineering LibreTexts)](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling) by LibreTexts: the bookshelf for signals and systems, which covers sampling and reconstruction.
- [Engineering LibreTexts home](https://eng.libretexts.org/) by LibreTexts: free engineering textbooks, including electrical topics.

The aliasing and ADC equations above are standard textbook results. For a full derivation of sampling and aliasing, see the signals bookshelf above.
