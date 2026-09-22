# -*- coding: utf-8 -*-
"""Round 9 docs: README (32 modules / 167 slides / new framework) + SPEC.md module table."""
import io, re

# ---------- README ----------
r = open("README.md", encoding="utf-8").read()
r = r.replace("badge/Slides-147-green", "badge/Slides-167-green")
old_f = r[r.index("- **28 个模块"):r.index("\n", r.index("- **28 个模块"))]
new_f = ("- **32 个模块 · 5 大部分（由浅入深的层级框架）/ 32 modules in 5 hierarchical parts**："
         "Ⅰ 词法篇（词性总览 → 名词/冠词/代词/动词/形容词/副词/数词/介词/连词，十大词类全部覆盖）→ "
         "Ⅱ 句法篇（句子成分、五大基本句型、There be、句子的种类、疑问句）→ "
         "Ⅲ 动词系统（时态、情态、被动、非谓语、虚拟、引语）→ "
         "Ⅳ 从句与一致（名词性/定语/状语从句、主谓一致）→ "
         "Ⅴ 特殊结构与实战（比较、倒装、强调、省略、标点、易错点、题型）。")
r = r.replace(old_f, new_f)
open("README.md", "w", encoding="utf-8", newline="").write(r)
print("README updated")

# ---------- SPEC.md ----------
s = open("content/SPEC.md", encoding="utf-8").read()
s = s.replace('如 "M04 · There be 的基本句型"', '如 "M02 · 名词的可数与不可数"').replace("code: 如 \"M04\"", "code: 如 \"M02\"")

# replace the module-assignment table rows wholesale
start = s.index("| there-be.py |")
end = s.index("\n", s.index("| punctuation.py |"))
new_rows = """| verbs.py | pos-verbs | M05 | Ⅰ 词法篇 | ①动词的分类(vt/vi/系/助/情态) ②五种基本形式 ③及物不及物与系表 ④练习 | light, dark, light, dark |
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
| punctuation.py | m26-punctuation | M30 | Ⅴ 特殊结构与实战 | ①逗号与句末符号 ②撇号与引号 ③大写规则 ④练习 | dark, light, dark, light |"""
s = s[:start] + new_rows + s[end:]
open("content/SPEC.md", "w", encoding="utf-8", newline="").write(s)
print("SPEC.md updated")
