# ARCHITECTURAL_BRIEF: pillman
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nanochess/pillman.git` |
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 1639 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 6 | 1621 | 66.7% |
| MAKEFILE | 1 | 16 | 11.1% |
| MARKDOWN | 1 | 0 | 11.1% |
| BATCH | 1 | 2 | 11.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8 | 88.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.com`: 1x Excluded (Unsupported Extension: '.com')
- `.img`: 1x Excluded (Unsupported Extension: '.img')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 12.0 | 7.5 | 9.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 66.1 | 46.3 | 60.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 38.0 | 15.4 | 12.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 60.6 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 9.9 | 1.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 48.1 | 16.1 | 14.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.0 | 5.9 | 6.9 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 112 | 6 | 19 | `old/pillman2.asm` |
| cleanup | 0 | 0 | 0 | - |
| guards | 101 | 6 | 17 | `old/pillman0.asm` |
| danger | 0 | 0 | 0 | - |
| concurrency | 37 | 6 | 6 | `old/pillman0.asm` |
| connectivity | 6 | 1 | 0 | `Makefile` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 25 | 6 | 4 | `pillman.asm` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 3 | 3 | 1 | `old/pillman0.asm` |
| mutation | 52 | 7 | 9 | `old/pillman0.asm` |
| dead_code | 29 | 6 | 6 | `pillman.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 5 | 5 | 1 | `old/pillman1.asm` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **17.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 0)
- `README` (Hits: 0)
- `e.bat` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
No file in this repository declares an import that GitGalaxy resolved, so there is no coupling ranking to report. See the note above -- the same caveat applies.


## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `move_sprite` (@ `pillman.asm`) -> Impact: **11.7** | LOC: 39
- `move_sprite` (@ `old/pillman2.asm`) -> Impact: **11.5** | LOC: 34
- `move_sprite` (@ `old/pillman3.asm`) -> Impact: **11.5** | LOC: 35
- `move_sprite` (@ `old/pillman4.asm`) -> Impact: **11.5** | LOC: 35
- `move_sprite` (@ `old/pillman1.asm`) -> Impact: **11.4** | LOC: 32
  * *Intent:* ; ; DI = address on screen ; BL = wanted direction ;
- `move_ghost` (@ `old/pillman0.asm`) -> Impact: **10.9** | LOC: 22
  * *Intent:* ; ; Move ghost ;
- `g9` (@ `old/pillman0.asm`) -> Impact: **8.4** | LOC: 22
- `g4` (@ `old/pillman0.asm`) -> Impact: **7.5** | LOC: 29
- `in0` (@ `old/pillman0.asm`) -> Impact: **7.4** | LOC: 13
- `in2` (@ `old/pillman1.asm`) -> Impact: **7.4** | LOC: 13

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `old` | 5 | 599.4 | 10.18% | 17.9% |
| `__monolith__` | 4 | 143.06 | 2.27% | 8.36% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `old/pillman0.asm` -> **37.9909%** Exposure
- `pillman.asm` -> **33.4388%** Exposure
- `old/pillman4.asm` -> **13.6536%** Exposure
- `old/pillman3.asm` -> **13.54%** Exposure
- `old/pillman1.asm` -> **12.1953%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `old/pillman0.asm` -> **48.0534%** Exposure
- `old/pillman3.asm` -> **20.6952%** Exposure
- `old/pillman2.asm` -> **18.8778%** Exposure
- `old/pillman1.asm` -> **14.8924%** Exposure
- `old/pillman4.asm` -> **13.381%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `old/pillman0.asm` -> **5** Orphaned Functions | **0** Duplicates
- `pillman.asm` -> **4** Orphaned Functions | **0** Duplicates
- `old/pillman3.asm` -> **3** Orphaned Functions | **0** Duplicates
- `old/pillman4.asm` -> **3** Orphaned Functions | **0** Duplicates
- `old/pillman1.asm` -> **1** Orphaned Functions | **0** Duplicates

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

### 1. `old/pillman0.asm` (ASSEMBLY) -> Cumulative Risk: **450.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 127.74 | **LOC:** 339 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (66.1277%)
- **Heaviest Functions:** `move_ghost` (Impact: 10.9), `g9` (Impact: 8.4), `g4` (Impact: 7.5)

### 2. `pillman.asm` (ASSEMBLY) -> Cumulative Risk: **404.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 117.32 | **LOC:** 388 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (59.9986%)
- **Heaviest Functions:** `move_sprite` (Impact: 11.7), `ds4` (Impact: 7.4), `game_loop` (Impact: 5.8)

### 3. `old/pillman3.asm` (ASSEMBLY) -> Cumulative Risk: **394.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 117.1 | **LOC:** 332 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (61.8742%)
- **Heaviest Functions:** `move_sprite` (Impact: 11.5), `ds4` (Impact: 7.4), `game_loop` (Impact: 7.0)

### 4. `old/pillman2.asm` (ASSEMBLY) -> Cumulative Risk: **390.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 126.52 | **LOC:** 346 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (61.4488%)
- **Heaviest Functions:** `move_sprite` (Impact: 11.5), `ds4` (Impact: 7.4), `clock_wait` (Impact: 5.8)

### 5. `old/pillman4.asm` (ASSEMBLY) -> Cumulative Risk: **386.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.56 | **LOC:** 336 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (60.4447%)
- **Heaviest Functions:** `move_sprite` (Impact: 11.5), `ds4` (Impact: 7.4), `game_loop` (Impact: 5.8)

### 6. `old/pillman1.asm` (ASSEMBLY) -> Cumulative Risk: **383.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 114.48 | **LOC:** 337 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (60.5532%)
- **Heaviest Functions:** `move_sprite` (Impact: 11.4), `in2` (Impact: 7.4), `clock_wait` (Impact: 5.8)

### 7. `Makefile` (MAKEFILE) -> Cumulative Risk: **212.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 13.22 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (9.8983%), Verification (2.4006%)
- **Heaviest Functions:** `pillman.com` (Impact: 1.2), `clean` (Impact: 1.2), `rundosbox` (Impact: 1.2)

### 8. `e.bat` (BATCH) -> Cumulative Risk: **2.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 11.04 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `old/pillman0.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 127.74 | **LOC:** 339 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9597%), Tech Debt (37.9909%)
**Top Internal Functions/Classes:**
  * `move_ghost` (Impact: 10.9)
    * *Intent:* ; ; Move ghost ;
  * `g9` (Impact: 8.4)
  * `g4` (Impact: 7.5)
  * `in0` (Impact: 7.4)
  * `clock_wait` (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 126`, `args: 148`, `func_start: 45`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* None
* *Defense:* `sync_locks: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman2.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 126.52 | **LOC:** 346 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2118%), Tech Debt (12.104%)
**Top Internal Functions/Classes:**
  * `move_sprite` (Impact: 11.5)
  * `ds4` (Impact: 7.4)
  * `clock_wait` (Impact: 5.8)
  * `ms9` (Impact: 5.5)
  * `dm2` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 112`, `args: 148`, `func_start: 49`
* *Risk/State:* `state_mutation: 9`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pillman.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 117.32 | **LOC:** 388 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0764%), Tech Debt (33.4388%)
**Top Internal Functions/Classes:**
  * `move_sprite` (Impact: 11.7)
  * `ds4` (Impact: 7.4)
  * `game_loop` (Impact: 5.8)
    * *Intent:* ; ; Main game loop ;
  * `dm2` (Impact: 5.1)
  * `ms9` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 108`, `args: 151`, `func_start: 48`
* *Risk/State:* `state_mutation: 8`, `dead_code: 3`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman3.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 117.1 | **LOC:** 332 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1114%), Tech Debt (13.54%)
**Top Internal Functions/Classes:**
  * `move_sprite` (Impact: 11.5)
  * `ds4` (Impact: 7.4)
  * `game_loop` (Impact: 7.0)
  * `dm2` (Impact: 5.0)
  * `ms9` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 109`, `args: 151`, `func_start: 45`
* *Risk/State:* `state_mutation: 9`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman1.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 114.48 | **LOC:** 337 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3632%), Tech Debt (12.1953%)
**Top Internal Functions/Classes:**
  * `move_sprite` (Impact: 11.4)
    * *Intent:* ; ; DI = address on screen ; BL = wanted direction ;
  * `in2` (Impact: 7.4)
  * `clock_wait` (Impact: 5.8)
  * `g9` (Impact: 5.8)
  * `ms9` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 121`, `args: 153`, `func_start: 45`
* *Risk/State:* `state_mutation: 7`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman4.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 113.56 | **LOC:** 336 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2359%), Tech Debt (13.6536%)
**Top Internal Functions/Classes:**
  * `move_sprite` (Impact: 11.5)
  * `ds4` (Impact: 7.4)
  * `game_loop` (Impact: 5.8)
  * `dm2` (Impact: 5.0)
  * `ms9` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 108`, `args: 150`, `func_start: 47`
* *Risk/State:* `state_mutation: 8`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.22 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pillman.com` (Impact: 1.2)
  * `clean` (Impact: 1.2)
  * `rundosbox` (Impact: 1.2)
  * `all` (Impact: 1.1)
  * `pillman.img` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e.bat` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 11.04 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.48 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
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

- `Makefile` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)
- `old/pillman0.asm` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)
- `old/pillman1.asm` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)
- `old/pillman2.asm` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)
- `old/pillman3.asm` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
