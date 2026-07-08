## Commit message

Write short, clear Git commit messages. Use imperative mood, max 50 chars for subject line. Omit body unless providing useful context beyond the subject.

## Language

users偏好使用繁體中文（臺灣），技術術語保留原文。優先使用臺灣詞彙，如「終端機」替代「控制面板」。

## Package Management

using Python with `uv` for dependency management. Use `uv add` / `uv run` instead of `pip`.

## Terminal Rules

Terminal（終端機）是 access command-line interface（CLI）的入口。Always use `terminal-navigation-guard` skill for directory navigation. Check for `was not in any of the project's worktrees` errors and validate `cd` parameters per the skill's SOP.

## Filesystem Tools

`create_directory` returns `Created directory <name>` on success. Treat this message as confirmation that the directory was created or already existed.

If unsure, verify with `list_directory` or `ls`.

## Ponytail (Full Intensity)

Apply YAGNI: exist? → stdlib? → native? → existing dep? → one line? → minimum code.

Principles: no unrequested abstractions, deletion over addition, mark simplifications with `ponytail:` comments.

Levels: `ponytail lite` / `ponytail full` (default) / `ponytail ultra`. Deactivate with "stop ponytail".
