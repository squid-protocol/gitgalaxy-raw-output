# ARCHITECTURAL_BRIEF: aiohappyeyeballs
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
| Total Artifacts | 19 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 2626 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.42 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5309 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 14 | 2626 | 93.3% |
| MARKDOWN | 1 | 0 | 6.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14 | 93.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 6.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 42 exceeds 500 chars)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 72.7 | 24.9 | 25.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 51.3 | 53.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 25.8 | 8.5 | 6.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 50.0 | 50.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 78.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 54.3 | 67.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6 | 2 | 1 | `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` |
| cleanup | 6 | 4 | 1 | `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` |
| guards | 178 | 10 | 19 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| danger | 87 | 8 | 18 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| concurrency | 290 | 7 | 34 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| connectivity | 89 | 12 | 16 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| io | 562 | 7 | 46 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 295 | 8 | 10 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| docs | 39 | 11 | 5 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| debt | 35 | 2 | 2 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| mutation | 873 | 11 | 58 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| dead_code | 55 | 8 | 8 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| credential | 0 | 0 | 0 | - |
| threat | 21 | 1 | 0 | `aiohappyeyeballs-2.6.1/tests/test_impl.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` (Hits: 490)
- `aiohappyeyeballs-2.6.1/tests/test_utils.py` (Hits: 46)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py`) — 5 inbound connections
2. **_staggered.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py`) — 3 inbound connections
3. **impl.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) — 1 inbound connections
4. **utils.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) — 1 inbound connections
5. **README.md** (`aiohappyeyeballs-2.6.1/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **impl.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) — 9 outbound dependencies
2. **conftest.py** (`aiohappyeyeballs-2.6.1/tests/conftest.py`) — 7 outbound dependencies
3. **test_impl.py** (`aiohappyeyeballs-2.6.1/tests/test_impl.py`) — 7 outbound dependencies
4. **test_staggered.py** (`aiohappyeyeballs-2.6.1/tests/test_staggered.py`) — 7 outbound dependencies
5. **utils.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `start_connection` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) -> Impact: **81.1** | LOC: 140
- `_connect_sock` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) -> Impact: **46.1** | LOC: 76
- `staggered_race` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py`) -> Impact: **41.8** | LOC: 156
- `remove_addr_infos` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) -> Impact: **17.0** | LOC: 28
- `_interleave_addrinfos` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) -> Impact: **11.6** | LOC: 25
- `pop_addr_infos_interleave` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) -> Impact: **11.5** | LOC: 22
- `test_ipv64_laddr_bind_fails_eyeballs_first_ipv6_fails` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **11.2** | LOC: 83
- `test_uvloop_mixing_os_and_runtime_error` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **10.1** | LOC: 88
- `test_ipv64_laddr_bind_fails_eyeballs_interleave_first__ipv6_fails` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **9.8** | LOC: 83
- `addr_to_addr_infos` (@ `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) -> Impact: **9.7** | LOC: 25

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `aiohappyeyeballs-2.6.1/tests` | 9 | 2149.66 | 19.86% | 0.0% |
| `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs` | 5 | 612.08 | 33.87% | 0.0% |
| `aiohappyeyeballs-2.6.1` | 1 | 1.94 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **100.0%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **100.0%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **100.0%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` -> **31.0026%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` -> **30** Orphaned Functions | **33** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` -> **8** Orphaned Functions | **0** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered.py` -> **4** Orphaned Functions | **2** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` -> **5** Orphaned Functions | **0** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_utils.py` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (PYTHON) -> Cumulative Risk: **699.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 261.42 | **LOC:** 260 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9339%)
- **Heaviest Functions:** `start_connection` (Impact: 81.1), `_connect_sock` (Impact: 46.1), `_interleave_addrinfos` (Impact: 11.6)

### 2. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` (PYTHON) -> Cumulative Risk: **596.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 205.0 | **LOC:** 208 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (92.484%)
- **Heaviest Functions:** `staggered_race` (Impact: 41.8), `_wait_one` (Impact: 7.9), `run_one_coro` (Impact: 3.3)

### 3. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` (PYTHON) -> Cumulative Risk: **514.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 110.22 | **LOC:** 98 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4193%)
- **Heaviest Functions:** `remove_addr_infos` (Impact: 17.0), `pop_addr_infos_interleave` (Impact: 11.5), `addr_to_addr_infos` (Impact: 9.7)

### 4. `aiohappyeyeballs-2.6.1/tests/test_impl.py` (PYTHON) -> Cumulative Risk: **472.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1672.18 | **LOC:** 2017 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (71.6639%)
- **Heaviest Functions:** `test_ipv64_laddr_bind_fails_eyeballs_first_ipv6_fails` (Impact: 11.2), `test_uvloop_mixing_os_and_runtime_error` (Impact: 10.1), `test_ipv64_laddr_bind_fails_eyeballs_interleave_first__ipv6_fails` (Impact: 9.8)

### 5. `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` (PYTHON) -> Cumulative Risk: **450.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 77.36 | **LOC:** 97 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Stability (50.0%)
- **Heaviest Functions:** `set_event_loop` (Impact: 6.3), `setUp` (Impact: 3.3), `test_staggered_race_with_eager_tasks` (Impact: 2.6)

### 6. `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` (PYTHON) -> Cumulative Risk: **440.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 92.4 | **LOC:** 147 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_long_delay_early_failure` (Impact: 3.9), `test_first_error_second_successful` (Impact: 3.8), `test_first_timeout_second_successful` (Impact: 3.8)

### 7. `aiohappyeyeballs-2.6.1/tests/test_staggered.py` (PYTHON) -> Cumulative Risk: **381.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 191.3 | **LOC:** 102 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Documentation (50.0%)
- **Heaviest Functions:** `test_multiple_winners_eager_task_factory` (Impact: 3.5), `test_multiple_winners` (Impact: 3.1), `test_one_winners` (Impact: 3.0)

### 8. `aiohappyeyeballs-2.6.1/tests/conftest.py` (PYTHON) -> Cumulative Risk: **368.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 66.4 | **LOC:** 63 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Safety Score (60.5532%), Stability (50.0%)
- **Heaviest Functions:** `verify_no_lingering_tasks` (Impact: 8.0), `get_scheduled_timer_handles` (Impact: 1.6), `long_repr_strings` (Impact: 1.6)

### 9. `aiohappyeyeballs-2.6.1/tests/test_init.py` (PYTHON) -> Cumulative Risk: **253.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2.16 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Api Exposure (3.5258%)
- **Heaviest Functions:** `test_init` (Impact: 1.1)

### 10. `aiohappyeyeballs-2.6.1/tests/test_utils.py` (PYTHON) -> Cumulative Risk: **199.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 34.82 | **LOC:** 186 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (39.3289%), Api Exposure (6.1533%)
- **Heaviest Functions:** `test_addr_to_addr_infos` (Impact: 4.0), `test_remove_addr_infos_slow_path` (Impact: 3.9), `test_pop_addr_infos_interleave` (Impact: 2.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `aiohappyeyeballs-2.6.1/tests/test_impl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1672.18 | **LOC:** 2017 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0104%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ipv64_laddr_bind_fails_eyeballs_first_ipv6_fails` (Impact: 11.2)
  * `test_uvloop_mixing_os_and_runtime_error` (Impact: 10.1)
  * `test_ipv64_laddr_bind_fails_eyeballs_interleave_first__ipv6_fails` (Impact: 9.8)
  * `test_ipv64_laddr_bind_fails_all_eyeballs_interleave_first__ipv6_fails` (Impact: 9.7)
  * `test_ipv64_laddr_socket_blocking_fails` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 128 instances
* *Amplified Cascading Flux:* 88 instances
* *Concurrency (weighted view):* 792
* *State Mutation (weighted view):* 429
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 295`, `args: 82`, `func_start: 82`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 253`, `duplicate_logic: 33`, `unreferenced_by_name: 30`
* *Architecture:* `io: 490`, `api: 36`, `concurrency: 152`, `import: 7`
* *Defense:* `safety: 55`, `doc: 9`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` aiohappyeyeballs, asyncio, pytest, socket, types, typing, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 261.42 | **LOC:** 260 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start_connection` (Impact: 81.1)
  * `_connect_sock` (Impact: 46.1)
  * `_interleave_addrinfos` (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 33`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 34`
* *Architecture:* `io: 13`, `api: 1`, `concurrency: 9`, `import: 9`
* *Defense:* `safety: 17`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071429
  * `Imports (Out-Degree: 1):` , .types, asyncio, collections, contextlib, functools, itertools, socket...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 205.0 | **LOC:** 208 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.9997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `staggered_race` (Impact: 41.8)
  * `_wait_one` (Impact: 7.9)
  * `run_one_coro` (Impact: 3.3)
  * `_set_result` (Impact: 3.0)
    * *Intent:* """Set the result of a future if it is not already done."""
  * `_on_completion` (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`
* *Architecture:* `api: 2`, `concurrency: 24`, `import: 3`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 159.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 0):` asyncio, contextlib, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/tests/test_staggered.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 191.3 | **LOC:** 102 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_winners_eager_task_factory` (Impact: 3.5)
    * *Intent:* """Test multiple winners are handled correctly."""
  * `test_multiple_winners` (Impact: 3.1)
    * *Intent:* """Test multiple winners are handled correctly."""
  * `test_one_winners` (Impact: 3.0)
    * *Intent:* """Test that there is only one winner when there is no await in the coro."""
  * `run` (Impact: 3.0)
  * `coro` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 135
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 48`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `duplicate_logic: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 25`, `import: 7`
* *Defense:* `safety: 17`, `doc: 4`, `test: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` aiohappyeyeballs._staggered, asyncio, collections.abc, functools, pytest, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 110.22 | **LOC:** 98 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.6909%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove_addr_infos` (Impact: 17.0)
  * `pop_addr_infos_interleave` (Impact: 11.5)
  * `addr_to_addr_infos` (Impact: 9.7)
  * `_addr_tuple_to_ip_address` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`
* *Architecture:* `io: 5`, `api: 3`, `import: 4`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071429
  * `Imports (Out-Degree: 1):` .types, ipaddress, socket, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 92.4 | **LOC:** 147 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.7852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_long_delay_early_failure` (Impact: 3.9)
  * `test_first_error_second_successful` (Impact: 3.8)
  * `test_first_timeout_second_successful` (Impact: 3.8)
  * `test_none_successful` (Impact: 3.8)
  * `coro` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 36`, `args: 25`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 16`, `concurrency: 31`, `import: 3`
* *Defense:* `doc: 1`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` aiohappyeyeballs._staggered, asyncio, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 77.36 | **LOC:** 97 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.6035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set_event_loop` (Impact: 6.3)
  * `setUp` (Impact: 3.3)
  * `test_staggered_race_with_eager_tasks` (Impact: 2.6)
    * *Intent:* # See https://github.com/python/cpython/issues/124309 async def fail(): await asyncio.sleep(0) raise...
  * `test_staggered_race_with_eager_tasks_no_delay` (Impact: 2.5)
    * *Intent:* # See https://github.com/python/cpython/issues/124309 async def fail(): raise ValueError("no good") ...
  * `close_loop` (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 22`, `args: 17`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 12`, `concurrency: 20`, `import: 4`
* *Defense:* `safety: 2`, `doc: 1`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` aiohappyeyeballs._staggered, asyncio, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 66.4 | **LOC:** 63 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `verify_no_lingering_tasks` (Impact: 8.0)
  * `get_scheduled_timer_handles` (Impact: 1.6)
    * *Intent:* """Return a list of scheduled TimerHandles."""
  * `long_repr_strings` (Impact: 1.6)
    * *Intent:* """Increase reprlib maxstring and maxother to 300."""
  * `verify_threads_ended` (Impact: 1.3)
    * *Intent:* """Verify that the threads are not running after the test."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 9`, `import: 7`
* *Defense:* `safety: 3`, `doc: 5`, `test: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncio, asyncio.events, contextlib, pytest, reprlib, threading, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.82 | **LOC:** 186 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3023%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_addr_to_addr_infos` (Impact: 4.0)
    * *Intent:* """Test addr_to_addr_infos."""
  * `test_remove_addr_infos_slow_path` (Impact: 3.9)
    * *Intent:* """Test remove_addr_infos with mis-matched formatting."""
  * `test_pop_addr_infos_interleave` (Impact: 2.8)
    * *Intent:* """Test pop_addr_infos_interleave."""
  * `test_remove_addr_infos` (Impact: 2.7)
    * *Intent:* """Test remove_addr_infos."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `unreferenced_by_name: 4`
* *Architecture:* `io: 46`, `api: 4`, `import: 4`
* *Defense:* `safety: 17`, `doc: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aiohappyeyeballs, pytest, socket, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.24 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .impl, .types, .utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.2 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 5`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 231.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.357143
  * `Imports (Out-Degree: 0):` socket, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2.52 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_callable_import_from_typing` (Impact: 1.4)
    * *Intent:* """ Test that Callable is imported from typing. PY3.9: https://github.com/python/cpython/issues/8713...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` aiohappyeyeballs.types, collections.abc, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_init.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2.16 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_init` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aiohappyeyeballs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.94 | **LOC:** 97 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.88
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

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` -> **Severity: 22.207** (Embedded: 0.3571 * Error Risk: 62.1788%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **Severity: 19.818** (Embedded: 0.2143 * Error Risk: 92.484%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **Severity: 7.101** (Embedded: 0.0714 * Error Risk: 99.4193%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **Severity: 6.608** (Embedded: 0.0714 * Error Risk: 92.5078%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **Severity: 13656.259** (Blast Radius: 159.323 * Doc Risk: 85.7143%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **Severity: 5759.6** (Blast Radius: 57.596 * Doc Risk: 100.0%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **Severity: 5759.6** (Blast Radius: 57.596 * Doc Risk: 100.0%)
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` -> **Severity: 4488.0** (Blast Radius: 44.88 * Doc Risk: 100.0%)
- `aiohappyeyeballs-2.6.1/tests/test_init.py` -> **Severity: 4488.0** (Blast Radius: 44.88 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
