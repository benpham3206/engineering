# Makerspaces and machine shops

**Type:** lesson
**Verify:** strict

A **shared fabrication space** is a place where people make or repair physical parts with common tools and machines. Engineers use these spaces to turn drawings and models into prototypes, test fixtures, and finished parts. Knowing how access, staff support, and machine time work helps a project move safely from an idea to a buildable job.

**Prerequisites:** [Shop safety](../manufacturing/01-shop-safety.md), [Shop tools](08-shop-tools.md), [Digital fabrication machines](15-digital-fabrication-machines.md), and [Fabrication drawings](../communication/07-fabrication-drawings.md)
**Time:** 2-3 h

## Core ideas

### Three kinds of shared space

A **makerspace** is a shared workspace for learning, prototyping, and small builds. It often has accessible equipment for plastics, wood, electronics, and light fabrication. A **machine shop** focuses on cutting and shaping material, often metal, with machines that need more training and careful setup. A **central shop** is a staff-run service that makes parts for several labs, courses, or project teams; its staff choose the process and operate machines that users may not be permitted to run.

The names overlap. One facility may have a makerspace, a student machine shop, and staff-run central services in the same building. Ask who may operate each machine, who accepts work orders, and which rules govern the area. Equipment, hours, booking systems, and charges vary by facility.

An equipped makerspace can provide fused deposition modeling (FDM) and resin printers, a laser cutter, soldering stations, and a grinding room with belt and disk sanders. It may also have a band saw, drill press, miter saw, sand blasting cabinet, and paint booth. An equipped machine shop or central shop can provide computer numerical control (CNC) mills and lathes, manual mills and lathes, a brake, a shear, punches, and a welder. These are examples of capabilities, not a promise that any particular space has them.

### Two ways to get work done

In **self-service work**, a trained user books a machine and makes the part. This can suit a prototype, a simple part, or a job that benefits from hands-on learning. The user still follows the machine's limits and asks a supervisor when a setup or material is unfamiliar.

In **staff-made work**, a user submits a job and trained staff make it. This can suit a CNC part, a difficult setup, a hazardous process, or work for which the user lacks authorization. Staff may change the process or request more information before accepting the job.

An access path often has three steps.

1. Complete the required safety course or machine-specific training. Training teaches the hazards, guards, controls, and operating limits before a person is near a machine.
2. Book the machine or submit a job ticket. A booking avoids conflicts and lets staff plan capacity; a ticket records the requested work and needed information.
3. Get supervisor sign-off when the process, material, project, or facility requires it. Approval checks that the work is authorized and that the design or risk has been reviewed.

Some facilities combine or omit steps. Follow the local procedure and do not treat a booking as permission to operate a machine without training.

### Submitting a job

Send the information a fabricator needs to decide whether the part can be made and how. A typical submission includes:

- Final drawings with dimensions, tolerances, material, finish, and revision. See [Fabrication drawings](../communication/07-fabrication-drawings.md).
- A solid model for each CNC part, matched to the drawing revision. A model helps program the tool path, while the drawing states dimensions and tolerances the shop must inspect.
- Material and quantity, including any supplied stock or required finish.
- The required project or supervisor approval, if the facility asks for one.

Incomplete or conflicting submissions are often returned for correction. Staff cannot safely choose between competing dimensions, guess a material, or know which file is final. A clear revision also prevents an obsolete drawing or model from being used.

### Capacity, time, and cost

Shop capacity is limited by the number of machines, staff, open hours, maintenance, training demand, and the queue of accepted jobs. A machine may be available only during staffed hours. A deadline should include the time waiting for approval, training, a booking, or staff capacity, not only the minutes when a tool is cutting.

The shop may charge for material, consumables, tooling, or staff time. A tool or fixture that wears during a job may add cost. Ask for an estimate before work begins, and do not assume a student space is free or open whenever the room is unlocked.

For a batch, estimate **machine time** as setup time plus the cycle time for each part. Estimate **lead time** by adding the expected queue delay. These are planning estimates: setup changes, tool changes, failed parts, inspection, and schedule changes can add time.

### Etiquette and safety

Read the local rules and clean the space after use. Return tools, remove chips and scraps with the approved method, and report damaged equipment or near misses. Ask before using another person's setup, changing a machine, bringing in an unapproved material, or using a process you have not seen.

> [!WARNING]
> Never work alone on a machine. Do not operate equipment without its required training, guards, and supervision. Stop and ask a qualified person when the setup, material, or safe procedure is unclear. Follow [Shop safety](../manufacturing/01-shop-safety.md) and the facility's rules.

## Key equations

Estimated machine time for a batch is setup time plus the cycle time for each part.

$$
t_m = t_s + n t_c
$$

Estimated lead time adds the expected queue delay.

$$
t_l = t_q + t_m
$$

Here $t_m$ is machine time in minutes, $t_s$ is setup time in minutes, $n$ is the number of parts (dimensionless), $t_c$ is cycle time per part in minutes, $t_l$ is lead time in minutes, and $t_q$ is queue delay in minutes. These estimates assume one setup for the batch and the same cycle time for each part. They do not include later inspection, rework, or schedule changes.

## Worked example

A staff-run shop estimates a queue delay of $180\ \text{min}$, setup time of $25\ \text{min}$, and cycle time of $7\ \text{min}$ per part for a batch of $8$ parts.

**Given:** Queue delay $t_q = 180\ \text{min}$, setup time $t_s = 25\ \text{min}$, cycle time $t_c = 7\ \text{min/part}$, and quantity $n = 8$.

**Find:** Estimated machine time and total lead time.

**Assumptions:** One setup serves the full batch, each part has the same cycle time, and the queue estimate does not change.

**Solution:** Machine time is $25 + 8(7) = 81\ \text{min}$. Adding the estimated queue gives $180 + 81 = 261\ \text{min}$.

**Answer:** The job uses an estimated $81\ \text{min}$ of machine time and has an estimated lead time of $261\ \text{min}$.

**Sanity check:** The machine time exceeds setup time because it includes all eight cycles. The lead time exceeds machine time because it includes the queue.

<details><summary>Verification</summary>

```verify
tq = q(180, "min")
ts = q(25, "min")
tc = q(7, "min")
n = q(8, "1")
tm = ts + n * tc
tl = tq + tm
expect(tm, "81 min")
expect(tl, "261 min")
```

</details>

## Practice

1. One setup takes $12\ \text{min}$. Each part takes $3\ \text{min}$. Estimate machine time for a batch of $5$ parts.
2. A job has a $40\ \text{min}$ setup and a $6\ \text{min}$ cycle per part. Estimate machine time for $12$ parts.
3. A queue is estimated at $150\ \text{min}$. Setup takes $15\ \text{min}$, and each of $10$ parts takes $4\ \text{min}$. Estimate machine time and lead time.
4. You need a one-off part with a difficult CNC setup, and you have not been trained on the machine. Should you book self-service time or submit a staff job? Explain what information the shop needs.

<details><summary>Answers</summary>

1. $12 + 5(3) = 27\ \text{min}$ of machine time.
2. $40 + 12(6) = 112\ \text{min}$ of machine time.
3. Machine time is $15 + 10(4) = 55\ \text{min}$. Lead time is $150 + 55 = 205\ \text{min}$.
4. Submit a staff job. Include the final drawing with tolerances, a solid model that matches the drawing, material, quantity, and any required approval. The shop can review the setup and schedule trained staff.

```verify
ts1 = q(12, "min")
tc1 = q(3, "min")
n1 = q(5, "1")
expect(ts1 + n1 * tc1, "27 min", ans=1)
ts2 = q(40, "min")
tc2 = q(6, "min")
n2 = q(12, "1")
expect(ts2 + n2 * tc2, "112 min", ans=2)
tq3 = q(150, "min")
ts3 = q(15, "min")
tc3 = q(4, "min")
n3 = q(10, "1")
tm3 = ts3 + n3 * tc3
expect(tm3, "55 min", ans=3)
expect(tq3 + tm3, "205 min", ans=3)
skip(ans=4, why="judgment answer")
```

</details>

## Common mistakes

- Assuming every shared space allows unsupervised use of every machine.
- Treating a booking or ticket as a substitute for training or approval.
- Sending a model without a matching final drawing, material, quantity, or revision.
- Planning only for cutting time and ignoring queue delay, setup, or the shop's hours.
- Leaving chips, scraps, or an unsafe setup for the next person.

## Go deeper

- [Shop tools](08-shop-tools.md) explains common shop machines and their operation.
- [Machinist bench tools](11-machinist-bench-tools.md) covers workholding and hand tools used to set up and finish machined parts.
- [Digital fabrication machines](15-digital-fabrication-machines.md) compares printers, cutters, and CNC routers.
- [Shop safety](../manufacturing/01-shop-safety.md) covers hazards, controls, and safe machine practice.
- [Fabrication drawings](../communication/07-fabrication-drawings.md) shows what a shop needs to build from a drawing.
