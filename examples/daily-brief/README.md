# Daily brief example

This deterministic example shows how a tiny personal AI workflow can use every scaffold layer without network access, API keys, or private data.

Run it with:

```bash
uv run agentic-os-template example /tmp/agentic-os-daily-brief
```

The command writes one artifact per layer plus `verification/report.json`.

Layer coverage:

- identity: local brief policy
- context: fixture inputs and rendered brief
- skills: summarization procedure note
- memory: example design decision
- connections: local fixture source list
- verification: checks and JSON report
- automations: scheduling note
