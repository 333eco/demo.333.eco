"""B-Mail thanks (A607, phase 3): the thank back on the check page, the sender's thank on Sign a mail, keep or give the files
through B-Origin, and 333.eco's Thank opened from a B-Mail. The spec is private (333.eco SPEC.md, "B-Mail thanks, phase 3";
founder 2026-11-25). Imported by build-boards.py, which injects the shared helpers.

Boards (prefix C; the spec's own names in brackets): CS1 [S1] Sign a mail with *Their @name* · CS2 [S2] the result card after the
press, with files · C1 [C1] the check page with the thank line · C1b the same page when the name is not confirmed (no thank line)
· CT1 [T1] 333.eco's Thank opened from a B-Mail. One dark pass: CS2.

These four screens extend LIVE pages, so their words are COPIED from the live code (Default 18), each key cited below; only the
spec's new words are ours. Copy rules this file must keep (checked at build time by check(), on the words AND the footer):
  - The thank is offered, never pre-selected or pre-filled: it is never the page's primary button, and the Thank opens with its
    words field empty (only the placeholder) and Send not yet pressable.
  - CT1 never offers *Without my name* (on this path it would hide nothing), and draws no checkbox at all.
  - The check page's thank line shows ONLY beside a found record whose signer check passed (*Signed with @x's passkey*), to that
    same @x; never beside an unconfirmed name, a withdrawn record, a failed comparison or no record.
  - Every thank link is exactly https://333.eco/@name?thank=b-mail#thank, and never carries from=b-mail (that marks another link).
  - Their @name is never part of the signed statement.
  - No count, no "not thanked", no absence (Sig-8); never "sign in"; never "verified".
  - Keep or give is a link to B-Origin, shown only when files were signed; nothing is uploaded from these pages.
Links are drawn inert (a data-href on a span), so a reviewer's tap reaches no live page.
All people are drawn and made up (@dara.chan sends, @sokha.keo receives), with example.com addresses.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""
import html
import re

# injected by build-boards.py
card = btns = spot = heart = person = None

SENDER, READER = "@dara.chan", "@sokha.keo"
THANK = "https://333.eco/%s?thank=b-mail#thank"
KEEP = "https://origin.333.eco/sign"
INVITE_HREF, SIGN_HREF = "https://333.eco/?from=b-mail", "https://sign.333.eco/b-mail?from=b-mail"  # explorer client/invite.ts
FILE = "kite-plan.pdf"
SHA = "3f9a2c71b0e4d58a6c1e9f20b7d43a8851c6e2f09ad7b314c5e8f61a2d90b7e4"  # a made-up fingerprint
SALT = "8b1e0c4fa27d95e3c06b4a1f7d28e9c5"

DT = {
"en": {
  # ── the check page: explorer.333.eco client/app.ts bmailPage + signerOf, client/attachments.ts fileBox, client/invite.ts ──
  "e_prod": "B-Explorer",  # client/index.html nav-name
  "e_tabs": ("B-Origin℠", "Ledger", "Corpus", "Legal"),  # client/index.html nav
  "e_foot": "explorer.333.eco · read-only · every check runs in your browser · visits are counted without cookies",  # client/index.html footer
  "c_h": "A B-Mail", "c_lede": "The exact message that was signed, checked in your browser just now. Compare it with the mail you received.",
  "c_rec": "This exact message is record #48,213", "c_when": "Signed 25 Nov 2026 (UTC). ", "c_record": "The record",
  "c_by": "Signed with {0}'s passkey",  # signerOf, ok
  "c_by_p": "Their page shows it, since 12 Nov 2026. It shows that a passkey signed, not who held it.",
  "c_nc": "Not confirmed against {0}'s page", "c_nc_p": "Its proof names a passkey that page doesn't show.",  # signerOf, not confirmed
  "kv": ("From", "To", "Subject", "Signed as", "Attachment"),  # bmailPage LABEL
  "f_h": "The files signed with it",
  "f_p": "This message was signed with these files, each by its fingerprint. Choose or drop the files that came with your mail to compare them. They are read on this device and never uploaded; only their fingerprints are compared.",
  "f_pick": "Choose files, or drop them here", "f_ok": "This is the file signed with the message.",
  "c_fine1": "This check runs in your browser at explorer.333.eco. A page at any other address, however alike it looks, is not this check. It shows that a passkey signed these words, never that a person did.",
  "c_fine2": "A link copied into another mail still shows this message, so what you see here is what was signed.",
  "c_invite": "{0} is an @name: a page at 333.eco where people find someone and thank them by name. You can hold your own.", "c_invite_a": "See 333.eco",
  "c_sign": "This mail was signed with a passkey. You can sign yours the same way.", "c_sign_a": "Sign your own mail",
  "c_thank": "Thank {0} for this mail",  # NEW (spec, Words)
  # ── Sign a mail: sign.333.eco services/sign/src/sign-text.ts MAIL_TEXT + SIGN_TEXT, public/mail.html, public/bmail.js ──
  "s_prod": "B-Origin℠",  # mail.html app-name
  "s_foot": "sign.333.eco · no passwords · only a passkey can sign",  # SIGN_TEXT foot
  "title": "Sign a mail",
  "lede": "Write your message and sign it with your passkey. Then send it from your own mail app. Whoever receives it can check that it is exactly what you signed.",
  "fromName": "Your name", "fromAddr": "Your email address", "to": "To", "toHint": "One address, or several with commas between them.",
  "cc": "Cc (optional)", "subject": "Subject", "body": "Message",
  "files": "Attached files (optional)", "pickFiles": "Choose files", "dropFiles": "or drop them here", "remove": "Remove",
  "filesHint": "Each file is signed by its fingerprint and stays on your device. You attach the same files to the mail yourself.",
  "asName": "Your @name (optional)",
  "asHint": "Readers are told it was signed with your @name's passkey only when your page at 333.eco shows the passkey you sign with.",
  "their": "Their @name (optional)",  # NEW (spec, Words)
  "theirHint": "So you can thank them after you sign. It isn't part of what you sign.",  # NEW (spec, Words)
  "exact": "Exactly what your passkey signs", "privacy": "Your message stays on your device. Only its fingerprint is sent.",
  "how": "How it was made", "howv": "Made by hand on a device",  # SIGN_TEXT how · SOURCE_LABELS digitalCreation
  "fingerprint": "Fingerprint", "size": "Size", "howLine": "How",
  "public": "This adds a public record: when it was signed and how it was made. The record holds a fingerprint, never your words. It shows that a passkey signed it, not who wrote it.",
  "go": "Sign with passkey", "new": "New here? Make a passkey",
  "done": "Signed", "doneLede": "Your signature is saved. It joins the public log at the next hourly update, around 3:07 PM.",
  "next": "Now send it from your own mail app, just as it is: from the same address, to the same people, with the same subject. If any of these change, a check will say the mail doesn't match.",
  "attachThese": "Attach these files to your mail, exactly as they are, and no others:",
  "noMailto": "Open in your mail app can't attach files. Attach them yourself before you send.",
  "attach": "Send it with no files attached. A file added to the mail will not match its signature.",  # hidden when files were signed (mail.js)
  "copy": "Copy the signed message", "open": "Open in your mail app", "see": "See what your readers see",
  "recordNo": "Record number", "at": "On", "atv": "11/25/2026, 3:06:41 PM",
  "fine": "We never receive your message. The link at its end carries the signed words and their proof to your readers.",
  "records": "Your records", "another": "Sign another mail",
  "said": "Signed with HeartBank® · បានចុះហត្ថលេខាជាមួយ HeartBank®",  # bmail.js SAID_EN · SAID_KM
  "s_thank": "Thank {0}",  # NEW position; words = 333.eco src/i18n.ts r8t_btn
  "keepGive": "Keep or give these files at B-Origin",  # NEW (spec, Words)
  # ── 333.eco's Thank: 333.eco src/pages/profile.ts renderWrite, src/i18n.ts ──
  "r8t_btn": "Thank {0}", "r8t_lede": "Say what you're thanking them for. That's the thanks; nothing else is needed.",
  "r8t_words": "Your words", "r8t_ph": "The kite you made for my daughter flew all afternoon.", "r8t_send": "Send my thanks",
  "r8t_fine": "Your words always arrive. A thanks can also carry Kiitos, which is how HeartBank® records a thank-you; if your passkey is asked for, it signs the Kiitos. Nothing is owed.",
  "cancel": "Cancel",
  # ── the drawn mail (made up) ──
  "m_from": "Dara Chan", "m_subject": "The kite plans",
  "m_body": "Here are the kite plans you asked for.\nThank you for teaching my daughter to fly it last Sunday.",
  "m_size": "1.2 MB", "m_stmt_size": "612 B", "m_fp": "9c41 7be0 2a5f d318 …",
},
"km": {
  "e_prod": "B-Explorer",
  "e_tabs": ("B-Origin℠", "បញ្ជីការដឹងគុណ", "សារពើភ័ណ្ឌឯកសារ", "ច្បាប់"),
  "e_foot": "explorer.333.eco · អានតែប៉ុណ្ណោះ · ការពិនិត្យទាំងអស់ដំណើរការក្នុងកម្មវិធីរុករករបស់អ្នក · ការចូលមើលត្រូវបានរាប់ដោយគ្មានខូគី",
  "c_h": "B-Mail មួយ", "c_lede": "សារពិតប្រាកដដែលបានចុះហត្ថលេខា ដែលបានពិនិត្យក្នុងកម្មវិធីរុករករបស់អ្នកមុននេះ។ សូមប្រៀបធៀបវាជាមួយសំបុត្រដែលអ្នកបានទទួល។",
  "c_rec": "សារពិតប្រាកដនេះគឺជាកំណត់ត្រា #48,213", "c_when": "បានចុះហត្ថលេខា ២៥ វិច្ឆិកា ២០២៦ (UTC)។ ", "c_record": "កំណត់ត្រា",
  "c_by": "បានចុះហត្ថលេខាដោយ passkey របស់ {0}",
  "c_by_p": "ទំព័ររបស់ពួកគេបង្ហាញវា តាំងពី ១២ វិច្ឆិកា ២០២៦។ វាបង្ហាញថា passkey មួយបានចុះហត្ថលេខា មិនមែនថាអ្នកណាកាន់វាទេ។",
  "c_nc": "មិនបានបញ្ជាក់ជាមួយទំព័ររបស់ {0} ទេ", "c_nc_p": "ភស្តុតាងរបស់វាដាក់ឈ្មោះ passkey ដែលទំព័រនោះមិនបង្ហាញ។",
  "kv": ("ពី", "ទៅ", "ប្រធានបទ", "បានចុះហត្ថលេខាជា", "ឯកសារភ្ជាប់"),
  "f_h": "ឯកសារដែលបានចុះហត្ថលេខាជាមួយវា",
  "f_p": "សារនេះត្រូវបានចុះហត្ថលេខាជាមួយឯកសារទាំងនេះ ដោយស្នាមម្រាមដៃរបស់ឯកសារនីមួយៗ។ សូមជ្រើសរើស ឬទម្លាក់ឯកសារដែលភ្ជាប់មកជាមួយសំបុត្ររបស់អ្នក ដើម្បីប្រៀបធៀបវា។ ឯកសារត្រូវបានអាននៅលើឧបករណ៍នេះ ហើយមិនដែលត្រូវបានផ្ទុកឡើងទេ។ មានតែស្នាមម្រាមដៃរបស់វាប៉ុណ្ណោះដែលត្រូវបានប្រៀបធៀប។",
  "f_pick": "ជ្រើសរើសឯកសារ ឬទម្លាក់វានៅទីនេះ", "f_ok": "នេះគឺជាឯកសារដែលបានចុះហត្ថលេខាជាមួយសារ។",
  "c_fine1": "ការពិនិត្យនេះដំណើរការក្នុងកម្មវិធីរុករករបស់អ្នកនៅ explorer.333.eco។ ទំព័រនៅអាសយដ្ឋានផ្សេង ទោះមើលទៅដូចគ្នាយ៉ាងណាក៏ដោយ មិនមែនជាការពិនិត្យនេះទេ។ វាបង្ហាញថា passkey មួយបានចុះហត្ថលេខាលើពាក្យទាំងនេះ មិនមែនថាមនុស្សម្នាក់បានធ្វើទេ។",
  "c_fine2": "តំណដែលបានចម្លងទៅក្នុងសំបុត្រផ្សេងទៀតនៅតែបង្ហាញសារនេះ ដូច្នេះអ្វីដែលអ្នកឃើញនៅទីនេះគឺជាអ្វីដែលបានចុះហត្ថលេខា។",
  "c_invite": "{0} គឺជា @name៖ ទំព័រមួយនៅ 333.eco ដែលមនុស្សស្វែងរកនរណាម្នាក់ ហើយអរគុណគេតាមឈ្មោះ។ អ្នកក៏អាចកាន់ឈ្មោះផ្ទាល់ខ្លួនបានដែរ។", "c_invite_a": "មើល 333.eco",
  "c_sign": "សំបុត្រនេះបានចុះហត្ថលេខាដោយ passkey។ អ្នកអាចចុះហត្ថលេខាលើសំបុត្ររបស់អ្នកតាមរបៀបដូចគ្នា។", "c_sign_a": "ចុះហត្ថលេខាលើសំបុត្ររបស់អ្នក",
  "c_thank": "អរគុណ {0} សម្រាប់សំបុត្រនេះ",  # NEW, ours
  "s_prod": "B-Origin℠",
  "s_foot": "sign.333.eco · គ្មានពាក្យសម្ងាត់ · មានតែ passkey ទេដែលអាចចុះហត្ថលេខាបាន",
  "title": "ចុះហត្ថលេខាលើសំបុត្រ",
  "lede": "សរសេរសាររបស់អ្នក ហើយចុះហត្ថលេខាដោយ passkey របស់អ្នក។ បន្ទាប់មក ផ្ញើវាពីកម្មវិធីអ៊ីមែលរបស់អ្នកផ្ទាល់។ អ្នកដែលទទួលវាអាចពិនិត្យថា វាជាអ្វីដែលអ្នកបានចុះហត្ថលេខាពិតប្រាកដ។",
  "fromName": "ឈ្មោះរបស់អ្នក", "fromAddr": "អាសយដ្ឋានអ៊ីមែលរបស់អ្នក", "to": "ទៅកាន់", "toHint": "អាសយដ្ឋានមួយ ឬច្រើន ដោយមានក្បៀសនៅចន្លោះ។",
  "cc": "Cc (ស្រេចចិត្ត)", "subject": "ប្រធានបទ", "body": "សារ",
  "files": "ឯកសារភ្ជាប់ (ស្រេចចិត្ត)", "pickFiles": "ជ្រើសរើសឯកសារ", "dropFiles": "ឬទម្លាក់វានៅទីនេះ", "remove": "ដកចេញ",
  "filesHint": "ឯកសារនីមួយៗត្រូវបានចុះហត្ថលេខាតាមស្នាមម្រាមដៃរបស់វា ហើយនៅលើឧបករណ៍របស់អ្នក។ អ្នកភ្ជាប់ឯកសារដដែលទៅសំបុត្រដោយខ្លួនឯង។",
  "asName": "@name របស់អ្នក (ស្រេចចិត្ត)",
  "asHint": "អ្នកអានត្រូវបានប្រាប់ថា វាបានចុះហត្ថលេខាដោយ passkey របស់ @name របស់អ្នក តែនៅពេលដែលទំព័ររបស់អ្នកនៅ 333.eco បង្ហាញ passkey ដែលអ្នកប្រើចុះហត្ថលេខា។",
  "their": "@name របស់ពួកគេ (ស្រេចចិត្ត)",  # NEW, ours
  "theirHint": "ដើម្បីឱ្យអ្នកអាចអរគុណពួកគេ បន្ទាប់ពីអ្នកចុះហត្ថលេខា។ វាមិនមែនជាផ្នែកនៃអ្វីដែលអ្នកចុះហត្ថលេខាទេ។",  # NEW, ours
  "exact": "អ្វីដែល passkey របស់អ្នកចុះហត្ថលេខាពិតប្រាកដ", "privacy": "សាររបស់អ្នកនៅលើឧបករណ៍របស់អ្នក។ មានតែស្នាមម្រាមដៃរបស់វាទេដែលត្រូវបានផ្ញើ។",
  "how": "របៀបដែលវាត្រូវបានបង្កើត", "howv": "បង្កើតដោយដៃនៅលើឧបករណ៍",
  "fingerprint": "ស្នាមម្រាមដៃ", "size": "ទំហំ", "howLine": "របៀប",
  "public": "ការនេះបន្ថែមកំណត់ត្រាសាធារណៈមួយ៖ ពេលដែលវាត្រូវបានចុះហត្ថលេខា និងរបៀបដែលវាត្រូវបានបង្កើត។ កំណត់ត្រាមានតែស្នាមម្រាមដៃ មិនដែលមានពាក្យរបស់អ្នកទេ។ វាបង្ហាញថា passkey មួយបានចុះហត្ថលេខា មិនមែនថាអ្នកណាជាអ្នកសរសេរវាទេ។",
  "go": "ចុះហត្ថលេខាដោយ passkey", "new": "ថ្មីនៅទីនេះ? បង្កើត passkey",
  "done": "បានចុះហត្ថលេខា", "doneLede": "ហត្ថលេខារបស់អ្នកត្រូវបានរក្សាទុក។ វានឹងចូលទៅក្នុងកំណត់ហេតុសាធារណៈនៅការធ្វើបច្ចុប្បន្នភាពរៀងរាល់ម៉ោងបន្ទាប់ ប្រហែល 15:07។",
  "next": "ឥឡូវ សូមផ្ញើវាពីកម្មវិធីអ៊ីមែលរបស់អ្នកផ្ទាល់ ដូចដែលវាមាន៖ ពីអាសយដ្ឋានដដែល ទៅកាន់អ្នកទទួលដដែល ជាមួយប្រធានបទដដែល។ ប្រសិនបើមានអ្វីមួយផ្លាស់ប្តូរ ការពិនិត្យនឹងនិយាយថាសំបុត្រមិនត្រូវគ្នា។",
  "attachThese": "សូមភ្ជាប់ឯកសារទាំងនេះទៅសំបុត្ររបស់អ្នក ដូចដែលវាមាន ហើយគ្មានឯកសារផ្សេងទៀតទេ៖",
  "noMailto": "«បើកក្នុងកម្មវិធីអ៊ីមែលរបស់អ្នក» មិនអាចភ្ជាប់ឯកសារបានទេ។ សូមភ្ជាប់វាដោយខ្លួនឯង មុនពេលផ្ញើ។",
  "attach": "សូមផ្ញើវាដោយគ្មានឯកសារភ្ជាប់។ ឯកសារដែលបន្ថែមទៅសំបុត្រនឹងមិនត្រូវគ្នានឹងហត្ថលេខារបស់វាទេ។",
  "copy": "ចម្លងសារដែលបានចុះហត្ថលេខា", "open": "បើកក្នុងកម្មវិធីអ៊ីមែលរបស់អ្នក", "see": "មើលអ្វីដែលអ្នកអានរបស់អ្នកឃើញ",
  "recordNo": "លេខកំណត់ត្រា", "at": "នៅ", "atv": "25/11/2026 15:06:41",
  "fine": "យើងមិនដែលទទួលសាររបស់អ្នកទេ។ តំណនៅចុងសារនាំពាក្យដែលបានចុះហត្ថលេខា និងភស្តុតាងរបស់វា ទៅកាន់អ្នកអានរបស់អ្នក។",
  "records": "កំណត់ត្រារបស់អ្នក", "another": "ចុះហត្ថលេខាលើសំបុត្រមួយទៀត",
  "said": "Signed with HeartBank® · បានចុះហត្ថលេខាជាមួយ HeartBank®",
  "s_thank": "អរគុណ {0}",
  "keepGive": "រក្សាទុក ឬផ្ដល់ឯកសារទាំងនេះនៅ B-Origin",  # NEW, ours
  "r8t_btn": "អរគុណ {0}", "r8t_lede": "និយាយថាអ្នកអរគុណពួកគេចំពោះអ្វី។ នោះហើយជាការអរគុណ គ្មានអ្វីផ្សេងទៀតត្រូវការទេ។",
  "r8t_words": "ពាក្យរបស់អ្នក", "r8t_ph": "ខ្លែងដែលអ្នកធ្វើឱ្យកូនស្រីខ្ញុំ ហោះពេញមួយរសៀល។", "r8t_send": "ផ្ញើការអរគុណរបស់ខ្ញុំ",
  "r8t_fine": "ពាក្យរបស់អ្នកតែងតែទៅដល់។ ការអរគុណក៏អាចមាន Kiitos ដែលជារបៀបដែល HeartBank® កត់ត្រាការអរគុណ។ ប្រសិនបើ passkey របស់អ្នកត្រូវបានស្នើ វាចុះហត្ថលេខាលើ Kiitos។ មិនជំពាក់អ្វីទេ។",
  "cancel": "បោះបង់",
  "m_from": "Dara Chan", "m_subject": "ផែនការខ្លែង",
  "m_body": "នេះជាផែនការខ្លែងដែលអ្នកបានស្នើសុំ។\nអរគុណដែលបានបង្រៀនកូនស្រីខ្ញុំឱ្យបង្ហោះវា កាលពីថ្ងៃអាទិត្យមុន។",
  "m_size": "1.2 MB", "m_stmt_size": "612 B", "m_fp": "9c41 7be0 2a5f d318 …",
},
}

# Which live host each board extends: its header and footer come from that host (build-boards.page asks here).
HOST = {"CS1": "sign", "CS2": "sign", "C1": "explorer", "C1b": "explorer", "CT1": "333"}


def _lang(d):
    return "km" if d is DT["km"] else "en"


def mark(sid, lang, registry_mark, heart_mark):
    """The header's mark: 333.eco's own for the Thank, else the wordmark with the live page's name beside it."""
    if HOST[sid] == "333":
        return registry_mark
    d = DT[lang]
    return heart_mark + ' <span class="prod">%s</span>' % (d["e_prod"] if HOST[sid] == "explorer" else d["s_prod"])


def foot(sid, lang, registry_foot):
    d = DT[lang]
    return registry_foot if HOST[sid] == "333" else d["e_foot"] if HOST[sid] == "explorer" else d["s_foot"]


# ── drawing helpers ───────────────────────────────────────────────────────────────────────────────────────────────
def _a(text, href, cls="link"):
    """A link, drawn inert: the address is kept in data-href, so a tap on a public drawing reaches no live page."""
    return '<span class="%s" data-href="%s">%s</span>' % (cls, href, text)


def _leg(ok, title, *body):
    cls = "bmt-ok" if ok is True else "bmt-bad" if ok is False else "bmt-q"
    return '<div class="bmt-leg"><b class="%s">%s</b><p>%s</p></div>' % (cls, title, "".join(body))


def _field(label, value="", hint="", cls=""):
    return ('<div class="bmt-f"><div class="bmt-l">%s</div><div class="field%s">%s</div>%s</div>'
            % (label, cls, value or "&nbsp;", '<p class="bmt-hint">%s</p>' % hint if hint else ""))


def _statement(d):
    """The b-mail/v1 text the press signs (sign.333.eco public/bmail.js statement): Their @name is NOT in it."""
    lines = ["b-mail/v1", "from: %s <dara@example.com>" % d["m_from"], "to: sokha@example.com", "subject: " + d["m_subject"],
             "name: " + SENDER, "salt: " + SALT, "attachment: %s %s" % (SHA, FILE)]
    return "\n".join(lines) + "\n\n" + d["m_body"] + "\n"


def _fileicon():
    return ('<svg width="30" height="36" viewBox="0 0 30 36" aria-hidden="true"><path d="M3 2h16l8 8v24H3z" fill="var(--surface-2)" '
            'stroke="var(--line-strong)" stroke-width="1.5" stroke-linejoin="round"/><path d="M19 2v8h8" fill="none" stroke="var(--line-strong)" '
            'stroke-width="1.5"/><path d="M8 18h14M8 23h14M8 28h9" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/></svg>')


def _filerow(d, action=""):
    return ('<div class="bmt-file">%s<div class="bmt-fm"><div class="t">%s</div><div class="s">%s</div></div>%s</div>'
            % (_fileicon(), FILE, d["m_size"], '<span class="link">%s</span>' % action if action else ""))


def _etabs(d):
    return '<div class="tabs bmt-tabs">%s</div>' % "".join("<span>%s</span>" % x for x in d["e_tabs"])  # /b-mail is no tab: none is on


# ── the boards ─────────────────────────────────────────────────────────────────────────────────────────────────────
def CS1(t, d):
    """Sign a mail, written: the new optional field Their @name, with its hint; the preview shows it is not signed."""
    files = ('<div class="bmt-f"><div class="bmt-l">%s</div><div class="card bmt-drop"><span class="btn ghost">%s</span>'
             '<span class="fine">%s</span></div><div class="card bmt-list">%s</div><p class="bmt-hint">%s</p></div>'
             % (d["files"], d["pickFiles"], d["dropFiles"], _filerow(d, d["remove"]), d["filesHint"]))
    facts = ('<dl class="kv bmt-facts"><dt>%s</dt><dd class="mono">%s</dd><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd></dl>'
             % (d["fingerprint"], d["m_fp"], d["size"], d["m_stmt_size"], d["howLine"], d["howv"]))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["title"], d["lede"])
            + _field(d["fromName"], d["m_from"]) + _field(d["fromAddr"], "dara@example.com")
            + _field(d["to"], "sokha@example.com", d["toHint"]) + _field(d["cc"]) + _field(d["subject"], d["m_subject"])
            + _field(d["body"], d["m_body"].replace("\n", "<br>"), cls=" area bmt-body") + files
            + _field(d["asName"], SENDER, d["asHint"], " mono")
            + '<div class="bmt-new">%s</div>' % _field(d["their"], READER, d["theirHint"], " mono")
            + '<p class="bmt-l bmt-exact">%s</p><pre class="bmt-pre">%s</pre>' % (d["exact"], html.escape(_statement(d), quote=False))
            + '<p class="fine">%s</p>' % d["privacy"]
            + _field(d["how"], d["howv"] + ' <span class="bmt-caret">▾</span>', cls=" bmt-sel") + facts
            + '<p class="fine">%s</p>' % d["public"]
            + '<button class="btn">%s</button><button class="btn ghost">%s</button>' % (d["go"], d["new"]))


def _out(d):
    sig = "%s\n\n-- \n%s · https://333.eco/%s\n%s: https://explorer.333.eco/b-mail#m=YmItbWFpbC92MQpmcm9tOiBE…" % (
        d["m_body"], d["m_from"], SENDER, d["said"])
    return '<div class="bmt-out">%s</div>' % sig.replace("\n", "<br>")


def CS2(t, d):
    """After the press, with a file signed: the live result card, plus Thank @them and Keep or give these files at B-Origin."""
    filescard = ('<div class="card bmt-note"><p>%s</p><div class="bmt-list">%s</div><p>%s</p><p class="bmt-keep">%s</p></div>'
                 % (d["attachThese"], _filerow(d), d["noMailto"], _a(d["keepGive"] + " ›", KEEP, "link bmt-keepgive")))
    return ("<h1>%s</h1><p class='lede'>%s</p><p class='bmt-p'>%s</p>" % (d["done"], d["doneLede"], d["next"]) + filescard + _out(d)
            + '<button class="btn">%s</button>' % d["copy"]
            + '<button class="btn ghost">%s</button><button class="btn ghost">%s</button>' % (d["open"], d["see"])
            + '<div class="bmt-sep"></div>'
            + _a(d["s_thank"].format(READER), THANK % READER, "btn ghost bmt-thank")
            + '<dl class="kv bmt-facts"><dt>%s</dt><dd>48213</dd><dt>%s</dt><dd>%s</dd></dl>' % (d["recordNo"], d["at"], d["atv"])
            + '<p class="fine">%s</p>' % d["fine"]
            + '<button class="btn ghost">%s</button><button class="btn ghost">%s</button>' % (d["records"], d["another"]))


def _check(d, confirmed):
    """The check page for one found record. `confirmed`: the signer check ran here and passed."""
    if confirmed:
        who = _leg(True, d["c_by"].format(SENDER), d["c_by_p"])
    else:
        who = _leg(None, d["c_nc"].format(SENDER), d["c_nc_p"])
    rows = '<div class="card">%s%s</div>' % (_leg(True, d["c_rec"], d["c_when"], " ", _a(d["c_record"], "/origin/48213")), who)
    k = d["kv"]
    kv = [(k[0], "%s &lt;dara@example.com&gt;" % d["m_from"]), (k[1], "sokha@example.com"), (k[2], d["m_subject"])]
    if confirmed:  # "Signed as" shows only when the signer check passed (bmailPage signedAs)
        kv.append((k[3], SENDER))
    kv.append((k[4], "%s… %s" % (SHA[:12], FILE)))
    mail = ('<div class="card"><dl class="bmt-kv">%s</dl><div class="bmt-mail">%s</div></div>'
            % ("".join("<dt>%s</dt><dd>%s</dd>" % x for x in kv), d["m_body"].replace("\n", "<br>")))
    box = ('<div class="card"><h2>%s</h2><p>%s</p><p class="bmt-pick">%s</p>%s</div>'
           % (d["f_h"], d["f_p"], _a(d["f_pick"], "#"), _leg(True, FILE, d["f_ok"])))
    thank = ('<div class="card bmt-line"><p>%s</p></div>' % _a(d["c_thank"].format(SENDER), THANK % SENDER)) if confirmed else ""
    return (_etabs(d) + "<h1>%s</h1><p class='lede'>%s</p>" % (d["c_h"], d["c_lede"]) + rows + mail + box
            + '<p class="fine">%s</p><p class="fine">%s</p>' % (d["c_fine1"], d["c_fine2"]) + thank
            + '<div class="card bmt-line"><p>%s %s</p></div>' % (d["c_invite"].format(SENDER), _a(d["c_invite_a"], INVITE_HREF))
            + '<div class="card bmt-line"><p>%s %s</p></div>' % (d["c_sign"], _a(d["c_sign_a"], SIGN_HREF)))


def C1(t, d):
    return _check(d, True)


def C1b(t, d):
    return _check(d, False)


def CT1(t, d):
    """333.eco's Thank, opened at once by ?thank=b-mail#thank: the page's own composer, words empty, with no Without my name."""
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["r8t_btn"].format(SENDER), d["r8t_lede"])
            + '<div class="bmt-l">%s</div><div class="field area bmt-ph">%s</div>' % (d["r8t_words"], d["r8t_ph"])
            + '<button class="btn bmt-off" aria-disabled="true">%s</button>' % d["r8t_send"]
            + '<p class="fine">%s</p>' % d["r8t_fine"]
            + '<button class="btn ghost">%s</button>' % d["cancel"])


SCREENS = [  # (id, page, title, render(t, d)), in the order the two people walk it
    ("CS1", "bmail", "Sign a mail: Their @name (optional) [S1]", CS1),
    ("CS2", "bmail", "Signed, with a file: Thank @them and Keep or give at B-Origin [S2]", CS2),
    ("C1", "bmail", "The check page, signer confirmed: Thank @x for this mail [C1]", C1),
    ("C1b", "bmail", "The check page, name not confirmed: no thank line (the rule C1 keeps)", C1b),
    ("CT1", "bmail", "333.eco's Thank opened from a B-Mail: no Without my name [T1]", CT1),
]
PUBLIC = set()  # a person's mail and their own pages: no share button (Default 8)
CSS = """
.bmt-f{margin:0 0 12px}
.bmt-l{font-size:13px;color:var(--ink-dim);margin:0 0 4px}
.bmt-f .field{margin-top:0}
.bmt-hint{font-size:12.5px;color:var(--ink-dim);margin:5px 0 0}
.bmt-body{min-height:0;color:var(--ink);font-size:15px}
.bmt-new{border-left:3px solid var(--accent);padding-left:10px;margin:0 0 12px -13px}
.bmt-new .bmt-f{margin:0}
.bmt-drop{display:flex;align-items:center;gap:12px;padding:10px 12px;margin:0 0 8px;border-style:dashed}
.bmt-drop .btn{width:auto;margin:0;padding:9px 14px;font-size:14px}
.bmt-drop .fine{margin:0}
.bmt-list{padding:6px 12px;margin:0}
.bmt-file{display:flex;align-items:center;gap:12px;padding:6px 0}
.bmt-file svg{flex:none}
.bmt-fm{flex:1;min-width:0}.bmt-fm .t{font-size:14px;font-family:var(--font-mono)}.bmt-fm .s{font-size:12.5px;color:var(--ink-dim)}
.bmt-exact{margin:4px 0 6px}
.bmt-pre{font:12px/1.5 var(--font-mono);white-space:pre-wrap;overflow-wrap:anywhere;background:var(--surface-2);border:1px solid var(--line);
  border-radius:12px;padding:10px 12px;margin:0 0 4px;color:var(--ink)}
.bmt-sel{display:flex;justify-content:space-between}
.bmt-caret{color:var(--ink-dim)}
.bmt-facts{margin:12px 0 0}
.bmt-p{margin:0 0 12px;font-size:14px}
.bmt-note p{margin:0 0 8px;color:var(--ink);font-size:14px}
.bmt-note .bmt-list{border:1px solid var(--line);border-radius:12px;margin:0 0 8px;background:var(--bg)}
.bmt-note .bmt-keep{margin:10px 0 0;padding-top:10px;border-top:1px solid var(--line)}
.bmt-out{font:13px/1.5 var(--font-mono);border:1px solid var(--line-strong);border-radius:12px;background:var(--bg);padding:10px 12px;
  overflow-wrap:anywhere;color:var(--ink);margin:4px 0 4px}
.bmt-sep{height:1px;background:var(--line);margin:16px 0 8px}
span.btn{box-sizing:border-box}
.bmt-leg{padding:11px 0;border-top:1px solid var(--line)}.bmt-leg:first-of-type{border-top:0}
.bmt-leg b{display:block;font-weight:650;font-size:15px}.bmt-leg p{margin:3px 0 0;overflow-wrap:anywhere;font-size:14px;color:var(--ink-dim)}
.bmt-ok::before{content:"✓ ";color:var(--accent)}
.bmt-kv{display:grid;grid-template-columns:1fr;gap:2px;margin:0;font-size:14px}.bmt-kv dt{color:var(--ink-dim)}
.bmt-kv dd{margin:0 0 8px;overflow-wrap:anywhere}
.bmt-mail{margin:6px 0 0;padding-top:10px;border-top:1px solid var(--line);font-size:15px;line-height:1.55}
.bmt-pick{margin:10px 0 4px}
.bmt-line p{color:var(--ink);font-size:14px}
.field.area.bmt-ph{color:var(--ink-faint)}
.bmt-tabs .sm{padding:0}
.bmt-off{opacity:.45}
"""
BARRED = [  # words these boards must never draw (markup stripped first; footer included)
    (r"\bsign[\s-]?in\b", "Log in authenticates; 'sign in' is barred (Default 10)"),
    (r"\bverified\b|\bunverified\b|បានផ្ទៀងផ្ទាត់", "never 'verified': a passkey signed, not a proven person"),
    (r"not thanked|haven.t (been )?thanked|\bnot yet\b|\byet to\b|\bunthanked\b|\bno thanks\b|\bwaiting\b|\bmissed\b|\bremind|មិនទាន់អរគុណ",
     "no absence: never what was not done (Sig-8)"),
    (r"\b\d[\d,]*\s+(thanks|thank-yous|kiitos|people|times|readers|thanked)\b|\bthanks? (count|total)\b|\btimes thanked\b",
     "no count of thanks (Sig-8)"),
    (r"don.t forget|\bplease thank\b|\bsay thanks\b", "the thank is offered, never pressed on anyone"),
]
THANK_RE = re.compile(r"^https://333\.eco/@[a-z0-9._-]+\?thank=b-mail#thank$")


def _text(html):
    t = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))


def check(sid, html):
    """Raise if a board breaks a rule of the spec. `html` is the board's body plus its footer."""
    text = _text(html)
    for pat, why in BARRED:
        m = re.search(pat, text, re.I)
        assert not m, "%s: %r is barred: %s" % (sid, m.group(0), why)
    links = re.findall(r'<span class="([^"]*)" data-href="([^"]*)"', html)
    thanks = [(c, h) for c, h in links if "thank=" in h or "333.eco/@" in h]
    for c, h in thanks:
        assert "from=" not in h, "%s: a thank link never carries from=b-mail (%s)" % (sid, h)
        assert THANK_RE.match(h), "%s: a thank link is exactly https://333.eco/@name?thank=b-mail#thank (%s)" % (sid, h)
        # Never pre-selected: never the page's primary button, never marked on.
        assert c.split()[0] == "link" or "ghost" in c.split(), "%s: the thank is never the primary button (%s)" % (sid, c)
        assert not re.search(r"\b(on|selected|checked|primary)\b", c), "%s: the thank is never pre-selected (%s)" % (sid, c)
    if HOST[sid] in ("explorer", "sign"):
        # A thank drawn in words alone (a plain line, a second button) would dodge every rule above, which reads the links.
        said = len(re.findall(r"(?:\bThank|អរគុណ) @", text, re.I))
        assert said == len(thanks), "%s: every thank offered is a checked thank link (%d said, %d links)" % (sid, said, len(thanks))
    if HOST[sid] == "explorer":
        for c, h in thanks:
            x = h.split("/", 3)[3].split("?")[0]
            ok = (r'<b class="bmt-ok">Signed with %s&#x27;s passkey</b>|<b class="bmt-ok">Signed with %s\'s passkey</b>|'
                  r'<b class="bmt-ok">បានចុះហត្ថលេខាដោយ passkey របស់ %s</b>') % (re.escape(x), re.escape(x), re.escape(x))
            assert re.search(ok, html), "%s: the thank line shows only beside a passing 'Signed with %s's passkey'" % (sid, x)
            bad = re.search(r"Not confirmed|withdrew|No record of this exact message|doesn.t fit this record|holds no B-Mail|didn.t pass its check|"
                            r"មិនបានបញ្ជាក់|បានដកវា|គ្មានកំណត់ត្រា|មិនត្រូវនឹងកំណត់ត្រា", text)
            assert not bad, "%s: no thank line beside %r" % (sid, bad.group(0))
            thank_text = re.search(r'data-href="%s">([^<]*)<' % re.escape(h), html).group(1)
            assert x in thank_text, "%s: the thank names the same @name the signer check passed" % sid
        if sid == "C1":
            assert len(thanks) == 1, "C1: the thank line is drawn, once"
        if sid == "C1b":
            assert not thanks, "C1b: no thank line beside an unconfirmed name"
    if sid == "CS1":
        pre = re.search(r'<pre class="bmt-pre">(.*?)</pre>', html, re.S).group(1)
        their = re.search(r'<div class="bmt-new">.*?<div class="field mono">([^<]*)</div>', html, re.S).group(1)
        assert their.startswith("@") and their not in pre, "CS1: Their @name is never part of the signed statement"
        assert not re.search(r"^(thank|their|to-name|recipient):", pre, re.M), "CS1: the statement's format is unchanged"
        assert re.search(r"\((optional|ស្រេចចិត្ត)\)", re.search(r'<div class="bmt-new">(.*?)</div>', html, re.S).group(1)), "CS1: Their @name is optional"
    if sid == "CS2":
        assert len(thanks) == 1, "CS2: one name, one Thank, in v1"
        keep = [h for c, h in links if "bmt-keepgive" in c]
        assert keep == [KEEP], "CS2: Keep or give links to %s and nowhere else" % KEEP
        assert 'class="bmt-file"' in html, "CS2: Keep or give shows only when files were signed"
        assert not re.search(r"Send it with no files attached|សូមផ្ញើវាដោយគ្មានឯកសារភ្ជាប់", text), \
            "CS2: with files signed, the no-files line is hidden (mail.js)"
    if HOST[sid] == "333":
        assert not re.search(r"without (my|your) name|ដោយមិនដាក់ឈ្មោះ|គ្មានឈ្មោះ", text, re.I), "%s: never Without my name on this path" % sid
        assert not re.search(r'type="checkbox"|class="check"|class="tog', html), "%s: no checkbox or switch on this path" % sid
        area = re.search(r'<div class="field area bmt-ph">([^<]*)</div>', html)
        ph = DT["km" if re.search("[\u1780-\u17ff]", text) else "en"]["r8t_ph"]  # the Thank board carries no Khmer in English
        assert area and area.group(1) == ph, "%s: the words field opens empty (only its placeholder), never pre-filled" % sid
        assert re.search(r'<button class="btn bmt-off" aria-disabled="true">', html), "%s: Send waits for the person's own words" % sid
