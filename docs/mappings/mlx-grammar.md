# MLX Grammar layer mapping

Status vocabulary: mature, partial, missing, not applicable.

| Layer | Status | Evidence and gap |
| --- | --- | --- |
| Identity | mature | The repo identity is a local-first structured-output helper for MLX-style workflows, with a baseline path that does not require Apple Silicon, model downloads, or MLX imports. |
| Context | mature | Usage, security/privacy, roadmap, and retrospective docs capture what the V1 does and does not claim. Source issue closeout links the implementation history. |
| Skills | partial | The useful reusable skills are schema-first generation, optional backend boundaries, and fixture eval authoring. They are present in code/docs but not yet packaged as a forkable scaffold. |
| Memory | partial | Retrospective guidance records where the tool is useful, but there is no dedicated memory/index layer beyond docs. |
| Connections | partial | The MLX backend boundary is explicit and optional; real MLX execution remains gated by dependency/environment checks. External model connections are intentionally deferred. |
| Verification | mature | Evidence includes pytest/Ruff, deterministic fixture eval runner, empty-glob failure via `EvalRunError`, optional smoke-test gate `MLX_GRAMMAR_RUN_MLX_SMOKE=1`, and independent review before merge. |
| Automations | missing | No scheduled runs or release automation are part of V1. Add only after fixture eval reports become stable release artifacts. |

## Sequencing guidance

Next issues should improve Verification and Connections before Automations: add more fixture corpora, clearer backend capability reporting, and release artifact checks before scheduling anything.
