# ARCHITECTURAL_BRIEF: filelock
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
| Total Artifacts | 31 |
| Analyzed Artifacts (Scanned) | 25 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 3853 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2086 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4968 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4576 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 24 | 3853 | 96.0% |
| MARKDOWN | 1 | 0 | 4.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 44%, Defensive Guards Files 24%, Large Core Modules 12%, Declarative / Non-Code 8%, Tests & Verification Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 24 | 96.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 74.0 | 37.2 | 44.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.5 | 51.6 | 47.1 | 85.1 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 10.2 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 3.5 | 61.2 | 20.2 | 12.3 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 41.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 28.0 | 2.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 91.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 72.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 145 | 14 | 15 | `filelock-3.25.2/tests/test_filelock.py` |
| cleanup | 25 | 7 | 4 | `filelock-3.25.2/src/filelock/_read_write.py` |
| guards | 600 | 23 | 69 | `filelock-3.25.2/tests/test_filelock.py` |
| danger | 114 | 16 | 15 | `filelock-3.25.2/tests/test_filelock.py` |
| concurrency | 350 | 15 | 48 | `filelock-3.25.2/tests/test_async_read_write.py` |
| connectivity | 360 | 24 | 27 | `filelock-3.25.2/tests/test_filelock.py` |
| io | 183 | 20 | 18 | `filelock-3.25.2/tests/test_filelock.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `filelock-3.25.2/tests/test_read_write.py` |
| time | 21 | 5 | 2 | `filelock-3.25.2/tests/test_read_write.py` |
| serialization | 1 | 1 | 0 | `filelock-3.25.2/tests/test_error.py` |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 597 | 12 | 68 | `filelock-3.25.2/tests/test_filelock.py` |
| docs | 101 | 12 | 17 | `filelock-3.25.2/src/filelock/_api.py` |
| debt | 1 | 1 | 0 | `filelock-3.25.2/src/filelock/_api.py` |
| mutation | 1650 | 24 | 164 | `filelock-3.25.2/tests/test_filelock.py` |
| dead_code | 239 | 14 | 24 | `filelock-3.25.2/tests/test_filelock.py` |
| credential | 0 | 0 | 0 | - |
| threat | 39 | 9 | 5 | `filelock-3.25.2/src/filelock/_api.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `filelock-3.25.2/tests/test_filelock.py` (Hits: 63)
- `filelock-3.25.2/src/filelock/_soft.py` (Hits: 19)
- `filelock-3.25.2/tests/test_soft_stale.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_api.py** (`filelock-3.25.2/src/filelock/_api.py`) — 7 inbound connections
2. **_read_write.py** (`filelock-3.25.2/src/filelock/_read_write.py`) — 7 inbound connections
3. **_error.py** (`filelock-3.25.2/src/filelock/_error.py`) — 4 inbound connections
4. **_soft.py** (`filelock-3.25.2/src/filelock/_soft.py`) — 3 inbound connections
5. **_util.py** (`filelock-3.25.2/src/filelock/_util.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **asyncio.py** (`filelock-3.25.2/src/filelock/asyncio.py`) — 20 outbound dependencies
2. **_api.py** (`filelock-3.25.2/src/filelock/_api.py`) — 19 outbound dependencies
3. **test_filelock.py** (`filelock-3.25.2/tests/test_filelock.py`) — 19 outbound dependencies
4. **_read_write.py** (`filelock-3.25.2/src/filelock/_read_write.py`) — 14 outbound dependencies
5. **__init__.py** (`filelock-3.25.2/src/filelock/__init__.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `acquire` **(Many-Argument Workhorses)** (@ `filelock-3.25.2/src/filelock/_api.py`) -> Impact: **52.9** | LOC: 106
- `__call__` **(Many-Argument Workhorses)** (@ `filelock-3.25.2/src/filelock/_api.py`) -> Impact: **36.4** | LOC: 64
- `acquire` **(Many-Argument Workhorses)** (@ `filelock-3.25.2/src/filelock/asyncio.py`) -> Impact: **23.6** | LOC: 80
- `open_permission_then_unlink` **(Compute Cores)** (@ `filelock-3.25.2/tests/test_filelock.py`) -> Impact: **22.8** | LOC: 9
- `_acquire` **(Many-Argument Workhorses)** (@ `filelock-3.25.2/src/filelock/_read_write.py`) -> Impact: **21.7** | LOC: 32
- `timeout_for_sqlite` **(Compute Cores)** (@ `filelock-3.25.2/src/filelock/_read_write.py`) -> Impact: **20.9** | LOC: 17
- `test_sticky_bit_fallback_handles_concurrent_unlink` **(Defensive Guards)** (@ `filelock-3.25.2/tests/test_filelock.py`) -> Impact: **18.5** | LOC: 23
- `test_write_non_starvation` **(Defensive Guards)** (@ `filelock-3.25.2/tests/test_read_write.py`) -> Impact: **18.3** | LOC: 54
  * *Intent:* """Test that write locks can eventually be acquired even with continuous read locks. Creates a chain of reader processes where the writer starts after...
- `_acquire` **(Defensive Guards)** (@ `filelock-3.25.2/src/filelock/_unix.py`) -> Impact: **18.0** | LOC: 48
- `acquire_lock` **(Many-Argument Workhorses)** (@ `filelock-3.25.2/tests/test_read_write.py`) -> Impact: **18.0** | LOC: 20

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `filelock-3.25.2/tests` | 13 | 2904.24 | 29.15% | 0.0% |
| `filelock-3.25.2/src/filelock` | 11 | 1332.92 | 46.79% | 0.93% |
| `filelock-3.25.2` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `filelock-3.25.2/src/filelock/_api.py` -> **10.2281%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `filelock-3.25.2/src/filelock/_read_write.py` -> **100.0%** Exposure
- `filelock-3.25.2/src/filelock/_soft.py` -> **100.0%** Exposure
- `filelock-3.25.2/src/filelock/_windows.py` -> **99.9999%** Exposure
- `filelock-3.25.2/src/filelock/__init__.py` -> **99.9998%** Exposure
- `filelock-3.25.2/src/filelock/version.py` -> **99.9997%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `filelock-3.25.2/tests/test_filelock.py` -> **56** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_read_write_unit.py` -> **46** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_async_read_write.py` -> **24** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_async_filelock.py` -> **17** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_read_write.py` -> **17** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `208` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `filelock-3.25.2/src/filelock/asyncio.py` (PYTHON) -> Cumulative Risk: **657.99**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.06)
- **Magnitude:** 232.1 | **LOC:** 377 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.748%), Safety Score (82.7846%)
- **Heaviest Functions:** `acquire` (Many-Argument Workhorses, Impact: 23.6), `__init__` (Many-Argument Workhorses, Impact: 13.8), `__call__` (Many-Argument Workhorses, Impact: 12.4)

### 2. `filelock-3.25.2/src/filelock/_unix.py` (PYTHON) -> Cumulative Risk: **615.27**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.50)
- **Magnitude:** 69.08 | **LOC:** 117 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Concurrency (91.7107%)
- **Heaviest Functions:** `_acquire` (Defensive Guards, Impact: 18.0), `_fallback_to_soft_lock` (Defensive Guards, Impact: 4.6), `_release` (Type Conversions, Impact: 1.8)

### 3. `filelock-3.25.2/src/filelock/_read_write.py` (PYTHON) -> Cumulative Risk: **579.15**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.05)
- **Magnitude:** 318.52 | **LOC:** 365 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9809%), Safety Score (95.5144%)
- **Heaviest Functions:** `_acquire` (Many-Argument Workhorses, Impact: 21.7), `timeout_for_sqlite` (Compute Cores, Impact: 20.9), `__call__` (Many-Argument Workhorses, Impact: 16.0)

### 4. `filelock-3.25.2/src/filelock/_api.py` (PYTHON) -> Cumulative Risk: **554.45**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.00)
- **Magnitude:** 312.3 | **LOC:** 579 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9951%), Safety Score (89.66%), Verification (80.0%)
- **Heaviest Functions:** `acquire` (Many-Argument Workhorses, Impact: 52.9), `__call__` (Many-Argument Workhorses, Impact: 36.4), `_check_give_up` (Many-Argument Workhorses, Impact: 16.8)

### 5. `filelock-3.25.2/src/filelock/_async_read_write.py` (PYTHON) -> Cumulative Risk: **539.57**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.45)
- **Magnitude:** 136.72 | **LOC:** 204 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8327%), Safety Score (67.1177%)
- **Heaviest Functions:** `read_lock` (Defensive Guards, Impact: 7.0), `write_lock` (Defensive Guards, Impact: 7.0), `_run` (Generic / Templated Code, Impact: 4.6)

### 6. `filelock-3.25.2/src/filelock/_soft.py` (PYTHON) -> Cumulative Risk: **523.21**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -1.06)
- **Magnitude:** 91.0 | **LOC:** 128 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (84.4224%)
- **Heaviest Functions:** `_acquire` (Defensive Guards, Impact: 12.5), `_is_process_alive` (Defensive Guards, Impact: 8.0), `_windows_unlink_with_retry` (Defensive Guards, Impact: 7.8)

### 7. `filelock-3.25.2/src/filelock/_windows.py` (PYTHON) -> Cumulative Risk: **469.95**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.21)
- **Magnitude:** 53.88 | **LOC:** 112 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (87.8897%), Documentation (80.0%)
- **Heaviest Functions:** `_acquire` (Defensive Guards, Impact: 9.9), `_is_reparse_point` (Compute Cores, Impact: 6.8), `_release` (Type Conversions, Impact: 1.8)

### 8. `filelock-3.25.2/tests/test_read_write_unit.py` (PYTHON) -> Cumulative Risk: **444.4**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.83)
- **Magnitude:** 463.26 | **LOC:** 575 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.534%), Stability (50.0%)
- **Heaviest Functions:** `test_double_check_wrong_mode_raises` (Many-Argument Workhorses, Impact: 15.9), `test_sequential_mode_switch` (Generic / Templated Code, Impact: 10.4), `test_operational_error_handling` (Generic / Templated Code, Impact: 8.0)

### 9. `filelock-3.25.2/tests/test_lock_expiry.py` (PYTHON) -> Cumulative Risk: **442.5**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +2.07)
- **Magnitude:** 113.08 | **LOC:** 145 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_lock_mtime_updated_on_acquire` (Generic / Templated Code, Impact: 3.8), `test_lifetime_singleton_mismatch` (Tests & Verification, Impact: 3.2), `test_expired_lock_race_rename_fails` (Tests & Verification, Impact: 2.2)

### 10. `filelock-3.25.2/tests/test_async_filelock.py` (PYTHON) -> Cumulative Risk: **440.16**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.40)
- **Magnitude:** 398.76 | **LOC:** 322 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_non_blocking` (Defensive Guards, Impact: 17.3), `test_simple` (Defensive Guards, Impact: 8.6), `test_acquire` (Defensive Guards, Impact: 8.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `filelock-3.25.2/tests/test_filelock.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 763.76 | **LOC:** 1148 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `open_permission_then_unlink` **(Compute Cores)** (Impact: 22.8)
  * `test_sticky_bit_fallback_handles_concurrent_unlink` **(Defensive Guards)** (Impact: 18.5)
  * `test_non_blocking` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* # raises Timeout error when the lock cannot be acquired lock_path = tmp_path / "a" lock_1, lock_2 = ...
  * `test_threaded_lock_different_lock_obj` **(Defensive Guards)** (Impact: 17.1)
  * `open_enoent_then_succeed` **(Compute Cores)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 422`, `args: 85`, `func_start: 82`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 160`, `dead_code: 10`, `unreferenced_by_name: 56`
* *Architecture:* `io: 63`, `api: 83`, `concurrency: 9`, `import: 20`
* *Defense:* `safety: 171`, `doc: 1`, `test: 172`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, concurrent.futures, contextlib, errno, filelock, inspect, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_async_read_write.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 602.38 | **LOC:** 271 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_clear_singleton_cache` **(Interface Declarations)** (Impact: 3.4)
  * `test_close` **(Defensive Guards)** (Impact: 3.2)
  * `test_upgrade_prohibited` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_downgrade_prohibited` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_close_on_unheld_lock` **(Generic / Templated Code)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 7 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 475
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 147`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 32`, `unreferenced_by_name: 24`
* *Architecture:* `io: 1`, `api: 24`, `concurrency: 90`, `import: 9`
* *Defense:* `safety: 57`, `test: 60`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, collections.abc, concurrent.futures, filelock, filelock._read_write, pathlib, pytest, sqlite3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_read_write_unit.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 463.26 | **LOC:** 575 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.4595%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_double_check_wrong_mode_raises` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `test_sequential_mode_switch` **(Generic / Templated Code)** (Impact: 10.4)
  * `test_operational_error_handling` **(Generic / Templated Code)** (Impact: 8.0)
  * `test_busy_timeout_recomputed_after_journal_mode` **(Generic / Templated Code)** (Impact: 6.5)
  * `test_reentrant_lock` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 39 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 178`, `args: 54`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 104`, `unreferenced_by_name: 46`
* *Architecture:* `io: 1`, `api: 53`, `concurrency: 13`, `import: 10`
* *Defense:* `safety: 70`, `test: 104`, `sync_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, collections.abc, filelock, filelock._read_write, pathlib, pytest, pytest_mock, sqlite3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_async_filelock.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 398.76 | **LOC:** 322 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_non_blocking` **(Defensive Guards)** (Impact: 17.3)
    * *Intent:* # raises Timeout error when the lock cannot be acquired lock_path = tmp_path / "a" lock_1, lock_2 = ...
  * `test_simple` **(Defensive Guards)** (Impact: 8.6)
  * `test_acquire` **(Defensive Guards)** (Impact: 8.6)
  * `test_attempting_to_release` **(Defensive Guards)** (Impact: 6.6)
  * `test_wait_message_logged` **(Generic / Templated Code)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 249
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 159`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 37`, `dead_code: 7`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 69`, `import: 5`
* *Defense:* `safety: 59`, `test: 68`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, filelock, logging, pathlib, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_read_write.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 318.52 | **LOC:** 365 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.6523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_acquire` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `timeout_for_sqlite` **(Compute Cores)** (Impact: 20.9)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `release` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* """ Release one level of the current lock. When the lock level reaches zero the underlying SQLite tr...
  * `_configure_and_begin` **(Many-Argument Workhorses)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 67`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 8`, `api: 11`, `concurrency: 8`, `import: 14`
* *Defense:* `safety: 7`, `doc: 9`, `sync_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 162.876
  * `Choke Point (Betweenness):` 0.016304 | `Ripple Effect (Closeness):` 0.352941
  * `Imports (Out-Degree: 2):` ._api, ._error, __future__, atexit, collections.abc, contextlib, logging, os...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_api.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 312.3 | **LOC:** 579 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3256%), Tech Debt (10.2281%)
**Top Internal Functions/Classes:**
  * `acquire` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `_check_give_up` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `release` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """ Release the file lock. The lock is only completely released when the lock counter reaches 0. The...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 99`, `args: 32`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 40`, `planned_debt: 1`
* *Architecture:* `io: 12`, `api: 27`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 1`, `doc: 30`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 147.679
  * `Choke Point (Betweenness):` 0.015399 | `Ripple Effect (Closeness):` 0.352941
  * `Imports (Out-Degree: 2):` ._error, ._read_write, __future__, abc, collections.abc, contextlib, dataclasses, inspect...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_read_write.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 260.6 | **LOC:** 562 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.517%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_non_starvation` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* """Test that write locks can eventually be acquired even with continuous read locks. Creates a chain...
  * `acquire_lock` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `chain_reader` **(Many-Argument Workhorses)** (Impact: 12.8)
  * `test_write_lock_excludes_read_locks` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* """Test that a write lock prevents other processes from acquiring read locks."""
  * `test_read_lock_excludes_write_locks` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* """Test that read locks prevent other processes from acquiring write locks."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 160`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 82`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 27`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 69`, `doc: 17`, `test: 39`, `sync_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, collections.abc, contextlib, filelock, filelock._read_write, multiprocessing, multiprocessing.sharedctypes, multiprocessing.synchronize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/asyncio.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 232.1 | **LOC:** 377 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acquire` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `_run_internal_method` **(Generic / Templated Code)** (Impact: 9.1)
  * `release` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """ Release the file lock. The lock is only completely released when the lock counter reaches 0. The...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 81`, `args: 16`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 20`
* *Architecture:* `io: 4`, `api: 18`, `concurrency: 27`, `import: 21`
* *Defense:* `safety: 1`, `doc: 19`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.532
  * `Choke Point (Betweenness):` 0.011775 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 5):` ._api, ._error, ._soft, ._unix, ._windows, __future__, asyncio, collections.abc...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_async_read_write.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 136.72 | **LOC:** 204 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `read_lock` **(Defensive Guards)** (Impact: 7.0)
    * *Intent:* """ Async context manager that acquires and releases a shared read lock. Falls back to instance defa...
  * `write_lock` **(Defensive Guards)** (Impact: 7.0)
    * *Intent:* """ Async context manager that acquires and releases an exclusive write lock. Falls back to instance...
  * `_run` **(Generic / Templated Code)** (Impact: 4.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
  * `acquire_read` **(Generic / Templated Code)** (Impact: 2.9)
    * *Intent:* """ Acquire a shared read lock. See :meth:`ReadWriteLock.acquire_read` for full semantics. :param ti...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 55`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 16`, `concurrency: 23`, `import: 10`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 2):` ._read_write, __future__, asyncio, collections.abc, concurrent, contextlib, functools, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_lock_expiry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 113.08 | **LOC:** 145 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lock_mtime_updated_on_acquire` **(Generic / Templated Code)** (Impact: 3.8)
  * `test_lifetime_singleton_mismatch` **(Tests & Verification)** (Impact: 3.2)
  * `test_expired_lock_race_rename_fails` **(Tests & Verification)** (Impact: 2.2)
  * `test_expired_lock_becomes_acquirable` **(Generic / Templated Code)** (Impact: 2.2)
  * `test_expired_lock_is_broken` **(Generic / Templated Code)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 57`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 13`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 12`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, filelock, os, pathlib, pytest, pytest_mock, time, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_soft.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 91.0 | **LOC:** 128 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_acquire` **(Defensive Guards)** (Impact: 12.5)
  * `_is_process_alive` **(Defensive Guards)** (Impact: 8.0)
  * `_windows_unlink_with_retry` **(Defensive Guards)** (Impact: 7.8)
  * `_try_break_stale_lock` **(Compute Cores)** (Impact: 6.4)
  * `_release` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 42`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 19`, `api: 4`, `import: 11`
* *Defense:* `safety: 7`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.523
  * `Choke Point (Betweenness):` 0.001812 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 2):` ._api, ._util, __future__, contextlib, ctypes, errno, os, pathlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_self_deadlock.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 83.02 | **LOC:** 140 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.219%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_symlink_same_canonical_path` **(Generic / Templated Code)** (Impact: 4.0)
  * `test_same_thread_different_instances_raises` **(Generic / Templated Code)** (Impact: 3.8)
  * `test_different_threads_no_false_positive` **(Defensive Guards)** (Impact: 2.8)
  * `test_force_release_cleans_registry` **(Generic / Templated Code)** (Impact: 2.3)
  * `test_cleanup_on_release` **(Generic / Templated Code)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 62`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 11`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 13`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, filelock, pathlib, pytest, sys, threading, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_default_mode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 76.08 | **LOC:** 140 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.5964%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_singleton_default_vs_explicit_mode_differ` **(Type Conversions)** (Impact: 3.1)
  * `test_default_mode_respects_umask` **(Defensive Guards)** (Impact: 2.5)
  * `test_default_mode_skips_fchmod` **(Defensive Guards)** (Impact: 2.2)
  * `test_explicit_mode_calls_fchmod` **(Defensive Guards)** (Impact: 2.2)
  * `test_explicit_mode_overrides_umask` **(Defensive Guards)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 56`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 14`
* *Architecture:* `io: 10`, `api: 14`, `import: 10`
* *Defense:* `safety: 20`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, filelock, filelock._api, os, pathlib, pytest, stat, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_unix.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 69.08 | **LOC:** 117 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.9743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_acquire` **(Defensive Guards)** (Impact: 18.0)
  * `_fallback_to_soft_lock` **(Defensive Guards)** (Impact: 4.6)
  * `_release` **(Type Conversions)** (Impact: 1.8)
  * `_acquire` **(Generic / Templated Code)** (Impact: 1.5)
  * `_release` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 38`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`
* *Architecture:* `io: 15`, `api: 3`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 9`, `doc: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.473
  * `Choke Point (Betweenness):` 0.001812 | `Ripple Effect (Closeness):` 0.09375
  * `Imports (Out-Degree: 4):` ._api, ._soft, ._util, .asyncio, __future__, contextlib, errno, fcntl...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_soft_stale.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 64.08 | **LOC:** 143 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.5327%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_stale_lock_rename_race` **(Tests & Verification)** (Impact: 2.3)
  * `test_stale_lock_broken_when_process_dead` **(Defensive Guards)** (Impact: 2.2)
  * `test_stale_lock_not_broken_when_eperm` **(Tests & Verification)** (Impact: 2.2)
  * `test_stale_lock_unexpected_kill_error_suppressed` **(Tests & Verification)** (Impact: 2.2)
  * `test_stale_detection_errors_suppressed` **(Tests & Verification)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 11`
* *Architecture:* `io: 18`, `api: 11`, `import: 11`
* *Defense:* `safety: 4`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, errno, filelock, os, pathlib, pytest, pytest_mock, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_windows.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 53.88 | **LOC:** 112 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.2305%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_acquire` **(Defensive Guards)** (Impact: 9.9)
  * `_is_reparse_point` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* """ Check if a path is a reparse point (symlink, junction, etc.) on Windows. :param path: Path to ch...
  * `_release` **(Type Conversions)** (Impact: 1.8)
  * `_acquire` **(Generic / Templated Code)** (Impact: 1.5)
  * `_release` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`
* *Architecture:* `io: 8`, `api: 3`, `import: 12`
* *Defense:* `safety: 4`, `doc: 3`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.473
  * `Choke Point (Betweenness):` 0.001812 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 2):` ._api, ._util, __future__, contextlib, ctypes, errno, msvcrt, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_unix_fallback.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 53.56 | **LOC:** 114 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_release_suppresses_eio_on_close` **(Generic / Templated Code)** (Impact: 4.2)
  * `test_fallback_emits_warning` **(Generic / Templated Code)** (Impact: 3.8)
  * `_close_eio` **(Generic / Templated Code)** (Impact: 3.0)
  * `test_fallback_subsequent_acquire_skips_flock` **(Generic / Templated Code)** (Impact: 2.3)
  * `test_fallback_release_unlinks_file` **(Defensive Guards)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 40`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 7`
* *Architecture:* `io: 7`, `api: 7`, `import: 11`
* *Defense:* `safety: 10`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, errno, filelock, os, pathlib, pytest, pytest_mock, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 47.24 | **LOC:** 83 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9328%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ._api, ._async_read_write, ._error, ._read_write, ._soft, ._unix, ._windows, .asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 19.2 | **LOC:** 54 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.408%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raise_on_not_writable_file` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* """ Raise an exception if attempting to open the file for writing would fail. This is done so files ...
  * `ensure_directory_exists` **(Generic / Templated Code)** (Impact: 1.8)
    * *Intent:* """ Ensure the directory containing the file exists (create it if necessary). :param filename: file....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 3`, `import: 6`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.15
  * `Imports (Out-Degree: 0):` __future__, errno, os, pathlib, stat, sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_error.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 17.36 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 1.9)
  * `lock_file` **(Generic / Templated Code)** (Impact: 1.6)
    * *Intent:* """:returns: The path of the file lock."""
  * `__reduce__` **(Generic / Templated Code)** (Impact: 1.5)
  * `__str__` **(Generic / Templated Code)** (Impact: 1.5)
  * `__repr__` **(Generic / Templated Code)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 160.459
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.320076
  * `Imports (Out-Degree: 0):` __future__, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_error.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14.08 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_timeout_pickle` **(Defensive Guards)** (Impact: 1.4)
  * `test_timeout_str` **(Tests & Verification)** (Impact: 1.1)
  * `test_timeout_repr` **(Tests & Verification)** (Impact: 1.1)
  * `test_timeout_lock_file` **(Tests & Verification)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 4`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 7`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, filelock, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.82 | **LOC:** 21 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.6396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pytest_sessionfinish` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, filelock._read_write, gc, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_virtualenv.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2.76 | **LOC:** 19 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_virtualenv` **(Generic / Templated Code)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 6`
* *Defense:* `safety: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, pathlib, pytest, sys, typing, virtualenv
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.186
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

- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 1.63** (Bridge: 0.0163 * Flux: 100.0%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 1.54** (Bridge: 0.0154 * Flux: 99.9951%)
- `filelock-3.25.2/src/filelock/asyncio.py` -> **Severity: 1.175** (Bridge: 0.0118 * Flux: 99.748%)
- `filelock-3.25.2/src/filelock/_soft.py` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 100.0%)
- `filelock-3.25.2/src/filelock/_unix.py` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 33.711** (Embedded: 0.3529 * Error Risk: 95.5144%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 31.645** (Embedded: 0.3529 * Error Risk: 89.66%)
- `filelock-3.25.2/src/filelock/_error.py` -> **Severity: 23.363** (Embedded: 0.3201 * Error Risk: 72.9934%)
- `filelock-3.25.2/src/filelock/_soft.py` -> **Severity: 11.256** (Embedded: 0.1333 * Error Risk: 84.4224%)
- `filelock-3.25.2/src/filelock/asyncio.py` -> **Severity: 10.348** (Embedded: 0.125 * Error Risk: 82.7846%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `filelock-3.25.2/src/filelock/_error.py` -> **Severity: 12836.72** (Blast Radius: 160.459 * Doc Risk: 80.0%)
- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 9307.207** (Blast Radius: 162.876 * Doc Risk: 57.1429%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 3627.203** (Blast Radius: 147.679 * Doc Risk: 24.5614%)
- `filelock-3.25.2/src/filelock/_soft.py` -> **Severity: 3452.3** (Blast Radius: 34.523 * Doc Risk: 100.0%)
- `filelock-3.25.2/src/filelock/_unix.py` -> **Severity: 2847.3** (Blast Radius: 28.473 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
