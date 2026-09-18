#!/usr/bin/env python3
"""Validator for neet-reader/questions/*.json — blocks AI slop, enforces accuracy."""
import json, glob, re, sys, os
from collections import Counter

files = sorted(f for f in glob.glob('questions/*.json') if os.path.basename(f) != 'manifest.json')
errors, warnings = [], []
total = 0
ans = Counter()
seen = {}
for f in files:
    try:
        d = json.load(open(f))
    except Exception as e:
        errors.append(f'{f}: invalid JSON ({e})'); continue
    if not isinstance(d, list):
        errors.append(f'{f}: top level must be a list'); continue
    for i, q in enumerate(d):
        total += 1
        loc = f'{f}#{i}'
        for k in ('question', 'options', 'answer'):
            if k not in q: errors.append(f'{loc}: missing {k}')
        opts = q.get('options', [])
        if len(opts) != 4: errors.append(f'{loc}: must have exactly 4 options')
        if q.get('answer') not in (0, 1, 2, 3): errors.append(f'{loc}: answer must be 0-3')
        ans[q.get('answer')] += 1
        if not q.get('source'): warnings.append(f'{loc}: missing source (exam+year+publisher)')
        if not q.get('year'): warnings.append(f'{loc}: missing year')
        if not q.get('explanation'): warnings.append(f'{loc}: missing explanation')
        if len(q.get('question', '')) < 20 and sum(len(o) for o in q.get('options', [])) < 60:
            warnings.append(f'{loc}: stem+options too thin — needs context from official paper')
        key = (q.get('question', '').strip().lower(), tuple(sorted(o.strip().lower() for o in opts)))
        if key in seen:
            if seen[key][0] == f:
                warnings.append(f'{loc}: duplicate of {seen[key][0]}#{seen[key][1]} in same chapter')
            # else: same Q cross-listed in two chapters (e.g. methanogens in
            # classification + microbes) — allowed, chapter views are independent
        else: seen[key] = (f, i)

print(f'Files: {len(files)}  Questions: {total}')
print(f'Answer balance A/B/C/D: {ans[0]}/{ans[1]}/{ans[2]}/{ans[3]}')
a = [ans[i] for i in range(4)]
if max(a) - min(a) > total * 0.15:
    warnings.append('Answer distribution skewed >15% — check for default-A generation')
flagged = sum(1 for f in files for q in json.load(open(f)) if q.get('outOfNcert'))
print(f'Flagged out-of-current-NCERT: {flagged}')
print(f'ERRORS: {len(errors)}')
for e in errors[:30]: print('  E:', e)
print(f'WARNINGS: {len(warnings)}')
for w in warnings[:40]: print('  W:', w)
sys.exit(1 if errors else 0)
