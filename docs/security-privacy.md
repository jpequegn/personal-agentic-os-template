# Security and privacy

## No secrets in the scaffold

No secrets, API keys, tokens, passwords, or private credentials should be committed to this repository or to projects forked from it. Document authentication requirements in the Connections layer, but store credentials in the user's secret manager or local environment.

## Local-first default

The template, validation command, and daily brief example are local by default. They do not require network access, external services, or private data. This makes the scaffold safe to test in CI and easy to fork.

## Privacy boundaries

Personal Agentic OS projects often touch sensitive notes, health metrics, emails, trading logs, or work artifacts. Each adopted project should document:

- what data is collected
- what data is persisted
- what data must never be persisted
- how exports and logs are redacted
- who or what can read generated artifacts

## Network and automation risk

Network connections and automations should be added only after Verification is mature. A project should have deterministic tests, dry-run behavior, and rollback notes before a scheduled job, webhook, or API-writing workflow is enabled.

## Template limitation

This repository is a scaffold, not a security product. It provides structure and checklists, but it does not enforce access control, encryption, or compliance requirements by itself.
