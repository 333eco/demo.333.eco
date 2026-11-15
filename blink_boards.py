"""B-Link at B.333.eco: the estate's link resolver (A493; the spec is private, 333eco/b.333.eco SPEC.md), with the one
storage.333.eco page (A639). Imported by build-boards.py, which injects the shared helpers and draws the pages.

Copy rules this file must keep (checked at build time by check()):
  - A preview says what the link IS. ⛔ Never a saving ("saved you 12 MB"), never a count of opens, never the receiver.
  - ⛔ The public pages show NO count. The one count is the sharer's own, inside the app, and only when they ask (B6).
  - ⛔ Nothing ends by itself: no "expires", no time left. An ended link states the fact once (Sig-8).
  - ⛔ No storage address is ever drawn. A cover is B.333.eco/<code>/cover.
  - People read the host as B.333.eco (capital B); it is never the emblem.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""

# injected by build-boards.py
card = btns = spot = heart = person = None

CODE = "7k2m9qx"

DT = {
"en": {
  "foot": "B.333.eco · drawings · nothing here is live",
  "sfoot": "storage.333.eco · drawings · nothing here is live",
  "prod": "B-Link",
  # B1 the front page
  "b1_h": "One short link for everything you share",
  "b1_lede": "A B-Link is the address of something shared from a HeartBank® app: a letter, a shop, a signed file. It opens the real thing, on our own sites.",
  "b1_cards": (("It only goes to our own sites", "A B-Link can never point anywhere else. If it starts with B.333.eco, it leads to a HeartBank® app.", "door"),
               ("We count opens, never people", "Each link keeps one number: how many times it was opened. We never keep who opened it, or from where.", "count"),
               ("A link never changes", "Once made, a link points to the same place for good. It never runs out, and its code is never used again.", "pin")),
  "b1_note": "Anyone can check that a link was never changed. The log is public, and it lists no one's private links.",
  "b1_btn": "Check a link", "b1_btn2": "See the log",
  "b1_bank": "HeartBank® is a data bank of gratitude. It is not a chartered bank or financial institution; it does not provide banking services, hold deposits, or extend credit. Nothing is paid through B-Link.",
  "b1_count": "Visits to this page are counted without cookies. Links themselves carry no tracker.",
  # B2 the preview in a chat
  "b2_h": "How a B-Link looks when you send it",
  "b2_lede": "In a chat, the link shows a small card. The card says what it is, and nothing else.",
  "b2_from": "Sokha", "b2_msg": "For you, grandma",
  "b2_title": "A video letter from @sokha",
  "b2_fact": "2 minutes · signed 15 Nov 2026 · one copy, opened by this link",
  "b2_c1h": "It states a fact", "b2_c1p": "What it is, who made it, and when. Never how many people opened it, and never anything about you.",
  "b2_c2h": "The picture comes from B.333.eco", "b2_c2p": "The cover is served by the link itself. No other address is shown to anyone.",
  # B3 about this link
  "b3_h": "About this link",
  "b3_rows": (("Goes to", "thank.heartbank.com"), ("Made by", "@sokha"), ("Signed", "15 Nov 2026 · B-Trace℠ record"),
              ("Shared by", "@sokha"), ("Made on", "15 Nov 2026")),
  "b3_same": "This link has pointed to the same place since the day it was made.",
  "b3_btn": "Open it", "b3_btn2": "Check it in the log",
  "b3_priv": "We count how many times a link is opened. We never keep who opened it.",
  # B4 ended
  "b4_h": "This link was ended",
  "b4_p": "The person who made it ended it on 20 Nov 2026.",
  "b4_c1h": "Its code is never used again", "b4_c1p": "B.333.eco/%s will never lead anywhere else." % CODE,
  "b4_c2h": "Nothing ends by itself", "b4_c2p": "A link stops only when its maker ends it, or when the law requires it.",
  # B5 no link here
  "b5_h": "No link here",
  "b5_p": "B.333.eco has no link with this code. Check the address for a missing or extra letter.",
  "b5_note": "Capital and small letters are read the same.",
  "b5_btn": "What is a B-Link?",
  # B6 inside an app: your own link
  "b6_from": "Inside the app that made the link",
  "b6_h": "Your link",
  "b6_lede": "Share this address. It opens your letter.",
  "b6_btn": "Share", "b6_btn2": "Copy",
  "b6_q": "How many times was it opened?", "b6_show": "Show", "b6_after": "After you tap Show:",
  "b6_a": "Opened 12 times",
  "b6_only": "Only you can see this number. We don't know who opened it.",
  "b6_end": "End this link", "b6_endp": "It stops opening your letter. The code is never used again.",
  # ST1 storage.333.eco
  "st_h": "This is where HeartBank® apps keep photos, voices and videos",
  "st_lede": "There is nothing to open here. You reach a file through the app it belongs to, or through a B-Link someone shared with you.",
  "st_cards": (("What you were given stays yours", "A file someone gave you is kept for you. It is never removed because of a payment.", "gift"),
               ("You can always take a copy", "Every app lets you save your own files to your device, at any time.", "out"),
               ("Private means private", "A private file opens only for the people its app allows. We keep no list of who opened what.", "lock")),
  "st_op": "Run by THonly™ for every HeartBank® app.",
},
"km": {
  "foot": "B.333.eco · គំនូរ · គ្មានអ្វីនៅទីនេះដំណើរការពិតទេ",
  "sfoot": "storage.333.eco · គំនូរ · គ្មានអ្វីនៅទីនេះដំណើរការពិតទេ",
  "prod": "B-Link",
  "b1_h": "តំណខ្លីមួយសម្រាប់អ្វីៗដែលអ្នកចែករំលែក",
  "b1_lede": "B-Link គឺជាអាសយដ្ឋានរបស់អ្វីមួយដែលចែករំលែកពីកម្មវិធី HeartBank®៖ សំបុត្រ ហាង ឬឯកសារដែលបានចុះហត្ថលេខា។ វាបើករបស់ពិត នៅលើគេហទំព័ររបស់យើងផ្ទាល់។",
  "b1_cards": (("វាទៅតែគេហទំព័ររបស់យើងប៉ុណ្ណោះ", "B-Link មិនអាចចង្អុលទៅកន្លែងផ្សេងបានទេ។ បើវាចាប់ផ្ដើមដោយ B.333.eco វានាំទៅកម្មវិធី HeartBank®។", "door"),
               ("យើងរាប់ការបើក មិនរាប់មនុស្សទេ", "តំណនីមួយៗរក្សាលេខតែមួយ៖ ចំនួនដងដែលវាត្រូវបានបើក។ យើងមិនរក្សាទុកថាអ្នកណាបើក ឬបើកពីណាទេ។", "count"),
               ("តំណមិនដែលផ្លាស់ប្ដូរទេ", "ពេលបង្កើតហើយ តំណចង្អុលទៅកន្លែងដដែលជារៀងរហូត។ វាមិនអស់សុពលភាពទេ ហើយកូដរបស់វាមិនត្រូវបានប្រើម្ដងទៀតឡើយ។", "pin")),
  "b1_note": "នរណាក៏អាចពិនិត្យបានថាតំណមួយមិនដែលត្រូវបានផ្លាស់ប្ដូរ។ កំណត់ត្រាជាសាធារណៈ ហើយវាមិនរាយតំណឯកជនរបស់នរណាម្នាក់ទេ។",
  "b1_btn": "ពិនិត្យតំណមួយ", "b1_btn2": "មើលកំណត់ត្រា",
  "b1_bank": "HeartBank® គឺជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ វាមិនមែនជាធនាគារដែលមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ វាមិនផ្តល់សេវាធនាគារ មិនទទួលប្រាក់បញ្ញើ ឬផ្តល់ឥណទានទេ។ គ្មានអ្វីត្រូវបានបង់តាម B-Link ទេ។",
  "b1_count": "ការចូលមើលទំព័រនេះត្រូវបានរាប់ដោយគ្មាន cookie។ តំណខ្លួនឯងគ្មានឧបករណ៍តាមដានទេ។",
  "b2_h": "របៀបដែល B-Link បង្ហាញពេលអ្នកផ្ញើវា",
  "b2_lede": "នៅក្នុងការជជែក តំណបង្ហាញកាតតូចមួយ។ កាតប្រាប់ថាវាជាអ្វី ហើយគ្មានអ្វីផ្សេងទៀតទេ។",
  "b2_from": "សុខា", "b2_msg": "សម្រាប់លោកយាយ",
  "b2_title": "សំបុត្រវីដេអូពី @sokha",
  "b2_fact": "២ នាទី · ចុះហត្ថលេខា ១៥ វិច្ឆិកា ២០២៦ · ច្បាប់តែមួយ បើកដោយតំណនេះ",
  "b2_c1h": "វាប្រាប់ការពិត", "b2_c1p": "វាជាអ្វី អ្នកណាបង្កើត និងពេលណា។ មិនដែលប្រាប់ថាមានមនុស្សប៉ុន្មាននាក់បានបើក ហើយមិនដែលប្រាប់អ្វីអំពីអ្នកទេ។",
  "b2_c2h": "រូបភាពមកពី B.333.eco", "b2_c2p": "រូបគម្របត្រូវបានផ្ដល់ដោយតំណខ្លួនឯង។ គ្មានអាសយដ្ឋានផ្សេងត្រូវបានបង្ហាញដល់នរណាទេ។",
  "b3_h": "អំពីតំណនេះ",
  "b3_rows": (("ទៅកាន់", "thank.heartbank.com"), ("បង្កើតដោយ", "@sokha"), ("ចុះហត្ថលេខា", "១៥ វិច្ឆិកា ២០២៦ · កំណត់ត្រា B-Trace℠"),
              ("ចែករំលែកដោយ", "@sokha"), ("បង្កើតនៅ", "១៥ វិច្ឆិកា ២០២៦")),
  "b3_same": "តំណនេះចង្អុលទៅកន្លែងដដែលតាំងពីថ្ងៃដែលវាត្រូវបានបង្កើត។",
  "b3_btn": "បើកវា", "b3_btn2": "ពិនិត្យវាក្នុងកំណត់ត្រា",
  "b3_priv": "យើងរាប់ចំនួនដងដែលតំណត្រូវបានបើក។ យើងមិនរក្សាទុកថាអ្នកណាបើកទេ។",
  "b4_h": "តំណនេះត្រូវបានបញ្ចប់",
  "b4_p": "អ្នកដែលបង្កើតវាបានបញ្ចប់វានៅថ្ងៃទី ២០ វិច្ឆិកា ២០២៦។",
  "b4_c1h": "កូដរបស់វាមិនត្រូវបានប្រើម្ដងទៀតទេ", "b4_c1p": "B.333.eco/%s នឹងមិននាំទៅកន្លែងផ្សេងឡើយ។" % CODE,
  "b4_c2h": "គ្មានអ្វីបញ្ចប់ដោយខ្លួនឯងទេ", "b4_c2p": "តំណឈប់តែពេលអ្នកបង្កើតវាបញ្ចប់វា ឬពេលច្បាប់តម្រូវប៉ុណ្ណោះ។",
  "b5_h": "គ្មានតំណនៅទីនេះទេ",
  "b5_p": "B.333.eco គ្មានតំណដែលមានកូដនេះទេ។ សូមពិនិត្យអាសយដ្ឋាន ក្រែងខ្វះ ឬលើសអក្សរ។",
  "b5_note": "អក្សរធំ និងអក្សរតូចត្រូវបានអានដូចគ្នា។",
  "b5_btn": "តើ B-Link ជាអ្វី?",
  "b6_from": "នៅក្នុងកម្មវិធីដែលបង្កើតតំណ",
  "b6_h": "តំណរបស់អ្នក",
  "b6_lede": "ចែករំលែកអាសយដ្ឋាននេះ។ វាបើកសំបុត្ររបស់អ្នក។",
  "b6_btn": "ចែករំលែក", "b6_btn2": "ចម្លង",
  "b6_q": "តើវាត្រូវបានបើកប៉ុន្មានដង?", "b6_show": "បង្ហាញ", "b6_after": "បន្ទាប់ពីអ្នកចុច បង្ហាញ៖",
  "b6_a": "បានបើក ១២ ដង",
  "b6_only": "មានតែអ្នកទេដែលអាចឃើញលេខនេះ។ យើងមិនដឹងថាអ្នកណាបើកទេ។",
  "b6_end": "បញ្ចប់តំណនេះ", "b6_endp": "វាឈប់បើកសំបុត្ររបស់អ្នក។ កូដមិនត្រូវបានប្រើម្ដងទៀតទេ។",
  "st_h": "នេះជាកន្លែងដែលកម្មវិធី HeartBank® រក្សារូបថត សំឡេង និងវីដេអូ",
  "st_lede": "គ្មានអ្វីត្រូវបើកនៅទីនេះទេ។ អ្នកទៅដល់ឯកសារតាមកម្មវិធីដែលវាជាកម្មសិទ្ធិ ឬតាម B-Link ដែលមាននរណាម្នាក់ចែករំលែកជាមួយអ្នក។",
  "st_cards": (("អ្វីដែលគេឱ្យអ្នក នៅតែជារបស់អ្នក", "ឯកសារដែលមាននរណាម្នាក់ឱ្យអ្នក ត្រូវបានរក្សាទុកសម្រាប់អ្នក។ វាមិនដែលត្រូវបានដកចេញដោយសារការបង់ប្រាក់ទេ។", "gift"),
               ("អ្នកអាចយកច្បាប់ចម្លងបានជានិច្ច", "កម្មវិធីនីមួយៗឱ្យអ្នករក្សាទុកឯកសាររបស់អ្នកទៅក្នុងឧបករណ៍របស់អ្នក នៅពេលណាក៏បាន។", "out"),
               ("ឯកជន មានន័យថាឯកជន", "ឯកសារឯកជនបើកតែសម្រាប់មនុស្សដែលកម្មវិធីរបស់វាអនុញ្ញាត។ យើងមិនរក្សាបញ្ជីថាអ្នកណាបើកអ្វីទេ។", "lock")),
  "st_op": "ដំណើរការដោយ THonly™ សម្រាប់កម្មវិធី HeartBank® ទាំងអស់។",
},
}


def bspot(kind):
    """Small drawings from the board's own tokens; the heart is always the emblem (heart())."""
    s = ['<svg class="spot" width="56" height="40" viewBox="0 0 56 40" aria-hidden="true">']
    if kind == "door":     # one link, one door of ours
        s += ['<rect x="30" y="4" width="20" height="32" rx="3" fill="var(--wash)" stroke="var(--accent)"/>',
              '<circle cx="46" cy="21" r="1.6" fill="var(--accent)"/>',
              '<path d="M4 20 h20 M18 14 l6 6 l-6 6" fill="none" stroke="var(--line-strong)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>']
    elif kind == "count":  # one number, no faces
        s += ['<rect x="8" y="8" width="40" height="24" rx="6" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<text x="28" y="26" text-anchor="middle" font-family="var(--font-mono)" font-size="15" font-weight="600" fill="var(--accent)">12</text>']
    elif kind == "pin":    # a link held to one place
        s += ['<path d="M6 30 h44" stroke="var(--line-strong)" stroke-width="2.5" stroke-linecap="round"/>',
              '<path d="M28 30 v-12" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/>',
              '<circle cx="28" cy="12" r="7" fill="var(--wash)" stroke="var(--accent)" stroke-width="2"/>', heart(28, 12, .34)]
    elif kind == "gift":   # a file with the emblem: given
        s += ['<rect x="16" y="4" width="24" height="32" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)"/>', heart(28, 20, .6)]
    elif kind == "out":    # a copy leaving to your device
        s += ['<rect x="6" y="6" width="20" height="28" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<rect x="36" y="2" width="16" height="36" rx="4" fill="var(--wash)" stroke="var(--accent)"/>',
              '<path d="M22 20 h12 M30 15 l5 5 l-5 5" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>']
    elif kind == "lock":
        s += ['<rect x="16" y="18" width="24" height="18" rx="4" fill="var(--wash)" stroke="var(--accent)"/>',
              '<path d="M21 18 v-5 a7 7 0 0 1 14 0 v5" fill="none" stroke="var(--line-strong)" stroke-width="2.5"/>',
              '<circle cx="28" cy="27" r="2.2" fill="var(--accent)"/>']
    s.append('</svg>')
    return "".join(s)


def _card(h, p, kind=None):
    return '<div class="card">%s<h2>%s</h2><p>%s</p></div>' % (bspot(kind) if kind else "", h, p)


def _addr(code=CODE):
    return '<div class="field mono baddr">B.333.eco/%s</div>' % code


def _cover():
    """The preview's cover: a drawn letter with a play mark and the emblem. Art, never a real person."""
    return ('<svg class="bcover" viewBox="0 0 320 168" aria-hidden="true">'
            '<rect width="320" height="168" fill="var(--wash)"/>'
            '<rect x="88" y="34" width="144" height="100" rx="10" fill="var(--surface)" stroke="var(--line-strong)"/>'
            '<path d="M88 46 l72 48 l72 -48" fill="none" stroke="var(--line-strong)" stroke-width="2"/>'
            '<circle cx="160" cy="98" r="20" fill="var(--accent)"/>'
            '<path d="M154 88 v20 l17 -10 z" fill="var(--accent-ink)"/>'
            + heart(250, 34, 1.0) + '</svg>')


def B1(t, d):
    cards = "".join(_card(h, p, k) for h, p, k in d["b1_cards"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["b1_h"], d["b1_lede"]) + cards
            + '<div class="note">%s</div>' % d["b1_note"] + btns(d["b1_btn"], d["b1_btn2"])
            + '<p class="fine" style="margin-top:18px">%s</p><p class="fine">%s</p>' % (d["b1_bank"], d["b1_count"]))


def B2(t, d):
    chat = ('<div class="chat"><div class="who">%s</div><div class="bub">%s</div>'
            '<div class="pcard">%s<div class="pt">%s</div><div class="pf">%s</div><div class="ph">B.333.eco</div></div></div>'
            % (d["b2_from"], d["b2_msg"], _cover(), d["b2_title"], d["b2_fact"]))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["b2_h"], d["b2_lede"]) + chat
            + _card(d["b2_c1h"], d["b2_c1p"]) + _card(d["b2_c2h"], d["b2_c2p"]))


def B3(t, d):
    rows = "".join('<div class="row"><div><div class="t">%s</div></div><span class="s">%s</span></div>' % (a, b) for a, b in d["b3_rows"])
    return ("<h1>%s</h1>" % d["b3_h"] + _addr() + '<div class="card">%s</div>' % rows
            + '<div class="note">%s</div>' % d["b3_same"] + btns(d["b3_btn"], d["b3_btn2"])
            + '<p class="fine" style="margin-top:18px">%s</p>' % d["b3_priv"])


def B4(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["b4_h"], d["b4_p"]) + _addr()
            + _card(d["b4_c1h"], d["b4_c1p"], "pin") + _card(d["b4_c2h"], d["b4_c2p"]))


def B5(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["b5_h"], d["b5_p"]) + _addr("7k2m9q")
            + '<div class="note">%s</div>' % d["b5_note"] + '<div class="grow"></div>' + btns(d["b5_btn"]))


def B6(t, d):
    ask = ('<div class="card"><div class="row"><div><div class="t">%s</div></div><span class="pillbtn">%s</span></div></div>'
           % (d["b6_q"], d["b6_show"]))
    shown = ('<div class="card"><div class="row"><div><div class="t">%s</div><div class="s">%s</div></div></div></div>'
             % (d["b6_a"], d["b6_only"]))
    end = ('<div class="card"><div class="row"><div><div class="t">%s</div><div class="s">%s</div></div></div></div>'
           % (d["b6_end"], d["b6_endp"]))
    return ('<div class="from">%s</div>' % d["b6_from"] + "<h1>%s</h1><p class='lede'>%s</p>" % (d["b6_h"], d["b6_lede"])
            + _addr() + btns(d["b6_btn"], d["b6_btn2"]) + '<div style="height:18px"></div>' + ask
            + '<p class="fine" style="margin:4px 0 8px">%s</p>' % d["b6_after"] + shown + end)


def ST1(t, d):
    cards = "".join(_card(h, p, k) for h, p, k in d["st_cards"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["st_h"], d["st_lede"]) + cards + '<p class="fine" style="margin-top:18px">%s</p>' % d["st_op"])


SCREENS = [  # (id, page, title, render(t, d))
    ("B1", "blink", "The front page: what a B-Link is", B1),
    ("B2", "blink", "The preview card in a chat", B2),
    ("B3", "blink", "About this link (/<code>/about)", B3),
    ("B4", "blink", "An ended link", B4),
    ("B5", "blink", "No link with this code", B5),
    ("B6", "blink", "Inside an app: your own link, the count on request", B6),
    ("ST1", "blink", "storage.333.eco: its one page", ST1),
]
DESKTOP = []
PUBLIC = {"B1"}  # a share button only on the front page; a link's own pages are shared by the link itself
CSS = """
.baddr{display:block;margin:0 0 14px;font-size:17px;letter-spacing:.01em}
.chat{margin:4px 0 18px;padding:14px;border-radius:var(--r);background:var(--surface-2);border:1px solid var(--line)}
.chat .who{font-size:12px;color:var(--ink-dim);margin:0 0 6px 4px}
.chat .bub{display:inline-block;background:var(--accent);color:var(--accent-ink);padding:8px 14px;border-radius:18px 18px 18px 6px;font-size:15px;margin:0 0 8px}
.pcard{border-radius:14px;overflow:hidden;background:var(--surface);border:1px solid var(--line-strong);max-width:320px}
.bcover{display:block;width:100%;height:auto}
.pcard .pt{font-weight:600;font-size:15px;padding:10px 12px 2px;color:var(--ink)}
.pcard .pf{font-size:13px;line-height:1.45;padding:0 12px;color:var(--ink-dim)}
.pcard .ph{font-size:12px;padding:6px 12px 10px;color:var(--ink-faint);font-family:var(--font-mono,monospace)}
.pillbtn{font-size:13px;font-weight:600;padding:6px 14px;border-radius:var(--r-pill);border:1px solid var(--accent);color:var(--ink);background:var(--wash)}
"""
BARRED = [  # words this surface must never draw
    (r"\bsaved you\b|\bMB\b|\bGB\b", "a preview states the fact, never a saving (fact-form, 2026-09-05)"),
    (r"\bexpire[sd]?\b|\btime left\b|\bremaining\b|\bcountdown\b", "nothing ends by itself; no clock is drawn (Sig-8)"),
    (r"storage\.333\.eco/", "a storage address is never shown (§one-store item 7)"),
    (r"\bviews\b|\bclicks\b|\btrending\b|\bpopular\b", "no public count, no rank"),
]


def check(sid, body):
    import re
    for pat, why in BARRED:
        assert not re.search(pat, body, re.I), "%s: %s" % (sid, why)
    if sid != "B6":  # the one count belongs to the sharer, inside the app
        assert not re.search(r"\b\d+\s+times\b|[០-៩]+\s*ដង", body), "%s: a public page shows no count of opens" % sid
