# Production lines and line balancing

**Type:** lesson
**Verify:** strict

A **production line** is a series of workstations through which each unit moves in turn, with a fixed share of the total work done at each station, and **line balancing** is the job of dividing that work among stations so that no station is overloaded and none sits idle for long. An engineer needs it because the slowest station sets the output of the whole line, so an unbalanced line wastes labor and machines while still missing its output target. This lesson covers takt time, precedence, the largest-candidate rule, balance efficiency, bottlenecks, and work in process.

**Prerequisites:** [Automation and robotics](09-automation-robotics.md) (cells and OEE), [Algebra](../math/01-algebra.md)
**Time:** 5-7 h

## Core ideas

### Time at a station

The work on one product is split into **tasks**, the smallest pieces of work the line plans around, such as "fit bracket" or "tighten four bolts". Each task has a **task time**, the seconds a worker or machine needs to finish it. The tasks given to one station add up to its **station time**.

The **cycle time** of a line is the time between one finished unit and the next at its exit. A paced line cannot have a cycle time shorter than its longest station time, because the units cannot move on until the slowest station is done. The **takt time** is the opposite quantity, set by the customer: the time per unit the line must achieve to meet demand. Its formula and a worked check live in the [manufacturing reference](reference.md#takt-time-and-cycle-time), and this lesson uses it without restating it. The rule of the reference applies here too. A line meets demand only when every station time is at or below takt.

### Precedence

Tasks cannot be done in any order. A hole must be drilled before it is tapped, and a part must be placed before it is welded. A **precedence diagram** draws each task as a node and each ordering constraint as an arrow from a task to its successor. A table of immediate predecessors carries the same information and is easier to compute with.

Any assignment of tasks to stations must respect two rules. No task may sit at an earlier station than any of its predecessors, and no station time may exceed the cycle time the line is designed for.

### Counting stations

If total task time is $\sum t_i$ and the design cycle time is $c$, the line needs at least $\sum t_i / c$ stations, rounded up. This bound ignores precedence and the indivisibility of tasks, so a real line can need more. The bound tells a planner when a result is already as good as possible and when more search is worthwhile.

### The largest-candidate rule

Balancing by the **largest-candidate rule** fills stations one at a time. At each point in a station, list the tasks that are not yet assigned, whose predecessors are all assigned, and whose time fits in the station's remaining time. Assign the longest task on that list. When the list is empty, close the station and open the next one.

The rule is a heuristic. It is quick and often good, but it does not promise the fewest stations. Check its result against the lower bound above, and try a different tie-break if the gap is large.

### Efficiency and delay

**Balance efficiency** is the fraction of the paid station time that goes to productive work. **Balance delay** is the rest, the fraction lost to idle time at stations that finish before the cycle time ends. The two add to one.

### Bottlenecks

The **bottleneck** is the station with the longest station time. In a line with no variation and no buffers, it alone sets the cycle time and the output. Speeding up any other station adds nothing. Speeding up the bottleneck helps only until the next longest station takes over, and then the bottleneck moves.

> [!NOTE]
> Real stations vary from unit to unit and stop for faults. A line then produces less than the bottleneck rate predicts, and the shortfall grows with variation and shrinks with buffers between stations. Treat the bottleneck rate as an upper bound, and apply an effective-utilization figure such as OEE (see the [manufacturing reference](reference.md#oee)) to the bottleneck.

### Work in process and Little's law

**Work in process (WIP)** is the number of units that have entered the line and have not yet left it. **Throughput** is the number of finished units leaving per unit time, and **lead time** is how long one unit spends between entry and exit. **Little's law** ties the three together for any stable system, whatever its layout or scheduling: the average WIP equals the average throughput times the average lead time (stated in the [manufacturing reference](reference.md#takt-time-and-cycle-time)). It holds for averages over a long period, with a steady line, and with throughput and lead time measured in matching units.

The law is useful in both directions. Count the units and read the throughput, and it gives the lead time without timing every unit. Cut WIP and, for the same throughput, the lead time falls in proportion. Holding extra WIP does not raise throughput once the bottleneck is busy.

## Key equations

Symbols: $t_i$ is the time of task $i$ (s). $\sum t_i$ is the total task time (s). $c$ is the design cycle time of the line (s), taken as takt time when the line is balanced to demand. $n$ is the number of stations (dimensionless). $T_k$ is the station time of station $k$ (s). $E$ is balance efficiency (dimensionless). $D$ is balance delay (dimensionless). $T_{\max}$ is the longest station time (s).

Minimum number of stations, where $\lceil\cdot\rceil$ rounds up to the next whole number:

$$n_{\min} = \left\lceil \frac{\sum t_i}{c} \right\rceil$$

It holds when tasks can be split between stations at will, and it breaks (the real number is higher) when precedence or indivisible tasks leave gaps.

Station time, as the sum over the tasks assigned to station $k$, with $T_k \le c$ required for every station:

$$T_k = \sum_{i \in \text{station } k} t_i$$

Balance efficiency and balance delay:

$$E = \frac{\sum t_i}{n\,c}, \qquad D = 1 - E$$

Both hold when every station is paid for the full cycle time $c$. They break when stations are staffed for different times, and they change if the same line is run at a different $c$.

Bottleneck cycle time and maximum output over a period $P$ (s):

$$c_{\text{line}} = T_{\max}, \qquad \text{output}_{\max} = \frac{P}{T_{\max}}$$

The output equation holds for a paced line with no breakdowns, no starved or blocked stations, and no scrap. It breaks as soon as any of those occurs.

Little's law, with WIP in units, throughput in units per second, and lead time in seconds, rearranged for the quantity usually unknown:

$$\text{lead time} = \frac{\text{WIP}}{\text{throughput}}$$

## Worked example

**Given:** A line makes one product from ten tasks, with times and immediate predecessors in the table. The plant runs one 8 h shift, which is 28800 s of available time, and the customer demand is 720 units per shift. Apply the largest-candidate rule at design cycle time equal to takt.

| Task | Time (s) | Immediate predecessors |
|---|---|---|
| A | 12 | none |
| B | 18 | none |
| C | 9 | A |
| D | 14 | A, B |
| E | 20 | C |
| F | 7 | D |
| G | 16 | C, D |
| H | 11 | E |
| I | 8 | F, G |
| J | 15 | H, I |

For part (e), 185 units are found in the plant between line entry and the shipping dock on a typical day, and the plant ships at the demand rate.

**Find:** (a) takt time and the minimum number of stations. (b) The station assignment by the largest-candidate rule. (c) Balance efficiency and delay. (d) The bottleneck, the maximum output, and whether a bottleneck OEE of 0.95 still meets demand. (e) The average lead time by Little's law.

**Assumptions:** a paced line with no buffers, task times that do not vary, tasks that cannot be split between stations, and no scrap. The OEE factor in part (d) is a stated input.

**Solution:**

1. Takt time from the reference formula with 28800 s and 720 units is $40\ \text{s}$. Total task time is $12+18+9+14+20+7+16+11+8+15 = 130\ \text{s}$. The lower bound is $130/40 = 3.25$, so $n_{\min} = 4$.
2. Station 1 (40 s available). Free tasks are A (12) and B (18). Take B, leaving 22. Free and fitting: A. Take A, leaving 10. Free: C (9) and D (14, too long). Take C, leaving 1. Nothing else fits. Station 1 holds B, A, C and has $T_1 = 39\ \text{s}$.
3. Station 2. Free: D (14) and E (20). Take E, leaving 20. Free: D (14) and H (11). Take D, leaving 6. F (7) and the rest do not fit. Station 2 holds E, D and has $T_2 = 34\ \text{s}$.
4. Station 3. Free: F (7), G (16), and H (11). Take G, leaving 24. Take H, leaving 13. Take F, leaving 6. I (8) does not fit. Station 3 holds G, H, F and has $T_3 = 34\ \text{s}$.
5. Station 4. Free: I (8). Take it, then J (15), since H and I are done. Station 4 holds I, J and has $T_4 = 23\ \text{s}$. All ten tasks are placed on $n = 4$ stations, equal to the lower bound, so no layout at this takt can use fewer.
6. Efficiency at $c = 40\ \text{s}$: $E = 130 / (4 \times 40) = 0.8125$ and $D = 0.1875$. The idle time per cycle is $1 + 6 + 6 + 17 = 30\ \text{s}$, which is $30/160 = 0.1875$ of the paid time.
7. Bottleneck: station 1 at $T_{\max} = 39\ \text{s}$. Maximum output over the shift is $28800/39 = 738.5$, so 738 whole units, against 720 demanded. At OEE 0.95 the bottleneck delivers $738.46 \times 0.95 = 701.5$ units, below demand. To meet 720 at that OEE the longest station would need to be at most $28800 \times 0.95 / 720 = 38\ \text{s}$.
8. Little's law: throughput is $720/8\ \text{h} = 90$ units per hour, so lead time is $185/90 = 2.06\ \text{h}$.

**Answer:** (a) Takt is 40 s and at least 4 stations are needed. (b) Station 1: B, A, C (39 s). Station 2: E, D (34 s). Station 3: G, H, F (34 s). Station 4: I, J (23 s). (c) $E = 0.8125$ and $D = 0.1875$. (d) The bottleneck is station 1 at 39 s, giving up to 738 units per shift. At OEE 0.95 it falls to about 701 units and misses demand, so station 1 must come down to 38 s or less. (e) Lead time is about 2.06 h.

**Sanity check:** The three stations at 39, 34, and 34 s are close to takt and the last holds the leftovers, and station 4 holds the leftovers. Idle time 30 s plus work 130 s makes 160 s, equal to $4 \times 40$. Little's law gives one more check. At 39 s per unit, a four-station paced line holds four units, each spending $4 \times 39 = 156\ \text{s}$, and $4 = (1/39) \times 156$. The law returns WIP 4 as it should.

<details><summary>Verification</summary>

```verify
ta = q(12, "s")
tb = q(18, "s")
tc = q(9, "s")
td = q(14, "s")
te = q(20, "s")
tf = q(7, "s")
tg = q(16, "s")
th = q(11, "s")
ti = q(8, "s")
tj = q(15, "s")
avail = q(8, "h")
demand = q(720, "1")
expect(avail, "28800 s")
takt = avail / demand
expect(takt, "40 s")
total = ta + tb + tc + td + te + tf + tg + th + ti + tj
expect(total, "130 s")
expect(total / takt, "3.25")
T1 = tb + ta + tc
T2 = te + td
T3 = tg + th + tf
T4 = ti + tj
expect(T1, "39 s")
expect(T2, "34 s")
expect(T3, "34 s")
expect(T4, "23 s")
expect(takt - tb, "22 s")
expect(takt - tb - ta, "10 s")
expect(takt - T1, "1 s")
expect(takt - te, "20 s")
expect(takt - te - td, "6 s")
expect(takt - tg, "24 s")
expect(takt - tg - th, "13 s")
expect(takt - T4, "17 s")
check(T1 + T2 + T3 + T4 == total, "all task time is assigned")
check(T1 < takt and T2 < takt and T3 < takt and T4 < takt, "each station fits in takt")
eff = total / (4 * takt)
expect(eff, "0.8125")
expect(1 - eff, "0.1875")
idle = (takt - T1) + (takt - T2) + (takt - T3) + (takt - T4)
expect(idle, "30 s")
expect(idle / (4 * takt), "0.1875")
expect(total + idle, "160 s")
expect(4 * takt, "160 s")
Tmax = max(max(T1, T2), max(T3, T4))
expect(Tmax, "39 s")
out = avail / Tmax
expect(out, "738.5")
expect(out, "738.46")
expect(out, "738", rel=0.001)
oee = q(0.95, "1")
expect(out * oee, "701.5")
expect(out * oee, "701", rel=0.001)
check(out * oee < demand, "OEE 0.95 misses demand")
expect(avail * oee / demand, "38 s")
rate = demand / avail
expect(rate, "90 1/h")
wip = q(185, "1")
expect(wip / rate, "2.06 h")
expect(4 * Tmax, "156 s")
expect(4 * Tmax / Tmax, "4")
```

</details>

## Practice

1. A plant has 7.5 h of available time per shift and a demand of 450 units per shift. Find takt time in seconds.
2. Station times of 39, 34, 34, and 23 s are run at a line cycle time of 39 s, the longest station time. Find the balance efficiency and balance delay at that cycle time.
3. A plant holds 180 units of WIP and ships 30 units per hour. Find the average lead time.
4. The tasks of the worked example total 130 s. The customer demand rises so that takt falls to 30 s. Find the minimum number of stations by the lower bound, and the balance efficiency if the line is built with exactly that many stations at a cycle time of 30 s.
5. In the worked example, a new fixture cuts task B from 18 s to 12 s and the other tasks stay where they are. Find the new bottleneck station time and the new maximum output per 8 h shift. State whether the answer would change if station 4 were also reduced.

<details><summary>Answers</summary>

1. $60\ \text{s}$.
2. $E = 0.8333$ and $D = 0.1667$.
3. $6.0\ \text{h}$.
4. The bound is $130/30 = 4.33$, so 5 stations. The efficiency is $130/(5 \times 30) = 0.8667$.
5. Station 1 falls to 33 s, so stations 2 and 3 at 34 s become the bottleneck. The maximum output rises from 738 to 847 units per shift. Reducing station 4 changes nothing, because it is not the bottleneck.

```verify
expect(q(7.5, "h") / 450, "60 s", ans=1)
tot = q(130, "s")
c = q(39, "s")
e = tot / (4 * c)
expect(e, "0.8333", ans=2)
expect(1 - e, "0.1667", ans=2)
expect(q(180, "1") / q(30, "1/h"), "6.0 h", ans=3)
expect(tot / q(30, "s"), "4.33", ans=4)
given("5")
expect(tot / (5 * q(30, "s")), "0.8667", ans=4)
s1 = q(12, "s") + q(12, "s") + q(9, "s")
expect(s1, "33 s", ans=5)
expect(q(8, "h") / q(34, "s"), "847", ans=5, rel=0.001)
expect(q(8, "h") / q(39, "s"), "738", ans=5, rel=0.001)
```

</details>

## Common mistakes

- Balancing to the average rather than to the limit. A station time above takt means the line misses demand, even when the line's average time is below takt.
- Treating the lower bound as the answer. The bound ignores precedence, so a line can need more stations than it gives. Compare against it, and do not assume it can be reached.
- Speeding up a station that is not the bottleneck. The line output is unchanged, and the cost buys only idle time.
- Reading Little's law as a recipe for output. It relates three averages. Adding WIP does not raise throughput past the bottleneck rate, and it lengthens lead time in the same proportion.
- Judging a line by its ideal bottleneck rate alone. The ideal figure is an upper bound. Breakdowns, scrap, and variation lower it, and a margin as thin as the 2.6 percent in the worked example is gone with a small loss.

## Go deeper

- [Introduction to Manufacturing Systems (2.854)](https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/), MIT OpenCourseWare. Free course materials on flow lines, variability, and inventory.
- [Introduction to Robotics (2.12)](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/), MIT OpenCourseWare, for the robot stations that often anchor an automated line.
- [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) by Kevin Lynch and Frank Park, for the cell and arm side of automated stations.
- [Manufacturing reference](reference.md) for takt, OEE, and Little's law, and for capability and quality tables.
- [Automation and robotics](09-automation-robotics.md) for OEE and the design of one automated cell.
- [Conveyors and automation](../applications/machines-robots/06-conveyors-and-automation.md) for the transport between stations.
- [Velocity kinematics and Jacobians](../applications/machines-robots/08-velocity-kinematics-and-jacobians.md) for how the arm at a station moves its tool.
