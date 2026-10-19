# Doors, hinges, and latches

**Type:** lesson

A door is a heavy panel that must carry its own weight, resist pushes and wind, close reliably, and stay shut. The hinge sets the axis of motion, the closer controls the speed and the force, and the latch holds the door against the frame. Engineers size each part against the loads, the door's mass, and the number of cycles it must survive.

**Prerequisites:** [Statics](../../physics/01-statics.md), [Rigid body dynamics](../../physics/03-rigid-body-dynamics.md), [Mechanical properties](../../materials/03-mechanical-properties.md), [Gears, fasteners, and springs](../../design/09-gears-fasteners-and-springs.md)
**Time:** 3-5 h

## Core ideas

### How it works

A hinge is a **revolute joint**. It constrains the door to rotate about one line, the hinge axis. Two hinges on the same axis keep the door from twisting. When a person pushes the handle, the push creates a moment about the hinge line. The two hinges react to that moment with equal and opposite forces that point sideways, perpendicular to the door face. The hinge that sits under the door also carries the door's weight, and the hinge at the top carries little or none of it.

A latch holds the door shut against the frame. A spring-loaded latch bolt has a beveled face. When the door swings closed, the bevel pushes the bolt back into the latch body, and the spring drives the bolt into the strike plate when the bolt reaches the hole. A **deadbolt** has no spring. A key or a thumb turn drives a solid bolt into the frame, so the door cannot open by pushing the bolt.

A **door closer** stores energy in a spring while the door opens. As the door swings closed, the spring releases its energy through a **hydraulic damper**. The damper forces oil through a small orifice. The orifice sets the closing speed, and an adjustable valve changes how fast the door closes near the end of its travel.

### Main parts

- **Hinge:** two leaves screwed to the door and the frame, a knuckle that carries a pin, and the pin itself.
- **Latch:** a bolt, a return spring, a beveled face, and a retractor that the handle pushes to pull the bolt back.
- **Strike plate:** a hardened plate on the frame that accepts the bolt and takes its load.
- **Closer body:** a spring, a piston, a damping valve, an arm or track, and a mounting bracket.
- **Door stop:** stops the door at its fully open position.

### Variants

Butt hinges are the most common interior hinge. Pivot hinges carry heavy or oversized doors, and they set the axis at the top and bottom of the door rather than at its edge. Piano hinges run the full length of a door or a lid. Concealed hinges hide inside cabinets and modern interior doors. Friction hinges hold the door at any angle.

Spring latches are the common passage latch. Dead latches have a bolt that locks when the door closes. Deadbolts give the most resistance to forced entry. Mortise locks cut into the door edge and include both a latch and a deadbolt.

Closers come as surface-mounted arm closers, concealed closers inside the frame, and floor springs for pivot doors. Gravity hinges use a spring in the hinge knuckle to close the door without a damper.

## Key equations

Assumptions for the equations below: the door is a rigid plate, the hinges are frictionless, all forces lie in the plane perpendicular to the hinge axis except where stated, and the push force is applied at a single point on the handle with its line of action perpendicular to the door face. The spring is linear (Hooke's law). The damper is linear (force proportional to speed).

- Moment: $M = F d$, where $M$ is the moment in newton metres (N m), $F$ is the force in newtons (N), and $d$ is the perpendicular distance from the hinge line to the line of action of the force, in metres (m).
- Hinge reaction from a moment: $R = F d / s$, where $R$ is the sideways reaction at each of two hinges in N, and $s$ is the spacing between the two hinges in metres. The assumption is that the two hinges share the moment as a couple and that the vertical force from the door's weight is handled separately.
- Door weight: $W = m g$, where $m$ is the door mass in kilograms (kg) and $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface, typical sea-level value).
- Kinetic energy of a closing door: $E_k = \tfrac{1}{2} m v^2$, where $v$ is the speed of the door's free edge in m/s. The assumption is that the door rotates about its hinge, so the energy here is the energy of the whole door treated as a point mass at the edge, which overstates the true value. This is a simple upper estimate.
- Spring energy: $E = \tfrac{1}{2} k x^2$, where $k$ is the spring stiffness in N/m and $x$ is the compression in metres. The assumption is that the spring is linear.

## Worked example

**Given:** A door has a mass of $m = 30\ \text{kg}$ and a width of $0.90\ \text{m}$. Two hinges sit $s = 1.5\ \text{m}$ apart on the hinge side. A person pushes the handle at the far edge, which is $d = 0.90\ \text{m}$ from the hinge line, with a force of $F = 100\ \text{N}$. The door closes at $v = 1.0\ \text{m/s}$ at the free edge. Gravity is $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).

**Find:** (a) the sideways reaction at each hinge, (b) the weight of the door, and (c) the kinetic energy of the door closing.

**Solution:**

1. Sideways reaction at each hinge: $R = F d / s = 100 \times 0.90 / 1.5 = 60\ \text{N}$.
2. Check the moment: the push gives $M = F d = 100 \times 0.90 = 90\ \text{N m}$, and the two hinges give $R s = 60 \times 1.5 = 90\ \text{N m}$. The two agree.
3. Door weight: $W = m g = 30 \times 9.81 = 294\ \text{N}$, carried mostly by the lower hinge.
4. Kinetic energy: $E_k = \tfrac{1}{2} m v^2 = 0.5 \times 30 \times 1.0^2 = 15\ \text{J}$.

**Answer:** (a) $60\ \text{N}$ at each hinge. (b) $294\ \text{N}$. (c) $15\ \text{J}$.

**Sanity check:** The two hinge reactions produce a moment of $90\ \text{N m}$, which matches the push. The weight of 294 N is a little under 300 N, which is reasonable for a solid 30 kg door. The 15 J of kinetic energy gives a sense of what a closer must absorb each time the door swings shut.

## Design trade-offs

- **Opening force.** A closer and a heavy door need enough force to close the door reliably, but a person must still open it. Accessibility codes limit the opening force on interior doors. In the United States, the limit for interior hinged doors is 5 lbf (about 22 N) under the ADA standard.
- **Closing speed.** A fast closer slams the door and wears the latch. A closer set too slow may leave a fire door open. Designers set the damper to meet both the safety and the comfort goals.
- **Security.** A spring latch is easy to open with a card, and a deadbolt resists force. A stronger latch and a stronger strike plate cost more and need a sturdier frame.
- **Hinge size.** A larger hinge carries more load and lasts longer, but it is heavier and changes the look of the door.
- **Cycle life.** A commercial door can open and close thousands of times a year. Designers pick hinges and closers rated for that count.
- **Material.** Steel and brass hinges resist wear and corrosion. Plastic hinges save weight but creep under load.

## Safety and the hierarchy of controls

Doors affect escape in a fire, the risk of injury from a closing door, and the ability to stay secure. The controls apply in order.

- **Elimination.** Remove the hazard. A door that swings open into a corridor creates a collision risk. Designers reverse the swing or use a sliding door in such places.
- **Substitution.** Replace a hazard with a lower one. A door that closes slowly with a damper replaces a door that slams. A panic bar replaces a handle that needs a key to leave a room.
- **Engineering controls.** Build the protection in. Examples are fire-rated doors with self-closing hinges, panic and exit devices that release from the inside, electric strikes that fail unlocked, and latches that engage with a smooth bevel rather than a sharp catch.
- **Administrative controls.** Set rules for use. Building codes require fire doors to remain closed, and facility staff check that they close and latch. Staff keep exit paths clear.
- **Personal protective equipment.** Gloves for handling heavy doors during installation. They protect the worker and do not protect anyone using the door.

## How it fails

- **Hinge screws pull out.** Short screws do not reach the stud in the frame, and the hinge loosens. Long screws into the frame stud fix the problem.
- **Door sag.** A heavy door on a loose or worn hinge drops at the free edge. The latch then misses the strike plate. A visible gap at the top of the door and a rubbing bottom edge are the warning signs.
- **Hinge pin walks out.** Vibration and wear can lift the pin out of the knuckle. A loose or missing pin lets the door come off.
- **Latch does not engage.** A misaligned strike plate or a worn bolt lets the door swing open. The door rattles when shut.
- **Closer failure.** A worn seal lets oil leak out and the damper loses its force. A closer that slams or never closes needs its valve adjusted or replaced.
- **Spring fatigue.** A spring that yields loses its stiffness over many cycles, and the door closes weakly.

## History

Hinged doors have turned on pivots and hinges for thousands of years, and early hinges were made of wood, leather, or simple metal pins. Linus Yale Jr. developed the modern pin tumbler lock in the 1840s and 1850s, and that lock now sits in most household doors. Lock and latch hardware developed together through the nineteenth and twentieth centuries.

## Practice

1. A door has a mass of 25 kg. Find its weight in newtons at $g = 9.81\ \text{m}/\text{s}^2$ (Earth surface).
2. Two hinges sit 1.2 m apart. A person pushes with 80 N at 0.80 m from the hinge line. Find the sideways reaction at each hinge.
3. A 25 kg door closes at 0.80 m/s. Find its kinetic energy, using the simple point-mass estimate.
4. A closer spring has $k = 800\ \text{N/m}$ and compresses by 25 mm. Find the stored energy.
5. A door sags at its free edge. Name the two hinge-related causes that a technician checks first, and say which of the two the bottom hinge usually addresses.

<details><summary>Answers</summary>

1. $W = 25 \times 9.81 = 245\ \text{N}$.
2. $R = F d / s = 80 \times 0.80 / 1.2 = 53.3\ \text{N}$.
3. $E_k = \tfrac{1}{2} \times 25 \times 0.80^2 = 8.0\ \text{J}$.
4. $E = \tfrac{1}{2} k x^2 = 0.5 \times 800 \times 0.025^2 = 0.25\ \text{J}$.
5. The technician checks the hinge screws, which may have pulled out of the frame, and the hinge pin, which may have walked out of the knuckle. The bottom hinge usually carries the door's weight, so wear there often shows up as the sag.

</details>

## Common mistakes

- Putting all of a door's weight on the top hinge. The bottom hinge usually carries the weight.
- Assuming a latch holds a door by weight. A spring or a bolt holds the door shut.
- Believing the closer spring alone sets the closing speed. The damper controls the speed.
- Using short screws that do not reach the stud. The hinge then pulls out under load.
- Treating a push at the handle as a single force at the hinge. The moment creates sideways forces that the hinges must resist.

## Go deeper

- [*OpenStax University Physics Volume 1*, Chapter 12](https://openstax.org/books/university-physics-volume-1/pages/12-introduction): free textbook on static equilibrium, which covers the moment and force balance used for hinge reactions.
- [Reference: mechanics](../../physics/reference-mechanics.md): the moment, force, and energy equations used in this lesson.
- [Statics](../../physics/01-statics.md) for force and moment balance on a rigid body.
- [Factor of safety and failure](../../design/07-factor-of-safety-and-failure.md) for choosing hinge and latch sizes against the loads.
- [Mechanical properties](../../materials/03-mechanical-properties.md) for the strength and stiffness of hinge and frame materials.
