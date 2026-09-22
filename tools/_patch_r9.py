# -*- coding: utf-8 -*-
"""Round 9: restructure MODULES into hierarchy-first framework (32 modules, 5 parts)."""
src = open("build.py", encoding="utf-8").read()

# --- 1) PART labels: hierarchy-first naming ---
old_parts = '''PART1 = ("Ⅰ", "句子基础", "SENTENCE BASICS")
PART2 = ("Ⅱ", "动词系统", "THE VERB SYSTEM")
PART3 = ("Ⅲ", "从句系统", "CLAUSES")
PART4 = ("Ⅳ", "特殊结构", "SPECIAL STRUCTURES")
PART5 = ("Ⅴ", "实战应用", "PRACTICE")'''
new_parts = '''PART1 = ("Ⅰ", "词法篇", "MORPHOLOGY · WORD CLASSES")
PART2 = ("Ⅱ", "句法篇", "SYNTAX")
PART3 = ("Ⅲ", "动词系统", "THE VERB SYSTEM")
PART4 = ("Ⅳ", "从句与一致", "CLAUSES & AGREEMENT")
PART5 = ("Ⅴ", "特殊结构与实战", "ADVANCED & PRACTICE")'''
assert old_parts in src, "PART block not found"
src = src.replace(old_parts, new_parts)

# --- 2) MODULES: 32 entries, 词法 -> 句法 -> 动词系统 -> 从句与一致 -> 特殊结构与实战
start = src.index("MODULES = [")
end = src.index("]", src.index('("m20-exam-types"')) + 1
new_modules = '''MODULES = [
    # ---- Part Ⅰ 词法篇:十大词类(词性总览是上位概念,统领 M02–M10) ----
    ("m1-parts-of-speech",     "M01", "词性总览",     "Parts of Speech",             PART1, "hero dark",  "十大词类，一张地图。"),
    ("m5-nouns",               "M02", "名词",        "Nouns",                       PART1, "hero light", "可不可数，差别很大。"),
    ("m6-articles",            "M03", "冠词",        "Articles",                    PART1, "hero dark",  "小小 a / the，大大讲究。"),
    ("m7-pronouns",            "M04", "代词",        "Pronouns",                    PART1, "hero light", "替名词出场的人。"),
    ("pos-verbs",              "M05", "动词",        "Verbs",                       PART1, "hero dark",  "句子的心脏，五副面孔。"),
    ("pos-adjectives",         "M06", "形容词",       "Adjectives",                  PART1, "hero light", "给名词上色的人。"),
    ("pos-adverbs",            "M07", "副词",        "Adverbs",                     PART1, "hero dark",  "修饰动词与形容词。"),
    ("pos-numerals",           "M08", "数词",        "Numerals",                    PART1, "hero light", "数得清，才算数得明白。"),
    ("m24-prepositions",       "M09", "介词",        "Prepositions",                PART1, "hero dark",  "小词定乾坤。"),
    ("m18-conjunctions",       "M10", "连词",        "Conjunctions",                PART1, "hero light", "把词与句粘起来。"),
    # ---- Part Ⅱ 句法篇:词如何组成句子 ----
    ("m2-sentence-elements",   "M11", "句子成分",     "Sentence Elements",           PART2, "hero dark",  "把句子拆成零件。"),
    ("m3-five-patterns",       "M12", "五种基本句型",  "Five Basic Patterns",         PART2, "hero light", "所有长句都能长出。"),
    ("m4-there-be",            "M13", "There be 句型", "There Be Structure",         PART2, "hero dark",  "说「有」，用 there be。"),
    ("m4-sentence-types",      "M14", "句子的种类",   "Simple · Compound · Complex", PART2, "hero light", "一根梁，还是三根梁。"),
    ("m25-questions",          "M15", "疑问句",      "Questions",                   PART2, "hero dark",  "会问，才会交流。"),
    # ---- Part Ⅲ 动词系统 ----
    ("m5-tenses",              "M16", "动词时态",     "The Twelve Tenses",           PART3, "hero light", "时间是动词的刻度。"),
    ("m6-modal-verbs",         "M17", "情态动词",     "Modal Verbs",                 PART3, "hero dark",  "态度与可能性的开关。"),
    ("m7-passive-voice",       "M18", "被动语态",     "Passive Voice",               PART3, "hero light", "谁做，还是谁被做。"),
    ("m8-non-finite-verbs",    "M19", "非谓语动词",   "to do · doing · done",        PART3, "hero dark",  "动词的三个分身。"),
    ("m9-subjunctive",         "M20", "虚拟语气",     "Subjunctive Mood",            PART3, "hero light", "假如的世界。"),
    ("m14-reported-speech",    "M21", "直接与间接引语", "Reported Speech",           PART3, "hero dark",  "把别人的话转个头。"),
    # ---- Part Ⅳ 从句与一致 ----
    ("m10-noun-clauses",       "M22", "名词性从句",   "Noun Clauses",                PART4, "hero light", "把从句整个当名词。"),
    ("m11-attribute-clauses",  "M23", "定语从句",     "Attributive Clauses",         PART4, "hero dark",  "跑到名词后面的形容词。"),
    ("m12-adverbial-clauses",  "M24", "状语从句",     "Adverbial Clauses",           PART4, "hero light", "条件 · 原因 · 让步。"),
    ("m13-agreement",          "M25", "主谓一致",     "Subject-Verb Agreement",      PART4, "hero dark",  "主语和谓语，人数对齐。"),
    # ---- Part Ⅴ 特殊结构与实战 ----
    ("m14-comparison",         "M26", "比较等级",     "Comparison",                  PART5, "hero light", "谁比谁，更怎么样。"),
    ("m15-inversion",          "M27", "倒装句",      "Inversion",                   PART5, "hero dark",  "倒过来，更有劲。"),
    ("m16-emphasis",           "M28", "强调句",      "Emphasis",                    PART5, "hero light", "把重点抬到台前。"),
    ("m17-ellipsis",           "M29", "省略句",      "Ellipsis",                    PART5, "hero dark",  "能省则省，不碍理解。"),
    ("m26-punctuation",        "M30", "标点与大写",   "Punctuation & Capitalization", PART5, "hero light", "细节见功夫。"),
    ("m19-common-mistakes",    "M31", "高频易错点",   "Common Mistakes",             PART5, "hero dark",  "中国学生的老坑。"),
    ("m20-exam-types",         "M32", "题型速览",     "Exam Question Types",         PART5, "hero light", "考场最爱怎么考。"),
]'''
src = src[:start] + new_modules + src[end + 1:]

# --- 3) pilot_for: register the four new word-class modules
old_pf = '''    "m24-prepositions":    ["m24-prep-time","m24-prep-place","m24-prep-fixed","m24-prep-practice"],'''
new_pf = '''    "pos-verbs":           ["pos-verbs-kinds","pos-verbs-forms","pos-verbs-transitive","pos-verbs-practice"],
    "pos-adjectives":      ["pos-adj-position","pos-adj-order","pos-adj-ed-ing","pos-adj-practice"],
    "pos-adverbs":         ["pos-adv-kinds","pos-adv-formation","pos-adv-position","pos-adv-practice"],
    "pos-numerals":        ["pos-num-cardinal","pos-num-ordinal","pos-num-usage","pos-num-practice"],
    "m24-prepositions":    ["m24-prep-time","m24-prep-place","m24-prep-fixed","m24-prep-practice"],'''
assert old_pf in src, "pilot_for anchor not found"
src = src.replace(old_pf, new_pf)

# --- 4) cover: M01–M32 / 32 模块
src = src.replace("M01–M28 · NN / TOTAL", "M01–M32 · NN / TOTAL")
src = src.replace("28 模块 · M01–M28", "32 模块 · M01–M32")

open("build.py", "w", encoding="utf-8", newline="").write(src)
print("MODULES:", src.count('("m'), "| parts renamed, cover updated")
