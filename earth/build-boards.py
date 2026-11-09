#!/usr/bin/env python3
"""Generate the earth.333.eco artboards, canvas.json and the board stylesheet.

One source for both languages and both themes, so the artboards cannot drift from each other. The spec is private
(HeartBank/ledger.heartbank.net SPEC §8.1); this public repo holds drawings only, with made-up entries.
Khmer below is OURS and marked as a placeholder on every board until a native reader approves it.

    python3 build-boards.py && python3 -m http.server 8333 &  python3 measure.py && python3 build-boards.py && python3 build-index.py && python3 build-wall.py
"""
import hashlib, io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from brand import EMBLEM, tok  # the vendored brand layer: the emblem and the neutrals are READ, never typed here

APP_HOST = "earth.333.eco"
LEDGER_LINK = "explorer.333.eco/ledger"

T = {
    "en": {
        "lang": "en", "share": "Share", "ph": "",
        "h1": "A private record of your thanks.",
        "para": ("When you thank someone on a HeartBank® app, this service keeps an encrypted note that it happened. We timestamp "
                 "a fingerprint of that note to a public ledger, so it can't be changed later without showing. The note itself stays "
                 "private and yours: you can open it here and download it. What you wrote, and any amount or time, stays in the app you "
                 "used. Nothing is paid here."),
        "cta": "See my record",
        "cta_note": "You'll log in with HeartBank®, using a passkey: the face or fingerprint you already use to open your phone.",
        "pub": "Check the public ledger yourself",
        "visits": "Visits to this page are counted without cookies.",
        "who1": "Founded by Thon Ly", "who2": "Miss Aquarius℠ is the CEO",
        "disc": ("HeartBank® is a planetary data bank of gratitude. It is not a chartered bank or financial institution; it does not "
                 "provide banking services, hold deposits, or extend credit. Nothing is paid here: this service keeps a record of thanks "
                 "and moves no money. Financial services are not provided by HeartBank."),
        "you_h": "Your record",
        "you_sub": "Each line is one entry, exactly as it was kept. Each entry shows your side only. Every time this page is opened, the opening is logged, and what it shows is not.",
        "legend": "<b>Kiitos</b> is a thank between two people. <b>Kiitti</b> is care for a thing, a plant or an animal.",
        "dl": "Download my record",
        "dl_note": "The file holds every entry and what you need to check it yourself, even if this service is ever gone. Keep it private: it proves your side.",
        "season": "Season 1 · 26 November 2026 to 7 January 2027",
        "rows": [("thank_out", "You thanked someone", "Kiitos", "333.eco", "2 Dec 2026, 9:41 AM"),
                 ("thank_in", "Someone thanked you", "Kiitos", "333.eco", "30 Nov 2026, 6:12 PM"),
                 ("plant", "You came back to a plant", "Kiitti", "B-Twin", "29 Nov 2026, 8:03 AM"),
                 ("thing", "You thanked a thing", "Kiitti", "B-Twin", "28 Nov 2026, 7:55 PM"),
                 ("animal", "You came back to an animal", "Kiitti", "B-Twin", "27 Nov 2026, 10:20 AM")],
        "kinds": {"care": {"thing": "You came back to a thing", "plant": "You came back to a plant", "animal": "You came back to an animal"},
                  "thanks": {"thing": "You thanked a thing", "plant": "You thanked a plant", "animal": "You thanked an animal"}},
        "seasons": {"1": "Season 1 · 26 November 2026 to 7 January 2027"},
        "thanked": "You thanked someone", "was_thanked": "Someone thanked you",
        "privacy_link": "Privacy", "terms_link": "Terms", "home_link": "Back to the front page",
        "earth_h1": "Every thank makes a crest and a trough.",
        "earth_sub": "The kind rise and the thankful fall by the same amount, so the sea never gets higher. It only moves.",
        "crest": "Crest", "crest_means": "kind", "trough": "Trough", "trough_means": "thankful", "color_means": "how often a place crosses zero",
        "earth_opens": "Season 1 opens on 26 November 2026.", "about_link": "What is this?",
        "card_place": "This part of the world, about 100 km across",
        "sample_short": "Made-up numbers to help you imagine it, until Season 1 opens on 26 November 2026.",
        "sample_note": "These numbers are made up, to help you imagine what this will look like. The real ledger begins when Season 1 opens on 26 November 2026, and these disappear by themselves.",
        "sample_day": "Day",
        "scholars_link": "For scholars",
        "scholars_title": "Questions the ledger could answer",
        "scholars_sub": "A scholar will be able to ask how gratitude moves through people, and get a comparison back: never a row, a pair, a person, a place or a rate.",
        "scholars_banner": "Everything on this page is made up. The people are simulated, and we wrote the patterns into them ourselves, so these results say nothing about real people. It runs the real rules on invented data, to help you imagine the research. The door is not open yet.",
        "sch_pick": "Try a question",
        "sch_group": "Group", "sch_share": "Share", "sch_range": "With its noise",
        "sch_gap": "Difference", "sch_each": "Each group is at least 50 people.",
        "sch_refused_h": "Refused", "sch_refused_p": "One of these groups is smaller than 50 people, so nothing comes back: no share, no count, not even how small it was. The code refuses it; no reviewer has to notice.",
        "sch_rules_h": "How the real door will work",
        "sch_rules": ["You write down the question, the hypothesis and the decision rule first, and it is published with a timestamp before it runs.", "It is reviewed by a person. Miss Aquarius\u2120 never chooses which questions are asked.", "Only finished seasons are studied, so no answer is about the present.", "It runs inside the service, every read logged. Only the comparison leaves.", "Every group is at least 50 people, every answer carries noise, and each season has a fixed budget, so many small questions cannot add up to one person."],
        "q_forward": "Of people thanked in a week, how many thanked someone the next week, against those who were not thanked?",
        "q_forward_a": "Were thanked", "q_forward_b": "Were not thanked", "q_forward_o": "Thanked someone the next week",
        "q_both": "Do people who both care and say thanks cross zero more often than people who only care?",
        "q_both_a": "Care and thanks", "q_both_b": "Care only", "q_both_o": "Crossed zero at least once",
        "q_kind": "Do people who care for something alive come back more than people who care for a thing?",
        "q_kind_a": "A plant or an animal", "q_kind_b": "A thing", "q_kind_o": "Came back the next week",
        "q_circle": "Do people who received before they gave keep giving longer than people who gave first?",
        "q_circle_a": "Received first", "q_circle_b": "Gave first", "q_circle_o": "Still thanking in the last week",
        "q_single": "What did the single person who thanked first this season do next?",
        "q_single_a": "The first person", "q_single_b": "Everyone else", "q_single_o": "Thanked again",
        "proof_link": "The zero-sum proof",
        "proof_title": "The zero-sum proof",
        "proof_sub": "Every thank moves the same amount up for one side and down for the other, so each sea adds up to zero. This proof lets anyone check that from the public log, without seeing a single thank.",
        "proof_checks_h": "What it checks",
        "proof_checks": ["Every counted thank carries a passkey press, with the person present and verified, over that exact thank.", "Each one moves exactly its rule's amount from one account to another, and is counted once.", "The chain starts from zero, at the log's first entry."],
        "proof_limits_h": "What it cannot show",
        "proof_limits": ["A passkey shows that someone holds a key, not that they are one human.", "Two people can still thank each other for show.", "A thank left out of the proof looks like padding. The person whose thank it is can find that out when the season ends.", "It does not check the log's own signature. explorer.333.eco/ledger does that."],
        "proof_lag": "Proofs are made each night, so the newest day is not in them yet.",
        "proof_go": "Check it in your browser",
        "proof_deep": "Check every proof (slower)",
        "proof_busy": "Checking…",
        "proof_good": "Checked in your browser, every counted thank in log entries",
        "proof_none": "No proof has been published yet. The first comes after Season 1 opens.",
        "proof_bad": "This did not check out:",
        "proof_failed": "The check could not run:",
        "ledger_title": "The ledger, day by day",
        "ledger_sub": "Each closed day: every area about 100 km across where at least two sides were counted. No name, no person and no single thank is here.",
        "ledger_area": "Area", "ledger_map": "On the map", "ledger_open": "In the open sea", "ledger_total": "Added together",
        "ledger_zero": "The zero is how the ledger is built: every thank takes one from the thankful and gives one to the kind. This table shows where the balances sit. It does not prove the zero by itself. For Kiitti, the open sea also holds the side of the things, plants and animals.",
        "ledger_json": "The same data as a file", "ledger_title_tag": "The ledger, day by day · HeartBank®",
        "draft_note": "This is a draft. No lawyer has reviewed it, and it may change before it is final. Where something is not settled yet, it says so.",
        "copied": "Copied", "working": "Working", "auto": "Auto", "light": "Light", "dark": "Dark",
        "title_home": "Every thank makes a crest and a trough · HeartBank®", "title_you": "Your record · HeartBank®",
        "desc": "Every thank on HeartBank® makes a crest and a trough on a turning Earth. The kind rise, the thankful fall by the same amount, and the sea never gets higher.",
        "desc_ledger": "The public sea, day by day and area by area: what is on the map, what is in the open sea, and what they add up to.",
        "desc_scholars": "The kinds of question a scholar could ask of the gratitude ledger, and the comparison that comes back. Worked here on simulated people.",
        "receipt": "Receipt", "r_place": "Place in the log", "r_finger": "Fingerprint", "r_log": "Log", "r_sig": "Signature",
        "copy": "Copy receipt", "check": "Check it on the public ledger",
        "jubilee": "On 7 January every balance starts again from zero. These entries stay.",
        "leave": "When you leave this page, you'll need your passkey to open it again.",
        "none_p": "This is where your entries will appear. When you thank someone on a HeartBank® app, or someone thanks you, it shows up here.",
        "pk_h": "This page opens with a passkey",
        "pk_p": "A passkey is the face or fingerprint you already use to open your phone. It proves the person opening this record is you. Add one to your HeartBank® account, then come back.",
        "pk_btn": "Add a passkey",
        "err_h": "This page can't open right now",
        "err_p": "Nothing in your record has changed. Try again in a little while.",
        "err_btn": "Try again",
        "st_none": "State · nothing yet", "st_pk": "State · needs a passkey", "st_err": "State · can't open",
        "tag": "[ Drawing. Nothing here is live, and these entries are made up. ]",
    },
    "km": {
        "lang": "km", "share": "ចែករំលែក", "ph": "ខ្មែរនេះជាពាក្យរង់ចាំ មុននឹងមានការអនុម័ត",
        "h1": "កំណត់ត្រាឯកជននៃការអរគុណរបស់អ្នក",
        "para": ("ពេលអ្នកអរគុណនរណាម្នាក់នៅលើកម្មវិធី HeartBank® សេវានេះរក្សាកំណត់ចំណាំដែលបានអ៊ិនគ្រីបមួយថាវាបានកើតឡើង។ "
                 "យើងបោះត្រាពេលវេលាលើស្នាមម្រាមដៃឌីជីថលនៃកំណត់ចំណាំនោះទៅក្នុងបញ្ជីសាធារណៈ ដូច្នេះវាមិនអាចត្រូវបានផ្លាស់ប្តូរនៅពេលក្រោយដោយមិនបង្ហាញឲ្យឃើញឡើយ។ "
                 "កំណត់ចំណាំនោះនៅតែឯកជន ហើយជារបស់អ្នក៖ អ្នកអាចបើកមើលនៅទីនេះ និងទាញយកបាន។ "
                 "អ្វីដែលអ្នកបានសរសេរ និងចំនួនប្រាក់ ឬពេលវេលាណាមួយ នៅតែស្ថិតក្នុងកម្មវិធីដែលអ្នកបានប្រើ។ គ្មានការបង់ប្រាក់នៅទីនេះទេ។"),
        "cta": "មើលកំណត់ត្រារបស់ខ្ញុំ",
        "cta_note": "អ្នកនឹងចូលជាមួយ HeartBank® ដោយប្រើ passkey គឺមុខ ឬស្នាមម្រាមដៃដែលអ្នកប្រើសម្រាប់បើកទូរស័ព្ទរបស់អ្នក។",
        "pub": "ពិនិត្យបញ្ជីសាធារណៈដោយខ្លួនឯង",
        "visits": "ការចូលមើលទំព័រនេះត្រូវបានរាប់ដោយគ្មានខូគី។",
        "who1": "ស្ថាបនិកគឺ Thon Ly", "who2": "Miss Aquarius℠ ជាប្រធានប្រតិបត្តិ",
        "disc": ("HeartBank® គឺជាឃ្លាំងទិន្នន័យនៃការដឹងគុណសម្រាប់ពិភពលោក។ HeartBank មិនមែនជាធនាគារដែលមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ "
                 "ហើយមិនផ្តល់សេវាធនាគារ មិនទទួលប្រាក់បញ្ញើ និងមិនផ្តល់ឥណទានឡើយ។ គ្មានការបង់ប្រាក់នៅទីនេះទេ៖ សេវានេះរក្សាកំណត់ត្រានៃការអរគុណ "
                 "ហើយមិនផ្លាស់ទីប្រាក់ឡើយ។ HeartBank មិនផ្តល់សេវាហិរញ្ញវត្ថុទេ។"),
        "you_h": "កំណត់ត្រារបស់អ្នក",
        "you_sub": "បន្ទាត់នីមួយៗគឺជាធាតុមួយ ដូចដែលវាត្រូវបានរក្សាទុក។ ធាតុនីមួយៗបង្ហាញតែផ្នែករបស់អ្នកប៉ុណ្ណោះ។ រាល់ពេលដែលទំព័រនេះត្រូវបានបើក ការបើកនោះត្រូវបានកត់ទុក ប៉ុន្តែអ្វីដែលវាបង្ហាញមិនត្រូវបានកត់ទុកទេ។",
        "legend": "<b>Kiitos</b> គឺជាការអរគុណរវាងមនុស្សពីរនាក់។ <b>Kiitti</b> គឺជាការថែទាំវត្ថុ រុក្ខជាតិ ឬសត្វ។",
        "dl": "ទាញយកកំណត់ត្រារបស់ខ្ញុំ",
        "dl_note": "ឯកសារនេះមានធាតុទាំងអស់ និងអ្វីដែលអ្នកត្រូវការដើម្បីពិនិត្យដោយខ្លួនឯង ទោះបីសេវានេះលែងមានក៏ដោយ។ សូមរក្សាវាជាឯកជន៖ វាបញ្ជាក់ផ្នែករបស់អ្នក។",
        "season": "រដូវកាលទី ១ · ២៦ វិច្ឆិកា ២០២៦ ដល់ ៧ មករា ២០២៧",
        "rows": [("thank_out", "អ្នកបានអរគុណនរណាម្នាក់", "Kiitos", "333.eco", "២ ធ្នូ ២០២៦ ម៉ោង ៩:៤១ ព្រឹក"),
                 ("thank_in", "មាននរណាម្នាក់បានអរគុណអ្នក", "Kiitos", "333.eco", "៣០ វិច្ឆិកា ២០២៦ ម៉ោង ៦:១២ ល្ងាច"),
                 ("plant", "អ្នកបានត្រឡប់ទៅរករុក្ខជាតិមួយ", "Kiitti", "B-Twin", "២៩ វិច្ឆិកា ២០២៦ ម៉ោង ៨:០៣ ព្រឹក"),
                 ("thing", "អ្នកបានអរគុណវត្ថុមួយ", "Kiitti", "B-Twin", "២៨ វិច្ឆិកា ២០២៦ ម៉ោង ៧:៥៥ យប់"),
                 ("animal", "អ្នកបានត្រឡប់ទៅរកសត្វមួយ", "Kiitti", "B-Twin", "២៧ វិច្ឆិកា ២០២៦ ម៉ោង ១០:២០ ព្រឹក")],
        "kinds": {"care": {"thing": "អ្នកបានត្រឡប់ទៅរកវត្ថុមួយ", "plant": "អ្នកបានត្រឡប់ទៅរករុក្ខជាតិមួយ", "animal": "អ្នកបានត្រឡប់ទៅរកសត្វមួយ"},
                  "thanks": {"thing": "អ្នកបានអរគុណវត្ថុមួយ", "plant": "អ្នកបានអរគុណរុក្ខជាតិមួយ", "animal": "អ្នកបានអរគុណសត្វមួយ"}},
        "seasons": {"1": "រដូវកាលទី ១ · ២៦ វិច្ឆិកា ២០២៦ ដល់ ៧ មករា ២០២៧"},
        "thanked": "អ្នកបានអរគុណនរណាម្នាក់", "was_thanked": "មាននរណាម្នាក់បានអរគុណអ្នក",
        "privacy_link": "ឯកជនភាព", "terms_link": "លក្ខខណ្ឌ", "home_link": "ត្រឡប់ទៅទំព័រដើម",
        "earth_h1": "រាល់ការអរគុណបង្កើតកំពូលរលក និងបាតរលក។",
        "earth_sub": "អ្នកមានចិត្តល្អឡើង ហើយអ្នកដឹងគុណចុះ ក្នុងចំនួនដូចគ្នា ដូច្នេះសមុទ្រមិនដែលខ្ពស់ឡើងទេ។ វាគ្រាន់តែផ្លាស់ទី។",
        "crest": "កំពូលរលក", "crest_means": "ចិត្តល្អ", "trough": "បាតរលក", "trough_means": "ដឹងគុណ", "color_means": "ញឹកញាប់ប៉ុណ្ណាដែលកន្លែងមួយឆ្លងកាត់សូន្យ",
        "earth_opens": "រដូវកាលទី ១ បើកនៅថ្ងៃទី ២៦ វិច្ឆិកា ២០២៦។", "about_link": "នេះជាអ្វី?",
        "card_place": "ផ្នែកនេះនៃពិភពលោក ទំហំប្រហែល ១០០ គីឡូម៉ែត្រ",
        "sample_short": "លេខបង្កើតឡើង ដើម្បីជួយអ្នកស្រមៃ រហូតដល់រដូវកាលទី ១ បើកនៅថ្ងៃទី ២៦ វិច្ឆិកា ២០២៦។",
        "sample_note": "លេខទាំងនេះជាការបង្កើតឡើង ដើម្បីជួយអ្នកស្រមៃថាវានឹងមើលទៅដូចម្តេច។ បញ្ជីពិតចាប់ផ្តើមនៅពេលរដូវកាលទី ១ បើកនៅថ្ងៃទី ២៦ វិច្ឆិកា ២០២៦ ហើយលេខទាំងនេះនឹងបាត់ដោយខ្លួនឯង។",
        "sample_day": "ថ្ងៃទី",
        "scholars_link": "សម្រាប់អ្នកស្រាវជ្រាវ",
        "scholars_title": "សំណួរដែលបញ្ជីអាចឆ្លើយបាន",
        "scholars_sub": "អ្នកស្រាវជ្រាវនឹងអាចសួរថាការដឹងគុណផ្លាស់ទីក្នុងចំណោមមនុស្សដូចម្តេច ហើយទទួលបានការប្រៀបធៀបមកវិញ៖ មិនមែនជួរ គូ បុគ្គល ទីកន្លែង ឬអត្រាឡើយ។",
        "scholars_banner": "អ្វីៗទាំងអស់នៅលើទំព័រនេះជាការបង្កើតឡើង។ មនុស្សត្រូវបានក្លែងធ្វើ ហើយយើងបានសរសេរគំរូទាំងនោះដោយខ្លួនឯង ដូច្នេះលទ្ធផលទាំងនេះមិននិយាយអ្វីអំពីមនុស្សពិតទេ។ ទ្វារមិនទាន់បើកទេ។",
        "sch_pick": "សាកល្បងសំណួរមួយ",
        "sch_group": "ក្រុម", "sch_share": "ចំណែក", "sch_range": "ជាមួយសំឡេងរំខាន",
        "sch_gap": "ភាពខុសគ្នា", "sch_each": "ក្រុមនីមួយៗមានយ៉ាងហោចណាស់ ៥០ នាក់។",
        "sch_refused_h": "បដិសេធ", "sch_refused_p": "ក្រុមមួយក្នុងចំណោមនេះមានតិចជាង ៥០ នាក់ ដូច្នេះគ្មានអ្វីត្រឡប់មកវិញទេ។ កូដបដិសេធវា។",
        "sch_rules_h": "របៀបដែលទ្វារពិតនឹងដំណើរការ",
        "sch_rules": ["អ្នកសរសេរសំណួរ សម្មតិកម្ម និងច្បាប់សម្រេចជាមុន ហើយវាត្រូវបានផ្សាយជាមួយត្រាពេលវេលាមុនពេលដំណើរការ។", "វាត្រូវបានពិនិត្យដោយមនុស្ស។ Miss Aquarius\u2120 មិនដែលជ្រើសរើសសំណួរទេ។", "មានតែរដូវកាលដែលបានបញ្ចប់ប៉ុណ្ណោះត្រូវបានសិក្សា។", "វាដំណើរការក្នុងសេវា រាល់ការអានត្រូវបានកត់ត្រា។ មានតែការប្រៀបធៀបទេដែលចេញទៅ។", "ក្រុមនីមួយៗមានយ៉ាងហោចណាស់ ៥០ នាក់ ចម្លើយនីមួយៗមានសំឡេងរំខាន ហើយរដូវកាលនីមួយៗមានថវិកាថេរ។"],
        "q_forward": "ក្នុងចំណោមអ្នកដែលត្រូវបានអរគុណក្នុងមួយសប្តាហ៍ តើប៉ុន្មាននាក់បានអរគុណនរណាម្នាក់នៅសប្តាហ៍បន្ទាប់ ធៀបនឹងអ្នកដែលមិនត្រូវបានអរគុណ?",
        "q_forward_a": "ត្រូវបានអរគុណ", "q_forward_b": "មិនត្រូវបានអរគុណ", "q_forward_o": "បានអរគុណនរណាម្នាក់នៅសប្តាហ៍បន្ទាប់",
        "q_both": "តើអ្នកដែលទាំងថែទាំ និងអរគុណ ឆ្លងកាត់សូន្យញឹកញាប់ជាងអ្នកដែលថែទាំតែប៉ុណ្ណោះទេ?",
        "q_both_a": "ថែទាំ និងអរគុណ", "q_both_b": "ថែទាំតែប៉ុណ្ណោះ", "q_both_o": "បានឆ្លងកាត់សូន្យយ៉ាងហោចណាស់ម្តង",
        "q_kind": "តើអ្នកដែលថែទាំអ្វីដែលមានជីវិត ត្រឡប់មកវិញច្រើនជាងអ្នកដែលថែទាំវត្ថុទេ?",
        "q_kind_a": "រុក្ខជាតិ ឬសត្វ", "q_kind_b": "វត្ថុ", "q_kind_o": "បានត្រឡប់មកវិញនៅសប្តាហ៍បន្ទាប់",
        "q_circle": "តើអ្នកដែលទទួលមុនពេលឲ្យ បន្តឲ្យយូរជាងអ្នកដែលឲ្យមុនទេ?",
        "q_circle_a": "ទទួលមុន", "q_circle_b": "ឲ្យមុន", "q_circle_o": "នៅតែអរគុណក្នុងសប្តាហ៍ចុងក្រោយ",
        "q_single": "តើបុគ្គលតែម្នាក់ដែលបានអរគុណមុនគេក្នុងរដូវកាលនេះ បានធ្វើអ្វីបន្ទាប់?",
        "q_single_a": "បុគ្គលដំបូង", "q_single_b": "អ្នកផ្សេងទៀត", "q_single_o": "បានអរគុណម្តងទៀត",
        "proof_link": "ភស្តុតាងផលបូកសូន្យ",
        "proof_title": "ភស្តុតាងផលបូកសូន្យ",
        "proof_sub": "រាល់ការអរគុណផ្លាស់ទីចំនួនដូចគ្នា ឡើងសម្រាប់ម្ខាង និងចុះសម្រាប់ម្ខាងទៀត ដូច្នេះសមុទ្រនីមួយៗបូកចូលគ្នាស្មើសូន្យ។ ភស្តុតាងនេះអនុញ្ញាតឲ្យនរណាក៏បានពិនិត្យរឿងនេះពីបញ្ជីសាធារណៈ ដោយមិនឃើញការអរគុណណាមួយឡើយ។",
        "proof_checks_h": "អ្វីដែលវាពិនិត្យ",
        "proof_checks": ["រាល់ការអរគុណដែលបានរាប់ មានការចុចសោសម្ងាត់ ដោយមានវត្តមាន និងបានផ្ទៀងផ្ទាត់អ្នកនោះ លើការអរគុណនោះពិតប្រាកដ។", "នីមួយៗផ្លាស់ទីចំនួនតាមច្បាប់របស់វាពិតប្រាកដ ពីគណនីមួយទៅគណនីមួយទៀត ហើយត្រូវបានរាប់តែម្តង។", "ខ្សែសង្វាក់ចាប់ផ្តើមពីសូន្យ នៅធាតុដំបូងនៃបញ្ជី។"],
        "proof_limits_h": "អ្វីដែលវាមិនអាចបង្ហាញ",
        "proof_limits": ["សោសម្ងាត់បង្ហាញថានរណាម្នាក់កាន់សោ មិនមែនថាពួកគេជាមនុស្សតែម្នាក់ទេ។", "មនុស្សពីរនាក់នៅតែអាចអរគុណគ្នាទៅវិញទៅមកដើម្បីបង្ហាញ។", "ការអរគុណដែលត្រូវបានទុកចោលពីភស្តុតាង មើលទៅដូចជាការបំពេញ។ អ្នកដែលជាម្ចាស់ការអរគុណនោះអាចដឹងនៅពេលរដូវកាលបញ្ចប់។", "វាមិនពិនិត្យហត្ថលេខារបស់បញ្ជីខ្លួនឯងទេ។ explorer.333.eco/ledger ធ្វើវា។"],
        "proof_lag": "ភស្តុតាងត្រូវបានធ្វើរៀងរាល់យប់ ដូច្នេះថ្ងៃថ្មីបំផុតមិនទាន់នៅក្នុងវានៅឡើយទេ។",
        "proof_go": "ពិនិត្យវានៅក្នុងកម្មវិធីរុករករបស់អ្នក",
        "proof_deep": "ពិនិត្យភស្តុតាងទាំងអស់ (យឺតជាង)",
        "proof_busy": "កំពុងពិនិត្យ…",
        "proof_good": "បានពិនិត្យនៅក្នុងកម្មវិធីរុករករបស់អ្នក រាល់ការអរគុណដែលបានរាប់ក្នុងធាតុបញ្ជី",
        "proof_none": "មិនទាន់មានភស្តុតាងបោះពុម្ពនៅឡើយទេ។ ភស្តុតាងដំបូងមកក្រោយរដូវកាលទី ១ បើក។",
        "proof_bad": "វាមិនត្រឹមត្រូវទេ៖",
        "proof_failed": "ការពិនិត្យមិនអាចដំណើរការបាន៖",
        "ledger_title": "បញ្ជី តាមថ្ងៃនីមួយៗ",
        "ledger_sub": "ថ្ងៃដែលបានបិទនីមួយៗ៖ តំបន់ទំហំប្រហែល ១០០ គីឡូម៉ែត្រ ដែលបានរាប់យ៉ាងហោចណាស់ពីរផ្នែក។ គ្មានឈ្មោះ គ្មានបុគ្គល និងគ្មានការអរគុណមួយៗនៅទីនេះទេ។",
        "ledger_area": "តំបន់", "ledger_map": "នៅលើផែនទី", "ledger_open": "នៅសមុទ្របើកចំហ", "ledger_total": "បូកចូលគ្នា",
        "ledger_zero": "សូន្យគឺជារបៀបដែលបញ្ជីត្រូវបានបង្កើត៖ រាល់ការអរគុណយកមួយពីអ្នកដឹងគុណ ហើយឲ្យមួយដល់អ្នកមានចិត្តល្អ។ តារាងនេះបង្ហាញថាសមតុល្យស្ថិតនៅឯណា។ វាមិនបញ្ជាក់អំពីសូន្យដោយខ្លួនឯងទេ។ សម្រាប់ Kiitti សមុទ្របើកចំហក៏កាន់ផ្នែករបស់វត្ថុ រុក្ខជាតិ និងសត្វផងដែរ។",
        "ledger_json": "ទិន្នន័យដូចគ្នាជាឯកសារ", "ledger_title_tag": "បញ្ជី តាមថ្ងៃនីមួយៗ · HeartBank®",
        "draft_note": "នេះជាសេចក្តីព្រាង ហើយមានជាភាសាអង់គ្លេសតែប៉ុណ្ណោះនៅពេលនេះ។ មិនទាន់មានមេធាវីពិនិត្យទេ ហើយវាអាចផ្លាស់ប្តូរមុនពេលចុងក្រោយ។",
        "copied": "បានចម្លង", "working": "កំពុងដំណើរការ", "auto": "ស្វ័យប្រវត្តិ", "light": "ភ្លឺ", "dark": "ងងឹត",
        "title_home": "រាល់ការអរគុណបង្កើតកំពូលរលក និងបាតរលក · HeartBank®", "title_you": "កំណត់ត្រារបស់អ្នក · HeartBank®",
        "desc": "រាល់ការអរគុណនៅលើ HeartBank® បង្កើតកំពូលរលក និងបាតរលកនៅលើផែនដីដែលកំពុងវិល។ អ្នកមានចិត្តល្អឡើង អ្នកដឹងគុណចុះក្នុងចំនួនដូចគ្នា ហើយសមុទ្រមិនដែលខ្ពស់ឡើងទេ។",
        "desc_ledger": "សមុទ្រសាធារណៈ តាមថ្ងៃ និងតាមតំបន់៖ អ្វីនៅលើផែនទី អ្វីនៅក្នុងសមុទ្របើកចំហ និងផលបូករបស់វា។",
        "desc_scholars": "ប្រភេទសំណួរដែលអ្នកស្រាវជ្រាវអាចសួរបញ្ជីនៃការដឹងគុណ និងការប្រៀបធៀបដែលត្រឡប់មកវិញ។ បង្ហាញនៅទីនេះលើមនុស្សក្លែងធ្វើ។",
        "receipt": "បង្កាន់ដៃ", "r_place": "ទីតាំងក្នុងកំណត់ហេតុ", "r_finger": "ស្នាមម្រាមដៃឌីជីថល", "r_log": "កំណត់ហេតុ", "r_sig": "ហត្ថលេខា",
        "copy": "ចម្លងបង្កាន់ដៃ", "check": "ពិនិត្យវានៅលើបញ្ជីសាធារណៈ",
        "jubilee": "នៅថ្ងៃទី ៧ មករា សមតុល្យទាំងអស់ចាប់ផ្តើមពីសូន្យឡើងវិញ។ ធាតុទាំងនេះនៅដដែល។",
        "leave": "ពេលអ្នកចាកចេញពីទំព័រនេះ អ្នកនឹងត្រូវការ passkey របស់អ្នកដើម្បីបើកវាម្តងទៀត។",
        "none_p": "នេះជាកន្លែងដែលធាតុរបស់អ្នកនឹងបង្ហាញ។ ពេលអ្នកអរគុណនរណាម្នាក់នៅលើកម្មវិធី HeartBank® ឬមាននរណាម្នាក់អរគុណអ្នក វានឹងបង្ហាញនៅទីនេះ។",
        "pk_h": "ទំព័រនេះបើកដោយ passkey",
        "pk_p": "Passkey គឺមុខ ឬស្នាមម្រាមដៃដែលអ្នកប្រើសម្រាប់បើកទូរស័ព្ទរបស់អ្នក។ វាបញ្ជាក់ថាអ្នកដែលបើកកំណត់ត្រានេះគឺជាអ្នក។ សូមបន្ថែមមួយទៅក្នុងគណនី HeartBank® របស់អ្នក រួចត្រឡប់មកវិញ។",
        "pk_btn": "បន្ថែម passkey",
        "err_h": "ទំព័រនេះមិនអាចបើកបានទេឥឡូវនេះ",
        "err_p": "គ្មានអ្វីនៅក្នុងកំណត់ត្រារបស់អ្នកបានផ្លាស់ប្តូរទេ។ សូមព្យាយាមម្តងទៀតបន្តិចក្រោយ។",
        "err_btn": "ព្យាយាមម្តងទៀត",
        "st_none": "ស្ថានភាព · មិនទាន់មានធាតុ", "st_pk": "ស្ថានភាព · ត្រូវការ passkey", "st_err": "ស្ថានភាព · មិនអាចបើកបាន",
        "tag": "[ គំនូរព្រាង។ គ្មានអ្វីនៅទីនេះដំណើរការពិតទេ ហើយធាតុទាំងនេះជាការបង្កើតឡើង។ ]",
    },
}


def brand_css(css):
    for k in ("bg", "surface", "surface-2", "line", "line-strong", "ink", "ink-dim"):
        for p in ("l", "d"):
            css = css.replace("@%s_%s@" % (p.upper(), k.upper().replace("-", "_")), tok("%s-%s" % (p, k)))
    css = css.replace("@SAPPHIRE@", tok("color-sapphire"))
    for k in ("duration", "delay"):
        css = css.replace("@BEAT_%s@" % k.upper(), tok("beat-" + k))
    assert not re.search(r"@[A-Z_0-9]+@", css), "unfilled brand placeholder"
    return css


# ⭐ The wordmark's ®: Newsreader carries its own, already drawn high (ink 253-688 of 1000, capitals 676). At .72em its top is .496em up, so it needs +.18em of the
# wordmark, +.25em of its own size, to sit level with the capitals (measured 2026-11-08; the -.27em in older boards was for a fallback glyph that rode higher).
# ⭐ The one block that is this surface's own: heartbank.net's hue is blue (data/tlds.json), so its accent is the sapphire gem,
# with a lighter measured value on dark. Every other value is read from the brand layer.
CSS = """
:root,[data-theme="light"]{
  --bg:@L_BG@; --surface:@L_SURFACE@; --surface-2:@L_SURFACE_2@; --line:@L_LINE@; --line-strong:@L_LINE_STRONG@;
  --ink:@L_INK@; --ink-dim:@L_INK_DIM@; --beat-duration:@BEAT_DURATION@; --beat-delay:@BEAT_DELAY@;
  --accent:@SAPPHIRE@; --accent-ink:#ffffff; --wash:rgba(15,82,186,.08); --edge:rgba(15,82,186,.26);
  --font-display:"Newsreader",Georgia,serif; --font-text:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace; --font-khmer:"Noto Sans Khmer",sans-serif;
  --r-card:1.25rem; --r-control:1rem; --r-pill:999px;
}
[data-theme="dark"]{
  --bg:@D_BG@; --surface:@D_SURFACE@; --surface-2:@D_SURFACE_2@; --line:@D_LINE@; --line-strong:@D_LINE_STRONG@;
  --ink:@D_INK@; --ink-dim:@D_INK_DIM@;
  --accent:#8ab4f8; --accent-ink:#10141c; --wash:rgba(138,180,248,.10); --edge:rgba(138,180,248,.30);
}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--font-text);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.km{font-family:var(--font-khmer),var(--font-text);line-height:1.75}
.board{width:var(--w);margin:0 auto;padding:0 var(--pad);background:var(--bg)}
.desk{--w:1440px;--pad:96px} .phone{--w:390px;--pad:20px}
header{display:flex;align-items:center;justify-content:space-between;padding:22px 0;gap:12px}
.wordmark{font-family:var(--font-display);font-weight:600;font-size:1.5rem;white-space:nowrap;letter-spacing:-.01em;
  --emblem-cap:.66em;--emblem-size:calc(var(--emblem-cap)*1.1);--emblem-box:calc(var(--emblem-size)/.7534)}
.wordmark svg{width:var(--emblem-box);height:var(--emblem-box);color:var(--accent);vertical-align:baseline;
  margin-top:calc(var(--emblem-box)*-.09312);margin-bottom:calc(var(--emblem-box)*-.15333);
  margin-left:calc(var(--emblem-box)*-.15343 + 1px);margin-right:calc(var(--emblem-box)*-.09312 - 1px)}
.wordmark sup{font-size:.72em;font-weight:500;vertical-align:.25em;margin-left:.05em;line-height:0}
.tools{display:flex;gap:8px;align-items:center}
.seg{display:inline-flex;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:3px;font-size:.8rem}
.seg span{padding:5px 12px;border-radius:var(--r-pill);color:var(--ink-dim)}
.seg span.on{background:var(--ink);color:var(--bg)}
.share{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:6px 13px;font-size:.85rem}
.share svg{width:16px;height:16px;flex:none}
.phone .share{padding:7px 9px}.phone .share .lbl{display:none}
h1{font-family:var(--font-display);font-weight:600;letter-spacing:-.022em;line-height:1.08;margin:0}
.desk h1{font-size:3.6rem;max-width:17ch} .phone h1{font-size:2.4rem}
.km h1,h1.km{letter-spacing:0;line-height:1.4} .desk h1.km{font-size:2.8rem;max-width:22ch} .phone h1.km{font-size:1.8rem}
.para{font-size:1.15rem;margin:24px 0 0;max-width:60ch}
.phone .para{font-size:1.05rem}
.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);border-radius:var(--r-control);padding:14px 26px;font-weight:600;font-size:1.05rem}
.btn2{display:inline-block;border:1px solid var(--line-strong);border-radius:var(--r-control);padding:12px 20px;font-weight:600;font-size:.95rem}
.note{color:var(--ink-dim);font-size:.9rem;margin:12px 0 0;max-width:60ch}
.flush{margin:0}
.tagline{font-family:var(--font-mono);color:var(--ink-dim);font-size:.75rem;margin:0 0 14px}
.cta{margin:30px 0 0}
a.link,.link{color:var(--accent);text-decoration:underline;text-underline-offset:3px}
.intro{padding:28px 0 56px}
.desk .intro{display:grid;grid-template-columns:1.15fr .85fr;gap:64px;align-items:center}
.art{border:1px solid var(--edge);background:var(--wash);border-radius:var(--r-card);padding:20px;margin-top:32px}
.desk .art{margin-top:0}
.art svg{width:100%;height:auto;display:block}
.you{padding:12px 0 8px}
.you .sub{color:var(--ink-dim);margin:14px 0 0;max-width:62ch}
.legend{background:var(--wash);border-radius:var(--r-control);padding:12px 16px;margin:20px 0 0;font-size:.95rem;max-width:62ch}
.dl{display:flex;flex-direction:column;align-items:flex-start;gap:8px;margin:22px 0 0}
.season{font-family:var(--font-mono);font-size:.78rem;color:var(--ink-dim);margin:34px 0 10px}
.season.km{font-family:var(--font-khmer);font-size:.9rem}
.rows{border:1px solid var(--line);border-radius:var(--r-card);background:var(--surface);overflow:hidden}
.row{padding:16px 18px;border-top:1px solid var(--line)}
.row:first-child{border-top:0}
.line{display:flex;gap:14px;align-items:flex-start}
.ico{flex:none;width:34px;height:34px;border-radius:50%;background:var(--wash);display:flex;align-items:center;justify-content:center;color:var(--accent)}
.ico svg{width:20px;height:20px}
.what{font-weight:500}
.meta{color:var(--ink-dim);font-size:.88rem}
.sum{display:inline-block;margin:8px 0 0 48px;color:var(--accent);font-size:.9rem}
.receipt{margin:10px 0 0 48px;background:var(--surface-2);border-radius:var(--r-control);padding:14px}
.phone .receipt{margin-left:0}
.f{display:grid;grid-template-columns:1fr;gap:1px;margin:0 0 10px}
.desk .f{grid-template-columns:170px 1fr;gap:12px}
.f dt{color:var(--ink-dim);font-size:.82rem}
.f dd{margin:0;font-family:var(--font-mono);font-size:.82rem;word-break:break-all}
.acts{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:12px}
.small{color:var(--ink-dim);font-size:.9rem;margin:18px 0 0;max-width:62ch}
.state{padding:44px 0;border-top:1px solid var(--line)}
.state:first-of-type{border-top:0}
.state h2{font-family:var(--font-display);font-weight:600;font-size:1.7rem;line-height:1.2;margin:0 0 10px}
.state h2.km{font-size:1.45rem;line-height:1.45}
.state p{margin:0 0 18px;max-width:60ch}
.spot{width:100%;height:88px;display:block;margin:0 0 16px;background:var(--wash);border-radius:var(--r-control)}
footer{border-top:1px solid var(--line);margin-top:56px;padding:30px 0 48px;color:var(--ink-dim);font-size:.88rem}
footer p{margin:0 0 14px}
.foot-row{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 18px}
.foot-row p{margin:0}
.nw{white-space:nowrap}
.sm{font-size:.5em;vertical-align:.7em;margin-left:.04em;line-height:0}
"""


def mark():
    return 'Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup>' % EMBLEM


def heart(cx, cy, k=1.0, fill="var(--accent)"):
    """Every heart is the B-Emblem, centered by its bbox, at .8 of a stock heart's width (founder 2026-10-24)."""
    return '<g transform="translate(%s %s) scale(%s) translate(-12.7237 -11.2776)"><path d="%s" fill="%s"/></g>' % (cx, cy, .8 * k, EMBLEM, fill)


def sm(s):
    return s.replace("℠", '<span class="sm">℠</span>')


def note_svg():
    """A private note with a lock, and a row of public fingerprints with one lit: the note stays, only its fingerprint goes out."""
    tiles = []
    for r in range(3):
        for c in range(6):
            lit = (r, c) == (1, 2)
            tiles.append('<rect x="%d" y="%d" width="28" height="28" rx="5" fill="%s" stroke="%s" stroke-width="1.5"/>'
                         % (300 + c * 34, 58 + r * 34, "var(--accent)" if lit else "var(--surface)", "var(--accent)" if lit else "var(--line-strong)"))
    return ('<svg viewBox="0 0 520 220" role="img" aria-hidden="true">'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="var(--accent)"/></marker></defs>'
            '<rect x="22" y="36" width="170" height="148" rx="14" fill="var(--surface)" stroke="var(--line-strong)" stroke-width="1.5"/>'
            '<line x1="46" y1="70" x2="168" y2="70" stroke="var(--line-strong)" stroke-width="5" stroke-linecap="round"/>'
            '<line x1="46" y1="92" x2="150" y2="92" stroke="var(--line-strong)" stroke-width="5" stroke-linecap="round"/>'
            + heart(70, 134, 1.3) +
            '<g transform="translate(142 120)"><rect x="0" y="16" width="36" height="30" rx="6" fill="var(--accent)"/><path d="M8 16v-7a10 10 0 0 1 20 0v7" fill="none" stroke="var(--accent)" stroke-width="4"/></g>'
            '<path d="M204 110 C232 110 256 110 288 110" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" marker-end="url(#ar)"/>'
            + "".join(tiles) + '</svg>')


ICONS = {
    "thank_out": lambda: '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % heart(12, 12, 1.0, "currentColor"),
    "thank_in": lambda: '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % heart(12, 12, 1.0, "currentColor"),
    "plant": lambda: '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21v-9"/><path d="M12 12C12 7 8 5 4 5c0 5 3 7 8 7z"/><path d="M12 14c0-4 3-6 8-6 0 5-3 6-8 6z"/></svg>',
    "thing": lambda: '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/></svg>',
    "animal": lambda: '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><ellipse cx="12" cy="16" rx="5.5" ry="4.5"/><circle cx="6" cy="10" r="2.2"/><circle cx="18" cy="10" r="2.2"/><circle cx="9.5" cy="6.5" r="2.2"/><circle cx="14.5" cy="6.5" r="2.2"/></svg>',
}


def spot(kind):
    if kind == "none":
        inner = '<rect x="150" y="18" width="90" height="56" rx="10" fill="var(--surface)" stroke="var(--line-strong)" stroke-width="1.5"/>' + heart(195, 46, 1.2)
    elif kind == "key":
        inner = ('<circle cx="176" cy="46" r="17" fill="none" stroke="var(--accent)" stroke-width="5"/>'
                 '<path d="M193 46h44M226 46v12M214 46v9" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>')
    else:
        inner = '<path d="M155 62a40 40 0 0 1 80 0" fill="none" stroke="var(--line-strong)" stroke-width="5" stroke-linecap="round"/><circle cx="195" cy="62" r="6" fill="var(--accent)"/>'
    return '<svg class="spot" viewBox="0 0 390 88" aria-hidden="true">%s</svg>' % inner


def who(t):
    a = lambda n: '<span class="link">%s</span>' % n
    return (t["who1"].replace("Thon Ly", a("Thon Ly")), sm(t["who2"].replace("Miss Aquarius", a("Miss Aquarius"))))


def disc(t):
    d = t["disc"]
    for sep in (". ", "។ "):
        i = d.find(sep)
        if i > 0:
            return '<span class="nw">%s</span> %s' % (d[:i + len(sep.strip())], d[i + len(sep):])
    return d


def page(lang, theme, size, kind):
    t = T[lang]
    kmc = " km" if lang == "km" else ""
    k = kmc.strip()
    cls = "desk" if size == "desk" else "phone"
    seg_l = '<div class="seg"><span%s>EN</span><span%s class="km">ខ្មែរ</span></div>' % (' class="on"' if lang == "en" else "", ' class="on"' if lang == "km" else "")
    tl = ("Auto", "Light", "Dark") if lang == "en" else ("ស្វ័យប្រវត្តិ", "ភ្លឺ", "ងងឹត")
    seg_t = '<div class="seg%s"><span>%s</span><span%s>%s</span><span%s>%s</span></div>' % (kmc, tl[0], ' class="on"' if theme == "light" else "", tl[1], ' class="on"' if theme == "dark" else "", tl[2])
    share = ('<span class="share"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M12 3l-4 4M12 3l4 4M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
             '<span class="lbl%s">%s</span></span>' % (kmc, t["share"])) if kind == "landing" else ""
    head = '<header><div class="wordmark">%s</div><div class="tools">%s%s</div></header>' % (mark(), seg_l, share)
    ph = '<p class="tagline km">[ %s ]</p>' % t["ph"] if t["ph"] else ""
    tag = '<p class="tagline%s">%s</p>' % (kmc, t["tag"])
    w1, w2 = who(t)
    foot_extra = '<p>%s</p>' % t["visits"] if kind == "landing" else ""
    links = '<p><span class="link">%s</span> · <span class="link">%s</span></p>' % (t["privacy_link"], t["terms_link"])
    foot = ('<footer class="%s"><p>%s</p>%s%s<div class="foot-row"><p>%s · %s</p>%s</div></footer>' % (k, disc(t), foot_extra, links, w1, w2, seg_t))

    if kind == "landing":
        body = ('%s%s%s<section class="intro"><div><h1 class="%s">%s</h1><p class="para%s">%s</p>'
                '<p class="cta"><span class="btn%s">%s</span></p><p class="note%s">%s</p>'
                '<p class="note%s"><span class="link">%s</span> · <span class="mono">%s</span></p></div>'
                '<div class="art">%s</div></section>'
                % (head, ph, tag, k, t["h1"], kmc, t["para"], kmc, t["cta"], kmc, t["cta_note"], kmc, t["pub"], LEDGER_LINK, note_svg()))
    elif kind == "record":
        rows = []
        for n, (ic, what, led, app, when) in enumerate(t["rows"]):
            line = ('<div class="line"><span class="ico">%s</span><div><div class="what%s">%s</div><div class="meta">%s · %s · <span class="%s">%s</span></div></div></div>'
                    % (ICONS[ic](), kmc, what, led, app, k, when))
            if n == 0:
                detail = ('<div class="receipt"><dl class="f">'
                          '<dt class="%s">%s</dt><dd>1,024</dd><dt class="%s">%s</dt><dd>Aq3fXv…9Lw2</dd>'
                          '<dt class="%s">%s</dt><dd>log.333.eco/ledger</dd><dt class="%s">%s</dt><dd>MEUCIQ…7hJw==</dd></dl>'
                          '<div class="acts"><span class="btn2%s">%s</span><span class="link%s">%s</span></div></div>'
                          % (k, t["r_place"], k, t["r_finger"], k, t["r_log"], k, t["r_sig"], kmc, t["copy"], kmc, t["check"]))
            else:
                detail = '<span class="sum%s">%s</span>' % (kmc, t["receipt"])
            rows.append('<div class="row">%s%s</div>' % (line, detail))
        body = ('%s%s%s<section class="you"><h1 class="%s">%s</h1><p class="sub%s">%s</p><p class="legend%s">%s</p>'
                '<div class="dl"><span class="btn%s">%s</span><p class="note flush%s">%s</p></div></section>'
                '<p class="season%s">%s</p><div class="rows">%s</div><p class="small%s">%s</p><p class="small%s">%s</p>'
                % (head, ph, tag, k, t["you_h"], kmc, t["you_sub"], kmc, t["legend"], kmc, t["dl"], kmc, t["dl_note"],
                   kmc, t["season"], "".join(rows), kmc, t["jubilee"], kmc, t["leave"]))
    else:  # the other states of /you
        body = ('%s%s%s'
                '<section class="state"><p class="tagline%s">%s</p>%s<h2 class="%s">%s</h2><p class="%s">%s</p></section>'
                '<section class="state"><p class="tagline%s">%s</p>%s<h2 class="%s">%s</h2><p class="%s">%s</p><span class="btn%s">%s</span></section>'
                '<section class="state"><p class="tagline%s">%s</p>%s<h2 class="%s">%s</h2><p class="%s">%s</p><span class="btn2%s">%s</span></section>'
                % (head, ph, tag,
                   kmc, t["st_none"], spot("none"), k, t["you_h"], k, t["none_p"],
                   kmc, t["st_pk"], spot("key"), k, t["pk_h"], k, t["pk_p"], kmc, t["pk_btn"],
                   kmc, t["st_err"], spot("err"), k, t["err_h"], k, t["err_p"], kmc, t["err_btn"]))

    width = 1440 if size == "desk" else 390
    return ('<!doctype html>\n<html lang="%s" data-theme="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=%d">\n'
            '<meta name="googlebot" content="noindex,nofollow"><meta name="bingbot" content="noindex,nofollow">\n'
            '<link rel="icon" type="image/svg+xml" href="favicon.svg">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Khmer:wght@400;500;600&display=swap">\n'
            '<link rel="stylesheet" href="board.css?v=%s">\n<title>%s (%s, %s, %s)</title>\n</head>\n<body>\n<div class="board %s">%s%s</div>\n</body>\n</html>\n'
            % (t["lang"], theme, width, CSSV, APP_HOST, lang, theme, size, cls, body, foot))


BOARDS = [
    # file, lang, theme, size, kind, title, page
    ("LandingEnPhone.html", "en", "light", "phone", "landing", "1 · The front page, English, phone", "front"),
    ("LandingKmPhone.html", "km", "light", "phone", "landing", "2 · The front page, Khmer, phone", "front"),
    ("LandingEnDesktop.html", "en", "light", "desk", "landing", "3 · The front page, English, desktop", "front"),
    ("LandingDarkPhone.html", "en", "dark", "phone", "landing", "4 · Dark pass, front page, phone", "front"),
    ("RecordEnPhone.html", "en", "light", "phone", "record", "5 · Your record, English, phone", "you"),
    ("RecordKmPhone.html", "km", "light", "phone", "record", "6 · Your record, Khmer, phone", "you"),
    ("RecordEnDesktop.html", "en", "light", "desk", "record", "7 · Your record, English, desktop", "you"),
    ("RecordDarkPhone.html", "en", "dark", "phone", "record", "8 · Dark pass, your record, phone", "you"),
    ("StatesEn.html", "en", "light", "phone", "states", "9 · Nothing yet, needs a passkey, can't open, English", "you"),
    ("StatesKm.html", "km", "light", "phone", "states", "10 · Nothing yet, needs a passkey, can't open, Khmer", "you"),
]
HEIGHTS = {}
if os.path.exists(os.path.join(HERE, "heights.json")):
    HEIGHTS = json.load(open(os.path.join(HERE, "heights.json")))
CSSV = hashlib.sha256((CSS.strip() + "\n").encode("utf-8")).hexdigest()[:8]


def contrast(a, b):
    def lum(h):
        h = h.lstrip("#")
        v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        v = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in v]
        return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]
    la, lb = lum(a), lum(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def main():
    # The accent is the one thing typed here, so its contrast is checked here (button text, and links on the page).
    pairs = [("light button", tok("color-sapphire"), "#ffffff"), ("light link", tok("color-sapphire"), tok("l-surface")),
             ("dark button", "#8ab4f8", "#10141c"), ("dark link", "#8ab4f8", tok("d-surface"))]
    for name, fg, bg in pairs:
        c = contrast(fg, bg)
        assert c >= 4.5, "%s contrast %.2f" % (name, c)
    io.open(os.path.join(HERE, "board.css"), "w", encoding="utf-8").write(brand_css(CSS).strip() + "\n")
    # The site reads its words from here (ledger.heartbank.net public/copy.json), so the page cannot drift from the drawing.
    drop = ("tag", "st_none", "st_pk", "st_err", "rows", "ph", "share_note")
    io.open(os.path.join(HERE, "copy.json"), "w", encoding="utf-8").write(json.dumps({l: {k: v for k, v in T[l].items() if k not in drop} for l in T}, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    artboards, xs = [], {"front": 0, "you": 0}
    for f, lang, theme, size, kind, title, pg in BOARDS:
        html = page(lang, theme, size, kind)
        # the four build checks that apply to a page with no script
        assert html.count("<div") == html.count("</div>"), "%s: div balance" % f
        assert not re.search(r'="[^"]*<', html), "%s: a tag inside a quoted attribute" % f
        for tag in re.findall(r"<[^>]+>", html):
            assert tag.count('"') % 2 == 0, "%s: odd quotes in %s" % (f, tag[:60])
        io.open(os.path.join(HERE, f), "w", encoding="utf-8").write(html)
        w = 1440 if size == "desk" else 390
        artboards.append({"file": f, "x": xs[pg], "y": 0, "w": w, "h": HEIGHTS.get(f, 900 if size == "desk" else 1400), "title": title, "page": pg})
        xs[pg] += w + 120
    canvas = {"artboards": artboards, "annotations": [], "launch": {"view": "canvas", "page": "front"},
              "pages": [{"id": "front", "name": "The front page"}, {"id": "you", "name": "Your record"}]}
    io.open(os.path.join(HERE, "canvas.json"), "w", encoding="utf-8").write(json.dumps(canvas, indent=1, ensure_ascii=False) + "\n")
    print("wrote %d artboards" % len(artboards))


if __name__ == "__main__":
    main()
