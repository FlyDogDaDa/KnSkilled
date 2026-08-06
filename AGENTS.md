## Commit message

Write short, clear Git commit messages. Use imperative mood, max 50 chars for subject line. Omit body unless providing useful context beyond the subject.

## Language

思考與推理過程使用英文。其餘回覆、說明與註解使用繁體中文（臺灣），技術術語保留原文。優先使用臺灣詞彙，如「終端機」替代「控制面板」。

## Package Management

using Python with `uv` for dependency management. Use `uv add` / `uv run` instead of `pip`.

## Terminal Rules

Terminal（終端機）是 access command-line interface（CLI）的入口。Always load and follow the `terminal-navigation-guard` skill before ANY terminal operation.

### Terminal failure override

Terminal failures follow a different rule than general failures — **do NOT blindly retry**.

1. First terminal failure: STOP. Load `terminal-navigation-guard` IMMEDIATELY and re-execute with corrected parameters.
2. Second terminal failure: STOP again. Verify the skill was applied correctly using the reference table.
3. Third+ failures: You may be facing a different problem (file missing, permission denied). Investigate before retrying.

**Key rule: Never retry a terminal command without loading `terminal-navigation-guard` first. Blind retries waste tokens and create infinite failure loops.**

### Sub-agent coordination

When spawning a sub-agent that may call the terminal, always include: "Load and follow `terminal-navigation-guard` before making terminal calls."

## Filesystem Tools

`create_directory` returns `Created directory <name>` on success. Treat this message as confirmation that the directory was created or already existed.

If unsure, verify with `list_directory` or `ls`.

## Ponytail (Full Intensity)

Apply YAGNI: exist? → stdlib? → native? → existing dep? → one line? → minimum code.

Principles: no unrequested abstractions, deletion over addition, mark simplifications with `ponytail:` comments.

Levels: `ponytail lite` / `ponytail full` (default) / `ponytail ultra`. Deactivate with "stop ponytail".

## Failure Handling

### General rule

First failure: try again.
Two consecutive failures: gather more information and rethink the decision.
Three or more failures: don't panic. Re-examine your current thinking and what you've done so far. You have time to think carefully, but remember — thinking and information are never truly complete.

### Exception: terminal failures

Terminal tool failures are handled by the `Terminal Rules` section above. Do NOT apply the general rule to terminal operations — blind retries create infinite loops.