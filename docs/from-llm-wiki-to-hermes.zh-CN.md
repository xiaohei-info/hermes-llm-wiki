# 从 Karpathy 的 LLM Wiki 到 Hermes 工作流

English version: [from-llm-wiki-to-hermes.md](from-llm-wiki-to-hermes.md)

这篇文档专门解释 `hermes-llm-wiki` 最有特色的那一层翻译工作：

- 原始想法来自 Andrej Karpathy 的 **LLM Wiki** gist
- 这个仓库把那套想法进一步落成 Hermes / Obsidian 可执行的 operating model
- 真正有价值的不只是概念本身，而是让这套概念在真实知识工作流中跑起来所需的操作纪律

## 原始来源

Karpathy 的原始 gist：

- Gist：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Raw：<https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw>

原始模式里最重要的三层是：

1. raw sources
2. 由 LLM 维护的 persistent wiki
3. 用来约束维护行为的 schema / rules layer

以及三个核心操作：

- ingest
- query
- lint

这就是整个项目的概念起点。

## 这个仓库额外做了什么

`hermes-llm-wiki` 不是对原始 gist 的摘要，也不是把原文换个说法再写一遍。

它真正回答的是一个更落地的问题：

> 如果你真的想让一个 Hermes 风格的 agent 在 Obsidian vault 里跑这套模式，那么目录边界、页面类型、操作规则、维护循环到底应该长什么样？

这个仓库给出的答案是一套 **有约束的操作模型**。

## 1. 把三层模式映射进 Hermes + Obsidian

### Karpathy 三层 -> Hermes 映射

| 原始模式 | Hermes / Obsidian 落地 |
|---|---|
| Raw sources | `Inbox/` 作为低摩擦输入层 |
| LLM-maintained wiki | `_wiki/` 作为 compiled knowledge layer |
| Schema / rules | `skills/`、`docs/`、`templates/`、`AGENTS.md`、`SOUL.md`、`MEMORY.md` |

这张映射表本身就是本仓库的重要贡献之一。

### 为什么是 `Inbox/`

raw 层必须允许混乱。

它需要容纳：

- 网页剪藏
- 临时笔记
- 研究碎片
- 未决问题
- 草稿分析
- 设计文档

所以这里的选择是：

- `Inbox/` 优化的是 **收集与保留**
- `_wiki/` 优化的是 **结构、复用与维护**

这个边界非常关键。它能防止一开始就过度结构化，也能避免 compiled layer 退化成 raw archive。

## 2. 把“persistent wiki”变成可操作的 compiled layer

原始 gist 说的是一个由 LLM 维护的持久 wiki。这个仓库把它具体化成一个最小但有立场的结构：

```text
_wiki/
  index.md
  log.md
  overview.md
  sources/
  concepts/
  entities/
  questions/
  syntheses/
  comparisons/
```

这个结构之所以重要，是因为它同时解决了两件事：

1. 给 agent 提供稳定的归档位置
2. 让 wiki 在不依赖重型检索堆栈的情况下也保持可读、可导航

### 为什么 `index.md` 和 `log.md` 是一等公民

这个仓库把 `index.md` 和 `log.md` 当作运行面，而不是装饰文件。

- `index.md` 是 agent 回答问题前应先读的导航图
- `log.md` 是 ingest / lint / maintenance 的 append-only 时间记录

这是把理念变成真实工作流时非常重要的一步。

## 3. 把 ingest 从“总结一下”升级成“编译动作”

很多人谈 LLM Wiki 时，会把 ingest 理解成“读一篇东西然后总结一下”。

这个仓库更强调：

> 一个合格的 ingest，本质上是编译动作，而不是摘要动作。

一个真正的 ingest 通常应至少包含：

1. 读 raw note
2. 创建或更新 `sources/` 页面
3. 判断是否需要联动更新下游 canonical pages
4. 更新 `index.md`
5. 追加 `log.md`
6. 暴露张力、缺口、后续问题

一份 source 合法地触发多个页面联动更新，并不是“过度设计”，而是这套模式最值钱的地方之一。

## 4. 用显式 page-type gates 避免 wiki 失控

原始 gist 对页面组织留了很大自由度。这个仓库刻意把自由度收窄。

这里明确区分：

- `sources/`：单源编译页
- `concepts/`：重复出现、值得复用的抽象概念
- `entities/`：人 / 公司 / 项目 / 产品 / 协议 / 组织等稳定对象
- `questions/`：会反复回来的高价值问题
- `syntheses/`：多 source 汇总后的综合判断
- `comparisons/`：横向比较页

这样做不是为了“分类学的完整感”，而是为了阻止 wiki 滑向这些坏结果：

- raw dump
- 重复页面
- 无依据综合判断
- 被当前聊天上下文驱动的随意建页

## 5. wiki-first 的 query posture

这个仓库还有一个非常明确的设计选择：**不把 raw source 作为默认回答层。**

相反，它要求：

1. 先看 `index.md`
2. 再读相关 compiled pages
3. 优先从 `_wiki/` 回答
4. 只有当 compiled layer 证据不足时，才回看 `Inbox/`

这会让 wiki 从“好像有点用的缓存层”变成真正会复利的知识工件。

## 6. selective writeback，而不是 summary spam

Karpathy 的原始 gist 很强调：好的答案应该写回 wiki。

这个仓库继承了这点，但增加了更严格的门槛：

只有当结果未来还会被复用时，才值得写回。

典型的 writeback 目标：

- recurring question
- durable synthesis
- 对 canonical concept / entity 的实质更新
- 未来还会用到的 structured comparison

这个约束的目的，是防止聊天记录源源不断地污染 wiki。

## 7. 把 lint 定义成知识健康维护

在这个仓库里，lint 指的是：

- duplicate detection
- orphan detection
- stale-page detection
- missing high-value page detection
- 从 `Inbox/` 暴露 backlog
- 检查导航层是否还健康

更重要的是：**lint 默认 audit-only。**

这是一个很实际的落地选择。它表达的意思是：维护应该持续发生，但不应该在默认情况下静默地做破坏性改写。

## 8. 显式的人 / Hermes 分工

原始 LLM Wiki 模式其实暗含了分工，但这个仓库把它明确写了出来。

### 人负责什么

- 决定什么重要
- 选择研究方向
- 判断哪些问题值得优先处理
- 对关键结论拍板

### Hermes 负责什么

- 读材料
- 提取结构
- 一次性更新多个页面
- 维护导航与时间记录
- 暴露冲突、缺口、backlog
- 把高价值答案转成可复用页面

这份分工是本仓库的重要特色，因为它同时防止了两种坏情况：

- 过度自动化
- 把 agent 用得过浅，只当聊天机器人

## 9. 先结构，后自动化

这个仓库还有一个非常鲜明的实施立场：

> 先定义边界和规则，先小规模试跑，再考虑更强自动化。

推荐顺序是：

1. 先定 roots 和 page types
2. 小规模测试 ingest
3. 建立 wiki-first query 和 audit-only lint
4. 只有结构稳定后，再加调度与更强工具

这也是为什么仓库会先提供 prompt templates 和 validation，而不是一开始就把自己包装成一个“自动化知识引擎”。

## 10. 为什么这套设计有特色

很多人都可以重复“LLM Wiki”这个词。

但这个仓库真正有特色的地方在于：它把这个概念落成了一种同时满足以下条件的工作模型：

- 足够轻，适合真实笔记工作流
- 足够明确，别的 agent 能照着 adopt
- 足够结构化，能长期复利
- 足够克制，不容易膨胀成噪音 wiki

一句话总结：

> Karpathy 提供了最初的概念模式，而 `hermes-llm-wiki` 提供的是一种更有 discipline 的 Hermes / Obsidian 落地方式，让这套模式真的能在长期知识维护里跑起来。
