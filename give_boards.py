"""Giving a kept file at origin.333.eco (A652): the Give sheet, the link and its code, the gift page, Keep, Thank, alerts, and
the choice to remove where a picture was taken before signing. The spec is private (sign.333.eco SPEC.md §10c-ter, founder
2026-11-17). Imported by build-boards.py, which injects the shared helpers.

Copy rules this file must keep (checked at build time by check()):
  - Every default is the quiet one: Anyone with the link · Give without a name · Private.
  - ⛔ Never an absence: no "opened", "not kept", "not thanked", "waiting" (Sig-8). A row says what happened: Offered, Given, Thanked.
  - ⛔ An anonymous gift names no one; the thank's return names no one.
  - ⛔ A private gift's chat card has no picture (the chat app's own computers fetch the card).
  - ⛔ No storage address, no "sign in", no countdown; a price is a fact, said once, only above the free length.
  - The thank is offered on the kept file only, never on the link or its card, and never pressed on anyone.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""
import io, os, re
import kept_boards as KP
import blink_boards as BL

# injected by build-boards.py
card = btns = spot = heart = person = sunflower = qr = None

KEY = KP.KEY
OK = KP.OK
LINK = "B.333.eco/h4kq8tz2mxw9c3vbn6rpyd5fj7"  # an unlisted link: 26 characters, so it can't be guessed
# ⭐ The link's code is a B-QR (founder 2026-11-17: *"make the QR code a B-QR"*), painted by the brand layer's own recipe
#   (brand/bqr.ts, vendored) into give-bqr.svg by scripts/bqr-svg.mjs, in its owner's ink: a link into 333.eco is MA's (B-Link
#   `ownerOf`). It is a real code for the drawn address (jsQR and ZXing both read it); regenerate it if LINK changes.
BQR_SVG = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "give-bqr.svg"), encoding="utf-8").read().strip()

DT = {
"en": {
  "date16": "16 Nov 2026", "signed": "Signed", "check": "Check its record", "kfiles": "Your kept files",
  # G1 sign: remove where it was taken
  "file": "sunflower.jpg · 2.4 MB",
  "loc_says": "This picture says where it was taken.",
  "loc": "Remove where it was taken",
  "loc_p": "The copy you sign won't say where it was taken. Your original on this device still does.",
  # G2 the giver's list
  "g2_lede": "Files you keep here. Only you can open them.",
  "g2_rows": (("pic", "Picture · 2.4 MB", "kept 16 Nov 2026 · a3f9 c2e1", None, ("Give", "Download", "Remove")),
              ("video", "Video · 1 min 40 s · 96 MB", "kept 14 Nov 2026 · 5d21 8e0b", "Offered", ("Copy link", "Withdraw")),
              ("doc", "PDF · 840 KB", "kept 12 Nov 2026 · 07bd 5a90", "Given", ()),
              ("voice", "Voice · 3.1 MB", "kept 2 Nov 2026 · e44c 1b72", "Given · Thanked", ())),
  "g2_note": "Give sends a file you keep to someone else. Once they keep it, it's theirs.",
  # G3 the Give sheet
  "g3_h": "Give this file", "g3_file": "Video · 1 min 40 s · 96 MB", "g3_signed": "Signed 14 Nov 2026",
  "who_h": "Who can keep it",
  "who1": "Anyone with the link", "who1p": "The first person to keep it has it for good. Until then, you can withdraw it.",
  "who2": "Only one @name", "who2p": "They show it's them with their passkey.",
  "name_h": "Your name",
  "name1": "Give without a name",
  "name1p": "Your name isn't shown. If you ever shared your passkey signature with this file, or the file's own details name you, they still can.",
  "name2": "Show my @name", "name2p": "You'll press your passkey to show it's yours.",
  "vis_h": "Who sees it",
  "vis1": "Private", "vis1p": "The link's preview shows no picture. Once it's kept, the link shows only that it was kept.",
  "vis2": "Public", "vis2p": "The preview shows the picture, and the link keeps showing the file until the person who keeps it makes it private.",
  "price": "Giving this keeps it for good. The part past the free minute costs $0.19 once, from your balance. The payment stays with the file: removing the file doesn't return it.",
  "give": "Give", "give_fine": "Then you'll get a link to send, and a code to print.",
  # G4 when a choice can't be made
  "g4_h": "Give: when a choice can't be made", "g4_lede": "The sheet says why, once, where the choice would be.",
  "g4_a": "A file that says where it was taken", "g4_ap": "This file says where it was taken, so it can be given only privately.",
  "g4_b": "An @name whose page shows no passkey",
  "g4_bp": "A gift locked to an @name needs a passkey shown on that @name's page. You can give it with a link instead.",
  "g4_c": "The balance can't pay", "g4_cp": "Your balance can't pay for this. Nothing was given.", "g4_cb": "Your balance",
  # G5 the link
  "g5_h": "Your link", "g5_lede": "Send it, or print its code. Whoever keeps it first has it for good.",
  "copy": "Copy", "share": "Share", "print": "Print or save it as a B-QR",  # b.333.eco pages.ts, word for word
  "qr_p": "The code is the link. Anyone who scans it can open the file.",
  "unlisted": "This link isn't listed anywhere. Only the people you give it to can open it.",
  "withdraw": "Until someone keeps it, you can withdraw it from Your kept files.",
  # G6 the cards in a chat
  "g6_h": "How the link looks in a chat", "g6_lede": "The card says what the link is. A private gift's card has no picture.",
  "priv": "Private", "pub": "Public", "from": "Sokha", "msg": "Something for you.",
  "pt": "A file for you", "pf": "Open it to see it and keep it.",
  "g6_ch": "The chat app makes the card",
  "g6_cp": "To draw a card, the chat app's own computers open the link. That's why a private gift's card never shows its picture.",
  # G7 the gift page
  "g7_h": "A file for you", "keep": "Keep it",
  "keep_fine": "It becomes yours for good, and costs you nothing. You'll log in with your passkey.",
  "look": "Looking needs no account.",
  # G8 locked to an @name
  "g8_h": "A file for @dara", "g8_lede": "Only @dara can open it and keep it.", "g8_btn": "Open it as @dara",
  "g8_fine": "Your passkey shows it's you: it must be one shown on @dara's page. Nothing else is shared.",
  # G9 the gift page afterward
  "g9_h": "The gift page, afterward", "g9_lede": "What anyone else sees at the link later.",
  "g9_a": "Private, once it's kept", "g9_ah": "This was kept", "g9_ap": "It belongs to the person who kept it.",
  "g9_b": "Public, once it's kept", "g9_c": "Withdrawn before anyone kept it",
  # G10 kept
  "g10_h": "It's yours",
  "g10_lede": "It's in Your kept files, for good. It costs you nothing, and it's never removed because of a payment.",
  # G11 the receiver's list
  "g11_lede": "Files you keep here, and files given to you. Only you can open them.",
  "g11_rows": (("pic", "Picture · 2.4 MB", "given to you 17 Nov 2026 · a3f9 c2e1", None, ("Download", "Make public", "Thank them", "Remove")),
               ("voice", "Voice · 3.1 MB", "given to you 9 Nov 2026 · e44c 1b72", "You thanked them", ("Download", "Make public", "Remove"))),
  "thank_fine": "Thank them: one Kiitos, the way HeartBank® records a thank-you. Nothing is owed.",
  "gift_note": "A file given to you is never removed because of a payment. Only you can remove it.",
  # G12 the thank's return
  "g12_h": "Your thanks went to them",
  "g12_lede": "One Kiitos, recorded with your passkey. They'll see that the person who kept their file thanked them, and nothing else.",
  # G13 alerts
  "g13_h": "Settings", "g13_lede": "Alerts on your phone, if you turn them on.",
  "al_t": "Alerts on this phone", "al_s": "When a file you gave is kept, or you're thanked for one.",
  "al_ios": "On iPhone, alerts need this page on your Home Screen: tap Share, then Add to Home Screen, and open it from there.",
  "al_h": "What an alert says",
  "al_n": ("A file you gave was kept.", "You were thanked for a file you gave."),
  "al_fine": "Each alert says one fact, once.",
},
"km": {
  "date16": "១៦ វិច្ឆិកា ២០២៦", "signed": "បានចុះហត្ថលេខា", "check": "ពិនិត្យកំណត់ត្រារបស់វា", "kfiles": "ឯកសារដែលអ្នករក្សាទុក",
  "file": "sunflower.jpg · 2.4 MB",
  "loc_says": "រូបភាពនេះប្រាប់ពីកន្លែងដែលវាត្រូវបានថត។",
  "loc": "ដកកន្លែងដែលវាត្រូវបានថតចេញ",
  "loc_p": "ច្បាប់ចម្លងដែលអ្នកចុះហត្ថលេខា នឹងមិនប្រាប់ពីកន្លែងដែលវាត្រូវបានថតទេ។ ឯកសារដើមរបស់អ្នកនៅលើឧបករណ៍នេះ នៅតែប្រាប់ដដែល។",
  "g2_lede": "ឯកសារដែលអ្នករក្សាទុកនៅទីនេះ។ មានតែអ្នកទេដែលអាចបើកវាបាន។",
  "g2_rows": (("pic", "រូបភាព · 2.4 MB", "រក្សាទុក ១៦ វិច្ឆិកា ២០២៦ · a3f9 c2e1", None, ("ផ្ដល់ឱ្យ", "ទាញយក", "ដកចេញ")),
              ("video", "វីដេអូ · ១ នាទី ៤០ វិនាទី · 96 MB", "រក្សាទុក ១៤ វិច្ឆិកា ២០២៦ · 5d21 8e0b", "មានតំណអំណោយ", ("ចម្លងតំណ", "ដកវិញ")),
              ("doc", "PDF · 840 KB", "រក្សាទុក ១២ វិច្ឆិកា ២០២៦ · 07bd 5a90", "បានផ្ដល់ឱ្យហើយ", ()),
              ("voice", "សំឡេង · 3.1 MB", "រក្សាទុក ២ វិច្ឆិកា ២០២៦ · e44c 1b72", "បានផ្ដល់ឱ្យហើយ · បានទទួលការអរគុណ", ())),
  "g2_note": "ផ្ដល់ឱ្យ ផ្ញើឯកសារដែលអ្នករក្សាទុកទៅអ្នកផ្សេង។ ពេលពួកគេរក្សាវាទុក វាជារបស់ពួកគេ។",
  "g3_h": "ផ្ដល់ឯកសារនេះ", "g3_file": "វីដេអូ · ១ នាទី ៤០ វិនាទី · 96 MB", "g3_signed": "បានចុះហត្ថលេខា ១៤ វិច្ឆិកា ២០២៦",
  "who_h": "អ្នកណាអាចរក្សាវាទុក",
  "who1": "អ្នកណាក៏ដោយដែលមានតំណ", "who1p": "អ្នកដំបូងដែលរក្សាវាទុក មានវាជារៀងរហូត។ មុននោះ អ្នកអាចដកវាវិញបាន។",
  "who2": "តែ @name មួយប៉ុណ្ណោះ", "who2p": "ពួកគេបង្ហាញថាជាពួកគេ ដោយ passkey របស់ពួកគេ។",
  "name_h": "ឈ្មោះរបស់អ្នក",
  "name1": "ផ្ដល់ដោយគ្មានឈ្មោះ",
  "name1p": "ឈ្មោះរបស់អ្នកមិនត្រូវបានបង្ហាញទេ។ ប្រសិនបើអ្នកធ្លាប់ចែករំលែកហត្ថលេខា passkey របស់អ្នកជាមួយឯកសារនេះ ឬព័ត៌មានលម្អិតរបស់ឯកសារខ្លួនឯងមានឈ្មោះអ្នក នោះវានៅតែអាចបង្ហាញឈ្មោះអ្នកបាន។",
  "name2": "បង្ហាញ @name របស់ខ្ញុំ", "name2p": "អ្នកនឹងចុច passkey របស់អ្នក ដើម្បីបង្ហាញថាវាជារបស់អ្នក។",
  "vis_h": "អ្នកណាឃើញវា",
  "vis1": "ឯកជន", "vis1p": "ការមើលជាមុនរបស់តំណ មិនបង្ហាញរូបភាពទេ។ ពេលវាត្រូវបានរក្សាទុក តំណបង្ហាញតែថាវាត្រូវបានរក្សាទុកប៉ុណ្ណោះ។",
  "vis2": "សាធារណៈ", "vis2p": "ការមើលជាមុនបង្ហាញរូបភាព ហើយតំណនៅតែបង្ហាញឯកសារ រហូតដល់អ្នកដែលរក្សាវាទុកធ្វើឱ្យវាជាឯកជន។",
  "price": "ការផ្ដល់ឯកសារនេះ រក្សាវាទុកជារៀងរហូត។ ផ្នែកដែលលើសពីមួយនាទីឥតគិតថ្លៃ មានតម្លៃ $0.19 តែម្ដង ពីសមតុល្យរបស់អ្នក។ ការបង់ប្រាក់នេះនៅជាមួយឯកសារ៖ ការដកឯកសារចេញ មិនប្រគល់វាវិញទេ។",
  "give": "ផ្ដល់ឱ្យ", "give_fine": "បន្ទាប់មក អ្នកនឹងទទួលបានតំណដើម្បីផ្ញើ និងកូដដើម្បីបោះពុម្ព។",
  "g4_h": "ផ្ដល់ឱ្យ៖ ពេលជម្រើសមួយមិនអាចធ្វើបាន", "g4_lede": "ផ្ទាំងនេះប្រាប់ពីមូលហេតុម្ដង នៅកន្លែងដែលជម្រើសនោះគួរនៅ។",
  "g4_a": "ឯកសារដែលប្រាប់ពីកន្លែងដែលវាត្រូវបានថត", "g4_ap": "ឯកសារនេះប្រាប់ពីកន្លែងដែលវាត្រូវបានថត ដូច្នេះវាអាចផ្ដល់ឱ្យបានតែជាឯកជនប៉ុណ្ណោះ។",
  "g4_b": "@name ដែលទំព័ររបស់វាមិនបង្ហាញ passkey",
  "g4_bp": "អំណោយដែលចាក់សោទៅ @name មួយ ត្រូវការ passkey ដែលបង្ហាញនៅលើទំព័ររបស់ @name នោះ។ អ្នកអាចផ្ដល់វាដោយតំណជំនួសវិញ។",
  "g4_c": "សមតុល្យមិនអាចបង់បាន", "g4_cp": "សមតុល្យរបស់អ្នកមិនអាចបង់សម្រាប់ការនេះបានទេ។ គ្មានអ្វីត្រូវបានផ្ដល់ឱ្យទេ។", "g4_cb": "សមតុល្យរបស់អ្នក",
  "g5_h": "តំណរបស់អ្នក", "g5_lede": "ផ្ញើវា ឬបោះពុម្ពកូដរបស់វា។ អ្នកដែលរក្សាវាទុកមុនគេ មានវាជារៀងរហូត។",
  "copy": "ចម្លង", "share": "ចែករំលែក", "print": "បោះពុម្ព ឬរក្សាទុកវាជា B-QR",
  "qr_p": "កូដនេះគឺជាតំណ។ អ្នកណាដែលស្កេនវា អាចបើកឯកសារបាន។",
  "unlisted": "តំណនេះមិនត្រូវបានរាយនៅកន្លែងណាទេ។ មានតែអ្នកដែលអ្នកផ្ដល់វាឱ្យប៉ុណ្ណោះ ដែលអាចបើកវាបាន។",
  "withdraw": "រហូតដល់មាននរណាម្នាក់រក្សាវាទុក អ្នកអាចដកវាវិញពី ឯកសារដែលអ្នករក្សាទុក។",
  "g6_h": "របៀបដែលតំណមើលទៅក្នុងការជជែក", "g6_lede": "កាតនេះប្រាប់ថាតំណនេះជាអ្វី។ កាតនៃអំណោយឯកជនមិនមានរូបភាពទេ។",
  "priv": "ឯកជន", "pub": "សាធារណៈ", "from": "សុខា", "msg": "របស់មួយសម្រាប់អ្នក។",
  "pt": "ឯកសារមួយសម្រាប់អ្នក", "pf": "បើកវា ដើម្បីមើល និងរក្សាវាទុក។",
  "g6_ch": "កម្មវិធីជជែកជាអ្នកបង្កើតកាត",
  "g6_cp": "ដើម្បីគូរកាត កុំព្យូទ័ររបស់កម្មវិធីជជែកខ្លួនឯងបើកតំណ។ នោះហើយជាមូលហេតុដែលកាតនៃអំណោយឯកជន មិនដែលបង្ហាញរូបភាពរបស់វា។",
  "g7_h": "ឯកសារមួយសម្រាប់អ្នក", "keep": "រក្សាវាទុក",
  "keep_fine": "វាក្លាយជារបស់អ្នកជារៀងរហូត ហើយមិនគិតថ្លៃអ្វីពីអ្នកទេ។ អ្នកនឹងចូលដោយ passkey របស់អ្នក។",
  "look": "ការមើល មិនត្រូវការគណនីទេ។",
  "g8_h": "ឯកសារមួយសម្រាប់ @dara", "g8_lede": "មានតែ @dara ទេដែលអាចបើក និងរក្សាវាទុកបាន។", "g8_btn": "បើកវាជា @dara",
  "g8_fine": "passkey របស់អ្នកបង្ហាញថាជាអ្នក៖ វាត្រូវតែជា passkey មួយដែលបង្ហាញនៅលើទំព័ររបស់ @dara។ គ្មានអ្វីផ្សេងទៀតត្រូវបានចែករំលែកទេ។",
  "g9_h": "ទំព័រអំណោយ ពេលក្រោយ", "g9_lede": "អ្វីដែលអ្នកផ្សេងឃើញនៅតំណនោះ នៅពេលក្រោយ។",
  "g9_a": "ឯកជន ពេលវាត្រូវបានរក្សាទុក", "g9_ah": "ឯកសារនេះត្រូវបានរក្សាទុកហើយ", "g9_ap": "វាជារបស់អ្នកដែលបានរក្សាវាទុក។",
  "g9_b": "សាធារណៈ ពេលវាត្រូវបានរក្សាទុក", "g9_c": "បានដកវិញ មុនពេលនរណាម្នាក់រក្សាវាទុក",
  "g10_h": "វាជារបស់អ្នក",
  "g10_lede": "វានៅក្នុង ឯកសារដែលអ្នករក្សាទុក ជារៀងរហូត។ វាមិនគិតថ្លៃអ្វីពីអ្នកទេ ហើយវាមិនដែលត្រូវបានដកចេញដោយសារការបង់ប្រាក់ទេ។",
  "g11_lede": "ឯកសារដែលអ្នករក្សាទុកនៅទីនេះ និងឯកសារដែលគេផ្ដល់ឱ្យអ្នក។ មានតែអ្នកទេដែលអាចបើកវាបាន។",
  "g11_rows": (("pic", "រូបភាព · 2.4 MB", "បានផ្ដល់ឱ្យអ្នក ១៧ វិច្ឆិកា ២០២៦ · a3f9 c2e1", None, ("ទាញយក", "ធ្វើជាសាធារណៈ", "អរគុណពួកគេ", "ដកចេញ")),
               ("voice", "សំឡេង · 3.1 MB", "បានផ្ដល់ឱ្យអ្នក ៩ វិច្ឆិកា ២០២៦ · e44c 1b72", "អ្នកបានអរគុណពួកគេ", ("ទាញយក", "ធ្វើជាសាធារណៈ", "ដកចេញ"))),
  "thank_fine": "អរគុណពួកគេ៖ Kiitos មួយ ដែលជារបៀបដែល HeartBank® កត់ត្រាការអរគុណ។ មិនជំពាក់អ្វីទេ។",
  "gift_note": "ឯកសារដែលគេផ្ដល់ឱ្យអ្នក មិនដែលត្រូវបានដកចេញដោយសារការបង់ប្រាក់ទេ។ មានតែអ្នកទេដែលអាចដកវាចេញបាន។",
  "g12_h": "ការអរគុណរបស់អ្នកបានទៅដល់ពួកគេ",
  "g12_lede": "Kiitos មួយ ត្រូវបានកត់ត្រាដោយ passkey របស់អ្នក។ ពួកគេនឹងឃើញថា អ្នកដែលបានរក្សាឯកសាររបស់ពួកគេបានអរគុណពួកគេ ហើយគ្មានអ្វីផ្សេងទៀតទេ។",
  "g13_h": "ការកំណត់", "g13_lede": "ការជូនដំណឹងនៅលើទូរសព្ទរបស់អ្នក ប្រសិនបើអ្នកបើកវា។",
  "al_t": "ការជូនដំណឹងនៅលើទូរសព្ទនេះ", "al_s": "ពេលឯកសារដែលអ្នកបានផ្ដល់ឱ្យត្រូវបានរក្សាទុក ឬពេលអ្នកទទួលបានការអរគុណសម្រាប់វា។",
  "al_ios": "នៅលើ iPhone ការជូនដំណឹងត្រូវការទំព័រនេះនៅលើ Home Screen របស់អ្នក៖ ចុច Share បន្ទាប់មក Add to Home Screen ហើយបើកវាពីទីនោះ។",
  "al_h": "អ្វីដែលការជូនដំណឹងនិយាយ",
  "al_n": ("ឯកសារដែលអ្នកបានផ្ដល់ឱ្យ ត្រូវបានរក្សាទុកហើយ។", "អ្នកទទួលបានការអរគុណ សម្រាប់ឯកសារដែលអ្នកបានផ្ដល់ឱ្យ។"),
  "al_fine": "ការជូនដំណឹងនីមួយៗ និយាយការពិតមួយ ម្ដង។",
},
}


def _kp(d):
    """The keep-a-copy words in the same language (shared with kept_boards)."""
    return KP.DT["km" if d is DT["km"] else "en"]


def _bl(d):
    return BL.DT["km" if d is DT["km"] else "en"]


def gspot(kind, px=44):
    """Small flat drawings from the board's own tokens."""
    if kind == "pic":
        return '<div class="kthumb">%s</div>' % sunflower(px)
    if kind in ("doc", "voice"):
        return KP.kspot(kind)
    s = ['<svg class="kicon" width="%d" height="%d" viewBox="0 0 44 44" aria-hidden="true">' % (px, px)]
    if kind == "video":
        s += ['<rect x="3" y="7" width="38" height="30" rx="6" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<circle cx="22" cy="22" r="9" fill="var(--accent)"/>', '<path d="M19 17 v10 l9 -5 z" fill="var(--accent-ink)"/>']
    elif kind == "lock":
        s = ['<svg class="glock" width="88" height="88" viewBox="0 0 88 88" aria-hidden="true">',
             '<rect x="18" y="38" width="52" height="40" rx="10" fill="var(--wash)" stroke="var(--accent)" stroke-width="2.5"/>',
             '<path d="M30 38 V28 a14 14 0 0 1 28 0 V38" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>',
             heart(44, 57, 1.1)]
    s.append('</svg>')
    return "".join(s)


def _opt(title, sub, on=False, extra=""):
    return ('<div class="gopt"><span class="grad%s"></span><div class="gtx"><div class="t">%s</div><div class="s">%s</div>%s</div></div>'
            % (" on" if on else "", title, sub, extra))


def _opt_off(title, sub, why):
    return ('<div class="gopt off"><span class="grad"></span><div class="gtx"><div class="t">%s</div><div class="s">%s</div></div></div>'
            '<div class="note">%s</div>' % (title, sub, why))


def _record(d):
    return ('<div class="card"><div class="row"><div><div class="t">%s</div></div><span class="s">%s</span></div>'
            '<p class="fine" style="margin-top:6px"><span class="link">%s</span></p></div>' % (d["signed"], d["date16"], d["check"]))


def _rows(rows, d):
    out = []
    for kind, a, b, stat, acts in rows:
        out.append('<div class="row krowf">%s<div class="kmeta"><div class="t">%s</div><div class="s mono">%s</div>%s</div>'
                   '<div class="kact">%s</div></div>'
                   % (gspot(kind), a, b, '<span class="gstat">%s</span>' % stat if stat else "",
                      "".join('<span class="pillbtn%s">%s</span>' % ("" if i == 0 else " ghost", x) for i, x in enumerate(acts))))
    return '<div class="card">%s</div>' % "".join(out)


def G1(t, d):
    k = _kp(d)
    locbox = ('<div class="card kkeep"><p class="fine" style="margin:0 0 8px">%s</p><label class="krow"><span class="kbox"></span><b>%s</b></label>'
              '<p>%s</p></div>' % (d["loc_says"], d["loc"], d["loc_p"]))
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (k["k1_h"], k["public"])
            + '<div class="card"><div class="thumb">%s<div class="mono">%s</div></div></div>' % (sunflower(48), d["file"])
            + locbox + KP._keepbox(k) + '<p class="fine">%s</p>' % k["privacy"]
            + '<div class="grow"></div><button class="btn">%s%s</button><p class="fine">%s</p>' % (KEY, k["go"], k["go_fine"]))


def G2(t, d):
    k = _kp(d)
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["kfiles"], d["g2_lede"]) + _rows(d["g2_rows"], d)
            + '<p class="fine">%s</p>' % d["g2_note"] + KP._paid(k))


def G3(t, d):
    head = ('<div class="card"><div class="row krowf">%s<div class="kmeta"><div class="t">%s</div><div class="s">%s</div></div></div></div>'
            % (gspot("video"), d["g3_file"], d["g3_signed"]))
    lock = '<div class="field mono gfield">@</div>'
    return ("<h1>%s</h1>" % d["g3_h"] + head
            + '<div class="kcap">%s</div><div class="card">%s%s</div>' % (d["who_h"], _opt(d["who1"], d["who1p"], True), _opt(d["who2"], d["who2p"], extra=lock))
            + '<div class="kcap">%s</div><div class="card">%s%s</div>' % (d["name_h"], _opt(d["name1"], d["name1p"], True), _opt(d["name2"], d["name2p"]))
            + '<div class="kcap">%s</div><div class="card">%s%s</div>' % (d["vis_h"], _opt(d["vis1"], d["vis1p"], True), _opt(d["vis2"], d["vis2p"]))
            + '<div class="note">%s</div>' % d["price"]
            + '<button class="btn">%s</button><p class="fine">%s</p>' % (d["give"], d["give_fine"]))


def G4(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g4_h"], d["g4_lede"])
            + '<div class="kcap">%s</div><div class="card">%s%s</div>' % (d["g4_a"], _opt(d["vis1"], d["vis1p"], True), _opt_off(d["vis2"], d["vis2p"], d["g4_ap"]))
            + '<div class="kcap">%s</div><div class="card">%s<div class="field mono gfield">@dara</div><p class="fine">%s</p></div>'
            % (d["g4_b"], _opt(d["who2"], d["who2p"], True), d["g4_bp"])
            + '<div class="kcap">%s</div><div class="card"><p>%s</p><span class="pillbtn">%s</span></div>' % (d["g4_c"], d["g4_cp"], d["g4_cb"]))


def G5(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g5_h"], d["g5_lede"])
            + '<div class="glink">%s</div>' % LINK + btns(d["copy"], d["share"])
            + '<div class="card" style="text-align:center;margin-top:14px">%s<span class="pillbtn">%s</span><p class="fine" style="margin-top:8px">%s</p></div>'
            % (BQR_SVG, d["print"], d["qr_p"])
            + '<p class="fine">%s</p><p class="fine">%s</p>' % (d["unlisted"], d["withdraw"]))


def _chat(d, cover):
    return ('<div class="chat"><div class="who">%s</div><div class="bub">%s</div>'
            '<div class="pcard">%s<div class="pt">%s</div><div class="pf">%s</div><div class="ph">B.333.eco</div></div></div>'
            % (d["from"], d["msg"], cover, d["pt"], d["pf"]))


def G6(t, d):
    pub_cover = '<div class="gcover">%s</div>' % sunflower(150)
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g6_h"], d["g6_lede"])
            + '<div class="kcap">%s</div>' % d["priv"] + '<div class="gpriv">%s</div>' % _chat(d, "")
            + '<div class="kcap">%s</div>' % d["pub"] + _chat(d, pub_cover)
            + card(d["g6_ch"], d["g6_cp"], "two"))


def G7(t, d):
    return ("<h1>%s</h1>" % d["g7_h"] + '<div class="gbig">%s</div>' % sunflower(200) + _record(d)
            + '<div class="grow"></div><button class="btn">%s%s</button>' % (KEY, d["keep"])
            + '<p class="fine">%s</p><p class="fine">%s</p>' % (d["keep_fine"], d["look"]))


def G8(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g8_h"], d["g8_lede"])
            + '<div class="card" style="text-align:center">%s</div>' % gspot("lock")
            + '<div class="grow"></div><button class="btn">%s%s</button><p class="fine">%s</p>' % (KEY, d["g8_btn"], d["g8_fine"]))


def G9(t, d):
    b = _bl(d)
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g9_h"], d["g9_lede"])
            + '<div class="kcap">%s</div><div class="card"><h2>%s</h2><p>%s</p></div>' % (d["g9_a"], d["g9_ah"], d["g9_ap"])
            + '<div class="kcap">%s</div><div class="card"><div class="row krowf">%s<div class="kmeta"><div class="t">%s</div>'
              '<div class="s">%s · <span class="link">%s</span></div></div></div></div>'
            % (d["g9_b"], gspot("pic"), d["pt"], d["date16"], d["check"])
            + '<div class="kcap">%s</div><div class="card"><h2>%s</h2><p>%s</p></div>' % (d["g9_c"], b["b4_h"], b["b4_p"]))


def G10(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g10_h"], d["g10_lede"])
            + '<div class="card"><div class="row krowf">%s<div class="kmeta"><div class="krow">%s<b>%s</b></div><div class="s">%s %s</div></div></div></div>'
            % (gspot("pic"), OK, d["pt"], d["signed"], d["date16"])
            + '<div class="grow"></div>' + btns(d["kfiles"]))


def G11(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["kfiles"], d["g11_lede"]) + _rows(d["g11_rows"], d)
            + '<p class="fine">%s</p><p class="fine">%s</p>' % (d["thank_fine"], d["gift_note"]))


def G12(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g12_h"], d["g12_lede"])
            + '<div class="card" style="text-align:center"><svg width="120" height="80" viewBox="0 0 120 80" aria-hidden="true">'
            + '<circle cx="60" cy="40" r="32" fill="var(--wash)"/>' + heart(60, 40, 2.2) + '</svg></div>'
            + '<div class="grow"></div>' + btns(d["kfiles"]))


def G13(t, d):
    sw = ('<div class="card"><div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><span class="gtog"></span></div>'
          '<p class="fine" style="margin-top:8px">%s</p></div>' % (d["al_t"], d["al_s"], d["al_ios"]))
    ls = "".join('<div class="gnt"><div class="gnh">origin.333.eco</div>%s</div>' % n for n in d["al_n"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["g13_h"], d["g13_lede"]) + sw
            + '<div class="kcap">%s</div><div class="gls">%s</div><p class="fine">%s</p>' % (d["al_h"], ls, d["al_fine"]))


SCREENS = [  # (id, page, title, render(t, d))
    ("G1", "origin", "Give · Sign a file: remove where it was taken (unticked)", G1),
    ("G2", "origin", "Give · Your kept files: Give, Offered, Given, Thanked", G2),
    ("G3", "origin", "Give · the sheet (above the free minute)", G3),
    ("G4", "origin", "Give · when a choice can't be made", G4),
    ("G5", "origin", "Give · your link and its code", G5),
    ("G6", "origin", "Give · the link's card in a chat: private and public", G6),
    ("G7", "origin", "Give · the gift page (anyone with the link)", G7),
    ("G8", "origin", "Give · the gift page, locked to an @name", G8),
    ("G9", "origin", "Give · the gift page afterward: kept (private, public) · withdrawn", G9),
    ("G10", "origin", "Give · kept: it's yours", G10),
    ("G11", "origin", "Give · Your kept files: given to you, Thank them", G11),
    ("G12", "origin", "Give · back from the thank's press", G12),
    ("G13", "origin", "Give · alerts in Settings", G13),
]
PUBLIC = set()  # a gift page is shared by its giver's link, never by a share button (Default 8)
CSS = """
.gopt{display:flex;gap:12px;align-items:flex-start;padding:10px 0}
.gopt+.gopt{border-top:1px solid var(--line)}
.gopt.off{opacity:.45}
.gtx{flex:1;min-width:0}
.grad{flex:none;width:20px;height:20px;border-radius:50%;border:2px solid var(--line-strong);margin-top:2px;box-sizing:border-box;background:var(--surface)}
.grad.on{border:6px solid var(--accent)}
.gfield{margin-top:8px;width:100%;box-sizing:border-box;color:var(--ink-dim)}
.gstat{display:inline-block;font-size:12px;font-weight:600;padding:2px 10px;margin-top:5px;border-radius:var(--r-pill);background:var(--wash);color:var(--ink)}
.glink{font-family:var(--font-mono,monospace);font-size:13px;padding:12px;margin:0 0 12px;border-radius:12px;border:1px solid var(--line-strong);background:var(--surface-2);word-break:break-all;color:var(--ink)}
.gbig{width:200px;height:200px;margin:4px auto 16px;border-radius:16px;overflow:hidden}
.gcover{display:flex;justify-content:center;background:var(--wash);padding:9px 0}
.glock{display:block;margin:6px auto}
.bqr{display:block;margin:2px auto 12px}
.gtog{flex:none;width:46px;height:28px;border-radius:14px;background:var(--line-strong);position:relative}
.gtog::after{content:"";position:absolute;left:3px;top:3px;width:22px;height:22px;border-radius:50%;background:var(--surface)}
.gls{padding:14px;border-radius:var(--r);background:var(--surface-2);border:1px solid var(--line)}
.gnt{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:10px 12px;font-size:14px;color:var(--ink);margin:0 0 8px}
.gnt:last-child{margin:0}
.gnh{font-size:12px;color:var(--ink-faint);margin:0 0 3px}
"""
BARRED = KP.BARRED + [  # words this surface must never draw
    (r"\bopened\b|\bunopened\b|not kept|not thanked|\bwaiting\b|haven.t|\bnot yet\b", "never an absence: say what happened, never what didn't (Sig-8)"),
    (r"\bverified\b|\bdeposit|\binterest\b|\bsavings\b|\byield\b", "no 'verified', no banking words (Default 2, B-Origin)"),
    (r"say thanks|don.t forget|\bplease thank\b", "the thank is offered, never pressed on anyone"),
]


def check(sid, body):
    for pat, why in BARRED:
        assert not re.search(pat, body, re.I), "%s: %s" % (sid, why)
    km = "ឯកសារ" in body
    if sid == "G3" and not km:
        for label in ("Anyone with the link", "Give without a name", "Private"):
            assert re.search(r'<span class="grad on"></span><div class="gtx"><div class="t">%s<' % re.escape(label), body), \
                "G3: '%s' must be the default (the quiet choice)" % label
        assert body.count('class="grad on"') == 3, "G3: exactly one default per choice"
    if sid == "G3":
        assert "$0.19" in body, "G3: above the free minute, the price is said once"
    if sid == "G6":
        priv = body.split('<div class="gpriv">', 1)[1].split('<div class="kcap">', 1)[0]
        assert "<svg" not in priv and "gcover" not in priv, "G6: a private gift's card has no picture"
    if sid in ("G7", "G8", "G9", "G10", "G12"):
        assert not re.search(r"\bfrom @|\bពី @", body, re.I), "%s: an anonymous gift names no one" % sid
    if sid == "G12":
        assert "@" not in body, "G12: the thank's return names no one"
    if sid == "G5":
        assert 'class="bqr"' in body and 'clip-path="url(#bqrc0)"' in body and 'class="qr"' not in body, "G5: the code is a B-QR from the recipe, never a plain QR"
    if sid in ("G5", "G6", "G7", "G8", "G9"):
        assert not re.search(r"thank them|អរគុណពួកគេ", body, re.I), "%s: the thank lives on the kept file, never on the link" % sid
