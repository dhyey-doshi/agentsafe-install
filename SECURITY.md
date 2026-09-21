# Security Policy

## Current scope

agentsafe-install is an early, learning-focused project. The current implementation is not a complete security product and should not be relied on as the only protection for package installation.

The project may eventually handle package names, versions, registry metadata, vulnerability information, provenance data, and signatures. Please avoid including real secrets, private package metadata, access tokens, or sensitive system information in issues, pull requests, logs, or example files.

## Reporting a potential vulnerability

Please do not disclose a suspected vulnerability in a public issue.

Contact the maintainer privately through the [Dhyey Doshi GitHub profile](https://github.com/dhyey-doshi) and include:

- A concise description of the issue
- The affected file, command, or behavior
- Reproduction steps or a minimal proof of concept
- The expected and observed behavior
- Any relevant version, operating-system, or environment details
- Your assessment of potential impact

If the report contains sensitive material, share only the minimum necessary information and redact secrets before sending it.

## What to expect

This project is maintained as a learning effort, so response times may vary. The maintainer will try to:

1. Acknowledge the report when possible.
2. Reproduce and understand the issue.
3. Assess its impact and affected versions.
4. Coordinate a fix or document the limitation.
5. Credit the reporter if they want to be credited.

Please do not publicly disclose the issue until a fix or coordinated disclosure plan is available.

## Safe research practices

When experimenting with the project:

- Use disposable test packages or local fixtures.
- Use test credentials only, never production credentials.
- Avoid executing untrusted package installation commands on important systems.
- Do not bypass package-manager safeguards just to test the tool.
- Treat advisory results as incomplete until the corresponding checks are implemented and tested.

## Supported versions

There are no stable releases yet. The \`main\` branch is the only actively documented development target.
