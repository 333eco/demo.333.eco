"""Keep a copy: the opt-in at signing on origin.333.eco and its Your kept files page (storage.333.eco M4 = B-Origin M6; the spec
is private, sign.333.eco SPEC.md §10c-bis; founder 2026-11-16). Imported by build-boards.py, which injects the shared helpers.

Copy rules this file must keep (checked at build time by check()):
  - The choice starts UNTICKED and is never a nudge: no "you'll lose it", no "before it's too late", no "don't risk".
  - Where it is offered, it says once that the file leaves the device, that we can see it, and that nothing public says it was kept.
  - ⛔ Nothing counts down: no days left, no "expires", no reminder. A lapse is said once, with the window (at least 90 days).
  - ⛔ An empty page says what the page is for, never what is missing ("no files", "nothing yet", "haven't").
  - ⛔ No storage address is drawn, and no file name is kept: a kept file shows its kind, size, day and fingerprint.
  - Words copied from the live sign.333.eco page (sign-text.ts SIGN_TEXT, SOURCE_LABELS) stay word for word.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""
import re

# injected by build-boards.py
card = btns = spot = heart = person = sunflower = None

KEY = ('<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2.4"/>'
       '<path d="M12 12h9M18 12v4M21 12v3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>')
OK = ('<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="var(--accent)" '
      'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

DT = {
"en": {
  # copied from the live sign.333.eco page (sign-text.ts, 2026-11-16)
  "public": "This adds a public record: when it was signed and how it was made. It shows that a passkey signed it, not who imagined it.",
  "how": "How it was made", "howv": "Made by hand on a device", "rights": "Share it under", "rightsv": "All rights reserved",
  "privacy": "Your file stays on your device. Only its fingerprint is sent.",
  "saveproof": "Save your proof", "another": "Sign another file", "signed": "Signed",
  "signedl": "Your signature is saved. It joins the public log at the next hourly update, around 14:00.",
  # new words (origin.333.eco)
  "k1_h": "Sign a file", "file": "sunflower.png · 2.4 MB",
  "keep": "Keep a copy here",
  "keep_says": "Your file will leave this device and be kept by us, where we can see it. Nothing public says you kept it.",
  "keep_cost": "For this file: about $0.0002 a month, paid from your balance. Remove it any time.",
  "go": "Sign with your passkey", "go_fine": "The next page, on sign.333.eco, asks for your passkey.",
  "k2_h": "Keep a copy: its other three states",
  "k2_lede": "Where the choice would be, the page says plainly why it isn't there yet. Signing works the same in every case.",
  "k2_a": "Not logged in", "k2_ap": "Log in to keep a copy of what you sign.", "k2_ab": "Log in",
  "k2_b": "No balance connected", "k2_bp": "Keeping a copy needs a connected balance at billing.thonly.com.", "k2_bb": "Connect your balance",
  "k2_c": "A kind of file the store doesn't take", "k2_cp": "This kind of file can't be kept here. You can still sign it.",
  "kept": "A copy is kept", "kept_p": "In Your kept files. Download it or remove it there, any time.", "kept_b": "Your kept files",
  "k4_note": "The copy wasn't kept. Your signature is saved either way.", "k4_b": "Keep it now",
  "k4_fine": "The file is still on this device until you leave this page.",
  "k5_h": "Your kept files", "k5_lede": "Copies you chose to keep when you signed. Only you can open them.",
  "rows": (("pic", "Picture · 2.4 MB", "kept 16 Nov 2026 · a3f9 c2e1"), ("doc", "PDF · 840 KB", "kept 12 Nov 2026 · 07bd 5a90"),
           ("voice", "Voice · 3.1 MB", "kept 2 Nov 2026 · e44c 1b72")),
  "dl": "Download", "rm": "Remove",
  "paid_h": "Paid from your balance", "paid_p": "Keeping a copy costs $0.003 per GB a day, from your balance at billing.thonly.com.",
  "paid_b": "Your balance", "stay": "Your public records stay whatever you do here.",
  "k6_h": "Remove this copy?", "k6_p": "Your public record stays. Only the copy goes, from us and from our second copy.",
  "k6_keep": "Keep it", "k6_rm": "Remove the copy",
  "k7_note": "Your balance isn't covering these files. They're kept for at least 90 days after it stopped, and you can download them here the whole time.",
  "k8_lede": "When you sign a file, you can choose to keep a copy here. Kept files are listed on this page, to download or remove at any time.",
  "k8_b": "Sign a file",
},
"km": {
  "public": "ការនេះបន្ថែមកំណត់ត្រាសាធារណៈមួយ៖ ពេលដែលវាត្រូវបានចុះហត្ថលេខា និងរបៀបដែលវាត្រូវបានបង្កើត។ វាបង្ហាញថា passkey មួយបានចុះហត្ថលេខា មិនមែនថាអ្នកណាជាអ្នកគិតវាទេ។",
  "how": "របៀបដែលវាត្រូវបានបង្កើត", "howv": "បង្កើតដោយដៃនៅលើឧបករណ៍", "rights": "ចែករំលែកក្រោម", "rightsv": "រក្សាសិទ្ធិគ្រប់យ៉ាង",
  "privacy": "ឯកសាររបស់អ្នកនៅលើឧបករណ៍របស់អ្នក។ មានតែស្នាមម្រាមដៃរបស់វាទេដែលត្រូវបានផ្ញើ។",
  "saveproof": "រក្សាទុកភស្តុតាងរបស់អ្នក", "another": "ចុះហត្ថលេខាលើឯកសារមួយទៀត", "signed": "បានចុះហត្ថលេខា",
  "signedl": "ហត្ថលេខារបស់អ្នកត្រូវបានរក្សាទុក។ វានឹងចូលទៅក្នុងកំណត់ហេតុសាធារណៈនៅការធ្វើបច្ចុប្បន្នភាពរៀងរាល់ម៉ោងបន្ទាប់ ប្រហែល 14:00។",
  "k1_h": "ចុះហត្ថលេខាលើឯកសារ", "file": "sunflower.png · 2.4 MB",
  "keep": "រក្សាច្បាប់ចម្លងនៅទីនេះ",
  "keep_says": "ឯកសាររបស់អ្នកនឹងចេញពីឧបករណ៍នេះ ហើយយើងរក្សាទុកវា ដែលយើងអាចមើលឃើញវា។ គ្មានអ្វីជាសាធារណៈនិយាយថាអ្នកបានរក្សាវាទុកទេ។",
  "keep_cost": "សម្រាប់ឯកសារនេះ៖ ប្រហែល $0.0002 ក្នុងមួយខែ បង់ពីសមតុល្យរបស់អ្នក។ ដកចេញបាននៅពេលណាក៏បាន។",
  "go": "ចុះហត្ថលេខាដោយ passkey របស់អ្នក", "go_fine": "ទំព័របន្ទាប់ នៅលើ sign.333.eco នឹងសុំ passkey របស់អ្នក។",
  "k2_h": "រក្សាច្បាប់ចម្លង៖ ស្ថានភាពបីផ្សេងទៀត",
  "k2_lede": "នៅកន្លែងដែលជម្រើសនេះគួរនៅ ទំព័រនិយាយយ៉ាងច្បាស់ថាហេតុអ្វីវាមិនទាន់មាន។ ការចុះហត្ថលេខាដំណើរការដូចគ្នាក្នុងគ្រប់ករណី។",
  "k2_a": "មិនទាន់ចូល", "k2_ap": "ចូល ដើម្បីរក្សាច្បាប់ចម្លងនៃអ្វីដែលអ្នកចុះហត្ថលេខា។", "k2_ab": "ចូល",
  "k2_b": "មិនទាន់ភ្ជាប់សមតុល្យ", "k2_bp": "ការរក្សាច្បាប់ចម្លង ត្រូវការសមតុល្យដែលបានភ្ជាប់នៅ billing.thonly.com។", "k2_bb": "ភ្ជាប់សមតុល្យរបស់អ្នក",
  "k2_c": "ប្រភេទឯកសារដែលមិនអាចរក្សាទុកនៅទីនេះ", "k2_cp": "ឯកសារប្រភេទនេះមិនអាចរក្សាទុកនៅទីនេះបានទេ។ អ្នកនៅតែអាចចុះហត្ថលេខាលើវាបាន។",
  "kept": "ច្បាប់ចម្លងមួយត្រូវបានរក្សាទុក", "kept_p": "នៅក្នុង ឯកសារដែលអ្នករក្សាទុក។ ទាញយក ឬដកវាចេញនៅទីនោះ នៅពេលណាក៏បាន។", "kept_b": "ឯកសារដែលអ្នករក្សាទុក",
  "k4_note": "ច្បាប់ចម្លងមិនត្រូវបានរក្សាទុកទេ។ ហត្ថលេខារបស់អ្នកត្រូវបានរក្សាទុករួចហើយ។", "k4_b": "រក្សាទុកឥឡូវនេះ",
  "k4_fine": "ឯកសារនៅតែនៅលើឧបករណ៍នេះ រហូតដល់អ្នកចាកចេញពីទំព័រនេះ។",
  "k5_h": "ឯកសារដែលអ្នករក្សាទុក", "k5_lede": "ច្បាប់ចម្លងដែលអ្នកបានជ្រើសរើសរក្សាទុក ពេលអ្នកចុះហត្ថលេខា។ មានតែអ្នកទេដែលអាចបើកវាបាន។",
  "rows": (("pic", "រូបភាព · 2.4 MB", "រក្សាទុក ១៦ វិច្ឆិកា ២០២៦ · a3f9 c2e1"), ("doc", "PDF · 840 KB", "រក្សាទុក ១២ វិច្ឆិកា ២០២៦ · 07bd 5a90"),
           ("voice", "សំឡេង · 3.1 MB", "រក្សាទុក ២ វិច្ឆិកា ២០២៦ · e44c 1b72")),
  "dl": "ទាញយក", "rm": "ដកចេញ",
  "paid_h": "បង់ពីសមតុល្យរបស់អ្នក", "paid_p": "ការរក្សាច្បាប់ចម្លងមានតម្លៃ $0.003 ក្នុងមួយ GB ក្នុងមួយថ្ងៃ ពីសមតុល្យរបស់អ្នកនៅ billing.thonly.com។",
  "paid_b": "សមតុល្យរបស់អ្នក", "stay": "កំណត់ត្រាសាធារណៈរបស់អ្នកនៅដដែល ទោះអ្នកធ្វើអ្វីនៅទីនេះក៏ដោយ។",
  "k6_h": "ដកច្បាប់ចម្លងនេះចេញ?", "k6_p": "កំណត់ត្រាសាធារណៈរបស់អ្នកនៅដដែល។ មានតែច្បាប់ចម្លងទេដែលត្រូវដកចេញ ពីយើង និងពីច្បាប់ចម្លងទីពីររបស់យើង។",
  "k6_keep": "ទុកវា", "k6_rm": "ដកច្បាប់ចម្លងចេញ",
  "k7_note": "សមតុល្យរបស់អ្នកមិនបានបង់សម្រាប់ឯកសារទាំងនេះទេ។ វាត្រូវបានរក្សាទុកយ៉ាងហោចណាស់ ៩០ ថ្ងៃ បន្ទាប់ពីវាឈប់ ហើយអ្នកអាចទាញយកវានៅទីនេះបានគ្រប់ពេល។",
  "k8_lede": "ពេលអ្នកចុះហត្ថលេខាលើឯកសារ អ្នកអាចជ្រើសរើសរក្សាច្បាប់ចម្លងនៅទីនេះ។ ឯកសារដែលបានរក្សាទុកត្រូវបានរាយនៅលើទំព័រនេះ ដើម្បីទាញយក ឬដកចេញនៅពេលណាក៏បាន។",
  "k8_b": "ចុះហត្ថលេខាលើឯកសារ",
},
}


def kspot(kind):
    """Small flat drawings from the board's own tokens."""
    s = ['<svg class="kicon" width="44" height="44" viewBox="0 0 44 44" aria-hidden="true">']
    if kind == "doc":
        s += ['<rect x="10" y="5" width="24" height="34" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M15 15h14M15 21h14M15 27h9" stroke="var(--ink-faint)" stroke-width="2" stroke-linecap="round"/>']
    elif kind == "voice":
        s += ['<rect x="3" y="3" width="38" height="38" rx="8" fill="var(--wash)"/>']
        s += ['<rect x="%d" y="%d" width="3" height="%d" rx="1.5" fill="var(--accent)"/>' % (9 + i * 5, 22 - h // 2, h)
              for i, h in enumerate((8, 16, 24, 14, 20, 10))]
    s.append('</svg>')
    return "".join(s)


def _select(label, value):
    return ('<div class="kf"><div class="kl">%s</div><div class="ksel"><span>%s</span>'
            '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>'
            '</div></div>' % (label, value))


def _file(d):
    return '<div class="card"><div class="thumb">%s<div class="mono">%s</div></div></div>' % (sunflower(48), d["file"])


def _keepbox(d, ticked=False):
    box = '<span class="kbox%s">%s</span>' % (" on" if ticked else "", OK if ticked else "")
    return ('<div class="card kkeep"><label class="krow">%s<b>%s</b></label><p>%s</p><p class="fine">%s</p></div>'
            % (box, d["keep"], d["keep_says"], d["keep_cost"]))


def K1(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["k1_h"], d["public"]) + _file(d)
            + '<div class="card">%s%s</div>' % (_select(d["how"], d["howv"]), _select(d["rights"], d["rightsv"]))
            + _keepbox(d) + '<p class="fine">%s</p>' % d["privacy"]
            + '<div class="grow"></div>' + '<button class="btn">%s%s</button>' % (KEY, d["go"]) + '<p class="fine">%s</p>' % d["go_fine"])


def K2(t, d):
    def state(cap, p, b=None):
        return ('<div class="kcap">%s</div><div class="card kkeep"><b>%s</b><p>%s</p>%s</div>'
                % (cap, d["keep"], p, '<button class="btn ghost">%s</button>' % b if b else ""))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["k2_h"], d["k2_lede"])
            + state(d["k2_a"], d["k2_ap"], d["k2_ab"]) + state(d["k2_b"], d["k2_bp"], d["k2_bb"]) + state(d["k2_c"], d["k2_cp"]))


def K3(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["signed"], d["signedl"])
            + '<div class="card"><div class="krow">%s<b>%s</b></div><p>%s</p></div>' % (OK, d["kept"], d["kept_p"])
            + '<div class="grow"></div>' + btns(d["kept_b"], d["saveproof"]) + '<p class="fine" style="text-align:center">%s</p>' % d["another"])


def K4(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["signed"], d["signedl"]) + '<div class="note">%s</div>' % d["k4_note"]
            + btns(d["k4_b"]) + '<p class="fine">%s</p>' % d["k4_fine"]
            + '<div class="grow"></div>' + btns(d["saveproof"], d["another"]))


def _rows(d):
    out = []
    for kind, a, b in d["rows"]:
        art = ('<div class="kthumb">%s</div>' % sunflower(44)) if kind == "pic" else kspot(kind)
        out.append('<div class="row krowf">%s<div class="kmeta"><div class="t">%s</div><div class="s mono">%s</div></div>'
                   '<div class="kact"><span class="pillbtn">%s</span><span class="pillbtn ghost">%s</span></div></div>' % (art, a, b, d["dl"], d["rm"]))
    return '<div class="card">%s</div>' % "".join(out)


def _paid(d):
    return ('<div class="card"><h2>%s</h2><p>%s</p><span class="pillbtn">%s</span></div>' % (d["paid_h"], d["paid_p"], d["paid_b"])
            + '<p class="fine">%s</p>' % d["stay"])


def K5(t, d):
    return "<h1>%s</h1><p class='lede'>%s</p>" % (d["k5_h"], d["k5_lede"]) + _rows(d) + _paid(d)


def K6(t, d):
    return ('<div class="kdim">' + K5(t, d) + '</div>'
            + '<div class="kdlg"><h2>%s</h2><p>%s</p><div class="kdbtn"><button class="btn ghost">%s</button><button class="btn">%s</button></div></div>'
            % (d["k6_h"], d["k6_p"], d["k6_keep"], d["k6_rm"]))


def K7(t, d):
    return ("<h1>%s</h1>" % d["k5_h"] + '<div class="note">%s</div>' % d["k7_note"] + btns(d["paid_b"])
            + '<div style="height:14px"></div>' + _rows(d) + '<p class="fine">%s</p>' % d["stay"])


def K8(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["k5_h"], d["k8_lede"]) + '<div class="grow"></div>' + btns(d["k8_b"])
            + '<p class="fine">%s</p>' % d["stay"])


SCREENS = [  # (id, page, title, render(t, d))
    ("K1", "origin", "Sign a file, with Keep a copy (unticked)", K1),
    ("K2", "origin", "Keep a copy: logged out · no balance · a kind of file not taken", K2),
    ("K3", "origin", "Signed, and a copy is kept", K3),
    ("K4", "origin", "Signed, but the copy wasn't kept", K4),
    ("K5", "origin", "Your kept files", K5),
    ("K6", "origin", "Remove a copy", K6),
    ("K7", "origin", "Your kept files when the balance stopped covering them", K7),
    ("K8", "origin", "Your kept files, before any is kept", K8),
]
PUBLIC = set()  # a person's own pages: no share button (Default 8)
CSS = """
.kf{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:8px 0}
.kf+.kf{border-top:1px solid var(--line)}
.kl{font-size:14px;color:var(--ink-dim)}
.ksel{display:inline-flex;gap:8px;align-items:center;font-size:14px;padding:7px 12px;border-radius:10px;border:1px solid var(--line-strong);background:var(--surface)}
.kkeep b{font-size:16px}
.krow{display:flex;gap:10px;align-items:center;margin:0 0 6px}
.kbox{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:6px;border:2px solid var(--line-strong);background:var(--surface);flex:none}
.kbox.on{border-color:var(--accent)}
.kcap{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint);margin:14px 0 6px}
.krowf{align-items:center;gap:12px}
.kthumb,.kicon{flex:none;width:44px;height:44px;border-radius:8px;overflow:hidden}
.kmeta{flex:1;min-width:0}
.kact{display:flex;flex-direction:column;gap:6px}
.pillbtn{display:inline-block;font-size:13px;font-weight:600;padding:6px 14px;border-radius:var(--r-pill);border:1px solid var(--accent);color:var(--ink);background:var(--wash);text-align:center}
.pillbtn.ghost{background:transparent;border-color:var(--line-strong)}
.kdim{opacity:.35;pointer-events:none}
.kdlg{position:absolute;left:20px;right:20px;top:260px;background:var(--surface);border:1px solid var(--line-strong);border-radius:var(--r);padding:20px;box-shadow:0 12px 40px rgba(0,0,0,.18)}
.kdbtn{display:flex;gap:10px;margin-top:14px}
.kdbtn .btn{flex:1;margin:0}
"""
BARRED = [  # words this surface must never draw
    (r"\blose\b|\blost\b|too late|don.t risk|\bbefore it\b|\bonly \d+", "no nudge, no fear: the choice is offered, never pressed (§keep-a-copy-m4)"),
    (r"\bexpire[sd]?\b|\btime left\b|\bremaining\b|\bcountdown\b|\bdays? left\b|\bremind", "nothing counts down (Sig-8)"),
    (r"storage\.333\.eco/", "a storage address is never shown (§one-store item 7)"),
    (r"\bsign[\s-]?in\b", "Log in authenticates; 'sign in' is barred (Default 10)"),
]


def check(sid, body):
    for pat, why in BARRED:
        assert not re.search(pat, body, re.I), "%s: %s" % (sid, why)
    if sid == "K1":
        assert 'class="kbox"' in body, "K1: the choice starts UNTICKED"
        for need in (("leave this device", "where we can see it", "Nothing public says") if "ឯកសារ" not in body else ()):
            assert need in body, "K1: the disclosure must say '%s'" % need
    if sid == "K8":
        assert not re.search(r"\bno files\b|nothing yet|haven.t|\byet\b|មិនទាន់", body, re.I), "K8: an empty page says what it is for, never what is missing"
    if sid == "K7":
        assert re.search(r"at least 90 days|យ៉ាងហោចណាស់ ៩០ ថ្ងៃ", body), "K7: the lapse is said once, with its window"
