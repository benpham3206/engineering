# Free engineering software

**Type:** lesson

**Free engineering software** is the set of no-cost programs that do the same jobs as paid engineering tools, such as CAD, simulation, spreadsheets, and programming. Knowing which free options exist lets a student or new engineer learn and work without a license budget.

You do not need expensive licenses to learn or do real engineering work. For almost every paid tool used in industry there is a free one that is capable enough for coursework, personal projects, and a lot of professional work. This lesson is a map of those tools, grouped by job.

> [!NOTE]
> Dated material (as of 2026). Software names, licenses, and free-plan terms change. The categories, the habits in Core ideas, and the open file formats will last much longer than any tool listed here. When a tool disappears, look for its replacement by job, not by name.

**Prerequisites:** none. Read [Starter kit](01-starter-kit.md) first if you have not set anything up yet.
**Time:** 2-3 h to read and install the core set, then ongoing

## Core ideas

- Free does not always mean **open source**. Open-source tools (FreeCAD, KiCad, OpenFOAM) are free for any use, forever. Free plans of commercial tools (Onshape, Fusion, SimScale, Ansys Student) have limits: non-commercial use only, public files, model size caps, or yearly renewal. Read the terms before you put real work in them.
- Learn the concept, not the button. Every parametric CAD tool has sketches, constraints, features, and assemblies. Every FEA tool has geometry, mesh, material, loads, boundary conditions, solve, and post-process. Skills move between tools far better than people expect.
- Prefer open file formats. Save neutral copies of your work: STEP for 3D CAD, DXF for 2D, STL or 3MF for printing, CSV for data, PDF for drawings and reports. A file you can only open in one program is a file you can lose.
- Pick one tool per job and get good at it. Installing ten CAD programs teaches you less than building twenty parts in one.

## The catalog

Each table lists free tools for one job, then the paid tool they replace. "Open source" means free for any use. Anything else has terms worth reading.

### 3D CAD (parametric modeling, assemblies, drawings)

| Tool | License | Notes |
|---|---|---|
| [FreeCAD](https://www.freecad.org/) | Open source | Full parametric modeler: sketcher, Part Design, assemblies, TechDraw drawings, plus FEM and CAM workbenches. Windows, macOS, Linux. |
| [Onshape](https://www.onshape.com/en/education/) | Free education and hobby plans | Runs in a browser, so it works on any computer. Free hobby documents are public. Closest free experience to SolidWorks. |
| [Autodesk Fusion for personal use](https://www.autodesk.com/products/fusion-360/personal) | Free, limited | Non-commercial, personal projects only, with reduced features. CAD, CAM, and basic simulation in one tool. |
| [SolveSpace](https://solvespace.com/) | Open source | Small, fast parametric modeler. Good for quick parts and mechanisms. |

Paid equivalents: SolidWorks, Creo, Siemens NX, CATIA, Inventor.

### Code-based CAD (models written as scripts)

| Tool | License | Notes |
|---|---|---|
| [OpenSCAD](https://openscad.org/) | Open source | Describe a part in a short script. Great for parts driven by dimensions you want to change often. |
| [CadQuery](https://cadquery.readthedocs.io/) | Open source | Python library for parametric CAD. Exports STEP. |
| [build123d](https://build123d.readthedocs.io/) | Open source | Newer Python CAD library on the same kernel as CadQuery. |

### 2D drafting

| Tool | License | Notes |
|---|---|---|
| [LibreCAD](https://librecad.org/) | Open source | 2D drafting in DXF. Good for plates, laser-cut parts, and floor plans. |
| [QCAD Community Edition](https://www.qcad.org/en/) | Open source | 2D drafting with a cleaner interface than most. |

Paid equivalent: AutoCAD.

### Finite element analysis (stress, deflection, vibration, heat)

| Tool | License | Notes |
|---|---|---|
| [FreeCAD FEM workbench](https://www.freecad.org/) | Open source | FEA inside FreeCAD, using the CalculiX solver. The easiest place to start. |
| [CalculiX](https://www.calculix.de/) | Open source | Solver that reads Abaqus-style input files. Static, frequency, buckling, heat. |
| [PrePoMax](https://prepomax.fs.um.si/) | Open source | Windows interface for CalculiX: import STEP, mesh, load, solve, view results. |
| [Code_Aster](https://code-aster.org/) | Open source | Industrial-strength solver from the French utility EDF. Steep learning curve. |
| [Elmer FEM](https://github.com/ElmerCSC/elmerfem) | Open source | Multiphysics: structures, heat, fluids, electromagnetics. |
| [Ansys Student](https://ansys.synopsys.com/academic/students) | Free for students | The real Ansys with model size limits. Windows only, renewable license. |

Paid equivalents: Ansys, Abaqus, SolidWorks Simulation, COMSOL.

### Computational fluid dynamics

| Tool | License | Notes |
|---|---|---|
| [OpenFOAM (Foundation)](https://openfoam.org/) | Open source | The standard open-source CFD toolbox. Linux first; runs on Windows through WSL. |
| [OpenFOAM (ESI)](https://www.openfoam.com/) | Open source | A parallel distribution of OpenFOAM with Windows builds. Pick one of the two and stay with it. |
| [SimScale Community](https://www.simscale.com/product/pricing/) | Free, limited | Browser-based CFD and FEA. Free plan has limited simulations and core hours, and projects are not private. |

Paid equivalents: Ansys Fluent and CFX, Star-CCM+, SolidWorks Flow Simulation.

### Meshing and results viewing

| Tool | License | Notes |
|---|---|---|
| [Gmsh](https://gmsh.info/) | Open source | Mesh generator used by many open solvers. |
| [Salome](https://www.salome-platform.org/) | Open source | Geometry, meshing, and a front end for Code_Aster. |
| [ParaView](https://www.paraview.org/) | Open source | Views and post-processes results from FEA and CFD: contours, slices, streamlines, animations. |

### Numerical computing (the MATLAB job)

| Tool | License | Notes |
|---|---|---|
| Python with [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), and [Matplotlib](https://matplotlib.org/) | Open source | The most capable free option. Arrays, linear algebra, ODE solvers, optimization, signal processing, plots. See [Python](02-python.md). |
| [Jupyter](https://jupyter.org/) | Open source | Notebooks that mix code, results, plots, and notes. Ideal for homework and lab analysis. |
| [GNU Octave](https://octave.org/) | Open source | Runs most MATLAB scripts unchanged. See [GNU Octave and MATLAB](04-matlab.md). |
| [Scilab](https://www.scilab.org/) | Open source | MATLAB-like language plus Xcos, a block-diagram simulator similar to Simulink. |
| [Julia](https://julialang.org/) | Open source | Fast language for heavy numerical work and large simulations. |

Paid equivalents: MATLAB, Mathcad.

### Symbolic math, units, and properties

| Tool | License | Notes |
|---|---|---|
| [SymPy](https://www.sympy.org/) | Open source | Symbolic algebra and calculus in Python: solve, differentiate, integrate, simplify. |
| [Maxima](https://maxima.sourceforge.io/) | Open source | Standalone computer algebra system. |
| [Pint](https://pint.readthedocs.io/) | Open source | Python units library. Carries units through every calculation and catches unit errors. |
| [CoolProp](http://www.coolprop.org/) | Open source | Thermodynamic properties of water, steam, air, refrigerants, and more. Replaces steam tables in code. |
| [Qalculate!](https://qalculate.github.io/) | Open source | Desktop calculator that understands units and conversions. |
| [Desmos](https://www.desmos.com/calculator) and [GeoGebra](https://www.geogebra.org/) | Free | Browser graphing calculators. Fast for checking a function or a root. |

Paid equivalents: Maple, Mathematica, EES (Engineering Equation Solver).

### System modeling and controls

| Tool | License | Notes |
|---|---|---|
| [python-control](https://python-control.readthedocs.io/) | Open source | Transfer functions, step and frequency response, root locus, state space. |
| [OpenModelica](https://openmodelica.org/) | Open source | Models mechanical, electrical, thermal, and hydraulic systems together, from component libraries. |
| Scilab Xcos | Open source | Block-diagram simulation, included with [Scilab](https://www.scilab.org/). |

Paid equivalents: Simulink, Dymola.

### Circuits, electronics, and embedded systems

| Tool | License | Notes |
|---|---|---|
| [KiCad](https://www.kicad.org/) | Open source | Schematic capture and PCB layout, used professionally. |
| [LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html) | Free, from Analog Devices | Fast, widely used SPICE circuit simulator. |
| [ngspice](https://ngspice.sourceforge.io/) | Open source | SPICE simulator, also built into KiCad. |
| [Falstad circuit simulator](https://www.falstad.com/circuit/) | Free, in browser | Animated circuit simulation. Great for building intuition. |
| [Arduino IDE](https://www.arduino.cc/en/software) | Open source | The easiest way to program microcontrollers. |
| [PlatformIO](https://platformio.org/) | Open source | Professional embedded development inside VS Code, for many boards. |
| [MicroPython](https://micropython.org/) | Open source | Python on microcontrollers. |

Paid equivalents: Altium, OrCAD, Multisim.

### Fabrication (3D printing, CNC, laser)

| Tool | License | Notes |
|---|---|---|
| [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) | Open source | Turns STL or 3MF models into printer G-code. Works with many printers, not only Prusa. |
| [Cura](https://github.com/Ultimaker/Cura) | Open source | Popular slicer with profiles for many printers. |
| [OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) | Open source | Slicer with strong calibration tools. |
| FreeCAD CAM workbench | Open source | Generates CNC toolpaths from FreeCAD models. Part of [FreeCAD](https://www.freecad.org/). |
| [Inkscape](https://inkscape.org/) | Open source | Vector drawing. Common for laser cutting and vinyl cutting files. |

Paid equivalents: Mastercam, Fusion CAM (full), SolidCAM.

### Rendering and visualization

| Tool | License | Notes |
|---|---|---|
| [Blender](https://www.blender.org/) | Open source | Photoreal renders and animations of your CAD models for reports, portfolios, and presentations. |

Paid equivalents: KeyShot, SolidWorks Visualize.

### Writing, diagrams, references, and version control

| Tool | License | Notes |
|---|---|---|
| [LibreOffice](https://www.libreoffice.org/) | Open source | Word processor, spreadsheet, and slides. Opens Microsoft Office files. |
| [TeX Live](https://www.tug.org/texlive/) | Open source | LaTeX, the standard for equation-heavy reports and papers. |
| [Overleaf](https://www.overleaf.com/) | Free plan | LaTeX in the browser, with templates and collaboration. |
| [draw.io](https://www.drawio.com/) | Open source | Flowcharts, block diagrams, P&IDs, wiring diagrams. |
| [Zotero](https://www.zotero.org/) | Open source | Collects sources and formats citations in reports. |
| [Git](https://git-scm.com/) | Open source | Version control for code, notes, and even CAD scripts. This repo uses it. |

Paid equivalents: Microsoft Office, Visio, EndNote.

### More free tools worth having

These come from a working mechanical engineering setup (as of 2026) and fill gaps the tables above do not.

| Tool | License | Use |
|---|---|---|
| [pandas](https://pandas.pydata.org/) | Open source | Tables of test data in Python: load CSV, clean, group, and summarize. |
| [OpenCV](https://opencv.org/) | Open source | Computer vision in Python: measuring parts from photos, tracking motion in test video. |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | Open source | Read, search, and extract text and tables from PDF datasheets and standards. |
| [pywin32](https://github.com/mhammond/pywin32) | Open source | Drive Windows programs from Python, including automating SolidWorks through its COM API. |
| [FFmpeg](https://ffmpeg.org/) | Open source | Converts and trims video. Pull frames from high-speed test footage, or make an animation from simulation frames. |
| [Unreal Engine](https://www.unrealengine.com/) | Free to use, royalties above a revenue threshold | Real-time 3D for interactive visualization, simulators, and digital twins. Read the license for commercial work. |
| [HP calculator software](https://hpcalcs.com/download/) | Free | Connectivity Kit and emulator for HP Prime calculators, from HP's official calculator licensee. See [Calculators](05-calculators.md). |
| [GitHub CLI](https://cli.github.com/) | Open source | Work with GitHub repositories, issues, and pull requests from the terminal. |

Licensed tools in the same setup, for reference: SolidWorks (CAD and simulation), MATLAB (numerical computing), and Microsoft 365 (documents). Each has a free equivalent in the tables above. Many universities give students these licenses free, so check before you pay.

## Checklist: a core install

If you install nothing else, install these. Together they cover almost every lesson in this repo.

- [ ] FreeCAD or Onshape, for CAD and drawings
- [ ] Python with NumPy, SciPy, Matplotlib, SymPy, Pint, and CoolProp, in Jupyter
- [ ] GNU Octave, if a course or job expects MATLAB
- [ ] PrePoMax with CalculiX, or the FreeCAD FEM workbench, for first FEA runs
- [ ] KiCad and LTspice, for circuits
- [ ] Arduino IDE, for mechatronics projects
- [ ] PrusaSlicer, if you have access to a 3D printer
- [ ] LibreOffice and draw.io, for reports
- [ ] Git, to keep your work safe and versioned

On Python, one command installs the libraries above:

```
pip install numpy scipy matplotlib sympy pint coolprop jupyter
```

## Example: one bracket through the whole free toolchain

1. **Design:** model an L-bracket in FreeCAD, fully constrained, and make a TechDraw drawing with dimensions and tolerances. Export STEP and PDF.
2. **Hand calculation:** in a Jupyter notebook, treat one leg as a cantilever and compute the bending stress at the root with Pint keeping the units honest.
3. **Simulate:** open the STEP in PrePoMax, mesh it, fix the mounting holes, apply the load, and solve with CalculiX. Compare the peak stress near the root with your hand calculation. If they disagree by more than about 20 percent, find out why before trusting either.
4. **Make it:** slice the STEP or an STL export in PrusaSlicer and print it, or cut it from plate.
5. **Report:** write it up in LibreOffice or Overleaf, with a draw.io load diagram and a Blender render. Commit the files to Git.

Every step uses a free tool, and every step is the same workflow an engineer follows with paid software.

## Practice

1. Install FreeCAD or open Onshape. Model a 60 mm cube with a 20 mm through hole and export it as STEP.
2. In Python, use CoolProp to look up the density of liquid water at 25 degrees C and 1 atm.
3. In LTspice or Falstad, build a 10 V source with a 1 kilohm and a 2 kilohm resistor in series. Read the voltage across the 2 kilohm resistor.
4. Pick one paid tool from a job posting that interests you. Find its free equivalent in this lesson and complete that tool's first official tutorial.

<details><summary>Answers</summary>

1. The STEP file should reopen in a second tool (for example, FreeCAD if you used Onshape) with the hole intact.
2. About 997 $\text{kg/m}^3$, from `CoolProp.CoolProp.PropsSI('D', 'T', 298.15, 'P', 101325, 'Water')`.
3. About 6.67 V, since $10\ \text{V} \times 2/(1 + 2) = 6.67\ \text{V}$.
4. Open-ended. You are done when you can redo the tutorial without the instructions.

</details>

## Common mistakes

- Putting private or client work on a free plan whose files are public.
- Using a personal-use or student license for paid work. That breaks the license terms.
- Trusting an FEA or CFD color plot without a hand calculation to check it against. Free and paid solvers both return confident wrong answers when the boundary conditions are wrong.
- Saving only in a native format. Export STEP, DXF, CSV, and PDF copies.
- Tool hopping. Finish projects in one tool before trying the next.

## Go deeper

- [FreeCAD](https://www.freecad.org/) by the FreeCAD project: downloads, documentation, and getting-started tutorials.
- [PrePoMax](https://prepomax.fs.um.si/) by the University of Maribor: free FEA interface with tutorials and example models.
- [SciPy](https://scipy.org/) by the SciPy community: the core library for scientific computing in Python, with user guides.
- [KiCad](https://www.kicad.org/) by the KiCad project: documentation and getting-started guide for schematics and PCBs.
- Related: [Starter kit](01-starter-kit.md), [Python](02-python.md), [GNU Octave and MATLAB](04-matlab.md), [CAD](06-cad-solidworks.md).
- [Tools reference](reference.md): the lookup sheet for this topic.
