import os
from pathlib import Path


for directory, folders, _ in os.walk("."):
    folders[:] = sorted(name for name in folders if not name.startswith("."))
    folder = Path(directory)
    if folder == Path("."):
        continue
    readme = folder / "README.md"
    try:
        with readme.open("x", encoding="utf-8") as file:
            file.write(f"# {folder.name}\n")
        print(readme)
    except FileExistsError:
        pass
