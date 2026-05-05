import json
import subprocess
import sys
from pathlib import Path

from personal_agentic_os_template.example import build_daily_brief


def test_example_builds_artifacts_for_all_layers(tmp_path):
    report = build_daily_brief(tmp_path)

    assert [item["layer"] for item in report["layers"]] == [
        "identity",
        "context",
        "skills",
        "memory",
        "connections",
        "verification",
        "automations",
    ]
    for item in report["layers"]:
        assert (tmp_path / item["path"]).exists()


def test_example_cli_writes_json_report(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "personal_agentic_os_template.cli",
            "example",
            str(tmp_path),
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    data = json.loads(result.stdout)
    assert data["example"] == "daily-brief"
    assert Path(tmp_path / "verification" / "report.json").exists()
