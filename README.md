# demo.333.eco

> ⚠️ **2026-11-11: these drawings are a dated record, not a source.** Once a surface is live, the live site is the record of what exists; no live site is generated from these files or checked against them any more (founder: *"deprecate all source drawings everywhere; keeping the demo in sync is unrealistic"*; `/build` Default 18). A redesign starts from the live code.

Drawings of **the B-Registry** (hold an @name or a #tag, make your page; `registry_boards.py`) and the identity screens: **Log in with HeartBank®** (proves who you are) and **Sign with HeartBank®**
(puts your name to one file), and **developers.333.eco** (one site for every HeartBank® API, its MCP server and its sandbox; `developers_boards.py`, A600), and **B-Link at B.333.eco** (one short link for everything shared from a HeartBank® app, with the one page of storage.333.eco; `blink_boards.py`, A493 and A639), and **the B-PoH℠ app** (a press made in a phone's own secure chip; Android version 0, drawn before it is built; `poh_boards.py`, A666). English and Khmer, with one dark pass per surface. These are drawings. They charge
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
- B-Link's words are checked at build time (`blink_boards.py`, `BARRED` + `check()`): a preview states a fact and never a saving; no public page shows a count of opens; nothing is drawn as running out; no storage address is drawn.
- legal.333.eco's words, and the explorer's Legal tab (`legal_boards.py`, T1–T6 + T2D desktop, E8–E10, A709), are checked at build time (the footer too) (`BARRED` + `check()`): a legal version is timestamped, never signed at B-Origin; a timestamp always carries its limit, and *existed by* stays apart from *served from*; the footer claims only *no analytics script, no cookies*; on that host Miss Aquarius is *the CEO of HeartBank®*, never unqualified, and never a party; the 333.eco heading is never Factory 333, and the Khmer never says *every institution* (ស្ថាប័ន is the institution); the legal text stays English, word for word, on the Khmer boards. T1b and T4 are drawn AHEAD (services join as their pages move; T4 is a version after counsel's review, its record replacing the banner).
- The B-PoH℠ app's words (`poh_boards.py`, P1–P18, A666) are checked at build time (`BARRED` + `check()`): a press shows that a key in a phone's chip pressed, never a fact about the person (no *verified*, no *human*, never *bank-level*); no count, last-used or time remaining; no phone maker or model, no chip jargon, no package name or signing digest; nothing that is not in version 0 (a wallet, money, uniqueness, voting); a press through the phone's passkey sheet says the website showed the words and the app can't see them. These boards draw a NATIVE frame of their own (`poh_boards.page`); the phone's own prompts are drawn stand-ins, named so in each title.
- B-Mail's thanks (`bmail_thanks_boards.py`, CS1 · CS2 · C1 · C1b · CT1, A607) extend three live pages, so their words are copied from the live code, each key cited in the file; only the new lines are ours. Checked at build time (`BARRED` + `check()`, the footer too): the thank is never pre-selected and never pre-filled (never the primary button; the Thank opens with its words field empty and Send not pressable); 333.eco's Thank opened from a B-Mail offers no *without my name* and draws no checkbox; the check page's thank line shows only beside a passing *Signed with @x's passkey*, to that same @x; every thank link is exactly `https://333.eco/@name?thank=b-mail#thank` and never carries `from=b-mail`; the recipient's @name is never in the signed statement; Keep or give links only to B-Origin, and only when files were signed; no count, no absence, never *sign in*, never *verified*. Links on these boards are inert (`data-href`).
- The word *notary* is refused at build time. No score, grade or "unverified" badge is drawn anywhere.
- The emblem and neutrals are READ from `brand/` (`brand.py`); the only surface value is the sapphire accent block.
- The Khmer is our own draft until a native reader approves it, and every Khmer board says so.

The spec these drawings follow is private (it carries the threat model). This repo is public.

## The Khmer review of the review tool itself

`khmer/translate.333.eco/` is the native readers' review of the review tool's OWN words (its buttons, messages, instructions and the home page at translate.333.eco), founder 2026-11-21: *"add all our draft khmer to the sheet"*. Generated by `/khmer-review self-sheet` from `.claude/skills/khmer-review/page/words.json`; ⛔ never hand-edit it. No visit counter (`stamp-analytics.py` stamps only the top-level pages).
