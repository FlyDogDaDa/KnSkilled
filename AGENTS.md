# AGENTS.md

Follow the instructions below.

## Language

- Use English for:
  - internal thinking and reasoning before replying
  - when searching the web
  - technical terms (e.g., `Attention`)
- Use Traditional Mandarin (Taiwan) for:
  - all replies, explanations, and code comments
  - use Taiwan vocabulary (e.g., `滑鼠` over `鼠標`, `游標` over `光標`, `軟體` over `軟件`)

## Package Management

using Python with `uv` for dependency management. Use `uv add` / `uv run` instead of `pip`.

## Terminal Rules

Terminal is the entry point for command-line access. Always load and follow the `terminal-navigation-guard` skill before making terminal calls.

> **`cd` parameter errors fail silently.** Retrying without loading `terminal-navigation-guard` = infinite loop.

**On any terminal failure:**

❌ Do NOT:
- Try different commands blindly
- Retry without loading `terminal-navigation-guard`
- Assume network or permission issues

✅ Do:
1. Stop
2. Load `terminal-navigation-guard`
3. Check `cd` format
4. Retry with corrected parameters

## Ponytail

Write minimal code. Load and follow the `ponytail` skill.
