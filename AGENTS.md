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

## Sub-agent (spawn_agent)

做事前，先問一句：「這個任務能不能拆成互相獨立、各自可以一氣呵成做完的子任務？」

**核心原則：只有當任務可拆成「獨立、自我完備」的子任務時才用 `spawn_agent`；否則直接自己做完。**

✅ 適合：
- 可並行的獨立任務（讀取或寫入範圍互不重疊）
- 大量資訊蒐集（掃整個 codebase、查多份外部資料）
- 大型任務能乾淨拆開時
- 需要客觀視角 review 自己剛做的變更

❌ 不該用：
- 一兩次 tool call 就能搞定的簡單任務
- 需要對話脈絡才能推進的工作
- 緊密串行的步驟（A 的結果是 B 的輸入）
- 寫入範圍會重疊的修改

⚠️ 代價：
- sub-agent 看不到對話歷史，必須一次把完整 context 寫進訊息
- 只會回傳最終訊息，中間過程不可見、不可中斷糾正
- token 成本約翻倍

一句話判斷法：拆得出「兩個以上互不重疊、各自可一氣呵成」的子任務就值得開 sub-agent；拆不出就自己做。重點是「有沒有」，不是「幾個」。

## Ponytail

Write minimal code. Load and follow the `ponytail` skill.
