# Locks and keys: pin tumbler mechanics and key counting

**Type:** lesson

A lock is a mechanism that keeps a door, box, or machine closed until the right key or code releases it. Locks guard property and people, so their design must hold up against anyone who tries to open them without the key.

A pin tumbler lock stops the plug from turning until every pin stack sits at exactly the right height. The key sets those heights, and the number of possible heights sets how many keys a lock can have. An engineer who understands the counting can judge how much a lock resists guessing, and how much it resists picking, drilling, and bumping.

**Prerequisites:** [Algebra](../../math/01-algebra.md), [Probability and statistics](../../math/07-probability-and-statistics.md), [Tolerancing and stack-up](../../design/04-tolerancing-and-stack-up.md), [Axial and torsion](../../physics/04-axial-and-torsion.md)
**Time:** 3-4 h

## Core ideas

### How it works

A pin tumbler lock has a plug that rotates inside a fixed shell. Along the plug's length sits a row of pin stacks. Each stack has a key pin on the bottom and a driver pin on top, with a spring pushing the driver pin down.

With no key inserted, each stack crosses the boundary between plug and shell. The driver pin blocks the plug from turning. When the correct key is inserted, its cuts lift each key pin so that the boundary between key pin and driver pin lands exactly on the shear line, the gap between plug and shell. Every boundary sits on the shear line at once, so nothing crosses it and the plug turns.

The key cut depth sets each pin height. A deeper cut lifts the key pin less, and a shallower cut lifts it more. Real locks use a small set of cut depths, typically around ten, spaced a few tenths of a millimetre apart.

### Main parts

- **Plug**: the rotating cylinder that the key turns. The cam or tailpiece attached to it drives the bolt.
- **Shell**: the fixed housing that holds the plug and the pin stacks.
- **Pin stacks**: a key pin, a driver pin, and a spring per stack. Typical locks have five or six stacks.
- **Springs**: push each driver pin down. The spring force sets how much pressure a pick feels, and it keeps the stack together when no key is present.
- **Shear line**: the plane between plug and shell. The lock opens when every pin boundary sits on it.

### Variants

- **Pin tumbler (single shear line)**: the common residential type described above.
- **Security pin locks**: add spool-shaped or serrated pins that make a false set. The plug binds at a wrong position, which fools a picker and adds time to a legitimate mistake check.
- **Wafer locks**: flat wafers replace pins. Car ignition and many cabinet locks use them. They have fewer possible positions per wafer, so they have fewer keys.
- **Disc detainer and high-security cylinders**: use rotating discs or sidebars. They add a second constraint that a pin count alone does not capture.

## Key equations

Assumptions for all equations below: each pin stack independently takes one of $k$ depths, every key in the set is equally likely to be tried, and the lock has no security pins.

Number of distinct keys:

$$N = k^{n}$$

where $n$ is the number of pin stacks (dimensionless count) and $k$ is the number of cut depths (dimensionless count).

Expected number of tries to find the right key by trying keys one at a time without repetition:

$$E = \frac{N + 1}{2}$$

where $E$ is the expected number of tries (dimensionless count). This assumes a uniform random search over all $N$ keys.

Number of keys when adjacent cuts may differ by at most $m$ depth steps (a simple model, not any manufacturer's rule):

$$C(n,k,m) = \#\{(d_1,\dots,d_n) \in \{1,\dots,k\}^n : |d_i - d_{i+1}| \le m \text{ for all } i\}$$

The count is a dimensionless integer. It assumes the constraint applies only between neighbouring cuts.

Expected probes to set every pin by single-pin picking, when each pin reveals its state independently:

$$P \approx n\,\frac{k+1}{2}$$

where $P$ is the expected number of probes (dimensionless count). The assumption is that each pin can be tested without disturbing the others, which holds only in the idealized picking model.

## Worked example

**Given:** A 5-pin lock with $k = 10$ cut depths, and a key tester that takes $2\ \text{s}$ per try (assumed).

**Find:** (a) the number of keys $N$, (b) the expected time to find the key by brute force, (c) the number of keys if adjacent cuts may differ by at most 2 depth steps, and (d) the expected single-pin picking probes.

**Solution:**

1. Keys: $N = 10^5 = 100\,000$ keys.
2. Expected tries: $E = (100\,000 + 1)/2 = 50\,000.5$. Time: $50\,000.5 \times 2\ \text{s} = 100\,001\ \text{s}$, which is about $27.8\ \text{h}$.
3. With the adjacency rule $m = 2$, enumerating all sequences gives $C(5,10,2) = 4236$. That is about $4.2\%$ of the unconstrained keys, so the rule removes most of the space.
4. Picking probes: $P = 5 \times 11 / 2 = 27.5$, so about 28 probes under the idealized model.

**Answer:** (a) $100\,000$ keys. (b) About $28\ \text{h}$ of brute-force testing on average. (c) $4236$ keys. (d) About $28$ probes.

**Sanity check:** The brute-force time is about $\tfrac{1}{2} \times 10^5 \times 2\ \text{s}$, which matches $27.8\ \text{h}$. The picking count is far smaller than the key count, which is the reason picking is a practical attack even on a large key space.

## Design trade-offs

- **Key space versus picking**: adding pins multiplies the key count, but per-pin picking grows only linearly with pin count. Pin count alone does not stop picking. Security pins, sidebars, and tighter tolerances do.
- **Manufacturing tolerance**: tight tolerances on pin diameter and shear line make the lock hard to pick, but they raise cost and make wear and dirt cause binding sooner.
- **Key cost and duplication**: a key with complex cuts is harder to copy. A key blank with a restricted keyway limits who can cut duplicates.
- **Durability**: brass and steel pins resist wear. Pins that rub against a worn key wear faster, so keys and cylinders must match.
- **Weather and dirt**: dust and grit cause sticky pins. Lubrication attracts dust, so most cylinders use dry graphite or no lubricant.

## How it fails

- **Picking**: an attacker lifts pins one at a time with a pick and a tension wrench. Single-pin picking exploits small manufacturing differences in pin heights.
- **Bumping**: a bump key with a tap pushes all pins up at once, so they jump through the shear line for an instant. Warning signs are scuff marks on the keyway and an unexplained unlock.
- **Drilling**: an attacker drills out the pins at the shear line. Anti-drill plates and hardened pins resist this.
- **Wear and dirt**: worn pins bind, and the key turns with difficulty. A sticky lock is a warning sign that it needs cleaning or replacing.
- **Key bending**: a thin key bends and jams the lock. A worn key with rounded cuts fails to lift every pin to the shear line.

The safety measures that exist because of these failures are described below.

## Hierarchy of controls for lock security

- **Elimination**: removing the lock entirely is not practical for a door. The control that matters is choosing a door with a lock at all.
- **Substitution**: a deadbolt with a rated grade, a high-security cylinder with security pins, or an electronic lock replaces a weaker lock.
- **Engineering controls**: security pins, hardened pin plates, anti-drill plates, and a strike plate with long screws resist attack. These are built into the cylinder and the door.
- **Administrative controls**: key control, which limits who holds keys and records copies. Rekeying the lock after a lost key is a standard step.
- **Personal protective equipment**: not applicable to lock security. The protection comes from the lock design and from how the lock is installed and managed.

## History

Pin tumbler mechanisms appear in ancient Egypt, where wooden pin locks with wooden keys were used about four thousand years ago. Joseph Bramah patented a lock with a different mechanism in London in 1784, and it was marketed as hard to pick. In 1851 Alfred Charles Hobbs opened a Bramah challenge lock on display at the Great Exhibition in London. Linus Yale Jr. patented a modern pin tumbler design in 1861, and its pin tumbler principle remains in common use.

## Practice

1. A 6-pin lock has 10 cut depths. How many keys does it have?
2. A 4-pin lock has 6 depths, and adjacent cuts may differ by at most 1 step. How many keys are allowed, and what fraction of all $6^4$ keys is that?
3. The lock in question 1 takes 0.5 s per try. What is the expected brute-force time in hours?
4. A 6-pin lock has 10 depths. What is the expected number of single-pin picking probes?

<details><summary>Answers</summary>

1. $10^6 = 1\,000\,000$ keys.
2. 122 keys out of 1296, which is about $9.4\%$.
3. $(1\,000\,000+1)/2 \times 0.5\ \text{s} = 250\,000\ \text{s}$, which is about $69.4\ \text{h}$.
4. $6 \times 11 / 2 = 33$ probes.

</details>

## Common mistakes

- Treating the key count as the security level. Picking, bumping, and drilling attack the pins and the shear line, not the key count.
- Forgetting the adjacency rule when counting keys. Most real key sets are far smaller than $k^n$.
- Assuming a lock is pick-proof because it has many keys. Security pins and sidebars matter more than pin count for resisting picking.
- Using lubricant that attracts dust. Dry graphite or no lubricant keeps pins moving freely.
- Ignoring key wear. A worn key lifts pins incorrectly and can jam a good lock.

## Go deeper

- [Mechanics reference sheet](../../physics/reference-mechanics.md): the friction, spring, and force relations that set pin behaviour.
- [Math reference sheet](../../math/reference.md): counting and expected-value methods used in the key-space calculations.
- [Design reference](../../design/reference.md): tolerance and stack-up tools for pin and shear line sizing.
- Related lessons: [Tolerancing and stack-up](../../design/04-tolerancing-and-stack-up.md), [Zippers and buttons](02-zippers-and-buttons.md).
