# -*- coding: utf-8 -*-
"""Publish the local commit to GitHub via the Git Data API (api.github.com).
Handles empty-repo bootstrap (Contents API) and recursive subtree creation.
Final remote main == local commit SHA, so future `git push` fast-forwards cleanly.
Used when github.com:443 is unreachable but api.github.com is."""
import base64, json, os, subprocess, sys, urllib.request, urllib.error

REPO = "Arikimizord/english-grammar-bilingual-slides"
API = "https://api.github.com/repos/" + REPO

if os.environ.get("GH_TOKEN"):
    TOKEN = os.environ["GH_TOKEN"]
else:
    tok = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                         capture_output=True, text=True).stdout
    TOKEN = [l.split("=", 1)[1].strip() for l in tok.splitlines() if l.startswith("password=")][0]

def api(method, url, payload=None, base=API):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(base + url, data=data, method=method)
    req.add_header("Authorization", "token " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, method, url, "->", e.read().decode()[:200])
        raise

def sh(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True).stdout.strip()

commit_sha = sh("rev-parse", "HEAD")
tree_sha = sh("rev-parse", "HEAD^{tree}")

# --- 0) bootstrap: empty repos reject Git Data API -> seed one file via Contents API
try:
    api("GET", "/git/ref/heads/main")
    print("main exists, no bootstrap needed")
except urllib.error.HTTPError:
    api("PUT", "/contents/.bootstrap", {"message": "bootstrap", "content": base64.b64encode(b"seed").decode()})
    print("bootstrapped empty repo")

NUL = b"\x00"   # entry separator for git ls-tree -z (never in filenames)
TAB = b"\t"

# --- 1) upload every blob (recursive)
def ls_tree(tree_sha):
    """yield (mode, type, sha, name) — raw, -z so non-ASCII names are never quoted."""
    raw = subprocess.run(["git", "ls-tree", "-z", tree_sha], capture_output=True).stdout
    for e in raw.split(NUL):
        if not e:
            continue
        meta, name = e.split(TAB, 1)
        mode, typ, osha = meta.decode().split(" ")
        yield mode, typ, osha, name.decode("utf-8")

def walk(tree_sha, prefix=""):
    """yield (path, mode, sha) for every blob under tree, recursively."""
    for mode, typ, osha, name in ls_tree(tree_sha):
        path = prefix + name
        if typ == "blob":
            yield path, mode, osha
        else:
            yield from walk(osha, path + "/")

blobs = list(walk(tree_sha))
print("total blobs:", len(blobs))
for path, mode, osha in blobs:
    data = subprocess.run(["git", "cat-file", "blob", osha], capture_output=True).stdout
    r = api("POST", "/git/blobs", {"content": base64.b64encode(data).decode(), "encoding": "base64"})
    assert r["sha"] == osha, (path, osha, r["sha"])
    print("  blob ok:", path)

# --- 2) recreate trees bottom-up so every subtree SHA matches local
def tree_entries(tree_sha, sha2remote_tree):
    items = []
    for mode, typ, osha, name in ls_tree(tree_sha):
        if typ == "blob":
            items.append({"path": name, "mode": mode, "type": "blob", "sha": osha})
        else:
            items.append({"path": name, "mode": "040000", "type": "tree", "sha": sha2remote_tree[osha]})
    return items

def build_tree(tree_sha, sha2remote_tree):
    t = api("POST", "/git/trees", {"tree": tree_entries(tree_sha, sha2remote_tree)})
    assert t["sha"] == tree_sha, "tree sha mismatch for " + tree_sha
    sha2remote_tree[tree_sha] = t["sha"]

# collect all subtree shas bottom-up
def subtrees(tree_sha):
    out = []
    for mode, typ, osha, name in ls_tree(tree_sha):
        if typ == "tree":
            out += subtrees(osha) + [osha]
    return out

sha2remote_tree = {}
for st in subtrees(tree_sha):
    build_tree(st, sha2remote_tree)
build_tree(tree_sha, sha2remote_tree)
print("root tree replicated:", tree_sha)

# --- 3) create commit with identical metadata
c = subprocess.run(["git", "cat-file", "-p", commit_sha], capture_output=True, text=True).stdout
meta = c.split("\n\n", 1)
head, msg = meta[0], meta[1]
def person(line, tag):
    from datetime import datetime, timedelta, timezone
    v = [l[len(tag):] for l in head.splitlines() if l.startswith(tag)][0]
    name, rest = v.split(" <", 1)
    email, date_tz = rest.split("> ", 1)
    ts, tz = date_tz.rsplit(" ", 1)          # git raw format: "<unix-ts> +0800"
    off = timezone(timedelta(hours=int(tz[1:3]), minutes=int(tz[3:5])) * (1 if tz[0] == "+" else -1))
    iso = datetime.fromtimestamp(int(ts), off).isoformat()   # -> "2026-09-21T15:04:44+08:00" (GitHub API needs ISO 8601)
    return {"name": name, "email": email, "date": iso}
parents = [l.split(" ", 1)[1] for l in head.splitlines() if l.startswith("parent ")]
nc = api("POST", "/git/commits", {"message": msg, "tree": tree_sha, "parents": parents,
                                  "author": person(head, "author "), "committer": person(head, "committer ")})
print("remote commit:", nc["sha"])
assert nc["sha"] == commit_sha, "commit sha mismatch!"

# --- 4) point refs/heads/main at the local commit (force over bootstrap)
try:
    api("POST", "/git/refs", {"ref": "refs/heads/main", "sha": commit_sha})
except urllib.error.HTTPError:
    api("PATCH", "/git/refs/heads/main", {"sha": commit_sha, "force": True})
print("refs/heads/main ->", commit_sha)
print("DONE: https://github.com/" + REPO)
