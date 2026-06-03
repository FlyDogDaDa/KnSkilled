---
name: agent-collab-daily-log
description: Record daily development activities, decisions, and progress as time-stamped entries in the project's daily log. Use when completing a task, resolving a bug, making a design decision, or when the user asks to log progress.
---

# Daily Log Skill

## Purpose

Create daily log entries for the development project. Each entry is a time-stamped record of work completed, decisions made, and things to follow up on.

## When to Activate

- User asks to record progress or log work
- A significant task is completed
- A design decision is made
- A bug is fixed (with notable details)
- Before ending a session with pending work

## Where to Save Entries

Save entries in the project directory:

```
<project>/chat_wtih_my_agent/
```

Use the naming convention from [naming convention](references/naming-convention.md).

## Entry Workflow

1. Check the existing entries in `chat_wtih_my_agent/` to determine the next `count` for the current day.
2. Create a new entry using the naming convention.
3. Populate the entry with:
   - Front matter (YAML)
   - Title (`#`)
   - Timestamp using your knowledge of the current date
   - **What was done** — specific and factual
   - **Why** — context or rationale for decisions
   - **How** — technical details (files changed, commands run, code patterns)
   - **Follow-up** — pending items or next steps
   - References — links or related entries
4. Use the template from [entry template](assets/entry-template.md).

## Entry Format

Each entry is a Markdown file with:

- **YAML front matter** (between `---`)
- **Sections** using `##` headings
- **References** at the bottom
- **Kebab-case** for topic names (e.g., `fix-database-connection`)

### Code Snippets Policy

**Do NOT embed code in daily log entries.** Use the `References` section to link to source files so readers can view the latest version directly.

Bad:
```markdown
## How
```python
def scan_dataset(root: Path) -> list[Path]:
    return list(root.rglob("**/*.jpg"))
```
```

Good:
```markdown
## How

- `src/utility.py`: `scan_dataset(root, pattern)` → `list[Path]` via `rglob()`
- `src/dataset.py`: `ImageDataset` with `transform` property and `get_batch()` for stacking
- `main.py`: Loads `DATASET_ROOT` from `.env`, tests dataset

## References

- [src/dataset.py](../../src/dataset.py)
- [src/utility.py](../../src/utility.py)
- [main.py](../../main.py)
```

Reason: source files are the source of truth and always up-to-date; logs become stale quickly if code is embedded.

## Entry Template

Use the template at `assets/entry-template.md`.

## Naming Convention

For the full file naming format, see [naming-convention.md](references/naming-convention.md).
