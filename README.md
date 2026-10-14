# Agent Upstream License (AUL)

**Fork freely. Improve openly. Leave when you choose.**

The **Agent Upstream License (AUL)** is a custom MIT-inspired software license drafted for projects built with AI and designed for AI agents. While a fork follows a direct upstream, it requires reporting *confirmed upstream issues* and offering *retained improvements* upstream as reviewable pull requests or accepted equivalents. Maintainers can elect to make their project independent, with itself as upstream, without permission from the former upstream.

**Current version: 1.0-draft.1 (15 October 2026).** This is a **public draft**, not the MIT License, not an OSI-approved open-source license, and not legal advice. Required contribution obligations may conflict with conventional open-source licenses and distribution policies. Get a legal review before relying on it in production.

[**License text (English)**](LICENSE.txt) · [中文许可证](LICENSE.zh-CN.md) · [中文说明](README.zh-CN.md) · [Design decisions](DESIGN-NOTES.md) · [Review scenarios](REVIEW-CASES.md)

## Rules at a glance

1. **MIT-like permissions.** Use, change, redistribute, and sell covered software, retaining license and third-party notices.
2. **Report confirmed upstream defects.** While following another project, send actionable issues to that direct upstream. Existing adequate issues count; duplicate or speculative reports do not.
3. **Offer retained changes upstream.** Open a pull request or accepted equivalent patch. No merge, perpetual maintenance, or repeated rejected submissions are required.
4. **Independence is a right.** An authorized maintainer can point upstream to their own actual fork. Future changes no longer have to go to the former upstream. Earlier obligations are not erased.
5. **Agents act only with authority.** An AI agent with the needed tools, access, safe channel and explicit publication authorization should submit during its work session; otherwise it must report the precise blocker. Never leak secrets or treat a license as an access grant.

This summary is not the license. Read [LICENSE.txt](LICENSE.txt) for exact definitions, conditions and exceptions.

## Adopt AUL for your project

- Add a copy of [LICENSE.txt](LICENSE.txt) to your project and replace the copyright placeholders **only if you own or have permission to license the covered material**. Keep separate licenses on third-party files and existing rights notices.
- Select a real direct upstream or your own repository in `UPSTREAM.toml`, using [follow](examples/UPSTREAM.follow.toml) or [independent](examples/UPSTREAM.independent.toml). Do not copy example URLs as actual targets.
- Merge [AGENTS.example.md](AGENTS.example.md) into existing Agent instructions; do not overwrite project-specific safety rules.
- Use `LicenseRef-AUL-1.0-draft.1` as a custom SPDX identifier where supported. For Rust packages, use `license-file = "LICENSE.txt"` if the license is the actual grant. Do not label the same material `MIT OR AUL` when the intention is to require AUL conditions.
- Existing MIT releases remain usable under their original grant. AUL cannot retroactively restrict them.

## Why this draft exists

AUL makes the preferred upstream feedback loop legible to both people and development agents, without forcing a project to remain connected to its original author forever. It defines concrete reporting and contribution duties, a practical independence election, safe disclosure exceptions, and a non-spam approach to upstream collaboration.

This repository includes [agent-facing guidance](AGENTS.example.md), [implementation notes](DESIGN-NOTES.md), [24 review cases](REVIEW-CASES.md) and [references](SOURCES.md).

## Status and feedback

**Status: draft.** License enforceability, multi-author consent, third-party compatibility, required private-change disclosures, jurisdiction-specific effects, and the exact OSI implications remain review topics. Please [open an issue](https://github.com/LIghtJUNction/AUL/issues) with a concrete case or propose improved wording in a pull request. Security-sensitive information must use an appropriate private route.

Copyright (c) 2026 LIghtJUNction for original documentation contributions, subject to the rights of other contributors. The reusable license text is governed by its [Section 15](LICENSE.txt).
