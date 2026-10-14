# 参考来源

核查日期：2026 年 10 月 15 日。只使用以下官方来源支持有关现有许可证、标准和工具的说明。AUL 的新条款是本次起草的设计，不是这些来源已经认可的法律结论。

[1] Open Source Initiative — The MIT License
`https://opensource.org/license/mit`
用于核对 MIT 的宽松授权、保留声明条件和免责结构。本包没有把新增义务冒充为原版 MIT。

[2] Open Source Initiative — The Open Source Definition；OSI Approved Licenses
`https://opensource.org/osd`
`https://opensource.org/licenses`
用于说明开源定义与审批状态。未获批准不等于已经得到“不符合定义”的裁决；本包也没有宣称符合。

[3] SPDX — Package information / custom license references；request-new-license
`https://spdx.github.io/spdx-spec/v2.3/package-information/`
`https://github.com/spdx/license-list-XML/blob/main/DOCS/request-new-license.md`
用于确认未收录许可证可以使用 LicenseRef 自定义引用。自定义引用不等于列入 SPDX License List。

[4] Rust — The Cargo Book, The Manifest Format
`https://doc.rust-lang.org/cargo/reference/manifest.html#the-license-and-license-file-fields`
用于非标准许可证的 license-file 配置，以及 AND / OR 的含义。此处没有假设 Cargo 接受任意自定义 license 字符串。

[5] Git — git-remote documentation
`https://git-scm.com/docs/git-remote`
用于 add、set-url 等本地远程设置。未将改本地远程说成修改托管平台的 Fork 归属。

[6] AGENTS.md — project instructions format
`https://agents.md/`
用于选用常见的 Agent 项目指令文件。此来源不证明所有模型都会服从，也不授予发布权限。

[7] Open Source Initiative — Q Public License 1.0
`https://opensource.org/license/QPL-1.0`
对比参考：既有许可证对提供源码和贡献存在不同安排。没有照搬其条款，也不据此断言 AUL 已符合开源定义。

## 命名检索范围

对 Agent Upstream License、Agent Relay License、Forkback License 和 AUL-1.0 做了有限的公开网页名称检索。这不是完整商标检索、平台名额确认或法律清查。推荐名称仍应视为工作名称，不保证全球唯一。

## 起草与验证范围

本包完成文本起草和文件格式检查，没有由律师审定，没有法律执行实测，没有进行 OSI 或 SPDX 申报，也没有为用户创建远程仓库或更改现有项目许可证。