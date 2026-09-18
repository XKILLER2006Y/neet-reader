# Legit question sources — add quantity WITHOUT scraping third-party banks

Rule: every question needs `source + year + explanation`. No guessed keys.
Never bulk-copy BYJU'S / coaching PDFs / PrepPage content — those are copyrighted.

## Tier 1 — official, use these to grow past 913
1. **NTA NEET UG papers** — `neet.nta.nic.in` (after each exam: paper PDF + final answer key).
   2020–2025 = 6 years × 180 Qs ≈ 1,000+ real Qs. Manually enter Physics/Chem/Bio
   sections chapter-wise with year+code (e.g. "NEET 2024 R1").
2. **NTA JEE Main papers** — `jeemain.nta.nic.in` → Public Notices / Archive.
   Use Physics + Chemistry sections only (skip Maths for NEET). 2019–2025,
   session+shift-wise. Official final answer keys are PDFs on the same site.
3. **NCERT Exemplar** — official NCERT books (ncert.nic.in → Exemplar Problems),
   Class 11/12 Physics/Chem/Biology. Higher-order MCQs with official answers.
   Best legit filler for thin chapters (your Physics chapters have only 2–5 Qs).

## How to add (2 min per Q)
```json
{"pdfPage": 9, "question": "...verbatim from official paper...",
 "options": ["...", "...", "...", "..."], "answer": 1,
 "explanation": "your own words + formula",
 "source": "NEET 2024 R1 via NTA", "year": "NEET 2024"}
```
Then: `python3 validate.py` — must show 0 ERRORS before commit.

## Priority gaps (from audit)
Physics XII (2/chapter), Physics XI-part2 (2–3/chapter) — fill from JEE Main
Physics sections + NEET Physics. Short stems (41 flagged "Pick INCORRECT…")
need full context re-added from the official paper.
