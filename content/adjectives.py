# -*- coding: utf-8 -*-
# content/adjectives.py —— M06 形容词（4 页）

PILOT["pos-adj-position"] = slide("pos-adj-position","light","M06 · 形容词的位置","M06",
  head("Adjective Position · 形容词站在哪","形容词的两种位置","attributive & predicative position") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">定语位置</span><span class="en">attributive</span></div>
        <span class="ex-line">My uncle drives a <span class="tgt">red</span> car.<span class="ex-gl">一般情况：形容词放在名词前面</span></span>
        <span class="ex-line">Is there <span class="tgt">something important</span> in today&rsquo;s email?<span class="ex-gl">不定代词 something / anything 要后置</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>important something</em> → ✔ <em>something important</em>（不定代词作定语要放后面，顺序不能反）</div></div>
        <div class="mini-p">""" + mp("I want to buy ___ for my mom.","something special / special something","✔ <em>something special</em> — 不定代词后置，形容词跟在后面。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">表语位置</span><span class="en">predicative</span></div>
        <span class="ex-line">The sky is <span class="tgt">blue</span>; the milk smells <span class="tgt">sour</span>.<span class="ex-gl">放在系动词后，说明主语什么样</span></span>
        <span class="ex-line">Don&rsquo;t be <span class="tgt">afraid</span>; the baby is finally <span class="tgt">asleep</span>.<span class="ex-gl">afraid / asleep / alike 只能作表语</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>an asleep baby</em> → ✔ <em>a sleeping baby</em>（asleep 不能放名词前，定语要换 sleeping）</div></div>
        <div class="mini-p">""" + mp("The twins look very ___.","alike / like","✔ <em>alike</em> — alike 只作表语；like 是介词，后面还得跟名词。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-adj-order"] = slide("pos-adj-order","dark","M06 · 多个形容词的排列顺序","M06",
  head("Adjective Order · 一串形容词怎么排","多个形容词的排列顺序","determiner → opinion → size → age → color …") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">排列公式</span><span class="en">OSASCOMP</span></div>
        <span class="ex-line"><span class="tgt">限定→观点→大小→形状→年龄→颜色→国籍→材料→用途</span>＋名词<span class="ex-gl">九层排队，一层不许插队</span></span>
        <span class="ex-line">中文口诀：<span class="tgt">限观大形龄色国材用</span><span class="ex-gl">九个字背下来，考试直接套</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>a big nice room</em> → ✔ <em>a nice big room</em>（观点 nice 排在大小 big 前面）</div></div>
        <div class="mini-p">""" + mp("She carries a ___ bag every day.","black leather / leather black","✔ <em>black leather</em> — 颜色在材料前：black（色）→ leather（材）。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">完整排队示例</span><span class="en">all in one line</span></div>
        <span class="ex-line"><span class="tgt">a beautiful little old Chinese wooden box</span><span class="ex-gl">观点→大小→年龄→国籍→材料，全对</span></span>
        <span class="ex-line">a <span class="tgt">famous young American</span> singer came to our school.<span class="ex-gl">观点→年龄→国籍，同样按公式走</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>a wooden Chinese box</em> → ✔ <em>a Chinese wooden box</em>（国籍在材料前面，木材不能越位）</div></div>
        <div class="mini-p">""" + mp("He bought an ___ watch yesterday.","expensive Swiss / Swiss expensive","✔ <em>expensive Swiss</em> — 观点 expensive 排在国籍 Swiss 前面。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-adj-ed-ing"] = slide("pos-adj-ed-ing","light","M06 · -ed 与 -ing 形容词","M06",
  head("-ed vs -ing · 一对双胞胎","-ed 与 -ing 形容词","boring or bored?") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">-ing 修饰物</span><span class="en">「令人……」</span></div>
        <span class="ex-line">The movie is <span class="tgt">boring</span>; I left early.<span class="ex-gl">电影「令人无聊」，主语是物</span></span>
        <span class="ex-line">We got some <span class="tgt">surprising</span> news yesterday.<span class="ex-gl">消息「令人惊讶」，还是物</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>The movie is bored.</em> → ✔ <em>The movie is boring.</em>（电影不会「感到」无聊，它只会「令人」无聊）</div></div>
        <div class="mini-p">""" + mp("This game is really ___.","boring / bored","✔ <em>boring</em> — 主语 game 是物，「令人无聊」用 -ing。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">-ed 修饰人</span><span class="en">「感到……」</span></div>
        <span class="ex-line">I am <span class="tgt">bored</span>. Can we go out now?<span class="ex-gl">我「感到」无聊，主语是人</span></span>
        <span class="ex-line">We were <span class="tgt">surprised</span> at the news.<span class="ex-gl">人「感到」惊讶，用 -ed</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>I am boring today.</em> → ✔ <em>I am bored today.</em>（说 I am boring 等于自报家门：我这人很无趣）</div></div>
        <div class="mini-p">""" + mp("I am ___ with this slow Wi-Fi.","bored / boring","✔ <em>bored</em> — 主语是人，「感到烦」用 -ed。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-adj-practice"] = slide("pos-adj-practice","dark","M06 · 练习","M06",
  head("Quick Practice · 形容词四连测","位置 · 顺序 · -ed / -ing","choose the right one", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">单句填空 · 从括号里选对的那个词</div>
      <div class="p-q"><span class="qnum">1.</span>She wants to buy ___ for lunch.（something sweet / sweet something）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>something sweet</em> — 不定代词后置，形容词放后面。</span></div>
      <div class="p-q"><span class="qnum">2.</span>The baby is ___ in the stroller.（asleep / sleep）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>asleep</em> — asleep 只作表语，放在系动词后面。</span></div>
      <div class="p-q"><span class="qnum">3.</span>She wears a ___ skirt to class.（red beautiful / beautiful red）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>beautiful red</em> — 口诀「限观大形龄色国材用」：观点在颜色前。</span></div>
      <div class="p-q"><span class="qnum">4.</span>We were all ___ at the final score.（surprised / surprising）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>surprised</em> — 主语是人，「感到惊讶」用 -ed。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">名词前，代词后；<em>afraid / asleep</em> 只作表语；串词背「限观大形龄色国材用」；物 <em>-ing</em>，人 <em>-ed</em>。比较等级（-er / -est）见 M26。</div>
    </div>""")

NOTES_FRAG = [
    N("pos-adj-position","形容词 · 两种位置","Ⅰ 词法篇 · 形容词",2.5,
      "让学生分清形容词的定语位置（名词前、不定代词后）与表语位置（系动词后），并记住 afraid / asleep / alike 只能作表语。",
      ["开场用 a red car 立住「形容词在名词前」的基本盘，全班齐读一遍。",
       "再抛出 something important：不定代词是唯一的例外，形容词要搬到后面。",
       "表语位置用 The sky is blue 带：形容词跟在 is / look / smell 这些系动词后。",
       "afraid / asleep / alike 单独敲一遍：只能当表语，放名词前就错，想说 an asleep baby 要改成 a sleeping baby。",
       "比较级 -er / -est 不在本模块展开，M26 比较等级会专门讲，这里先不提。"],
      "位置定了，接下来解决一串形容词挤在一起时，谁站前谁站后。"),
    N("pos-adj-order","形容词 · 排列顺序","Ⅰ 词法篇 · 形容词",2.5,
      "掌握九层排列公式 限定→观点→大小→形状→年龄→颜色→国籍→材料→用途，会用中文口诀「限观大形龄色国材用」套题。",
      ["先带读九层公式，再教口诀「限观大形龄色国材用」，九个字对应九层。",
       "用 a beautiful little old Chinese wooden box 做全程示范，逐词标出是哪一层。",
       "提醒学生：真正考试里一串最多四五个形容词，抓住「观点最前、材料国籍靠后」就能拿分。",
       "mist 里 a wooden Chinese box 是高频错项，让学生自己用口诀查出错在哪一层。"],
      "顺序排好了，最后看一对最容易混的双胞胎：-ed 与 -ing 形容词。"),
    N("pos-adj-ed-ing","形容词 · -ed 与 -ing","Ⅰ 词法篇 · 形容词",2.5,
      "分清 -ing 形容词（修饰物、令人……）与 -ed 形容词（修饰人、感到……），不再写出 I am boring 这类自黑句。",
      ["先给一对例句：The movie is boring. / I am bored. 让学生自己找区别。",
       "总结成一句话：东西 -ing「令人」，人 -ed「感到」，主语是谁就跟着谁变。",
       "I am boring today 这个错误要当堂演一遍：说完问学生「你确定要这么介绍自己吗」，笑过就记住了。",
       "顺带扩展 surprising / surprised、tiring / tired，都是同一套规律。"],
      "规律都讲完了，来做四道题，把位置、顺序、-ed / -ing 一次过完。"),
    N("pos-adj-practice","形容词 · 练习","Ⅰ 词法篇 · 形容词",2.0,
      "用四道覆盖不定代词后置、表语形容词、排列口诀和 -ed / -ing 的题收束本模块，当场检验。",
      ["第 1、2 题查位置：something sweet 靠后置，asleep 只能当表语。",
       "第 3 题让学生现场背口诀「限观大形龄色国材用」再选 beautiful red。",
       "第 4 题查 -ed / -ing：主语是人，感到惊讶用 surprised。",
       "请做对的同学用「某个东西很令人惊讶」自己造一句，现学现用。",
       "最后带读口诀收尾，并预告：形容词的比较等级在 M26 专门开讲。"],
      "形容词到位了，接下来看替名词「值班」的词——下一模块讲代词。"),
]
