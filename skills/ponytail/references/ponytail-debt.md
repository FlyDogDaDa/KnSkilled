# Ponytail Debt

> Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

Harvest every `ponytail:` comment in the codebase into a debt ledger,
so deferrals don't silently rot into "later means never".

## When to use

User says: "ponytail debt", "/ponytail-debt", "what did ponytail defer",
"list the shortcuts", "ponytail ledger", "what did we mark to do later".

## Scan

Grep for comment markers (skip node_modules, .git, build output):
`grep -rnE '(#|//) ?ponytail:' .`

Each hit is one ledger row. The comment prefix keeps prose that merely
mentions the convention out of the ledger.

## Output

One row per marker, grouped by file:
`<file>:<line>: <ceiling>. upgrade: <trigger>.`

Pull the ceiling and trigger straight from the comment convention:
`ponytail: <ceiling>, <upgrade path>`

Flag any `ponytail:` comment that names **no** upgrade path or trigger
with a `no-trigger` tag — those are the ones that silently rot.

End with: `<n> markers, <m> with no trigger.`
or `No ponytail: debt. Clean ledger.`

Reads and reports only. Changes nothing.
To persist, write the ledger to a file (e.g. `PONYTAIL-DEBT.md`).
