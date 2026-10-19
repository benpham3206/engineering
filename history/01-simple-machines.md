# Simple machines

**Type:** lesson

The six simple machines are the basic mechanical parts from which nearly every machine is built. Each one trades distance for force, and the ideal mechanical advantage tells an engineer exactly how much force it saves before friction takes its share.

**Prerequisites:** none
**Time:** 4-5 h

## Core ideas

Every simple machine follows one rule. A machine cannot create energy, so when it multiplies force, it must move the point where the force acts over a longer distance. Force times distance stays the same, minus friction. Ideal mechanical advantage (IMA) is the ratio of the output force to the input force with no losses. It also equals the ratio of the input distance to the output distance.

The six machines are the lever, the wheel and axle, the pulley, the inclined plane, the wedge, and the screw. Greek writers described these machines, and the six-machine list used today took shape from those sources during the Renaissance. Each machine below comes with its ideal mechanical advantage formula and a short sketch in words.

### Lever

Picture a rigid bar that turns about a fixed point, called the fulcrum. The effort pushes on one end, and the load sits on the other end. The effort arm is the distance from the fulcrum to the effort. The load arm is the distance from the fulcrum to the load.

$$\text{IMA} = \frac{d_E}{d_L}$$

Here $d_E$ is the effort arm in metres and $d_L$ is the load arm in metres. A lever with a 1.6 m effort arm and a 0.4 m load arm has an IMA of 4.0.

Engineers sort levers into three classes by the order of the fulcrum, load, and effort:

- Class 1 puts the fulcrum between the effort and the load. A crowbar, a seesaw, and scissors work this way.
- Class 2 puts the load between the fulcrum and the effort. A wheelbarrow and a nutcracker work this way. The IMA is always greater than 1.
- Class 3 puts the effort between the fulcrum and the load. Tweezers and the human forearm work this way. The IMA is less than 1, so the effort force is larger than the load, but the load moves through a larger distance.

### Wheel and axle

Picture a large wheel fixed to a smaller axle, so the two turn together. Force applied to the wheel turns the axle, and a rope wound on the axle lifts the load. A winch, a ship's steering wheel, and a screwdriver handle all use this machine.

$$\text{IMA} = \frac{R}{r}$$

Here $R$ is the wheel radius in metres and $r$ is the axle radius in metres. A wheel of 0.30 m radius on an axle of 0.050 m radius has an IMA of 6.0.

### Pulley

Picture a grooved wheel that carries a rope. A fixed pulley hangs from a support and only changes the direction of the pull, so its IMA is 1. A movable pulley hangs from the load itself, and two rope segments share the load, so its IMA is 2.

In a system where $n$ rope segments support the load, the IMA is $n$. The effort moves $n$ times as far as the load moves. Pulleys are simple to combine with other pulleys, and that combination is the block and tackle described later in this lesson.

$$\text{IMA} = n$$

### Inclined plane

Picture a ramp that rises from a low end to a high end. Pushing a load up the ramp requires less force than lifting it straight up, because the same work is spread over a longer path.

$$\text{IMA} = \frac{L}{h}$$

Here $L$ is the length of the slope in metres and $h$ is the height gained in metres. A 4.0 m ramp that rises 1.0 m has an IMA of 4.0. Ideally, an 800 N load needs only 200 N along the ramp.

### Wedge

Picture two inclined planes joined back to back, with the thin edge driven into a material. The force of a hammer pushes the wedge in, and the wedge pushes the material apart to the sides. An axe, a knife, a chisel, and a nail all act as wedges.

$$\text{IMA} = \frac{L}{t}$$

Here $L$ is the length of the slope on the long side in metres and $t$ is the thickness of the blunt end in metres. A wedge 0.20 m long with a 0.030 m blunt end has an IMA of about 6.7.

### Screw

Picture an inclined plane wrapped around a cylinder. Turning the screw by one full turn moves it forward by one pitch, the distance between neighbouring threads. A turning handle supplies the effort at a radius from the screw axis.

$$\text{IMA} = \frac{2\pi R}{p}$$

Here $R$ is the handle radius in metres and $p$ is the pitch in metres. A handle of 0.25 m radius on a screw with a 5 mm pitch has an IMA of about 314. Screws carry high IMA values, and friction takes a large share of the input work, so real screw efficiency is often low. A jar lid, a car jack, and a bench vise all use screws.

### Compound machines

A compound machine connects two or more simple machines so the output of one feeds the input of the next. The ideal mechanical advantages multiply. Each stage multiplies the distance ratio of the stage before it, so the total ideal advantage is the product of the stage values.

Friction makes the real advantage smaller. Each stage has an efficiency, the output work divided by the input work for that stage. The overall efficiency is the product of the stage efficiencies. A winch that drives a block and tackle gives the clearest example of this, and the worked example below shows the numbers.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|---|---|---|---|
| About 3500 BCE | Wheel and axle | Mesopotamia, Sumer (date approximate) | Carried loads and turned rotation into a force multiplier. |
| Date uncertain | Shaduf, a counterweighted lever for raising water | Mesopotamia and Egypt | Lifted water to fields with little effort. |
| Third century BCE | Law of the lever and the compound pulley | Archimedes, Syracuse | Gave the first rigorous account of mechanical advantage. |
| Third century BCE, traditionally | Screw for raising water | Attributed to Archimedes, Syracuse | Raised water continuously with a turning screw. |
| First century CE | Written descriptions of machines and devices | Hero of Alexandria, Alexandria | The text of his Pneumatics survives and describes working devices in detail. |

## Key equations

Ideal mechanical advantage, with forces in newtons (N) and distances in metres (m):

$$\text{IMA} = \frac{F_L}{F_E} = \frac{d_E}{d_L}$$

Here $F_L$ is the load force in N, $F_E$ is the effort force in N, $d_E$ is the distance the effort moves in m, and $d_L$ is the distance the load moves in m. The two forms are equal because an ideal machine conserves work.

Actual mechanical advantage with friction:

$$\mathrm{MA} = \frac{F_L}{F_E} = \eta \, \text{IMA}$$

Here $\eta$ is the efficiency of the machine, a number between 0 and 1 with no units. Work and efficiency:

$$W_{\text{in}} = F_E \, d_E, \qquad W_{\text{out}} = F_L \, d_L, \qquad \eta = \frac{W_{\text{out}}}{W_{\text{in}}}$$

Work $W$ is in joules (J). Lever balance for an ideal lever, with the moments in newton metres (N m):

$$F_E \, d_E = F_L \, d_L$$

Compound machines, with $k$ stages:

$$\text{IMA}_{\text{total}} = \prod_{i=1}^{k} \text{IMA}_i, \qquad \eta_{\text{total}} = \prod_{i=1}^{k} \eta_i$$

## Worked example

**Given:** A winch lifts a load of $W = 1000\ \text{N}$, which is the weight of about 102 kg at $g = 9.81\ \text{m/s}^2$ (Earth surface). The winch handle has a radius $R = 0.30\ \text{m}$, and the drum has a radius $r = 0.050\ \text{m}$. A block and tackle with $n = 4$ supporting rope segments connects the drum to the load. The load rises $h = 2.0\ \text{m}$. Typical efficiencies are $\eta_{\text{winch}} = 0.80$ and $\eta_{\text{pulley}} = 0.90$.

**Find:** (a) the ideal effort, (b) the actual effort, (c) the distance the handle moves, and (d) the input work and the output work.

**Assumptions:** The rope does not stretch. Efficiencies stay constant over the lift.

**Solution:**

1. Winch IMA: $\text{IMA}_{\text{winch}} = R / r = 0.30 / 0.050 = 6.0$.
2. Block and tackle IMA: $\text{IMA}_{\text{pulley}} = n = 4$.
3. Total ideal IMA: $\text{IMA}_{\text{total}} = 6.0 \times 4 = 24$.
4. Ideal effort: $F_{\text{ideal}} = W / \text{IMA}_{\text{total}} = 1000 / 24 = 41.7\ \text{N}$.
5. Overall efficiency: $\eta = 0.80 \times 0.90 = 0.72$.
6. Actual effort: $F_E = W / (\text{IMA}_{\text{total}} \, \eta) = 1000 / (24 \times 0.72) = 57.9\ \text{N}$.
7. Rope pulled off the drum: $n h = 4 \times 2.0 = 8.0\ \text{m}$.
8. Drum turns: $8.0 / (2\pi \times 0.050) = 25.5$ turns.
9. Handle travel per turn: $2\pi \times 0.30 = 1.885\ \text{m}$. Total handle travel: $25.5 \times 1.885 = 48.0\ \text{m}$.
10. Output work: $W h = 1000 \times 2.0 = 2000\ \text{J}$.
11. Input work: $F_E \times 48.0 = 57.9 \times 48.0 = 2778\ \text{J}$.

**Answer:** (a) The ideal effort is 41.7 N. (b) The actual effort is 57.9 N. (c) The handle moves 48.0 m. (d) The input work is 2.78 kJ, and the output work is 2.00 kJ.

**Sanity check:** The handle travel equals $\text{IMA}_{\text{total}} \times h = 24 \times 2.0 = 48\ \text{m}$, which matches step 9. The ratio of output work to input work, $2000 / 2778 = 0.72$, matches the overall efficiency in step 5. The operator pulls about 58 N, which is a modest force, and the price is a long pull of 48 m.

## Lessons for engineers today

The formulas stay the same in every machine, from a bicycle crank to a hydraulic excavator. Engineers write IMA first, then add efficiency to predict the real force. They also check the travel distance, because a machine that saves force always costs distance. Friction changes the answer most in screws and in long chains of stages, so engineers measure efficiency for the real parts, not only the ideal ones.

## Practice

1. A lever has a 1.6 m effort arm and a 0.4 m load arm. Find its ideal mechanical advantage.
2. A ramp is 4.0 m long and rises 1.0 m. Ideally, how much force along the ramp lifts an 800 N load?
3. A pulley system has 3 supporting rope segments. Ideally, what effort lifts a 600 N load, and how far must the effort move to raise the load 2.0 m?
4. A screw has a 5 mm pitch, and its handle has a 0.25 m radius. Find the ideal mechanical advantage.
5. A compound machine uses a lever with IMA 5 and a pulley system with IMA 3. Ideally, what effort lifts a 900 N load?

<details><summary>Answers</summary>

1. IMA $= 1.6 / 0.4 = 4.0$.
2. $800 / 4.0 = 200\ \text{N}$.
3. Ideal effort $= 600 / 3 = 200\ \text{N}$. The effort moves $3 \times 2.0 = 6.0\ \text{m}$.
4. IMA $= 2\pi \times 0.25 / 0.005 = 314$, rounded from 314.2.
5. Total IMA $= 5 \times 3 = 15$. Ideal effort $= 900 / 15 = 60\ \text{N}$.

</details>

## Common mistakes

- Thinking a simple machine adds energy. The output work is always less than or equal to the input work, and friction makes it less.
- Using the lever arm length where the formula needs the distance from the fulcrum to the point where the force acts. Measure from the fulcrum, along the arm, to the load or effort.
- Multiplying the IMA of a compound machine by the efficiency of only one stage. The overall efficiency is the product of every stage efficiency.
- Confusing a fixed pulley with a movable pulley. A fixed pulley only changes direction, so its IMA is 1.
- Calling the inclined plane "free" force. The ramp reduces the force, but the load travels farther, and the work stays the same apart from friction.

## Go deeper

- [The Pneumatics of Hero of Alexandria](https://www.gutenberg.org/ebooks/77400), Project Gutenberg. Hero wrote about the first century CE, and the text describes working devices.
- [The Ten Books on Architecture](https://www.gutenberg.org/ebooks/20239) by Vitruvius, Project Gutenberg. Book X of the treatise covers lifting machines.
- [MIT OpenCourseWare](https://ocw.mit.edu/), free course materials from MIT, including engineering courses on mechanics.
- Related lessons: [Statics](../physics/01-statics.md), [Elevators and cranes](../applications/machines-robots/05-elevators-and-cranes.md), [Conveyors and automation](../applications/machines-robots/06-conveyors-and-automation.md).
- Next: [Ancient engineering](02-ancient-engineering.md).
- [History of engineering reference](reference.md): the lookup sheet for this topic.
