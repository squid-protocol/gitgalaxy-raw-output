# ARCHITECTURAL_BRIEF: docker-py
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/docker/docker-py.git` |
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
| Total Artifacts | 193 |
| Analyzed Artifacts (Scanned) | 154 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 39 |
| Total LOC | 21301 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 79.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6346 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.43 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7233 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 135 | 21039 | 87.7% |
| PLAINTEXT | 11 | 7 | 7.1% |
| MARKDOWN | 2 | 0 | 1.3% |
| DOCKERFILE | 2 | 36 | 1.3% |
| SHELL | 2 | 43 | 1.3% |
| MAKEFILE | 1 | 157 | 0.6% |
| JSON | 1 | 19 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.291`
> **Composition Archetype:** `Hub-Coupled App` (z +0.78; from the repo's file-archetype mix)
> **File Composition:** Defensive Guards Files 31%, Data / Markup / Trivial 18%, Large Core Modules 17%, Interface Declarations Files 10%, Many-Argument Workhorses Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 141 | 91.6% |
| Unknown | 7 | 4.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 3.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 39*

**Composition by Extension & Reason:**
- `.rst`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.8 | 25.5 | 17.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 56.7 | 59.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.5 | 4.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 92.4 | 27.3 | 11.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.6 | 1.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.3 | 96.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 91.2 | 0.6 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 180 | 59 | 4 | `tests/unit/utils_config_test.py` |
| cleanup | 49 | 24 | 1 | `Makefile` |
| guards | 2416 | 107 | 45 | `tests/integration/api_service_test.py` |
| danger | 594 | 78 | 11 | `docker/types/containers.py` |
| concurrency | 39 | 15 | 0 | `docker/api/client.py` |
| connectivity | 2024 | 119 | 32 | `tests/integration/api_container_test.py` |
| io | 452 | 46 | 10 | `tests/integration/api_build_test.py` |
| crypto | 6 | 6 | 0 | `docker/__init__.py` |
| ipc | 52 | 6 | 0 | `Makefile` |
| time | 20 | 8 | 0 | `tests/unit/api_test.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 14 | 9 | 0 | `docker/utils/build.py` |
| events | 5 | 3 | 0 | `docker/transport/npipesocket.py` |
| tests | 1559 | 62 | 30 | `tests/unit/api_container_test.py` |
| docs | 390 | 60 | 8 | `docker/models/containers.py` |
| debt | 46 | 18 | 1 | `scripts/release.sh` |
| mutation | 10311 | 127 | 187 | `tests/integration/api_service_test.py` |
| dead_code | 1038 | 64 | 20 | `tests/unit/api_container_test.py` |
| credential | 5 | 2 | 0 | `tests/unit/fake_api.py` |
| threat | 129 | 36 | 3 | `docker/client.py` |
| ml_ai | 30 | 6 | 0 | `tests/unit/auth_test.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/integration/api_build_test.py` (Hits: 44)
- `tests/unit/utils_build_test.py` (Hits: 43)
- `tests/ssh/api_build_test.py` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **helpers.py** (`tests/helpers.py`) — 20 inbound connections
2. **constants.py** (`docker/constants.py`) — 11 inbound connections
3. **api.py** (`docker/context/api.py`) — 11 inbound connections
4. **resource.py** (`docker/models/resource.py`) — 10 inbound connections
5. **socket.py** (`docker/utils/socket.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **client.py** (`docker/api/client.py`) — 30 outbound dependencies
2. **api_test.py** (`tests/unit/api_test.py`) — 21 outbound dependencies
3. **client.py** (`docker/client.py`) — 14 outbound dependencies
4. **utils.py** (`docker/utils/utils.py`) — 14 outbound dependencies
5. **api_container_test.py** (`tests/integration/api_container_test.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `docker/types/containers.py`) -> Impact: **1116.7** | LOC: 398
- `build` **(Many-Argument Workhorses)** (@ `docker/api/build.py`) -> Impact: **309.5** | LOC: 264
- `__init__` **(Many-Argument Workhorses)** (@ `docker/types/services.py`) -> Impact: **189.9** | LOC: 93
- `__init__` **(Many-Argument Workhorses)** (@ `docker/types/containers.py`) -> Impact: **130.1** | LOC: 102
- `_check_api_features` **(Many-Argument Workhorses)** (@ `docker/api/service.py`) -> Impact: **119.7** | LOC: 92
- `logs` **(Many-Argument Workhorses)** (@ `docker/api/container.py`) -> Impact: **113.5** | LOC: 81
- `__init__` **(Many-Argument Workhorses)** (@ `docker/types/swarm.py`) -> Impact: **108.8** | LOC: 84
- `update_service` **(Many-Argument Workhorses)** (@ `docker/api/service.py`) -> Impact: **103.2** | LOC: 118
- `__init__` **(Many-Argument Workhorses)** (@ `docker/types/services.py`) -> Impact: **85.3** | LOC: 60
- `run` **(Many-Argument Workhorses)** (@ `docker/models/containers.py`) -> Impact: **75.4** | LOC: 378

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/unit/testdata/certs` | 3 | 15000.0 | 0.0% | 0.0% |
| `tests/ssh/config/client` | 2 | 10000.0 | 0.0% | 0.0% |
| `tests/ssh/config/server` | 2 | 10000.0 | 0.0% | 0.0% |
| `tests/integration` | 28 | 4238.8 | 19.84% | 0.0% |
| `tests/unit` | 31 | 3558.82 | 6.16% | 0.0% |
| `docker/api` | 14 | 3545.06 | 38.19% | 10.5% |
| `docker/types` | 8 | 3118.36 | 49.18% | 1.54% |
| `docker/utils` | 10 | 1545.34 | 49.79% | 9.75% |
| `docker/models` | 12 | 1330.54 | 30.06% | 8.23% |
| `docker` | 7 | 733.62 | 39.76% | 20.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `docker/errors.py` -> **99.5207%** Exposure
- `docker/utils/ports.py` -> **97.4762%** Exposure
- `docker/api/exec_api.py` -> **86.7036%** Exposure
- `scripts/versions.py` -> **85.9404%** Exposure
- `docker/models/swarm.py` -> **72.0768%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `docker/api/build.py` -> **100.0%** Exposure
- `docker/api/config.py` -> **100.0%** Exposure
- `docker/api/container.py` -> **100.0%** Exposure
- `docker/api/daemon.py` -> **100.0%** Exposure
- `docker/api/exec_api.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/unit/api_container_test.py` -> **102** Orphaned Functions | **0** Duplicates
- `tests/integration/api_container_test.py` -> **89** Orphaned Functions | **0** Duplicates
- `tests/unit/utils_test.py` -> **75** Orphaned Functions | **0** Duplicates
- `tests/integration/api_service_test.py` -> **69** Orphaned Functions | **0** Duplicates
- `tests/unit/dockertypes_test.py` -> **62** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/unit/auth_test.py` -> **91.2172%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `409` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `docker/errors.py` (PYTHON) -> Cumulative Risk: **726.31**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.73)
- **Magnitude:** 175.28 | **LOC:** 210 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5207%), Safety Score (98.0976%)
- **Heaviest Functions:** `create_api_error_from_http_exception` (Defensive Guards, Impact: 10.8), `__str__` (Compute Cores, Impact: 9.4), `__init__` (Many-Argument Workhorses, Impact: 8.5)

### 2. `docker/context/context.py` (PYTHON) -> Cumulative Risk: **625.76**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.53)
- **Magnitude:** 270.1 | **LOC:** 250 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5342%), Cognitive Load (95.7799%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 28.6), `_load_certs` (Compute Cores, Impact: 15.4), `_load_meta` (Defensive Guards, Impact: 10.0)

### 3. `docker/utils/ports.py` (PYTHON) -> Cumulative Risk: **622.54**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +2.04)
- **Magnitude:** 104.6 | **LOC:** 84 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.4762%)
- **Heaviest Functions:** `split_port` (Compute Cores, Impact: 25.4), `port_range` (Type Conversions, Impact: 11.6), `add_port` (Compute Cores, Impact: 10.4)

### 4. `docker/utils/utils.py` (PYTHON) -> Cumulative Risk: **620.43**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.08)
- **Magnitude:** 596.68 | **LOC:** 518 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.9514%), Documentation (87.7551%)
- **Heaviest Functions:** `parse_host` (Many-Argument Workhorses, Impact: 68.5), `convert_volume_binds` (Defensive Guards, Impact: 30.9), `parse_bytes` (Defensive Guards, Impact: 21.7)

### 5. `docker/types/containers.py` (PYTHON) -> Cumulative Risk: **619.39**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.58)
- **Magnitude:** 1736.92 | **LOC:** 791 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (92.7273%), Safety Score (91.19%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 1116.7), `__init__` (Many-Argument Workhorses, Impact: 130.1), `__init__` (Defensive Guards, Impact: 20.8)

### 6. `docker/utils/build.py` (PYTHON) -> Cumulative Risk: **608.67**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.75)
- **Magnitude:** 356.46 | **LOC:** 261 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2166%), Documentation (93.3333%)
- **Heaviest Functions:** `create_archive` (Many-Argument Workhorses, Impact: 41.7), `walk` (Compute Cores, Impact: 26.0), `matches` (Compute Cores, Impact: 21.7)

### 7. `docker/types/services.py` (PYTHON) -> Cumulative Risk: **605.05**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.30)
- **Magnitude:** 969.06 | **LOC:** 871 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0813%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 189.9), `__init__` (Many-Argument Workhorses, Impact: 85.3), `__init__` (Many-Argument Workhorses, Impact: 38.3)

### 8. `docker/transport/npipesocket.py` (PYTHON) -> Cumulative Risk: **598.52**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.53)
- **Magnitude:** 198.36 | **LOC:** 231 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9979%), Safety Score (80.103%)
- **Heaviest Functions:** `recv_into` (Defensive Guards, Impact: 11.1), `settimeout` (Defensive Guards, Impact: 9.1), `makefile` (Compute Cores, Impact: 8.3)

### 9. `docker/transport/sshconn.py` (PYTHON) -> Cumulative Risk: **587.72**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.63)
- **Magnitude:** 248.56 | **LOC:** 251 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.6237%)
- **Heaviest Functions:** `_create_paramiko_client` (Compute Cores, Impact: 17.1), `get_connection` (Many-Argument Workhorses, Impact: 11.3), `__init__` (Many-Argument Workhorses, Impact: 8.9)

### 10. `docker/api/exec_api.py` (PYTHON) -> Cumulative Risk: **587.44**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.21)
- **Magnitude:** 132.3 | **LOC:** 177 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.8194%), Tech Debt (86.7036%)
- **Heaviest Functions:** `exec_create` (Many-Argument Workhorses, Impact: 43.3), `exec_start` (Many-Argument Workhorses, Impact: 22.7), `exec_resize` (Many-Argument Workhorses, Impact: 5.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/ssh/config/client/id_rsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/client/id_rsa.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/server/known_ed25519.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/server/unknown_ed25519.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/types/containers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1736.92 | **LOC:** 791 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.1527%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 1116.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 130.1)
  * `__init__` **(Defensive Guards)** (Impact: 20.8)
  * `__init__` **(Defensive Guards)** (Impact: 11.1)
  * `__init__` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 66`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 129`
* *Architecture:* `api: 31`, `import: 4`
* *Defense:* `safety: 51`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.247
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 1):` .., ..utils.utils, .base, .healthcheck, docker.types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/integration/api_container_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 972.66 | **LOC:** 1625 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_remove_link` **(Compute Cores)** (Impact: 10.4)
    * *Intent:* # Create containers container1 = self.client.create_container( TEST_IMG, 'cat', detach=True, stdin_o...
  * `test_port` **(Defensive Guards)** (Impact: 7.4)
  * `test_get_container_stats_no_stream` **(Defensive Guards)** (Impact: 7.0)
  * `test_run_shlex_commands` **(Defensive Guards)** (Impact: 6.6)
  * `test_remove` **(Defensive Guards)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 543
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 407`, `args: 95`, `func_start: 93`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 431`, `unreferenced_by_name: 89`
* *Architecture:* `io: 10`, `api: 115`, `concurrency: 3`, `import: 14`
* *Defense:* `safety: 250`, `doc: 1`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .., ..helpers, .base, datetime, docker, docker.constants, docker.utils.socket, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/types/services.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 969.06 | **LOC:** 871 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.4834%), Tech Debt (12.3462%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 189.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 89`, `args: 25`, `func_start: 25`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 138`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `safety: 21`, `doc: 17`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.692
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013072
  * `Imports (Out-Degree: 0):` .., ..constants, ..utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/integration/api_service_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 861.86 | **LOC:** 1468 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.2974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_update_service_with_defaults_endpoint_spec` **(Defensive Guards)** (Impact: 18.4)
  * `_update_service` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* # service update tests seem to be a bit flaky # give them a chance to retry the update with a new ve...
  * `get_service_container` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `test_create_service_with_endpoint_spec` **(Defensive Guards)** (Impact: 9.9)
  * `test_service_logs` **(Defensive Guards)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 529
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 374`, `args: 76`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 487`, `unreferenced_by_name: 69`
* *Architecture:* `api: 73`, `import: 6`
* *Defense:* `safety: 283`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..helpers, .base, docker, pytest, random, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/container.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 774.6 | **LOC:** 1349 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.1849%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `logs` **(Many-Argument Workhorses)** (Impact: 113.5)
  * `update_container` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `containers` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `create_container` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `attach` **(Many-Argument Workhorses)** (Impact: 33.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 74`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 109`, `fragile_debt: 2`
* *Architecture:* `api: 32`, `import: 4`
* *Defense:* `safety: 10`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.275
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011765
  * `Imports (Out-Degree: 0):` .., ..constants, ..types, datetime
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/utils/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 596.68 | **LOC:** 518 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5291%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_host` **(Many-Argument Workhorses)** (Impact: 68.5)
    * *Intent:* # Sensible defaults if not addr and is_win32: return DEFAULT_NPIPE if not addr or addr.strip() == 'u...
  * `convert_volume_binds` **(Defensive Guards)** (Impact: 30.9)
  * `parse_bytes` **(Defensive Guards)** (Impact: 21.7)
  * `_convert_port_binding` **(Defensive Guards)** (Impact: 18.3)
  * `compare_version` **(Type Conversions)** (Impact: 15.2)
    * *Intent:* """Compare docker versions >>> v1 = '1.9' >>> v2 = '1.10' >>> compare_version(v1, v2) 1 >>> compare_...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 96`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 97`
* *Architecture:* `io: 7`, `api: 24`, `import: 14`
* *Defense:* `safety: 24`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., ..constants, ..tls, base64, collections, datetime, functools, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/build.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 508.02 | **LOC:** 383 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4221%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 309.5)
  * `prune_builds` **(Many-Argument Workhorses)** (Impact: 20.0)
    * *Intent:* """ Delete the builder cache Args: filters (dict): Filters to process on the prune list. Needs Docke...
  * `_set_auth_headers` **(Compute Cores)** (Impact: 18.9)
  * `process_dockerfile` **(Compute Cores)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 22`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 46`
* *Architecture:* `io: 12`, `api: 4`, `import: 5`
* *Defense:* `safety: 1`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 0):` .., docker, io, json, logging, os, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/api/service.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 502.38 | **LOC:** 487 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.8203%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_api_features` **(Many-Argument Workhorses)** (Impact: 119.7)
  * `update_service` **(Many-Argument Workhorses)** (Impact: 103.2)
  * `create_service` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `_merge_task_template` **(Compute Cores)** (Impact: 14.5)
  * `services` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* """ List services. Args: filters (dict): Filters to process on the nodes list. Valid filters: ``id``...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 25`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 63`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.275
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011765
  * `Imports (Out-Degree: 0):` .., ..types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/unit/api_container_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 499.46 | **LOC:** 1595 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_create_container_with_device_requests` **(Defensive Guards)** (Impact: 4.4)
  * `test_create_container_with_port_binds` **(Defensive Guards)** (Impact: 3.5)
  * `test_inspect_container_undefined_id` **(Defensive Guards)** (Impact: 3.1)
  * `test_create_container_with_devices` **(Defensive Guards)** (Impact: 2.8)
  * `test_create_container_with_named_volume` **(Defensive Guards)** (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 327`, `args: 103`, `func_start: 103`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 155`, `unreferenced_by_name: 102`
* *Architecture:* `api: 106`, `import: 10`
* *Defense:* `safety: 173`, `doc: 15`, `test: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , ..helpers, .api_test, datetime, docker, docker.api, json, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/api_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 455.54 | **LOC:** 665 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.2466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` **(Defensive Guards)** (Impact: 11.8)
  * `early_response_sending_handler` **(Defensive Guards)** (Impact: 9.7)
  * `fake_resp` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `response` **(Many-Argument Workhorses)** (Impact: 9.1)
  * `test_early_stream_response` **(Defensive Guards)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 184`, `args: 68`, `func_start: 68`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`
* *Architecture:* `io: 30`, `api: 74`, `concurrency: 3`, `import: 22`
* *Defense:* `safety: 59`, `doc: 5`, `test: 57`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.457
  * `Choke Point (Betweenness):` 0.001849 | `Ripple Effect (Closeness):` 0.045752
  * `Imports (Out-Degree: 3):` , datetime, docker, docker.api, docker.constants, http.server, io, json...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `docker/models/containers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 433.42 | **LOC:** 1199 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1602%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `_create_container_args` **(Compute Cores)** (Impact: 31.3)
    * *Intent:* """ Convert arguments to create() to arguments to create_container(). """
  * `list` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `exec_run` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `_host_volume_from_bind` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 100`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 61`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 35`, `import: 10`
* *Defense:* `safety: 10`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.886
  * `Choke Point (Betweenness):` 0.000124 | `Ripple Effect (Closeness):` 0.013072
  * `Imports (Out-Degree: 3):` ..api, ..constants, ..errors, ..types, ..utils, .images, .resource, collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docker/api/client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 415.36 | **LOC:** 533 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.5598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.6)
  * `_read_from_socket` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* """Consume all data from the socket, close the response and return the data. If stream=True, then a ...
  * `_stream_helper` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* """Generator for data coming from a chunked-encoded HTTP response."""
  * `_post_json` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* # Go <1.1 can't unserialize null to a string # so we do this disgusting thing here. data2 = {} if da...
  * `_get_result_tty` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* # We should also use raw streaming (without keep-alives) # if we're dealing with a tty-enabled conta...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 140`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 65`, `dead_code: 1`
* *Architecture:* `io: 19`, `api: 13`, `import: 31`
* *Defense:* `safety: 30`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.053
  * `Choke Point (Betweenness):` 0.00101 | `Ripple Effect (Closeness):` 0.013072
  * `Imports (Out-Degree: 12):` .., ..constants, ..errors, ..tls, ..transport, ..utils, ..utils.json_stream, ..utils.proxy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/integration/api_build_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 387.46 | **LOC:** 598 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.9391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_build_with_cache_from` **(Defensive Guards)** (Impact: 10.2)
  * `test_build_squash` **(Defensive Guards)** (Impact: 6.8)
  * `build_squashed` **(Compute Cores)** (Impact: 6.2)
  * `test_build_with_dockerignore` **(I/O & Config Routines)** (Impact: 6.0)
  * `test_build_with_extra_hosts` **(Defensive Guards)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 139`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 128`, `fragile_debt: 4`, `unreferenced_by_name: 24`
* *Architecture:* `io: 44`, `api: 26`, `import: 9`
* *Defense:* `safety: 36`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..helpers, .base, docker, docker.utils.proxy, io, os, pytest, shutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/api_build_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 386.82 | **LOC:** 589 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.9798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_build_with_cache_from` **(Defensive Guards)** (Impact: 10.2)
  * `test_build_squash` **(Defensive Guards)** (Impact: 6.8)
  * `build_squashed` **(Compute Cores)** (Impact: 6.2)
  * `test_build_with_extra_hosts` **(Defensive Guards)** (Impact: 5.6)
  * `test_build_with_dockerignore` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 130`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 128`, `fragile_debt: 4`, `unreferenced_by_name: 24`
* *Architecture:* `io: 40`, `api: 26`, `import: 9`
* *Defense:* `safety: 36`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..helpers, .base, docker, docker.utils.proxy, io, os, pytest, shutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/integration/models_containers_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 384.86 | **LOC:** 561 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_list_sparse` **(Defensive Guards)** (Impact: 6.6)
  * `test_list` **(Defensive Guards)** (Impact: 6.5)
  * `test_ports_target_none` **(Defensive Guards)** (Impact: 5.2)
  * `test_ports_target_tuple` **(Defensive Guards)** (Impact: 5.2)
  * `test_ports_target_list` **(Defensive Guards)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 146`, `args: 41`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `state_mutation: 171`, `unreferenced_by_name: 41`
* *Architecture:* `api: 43`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 85`, `test: 50`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..helpers, .base, docker, os, pytest, tempfile, threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/image.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 372.76 | **LOC:** 602 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0909%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pull` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `images` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* """ List images. Similar to the ``docker images`` command. Args: name (str): Only show images belong...
  * `import_image` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `push` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `_import_image_params` **(Many-Argument Workhorses)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 57`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 55`
* *Architecture:* `io: 2`, `api: 20`, `import: 4`
* *Defense:* `safety: 5`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.275
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011765
  * `Imports (Out-Degree: 0):` .., ..constants, from, from., logging, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/utils/build.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 356.46 | **LOC:** 261 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.9512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_archive` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `walk` **(Compute Cores)** (Impact: 26.0)
  * `matches` **(Compute Cores)** (Impact: 21.7)
  * `rec_walk` **(Compute Cores)** (Impact: 21.4)
  * `tar` **(Many-Argument Workhorses)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 55`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 56`
* *Architecture:* `io: 16`, `api: 16`, `import: 7`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..constants, .fnmatch, io, os, re, tarfile, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/auth.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 333.4 | **LOC:** 379 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.8771%), Tech Debt (40.5014%)
**Top Internal Functions/Classes:**
  * `parse_auth` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* """ Parses authentication entries Args: entries: Dict of authentication entries. raise_on_error: If ...
  * `resolve_authconfig` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* """ Returns the authentication data from the given auth configuration for a specific registry. As wi...
  * `load_config` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* """ Loads authentication data from a Docker configuration file in the given root directory or if con...
  * `_resolve_authconfig_credstore` **(Defensive Guards)** (Impact: 15.3)
  * `get_config_header` **(Compute Cores)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 81`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 51`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 22`, `import: 5`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , .utils, base64, json, logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/integration/api_service_test.py` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 861.86
- `tests/integration/api_network_test.py` -> **Rob Murray** (100.0% isolated ownership) | Magnitude: 190.9
- `tests/unit/client_test.py` -> **Ricardo Branco** (100.0% isolated ownership) | Magnitude: 112.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docker/context/api.py` -> **Severity: 0.186** (Bridge: 0.0022 * Flux: 85.0%)
- `docker/context/context.py` -> **Severity: 0.15** (Bridge: 0.0018 * Flux: 85.0%)
- `docker/api/client.py` -> **Severity: 0.101** (Bridge: 0.001 * Flux: 99.9999%)
- `docker/constants.py` -> **Severity: 0.099** (Bridge: 0.001 * Flux: 100.0%)
- `docker/models/images.py` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docker/utils/socket.py` -> **Severity: 9.746** (Embedded: 0.1271 * Error Risk: 76.6785%)
- `docker/constants.py` -> **Severity: 9.231** (Embedded: 0.0988 * Error Risk: 93.445%)
- `docker/context/api.py` -> **Severity: 8.427** (Embedded: 0.0902 * Error Risk: 93.4817%)
- `docker/errors.py` -> **Severity: 8.311** (Embedded: 0.0847 * Error Risk: 98.0976%)
- `tests/helpers.py` -> **Severity: 7.246** (Embedded: 0.1307 * Error Risk: 55.433%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/helpers.py` -> **Severity: 4808.656** (Blast Radius: 51.092 * Doc Risk: 94.1176%)
- `docker/context/context.py` -> **Severity: 3082.7** (Blast Radius: 30.827 * Doc Risk: 100.0%)
- `docker/errors.py` -> **Severity: 3036.852** (Blast Radius: 32.798 * Doc Risk: 92.5926%)
- `tests/unit/api_test.py` -> **Severity: 1859.225** (Blast Radius: 19.457 * Doc Risk: 95.5556%)
- `docker/models/resource.py` -> **Severity: 1772.624** (Blast Radius: 26.068 * Doc Risk: 68.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
