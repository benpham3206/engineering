# Cameras and lenses: focal length, aperture, and image sensors

**Type:** lesson

A camera uses a lens to form a sharp image of a scene on an image sensor. The lens sets the image size, the sharpness, and the brightness. Engineers need these relations to pick a lens for a given field of view, working distance, and light level.

**Prerequisites:** [Oscillations, waves, light, and heat](../../physics/07-waves-light-heat.md), [Trigonometry](../../math/02-trigonometry.md)
**Time:** 6-8 h

## Core ideas

### How it works

A lens bends light so that rays from one point on the subject meet again at one point on the sensor. For a given sensor position, only subjects at one distance are in sharp focus. Moving the lens or the sensor changes that distance.

The lens forms a real image on the sensor. The image is inverted and smaller than the subject when the subject is far away. The image size scales with the focal length, so a longer lens makes the same subject appear larger.

Light reaching the sensor depends on the aperture, which is the opening that the light passes through. The shutter sets how long the sensor collects light. The sensor counts the photons in each pixel and converts the count into a signal.

### Main parts

- **Lens elements.** Glass or plastic shaped to bend light. Most lenses use several elements to cancel errors.
- **Aperture diaphragm.** A set of blades that sets the opening diameter $D$.
- **Focus mechanism.** Moves the lens or a group of elements to change the object distance that is in focus.
- **Image sensor.** A grid of pixels. Most are CMOS sensors. Each pixel holds a photodiode that turns light into charge.
- **Shutter.** A mechanical or electronic gate that sets exposure time.
- **Image processor.** Converts the raw pixel values into a color image.

### Variants

- **Fixed focal length (prime) lenses.** Simple, sharp, and bright. They do not zoom.
- **Zoom lenses.** Change focal length by moving groups of elements. They trade size and brightness for range.
- **Phone cameras.** Small lenses and small sensors. The short focal length gives a wide field of view and deep depth of field, at the cost of low-light performance.
- **Specialized optics.** Telescope and microscope cameras use special optics built for one job.

## Key equations

- Thin-lens equation, with object distance $d_o$ and image distance $d_i$ in millimetres and focal length $f$ in millimetres: $\dfrac{1}{f} = \dfrac{1}{d_o} + \dfrac{1}{d_i}$.
- Magnification, dimensionless: $m = -d_i / d_o$. The negative sign means the image is inverted. The image height is $h_i = m\,h_o$, where $h_o$ is the object height in millimetres.
- f-number, dimensionless: $N = f / D$, where $D$ is the aperture diameter in millimetres.
- Relative light: the light reaching the sensor scales as $1/N^2$. Each full stop multiplies $N$ by $\sqrt{2}$ and halves the light.
- Horizontal field of view, with sensor width $s$ in millimetres: $\theta = 2\arctan\!\left(\dfrac{s}{2f}\right)$.
- Hyperfocal distance, in millimetres, with circle of confusion $c$ in millimetres (0.03 mm for full-frame sensors, typical): $H = \dfrac{f^2}{N c} + f$. Focusing at $H$ keeps everything from $H/2$ to infinity acceptably sharp.
- Pixel pitch, with sensor width $s$ in millimetres and $n_{px}$ pixels across: $p = s / n_{px}$.

## Worked example

**Given:** A 50 mm lens on a full-frame sensor, which is 36 mm wide and 24 mm tall. The subject is a person 1.7 m tall standing 2.0 m away.

**Find:** (a) the image distance and the image height, (b) the distance at which the person just fills the 24 mm sensor height, and (c) the horizontal field of view.

**Solution:**

1. Image distance: $\dfrac{1}{d_i} = \dfrac{1}{50} - \dfrac{1}{2000} = 0.0195\ \text{mm}^{-1}$, so $d_i = 51.3$ mm.
2. Magnification: $m = -51.3 / 2000 = -0.0256$.
3. Image height: $h_i = -0.0256 \times 1700\ \text{mm} = -43.6$ mm. The sign shows the image is inverted.
4. Distance for a 24 mm image height: $|m| = 24 / 1700 = 0.01412$. From $|m| = f / (d_o - f)$, $d_o = f(1 + 1/|m|) = 50 \times 71.83 = 3592$ mm.
5. Field of view: $\theta = 2\arctan(36 / (2 \times 50)) = 2\arctan(0.36) = 39.6^\circ$.

**Answer:** (a) $d_i = 51.3$ mm and $h_i = 43.6$ mm. (b) 3.6 m. (c) $39.6^\circ$.

**Sanity check:** At 2.0 m the image is 43.6 mm tall, which is larger than the 24 mm sensor. The person does not fit, which agrees with the result that the person fills the sensor only at 3.6 m. The image distance of 51.3 mm is just larger than $f = 50$ mm, as expected for a distant subject.

## Design trade-offs

- **Focal length.** A wide lens sees more of the scene but makes subjects smaller. A telephoto lens sees less, needs more distance, and is larger and heavier.
- **Aperture.** A wide aperture (low $N$) gathers more light and gives a shallow depth of field. It also makes the lens bigger, more expensive, and harder to correct for edge sharpness.
- **Sensor size.** A larger sensor gathers more light per pixel and gives lower noise in dim scenes. It also needs a larger lens to cover the same field of view.
- **Noise.** Light arrives as photons, and photon counts vary randomly. With $N_{ph}$ photons in a pixel, the signal-to-noise ratio is about $\sqrt{N_{ph}}$. Ten thousand photons give a signal-to-noise ratio of about 100, and a pixel with four times the area collects four times the photons.
- **Resolution.** More pixels on the same sensor make each pixel smaller and collect less light. The lens must also resolve the finer detail, and at small apertures diffraction limits the sharpness.

## How it fails

- **Out-of-focus images.** The subject lies outside the depth of field, or autofocus locks onto the wrong object. Low contrast scenes make autofocus hunt.
- **Chromatic aberration.** Glass has a slightly different index for each color, so colors focus at different points. Lenses use elements of different glass to cancel the error. The warning sign is color fringes along high-contrast edges.
- **Flare and ghosting.** Light reflects between glass surfaces and creates bright patches or ghost images. Anti-reflection coatings reduce this.
- **Clipped highlights.** Too much light saturates the pixels, and bright areas show no detail. Exposure settings and the sensor's dynamic range control this.
- **Rolling shutter.** Electronic shutters read rows one after another, so fast motion skews. Global shutters avoid this at higher cost.
- **Sensor damage.** A lens can focus enough sunlight onto the sensor to damage its pixels. Keep the sun out of the frame.

## History

Ibn al-Haytham described the pinhole camera in his *Book of Optics*, written in the early 11th century. Joseph Nicephore Niepce made the first surviving photograph from a window in France about 1826. Louis Daguerre announced the daguerreotype process in Paris in 1839. George Eastman's Kodak camera of 1888 used roll film and made photography widely available. Willard Boyle and George E. Smith invented the charge-coupled device (CCD) sensor at Bell Labs in 1969, and they shared the 2009 Nobel Prize in Physics for it with Charles Kao.

## Practice

1. A lens has $f = 85$ mm. The subject is 3.0 m away. Find the image distance and the magnitude of the magnification.
2. A 24 mm lens is set to $N = 5.6$. The circle of confusion is 0.03 mm. Find the hyperfocal distance in metres.
3. Compare the light reaching the sensor at $N = 4$ and at $N = 5.6$. Give the ratio.
4. A sensor is 36 mm wide and has 9000 pixels across. Find the pixel pitch in micrometres.
5. Explain why a larger sensor usually gives less noise in dim light, even with the same number of megapixels.

<details><summary>Answers</summary>

1. $1/d_i = 1/85 - 1/3000$, so $d_i = 87.5$ mm. The magnification is $|m| = 87.5 / 3000 = 0.0292$.
2. $H = 24^2 / (5.6 \times 0.03) + 24 = 3429 + 24 = 3453$ mm, which is 3.45 m.
3. The light scales as $1/N^2$, so the ratio is $(5.6 / 4)^2 = 1.96$. The $N = 4$ setting gathers about twice the light, which is one stop.
4. $p = 36 / 9000 = 0.0040$ mm, which is $4.0\ \mu\text{m}$.
5. A larger sensor with the same pixel count has larger pixels. Larger pixels collect more photons each, and the signal-to-noise ratio grows as the square root of the photon count.

</details>

## Common mistakes

- Treating the focal length as the distance from the lens to the subject. Focal length is a property of the lens.
- Thinking a wider aperture changes the focal length. It does not.
- Confusing the f-number with the aperture diameter. $N = f/D$, so a small $N$ means a large opening.
- Ignoring sensor size when comparing lenses. A 50 mm lens on a small sensor gives a narrower field of view than the same lens on a full-frame sensor.
- Assuming more megapixels always gives a sharper or better image. Pixel size, lens quality, and light level matter as much.

## Go deeper

- [University Physics Volume 3, Chapter 2: geometric optics, thin lenses, the eye, and the camera](https://openstax.org/books/university-physics-volume-3/pages/2-introduction) by OpenStax. Free, with the thin-lens model and the camera section.
- [Optics, course 2.71](https://ocw.mit.edu/courses/2-71-optics-spring-2009/) by MIT OpenCourseWare. Free lecture materials on optical systems and their engineering use.
- Related lessons: [Sensors in products](../electronics/05-sensors-in-products.md), which covers image sensors in more depth, and [Waves, light, and heat](../../physics/07-waves-light-heat.md), which covers the wave behavior of light.
- [Applications reference](../reference.md): the lookup sheet for this topic.
