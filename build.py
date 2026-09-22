# -*- coding: utf-8 -*-
"""Assemble the bilingual English-grammar web-PPT from the guizang template.

Splices: Forest Ink theme, <title>, navigation cluster CSS/JS, all slides,
and SPEAKER_NOTES into a copy of assets/template.html.
Re-run any time slides are added — page numbers auto-recompute.
"""
import re, os

# Template resolution: env var > repo-local template/ > local skill install.
# The template ships with this repo under AGPL-3.0 (see template/README.md);
# original upstream: https://github.com/op7418/guizang-ppt-skill
_here = os.path.dirname(os.path.abspath(__file__))
_local = os.path.join(_here, "template", "template.html")
_skill = os.path.join(os.environ.get("GUIZANG_SKILL",
        r"E:" + chr(92) + "ClaudeCode" + chr(92) + "claude-config" + chr(92) + "skills" + chr(92) + "guizang-ppt-skill"),
        "assets", "template.html")
SRC = os.environ.get("GRAMMAR_TEMPLATE") or (_local if os.path.exists(_local) else _skill)
# Output defaults to the repo ROOT (index.html) so static hosts like
# Tencent EdgeOne Pages / GitHub Pages can serve the deck directly.
OUT_DIR = os.environ.get("GRAMMAR_OUT") or _here
OUT = os.path.join(OUT_DIR, "index.html")

html = open(SRC, encoding="utf-8").read()

# ------------------------------------------------------------------
# 1) Theme -> Forest Ink
# ------------------------------------------------------------------
html = re.sub(
    r"--ink:#[0-9a-fA-F]+;\s*\n\s*--ink-rgb:[0-9, ]+;\s*\n\s*--paper:#[0-9a-fA-F]+;\s*\n\s*--paper-rgb:[0-9, ]+;\s*\n\s*--paper-tint:#[0-9a-fA-F]+;\s*\n\s*--ink-tint:#[0-9a-fA-F]+;",
    "--ink:#1a2e1f;\n    --ink-rgb:26,46,31;\n    --paper:#f5f1e8;\n    --paper-rgb:245,241,232;\n    --paper-tint:#ece7da;\n    --ink-tint:#253d2c;",
    html, count=1,
)
html = html.replace(
    "<title>[必填] 替换为 PPT 标题 · Deck Title</title>",
    "<title>英语语法双语精讲 · English Grammar Guide for Vocational College</title>",
)

# ------------------------------------------------------------------
# 2) extra CSS before </style>
# ------------------------------------------------------------------
EXTRA_CSS = """
/* ============ 自定义:顶栏导航簇 + 学习卡片 (本 deck 追加) ============ */
#nav-back{position:fixed;left:2.4vw;top:3vh;z-index:40;display:flex;gap:8px;align-items:center;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase}
#nav-back button{all:unset;display:inline-flex;align-items:center;gap:.5em;cursor:pointer;padding:6px 12px;border:1px solid currentColor;border-radius:3px;opacity:.75;color:inherit;white-space:nowrap}
#nav-back button:hover,#nav-back button:focus-visible{opacity:1;text-decoration:underline;text-underline-offset:.3em}
body.ppt-audience #nav-back,body.ppt-preview #nav-back{display:none!important}
.learn-card{display:flex;flex-direction:column;gap:.7vh;padding-top:.9vh;border-top:1px solid currentColor;border-color:rgba(127,127,127,.32);min-width:0}
.learn-card .lc-t{display:flex;align-items:baseline;gap:.8em;flex-wrap:wrap}
.learn-card .lc-t .cn{font-family:var(--serif-zh);font-weight:700;font-size:max(26px,min(2.1vw,3.74vh));line-height:1.15}
.learn-card .lc-t .en{font-family:var(--serif-en);font-style:italic;font-weight:500;font-size:max(18px,min(1.45vw,2.58vh));opacity:.5}
.learn-card .lc-rule{font-family:var(--sans-zh);font-weight:400;font-size:max(18px,min(1.4vw,2.49vh));line-height:1.55;opacity:.8}
.ex-line{font-family:var(--serif-en);font-size:max(21px,min(1.65vw,2.94vh));line-height:1.4;font-weight:400}
.ex-line .tgt{font-style:italic;font-weight:600}
.ex-gl{display:block;font-family:var(--sans-zh);font-size:max(17px,min(1.35vw,2.40vh));line-height:1.45;opacity:.66;margin-top:.15vh}
.mist{margin-top:.6vh}
.mist .m-label{display:flex;align-items:center;gap:.5em;font-family:var(--mono);font-size:12px;letter-spacing:.22em;text-transform:uppercase;opacity:.6;margin-bottom:.6vh}
.mist .m-body{font-family:var(--sans-zh);font-size:max(18px,min(1.4vw,2.49vh));line-height:1.55;opacity:.85}
.practice{padding-top:1vh;border-top:1px dashed rgba(127,127,127,.32);margin-top:1.2vh}
.practice .p-label{font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;opacity:.55;margin-bottom:.8vh}
.practice .p-q{font-family:var(--sans-zh);font-size:max(20px,min(1.55vw,2.76vh));line-height:1.45;opacity:.9;margin-bottom:.5vh}
.practice .p-q .qnum{font-family:var(--serif-en);font-style:italic;font-weight:600;margin-right:.5em}
.sv-main{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:minmax(0,1fr);gap:1.2vh 2.6vw;flex:1;align-content:center;margin-top:.6vh}
.sv-cols{display:grid;grid-template-columns:1fr 1fr;gap:3vw;flex:1;align-content:center;margin-top:1vh}
media (max-width:900px){.sv-cols{grid-template-columns:1fr}}
/* 课堂投影可读性:lead 加大 */
.lead{font-size:max(20px,min(1.9vw,3.38vh))}
/* ============ Aha! 点击揭晓练习 ============ */
.mini-p{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4em .8em;margin-top:.4vh;border-top:1px dashed rgba(127,127,127,.25);padding-top:.8vh;font-family:var(--sans-zh);font-size:max(17px,min(1.35vw,2.40vh));line-height:1.5}
.mini-p .mp-label{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;opacity:.55;white-space:nowrap}
.mini-p .mp-q{opacity:.92}
.mini-p .mp-q em{font-family:var(--serif-en);font-weight:600}
.p-q{display:flex;flex-wrap:wrap;align-items:baseline;gap:.3em .8em}
.aha{all:unset;cursor:pointer;font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;border:1px solid currentColor;border-radius:3px;padding:4px 12px;opacity:.7;white-space:nowrap;transform:translateY(-1px)}
.aha:hover,.aha:focus-visible{opacity:1;text-decoration:underline;text-underline-offset:.3em}
.mini-p .ans,.p-q .ans{display:none;flex-basis:100%;margin-top:.2vh;padding:.3vh 1vw;border-left:2px solid currentColor;background:rgba(127,127,127,.08);font-family:var(--sans-zh);font-size:max(17px,min(1.3vw,2.31vh));line-height:1.4}
.mini-p .ans em,.p-q .ans em{font-family:var(--serif-en);font-weight:600;font-style:italic}
.revealed .ans{display:block}
/* ============ 目录右上角 IP:Learn with Adam (动态) ============ */
.ip-brand{position:absolute;top:8.2vh;right:6vw;z-index:6;font-family:var(--serif-en);font-style:italic;font-weight:600;font-size:max(19px,min(1.55vw,2.76vh));letter-spacing:.02em;pointer-events:none;white-space:nowrap}
.ip-brand .lwa-text{background:linear-gradient(90deg,var(--ink) 0%,#4e6b52 30%,#86a089 50%,#4e6b52 70%,var(--ink) 100%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:lwa-shine 4s ease-in-out infinite}
.ip-brand .lwa-dot{display:inline-block;margin-left:.35em;width:.32em;height:.32em;border-radius:50%;background:var(--ink);vertical-align:.32em;animation:lwa-pulse 2s ease-in-out infinite}
keyframes lwa-shine{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
keyframes lwa-pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(.75)}}
/* ============ 目录页行(类化,便于矮视口压缩) ============ */
.toc-row{all:unset;cursor:pointer;display:flex;align-items:baseline;gap:.9em;width:100%;text-align:left;padding:.2vh 0;border-top:1px solid rgba(127,127,127,.25)}
.toc-code{font-family:var(--mono);font-size:12px;letter-spacing:.18em;opacity:.5;white-space:nowrap}
.toc-cn{font-family:var(--serif-zh);font-weight:600;font-size:max(15px,min(1.4vw,2.05vh));white-space:nowrap;line-height:1.2}
.toc-en{font-family:var(--serif-en);font-style:italic;font-weight:400;font-size:max(12px,min(1.05vw,1.55vh));opacity:.55;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* ============ 矮视口(笔记本带浏览器条 / 超宽屏)紧凑模式 ============ */
@media (max-height:840px){
  .learn-card{gap:.3vh;padding-top:.5vh}
  .mini-p{padding-top:.35vh;margin-top:.2vh}
  .mini-p .ans,.p-q .ans{padding:.1vh 1vw;margin-top:.1vh}
  .practice{padding-top:.4vh;margin-top:.5vh}
  .practice .p-q{margin-bottom:.2vh}
  .mist{margin-top:.3vh}
  .sv-cols,.sv-main{margin-top:.4vh!important}
  .ex-line{line-height:1.24}
  .ex-gl{margin-top:0;line-height:1.24}
  .h-sub{margin-top:.2vh!important}
  .lead{margin-top:.4vh!important}
  .toc-row{padding:0}
  .toc-code{font-size:9px}
  .toc-cn{font-size:max(13px,min(1.05vw,1.8vh))}
  .toc-en{font-size:10px}
}
"""
html = html.replace("</style>", EXTRA_CSS + "</style>", 1)

# ------------------------------------------------------------------
# 3) NAV JS before </body>
# ------------------------------------------------------------------
NAV_JS = """
<script>
(function(){
  document.addEventListener('click',function(e){
    if(!(e.target && e.target.closest)) return;
    var a = e.target.closest('.aha');
    if(a){
      var box = a.closest('.mini-p') || a.closest('.p-q') || a.closest('.practice');
      if(box){
        var on = box.classList.toggle('revealed');
        a.textContent = on ? '\\u25B2 收起答案' : 'Aha! 答案揭晓';
      }
      e.preventDefault();
      return;
    }
    var g = e.target.closest('[data-goto]');
    if(!g) return;
    if(!g) return;
    e.preventDefault();
    var id = g.getAttribute('data-goto');
    var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
    var i = slides.findIndex(function(s){return s.getAttribute('data-slide-id')===id;});
    if(i>=0 && window.go) go(i,{force:true});
  });
})();
</script>
"""
html = html.replace("</body>", NAV_JS + "</body>", 1)

# ------------------------------------------------------------------
# 4) Module metadata + slide templates
# ------------------------------------------------------------------
PART1 = ("Ⅰ", "词法篇", "MORPHOLOGY · WORD CLASSES")
PART2 = ("Ⅱ", "句法篇", "SYNTAX")
PART3 = ("Ⅲ", "动词系统", "THE VERB SYSTEM")
PART4 = ("Ⅳ", "从句与一致", "CLAUSES & AGREEMENT")
PART5 = ("Ⅴ", "特殊结构与实战", "ADVANCED & PRACTICE")

MODULES = [
    # ---- Part Ⅰ 词法篇:十大词类(词性总览是上位概念,统领 M02–M10) ----
    ("m1-parts-of-speech",     "M01", "词性总览",     "Parts of Speech",             PART1, "hero dark",  "十大词类，一张地图。"),
    ("m5-nouns",               "M02", "名词",        "Nouns",                       PART1, "hero light", "可不可数，差别很大。"),
    ("m6-articles",            "M03", "冠词",        "Articles",                    PART1, "hero light",  "小小 a / the，大大讲究。"),
    ("m7-pronouns",            "M04", "代词",        "Pronouns",                    PART1, "hero dark", "替名词出场的人。"),
    ("pos-verbs",              "M05", "动词",        "Verbs",                       PART1, "hero dark",  "句子的心脏，五副面孔。"),
    ("pos-adjectives",         "M06", "形容词",       "Adjectives",                  PART1, "hero light", "给名词上色的人。"),
    ("pos-adverbs",            "M07", "副词",        "Adverbs",                     PART1, "hero dark",  "修饰动词与形容词。"),
    ("pos-numerals",           "M08", "数词",        "Numerals",                    PART1, "hero light", "数得清，才算数得明白。"),
    ("m24-prepositions",       "M09", "介词",        "Prepositions",                PART1, "hero light",  "小词定乾坤。"),
    ("m18-conjunctions",       "M10", "连词",        "Conjunctions",                PART1, "hero light", "把词与句粘起来。"),
    # ---- Part Ⅱ 句法篇:词如何组成句子 ----
    ("m2-sentence-elements",   "M11", "句子成分",     "Sentence Elements",           PART2, "hero dark",  "把句子拆成零件。"),
    ("m3-five-patterns",       "M12", "五种基本句型",  "Five Basic Patterns",         PART2, "hero dark", "所有长句都能长出。"),
    ("m4-there-be",            "M13", "There be 句型", "There Be Structure",         PART2, "hero light",  "说「有」，用 there be。"),
    ("m4-sentence-types",      "M14", "句子的种类",   "Simple · Compound · Complex", PART2, "hero light", "一根梁，还是三根梁。"),
    ("m25-questions",          "M15", "疑问句",      "Questions",                   PART2, "hero dark",  "会问，才会交流。"),
    # ---- Part Ⅲ 动词系统 ----
    ("m5-tenses",              "M16", "动词时态",     "The Twelve Tenses",           PART3, "hero light", "时间是动词的刻度。"),
    ("m6-modal-verbs",         "M17", "情态动词",     "Modal Verbs",                 PART3, "hero light",  "态度与可能性的开关。"),
    ("m7-passive-voice",       "M18", "被动语态",     "Passive Voice",               PART3, "hero dark", "谁做，还是谁被做。"),
    ("m8-non-finite-verbs",    "M19", "非谓语动词",   "to do · doing · done",        PART3, "hero light",  "动词的三个分身。"),
    ("m9-subjunctive",         "M20", "虚拟语气",     "Subjunctive Mood",            PART3, "hero light", "假如的世界。"),
    ("m14-reported-speech",    "M21", "直接与间接引语", "Reported Speech",           PART3, "hero light",  "把别人的话转个头。"),
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
]
def divider(mid):
    code, cn, en, part, theme, tag = MODULES_by_id[mid][1:8] if False else (None,None,None,None,None,None)
    mid, code, cn, en, part, theme, tag = MODULES_by_id[mid]
    pnum, pcn, pen = part
    return f"""<section class="slide {theme}" data-slide-id="{mid}">
  <div class="chrome"><div>English Grammar · 英语语法</div><div>{code} · NN / TOTAL</div></div>
  <div class="frame" style="display:grid; gap:5vh; align-content:center; min-height:80vh">
    <div style="display:flex; align-items:center; gap:1.6vw">
      <div class="kicker" data-anim>Part {pnum} · {pen}</div><span class="tag" data-anim>{code}</span>
    </div>
    <h1 class="h-hero" style="font-size:8vw" data-anim>{cn}</h1>
    <h2 class="h-sub" data-anim>{en}</h2>
    <p class="lead" style="max-width:55vw" data-anim>{tag}</p>
    <div data-anim style="margin-top:.5vh"><button type="button" data-goto="contents" class="bk">Outloopy ↖ 返回目录 · Contents</button></div>
  </div>
  <div class="foot"><div>Part {pnum} · {pcn} · {cn}</div><div>— · —</div></div>
</section>"""

CHROME_LEFT = "English Grammar · 英语语法"

def slide(mid, theme, foot_left, code="GRAMMAR", body=""):
    return f"""<section class="slide {theme}" data-slide-id="{mid}">
  <div class="chrome"><div>{CHROME_LEFT}</div><div>{code} · NN / TOTAL</div></div>
  <div class="frame" style="display:flex; flex-direction:column">{body}</div>
  <div class="foot"><div>{foot_left}</div><div>— · —</div></div>
</section>"""

MODULES_by_id = {m[0]: m for m in MODULES}

# kicker/head helpers reused across pilot content
def _est_em(t):
    """Estimate rendered width (em units) of a title: CJK≈1em, latin≈0.56em etc."""
    import re as _re, html as _html, unicodedata as _ud
    t = _html.unescape(_re.sub(r'<[^>]+>', '', t))
    w = 0.0
    for ch in t:
        if _ud.east_asian_width(ch) in ('W','F'): w += 1.0
        elif ch == ' ': w += 0.26
        elif ch in '.,:;+\'’&': w += 0.30
        elif ch.isdigit() or ch in '()': w += 0.42
        else: w += 0.56
    return w

AVAIL_VW = 88  # slide padding 6vw each side
def head(kicker, cn_title, en_title, lead=None, xl_style=""):
    m_xl = re.search(r"font-size:([\d.]+)vw", xl_style)
    if m_xl:
        v_xl = float(m_xl.group(1))
        xl_style = xl_style.replace(m_xl.group(0), f"font-size:min({v_xl}vw,{v_xl*1.78:.2f}vh)")
    fs = min(6.2, AVAIL_VW * 0.96 / max(_est_em(cn_title), 1.0))
    h = f'<div class="kicker" data-anim>{kicker}</div>'
    h += f'<h2 class="h-xl" style="white-space:nowrap;font-size:min({fs:.2f}vw,{fs*1.78:.2f}vh);{xl_style}" data-anim>{cn_title}</h2>'
    if en_title:
        h += f'<div class="h-sub" style="margin-top:.6vh" data-anim>{en_title}</div>'
    if lead:
        h += f'<p class="lead" style="max-width:64vw; margin-top:.8vh" data-anim>{lead}</p>'
    return h

# ------------------------------------------------------------------
# 5) Pilot content: M1 (词性) and M3 (五种基本句型)
# ------------------------------------------------------------------
PILOT = {}

PILOT["m1-pos-overview"] = slide("m1-pos-overview","light","M01 · 9大词性总览","M01",
  head("Parts of Speech · 什么叫词性","一个字，一个身份","9 parts of speech") +
  """<div class="sv-main">
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">名词</span><span class="en">noun · n.</span></div><span class="ex-line">a <span class="tgt">book</span>, <span class="tgt">Paris</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">动词</span><span class="en">verb · v.</span></div><span class="ex-line">He <span class="tgt">runs</span>.</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">形容词</span><span class="en">adjective · adj.</span></div><span class="ex-line">a <span class="tgt">beautiful</span> flower</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">副词</span><span class="en">adverb · adv.</span></div><span class="ex-line">She sings <span class="tgt">well</span>.</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">代词</span><span class="en">pronoun · pron.</span></div><span class="ex-line"><span class="tgt">It</span> is mine.</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">数词</span><span class="en">numeral · num.</span></div><span class="ex-line"><span class="tgt">three</span> books</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">冠词</span><span class="en">article · art.</span></div><span class="ex-line"><span class="tgt">a</span> / <span class="tgt">an</span> / <span class="tgt">the</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">介词</span><span class="en">preposition · prep.</span></div><span class="ex-line"><span class="tgt">in</span> 2024</span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">连词</span><span class="en">conjunction · conj.</span></div><span class="ex-line"><span class="tgt">and</span> / <span class="tgt">but</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">感叹词</span><span class="en">interjection · int.</span></div><span class="ex-line"><span class="tgt">Oh!</span></span></div>
  </div>""")

PILOT["m1-pos-content-words"] = slide("m1-pos-content-words","dark","M01 · 实词细节（上）","M01",
  head("Content Words (1) · 可以真正&lsquo;翻译&rsquo;的词","实词：名词 动词","content words carry meaning") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">名词 noun</span><span class="en">n. · 表人事物地</span></div>
        <span class="ex-line">I have <span class="tgt">a pen</span>.<span class="ex-gl">注意可数 / 不可数、单复数</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I have many homework.</em> → ✔ <em>much homework</em>（homework 不可数）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">There are five <em>___</em> on the desk.（boxs / boxes）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>boxes</em> — box 以 x 结尾，复数加 <em>-es</em>：box → boxes。可数名词复数别漏词尾。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">动词 verb</span><span class="en">v. · 动作与状态</span></div>
        <span class="ex-line">She <span class="tgt">is</span> a teacher.<span class="ex-gl">系动词 / 及物 / 不及物由此展开</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">She <em>___</em> to school every day.（go / goes）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>goes</em> — 一般现在时，主语 she 是第三人称单数，动词加 <em>-es</em>。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m1-pos-content-words-b"] = slide("m1-pos-content-words-b","light","M01 · 实词细节（下）","M01",
  head("Content Words (2) · 修饰与被修饰","实词：形容词 副词","adjectives describe nouns") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">形容词 adjective</span><span class="en">adj. · 修饰名词</span></div>
        <span class="ex-line">a <span class="tgt">tall</span> boy<span class="ex-gl">放名词前，或放 be 之后</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>She is very beauty.</em> → ✔ <em>She is very beautiful.</em>（用形容词）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">He is a <em>___</em> boy.（carefully / careful）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>careful</em> — 修饰名词 boy 用形容词；carefully 是副词。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">副词 adverb</span><span class="en">adv. · 修饰动词/形容词</span></div>
        <span class="ex-line">He runs <span class="tgt">quickly</span>.<span class="ex-gl">常由 adj + -ly 变来</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">He sings <em>___</em>.（beautiful / beautifully）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>beautifully</em> — 修饰动作 sings 用副词：beautiful + ly。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m1-pos-function-words"] = slide("m1-pos-function-words","dark","M01 · 虚词细节（上）","M01",
  head("Function Words (1) · 字数不多,作用不小","虚词：冠词 介词 连词","function words glue the sentence") +
  """<div class="sv-cols" style="margin-top:.5vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">冠词 article</span><span class="en">a / an / the</span></div>
        <span class="ex-line"><span class="tgt">The</span> sun is bright.<span class="ex-gl">the 特指；a/an 泛指</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">运动不加 the：✘ <em>I play the basketball.</em> → ✔ <em>I play basketball.</em></div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">I saw <em>___</em> elephant.（a / an）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>an</em> — elephant 以元音音素开头，用 an。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">介词 preposition</span><span class="en">in / on / at…</span></div>
        <span class="ex-line">at 7 o&rsquo;clock · on Monday · <span class="tgt">in</span> March</span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The book is <em>___</em> the desk.（in / on / at）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>on</em> — 在桌面上用 on；in 表“里面”，at 只到“点”。</span></div>
      </div>
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">连词 conjunction</span><span class="en">and / but / because…</span></div>
        <span class="ex-line"><span class="tgt">Because</span> it rained, we stayed home.</span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">He was tired, <em>___</em> he kept going.（but / so / because）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>but</em> — 前后意思转折（累 ↔ 坚持），用表转折的连词。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m1-pos-function-words-b"] = slide("m1-pos-function-words-b","light","M01 · 虚词细节（下）","M01",
  head("Function Words (2) · 代替与数数","虚词：代词 数词","pronouns and numerals") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">代词 pronoun</span><span class="en">he / she / it / they</span></div>
        <span class="ex-line"><span class="tgt">They</span> are my friends.<span class="ex-gl">主格 / 宾格 / 物主代词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">主语用主格：✘ <em>Lily and me are classmates.</em> → ✔ <em>Lily and I are classmates.</em></div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">This book is <em>___</em>.（my / mine）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>mine</em> — 后面没有名词时用名词性物主代词 mine = my book。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">数词 numeral</span><span class="en">基数 + 序数</span></div>
        <span class="ex-line">three desks · the <span class="tgt">third</span> day<span class="ex-gl">序数词前常加 the</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">May is the <em>___</em> month of the year.（five / fifth）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>fifth</em> — “第五个月”表顺序用序数词，前面加 the：the fifth。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m1-pos-practice"] = slide("m1-pos-practice","dark","M01 · 练习","M01",
  head("Quick Practice · 词性见分晓","练一练：选词填空","choose the right word", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选词填空 · Choose the right word</div>
      <div class="p-q"><span class="qnum">1.</span><em>beautiful / beauty</em> — This flower is so ______ .（是“样子”，用 adj.）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>beautiful</em> — be 动词后作表语用形容词；beauty 是名词“美丽”。</span></div>
      <div class="p-q"><span class="qnum">2.</span><em>careful / carefully</em> — Drive ______ on the wet road.（修饰“开车”，用 adv.）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>carefully</em> — 修饰动作 drive 用副词：careful + ly。</span></div>
      <div class="p-q"><span class="qnum">3.</span><em>their / they</em> — ______ love reading.（作主语）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>They</em> — 空缺处是句子主语，用主格代词；their 是物主代词“他们的”。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">看到 <em>be / look / smell</em> 后缺的通常是形容词；看到“动作怎样发生”，用副词。</div>
    </div>""")

PILOT["m3-patterns-overview"] = slide("m3-patterns-overview","light","M03 · 五句型总览","M03",
  head("Five Basic Patterns · 五种基本句型","长句都由这 5 种骨架长出","S 主语 · V 谓语 · O 宾语 · C 补语") +
  """<div class="sv-main" style="grid-template-columns:repeat(3,1fr);margin-top:1.5vh">
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">1 · 主谓</span><span class="en">SV</span></div><span class="ex-line"><span class="tgt">We</span> <span class="tgt">work</span>.<span class="ex-gl">最简单：谁 + 干什么</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">2 · 主系表</span><span class="en">SVC</span></div><span class="ex-line"><span class="tgt">She</span> <span class="tgt">is</span> <span class="tgt">a teacher</span>.<span class="ex-gl">be/look 等系动词 + 补语</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">3 · 主谓宾</span><span class="en">SVO</span></div><span class="ex-line"><span class="tgt">I</span> <span class="tgt">like</span> <span class="tgt">English</span>.<span class="ex-gl">动作 + 承受者</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">4 · 主谓双宾</span><span class="en">SVOO</span></div><span class="ex-line"><span class="tgt">I</span> <span class="tgt">gave</span> <span class="tgt">him</span> <span class="tgt">a book</span>.<span class="ex-gl">给“人” + 给“物”</span></span></div>
    <div class="learn-card" data-anim><div class="lc-t"><span class="cn">5 · 主谓宾宾补</span><span class="en">SVOC</span></div><span class="ex-line"><span class="tgt">We</span> <span class="tgt">call</span> <span class="tgt">him</span> <span class="tgt">Tom</span>.<span class="ex-gl">宾语 + 补充宾语的补语</span></span></div>
  </div>""")

PILOT["m3-patterns-svc-svo"] = slide("m3-patterns-svc-svo","dark","M03 · SVC / SVO","M03",
  head("SVC 主系表 · SVO 主谓宾","最重要的两种骨架","be / look / feel …　及物动词") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主系表 SVC</span><span class="en">「是 / 变得 / 显得」</span></div>
        <span class="ex-line"><span class="tgt">The sky</span> <span class="tgt">looks</span> <span class="tgt">blue</span>.<span class="ex-gl">系动词常见：be, look, feel, taste, seem, become</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">系动词后要形容词，不是副词：✘ <em>The sky looks beautifully-ly.</em> → ✔ <em>The sky looks blue.</em></div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The soup tastes <em>___</em>.（well / good）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>good</em> — taste 是系动词，后面接形容词作表语；well 一般修饰动作。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主谓宾 SVO</span><span class="en">动作 + 宾语</span></div>
        <span class="ex-line"><span class="tgt">I</span> <span class="tgt">eat</span> <span class="tgt">an apple</span>.<span class="ex-gl">及物动词才有宾语</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">“发生”是不及物动词，不接宾：✘ <em>He happened an accident.</em> → ✔ <em>An accident happened.</em></div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">划出宾语：<em>My sister loves music.</em></span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ 宾语是 <em>music</em> — loves 是及物动词，music 是动作的承受者（SVO）。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m3-patterns-svooc"] = slide("m3-patterns-svooc","light","M03 · SVOO / SVOC","M03",
  head("SVOO 双宾 · SVOC 宾补","给谁，「把」什么称为什么","give · send · call · make · keep") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主谓双宾 SVOO</span><span class="en">give / send / buy</span></div>
        <span class="ex-line"><span class="tgt">She</span> <span class="tgt">sent</span> <span class="tgt">me</span> <span class="tgt">a postcard</span>.<span class="ex-gl">人（间宾）+ 物（直宾），可换写成 to me</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">She told <em>___</em> a story.（we / us）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>us</em> — 间接宾语（给“谁”）用宾格代词；we 是主格。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主谓宾宾补 SVOC</span><span class="en">make / call / keep</span></div>
        <span class="ex-line"><span class="tgt">They</span> <span class="tgt">call</span> <span class="tgt">the dog</span> <span class="tgt">Lucky</span>.<span class="ex-gl">宾语 + 补语，合起来才算完整</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">“这让我很高兴”：直接用 <em>This makes me happy.</em> 不用画蛇添足。</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The news made everybody <em>___</em>.（happily / happy）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>happy</em> — 宾补说明 everybody 的状态，用形容词；happily 是副词。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m3-patterns-practice"] = slide("m3-patterns-practice","dark","M03 · 练习","M03",
  head("Quick Practice · 给句子定骨架","练一练：判定句型","identify the pattern", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">判定句型 · SV / SVC / SVO / SVOO / SVOC</div>
      <div class="p-q"><span class="qnum">1.</span>I <em>bought</em> my mother <em>a coat</em>. → ______（两个宾语）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>SVOO</em> — 双宾：my mother（给人）+ a coat（给物）。</span></div>
      <div class="p-q"><span class="qnum">2.</span>He <em>looks</em> tired. → ______（系动词+补语）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>SVC</em> — looks 是系动词，tired 是表语（说明 He 的状态）。</span></div>
      <div class="p-q"><span class="qnum">3.</span>We <em>made</em> him <em>the captain</em>. → ______（宾语+补语）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>SVOC</em> — the captain 补充说明 him：we made him [to be] the captain。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Birds <em>fly</em>. → ______（最短的骨架）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>SV</em> — 主语 + 不及物动词，最短但完整的句子。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">记得 · Remember</div>
      <div class="m-body">先找 <em>S + V</em>，再看后面跟着 <em>O / C / OO / OC</em> —— 骨架就出来了，长句只是它的加长版。</div>
    </div>""")

# ------------------------------------------------------------------
# 5b) M09 动词时态（The Twelve Tenses）— 6 pages
# ------------------------------------------------------------------
def mp(label_q, choices, ans):
    """mini-p row: 练 label + question + Aha! button + hidden answer."""
    return ('<div class="mini-p"><span class="mp-label">练</span>'
            f'<span class="mp-q">{label_q}（{choices}）</span>'
            '<button type="button" class="aha">Aha! 答案揭晓</button>'
            f'<span class="ans">{ans}</span></div>')

PILOT["m5-tense-overview"] = slide("m5-tense-overview","light","M09 · 十二时态地图","M09",
  head("The Twelve Tenses · 十二时态地图","4 种「体」× 3 种「时间」","time × aspect", xl_style="font-size:5vw") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim><div class="lc-t"><span class="cn">一般 · Simple</span><span class="en">do / did / will do</span></div><span class="ex-line">He <span class="tgt">goes</span> to school every day.</span>""" +
      mp("He ___ up at six.","go / goes","✔ <em>goes</em> — 表习惯 / 事实；he 是三单，动词加 -es。") + """
      </div>
      <div class="learn-card" data-anim><div class="lc-t"><span class="cn">完成 · Perfect</span><span class="en">have / has + done</span></div><span class="ex-line">I <span class="tgt">have finished</span> my homework.</span>""" +
      mp("I have ___ it.","do / done","✔ <em>done</em> — have + 过去分词，强调「已经做完」。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim><div class="lc-t"><span class="cn">进行 · Continuous</span><span class="en">be + doing</span></div><span class="ex-line">She <span class="tgt">is reading</span> now.</span>""" +
      mp("She ___ TV now.","watches / is watching","✔ <em>is watching</em> — be + doing，此刻正在做。") + """
      </div>
      <div class="learn-card" data-anim><div class="lc-t"><span class="cn">完成进行 · Perfect Cont.</span><span class="en">have been doing</span></div><span class="ex-line">We <span class="tgt">have been waiting</span> for an hour.</span>""" +
      mp("I have been ___ .","wait / waiting","✔ <em>waiting</em> — have been + doing，一直做到现在。") + """
      </div>
    </div>
  </div>""")

PILOT["m5-tense-present"] = slide("m5-tense-present","dark","M09 · 现在：一般 / 进行","M09",
  head("一般现在时 · 现在进行时","习惯用一般，「此刻」用进行","simple present · present continuous") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">一般现在时 Simple Present</span><span class="en">do / does</span></div>
        <span class="ex-line">The sun <span class="tgt">rises</span> in the east.<span class="ex-gl">习惯 / 事实 / 常态；三单主语动词加 -s/-es</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">三单漏 -s：✘ <em>He like music.</em> → ✔ <em>He likes music.</em></div></div>""" +
      mp("Water ___ at 100&deg;C.","boil / boils","✔ <em>boils</em> — 客观事实用一般现在时；water 三单，加 -s。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">现在进行时 Present Continuous</span><span class="en">am / is / are + doing</span></div>
        <span class="ex-line">She <span class="tgt">is reading</span> now.<span class="ex-gl">此刻正在做；信号词：now, Look!, Listen!</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">漏掉 be 动词：✘ <em>She reading.</em> → ✔ <em>She is reading.</em>（be + doing 缺一不可）</div></div>""" +
      mp("Look! It ___ .","rains / is raining","✔ <em>is raining</em> — Look! 说明动作正在进行，用 is + raining。") + """
      </div>
    </div>
  </div>""")

PILOT["m5-tense-past"] = slide("m5-tense-past","light","M09 · 过去：一般 / 进行","M09",
  head("一般过去时 · 过去进行时","过去发生的事，动词「变形」","simple past · past continuous") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">一般过去时 Simple Past</span><span class="en">did</span></div>
        <span class="ex-line">I <span class="tgt">visited</span> the museum last week.<span class="ex-gl">过去某时做了；信号词：yesterday, last…, …ago</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">did 后面用原形：✘ <em>Did you went?</em> → ✔ <em>Did you go?</em>（did 已带过去含义）</div></div>""" +
      mp("He ___ to Beijing in 2020.","goes / went","✔ <em>went</em> — in 2020 是过去时间，用 go 的过去式 went。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">过去进行时 Past Continuous</span><span class="en">was / were + doing</span></div>
        <span class="ex-line">I <span class="tgt">was cooking</span> when he called.<span class="ex-gl">过去某刻正在做；常与 when 搭配当背景</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">was 后面别忘 doing：✘ <em>I was cook.</em> → ✔ <em>I was cooking.</em></div></div>""" +
      mp("At 8 pm I ___ .","read / was reading","✔ <em>was reading</em> — 过去某一时刻正在进行：was + doing。") + """
      </div>
    </div>
  </div>""")

PILOT["m5-tense-future"] = slide("m5-tense-future","dark","M09 · 将来：will / be going to","M09",
  head("一般将来时 · 两种说法","临时决定 · 早已计划","will vs be going to") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">will do</span><span class="en">临时决定 / 预测</span></div>
        <span class="ex-line">I <span class="tgt">will call</span> you tonight.<span class="ex-gl">说话时才决定的事；will 后面用动词原形</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">will 后用原形：✘ <em>He will comes.</em> → ✔ <em>He will come.</em></div></div>""" +
      mp("He ___ 18 next year.","will be / is","✔ <em>will be</em> — 明年是将来的事，will + be（原形）。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">be going to do</span><span class="en">计划 / 有迹象</span></div>
        <span class="ex-line">We <span class="tgt">are going to have</span> a picnic.<span class="ex-gl">早就计划好的事；别漏 be 动词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">漏 be：✘ <em>I going to go.</em> → ✔ <em>I am going to go.</em></div></div>""" +
      mp("I ___ visit my grandma.","am going to / going to","✔ <em>am going to</em> — be going to 前面必须带上 be 动词 am。") + """
      </div>
    </div>
  </div>""")

PILOT["m5-tense-perfect"] = slide("m5-tense-perfect","light","M09 · 完成：现在 / 过去","M09",
  head("现在完成时 · 过去完成时","「已经做了」与「过去的过去」","present perfect · past perfect") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">现在完成时 Present Perfect</span><span class="en">have / has + done</span></div>
        <span class="ex-line">I <span class="tgt">have finished</span> my homework.<span class="ex-gl">做完了且影响现在；信号词：already, since, for</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">明确过去时间不用完成时：✘ <em>I have seen him yesterday.</em> → ✔ <em>I saw him yesterday.</em></div></div>""" +
      mp("He ___ here since 2019.","lives / has lived","✔ <em>has lived</em> — since + 过去时间点，动作延续到现在，用现在完成时。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">过去完成时 Past Perfect</span><span class="en">had + done</span></div>
        <span class="ex-line">The train <span class="tgt">had left</span> when I arrived.<span class="ex-gl">「过去的过去」：比过去动作更早</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">两件过去的事，先发生的用 had done：✘ <em>had left · arrived</em> 顺序别颠倒。</div></div>""" +
      mp("When I got there, the film ___ .","began / had begun","✔ <em>had begun</em> — 开演在「到达」之前，是过去的过去：had + done。") + """
      </div>
    </div>
  </div>""")

PILOT["m5-tense-practice"] = slide("m5-tense-practice","dark","M09 · 练习","M09",
  head("Quick Practice · 给动词定时态","练一练：括号词填空","put the verb in the right tense", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">用括号内动词的正确形式填空 · Put the verb in the right tense</div>
      <div class="p-q"><span class="qnum">1.</span>My father ______ TV every evening.（watch）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>watches</em> — every evening 表习惯，用一般现在时；主语三单，加 -es。</span></div>
      <div class="p-q"><span class="qnum">2.</span>Look! The children ______ in the river.（swim）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>are swimming</em> — Look! 提示此刻正在进行：are + doing。</span></div>
      <div class="p-q"><span class="qnum">3.</span>We ______ basketball yesterday afternoon.（play）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>played</em> — yesterday 是过去时间，用过去式。</span></div>
      <div class="p-q"><span class="qnum">4.</span>She ______ a teacher since 2015.（be）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>has been</em> — since + 过去时间点，延续到现在：has + been。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">先找<b>时间信号词</b>：every/usually → 一般；now/Look → 进行；yesterday/last → 过去；since/for/already → 完成。词形跟着信号词走。</div>
    </div>""")

# ------------------------------------------------------------------
# 5c) M10 情态动词（Modal Verbs）— 4 pages
# ------------------------------------------------------------------
PILOT["m6-modal-can"] = slide("m6-modal-can","dark","M10 · 能力与许可","M10",
  head("can · could · may","能不能，请求与许可","ability · permission") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">can / could</span><span class="en">能力 · 请求</span></div>
        <span class="ex-line">She <span class="tgt">can</span> swim fast. / <span class="tgt">Can</span> I borrow your pen?<span class="ex-gl">can 表「会」，could 更委婉</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">can 后接原形，没有三单变化：✘ <em>She can swims.</em> → ✔ <em>She can swim.</em></div></div>""" +
      mp("Monkeys ___ climb trees.","can / cans","✔ <em>can</em> — 情态动词后永远接动词原形，不受主语影响。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">may / might</span><span class="en">许可 · 可能</span></div>
        <span class="ex-line"><span class="tgt">May</span> I come in?<span class="ex-gl">May I…? 最礼貌的请求；might 表更小的可能</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">回答 May I…? 不说 <em>Yes, you may not</em> —— 拒绝说 <em>I&rsquo;m afraid not.</em></div></div>""" +
      mp("___ I ask a question?","May / Am","✔ <em>May</em> — 请求许可用 May I…?，句尾可用 please 更礼貌。") + """
      </div>
    </div>
  </div>""")

PILOT["m6-modal-must"] = slide("m6-modal-must","light","M10 · 必须与禁止","M10",
  head("must · have to","「必须」的两种说法","obligation") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">must</span><span class="en">主观必须 · 禁止</span></div>
        <span class="ex-line">You <span class="tgt">must</span> finish it today.<span class="ex-gl">mustn&rsquo;t = 禁止（别做！）</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">mustn&rsquo;t ≠ 不必：「不必」是 <em>don&rsquo;t have to</em>；✘ <em>You mustn&rsquo;t come if you&rsquo;re busy.</em>（应为 don&rsquo;t have to）</div></div>""" +
      mp("The light is red. You ___ stop.","must / can","✔ <em>must</em> — 红灯必须停：must 表「必须」，语气最强。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">have to</span><span class="en">客观必须</span></div>
        <span class="ex-line">She <span class="tgt">has to</span> get up early.<span class="ex-gl">外部条件逼的；随人称、时态变化</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">三单要变形：✘ <em>He have to go.</em> → ✔ <em>He has to go.</em>（must 永远不变形）</div></div>""" +
      mp("He ___ wear a uniform at work.","have to / has to","✔ <em>has to</em> — 主语 he 三单，have 变 has。") + """
      </div>
    </div>
  </div>""")

PILOT["m6-modal-should"] = slide("m6-modal-should","dark","M10 · 建议与劝告","M10",
  head("should · had better","「应该」与「最好」","advice") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">should / shouldn&rsquo;t</span><span class="en">建议</span></div>
        <span class="ex-line">You <span class="tgt">should</span> see a doctor.<span class="ex-gl">给建议的常用词；shouldn&rsquo;t = 不应该</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">should 后接原形：✘ <em>You should to go.</em> → ✔ <em>You should go.</em></div></div>""" +
      mp("He ___ study harder.","should / should to","✔ <em>should</em> — 情态动词后接原形，不加 to。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">had better</span><span class="en">最好…（带警告）</span></div>
        <span class="ex-line">You&rsquo;d <span class="tgt">better</span> hurry.<span class="ex-gl">否则会有不好的结果；缩写 You&rsquo;d better</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别漏 had 的缩写：✘ <em>You better go.</em> → ✔ <em>You&rsquo;d better go.</em></div></div>""" +
      mp("You&rsquo;d ___ tell her the truth.","better / good","✔ <em>better</em> — had better do = 最好做…；缩写 You&rsquo;d better。") + """
      </div>
    </div>
  </div>""")

PILOT["m6-modal-practice"] = slide("m6-modal-practice","light","M10 · 练习","M10",
  head("Quick Practice · 选对情态动词","练一练：语气对了才算对","choose the right modal", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选词填空 · Choose the right modal</div>
      <div class="p-q"><span class="qnum">1.</span>______ I use your phone?（May / Must）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>May</em> — 请求许可用 May I…?；must 是「必须」。</span></div>
      <div class="p-q"><span class="qnum">2.</span>She ______ speak three languages.（can / cans）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>can</em> — 情态动词后接原形，永远不加 -s。</span></div>
      <div class="p-q"><span class="qnum">3.</span>You ______ play on the street. It&rsquo;s dangerous!（mustn&rsquo;t / don&rsquo;t have to）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>mustn&rsquo;t</em> — 危险的事要「禁止」；don&rsquo;t have to 只是「不必」。</span></div>
      <div class="p-q"><span class="qnum">4.</span>It&rsquo;s cold outside. You ______ wear a coat.（should / shouldn&rsquo;t）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>should</em> — 天冷该穿衣，给建议用 should。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">情态动词三不走：<b>不加 -s、不加 to、否定直接 not</b>。后接动词原形，谁做主语都不变。</div>
    </div>""")

# ------------------------------------------------------------------
# 5d) M11 被动语态（Passive Voice）— 4 pages
# ------------------------------------------------------------------
PILOT["m7-passive-core"] = slide("m7-passive-core","light","M11 · 什么是被动","M11",
  head("be + 过去分词","主语是「被做」的那一个","passive voice") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">构成：be + done</span><span class="en">被动分词不变形</span></div>
        <span class="ex-line">English <span class="tgt">is spoken</span> all over the world.<span class="ex-gl">英语是「被说」的；be 随时态人称变，done 不变</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别漏 be：✘ <em>The room cleaned every day.</em> → ✔ <em>The room is cleaned every day.</em></div></div>""" +
      mp("Rice ___ in the south.","grow / is grown","✔ <em>is grown</em> — rice 是「被种」的，用 be + 过去分词 grown。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">何时用被动</span><span class="en">when &amp; why</span></div>
        <span class="ex-line">The window <span class="tgt">was broken</span>.<span class="ex-gl">不知道谁做的 / 谁做的不重要 / 强调承受者</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">过去分词别写错：break → broke → <em>broken</em>；✘ <em>was broke</em></div></div>""" +
      mp("The window ___ by Tom.","break / was broken","✔ <em>was broken</em> — 窗户是「被打碎」的，用 was + broken。") + """
      </div>
    </div>
  </div>""")

PILOT["m7-passive-tenses"] = slide("m7-passive-tenses","dark","M11 · 被动的时态","M11",
  head("被动也分时态","变 be，不动 done","tense lives in be") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">常用三种</span><span class="en">is done · was done · can be done</span></div>
        <span class="ex-line">The room <span class="tgt">is cleaned</span> every day.<span class="ex-gl">一般现在被动态；时态全压在 be 上</span></span>
        <span class="ex-line">The bridge <span class="tgt">was built</span> in 1990.<span class="ex-gl">一般过去被动态：is → was</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">情态动词后：✘ <em>can built</em> → ✔ <em>can be built</em>（be 别丢）</div></div>""" +
      mp("The bridge ___ in 1990.","built / was built","✔ <em>was built</em> — 1990 是过去，被动用 was + 过去分词。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">将来与情态</span><span class="en">will be done · must be done</span></div>
        <span class="ex-line">The work <span class="tgt">will be finished</span> tomorrow.<span class="ex-gl">will + be + done；must/can 同理</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">will 后的 be 不能省：✘ <em>will finished</em> → ✔ <em>will be finished</em></div></div>""" +
      mp("Homework must ___ today.","finish / be finished","✔ <em>be finished</em> — 作业是「被完成」：must + be + done。") + """
      </div>
    </div>
  </div>""")

PILOT["m7-passive-transform"] = slide("m7-passive-transform","light","M11 · 主动变被动","M11",
  head("主动 → 被动 三步走","宾语提前 · be + done · by 短语","active to passive") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">三步口诀</span><span class="en">3 steps</span></div>
        <span class="ex-line">Tom <span class="tgt">cleans</span> the room. &rarr; The room <span class="tgt">is cleaned</span> by Tom.<span class="ex-gl">① 宾语当主语 ② be+过去分词 ③ 原主语变 by…</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">时态要跟着原句走：原句是过去式，被动就用 <em>was/were + done</em>，别写成 is。</div></div>""" +
      mp("They built the school in 2001. &rarr; The school ___ by them.","was built / is built","✔ <em>was built</em> — 原句 built 是过去式，被动用 was built。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">by 短语可省</span><span class="en">omit the doer</span></div>
        <span class="ex-line">Chinese <span class="tgt">is spoken</span> here.<span class="ex-gl">谁说的不重要时，by 短语直接省掉</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">不及物动词没有被动：✘ <em>The accident was happened.</em> → ✔ <em>The accident happened.</em></div></div>""" +
      mp("判断：&ldquo;An accident was happened.&rdquo; 对吗?","对 / 错","✔ <em>错</em> — happen 是不及物动词，没有被动语态。") + """
      </div>
    </div>
  </div>""")

PILOT["m7-passive-practice"] = slide("m7-passive-practice","dark","M11 · 练习","M11",
  head("Quick Practice · 变被动","练一练：主动句改造","turn into passive", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">用被动语态填空 · Fill in with the passive</div>
      <div class="p-q"><span class="qnum">1.</span>Stamps ______ (use) to send letters.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>are used</em> — 邮票是「被用」的，一般现在被动：are + used。</span></div>
      <div class="p-q"><span class="qnum">2.</span>The Great Wall ______ (build) long long ago.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>was built</em> — 很久以前是过去时间，was + built。</span></div>
      <div class="p-q"><span class="qnum">3.</span>The homework must ______ (hand in) today.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>be handed in</em> — 情态动词后：must + be + 过去分词。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Tom ______ (give) a new bike last week.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>was given</em> — Tom 是「被给」的，last week 表过去。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">主语不会做这个动作 → 用被动；时态只改 <b>be</b>，过去分词 <b>done</b> 永远不动。</div>
    </div>""")

# ------------------------------------------------------------------
# 5e) M12 非谓语动词（Non-finite Verbs）— 5 pages
# ------------------------------------------------------------------
PILOT["m8-nonfinite-gerund"] = slide("m8-nonfinite-gerund","dark","M12 · 分身一：doing","M12",
  head("doing 作主语 / 宾语","动词变名词用：enjoy + doing","gerund") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">动词 + doing</span><span class="en">enjoy · finish · mind · like</span></div>
        <span class="ex-line">I enjoy <span class="tgt">reading</span> at night.<span class="ex-gl">enjoy / finish / mind 后面固定接 doing</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I enjoy to read.</em> → ✔ <em>I enjoy reading.</em>（enjoy 后不用 to do）</div></div>""" +
      mp("She enjoys ___ books.","read / reading","✔ <em>reading</em> — enjoy 后接 doing，这是固定搭配。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">doing 作主语 / 介词后</span><span class="en">swimming is fun</span></div>
        <span class="ex-line"><span class="tgt">Swimming</span> is good exercise.<span class="ex-gl">动词短语当名词用；介词后也一律 doing</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">介词后用 doing：✘ <em>good at swim</em> → ✔ <em>good at swimming</em></div></div>""" +
      mp("He is good at ___ .","draw / drawing","✔ <em>drawing</em> — 介词 at 后面的动词一律加 -ing。") + """
      </div>
    </div>
  </div>""")

PILOT["m8-nonfinite-infinitive"] = slide("m8-nonfinite-infinitive","light","M12 · 分身二：to do","M12",
  head("to do 表目的与愿望","want / decide / hope + to do","infinitive") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">动词 + to do</span><span class="en">want · decide · hope · plan</span></div>
        <span class="ex-line">I want <span class="tgt">to go</span> home.<span class="ex-gl">want / decide / hope 后固定接 to do</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">to 别丢：✘ <em>I want go home.</em> → ✔ <em>I want to go home.</em></div></div>""" +
      mp("He decided ___ the job.","accept / to accept","✔ <em>to accept</em> — decide 后接 to do。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">to do 表目的</span><span class="en">in order to</span></div>
        <span class="ex-line">He got up early <span class="tgt">to catch</span> the bus.<span class="ex-gl">「为了…」；放句首也可：To catch the bus, …</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">表目的用 to do，不用 for do：✘ <em>for catch the bus</em> → ✔ <em>to catch the bus</em></div></div>""" +
      mp("She ran fast ___ the train.","to catch / for catch","✔ <em>to catch</em> — 表「为了赶…」用 to do。") + """
      </div>
    </div>
  </div>""")

PILOT["m8-nonfinite-stop"] = slide("m8-nonfinite-stop","dark","M12 · 分身辨析：stop","M12",
  head("stop doing vs stop to do","一字之差，意思相反","classic contrast") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">stop doing</span><span class="en">停止手头的事</span></div>
        <span class="ex-line">He <span class="tgt">stopped smoking</span>.<span class="ex-gl">把「抽烟」这件事停了 = 戒烟</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">考试常考语义颠倒：说「停下来去休息」是 <em>stop to rest</em>，不是 stop resting。</div></div>""" +
      mp("We stopped ___ when the teacher came in.","talking / to talk","✔ <em>talking</em> — 老师来了，停止讲话：stop doing。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">stop to do</span><span class="en">停下来去做另一件事</span></div>
        <span class="ex-line">He <span class="tgt">stopped to smoke</span>.<span class="ex-gl">停下（手里的活）去抽烟</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">同类辨析：remember doing = 记得做过；remember to do = 记得要去做。</div></div>""" +
      mp("Tired, he stopped ___ a rest.","have / to have","✔ <em>to have</em> — 停下（原事）去休息：stop to do。") + """
      </div>
    </div>
  </div>""")

PILOT["m8-nonfinite-done"] = slide("m8-nonfinite-done","light","M12 · 分身三：done","M12",
  head("done 修饰名词：被动与完成","过去分词当形容词","past participle as adjective") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">done = 「被…的」</span><span class="en">a broken window</span></div>
        <span class="ex-line">a <span class="tgt">broken</span> window<span class="ex-gl">窗户是「被打破」的 → 用过去分词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">-ing 表主动，-ed 表被动：✘ <em>a breaking window</em>（窗在打人？）→ ✔ <em>a broken window</em></div></div>""" +
      mp("a ___ window（break 的形式）","breaking / broken","✔ <em>broken</em> — 窗户被打破，被动用 done。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">-ing vs -ed 的感觉</span><span class="en">boring · bored</span></div>
        <span class="ex-line">The book is <span class="tgt">boring</span>. I am <span class="tgt">bored</span>.<span class="ex-gl">物用 -ing（令人…），人用 -ed（感到…）</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I am boring.</em>（我在无聊地逗别人？）→ ✔ <em>I am bored.</em></div></div>""" +
      mp("The film was ___.","bored / boring","✔ <em>boring</em> — 电影「令人无聊」，物用 -ing。") + """
      </div>
    </div>
  </div>""")

PILOT["m8-nonfinite-practice"] = slide("m8-nonfinite-practice","dark","M12 · 练习","M12",
  head("Quick Practice · 选对分身","练一练：doing / to do / done","choose the right form", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">用所给动词的正确形式填空 · Choose the right form</div>
      <div class="p-q"><span class="qnum">1.</span>Would you mind ______ (open) the window?<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>opening</em> — mind 后固定接 doing。</span></div>
      <div class="p-q"><span class="qnum">2.</span>They hope ______ (visit) Beijing next year.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>to visit</em> — hope 后接 to do。</span></div>
      <div class="p-q"><span class="qnum">3.</span>Don&rsquo;t forget ______ (close) the door when you leave.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>to close</em> — 记得「要做」的事：forget to do。</span></div>
      <div class="p-q"><span class="qnum">4.</span>I fell asleep during the ______ (bore) lecture.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>boring</em> — 修饰事物（lecture 令人无聊）用 -ing。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">看前面的词：<b>enjoy/finish/mind/介词</b> 后用 doing；<b>want/decide/hope</b> 后用 to do；修饰名词时<b>被动用 done、物令人…用 -ing</b>。</div>
    </div>""")

# ------------------------------------------------------------------
# 5f) M13 虚拟语气（Subjunctive Mood）— 4 pages
# ------------------------------------------------------------------
PILOT["m9-subjunctive-if"] = slide("m9-subjunctive-if","light","M13 · 与现在相反","M13",
  head("If I were you…","与现在事实相反","did / would do · if I were") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">公式</span><span class="en">if + did, would + do</span></div>
        <span class="ex-line">If I <span class="tgt">had</span> time, I <span class="tgt">would come</span>.<span class="ex-gl">「要是…就好了」—— 其实没有时间</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">be 动词一律用 <em>were</em>：✘ <em>If I was you.</em> → ✔ <em>If I were you.</em></div></div>""" +
      mp("If I ___ you, I would study hard.","was / were","✔ <em>were</em> — 虚拟语气里 be 一律用 were，不分主语。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">语气判断</span><span class="en">real vs unreal</span></div>
        <span class="ex-line">If it <span class="tgt">rains</span>, I will stay. &ne; If it <span class="tgt">rained</span>, I would stay.<span class="ex-gl">真实条件用现在时；虚拟条件用过去式</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">虚拟句不是「过去的事」，是「不可能 / 假设的事」—— 时态往回退一步只为表虚拟。</div></div>""" +
      mp("If he ___ rich, he would buy a plane.","is / were","✔ <em>were</em> — 他并不富有，虚拟假设用 were。") + """
      </div>
    </div>
  </div>""")

PILOT["m9-subjunctive-past"] = slide("m9-subjunctive-past","dark","M13 · 与过去相反","M13",
  head("If I had done…","与过去事实相反","had done + would have done") +
  """<div class="sv-cols" style="margin-top:.3vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">公式</span><span class="en">if + had done, would have done</span></div>
        <span class="ex-line">If I <span class="tgt">had got up</span> early, I <span class="tgt">would have caught</span> the bus.<span class="ex-gl">「早知道就…」—— 过去没做到的事</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">主句别丢 have：✘ <em>would caught</em> → ✔ <em>would have caught</em></div></div>""" +
      mp("If he ___ earlier, he would not have missed it.","got up / had got up","✔ <em>had got up</em> — 过去没早起，从句用 had done。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">怎么区分两档</span><span class="en">now vs then</span></div>
        <span class="ex-line">与现在相反：did / would do<span class="ex-gl">退一步：现在 → 过去式</span></span>
        <span class="ex-line">与过去相反：had done / would have done<span class="ex-gl">退两步：过去 → 过去完成</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">看到过去时间（yesterday / last night）：从句 <em>had done</em>，主句 <em>would have done</em>。</div></div>""" +
      mp("虚拟的「退一步」:现在假设用 ___ 。","did / had done","✔ <em>did</em> — 与现在相反退一步；与过去相反退两步。") + """
      </div>
    </div>
  </div>""")

PILOT["m9-subjunctive-wish"] = slide("m9-subjunctive-wish","light","M13 · wish 的虚拟","M13",
  head("wish + 过去式","「但愿…（其实不能）」","I wish") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">wish 与现在相反</span><span class="en">wish + did / were</span></div>
        <span class="ex-line">I wish I <span class="tgt">were</span> taller.<span class="ex-gl">「真希望我更高」—— 现在不满足</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">wish 后不用现在时：✘ <em>I wish I am tall.</em> → ✔ <em>I wish I were tall.</em></div></div>""" +
      mp("I wish I ___ a bird.","am / were","✔ <em>were</em> — wish 表「不能实现的愿望」，用过去式 were。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">wish 与过去相反</span><span class="en">wish + had done</span></div>
        <span class="ex-line">I wish I <span class="tgt">had studied</span> harder.<span class="ex-gl">「后悔当初没更努力」</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">后悔用过去完成：✘ <em>I wish I studied harder then.</em>（要用 had studied）</div></div>""" +
      mp("I wish it ___ raining yesterday.","stopped / had stopped","✔ <em>had stopped</em> — 昨天的事没实现，用 had done。") + """
      </div>
    </div>
  </div>""")

PILOT["m9-subjunctive-practice"] = slide("m9-subjunctive-practice","dark","M13 · 练习","M13",
  head("Quick Practice · 虚拟一下","练一练：给动词退一步","put the verb back", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">用括号内动词的正确形式填空 · Put the verb in the right form</div>
      <div class="p-q"><span class="qnum">1.</span>If I ______ (be) a bird, I would fly away.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>were</em> — 与现在相反，be 一律用 were。</span></div>
      <div class="p-q"><span class="qnum">2.</span>If she ______ (study) harder, she would have passed the exam.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>had studied</em> — 与过去相反，从句用 had done。</span></div>
      <div class="p-q"><span class="qnum">3.</span>I wish today ______ (be) Sunday.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>were</em> — wish 与现在相反，用 were。</span></div>
      <div class="p-q"><span class="qnum">4.</span>If it ______ (not rain) yesterday, we would have played football.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>hadn&rsquo;t rained</em> — 过去下雨了才没踢成，从句用 had not rained。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">虚拟 = 时态<b>往回退</b>：现在的事退一步（did / were），过去的事退两步（had done）。主句相应配 would do / would have done。</div>
    </div>""")

# ------------------------------------------------------------------
# 5g) M15 名词性从句（Noun Clauses）— 4 pages
# ------------------------------------------------------------------
PILOT["m10-nc-overview"] = slide("m10-nc-overview","dark","M15 · 引导词 that / what","M15",
  head("Noun Clauses","把从句整个当名词","three connectors") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">用 that 引导</span><span class="en">clause is complete</span></div>
        <span class="ex-line">I know <span class="tgt">that he is right</span>.<span class="ex-gl">从句啥都不缺 → 用 that（只连接，无意义）</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">that 与 what 分不清：what = the thing that，<b>既引导又作成分</b>。✘ <em>I like that he said.</em> → ✔ <em>I like what he said.</em></div></div>""" +
      mp("I know ___ he likes music.","that / what","✔ <em>that</em> — 从句不缺任何成分，只做连接。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">用 what / who 引导</span><span class="en">clause needs a part</span></div>
        <span class="ex-line">Tell me <span class="tgt">what you want</span>.<span class="ex-gl">want 缺宾语 → what 补上这个位置</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">从句里缺主语或宾语时，别用 that：✘ <em>Tell me that you want.</em> → ✔ <em>Tell me what you want.</em></div></div>""" +
      mp("Tell me ___ you want.","that / what","✔ <em>what</em> — want 后面缺宾语，what 既引导又当宾语。") + """
      </div>
    </div>
  </div>""")

PILOT["m10-nc-order"] = slide("m10-nc-order","light","M15 · 宾语从句语序与时态","M15",
  head("宾语从句","陈述语序 · 时态跟着变","word order & tense") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">用陈述语序</span><span class="en">no do / does / did</span></div>
        <span class="ex-line">I don&rsquo;t know <span class="tgt">where he lives</span>.<span class="ex-gl">从句当宾语 → 按正常陈述句排</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别把疑问句语序搬进来：✘ <em>I don&rsquo;t know where does he live.</em> → ✔ <em>where he lives</em></div></div>""" +
      mp("Do you know where ___?","does he live / he lives","✔ <em>he lives</em> — 宾语从句一律用陈述语序，不倒装。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">时态跟着主句走</span><span class="en">tense back-shift</span></div>
        <span class="ex-line">He said <span class="tgt">he was busy</span>.<span class="ex-gl">主句过去时 → 从句也用过去时态</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He said he is busy.</em> → ✔ <em>He said he was busy.</em>（客观真理除外：The teacher said light travels fast.）</div></div>""" +
      mp("He said he ___ tired.","is / was","✔ <em>was</em> — 主句 said 是过去时，从句跟着用过去时。") + """
      </div>
    </div>
  </div>""")

PILOT["m10-nc-formal"] = slide("m10-nc-formal","dark","M15 · whether 与形式主语","M15",
  head("It / Whether","主语从句与形式主语","formal subject") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">It 顶位</span><span class="en">formal subject it</span></div>
        <span class="ex-line"><span class="tgt">It</span> is clear <span class="tgt">that he is right</span>.<span class="ex-gl">真主语太长 → It 占位，真主语放后面</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">主语从句放句首时用 whether，不用 if：✘ <em>If he will come is unknown.</em> → ✔ <em>Whether he will come is unknown.</em></div></div>""" +
      mp("___ he will come is unknown.","If / Whether","✔ <em>Whether</em> — 在句首当主语，只能用 whether。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">介词后只用 whether</span><span class="en">after preposition</span></div>
        <span class="ex-line">It depends on <span class="tgt">whether it rains</span>.<span class="ex-gl">介词 on 后面的「是否」→ whether</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">「是否」三场合只用 <b>whether</b>：句首主语、介词后面、or not 连用。宾语从句里 if / whether 都行。</div></div>""" +
      mp("I worry about ___ he is safe.","if / whether","✔ <em>whether</em> — 介词 about 后面只用 whether。") + """
      </div>
    </div>
  </div>""")

PILOT["m10-nc-practice"] = slide("m10-nc-practice","light","M15 · 练习","M15",
  head("Quick Practice · 填引导词","练一练：选对引导词","pick the connector", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的一项 · Pick the right connector</div>
      <div class="p-q"><span class="qnum">1.</span>I believe ______ he is honest.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>that</em> — 从句不缺成分，用 that 连接即可。</span></div>
      <div class="p-q"><span class="qnum">2.</span>Do you know ______ the book is?<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>where</em> — 从句缺地点状语，用 where，且用陈述语序。</span></div>
      <div class="p-q"><span class="qnum">3.</span>______ we need is more time.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>What</em> — 从句缺主语，what 既引导又作成分。</span></div>
      <div class="p-q"><span class="qnum">4.</span>She asked ______ I had finished it.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>whether / if</em> — 表「是否」；宾语从句里两者皆可，用陈述语序。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">缺什么补什么：缺主宾用 <b>what / who</b>，缺状语用 <b>where / when</b>，不缺用 <b>that</b>，表「是否」用 whether / if。</div>
    </div>""")

# ------------------------------------------------------------------
# 5h) M16 定语从句（Attributive Clauses）— 4 pages
# ------------------------------------------------------------------
PILOT["m11-rel-overview"] = slide("m11-rel-overview","light","M16 · 先行词与关系词","M16",
  head("Attributive","跑到名词后面的形容词","which noun?") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">先行词 + 关系词</span><span class="en">antecedent &amp; relative</span></div>
        <span class="ex-line">The book <span class="tgt">that I bought</span> is good.<span class="ex-gl">从句紧跟名词后，像形容词一样修饰它</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别重复宾语：✘ <em>The book that I bought it is good.</em>（that 已顶替 it 的位置）→ 删掉 it。</div></div>""" +
      mp("The girl ___ is singing is my sister.","who / whom","✔ <em>who</em> — 从句缺主语，指人用 who。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">who 指人 · which 指物</span><span class="en">who = person</span></div>
        <span class="ex-line">This is the man <span class="tgt">who helped me</span>.<span class="ex-gl">先行词是「人」→ who</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">先行词是物别用 who：✘ <em>the dog who barks</em> → ✔ <em>the dog which / that barks</em></div></div>""" +
      mp("The pen ___ I lost was new.","which / who","✔ <em>which</em> — 先行词 pen 是物，用 which（或 that）。") + """
      </div>
    </div>
  </div>""")

PILOT["m11-rel-that"] = slide("m11-rel-that","dark","M16 · 只能用 that 的场合","M16",
  head("Only That","只能用 that 的场合","special cases") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">最高级 / 序数词 / all</span><span class="en">superlative &amp; all</span></div>
        <span class="ex-line">This is the best film <span class="tgt">that</span> I have seen.<span class="ex-gl">先行词被最高级 / 序数词 / all / anything 修饰 → 用 that</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>the best film which I have seen</em> → 最高级后面习惯用 <b>that</b>。</div></div>""" +
      mp("All ___ glitters is not gold.","that / which","✔ <em>that</em> — 先行词是 all，关系词只能用 that。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">whose = 他的 / 它的</span><span class="en">possessive relative</span></div>
        <span class="ex-line">the boy <span class="tgt">whose father</span> is a doctor<span class="ex-gl">「他的爸爸」→ whose 代替 his</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>the boy who father is a doctor</em> → 从句里要表达「某人的」，用 <b>whose</b>。</div></div>""" +
      mp("the boy ___ father is a doctor","whose / who","✔ <em>whose</em> — 从句缺定语（他的），用 whose。") + """
      </div>
    </div>
  </div>""")

PILOT["m11-rel-where"] = slide("m11-rel-where","light","M16 · where / when","M16",
  head("Where / When","地点与时间的状语","adverb relatives") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">先行词是地点</span><span class="en">where = in which</span></div>
        <span class="ex-line">This is the town <span class="tgt">where I was born</span>.<span class="ex-gl">从句不缺主宾，缺「在哪里」→ where</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">从句缺宾语时用 which：✘ <em>the town where I like</em> → ✔ <em>the town which I like</em>（like 缺宾语）</div></div>""" +
      mp("This is the town ___ I was born.","where / which","✔ <em>where</em> — 从句成分齐全，只缺地点状语。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">先行词是时间</span><span class="en">when = on which</span></div>
        <span class="ex-line">I remember the day <span class="tgt">when we met</span>.<span class="ex-gl">缺「在什么时候」→ when</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">判断步骤：先看先行词（人 / 物 / 时间 / 地点），再看从句<b>缺什么</b>：缺主语宾语 → who / which / that；不缺 → where / when。</div></div>""" +
      mp("I remember the day ___ we met.","when / where","✔ <em>when</em> — 先行词 day 是时间。") + """
      </div>
    </div>
  </div>""")

PILOT["m11-rel-practice"] = slide("m11-rel-practice","dark","M16 · 练习","M16",
  head("Quick Practice · 填关系词","练一练：选对关系词","pick the relative", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的关系词 · Pick the right relative</div>
      <div class="p-q"><span class="qnum">1.</span>The man ______ lives next door is a pilot.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>who</em> — 指人，且从句缺主语。</span></div>
      <div class="p-q"><span class="qnum">2.</span>This is the best movie ______ I have ever seen.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>that</em> — 先行词被最高级修饰，只能用 that。</span></div>
      <div class="p-q"><span class="qnum">3.</span>I still remember the day ______ we first met.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>when</em> — 先行词是时间，从句不缺主宾。</span></div>
      <div class="p-q"><span class="qnum">4.</span>The girl ______ mother is a nurse is my classmate.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>whose</em> — 从句缺定语「她的」，用 whose。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">两步定关系词：① 看先行词（人 who · 物 which · 时间 when · 地点 where · 谁的 whose）；② 看从句缺不缺成分。</div>
    </div>""")

# ------------------------------------------------------------------
# 5i) M17 状语从句（Adverbial Clauses）— 4 pages
# ------------------------------------------------------------------
PILOT["m12-adv-overview"] = slide("m12-adv-overview","dark","M17 · 连词地图","M17",
  head("Adverbial","从句当副词：时间 · 条件 · 原因","connector map") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">四类常客</span><span class="en">four frequent connectors</span></div>
        <span class="ex-line"><span class="tgt">When</span> he came, I was cooking.<span class="ex-gl">when 时间 · if 条件 · because 原因 · although 让步</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">从句在主句前时，后面<b>加逗号</b>：When he came<em>,</em> I was cooking.</div></div>""" +
      mp("___ he came, I was cooking.","When / Whether","✔ <em>When</em> — 表「当…时候」，时间状语从句。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">铁律：主将从现</span><span class="en">no will in the clause</span></div>
        <span class="ex-line">If it <span class="tgt">rains</span>, I will stay.<span class="ex-gl">主句将来时 → 时间 / 条件从句用一般现在时</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>If it will rain, I will stay.</em> → will 不进 if / when 从句。</div></div>""" +
      mp("I&rsquo;ll go if it ___ fine.","will be / is","✔ <em>is</em> — 主将从现：条件从句用一般现在时。") + """
      </div>
    </div>
  </div>""")

PILOT["m12-adv-cause"] = slide("m12-adv-cause","light","M17 · 原因与让步","M17",
  head("Because / Although","原因与让步：连词不配对","never paired") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">because 不配 so</span><span class="en">one connector only</span></div>
        <span class="ex-line">He was tired, <span class="tgt">so</span> he slept.<span class="ex-gl">so 表结果；because 表原因，两者只用一个</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">中式连用是错的：✘ <em>Because he was tired, so he slept.</em> → 删掉 so（或删 because）。</div></div>""" +
      mp("He was tired, ___ he slept.","so / because","✔ <em>so</em> — 前因后果，结果用 so。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">although 不配 but</span><span class="en"> concession</span></div>
        <span class="ex-line"><span class="tgt">Although</span> it rained, we went out.<span class="ex-gl">「虽然…但是…」英文只用 although</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Although it rained, but we went out.</em> → 删掉 but。</div></div>""" +
      mp("___ it rained, we went out.","Although / Because","✔ <em>Although</em> — 前后是让步关系（下雨还是出门）。") + """
      </div>
    </div>
  </div>""")

PILOT["m12-adv-until"] = slide("m12-adv-until","dark","M17 · until 直到","M17",
  head("Until","直到为止 · 直到才","until & not until") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">肯定：一直等到</span><span class="en">keep doing until</span></div>
        <span class="ex-line">I waited <span class="tgt">until</span> he came.<span class="ex-gl">等这个动作一直持续到他来</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">until 从句同样<b>主将从现</b>：I will wait until he <em>comes</em>.</div></div>""" +
      mp("I will wait ___ he comes back.","until / because","✔ <em>until</em> — 「一直等到」用 until。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">否定：直到…才</span><span class="en">not &hellip; until</span></div>
        <span class="ex-line">He <span class="tgt">didn&rsquo;t leave</span> until I came.<span class="ex-gl">「我才走」→ not &hellip; until 是固定搭档</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He left until I came.</em> → 否定句才配 until：「没走，直到我来」。</div></div>""" +
      mp("He didn&rsquo;t sleep ___ his mother came back.","until / after","✔ <em>until</em> — 「直到妈妈回来才睡」→ not &hellip; until。") + """
      </div>
    </div>
  </div>""")

PILOT["m12-adv-practice"] = slide("m12-adv-practice","light","M17 · 练习","M17",
  head("Quick Practice · 选连词","练一练：选对连词","pick the connector", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的连词 · Pick the right connector</div>
      <div class="p-q"><span class="qnum">1.</span>I will call you when he ______ back.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>comes</em> — 主将从现：时间从句用一般现在时。</span></div>
      <div class="p-q"><span class="qnum">2.</span>______ he was ill, he still came to class.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>Although</em> — 让步关系，且不与 but 连用。</span></div>
      <div class="p-q"><span class="qnum">3.</span>She didn&rsquo;t stop working ______ it was midnight.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>until</em> — 「直到半夜才停」→ not &hellip; until。</span></div>
      <div class="p-q"><span class="qnum">4.</span>He studied hard, ______ he passed the exam.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>so</em> — 前因后果；注意不用 because &hellip; so 连用。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">两条铁律带走：<b>主将从现</b>（if / when 从句不用 will）；<b>连词不配对</b>（because 不配 so，although 不配 but）。</div>
    </div>""")

# ------------------------------------------------------------------
# 5j) M18 主谓一致（Subject-Verb Agreement）— 4 pages
# ------------------------------------------------------------------
PILOT["m13-agr-overview"] = slide("m13-agr-overview","light","M18 · 三单与不可数","M18",
  head("Agreement","主语和谓语，人数对齐","who does what") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">三单 + s</span><span class="en">third person singular</span></div>
        <span class="ex-line">He <span class="tgt">likes</span> music.<span class="ex-gl">一般现在时：he / she / it 后动词加 s</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He like music.</em> → 中国学生最高频的漏 s 错误。</div></div>""" +
      mp("She ___ (like) music.","like / likes","✔ <em>likes</em> — she 是第三人称单数。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">不可数名词当单数</span><span class="en">uncountable = singular</span></div>
        <span class="ex-line">The news <span class="tgt">is</span> good.<span class="ex-gl">news / maths / water 都是单数</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">news 看着像复数其实是单数：✘ <em>The news are good.</em> → ✔ <em>is</em></div></div>""" +
      mp("The news ___ good.","is / are","✔ <em>is</em> — news 是不可数名词，当单数。") + """
      </div>
    </div>
  </div>""")

PILOT["m13-agr-plural"] = slide("m13-agr-plural","dark","M18 · 复数主语","M18",
  head("Both / People","复数主语一览","plural subjects") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">天生复数词</span><span class="en">always plural</span></div>
        <span class="ex-line">Many people <span class="tgt">are</span> here.<span class="ex-gl">people / police 永远配复数动词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Many people is here.</em> → people 本身就是复数，「一个人」要说 a person。</div></div>""" +
      mp("Many people ___ here.","is / are","✔ <em>are</em> — people 是复数。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">both 复数 · either 单数</span><span class="en">both vs either</span></div>
        <span class="ex-line"><span class="tgt">Both</span> answers <span class="tgt">are</span> right. / <span class="tgt">Either</span> of them <span class="tgt">is</span> fine.<span class="ex-gl">两个都 → 复数；任选其 → 单数</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">each / either / neither + of 后接单数：✘ <em>Neither of them are right.</em> → ✔ <em>is right</em></div></div>""" +
      mp("Both answers ___ right.","is / are","✔ <em>are</em> — both 表示「两个都」，配复数。") + """
      </div>
    </div>
  </div>""")

PILOT["m13-agr-nearby"] = slide("m13-agr-nearby","light","M18 · 就近与就远","M18",
  head("Near or Far","就近 · 就远","proximity rule") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">就近原则</span><span class="en">agree with the nearest</span></div>
        <span class="ex-line">Neither he nor I <span class="tgt">am</span> a teacher.<span class="ex-gl">either&hellip;or / neither&hellip;nor / not only&hellip;but also / there be → 动词跟最近的主语</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Neither he nor I is a teacher.</em> → 离动词最近的是 I，所以用 am。</div></div>""" +
      mp("Neither he nor I ___ a teacher.","am / is","✔ <em>am</em> — 就近原则：跟最近的主语 I 保持一致。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">就远原则</span><span class="en">agree with the first</span></div>
        <span class="ex-line">The teacher with his students <span class="tgt">is</span> coming.<span class="ex-gl">with / as well as / together with → 跟前面的主语保持一致</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">with 类短语是「陪同」，不算主语人数 → 就远，看第一个主语；or 类选择是「二选一」→ 就近，看离得最近的。</div></div>""" +
      mp("The teacher with his students ___ coming.","is / are","✔ <em>is</em> — 就远原则：主语是 the teacher。") + """
      </div>
    </div>
  </div>""")

PILOT["m13-agr-practice"] = slide("m13-agr-practice","dark","M18 · 练习","M18",
  head("Quick Practice · 定动词","练一练：动词跟谁走","pick the verb", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的动词形式 · Pick the right verb</div>
      <div class="p-q"><span class="qnum">1.</span>Maths ______ my favorite subject.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>is</em> — maths 看似复数实为单数（学科名）。</span></div>
      <div class="p-q"><span class="qnum">2.</span>Neither of the answers ______ correct.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>is</em> — neither &hellip; of 后接单数。</span></div>
      <div class="p-q"><span class="qnum">3.</span>Either you or he ______ to go.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>has</em> — 就近原则：离动词最近的是 he。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Mr. Wang as well as his sons ______ fishing every Sunday.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>goes</em> — 就远原则：as well as 不算主语，主语是 Mr. Wang。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">先抓<b>真正的主语</b>：with / as well as 是陪同（就远），or / nor 是选择（就近）；news / maths 当单数，people 当复数。</div>
    </div>""")

# ------------------------------------------------------------------
# 5k) M19 比较等级（Comparison）— 4 pages
# ------------------------------------------------------------------
PILOT["m14-comp-forms"] = slide("m14-comp-forms","dark","M19 · 比较级怎么变","M19",
  head("Comparison","比较级：-er 或 more","forms") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">短词 -er · 长词 more</span><span class="en">er vs more</span></div>
        <span class="ex-line">tall &rarr; taller &middot; useful &rarr; <span class="tgt">more useful</span><span class="ex-gl">单音节加 -er；多音节前加 more</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>more bigger</em> → 二选一：bigger 或 more big（更错），只能 bigger。</div></div>""" +
      mp("This road is ___ than that one.","long / longer","✔ <em>longer</em> — 有 than，用比较级。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">双写与改 y</span><span class="en">spelling rules</span></div>
        <span class="ex-line">big &rarr; <span class="tgt">bigger</span> &middot; happy &rarr; <span class="tgt">happier</span><span class="ex-gl">重读闭音节双写辅音；辅音字母 + y 改 i 加 er</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>biger / happyer</em> → big 双写 g；happy 把 y 变 i。</div></div>""" +
      mp("Today is ___ (hot) than yesterday.","hoter / hotter","✔ <em>hotter</em> — 重读闭音节，双写 t 再加 er。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-comp-than"] = slide("m14-comp-than","light","M19 · 比较级句型","M19",
  head("Than","比较级的三个搭档","patterns") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">much / even 修饰</span><span class="en">much, not very</span></div>
        <span class="ex-line">He is <span class="tgt">much taller</span> than me.<span class="ex-gl">比较级前用 much / even / a little 加强</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>very taller</em> → very 只修饰原级，比较级前用 much。</div></div>""" +
      mp("He is ___ taller than me.","very / much","✔ <em>much</em> — 比较级前用 much 加强，不用 very。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">越…越…</span><span class="en">the + er, the + er</span></div>
        <span class="ex-line"><span class="tgt">The more</span> you read, <span class="tgt">the better</span> you write.<span class="ex-gl">「The + 比较级, the + 比较级」= 越…越…</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">两个 the 都不能丢：✘ <em>More you read, better you write.</em></div></div>""" +
      mp("___ you practice, the better you get.","The more / More","✔ <em>The more</em> — 前 the 引导从句，后 the 配套。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-comp-super"] = slide("m14-comp-super","dark","M19 · 最高级","M19",
  head("Superlative","最高级：the + -est / most","the best") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">the 不能丢</span><span class="en">always the</span></div>
        <span class="ex-line">She is <span class="tgt">the tallest</span> in our class.<span class="ex-gl">最高级前必须加 the</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>She is tallest in our class.</em> → 最高级前面加 the。</div></div>""" +
      mp("She is the ___ of the three.","taller / tallest","✔ <em>tallest</em> — 三者以上比较用最高级。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">in 范围 · of 同类</span><span class="en">in vs of</span></div>
        <span class="ex-line">the tallest <span class="tgt">in</span> the class &middot; the tallest <span class="tgt">of</span> the three<span class="ex-gl">in + 集体 / 地点；of + 同类数量</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>the most easiest</em> → est 和 most 只能用一个：easiest。</div></div>""" +
      mp("He is the best ___ all the students.","in / of","✔ <em>of</em> — of + 同类的人或物；in + 地点范围。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-comp-practice"] = slide("m14-comp-practice","light","M19 · 练习","M19",
  head("Quick Practice · 比一比","练一练：选对比较形式","pick the form", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的形式 · Pick the right form</div>
      <div class="p-q"><span class="qnum">1.</span>Li Lei is ______ than his brother.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>taller</em> — 有 than 用比较级，不加 more。</span></div>
      <div class="p-q"><span class="qnum">2.</span>It is much ______ today than yesterday.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>hotter</em> — much 修饰比较级；hot 双写 t。</span></div>
      <div class="p-q"><span class="qnum">3.</span>She is ______ student in our class.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>the best</em> — in + 范围用最高级，the 别丢。</span></div>
      <div class="p-q"><span class="qnum">4.</span>The harder you work, ______ you get.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>the luckier</em> — 「the + 比较级, the + 比较级」结构。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">见 <b>than</b> 用比较级，见范围用最高级（the 别丢）；比较级前用 <b>much</b> 不用 very；两者比较 -er，三者以上 -est。</div>
    </div>""")

# ------------------------------------------------------------------
# 5l) M20 倒装句（Inversion）— 4 pages
# ------------------------------------------------------------------
PILOT["m15-inv-full"] = slide("m15-inv-full","light","M20 · 完全倒装","M20",
  head("Full Inversion","地点副词开头：完全倒装","here & there") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">Here / There 开头</span><span class="en">verb before subject</span></div>
        <span class="ex-line"><span class="tgt">Here comes</span> the bus.<span class="ex-gl">地点副词开头 → 动词放主语前面</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Here the bus comes.</em> → 正常语序要倒过来：comes the bus。</div></div>""" +
      mp("Here ___ the bus.","come / comes","✔ <em>comes</em> — 主语是 the bus（三单），动词跟主语一致。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主语是代词不倒装</span><span class="en">pronoun例外</span></div>
        <span class="ex-line">Here <span class="tgt">he comes</span>.<span class="ex-gl">主语是代词 → 语序不倒</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">Here/There 开头：主语是<b>名词</b>才倒装（Here comes the bus），是<b>代词</b>不倒（Here he comes）。</div></div>""" +
      mp("Here ___ .","comes she / she comes","✔ <em>she comes</em> — 主语是代词，不倒装。") + """
      </div>
    </div>
  </div>""")

PILOT["m15-inv-negative"] = slide("m15-inv-negative","dark","M20 · 部分倒装","M20",
  head("Partial Inversion","否定词开头：助动词提前","never / hardly") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">否定副词开头</span><span class="en">never have I</span></div>
        <span class="ex-line"><span class="tgt">Never have I</span> seen such a thing.<span class="ex-gl">Never / Seldom / Hardly 开头 → 助动词提到主语前</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Never I have seen.</em> → 否定词开头必须倒装：have 提前。</div></div>""" +
      mp("Never ___ I seen such a thing.","have / had","✔ <em>have</em> — 现在完成时倒装：have 提到主语前。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">Only + 状语开头</span><span class="en">only then</span></div>
        <span class="ex-line"><span class="tgt">Only then did</span> I understand.<span class="ex-gl">Only + 状语开头 → 借助 did / do / does 倒装</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Only then I understood.</em> → did 提前，动词还原过去式。</div></div>""" +
      mp("Only then ___ he realize it.","did / does","✔ <em>did</em> — 过去的事情，倒装借 did。") + """
      </div>
    </div>
  </div>""")

PILOT["m15-inv-so"] = slide("m15-inv-so","light","M20 · So / Neither 倒装","M20",
  head("So / Neither","我也一样：so / neither 倒装","me too") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">So do I</span><span class="en">so + aux + subject</span></div>
        <span class="ex-line">— I like tea. — <span class="tgt">So do I</span>.<span class="ex-gl">「我也是」→ So + 助动词 + 主语</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>So I do.</em>（意思变成「我确实如此」）→ 表「我也是」必须 So do I。</div></div>""" +
      mp("— I like tea. — ___ do I.","So / Neither","✔ <em>So</em> — 前句肯定，表「我也是」用 So。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">Neither do I</span><span class="en">neither + aux + subject</span></div>
        <span class="ex-line">— I don&rsquo;t smoke. — <span class="tgt">Neither do I</span>.<span class="ex-gl">「我也不」→ Neither + 助动词 + 主语</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">助动词跟前句走：前句有 be 用 be，有情态用情态，一般动词借 do / does / did。</div></div>""" +
      mp("— He can swim. — So ___ I.","can / do","✔ <em>can</em> — 前句有情态 can，回答照搬 can。") + """
      </div>
    </div>
  </div>""")

PILOT["m15-inv-practice"] = slide("m15-inv-practice","dark","M20 · 练习","M20",
  head("Quick Practice · 倒一倒","练一练：把语序倒过来","invert it", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的一项 · Pick the right one</div>
      <div class="p-q"><span class="qnum">1.</span>Never ______ such a beautiful place.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>have I seen</em> — 否定词开头，助动词 have 提前。</span></div>
      <div class="p-q"><span class="qnum">2.</span>Here ______ . Look!<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>comes the bus</em> — 主语是名词，完全倒装。</span></div>
      <div class="p-q"><span class="qnum">3.</span>— I have finished it. — ______ .<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>So have I</em> — 前句有 have，回答照搬 have。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Only in this way ______ progress.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>can we make</em> — Only + 状语开头，情态动词 can 提前。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">两类倒装记住：<b>否定词 / Only + 状语</b> 开头 → 助动词提前（部分倒装）；<b>Here / There</b> 开头且主语是名词 → 动词提前（完全倒装）。</div>
    </div>""")

# ------------------------------------------------------------------
# 5m) M21 强调句（Emphasis）— 4 pages
# ------------------------------------------------------------------
PILOT["m16-emp-cleft"] = slide("m16-emp-cleft","dark","M21 · It is...that","M21",
  head("It is &hellip; that","强调句：把重点抬到台前","cleft sentence") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">公式</span><span class="en">it is/was + 被强调 + that</span></div>
        <span class="ex-line">I met Tom yesterday. &rarr; <span class="tgt">It was Tom that</span> I met yesterday.<span class="ex-gl">把想强调的部分放进 It is/was &hellip; that 中间</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">强调<b>人</b>可用 who，强调<b>物 / 时间 / 地点</b>一律用 that。</div></div>""" +
      mp("It was Tom ___ broke the window.","who / which","✔ <em>who</em> — 强调的是人 Tom，用 who（that 也可）。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">检验方法</span><span class="en">remove and check</span></div>
        <span class="ex-line">去掉 <span class="tgt">It was &hellip; that</span>，剩下的仍是完整句<span class="ex-gl">It was Tom that I met → I met Tom ✔ 是强调句</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">强调过去的事用 <b>It was</b>，现在的事用 <b>It is</b>，时态只看 is/was。</div></div>""" +
      mp("It ___ Tom that I met yesterday.","is / was","✔ <em>was</em> — met 是过去发生的事，用 It was。") + """
      </div>
    </div>
  </div>""")

PILOT["m16-emp-that"] = slide("m16-emp-that","light","M21 · 强调时间 / 地点","M21",
  head("Still That","强调时间地点：还是 that","not when / where") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">强调时间用 that</span><span class="en">not when</span></div>
        <span class="ex-line">It was yesterday <span class="tgt">that</span> I met him.<span class="ex-gl">强调句里时间也用 that，不用 when</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>It was yesterday when I met him.</em> → 强调句一律 that（人可用 who）。</div></div>""" +
      mp("It was yesterday ___ I met him.","when / that","✔ <em>that</em> — 强调句结构固定 It be + 部分 + that。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">强调 not until</span><span class="en">it was not until</span></div>
        <span class="ex-line">It was not until midnight <span class="tgt">that</span> he came back.<span class="ex-gl">「直到半夜才回来」放进强调句型</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">强调 not until 时，not until 留在 It be 后面，从句用<b>肯定式</b>（he came back）。</div></div>""" +
      mp("It was not until 6 o&rsquo;clock ___ he got up.","that / when","✔ <em>that</em> — not until 的强调句仍用 that。") + """
      </div>
    </div>
  </div>""")

PILOT["m16-emp-do"] = slide("m16-emp-do","dark","M21 · do 强调谓语","M21",
  head("Do / Does / Did","强调谓语动词：加 do","emphatic do") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">do 放动词前</span><span class="en">he does like it</span></div>
        <span class="ex-line">He <span class="tgt">does</span> like music.<span class="ex-gl">「真的喜欢」→ 动词前加 do / does / did</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">do 后动词用原形：✘ <em>He did liked it.</em> → ✔ <em>He did like it.</em></div></div>""" +
      mp("He ___ like music.","does / do","✔ <em>does</em> — 主语 he 是三单，借 does。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">两种强调分工</span><span class="en">which one to use</span></div>
        <span class="ex-line">强调<b>名词 / 时间 / 地点</b> &rarr; It is&hellip;that<br>强调<b>动词</b> &rarr; 加 do / does / did<span class="ex-gl">It was Tom that I met. / He did come.</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">只有一般现在时和一般过去时的动词能加 do 强调；进行时、完成时不行。</div></div>""" +
      mp("I ___ finish it yesterday.","do / did","✔ <em>did</em> — yesterday 提示过去，强调借 did。") + """
      </div>
    </div>
  </div>""")

PILOT["m16-emp-practice"] = slide("m16-emp-practice","light","M21 · 练习","M21",
  head("Quick Practice · 强调一下","练一练：把重点抬出来","emphasize it", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的一项 · Pick the right one</div>
      <div class="p-q"><span class="qnum">1.</span>It was in the park ______ we met.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>that</em> — 强调地点也用 that，不用 where。</span></div>
      <div class="p-q"><span class="qnum">2.</span>It ______ John and Mary who helped me.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>was</em> — 强调句 It be 用单数形式（习惯用法）。</span></div>
      <div class="p-q"><span class="qnum">3.</span>He ______ come yesterday.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>did</em> — 强调过去的谓语动词，借 did + 原形。</span></div>
      <div class="p-q"><span class="qnum">4.</span>It was not until he came ______ we started.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>that</em> — not until 的强调句：It was not until &hellip; that &hellip;</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">强调句只认一个架子：<b>It is / was + 被强调 + that</b>（人可换 who）；去掉架子句子还完整才是强调句；强调动词改用 do / does / did。</div>
    </div>""")

# ------------------------------------------------------------------
# 5n) M22 省略句（Ellipsis）— 4 pages
# ------------------------------------------------------------------
PILOT["m17-ell-clause"] = slide("m17-ell-clause","light","M22 · 状语从句的省略","M22",
  head("Clause Ellipsis","从句省略：doing / done 顶上","while walking") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主从句主语一致才能省</span><span class="en">same subject</span></div>
        <span class="ex-line"><span class="tgt">While (I was) walking</span>, I met him.<span class="ex-gl">从句主语与主句相同 + be 动词 → 一起省掉</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">主语不一致不能省：✘ <em>While reading, the phone rang.</em>（ring 的不是 reading 的人）</div></div>""" +
      mp("While ___ in Beijing, I met him.","traveling / traveled","✔ <em>traveling</em> — 主语 I 与 travel 是主动关系，用 doing。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">被动用 done</span><span class="en">if caught</span></div>
        <span class="ex-line"><span class="tgt">If caught</span>, he will be punished.<span class="ex-gl">「如果被抓住」→ 被动关系用 done</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">省略后的形式看主语和动词的关系：主动用 <b>doing</b>，被动用 <b>done</b>，将来用 <b>to do</b>。</div></div>""" +
      mp("If ___ more time, I would do it better.","given / giving","✔ <em>given</em> — 「被给」是被动关系，用 done。") + """
      </div>
    </div>
  </div>""")

PILOT["m17-ell-to"] = slide("m17-ell-to","dark","M22 · 不定式的省略","M22",
  head("To or Not","使役感官动词后省 to","make him go") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">make / let / see 后省 to</span><span class="en">bare infinitive</span></div>
        <span class="ex-line">The teacher made him <span class="tgt">read</span> the text.<span class="ex-gl">使役 / 感官动词 + 宾语 + 动词原形</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>made him to read</em> → make / let / have / see / hear 后省 to。</div></div>""" +
      mp("I saw him ___ the street.","cross / to cross","✔ <em>cross</em> — see 是感官动词，后接原形。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">变被动 to 回来</span><span class="en">be made to do</span></div>
        <span class="ex-line">He was made <span class="tgt">to read</span> the text.<span class="ex-gl">变被动语态后，省掉的 to 要补回来</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">省 to 的家族：使役 <b>make / let / have</b> + 感官 <b>see / hear / watch / feel</b>。唯独变被动时 make 后 to 回来。</div></div>""" +
      mp("He was made ___ all night.","work / to work","✔ <em>to work</em> — 被动语态里 to 补回来。") + """
      </div>
    </div>
  </div>""")

PILOT["m17-ell-other"] = slide("m17-ell-other","light","M22 · 常见省略","M22",
  head("Common Omission","常见省略场合","daily omissions") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">不定式保留 to</span><span class="en">keep the to</span></div>
        <span class="ex-line">— Will you come? — I&rsquo;d like <span class="tgt">to</span>.<span class="ex-gl">重复的不定式只留 to，动词省掉</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I&rsquo;d like come.</em> → to 不能丢，省的只是后面的动词。</div></div>""" +
      mp("— Will you join us? — I&rsquo;d love ___ .","to / do","✔ <em>to</em> — 不定式省略保留 to。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">比较句的省略</span><span class="en">than 后的省略</span></div>
        <span class="ex-line">He is taller than <span class="tgt">I (am)</span>.<span class="ex-gl">than / as 后面与前面重复的部分可省</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">省略的原则：<b>删掉后意思不变、句子能还原</b>就省；还原不了就别省。</div></div>""" +
      mp("She sings as well as her sister ___ .","does / do","✔ <em>does</em> — 补出的助动词跟主语 sister（三单）一致。") + """
      </div>
    </div>
  </div>""")

PILOT["m17-ell-practice"] = slide("m17-ell-practice","dark","M22 · 练习","M22",
  head("Quick Practice · 省一省","练一练：省对地方","omit right", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的一项 · Pick the right one</div>
      <div class="p-q"><span class="qnum">1.</span>While ______ football, he hurt his leg.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>playing</em> — 主语一致 + 主动关系，省略成 doing。</span></div>
      <div class="p-q"><span class="qnum">2.</span>The boss made them ______ twelve hours a day.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>work</em> — make 后接不带 to 的不定式。</span></div>
      <div class="p-q"><span class="qnum">3.</span>— Would you like to swim? — I&rsquo;d like ______ .<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>to</em> — 不定式省略保留 to。</span></div>
      <div class="p-q"><span class="qnum">4.</span>If ______ , water can be turned into ice.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>cooled</em> — 水是「被冷却」，被动用 done。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">省略两步自查：① 主从句<b>主语一致</b>才能省；② 主语与动词<b>主动 doing、被动 done</b>。make / let / 感官动词后接原形，变被动 to 回来。</div>
    </div>""")

# ------------------------------------------------------------------
# 5o) M23 连词与并列（Conjunctions & Coordination）— 4 pages
# ------------------------------------------------------------------
PILOT["m18-conj-basic"] = slide("m18-conj-basic","dark","M23 · 四大并列连词","M23",
  head("And / But / Or","并列连词：and · but · or · so","the big four") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">or 表「否则」</span><span class="en">or = otherwise</span></div>
        <span class="ex-line">Hurry up, <span class="tgt">or</span> you will be late.<span class="ex-gl">「赶快，否则迟到」→ or 表转折警告</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">and 并列 / but 转折 / or 否则 / so 结果，各管一摊别混用。</div></div>""" +
      mp("Hurry up, ___ you will miss the bus.","or / and","✔ <em>or</em> — 「否则赶不上」表警告。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">并列结构要对称</span><span class="en">parallel structure</span></div>
        <span class="ex-line">He likes <span class="tgt">swimming and fishing</span>.<span class="ex-gl">and 两边形式要一致：都 doing 或都 to do</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He likes swimming and to fish.</em> → 改成 swimming and fishing 对称。</div></div>""" +
      mp("She can sing and ___ .","dance / dancing","✔ <em>dance</em> — and 前后都是动词原形，对称。") + """
      </div>
    </div>
  </div>""")

PILOT["m18-conj-both"] = slide("m18-conj-both","light","M23 · both / either / neither","M23",
  head("Both &hellip; and","both · either · neither 的搭档","paired conjunctions") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">三组固定搭档</span><span class="en">fixed pairs</span></div>
        <span class="ex-line"><span class="tgt">Both</span> Tom <span class="tgt">and</span> Jerry are here.<span class="ex-gl">both&hellip;and 两个都；either&hellip;or 二选一；neither&hellip;nor 两个都不</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">搭档不能拆混：✘ <em>both &hellip; or</em> / ✘ <em>neither &hellip; or</em> → and 配 both，nor 配 neither。</div></div>""" +
      mp("Neither he ___ I know it.","nor / or","✔ <em>nor</em> — neither 必须搭配 nor。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">either&hellip;or 表「要么」</span><span class="en">either A or B</span></div>
        <span class="ex-line"><span class="tgt">Either</span> you <span class="tgt">or</span> he must go.<span class="ex-gl">「要么你去，要么他去」→ 动词跟最近的主语（就近）</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">both&hellip;and 永远复数；either&hellip;or / neither&hellip;nor 谓语<b>就近</b>（复习 M18）。</div></div>""" +
      mp("Either you or he ___ wrong.","is / are","✔ <em>is</em> — 就近原则：离动词最近的是 he。") + """
      </div>
    </div>
  </div>""")

PILOT["m18-conj-subordinate"] = slide("m18-conj-subordinate","dark","M23 · 并列 vs 从属","M23",
  head("Coordination","并列连词 vs 从属连词","two families") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">两族连词</span><span class="en">two families</span></div>
        <span class="ex-line">He is rich, <span class="tgt">but</span> he is not happy.<span class="ex-gl">并列：and/but/or/so 连接对等的句子；从属：because/although/when 引导从句</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">从属连词不能和并列连词配对：✘ <em>Because&hellip;, so&hellip;</em> / ✘ <em>Although&hellip;, but&hellip;</em></div></div>""" +
      mp("He is rich, ___ he is not happy.","but / so","✔ <em>but</em> — 前后是转折关系。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">选词看逻辑</span><span class="en">logic first</span></div>
        <span class="ex-line"><span class="tgt">Because</span> he was ill, he stayed home.<span class="ex-gl">因果 because · 转折 but / although · 时间 when · 条件 if</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">做题先问「前后是什么关系」：因果、转折、时间、条件——关系定了，连词就定了。</div></div>""" +
      mp("___ he was ill, he stayed home.","Because / Although","✔ <em>Because</em> — 生病和待在家是因果关系。") + """
      </div>
    </div>
  </div>""")

PILOT["m18-conj-practice"] = slide("m18-conj-practice","light","M23 · 练习","M23",
  head("Quick Practice · 连一连","练一练：选对连词","pick the conjunction", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的连词 · Pick the right conjunction</div>
      <div class="p-q"><span class="qnum">1.</span>Study hard, ______ you will fail.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>or</em> — 「否则会不及格」表警告。</span></div>
      <div class="p-q"><span class="qnum">2.</span>______ he ______ I agree with you.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>Neither &hellip; nor</em> — 「他和我都不同意」，固定搭档。</span></div>
      <div class="p-q"><span class="qnum">3.</span>He is poor ______ happy.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>but</em> — 穷和快乐是转折关系。</span></div>
      <div class="p-q"><span class="qnum">4.</span>______ it was late, they kept working.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>Although</em> — 让步关系，且不与 but 连用。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">先定<b>逻辑关系</b>再选连词：并列 and / 转折 but / 否则 or / 结果 so；固定搭档不拆混（both&hellip;and、either&hellip;or、neither&hellip;nor）。</div>
    </div>""")

# ------------------------------------------------------------------
# 5p) M27 高频易错点（Common Mistakes）— 4 pages
# ------------------------------------------------------------------
PILOT["m19-err-nouns"] = slide("m19-err-nouns","light","M27 · 冠词与单复数","M27",
  head("Countable?","名词类老坑：可数与不可数","count or not") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">不可数不加 s</span><span class="en">no plural form</span></div>
        <span class="ex-line">She gave me some <span class="tgt">advice</span>.<span class="ex-gl">advice / information / homework 都不可数</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>many homeworks</em> → ✔ <em>much / a lot of homework</em></div></div>""" +
      mp("She gave me some ___ .","advice / advices","✔ <em>advice</em> — advice 不可数，没有复数。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">a / an / the 别漏</span><span class="en">missing article</span></div>
        <span class="ex-line">He is <span class="tgt">a</span> student of <span class="tgt">an</span> English school.<span class="ex-gl">单数可数名词前必须有冠词或限定词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He is student.</em> → 单数可数名词裸用是错的，补 a。</div></div>""" +
      mp("She is ___ honest girl.","a / an","✔ <em>an</em> — honest 的 h 不发音，以元音音素开头。") + """
      </div>
    </div>
  </div>""")

PILOT["m19-err-verbs"] = slide("m19-err-verbs","dark","M27 · 动词类老坑","M27",
  head("Verb Traps","动词类老坑","三单 · 双谓语 · there be") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">there be 不是 there have</span><span class="en">there be only</span></div>
        <span class="ex-line"><span class="tgt">There is</span> a book on the desk.<span class="ex-gl">「有」用 there be；be 后才是名词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>There have many people.</em> → ✔ <em>There are many people.</em></div></div>""" +
      mp("There ___ a book on the desk.","is / have","✔ <em>is</em> — there be 句型，跟最近主语一致。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">一句只有一个谓语</span><span class="en">no double verb</span></div>
        <span class="ex-line">If he <span class="tgt">comes</span>, I will tell him.<span class="ex-gl">从句和主句各一个谓语，靠连词连接</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He said he is tired was true.</em> → 没有连词的堆叠是错的；两句要用 that / and 连。</div></div>""" +
      mp("Although he is tired, ___ he keeps going.","but / 不填","✔ <em>不填</em> — although 与 but 不能连用（呼应 M17）。") + """
      </div>
    </div>
  </div>""")

PILOT["m19-err-word"] = slide("m19-err-word","light","M27 · 汉语直译坑","M27",
  head("Chinglish","汉语直译坑：别把中文搬进英文","word order") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">very 不修饰动词</span><span class="en">not "I very like"</span></div>
        <span class="ex-line">I like English <span class="tgt">very much</span>.<span class="ex-gl">「我很喜欢」→ like it very much / really like</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I very like English.</em> → very 只修饰形容词副词，动词用 very much。</div></div>""" +
      mp("I ___ like English.","very / really","✔ <em>really</em> — very 不能直接修饰动词。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">「我的英语说不好」</span><span class="en">subject check</span></div>
        <span class="ex-line">I don&rsquo;t speak English <span class="tgt">well</span>.<span class="ex-gl">主语是「我」不是「我的英语」</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>My English speaks poorly.</em> → 先找对主语：是人「说」语言。</div></div>""" +
      mp("___ speak English well.","My sister / My sister's","✔ <em>My sister</em> — 主语要用「人」，不能用所有格。") + """
      </div>
    </div>
  </div>""")

PILOT["m19-err-practice"] = slide("m19-err-practice","dark","M27 · 练习","M27",
  head("Quick Practice · 避坑测试","练一练：找出正确说法","spot the right one", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">选出正确的说法 · Pick the right one</div>
      <div class="p-q"><span class="qnum">1.</span>He gave me many useful ______ .<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>suggestions</em> — suggestion 可数；advice 不可数。</span></div>
      <div class="p-q"><span class="qnum">2.</span>______ forty students in our class.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>There are</em> — 「有」用 there be，不用 there have。</span></div>
      <div class="p-q"><span class="qnum">3.</span>He is a student, ______ he works very hard.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>and</em> — 并列关系；一句一个连词，不与 although/because 连用。</span></div>
      <div class="p-q"><span class="qnum">4.</span>The weather in Beijing is colder than ______ in Guangzhou.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>that</em> — that 代替 the weather，避免重复。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">避坑口诀 · Shortcut</div>
      <div class="m-body">四大老坑自查：① 不可数名词不加 s；② 单数可数名词不裸用；③ there be 不是 there have；④ very 不修饰动词、从属连词不配对。</div>
    </div>""")

# ------------------------------------------------------------------
# 5q) M28 题型速览（Exam Question Types）— 4 pages
# ------------------------------------------------------------------
PILOT["m20-exam-mcq"] = slide("m20-exam-mcq","dark","M28 · 单选题步骤","M28",
  head("Multiple Choice","单选题：先找信号词","find the signal") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">三步法</span><span class="en">3-step method</span></div>
        <span class="ex-line">If it ___ tomorrow, we&rsquo;ll stay home.<span class="ex-gl">① 找信号词 if ② 套规则主将从现 ③ 选一般现在时</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别只靠语感：先定「考什么语法点」，再套本课件的对应口诀。</div></div>""" +
      mp("见到 than，想到 ___ 。","比较级 / 最高级","✔ <em>比较级</em> — than 是比较级的信号词。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">信号词速查</span><span class="en">signal words</span></div>
        <span class="ex-line">yesterday &rarr; 过去时 &middot; since &rarr; 完成时<span class="ex-gl">if / when &rarr; 主将从现 · than &rarr; 比较级 · the + 名词后从句 &rarr; 定语从句</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">信号词是题目的「标签」：看到它就知道这题在考哪个模块。</div></div>""" +
      mp("I have lived here ___ 2020.","since / for","✔ <em>since</em> — since + 时间点，完成时的信号词。") + """
      </div>
    </div>
  </div>""")

PILOT["m20-exam-cloze"] = slide("m20-exam-cloze","light","M28 · 完形与填空","M28",
  head("Cloze &amp; Blanks","完形与填空：上下文定答案","context first") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">先通读再下笔</span><span class="en">read through</span></div>
        <span class="ex-line">He was tired, <span class="tgt">so/because</span> &hellip; 看前后句<span class="ex-gl">完形考逻辑：前后是因果、转折还是并列</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">别只看空格所在句：答案常常藏在前一句或后一句。</div></div>""" +
      mp("He was tired, ___ he slept.","so / because","✔ <em>so</em> — 前因后果（呼应 M17）。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">语法填空看功能</span><span class="en">what does the blank do</span></div>
        <span class="ex-line">She is good at <span class="tgt">swimming</span>.<span class="ex-gl">介词后填 doing；缺主语填 what / who；缺限定词填 a / the</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">先问「这个空在句子里当什么成分」，成分定了，形式就定了。</div></div>""" +
      mp("It is no use ___ about it.","to complain / complaining","✔ <em>complaining</em> — It is no use doing 固定句型。") + """
      </div>
    </div>
  </div>""")

PILOT["m20-exam-trans"] = slide("m20-exam-trans","dark","M28 · 改错与翻译","M28",
  head("Correct &amp; Translate","改错与翻译：先抓主干","backbone first") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">改错查四处</span><span class="en">4 checkpoints</span></div>
        <span class="ex-line">主谓一致 &middot; 时态 &middot; 连词重复 &middot; 冠词<span class="ex-gl">He don&rsquo;t like it. → doesn&rsquo;t（三单）</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">看到 because 找 so、看到 although 找 but——重复连词是最高频改错点。</div></div>""" +
      mp("He don&rsquo;t like it. 改：___","don&rsquo;t &rarr; doesn&rsquo;t","✔ <em>doesn&rsquo;t</em> — 主语 he 是三单。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">翻译先找主干</span><span class="en">S + V + O first</span></div>
        <span class="ex-line">「如果你努力学习，你就会成功。」<span class="ex-gl">先搭 If you work hard, you will succeed. 再润色</span></span>
        <div class="mist"><div class="m-label">判定口诀 · Shortcut</div><div class="m-body">翻译三步：① 定句型（if 条件？that 从句？）② 落口诀（主将从现）③ 查时态与三单。</div></div>""" +
      mp("翻译「如果明天下雨,我就不去」用 ___ 时。","will rain / rains","✔ <em>rains</em> — 主将从现，从句用一般现在时。") + """
      </div>
    </div>
  </div>""")

PILOT["m20-exam-practice"] = slide("m20-exam-practice","light","M28 · 练习","M28",
  head("Quick Practice · 全真演练","练一练：综合小测","mixed drill", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">综合题 · Mixed drill</div>
      <div class="p-q"><span class="qnum">1.</span>By the time he arrived, the film ______ already ______ .<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>had started</em> — 「过去的过去」用过去完成时（呼应 M09）。</span></div>
      <div class="p-q"><span class="qnum">2.</span>This is the museum ______ we visited last year.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>which / that</em> — visit 缺宾语，用 which（呼应 M16）。</span></div>
      <div class="p-q"><span class="qnum">3.</span>If I ______ you, I would take the chance.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>were</em> — 与现在相反的虚拟，be 一律 were（呼应 M13）。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Only in this way ______ our English.<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>can we improve</em> — Only + 状语开头，部分倒装（呼应 M20）。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">课程收束 · Wrap-up</div>
      <div class="m-body">20 个模块讲完了。回到<b>目录</b>随时重讲任一模块；每页口诀已内置，考前把各模块的「判定口诀」过一遍即可。</div>
    </div>""")

# order of pilot slides per module (first in list = right after its divider)
def pilot_for(mid):
    return {
        "m1-parts-of-speech":  ["m1-pos-overview","m1-pos-content-words","m1-pos-content-words-b","m1-pos-function-words","m1-pos-function-words-b","m1-pos-practice"],
        "m3-five-patterns":    ["m3-patterns-overview","m3-patterns-svc-svo","m3-patterns-svooc","m3-patterns-practice"],
        "m5-tenses":           ["m5-tense-overview","m5-tense-present","m5-tense-past","m5-tense-future","m5-tense-perfect","m5-tense-practice"],
        "m6-modal-verbs":      ["m6-modal-can","m6-modal-must","m6-modal-should","m6-modal-practice"],
        "m7-passive-voice":    ["m7-passive-core","m7-passive-tenses","m7-passive-transform","m7-passive-practice"],
        "m8-non-finite-verbs": ["m8-nonfinite-gerund","m8-nonfinite-infinitive","m8-nonfinite-stop","m8-nonfinite-done","m8-nonfinite-practice"],
        "m9-subjunctive":      ["m9-subjunctive-if","m9-subjunctive-past","m9-subjunctive-wish","m9-subjunctive-practice"],
        "m10-noun-clauses":    ["m10-nc-overview","m10-nc-order","m10-nc-formal","m10-nc-practice"],
        "m11-attribute-clauses":["m11-rel-overview","m11-rel-that","m11-rel-where","m11-rel-practice"],
        "m12-adverbial-clauses":["m12-adv-overview","m12-adv-cause","m12-adv-until","m12-adv-practice"],
        "m13-agreement":       ["m13-agr-overview","m13-agr-plural","m13-agr-nearby","m13-agr-practice"],
        "m14-comparison":      ["m14-comp-forms","m14-comp-than","m14-comp-super","m14-comp-practice"],
        "m15-inversion":       ["m15-inv-full","m15-inv-negative","m15-inv-so","m15-inv-practice"],
        "m16-emphasis":        ["m16-emp-cleft","m16-emp-that","m16-emp-do","m16-emp-practice"],
        "m17-ellipsis":        ["m17-ell-clause","m17-ell-to","m17-ell-other","m17-ell-practice"],
        "m18-conjunctions":    ["m18-conj-basic","m18-conj-both","m18-conj-subordinate","m18-conj-practice"],
    "m19-common-mistakes": ["m19-err-nouns","m19-err-verbs","m19-err-word","m19-err-practice"],
    "m20-exam-types":      ["m20-exam-mcq","m20-exam-cloze","m20-exam-trans","m20-exam-practice"],
    "m2-sentence-elements":["m2-elem-subj-pred","m2-elem-obj-pred","m2-elem-attrib-adverb","m2-elem-practice"],
    "m4-there-be":         ["m4-therebe-basic","m4-therebe-neg","m4-therebe-tense","m4-therebe-practice"],
    "m5-nouns":            ["m5-noun-count","m5-noun-plural","m5-noun-poss","m5-noun-practice"],
    "m6-articles":         ["m6-art-aan","m6-art-the","m6-art-zero","m6-art-practice"],
    "m7-pronouns":         ["m7-pron-personal","m7-pron-possessive","m7-pron-indefinite","m7-pron-practice"],
    "m4-sentence-types":   ["m8-type-simple","m8-type-compound","m8-type-complex","m8-type-practice"],
    "m14-reported-speech": ["m14-rep-statement","m14-rep-changes","m14-rep-questions","m14-rep-practice"],
    "pos-verbs":           ["pos-verbs-kinds","pos-verbs-forms","pos-verbs-transitive","pos-verbs-practice"],
    "pos-adjectives":      ["pos-adj-position","pos-adj-order","pos-adj-ed-ing","pos-adj-practice"],
    "pos-adverbs":         ["pos-adv-kinds","pos-adv-formation","pos-adv-position","pos-adv-practice"],
    "pos-numerals":        ["pos-num-cardinal","pos-num-ordinal","pos-num-usage","pos-num-practice"],
    "m24-prepositions":    ["m24-prep-time","m24-prep-place","m24-prep-fixed","m24-prep-practice"],
    "m25-questions":       ["m25-ques-yesno","m25-ques-wh","m25-ques-tag","m25-ques-practice"],
    "m26-punctuation":     ["m26-punct-basic","m26-punct-apos","m26-punct-caps","m26-punct-practice"],
    }.get(mid, [])

# ------------------------------------------------------------------
# 6) Cover + Contents
# ------------------------------------------------------------------
def cover():
    return """<section class="slide hero dark" data-slide-id="cover">
  <div class="chrome"><div>English Grammar · 英语语法</div><div>M01–M32 · NN / TOTAL</div></div>
  <div class="frame" style="display:grid; gap:4vh; align-content:center; min-height:80vh">
    <div class="kicker" data-anim>Bilingual Grammar Guide · 双语精讲</div>
    <h1 class="h-hero" style="font-size:9vw" data-anim>英语语法</h1>
    <h2 class="h-sub" data-anim>English Grammar · 高职英语语法双语讲义</h2>
    <p class="lead" style="max-width:60vw" data-anim>
      一套完整、系统的语法知识地图 —— 从词性、时态到从句与句型，逐点给规则、给例句、给常见错误与练习。
      点下方进入目录，即可跳到想讲的模块，随时回来接着讲。
    </p>
    <div class="meta-row" data-anim>
      <button type="button" data-goto="contents" style="all:unset;cursor:pointer;font-family:var(--serif-zh);font-weight:600;font-size:max(16px,min(1.4vw,2.49vh));border-bottom:1px solid currentColor;padding-bottom:6px">进入目录 · Contents &rarr;</button>
      <span>·</span><span>32 模块 · M01–M32</span>
    </div>
    <div style="font-family:var(--mono);font-size:max(12px,min(0.9vw,1.60vh));letter-spacing:.14em;opacity:.78" data-anim>作者 · Adam Wang &middot; 英语教师 &middot; arikimizord@163.com</div>
  </div>
  <div class="foot"><div>一套能当「教材」翻的语法课</div><div>— 2026 —</div></div>
</section>"""

def contents():
    groups = []
    for part in (PART1, PART2, PART3, PART4, PART5):
        ms = [m for m in MODULES if m[4] == part]
        if ms: groups.append((part, ms))
    def part_col(part, ms):
        cells = ""
        for mm in ms:
            cells += (
                f'<button type="button" data-goto="{mm[0]}" class="toc-row">'
                f'<span class="toc-code">{mm[1]}</span>'
                f'<span class="toc-cn">{mm[2]}</span>'
                f'<span class="toc-en">{mm[3]}</span>'
                f'</button>'
            )
        pnum, pcn, pen = part
        return f"""<div style="min-width:0">
          <div class="kicker" style="margin-bottom:.25vh">Part {pnum} · {pen} · {pcn}</div>
          {cells}
        </div>"""
    left = part_col(*groups[0])
    mid = part_col(*groups[1]) + part_col(*groups[2])
    right = part_col(*groups[3]) + part_col(*groups[4])
    return f"""<section class="slide hero light" data-slide-id="contents">
  <div class="chrome"><div>English Grammar · 英语语法</div><div>目录 · NN / TOTAL</div></div>
  <div class="frame" style="display:flex; flex-direction:column">
    <div class="kicker" data-anim>Contents · 目录</div>
    <h2 class="h-xl" style="white-space:nowrap;font-size:min(4.5vw,8vh)" data-anim>轻轻一点，去哪一章</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8vh 2.2vw;align-content:start;flex:1;min-height:0;margin-top:.6vh">{left}{mid}{right}</div>
  </div>
  <div class="ip-brand"><span class="lwa-text">Learn with Adam</span><span class="lwa-dot"></span></div>
  <div class="foot"><div>目录 · Contents</div><div>⌂ 首页随时回去</div></div>
</section>"""

# ------------------------------------------------------------------
# 6b) content fragments (content/*.py) -- exec'd with helpers in scope,
#     BEFORE assembly so PILOT is complete when order is built
# ------------------------------------------------------------------
def N(id, title, section, minutes, purpose, talk, transition="接下来进入下一部分，逐步推进。"):
    d = {"id": id, "title": title, "section": section, "minutes": minutes,
         "purpose": purpose, "talk": talk, "transition": transition}
    return d

import glob as _glob
FRAG_NOTES = []
for _f in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "*.py"))):
    exec(compile(open(_f, encoding="utf-8").read(), _f, "exec"), globals())
    FRAG_NOTES.extend(globals().get("NOTES_FRAG", []))

# ------------------------------------------------------------------
# 7) Assemble all slides in order
# ------------------------------------------------------------------
order = []  # list of (slide_id, html)
order.append(("cover", cover()))
order.append(("contents", contents()))
for m in MODULES:
    mid = m[0]
    order.append((mid, divider(mid)))
    for pid in pilot_for(mid):
        order.append((pid, PILOT[pid]))

# insert nav-back cluster as fixed overlay (not a slide)
nav_back = """<div id="nav-back">
  <button type="button" data-goto="cover"><i data-lucide="home" class="ico-sm"></i>首页</button>
  <button type="button" data-goto="contents"><i data-lucide="book-open" class="ico-sm"></i>目录</button>
</div>"""

# number the slides
num_pages = len(order)
slides_html = []
for i, (sid, h) in enumerate(order, start=1):
    slides_html.append(h.replace("NN", f"{i:02d}").replace("TOTAL", str(num_pages)))
SLIDES_BODY = "\n\n".join(slides_html)

# ------------------------------------------------------------------
# 8) SPEAKER_NOTES (double-quoted strings: dodges apostrophe gotcha)
# ------------------------------------------------------------------
import json
NOTES = [
    N("cover","封面 · Cover","导览",0.5,
      "让老师点入目录，了解这是一套可以按模块跳讲的完整语法地图。",
      ["点「进入目录」演示跳转","说明 28 个模块、可随时回来","强调这套课件是长期授课用的知识地图"],
      transition="进入目录页，建立 5 大部分的全貌。"),
    N("contents","目录 · Contents","导览",0.5,
      "建立全貌：5 大部分 28 模块，方便按需点讲、随时续讲。",
      ["按 Part 依次介绍","可现场演示点击跳到某个模块","提示右下角首页/目录按钮随时可用"],
      transition="从最短的模块「词性」讲起，一切句法的地基。"),
    N("m1-parts-of-speech","词性 · 模块开篇","句子基础 · 词性",2.0,
      "用幕封定调：这章解决“一个词是干什么用的”这个根基问题。",
      ["点目录跳入说明多模块结构","预告本章 9 大词性","让学生在脑中挂一张词性清单"],
      transition="先看总览，9 大词性一次排开。"),
    N("m1-pos-overview","9 大词性总览","句子基础 · 词性",3.0,
      "让学生一眼看见 9 大词性的各自职责，建立整体框架。",
      ["逐个念词性 + 中文含义","强调：先认身份，句子才排得动","指出多数英文单词兼有多重词性"],
      transition="概览之后，逐个看扛起含义的实词。"),
    N("m1-pos-content-words","实词 · 名词动词","句子基础 · 词性",2.5,
      "聚焦承载含义的实词先讲名词与动词，用常见错误点破易错处。",
      ["名词:可数不可数规则","动词:第三人称单数 -es","预告动词的及物/不及物将支撑句型"],
      transition="再看负责「修饰」的两类实词：形容词与副词。"),
    N("m1-pos-content-words-b","实词 · 形容词副词","句子基础 · 词性",2.5,
      "讲清修饰关系：形容词管名词，副词管动作，-ly 是分水岭。",
      ["形容词位置:名词前或 be 后","副词常由 adj + -ly 变来","点 Aha! 前先让学生口头选择"],
      transition="含义靠实词，结构靠虚词——接着看虚词。"),
    N("m1-pos-function-words","虚词 · 冠词介词连词","句子基础 · 词性",2.5,
      "讲清小词如何把句子粘起来：冠词、介词、连词各自管什么。",
      ["讲 the 的特指 vs a/an 泛指","运动/三餐不带 the","连词 but / because 表转折还是因果"],
      transition="再看负责「代替」与「数数」的两类虚词：代词与数词。"),
    N("m1-pos-function-words-b","虚词 · 代词数词","句子基础 · 词性",2.5,
      "讲清代词的格与数词的基数/序数之分，都是中国学生高频错点。",
      ["主语用主格: Lily and I","mine = my book,后面不带名词","「第几」用序数词并加 the"],
      transition="用一组选词填空收束本章，立刻练手。"),
    N("m1-pos-practice","词性 · 练一练","句子基础 · 词性",2.0,
      "用选词填空及时巩固；答案默认隐藏，点「Aha! 答案揭晓」逐题显示答案与解析。",
      ["先让学生口头作答,再点 Aha! 揭晓","每题都点出判断依据(词性/格/词形)","口诀收尾:be 之后常接形容词"],
      transition="词性有了身份，下一章把句子拆成零件——句子成分。"),
    N("m2-sentence-elements","句子成分 · 模块开篇","句子基础 · 句子成分",2.0,
      "幕封定位：这章把句子拆成零件，为五种句型做铺垫。",
      ["预告：下一章用这些零件搭句型","说明主语/谓语/宾语/定语/状语各司其职","提醒词性决定能当什么成分"],
      transition="零件备齐，直接进入全书最核心的五种基本句型。"),
    N("m3-five-patterns","五种基本句型 · 模块开篇","句子基础 · 句型",2.0,
      "给出 5 种骨架，是全书最核心的地基。",
      ["强调：长句都是这 5 种长出","预告 SV/SVC/SVO/SVOO/SVOC","鼓励学生背熟这句型表"],
      transition="先看五种骨架同时排开的完整图景。"),
    N("m3-patterns-overview","五句型总览","句子基础 · 句型",3.0,
      "立即给出 5 种骨架，配合符号让学生有抓手。",
      ["建立符号表格:SV 主谓,SVC 主系表…","强调 O 与 C 的区别","用一个例句对应每种骨架"],
      transition="最常用的两种骨架先行细讲：主系表与主谓宾。"),
    N("m3-patterns-svc-svo","主系表 · 主谓宾","句子基础 · 句型",3.0,
      "最常用的两种骨架，给出系动词清单与及物/不及物区分。",
      ["系动词后接形容词(常见错误)","不及物动词不接宾(常见错误)","逐个核对 be/look/feel/seem"],
      transition="再看带两个宾语的骨架。"),
    N("m3-patterns-svooc","主谓双宾 · 主谓宾宾补","句子基础 · 句型",3.0,
      "讲清两个宾语的骨架以及宾语+补语的区别。",
      ["SVOO 可换写成 to/for 结构","SVOC 中补语补充的是宾语","强调 SVOC 里宾语与补语是一体"],
      transition="用判定题收尾，检测骨架掌握。"),
    N("m3-patterns-practice","句型 · 练一练","句子基础 · 句型",2.0,
      "用判定题收尾；答案默认隐藏，点「Aha! 答案揭晓」逐题显示句型与依据。",
      ["先让学生口头判定,再点 Aha! 揭晓","逐题说明判定依据(双宾/系表/宾补)","预告五种句型是整本书的地基，务必牢固"],
      transition="再到句型的种类：简单句、并列句、复合句。"),
    N("m5-tense-overview","时态 · 十二时态地图","动词系统 · 时态",3.0,
      "不逐个背 12 个时态，先建立「3 时间 × 4 体貌」的地图，剩下的都是组合。",
      ["横着念时间:过去/现在/将来","竖着念体貌:一般/进行/完成/完成进行","每张卡配一道 Aha! 练习,现场点揭晓"],
      transition="先讲用得最多的现在双时态。"),
    N("m5-tense-present","时态 · 一般现在 / 现在进行","动词系统 · 时态",3.0,
      "一般现在管习惯与事实,现在进行管此刻正在做;两大高频错点是三单 -s 和漏 be。",
      ["先让学生口头选择再点 Aha!","强调 Look!/Listen! 是进行时的信号词","板书动词第三人称单数变化规则"],
      transition="把时间轴拨回昨天:过去双时态。"),
    N("m5-tense-past","时态 · 一般过去 / 过去进行","动词系统 · 时态",3.0,
      "一般过去用动词过去式,过去进行是过去某刻的背景动作;did 后必须还原原形。",
      ["yesterday/last/ago 三类信号词","when 引导的背景句常配过去进行","点破 Did you went? 这类叠加过去式错误"],
      transition="再往将来看:will 与 be going to 两种说法。"),
    N("m5-tense-future","时态 · 一般将来","动词系统 · 时态",2.5,
      "will 偏临时决定与预测,be going to 偏早有计划;两者的共同错点是动词形不对。",
      ["will 后永远接原形","be going to 前别漏 be 动词","让学生各自造一个周末计划句"],
      transition="最后攻最难的完成时态。"),
    N("m5-tense-perfect","时态 · 现在完成 / 过去完成","动词系统 · 时态",3.5,
      "现在完成强调对现在的影响,过去完成是「过去的过去」;since/for 是现在完成的信号。",
      ["对比 saw yesterday 与 have seen 的差别","过去完成必须有两个过去时间做参照","点 Aha! 前先问学生哪件事先发生"],
      transition="用四道填空收束本章。"),
    N("m5-tense-practice","时态 · 练一练","动词系统 · 时态",3.0,
      "四道动词填空覆盖四个核心时态;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生写下答案再逐题揭晓","每题追问判断依据是哪个信号词","总结:先找信号词,词形跟着走"],
      transition="时态之后,看给动词加「态度」的情态动词。"),
    N("m6-modal-can","情态 · can / may","动词系统 · 情态动词",3.0,
      "can 管能力与请求, may 管许可与可能;核心错点是情态动词后误加三单或 to。",
      ["先练 can swim 这类搭配再点 Aha!","对比 Can I 与 May I 的礼貌程度","提醒 could 是 can 的过去式也更委婉"],
      transition="再看语气最强的 must 与它的客观版 have to。"),
    N("m6-modal-must","情态 · must / have to","动词系统 · 情态动词",3.0,
      "must 主观必须且永不变形, have to 客观必须且随人称时态变化;mustn't 是禁止不是不必。",
      ["红灯例子讲 must 的强制性","三单场景对比 has to 与 must","重点点破 mustn't 与 don't have to 的区别"],
      transition="语气缓和下来:给建议的 should。"),
    N("m6-modal-should","情态 · should / had better","动词系统 · 情态动词",2.5,
      "should 是常规建议, had better 带警告意味;共同错点是后接 to 或漏掉 'd 缩写。",
      ["看医生例子引出 should","had better 强调不做会有坏结果","让学生用 should 给同桌提一条建议"],
      transition="用四道选词填空收束本章。"),
    N("m6-modal-practice","情态 · 练一练","动词系统 · 情态动词",2.5,
      "四道选词填空覆盖许可/能力/禁止/建议;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生举手选再揭晓","第 3 题重点追问 mustn't 与 don't have to","总结口诀:不加 -s 不加 to"],
      transition="情态之后,换一个视角看动词:被动语态。"),
    N("m7-passive-core","被动 · be + 过去分词","动词系统 · 被动语态",3.0,
      "被动语态只有一个公式 be + done;主语是动作的承受者时才用。",
      ["用 is spoken / is grown 两个例子立公式","点破漏 be 的常见错误","问学生:谁是「被做」的那一个?"],
      transition="被动也要分时态,变化全在 be 上。"),
    N("m7-passive-tenses","被动 · 被动的时态","动词系统 · 被动语态",3.0,
      "时态只压在 be 上:is/was/will be + done;情态动词后必须带 be。",
      ["三句对照:is cleaned / was built / will be finished","情态被动 can be done 别丢 be","让学生齐读公式:变时态、变 be、done 不动"],
      transition="学会把主动句改造成被动句。"),
    N("m7-passive-transform","被动 · 主动变被动","动词系统 · 被动语态",3.0,
      "三步口诀:宾语提前、be+done、by 短语;不及物动词没有被动。",
      ["现场把 Tom cleans the room 改三步","点破 was happened 这类错误","说明 by 短语什么时候省略"],
      transition="用四道填空收束本章。"),
    N("m7-passive-practice","被动 · 练一练","动词系统 · 被动语态",2.5,
      "四道被动填空覆盖现在/过去/情态被动;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生写再逐题揭晓","追问每题的时态信号词","总结:时态改 be,done 不动"],
      transition="下一个模块:动词的三个分身,非谓语动词。"),
    N("m8-nonfinite-gerund","非谓语 · doing","动词系统 · 非谓语动词",3.0,
      "doing 的两个岗位:跟在 enjoy/finish/mind 后,或自己当主语、紧跟介词。",
      ["enjoy reading 立固定搭配","介词后一律 doing:good at swimming","让学生说出自己的 enjoy + doing 爱好"],
      transition="第二个分身:to do。"),
    N("m8-nonfinite-infinitive","非谓语 · to do","动词系统 · 非谓语动词",3.0,
      "to do 跟在 want/decide/hope 后,也能表「为了」的目的。",
      ["want to go 立公式","目的句 to catch the bus","对比上一页:哪些词接 doing 哪些接 to do"],
      transition="第三个分身最容易混:stop doing 与 stop to do。"),
    N("m8-nonfinite-stop","非谓语 · stop 辨析","动词系统 · 非谓语动词",3.0,
      "stop doing 停止手头的事, stop to do 停下来去做另一件事;一字之差意思相反。",
      ["戒烟与停下抽烟两例对照","延伸 remember/forget 的同款辨析","考试高频,让学生把两句抄进笔记"],
      transition="第三个分身:done。"),
    N("m8-nonfinite-done","非谓语 · done","动词系统 · 非谓语动词",2.5,
      "过去分词修饰名词表被动;boring/bored 分清「令人…」与「感到…」。",
      ["broken window 立被动概念","boring(物)/bored(人)成对记","点破 I am boring 的笑话记忆点"],
      transition="用四道填空收束本章。"),
    N("m8-nonfinite-practice","非谓语 · 练一练","动词系统 · 非谓语动词",2.5,
      "四道形式填空覆盖 doing/to do/forget to do/boring;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","追问每题前面的「信号词」","总结口诀:看前面的词定形式"],
      transition="动词系统最后一个模块:虚拟语气。"),
    N("m9-subjunctive-if","虚拟 · 与现在相反","动词系统 · 虚拟语气",3.0,
      "与现在事实相反:if + 过去式,主句 would do;be 动词一律 were。",
      ["If I were you 立标杆","对比真实条件与虚拟条件两句","点破:时态退一步只为表虚拟"],
      transition="再退一步:与过去相反。"),
    N("m9-subjunctive-past","虚拟 · 与过去相反","动词系统 · 虚拟语气",3.0,
      "与过去事实相反:if + had done,主句 would have done;主句的 have 别丢。",
      ["赶车例子:早知道就…","退一步/退两步对照表","学生常错 would caught,重点纠正"],
      transition="wish 后面也要退。"),
    N("m9-subjunctive-wish","虚拟 · wish 的虚拟","动词系统 · 虚拟语气",2.5,
      "wish 表不能实现的愿望:与现在相反用 did/were,与过去相反用 had done。",
      ["I wish I were taller 立公式","后悔句 had studied","提醒 wish 后绝不用现在时"],
      transition="用四道填空收束动词系统。"),
    N("m9-subjunctive-practice","虚拟 · 练一练","动词系统 · 虚拟语气",2.5,
      "四道填空覆盖 were/had done/wish;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","第 2、4 题追问是哪一档虚拟","总结:虚拟=时态往回退"],
      transition="Part Ⅱ 动词系统完成,进入 Part Ⅲ 从句。"),
    N("m10-nc-overview","从句 · 引导词 that / what","从句系统 · 名词性从句",3.0,
      "名词性从句开头:先分清 that 与 what——从句缺成分用 what,不缺用 that。",
      ["用 I know that he is right 立标杆","what = the thing that 既引导又作成分","让学生判断几个从句缺不缺成分"],
      transition="最常用的宾语从句:语序与时态两条规则。"),
    N("m10-nc-order","从句 · 宾语从句语序","从句系统 · 名词性从句",3.0,
      "宾语从句两条铁律:一律陈述语序;主句过去时从句跟着过去。",
      ["对比 where does he live 与 where he lives","时态后移:He said he was busy","客观真理例外:light travels fast"],
      transition="主语从句太长怎么办:It 顶位与 whether 的专场。"),
    N("m10-nc-formal","从句 · whether 与形式主语","从句系统 · 名词性从句",3.0,
      "It 作形式主语顶住长从句;「是否」在句首、介词后、or not 前只用 whether。",
      ["It is clear that 立结构","whether 三场合口诀","让学生造一句 It depends on whether"],
      transition="用四道选择收束本章。"),
    N("m10-nc-practice","从句 · 练一练","从句系统 · 名词性从句",2.5,
      "四道引导词选择覆盖 that/where/what/whether;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生说缺不缺成分再揭晓","第 2 题顺带提醒陈述语序","总结:缺什么补什么,不缺用 that"],
      transition="下一个模块:定语从句,跑到名词后面的形容词。"),
    N("m11-rel-overview","定语 · 先行词与关系词","从句系统 · 定语从句",3.0,
      "定语从句总览:从句紧跟名词后当形容词;who 指人 which 指物。",
      ["The book that I bought 立结构","点破 bought it 重复宾语错误","who/which 二分让学生抢答"],
      transition="几个只能用 that 的特殊场合。"),
    N("m11-rel-that","定语 · 只能用 that","从句系统 · 定语从句",2.5,
      "最高级、序数词、all、anything 后只能用 that;whose 表「某人的」。",
      ["the best film that 立规则","All that glitters 谚语记忆","whose 顶替 his 的替换演示"],
      transition="先行词是时间和地点时用 where / when。"),
    N("m11-rel-where","定语 · where / when","从句系统 · 定语从句",3.0,
      "从句不缺主宾只缺状语时用 where / when;判断看先行词加缺什么。",
      ["the town where I was born 立例","对比 the town which I like 缺宾语","两步判断法带学生过一遍"],
      transition="用四道关系词选择收束本章。"),
    N("m11-rel-practice","定语 · 练一练","从句系统 · 定语从句",2.5,
      "四道关系词选择覆盖 who/that/when/whose;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先问先行词是什么再揭晓","追问从句缺主语宾语还是状语","总结两步判断法"],
      transition="下一个模块:状语从句,说明时间条件原因的副词性从句。"),
    N("m12-adv-overview","状语 · 连词地图","从句系统 · 状语从句",3.0,
      "状语从句总览:when/if/because/although 四类连词;核心铁律主将从现。",
      ["When he came, I was cooking 立例","主将从现重点敲黑板","让学生齐读 if it rains, I will stay"],
      transition="原因与让步:中式连用是重灾区。"),
    N("m12-adv-cause","状语 · 原因与让步","从句系统 · 状语从句",2.5,
      "because 不配 so,although 不配 but——一个句子只用一个连词。",
      ["点破 Because..., so... 中式连用","although 与 but 同理","让学生翻译「虽然累但坚持」"],
      transition="until 的两种用法:一直等到与直到才。"),
    N("m12-adv-until","状语 · until","从句系统 · 状语从句",2.5,
      "肯定句 until 表持续到某时;not...until 表「直到…才」。",
      ["I waited until he came","He didn't leave until I came 对照","提醒 until 从句同样主将从现"],
      transition="用四道连词选择收束本章。"),
    N("m12-adv-practice","状语 · 练一练","从句系统 · 状语从句",2.5,
      "四道连词选择覆盖主将从现/although/until/so;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","第 1 题再敲一次主将从现","总结两条铁律"],
      transition="从句系统最后一站:主谓一致。"),
    N("m13-agr-overview","一致 · 三单与不可数","从句系统 · 主谓一致",3.0,
      "主谓一致开篇:三单加 s 与不可数名词当单数。",
      ["He likes music 立标杆","news/maths 当单数","点破漏 s 最高频错误"],
      transition="天生复数词与 both/either 的分工。"),
    N("m13-agr-plural","一致 · 复数主语","从句系统 · 主谓一致",2.5,
      "people/police 天生复数;both 配复数、either/neither 配单数。",
      ["Many people are here","both/either 对照记","neither of + 单数纠正"],
      transition="就近与就远两条原则。"),
    N("m13-agr-nearby","一致 · 就近与就远","从句系统 · 主谓一致",3.0,
      "either...or 类就近,with 类就远——动词到底跟谁走。",
      ["Neither he nor I am 立例","with his students 不算人数","对比两条原则让学生区分"],
      transition="用四道动词选择收束本章与 Part Ⅲ。"),
    N("m13-agr-practice","一致 · 练一练","从句系统 · 主谓一致",2.5,
      "四道动词选择覆盖 maths/neither/就近/就远;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生找真正的主语再揭晓","第 3、4 题追问就近还是就远","总结:先抓真正的主语"],
      transition="Part Ⅲ 从句系统完成,进入 Part Ⅳ 特殊结构。"),
    N("m14-comp-forms","比较 · 比较级构成","特殊结构 · 比较等级",3.0,
      "比较级构成:短词加 -er,长词前加 more;双写与改 y 两条拼写规则。",
      ["taller / more useful 二分","bigger 双写、happier 改 y","点破 more bigger 重复错误"],
      transition="比较级句型:much 修饰与越…越…。"),
    N("m14-comp-than","比较 · 比较级句型","特殊结构 · 比较等级",3.0,
      "比较级前用 much / even 加强,不用 very;「the + 比较级, the + 比较级」表越…越…。",
      ["much taller 不是 very taller","The more, the better 立结构","两个 the 都不能丢"],
      transition="最高级:the 别丢,in / of 分范围。"),
    N("m14-comp-super","比较 · 最高级","特殊结构 · 比较等级",2.5,
      "最高级 the + -est / most;in + 大范围,of + 同类;est 与 most 不叠加。",
      ["the tallest in our class","of the three 同类比较","点破 the most easiest"],
      transition="用四道形式选择收束本章。"),
    N("m14-comp-practice","比较 · 练一练","特殊结构 · 比较等级",2.5,
      "四道题覆盖比较级/双写/最高级/越越结构;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先让学生说规则再揭晓","第 2 题追问双写规则","总结口诀"],
      transition="下一个模块:倒装句,倒过来更有劲。"),
    N("m15-inv-full","倒装 · 完全倒装","特殊结构 · 倒装句",2.5,
      "Here / There 开头且主语是名词时,动词放到主语前;主语是代词不倒装。",
      ["Here comes the bus 立标杆","Here he comes 代词例外","让学生念熟节奏"],
      transition="否定词开头的部分倒装,考试更高频。"),
    N("m15-inv-negative","倒装 · 部分倒装","特殊结构 · 倒装句",3.0,
      "Never / Seldom / Hardly 或 Only + 状语开头,助动词提到主语前。",
      ["Never have I seen 立结构","Only then did I understand","点破 Never I have seen 语序错误"],
      transition="对话里最常用的 So / Neither 倒装。"),
    N("m15-inv-so","倒装 · So / Neither","特殊结构 · 倒装句",2.5,
      "「我也是」So do I,「我也不」Neither do I;助动词跟前句走。",
      ["I like tea — So do I","前句有情态照搬情态","区分 So I do 的不同意思"],
      transition="用四道倒装题收束本章。"),
    N("m15-inv-practice","倒装 · 练一练","特殊结构 · 倒装句",2.5,
      "四道题覆盖否定倒装/完全倒装/So have I/Only 倒装;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","追问是完全倒装还是部分倒装","总结两类倒装"],
      transition="下一个模块:强调句,把重点抬到台前。"),
    N("m16-emp-cleft","强调 · It is...that","特殊结构 · 强调句",3.0,
      "强调句公式:It is/was + 被强调 + that;强调人可用 who;去掉架子句子要完整。",
      ["I met Tom 变强调句演示","去掉 It was…that 检验法","时态只看 is / was"],
      transition="强调时间地点也用 that,不用 when。"),
    N("m16-emp-that","强调 · 时间地点","特殊结构 · 强调句",2.5,
      "强调句里时间、地点一律用 that;not until 放进强调句后从句用肯定式。",
      ["It was yesterday that 立例","not until 强调句拆解","点破 when 的误用"],
      transition="强调谓语动词用 do / does / did。"),
    N("m16-emp-do","强调 · do 强调","特殊结构 · 强调句",2.5,
      "强调谓语动词:动词前加 do / does / did,后接原形;只用于一般现在时与过去时。",
      ["He does like music 立例","did like 原形纠正","两种强调的分工表"],
      transition="用四道强调题收束本章。"),
    N("m16-emp-practice","强调 · 练一练","特殊结构 · 强调句",2.5,
      "四道题覆盖 that/It was/did 强调/not until 强调;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","第 1 题强调地点仍用 that","总结强调句唯一架子"],
      transition="下一个模块:省略句,能省则省。"),
    N("m17-ell-clause","省略 · 从句省略","特殊结构 · 省略句",3.0,
      "状语从句省略:主从句主语一致时,连词后用 doing(主动)/ done(被动)。",
      ["While walking, I met him 立例","While reading, the phone rang 反例","主动 doing 被动 done"],
      transition="使役感官动词后省 to。"),
    N("m17-ell-to","省略 · 省略 to","特殊结构 · 省略句",2.5,
      "make / let / have 与 see / hear 等后接不带 to 的不定式;变被动时 to 回来。",
      ["made him read 立例","be made to work 被动补 to","背省 to 家族名单"],
      transition="常见的 to 保留与比较句省略。"),
    N("m17-ell-other","省略 · 常见省略","特殊结构 · 省略句",2.5,
      "不定式省略保留 to;than / as 后重复部分可省;省略标准是能还原。",
      ["I&rsquo;d love to 立例","taller than I (am)","省略两步自查法"],
      transition="用四道省略题收束本章。"),
    N("m17-ell-practice","省略 · 练一练","特殊结构 · 省略句",2.5,
      "四道题覆盖 doing 省略/make 后原形/保留 to/被动 done;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","追问主动还是被动","总结省略两步自查"],
      transition="下一个模块:连词与并列,把句子粘起来。"),
    N("m18-conj-basic","连词 · 四大并列","特殊结构 · 连词与并列",2.5,
      "and / but / or / so 四大并列连词;or 表「否则」;并列结构前后要对称。",
      ["Hurry up, or 立例","对称:swimming and fishing","四个连词各管一摊"],
      transition="both / either / neither 三组固定搭档。"),
    N("m18-conj-both","连词 · 固定搭档","特殊结构 · 连词与并列",2.5,
      "both…and / either…or / neither…nor 三组搭档不拆混;谓语就近呼应 M18。",
      ["Both Tom and Jerry are here","Neither…nor 搭档配对","either…or 就近原则复习"],
      transition="并列连词与从属连词两族对照。"),
    N("m18-conj-subordinate","连词 · 并列与从属","特殊结构 · 连词与并列",2.5,
      "并列连词连接对等句子,从属连词引导从句;从属连词不与 so / but 配对。",
      ["He is rich, but 立例","because 与 so 不并用的呼应","先定关系再选连词"],
      transition="用四道连词选择收束本章与 Part Ⅳ。"),
    N("m18-conj-practice","连词 · 练一练","特殊结构 · 连词与并列",2.5,
      "四道题覆盖 or/neither…nor/but/although;答案默认隐藏,点「Aha! 答案揭晓」逐题显示。",
      ["先写后揭晓","第 1 题追问 or 的含义","总结:先定逻辑关系"],
      transition="Part Ⅳ 特殊结构完成,进入 Part Ⅴ 实战应用。"),
    N("m19-err-nouns","易错点 · 名词类老坑","实战应用 · 高频易错点",2.5,
      "不可数名词不加 s;单数可数名词前不能裸用,必须有冠词或限定词。中国学生受汉语「不可数」概念影响最深。",
      ["advice / homework 立例","✘ many homeworks 纠错","a / an honest girl 的音素判断"],
      transition="从名词转向动词类老坑。"),
    N("m19-err-verbs","易错点 · 动词类老坑","实战应用 · 高频易错点",2.5,
      "「有」用 there be 不是 there have;一句只有一个谓语,两句话要靠连词连接;although 不配 but(呼应 M17)。",
      ["✘ There have 纠错","一句一个谓语原理解释","Although 不填 but 追问"],
      transition="下一个老坑:汉语直译。"),
    N("m19-err-word","易错点 · 汉语直译坑","实战应用 · 高频易错点",2.5,
      "very 不能直接修饰动词,要用 very much / really;造句先找对主语,「我的英语说不好」主语是「我」。",
      ["✘ I very like 纠错","✘ My English speaks poorly 纠错","主语要用「人」的追问"],
      transition="用四道避坑题收束本章。"),
    N("m19-err-practice","易错点 · 练一练","实战应用 · 高频易错点",2.5,
      "四道题覆盖可数性/there be/连词/that 替代;答案默认隐藏,点「Aha! 答案揭晓」逐题显示;末尾四大老坑自查口诀。",
      ["先写后揭晓","第 4 题追问 that 代替了什么","总结四大老坑自查清单"],
      transition="最后一个模块:题型速览,讲考试怎么用这些知识。"),
    N("m20-exam-mcq","题型 · 单选题步骤","实战应用 · 题型速览",2.5,
      "单选三步法:找信号词→套规则→验证;信号词速查表(yesterday→过去时, since→完成时, than→比较级, if/when→主将从现)。",
      ["If it rains 立例三步演示","信号词速查带读","since 2020 追问 for 的区别"],
      transition="完形与语法填空的套路。"),
    N("m20-exam-cloze","题型 · 完形与填空","实战应用 · 题型速览",2.5,
      "完形先通读,答案常藏在前一句;语法填空先判断空格的句子成分,成分定形式;It is no use doing 固定句型。",
      ["so/because 逻辑判断演示","成分分析三问","no use doing 追问"],
      transition="改错与翻译的抓手。"),
    N("m20-exam-trans","题型 · 改错与翻译","实战应用 · 题型速览",2.5,
      "改错四处自查:主谓一致/时态/连词重复/冠词;翻译三步:定句型→落口诀→查时态三单。",
      ["He don&rsquo;t 纠错演示","翻译主干先行示例","主将从现翻译追问"],
      transition="用四道综合题收束全课。"),
    N("m20-exam-practice","题型 · 综合小测","实战应用 · 题型速览",3.0,
      "四道综合题回扣 M09/M16/M13/M20 四个模块,检验全课贯通;末尾收束语引导回目录复讲。",
      ["先写后揭晓","逐题点出对应模块","引导回目录复习"],
      transition="全课完成,鼓励学生用目录页自主复习。"),
]
NOTES.extend(FRAG_NOTES)
for m in MODULES:
    mid = m[0]
    if mid not in {"m1-parts-of-speech","m2-sentence-elements","m3-five-patterns"}:
        code, cn, en, part, theme, tag = MODULES_by_id[mid][1:]
        pnum, pcn, pen = part
        NOTES.append(N(mid, f"{cn} · 模块开篇", pcn, 2.0,
                       f"幕封定位：第{pnum}部分「{pcn}」的过渡与铺垫。",
                       [f"展示章节名与副标 {en}", "预示本章核心语法点", "点明这一模块在整张语法地图里的位置"]))
NOTES.sort(key=lambda n: [i for i,(sid,_) in enumerate(order) if sid==n["id"]][0])

notes_js = "const SPEAKER_NOTES = " + json.dumps(NOTES, ensure_ascii=False, indent=2) + ";\nwindow.__SPEAKER_NOTES__ = SPEAKER_NOTES;"
html = re.sub(r"\nconst SPEAKER_NOTES = \[[\s\S]*?\];\nwindow\.__SPEAKER_NOTES__ = SPEAKER_NOTES;", "\n" + notes_js, html, count=1)

# ------------------------------------------------------------------
# 9) Insert slides + nav cluster + lucide create
# ------------------------------------------------------------------
html = html.replace("<!-- SLIDES_HERE -->", SLIDES_BODY, 1)

open(OUT, "w", encoding="utf-8").write(html)

# stats
n_slides = num_pages
n_notes = len(NOTES)
n_anim = SLIDES_BODY.count("data-anim")
print(f"wrote {OUT}")
print(f"slides: {n_slides} | notes: {n_notes} | data-anim count: {n_anim}")