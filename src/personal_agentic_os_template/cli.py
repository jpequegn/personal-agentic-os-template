from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from personal_agentic_os_template import __version__

app = typer.Typer(help="Reusable 7-layer Personal Agentic OS scaffold tools.")
console = Console()

LAYERS = [
    ("identity", "Purpose, boundaries, roles, and operating principles."),
    ("context", "Project state, source snapshots, plans, and active constraints."),
    ("skills", "Reusable procedures, prompts, commands, and implementation playbooks."),
    ("memory", "Durable facts, decisions, retrospectives, and retrieval surfaces."),
    (
        "connections",
        "Repositories, tools, APIs, humans, and organizational interfaces.",
    ),
    ("verification", "Tests, checks, reviews, evals, and quality gates."),
    ("automations", "Scheduled or event-driven workflows that keep the system alive."),
]


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"personal-agentic-os-template {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option("--version", callback=_version_callback, help="Show version."),
    ] = False,
) -> None:
    """Reusable 7-layer Personal Agentic OS scaffold tools."""


@app.command()
def layers() -> None:
    """List the seven scaffold layers."""
    table = Table(title="Personal Agentic OS Layers")
    table.add_column("Layer")
    table.add_column("Purpose")
    for name, purpose in LAYERS:
        table.add_row(name, purpose)
    console.print(table)
