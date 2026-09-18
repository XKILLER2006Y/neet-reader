# Physics top-up plan — 238 banked (ground truth) → ~250 verified Qs (NEET weightage-ordered)

> Counts below regenerated from direct file reads. Never hand-edit counts — recount with:
> `python3 -c "import json,glob;print(sum(len(json.load(open(f))) for f in glob.glob('questions/kep*.json'))+sum(len(json.load(open(f))) for f in glob.glob('questions/lep*.json')))"`

Source for weightage: 12-year NEET analysis (2014–2025) + NEET 2024/2026 chapter splits.
Rule stays: hand-enter from official papers, key checked vs NTA final answer key,
`python3 validate.py` must stay 0 ERRORS. No bulk copying coaching banks.

Official pools:
- NTA NEET papers+keys: `neet.nta.nic.in` (2020–2025 ≈ 6×45 = 270 physics Qs)
- NTA JEE Main papers+keys: `jeemain.nta.nic.in` → Archive (Physics Sec-A only, 2019–2025)
- NCERT Exemplar: `ncert.nic.in` → Exemplar Problems, Physics 11/12 (official answers)

## P0 — COMPLETE ✅ (all 7 chapters at/above target)
| File | Chapter | Have | Target | Need | Pull from |
|---|---|---|---|---|---|
| leph103 | Current Electricity | 20 | 15 | 0 ✅ | NEET 2020–25 Physics (≈3/yr) + JEE Main Physics Sec-A + Exemplar Ch |
| leph206 | Semiconductors | 17 | 15 | 0 ✅ | NEET 2024×4, 2026×5 — richest recent seams + Exemplar |
| keph102 | Motion in a Straight Line | 12 | 12 | 0 ✅ | NEET Kinematics pool (≈31/12yr incl. plane) + JEE Main |
| keph103 | Motion in a Plane | 12 | 12 | 0 ✅ | same Kinematics pool, split projectile/relative out |
| leph201 | Ray Optics | 15 | 15 | 0 ✅ | NEET 2026×5 Geometrical + 2020–25 + Exemplar Ray Optics |
| leph101 | Electric Charges and Fields | 12 | 12 | 0 ✅ | NEET Electrostatics ≈4/yr + JEE Main + Exemplar |
| leph102 | Electrostatic Potential and Capacitance | 10 | 12 | 2 | Capacitor ≈3/yr 2026 + 24/12yr + Exemplar |

## P1 — medium yield (3–4%, ~20 Qs/12yr, have 2–5)
| File | Chapter | Have | Target | Need | Pull from |
|---|---|---|---|---|---|
| keph101 | Units and Measurements | 5 | 10 | 5 | 21/12yr, steady 2–3/yr — NEET papers first |
| keph104 | Laws of Motion | 5 | 10 | 5 | 22/12yr + JEE Main friction/banking |
| keph105 | Work, Energy and Power | 5 | 10 | 5 | 23/12yr |
| keph106 | Rotational Motion | 5 | 10 | 5 | 2026×4, Rotational 6% band + JEE Main |
| keph107 | Gravitation | 5 | 8 | 3 | 2026×3 |
| keph204 | Thermodynamics (XI) | 2 | 8 | 6 | Heat & Thermo 2026×7 — hot seam |
| keph206 | Oscillations | 2 | 8 | 6 | 2026×5 (↑25%) |
| leph104 | Moving Charges and Magnetism | 2 | 10 | 8 | 2026×4 + Exemplar |
| leph106 | Electromagnetic Induction | 2 | 8 | 6 | 2026×4 (↑100%) |
| leph107 | Alternating Current | 2 | 8 | 6 | 2026×3 (↑50%) |
| leph203 | Dual Nature of Radiation and Matter | 2 | 8 | 6 | 2026×5 |
| leph204+leph205 | Atoms + Nuclei | 2+2 | 8+8 | 6+6 | 2026×6 Atoms+Nuclei (↑200%) — top momentum |
| leph202 | Wave Optics | 2 | 8 | 6 | 2024×2 + Exemplar |

## P2 — fill to 8 (lower but steady, have 2–3)
keph201 Solids (2026 Properties of Matter ×4 ↑100%), keph202 Fluids, keph203 Thermal
Properties, keph205 Kinetic Theory, keph207 Waves (syllabus-reduced but still ×2),
leph105 Magnetism and Matter (2024×4 spike — verify vs rationalised syllabus),
leph108 EM Waves (2026×3 ↑50%).

## Entry template (same schema, pdfPage from keyword match)
```json
{"pdfPage": 9, "question": "verbatim stem from official paper",
 "options": ["A","B","C","D"], "answer": 1,
 "explanation": "own words + formula",
 "source": "NEET 2024 R1 via NTA", "year": "NEET 2024"}
```
Physics stems often carry diagrams — if the Q needs its figure, either
describe the setup fully in the stem or skip it and pick a text-complete one.
Never strip a diagram-dependent Q down to a guessable stub.

## Order of work
1. P0 seven files (+72 Qs) → physics 79→151
2. P1 thirteen files (+~80) → ~230
3. P2 remainder → ~250. Re-run `validate.py` after every file.
