# ARCHITECTURAL_BRIEF: temp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 139 |
| Analyzed Artifacts (Scanned) | 127 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 9796 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4778 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.656 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7011 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 43 | 6709 | 33.9% |
| PLAINTEXT | 41 | 0 | 32.3% |
| JCL | 29 | 3070 | 22.8% |
| MARKDOWN | 13 | 0 | 10.2% |
| SHELL | 1 | 17 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z -1.16; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, I/O & Config Routines Files 39%, Interface Declarations Files 6%, Declarative / Non-Code 6%, Many-Argument Workhorses Files 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 73 | 57.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 42.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 124 LOC), 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.rexx`: 2x Excluded (Unsupported Extension: '.rexx')
- `.evbind`: 1x Excluded (Unsupported Extension: '.evbind')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 24204 LOC)
- `.bms`: 1x Zero-Density Threshold (LOC: 688, Signals: 0)
- `.cpy`: 1x Zero-Density Threshold (LOC: 85, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.3 | 36.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 41.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 60.9 | 11.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 89.1 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 28.3 | 3.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 82.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.0 | 1.4 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 55 | 22 | 2 | `cics-genapp/base/src/lgcmarea.cpy` |
| cleanup | 49 | 7 | 0 | `cics-genapp/base/src/lgsetup.cbl` |
| guards | 86 | 27 | 2 | `cics-genapp/base/src/lgipdb01.cbl` |
| danger | 125 | 33 | 1 | `cics-genapp/base/src/lgtestp1.cbl` |
| concurrency | 12 | 5 | 0 | `cics-genapp/base/cntl/asmmap.jcl` |
| connectivity | 28 | 28 | 1 | `cics-genapp/base/cntl/cobol.jcl` |
| io | 592 | 51 | 14 | `cics-genapp/base/src/lgsetup.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 238 | 31 | 7 | `cics-genapp/base/src/lgipdb01.cbl` |
| time | 44 | 22 | 2 | `cics-genapp/base/src/lgacdb01.cbl` |
| serialization | 25 | 1 | 0 | `cics-genapp/base/src/lgwebst5.cbl` |
| regex | 4 | 1 | 0 | `cics-genapp/base/src/lgtestc1.cbl` |
| events | 48 | 38 | 1 | `cics-genapp/base/src/lgtestc1.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 60 | 16 | 1 | `cics-genapp/base/src/lgwebst5.cbl` |
| mutation | 2315 | 61 | 66 | `cics-genapp/base/src/lgwebst5.cbl` |
| dead_code | 101 | 31 | 3 | `cics-genapp/base/src/lgipdb01.cbl` |
| credential | 1 | 1 | 0 | `cics-genapp/base/src/lgacdb01.cbl` |
| threat | 581 | 32 | 13 | `cics-genapp/base/src/lgsetup.cbl` |
| ml_ai | 2 | 1 | 0 | `cics-genapp/base/src/lgicvs01.cbl` |
| ui | 52 | 9 | 0 | `cics-genapp/base/src/lgtestp1.cbl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cics-genapp/base/src/lgsetup.cbl` (Hits: 99)
- `cics-genapp/base/src/lgwebst5.cbl` (Hits: 46)
- `cics-genapp/base/src/lgicvs01.cbl` (Hits: 35)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lgcmarea.cpy** (`cics-genapp/base/src/lgcmarea.cpy`) — 25 inbound connections
2. **Building.md** (`cics-genapp/base/Building.md`) — 2 inbound connections
3. **Installation.md** (`cics-genapp/base/Installation.md`) — 2 inbound connections
4. **Reference.md** (`cics-genapp/base/Reference.md`) — 2 inbound connections
5. **Testing.md** (`cics-genapp/base/Testing.md`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Installation.md** (`cics-genapp/base/Installation.md`) — 7 outbound dependencies
2. **README.md** (`cics-genapp/base/README.md`) — 5 outbound dependencies
3. **README.md** (`cics-genapp/README.md`) — 3 outbound dependencies
4. **lgacdb01.cbl** (`cics-genapp/base/src/lgacdb01.cbl`) — 3 outbound dependencies
5. **lgapdb01.cbl** (`cics-genapp/base/src/lgapdb01.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `A-GAIN` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgtestp4.cbl`) -> Impact: **24.0** | LOC: 199
- `UPDATE-POLICY-DB2-INFO` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgupdb01.cbl`) -> Impact: **22.5** | LOC: 110
  * *Intent:* *================================================================* * 1) Use SELECT FOR UPDATE to obtain a lock on the row in the * * policy table, che...
- `MAINLINE` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgapdb01.cbl`) -> Impact: **20.2** | LOC: 105
  * *Intent:* *----------------------------------------------------------------*
- `MAINLINE` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgicvs01.cbl`) -> Impact: **19.6** | LOC: 133
  * *Intent:* *---------------------------------------------------------------*
- `A-GAIN` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgtestp1.cbl`) -> Impact: **18.0** | LOC: 204
- `A-GAIN` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgtestp2.cbl`) -> Impact: **18.0** | LOC: 191
- `A-GAIN` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgtestp3.cbl`) -> Impact: **18.0** | LOC: 187
- `GET-ENDOW-DB2-INFO` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgipdb01.cbl`) -> Impact: **16.3** | LOC: 106
  * *Intent:* *----------------------------------------------------------------* *================================================================* * Use Select on ...
- `A-GAIN` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgtestc1.cbl`) -> Impact: **15.5** | LOC: 159
- `MAINLINE` **(I/O & Config Routines)** (@ `cics-genapp/base/src/lgipdb01.cbl`) -> Impact: **15.2** | LOC: 84
  * *Intent:* *----------------------------------------------------------------*

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cics-genapp/base/src` | 45 | 3251.17 | 58.35% | 18.42% |
| `cics-genapp/base/cntl` | 30 | 264.92 | 0.0% | 0.0% |
| `cics-genapp/base/wsim` | 39 | 79.64 | 0.0% | 0.0% |
| `cics-genapp/base` | 5 | 9.46 | 0.0% | 0.0% |
| `cics-genapp/base/bin` | 1 | 6.24 | 0.0% | 0.0% |
| `cics-genapp` | 3 | 3.78 | 0.0% | 0.0% |
| `cics-genapp/base/data` | 2 | 2.0 | 0.0% | 0.0% |
| `cics-genapp/base/exec` | 1 | 1.58 | 0.0% | 0.0% |
| `cics-genapp/base/event-bindings` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cics-genapp/base/src/lgstsq.cbl` -> **60.8539%** Exposure
- `cics-genapp/base/src/lgacvs01.cbl` -> **58.4411%** Exposure
- `cics-genapp/base/src/lgicus01.cbl` -> **52.6018%** Exposure
- `cics-genapp/base/src/lgdpvs01.cbl` -> **51.932%** Exposure
- `cics-genapp/base/src/lgucvs01.cbl` -> **48.7748%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cics-genapp/base/src/lgapvs01.cbl` -> **100.0%** Exposure
- `cics-genapp/base/src/lgipdb01.cbl` -> **100.0%** Exposure
- `cics-genapp/base/src/lgtestp1.cbl` -> **100.0%** Exposure
- `cics-genapp/base/src/lgtestp2.cbl` -> **100.0%** Exposure
- `cics-genapp/base/src/lgtestp3.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cics-genapp/base/src/lgipdb01.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `cics-genapp/base/src/lgacvs01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `cics-genapp/base/src/lgapvs01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `cics-genapp/base/src/lgdpvs01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `cics-genapp/base/src/lgicdb01.cbl` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `cics-genapp/base/src/lgacdb01.cbl` -> **99.0093%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `68` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cics-genapp/base/src/lgicvs01.cbl` (COBOL) -> Cumulative Risk: **649.11**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.14)
- **Magnitude:** 88.3 | **LOC:** 231 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9868%), Cognitive Load (90.2227%)
- **Heaviest Functions:** `MAINLINE` (I/O & Config Routines, Impact: 19.6), `A-EXIT` (Interface Declarations, Impact: 1.1)

### 2. `cics-genapp/base/src/lgacdb01.cbl` (COBOL) -> Cumulative Risk: **639.92**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.62)
- **Magnitude:** 90.56 | **LOC:** 329 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9859%), Secrets Risk (99.0093%)
- **Heaviest Functions:** `INSERT-CUSTOMER` (I/O & Config Routines, Impact: 8.7), `MAINLINE` (I/O & Config Routines, Impact: 6.2), `WRITE-ERROR-MESSAGE` (I/O & Config Routines, Impact: 5.7)

### 3. `cics-genapp/base/src/lgapdb01.cbl` (COBOL) -> Cumulative Risk: **626.11**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.37)
- **Magnitude:** 186.96 | **LOC:** 596 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9942%), Safety Score (83.9459%)
- **Heaviest Functions:** `MAINLINE` (I/O & Config Routines, Impact: 20.2), `INSERT-POLICY` (I/O & Config Routines, Impact: 8.1), `INSERT-ENDOW` (I/O & Config Routines, Impact: 7.0)

### 4. `cics-genapp/base/src/lgipdb01.cbl` (COBOL) -> Cumulative Risk: **623.82**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.40)
- **Magnitude:** 436.08 | **LOC:** 1031 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (90.4906%)
- **Heaviest Functions:** `GET-ENDOW-DB2-INFO` (I/O & Config Routines, Impact: 16.3), `MAINLINE` (I/O & Config Routines, Impact: 15.2), `GET-MOTOR-DB2-INFO` (I/O & Config Routines, Impact: 13.7)

### 5. `cics-genapp/base/src/lgstsq.cbl` (COBOL) -> Cumulative Risk: **608.68**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.04)
- **Magnitude:** 43.8 | **LOC:** 127 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Cognitive Load (90.9363%)
- **Heaviest Functions:** `MAINLINE` (I/O & Config Routines, Impact: 8.0), `A-EXIT` (Interface Declarations, Impact: 1.1)

### 6. `cics-genapp/base/src/lgtestc1.cbl` (COBOL) -> Cumulative Risk: **592.96**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.24)
- **Magnitude:** 163.04 | **LOC:** 348 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Cognitive Load (99.3398%)
- **Heaviest Functions:** `A-GAIN` (I/O & Config Routines, Impact: 15.5), `WRITE-GENACNTL` (I/O & Config Routines, Impact: 8.2), `MAINLINE` (I/O & Config Routines, Impact: 2.8)

### 7. `cics-genapp/base/src/lgapol01.cbl` (COBOL) -> Cumulative Risk: **589.45**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.67)
- **Magnitude:** 46.88 | **LOC:** 170 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Cognitive Load (89.3175%)
- **Heaviest Functions:** `WRITE-ERROR-MESSAGE` (I/O & Config Routines, Impact: 5.7), `MAINLINE` (I/O & Config Routines, Impact: 5.3), `MAINLINE-EXIT` (Interface Declarations, Impact: 1.1)

### 8. `cics-genapp/base/src/lgacus01.cbl` (COBOL) -> Cumulative Risk: **583.96**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.93)
- **Magnitude:** 50.4 | **LOC:** 180 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9993%), Safety Score (87.8959%)
- **Heaviest Functions:** `WRITE-ERROR-MESSAGE` (I/O & Config Routines, Impact: 5.7), `MAINLINE` (I/O & Config Routines, Impact: 5.3), `INSERT-CUSTOMER` (I/O & Config Routines, Impact: 1.4)

### 9. `cics-genapp/base/src/lgicus01.cbl` (COBOL) -> Cumulative Risk: **582.57**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.52)
- **Magnitude:** 50.82 | **LOC:** 167 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%), Safety Score (87.7129%)
- **Heaviest Functions:** `WRITE-ERROR-MESSAGE` (I/O & Config Routines, Impact: 5.6), `MAINLINE` (I/O & Config Routines, Impact: 4.7), `GET-CUSTOMER-INFO` (I/O & Config Routines, Impact: 1.4)

### 10. `cics-genapp/base/src/lgdpol01.cbl` (COBOL) -> Cumulative Risk: **578.06**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.93)
- **Magnitude:** 59.02 | **LOC:** 187 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Cognitive Load (90.8631%)
- **Heaviest Functions:** `MAINLINE` (I/O & Config Routines, Impact: 8.8), `WRITE-ERROR-MESSAGE` (I/O & Config Routines, Impact: 5.7), `DELETE-POLICY-DB2-INFO` (I/O & Config Routines, Impact: 1.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cics-genapp/base/src/lgipdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 436.08 | **LOC:** 1031 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6975%), Tech Debt (11.646%)
**Top Internal Functions/Classes:**
  * `GET-ENDOW-DB2-INFO` **(I/O & Config Routines)** (Impact: 16.3)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* *----------------------------------------------------------------*
  * `GET-MOTOR-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-HOUSE-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-Commercial-DB2-INFO-1` **(I/O & Config Routines)** (Impact: 11.5)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 44`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `dead_code: 10`, `unreferenced_by_name: 3`
* *Architecture:* `io: 29`, `api: 1`, `import: 3`
* *Defense:* `safety: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgwebst5.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 238.64 | **LOC:** 803 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.789%), Tech Debt (10.2702%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 14.0)
    * *Intent:* *---------------------------------------------------------------*
  * `Tran-Rate-Interval` **(I/O & Config Routines)** (Impact: 3.5)
  * `Tran-Rate-Counts` **(I/O & Config Routines)** (Impact: 2.0)
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 76`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 199`, `unreferenced_by_name: 2`
* *Architecture:* `io: 46`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgtestp1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 190.58 | **LOC:** 319 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.8138%), Tech Debt (12.7767%)
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 101`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgapdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 186.96 | **LOC:** 596 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.1304%), Tech Debt (10.5992%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 20.2)
    * *Intent:* *----------------------------------------------------------------*
  * `INSERT-POLICY` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `INSERT-ENDOW` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* *================================================================* * Issue INSERT on endowment table...
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `INSERT-MOTOR` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* *================================================================* * Issue INSERT on motor table usi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 29`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `dead_code: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 19`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgtestp4.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 185.98 | **LOC:** 319 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8917%), Tech Debt (17.4649%)
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 24.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 100`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgtestp2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 179.08 | **LOC:** 301 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.9028%), Tech Debt (13.1787%)
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 90`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgupdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 173.78 | **LOC:** 536 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2774%), Tech Debt (11.5369%)
**Top Internal Functions/Classes:**
  * `UPDATE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 22.5)
    * *Intent:* *================================================================* * 1) Use SELECT FOR UPDATE to obt...
  * `CLOSE-PCURSOR` **(I/O & Config Routines)** (Impact: 6.0)
  * `UPDATE-MOTOR-DB2-INFO` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *================================================================* * Update row in Motor table which...
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-ENDOW-DB2-INFO` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* *================================================================* * Update row in Endowment table w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 33`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `dead_code: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 24`, `api: 1`, `import: 3`
* *Defense:* `safety: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgtestp3.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 172.22 | **LOC:** 300 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.9459%), Tech Debt (13.2666%)
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 87`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgtestc1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 163.04 | **LOC:** 348 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.3398%), Tech Debt (12.2595%)
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 15.5)
  * `WRITE-GENACNTL` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* *--------------------------------------------------------------*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 73`, `unreferenced_by_name: 1`
* *Architecture:* `io: 29`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgupvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 111.54 | **LOC:** 207 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3162%), Tech Debt (27.7521%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 12.5)
    * *Intent:* *---------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgapvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 101.42 | **LOC:** 189 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.5798%), Tech Debt (31.2669%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 10.7)
    * *Intent:* *---------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgacdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 90.56 | **LOC:** 329 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9554%), Tech Debt (14.2366%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER` **(I/O & Config Routines)** (Impact: 8.7)
    * *Intent:* *================================================================*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* *================================...
  * `Obtain-CUSTOMER-Number` **(I/O & Config Routines)** (Impact: 3.6)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `api: 1`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgicvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 88.3 | **LOC:** 231 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2227%), Tech Debt (24.7664%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 35`, `api: 1`, `concurrency: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgupol01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 84.74 | **LOC:** 202 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.8095%), Tech Debt (22.8298%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgicdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 74.42 | **LOC:** 246 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.3954%), Tech Debt (32.5864%)
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE-END` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *----------------------------------------------------------------* * END PROGRAM and return to calle...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 16`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgdpdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 73.62 | **LOC:** 246 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2824%), Tech Debt (20.506%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `DELETE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgacdb02.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 64.62 | **LOC:** 226 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.7374%), Tech Debt (21.2567%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `INSERT-CUSTOMER-PASSWORD` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgdpol01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 59.02 | **LOC:** 187 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.8631%), Tech Debt (26.6031%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `DELETE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgipvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 57.82 | **LOC:** 150 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.4191%), Tech Debt (43.8378%)
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 10.5)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 2`
* *Architecture:* `io: 14`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgucdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 56.32 | **LOC:** 223 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9758%), Tech Debt (19.2139%)
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/cntl/db2cre.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 53.42 | **LOC:** 1241 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `INSERT` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* /* //* //********************************************************************
  * `CREATE` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* //GENADB2 JOB 241901,'Db2 create',NOTIFY=&SYSUID, // CLASS=A,MSGCLASS=H //* //* (C) Copyright IBM Co...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* /* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE TABLES AND INDEXES //* <<<<<<<<<<...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* /* //* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE Commercial TABLE //* <<<<<<<<...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* /* //* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE policy TABLE //* <<<<<<<<<<<<...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Rce:* 10 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 52`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 10`
* *Architecture:* `io: 32`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgicus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 50.82 | **LOC:** 167 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1766%), Tech Debt (52.6018%)
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* *----------------------------------------------------------------*
  * `GET-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-END` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *----------------------------------------------------------------* * END PROGRAM and return to calle...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgacus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 50.4 | **LOC:** 180 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.7441%), Tech Debt (28.4743%)
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* *----------------------------------------------------------------*
  * `INSERT-CUSTOMER` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------* *--------------------------------...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LGCMAREA, LGPOLICY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgucus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 50.02 | **LOC:** 173 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.662%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.9)
    * *Intent:* *----------------------------------------------------------------*
  * `UPDATE-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-genapp/base/src/lgapol01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 46.88 | **LOC:** 170 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3175%), Tech Debt (30.691%)
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cics-genapp/base/bin/install.sh` -> **Severity: 1.282** (Embedded: 0.0187 * Error Risk: 68.383%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cics-genapp/base/cntl/adef121.jcl` -> **Severity: 608.2** (Blast Radius: 6.082 * Doc Risk: 100.0%)
- `cics-genapp/base/cntl/asmmap.jcl` -> **Severity: 608.2** (Blast Radius: 6.082 * Doc Risk: 100.0%)
- `cics-genapp/base/cntl/cdef121.jcl` -> **Severity: 608.2** (Blast Radius: 6.082 * Doc Risk: 100.0%)
- `cics-genapp/base/cntl/cdef122.jcl` -> **Severity: 608.2** (Blast Radius: 6.082 * Doc Risk: 100.0%)
- `cics-genapp/base/cntl/cdef123.jcl` -> **Severity: 608.2** (Blast Radius: 6.082 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
