import json
from pathlib import Path
from typing import Any

from personal_agentic_os_template.layers import LAYER_NAMES

SAMPLE_ITEMS = [
    {"source": "calendar", "text": "Review agentic OS scaffold PR."},
    {"source": "notes", "text": "Capture reusable layer mapping."},
    {"source": "tasks", "text": "Verify no-network example output."},
]


def build_daily_brief(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = [
        ("identity", "brief-policy.md", "Optimize for a concise local daily brief."),
        ("context", "today.json", json.dumps(SAMPLE_ITEMS, indent=2)),
        ("skills", "summarize.md", "Skill: group local items into one brief."),
        ("memory", "decisions.md", "Decision: no external APIs in the example."),
        ("connections", "sources.md", "Sources: calendar, notes, tasks fixtures."),
        (
            "verification",
            "checks.md",
            "Checks: deterministic item count and layer coverage.",
        ),
        ("automations", "schedule.md", "Schedule: run manually or from cron at 08:00."),
    ]
    report_layers: list[dict[str, str]] = []
    for layer, filename, content in artifacts:
        path = output_dir / layer / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content + "\n", encoding="utf-8")
        report_layers.append(
            {"layer": layer, "path": str(path.relative_to(output_dir))}
        )

    brief = "\n".join(f"- [{item['source']}] {item['text']}" for item in SAMPLE_ITEMS)
    brief_path = output_dir / "context" / "daily-brief.md"
    brief_path.write_text(f"# Daily Brief\n\n{brief}\n", encoding="utf-8")

    report = {
        "example": "daily-brief",
        "deterministic": True,
        "network_required": False,
        "layers": report_layers,
        "canonical_layers": LAYER_NAMES,
        "item_count": len(SAMPLE_ITEMS),
    }
    report_path = output_dir / "verification" / "report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report
