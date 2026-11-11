# demo.333.eco/earth

> ⚠️ **2026-11-11: these drawings are a dated record, not a source.** Once a surface is live, the live site is the record of what exists; no live site is generated from these files or checked against them any more (founder: *"deprecate all source drawings everywhere; keeping the demo in sync is unrealistic"*; `/build` Default 18). A redesign starts from the live code.

Review site for `earth.333.eco`: static artboards of its public front page and of *your record* (English and Khmer, light plus one dark pass, phone and desktop).

- These are **drawings. They charge nobody** and nothing here is live. The entries shown are made up.
- Unlisted: hidden from search by named crawler in each page, no `robots.txt` (so link previews work).
- Khmer is our own and marked as a placeholder until a native reader approves it.
- Public repo: it holds drawings only. The spec lives in a private repo.
- Source of truth is this repo; the index and wall are generated from `canvas.json`. The look comes from `brand.333.eco` (`brand.lock`, `scripts/check-brand.mjs`).
- Where a drawing and the memory files disagree, memory is canonical.

    python3 build-boards.py && python3 build-icons.py && python3 build-og.py
    python3 -m http.server 8333 &
    python3 measure.py && python3 build-boards.py && python3 build-index.py && python3 build-wall.py

`Earth.html` is the 3D prototype for earth.333.eco (`earth/`, built with `npm run build` there). Every number in it is made up. It bundles three.js (MIT) and the Natural Earth land outlines (public domain, through world-atlas, ISC). It draws no national borders.
