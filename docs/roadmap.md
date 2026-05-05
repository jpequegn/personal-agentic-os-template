# Roadmap

## V1 status

V1 is a reusable template/scaffold for seven-layer personal AI infrastructure projects. It includes:

- canonical layer directories and READMEs
- manifest validation
- CLI commands for layer listing, scaffold validation, and deterministic example generation
- adoption checklist
- project mapping examples
- usage, security/privacy, and readiness docs

## Future work

- Add a `new-project` command that copies the scaffold into a target directory.
- Add stricter manifest schema validation when the YAML shape grows.
- Add snapshot tests for generated example artifacts.
- Add optional templates for common project types such as daily brief, personal CRM, research assistant, and trading journal.
- Add CI workflow examples for running validation in forked repos.

## Non-goals

- Do not become a full personal OS platform.
- Do not store credentials or private user data.
- Do not automate external services by default.
- Do not replace project-specific verification with generic checklist claims.

## Automation guidance

Automation should remain a later layer. Add scheduled jobs, watchers, or webhooks only after the project has deterministic validation, dry-run behavior, and rollback notes.
