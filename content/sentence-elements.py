# -*- coding: utf-8 -*-
# content/sentence-elements.py —— 句子成分（M02）内容片段

PILOT["m2-elem-subj-pred"] = slide("m2-elem-subj-pred","dark","M02 · 主语与谓语","M02",
  head("Subject & Predicate · 主语与谓语","先抓骨架：主语 + 谓语","subject = 谁 / 什么　predicate = 动词") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">主语 Subject</span><span class="en">「谁 / 什么」</span></div>
        <span class="ex-line"><span class="tgt">Swimming</span> keeps me fit.<span class="ex-gl">主语可以是名词、代词、doing 或从句</span></span>
        <span class="ex-line"><span class="tgt">That he lied</span> surprised nobody.<span class="ex-gl">一个从句也能当主语</span></span>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">___ makes me sleepy.（Read / Reading）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>Reading</em> — 作主语用动名词；动词原形 Read 不能直接当主语。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">谓语 Predicate</span><span class="en">动词，跟主语的人称和数</span></div>
        <span class="ex-line">My roommate <span class="tgt">watches</span> videos after class.<span class="ex-gl">三单主语 → 动词加 -s</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I am study English.</em> → ✔ <em>I study English.</em> / <em>I am studying English.</em>（一句只有一个谓语）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">He opened the door ___ looked out.（and / but）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>and</em> — 两个动作要么用连词，要么改非谓语，不能裸放两个谓语。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m2-elem-obj-pred"] = slide("m2-elem-obj-pred","light","M02 · 宾语与表语","M02",
  head("Object & Predicative · 宾语与表语","动词后面跟什么","object 宾语　predicative 表语") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">宾语 Object</span><span class="en">动作的承受者</span></div>
        <span class="ex-line">I borrowed <span class="tgt">a novel</span> from the library.<span class="ex-gl">放在及物动词后：给「什么」</span></span>
        <span class="ex-line">He gave <span class="tgt">me</span> <span class="tgt">a ride</span> to the station.<span class="ex-gl">双宾：给「谁」+ 给「什么」</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>Listen me.</em> → ✔ <em>Listen to me.</em>（listen 不及物，要先加 to）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">She showed ___ her new phone.（we / us）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>us</em> — 间接宾语（给「谁」）用宾格；we 是主格。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">表语 Predicative</span><span class="en">系动词后的身份 / 状态</span></div>
        <span class="ex-line">The milk smells <span class="tgt">sour</span>.<span class="ex-gl">be / become / look / seem 后，形容词作表语</span></span>
        <span class="ex-line">My cousin became <span class="tgt">a nurse</span>.<span class="ex-gl">表语也可以是名词：说明主语身份</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I am agree.</em> → ✔ <em>I agree.</em>（agree 本身是动词，不再搭 be）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The campus looks ___ at night.（quiet / quietly）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>quiet</em> — look 是系动词，后接形容词作表语，不用副词。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m2-elem-attrib-adverb"] = slide("m2-elem-attrib-adverb","dark","M02 · 定语与状语","M02",
  head("Attributive & Adverbial · 定语与状语","挂上去的修饰成分","attributive 定语　adverbial 状语") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">定语 Attributive</span><span class="en">修饰名词</span></div>
        <span class="ex-line">She found a <span class="tgt">part-time</span> job.<span class="ex-gl">形容词放名词前</span></span>
        <span class="ex-line">Do you know the girl <span class="tgt">in red</span>?<span class="ex-gl">介词短语 / 从句放名词后</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>a student smart</em> → ✔ <em>a smart student</em>（单个形容词要放名词前）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">The man ___ is my coach.（in a cap / cap）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>in a cap</em> — 介词短语后置修饰 the man：「戴帽子的那位」。</span></div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">状语 Adverbial</span><span class="en">修饰动词 / 形容词 / 整句</span></div>
        <span class="ex-line">We practice English <span class="tgt">every morning</span>.<span class="ex-gl">时间状语：什么时候</span></span>
        <span class="ex-line"><span class="tgt">Luckily</span>, the bus came on time.<span class="ex-gl">修饰整句的状语，常放句首</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>He speaks English good.</em> → ✔ <em>well</em>（修饰动词要用副词）</div></div>
        <div class="mini-p"><span class="mp-label">练</span><span class="mp-q">She answers questions ___.（quick / quickly）</span><button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>quickly</em> — 修饰动词 answers，作方式状语用副词。</span></div>
      </div>
    </div>
  </div>""")

PILOT["m2-elem-practice"] = slide("m2-elem-practice","light","M02 · 练习","M02",
  head("Quick Practice · 认成分","练一练：判断句子成分","identify the element", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">划线提问 · 主语 / 谓语 / 宾语 / 表语 / 定语 / 状语</div>
      <div class="p-q"><span class="qnum">1.</span><em>I</em> put the keys on the table. → 划线是 ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>主语 S</em> — 动作的发出者：谁放的钥匙。</span></div>
      <div class="p-q"><span class="qnum">2.</span>The noodles taste <em>spicy</em>. → 划线是 ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>表语</em> — taste 是系动词，spicy 说明主语的状态。</span></div>
      <div class="p-q"><span class="qnum">3.</span>The boy <em>under the tree</em> is my classmate. → 划线是 ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>定语</em> — 介词短语后置，修饰 the boy：「树下的那个」。</span></div>
      <div class="p-q"><span class="qnum">4.</span>My grandma waters the plants <em>every evening</em>. → 划线是 ______<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>状语</em> — 说明浇水的时间，修饰动词 waters。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">主干先抓 <em>主谓</em>，修饰再挂两边：挂名词的是 <em>定语</em>，挂动词或整句的是 <em>状语</em>。</div>
    </div>""")

NOTES_FRAG = [
    N("m2-elem-subj-pred","主语与谓语","句子基础 · 句子成分",2.5,
      "让学生先抓句子骨架：主语答「谁/什么」，谓语是动词并随主语变化。",
      ["提问：I am study English 错在哪，请学生先说",
       "强调一句只有一个谓语，两个动作要有连词或非谓语",
       "让学生用自己的日常活动各造一个主谓句"],
      transition="骨架有了，接下来看动词后面还能挂什么——宾语和表语。"),
    N("m2-elem-obj-pred","宾语与表语","句子基础 · 句子成分",2.5,
      "分清动作的承受者（宾语）和系动词后的身份状态（表语）。",
      ["用 gave me a ride 演示双宾：给谁、给什么",
       "对比 He became a nurse 和 He greeted a nurse，辨宾语与表语",
       "提醒 listen to me、I agree 这类高频口语错误"],
      transition="主干成分齐了，下一页给句子挂上修饰成分——定语和状语。"),
    N("m2-elem-attrib-adverb","定语与状语","句子基础 · 句子成分",2.5,
      "掌握两条位置规则：定语修饰名词，状语修饰动词或整句。",
      ["用 the girl in red 讲后置定语，让学生现场仿写",
       "对比 good / well，讲清形容词与副词的分工",
       "让学生给 We practice English 加时间、地点、方式状语"],
      transition="成分都认全了，最后用四道判断题验收。"),
    N("m2-elem-practice","句子成分 · 练一练","句子基础 · 句子成分",2.0,
      "用划线判断题检验六种成分的辨认，收束本模块。",
      ["先让学生齐答四题，再点开答案核对",
       "错得多的题回翻对应内容页讲透",
       "带读口诀：主干先抓主谓，修饰再挂两边"],
      transition="成分是零件，下一模块看零件怎么拼成三种句型。"),
]
