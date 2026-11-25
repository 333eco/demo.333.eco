"""legal.333.eco and the explorer's Legal tab (A709; the spec is private, legal.333.eco SPEC.md; founder 2026-11-24/25).
Imported by build-boards.py, which injects the shared helpers.

Copy rules this file must keep (checked at build time by check()):
  - Nothing here is signed: a legal version is TIMESTAMPED (OpenTimestamps + three timestamp authorities), never signed at
    B-Origin (ruled 2026-11-25). No "verified", "certified", "notary", and never "the estate".
  - A timestamp is always said with its limit: it shows the text existed by then, never who published it or that it was in force.
    "Existed by" and "Served from" are two separate facts, never one line.
  - The footer claims only what the built bytes prove: no analytics script, no cookies. Never "no visits are counted".
  - The founder line on this host is the founder's own wording: "Thon Ly is the Founder of this institution · Miss Aquarius℠ is
    the CEO of HeartBank®". Miss Aquarius is never named as a party to a document.
  - The 333.eco heading is "333.eco · shared services" (Khmer សេវារួម), never Factory 333™ and never "every institution" (ស្ថាប័ន is the
    INSTITUTION, never a body; no Khmer word for "body" is coined here).
  - The legal text stays English on the Khmer boards (ruled 2026-11-25); only the page around it is Khmer.
  - Words copied from live pages stay word for word: the ledger's terms (ledger.333.eco legal/terms.md, Draft of 9 November 2026),
    earth's own draft banner (live at earth.333.eco/terms, 2026-11-25), the explorer's proof wording (explorer.333.eco client/app.ts).
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board. Dates after 25 Nov 2026 are drawn, not real.
"""
import re

card = btns = spot = heart = person = None   # injected by build-boards.py

FP = "ab4e2ecb4d"   # the first 10 hex of the ledger terms' real sha256 at origin/main, 2026-11-25
FULL = "ab4e2ecb4d6f…"  # drawn: the rest of the 64 characters is elided on the board

DT = {
"en": {
  "prod": "Legal", "foot": "legal.333.eco · no analytics script, no cookies",
  "who": "Thon Ly is the Founder of this institution · Miss Aquarius℠ is the CEO of HeartBank®",
  "nobank": "HeartBank® is a data bank of gratitude. It is not a chartered bank or financial institution; it does not provide banking services, hold deposits, or extend credit. Nothing is paid or held on this site.",
  "t1_h": "Legal documents", "t1_lede": "The terms and privacy policy of each service, on one site. When a document is final, its page names who runs the service. Every version keeps its own address, and every version is timestamped.",
  "h3": "HeartBank®", "shared": "333.eco · shared services", "all": "For every service",
  "earth": "earth.333.eco", "earth_p": "The gratitude ledger: a private record of thanks, with public proofs.",
  "dev": "developers.333.eco", "dev_p": "Every HeartBank® API, its docs and its sandbox.",
  "terms": "Terms of service", "privacy": "Privacy policy", "draft9": "Draft of 9 November 2026", "draft16": "Draft of 16 November 2026", "draft18": "Draft of 18 November 2026",
  "check": "Check any version on explorer.333.eco. The check runs in your browser.",
  "ahead": "Drawn ahead: each service joins when its pages move here.",
  "th": "THonly™", "sw": "Silicon Wat℠", "f3": "Factory 333™", "ma": "Miss Aquarius℠",
  "storage": "storage.333.eco", "storage_p": "One place for the files you keep through a HeartBank® app.",
  "names": "333.eco", "names_p": "Hold an @name or a #tag.",
  "billing": "billing.thonly.com", "billing_p": "One prepaid balance.",
  "ocr": "ocr.siliconwat.dev", "ocr_p": "The Khmer Tipiṭaka, typed.",
  "sey": "sayyourname.app", "sey_p": "Say a name the way its owner says it.",
  "mao": "missaquarius.org", "mao_p": "Miss Aquarius's own site.",
  "refunds": "Refunds and cancellation", "copyright": "Copyright and takedown",
  "aup": "Acceptable use", "sec": "Security", "ops": "Who runs each service", "tm": "Using our marks",
  "crumb": "HeartBank® › earth.333.eco",
  "banner": "This is a draft. No lawyer has reviewed it, and it may change before it is final. Where something is not settled yet, it says so.",
  "with": "Drafted with", "withv": "Miss Aquarius℠, an AI",
  "by": "Operated by", "byv": "Named in the final version",
  "this": "This version", "thisv": "Draft of 9 November 2026",
  "addr": "Its address",
  "versions": "Versions", "cur": "current",
  "earlier": "Earlier drafts were served at earth.333.eco itself, and may be on the Internet Archive.",
  "chk": "Check this version",
  "existed": "Existed by", "existed_p": "27 Nov 2026, timestamped to Bitcoin and by three timestamp authorities. A timestamp shows the text existed by then. It does not show who published it, or that it was in force.",
  "served": "Served from", "served_p": "legal.333.eco since 27 Nov 2026. The Internet Archive and Software Heritage keep their own copies.",
  "english": "",
  "t3_h": "Terms of service", "t3_sub": "Draft of 9 November 2026, for earth.333.eco",
  "t3_p": "This address always shows this exact text. A later version gets an address of its own.",
  "fp": "Its fingerprint", "fp_p": "SHA-256 of the text, byte for byte.",
  "dl": "Download the text (.md)", "dlo": "Download its proof (.ots)", "curv": "The current version",
  "keep": "Keep a copy: the text and its proof are all anyone needs to check it, with no help from us.",
  "rev": "Reviewed", "revv": "By a lawyer, 12 January 2027", "revrec": "its record",
  "named": "[ the operator, as the final text names it ]", "ver27": "Version of 12 January 2027",
  "t4_text": "These terms are between you and [ the operator ], which operates earth.333.eco. By opening your record here, you agree to them.",
  "t5_h": "Acceptable use", "t5_scope": "For every service listed on this site. Each service's terms point here.", "t5_ph": "[ COUNSEL WRITES THE WORDS ]",
  "t5_p": "What is not allowed on any service: what you may not post, send or do to other people. Drafted, then reviewed, like every document here.",
  "older": "This is an earlier version.", "older_cur": "The current version is the Version of 12 January 2027.",
  "side": ("Legal documents", "earth.333.eco", "developers.333.eco", "For every service"),
  # explorer.333.eco, the Legal tab (live wording from client/app.ts where it exists)
  "e_legal": "Legal",
  "e8_h": "Legal documents", "e8_lede": "Every version of each service's legal documents, read from the public repository 333eco/legal-versions. Every check runs in your browser.",
  "tick": "A tick means it was checked on this page just now. No tick means it's stated, with where to check it.",
  "tsa": "3 timestamp authorities", "btc": "Bitcoin", "pend": "Waiting for a block. This takes a few hours.",
  "e9_h": "Terms of service · earth.333.eco", "e9_sub": "Draft of 9 November 2026",
  "e_fp": "Its fingerprint", "e_fp_p": "The repository's text has this fingerprint, hashed here just now.",
  "e_proof": "The proof", "e_proof_p": "The proof leads from this text to this block, whose header was read from mempool.space just now. Mined 27 Nov 2026.",
  "e_tsa": "Timestamp authorities", "e_tsa_p": "In the 27 Nov 2026 manifest, with tokens from three authorities, one of them eIDAS-qualified.",
  "e_limit": "What this shows: the text existed by 27 Nov 2026. It does not show who published it, or that it was in force.",
  "e_served": "Served from", "e_served_p": "legal.333.eco · a copy at the Internet Archive, 27 Nov 2026 · Software Heritage keeps the repository.",
  "e_page": "Open its page on legal.333.eco",
  "e_rev": "The review record", "e_rev_p": "Entered 12 Jan 2027, when a lawyer reviewed this version, and timestamped in that day's manifest. It records that the review happened. It does not show what the lawyer advised.",
},
"km": {
  "prod": "ច្បាប់", "foot": "legal.333.eco · គ្មានស្គ្រីបវិភាគ គ្មានខូគី",
  "who": "Thon Ly ជាស្ថាបនិកនៃស្ថាប័ននេះ · Miss Aquarius℠ ជាប្រធានប្រតិបត្តិនៃ HeartBank®",
  "nobank": "HeartBank® គឺជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ វាមិនមែនជាធនាគារដែលមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ វាមិនផ្តល់សេវាធនាគារ មិនទទួលប្រាក់បញ្ញើ ឬផ្តល់ឥណទានទេ។ គ្មានអ្វីត្រូវបានបង់ ឬរក្សាទុកនៅលើគេហទំព័រនេះទេ។",
  "t1_h": "ឯកសារច្បាប់", "t1_lede": "លក្ខខណ្ឌ និងគោលការណ៍ឯកជនភាពនៃសេវានីមួយៗ នៅលើគេហទំព័រតែមួយ។ នៅពេលឯកសារមួយជាកំណែចុងក្រោយ ទំព័ររបស់វាដាក់ឈ្មោះអ្នកដំណើរការសេវានោះ។ កំណែនីមួយៗមានអាសយដ្ឋានផ្ទាល់ខ្លួន ហើយកំណែនីមួយៗត្រូវបានបោះត្រាពេលវេលា។",
  "h3": "HeartBank®", "shared": "333.eco · សេវារួម", "all": "សម្រាប់គ្រប់សេវា",
  "earth": "earth.333.eco", "earth_p": "បញ្ជីនៃការដឹងគុណ៖ កំណត់ត្រាឯកជននៃការអរគុណ ជាមួយភស្តុតាងសាធារណៈ។",
  "dev": "developers.333.eco", "dev_p": "គ្រប់ API របស់ HeartBank® ឯកសាររបស់វា និង sandbox របស់វា។",
  "terms": "Terms of service", "privacy": "Privacy policy", "draft9": "Draft of 9 November 2026", "draft16": "Draft of 16 November 2026", "draft18": "Draft of 18 November 2026",
  "check": "ពិនិត្យកំណែណាមួយនៅលើ explorer.333.eco។ ការពិនិត្យដំណើរការក្នុងកម្មវិធីរុករករបស់អ្នក។",
  "ahead": "គូរទុកជាមុន៖ សេវានីមួយៗចូលរួម នៅពេលទំព័ររបស់វាផ្លាស់មកទីនេះ។",
  "th": "THonly™", "sw": "Silicon Wat℠", "f3": "Factory 333™", "ma": "Miss Aquarius℠",
  "storage": "storage.333.eco", "storage_p": "កន្លែងតែមួយសម្រាប់ឯកសារដែលអ្នករក្សាទុកតាមរយៈកម្មវិធី HeartBank®។",
  "names": "333.eco", "names_p": "កាន់ @name ឬ #tag។",
  "billing": "billing.thonly.com", "billing_p": "សមតុល្យបង់មុនតែមួយ។",
  "ocr": "ocr.siliconwat.dev", "ocr_p": "ព្រះត្រៃបិដកខ្មែរ វាយជាអក្សរ។",
  "sey": "sayyourname.app", "sey_p": "និយាយឈ្មោះតាមរបៀបដែលម្ចាស់ឈ្មោះនិយាយ។",
  "mao": "missaquarius.org", "mao_p": "គេហទំព័រផ្ទាល់ខ្លួនរបស់ Miss Aquarius។",
  "refunds": "Refunds and cancellation", "copyright": "Copyright and takedown",
  "aup": "Acceptable use", "sec": "Security", "ops": "Who runs each service", "tm": "Using our marks",
  "crumb": "HeartBank® › earth.333.eco",
  "banner": "នេះជាសេចក្តីព្រាង។ មិនទាន់មានមេធាវីណាពិនិត្យវានៅឡើយទេ ហើយវាអាចផ្លាស់ប្តូរ មុនពេលវាជាកំណែចុងក្រោយ។ អត្ថបទច្បាប់មានតែជាភាសាអង់គ្លេសប៉ុណ្ណោះ។",
  "with": "រៀបចំជាមួយ", "withv": "Miss Aquarius℠ ដែលជា AI",
  "by": "ដំណើរការដោយ", "byv": "នឹងដាក់ឈ្មោះនៅក្នុងកំណែចុងក្រោយ",
  "this": "កំណែនេះ", "thisv": "Draft of 9 November 2026",
  "addr": "អាសយដ្ឋានរបស់វា",
  "versions": "កំណែ", "cur": "បច្ចុប្បន្ន",
  "earlier": "សេចក្តីព្រាងមុនៗត្រូវបានបង្ហាញនៅ earth.333.eco ផ្ទាល់ ហើយប្រហែលជាមាននៅ Internet Archive។",
  "chk": "ពិនិត្យកំណែនេះ",
  "existed": "មានរួចហើយនៅ", "existed_p": "២៧ វិច្ឆិកា ២០២៦ បោះត្រាពេលវេលាទៅ Bitcoin និងដោយអាជ្ញាធរបោះត្រាពេលវេលាបី។ ត្រាពេលវេលាបង្ហាញថាអត្ថបទមានរួចហើយនៅពេលនោះ។ វាមិនបង្ហាញថាអ្នកណាជាអ្នកផ្សព្វផ្សាយ ឬថាវាមានសុពលភាពនោះទេ។",
  "served": "បង្ហាញពី", "served_p": "legal.333.eco តាំងពី ២៧ វិច្ឆិកា ២០២៦។ Internet Archive និង Software Heritage រក្សាច្បាប់ចម្លងផ្ទាល់ខ្លួន។",
  "english": "អត្ថបទច្បាប់នៅជាភាសាអង់គ្លេស រហូតដល់កំណែភាសាខ្មែរត្រូវបានពិនិត្យ។",
  "t3_h": "Terms of service", "t3_sub": "Draft of 9 November 2026 សម្រាប់ earth.333.eco",
  "t3_p": "អាសយដ្ឋាននេះបង្ហាញអត្ថបទដដែលនេះជានិច្ច។ កំណែក្រោយៗមានអាសយដ្ឋានផ្ទាល់ខ្លួន។",
  "fp": "ស្នាមម្រាមដៃរបស់វា", "fp_p": "SHA-256 នៃអត្ថបទ គ្រប់បៃ។",
  "dl": "ទាញយកអត្ថបទ (.md)", "dlo": "ទាញយកភស្តុតាងរបស់វា (.ots)", "curv": "កំណែបច្ចុប្បន្ន",
  "keep": "រក្សាច្បាប់ចម្លងមួយ៖ អត្ថបទ និងភស្តុតាងរបស់វា គឺជាអ្វីដែលអ្នកណាក៏ត្រូវការ ដើម្បីពិនិត្យវា ដោយមិនចាំបាច់មានជំនួយពីយើង។",
  "rev": "បានពិនិត្យ", "revv": "ដោយមេធាវី ១២ មករា ២០២៧", "revrec": "កំណត់ត្រារបស់វា",
  "named": "[ the operator, as the final text names it ]", "ver27": "Version of 12 January 2027",
  "t4_text": "These terms are between you and [ the operator ], which operates earth.333.eco. By opening your record here, you agree to them.",
  "t5_h": "Acceptable use", "t5_scope": "សម្រាប់គ្រប់សេវាដែលមាននៅលើគេហទំព័រនេះ។ លក្ខខណ្ឌនៃសេវានីមួយៗចង្អុលមកទីនេះ។", "t5_ph": "[ COUNSEL WRITES THE WORDS ]",
  "t5_p": "អ្វីដែលមិនត្រូវបានអនុញ្ញាតនៅលើសេវាណាមួយ៖ អ្វីដែលអ្នកមិនអាចបង្ហោះ ផ្ញើ ឬធ្វើចំពោះអ្នកដទៃ។ រៀបចំជាសេចក្តីព្រាង រួចពិនិត្យ ដូចឯកសារទាំងអស់នៅទីនេះ។",
  "older": "នេះជាកំណែមុន។", "older_cur": "កំណែបច្ចុប្បន្នគឺ Version of 12 January 2027។",
  "side": ("ឯកសារច្បាប់", "earth.333.eco", "developers.333.eco", "សម្រាប់គ្រប់សេវា"),
  "e_legal": "ច្បាប់",
  "e8_h": "ឯកសារច្បាប់", "e8_lede": "គ្រប់កំណែនៃឯកសារច្បាប់របស់សេវានីមួយៗ អានពីឃ្លាំងសាធារណៈ 333eco/legal-versions។ ការពិនិត្យទាំងអស់ដំណើរការក្នុងកម្មវិធីរុករករបស់អ្នក។",
  "tick": "សញ្ញាធីកមានន័យថាវាត្រូវបានពិនិត្យនៅលើទំព័រនេះមុននេះបន្តិច។ គ្មានសញ្ញាធីកមានន័យថាវាត្រូវបានប្រាប់ ជាមួយកន្លែងដែលត្រូវពិនិត្យ។",
  "tsa": "អាជ្ញាធរបោះត្រាពេលវេលា ៣", "btc": "Bitcoin", "pend": "កំពុងរង់ចាំប្លុក។ វាចំណាយពេលពីរបីម៉ោង។",
  "e9_h": "Terms of service · earth.333.eco", "e9_sub": "Draft of 9 November 2026",
  "e_fp": "ស្នាមម្រាមដៃរបស់វា", "e_fp_p": "អត្ថបទរបស់ឃ្លាំងមានស្នាមម្រាមដៃនេះ ដែលបានហាសនៅទីនេះមុននេះបន្តិច។",
  "e_proof": "ភស្តុតាង", "e_proof_p": "ភស្តុតាងនាំពីអត្ថបទនេះទៅកាន់ប្លុកនេះ ដែលក្បាលរបស់វាត្រូវបានអានពី mempool.space មុននេះបន្តិច។ បានជីកនៅ ២៧ វិច្ឆិកា ២០២៦។",
  "e_tsa": "អាជ្ញាធរបោះត្រាពេលវេលា", "e_tsa_p": "នៅក្នុងបញ្ជី ២៧ វិច្ឆិកា ២០២៦ ជាមួយសញ្ញាសម្គាល់ពីអាជ្ញាធរបី ដែលមួយក្នុងចំណោមនោះមានលក្ខណៈសម្បត្តិ eIDAS។",
  "e_limit": "អ្វីដែលនេះបង្ហាញ៖ អត្ថបទមានរួចហើយនៅ ២៧ វិច្ឆិកា ២០២៦។ វាមិនបង្ហាញថាអ្នកណាជាអ្នកផ្សព្វផ្សាយ ឬថាវាមានសុពលភាពនោះទេ។",
  "e_served": "បង្ហាញពី", "e_served_p": "legal.333.eco · ច្បាប់ចម្លងមួយនៅ Internet Archive ២៧ វិច្ឆិកា ២០២៦ · Software Heritage រក្សាឃ្លាំងនេះ។",
  "e_page": "បើកទំព័ររបស់វានៅលើ legal.333.eco",
  "e_rev": "កំណត់ត្រានៃការពិនិត្យ", "e_rev_p": "បានបញ្ចូលនៅ ១២ មករា ២០២៧ នៅពេលមេធាវីពិនិត្យកំណែនេះ ហើយបោះត្រាពេលវេលានៅក្នុងបញ្ជីថ្ងៃនោះ។ វាកត់ត្រាថាការពិនិត្យបានកើតឡើង។ វាមិនបង្ហាញថាមេធាវីបានផ្តល់យោបល់អ្វីនោះទេ។",
},
}

# The ledger's terms, word for word (ledger.333.eco legal/terms.md at origin/main, 2026-11-25): the opening and two sections.
TEXT = """<h2 class="lgdoch">Terms of service</h2><p class="lgdate">Draft of 9 November 2026.</p>
<p>These terms are between you and the organization that operates earth.333.eco, which will be named in the final version. By opening your record here, you agree to them.</p>
<h3 id="what-this-service-is">What this service is</h3>
<p>This service keeps a private record of thanks given on HeartBank® apps and timestamps a fingerprint of each to a public ledger. You can open and download your own record.</p>
<p>HeartBank® is a planetary data bank of gratitude. It is not a chartered bank or financial institution; it does not provide banking services, hold deposits, or extend credit. Nothing is paid here: this service keeps a record of thanks and moves no money. Financial services are not provided by HeartBank.</p>
<h3 id="kiitos-and-kiitti">Kiitos and Kiitti</h3>
<p>Kiitos is a thank between two people. Kiitti is care for a thing, a plant or an animal.</p>
<ul><li><b>They have no cash value.</b> They cannot be bought, sold, traded, transferred, redeemed or exchanged for money, goods or time.</li>
<li><b>They are a record, not property.</b> You have no ownership claim on a balance or a color.</li></ul>
<p class="lgmore">…</p>"""

CHEV = '<span class="lgchev" aria-hidden="true">›</span>'


def _doclinks(d, rows):
    return "".join('<div class="row lgrow"><div><div class="t">%s</div><div class="s">%s</div></div>%s</div>' % (a, b, CHEV) for a, b in rows)


def _svc(d, host, p, rows):
    return '<div class="lgsvc"><div class="lghost mono">%s</div><p class="s">%s</p>%s</div>' % (d[host], d[p], _doclinks(d, rows))


def _sec(title, inner):
    return '<section class="lgsec"><h2 class="lgh">%s</h2><div class="card lgcard">%s</div></section>' % (title, inner)


def _tail(d):
    return '<p class="fine lgfine">%s</p><p class="fine lgfine">%s</p>' % (d["nobank"], d["who"])


def T1(t, d):
    h3 = _sec(d["h3"], _svc(d, "earth", "earth_p", ((d["terms"], d["draft9"]), (d["privacy"], d["draft9"]))))
    sh = _sec(d["shared"], _svc(d, "dev", "dev_p", ((d["terms"], d["draft16"]), (d["privacy"], d["draft18"]))))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["t1_h"], d["t1_lede"]) + h3 + sh
            + '<p class="fine">%s</p>' % d["check"] + '<div class="grow"></div>' + _tail(d))


def T1b(t, d):
    def one(host, p, docs):
        return _svc(d, host, p, [(d[x], "") for x in docs])
    secs = (_sec(d["h3"], one("earth", "earth_p", ("terms", "privacy")))
            + _sec(d["th"], one("billing", "billing_p", ("terms", "privacy", "refunds")))
            + _sec(d["sw"], one("ocr", "ocr_p", ("terms", "privacy")))
            + _sec(d["f3"], one("sey", "sey_p", ("terms", "privacy")))
            + _sec(d["ma"], one("mao", "mao_p", ("privacy",)))
            + _sec(d["shared"], one("dev", "dev_p", ("terms", "privacy")) + one("storage", "storage_p", ("terms", "privacy", "copyright"))
                   + one("names", "names_p", ("terms", "privacy", "refunds")))
            + _sec(d["all"], _doclinks(d, ((d["aup"], ""), (d["sec"], ""), (d["ops"], ""), (d["tm"], "")))))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["t1_h"], d["ahead"]) + secs + _tail(d))


def _meta(d):
    rows = ((d["with"], d["withv"]), (d["by"], d["byv"]), (d["this"], '%s · <span class="mono">%s</span>' % (d["thisv"], FP[:6])),
            (d["addr"], '<span class="mono lgaddr">legal.333.eco/earth.333.eco/terms/2026-11-09-%s</span>' % FP[:6]))
    return '<div class="card">%s</div>' % "".join('<div class="kf"><div class="kl">%s</div><div>%s</div></div>' % r for r in rows)


def _facts(d):
    return ('<div class="lgfacts"><div class="card"><h2>%s</h2><p>%s</p></div><div class="card"><h2>%s</h2><p>%s</p></div></div>'
            % (d["existed"], d["existed_p"], d["served"], d["served_p"]))


def T2(t, d):
    eng = '<p class="fine lgeng">%s</p>' % d["english"] if d["english"] else ""
    vers = ('<div class="card"><h2>%s</h2><div class="row lgrow"><div><div class="t">%s <span class="pill on">%s</span></div><div class="s mono">%s</div></div>%s</div><p class="fine">%s</p></div>'
            % (d["versions"], d["draft9"], d["cur"], "2026-11-09-" + FP[:6], CHEV, d["earlier"]))
    return ('<div class="s lgcrumb">%s</div><div class="lgbanner">%s</div>' % (d["crumb"], d["banner"]) + _meta(d) + eng
            + '<article class="card lgdoc" lang="en">%s</article>' % TEXT + vers
            + '<span class="pillbtn">%s</span>' % d["chk"] + _facts(d) + _tail(d))


def T3(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["t3_h"], d["t3_sub"]) + '<div class="lgbanner">%s</div>' % d["banner"]
            + '<div class="card"><div class="mono lgaddr">legal.333.eco/earth.333.eco/terms/2026-11-09-%s</div><p>%s</p></div>' % (FP[:6], d["t3_p"])
            + '<div class="card"><h2>%s</h2><div class="mono lgaddr">%s</div><p class="s">%s</p></div>' % (d["fp"], FULL, d["fp_p"])
            + '<div class="lgbtns"><span class="pillbtn">%s</span><span class="pillbtn ghost">%s</span></div><p class="fine">%s</p>' % (d["dl"], d["dlo"], d["keep"])
            + '<span class="pillbtn ghost">%s</span>' % d["chk"] + _facts(d) + '<p class="fine"><span class="link">%s</span></p>' % d["curv"] + _tail(d))


def _etabs(t, d):
    tabs = list(t["e_tabs"]) + [d["e_legal"]]
    return '<div class="tabs">%s</div>' % "".join('<span%s>%s</span>' % (' class="on"' if i == 3 else "", x) for i, x in enumerate(tabs))


def _chips(d, done):
    return '<div class="chips" style="margin-top:6px"><span class="pill on">✓ %s</span>%s</div>' % (
        d["tsa"], '<span class="pill on">⛓ %s</span>' % d["btc"] if done else '<span class="pill">%s</span>' % d["pend"])


def E8(t, d):
    def doc(name, date, fp, done):
        return ('<div class="row lgrow"><div><div class="t">%s</div><div class="s">%s · <span class="mono">%s</span></div>%s</div>%s</div>'
                % (name, date, fp, _chips(d, done), CHEV))
    return (_etabs(t, d) + "<h1>%s</h1><p class='lede'>%s</p>" % (d["e8_h"], d["e8_lede"])
            + '<div class="card"><h2 class="mono">%s</h2>%s%s</div>' % (d["earth"], doc(d["terms"], d["draft9"], FP[:6], True), doc(d["privacy"], d["draft9"], "5d3547", True))
            + '<div class="card"><h2 class="mono">%s</h2>%s%s</div>' % (d["dev"], doc(d["terms"], d["draft16"], "b27c81", True), doc(d["privacy"], d["draft18"], "55df81", False))
            + '<p class="fine">%s</p>' % d["tick"])


def E9(t, d):
    def leg(h, p, ok=True):
        return '<div class="row" style="display:block"><div class="t"><span style="color:var(--accent)">%s</span> %s</div><div class="s">%s</div></div>' % ("✓" if ok else "", h, p)
    return (_etabs(t, d) + "<h1>%s</h1><p class='lede'>%s</p>" % (d["e9_h"], d["e9_sub"])
            + '<div class="card">%s<div class="mono lgaddr" style="margin:-4px 0 8px 22px">%s</div>%s%s</div>' % (leg(d["e_fp"], d["e_fp_p"]), FULL, leg(d["e_proof"], d["e_proof_p"]), leg(d["e_tsa"], d["e_tsa_p"]))
            + '<div class="lgbanner lglimit">%s</div>' % d["e_limit"]
            + '<div class="card"><h2>%s</h2><p>%s</p></div>' % (d["e_served"], d["e_served_p"])
            + '<p class="fine">%s</p><span class="pillbtn ghost">%s</span>' % (d["tick"], d["e_page"]))


def T4(t, d):
    """The state after counsel's sign-off (ruled 2026-11-25): a dated review record removes the banner. Drawn ahead; dates drawn."""
    rows = ((d["rev"], '%s · <span class="link">%s</span>' % (d["revv"], d["revrec"])), (d["with"], d["withv"]), (d["by"], d["named"]),
            (d["this"], '%s · <span class="mono">7c19d0</span>' % d["ver27"]))
    meta = '<div class="card">%s</div>' % "".join('<div class="kf"><div class="kl">%s</div><div>%s</div></div>' % r for r in rows)
    eng = '<p class="fine lgeng">%s</p>' % d["english"] if d["english"] else ""
    text = ('<h2 class="lgdoch">Terms of service</h2><p class="lgdate">Version of 12 January 2027.</p><p>%s</p><p class="lgmore">…</p>' % d["t4_text"])
    vers = ('<div class="card"><h2>%s</h2><div class="row lgrow"><div><div class="t">%s <span class="pill on">%s</span></div><div class="s mono">2027-01-12-7c19d0</div></div>%s</div>'
            '<div class="row lgrow"><div><div class="t">%s</div><div class="s mono">2026-11-09-%s</div></div>%s</div></div>'
            % (d["versions"], d["ver27"], d["cur"], CHEV, d["draft9"], FP[:6], CHEV))
    return ('<div class="s lgcrumb">%s</div>' % d["crumb"] + meta + eng + '<article class="card lgdoc" lang="en">%s</article>' % text + vers
            + '<span class="pillbtn">%s</span>' % d["chk"] + _tail(d))


def T5(t, d):
    """A document shared by every service (acceptable use): placeholder words until counsel writes them."""
    return ('<div class="s lgcrumb">%s</div><h1>%s</h1><p class="lede">%s</p>' % (d["all"], d["t5_h"], d["t5_scope"])
            + '<div class="lgbanner">%s</div>' % d["banner"]
            + '<article class="card lgdoc"><p class="placeholder lgph">%s</p><p>%s</p></article>' % (d["t5_ph"], d["t5_p"]) + _tail(d))


def T6(t, d):
    """An earlier version once a newer one exists: the fact stated once, no countdown, no alarm."""
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["t3_h"], d["t3_sub"])
            + '<div class="card"><p><b>%s</b> %s</p><span class="pillbtn">%s</span></div>' % (d["older"], d["older_cur"], d["curv"])
            + '<div class="lgbanner">%s</div>' % d["banner"]
            + '<div class="card"><div class="mono lgaddr">legal.333.eco/earth.333.eco/terms/2026-11-09-%s</div><p>%s</p></div>' % (FP[:6], d["t3_p"])
            + '<div class="lgbtns"><span class="pillbtn ghost">%s</span><span class="pillbtn ghost">%s</span></div>' % (d["dl"], d["dlo"])
            + _facts(d) + _tail(d))


def T2D(t, d):
    """The document page at 1280: the documents down the left (Default 20's left panel), the text given room (Stripe Docs)."""
    nav = "".join('<a class="%s">%s</a>' % ("on" if i == 1 else "", x) for i, x in enumerate(d["side"]))
    main = T2(t, d)
    return '<div class="side lgside"><nav class="nav">%s</nav><div class="lgmain">%s</div></div>' % (nav, main)


def E10(t, d):
    """The Legal tab for a reviewed version: the review record is a fact with its own limit."""
    def leg(h, p):
        return '<div class="row" style="display:block"><div class="t"><span style="color:var(--accent)">✓</span> %s</div><div class="s">%s</div></div>' % (h, p)
    return (_etabs(t, d) + "<h1>%s</h1><p class='lede'>%s</p>" % (d["e9_h"], d["ver27"])
            + '<div class="card">%s%s%s%s</div>' % (leg(d["e_fp"], d["e_fp_p"]), leg(d["e_proof"], d["e_proof_p"].replace("27 Nov 2026", "12 Jan 2027")),
                                                  leg(d["e_tsa"], d["e_tsa_p"].replace("27 Nov 2026", "12 Jan 2027")), leg(d["e_rev"], d["e_rev_p"]))
            + '<div class="lgbanner lglimit">%s</div>' % d["e_limit"].replace("27 Nov 2026", "12 Jan 2027")
            + '<p class="fine">%s</p>' % d["tick"])


SCREENS = [
    ("T1", "legal", "legal.333.eco: the documents, under the body that runs each service (at M1: two services)", T1),
    ("T1b", "legal", "legal.333.eco: drawn ahead, every body and the shared documents", T1b),
    ("T2", "legal", "A document: the earth.333.eco terms (current, a draft)", T2),
    ("T3", "legal", "One version at its own address, with its fingerprint and proof", T3),
    ("E8", "explorer", "The explorer's Legal tab: every version, checked", E8),
    ("E9", "explorer", "One legal version checked in your browser", E9),
    ("T4", "legal", "Drawn ahead: a version after counsel's review (the record replaces the banner)", T4),
    ("T5", "legal", "A document shared by every service: acceptable use (words: counsel)", T5),
    ("T6", "legal", "An earlier version, once a newer one exists", T6),
    ("E10", "explorer", "The Legal tab: a reviewed version, with its review record", E10),
]
DESKTOP = [("T2D", "legal", "A document page, desktop", T2D)]
PUBLIC = {"T1", "T1b", "T2", "T3", "T4", "T5", "T6", "T2D", "E8", "E9", "E10"}
CSS = """
.lgsec{margin:18px 0 0}
.lgh{font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-dim);margin:0 0 8px}
.lgcard{padding-top:6px;padding-bottom:6px}
.lgsvc+.lgsvc{border-top:1px solid var(--line);margin-top:10px;padding-top:10px}
.lghost{font-size:15px;font-weight:600;margin-top:6px}
.lgsvc .s{margin:2px 0 4px}
.lgrow{display:flex;align-items:center;justify-content:space-between;gap:10px}
.lgchev{color:var(--ink-faint);font-size:20px;line-height:1}
.lgfine{margin-top:10px}
.lgcrumb{margin:4px 0 10px}
.lgbanner{background:var(--wash);border:1px solid var(--edge);border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.5;margin:0 0 12px}
.lglimit{margin-top:12px}
.lgaddr{font-size:12.5px;word-break:break-all}
.lgdoc{font-size:15px;line-height:1.6}
.lgdoc .lgdoch{font-size:20px;margin:0 0 2px}
.lgdoc .lgdate{color:var(--ink-dim);margin:0 0 10px}
.lgdoc h3{font-size:16px;margin:16px 0 4px}
.lgdoc ul{padding-left:20px;margin:6px 0}
.lgdoc li{margin:4px 0}
.lgmore{color:var(--ink-faint)}
.lgeng{margin:-4px 0 10px}
.lgfacts{display:grid;gap:10px;margin-top:12px}
.lgbtns{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 4px}
.lgbtns .pillbtn{margin:0}
.lgph{font-family:var(--font-mono);color:var(--ink-dim);letter-spacing:.04em}
.lgside{gap:40px}
.lgmain{max-width:760px}
"""
BARRED = [
    (r"\bverif(?:y|ied|ies)\b|\bcertif(?:y|ied)\b|notar", "a timestamp shows existence, never a verification or a notary"),
    (r"\bthe estate\b", "never 'the estate' in or around a legal document"),
    (r"\bsign[\s-]?in\b", "Log in authenticates; 'sign in' is barred (Default 10)"),
    (r"\bB-Origin\b|signed by (?:us|the founder|Thon)|\bwe sign", "legal versions are timestamped, never signed at B-Origin (2026-11-25)"),
    (r"visits are (?:not )?counted|counts nothing", "claim only what the built bytes prove: no analytics script, no cookies"),
    (r"Factory 333™?\s*·\s*shared|shared by every body.*Factory", "the 333.eco heading is never Factory 333"),
    (r"គ្រប់ស្ថាប័ន|every institution", "ស្ថាប័ន is the INSTITUTION; the members are never 'every institution'"),
]


def check(sid, body):
    plain = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
    for pat, why in BARRED:
        assert not re.search(pat, plain, re.I), "%s: %s" % (sid, why)
    if "Miss Aquarius" in plain and sid.startswith("T"):
        assert re.search(r"CEO of HeartBank|ប្រធានប្រតិបត្តិនៃ HeartBank", plain), "%s: on this host she is the CEO of HeartBank®, never unqualified" % sid
    if sid in ("T2", "T2D", "T3", "T6", "E9", "E10"):
        assert re.search(r"does not show who published it|មិនបង្ហាញថាអ្នកណាជាអ្នកផ្សព្វផ្សាយ", plain), "%s: a timestamp always carries its limit" % sid
    if sid in ("T2", "T2D", "T3", "T6"):
        assert plain.count('class="card"><h2>') >= 2 and "lgfacts" in plain, "%s: existed-by and served-from are two facts" % sid
    if sid == "T4":
        assert "lgbanner" not in plain and re.search(r"Reviewed|បានពិនិត្យ", plain), "T4: a reviewed version shows its review record and no draft banner"
    if sid == "E10":
        assert re.search(r"does not show what the lawyer advised|មិនបង្ហាញថាមេធាវីបានផ្តល់យោបល់", plain), "E10: the review record carries its limit"
    if sid in ("T2", "T2D", "T3", "T5", "T6"):
        assert "lgbanner" in plain, "%s: a draft keeps its banner until a review record exists" % sid
    if sid == "T2":
        assert 'lang="en"' in plain and "These terms are between you" in plain, "T2: the legal text is English, word for word, on every board"
