from pathlib import Path

MAPPING_DOCS = [
    Path("docs/mappings/p3.md"),
    Path("docs/mappings/signal-newsletter.md"),
    Path("docs/mappings/mlx-grammar.md"),
    Path("docs/mappings/project-ideas.md"),
    Path("docs/mappings/trade-thesis-journal.md"),
    Path("docs/mappings/health-metrics-forecaster.md"),
]

LAYERS = [
    "Identity",
    "Context",
    "Skills",
    "Memory",
    "Connections",
    "Verification",
    "Automations",
]


def test_backlog_mapping_doc_covers_required_projects_and_layers():
    content = Path("docs/project-mappings.md").read_text(encoding="utf-8")

    for project in ["P³", "signal-newsletter", "mlx-grammar", "project-ideas"]:
        assert project in content
    for mapping in [str(path) for path in MAPPING_DOCS]:
        assert mapping in content
    for layer in LAYERS:
        assert layer in content
    for status in ["mature", "partial", "missing"]:
        assert status in content.lower()


def test_each_mapping_classifies_every_layer():
    allowed_statuses = ["mature", "partial", "missing", "not applicable"]
    for path in MAPPING_DOCS:
        content = path.read_text(encoding="utf-8")
        for layer in LAYERS:
            assert f"| {layer} |" in content
        for line in content.splitlines():
            if line.startswith("| ") and not line.startswith("| ---"):
                cells = [cell.strip().lower() for cell in line.strip("|").split("|")]
                if cells[0] in [layer.lower() for layer in LAYERS]:
                    assert cells[1] in allowed_statuses


def test_p3_verification_links_to_concrete_quality_work():
    content = Path("docs/mappings/p3.md").read_text(encoding="utf-8")

    for evidence in [
        "mlx-grammar",
        "fixture eval runner",
        "signal-newsletter",
        "quality gates",
    ]:
        assert evidence in content


def test_readme_links_project_mapping_doc():
    content = Path("README.md").read_text(encoding="utf-8")

    assert "docs/project-mappings.md" in content
