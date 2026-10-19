"""Tests for the inline-math rendering check in verify.py.

The rule mirrors GitHub's renderer, checked against its markdown API: inline
math renders only when the opening $ follows whitespace, the line start, "(" or
"**", and the closing $ is not followed by a letter or digit.

Run from the repo root:  python -m unittest discover -s tests
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import verify  # noqa: E402


class UnrenderedMath(unittest.TestCase):
    def test_renders(self):
        for line in [
            r"Density is $7.87\ \text{g/cm}^3$ for steel.",
            r"($\rho$ in $\text{kg/m}^3$)",
            r"**$x$** and $x$. Then $y$, $z$; and $w$-based ends.",
            r"A code span `kg/m$^3$` is literal, not math.",
            r"Display $$E = mc^2$$ is separate.",
            r"Escaped \$5 stays text and $a$ renders.",
        ]:
            self.assertEqual(verify.unrendered_math(line), [], line)

    def test_raw(self):
        for line in [
            r"Density is 7.87 g/cm$^3$ for steel.",
            r"The $F$s add up.",
            r"An order-$p$ method.",
            r'A note such as "$\pm 0.1$ mm".',
            r"Units of 1/$\text{s}^2$.",
            r"The $S$-$N$ curve.",
        ]:
            self.assertEqual(len(verify.unrendered_math(line)), 1, line)


class CollapsedEscape(unittest.TestCase):
    def test_tab_in_prose_is_a_gate_finding(self):
        import tempfile
        with tempfile.TemporaryDirectory(dir=ROOT / "tests" / "fixtures") as d:
            p = Path(d) / "tab.md"
            p.write_text("# Tab\n\n**Type:** lesson\n\nArea in $\text{m}^2$.\n", encoding="utf-8")
            out = []
            verify.check_doc(verify.Doc(p), {}, verify.Data(out), out, verify.Stats(), {})
            self.assertIn("control", [f.check for f in out])

    def test_bare_command_names(self):
        self.assertEqual(verify.bare_commands(r"A $1\ \text{k}\Omega$ and $\alpha\,\varepsilon$ load."), [])
        self.assertEqual(verify.bare_commands(r"A $\text{alpha test}$ is text."), [])
        self.assertEqual(verify.bare_commands(r"A $1\ kOmega$ resistor."), ["Omega"])
        self.assertEqual(verify.bare_commands(r"$T = arepsilon T_s$ and $x = frac{1}{2}$"), ["epsilon", "frac"])


if __name__ == "__main__":
    unittest.main()
