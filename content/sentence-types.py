# -*- coding: utf-8 -*-
# content/sentence-types.py —— 句子类型（M08）内容片段

PILOT["m8-type-simple"] = slide("m8-type-simple","dark","M08 · 简单句","M08",
  head("Simple Sentence · 简单句","一套主谓，就是简单句","one subject-predicate pair",
       "简单句也可以很长：主语带定语、谓语带状语，骨架仍是一套主谓。") +
  """<div class="sv-cols" style="margin-top:1.6vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">一套主谓</span><span class="en">short or long</span></div>
        <span class="ex-line">My roommate <span class="tgt">cooks</span> noodles at midnight.<span class="ex-gl">主语 + 谓语，一套就够</span></span>
        <span class="ex-line"><span class="tgt">The tired student in the back row</span> <span class="tgt">passed</span> the exam.<span class="ex-gl">带定语带状语，仍是简单句</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">Both twins ___ in the school band.（play / plays）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>play</em> — 主语 twins 复数，一套主谓的简单句。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">两个谓语要连词</span><span class="en">two verbs, one link</span></div>
        <span class="ex-line">I opened the door <span class="tgt">and</span> looked out.<span class="ex-gl">两个动作，一个连词</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I opened the door looked out.</em> → ✔ <em>…door and looked out.</em>（两个谓语不能裸奔）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">He took out his phone, ___ a photo.（take / took）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>took</em> — and 连接的动词要同形，共享一个主语。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m8-type-compound"] = slide("m8-type-compound","light","M08 · 并列句","M08",
  head("Compound Sentence · 并列句","两条梁，用连词并肩","句 + , + 连词 + 句",
       "并列连词四兄弟：and 并列、but 转折、or 选择、so 因果。") +
  """<div class="sv-cols" style="margin-top:1.6vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">结构：句 + , + 连词 + 句</span><span class="en">equal clauses</span></div>
        <span class="ex-line">I like milk tea, <span class="tgt">but</span> it is expensive.<span class="ex-gl">两个句子等价，用逗号 + 连词相连</span></span>
        <span class="ex-line">It was raining, <span class="tgt">so</span> we stayed in the dorm.<span class="ex-gl">so 表结果：下雨，所以待在宿舍</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">Hurry up, ___ we&rsquo;ll miss the bus.（or / so）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>or</em> — 这里是「否则」，表选择；so 表结果。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">逗号粘连 Comma Splice</span><span class="en">最常见的病句</span></div>
        <span class="ex-line">I like tea; <span class="tgt">however</span>, he likes coffee.<span class="ex-gl">分号 + however 也能连两个分句</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I like tea, he likes coffee.</em> → ✔ <em>…tea, but he likes coffee.</em>（逗号粘不住两个句子）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">I knocked, ___ nobody answered.（but / and）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>but</em> — 敲了门但没人应，转折关系用 but。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m8-type-complex"] = slide("m8-type-complex","dark","M08 · 复合句","M08",
  head("Complex Sentence · 复合句","一主一仆：主句 + 从句","main clause + subordinate clause",
       "一句话点破：并列句是「两条梁」并肩，复合句是「一主一仆」。") +
  """<div class="sv-cols" style="margin-top:1.6vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主句 + 从句</span><span class="en">because / when / if / that / who</span></div>
        <span class="ex-line">I stayed up <span class="tgt">because</span> the exam was near.<span class="ex-gl">because 引导原因从句，挂在主句上</span></span>
        <span class="ex-line">The girl <span class="tgt">who wears glasses</span> is our monitor.<span class="ex-gl">who 从句修饰 the girl，作定语</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The classmate ___ helped me is here.（who / which）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>who</em> — 先行词是人用 who；which 用于物。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">从句不能独立成句</span><span class="en">no lone clause</span></div>
        <span class="ex-line"><span class="tgt">When the bell rang</span>, the students rushed out.<span class="ex-gl">从句是仆人，离了主句就是半句话</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Because I was tired.</em> → ✔ <em>Because I was tired, I slept early.</em>（从句要靠主句）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">___ it rains tomorrow, we&rsquo;ll stay indoors.（If / But）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>If</em> — 条件从句用 if；but 是并列连词，管不了从句。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m8-type-practice"] = slide("m8-type-practice","light","M08 · 练习","M08",
  head("Quick Practice · 判句型","练一练：简单 / 并列 / 复合","simple, compound or complex", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">判断句型 · Simple / Compound / Complex</div>
      <div class="p-q"><span class="qnum">1.</span>My uncle repairs bikes on weekends. → ______（提示：几套主谓？）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>简单句</em> — 一套主谓，状语再长也不变骨架。</span></div>
      <div class="p-q"><span class="qnum">2.</span>I called him, but nobody answered. → ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>并列句</em> — 逗号 + but 连接两个等价分句。</span></div>
      <div class="p-q"><span class="qnum">3.</span>When the bell rang, the students rushed out. → ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>复合句</em> — when 引导时间从句 + 主句，一主一仆。</span></div>
      <div class="p-q"><span class="qnum">4.</span>Send me the address, or I can&rsquo;t find the shop. → ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>并列句</em> — or 表「否则」，两个祈使分句并列。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">数谓语、看连词：一套主谓是 <em>简单</em>，逗号 + 连词是 <em>并列</em>，从句挂主句是 <em>复合</em>。</div>
    </div>""")

NOTES_FRAG = [
    N("m8-type-simple","简单句","句子基础 · 句子类型",2.5,
      "让学生抓住判定标准：不管多长，只有一套主谓就是简单句。",
      ["用长例句演示：加了定语状语，骨架还是一套",
       "讲 I opened the door looked out 的病根：两个裸谓语",
       "让学生把上周写过的短句拿出来加长，仍保持简单句"],
      transition="一套主谓会说了，两套主谓怎么拼？看并列句。"),
    N("m8-type-compound","并列句","句子基础 · 句子类型",2.5,
      "掌握「句 + 逗号 + 连词 + 句」的结构和 and/but/or/so 的分工。",
      ["带读四个并列连词：并列、转折、选择、因果",
       "重点讲逗号粘连：光有逗号粘不住两个句子",
       "让学生用 so 和 but 各造一句宿舍生活"],
      transition="并列是平起平坐，下一页看谁主谁从——复合句。"),
    N("m8-type-complex","复合句","句子基础 · 句子类型",2.5,
      "理解主句与从句的主从关系，认识 because/when/if/that/who 等引导词。",
      ["用「两条梁 vs 一主一仆」比喻对比并列与复合",
       "强调从句不能独立成句，Because I was tired 只是半句话",
       "让学生把两个简单句合并成一个复合句"],
      transition="三种句型都认完了，最后四道题验收。"),
    N("m8-type-practice","句子类型 · 练一练","句子基础 · 句子类型",2.0,
      "用判断题检验三种句型的辨认，收束本模块。",
      ["先全班齐答四题，再逐题点开答案",
       "第 1 题易错：提醒状语长不代表句子复杂",
       "带读口诀：数谓语、看连词"],
      transition="句子骨架和类型都齐了，下一部分进入动词系统。"),
]
