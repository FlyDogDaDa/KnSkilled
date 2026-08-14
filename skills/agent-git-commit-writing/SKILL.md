---
name: git-commit-writing
description: "Automate git commits: analyze diffs directly, generate Conventional Commits messages, stage files by intent, and auto-commit (no prompts). Use when user asks to commit, /commit, 寫 commit."
---

# Git Commit Message Writer

Create atomic, well-structured Git commits following the Conventional Commits specification.

## Dependencies

- **terminal-navigation-guard** — MUST be loaded before ANY `git` terminal operation.

> Before running any `git` command, load `terminal-navigation-guard` first.

## Commit Type Guide

| Type | When to use | Example |
|------|-------------|---------|
| `feat` | New feature or functionality | `feat(auth): add JWT token refresh` |
| `fix` | Bug fix | `fix(loader): handle null response` |
| `docs` | Documentation changes only | `docs(readme): update setup instructions` |
| `style` | Formatting, whitespace, semicolons (no logic change) | `style: fix indentation in trainer` |
| `refactor` | Code reorganization, no behavior change | `refactor(trainer): split into modules` |
| `perf` | Performance improvement | `perf(query): add result caching` |
| `test` | Add or update tests | `test(api): add integration tests` |
| `build` | Build system or dependency changes | `build(deps): bump pydantic` |
| `ci` | CI/CD configuration | `ci: add pull_request workflow` |
| `chore` | Maintenance, misc housekeeping | `chore: update lint config` |
| `revert` | Revert a previous commit | `revert: revert "feat(search)"` |

---

## Workflow

### Step 1: Discover changes

Run `git status --porcelain` (after loading `terminal-navigation-guard`).

Identify all modified, renamed, added, and untracked files. If **no changes found**, inform the user and abort.

### Step 2: Batch files into groups

Group files by **intent/theme** (code + config + docs, etc.). Each group becomes **one commit**.

### Step 3: Analyze diffs directly

For each group, read the diff using `git diff <filepath1> <filepath2> ...` (after loading `terminal-navigation-guard`).

For new (untracked) files, use `cat <filepath>` to read their contents.

Analyze the changes to determine:
- **type**: One of feat/fix/docs/style/refactor/perf/test/build/ci/chore/revert
- **scope**: The affected module/area (e.g., auth, api, utils, or empty)
- **subject**: A concise summary (imperative mood, ≤50 chars, no ending punctuation, capitalize first letter)
- **body**: Optional detailed explanation if the change is complex (wrap at 72 chars)

### Step 4: Stage and commit

```
git add <files-for-group>
git commit -m "<type>[scope]: <subject>"
# or multi-line:
git commit -m "<type>[scope]: <subject>\n\n<body>"
```

- If changes are already staged, skip `git add`.
- **Never ask for confirmation. Just commit.**

---

## Commit Message Rules

- **Subject**: Max 50 chars, capitalize first letter, no ending punctuation, imperative mood
- **Body**: Only if it provides useful context. Wrap at 72 chars.
- **No repetition**: Don't repeat subject in body.
- **Reference issues**: `Closes #123`, `Refs #456` when applicable.

---

## Git Merge Strategy

Prefer `--no-ff` merges: keeps the main line history clean and straight while preserving full branch development history.

## Git Safety Protocol

- **NEVER** update git config
- **NEVER** run destructive commands (`--force`, `hard reset`) without explicit request
- **NEVER** skip hooks (`--no-verify`) unless user asks
- **NEVER** force push to `main`/`master`
- If commit fails due to hooks, **fix and create a NEW commit** (don't amend)
- If committing to `main`/`master`, warn first
- **Never stage secrets** (`.env`, `credentials.json`, private keys, etc.)

---

## Execution

After determining the commit message, **directly execute `git commit`** — no confirmation, no preview to user, no meta-commentary.
