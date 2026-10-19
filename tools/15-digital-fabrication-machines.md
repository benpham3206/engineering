# Digital fabrication machines

**Type:** lesson
**Verify:** strict

A **digital fabrication machine** is a tool that makes a part by following instructions a computer wrote, instead of a hand guiding it. The 3D printers, laser cutters, and CNC routers in a makerspace are examples. An engineer who can run them turns a CAD model into a physical part in hours, and one who cannot run them safely can start a fire, breathe toxic fumes, or ruin a machine.

This lesson is for the operator. It covers how the machines work, how to run them, and how to choose among them. The physics of the printing processes is in [Additive manufacturing](../manufacturing/04-additive-manufacturing.md), and the cutting mechanics are in [Machining speeds and feeds](../manufacturing/02-machining-speeds-and-feeds.md).

**Prerequisites:** [Shop safety](../manufacturing/01-shop-safety.md), [CAD: SolidWorks and free alternatives](06-cad-solidworks.md), [Shop tools](08-shop-tools.md), [Additive manufacturing](../manufacturing/04-additive-manufacturing.md)
**Time:** 6-8 h

## Core ideas

### The digital chain

Every machine in this lesson sits at the end of the same chain. Each link changes the file into something closer to motion.

1. **CAD model.** A solid or a drawing, built in CAD to the dimensions of the part.
2. **Export.** For printing, the model is exported as a **mesh**, a surface made of many small triangles (file types STL or 3MF). For cutting flat shapes, the outlines are exported as **vector** paths (file types DXF or SVG), which are curves and lines with no thickness.
3. **Slicer or CAM.** A **slicer** cuts a mesh into layers and plans the nozzle path for each. **Computer-aided manufacturing (CAM)** software plans the tool path for a cutter, with the speed, depth, and order of cuts. Both turn geometry into a plan for the machine.
4. **Machine code.** The plan is saved as a text file of commands, most often **G-code**. Each line is a move or a setting.
5. **Machine.** A controller reads the code and drives motors, heaters, spindles, or a laser.

A few lines of G-code show how plain it is.

```
G21            ; units are millimeters
G90            ; coordinates are absolute positions
G0 X10 Y10     ; move quickly to X = 10, Y = 10 without cutting
G1 X50 F1200   ; move in a straight line to X = 50 at a feed of 1200 mm/min
```

Read the code as the machine will, one line at a time. A wrong unit or origin here moves the tool to the wrong place, so the preview in the slicer or CAM software is the last check before the machine moves.

Three faults in this chain cause most failed jobs.

- **Units are lost.** A mesh file carries numbers and no units. A part exported in inches and read as millimeters comes out 25.4 times too small.
- **The mesh is not closed.** A slicer needs a **watertight** (closed, no gaps) surface. A model with holes in its skin may slice with missing walls.
- **The mesh is too coarse.** Triangles approximate curves. A circle exported with too few triangles prints as a polygon. Lower the export tolerance until a curve looks smooth in the preview.

### FDM 3D printers

A **fused deposition modeling (FDM)** printer melts plastic filament and lays it down in lines, layer on layer (see [Additive manufacturing](../manufacturing/04-additive-manufacturing.md) for the process). The main parts are:

- the **frame and motion system**, which positions the nozzle in X, Y, and Z.
- the **build plate** (bed), the surface the first layer sticks to. It is often heated.
- the **extruder**, a motor and gear that pushes filament forward.
- the **hot end**, a heater block and nozzle that melts the plastic. It is hot enough to burn skin on contact, and it stays hot after a print ends.
- the **cooling fan**, which hardens each line after it is placed.
- the **controller**, which reads the G-code.

Run a first print safely this way. Pick a small test model, load the filament the slicer profile names, clean the bed, and watch the whole first layer. Keep hands out of the build area while it moves, and touch the nozzle only when the machine reports it cool.

#### Slicer settings that matter

| Setting | What it does | Typical choice and effect |
|---|---|---|
| Layer height | Thickness of each layer | Often 25 to 75 percent of the nozzle diameter. Thinner gives a smoother surface and a longer print. Thicker is faster and rougher |
| Wall count (perimeters) | Number of outlines printed around each layer | 2 to 4. Walls carry most bending and tensile load, so more walls add strength faster than more infill |
| Infill | Pattern and density that fill the inside | 10 to 30 percent for most parts. Higher density adds mass and time and gives diminishing strength |
| Supports | Temporary material under overhangs | Needed for steep overhangs and bridges. Costs time, material, and surface finish where they touch |
| Orientation | Which face sits on the bed | Sets the layer direction, the supports, and the strength (see below) |
| Bed adhesion aid | Brim (a ring of extra first-layer lines) or raft (a printed base) | A brim stops edges lifting. A raft helps on a poor bed but leaves a rough bottom face |

Layer height is bounded by the nozzle. A line is squashed flat against the layer below, so a layer much thinner than the nozzle makes it bulge, and one thicker than the nozzle diameter cannot be filled. The 25 to 75 percent range is a rule of thumb, and each machine's profile gives its own limits.

#### Orientation and strength

A printed part is **anisotropic**, meaning its strength depends on direction. Along a printed line, the plastic is continuous. Between two layers, the plastic only fused to the layer below while still warm, so that interface is the weak plane. A part loaded in tension across the layers breaks at a layer line at a fraction of the strength along the lines. Orient the part so the main load runs along the layers, and add fillets so a layer line does not meet a sharp corner. A hook that hangs from a printed shaft stands upright for looks but fails across the layers, while the same hook printed lying down is much stronger.

Orientation also trades against supports and finish. A round hole with its axis along the build direction prints round, and one lying sideways sags at the top without support.

#### Bed adhesion and the first-layer check

The first layer decides the print. If it does not stick, the part shifts or peels. If it is pressed too hard, the part flares at the base.

1. Clean the bed of dust and finger oils with the cleaner the shop names.
2. Level the bed (manually or by the machine's probe) so the nozzle is the same height above every corner of the plate.
3. Set the nozzle height so the first line is slightly squashed. It should look like a flat, smooth band, with neighboring lines touching.
4. Print a thin single-layer square. Look at it before starting the real part. Lines that are round and apart mean the nozzle is too high. Lines that are wavy and ridged mean it is too low.

Stay at the machine for the first layer, then check back at the start of each hour.

#### Common FDM failures and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| First layer will not stick, or peels | Dirty or unlevel bed, nozzle too high, bed too cool | Clean, relevel, lower the nozzle, check bed temperature, add a brim |
| Corners lift during printing (warping) | Plastic shrinks as it cools and pulls the base up | Brim, heated bed, enclosure, fewer drafts, a plastic with less shrinkage |
| Thin strings between features | Plastic oozes during travel moves | Lower nozzle temperature, enable retraction, dry the filament |
| Gaps and thin walls (under-extrusion) | Partial clog, worn extruder gear, filament too thick for the setting, nozzle too cold | Clear or replace the nozzle, check the filament path, raise the temperature a little |
| Shifted layers | Belt slipped or the head hit a curled part | Tighten belts, slow down, reduce travel over printed parts |
| Printed part detaches and a tangle forms (spaghetti) | Adhesion failed mid-print | Stop the print. Fix adhesion and restart |
| Wet filament: bubbles, popping sounds, rough surface | Filament absorbed moisture | Dry the spool and store it sealed |

Stop the machine, do not open it by hand while moving, and let the nozzle cool before clearing a jam.

#### Estimating time and material

The slicer reports time and mass, but an engineer should be able to check them. A nozzle extrudes a line of width $w$ and height $t$ moving at speed $v$, so the volume rate is $Q = w\,t\,v$. The printed volume $V_{dep}$ is the walls and skins plus the infill fraction of the interior. Time is the volume divided by the rate, multiplied by an overhead factor $k_o$ for acceleration, travel moves, and layer changes. Mass is the printed volume times the filament density.

### Resin (SLA and MSLA) printers

A **resin printer** cures liquid photopolymer with light, one layer at a time (see [Additive manufacturing](../manufacturing/04-additive-manufacturing.md)). In **masked stereolithography (MSLA)**, a screen shows each layer as a pattern of ultraviolet light under a vat of resin, and the build plate lifts the part out of the vat. These printers make fine detail and smooth surfaces, and they also bring chemistry hazards into the shop.

> [!WARNING]
> Uncured resin is a skin and eye irritant, and repeated skin contact can cause a lasting allergy to it. Wear nitrile gloves and eye protection, work with ventilation, and keep resin and solvent off bare skin and off shared surfaces such as keyboards and door handles. Wash skin with soap and water after contact, and follow the safety data sheet of the resin and of the cleaning solvent. Never pour liquid resin or wash solvent down a drain.

The post-processing steps are required, not optional.

1. **Drain** the part over the vat, then remove it from the plate with the scraper while wearing gloves.
2. **Wash** it in the solvent the resin calls for (often isopropyl alcohol, or water for water-washable resin) to remove uncured resin from the surface. Isopropyl alcohol is highly flammable, and its vapor is heavier than air. Keep wash containers closed and away from ignition sources, including heaters in curing stations. Wash for the time the resin maker gives, because long soaking can soften or crack some parts.
3. **Dry** the part and **cure** it under ultraviolet light for the stated time. Curing finishes the chemistry, and an uncured part stays weak and sticky and still irritates skin. Do not open a curing station while its ultraviolet light is on, because the light can injure eyes and skin.
4. **Remove supports** after washing, before or after curing as the resin maker states.
5. **Dispose** of used wipes, gloves, and failed prints as the shop instructs. A common rule is to cure waste resin in light until solid before it goes in the trash.

Resin parts are usually more brittle than FDM parts, and they are not usually food safe or load rated for hard use.

### Laser cutters

A **laser cutter** focuses a beam of light so intense that it burns or vaporizes the material at one point, and moves that point along a path. The beam from a typical shop CO2 laser is invisible infrared, at a wavelength of about 10 micrometers. It cuts and engraves wood, paper, cardboard, acrylic, and some fabrics and leathers, but cuts metal poorly.

The same file can make two different kinds of mark, and the software chooses by the line's color or layer setting.

- **Vector cut.** The beam follows a line and cuts through the material along it. The path must be a thin line (a hairline) in the file.
- **Raster engrave.** The beam sweeps back and forth like a printer head, burning shallow marks that make an image. Filled areas and pictures engrave in this mode. It takes much longer than a cut of the same area, because the head covers the whole area.

#### Kerf

The beam removes a thin strip of material, called the **kerf**. A path cut on the line leaves a piece smaller by the kerf, and a hole larger by the kerf. For parts that must fit together (slots, tabs, press fits), measure the kerf and offset the drawing to compensate.

1. Cut a test square of known drawn size $d$ on the material and thickness you will use.
2. Measure the piece with calipers to get $d_m$.
3. The kerf is $k = d - d_m$.
4. Offset the drawing, by drawing outside shapes larger by $k$ and inside shapes (holes and slots) smaller by $k$. That moves each edge by $k/2$, which is the half of the kerf that the beam removes on each side of the line.

Kerf changes with the material, its thickness, the power, the speed, and the focus, so measure it again whenever these change.

#### Focus and settings

The beam is narrowest at one distance from the lens, the **focal distance**. Set the material surface at that distance with the gauge or auto-focus the machine provides. A blurred focus widens the kerf, cuts less deeply, and burns more. Power and speed trade against each other. Too slow or too hot burns edges and risks fire, and too fast or too cold leaves the cut incomplete. Start from the shop's setting for the material, run a small test, and change one setting at a time.

#### Materials that must never be cut

Some materials give off gases that are toxic to people or corrosive to the machine when heated by a laser. Cut a material only if the shop lists it as approved and you know exactly what it is.

- **Chlorine- or fluorine-containing plastics, including PVC, vinyl, and fluoropolymers such as PTFE.** Heating these halogenated plastics can release corrosive or toxic fumes. PVC releases hydrogen chloride, which forms hydrochloric acid on contact with moisture and corrodes the laser's optics, rails, and electronics. Heating PTFE can release hydrogen fluoride. If you cannot tell what a plastic is, do not cut it.
- **ABS, polycarbonate, polystyrene foam, and HDPE.** ABS can release hydrogen cyanide. Polycarbonate can catch fire and discolor, while polystyrene foam and HDPE can melt and catch fire. Do not assume a labelled sheet is safe; cut only materials the shop lists as approved.
- **Any plastic or sheet of unknown type.** A scrap with no label, or a sheet without a safety data sheet, stays out of the machine.
- **Carbon fiber and fiberglass sheet.** The resin binders and fibers give off harmful fumes and dust.
- **Leather tanned with chromium, and coated or laminated boards of unknown glue.** The coating decides the fumes, not the board under it.

> [!WARNING]
> The beam inside an enclosed laser cutter is class 4 and can blind you instantly; the enclosure and interlock contain it. An open-frame laser does not provide that protection. Everyone in the room must wear eyewear rated for that laser's wavelength and optical density. Never leave a laser cutter running. Stay within reach of its stop button and the shop's fire extinguisher, keep the lid closed, turn on the exhaust and air assist, and clear scraps from the bed before cutting. If a flame appears, stop the job and turn off the air assist. If the fire does not go out at once, leave the room, raise the alarm, and call emergency services. Use the shop-provided extinguisher, often CO2, only if you are trained and can do so safely. Never defeat the lid interlock.

### CNC routers

A **computer numerical control (CNC) router** moves a spinning cutter through sheet or block material along a path from CAM. It cuts wood, plastics, foam, and soft metals such as aluminum on rigid machines, and it makes flat parts, pockets, and carved relief.

- **Workholding.** The sheet must not move. Use screws into a sacrificial **spoilboard** (a board under the work that the cutter may touch), clamps outside the cutter path, a vacuum table, or tabs that hold the part to the sheet until the end. Check that no clamp lies on the tool path before the program runs.
- **Work origin.** Tell the machine where the part is by setting the X, Y, and Z zero on the material. Setting Z to the top of the work or to the spoilboard decides the depth of every cut, so set it carefully.
- **Cutters.** An up-cut bit lifts chips out of the slot, a down-cut bit presses the top face down for a clean top edge, and a compression bit does both. Match the bit to the material.
- **Climb versus conventional milling.** In **climb milling**, the cutter turns the same way as the feed, so each tooth bites in at full chip thickness and leaves thin. It leaves a cleaner edge, but it can pull the tool into the work on a machine with slack. In **conventional milling**, the cutter turns against the feed, so each chip starts thin and ends thick, and the cutter pushes away from the work. It is safer on light, loose machines and leaves a rougher edge. CAM software sets the direction, so check the setting against what you intend.
- **Feeds and speeds.** Spindle speed and feed per tooth set the chip size. Take starting values from the cutter maker's table for the material, and see [Shop tools](08-shop-tools.md) and [Machining speeds and feeds](../manufacturing/02-machining-speeds-and-feeds.md) for the method. Too slow a feed rubs and burns the material, and too fast a feed breaks the bit.

Router safety follows the rules of [Shop safety](../manufacturing/01-shop-safety.md). Wear eye and hearing protection, tie back hair, and keep sleeves close. Never reach into the machine while the spindle is on. Know where the emergency stop is before you press start. Use dust collection, because fine wood and board dust harms lungs. Stay at the machine for the cut, and stop at once if the sound changes.

### Vinyl cutters and waterjets

A **vinyl cutter** drags a small knife along a vector path through thin sheet such as adhesive vinyl, paper, or film. It cuts a design out of a sheet, then the user **weeds** (peels away) the waste and lifts the design with transfer tape. It makes labels, decals, and stencils. A **kiss cut** goes through the film and not the backing, and a through-cut goes through both. The knife is sharp, and the cut depth and force need setting for each material.

A **waterjet** cuts with a very fast stream of water, usually carrying fine abrasive grit, aimed through a small nozzle. It cuts almost any material, including thick metal, stone, and glass, with no heat-affected zone, because the water carries the heat away. It is slower than a laser on thin sheet, the edge tapers a little on thick work, and the process is wet and noisy. The jet can injure at close range, so the operator stays out of the cutting area and uses only the interlocked enclosure and the controls the shop teaches.

### Choosing the machine

The ranges below are typical values for shop and benchtop machines. They vary with machine, calibration, material, and operator, so test a part before relying on a tolerance.

| Machine | Part type | Material | Typical tolerance | Speed |
|---|---|---|---|---|
| FDM printer | Any 3D shape, enclosed cavities, one-off prototypes | Thermoplastics such as PLA, PETG, ABS, nylon | 0.1 to 0.5 mm | Slow, hours for a palm-sized part |
| Resin printer | Fine detail, small smooth parts | Photopolymer resin | 0.05 to 0.2 mm | Slow, hours, plus washing and curing |
| Laser cutter | Flat parts and engraving, from thin sheet | Wood, paper, acrylic, some fabrics | 0.1 to 0.3 mm | Fast on thin sheet, minutes |
| CNC router | Flat parts, pockets, and relief from sheet or block | Wood, plastics, foam, soft metals | 0.1 to 0.3 mm | Moderate, minutes to an hour |
| Vinyl cutter | Decals and stencils from thin film | Adhesive vinyl, paper, film | 0.2 to 0.5 mm | Fast, minutes |
| Waterjet | Flat parts in thick or hard material | Metal, stone, glass, composites | 0.1 to 0.3 mm | Slow on thick stock, minutes to hours |

Use the table in this order.

1. Is the part flat, cut from a sheet? Choose a laser cutter, router, waterjet, or vinyl cutter. Is it a 3D shape with internal features? Choose a printer.
2. What is the material? It rules out machines first. A PVC sheet must not go in a laser cutter.
3. What tolerance and finish does the part need? Fits need a measured kerf or a finishing step, and sliding fits need a test piece.
4. How many parts, and how soon? One part favors a printer, and many flat parts favor cutting.

## Key equations

Symbols: $w$ = extruded line width (mm), $t$ = layer height (mm), $v$ = print speed (mm/s), $Q$ = volume rate ($\text{mm}^3$/s), $V_{dep}$ = printed volume ($\text{mm}^3$ or $\text{cm}^3$), $k_o$ = overhead factor (dimensionless), $T$ = print time (s), $\rho$ = filament density ($\text{kg/m}^3$, often written as $\text{g/cm}^3$), $m$ = printed mass (kg or g), $h$ = part height (mm), $n$ = number of layers, $d$ = drawn size (mm), $d_m$ = measured size (mm), $k$ = kerf (mm), $N$ = spindle speed (1/min), $z$ = number of cutter teeth, $f_z$ = chip load per tooth (mm), $v_f$ = feed rate (mm/min).

Volume rate at the nozzle, printed volume, time, and mass for an FDM part, holding for steady printing at one setting:

$$
Q = w\,t\,v, \qquad V_{dep} = V_{walls} + \phi\,V_{interior}, \qquad T = k_o\frac{V_{dep}}{Q}, \qquad m = \rho\,V_{dep}
$$

Here $V_{walls}$ is the volume of the walls and solid skins, $V_{interior}$ is the volume inside them that infill fills, and $\phi$ is the infill fraction. The number of layers is $n = h/t$.

Kerf from a test cut, and the drawn size that gives a wanted cut size $d_{want}$, holding when the kerf is the same on both sides of the line:

$$
k = d - d_m, \qquad d_{outside} = d_{want} + k, \qquad d_{inside} = d_{want} - k
$$

Router feed rate from spindle speed, tooth count, and chip load, holding when every tooth takes the same cut:

$$
v_f = N\,z\,f_z
$$

## Worked example

### Estimating an FDM print

A block of 40 mm by 30 mm by 20 mm is printed with a 0.4 mm line width, a 0.2 mm layer height, a speed of 50 mm/s, and 20 percent infill. The slicer shows the walls and solid top and bottom skins as 8.0 $\text{cm}^3$ and the interior they enclose as 16 $\text{cm}^3$. The filament has a density of 1.24 $\text{g/cm}^3$ (a typical value for the plastic, which the spool's datasheet states). Travel, acceleration, and layer changes add an overhead factor of 1.3.

**Given:** $w = 0.4$ mm, $t = 0.2$ mm, $v = 50$ mm/s, $\phi = 20$ percent, $V_{walls} = 8.0$ $\text{cm}^3$, $V_{interior} = 16$ $\text{cm}^3$, $\rho = 1.24$ $\text{g/cm}^3$, $k_o = 1.3$, $h = 20$ mm.

**Find:** The number of layers, the printed volume, the mass, and the print time.

**Assumptions:** Steady extrusion at the stated speed, the slicer's volumes are correct, and the overhead factor is an estimate.

**Solution:**

1. Layers: $n = h/t = 100$.
2. Printed volume: $V_{dep} = 8.0 + 0.20 \times 16 = 11.2$ $\text{cm}^3$.
3. Mass: $m = \rho V_{dep} = 13.9$ g.
4. Volume rate: $Q = w\,t\,v = 4.0$ $\text{mm}^3$/s.
5. Ideal time: $V_{dep}/Q = 46.7$ min. With overhead, $T = k_o \times 46.7 = 60.7$ min.

**Answer:** 100 layers, 11.2 $\text{cm}^3$ of plastic, 13.9 g, and about 60.7 min.

**Sanity check:** A solid block would hold 24 $\text{cm}^3$ and weigh 29.8 g, so the infilled block is lighter, as it should be. The time is a little over an hour, which is a plausible order of magnitude for a small block, and a slicer estimate within a few tens of percent of it is normal. A big gap means a wrong setting, such as the wrong speed or line width.

<details><summary>Verification</summary>

```verify
w = q(0.4, "mm")
t = q(0.2, "mm")
v = q(50, "mm/s")
phi = q(20, "percent")
Vwalls = q(8.0, "cm^3")
Vint = q(16, "cm^3")
rho = q(1.24, "g/cm^3")
ko = q(1.3, "1")
h = q(20, "mm")
lx = q(40, "mm")
ly = q(30, "mm")
expect(lx * ly * h, "24 cm^3")
n = h / t
expect(n, "100 1")
Vdep = Vwalls + phi * Vint
expect(Vdep, "11.2 cm^3")
m = rho * Vdep
expect(m, "13.9 g")
Q = w * t * v
expect(Q, "4.0 mm^3/s")
Tideal = Vdep / Q
expect(Tideal, "46.7 min")
T = ko * Tideal
expect(T, "60.7 min")
expect(rho * (Vwalls + Vint), "29.8 g")
check(m < rho * (Vwalls + Vint), "infilled block is lighter than a solid block")
```

</details>

### Compensating laser kerf

A tab and a slot must each be 12.00 mm wide to fit a plywood joint. To measure the kerf, a 20 mm square is drawn and cut from the same sheet, and the cut-out piece measures 19.82 mm.

**Given:** $d = 20$ mm, $d_m = 19.82$ mm, $d_{want} = 12.00$ mm.

**Find:** The kerf, the drawn width of the tab, and the drawn width of the slot.

**Assumptions:** The kerf is the same on both sides of every line, and the settings and focus are the same as in the test cut.

**Solution:**

1. Kerf: $k = d - d_m = 0.18$ mm.
2. The tab is a piece, so the beam removes material from outside the line and the piece comes out smaller. Draw it larger: $d_{outside} = 12.00 + 0.18 = 12.18$ mm.
3. The slot is a hole, so the beam removes material inside the line and the hole comes out larger. Draw it smaller: $d_{inside} = 12.00 - 0.18 = 11.82$ mm.

**Answer:** The kerf is 0.18 mm. Draw the tab 12.18 mm wide and the slot 11.82 mm wide.

**Sanity check:** Cutting the drawn tab gives $12.18 - 0.18 = 12.00$ mm, and cutting the drawn slot gives $11.82 + 0.18 = 12.00$ mm. A plain press fit also needs the slot a few hundredths of a millimeter smaller, found by a test joint.

<details><summary>Verification</summary>

```verify
d = q(20, "mm")
dm = q(19.82, "mm")
dwant = q(12.00, "mm")
k = d - dm
expect(k, "0.18 mm")
dout = dwant + k
expect(dout, "12.18 mm")
din = dwant - k
expect(din, "11.82 mm")
expect(dout - k, "12.00 mm")
expect(din + k, "12.00 mm")
check(dout > dwant and din < dwant, "pieces are drawn larger and holes smaller")
```

</details>

## Practice

1. A part deposits 18 $\text{cm}^3$ of PETG, which has a density of 1.27 $\text{g/cm}^3$. Find the mass of plastic, in g.
2. A print uses a 0.45 mm line width, a 0.3 mm layer height, and a speed of 60 mm/s, and deposits 9720 $\text{mm}^3$. Find the ideal print time, in min, with no overhead.
3. A 25 mm square is laser cut and the piece measures 24.78 mm. Find the kerf, and the drawn size of a hole that must cut to 8.00 mm.
4. A printed hook will hang from a hole and carry a pull along its shaft. Should the shaft be printed standing up or lying flat on the bed? Give the reason in one sentence.
5. A router with a 2-flute cutter turns at 18000 1/min. The cutter maker's table gives a chip load of 0.05 mm per tooth. Find the feed rate, in mm/min.

<details><summary>Answers</summary>

1. 22.9 g
2. 20.0 min
3. Kerf 0.22 mm, so the hole is drawn at 7.78 mm
4. Lying flat, so the layers run along the shaft and the pull is along the strong printed lines, not across the weak layer interfaces
5. 1800 mm/min

```verify
rho = q(1.27, "g/cm^3")
V = q(18, "cm^3")
expect(rho * V, "22.9 g", ans=1)
w = q(0.45, "mm")
t = q(0.3, "mm")
v = q(60, "mm/s")
Vdep = q(9720, "mm^3")
Q = w * t * v
expect(Vdep / Q, "20.0 min", ans=2)
d = q(25, "mm")
dm = q(24.78, "mm")
k = d - dm
expect(k, "0.22 mm", ans=3)
expect(q(8.00, "mm") - k, "7.78 mm", ans=3)
skip(ans=4, why="short answer")
N = q(18000, "1/min")
z = q(2, "1")
fz = q(0.05, "mm")
expect(N * z * fz, "1800 mm/min", ans=5)
```

</details>

## Common mistakes

- Trusting the units of an exported mesh. Check the size of the part in the slicer against the CAD dimension before slicing.
- Starting a print and walking away before the first layer is down and stuck.
- Printing a loaded part with its layers across the load path, then blaming the plastic for the break.
- Using more infill to fix a weak part, when more walls or a better orientation would do more.
- Skipping the wash and cure of a resin part, or handling resin with bare hands.
- Cutting an unknown or vinyl sheet in a laser cutter, or leaving a running laser unattended.
- Drawing a laser joint at its nominal size without measuring and compensating the kerf.
- Placing a router clamp on the tool path, or setting the Z zero at the wrong surface so the first cut goes too deep.

## Go deeper

- [Additive manufacturing](https://www.nist.gov/additive-manufacturing) by NIST: the national measurement institute's page on additive manufacturing research and standards.
- [How to Make (Almost) Anything](https://ocw.mit.edu/courses/mas-863-how-to-make-almost-anything-fall-2002/) by MIT OpenCourseWare: a free course covering 3D printing, laser cutting, and computer-controlled machining.
- Previous: [Software skills for engineers](12-software-for-engineers.md), [Shop tools](08-shop-tools.md).
- Related: [Additive manufacturing](../manufacturing/04-additive-manufacturing.md), [Machining speeds and feeds](../manufacturing/02-machining-speeds-and-feeds.md), [Machining processes](../manufacturing/03-machining-processes.md), [Sheet metal](../manufacturing/07-sheet-metal.md), [Shop safety](../manufacturing/01-shop-safety.md).
