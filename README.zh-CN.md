# Agent Upstream License

**Agent 上游回馈许可证 · AUL 1.0-draft.1**

默认回馈直接上游。允许自主独立。Agent 有工具和授权时，应实际提交，而不是只给建议。

这是依据你的要求编写的完整首版草案，参考 MIT 的授权思路，但重新起草了正文。它不是标准 MIT，不是已获 OSI 批准的许可证，也没有经过执业律师审查。实际执行效力与其他许可证的兼容性，需要按适用法律及项目材料审查。[1][2]

## 名称

正式英文名：Agent Upstream License。
中文名：Agent 上游回馈许可证。
简称：AUL。
首版标识：`LicenseRef-AUL-1.0-draft.1`。
许可证仓库：[LIghtJUNction/AUL](https://github.com/LIghtJUNction/AUL)。

名称中的 Agent 表示主要阅读和执行对象，Upstream 表示回馈方向。它不把最初作者设为永久接收方。本名称是工作名称；有限的网页检索不是商标、域名或仓库名称的全面清查，不保证全球唯一。

## 文件

| 文件 | 用途 |
| --- | --- |
| LICENSE.txt | 完整英文许可正文；发生解释冲突时以此为准 |
| LICENSE.zh-CN.md | 完整中文参考译文 |
| AGENTS.example.md | 可合并到项目 AGENTS.md 的执行规则 |
| examples/UPSTREAM.follow.toml | 跟随外部上游的声明样例 |
| examples/UPSTREAM.independent.toml | 独立分叉的声明样例 |
| examples/CONTRIBUTION-STATUS.json | Agent 提交状态的结构化样例 |
| DESIGN-NOTES.md | 默认选择、配置规则、边界和待审查事项 |
| REVIEW-CASES.md | 规则检查场景；不是法律有效性测试 |
| SOURCES.md | 官方参考资料与核查范围 |

## 核心规则

使用、修改、分发、出售和商业使用均允许，同时必须保留适用的版权和许可证声明。[1]

继续跟随外部上游的分叉，在开发中确认上游缺陷后，必须提交 issue；保留修复、功能、性能、测试或文档改进后，必须提交 PR 或上游认可的等效补丁。可以引用已有报告或已有提交，不要求上游合并。纯粹使用不触发义务；废弃试验不要求提交。

有工具、账户权限、安全目标和发布授权的 Agent，应在本次工作中实际提交。没有这些条件时，应交付具体待办与原因。不得绕过权限，不得泄露私有内容，不得把本地草稿说成已经发出。

项目所有者可以将 `upstream` 指向自己的真实分叉，从此独立。无须旧上游批准、说明理由或通知旧上游。独立后新增工作不必回馈旧上游，也不必给自己发 PR；独立前已产生的义务仍需解决。

**这是默认回馈规则，不是永久强制回馈最初作者的规则。** 允许轻便独立，就不可能保证原项目永远收到全部改进。

## 在项目中采用

只为你有权授权的材料采用本许可证。不要删除继承代码中的 MIT 或其他声明，也不要声称新许可证收回旧版本已经授出的许可。[1]

把 `LICENSE.txt` 放在项目根目录。将其中的 `[YEAR]` 和 `[COPYRIGHT HOLDER(S)]` 替换为实际软件版权声明。不要把整份项目的所有权都无依据地归给一个人。

把中文译文一并保留，方便人类阅读。将 `AGENTS.example.md` 的内容合并到已有 `AGENTS.md`，而不是覆盖项目已有规则。AGENTS.md 是向 Agent 提供项目指令的文件格式，不是自动执行或账户授权机制。[6]

在两个 UPSTREAM 样例中选择适用的一个，替换 `code.example` 示例地址，再保存为 `UPSTREAM.toml`。这些地址不是实际存在的贡献目标。原始项目没有外部来源时，可在 `mode = "independent"` 下把 `repository` 和 `upstream` 都设为自身，并省略 `source_repository`。

已有 upstream 远程时，独立操作示例：

```sh
# 仅由项目所有者授权执行；替换为真实的本分叉地址。
git remote set-url upstream https://code.example/your/project.git
```

没有 upstream 远程时使用：

```sh
git remote add upstream https://code.example/your/project.git
```

命令的对象是本地 Git 远程设置，不是托管平台的 Fork 关系。它不会自动改变 GitHub 的父仓库显示，也不会替你修改旧提交的授权。分发前仍要保存准确的 UPSTREAM.toml，以便接收者读取选择。[5]

## 标记许可证

代码头可采用自定义 SPDX 引用。这不是声称 SPDX 已经收录了 AUL。[3]

```text
SPDX-License-Identifier: LicenseRef-AUL-1.0-draft.1
```

Rust 项目对非标准许可证使用 `license-file`，不要把包标为 `MIT`，也不要假设 Cargo 接受所有自定义 LicenseRef 作为 `license` 字段。[4]

```toml
[package]
# 保留项目原有的 name、version 等字段。
license-file = "LICENSE.txt"
```

不要给同一份自有代码写 `MIT OR LicenseRef-AUL-1.0-draft.1`，否则选择 MIT 的接收者可以不接受 AUL 新增义务。“OR”表示可任选其一，而不是两者都必须遵守。[4]

## 采用前需理解

条款面向 Agent 执行，但履行责任落在实际获得许可的个人或组织上。配置文件不能自行授予发布权限。安全披露优先使用私有渠道；遇到真实障碍，保留待办并交给操作者处理。

草案自行选择了两个 30 日期限：一般提交期限，以及收到实质违约通知后的补救期限。这不是 MIT 的规则。前者不能让有能力且获授权的 Agent 故意把可完成的工作推迟到第 30 天。

“通过 AI 开发，为 AI 设计”写在目的中，而不是写成禁止人类使用的条件。这样保留项目定位，也避免直接加入按使用者或领域排除的条款。[2]

尚未就名称商标、不同国家的执行效力、GPL 等许可证兼容性、强制私有改动回馈的开源定义问题作法律结论。正式广泛采用前，应由熟悉软件许可的律师审查。后续版本不自动替换这一版本。

参考编号对应 SOURCES.md。