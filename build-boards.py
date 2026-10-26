#!/usr/bin/env python3
"""Generate the b.333.eco artboards (Log in with HeartBank® · Sign with HeartBank®) and canvas.json.

    python3 build-boards.py && python3 build-index.py && python3 build-wall.py

The spec is private (it carries the threat model); these drawings follow it.
The brand layer, vendored under brand/ and guarded by scripts/check-brand.mjs: the emblem and the neutrals are READ
from it (brand.py), never typed here. This surface's own values are the ONE marked block in CSS below.

Copy rules this file must keep:
  - "Log in" authenticates, "Sign" attests. ⛔ "sign in" never appears, in either language.
  - ⛔ never "notary"; ⛔ no score, grade, badge or "unverified" state; a fact is stated once, never animated.
  - a record shows who SIGNED, never who imagined; the source is IPTC's own label.
The Khmer is OURS and UNREVIEWED; every Khmer board says so in its top band.
"""
import io, json, os, re
from brand import EMBLEM, tok

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 390, 844

CSS = """
:root{
  --bg:@L_BG@; --surface:@L_SURFACE@; --surface-2:@L_SURFACE_2@; --line:@L_LINE@; --line-strong:@L_LINE_STRONG@;
  --ink:@L_INK@; --ink-dim:@L_INK_DIM@; --ink-faint:@L_INK_FAINT@;
  /* ── this surface's own (b.333.eco): the accent 333.eco already wears, the brand layer's sapphire gem ── */
  --accent:@SAPPHIRE@; --accent-ink:#ffffff;
  --wash:color-mix(in oklab,var(--accent) 9%,transparent); --edge:color-mix(in oklab,var(--accent) 30%,transparent);
  /* ─────────────────────────────────────────────────────────────────────────────────────────────────────── */
  --font-text:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif; --font-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  --font-khmer:"Noto Sans Khmer","Khmer Sangam MN",sans-serif; --r:16px; --r-pill:999px;
}
.dark{
  --bg:@D_BG@; --surface:@D_SURFACE@; --surface-2:@D_SURFACE_2@; --line:@D_LINE@; --line-strong:@D_LINE_STRONG@;
  --ink:@D_INK@; --ink-dim:@D_INK_DIM@; --ink-faint:@D_INK_FAINT@;
  --accent:color-mix(in oklab,@SAPPHIRE@ 55%,#ffffff); --accent-ink:@D_BG@;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg)}
body{width:390px;min-height:844px;color:var(--ink);font:15px/1.5 var(--font-text);-webkit-font-smoothing:antialiased}
.km body,body.km{font-family:var(--font-khmer),var(--font-text);line-height:1.7}
.band{background:var(--surface-2);color:var(--ink-dim);font-size:11px;padding:6px 20px;text-align:center}
.app{padding:0 20px 28px;min-height:820px;display:flex;flex-direction:column}
header{display:flex;align-items:center;justify-content:space-between;padding:18px 0 10px}
.wordmark{font-weight:600;font-size:1.15rem;white-space:nowrap;letter-spacing:-.01em;
  --emblem-cap:.68em;--emblem-size:calc(var(--emblem-cap)*1.1);--emblem-box:calc(var(--emblem-size)/.7534)}
.wordmark svg{width:var(--emblem-box);height:var(--emblem-box);color:var(--accent);vertical-align:baseline;
  margin-top:calc(var(--emblem-box)*-.09312);margin-bottom:calc(var(--emblem-box)*-.15333);
  margin-left:calc(var(--emblem-box)*-.15343 + 1px);margin-right:calc(var(--emblem-box)*-.09312 - 1px)}
.wordmark sup{font-size:.55em;font-weight:500;vertical-align:.62em;margin-left:.06em;line-height:0}
.seg{display:inline-flex;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:2px;font-size:12px}
.seg span{padding:3px 10px;border-radius:var(--r-pill);color:var(--ink-dim)}
.seg span.on{background:var(--ink);color:var(--bg)}
.from{display:flex;align-items:center;gap:10px;margin:14px 0 6px;color:var(--ink-dim);font-size:13px}
.from .site{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:var(--r-pill);
  padding:4px 12px 4px 4px;color:var(--ink);font-weight:500}
.from .site i{width:22px;height:22px;border-radius:50%;background:var(--surface-2);display:grid;place-items:center;
  font:600 10px var(--font-mono);font-style:normal;color:var(--ink-dim)}
h1{font-size:26px;line-height:1.2;margin:14px 0 6px;letter-spacing:-.015em}
.lede{color:var(--ink-dim);margin:0 0 18px}
.card{border:1px solid var(--line);border-radius:var(--r);background:var(--surface);padding:16px;margin:0 0 12px}
.card h2{font-size:14px;margin:0 0 6px}
.card p{margin:0;color:var(--ink-dim);font-size:14px}
.spot{display:block;margin:0 0 10px}
.row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-top:1px solid var(--line)}
.row:first-of-type{border-top:0}
.row .t{font-size:14px}.row .s{font-size:12.5px;color:var(--ink-dim)}
.tog{width:44px;height:26px;border-radius:13px;background:var(--line-strong);position:relative;flex:none}
.tog::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff}
.tog.on{background:var(--accent)}.tog.on::after{left:21px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.chip{border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:6px 12px;font-size:13px;color:var(--ink-dim)}
.chip.on{border-color:var(--accent);background:var(--wash);color:var(--ink);font-weight:500}
.btn{display:block;width:100%;border:0;border-radius:14px;padding:15px;font:600 16px var(--font-text);text-align:center;
  background:var(--accent);color:var(--accent-ink);margin:8px 0 0}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line-strong)}
.btn svg{vertical-align:-3px;margin-right:6px}
.fine{color:var(--ink-dim);font-size:12.5px;margin:14px 0 0}
.grow{flex:1}
.thumb{display:flex;gap:14px;align-items:center}
.thumb svg{flex:none;border-radius:10px;border:1px solid var(--line)}
.kv{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:13.5px;margin-top:10px}
.kv dt{color:var(--ink-dim)}.kv dd{margin:0}
.mono{font-family:var(--font-mono);font-size:12.5px}
.field{border:1px solid var(--line-strong);border-radius:12px;padding:12px 14px;background:var(--bg);font-size:15px;margin-top:8px}
.field.area{min-height:96px;color:var(--ink-dim);font-size:14px}
.check{display:flex;gap:10px;align-items:flex-start;font-size:14px;margin-top:12px}
.check b{flex:none;width:20px;height:20px;border-radius:6px;border:1.5px solid var(--accent);background:var(--accent);
  color:var(--accent-ink);display:grid;place-items:center;font-size:12px}
.note{border-left:3px solid var(--accent);background:var(--wash);border-radius:0 12px 12px 0;padding:12px 14px;font-size:14px;margin:0 0 12px}
.more{margin:12px 0 0;color:var(--accent);font-weight:600;font-size:14px}
.scrim{position:absolute;inset:0;background:color-mix(in oklab,var(--ink) 38%,transparent)}
.app{position:relative}
.sheet{position:absolute;left:0;right:0;top:96px;padding:10px 20px 28px;background:var(--bg);border-radius:22px 22px 0 0;
  box-shadow:0 -8px 30px rgba(0,0,0,.18)}
.grab{width:40px;height:5px;border-radius:3px;background:var(--line-strong);margin:0 auto 6px}
.sh{font-size:13px;letter-spacing:.02em;color:var(--ink-dim);margin:16px 0 6px;text-transform:uppercase}
.km .sh{text-transform:none;letter-spacing:0}
.ticks,.dots{list-style:none;margin:0;padding:0}
.ticks li,.dots li{display:flex;gap:10px;align-items:flex-start;padding:6px 0;font-size:14px}
.ticks svg{flex:none;margin-top:2px}
.dots i{flex:none;width:6px;height:6px;border-radius:50%;background:var(--ink-faint);margin:9px 6px 0}
.pill{flex:none;font-size:12px;border:1px solid var(--line-strong);border-radius:999px;padding:3px 10px;color:var(--ink-dim)}
.pill.on{border-color:var(--accent);color:var(--accent);font-weight:600}
footer{display:flex;align-items:center;justify-content:space-between;gap:10px;border-top:1px solid var(--line);
  padding-top:14px;margin-top:20px;color:var(--ink-faint);font-size:11.5px}
"""


def brand_css(css):
    for k in ("bg", "surface", "surface-2", "line", "line-strong", "ink", "ink-dim", "ink-faint"):
        for p in ("l", "d"):
            css = css.replace("@%s_%s@" % (p.upper(), k.upper().replace("-", "_")), tok("%s-%s" % (p, k)))
    css = css.replace("@SAPPHIRE@", tok("color-sapphire"))
    assert not re.search(r"@[A-Z_0-9]+@", css), "unfilled brand placeholder"
    return css


def mark():
    return ('<span class="wordmark">Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/>'
            '</svg>ank<sup>®</sup></span>' % EMBLEM)


def heart(cx, cy, k=1.0, fill="var(--accent)"):
    """The B-Emblem, centred by its measured bbox (brand.json mark.geometry), at .8 of a stock heart's width."""
    return ('<path transform="translate(%s %s) scale(%s) translate(-12.7237 -11.2776)" d="%s" fill="%s"/>'
            % (cx, cy, round(k * .8, 3), EMBLEM, fill))


# ── spot drawings (flat, from the tokens; one per info card) ──────────────────────────────────────────────────────
def spot(kind):
    s = ['<svg class="spot" width="56" height="40" viewBox="0 0 56 40" aria-hidden="true">']
    if kind == "key":       # a passkey: a phone holding a key
        s += ['<rect x="4" y="2" width="22" height="36" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<circle cx="15" cy="17" r="5" fill="none" stroke="var(--accent)" stroke-width="2.5"/>',
              '<path d="M18.5 20.5 L24 26 M22 24 L24.5 21.5" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/>',
              '<path d="M32 14 h18 M32 21 h14 M32 28 h16" stroke="var(--line-strong)" stroke-width="2.5" stroke-linecap="round"/>']
    elif kind == "split":   # a pairwise ID: one person, two different keys
        s += ['<circle cx="28" cy="20" r="7" fill="var(--accent)"/>',
              '<path d="M21 20 L8 10 M35 20 L48 10" stroke="var(--line-strong)" stroke-width="2"/>',
              '<rect x="1" y="4" width="13" height="10" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<rect x="42" y="4" width="13" height="10" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M4 9 h7 M45 9 h7" stroke="var(--ink-faint)" stroke-width="1.6"/>']
    elif kind == "log":     # the public log: a stack of entries
        s += ['<rect x="8" y="4" width="40" height="9" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<rect x="8" y="16" width="40" height="9" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<rect x="8" y="28" width="40" height="9" rx="3" fill="var(--wash)" stroke="var(--accent)"/>',
              heart(15, 32.5, .38)]
    elif kind == "two":     # two devices
        s += ['<rect x="6" y="6" width="16" height="28" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<rect x="28" y="10" width="22" height="16" rx="2" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M25 30 h28" stroke="var(--line-strong)" stroke-width="2.5" stroke-linecap="round"/>',
              heart(14, 20, .45), heart(39, 18, .45)]
    s.append('</svg>')
    return "".join(s)


def sunflower(px=72):
    """A small pixel-art sunflower: the file being signed (drawn, a stand-in for the person's own work)."""
    grid = ["....YYYY....", "..YYYYYYYY..", ".YYYBBBBYYY.", ".YYBBBBBBYY.", "YYBBBBBBBBYY", "YYBBBBBBBBYY",
            ".YYBBBBBBYY.", ".YYYBBBBYYY.", "..YYYYYYYY..", "....GG.LL...", "...LGG.LLL..", "....GG......"]
    col = {"Y": "#f2b632", "B": "#6b3f1d", "G": "#3f7d3a", "L": "#5fa04e"}
    c = px / 12.0
    r = ['<svg width="%d" height="%d" viewBox="0 0 %d %d" aria-hidden="true" style="background:#fff6df">' % (px, px, px, px)]
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch in col:
                r.append('<rect x="%.1f" y="%.1f" width="%.2f" height="%.2f" fill="%s"/>' % (x * c, y * c, c + .2, c + .2, col[ch]))
    r.append('</svg>')
    return "".join(r)


KEY = ('<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="5" fill="none" '
       'stroke="currentColor" stroke-width="2.4"/><path d="M13 12h9M19 12v4M16 12v3" stroke="currentColor" '
       'stroke-width="2.4" stroke-linecap="round"/></svg>')

# ── the copy ─────────────────────────────────────────────────────────────────────────────────────────────────────
T = {
 "en": {
  "band": "", "lang": ("EN", "ខ្មែរ"), "theme": ("System", "Light", "Dark"),
  "foot": "B.333.eco · passkeys only · no password, no email",
  "from": "Asked by",
  # L1
  "l1_h": "Log in to 333.eco", "l1_lede": "with your HeartBank® passkey.",
  "l1_c1h": "No password to steal", "l1_c1p": "Your phone holds your passkey and unlocks it with its own screen lock. It never leaves the phone.",
  "l1_c2h": "A private ID for each site", "l1_c2p": "333.eco gets an ID made only for it. Other sites can't use it to follow you.",
  "l1_btn": "Log in with passkey", "l1_new": "New here? Make a passkey",
  # L2
  "l2_h": "Make your passkey", "l2_lede": "It takes one tap. We never ask for your name, email or phone number.",
  "l2_c1h": "What happens", "l2_c1p": "Your phone makes a key that only it holds. We keep only the public half, which can check a signature but never make one.",
  "l2_age": "I am 18 or older.", "l2_btn": "Make my passkey",
  # L3
  "l3_h": "Accounts start at 18, for now", "l3_lede": "HeartBank® accounts are for adults while we work out the right way to include younger people.",
  "l3_c1h": "If you're younger", "l3_c1p": "Show this to a parent or guardian. Nothing about you was saved.",
  "l3_btn": "Back to 333.eco",
  # L4
  "l4_h": "333.eco would like to know", "l4_lede": "Share only what you choose. You can change it any time in your account.",
  "l4_r1t": "That you have a HeartBank® passkey", "l4_r1s": "Yes or no. Nothing else about you.",
  "l4_r2t": "Your @handle", "l4_r2s": "Your public name in the registry.",
  "l4_c1h": "Its own ID for you", "l4_c1p": "333.eco can't link this ID to any other site you log in to.",
  "l4_btn": "Continue", "l4_no": "Not now",
  # L5
  "l5_h": "You're logged in", "l5_lede": "333.eco now knows it's you.",
  "l5_c1h": "Add a second passkey", "l5_c1p": "This is your only passkey. Add one on another device so losing this phone can't cost you your account or your signed works.",
  "l5_btn": "Add another device", "l5_no": "Later",
  # L6
  "l6_h": "Your account", "l6_lede": "Everything we hold about you is on this page.",
  "l6_pk": "Passkeys", "l6_pk1": ("iPhone", "Added 25 Oct 2026"), "l6_pk2": ("MacBook", "Added 25 Oct 2026"),
  "l6_st": "Sites you log in to", "l6_st1": ("333.eco", "Shares: has a passkey"), "l6_change": "Change",
  "l6_wk": "Your signed works", "l6_wk1": ("sunflower.png", "Signed 25 Oct 2026"),
  "l6_q": "Who checked a fact about you", "l6_q1": ("333.eco", "Checked: has a passkey · 25 Oct"),
  # S1
  "s_from": "dpixxi", "s1_h": "Sign this file", "s1_lede": "dpixxi asks you to put your name to it.",
  "s1_kvm": "How it was made", "s1_kvmv": "Digital creation", "s1_kvf": "File", "s1_kvt": "Tool", "s1_kvtv": "dpixxi editor",
  "s1_hint": "dpixxi read this from the editor's own history.",
  "s1_rh": "Share it under", "s1_r": ("CC0", "CC BY 4.0", "All rights reserved"),
  "s1_note": "Signing adds a public record: who signed, when, and how it was made. It shows that you signed it, not that you imagined it.",
  "s1_btn": "Sign with passkey", "s1_fine": "Your file stays on your device. Only its fingerprint is sent.",
  # S2
  "s2_h": "Signed", "s2_lede": "A record of this file is now in the public log.",
  "s2_kv": (("Signed by", "a person with a HeartBank® passkey"), ("On", "25 Oct 2026, 2:14 pm"), ("How", "Digital creation"),
            ("Shared under", "CC BY 4.0"), ("Record", "7f3a 91c2 … c21e")),
  "s2_c1h": "Anyone can check it", "s2_c1p": "At origin.333.eco, or with the free verify package. Checking the signature never needs us online.",
  "s2_btn": "Done", "s2_no": "Show my @handle on it",
  "s2_more": "What this record shows ›",
  "s7_h": "What this record shows", "s7_has": "This record carries",
  "s7_has_i": ("A passkey on an approved phone or computer, unlocked by its owner at the moment of signing",
               "The file's fingerprint, which matches only this picture",
               "The time, anchored to Bitcoin every day",
               "Co-signatures from independent witnesses, so the log can't be quietly changed"),
  "s7_not": "What a record can't show", "s7_not_i": ("Who imagined the work", "That this person holds only one account"),
  "s7_today": "What HeartBank® can prove today",
  "s7_today_i": (("A passkey on an approved device", "Live"), ("A family tree vouched for by relatives", "Being built"),
                 ("Live breath, from a wearable heart", "Planned"), ("A family tree checked by DNA", "Planned")),
  "s7_fine": "Every layer is optional. None is needed to sign.", "s7_btn": "Close",
  # S3
  "s3_h": "Withdraw this record?", "s3_lede": "sunflower.png · signed 25 Oct 2026",
  "s3_c1h": "Nothing is erased", "s3_c1p": "The record stays in the public log, marked “withdrawn by the signer on 25 Oct 2026”. Your @handle comes off it everywhere.",
  "s3_btn": "Withdraw", "s3_no": "Keep it",
  # S4
  "s4_h": "A device lost or stolen?", "s4_lede": "Remove its passkey, and withdraw what it signed after a time you choose.",
  "s4_dev": "Device", "s4_devv": "iPhone", "s4_after": "Withdraw everything it signed after", "s4_afterv": "24 Oct 2026, 6:00 pm",
  "s4_c1h": "What stays", "s4_c1p": "Records signed before that time stay valid. This adds one entry to the public log.",
  "s4_btn": "Remove passkey and withdraw",
  # S5
  "s5_h": "Bring your works back", "s5_lede": "Lost every passkey? Prove you own your @handle, and the works signed under it follow.",
  "s5_field": "@handle", "s5_fieldv": "@thon",
  "s5_c1h": "Works with no @handle", "s5_c1p": "They stay valid and anyone can still check them, but they can't be moved to a new account.",
  "s5_btn": "Prove it with the registry",
  # S6
  "s6_h": "Dispute this record", "s6_lede": "sunflower.png · signed with a HeartBank® passkey · 25 Oct 2026",
  "s6_c1h": "HeartBank® never decides", "s6_c1p": "Your statement is added to the public log beside the record. Anyone checking the file sees both.",
  "s6_field": "What you say", "s6_fieldv": "I drew this in March 2026. My own record of it is 1b9e … 44d0.",
  "s6_btn": "Sign my statement",
 },
 "km": {
  "band": "ភាសាខ្មែរ៖ សេចក្ដីព្រាងរបស់យើង មិនទាន់ពិនិត្យដោយអ្នកនិយាយភាសាកំណើត · Khmer: our draft, not yet reviewed",
  "lang": ("EN", "ខ្មែរ"), "theme": ("ប្រព័ន្ធ", "ភ្លឺ", "ងងឹត"),
  "foot": "B.333.eco · ប្រើតែ passkey · គ្មានពាក្យសម្ងាត់ គ្មានអ៊ីមែល",
  "from": "ស្នើដោយ",
  "l1_h": "ចូលទៅ 333.eco", "l1_lede": "ដោយប្រើ passkey HeartBank® របស់អ្នក។",
  "l1_c1h": "គ្មានពាក្យសម្ងាត់ឱ្យគេលួច", "l1_c1p": "ទូរសព្ទរបស់អ្នករក្សា passkey ហើយបើកវាដោយសោអេក្រង់របស់ទូរសព្ទផ្ទាល់។ វាមិនដែលចេញពីទូរសព្ទឡើយ។",
  "l1_c2h": "លេខសម្គាល់ដាច់ដោយឡែកសម្រាប់គេហទំព័រនីមួយៗ", "l1_c2p": "333.eco ទទួលបានលេខសម្គាល់ដែលបង្កើតសម្រាប់វាតែប៉ុណ្ណោះ។ គេហទំព័រផ្សេងមិនអាចប្រើវាដើម្បីតាមដានអ្នកបានទេ។",
  "l1_btn": "ចូលដោយប្រើ passkey", "l1_new": "ទើបមកដំបូង? បង្កើត passkey",
  "l2_h": "បង្កើត passkey របស់អ្នក", "l2_lede": "ចុចតែម្ដង។ យើងមិនសួររកឈ្មោះ អ៊ីមែល ឬលេខទូរសព្ទរបស់អ្នកឡើយ។",
  "l2_c1h": "អ្វីដែលកើតឡើង", "l2_c1p": "ទូរសព្ទរបស់អ្នកបង្កើតកូនសោដែលមានតែវាប៉ុណ្ណោះកាន់។ យើងរក្សាទុកតែពាក់កណ្ដាលសាធារណៈ ដែលអាចពិនិត្យហត្ថលេខាបាន ប៉ុន្តែមិនអាចបង្កើតហត្ថលេខាបានទេ។",
  "l2_age": "ខ្ញុំមានអាយុ ១៨ ឆ្នាំ ឬលើសពីនេះ។", "l2_btn": "បង្កើត passkey របស់ខ្ញុំ",
  "l3_h": "គណនីចាប់ពីអាយុ ១៨ ឆ្នាំ សម្រាប់ពេលនេះ", "l3_lede": "គណនី HeartBank® សម្រាប់មនុស្សពេញវ័យ ខណៈដែលយើងកំពុងរកវិធីត្រឹមត្រូវដើម្បីទទួលយកអ្នកដែលក្មេងជាងនេះ។",
  "l3_c1h": "ប្រសិនបើអ្នកនៅក្មេង", "l3_c1p": "សូមបង្ហាញទំព័រនេះទៅឪពុកម្ដាយ ឬអាណាព្យាបាល។ គ្មានអ្វីអំពីអ្នកត្រូវបានរក្សាទុកទេ។",
  "l3_btn": "ត្រឡប់ទៅ 333.eco",
  "l4_h": "333.eco ចង់ដឹង", "l4_lede": "ចែករំលែកតែអ្វីដែលអ្នកជ្រើសរើស។ អ្នកអាចប្ដូរវាបានគ្រប់ពេលក្នុងគណនីរបស់អ្នក។",
  "l4_r1t": "ថាអ្នកមាន passkey HeartBank®", "l4_r1s": "បាទ/ចាស ឬទេ។ គ្មានអ្វីផ្សេងអំពីអ្នកឡើយ។",
  "l4_r2t": "@handle របស់អ្នក", "l4_r2s": "ឈ្មោះសាធារណៈរបស់អ្នកក្នុងបញ្ជី។",
  "l4_c1h": "លេខសម្គាល់ផ្ទាល់ខ្លួនសម្រាប់អ្នក", "l4_c1p": "333.eco មិនអាចភ្ជាប់លេខសម្គាល់នេះទៅគេហទំព័រផ្សេងទៀតដែលអ្នកចូលបានទេ។",
  "l4_btn": "បន្ត", "l4_no": "មិនមែនឥឡូវទេ",
  "l5_h": "អ្នកបានចូលហើយ", "l5_lede": "ឥឡូវនេះ 333.eco ដឹងថាជាអ្នក។",
  "l5_c1h": "បន្ថែម passkey ទីពីរ", "l5_c1p": "នេះជា passkey តែមួយគត់របស់អ្នក។ បន្ថែមមួយទៀតនៅលើឧបករណ៍ផ្សេង ដើម្បីកុំឱ្យការបាត់ទូរសព្ទនេះធ្វើឱ្យអ្នកបាត់គណនី ឬស្នាដៃដែលអ្នកបានចុះហត្ថលេខា។",
  "l5_btn": "បន្ថែមឧបករណ៍មួយទៀត", "l5_no": "ពេលក្រោយ",
  "l6_h": "គណនីរបស់អ្នក", "l6_lede": "អ្វីៗទាំងអស់ដែលយើងរក្សាទុកអំពីអ្នក មាននៅលើទំព័រនេះ។",
  "l6_pk": "Passkeys", "l6_pk1": ("iPhone", "បានបន្ថែម ២៥ តុលា ២០២៦"), "l6_pk2": ("MacBook", "បានបន្ថែម ២៥ តុលា ២០២៦"),
  "l6_st": "គេហទំព័រដែលអ្នកចូល", "l6_st1": ("333.eco", "ចែករំលែក៖ មាន passkey"), "l6_change": "ប្ដូរ",
  "l6_wk": "ស្នាដៃដែលអ្នកបានចុះហត្ថលេខា", "l6_wk1": ("sunflower.png", "ចុះហត្ថលេខា ២៥ តុលា ២០២៦"),
  "l6_q": "អ្នកដែលបានពិនិត្យការពិតអំពីអ្នក", "l6_q1": ("333.eco", "បានពិនិត្យ៖ មាន passkey · ២៥ តុលា"),
  "s_from": "dpixxi", "s1_h": "ចុះហត្ថលេខាលើឯកសារនេះ", "s1_lede": "dpixxi សុំឱ្យអ្នកដាក់ឈ្មោះរបស់អ្នកលើវា។",
  "s1_kvm": "របៀបដែលវាត្រូវបានបង្កើត", "s1_kvmv": "ការបង្កើតឌីជីថល (Digital creation)", "s1_kvf": "ឯកសារ", "s1_kvt": "ឧបករណ៍", "s1_kvtv": "កម្មវិធីកែ dpixxi",
  "s1_hint": "dpixxi អានព័ត៌មាននេះពីប្រវត្តិរបស់កម្មវិធីកែផ្ទាល់។",
  "s1_rh": "ចែករំលែកក្រោម", "s1_r": ("CC0", "CC BY 4.0", "រក្សាសិទ្ធិគ្រប់យ៉ាង"),
  "s1_note": "ការចុះហត្ថលេខាបន្ថែមកំណត់ត្រាសាធារណៈ៖ អ្នកណាចុះហត្ថលេខា ពេលណា និងរបៀបដែលវាត្រូវបានបង្កើត។ វាបង្ហាញថាអ្នកបានចុះហត្ថលេខា មិនមែនថាអ្នកជាអ្នកគិតវាឡើងទេ។",
  "s1_btn": "ចុះហត្ថលេខាដោយ passkey", "s1_fine": "ឯកសាររបស់អ្នកនៅលើឧបករណ៍របស់អ្នក។ មានតែស្នាមម្រាមដៃឌីជីថលរបស់វាប៉ុណ្ណោះដែលត្រូវបានផ្ញើ។",
  "s2_h": "បានចុះហត្ថលេខា", "s2_lede": "កំណត់ត្រានៃឯកសារនេះ ឥឡូវមាននៅក្នុងបញ្ជីសាធារណៈ។",
  "s2_kv": (("ចុះហត្ថលេខាដោយ", "មនុស្សដែលមាន passkey HeartBank®"), ("នៅ", "២៥ តុលា ២០២៦ ម៉ោង ២:១៤ រសៀល"), ("របៀប", "ការបង្កើតឌីជីថល"),
            ("ចែករំលែកក្រោម", "CC BY 4.0"), ("កំណត់ត្រា", "7f3a 91c2 … c21e")),
  "s2_c1h": "អ្នកណាក៏អាចពិនិត្យវាបាន", "s2_c1p": "នៅ origin.333.eco ឬដោយកញ្ចប់ verify ឥតគិតថ្លៃ។ ការពិនិត្យហត្ថលេខាមិនត្រូវការយើងនៅលើបណ្ដាញទេ។",
  "s2_btn": "រួចរាល់", "s2_no": "បង្ហាញ @handle របស់ខ្ញុំលើវា",
  "s2_more": "អ្វីដែលកំណត់ត្រានេះបង្ហាញ ›",
  "s7_h": "អ្វីដែលកំណត់ត្រានេះបង្ហាញ", "s7_has": "កំណត់ត្រានេះមាន",
  "s7_has_i": ("passkey នៅលើទូរសព្ទ ឬកុំព្យូទ័រដែលបានអនុម័ត ដែលម្ចាស់បានបើកនៅពេលចុះហត្ថលេខា",
               "ស្នាមម្រាមដៃឌីជីថលរបស់ឯកសារ ដែលត្រូវគ្នាតែនឹងរូបភាពនេះប៉ុណ្ណោះ",
               "ពេលវេលា ដែលបានភ្ជាប់ទៅ Bitcoin រៀងរាល់ថ្ងៃ",
               "ហត្ថលេខារួមពីសាក្សីឯករាជ្យ ដើម្បីកុំឱ្យបញ្ជីអាចត្រូវបានប្ដូរដោយស្ងាត់ៗ"),
  "s7_not": "អ្វីដែលកំណត់ត្រាមិនអាចបង្ហាញ", "s7_not_i": ("អ្នកណាជាអ្នកគិតស្នាដៃនេះ", "ថាមនុស្សនេះមានគណនីតែមួយប៉ុណ្ណោះ"),
  "s7_today": "អ្វីដែល HeartBank® អាចបង្ហាញភស្តុតាងបាននៅថ្ងៃនេះ",
  "s7_today_i": (("passkey នៅលើឧបករណ៍ដែលបានអនុម័ត", "ដំណើរការ"), ("មែកធាងគ្រួសារ ដែលសាច់ញាតិធានា", "កំពុងសាងសង់"),
                 ("ដង្ហើមផ្ទាល់ ពីបេះដូងដែលពាក់ជាប់ខ្លួន", "គ្រោងទុក"), ("មែកធាងគ្រួសារ ដែលពិនិត្យដោយ DNA", "គ្រោងទុក")),
  "s7_fine": "ស្រទាប់នីមួយៗជាជម្រើស។ មិនត្រូវការស្រទាប់ណាមួយដើម្បីចុះហត្ថលេខាទេ។", "s7_btn": "បិទ",
  "s3_h": "ដកកំណត់ត្រានេះវិញ?", "s3_lede": "sunflower.png · ចុះហត្ថលេខា ២៥ តុលា ២០២៦",
  "s3_c1h": "គ្មានអ្វីត្រូវបានលុបទេ", "s3_c1p": "កំណត់ត្រានៅតែមានក្នុងបញ្ជីសាធារណៈ ដោយមានសម្គាល់ថា «បានដកវិញដោយអ្នកចុះហត្ថលេខា នៅ ២៥ តុលា ២០២៦»។ @handle របស់អ្នកត្រូវបានដកចេញពីវានៅគ្រប់កន្លែង។",
  "s3_btn": "ដកវិញ", "s3_no": "រក្សាទុក",
  "s4_h": "ឧបករណ៍បាត់ ឬត្រូវគេលួច?", "s4_lede": "ដក passkey របស់វាចេញ ហើយដកវិញនូវអ្វីដែលវាបានចុះហត្ថលេខា បន្ទាប់ពីពេលដែលអ្នកជ្រើស។",
  "s4_dev": "ឧបករណ៍", "s4_devv": "iPhone", "s4_after": "ដកវិញនូវអ្វីៗដែលវាបានចុះហត្ថលេខាបន្ទាប់ពី", "s4_afterv": "២៤ តុលា ២០២៦ ម៉ោង ៦:០០ ល្ងាច",
  "s4_c1h": "អ្វីដែលនៅដដែល", "s4_c1p": "កំណត់ត្រាដែលបានចុះហត្ថលេខាមុនពេលនោះ នៅតែមានសុពលភាព។ សកម្មភាពនេះបន្ថែមធាតុមួយទៅក្នុងបញ្ជីសាធារណៈ។",
  "s4_btn": "ដក passkey និងដកវិញ",
  "s5_h": "នាំស្នាដៃរបស់អ្នកមកវិញ", "s5_lede": "បាត់ passkey ទាំងអស់? បង្ហាញថាអ្នកជាម្ចាស់ @handle របស់អ្នក ហើយស្នាដៃដែលបានចុះហត្ថលេខាក្រោមវានឹងមកតាម។",
  "s5_field": "@handle", "s5_fieldv": "@thon",
  "s5_c1h": "ស្នាដៃដែលគ្មាន @handle", "s5_c1p": "វានៅតែមានសុពលភាព ហើយអ្នកណាក៏នៅតែអាចពិនិត្យបាន ប៉ុន្តែមិនអាចផ្លាស់ទៅគណនីថ្មីបានទេ។",
  "s5_btn": "បង្ហាញភស្តុតាងតាមរយៈបញ្ជី",
  "s6_h": "ជំទាស់នឹងកំណត់ត្រានេះ", "s6_lede": "sunflower.png · ចុះហត្ថលេខាដោយ passkey HeartBank® · ២៥ តុលា ២០២៦",
  "s6_c1h": "HeartBank® មិនដែលសម្រេចទេ", "s6_c1p": "សេចក្ដីថ្លែងរបស់អ្នកត្រូវបានបន្ថែមទៅក្នុងបញ្ជីសាធារណៈ នៅក្បែរកំណត់ត្រា។ អ្នកណាដែលពិនិត្យឯកសារនឹងឃើញទាំងពីរ។",
  "s6_field": "អ្វីដែលអ្នកនិយាយ", "s6_fieldv": "ខ្ញុំគូរវានៅខែមីនា ២០២៦។ កំណត់ត្រារបស់ខ្ញុំគឺ 1b9e … 44d0។",
  "s6_btn": "ចុះហត្ថលេខាលើសេចក្ដីថ្លែងរបស់ខ្ញុំ",
 },
}

# ── screens ──────────────────────────────────────────────────────────────────────────────────────────────────────
def frm(t, site, mono):
    return '<div class="from">%s <span class="site"><i>%s</i>%s</span></div>' % (t["from"], mono, site)


def card(h, p, kind=None):
    return '<div class="card">%s<h2>%s</h2><p>%s</p></div>' % (spot(kind) if kind else "", h, p)


def btns(a, b=None, key=False):
    s = '<button class="btn">%s%s</button>' % (KEY if key else "", a)
    return s + ('<button class="btn ghost">%s</button>' % b if b else "")


def L1(t): return (frm(t, "333.eco", "333") + "<h1>%s</h1><p class='lede'>%s</p>" % (t["l1_h"], t["l1_lede"])
                   + card(t["l1_c1h"], t["l1_c1p"], "key") + card(t["l1_c2h"], t["l1_c2p"], "split")
                   + '<div class="grow"></div>' + btns(t["l1_btn"], t["l1_new"], key=True))
def L2(t): return (frm(t, "333.eco", "333") + "<h1>%s</h1><p class='lede'>%s</p>" % (t["l2_h"], t["l2_lede"])
                   + card(t["l2_c1h"], t["l2_c1p"], "key")
                   + '<div class="check"><b>✓</b><span>%s</span></div>' % t["l2_age"]
                   + '<div class="grow"></div>' + btns(t["l2_btn"], key=True))
def L3(t): return (frm(t, "333.eco", "333") + "<h1>%s</h1><p class='lede'>%s</p>" % (t["l3_h"], t["l3_lede"])
                   + card(t["l3_c1h"], t["l3_c1p"]) + '<div class="grow"></div>' + btns(t["l3_btn"]))
def L4(t): return (frm(t, "333.eco", "333") + "<h1>%s</h1><p class='lede'>%s</p>" % (t["l4_h"], t["l4_lede"])
                   + '<div class="card"><div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><span class="tog on"></span></div>'
                     '<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><span class="tog"></span></div></div>'
                     % (t["l4_r1t"], t["l4_r1s"], t["l4_r2t"], t["l4_r2s"])
                   + card(t["l4_c1h"], t["l4_c1p"], "split") + '<div class="grow"></div>' + btns(t["l4_btn"], t["l4_no"]))
def L5(t): return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["l5_h"], t["l5_lede"])
                   + card(t["l5_c1h"], t["l5_c1p"], "two") + '<div class="grow"></div>' + btns(t["l5_btn"], t["l5_no"]))
def L6(t):
    def sec(title, rows, action=None):
        r = "".join('<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div>%s</div>'
                    % (a, b, '<span class="s">%s</span>' % action if action else "") for a, b in rows)
        return '<div class="card"><h2>%s</h2>%s</div>' % (title, r)
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["l6_h"], t["l6_lede"])
            + sec(t["l6_pk"], [t["l6_pk1"], t["l6_pk2"]]) + sec(t["l6_st"], [t["l6_st1"]], t["l6_change"])
            + sec(t["l6_wk"], [t["l6_wk1"]]) + sec(t["l6_q"], [t["l6_q1"]]))
def S1(t):
    chips = "".join('<span class="chip%s">%s</span>' % (" on" if i == 1 else "", c) for i, c in enumerate(t["s1_r"]))
    return (frm(t, t["s_from"], "dp") + "<h1>%s</h1><p class='lede'>%s</p>" % (t["s1_h"], t["s1_lede"])
            + '<div class="card"><div class="thumb">%s<dl class="kv"><dt>%s</dt><dd class="mono">sunflower.png</dd>'
              '<dt>%s</dt><dd><b>%s</b></dd><dt>%s</dt><dd>%s</dd></dl></div><p class="fine">%s</p></div>'
              % (sunflower(), t["s1_kvf"], t["s1_kvm"], t["s1_kvmv"], t["s1_kvt"], t["s1_kvtv"], t["s1_hint"])
            + '<div class="card"><h2>%s</h2><div class="chips">%s</div></div>' % (t["s1_rh"], chips)
            + '<div class="note">%s</div>' % t["s1_note"]
            + '<div class="grow"></div>' + btns(t["s1_btn"], key=True) + '<p class="fine">%s</p>' % t["s1_fine"])
def S2(t):
    kv = "".join("<dt>%s</dt><dd%s>%s</dd>" % (a, ' class="mono"' if i == 4 else "", b) for i, (a, b) in enumerate(t["s2_kv"]))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["s2_h"], t["s2_lede"])
            + '<div class="card"><div class="thumb">%s<dl class="kv">%s</dl></div><p class="more">%s</p></div>' % (sunflower(64), kv, t["s2_more"])
            + card(t["s2_c1h"], t["s2_c1p"], "log") + '<div class="grow"></div>' + btns(t["s2_btn"], t["s2_no"]))
def S3(t): return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["s3_h"], t["s3_lede"])
                   + card(t["s3_c1h"], t["s3_c1p"], "log") + '<div class="grow"></div>' + btns(t["s3_btn"], t["s3_no"], key=True))
def S4(t): return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["s4_h"], t["s4_lede"])
                   + '<div class="card"><h2>%s</h2><div class="field">%s</div><h2 style="margin-top:14px">%s</h2><div class="field">%s</div></div>'
                     % (t["s4_dev"], t["s4_devv"], t["s4_after"], t["s4_afterv"])
                   + card(t["s4_c1h"], t["s4_c1p"], "log") + '<div class="grow"></div>' + btns(t["s4_btn"], key=True))
def S5(t): return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["s5_h"], t["s5_lede"])
                   + '<div class="card"><h2>%s</h2><div class="field mono">%s</div></div>' % (t["s5_field"], t["s5_fieldv"])
                   + card(t["s5_c1h"], t["s5_c1p"]) + '<div class="grow"></div>' + btns(t["s5_btn"]))
def S6(t): return ("<h1>%s</h1><p class='lede'>%s</p>" % (t["s6_h"], t["s6_lede"])
                   + card(t["s6_c1h"], t["s6_c1p"], "log")
                   + '<div class="card"><h2>%s</h2><div class="field area">%s</div></div>' % (t["s6_field"], t["s6_fieldv"])
                   + '<div class="grow"></div>' + btns(t["s6_btn"], key=True))

def S7(t):
    ok = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    has = "".join('<li>%s<span>%s</span></li>' % (ok, x) for x in t["s7_has_i"])
    nots = "".join('<li><i></i><span>%s</span></li>' % x for x in t["s7_not_i"])
    today = "".join('<div class="row"><div class="t">%s</div><span class="pill%s">%s</span></div>' % (a, " on" if i == 0 else "", b)
                    for i, (a, b) in enumerate(t["s7_today_i"]))
    return (S2(t) + '<div class="scrim"></div><div class="sheet"><div class="grab"></div>'
            + "<h1>%s</h1>" % t["s7_h"]
            + '<h2 class="sh">%s</h2><ul class="ticks">%s</ul>' % (t["s7_has"], has)
            + '<h2 class="sh">%s</h2><ul class="dots">%s</ul>' % (t["s7_not"], nots)
            + '<div class="card"><h2>%s</h2>%s<p class="fine">%s</p></div>' % (t["s7_today"], today, t["s7_fine"])
            + btns(t["s7_btn"]).replace('class="btn"', 'class="btn ghost"') + '</div>')

SCREENS = [  # (id, page, title, render)
    ("L1", "login", "Log in", L1), ("L2", "login", "Make a passkey", L2), ("L3", "login", "Under 18", L3),
    ("L4", "login", "What a site may know", L4), ("L5", "login", "Logged in: add a second passkey", L5),
    ("L6", "login", "Your account", L6),
    ("S1", "sign", "Sign a file", S1), ("S2", "sign", "Signed", S2), ("S7", "sign", "What this record shows (sheet)", S7), ("S3", "sign", "Withdraw a record", S3),
    ("S4", "sign", "A device lost or stolen", S4), ("S5", "sign", "Bring your works back", S5),
    ("S6", "sign", "Dispute a record", S6),
]


def page(sid, render, lang, dark=False):
    t = T[lang]
    body = render(t)
    assert not re.search(r"\bsign[\s-]?in\b", body, re.I), "%s: 'sign in' is barred (Default 10)" % sid
    assert "notar" not in body.lower(), "%s: 'notary' is barred in public copy" % sid
    themes = "".join('<span%s>%s</span>' % (' class="on"' if i == (2 if dark else 0) else "", x) for i, x in enumerate(t["theme"]))
    langs = "".join('<span%s>%s</span>' % (' class="on"' if (i == 0) == (lang == "en") else "", x) for i, x in enumerate(t["lang"]))
    return ("""<!doctype html>
<html lang="%s" class="%s%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=%d">
<meta name="googlebot" content="noindex,nofollow"><meta name="bingbot" content="noindex,nofollow">
<meta name="slurp" content="noindex,nofollow"><meta name="yandex" content="noindex,nofollow">
<title>B.333.eco · %s</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>[hidden]{display:none!important}</style>
<link rel="stylesheet" href="board.css?v=@CSSV@">
</head>
<body>
%s<div class="app">
<header>%s<span class="seg">%s</span></header>
%s
<footer><span>%s</span><span class="seg">%s</span></footer>
</div>
</body>
</html>
""" % ("km" if lang == "km" else "en", "km" if lang == "km" else "en", " dark" if dark else "", W, sid,
       '<div class="band">%s</div>' % t["band"] if t["band"] else "", mark(), langs, body, t["foot"], themes))


def main():
    css = brand_css(CSS)
    io.open(os.path.join(HERE, "board.css"), "w", encoding="utf-8").write(css)
    import hashlib
    cssv = hashlib.sha256(css.encode()).hexdigest()[:8]
    hpath = os.path.join(HERE, "heights.json")  # measured by measure.py; a frame is max(844, its content)
    hts = json.load(io.open(hpath)) if os.path.exists(hpath) else {}
    def hh(f): return max(H, int(hts.get(f, H)))
    tall_en = max([H] + [int(v) for k, v in hts.items() if not k.endswith("Km.html")])
    tall_km = max([H] + [int(v) for k, v in hts.items() if k.endswith("Km.html")])
    boards, col = [], {"login": 0, "sign": 0}
    pages = [{"id": "login", "name": "Log in with HeartBank®"}, {"id": "sign", "name": "Sign with HeartBank®"}]
    rowy = {"en": 0, "km": tall_en + 160}
    for sid, pg, title, render in SCREENS:
        for lang in ("en", "km"):
            f = "%s%s.html" % (sid, "" if lang == "en" else "Km")
            io.open(os.path.join(HERE, f), "w", encoding="utf-8").write(page(sid, render, lang).replace("@CSSV@", cssv))
            boards.append({"file": f, "page": pg, "title": "%s · %s, %s" % (sid, title, "English" if lang == "en" else "Khmer"),
                           "w": W, "h": hh(f), "x": col[pg] * (W + 80), "y": rowy[lang]})
        col[pg] += 1
    for sid, pg in (("L1", "login"), ("S1", "sign")):  # one dark pass per surface (Default 6)
        f = "%sDark.html" % sid
        render = dict((s[0], s[3]) for s in SCREENS)[sid]
        io.open(os.path.join(HERE, f), "w", encoding="utf-8").write(page(sid, render, "en", dark=True).replace("@CSSV@", cssv))
        boards.append({"file": f, "page": pg, "title": "%s · dark pass, English" % sid, "w": W, "h": hh(f),
                       "x": 0, "y": rowy["km"] + tall_km + 160})
    canvas = {"pages": pages, "artboards": boards, "annotations": [], "launch": {"page": "login", "view": "canvas"}}
    io.open(os.path.join(HERE, "canvas.json"), "w", encoding="utf-8").write(json.dumps(canvas, ensure_ascii=False, indent=1))
    print("%d artboards written · board.css v=%s" % (len(boards), cssv))


if __name__ == "__main__":
    main()
