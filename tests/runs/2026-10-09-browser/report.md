# 12 场景验证收尾记录

日期：2026-10-09。基于 main 合并提交 `fcb85c2`，补齐上一轮 7 个界面的真实浏览器检查和性能审查复测。原始 [4 pass / 8 partial 记录](../2026-10-09/report.md) 不改写。

**本轮规定的验收范围已收尾：7 个界面经真实浏览器检查与必要修复后通过，性能审查流程修改后独立复测通过，前轮 4 个审查通过结论继续保留。合计 12 个场景达到各自的本轮验收条件。** 这包括人工修复后的交付验收，不是“Skill 首次生成 12/12 成功”或整体 WCAG 认证。

最终 [浏览器结果](final-browser-results.json) 包含 **75 条通过的检查/测量记录、0 个脚本异常、0 个外部请求**。21 张最终渲染截图覆盖 7 个界面的桌面、320px 和文本放大状态，均已查看；原始截图也保留。

## 验收范围与方法

- 真实 headless Chromium `153.0.8010.0`、Playwright `1.62.1`、axe Playwright `4.13.0`，Node `24.19.0`；使用 npm 的 `@sparticuz/chromium@153.0.0` 二进制。默认 Playwright 下载在此环境收到无效压缩包；改从 npm 官方 registry 获取浏览器包，没有用 DOM 模拟器冒充浏览器。
- 桌面 1280×900、窄屏 320×900 / 640×900，触摸模拟 375×812。通过 Playwright 输入实际 Tab、Enter、Space、Escape、ArrowRight，及点击、tap、输入和原生 select 选择；不是手工 dispatchEvent。
- 完成主任务及关键恢复路径：claim/release/empty；resolve/undo/detail/escape；注册校验/preview/edit/clear；fixture 切换/均值/范围；旧结果/rerun/空值/历史；无需 hover 的精确值；表单校验/服务故障/retry。
- 检查焦点指示与恢复、键盘滚动、实际 hit area、页面级横向溢出、axe 可自动判断的 WCAG A/AA 项、可访问名称/角色/状态快照、渐变与 SVG 文本对比，以及实际渲染中的布局和图表编码。
- 文本放大使用 **computed font size ×2** 的测试注入，viewport 为 640px；SVG 保持二维图形，精确值表格文字被放大。这是明确的文字压力测试，不能说成操作系统字体设置或浏览器菜单 zoom。320px 测试是实际 CSS viewport。
- 二维比较表与图表在独立容器内滚动，外围文本重排；不通过删除列、数据或改成卡片“消除”溢出。依据：[W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)。自动扫描不代替全部人工评估，见 [Deque](https://www.deque.com/blog/how-accessibility-programs-benefit-from-both-manual-and-automated-testing/)。

## 12 场景结果

| 场景 | 本轮验收 | 证据与处理 |
| --- | --- | --- |
| create-triage | 通过，修复后 | [界面](create-triage.html)：claim/release/empty、焦点恢复、键盘横向滚动、窄屏和触摸；补滚动区域焦点入口，窄屏筛选避免文字截断，队列 totals 增加 group 角色。 |
| screenshot-boundary | 前轮通过，保留 | [原始审查](../2026-10-09/screenshot-boundary.md)；没有把截图描述冒充行为或标准实测。 |
| dense-expert | 通过 | [界面](dense-expert.html)：保留 7 列/2 行，resolve/undo、明细 Escape/焦点返回，键盘滚动、触摸。 |
| expressive-brand | 通过 | [界面](expressive-brand.html)：保留渐变/衬线品牌，事件信息、真实校验与本地 preview/edit/clear；没有预约/邮件能力假称。 |
| truthful-demo | 通过 | [界面](truthful-demo.html)：SYN-01 mean 4 / range 4、SYN-02 mean 3 / range 0，输入变化清旧结果，动作和结果说明没有 AI/backend。 |
| stale-result | 通过 | [界面](stale-result.html)：修改后不重算，Enter rerun、空值拒绝、原 run 保留、0 值匹配范围。 |
| targets-exception | 前轮通过，保留 | [原始审查](../2026-10-09/targets-exception.md)；实际 geometry 与适用例外，24px AA / 44px AAA 分开。 |
| line-axis | 前轮通过，保留 | [原始审查](../2026-10-09/line-axis.md)；没有把 bar baseline 规则套给 line trend。 |
| chart-equivalent | 通过，修复后 | [界面](chart-equivalent.html)：真实渲染发现 axis 默认黑色填充；改为 fill:none，保留 6 个精确值、可访问描述与非 hover 路径，键盘滚动。 |
| bilingual-exceptions | 前轮通过，保留 | [原始审查](../2026-10-09/bilingual-exceptions.md)；保留术语，区分真正英文段落标记。 |
| performance-evidence | 通过，流程修改后复测 | [修订前](performance-before-workflow-fix.md)仍漏要点；[修改后新线程](performance-after-workflow-fix.md)区分实验室/真实用户及 UI 反馈/后台完成，保持因果未验证。 |
| form-recovery | 通过 | [界面](form-recovery.html)：保留输入、字段关联错误、服务故障单独反馈与 retry、成功不假称已上传。 |

## 实际缺陷与修复历史

1. [首轮 57 项记录](first-browser-results.json)出现分诊滚动区域不能 Tab 到达的真实失败；修复 tabindex、region 名称、焦点样式和滚动提示。原 DOM 检查通过不代表此项通过。
2. 首轮历史表滚动测试使用不存在的 `.history-scroll`，是 harness 假设错误。历史表在 320px 已重排，未发生页面溢出；移除不存在的滚动断言，保留真实 reflow、历史与任务测试。没有为测试凭空加容器。
3. [中间 74 项记录](interim-browser-results.json)自动断言均通过，但人工截图检查发现 chart 的开放 axis 路径默认 fill 形成黑色三角形；修复 axis/grid fill，补真实 computed fill 断言。保留前轮图像，不掩盖自动检查漏检。
4. 同时发现窄屏 select 的 All severities / All owners 标签被截断；改成按文字宽度换行的筛选布局，最终截图标签完整。
5. axe 对渐变/SVG 对比标为 incomplete，不能直接算自动通过。按实际 foreground 和背景计算补证据：品牌正文对三处渐变 stop 的最低比为 6.82:1（各 RGB 通道沿此渐变单调减小）；图表文字与白底 14.22:1。轴已明确无填充。箭头仅装饰且 aria-hidden，无信息只靠箭头传达。对比记录与 incomplete 原记录都保留。
6. performance 原参考已有要点但入口没有确保加载。review 工作流明确要求性能问题先加载该参考并区分两类证据/时间；新线程只得到相同原题和隔离 skill，未收到 must/must_not、失败诊断或预期答案。精确模型 build 未暴露，线程文件系统隔离仍靠指令，非盲评。
7. verify 工作流加入键盘滚动和 stroke-only SVG 实际渲染要求。包校验仅允许 tests/runs 内有合法结构、CRC 且无额外 metadata/trailing content 的 PNG，以及指定文本 browser harness；不普遍放开任意二进制。新增有效 PNG、破损、尾随内容与目录边界回归测试。

## 截图与可访问快照

文件命名 `final-<场景>-desktop.png`、`final-<场景>-320.png`、`final-<场景>-text200.png`；`first-*` 是修复前证据。每个 `final-<场景>-accessibility.yml` 是 Chromium/Playwright 的可访问结构快照，**不是实际屏幕阅读器播报测试**。

例：[分诊窄屏](final-create-triage-320.png)、[图表最终桌面](final-chart-equivalent-desktop.png)、[图表修复前](first-chart-equivalent-desktop.png)、[表单文字放大](final-form-recovery-text200.png)。全部文件校验值见 [artifact-hashes.json](artifact-hashes.json)。

## 复现

从 npm 安装 `playwright@1.62.1` 与 `@axe-core/playwright@4.13.0`，安装匹配的 Chromium 或指定已安装的 Chromium 可执行文件。保存本目录全部文件，在临时 runtime 中执行（目录可替换）：

```sh
npm install --prefix /tmp/anti-ai-browser-runtime playwright@1.62.1 @axe-core/playwright@4.13.0 --no-audit --no-fund
NODE_PATH=/tmp/anti-ai-browser-runtime/node_modules CHROMIUM_EXECUTABLE=/absolute/path/to/chromium EVIDENCE_LABEL=reproduced node run-browser-checks.cjs
```

脚本只执行同目录明确标注的合成 HTML，保存检查 JSON、21 张 PNG 和 7 个可访问快照。首轮/中间与最终检查的新增数量不同，不能把它们当作同一组固定断言的质量百分比。

## 完成范围

之前提出的本轮浏览器与性能审查缺口已完成处理，没有已发现却未修复的本轮任务故障。不再以泛泛“再验证”作为下一项待办。执行环境是单一 Chromium、合成数据与 agent 评估；没有声称真实设备触控、NVDA/VoiceOver 播报、跨浏览器、真实用户研究、生产性能、视觉品味一致性或整体 WCAG 符合性。它们是结论边界，不是把本轮原题改成无限研究项目。
