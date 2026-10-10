import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


generator = Path(__file__).with_name("generate_readmes.py").resolve()


def run(root):
    subprocess.run([sys.executable, str(generator)], cwd=root, check=True)


def snapshot(root):
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(root).parts
    }


with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    existing = {
        "README.md": b"# Original root\n",
        "math/README.md": b"Topics:\n\nAlgebra\n\nCalculus\n",
        "math/topics/README.md": b"# Handwritten\n\nKeep this text.\n",
        "physics/README.md": b"",
        "math/topics/deep/topic.txt": b"Nested content\n",
        ".github/workflows/config.yml": b"configuration\n",
        "math/.private/nested/config.txt": b"hidden\n",
        "reverse-engineering/café & forces/data.txt": b"unusual name\n",
    }
    for name, content in existing.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    (root / "empty/nested").mkdir(parents=True)
    (root / "linked-content").symlink_to(root / "math", target_is_directory=True)
    (root / "link-readme").mkdir()
    (root / "link-readme/README.md").symlink_to("absent.md")
    run(root)
    for name, content in existing.items():
        assert (root / name).read_bytes() == content, name
    expected = {
        "math/topics/deep": "deep",
        "reverse-engineering": "reverse-engineering",
        "reverse-engineering/café & forces": "café & forces",
        "empty": "empty",
        "empty/nested": "nested",
    }
    for folder, heading in expected.items():
        assert (root / folder / "README.md").read_text() == f"# {heading}\n", folder
    assert not (root / ".github/README.md").exists()
    assert not (root / "math/.private/README.md").exists()
    assert not (root / "math/.private/nested/README.md").exists()
    assert not (root / ".git/README.md").exists()
    assert (root / "link-readme/README.md").is_symlink()
    before = snapshot(root)
    run(root)
    assert snapshot(root) == before, "Second run changed files"
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run([
        "git", "-c", "user.name=Verification", "-c", "user.email=verify@example.invalid",
        "commit", "-qm", "Capture generated READMEs",
    ], cwd=root, check=True)
    run(root)
    assert not subprocess.check_output(["git", "status", "--porcelain"], cwd=root)
    print("PASS: nested and empty folders, exact headings, existing content, hidden folders, symlinks, repeated runs, clean Git tree")
