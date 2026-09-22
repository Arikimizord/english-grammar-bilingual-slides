# 内容片段编写规范（content/*.py）

本文件是给内容作者（人类或 AI）的唯一权威规范。build.py 会在运行时 `exec` 本目录下所有 `*.py` 片段，
因此片段文件里可以直接使用 `slide()`、`head()`、`mp()`、`N()`、`PILOT` 这些在 build.py 中已定义的名字。
**禁止**在片段文件里 import、定义 slide/head/mp/N、修改 EXTRA_CSS 或任何全局状态。

## 1. 文件契约

```python
# -*- coding: utf-8 -*-
# content/<module-slug>.py —— 内容片段

PILOT["<slide-id-1>"] = slide("<slide-id-1>", "<theme>", "<foot_left>", "<code>", body_html)
# ... 每页一个 PILOT 赋值

NOTES_FRAG = [
    N("<slide-id-1>", "<标题>", "<Part中文名> · <模块中文名>", 2.5, "<目的一句话>", ["talk1", "talk2", "talk3"], "<转场语>"),
    # 每页一条，id 必须与 PILOT 键完全一致
]
```

- 每个片段文件 = 一个模块的 4 页（3 内容页 + 1 练习页）。
- Python 字符串一律用**双引号**（防撇号炸校验器的历史坑）。
- HTML 中的撇号写实体 `&rsquo;`（如 `Don&rsquo;t`）；中文引号直接用「」。
- `NOTES_FRAG` 里的 `talk` 必须 ≥3 条；每条备注必须有 `transition`（有意义的转场语）。

## 2. 助手函数签名

```python
slide(mid, theme, foot_left, code="GRAMMAR", body="")
# theme: "light" 或 "dark"；foot_left: 如 "M02 · 名词的可数与不可数"；code: 如 "M02"

head(kicker, cn_title, en_title, lead=None, xl_style="")
# kicker: 英文短语 + 中文，如 "There Be · 说『有』的句型"
# cn_title: 中文大标题（≤14 个汉字，过长会自动缩字号但尽量短）
# en_title: 英文副标题小字
# 练习页统一加 xl_style="font-size:4.6vw"

mp(label_q, choices, ans)
# mini-p 练习行：题干（含 ___ 空格）、括号里的选项、隐藏答案（✔ <em>...</em> — 解析）
```

## 3. 版式配方（照抄 M03 示例骨架）

内容页 = `head(...)` + 一个 `.sv-cols` 双列容器，每列一张 `.learn-card`（均带 `data-anim`）：

```html
<div class="sv-cols" style="margin-top:1.4vh">
  <div class="col">
    <div class="learn-card" data-anim>
      <div class="lc-t"><span class="cn">卡片中文名</span><span class="en">英文小注</span></div>
      <span class="ex-line">She <span class="tgt">sent</span> me a postcard.<span class="ex-gl">中文注释一行</span></span>
      <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>错误句</em> → ✔ <em>正确句</em>（一句话点破）</div></div>
      + mp("题目 ___ 空格", "选项A / 选项B", "✔ <em>答案</em> — 解析一句话")
    </div>
  </div>
  <div class="col">...第二张卡片...</div>
</div>
```

- 例句中的**目标语法**一律包 `<span class="tgt">…</span>` 或 `<em>…</em>`（衬线斜体加重）。
- 每卡最多一个 `mist`；也可以没有 mist。
- 每卡**必须**有一个 mp() 练习行。

练习页 = `head(..., xl_style="font-size:4.6vw")` + 一个 `.practice` 块（4 道 `.p-q` 题）+ 结尾一个口诀 `mist`：

```html
<div class="practice" data-anim>
  <div class="p-label">题型说明 · Choose the right word</div>
  <div class="p-q"><span class="qnum">1.</span><em>选项 / 选项</em> — 题干 ______（提示）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>答案</em> — 解析</span></div>
  <!-- 4 道 -->
</div>
<div class="mist" style="margin-top:1vh" data-anim>
  <div class="m-label">判定口诀 · Shortcut</div>
  <div class="m-body">一两句口诀。</div>
</div>
```

## 4. 高度预算（最重要！）

画框会在答案**全部展开**的状态下被 overflow:hidden 硬裁。经验法则：
- `ex-gl` 注释、`mist .m-body`、`mp` 答案都控制在**一行**（≤40 个中文字符）。
- 例句 `ex-line` 尽量一行放下（≤55 字符）。
- 每卡结构固定：标题 1 行 + 例句 1-2 行 + mist 1 行 + mini-p 1-2 行。**不要**再往卡片里加别的东西。
- mini-p 题干过长会把 Aha! 按钮挤到第二行，答案展开就会超高——题干 ≤28 字符。

## 5. 双语与文风

- 规则用中文说清楚，术语给英文（可数 countable、所有格 possessive case）。
- 例句全部自创、贴近高职学生生活（校园、兼职、食堂、快递、社团），**不得**复制任何教科书原句。
- 语气与现有页面一致：短句、直给、带点温度（参考「一根梁，还是三根梁。」这种风格，但不必强行金句）。

## 6. 质量自查（提交前）

1. `python -c "compile(open('content/xxx.py',encoding='utf-8').read(),'x','exec')"` 通过。
2. 每页有 data-anim 卡片；每个 PILOT 键在 NOTES_FRAG 有对应 N() 且 id 一致。
3. 页码 foot_left 的模块号与分配表一致（见 §7）。

## 7. 本轮 10 个模块的分配表

| 文件 | 模块 id | code | 分区 | 页面主题（3 内容 + 1 练习） | 内容页主题色序列 |
|---|---|---|---|---|---|
| verbs.py | pos-verbs | M05 | Ⅰ 词法篇 | ①动词的分类(vt/vi/系/助/情态) ②五种基本形式 ③及物不及物与系表 ④练习 | light, dark, light, dark |
| adjectives.py | pos-adjectives | M06 | Ⅰ | ①两种位置(定语/表语) ②多个形容词排序 ③-ed与-ing ④练习 | light, dark, light, dark |
| adverbs.py | pos-adverbs | M07 | Ⅰ | ①五大类 ②-ly拼写规则 ③位置 ④练习 | light, dark, light, dark |
| numerals.py | pos-numerals | M08 | Ⅰ | ①基数词 ②序数词 ③确数约数/年份分数 ④练习 | light, dark, light, dark |
| there-be.py | m4-there-be | M13 | Ⅱ 句法篇 | ①基本句型(就近原则) ②否定与疑问 ③时态变化 ④练习 | dark, light, dark, light |
| nouns.py | m5-nouns | M02 | Ⅰ 词法篇 | ①可数与不可数 ②复数规则 ③所有格与复合名词 ④练习 | light, dark, light, dark |
| articles.py | m6-articles | M03 | Ⅰ | ①a / an(音素判断) ②the 的用法 ③零冠词 ④练习 | dark, light, dark, light |
| pronouns.py | m7-pronouns | M04 | Ⅰ | ①人称代词 ②物主与反身 ③不定代词 ④练习 | light, dark, light, dark |
| sentence-elements.py | m2-sentence-elements | M11 | Ⅱ 句法篇 | ①主语与谓语 ②宾语与表语 ③定语与状语 ④练习 | dark, light, dark, light |
| sentence-types.py | m4-sentence-types | M14 | Ⅱ | ①简单句 ②并列句 ③复合句 ④练习 | dark, light, dark, light |
| reported-speech.py | m14-reported-speech | M21 | Ⅲ 动词系统 | ①陈述句转述 ②人称时间变化 ③疑问句转述 ④练习 | dark, light, dark, light |
| prepositions.py | m24-prepositions | M09 | Ⅰ 词法篇 | ①时间介词 ②地点介词 ③固定搭配 ④练习 | dark, light, dark, light |
| questions.py | m25-questions | M15 | Ⅱ 句法篇 | ①一般疑问句 ②特殊疑问句 ③反意疑问句 ④练习 | light, dark, light, dark |
| punctuation.py | m26-punctuation | M30 | Ⅴ 特殊结构与实战 | ①逗号与句末符号 ②撇号与引号 ③大写规则 ④练习 | dark, light, dark, light |

slide-id 命名：`<模块id去掉m前缀>-<主题>`，如 `m4-therebe-basic`、`m4-therebe-neg`、`m4-therebe-tense`、`m4-therebe-practice`；
`m5-noun-count`、`m5-noun-plural`、`m5-noun-poss`、`m5-noun-practice`；其余类推（articles→m6-art-*，pronouns→m7-pron-*，
elements→m2-elem-*，types→m8-type-*，reported→m14-rep-*，prep→m24-prep-*，questions→m25-ques-*，punct→m26-punct-*）。

练习页 id 一律 `<...>-practice`。
