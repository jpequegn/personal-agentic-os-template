# Project mappings

These mappings demonstrate how real backlog projects and P³-style systems fit the seven-layer scaffold. Status values are mature, partial, missing, or not applicable.

| Project | Mapping | Primary sequencing lesson |
| --- | --- | --- |
| P³ | `docs/mappings/p3.md` | Treat Verification as partial until eval runners, quality gates, fixture checks, and retrospective evidence are linked to each workflow. |
| signal-newsletter | `docs/mappings/signal-newsletter.md` | Validation and feedback tracking belong in Verification before Automations expand. |
| mlx-grammar | `docs/mappings/mlx-grammar.md` | Optional backend boundaries and fixture evals are Verification/Connections work, not just implementation detail. |
| project-ideas | `docs/mappings/project-ideas.md` | Source backlog Context should close only after execution-repo Verification and PRs complete. |
| Trade Thesis Journal | `docs/mappings/trade-thesis-journal.md` | Start with Identity and Verification before adding market-data Connections. |
| Health Metrics Forecaster | `docs/mappings/health-metrics-forecaster.md` | Treat privacy and evidence quality as Verification constraints before Automations. |

## Layer checklist

- Identity: purpose, owner, boundaries, non-goals.
- Context: current state, source snapshots, constraints.
- Skills: reusable procedures and commands.
- Memory: durable facts, decisions, retrospectives.
- Connections: tools, repos, files, APIs, humans.
- Verification: tests, evals, reviews, quality gates.
- Automations: cron, webhooks, watchers, scheduled routines.

## How mapping guides issue placement

When a project feels too broad, classify the weak layer first. A missing or partial layer becomes the next issue. Mature layers become acceptance criteria and guardrails. Not applicable layers should be documented explicitly so future contributors do not add unnecessary infrastructure.

Concrete sequencing pattern:

1. Choose the weakest layer that blocks trust or usefulness.
2. Create one implementation issue for that layer.
3. Add verification evidence before promoting the layer to mature.
4. Add automations only after verification and rollback guidance are present.
