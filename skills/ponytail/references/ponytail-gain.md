# Ponytail Gain

> Based on [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) (MIT License).

Display the published benchmark scoreboard: less code, less cost, more speed.

## When to use

User says: "/ponytail-gain", "ponytail gain", "what does ponytail save",
"show ponytail impact", "ponytail scoreboard".

## Scoreboard

Render plain ASCII bars. Bar length shows the measured range;
the label carries the exact figure.

```
ponytail gain benchmark median · 5 tasks · 3 models

Lines of code
  no-skill  ████████████████████  100%
  ponytail  ██▒.................  6-20%  ▼ 80-94%

Cost
  no-skill  ████████████████████  100%
  ponytail  █████▒...............  23-53% ▼ 47-77%

Speed
  ponytail  ▸ 3-6x faster

This repo: /ponytail-debt (shortcuts you deferred)
           /ponytail-audit (what's still cuttable)
```

## Honesty boundary

These are benchmark medians, not per-repo numbers.
NEVER print a per-repo savings number — the unbuilt version was never
written, so there is no real baseline to subtract from.

One-shot display. Edits nothing, changes no mode.
