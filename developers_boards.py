"""developers.333.eco: one site for every HeartBank® API, its MCP server and its sandbox (A600; the spec is private,
333eco/developers.333.eco SPEC.md). Imported by build-boards.py, which injects the shared helpers and draws the pages.

Copy rules this file must keep (checked at build time by check()):
  - "Log in" authenticates, "Sign" attests; ⛔ "sign in" never (build-boards.py refuses it on every board).
  - ⚠️ A B-Trace CHECK through the API is METERED (free only in the portal); only a SIGNATURE's verification is free everywhere
    (founder 2026-11-10: "checking via API is also metered; memory seems to always confuse this subtlety").
  - ⛔ No real company, product or model is named: an agent is "your-agent.example", an app is the estate's made-up Pixel Wild.
  - ⛔ No count, streak or countdown about people; usage is the developer's own plain figures.
  - Unruled prices are drawn as placeholders and say so.
The Khmer is OURS and UNREVIEWED; the shared band says so on every Khmer board.
"""
import html as _h

# injected by build-boards.py
card = btns = spot = heart = person = None

APP, APP_HOST, AGENT = "Pixel Wild", "pixelwild.app", "your-agent.example"

DT = {
"en": {
  "foot": "developers.333.eco · drawings · nothing here is live",
  "prod": "Developers",
  "nav": ("Apps", "Keys", "Usage", "Balance"),
  # D1 the front door
  "d1_h": "Build with HeartBank®",
  "d1_lede": "One site for every door: log people in, sign files, record thanks, and check it all yourself. Your agent can build with you.",
  "d1_cards": (("Log in with HeartBank®", "Prove who someone is, with a passkey. No passwords. Each app gets its own ID for a person.", "key"),
               ("Sign with HeartBank®", "Put a person's name to one file, with a fresh passkey signature over its fingerprint.", "file"),
               ("Thank with HeartBank®", "Record a thank on the gratitude ledger. You prepare it, the person presses, you send it back.", "thank"),
               ("Verify, free", "Check the public logs, receipts and the zero-sum proof yourself. No key needed.", "log")),
  "d1_agent": "An agent can do everything except the press. Every thank needs the person's own passkey.",
  "d1_btn": "Read the docs", "d1_btn2": "Add the MCP server",
  "d1_bank": "HeartBank® is a data bank of gratitude. It is not a chartered bank or financial institution; it does not provide banking services, hold deposits, or extend credit. Nothing is paid through these APIs: Sign is paid for from a prepaid balance at billing.thonly.com.",
  # D2 Thank
  "d2_h": "Thank with HeartBank®",
  "d2_lede": "Record a thank on the gratitude ledger. Your app never writes a thank alone: the person signs it with their own passkey.",
  "d2_steps": (("1  Prepare", "Your server asks the ledger. It answers with a ticket."),
               ("2  The person presses", "They open sign.333.eco, which shows them what they are signing, and press their passkey."),
               ("3  Commit", "Your server sends the press back. The ledger writes the thank and gives you a receipt.")),
  "d2_code": 'const { pending, ticket } = await ledger.prepare({ ref, ledger: "kiitos", to })\n'
             '// the person presses at sign.333.eco/press#ticket=…\n'
             'const { receipt } = await ledger.commit({ ref, pending, pressToken })',
  "d2_c1h": "Outside apps: from season 2", "d2_c1p": "Apps outside HeartBank® write from 7 January 2027, after review.",
  "d2_c2h": "Kiitos, and Kiitti as thanks to all of life", "d2_c2p": "An outside app writes Kiitos, and Kiitti only as a person's thanks to all of life. Care for a plant or an animal is witnessed, never claimed by an app.",
  "d2_c3h": "A refusal says nothing", "d2_c3p": "When the ledger declines a thank, your app is told only that it wasn't written. No reason and no count: it protects the people involved. It is not a bug.",
  # D3 Log in
  "d3_h": "Log in with HeartBank®",
  "d3_lede": "Passkeys only. Each app sees its own ID for a person, never one another app can match.",
  "d3_b1": "Log in with HeartBank®", "d3_b2": "Connect HeartBank®",
  "d3_bnote": "The second button is for people adding HeartBank® to an account they already have in your app.",
  "d3_self_h": "Register by publishing one file",
  "d3_self_p": "Your app's ID is the address of a small file on your own site: your name, where log-ins return, where your keys are. We read it at every log-in, so nothing is verified once and trusted after.",
  "d3_code": '{\n  "client_id": "https://pixelwild.app/heartbank.json",\n  "client_name": "Pixel Wild",\n'
             '  "redirect_uris": ["https://pixelwild.app/login/callback"],\n  "jwks_uri": "https://pixelwild.app/jwks.json"\n}',
  "d3_scopes_h": "What an app may ask for",
  "d3_scopes": (("Log in", "Ready at once"), ("Verified human", "After review"), ("The ledger", "After review")),
  # D4 Sign
  "d4_h": "Sign with HeartBank®",
  "d4_lede": "A fresh passkey signature over one file's fingerprint. A log-in can never sign: each signature is its own press.",
  "d4_rows": (("Sign a file", "Metered"), ("Check a file for traces (B-Trace) through the API", "Metered"),
              ("Check a file for traces in the portal", "Free"), ("Verify a record's signature", "Free, anywhere, no key")),
  "d4_code": 'const record = await origin.attest(fileHash, { label })\n// the person presses at sign.333.eco\n'
             'await verify(record)   // free, offline: @333eco/origin-verify',
  "d4_c1h": "The file never leaves", "d4_c1p": "Only its fingerprint is signed. The file stays wherever it is.",
  # D5 agents
  "d5_h": "Your agent can build with you",
  "d5_lede": "Add one MCP server. Press your passkey once, and your agent can read the docs, register apps and run the sandbox.",
  "d5_code": "https://developers.333.eco/mcp",
  "d5_tools_h": "Tools",
  "d5_tools": (("search_docs", "Every page of these docs"), ("lookup", "An @name or #tag, and what it names"),
               ("verify_receipt", "A receipt against the public log"), ("my_apps", "Your apps, after your passkey"),
               ("sandbox_thank", "Prepare, test press, commit: in the sandbox only")),
  "d5_skills_h": "Skills",
  "d5_skills": (("Add Log in with HeartBank®", "Passkey first; log out ends both sessions"),
                ("Add Thank with HeartBank®", "Never pre-fill a thank; the press is the person's"),
                ("Sign a file", "Log in is never sign"), ("Verify a receipt", "And the zero-sum proof")),
  "d5_note": "An agent can do everything except the press. No tool writes a real thank or presses for anyone.",
  # D6 pricing
  "d6_h": "Prices",
  "d6_lede": "Stated once. Paid from a prepaid balance; no subscription.",
  "d6_rows": (("Log in with HeartBank®", "Free"), ("Verify: logs, receipts, the zero-sum proof, a record's signature", "Free"),
              ("Thank with HeartBank®", "Free [ placeholder: not yet ruled ]"), ("Lookup", "[ placeholder: not yet ruled ]"),
              ("Sign a file", "Metered"), ("Check a file for traces (B-Trace) through the API", "Metered (free in the portal)")),
  "d6_fine": "The balance lives at billing.thonly.com. It is never spent on anything you did not ask for.",
  # D7 sandbox
  "d7_h": "The sandbox",
  "d7_lede": "A copy of everything with nothing real in it: a test ledger, a test log-in, and test passkeys your agent can press without a phone.",
  "d7_c1h": "Nothing reaches the public log", "d7_c1p": "The sandbox has its own log. Not one entry of it ever enters the real one.",
  "d7_c2h": "Test passkeys", "d7_c2p": "The sandbox holds a test passkey for you, so a whole integration runs end to end. A real thank always needs a person's own passkey.",
  "d7_c3h": "Wiped every week", "d7_c3p": "Start fresh any time; keep nothing you need there.",
  # D8 your apps
  "d8_h": "Your apps",
  "d8_apps": ((APP, APP_HOST, ("Log in", "Sign")), ("Pixel Wild (test)", "localhost:5173", ("Sandbox",))),
  "d8_btn": "Register an app",
  # D9 register
  "d9_h": "Register an app",
  "d9_lede": "Give us the address of your app's file. We read it now, and again at every log-in.",
  "d9_field": "Your app's ID (an address on your own site)",
  "d9_val": "https://pixelwild.app/heartbank.json",
  "d9_checks_h": "What we found",
  "d9_checks": (("The file", "Found on pixelwild.app"), ("Name", APP), ("Where log-ins return", "Only on pixelwild.app"), ("Your keys", "pixelwild.app/jwks.json")),
  "d9_ready": "Log in with HeartBank® is ready now. Verified human, the ledger and Thank ask for review.",
  "d9_btn": "Register",
  # D10 one app
  "d10_h": APP,
  "d10_key_h": "New key", "d10_key": "hb_live_7Qe2…wX4m", "d10_once": "Shown once. We keep only its fingerprint.", "d10_copy": "Copy",
  "d10_use_h": "This month", "d10_use": (("Log-ins", "1,204"), ("Signed files", "38")),
  "d10_pause": "Pause this app's writing", "d10_pauses": "Takes effect at once. Reading goes on.",
  "d10_export": "Download everything about this app",
  # L11 the narrow door, at login.333.eco
  "l11_h": "An agent wants to work on your developer account",
  "l11_lede": "It can read the docs, register apps and run the sandbox. It can never press for anyone, write a real thank, or see anyone's data.",
  "l11_local_h": "It runs on this computer", "l11_local_p": "Its address is localhost. Only continue if you just started this agent yourself.",
  "l11_btn": "Allow with my passkey", "l11_no": "Not now",
  # D11 review
  "d11_h": "Asking for review",
  "d11_rows": ((APP, "Verified human · pixelwild.app"), ("Sunfield Market", "Thank (season 2) · sunfield.example")),
  "d11_yes": "Approve", "d11_no": "Decline",
},
"km": {
  "foot": "developers.333.eco · គំនូរ · គ្មានអ្វីនៅទីនេះដំណើរការពិតទេ",
  "prod": "អ្នកអភិវឌ្ឍ",
  "nav": ("កម្មវិធី", "កូនសោ", "ការប្រើប្រាស់", "សមតុល្យ"),
  "d1_h": "បង្កើតជាមួយ HeartBank®",
  "d1_lede": "គេហទំព័រតែមួយសម្រាប់ទ្វារទាំងអស់៖ ឱ្យមនុស្សចូល ចុះហត្ថលេខាលើឯកសារ កត់ត្រាការអរគុណ ហើយពិនិត្យវាទាំងអស់ដោយខ្លួនឯង។ ភ្នាក់ងាររបស់អ្នកអាចបង្កើតជាមួយអ្នក។",
  "d1_cards": (("Log in with HeartBank®", "បញ្ជាក់ថានរណាម្នាក់ជានរណា ដោយប្រើ passkey។ គ្មានពាក្យសម្ងាត់។ កម្មវិធីនីមួយៗទទួលបាន ID ផ្ទាល់ខ្លួនសម្រាប់មនុស្សម្នាក់។", "key"),
               ("Sign with HeartBank®", "ដាក់ឈ្មោះមនុស្សម្នាក់លើឯកសារមួយ ដោយហត្ថលេខា passkey ថ្មីលើស្នាមម្រាមដៃរបស់វា។", "file"),
               ("Thank with HeartBank®", "កត់ត្រាការអរគុណក្នុងបញ្ជីនៃការដឹងគុណ។ អ្នករៀបចំវា មនុស្សនោះចុច ហើយអ្នកផ្ញើវាត្រឡប់មកវិញ។", "thank"),
               ("ការផ្ទៀងផ្ទាត់ ដោយឥតគិតថ្លៃ", "ពិនិត្យកំណត់ហេតុសាធារណៈ បង្កាន់ដៃ និងភស្តុតាងផលបូកសូន្យដោយខ្លួនឯង។ មិនត្រូវការកូនសោទេ។", "log")),
  "d1_agent": "ភ្នាក់ងារអាចធ្វើអ្វីៗគ្រប់យ៉ាង លើកលែងតែការចុច។ ការអរគុណនីមួយៗត្រូវការ passkey ផ្ទាល់ខ្លួនរបស់មនុស្សនោះ។",
  "d1_btn": "អានឯកសារណែនាំ", "d1_btn2": "បន្ថែមម៉ាស៊ីនមេ MCP",
  "d1_bank": "HeartBank® គឺជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ វាមិនមែនជាធនាគារដែលមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ វាមិនផ្តល់សេវាធនាគារ មិនទទួលប្រាក់បញ្ញើ ឬផ្តល់ឥណទានទេ។ គ្មានអ្វីត្រូវបានបង់តាម API ទាំងនេះទេ៖ Sign ត្រូវបានបង់ពីសមតុល្យបង់មុននៅ billing.thonly.com។",
  "d2_h": "Thank with HeartBank®",
  "d2_lede": "កត់ត្រាការអរគុណក្នុងបញ្ជីនៃការដឹងគុណ។ កម្មវិធីរបស់អ្នកមិនដែលសរសេរការអរគុណតែឯងទេ៖ មនុស្សនោះចុះហត្ថលេខាវាដោយ passkey ផ្ទាល់ខ្លួន។",
  "d2_steps": (("១  រៀបចំ", "ម៉ាស៊ីនមេរបស់អ្នកសួរបញ្ជី។ វាឆ្លើយដោយសំបុត្រមួយ។"),
               ("២  មនុស្សនោះចុច", "ពួកគេបើក sign.333.eco ដែលបង្ហាញពួកគេនូវអ្វីដែលពួកគេកំពុងចុះហត្ថលេខា ហើយចុច passkey របស់ពួកគេ។"),
               ("៣  បញ្ជូន", "ម៉ាស៊ីនមេរបស់អ្នកផ្ញើការចុចត្រឡប់មកវិញ។ បញ្ជីសរសេរការអរគុណ ហើយផ្តល់បង្កាន់ដៃឱ្យអ្នក។")),
  "d2_c1h": "កម្មវិធីខាងក្រៅ៖ ចាប់ពីរដូវកាលទី ២", "d2_c1p": "កម្មវិធីក្រៅពី HeartBank® សរសេរចាប់ពីថ្ងៃទី ៧ ខែមករា ឆ្នាំ ២០២៧ បន្ទាប់ពីការពិនិត្យ។",
  "d2_c2h": "Kiitos និង Kiitti ជាការអរគុណចំពោះជីវិតទាំងអស់", "d2_c2p": "កម្មវិធីខាងក្រៅសរសេរ Kiitos ហើយ Kiitti តែជាការអរគុណរបស់មនុស្សចំពោះជីវិតទាំងអស់ប៉ុណ្ណោះ។ ការថែទាំរុក្ខជាតិ ឬសត្វ ត្រូវបានធ្វើជាសាក្សី មិនដែលអះអាងដោយកម្មវិធីទេ។",
  "d2_c3h": "ការបដិសេធមិននិយាយអ្វីទេ", "d2_c3p": "នៅពេលបញ្ជីបដិសេធការអរគុណ កម្មវិធីរបស់អ្នកត្រូវបានប្រាប់តែថាវាមិនត្រូវបានសរសេរ។ គ្មានហេតុផល គ្មានចំនួន៖ វាការពារមនុស្សដែលពាក់ព័ន្ធ។ វាមិនមែនជាកំហុសទេ។",
  "d3_h": "Log in with HeartBank®",
  "d3_lede": "មានតែ passkey ប៉ុណ្ណោះ។ កម្មវិធីនីមួយៗឃើញ ID ផ្ទាល់ខ្លួនសម្រាប់មនុស្សម្នាក់ មិនដែលជា ID ដែលកម្មវិធីផ្សេងអាចផ្គូផ្គងបានទេ។",
  "d3_b1": "Log in with HeartBank®", "d3_b2": "Connect HeartBank®",
  "d3_bnote": "ប៊ូតុងទីពីរគឺសម្រាប់មនុស្សដែលបន្ថែម HeartBank® ទៅគណនីដែលពួកគេមានរួចហើយក្នុងកម្មវិធីរបស់អ្នក។",
  "d3_self_h": "ចុះឈ្មោះដោយបោះពុម្ពឯកសារមួយ",
  "d3_self_p": "ID កម្មវិធីរបស់អ្នក គឺជាអាសយដ្ឋាននៃឯកសារតូចមួយនៅលើគេហទំព័ររបស់អ្នក៖ ឈ្មោះរបស់អ្នក កន្លែងដែលការចូលត្រឡប់មកវិញ កន្លែងដែលកូនសោរបស់អ្នកនៅ។ យើងអានវារាល់ពេលចូល ដូច្នេះគ្មានអ្វីត្រូវបានផ្ទៀងផ្ទាត់ម្តង ហើយជឿទុកចិត្តតទៅទេ។",
  "d3_scopes_h": "អ្វីដែលកម្មវិធីអាចស្នើសុំ",
  "d3_scopes": (("Log in", "រួចរាល់ភ្លាមៗ"), ("មនុស្សដែលបានផ្ទៀងផ្ទាត់", "បន្ទាប់ពីការពិនិត្យ"), ("បញ្ជី", "បន្ទាប់ពីការពិនិត្យ")),
  "d4_h": "Sign with HeartBank®",
  "d4_lede": "ហត្ថលេខា passkey ថ្មីលើស្នាមម្រាមដៃរបស់ឯកសារមួយ។ ការចូលមិនអាចចុះហត្ថលេខាបានទេ៖ ហត្ថលេខានីមួយៗជាការចុចផ្ទាល់ខ្លួន។",
  "d4_rows": (("ចុះហត្ថលេខាលើឯកសារ", "គិតតាមការប្រើ"), ("ពិនិត្យឯកសាររកដាន (B-Trace) តាម API", "គិតតាមការប្រើ"),
              ("ពិនិត្យឯកសាររកដាននៅក្នុងវិបផតថល", "ឥតគិតថ្លៃ"), ("ផ្ទៀងផ្ទាត់ហត្ថលេខារបស់កំណត់ត្រា", "ឥតគិតថ្លៃ គ្រប់ទីកន្លែង គ្មានកូនសោ")),
  "d4_c1h": "ឯកសារមិនដែលចាកចេញទេ", "d4_c1p": "មានតែស្នាមម្រាមដៃរបស់វាប៉ុណ្ណោះដែលត្រូវបានចុះហត្ថលេខា។ ឯកសារនៅកន្លែងដែលវានៅ។",
  "d5_h": "ភ្នាក់ងាររបស់អ្នកអាចបង្កើតជាមួយអ្នក",
  "d5_lede": "បន្ថែមម៉ាស៊ីនមេ MCP មួយ។ ចុច passkey របស់អ្នកម្តង ហើយភ្នាក់ងាររបស់អ្នកអាចអានឯកសារណែនាំ ចុះឈ្មោះកម្មវិធី និងដំណើរការប្រអប់សាកល្បង។",
  "d5_tools_h": "ឧបករណ៍",
  "d5_tools": (("search_docs", "គ្រប់ទំព័រនៃឯកសារណែនាំទាំងនេះ"), ("lookup", "@name ឬ #tag និងអ្វីដែលវាដាក់ឈ្មោះ"),
               ("verify_receipt", "បង្កាន់ដៃធៀបនឹងកំណត់ហេតុសាធារណៈ"), ("my_apps", "កម្មវិធីរបស់អ្នក បន្ទាប់ពី passkey របស់អ្នក"),
               ("sandbox_thank", "រៀបចំ ចុចសាកល្បង បញ្ជូន៖ តែក្នុងប្រអប់សាកល្បងប៉ុណ្ណោះ")),
  "d5_skills_h": "ជំនាញ",
  "d5_skills": (("បន្ថែម Log in with HeartBank®", "passkey មុនគេ ការចាកចេញបញ្ចប់វគ្គទាំងពីរ"),
                ("បន្ថែម Thank with HeartBank®", "កុំបំពេញការអរគុណជាមុន ការចុចជារបស់មនុស្សនោះ"),
                ("ចុះហត្ថលេខាលើឯកសារ", "ការចូលមិនមែនជាការចុះហត្ថលេខាទេ"), ("ផ្ទៀងផ្ទាត់បង្កាន់ដៃ", "និងភស្តុតាងផលបូកសូន្យ")),
  "d5_note": "ភ្នាក់ងារអាចធ្វើអ្វីៗគ្រប់យ៉ាង លើកលែងតែការចុច។ គ្មានឧបករណ៍ណាសរសេរការអរគុណពិត ឬចុចជំនួសនរណាម្នាក់ទេ។",
  "d6_h": "តម្លៃ",
  "d6_lede": "បញ្ជាក់ម្តង។ បង់ពីសមតុល្យបង់មុន គ្មានការជាវទេ។",
  "d6_rows": (("Log in with HeartBank®", "ឥតគិតថ្លៃ"), ("ការផ្ទៀងផ្ទាត់៖ កំណត់ហេតុ បង្កាន់ដៃ ភស្តុតាងផលបូកសូន្យ ហត្ថលេខារបស់កំណត់ត្រា", "ឥតគិតថ្លៃ"),
              ("Thank with HeartBank®", "ឥតគិតថ្លៃ [ ជំនួសបណ្ដោះអាសន្ន៖ មិនទាន់សម្រេច ]"), ("Lookup", "[ ជំនួសបណ្ដោះអាសន្ន៖ មិនទាន់សម្រេច ]"),
              ("ចុះហត្ថលេខាលើឯកសារ", "គិតតាមការប្រើ"), ("ពិនិត្យឯកសាររកដាន (B-Trace) តាម API", "គិតតាមការប្រើ (ឥតគិតថ្លៃនៅក្នុងវិបផតថល)")),
  "d6_fine": "សមតុល្យនៅ billing.thonly.com។ វាមិនដែលត្រូវបានចំណាយលើអ្វីដែលអ្នកមិនបានស្នើសុំទេ។",
  "d7_h": "ប្រអប់សាកល្បង",
  "d7_lede": "ច្បាប់ចម្លងនៃអ្វីៗទាំងអស់ ដោយគ្មានអ្វីពិតនៅក្នុងវា៖ បញ្ជីសាកល្បង ការចូលសាកល្បង និង passkey សាកល្បងដែលភ្នាក់ងាររបស់អ្នកអាចចុចដោយគ្មានទូរស័ព្ទ។",
  "d7_c1h": "គ្មានអ្វីទៅដល់កំណត់ហេតុសាធារណៈទេ", "d7_c1p": "ប្រអប់សាកល្បងមានកំណត់ហេតុផ្ទាល់ខ្លួន។ គ្មានធាតុណាមួយរបស់វាចូលក្នុងកំណត់ហេតុពិតទេ។",
  "d7_c2h": "passkey សាកល្បង", "d7_c2p": "ប្រអប់សាកល្បងរក្សា passkey សាកល្បងមួយសម្រាប់អ្នក ដូច្នេះការរួមបញ្ចូលទាំងមូលដំណើរការពីដើមដល់ចប់។ ការអរគុណពិតតែងតែត្រូវការ passkey ផ្ទាល់ខ្លួនរបស់មនុស្ស។",
  "d7_c3h": "លុបរៀងរាល់សប្តាហ៍", "d7_c3p": "ចាប់ផ្តើមថ្មីនៅពេលណាក៏បាន កុំទុកអ្វីដែលអ្នកត្រូវការនៅទីនោះ។",
  "d8_h": "កម្មវិធីរបស់អ្នក",
  "d8_apps": ((APP, APP_HOST, ("Log in", "Sign")), ("Pixel Wild (សាកល្បង)", "localhost:5173", ("ប្រអប់សាកល្បង",))),
  "d8_btn": "ចុះឈ្មោះកម្មវិធី",
  "d9_h": "ចុះឈ្មោះកម្មវិធី",
  "d9_lede": "ផ្តល់អាសយដ្ឋាននៃឯកសារកម្មវិធីរបស់អ្នកមកយើង។ យើងអានវាឥឡូវនេះ និងម្តងទៀតរាល់ពេលចូល។",
  "d9_field": "ID កម្មវិធីរបស់អ្នក (អាសយដ្ឋាននៅលើគេហទំព័ររបស់អ្នក)",
  "d9_val": "https://pixelwild.app/heartbank.json",
  "d9_checks_h": "អ្វីដែលយើងបានរកឃើញ",
  "d9_checks": (("ឯកសារ", "រកឃើញនៅលើ pixelwild.app"), ("ឈ្មោះ", APP), ("កន្លែងដែលការចូលត្រឡប់មកវិញ", "តែនៅលើ pixelwild.app"), ("កូនសោរបស់អ្នក", "pixelwild.app/jwks.json")),
  "d9_ready": "Log in with HeartBank® រួចរាល់ឥឡូវនេះ។ មនុស្សដែលបានផ្ទៀងផ្ទាត់ បញ្ជី និង Thank ស្នើសុំការពិនិត្យ។",
  "d9_btn": "ចុះឈ្មោះ",
  "d10_h": APP,
  "d10_key_h": "កូនសោថ្មី", "d10_key": "hb_live_7Qe2…wX4m", "d10_once": "បង្ហាញតែម្តង។ យើងរក្សាតែស្នាមម្រាមដៃរបស់វាប៉ុណ្ណោះ។", "d10_copy": "ចម្លង",
  "d10_use_h": "ខែនេះ", "d10_use": (("ការចូល", "1,204"), ("ឯកសារដែលបានចុះហត្ថលេខា", "38")),
  "d10_pause": "ផ្អាកការសរសេររបស់កម្មវិធីនេះ", "d10_pauses": "មានប្រសិទ្ធភាពភ្លាមៗ។ ការអានបន្តទៅមុខ។",
  "d10_export": "ទាញយកអ្វីៗទាំងអស់អំពីកម្មវិធីនេះ",
  "l11_h": "ភ្នាក់ងារមួយចង់ធ្វើការលើគណនីអ្នកអភិវឌ្ឍរបស់អ្នក",
  "l11_lede": "វាអាចអានឯកសារណែនាំ ចុះឈ្មោះកម្មវិធី និងដំណើរការប្រអប់សាកល្បង។ វាមិនអាចចុចជំនួសនរណាម្នាក់ សរសេរការអរគុណពិត ឬមើលទិន្នន័យរបស់នរណាម្នាក់បានទេ។",
  "l11_local_h": "វាដំណើរការនៅលើកុំព្យូទ័រនេះ", "l11_local_p": "អាសយដ្ឋានរបស់វាគឺ localhost។ បន្តតែប្រសិនបើអ្នកទើបតែចាប់ផ្តើមភ្នាក់ងារនេះដោយខ្លួនឯង។",
  "l11_btn": "អនុញ្ញាតដោយ passkey របស់ខ្ញុំ", "l11_no": "មិនមែនឥឡូវនេះទេ",
  "d11_h": "ស្នើសុំការពិនិត្យ",
  "d11_rows": ((APP, "មនុស្សដែលបានផ្ទៀងផ្ទាត់ · pixelwild.app"), ("Sunfield Market", "Thank (រដូវកាលទី ២) · sunfield.example")),
  "d11_yes": "អនុម័ត", "d11_no": "បដិសេធ",
},
}
# code samples and the MCP address read the same in both languages
for _k in ("d2_code", "d3_code", "d4_code", "d5_code"):
    DT["km"][_k] = DT["en"][_k]


def dspot(kind):
    """Spots of this surface's own (the rest come from build-boards.py's spot())."""
    s = ['<svg class="spot" width="56" height="40" viewBox="0 0 56 40" aria-hidden="true">']
    if kind == "file":       # a file and its fingerprint
        s += ['<path d="M10 3 h18 l8 8 v26 h-26 z" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M28 3 v8 h8" fill="none" stroke="var(--line-strong)"/>',
              '<path d="M42 14 q6 6 0 12 M46 11 q9 9 0 18" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/>']
    elif kind == "thank":    # two people and a mark between them
        s += [person(13, 22, "var(--accent)", "#c99a6e", "#2a1d17", "bun", .42), person(43, 22, "#4f7a62", "#b98a63", "#2a1d17", "cap", .42),
              heart(28, 15, .5)]
    elif kind == "agent":    # a terminal window with a cursor
        s += ['<rect x="6" y="5" width="44" height="30" rx="5" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M13 15 l5 4 -5 4" fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
              '<path d="M22 24 h10" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>']
    elif kind == "box":      # the sandbox: an open box
        s += ['<path d="M8 16 l20 -8 20 8 v16 l-20 6 -20 -6 z" fill="var(--surface-2)" stroke="var(--line-strong)"/>',
              '<path d="M8 16 l20 7 20 -7 M28 23 v15" fill="none" stroke="var(--line-strong)"/>',
              '<path d="M14 9 l4 -5 M28 4 v-3 M42 9 l-4 -5" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/>']
    s.append('</svg>')
    return "".join(s)


def _spot(kind):
    return dspot(kind) if kind in ("file", "thank", "agent", "box") else spot(kind)


def _card(h, p, kind=None):
    return '<div class="card">%s<h2>%s</h2><p>%s</p></div>' % (_spot(kind) if kind else "", h, p)


def _rows(items, cls=""):
    return '<div class="card">%s</div>' % "".join(
        '<div class="row"><div><div class="t%s">%s</div></div><span class="s">%s</span></div>' % (cls, a, b) for a, b in items)


def _code(s):
    return '<pre class="code">%s</pre>' % _h.escape(s)


def _tabs(d, on):
    return '<nav class="dtabs">%s</nav>' % "".join('<a class="%s">%s</a>' % ("on" if i == on else "", x) for i, x in enumerate(d["nav"]))


def D1(t, d):
    cards = "".join(_card(h, p, k) for h, p, k in d["d1_cards"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d1_h"], d["d1_lede"]) + cards
            + '<div class="note">%s</div>' % d["d1_agent"] + btns(d["d1_btn"], d["d1_btn2"])
            + '<p class="fine" style="margin-top:18px">%s</p>' % d["d1_bank"])
def D2(t, d):
    steps = "".join('<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div></div>' % (a, b) for a, b in d["d2_steps"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d2_h"], d["d2_lede"]) + '<div class="card">%s</div>' % steps + _code(d["d2_code"])
            + _card(d["d2_c1h"], d["d2_c1p"]) + _card(d["d2_c2h"], d["d2_c2p"], "thank") + _card(d["d2_c3h"], d["d2_c3p"]))
def D3(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d3_h"], d["d3_lede"])
            + btns(d["d3_b1"], d["d3_b2"], key=True) + '<p class="fine">%s</p>' % d["d3_bnote"]
            + _card(d["d3_self_h"], d["d3_self_p"], "key") + _code(d["d3_code"])
            + '<h2 class="sh">%s</h2>' % d["d3_scopes_h"] + _rows(d["d3_scopes"]))
def D4(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d4_h"], d["d4_lede"]) + _rows(d["d4_rows"]) + _code(d["d4_code"])
            + _card(d["d4_c1h"], d["d4_c1p"], "file"))
def D5(t, d):
    tools = "".join('<div class="row"><div><div class="t mono">%s</div><div class="s">%s</div></div></div>' % (a, b) for a, b in d["d5_tools"])
    skills = "".join('<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div></div>' % (a, b) for a, b in d["d5_skills"])
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d5_h"], d["d5_lede"]) + '<div class="field mono">%s</div>' % d["d5_code"]
            + '<h2 class="sh">%s</h2><div class="card">%s</div>' % (d["d5_tools_h"], tools)
            + '<h2 class="sh">%s</h2><div class="card">%s</div>' % (d["d5_skills_h"], skills)
            + '<div class="note">%s</div>' % d["d5_note"])
def D6(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d6_h"], d["d6_lede"]) + _rows(d["d6_rows"]) + '<p class="fine">%s</p>' % d["d6_fine"])
def D7(t, d):
    return ("<h1>%s</h1><p class='lede'>%s</p>" % (d["d7_h"], d["d7_lede"]) + _card(d["d7_c1h"], d["d7_c1p"], "log")
            + _card(d["d7_c2h"], d["d7_c2p"], "box") + _card(d["d7_c3h"], d["d7_c3p"]))
def D8(t, d):
    apps = "".join('<div class="row"><div><div class="t">%s</div><div class="s mono">%s</div><div class="chips">%s</div></div></div>'
                   % (a, h, "".join('<span class="chip on">%s</span>' % x for x in z)) for a, h, z in d["d8_apps"])
    return (_tabs(d, 0) + "<h1>%s</h1>" % d["d8_h"] + '<div class="card">%s</div>' % apps + '<div class="grow"></div>' + btns(d["d8_btn"]))
def D9(t, d):
    checks = "".join('<div class="row"><div class="t">✓ %s</div><span class="s">%s</span></div>' % (a, b) for a, b in d["d9_checks"])
    return (_tabs(d, 0) + "<h1>%s</h1><p class='lede'>%s</p>" % (d["d9_h"], d["d9_lede"])
            + '<div class="card"><h2>%s</h2><div class="field mono">%s</div></div>' % (d["d9_field"], d["d9_val"])
            + '<div class="card"><h2>%s</h2>%s</div>' % (d["d9_checks_h"], checks) + '<div class="note">%s</div>' % d["d9_ready"]
            + '<div class="grow"></div>' + btns(d["d9_btn"]))
def D10(t, d):
    use = "".join('<div class="row"><div class="t">%s</div><b>%s</b></div>' % (a, b) for a, b in d["d10_use"])
    return (_tabs(d, 1) + "<h1>%s</h1>" % d["d10_h"]
            + '<div class="card" style="border-color:var(--accent)"><h2>%s</h2><div class="field mono">%s</div><p class="fine">%s</p>%s</div>'
              % (d["d10_key_h"], d["d10_key"], d["d10_once"], '<button class="btn">%s</button>' % d["d10_copy"])
            + '<div class="card"><h2>%s</h2>%s</div>' % (d["d10_use_h"], use)
            + '<div class="card"><div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><span class="tog"></span></div></div>'
              % (d["d10_pause"], d["d10_pauses"])
            + btns(d["d10_export"]).replace('class="btn"', 'class="btn ghost"'))
def L11(t, d):
    return ("<h1>%s</h1>" % d["l11_h"] + '<div class="card"><div class="big mono">%s</div><p>%s</p></div>' % (AGENT, d["l11_lede"])
            + _card(d["l11_local_h"], d["l11_local_p"], "agent") + '<div class="grow"></div>' + btns(d["l11_btn"], d["l11_no"], key=True))
def D11(t, d):
    rows = "".join('<div class="row"><div><div class="t">%s</div><div class="s">%s</div></div><span class="s">%s · %s</span></div>'
                   % (a, b, d["d11_yes"], d["d11_no"]) for a, b in d["d11_rows"])
    return "<h1>%s</h1>" % d["d11_h"] + '<div class="card">%s</div>' % rows


SCREENS = [  # (id, page, title, render(t, d)) — page "developers", except the consent screen, which is login.333.eco's
    ("D1", "developers", "Build with HeartBank®", D1), ("D2", "developers", "Thank with HeartBank®", D2),
    ("D3", "developers", "Log in with HeartBank®", D3), ("D4", "developers", "Sign with HeartBank®", D4),
    ("D5", "developers", "For agents: the MCP server", D5), ("D6", "developers", "Prices", D6), ("D7", "developers", "The sandbox", D7),
    ("D8", "developers", "Dashboard: your apps", D8), ("D9", "developers", "Register an app (its own file)", D9),
    ("D10", "developers", "One app: key, usage, pause, export", D10), ("D11", "developers", "Review (founder)", D11),
    ("L11", "login", "An agent asks for your developer account", L11),
]
PUBLIC = {"D1", "D2", "D3", "D4", "D5", "D6", "D7"}
CSS = """
.dtabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}
.dtabs a{font-size:13px;padding:6px 12px;border-radius:var(--r-pill);border:1px solid var(--line);color:var(--ink-dim)}
.dtabs a.on{border-color:var(--accent);color:var(--ink);background:var(--wash);font-weight:600}
/* a phone-width board never clips a code line or an address: it wraps (all boards; clipping hid the end of each sample) */
.code{white-space:pre-wrap;overflow-wrap:anywhere}
.field.mono{overflow-wrap:anywhere}
"""
BARRED = [  # words this surface must never draw
    (r"\bclaude\b|\bcursor\b|\bchatgpt\b|\bopenai\b|\banthropic\b|\bgemini\b", "no real company, product or model is named"),
    (r"\bstreak\b|\bleaderboard\b|\btime left\b|\bremaining\b", "no streak, ranking or countdown (Sig-8)"),
]


def check(sid, body):
    import re
    for pat, why in BARRED:
        assert not re.search(pat, body, re.I), "%s: %s" % (sid, why)
    if sid == "D4" or sid == "D6":  # the subtlety memory keeps confusing: a B-Trace check through the API is METERED
        assert re.search(r"trace.{0,40}API", body, re.I), "%s: the B-Trace check through the API must be drawn as metered" % sid
