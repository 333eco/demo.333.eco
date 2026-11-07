#!/usr/bin/env python3
"""The B-Registry screens of 333.eco: hold an @name or a #tag, make a page. Imported by build-boards.py.

Copy rules this file must keep (the build refuses them, see BARRED):
  - the fee is an exchange: never gift, tip, donation, charity, nonprofit, tax-deductible;
  - the Pool is stated as a fact, never an ask, a goal, a total or a thank-you for supporting;
  - a name is OFFERED: no screen reports a name as gone for good, and an unheld page says nothing about why;
  - no list or search of people, no counts, no score, no ticking clock;
  - Thank After always says nothing is owed; no banking word.
All names and figures are made up. The seller is left as a placeholder in these public drawings; the terms name it at launch. The Khmer is OURS and UNREVIEWED.
"""
import re

LANG = ["en"]
heart = None    # injected by build-boards.py, so the emblem stays one helper
person = None


def _(en, km):
    return km if LANG[0] == "km" else en


CSS = """
.rmark{display:inline-flex;align-items:center;gap:7px;font-weight:600;font-size:1.1rem;letter-spacing:-.01em;white-space:nowrap}
.rmark svg{width:20px;height:20px;color:var(--accent)}
.ladder{display:grid;grid-template-columns:1fr;gap:8px;margin:0 0 16px}
.rung{display:grid;grid-template-columns:104px 1fr;gap:12px;align-items:center;border:1px solid var(--line);border-radius:14px;background:var(--surface);padding:8px 14px}
.rung.on{border-color:var(--accent);background:var(--wash)}
.rung b{font-size:14px;font-weight:600}.rung span{display:block;font-size:12.5px;color:var(--ink-dim)}
.card .price{font-size:32px;font-weight:600;letter-spacing:-.02em;margin:0;color:var(--ink);line-height:1.2}
.price small{font-size:14px;font-weight:400;color:var(--ink-dim);letter-spacing:0}
.link{color:var(--accent);font-weight:600}
.handle{font-family:var(--font-mono);font-size:13px;color:var(--ink-dim)}
.said{font-size:27px;font-weight:600;line-height:1.25;margin:12px 0 2px;letter-spacing:-.01em}
.play{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line-strong);border-radius:999px;padding:7px 14px;font-size:14px;margin:8px 0 14px}
.center{text-align:center}.center svg.face{display:block;margin:10px auto 0}
.lnk{display:flex;justify-content:space-between;gap:10px;padding:12px 0;border-top:1px solid var(--line);font-size:14px}
.sum{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-top:1px solid var(--line);font-size:14px}
.sum.tot{font-weight:600;border-top:1.5px solid var(--line-strong)}
.sum i{font-style:normal;color:var(--ink-dim)}
.tagword{font:600 26px var(--font-mono);letter-spacing:-.01em;margin:12px 0 4px}
.lab{font-size:13px;color:var(--ink-dim);margin:12px 0 0}
.lab+.field{margin-top:4px}
.placeholder{font:600 11px var(--font-mono);color:var(--ink-faint);letter-spacing:.03em;margin:0 0 8px}
.desk .ladder{grid-template-columns:repeat(3,1fr)}.desk .rung{grid-template-columns:1fr;align-content:start;align-items:start}
.desk .said{font-size:34px}
.said .poh{display:inline-block;width:.8em;height:.8em;color:var(--accent);vertical-align:-.02em;margin-right:.18em}
.why{display:table;margin-left:auto;margin-right:auto;font-size:12.5px;color:var(--ink-dim);border-bottom:1px dotted var(--line-strong);margin:6px auto 2px}
.rail{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 0;border-top:1px solid var(--line);font-size:14px}
.rail:first-of-type{border-top:0}
.rail b{font-weight:600}.rail .s{display:block;font-size:12.5px;color:var(--ink-dim)}
.qr{display:block;margin:6px auto 8px;border:1px solid var(--line);border-radius:12px;background:#fff;padding:10px}
.ref{font-family:var(--font-mono);font-size:15px;letter-spacing:.06em}
"""


def brandmark(emblem):
    return '<span class="rmark"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>333.eco</span>' % emblem


FOOT = ("333.eco · sold by [the seller LLC] · visits are counted without cookies",
        "333.eco · លក់ដោយ [the seller LLC] · រាប់ការចូលមើលដោយគ្មាន cookie")

MINE = "@sokha.keo"
TAG = "#sunriseteas"


def card(h, p, svg=""):
    return '<div class="card">%s<h2>%s</h2><p>%s</p></div>' % (svg, h, p)


def head(h, lede=""):
    return "<h1>%s</h1>" % h + ("<p class='lede'>%s</p>" % lede if lede else "")


def field(label, value, area=False):
    return '<div class="lab">%s</div><div class="field%s">%s</div>' % (label, " area" if area else "", value)


def btn(a, b=None):
    return '<button class="btn">%s</button>' % a + ('<button class="btn ghost">%s</button>' % b if b else "")


def radio(rows):
    return "".join('<div class="radio%s"><i></i><span class="mono" style="font-size:15px">%s</span></div>' % (" on" if i == 0 else "", r)
                   for i, r in enumerate(rows))


def tog(t, s, on=False):
    return '<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><div class="tog%s"></div></div>' % (t, s, " on" if on else "")


def sp(body, w=56, h=40):
    return '<svg class="spot" width="%d" height="%d" viewBox="0 0 %d %d" aria-hidden="true">%s</svg>' % (w, h, w, h, body)


def s_id():      # a person and a thing, side by side
    return sp('<circle cx="14" cy="13" r="7" fill="var(--accent)"/><path d="M3 34c0-9 5-13 11-13s11 4 11 13z" fill="var(--accent)"/>'
              '<rect x="34" y="12" width="20" height="20" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)"/>'
              '<path d="M39 22h10M44 17v10" stroke="var(--ink-faint)" stroke-width="2"/>')


def s_pool():    # a pool that empties: rain rising, a heart at its middle
    return sp('<path d="M4 28c6-5 10 5 16 0s10 5 16 0 10 5 16 0v8H4z" fill="var(--wash)" stroke="var(--edge)"/>'
              '<path d="M16 16v-8M28 14V4M40 16V8" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round"/>' + heart(28, 24, .55))


def s_rule():    # one name, one line
    return sp('<rect x="3" y="6" width="50" height="28" rx="6" fill="var(--surface-2)" stroke="var(--line-strong)"/>'
              '<path d="M11 16h34M11 24h22" stroke="var(--ink-faint)" stroke-width="2.5" stroke-linecap="round"/>')


def s_river():   # the river that reverses
    return sp('<path d="M2 26c10-10 18 8 28-2s16-6 24-8" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/>'
              '<path d="M42 28l8 3-3 7M16 10l-8-3 3-5" fill="none" stroke="var(--ink-faint)" stroke-width="2" stroke-linecap="round"/>')


def s_stamp():   # a trademark sheet read by a person
    return sp('<rect x="4" y="3" width="28" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)"/>'
              '<path d="M10 12h16M10 19h16M10 26h10" stroke="var(--ink-faint)" stroke-width="2" stroke-linecap="round"/>'
              '<circle cx="42" cy="17" r="6" fill="var(--accent)"/><path d="M32 37c1-7 5-11 10-11s9 4 10 11z" fill="var(--accent)"/>')


def s_books():   # a statement
    return sp('<rect x="8" y="3" width="40" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)"/>'
              '<path d="M15 12h14M15 20h14M15 28h14" stroke="var(--ink-faint)" stroke-width="2"/>'
              '<path d="M35 12h7M35 20h7M35 28h7" stroke="var(--accent)" stroke-width="2.5"/>')


def rung(title, sub, a, b, on=False):
    """Item and money, in the order they cross: the drawing is the argument, the words only name it."""
    def cup(x): return ('<path d="M%d 8h15v11a6 6 0 0 1-6 6h-3a6 6 0 0 1-6-6z" fill="var(--ink-faint)"/>'
                        '<path d="M%d 11h3a3 3 0 0 1 0 8h-3" fill="none" stroke="var(--ink-faint)" stroke-width="2"/>' % (x, x + 15))
    def coin(x): return '<circle cx="%d" cy="16" r="8" fill="none" stroke="var(--ink-dim)" stroke-width="2"/>' % (x + 7)
    def thank(x): return heart(x + 7, 16, .8)
    d = {"cup": cup, "coin": coin, "thank": thank}
    svg = ('<svg width="96" height="32" viewBox="0 0 96 32" aria-hidden="true">%s'
           '<path d="M34 16h20M49 11l6 5-6 5" fill="none" stroke="var(--ink-faint)" stroke-width="2" stroke-linecap="round"/>%s</svg>'
           % (d[a](10), d[b](66)))
    return '<div class="rung%s">%s<div><b>%s</b><span>%s</span></div></div>' % (" on" if on else "", svg, title, sub)


def ladder():
    return ('<div class="ladder">' +
            rung(_("Pay now", "បង់ឥឡូវ"), _("Money first, then the thing.", "ប្រាក់មុន បន្ទាប់មករបស់។"), "coin", "cup") +
            rung(_("Pay later", "បង់តាមក្រោយ"), _("The thing first. You owe the money.", "របស់មុន។ អ្នកជំពាក់ប្រាក់។"), "cup", "coin") +
            rung(_("Thank after", "អរគុណតាមក្រោយ"), _("The thing first. Nothing is owed.", "របស់មុន។ មិនជំពាក់អ្វីទេ។"), "cup", "thank", True) +
            '</div>')


def _front_words():
    return (_("Pay now.<br>Pay later.<br>Thank after.", "បង់ឥឡូវ។<br>បង់តាមក្រោយ។<br>អរគុណតាមក្រោយ។"),
            _("Thank After means you get it first, then decide what thanks it's worth. Nothing is owed.",
              "អរគុណតាមក្រោយ មានន័យថា អ្នកទទួលបានរបស់មុន រួចសម្រេចថាវាសមនឹងការអរគុណប៉ុណ្ណា។ មិនជំពាក់អ្វីទេ។"),
            _("Holding an @name or a #tag helps support it.", "ការកាន់ @name ឬ #tag ជួយគាំទ្រវា។"))


def _pool_card():
    return card(_("Where the money goes", "ប្រាក់ទៅណា"),
                _("All profits from names and tags are held for the Aquarian Pool℠, which gives every verified person something to thank with, each 7 January. "
                  "The Pool isn't running yet, so for now the money waits in a separate account. <span class='link'>See the statement</span>",
                  "ប្រាក់ចំណេញទាំងអស់ពីឈ្មោះ និងស្លាក ត្រូវរក្សាទុកសម្រាប់ Aquarian Pool℠ ដែលផ្ដល់អ្វីមួយសម្រាប់អរគុណដល់មនុស្សគ្រប់រូបដែលបានផ្ទៀងផ្ទាត់ រៀងរាល់ថ្ងៃទី៧ មករា។ "
                  "Pool មិនទាន់ដំណើរការទេ ដូច្នេះឥឡូវនេះប្រាក់ស្ថិតនៅក្នុងគណនីដាច់ដោយឡែក។ <span class='link'>មើលរបាយការណ៍</span>"), s_pool())


def _id_card():
    return card(_("A person has a name. A thing has a tag.", "មនុស្សមានឈ្មោះ។ របស់មានស្លាក។"),
                _("An @name is how people find you and thank you, said the way your family says it: 333.eco/@sokha.keo. "
                  "A #tag is the address of a company, a place or a machine: 333.eco/sunriseteas. A name costs $3 to $12 a year, set by your card's country. A tag costs $33 or $333, set the same way.",
                  "@name គឺជារបៀបដែលគេរកឃើញ និងអរគុណអ្នក ហៅតាមរបៀបគ្រួសារអ្នកហៅ៖ 333.eco/@sokha.keo។ "
                  "#tag គឺជាអាសយដ្ឋានរបស់ក្រុមហ៊ុន ទីកន្លែង ឬម៉ាស៊ីន៖ 333.eco/sunriseteas។ ឈ្មោះមានតម្លៃ ៣ ទៅ ១២ ដុល្លារក្នុងមួយឆ្នាំ តាមប្រទេសនៃប័ណ្ណរបស់អ្នក។ ស្លាកមានតម្លៃ ៣៣ ឬ ៣៣៣ ដុល្លារ តាមរបៀបដូចគ្នា។"), s_id())


def _find():
    return (field(_("Your name, the way you write it", "ឈ្មោះរបស់អ្នក តាមរបៀបដែលអ្នកសរសេរ"), "Sokha Keo") +
            btn(_("Show me names", "បង្ហាញឈ្មោះឱ្យខ្ញុំ")))


def R1():     # front door
    h, l, s = _front_words()
    return (head(h, l) + ladder() + '<div class="note">%s</div>' % s + _find() + '<div style="height:16px"></div>' + _id_card() + _pool_card() +
            '<p class="fine"><span class="link">%s</span></p>' % _("The rules, in plain words", "ច្បាប់ ជាពាក្យសាមញ្ញ"))


def R1D():
    h, l, s = _front_words()
    return ('<div class="cols"><div>' + head(h, l) + ladder() + '<div class="note">%s</div>' % s + '</div><div>' + _find() + '</div></div>'
            '<div class="cols" style="grid-template-columns:1fr 1fr;margin-top:24px"><div>' + _id_card() + '</div><div>' + _pool_card() + '</div></div>')


OFFERS = ["@sokha.keo", "@sokhakeo", "@sokha.k", "@keo.sokha"]


def R2():
    return (head(_("Names for you", "ឈ្មោះសម្រាប់អ្នក"), _("From what you wrote: Sokha Keo. Pick one, or write it another way.", "ពីអ្វីដែលអ្នកសរសេរ៖ Sokha Keo។ ជ្រើសមួយ ឬសរសេរតាមរបៀបផ្សេង។")) +
            '<div class="card">' + radio(OFFERS) + '</div>' +
            field(_("Write it another way", "សរសេរតាមរបៀបផ្សេង"), "Sokha Keo") +
            btn(_("Hold this name", "កាន់ឈ្មោះនេះ")) +
            '<p class="fine">%s</p>' % _("One name per person. It can't be sold or passed on. Next you log in with HeartBank®, then you see the fee before you pay.",
                                         "ឈ្មោះមួយក្នុងមនុស្សម្នាក់។ មិនអាចលក់ ឬផ្ទេរបានទេ។ បន្ទាប់មកអ្នកចូលជាមួយ HeartBank® រួចឃើញថ្លៃមុនពេលបង់។"))


def R3():
    rows = ["@sokha.keo.pp", "@sokha.k.keo", "@s.keo"]
    return (head(_("That one just went", "ឈ្មោះនោះទើបតែបាត់"), _("Here are three more, from the same name.", "នេះគឺបីទៀត ពីឈ្មោះដដែល។")) +
            '<div class="card">' + radio(rows) + '</div>' + btn(_("Hold this name", "កាន់ឈ្មោះនេះ")))


def _hold_facts():
    return ('<ul class="dots" style="margin-top:12px">' + "".join("<li><i></i><span>%s</span></li>" % x for x in (
        _("You hold a registration. You don't own the name.", "អ្នកកាន់ការចុះឈ្មោះ។ អ្នកមិនមែនជាម្ចាស់ឈ្មោះនោះទេ។"),
        _("Names are for adults, and holding one needs a passkey on your account.", "ឈ្មោះសម្រាប់មនុស្សពេញវ័យ ហើយការកាន់ឈ្មោះត្រូវការ passkey នៅលើគណនីរបស់អ្នក។"),
        _("Sold by [the seller LLC]. <span class='link'>Terms</span>", "លក់ដោយ [the seller LLC]។ <span class='link'>លក្ខខណ្ឌ</span>"))) + '</ul>')


def R4():     # the fee, before the card says which
    return (head(_("Hold %s" % MINE, "កាន់ %s" % MINE)) +
            '<div class="card"><p class="price">$3 – $12 <small>%s</small></p><p style="margin-top:6px">%s</p></div>' % (
                _("a year", "ក្នុងមួយឆ្នាំ"),
                _("The fee follows your card's country, by the World Bank's four income groups. You'll see the exact fee before you pay.",
                  "ថ្លៃតាមប្រទេសនៃប័ណ្ណរបស់អ្នក តាមក្រុមប្រាក់ចំណូលទាំងបួនរបស់ធនាគារពិភពលោក។ អ្នកនឹងឃើញថ្លៃពិតប្រាកដមុនពេលបង់។")) +
            field(_("Card number", "លេខប័ណ្ណ"), "•••• •••• •••• 4242") +
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + field(_("Expires", "ផុតកំណត់"), "11 / 29") + field("CVC", "•••") + '</div>' +
            btn(_("See my fee", "មើលថ្លៃរបស់ខ្ញុំ")) + _hold_facts())


def R5():     # the fee, once known
    return (head(_("Hold %s" % MINE, "កាន់ %s" % MINE)) +
            '<div class="card"><p class="price">$6 <small>%s</small></p><p style="margin-top:6px">%s</p></div>' % (
                _("a year", "ក្នុងមួយឆ្នាំ"),
                _("Your card is from Cambodia. The fee is the same for every card from there.", "ប័ណ្ណរបស់អ្នកមកពីកម្ពុជា។ ថ្លៃដូចគ្នាសម្រាប់គ្រប់ប័ណ្ណមកពីទីនោះ។")) +
            '<div class="card">' + tog(_("Renew each year", "បន្តរៀងរាល់ឆ្នាំ"), _("Off unless you turn it on. You can change it any time.", "បិទ លុះត្រាអ្នកបើក។ អ្នកអាចប្ដូរបានគ្រប់ពេល។")) + '</div>' +
            btn(_("Pay $6 and hold it", "បង់ ៦ ដុល្លារ ហើយកាន់វា")) + _hold_facts())


def _qr(px=168):
    """A drawn stand-in for a KHQR code: a fixed pattern, never a scannable code."""
    import random
    rnd = random.Random(333)
    n, c = 25, px / 25.0
    r = ['<svg class="qr" width="%d" height="%d" viewBox="0 0 %d %d" aria-hidden="true">' % (px + 20, px + 20, px, px)]
    for y in range(n):
        for x in range(n):
            corner = any(x0 <= x < x0 + 7 and y0 <= y < y0 + 7 for x0, y0 in ((0, 0), (n - 7, 0), (0, n - 7)))
            on = ((x in (0, 6) or y in (0, 6) or (2 <= x <= 4 and 2 <= y <= 4)) if corner and (x < 7 and y < 7) else
                  (x in (n - 7, n - 1) or y in (0, 6) or (n - 5 <= x <= n - 3 and 2 <= y <= 4)) if corner and x >= n - 7 else
                  (x in (0, 6) or y in (n - 7, n - 1) or (2 <= x <= 4 and n - 5 <= y <= n - 3)) if corner else rnd.random() < .45)
            if on:
                r.append('<rect x="%.1f" y="%.1f" width="%.2f" height="%.2f" fill="#111"/>' % (x * c, y * c, c + .1, c + .1))
    r.append('</svg>')
    return "".join(r)


def R5K():    # Cambodia: KHQR, settled by hand
    return ('<p class="placeholder">[ PLACEHOLDER RATE AND ACCOUNT ]</p>' + head(_("Hold %s" % MINE, "កាន់ %s" % MINE)) +
            '<div class="card center"><p class="price">24,600៛ <small>%s</small></p><p style="margin-top:4px">%s</p>' % (
                _("a year", "ក្នុងមួយឆ្នាំ"), _("$6 at the posted rate of 4,100៛.", "៦ ដុល្លារ តាមអត្រាដែលបានបង្ហាញ ៤.១០០៛។")) +
            _qr() + '<div class="lab">%s</div><div class="ref">333-K7QF</div></div>' % _("Reference", "លេខយោង") +
            '<ul class="dots">' + "".join("<li><i></i><span>%s</span></li>" % x for x in (
                _("Pay in your bank app. The reference is already in the code.", "បង់នៅក្នុងកម្មវិធីធនាគាររបស់អ្នក។ លេខយោងមាននៅក្នុងកូដរួចហើយ។"),
                _("We keep the name for you for 3 days while we check. We'll email you when it's yours.", "យើងរក្សាឈ្មោះសម្រាប់អ្នក ៣ ថ្ងៃ ខណៈយើងពិនិត្យ។ យើងនឹងផ្ញើអ៊ីមែលពេលវាជារបស់អ្នក។"),
                _("Paid to [the registry's KHQR account], used for nothing else.", "បង់ទៅ [គណនី KHQR របស់បញ្ជី] ដែលមិនប្រើសម្រាប់អ្វីផ្សេងទៀតទេ។"))) + '</ul>' +
            _hold_facts())


def R6():     # held
    return (head(_("%s is yours to hold" % MINE, "%s ជារបស់អ្នកសម្រាប់កាន់" % MINE), _("Through 5 November 2027. Your receipt is in your email.", "រហូតដល់ ៥ វិច្ឆិកា ២០២៧។ បង្កាន់ដៃនៅក្នុងអ៊ីមែលរបស់អ្នក។")) +
            card(_("Make your page", "បង្កើតទំព័ររបស់អ្នក"), _("Say your name your way, in your own voice if you like. Only you write it.", "ហៅឈ្មោះតាមរបៀបរបស់អ្នក ដោយសំឡេងផ្ទាល់ប្រសិនបើអ្នកចង់។ មានតែអ្នកទេដែលសរសេរវា។"), s_id()) +
            btn(_("Make my page", "បង្កើតទំព័ររបស់ខ្ញុំ")))


def R7():     # your page, editing
    return (head(_("Your page", "ទំព័ររបស់អ្នក"), '<span class="mono">333.eco/@sokha.keo</span>') +
            field(_("Your name as you write it", "ឈ្មោះរបស់អ្នកតាមរបៀបដែលអ្នកសរសេរ"), "សុខា កែវ · Sokha Keo") +
            '<div class="lab">%s</div><div class="play">▶ %s</div>' % (_("Your name, said by you (you choose)", "ឈ្មោះរបស់អ្នក ហៅដោយអ្នក (អ្នកជ្រើសរើស)"), _("Record it", "ថតសំឡេង")) +
            field(_("A short line", "បន្ទាត់ខ្លី"), _("I make kites in Kampot.", "ខ្ញុំធ្វើខ្លែងនៅកំពត។")) +
            field(_("Links", "តំណ"), "sokhakites.example") +
            btn(_("Save", "រក្សាទុក")) +
            '<div class="sh">%s</div><div class="card">' % _("Ways to send you money (optional)", "វិធីផ្ញើប្រាក់ឱ្យអ្នក (ស្រេចចិត្ត)") +
            '<div class="rail"><span><b>KHQR</b><span class="s">ABA · Sokha Keo</span></span><span class="link">%s</span></div>' % _("Change", "ប្ដូរ") +
            '<div class="rail"><span><b>Zelle</b><span class="s">s•••@example.com</span></span><span class="link">%s</span></div>' % _("Change", "ប្ដូរ") +
            '<div class="more">+ %s</div></div>' % _("Add a way", "បន្ថែមវិធី") +
            '<p class="fine" style="margin-top:0">%s</p>' % _("People see these only after they thank you. KHQR shows your name and Zelle your email or phone to whoever sends. A change needs your passkey, and we'll email you when it happens.",
                                                              "មនុស្សឃើញវាតែបន្ទាប់ពីពួកគេអរគុណអ្នក។ KHQR បង្ហាញឈ្មោះរបស់អ្នក ហើយ Zelle បង្ហាញអ៊ីមែល ឬលេខទូរស័ព្ទ ដល់អ្នកដែលផ្ញើ។ ការប្ដូរត្រូវការ passkey របស់អ្នក ហើយយើងនឹងផ្ញើអ៊ីមែលពេលវាកើតឡើង។") +
            '<div class="sh">%s</div><div class="card">' % _("Yours", "របស់អ្នក") +
            tog(_("Renew each year", "បន្តរៀងរាល់ឆ្នាំ"), _("Held through 5 November 2027.", "កាន់រហូតដល់ ៥ វិច្ឆិកា ២០២៧។")) +
            tog(_("Let search engines find my page", "អនុញ្ញាតឱ្យម៉ាស៊ីនស្វែងរករកឃើញទំព័ររបស់ខ្ញុំ"), _("Off unless you turn it on.", "បិទ លុះត្រាអ្នកបើក។")) +
            '</div><button class="btn ghost">%s</button>' % _("Download my page, any time", "ទាញយកទំព័ររបស់ខ្ញុំ គ្រប់ពេល"))


def _face():
    return ('<svg class="face" width="104" height="104" viewBox="-40 -40 80 80" aria-hidden="true">%s</svg>'
            % person(0, 0, "var(--accent)", "#c98f5c", "#2a1a12", "bun"))


def _said():
    return ('<div class="said">' + POH + 'សុខា កែវ</div><div class="handle">Sokha Keo · @sokha.keo</div>'
            '<div class="why">ⓘ %s</div>' % _("Why the heart beats", "ហេតុអ្វីបេះដូងលោត") +
            '<div class="play">▶ %s</div><p class="lede">%s</p>' % (_("Hear it said", "ស្ដាប់ការហៅឈ្មោះ"), _("I make kites in Kampot.", "ខ្ញុំធ្វើខ្លែងនៅកំពត។")))


POH = None  # set below, once the emblem path is known


def poh(emblem):
    """The Proof of Humanity mark beside a person: it beats on EVERY @name page alike (founder 2026-11-06),
    because holding a name needs a passkey. Its disclaimer says what that does and doesn't show."""
    global POH
    POH = '<svg class="poh beating" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>' % emblem


DISCLAIMER = ("This heart beats on every @name: each is held by someone who logs in with a passkey. "
              "A passkey shows they hold a key. It doesn't show who they are, or that they're only one person.",
              "បេះដូងនេះលោតនៅលើគ្រប់ @name៖ ម្នាក់ៗត្រូវបានកាន់ដោយអ្នកដែលចូលដោយ passkey។ "
              "passkey បង្ហាញថាពួកគេកាន់សោមួយ។ វាមិនបង្ហាញថាពួកគេជានរណា ឬថាពួកគេជាមនុស្សតែម្នាក់នោះទេ។")


def R8P():    # the disclaimer, one tap from the beat
    return ('<div class="center">' + _face() + _said() + '</div><div class="scrim"></div><div class="sheet"><div class="grab"></div>' +
            '<h1 style="font-size:22px">%s</h1>' % _("Why the heart beats", "ហេតុអ្វីបេះដូងលោត") +
            '<p class="lede">%s</p>' % _(DISCLAIMER[0], DISCLAIMER[1]) +
            '<div class="sh">%s</div><div class="card">' % _("What HeartBank® can show today", "អ្វីដែល HeartBank® អាចបង្ហាញបាននៅថ្ងៃនេះ") +
            "".join('<div class="rail"><span>%s</span><span class="pill%s">%s</span></div>' % (a, " on" if i == 0 else "", b) for i, (a, b) in enumerate((
                (_("A passkey", "passkey"), _("Live", "ដំណើរការ")),
                (_("A family tree vouched for by relatives", "មែកធាងគ្រួសារ ដែលសាច់ញាតិធានា"), _("Being built", "កំពុងសាងសង់")),
                (_("Live breath, from a wearable heart", "ដង្ហើមផ្ទាល់ ពីបេះដូងពាក់"), _("Planned", "គ្រោងទុក")),
                (_("A family tree checked by DNA", "មែកធាងគ្រួសារ ដែលពិនិត្យដោយ DNA"), _("Planned", "គ្រោងទុក"))))) + '</div>' +
            '<p class="fine" style="margin-top:0">%s</p>' % _("This list is the same on every page. It says what HeartBank® can do, not what this person has done. If a name ever needs more than a passkey, this note will say so.",
                                                              "បញ្ជីនេះដូចគ្នានៅគ្រប់ទំព័រ។ វានិយាយពីអ្វីដែល HeartBank® អាចធ្វើ មិនមែនអ្វីដែលមនុស្សនេះបានធ្វើទេ។ ប្រសិនបើឈ្មោះណាមួយត្រូវការលើសពី passkey កំណត់ចំណាំនេះនឹងប្រាប់។") +
            btn(_("Close", "បិទ")) + '</div>')


def _rails():
    rows = (("KHQR", _("Cambodia", "កម្ពុជា")), ("Zelle", _("United States", "សហរដ្ឋអាមេរិក")), ("Wise", _("most countries", "ប្រទេសភាគច្រើន")))
    return '<div class="card">' + "".join('<div class="rail"><span><b>%s</b><span class="s">%s</span></span><span class="link">%s</span></div>' % (n, w, _("Open", "បើក")) for n, w in rows) + '</div>'


def R8T():    # thanking: words first, always
    return (head(_("Thank @sokha.keo", "អរគុណ @sokha.keo"), _("Say what you're thanking her for. That's the thanks; nothing else is needed.", "និយាយថាអ្នកអរគុណនាងចំពោះអ្វី។ នោះហើយជាការអរគុណ គ្មានអ្វីផ្សេងទៀតត្រូវការទេ។")) +
            field(_("Your words", "ពាក្យរបស់អ្នក"), _("The kite you made for my daughter flew all afternoon.", "ខ្លែងដែលអ្នកធ្វើឱ្យកូនស្រីខ្ញុំ ហោះពេញមួយរសៀល។"), True) +
            btn(_("Send my thanks", "ផ្ញើការអរគុណរបស់ខ្ញុំ")) +
            '<p class="fine">%s</p>' % _("Your thanks carries Kiitos, which is how HeartBank® records a thank-you. Nothing is owed.", "ការអរគុណរបស់អ្នកមាន Kiitos ដែលជារបៀបដែល HeartBank® កត់ត្រាការអរគុណ។ មិនជំពាក់អ្វីទេ។"))


def R8M():    # after the words: money, only if they'd like
    return (head(_("Your thanks reached @sokha.keo", "ការអរគុណរបស់អ្នកបានទៅដល់ @sokha.keo")) +
            '<div class="sh">%s</div>' % _("Send money too, only if you'd like", "ផ្ញើប្រាក់ផងដែរ លុះត្រាតែអ្នកចង់") +
            _rails() +
            '<p class="fine">%s</p>' % _("These are Sokha's own accounts; the money goes straight to her. 333.eco never learns whether you sent anything. KHQR and Zelle show each of you the other's name.",
                                         "ទាំងនេះជាគណនីផ្ទាល់របស់សុខា ប្រាក់ទៅដល់នាងផ្ទាល់។ 333.eco មិនដែលដឹងថាអ្នកបានផ្ញើអ្វីឬអត់ទេ។ KHQR និង Zelle បង្ហាញឈ្មោះរបស់អ្នកទាំងពីរដល់គ្នាទៅវិញទៅមក។") +
            '<button class="btn ghost">%s</button>' % _("Done", "រួចរាល់"))


def _thank():
    return '<button class="btn">%s</button>' % _("Thank @sokha.keo", "អរគុណ @sokha.keo")


def _links():
    return '<div class="lnk"><span>sokhakites.example</span><span class="link">↗</span></div>'


def R8():     # a person's page, as a visitor sees it: nothing here counts anyone
    return '<div class="center">' + _face() + _said() + '</div>' + _thank() + '<div style="height:14px"></div>' + _links()


def R8D():
    return ('<div class="cols"><div>' + _face().replace('margin', 'x') + _said() + '</div><div>' + _thank() + '<div style="height:14px"></div>' + _links() + '</div></div>')


def R9():     # one plain notice, before the year ends
    return (head(_("Your year for %s ends on 5 November" % MINE, "ឆ្នាំរបស់អ្នកសម្រាប់ %s បញ្ចប់នៅថ្ងៃទី៥ វិច្ឆិកា" % MINE),
                 _("Renewal is off, so nothing will be charged. If you'd like another year, it's $6.", "ការបន្តបានបិទ ដូច្នេះនឹងមិនគិតប្រាក់ទេ។ ប្រសិនបើអ្នកចង់បានមួយឆ្នាំទៀត វាគឺ ៦ ដុល្លារ។")) +
            btn(_("Hold it another year", "កាន់វាមួយឆ្នាំទៀត")))


def R10():    # after the year: the fact, once
    return (head(_("Your year for %s has ended" % MINE, "ឆ្នាំរបស់អ្នកសម្រាប់ %s បានបញ្ចប់" % MINE),
                 _("We keep the name for you for 90 days, until 3 February 2028. Your page is in your download, whatever you decide.",
                   "យើងរក្សាឈ្មោះសម្រាប់អ្នក ៩០ ថ្ងៃ រហូតដល់ ៣ កុម្ភៈ ២០២៨។ ទំព័ររបស់អ្នកនៅក្នុងឯកសារទាញយក ទោះអ្នកសម្រេចយ៉ាងណាក៏ដោយ។")) +
            btn(_("Hold it another year, $6", "កាន់វាមួយឆ្នាំទៀត ៦ ដុល្លារ"), _("Download my page", "ទាញយកទំព័ររបស់ខ្ញុំ")))


def R11():    # the same page for a name nobody holds and a name whose year ended: it can't show which
    return ('<div class="center"><div class="tagword" style="margin-top:40px">@sokha.keo</div><p class="lede">%s</p></div>' % _("Names here belong to people, said the way they say them.", "ឈ្មោះនៅទីនេះជារបស់មនុស្ស ហៅតាមរបៀបដែលពួកគេហៅ។") +
            btn(_("Find your own name", "រកឈ្មោះរបស់អ្នក")))


def R12():    # the tag page
    return (head(_("A thing has a tag", "របស់មានស្លាក"),
                 _("A #tag is the address of a company, a product, a place or a machine. It lives at 333.eco/yourtag.",
                   "#tag គឺជាអាសយដ្ឋានរបស់ក្រុមហ៊ុន ផលិតផល ទីកន្លែង ឬម៉ាស៊ីន។ វានៅ 333.eco/yourtag។")) +
            '<div class="note">%s</div>' % _("Holding a #tag helps support Thank After.", "ការកាន់ #tag ជួយគាំទ្រការអរគុណតាមក្រោយ។") +
            '<div class="card"><p class="price">$33 <small>%s</small> $333</p><p style="margin-top:6px">%s</p></div>' % (
                _("or", "ឬ"),
                _("$33 a year when your card is from a low or lower-middle income country, $333 everywhere else. This price doesn't fall. The @name fee is meant to, because brands are not the point and people are.",
                  "៣៣ ដុល្លារក្នុងមួយឆ្នាំ ពេលប័ណ្ណរបស់អ្នកមកពីប្រទេសដែលមានប្រាក់ចំណូលទាប ឬមធ្យមកម្រិតទាប និង ៣៣៣ ដុល្លារនៅកន្លែងផ្សេងទៀត។ តម្លៃនេះមិនធ្លាក់ចុះទេ។ ថ្លៃ @name ត្រូវបានគេរំពឹងថានឹងធ្លាក់ចុះ ព្រោះយីហោមិនមែនជាគោលដៅទេ មនុស្សទើបជាគោលដៅ។")) +
            btn(_("Claim a tag for a business", "ទាមទារស្លាកសម្រាប់អាជីវកម្ម"), _("Ask for a free tag: a river, a temple, a species", "សុំស្លាកឥតគិតថ្លៃ៖ ទន្លេ វត្ត ប្រភេទសត្វ")) +
            '<div style="height:14px"></div>' +
            card(_("An address, nothing more", "អាសយដ្ឋាន គ្មានអ្វីលើសពីនេះ"),
                 _("A tag buys no placement: nothing here sorts by who paid. It says what something is, not that anyone approves of it. Ten tags per holder, more if you ask.",
                   "ស្លាកមិនទិញទីតាំងបង្ហាញទេ៖ គ្មានអ្វីនៅទីនេះតម្រៀបតាមអ្នកបង់ទេ។ វានិយាយថាវាជាអ្វី មិនមែនថាមានអ្នកយល់ព្រមនោះទេ។ ស្លាកដប់ក្នុងម្ចាស់ម្នាក់ ច្រើនជាងនេះបើអ្នកសុំ។"), s_rule()) +
            '<p class="fine">%s</p>' % _("A shop that opens on HeartBank® gets its tag free.", "ហាងដែលបើកនៅលើ HeartBank® ទទួលបានស្លាកឥតគិតថ្លៃ។"))


def R13():    # the brand window
    return (head(_("Claim %s" % TAG, "ទាមទារ %s" % TAG),
                 _("For the first 90 days after tags open, business tags go to trademark holders first, so nobody can hold a name that's yours.",
                   "ក្នុងរយៈពេល ៩០ ថ្ងៃដំបូងបន្ទាប់ពីបើកស្លាក ស្លាកអាជីវកម្មទៅកាន់ម្ចាស់ពាណិជ្ជសញ្ញាមុន ដើម្បីកុំឱ្យអ្នកណាកាន់ឈ្មោះដែលជារបស់អ្នក។")) +
            field(_("Trademark registration number", "លេខចុះបញ្ជីពាណិជ្ជសញ្ញា"), "KH / 12345") +
            field(_("Where it's registered", "កន្លែងចុះបញ្ជី"), _("Cambodia", "កម្ពុជា")) +
            field(_("Company name on the registration", "ឈ្មោះក្រុមហ៊ុននៅលើការចុះបញ្ជី"), "Sunrise Teas Co.") +
            btn(_("Send it to be read", "ផ្ញើឱ្យគេអាន")) +
            card(_("A person reads each one", "មនុស្សម្នាក់អានម្ដងមួយៗ"), _("After the 90 days, the first valid claim holds the tag. If a brand disagrees, disputes go through the published rules.",
                 "បន្ទាប់ពី ៩០ ថ្ងៃ ការទាមទារត្រឹមត្រូវដំបូងកាន់ស្លាកនោះ។ ប្រសិនបើយីហោណាមួយមិនយល់ស្រប វិវាទឆ្លងកាត់ច្បាប់ដែលបានបោះពុម្ព។"), s_stamp()).replace('<div class="card">', '<div class="card" style="margin-top:16px">'))


def R14():    # read and accepted: pay
    return (head(_("%s is ready for you" % TAG, "%s រួចរាល់សម្រាប់អ្នក" % TAG), _("A person read your registration and it matches.", "មនុស្សម្នាក់បានអានការចុះបញ្ជីរបស់អ្នក ហើយវាត្រូវគ្នា។")) +
            '<div class="card"><p class="price">$33 <small>%s</small></p><p style="margin-top:6px">%s</p></div>' % (_("a year", "ក្នុងមួយឆ្នាំ"), _("Your card is from Cambodia.", "ប័ណ្ណរបស់អ្នកមកពីកម្ពុជា។")) +
            '<div class="card">' + tog(_("Renew each year", "បន្តរៀងរាល់ឆ្នាំ"), _("Off unless you turn it on.", "បិទ លុះត្រាអ្នកបើក។")) + '</div>' +
            field(_("Card number", "លេខប័ណ្ណ"), "•••• •••• •••• 4242") +
            btn(_("Pay $33 and hold it", "បង់ ៣៣ ដុល្លារ ហើយកាន់វា"), _("Pay with KHQR instead", "បង់តាម KHQR ជំនួសវិញ")) +
            '<p class="fine">%s</p>' % _("Sold by [the seller LLC]. A tag can move with the business that holds it.", "លក់ដោយ [the seller LLC]។ ស្លាកអាចផ្លាស់ទីជាមួយអាជីវកម្មដែលកាន់វា។"))


def R15():    # the steward lane: no fee anywhere on this path
    return (head(_("A free tag, for what can't speak for itself", "ស្លាកឥតគិតថ្លៃ សម្រាប់អ្វីដែលមិនអាចនិយាយដោយខ្លួនឯង"),
                 _("A river, a temple, a species, a machine with no business behind it. It's never paid for: someone looks after it.",
                   "ទន្លេ វត្ត ប្រភេទសត្វ ម៉ាស៊ីនដែលគ្មានអាជីវកម្មនៅពីក្រោយ។ វាមិនត្រូវបានបង់ថ្លៃឡើយ៖ មានអ្នកថែរក្សាវា។")) +
            field(_("What is it?", "វាជាអ្វី?"), _("The Tonlé Sap", "ទន្លេសាប")) +
            field(_("The tag you'd like", "ស្លាកដែលអ្នកចង់បាន"), "#tonlesap") +
            field(_("Who are you to it?", "តើអ្នកជាអ្វីចំពោះវា?"), _("We run a fishing community's school on the lake.", "យើងដំណើរការសាលារបស់សហគមន៍នេសាទនៅលើបឹង។"), True) +
            btn(_("Send it to be read", "ផ្ញើឱ្យគេអាន")) +
            '<p class="fine">%s</p>' % _("A person reads each one. Looking after a tag doesn't make you its owner.", "មនុស្សម្នាក់អានម្ដងមួយៗ។ ការថែរក្សាស្លាកមិនធ្វើឱ្យអ្នកក្លាយជាម្ចាស់វាទេ។"))


def R16():    # a company's tag page
    return ('<div class="tagword">%s</div>' % TAG + '<p class="lede">%s</p>' % _("Sunrise Teas Co. Green tea from Mondulkiri.", "Sunrise Teas Co. តែបៃតងពីមណ្ឌលគិរី។") +
            '<div class="lnk"><span>sunriseteas.example</span><span class="link">↗</span></div>' +
            '<p class="fine">%s <span class="link">%s</span></p>' % (_("A #tag is an address, written by whoever holds it. It isn't an approval.", "#tag គឺជាអាសយដ្ឋាន សរសេរដោយអ្នកកាន់វា។ វាមិនមែនជាការយល់ព្រមទេ។"), _("What's a tag?", "តើស្លាកជាអ្វី?")))


def R17():    # a steward's tag page
    return ('<div class="tagword">#tonlesap</div>' + s_river() +
            '<p class="lede">%s</p>' % _("The Tonlé Sap, renowned as the river that reverses its course twice a year.", "ទន្លេសាប ល្បីថាជាទន្លេដែលបង្វែរទិសហូររបស់វាពីរដងក្នុងមួយឆ្នាំ។") +
            '<div class="card"><h2>%s</h2><p>%s</p></div>' % (_("Looked after by", "ថែរក្សាដោយ"), _("A lake school (made up for this drawing). No fee: a river never pays.", "សាលាមួយនៅបឹង (បង្កើតឡើងសម្រាប់គំនូរនេះ)។ គ្មានថ្លៃ៖ ទន្លេមិនដែលបង់ទេ។")))


def R18():    # the rules
    rows = (("1", _("One name per person. It can't be sold or passed on.", "ឈ្មោះមួយក្នុងមនុស្សម្នាក់។ មិនអាចលក់ ឬផ្ទេរបានទេ។")),
            ("2", _("A name ends if its year ends. It's never confiscated for not paying.", "ឈ្មោះបញ្ចប់ បើឆ្នាំរបស់វាបញ្ចប់។ មិនត្រូវបានរឹបអូសដោយសារមិនបង់ទេ។")),
            ("3", _("Nothing here goes from a name to who someone is. There's no list or search of people.", "គ្មានអ្វីនៅទីនេះនាំពីឈ្មោះទៅកាន់អត្តសញ្ញាណមនុស្សទេ។ គ្មានបញ្ជី ឬការស្វែងរកមនុស្សទេ។")),
            ("4", _("A name can be ended for impersonation, harassment or a slur. It never goes to whoever complained.", "ឈ្មោះអាចត្រូវបញ្ចប់ដោយសារការក្លែងបន្លំ ការយាយី ឬពាក្យជេរ។ វាមិនដែលទៅកាន់អ្នកប្ដឹងទេ។")),
            ("5", _("A trademark claim can't take a person's name. That's what #tag is for.", "ការទាមទារពាណិជ្ជសញ្ញាមិនអាចយកឈ្មោះមនុស្សបានទេ។ នោះហើយជាមូលហេតុដែលមាន #tag។")))
    fees = ((_("Low income", "ប្រាក់ចំណូលទាប"), "$3"), (_("Lower-middle income", "ប្រាក់ចំណូលមធ្យមកម្រិតទាប"), "$6"),
            (_("Upper-middle income", "ប្រាក់ចំណូលមធ្យមកម្រិតខ្ពស់"), "$9"), (_("High income, or a country not on the list", "ប្រាក់ចំណូលខ្ពស់ ឬប្រទេសដែលមិននៅក្នុងបញ្ជី"), "$12"))
    return (head(_("The rules", "ច្បាប់")) + '<ul class="dots">' + "".join("<li><i></i><span>%s</span></li>" % r for _n, r in rows) + '</ul>' +
            '<div class="sh">%s</div>' % _("The @name fee, per year", "ថ្លៃ @name ក្នុងមួយឆ្នាំ") +
            "".join('<div class="sum"><i>%s</i><span>%s</span></div>' % f for f in fees) +
            '<div class="sh">%s</div>' % _("The #tag fee, per year", "ថ្លៃ #tag ក្នុងមួយឆ្នាំ") +
            '<div class="sum"><i>%s</i><span>$33</span></div><div class="sum"><i>%s</i><span>$333</span></div>' % (
                _("Low or lower-middle income", "ប្រាក់ចំណូលទាប ឬមធ្យមកម្រិតទាប"), _("Upper-middle or high income", "ប្រាក់ចំណូលមធ្យមកម្រិតខ្ពស់ ឬខ្ពស់")) +
            '<p class="fine">%s</p>' % _("By your card's country and the World Bank's income groups, reread each July; paying by KHQR is Cambodia's fee. Nothing else about you changes the fee.",
                                         "តាមប្រទេសនៃប័ណ្ណរបស់អ្នក និងក្រុមប្រាក់ចំណូលរបស់ធនាគារពិភពលោក អានឡើងវិញរៀងរាល់ខែកក្កដា ការបង់តាម KHQR គឺជាថ្លៃរបស់កម្ពុជា។ គ្មានអ្វីផ្សេងទៀតអំពីអ្នកប្ដូរថ្លៃទេ។"))


def R19():    # the statement
    rows = ((_("Fees received", "ថ្លៃដែលបានទទួល"), "$0,000"), (_("Card processing", "ការដំណើរការប័ណ្ណ"), "−$000"), (_("Hosting", "ការបង្ហោះ"), "−$000"),
            (_("Contract: THonly, the written work", "កិច្ចសញ្ញា៖ THonly ការងារសរសេរ"), "−$000"), (_("Tax", "ពន្ធ"), "−$000"))
    return ('<p class="placeholder">[ PLACEHOLDER FIGURES ]</p>' + head(_("The statement", "របាយការណ៍"), _("July to September, in plain numbers, every quarter.", "ខែកក្កដាដល់កញ្ញា ជាលេខសាមញ្ញ រៀងរាល់ត្រីមាស។")) +
            s_books() + "".join('<div class="sum"><i>%s</i><span>%s</span></div>' % r for r in rows) +
            '<div class="sum tot"><span>%s</span><span>$0,000</span></div>' % _("Profit, held for the Aquarian Pool℠", "ប្រាក់ចំណេញ រក្សាទុកសម្រាប់ Aquarian Pool℠") +
            '<div class="sum"><i>%s</i><span>$0,000</span></div>' % _("In the separate account, all quarters", "នៅក្នុងគណនីដាច់ដោយឡែក គ្រប់ត្រីមាស") +
            '<p class="fine">%s</p>' % _("Nothing here pays the founder. Contracts are at documented fair prices and named here. This page shows no one's fee and no target.",
                                         "គ្មានអ្វីនៅទីនេះបង់ឱ្យស្ថាបនិកទេ។ កិច្ចសញ្ញាមានតម្លៃសមរម្យដែលមានឯកសារ ហើយត្រូវបានដាក់ឈ្មោះនៅទីនេះ។ ទំព័រនេះមិនបង្ហាញថ្លៃរបស់អ្នកណា និងគ្មានគោលដៅទេ។"))


def R20():    # terms and privacy: the skeleton counsel fills
    return ('<p class="placeholder">[ COUNSEL WRITES THE WORDS ]</p>' + head(_("Terms and privacy", "លក្ខខណ្ឌ និងឯកជនភាព")) +
            card(_("Who you're dealing with", "អ្នកកំពុងជួញដូរជាមួយអ្នកណា"), _("[the seller LLC] sells names and tags until the registry's own company exists. Your name moves with it, and you'd be told once.",
                 "[the seller LLC] លក់ឈ្មោះ និងស្លាក រហូតដល់ក្រុមហ៊ុនផ្ទាល់របស់បញ្ជីមាន។ ឈ្មោះរបស់អ្នកផ្លាស់ទីជាមួយវា ហើយអ្នកនឹងត្រូវបានជូនដំណឹងម្ដង។")) +
            card(_("What you get", "អ្វីដែលអ្នកទទួលបាន"), _("A yearly registration of a name, and a page you write. No perks and no membership.", "ការចុះឈ្មោះប្រចាំឆ្នាំ និងទំព័រដែលអ្នកសរសេរ។ គ្មានអត្ថប្រយោជន៍បន្ថែម និងគ្មានសមាជិកភាពទេ។")) +
            card(_("What we keep", "អ្វីដែលយើងរក្សាទុក"), _("Your name, your page, the year it's held through, and your fee group. Your card stays with the card processor. Visits are counted without cookies.",
                 "ឈ្មោះ ទំព័រ ឆ្នាំដែលបានកាន់ និងក្រុមថ្លៃរបស់អ្នក។ ប័ណ្ណរបស់អ្នកនៅជាមួយអ្នកដំណើរការប័ណ្ណ។ រាប់ការចូលមើលដោយគ្មាន cookie។")))


SCREENS = [  # (id, page, title, render)
    ("R1", "registry", "Front door", R1), ("R2", "registry", "Names for you", R2), ("R3", "registry", "Offers, when one just went", R3),
    ("R4", "registry", "The fee, before the card", R4), ("R5", "registry", "The fee, from the card's country", R5), ("R5K", "registry", "Cambodia: KHQR, settled by hand", R5K), ("R6", "registry", "Held", R6),
    ("R7", "registry", "Your page: edit, renew, download", R7), ("R8", "registry", "A person's page: the heart beats on every name", R8),
    ("R8P", "registry", "Why the heart beats (passkey note)", R8P), ("R8T", "registry", "Thank: words first", R8T), ("R8M", "registry", "Money too, only if they'd like", R8M),
    ("R9", "registry", "The one notice before the year ends", R9), ("R10", "registry", "After the year ends: 90 days", R10),
    ("R11", "registry", "A name nobody holds (same page for one that lapsed)", R11), ("R12", "registry", "What a tag is", R12),
    ("R13", "registry", "Brand window: claim a tag", R13), ("R14", "registry", "Tag read and ready: the fee", R14), ("R15", "registry", "A free tag: the steward's form", R15),
    ("R16", "registry", "A company's tag page", R16), ("R17", "registry", "A steward's tag page", R17), ("R18", "registry", "The rules", R18),
    ("R19", "registry", "The statement", R19), ("R20", "registry", "Terms and privacy", R20),
]
DESKTOP = [("R1D", "registry", "Front door, desktop", R1D), ("R8D", "registry", "A person's page, desktop", R8D)]
# A page about a named person gets the preview card and no share button (Default 8); signed-in pages get neither.
PUBLIC = {"R1", "R1D", "R12", "R16", "R17", "R18", "R19"}
# the person-page boards stay without a share button (Default 8)


# ⛔ Refused at build time. Each entry is a thing the founder's rulings bar from this surface's copy.
BARRED = [
    (r"\bdonat", "the fee is an exchange"), (r"\btips?\b", "the fee is an exchange"), (r"\bgift", "the fee is an exchange"),
    (r"\bcharit", "the Pool is not a charity"), (r"\bnon-?profit", "not a nonprofit"), (r"deductible", "not deductible"),
    (r"\bis taken\b|unavailable|not available|already (held|taken)", "never report a name as gone"), (r"\brejected\b|\bdenied\b", "never report a name as gone"),
    (r"\bdeposit|\bsavings\b|\byield\b|\binterest\b|\bcredit\b|\bloan\b", "no regulated word"),
    (r"\bbuy\b|\bbuying\b|\bpurchase", "hold, never buy: a registration, not property"),
    (r"\bdays? left\b|\bhurry\b|\bexpiring\b|\bonly \d+ left\b|\bremaining\b", "state the fact once; never animate the loss"),
    (r"\bsupporters?\b|thank you for support|help the pool|\braised\b", "no ask, no badge, no total"),
    (r"\bnew\b|\bfirst of its kind\b", "no novelty claim"),
    (r"\bverified (holder|badge)\b|\bscore\b|\branked?\b", "class, never endorsement"),
    (r"\bverified\b(?! person)|proven human|real human|a real person", "a passkey shows a key, never a proven human (A562)"),
    (r"\bclub\b|\bmembers?\b", "a holder is not a member"),
    (r"ធនាគារ(?!ពិភពលោក|របស់អ្នក)", "ធនាគារ is the regulated word; only the World Bank's name or a person's own bank"),
]


def check(sid, html):
    """Raise if a board's visible words break a ruling. Markup is stripped first, so a class or path can't trip it."""
    text = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    for pat, why in BARRED:
        m = re.search(pat, text, re.I)
        assert not m, "%s: %r is barred: %s" % (sid, m.group(0), why)
    return text
