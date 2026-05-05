from dataclasses import dataclass
from pathlib import Path

LAYER_NAMES = [
    "identity",
    "context",
    "skills",
    "memory",
    "connections",
    "verification",
    "automations",
]


@dataclass(frozen=True)
class Layer:
    name: str
    purpose: str
    readme: str
    required_files: list[str]


@dataclass(frozen=True)
class LayerManifest:
    layers: list[Layer]


def load_manifest(path: Path) -> LayerManifest:
    if not path.exists():
        raise FileNotFoundError(path)
    layers: list[Layer] = []
    current: dict[str, str | list[str]] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line == "layers:":
            continue
        if line.startswith("- name: "):
            if current is not None:
                layers.append(_layer_from_mapping(current))
            current = {"name": line.removeprefix("- name: ").strip('"')}
        elif current is not None and ": " in line:
            key, value = line.split(": ", 1)
            current[key] = value.strip('"')
        elif current is not None and line.startswith("- "):
            current.setdefault("required_files", [])
            required = current["required_files"]
            if isinstance(required, list):
                required.append(line.removeprefix("- ").strip('"'))
    if current is not None:
        layers.append(_layer_from_mapping(current))
    return LayerManifest(layers=layers)


def _layer_from_mapping(mapping: dict[str, str | list[str]]) -> Layer:
    required_files = mapping.get("required_files", [])
    if not isinstance(required_files, list):
        required_files = []
    return Layer(
        name=str(mapping["name"]),
        purpose=str(mapping["purpose"]),
        readme=str(mapping["readme"]),
        required_files=required_files,
    )


def validate_layers(template_dir: Path, manifest: LayerManifest) -> list[str]:
    problems: list[str] = []
    names = [layer.name for layer in manifest.layers]
    if names != LAYER_NAMES:
        problems.append("manifest layer order must match canonical seven-layer order")
    for layer in manifest.layers:
        layer_dir = template_dir / layer.name
        readme = layer_dir / layer.readme
        if not layer_dir.is_dir():
            problems.append(f"missing layer directory: {layer.name}")
        if not readme.is_file():
            problems.append(f"missing README for layer: {layer.name}")
            continue
        content = readme.read_text(encoding="utf-8").lower()
        required_headings = [
            "purpose",
            "inputs",
            "outputs",
            "common failure modes",
            "examples",
        ]
        for heading in required_headings:
            if heading not in content:
                problems.append(f"{layer.name} README missing {heading}")
        for filename in layer.required_files:
            if not (layer_dir / filename).exists():
                problems.append(f"{layer.name} missing required file: {filename}")
    return problems
