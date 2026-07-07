---
name: terminal-navigation-guard
description: >-
  Act as a terminal navigation guardian. Prevents costly tool call failures caused by invalid cd parameters
  before they happen. Every terminal error wastes time and breaks flow.
  
  Your job: Ensure the cd parameter ONLY contains the project root directory name.
  No subdirectories, no absolute paths, no redundancy.
  
  Use whenever: (1) Spawning sub-agents that may use terminal, (2) Planning any terminal command execution,
  (3) Writing instructions that involve directory navigation.
  
  Proactive rule: Tell sub-agents to 'Load and follow terminal-navigation-guard before making terminal calls.'
  This prevents failures in delegated work.
---

# Terminal Navigation Guard

> "A single terminal error can undo hours of productive work. Prevention is cheaper than recovery."

This skill is your first line of defense against `terminal` tool call failures. Invalid `cd` parameters cause immediate, silent failures that waste time and break agent flow.

**The problem:** The terminal tool requires a specific format for directory navigation. Getting it wrong doesn't warn you — it just fails.

**The solution:** Proactively validate every `cd` parameter before any terminal command executes.

## Core Rules — Non-Negotiable

Violation consequences: **Immediate tool failure**, wasted tokens, broken agent workflow.

| Rule | Valid Example | Invalid Example | Why It Fails |
|------|---------------|-----------------|---------------|
| **Root Only** | `cd="KnSkilled"` | `cd="KnSkilled/skills"` | Subdirectories not allowed |
| **No Absolute Paths** | `cd="KnSkilled"` | `cd="C:\\KnSkilled"` | Absolute paths rejected |
| **No Redundancy** | `cd="KnSkilled"` | `cd="KnSkilled/KnSkilled"` | Duplicate root detected |

**Memory hook:** `cd` = **C**urrent **D**irectory (root level only). Use `command` for everything else.

## SOP: Navigating to Sub-directories

When a command needs to operate in a sub-directory, split the responsibility:

1. **`cd`** = Project root only (non-negotiable)
2. **`command`** = Full path to target (includes subdirectories)

### Quick Reference Table

| Target File | ✅ Correct | ❌ Wrong |
|-------------|------------|----------|
| `KnSkilled/skills/ponytail/SKILL.md` | `cd="KnSkilled" command="cat skills/ponytail/SKILL.md"` | `cd="KnSkilled/skills/ponytail" command="cat SKILL.md"` |
| `KnSkilled/chat_wlih_my_agent/2024-01-15.md` | `cd="KnSkilled" command="ls chat_wlih_my_agent/2024-01-15.md"` | `cd="KnSkilled/chat_wlih_my_agent" command="ls 2024-01-15.md"` |

### Pattern to Remember

```
cd="<root_project_name>" command="<subdir_path>/<filename>"
```

**Mnemonic:** "Root for cd, full path for command."

## Sub-agent Coordination

When spawning a sub-agent that may need to use the `terminal` tool, **always include this instruction**:

> "Load and follow the `terminal-navigation-guard` skill before making any terminal calls."

This prevents failures in delegated work and ensures consistent behavior across all agent invocations.

### When to Apply

- [ ] Spawning sub-agents with terminal commands
- [ ] Planning multi-step workflows involving directories
- [ ] Writing instructions for other agents about file operations
- [ ] Debugging terminal tool failures

## Error Recovery

If a terminal call fails with an unexpected error:

1. **Check `cd` parameter**: Is it only the project root?
2. **Review `command` path**: Does it include subdirectory navigation?
3. **Re-run with corrected parameters**: Use the patterns above.

**Common mistake pattern:**
```
❌ cd="project/root/subdir" command="ls file.txt"
✅ cd="project" command="ls root/subdir/file.txt"
```
