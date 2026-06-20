---
name: terminal-navigation-guard
description: Prevents terminal tool failures by enforcing correct 'cd' parameter usage (root-only, relative, no sub-directories).
---

# Terminal Navigation Guard

This skill prevents `terminal` tool call failures caused by invalid `cd` parameter inputs.

## Core Rules
- **Root Only**: The `cd` parameter MUST ONLY contain the project root directory name.
- **No Sub-directories**: Never include sub-directories (e.g., `root/folder`) in the `cd` parameter.
- **No Absolute Paths**: Never use absolute paths (e.g., `/home/...` or `C:\...`).
- **No Redundancy**: Do not repeat the root directory name (e.g., `root/root`).

## SOP: Navigating to Sub-directories
When you need to execute a command in a sub-directory:
1. **Set `cd`**: Use the project root directory name.
2. **Set `command`**: Include the sub-directory path within the command string.

**Examples:**
- **Target**: `project_root/sub_dir/file.txt`
- **Correct**: `cd="project_root" command="ls sub_dir/file.txt"`
- **Incorrect**: `cd="project_root/sub_dir" command="ls file.txt"` (❌ Tool will fail)

## Sub-agent Instructions
When spawning a sub-agent that may need to use the `terminal` tool, proactively tell it: "Load and follow the `terminal-navigation-guard` skill before making any terminal calls."
