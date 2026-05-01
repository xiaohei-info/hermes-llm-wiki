# hermes-llm-wiki

一个面向 Obsidian 的 **LLM 编译式 Wiki 方法论与 Skill 套件**。

## 它为什么存在

原始笔记不是知识系统。

很多笔记库会不断积累剪藏、草稿、研究片段和临时判断，但这些内容不会自动变成一个可持续维护、可复用、可导航的知识层。Agent 如果只是不断“总结”，反而会制造更多重复内容和结构噪声。

`hermes-llm-wiki` 的目标是提供一套更稳的工作模型：

- `Inbox/` 放原始材料
- `_wiki/` 放编译后的 durable knowledge
- 把 agent 当作编译器 / 编辑器 / curator
- 强调 selective writeback，而不是自动膨胀

## 核心理念

- **原始材料不等于编译知识。** `Inbox/` 与 `_wiki/` 职责必须分离。
- **选择性编译。** 不是每个输入都值得生成 concept / synthesis / question 页面。
- **保留来源链路。** durable 页面应尽量能追溯回 source note 或 source page。
- **查询时 wiki-first。** 先读 `_wiki/`，只有不够时才回看原始材料。
- **没有验证，就不算完成。** 合格 ingest 必须有 canonical placement、导航更新和回读验证。
- **维护本身就是系统的一部分。** duplicate / orphan / stale / backlog 巡检不能缺位。

## 仓库包含什么

### 方法论
- Obsidian compiled wiki 的工作模型
- source space 与 compiled layer 的分层约束
- query / ingest / lint / writeback 规则

### Skills
- `karpathy-llm-wiki-obsidian` —— 方法与落地设计
- `obsidian-inbox-to-wiki-ingest` —— `Inbox/ -> _wiki/` 编译执行
- `obsidian-wiki-lint-triage` —— `_wiki/` 巡检与维护

### 模板
- `_wiki` 骨架
- page type 模板
- triage / lint / digest 的 cron prompt 模板

### 落地文档
- host-neutral implementation guide
- Hermes 集成说明
- generic agent 集成说明

## 它不是什么

它**不是**：

- Obsidian 插件
- 向量数据库方案
- 图谱引擎
- 通用 RAG 框架
- 全自动后台 wiki 服务
- “把所有笔记都自动编译”的流水线

它的价值主要在于：**操作模型、边界和可复用 skill surface**，而不是复杂运行时。

## 快速开始

1. 选择根目录：
   - `INBOX_ROOT`（默认 `Inbox/`）
   - `WIKI_ROOT`（默认 `_wiki/`）
2. 用 `templates/_wiki/` 初始化 `_wiki/` 骨架。
3. 将 `skills/` 下的 3 个 skill 接入你的 agent host。
4. 手动 ingest 一篇真实 source note。
5. 验证：
   - `_wiki/sources/...` 已生成
   - `index.md` 有新的导航项
   - `log.md` 有时间记录
6. 只有当手动流程稳定后，再开启 audit-only lint 或 triage cron。

## 采纳层级

- **Minimum**：文档 + `_wiki` 骨架 + 单次手动 ingest
- **Standard**：3 个 skill + page 模板 + audit-only lint
- **Full**：skills + templates + triage/lint/digest 定时提示接入调度器

详见 [docs/implementation-guide.md](docs/implementation-guide.md)。

## For Agents

推荐阅读顺序：
1. `SOUL.md`
2. `MEMORY.md`
3. `docs/implementation-guide.md`
4. `skills/README.md`

用途：
- `karpathy-llm-wiki-obsidian`：方法论与落地设计
- `obsidian-inbox-to-wiki-ingest`：编译执行
- `obsidian-wiki-lint-triage`：巡检与维护

不要：
- 批量无脑 ingest
- 只为“整齐”自动建页
- 在 audit-only lint 中静默改写 `_wiki/`
- 把 Inbox 原始材料当作 compiled wiki 页面

## License

MIT。
