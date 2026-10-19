# Software skills for engineers

**Type:** lesson

Most engineers write some software, even if they never call themselves programmers. You repeat the same calculation in a spreadsheet, rename 200 files by hand, or export the same CAD view for each revision. This lesson covers the working skills behind that work: the terminal, version control, reproducible environments, small reliable scripts, testing, debugging, and the basics of web apps. The ideas last longer than any single tool.

**Prerequisites:** [Python for engineering calculations](02-python.md), [Free engineering software](09-free-software.md), [Tools reference](reference.md) (the Git and checklist sections), [Factor of safety and failure](../design/07-factor-of-safety-and-failure.md)
**Time:** 20-30 h to work through the core ideas and practice, then ongoing

## Core ideas

### The terminal and the shell

- The **terminal** is a text window where you type commands. The **shell** is the program that reads those commands. Examples (as of 2026): PowerShell or Command Prompt on Windows, Bash or zsh on macOS and Linux.
- Learn a few commands and their meaning, not their menus. Common ones: `pwd` (print where you are), `ls` or `dir` (list files), `cd` (change folder), `mkdir` (make a folder), `cp`, `mv`, and `rm`.
- A **path** names a file. An absolute path starts at the drive or root (`C:\Projects\bracket\notes.txt`). A relative path starts from where you are now (`..\data\run1.csv`).
- A **pipe** (`|`) sends the output of one command into the next. Each step does one small job. On a Unix-style shell, `grep "FAIL" results.txt | wc -l` counts the failing lines.
- **Scripts beat clicking.** A script is a text file of commands you can rerun. A list of clicks leaves no record and is hard to repeat after a revision changes one number. Write the steps down as code, even if the code is short.

### Text editors and IDEs

- A **text editor** edits plain text. Use one that shows line numbers and can save as UTF-8.
- An **IDE** (integrated development environment) adds a debugger, a file tree, a terminal, and code help. Visual Studio Code is a free example (as of 2026), and it works for Python, Markdown, and many other formats.
- Pick one editor and learn its search, multi-file replace, and run-in-terminal features. Switching editors often costs more time than it saves.

### Version control with Git

- **Version control** records every change to a set of files, who made it, and why. **Git** is the standard free tool (see [Git](https://git-scm.com/) in the [free software list](09-free-software.md)).
- A **commit** is one saved snapshot with a message. Keep one logical change per commit, and write the message as a short imperative sentence with units where they apply, such as `Use 25 kN allowable in bolt check`.
- A **branch** is a separate line of work. Make a branch for a design change or an experiment, so the main line stays working.
- A **merge** combines a finished branch back into another branch. A **pull request** (a review request on a hosting site such as GitHub, as of 2026) asks someone to read the changes before the merge.
- **Commit these.** Scripts, tests, input data (CSV or JSON), exported neutral files that matter (STEP, PDF, a results table), a list of library versions, and a README that says how to run the work.
- **Keep these out.** Generated outputs you can regenerate, virtual environment folders, cache folders such as `__pycache__/`, temporary files, and secrets. Put the patterns in a `.gitignore` file.
- **Large binary CAD files** such as `.SLDPRT` or `.FCStd` cannot be diffed or merged. Git stores each version as a full copy, so the repository grows fast. Options: track them with Git LFS (as of 2026), keep them in a shared file vault with its own revision system, or keep a text source (a script that rebuilds the model) next to the native file. Always keep a neutral export (STEP) for the revision a drawing or test refers to.

### Project environments and dependencies

- A **dependency** is a library your code needs, such as NumPy or Pint in Python.
- A **virtual environment** is a folder that holds one project's libraries, separate from every other project. In Python, make one with `python -m venv .venv` and activate it with the command your shell prints.
- **Pin versions.** A file such as `requirements.txt` that says `numpy==2.5.1` lets you rebuild the same environment later. An unpinned file gives different results after an upgrade.
- Save the environment list with the results it produced. A result you cannot reproduce cannot be checked.

### Writing small, reliable scripts

- A **function** takes named inputs and returns an output. Write one for each formula you repeat, and keep it short enough to test.
- Give each input and output a unit in its name: `preload_N`, `length_mm`, `rate_kg_per_s`. Python will not stop you from mixing millimeters and meters, so the name has to do that job.
- Keep input and output separate. Read data in one function, calculate in another, and print or write results at the end. A calculation that reads files and prints output at the same time is hard to test.
- Use `logging` (a standard library module) or clear `print` lines to show what the script did. A log that says `loaded 3 rows from preloads.csv` helps when a result looks wrong.
- Handle bad input on purpose. A missing column or a text value where a number belongs should stop the script with a clear message, not a wrong answer.

### Testing

- A **test** is a small piece of code that runs your function on an input and checks the output. Automated tests run in seconds and catch breakage after every change.
- The most useful test for engineering code is one with a **hand-calculated value**. Work the answer on paper first, write it into the test, then check the code against it. If the code and the hand value disagree, one of them is wrong, and you learn which by looking.
- A **regression test** records a result you already trust, and fails if a later change moves it. Add one each time you fix a bug, so the bug cannot quietly come back.
- Python's built-in `unittest` module runs tests with no extra install (see the [Python Tutorial](https://docs.python.org/3/tutorial/index.html) for the language basics).

### Debugging

- **Reproduce first.** Write down the exact input that gives the wrong output. A bug you cannot trigger on command is hard to fix.
- **Isolate.** Cut the input down to the smallest case that still fails. Then test each function on that case, one at a time.
- **Look at the values.** A `print` of intermediate values is often enough. A **debugger** pauses the program at a line and lets you read every variable. Python has one built in (`breakpoint()`, which opens `pdb`).
- **Bisect the history.** If a test passed last month and fails now, Git can search the commits for the change that broke it (`git bisect`). The Git documentation and the Pro Git book describe the workflow.
- Change one thing at a time. Two changes at once hide which one fixed the problem.

### Automating engineering tools

- Many engineering programs have a scripting interface. Examples (as of 2026): the SolidWorks API can be driven from Python through COM (Windows' component interface) using the `pywin32` package. **FreeCAD** has a built-in Python console and a macro editor. **Blender** runs Python scripts from its command line.
- The usual jobs are batch exports (every drawing in a folder to PDF), setting parameters and regenerating a model, and pulling mass or volume values into a table.
- Before you automate a tool, do the job once by hand and write down each step. A script that repeats a wrong manual step is still wrong.
- Keep the script, the input list, and a log of what was produced in the same repository.

### Data handling

- **CSV** (comma-separated values) is the most portable table format. Put units in the header row, such as `preload_N`.
- **JSON** stores nested data as text. Put units in key names, such as `"length_mm": 50.0`.
- **SQLite** is a small database in a single file, and Python has it built in (`sqlite3`). Use it when many runs need to be searched or compared.
- **Plots** show the shape of data. Use `matplotlib` (as of 2026) or a spreadsheet. Label every axis with a quantity and its unit.

### Web and full-stack basics

You do not need to build web apps to work with them, but you will use them: a supplier's ordering page, a test-data dashboard, a company tool. Know these terms.

- A **client** is the program that asks for something, usually a browser. A **server** is the program that answers.
- **HTTP** is the request-and-response protocol browsers and servers use. A **request** has a method (`GET` to read, `POST` to send data), a URL, and optional data. A **response** has a status code and a body. `200` means success, `404` means not found, `500` means the server failed.
- An **API** (application programming interface) is a set of URLs a program can call to read or change data. Most APIs send and receive **JSON**. A script that calls an API and saves the JSON is a common engineering tool.
- A **database** holds the stored data. Most web apps keep the data in a database on the server and send only what the page needs.
- **Front end** is the part that runs in the user's browser (layout, buttons, forms). **Back end** is the part on the server (rules, calculations, database access). A full-stack engineer works on both.

### Continuous integration (one paragraph)

**Continuous integration** (CI) runs your tests automatically on a server each time you push a commit or open a pull request. The idea is that a broken change shows up within minutes, not weeks later. Hosting sites such as GitHub include CI services (as of 2026). For a small engineering repository, a CI job that installs the pinned environment and runs the tests is enough.

### Security basics

- **Never commit secrets.** Secrets are passwords, API keys, tokens, and license files. Once a secret is in Git history it is exposed, even after you delete it in a later commit. Treat any leaked secret as compromised and replace it.
- Keep secrets in environment variables or a local file listed in `.gitignore`. Commit an example file with placeholder values instead.
- Check `git status` before every commit. Read the list of files that will go in.
- Be careful with data that is not yours to share, such as customer drawings or proprietary test data.

## Key equations

The worked example uses one engineering check. The **margin of safety** $\mathrm{MS}$ (dimensionless) compares an allowable load $A$ (N) with an applied preload $P$ (N):

$$\mathrm{MS} = \frac{A - P}{P}$$

- $P$ is the preload in newtons (N) that the bolt carries after tightening.
- $A$ is the allowable preload in N from the design rule or the bolt specification.
- $\mathrm{MS} \ge 0$ means the preload is within the allowable. $\mathrm{MS} < 0$ means it is over the limit.

The formula is simple on purpose. The lesson is in how the code is organized and tested.

## Worked example

**Given:** A CSV file of three bolt preloads and their allowables (values are illustrative, not from a standard):

```
bolt_id,preload_N,allowable_N
B1,20000,25000
B2,31000,25000
B3,18500,22000
```

**Find:** The margin of safety for each bolt, and whether each one passes.

**Assumptions:** The allowable and the preload are both in newtons. Each row is one bolt. The margin uses $P$ as the denominator.

**Solution (script, saved as `check_preload.py`):**

```python
"""Check bolt preloads against an allowable preload."""
import csv
import sys


def load_preloads(path):
    """Return a list of (bolt_id, preload_N, allowable_N) rows."""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append((row["bolt_id"], float(row["preload_N"]), float(row["allowable_N"])))
    return rows


def margin_of_safety(preload_N, allowable_N):
    """Return (allowable - preload) / preload, dimensionless."""
    return (allowable_N - preload_N) / preload_N


def check(rows):
    """Return a list of (bolt_id, margin, passed) tuples."""
    results = []
    for bolt_id, preload_N, allowable_N in rows:
        margin = margin_of_safety(preload_N, allowable_N)
        results.append((bolt_id, margin, preload_N <= allowable_N))
    return results


def main(path):
    for bolt_id, margin, passed in check(load_preloads(path)):
        status = "PASS" if passed else "FAIL"
        print(f"{bolt_id}  margin = {margin:+.3f}  {status}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "preloads.csv")
```

**Test (saved as `test_check_preload.py`):**

```python
"""Tests for check_preload. Run with: python -m unittest test_check_preload"""
import unittest

from check_preload import check, margin_of_safety


class TestMarginOfSafety(unittest.TestCase):
    def test_hand_calculated_value(self):
        # Hand calc: (25000 - 20000) / 20000 = 0.25
        self.assertAlmostEqual(margin_of_safety(20000.0, 25000.0), 0.25, places=9)

    def test_over_limit_is_negative(self):
        # Hand calc: (25000 - 31000) / 31000 = -0.19355
        self.assertAlmostEqual(margin_of_safety(31000.0, 25000.0), -6000.0 / 31000.0, places=9)


class TestCheck(unittest.TestCase):
    def test_pass_and_fail_flags(self):
        rows = [("B1", 20000.0, 25000.0), ("B2", 31000.0, 25000.0)]
        self.assertEqual(check(rows)[0][2], True)
        self.assertEqual(check(rows)[1][2], False)


if __name__ == "__main__":
    unittest.main()
```

**Run it:**

```
python -m unittest -v test_check_preload
...
Ran 3 tests in 0.001s

OK

python check_preload.py preloads.csv
B1  margin = +0.250  PASS
B2  margin = -0.194  FAIL
B3  margin = +0.189  PASS
```

**Answer:**

- B1: $\mathrm{MS} = (25000 - 20000)/20000 = 0.250$, passes.
- B2: $\mathrm{MS} = (25000 - 31000)/31000 = -0.194$, fails. The preload is 24 percent over the allowable.
- B3: $\mathrm{MS} = (22000 - 18500)/18500 = 0.189$, passes.

**Sanity check:** B1's margin is exactly 0.25 because 20000 is 0.8 of 25000 and the margin is $1/0.8 - 1$. That matches the printed value. B2 is over the allowable, so its margin must be negative, and it is. The three signs agree with the comparison in the code.

What the example shows: the formula lives in one small function, the file reading lives in another, and the test checks the function against values worked by hand. Changing the allowable in the CSV needs no code change. Adding a bolt needs one new row.

## Practice

Each task is a hands-on exercise. Do them in a folder with a Git repository, and keep the script, the CSV, and the test together.

1. Add a fourth bolt with preload 24000 N and allowable 25000 N. Predict the sign and approximate value of its margin before you run the script, then compare.
2. Write a test for a preload exactly equal to the allowable. Work the expected margin by hand first. Decide whether the code should report a pass.
3. Change the script so it reads a unit from the header row (for example `preload_kN`) and converts to newtons. Add a test for the conversion, using a hand-calculated value.
4. Make a virtual environment, install nothing, and run the tests inside it. Write the Python version to a `README.md`. Commit the script, the test, the CSV, and the README, and check `git status` first so no generated files go in.
5. Write a regression test for a bug you introduce on purpose (for example, swap the numerator and denominator). Watch the test fail, then restore the code and watch it pass.

<details><summary>Answers</summary>

Numbers and checks to compare against. A good answer includes the work, not only the number.

1. Margin about $+0.042$ ($1000/24000 = 0.0417$), passes. A good answer predicts the sign before running.
2. Margin 0.000, and the code should report a pass under the `<=` rule. A good answer states the rule it chose and why.
3. For `preload_kN` $= 20.0$, the margin is 0.250 when the allowable is 25.0 kN. A good answer shows the conversion factor (1000) and the hand value.
4. The commit should list the script, test, CSV, and README, and nothing from `.venv` or `__pycache__`. A good answer shows the `git status` output.
5. The test should fail with the swapped formula and pass again after restoring it. A good answer keeps the bad version out of the commit.

</details>

## Common mistakes

- Writing a script that reads files, calculates, and prints in one long block. Split it into functions so each can be tested.
- Trusting output that has no test and no hand value to compare against. A wrong formula gives a clean-looking table.
- Committing generated files, virtual environment folders, or a file with a password in it. Check `git status` before every commit.
- Storing a large CAD file in Git without a plan. Git keeps every copy, and the repository grows without limit.
- Upgrading libraries without pinning the old versions first. A result from last month may no longer reproduce.

## Go deeper

- [Pro Git](https://git-scm.com/book/en/v2) by Scott Chacon and Ben Straub: the free online book on Git, from first commit through branches, merges, and remotes (2nd edition, 2014, still the standard reference).
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) by the Python Software Foundation: the official language guide, with sections on functions, modules, and the standard library.
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) by MIT: free course on the shell, editors, Git, debugging, and automation, with lectures and notes.
- Related: [Python for engineering calculations](02-python.md), [Free engineering software](09-free-software.md), [Tools reference](reference.md) (Git commands and file formats).
