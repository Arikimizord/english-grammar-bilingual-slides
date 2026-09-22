# -*- coding: utf-8 -*-
"""Round 9: iteratively flip divider themes in build.py until no 3+ same-theme run."""
import re, subprocess, sys

def scan():
    src = open("ppt/index.html", encoding="utf-8").read()
    secs = [(m.group(1), m.group(2)) for m in re.finditer(
        r'<section class="slide ([^"]+)" data-slide-id="([^"]+)"', src)]
    themes = [("dark" if "dark" in c else "light", sid) for c, sid in secs]
    runs = []
    i = 0
    while i < len(themes):
        j = i
        while j + 1 < len(themes) and themes[j + 1][0] == themes[i][0]:
            j += 1
        if j - i >= 2:
            runs.append(themes[i:j + 1])
        i = j + 1
    return runs

for it in range(8):
    runs = scan()
    if not runs:
        print("iteration", it, ": rhythm clean")
        sys.exit(0)
    mids = set()
    for r in runs:
        mids.add(r[1][1])          # middle slide id (the divider, = module id)
    print("iteration", it, ": runs:", [[s for _, s in r] for r in runs], "-> flip:", sorted(mids))
    src = open("build.py", encoding="utf-8").read()
    for mid in mids:
        pat = re.compile(r'\("' + re.escape(mid) + r'",(\s*"[^"]*",.*?)"(hero (?:dark|light))"')
        m = pat.search(src)
        assert m, "module row not found: " + mid
        flipped = "hero light" if m.group(2) == "hero dark" else "hero dark"
        src = src[:m.start(2)] + flipped + src[m.end(2):]
    open("build.py", "w", encoding="utf-8", newline="").write(src)
    subprocess.run([sys.executable, "build.py"], check=True, capture_output=True)
print("did not converge in 8 iterations")
sys.exit(1)
