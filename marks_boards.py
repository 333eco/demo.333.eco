"""Marks that point, on origin.333.eco (A701; the spec is private, sign.333.eco SPEC.md §10f; founder 2026-11-23: "1: yes; also, align the strip
to the right side instead / 2: yes / …"). Imported by build-boards.py, which injects the shared helpers.

Copy rules this file must keep (checked at build time by check()):
  - ⛔ A mark is an ADDRESS, never a claim: no "verified", "authentic", "real", "proof of"; the code's words are its address.
  - Both choices start UNTICKED; where they are offered, the page says once what they change and what becomes public.
  - ⛔ "a likely match" or "looks like", never "passed" or "matches" for a resized or edited copy.
  - A page a code opens never asks for a password, a code or a payment, and says so once.
  - Words copied from the live origin.333.eco sign page (client/keep.ts) stay word for word.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""
import io, os, re

card = btns = spot = heart = person = sunflower = None   # injected by build-boards.py
HERE = os.path.dirname(os.path.abspath(__file__))
BQR = io.open(os.path.join(HERE, "marks-bqr.svg"), encoding="utf-8").read().replace(' shape-rendering="crispEdges"', "")
from kept_boards import KEY, OK

DT = {
"en": {
  # copied from the live sign page (client/keep.ts, 2026-11-23)
  "h": "Sign a file", "public": "This adds a public record: when it was signed and how it was made. It shows that a passkey signed it, not who imagined it.",
  "how": "How it was made", "howv": "Photo or recording", "rights": "Share it under", "rightsv": "All rights reserved",
  "go": "Sign with your passkey", "go_fine": "The next page, on sign.333.eco, asks for your passkey.",
  "signed": "Signed", "signedl": "Your signature is saved. It joins the public log within the hour.", "records": "Your records", "another": "Sign another file",
  # new words
  "file": "sunflower.jpg · 3024 × 4032",
  "m_h": "Add a mark to the picture", "m_p": "A mark leads people from the picture to its page. It is yours to choose.",
  "inv": "A mark you can't see", "inv_p": "It changes the colors very slightly, and usually still works after the picture is resized, posted or captured in a screenshot.",
  "code": "A code people can scan", "code_p": "A heart in a corner, or a strip under the picture with the address in words.",
  "nm": "Show my @name on its page", "nm_p": "@thon, from your name at 333.eco. It says you made this page.",
  "pub": "The page is public: it shows this picture, the day it was signed and how it was made. The signed picture is sent to us once, to make the small copy that page shows. Only the small copy is kept.",
  "copy": "Anyone can copy a mark onto another picture, so the page shows yours to compare.",
  "m2_h": "Where the code goes", "corner": "Corner", "strip": "Strip", "which": "Which corner", "corners": ("Top left", "Top right", "Bottom left", "Bottom right"), "side": "Which side", "sides": ("Left", "Right"),
  "addr": "B.333.eco/7K2M-9QX4-B8T3", "scan": "Scan to open in B-Origin℠", "prev": "This is the picture you will sign, with its mark.", "back": "Back", "use": "Use this picture",
  "m3_p": "Share the marked picture below. It is the exact file you signed.", "save": "Save the marked picture", "page": "Its page", "end": "End the mark", "m3_fine": "If you end it, the code stops leading here. Your record stays.",
  "m4_h": "A signed picture", "day": "Signed", "dayv": "23 Nov 2026", "by": "Page made by", "byv": "@thon", "rec": "Public record", "recv": "No. 24",
  "saysh": "The signer says", "cmp_h": "Is yours the same?", "cmp_p": "Compare it with the picture above. If anything is different, yours isn't the one that was signed: an edited copy keeps its mark.",
  "chk": "Check my file", "never": "This page never asks for a password, a code or a payment.", "own": "Sign your own pictures at origin.333.eco",
  "m5_h": "Your file and this page", "a": "The exact file", "ap": "Every byte is the same as the file that was signed.",
  "b": "A likely match", "bp": "It looks like the picture on this page, but it isn't the exact file. It may have been resized, or changed. Compare the two.",
  "c": "A different picture", "cp": "It doesn't look like the picture on this page.", "here": "Read on this device. Your file stays here.",
  "m6_h": "Check a file", "m6_f": "IMG_2041.jpg", "found": "A mark that leads to a page", "found_p": "B.333.eco/7K2M-9QX4-B8T3", "open": "Open its page",
  "like": "A likely match: it looks like the picture on that page. Compare them before you rely on it.",
  "diff": "It leads to a different picture. Someone may have copied the mark.", "m6_cap1": "When it looks like the page's picture", "m6_cap2": "When it doesn't",
},
"km": {
  "h": "ចុះហត្ថលេខាលើឯកសារ", "public": "ការនេះបន្ថែមកំណត់ត្រាសាធារណៈមួយ៖ ពេលដែលវាត្រូវបានចុះហត្ថលេខា និងរបៀបដែលវាត្រូវបានបង្កើត។ វាបង្ហាញថា passkey មួយបានចុះហត្ថលេខា មិនមែនថាអ្នកណាជាអ្នកគិតវាទេ។",
  "how": "របៀបដែលវាត្រូវបានបង្កើត", "howv": "រូបថត ឬការថត", "rights": "ចែករំលែកក្រោម", "rightsv": "រក្សាសិទ្ធិគ្រប់យ៉ាង",
  "go": "ចុះហត្ថលេខាដោយ passkey របស់អ្នក", "go_fine": "ទំព័របន្ទាប់ នៅលើ sign.333.eco នឹងសុំ passkey របស់អ្នក។",
  "signed": "បានចុះហត្ថលេខា", "signedl": "ហត្ថលេខារបស់អ្នកត្រូវបានរក្សាទុក។ វានឹងចូលទៅក្នុងកំណត់ហេតុសាធារណៈក្នុងរយៈពេលមួយម៉ោង។", "records": "កំណត់ត្រារបស់អ្នក", "another": "ចុះហត្ថលេខាលើឯកសារមួយទៀត",
  "file": "sunflower.jpg · 3024 × 4032",
  "m_h": "បន្ថែមសញ្ញាមួយលើរូបភាព", "m_p": "សញ្ញានាំមនុស្សពីរូបភាព ទៅកាន់ទំព័ររបស់វា។ អ្នកជាអ្នកជ្រើសរើស។",
  "inv": "សញ្ញាដែលមើលមិនឃើញ", "inv_p": "វាប្តូរពណ៌បន្តិចបន្តួចប៉ុណ្ណោះ ហើយជាធម្មតានៅតែដំណើរការ ក្រោយពេលរូបភាពត្រូវបានប្តូរទំហំ បង្ហោះ ឬថតរូបអេក្រង់។",
  "code": "កូដដែលមនុស្សអាចស្កេន", "code_p": "បេះដូងមួយនៅជ្រុង ឬបន្ទះមួយនៅក្រោមរូបភាព ដែលមានអាសយដ្ឋានជាអក្សរ។",
  "nm": "បង្ហាញ @name របស់ខ្ញុំនៅលើទំព័ររបស់វា", "nm_p": "@thon ពីឈ្មោះរបស់អ្នកនៅ 333.eco។ វាប្រាប់ថាអ្នកបានបង្កើតទំព័រនេះ។",
  "pub": "ទំព័រនេះជាសាធារណៈ៖ វាបង្ហាញរូបភាពនេះ ថ្ងៃដែលវាត្រូវបានចុះហត្ថលេខា និងរបៀបដែលវាត្រូវបានបង្កើត។ រូបភាពដែលបានចុះហត្ថលេខាត្រូវបានផ្ញើមកយើងម្តង ដើម្បីបង្កើតច្បាប់ចម្លងតូចដែលទំព័រនោះបង្ហាញ។ មានតែច្បាប់ចម្លងតូចទេដែលត្រូវបានរក្សាទុក។",
  "copy": "អ្នកណាក៏អាចចម្លងសញ្ញាទៅដាក់លើរូបភាពផ្សេងបាន ដូច្នេះទំព័រនេះបង្ហាញរូបភាពរបស់អ្នក ដើម្បីប្រៀបធៀប។",
  "m2_h": "កន្លែងដាក់កូដ", "corner": "ជ្រុង", "strip": "បន្ទះ", "which": "ជ្រុងណា", "corners": ("លើឆ្វេង", "លើស្តាំ", "ក្រោមឆ្វេង", "ក្រោមស្តាំ"), "side": "ខាងណា", "sides": ("ឆ្វេង", "ស្តាំ"),
  "addr": "B.333.eco/7K2M-9QX4-B8T3", "scan": "ស្កេនដើម្បីបើកក្នុង B-Origin℠", "prev": "នេះជារូបភាពដែលអ្នកនឹងចុះហត្ថលេខា ជាមួយសញ្ញារបស់វា។", "back": "ត្រឡប់ក្រោយ", "use": "ប្រើរូបភាពនេះ",
  "m3_p": "ចែករំលែករូបភាពដែលមានសញ្ញាខាងក្រោម។ វាជាឯកសារដដែលដែលអ្នកបានចុះហត្ថលេខា។", "save": "រក្សាទុករូបភាពដែលមានសញ្ញា", "page": "ទំព័ររបស់វា", "end": "បញ្ចប់សញ្ញា", "m3_fine": "បើអ្នកបញ្ចប់វា កូដលែងនាំមកទីនេះ។ កំណត់ត្រារបស់អ្នកនៅដដែល។",
  "m4_h": "រូបភាពដែលបានចុះហត្ថលេខា", "day": "ចុះហត្ថលេខា", "dayv": "២៣ វិច្ឆិកា ២០២៦", "by": "ទំព័របង្កើតដោយ", "byv": "@thon", "rec": "កំណត់ត្រាសាធារណៈ", "recv": "លេខ ២៤",
  "saysh": "អ្នកចុះហត្ថលេខានិយាយថា", "cmp_h": "របស់អ្នកដូចគ្នាទេ?", "cmp_p": "ប្រៀបធៀបវាជាមួយរូបភាពខាងលើ។ បើមានអ្វីខុសគ្នា របស់អ្នកមិនមែនជារូបភាពដែលបានចុះហត្ថលេខាទេ៖ ច្បាប់ដែលបានកែ នៅតែមានសញ្ញារបស់វា។",
  "chk": "ពិនិត្យឯកសាររបស់ខ្ញុំ", "never": "ទំព័រនេះមិនដែលសុំពាក្យសម្ងាត់ លេខកូដ ឬការបង់ប្រាក់ទេ។", "own": "ចុះហត្ថលេខាលើរូបភាពរបស់អ្នកនៅ origin.333.eco",
  "m5_h": "ឯកសាររបស់អ្នក និងទំព័រនេះ", "a": "ឯកសារដដែល", "ap": "គ្រប់បៃដូចគ្នានឹងឯកសារដែលបានចុះហត្ថលេខា។",
  "b": "ប្រហែលជាដូចគ្នា", "bp": "វាមើលទៅដូចរូបភាពនៅលើទំព័រនេះ ប៉ុន្តែមិនមែនជាឯកសារដដែលទេ។ វាអាចត្រូវបានប្តូរទំហំ ឬកែប្រែ។ សូមប្រៀបធៀបទាំងពីរ។",
  "c": "រូបភាពផ្សេង", "cp": "វាមើលទៅមិនដូចរូបភាពនៅលើទំព័រនេះទេ។", "here": "អាននៅលើឧបករណ៍នេះ។ ឯកសាររបស់អ្នកនៅទីនេះ។",
  "m6_h": "ពិនិត្យឯកសារ", "m6_f": "IMG_2041.jpg", "found": "សញ្ញាដែលនាំទៅកាន់ទំព័រមួយ", "found_p": "B.333.eco/7K2M-9QX4-B8T3", "open": "បើកទំព័ររបស់វា",
  "like": "ប្រហែលជាដូចគ្នា៖ វាមើលទៅដូចរូបភាពនៅលើទំព័រនោះ។ សូមប្រៀបធៀប មុនពេលពឹងផ្អែកលើវា។",
  "diff": "វានាំទៅរូបភាពផ្សេង។ អ្នកណាម្នាក់ប្រហែលជាបានចម្លងសញ្ញានេះ។", "m6_cap1": "ពេលវាមើលទៅដូចរូបភាពនៅលើទំព័រ", "m6_cap2": "ពេលវាមិនដូច",
},
}


def _scene(w=320, h=240, uid="s"):
    """A drawn picture (a sunflower field at evening), so a mark is judged on a picture and not on paper."""
    return ('<svg class="mscene" viewBox="0 0 320 240" width="%d" height="%d" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            '<rect width="320" height="240" fill="#f3c98b"/><rect y="96" width="320" height="34" fill="#e2a15c"/><circle cx="232" cy="92" r="30" fill="#fbe3ad"/>'
            '<path d="M0 128h320v112H0z" fill="#4f7a3a"/><path d="M0 150c60-14 120 10 180-2s90-10 140 2v90H0z" fill="#3e642e"/>%s</svg>'
            % (w, h, "".join('<g transform="translate(%d %d) scale(%s)"><path d="M0 0v46" stroke="#274a1c" stroke-width="5"/><circle r="17" fill="#f2b21b"/><circle r="8" fill="#5b3414"/></g>' % (x, y, s)
                             for x, y, s in ((54, 142, 1.1), (118, 160, .8), (186, 148, 1), (262, 168, 1.2), (30, 200, .7), (222, 206, .7)))))


def _bqr(px, op=.7):
    s = re.sub(r'width="200" height="200"', 'width="%d" height="%d"' % (px, px), BQR, count=1)
    return s.replace('fill="#ffffff"', 'fill="#ffffff" fill-opacity="%s"' % op, 1).replace('fill="#fff"', 'fill="#fff" fill-opacity="%s"' % op, 1)


def _select(label, value):
    return ('<div class="kf"><div class="kl">%s</div><div class="ksel"><span>%s</span>'
            '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>'
            '</div></div>' % (label, value))


def _opt(h, p, on=False):
    return '<label class="krow mopt"><span class="kbox%s">%s</span><span><b>%s</b><span class="mop">%s</span></span></label>' % (" on" if on else "", OK if on else "", h, p)


def M1(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["h"], d["public"]) + '<div class="card"><div class="thumb">%s<div class="mono">%s</div></div></div>' % (_scene(96, 72), d["file"])
            + '<div class="card">%s%s</div>' % (_select(d["how"], d["howv"]), _select(d["rights"], d["rightsv"]))
            + '<div class="card kkeep"><b>%s</b><p>%s</p>%s%s%s<p class="fine mfine">%s</p><p class="fine">%s</p></div>'
            % (d["m_h"], d["m_p"], _opt(d["inv"], d["inv_p"]), _opt(d["code"], d["code_p"]), _opt(d["nm"], d["nm_p"]), d["pub"], d["copy"])
            + '<div class="grow"></div><button class="btn">%s%s</button><p class="fine">%s</p>' % (KEY, d["go"], d["go_fine"]))


def M2(t, d):
    seg = '<div class="mseg"><span class="on">%s</span><span>%s</span></div>' % (d["corner"], d["strip"])
    cs = '<div class="mcorners">%s</div>' % "".join('<span class="pillbtn%s">%s</span>' % ("" if i == 3 else " ghost", c) for i, c in enumerate(d["corners"]))
    corner = '<div class="mpic">%s<span class="mbr">%s</span></div>' % (_scene(), _bqr(78))
    strip = ('<div class="mpic"><div>%s</div><div class="mstrip"><span class="mwords"><b>%s</b><i>%s</i></span>%s</div></div>' % (_scene(), d["addr"], d["scan"], _bqr(62, 1)))
    return ("<h1>%s</h1>" % d["m2_h"] + seg + '<div class="kcap">%s</div>' % d["which"] + cs + corner + '<div class="kcap">%s · %s</div><div class="mcorners">%s</div>' % (d["strip"], d["side"], "".join('<span class="pillbtn%s">%s</span>' % ("" if i == 1 else " ghost", c) for i, c in enumerate(d["sides"]))) + strip
            + '<p class="fine">%s</p>' % d["prev"] + '<div class="kdbtn"><button class="btn ghost">%s</button><button class="btn">%s</button></div>' % (d["back"], d["use"]))


def M3(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["signed"], d["signedl"]) + '<div class="mpic">%s<span class="mbr">%s</span></div>' % (_scene(), _bqr(78))
            + "<p>%s</p>" % d["m3_p"] + '<button class="btn msave">%s</button>' % d["save"]
            + '<div class="card"><div class="row krowf"><div class="kmeta"><div class="t">%s</div><div class="s mono">%s</div></div><div class="kact"><span class="pillbtn ghost">%s</span></div></div><p class="fine">%s</p></div>'
            % (d["page"], d["addr"], d["end"], d["m3_fine"]) + '<div class="grow"></div>' + btns(d["records"], d["another"]))


def M4(t, d):
    rows = "".join('<div class="kf"><div class="kl">%s</div><div>%s</div></div>' % r for r in ((d["day"], d["dayv"]), (d["saysh"], d["howv"]), (d["by"], '<span class="link">%s</span>' % d["byv"]), (d["rec"], '<span class="link">%s</span>' % d["recv"])))
    return ("<h1>%s</h1>" % d["m4_h"] + '<div class="mpic">%s<span class="mbr">%s</span></div>' % (_scene(350, 262), _bqr(78)) + '<div class="card">%s</div>' % rows
            + '<div class="card"><h2>%s</h2><p>%s</p><span class="pillbtn">%s</span></div>' % (d["cmp_h"], d["cmp_p"], d["chk"])
            + '<div class="grow"></div><p class="fine">%s</p><p class="fine"><span class="link">%s</span></p>' % (d["never"], d["own"]))


def M5(t, d):
    def st(h, p, k):
        return '<div class="card"><div class="krow">%s<b>%s</b></div><p>%s</p></div>' % (k, h, p)
    dot = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="7" fill="none" stroke="var(--ink-dim)" stroke-width="2.4"/></svg>'
    return ("<h1>%s</h1>" % d["m5_h"] + '<div class="mpair"><div class="mpic">%s</div><div class="mpic">%s</div></div>' % (_scene(168, 126), _scene(168, 126))
            + st(d["a"], d["ap"], OK) + st(d["b"], d["bp"], dot) + st(d["c"], d["cp"], dot) + '<p class="fine">%s</p>' % d["here"])


def M6(t, d):
    def res(p):
        return ('<div class="card"><h2>%s</h2><div class="mono">%s</div><p>%s</p><span class="pillbtn">%s</span></div>' % (d["found"], d["found_p"], p, d["open"]))
    return ("<h1>%s</h1>" % d["m6_h"] + '<div class="card"><div class="thumb">%s<div class="mono">%s</div></div></div>' % (_scene(96, 72), d["m6_f"])
            + '<div class="kcap">%s</div>' % d["m6_cap1"] + res(d["like"]) + '<div class="kcap">%s</div>' % d["m6_cap2"] + res(d["diff"]) + '<p class="fine">%s</p>' % d["here"])


SCREENS = [
    ("M1", "origin", "Sign a file, with a mark (both choices unticked)", M1),
    ("M2", "origin", "Where the code goes: a corner or a strip", M2),
    ("M3", "origin", "Signed, with the marked picture to save", M3),
    ("M4", "origin", "The mark's page (anyone with the code)", M4),
    ("M5", "origin", "The mark's page: your file against it", M5),
    ("M6", "origin", "Check a file, when it carries a mark", M6),
]
PUBLIC = {"M4", "M5"}  # a public page: the share button (Default 8)
CSS = """
.mscene{display:block;border-radius:10px;max-width:100%}
.mopt{align-items:flex-start;margin:12px 0 0}
.mopt b{display:block;font-size:15px}
.mop{display:block;font-size:14px;color:var(--ink-dim);margin-top:2px}
.mpic{position:relative;border-radius:12px;overflow:hidden;background:var(--surface-2,var(--surface));margin:10px 0}
.mpic .mscene{width:100%;height:auto;border-radius:0}
.mbr{position:absolute;right:10px;bottom:8px;line-height:0}
.mstrip{display:flex;justify-content:flex-end;align-items:center;gap:12px;padding:8px 12px;background:linear-gradient(180deg,#3e642e,#33552a)}
.mwords{display:flex;flex-direction:column;align-items:flex-end;color:#fff}
.mwords b{font-size:13px;letter-spacing:.02em}
.mwords i{font-style:normal;font-size:11.5px;opacity:.92}
.mseg{display:flex;border:1px solid var(--line-strong);border-radius:var(--r-pill);overflow:hidden;margin:6px 0 4px}
.mseg span{flex:1;text-align:center;padding:9px 0;font-size:15px;font-weight:600}
.mseg .on{background:var(--wash)}
.mcorners{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mfine{margin-top:14px}
.card .pillbtn{margin-top:12px}
.mpic .mscene{vertical-align:top}
.mstrip{margin-top:-1px}
.msave{margin-bottom:16px}
.mpair{display:grid;grid-template-columns:1fr 1fr;gap:10px}
"""
BARRED = [
    (r"\bverif(?:y|ied|ies)\b|\bauthentic|\bgenuine\b|\bguarantee|\bproves?\b", "a mark is an address, never a claim (§marks-that-point)"),
    (r"\bpassed\b|\bmatches\b|\bcertified\b", "a likely match, never a check passed"),
    (r"\bsign[\s-]?in\b", "Log in authenticates; 'sign in' is barred (Default 10)"),
    (r"storage\.333\.eco/", "a storage address is never shown"),
]


def check(sid, body):
    for pat, why in BARRED:
        assert not re.search(pat, re.sub(r"<svg.*?</svg>", "", body, flags=re.S), re.I), "%s: %s" % (sid, why)
    if sid == "M1":
        assert body.count('class="kbox"') == 3 and 'class="kbox on"' not in body, "M1: every choice starts UNTICKED"
    if sid == "M4":
        assert re.search(r"never asks for a password|មិនដែលសុំពាក្យសម្ងាត់", body), "M4: a page a code opens says it never asks"
