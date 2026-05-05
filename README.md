# Personal Agentic OS Template

Reusable 7-layer scaffold for building personal AI infrastructure projects.

Source idea: https://github.com/jpequegn/project-ideas/issues/33

## Goal

Turn the 7-layer Personal Agentic OS model into an opinionated but reusable project template for systems such as daily briefs, trade journals, health forecasters, research assistants, and personal CRMs.

The seven layers are:

1. Identity — who the system serves and what it optimizes for.
2. Context — current state, recent activity, and relevant facts.
3. Skills — verbs the system can execute.
4. Memory — durable records, indices, and retrieval surfaces.
5. Connections — external sources, APIs, files, and feeds.
6. Verification — tests, evals, quality gates, and audit trails.
7. Automations — cron, launchd, webhooks, watchers, and scheduled routines.

## V1 shape

This repo starts as a template and reference implementation, not a full app platform. V1 should include:

- one folder per layer
- concise README guidance for each layer
- a tiny example app that exercises all seven layers
- checklist and docs for applying the scaffold to future projects
- closeout guidance explaining where the scaffold is useful vs overkill

## Quickstart

```bash
uv run --extra dev python -m pytest -q
uv run --extra dev ruff check .
uv run agentic-os-template --help
uv run agentic-os-template layers
uv run agentic-os-template validate template
uv run agentic-os-template example /tmp/agentic-os-daily-brief
```

## Planning docs

- Source snapshot: `docs/source/project-ideas-33.md`
- Implementation plan: `docs/plans/2026-05-04-personal-agentic-os-template.md`
- Issue checklist: `docs/issue-checklist.md`

- Project mappings: `docs/project-mappings.md`
- Adoption checklist: `docs/adoption-checklist.md`
- Usage guide: `docs/usage.md`
- Security/privacy guide: `docs/security-privacy.md`
- Roadmap: `docs/roadmap.md`
- V1 readiness review: `docs/retrospectives/v1-readiness-review.md`

## Usual protocol

Implementation proceeds issue-by-issue on feature branches with tests/review where applicable, PRs linked with `Closes #N`, squash merges, and main sync between issues.
