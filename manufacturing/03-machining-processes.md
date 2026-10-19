# Machining processes

**Type:** lesson

**Machining** is the family of processes that shapes a part by cutting away material with a tool. Engineers need to know which process to choose because each one sets the shape, accuracy, and cost of the finished part. Milling uses a rotating multi-tooth cutter on a stationary or moving workpiece. Turning spins the workpiece and holds a single-point tool against it. Drilling makes round holes with a rotating bit. **CNC (computer numerical control)** runs these operations from a program, so the same part can be made again and again with the same accuracy.

**Prerequisites:** [Shop safety](01-shop-safety.md), [Machining speeds and feeds](02-machining-speeds-and-feeds.md)
**Time:** 6-8 h

## Core ideas

- **Milling**: the cutter spins and the table moves the work past it. Face mills cut flat surfaces, end mills cut slots and pockets, and ball-end mills cut curves.
- **Turning**: the workpiece spins in a chuck or between centers, and the tool moves along or across it. Turning makes shafts, bushings, and other round parts.
- **Drilling**: a twist drill spins and feeds straight into the work. Drilling is usually a fast, simple operation, but chips must clear the hole, and the drill must be kept straight.
- **Boring and reaming**: boring enlarges and finishes an existing hole with a single-point tool. Reaming gives a smooth, accurate hole size. Both come after drilling.
- **Conventional and climb milling**: in conventional milling the cutter teeth move against the feed. In climb milling they move with the feed. Climb milling usually gives a better finish, but it needs a rigid machine and no backlash in the table screw.
- **Coordinate system**: CNC machines use axes $X$, $Y$, and $Z$. The program moves the tool to coordinates on each axis.

A CNC program is usually a list of blocks, each with a command code. Common codes include:

- `G00`: rapid move (move fast, no cutting).
- `G01`: linear feed move (cut in a straight line at a set feed rate).
- `G02` and `G03`: clockwise and counterclockwise arc moves.
- `M03` and `M05`: start and stop the spindle.
- `F`: feed rate. `S`: spindle speed.

A **CAM (computer-aided manufacturing)** program writes most CNC programs from a CAD model. An engineer should still know what the commands mean so the program can be checked by eye.

> [!WARNING]
> Workholding is a large part of any machining job. Vises, clamps, fixtures, and chucks hold the part so the cut does not move it. A poor hold causes chatter, poor finish, and dangerous part ejection.

## Checklist

Before you run a new CNC program or a new setup:

- Check the tool. Confirm diameter, length, and flute count match the program.
- Check the work offset. Confirm where the part's zero is on each axis.
- Dry-run the program with the spindle off, or in the simulator, and watch the tool path.
- Use a safe starting feed rate and override it down in the first run.
- Keep the guard closed. Stay at the controls. Be ready to hit feed hold or emergency stop.
- Measure the first part before you run a batch.

## Example

**Given:** A slot 10 mm wide, 40 mm long, and 10 mm deep must be cut in a block of 6061 aluminum (a common alloy) using a 10 mm, 3-flute end mill. The slot is a full-width cut in one pass. Starting values from the tool maker are $V = 250$ m/min and $f_z = 0.08$ mm/tooth.

**Find:** Which process to use, and the starting spindle speed and feed rate.

**Assumptions:** The machine is rigid, the work is clamped, and coolant is used.

**Solution:**

1. Process: a slot in a flat block is a milling operation, using an end mill.
2. Spindle speed (SI form):
$$N = \frac{1000 \times 250}{\pi \times 10} = 7958 \text{ rpm}$$
3. Feed rate:
$$f_m = 0.08 \times 3 \times 7958 = 1910 \text{ mm/min}$$

**Answer:** Mill the slot with an end mill at about 7960 rpm and a feed of about 1910 mm/min.

**Sanity check:** The slot width equals the tool diameter, so the cut is full width and the tool is at full radial engagement, and the 10 mm depth equals one tool diameter. Full-width slots load the tool heavily. Many machinists would reduce the depth per pass or the feed for the first run, so the 1910 mm/min is a ceiling, not a target.

## Practice

1. Which process would you pick to make a 25 mm diameter shaft from round bar stock? Give a one-word answer.
2. Which process makes a flat face on a block of steel?
3. A CNC program line reads `G01 X50 F300`. Describe the move in one sentence.
4. A 2-flute end mill runs at 6000 rpm with $f_z = 0.05$ mm/tooth. What is the feed rate in mm/min?
5. Why should you dry-run a new program before running the part?

<details><summary>Answers</summary>

1. Turning
2. Milling (face mill)
3. A straight feed cut to $X = 50$ at 300 units per minute
4. 600 mm/min
5. To check the tool path and offsets for crashes before the tool or part is at risk.

</details>

## Common mistakes

- Picking drilling when a bore or ream is needed. A drill alone does not hold a tight size.
- Forgetting the work offset. A wrong zero moves the whole program.
- Trusting the program without checking the tool length and diameter.
- Running with a loose clamp because the cut "looks light."
- Confusing `G00` with `G01`. A rapid move at the cutting depth can crash the tool.

## Go deeper

- [NIST: Manufacturing](https://www.nist.gov/manufacturing) by NIST: an overview of national manufacturing research, including machining and quality.
- [NASA Glenn Research Center](https://www.nasa.gov/glenn/) by NASA: a government research center with machining and manufacturing work, useful for real industry context.
- [Manufacturing reference](reference.md): the lookup sheet for this topic.
