# ARCHITECTURAL_BRIEF: httpcore
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
| Total Artifacts | 61 |
| Analyzed Artifacts (Scanned) | 56 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 9280 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1526 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0024 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9828 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 53 | 9280 | 94.6% |
| MARKDOWN | 3 | 0 | 5.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 53 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 35.6 | 30.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.8 | 56.3 | 60.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 27.1 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 49.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.8 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 71.4 | 92.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 74 | 23 | 4 | `httpcore-1.0.9/tests/test_models.py` |
| cleanup | 37 | 15 | 3 | `httpcore-1.0.9/httpcore/_sync/http2.py` |
| guards | 1018 | 43 | 44 | `httpcore-1.0.9/httpcore/_async/http2.py` |
| danger | 293 | 33 | 15 | `httpcore-1.0.9/httpcore/_async/http2.py` |
| concurrency | 747 | 35 | 47 | `httpcore-1.0.9/tests/_async/test_connection_pool.py` |
| connectivity | 614 | 49 | 23 | `httpcore-1.0.9/tests/_async/test_connection_pool.py` |
| io | 46 | 9 | 2 | `httpcore-1.0.9/httpcore/_backends/sync.py` |
| crypto | 29 | 23 | 2 | `httpcore-1.0.9/httpcore/_async/connection.py` |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `httpcore-1.0.9/httpcore/_backends/base.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 23 | 12 | 2 | `httpcore-1.0.9/httpcore/_trace.py` |
| tests | 321 | 17 | 26 | `httpcore-1.0.9/tests/_async/test_connection_pool.py` |
| docs | 182 | 32 | 10 | `httpcore-1.0.9/tests/_async/test_connection_pool.py` |
| debt | 76 | 12 | 6 | `httpcore-1.0.9/httpcore/_async/http_proxy.py` |
| mutation | 3415 | 49 | 153 | `httpcore-1.0.9/httpcore/_async/http_proxy.py` |
| dead_code | 172 | 18 | 13 | `httpcore-1.0.9/tests/_async/test_connection_pool.py` |
| credential | 0 | 0 | 0 | - |
| threat | 8 | 6 | 1 | `httpcore-1.0.9/httpcore/_models.py` |
| ml_ai | 2 | 1 | 0 | `httpcore-1.0.9/tests/benchmark/client.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.7879**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `httpcore-1.0.9/httpcore/_backends/sync.py` (Hits: 23)
- `httpcore-1.0.9/httpcore/_backends/trio.py` (Hits: 7)
- `httpcore-1.0.9/tests/benchmark/client.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.py** (`httpcore-1.0.9/httpcore/_backends/base.py`) — 17 inbound connections
2. **_exceptions.py** (`httpcore-1.0.9/httpcore/_exceptions.py`) — 17 inbound connections
3. **_models.py** (`httpcore-1.0.9/httpcore/_models.py`) — 17 inbound connections
4. **_synchronization.py** (`httpcore-1.0.9/httpcore/_synchronization.py`) — 13 inbound connections
5. **_trace.py** (`httpcore-1.0.9/httpcore/_trace.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **http2.py** (`httpcore-1.0.9/httpcore/_async/http2.py`) — 17 outbound dependencies
2. **http2.py** (`httpcore-1.0.9/httpcore/_sync/http2.py`) — 17 outbound dependencies
3. **connection.py** (`httpcore-1.0.9/httpcore/_async/connection.py`) — 16 outbound dependencies
4. **http_proxy.py** (`httpcore-1.0.9/httpcore/_async/http_proxy.py`) — 16 outbound dependencies
5. **connection.py** (`httpcore-1.0.9/httpcore/_sync/connection.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> Impact: **30.1** | LOC: 79
- `__init__` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> Impact: **30.1** | LOC: 79
- `_assign_requests_to_connections` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> Impact: **29.0** | LOC: 70
  * *Intent:* """ Manage the state of the connection pool, assigning incoming requests to connections as available. Called whenever a new request is added or remove...
- `_assign_requests_to_connections` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> Impact: **29.0** | LOC: 70
  * *Intent:* """ Manage the state of the connection pool, assigning incoming requests to connections as available. Called whenever a new request is added or remove...
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/socks_proxy.py`) -> Impact: **28.4** | LOC: 84
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/socks_proxy.py`) -> Impact: **28.4** | LOC: 84
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/http_proxy.py`) -> Impact: **26.5** | LOC: 79
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/http_proxy.py`) -> Impact: **26.5** | LOC: 79
- `_receive_events` (@ `httpcore-1.0.9/httpcore/_async/http2.py`) -> Impact: **26.4** | LOC: 47
- `_receive_events` (@ `httpcore-1.0.9/httpcore/_sync/http2.py`) -> Impact: **26.4** | LOC: 47

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `httpcore-1.0.9/httpcore/_async` | 8 | 2348.88 | 66.34% | 12.5% |
| `httpcore-1.0.9/tests/_async` | 8 | 1817.92 | 23.46% | 0.0% |
| `httpcore-1.0.9/httpcore/_sync` | 8 | 1609.88 | 50.08% | 12.5% |
| `httpcore-1.0.9/httpcore` | 8 | 1102.34 | 32.42% | 12.49% |
| `httpcore-1.0.9/tests/_sync` | 8 | 696.36 | 3.73% | 0.0% |
| `httpcore-1.0.9/httpcore/_backends` | 6 | 539.7 | 50.97% | 31.23% |
| `httpcore-1.0.9/tests` | 5 | 363.72 | 18.01% | 0.0% |
| `httpcore-1.0.9/tests/benchmark` | 2 | 281.98 | 40.21% | 0.0% |
| `httpcore-1.0.9` | 3 | 12.78 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` -> **99.9995%** Exposure
- `httpcore-1.0.9/httpcore/_sync/http_proxy.py` -> **99.9995%** Exposure
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **99.9591%** Exposure
- `httpcore-1.0.9/httpcore/_backends/base.py` -> **98.8593%** Exposure
- `httpcore-1.0.9/httpcore/_backends/sync.py` -> **88.5488%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `httpcore-1.0.9/httpcore/_async/connection_pool.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http11.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_sync/connection.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_sync/connection_pool.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_sync/http11.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `httpcore-1.0.9/tests/_async/test_connection_pool.py` -> **18** Orphaned Functions | **6** Duplicates
- `httpcore-1.0.9/tests/_sync/test_connection_pool.py` -> **18** Orphaned Functions | **6** Duplicates
- `httpcore-1.0.9/tests/_async/test_connection.py` -> **13** Orphaned Functions | **6** Duplicates
- `httpcore-1.0.9/tests/test_models.py` -> **17** Orphaned Functions | **2** Duplicates
- `httpcore-1.0.9/tests/_sync/test_connection.py` -> **12** Orphaned Functions | **6** Duplicates

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
- **Unknown Dependencies:** `221` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `httpcore-1.0.9/httpcore/_async/http_proxy.py` (PYTHON) -> Cumulative Risk: **841.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 283.24 | **LOC:** 368 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%), Concurrency (99.9994%)
- **Heaviest Functions:** `handle_async_request` (Impact: 26.5), `__init__` (Impact: 24.9), `merge_headers` (Impact: 14.7)

### 2. `httpcore-1.0.9/httpcore/_synchronization.py` (PYTHON) -> Cumulative Risk: **818.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 444.88 | **LOC:** 319 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9591%)
- **Heaviest Functions:** `wait` (Impact: 11.1), `current_async_library` (Impact: 8.2), `__aexit__` (Impact: 7.2)

### 3. `httpcore-1.0.9/httpcore/_trace.py` (PYTHON) -> Cumulative Risk: **797.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 192.2 | **LOC:** 108 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `trace` (Impact: 18.9), `atrace` (Impact: 18.9), `__init__` (Impact: 13.1)

### 4. `httpcore-1.0.9/httpcore/_async/http11.py` (PYTHON) -> Cumulative Risk: **756.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 427.02 | **LOC:** 380 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 15.7), `_receive_event` (Impact: 11.8), `_receive_response_headers` (Impact: 9.9)

### 5. `httpcore-1.0.9/httpcore/_backends/trio.py` (PYTHON) -> Cumulative Risk: **755.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 149.68 | **LOC:** 160 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9963%), State Flux (99.9804%)
- **Heaviest Functions:** `get_extra_info` (Impact: 14.8), `connect_tcp` (Impact: 14.5), `connect_unix_socket` (Impact: 12.2)

### 6. `httpcore-1.0.9/httpcore/_async/connection.py` (PYTHON) -> Cumulative Risk: **743.48**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 257.38 | **LOC:** 223 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (94.1773%)
- **Heaviest Functions:** `_connect` (Impact: 22.1), `handle_async_request` (Impact: 15.6), `__init__` (Impact: 11.8)

### 7. `httpcore-1.0.9/httpcore/_async/socks_proxy.py` (PYTHON) -> Cumulative Risk: **734.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 307.6 | **LOC:** 342 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `handle_async_request` (Impact: 28.4), `_init_socks5_connection` (Impact: 18.7), `__init__` (Impact: 13.6)

### 8. `httpcore-1.0.9/httpcore/_sync/http_proxy.py` (PYTHON) -> Cumulative Risk: **728.31**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 232.24 | **LOC:** 368 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%), State Flux (99.9993%)
- **Heaviest Functions:** `handle_request` (Impact: 26.5), `__init__` (Impact: 24.9), `merge_headers` (Impact: 14.7)

### 9. `httpcore-1.0.9/httpcore/_async/connection_pool.py` (PYTHON) -> Cumulative Risk: **715.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 345.48 | **LOC:** 421 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (94.3552%)
- **Heaviest Functions:** `__init__` (Impact: 30.1), `_assign_requests_to_connections` (Impact: 29.0), `handle_async_request` (Impact: 13.9)

### 10. `httpcore-1.0.9/httpcore/_async/http2.py` (PYTHON) -> Cumulative Risk: **701.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 637.02 | **LOC:** 593 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Safety Score (89.8721%)
- **Heaviest Functions:** `_receive_events` (Impact: 26.4), `handle_async_request` (Impact: 19.0), `_receive_response` (Impact: 13.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `httpcore-1.0.9/tests/_async/test_connection_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 661.6 | **LOC:** 833 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3382%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_connection_pool_with_keepalive` (Impact: 11.6)
    * *Intent:* """ By default HTTP/1.1 requests should be returned to the connection pool. """
  * `test_connection_pool_concurrency_same_domain_keepalive` (Impact: 6.3)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
  * `test_connection_pool_concurrency` (Impact: 6.1)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
  * `test_connection_pool_with_http2` (Impact: 6.0)
    * *Intent:* """ Test a connection pool with HTTP/2 requests. """
  * `test_connection_pool_concurrency_same_domain_closing` (Impact: 6.0)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 64 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 408
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 205`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 59`, `duplicate_logic: 6`, `unreferenced_by_name: 18`
* *Architecture:* `api: 27`, `concurrency: 88`, `import: 7`
* *Defense:* `safety: 64`, `doc: 17`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hpack, httpcore, hyperframe.frame, logging, pytest, trio, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/http2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 637.02 | **LOC:** 593 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_receive_events` (Impact: 26.4)
  * `handle_async_request` (Impact: 19.0)
  * `_receive_response` (Impact: 13.1)
    * *Intent:* # Receiving the response...
  * `_response_closed` (Impact: 12.8)
  * `_send_request_headers` (Impact: 11.5)
    * *Intent:* # Sending the request... """ Send the request headers to a given stream ID. """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 259
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 138`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 85`
* *Architecture:* `api: 17`, `concurrency: 69`, `import: 17`
* *Defense:* `safety: 20`, `doc: 10`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._backends.base, .._exceptions, .._models, .._synchronization, .._trace, .interfaces, __future__, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_synchronization.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 444.88 | **LOC:** 319 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.798%), Tech Debt (99.9591%)
**Top Internal Functions/Classes:**
  * `wait` (Impact: 11.1)
  * `current_async_library` (Impact: 8.2)
    * *Intent:* # Determine if we're running under trio or asyncio. # See https://sniffio.readthedocs.io/en/latest/ ...
  * `__aexit__` (Impact: 7.2)
  * `__exit__` (Impact: 7.2)
  * `__aenter__` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 169
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 78`, `args: 32`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `duplicate_logic: 8`
* *Architecture:* `api: 24`, `concurrency: 34`, `import: 7`
* *Defense:* `safety: 5`, `doc: 8`, `sync_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.138
  * `Choke Point (Betweenness):` 0.010382 | `Ripple Effect (Closeness):` 0.227273
  * `Imports (Out-Degree: 3):` ._exceptions, __future__, anyio, sniffio, threading, trio, types
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/httpcore/_async/http11.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 427.02 | **LOC:** 380 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 15.7)
  * `_receive_event` (Impact: 11.8)
  * `_receive_response_headers` (Impact: 9.9)
    * *Intent:* # Receiving the response...
  * `_response_closed` (Impact: 7.7)
  * `_receive_response_body` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 167
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 113`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`
* *Architecture:* `api: 22`, `concurrency: 47`, `import: 14`
* *Defense:* `safety: 10`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._backends.base, .._exceptions, .._models, .._synchronization, .._trace, .interfaces, __future__, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 390.42 | **LOC:** 517 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `include_request_headers` (Impact: 23.4)
  * `__init__` (Impact: 20.1)
  * `enforce_headers` (Impact: 13.6)
  * `__init__` (Impact: 12.6)
  * `iter_stream` (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 74`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 52`
* *Architecture:* `api: 23`, `concurrency: 15`, `import: 5`
* *Defense:* `safety: 24`, `doc: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 84.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.309091
  * `Imports (Out-Degree: 0):` __future__, base64, ssl, typing, urllib.parse
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/httpcore/_sync/http2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 380.02 | **LOC:** 593 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1681%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_receive_events` (Impact: 26.4)
  * `handle_request` (Impact: 19.0)
  * `_receive_response` (Impact: 13.1)
    * *Intent:* # Receiving the response...
  * `_response_closed` (Impact: 12.8)
  * `_send_request_headers` (Impact: 11.5)
    * *Intent:* # Sending the request... """ Send the request headers to a given stream ID. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 104`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 85`
* *Architecture:* `api: 17`, `import: 17`
* *Defense:* `safety: 20`, `doc: 10`, `sync_locks: 9`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._backends.base, .._exceptions, .._models, .._synchronization, .._trace, .interfaces, __future__, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/connection_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 345.48 | **LOC:** 421 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 30.1)
  * `_assign_requests_to_connections` (Impact: 29.0)
    * *Intent:* """ Manage the state of the connection pool, assigning incoming requests to connections as available...
  * `handle_async_request` (Impact: 13.9)
    * *Intent:* """ Send an HTTP request, and return an HTTP response. This is the core implementation that is calle...
  * `create_connection` (Impact: 9.5)
  * `__repr__` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 70
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 85`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 65`
* *Architecture:* `io: 2`, `api: 16`, `concurrency: 20`, `import: 15`
* *Defense:* `safety: 8`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._backends.auto, .._backends.base, .._exceptions, .._models, .._synchronization, .connection, .http_proxy, .interfaces...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/socks_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 307.6 | **LOC:** 342 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.0816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 28.4)
  * `_init_socks5_connection` (Impact: 18.7)
  * `__init__` (Impact: 13.6)
  * `__init__` (Impact: 10.7)
  * `is_available` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 81`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 49`
* *Architecture:* `api: 12`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._backends.auto, .._backends.base, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .connection_pool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_async/test_connection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 305.58 | **LOC:** 382 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `connect_tcp` (Impact: 6.1)
  * `start_tls` (Impact: 5.1)
  * `test_write_error_with_response_sent` (Impact: 4.6)
    * *Intent:* """ If a server half-closes the connection while the client is sending the request, it may still sen...
  * `write` (Impact: 4.3)
  * `write` (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 167
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 112`, `args: 23`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `duplicate_logic: 6`, `unreferenced_by_name: 13`
* *Architecture:* `api: 24`, `concurrency: 47`, `import: 6`
* *Defense:* `safety: 22`, `doc: 4`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hpack, httpcore, hyperframe.frame, pytest, ssl, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/http_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 283.24 | **LOC:** 368 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.4908%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 26.5)
  * `__init__` (Impact: 24.9)
  * `merge_headers` (Impact: 14.7)
  * `__init__` (Impact: 5.0)
  * `create_connection` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 83`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 55`, `duplicate_logic: 16`
* *Architecture:* `api: 21`, `concurrency: 13`, `import: 16`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .._backends.base, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .connection, .connection_pool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_async/test_http11.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 277.76 | **LOC:** 381 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_http11_upgrade_with_trailing_data` (Impact: 3.4)
    * *Intent:* """ HTTP "101 Switching Protocols" indicates an upgraded connection. In `CONNECT` and `Upgrade:` req...
  * `test_http11_early_hints` (Impact: 2.7)
    * *Intent:* """ HTTP "103 Early Hints" is an interim response. We simply ignore it and return the final response...
  * `test_http11_upgrade_connection` (Impact: 2.6)
    * *Intent:* """ HTTP "101 Switching Protocols" indicates an upgraded connection. We should return the response, ...
  * `test_http11_connection_with_local_protocol_error` (Impact: 2.5)
    * *Intent:* """ If a local protocol error occurs, then no response will be returned, and the connection will not...
  * `test_http11_expect_continue` (Impact: 2.5)
    * *Intent:* """ HTTP "100 Continue" is an interim response. We simply ignore it and return the final response. h...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Concurrency (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 122`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 13`
* *Architecture:* `api: 13`, `concurrency: 47`, `import: 2`
* *Defense:* `safety: 44`, `doc: 12`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpcore, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/connection_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 275.48 | **LOC:** 421 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 30.1)
  * `_assign_requests_to_connections` (Impact: 29.0)
    * *Intent:* """ Manage the state of the connection pool, assigning incoming requests to connections as available...
  * `handle_request` (Impact: 13.9)
    * *Intent:* """ Send an HTTP request, and return an HTTP response. This is the core implementation that is calle...
  * `create_connection` (Impact: 9.5)
  * `__repr__` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 65`
* *Architecture:* `io: 2`, `api: 16`, `import: 15`
* *Defense:* `safety: 8`, `doc: 5`, `sync_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.228
  * `Choke Point (Betweenness):` 0.002694 | `Ripple Effect (Closeness):` 0.024242
  * `Imports (Out-Degree: 5):` .._backends.base, .._backends.sync, .._exceptions, .._models, .._synchronization, .connection, .http_proxy, .interfaces...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/tests/benchmark/client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 262.38 | **LOC:** 191 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_sync_requests` (Impact: 16.0)
  * `run_async_requests` (Impact: 14.4)
  * `main` (Impact: 5.8)
  * `run_in_executor` (Impact: 5.5)
  * `gather_limited_concurrency` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 137
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 69`, `args: 16`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 10`, `state_mutation: 31`
* *Architecture:* `io: 5`, `api: 12`, `concurrency: 32`, `import: 13`
* *Defense:* `safety: 9`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aiohttp, asyncio, concurrent.futures, contextlib, httpcore, matplotlib.axes, matplotlib.pyplot, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/http11.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 260.02 | **LOC:** 380 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.85%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 15.7)
  * `_receive_event` (Impact: 11.8)
  * `_receive_response_headers` (Impact: 9.9)
    * *Intent:* # Receiving the response...
  * `_response_closed` (Impact: 7.7)
  * `_receive_response_body` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 93`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`
* *Architecture:* `api: 22`, `import: 14`
* *Defense:* `safety: 10`, `sync_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._backends.base, .._exceptions, .._models, .._synchronization, .._trace, .interfaces, __future__, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/connection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 257.38 | **LOC:** 223 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.1773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_connect` (Impact: 22.1)
  * `handle_async_request` (Impact: 15.6)
  * `__init__` (Impact: 11.8)
  * `is_available` (Impact: 7.6)
  * `info` (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 77`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`
* *Architecture:* `api: 14`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._backends.auto, .._backends.base, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .http11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_sync/test_connection_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 252.94 | **LOC:** 833 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0532%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_connection_pool_with_keepalive` (Impact: 11.6)
    * *Intent:* """ By default HTTP/1.1 requests should be returned to the connection pool. """
  * `test_connection_pool_concurrency_same_domain_keepalive` (Impact: 6.3)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
  * `test_connection_pool_concurrency` (Impact: 6.1)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
  * `test_connection_pool_with_http2` (Impact: 6.0)
    * *Intent:* """ Test a connection pool with HTTP/2 requests. """
  * `test_connection_pool_concurrency_same_domain_closing` (Impact: 6.0)
    * *Intent:* """ HTTP/1.1 requests made in concurrency must not ever exceed the maximum number of allowable conne...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 178`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 59`, `duplicate_logic: 6`, `unreferenced_by_name: 18`
* *Architecture:* `api: 27`, `import: 7`
* *Defense:* `safety: 64`, `doc: 17`, `test: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hpack, httpcore, hyperframe.frame, logging, pytest, tests, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/http_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 232.24 | **LOC:** 368 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6151%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 26.5)
  * `__init__` (Impact: 24.9)
  * `merge_headers` (Impact: 14.7)
  * `__init__` (Impact: 5.0)
  * `create_connection` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 76`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 55`, `duplicate_logic: 16`
* *Architecture:* `api: 21`, `import: 16`
* *Defense:* `doc: 3`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .._backends.base, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .connection, .connection_pool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/socks_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 224.6 | **LOC:** 342 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.0828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 28.4)
  * `_init_socks5_connection` (Impact: 18.7)
  * `__init__` (Impact: 13.6)
  * `__init__` (Impact: 10.7)
  * `is_available` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 70`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 49`
* *Architecture:* `api: 12`, `import: 15`
* *Defense:* `safety: 8`, `doc: 2`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._backends.base, .._backends.sync, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .connection_pool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_async/test_http2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 220.92 | **LOC:** 383 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5535%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_http2_remote_max_streams_update` (Impact: 6.5)
    * *Intent:* """ If the remote server updates the maximum concurrent streams value, we should be adjusting how ma...
  * `test_http2_connection_with_flow_control` (Impact: 3.9)
  * `test_http2_connection_with_goaway` (Impact: 3.4)
    * *Intent:* """ If a GoAway frame occurs, then no response will be returned, and the connection will not be reus...
  * `test_http2_connection_with_rst_stream` (Impact: 3.1)
    * *Intent:* """ If a stream reset occurs, then no response will be returned, but the connection will remain reus...
  * `test_http2_connection` (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 91`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 10`
* *Architecture:* `api: 10`, `concurrency: 37`, `import: 4`
* *Defense:* `safety: 22`, `doc: 6`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hpack, httpcore, hyperframe.frame, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/test_cancellations.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 195.14 | **LOC:** 246 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 6.3)
  * `read` (Impact: 4.3)
  * `connect_tcp` (Impact: 3.1)
  * `connect_tcp` (Impact: 3.1)
  * `test_h2_timeout_during_response` (Impact: 2.7)
    * *Intent:* """ An async timeout on an HTTP/2 during the response reading should leave the connection in a neatl...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 78`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`, `duplicate_logic: 4`, `unreferenced_by_name: 8`
* *Architecture:* `api: 21`, `concurrency: 36`, `import: 6`
* *Defense:* `safety: 9`, `doc: 10`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyio, hpack, httpcore, hyperframe, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_trace.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 192.2 | **LOC:** 108 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.8118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `trace` (Impact: 18.9)
  * `atrace` (Impact: 18.9)
  * `__init__` (Impact: 13.1)
  * `__exit__` (Impact: 9.6)
  * `__aexit__` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 24`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 23`
* *Architecture:* `api: 8`, `concurrency: 7`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 1):` ._models, __future__, inspect, logging, types, typing
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/httpcore/_sync/connection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 180.38 | **LOC:** 223 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.9337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_connect` (Impact: 22.1)
  * `handle_request` (Impact: 15.6)
  * `__init__` (Impact: 11.8)
  * `is_available` (Impact: 7.6)
  * `info` (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 69`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`
* *Architecture:* `api: 14`, `import: 16`
* *Defense:* `safety: 2`, `doc: 1`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._backends.base, .._backends.sync, .._exceptions, .._models, .._ssl, .._synchronization, .._trace, .http11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_backends/sync.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 165.36 | **LOC:** 242 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.6347%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `connect_tcp` (Impact: 14.7)
  * `get_extra_info` (Impact: 12.7)
  * `_perform_io` (Impact: 11.6)
  * `get_extra_info` (Impact: 11.0)
  * `connect_unix_socket` (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 60`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 22`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 23`, `api: 15`, `import: 9`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.738
  * `Choke Point (Betweenness):` 0.001515 | `Ripple Effect (Closeness):` 0.075758
  * `Imports (Out-Degree: 3):` .._exceptions, .._utils, .base, __future__, functools, socket, ssl, sys...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/tests/_async/test_http_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 153.96 | **LOC:** 279 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.2018%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_proxy_tunneling_http2` (Impact: 6.1)
    * *Intent:* """ Send an HTTP/2 request via a proxy. """
  * `test_proxy_tunneling` (Impact: 5.6)
    * *Intent:* """ Send an HTTPS request via a proxy. """
  * `test_proxy_forwarding` (Impact: 5.5)
    * *Intent:* """ Send an HTTP request via a proxy. """
  * `connect_tcp` (Impact: 3.1)
  * `start_tls` (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 85
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 81`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 8`
* *Architecture:* `api: 10`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 38`, `doc: 5`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hpack, httpcore, hyperframe.frame, pytest, ssl, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_backends/trio.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 149.68 | **LOC:** 160 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.155%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_extra_info` (Impact: 14.8)
  * `connect_tcp` (Impact: 14.5)
  * `connect_unix_socket` (Impact: 12.2)
  * `write` (Impact: 8.7)
  * `start_tls` (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 54`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`
* *Architecture:* `io: 7`, `api: 11`, `concurrency: 15`, `import: 6`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.964
  * `Choke Point (Betweenness):` 0.000954 | `Ripple Effect (Closeness):` 0.169501
  * `Imports (Out-Degree: 2):` .._exceptions, .base, __future__, ssl, trio, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `httpcore-1.0.9/httpcore/_synchronization.py` -> **Severity: 1.038** (Bridge: 0.0104 * Flux: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/anyio.py` -> **Severity: 0.51** (Bridge: 0.0052 * Flux: 98.7497%)
- `httpcore-1.0.9/httpcore/_sync/connection_pool.py` -> **Severity: 0.269** (Bridge: 0.0027 * Flux: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/sync.py` -> **Severity: 0.151** (Bridge: 0.0015 * Flux: 99.9698%)
- `httpcore-1.0.9/httpcore/_backends/auto.py` -> **Severity: 0.139** (Bridge: 0.0015 * Flux: 91.6827%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `httpcore-1.0.9/httpcore/_exceptions.py` -> **Severity: 31.599** (Embedded: 0.3207 * Error Risk: 98.5226%)
- `httpcore-1.0.9/httpcore/_models.py` -> **Severity: 25.918** (Embedded: 0.3091 * Error Risk: 83.8539%)
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **Severity: 22.123** (Embedded: 0.2273 * Error Risk: 97.3403%)
- `httpcore-1.0.9/httpcore/_backends/base.py` -> **Severity: 21.192** (Embedded: 0.3207 * Error Risk: 66.0756%)
- `httpcore-1.0.9/httpcore/_trace.py` -> **Severity: 17.969** (Embedded: 0.1818 * Error Risk: 98.8281%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `httpcore-1.0.9/httpcore/_models.py` -> **Severity: 7732.379** (Blast Radius: 84.688 * Doc Risk: 91.3043%)
- `httpcore-1.0.9/httpcore/_exceptions.py` -> **Severity: 7687.6** (Blast Radius: 76.876 * Doc Risk: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/base.py` -> **Severity: 6987.2** (Blast Radius: 69.872 * Doc Risk: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/anyio.py` -> **Severity: 3696.4** (Blast Radius: 36.964 * Doc Risk: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/trio.py` -> **Severity: 3696.4** (Blast Radius: 36.964 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
