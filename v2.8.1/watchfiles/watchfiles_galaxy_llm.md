# ARCHITECTURAL_BRIEF: watchfiles
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
| Total Artifacts | 42 |
| Analyzed Artifacts (Scanned) | 32 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 1954 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2968 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0338 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5417 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 16 | 1891 | 50.0% |
| PLAINTEXT | 13 | 0 | 40.6% |
| MARKDOWN | 2 | 0 | 6.2% |
| MAKEFILE | 1 | 63 | 3.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Typed Library` (z +1.37; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 56%, Defensive Guards Files 12%, Generic / Templated Code Files 9%, Large Core Modules 9%, Declarative / Non-Code 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17 | 53.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 46.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 69.9 | 24.0 | 17.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.2 | 48.8 | 62.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 78.8 | 24.4 | 13.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.3 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 76.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 63.3 | 75.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 92 | 8 | 8 | `watchfiles-1.1.1/tests/test_rust_notify.py` |
| cleanup | 18 | 4 | 1 | `watchfiles-1.1.1/Makefile` |
| guards | 202 | 11 | 22 | `watchfiles-1.1.1/tests/test_run_process.py` |
| danger | 77 | 9 | 8 | `watchfiles-1.1.1/watchfiles/run.py` |
| concurrency | 75 | 5 | 9 | `watchfiles-1.1.1/tests/test_watch.py` |
| connectivity | 204 | 15 | 21 | `watchfiles-1.1.1/tests/test_run_process.py` |
| io | 119 | 10 | 6 | `watchfiles-1.1.1/tests/test_cli.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 2 | 0 | `watchfiles-1.1.1/watchfiles/run.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 3 | 3 | 0 | `watchfiles-1.1.1/tests/test_filters.py` |
| events | 35 | 4 | 3 | `watchfiles-1.1.1/watchfiles/run.py` |
| tests | 238 | 8 | 33 | `watchfiles-1.1.1/tests/test_cli.py` |
| docs | 43 | 7 | 6 | `watchfiles-1.1.1/watchfiles/filters.py` |
| debt | 6 | 3 | 0 | `watchfiles-1.1.1/tests/conftest.py` |
| mutation | 778 | 14 | 89 | `watchfiles-1.1.1/tests/test_cli.py` |
| dead_code | 106 | 7 | 17 | `watchfiles-1.1.1/tests/test_rust_notify.py` |
| credential | 0 | 0 | 0 | - |
| threat | 16 | 7 | 2 | `watchfiles-1.1.1/watchfiles/run.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `watchfiles-1.1.1/tests/test_cli.py` (Hits: 55)
- `watchfiles-1.1.1/tests/test_run_process.py` (Hits: 28)
- `watchfiles-1.1.1/watchfiles/run.py` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 7 inbound connections
2. **conftest.py** (`watchfiles-1.1.1/tests/conftest.py`) — 5 inbound connections
3. **filters.py** (`watchfiles-1.1.1/watchfiles/filters.py`) — 4 inbound connections
4. **_rust_notify.pyi** (`watchfiles-1.1.1/watchfiles/_rust_notify.pyi`) — 3 inbound connections
5. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 23 outbound dependencies
2. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 14 outbound dependencies
3. **cli.py** (`watchfiles-1.1.1/watchfiles/cli.py`) — 13 outbound dependencies
4. **test_run_process.py** (`watchfiles-1.1.1/tests/test_run_process.py`) — 12 outbound dependencies
5. **test_watch.py** (`watchfiles-1.1.1/tests/test_watch.py`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `awatch` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/main.py`) -> Impact: **70.4** | LOC: 136
- `watch` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/main.py`) -> Impact: **53.6** | LOC: 99
- `cli` **(Compute Cores)** (@ `watchfiles-1.1.1/watchfiles/cli.py`) -> Impact: **39.0** | LOC: 157
  * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file changes. Example of watching the current directory a...
- `run_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **34.3** | LOC: 126
- `arun_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **33.8** | LOC: 78
- `start_process` **(Many-Argument Workhorses)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **33.5** | LOC: 34
- `build_filter` **(Defensive Guards)** (@ `watchfiles-1.1.1/watchfiles/cli.py`) -> Impact: **23.9** | LOC: 28
- `__call__` **(Compute Cores)** (@ `watchfiles-1.1.1/watchfiles/filters.py`) -> Impact: **17.1** | LOC: 21
  * *Intent:* """ Instances of `BaseFilter` subclasses can be used as callables. Args: change: The type of change that occurred, see [`Change`][watchfiles.Change]. ...
- `stop` **(Defensive Guards)** (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **11.2** | LOC: 23
- `__init__` **(Generic / Templated Code)** (@ `watchfiles-1.1.1/watchfiles/filters.py`) -> Impact: **10.0** | LOC: 21

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `watchfiles-1.1.1/tests` | 8 | 974.52 | 23.75% | 0.0% |
| `watchfiles-1.1.1/watchfiles` | 8 | 870.82 | 27.05% | 0.0% |
| `watchfiles-1.1.1` | 2 | 40.64 | 1.03% | 0.0% |
| `watchfiles-1.1.1/tests/test_files/dir_a` | 8 | 8.0 | 0.0% | 0.0% |
| `watchfiles-1.1.1/tests/test_files` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **100.0%** Exposure
- `watchfiles-1.1.1/watchfiles/main.py` -> **100.0%** Exposure
- `watchfiles-1.1.1/watchfiles/run.py` -> **99.9981%** Exposure
- `watchfiles-1.1.1/watchfiles/cli.py` -> **99.9894%** Exposure
- `watchfiles-1.1.1/watchfiles/__init__.py` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `watchfiles-1.1.1/tests/test_rust_notify.py` -> **29** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_run_process.py` -> **21** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_watch.py` -> **21** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_cli.py` -> **17** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_filters.py` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `108` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `watchfiles-1.1.1/watchfiles/run.py` (PYTHON) -> Cumulative Risk: **724.54**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.61)
- **Magnitude:** 297.14 | **LOC:** 439 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9981%), Concurrency (99.9971%), Safety Score (89.8959%)
- **Heaviest Functions:** `run_process` (Many-Argument Workhorses, Impact: 34.3), `arun_process` (Many-Argument Workhorses, Impact: 33.8), `start_process` (Many-Argument Workhorses, Impact: 33.5)

### 2. `watchfiles-1.1.1/watchfiles/main.py` (PYTHON) -> Cumulative Risk: **600.78**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.42)
- **Magnitude:** 289.28 | **LOC:** 374 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.7109%), Safety Score (92.1748%)
- **Heaviest Functions:** `awatch` (Many-Argument Workhorses, Impact: 70.4), `watch` (Many-Argument Workhorses, Impact: 53.6), `_prep_changes` (Generic / Templated Code, Impact: 9.1)

### 3. `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON) -> Cumulative Risk: **497.34**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.18)
- **Magnitude:** 83.6 | **LOC:** 150 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.117%), Documentation (81.8182%)
- **Heaviest Functions:** `__call__` (Compute Cores, Impact: 17.1), `__init__` (Generic / Templated Code, Impact: 10.0), `__call__` (Generic / Templated Code, Impact: 4.1)

### 4. `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON) -> Cumulative Risk: **490.88**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.08)
- **Magnitude:** 132.44 | **LOC:** 225 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9894%), Safety Score (83.8401%), Documentation (66.6667%)
- **Heaviest Functions:** `cli` (Compute Cores, Impact: 39.0), `build_filter` (Defensive Guards, Impact: 23.9), `resolve_path` (Generic / Templated Code, Impact: 4.5)

### 5. `watchfiles-1.1.1/tests/test_watch.py` (PYTHON) -> Cumulative Risk: **459.01**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.48)
- **Magnitude:** 268.06 | **LOC:** 241 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_awatch_interrupt_warning` (Defensive Guards, Impact: 5.6), `test_awatch_unexpected_signal` (Defensive Guards, Impact: 4.7), `test_awatch_no_yield` (Defensive Guards, Impact: 4.2)

### 6. `watchfiles-1.1.1/tests/conftest.py` (PYTHON) -> Cumulative Risk: **458.16**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.65)
- **Magnitude:** 128.66 | **LOC:** 205 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (91.1111%), Api Exposure (78.8067%), Safety Score (76.7079%)
- **Heaviest Functions:** `__exit__` (Compute Cores, Impact: 8.6), `watch` (Defensive Guards, Impact: 5.3), `test_dir` (Interface Declarations, Impact: 4.5)

### 7. `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON) -> Cumulative Risk: **418.08**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.40)
- **Magnitude:** 193.6 | **LOC:** 280 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9998%), Stability (50.0%)
- **Heaviest Functions:** `test_alive_terminates` (Defensive Guards, Impact: 6.7), `test_function_string_not_win` (Defensive Guards, Impact: 6.7), `test_command_with_args` (Defensive Guards, Impact: 6.7)

### 8. `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON) -> Cumulative Risk: **350.7**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.24)
- **Magnitude:** 23.92 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (69.1195%), Api Exposure (64.787%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Generic / Templated Code, Impact: 3.3), `watch` (Generic / Templated Code, Impact: 2.8), `__exit__` (Generic / Templated Code, Impact: 1.8)

### 9. `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON) -> Cumulative Risk: **347.16**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.86)
- **Magnitude:** 53.2 | **LOC:** 105 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (71.095%), Stability (50.0%)
- **Heaviest Functions:** `test_default_force_polling_wsl` (Defensive Guards, Impact: 5.6), `test_default_force_polling` (Defensive Guards, Impact: 5.2), `test_watch_polling_env` (Tests & Verification, Impact: 3.9)

### 10. `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON) -> Cumulative Risk: **333.44**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +2.19)
- **Magnitude:** 195.7 | **LOC:** 343 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Safety Score (45.2147%)
- **Heaviest Functions:** `test_move_internal` (Type Conversions, Impact: 5.3), `test_default_ignore_permission_denied` (Defensive Guards, Impact: 4.7), `test_does_not_exist_message` (Type Conversions, Impact: 4.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `watchfiles-1.1.1/watchfiles/run.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 297.14 | **LOC:** 439 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_process` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `arun_process` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `start_process` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `stop` **(Defensive Guards)** (Impact: 11.2)
  * `detect_target_type` **(Defensive Guards)** (Impact: 8.6)
    * *Intent:* """ Used by [`run_process`][watchfiles.run_process], [`arun_process`][watchfiles.arun_process] and i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 84`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 3`, `state_mutation: 29`
* *Architecture:* `io: 8`, `api: 19`, `concurrency: 10`, `import: 21`
* *Defense:* `safety: 21`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.49
  * `Choke Point (Betweenness):` 0.002151 | `Ripple Effect (Closeness):` 0.115207
  * `Imports (Out-Degree: 2):` .filters, .main, anyio, asyncio, contextlib, fails., importlib, inspect...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/main.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 289.28 | **LOC:** 374 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3492%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `awatch` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `watch` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `_prep_changes` **(Generic / Templated Code)** (Impact: 9.1)
  * `_log_changes` **(Generic / Templated Code)** (Impact: 8.9)
  * `_calc_async_timeout` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* """ see https://github.com/samuelcolvin/watchfiles/issues/110 """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 59`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 6`, `import: 14`
* *Defense:* `safety: 1`, `doc: 11`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 162.255
  * `Choke Point (Betweenness):` 0.009677 | `Ripple Effect (Closeness):` 0.215054
  * `Imports (Out-Degree: 2):` ._rust_notify, .filters, anyio, asyncio, enum, logging, os, pathlib...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_watch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 268.06 | **LOC:** 241 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_awatch_interrupt_warning` **(Defensive Guards)** (Impact: 5.6)
  * `test_awatch_unexpected_signal` **(Defensive Guards)** (Impact: 4.7)
  * `test_awatch_no_yield` **(Defensive Guards)** (Impact: 4.2)
  * `test_watch_timeout` **(Defensive Guards)** (Impact: 4.2)
  * `test_awatch_timeout` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 92`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 27`, `unreferenced_by_name: 21`
* *Architecture:* `io: 3`, `api: 22`, `concurrency: 20`, `import: 12`
* *Defense:* `safety: 37`, `test: 27`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` anyio, conftest, contextlib, exceptiongroup, pathlib, pytest, sys, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 195.7 | **LOC:** 343 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.8445%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_move_internal` **(Type Conversions)** (Impact: 5.3)
    * *Intent:* # can't use tmp_path as it causes problems on Windows (different drive), and macOS (delayed events) ...
  * `test_default_ignore_permission_denied` **(Defensive Guards)** (Impact: 4.7)
  * `test_does_not_exist_message` **(Type Conversions)** (Impact: 4.4)
  * `test_does_not_exist_polling` **(Type Conversions)** (Impact: 4.4)
  * `test_wrong_type_event_is_set` **(Type Conversions)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 86`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 29`
* *Architecture:* `io: 5`, `api: 30`, `import: 9`
* *Defense:* `safety: 28`, `test: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .conftest, os, pathlib, pytest, re, sys, typing, watchfiles._rust_notify...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 193.6 | **LOC:** 280 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.382%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_alive_terminates` **(Defensive Guards)** (Impact: 6.7)
  * `test_function_string_not_win` **(Defensive Guards)** (Impact: 6.7)
  * `test_command_with_args` **(Defensive Guards)** (Impact: 6.7)
  * `poll` **(Compute Cores)** (Impact: 4.3)
  * `join` **(Parameter Forwarders)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 3 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 43
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 121`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 39`, `unreferenced_by_name: 21`
* *Architecture:* `io: 28`, `api: 30`, `concurrency: 8`, `import: 12`
* *Defense:* `safety: 54`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` conftest, dirty_equals, multiprocessing.context, os, pathlib, pytest, subprocess, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 132.44 | **LOC:** 225 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.7422%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cli` **(Compute Cores)** (Impact: 39.0)
    * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file ch...
  * `build_filter` **(Defensive Guards)** (Impact: 23.9)
  * `resolve_path` **(Generic / Templated Code)** (Impact: 4.5)
  * `import_exit` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 53`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `io: 6`, `api: 4`, `import: 12`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.966
  * `Choke Point (Betweenness):` 0.010753 | `Ripple Effect (Closeness):` 0.064516
  * `Imports (Out-Degree: 3):` , .filters, .run, .version, argparse, logging, of, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 128.66 | **LOC:** 205 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7309%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__exit__` **(Compute Cores)** (Impact: 8.6)
  * `watch` **(Defensive Guards)** (Impact: 5.3)
  * `test_dir` **(Interface Declarations)** (Impact: 4.5)
  * `clear` **(Interface Declarations)** (Impact: 3.0)
  * `write_soon` **(Interface Declarations)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 56`, `args: 26`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 31`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 21`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 2`, `doc: 3`, `test: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.613
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.16129
  * `Imports (Out-Degree: 0):` logging, os, pathlib, pytest, sys, threading, time, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 84.16 | **LOC:** 332 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_args` **(Many-Argument Workhorses)** (Impact: 3.3)
  * `test_ignore_paths` **(Tests & Verification)** (Impact: 3.1)
  * `test_filter_all` **(Defensive Guards)** (Impact: 3.0)
  * `test_args_command` **(Many-Argument Workhorses)** (Impact: 3.0)
  * `test_function` **(Tests & Verification)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 3 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 16`, `unreferenced_by_name: 17`
* *Architecture:* `io: 55`, `api: 18`, `import: 7`
* *Defense:* `safety: 15`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirty_equals, os, pathlib, pytest, sys, watchfiles, watchfiles.cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 83.6 | **LOC:** 150 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """ Instances of `BaseFilter` subclasses can be used as callables. Args: change: The type of change ...
  * `__init__` **(Generic / Templated Code)** (Impact: 10.0)
  * `__call__` **(Generic / Templated Code)** (Impact: 4.1)
  * `__init__` **(Type Conversions)** (Impact: 3.0)
  * `__repr__` **(Generic / Templated Code)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 3`, `api: 5`, `import: 6`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 118.979
  * `Choke Point (Betweenness):` 0.001613 | `Ripple Effect (Closeness):` 0.201613
  * `Imports (Out-Degree: 1):` .main, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 53.2 | **LOC:** 105 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1495%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_default_force_polling_wsl` **(Defensive Guards)** (Impact: 5.6)
  * `test_default_force_polling` **(Defensive Guards)** (Impact: 5.2)
  * `test_watch_polling_env` **(Tests & Verification)** (Impact: 3.9)
  * `test_watch_polling_env_with_custom_delay` **(Tests & Verification)** (Impact: 3.9)
  * `test_watch_polling_not_env` **(Tests & Verification)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 3`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .conftest, __future__, pytest, typing, watchfiles, watchfiles.main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 40.62 | **LOC:** 101 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` **(Generic / Templated Code)** (Impact: 4.1)
  * `test_web_filter` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* # test case from docs class WebFilter(DefaultFilter): allowed_extensions = '.html', '.css', '.js' de...
  * `test_default_filter` **(Type Conversions)** (Impact: 1.9)
  * `test_simple_function` **(Generic / Templated Code)** (Impact: 1.8)
  * `only_added` **(Generic / Templated Code)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 11`, `import: 8`
* *Defense:* `safety: 16`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` conftest, dirty_equals, pathlib, pytest, re, sys, typing, watchfiles
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 38.46 | **LOC:** 78 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.0653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `.uv` **(I/O & Config Routines)** (Impact: 2.2)
  * `.pre-commit` **(I/O & Config Routines)** (Impact: 2.2)
  * `clean` **(I/O & Config Routines)** (Impact: 1.5)
  * `lint-rust` **(I/O & Config Routines)** (Impact: 1.4)
  * `format` **(I/O & Config Routines)** (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 18`
* *Defense:* `doc: 3`, `test: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 23.92 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 3.3)
  * `watch` **(Generic / Templated Code)** (Impact: 2.8)
  * `__exit__` **(Generic / Templated Code)** (Impact: 1.8)
    * *Intent:* """ Calls [`close`][watchfiles._rust_notify.RustNotify.close]. """
  * `is_set` **(Generic / Templated Code)** (Impact: 1.5)
  * `__enter__` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Does nothing, but allows `RustNotify` to be used as a context manager. !!! note The watching the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 119.419
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.201964
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__init__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 18.32 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .filters, .main, .run, .version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/version.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14.56 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.666
  * `Choke Point (Betweenness):` 0.003763 | `Ripple Effect (Closeness):` 0.086022
  * `Imports (Out-Degree: 1):` ._rust_notify
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__main__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.18 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/b.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/c.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/c_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/dir_a/a.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.025
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

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 1.075** (Bridge: 0.0108 * Flux: 99.9894%)
- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 0.968** (Bridge: 0.0097 * Flux: 100.0%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 0.215** (Bridge: 0.0022 * Flux: 99.9981%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 0.161** (Bridge: 0.0016 * Flux: 100.0%)
- `watchfiles-1.1.1/watchfiles/version.py` -> **Severity: 0.117** (Bridge: 0.0038 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 19.823** (Embedded: 0.2151 * Error Risk: 92.1748%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 18.37** (Embedded: 0.2016 * Error Risk: 91.117%)
- `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` -> **Severity: 13.96** (Embedded: 0.202 * Error Risk: 69.1195%)
- `watchfiles-1.1.1/tests/conftest.py` -> **Severity: 12.372** (Embedded: 0.1613 * Error Risk: 76.7079%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 10.357** (Embedded: 0.1152 * Error Risk: 89.8959%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 12169.125** (Blast Radius: 162.255 * Doc Risk: 75.0%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 9734.648** (Blast Radius: 118.979 * Doc Risk: 81.8182%)
- `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` -> **Severity: 5970.95** (Blast Radius: 119.419 * Doc Risk: 50.0%)
- `watchfiles-1.1.1/tests/conftest.py` -> **Severity: 5066.962** (Blast Radius: 55.613 * Doc Risk: 91.1111%)
- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 3064.402** (Blast Radius: 45.966 * Doc Risk: 66.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
