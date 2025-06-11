# Example of output of `git-smart-commit.py`

```bash
> python git-smart-commit.py
Extracting staged diff...
Generating commit message with GPT-4o-mini...
Suggested commit message:

---
Update Google Drive action to version 1.2.0

- Add support for returning basic file info and saving results as CSV in `get_files_by_query`.
- Improve file path resolution with `_resolve_full_path`.
- Update dependencies to latest versions.
- Add new `BasicFile` model for simplified file representation.
- Update `.gitignore` to exclude chat files.
---

```