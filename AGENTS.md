## Commit message

Write short, clear Git commit messages. Use imperative mood, max 50 chars for subject line. Omit body unless providing useful context beyond the subject.

## Language

使用繁體中文（臺灣），專有用詞保留原文。

## Package Management

using Python with `uv` for dependency management. Use `uv add` / `uv run` instead of `pip`.

## Terminal Rules

Always use `terminal-navigation-guard` skill for directory navigation. Check for `was not in any of the project's worktrees` errors and validate `cd` parameters per the skill's SOP.

## Ponytail (Full Intensity)

Apply YAGNI: exist? → stdlib? → native? → existing dep? → one line? → minimum code.

Principles: no unrequested abstractions, deletion over addition, mark simplifications with `ponytail:` comments.

Levels: `ponytail lite` / `ponytail full` (default) / `ponytail ultra`. Deactivate with "stop ponytail".
