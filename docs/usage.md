# Usage

## Quickstart

Clone or fork this repository when starting a personal AI infrastructure project that needs explicit layers for identity, context, skills, memory, connections, verification, and automations.

```bash
uv run --extra dev python -m pytest -q
uv run --extra dev ruff check .
uv run agentic-os-template --help
uv run agentic-os-template layers
uv run agentic-os-template validate template
uv run agentic-os-template example /tmp/agentic-os-daily-brief
```

## How to use the template

1. Fork the repo or copy the `template/` directory into a new project.
2. Rename or update project metadata such as README title, package name, repository links, and source-issue references if the fork becomes a standalone project.
3. Fill in each layer README with project-specific decisions and artifacts.
4. Use `docs/adoption-checklist.md` to decide what belongs in each layer.
5. Use `docs/project-mappings.md` as examples for issue placement and sequencing.
6. Run `agentic-os-template validate template` before merging scaffold changes.
7. Add tests for any project-specific commands or generated artifacts.

## Validation command

`agentic-os-template validate template` emits deterministic JSON and exits nonzero when the scaffold is missing `layers.yaml`, a layer directory, required README, or required README sections.

## Example command

`agentic-os-template example /tmp/agentic-os-daily-brief` generates a deterministic no-network daily brief example that writes one artifact per layer and a JSON verification report.

## When to fork

Fork this template when the project will accumulate enough context, memory, verification, or automation surface area that a single README would become ambiguous. For a one-off script or throwaway prototype, this scaffold may be too heavy.
