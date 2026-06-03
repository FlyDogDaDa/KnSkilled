# File Naming Convention

## Format

All log entries must follow this naming format:

```
{count}_{yyyy}_{mm}_{dd}_{Agent/Human}_{topic}.md
```

### Field Definitions

| Field | Description | Example |
|-------|-------------|---------|
| `count` | Sequence number for the day, starting from `00` | `00`, `01`, `02` |
| `yyyy` | Four-digit year | `2026` |
| `mm` | Two-digit month | `06` |
| `dd` | Two-digit day | `02` |
| `Agent/Human` | Who initiated: `agent` or `human` | `agent`, `human` |
| `topic` | Topic name in kebab-case (hyphens, not underscores) | `fix-database-connection`, `add-git-push` |

### Naming Rules

- `topic` must use **kebab-case** (hyphens as separators), NOT underscores
- `count` increments for each entry within the same day, starting from `00` and comes **before** the date
- `Agent` or `Human` indicates whether the entry was created by the user or the agent
- The entire filename must be lowercase

### Examples

```
00_2026_06_02_human_daily-log-setup.md
01_2026_06_02_agent_fix-git-configuration.md
02_2026_06_02_human_uv-project-initialization.md
00_2026_06_03_agent_daily-progress-report.md
```

## Examples

For a ready-to-use entry template with front matter, see [entry template](../assets/entry-template.md).
