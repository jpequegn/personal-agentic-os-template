from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_closeout_docs_exist_and_cover_readiness():
    docs = {
        "docs/usage.md": ["Quickstart", "validate", "example", "fork"],
        "docs/security-privacy.md": ["No secrets", "local", "privacy", "network"],
        "docs/roadmap.md": ["V1", "future", "non-goals", "automation"],
        "docs/retrospectives/v1-readiness-review.md": [
            "template readiness",
            "applicability guidance",
            "source issue closeout",
            "project-ideas issue #33",
            "no open execution-repo issues or PRs",
        ],
    }
    for path, phrases in docs.items():
        content = read(path)
        for phrase in phrases:
            assert phrase.lower() in content.lower()


def test_readme_and_checklist_link_closeout_docs():
    readme = read("README.md")
    checklist = read("docs/issue-checklist.md")

    for path in [
        "docs/usage.md",
        "docs/security-privacy.md",
        "docs/roadmap.md",
        "docs/retrospectives/v1-readiness-review.md",
    ]:
        assert path in readme
    assert "[x] #6" in checklist
