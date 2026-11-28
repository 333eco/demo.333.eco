"""The B-PoH℠ app, Android version 0 (roadmap A666; the spec is private: 333eco/poh.333.eco SPEC.md, milestone P3, written
2026-11-25; founder 2026-11-25: "go per your recommendation"). Imported by build-boards.py, which injects the shared helpers.

A NATIVE app, so these boards get their own frame (status bar, app bar, gesture bar; no web header or footer). The one web page
among them, P2, is sign.333.eco opened in a Custom Tab inside the app, and carries sign.333.eco's own header and footer.
Sheets the PHONE draws (its fingerprint prompt, its passkey sheet) are drawn stand-ins, named so in each board's title; the
words inside the fingerprint prompt are ours (the app sets them).

Copy rules this file must keep (checked at build time by check()):
  - A press shows that a key in a phone's chip pressed, unlocked by a finger or a PIN. ⛔ Never a fact about the PERSON:
    no "verified", no "human", no "proves who"; never "bank-level". ⛔ Never "sign in" (Default 10).
  - Presence only (Sig-8): no count, no "last used", no time remaining, no "not pressed". A date is stated once, as a date.
  - No phone maker or model, no chip jargon (TEE, StrongBox, KeyMint), no package name or signing digest: this repo is public.
  - Not in v0, so never drawn: a wallet, money, uniqueness, voting, B-Vouch, a password manager.
  - A provider press (P13) says the WEBSITE showed the words and this app can't see them (SPEC §10 F1+F4: shown "site").
  - Live sign.333.eco words are copied word for word where they exist (src/sign-text.ts and app.ts, 2026-11-25): "Confirm with
    your passkey", "Not now", "New here? Make a passkey", "Nothing was signed.", "Signed", "{app} asks you to sign:", the field
    labels. (Khmer: *Confirm with your passkey* follows the sign page's own word, passkey, not CONFIRM_TEXT's សោសម្ងាត់; the live
    pages differ, a question for the native readers.) ⚠️ Its live footer says "only a passkey can sign", which stops being true when app keys sign; P2 draws it without
    that clause, and the live footer is owed a change at the app's release.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board. The not-a-chartered-bank paragraph stays in
English on the Khmer boards (Default 3: no disclosure in unreviewed Khmer).
"""
import io, os, re

card = btns = spot = heart = person = EMBLEM = None   # injected by build-boards.py
HERE = os.path.dirname(os.path.abspath(__file__))
BQR = io.open(os.path.join(HERE, "marks-bqr.svg"), encoding="utf-8").read().replace(' shape-rendering="crispEdges"', "")
BQR = re.sub(r'<g clip-path="url\(#bqrc1\)">.*?</g>', "", BQR, count=1, flags=re.S)  # a handoff code carries no B-Autograph (that is a mark's)
assert "bqrc1)" not in BQR, "the autograph group is gone from the handoff code"

DISCLAIMER = ("HeartBank® is a data bank of gratitude, not a chartered bank or financial institution; it does not provide banking "
              "services, hold deposits, or extend credit. Nothing is paid or held in this app.")

DT = {
"en": {
  "app": "B-PoH℠", "time": "9:41", "settings": "Settings", "close": "Close", "back": "Back",
  "lang": ("EN", "ខ្មែរ"), "theme": ("System", "Light", "Dark"),
  # P1 first open
  "p1_h": "A press made in this phone's own chip",
  "p1_lede": "B-PoH℠ signs with a key inside this phone's secure chip. Each press signs the exact words the app shows you, unlocked by your finger or your phone's PIN.",
  "p1_c1h": "The words, then the press", "p1_c1p": "You read what you are signing on this screen, then press once. The press signs those words and nothing else.",
  "p1_c2h": "Keys that never leave", "p1_c2p": "The keys are made inside the chip and can't be copied out of it. The finger key ends if a new finger or face is added to this phone.",
  "p1_c3h": "What a press shows", "p1_c3p": "That a key in a phone's chip pressed, unlocked by a finger or a PIN. Not who is holding the phone.",
  "p1_go": "Add this phone", "p1_fine": "Your passkey stays your way in. B-PoH adds to it.", "by": "Published by HeartBank®",
  # P2 sign.333.eco/enroll, in a Custom Tab
  "host": "sign.333.eco", "p2_h": "Add this phone", "p2_from": "Asked by the B-PoH℠ app on this phone",
  "p2_lede": "Your passkey confirms it's you. Then the app makes its keys in this phone's own chip, to sign with.",  # 2026-11-28: a PIN-only phone makes one key (P4b), so never "two"
  "p2_ch": "Only a press can add a phone", "p2_cp": "Your passkey, or another phone that already has B-PoH, can add this one. Logging in alone never can.",
  "p2_go": "Confirm with your passkey", "p2_other": "Approve from another phone of yours", "p2_new": "New here? Make a passkey", "no": "Not now",
  "p2_foot": "sign.333.eco · no passwords",
  "p2b_h": "Approve from another phone",
  "p2b_lede": "On a phone you've already added, open B-PoH, tap Scan a code, and scan this code. Keep the two phones together.",
  "p2b_ch": "Why the phones must be together", "p2b_cp": "The other phone checks by Bluetooth that it is next to this one, so a code sent from somewhere else can't add a stranger's phone.",
  "p2b_alt": "Use your passkey instead",
  "p19_ask": "sign.333.eco asks you to approve:", "p19_f": ("What", "It will"),
  "p19_v": ("Add the phone you just scanned to your account", "Make its own finger key and PIN key, and press for you"),
  "p19_fine": "Approve only a phone you are holding. It never gets this phone's keys.",
  "p12b_h": "forum.example.org asks for a passkey made in this phone's chip",
  "p12b_lede": "The website receives this phone's proof that the key was made in its chip.",
  "p12b_c1h": "What the proof also shows", "p12b_c1p": "This phone's Android version and last security update, and on some phones the batch it was made in. It doesn't name this phone. If you'd rather the website didn't see this, go back and choose your usual passkey manager.",
  "p12b_c2h": "It stays on this phone", "p12b_c2p": "This passkey can't be copied to another device. If you lose this phone, it is gone too, so keep another way into forum.example.org.",
  "p12b_go": "Make it with your finger", "p12b_go_pin": "Make it with your PIN",  # the PIN key alone's button (founder 2026-11-27: a PIN-only phone makes it with the PIN)
  "p12b_fine": "Made with your finger, it ends if a new finger or face is added to this phone. Made with your PIN, it stays.",  # SPEC §4: made like the press keys
  "p4b_h": "This phone is added, with a PIN key",
  "p4b_lede": "This phone has no fingerprint or face sensor strong enough for a finger key, so it presses with your PIN.",
  "p4b_ch": "Every press says which key pressed", "p4b_cp": "Some websites may ask for a finger press, and this phone can't give one. Everything else works the same.",
  "p20_h": "This phone needs adding again",
  "p20_lede": "Your account was opened with a text message, so this phone's keys have ended. A text message can never add a phone.",
  "p20_ch": "Add it again with a passkey",
  "p20_cp": "A passkey you still have can add it now. A passkey made after the text message can add it after a waiting period, told first to every address linked to your account, so it can be stopped if it wasn't you.",
  "p20_go": "Add this phone again", "p20_fine": "If this wasn't you, someone may be using your phone number. Your records are unchanged.",
  "p2c_h": "This phone can be added on 2 Dec 2026",
  "p2c_lede": "Your account was opened with a text message on 25 Nov 2026. A passkey made after that adds a phone only after a waiting period, so we told every address linked to your account first.",
  "p2c_ch": "If this wasn't you", "p2c_cp": "Someone may be using your phone number. The message we sent says how to stop it.",
  # P21–P23 a lost or stolen phone, on sign.333.eco (live words: src/app.ts ACCOUNT_TEXT — title, Remove, Added, This one)
  "acct_h": "Your passkeys", "acct_this": "This one", "acct_added": "Added", "acct_remove": "Remove",
  "acct_pk": "My laptop", "acct_pkd": "Added 3 Nov 2026",
  "acct_ph": "Phones with B-PoH", "acct_phone": "A phone", "acct_phoned": "Added 25 Nov 2026 · finger key and PIN key",
  "acct_lost": "Lost or stolen?",
  "acct_which": "Remove a phone you still have and no longer use. If it was lost or stolen, report it instead: that also covers what its keys pressed since you last had it.",
  "p22_h": "Report a lost or stolen phone", "p22_when": "When did you last have it?", "p22_day": "25 Nov 2026", "p22_time": "18:00",
  "p22_ch": "What becomes public", "p22_cp": "A public record that this phone's keys were reported, and the time you give. Presses its keys made from then on are no longer backed by what its chip showed; presses before it are unchanged. If you shared presses made on this phone, anyone holding them can see they came from the same phone. It can't be undone.",
  "p22_go": "Report it with your passkey",
  "p23_h": "Reported", "p23_lede": "This phone's keys are ended. They can't press again.",
  "p23_ch": "On the public record", "p23_cp": "From 25 Nov 2026, 18:00, presses by this phone's keys are no longer backed by what its chip showed. Presses before that are unchanged. The record names the keys, never you.",
  "p23_go": "Back to your passkeys", "p23_new": "Add a new phone",
  # P3 making the two keys
  "p3_h": "Making your two keys",
  "p3_steps": ("Your passkey confirmed it's you", "Finger key: touch the sensor", "PIN key: then enter your PIN", "sign.333.eco reads this phone's proof"),
  "p3_sys_h": "Make your finger key", "p3_sys_sub": "B-PoH℠ · for sign.333.eco", "touch": "Touch the fingerprint sensor", "cancel": "Cancel",
  # P4 added
  "p4_h": "This phone is added", "p4_lede": "It can now press for you, with your finger or your PIN.",
  "p4_read": "What sign.333.eco read from this phone's proof",
  "p4_reads": ("The keys were made inside this phone's secure chip, and can't leave it.", "The phone is running its maker's own software.", "This is the app HeartBank® publishes."),
  "p4_not": "It says nothing about who is holding the phone.",
  "p4_kh": "A statement about these keys", "p4_kp": "sign.333.eco signed what it read, and this phone keeps it. It is shown only when you share a press. The statement itself is not published.",
  "done": "Done",
  # P5 home
  "p5_ready": "This phone can press for you.", "p5_scan": "Scan a code", "p5_scan_s": "When another screen asks you to press",
  "p5_ph": "Your presses, kept on this phone", "p5_list": (("Sign this file", "origin.333.eco · 25 Nov"), ("Confirm it's you", "origin.333.eco · 24 Nov")),
  "p5_fine": "Only you see this list.", "keys": "Your keys", "keys_s": "Finger key · PIN key",
  # P6 the words (live labels: sign-text.ts SIGN_TEXT)
  "ask": "origin.333.eco asks you to sign:",
  "f_file": "File", "f_size": "Size", "f_fp": "Fingerprint", "f_how": "How it was made", "f_rights": "Share it under",
  "w1": ("sunflower.jpg", "3.1 MB", "c8e1 04ab … 9d37", "Photo or recording", "All rights reserved"),
  "p6_pub": "This adds a public record: when it was signed and how it was made. It shows that a key in a phone's chip signed it, not who imagined it.",
  "go_finger": "Press with your finger", "go_pin": "Use your PIN instead",
  "nothing": "Nothing was signed.",
  # P7 the phone's own prompt (title, subtitle, words and the second button are ours)
  "p7_sys_h": "Sign these exact words", "p7_sys_sub": "Asked by origin.333.eco",
  "pin_enter": "Enter your PIN", "p8_pin": "Pressed with your PIN key",
  # P8 signed (live: SIGN_TEXT done / doneLede)
  "p8_h": "Signed", "p8_lede": "Your signature is saved. It joins the public log within the hour.",
  "p8_ch": "Pressed with your finger key", "p8_cp": "The record says a key in this phone's chip pressed, unlocked by a finger. It never says who you are.",
  "p8_go": "Back to origin.333.eco",
  # P9 scan
  "p9_lede": "Point this phone at the code on the screen that asked.",
  "p9_ch": "Keep the two together", "p9_cp": "This phone checks by Bluetooth that it is near that screen, so a code passed along from somewhere else can't be pressed.",
  # P10 another screen's words
  "p10_from": "On the computer next to you", "near": "Near this phone",
  "p10_sealed": "These words came from that screen, sealed so only this phone could open them.",
  "w2": ("harvest.png", "2.4 MB", "5b0e 91c2 … 44af", "Made by hand on a device", "All rights reserved"),
  # P11 not near
  "p11_h": "This phone isn't near the screen that asked",
  "p11_lede": "A press made away from that screen could be a code someone passed along, so this one can't go ahead. Nothing was signed.",
  "p11_ch": "Bring them together", "p11_cp": "Take this phone to that screen and scan again. Or press on that screen itself, with your passkey.",
  "p11_go": "Scan again",
  # P12 the phone's passkey sheet (Android 14+)
  "site": "forum.example.org", "p12_page": "Make your account here", "p12_sys_h": "Make a passkey for forum.example.org?",
  "p12_o1s": "In this phone's chip", "p12_o2": "Your usual passkey manager", "cont": "Continue",
  # P13 the app's provider screen
  "p13_h": "forum.example.org asks for a press",
  "p13_lede": "Its own page shows what you are pressing for. This app can't see those words, so read them there before you press.",
  "p13_ch": "The record will say so", "p13_cp": "It says the website showed the words, not this app.",
  # P14 your keys
  "p14_g1": "In this phone's chip",
  "p14_rows": (("Finger key", "Made 25 Nov 2026 · Ends if a new finger or face is added to this phone"), ("PIN key", "Made 25 Nov 2026 · Stays when a finger or face is added")),
  "p14_g2": "Passkeys this app made for websites", "p14_site": ("forum.example.org", "Made 25 Nov 2026"),
  "p14_note": "Your passkey stays your way in, on every device. These keys add to it.", "remove": "Remove this phone",
  # P15 the finger key ended
  "p15_h": "Your finger key has ended",
  "p15_lede": "This key can't press again: a new finger or face was added to this phone, or its screen lock was removed. That is how it keeps out a finger that isn't yours.",  # founder 2026-11-27 "3: yes" (removing the lock ends it too, measured L1)
  "p15_ch": "Your PIN key still works", "p15_cp": "You can press with your PIN now. To make a new finger key, confirm with your passkey, or from another phone of yours.",
  "p15_go": "Make a new finger key", "p15_fine": "Your passkey and your records are unchanged.",
  # P16 remove
  "p16_h": "Remove this phone?",
  "p16_p": "Its finger key and PIN key end, and so do the passkeys it made for websites. Your passkey, your account and your records stay.",
  "keep": "Keep it",
  # P17 settings
  "p17_lang": "Language", "p17_look": "Appearance", "p17_web": "Websites",
  "p17_web_t": "Make passkeys for websites that ask",
  "p17_web_s": "Only when a website asks for a key from a phone's chip. Every other website keeps your usual passkey manager.",
  "p17_web_go": "Open the phone's passkey settings", "p17_about": "About", "privacy": "Privacy",
  # P18 when a phone can't be added
  "p18_h": "When a phone can't be added",
  "p18_c1": "When the phone's software was changed", "p18_c1h": "This phone can't hold B-PoH keys",
  "p18_c1p": "Its proof says it isn't running its maker's own software, so the keys in its chip can't be shown to be its own. Your passkey still works everywhere it did.",
  "p18_c2": "When the phone has no screen lock", "p18_c2h": "Turn on a screen lock first",
  "p18_c2p": "These keys unlock only with a PIN, or a finger set up on this phone. Set one in the phone's settings, then add the phone again.",
  "p18_c3": "When your account holds all the phones it can", "p18_c3h": "Remove a phone first",
  "p18_c3p": "Your account holds as many phone keys as it can. Remove one you no longer use, in Your keys, then add this one.",
  "p18_c4": "When adding phones is paused", "p18_c4t": "Adding phones is paused right now. Nothing changed. Try again later.",
},
"km": {
  "app": "B-PoH℠", "time": "9:41", "settings": "ការកំណត់", "close": "បិទ", "back": "ត្រឡប់ក្រោយ",
  "lang": ("EN", "ខ្មែរ"), "theme": ("ប្រព័ន្ធ", "ភ្លឺ", "ងងឹត"),
  "p1_h": "ការចុច​ដែល​ធ្វើ​ឡើង​ក្នុង​បន្ទះឈីប​របស់​ទូរស័ព្ទ​នេះ​ផ្ទាល់",
  "p1_lede": "B-PoH℠ ចុះហត្ថលេខាដោយសោមួយនៅក្នុងបន្ទះឈីបសុវត្ថិភាពរបស់ទូរស័ព្ទនេះ។ ការចុចនីមួយៗចុះហត្ថលេខាលើពាក្យពិតប្រាកដដែលកម្មវិធីបង្ហាញអ្នក ដោយដោះសោដោយម្រាមដៃរបស់អ្នក ឬលេខកូដ PIN របស់ទូរស័ព្ទ។",
  "p1_c1h": "ពាក្យមុន បន្ទាប់មកការចុច", "p1_c1p": "អ្នកអានអ្វីដែលអ្នកកំពុងចុះហត្ថលេខានៅលើអេក្រង់នេះ រួចចុចម្តង។ ការចុចចុះហត្ថលេខាលើពាក្យទាំងនោះ ហើយគ្មានអ្វីផ្សេងទៀតទេ។",
  "p1_c2h": "សោដែលមិនដែលចាកចេញ", "p1_c2p": "សោត្រូវបានបង្កើតនៅក្នុងបន្ទះឈីប ហើយមិនអាចចម្លងចេញពីវាបានទេ។ សោម្រាមដៃនឹងបញ្ចប់ ប្រសិនបើមានម្រាមដៃ ឬមុខថ្មីត្រូវបានបន្ថែមទៅទូរស័ព្ទនេះ។",
  "p1_c3h": "អ្វីដែលការចុចបង្ហាញ", "p1_c3p": "ថាសោមួយនៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទបានចុច ដោយដោះសោដោយម្រាមដៃ ឬលេខកូដ PIN។ មិនមែនថាអ្នកណាកំពុងកាន់ទូរស័ព្ទនោះទេ។",
  "p1_go": "បន្ថែមទូរស័ព្ទនេះ", "p1_fine": "passkey របស់អ្នកនៅតែជាផ្លូវចូលរបស់អ្នក។ B-PoH បន្ថែមលើវា។", "by": "បោះផ្សាយដោយ HeartBank®",
  "host": "sign.333.eco", "p2_h": "បន្ថែមទូរស័ព្ទនេះ", "p2_from": "ស្នើដោយកម្មវិធី B-PoH℠ នៅលើទូរស័ព្ទនេះ",
  "p2_lede": "passkey របស់អ្នកបញ្ជាក់ថាជាអ្នក។ បន្ទាប់មក កម្មវិធីបង្កើតសោរបស់វានៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទនេះផ្ទាល់ សម្រាប់ចុះហត្ថលេខា។",
  "p2_ch": "មានតែការចុចទេដែលអាចបន្ថែមទូរស័ព្ទបាន", "p2_cp": "passkey របស់អ្នក ឬទូរស័ព្ទមួយទៀតដែលមាន B-PoH រួចហើយ អាចបន្ថែមទូរស័ព្ទនេះបាន។ ការចូលតែម្យ៉ាង មិនអាចទេ។",
  "p2_go": "បញ្ជាក់ដោយ passkey របស់អ្នក", "p2_other": "អនុម័តពីទូរស័ព្ទមួយទៀតរបស់អ្នក", "p2_new": "ថ្មីនៅទីនេះ? បង្កើត passkey", "no": "មិនមែនពេលនេះ",
  "p2_foot": "sign.333.eco · គ្មានពាក្យសម្ងាត់",
  "p2b_h": "អនុម័តពីទូរស័ព្ទមួយទៀត",
  "p2b_lede": "នៅលើទូរស័ព្ទដែលអ្នកបានបន្ថែមរួចហើយ សូមបើក B-PoH ចុច ស្កេនកូដ ហើយស្កេនកូដនេះ។ ទុកទូរស័ព្ទទាំងពីរនៅជាមួយគ្នា។",
  "p2b_ch": "ហេតុអ្វីទូរស័ព្ទទាំងពីរត្រូវនៅជាមួយគ្នា", "p2b_cp": "ទូរស័ព្ទមួយទៀតពិនិត្យតាមប៊្លូធូសថាវានៅក្បែរទូរស័ព្ទនេះ ដូច្នេះកូដដែលផ្ញើមកពីកន្លែងផ្សេង មិនអាចបន្ថែមទូរស័ព្ទរបស់មនុស្សចម្លែកបានទេ។",
  "p2b_alt": "ប្រើ passkey របស់អ្នកជំនួសវិញ",
  "p19_ask": "sign.333.eco សុំឱ្យអ្នកអនុម័ត៖", "p19_f": ("អ្វី", "វានឹង"),
  "p19_v": ("បន្ថែមទូរស័ព្ទដែលអ្នកទើបតែស្កេន ទៅក្នុងគណនីរបស់អ្នក", "បង្កើតសោម្រាមដៃ និងសោ PIN ផ្ទាល់ខ្លួនរបស់វា ហើយចុចសម្រាប់អ្នក"),
  "p19_fine": "សូមអនុម័តតែទូរស័ព្ទដែលអ្នកកំពុងកាន់ប៉ុណ្ណោះ។ វាមិនដែលទទួលបានសោរបស់ទូរស័ព្ទនេះទេ។",
  "p12b_h": "forum.example.org សុំ​passkey​ដែល​បង្កើត​ក្នុង​បន្ទះឈីប​របស់​ទូរស័ព្ទ​នេះ",
  "p12b_lede": "គេហទំព័រនឹងទទួលបានភស្តុតាងរបស់ទូរស័ព្ទនេះ ថាសោត្រូវបានបង្កើតនៅក្នុងបន្ទះឈីបរបស់វា។",
  "p12b_c1h": "អ្វីដែលភស្តុតាងក៏បង្ហាញផងដែរ", "p12b_c1p": "កំណែ Android និងបច្ចុប្បន្នភាពសុវត្ថិភាពចុងក្រោយរបស់ទូរស័ព្ទនេះ ហើយនៅលើទូរស័ព្ទខ្លះ ក៏បង្ហាញក្រុមទូរស័ព្ទដែលវាត្រូវបានផលិតជាមួយដែរ។ វាមិនដាក់ឈ្មោះទូរស័ព្ទនេះទេ។ ប្រសិនបើអ្នកមិនចង់ឱ្យគេហទំព័រឃើញរឿងនេះ សូមត្រឡប់ក្រោយ ហើយជ្រើសរើសកម្មវិធីគ្រប់គ្រង passkey ធម្មតារបស់អ្នក។",
  "p12b_c2h": "វានៅលើទូរស័ព្ទនេះ", "p12b_c2p": "passkey នេះមិនអាចចម្លងទៅឧបករណ៍ផ្សេងបានទេ។ ប្រសិនបើអ្នកបាត់ទូរស័ព្ទនេះ វាក៏បាត់ដែរ ដូច្នេះសូមរក្សាផ្លូវចូលមួយទៀតទៅ forum.example.org។",
  "p12b_go": "បង្កើតវាដោយម្រាមដៃរបស់អ្នក", "p12b_go_pin": "បង្កើតវាដោយលេខកូដ PIN របស់អ្នក",
  "p12b_fine": "បើបង្កើតដោយម្រាមដៃ វានឹងបញ្ចប់ ប្រសិនបើមានម្រាមដៃ ឬមុខថ្មីត្រូវបានបន្ថែមទៅទូរស័ព្ទនេះ។ បើបង្កើតដោយលេខកូដ PIN វានៅដដែល។",
  "p4b_h": "ទូរស័ព្ទ​នេះ​ត្រូវ​បាន​បន្ថែម​ហើយ ជាមួយ​សោ PIN",
  "p4b_lede": "ទូរស័ព្ទនេះគ្មានឧបករណ៍ចាប់ស្នាមម្រាមដៃ ឬមុខ ដែលខ្លាំងគ្រប់គ្រាន់សម្រាប់សោម្រាមដៃទេ ដូច្នេះវាចុចដោយលេខកូដ PIN របស់អ្នក។",
  "p4b_ch": "ការចុចនីមួយៗប្រាប់ថាសោមួយណាបានចុច", "p4b_cp": "គេហទំព័រខ្លះអាចស្នើសុំការចុចដោយម្រាមដៃ ហើយទូរស័ព្ទនេះមិនអាចផ្តល់វាបានទេ។ អ្វីៗផ្សេងទៀតដំណើរការដូចគ្នា។",
  "p20_h": "ទូរស័ព្ទ​នេះ​ត្រូវ​ការ​បន្ថែម​ម្តង​ទៀត",
  "p20_lede": "គណនីរបស់អ្នកត្រូវបានបើកដោយសារជាអក្សរ ដូច្នេះសោរបស់ទូរស័ព្ទនេះបានបញ្ចប់ហើយ។ សារជាអក្សរមិនអាចបន្ថែមទូរស័ព្ទបានទេ។",
  "p20_ch": "បន្ថែមវាម្តងទៀតដោយ passkey",
  "p20_cp": "passkey ដែលអ្នកនៅមាន អាចបន្ថែមវាបានឥឡូវនេះ។ passkey ដែលបង្កើតក្រោយសារជាអក្សរនោះ អាចបន្ថែមវាបានក្រោយរយៈពេលរង់ចាំមួយ ដែលត្រូវបានប្រាប់ជាមុនទៅគ្រប់អាសយដ្ឋានដែលភ្ជាប់នឹងគណនីរបស់អ្នក ដើម្បីឱ្យគេអាចបញ្ឈប់វាបាន ប្រសិនបើវាមិនមែនជាអ្នក។",
  "p20_go": "បន្ថែមទូរស័ព្ទនេះម្តងទៀត", "p20_fine": "ប្រសិនបើនេះមិនមែនជាអ្នកទេ នរណាម្នាក់ប្រហែលជាកំពុងប្រើលេខទូរស័ព្ទរបស់អ្នក។ កំណត់ត្រារបស់អ្នកមិនផ្លាស់ប្តូរទេ។",
  "p2c_h": "ទូរស័ព្ទ​នេះ​អាច​បន្ថែម​បាន​នៅ​ថ្ងៃ ២ ធ្នូ ២០២៦",
  "p2c_lede": "គណនីរបស់អ្នកត្រូវបានបើកដោយសារជាអក្សរ នៅថ្ងៃ ២៥ វិច្ឆិកា ២០២៦។ passkey ដែលបង្កើតក្រោយពេលនោះ បន្ថែមទូរស័ព្ទបានតែក្រោយរយៈពេលរង់ចាំមួយប៉ុណ្ណោះ ដូច្នេះយើងបានប្រាប់គ្រប់អាសយដ្ឋានដែលភ្ជាប់នឹងគណនីរបស់អ្នកជាមុនសិន។",
  "p2c_ch": "ប្រសិនបើនេះមិនមែនជាអ្នកទេ", "p2c_cp": "នរណាម្នាក់ប្រហែលជាកំពុងប្រើលេខទូរស័ព្ទរបស់អ្នក។ សារដែលយើងបានផ្ញើប្រាប់ពីរបៀបបញ្ឈប់វា។",
  "acct_h": "passkey របស់អ្នក", "acct_this": "ឧបករណ៍នេះ", "acct_added": "បានបន្ថែម", "acct_remove": "លុប",
  "acct_pk": "កុំព្យូទ័រយួរដៃរបស់ខ្ញុំ", "acct_pkd": "បានបន្ថែម ៣ វិច្ឆិកា ២០២៦",
  "acct_ph": "ទូរស័ព្ទដែលមាន B-PoH", "acct_phone": "ទូរស័ព្ទមួយ", "acct_phoned": "បានបន្ថែម ២៥ វិច្ឆិកា ២០២៦ · សោម្រាមដៃ និងសោ PIN",
  "acct_lost": "បាត់ ឬត្រូវគេលួច?",
  "acct_which": "សូមលុបទូរស័ព្ទដែលអ្នកនៅមាន ហើយលែងប្រើ។ ប្រសិនបើវាបាត់ ឬត្រូវគេលួច សូមរាយការណ៍ជំនួសវិញ៖ ការនោះក៏គ្របដណ្តប់អ្វីដែលសោរបស់វាបានចុច ចាប់តាំងពីពេលចុងក្រោយដែលអ្នកមានវាផងដែរ។",
  "p22_h": "រាយការណ៍​ទូរស័ព្ទ​ដែល​បាត់ ឬ​ត្រូវ​គេ​លួច", "p22_when": "តើអ្នកមានវាចុងក្រោយនៅពេលណា?", "p22_day": "២៥ វិច្ឆិកា ២០២៦", "p22_time": "18:00",
  "p22_ch": "អ្វីដែលនឹងក្លាយជាសាធារណៈ", "p22_cp": "កំណត់ត្រាសាធារណៈមួយថា សោរបស់ទូរស័ព្ទនេះត្រូវបានរាយការណ៍ និងពេលវេលាដែលអ្នកផ្តល់។ ការចុចដែលសោរបស់វាបានធ្វើចាប់ពីពេលនោះទៅ លែងត្រូវបានគាំទ្រដោយអ្វីដែលបន្ទះឈីបរបស់វាបានបង្ហាញទៀតហើយ។ ការចុចមុនពេលនោះនៅដដែល។ ប្រសិនបើអ្នកបានចែករំលែកការចុចដែលធ្វើនៅលើទូរស័ព្ទនេះ អ្នកណាដែលមានវាអាចឃើញថាវាមកពីទូរស័ព្ទតែមួយ។ វាមិនអាចត្រឡប់វិញបានទេ។",
  "p22_go": "រាយការណ៍ដោយ passkey របស់អ្នក",
  "p23_h": "បាន​រាយការណ៍", "p23_lede": "សោរបស់ទូរស័ព្ទនេះបានបញ្ចប់ហើយ។ វាមិនអាចចុចម្តងទៀតបានទេ។",
  "p23_ch": "នៅលើកំណត់ត្រាសាធារណៈ", "p23_cp": "ចាប់ពីថ្ងៃ ២៥ វិច្ឆិកា ២០២៦ ម៉ោង 18:00 ការចុចដោយសោរបស់ទូរស័ព្ទនេះ លែងត្រូវបានគាំទ្រដោយអ្វីដែលបន្ទះឈីបរបស់វាបានបង្ហាញទៀតហើយ។ ការចុចមុនពេលនោះនៅដដែល។ កំណត់ត្រានោះដាក់ឈ្មោះសោ មិនដែលដាក់ឈ្មោះអ្នកទេ។",
  "p23_go": "ត្រឡប់ទៅ passkey របស់អ្នកវិញ", "p23_new": "បន្ថែមទូរស័ព្ទថ្មី",
  "p3_h": "កំពុង​បង្កើត​សោ​ពីរ​របស់​អ្នក",
  "p3_steps": ("passkey របស់អ្នកបានបញ្ជាក់ថាជាអ្នក", "សោម្រាមដៃ៖ ប៉ះឧបករណ៍ចាប់ស្នាមម្រាមដៃ", "សោ PIN៖ បន្ទាប់មកបញ្ចូលលេខកូដ PIN របស់អ្នក", "sign.333.eco អានភស្តុតាងរបស់ទូរស័ព្ទនេះ"),
  "p3_sys_h": "បង្កើត​សោ​ម្រាមដៃ​របស់​អ្នក", "p3_sys_sub": "B-PoH℠ · សម្រាប់ sign.333.eco", "touch": "ប៉ះឧបករណ៍ចាប់ស្នាមម្រាមដៃ", "cancel": "បោះបង់",
  "p4_h": "ទូរស័ព្ទ​នេះ​ត្រូវ​បាន​បន្ថែម​ហើយ", "p4_lede": "ឥឡូវនេះ វាអាចចុចសម្រាប់អ្នកបាន ដោយម្រាមដៃ ឬលេខកូដ PIN របស់អ្នក។",
  "p4_read": "អ្វីដែល sign.333.eco បានអានពីភស្តុតាងរបស់ទូរស័ព្ទនេះ",
  "p4_reads": ("សោត្រូវបានបង្កើតនៅក្នុងបន្ទះឈីបសុវត្ថិភាពរបស់ទូរស័ព្ទនេះ ហើយមិនអាចចាកចេញពីវាបានទេ។", "ទូរស័ព្ទកំពុងដំណើរការកម្មវិធីប្រព័ន្ធផ្ទាល់របស់អ្នកផលិតវា។", "នេះជាកម្មវិធីដែល HeartBank® បោះផ្សាយ។"),
  "p4_not": "វាមិននិយាយអ្វីទាំងអស់អំពីអ្នកណាកំពុងកាន់ទូរស័ព្ទនោះទេ។",
  "p4_kh": "សេចក្តីថ្លែងការណ៍អំពីសោទាំងនេះ", "p4_kp": "sign.333.eco បានចុះហត្ថលេខាលើអ្វីដែលវាបានអាន ហើយទូរស័ព្ទនេះរក្សាទុកវា។ វាត្រូវបានបង្ហាញតែនៅពេលអ្នកចែករំលែកការចុចមួយប៉ុណ្ណោះ។ សេចក្តីថ្លែងការណ៍នោះមិនត្រូវបានផ្សព្វផ្សាយជាសាធារណៈទេ។",
  "done": "រួចរាល់",
  "p5_ready": "ទូរស័ព្ទ​នេះ​អាច​ចុច​សម្រាប់​អ្នក​បាន។", "p5_scan": "ស្កេនកូដ", "p5_scan_s": "នៅពេលអេក្រង់មួយទៀតសុំឱ្យអ្នកចុច",
  "p5_ph": "ការចុចរបស់អ្នក ដែលរក្សាទុកនៅលើទូរស័ព្ទនេះ", "p5_list": (("ចុះហត្ថលេខាលើឯកសារនេះ", "origin.333.eco · ២៥ វិច្ឆិកា"), ("បញ្ជាក់ថាជាអ្នក", "origin.333.eco · ២៤ វិច្ឆិកា")),
  "p5_fine": "មានតែអ្នកទេដែលឃើញបញ្ជីនេះ។", "keys": "សោរបស់អ្នក", "keys_s": "សោម្រាមដៃ · សោ PIN",
  "ask": "origin.333.eco សុំឱ្យអ្នកចុះហត្ថលេខា៖",
  "f_file": "ឯកសារ", "f_size": "ទំហំ", "f_fp": "ស្នាមម្រាមដៃ", "f_how": "របៀបដែលវាត្រូវបានបង្កើត", "f_rights": "ចែករំលែកក្រោម",
  "w1": ("sunflower.jpg", "3.1 MB", "c8e1 04ab … 9d37", "រូបថត ឬការថត", "រក្សាសិទ្ធិគ្រប់យ៉ាង"),
  "p6_pub": "ការនេះបន្ថែមកំណត់ត្រាសាធារណៈមួយ៖ ពេលដែលវាត្រូវបានចុះហត្ថលេខា និងរបៀបដែលវាត្រូវបានបង្កើត។ វាបង្ហាញថាសោមួយនៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទបានចុះហត្ថលេខា មិនមែនថាអ្នកណាជាអ្នកគិតវាទេ។",
  "go_finger": "ចុចដោយម្រាមដៃរបស់អ្នក", "go_pin": "ប្រើលេខកូដ PIN របស់អ្នកជំនួសវិញ",
  "nothing": "មិនបានចុះហត្ថលេខាទេ។",
  "pin_enter": "បញ្ចូលលេខកូដ PIN របស់អ្នក", "p8_pin": "បានចុចដោយសោ PIN របស់អ្នក",
  "p7_sys_h": "ចុះហត្ថលេខា​លើ​ពាក្យ​ពិតប្រាកដ​ទាំងនេះ", "p7_sys_sub": "ស្នើដោយ origin.333.eco",
  "p8_h": "បានចុះហត្ថលេខា", "p8_lede": "ហត្ថលេខារបស់អ្នកត្រូវបានរក្សាទុក។ វានឹងចូលទៅក្នុងកំណត់ហេតុសាធារណៈក្នុងរយៈពេលមួយម៉ោង។",
  "p8_ch": "បានចុចដោយសោម្រាមដៃរបស់អ្នក", "p8_cp": "កំណត់ត្រានិយាយថា សោមួយនៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទនេះបានចុច ដោយដោះសោដោយម្រាមដៃ។ វាមិនដែលនិយាយថាអ្នកជានរណាទេ។",
  "p8_go": "ត្រឡប់ទៅ origin.333.eco វិញ",
  "p9_lede": "តម្រង់ទូរស័ព្ទនេះទៅកូដនៅលើអេក្រង់ដែលបានស្នើ។",
  "p9_ch": "ទុកឧបករណ៍ទាំងពីរនៅជាមួយគ្នា", "p9_cp": "ទូរស័ព្ទនេះពិនិត្យតាមប៊្លូធូសថាវានៅជិតអេក្រង់នោះ ដូច្នេះកូដដែលគេបញ្ជូនបន្តមកពីកន្លែងផ្សេង មិនអាចចុចបានទេ។",
  "p10_from": "នៅលើកុំព្យូទ័រក្បែរអ្នក", "near": "នៅជិតទូរស័ព្ទនេះ",
  "p10_sealed": "ពាក្យទាំងនេះមកពីអេក្រង់នោះ ដោយបិទជិត ដើម្បីឱ្យមានតែទូរស័ព្ទនេះទេដែលអាចបើកវាបាន។",
  "w2": ("harvest.png", "2.4 MB", "5b0e 91c2 … 44af", "បង្កើតដោយដៃនៅលើឧបករណ៍", "រក្សាសិទ្ធិគ្រប់យ៉ាង"),
  "p11_h": "ទូរស័ព្ទ​នេះ​មិន​នៅ​ជិត​អេក្រង់​ដែល​បាន​ស្នើ​ទេ",
  "p11_lede": "ការចុចដែលធ្វើឡើងឆ្ងាយពីអេក្រង់នោះ អាចជាកូដដែលនរណាម្នាក់បានបញ្ជូនបន្ត ដូច្នេះការចុចនេះមិនអាចបន្តបានទេ។ មិនបានចុះហត្ថលេខាទេ។",
  "p11_ch": "នាំវាមកជាមួយគ្នា", "p11_cp": "យកទូរស័ព្ទនេះទៅអេក្រង់នោះ ហើយស្កេនម្តងទៀត។ ឬចុចនៅលើអេក្រង់នោះផ្ទាល់ ដោយ passkey របស់អ្នក។",
  "p11_go": "ស្កេនម្តងទៀត",
  "site": "forum.example.org", "p12_page": "បង្កើតគណនីរបស់អ្នកនៅទីនេះ", "p12_sys_h": "បង្កើត passkey សម្រាប់ forum.example.org?",
  "p12_o1s": "នៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទនេះ", "p12_o2": "កម្មវិធីគ្រប់គ្រង passkey ធម្មតារបស់អ្នក", "cont": "បន្ត",
  "p13_h": "forum.example.org សុំ​ការចុច​មួយ",
  "p13_lede": "ទំព័ររបស់វាផ្ទាល់បង្ហាញថាអ្នកកំពុងចុចសម្រាប់អ្វី។ កម្មវិធីនេះមិនអាចមើលឃើញពាក្យទាំងនោះទេ ដូច្នេះសូមអានវានៅទីនោះមុននឹងចុច។",
  "p13_ch": "កំណត់ត្រានឹងនិយាយដូច្នេះ", "p13_cp": "វានិយាយថា គេហទំព័របានបង្ហាញពាក្យទាំងនោះ មិនមែនកម្មវិធីនេះទេ។",
  "p14_g1": "នៅក្នុងបន្ទះឈីបរបស់ទូរស័ព្ទនេះ",
  "p14_rows": (("សោម្រាមដៃ", "បង្កើត ២៥ វិច្ឆិកា ២០២៦ · បញ្ចប់ប្រសិនបើមានម្រាមដៃ ឬមុខថ្មីត្រូវបានបន្ថែមទៅទូរស័ព្ទនេះ"), ("សោ PIN", "បង្កើត ២៥ វិច្ឆិកា ២០២៦ · នៅដដែល នៅពេលមានម្រាមដៃ ឬមុខត្រូវបានបន្ថែម")),
  "p14_g2": "passkey ដែលកម្មវិធីនេះបានបង្កើតសម្រាប់គេហទំព័រ", "p14_site": ("forum.example.org", "បង្កើត ២៥ វិច្ឆិកា ២០២៦"),
  "p14_note": "passkey របស់អ្នកនៅតែជាផ្លូវចូលរបស់អ្នក នៅលើគ្រប់ឧបករណ៍។ សោទាំងនេះបន្ថែមលើវា។", "remove": "ដកទូរស័ព្ទនេះចេញ",
  "p15_h": "សោ​ម្រាមដៃ​របស់​អ្នក​បាន​បញ្ចប់​ហើយ",
  "p15_lede": "សោនេះមិនអាចចុចម្តងទៀតបានទេ៖ ម្រាមដៃ ឬមុខថ្មីត្រូវបានបន្ថែមទៅទូរស័ព្ទនេះ ឬការចាក់សោអេក្រង់របស់វាត្រូវបានដកចេញ។ នេះជារបៀបដែលវារារាំងម្រាមដៃដែលមិនមែនជារបស់អ្នក។",
  "p15_ch": "សោ PIN របស់អ្នកនៅតែដំណើរការ", "p15_cp": "អ្នកអាចចុចដោយលេខកូដ PIN របស់អ្នកឥឡូវនេះ។ ដើម្បីបង្កើតសោម្រាមដៃថ្មី សូមបញ្ជាក់ដោយ passkey របស់អ្នក ឬពីទូរស័ព្ទមួយទៀតរបស់អ្នក។",
  "p15_go": "បង្កើតសោម្រាមដៃថ្មី", "p15_fine": "passkey និងកំណត់ត្រារបស់អ្នកមិនផ្លាស់ប្តូរទេ។",
  "p16_h": "ដក​ទូរស័ព្ទ​នេះ​ចេញ​ឬ?",
  "p16_p": "សោម្រាមដៃ និងសោ PIN របស់វានឹងបញ្ចប់ ហើយ passkey ដែលវាបានបង្កើតសម្រាប់គេហទំព័រក៏ដូចគ្នាដែរ។ passkey គណនី និងកំណត់ត្រារបស់អ្នកនៅដដែល។",
  "keep": "រក្សាវាទុក",
  "p17_lang": "ភាសា", "p17_look": "រូបរាង", "p17_web": "គេហទំព័រ",
  "p17_web_t": "បង្កើត passkey សម្រាប់គេហទំព័រដែលស្នើ",
  "p17_web_s": "តែនៅពេលគេហទំព័រមួយស្នើសុំសោពីបន្ទះឈីបរបស់ទូរស័ព្ទប៉ុណ្ណោះ។ គេហទំព័រផ្សេងទៀតទាំងអស់ នៅតែប្រើកម្មវិធីគ្រប់គ្រង passkey ធម្មតារបស់អ្នក។",
  "p17_web_go": "បើកការកំណត់ passkey របស់ទូរស័ព្ទ", "p17_about": "អំពី", "privacy": "ឯកជនភាព",
  "p18_h": "នៅ​ពេល​ដែល​ទូរស័ព្ទ​មួយ​មិន​អាច​បន្ថែម​បាន",
  "p18_c1": "នៅពេលកម្មវិធីប្រព័ន្ធរបស់ទូរស័ព្ទត្រូវបានផ្លាស់ប្តូរ", "p18_c1h": "ទូរស័ព្ទនេះមិនអាចកាន់សោ B-PoH បានទេ",
  "p18_c1p": "ភស្តុតាងរបស់វានិយាយថា វាមិនកំពុងដំណើរការកម្មវិធីប្រព័ន្ធផ្ទាល់របស់អ្នកផលិតទេ ដូច្នេះមិនអាចបង្ហាញថាសោក្នុងបន្ទះឈីបរបស់វាជារបស់វាផ្ទាល់បានទេ។ passkey របស់អ្នកនៅតែដំណើរការនៅគ្រប់កន្លែងដូចមុន។",
  "p18_c2": "នៅពេលទូរស័ព្ទគ្មានការចាក់សោអេក្រង់", "p18_c2h": "បើកការចាក់សោអេក្រង់ជាមុនសិន",
  "p18_c2p": "សោទាំងនេះដោះសោបានតែដោយលេខកូដ PIN ឬម្រាមដៃដែលបានរៀបចំនៅលើទូរស័ព្ទនេះប៉ុណ្ណោះ។ សូមកំណត់មួយនៅក្នុងការកំណត់របស់ទូរស័ព្ទ រួចបន្ថែមទូរស័ព្ទម្តងទៀត។",
  "p18_c3": "នៅពេលគណនីរបស់អ្នកកាន់ទូរស័ព្ទច្រើនតាមដែលវាអាចកាន់បាន", "p18_c3h": "ដកទូរស័ព្ទមួយចេញជាមុនសិន",
  "p18_c3p": "គណនីរបស់អ្នកកាន់សោទូរស័ព្ទច្រើនតាមដែលវាអាចកាន់បាន។ សូមដកទូរស័ព្ទមួយដែលអ្នកលែងប្រើចេញ នៅក្នុង សោរបស់អ្នក រួចបន្ថែមទូរស័ព្ទនេះ។",
  "p18_c4": "នៅពេលការបន្ថែមទូរស័ព្ទត្រូវបានផ្អាក", "p18_c4t": "ការបន្ថែមទូរស័ព្ទត្រូវបានផ្អាកឥឡូវនេះ។ គ្មានអ្វីផ្លាស់ប្តូរទេ។ សូមព្យាយាមម្តងទៀតពេលក្រោយ។",
},
}

# ── the native frame ──────────────────────────────────────────────────────────────────────────────────────────────
def _icon(d, w=22, sw=2.2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" aria-hidden="true"><path d="%s" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/></svg>' % (w, w, d, sw)

BACK, CLOSE, CHEV = "M15 5l-7 7 7 7", "M6 6l12 12M18 6L6 18", "M9 6l6 6-6 6"
GEAR = ("M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1"
        "a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8"
        "l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1"
        "a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z")
SCAN = "M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3M7 12h10"
LOCK = "M7 11V8a5 5 0 0 1 10 0v3M6 11h12v9H6z"


def _emblem(px=22):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>' % (px, px, EMBLEM)


def _sb(d):
    """Android's status bar: the time, then signal, wifi and battery (drawn)."""
    icons = ('<svg width="54" height="12" viewBox="0 0 54 12" aria-hidden="true"><path d="M1 11h2V8H1zM5 11h2V6H5zM9 11h2V4H9zM13 11h2V1h-2z" fill="currentColor"/>'
             '<path d="M20 4.5a9 9 0 0 1 12 0M22.5 7a5.4 5.4 0 0 1 7 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="26" cy="9.6" r="1.4" fill="currentColor"/>'
             '<rect x="36.5" y="1.5" width="14" height="9" rx="2" fill="none" stroke="currentColor"/><rect x="38" y="3" width="9" height="6" rx="1" fill="currentColor"/><path d="M52 4.5v3" stroke="currentColor" stroke-width="1.4"/></svg>')
    return '<div class="ph-sb"><span>%s</span>%s</div>' % (d["time"], icons)


def _bar(left="", title="", right=""):
    return '<div class="ph-bar"><span class="ph-bl">%s</span><span class="ph-bt">%s</span><span class="ph-br">%s</span></div>' % (left, title, right)


def _brand(d):
    return '<span class="ph-brand">%s<b>%s</b></span>' % (_emblem(), d["app"])


def _gb():
    return '<div class="ph-gb"><i></i></div>'


def _scr(d, bar, inner, over="", cls=""):
    return _sb(d) + bar + '<div class="ph-in%s">%s</div>' % (cls, inner) + _gb() + over


def _btn(label, ghost=False, icon=""):
    return '<button class="btn%s">%s%s</button>' % (" ghost" if ghost else "", icon, label)


def _link(label):
    return '<p class="ph-link"><span class="link">%s</span></p>' % label


def _toast(text, inline=False):
    return '<div class="ph-toast%s" role="status">%s</div>' % (" inline" if inline else "", text)


# ── spot drawings (flat, from the tokens; one per info card, Default 5) ─────────────────────────────────────────────
def _art(kind):
    s = ['<svg class="spot" width="56" height="40" viewBox="0 0 56 40" aria-hidden="true">']
    if kind == "chip":      # a chip with a key inside it
        s += ['<rect x="14" y="6" width="28" height="28" rx="5" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/>',
              '<path d="M9 13h5M9 20h5M9 27h5M42 13h5M42 20h5M42 27h5M21 1v5M28 1v5M35 1v5M21 34v5M28 34v5M35 34v5" stroke="var(--line-strong)" stroke-width="2" stroke-linecap="round"/>',
              '<circle cx="24" cy="18" r="4" fill="none" stroke="var(--accent)" stroke-width="2.4"/><path d="M27 21l6 6M31 25l2-2" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>']
    elif kind == "words":   # a card of words, one line pressed
        s += ['<rect x="6" y="4" width="44" height="32" rx="5" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/>',
              '<path d="M13 13h30M13 20h24M13 27h27" stroke="var(--line-strong)" stroke-width="2.4" stroke-linecap="round"/>',
              heart(44, 30, .55)]
    elif kind == "near":    # a phone beside a screen, with the waves between
        s += ['<rect x="2" y="9" width="15" height="25" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/>',
              '<rect x="32" y="6" width="22" height="16" rx="2" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/><path d="M29 27h28" stroke="var(--line-strong)" stroke-width="2.4" stroke-linecap="round"/>',
              '<path d="M21 14a6 6 0 0 1 0 10M24.5 11a10 10 0 0 1 0 16" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/>']
    elif kind == "lock":    # a phone with a lock on its screen
        s += ['<rect x="18" y="2" width="20" height="36" rx="4" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/>',
              '<path d="M24 19v-3a4 4 0 0 1 8 0v3" fill="none" stroke="var(--accent)" stroke-width="2.2"/><rect x="22.5" y="19" width="11" height="9" rx="2" fill="var(--accent)"/>']
    elif kind == "phones":  # two phones, one leaving
        s += ['<rect x="6" y="6" width="17" height="30" rx="3" fill="var(--surface-2)" stroke="var(--line-strong)" stroke-width="1.5"/>',
              '<rect x="33" y="6" width="17" height="30" rx="3" fill="none" stroke="var(--line-strong)" stroke-width="1.5" stroke-dasharray="3 3"/>',
              heart(14.5, 21, .5)]
    s.append('</svg>')
    return "".join(s)


def _card(h, p, kind):
    art = spot(kind) if kind in ("key", "split", "log", "two") else _art(kind)   # the shared spots, or this file's own
    return '<div class="card">%s<h2>%s</h2><p>%s</p></div>' % (art, h, p)


def _fp_icon():
    return ('<svg class="ph-fp" width="64" height="64" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="31" fill="var(--wash)"/>'
            '<g fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round">'
            '<path d="M21 25a12 12 0 0 1 22 0"/><path d="M19 32a13 13 0 0 1 26 0c0 5-1 9-3 12"/><path d="M25 44c2-3 3-7 3-12a4 4 0 0 1 8 0c0 6-1 11-4 15"/>'
            '<path d="M22 40c1-2 2-5 2-8a8 8 0 0 1 16 0c0 4 0 7-1 10"/></g></svg>')


def _words(d, w):
    """The exact words of a press, Linear-quiet: the asker, then the fields, given the room."""
    labels = (d["f_file"], d["f_size"], d["f_fp"], d["f_how"], d["f_rights"])
    rows = "".join('<div class="ph-w"><span>%s</span><b%s>%s</b></div>' % (l, ' class="mono"' if i == 2 else "", v) for i, (l, v) in enumerate(zip(labels, w)))
    return '<div class="ph-words">%s</div>' % rows


def _press_btns(d):
    return _btn(d["go_finger"]) + _btn(d["go_pin"], ghost=True) + _link(d["no"])


def _li(t, s="", right=CHEV, lead=""):
    return ('<div class="ph-li">%s<span class="ph-lt"><span class="t">%s</span>%s</span>%s</div>'
            % (lead, t, '<span class="s">%s</span>' % s if s else "", _icon(right, 18) if right else ""))


def _group(h, rows):
    return '<div class="ph-gh">%s</div><div class="ph-list">%s</div>' % (h, "".join(rows))


def _seg(opts, on):
    return '<div class="seg ph-seg">%s</div>' % "".join('<span%s>%s</span>' % (' class="on"' if i == on else "", o) for i, o in enumerate(opts))


# ── the screens ─────────────────────────────────────────────────────────────────────────────────────────────────────
def P1(t, d):
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p1_h"], d["p1_lede"])
             + _card(d["p1_c1h"], d["p1_c1p"], "words") + _card(d["p1_c2h"], d["p1_c2p"], "chip") + _card(d["p1_c3h"], d["p1_c3p"], "log")
             + '<div class="grow"></div>' + _btn(d["p1_go"]) + '<p class="fine">%s</p><p class="fine ph-by">%s</p>' % (d["p1_fine"], d["by"]))
    return _scr(d, _bar(_brand(d), "", _seg(d["lang"], 1 if t["band"] else 0)), inner)


def P1w(t, d):
    """A phone never added that holds passkeys it made for websites (the provider works on its own; founder 2026-11-27, 'do per your
    recommendation': standalone): its keys and Settings are reachable from the first screen. The language choice moves to Settings."""
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p1_h"], d["p1_lede"])
             + _card(d["p1_c1h"], d["p1_c1p"], "words") + _card(d["p1_c2h"], d["p1_c2p"], "chip") + _card(d["p1_c3h"], d["p1_c3p"], "log")
             + '<div class="grow"></div>' + _btn(d["p1_go"]) + '<p class="fine">%s</p>' % d["p1_fine"]
             + _group("", [_li(d["keys"])]) + '<p class="fine ph-by">%s</p>' % d["by"])
    return _scr(d, _bar(_brand(d), "", '<span aria-label="%s">%s</span>' % (d["settings"], _icon(GEAR, 22, 1.8))), inner)


def _tab(d, host):
    return ('<div class="ph-ct">%s<span class="ph-ctu">%s<span>%s</span></span>%s</div>'
            % (_icon(CLOSE, 20), _icon(LOCK, 14, 2), host, '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="5" r="1.8" fill="currentColor"/><circle cx="12" cy="12" r="1.8" fill="currentColor"/><circle cx="12" cy="19" r="1.8" fill="currentColor"/></svg>'))


def P2b(t, d):
    """The new phone, in sign.333.eco's Custom Tab: approve from a phone already added (SPEC §5.2.1 + F2: scan, sealed words, nearness)."""
    wm = ('<span class="wordmark">Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup></span>' % EMBLEM)
    qr = re.sub(r'width="200" height="200"', 'width="176" height="176"', BQR, count=1)
    page = ('<div class="ph-web"><header>%s</header><h1>%s</h1><p class="lede">%s</p>' % (wm, d["p2b_h"], d["p2b_lede"])
            + '<div class="ph-qr">%s</div>' % qr + _card(d["p2b_ch"], d["p2b_cp"], "near")
            + '<div class="grow"></div>' + _link(d["p2b_alt"]) + _link(d["no"]) + '<footer><span>%s</span></footer></div>' % d["p2_foot"])
    return _sb(d) + _tab(d, d["host"]) + page + _gb()


def P19(t, d):
    """The phone already added, after scanning P2b's code: the words of an approval, with nearness (F2)."""
    near = '<span class="ph-near">%s%s</span>' % (_icon("M5 12.5l4.5 4.5L19 7.5", 14, 2.6), d["near"])
    rows = "".join('<div class="ph-w"><span>%s</span><b>%s</b></div>' % (l, v) for l, v in zip(d["p19_f"], d["p19_v"]))
    inner = ('<div class="ph-from"><span>%s</span>%s</div>' % ("", near) + '<p class="ph-ask">%s</p>' % d["p19_ask"]
             + '<div class="ph-words">%s</div>' % rows + '<p class="fine ph-pub">%s</p>' % d["p19_fine"] + '<div class="grow"></div>' + _press_btns(d))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner)


def P12b(t, d):
    """The app's own screen when a website asks it to MAKE a passkey (founder 2026-11-25, item 3 'decide for me'): say what the website receives."""
    inner = ('<div class="from"><span class="site"><i>f</i><span>%s</span></span></div><h1>%s</h1><p class="lede">%s</p>' % (d["site"], d["p12b_h"], d["p12b_lede"])
             + _card(d["p12b_c1h"], d["p12b_c1p"], "chip") + _card(d["p12b_c2h"], d["p12b_c2p"], "lock")
             + '<div class="grow"></div>' + _btn(d["p12b_go"]) + _btn(d["go_pin"], ghost=True) + '<p class="fine">%s</p>' % d["p12b_fine"] + _link(d["no"]))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner)


def P4b(t, d):
    """A phone with a PIN but no strong biometric: the PIN key alone (founder 2026-11-25, 'PIN key alone')."""
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p4b_h"], d["p4b_lede"]) + _card(d["p4b_ch"], d["p4b_cp"], "key")
             + '<div class="grow"></div>' + _btn(d["done"]))
    return _scr(d, _bar(_brand(d)), inner)


def P20(t, d):
    """After a text-message recovery the app layer drops (SPEC §5.2.4); a NEW passkey re-adds only after a waiting period told first (founder 2026-11-25)."""
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p20_h"], d["p20_lede"]) + _card(d["p20_ch"], d["p20_cp"], "key")
             + '<div class="grow"></div>' + _btn(d["p20_go"]) + _link(d["no"]) + '<p class="fine">%s</p>' % d["p20_fine"])
    return _scr(d, _bar(_brand(d)), inner)


def P2c(t, d):
    """sign.333.eco during the waiting period: the date stated ONCE, never counted down (Sig-8). ⚠️ The length (drawn as 7 days) is not ruled."""
    wm = ('<span class="wordmark">Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup></span>' % EMBLEM)
    page = ('<div class="ph-web"><header>%s</header><h1>%s</h1><p class="lede">%s</p>' % (wm, d["p2c_h"], d["p2c_lede"])
            + _card(d["p2c_ch"], d["p2c_cp"], "lock") + '<div class="grow"></div>' + _link(d["no"]) + '<footer><span>%s</span></footer></div>' % d["p2_foot"])
    return _sb(d) + _tab(d, d["host"]) + page + _gb()


def _browser(host):
    """An ordinary phone browser's address bar: these pages are sign.333.eco itself, opened anywhere (the phone is gone)."""
    return '<div class="ph-ab"><span class="ph-abu">%s<span>%s</span></span></div>' % (_icon(LOCK, 13, 2), host)


def _webpage(d, body):
    wm = ('<span class="wordmark">Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup></span>' % EMBLEM)
    return _sb(d) + _browser(d["host"]) + '<div class="ph-web"><header>%s</header>%s<footer><span>%s</span></footer></div>' % (wm, body, d["p2_foot"]) + _gb()


def P21(t, d):
    """The live 'Your passkeys' page, with the B-PoH phones it will list: Remove (a phone you still have) and Lost or stolen? (a report)."""
    pk = '<div class="ph-li"><span class="ph-lt"><span class="t">%s <span class="ph-tag">%s</span></span><span class="s">%s</span></span></div>' % (d["acct_pk"], d["acct_this"], d["acct_pkd"])
    ph = ('<div class="ph-li ph-col"><span class="ph-lt"><span class="t">%s</span><span class="s">%s</span></span>'
          '<span class="ph-acts"><span class="pillbtn ghost">%s</span><span class="pillbtn ph-warn">%s</span></span></div>' % (d["acct_phone"], d["acct_phoned"], d["acct_remove"], d["acct_lost"]))
    body = ('<h1>%s</h1>' % d["acct_h"] + '<div class="ph-list">%s</div>' % pk + _group(d["acct_ph"], [ph]) + '<p class="fine">%s</p>' % d["acct_which"] + '<div class="grow"></div>')
    return _webpage(d, body)


def P22(t, d):
    body = ('<h1>%s</h1><div class="ph-gh">%s</div><div class="ph-when"><div class="field">%s</div><div class="field">%s</div></div>' % (d["p22_h"], d["p22_when"], d["p22_day"], d["p22_time"])
            + _card(d["p22_ch"], d["p22_cp"], "log") + '<div class="grow"></div>' + _btn(d["p22_go"], icon=KEY) + _link(d["no"]))
    return _webpage(d, body)


def P23(t, d):
    body = ('<div class="ph-done">%s</div><h1>%s</h1><p class="lede">%s</p>' % (OKBIG, d["p23_h"], d["p23_lede"]) + _card(d["p23_ch"], d["p23_cp"], "log")
            + '<div class="grow"></div>' + _btn(d["p23_go"]) + _link(d["p23_new"]))
    return _webpage(d, body)


def P2(t, d):
    tab = ('<div class="ph-ct">%s<span class="ph-ctu">%s<span>%s</span></span>%s</div>'
           % (_icon(CLOSE, 20), _icon(LOCK, 14, 2), d["host"], '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="5" r="1.8" fill="currentColor"/><circle cx="12" cy="12" r="1.8" fill="currentColor"/><circle cx="12" cy="19" r="1.8" fill="currentColor"/></svg>'))
    wm = ('<span class="wordmark">Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup></span>' % EMBLEM)
    page = ('<div class="ph-web"><header>%s</header><h1>%s</h1>' % (wm, d["p2_h"])
            + '<div class="from"><span class="site"><i>%s</i><span>%s</span></span></div>' % (_emblem(14), d["p2_from"])
            + '<p class="lede">%s</p>' % d["p2_lede"] + _card(d["p2_ch"], d["p2_cp"], "lock")
            + '<div class="grow"></div>' + _btn(d["p2_go"], icon=KEY) + _btn(d["p2_other"], ghost=True) + _link(d["p2_new"]) + _link(d["no"])
            + '<footer><span>%s</span></footer></div>' % d["p2_foot"])
    return _sb(d) + tab + page + _gb()


def P3(t, d):
    st = d["p3_steps"]
    steps = "".join('<li class="%s"><i>%s</i><span>%s</span></li>' % (c, mark, s) for c, mark, s in
                    (("done", OKM, st[0]), ("now", "2", st[1]), ("", "3", st[2]), ("", "4", st[3])))
    inner = '<h1>%s</h1><ol class="ph-steps">%s</ol>' % (d["p3_h"], steps)
    sheet = ('<div class="ph-scrim"></div><div class="ph-sys"><h3>%s</h3><div class="sub">%s</div>%s<div class="ph-touch">%s</div>'
             '<div class="ph-neg"><span>%s</span></div></div>' % (d["p3_sys_h"], d["p3_sys_sub"], _fp_icon(), d["touch"], d["cancel"]))
    return _scr(d, _bar(_brand(d)), inner, sheet)


def P4(t, d):
    reads = "".join('<li>%s<span>%s</span></li>' % (OKM, r) for r in d["p4_reads"])
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p4_h"], d["p4_lede"])
             + '<div class="card">%s<h2>%s</h2><ul class="ph-ticks">%s</ul><p class="ph-not">%s</p></div>' % (_art("chip"), d["p4_read"], reads, d["p4_not"])
             + _card(d["p4_kh"], d["p4_kp"], "words") + '<div class="grow"></div>' + _btn(d["done"]))
    return _scr(d, _bar(_brand(d)), inner)


def P5(t, d):
    presses = [_li(a, b) for a, b in d["p5_list"]]
    inner = ('<p class="ph-ready">%s</p>' % d["p5_ready"]
             + '<div class="ph-scanbig">%s<span><b>%s</b><span>%s</span></span></div>' % (_icon(SCAN, 28), d["p5_scan"], d["p5_scan_s"])
             + _group(d["p5_ph"], presses) + '<p class="fine">%s</p>' % d["p5_fine"]
             + _group("", [_li(d["keys"], d["keys_s"])]))
    return _scr(d, _bar(_brand(d), "", '<span aria-label="%s">%s</span>' % (d["settings"], _icon(GEAR, 22, 1.8))), inner)


def _p6(d, over=""):
    inner = ('<p class="ph-ask">%s</p>' % d["ask"] + _words(d, d["w1"]) + '<p class="fine ph-pub">%s</p>' % d["p6_pub"]
             + '<div class="grow"></div>' + _press_btns(d))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner, over)


def P6(t, d):
    return _p6(d)


def P6b(t, d):
    return _p6(d, _toast(d["nothing"]))


def P7(t, d):
    w = d["w1"]
    sheet = ('<div class="ph-scrim"></div><div class="ph-sys"><h3>%s</h3><div class="sub">%s</div><div class="ph-desc">%s</div>%s<div class="ph-touch">%s</div>'
             '<div class="ph-neg"><span>%s</span></div></div>' % (d["p7_sys_h"], d["p7_sys_sub"], " · ".join((w[0], w[1], w[3], w[4])), _fp_icon(), d["touch"], d["go_pin"]))
    return _p6(d, sheet)


def P7p(t, d):
    """The PIN key's press: the phone's own PIN screen (drawn); the title, subtitle and words in it are ours."""
    w = d["w1"]
    keys = "".join('<span>%s</span>' % k for k in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "", "0", ""))
    inner = ('<div class="ph-pin"><h3>%s</h3><div class="sub">%s</div><div class="ph-desc">%s</div>'
             '<div class="ph-pinlbl">%s</div><div class="ph-dots"><i class="on"></i><i class="on"></i><i></i><i></i></div>'
             '<div class="ph-pad">%s</div><div class="ph-neg"><span>%s</span></div></div>'
             % (d["p7_sys_h"], d["p7_sys_sub"], " · ".join((w[0], w[1], w[3], w[4])), d["pin_enter"], keys, d["cancel"]))
    return _sb(d) + '<div class="ph-in">%s</div>' % inner + _gb()


def P8(t, d):
    inner = ('<div class="ph-done">%s</div><h1>%s</h1><p class="lede">%s</p>' % (OKBIG, d["p8_h"], d["p8_lede"])
             + _card(d["p8_ch"], d["p8_cp"], "chip") + '<div class="grow"></div>' + _btn(d["p8_go"]))
    return _scr(d, _bar(_brand(d)), inner)


def P9(t, d):
    qr = re.sub(r'width="200" height="200"', 'width="150" height="150"', BQR, count=1)
    cam = ('<div class="ph-cam"><div class="ph-scr">%s</div><i class="c1"></i><i class="c2"></i><i class="c3"></i><i class="c4"></i></div>' % qr)
    inner = '<p class="lede ph-top">%s</p>' % d["p9_lede"] + cam + _card(d["p9_ch"], d["p9_cp"], "near")
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["back"], _icon(BACK)), d["p5_scan"]), inner)


def P10(t, d):
    near = '<span class="ph-near">%s%s</span>' % (_icon("M5 12.5l4.5 4.5L19 7.5", 14, 2.6), d["near"])
    inner = ('<div class="ph-from"><span>%s</span>%s</div>' % (d["p10_from"], near) + '<p class="ph-ask">%s</p>' % d["ask"] + _words(d, d["w2"])
             + '<p class="fine ph-pub">%s</p>' % d["p10_sealed"] + '<div class="grow"></div>' + _press_btns(d))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner)


def P11(t, d):
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p11_h"], d["p11_lede"]) + _card(d["p11_ch"], d["p11_cp"], "near")
             + '<div class="grow"></div>' + _btn(d["p11_go"]) + _link(d["no"]))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner)


def P12(t, d):
    tab = ('<div class="ph-ct">%s<span class="ph-ctu">%s<span>%s</span></span><span></span></div>' % (_icon(CLOSE, 20), _icon(LOCK, 14, 2), d["site"]))
    page = ('<div class="ph-web ph-ghost"><h1>%s</h1><div class="field">Lotus</div><div class="field">@lotus</div></div>' % d["p12_page"])
    opts = ('<div class="ph-opt on"><i></i><span><b>%s</b><span>%s</span></span>%s</div>' % (d["app"], d["p12_o1s"], _emblem(20))
            + '<div class="ph-opt"><i></i><span><b>%s</b></span></div>' % d["p12_o2"])
    sheet = ('<div class="ph-scrim"></div><div class="ph-sys ph-left"><h3>%s</h3>%s<div class="ph-sysbtn"><span>%s</span><b>%s</b></div></div>'
             % (d["p12_sys_h"], opts, d["cancel"], d["cont"]))
    return _sb(d) + tab + page + _gb() + sheet


def P13(t, d):
    inner = ('<div class="from"><span class="site"><i>f</i>%s</span></div><h1>%s</h1><p class="lede">%s</p>' % (d["site"], d["p13_h"], d["p13_lede"])
             + _card(d["p13_ch"], d["p13_cp"], "words") + '<div class="grow"></div>' + _press_btns(d))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["close"], _icon(CLOSE)), "", _brand(d)), inner)


def _keys(d):
    rows = [_li(a, b, right="") for a, b in d["p14_rows"]]
    return (_group(d["p14_g1"], rows) + _group(d["p14_g2"], [_li(d["p14_site"][0], d["p14_site"][1])])
            + '<p class="fine">%s</p>' % d["p14_note"] + '<div class="grow"></div>' + '<button class="btn ghost ph-danger">%s</button>' % d["remove"])


def P14(t, d):
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["back"], _icon(BACK)), d["keys"]), _keys(d))


def P15(t, d):
    inner = ('<h1>%s</h1><p class="lede">%s</p>' % (d["p15_h"], d["p15_lede"]) + _card(d["p15_ch"], d["p15_cp"], "key")
             + '<div class="grow"></div>' + _btn(d["p15_go"]) + _link(d["no"]) + '<p class="fine">%s</p>' % d["p15_fine"])
    return _scr(d, _bar(_brand(d)), inner)


def P16(t, d):
    sheet = ('<div class="ph-scrim"></div><div class="ph-own">%s<h3>%s</h3><p>%s</p>%s%s</div>'
             % ('<div class="grab"></div>', d["p16_h"], d["p16_p"], '<button class="btn ph-dangerfill">%s</button>' % d["remove"], _btn(d["keep"], ghost=True)))
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["back"], _icon(BACK)), d["keys"]), _keys(d), sheet)


def P17(t, d):
    km = bool(t["band"])
    inner = ('<div class="ph-gh">%s</div>%s' % (d["p17_lang"], _seg(("English", "ខ្មែរ"), 1 if km else 0))
             + '<div class="ph-gh">%s</div>%s' % (d["p17_look"], _seg(d["theme"], 0))
             + _group(d["p17_web"], ['<div class="ph-li"><span class="ph-lt"><span class="t">%s</span><span class="s">%s</span><span class="link ph-act">%s</span></span></div>'
                                     % (d["p17_web_t"], d["p17_web_s"], d["p17_web_go"])])
             + _group(d["p17_about"], [_li(d["keys"]), _li(d["privacy"]), _li(d["by"], right="")])
             + '<p class="fine ph-disc">%s</p>' % DISCLAIMER)
    return _scr(d, _bar('<span aria-label="%s">%s</span>' % (d["back"], _icon(BACK)), d["settings"]), inner)


def P18(t, d):
    inner = ('<h1>%s</h1>' % d["p18_h"]
             + '<div class="ph-cap">%s</div>' % d["p18_c1"] + _card(d["p18_c1h"], d["p18_c1p"], "chip")
             + '<div class="ph-cap">%s</div>' % d["p18_c2"] + _card(d["p18_c2h"], d["p18_c2p"], "lock")
             + '<div class="ph-cap">%s</div>' % d["p18_c3"] + _card(d["p18_c3h"], d["p18_c3p"], "phones")
             + '<div class="ph-cap">%s</div>' % d["p18_c4"] + _toast(d["p18_c4t"], inline=True))
    return _scr(d, _bar(_brand(d)), inner)


KEY = ('<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2.4"/>'
       '<path d="M12 12h9M18 12v3M21 12v2" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>')
OKM = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
OKBIG = '<svg width="56" height="56" viewBox="0 0 56 56" aria-hidden="true"><circle cx="28" cy="28" r="27" fill="var(--wash)"/><path d="M17 29l7 7 15-16" fill="none" stroke="var(--accent)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

SCREENS = [
    ("P1", "poh", "First open: what a press is (the language choice shows until a phone is added)", P1),
    ("P1w", "poh", "First open on a phone never added that holds website passkeys: Your keys and Settings reachable (the provider stands alone)", P1w),
    ("P2", "poh", "Add this phone: sign.333.eco in a Custom Tab, an existing press first", P2),
    ("P2b", "poh", "Add this phone from another phone already added: the code to scan, in the Custom Tab", P2b),
    ("P19", "poh", "On the phone already added: approve the phone you just scanned (nearness required)", P19),
    ("P2c", "poh", "Adding a phone with a passkey made after a text-message recovery: the waiting period (its length, drawn as 7 days, is not ruled)", P2c),
    ("P3", "poh", "Making the two keys, under the phone's own fingerprint prompt (drawn; its title is ours)", P3),
    ("P4", "poh", "This phone is added: what sign.333.eco read from its proof", P4),
    ("P4b", "poh", "A phone with a PIN but no strong fingerprint or face: added with the PIN key alone", P4b),
    ("P5", "poh", "Home", P5),
    ("P6", "poh", "A press asked on this phone: the exact words", P6),
    ("P6b", "poh", "The same, after the person cancels the prompt (a toast)", P6b),
    ("P7", "poh", "The phone's own fingerprint prompt over the words (drawn; its words are ours)", P7),
    ("P7p", "poh", "The press with the PIN key: the phone's own PIN screen (drawn; its words are ours)", P7p),
    ("P8", "poh", "Signed: which key pressed (the PIN key's reads Pressed with your PIN key)", P8),
    ("P9", "poh", "Another screen asks: scan its code (with Bluetooth nearness)", P9),
    ("P10", "poh", "The other screen's words, opened on this phone", P10),
    ("P11", "poh", "When this phone isn't near the screen that asked", P11),
    ("P12", "poh", "A website asks for a passkey from a phone's chip: the phone's own passkey sheet (Android 14+, drawn)", P12),
    ("P12b", "poh", "When a website asks the app to MAKE a passkey: what the website receives, said first", P12b),
    ("P13", "poh", "Through the sheet: the website showed the words, this app can't see them", P13),
    ("P14", "poh", "Your keys", P14),
    ("P15", "poh", "When the finger key has ended (a new finger or face was added)", P15),
    ("P16", "poh", "Remove this phone", P16),
    ("P17", "poh", "Settings (language and appearance move here once a phone is added)", P17),
    ("P20", "poh", "After a text-message recovery: this phone needs adding again", P20),
    ("P21", "poh", "On sign.333.eco, from any device (the phone is gone): the phone on Your passkeys, with Remove and Lost or stolen?", P21),
    ("P22", "poh", "Report a lost or stolen phone: when you last had it, and what becomes public, said once", P22),
    ("P23", "poh", "Reported: the phone's keys are ended; the public record", P23),
    ("P18", "poh", "When a phone can't be added", P18),
]
PUBLIC = set()  # an app's own screens: no share button (Default 8)

CSS = """
.ph-root{position:relative;min-height:844px;display:flex;flex-direction:column;background:var(--bg)}
.ph-sb{display:flex;justify-content:space-between;align-items:center;height:30px;padding:0 20px;font:600 13px var(--font-text);color:var(--ink)}
.ph-bar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:6px 16px;min-height:52px;color:var(--ink)}
.ph-bl,.ph-br{display:flex;align-items:center;min-width:28px}
.ph-br{justify-content:flex-end}
.ph-bt{flex:1;font-size:18px;font-weight:600}
.ph-brand{display:inline-flex;align-items:center;gap:7px;font-size:17px;white-space:nowrap}
.ph-brand svg{color:var(--accent)}
.ph-in{flex:1;display:flex;flex-direction:column;padding:0 20px 20px}
.ph-gb{height:24px;display:grid;place-items:center}
.ph-gb i{width:108px;height:4px;border-radius:2px;background:var(--ink);opacity:.3}
.ph-seg{font-size:13px;align-self:flex-start}
.km .ph-root h1{line-height:1.45}
.ph-link{text-align:center;margin:14px 0 0;font-size:15px}
.ph-link .link,.ph-act{color:var(--accent);font-weight:600}
.ph-by{text-align:center}
.ph-ask{font-size:15px;color:var(--ink-dim);margin:18px 0 10px}
.ph-words{border-top:1px solid var(--line)}
.ph-w{display:flex;flex-direction:column;gap:2px;padding:12px 0;border-bottom:1px solid var(--line)}
.ph-w span{font-size:13px;color:var(--ink-dim)}
.ph-w b{font-size:19px;font-weight:500;letter-spacing:-.01em;line-height:1.35}
.ph-w b.mono{font-size:16px}
.ph-pub{margin-top:16px}
.ph-scrim{position:absolute;inset:0;background:rgba(0,0,0,.42)}
.ph-sys{position:absolute;left:10px;right:10px;bottom:32px;background:var(--surface);border-radius:28px;padding:24px 22px 18px;text-align:center;
  box-shadow:0 10px 40px rgba(0,0,0,.28);font-family:Roboto,var(--font-text)}
.km .ph-sys{font-family:var(--font-khmer),var(--font-text)}
.ph-sys h3{font-size:20px;font-weight:500;margin:0 0 4px;line-height:1.3}
.ph-sys .sub{font-size:14px;color:var(--ink-dim)}
.ph-desc{font-size:14px;text-align:left;margin:12px 0 0;color:var(--ink)}
.ph-fp{display:block;margin:18px auto 8px}
.ph-touch{font-size:14px;color:var(--ink-dim)}
.ph-neg{display:flex;justify-content:flex-start;margin-top:18px}
.ph-neg span{color:var(--accent);font-weight:600;font-size:15px}
.ph-left{text-align:left}
.ph-opt{display:flex;align-items:center;gap:12px;padding:12px;border:1px solid var(--line);border-radius:16px;margin-top:10px}
.ph-opt i{flex:none;width:18px;height:18px;border-radius:50%;border:2px solid var(--line-strong)}
.ph-opt.on{border-color:var(--accent);background:var(--wash)}
.ph-opt.on i{border:6px solid var(--accent)}
.ph-opt>span{flex:1}.ph-opt b{display:block;font-weight:600;font-size:15px}.ph-opt span span{font-size:13px;color:var(--ink-dim)}
.ph-opt svg{color:var(--accent)}
.ph-sysbtn{display:flex;justify-content:flex-end;align-items:center;gap:22px;margin-top:18px;font-size:15px}
.ph-sysbtn span{color:var(--accent);font-weight:600}
.ph-sysbtn b{background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:9px 20px;font-weight:600}
.ph-toast{position:absolute;left:16px;right:16px;bottom:44px;background:var(--ink);color:var(--bg);border-radius:12px;padding:12px 16px;font-size:14px;
  box-shadow:0 6px 24px rgba(0,0,0,.2)}
.ph-toast.inline{position:static;margin:4px 0 12px}
.ph-ct{display:flex;align-items:center;gap:14px;padding:10px 16px;border-bottom:1px solid var(--line);background:var(--surface);color:var(--ink)}
.ph-ctu{flex:1;display:flex;align-items:center;gap:6px;font-size:15px;font-weight:500}
.ph-ctu svg{color:var(--ink-dim)}
.ph-web{flex:1;display:flex;flex-direction:column;padding:0 20px 20px}
.ph-web header{padding:16px 0 4px}
.ph-ghost{opacity:.55}
.ph-steps{list-style:none;padding:0;margin:8px 0 0}
.ph-steps li{display:flex;gap:12px;align-items:center;padding:12px 0;border-top:1px solid var(--line);font-size:15px;color:var(--ink-dim)}
.ph-steps li:first-child{border-top:0}
.ph-steps i{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font:600 13px var(--font-text);font-style:normal;
  border:1.5px solid var(--line-strong);color:var(--ink-dim)}
.ph-steps li.done i{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.ph-steps li.now{color:var(--ink);font-weight:600}
.ph-steps li.now i{border-color:var(--accent);color:var(--accent)}
.ph-ticks{list-style:none;padding:0;margin:8px 0 0}
.ph-ticks li{display:flex;gap:10px;align-items:flex-start;padding:5px 0;font-size:14px}
.ph-ticks svg{flex:none;margin-top:3px;color:var(--accent)}
.ph-not{margin-top:10px!important}
.ph-ready{font-size:22px;font-weight:600;letter-spacing:-.01em;margin:14px 0 16px}
.ph-scanbig{display:flex;align-items:center;gap:14px;background:var(--accent);color:var(--accent-ink);border-radius:18px;padding:18px}
.ph-scanbig b{display:block;font-size:17px}.ph-scanbig span span{font-size:13.5px;opacity:.9}
.ph-gh{font-size:13px;color:var(--ink-dim);margin:22px 0 8px}
.ph-gh:empty{margin-top:14px}
.ph-list{border:1px solid var(--line);border-radius:14px;background:var(--surface);overflow:hidden}
.ph-li{display:flex;gap:12px;align-items:center;padding:13px 14px;border-top:1px solid var(--line)}
.ph-li:first-child{border-top:0}
.ph-lt{flex:1;display:flex;flex-direction:column}
.ph-lt .t{font-size:15px}.ph-lt .s{font-size:13px;color:var(--ink-dim);margin-top:2px}
.ph-act{margin-top:8px;font-size:14px}
.ph-li>svg{color:var(--ink-faint);flex:none}
.btn.ph-danger{color:#b3261e;border-color:color-mix(in oklab,#b3261e 40%,transparent)}
.dark .btn.ph-danger{color:#f2b8b5}
.ph-dangerfill{background:#b3261e;color:#fff}
.ph-own{position:absolute;left:0;right:0;bottom:0;background:var(--bg);border-radius:22px 22px 0 0;padding:10px 20px 40px;box-shadow:0 -8px 30px rgba(0,0,0,.18)}
.ph-own h3{font-size:20px;margin:12px 0 6px}.ph-own p{color:var(--ink-dim);margin:0 0 10px;font-size:15px}
.ph-cam{position:relative;background:#16181c;border-radius:20px;height:300px;display:grid;place-items:center;margin:6px 0 16px;overflow:hidden}
.ph-scr{background:#f4f5f7;border-radius:10px;padding:14px;line-height:0}
.ph-cam i{position:absolute;width:34px;height:34px;border:4px solid #fff;border-radius:6px}
.ph-cam .c1{left:56px;top:40px;border-right:0;border-bottom:0}.ph-cam .c2{right:56px;top:40px;border-left:0;border-bottom:0}
.ph-cam .c3{left:56px;bottom:40px;border-right:0;border-top:0}.ph-cam .c4{right:56px;bottom:40px;border-left:0;border-top:0}
.ph-top{margin-top:8px}
.ph-from{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:12px 0 0;font-size:14px;color:var(--ink-dim)}
.ph-near{display:inline-flex;align-items:center;gap:5px;border:1px solid var(--edge);background:var(--wash);color:var(--ink);border-radius:999px;padding:4px 10px;font-size:13px;white-space:nowrap}
.ph-near svg{color:var(--accent)}
.ph-done{margin:28px 0 0}
.ph-ab{padding:8px 14px;border-bottom:1px solid var(--line);background:var(--surface)}
.ph-abu{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--surface-2);border-radius:999px;padding:8px 12px;font-size:14px;color:var(--ink)}
.ph-abu svg{color:var(--ink-dim)}
.ph-tag{font-size:12px;color:var(--accent);font-weight:600;margin-left:6px}
.ph-col{flex-direction:column;align-items:stretch}
.ph-acts{display:flex;gap:10px;margin-top:10px}.ph-acts .pillbtn{margin:0}
.ph-warn{background:#b3261e;color:#fff;border-color:#b3261e}
.ph-when{display:grid;grid-template-columns:1.4fr 1fr;gap:10px;margin-bottom:14px}
.ph-qr{display:grid;place-items:center;background:#f4f5f7;border-radius:16px;padding:16px;margin:4px 0 14px;line-height:0}
.ph-pin{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:36px;font-family:Roboto,var(--font-text)}
.km .ph-pin{font-family:var(--font-khmer),var(--font-text)}
.ph-pin h3{font-size:22px;font-weight:500;margin:0 0 4px}.ph-pin .sub{font-size:14px;color:var(--ink-dim)}
.ph-pin .ph-desc{text-align:center;margin:14px 8px 0}
.ph-pinlbl{margin:34px 0 12px;font-size:15px;color:var(--ink-dim)}
.ph-dots{display:flex;gap:16px;margin-bottom:30px}.ph-dots i{width:12px;height:12px;border-radius:50%;border:2px solid var(--ink-dim)}.ph-dots i.on{background:var(--ink);border-color:var(--ink)}
.ph-pad{display:grid;grid-template-columns:repeat(3,72px);gap:14px 34px}.ph-pad span{height:56px;display:grid;place-items:center;font-size:26px;border-radius:50%}
.ph-pad span:not(:empty){background:var(--surface-2)}
.ph-pin .ph-neg{align-self:flex-start;margin-top:auto;padding:0 10px 6px}
.ph-disc{margin-top:22px}
.ph-cap{font-size:13px;color:var(--ink-dim);margin:16px 0 6px}
"""

_PERSON = r"ផ្ទៀងផ្ទាត់|\bverif(?:y|ied|ies|ication)\b|\bhumans?\b|\bproves?\b|\bproof of (?:who|you|a person)|\bauthentic|\bgenuine\b"
BARRED = [
    (_PERSON, "a press shows a key pressed, never a fact about the person (SPEC §0, §3)"),
    (r"bank[\s-]?(?:level|grade)", "never 'bank-level' (SPEC §0)"),
    (r"\bsign[\s-]?in\b", "Log in authenticates; 'sign in' is barred (Default 10)"),
    (r"\bdeposits?\b|\binterest\b|\bsavings\b|\byield\b|\bbank\b", "no regulated word outside the disclosure (Default 2)"),
    (r"\bremaining\b|\bexpir|\bcountdown\b|\btime left\b|\bdays? left\b|\blast (?:used|pressed)\b|\bnot pressed\b|\bstreak",
     "presence only: no time remaining, no last-used, no 'not pressed' (Sig-8)"),
    (r"\b\d+ (?:presses|times|signatures|records|keys)\b|\byou(?:'ve| have) pressed\b", "never a count (Sig-8)"),
    (r"\b(?:oppo|samsung|pixel|xiaomi|vivo|realme|huawei|motorola|nokia|iphone|google)\b|\b(?:TEE|StrongBox|KeyMint|Keystore|TrustZone)\b",
     "no phone make or model and no chip jargon (public repo; layperson copy)"),
    (r"\b(?:com|eco|org|io|net)\.[a-z0-9_]+\.[a-z0-9_.]+|apk-key-hash|\b[0-9a-f]{40,}\b|\bandroid:", "no package name or signing digest (public repo)"),
    (r"\bwallet\b|\bvot(?:e|ing)\b|\bunique(?:ness)?\b|B-Vouch|password manager|\bbalance\b|\bpay(?:s|ment)?\b",
     "not in v0: no wallet, money, uniqueness, voting, B-Vouch or password manager (SPEC §5.6)"),
    (r"notar", "'notary' is barred in public copy"),
]


def check(sid, body):
    text = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
    text = text.replace(DISCLAIMER, "")          # the disclosure is the one place a banking word belongs
    text = re.sub(r"<[^>]+>", " ", text)
    for pat, why in BARRED:
        m = re.search(pat, text, re.I)
        assert not m, "%s: %r — %s" % (sid, m.group(0), why)
    if sid in ("P6", "P6b", "P7", "P10"):
        assert re.search(r"asks you to sign|សុំឱ្យអ្នកចុះហត្ថលេខា", text), "%s: a press screen names who asked" % sid
        assert body.count('class="ph-w"') == 5, "%s: the words are shown whole (five fields)" % sid
    if sid == "P13":
        assert re.search(r"can't see those words|មិនអាចមើលឃើញពាក្យ", text), "P13: a provider press says this app can't see the words (F1+F4)"
    if sid == "P12b":
        assert re.search(r"doesn't name this phone|មិនដាក់ឈ្មោះទូរស័ព្ទនេះ", text) and re.search(r"usual passkey manager|passkey ធម្មតា", text), \
            "P12b: says what the website receives, that it doesn't name the phone, and the way out (founder 2026-11-25, item 3)"
        assert re.search(r"ends if a new finger or face|ម្រាមដៃ ឬមុខថ្មី", text), "P12b: says before the press that a finger-made passkey ends on a new finger or face (SPEC §4)"
    if sid == "P19":
        assert 'class="ph-near"' in body and re.search(r"asks you to approve|សុំឱ្យអ្នកអនុម័ត", text), "P19: an approval names who asks and needs nearness (F2)"
    if sid == "P22":
        assert re.search(r"can't be undone|មិនអាចត្រឡប់វិញបានទេ", text) and re.search(r"same phone|ទូរស័ព្ទតែមួយ", text), \
            "P22: a report says once that it is public, links the shared presses of that phone, and can't be undone"
    if sid == "P21":
        assert re.search(r"Lost or stolen|បាត់ ឬត្រូវគេលួច", text) and re.search(r"report it instead|រាយការណ៍ជំនួសវិញ", text), "P21: both acts, and which to pick"
    if sid == "P1":
        assert re.search(r"Not who is holding|មិនមែនថាអ្នកណាកំពុងកាន់", text), "P1: says what a press shows, and what it doesn't"
    if sid == "P17":
        assert DISCLAIMER in body, "P17: the not-a-chartered-bank paragraph (B2), in English on both boards"


def page(sid, body, t, lang, dark):
    """A native board: no web header or footer, no share button; the band on a Khmer board."""
    check(sid, body)
    body = body.replace("℠", '<span class="sm">℠</span>')
    return ("""<!doctype html>
<html lang="%s" class="%s%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=390">
<meta name="googlebot" content="noindex,nofollow"><meta name="bingbot" content="noindex,nofollow">
<meta name="slurp" content="noindex,nofollow"><meta name="yandex" content="noindex,nofollow">
<title>333.eco drawings · %s</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>[hidden]{display:none!important}</style>
<link rel="stylesheet" href="board.css?v=@CSSV@">
</head>
<body>
%s<div class="ph-root">
%s
</div>
</body>
</html>
""" % (lang, lang, " dark" if dark else "", sid, '<div class="band">%s</div>' % t["band"] if t["band"] else "", body))
