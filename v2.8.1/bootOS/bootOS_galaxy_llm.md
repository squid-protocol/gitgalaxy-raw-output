# ARCHITECTURAL_BRIEF: bootOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nanochess/bootOS.git` |
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
| Total Artifacts | 18 |
| Analyzed Artifacts (Scanned) | 8 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 1086 |
| Volatility Index | 0.125 |
| % Scanned of codebase = | 44.4% |
| Dominant Lang | ASSEMBLY |

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
| ASSEMBLY | 5 | 1073 | 62.5% |
| MAKEFILE | 1 | 11 | 12.5% |
| MARKDOWN | 1 | 0 | 12.5% |
| BATCH | 1 | 2 | 12.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 25%, Large Core Modules 25%, Parameter Forwarders Files 25%, I/O & Config Routines Files 12%, Interface Declarations Files 12%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7 | 87.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 12.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `.img`: 5x Excluded (Unsupported Extension: '.img')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lst`: 2x Excluded (Unsupported Extension: '.lst')
- `.fdd`: 1x Excluded (Unsupported Extension: '.fdd')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 16.4 | 8.5 | 10.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 74.3 | 45.9 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 47.9 | 52.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 46.7 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 9.1 | 1.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 59.2 | 29.3 | 28.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 13.4 | 2.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 64.3 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 73 | 5 | 22 | `patch/snake.asm` |
| cleanup | 0 | 0 | 0 | - |
| guards | 18 | 2 | 4 | `os.asm` |
| danger | 1 | 1 | 0 | `os.asm` |
| concurrency | 2 | 1 | 0 | `os.asm` |
| connectivity | 5 | 1 | 0 | `Makefile` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `patch/mine.asm` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 34 | 5 | 7 | `patch/snake.asm` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 9 | 1 | 0 | `patch/mine.asm` |
| mutation | 27 | 6 | 6 | `os.asm` |
| dead_code | 33 | 5 | 8 | `patch/snake.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 0)
- `README.md` (Hits: 0)
- `counter.asm` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
No file in this repository declares an import that GitGalaxy resolved, so there is no coupling ranking to report. See the note above -- the same caveat applies.


## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `.after_al` **(Many-Argument Workhorses)** (@ `patch/sokoban.asm`) -> Impact: **22.5** | LOC: 59
- `.loop` **(Many-Argument Workhorses)** (@ `patch/sokoban.asm`) -> Impact: **10.5** | LOC: 15
- `ClearScreen` **(Many-Argument Workhorses)** (@ `patch/mine.asm`) -> Impact: **9.6** | LOC: 13
- `.loop` **(Compute Cores)** (@ `os.asm`) -> Impact: **9.4** | LOC: 9
- `.mainloop` **(State Mutators)** (@ `patch/sokoban.asm`) -> Impact: **9.4** | LOC: 19
- `Flood` **(Compute Cores)** (@ `patch/mine.asm`) -> Impact: **9.2** | LOC: 42
  * *Intent:* ;; Flood fill empty cells ;; ;; Parameters: ;; * BP - Cell index ;; Clobbered registers: ;; * Yes [TODO]
- `check_collisions` **(Compute Cores)** (@ `patch/snake.asm`) -> Impact: **9.2** | LOC: 11
- `no_exit` **(State Mutators)** (@ `patch/snake.asm`) -> Impact: **7.5** | LOC: 9
- `os6` **(Parameter Forwarders)** (@ `os.asm`) -> Impact: **6.6** | LOC: 12
- `PopulateMines` **(Parameter Forwarders)** (@ `patch/mine.asm`) -> Impact: **6.4** | LOC: 8
  * *Intent:* ;; Populate Map.Mines with mines

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code
  * **State Mutators**: general-purpose function that reassigns or mutates state

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `patch` | 3 | 353.88 | 12.47% | 70.89% |
| `__monolith__` | 5 | 190.76 | 4.48% | 24.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `patch/mine.asm` -> **99.9536%** Exposure
- `patch/snake.asm` -> **89.5777%** Exposure
- `counter.asm` -> **70.8855%** Exposure
- `os.asm` -> **52.015%** Exposure
- `patch/sokoban.asm` -> **23.1244%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `patch/sokoban.asm` -> **59.1595%** Exposure
- `counter.asm` -> **57.734%** Exposure
- `patch/mine.asm` -> **36.8296%** Exposure
- `patch/snake.asm` -> **28.6667%** Exposure
- `os.asm` -> **22.4661%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `patch/mine.asm` -> **8** Orphaned Functions | **2** Duplicates
- `patch/snake.asm` -> **9** Orphaned Functions | **0** Duplicates
- `os.asm` -> **7** Orphaned Functions | **0** Duplicates
- `patch/sokoban.asm` -> **2** Orphaned Functions | **0** Duplicates
- `counter.asm` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `patch/mine.asm` (ASSEMBLY) -> Cumulative Risk: **487.58**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.12)
- **Magnitude:** 128.86 | **LOC:** 405 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9536%), Verification (80.0%)
- **Heaviest Functions:** `ClearScreen` (Many-Argument Workhorses, Impact: 9.6), `Flood` (Compute Cores, Impact: 9.2), `PopulateMines` (Parameter Forwarders, Impact: 6.4)

### 2. `patch/snake.asm` (ASSEMBLY) -> Cumulative Risk: **469.14**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.37)
- **Magnitude:** 101.3 | **LOC:** 242 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (89.5777%), Verification (80.0%)
- **Heaviest Functions:** `check_collisions` (Compute Cores, Impact: 9.2), `no_exit` (State Mutators, Impact: 7.5), `check_collisions_self` (Compute Cores, Impact: 5.5)

### 3. `patch/sokoban.asm` (ASSEMBLY) -> Cumulative Risk: **456.02**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.90)
- **Magnitude:** 123.72 | **LOC:** 398 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (63.9618%)
- **Heaviest Functions:** `.after_al` (Many-Argument Workhorses, Impact: 22.5), `.loop` (Many-Argument Workhorses, Impact: 10.5), `.mainloop` (State Mutators, Impact: 9.4)

### 4. `os.asm` (ASSEMBLY) -> Cumulative Risk: **382.94**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +2.29)
- **Magnitude:** 145.6 | **LOC:** 656 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (62.0321%), Tech Debt (52.015%)
- **Heaviest Functions:** `.loop` (Compute Cores, Impact: 9.4), `os6` (Parameter Forwarders, Impact: 6.6), `restart` (Parameter Forwarders, Impact: 4.8)

### 5. `counter.asm` (ASSEMBLY) -> Cumulative Risk: **366.83**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.60)
- **Magnitude:** 20.18 | **LOC:** 91 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (74.3319%), Tech Debt (70.8855%), State Flux (57.734%)
- **Heaviest Functions:** `.1` (Parameter Forwarders, Impact: 5.9), `start` (Parameter Forwarders, Impact: 3.9), `.2` (Parameter Forwarders, Impact: 3.2)

### 6. `Makefile` (MAKEFILE) -> Cumulative Risk: **161.48**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.17)
- **Magnitude:** 9.82 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (50.0%), Api Exposure (9.1141%), Verification (2.3658%)
- **Heaviest Functions:** `os.img` (I/O & Config Routines, Impact: 1.2), `clean` (I/O & Config Routines, Impact: 1.2), `all` (I/O & Config Routines, Impact: 1.1)

### 7. `e.bat` (BATCH) -> Cumulative Risk: **2.3**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 11.04 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `os.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 145.6 | **LOC:** 656 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0221%), Tech Debt (52.015%)
**Top Internal Functions/Classes:**
  * `.loop` **(Compute Cores)** (Impact: 9.4)
  * `os6` **(Parameter Forwarders)** (Impact: 6.6)
  * `restart` **(Parameter Forwarders)** (Impact: 4.8)
    * *Intent:* ; ; Warm start of bootOS ;
  * `os11` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* ; Notice that filenames starting with same characters ; won't be recognized as such (so file dirab c...
  * `.find` **(Interface Declarations)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 162`, `args: 129`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* None
* *Defense:* `sync_locks: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/mine.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 128.86 | **LOC:** 405 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1717%), Tech Debt (99.9536%)
**Top Internal Functions/Classes:**
  * `ClearScreen` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `Flood` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* ;; Flood fill empty cells ;; ;; Parameters: ;; * BP - Cell index ;; Clobbered registers: ;; * Yes [T...
  * `PopulateMines` **(Parameter Forwarders)** (Impact: 6.4)
    * *Intent:* ;; Populate Map.Mines with mines
  * `NumCells` **(Parameter Forwarders)** (Impact: 6.4)
    * *Intent:* ;; Number empty cells with amount of neighboring mines
  * `IncIfMineAtCell` **(Parameter Forwarders)** (Impact: 5.6)
    * *Intent:* ;; TODO: Update comment ;; ;; Increment AX if there is a mine in Map.Mines at index BX, where BX is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 154`, `args: 117`, `func_start: 35`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 7`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/sokoban.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 123.72 | **LOC:** 398 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4097%), Tech Debt (23.1244%)
**Top Internal Functions/Classes:**
  * `.after_al` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `.loop` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `.mainloop` **(State Mutators)** (Impact: 9.4)
  * `.loop` **(Compute Cores)** (Impact: 6.1)
  * `.nextrow` **(Parameter Forwarders)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 133`, `args: 156`, `func_start: 26`
* *Risk/State:* `state_mutation: 6`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/snake.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 101.3 | **LOC:** 242 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.818%), Tech Debt (89.5777%)
**Top Internal Functions/Classes:**
  * `check_collisions` **(Compute Cores)** (Impact: 9.2)
  * `no_exit` **(State Mutators)** (Impact: 7.5)
  * `check_collisions_self` **(Compute Cores)** (Impact: 5.5)
  * `no_collision` **(Parameter Forwarders)** (Impact: 5.2)
  * `update_body` **(Parameter Forwarders)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 120`, `args: 101`, `func_start: 32`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 9`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `counter.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 20.18 | **LOC:** 91 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.3967%), Tech Debt (70.8855%)
**Top Internal Functions/Classes:**
  * `.1` **(Parameter Forwarders)** (Impact: 5.9)
  * `start` **(Parameter Forwarders)** (Impact: 3.9)
  * `.2` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 41`, `args: 36`, `func_start: 7`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e.bat` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11.04 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.82 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `os.img` **(I/O & Config Routines)** (Impact: 1.2)
  * `clean` **(I/O & Config Routines)** (Impact: 1.2)
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `runqemu` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.12 | **LOC:** 206 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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

- `patch/mine.asm` -> **Severity: 12500.0** (Blast Radius: 125.0 * Doc Risk: 100.0%)
- `patch/snake.asm` -> **Severity: 12500.0** (Blast Radius: 125.0 * Doc Risk: 100.0%)
- `patch/sokoban.asm` -> **Severity: 12500.0** (Blast Radius: 125.0 * Doc Risk: 100.0%)
- `Makefile` -> **Severity: 6250.0** (Blast Radius: 125.0 * Doc Risk: 50.0%)
- `counter.asm` -> **Severity: 6250.0** (Blast Radius: 125.0 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
