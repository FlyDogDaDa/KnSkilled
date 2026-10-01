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
  - 若檔案內容混入簡體字請使用 `chinese-conversion-for-files` 技能，預設 `s2twp` 自動將將簡體轉為繁體（臺灣）。
  - 寫中文時善用全形的標點符號（如 `，`、`。`、`、`、`：`、`；`、`「」`、`（）`），勿混用半形。

## Package Management

using Python with `uv` for dependency management. Use `uv add` / `uv run` instead of `pip`.

## Tool Priority

採取行動時，工具優先於 terminal：能用內建工具完成的事，不用 terminal 命令。
terminal 保留給沒有對等工具的操作（執行指令、build、test、git 等）。

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

## Sub-agent (spawn_agent)

拆不拆子任務給 sub-agent？載入並遵循 `sub-agent-delegation` 技能。

## Ponytail

Write minimal code. Load and follow the `ponytail` skill.

## Context Compression

當對話發生壓縮（`lossy compression`）時，腦中可能遺失細節：建議重讀相關技能與文件，把缺的資訊補回來。
