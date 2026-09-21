from __future__ import annotations

import json
from pathlib import Path

import typer

app = typer.Typer(help="Pre-install trust gate for AI coding agents.")


def load_policy(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


@app.command()
def check(
              package: str,
              policy: Path = typer.Option(Path("policies/default.json"), "--policy"),
          ) -> None:
    """Evaluate a package request using the local deterministic policy."""
    cfg = load_policy(policy)
    if package.endswith("@"):
        raise typer.BadParameter("Package version cannot be empty.")

    decision = cfg.get("default_if_unverified", "warn")
    result = {
        "package": package,
        "decision": decision,
        "reasons": [
            "Registry, vulnerability, and provenance providers are not wired yet; treat this as an advisory result."
        ],
    }
    typer.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    app()
