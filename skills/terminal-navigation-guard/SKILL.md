---
name: terminal-navigation-guard
description: >-
  Mandatory pre-flight check and error recovery procedure for ALL terminal operations.
  This skill MUST be loaded before every `terminal` tool call. This is not optional.
  
  When to load: (a) About to call the `terminal` tool — load BEFORE executing;
  (b) Terminal tool call failed — load IMMEDIATELY before retrying;
  (c) Spawning a sub-agent that may call `terminal` — instruct it to load this skill first;
  (d) You just saw a terminal failure or `was not in any of the project's worktrees` error — this is the fix.
  
  Terminal failures with invalid `cd` parameters fail silently. Blind retries waste tokens and create infinite failure loops. Loading this skill is the ONLY way to break the loop.
  
  Proactive rule: Always tell sub-agents: "Load and follow `terminal-navigation-guard` before making terminal calls."
---

# Terminal Navigation Guard

> 「`cd` 參數錯誤會**靜默失敗**。不載入此技能就重試 = 無限迴圈。」

## 核心機制

這是一個 **兩階段防護**：

| 階段 | 時機 | 動作 |
|------|------|------|
| **階段 1：執行前** | 準備呼叫 `terminal` | 檢查 `cd` + `command` 格式（見下方檢查清單） |
| **階段 2：失敗後** | `terminal` 呼叫失敗 | 載入本技能 → 修正參數 → 重試 |

**不管哪個階段，都要先載入此技能。**

## 絕對規則（`cd` 參數）

| 規則 | ✅ 正確 | ❌ 錯誤 | 原因 |
|------|---------|---------|------|
| **只能放根目錄** | `cd="KnSkilled"` | `cd="KnSkilled/skills"` | 系統不接受子目錄 |
| **不能放絕對路徑** | `cd="KnSkilled"` | `cd="C:\KnSkilled"` | 被系統拒絕 |
| **不能冗餘** | `cd="KnSkilled"` | `cd="KnSkilled/KnSkilled"` | 根目錄重複 |

**口訣：** `cd` 只放**專案根目錄名稱**。其餘一切放進 `command`。

## 子目錄操作模式

```
cd="<根目錄>" command="<子路徑>/<指令>"
```

| 目標 | ✅ 正確 | ❌ 錯誤 |
|------|---------|---------|
| 讀 `skills/ponytail/SKILL.md` | `cd="KnSkilled" command="cat skills/ponytail/SKILL.md"` | `cd="KnSkilled/skills/ponytail" command="cat SKILL.md"` |
| 列 `chat/` 目錄 | `cd="KnSkilled" command="ls chat/"` | `cd="KnSkilled/chat" command="ls ."` |
| 執行 `uv run script.py` | `cd="KnSkilled" command="uv run script.py"` | `cd="KnSkilled/scripts" command="uv run script.py"` |

## 執行前檢查清單

在呼叫 `terminal` 之前，**每一項**都必須是 YES：

```
[ ] cd 參數 = 只有根目錄名稱（不含子目錄）
[ ] command 參數 = 包含完整子路徑（如有）
[ ] cd 參數 = 沒有絕對路徑
[ ] cd 參數 = 沒有路徑冗餘
```

有任何 NO → 修正後再呼叫。

## 失敗處理（終止無限迴圈）

```
❌ 不要做的事：
   • 盲試不同的 command
   • 不載入本技能就直接重試
   • 假設是網路或權限問題

✅ 要做的事：
   1. 看到 terminal 失敗 → 停止
   2. 載入 terminal-navigation-guard
   3. 對照上方規則檢查 cd/command
   4. 修正後重試
```

**記住：不載入本技能就重試 = 延長失敗迴圈。**

## 子-agent 協調

派發 sub-agent 且其「可能」使用 terminal 時，任務說明中**必須包含**：

> "Load and follow `terminal-navigation-guard` before making terminal calls."

適用時機：
- [ ] 派發 sub-agent
- [ ] 規劃多步驟含目錄操作的工作流
- [ ] 為其他 agent 編寫包含路徑的操作說明
- [ ] terminal 失敗後的重試前

## 常見錯誤碼對照

| 錯誤訊息片段 | 根因 | 解法 |
|-------------|------|------|
| `was not in any of the project's worktrees` | `cd` 包含子目錄 | 改為根目錄名稱 |
| 無輸出/靜默失敗 | `cd` 格式錯誤 | 檢查是否為絕對路徑或冗餘 |
| 重複失敗 | 未載入本技能就直接重試 | 載入技能 → 修正參數 |