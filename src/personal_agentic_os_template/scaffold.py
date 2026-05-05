from pathlib import Path
from typing import Any

from personal_agentic_os_template.layers import load_manifest, validate_layers


def validate_scaffold(template_dir: Path) -> dict[str, Any]:
    manifest_path = template_dir / "layers.yaml"
    missing: list[str] = []
    if not manifest_path.exists():
        return {
            "ok": False,
            "template": str(template_dir),
            "layer_count": 0,
            "missing": ["missing manifest: layers.yaml"],
        }
    manifest = load_manifest(manifest_path)
    missing.extend(validate_layers(template_dir, manifest))
    return {
        "ok": not missing,
        "template": str(template_dir),
        "layer_count": len(manifest.layers),
        "missing": missing,
    }
