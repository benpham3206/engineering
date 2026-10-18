# Medieval and renaissance engineering

**Type:** lesson

Between about 500 and 1600, engineers in Europe, the Islamic world, and China turned moving water, wind, and springs into steady power. They built mills, clocks, cathedrals, and printing presses. Each of these machines still shows up in modern design: the water wheel as a turbine ancestor, the clock as a timing regulator, the printing press as the first mass production of a document.

**Prerequisites:** [Simple machines](01-simple-machines.md), [Ancient engineering](02-ancient-engineering.md)
**Time:** 2-3 h

## Core ideas

Ancient builders had levers, pulleys, screws, and water channels. Medieval builders added a new source of power: they harnessed flowing water and wind to run machines continuously, without muscles or animals. A water wheel turns for hours on a stream that a person would need a team of workers to match.

The water wheel spread across Europe. The Domesday survey of England in 1086 recorded about 5,600 water mills. Mills ground grain, but they also drove fulling hammers for cloth, forge hammers, bellows, and later saw blades. Windmills followed. The earliest windmills in the Islamic world appear in records from eastern Persia by about the 900s. Windmills reached western Europe around the 1100s and spread through the Low Countries and England.

Mechanical clocks appeared in Europe in the late 1200s and 1300s. Early clocks used a falling weight to drive a gear train, and an escapement that released the gears one tooth at a time. The verge and foliot escapement was an early version. Its errors were often a quarter hour or more per day, far from the seconds per day of later clocks. Most early clocks were built for cathedrals and town squares.

Gothic cathedrals rose in France and England from the 1100s on. Builders used pointed arches, ribbed vaults, and flying buttresses. The buttress carried the outward push of the vault to a pier outside the wall. This let walls hold large windows. Builders learned by trial and error. The choir of Beauvais Cathedral collapsed in 1284 after its vaults were pushed beyond what the piers could carry, and the failure taught later builders to add more support.

The Islamic world kept and extended Greek and Indian mathematics and mechanics. The Banu Musa brothers wrote a book of mechanical devices in Baghdad about 850. Al-Jazari completed *The Book of Knowledge of Ingenious Mechanical Devices* in 1206 at the Artuqid court in Diyarbakir, in what is now southeastern Turkey. It describes water-raising machines, a water clock shaped like an elephant, and crank and connecting-rod mechanisms.

In Song dynasty China, engineers built large mechanical instruments. Su Song and his team completed an astronomical clock tower at Kaifeng in 1088. A water wheel drove an armillary sphere, a star chart that turned once a day, and wooden figures that struck bells and gongs at set hours. The tower used an escapement that released the drive in steps. Bi Sheng developed movable type from baked clay about 1040, and the Song court printed with it. Woodblock printing remained more common in China, and movable type was used on a smaller scale.

In Europe, Johannes Gutenberg combined a screw-press, metal movable type, and oil-based ink in Mainz, around 1440. The press made many identical pages fast. The Gutenberg Bible, printed in the mid-1450s, was an early large product. The press changed engineering documentation too. Drawings and tables could be copied accurately, so knowledge moved faster between workshops.

Brunelleschi built the dome of Florence Cathedral between about 1420 and 1436. He used a double shell, with a herringbone pattern of bricks, and built the dome without a full timber centering across the whole span. The work was a turning point for Renaissance engineers, who began to treat construction as a problem to solve on paper and with models.

Leonardo da Vinci, active from about 1470 to 1519, filled notebooks with drawings of machines, lifting devices, canals, and hydraulic works. Most of his machines were never built, and his notes were not published in his lifetime. His drawings show how a designer thinks about gears, cams, and loads.

## Key inventions

| Year | Invention | Who and where | Why it mattered |
|------|-----------|---------------|-----------------|
| About 850 | Book of mechanical devices | Banu Musa brothers, Baghdad | Collected automatic and hydraulic devices in one written source |
| 1088 | Astronomical clock tower | Su Song and team, Kaifeng, Song China | A water-driven clock with a stepped escapement and a rotating star chart |
| 1206 | Book of Knowledge of Ingenious Mechanical Devices | Al-Jazari, Diyarbakir | Described crank and connecting-rod mechanisms and water-raising machines in detail |
| About 1040 | Movable type from clay | Bi Sheng, China | Showed that movable type could be made and used for printing |
| Late 1200s to 1300s | Mechanical clock with verge escapement | Western Europe | Gave towns a timekeeper driven by a weight instead of water or sun |
| 1420 to 1436 | Double-shell dome | Brunelleschi, Florence | Spanned a large opening without a full timber centering |
| About 1440 | Movable-type printing press | Gutenberg, Mainz | Made many identical copies of a text quickly |

## Key equations

The power of a water wheel depends on the mass of water that falls each second and the height it falls through.

$$P = \rho \, g \, Q \, H \, \eta$$

Here $P$ is the shaft power in watts (W), $\rho$ is the water density in kilograms per cubic metre (kg/m$^3$), with a typical value of $1000\ \text{kg/m}^3$ for fresh water, $g$ is gravitational acceleration in metres per second squared (m/s$^2$), with $g = 9.81\ \text{m/s}^2$ at typical latitudes, $Q$ is the volume flow rate of water in cubic metres per second (m$^3$/s), $H$ is the head, or height the water falls through, in metres (m), and $\eta$ is the wheel efficiency, a number between 0 and 1. Overshot wheels reached efficiencies around 0.7 to 0.8. Undershot wheels, which the water pushed from below, were often 0.2 to 0.4 efficient.

The lever and pulley relations from [simple machines](01-simple-machines.md) still apply to the gear trains that connected the wheel to the stone or the hammer.

## Worked example

**Given:** An overshot water wheel sits on a stream that carries $Q = 0.5\ \text{m}^3/\text{s}$. The water falls $H = 3.0\ \text{m}$ onto the buckets. Water density is $\rho = 1000\ \text{kg/m}^3$, and the wheel efficiency is $\eta = 0.70$.

**Find:** (a) the power the water delivers to the wheel, and (b) the shaft power the wheel delivers to the millstone.

**Solution:**

1. Power delivered by the water, before losses: $P_{\text{water}} = \rho g Q H = 1000 \times 9.81 \times 0.5 \times 3.0 = 14\,715\ \text{W}$, which is about $14.7\ \text{kW}$.
2. Shaft power: $P_{\text{shaft}} = \eta P_{\text{water}} = 0.70 \times 14\,715 = 10\,300\ \text{W}$, which is about $10.3\ \text{kW}$.

**Answer:** The water delivers about 14.7 kW to the wheel, and the wheel delivers about 10.3 kW to the mill.

**Sanity check:** A working horse sustains roughly 0.75 kW (typical value). The wheel's output equals about 14 horses. A medieval mill that ran nonstop on one stream provided the labor of a large team, with no feed and no rest.

## Design trade-offs

A miller balanced wheel size, speed, and efficiency against the flow of the stream. A larger wheel gave more head and a slower, steadier turn, but it cost more timber and needed a deeper mill race. Overshot wheels used the fall of water over the top of the wheel and gave the best efficiency. They needed a steep drop, and the buckets had to stay clear of ice and silt. Undershot wheels worked on flat streams, but they wasted much of the energy in turbulence.

Clock makers balanced accuracy against cost and maintenance. A verge escapement was cheap to build, but it swung with the driving weight and drifted with temperature and friction. Regulating the swing more closely would later need a pendulum or a balance spring, covered in [the scientific revolution](04-scientific-revolution.md).

Cathedral builders balanced height against the risk of collapse. Thin walls with large windows were light, but the vault thrust had to go somewhere. Flying buttresses moved that thrust outward, which left room for glass.

## How it fails

Water wheels failed when the head or flow dropped in a dry season or froze in winter. Mill owners sometimes lost the entire year's income. Wooden axles and gears wore out, and a broken shaft could throw a wheel off its bearings.

Cathedrals failed when piers were too thin or when vault thrust was not carried away. Beauvais Cathedral's collapse in 1284 is the best-known example. Builders responded by adding buttresses, thicker piers, and iron ties. Modern structural codes still check thrust paths in masonry arches.

Printing presses failed when the screw was misaligned, or when the paper was damp and the ink smeared. A practical press also needed careful casting of type. Movable-type printers in Mainz and later in Venice spent much of their effort on the metal alloy.

## History

Water wheels, windmills, and mechanical clocks each spread from a few workshops into a whole economy during these centuries. The Islamic and Chinese engineers recorded their devices in detailed books and instruments, while European builders relied more on drawings and masons' lodges. Movable type had been developed in China and Korea before the Mainz press. Gutenberg's achievement was a practical system of metal type and a press that suited the Latin alphabet, and it is the reason his name is attached to European printing. The cathedrals of northern France are the best surviving record of how medieval builders solved the problem of thrust.

## Practice

1. A water wheel has $Q = 0.4\ \text{m}^3/\text{s}$, $H = 2.5\ \text{m}$, and $\eta = 0.60$. Find the shaft power in kilowatts. Use $\rho = 1000\ \text{kg/m}^3$ and $g = 9.81\ \text{m/s}^2$.
2. A block and tackle has four supporting ropes and a rope efficiency of 0.80. It lifts a load of 800 N. Find the effort force in newtons.
3. In one sentence, explain why a water wheel is a better source of power for a mill than a horse that must rest and eat.
4. Why did Gothic builders place flying buttresses outside the walls instead of thickening the walls?

<details><summary>Answers</summary>

1. $P = 1000 \times 9.81 \times 0.4 \times 2.5 \times 0.60 = 5886\ \text{W}$, which is about 5.9 kW.
2. Ideal effort is $800 / 4 = 200\ \text{N}$. With efficiency 0.80, the effort is $200 / 0.80 = 250\ \text{N}$.
3. A water wheel runs continuously as long as the stream flows, and it needs no feed or rest. A horse tires and must eat, so it delivers power in shorter bursts.
4. A buttress carries the outward push of a vault to a pier outside the wall. A thicker wall would be heavy and would block the windows.

</details>

## Common mistakes

- **Myth: medieval people believed the Earth was flat.** Educated Europeans knew the Earth was a sphere. Many textbooks and scholars wrote about it from the 1200s on.
- **Myth: the Middle Ages produced no engineering.** Water mills, windmills, mechanical clocks, and Gothic cathedrals were all built in this period, many of them well ahead of anything before them.
- **Mistake: treating Gutenberg as the sole inventor of printing.** Movable type was developed earlier in China and Korea. Gutenberg's contribution was a practical European system.
- **Mistake: assuming a water wheel gives its full flow power.** Real wheels lose energy to turbulence, friction, and leakage. Use an efficiency between about 0.2 and 0.8, depending on the type.
- **Mistake: reading early mechanical clocks as accurate to seconds.** Their errors were often a quarter hour or more per day.

## Go deeper

- [De Re Metallica (Project Gutenberg)](https://www.gutenberg.org/ebooks/38015). Georg Agricola's 1556 mining and metallurgy book, translated into English by Herbert and Lou Henry Hoover. It shows water-powered mining machinery in detail.
- [MIT OpenCourseWare](https://ocw.mit.edu/). Free course notes and lectures from MIT, useful for the physics behind the machines in this lesson.
- [Science History Institute](https://www.sciencehistory.org/). Free collections and articles on the history of chemistry, materials, and engineering.
- [Library of Congress](https://www.loc.gov/). Digitized books and prints that include medieval and early modern technical works.

Related lessons: [Simple machines](01-simple-machines.md), [Ancient engineering](02-ancient-engineering.md), [Scientific revolution](04-scientific-revolution.md), [Medieval and renaissance people](people/02-renaissance-polymaths.md), [Ancient and medieval minds](people/01-ancient-and-medieval-minds.md), [Pumps](../applications/thermal-fluid/09-pumps.md), [Clocks and watches](../applications/everyday/07-clocks-and-watches.md), [Buildings and skyscrapers](../applications/structures/02-buildings-and-skyscrapers.md).
