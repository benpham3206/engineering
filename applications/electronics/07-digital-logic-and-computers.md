# Digital logic and computers

**Type:** lesson

A computer is billions of transistors, and each one is either on or off. Logic gates, memory cells, and a clock turn those two states into arithmetic, storage, and decisions. An engineer who understands the path from a gate to a running program can read a microcontroller datasheet, find a timing problem, and choose the right memory.

**Prerequisites:** [Circuit basics](01-circuit-basics.md), [Semiconductors](03-semiconductors-diodes-and-transistors.md), [Algebra](../../math/01-algebra.md)
**Time:** 8-12 h

## Core ideas

### How it works

- **Binary.** A digital signal has two levels, 0 and 1. In a circuit, 0 is near 0 V and 1 is near the supply voltage. A gate accepts any voltage close to a rail as a valid level. A voltage between the rails is a fault, and a well-designed system avoids it.
- **Positional notation.** A binary number $b_{n-1} \cdots b_1 b_0$ has the value $\sum_i b_i 2^i$. The pattern 1011 is $8 + 2 + 1 = 11$.
- **Logic gates.** AND, OR, and NOT are the basic functions. NAND and NOR are the AND and OR gates with an inverted output. XOR outputs 1 when its inputs differ. A truth table lists the output for every input combination.
- **Gates from transistors.** A CMOS gate pairs a pull-up network of PMOS transistors with a pull-down network of NMOS transistors. In a NAND gate, two NMOS transistors sit in series, so the output goes low only when both inputs are high. Two PMOS transistors sit in parallel, so the output goes high when either input is low. Only one network conducts at a time, which keeps static power low.
- **Universal gates.** NAND alone builds any logic function. NOT A equals A NAND A. AND equals NOT of a NAND. OR follows from De Morgan's law, $A + B = \overline{\overline{A}\,\overline{B}}$.
- **Combinational logic.** The output depends only on the present inputs. An adder is the classic example. A half adder adds two bits and produces a sum and a carry. A full adder adds three bits: two data bits and a carry in. Chaining full adders gives a multi-bit adder.
- **Sequential logic.** A circuit with memory depends on its past. Two cross-coupled NAND gates form a latch that holds one bit. A D flip-flop adds a clock. On each rising clock edge, it copies its D input to its output and holds that value until the next edge. A clock makes every flip-flop in a design update at the same moment, which keeps the timing predictable.
- **Registers.** A register is a group of flip-flops that stores a word, such as 8, 16, or 32 bits.
- **Memory cells.** An SRAM cell uses six transistors to hold one bit as long as power is applied. A DRAM cell uses one transistor and one capacitor. The capacitor leaks charge, so DRAM rows are refreshed on a regular schedule. Many DRAM parts refresh every row about every 64 ms.
- **The processor.** A CPU repeats a fetch, decode, and execute cycle. The program counter holds the address of the next instruction. The fetch step reads that instruction into the instruction register. The decode step turns the instruction into control signals. The execute step runs the arithmetic logic unit (ALU) or a memory access, and the program counter moves to the next instruction. The clock sets the pace of each step.
- **Microcontroller.** A microcontroller puts a CPU, program memory (flash), working memory (RAM), and peripherals such as timers, ADCs, and PWM outputs on one chip. On reset, the CPU loads the program counter from a fixed address and starts the program. An interrupt pauses the main program, runs a short handler, and returns.

### Main parts

| Part | What it does | Example |
|---|---|---|
| Logic gate | Computes one Boolean function of its inputs | NAND gate in a CMOS chip |
| Flip-flop | Stores one bit on a clock edge | D flip-flop in a counter |
| Register | Stores a word | 32-bit register in an ARM core |
| ALU | Adds, subtracts, and compares words | Adder and logic unit in a CPU |
| Flash | Holds the program without power | Program code in a microcontroller |
| SRAM and DRAM | Hold working data | Small RAM in a microcontroller, DRAM in a PC |
| Clock | Sets the time step for all registers | Crystal oscillator at 16 MHz |

### Variants

- **Microcontroller.** A CPU, memory, and peripherals on one chip run one program for one product. Appliances, cars, and printers use them.
- **Microprocessor.** A CPU alone needs external memory and support chips. Personal computers and servers use microprocessors.
- **FPGA.** A field-programmable gate array is a chip of configurable logic blocks. Engineers describe the circuit in a hardware language, and the chip wires itself to match. FPGAs suit parallel, high-speed work such as video processing.
- **ASIC.** An application-specific integrated circuit is a custom chip. It costs a lot to design, but it costs little per unit at high volume.

## Key equations

Positional value of an $n$-bit binary number:

$$N = \sum_{i=0}^{n-1} b_i \, 2^i$$

where each $b_i$ is 0 or 1, and $N$ is dimensionless.

Two's complement range for $n$ bits:

$$-2^{n-1} \le N \le 2^{n-1} - 1$$

Negating a two's complement value: $-x = \overline{x} + 1$, where $\overline{x}$ is the bitwise NOT of $x$.

Full adder outputs for inputs $A$, $B$, and carry in $C_{in}$:

$$S = A \oplus B \oplus C_{in}, \qquad C_{out} = AB + C_{in}(A \oplus B)$$

CPU execution time for $N_i$ instructions, average cycles per instruction $CPI$ (dimensionless), and clock frequency $f$ in hertz (Hz):

$$t = \frac{N_i \cdot CPI}{f}$$

where $t$ is in seconds (s).

Maximum clock frequency for a path with clock-to-output delay $t_{cq}$, logic delay $t_{logic}$, and setup time $t_{su}$, each in seconds:

$$f_{max} = \frac{1}{t_{cq} + t_{logic} + t_{su}}$$

Dynamic power of a digital circuit with activity factor $\alpha$ (dimensionless), switched capacitance $C$ in farads, supply voltage $V$ in volts, and clock frequency $f$ in hertz:

$$P = \alpha C V^2 f$$

where $P$ is in watts (W).

## Worked example

**Given:** A microcontroller runs at $f = 16$ MHz. A loop body has 500 instructions. Of these, 40 percent are loads that take 2 cycles each, and the rest take 1 cycle each.

**Find:** (a) the cycles per loop, (b) the time per loop, (c) the average cycles per instruction, and (d) the number of loops per second.

**Assumptions:** The loads never wait for memory. No interrupts run during the loop.

**Solution:**

1. (a) Loads are 40 percent of 500, which is 200 instructions. The other 300 take one cycle each. The total is $200 \times 2 + 300 \times 1 = 700$ cycles.
2. (b) $t = 700 / (16 \times 10^6\ \text{Hz}) = 43.75\ \mu\text{s}$.
3. (c) $CPI = 700 / 500 = 1.4$.
4. (d) $16 \times 10^6 / 700 = 22\,857$ loops per second.

**Answer:** (a) 700 cycles. (b) $43.75\ \mu\text{s}$. (c) $CPI = 1.4$. (d) About $2.29 \times 10^4$ loops per second.

**Sanity check:** The average CPI must lie between 1 and 2, because every instruction takes 1 or 2 cycles. The value 1.4 fits. Also, 22,857 loops at 43.75 µs each gives $22\,857 \times 43.75\ \mu\text{s} = 1.00$ s, which confirms the rate.

## Design trade-offs

- **Speed and power.** Dynamic power grows with $V^2 f$. Halving the supply voltage at the same clock cuts dynamic power to one quarter. Doubling the clock doubles it. Battery devices run their processors slowly most of the time and wake them for short bursts.
- **Pipelining.** A pipeline splits the fetch, decode, and execute steps into stages that overlap. Each instruction still takes the same number of stages, so latency stays the same. Throughput rises, because a new instruction enters the pipeline on every clock cycle when nothing stalls it. A branch or a memory wait can stall the pipeline.
- **Memory types.** SRAM is fast and needs six transistors per bit, so it is large and costly per bit. DRAM packs one bit into one transistor and one capacitor, which is dense, but it needs refresh. Flash keeps data without power, but writing it is slow and wears the cell.
- **Microcontroller or FPGA.** A microcontroller runs software and costs a few dollars in volume. An FPGA runs hardware in parallel and handles fast, repeated tasks, but it costs more and needs a hardware design flow.
- **Clock margin.** A faster clock leaves less time for each path to settle. Designers choose a clock below $f_{max}$ with a margin for temperature and voltage changes.

## How it fails

- **Setup and hold violations.** If the data input of a flip-flop changes too close to the clock edge, the flip-flop may capture the wrong value or go metastable. The warning sign is an error that appears only at some temperatures or clock speeds. A design fixes this by meeting the timing constraints. Signals that come from outside the clock domain pass through two flip-flops in series, a synchronizer, before the logic uses them.
- **Glitches.** When two paths through a gate reach it at different times, the output can pulse briefly even though its final value stays the same. Clocked designs wait for the logic to settle before they sample it.
- **Brown-out.** If the supply falls below the minimum voltage, the processor can run wrong instructions or reset at random. A brown-out detector holds the chip in reset until the supply recovers.
- **Software lockup.** A program that stops responding can hang a device. A watchdog timer resets the processor if the software does not reset the timer in time. Appliances and cars use watchdogs for this reason.
- **Memory bit flips.** A cosmic ray or a weak DRAM cell can flip a stored bit. Error-correcting code (ECC) memory detects and corrects single-bit errors, and it detects most double-bit errors. Servers and safety-critical systems use it.
- **Stack overflow.** A microcontroller has little RAM. A deep call chain or a large local array can overwrite other data without any warning, so the program fails in an unrelated place.

## History

George Boole published *The Laws of Thought* in 1854, which set out the algebra of logic that bears his name. In 1937, Claude Shannon showed in his master's thesis at MIT that Boolean algebra could describe relay switching circuits. The ENIAC, completed at the University of Pennsylvania about 1945, used about 17,000 vacuum tubes. Bell Labs demonstrated the point-contact transistor in 1947, and Jack Kilby at Texas Instruments and Robert Noyce at Fairchild Semiconductor developed the integrated circuit in 1958 and 1959. Intel released the 4004 microprocessor in 1971.

## Practice

1. Convert the binary number 10110110 to decimal.
2. Write $-5$ as an 8-bit two's complement number.
3. Show that a NAND gate with both inputs tied together acts as a NOT gate.
4. A CPU at 8 MHz runs a program of 1,000,000 instructions with an average CPI of 1.5. Find the run time.
5. A 16-bit address bus can reach how many byte addresses? A 32-bit bus?

<details><summary>Answers</summary>

1. $128 + 32 + 16 + 4 + 2 = 182$
2. $11111011$. Start from $00000101$, invert to get $11111010$, and add 1.
3. With $A = B$, the NAND output is $\overline{A \cdot A} = \overline{A}$, which is NOT.
4. $t = 1\,000\,000 \times 1.5 / (8 \times 10^6\ \text{Hz}) = 0.1875$ s, or 187.5 ms.
5. $2^{16} = 65\,536$ addresses. $2^{32} = 4\,294\,967\,296$ addresses, which is 4 GiB.

</details>

## Common mistakes

- Reading a binary number as if it were decimal digits. The pattern 1010 is ten, not one thousand ten.
- Assuming every instruction takes one cycle. Loads, branches, and memory waits add cycles, so the CPI is usually above 1.
- Treating a gate delay as the whole story. The longest path through the logic between two flip-flops sets the maximum clock frequency, and the setup and clock-to-output times add to it.
- Confusing flash with RAM. Flash holds the program and keeps it when power is off. RAM holds working data and loses it at power-off.
- Forgetting that the supply voltage has tolerance. A circuit tested at 3.3 V can fail at 3.0 V if the design margin is thin.

## Go deeper

- [Computation Structures (6.004), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) by MIT: binary information, combinational and sequential logic, finite state machines, and processor and memory design.
- [Introductory Digital Systems Laboratory (6.111), MIT OpenCourseWare](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/) by MIT: digital logic, state machines, and building a system on an FPGA.
- Related lessons: [Mechatronics](06-mechatronics.md), [Sensors in products](05-sensors-in-products.md), [Printed circuit boards](04-printed-circuit-boards.md), [Data acquisition and sampling](../../measurement/08-data-acquisition-and-sampling.md), and [Semiconductors and computing](../../history/09-semiconductors-and-computing.md).
- [Applications reference](../reference.md): the lookup sheet for this topic.
