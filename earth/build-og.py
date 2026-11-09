#!/usr/bin/env python3
"""Render the Open Graph link-preview cards to PNG.

    python3 build-og.py     ->  og.png

Both are 1200x630, the size every platform crops from. They are rendered by
headless Chrome from the same tokens, fonts and emblem path the site uses, so a
preview card cannot drift from the pages it advertises — the alternative is a
hand-made image that silently goes stale.

Chrome needs the network on the first run (Google Fonts). If it is offline the
cards still render, in the fallback stack, and look wrong: check before shipping.
"""
import io, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

import re
from brand import EMBLEM, tok  # the vendored brand layer, never typed here

def brand_fill(css):
    for k in ("bg", "ink", "ink-dim"):
        css = css.replace("@D_%s@" % k.upper().replace("-", "_"), tok("d-" + k))
    assert not re.search(r"@[A-Z_]+@", css), "unfilled brand placeholder"
    return css


SHELL = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Khmer:wght@400;600&display=swap">
<style>
  *{box-sizing:border-box;margin:0}
  html,body{width:1200px;height:630px;overflow:hidden}
  body{background:@D_BG@;color:@D_INK@;
       font-family:"IBM Plex Sans",system-ui,sans-serif;
       display:flex;flex-direction:column;justify-content:center;padding-bottom:40px;
       padding:0 92px;position:relative;-webkit-font-smoothing:antialiased}
  /* one soft accent bloom, bottom-left, so the card is not a flat rectangle */
  body::before{content:"";position:absolute;left:-160px;bottom:-260px;width:760px;height:760px;
       border-radius:50%;background:radial-gradient(circle,rgba(127,166,230,.20),transparent 62%)}
  .inner{position:relative}
  h1{font-family:"Newsreader",Georgia,serif;font-weight:600;letter-spacing:-.022em;
     line-height:1.03;margin-bottom:26px}
  .em{display:inline-block;vertical-align:-.141em;color:#7fa6e6;
      margin-left:-.09em;margin-right:-.04em}
  .reg{font-size:.34em;vertical-align:1.3em;font-weight:500;margin-left:.06em}
  p{font-size:30px;line-height:1.5;color:@D_INK_DIM@;max-width:23ch}
  .site{display:flex;align-items:center;gap:14px;font-size:38px;font-weight:500;color:@D_INK@;margin-bottom:22px}
  .site .em{margin:0;vertical-align:0}
  .wide{max-width:44ch;font-size:27px}
  .globe{position:absolute;right:-70px;top:50%;transform:translateY(-50%);width:600px;height:600px}
  .star{position:absolute;width:var(--s);height:var(--s);color:#dfe6f5}
  .km{font-family:"Noto Sans Khmer","IBM Plex Sans",sans-serif}
  .foot{position:absolute;left:92px;bottom:56px;display:flex;align-items:center;gap:14px;
        font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:22px;color:#7fa6e6}
  .rule{width:52px;height:2px;background:#7fa6e6;opacity:.5}
</style></head><body>{BODY}
<div class="foot"><span class="rule"></span>{FOOT}</div>
</body></html>"""


def emblem(size_em=".92em"):
    return ('<svg class="em" viewBox="0 0 24 24" style="width:%s;height:%s">'
            '<path fill="currentColor" d="%s"/></svg>' % (size_em, size_em, EMBLEM))


STAR = '<svg class="star" style="--s:%dpx;left:%dpx;top:%dpx;opacity:%s" viewBox="-10 -10 20 20"><path fill="currentColor" d="M0-10Q.6-.6 10 0Q.6.6 0 10Q-.6.6-10 0Q-.6-.6 0-10Z"/></svg>'
STARS = "".join(STAR % t for t in [(26, 560, 70, .9), (14, 640, 150, .6), (18, 520, 500, .7), (12, 610, 560, .5), (30, 1130, 40, .9), (16, 1070, 90, .6), (20, 1150, 560, .8), (12, 700, 40, .5), (14, 90, 60, .5), (20, 470, 40, .55)])
GLOBE = '<img class="globe" src="file://%s" alt="">' % os.path.join(HERE, "earth-still-calm.png")

def card(tag):
    return (STARS + GLOBE + '<div class="inner">'
            '<div style="font-family:Newsreader,Georgia,serif;font-weight:600;font-size:46px;letter-spacing:-.02em;margin-bottom:20px">Heart' + emblem(".92em") + 'ank<span class="reg">®</span></div>'
            '<h1 style="font-size:66px;margin-bottom:22px;max-width:9.5em">Every thank makes a crest and a trough.</h1>'
            '<p class="wide" style="max-width:21em">' + tag + '</p></div>')

# name -> (body, the address at the foot)
CARDS = {
    "og.png": (card("The earth.333.eco screens. Drawings, in English and Khmer."), "demo.333.eco/earth"),
    # The live site's card: no "drawings" on it. sync-site copies it to the ledger's public/og.png.
    "og-site.png": (card("The kind rise, the thankful fall, and the sea never gets higher."), "earth.333.eco"),
}

def main():
    if not os.path.exists(CHROME):
        sys.exit("Chrome not found at %s — render the cards elsewhere." % CHROME)
    only = set(sys.argv[1:])
    for name, (body, foot) in CARDS.items():
        if only and name not in only:
            continue
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "card.html")
            io.open(src, "w", encoding="utf-8").write(brand_fill(SHELL).replace("{BODY}", body).replace("{FOOT}", foot))
            out = os.path.join(HERE, name)
            subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=1", "--window-size=1200,630",
                            "--virtual-time-budget=4000", "--allow-file-access-from-files",
                            "--screenshot=" + out, "file://" + src],
                           check=True, capture_output=True)
            print("%-22s %6d bytes" % (name, os.path.getsize(out)))


if __name__ == "__main__":
    main()
