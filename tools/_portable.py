# -*- coding: utf-8 -*-
"""Make build.py portable: repo-local template + env overrides (for open-source release)."""
src = open("build.py", encoding="utf-8").read()

old = 'SKILL = r"E:\\ClaudeCode\\claude-config\\skills\\guizang-ppt-skill"\nSRC = os.path.join(SKILL, "assets", "template.html")'
assert old in src, "SKILL block not found"
new = """# Template resolution: env var > repo-local template/ > local skill install.
# The template ships with this repo under AGPL-3.0 (see template/README.md);
# original upstream: https://github.com/op7418/guizang-ppt-skill
_here = os.path.dirname(os.path.abspath(__file__))
_local = os.path.join(_here, "template", "template.html")
_skill = os.path.join(os.environ.get("GUIZANG_SKILL",
        r"E:" + chr(92) + "ClaudeCode" + chr(92) + "claude-config" + chr(92) + "skills" + chr(92) + "guizang-ppt-skill"),
        "assets", "template.html")
SRC = os.environ.get("GRAMMAR_TEMPLATE") or (_local if os.path.exists(_local) else _skill)"""
src = src.replace(old, new)

old2 = 'OUT_DIR = r"E:\\ClaudeCode\\projects\\\u9ad8\u6821\u82f1\u8bed\u8bed\u6cd5\u53cc\u8bed\u8bfe\u4ef6_20260921\\ppt"'
assert old2 in src, "OUT_DIR not found"
src = src.replace(old2, 'OUT_DIR = os.environ.get("GRAMMAR_OUT") or os.path.join(_here, "ppt")')

open("build.py", "w", encoding="utf-8", newline="").write(src)
print("patched build.py for portability")
