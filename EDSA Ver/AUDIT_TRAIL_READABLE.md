# AUDIT TRAIL (EDSA Ver — READABLE) — Group B3 Thesis, EDSA Backup Folder
# Plain-English companion to AUDIT_TRAIL.md in THIS folder (`EDSA Ver/`).
# Same entries, same order, but with LaTeX markup stripped so the actual
# sentences are easy to read.
#
# This is SEPARATE from the root-level audit trails, which track the live
# (Texas CapMetro) manuscript. These two files track only the .tex files
# inside `EDSA Ver/`.
#
# WHAT THIS FOLDER IS:
#   `EDSA Ver/` is the EDSA manuscript as it stood at the last main-line
#   commit before the Texas CapMetro pivot — the June 2024 defense manuscript
#   with all the 2026-08-06 panel (RTC) revisions applied, still on the
#   SafeTravelPH/EDSA dataset, waiting only for that dataset to be acquired.
#   It is the recovery point for the EDSA research direction.
#
# Format: every change has a bold **BEFORE** and **AFTER**, with the part that
# actually changed in **bold**. No "..." truncation of the key sentences.
#
# STATUS TAGS:
#   ACTIVE — the AFTER text is present in the current EDSA Ver files.

---

## 2026-08-25 — EDSA Ver restoration: strip CapMetro contamination, align to the true pre-pivot state
**Status:** ACTIVE
**Commits:** `299901a` (CapMetro cleanup), `42bfdb8` (alignment to the pre-pivot state)

### What happened, in one paragraph

When the `EDSA Ver/` backup was first created (during the Texas pivot), it was
populated from a transitional copy that had **already replaced the SafeTravelPH
dataset with the CapMetro Route 801 dataset** in its dataset sections — and it
was **missing two of the group's own self-identified additions (N2)** that the
real pre-pivot manuscript had. In short, the backup was not a clean "EDSA +
revisions" copy; it was a half-migrated hybrid. The changes below strip out all
the CapMetro/Texas content and put back the missing pieces, so `EDSA Ver/` now
faithfully reproduces the real pre-pivot EDSA manuscript (defense + all
2026-08-06 panel revisions, SafeTravelPH dataset, no Texas anywhere).

After these fixes: the Introduction and Methods chapters are identical to the
real pre-pivot manuscript, and the Problem Statement differs only by a typo fix
(a stray "TThe" corrected to "The") and some trailing spaces.

---

### 1. problem.tex — Scope section

**BEFORE**

"This study develops and evaluates a MARL-based bus scheduling framework for **a BRT corridor**. The framework is built on a calibrated SUMO microsimulation and runs over a single-day operational horizon..."

Followed by a whole extra paragraph: "**The simulation is calibrated against a six-month Automatic Passenger Counter (APC) archive from Capital Metro Route 801 (Austin, TX, July–December 2021), comprising 229,421 validated stop-level event records across 184 service days and 29 stops, with 420,201 total recorded boardings. Weather conditions during the same period are captured via NOAA hourly surface observations. The dataset, cleaning methodology, and derived parameters are described in detail in Chapter 3, Section 3.2.5.**"

**AFTER**

"This study develops and evaluates a MARL-based bus scheduling framework for **the EDSA Carousel corridor**. The framework is built on a calibrated SUMO microsimulation and runs over a single-day operational horizon..."

**The entire Capital Metro / Austin / NOAA calibration paragraph was removed.** The Scope now flows straight into the definition of non-ideal conditions, as in the defense manuscript.

---

### 2. problem.tex — Research Gap (restored the missing N2 addition)

**BEFORE**

The Research Gap paragraph ended at: "...which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment." (The N2 sentence was missing from the backup.)

**AFTER**

The same paragraph, now with the N2 addition restored: "...which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment. **This joint-disturbance framing reflects two independently-documented, concurrent operational realities of the same corridor rather than only a gap in existing comparison tables: EDSA experiences both weather-driven service disruptions (Philstar typhoon reporting; PIA emergency-response reporting) and chronic mechanical-failure risk (Chua, 2026) as ongoing features of its operating environment, so a controller validated against each in isolation provides no evidence of how it behaves when a transit operator's actual risk exposure includes both at once. The disturbance generators remain independently sampled within the simulation (Section 3.2.6); this operational context motivates evaluating their union, not a claim that the two are causally or temporally linked.**"

---

### 3. problem.tex — Significance (restored the missing N2 addition)

**BEFORE**

"This study contributes both practical and scientific significance."

**AFTER**

"This study contributes both practical and scientific significance. **MARL is the control method under evaluation in this study; the corridor's service reliability under disturbance is the object of study it is applied to measure, which is why practical significance is discussed first.**"

---

### 4. methods.tex — Required Datasets (CapMetro dataset → SafeTravelPH/EDSA dataset)

**BEFORE**

Three CapMetro bullets: a "primary" bullet describing the **Capital Metro (CapMetro) APC raw archive for July–December 2021 (Socrata im6q-3pc9), 9,197,694 records across 47 fields**; a paragraph naming **MetroRapid Route 801 (North Lamar/South Congress BRT), direction code 6, New Flyer XDE60 buses, 123-passenger crush capacity, 29 stops over 20 miles**; a cleaning paragraph citing **229,421 records / 420,201 boardings**; a **NOAA weather** secondary bullet (Camp Mabry / Austin-Bergstrom); and a **2021 NTD Revenue Vehicle Inventory** supplementary bullet.

**AFTER**

A single EDSA bullet, restored from the defense manuscript: "**Corridor bus operational data.** A per-trip record of EDSA Carousel bus operation along the study sub-corridor, collected over a continuous observation window of at least two weeks. The required fields are GPS-tracked vehicle location, boarding and alighting events, passenger occupancy, operating speed, and dwell time at each stop... **The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application.**" (Plus the original commented-out note about supplementary MMDA/DOTr/FOI records.)

---

### 5. methods.tex — Field-mapping table (CapMetro column names → generic EDSA fields)

**BEFORE** (raw-field column used CapMetro database field names)

departure_dtm + GPS coordinates · ons (boardings per stop visit) · offs (alightings per stop visit) · load, max_load · derived from consecutive departure_dtm · derived from stop_sequence timing

The intro sentence also said "**All listed fields are present in the CapMetro APC archive.**"

**AFTER** (raw-field column uses the study's generic data requirements)

**GPS-tracked vehicle location · Boarding events · Alighting events · Passenger occupancy · Operating speed · Dwell time**

The intro sentence now reads: "**The mapping reflects the study's design intent, not properties of a processed dataset; specific statistics remain TODO-DATA pending dataset acquisition.**" (The middle "Derived Parameter" and "MARL Component" columns were unchanged.)

---

### 6. methods.tex — Severe-weather paragraphs (removed the NOAA-join framing)

**BEFORE**

"Severe-weather conditions are not estimated from operational data alone. **The NOAA weather join (Stage 2 of the pipeline) identifies which service days experienced measurable precipitation** and provides empirical evidence that rain events occur within the observation period, but the severe-weather generator's disturbance magnitudes are swept across a range of coefficient-of-variation values anchored to the validated lognormal form of Patil et al. rather than calibrated to a single corridor-specific severe-weather sample."

**AFTER**

"Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable, with disturbance magnitudes anchored to validated literature values rather than to a corridor-specific severe-weather sample." (Followed by the defense manuscript's "short empirical observation window..." paragraph, restored.)

---

### 7. methods.tex — Data Pre-Processing Pipeline (4 CapMetro stages → 3 EDSA stages)

**BEFORE**

"Pre-processing proceeds in **four** stages." — Stage 1: Filtering and validation (filter the raw APC archive by route/import-error/stop-id/direction code 6, reducing 9,197,694 → 229,421 records, SHA-256 verified); Stage 2: Temporal and weather join (join to NOAA hourly weather at Camp Mabry); Stage 3: Empirical distribution extraction; Stage 4: Train/validation split.

**AFTER**

"Pre-processing proceeds in **three** stages." — Stage 1: Cleaning (drop records with missing GPS/timestamps/negative times, filter to weekdays, bin by time-of-day); Stage 2: Empirical distribution extraction; Stage 3: Train/validation split. (The defense manuscript's SafeTravelPH-oriented pipeline.)

---

### 8. thesis_refs.bib — removed the 4 Texas-only citations

**BEFORE**

Four CapMetro/Texas bibliography entries were present: **TexasCapMetroAPC2021** (Socrata im6q-3pc9), **NOAALCDv2** (Camp Mabry, Austin), **NTD2021Fleet** (NTD ID 60048), and **CapMetroRapid801** (MetroRapid Route 801).

**AFTER**

**All four removed.** The bibliography is now identical to the defense manuscript's. (Verified: no remaining citation in the EDSA Ver text points to any of these four keys, so there are no broken references.)

---

**Why (all of the above):** `EDSA Ver/` is meant to be the pre-pivot EDSA
manuscript with the panel revisions applied and the SafeTravelPH/EDSA dataset
still in place, waiting only for that dataset. A transitional snapshot had
spliced the CapMetro dataset in and dropped the two N2 additions. These changes
remove every CapMetro/Texas/Austin reference and restore the missing content, so
the folder now faithfully matches the authoritative pre-pivot manuscript. The
parameter-summary table was already in correct EDSA form (24 stops, DOTr
schedule, SafeTravelPH source) and was left untouched; every other 2026-08-06
panel revision was already present in EDSA form and preserved.

**Cross-check performed:** after the fix, the Introduction and Methods chapters
are byte-identical to the real pre-pivot manuscript; the Problem Statement
differs only by a "TThe"→"The" typo fix and trailing whitespace; the Research
Objectives and all Expected Outputs are identical to the June 2024 defense; and
every citation key resolves.

---

*Nothing follows.*
