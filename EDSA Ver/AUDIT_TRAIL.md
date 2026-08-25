# AUDIT TRAIL (EDSA Ver) — Group B3 Thesis, EDSA Backup Folder
# Before/after log of the ACTUAL .tex CONTENT of the files in THIS folder
# (`EDSA Ver/`) ONLY. This is separate from the root-level AUDIT_TRAIL.md,
# which tracks the live/compiled manuscript (the Texas CapMetro version).
#
# WHAT THIS FOLDER IS:
#   `EDSA Ver/` is the EDSA manuscript as it stood at the last main-line commit
#   before the Texas CapMetro pivot — i.e., the June 2024 defense manuscript
#   with all 2026-08-06 panel (RTC) revisions applied, still on the
#   SafeTravelPH/EDSA dataset, awaiting acquisition of that dataset. It is the
#   recovery point for the EDSA research direction.
#
# Format: one ```diff fence per change. `-` = removed, `+` = added, no prefix =
# unchanged context. See AUDIT_TRAIL_READABLE.md (in this folder) for the
# plain-English companion.
#
# STATUS TAGS:
#   ACTIVE — the AFTER text is present in the current EDSA Ver files.

---

## 2026-08-25 — EDSA Ver restoration: strip CapMetro contamination, align to the true pre-pivot state
**Status:** ACTIVE
**Commits:** `299901a` (CapMetro cleanup), `42bfdb8` (alignment to `a64f44c`)

### Background

When the `EDSA Ver/` backup folder was first created (during the Texas pivot
commit `aff79b0`), it was populated from a transitional snapshot that had
already spliced the CapMetro Route 801 dataset into its dataset sections, and
was missing the two N2 self-identified additions the real pre-pivot manuscript
contained. The changes below restore `EDSA Ver/` to a faithful reproduction of
the authoritative pre-pivot main-line state (commit `a64f44c` = defense + all
2026-08-06 revisions, pure EDSA/SafeTravelPH, zero CapMetro). After these
changes, `EDSA Ver/introduction.tex` and `EDSA Ver/methods.tex` are
byte-identical (modulo line endings) to `a64f44c`, and `EDSA Ver/problem.tex`
differs only by a `TThe`->`The` typo fix and trailing whitespace.

### problem.tex — Scope: revert corridor label, remove CapMetro calibration paragraph

```diff
- \textbf{Scope.} This study develops and evaluates a MARL-based bus scheduling framework for a BRT corridor. The framework is built on a calibrated SUMO microsimulation [...]
+ \textbf{Scope.} This study develops and evaluates a MARL-based bus scheduling framework for the EDSA Carousel corridor. The framework is built on a calibrated SUMO microsimulation [...]

- The simulation is calibrated against a six-month Automatic Passenger Counter (APC) archive from Capital Metro Route 801 (Austin, TX, July--December 2021)~\cite{TexasCapMetroAPC2021}, comprising 229,421 validated stop-level event records across 184 service days and 29 stops, with 420,201 total recorded boardings. Weather conditions during the same period are captured via NOAA hourly surface observations~\cite{NOAALCDv2}. The dataset, cleaning methodology, and derived parameters are described in detail in Chapter~3, Section~3.2.5.
-
  For this study, \textbf{non-ideal conditions} are operating regimes [...]
```

### problem.tex — Research Gap: restore N2 self-identified addition

```diff
  [...] which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment.
+ This joint-disturbance framing reflects two independently-documented, concurrent operational realities of the same corridor rather than only a gap in existing comparison tables: EDSA experiences both weather-driven service disruptions \cite{PhilstarTyphoon2024, PIA_Emergency2023} and chronic mechanical-failure risk \cite{Chua2026} as ongoing features of its operating environment, so a controller validated against each in isolation provides no evidence of how it behaves when a transit operator's actual risk exposure includes both at once. The disturbance generators remain independently sampled within the simulation (Section~3.2.6); this operational context motivates evaluating their union, not a claim that the two are causally or temporally linked.
```

### problem.tex — Significance: restore N2 self-identified addition

```diff
- This study contributes both practical and scientific significance.
+ This study contributes both practical and scientific significance. MARL is the control method under evaluation in this study; the corridor's service reliability under disturbance is the object of study it is applied to measure, which is why practical significance is discussed first.
```

### methods.tex — Required Datasets: CapMetro APC bullets -> SafeTravelPH/EDSA bullet

```diff
- \item \textbf{Corridor bus operational data (primary).} The primary operational dataset is the Capital Metropolitan Transportation Authority (CapMetro) Automatic Passenger Counter (APC) raw archive for July--December 2021~\cite{TexasCapMetroAPC2021}, published on the Texas Open Data Portal (Socrata dataset ID \texttt{im6q-3pc9}). [...47-field CapMetro schema...]
-
- This study uses the subset corresponding to MetroRapid Route 801 (North Lamar/South Congress BRT corridor), direction code 6 (northbound), operated by New Flyer Xcelsior XDE60 articulated buses [...]
-
- After cleaning (Section~\ref{subsec:data-pipeline}), the usable subset comprises 229,421 stop-level event records spanning 184 service days with a total of 420,201 recorded boardings. [...]
-
- \item \textbf{Weather data (secondary).} Hourly surface observations from NOAA Local Climatological Data Version~2~\cite{NOAALCDv2} [...Camp Mabry / Austin-Bergstrom...]
-
- \item \textbf{Vehicle fleet data (supplementary).} The 2021 National Transit Database Revenue Vehicle Inventory~\cite{NTD2021Fleet} (NTD ID 60048) [...]
+ \item \textbf{Corridor bus operational data.} A per-trip record of EDSA Carousel bus operation along the study sub-corridor, collected over a continuous observation window of at least two weeks. The required fields are GPS-tracked vehicle location, boarding and alighting events, passenger occupancy, operating speed, and \textit{dwell time} at each stop [...] The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application.
+
+ %A crowdsourced operational dataset of this form [...] under the Freedom of Information process.
```

### methods.tex — field-mapping table: CapMetro field names -> generic EDSA fields

```diff
- \texttt{departure\_dtm}, GPS coordinates & Per-segment inter-stop travel time distribution ($\mu$, $\sigma$) & [...]
- \texttt{ons} (boardings per stop visit) & Per-(stop, time-of-day) baseline demand rate & [...]
- \texttt{offs} (alightings per stop visit) & Through-passenger volume per stop & [...]
- \texttt{load}, \texttt{max\_load} & Per-segment load profile & [...]
- Derived from consecutive \texttt{departure\_dtm} & Per-segment baseline cruising speed & [...]
- Derived from \texttt{stop\_sequence} timing & Per-(stop, time-of-day) dwell time distribution & [...]
+ GPS-tracked vehicle location & Per-segment inter-stop travel time distribution ($\mu$, $\sigma$) & [...]
+ Boarding events & Per-(stop, time-of-day) baseline demand rate & [...]
+ Alighting events & Through-passenger volume per stop & [...]
+ Passenger occupancy & Per-segment load profile & [...]
+ Operating speed & Per-segment baseline cruising speed & [...]
+ Dwell time & Per-(stop, time-of-day) dwell time distribution & [...]
```

Also, the field-map intro sentence had "All listed fields are present in the CapMetro APC archive" replaced with "The mapping reflects the study's design intent, not properties of a processed dataset; specific statistics remain \%TODO-DATA pending dataset acquisition."

### methods.tex — severe-weather paragraphs: remove NOAA-join framing

```diff
- Severe-weather conditions are not estimated from operational data alone. The NOAA weather join (Stage~2 of the pipeline) identifies which service days experienced measurable precipitation [...] rather than calibrated to a single corridor-specific severe-weather sample.
+ Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable, with disturbance magnitudes anchored to validated literature values rather than to a corridor-specific severe-weather sample.
+
+ A short empirical observation window cannot reliably resolve the variance of a heavy-tailed severe-weather distribution [...] The full disturbance parameterization is described in Section~\ref{subsec:stochastic-vars}.
```

### methods.tex — Data Pre-Processing Pipeline: 4-stage CapMetro -> 3-stage EDSA

```diff
- Pre-processing proceeds in four stages.
- \textit{Stage 1: Filtering and validation.} The raw APC archive is filtered [...] (\texttt{direction\_code\_id}~$= 6$) [...] reduce the archive from 9,197,694 records to 229,421 records [...]
- \textit{Stage 2: Temporal and weather join.} Cleaned stop-visit records are joined to NOAA hourly weather observations~\cite{NOAALCDv2} [...]
- \textit{Stage 3: Empirical distribution extraction.} [...]
- \textit{Stage 4: Train/validation split for calibration.} [...]
+ Pre-processing proceeds in three stages.
+ \textit{Stage 1: Cleaning.} Trip records with missing GPS coordinates, missing timestamps, negative inter-stop times, or trips that fail integrity checks [...] are dropped. [...] Records are therefore filtered to regular weekdays and binned by time-of-day [...]
+ \textit{Stage 2: Empirical distribution extraction.} For each (segment, time-of-day) bin, the cleaned operational data yield the mean $\mu$ and standard deviation $\sigma$ [...]
+ \textit{Stage 3: Train/validation split for calibration.} The calibration data are split chronologically [...]
```

### thesis_refs.bib — remove the 4 Texas-only entries

```diff
- @misc{TexasCapMetroAPC2021, ... Texas Open Data Portal, Socrata Dataset ID im6q-3pc9 ...}
- @misc{NOAALCDv2, ... Station USW00013958 (Camp Mabry, Austin, TX) ...}
- @misc{NTD2021Fleet, ... NTD ID 60048 (Capital Metropolitan Transportation Authority) ...}
- @misc{CapMetroRapid801, ... MetroRapid Route 801: North Lamar/South Congress ...}
```

**Why:** `EDSA Ver/` is supposed to be the pre-pivot EDSA manuscript with the
panel revisions applied and the SafeTravelPH/EDSA dataset still in place. A
transitional snapshot had introduced CapMetro Route 801 dataset content into
its dataset sections and had dropped the two N2 additions. These changes remove
all CapMetro/Texas references (verified: zero remain; no dangling `\cite`), and
restore the N2 additions and the field-map wording, so the folder now faithfully
matches the authoritative pre-pivot main-line state `a64f44c`. The E3C15
parameter table was already in correct EDSA form (M=24, DOTr, SafeTravelPH) and
was not touched; all other 2026-08-06 panel revisions were already present in
EDSA form and were preserved.

---

*Nothing follows.*
