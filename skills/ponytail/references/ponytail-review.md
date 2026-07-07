# Ponytail Review

> Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

Code review focused exclusively on over-engineering. Finds what to delete:
reinvented standard library, unneeded dependencies, speculative abstractions,
dead flexibility. One line per finding.

## When to use

User says: "review for over-engineering", "what can we delete",
"is this over-engineered", "simplify review", or "/ponytail-review".

## Format

`L<n>: <tag>: <description>.`
Multi-file diffs: `<file>:L<n>: <tag>: <description>.`

## Tags

- `delete:` — dead code, unused flexibility, speculative feature. Nothing replaces it.
- `stdlib:` — hand-rolled thing the standard library ships. Name the function.
- `native:` — dependency or code the platform already does. Name the feature.
- `yagni:` — abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` — same logic, fewer lines. Show the shorter form.

## Examples

- `L12-38: stdlib: 27-line validator class. "@" in email, 1 line, real validation is the confirmation mail.`
- `L4: native: moment.js imported for one format call. Intl.DateTimeFormat, 0 deps.`
- `repo.py:L88: yagni: AbstractRepository with one implementation. Inline it.`
- `L52-71: delete: retry wrapper around an idempotent local call.`
- `L30-44: shrink: manual loop builds dict. dict(zip(keys, values)), 1 line.`

## Scoring

End with `net: -<n> lines possible.` or `Lean already. Ship.`

## Scope

Over-engineering and complexity only. Not for correctness, security, or performance.
Does not apply fixes, only lists them.

"stop ponytail-review" or "normal mode" to revert.
