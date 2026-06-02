# File Naming Convention

## Format

All log entries must follow this naming format:

```
{yyyy}_{mm}_{dd}_{count}_{Agent/Human}_{topic}.md
```

### Field Definitions

| Field | Description | Example |
|-------|-------------|---------|
| `yyyy` | Four-digit year | `2026` |
| `mm` | Two-digit month | `06` |
| `dd` | Two-digit day | `02` |
| `count` | Sequence number for the day, starting from `00` | `00`, `01`, `02` |
| `Agent/Human` | Who initiated: `agent` or `human` | `agent`, `human` |
| `topic` | Topic name in kebab-case (hyphens, not underscores) | `fix-database-connection`, `add-git-push` |

### Naming Rules

- `topic` must use **kebab-case** (hyphens as separators), NOT underscores
- `count` increments for each entry within the same day, starting from `00`
- `Agent` or `Human` indicates whether the entry was created by the user or the agent
- The entire filename must be lowercase

### Examples

```
2026_06_02_00_human_daily-log-setup.md
2026_06_02_01_agent_fix-git-configuration.md
2026_06_02_02_human_uv-project-initialization.md
2026_06_03_00_agent_daily-progress-report.md
```

## Examples

For a ready-to-use entry template with front matter, see [entry template](../assets/entry-template.md).
