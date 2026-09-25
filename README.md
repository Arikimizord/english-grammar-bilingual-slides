# 高校英语语法双语课件 · Bilingual English Grammar Courseware

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Template: AGPL-3.0](https://img.shields.io/badge/Template-AGPL--3.0-blue.svg)](./template/README.md)
[![Slides](https://img.shields.io/badge/Slides-167-green.svg)](./index.html)
[![Platforms](https://img.shields.io/badge/Platforms-phone%20%7C%20tablet%20%7C%20desktop-blueviolet.svg)](./index.html)

一套**单文件、零依赖、免费开源**的高校英语语法双语教学课件（网页 PPT）。面向英语基础较弱的中国学生（高职 / 专升本 / 大学基础段），中文讲规则、英文给例句，教室投影后排也能看清。

A single-file, zero-dependency, open-source **bilingual (Chinese–English) English-grammar courseware** as a web slide deck. Built for Chinese college students with weaker English foundations: rules explained in Chinese, examples in English, classroom-projector friendly.

> **作者 / Author: Adam Wang（英语教师 / English teacher）· arikimizord@163.com**

---

## ✨ 特性 / Features

- **32 个模块 · 5 大部分（由浅入深的层级框架）/ 32 modules in 5 hierarchical parts**：Ⅰ 词法篇（词性总览 → 名词/冠词/代词/动词/形容词/副词/数词/介词/连词，十大词类全部覆盖）→ Ⅱ 句法篇（句子成分、五大基本句型、There be、句子的种类、疑问句）→ Ⅲ 动词系统（时态、情态、被动、非谓语、虚拟、引语）→ Ⅳ 从句与一致（名词性/定语/状语从句、主谓一致）→ Ⅴ 特殊结构与实战（比较、倒装、强调、省略、标点、易错点、题型）。
- **每个知识点一个配方 / one recipe per point**：规则（中英）＋ 双语例句 ＋「常见错误」提示框 ＋ 随堂练习。
- **Aha! 点击揭晓 / click-to-reveal practice**：每个练习先让学生想，点击按钮才显示答案与解析。
- **随时跳转 / jump anywhere**：首页 ＋ 目录页 ＋ 左上角常驻「⌂ 首页 / ☰ 目录」按钮，任何页面一键返回；每个模块可独立开讲，适合多课时拆分使用。
- **演讲者模式 / presenter mode**：按 `P` 打开（左预览 + 右备注，备注可现场编辑并自动保存）；`ESC` 总览、`B/W` 黑白屏、`F` 冻结、`L/C` 激光笔与圈选。
- **大字号投影友好 / projector-friendly**：字号同时按视口宽高自适应封顶，从超宽屏到笔记本浏览器实测无文字裁切。
- **多平台适配 / multi-platform**：安卓 / iOS 手机、各平台平板、桌面端全适配——窄屏自动进入「滚动阅读模式」（单列网格、页面内可上下滚动、刘海屏安全区、`100dvh` 地址栏修正），并提供触屏翻页悬浮球；桌面端布局不受影响。
- **轻量 · 零外部依赖 / lightweight, zero external dependencies**：仍是单文件 HTML（约 570KB），不引用任何 CDN 脚本；动效由原生 WAAPI 驱动（离线可用），网页字体异步加载、被墙/离线自动回退系统字体；手机与旧电脑自动降低动画与渲染开销（WebGL 背景按设备能力门控）。

## 🚀 使用 / Usage

无需安装任何东西：**直接下载 [`index.html`](./index.html)，双击用浏览器打开即可上课。**（仓库根目录即最终课件，可直接部署到 EdgeOne Pages / GitHub Pages 等静态托管；手机浏览器同样可以直接打开）

No installation needed: just download `index.html` and open it in a browser — desktop or phone.

| 操作 / Action | 方式 / How |
|---|---|
| 翻页 / navigate | `←` `→` / 滚轮 / 触屏滑动 / 底部圆点；手机用右下角悬浮球 `‹` `›` |
| 回首页·目录 / home·contents | 左上角 `⌂ 首页` `☰ 目录` |
| 总览选页 / overview | `ESC`；手机用悬浮球 `☰` |
| 演讲者模式 / presenter mode | 右下角 `P`（备注可编辑、自动保存 / notes editable & autosaved） |
| 黑屏·白屏 / blackout | `B` / `W` |
| 手机阅读 / mobile reading | 窄屏自动进入滚动阅读模式，每页内可上下滑动；再横向滑动即翻页 |

## 🛠 本地重建 / Rebuild locally

课件由 `build.py` 从内容片段组装而成（页码、目录、备注自动重算）：

```bash
git clone https://github.com/Arikimizord/english-grammar-bilingual-slides.git
cd english-grammar-bilingual-slides
python build.py        # 需要 Python 3.8+，无第三方依赖 / Python 3.8+, no third-party deps
```

- 修改内容：编辑 `content/*.py`（每个模块一个文件）或 `build.py` 内置页面，重跑 `python build.py` 即可。
- 内容规范（版式配方、高度预算、命名规则）：见 [`content/SPEC.md`](./content/SPEC.md)。
- 模板可被环境变量覆盖：`GRAMMAR_TEMPLATE`（模板路径）、`GRAMMAR_OUT`（输出目录）、`GUIZANG_SKILL`（本地技能安装路径）。

## 📁 目录结构 / Repository layout

```
├── index.html              ← 最终课件（双击即用，可在仓库根目录直接静态部署）/ the deck (self-contained)
├── build.py                ← 组装脚本 / assembler
├── content/                ← 模块内容片段（每模块一文件）/ module content fragments
│   └── SPEC.md             ← 内容编写规范 / authoring spec
├── template/template.html  ← 演示模板（AGPL-3.0，未修改）/ presentation template, unmodified
├── tools/                  ← 探针与补丁脚本 / probe & patch scripts
├── docs/                   ← 项目过程记录 / project history (中文)
└── LICENSE                 ← CC BY-SA 4.0（教学内容）/ content license
```

## 🤝 参与优化 / Contributing

欢迎提 Issue / PR：新的知识点模块、例句改进、错别字与讲解纠错、深色投影对比度……都很好。
新增一个模块的最小路径：复制 `content/` 下任一片段作骨架 → 按 `SPEC.md` 写 4 页 → 在 `build.py` 的 `MODULES` 与 `pilot_for()` 各加一行 → 重跑 `build.py`。

Issues and PRs welcome: new grammar modules, better example sentences, typo fixes, readability tweaks. The minimal path to add a module is documented above.

## 📄 许可 / License

- **教学内容与例句**（`content/`、`build.py` 内置页面、README）：[**CC BY-SA 4.0**](./LICENSE) —— 署名 Adam Wang，以相同方式共享。
  Teaching content & example sentences: CC BY-SA 4.0, attribution "Adam Wang", share-alike.
- **演示模板**（`template/template.html`）：基于 [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) 的未修改副本，遵循 **AGPL-3.0**，详见 [`template/README.md`](./template/README.md)。

## 🙏 致谢 / Acknowledgements

- 演示引擎与视觉系统：[guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)（AGPL-3.0）
- 知识点主题覆盖参考了《The Grammar Guide》（Pearson ERPI, 2013）的目录结构——仅作主题清单参考，本仓库全部讲解与例句均为原创。
- Topic coverage was cross-checked against the table of contents of *The Grammar Guide* (Pearson ERPI, 2013) — used as a topic checklist only; all explanations and examples here are original.
