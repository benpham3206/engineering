# Zippers and buttons: interlocking teeth, slider friction, and snap springs

**Type:** lesson

A zipper joins two rows of teeth that interlock when a slider pushes them together and separate when it pulls them apart. A button or snap holds a garment closed through a shank or a spring socket that yields and then grips. Engineers who size fasteners need the tooth count, the load shared by the teeth, and the stiffness of the snap spring.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Axial and torsion](../../physics/04-axial-and-torsion.md), [Mechanical properties](../../materials/03-mechanical-properties.md)
**Time:** 2-3 h

## Core ideas

### How it works

A zipper has two tape strips, each carrying a row of teeth. The teeth are metal or molded plastic elements spaced at a fixed pitch. A slider rides along the tapes. Its wedge-shaped channel forces the two rows of teeth together, so each tooth on one side slips into a gap on the other side. Pulling the slider the other way opens the teeth again.

A snap fastener has a stud and a socket. Pressing the stud into the socket deflects a set of spring fingers outward, and the fingers snap back to grip the stud. A sewn button uses a shank, a loop of thread or fabric that passes through a buttonhole and resists pull-out.

### Main parts

- **Teeth**: the interlocking elements. Their shape sets how strongly the two rows resist separation.
- **Tapes**: the fabric strips that carry the teeth and transfer load to the garment.
- **Slider**: the wedge that closes or opens the teeth. Its friction against the teeth is the force the user feels.
- **Stop and bottom end**: limit the slider and keep it from leaving the track.
- **Snap stud and socket**: a spring socket and a stud that clamp through the fabric.
- **Button and shank**: the button clamps the fabric through its shank.

### Variants

- **Coil zippers**: a continuous plastic or metal coil stitched to the tape. They bend well and suit jackets and bags.
- **Molded plastic zippers**: individual plastic teeth injected onto the tape. They resist corrosion and suit swimwear.
- **Metal zippers**: stamped metal teeth. They are strong and suit jeans and heavy bags.
- **Snap fasteners**: spring socket and stud. They suit cuffs and fast closures.
- **Sewn buttons**: the usual choice for shirts. The shank sets how much the fabric can stretch.

## Key equations

Assumptions for all equations below: teeth are uniformly spaced, the slider is fully engaged, the load is shared as stated, and loads are static and small.

Number of tooth pairs along a zipper length:

$$N_t = \frac{L}{p}$$

where $N_t$ is the number of tooth pairs (dimensionless count), $L$ is the zipper length in metres (m), and $p$ is the tooth pitch in metres (m). This assumes a uniform pitch and that the whole length is engaged.

Load on one engaged tooth when the pull force is shared equally:

$$F_t = \frac{F}{n_e}$$

where $F_t$ is the load per tooth in newtons (N), $F$ is the pull force in newtons (N), and $n_e$ is the number of engaged teeth (dimensionless count). This assumes equal sharing among the engaged teeth.

Stiffness of a snap spring finger modelled as a cantilever with a point load at the tip:

$$k = \frac{E\,b\,t^{3}}{4\,L^{3}}$$

where $k$ is the stiffness in newtons per metre (N/m), $E$ is the Young's modulus in pascals (Pa), $b$ is the finger width in metres (m), $t$ is the finger thickness in metres (m), and $L$ is the finger length in metres (m). The model assumes a rectangular cross section, a linear elastic material, small deflection, and a load applied at the tip.

Root bending stress in the same cantilever at deflection $\delta$ (metres):

$$\sigma = \frac{6\,k\,\delta\,L}{b\,t^{2}}$$

where $\sigma$ is the bending stress in pascals (Pa) and $\delta$ is the tip deflection in metres (m). The same assumptions apply.

## Worked example

**Given:** A 60 cm zipper with a tooth pitch of 4.5 mm (assumed for this example, not a standard value). A user pulls the slider with $F = 50\ \text{N}$, and 6 teeth carry the load at once (assumed).

**Find:** (a) the number of tooth pairs, (b) the load on each engaged tooth.

**Solution:**

1. Tooth pairs: $N_t = 0.60 / 0.0045 = 133.3$, so about 133 pairs.
2. Load per tooth: $F_t = 50 / 6 = 8.3\ \text{N}$.

**Answer:** (a) About 133 tooth pairs. (b) About $8.3\ \text{N}$ per engaged tooth.

**Sanity check:** Each tooth carries about a sixth of the load, which is plausible for a closed zipper with a few teeth engaged. A few newtons per tooth is far below what a tooth should resist.

**Second example (snap spring).** A steel snap finger has $b = 2\ \text{mm}$, $t = 0.2\ \text{mm}$, and $L = 4\ \text{mm}$, with $E = 200\ \text{GPa}$ (typical for steel). Deflecting the tip by $\delta = 0.1\ \text{mm}$ gives $k = 12\,500\ \text{N/m}$, force $F = k\delta = 1.25\ \text{N}$, and root stress $\sigma = 375\ \text{MPa}$. Typical spring steel has a yield strength well above 375 MPa, so the finger stays elastic. A deflection of $0.5\ \text{mm}$ would give $\sigma = 1875\ \text{MPa}$, which the steel cannot survive, so the design limit is set by stress.

## Design trade-offs

- **Strength versus flexibility**: thicker teeth and tapes resist separation but make the zipper stiff and heavy. Coil zippers trade some strength for bending ease.
- **Corrosion**: metal teeth rust in salt water. Molded plastic teeth resist corrosion, which suits swimwear and marine gear.
- **Friction and feel**: a tight slider needs more pull force. Designers balance tooth profile against the force a user can apply with one hand.
- **Cost**: coil and molded zippers cost less per metre than fine metal zippers.
- **Snap stiffness**: a stiffer snap holds better but needs more force to close. A softer snap closes easily but can pop open.

## How it fails

- **Tooth misalignment**: a tooth that does not seat in its gap jams the slider. Warning signs are a slider that catches or a wavy closed line.
- **Slider drops off the track**: a worn or bent stop lets the slider leave the teeth. The zipper then splits open.
- **Tape tearing**: stitching or tape fabric tears under repeated pull. The stitch line is usually the weak point.
- **Snap fatigue**: repeated flexing work-hardens and cracks the spring fingers. A cracked snap no longer grips.
- **Button pull-out**: a loose shank or thread wears through and the button detaches.

## Hierarchy of controls for small-part hazards

Small buttons, snaps, and zipper sliders pose a choking hazard for young children.

- **Elimination**: omit detachable small parts from clothing made for children under three.
- **Substitution**: use large sewn-in closures or fabric ties in place of small snaps or buttons.
- **Engineering controls**: a snap or button must pass a pull test set by the product standard, so it does not detach in normal use.
- **Administrative controls**: label garments with age warnings and inspect fasteners on use and before resale.
- **Personal protective equipment**: not applicable. The protection comes from design, testing, and labelling.

## History

The first zipper patent in the United States went to Whitcomb Judson in 1893 for a clasp locker, a hook-and-eye design that was hard to use reliably. Gideon Sundback improved the design in 1913 with interlocking stamped teeth, which is close to the modern zipper. The name "zipper" came into use about 1923, when the B.F. Goodrich company used it for rubber boots. Buttons are older than zippers. Shell buttons with holes have been found in the Indus Valley from the third millennium BCE.

## Practice

1. A zipper is 40 cm long with a tooth pitch of 4 mm. How many tooth pairs does it have?
2. A pull force of 40 N is shared equally by 5 engaged teeth. What is the load per tooth?
3. A snap finger has $b = 3\ \text{mm}$, $t = 0.3\ \text{mm}$, $L = 5\ \text{mm}$, and $E = 200\ \text{GPa}$. Find its stiffness $k$ in newtons per metre.
4. A zipper has a tooth pitch of 3.5 mm. How many tooth pairs are in 1 m?

<details><summary>Answers</summary>

1. $0.40 / 0.004 = 100$ tooth pairs.
2. $40 / 5 = 8\ \text{N}$ per tooth.
3. $k = E b t^3 / (4 L^3) = 32\,400\ \text{N/m}$, which is about $3.2 \times 10^4\ \text{N/m}$.
4. $1 / 0.0035 = 286$ tooth pairs (rounded).

</details>

## Common mistakes

- Using the tooth pitch in centimetres when the formula needs metres. Convert every length to metres first.
- Assuming the full pull force reaches one tooth. The load spreads across the engaged teeth.
- Treating the snap spring as a rigid part. Its stiffness is set by thickness cubed, so a small thickness change shifts the force a lot.
- Ignoring stress when sizing a snap. A snap can deflect enough to cross yield, which the force alone does not show.
- Selling children's garments with small detachable parts and no pull test or age warning.

## Go deeper

- [Applications of Newton's laws, OpenStax University Physics Volume 1](https://openstax.org/books/university-physics-volume-1/pages/6-introduction): friction and the forces on a sliding part, relevant to the slider.
- [Mechanics reference sheet](../../physics/reference-mechanics.md): beam and cantilever relations.
- [Materials reference sheet](../../materials/reference.md): modulus, yield strength, and fatigue values for fastener materials.
- Related lessons: [Locks and keys](01-locks-and-keys.md), [Mechanical properties](../../materials/03-mechanical-properties.md).
