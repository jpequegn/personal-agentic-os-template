from typer.testing import CliRunner

from personal_agentic_os_template.cli import app


def test_cli_shows_version():
    result = CliRunner().invoke(app, ["--version"])

    assert result.exit_code == 0
    assert "personal-agentic-os-template" in result.output


def test_cli_help_describes_scaffold_tools():
    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Reusable 7-layer Personal Agentic OS scaffold tools" in result.output


def test_cli_lists_layers_command_exists():
    result = CliRunner().invoke(app, ["layers"])

    assert result.exit_code == 0
    assert "identity" in result.output.lower()
    assert "automations" in result.output.lower()
