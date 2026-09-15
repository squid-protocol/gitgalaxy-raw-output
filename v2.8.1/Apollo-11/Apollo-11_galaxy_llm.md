# ARCHITECTURAL_BRIEF: Apollo-11
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/chrislgarry/Apollo-11` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 262 |
| Analyzed Artifacts (Scanned) | 246 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 74054 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 93.9% |
| Dominant Lang | AGC_ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| AGC_ASSEMBLY | 171 | 74054 | 69.5% |
| MARKDOWN | 74 | 0 | 30.1% |
| PLAINTEXT | 1 | 0 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z +2.60; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 33%, Interface Declarations Files 26%, I/O & Config Routines Files 23%, Large Core Modules 10%, Declarative / Non-Code 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 171 | 69.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 75 | 30.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.agc`: 1x Excluded (Lexical Monotony: High structural repetition detected in 3786 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2636 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3799 LOC)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lockb`: 1x Excluded (Unsupported Extension: '.lockb')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 61.3 | 24.4 | 22.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.0 | 68.6 | 72.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.0 | 29.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 35.5 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 44.8 | 3.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 31.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 80.4 | 98.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 12.7 | 1.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 99.2 | 61.2 | 81.2 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 50.0 | 38.4 | 43.6 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3918 | 145 | 38 | `Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc` |
| cleanup | 334 | 78 | 3 | `Luminary099/P20-P25.agc` |
| guards | 508 | 76 | 6 | `Luminary099/P20-P25.agc` |
| danger | 337 | 70 | 4 | `Luminary099/P20-P25.agc` |
| concurrency | 1347 | 111 | 15 | `Luminary099/P20-P25.agc` |
| connectivity | 1461 | 170 | 11 | `Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc` |
| io | 422 | 75 | 5 | `Luminary099/P51-P53.agc` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 236 | 72 | 3 | `Comanche055/P40-P47.agc` |
| tests | 32 | 15 | 0 | `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc` |
| docs | 4418 | 170 | 42 | `Luminary099/P20-P25.agc` |
| debt | 198 | 14 | 0 | `Comanche055/ASSEMBLY_AND_OPERATION_INFORMATION.agc` |
| mutation | 10780 | 163 | 99 | `Luminary099/INTERPRETER.agc` |
| dead_code | 1200 | 131 | 13 | `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` |
| credential | 0 | 0 | 0 | - |
| threat | 2118 | 140 | 22 | `Comanche055/INTERPRETER.agc` |
| ml_ai | 3688 | 87 | 42 | `Comanche055/CONIC_SUBROUTINES.agc` |
| ui | 15 | 4 | 0 | `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Luminary099/P51-P53.agc` (Hits: 21)
- `Comanche055/P61-P67.agc` (Hits: 20)
- `Luminary099/EXTENDED_VERBS.agc` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **P32-P33_P72-P73.agc** (`Comanche055/P32-P33_P72-P73.agc`) — 31 outbound dependencies
2. **PINBALL_GAME_BUTTONS_AND_LIGHTS.agc** (`Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc`) — 29 outbound dependencies
3. **CONTROLLED_CONSTANTS.agc** (`Luminary099/CONTROLLED_CONSTANTS.agc`) — 26 outbound dependencies
4. **P20-P25.agc** (`Comanche055/P20-P25.agc`) — 22 outbound dependencies
5. **P34-35_P74-75.agc** (`Comanche055/P34-35_P74-75.agc`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PLUSX` **(Many-Argument Workhorses)** (@ `Luminary099/P40-P47.agc`) -> Impact: **22.8** | LOC: 248
- `SIZETAB` **(Compute Cores)** (@ `Comanche055/RESTART_TABLES.agc`) -> Impact: **22.6** | LOC: 423
  * *Intent:* # RESTART 2CADR
- `CSISTEP` **(Compute Cores)** (@ `Comanche055/P32-P33_P72-P73.agc`) -> Impact: **21.9** | LOC: 297
- `P23` **(I/O & Config Routines)** (@ `Comanche055/P20-P25.agc`) -> Impact: **18.6** | LOC: 112
- `EJSCAN` **(Compute Cores)** (@ `Luminary099/EXECUTIVE.agc`) -> Impact: **18.3** | LOC: 54
- `PICAPAR` **(I/O & Config Routines)** (@ `Luminary099/P51-P53.agc`) -> Impact: **16.6** | LOC: 133
- `EJSCAN` **(Compute Cores)** (@ `Comanche055/EXECUTIVE.agc`) -> Impact: **16.5** | LOC: 48
- `PICAPAR` **(I/O & Config Routines)** (@ `Comanche055/P51-P53.agc`) -> Impact: **16.4** | LOC: 129
- `STORCMD` **(Compute Cores)** (@ `Comanche055/T4RUPT_PROGRAM.agc`) -> Impact: **15.9** | LOC: 40
- `CHECKALT` **(Compute Cores)** (@ `Luminary099/ASCENT_GUIDANCE.agc`) -> Impact: **15.9** | LOC: 120

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Comanche055` | 85 | 17046.78 | 23.2% | 40.72% |
| `Luminary099` | 88 | 16399.7 | 24.95% | 40.32% |
| `Translations` | 69 | 219.42 | 0.0% | 0.0% |
| `__monolith__` | 4 | 8.58 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Comanche055/ASSEMBLY_AND_OPERATION_INFORMATION.agc` -> **100.0%** Exposure
- `Comanche055/INTER-BANK_COMMUNICATION.agc` -> **100.0%** Exposure
- `Comanche055/TVCSTROKETEST.agc` -> **100.0%** Exposure
- `Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc` -> **100.0%** Exposure
- `Luminary099/INTER-BANK_COMMUNICATION.agc` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Comanche055/DOWN-TELEMETRY_PROGRAM.agc` -> **100.0%** Exposure
- `Comanche055/EXECUTIVE.agc` -> **100.0%** Exposure
- `Comanche055/INTER-BANK_COMMUNICATION.agc` -> **100.0%** Exposure
- `Comanche055/INTERPRETER.agc` -> **100.0%** Exposure
- `Comanche055/TVCEXECUTIVE.agc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Luminary099/DISPLAY_INTERFACE_ROUTINES.agc` -> **41** Orphaned Functions | **0** Duplicates
- `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` -> **40** Orphaned Functions | **0** Duplicates
- `Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc` -> **40** Orphaned Functions | **0** Duplicates
- `Comanche055/P40-P47.agc` -> **40** Orphaned Functions | **0** Duplicates
- `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` -> **38** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `681` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Comanche055/PHASE_TABLE_MAINTENANCE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **626.36**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.65)
- **Magnitude:** 157.38 | **LOC:** 417 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9989%), Tech Debt (99.4685%), Concurrency (86.2429%), Safety Score (85.1894%)
- **Heaviest Functions:** `SETUPDSP` (Many-Argument Workhorses, Impact: 7.7), `ONEORTWO` (Interface Declarations, Impact: 5.0), `BELOW2` (Interface Declarations, Impact: 4.9)

### 2. `Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **620.3**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.98)
- **Magnitude:** 554.38 | **LOC:** 1407 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9321%), Spec Match (95.4545%), Concurrency (83.9205%), Verification (80.0%)
- **Heaviest Functions:** `CHKCOMED` (Defensive Guards, Impact: 6.6), `OPTDATA` (Compute Cores, Impact: 6.4), `FINETIME` (Defensive Guards, Impact: 5.1)

### 3. `Luminary099/UPDATE_PROGRAM.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **612.99**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.09)
- **Magnitude:** 211.14 | **LOC:** 557 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9973%), Concurrency (99.7059%), Spec Match (95.2381%), Safety Score (84.7461%)
- **Heaviest Functions:** `LDLOOP72` (Compute Cores, Impact: 6.8), `DELTATOK` (Compute Cores, Impact: 5.6), `STORLP71` (Parameter Forwarders, Impact: 4.8)

### 4. `Comanche055/UPDATE_PROGRAM.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **612.15**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.55)
- **Magnitude:** 224.44 | **LOC:** 556 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9981%), Concurrency (99.628%), Spec Match (87.5%), Safety Score (85.522%)
- **Heaviest Functions:** `LDLOOP72` (Compute Cores, Impact: 6.9), `DELTATOK` (Compute Cores, Impact: 5.7), `STORLP71` (Parameter Forwarders, Impact: 4.8)

### 5. `Luminary099/PHASE_TABLE_MAINTENANCE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **585.86**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.69)
- **Magnitude:** 155.9 | **LOC:** 412 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9989%), Tech Debt (99.8499%), Spec Match (95.2381%), Safety Score (84.6482%)
- **Heaviest Functions:** `SETUPDSP` (Many-Argument Workhorses, Impact: 7.7), `ONEORTWO` (Interface Declarations, Impact: 5.0), `BELOW2` (Interface Declarations, Impact: 4.9)

### 6. `Luminary099/IMU_PERFORMANCE_TEST_2.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **581.78**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.98)
- **Magnitude:** 187.44 | **LOC:** 422 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9923%), Spec Match (93.9394%), Tech Debt (91.6761%), Safety Score (85.5137%)
- **Heaviest Functions:** `PIPJOBB` (I/O & Config Routines, Impact: 5.8), `FINETIME` (Defensive Guards, Impact: 5.1), `CHECKG1` (I/O & Config Routines, Impact: 4.3)

### 7. `Comanche055/P40-P47.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **580.53**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.78)
- **Magnitude:** 795.44 | **LOC:** 2430 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (99.9434%), State Flux (97.2318%), Spec Match (95.0%), Verification (80.0%)
- **Heaviest Functions:** `ENDV97E` (I/O & Config Routines, Impact: 14.5), `TOGETHER` (Compute Cores, Impact: 14.5), `RATEZRO` (Compute Cores, Impact: 12.5)

### 8. `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **578.93**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.03)
- **Magnitude:** 1585.62 | **LOC:** 3810 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9963%), Spec Match (98.6014%), Safety Score (85.6225%), Verification (80.0%)
- **Heaviest Functions:** `HMSOUT` (Compute Cores, Impact: 12.2), `NUM` (Compute Cores, Impact: 7.2), `HMSIN` (I/O & Config Routines, Impact: 6.5)

### 9. `Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **578.15**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.33)
- **Magnitude:** 412.28 | **LOC:** 1060 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (99.9865%), State Flux (98.9804%), Spec Match (96.9697%), Verification (80.0%)
- **Heaviest Functions:** `P40AUTO` (Compute Cores, Impact: 6.4), `CLOKJOB` (Compute Cores, Impact: 6.0), `IGNITE` (Defensive Guards, Impact: 4.1)

### 10. `Luminary099/AOTMARK.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **569.6**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.78)
- **Magnitude:** 288.16 | **LOC:** 696 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.8759%), Concurrency (98.2078%), Spec Match (97.6744%), Verification (80.0%)
- **Heaviest Functions:** `MARKRUPT` (Compute Cores, Impact: 8.4), `MKVAC` (I/O & Config Routines, Impact: 6.7), `FINDKEY` (Interface Declarations, Impact: 6.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *THE KEYBOARD AND DISPLAY SYSTEM PROGRAM OPERATES UNDER EXECUTIVE CONTROL AND PROCESSES INFORMATION EXCHANGED BETWEEN THE AGC AND THE COMPUTER OPERATOR. THE INPUTS TO THE PROGRAM ARE FROM THE KEYBOARD, FROM INTERNAL PROGRAM, AND FROM THE UPLINK.*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1585.62 | **LOC:** 3810 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.3799%), Tech Debt (28.5921%)
**Top Internal Functions/Classes:**
  * `HMSOUT` **(Compute Cores)** (Impact: 12.2)
  * `NUM` **(Compute Cores)** (Impact: 7.2)
  * `HMSIN` **(I/O & Config Routines)** (Impact: 6.5)
  * `ENTPASHI` **(Compute Cores)** (Impact: 6.3)
  * `DSPIN` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 163 instances
* *Concurrency (weighted view):* 135
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 775
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 1801`, `args: 128`, `func_start: 286`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 449`, `unreferenced_by_name: 38`
* *Architecture:* `io: 6`, `api: 12`, `concurrency: 35`, `import: 28`
* *Defense:* `safety: 23`, `doc: 96`, `test: 4`, `sync_locks: 23`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BLANKCON, COUNT, DOPROC, DSP2BIT, ENDALM, ENDBLFF, ENDBSUB1, ENDDPDEC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 2 BY P. VOLANTE*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1535.74 | **LOC:** 5183 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1986%), Tech Debt (33.1576%)
**Top Internal Functions/Classes:**
  * `R61LEM2` **(Defensive Guards)** (Impact: 11.9)
  * `CHKSRCH` **(Compute Cores)** (Impact: 11.7)
  * `REMODE` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* # RADMODES # # SUBROUTINES CALLED: # # RRTONLY, RRSONL, RMODINV (ACTUALLY PART OF) # # JOBS OR TASKS...
  * `DODES` **(I/O & Config Routines)** (Impact: 9.2)
    * *Intent:* # # SUBROUTINES CALLED: # # READCDUS, SMNB, CDULOGIC, MAGSUB, RROUT # Page 548 # # JOBS OR TASKS INI...
  * `RENDRAD` **(Many-Argument Workhorses)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 126 instances
* *Concurrency (weighted view):* 214
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 588
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 1591`, `args: 144`, `func_start: 226`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 336`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 38`
* *Architecture:* `io: 15`, `api: 12`, `concurrency: 79`, `import: 25`
* *Defense:* `safety: 44`, `doc: 239`, `test: 2`, `sync_locks: 44`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, F2DPS, FFTAG5, FFTAG6, LRS22, P20S, P20S1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1466.34 | **LOC:** 3076 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3446%), Tech Debt (28.5206%)
**Top Internal Functions/Classes:**
  * `MAXDV` **(I/O & Config Routines)** (Impact: 15.4)
    * *Intent:* # Page 1065 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `BHIZ` **(I/O & Config Routines)** (Impact: 11.5)
  * `UNIT` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* # Page 1070 # THE FOLLOWING ROUTINE EXECUTES THE UNIT INSTRUCTION, WHICH TAKES THE UNIT OF THE VECTO...
  * `MPAC-` **(Compute Cores)** (Impact: 7.8)
  * `BUFNEG` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 1386`, `args: 89`, `func_start: 241`
* *Risk/State:* `state_mutation: 507`, `dead_code: 2`, `unreferenced_by_name: 32`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1465.1 | **LOC:** 3064 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3101%), Tech Debt (29.5399%)
**Top Internal Functions/Classes:**
  * `MAXDV` **(I/O & Config Routines)** (Impact: 15.4)
    * *Intent:* # Page 1170 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `BHIZ` **(I/O & Config Routines)** (Impact: 11.6)
  * `UNIT` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* # Page 1175 # THE FOLLOWING ROUTINE EXECUTES THE UNIT INSTRUCTION, WHICH TAKES THE UNIT OF THE VECTO...
  * `MPAC-` **(Compute Cores)** (Impact: 7.8)
  * `BUFNEG` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 188 instances
* *State Mutation (weighted view):* 882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 1385`, `args: 89`, `func_start: 243`
* *Risk/State:* `state_mutation: 506`, `dead_code: 2`, `unreferenced_by_name: 33`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 1 MOD BY -- N. BRODEUR*
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 848.86 | **LOC:** 3530 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.9406%), Tech Debt (20.5507%)
**Top Internal Functions/Classes:**
  * `P23` **(I/O & Config Routines)** (Impact: 18.6)
  * `R60CALL` **(I/O & Config Routines)** (Impact: 12.0)
  * `S22NXTIN` **(I/O & Config Routines)** (Impact: 10.4)
  * `DECRM61` **(Many-Argument Workhorses)** (Impact: 9.1)
  * `REND9A` **(I/O & Config Routines)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 126
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 346
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 839`, `args: 26`, `func_start: 105`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 250`, `unreferenced_by_name: 31`
* *Architecture:* `io: 14`, `api: 3`, `concurrency: 26`, `import: 20`
* *Defense:* `safety: 11`, `doc: 121`, `test: 1`, `sync_locks: 11`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, ENDPINS1, FFTAG2, LDPLANET, LOWMEMRY, P20S, P20S1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P40-P47.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *IS THIS AN EXTERNAL DELTA V BURN NO CSTEER = ECSTEER YES CSTEER = ZERO SET UP THRUST FOR P40 20,000 LBS P41 ENTERS HERE ORIGINAL TIG MAY BE SLIPPED BY P40S/SV SET ORIGINAL TIME OF IGNITION FOR S40.9 IMU STATUS CHECK COMPUTE VGTIG,UT COMPUTE PREFERRED ATTITUDE NARROW DEADBAND FOR MANEUVER (EBANK6) ATTITUDE MANEUVER FOR UPDATEVG ALLOW CLOCKTASK P41 INITIALIZE FOR CLOCKTASK WHICH IS CALLED Page 685 BELOW FOR R2 SET FOR UPDATEVG AND TEST FOR STEERING AFTER AVERAGE G (4.1 PROTECTION) V34 V33 SET MRKRTEMP FOR GIMBAL TRIM (-1) ENTRY FROM TST,TRIM SET CNTR +0 FOR RESTART LOGIC IN S40.6 +0 SAYS NORMAL ENTRY +1 (PRE40.6) SAYS RESTART ENTRY TEST TO FIND TIME TO WAIT FOR GIMBAL TEST PLUS, DELAY FOR 18 SECONDS HOLE DELAY FOR TRIM ONLY TASK 6.2 = PRE40.6(-0CS), CLOKTASK(100CS) 4.23 = P40S/SV (PRIO12) P4...*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 795.44 | **LOC:** 2430 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6358%), Tech Debt (46.013%)
**Top Internal Functions/Classes:**
  * `ENDV97E` **(I/O & Config Routines)** (Impact: 14.5)
  * `TOGETHER` **(Compute Cores)** (Impact: 14.5)
  * `RATEZRO` **(Compute Cores)** (Impact: 12.5)
  * `SERVXT` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `NOTADDUL` **(Compute Cores)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 236
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 764`, `args: 98`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 175`, `dead_code: 1`, `unreferenced_by_name: 40`
* *Architecture:* `io: 12`, `concurrency: 56`, `import: 17`
* *Defense:* `safety: 17`, `doc: 82`, `sync_locks: 17`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DAPFIG, DAPS3, DAPS6, DAPS7, DEC409, EBANK, EXTVBS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/SERVICER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUBROUTINE TO READ PIPA COUNTERS, TRYING TO BE VERY CAREFUL SO THAT WILL BE RESTARTABLE. PIPA READINGS ARE STORED IN THE VECTOR DELV. THE HIGH ORDER PART OF EACH COMPONENT CONTAINS THE PIPA READING, RESTARTS BEGIN AT REREADAC.*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 656.36 | **LOC:** 1716 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.1546%), Tech Debt (26.8631%)
**Top Internal Functions/Classes:**
  * `PIPSDONE` **(Compute Cores)** (Impact: 9.2)
  * `NOREASON` **(Compute Cores)** (Impact: 8.7)
  * `VUPDAT` **(Compute Cores)** (Impact: 8.5)
  * `REREADAC` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* # Page 871
  * `HIGATASK` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* # HIGATASK IS ENTERED APPROXIMATELY 6 SECS PRIOR TO HIGATE DURING THE # DESCENT PHASE. HIGATASK SETS...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 671`, `args: 59`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 191`, `dead_code: 3`, `unreferenced_by_name: 18`
* *Architecture:* `api: 1`, `concurrency: 24`, `import: 14`
* *Defense:* `safety: 9`, `doc: 47`, `test: 2`, `sync_locks: 9`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, NORMLIZ, R10, R12STUFF, SERV, SERV1, SERV2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 620.7 | **LOC:** 2342 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.1273%), Tech Debt (16.5889%)
**Top Internal Functions/Classes:**
  * `PICAPAR` **(I/O & Config Routines)** (Impact: 16.6)
  * `INCAZ` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `DSPOPTN` **(Compute Cores)** (Impact: 9.9)
  * `P51G` **(I/O & Config Routines)** (Impact: 7.5)
  * `LSDISP` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 116
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 628`, `args: 35`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 11`, `state_mutation: 141`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 21`, `api: 3`, `concurrency: 31`, `import: 6`
* *Defense:* `safety: 2`, `doc: 85`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AOTMARK2, COUNT, EBANK, P50S, P50S1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 605.04 | **LOC:** 1274 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6282%), Tech Debt (17.5103%)
**Top Internal Functions/Classes:**
  * `EXDAP2` **(Compute Cores)** (Impact: 12.1)
  * `COMPAT` **(Compute Cores)** (Impact: 11.5)
  * `NOTYET` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `BIASEDZ` **(Many-Argument Workhorses)** (Impact: 9.2)
    * *Intent:* # BIASED DZ FOR EXT ATM DAP.
  * `EXDAP` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* # 2. IF C(45) GEQ CALFA GEQ -C(45), USE CMDAPMOD = +1 # BETA: ROLL ERROR = SGN(-SALF) (BETACOM -BETA...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 545`, `args: 55`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 168`, `dead_code: 8`, `unreferenced_by_name: 7`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 3`, `doc: 35`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DAPS1, ETRYDAP, RATEAVG
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/AOSTASK_AND_AOSJOB.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *1/ACCS PROVIDES THE INTERFACE BETWEEN THE GUIDANCE PROGRAMS AND THE DIGITAL AUTOPILOT. WHENEVER THERE IS A CHANGE IN THE MASS OF THE VEHICLE, IN THE DEADBAND SELECTED, IN THE VEHICLE CONFIGURATION (ASCENT-DESCENT- DOCKED), AND DURING A FRESH START OR A RESTART, 1/ACCS IS CALLED TO COMMUNICATE THE DATA CHANGES TO THE DAP.*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 561.0 | **LOC:** 1070 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3452%), Tech Debt (16.8433%)
**Top Internal Functions/Classes:**
  * `SPSLOOP2` **(Many-Argument Workhorses)** (Impact: 11.7)
  * `GETAOSUV` **(Defensive Guards)** (Impact: 9.8)
  * `FIXMIN` **(Many-Argument Workhorses)** (Impact: 9.3)
  * `DVOVSUB` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* # THE DIVISOR FOR THIS ROUTINE MAY BE IN EITHER FIXED OR ERASABLE STORAGE. SIGN AGREEMENT IS # ASSUM...
  * `STACCDOT` **(I/O & Config Routines)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 90 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 497`, `args: 22`, `func_start: 45`
* *Risk/State:* `state_mutation: 172`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 12`, `doc: 32`, `test: 1`, `sync_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DAPS3, EBANK
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *POSITIONING ROUTINES FOR THE IMU PERFORMANCE TESTS AS WELL AS SOME OF THE TESTS THEMSELVES. FOR A DESCRIPTION OF THESE SUBROUTINES AND THE OPERATING PROCEDURES (TYPICALLY) SEE STG MEMO 685.THEORETICAL REF.E-1973 TAKE CARE OF DRIFT FLAG CALCULATE -COS LATITUDE AND SIN LATITUDE GYROCOMPASS COMES IN HERE Page 424 SEE IF IN OPTICAL VERIFICATION NO YES IF GLOKFAIL SET, GIMBAL LOCK +1 IF IN GIMBAL LOCK,OTHERWISE 0 RESET GIMBAL LOCK FLAG BIT 14 FLAG 3 IF ONE GO AND DO A PIPA TEST ONLY ALIGN AND MEASURE VERTICAL PIPA RATE Page 425 PIPA TEST PIP PULSE CATCHING ROUTINE Page 426 DEC585 HAS BEEN REDEFINED FOR LEM TAKE PLATFORM OUT OF GIMBAL LOCK ABOUT 1 HOUR VERTICAL DRIFT TEST 0 IF POSN 4 OFFSET PLATFORM ALLOW ONLY SOUTH GYRO EARTH RATE COMPENS Page 427 IMU NOT IN USE BIT 8 FLAG 0 Page 428 COARSE ALI...*
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 554.38 | **LOC:** 1407 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.7756%), Tech Debt (76.5025%)
**Top Internal Functions/Classes:**
  * `CHKCOMED` **(Defensive Guards)** (Impact: 6.6)
  * `OPTDATA` **(Compute Cores)** (Impact: 6.4)
  * `FINETIME` **(Defensive Guards)** (Impact: 5.1)
  * `RETARG` **(Compute Cores)** (Impact: 5.1)
  * `RETARG1` **(Compute Cores)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 70
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 493`, `args: 26`, `func_start: 88`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 168`, `unreferenced_by_name: 40`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 20`, `import: 8`
* *Defense:* `safety: 12`, `doc: 39`, `sync_locks: 12`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EARTHR, EBANK, ERTHRVSE, ESTIMS, IMUCAL, IMUCAL1, IMUCAL3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUNDISK REV 120 FUNCTIONAL DESCRIPTION SLAP1 MAN INITIATED FRESH START 1. EXECUTE STARTSUB 2. TURN OFF DSKY DISCRETE-LAMPS 3. CLEAR FAIL REGISTERS,SELF-CHECK ERROR COUNTER AND RESTART COUNTER 4. EXECUTE DOFSTART DOFSTART MACHINE INITIATED FRESH START 1. CLEAR SELF-CHECK REGISTERS, MODE REGISTER AND CDUZ REGISTER 2. CLEAR PHASE TABLE 3. INITIALIZE IMU FLAGS 4. INITIALIZE FLAGWORDS 5. TRANSFER CONTROL TO IDLE LOOP IN DUMMYJOB GOPROG HARDWARE RESTART 0. EXECUTE STARTSUB 1. TRANSFER CONTROL TO DOFSTART IF ANY OF THE FOLLOWING CONDITIONS EXIST. A. RESTART OCCURED DURING EXECUTION OF ERASCHK B. BOTH OSCILLATOR FAIL AND AGC WARNING ARE ON C. MARK REJECT AND EITHER NAV OR MAIN DSKY ERROR LIGHT RESET ARE ON. 2. SCHEDULE A T5RUPT PROGRAM FOR THE DAP 3. SET FLAGWRD5 BITS FOR INTWAKE ROUTINE 4. EXTING...*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 531.08 | **LOC:** 1481 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5217%), Tech Debt (25.6807%)
**Top Internal Functions/Classes:**
  * `V5OUT2` **(Compute Cores)** (Impact: 15.2)
  * `DOFSTART` **(Compute Cores)** (Impact: 7.4)
  * `PCLOOP` **(Compute Cores)** (Impact: 7.3)
  * `V37` **(Compute Cores)** (Impact: 6.6)
  * `T5IDLOC` **(Many-Argument Workhorses)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 551`, `args: 57`, `func_start: 60`
* *Risk/State:* `state_mutation: 183`, `unreferenced_by_name: 13`
* *Architecture:* `io: 11`, `api: 10`, `concurrency: 8`, `import: 10`
* *Defense:* `safety: 13`, `doc: 41`, `sync_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, FFTAG10, FRANDRES, INTINIT, NEG7, PREMM1, VAC5LOC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P-AXIS_RCS_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 505.2 | **LOC:** 1057 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.1826%), Tech Debt (13.2964%)
**Top Internal Functions/Classes:**
  * `PJETSLEC` **(Compute Cores)** (Impact: 9.5)
  * `RATERROR` **(Compute Cores)** (Impact: 9.2)
  * `BACKP` **(Compute Cores)** (Impact: 8.8)
  * `LAST` **(Compute Cores)** (Impact: 6.6)
  * `DETENTCK` **(I/O & Config Routines)** (Impact: 6.3)
    * *Intent:* # IF THE INITIAL COMMAND DOES NOT EXCEED THE BREAKOUT LEVEL, CONTROL GOES TO PSEUDO-AUTO IMMEDIATELY...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 484`, `args: 22`, `func_start: 50`
* *Risk/State:* `state_mutation: 159`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 8`, `doc: 23`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DAPS1, EBANK
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/T4RUPT_PROGRAM.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *CHANNEL 30 AND CALLS THE APPROPRIATE SUBROUTINES. THE BITS PROCESSED AND THEIR RELEVANT SUBROUTINES ARE:*
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 502.0 | **LOC:** 1468 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.1629%), Tech Debt (22.6475%)
**Top Internal Functions/Classes:**
  * `STORCMD` **(Compute Cores)** (Impact: 15.9)
  * `CONTDRVE` **(Compute Cores)** (Impact: 8.3)
  * `GLOCKCHK` **(Compute Cores)** (Impact: 8.0)
  * `OPTDRIVE` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* # SHAFT STOP MONITOR-ZONE UPDATE
  * `33OPTMON` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 25
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 562`, `args: 51`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`, `unreferenced_by_name: 10`
* *Architecture:* `io: 10`, `api: 8`, `concurrency: 10`, `import: 4`
* *Defense:* `doc: 84`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, FFTAG12, OPTDRV, RELTAB, T4RUP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/EXTENDED_VERBS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 475.16 | **LOC:** 1682 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.9118%), Tech Debt (63.0384%)
**Top Internal Functions/Classes:**
  * `DPDAT1` **(Compute Cores)** (Impact: 11.4)
  * `DAPDAT2` **(Compute Cores)** (Impact: 8.0)
  * `RDRUSECK` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* # Page 280
  * `IMUATTCK` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* # Page 281 # IMUATTCK VERB 43 DESCRIPTION # LOAD IMU ATTITUDE ERROR METERS # # 1. REQUIRE P00 OR FRE...
  * `R04C` **(Defensive Guards)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 739`, `args: 59`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `io: 19`, `api: 5`, `concurrency: 44`, `import: 13`
* *Defense:* `safety: 20`, `doc: 41`, `sync_locks: 20`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, EXTVB1, EXTVERBS, LOADDAP, LOADDAP1, PINBALL1, PINBALL3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *FLASH V 37 ON DSKY MM CHANGE REQUEST*
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 471.6 | **LOC:** 1243 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.1852%), Tech Debt (30.8939%)
**Top Internal Functions/Classes:**
  * `SETUP70` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `V37` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* # D. DEBRIS # MMNUMBER, MPAC +1, MINDEX, BASETEMP +C(MINDEX), FLAGWRD0, FLAGWRD1, FLAGWRD2, MODREG, ...
  * `RENDV00` **(Compute Cores)** (Impact: 9.5)
  * `DOFSTRT1` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `STARTSB2` **(Compute Cores)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 20
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 550`, `args: 27`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 192`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 10`, `api: 6`, `concurrency: 5`, `import: 4`
* *Defense:* `safety: 7`, `doc: 36`, `sync_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, FFTAG5, FRANDRES, INTINIT, VERB37
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 452.86 | **LOC:** 1475 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3109%), Tech Debt (36.4827%)
**Top Internal Functions/Classes:**
  * `RODCOMP` **(I/O & Config Routines)** (Impact: 10.2)
  * `STARTP67` **(Compute Cores)** (Impact: 8.9)
  * `QUADGUID` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* # # AS PUBLISHED -- # ___ __ ___ __ # ___ ___ 6(VDG + VG) 12(RDG - RG) # ACG = ADG + ----------- + -...
  * `CGCALC` **(Many-Argument Workhorses)** (Impact: 8.1)
    * *Intent:* # *********************************************************************** # ERECT GUIDANCE-STABLE ME...
  * `REDESIG` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* # ********************************************************************* # LANDING SITE PERTURBATION ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 475`, `args: 41`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 146`, `unreferenced_by_name: 19`
* *Architecture:* `io: 10`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 2`, `doc: 33`, `sync_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, F2DPS, LANDCNST, P66LOC, RODTRAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 434.96 | **LOC:** 1460 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4618%), Tech Debt (96.995%)
**Top Internal Functions/Classes:**
  * `NORMRET` **(Defensive Guards)** (Impact: 9.9)
  * `1STOR2ND` **(Compute Cores)** (Impact: 6.7)
  * `LINUSCHR` **(Compute Cores)** (Impact: 6.4)
  * `FLASHSUB` **(Compute Cores)** (Impact: 5.3)
  * `MAKEMARK` **(Interface Declarations)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 23
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 498`, `args: 34`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 86`, `dead_code: 1`, `unreferenced_by_name: 41`
* *Architecture:* `io: 10`, `api: 24`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 18`, `doc: 39`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DISPLAYS, FFTAG4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Comanche, build 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), Apollo 11.*
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 433.1 | **LOC:** 1477 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4833%), Tech Debt (96.6338%)
**Top Internal Functions/Classes:**
  * `NORMRET` **(Defensive Guards)** (Impact: 9.9)
  * `1STOR2ND` **(Compute Cores)** (Impact: 6.6)
  * `LINUSCHR` **(Compute Cores)** (Impact: 6.4)
  * `FLASHSUB` **(Compute Cores)** (Impact: 5.3)
  * `MAKEMARK` **(Interface Declarations)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 23
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 495`, `args: 34`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 85`, `dead_code: 2`, `unreferenced_by_name: 40`
* *Architecture:* `io: 10`, `api: 24`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 18`, `doc: 38`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DISPLAYS, FFTAG4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P37_P70.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *DESCRIPTION A RETURN TO EARTH TRAJECTORY IS COMPUTED PROVIDED THE CSM IS OUTSIDE THE LUNAR SPHERE OF INFLUENCE AT THE TIME OF IGNITION. INITIALLY A CONIC TRAJECTORY IS DETERMINED AND RESULTING IGNITION AND REENTRY PARAMETERS ARE DISPLAYED TO THE ASTRONAUT. THEN IF THE ASTRONAUT SO DESIRES, A PRECISION TRAJECTORY IS DETERMINED WITH THE RESULTING IGNITION AND REENTRY PARAMETERS DISPLAYED. UPON FINAL ACCEPTANCE BY THE ASTRONAUT, THE PROGRAM COMPUTES AND STORES THE TARGET PARAMETERS FOR RETURN TO EARTH FOR USE BY SPS PROGRAM (P40) OR RCS PROGRAM (P41).*
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 426.88 | **LOC:** 1951 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8724%), Tech Debt (14.8%)
**Top Internal Functions/Classes:**
  * `P37PROC` **(I/O & Config Routines)** (Impact: 10.1)
  * `RTENCK3D` **(I/O & Config Routines)** (Impact: 10.0)
    * *Intent:* # Page 916
  * `RTD22` **(I/O & Config Routines)** (Impact: 8.5)
  * `V2T165` **(I/O & Config Routines)** (Impact: 6.7)
  * `V2T1X` **(I/O & Config Routines)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 239`, `args: 1`, `func_start: 82`
* *Risk/State:* `state_mutation: 94`, `unreferenced_by_name: 9`
* *Architecture:* `concurrency: 2`, `import: 8`
* *Defense:* `doc: 67`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` C4RTE, COUNT, EBANK, PREC220, PREC225, RTE, RTE1, RTE2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 426.24 | **LOC:** 2214 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.8017%), Tech Debt (14.8349%)
**Top Internal Functions/Classes:**
  * `PICAPAR` **(I/O & Config Routines)** (Impact: 16.4)
  * `TERM52` **(I/O & Config Routines)** (Impact: 12.4)
  * `COARSTYP` **(I/O & Config Routines)** (Impact: 6.4)
  * `ROTA` **(I/O & Config Routines)** (Impact: 6.4)
  * `P51G` **(I/O & Config Routines)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 4 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 55
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 535`, `args: 23`, `func_start: 65`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 104`, `dead_code: 2`, `unreferenced_by_name: 10`
* *Architecture:* `io: 17`, `api: 2`, `concurrency: 20`, `import: 18`
* *Defense:* `safety: 6`, `doc: 83`, `sync_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ADVTRACK, COUNT, P50S, P50S1, P50S2, P50S3, PICAPAR, PLANET...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 418.6 | **LOC:** 1068 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5767%), Tech Debt (56.8007%)
**Top Internal Functions/Classes:**
  * `GSELECT` **(Compute Cores)** (Impact: 8.0)
  * `8192AUG` **(Compute Cores)** (Impact: 5.2)
  * `IMUZEROA` **(Compute Cores)** (Impact: 5.1)
  * `GOMANUR` **(I/O & Config Routines)** (Impact: 5.1)
  * `GMERGE` **(Compute Cores)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 436`, `args: 36`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 94`, `dead_code: 2`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 10`, `import: 4`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, FFTAG3, MODESW, P05P06, R02
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82 FUNCTIONAL DESCRIPTION- TO DELAY FURTHER EXECUTION OF THE CALLING ROUTINE UNTIL ITS SELECTED I/O FUNCTION IS COMPLETE. THE FOLLOWING CHECKS ON THE CALLING ROUTINES MODECADR ARE MADE AND ACTED UPON. 1) +0 INDICATES INCOMPLETE I/O OPERATION.CALLING ROUTINE IS PUT TO SLEEP. 2) -1 INDICATES COMPLETED I/O OPERATION. STALL BYPASSES JOBSLEEP CALL AND RETURNS TO CALLING ROUTINE AT L+3 3) -0 INDICATES COMPLETED I/O WITH FAILURE. STALL CLEARS MODECADR AND RETURNS TO CALLING ROUTINE AT L+2. 4) VALUE GREATER THAN 0 INDICATES TWO ROUTINES CALLING FOR USE OF SAME DEVICE. STALL EXITS TO ABORT WHICH EXECUTES A PROGRAM RESTART WHICH IN TURN CLEARS ALL MODECADR REGISTERS. CALLING SEQUENCE- L TC BANKCALL L+1 CADR ...*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 417.34 | **LOC:** 1067 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5676%), Tech Debt (57.0998%)
**Top Internal Functions/Classes:**
  * `GSELECT` **(Compute Cores)** (Impact: 8.0)
  * `8192AUG` **(Compute Cores)** (Impact: 5.2)
  * `IMUZEROA` **(Compute Cores)** (Impact: 5.1)
  * `GOMANUR` **(I/O & Config Routines)** (Impact: 5.1)
  * `GMERGE` **(Compute Cores)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 435`, `args: 36`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 93`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 4`, `concurrency: 10`, `import: 4`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, FFTAG3, MODESW, P05P06, R02
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *KILLTASK IS USED TO REMOVE A TASK FROM THE WAITLIST BY SUBSTITUTING A NULL TASK CALLED `NULLTASK' (OF COURSE), WHICH MERELY DOES A TC TASKOVER. IF THE SAME TASK IS SCHEDULED MORE THAN ONCE, ONLY THE ONE WHICH WILL OCCUR FIRST IS REMOVED. IF THE TASK IS NOT SCHEDULED, KILLTASK TAKES NO ACTION AND RETURNS WITH NO ALARM. KILLTASK LEAVES INTERRUPTS INHIBITED SO CALLER MUST RELINT*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 412.28 | **LOC:** 1060 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9763%), Tech Debt (19.6221%)
**Top Internal Functions/Classes:**
  * `P40AUTO` **(Compute Cores)** (Impact: 6.4)
  * `CLOKJOB` **(Compute Cores)** (Impact: 6.0)
  * `IGNITE` **(Defensive Guards)** (Impact: 4.1)
  * `TIG-35` **(Interface Declarations)** (Impact: 4.0)
    * *Intent:* # ********************************
  * `TIG-30` **(Interface Declarations)** (Impact: 4.0)
    * *Intent:* # ********************************
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 123
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 456`, `args: 50`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 82`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 38`, `import: 7`
* *Defense:* `safety: 13`, `doc: 31`, `test: 2`, `sync_locks: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, EBANK, FFTAG6, P40S, P40S1, P40S2, P40S3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/RCS-CSM_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *THIS SUBROUTINE IS USED TO DISPLAY ATTITUDE ERRORS ON THE FDAI VIA THE DIGITAL TO ANALOG CONVERTERS (DACS) IN THE CDUS. CARE IS TAKEN TO METER OUT THE APPROPRIATE NUMBER OF PULSES TO THE IMU ERROR COUNTERS AND PREVENT OVERFLOW, TO CONTROL THE RELAY SEQUENCING, AND TO AVOID INTERFERENCE WITH THE COARSE ALIGN LOOP WHICH ALSO USES THE DACS. CALLING SEQUENCE: DURING THE INITIALIZATION SECTION OF THE USER'S PROGRAM, BIT3 OF RCSFLAGS SHOULD BE SET TO INITIATE THE TURN-ON SEQUENCE WITHIN THE NEEDLES PROGRAM: CS RCSFLAGS # IN EBANK6 MASK BIT3 ADS RCSFLAGS THEREAFTER, THE ATTITUDE ERRORS GENERATED BY THE USER SHOULD BE TRANSFERED TO THE FOLLOWING LOCATIONS IN EBANK6: AK SCALED 180 DEGREES NOTE: THESE LOCATIONS ARE SUBJECT AK1 SCALED 180 DEGREES TO CHANGE AK2 SCALED 180 DEGREES FULL SCALED DEFLECTIO...*
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 409.78 | **LOC:** 976 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3965%), Tech Debt (48.0825%)
**Top Internal Functions/Classes:**
  * `NOCHANGE` **(Compute Cores)** (Impact: 9.3)
  * `DACLOOP` **(Compute Cores)** (Impact: 6.6)
  * `ZEROT5` **(Compute Cores)** (Impact: 6.4)
  * `DRHOLOOP` **(I/O & Config Routines)** (Impact: 5.4)
  * `SETWBODY` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 375`, `args: 23`, `func_start: 45`
* *Risk/State:* `state_mutation: 125`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 2`, `import: 1`
* *Defense:* `doc: 29`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, DAPS3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Comanche055/ALARM_AND_ABORT.agc` -> **Severity: 202.45** (Blast Radius: 4.049 * Doc Risk: 50.0%)
- `Comanche055/CM_BODY_ATTITUDE.agc` -> **Severity: 202.45** (Blast Radius: 4.049 * Doc Risk: 50.0%)
- `Comanche055/CSM_GEOMETRY.agc` -> **Severity: 202.45** (Blast Radius: 4.049 * Doc Risk: 50.0%)
- `Comanche055/GROUND_TRACKING_DETERMINATION_PROGRAM.agc` -> **Severity: 202.45** (Blast Radius: 4.049 * Doc Risk: 50.0%)
- `Comanche055/INFLIGHT_ALIGNMENT_ROUTINES.agc` -> **Severity: 202.45** (Blast Radius: 4.049 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
