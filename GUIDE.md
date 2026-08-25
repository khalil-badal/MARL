# GUIDE — Where the Manuscript Stands & Where It's Headed

*Group B3 · UST Electronics Engineering · Thesis Revision*
*Last updated: 2026-08-25*

This is the plain-English orientation doc for the thesis. Read this first if you
(a teammate, an adviser, or an AI assistant) want to understand **what the
manuscript is right now** and **the direction we're leaning toward** without
digging through LaTeX or git history.

---

## TL;DR (read this if you read nothing else)

- **Right now, the compiled manuscript is 100% Texas (CapMetro).** Every number,
  table, dataset description, calibration step, and evaluation is built on the
  **CapMetro Rapid Route 801** dataset from Austin, Texas.
- **The EDSA (Metro Manila) version still exists**, fully intact, but it is
  *switched off* — preserved in the source so nothing was lost.
- **The idea we're moving toward:** keep **EDSA as the motivation** (the
  real-world reason the problem matters) while **using the Texas dataset as the
  actual empirical testbed** (what we calibrate and evaluate on).
- **This is NOT done yet.** We are **waiting on our adviser's decision** before
  making that change. Until they say go, the manuscript stays fully Texas.

---

## 1. What the manuscript is today

### The topic hasn't changed
The thesis is still:

> **"An Evaluation of Multi-Agent Reinforcement Learning for Dynamic Bus
> Scheduling Under Non-Ideal Conditions."**

The title is deliberately **corridor-neutral** — it names no city — so it works
no matter which framing we land on. (The title is fixed; do not change it.)

### What actually compiles
Three chapters are live and build into the PDF:

| Chapter | File | Status |
|---|---|---|
| Ch. 1 — Introduction & Literature Review | `introduction.tex` | Live, Texas-based |
| Ch. 2 — Problem Statement | `problem.tex` | Live, Texas-based |
| Ch. 3 — Methods & Research Design | `methods.tex` | Live, Texas-based |
| Ch. 4 — Results | `results.tex` | Not written yet (commented out) |
| Ch. 5 — Discussion | `discussion.tex` | Not written yet (commented out) |
| Future Work / Appendix | `futurework.tex`, `appendix.tex` | Not written yet (commented out) |

Results don't exist yet because **the simulation hasn't been run** — this is a
**proposal** manuscript. No MARL training, no SUMO calibration, and no processed
results have happened. All figures marked "illustrative" are placeholders.

### What the manuscript is built on right now
Everything empirical is **CapMetro Rapid Route 801, Austin, Texas**:

- **Primary dataset:** CapMetro's public Automatic Passenger Counter (APC)
  archive, July–December 2021 (Texas Open Data Portal, Socrata `im6q-3pc9`).
  9,197,694 raw stop-event records across 47 fields; cleaned down to
  **229,421 records** for Route 801 direction code 6 (184 service days,
  29 distinct stops). The cleaning is reproducible and SHA-256 verified.
- **Weather:** NOAA Local Climatological Data v2 — Camp Mabry (primary),
  Austin-Bergstrom (sensitivity). Joined to APC events by nearest hour.
- **What's real vs. synthetic:** ordinary demand, dwell, load, and travel-time
  behavior come from the real data; **severe weather and breakdowns are
  explicitly synthetic stress tests** (the data has no breakdown field, and
  severe weather is out of the observed range).

### The EDSA version is preserved, not deleted
When the group pivoted from EDSA to Texas, we did **not** throw the EDSA work
away. It lives in two places:

1. **Inside the live files, switched off.** In `introduction.tex` (starting at
   line ~43) and `methods.tex` (starting at line ~215), the old EDSA content is
   wrapped in LaTeX `\iffalse … \fi` blocks. That means it's still in the file,
   still readable, but **does not appear in the compiled PDF**. Think of it as a
   light switch that's currently off.
2. **A full backup folder: `EDSA Ver/`.** This is the **EDSA manuscript with the
   panel revisions applied and the SafeTravelPH (EDSA) dataset still in place**,
   awaiting acquisition of the SafeTravelPH data — i.e., close to the June 2024
   defense manuscript but with all the RTC-requested revisions from 2026-08-06
   already addressed. It is our safety net / recovery point for the EDSA
   direction.
   - *Note (2026-08-25):* an earlier snapshot of this folder had accidentally
     picked up CapMetro dataset text in its dataset sections during the
     transition. That was cleaned out — `EDSA Ver/` now contains **no CapMetro /
     Texas / Austin references**; its dataset is SafeTravelPH throughout, exactly
     as an EDSA-with-revisions version should be.

The EDSA citations (DOTr ridership, EDSA breakdown reporting, Philippine
rainfall studies, typhoon service suspensions) are **still in the bibliography**,
so re-activating EDSA motivation wouldn't require hunting down sources again.

---

## 2. The direction we're leaning toward

### The core idea
**Motivate with EDSA. Calibrate and evaluate on Texas.**

In plain terms:

- **EDSA answers "why does this matter?"** Bus bunching under non-ideal
  conditions is a real, high-stakes problem, and the EDSA Carousel is a concrete
  example — it genuinely suffers weather disruptions, mechanical breakdowns, and
  demand surges, carrying hundreds of thousands of daily riders.
- **Texas/CapMetro answers "what did you actually test on?"** Because
  EDSA-quality operational data isn't publicly available or documented, we use
  CapMetro's **open, reproducible** APC dataset as the empirical testbed for the
  same class of control problem.

### Why this is a legitimate structure
This is a recognized and honest research pattern: a study can be **motivated** by
one context but **demonstrated** on a different, available dataset — as long as
the line between the two is never blurred.

It actually plays to our strengths. Our RTC panel pushed hard on "show us the
dataset, describe its contents, prove it's real" (comments E1C1, E2C5, E4C22).
EDSA data could never fully satisfy that — CapMetro does. So "we couldn't get
EDSA data, so we used a public, auditable dataset" is a **strength**, not an
excuse.

### The hard rule that keeps it honest

| ✅ We CAN say | ❌ We must NOT say |
|---|---|
| "Corridors like EDSA motivate studying combined disturbances." | "This study improves EDSA service." |
| "The disturbance *types* (weather, breakdowns, surges) reflect EDSA's documented reality." | Present Austin numbers as if they were EDSA's. |
| "Results are demonstrated on an Austin case; transfer to any specific corridor is future work." | Imply the dataset is EDSA's, or calibrate 'EDSA' from Austin data. |

As long as the **empirical basis is unmistakably labeled Texas** everywhere it
appears, motivating with EDSA is completely fine.

### The one thing to be careful about
EDSA's motivating weather is **typhoons and heavy tropical rain**. Austin's
*observed* weather is ordinary rain, and our *severe* weather is **synthetic**
anyway (a heavy-tailed lognormal stress test, not calibrated to any city). So:

- We **can** say "severe weather like EDSA's typhoons motivates a heavy-tailed
  stress test."
- We **cannot** say the synthetic severe-weather magnitudes are calibrated to
  EDSA typhoons.

Our current synthetic-stress framing already handles this correctly — it just
needs the motivation worded so it never implies Austin data measures
EDSA-grade weather.

---

## 3. What this change would actually involve (when/if approved)

**Important:** this is **not** as simple as flipping the `\iffalse` switches back
on. The EDSA content sitting in those blocks is the *old version where EDSA was
the empirical basis* — full EDSA calibration, the SafeTravelPH data plan,
EDSA-specific parameters. Turning it back on wholesale would create a
**self-contradicting manuscript**: EDSA calibration claims sitting right next to
CapMetro Route 801 tables.

The correct approach is a **scoped, deliberate rewrite**:

- **Re-activate EDSA only as motivation**, in two places:
  1. **Background of the Study** (the opening of Ch. 1) — lead with the general
     bunching problem, use EDSA as the concrete real-world instance, then bridge
     to CapMetro.
  2. **Significance** — note relevance to corridors like EDSA.
- **Write new "bridge" text** — the sentence(s) that explain *why* we motivate
  with EDSA but use Texas data (EDSA data isn't public; CapMetro is
  reproducible).
- **Leave every Texas empirical section untouched** — Ch. 2 problem statement,
  Ch. 3 methods, all tables, calibration, evaluation.
- **Re-check for contradictions** so nothing implies Austin data measures EDSA.

Estimated effort: roughly an hour of focused work. Every change would be tracked
in the audit trail like everything else.

---

## 4. Current status: WAITING ON THE ADVISER

**Nothing about the EDSA-motivation change has been done yet.** The manuscript is
fully Texas and stays that way until we get a decision.

### Questions to bring to the adviser
1. Does the panel expect the thesis to still be *about* EDSA (since they reviewed
   an EDSA proposal), or are they fine with **EDSA-as-motivation +
   Austin-as-testbed**?
2. Are they comfortable with the **generalizability framing** — that we make no
   on-EDSA performance claim?
3. Should the abstract reflect the Austin case study at all? (The title is
   corridor-neutral and stays as is.)

### Possible outcomes and what each means
- **"Yes, EDSA motivation + Texas data"** → we do the scoped rewrite in Section 3
  above.
- **"Keep it fully Texas"** → we do nothing; the manuscript is already there.
- **"Go back to fully EDSA"** → bigger job, but the `EDSA Ver/` backup and the
  `\iffalse` blocks mean the material still exists to restore.

---

## 5. For an AI assistant picking this up

If you're an AI assistant asked to help with this:

- **Do not make the EDSA change until a human explicitly says the adviser
  approved it.** This doc records intent, not authorization.
- When it's approved, do the **scoped rewrite** described in Section 3 — do
  **not** blindly un-comment the `\iffalse` blocks.
- Follow the existing rules: see `CLAUDE.md` (the full rulebook — no fabricated
  data, no fabricated citations, dataset-language rules) and `README.md` (the
  REWRITE workflow). Every manuscript change goes into both audit-trail files
  (`AUDIT_TRAIL.md` and `AUDIT_TRAIL_READABLE.md`).
- The manuscript's current state, and the full history of what changed and why,
  is in the audit trails. The Texas pivot is documented under the "2026-08-24 —
  Texas CapMetro pivot" entry.

---

## Quick reference — key files

| File | What it is |
|---|---|
| `GUIDE.md` | This document — orientation and current direction |
| `CLAUDE.md` | The full rulebook for editing the manuscript (esp. for AI) |
| `README.md` | Repo map + the REWRITE workflow |
| `REVISION_QUEUE.md` | The panel's revision tasks (all 22 done) |
| `TRACKER.md` | Per-task change log + conformity-table rows |
| `AUDIT_TRAIL.md` | Before/after log of every manuscript change (LaTeX) |
| `AUDIT_TRAIL_READABLE.md` | Same log, plain English |
| `RTC_DECISION_LETTER.md` | The verbatim panel feedback (source of truth) |
| `introduction.tex`, `problem.tex`, `methods.tex` | The live manuscript chapters (Texas) |
| `EDSA Ver/` | Full backup of the pre-pivot EDSA manuscript |

---

*This guide reflects the manuscript as of 2026-08-25 (latest commit `65076ff`).
Update it whenever the direction or status changes.*
