#!/usr/bin/env python3
"""Generate index.html from canvas.json: the front door cannot drift from the artboards.

    python3 build-index.py
"""
import hashlib, io, json, os, html
from brand import tok

HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(io.open(os.path.join(HERE, "canvas.json"), encoding="utf-8"))
boards = sorted(c["artboards"], key=lambda b: (b["y"], b["x"]))
rows = "".join(
    '<li><a href="%s?v=%s&w=%d">%s</a><span class="m">%d px wide</span></li>' % (b["file"], hashlib.sha256(io.open(os.path.join(HERE, b["file"]), "rb").read()).hexdigest()[:8], b["w"], html.escape(b["title"]), b["w"])
    for b in boards)
page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="googlebot" content="noindex,nofollow">
<meta name="bingbot" content="noindex,nofollow">
<meta name="slurp" content="noindex,nofollow">
<meta name="yandex" content="noindex,nofollow">
<script src="./analytics.js"></script>
<title>Log in and Sign with HeartBank&#174;: drawings</title>
<meta property="og:type" content="website">
<meta property="og:url" content="https://demo.333.eco/">
<meta property="og:site_name" content="b.333.eco drawings">
<meta property="og:title" content="Log in and Sign with HeartBank&#174;: drawings">
<meta property="og:description" content="The b.333.eco screens, drawn in English and Khmer. These are drawings. They charge nobody.">
<meta property="og:image" content="https://demo.333.eco/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Log in and Sign with HeartBank on a dark ground, the B-Emblem standing in for the B.">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f52ba">
<style>[hidden]{display:none!important}
:root{--bg:@L_BG@;--fg:@L_INK@;--dim:@L_INK_DIM@;--line:@L_LINE@;--acc:#0f52ba}
@media (prefers-color-scheme:dark){:root{--bg:@D_BG@;--fg:@D_INK@;--dim:@D_INK_DIM@;--line:@D_LINE@;--acc:#7fa6e6}}
body{margin:0;padding:2.5rem 16px 4rem;background:var(--bg);color:var(--fg);font:1rem/1.6 system-ui,sans-serif}
main{max-width:36rem;margin:0 auto}
h1{font-size:1.9rem;line-height:1.2;margin:0 0 .5rem}
p{color:var(--dim)}
.start{display:block;border:1px solid var(--acc);border-radius:1rem;padding:1rem 1.2rem;margin:1.5rem 0;color:var(--fg);text-decoration:none}
.start b{color:var(--acc)}
ul{list-style:none;margin:0;padding:0}
li{display:flex;justify-content:space-between;gap:1rem;padding:.8rem 0;border-top:1px solid var(--line)}
li a{color:var(--fg)} .m{color:var(--dim);font-size:.85rem;white-space:nowrap}
small{display:block;margin-top:2rem;color:var(--dim)}</style>
</head>
<body>
<main>
<h1>Log in and Sign with HeartBank&#174;: drawings</h1>
<p>The screens for b.333.eco, the estate's identity layer: <b>Log in</b> proves who you are; <b>Sign</b> puts your name to one file. English and Khmer, with a dark pass.</p>
<a class="start" href="wall.html"><b>Start here</b><br>Every screen on one wall. Drag to pan, pinch to zoom, tap a screen to open it.</a>
<ul>%s</ul>
<small>These are drawings. They charge nobody, and nothing here is live. The Khmer is our own placeholder until a native reader approves it. Hidden from search by named crawler; shareable by link. This site counts visits without cookies.</small>
</main>
</body>
</html>
""" % rows
for _p, _k in (("L", "bg"), ("L", "ink"), ("L", "ink-dim"), ("L", "line"), ("D", "bg"), ("D", "ink"), ("D", "ink-dim"), ("D", "line")):
    page = page.replace("@%s_%s@" % (_p, _k.upper().replace("-", "_")), tok("%s-%s" % (_p.lower(), _k)))
assert "@L_" not in page and "@D_" not in page, "unfilled brand placeholder"
io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
print("index.html written: %d artboards" % len(boards))

# Re-stamp the tracker reference from the file's own hash so a change is never served stale.
import subprocess as _sp
_sp.run(["python3", os.path.join(HERE, "stamp-analytics.py")], check=True)
