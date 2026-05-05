from pathlib import Path

from personal_agentic_os_template.layers import (
    LAYER_NAMES,
    load_manifest,
    validate_layers,
)


def test_manifest_defines_exactly_seven_layers():
    manifest = load_manifest(Path("template/layers.yaml"))

    assert [layer.name for layer in manifest.layers] == LAYER_NAMES
    assert all(layer.readme for layer in manifest.layers)
    assert all(layer.required_files for layer in manifest.layers)


def test_template_has_readme_for_each_layer():
    manifest = load_manifest(Path("template/layers.yaml"))
    problems = validate_layers(Path("template"), manifest)

    assert problems == []


def test_validation_reports_missing_layer_readme(tmp_path):
    manifest = load_manifest(Path("template/layers.yaml"))
    problems = validate_layers(tmp_path, manifest)

    assert "missing layer directory: identity" in problems
    assert "missing README for layer: identity" in problems
