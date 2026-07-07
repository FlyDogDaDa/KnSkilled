# Ponytail Help

> Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

Quick-reference card for all ponytail modes, skills, and commands.

## When to use

User says: "/ponytail-help", "ponytail help", "what ponytail commands",
"how do I use ponytail".

## Levels

| Level | Trigger | Behaviour |
|-------|---------|-----------|
| **Lite** | `ponytail lite` | Build what's asked, name the lazier alternative in one line. |
| **Full** | `ponytail` | The ladder enforced. YAGNI → stdlib → native → one line → minimum. **Default.** |
| **Ultra** | `ponytail ultra` | YAGNI extremist. Deletion before addition. Challenges requirements before building. |

Level sticks until changed or session end.

## Companion skills

| Skill | When to use |
|-------|-------------|
| **ponytail-review** | Review current diff/selection for over-engineering. |
| **ponytail-audit** | Scan whole repo for bloat and over-engineering. |
| **ponytail-debt** | Harvest `ponytail:` comments into a debt ledger. |
| **ponytail-gain** | Show benchmark scoreboard (less code, less cost, more speed). |
| **ponytail-help** | This reference card. |

## Deactivate

Say "stop ponytail" or "normal mode". Resume anytime with `ponytail`.

## Configure default mode

Default = **full**, auto-active every session.

Environment variable (highest priority):
`PONYTAIL_DEFAULT_MODE=ultra`

One-shot display. Edits nothing, changes no mode.
