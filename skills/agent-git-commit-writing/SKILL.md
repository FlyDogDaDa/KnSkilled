---
name: git-commit-writing
description: "Expert git commit message writer. Analyzes git status/diff and reads file contents to write precise messages. Use when user asks to commit, write commit message, or says 寫 commit. Handles features, fixes, refactors, config changes, docs, and agent logs. Spawns SubAgents for untracked files when needed."
---

# Git Commit Message Writer

You are an expert at writing Git commit messages. Write short, clear messages that summarize changes accurately.

## Rules

- **Subject line**: Max 50 characters, lowercase first letter of subject, no ending punctuation, use imperative mood ("add", "fix", "update", "remove", "refactor", etc.)
- **Body**: Only include if it provides useful context the subject line cannot. Wrap at 72 characters. Keep it short.
- **No repetition**: Don't repeat subject line content in the body
- **No meta-commentary**: Only return the commit message. No explanations, no diff output, no "Here's your commit message:"
- **Format**: Separate subject and body with a blank line. No body if not needed.

## Execution

After writing the commit message, **directly execute it** — do not ask for confirmation, do not output the message to the user.

1. Run `git status --short` to see all changes
2. Read `git diff` for modified files to understand what changed
3. **For untracked files**:
   - If they are **code** (`.py`, `.ts`, `.rs`, etc.): read them briefly to confirm purpose
   - If they are **logs/docs/agent conversations** or you need richer context to write an accurate message: spawn a SubAgent to summarize the content. Pass the file path(s) to the SubAgent and ask for a summary in Traditional Chinese plus a concise English commit subject
   - **Parallelize**: If there are multiple untracked or context-needing files, spawn **one SubAgent per file** at the same time — do not wait for one before starting the next.
4. Identify the **primary intent** of the change (feature, fix, refactor, config, docs, cleanup)
5. If multiple files are involved, group them logically — do not list every file in the subject
6. **Stage and commit**:
   - If changes are already staged: run `git commit -m "<message>"`
   - If unstaged: run `git add <files>` then `git commit -m "<message>"`
   - Do NOT ask for confirmation. Do NOT output the message. Just commit.

## Commit Type Guide

Output in conventional commits format:

```
type(scope): subject
```

| Type | When to use | Example output |
|------|-------------|----------------|
| `feat` | New feature or functionality | `feat(auth): add JWT token refresh` |
| `fix` | Bug fix | `fix(loader): handle null response` |
| `docs` | Documentation changes | `docs(readme): update setup instructions` |
| `style` | Formatting, whitespace, semicolons (no code logic change) | `style: fix indentation in trainer` |
| `refactor` | Code reorganization, no behavior change | `refactor(trainer): split into modules` |
| `perf` | Performance improvement | `perf(query): add result caching` |
| `test` | Add or update tests | `test(api): add integration tests` |
| `chore` | Build, tooling, dependencies, housekeeping | `chore(deps): bump pydantic to v2` |
| `ci` | CI/CD configuration | `ci: add pull_request workflow` |
| `revert` | Revert a previous commit | `revert: revert "feat(search)"` |

## When to Split Commits

If `git status` shows clearly distinct categories of changes (e.g., code + config + docs), suggest splitting into multiple commits rather than one catch-all commit.
