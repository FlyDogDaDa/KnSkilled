# AGENTS.md

Follow the instructions below.

## Language

- Use English for:
  - internal thinking and reasoning before replying
  - when searching the web
  - technical terms (e.g., `Attention`, `know-how`)
- Use Traditional Mandarin (Taiwan) for:
  - all replies, explanations, and code comments
  - use Taiwan internet culture vocabulary (e.g., `鄉民`、`業配`、`貼文`、`迷因`、`置入`、`炎上`、`帶風向`、`敲碗`、`推文`、`酸民`、`潛水`、`開箱`、`朝聖`)
  - use Taiwan IT/programming vocabulary (e.g., `軟體`、`演算法`、`資料庫`、`巨集`、`硬體`、`程式碼`、`專案`、`物件導向`、`變數`、`函式`、`陣列`、`執行緒`、`儲存`、`網路`、`預設`)
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
