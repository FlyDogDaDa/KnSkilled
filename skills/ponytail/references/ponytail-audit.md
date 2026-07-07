# Ponytail Audit

> Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

Whole-repo scan for over-engineering. Like ponytail-review, but repo-wide.

## When to use

User says: "audit this codebase", "audit for over-engineering",
"what can I delete from this repo", "find bloat", "/ponytail-audit".

## Hunt targets

- Deps the stdlib or platform already ships
- Single-implementation interfaces
- Factories with one product
- Wrappers that only delegate
- Files exporting one thing
- Dead flags and config
- Hand-rolled stdlib

## Output

One line per finding, ranked biggest cut first:
`<tag>: <description>. [<path>]`

End with `net: -<n> lines, -<n> deps possible.`
or `Lean already. Ship.`

## Tags

Same as ponytail-review: `delete:`, `stdlib:`, `native:`, `yagni:`, `shrink:`.

One-shot. Lists findings, applies nothing.
