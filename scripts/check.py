"""Check the repo: links resolve, every file declares its type, lessons follow the template,
and every folder README lists its lessons and reference sheets.

Run from the repo root:  python scripts/check.py
Exits with status 1 and prints each problem if anything fails. Standard library only.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s]+(?:\([^)]*\)[^)\s]*)?)\)")
LESSON = re.compile(r"^\d\d-[a-z0-9-]+\.md$")
LESSON_SECTIONS = ["## Practice", "## Common mistakes", "## Go deeper"]
TYPES = {"lesson", "reference", "philosophy"}


def folders():
    return sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name != "scripts"
        and (p / "README.md").exists()
    )


def check_links(path, text, problems):
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        resolved = (path.parent / target.split("#")[0]).resolve()
        if not resolved.exists():
            problems.append(f"{path.relative_to(ROOT)}: broken link {target}")


def check_type(path, text, problems):
    match = re.search(r"^\*\*Type:\*\* (\w+)", text, re.M)
    if not match or match.group(1) not in TYPES:
        problems.append(f"{path.relative_to(ROOT)}: missing or unknown **Type:** line")
    return match.group(1) if match else None


def main():
    problems = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        check_links(md, text, problems)
        if "—" in text:
            problems.append(f"{md.relative_to(ROOT)}: contains an em dash")

    for folder in folders():
        readme = (folder / "README.md").read_text(encoding="utf-8")
        for md in sorted(folder.glob("*.md")):
            if md.name == "README.md":
                continue
            text = md.read_text(encoding="utf-8")
            kind = check_type(md, text, problems)
            if LESSON.match(md.name) and kind in ("lesson", "philosophy"):
                for section in LESSON_SECTIONS:
                    if section not in text:
                        problems.append(f"{md.relative_to(ROOT)}: missing {section}")
                if "<details>" not in text:
                    problems.append(f"{md.relative_to(ROOT)}: practice has no answers block")
            if f"({md.name})" not in readme:
                problems.append(f"{folder.name}/README.md: does not link {md.name}")

    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
