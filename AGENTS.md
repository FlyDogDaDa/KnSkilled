## 關於 terminal

`cd` 是 **必填參數**，而且必須填寫 **專案根目錄名稱**（不是完整路徑）。

而不是完整路徑 `/home/A/B/project`（這樣會報錯）。

所以正常運作的 terminal 呼叫長這樣：

```
terminal(command="date", cd="project")
```

## Commit message

You are an expert at writing Git commits. Your job is to write a short clear commit message that summarizes the changes.

If you can accurately express the change in just the subject line, don't include anything in the message body. Only use the body when it is providing *useful* information.

Don't repeat information from the subject line in the message body.

Only return the commit message in your response. Do not include any additional meta-commentary about the task. Do not include the raw diff output in the commit message.

Follow good Git style:

- Separate the subject from the body with a blank line
- Try to limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with any punctuation
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Keep the body short and concise (omit it entirely if not useful)

## Language

使用者偏好使用與閱讀「繁體中文：臺灣」，在臺灣專有名詞通常使用原文


## PackagesManagement

使用者是 AI　專科學士，第一程式語言是 Python ，慣用　UV 管理 dependency。

When managing dependencies, installing packages, or updating the environment, always use `uv` instead of `pip`. For example, use `uv add <package>` to add new dependencies and `uv run <script>` to execute scripts within the managed environment.

