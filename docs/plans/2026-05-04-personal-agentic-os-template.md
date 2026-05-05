# Personal Agentic OS Template Implementation Plan

> **For Hermes:** Use the usual GitHub issue-by-issue protocol: implement with TDD where applicable, request independent review, test/lint, commit on a feature branch, push, create a PR with `Closes #N`, squash merge, sync `main`, then continue only after the issue is closed.

**Goal:** Build a reusable 7-layer Personal Agentic OS template repo with docs, a minimal example app, validation checks, and applicability guidance.

**Architecture:** The repo will be a template-first Python project. The template structure is documentation-driven, with optional lightweight Python tooling to validate the layer manifest and run a tiny example app. Each issue produces a self-contained artifact that can be reviewed and merged independently.

**Tech Stack:** Markdown, Python 3.11+, pytest, Ruff, optional Typer CLI for validation/example commands.

---

## Issue 1 — Scaffold repo, Python package, and quality tooling

Objective: Create a minimal Python project with test/lint tooling and CLI entrypoint.

Deliverables:
- `pyproject.toml`
- `src/agentic_os_template/`
- `tests/`
- CLI help command
- README quickstart

Acceptance criteria:
- `uv run --extra dev python -m pytest -q` passes.
- `uv run --extra dev ruff check .` passes.
- `uv run agentic-os-template --help` works.

## Issue 2 — Define the 7-layer template structure

Objective: Add one folder per layer with README guidance and a machine-readable manifest.

Deliverables:
- `template/identity/README.md`
- `template/context/README.md`
- `template/skills/README.md`
- `template/memory/README.md`
- `template/connections/README.md`
- `template/verification/README.md`
- `template/automations/README.md`
- `template/layers.yaml` or JSON manifest
- tests validating all seven layers exist and are documented

Acceptance criteria:
- Every layer has purpose, inputs, outputs, failure mode, and examples.
- Manifest order matches the seven-layer model.
- Tests fail if a layer README or manifest entry is missing.

## Issue 3 — Add tiny example app exercising all seven layers

Objective: Build a small readable example, likely a daily-brief or personal-CRM stub, that touches every layer without overengineering.

Deliverables:
- `examples/daily_brief/` or `examples/personal_crm/`
- sample data
- simple CLI/example runner
- tests proving every layer is exercised

Acceptance criteria:
- Example can run locally with a deterministic output.
- Example references all seven layers explicitly.
- No external API keys or network calls are required.

## Issue 4 — Add adoption checklist and scaffold validation command

Objective: Make the template actionable for future projects.

Deliverables:
- `docs/adoption-checklist.md`
- CLI validation command for a scaffold instance
- tests for validation success/failure

Acceptance criteria:
- Checklist helps decide what belongs in each layer.
- Validation detects missing layer directories/docs.
- Validation output is deterministic and CI-friendly.

## Issue 5 — Map backlog projects and P³-style systems to the scaffold

Objective: Demonstrate applicability with concrete mappings.

Deliverables:
- `docs/mappings/p3.md`
- `docs/mappings/trade-thesis-journal.md`
- `docs/mappings/health-metrics-forecaster.md`
- optional mapping for signal-newsletter or weekly intelligence brief

Acceptance criteria:
- Mapping docs distinguish mature, partial, missing, and not-applicable layers.
- P³ mapping explicitly marks verification as filled by eval/quality-gate work where appropriate, not hand-waved.
- Docs explain how mappings guide future issue placement.

## Issue 6 — Closeout docs and template readiness review

Objective: Finish V1 with usage docs, roadmap, retrospective, and source issue closeout.

Deliverables:
- `docs/usage.md`
- `docs/roadmap.md`
- `docs/retrospectives/v1-retrospective.md`
- final source project-ideas closeout comment after merge

Acceptance criteria:
- Retrospective includes where the template is useful vs overkill.
- Repo has no open execution issues/PRs before source issue closure.
- Source issue #33 is updated with repo and artifact links and closed after final PR merges.
