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

- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) — A sidebar workbench with extensible tabs, file viewing and editing, terminal, Git, and sub-agent tools.

- [dsh-artifact](https://github.com/william-jin-cmu/dsh-artifact) — A send_artifact tool that validates model-produced files and delivers structured descriptors through the standard dsh event stream for any client to render.

- [dsh-at-file](https://github.com/FSMargoo/dsh-at-file) — Adds Codex-style @file mentions to search workspace files and attach their contents to prompts.

- [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) — Embeds a headed browser in the DSH Web UI so agents can operate a real browser with visible steps.

- [dsh-custom-tool](https://github.com/FSMargoo/dsh-custom-tool) — Create and manage sandboxed JavaScript tools with a Monaco editor and a model-driven lifecycle.

- [dsh-git-identity](https://github.com/LoserFox/dsh-git-identity) — Pins Git commit authorship to the active environment identity, prioritizing the signed-in GitHub CLI account.

- [dsh-open-in-vscode](https://github.com/FSMargoo/dsh-open-in-vscode) — Open DeepSeek Harness workspace directories in VS Code from the web interface.

- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) — Embeds isolated web page previews in DSH Web for element annotations and visual adjustments that guide source edits.

- [Prompt Studio](https://github.com/Moeblack/dsh-prompt-studio) — Edit user and built-in system-prompt sections with live preview.

### Agent orchestration & automation

- [dsh-evolve](https://github.com/william-jin-cmu/dsh-evolve) — Lets the agent write, hot-mount, and reversibly remove its own cordis plugins mid-session, growing new tools, prompt rules, and event hooks that persist across restarts.

- [mstar-harness](https://github.com/btspoony/mstar-harness) — A skill-driven workflow agent plugin for structured harness-loop engineering.

### Productivity & collaboration

- [deepseek-manners](https://github.com/Moeblack/deepseek-manners) — Appends a thank-you line to every assistant reply.

- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) — A DeepSeek Harness distribution of the Cetus macOS desktop agent: a resident chat companion with global hotkey, screen context, scheduled tasks, and file hand-off.

- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) — Branch-based message editing with reroll, retry, and a version timeline for DeepSeek Harness conversations.

- [dsh-notification](https://github.com/FSMargoo/dsh-notification) — Sends desktop notifications when a DeepSeek Harness turn completes, with outcome and keyword rules.

### Data, research & knowledge

- [context-doctor](https://github.com/dsh-external/context-doctor) — Audits the token cost of instruction chains, skill catalogs, and tool schemas, and detects duplication and conflicts.

- [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) — Lets DeepSeek Harness cite relevant conversation history from Codex and Claude Code.

- [dsh-data-agent](https://github.com/dsh-external/dsh-data-agent) — Helps agents connect to databases and write SQL for data tasks.

- [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) — Adds long-term cross-session memory with Git-branch awareness and background skill evolution.

- [dsh-session-search](https://github.com/dsh-external/dsh-session-search) — Provides full-text search across DSH, Codex, Claude Code, pi, and OpenCode sessions.

### Cloud, DevOps & observability

No entries yet. [Submit the first plugin.](CONTRIBUTING.md)

### AI, design & media

- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) — Connects DeepSeek Harness to OpenPencil so agents can create, edit, preview, and validate interactive, multi-page design canvases.

- [dsh-cc-tui](https://github.com/ccch1mneyyy/dsh-cc-tui) — A Claude Code-style full-screen terminal interface with streaming thought display, rollback controls, and context/TPS indicators.

- [dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) — A switchable QQ2006 skin for the DeepSeek Harness Web UI with a coral-blue theme and retro assets.

- [dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) — A shared sticker catalog serving the Web UI picker, a /sticker command, and an agent send_sticker tool, with two character variants and workflow-reaction stickers.

- [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) — A hand-drawn pixel whale companion for the DSH Web UI that reacts to agent activity.

- [dsh-vision](https://github.com/william-jin-cmu/dsh-vision) — Adds a view_image bridge from text-only DeepSeek models to OpenAI-compatible vision-language models.

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
