# demo.333.eco

> ⚠️ **2026-11-11: these drawings are a dated record, not a source.** Once a surface is live, the live site is the record of what exists; no live site is generated from these files or checked against them any more (founder: *"deprecate all source drawings everywhere; keeping the demo in sync is unrealistic"*; `/build` Default 18). A redesign starts from the live code.

Drawings of **the B-Registry** (hold an @name or a #tag, make your page; `registry_boards.py`) and the identity screens: **Log in with HeartBank®** (proves who you are) and **Sign with HeartBank®**
(puts your name to one file), and **developers.333.eco** (one site for every HeartBank® API, its MCP server and its sandbox; `developers_boards.py`, A600). English and Khmer, with one dark pass per surface. These are drawings. They charge
nobody, and nothing here is live.

**Front door:** <https://demo.333.eco/> · **The wall** (every screen at once): <https://demo.333.eco/wall.html>

## Rebuild

```sh
python3 -m http.server 8333 &      # measure.py reads the boards over HTTP
python3 build-boards.py            # the boards + board.css + canvas.json, from the brand layer
python3 measure.py                 # each board's real height → heights.json (a Khmer screen is never cut)
python3 build-boards.py            # again, so canvas.json carries the measured heights
python3 build-og.py                # the link-preview card (before the index: the index stamps its hash)
python3 build-index.py && python3 build-wall.py   # the front door and the wall, generated from canvas.json
node scripts/check-brand.mjs       # the vendored brand layer still matches brand.lock
```

⛔ Never hand-edit a generated file (`*.html`, `board.css`, `canvas.json`, `heights.json`). Edit `build-boards.py`.

## Rules the generator enforces

- **Log in** authenticates and **Sign** attests. The phrase *sign in* is refused at build time, in either language.
- The registry's words are checked at build time (`registry_boards.py`, `BARRED`): no gift or donation language for a fee, no name reported as gone for good, no banking word, no ticking clock.
- developers.333.eco's words are checked at build time (`developers_boards.py`, `BARRED` + `check()`): no real company, product or model named; no streak, ranking or countdown; a B-Trace check through the API is drawn as METERED (only a signature's verification is free).
- The word *notary* is refused at build time. No score, grade or "unverified" badge is drawn anywhere.
- The emblem and neutrals are READ from `brand/` (`brand.py`); the only surface value is the sapphire accent block.
- The Khmer is our own draft until a native reader approves it, and every Khmer board says so.

The spec these drawings follow is private (it carries the threat model). This repo is public.
