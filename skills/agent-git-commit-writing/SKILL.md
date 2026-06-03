---
name: git-commit-writing
description: "Expert git commit message writer. Spawns SubAgents to read and analyze every changed file, then writes precise conventional commit messages. Use when user asks to commit, write commit message, or says 寫 commit."
---

# Git Commit Message Writer

You are an expert at writing Git commit messages. Write short, clear messages that summarize changes accurately.

## Rules

- **Subject line**: Max 50 characters, lowercase first letter, no ending punctuation, use imperative mood (add, fix, update, remove, refactor, etc.)
- **Body**: Only include if it provides useful context the subject line cannot. Wrap at 72 characters. Keep it short.
- **No repetition**: Don't repeat subject line content in the body.
- **No meta-commentary**: Only return the commit message. No explanations, no diff output, no "Here's your commit message:".
- **Format**: Separate subject and body with a blank line. No body if not needed.

## Commit Type Guide

| Type | When to use | Example |
|------|-------------|---------|
| `feat` | New feature or functionality | `feat(auth): add JWT token refresh` |
| `fix` | Bug fix | `fix(loader): handle null response` |
| `docs` | Documentation changes | `docs(readme): update setup instructions` |
| `style` | Formatting, whitespace, semicolons (no code logic change) | `style: fix indentation in trainer` |
| `refactor` | Code reorganization, no behavior change | `refactor(trainer): split into modules` |
| `perf` | Performance improvement | `perf(query): add result caching` |
| `test` | Add or update tests | `test(api): add integration tests` |
| `chore` | Build, tooling, dependencies, housekeeping | `chore(deps): bump pydantic` |
| `ci` | CI/CD configuration | `ci: add pull_request workflow` |
| `revert` | Revert a previous commit | `revert: revert "feat(search)"` |

## Execution — Do Not Skip Steps

After writing the commit message, **directly execute it** — do not ask for confirmation, do not output the message to the user.

### Step 1: Discover changes

```
git status --short
```

Identify all modified, renamed, and untracked files.

### Step 2: Spawn SubAgents — BLOCKING PHASE

Spawn **one SubAgent per file** in **parallel** (fire all spawns without waiting). Each SubAgent receives:

- For **modified/renamed files**: the `git diff` output
- For **untracked files**: the file contents

Ask each SubAgent to return:
1. Traditional Chinese summary of the changes
2. A concise English commit subject (≤50 chars, no ending punctuation, imperative mood)

**Rules for SubAgents:**
- Spawn all SubAgents **at the same time** — do not spawn sequentially.
- Do **NOT** proceed to Step 3 until **all** SubAgents have returned.
- If any SubAgent fails or returns empty, check the result before continuing.

### Step 3: Determine commit strategy

- **Single commit**: If changes share a common intent, write one commit message.
- **Split commits**: If `git status` shows clearly distinct categories (e.g., code + config + docs), recommend splitting into multiple commits.

### Step 4: Stage and commit

```
git add <files>
git commit -m "<message>"
```

- If changes are already staged, skip `git add`.
- **Do NOT ask for confirmation. Do NOT output the message to the user. Just commit.**

## Critical Reminders

- **Every file needs a SubAgent.** Missing even one file means incomplete context.
- **All SubAgents run in parallel**, not sequentially.
- **Blocking checkpoint**: Step 3 (strategy) must not start until Step 2 (SubAgents) is fully complete.
- If `git status` reveals no changes, inform the user and abort.
