# -*- coding: utf-8 -*-
"""Create a probe copy of the deck that reports, per slide, any element
wider/taller than its box (the hard-clip condition under overflow:hidden)."""
src = open('ppt/index.html', encoding='utf-8').read()
probe = """
<script>
window.addEventListener('load', function () {
  setTimeout(function () {
    var res = [];
    document.querySelectorAll('section.slide').forEach(function (s) {
      var sid = s.getAttribute('data-slide-id');
      // horizontal: any descendant clipped inside its own box
      s.querySelectorAll('*').forEach(function (el) {
        if (el.tagName === 'CANVAS') return;
        if (el.scrollWidth > el.clientWidth + 2 && el.clientWidth > 0)
          res.push(sid + ' H ' + el.tagName + '.' + String(el.className).split(' ')[0] + ' ' + el.scrollWidth + '>' + el.clientWidth);
        if (el.scrollHeight > el.clientHeight + 2 && el.clientHeight > 0)
          res.push(sid + ' V ' + el.tagName + '.' + String(el.className).split(' ')[0] + ' ' + el.scrollHeight + '>' + el.clientHeight);
      });
    });
    // also check the hidden-frame containers themselves
    document.querySelectorAll('.frame').forEach(function (f, i) {
      if (f.scrollWidth > f.clientWidth + 2) res.push('frame' + i + ' H ' + f.scrollWidth + '>' + f.clientWidth);
      if (f.scrollHeight > f.clientHeight + 2) res.push('frame' + i + ' V ' + f.scrollHeight + '>' + f.clientHeight);
    });
    document.body.setAttribute('data-overflow-report', res.join(' ;; ') || 'NONE');
    document.body.setAttribute('data-overflow-done', '1');
  }, 1200);
});
</script>
"""
src = src.replace('</body>', probe + '</body>')
open(r'E:\ClaudeCode\temp\_probe.html', 'w', encoding='utf-8').write(src)
print('probe written')
