# 技能大師

當 Agent 要使用某個技能時，確認 deps 並執行。

## 情境

「我要用這個技能。」

## 流程簡述

讀取目標技能的 `SKILL.md`，列出其 `dependencies`；每個 dep 去讀對應的 skill，匯總結果。

此為遞迴 resolve 過程。若某個共同依賴已經讀過，可以直接跳過，不必重複。

## 依賴

None
