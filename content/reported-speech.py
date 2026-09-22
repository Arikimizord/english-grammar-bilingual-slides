# -*- coding: utf-8 -*-
# content/reported-speech.py —— M14 间接引语（Reported Speech）

PILOT["m14-rep-statement"] = slide("m14-rep-statement", "dark", "M14 · 陈述句转述", "M14",
  head("Reported Speech · 把『别人的话』转给别人听", "陈述句转述", "say → said + (that) + 陈述语序") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">直接引语 → 间接引语</span><span class="en">direct → reported</span></div>
        <span class="ex-line">He said, &ldquo;I am busy.&rdquo; → He said <span class="tgt">(that) he was busy</span>.<span class="ex-gl">去引号，加 that，人称时态一起变</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ He said he <em>is</em> busy. → ✔ He said he <em>was</em> busy.（主句过去时，从句没跟着退）</div></div>
        """ + mp("I am tired. → He said he ___ tired.", "am / was", "✔ <em>was</em> — said 是过去时，am 退成 was。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">时态整体后移</span><span class="en">backshift</span></div>
        <span class="ex-line"><span class="tgt">am/is → was</span> · are → were · will → would · can → could<span class="ex-gl">现在往前退一格，变成过去</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ She said she <em>will</em> come. → ✔ she <em>would</em> come.（will 也要退成 would）</div></div>
        """ + mp("I can swim. → She said she ___ swim.", "can / could", "✔ <em>could</em> — can 整体退一格，变 could。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-rep-changes"] = slide("m14-rep-changes", "light", "M14 · 人称与时间地点变化", "M14",
  head("Change of View · 跟着转述人换视角", "人称与时间地点也要变", "I → he/she · today → that day") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">人称跟着换</span><span class="en">pronouns</span></div>
        <span class="ex-line">She said, &ldquo;My phone is dead.&rdquo; → She said <span class="tgt">her</span> phone was dead.<span class="ex-gl">I → he/she，my → his/her</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ He said <em>I</em> lost <em>my</em> card. → ✔ He said <em>he</em> lost <em>his</em> card.（转述时不再是「我」）</div></div>
        """ + mp("I lost my card. → He said he lost ___ card.", "my / his", "✔ <em>his</em> — 我变他，我的也跟着变他的。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">时间地点跟着换</span><span class="en">time &amp; place</span></div>
        <span class="ex-line"><span class="tgt">today → that day</span> · yesterday → the day before · tomorrow → the next day<span class="ex-gl">here → there，this → that</span></span>
        <div class="mist"><div class="m-label">记法 · Shortcut</div><div class="m-body">「跟着转述人换视角」——转述的那一刻，你站在哪里说这句话。</div></div>
        """ + mp("I am free today. → She said she was free ___.", "today / that day", "✔ <em>that day</em> — 换到转述人的视角，today 变 that day。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-rep-questions"] = slide("m14-rep-questions", "dark", "M14 · 疑问句转述", "M14",
  head("Reporting Questions · 问句变陈述", "疑问句转述", "asked + if / whether / 疑问词 + 陈述语序") +
  """<div class="sv-cols" style="margin-top:1.4vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">一般疑问 → asked + if</span><span class="en">yes/no questions</span></div>
        <span class="ex-line">He asked, &ldquo;Are you free?&rdquo; → He asked <span class="tgt">if I was free</span>.<span class="ex-gl">if/whether 接管问句，语序变陈述</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ He asked <em>was I free</em>. → ✔ He asked <em>if I was free</em>.（不倒装，也不加问号）</div></div>
        """ + mp("Do you like tea? → He asked ___ I liked tea.", "that / if", "✔ <em>if</em> — 一般疑问用 if/whether 转述。") + """
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">特殊疑问 → 保留疑问词</span><span class="en">wh-questions</span></div>
        <span class="ex-line">She asked, &ldquo;Where do you live?&rdquo; → She asked <span class="tgt">where I lived</span>.<span class="ex-gl">疑问词留下，do 消失，语序回陈述</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ He asked where <em>did I live</em>. → ✔ where <em>I lived</em>.（do/does/did 一律不再出现）</div></div>
        """ + mp("Where do you work? → She asked where I ___.", "worked / did work", "✔ <em>worked</em> — 疑问词后直接接陈述语序。") + """
      </div>
    </div>
  </div>""")

PILOT["m14-rep-practice"] = slide("m14-rep-practice", "light", "M14 · 练习", "M14",
  head("Quick Practice · 转述四连", "练一练：转述别人说的话", "statements · questions", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">转述改写 · turn the words into reported speech</div>
      <div class="p-q"><span class="qnum">1.</span>Tom said, &ldquo;I am hungry.&rdquo; → Tom said he ______ hungry.（am / was）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>was</em> — 主句过去时，am 整体退成 was。</span></div>
      <div class="p-q"><span class="qnum">2.</span>She said, &ldquo;I will call tomorrow.&rdquo; → She said she would call ______.（tomorrow / the next day）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>the next day</em> — 换到转述人视角，明天变 the next day。</span></div>
      <div class="p-q"><span class="qnum">3.</span>He asked, &ldquo;Do you have a pen?&rdquo; → He asked ______ I had a pen.（that / if）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>if</em> — 一般疑问句用 if/whether 转述。</span></div>
      <div class="p-q"><span class="qnum">4.</span>&ldquo;Where do you study?&rdquo; → Lily asked where ______.（did I study / I studied）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>I studied</em> — 疑问词 + 陈述语序，did 消失。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">转述口诀 · Shortcut</div>
      <div class="m-body"><em>一退二换三语序</em>：时态退一格，人称换视角，问句回陈述。</div>
    </div>""")

NOTES_FRAG = [
    N("m14-rep-statement", "陈述句转述", "Ⅱ 动词系统 · 间接引语", 2.5,
      "掌握 said + (that) + 陈述语序的骨架，理解时态后移的一半规则。",
      ["先演一遍班级场景：同学说他忙，你要转给别人听",
       "强调 that 可省略，但语序必须是陈述语序",
       "用 am → was 板书演示「整体后移」，让学生跟读",
       "点出高频错误：主句过去、从句现在，是阅卷最扣分的点"],
      transition="光退时态还不够——下一页看人称和时间词怎么跟着换。"),
    N("m14-rep-changes", "人称与时间地点变化", "Ⅱ 动词系统 · 间接引语", 2.5,
      "把「跟着转述人换视角」变成直觉，人称和时间地点词一换到位。",
      ["让学生站到转述人位置：我变他，今天变那天",
       "左卡练人称：my → his，现场口头替换两轮",
       "右卡给时间地点对照表，请学生齐读一遍",
       "强调记法一句：转述那一刻你站在哪里说这句话"],
      transition="陈述句会转了，那别人问的问题怎么转？下一页看疑问句。"),
    N("m14-rep-questions", "疑问句转述", "Ⅱ 动词系统 · 间接引语", 2.5,
      "分清一般疑问（if/whether）和特殊疑问（保留疑问词），一律回到陈述语序。",
      ["左卡：Are you free? 转 asked if I was free，问号消失",
       "右卡：Where do you live? 转 where I lived，do 消失",
       "用「不再用问号与 do/does/did」一句收束两条规则",
       "对比板书 did I live / I lived，让学生自己指出错在哪"],
      transition="四页凑齐了，进练习页做转述四连，验收这模块。"),
    N("m14-rep-practice", "练习：间接引语", "Ⅱ 动词系统 · 间接引语", 3.0,
      "用四道覆盖时态、时间词、if 转述、语序的题目验收，最后用口诀收束。",
      ["四题逐题做，先全班齐答再点个别学生说理由",
       "第 2 题易错：提醒 will 退 would、tomorrow 也要换",
       "第 4 题是本模块最高频错误，请学生复述规则",
       "带读口诀「一退二换三语序」，作为课后记忆锚点"],
      transition="间接引语收工，接下来换一个模块：无处不在的介词。"),
]
