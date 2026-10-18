# GD&T symbols and frames

**Type:** lesson

Geometric Dimensioning and Tolerancing (GD&T) is a symbolic language for describing the shape, orientation, and location of features, and how much each may vary. Plus-minus tolerances on a size cannot control a flat face, a square corner, or a hole's position on a bolt circle. GD&T can. The next lesson covers material conditions and position in depth.

The rules are written in the ASME Y14.5 standard, which is paid. Read it through a library or your employer. The ideas in this lesson are the common core that the standard describes.

**Prerequisites:** [02 Engineering graphics](02-engineering-graphics.md), [04 Tolerancing and stack-up](04-tolerancing-and-stack-up.md)
**Time:** 8-12 h

## Core ideas

- **Size tolerance** controls how big a feature is. **Geometric tolerance** controls its shape, orientation, or location. Both can apply to one feature.
- **Tolerance zone** is the three-dimensional region that the actual feature must fit inside. For a flat face, the zone is the space between two parallel planes. For a hole's position, the zone is a cylinder around the true position.
- **Datum** is a theoretical reference, such as a plane, axis, or point, used to measure against. Datums are made real by the part's surfaces through **datum features**.
- **Feature control frame (FCF)** is the rectangular box on a drawing that holds the whole callout.
- **Basic dimension** is a theoretically exact dimension, shown in a box, with no tolerance of its own. It locates a tolerance zone.

GD&T is about function. Ask, "What must this feature do, and what variation can it tolerate?" Then choose the characteristic that controls that function.

## Datums

A datum is set up by a datum feature, which is a real surface on the part.

- A datum feature symbol is a box with a letter (for example A), attached by a leader to the surface, with a filled triangle at the end.
- Datums are labeled with capital letters, except I, O, and Q, which are skipped to avoid confusion with numbers.
- A **datum reference frame (DRF)** uses up to three datums in a fixed order. The first is primary, then secondary, then tertiary.
- The primary datum usually restricts three degrees of freedom (a plane), the secondary two (a line), and the tertiary one (a point). This is the 3-2-1 idea: a part placed on a plane, against a stop, and against a pin is held in a single known position.
- The order of datums in the FCF is the order the part is set up on the inspection fixture. Changing the order changes the answer.

Choose datums from how the part is mounted or mated. A datum should be the surface that the other parts touch.

## The feature control frame

An FCF is read left to right. It has up to five compartments:

1. The **characteristic symbol**, such as position or flatness.
2. The **tolerance value**, a number with a diameter symbol (Ø) if the zone is cylindrical. The value is the full width of the zone.
3. An optional **material condition modifier** in a circle, such as M for maximum material condition (MMC).
4. The **primary datum**, then optionally a **secondary** and **tertiary** datum, separated by compartments.

A simple frame for a hole position reads, in words, "position, diameter zone 0.25, at MMC, to datums A, B, and C."

Only one characteristic goes in each frame. If a feature needs two controls, use two frames stacked or side by side.

## The main characteristic symbols

Characteristics are grouped by what they control.

**Form** controls shape only. No datum is used.

- Straightness: a line element of a surface or axis is straight.
- Flatness: a surface lies between two parallel planes.
- Circularity: each cross section of a round feature is round.
- Cylindricity: the whole cylinder is round and straight at once.

**Orientation** controls angle to a datum. A datum is required.

- Perpendicularity: a feature is at 90 degrees to a datum.
- Angularity: a feature is at a specified angle to a datum.
- Parallelism: a feature is parallel to a datum.

**Location** controls where a feature is. A datum is required.

- Position: the center of a feature (or its axis) lies within a zone around its true location. It is the most common location control for holes.
- Concentricity: a feature's axis is coaxial with a datum axis. Largely replaced in newer practice by position with a zero tolerance at MMC.
- Symmetry: a feature's center plane lies within a zone around a datum center plane.

**Profile** controls a line or surface outline.

- Profile of a line: the outline of each cross section lies within a zone.
- Profile of a surface: the whole surface lies within a zone around its true shape. It can control form, orientation, and location at once, depending on whether datums are used.

**Runout** controls the variation of a surface as the part rotates about a datum axis. A datum is required.

- Circular runout: measured at one position at a time as the part rotates.
- Total runout: measured along the whole surface at once.

Some symbols are easy to mix up. Perpendicularity and angularity both use a datum to set an angle, but perpendicularity fixes it at 90 degrees. Circularity controls one slice; cylindricity controls the whole cylinder. Runout depends on rotation; form does not.

## Checklist

- Is the characteristic chosen from the function, not from habit?
- Does each datum sit on a real surface the mating part uses?
- Is the datum order (primary, secondary, tertiary) the order of setup?
- Does a form control have no datum, and does an orientation, location, or runout control have one?
- Is the tolerance a full zone width, with the diameter symbol where the zone is round?
- Is there exactly one characteristic per frame?

## Example

A round shaft has a journal that must rotate smoothly inside a bearing. The shaft is mounted on two centers, and the bearing seat must be coaxial with them.

- **Datum.** The two center holes at each end define the axis. Datums A and B are set on the ends. The datum axis is named A-B.
- **Callout.** On the journal surface, the frame reads: circular runout, tolerance 0.02, datum A-B.
- **Reading it.** The journal may vary in radius as it turns, but a dial indicator held on the surface must not read more than 0.02 mm (0.0008 in) total swing at each position, measured against the axis A-B.
- **Why it matters.** The bearing sees a wobbling shaft as a rotating load on one side. A runout limit keeps that wobble small. A diameter size tolerance would not catch it, because a perfectly round but off-center journal can still pass a diameter check.
- **Check.** Would a flatness control solve the problem? No. Flatness does not refer to rotation about an axis, so it misses the wobble.

Runout matches a rotating part, and the size tolerance alone does not.

## Practice

1. Which characteristic controls how flat a surface is, with no datum? Answer with the name.
2. Which characteristic needs a datum and controls the angle between a face and a datum, with 90 degrees as the target? Answer with the name.
3. How many characteristics belong in one feature control frame? Answer with a number.
4. Which symbol set is used to control the location of a hole center: form, orientation, or location? Answer with one word.

<details><summary>Answers</summary>

1. Flatness.
2. Perpendicularity.
3. One.
4. Location.

</details>

## Common mistakes

- Putting a datum on a form control, which is not allowed because form does not refer to anything.
- Reversing the datum order, which changes how the part is set up and measured.
- Using a diameter size tolerance to control a shape or wobble that only geometric tolerances can capture.
- Forgetting that the tolerance value is a full zone width, not a plus-minus number.
- Calling a datum a feature. A datum is a theoretical reference, and the datum feature is the real surface that sets it.

## Go deeper

- [Engineering LibreTexts](https://eng.libretexts.org/) by the LibreTexts project: free engineering textbooks where drawing and tolerance topics appear.
- [MIT OpenCourseWare, 2.017J Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) by MIT: a free course that shows how tolerances and fits affect real mechanical designs.
- No free GD&T textbook was confirmed for this lesson. The standard itself is ASME Y14.5, a paid document, named here for reference only.
- [Design reference](reference.md): the lookup sheet for this topic.
