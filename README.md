# Awesome DeepSeek Harness Plugins

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Catalog validation](https://github.com/dsh-external/awesome-DSH-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/dsh-external/awesome-DSH-plugin/actions/workflows/validate.yml)

> A community-curated, vendor-neutral catalog of plugins for DeepSeek Harness (DSH) — from developer tooling and data workflows to media, operations, and everyday life.

**Language:** English | [简体中文](docs/README.zh-CN.md)

DeepSeek Harness plugins can connect an agent to tools, services, devices, and repeatable workflows. This list is intentionally broad: if it gives an agent a useful real-world capability, it belongs here.

## Contents

- [Getting started](#getting-started)
- [Plugin catalog](#plugin-catalog)
  - [Developer tools](#developer-tools)
  - [Agent orchestration & automation](#agent-orchestration--automation)
  - [Productivity & collaboration](#productivity--collaboration)
  - [Data, research & knowledge](#data-research--knowledge)
  - [Cloud, DevOps & observability](#cloud-devops--observability)
  - [AI, design & media](#ai-design--media)
  - [Business, finance & commerce](#business-finance--commerce)
  - [Life, devices & the physical world](#life-devices--the-physical-world)
- [Add a plugin](#add-a-plugin)
- [Catalog rules](#catalog-rules)
- [License](#license)

## Getting started

1. Browse a category below and open a plugin's repository or marketplace page.
2. Follow that plugin's installation instructions for DeepSeek Harness.
3. Restart or reload DeepSeek Harness if the plugin requires it.

> The catalog links to third-party projects. Review a plugin's source, permissions, and data-handling policy before installing it.

## Plugin catalog

<!-- CATALOG:START -->
### Developer tools

- [dsh-at-file](https://github.com/FSMargoo/dsh-at-file) — Adds Codex-style @file mentions to search workspace files and attach their contents to prompts.

- [dsh-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) — A full-featured sidebar workbench for DSH — file explorer, editor/preview, terminal, Git panel, embedded browser — with a service API for third-party tabs and file viewers.

- [dsh-custom-tool](https://github.com/FSMargoo/dsh-custom-tool) — Create and manage sandboxed JavaScript tools with a Monaco editor and a model-driven lifecycle.

- [dsh-open-in-vscode](https://github.com/FSMargoo/dsh-open-in-vscode) — Open DeepSeek Harness workspace directories in VS Code from the web interface.

### Agent orchestration & automation

- [mstar-harness](https://github.com/btspoony/mstar-harness) — A skill-driven workflow agent plugin for structured harness-loop engineering.

### Productivity & collaboration

- [dsh-notification](https://github.com/FSMargoo/dsh-notification) — Sends desktop notifications when a DeepSeek Harness turn completes, with outcome and keyword rules.

### Data, research & knowledge

No entries yet. [Submit the first plugin.](CONTRIBUTING.md)

### Cloud, DevOps & observability

No entries yet. [Submit the first plugin.](CONTRIBUTING.md)

### AI, design & media

- [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) — A hand-drawn pixel whale companion for the DSH Web UI that reacts to agent activity.

- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) — Adds image Q&A, long-screenshot OCR, UI restoration, visual grounding, pixel diffs, and artifacts.

### Business, finance & commerce

No entries yet. [Submit the first plugin.](CONTRIBUTING.md)

### Life, devices & the physical world

No entries yet. [Submit the first plugin.](CONTRIBUTING.md)
<!-- CATALOG:END -->

## Add a plugin

Additions are welcome. Please read [the contribution guide](CONTRIBUTING.md), add a bilingual entry to [`catalog/plugins.json`](catalog/plugins.json), and run:

```bash
python scripts/generate_readmes.py
python scripts/generate_readmes.py --check
```

The first command regenerates both language pages; the second verifies that committed pages match the catalog.

## Catalog rules

- The plugin must be relevant to DeepSeek Harness or provide clear installation/integration instructions for it.
- Entries need a stable public URL, a concise factual description, and both English and Simplified Chinese copy.
- Keep entries vendor-neutral, useful, and non-duplicative.
- Do not include secrets, affiliate links, unmaintained forks without context, or projects that primarily distribute malware, credential theft, or policy-violating automation.

## License

This repository is released under the [MIT License](LICENSE).
