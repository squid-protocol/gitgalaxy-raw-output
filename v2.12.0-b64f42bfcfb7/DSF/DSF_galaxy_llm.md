# ARCHITECTURAL_BRIEF: DSF
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/navikt/DSF` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1483 analyzed artifact(s), 495513 LOC.
- **Load-bearing artifact:** `src/GML/R0019913.pli` -- 82 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/R0018090.pli` -- pulls in 60 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/R0010410.pli` at magnitude 3609.0 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1483 |
| Analyzed Artifacts (Scanned) | 1483 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 495513 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | PLI |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7035 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0762 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.4987 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 147 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLI | 1473 | 494385 | 99.3% |
| COBOL | 7 | 1128 | 0.5% |
| MARKDOWN | 2 | 0 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1483 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 55%, Compute Cores Files 22%, Many-Argument Workhorses Files 15%, Parameter Forwarders Files 4%, Interface Declarations Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1480 | 99.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.7 | 41.8 | 42.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.3 | 61.5 | 61.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 33.7 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.6 | 15.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 84.9 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 88.5 | 99.9 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 7.0 | 7.6 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 99.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1500 | 238 | 3 | `src/GML/R0010480.pli` |
| cleanup | 108 | 56 | 0 | `src/GML/R001I904.pli` |
| guards | 1145 | 302 | 3 | `src/GML/R0010202.pli` |
| danger | 5186 | 601 | 10 | `src/R0010410.pli` |
| concurrency | 312 | 66 | 0 | `src/GML/R0010501.pli` |
| connectivity | 1958 | 1330 | 2 | `src/R0019912.pli` |
| io | 2006 | 303 | 4 | `src/GML/R0019H80.pli` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2967 | 560 | 6 | `src/GML/R0019E04.pli` |
| time | 105 | 47 | 0 | `src/GML/R001NO10.pli` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 649 | 182 | 1 | `src/GML/R001I101.pli` |
| tests | 0 | 0 | 0 | - |
| docs | 8 | 8 | 0 | `src/GML/R0014153.pli` |
| debt | 118 | 23 | 0 | `src/GML/R001NO20.pli` |
| mutation | 149484 | 1465 | 231 | `src/R0010410.pli` |
| dead_code | 2100 | 881 | 4 | `src/R001I501.pli` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 2346 | 241 | 6 | `src/GML/R001I501.pli` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/GML/R0019H80.pli` (Hits: 88)
- `src/GML/R0019E04.pli` (Hits: 38)
- `src/R0019E04.pli` (Hits: 38)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **R0019913.pli** (`src/GML/R0019913.pli`) — 82 inbound connections
2. **R0019912.pli** (`src/GML/R0019912.pli`) — 78 inbound connections
3. **R0019995.pli** (`src/R0019995.pli`) — 77 inbound connections
4. **R0019912.pli** (`src/R0019912.pli`) — 76 inbound connections
5. **R0019905.pli** (`src/GML/R0019905.pli`) — 69 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **R0018090.pli** (`src/R0018090.pli`) — 60 outbound dependencies
2. **R0010490.pli** (`src/GML/R0010490.pli`) — 59 outbound dependencies
3. **R0010490.pli** (`src/R0010490.pli`) — 59 outbound dependencies
4. **R001NO10.pli** (`src/R001NO10.pli`) — 59 outbound dependencies
5. **R0014101.pli** (`src/R0014101.pli`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (@ `src/R0017044.pli`) -> Impact: **1173.6** | LOC: 2098
  * *Intent:* /* ***************************************************************** */ /* IDENTIFIKASJON: */ /* R0017044 - PROSEDYRE I PLI */ /* PROGRAMMERER: JAN JA...
- `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (@ `src/GML/R0017044.pli`) -> Impact: **1160.8** | LOC: 3020
- `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (@ `src/R0017099.pli`) -> Impact: **1083.0** | LOC: 3161
- `PLASSER_TEKSTTYPE_A_KODE` **(Many-Argument Workhorses)** (@ `src/R0017041.pli`) -> Impact: **816.5** | LOC: 2093
  * *Intent:* /*IDENTIFIKASJON: */ /* R0017041 - PROSEDYRE I PLI */ /* PROGRAMMERER: JAN, DESEMBER 82 */ /*HENSIKT: */ /* RUTINEN SETTER INN KODER FOR TEKSTTYPE A I...
- `PLASSER_TEKSTTYPE_A_KODE` **(Many-Argument Workhorses)** (@ `src/GML/R0017041.pli`) -> Impact: **629.3** | LOC: 1709
  * *Intent:* /* R0017041 - PROSEDYRE I PLI */ 00000330 /* PROGRAMMERER: JAN, DESEMBER 82 */ 00000340 /*HENSIKT: */ 00000350 /* RUTINEN SETTER INN KODER FOR TEKSTTY...
- `OVERFØR_INNTEKT_MAP` **(I/O & Config Routines)** (@ `src/GML/R001I903.pli`) -> Impact: **554.1** | LOC: 1803
- `OVERFØR_INNTEKT_MAP` **(I/O & Config Routines)** (@ `src/R001I903.pli`) -> Impact: **554.1** | LOC: 1803
  * *Intent:* %SKIP; /* ***************************************************************** */ /* */ /* PROSEDYRA OVERFØRER DATA FRA INNTEKT_OMR TIL */ /* SKJERMBILDE...
- `R01UE20` **(Many-Argument Workhorses)** (@ `src/R001UE20.pli`) -> Impact: **532.8** | LOC: 2029
  * *Intent:* /* SKILSMISSE......................1440 */ /* FLYTTE SAMMEN...................1450 */ /* FLYTTE FRA HVERANDRE............1460 */ /* DISSE RUTINENE BRU...
- `EØS_TEKSTER_UP_AP` **(Many-Argument Workhorses)** (@ `src/R0017044.pli`) -> Impact: **422.1** | LOC: 1168
  * *Intent:* /* ----------------------------------------------------------------- */
- `R01UE20` **(Many-Argument Workhorses)** (@ `src/GML/R001UE20.pli`) -> Impact: **400.3** | LOC: 1501

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 718 | 145622.82 | 51.45% | 3.82% |
| `src/GML` | 763 | 126822.24 | 32.71% | 4.71% |
| `__monolith__` | 2 | 2.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/R00104KF.pli` -> **97.0688%** Exposure
- `src/GML/R0010707.pli` -> **81.7574%** Exposure
- `src/R00104UF.pli` -> **77.73%** Exposure
- `src/GML/R00104UF.pli` -> **74.4868%** Exposure
- `src/GML/R00104AF.pli` -> **51.0592%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/A0010301.pli` -> **100.0%** Exposure
- `src/G0019999.pli` -> **100.0%** Exposure
- `src/GML/R0010506.pli` -> **100.0%** Exposure
- `src/GML/R0010507.pli` -> **100.0%** Exposure
- `src/GML/R0010602.pli` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/GML/R0011007.pli` -> **6** Orphaned Functions | **0** Duplicates
- `src/GML/R0019F05.pli` -> **6** Orphaned Functions | **0** Duplicates
- `src/GML/R0015401.pli` -> **4** Orphaned Functions | **0** Duplicates
- `src/R0015401.pli` -> **4** Orphaned Functions | **0** Duplicates
- `src/GML/R0010422.pli` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7390` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/R0010410.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.717)
- **Top Global Matches:** file_cluster_8: 7.717, file_cluster_6: 12.936, file_cluster_4: 21.249
- **Magnitude:** 3609.0 | **LOC:** 5683 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BYGG_BEREGNINGSGRUNNLAG` **(I/O & Config Routines)** (Impact: 379.6)
    * *Intent:* /* ----------------------------------------------------------------- */ /* BYGG BEREGNINGSGRUNNLAG *...
  * `BYGG_YTELSER` **(I/O & Config Routines)** (Impact: 123.6)
    * *Intent:* /* ----------------------------------------------------------------- */ /* BYGG YTELSER INTERN PROC ...
  * `BYGG_STATUS` **(I/O & Config Routines)** (Impact: 73.0)
  * `ACCUM_INNT` **(I/O & Config Routines)** (Impact: 64.7)
  * `HENT_PENSJONSTYPE1` **(Compute Cores)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 447 instances
* *State Mutation (weighted view):* 2306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 840`, `structural_boundaries: 552`, `args: 9`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 1`, `state_mutation: 1412`, `dead_code: 17`
* *Architecture:* `io: 8`, `api: 1`, `import: 33`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` DLIUIB, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912, P0019913...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/R001I903.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.629)
- **Top Global Matches:** file_cluster_3: 15.629, file_cluster_1: 33.575, file_cluster_8: 36.926
- **Magnitude:** 3557.68 | **LOC:** 3926 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_INNTEKT_MAP` **(I/O & Config Routines)** (Impact: 554.1)
    * *Intent:* %SKIP; /* ***************************************************************** */ /* */ /* PROSEDYRA OV...
  * `OVERFØR_INNTEKT` **(I/O & Config Routines)** (Impact: 175.8)
    * *Intent:* %PAGE; /* ***************************************************************** */ /* */ /* PROSEDYREN O...
  * `KONTROLL_INNTEKT` **(Compute Cores)** (Impact: 134.9)
    * *Intent:* %PAGE; /* */ /* ***************************************************************** */ /* */ /* KONTRO...
  * `R001I93` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* /* ***************************************************************** */ /*DATASETTOPPLYSNINGER: */ /...
  * `OVERFØR_INNTEKT_HOPPL_MAP` **(I/O & Config Routines)** (Impact: 25.0)
    * *Intent:* /* ***************************************************************** */ /* */ /* PROSEDYRA OVERFØRER...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 679 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 2475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 767`, `structural_boundaries: 313`, `args: 3`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1117`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` DFHBMSCA, P0019906, P0019908, P0019910, P0019912, P0019924, P0019925, P0019956...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/R0014901.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.26)
- **Top Global Matches:** file_cluster_3: 9.26, file_cluster_8: 15.557, file_cluster_6: 28.315
- **Magnitude:** 3260.1 | **LOC:** 4789 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **19**; blast radius 0.713; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (71.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AUTO_ONLINE` **(I/O & Config Routines)** (Impact: 357.6)
    * *Intent:* /***** HER SLUTTER HOVEDSTYRINGEN *****/
  * `R001490` **(Compute Cores)** (Impact: 120.1)
    * *Intent:* /*ENDRET : 23.12.88 - HERMAN */ /* UNGE UFØRE FÅR ENDRET ALDERSGRENSEN TIL 22 ÅR FRA 01895 */ /*ENDR...
  * `OVERGANG_TIL_P67` **(Compute Cores)** (Impact: 94.4)
    * *Intent:* /* ----------------------------------------------------------------- */
  * `UF_DØD` **(Compute Cores)** (Impact: 74.0)
    * *Intent:* /*NY PROC 0892 TRUDE PGA DØDE UFØRE FØR 24 ÅR FØDT < 43 */
  * `UNG_DØD_D` **(Many-Argument Workhorses)** (Impact: 73.0)
    * *Intent:* /* -------------------------------------------------------------- */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 390 instances
* *State Mutation (weighted view):* 1915
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 782`, `structural_boundaries: 526`, `args: 21`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1135`, `dead_code: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.713
  * `Choke Point (Betweenness):` 0.000574 | `Ripple Effect (Closeness):` 0.016032
  * `Imports (Out-Degree: 14):` P0014003, P0019906, P0019908, P0019910, P0019911, P0019912, P0019921, P0019925...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/R0017044.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.742)
- **Top Global Matches:** file_cluster_3: 15.742, file_cluster_1: 33.65, file_cluster_8: 36.946
- **Magnitude:** 2816.0 | **LOC:** 3877 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.444; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (Impact: 1173.6)
    * *Intent:* /* ***************************************************************** */ /* IDENTIFIKASJON: */ /* R00...
  * `EØS_TEKSTER_UP_AP` **(Many-Argument Workhorses)** (Impact: 422.1)
    * *Intent:* /* ----------------------------------------------------------------- */
  * `EØS_TEKSTER_ETTERL` **(Many-Argument Workhorses)** (Impact: 93.2)
    * *Intent:* /* ***************************************************************** */
  * `EØS_TEKSTER_UP` **(Many-Argument Workhorses)** (Impact: 92.3)
    * *Intent:* /* ----------------------------------------------------------------- */ /* *************************...
  * `EØS_FORSØRG` **(I/O & Config Routines)** (Impact: 16.9)
    * *Intent:* /* ----------------------------------------------------------------- */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 953
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 462`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 521`, `dead_code: 25`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012249
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GML/R0017044.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.191)
- **Top Global Matches:** file_cluster_1: 5.191, file_cluster_3: 48.177, file_cluster_8: 70.028
- **Magnitude:** 2727.28 | **LOC:** 3531 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.446; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (Impact: 1160.8)
  * `EØS_TEKSTER` **(Many-Argument Workhorses)** (Impact: 69.0)
    * *Intent:* /* ----------------------------------------------------------------- */00030760 /* *****************...
  * `EØS_TEKSTER_ETTERL` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* /* ***************************************************************** */00033490
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 1370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 641`, `structural_boundaries: 527`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 814`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.446
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014456
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GML/R001I903.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.663)
- **Top Global Matches:** file_cluster_3: 15.663, file_cluster_1: 33.592, file_cluster_8: 36.941
- **Magnitude:** 2562.2 | **LOC:** 3916 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_INNTEKT_MAP` **(I/O & Config Routines)** (Impact: 554.1)
  * `OVERFØR_INNTEKT` **(I/O & Config Routines)** (Impact: 175.8)
    * *Intent:* %PAGE; 00006600 /* ***************************************************************** */00006610 /* *...
  * `KONTROLL_INNTEKT` **(Compute Cores)** (Impact: 134.9)
  * `R001I93` **(Many-Argument Workhorses)** (Impact: 63.8)
  * `OVERFØR_INNTEKT_HOPPL_MAP` **(I/O & Config Routines)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 342 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 767`, `structural_boundaries: 310`, `args: 3`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 779`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` DFHBMSCA, P0019906, P0019908, P0019910, P0019912, P0019924, P0019925, P0019956...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/GML/R0014901.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.634)
- **Top Global Matches:** file_cluster_8: 10.634, file_cluster_3: 14.166, file_cluster_6: 22.929
- **Magnitude:** 2337.5 | **LOC:** 4176 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 0.754; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (52.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AUTO_ONLINE` **(I/O & Config Routines)** (Impact: 301.4)
  * `R001490` **(Compute Cores)** (Impact: 85.0)
    * *Intent:* /*ENDRET : 23.12.88 - HERMAN */00001850 /* UNGE UFØRE FÅR ENDRET ALDERSGRENSEN TIL 22 ÅR FRA 01895 *...
  * `UF_DØD` **(Compute Cores)** (Impact: 70.9)
    * *Intent:* /*NY PROC 0892 TRUDE PGA DØDE UFØRE FØR 24 ÅR FØDT < 43 */ 00038220
  * `OVERGANG_TIL_P67` **(Compute Cores)** (Impact: 64.8)
  * `FJERN_BARNEPENSJON` **(Many-Argument Workhorses)** (Impact: 61.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 1232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 458`, `args: 20`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 832`, `dead_code: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.754
  * `Choke Point (Betweenness):` 0.000684 | `Ripple Effect (Closeness):` 0.016378
  * `Imports (Out-Degree: 12):` P0019906, P0019908, P0019910, P0019911, P0019912, P0019921, P0019925, R0019902...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/R0017099.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.253)
- **Top Global Matches:** file_cluster_1: 5.253, file_cluster_3: 48.192, file_cluster_8: 70.04
- **Magnitude:** 2249.64 | **LOC:** 3289 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (58.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLASSER_TEKSTTYPE_U_KODE` **(Many-Argument Workhorses)** (Impact: 1083.0)
  * `EØS_TEKSTER` **(Many-Argument Workhorses)** (Impact: 33.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 1069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 434`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 741`, `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/GML/R0010410.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.914)
- **Top Global Matches:** file_cluster_6: 6.914, file_cluster_4: 13.016, file_cluster_8: 13.174
- **Magnitude:** 2123.12 | **LOC:** 3869 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BYGG_BEREGNINGSGRUNNLAG` **(I/O & Config Routines)** (Impact: 133.2)
  * `BYGG_YTELSER` **(I/O & Config Routines)** (Impact: 88.8)
  * `ACCUM_INNT` **(I/O & Config Routines)** (Impact: 64.0)
  * `BYGG_STATUS` **(I/O & Config Routines)** (Impact: 50.6)
  * `HENT_PENSJONSTYPE1` **(Compute Cores)** (Impact: 44.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 1264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 432`, `args: 10`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 1`, `state_mutation: 864`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 1`, `import: 25`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` DLIUIB, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912, P0019913...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/GML/R00149X1.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.474)
- **Top Global Matches:** file_cluster_8: 10.474, file_cluster_3: 14.256, file_cluster_6: 22.782
- **Magnitude:** 1673.04 | **LOC:** 3048 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AUTO_ONLINE` **(I/O & Config Routines)** (Impact: 170.8)
  * `UNG_UFØR` **(I/O & Config Routines)** (Impact: 70.3)
  * `R001490` **(Compute Cores)** (Impact: 68.8)
    * *Intent:* /*ENDRET : 16.2.88 - HERMAN */00001170 /* UNGE UFØRE FÅR ENDRET BUP_GARANTI TIL 3.00 POENG */0000118...
  * `FJERN_BARNEPENSJON` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `OVERGANG_TIL_P67` **(Compute Cores)** (Impact: 58.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 327`, `args: 15`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 635`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` P0019906, P0019908, P0019910, P0019911, P0019912, P0019921, P0019925, R0019902...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/R001I201.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.358)
- **Top Global Matches:** file_cluster_8: 12.358, file_cluster_3: 12.823, file_cluster_6: 24.733
- **Magnitude:** 1666.52 | **LOC:** 3088 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.469; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SKRIV_INNT` **(Many-Argument Workhorses)** (Impact: 82.6)
    * *Intent:* /* **************************************************************** */ /* */ /* PROCEDURE FOR Å FLYT...
  * `OVERFØR_INNTEKTER` **(Many-Argument Workhorses)** (Impact: 65.8)
  * `R001I20` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /*ENDRET: 06.04.88 AV SVERRE LUNDEBY, DATA-UTVIKLING A/S */ /* ****** */ /* INITIERER BRUKERID I FNR...
  * `FLYTT_DBOPPL_TIL_BL_OMR_FRAFNR` **(I/O & Config Routines)** (Impact: 40.6)
  * `BEHANDLE_MARKERTE_LINJER` **(I/O & Config Routines)** (Impact: 37.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 1076
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 298`, `args: 4`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 784`, `dead_code: 6`
* *Architecture:* `io: 18`, `api: 1`, `import: 23`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.001542
  * `Imports (Out-Degree: 11):` DLIUIB, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912, P0019921...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/R001U606.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.177)
- **Top Global Matches:** file_cluster_1: 6.177, file_cluster_3: 48.298, file_cluster_8: 70.105
- **Magnitude:** 1577.6 | **LOC:** 1388 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.552; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_U3_SØKER_MAP` **(I/O & Config Routines)** (Impact: 139.7)
    * *Intent:* /* CALL TIL R0019963 - SKRIV_FEIL_YP. I DE ANDRE */ /* LEGGES DE UT PÅ SKJERMBILDET (MAP S001U61) VE...
  * `OVERFØR_U3_SP_MAP` **(I/O & Config Routines)** (Impact: 137.9)
    * *Intent:* % PAGE; /* **************************************************************** */ /* */ /* PROSEDYRA OV...
  * `OVERFØR_U3_EØS_MAP` **(I/O & Config Routines)** (Impact: 58.3)
  * `OVERFØR_U3_YP_MAP` **(I/O & Config Routines)** (Impact: 57.7)
    * *Intent:* % PAGE; /* ***************************************************************** */ /* PROSEDYRA OVERFØR...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 325 instances
* *State Mutation (weighted view):* 1156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 130`, `func_start: 4`
* *Risk/State:* `state_mutation: 506`, `dead_code: 1`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.552
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.010541
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/GML/R001I201.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.09)
- **Top Global Matches:** file_cluster_8: 12.09, file_cluster_3: 12.639, file_cluster_6: 24.575
- **Magnitude:** 1540.36 | **LOC:** 3027 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%), Complexity Load (formerly Cognitive Load) (58.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SKRIV_INNT` **(Many-Argument Workhorses)** (Impact: 91.0)
    * *Intent:* /* **************************************************************** */00026400 /* */00026410 /* PROC...
  * `OVERFØR_INNTEKTER` **(Many-Argument Workhorses)** (Impact: 65.8)
  * `R001I20` **(Many-Argument Workhorses)** (Impact: 58.1)
  * `FLYTT_DBOPPL_TIL_BL_OMR_FRAFNR` **(I/O & Config Routines)** (Impact: 40.6)
  * `BEHANDLE_MARKERTE_LINJER` **(I/O & Config Routines)** (Impact: 37.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 941
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 289`, `args: 5`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 737`, `dead_code: 6`
* *Architecture:* `io: 19`, `api: 1`, `import: 18`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.000127 | `Ripple Effect (Closeness):` 0.001874
  * `Imports (Out-Degree: 6):` DLIUIB, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912, P0019921...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GML/R0010480.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.935)
- **Top Global Matches:** file_cluster_8: 7.935, file_cluster_6: 15.41, file_cluster_3: 23.378
- **Magnitude:** 1469.5 | **LOC:** 3976 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **49**; blast radius 0.479; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.9%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P40_OVERFØR_TIL_BLANKETT` **(I/O & Config Routines)** (Impact: 74.0)
  * `FLYTT_BASEDATA_TIL_BILDE_OMR` **(I/O & Config Routines)** (Impact: 62.8)
  * `R001048` **(Many-Argument Workhorses)** (Impact: 60.4)
  * `OVER_OG_UT` **(Compute Cores)** (Impact: 34.2)
  * `FLYTT_DBOPPL_TIL_BL_OMR_REGDATO` **(I/O & Config Routines)** (Impact: 28.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 768
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 415`, `args: 3`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 526`, `dead_code: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 1`, `import: 50`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.479
  * `Choke Point (Betweenness):` 0.00388 | `Ripple Effect (Closeness):` 0.016083
  * `Imports (Out-Degree: 37):` DLIUIB, P0012001, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/R0019E04.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.879)
- **Top Global Matches:** file_cluster_6: 8.879, file_cluster_4: 12.133, file_cluster_8: 17.073
- **Magnitude:** 1338.82 | **LOC:** 4669 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.424; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%), Complexity Load (formerly Cognitive Load) (51.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FNR_SKAL_ENDRES` **(I/O & Config Routines)** (Impact: 91.2)
  * `TRANHIST_TILKN` **(I/O & Config Routines)** (Impact: 88.8)
  * `R0019E4` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* /* INPUT-DATSETTET ER VSAM-FILEN P001.FNRTILG OG RF-BASEN */ /* OUTPUT ER VSAMFILEN P001.FNRENDR, */...
  * `OMREGN` **(I/O & Config Routines)** (Impact: 52.5)
  * `DØD` **(I/O & Config Routines)** (Impact: 41.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 525`, `args: 2`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 427`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 38`, `api: 1`, `import: 51`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` DLIUIB, P0010601, P0012002, P0012003, P0014009, P0019014, P0019906, P0019908...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/R0019E01.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.727)
- **Top Global Matches:** file_cluster_6: 8.727, file_cluster_4: 11.04, file_cluster_9: 16.314
- **Magnitude:** 1327.08 | **LOC:** 4493 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **49**; blast radius 0.506; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.0%), Complexity Load (formerly Cognitive Load) (45.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FNR_SKAL_ENDRES` **(I/O & Config Routines)** (Impact: 91.2)
  * `TRANHIST_TILKN` **(I/O & Config Routines)** (Impact: 88.8)
  * `R0019E` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* /* OUTPUT ER VSAMFILEN P001.FNRENDR, */ /* VSAMFILEN P001.MELD.TRANS, */ /* OPPDATERT RF-BASE, */ /*...
  * `OMREGN` **(I/O & Config Routines)** (Impact: 52.5)
  * `DØD` **(I/O & Config Routines)** (Impact: 41.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 522`, `args: 2`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 439`, `dead_code: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 30`, `api: 1`, `import: 55`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.506
  * `Choke Point (Betweenness):` 0.000415 | `Ripple Effect (Closeness):` 0.015301
  * `Imports (Out-Degree: 11):` DFHBMSCA, DLIUIB, P0012002, P0012003, P0014009, P0019014, P0019906, P0019908...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/R0017041.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.087)
- **Top Global Matches:** file_cluster_1: 5.087, file_cluster_3: 48.204, file_cluster_8: 70.06
- **Magnitude:** 1227.4 | **LOC:** 2134 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.444; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (59.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLASSER_TEKSTTYPE_A_KODE` **(Many-Argument Workhorses)** (Impact: 816.5)
    * *Intent:* /*IDENTIFIKASJON: */ /* R0017041 - PROSEDYRE I PLI */ /* PROGRAMMERER: JAN, DESEMBER 82 */ /*HENSIKT...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 114`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 150`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012249
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GML/R001U606.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.271)
- **Top Global Matches:** file_cluster_1: 6.271, file_cluster_3: 48.31, file_cluster_8: 70.115
- **Magnitude:** 1206.7 | **LOC:** 1326 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.721; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_U3_SP_MAP` **(I/O & Config Routines)** (Impact: 182.9)
    * *Intent:* % PAGE; 00005120 /* **************************************************************** */00005130 /* *...
  * `OVERFØR_U3_SØKER_MAP` **(I/O & Config Routines)** (Impact: 136.9)
    * *Intent:* /* CALL TIL R0019963 - SKRIV_FEIL_YP. I DE ANDRE */ 00000600 /* LEGGES DE UT PÅ SKJERMBILDET (MAP S0...
  * `OVERFØR_U3_YP_MAP` **(I/O & Config Routines)** (Impact: 57.6)
    * *Intent:* % PAGE; 00011230 /* ***************************************************************** */00011240 /* ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 205 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 116`, `func_start: 3`
* *Risk/State:* `state_mutation: 390`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.721
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.012254
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/GML/R0019E04.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.161)
- **Top Global Matches:** file_cluster_6: 8.161, file_cluster_4: 11.515, file_cluster_8: 16.718
- **Magnitude:** 1203.92 | **LOC:** 4517 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.502; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FNR_SKAL_ENDRES` **(I/O & Config Routines)** (Impact: 93.5)
  * `R0019E4` **(Many-Argument Workhorses)** (Impact: 72.1)
  * `TRANHIST_TILKN` **(I/O & Config Routines)** (Impact: 69.8)
  * `OMREGN` **(I/O & Config Routines)** (Impact: 50.5)
  * `DØD` **(I/O & Config Routines)** (Impact: 44.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 497`, `args: 2`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 363`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 38`, `api: 1`, `import: 44`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.502
  * `Choke Point (Betweenness):` 0.000198 | `Ripple Effect (Closeness):` 0.014524
  * `Imports (Out-Degree: 8):` DLIUIB, P0010601, P0012002, P0012003, P0014009, P0019014, P0019906, P0019908...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/R001U806.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.074)
- **Top Global Matches:** file_cluster_1: 6.074, file_cluster_3: 48.28, file_cluster_8: 70.09
- **Magnitude:** 1154.24 | **LOC:** 1323 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.54; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_EE_SØKER_MAP` **(I/O & Config Routines)** (Impact: 97.3)
    * *Intent:* /* ***************************************************************** */ /* FEILMELDINGER: */ /* ----...
  * `OVERFØR_EE_EØS_MAP` **(I/O & Config Routines)** (Impact: 90.9)
    * *Intent:* /* ----------------------------------------------------------------- */
  * `OVERFØR_EE_YP_MAP` **(I/O & Config Routines)** (Impact: 57.2)
    * *Intent:* /* ----------------------------------------------------------------- */
  * `OVERFØR_EE_SP_SØKER_MAP` **(I/O & Config Routines)** (Impact: 40.4)
    * *Intent:* /* ----------------------------------------------------------------- */
  * `OVERFØR_EE_SP_AVDØD_MAP` **(I/O & Config Routines)** (Impact: 39.5)
    * *Intent:* /* ----------------------------------------------------------------- */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 805
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 110`, `func_start: 5`
* *Risk/State:* `state_mutation: 349`, `dead_code: 3`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.54
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.010541
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/R0011006.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 17.43)
- **Top Global Matches:** file_cluster_1: 17.43, file_cluster_3: 31.889, file_cluster_8: 53.578
- **Magnitude:** 1145.12 | **LOC:** 1019 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.542; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_FB_FAR_MAP` **(I/O & Config Routines)** (Impact: 61.0)
    * *Intent:* %PAGE; /* **************************************************************** */ /* */ /* PROSEDYREN OV...
  * `OVERFØR_FBY_MOR_MAP` **(I/O & Config Routines)** (Impact: 56.5)
    * *Intent:* %PAGE; /* *************************************************************** */ /* */ /* PROSEDYREN OVE...
  * `OVERFØR_FBY_FAR_MAP` **(I/O & Config Routines)** (Impact: 56.5)
    * *Intent:* %PAGE; /* *************************************************************** */ /* */ /* PROSEDYREN OVE...
  * `INTERN_OVERFØR_BARN` **(I/O & Config Routines)** (Impact: 52.7)
  * `OVERFØR_FB_MOR_MAP` **(I/O & Config Routines)** (Impact: 42.6)
    * *Intent:* %PAGE; /* **************************************************************** */ /* */ /* PROSEDYREN OV...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 92`, `func_start: 6`
* *Risk/State:* `state_mutation: 361`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.010541
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/GML/R001U806.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.279)
- **Top Global Matches:** file_cluster_1: 6.279, file_cluster_3: 48.307, file_cluster_8: 70.111
- **Magnitude:** 1127.24 | **LOC:** 1263 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.661; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_EE_SP_MAP` **(I/O & Config Routines)** (Impact: 189.2)
    * *Intent:* % PAGE; 00004030 /* **************************************************************** */00004040 /* *...
  * `OVERFØR_EE_SØKER_MAP` **(I/O & Config Routines)** (Impact: 99.2)
    * *Intent:* /* CALL TIL R0019963 - SKRIV_FEIL_YP. I DE ANDRE */ 00000460 /* LEGGES DE UT PÅ SKJERMBILDET (MAP S0...
  * `OVERFØR_EE_YP_MAP` **(I/O & Config Routines)** (Impact: 57.6)
    * *Intent:* % PAGE; 00010600 /* ***************************************************************** */00010610 /* ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 188 instances
* *State Mutation (weighted view):* 753
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 109`, `func_start: 3`
* *Risk/State:* `state_mutation: 377`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.661
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.011958
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/R001I301.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.379)
- **Top Global Matches:** file_cluster_3: 10.379, file_cluster_8: 14.885, file_cluster_6: 27.501
- **Magnitude:** 1096.9 | **LOC:** 2214 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.469; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SKRIV_INNT` **(Compute Cores)** (Impact: 53.9)
  * `R001I30` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /* */ /*ENDRET: 06.04.88 AV SVERRE LUNDEBY, DATA-UTVIKLING A/S */ /* ****** */ /* INITIERER BRUKERID...
  * `FLYTT_DBOPPL_TIL_BL_OMR_FRAFNR` **(I/O & Config Routines)** (Impact: 42.9)
  * `BEHANDLE_MARKERTE_LINJER` **(I/O & Config Routines)** (Impact: 33.6)
  * `AKSJON_BEHANDLING` **(I/O & Config Routines)** (Impact: 31.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 220`, `args: 3`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 518`, `dead_code: 7`
* *Architecture:* `io: 11`, `api: 1`, `import: 20`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.001215
  * `Imports (Out-Degree: 10):` DLIUIB, P0012002, P0012003, P0019906, P0019908, P0019910, P0019912, P0019921...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GML/R0010606.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.15)
- **Top Global Matches:** file_cluster_1: 6.15, file_cluster_3: 48.295, file_cluster_8: 70.103
- **Magnitude:** 1091.88 | **LOC:** 1205 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.538; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_UPSØKER_MAP` **(I/O & Config Routines)** (Impact: 113.5)
    * *Intent:* /* I PROSEDYREN OVERFØR_YP_MAP LEGGES FEILMELDINGER UT VED */ 00000640 /* CALL TIL R0019963 - SKRIV_...
  * `OVERFØR_UPBARN_MAP` **(I/O & Config Routines)** (Impact: 102.3)
    * *Intent:* /* ***************************************************************** */00006690 /* */00006700 /* OVE...
  * `OVERFØR_UPSPES_MAP` **(I/O & Config Routines)** (Impact: 83.4)
    * *Intent:* % PAGE; 00004290 /* **************************************************************** */00004300 /* *...
  * `OVERFØR_YP_MAP` **(I/O & Config Routines)** (Impact: 57.6)
    * *Intent:* % PAGE; 00010020 /* ***************************************************************** */00010030 /* ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 116`, `func_start: 4`
* *Risk/State:* `state_mutation: 311`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.012254
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/R0010606.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.148)
- **Top Global Matches:** file_cluster_1: 6.148, file_cluster_3: 48.294, file_cluster_8: 70.103
- **Magnitude:** 1091.86 | **LOC:** 1194 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.517; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OVERFØR_UPSØKER_MAP` **(I/O & Config Routines)** (Impact: 113.7)
    * *Intent:* /* I PROSEDYREN OVERFØR_YP_MAP LEGGES FEILMELDINGER UT VED */ 00000510 /* CALL TIL R0019963 - SKRIV_...
  * `OVERFØR_UPBARN_MAP` **(I/O & Config Routines)** (Impact: 102.3)
    * *Intent:* /* ***************************************************************** */00006580 /* */00006590 /* OVE...
  * `OVERFØR_UPSPES_MAP` **(I/O & Config Routines)** (Impact: 83.4)
    * *Intent:* % PAGE; 00004180 /* **************************************************************** */00004190 /* *...
  * `OVERFØR_YP_MAP` **(I/O & Config Routines)** (Impact: 57.6)
    * *Intent:* % PAGE; 00009910 /* ***************************************************************** */00009920 /* ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 116`, `func_start: 4`
* *Risk/State:* `state_mutation: 311`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.517
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.010541
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/GML/R001UJ02.pli` (PLI) | Magnitude: 61.8 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 58, state_mutation: 50, structural_boundaries: 7, func_start: 3
- `src/GML/R0010502.pli` (PLI) | Magnitude: 91.12 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 65, structural_boundaries: 12, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/GML/R001NRCO.pli` (PLI) | Magnitude: 7.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 5, core_var_decl: 3, design_upper_case: 3
- `src/GML/R001NACO.pli` (PLI) | Magnitude: 7.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 5, core_var_decl: 3, design_upper_case: 3
- `src/GML/R001NAPL.pli` (PLI) | Magnitude: 8.04 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 5, core_var_decl: 3, design_upper_case: 3
- `src/GML/R001NRPL.pli` (PLI) | Magnitude: 8.04 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 5, core_var_decl: 3, design_upper_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/R0019923.pli` (PLI) | Magnitude: 15.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 4, branch: 3, structural_boundaries: 3
- `src/GML/R0019901.pli` (PLI) | Magnitude: 6.58 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, branch: 2, core_var_decl: 2
- `src/R0019988.pli` (PLI) | Magnitude: 14.38 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 8, core_var_decl: 4, design_upper_case: 4
- `src/GML/R0019948.pli` (PLI) | Magnitude: 14.18 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, branch: 3, core_var_decl: 3
- `src/R0019948.pli` (PLI) | Magnitude: 14.18 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, branch: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/GML/R0016051.pli` (PLI) | Magnitude: 16.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 7, core_var_decl: 5, design_upper_case: 5
- `src/GML/R0017201.pli` (PLI) | Magnitude: 36.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 19, structural_boundaries: 9, branch: 4
- `src/R0017034.pli` (PLI) | Magnitude: 39.06 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 26, core_var_decl: 7, design_upper_case: 7
- `src/R0019990.pli` (PLI) | Magnitude: 14.42 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 8, core_var_decl: 4, design_upper_case: 4
- `src/GML/R0017301.pli` (PLI) | Magnitude: 41.78 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 22, structural_boundaries: 9, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/R0015501.pli` (PLI) | Magnitude: 294.74 | Delta: **0.234** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 707, structural_boundaries: 123, core_var_decl: 103, design_upper_case: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/GML/R001TK09.pli` (PLI) | Magnitude: 879.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1743, state_mutation: 327, core_var_decl: 283, design_upper_case: 283
- `src/R001TK09.pli` (PLI) | Magnitude: 879.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1743, state_mutation: 327, core_var_decl: 283, design_upper_case: 283

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/GML/R001I301.pli` (PLI) | Magnitude: 1021.92 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 2138, state_mutation: 474, branch: 223, structural_boundaries: 222

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/GML/R001UJ05.pli` (PLI) | Magnitude: 75.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 152, state_mutation: 29, structural_boundaries: 27, core_var_decl: 24
- `src/GML/R0015602.pli` (PLI) | Magnitude: 42.92 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 238, structural_boundaries: 26, core_var_decl: 14, design_upper_case: 14
- `src/R0015602.pli` (PLI) | Magnitude: 41.8 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 27, core_var_decl: 14, design_upper_case: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/GML/R0010401.pli` -> **Severity: 2.343** (Bridge: 0.0242 * Flux: 96.7269%)
- `src/R0010301.pli` -> **Severity: 1.751** (Bridge: 0.0175 * Flux: 100.0%)
- `src/R0010426.pli` -> **Severity: 1.707** (Bridge: 0.0171 * Flux: 99.9446%)
- `src/GML/R0012001.pli` -> **Severity: 1.552** (Bridge: 0.0243 * Flux: 63.8242%)
- `src/R001NO10.pli` -> **Severity: 1.425** (Bridge: 0.0142 * Flux: 99.9987%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/R0019944.pli` -> **Severity: 3.291** (Embedded: 0.0476 * Error Risk: 69.1085%)
- `src/R0010301.pli` -> **Severity: 2.818** (Embedded: 0.0379 * Error Risk: 74.4382%)
- `src/G0019999.pli` -> **Severity: 2.773** (Embedded: 0.0385 * Error Risk: 72.1171%)
- `src/R0019905.pli` -> **Severity: 2.703** (Embedded: 0.0446 * Error Risk: 60.5532%)
- `src/R0019921.pli` -> **Severity: 2.658** (Embedded: 0.0434 * Error Risk: 61.2336%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/GML/R0019906.pli` -> **Severity: 1773.3** (Blast Radius: 17.733 * Doc Risk: 100.0%)
- `src/GML/R0019921.pli` -> **Severity: 1674.8** (Blast Radius: 16.748 * Doc Risk: 100.0%)
- `src/R0019921.pli` -> **Severity: 1593.1** (Blast Radius: 15.931 * Doc Risk: 100.0%)
- `src/GML/R0019944.pli` -> **Severity: 1393.8** (Blast Radius: 13.938 * Doc Risk: 100.0%)
- `src/R0019944.pli` -> **Severity: 1282.0** (Blast Radius: 12.82 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `1479` files carry mainframe facts -- `10088` call sites, `22` dataset bindings, `29958` record items.

- **CICS operations:** `3251` EXEC CICS operations naming a resource (`810` FILE, `2421` MAP, `20` QUEUE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `167` commands (`145` DELAY, `22` POST); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `src/R0010410.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `RETURN TRANSID TRANS_OPPL_OMR.TRANSKODE`, `CALL PLITDLI`, `XCTL R0010301`, `LINK R0019906`, `LINK R0015201`, `LINK R0010411`, `XCTL R0010412`, `LINK R0013110`
- **COMMAREA passed:** `RETURN TRANSID TRANS_OPPL_OMR.TRANSKODE ← KOM_OMR`, `XCTL R0010301 ← KOM_OMR`, `LINK R0019906 ← FNR_REG`, `LINK R0015201 ← KOM_OMR`, `LINK R0010411 ← LOKAL_KOM_OMR`, `XCTL R0010412 ← LOKAL_KOM_OMR`, `LINK R0013110 ← KOM_OMR`
- **Record layouts (183 items):** `W01_DLI_PARAM (7)`, `SSA1_RF0PERSN (5)`, `FNR_REG (4)`, `B01 (1)`, `B02 (1)`, `RF1 (1)`, `W01_PSB_NAVN (1)`, `W01_PINT_AKT (1)`, `W01_PINT_UT (1)`, `W01_IO (1)`, `SSA_UQUAL (1)`, `QUENAME (1)` … (+158 more)
- **CICS operations:** `QUEUE QUENAME? (delete/read/write)`, `MAP BLANKL (write)`, `MAP UTLINJE (write)`, `MAP UTLS (write)`, `MAP GENHEAD (write)`, `MAP S001042 (write)`, `MAP INTHEAD (write)`, `MAP MORFAR (write)`, `MAP INNTEKT (write)`, `MAP ROTMENY (write)`, `MAP STATUS (write)`, `MAP TILKN (write)` … (+16 more)
- **Data moves:** 1649 (ASSIGN 1649); most-fed items `UTLINJEO.ANDREO`, `SUM_BRUTTO`, `SUM_NETTO`, `UTLINJEO.FØRSTEO`, `BR_F`, `PIC_ZZ9`
- **Unit of work:** `0` commit / `0` rollback points; handlers `OVERFLOW->OVERFLOW`, `SIGNAL->OVERFLOW`; `0/1` RESP results tested

### `src/R0014901.pli` (PLI)
- **Calls:** `LINK R0014001`, `LINK R0017001`, `LINK R0016001`, `CALL UFØREPENSJON_OPPHØRER`, `CALL ETTERLATTEPENSJON_OPPHØRER`, `CALL AFP_NULL_OPPHØRER`, `CALL LEGG_UFØREHIST_I_TAB`, `CALL OPPHØR_KOBLING_TO_PERSONER`, `CALL RULL_FORVENTET`, `CALL RULL_FAI`
- **COMMAREA passed:** `LINK R0014001 ← KOM_OMR`, `LINK R0017001 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`
- **Record layouts (156 items):** `FNR_R (5)`, `R_FNR (5)`, `ALDERSOMRÅDE (4)`, `TRANS_LISTE_OMR (2)`, `ALDERSOMRÅDE_DEF (2)`, `B00 (1)`, `B01 (1)`, `B01_HJELP (1)`, `B02 (1)`, `B02_HJELP (1)`, `WORK_TRANS_LISTE (1)`, `COMMAREA_PEKER (1)` … (+131 more)
- **Data moves:** 1207 (ASSIGN 1207); most-fed items `HENDELSE_IND`, `B02.STATUS.VIRK_DATO_ÅMD`, `TRANS_OPPL_OMR.VIRKNINGSDATO_ÅMD`, `SØKER_IND`, `TRANS_OPPL_OMR.FØDSNUMMER`, `I`

### `src/R001I903.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `RETURN TRANSID TRANSKODE`, `LINK R0019906`, `LINK R0019921`
- **COMMAREA passed:** `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0019906 ← FNR_REG`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (173 items):** `TRANS_OMR (20)`, `TRANS_LISTE_OMR (20)`, `TRANS_SAVE_OMR (20)`, `REC_OMR (20)`, `NYKKEL (11)`, `FNR (6)`, `DATO_REDEF (4)`, `HDATO_REDEF (4)`, `FNR_REG (4)`, `FEIL_STRUC (4)`, `TID (3)`, `INNT_RAPP (1)` … (+56 more)
- **CICS operations:** `MAP S001I09 (read/write)`, `MAP S001012 (write)`, `FILE LIKNING (read)`, `FILE STRYK (read)`, `FILE INBRUDD (write)`, `FILE OLBRUDD (write)`
- **CICS task control:** `DELAY`
- **Data moves:** 1136 (ASSIGN 1136); most-fed items `INNTEKT.FNR`, `INNTEKT.AGIVKODE`, `INNTEKT.ART`, `INNTEKT.ETYPE`, `INNTEKT.KOMMNR`, `INNTEKT.MERKE`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ERROR->FEILBEH`, `ERROR->ABEND`, `NOTFND->NOTFND1`, `NOTFND->ALT_OK1`; `0/0` RESP results tested

### `src/GML/R001I903.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `RETURN TRANSID TRANSKODE`, `LINK R0019906`, `LINK R0019921`
- **COMMAREA passed:** `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0019906 ← FNR_REG`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (171 items):** `TRANS_OMR (20)`, `TRANS_LISTE_OMR (20)`, `TRANS_SAVE_OMR (20)`, `REC_OMR (20)`, `NYKKEL (11)`, `FNR (6)`, `DATO_REDEF (4)`, `HDATO_REDEF (4)`, `FNR_REG (4)`, `FEIL_STRUC (4)`, `TID (3)`, `INNT_RAPP (1)` … (+54 more)
- **CICS operations:** `MAP S001I09 (read/write)`, `MAP S001012 (write)`, `FILE KOMTAB (read)`, `FILE STRYK (read)`, `FILE INBRUDD (write)`, `FILE OLBRUDD (write)`
- **CICS task control:** `DELAY`
- **Data moves:** 1134 (ASSIGN 1134); most-fed items `INNTEKT.FNR`, `INNTEKT.AGIVKODE`, `INNTEKT.ART`, `INNTEKT.ETYPE`, `INNTEKT.KOMMNR`, `INNTEKT.MERKE`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ERROR->FEILBEH`, `ERROR->ABEND`, `NOTFND->NOTFND1`, `NOTFND->ALT_OK1`; `0/0` RESP results tested

### `src/GML/R0014901.pli` (PLI)
- **Calls:** `LINK R0014001`, `LINK R0017001`, `LINK R0016001`, `CALL ETTERLATTEPENSJON_OPPHØRER`, `CALL AFP_NULL_OPPHØRER`, `CALL OPPHØR_KOBLING_TO_PERSONER`, `CALL RULL_FORVENTET`, `CALL RULL_FAI`
- **COMMAREA passed:** `LINK R0014001 ← KOM_OMR`, `LINK R0017001 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`
- **Record layouts (131 items):** `FNR_R (6)`, `R_FNR (6)`, `ALDERSOMRÅDE (4)`, `TRANS_LISTE_OMR (2)`, `ALDERSOMRÅDE_DEF (2)`, `B01 (1)`, `B02 (1)`, `WORK_TRANS_LISTE (1)`, `B01_HJELP (1)`, `B02_HJELP (1)`, `COMMAREA_PEKER (1)`, `START_TRANS_OPPL_PEKER (1)` … (+104 more)
- **Data moves:** 1003 (ASSIGN 1003); most-fed items `HENDELSE_IND`, `B02.STATUS.VIRK_DATO_ÅM`, `SØKER_IND`, `TRANS_OPPL_OMR.VIRKNINGSDATO`, `TRANS_OPPL_OMR.FØDSNUMMER`, `I`

### `src/GML/R0010410.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `RETURN TRANSID TRANS_OPPL_OMR.TRANSKODE`, `CALL PLITDLI`, `XCTL R0010301`, `LINK R0019906`, `LINK R0015201`, `LINK R0010411`, `XCTL R0010412`, `LINK R0013110`
- **COMMAREA passed:** `RETURN TRANSID TRANS_OPPL_OMR.TRANSKODE ← KOM_OMR`, `XCTL R0010301 ← KOM_OMR`, `LINK R0019906 ← FNR_REG`, `LINK R0015201 ← KOM_OMR`, `LINK R0010411 ← LOKAL_KOM_OMR`, `XCTL R0010412 ← LOKAL_KOM_OMR`, `LINK R0013110 ← KOM_OMR`
- **Record layouts (138 items):** `W01_DLI_PARAM (7)`, `SSA1_RF0PERSN (5)`, `FNR_REG (4)`, `B01 (1)`, `B02 (1)`, `RF1 (1)`, `W01_PSB_NAVN (1)`, `W01_PINT_AKT (1)`, `W01_PINT_UT (1)`, `W01_IO (1)`, `SSA_UQUAL (1)`, `QUENAME (1)` … (+113 more)
- **CICS operations:** `QUEUE QUENAME? (delete/read/write)`, `MAP BLANKL (write)`, `MAP UTLINJE (write)`, `MAP GENHEAD (write)`, `MAP S001042 (write)`, `MAP INTHEAD (write)`, `MAP MORFAR (write)`, `MAP INNTEKT (write)`, `MAP ROTMENY (write)`, `MAP STATUS (write)`, `MAP TILKN (write)`, `MAP FORSI (write)` … (+11 more)
- **Data moves:** 937 (ASSIGN 937); most-fed items `UTLINJEO.ANDREO`, `PIC_ZZZZ9`, `PIC_ZZ9`, `MAP_MELDING`, `PIC_9V99`, `PIC_11`
- **Unit of work:** `0` commit / `0` rollback points; handlers `OVERFLOW->OVERFLOW`, `SIGNAL->OVERFLOW`; `0/1` RESP results tested

### `src/R0010430.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `XCTL R0010301`, `XCTL R0010420`, `RETURN TRANSID TRANSKODE`, `LINK R0013110`, `LINK R0019906`, `CALL PLITDLI`
- **COMMAREA passed:** `XCTL R0010301 ← KOM_OMR`, `XCTL R0010420 ← KOM_OMR`, `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0013110 ← KOM_OMR`, `LINK R0019906 ← FNR_REG`
- **Record layouts (738 items):** `BOND_TX (19)`, `INT_VERIBLE (18)`, `L01_INNT_DEF (11)`, `W01 (11)`, `TKNR_REC (10)`, `CHARLIST2 (7)`, `LOKAL_OMR (7)`, `L01_TKNR_DEF (7)`, `DATO_DEF (6)`, `DF_PRINT_LINE (6)`, `L01_STATSBORGER_DEF (6)`, `L01_FNR_DEF (5)` … (+262 more)
- **CICS operations:** `MAP S001A81 (read/write)`, `FILE TKNRTAB (read)`, `FILE STATTAB (read)`, `FILE PRINTRX (write)`
- **Data moves:** 317 (ASSIGN 317); most-fed items `W_POENG`, `W_INNTEKT`, `S001A81O.CICS_INFOO`, `WÅRMND`, `MAP_MELDING`, `AYY_LINE`
- **Unit of work:** `0` commit / `0` rollback points; handlers `NOTFND->NOTFND_TK`, `IOERR->NOTFND_TK`, `SYSIDERR->NOTFND_TK`, `NOTFND->NOTFND_ST`; `0/0` RESP results tested

### `src/GML/R0010430.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `XCTL R0010301`, `XCTL R0010420`, `RETURN TRANSID TRANSKODE`, `LINK R0013110`, `LINK R0019906`, `CALL PLITDLI`
- **COMMAREA passed:** `XCTL R0010301 ← KOM_OMR`, `XCTL R0010420 ← KOM_OMR`, `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0013110 ← KOM_OMR`, `LINK R0019906 ← FNR_REG`
- **Record layouts (736 items):** `BOND_TX (19)`, `INT_VERIBLE (18)`, `L01_INNT_DEF (11)`, `W01 (11)`, `TKNR_REC (10)`, `CHARLIST2 (7)`, `LOKAL_OMR (7)`, `L01_TKNR_DEF (7)`, `DATO_DEF (6)`, `DF_PRINT_LINE (6)`, `L01_STATSBORGER_DEF (6)`, `L01_FNR_DEF (5)` … (+262 more)
- **CICS operations:** `MAP S001A43 (read/write)`, `FILE TKNRTAB (read)`, `FILE STATTAB (read)`, `FILE PRINTRX (write)`
- **Data moves:** 322 (ASSIGN 322); most-fed items `W_POENG`, `W_INNTEKT`, `MAP_MELDING`, `WÅRMND`, `AYY_LINE`, `DF_LINE`
- **Unit of work:** `0` commit / `0` rollback points; handlers `NOTFND->NOTFND_TK`, `IOERR->NOTFND_TK`, `SYSIDERR->NOTFND_TK`, `NOTFND->NOTFND_ST`; `0/0` RESP results tested

### `src/R001I201.pli` (PLI)
- **Calls:** `CALL DATABASE`, `LINK R001I601`, `XCTL R001I201`, `CALL PLITDLI`, `CALL OPPDATE_DR_INNTEKT`, `CALL OPPDATE_DR_FNR`, `CALL KONTROLL_ACF2`, `RETURN TRANSID TRANSKODE`, `LINK R0019921`
- **COMMAREA passed:** `LINK R001I601 ← KOM_OMR`, `XCTL R001I201 ← INTERN_KOM_OMR`, `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (159 items):** `OLI_OMR (21)`, `W01_DLI_PARAM (12)`, `W01 (10)`, `W03 (9)`, `FNRH (7)`, `SSA1_PINNTEKT (6)`, `SSA1_RF0PERSN (5)`, `FEIL_STRUC (4)`, `FNR_REG (4)`, `INTERN_KOM_OMR (4)`, `HDATO_REDEF (4)`, `DATO_REDEF (4)` … (+67 more)
- **CICS operations:** `MAP S001I02 (read/write)`, `MAP S001I01 (write)`, `FILE OLINNTE (write)`
- **Data moves:** 860 (ASSIGN 860); most-fed items `W02.TAB_PI`, `W02.TAB_PI_KODE`, `W02.TAB_PI_KOMMNR`, `W02.TAB_PI_RAPPDATO`, `W02.TAB_PI_ÅR`, `DB_STATUS_KODE`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ERROR->ERRBEH`, `ERROR->DEFAULT`, `ERROR->L125`, `DUPREC->ALT_OK`, `ERROR->L270`, `DUPREC->ALT_OK2`; `0/0` RESP results tested

### `src/GML/R001I201.pli` (PLI)
- **Calls:** `LINK R001I601`, `CALL P900_NOR_DATA`, `XCTL R001I201`, `CALL PLITDLI`, `RETURN TRANSID TRANSKODE`, `LINK R0019921`
- **COMMAREA passed:** `LINK R001I601 ← KOM_OMR`, `XCTL R001I201 ← INTERN_KOM_OMR`, `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (161 items):** `REC_OMR (21)`, `W01_DLI_PARAM (12)`, `NYKKEL (11)`, `W01 (10)`, `W03 (9)`, `SSA1_PINNTEKT (6)`, `SSA1_RF0PERSN (5)`, `FEIL_STRUC (4)`, `FNR_REG (4)`, `INTERN_KOM_OMR (4)`, `HDATO_REDEF (4)`, `DATO_REDEF (4)` … (+62 more)
- **CICS operations:** `MAP S001I02 (read/write)`, `MAP S001I01 (write)`, `FILE OLINNTE (write)`
- **Data moves:** 849 (ASSIGN 849); most-fed items `W02.TAB_PI`, `W02.TAB_PI_KODE`, `W02.TAB_PI_KOMMNR`, `W02.TAB_PI_RAPPDATO`, `W02.TAB_PI_ÅR`, `DB_STATUS_KODE`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ERROR->ERRBEH`, `ERROR->DEFAULT`, `ERROR->L125`, `DUPREC->ALT_OK`, `ERROR->L126`, `DUPREC->ALT_OK2`; `0/0` RESP results tested

### `src/GML/R001I501.pli` (PLI)
- **Calls:** `LINK R001I601`, `CALL P900_NOR_DATA`, `CALL PLITDLI`, `LINK R0015602`, `LINK R0019921`, `LINK R0013301`
- **COMMAREA passed:** `LINK R001I601 ← KOM_OMR`, `LINK R0015602 ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`, `LINK R0013301 ← KOM_OMR`
- **Record layouts (345 items):** `REC_OMR (20)`, `REC_OMR (20)`, `W01_DLI_PARAM (13)`, `REC_OMR (13)`, `SSA3_PINNTEKT (11)`, `NYKKEL (11)`, `NYKKEL (11)`, `SSA2_PINNTEKT (9)`, `REC_OMR (9)`, `W01 (7)`, `CHARLIST2 (7)`, `SSA1_PINNTEKT (6)` … (+130 more)
- **CICS operations:** `MAP S001I04 (read/write)`, `FILE KEYFIL (write)`, `FILE KOMP (write)`, `FILE FFUDATA (write)`, `FILE KOMTAB (read)`, `FILE OLINNTE (write)`
- **CICS task control:** `DELAY`
- **Data moves:** 594 (ASSIGN 594); most-fed items `UTLINJE1`, `DB_STATUS_KODE`, `FEIL_MELDING`, `KEY_PEKER`, `DATO_CHAR`, `REC_OMR.FNR`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ERROR->L110`, `DUPREC->ALT_OK`, `ERROR->L115`, `ERROR->L120`, `DUPREC->ALT_OK`, `ERROR->IKKE_FUNNET1`; `0/0` RESP results tested

### `src/R0019E01.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `XCTL R0010301`, `CALL PLITDLI`, `XCTL R0019E01`, `LINK R0013101`, `LINK R0014901`, `CALL OMREGNING_PGA_FNRENDRING`, `LINK R0016001`, `LINK R0015401`
- **COMMAREA passed:** `XCTL R0010301 ← KOM_OMR`, `XCTL R0019E01 ← KOM_OMR`, `LINK R0013101 ← KOM_OMR`, `LINK R0014901 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`, `LINK R0015401 ← KOM_OMR`
- **Record layouts (284 items):** `MELD_IO (15)`, `W01_DLI_PARAM (14)`, `FNRREC (8)`, `SSA5_TRANHIST (6)`, `ENDR_DSR (6)`, `FØD13_DEF (6)`, `FØD13_DEF (6)`, `SSA1_RF0PERSN (5)`, `SSA2_RF0PERSN (5)`, `SSA3_RF0PERSN (5)`, `SSA3_TILKN (5)`, `SSA3_STATUS (5)` … (+186 more)
- **CICS operations:** `MAP S0019E1 (read/write)`, `FILE FNRTILG (browse/read)`, `FILE ENDRDSR (write)`, `FILE MELDREC (write)`, `FILE FNRFEIL (write)`
- **Data moves:** 629 (ASSIGN 629); most-fed items `DB_STATUS_KODE`, `TRANHIST_ENDRET`, `FEIL_MELD`, `FEIL_MELDING`, `TRANS_OPPL_OMR.FØDSNUMMER`, `WORK_DATO_ÅR_MND`
- **Unit of work:** `1` commit / `1` rollback points; handlers `ERROR->FEILBEH`, `ERROR->ABEND`; `0/0` RESP results tested

### `src/R0019E04.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `CALL PLITDLI`, `LINK R0013101`, `LINK R0014901`, `CALL OMREGNING_PGA_FNRENDRING`, `LINK R0016001`, `LINK R0015401`, `LINK R0019921`
- **COMMAREA passed:** `LINK R0013101 ← KOM_OMR`, `LINK R0014901 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`, `LINK R0015401 ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (289 items):** `MELD_IO (15)`, `W01_DLI_PARAM (14)`, `FNRREC (8)`, `ROUTLISTE (7)`, `SSA5_TRANHIST (6)`, `TEST_OMR (6)`, `ENDR_DSR (6)`, `FØD13_DEF (6)`, `FØD13_DEF (6)`, `SSA1_RF0PERSN (5)`, `SSA2_RF0PERSN (5)`, `SSA3_RF0PERSN (5)` … (+176 more)
- **CICS operations:** `FILE FNRTILG (browse/read)`, `FILE OMRFEIL (write)`, `FILE ENDRDSR (write)`, `FILE MELDREC (write)`
- **Data moves:** 615 (ASSIGN 615); most-fed items `DB_STATUS_KODE`, `TRANHIST_ENDRET`, `W01_UTLINJE`, `TRANS_OPPL_OMR.FØDSNUMMER`, `WORK_DATO_ÅR_MND`, `W01_HJELPE_IO`
- **Unit of work:** `1` commit / `0` rollback points; handlers `ENDFILE->ENDINP`, `ERROR->ERRBEH`, `NOTFND->L015NOTF`, `ERROR->DEFAULT`; `0/0` RESP results tested

### `src/GML/R0017044.pli` (PLI)
- **Record layouts (40 items):** `IND (1)`, `W_VIRK (1)`, `IND_EK (1)`, `F_NUM (1)`, `F_NUM_EK (1)`, `F_AAR (1)`, `F_ÅM (1)`, `F_ÅM_EK (1)`, `UFØR_ALDER (1)`, `HJ_VIRK_DATO_ÅM (1)`, `VIRK_DATO_Å (1)`, `VIRK_DATO_M (1)` … (+28 more)
- **Data moves:** 893 (ASSIGN 893); most-fed items `J`, `UFØR_ALDER_DØD`, `SISTE`, `UFØR_ALDER`, `ALDER`, `F_NUM`

### `src/GML/R0019E04.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `CALL PLITDLI`, `LINK R0013101`, `LINK R0014901`, `CALL OMREGNING_PGA_FNRENDRING`, `LINK R0016001`, `LINK R0015401`, `LINK R0019921`
- **COMMAREA passed:** `LINK R0013101 ← KOM_OMR`, `LINK R0014901 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`, `LINK R0015401 ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`
- **Record layouts (266 items):** `MELD_IO (15)`, `W01_DLI_PARAM (14)`, `FNRREC (8)`, `ROUTLISTE (7)`, `SSA5_TRANHIST (6)`, `TEST_OMR (6)`, `ENDR_DSR (6)`, `SSA1_RF0PERSN (5)`, `SSA2_RF0PERSN (5)`, `SSA3_RF0PERSN (5)`, `SSA3_TILKN (5)`, `SSA3_STATUS (5)` … (+163 more)
- **CICS operations:** `FILE FNRTILG (browse/read)`, `FILE OMRFEIL (write)`, `FILE ENDRDSR (write)`, `FILE MELDREC (write)`
- **Data moves:** 584 (ASSIGN 584); most-fed items `DB_STATUS_KODE`, `TRANHIST_ENDRET`, `W01_UTLINJE`, `WORK_DATO`, `TRANS_OPPL_OMR.FØDSNUMMER`, `W01_HJELPE_IO`
- **Unit of work:** `1` commit / `0` rollback points; handlers `ENDFILE->ENDINP`, `ERROR->ERRBEH`, `NOTFND->L015NOTF`, `ERROR->DEFAULT`; `0/0` RESP results tested

### `src/GML/R00149X1.pli` (PLI)
- **Calls:** `LINK R0014001`, `LINK R0017001`, `LINK R0016001`, `CALL ETTERLATTEPENSJON_OPPHØRER`, `CALL AFP_NULL_OPPHØRER`, `CALL OPPHØR_KOBLING_TO_PERSONER`
- **COMMAREA passed:** `LINK R0014001 ← KOM_OMR`, `LINK R0017001 ← KOM_OMR`, `LINK R0016001 ← KOM_OMR`
- **Record layouts (99 items):** `FNR_R (6)`, `ALDERSOMRÅDE (4)`, `TRANS_LISTE_OMR (2)`, `ALDERSOMRÅDE_DEF (2)`, `B01 (1)`, `B02 (1)`, `WORK_TRANS_LISTE (1)`, `B01_HJELP (1)`, `B02_HJELP (1)`, `COMMAREA_PEKER (1)`, `START_TRANS_OPPL_PEKER (1)`, `I (1)` … (+77 more)
- **Data moves:** 744 (ASSIGN 744); most-fed items `HENDELSE_IND`, `B02.STATUS.VIRK_DATO_ÅM`, `SØKER_IND`, `TRANS_OPPL_OMR.VIRKNINGSDATO`, `FIXED_DEC5`, `I`

### `src/R001I501.pli` (PLI)
- **Calls:** `LINK R001I601`, `CALL PLITDLI`, `CALL SKRIV_INNTEKT_TIL_DR`, `LINK R0019921`, `LINK R0013301`
- **COMMAREA passed:** `LINK R001I601 ← KOM_OMR`, `LINK R0019921 ← FEIL_STRUC`, `LINK R0013301 ← KOM_OMR`
- **Record layouts (257 items):** `OLI_OMR (20)`, `W01_DLI_PARAM (13)`, `KOM_OMR (13)`, `SSA3_PINNTEKT (11)`, `SSA2_PINNTEKT (9)`, `FFU_OMR (9)`, `W01 (7)`, `CHARLIST2 (7)`, `SSA1_PINNTEKT (6)`, `REC_OMR (6)`, `KOMMNR_OMR (6)`, `SSA1_RF0PERSN (5)` … (+97 more)
- **CICS operations:** `MAP S001I04 (read/write)`, `FILE KEYFIL (write)`, `FILE KOMP (write)`, `FILE FFUDATA (write)`, `FILE LIKNING (read)`, `FILE OLINNTE (write)`
- **CICS task control:** `DELAY`
- **Data moves:** 529 (ASSIGN 529); most-fed items `UTLINJE1`, `DB_STATUS_KODE`, `FEIL_MELDING`, `DATO_NUM`, `HDATO`, `W02_PI_MERKE`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ERROR->L117`, `DUPREC->ALT_OK`, `ERROR->L11X`, `ERROR->L120`, `DUPREC->ALT_OK`, `ERROR->IKKE_FUNNET1`; `0/0` RESP results tested

### `src/GML/R0010480.pli` (PLI)
- **Calls:** `CALL P9956_BER_G_CICS`, `XCTL R0010480`, `LINK R0019906`, `CALL PLITDLI`, `CALL P050_LES_AP_TRANS`, `CALL P050_LES_A1_TRANS`, `CALL P060_LES_UP_TRANS`, `CALL P060_LES_U2_TRANS`, `CALL P060_LES_U3_TRANS`, `CALL P183_LES_UF_TRANS`, `CALL P070_LES_US_TRANS`, `CALL P080_LES_EP_TRANS` … (+20)
- **COMMAREA passed:** `XCTL R0010480 ← KOM_OMR`, `LINK R0019906 ← FNR_REG`, `RETURN TRANSID TRANSKODE ← KOM_OMR`, `LINK R0010470 ← KOM_OMR`, `LINK R0013301 ← KOM_OMR`, `XCTL R0012001 ← KOM_OMR`
- **Record layouts (101 items):** `W01 (11)`, `W01_DLI_PARAM (11)`, `SSA3_TRANHIST (6)`, `SSA1_TRANHIST_CMD (5)`, `SSA1_VT0PERSN (5)`, `SSA1_TRANHIST (5)`, `FEIL_STRUC (4)`, `FNR_REG (4)`, `W01_DLI_PARAM (4)`, `W01_IDENT_DEF (3)`, `MAP_MELDING (1)`, `PLIXOPT (1)` … (+41 more)
- **CICS operations:** `MAP S001481 (read/write)`, `MAP S001482 (read/write)`, `MAP S001483 (read/write)`, `MAP S001484 (read/write)`, `MAP S00101E (write)`, `MAP S001014 (write)`, `MAP S001015 (write)`, `FILE FUNKTAD (read)`, `MAP S001I01 (write)`, `MAP S001013 (write)`, `MAP S001012 (write)`
- **Data moves:** 646 (ASSIGN 646); most-fed items `W01_HJELPE_IO`, `SEARCH_FNR`, `S001481O.CICS_INFOO`, `SSA1_TRANHIST.REGDATO`, `SSA3_TRANHIST.VTP_KEY`, `W_BLTYPE`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ERROR->FEILBEH`; `0/0` RESP results tested

### `src/R0017099.pli` (PLI)
- **Record layouts (38 items):** `IND (1)`, `W_VIRK (1)`, `IND_EK (1)`, `F_NUM13 (1)`, `F_NUM13_EK (1)`, `F_AAR (1)`, `F_ÅMD (1)`, `F_ÅMD_EK (1)`, `UFØR_ALDER (1)`, `HJ_VIRK_DATO_ÅMD (1)`, `VIRK_DATO_Å (1)`, `VIRK_DATO_M (1)` … (+26 more)
- **Data moves:** 795 (ASSIGN 795); most-fed items `J`, `UFØR_ALDER_DØD`, `SISTE`, `UFØR_ALDER`, `ALDER`, `F_NUM13`

### `src/GML/R001TK09.pli` (PLI)
- **Calls:** `XCTL PROGRAM_ID`, `CALL PLITDLI`
- **COMMAREA passed:** `XCTL PROGRAM_ID ← KOM_OMR`
- **Record layouts (95 items):** `SSA_TK (5)`, `SSA_TK2 (5)`, `TK_PCB_PEKERE (4)`, `FEIL_STRUC (4)`, `DLI_PARAM (4)`, `TK1 (1)`, `TK2 (1)`, `TK3 (1)`, `GU (1)`, `GN (1)`, `GHU (1)`, `GNP (1)` … (+66 more)
- **CICS operations:** `MAP S001019 (read/write)`, `MAP S001020 (read/write)`, `MAP S001022 (read/write)`
- **Data moves:** 660 (ASSIGN 660); most-fed items `HJ_TOTAL`, `HJ_SUM_K`, `HJ_SUM_M`, `HJ_KV_0_9`, `HJ_KV_10_19`, `HJ_KV_20_29`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ERROR->FEILBEH`; `0/0` RESP results tested

*(+1459 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 46% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: BMS map sources (2421 gaps); JCL and PROC libraries (129 gaps); CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (75 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6266 call pairs -- scoped 77.3%, unique 1.9%, ambiguous 11.7%, external 9.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| pli | 6261 | 77.3% | 1.9% | 11.7% | 9.1% |
| cobol | 5 | 40.0% | 0.0% | 0.0% | 60.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
