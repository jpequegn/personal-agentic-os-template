# Health Metrics Forecaster layer mapping

Status vocabulary: mature, partial, missing, not applicable.

| Layer | Status | Evidence and gap |
| --- | --- | --- |
| Identity | partial | The system should help interpret personal health trends, but it must explicitly avoid diagnosis and medical advice claims. |
| Context | partial | Candidate context includes wearable exports, sleep logs, symptoms, and subjective notes. Data provenance and recency rules are missing. |
| Skills | missing | Skills such as anomaly explanation, trend summaries, and experiment retrospectives need narrow definitions and human review boundaries. |
| Memory | partial | Longitudinal baselines are useful memory, but retention/privacy rules and redaction practices must be defined. |
| Connections | partial | Wearable/file imports are plausible; API connections should remain optional and documented without secrets. |
| Verification | missing | Verification needs fixture datasets, privacy checks, calibration notes, and explicit non-diagnostic language gates before use. |
| Automations | missing | Automated forecasts or alerts are overkill until Verification matures and false-positive handling is documented. |

## Sequencing guidance

Begin with privacy-aware Identity, then deterministic Context fixtures, then Verification gates for non-diagnostic wording before any Automation work.
