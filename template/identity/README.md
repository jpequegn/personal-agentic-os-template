# Identity Layer

## Purpose

Purpose, roles, boundaries, and operating principles for the system.

## Inputs

- Human intent and project-specific constraints.
- Upstream artifacts from adjacent layers.
- Repo-local files committed with the template consumer project.

## Outputs

- Clear layer artifacts that another maintainer or agent can inspect.
- Decisions and references that make the project reproducible.
- Hand-off notes for verification and automation layers.

## Common failure modes

- Storing transient task state as durable doctrine.
- Depending on an external tool without documenting the fallback.
- Mixing responsibilities from another layer and making ownership unclear.

## Examples

- `identity.md` as a project-specific layer artifact.
- A README section documenting how this layer is used in the adopted project.
