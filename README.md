# demo.333.eco

Drawings of the `b.333.eco` screens: **Log in with HeartBank®** (proves who you are) and **Sign with HeartBank®**
(puts your name to one file). English and Khmer, with one dark pass per surface. These are drawings. They charge
nobody, and nothing here is live.

**Front door:** <https://demo.333.eco/> · **The wall** (every screen at once): <https://demo.333.eco/wall.html>

## Rebuild

```sh
python3 -m http.server 8333 &      # measure.py reads the boards over HTTP
python3 build-boards.py            # the boards + board.css + canvas.json, from the brand layer
python3 measure.py                 # each board's real height → heights.json (a Khmer screen is never cut)
python3 build-boards.py            # again, so canvas.json carries the measured heights
python3 build-index.py && python3 build-wall.py   # the front door and the wall, generated from canvas.json
python3 build-og.py                # the link-preview card
node scripts/check-brand.mjs       # the vendored brand layer still matches brand.lock
```

⛔ Never hand-edit a generated file (`*.html`, `board.css`, `canvas.json`, `heights.json`). Edit `build-boards.py`.

## Rules the generator enforces

- **Log in** authenticates and **Sign** attests. The phrase *sign in* is refused at build time, in either language.
- The word *notary* is refused at build time. No score, grade or "unverified" badge is drawn anywhere.
- The emblem and neutrals are READ from `brand/` (`brand.py`); the only surface value is the sapphire accent block.
- The Khmer is our own draft until a native reader approves it, and every Khmer board says so.

The spec these drawings follow is private (it carries the threat model). This repo is public.
