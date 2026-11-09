#!/usr/bin/env python3
"""earth/ has no landing page of its own: its drawings are listed on the site's one landing page (founder 2026-11-09: "merge them"). This keeps the old address working."""
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=../#earth"><link rel="canonical" href="https://demo.333.eco/#earth"><title>earth.333.eco drawings</title></head><body><p><a href="../#earth">The earth.333.eco drawings</a></p></body></html>\n')
print("earth/index.html written")
