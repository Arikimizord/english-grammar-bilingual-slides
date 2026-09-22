# -*- coding: utf-8 -*-
"""Probe copy v2: wait for webfonts, report only real clip conditions at 16:9."""
src = open('ppt/index.html', encoding='utf-8').read()
probe = """
<script>
window.addEventListener('load', function () {
  var run = function () {
    var res = [];
    document.querySelectorAll('section.slide').forEach(function (s) {
      var sid = s.getAttribute('data-slide-id');
      // horizontal clip: any descendant wider than its own client box
      s.querySelectorAll('*').forEach(function (el) {
        if (el.tagName === 'CANVAS') return;
        if (el.scrollWidth > el.clientWidth + 3 && el.clientWidth > 0)
          res.push(sid + ' H ' + el.tagName + '.' + String(el.className).split(' ')[0] + ' ' + el.scrollWidth + '>' + el.clientWidth);
      });
      // vertical clip at the frame boundary (the actual overflow:hidden cut)
      var f = s.querySelector('.frame');
      if (f && f.scrollHeight > f.clientHeight + 4)
        res.push(sid + ' FRAME-V ' + f.scrollHeight + '>' + f.clientHeight);
    });
    document.body.setAttribute('data-overflow-report', res.join(' ;; ') || 'NONE');
    document.body.setAttribute('data-overflow-done', '1');
  };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { setTimeout(run, 1500); });
  } else { setTimeout(run, 1500); }
});
</script>
"""
src = src.replace('</body>', probe + '</body>')
open(r'E:\ClaudeCode\temp\_probe2.html', 'w', encoding='utf-8').write(src)
print('probe2 written')
