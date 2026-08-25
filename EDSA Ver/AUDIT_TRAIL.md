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
#
# NOTE ON STATUS TAGS BELOW: the entries dated 2026-08-06 were originally
# written for the root-level audit trail, where many are tagged SUPERSEDED
# because the 2026-08-24 Texas pivot later overwrote them. In THIS folder
# (EDSA Ver/), that pivot never happened, so every one of these 2026-08-06
# revisions has been individually re-verified against the actual EDSA Ver
# .tex files and is tagged ACTIVE here. Commit hashes are shared history
# with the root repo (both trees descend from the same commits up to the
# pivot) and are kept for traceability.

---

## 2026-08-06 — E1C3 — problem.tex, Section 2.2 (Research Gap)
**Status:** ACTIVE (verified present in EDSA Ver/problem.tex)
**Commit:** `34017d3`

```diff
  Without this characterization, it cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment.
+
+ The weather-disturbance class (W) in particular was identified through the literature survey conducted earlier in this study (Section~\ref{subsec:marl-applied}), which found that no prior MARL bus-scheduling paper models heavy-tailed weather-induced travel-time delays (Table~\ref{tab:marl_performance}, column W). Its operational relevance to the EDSA corridor is established by the rainfall-driven reductions in average speed and free-flow capacity documented in Section~1.1 \cite{TSSP_Rain2018} and by the typhoon-related service suspensions recorded for the corridor \cite{DOTr2020Suspension}. The lognormal parameterization adopted for this disturbance class follows the Kolmogorov--Smirnov-validated form of Patil et al.~\cite{Patil2025Conformal}, introduced in this study to address the resulting lack of temporally aligned, corridor-specific anomaly data (Section~\ref{subsec:disturbance-gap}).
```

**Why:** RTC comment 3 — research gap should include how the weather disturbance column was arrived at.

---

## 2026-08-06 — E2C6 — introduction.tex 1.2.1, methods.tex Baseline Controllers
**Status:** ACTIVE (verified present in EDSA Ver)
**Commit:** `34017d3`

```diff
  ...allowing small headway perturbations to amplify into bunching \cite{Daganzo2009}. Static schedules therefore remain mathematically inadequate for stochastic traffic environments, where the governing quantities are random variables rather than deterministic constants.
+ Under the specific non-ideal conditions this study targets, the failure modes differ by control strategy. A fixed timetable has no feedback mechanism at all, so once bunching begins nothing in the schedule corrects it. A local reactive rule that holds a bus based only on the gap to the bus ahead can partially correct bunching under ordinary congestion, but has no way to respond to a breakdown, since it observes only the forward gap and not the enlarged gap a failed bus leaves behind it. A more globally aware reactive rule that accounts for both the forward and backward gap improves on this, but still follows a fixed, pre-specified rule rather than a learned response, so it cannot adapt its behavior to the heavier-tailed delays that severe weather introduces.
  These limitations motivated the transition toward more adaptive and data-driven scheduling methodologies.
```

```diff
  (methods.tex, No Control subsection, excerpt)
  ...NC also provides the reference point for measuring the severity of bus bunching.
+ Under non-ideal conditions, NC has no corrective mechanism whatsoever, so demand surges, weather-induced delays, and breakdowns are expected to compound directly into bunching with no attenuation.
```

(Equivalent one-sentence additions were made to the Forward Headway and Even Headway subsections, describing their own expected failure modes — FH: can't observe the backward gap a breakdown creates; EH: no mechanism to anticipate weather's heavy tails.)

**Why:** RTC comment 6 — expound on how traditional non-AI scheduling performs under bunching/weather/breakdowns.

---

## 2026-08-06 — E2C7 — methods.tex, Section 3.2.10
**Status:** ACTIVE
**Commit:** `34017d3`

```diff
- \textbf{Stage A: Ideal-condition evaluation.} ...The acceptance criterion is twofold: (i) mean passenger waiting time no worse than EH (no statistically significant degradation at $p < 0.05$ with multiple-comparison correction), and ideally a statistically significant improvement; and (ii) a statistically significant reduction in headway coefficient of variation relative to NC. Under ideal conditions EH is already near-optimal...
+ \textbf{Stage A: Ideal-condition evaluation.} ...Under ideal conditions EH is already near-optimal, so parity with EH is an acceptable Stage A outcome. Outperforming EH is the target but not required to pass Stage A...
+
+ \paragraph{Stage A acceptance criterion}
+ \begin{itemize}
+ \item[(i)] Mean passenger waiting time no worse than EH (no statistically significant degradation at $p < 0.05$ with multiple-comparison correction), and ideally a statistically significant improvement.
+ \item[(ii)] A statistically significant reduction in headway coefficient of variation relative to NC.
+ \end{itemize}
```
(Stage B's criterion sentence was similarly pulled into a `\paragraph{Stage B acceptance criterion}` callout, unchanged in substance.)

**Why:** RTC comment 7 — describe what successful performance will look like, more visually prominent.

---

## 2026-08-06 — E3C12 — introduction.tex, Section 1.2.3 (after Figure 1.3)
**Status:** ACTIVE
**Commit:** `34017d3`

```diff
      \label{fig:sarl-vs-marl}
  \end{figure}
+
+ In both panels of Figure~\ref{fig:sarl-vs-marl}, the per-bus state (denoted $s_{i,t}$ in the formal MDP notation of Section~\ref{subsec:state-space}, and shown in the figure as the local observation $o_i$) encodes the bus's current position, forward and backward headways, onboard load, and queue length at its current stop, as defined in full in Section~\ref{subsec:state-space}. The action $a_{i,t}$ is the holding-strength and stop-skipping decision the controller emits for that bus, defined in Section~\ref{subsec:action-space}. In the SARL panel (a), a single centralized network ingests all $N$ per-bus state vectors concatenated into one global state $s \in \mathbb{R}^{N \cdot d}$ and outputs all $N$ actions simultaneously; in the MARL panel (b), the same shared network weights $\theta$ instead process each bus's local state independently, so each agent acts on only its own observation rather than the concatenated global one.
+
  Multi-Agent Reinforcement Learning (MARL) addresses the three limitations above
```

**Why:** RTC comment 12 — explain the concepts in Figure 1.3 (bus states and actions).

---

## 2026-08-06 — E3C13 — introduction.tex Section 1.1, methods.tex Section 3.2.3
**Status:** ACTIVE
**Commit:** `34017d3`

```diff
  (introduction.tex)
- ...empirical studies on Philippine expressways show that increasing rainfall intensity significantly reduces average traffic speed and free-flow capacity \cite{TSSP_Rain2018}.
+ ...empirical studies on Philippine expressways show that increasing rainfall intensity significantly reduces average traffic speed and free-flow capacity \cite{TSSP_Rain2018}. This rainfall-impact evidence is drawn from a 2018 study of the North Luzon Expressway rather than the EDSA Busway, and is used here only as contextual motivation that weather materially affects Philippine road-traffic operations; the weather-disturbance generator in this study (Section~3.2.6) does not adopt this study's specific speed-reduction percentages, and EDSA-specific travel-time behavior is independently calibrated through the GEH/RMSE procedure described in Section~3.2.3.
```

```diff
  (methods.tex, Environment Model Validation opening)
- ...The calibration is restricted to the bus corridor itself, since the agents' state and reward depend only on bus dynamics; surrounding mixed-traffic flows do not enter the Python environment.
+ ...The calibration is restricted to the bus corridor itself, since the agents' state and reward depend only on bus dynamics; surrounding mixed-traffic flows do not enter the Python environment. This GEH/RMSE procedure calibrates EDSA-specific parameters directly from EDSA operational data and does not depend on the North Luzon Expressway rainfall-impact figures cited as motivating evidence in Section~1.1 \cite{TSSP_Rain2018}; that citation establishes only that weather materially affects Philippine road-traffic operations in general, not any EDSA-specific speed or capacity value used in this calibration.
```

**Why:** RTC comment 13 — Reference [10] is both dated (2018) and a different corridor (North Luzon Expressway); clarify whether adopted or independently tuned for EDSA.

---

## 2026-08-06 — E3C8 — methods.tex, Section 3.2.6
**Status:** ACTIVE — including the original "W replaces T" design (EDSA Ver never received the Texas-pivot's "W composes with T" redesign)
**Commit:** `01c49bf`

```diff
  \subsection{Stochastic Disturbance Generators}
  \label{subsec:stochastic-vars}

+ \paragraph{Disturbance Classes and Independence}
+
+ This study distinguishes five disturbance classes, denoted D, S, T, W, and B:
+
+ \begin{itemize}
+ \item \textbf{Stochastic demand (D):} the baseline, always-present day-to-day randomness in passenger arrivals, drawn from the calibrated per-(stop, time-of-day) demand distributions (Section~\ref{subsec:data-pipeline}). D is not a disturbance layered on top of a deterministic baseline; it \textit{is} the baseline stochastic environment, present in every run regardless of which other generators are active.
+ \item \textbf{Demand surge (S):} an episode-level multiplicative scaling factor, with standard deviation $\sigma_d$ (Table~\ref{tab:notation}), that amplifies baseline boarding rates above their empirical mean. S is the controlled experimental variable; D is always present, and S is what is added on top of it. Setting $\sigma_d = 0$ removes the surge and leaves only baseline demand variability (D).
+ \item \textbf{Traffic-speed perturbation (T):} an episode-level scaling of corridor cruising speed, with standard deviation $\sigma_s$, representing everyday congestion friction. T governs inter-stop travel-time variability under ideal conditions.
+ \item \textbf{Weather-induced delay (W):} a per-segment travel-time distribution with coefficient of variation $\eta$, drawn from a right-skewed lognormal rather than the Gaussian-based scaling used by T. W replaces T as the source of travel-time stochasticity once $\eta > 0$ (Section~\ref{subsec:stochastic-vars}).
+ \item \textbf{Discrete bus breakdown (B):} a Poisson-distributed discrete event, with rate $\lambda$, that permanently removes one bus from the active agent set for the remainder of the simulated day.
+ \end{itemize}
+
+ The four generators that produce S, T, W, and B are injected independently: no causal chain links them within the simulation. A breakdown event (B) does not trigger a demand surge (S) or a weather delay (W), and a weather event does not induce a mechanical failure. In practice, some real-world disturbances co-occur causally --- for example, heavy rain may both slow buses (W) and concentrate passengers at covered stops (S) --- but this study treats each generator as an independent factor. This design choice isolates the individual and combined effect of each disturbance class on controller performance and allows the single-disturbance ablation (Section~\ref{subsec:evaluation}) to attribute degradation unambiguously to a specific class.
+
  Four stochastic generators inject variability into the Python environment. Generators (i) and (ii) follow the perturbation framework of Wang and Sun~\cite{Wangsun}; the weather generator's heavy-tailed lognormal formulation follows Patil et al.~\cite{Patil2025Conformal}; the breakdown generator follows the rescheduling formulation of Cao et al.~\cite{Cao2022Train}. Table~\ref{tab:notation} collects the symbols used across this section and the MARL formulation that follows.
```

**Why:** RTC comment 8 — define each disturbance explicitly, clarify independence, distinguish stochastic demand from demand surge.

---

## 2026-08-06 — E3C15 — methods.tex, Section 3.2.4 (end)
**Status:** ACTIVE — with the original EDSA values (M=24, DOTr, SafeTravelPH). See AUDIT_TRAIL_READABLE.md (in this folder) for the full reconstructed table content.
**Commit:** `01c49bf`

```diff
  Throughout this chapter, \textit{ideal conditions} and \textit{non-ideal conditions} refer to these operating states of the simulated environment. \textit{Baseline controllers} refers separately to the three non-MARL control strategies (No Control, Forward Headway, Even Headway) against which the MARL policy is benchmarked. A condition is a state of the world; a controller is a choice of algorithm.

+ \begin{table}[htbp]
+ \centering
+ \caption{Simulation parameter summary: fixed, swept/variable, and derived parameters.}
+ \label{tab:sim-parameters}
+ ...
+ [three-part table: Fixed parameters (simulation horizon, M=24 stops,
+ N≈12-30 fleet, control stop count TBD, H_0 TBD, capacity TBD, ΔT TBD,
+ Ω={0.0,0.1,0.2,0.3,0.4}, |A_i|=10, N_runs≥30, γ/β TBD) | Swept/variable
+ parameters (η sweep, σ_d clip [1,3], σ_s clip [0.8,1.2], λ TBD) | Derived
+ parameters (μ, σ, CV_0 all TBD-DATA; σ_ln, μ_ln via method of moments)]
+ ...
+ \end{table}
+
+ Parameters marked \%TODO-VAL are to be confirmed during the implementation phase upon receipt of the operational dataset and DOTr schedule records; parameters marked \%TODO-DATA will be computed during the SUMO calibration phase described in Section~3.2.3. The stop count ($M=24$) and fleet-size range ($N \approx 12$--$30$) are carried over from the state-space dimensionality discussion in Section~1.2.2 and are not new values introduced here.

  \subsection{Data Processing}
```

**Why:** RTC comment 15 — summarize fixed/variable simulation parameters with target values.

---

## 2026-08-06 — E4C20 — methods.tex, Section 3.2.6 (four generator subsections)
**Status:** ACTIVE — all four sentences present (unlike the root manuscript, where the Texas pivot removed two of them)
**Commit:** `01c49bf`

```diff
  (Passenger Demand)
  ...Sampling occurs at the start of each simulation run, producing varied demand profiles across episodes.
+ In implementation, the scaling factor $f_d \sim \mathcal{N}(1, \sigma_d^2)$ is sampled once per episode at initialization and applied uniformly to every per-stop, per-time-of-day arrival rate for the duration of that simulated operating day, so all stops experience the same proportional demand shift within a single run while the shift itself varies across runs.
```

```diff
  (Traffic Delays)
  ...clipped to $[0.8, 1.2]$, representing typical daily congestion friction \cite{Wangsun}.
+ In implementation, the speed scaling factor $f_s \sim \mathcal{N}(1, \sigma_s^2)$ is sampled once per episode and applied to the bus's mean cruising speed on every inter-stop segment traversal during that day, producing a uniformly slower or faster corridor for that run without segment-level variation beyond the calibrated baseline.
  This generator provides the baseline stochastic variability in inter-stop travel time when the weather generator is inactive.
```

```diff
  (Weather-Induced Anomalies)
  ...regardless of its meteorological label.
+ In implementation, when $\eta > 0$ a fresh travel-time sample $T \sim \text{LogNormal}(\mu_{ln}, \sigma_{ln})$ is drawn independently for each bus at each inter-stop segment traversal during the episode, replacing the traffic-speed generator's output for that traversal; the lognormal parameters $\mu_{ln}$ and $\sigma_{ln}$ are computed from the segment's empirical mean $\mu$ and the swept $\eta$ via Equations~\eqref{eq:sigma_ln}--\eqref{eq:mu_ln}.
  The disturbance intensity sweep is therefore read as a span of travel-time variability magnitudes, not as a sweep across named weather categories.
```

```diff
  (Bus Breakdowns)
  ...with a configurable rate $\lambda$ (Table~\ref{tab:notation}).
+ In implementation, at each discrete simulation timestep of length $dt$, a Bernoulli trial with probability $\lambda \cdot dt$ is evaluated independently for each active bus; a success removes that bus from the active agent set for the remainder of the simulated day.
  When a breakdown occurs at bus $b_k$, $b_k$ is removed from the active agent set...
```

**Why:** RTC comment 20 — explain in detail how each disturbance scenario is simulated.

---

## 2026-08-06 — E4C21 — methods.tex, Sections 3.2.9 and 3.2.7
**Status:** ACTIVE — including the original "Disturbance intensity flag" observation-table row (EDSA Ver never received the Texas pivot's row edits)
**Commit:** `01c49bf`

```diff
  (3.2.9 opening)
  \subsection{Data Analysis Methods}

+ The three response variables logged per run are defined as follows. \textbf{Mean passenger waiting time} ($\bar{W}$) is the average time elapsed from a passenger's arrival at a stop to their successful boarding, averaged across all passengers served and all stops over one simulated operating day:
+
+ \begin{equation}
+ \bar{W} = \frac{1}{P} \sum_{p=1}^{P} \left(t_p^{\text{board}} - t_p^{\text{arrive}}\right)
+ \label{eq:waiting_time}
+ \end{equation}
+
+ where $P$ is the total number of passengers served in the run... \textbf{Mean total travel time} ($\bar{T}$) is the average elapsed time from a bus's departure from the origin terminal to its arrival at the final stop of the sub-corridor... \textbf{Headway coefficient of variation} ($CV_h$) measures headway regularity:
+
+ \begin{equation}
+ CV_h = \frac{\sigma_h}{\mu_h}
+ \label{eq:headway_cv}
+ \end{equation}
+
+ where $\sigma_h$ and $\mu_h$ are the standard deviation and mean of observed inter-bus headways... This construction mirrors the baseline coefficient of variation $CV_0$ already defined for travel time (Table~\ref{tab:notation}), applied here to the headway distribution instead.
+
  For each (control strategy, disturbance level) cell, $N \geq 30$ independent Monte Carlo runs are executed using matched random seeds across strategies. Three response variables are logged per run: mean passenger waiting time, mean total travel time, and headway coefficient of variation.
```

```diff
  (3.2.7 State Space, end of bullet list)
  \item \textbf{Environmental flags:} encoded indicators for the current disturbance intensity and any active downstream incident or breakdown.
  \end{itemize}

+ \begin{table}[htbp]
+ \centering
+ \caption{Agent observation vector: features, symbols, and data sources.}
+ \label{tab:observation-features}
+ ...
+ [7-row table: control stop index, forward/backward headway, onboard count,
+ waiting count, disturbance intensity flag, breakdown flag — each with Deployment
+ Source (AVL/APC/AFC/weather API/incident system) vs Simulation Source]
+ ...
+ \end{table}
+
+ In simulation, all observation features are generated synthetically by the Python environment at each control event by querying the analytical bus model and the active stochastic generators; no real sensor data is consumed during training or evaluation.
+
  \subsubsection{Action Space ($A_i$)}
```

**Why:** RTC comment 21 — metric definitions and observation-feature descriptions.

---

## 2026-08-06 — E1C1+E2C5+E4C22 — REVERTED
**Status:** REVERTED — confirmed the drafted block is absent from EDSA Ver

**Step 1 — Added (mid-session, not committed):**
```diff
  \item \textbf{Corridor bus operational data.} A per-trip record of EDSA Carousel bus operation... The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application.

  \end{itemize}

+ \paragraph{Dataset Description}
+
+ The baseline operating point described above is grounded in the SafeTravelPH dataset: a crowdsourced mobile application through which commuters submit trip-level GPS trajectory reports while travelling along Philippine transit corridors... Each submission corresponds to a single commuter trip and yields a per-trip trajectory log rather than a fixed-interval sensor feed, so record density varies by segment and time of day according to rider participation. The dataset comprises \%TODO-DATA: insert total trip record count...
+
+ [Table 3.2: "SafeTravelPH dataset fields and their role in simulation calibration" — 6 rows]
+
+ A secondary source of station-level ridership aggregates...is to be acquired from the Department of Transportation (DOTr) under the Freedom of Information framework...
+
  Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable, with disturbance magnitudes anchored to validated literature values rather than to a corridor-specific severe-weather sample.
```

**Step 2 — User caught it before commit:** "I should have said that you should not edit yet anything regarding the dataset. Because, we still dont have access to it yet."

**Step 3 — Reverted (back to original):**
```diff
+ \item \textbf{Corridor bus operational data.} A per-trip record of EDSA Carousel bus operation... The baseline operating point for this study is established from a crowdsourced operational record collected from the EDSA Busway during July 2023 through the SafeTravelPH mobile application.
+
+ \end{itemize}
+
- \paragraph{Dataset Description}
- [...entire drafted block removed...]
-
  Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable...
```

**Net result:** the pushed commit (`01c49bf`) contains no trace of the drafted block. EDSA Ver/methods.tex, which descends from this commit, likewise contains no trace of it.

---

## 2026-08-06 — Citation fix: Patil2025Conformal — methods.tex, Section 3.2.6
**Status:** ACTIVE (verified present — EDSA Ver never received the Texas pivot's later composition redesign of this section)
**Commit:** `4fcc1a1`

```diff
- Travel time is drawn as $T \sim \text{LogNormal}(\mu_{ln}, \sigma_{ln})$. Patil et al.~\cite{Patil2025Conformal} validated this parameterization against INRIX freeway data via the Kolmogorov-Smirnov test, reporting a close fit at the highest variability level they tested ($KS = 0.036$, $p = 0.94$ at $CV = 1.0$).
+ Travel time is drawn as $T \sim \text{LogNormal}(\mu_{ln}, \sigma_{ln})$. Patil et al.~\cite{Patil2025Conformal} tested this parameterization by generating SUMO-simulated travel times under the same CV-driven lognormal recipe --- with time windows and mean travel times anchored to INRIX historical data for an urban arterial corridor, not a freeway --- and confirming via the Kolmogorov-Smirnov test that the simulated distribution matches the assumed log-normal shape, reporting a close fit at the highest variability level they tested ($KS = 0.036$, $p = 0.94$ at $CV = 1.0$).
```

**Why:** Verified against the actual PDF. The paper's Table V classifies its route as "Local, Minor/Principal Arterials," not freeway; the KS test checks the simulated distribution's shape, not a direct INRIX comparison.

---

## 2026-08-06 — Citation fix: Rodriguez2023Cooperative — methods.tex, Section 3.2.7
**Status:** ACTIVE — the substance of the fix (broader 10-action space; six mutually-exclusive Rodriguez actions; 60-80% driver-compliance detail) is present in EDSA Ver/methods.tex, phrased close to but not word-for-word identical to the diff below (EDSA Ver retains the discretized-set "matches theirs exactly" clause that a later root-only rewrite dropped)
**Commit:** `4fcc1a1`

```diff
- The full action set is the Cartesian product of these two components: $|A_i| = 5 \times 2 = 10$ discrete actions per control event. A continuous holding parameter $\alpha \in [0, 1]$ was considered, following Wang and Sun~\cite{Wangsun}, but rejected for three reasons. First, continuous actions require actor-critic algorithms, whose training instability compounds across the swept-disturbance evaluation budget. Second, Rodriguez et al.~\cite{Rodriguez2023Cooperative} showed that a 5-bin discretization of $\alpha$ achieves combined holding-and-skipping control on a comparable corridor without measurable loss of performance versus continuous formulations. Third, real driver compliance with second-level holding instructions is itself coarse \cite{Rodriguez2023Cooperative}, so continuous precision in $\alpha$ is not meaningful at deployment.
+ The full action set is the Cartesian product of these two components: $|A_i| = 5 \times 2 = 10$ discrete actions per control event, allowing the agent to select a holding strength and a skip decision independently at each control event. This is a broader action space than Rodriguez et al.~\cite{Rodriguez2023Cooperative}, whose combined holding-and-skipping controller (DDQN-HA) instead selects among six \textit{mutually exclusive} actions: five holding strengths $\Omega = \{0.0, 0.1, 0.2, 0.3, 0.4\}$ (with $\omega = 0$ already covering the no-holding case) plus a single skip action. The discretized holding-strength set $\Omega$ adopted here matches theirs exactly. A continuous holding parameter $\alpha \in [0, 1]$ was considered, following Wang and Sun~\cite{Wangsun}, but rejected for two reasons. First, continuous actions require actor-critic algorithms, whose training instability compounds across the swept-disturbance evaluation budget. Second, real driver compliance with holding instructions is itself imperfect: Rodriguez et al.~\cite{Rodriguez2023Cooperative} model non-compliant drivers as departing after only 60--80\% of the instructed holding time, so continuous precision in $\alpha$ is not meaningful at deployment.
```

**Why:** Verified against the actual PDF. No continuous-vs-discrete comparison exists anywhere in it — that claim was unsupported. Rodriguez's actual action space is 6 mutually-exclusive actions, not this study's 10-action independent Cartesian space.

---

## 2026-08-06 — Citation fix: Wangsun — methods.tex, Section 3.2.6
**Status:** ACTIVE
**Commit:** `b366932`

```diff
- The baseline empirical transit demand is perturbed each episode by a scaling factor sampled from $\mathcal{N}(1, \sigma_d^2)$, clipped to $[1, 3]$, following Wang and Sun~\cite{Wangsun}. The asymmetric clip focuses the test on demand surges rather than symmetric variation, since demand drops produce lightly loaded conditions that do not stress-test the controller. The upper bound of 3 corresponds to roughly a tripling of baseline boarding rates, spanning the range observed during major event let-outs and severe-weather mode shifts.
+ The baseline empirical transit demand is perturbed each episode by a scaling factor sampled from $\mathcal{N}(1, \sigma_d^2)$ and clipped to $[1, 3]$, following the general Gaussian-clipped demand-scaling mechanism of Wang and Sun~\cite{Wangsun}, though this study adopts a narrower clip than their $[1, 10]$ range. The asymmetric clip focuses the test on demand surges rather than symmetric variation, since demand drops produce lightly loaded conditions that do not stress-test the controller. The upper bound of 3, corresponding to roughly a tripling of baseline boarding rates, is this study's own choice (\%TODO-VAL: revisit against Wang and Sun's wider range during implementation) rather than a value drawn from prior work.
```

**Why:** Verified against the actual PDF. Their Eq. 22 clips the demand scaling factor to $[1,10]$, not $[1,3]$.

---

## 2026-08-06 — E3C9 + E2C4 — introduction.tex, after Section 1.2.2 (SARL)
**Status:** ACTIVE — including the original Verbich & El-Geneidy row (EDSA Ver never received the Texas pivot's later swap to a Sun et al. row)
**Commit:** `4fcc1a1`

```diff
  ...which motivates the MARL choice here while acknowledging this caveat.

+ To situate the MARL literature reviewed in the next subsection within the broader ML and SARL landscape, Table~\ref{tab:ml_sarl_coverage} extends the paradigm comparison of Table~\ref{tab:control_paradigms} with a disturbance-coverage column, using the same D/S/T/W/B notation as Table~\ref{tab:marl_performance}.
+
+ \begin{table}[htbp]
+ \centering
+ \caption{Disturbance coverage across ML and SARL vehicle-scheduling studies...}
+ \label{tab:ml_sarl_coverage}
+ ...
+ [5-row table: Wang2017 (ML, D), Barrera2025Optimization (ML-assisted, D),
+ Zhao2022STDH (SARL, D+T), Zhang2025SADRL (SARL, D+T), verbich2021
+ (heuristic, W+B)]
+ ...
+ \end{table}
+
+ The funnel is now complete: no ML or SARL study covers W or B, and among MARL studies (Table~\ref{tab:marl_performance}), only Verbich and El-Geneidy's heuristic controller~\cite{verbich2021} addresses both --- and it is explicitly non-MARL. Patil et al.~\cite{Patil2025Conformal} similarly validate weather-induced travel-time distributions but do not address bus control at all... No prior study, ML, SARL, or MARL, combines W and B coverage with an actual MARL bus-scheduling controller, which is the specific gap this study fills.
+
  \subsection{Multi-Agent Reinforcement Learning}
```

**Why:** RTC comment 9 (ML/SARL disturbance table) and comment 4 (severe-weather comparison study) — satisfied together via a companion table rather than adding Verbich as a Table 1.2 row.

---

## 2026-08-06 — E3C10 — introduction.tex, before Table 1.2 discussion
**Status:** ACTIVE — including the original "Only Shi et al. carries a breakdown (B) entry" claim and Shi et al.'s "D, B" table classification (EDSA Ver never received the Texas pivot's later reclassification)
**Commit:** `4fcc1a1`

```diff
+ Only Shi et al.~\cite{Shi2022DistDRL} carries a B (breakdown) entry in Table~\ref{tab:marl_performance}. Cao et al.~\cite{Cao2022Train}, which also models discrete vehicle failures, is deliberately excluded from this count: their MARL application is to \textit{train} rescheduling, not bus scheduling, so it does not belong in a table scoped to MARL bus-control literature. Verbich and El-Geneidy~\cite{verbich2021} likewise model breakdowns but use heuristic, non-MARL control (Table~\ref{tab:ml_sarl_coverage}), so they are excluded for the same reason. Among MARL bus-scheduling studies specifically, Shi et al. remains the only one to model discrete breakdowns.
+
  Table~\ref{tab:marl_performance} summarizes what each study evaluated, what disturbances it modeled, and what it reported.
```

**Why:** RTC comment 10 — Table 1.2 shows only one B-paper but the presentation reportedly showed two.

---

## 2026-08-06 — E3C11 — figure caption attribution (introduction.tex, methods.tex)
**Status:** ACTIVE
**Commit:** `4fcc1a1`

```diff
  (one example — introduction.tex Figure 1.3; same pattern applied to 6 more captions)
- across $N$ agents, each acting on its own local observation $o_i$.}
+ across $N$ agents, each acting on its own local observation $o_i$. Authors' illustration.}
  \label{fig:sarl-vs-marl}
```

**Why:** RTC comment 11 — some figures lack citations; Figures 1.3 and 1.4 are original diagrams needing an "authors' illustration" note.

---

## 2026-08-06 — E3C14 — problem.tex, Delimitations (a)
**Status:** ACTIVE
**Commit:** `4fcc1a1`

```diff
- \textbf{Delimitations.} (a) Due to computational constraints, the simulation is restricted to a defined operational sub-segment of the EDSA Carousel corridor rather than the entire metropolitan road network. The restriction is justified by the need to preserve 1:1 empirical traffic volumes for GEH calibration without resorting to flow scaling; corresponding GEH calibration statistics are reported in Chapter~4.
+ \textbf{Delimitations.} (a) Due to computational constraints, the simulation is restricted to a defined operational sub-segment of the EDSA Carousel corridor rather than the entire metropolitan road network, and minor feeder roads leading into the corridor are not modeled. Both restrictions are justified by the same structural fact: the EDSA Carousel operates on a physically separated, barrier-protected busway \cite{Chua2026}, so the agents' state and reward depend only on bus dynamics within the dedicated lane, specifically headways, dwell times, and onboard loads, none of which are directly observed by or computed from feeder-road traffic. Feeder roads affect the corridor only indirectly, through the passenger arrival rates they produce at each stop, and that effect is already captured by the calibrated per-stop demand distributions (Section~3.2.5) without needing to simulate the feeder network itself. Modeling feeder roads in SUMO would add computational cost without adding any new information the agents' observation or reward could use, since the sub-corridor restriction also preserves 1:1 empirical traffic volumes for GEH calibration without resorting to flow scaling; corresponding GEH calibration statistics are reported in Chapter~4.
```

**Why:** RTC comment 14 — justify why minor roads leading to the corridor are no longer considered.

---

## 2026-08-06 — E3C16 — figure/table callout sweep (introduction.tex, methods.tex)
**Status:** ACTIVE — all 10 callouts verified present
**Commit:** `b15ab23`

Ten one-clause insertions, each adding a missing `\ref{}` to an existing sentence next to a previously-uncited figure/table:

```diff
  (introduction.tex)
- ...up from 63.02 million in 2024 \cite{DOTr2025Ridership}.
+ ...up from 63.02 million in 2024 (Figure~\ref{fig:bg-ridership}) \cite{DOTr2025Ridership}.

- The reduction in average speeds are about 5.34\%...
+ As Figure~\ref{fig:bg-rainfall} shows, the reduction in average speeds are about 5.34\%...

- To address this, most modern formulations use \textbf{Centralized Training with Decentralized Execution (CTDE)}.
+ To address this, most modern formulations use \textbf{Centralized Training with Decentralized Execution (CTDE)}, illustrated in Figure~\ref{fig:ctde}.
```

```diff
  (methods.tex)
- The pipeline proceeds in two phases.
+ As shown in Figure~\ref{fig:pipeline}, the pipeline proceeds in two phases.

- ...measures the discrepancy between simulated and observed hourly bus volumes on individual corridor segments:
+ ...measures the discrepancy...on individual corridor segments, illustrated in panel (a) of Figure~\ref{fig:calibration-illustrative}:

- RMSE evaluates how closely simulated bus speed trajectories match empirical observations:
+ RMSE evaluates...match empirical observations, illustrated in panel (b) of Figure~\ref{fig:calibration-illustrative}:

- Parameters marked \%TODO-VAL are to be confirmed...
+ Table~\ref{tab:sim-parameters} therefore serves as the single reference point for every parameter used across this chapter. Parameters marked \%TODO-VAL are to be confirmed...

- In simulation, all observation features are generated synthetically...
+ As Table~\ref{tab:observation-features} shows, in simulation all observation features are generated synthetically...

- The learning process follows the standard reinforcement-learning feedback loop...
+ ...follows the standard...feedback loop..., illustrated in Figure~\ref{fig:aec-training}.

- ...are each run for $N \geq 30$ Monte Carlo iterations with matched seeds. Under ideal conditions EH is already near-optimal,
+ ...matched seeds, reported in the format shown in Figure~\ref{fig:stage-a-illustrative}. Under ideal conditions EH is already near-optimal,

- ...with the breakdown generator active at each level.
+ ...active at each level, using the Monte Carlo evaluation procedure illustrated in Figure~\ref{fig:aec-eval}.
```

**Why:** RTC comment 16 — figures and tables should be called and discussed in the paragraphs, not just placed.

---

## 2026-08-06 — E3C18 + E3C19 — main.tex preamble
**Status:** ACTIVE
**Commit:** `b15ab23`

```diff
  \usepackage{ragged2e}
  \usepackage{totalcount}
+ \usepackage{setspace}
```

```diff
  %TC:ignore
  \begin{document}
  %TC:ignore
+ \onehalfspacing
  \input{title.tex} % Putting the title page
```

```diff
  % --------------------------------------------------------------------------------
  % Start line numbering
- %\linenumbers
+ \linenumbers
```

**Why:** RTC comments 18 and 19 — 1.5 line spacing and line numbers for the non-final manuscript.

---

## 2026-08-06 — E1C2 — methods.tex, Section 3.2.5 (end)
**Status:** ACTIVE — the field-mapping table (`\label{tab:field-mapping}`) is compiled/live in EDSA Ver (unlike the root manuscript, where the Texas pivot buried it inside an `\iffalse` block)
**Commit:** `ce79e06`

```diff
  \end{itemize}

+ Table~\ref{tab:field-mapping} maps each required raw field to the parameter derived from it and the MARL component that parameter feeds into, connecting the data requirements above to the disturbance generators (Section~\ref{subsec:stochastic-vars}), the control-stop selection criteria (Section~\ref{subsec:control-stop-selection}), and the agent observation vector (Section~\ref{subsec:state-space}). The mapping reflects the study's design intent, not properties of a processed dataset; specific statistics remain \%TODO-DATA pending dataset acquisition.
+
+ \begin{table}[htbp]
+ \centering
+ \caption{Mapping of required raw dataset fields to derived parameters and their role in the MARL formulation.}
+ \label{tab:field-mapping}
+ ...
+ [6-row table: GPS location → travel-time distribution → SUMO calibration/
+ traffic-speed & weather generators; boarding events → demand rate →
+ demand-surge generator/observation feature; alighting events →
+ through-volume → control-stop selection criterion 3; occupancy → load
+ profile → observation feature/dwell-time estimation; operating speed →
+ cruising speed → GEH calibration/traffic-speed generator; dwell time →
+ dwell distribution → event-driven bus model]
+ ...
+ \end{table}
+
  Severe-weather conditions are not estimated from operational data in this study but are injected as a controlled experimental variable...
```

**Why:** RTC comment 2 — map dataset fields to proposed features of the study.

---

## 2026-08-06 — E3C17 — introduction.tex (Background), methods.tex (Weather-Induced Anomalies)
**Status:** ACTIVE — both the corridor map figure and the η-sweep basis table are compiled/live in EDSA Ver (unlike the root manuscript, where the Texas pivot buried the corridor map inside an `\iffalse` block)
**Commit:** `142502b`

```diff
  (introduction.tex, after the ridership figure)
      \label{fig:bg-ridership}
  \end{figure}
  %%

+ Figure~\ref{fig:bg-corridor-map} shows the EDSA Carousel Southbound route from Monumento to PITX, the corridor this study is grounded in, together with the other public transport modes (jeepney, MRT, LRT, tricycle, UV/FX) that intersect it at each major stop.
+
+ \begin{figure}[htbp]
+     \centering
+     \includegraphics[width=0.75\textwidth]{Figures/bg_fig3_edsa_corridor_map.pdf}
+     \caption[EDSA Carousel corridor map]{EDSA Carousel Southbound route
+     (Monumento to PITX) with intersecting public transport modes at each
+     stop. Authors' illustration, adapted from the group's defense
+     presentation.}
+     \label{fig:bg-corridor-map}
+ \end{figure}
+
  Despite the gradual increase in demand,
```

```diff
  (methods.tex, Weather-Induced Anomalies subsubsection)
  ...results at this level are interpreted as a probe of controller behavior under extreme conditions rather than as a calibrated scenario.
+ Table~\ref{tab:eta-basis} summarizes this reasoning.
+
+ \begin{table}[htbp]
+ \centering
+ \caption{Basis for each swept weather-disturbance intensity value.}
+ \label{tab:eta-basis}
+ ...
+ [5-row table: η=0.0 generator off; η=0.3/0.6 inside Patil et al.'s
+ validated range; η=1.0 top of validated range (nominal severe point);
+ η=1.3 beyond validated range (extrapolated stress test)]
+ ...
+ \end{table}

  The mapping from $\eta$ to a specific named weather severity...
```

**Why:** RTC comment 17 — include figures/tables shown in the defense but missing from the manuscript.

---

## 2026-08-06 — N1 (self-identified, not RTC) — methods.tex, Section 3.2.7
**Status:** ACTIVE
**Commit:** `14e926e`

```diff
  ...This study defines the reward \textit{structure} for the hybrid action space, the three component terms above, and treats their relative weighting, plus a sensitivity analysis over those weights, as the implementation-phase deliverable (EO 2.1). The component structure is fixed; the coefficients are not yet finalized.
+
+ The reward is computed individually for each agent at every control event, not as a shared team-level signal: $r_{i,t}$ is agent $i$'s own entry in the transition $(s_{i,t}, a_{i,t}, r_{i,t}, s_{i,t'})$ written to the shared replay buffer (Training and Execution Protocol, step 4), so each bus is scored on the consequences of its own action even though all agents update the same shared network. Locally-observable quantities already in $s_{i,t}$, principally the forward and backward headway components $h^-$ and $\hat{h}^+$, let this individual signal still reflect corridor-wide regularity without requiring a centralized reward computation at execution time. The three priorities combine additively as a weighted sum of per-event penalty terms,
+
+ \begin{equation}
+ r_{i,t+k} = -w_1 \cdot (\text{headway-irregularity term}) - w_2 \cdot (\text{waiting-time term}) - w_3 \cdot (\text{skip-degeneracy term}),
+ \label{eq:reward-form}
+ \end{equation}
+
+ with weights $w_1, w_2, w_3$ \%TODO-VAL: to be tuned as the Expected Output 2.1 sensitivity analysis. Each term is expressed as a non-positive penalty, so the agent maximizes its expected return in Eq.~\eqref{eq:bellman} by simultaneously minimizing headway irregularity, passenger waiting, and degenerate skipping; this sign convention, not the specific per-term formulas or their relative weights, is what this chapter fixes ahead of implementation.
```

**Why:** self-identified gap (user notice, not an RTC comment).

---

## 2026-08-06 — N2 — problem.tex, Section 2.3 (Significance)
**Status:** ACTIVE — restored to EDSA Ver on 2026-08-25 after being found missing from the initial (contaminated) backup snapshot; see the 2026-08-25 restoration entry below
**Commit:** `a64f44c`

```diff
  \section{Significance of the Study}
- This study contributes both practical and scientific significance.
+ This study contributes both practical and scientific significance. MARL is the control method under evaluation in this study; the corridor's service reliability under disturbance is the object of study it is applied to measure, which is why practical significance is discussed first.

  \textbf{Practical significance.} The EDSA Carousel carries on the order of $1.8\times10^5$ passengers daily...
```

**Why:** self-identified, prompted by the user's recollection that a panelist questioned during Q&A whether the study reads as more focused on MARL than bus scheduling.

---

## 2026-08-06 — N2 — problem.tex, Section 2.2 (Research Gap)
**Status:** ACTIVE — restored to EDSA Ver on 2026-08-25 after being found missing from the initial (contaminated) backup snapshot; see the 2026-08-25 restoration entry below
**Commit:** `a64f44c`

```diff
  Without this characterization, it cannot be determined whether reported MARL gains persist, degrade gracefully, or collapse under realistic operating disturbances, which in turn blocks the transition of MARL bus scheduling from simulation to real urban transit deployment.
+ This joint-disturbance framing reflects two independently-documented, concurrent operational realities of the same corridor rather than only a gap in existing comparison tables: EDSA experiences both weather-driven service disruptions \cite{PhilstarTyphoon2024, PIA_Emergency2023} and chronic mechanical-failure risk \cite{Chua2026} as ongoing features of its operating environment, so a controller validated against each in isolation provides no evidence of how it behaves when a transit operator's actual risk exposure includes both at once. The disturbance generators remain independently sampled within the simulation (Section~3.2.6); this operational context motivates evaluating their union, not a claim that the two are causally or temporally linked.

  The weather-disturbance class (W) in particular was identified through the literature survey conducted earlier in this study...
```

**Why:** self-identified. Grounds the "combined disturbance" framing in an EDSA-specific operational fact.

---

## 2026-08-06 — N1 rewrite (user-provided prose) — methods.tex, Section 3.2.7
**Status:** NOT applied to EDSA Ver — see note

**Note:** this stylistic rewrite of N1 was applied to the root manuscript on 2026-08-06 (same day, commit `79085f4`), but `EDSA Ver/methods.tex` retains N1's *original* wording (see the N1 entry directly above), not this polished rewrite. `EDSA Ver/` was forked from a commit that predates this particular same-day rewrite. The underlying content (reward structure, individual-vs-shared computation, sign convention, equation) is identical in substance; only the prose style differs.

```diff
  ...Existing MARL bus-control reward formulations span a range of trade-offs among these priorities, from headway-coefficient-of-variation forms for holding-only action spaces \cite{Wangsun,Wang2023MultiObj} to passenger-time forms for combined holding-and-skipping action spaces \cite{Rodriguez2023Cooperative}.
- This study defines the reward \textit{structure} for the hybrid action space, the three component terms above, and treats their relative weighting, plus a sensitivity analysis over those weights, as the implementation-phase deliverable (EO 2.1). The component structure is fixed; the coefficients are not yet finalized.
-
- The reward is computed individually for each agent at every control event, not as a shared team-level signal: $r_{i,t}$ is agent $i$'s own entry in the transition $(s_{i,t}, a_{i,t}, r_{i,t}, s_{i,t'})$ written to the shared replay buffer (Training and Execution Protocol, step 4), so each bus is scored on the consequences of its own action even though all agents update the same shared network. Locally-observable quantities already in $s_{i,t}$, principally the forward and backward headway components $h^-$ and $\hat{h}^+$, let this individual signal still reflect corridor-wide regularity without requiring a centralized reward computation at execution time. The three priorities combine additively as a weighted sum of per-event penalty terms,
+ This study establishes the overall reward structure for the hybrid action space by defining the three reward components and their additive formulation, while treating the corresponding weighting coefficients, together with their sensitivity analysis, as the implementation-phase deliverable under Expected Output 2.1. Although the component structure is fixed at this stage, the coefficients remain as placeholders to be determined during implementation through experimental evaluation.
+
+ The reward is computed independently for each agent at every control event rather than as a shared team-level objective. Accordingly, $r_{i,t}$ represents the reward assigned to agent $i$ and is stored as that agent's transition in the shared replay buffer (Training and Execution Protocol, step 4). Each bus is therefore evaluated based on the consequences of its own action, even though all agents learn from a common shared network. Since the reward is derived from locally observable quantities already contained in the agent's observation, particularly the forward and backward headway measurements, the resulting signal remains aligned with corridor-wide service regularity without requiring a centralized reward computation during execution.
+
+ The overall reward function is expressed as the weighted sum of three penalty terms:

  \begin{equation}
  r_{i,t+k} = -w_1 \cdot (\text{headway-irregularity term}) - w_2 \cdot (\text{waiting-time term}) - w_3 \cdot (\text{skip-degeneracy term}),
  \label{eq:reward-form}
  \end{equation}

- with weights $w_1, w_2, w_3$ \%TODO-VAL: to be tuned as the Expected Output 2.1 sensitivity analysis. Each term is expressed as a non-positive penalty, so the agent maximizes its expected return in Eq.~\eqref{eq:bellman} by simultaneously minimizing headway irregularity, passenger waiting, and degenerate skipping; this sign convention, not the specific per-term formulas or their relative weights, is what this chapter fixes ahead of implementation.
+ where $w_1$, $w_2$, and $w_3$ denote the weighting coefficients (\%TODO-VAL) to be determined through the Expected Output 2.1 sensitivity analysis. Each component is formulated as a non-positive penalty, allowing the agent to maximize its cumulative return in Eq.~\eqref{eq:bellman} by minimizing headway irregularity, passenger waiting time, and unnecessary stop-skipping behavior. Consequently, this chapter establishes the reward formulation and its optimization objective, while the specific mathematical expressions and coefficient values are reserved for the implementation and evaluation phase.
```

**Why (root-manuscript rationale, not yet applied here):** the user supplied polished replacement prose for N1's content. Not yet applied to EDSA Ver; can be added as a small follow-up edit if desired.

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
