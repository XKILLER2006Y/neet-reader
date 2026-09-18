# NEET Split Reader

Free, offline-capable NEET prep: official NCERT page on the left, verified PYQs on the right.

- 1386 verified PYQs across 79 chapters (Bio 544 / Chem 344 / Phys 498), every answer 0-3 keyed.
- Left pane = official NCERT PDF loaded live from `https://ncert.nic.in/textbook/pdf/<code>.pdf` — no books stored in this repo.
- Right pane = your own questions from `questions/<pdf-code>.json`.
- Attempt history, +4/-1 scoring, weak-first dashboard, mistake book, timed drills, bookmarks, 180-Q full mock, service-worker offline mode, JSON backup/restore.

## Run

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Validate

```bash
python3 validate.py   # 0 errors, 0 warnings
```

## Deploy (free, 2 min)

```bash
git init && git add -A && git commit -m init
gh repo create neet-reader --public --source=. --push
gh api repos/{owner}/neet-reader/pages -f source[branch]=main -f source[path]=/
```

Then open `https://{owner}.github.io/neet-reader/`. All paths are relative, so project-subpath hosting works. No backend, no secrets.

## Add questions per PDF page

```json
[{"pdfPage":18,"question":"...","options":["A","B","C","D"],"answer":1,"explanation":"...","source":"NEET 2022"}]
```

## Rules

Do NOT copy PrepPage text/bank, and never commit a downloaded NCERT PDF — the iframe streams the official page, that is the entire content license.

Backup: header ⤓ downloads all progress (attempts/stars/bests/theme) as JSON — do it weekly, browsers can wipe localStorage. ⤒ restores on any device.
