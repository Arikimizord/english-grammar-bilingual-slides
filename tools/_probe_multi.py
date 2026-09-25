# -*- coding: utf-8 -*-
"""Multi-viewport overflow probe (v3).

Windows headless Chrome enforces a ~512px minimum window width, so narrow
viewports are tested through an <iframe> sized to the exact CSS viewport
(media queries / dvh all respond to the iframe box).

For each viewport (default + all-answers-expanded) reports:
  - fixed-mode viewports : element-level horizontal clips + frame vertical clips
  - scroll-mode viewports: horizontal clips only (vertical scroll is by design)

Usage: python tools/_probe_multi.py
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
TEMP = r"E:\ClaudeCode\temp"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# (label, w, h, mode)  mode: 'fixed' = desktop rules, 'scroll' = scroll-mode rules
VIEWPORTS = [
    ("portrait-phone",   390, 844, "scroll"),
    ("landscape-phone",  844, 390, "scroll"),
    ("ipad-portrait",    768, 1024, "scroll"),
    ("ipad-landscape",   1024, 768, "scroll"),  # <=1100px and <=800px high -> scroll mode
    ("desktop-1440",     1440, 810, "fixed"),
    ("desktop-wide",     1920, 950, "fixed"),
]

# Injected into the deck itself: expand answers, measure, publish report on body.
DECK_PROBE = """
<script>
window.addEventListener('load', function () {
  var run = function () {
    var res = [];
    if (window.__EXPAND) document.querySelectorAll('.aha').forEach(function (b) { b.click(); });
    document.querySelectorAll('section.slide').forEach(function (s) {
      var sid = s.getAttribute('data-slide-id');
      s.querySelectorAll('*').forEach(function (el) {
        if (el.tagName === 'CANVAS') return;
        if (el.scrollWidth > el.clientWidth + 3 && el.clientWidth > 0)
          res.push(sid + ' H ' + el.tagName + '.' + String(el.className).split(' ')[0] + ' ' + el.scrollWidth + '>' + el.clientWidth);
      });
    });
    window.__VERT_CHECK__
    document.body.setAttribute('data-overflow-report', res.join(' ;; ') || 'NONE');
    document.body.setAttribute('data-overflow-done', '1');
  };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { setTimeout(run, 1200); });
  } else { setTimeout(run, 1200); }
});
</script>
"""

VERT_CHECK_FIXED = """
    document.querySelectorAll('section.slide').forEach(function (s) {
      var f = s.querySelector('.frame');
      if (f && f.scrollHeight > f.clientHeight + 4)
        res.push(s.getAttribute('data-slide-id') + ' FRAME-V ' + f.scrollHeight + '>' + f.clientHeight);
    });
"""

# Wrapper: hosts the deck in an iframe of the exact viewport size (narrow viewports)
WRAPPER = """<!DOCTYPE html><html><body style="margin:0">
<iframe id="d" src="_deck_v3.html?slide=1" style="border:0;width:%dpx;height:%dpx"></iframe>
<script>
window.addEventListener('load', function () {
  var tries = 0;
  (function poll() {
    tries++;
    var doc;
    try { doc = document.getElementById('d').contentDocument; } catch (e) {}
    if (doc && doc.body && doc.body.getAttribute('data-overflow-done') === '1') {
      var pre = document.createElement('pre');
      pre.id = 'report';
      pre.setAttribute('data-overflow-report', doc.body.getAttribute('data-overflow-report'));
      document.body.appendChild(pre);
    } else if (tries < 120) { setTimeout(poll, 250); }
    else { document.body.appendChild(Object.assign(document.createElement('pre'), {id:'report', dataset:{overflowReport:'NO-REPORT-FROM-IFRAME'}})); }
  })();
});
</script>
</body></html>"""


def build_deck_copy(path, expand, fixed):
    src = open(SRC, encoding="utf-8").read()
    probe = DECK_PROBE.replace("window.__EXPAND__", "true" if expand else "false")
    probe = probe.replace("__EXPAND__", "true" if expand else "false")
    probe = probe.replace("window.__VERT_CHECK__", VERT_CHECK_FIXED if fixed else "")
    open(path, "w", encoding="utf-8").write(src.replace("</body>", probe + "</body>"))


def run_chrome(url, w, h, profile):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--dump-dom",
           f"--window-size={w},{h}", f"--user-data-dir={profile}",
           "--allow-file-access-from-files",
           "--virtual-time-budget=12000", url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return r.stdout
    except subprocess.TimeoutExpired:
        return ""
    finally:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], capture_output=True)


def report_of(dom):
    m = re.search(r'data-overflow-report="([^"]*)"', dom)
    return m.group(1) if m else None


def main():
    os.makedirs(TEMP, exist_ok=True)
    deck_copy = os.path.join(TEMP, "_deck_v3.html")
    fail = 0
    for label, w, h, mode in VIEWPORTS:
        for expand in (False, True):
            tag = f"{label}-{'exp' if expand else 'def'}"
            build_deck_copy(deck_copy, expand, mode == "fixed")
            if w < 540:  # Windows 最小窗口宽 ~512:窄视口走 iframe 包装
                wrap = os.path.join(TEMP, "_wrap_v3.html")
                open(wrap, "w", encoding="utf-8").write(WRAPPER % (w, h))
                dom = run_chrome("file:///" + wrap.replace("\\", "/"), max(w, 512), h + 40,
                                 os.path.join(TEMP, f"_prof_{tag}"))
            else:
                dom = run_chrome("file:///" + deck_copy.replace("\\", "/") + "?slide=1",
                                 w, h, os.path.join(TEMP, f"_prof_{tag}"))
            report = report_of(dom)
            if report is None:
                print(f"[{tag}] NO-REPORT (dom {len(dom)}B)")
                fail += 1
            elif report == "NONE":
                print(f"[{tag}] NONE")
            else:
                items = report.split(" ;; ")
                print(f"[{tag}] {len(items)} issue(s):")
                for it in items[:12]:
                    print("   ", it)
                if len(items) > 12:
                    print(f"    ... +{len(items)-12} more")
                fail += 1
    try:
        os.remove(deck_copy)
    except OSError:
        pass
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
