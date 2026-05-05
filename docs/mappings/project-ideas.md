# Project Ideas backlog layer mapping

Status vocabulary: mature, partial, missing, not applicable.

| Layer | Status | Evidence and gap |
| --- | --- | --- |
| Identity | mature | The backlog is a source-of-truth idea queue for project selection and execution. It optimizes for concrete repos, artifacts, and source issue closeout. |
| Context | mature | Each issue body stores the source idea, rationale, and links. Bootstrap comments add execution repo, plan, checklist, and backlog links. |
| Skills | partial | Selection, repo bootstrap, implementation protocol, and closeout protocol are recurring skills, but not every issue encodes the protocol directly. |
| Memory | partial | Closed source issues and closeout comments preserve durable outcomes, but cross-project lessons still need retrospectives or memories to become reusable. |
| Connections | mature | GitHub issues connect source ideas to execution repos, PRs, docs, and final artifacts. |
| Verification | partial | Execution repos have tests/reviews, but the backlog itself does not enforce quality gates before an idea is selected. |
| Automations | missing | No automatic triage, stale issue detection, or validation reminders are currently part of the backlog. |

## Sequencing guidance

Use Context to choose and scope, then create Skills/Verification issues inside the execution repo. Close the source issue only after execution-repo issues and PRs are complete.
