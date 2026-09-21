# agentsafe-install

A local-first pre-install trust gate for AI coding agents that verifies package versions, vulnerabilities, provenance, and signatures before installation.

> This is a learning-focused project. The goal is to understand the technologies and security checks involved in safer package installation by building the system incrementally.

## Current status

The repository currently contains an early CLI and policy configuration skeleton. The command can load a local policy and return an advisory JSON decision, but registry lookups, vulnerability providers, provenance checks, signature verification, and installation enforcement are not wired yet.

Do not treat the current output as a complete security decision or as a replacement for your package manager's normal safeguards.

## Why this project exists

AI coding agents can suggest and execute package-installation commands quickly. That speed makes it useful to place a transparent trust gate before installation. agentsafe-install is intended to make the checks explicit and configurable rather than silently trusting every requested dependency.

The project is designed to explore:

- Package metadata and version resolution
- Vulnerability intelligence and severity normalization
- Package provenance and publisher verification
- Integrity and signature verification
- Deterministic, explainable allow/warn/block decisions
- Local-first policies that can be reviewed before use

## Planned workflow

The intended workflow is:

1. Receive a package request from an agent or developer.
2. Resolve the package and requested version from an allowed registry.
3. Check version constraints, vulnerabilities, provenance, and signatures.
4. Evaluate the findings against a local policy.
5. Return an explainable decision: allow, warn, or block.
6. Permit installation only after the decision passes the configured gate.

This workflow is a roadmap, not a claim that all steps are implemented today.

## Repository layout

\`\`\`text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
policies/default.json
pyproject.toml
src/agentsafe/cli.py
\`\`\`

| Path | Purpose |
| --- | --- |
| \`policies/default.json\` | Initial example policy for local decisions. |
| \`src/agentsafe/cli.py\` | Current Typer-based command-line entry point. |
| \`pyproject.toml\` | Python package metadata and console-script configuration. |
| \`CONTRIBUTING.md\` | Guidance for learning, experimenting, and contributing. |
| \`SECURITY.md\` | Responsible vulnerability-reporting guidance. |
| \`CODE_OF_CONDUCT.md\` | Community participation expectations. |

## Installation

The package targets Python 3.11 or newer.

Create an isolated environment and install the project in editable mode:

\`\`\`bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -e .
\`\`\`

The implementation is still under active development, so installation only provides the current learning scaffold.

## Current CLI usage

The currently declared console command is:

\`\`\`bash
agentsafe check PACKAGE
\`\`\`

You can provide another policy file with:

\`\`\`bash
agentsafe check PACKAGE --policy path/to/policy.json
\`\`\`

For example:

\`\`\`bash
agentsafe check requests@2.32.3
\`\`\`

At the current stage, this produces an advisory JSON response and explicitly reports that external registry, vulnerability, and provenance providers are not wired yet.

## Policy configuration

The example policy is stored in \`policies/default.json\`:

\`\`\`json
{
  "default_if_unverified": "warn",
  "block_severity_at_or_above": "high",
  "require_exact_version": true,
  "require_provenance": false,
  "allowed_registries": [
    "https://registry.npmjs.org",
    "https://pypi.org"
  ]
}
\`\`\`

These fields describe the intended policy direction. They should be considered configuration placeholders until the corresponding checks are implemented and tested.

## Learning roadmap

The project will be developed in small, reviewable steps:

- Define typed models for package requests, findings, policies, and decisions.
- Implement policy loading and validation.
- Add read-only package metadata lookups for npm and PyPI.
- Add vulnerability-provider adapters and normalized severity handling.
- Explore provenance and publisher metadata.
- Explore signatures and integrity verification.
- Build a deterministic decision engine with useful explanations.
- Add tests for safe, warning, blocking, and provider-failure scenarios.
- Integrate the decision gate with installation workflows only after the checks are reliable.

## Project principles

- Local-first and inspectable configuration
- Explicit, explainable decisions
- Fail safely when verification is unavailable
- Small integrations that can be tested independently
- Learning before automation
- No claim of security without evidence and tests

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change. Ideas, documentation improvements, experiments, and carefully scoped implementation work are welcome.

## Security

Please read [SECURITY.md](SECURITY.md) before reporting a potential vulnerability.

## Code of conduct

Participation in this project is governed by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).
