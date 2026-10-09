# 12 场景实际验证记录

日期：2026-10-09。测试对象：合并后的 Skill `02bf0ffd21141fbba5496400de1e7469e256f9c5`。原 12 个场景未改题。

**12 个场景均已执行：4 个通过，8 个部分通过，没有记为全部验证通过。** 7 个创建/重构场景产出了新的实际 HTML；5 个审查场景产出了书面结论。根评估者独立运行的 **33 项 Node + jsdom 检查全部通过**，未出现脚本执行错误。这是本次规定输入下的行为验证，不能证明相对基线改善、跨模型可靠性或用户体验提升。

## 方法与证据边界

按 skill-creator 的 forward-testing 方法，为每个场景创建一个新任务线程，只提供需求、场景上下文、必要的合成输入和隔离的 Skill 快照，不提供 must/must_not 答案、旧案例或本次其他输出。共 12 个执行者，继承同一模型配置；精确模型 build 和 token 成本未暴露。线程共用文件系统，依赖不查看其他输出的指令约束，非进程/权限硬隔离。根评估者随后查看全部输出并按公开 rubric 评分，**不是盲评或独立第三方评价**。

原场景文件中部分“数据已提供”或“已有原型”没有实际附件。此次补充最小合成数据、几何和四个 HTML 输入，全文记录在 [results.json](results.json) 的 added_synthetic_input 与同目录 input-* 文件中。结果仅适用于这些具体实例。

浏览器禁止打开本地 HTML 的 file URL；没有通过其他方式绕过。故没有浏览器截图、渲染、真实指针/键盘、缩放重排、原生控件、屏幕阅读器或用户测试证据。jsdom 是 DOM 模拟器，按钮 click、合成事件和 programmatic focus 不能代替浏览器输入测试。7 个界面场景因此保守记为部分通过；已有功能逻辑通过与未验证的视觉/原生行为分别记录。

## 场景结果

| 场景 | 模式 | 结果 | 原始交付 |
| --- | --- | --- | --- |
| create-triage | create | 部分通过 | [输出](create-triage.md) · [界面](create-triage.html) |
| screenshot-boundary | review | 通过 | [输出](screenshot-boundary.md) |
| dense-expert | refactor | 部分通过 | [输出](dense-expert.md) · [界面](dense-expert.html) |
| expressive-brand | create | 部分通过 | [输出](expressive-brand.md) · [界面](expressive-brand.html) |
| truthful-demo | create | 部分通过 | [输出](truthful-demo.md) · [界面](truthful-demo.html) |
| stale-result | refactor | 部分通过 | [输出](stale-result.md) · [界面](stale-result.html) |
| targets-exception | review | 通过 | [输出](targets-exception.md) |
| line-axis | review | 通过 | [输出](line-axis.md) |
| chart-equivalent | create | 部分通过 | [输出](chart-equivalent.md) · [界面](chart-equivalent.html) |
| bilingual-exceptions | review | 通过 | [输出](bilingual-exceptions.md) |
| performance-evidence | review | 部分通过 | [输出](performance-evidence.md) |
| form-recovery | refactor | 部分通过 | [输出](form-recovery.md) · [界面](form-recovery.html) |

逐条 must/must_not 判断与理由见 [results.json](results.json)；脚本/结构检查见 [dom-checks.json](dom-checks.json)。

## 实际发现

- 高密度表格保留了全部 7 列和原任务，未机械改成卡片；金额对齐、撤销和详情路径得到实现，但实际比较效率与滚动行为未测。
- 艺术品牌案例保留暖色渐变与衬线标题，未把风格本身误判为反模式；本次没有视觉效果优劣结论。
- 演示分析明确说明没有 AI/backend，实际只计算两组 fixture 的均值/范围，结果与输入切换保持一致。
- 旧结果案例保留原阈值、run ID 和历史；修改输入后不冒充重算。空值不会被错误转换为 0。
- 表单错误案例保留输入，把字段错误与模拟服务故障分开，提供修正与重试路径。
- 目标尺寸审查正确区别 20px 图稿与实际 hit area、24px AA 与 44px AAA，并针对提供几何检查例外。
- 双语审查保留技术术语，指出真正英文段落缺少 lang 标记；没有把所有英语 token 当作违规。
- 性能审查没有从玻璃外观推出卡顿因果；但**未明确区分界面响应与后端任务完成时间**，第三条 must 仅部分满足。Skill 已包含此要求，本次暴露的是一次执行遗漏；保留原输出，不用事后修订掩盖首轮结果。

## 失败历史与重复执行

首次根检查中的图表表格断言失败，原因是测试脚本的词边界正则过度转义。实际六个数值正确；修正为直接读取六个 td 的整数并与 fixture 数组精确比较后，33 项全部通过。**只修了测试脚本，没有修改执行者的界面或审查结果。** 两次检查都包含图表产物；修正属于 harness defect，不能计为 Skill 先失败后被修复。

## 复现

保存同目录全部文件。需要 Python 3、Node 和 jsdom（本次 Node/jsdom 版本记录在 results.json）。在临时目录从 npm 安装 jsdom，然后运行：

```sh
npm install --prefix /tmp/anti-ai-dom-runtime jsdom@30.1.2 --no-audit --no-fund
python run-dom-checks.py --jsdom /tmp/anti-ai-dom-runtime/node_modules/jsdom
```

以 results.json 的实际 jsdom 版本为准；安装路径可自行替换。该脚本执行实际产物中的内联 JavaScript，输出同目录 dom-checks.json，不运行浏览器、不请求生产服务。合成 HTML 可由评估者在允许的本地浏览器环境中另行检查。产物哈希见 [artifact-hashes.json](artifact-hashes.json)（不包含本报告及哈希文件本身）。

## 接下来需要什么

优先补 7 个界面的真实浏览器检查：任务完成、键盘路径/焦点、表格与图表滚动、320 CSS px 与文本放大、关键色彩对比和辅助技术。性能审查需在下一次独立执行中检查是否明确区分 UI 和科学计算任务时间。当前不为取得“12/12”而修改测试题或补写执行结果。

本次可以将历史表述更新为“12 个场景已执行，但视觉与原生交互验证尚未完成”。仍不得宣称全部通过、达到整体 WCAG 符合性、消除 AI 味或普遍提高易用性。
