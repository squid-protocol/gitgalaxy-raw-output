# ARCHITECTURAL_BRIEF: exceptiongroup
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
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 17 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 2376 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7746 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 17 | 2376 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Defensive Guards Files 24%, Data / Markup / Trivial 18%, Declarative / Non-Code 18%, Generic / Templated Code Files 18%, Large Core Modules 12%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.8 | 27.7 | 18.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 57.6 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 81.8 | 7.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.3 | 0.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 61.2 | 14.6 | 9.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 16.8 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 63.1 | 94.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 28 | 9 | 4 | `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 370 | 11 | 69 | `exceptiongroup-1.3.1/tests/test_catch_py311.py` |
| danger | 194 | 13 | 29 | `exceptiongroup-1.3.1/tests/test_exceptions.py` |
| concurrency | 23 | 3 | 1 | `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` |
| connectivity | 190 | 13 | 20 | `exceptiongroup-1.3.1/tests/test_exceptions.py` |
| io | 95 | 12 | 6 | `exceptiongroup-1.3.1/tests/test_formatting.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 2 | 0 | `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `exceptiongroup-1.3.1/tests/test_formatting.py` |
| regex | 0 | 0 | 0 | - |
| events | 28 | 4 | 7 | `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` |
| tests | 149 | 6 | 28 | `exceptiongroup-1.3.1/tests/test_exceptions.py` |
| docs | 17 | 8 | 1 | `exceptiongroup-1.3.1/tests/test_formatting.py` |
| debt | 13 | 6 | 2 | `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` |
| mutation | 851 | 15 | 144 | `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` |
| dead_code | 88 | 6 | 14 | `exceptiongroup-1.3.1/tests/test_exceptions.py` |
| credential | 0 | 0 | 0 | - |
| threat | 37 | 5 | 8 | `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8571**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `exceptiongroup-1.3.1/tests/test_formatting.py` (Hits: 61)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (Hits: 13)
- `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_exceptions.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`) — 4 inbound connections
2. **_catch.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) — 1 inbound connections
3. **_formatting.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) — 1 inbound connections
4. **_suppress.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py`) — 1 inbound connections
5. **_version.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_version.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_formatting.py** (`exceptiongroup-1.3.1/tests/test_formatting.py`) — 12 outbound dependencies
2. **__init__.py** (`exceptiongroup-1.3.1/src/exceptiongroup/__init__.py`) — 10 outbound dependencies
3. **_formatting.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) — 10 outbound dependencies
4. **_catch.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) — 8 outbound dependencies
5. **_exceptions.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **143.1** | LOC: 142
- `format` **(Many-Argument Workhorses)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **87.1** | LOC: 88
- `split_exception_group` **(Compute Cores)** (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **63.1** | LOC: 62
  * *Intent:* """Split an EG and do some sanity checks on the result"""
- `_levenshtein_distance` **(Many-Argument Workhorses)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **47.0** | LOC: 59
  * *Intent:* # A Python implementation of Python/suggestions.c:levenshtein_distance. # Both strings are the same if a == b: return 0 # Trim away common affixes pre...
- `test_split_by_type` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **30.5** | LOC: 100
- `handle_exception` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) -> Impact: **29.9** | LOC: 44
- `__new__` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`) -> Impact: **29.9** | LOC: 39
- `_compute_suggestion_error` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **28.3** | LOC: 47
- `test_split_ExceptionGroup_subclass_derive_and_new_overrides` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **27.1** | LOC: 62
- `catch` **(Defensive Guards)** (@ `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) -> Impact: **21.9** | LOC: 43

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `exceptiongroup-1.3.1/tests` | 11 | 1238.72 | 10.43% | 0.0% |
| `exceptiongroup-1.3.1/src/exceptiongroup` | 6 | 1209.02 | 59.34% | 19.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **81.7574%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **37.2482%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **100.0%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` -> **99.9997%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **99.9897%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **99.9872%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` -> **99.9665%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `exceptiongroup-1.3.1/tests/test_exceptions.py` -> **46** Orphaned Functions | **2** Duplicates
- `exceptiongroup-1.3.1/tests/test_formatting.py` -> **16** Orphaned Functions | **0** Duplicates
- `exceptiongroup-1.3.1/tests/test_catch.py` -> **14** Orphaned Functions | **0** Duplicates
- `exceptiongroup-1.3.1/tests/test_catch_py311.py` -> **10** Orphaned Functions | **0** Duplicates
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **0** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `76` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` (PYTHON) -> Cumulative Risk: **615.3**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.12)
- **Magnitude:** 239.06 | **LOC:** 337 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9872%), Cognitive Load (84.7693%)
- **Heaviest Functions:** `__new__` (Defensive Guards, Impact: 29.9), `subgroup` (Compute Cores, Impact: 20.7), `get_condition_filter` (Defensive Guards, Impact: 13.5)

### 2. `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` (PYTHON) -> Cumulative Risk: **561.54**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.62)
- **Magnitude:** 29.84 | **LOC:** 56 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Tech Debt (81.7574%)
- **Heaviest Functions:** `__exit__` (Many-Argument Workhorses, Impact: 14.9), `__init__` (Generic / Templated Code, Impact: 1.8), `__enter__` (Generic / Templated Code, Impact: 1.5)

### 3. `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (PYTHON) -> Cumulative Risk: **553.11**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.21)
- **Magnitude:** 764.74 | **LOC:** 603 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1013%), Cognitive Load (94.8173%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 143.1), `format` (Many-Argument Workhorses, Impact: 87.1), `_levenshtein_distance` (Many-Argument Workhorses, Impact: 47.0)

### 4. `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` (PYTHON) -> Cumulative Risk: **529.46**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.48)
- **Magnitude:** 110.08 | **LOC:** 139 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9897%), Safety Score (82.7379%)
- **Heaviest Functions:** `handle_exception` (Defensive Guards, Impact: 29.9), `catch` (Defensive Guards, Impact: 21.9), `__exit__` (Defensive Guards, Impact: 14.7)

### 5. `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (PYTHON) -> Cumulative Risk: **371.97**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.63)
- **Magnitude:** 37.24 | **LOC:** 68 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (95.1794%), Stability (50.0%)
- **Heaviest Functions:** `run_script` (Type Conversions, Impact: 5.4), `test_apport_excepthook_monkeypatch_interaction` (Interface Declarations, Impact: 1.9)

### 6. `exceptiongroup-1.3.1/tests/test_formatting.py` (PYTHON) -> Cumulative Risk: **362.75**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.18)
- **Magnitude:** 347.92 | **LOC:** 578 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (75.2973%), Stability (50.0%)
- **Heaviest Functions:** `test_print_exception` (Many-Argument Workhorses, Impact: 20.4), `test_format_exception` (Defensive Guards, Impact: 19.1), `test_format_nested` (Defensive Guards, Impact: 14.4)

### 7. `exceptiongroup-1.3.1/tests/test_exceptions.py` (PYTHON) -> Cumulative Risk: **350.9**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.16)
- **Magnitude:** 632.32 | **LOC:** 889 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (95.9184%), Safety Score (54.4922%), Stability (50.0%)
- **Heaviest Functions:** `split_exception_group` (Compute Cores, Impact: 63.1), `test_split_by_type` (Defensive Guards, Impact: 30.5), `test_split_ExceptionGroup_subclass_derive_and_new_overrides` (Defensive Guards, Impact: 27.1)

### 8. `exceptiongroup-1.3.1/tests/check_types.py` (PYTHON) -> Cumulative Risk: **324.16**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.14)
- **Magnitude:** 9.98 | **LOC:** 42 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (64.5656%), Stability (50.0%)
- **Heaviest Functions:** `value_key_err_handler` (Generic / Templated Code, Impact: 3.0), `runtime_err_handler` (Generic / Templated Code, Impact: 1.5)

### 9. `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` (PYTHON) -> Cumulative Risk: **314.14**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.04)
- **Magnitude:** 35.52 | **LOC:** 35 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9997%), Safety Score (87.7764%), Cognitive Load (53.9915%), Stability (50.0%)

### 10. `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` (PYTHON) -> Cumulative Risk: **296.04**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.69)
- **Magnitude:** 29.78 | **LOC:** 47 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9665%), Safety Score (81.1095%), Stability (50.0%), Cognitive Load (37.2852%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 764.74 | **LOC:** 603 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8173%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 143.1)
  * `format` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `_levenshtein_distance` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* # A Python implementation of Python/suggestions.c:levenshtein_distance. # Both strings are the same ...
  * `_compute_suggestion_error` **(Defensive Guards)** (Impact: 28.3)
  * `format_exception_only` **(Defensive Guards)** (Impact: 20.8)
    * *Intent:* """Format the exception part of the traceback. The return value is a generator of strings, each endi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 91`, `args: 21`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 135`
* *Architecture:* `io: 13`, `api: 10`, `import: 11`
* *Defense:* `safety: 17`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` ._exceptions, __future__, apport_python_hook, collections.abc, functools, sys, textwrap, traceback...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/test_exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 632.32 | **LOC:** 889 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.308%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `split_exception_group` **(Compute Cores)** (Impact: 63.1)
    * *Intent:* """Split an EG and do some sanity checks on the result"""
  * `test_split_by_type` **(Defensive Guards)** (Impact: 30.5)
  * `test_split_ExceptionGroup_subclass_derive_and_new_overrides` **(Defensive Guards)** (Impact: 27.1)
  * `test_split_ExceptionGroup_subclass_no_derive_no_new_override` **(Defensive Guards)** (Impact: 14.9)
  * `test_split_BaseExceptionGroup_subclass_no_derive_new_override` **(Defensive Guards)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 181`, `args: 74`, `func_start: 68`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 93`, `duplicate_logic: 2`, `unreferenced_by_name: 46`
* *Architecture:* `io: 4`, `api: 87`, `import: 6`
* *Defense:* `safety: 69`, `doc: 2`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections.abc, exceptiongroup, platform, pytest, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_formatting.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 347.92 | **LOC:** 578 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.8758%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_print_exception` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `test_format_exception` **(Defensive Guards)** (Impact: 19.1)
  * `test_format_nested` **(Defensive Guards)** (Impact: 14.4)
  * `test_print_exc` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `test_format_exception_only` **(Defensive Guards)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 49 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 128`, `args: 28`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 69`, `unreferenced_by_name: 16`
* *Architecture:* `io: 61`, `api: 20`, `import: 20`
* *Defense:* `safety: 56`, `doc: 9`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _pytest.capture, _pytest.fixtures, _pytest.monkeypatch, exceptiongroup, pathlib, pickle, pytest, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 239.06 | **LOC:** 337 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.7693%), Tech Debt (37.2482%)
**Top Internal Functions/Classes:**
  * `__new__` **(Defensive Guards)** (Impact: 29.9)
  * `subgroup` **(Compute Cores)** (Impact: 20.7)
  * `get_condition_filter` **(Defensive Guards)** (Impact: 13.5)
  * `add_note` **(Defensive Guards)** (Impact: 5.7)
  * `check_direct_subclass` **(Generic / Templated Code)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 94`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 28`, `import: 7`
* *Defense:* `safety: 14`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 199.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` __future__, collections.abc, functools, inspect, sys, typing, typing_extensions
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 110.08 | **LOC:** 139 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2452%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_exception` **(Defensive Guards)** (Impact: 29.9)
  * `catch` **(Defensive Guards)** (Impact: 21.9)
  * `__exit__` **(Defensive Guards)** (Impact: 14.7)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `__enter__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 45`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 5`, `import: 8`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` ._exceptions, __future__, collections.abc, contextlib, inspect, sys, types, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/test_catch.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 88.78 | **LOC:** 223 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.781%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_async_handler` **(Interface Declarations)** (Impact: 3.4)
  * `test_catch_ungrouped` **(Defensive Guards)** (Impact: 3.3)
  * `test_bare_raise_in_handler` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """Test that a bare "raise" "middle" ecxeption group gets discarded."""
  * `test_catch_exceptiongroup` **(Callbacks & Closures)** (Impact: 3.0)
  * `test_catch_handler_raises` **(Defensive Guards)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 99`, `args: 24`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 18`, `unreferenced_by_name: 14`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 74`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_catch_py311.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 65.1 | **LOC:** 191 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_catch_ungrouped` **(Defensive Guards)** (Impact: 3.2)
  * `test_catch_handler_raises` **(Defensive Guards)** (Impact: 2.7)
  * `test_catch_no_match` **(Defensive Guards)** (Impact: 2.6)
  * `test_catch_group` **(Defensive Guards)** (Impact: 2.5)
  * `test_catch_single_no_match` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 78`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 24`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 10`, `import: 3`
* *Defense:* `safety: 91`, `doc: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 37.24 | **LOC:** 68 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.5966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_script` **(Type Conversions)** (Impact: 5.4)
  * `test_apport_excepthook_monkeypatch_interaction` **(Interface Declarations)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 2`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, exceptiongroup, os, pathlib, pytest, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 35.52 | **LOC:** 35 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9915%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 29.84 | **LOC:** 56 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9549%), Tech Debt (81.7574%)
**Top Internal Functions/Classes:**
  * `__exit__` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.8)
  * `__enter__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 6`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` ._exceptions, __future__, contextlib, sys, types, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 29.78 | **LOC:** 47 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2852%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 3`, `api: 1`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , ._catch, ._exceptions, ._formatting, ._suppress, ._version, contextlib, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/dummyscript.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 15.68 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pickle, sys, traceback
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14.56 | **LOC:** 5 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0086%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/apport_excepthook.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 14.12 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` apport_python_hook, exceptiongroup, it, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/check_types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.98 | **LOC:** 42 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `value_key_err_handler` **(Generic / Templated Code)** (Impact: 3.0)
    * *Intent:* # code snippets from the README
  * `runtime_err_handler` **(Generic / Templated Code)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, typing_extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_suppress.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2.5 | **LOC:** 17 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_suppress_exception` **(Tests & Verification)** (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `safety: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, pytest, sys
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

- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **Severity: 20.536** (Embedded: 0.25 * Error Risk: 82.1446%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **Severity: 6.194** (Embedded: 0.0625 * Error Risk: 99.1013%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` -> **Severity: 5.486** (Embedded: 0.0625 * Error Risk: 87.7764%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **Severity: 5.171** (Embedded: 0.0625 * Error Risk: 82.7379%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **Severity: 4.968** (Embedded: 0.0625 * Error Risk: 79.4829%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **Severity: 19936.4** (Blast Radius: 199.364 * Doc Risk: 100.0%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **Severity: 5616.0** (Blast Radius: 56.16 * Doc Risk: 100.0%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **Severity: 5616.0** (Blast Radius: 56.16 * Doc Risk: 100.0%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **Severity: 5134.63** (Blast Radius: 56.16 * Doc Risk: 91.4286%)
- `exceptiongroup-1.3.1/tests/check_types.py` -> **Severity: 4800.0** (Blast Radius: 48.0 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
