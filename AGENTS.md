# AI Practical Handbook — Agent Guide

This repository is a public educational reference, not a software service. Its
Markdown is read directly on GitHub; there is no reader-side build, runtime,
datastore, or secret.

- **Entries and indexes:** follow the [dictionary contract](docs/specs/dictionary.md)
  before editing `dictionary/`. For reader-facing tutorials in `workflows/`, follow
  the [workflow contract](docs/specs/workflows.md). Use [CONTEXT.md](CONTEXT.md) for editorial terms.
- **Documentation:** the [blueprint](docs/docs-organization-blueprint.md) owns
  filing, scratch space, and lifecycle rules. Use the [wiki index](docs/index.md)
  to find decisions and specifications.
- **Checks:** after changing a spec, regenerate its diagram with
  `python3 scripts/render_spec_ir.py <spec.md>` (requires PyYAML and markdown-it-py).
  Run `python3 -m unittest discover -s tests` with those same dependencies before
  publishing; review both languages for clarity and factual parity.
