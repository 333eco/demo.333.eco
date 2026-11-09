#!/usr/bin/env python3
"""Render the Open Graph link-preview cards to PNG.

    python3 build-og.py     ->  og.png (this demo) + og-site.png (333.eco's own card, copied to its static/assets/og.png)

Both are 1200x630, the size every platform crops from. They are rendered by
headless Chrome from the same tokens, fonts and emblem path the site uses, so a
preview card cannot drift from the pages it advertises — the alternative is a
hand-made image that silently goes stale.

Chrome needs the network on the first run (Google Fonts). If it is offline the
cards still render, in the fallback stack, and look wrong: check before shipping.
"""
import io, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

import re
from brand import EMBLEM, tok  # the vendored brand layer, never typed here
import registry_boards as rb  # the ladder itself, so the card cannot draw a different one than the page

# Every card stamps itself (/media step 6): an undeclared rebuild is how a disclosure goes missing.
STAMP = os.path.join(HERE, "..", "..", "..", ".claude", "skills", "media", "scripts", "stamp.py")
# Where a finished card is delivered, stamped, so the site can never keep an older drawing.
DELIVER = {"og-site.png": os.path.join(HERE, "..", "333.eco", "static", "assets", "og.png")}


def _heart(cx, cy, k=1.0, fill="var(--accent)"):
    """build-boards.py's heart(): the B-Emblem centred by its measured bbox (brand.json mark.geometry)."""
    return ('<path transform="translate(%s %s) scale(%s) translate(-12.7237 -11.2776)" d="%s" fill="%s"/>'
            % (cx, cy, round(k * .8, 3), EMBLEM, fill))


rb.heart = _heart


def brand_fill(css):
    for k in ("bg", "ink", "ink-dim", "ink-faint", "surface", "line-strong"):
        css = css.replace("@D_%s@" % k.upper().replace("-", "_"), tok("d-" + k))
    css = css.replace("@SAPPHIRE@", tok("color-sapphire"))
    assert not re.search(r"@[A-Z_]+@", css), "unfilled brand placeholder"
    return css


SHELL = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Khmer:wght@400;600&display=swap">
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
  .km{font-family:"Noto Sans Khmer","IBM Plex Sans",sans-serif}
  .foot{position:absolute;left:92px;bottom:56px;display:flex;align-items:center;gap:14px;
        font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:22px;color:#7fa6e6}
  .rule{width:52px;height:2px;background:#7fa6e6;opacity:.5}
</style></head><body>{BODY}
<div class="foot"><span class="rule"></span>demo.333.eco</div>
</body></html>"""


def emblem(size_em=".92em"):
    return ('<svg class="em" viewBox="0 0 24 24" style="width:%s;height:%s">'
            '<path fill="currentColor" d="%s"/></svg>' % (size_em, size_em, EMBLEM))


# The live site's card: the front door's own line and ladder, in the site's dark colors. No "demo", no "drawings".
SITE_CARD = """<style>
  :root{--ink:@D_INK@;--ink-dim:@D_INK_DIM@;--ink-faint:@D_INK_FAINT@;--surface:@D_SURFACE@;
        --accent:color-mix(in oklab,@SAPPHIRE@ 55%,#ffffff);--wash:color-mix(in oklab,var(--accent) 14%,transparent)}
  body{padding:0 72px}
  body::before{background:radial-gradient(circle,color-mix(in oklab,var(--accent) 22%,transparent),transparent 62%)}
  .foot{display:none}
  .em{color:var(--accent)}
  .site{font-size:42px;font-weight:600;letter-spacing:-.01em;margin-bottom:18px}
  h1.one{font:700 73px/1.12 "IBM Plex Sans",sans-serif;letter-spacing:-.015em;white-space:nowrap;margin-bottom:36px}
  .ladder{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
  .rung{border:1.5px solid @D_LINE_STRONG@;border-radius:26px;background:var(--surface);padding:26px 28px}
  .rung.on{border-color:var(--accent);background:color-mix(in oklab,var(--accent) 14%,var(--surface))}
  .rung svg{display:block;width:252px;height:96px;margin-bottom:18px}
  .rung b{display:block;font-size:36px;font-weight:600;letter-spacing:-.01em;line-height:1.2}
  .rung span{display:block;font-size:25px;line-height:1.3;color:var(--ink-dim);margin-top:6px}
</style>"""

CARDS = {
    # The registry leads: 333.eco is the B-Registry's home, so the card names the site, not a body's wordmark.
    "og.png": '<div class="inner">'
              '<div class="site">' + emblem("1em") + '333.eco</div>'
              '<h1 style="font-size:70px;margin-bottom:22px;white-space:nowrap">Pay now. Pay later. Thank after.</h1>'
              '<p class="wide">Hold an @name or a #tag, and make your page. Drawings, in English and Khmer.</p></div>',
    "og-site.png": SITE_CARD + '<div class="inner">'
              '<div class="site">' + emblem("1em") + '333.eco</div>'
              '<h1 class="one">Pay now. Pay later. Thank after.</h1>'
              + rb.ladder() + '</div>',
}

DISCLOSED = {"og.png": "https://demo.333.eco/", "og-site.png": "https://333.eco/"}


def main():
    if not os.path.exists(CHROME):
        sys.exit("Chrome not found at %s — render the cards elsewhere." % CHROME)
    only = set(sys.argv[1:])
    for name, body in CARDS.items():
        if only and name not in only:
            continue
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "card.html")
            io.open(src, "w", encoding="utf-8").write(brand_fill(SHELL.replace("{BODY}", body)))
            out = os.path.join(HERE, name)
            subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=1", "--window-size=1200,630",
                            "--virtual-time-budget=4000",
                            "--screenshot=" + out, "file://" + src],
                           check=True, capture_output=True)
            subprocess.run([sys.executable, STAMP, out, "--source", "drawn", "--rights", "reserved",
                            "--credit", "B-Registry", "--depicts", "no identifiable person", "--consent", "n/a",
                            "--disclosure", DISCLOSED[name], "--register", "M-0019",
                            "--note", "Drawn by our own code from the brand layer's tokens and the B-Emblem; no AI."],
                           check=True, capture_output=True)
            print("%-22s %6d bytes" % (name, os.path.getsize(out)))
            if name in DELIVER and os.path.isdir(os.path.dirname(DELIVER[name])):
                shutil.copyfile(out, DELIVER[name])
                print("%-22s -> %s" % ("", os.path.relpath(DELIVER[name], HERE)))


if __name__ == "__main__":
    main()
