# Machinist bench tools

**Type:** lesson

**Machinist bench tools** are the hand tools and fixtures a machinist uses at a workbench to hold, locate, thread, and finish a part. Engineers who know what these tools can do avoid designs that cost extra time to hold, thread, or finish.

A machinist spends much of the day holding parts, finding edges, cutting threads, and checking holes. The bench tools for those jobs are cheap, and each one has a correct way to use it. As a designer, you need to know what these tools can and cannot do, so you draw parts they can actually make.

**Prerequisites:** [Measurement tools](07-measurement-tools.md), [Shop tools](08-shop-tools.md), and [Machining speeds and feeds](../manufacturing/02-machining-speeds-and-feeds.md).
**Time:** 6-10 h of reading, plus supervised practice in a shop

## Core ideas

Read the [measurement lesson](07-measurement-tools.md) and the [shop tools lesson](08-shop-tools.md) first. This lesson does not repeat calipers, micrometers, or the basics of spindle speed. It covers the hand tools and fixtures that hold, locate, thread, and finish a part.

> [!WARNING]
> Safety rules come first. Ask your instructor for the shop's rules, which override anything written here. Read the [OSHA machine guarding overview](https://www.osha.gov/machine-guarding), which says that any part of a machine that could injure a worker must be guarded.

### Workholding

**Workholding** means holding the part so it cannot move while the tool cuts it.

- **Machine vise.** A vise has a fixed jaw and a movable jaw. It clamps the part against the bottom parallels, which lift the part off the bed so the cutter does not hit the vise.
- **Soft jaws.** These are jaw inserts, often made of aluminum or another soft metal. You machine them to match the shape of the part, so the clamping force spreads over a larger area and the part does not mark or slip.
- **Parallels.** These are precision bars with flat, parallel faces. They lift and support the part so it sits square and at a known height.
- **V-blocks.** These hold round stock. The V shape centers the round part, and the clamp holds it against the V.
- **1-2-3 blocks.** These are steel blocks with three faces in a 1 in, 2 in, and 3 in ratio, so you can build a known height quickly by stacking them.
- **Step clamps.** These are steel clamps with stepped bodies. They press down on the part while the bolt passes through a slot in the table.
- **Angle plates.** These are L-shaped steel fixtures. They hold a part at 90 degrees to the table so you can drill or mill a face that is square to another face.

### Locating and setup

Setup means finding where the part is relative to the machine, so each cut lands where the drawing says.

- **Edge finder.** This tool touches the edge of the part to find its position. A spring-loaded tip offsets from the true edge by a known amount, which is the finder's radius. Add or subtract that offset from the reading.
- **Dial test indicator (DTI).** A DTI has a lever with a tip that moves in a pivoting arc. It is good for checking runout and small side-to-side movement.
- **Plunger dial indicator.** This indicator has a plunger that moves straight along its axis. It is good for measuring height, depth, and flatness in one direction.
- **Tramming a vise.** Tramming means making the fixed jaw parallel to the machine's axis of travel. You clamp a test indicator in the spindle, sweep it across the jaw, and adjust the vise until the reading stays constant.
- **Indicating a bore.** You put a test indicator in the bore, turn the spindle by hand, and read the runout. A bore that is out of line shows up as a changing reading.

### Threading

A tapped hole has internal threads. A die cuts external threads on a rod or bolt.

- **Taper tap.** The first tap, with a long chamfer. It starts the thread in a blind or through hole.
- **Plug tap.** The second tap, with a shorter chamfer. It cuts a full thread in a through hole, or deeper in a blind hole.
- **Bottoming tap.** The last tap, with almost no chamfer. It cuts the thread to the bottom of a blind hole.
- **Tap drill.** The drill that makes the hole for the tap. Its size sets how much of the thread the tap cuts. A larger drill cuts less thread and takes less torque. A smaller drill cuts more thread and takes more torque.
- **Dies.** Die threads are cut on the outside of round stock. A die is held in a die stock and turned by hand or machine.
- **Thread gauges.** A go gauge should screw in the whole length of the thread. A no-go gauge should not enter the thread past the first turn. Use them to check the thread after tapping.
- **Thread repair inserts.** A helical insert is a coil of wire that you screw into a damaged tapped hole. It restores the original thread size. You drill out the old hole, tap a larger thread, and install the insert.

Thread size is a **major diameter** (outside of the thread) and a **pitch** (distance between threads). For metric threads, the pitch is in millimeters. For inch threads, the **threads per inch (TPI)** is the count per inch.

### Hole finishing

- **Reamers.** A reamer enlarges a drilled hole and makes it straight and round to a close tolerance. A reamed hole must start from a drilled hole that is slightly undersized. If the drilled hole is too large, the reamer has nothing to cut and rides on the hole wall, which leaves a rough or tapered bore. Follow the reamer maker's drill chart for the right undersize.
- **Countersinks.** A countersink cuts a cone at the top of a hole so a flat-head screw sits flush.
- **Counterbores.** A counterbore cuts a flat-bottomed step, so a socket-head cap screw sits below the surface.
- **Spot drills.** A short, stiff drill that makes a shallow starter hole. It locates the drill point so the drill does not wander.

### Deburring and filing

- **File cuts.** A file's cut is the number of teeth per inch and the coarseness. The coarse cut is bastard, then second cut, then smooth, then dead smooth. Pick the cut to match how much material you remove.
- **Draw filing.** You hold the file with both hands, push it along the length of the part, and keep the strokes long and straight. It leaves a smooth finish and removes burrs without rounding edges.
- **Deburring tools.** These include a hand scraper, a chamfer tool, and a rotary deburring tool. They remove the sharp edge a drill or mill leaves behind.

### Hand tools

- **Hacksaw blades.** Blade TPI is set by the thickness of the work. A rule of thumb is to have at least three teeth in contact with the work at once. Thin work needs a fine blade. Thick work needs a coarse blade so the chips clear.
- **Mallets.** A soft-faced mallet, made of plastic, rubber, or copper, drives a part without marking it. Do not use a steel hammer on a hardened part.
- **Punches.** A center punch marks a drill location. A drift punch drives a pin out of a hole.
- **Torque wrench.** A torque wrench tightens a fastener to a set value. Set it to the value the drawing gives. Store it at its lowest setting, because a spring left under load loses accuracy. Do not use it to loosen a bolt. Check its calibration on a schedule.

### Bench habits

- Clear chips with a brush, not your hands. Chips are sharp and hot.
- Never blow chips off with compressed air toward your face or another person.
- Clean the part and the gauge before you measure. A chip under a gauge block adds an error larger than most tolerances.
- Keep tools in a known place. A missing tool costs more time than the tool costs to replace.

## Key equations

Tap drill from the rule used in most metric and inch charts. The rule has the same form for both systems:

Metric:

$$d_{\text{tap}} = D - P$$

Inch:

$$d_{\text{tap}} = D - \frac{1}{N}$$

Here $d_{\text{tap}}$ is the tap drill diameter, $D$ is the thread major diameter, $P$ is the metric pitch in mm, and $N$ is the threads per inch (TPI). Use the same length unit for $D$ and $P$, and for $D$ and $1/N$. For inch threads, $1/N$ is the pitch in inches.

> [!NOTE]
> The rule gives a usable starting size. Commercial tap drill charts publish the exact drill for each thread. Use the chart when one exists.

## Worked example

**Given:**
- An $\mathrm{M6} \times 1.0$ thread (major diameter 6.0 mm, pitch 1.0 mm).
- An $\mathrm{M10} \times 1.5$ thread (major diameter 10.0 mm, pitch 1.5 mm).
- A 1/4-20 thread (major diameter 0.25 in, 20 threads per inch).

**Find:** The tap drill for each thread. Give the metric drills in mm and the 1/4-20 drill in inches.

**Assumptions:** The rule $d = D - P$ (or $D - 1/N$) is a starting size. The 1/4-20 value is also checked against the common chart value.

**Solution (run in Python):**

```python
# metric rule: tap drill = major - pitch
for name, D, P in [("M6x1.0", 6.0, 1.0), ("M10x1.5", 10.0, 1.5)]:
    d = D - P
    print(name, "tap drill =", round(d, 3), "mm")

# inch rule: tap drill = major - 1/N
D, N = 0.25, 20
d = D - 1 / N
print("1/4-20 rule =", round(d, 4), "in =", round(d * 25.4, 3), "mm")
print("#7 chart value = 0.201 in =", round(0.201 * 25.4, 3), "mm")
```

Output:

```
M6x1.0 tap drill = 5.0 mm
M10x1.5 tap drill = 8.5 mm
1/4-20 rule = 0.2 in = 5.08 mm
#7 chart value = 0.201 in = 5.105 mm
```

**Answer:**
- $\mathrm{M6} \times 1.0$: tap drill 5.0 mm.
- $\mathrm{M10} \times 1.5$: tap drill 8.5 mm.
- 1/4-20: the rule gives 0.200 in. The common chart value is a #7 drill, 0.201 in. Use the #7 drill as a typical value. It is the drill you will find on the shop shelf.

**Sanity check:** The rule removes one pitch from the diameter. Each metric thread has a pitch of 1.0 mm, so the drill is 1.0 mm smaller in diameter, which is 0.5 mm smaller in radius. That matches a thread that is a little under full depth, which is what the tap needs. The 1/4-20 value of 0.200 in is within 0.001 in of the #7 chart value, so the rule and the chart agree.

A note on engagement: shops describe this rule as giving about 75 percent thread. Percent thread is measured against a full thread height of $0.6495P$, so for $\mathrm{M6} \times 1.0$ it is $(6.0 - 5.0)/(2 \times 0.6495 \times 1.0) \approx 77$ percent. That is close to the strength of a full thread while making the tap far less likely to break. For a critical thread, use the chart value for the thread you are cutting.

## Practice

1. Find the tap drill for an $\mathrm{M8} \times 1.25$ thread, in mm.
2. Find the tap drill for an $\mathrm{M12} \times 1.75$ thread, in mm.
3. Find the tap drill for a 3/8-16 thread, in inches, using the rule $D - 1/N$.
4. Convert the $\mathrm{M6} \times 1.0$ tap drill of 5.0 mm to inches, to four decimal places.
5. A hacksaw blade has 24 TPI. The work is a tube wall 0.125 in thick. How many teeth are in contact with the work, and does the blade meet the rule of at least three?

<details><summary>Answers</summary>

1. 6.75 mm
2. 10.25 mm
3. 0.3125 in
4. 0.1969 in
5. 3.0 teeth. Yes, exactly at the minimum of three.

</details>

## Common mistakes

- Using the tap drill chart value for a different thread pitch. Check the pitch and the TPI first.
- Drilling a hole for a reamer at the final size. A reamer needs an undersized starter hole, or it rides on the wall and leaves a poor bore.
- Using a steel hammer on a hardened part, which chips the part or sends fragments flying. Use a soft-faced mallet.
- Storing a torque wrench at a high setting, which weakens the spring and throws off the reading.
- Measuring a part before it is clean, so a chip or oil film adds a false error to the reading.

## Go deeper

- [OSHA: Machine guarding](https://www.osha.gov/machine-guarding) by the U.S. Department of Labor: the guarding requirement for every machine you run.
- [*NIST Special Publication 811*](https://www.nist.gov/pml/special-publication-811) by NIST: the official guide for using SI units, which you need when you convert mm and inches.
- [*Machining*](https://en.wikibooks.org/wiki/Machining) on Wikibooks: an open textbook on turning, milling, drilling, grinding, and inspection.
- [Measurement folder](../measurement/README.md): error and uncertainty, for the reading you take with an indicator or gauge.
- Related: [Measurement tools](07-measurement-tools.md), [Shop tools](08-shop-tools.md), [Manufacturing folder](../manufacturing/README.md).
- [Tools reference](reference.md): the lookup sheet for this topic.
