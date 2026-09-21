# Contributing to agentsafe-install

Thank you for your interest in agentsafe-install. This is a learning-focused project, so questions, documentation improvements, experiments, and small implementation changes are welcome.

## Before you start

Please read the [README](README.md) to understand the project's purpose, current limitations, and roadmap. The current CLI is an early scaffold, not a production security tool.

For security-sensitive reports, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Good first contributions

- Improve explanations or examples in the documentation.
- Add a focused experiment that teaches one relevant technology.
- Clarify policy terminology and expected behavior.
- Add tests for behavior that is already intended and understood.
- Document provider APIs, trade-offs, or failed approaches.
- Review a proposed change for clarity, safety, and learning value.

## Development principles

- Keep changes small and explainable.
- Prefer explicit behavior over hidden automation.
- Separate provider integrations from policy and decision logic.
- Do not claim that a security check works until it has evidence and tests.
- Treat unavailable or unverifiable information conservatively.
- Document important assumptions and trade-offs.
- Avoid collecting secrets, tokens, or unnecessary package data.

## Local setup

The project targets Python 3.11 or newer:

\`\`\`bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -e .
\`\`\`

The package and its interfaces are still evolving. If setup does not work as expected, document the environment and the exact error in your report.

## Making a change

1. Create a focused branch for your experiment or improvement.
2. Make the smallest change that demonstrates the idea.
3. Update documentation when behavior, assumptions, or commands change.
4. Add or update tests when the behavior is testable.
5. Review the diff for accidental secrets, credentials, generated files, or unrelated edits.
6. Use a clear commit message that describes the change.

## Pull requests

A useful pull request should explain:

- What changed
- Why the change is useful
- What was learned or validated
- How it was tested
- What remains intentionally incomplete

Please keep pull requests narrow enough to review and discuss. A learning experiment does not need to be production-ready, but it should clearly state its limitations.

## Code review expectations

Reviews should be constructive and specific. Focus on correctness, clarity, safety, evidence, and learning value. It is appropriate to request documentation or tests when a change would otherwise be difficult to understand or trust.

## License

By contributing to agentsafe-install, you agree that your contributions will be licensed under the [MIT License](LICENSE).
