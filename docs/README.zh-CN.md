# Awesome DeepSeek Harness Plugins

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![欢迎贡献](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](../CONTRIBUTING.md)

> 面向 DeepSeek Harness（DSH）的社区精选、厂商中立 Plugin 索引——覆盖开发工具、数据工作流、媒体、运维与日常生活等场景。

**语言：** [English](../README.md) | 简体中文

DeepSeek Harness Plugin 能让智能体连接工具、服务、设备和可复用的工作流。本索引的范围刻意保持开放：只要它能赋予智能体有价值的现实能力，就值得被收录。

## 目录

- [快速开始](#快速开始)
- [Plugin 索引](#plugin-索引)
  - [开发工具](#开发工具)
  - [智能体编排与自动化](#智能体编排与自动化)
  - [效率与协作](#效率与协作)
  - [数据、研究与知识](#数据研究与知识)
  - [云、DevOps 与可观测性](#云devops-与可观测性)
  - [AI、设计与媒体](#ai设计与媒体)
  - [商业、金融与电商](#商业金融与电商)
  - [生活、设备与物理世界](#生活设备与物理世界)
- [提交 Plugin](#提交-plugin)
- [索引规则](#索引规则)
- [许可证](#许可证)

## 快速开始

1. 在下方选择分类，打开目标 Plugin 的仓库或市场页面。
2. 按该 Plugin 的说明完成 DeepSeek Harness 安装与配置。
3. 如有要求，重启或重新加载 DeepSeek Harness。

> 本索引链接到第三方项目。安装前，请自行检查源码、权限范围及数据处理政策。

## Plugin 索引

<!-- CATALOG:START -->
### 开发工具

- [dsh-at-file](https://github.com/FSMargoo/dsh-at-file) — 提供 Codex 风格的 @file 引用，可搜索工作区文件并将内容附加到提示词。

- [dsh-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) — 为 DSH 提供完整的侧边栏工作台——资源管理器、编辑预览、终端、Git 面板、内嵌浏览器，并通过服务 API 支持第三方注册 Tab 和文件预览器。

- [dsh-custom-tool](https://github.com/FSMargoo/dsh-custom-tool) — 通过 Monaco 编辑器及模型驱动的生命周期创建和管理沙箱化 JavaScript 工具。

- [dsh-open-in-vscode](https://github.com/FSMargoo/dsh-open-in-vscode) — 可从 DeepSeek Harness Web 界面直接在 VS Code 中打开工作区目录。

### 智能体编排与自动化

- [mstar-harness](https://github.com/btspoony/mstar-harness) — 面向结构化 Harness 循环工程的技能驱动工作流智能体 Plugin。

### 效率与协作

- [dsh-notification](https://github.com/FSMargoo/dsh-notification) — 在 DeepSeek Harness 回合完成时发送桌面通知，并支持按结果和关键词制定规则。

### 数据、研究与知识

暂未收录。欢迎[提交第一个 Plugin](../CONTRIBUTING.md)。

### 云、DevOps 与可观测性

暂未收录。欢迎[提交第一个 Plugin](../CONTRIBUTING.md)。

### AI、设计与媒体

- [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) — 为 DSH Web UI 提供会随智能体活动作出反应的手绘像素鲸鱼伙伴。

- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) — 提供图像问答、长截图 OCR、UI 还原、视觉定位、像素差异和 Artifacts 能力。

### 商业、金融与电商

暂未收录。欢迎[提交第一个 Plugin](../CONTRIBUTING.md)。

### 生活、设备与物理世界

暂未收录。欢迎[提交第一个 Plugin](../CONTRIBUTING.md)。
<!-- CATALOG:END -->

## 提交 Plugin

欢迎贡献。请先阅读[贡献指南](../CONTRIBUTING.md)，然后在 [`catalog/plugins.json`](../catalog/plugins.json) 中添加中英双语条目，并执行：

```bash
python scripts/generate_readmes.py
python scripts/generate_readmes.py --check
```

第一条命令会重新生成两种语言的页面；第二条命令会验证提交的页面与索引源数据一致。

## 索引规则

- Plugin 应与 DeepSeek Harness 直接相关，或提供清晰的安装/集成说明。
- 每个条目必须提供稳定的公开链接、简洁准确的描述，以及英文和简体中文文案。
- 请保持厂商中立、实用且避免重复收录。
- 不收录密钥、联盟营销链接、未说明背景的废弃分叉，以及主要用于恶意软件、凭据窃取或违规自动化的项目。

## 许可证

本仓库以 [MIT License](../LICENSE) 发布。
