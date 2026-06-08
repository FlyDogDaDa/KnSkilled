---
name: git-commit-writing
description: "Automate git commits: analyze diffs via sub-agents, generate Conventional Commits messages, stage files by intent, and auto-commit (no prompts). Use when user asks to commit, /commit, or 寫 commit."
---

# Git Commit Message Writer

Create atomic, well-structured Git commits following the Conventional Commits specification.

## Role Division

| Role | Responsibility |
|------|----------------|
| **Main Agent** | Run `git status`, batch files into groups, **spawn sub-agents**, coordinate results, execute commit |
| **Sub-Agent** | Read file(s), analyze diff, output structured analysis |

## ⚠️ CRITICAL RULE — Main Agent

**You MUST NEVER read or analyze any file or diff yourself.**

When `git status` reveals changed files, **your only job** is to spawn sub-agents and delegate all analysis. Reading files yourself wastes this architecture's design.

---

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

```
git status --porcelain
```

Identify all modified, renamed, added, and untracked files. If **no changes found**, inform the user and abort.

### Step 2: Batch files into groups

Group files by **intent/theme** (code + config + docs, etc.). Each group becomes **one sub-agent task**.

If only 1 group exists, spawn **1 sub-agent**. If 3 groups, spawn **3 sub-agents in parallel**.

### Step 3: Spawn sub-agents — BLOCKING

Spawn one sub-agent per group. **All spawns in parallel, then block until all return.**

For each sub-agent, provide a **self-contained task** with the sub-agent prompt defined below.

#### Sub-Agent Prompt Template

Copy this exact structure for each sub-agent you spawn:

```
You are a code change analyzer. Your job is to read file(s), analyze what changed, and return a structured result.

## Context
This is part of a git commit workflow. You are analyzing a group of related changes to determine the commit type and message.

## Task
1. Run `git diff <filepath1> <filepath2> ...` to read the diff of the provided files
   - If files are new (untracked), use `cat <filepath>` to read their contents
2. Analyze the changes to determine:
   - **type**: One of feat/fix/docs/style/refactor/perf/test/build/ci/chore/revert
   - **scope**: The affected module/area (e.g., auth, api, utils, or empty)
   - **description**: A concise summary of what changed (imperative mood, present tense, ≤50 chars, no ending punctuation, capitalize first letter)
   - **body**: Optional detailed explanation if the change is complex (wrap at 72 chars)

## Output Format — Return ONLY this JSON, nothing else:

```json
{
  "type": "feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert",
  "scope": "optional-scope",
  "subject": "Brief description of what changed",
  "body": "Detailed explanation (omit if not useful, use null if empty)"
}
```

## Rules
- Be concise in the subject line (≤50 chars)
- Use imperative mood: "add" not "added", "fix" not "fixes"
- Scope is extracted from file paths when obvious (e.g., `src/auth/` → `auth`)
- If no clear scope, omit it (return null or empty string)
- **DO NOT** execute git commands other than `git diff` or `cat` on the provided files
- **DO NOT** run `git add` or `git commit` — you only analyze
```

### Step 4: Collect and synthesize results

Wait for **all sub-agents to return**. Then:

- If **all agree on the same type**, produce **one commit message**.
- If **sub-agents report different types**, you have **mixed intent** — split into **multiple commits**.

### Step 5: Stage and commit

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
