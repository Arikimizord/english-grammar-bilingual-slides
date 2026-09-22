# -*- coding: utf-8 -*-
# content/verbs.py —— M05 动词（词法层面：分类 · 形式 · 及物性，4 页）

PILOT["pos-verbs-kinds"] = slide("pos-verbs-kinds","light","M05 · 动词的分类","M05",
  head("Verb Kinds · 动词的四大家族","动词的分类","notional · linking · auxiliary · modal") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">实义动词</span><span class="en">vt / vi</span></div>
        <span class="ex-line">I <span class="tgt">bought</span> a new phone last week.<span class="ex-gl">及物动词 vt：后面直接跟宾语</span></span>
        <span class="ex-line">She <span class="tgt">listens to</span> music after class.<span class="ex-gl">不及物动词 vi：要借介词 to 接宾语</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>listen the music</em> → ✔ <em>listen to the music</em>（listen 是 vi，不能直接带宾语）</div></div>
        <div class="mini-p">""" + mp("He ___ the radio every morning.","listens to / listens","✔ <em>listens to</em> — listen 是不及物动词，接 the radio 要先加 to。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">系 · 助 · 情态</span><span class="en">linking · auxiliary · modal</span></div>
        <span class="ex-line">The milk <span class="tgt">seems</span> sour.<span class="ex-gl">系动词：后接形容词说明主语</span></span>
        <span class="ex-line"><span class="tgt">Do</span> you like tea? You <span class="tgt">must</span> try it.<span class="ex-gl">助动词帮造句，情态动词表态度</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He cans swim.</em> → ✔ <em>He can swim.</em>（情态动词后一律接动词原形）</div></div>
        <div class="mini-p">""" + mp("She ___ be at home; the light is on.","must / musts","✔ <em>must</em> — 情态动词没有人称变化，第三人称也不加 s。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-verbs-forms"] = slide("pos-verbs-forms","dark","M05 · 动词的五种形式","M05",
  head("Five Forms · 一个动词，五副面孔","动词的五种基本形式","do · does · did · done · doing") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">五种基本形式</span><span class="en">the five forms</span></div>
        <span class="ex-line">do → <span class="tgt">does</span> → <span class="tgt">did</span> → <span class="tgt">done</span> → <span class="tgt">doing</span><span class="ex-gl">原形 · 三单 · 过去式 · 过去分词 · 现在分词</span></span>
        <span class="ex-line">watch → <span class="tgt">watches</span>; study → <span class="tgt">studies</span><span class="ex-gl">三单：ch/sh 加 es，辅音字母+y 变 ies</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He go to school by bike.</em> → ✔ <em>He goes to school</em>（主语三单，动词要跟着变三单）</div></div>
        <div class="mini-p">""" + mp("My mom ___ TV every evening.","watchs / watches","✔ <em>watches</em> — watch 结尾是 ch，三单加 es 不加 s。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">去 e 与双写</span><span class="en">-ing / -ed spelling</span></div>
        <span class="ex-line">write → <span class="tgt">writing</span>; take → <span class="tgt">taking</span><span class="ex-gl">词尾不发音的 e，先去掉再加 ing</span></span>
        <span class="ex-line">stop → <span class="tgt">stopped / stopping</span>; run → <span class="tgt">running</span><span class="ex-gl">重读闭音节：末尾辅音双写再加</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>stoped / runing</em> → ✔ <em>stopped / running</em>（双写是这类词的必经工序）</div></div>
        <div class="mini-p">""" + mp("She is ___ a letter now.","writeing / writing","✔ <em>writing</em> — write 去 e 再加 ing，没有 writeing 这种写法。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-verbs-transitive"] = slide("pos-verbs-transitive","light","M05 · 及物 · 不及物 · 系动词","M05",
  head("Transitive or Not · 后面怎么接","及物 · 不及物 · 系动词","vt · vi · linking verbs") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">及物 vs 不及物</span><span class="en">vt · vi</span></div>
        <span class="ex-line">She <span class="tgt">sent</span> me a photo of the party.<span class="ex-gl">及物动词直接接宾语，中间不隔介词</span></span>
        <span class="ex-line">We waited <span class="tgt">for</span> the bus for half an hour.<span class="ex-gl">wait 是 vi，等「什么」要靠 for</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>We discussed about the plan.</em> → ✔ <em>discussed the plan</em>（discuss 是 vt，本身就带宾语）</div></div>
        <div class="mini-p">""" + mp("They arrived ___ the airport.","at / to","✔ <em>at</em> — arrive 是不及物动词，接小地点用 arrive at。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">系动词接形容词</span><span class="en">linking verbs</span></div>
        <span class="ex-line">The soup <span class="tgt">smells</span> good.<span class="ex-gl">smell 后接形容词作表语，说明「汤」</span></span>
        <span class="ex-line">He <span class="tgt">became</span> a nurse after graduation.<span class="ex-gl">become 后接名词，表语说明主语身份</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I feel badly about it.</em> → ✔ <em>I feel bad</em>（feel 是系动词，后接形容词不用副词）</div></div>
        <div class="mini-p">""" + mp("The flowers smell ___.","sweetly / sweet","✔ <em>sweet</em> — smell 是系动词，后接形容词作表语。") + """</div>
      </div>
    </div>
  </div>
  <div class="mist" style="margin-top:1vh" data-anim>
    <div class="m-label">延伸 · Where Next</div>
    <div class="m-body">动词是英语句子的心脏：时态、语态、语气三大系统，见 M16–M20。</div>
  </div>""")

PILOT["pos-verbs-practice"] = slide("pos-verbs-practice","dark","M05 · 练习","M05",
  head("Quick Practice · 动词四连测","分类 · 形式 · 及物","choose the right form", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">单句填空 · 从括号里选对的那个词</div>
      <div class="p-q"><span class="qnum">1.</span>___ you often play basketball after class?（Do / Are）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>Do</em> — 一般疑问句用助动词 do 开头，主语 you 配 Do。</span></div>
      <div class="p-q"><span class="qnum">2.</span>He ___ his homework before dinner.（finishes / finishs）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>finishes</em> — 结尾是 sh，三单加 es；没有 finishs 这种写法。</span></div>
      <div class="p-q"><span class="qnum">3.</span>We finally arrived ___ the museum.（at / to）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>at</em> — arrive 是不及物动词，接小地点用 arrive at。</span></div>
      <div class="p-q"><span class="qnum">4.</span>The milk smells ___. Please throw it away.（strange / strangely）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>strange</em> — smell 是系动词，后接形容词作表语。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">vt 直接带宾，vi 借介词；系动词后跟形容词；拼写记三招：变 y、去 e、双写。</div>
    </div>""")

NOTES_FRAG = [
    N("pos-verbs-kinds","动词 · 分类","Ⅰ 词法篇 · 动词",2.5,
      "把动词分成实义、系、助、情态四类，让学生拿到动词先问「它在句子里干什么活」。",
      ["开场问一句：一个英语句子里最不能少的词是什么？把「动词是心脏」的印象先立住。",
       "用 bought a new phone 立住 vt 直接带宾语，再用 listen to music 对比 vi 要借介词。",
       "讲助动词和情态动词时强调它们「不表动作、只帮语法」：do 帮忙提问，can/must 表态度。",
       "敲一遍高频错点：情态动词后接原形、不加 s——He can swims 是作文里的常客。"],
      "分完了工种，接下来看同一个动词上岗前要换的五副「工装」——动词的五种基本形式。"),
    N("pos-verbs-forms","动词 · 五种基本形式","Ⅰ 词法篇 · 动词",2.5,
      "记住动词五种形式的名字，并掌握三单 -s 与现在分词 -ing 的拼写规则（去 e、双写）。",
      ["用 do 这一个词把五种形式走一遍：do/does/did/done/doing，先认脸，再谈用途。",
       "三单拼写抓词尾：ch/sh 加 es、辅音字母加 y 变 ies，可让学生当场拼 watches、studies。",
       "去 e 用 write→writing 现场演示，双写用 stop→stopped 敲「重读闭音节末尾辅音双写」。",
       "提醒：这一页只认形式、不讲时态——什么时候用哪种形式，是 M16 时态模块的事。"],
      "形式会拼了，接下来解决一个更实际的问题：动词后面到底能不能直接跟东西。"),
    N("pos-verbs-transitive","动词 · 及物 · 不及物 · 系动词","Ⅰ 词法篇 · 动词",2.5,
      "分清及物、不及物与系动词三种「接法」：后接宾语、介词短语还是形容词作表语。",
      ["用 sent me a photo 说明 vt 直接带宾语；waited for the bus 说明 vi 要借介词 for。",
       "discussed about 是「多此一举」型错误，正好和 listen the music 的「缺介词」型凑成一对。",
       "系动词家族用「闻、尝、变」串记：smell/taste/become 后面都接形容词作表语。",
       "最后指一下底部延伸条：时态、语态、语气在 M16–M20 展开，这里先把词法地基打牢。"],
      "接法也过了，来做四道题，把分类、拼写、介词、表语一次验收。"),
    N("pos-verbs-practice","动词 · 练习","Ⅰ 词法篇 · 动词",2.0,
      "用四道题覆盖助动词提问、三单拼写、不及物动词加介词、系动词接形容词四个考点。",
      ["第 1 题带全班齐读一遍 Do you often play...，让助动词开头变成肌肉记忆。",
       "第 2 题和第 4 题是一对：一个考词尾 es 的拼写，一个考系动词后要用形容词。",
       "第 3 题可以让学生再举一个 vi 加介词的搭配，比如 look at、listen to、wait for。",
       "带读口诀收尾：vt 直接带宾，vi 借介词；系动词后跟形容词；拼写三招：变 y、去 e、双写。"],
      "动词是词法里最大的一族，骨架已经立住；词法篇的下一站，去看给名词当「化妆师」的形容词。"),
]
