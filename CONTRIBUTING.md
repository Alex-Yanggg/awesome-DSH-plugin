# Contributing

Thanks for helping build the DeepSeek Harness plugin ecosystem. This catalog is English-first and offers a Simplified Chinese mirror generated from the same source.

## Before you submit

Please make sure the project:

- is a plugin for DeepSeek Harness, or documents a clear and maintained DeepSeek Harness integration;
- has a stable, public `http` or `https` URL;
- is useful to more than one private deployment;
- has clear installation or usage documentation; and
- is not already listed under another name or URL.

## Add an entry

1. Fork the repository and create a focused branch.
2. Edit [`catalog/plugins.json`](catalog/plugins.json). Do not edit the catalog sections in either README by hand.
3. Use the category that best matches the plugin. If none fit, propose a new bilingual category in the same pull request.
4. Provide a concise, factual description in **both** `en` and `zh-CN`.
5. Generate and validate the pages:

   ```bash
   python scripts/generate_readmes.py
   python scripts/generate_readmes.py --check
   ```

6. Open a pull request using the provided template.

### Entry shape

```json
{
  "name": "Example Plugin",
  "url": "https://github.com/example/deepseek-harness-plugin",
  "category": "developer-tools",
  "description": {
    "en": "One precise sentence describing the capability.",
    "zh-CN": "用一句准确的话说明它提供的能力。"
  },
  "status": "active",
  "source": "community"
}
```

`status` is optional and defaults to `active`; use `beta` or `archived` only when useful context for readers. `source` defaults to `community`; use `official` only for a project published by the service or product owner.

## Editorial style

- Prefer one short sentence over marketing copy, feature lists, or unverified claims.
- Link directly to the project's canonical repository, plugin page, or documentation.
- Keep plugin names as published by their maintainers.
- Do not add tracking parameters, affiliate links, or promotional badges.
- A maintainer may move an entry to a more appropriate category, request clarification, or decline entries that do not meet the catalog rules.

## Reporting an issue

Please open an issue or pull request for dead links, ownership changes, security concerns, or outdated DeepSeek Harness integration guidance.

## 中文说明

中文读者可查看[中文主页](docs/README.zh-CN.md)。提交条目时请同时更新 `en` 与 `zh-CN`；脚本会用同一个数据源生成两个页面，确保内容一致。
