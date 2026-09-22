# -*- coding: utf-8 -*-
"""One-shot patch: renumber modules to 28, cover author, 3-col contents, vh font caps,
content-fragment loader, new pilot_for mappings."""
import re

p = "build.py"
src = open(p, encoding="utf-8").read()
n0 = len(src)

# --- 1) module code remap (old numbering -> new), two-pass to avoid chaining
mapping = {"M04": "M08", "M05": "M09", "M06": "M10", "M07": "M11", "M08": "M12",
           "M09": "M13", "M10": "M15", "M11": "M16", "M12": "M17", "M13": "M18",
           "M14": "M19", "M15": "M20", "M16": "M21", "M17": "M22", "M18": "M23",
           "M19": "M27", "M20": "M28"}
hits = {k: len(re.findall(r"\b" + k + r"\b", src)) for k in mapping}
src = re.sub(r"\bM(0[4-9]|1[0-9]|20)\b",
             lambda m: "@" + mapping["M" + m.group(1)] + "@", src)
src = src.replace("@", "")
print("remap hits:", hits)

# --- 2) MODULES -> 28 modules
new_modules = """MODULES = [
    ("m1-parts-of-speech",     "M01", "词性",        "Parts of Speech",              PART1, "hero dark",  "一个字就是一个身份。"),
    ("m2-sentence-elements",   "M02", "句子成分",     "Sentence Elements",            PART1, "hero light", "把句子拆成零件。"),
    ("m3-five-patterns",       "M03", "五种基本句型",  "Five Basic Patterns",         PART1, "hero dark",  "所有长句都能长出。"),
    ("m4-there-be",            "M04", "There be 句型", "There Be Structure",         PART1, "hero light", "说「有」，用 there be。"),
    ("m5-nouns",               "M05", "名词",        "Nouns",                       PART1, "hero dark",  "可不可数，差别很大。"),
    ("m6-articles",            "M06", "冠词",        "Articles",                    PART1, "hero light", "小小 a / the，大大讲究。"),
    ("m7-pronouns",            "M07", "代词",        "Pronouns",                    PART1, "hero dark",  "替名词出场的人。"),
    ("m4-sentence-types",      "M08", "句子的种类",   "Simple · Compound · Complex", PART1, "hero light", "一根梁，还是三根梁。"),
    ("m5-tenses",              "M09", "动词时态",     "The Twelve Tenses",           PART2, "hero dark",  "时间是动词的刻度。"),
    ("m6-modal-verbs",         "M10", "情态动词",     "Modal Verbs",                 PART2, "hero light", "态度与可能性的开关。"),
    ("m7-passive-voice",       "M11", "被动语态",     "Passive Voice",               PART2, "hero dark",  "谁做，还是谁被做。"),
    ("m8-non-finite-verbs",    "M12", "非谓语动词",   "to do · doing · done",        PART2, "hero light", "动词的三个分身。"),
    ("m9-subjunctive",         "M13", "虚拟语气",     "Subjunctive Mood",            PART2, "hero dark",  "假如的世界。"),
    ("m14-reported-speech",    "M14", "直接与间接引语", "Reported Speech",           PART2, "hero light", "把别人的话转个头。"),
    ("m10-noun-clauses",       "M15", "名词性从句",   "Noun Clauses",                PART3, "hero dark",  "把从句整个当名词。"),
    ("m11-attribute-clauses",  "M16", "定语从句",     "Attributive Clauses",         PART3, "hero light", "跑到名词后面的形容词。"),
    ("m12-adverbial-clauses",  "M17", "状语从句",     "Adverbial Clauses",           PART3, "hero dark",  "条件 · 原因 · 让步。"),
    ("m13-agreement",          "M18", "主谓一致",     "Subject-Verb Agreement",      PART3, "hero light", "主语和谓语，人数对齐。"),
    ("m14-comparison",         "M19", "比较等级",     "Comparison",                  PART4, "hero dark",  "谁比谁，更怎么样。"),
    ("m15-inversion",          "M20", "倒装句",      "Inversion",                   PART4, "hero light", "倒过来，更有劲。"),
    ("m16-emphasis",           "M21", "强调句",      "Emphasis",                    PART4, "hero dark",  "把重点抬到台前。"),
    ("m17-ellipsis",           "M22", "省略句",      "Ellipsis",                    PART4, "hero light", "能省则省，不碍理解。"),
    ("m18-conjunctions",       "M23", "连词与并列",   "Conjunctions & Coordination", PART4, "hero dark",  "把句子粘起来。"),
    ("m24-prepositions",       "M24", "介词",        "Prepositions",                PART4, "hero light", "小词定乾坤。"),
    ("m25-questions",          "M25", "疑问句",      "Questions",                   PART4, "hero dark",  "会问，才会交流。"),
    ("m26-punctuation",        "M26", "标点与大写",   "Punctuation & Capitalization", PART5, "hero light", "细节见功夫。"),
    ("m19-common-mistakes",    "M27", "高频易错点",   "Common Mistakes",             PART5, "hero dark",  "中国学生的老坑。"),
    ("m20-exam-types",         "M28", "题型速览",     "Exam Question Types",         PART5, "hero light", "考场最爱怎么考。"),
]"""
src, n = re.subn(r"MODULES = \[\n(?:.*\n)*?\]\n", new_modules + "\n", src, count=1)
print("MODULES replaced:", n)

# --- 3) cover: 20 -> 28 modules + author line
old = "<span>·</span><span>20 模块 · M01–M28</span>"
assert old in src, "cover meta not found"
src = src.replace(old, "<span>·</span><span>28 模块 · M01–M28</span>")
old = """    </div>
  </div>
  <div class="foot"><div>一套能当「教材」翻的语法课</div>"""
assert old in src, "cover foot anchor not found"
src = src.replace(old, """    </div>
    <div style="font-family:var(--mono);font-size:max(12px,0.9vw);letter-spacing:.14em;opacity:.78" data-anim>作者 · Adam Wang &middot; 英语教师 &middot; arikimizord@163.com</div>
  </div>
  <div class="foot"><div>一套能当「教材」翻的语法课</div>""")

# --- 4) contents: 3 columns
old = """    left = part_col(*groups[0]) + part_col(*groups[1])
    right = part_col(*groups[2]) + part_col(*groups[3]) + part_col(*groups[4])"""
assert old in src, "contents cols not found"
src = src.replace(old, """    left = part_col(*groups[0])
    mid = part_col(*groups[1]) + part_col(*groups[2])
    right = part_col(*groups[3]) + part_col(*groups[4])""")
old = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:.8vh 2.6vw;align-content:start;flex:1;min-height:0;margin-top:.6vh">{left}{right}</div>'
assert old in src, "contents grid not found"
src = src.replace(old, '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8vh 2.2vw;align-content:start;flex:1;min-height:0;margin-top:.6vh">{left}{mid}{right}</div>')
old = '<h2 class="h-xl" style="white-space:nowrap;font-size:4.5vw" data-anim>轻轻一点，去哪一章</h2>'
assert old in src, "contents title not found"
src = src.replace(old, '<h2 class="h-xl" style="white-space:nowrap;font-size:min(4.5vw,8vh)" data-anim>轻轻一点，去哪一章</h2>')

# --- 5) head(): vh cap on h-xl + xl_style vw transform
old = """def head(kicker, cn_title, en_title, lead=None, xl_style=""):
    fs = min(6.2, AVAIL_VW * 0.96 / max(_est_em(cn_title), 1.0))"""
assert old in src, "head() not found"
src = src.replace(old, """def head(kicker, cn_title, en_title, lead=None, xl_style=""):
    m_xl = re.search(r"font-size:([\\d.]+)vw", xl_style)
    if m_xl:
        v_xl = float(m_xl.group(1))
        xl_style = xl_style.replace(m_xl.group(0), f"font-size:min({v_xl}vw,{v_xl*1.78:.2f}vh)")
    fs = min(6.2, AVAIL_VW * 0.96 / max(_est_em(cn_title), 1.0))""")
old = '''h += f'<h2 class="h-xl" style="white-space:nowrap;font-size:{fs:.2f}vw;{xl_style}" data-anim>{cn_title}</h2>\''''
assert old in src, "h-xl template not found"
src = src.replace(old, '''h += f'<h2 class="h-xl" style="white-space:nowrap;font-size:min({fs:.2f}vw,{fs*1.78:.2f}vh);{xl_style}" data-anim>{cn_title}</h2>\'''')

# --- 6) font cap: max(PX, Xvw) -> max(PX, min(Xvw, 1.78X vh)) across build.py
def cap(m):
    px, vw = m.group(1), m.group(2)
    return "max(%spx,min(%svw,%.2fvh))" % (px, vw, float(vw) * 1.78)
src, n = re.subn(r"max\((\d+(?:\.\d+)?)px,(\d+(?:\.\d+)?)vw\)", cap, src)
print("max() capped:", n)

# --- 7) exec content fragments + NOTES_FRAG collection, before NOTES.sort
old = "NOTES.sort(key=lambda n:"
assert old in src, "NOTES.sort anchor not found"
src = src.replace(old, """# ------------------------------------------------------------------
# 8b) content fragments (content/*.py) -- exec'd with helpers in scope
# ------------------------------------------------------------------
import glob as _glob
for _f in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "*.py"))):
    exec(compile(open(_f, encoding="utf-8").read(), _f, "exec"), globals())
    NOTES.extend(globals().get("NOTES_FRAG", []))

NOTES.sort(key=lambda n:""")

# --- 8) pilot_for: new module mappings
old = """    "m20-exam-types":      ["m20-exam-mcq","m20-exam-cloze","m20-exam-trans","m20-exam-practice"],
    }.get(mid, [])"""
assert old in src, "pilot_for tail not found"
src = src.replace(old, """    "m20-exam-types":      ["m20-exam-mcq","m20-exam-cloze","m20-exam-trans","m20-exam-practice"],
    "m2-sentence-elements":["m2-elem-subj-pred","m2-elem-obj-pred","m2-elem-attrib-adverb","m2-elem-practice"],
    "m4-there-be":         ["m4-therebe-basic","m4-therebe-neg","m4-therebe-tense","m4-therebe-practice"],
    "m5-nouns":            ["m5-noun-count","m5-noun-plural","m5-noun-poss","m5-noun-practice"],
    "m6-articles":         ["m6-art-aan","m6-art-the","m6-art-zero","m6-art-practice"],
    "m7-pronouns":         ["m7-pron-personal","m7-pron-possessive","m7-pron-indefinite","m7-pron-practice"],
    "m4-sentence-types":   ["m8-type-simple","m8-type-compound","m8-type-complex","m8-type-practice"],
    "m14-reported-speech": ["m14-rep-statement","m14-rep-changes","m14-rep-questions","m14-rep-practice"],
    "m24-prepositions":    ["m24-prep-time","m24-prep-place","m24-prep-fixed","m24-prep-practice"],
    "m25-questions":       ["m25-ques-yesno","m25-ques-wh","m25-ques-tag","m25-ques-practice"],
    "m26-punctuation":     ["m26-punct-basic","m26-punct-apos","m26-punct-caps","m26-punct-practice"],
    }.get(mid, [])""")

# --- 9) NOTES cover/contents text: 20 -> 28
src = src.replace("说明 20 个模块、可随时回来", "说明 28 个模块、可随时回来")
src = src.replace("5 大部分 20 模块", "5 大部分 28 模块")

open(p, "w", encoding="utf-8", newline="").write(src)
print("done, size", n0, "->", len(src))
