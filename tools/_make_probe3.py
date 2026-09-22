# -*- coding: utf-8 -*-
"""Probe v3: same as v2 but with ALL Aha! answers pre-revealed (worst-case height)."""
src = open('ppt/index.html', encoding='utf-8').read()
src = src.replace('class="mini-p"', 'class="mini-p revealed"')
src = src.replace('class="p-q"', 'class="p-q revealed"')
probe = """
<script>
window.addEventListener('load', function () {
  var run = function () {
    var res = [];
    document.querySelectorAll('section.slide').forEach(function (s) {
      var sid = s.getAttribute('data-slide-id');
      s.querySelectorAll('*').forEach(function (el) {
        if (el.tagName === 'CANVAS') return;
        if (el.scrollWidth > el.clientWidth + 3 && el.clientWidth > 0)
          res.push(sid + ' H ' + el.tagName + '.' + String(el.className).split(' ')[0] + ' ' + el.scrollWidth + '>' + el.clientWidth);
      });
      var f = s.querySelector('.frame');
      if (f && f.scrollHeight > f.clientHeight + 4)
        res.push(sid + ' FRAME-V ' + f.scrollHeight + '>' + f.clientHeight);
    });
    document.body.setAttribute('data-overflow-report', res.join(' ;; ') || 'NONE');
  };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { setTimeout(run, 1500); });
  } else { setTimeout(run, 1500); }
});
</script>
"""
src = src.replace('</body>', probe + '</body>')
open(r'E:\ClaudeCode\temp\_probe3.html', 'w', encoding='utf-8').write(src)
print('probe3 written')
