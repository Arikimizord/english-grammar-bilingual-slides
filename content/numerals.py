# -*- coding: utf-8 -*-
# content/numerals.py —— M08 数词（4 页）

PILOT["pos-num-cardinal"] = slide("pos-num-cardinal","light","M08 · 基数词","M08",
  head("Cardinal Numbers · 数东西的词","基数词：从一到一百","one, two, three …") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">1–12 独立记，13–19 加 -teen</span><span class="en">teen = 十几</span></div>
        <span class="ex-line"><span class="tgt">one, two, three … twelve</span><span class="ex-gl">一到十二没规律，只能硬背</span></span>
        <span class="ex-line">four → <span class="tgt">fourteen</span>, six → <span class="tgt">sixteen</span><span class="ex-gl">直接加 -teen，重音移到 -teen</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>fiveteen</em> → ✔ <em>fifteen</em>（five 变 fif 再加 teen；发 /fɪfˈtiːn/）</div></div>
        <div class="mini-p">""" + mp("Seven plus eight is ___.","fifteen / fiveteen","✔ <em>fifteen</em> — five 的 ve 变 f，没有 fiveteen 这个词。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">整十加 -ty，两位数连字符</span><span class="en">twenty, thirty, forty …</span></div>
        <span class="ex-line">six → <span class="tgt">sixty</span>, nine → <span class="tgt">ninety</span><span class="ex-gl">整十加 -ty，重音在前面</span></span>
        <span class="ex-line"><span class="tgt">twenty-one</span>, forty-six; 101 = a hundred <span class="tgt">and</span> one<span class="ex-gl">十位个位加连字符；百位后加 and</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>fourty</em> → ✔ <em>forty</em>（四十要去掉 u，别被 four 带跑）</div></div>
        <div class="mini-p">""" + mp("101 = one hundred ___ one.","and / with","✔ <em>and</em> — 百位和十位之间用 and 连起来。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-num-ordinal"] = slide("pos-num-ordinal","dark","M08 · 序数词","M08",
  head("Ordinal Numbers · 排第几","序数词：the + 第几","first, second, third …") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">特殊的前三名，其余加 -th</span><span class="en">first / second / third</span></div>
        <span class="ex-line"><span class="tgt">first</span>, <span class="tgt">second</span>, <span class="tgt">third</span><span class="ex-gl">前三名特殊，整体记</span></span>
        <span class="ex-line">four → <span class="tgt">fourth</span>; eight → <span class="tgt">eighth</span> 只加 h<span class="ex-gl">fifth 变 f、ninth 去 e、twelfth 变 f</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>nineth</em> → ✔ <em>ninth</em>（nine 去 e 再加 th，别把 e 带上）</div></div>
        <div class="mini-p">""" + mp("September is the ___ month.","ninth / nineth","✔ <em>ninth</em> — nine 去 e 加 th，九月排在第九。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">整十序数与缩写</span><span class="en">twentieth · 1st 2nd 3rd 4th</span></div>
        <span class="ex-line">twenty → <span class="tgt">twentieth</span>, forty → <span class="tgt">fortieth</span><span class="ex-gl">y 变 i 加 -eth</span></span>
        <span class="ex-line">This is <span class="tgt">the first</span> English lesson; June <span class="tgt">1st</span><span class="ex-gl">序数词前加 the；缩写取末两个字母</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>This is first lesson.</em> → ✔ <em>the first lesson</em>（说「第几」必须带 the）</div></div>
        <div class="mini-p">""" + mp("We live on ___ floor.","the fifth / fifth","✔ <em>the fifth</em> — 序数词前面要加 the，不能光秃秃用。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-num-usage"] = slide("pos-num-usage","light","M08 · 数词的应用","M08",
  head("Big Numbers · 几百，几千，几分之几","确数不加 s，约数才加","hundred / thousand / fraction") +
  """<div class="sv-cols" style="margin-top:2vh">
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">确数 vs 约数</span><span class="en">three hundred / hundreds of</span></div>
        <span class="ex-line"><span class="tgt">three hundred</span> people are in the hall.<span class="ex-gl">有具体数字：不加 s，不加 of</span></span>
        <span class="ex-line"><span class="tgt">Hundreds of</span> students queued for milk tea.<span class="ex-gl">约数「成百上千」：加 s 还要带 of</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>three hundreds of students</em> → ✔ <em>three hundred students</em>（有数字就不加 s 不加 of）</div></div>
        <div class="mini-p">""" + mp("About two ___ students joined.","thousand / thousands","✔ <em>thousand</em> — 前面有 two 这个确数，thousand 不加 s。") + """</div>
      </div>
    </div>
    <div class="col">
      <div class="learn-card" data-anim>
        <div class="lc-t"><span class="cn">年份与分数</span><span class="en">years · fractions</span></div>
        <span class="ex-line">2026 读 <span class="tgt">twenty twenty-six</span>；1949 前后分两半<span class="ex-gl">年份两位两位读</span></span>
        <span class="ex-line"><span class="tgt">half</span> an hour, a <span class="tgt">quarter</span>, two <span class="tgt">thirds</span><span class="ex-gl">分子基数、分母序数，分子大于 1 分母加 s</span></span>
        <div class="mist"><div class="m-label">常见错误 · Common Mistake</div><div class="m-body">✘ <em>two third of the food</em> → ✔ <em>two thirds</em>（分子大于 1，分母序数词要加 s）</div></div>
        <div class="mini-p">""" + mp("About ___ of the food was wasted.","two thirds / two third","✔ <em>two thirds</em> — 分子是 2，分母 third 就要加 s。") + """</div>
      </div>
    </div>
  </div>""")

PILOT["pos-num-practice"] = slide("pos-num-practice","dark","M08 · 练习","M08",
  head("Quick Practice · 数词四连测","基数 · 序数 · 确约数 · 分数","choose the right form", xl_style="font-size:4.6vw") +
  """<div class="practice" data-anim>
      <div class="p-label">单句填空 · 从括号里选对的那个词</div>
      <div class="p-q"><span class="qnum">1.</span>My grandma is ___ years old this autumn.（eighty / eightty）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>eighty</em> — 整十加 -ty：eighty，注意别写成 eightty。</span></div>
      <div class="p-q"><span class="qnum">2.</span>February is the ___ month of the year.（second / two）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>second</em> — 「第几个月」用序数词，two 是基数词。</span></div>
      <div class="p-q"><span class="qnum">3.</span>The club has about two ___ members now.（thousand / thousands）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>thousand</em> — 前面有 two，是确数，thousand 不加 s。</span></div>
      <div class="p-q"><span class="qnum">4.</span>About ___ of the students work part-time.（one thirds / one third）<button type="button" class="aha">Aha! 答案揭晓</button><span class="ans">✔ <em>one third</em> — 分子是 1，分母不加 s；分子大于 1 才加。</span></div>
    </div>
    <div class="mist" style="margin-top:1vh" data-anim>
      <div class="m-label">判定口诀 · Shortcut</div>
      <div class="m-body">确数不加 <em>s</em>，约数加 <em>s</em> 带 of；年份两位两位读；分子基数、分母序。</div>
    </div>""")

NOTES_FRAG = [
    N("pos-num-cardinal","数词 · 基数词","Ⅰ 词法篇 · 数词",2.5,
      "让学生掌握 one 到 ninety-nine 的构词规律：独立记、-teen、-ty、连字符与 hundred 后的 and。",
      ["先问学生十二个月和一到十二能不能对上号——一到十二只能硬背，没有规律。",
       "13 到 19 讲「teen 挂尾巴」，重音移到 -teen 上，和整十 -ty 对比着读一遍。",
       "fifteen 和 fifty 是发音双胞胎坑：让学生跟读 /fɪfˈtiːn/ 和 /ˈfɪfti/，重音位置不同意思不同。",
       "forty 去 u 这个坑单独敲一遍：four 里明明有 u，四十偏偏没有。"],
      "会数数了，接下来看「排第几」——序数词的规矩比基数词还多几个特殊分子。"),
    N("pos-num-ordinal","数词 · 序数词","Ⅰ 词法篇 · 数词",2.5,
      "掌握序数词的构成（特殊前三名、-th 的拼写变化、y 变 i 加 -eth）以及 the + 序数词、日期缩写两个用法。",
      ["first/second/third 是特殊分子，先立住；其余基本就是加 -th。",
       "拼写陷阱连着讲：fifth 变 f、eighth 只加 h、ninth 去 e、twelfth 变 f，一组带读。",
       "整十变序数让学生自己推：twenty → twentieth，y 变 i 加 -eth，多举两个当场验证。",
       "用法上抓住一条主线：说「第几」必须带 the——the first lesson、June 1st 读 June the first。"],
      "单个的数词会写了，接下来看它们在真实句子里怎么用——几百几千和几分之几。"),
    N("pos-num-usage","数词 · 应用","Ⅰ 词法篇 · 数词",2.5,
      "掌握 hundred/thousand/million 的确数与约数用法、年份的两位两位读法、以及分数的「分子基数分母序」公式。",
      ["用奶茶店排队立场景：three hundred 是数得清的，hundreds of 是「乌泱泱一大片」。",
       "确数口诀带读两遍：有数字，不加 s，不加 of；三个条件绑定出现。",
       "年份让学生现场读 2026 和自己入学年份，两位两位断开来读就顺了。",
       "分数用切披萨讲：half、a quarter、two thirds，分子大于 1 分母才加 s。"],
      "规则都过完了，来做四道题，把基数、序数、确约数和分数一次验收。"),
    N("pos-num-practice","数词 · 练习","Ⅰ 词法篇 · 数词",2.0,
      "用四道覆盖整十拼写、序数词、确数 thousand、分数分母的单句填空收束本模块，当场检验。",
      ["第 1 题查 eighty 的拼写，顺带复习 eighteen，两个词别混。",
       "第 2 题和第 3 题是一对：「第几」用序数词，有确数 thousand 不加 s。",
       "第 4 题请做对的同学反过来说一句 two thirds 的句子，检验分子大于 1 的情况。",
       "最后带读口诀：确数不加 s，约数加 s 带 of；年份两位两位读；分子基数、分母序。"],
      "数词这块拿下了，接下来认识句子里「指来指去」的词——下一模块讲代词。"),
]
