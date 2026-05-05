import json
import subprocess
import sys
from pathlib import Path

from personal_agentic_os_template.scaffold import validate_scaffold


def test_validate_scaffold_reports_ready_template():
    report = validate_scaffold(Path("template"))

    assert report["ok"] is True
    assert report["missing"] == []
    assert report["layer_count"] == 7


def test_validate_cli_outputs_json():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "personal_agentic_os_template.cli",
            "validate",
            "template",
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    data = json.loads(result.stdout)
    assert data["ok"] is True
    assert data["layer_count"] == 7


def test_validate_cli_exits_nonzero_with_json_for_invalid_scaffold(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "personal_agentic_os_template.cli",
            "validate",
            str(tmp_path),
        ],
        check=False,
        text=True,
        capture_output=True,
    )

    data = json.loads(result.stdout)
    assert result.returncode == 1
    assert data["ok"] is False
    assert data["missing"] == ["missing manifest: layers.yaml"]


def test_adoption_checklist_exists():
    content = Path("docs/adoption-checklist.md").read_text(encoding="utf-8")

    assert "Identity" in content
    assert "Verification" in content
    assert "Automations" in content
