# Adoption checklist

Use this checklist when adopting the scaffold for a new personal AI infrastructure project.

## Identity

- [ ] State who the system serves and what it optimizes for.
- [ ] Document non-goals and boundaries.
- [ ] Record escalation rules for ambiguous or risky actions.

## Context

- [ ] Store source snapshots, active plans, and current constraints.
- [ ] Separate durable context from temporary task state.
- [ ] Link back to upstream issues, repos, or human decisions.

## Skills

- [ ] Capture reusable procedures as commands, scripts, prompts, or docs.
- [ ] Include trigger conditions and verification steps.
- [ ] Avoid hiding project-specific assumptions in generic skills.

## Memory

- [ ] Record stable facts, decisions, and retrospectives.
- [ ] Define what should not be persisted.
- [ ] Include retrieval paths or indexes when the memory grows.

## Connections

- [ ] List required tools, files, APIs, humans, and repositories.
- [ ] Document authentication requirements without storing secrets.
- [ ] Provide local or mock fallbacks when possible.

## Verification

- [ ] Add tests, lint, review criteria, and quality gates.
- [ ] Define deterministic fixtures for local validation.
- [ ] Specify what must pass before merge or automation.

## Automations

- [ ] Document schedules, triggers, ownership, and rollback steps.
- [ ] Prefer no-op or dry-run defaults until the workflow is trusted.
- [ ] Keep logs or reports that make automation outcomes inspectable.
