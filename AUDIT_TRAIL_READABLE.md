# AUDIT TRAIL (READABLE) — Group B3 Thesis Manuscript Changes
# Plain-English companion to AUDIT_TRAIL.md. Same entries, same order, same
# before/after content — but LaTeX markup stripped out (\cite{} → (Author,
# Year), \ref{}/\label{} → plain section/table names, math mode → words,
# \textbf{}/\textit{} → plain text) so the actual sentences are easy to read
# and easy to reuse when rewriting or discussing ideas.
#
# Format: every entry has a bold **BEFORE** label on its own line, a blank
# line, then its paragraph — then the same for **AFTER**. No ellipsis
# truncation — write the actual relevant sentence(s) in full rather than
# trailing off with "...". Within the AFTER paragraph, the part that's
# actually new/different is **bolded**; unchanged surrounding text stays
# plain so your eye goes straight to the change.
#
# This file is NOT what goes into Overleaf — for the compilable LaTeX, use
# AUDIT_TRAIL.md. This file is for reading, discussing, and drafting.
# Keep both in sync: whenever AUDIT_TRAIL.md gets a new entry, add the same
# entry here in this BEFORE/AFTER format.
#
# STATUS TAGS (added after entry header):
#   ACTIVE      — the AFTER text is still present in the current .tex files
#   SUPERSEDED  — the AFTER text was overwritten by a later change (usually
#                 the 2026-08-24 Texas pivot); kept for history
#   REVERTED    — the change was undone before it shipped
#   mixed       — entry has multiple sub-changes with different statuses;
#                 each is listed individually in a table
#
# REWRITE WORKFLOW:
#   When applying writing-style changes, a third block is added:
#     **BEFORE**  — original text before the revision
#     **AFTER**   — revision agent's (or Jared's) version
#     **REWRITE** — user's writing-style-adjusted version
#   The REWRITE replaces AFTER as the live manuscript text. When a REWRITE
#   is applied, both audit trail files and the .tex file are updated together.

---

## 2026-08-06 — E1C3 — problem.tex, Section 2.2 (Research Gap)
**Status:** SUPERSEDED — problem.tex fully rewritten for CapMetro in Texas pivot

**BEFORE**

"It cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment."

**AFTER**

"It cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment. **The weather-disturbance class (W) in particular was identified through the literature survey conducted earlier in this study (the 'MARL Applied to Bus Scheduling' section), which found that no prior MARL bus-scheduling paper models heavy-tailed weather-induced travel-time delays (see the W column of the MARL literature table). Its operational relevance to the EDSA corridor is established by the rainfall-driven reductions in average speed and free-flow capacity documented in Section 1.1 (TSSP Rain 2018) and by the typhoon-related service suspensions on record for the corridor (DOTr 2020). The lognormal parameterization for this disturbance class follows the Kolmogorov-Smirnov-validated form from Patil et al., introduced here to address the resulting lack of temporally aligned, corridor-specific anomaly data (the 'Disturbance Gap' section).**"

**Why:** RTC comment 3 — the research gap section should explain how the weather disturbance column was arrived at.

---

## 2026-08-06 — E2C6 — introduction.tex 1.2.1, methods.tex Baseline Controllers
**Status:** ACTIVE — all four additions verified present (NC/FH/EH sentences reworded in Texas pivot but functionally equivalent)

**BEFORE (introduction.tex)**

"Allowing small headway perturbations to amplify into bunching (Daganzo 2009). Static schedules therefore remain mathematically inadequate for stochastic traffic environments, where the governing quantities are random variables rather than deterministic constants. These limitations motivated the transition toward more adaptive and data-driven scheduling methodologies."

**AFTER (introduction.tex)**

"Allowing small headway perturbations to amplify into bunching (Daganzo 2009). Static schedules therefore remain mathematically inadequate for stochastic traffic environments, where the governing quantities are random variables rather than deterministic constants. **Under the specific non-ideal conditions this study targets, the failure modes differ by control strategy. A fixed timetable has no feedback mechanism at all, so once bunching begins nothing in the schedule corrects it. A local reactive rule that holds a bus based only on the gap to the bus ahead can partially correct bunching under ordinary congestion, but has no way to respond to a breakdown, since it observes only the forward gap and not the enlarged gap a failed bus leaves behind it. A more globally aware reactive rule that accounts for both the forward and backward gap improves on this, but still follows a fixed, pre-specified rule rather than a learned response, so it cannot adapt its behavior to the heavier-tailed delays that severe weather introduces.** These limitations motivated the transition toward more adaptive and data-driven scheduling methodologies."

**BEFORE (methods.tex, No Control subsection, excerpt)**

"NC also provides the reference point for measuring the severity of bus bunching."

**AFTER (methods.tex, No Control subsection, excerpt)**

"NC also provides the reference point for measuring the severity of bus bunching. **Under non-ideal conditions, NC has no corrective mechanism whatsoever, so demand surges, weather-induced delays, and breakdowns are expected to compound directly into bunching with no attenuation.**"

Similar one-sentence additions were made to Forward Headway and Even Headway's subsections — FH can't see the backward gap a breakdown creates; EH has no way to anticipate weather's heavy-tailed delays.

**Why:** RTC comment 6 — explain how traditional non-AI scheduling performs under bunching/weather/breakdowns.

---

## 2026-08-06 — E2C7 — methods.tex, Section 3.2.10
**Status:** ACTIVE

**BEFORE**

"The acceptance criterion is twofold: (i) mean passenger waiting time no worse than Even Headway (no statistically significant degradation at p < 0.05 with multiple-comparison correction), and ideally a statistically significant improvement; and (ii) a statistically significant reduction in headway coefficient of variation relative to No Control."

**AFTER**

**Stage A acceptance criterion**

**(i)** Mean passenger waiting time no worse than EH (no statistically significant degradation at p < 0.05 with multiple-comparison correction), and ideally a statistically significant improvement.

**(ii)** A statistically significant reduction in headway coefficient of variation relative to NC.

**Stage B acceptance criterion:** The MARL policy is reported as performing well under disturbance if its mean waiting time stays below that of the best-performing baseline across the full sweep, with statistical significance under the same correction as Stage A.

**Why:** RTC comment 7 — describe what successful performance will look like, make it more visually prominent. No new thresholds were invented — only reformatted from inline sentence to labeled callout boxes.

---

## 2026-08-06 — E3C12 — introduction.tex, Section 1.2.3 (after Figure 1.3)
**Status:** SUPERSEDED — Figure 1.3 explanation removed in Texas pivot

**BEFORE**

"Multi-Agent Reinforcement Learning (MARL) addresses the three limitations above by decomposing decision-making across multiple agents that share the environment."

(No text existed between Figure 1.3's caption and this sentence.)

**AFTER**

"**In both panels of Figure 1.3, the per-bus state (the same thing methods.tex calls s_i,t in its formal notation, shown in the figure as the local observation o_i) encodes the bus's current position, forward and backward headways, onboard load, and queue length at its current stop, as defined in full in the State Space section. The action is the holding-strength and stop-skipping decision the controller emits for that bus, defined in the Action Space section. In the SARL panel (a), a single centralized network ingests all N per-bus state vectors concatenated into one global state and outputs all N actions simultaneously; in the MARL panel (b), the same shared network weights instead process each bus's local state independently, so each agent acts on only its own observation rather than the concatenated global one.** Multi-Agent Reinforcement Learning (MARL) addresses the three limitations above by decomposing decision-making across multiple agents that share the environment."

**Why:** RTC comment 12 — explain the concepts in Figure 1.3 (bus states and actions).

---

## 2026-08-06 — E3C13 — introduction.tex Section 1.1, methods.tex Section 3.2.3
**Status:** SUPERSEDED — both sub-parts removed in Texas pivot (intro.tex NLEx paragraph inside `\iffalse`; methods.tex EDSA calibration sentence deleted)

**BEFORE (introduction.tex)**

"Empirical studies on Philippine expressways show that increasing rainfall intensity significantly reduces average traffic speed and free-flow capacity (TSSP Rain 2018)."

**AFTER (introduction.tex)**

"Empirical studies on Philippine expressways show that increasing rainfall intensity significantly reduces average traffic speed and free-flow capacity (TSSP Rain 2018). **This rainfall-impact evidence is drawn from a 2018 study of the North Luzon Expressway rather than the EDSA Busway, and is used here only as contextual motivation that weather materially affects Philippine road-traffic operations; the weather-disturbance generator in this study does not adopt this study's specific speed-reduction percentages, and EDSA-specific travel-time behavior is independently calibrated through the GEH/RMSE procedure described in Section 3.2.3.**"

**BEFORE (methods.tex, Environment Model Validation opening)**

"The calibration is restricted to the bus corridor itself, since the agents' state and reward depend only on bus dynamics; surrounding mixed-traffic flows do not enter the Python environment."

**AFTER (methods.tex, Environment Model Validation opening)**

"The calibration is restricted to the bus corridor itself, since the agents' state and reward depend only on bus dynamics; surrounding mixed-traffic flows do not enter the Python environment. **This GEH/RMSE procedure calibrates EDSA-specific parameters directly from EDSA operational data and does not depend on the North Luzon Expressway rainfall-impact figures cited as motivating evidence in Section 1.1; that citation establishes only that weather materially affects Philippine road-traffic operations in general, not any EDSA-specific speed or capacity value used in this calibration.**"

**Why:** RTC comment 13 — Reference [10] is both dated (2018) and a different corridor (North Luzon Expressway, not EDSA); clarify whether its data was adopted or independently tuned for EDSA. This version fixes an earlier draft that only addressed the corridor-mismatch half, missing the "not quite new" recency half — caught during the cross-check against the verbatim RTC letter.

---

## 2026-08-06 — E3C8 — methods.tex, Section 3.2.6
**Status:** ACTIVE

**BEFORE**

"Four stochastic generators inject variability into the Python environment. Generators (i) and (ii) follow the perturbation framework of Wang and Sun; the weather generator's heavy-tailed lognormal formulation follows Patil et al.; the breakdown generator follows the rescheduling formulation of Cao et al. The notation table collects the symbols used across this section and the MARL formulation that follows."

(No definitions of the individual disturbance classes preceded this paragraph.)

**AFTER**

"**This study distinguishes five disturbance classes, denoted D, S, T, W, and B:**

- **Stochastic demand (D):** the baseline, always-present day-to-day randomness in passenger arrivals, drawn from the calibrated per-stop, per-time-of-day demand distributions. D is not a disturbance layered on top of a deterministic baseline — it IS the baseline stochastic environment, present in every run regardless of which other generators are active.
- **Demand surge (S):** an episode-level multiplicative scaling factor that amplifies baseline boarding rates above their empirical mean. S is the controlled experimental variable; D is always present, and S is what is added on top of it. Setting the standard deviation to 0 removes the surge and leaves only baseline demand variability (D).
- **Traffic-speed perturbation (T):** an episode-level scaling of corridor cruising speed, representing everyday congestion friction.
- **Weather-induced delay (W):** a per-segment travel-time distribution drawn from a right-skewed lognormal. W replaces T as the source of travel-time stochasticity once the intensity parameter exceeds zero.
- **Discrete bus breakdown (B):** a Poisson-distributed discrete event, with rate lambda, that permanently removes one bus from the active agent set for the remainder of the simulated day.

The generators that produce S, W, and B are sampled independently conditional on the always-active D and T baselines: no causal chain links them within the simulation. A breakdown does not trigger a demand surge or weather delay, and weather does not induce a mechanical failure. This factorial choice supports attribution in the single-disturbance ablations; it is not a claim that real disturbances are causally independent.**

Four stochastic generators inject variability into the Python environment..."

**Why:** RTC comment 8 — define each disturbance explicitly, clarify independence, distinguish stochastic demand from demand surge.

---

## 2026-08-06 — E3C15 — methods.tex, Section 3.2.4 (end)
**Status:** ACTIVE

**BEFORE**

"A condition is a state of the world; a controller is a choice of algorithm."

(Then moved straight into the "Data Processing" section — no parameter summary table existed.)

**AFTER**

"A condition is a state of the world; a controller is a choice of algorithm.

**Simulation parameter summary: fixed, swept/variable, and derived parameters (new table inserted here)**

| Parameter | Symbol | Value / Source |
|---|---|---|
| *Fixed* | | |
| Simulation horizon | — | Single observed Route 801 service window (TODO-DATA) |
| Total distinct stop IDs (direction code 6) | M | 29 (reproduced from CapMetro APC audit) |
| Fleet size (active buses) | N | TODO-DATA: derive from concurrent Route 801 vehicle activity |
| Control stop count | — | TODO-VAL: select from 29 observed stop IDs |
| Scheduled headway | H₀ | TODO-DATA: 2021-compatible GTFS or schedule record |
| Bus passenger capacity | — | TODO-DATA: verified vehicle/fleet specification |
| Maximum holding duration | ΔT | TODO-VAL: to be set during implementation |
| Holding action bins | Ω | {0.0, 0.1, 0.2, 0.3, 0.4} |
| Action space size per agent | \|Aᵢ\| | 10 (5 hold × 2 skip) |
| Monte Carlo runs per cell | N_runs | ≥ 30 |
| Discount / event-based discount | γ, β | TODO-VAL: tuned during implementation |
| *Swept / variable* | | |
| Synthetic severe-weather intensity | η | {0.0, 0.3, 0.6, 1.0, 1.3} |
| Demand-surge scale | f_d | N(1, σ_d²) clipped to [1, 3] |
| Traffic-speed stress scale | f_s | N(1, σ_s²) clipped to [0.8, 1.2] |
| Breakdown rate | λ | TODO-VAL: declared scenario rate |
| *Derived empirical/calibration* | | |
| Baseline inter-stop travel time | μ | Per-segment, time-of-day, day-type bin (to be computed) |
| Baseline travel-time std. dev. | σ | Per-segment, time-of-day, day-type bin (to be computed) |
| Baseline coefficient of variation | CV₀ | σ/μ per segment (TODO-DATA) |
| Lognormal shape parameter | σ_ln | √(ln(η²+1)) |
| Lognormal unit-mean factor location | μ_ln | −σ_ln²/2 |

The table is the parameter reference for this chapter. A TODO-VAL is a design value still requiring an explicitly justified experimental choice; a TODO-DATA is a value blocked on an external source or unfinished empirical derivation."

**Why:** RTC comment 15 — summarize fixed and variable simulation parameters with target values.

---

## 2026-08-06 — E4C20 — methods.tex, Section 3.2.6 (four generator subsections)
**Status:** mixed — 2 of 4 sentences survived the Texas pivot

| # | Generator | Status |
|---|-----------|--------|
| 1 | Passenger Demand | ACTIVE |
| 2 | Traffic Delays | SUPERSEDED (subsection rewritten, sentence removed) |
| 3 | Weather-Induced Anomalies | SUPERSEDED (subsection rewritten, sentence removed) |
| 4 | Bus Breakdowns | ACTIVE |

Each of the four disturbance generator subsections had a BEFORE sentence describing the generator statistically, and the AFTER appended an implementation-mechanics sentence to it.

**Passenger Demand (ACTIVE)**

**BEFORE:** "Sampling occurs at the start of each simulation run, producing varied demand profiles across episodes."

**AFTER:** "Sampling occurs at the start of each simulation run, producing varied demand profiles across episodes. **In implementation, the scaling factor f_d ~ N(1, σ_d²) is sampled once per episode at initialization and applied uniformly to every per-stop, per-time-of-day arrival rate for the duration of that simulated operating day, so all stops experience the same proportional demand shift within a single run while the shift itself varies across runs.**"

**Traffic Delays (SUPERSEDED)**

**BEFORE:** "Ordinary inter-stop travel time is sampled from the empirical T distribution for the current segment, time-of-day, and day-type stratum. If a separate corridor-wide stress test is retained, a speed scaling factor is sampled once per episode and clipped to [0.8, 1.2], representing typical daily congestion friction (Wang and Sun)."

**AFTER:** "Ordinary inter-stop travel time is sampled from the empirical T distribution for the current segment, time-of-day, and day-type stratum. If a separate corridor-wide stress test is retained, a speed scaling factor is sampled once per episode and clipped to [0.8, 1.2] (Wang and Sun). **In implementation, the speed scaling factor f_s ~ N(1, σ_s²) is sampled once per episode and applied to the bus's mean cruising speed on every inter-stop segment traversal during that day, producing a uniformly slower or faster corridor for that run without segment-level variation beyond the calibrated baseline.**"

Current methods.tex Traffic Delays subsection was rewritten in the Texas pivot and no longer contains this sentence — it now reads: "Ordinary inter-stop travel time is sampled from the empirical T distribution for the current segment, time-of-day, and day-type stratum. If a separate corridor-wide stress test is retained, the speed scaling factor is sampled once per episode and clipped to [0.8, 1.2] (Wang and Sun); its standard deviation is a TODO-VAL and is not equal to either clip bound. T remains active when W or B is enabled."

**Weather-Induced Anomalies (SUPERSEDED)**

**BEFORE:** "The mapping from η to a specific named weather severity...regardless of its meteorological label."

**AFTER:** "...regardless of its meteorological label. **In implementation, when η > 0 a fresh travel-time sample T ~ LogNormal(μ_ln, σ_ln) is drawn independently for each bus at each inter-stop segment traversal during the episode, replacing the traffic-speed generator's output for that traversal; the lognormal parameters μ_ln and σ_ln are computed from the segment's empirical mean and the swept η via the method-of-moments equations given earlier.**"

Current methods.tex Weather-Induced Anomalies subsection was rewritten in the Texas pivot (now uses a composed weather factor applied on top of the traffic-speed distribution, T_W = T_0 · m(w) · F_W) and no longer contains this sentence.

**Bus Breakdowns (ACTIVE)**

**BEFORE:** "Breakdowns are therefore a labeled synthetic stressor triggered at random times from a Poisson process with a configurable rate lambda (notation table)."

**AFTER:** "Breakdowns are therefore a labeled synthetic stressor triggered at random times from a Poisson process with a configurable scenario rate lambda (notation table). **In implementation, at each discrete simulation timestep of length dt, a Bernoulli trial with probability λ · dt is evaluated independently for each active bus; a success removes that bus from the active agent set for the remainder of the simulated day.**"

**Why:** RTC comment 20 — explain in detail how each disturbance scenario is actually simulated.

---

## 2026-08-06 — E4C21 — methods.tex, Sections 3.2.9 and 3.2.7
**Status:** ACTIVE

**BEFORE (3.2.9 opening)**

"For each (control strategy, disturbance level) cell, at least 30 independent Monte Carlo runs are executed using matched random seeds across strategies. Three response variables are logged per run: mean passenger waiting time, mean total travel time, and headway coefficient of variation."

**AFTER (3.2.9 opening)**

"**The three response variables logged per run are defined as follows. Mean passenger waiting time (W̄) is the average time elapsed from a passenger's arrival at a stop to their successful boarding, averaged across all passengers served and all stops over one simulated operating day: W̄ = (1/P) Σ (t_board − t_arrive), where P is the total number of passengers served. Mean total travel time (T̄) is the average elapsed time from a bus's departure from the origin terminal to its arrival at the final stop of the sub-corridor, averaged across all bus trips completed during the simulated day. Headway coefficient of variation (CV_h) measures headway regularity: CV_h = σ_h / μ_h, where σ_h and μ_h are the standard deviation and mean of observed inter-bus headways. CV_h = 0 denotes perfectly regular headways; larger values indicate increasing bunching severity.** For each (control strategy, condition) cell, N_runs ≥ 30 independent Monte Carlo runs are executed using matched random seeds across strategies."

**BEFORE (3.2.7 State Space, end of bullet list)**

"Environmental flags: encoded indicators for the current disturbance intensity and any active downstream incident or breakdown."

(Then jumped straight to the "Action Space" subsection.)

**AFTER (3.2.7 State Space, end of bullet list)**

"Environmental flags: encoded indicators for the current disturbance intensity and any active downstream incident or breakdown.

**Agent observation vector: features, symbols, and data sources (new table inserted here)**

| Feature | Deployment Source | Simulation Source |
|---|---|---|
| Control stop index | Hardcoded list | Hardcoded list |
| Forward headway | AVL feed | Event-driven bus model |
| Backward headway | AVL feed | Event-driven bus model |
| Onboard count | APC system | Event-driven bus model |
| Waiting count | AFC terminal / camera | Simulated queue |
| Disturbance flag | Weather API | Generator parameter |
| Breakdown flag | Incident system | Generator event |

In simulation, all observation features are generated synthetically by the Python environment at each control event by querying the analytical bus model and the active stochastic generators; no real sensor data is consumed during training or evaluation.**"

**Why:** RTC comment 21 — include details on the metrics and description of observation features.

---

## 2026-08-06 — E1C1+E2C5+E4C22 — REVERTED, no net change

**BEFORE**

"Corridor bus operational data. A per-trip record of EDSA Carousel bus operation along the study sub-corridor... The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application."

"Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable..."

**DRAFTED (never committed)**

"Corridor bus operational data..." [same as before]

"**The baseline operating point described above is grounded in the SafeTravelPH dataset: a crowdsourced mobile application through which commuters submit trip-level GPS trajectory reports while travelling along Philippine transit corridors... Each submission corresponds to a single commuter trip and yields a per-trip trajectory log... The dataset comprises TODO-DATA: insert total trip record count...**"

[Table: SafeTravelPH dataset fields and their role in simulation calibration — 6 rows]

"**A secondary source of station-level ridership aggregates... is to be acquired from the Department of Transportation (DOTr) under the Freedom of Information framework...**"

"Severe-weather conditions are not estimated from operational data in this study..."

**REVERTED TO (final, pushed state)**

Same as BEFORE — the drafted block was removed entirely before any commit.

**Why reverted:** the user caught this before any commit — the group doesn't actually have access to the SafeTravelPH dataset yet, and even though the numbers were placeholder-tagged, the qualitative description asserted more familiarity with the dataset than is currently honest.

---

## 2026-08-06 — Citation fix: Patil2025Conformal — methods.tex, Section 3.2.6
**Status:** SUPERSEDED — methods.tex Section 3.2.6 rewritten in Texas pivot

**BEFORE**

"Patil et al. validated this parameterization against INRIX freeway data via the Kolmogorov-Smirnov test, reporting a close fit at the highest variability level they tested (KS = 0.036, p = 0.94 at CV = 1.0)."

**AFTER**

"Patil et al. **tested this parameterization by generating SUMO-simulated travel times under the same CV-driven lognormal recipe, with time windows and mean travel times anchored to INRIX historical data for an urban arterial corridor, not a freeway, and confirming via the Kolmogorov-Smirnov test that the simulated distribution matches the assumed log-normal shape**, reporting a close fit at the highest variability level they tested (KS = 0.036, p = 0.94 at CV = 1.0)."

**Why:** checked against the actual paper. Its own Table V classifies the test route as "Local, Minor/Principal Arterials" — not a freeway. Also, the KS test checks whether SUMO-simulated travel times follow the assumed log-normal shape; it isn't a direct comparison against INRIX's own data. The numeric KS/p values themselves were confirmed correct — only the description of what was tested and against what changed.

---

## 2026-08-06 — Citation fix: Rodriguez2023Cooperative — methods.tex, Section 3.2.7
**Status:** ACTIVE

**BEFORE**

"A continuous holding parameter was considered but rejected for three reasons. First, continuous actions require actor-critic algorithms with training instability. Second, Rodriguez et al. showed that a 5-bin discretization achieves combined holding-and-skipping control on a comparable corridor without measurable loss of performance versus continuous formulations. Third, real driver compliance with second-level holding instructions is itself coarse, so continuous precision is not meaningful at deployment."

**AFTER**

**"This study's action space (10 discrete actions: 5 holding strengths times 2 skip choices, selected independently) is broader than Rodriguez et al.'s combined holding-and-skipping controller, which instead selects among 6 mutually exclusive actions: 5 holding strengths, where zero-strength already covers 'no holding,' plus a single separate skip action. The same 5-value holding-strength set is used in both studies."** A continuous holding parameter was considered but rejected for two reasons: continuous actions require actor-critic algorithms with training instability, and **"real driver compliance with holding instructions is itself imperfect — Rodriguez et al. model non-compliant drivers as executing only 60-80% of the instructed holding time"** — so continuous precision isn't meaningful at deployment anyway.

**Why:** checked against the full paper. No comparison against a continuous action space exists anywhere in it — that claim was unsupported and has been removed. Rodriguez's actual action space is a 6-way mutually exclusive choice, not a 10-way independent combination like this thesis's own design — the description was corrected to reflect that difference honestly, while keeping this thesis's own 10-action design unchanged.

---

## 2026-08-06 — Citation fix: Wangsun — methods.tex, Section 3.2.6
**Status:** ACTIVE

**BEFORE**

"The baseline empirical transit demand is perturbed each episode by a scaling factor clipped to [1, 3], following Wang and Sun. The upper bound of 3 corresponds to roughly a tripling of baseline boarding rates, spanning the range observed during major event let-outs and severe-weather mode shifts."

**AFTER**

"The baseline empirical transit demand is perturbed each episode by a scaling factor sampled from a normal distribution and clipped to [1, 3], **following the general Gaussian-clipped demand-scaling mechanism of Wang and Sun, though this study adopts a narrower clip than their [1, 10] range**. The asymmetric clip focuses the test on demand surges rather than symmetric variation, since demand drops produce lightly loaded conditions that do not stress-test the controller. The upper bound of 3, corresponding to roughly a tripling of baseline boarding rates, **is this study's own choice (flagged to revisit against Wang and Sun's wider range during implementation) rather than a value drawn from prior work**."

**Why:** checked against the actual paper. Their own equation clips the demand-scaling factor to [1, 10], not [1, 3] — and the "event let-outs" justification for the number 3 doesn't appear anywhere in their paper either. Kept the study's own [1, 3] choice, since changing it would be a real experimental redesign, not a citation fix, but stopped implying that specific number came from Wang and Sun.

---

## 2026-08-06 — E3C9 + E2C4 — introduction.tex, after Section 1.2.2 (SARL)
**Status:** SUPERSEDED — introduction.tex literature tables restructured in Texas pivot

**BEFORE**

"...which motivates the MARL choice here while acknowledging this caveat."

(Then jumped straight to the "Multi-Agent Reinforcement Learning" section — no ML/SARL disturbance table existed.)

**AFTER**

"...which motivates the MARL choice here while acknowledging this caveat.

**To situate the MARL literature reviewed in the next subsection within the broader ML and SARL landscape, this table extends the paradigm comparison of Table 1.1 with a disturbance-coverage column, using the same D/S/T/W/B notation as the main MARL comparison table.**"

**Disturbance coverage across ML and SARL vehicle-scheduling studies (new table):**

| Paper | Paradigm | Method | Disturbances |
|---|---|---|---|
| Wang et al. | ML (data-driven) | Bus scheduling incorporating time-dependent traffic and demand | D |
| Barrera Hernandez et al. | ML-assisted (heuristic dispatcher) | Passenger-demand forecasting supporting a heuristic dispatcher | D |
| Zhao et al. | SARL | STDH-DQN; self-attention state encoder over spatial-temporal AVL features | D, T |
| Zhang and Zheng | SARL | SA-DRL; categorical identity features | D, T |
| Verbich and El-Geneidy | Heuristic (non-MARL) | Dynamic transit control under severe weather and vehicle breakdowns | W, B |

"**The funnel is now complete: no ML or SARL study covers W or B, and among MARL studies, only Verbich and El-Geneidy's heuristic controller addresses both, and it's explicitly non-MARL. Patil et al. similarly validate weather-induced travel-time distributions but don't address bus control at all; their contribution here is the lognormal parameterization for the weather generator, not a bus-control baseline. No prior study, ML, SARL, or MARL, combines W and B coverage with an actual MARL bus-scheduling controller, which is the specific gap this study fills.**"

**Why:** RTC comment 9 (asks for an ML/SARL disturbance table) and comment 4 (asks for a severe-weather comparison study) — solved together, since Verbich & El-Geneidy is exactly what comment 4 wants and fits naturally as a row here.

---

## 2026-08-06 — E3C10 — introduction.tex, before Table 1.2 discussion
**Status:** SUPERSEDED — Table 1.2 discussion rewritten in Texas pivot

**BEFORE**

"Table 1.2 summarizes what each study evaluated, what disturbances it modeled, and what it reported."

**AFTER**

"**Only Shi et al. carries a breakdown (B) entry in Table 1.2. Cao et al., who also model discrete vehicle failures, are deliberately excluded from this count: their MARL application is to train rescheduling, not bus scheduling, so they don't belong in a table scoped to MARL bus-control literature. Verbich and El-Geneidy likewise model breakdowns but use heuristic, non-MARL control (see the ML/SARL table), so they're excluded for the same reason. Among MARL bus-scheduling studies specifically, Shi et al. remains the only one to model discrete breakdowns.** Table 1.2 summarizes what each study evaluated, what disturbances it modeled, and what it reported."

**Why:** RTC comment 10 — the table shows only one breakdown paper but the presentation reportedly showed two. Could not confirm what was actually shown, since there was no slide access at the time, so used the RTC letter's own suggested fallback: explain why the two "candidate" second papers are correctly excluded, rather than guessing at an unverified row.

---

## 2026-08-06 — E3C11 — figure caption attribution (introduction.tex, methods.tex)
**Status:** ACTIVE

**BEFORE** (example — Figure 1.3 caption)

"Comparison of single-agent and multi-agent formulations. (a) SARL: a centralized policy consumes the concatenated global state and outputs a joint action covering every bus. (b) MARL with parameter sharing: a single set of weights is shared across N agents, each acting on its own local observation o_i."

(Same pattern for Figures 1.4, 3.1–3.5 — captions ended with no source attribution.)

**AFTER** (example — Figure 1.3 caption)

"Comparison of single-agent and multi-agent formulations. (a) SARL: a centralized policy consumes the concatenated global state and outputs a joint action covering every bus. (b) MARL with parameter sharing: a single set of weights is shared across N agents, each acting on its own local observation o_i. **Authors' illustration.**"

(Same "Authors' illustration." appended to all 7 original diagram captions. Figures 1.1 and 1.2 already had proper citations and were unchanged.)

**Why:** RTC comment 11 — some figures lack citations; original diagrams should say so explicitly rather than looking uncredited.

---

## 2026-08-06 — E3C14 — problem.tex, Delimitations (a)
**Status:** SUPERSEDED — problem.tex Scope section fully rewritten for CapMetro in Texas pivot

**BEFORE**

"(a) Due to computational constraints, the simulation is restricted to a defined operational sub-segment of the EDSA Carousel corridor rather than the entire metropolitan road network. The restriction is justified by the need to preserve 1:1 empirical traffic volumes for GEH calibration without resorting to flow scaling; corresponding GEH calibration statistics are reported in Chapter 4."

**AFTER**

"(a) Due to computational constraints, the simulation is restricted to a defined operational sub-segment of the EDSA Carousel corridor rather than the entire metropolitan road network, **and minor feeder roads leading into the corridor are not modeled. Both restrictions are justified by the same structural fact: the EDSA Carousel operates on a physically separated, barrier-protected busway, so the agents' state and reward depend only on bus dynamics within the dedicated lane, specifically headways, dwell times, and onboard loads, none of which are directly observed by or computed from feeder-road traffic. Feeder roads affect the corridor only indirectly, through the passenger arrival rates they produce at each stop, and that effect is already captured by the calibrated per-stop demand distributions without needing to simulate the feeder network itself. Modeling feeder roads in SUMO would add computational cost without adding any new information the agents' observation or reward could use, since** the sub-corridor restriction also preserves 1:1 empirical traffic volumes for GEH calibration without resorting to flow scaling; corresponding GEH calibration statistics are reported in Chapter 4."

**Why:** RTC comment 14 — explain why minor roads leading to the corridor are excluded from the simulation.

---

## 2026-08-06 — E3C16 — figure/table callout sweep (introduction.tex, methods.tex)
**Status:** mixed — see per-callout breakdown below

| # | Location | Status |
|---|----------|--------|
| 1 | intro: ridership figure callout | SUPERSEDED (inside `\iffalse`) |
| 2 | intro: rainfall figure callout | SUPERSEDED (inside `\iffalse`) |
| 3 | intro: CTDE figure callout | ACTIVE |
| 4 | methods: pipeline figure callout | ACTIVE |
| 5 | methods: GEH panel (a) callout | ACTIVE |
| 6 | methods: RMSE panel (b) callout | ACTIVE |
| 7 | methods: parameter-table reference sentence | SUPERSEDED (replaced by shorter phrasing) |
| 8 | methods: observation-features table callout | ACTIVE |
| 9 | methods: training-loop figure callout | ACTIVE |
| 10 | methods: Stage A figure callout | SUPERSEDED (prose callout removed) |
| 11 | methods: Stage B figure callout | SUPERSEDED (prose callout removed) |

Ten short additions, each linking an existing sentence to a figure/table that was never explicitly named anywhere in the prose:

| Location | Before | After |
|---|---|---|
| Ridership stat (intro) | "up from 63.02M in 2024." | "up from 63.02M in 2024 **(Figure 1.1)**." |
| Rainfall stat (intro) | "The reduction in average speeds are about 5.34% under light rain conditions." | "**As Figure 1.2 shows,** the reduction in average speeds are about 5.34% under light rain conditions." |
| CTDE intro (intro) | "Most modern formulations use Centralized Training with Decentralized Execution (CTDE)." | "Most modern formulations use CTDE, **illustrated in Figure 1.4**." |
| Pipeline intro (methods) | "The pipeline proceeds in two phases." | "**As shown in Figure 3.1,** the pipeline proceeds in two phases." |
| GEH statistic (methods) | "It measures the discrepancy between simulated and observed hourly bus volumes on individual corridor segments." | "It measures the discrepancy between simulated and observed hourly bus volumes, **illustrated in panel (a) of Figure 3.2**." |
| RMSE (methods) | "RMSE evaluates how closely simulated bus speed trajectories match empirical observations." | "RMSE evaluates how closely simulated bus speed trajectories match empirical observations, **illustrated in panel (b) of Figure 3.2**." |
| Parameter table close (methods) | "Parameters marked TODO-VAL are to be confirmed during the implementation phase." | "**Table 3.2 therefore serves as the single reference point for every parameter used across this chapter.** Parameters marked TODO-VAL are to be confirmed during the implementation phase." |
| Observation features (methods) | "In simulation, all observation features are generated synthetically." | "**As Table 3.3 shows,** in simulation all observation features are generated synthetically." |
| Training loop (methods) | "The learning process follows the standard RL feedback loop." | "The learning process follows the standard RL feedback loop, **illustrated in Figure 3.3**." |
| Stage A (methods) | "They are each run for at least 30 Monte Carlo iterations with matched seeds." | "Matched seeds, **reported in the format shown in Figure 3.4**." |
| Stage B (methods) | "With the breakdown generator active at each level." | "Active at each level, **using the Monte Carlo evaluation procedure illustrated in Figure 3.5**." |

**Why:** RTC comment 16 — figures and tables should be called and discussed in the paragraphs, not just placed. Found 10 with zero references despite adjacent topical discussion; added one reference each without touching the discussion itself. Table 3.1, the notation table and the RTC's own example of a too-thin callout, was checked and already has 5 separate substantive references elsewhere in the chapter, so no fix was needed there.

---

## 2026-08-06 — E3C18 + E3C19 — main.tex preamble
**Status:** ACTIVE

This entry is a preamble-only change (no manuscript prose changed). See AUDIT_TRAIL.md for the exact LaTeX diff. In summary: added the setspace package, added onehalfspacing after begin-document, and uncommented the linenumbers command.

**Why:** RTC comments 18 and 19 — 1.5 line spacing and line numbers for the non-final manuscript. Applied last, after all other content edits in this revision round, per CLAUDE.md's own guidance to avoid disrupting line references mid-revision.

---

## 2026-08-06 — E1C2 — methods.tex, Section 3.2.5 (end)
**Status:** ACTIVE

**BEFORE**

"Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable, with disturbance magnitudes anchored to validated literature values rather than to a corridor-specific severe-weather sample."

(The required-datasets bullet list ended and went straight to this sentence — no mapping table existed.)

**AFTER**

"**Table 3.2 maps each required raw field to the parameter derived from it and the MARL component that parameter feeds into, connecting the data requirements above to the disturbance generators, the control-stop selection criteria, and the agent observation vector. The mapping reflects the study's design intent, not properties of a processed dataset; specific statistics remain TODO-DATA pending dataset acquisition.**

| Raw Field | Derived Parameter | MARL Component |
|---|---|---|
| GPS-tracked vehicle location | Per-segment travel-time distribution | SUMO speed calibration; anchors traffic-speed and weather generators |
| Boarding events | Per-stop demand rate | Demand-surge generator baseline; waiting-count observation feature |
| Alighting events | Through-passenger volume per stop | Control-stop selection criterion 3 (avoid high through-volume stops) |
| Passenger occupancy | Per-segment load profile | Onboard-count observation feature; dwell-time estimation |
| Operating speed | Per-segment cruising speed | SUMO volume calibration; traffic-speed generator baseline |
| Dwell time | Per-stop dwell distribution | Event-driven bus model, advances the simulation clock |

"Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable, with disturbance magnitudes anchored to validated literature values rather than to a corridor-specific severe-weather sample."

**Bug caught while drafting:** one of the new cross-references initially pointed at the wrong section — the data pre-processing pipeline instead of control-stop selection, which didn't have a label yet. Added the missing label and fixed both references before finalizing.

**Why:** RTC comment 2 — map dataset fields to the study's proposed features. Judged safe without dataset access, since it connects two things already spelled out elsewhere in the manuscript (required fields, MARL components) rather than describing the dataset itself.

---

## 2026-08-06 — E3C17 — introduction.tex (Background), methods.tex (Weather-Induced Anomalies)
**Status:** mixed — see per-addition breakdown below

| # | Addition | Status |
|---|----------|--------|
| 1 | intro: EDSA corridor map figure | SUPERSEDED (inside `\iffalse`) |
| 2 | methods: η-sweep basis table (tab:eta-basis) | ACTIVE |

**Addition 1 — introduction.tex: corridor map figure (SUPERSEDED)**

**BEFORE:** "Despite the gradual increase in demand, the EDSA Bus Carousel still faces a lot of significant operational issues that affect the quality of bus routing."

(No corridor map figure existed between the ridership figure and this sentence.)

**AFTER:** "**Figure 1.3 shows the EDSA Carousel Southbound route from Monumento to PITX, the corridor this study is grounded in, together with the other public transport modes (jeepney, MRT, LRT, tricycle, UV/FX) that intersect it at each major stop.** [corridor map image, captioned: EDSA Carousel Southbound route (Monumento to PITX) with intersecting public transport modes at each stop. Authors' illustration, adapted from the group's defense presentation.] Despite the gradual increase in demand, the EDSA Bus Carousel still faces a lot of significant operational issues that affect the quality of bus routing."

**Addition 2 — methods.tex: η-sweep basis table (ACTIVE)**

**BEFORE:** "The synthetic factor is swept over η in {0.0, 0.3, 0.6, 1.0, 1.3}. Values through 1.0 span the range evaluated by Patil et al.; 1.3 is a deliberate extrapolation. None is assigned a rain-rate label. Observed ordinary-rain experiments are reported by their NOAA exposure definition rather than by η. The mapping from η to named weather severity is not established."

(The η sweep values were explained in prose only — no summary table.)

**AFTER:** "The synthetic factor is swept over η in {0.0, 0.3, 0.6, 1.0, 1.3}. Values through 1.0 span the range evaluated by Patil et al.; 1.3 is a deliberate extrapolation. None is assigned a rain-rate label. Observed ordinary-rain experiments are reported by their NOAA exposure definition rather than by η.

**Basis for each synthetic weather-stress intensity value (new table inserted here):**

| η | Basis |
|---|---|
| 0.0 | Synthetic factor off; empirical T remains active |
| 0.3 | Within the published CV range; synthetic variability stress |
| 0.6 | Within the published CV span; synthetic variability stress |
| 1.0 | Upper end of the published CV range; synthetic severe stress |
| 1.3 | Beyond the published range; deliberate extreme extrapolation |

The mapping from η to named weather severity is not established."

**Why:** RTC comment 17 — include figures/tables shown in the defense but missing from the manuscript. All 58 slides of the defense deck were reviewed against the manuscript; most content (SARL vs MARL, CTDE, calibration formulas, parameter notation, training-vs-execution protocol) duplicated what's already written — adding it again would just repeat existing material. These two were the genuinely new items. The corridor map specifically matches the example the RTC letter itself gave for what might be missing.

**Judged out of scope, not added:** Work Plan Gantt charts (project timeline, not manuscript content) and a software/tools appendix (SUMO, PettingZoo, PyTorch, and so on — implementation detail for later, not this revision round).

**Important:** this repo doesn't have a `Figures/` folder for any of the existing images — they live only on Overleaf. A `Figures/` folder was created locally just to hold the new map image. The user needs to upload `bg_fig3_edsa_corridor_map.pdf` to Overleaf's Figures folder too, or the new figure won't show up when compiled there.

---

## 2026-08-06 — N2 (self-identified, not RTC) — problem.tex, Section 2.3 (Significance)
**Status:** SUPERSEDED — problem.tex Significance section fully rewritten for CapMetro in Texas pivot

**BEFORE**

"This study contributes both practical and scientific significance."

**AFTER**

"This study contributes both practical and scientific significance. **MARL is the control method under evaluation in this study; the corridor's service reliability under disturbance is the object of study it is applied to measure, which is why practical significance is discussed first.**"

**Why:** self-identified, prompted by the user's recollection that a panelist questioned during Q&A whether the study reads as more focused on MARL than on bus scheduling. This isn't in the official RTC decision letter's 22 written items, so it's treated as an oral/impression-level concern rather than a formal requirement. States the thesis's own positioning explicitly instead of leaving readers to infer it from section ordering.

**Note:** since this isn't an RTC panel comment, it doesn't get a row in the conformity-of-revisions table.

---

## 2026-08-06 — N2 (self-identified, not RTC) — problem.tex, Section 2.2 (Research Gap)
**Status:** SUPERSEDED — problem.tex Research Gap section fully rewritten for CapMetro in Texas pivot

**BEFORE**

"Without this characterization, it cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment."

**AFTER**

"Without this characterization, it cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment. **This joint-disturbance framing reflects two independently-documented, concurrent operational realities of the same corridor rather than only a gap in existing comparison tables: EDSA experiences both weather-driven service disruptions (Mangaluz, 2024; PIA emergency-response reporting) and chronic mechanical-failure risk (Chua, 2026) as ongoing features of its operating environment, so a controller validated against each in isolation provides no evidence of how it behaves when a transit operator's actual risk exposure includes both at once. The disturbance generators remain independently sampled within the simulation (Section 3.2.6); this operational context motivates evaluating their union, not a claim that the two are causally or temporally linked.**"

**Why:** self-identified. Grounds the "combined disturbance" framing in a real, citable fact about EDSA's operating environment rather than presenting the combination as valuable only because no prior comparison table has filled that cell. Also explicitly reaffirms that the disturbance generators remain independently sampled (established earlier in the methods chapter), so this addition doesn't contradict that existing design choice.

**Citation check performed first:** an earlier draft tried to claim breakdowns and weather delays cluster in the same wet-season months, citing a DPWH road-repair-closure article and a single flooding article. Checked both sources before writing anything into the manuscript: the road-repair article is about infrastructure closures, not documented bus breakdowns, and doesn't establish a weather cause; the flooding article is one dated event, not evidence of a recurring seasonal pattern. Neither supported the clustering claim, so it was dropped in favor of the weaker but fully-supported "two documented, concurrent risks" framing actually used above.

**Note:** since this isn't an RTC panel comment, it doesn't get a row in the conformity-of-revisions table.

---

## 2026-08-06 — N1 (self-identified, not RTC) — methods.tex, Section 3.2.7
**Status:** ACTIVE

**BEFORE**

"This study defines the reward structure for the hybrid action space, the three component terms above, and treats their relative weighting, plus a sensitivity analysis over those weights, as the implementation-phase deliverable (EO 2.1). The component structure is fixed; the coefficients are not yet finalized."

**AFTER**

"This study defines the reward structure for the hybrid action space, the three component terms above, and treats their relative weighting, plus a sensitivity analysis over those weights, as the implementation-phase deliverable (EO 2.1). The component structure is fixed; the coefficients are not yet finalized. **The reward is computed individually for each agent at every control event, not as a shared team-level signal: r_i,t is agent i's own entry in the transition tuple written to the shared replay buffer, so each bus is scored on the consequences of its own action even though all agents update the same shared network. Locally-observable quantities already in the agent's local observation, principally the forward and backward headway components, let this individual signal still reflect corridor-wide regularity without requiring a centralized reward computation at execution time. The three priorities combine additively as a weighted sum of per-event penalty terms:**

**r(i, t+k) = −w₁ · (headway-irregularity term) − w₂ · (waiting-time term) − w₃ · (skip-degeneracy term)**

**with weights w₁, w₂, w₃ left as placeholders to be tuned as the Expected Output 2.1 sensitivity analysis. Each term is expressed as a non-positive penalty, so the agent maximizes its expected return by simultaneously minimizing headway irregularity, passenger waiting, and degenerate skipping; this sign convention, not the specific per-term formulas or their relative weights, is what this chapter fixes ahead of implementation.**"

**Why:** self-identified gap, not an RTC comment. The existing text explained the reward's *priorities* and said the *weighting* is deferred to implementation, but never said whether the reward is individual or shared, how the priorities combine into one number, or the sign convention. Added those three things without touching the existing structure/weighting distinction or specifying any coefficient value.

**Note:** since this isn't an RTC panel comment, it doesn't get a row in the conformity-of-revisions table.

---

## 2026-08-06 — N1 rewrite (user-provided prose) — methods.tex, Section 3.2.7
**Status:** ACTIVE

**BEFORE**

"This study defines the reward structure for the hybrid action space, the three component terms above, and treats their relative weighting, plus a sensitivity analysis over those weights, as the implementation-phase deliverable (EO 2.1). The component structure is fixed; the coefficients are not yet finalized. The reward is computed individually for each agent at every control event, not as a shared team-level signal: r_i,t is agent i's own entry in the transition tuple written to the shared replay buffer, so each bus is scored on the consequences of its own action even though all agents update the same shared network. Locally-observable quantities already in the agent's observation, principally the forward and backward headway components, let this individual signal still reflect corridor-wide regularity without requiring a centralized reward computation at execution time. The three priorities combine additively as a weighted sum of per-event penalty terms: [equation] with weights left as placeholders to be tuned as the Expected Output 2.1 sensitivity analysis. Each term is expressed as a non-positive penalty, so the agent maximizes its expected return by simultaneously minimizing headway irregularity, passenger waiting, and degenerate skipping; this sign convention, not the specific per-term formulas or their relative weights, is what this chapter fixes ahead of implementation."

**AFTER**

**"This study establishes the overall reward structure for the hybrid action space by defining the three reward components and their additive formulation, while treating the corresponding weighting coefficients, together with their sensitivity analysis, as the implementation-phase deliverable under Expected Output 2.1. Although the component structure is fixed at this stage, the coefficients remain as placeholders to be determined during implementation through experimental evaluation.**

**The reward is computed independently for each agent at every control event rather than as a shared team-level objective. Accordingly, r_i,t represents the reward assigned to agent i and is stored as that agent's transition in the shared replay buffer. Each bus is therefore evaluated based on the consequences of its own action, even though all agents learn from a common shared network. Since the reward is derived from locally observable quantities already contained in the agent's observation, particularly the forward and backward headway measurements, the resulting signal remains aligned with corridor-wide service regularity without requiring a centralized reward computation during execution.**

**The overall reward function is expressed as the weighted sum of three penalty terms:** [same equation as before, unchanged] **where w₁, w₂, and w₃ denote the weighting coefficients to be determined through the Expected Output 2.1 sensitivity analysis. Each component is formulated as a non-positive penalty, allowing the agent to maximize its cumulative return by minimizing headway irregularity, passenger waiting time, and unnecessary stop-skipping behavior. Consequently, this chapter establishes the reward formulation and its optimization objective, while the specific mathematical expressions and coefficient values are reserved for the implementation and evaluation phase.**"

**Why:** the user supplied polished replacement prose for the N1 addition and asked that it be applied directly. The equation itself is unchanged — only the surrounding explanatory prose was rewritten, folding the "additive formulation" idea earlier into the structure paragraph and restating the mechanics/sign-convention explanation in the user's own words. The TODO-VAL placeholder tag on the coefficients was kept even though the user's text didn't include it, since CLAUDE.md's convention requires it so unresolved values stay greppable.

---

## 2026-08-24 — Texas CapMetro pivot + E1C1/E2C5/E4C22 — all major .tex files
**Status:** ACTIVE

This entry covers the full adoption of Jared's Texas CapMetro rewrite (from his `dataset/texas-capmetro-801` branch, audited and verified before merge). EDSA-focused versions are preserved in `EDSA Ver/`. The changes below highlight the dataset-description content that directly answers E1C1/E2C5/E4C22; the full file diffs are in commit `aff79b0`.

### methods.tex — Required Datasets (Section 3.2.5)

**BEFORE**

Corridor bus operational data. A per-trip record of EDSA Carousel bus operation along the study sub-corridor, collected over a continuous observation window of at least two weeks. The required fields are GPS-tracked vehicle location, boarding and alighting events, passenger occupancy, operating speed, and dwell time at each stop. The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application.

**AFTER**

**Corridor operational data (primary).** The primary dataset is the Capital Metropolitan Transportation Authority (CapMetro) Automatic Passenger Counter (APC) raw archive for **July–December 2021** (Texas Open Data Portal, Socrata dataset ID im6q-3pc9). The archive contains **9,197,694 stop-level event records across 47 columns**. Each record is a single bus stop visit with: calendar fields, route and trip identifiers, stop spatial data (bs_id, stop_sequence, GPS), passenger activity (ons, offs, load, max_load), temporal measurements (departure_dtm), vehicle identifiers, and quality flags (import_error, import_trip_error).

**Weather data (secondary).** NOAA Local Climatological Data Version 2, Camp Mabry station (USW00013958), same July–December 2021 period. Joined to APC records by nearest-hour timestamp.

**Vehicle fleet data (supplementary).** 2021 NTD Revenue Vehicle Inventory (NTD ID 60048) for per-vehicle capacity confirmation.

### methods.tex — Data Pre-Processing Pipeline (Section 3.2.5)

**BEFORE**

Pre-processing proceeds in three stages. Stage 1: Cleaning — trip records with missing GPS coordinates, missing timestamps, negative inter-stop times, or trips that fail integrity checks are dropped. Records filtered to regular weekdays and binned by time-of-day. Stage 2: Empirical distribution extraction. Stage 3: Train/validation split for calibration.

**AFTER**

Pre-processing proceeds in four stages. **Stage 1: Filtering and validation** — the raw APC archive is filtered using four sequential rules: (1) route consistency (current_route_id equals route_id); (2) import-error exclusion (import_error = 0 and import_trip_error = 0); (3) valid stop identification (bs_id ≠ 0); and (4) direction selection (direction_code_id = 6). These filters reduce the archive from 9,197,694 to 229,421 records. Output integrity verified via SHA-256 checksum. **Stage 2: Temporal and weather join** — cleaned records joined to NOAA hourly weather by rounding departure timestamp to nearest hour. Stage 3: Empirical distribution extraction (unchanged). Stage 4: Train/validation split (unchanged, renumbered).

### problem.tex — full rewrite for CapMetro

**BEFORE**

The public transportation system has long been a commodity that comes in the form of bus transport, train networks, and the like, with predetermined routes and fares. In Metro Manila, traffic congestion has long been a problem stemming from insufficient road infrastructure and poor traffic mitigation policies, resulting in an inefficient public transport system. One of the government's actions for an alternative transportation system that runs within the metropolitan area is the implementation of the EDSA Carousel in 2020.

**AFTER**

**High-frequency bus operation is a sequential control problem: a holding or stop-skipping decision changes the headways, queues, loads, and downstream dwell times encountered by later buses.** Fixed timetables cannot adapt after these quantities depart from their planned values. **The empirical case is CapMetro Rapid Route 801 in Austin, Texas.** CapMetro's public APC dataset covers July–December 2021 and contains event timestamps, route and direction codes, stop IDs, boarding and alighting counts, onboard load, dwell time, revenue travel time and distance, event coordinates, and quality indicators. **The one-direction study subset uses direction code 6 and contains 229,421 clean stop events, 184 service-day codes, and 29 distinct stop IDs.**

**Why:** E1C1 ("Update manuscript with proposed setup and discussion of dataset"), E2C5 ("Explain what the dataset looks like"), E4C22 ("Describe dataset contents explicitly") — all three previously blocked on dataset access. Dataset now verified locally (229,421 clean rows, SHA-256 confirmed). The broader EDSA-to-CapMetro pivot was done on Jared's branch and adopted after a full audit.

---

## 2026-08-24 — REWRITE of E3C8 — methods.tex, Section 3.2.6
**Status:** ACTIVE

**BEFORE**

"This study distinguishes five disturbance classes, denoted D, S, T, W, and B:

- **Stochastic demand (D):** the baseline, always-present day-to-day randomness in passenger arrivals, drawn from the calibrated per-(stop, time-of-day) demand distributions. D is not a disturbance layered on top of a deterministic baseline; it IS the baseline stochastic environment, present in every run regardless of which other generators are active.
- **Demand surge (S):** an episode-level multiplicative scaling factor, with standard deviation σ_d, that amplifies baseline boarding rates above their empirical mean. S is the controlled experimental variable; D is always present, and S is what is added on top of it. Setting σ_d = 0 removes the surge and leaves only baseline demand variability (D).
- Ordinary travel-time variation (T) and Weather-induced delay (W) definitions — unchanged by this rewrite, see current methods.tex.
- **Discrete bus breakdown (B):** a Poisson-distributed discrete event, with rate λ, that permanently removes one bus from the active agent set for the remainder of the simulated day.

The generators that produce S, W, and B are sampled independently conditional on the always-active D and T baselines: no causal chain links them within the simulation. A breakdown does not trigger a demand surge or weather delay, and weather does not induce a mechanical failure. This factorial choice supports attribution in the single-disturbance ablations; it is not a claim that real disturbances are causally independent."

**AFTER**

"This study distinguishes five disturbance classes, denoted D, S, T, W, and B:

- **Stochastic demand (D):** **represents the normal day-to-day variation in passenger arrivals. Passenger demand is sampled from calibrated distributions for each stop and time of day. Unlike the other disturbances, D is always active and serves as the baseline demand condition of the simulation rather than an additional disturbance applied to a fixed demand profile.**
- **Demand surge (S):** **represents an increase in passenger demand by scaling the baseline boarding rates for a given episode, with standard deviation σ_d. In this case, D remains active as the baseline demand variation, while S introduces an additional increase in demand. Setting σ_d = 0 removes the surge and leaves only the baseline stochastic demand represented by D.**
- Ordinary travel-time variation (T) and Weather-induced delay (W) definitions — unchanged by this rewrite (kept as-is; they reflect the current CapMetro composition design, not the older wording this rewrite was drafted against — see Why below).
- **Discrete bus breakdown (B):** **represents the occurrence of bus breakdowns during operation. Breakdowns are modeled as discrete events following a Poisson distribution with rate λ. Once a bus breaks down, it is removed from the active fleet for the remainder of the simulated day.**

**The generators for S, W, and B are sampled independently while D and T serve as the baseline conditions. Therefore, one disturbance does not directly trigger another within the simulation: a bus breakdown does not cause a demand surge or weather delay, and weather conditions do not cause a bus breakdown. This setup allows the individual effect of each disturbance to be evaluated more clearly during the single-disturbance ablation experiments. However, this assumption is only used for the simulation design and does not imply that these disturbances are necessarily independent in real-world operations.**"

**Why:** user-supplied writing-style rewrite of the E3C8 addition (2026-08-06). The user's original draft also reworded the T and W bullets, but those used the older EDSA-era definitions (T = simple speed scaling; W replaces T), which conflict with the current CapMetro methods.tex design where T is an empirical rev_seconds distribution and W composes with T rather than replacing it (per the composition equation T_W = T_0 · m(w) · F_W already in the manuscript). Per the user's decision, only the D, S, B bullets and the closing independence paragraph were rewritten; T and W were left untouched to avoid introducing an internal contradiction with the existing composition design.

---

## 2026-08-24 — REWRITE of citation fix: Rodriguez2023Cooperative — methods.tex, Section 3.2.7
**Status:** ACTIVE

**BEFORE**

"This study's action space (10 discrete actions: 5 holding strengths times 2 skip choices, selected independently) is broader than Rodriguez et al.'s combined holding-and-skipping controller, which instead selects among 6 mutually exclusive actions: 5 holding strengths, where zero-strength already covers 'no holding,' plus a single separate skip action. The same 5-value holding-strength set is used in both studies. A continuous holding parameter was considered but rejected for two reasons: continuous actions require actor-critic algorithms with training instability, and real driver compliance with holding instructions is itself imperfect — Rodriguez et al. model non-compliant drivers as executing only 60-80% of the instructed holding time — so continuous precision isn't meaningful at deployment anyway."

**AFTER**

"**This study uses an action space consisting of 10 discrete actions, combining five holding strengths with two skip choices that can be selected independently. This provides a broader action space compared with the combined holding-and-skipping controller used by Rodriguez et al., which consists of six mutually exclusive actions: five holding strengths, where zero holding already represents the option of not holding, and one separate skip action. Both studies use the same five-value set for holding strength.**

**A continuous holding parameter was considered but was not used for two main reasons. First, continuous actions generally require actor-critic algorithms, which can introduce additional training instability. Second, continuous precision is not necessarily meaningful during actual deployment because driver compliance with holding instructions is imperfect. Rodriguez et al. account for this by modeling non-compliant drivers as executing only 60–80% of the instructed holding time. Therefore, using a continuous holding value would provide a level of control precision that may not be reliably achieved in practice.**"

**Why:** user-supplied writing-style rewrite of the Rodriguez2023Cooperative citation fix (2026-08-06). Content verified compatible with the current live text — no new claims, same 60-80% compliance figure, same 5-value holding set — so applied as-is, split into two paragraphs per the user's structure.

---

## 2026-08-24 — REWRITE of citation fix: Wangsun — methods.tex, Section 3.2.6
**Status:** ACTIVE

**BEFORE**

"The baseline empirical transit demand is perturbed each episode by a scaling factor sampled from a normal distribution and clipped to [1, 3], following the general Gaussian-clipped demand-scaling mechanism of Wang and Sun, though this study adopts a narrower clip than their [1, 10] range. The asymmetric clip focuses the test on demand surges rather than symmetric variation, since demand drops produce lightly loaded conditions that do not stress-test the controller. The upper bound of 3, corresponding to roughly a tripling of baseline boarding rates, is this study's own choice (flagged to revisit against Wang and Sun's wider range during implementation) rather than a value drawn from prior work."

**AFTER**

"**The baseline empirical transit demand is adjusted at each episode using a scaling factor sampled from a normal distribution and clipped to [1, 3]. This follows the general Gaussian-clipped demand-scaling approach used by Wang and Sun, but this study uses a narrower range than their [1, 10] setting. The asymmetric range focuses the experiments on demand surges rather than demand reductions, since lower demand mainly produces lightly loaded conditions and does not provide the same level of stress on the controller. The upper bound of 3, which allows the baseline boarding rate to increase by roughly three times, is a choice specific to this study (flagged to revisit against Wang and Sun's wider range during implementation) rather than a value directly adopted from prior work.**"

**Why:** user-supplied writing-style rewrite of the Wangsun citation fix (2026-08-06). The user's draft included a closing clause ("and should be revisited during implementation against the wider range used by Wang and Sun") that duplicated the TODO-VAL placeholder tag's own wording; merged into one clause to avoid saying the same thing twice, keeping the TODO-VAL tag itself per CLAUDE.md's placeholder convention. The paragraph's trailing sentences ("Sampling occurs at the start of each simulation run..." and the E4C20 implementation-mechanics sentence) are unaffected by this rewrite and remain unchanged.

---

## 2026-08-24 — REWRITE #2 of N1 — methods.tex, Section 3.2.7
**Status:** ACTIVE

**BEFORE**

"This study establishes the overall reward structure for the hybrid action space by defining the three reward components and their additive formulation, while treating the corresponding weighting coefficients, together with their sensitivity analysis, as the implementation-phase deliverable under Expected Output 2.1. Although the component structure is fixed at this stage, the coefficients remain as placeholders to be determined during implementation through experimental evaluation.

The reward is computed independently for each agent at every control event rather than as a shared team-level objective. Accordingly, r_i,t represents the reward assigned to agent i and is stored as that agent's transition in the shared replay buffer. Each bus is therefore evaluated based on the consequences of its own action, even though all agents learn from a common shared network. Since the reward is derived from locally observable quantities already contained in the agent's observation, particularly the forward and backward headway measurements, the resulting signal remains aligned with corridor-wide service regularity without requiring a centralized reward computation during execution.

The overall reward function is expressed as the weighted sum of three penalty terms:

r(i,t+k) = −w₁ · (headway-irregularity term) − w₂ · (waiting-time term) − w₃ · (skip-degeneracy term)

where w₁, w₂, and w₃ denote the weighting coefficients (TODO-VAL) to be determined through the Expected Output 2.1 sensitivity analysis. Each component is formulated as a non-positive penalty, allowing the agent to maximize its cumulative return by minimizing headway irregularity, passenger waiting time, and unnecessary stop-skipping behavior. Consequently, this chapter establishes the reward formulation and its optimization objective, while the specific mathematical expressions and coefficient values are reserved for the implementation and evaluation phase."

**AFTER**

"**This study defines the reward structure for the hybrid action space using the three component terms described above. The overall structure of the reward is fixed, while the relative weights of the three components, together with their sensitivity analysis, will be finalized during the implementation phase as part of Expected Output 2.1. The coefficients are therefore treated as placeholders at this stage.**

**The reward is computed individually for each agent at every control event rather than using a shared team-level reward. The value r_i,t represents the reward assigned to agent i in the transition tuple stored in the shared replay buffer. This means that each bus is evaluated based on the consequences of its own action, even though all agents use the same shared network for learning. Since the agents already observe locally available quantities, particularly the forward and backward headway components, the individual reward can still capture the effects of an agent's action on corridor-wide regularity without requiring a centralized reward calculation during execution.**

**The three priorities are combined as a weighted sum of per-event penalty terms:**

r(i,t+k) = −w₁ · (headway-irregularity term) − w₂ · (waiting-time term) − w₃ · (skip-degeneracy term)

**The weights w₁, w₂, and w₃ are left as placeholders (TODO-VAL) and will be tuned through the Expected Output 2.1 sensitivity analysis. Each component is expressed as a non-positive penalty, allowing the agent to maximize its expected return by minimizing headway irregularity, passenger waiting time, and excessive or degenerate skipping. Therefore, what is fixed in this chapter is the overall reward structure and its sign convention, while the specific component formulas and relative weights will be finalized during implementation.**"

**Why:** user-supplied second-pass writing-style rewrite of the reward-function mechanics text (originally N1, self-identified not RTC; first rewritten 2026-08-06). The equation itself is unchanged. The TODO-VAL placeholder tag was kept on the weights sentence per CLAUDE.md's convention, though the user's draft didn't include it explicitly.

---

*Nothing follows.*
