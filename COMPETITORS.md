# Competitor teardown (Sept 2026 research) → what we steal, what we refuse

## Allen (test series + SPR)
- Has: exact exam simulation, Student Performance Report per test, AIR, timed tests,
  150+ NCERT tests / 6000+ Qs, improvement book, custom practice, revision notes.
- Steal: SPR idea → our 📊 weak-first dashboard (accuracy × weightage). Timed mode — planned.
- Refuse: paywall, account lock-in, AIR anxiety engine.

## BYJU'S (mock analysis method)
- Has: analysis framework — silly mistakes, guessed-vs-wrong, time-per-Q, skip-vs-risk,
  unattempted-question review.
- Steal: ❌ Mistake book with clear-to-retry (= their review loop, offline).
- Refuse: 10-minute generic advice articles instead of tooling.

## Darwin (33k MCQs, PrepDNA/EffortDNA/QuestionDNA)
- Has: biggest free-tier bank (8000 free), difficulty tags, weakness/effort analytics,
  mistake revision, 30-yr papers.
- Steal: weakness-first ordering (dashboard), difficulty awareness (weightage stars).
- Refuse: AI-slop-scale banks; our cap is verified-only even if smaller (874 and counting).

## MemoNeet (line-by-line NCERT, forgetting curve, streaks)
- Has: microtopic segmentation, spaced-repetition scheduling, gamified streaks, mistake book.
- Steal: mistake book (done); page-pinned Qs ARE microtopics (done via pdfPage).
- Refuse: AI revision claims, subscription.

## NEETprep / generic apps (paywall complaints in reviews)
- Users: "free version feels very limited… looking for completely free".
- Our wedge: 100% free, offline-capable, no login — stated in README, enforced by architecture
  (no backend, no accounts, no phone-home).

## PrepPage.in (the original reference)
- Has: split reader + 30-day plan + Pro tier (₹499): 34yr papers, 70+ papers, advanced analytics,
  revision system, OMR practice, 2000+ flashcards.
- Steal: split-reader UX (rebuilt original), OMR/timed ideas (planned).
- Refuse: cloning content/bank; Pro-gating core prep tools.

## Anki / spaced repetition (PMC studies 2023-25, Medscape, FSRS docs)
- Evidence: higher scorers start spaced repetition earlier + do more total reps;
  FSRS beats SM-2 for large decks; 97.6% of med students use PRE-MADE decks.
- Caveats we design around: transfer problem (cards train recall, exams test
  application in noise) + garbage prompts (scheduler can't fix bad cards) +
  multi-deck guilt-machine effect.
- Steal: timestamps on every attempt → mistake book sorted oldest-first with
  "N due for review" (3-day rule) = FSRS-lite with zero server.
- Our structural answer to the transfer problem: the bank IS exam-format retrieval
  practice (full NEET stems + distractors), not cloze cards. Pre-made-deck insight
  = our verified bank is the deck; page-pinning is the organization.
- Refuse: pretending scheduling replaces solving; daily-streak gamification.

## Embibe (AI analytics) + topper error-log method (AIR 39, PrepLadder, Eklavya)
- Embibe's real ideas: attempt-quality over raw score, overtime-correct as hidden
  weakness, time-per-Q benchmarks, predictive realism.
- Topper consensus: mistake notebook with cause tags (Concept/Silly/Calc/Time),
  55–60% of errors are non-knowledge; review same-day; 3-7-21 revision cycles;
  attempt-only-if-2-options-eliminated; single resource depth over variety.
- Steal (shipped): per-answer latency → dashboard Pace + Slow(>90s) columns,
  drill pace readout, one-tap cause tags on every mistake entry.
- Refuse: server-side prediction theater, rank predictions, OMR-fear content.

## NTA Abhyas (the official free app — dead) + ExamSIDE + neet.training/abhyas clones
- NTA Abhyas: free official mocks + AI analytics on paper. Reality 2024-26: 2.8★,
  login/pincode failures, dead backend, unanswered tickets. Lesson: official+free
  means nothing if it doesn't run. Our answer: no login, no server, offline-first —
  there is no backend to die.
- ExamSIDE's real edge: radical coverage transparency — per-chapter per-year counts,
  weightage %, trend arrows, 2000–2026 span, paper-wise + chapter-wise + mock.
  Steal (shipped): dashboard Years column (range + distinct-year count per chapter),
  computed live from our own year tags — exposes thin chapters instead of hiding them.
- neet.training / abhyasexams.in: "100% PYQs, no filler", free timed chapter mocks
  no login — closest living cousins. Their paywall arrives at 5 mocks / full mocks.
  Our wedge: unlimited everything + page-pinning + verified-only bank, free forever.
- Weightage cross-check (PW 5-yr: CE 9%, RayOptics 6%, Semi 6%, Units 6%, EP&C 7%):
  bumped Units to ★★★ in our map; rest confirmed.
- Refuse: rank prediction, login-gated analytics, trend-arrow theater on tiny samples.

## Our moat (free + verified + page-pinned)
Nobody else pins every question to the exact NCERT PDF page while staying free and offline.
That stays the identity. Everything added must serve it.
