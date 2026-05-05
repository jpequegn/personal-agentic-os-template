# Source project idea #33

Source: https://github.com/jpequegn/project-ideas/issues/33
Title: Personal Agentic OS Scaffold — 7-Layer Reorg of P³ + Reusable Template
State at bootstrap: OPEN

---

## Overview
A reusable scaffold (template repo + reference doc) for building "Personal Agentic OS" projects, applying the **7-layer model** from EP 1350 (AI Breakdown — *How To Build a Personal Agentic Operating System*): identity, context, skills, memory, connections, verification, automations. Forces an explicit reorg of P³ along these layers (clarifies the architecture *and* exposes gaps), and produces a starter template anyone can fork to build a personal AI infra project in any domain (finance, health, research, CRM).

## Problem
P³ today is "a pile of CLI commands and a launchd job" with implicit layering. It works, but it's hard to:
- Onboard a new contributor (or future-you) to the architecture
- Identify what's missing (e.g., the verification layer is *empty* — that's the eval-library issue)
- Reuse parts of it for adjacent projects (Trade Thesis Journal, Daily Brief, Health Metrics)

The 7-layer Agent OS model from EP 1350 names the parts of a personal AI system explicitly. Mapping P³ to it makes the architecture legible **and** reveals which layers are mature, partial, or missing. Done well, the same scaffold drops onto adjacent projects.

This is more conceptual reorg than new code, but it's the kind of work Cat Wu calls "removing barriers to shipping" — once the layers are explicit, every future feature has a clear home.

## What to Build
Two artifacts:

**(1) P³-internal reorg**
- Map every P³ component to one of the 7 layers:
  - **Identity** — `feeds.yaml`, `interest_signal_engine`
  - **Context** — `episodes` table, `transcript_quality_score`, `filter_decisions`
  - **Skills** — CLI commands (`fetch`, `transcribe`, `digest`, `write`, `interrogate`, `query`)
  - **Memory** — `summaries` table + FTS index + `quote bank` (TBD)
  - **Connections** — RSS sources, MCP servers, `transcript_fetcher` web sources
  - **Verification** — *missing today* → fill via eval-library issue
  - **Automations** — launchd pipeline, `setup-pipeline-service`
- Update `CLAUDE.md` and project README with the layer map. Add a `docs/architecture.md` with the diagram.
- For the verification layer (currently empty): explicit pointer to the eval-library issue and the grammar-constrained-output issue as the work that fills it.

**(2) Reusable template repo** — `personal-agentic-os-template`
- Skeleton directory structure with one folder per layer
- Each layer ships with a README explaining its purpose + 1–2 example modules
- Example "starter app" — a tiny personal CRM or daily-brief that exercises all 7 layers minimally
- Documentation: when does each layer matter? How do you know it's missing?
- License: MIT, public

## Architecture sketch
```
                       ┌──────────────┐
                       │  Identity    │  who am I, what do I care about
                       └──────┬───────┘
                              │
                       ┌──────▼───────┐
                       │  Context     │  what's happened, what's known
                       └──────┬───────┘
                              │
            ┌─────────────────┼──────────────────┐
            ▼                 ▼                  ▼
       ┌─────────┐      ┌──────────┐      ┌────────────┐
       │  Skills │      │  Memory  │      │ Connections│
       │ (verbs) │◄────►│  (DB)    │◄────►│ (sources)  │
       └────┬────┘      └──────────┘      └────────────┘
            │
            ▼
       ┌──────────────┐
       │ Verification │  evals, schema gates, quality scorers
       └──────┬───────┘
              ▼
       ┌──────────────┐
       │ Automations  │  cron, launchd, watchers
       └──────────────┘
```

## Tech Stack
Markdown for the doc. The template repo can be Python (matching P³'s ecosystem), but the layer model is language-agnostic — note that explicitly. Optional: a `cookiecutter` template for fast scaffolding.

## Broader Applications (beyond P³)
The whole point of this issue is reuse. The 7-layer scaffold applies to:
- **Trade Thesis Journal** (existing issue #24) — identity (your strategy), context (positions held), skills (analyze, journal), memory (past trades), connections (broker, market data), verification (PnL truth check), automations (daily journal prompt).
- **Health Metrics Forecaster** (existing issue #27) — identity (you), context (vitals history), skills (ingest, forecast), memory (long-term trends), connections (Apple Health, Whoop), verification (sanity bands), automations (daily ingest).
- **Personal Context Engine** (existing issue #28) — heavy memory + connections layers, partial others.
- **Universal Signal Ingestion** (#12) — heavy connections layer.
- Future projects: personal CRM, research assistant, investment dashboard.

This issue is *infrastructure for the rest of the backlog*.

## Open Decisions
- **Should the template be opinionated** (Python + DuckDB + MCP) or language-neutral (just docs)? Opinionated is more useful for the user; neutral is more reusable. Probably go opinionated to match what works for him.
- **How thin should the example app be**? Thin enough to read in 10 min, fat enough to actually exercise all 7 layers without hand-waving.
- **Public vs. private**? Probably public for the template repo (low sensitivity), private for the P³ reorg.
- **Cross-link with Featureform pattern** (issue #28's four pillars)? Yes — the 4-pillar pattern is a sub-pattern of the memory + context layers. Note the relationship.

## Success Metrics
- P³ docs explicitly identify 7 layers; every component maps to exactly one. No orphans.
- Verification layer gap is filled (via eval-library issue) — fail closed if no scorers exist.
- Template repo gets used by ≥1 other project in the backlog within 60 days (e.g., #24 or #27 reorg around the layers).
- "Where does this new feature go?" decisions are unambiguous after the reorg — measurable as PRs that don't get reworked due to "wrong place" comments.

## Suggested Milestones
- **M1** P³ component → layer mapping doc. `docs/architecture.md` with diagram. Cross-references to other issues that fill specific layers.
- **M2** Update P³ README and CLAUDE.md. Skim every CLI command's docstring; ensure each names its layer.
- **M3** Create `personal-agentic-os-template` repo. Skeleton + READMEs per layer.
- **M4** Build a tiny example app inside the template that exercises all 7 layers. Could be a personal CRM or daily-brief for a single domain.
- **M5** Apply the template to one existing backlog issue (#24 or #27) — does it actually cleanly fit?

## Why Now
The Agent OS framework is fresh from EP 1350; nobody else has applied it as a reusable template yet. P³ is mature enough that the reorg pays back immediately (clearer architecture, easier feature placement) without being so calcified that reorg is painful. And the template, once written, accelerates every other backlog project that touches personal AI.

