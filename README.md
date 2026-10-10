# engineering

everything i learned as a mechanical engineering student at SJSU


## Verify README generation

Run `python3 .github/scripts/verify_readmes.py` from the repository root.
The check uses a temporary Git repository and preserves this repository.

On pushes to `main`, GitHub Actions creates missing `README.md` files in
all non-hidden folders, including nested folders. Each new file uses its
folder name as its heading. Existing READMEs are preserved. Bot commits use
the repository's `GITHUB_TOKEN` and `[skip ci]` to prevent workflow loops.
