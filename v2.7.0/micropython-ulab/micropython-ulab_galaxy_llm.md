# ARCHITECTURAL_BRIEF: micropython-ulab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/v923z/micropython-ulab` |
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
| Total Artifacts | 333 |
| Analyzed Artifacts (Scanned) | 187 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 146 |
| Total LOC | 19165 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 56.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2999 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4444 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2861 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 112 | 3350 | 59.9% |
| C | 66 | 15647 | 35.3% |
| SHELL | 4 | 132 | 2.1% |
| MARKDOWN | 2 | 0 | 1.1% |
| PLAINTEXT | 2 | 0 | 1.1% |
| MAKEFILE | 1 | 36 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 183 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 146*

**Composition by Extension & Reason:**
- `.exp`: 92x Excluded (Unsupported Extension: '.exp'), 1x Unsupported Format (.exp)
- `.ipynb`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 1x Excluded (Unsupported Extension: '.cmake')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.3 | 23.9 | 9.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 63.6 | 73.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.7 | 5.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 95.8 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 1.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.4 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5834 | 57 | 88 | `code/ndarray.c` |
| cleanup | 6 | 4 | 0 | `run-tests` |
| guards | 1586 | 140 | 21 | `code/ndarray.c` |
| danger | 530 | 99 | 6 | `code/numpy/carray/carray.c` |
| concurrency | 10 | 3 | 0 | `run-tests` |
| connectivity | 384 | 65 | 4 | `code/ndarray.h` |
| io | 87 | 9 | 0 | `run-tests` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 1 | 0 | `run-tests` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `run-tests` |
| events | 4 | 1 | 0 | `run-tests` |
| tests | 2 | 1 | 0 | `tests/1d/numpy/universal_functions.py` |
| docs | 22 | 8 | 0 | `snippets/scipy/signal/filter_design.py` |
| debt | 880 | 112 | 10 | `tests/2d/numpy/numericals.py` |
| mutation | 7079 | 147 | 110 | `code/ndarray.c` |
| dead_code | 132 | 29 | 1 | `code/ndarray.c` |
| credential | 0 | 0 | 0 | - |
| threat | 145 | 10 | 0 | `code/ndarray.h` |
| ml_ai | 315 | 140 | 2 | `code/numpy/vector.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `run-tests` (Hits: 26)
- `build-cp.sh` (Hits: 19)
- `build.sh` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ulab.h** (`code/ulab.h`) — 43 inbound connections
2. **ndarray.h** (`code/ndarray.h`) — 34 inbound connections
3. **ulab_tools.h** (`code/ulab_tools.h`) — 23 inbound connections
4. **carray_tools.h** (`code/numpy/carray/carray_tools.h`) — 13 inbound connections
5. **carray.h** (`code/numpy/carray/carray.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **numpy.c** (`code/numpy/numpy.c`) — 19 outbound dependencies
2. **ulab.c** (`code/ulab.c`) — 18 outbound dependencies
3. **ndarray.c** (`code/ndarray.c`) — 15 outbound dependencies
4. **transform.c** (`code/numpy/transform.c`) — 13 outbound dependencies
5. **run-tests** (`run-tests`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ndarray_binary_more` (@ `code/ndarray_operators.c`) -> Impact: **326.7** | LOC: 142
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MULTIPLY */ #if NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS | NDARRAY_H...
- `ndarray_binary_logical` (@ `code/ndarray_operators.c`) -> Impact: **294.9** | LOC: 184
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_POWER */ #if NDARRAY_HAS_BINARY_OP_OR | NDARRAY_HAS_BINARY_OP_XOR | NDARRAY_HAS_BINARY_OP_AND
- `ndarray_binary_equality` (@ `code/ndarray_operators.c`) -> Impact: **243.8** | LOC: 125
  * *Intent:* */ #if NDARRAY_HAS_BINARY_OP_EQUAL | NDARRAY_HAS_BINARY_OP_NOT_EQUAL
- `vector_exp` (@ `code/numpy/vector.c`) -> Impact: **228.1** | LOC: 482
  * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_SCIPY_SPECIAL_HAS_ERFC */ #if ULAB_NUMPY_HAS_EXP //| def exp(a: _ScalarOrArrayLike) -> _Sc...
- `ndarray_unary_op` (@ `code/ndarray.c`) -> Impact: **214.8** | LOC: 346
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS */ #if NDARRAY_HAS_UNARY_OPS
- `ndarray_binary_op` (@ `code/ndarray.c`) -> Impact: **210.9** | LOC: 218
  * *Intent:* #if NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS
- `ndarray_binary_true_divide` (@ `code/ndarray_operators.c`) -> Impact: **163.2** | LOC: 89
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_SUBTRACT */ #if NDARRAY_HAS_BINARY_OP_TRUE_DIVIDE
- `run_tests` (@ `run-tests`) -> Impact: **159.4** | LOC: 248
- `ndarray_binary_subtract` (@ `code/ndarray_operators.c`) -> Impact: **158.6** | LOC: 102
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS | NDARRAY_HAS_BINARY_OP_LESS_EQUAL */ #if NDARRAY...
- `io_loadtxt` (@ `code/numpy/io/io.c`) -> Impact: **158.1** | LOC: 241

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `code/numpy` | 22 | 6374.34 | 42.59% | 3.04% |
| `code` | 11 | 6115.64 | 47.03% | 18.72% |
| `tests/2d/numpy` | 46 | 1250.62 | 10.46% | 0.0% |
| `code/numpy/carray` | 4 | 1220.04 | 40.69% | 19.97% |
| `snippets/scipy/signal` | 2 | 1080.36 | 25.52% | 6.0% |
| `__monolith__` | 9 | 920.82 | 33.19% | 1.41% |
| `code/numpy/io` | 2 | 882.0 | 38.76% | 0.0% |
| `code/numpy/linalg` | 4 | 781.4 | 37.22% | 13.61% |
| `code/scipy/integrate` | 2 | 662.26 | 36.36% | 0.0% |
| `tests/1d/numpy` | 14 | 438.96 | 12.43% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `code/ulab_tools.c` -> **99.6643%** Exposure
- `snippets/numpy/core/fromnumeric.py` -> **98.9013%** Exposure
- `code/numpy/ndarray/ndarray_iter.c` -> **92.4142%** Exposure
- `snippets/rclass.py` -> **90.9512%** Exposure
- `code/numpy/carray/carray_tools.c` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build-cp.sh` -> **100.0%** Exposure
- `build.sh` -> **100.0%** Exposure
- `code/micropython.mk` -> **100.0%** Exposure
- `code/ndarray.c` -> **100.0%** Exposure
- `code/numpy/approx.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/ndarray.c` -> **22** Orphaned Functions | **0** Duplicates
- `code/ndarray_operators.c` -> **14** Orphaned Functions | **0** Duplicates
- `code/ulab_tools.c` -> **12** Orphaned Functions | **0** Duplicates
- `code/numpy/carray/carray.c` -> **6** Orphaned Functions | **0** Duplicates
- `snippets/numpy/core/fromnumeric.py` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `541` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `code/ulab_tools.c` (C) -> Cumulative Risk: **671.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 320.86 | **LOC:** 332 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9987%), Tech Debt (99.6643%)
- **Heaviest Functions:** `ndarray_upcast_dtype` (Impact: 43.1), `ulab_tools_inspect_out` (Impact: 20.9), `ndarray_get_float_index` (Impact: 18.7)

### 2. `code/ndarray.c` (C) -> Cumulative Risk: **652.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2587.62 | **LOC:** 2118 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (95.2624%)
- **Heaviest Functions:** `ndarray_unary_op` (Impact: 214.8), `ndarray_binary_op` (Impact: 210.9), `ndarray_assign_from_boolean_index` (Impact: 137.6)

### 3. `run-tests` (PYTHON) -> Cumulative Risk: **646.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 738.72 | **LOC:** 571 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.9406%), Cognitive Load (96.3482%)
- **Heaviest Functions:** `run_tests` (Impact: 159.4), `run_micropython` (Impact: 103.8), `run_one_test` (Impact: 47.6)

### 4. `code/numpy/create.c` (C) -> Cumulative Risk: **633.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1181.08 | **LOC:** 1217 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.7344%)
- **Heaviest Functions:** `create_take` (Impact: 111.5), `create_meshgrid` (Impact: 84.0), `create_concatenate` (Impact: 67.7)

### 5. `code/ndarray_properties.c` (C) -> Cumulative Risk: **609.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 106.68 | **LOC:** 105 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (90.0414%)
- **Heaviest Functions:** `ndarray_properties_attr` (Impact: 67.9)

### 6. `code/ndarray_operators.c` (C) -> Cumulative Risk: **593.85**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2406.28 | **LOC:** 1246 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%), Safety Score (92.2338%)
- **Heaviest Functions:** `ndarray_binary_more` (Impact: 326.7), `ndarray_binary_logical` (Impact: 294.9), `ndarray_binary_equality` (Impact: 243.8)

### 7. `code/numpy/carray/carray.c` (C) -> Cumulative Risk: **586.31**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1112.46 | **LOC:** 835 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.0928%)
- **Heaviest Functions:** `carray_binary_subtract` (Impact: 108.3), `carray_binary_equal_not_equal` (Impact: 92.5), `carray_binary_add` (Impact: 84.5)

### 8. `snippets/rclass.py` (PYTHON) -> Cumulative Risk: **582.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 95.44 | **LOC:** 76 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.478%)
- **Heaviest Functions:** `__getitem__` (Impact: 28.9), `__len__` (Impact: 1.5)

### 9. `code/numpy/ndarray/ndarray_iter.c` (C) -> Cumulative Risk: **573.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 37.46 | **LOC:** 67 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (92.4142%)
- **Heaviest Functions:** `ndarray_flatiter_next` (Impact: 6.6), `ndarray_new_flatiterator` (Impact: 2.2), `ndarray_get_flatiterator` (Impact: 1.9)

### 10. `code/numpy/numerical.c` (C) -> Cumulative Risk: **573.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1569.6 | **LOC:** 1430 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.4773%)
- **Heaviest Functions:** `numerical_sum_mean_std_ndarray` (Impact: 126.4), `numerical_all_any` (Impact: 125.6), `numerical_argmin_argmax_ndarray` (Impact: 92.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `code/ndarray.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2587.62 | **LOC:** 2118 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.2624%), Tech Debt (40.9947%)
**Top Internal Functions/Classes:**
  * `ndarray_unary_op` (Impact: 214.8)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS */ #if NDARRAY_HAS_UNARY_OPS
  * `ndarray_binary_op` (Impact: 210.9)
    * *Intent:* #if NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS
  * `ndarray_assign_from_boolean_index` (Impact: 137.6)
  * `ndarray_print` (Impact: 72.2)
    * *Intent:* #endif
  * `ndarray_dtype_make_new` (Impact: 56.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 636`, `structural_boundaries: 188`, `args: 186`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 343`, `dead_code: 16`, `planned_debt: 7`, `unreferenced_by_name: 22`
* *Architecture:* `api: 57`, `import: 15`
* *Defense:* `safety: 105`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` math.h, ndarray.h, ndarray_operators.h, carray.h, carray_tools.h, binary.h, obj.h, objint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray_operators.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2406.28 | **LOC:** 1246 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.2662%), Tech Debt (22.6715%)
**Top Internal Functions/Classes:**
  * `ndarray_binary_more` (Impact: 326.7)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MULTIPLY */ #if NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_M...
  * `ndarray_binary_logical` (Impact: 294.9)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_POWER */ #if NDARRAY_HAS_BINARY_OP_OR | NDARRAY_HAS_BINARY_OP_XOR | ...
  * `ndarray_binary_equality` (Impact: 243.8)
    * *Intent:* */ #if NDARRAY_HAS_BINARY_OP_EQUAL | NDARRAY_HAS_BINARY_OP_NOT_EQUAL
  * `ndarray_binary_true_divide` (Impact: 163.2)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_SUBTRACT */ #if NDARRAY_HAS_BINARY_OP_TRUE_DIVIDE
  * `ndarray_binary_subtract` (Impact: 158.6)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 712`, `structural_boundaries: 57`, `args: 40`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 136`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` math.h, ndarray.h, ndarray_operators.h, carray.h, objtuple.h, runtime.h, ulab.h, ulab_tools.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/numerical.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1569.6 | **LOC:** 1430 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2888%), Tech Debt (8.575%)
**Top Internal Functions/Classes:**
  * `numerical_sum_mean_std_ndarray` (Impact: 126.4)
  * `numerical_all_any` (Impact: 125.6)
    * *Intent:* #if ULAB_NUMPY_HAS_ALL | ULAB_NUMPY_HAS_ANY
  * `numerical_argmin_argmax_ndarray` (Impact: 92.8)
  * `numerical_roll` (Impact: 92.0)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_ROLL //| def roll(array: ulab.numpy.ndarray, distance: int, *, axis: Optio...
  * `numerical_cross` (Impact: 84.9)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_CROSS //| def cross(a: ulab.numpy.ndarray, b: ulab.numpy.ndarray) -> ulab....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 75`, `args: 100`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 230`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 75`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ulab.h, ulab_tools.h, carray_tools.h, math.h, numerical.h, builtin.h, misc.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/create.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1181.08 | **LOC:** 1217 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.4382%), Tech Debt (8.8721%)
**Top Internal Functions/Classes:**
  * `create_take` (Impact: 111.5)
  * `create_meshgrid` (Impact: 84.0)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_MESHGRID //| def meshgrid(*xi, indexing="xy"): //| """ //| .. param: xi //...
  * `create_concatenate` (Impact: 67.7)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_CONCATENATE //| def concatenate(arrays: Tuple[ulab.numpy.ndarray], *, axis...
  * `create_arange` (Impact: 48.8)
    * *Intent:* //| """ //| .. param: start //| First value in the array, optional, defaults to 0 //| .. param: stop...
  * `create_logspace` (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 185 instances
* *State Mutation (weighted view):* 560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 31`, `args: 66`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 190`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 94`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ulab.h, ulab_tools.h, create.h, math.h, obj.h, runtime.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/carray/carray.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1112.46 | **LOC:** 835 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.2364%), Tech Debt (17.6347%)
**Top Internal Functions/Classes:**
  * `carray_binary_subtract` (Impact: 108.3)
  * `carray_binary_equal_not_equal` (Impact: 92.5)
  * `carray_binary_add` (Impact: 84.5)
  * `carray_binary_divide` (Impact: 81.4)
  * `carray_binary_multiply` (Impact: 54.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 478
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 23`, `args: 19`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 184`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ndarray.h, ulab.h, ulab_tools.h, carray.h, math.h, builtin.h, misc.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/scipy/signal/filter_design.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1069.84 | **LOC:** 1480 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.0389%), Tech Debt (12.0059%)
**Top Internal Functions/Classes:**
  * `iirfilter` (Impact: 124.5)
  * `zpk2sos` (Impact: 77.0)
    * *Intent:* """ Return second-order sections from zeros, poles, and gain of a system Parameters ---------- z : a...
  * `buttord` (Impact: 61.5)
    * *Intent:* """Butterworth filter order selection. Return the order of the lowest order digital or analog Butter...
  * `zpk2tf` (Impact: 28.9)
    * *Intent:* """ Return polynomial transfer function representation from zeros and poles Parameters ---------- z ...
  * `_cplxreal` (Impact: 22.5)
    * *Intent:* """ Split into complex and real parts, combining conjugate pairs. The 1-D input vector `z` is split ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 81`, `args: 23`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 238`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 17`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ...numpy, math, matplotlib.pyplot, scipy, ulab
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/io/io.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 868.36 | **LOC:** 807 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5105%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `io_loadtxt` (Impact: 158.1)
  * `io_load` (Impact: 89.8)
  * `io_savetxt` (Impact: 60.0)
  * `io_save` (Impact: 43.4)
  * `io_format_float` (Impact: 31.5)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_SAVE */ #if ULAB_NUMPY_HAS_SAVETXT
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 33`, `args: 44`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 150`, `dead_code: 1`
* *Architecture:* `io: 16`, `import: 12`
* *Defense:* `safety: 27`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ndarray.h, ulab_tools.h, vfs.h, io.h, math.h, builtin.h, formatfloat.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-tests` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 738.72 | **LOC:** 571 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3482%), Tech Debt (12.7127%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 159.4)
  * `run_micropython` (Impact: 103.8)
  * `run_one_test` (Impact: 47.6)
  * `convert_regex_escapes` (Impact: 10.7)
    * *Intent:* # unescape wanted regex chars and escape unwanted ones
  * `__call__` (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 4 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 103 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 31
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 79`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 119`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 26`, `api: 14`, `concurrency: 6`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, glob, multiprocessing, multiprocessing.pool, os, platform, pty, pyboard...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/compare.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 710.74 | **LOC:** 774 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.397%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare_function` (Impact: 129.1)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_BINCOUNT */
  * `compare_bincount` (Impact: 80.2)
    * *Intent:* #include <math.h> #include <stdlib.h> #include <string.h> #include "py/obj.h" #include "py/runtime.h...
  * `compare_where` (Impact: 53.5)
    * *Intent:* //| //| :param condition: //| Input scalar or array. If an element (or scalar) is truthy, //| the co...
  * `compare_nonzero` (Impact: 52.9)
    * *Intent:* #if ULAB_NUMPY_HAS_NONZERO //| def nonzero(x: _ScalarOrArrayLike) -> ulab.numpy.ndarray: //| """ //|...
  * `compare_isinf_isfinite` (Impact: 35.4)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_ISFINITE | ULAB_NUMPY_HAS_ISINF
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 33`, `args: 67`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 102`, `dead_code: 2`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `safety: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ndarray_operators.h, ulab.h, ulab_tools.h, carray_tools.h, compare.h, math.h, misc.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/bitwise.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 678.46 | **LOC:** 431 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bitwise_left_shift_loop` (Impact: 87.9)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_LEFT_SHIFT
  * `bitwise_right_shift_loop` (Impact: 87.9)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_RIGHT_SHIFT
  * `bitwise_bitwise_and_loop` (Impact: 74.1)
    * *Intent:* * */ #include <math.h> #include <stdio.h> #include <stdlib.h> #include <string.h> #include "py/obj.h...
  * `bitwise_bitwise_or_loop` (Impact: 74.1)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_BITWISE_OR
  * `bitwise_bitwise_xor_loop` (Impact: 74.1)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_BITWISE_XOR
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 26`, `args: 23`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 67`
* *Architecture:* `api: 11`, `import: 7`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bitwise.h, math.h, obj.h, runtime.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/vector.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 669.62 | **LOC:** 979 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.4275%), Tech Debt (11.1844%)
**Top Internal Functions/Classes:**
  * `vector_exp` (Impact: 228.1)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_SCIPY_SPECIAL_HAS_ERFC */ #if ULAB_NUMPY...
  * `vector_generic_vector` (Impact: 57.9)
    * *Intent:* #include "../ulab.h" #include "../ulab_tools.h" #include "carray/carray_tools.h" #include "vector.h"...
  * `vector_sqrt` (Impact: 46.2)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_SINH */ #if ULAB_NUMPY_HAS_SQR...
  * `vector_arctan2` (Impact: 38.7)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_ATANH */ #if ULAB_NUMPY_HAS_AR...
  * `vector_generic_vector` (Impact: 29.9)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 37`, `args: 57`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 61`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `safety: 22`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ulab.h, ulab_tools.h, carray_tools.h, math.h, binary.h, obj.h, objarray.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/integrate/integrate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 645.92 | **LOC:** 702 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tanhsinh` (Impact: 81.8)
    * *Intent:* // integrate function f, range a..b, max levels n, error tolerance eps
  * `exp_sinh_opt_d` (Impact: 42.7)
    * *Intent:* #if ULAB_INTEGRATE_HAS_TANHSINH // Tanh-Sinh, Sinh-Sinh and Exp-Sinh quadrature // https://www.geniv...
  * `qromb` (Impact: 16.1)
    * *Intent:* #endif /* ULAB_INTEGRATE_HAS_TANHSINH */ #if ULAB_INTEGRATE_HAS_ROMBERG // Romberg quadrature // Thi...
  * `qakro` (Impact: 15.0)
  * `integrate_tanhsinh` (Impact: 14.1)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to integrate //| :param float a: The low...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 18`, `args: 29`, `func_start: 13`
* *Risk/State:* `state_mutation: 132`, `dead_code: 13`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ndarray.h, ulab.h, ulab_tools.h, integrate.h, math.h, misc.h, obj.h, objtuple.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 544.2 | **LOC:** 543 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.3527%), Tech Debt (9.5623%)
**Top Internal Functions/Classes:**
  * `linalg_qr` (Impact: 58.0)
    * *Intent:* #if ULAB_MAX_DIMS > 1 //| def qr(m: ulab.numpy.ndarray) -> Tuple[ulab.numpy.ndarray, ulab.numpy.ndar...
  * `linalg_norm` (Impact: 50.2)
    * *Intent:* #endif //| def norm(x: ulab.numpy.ndarray) -> float: //| """ //| :param ~ulab.numpy.ndarray x: a vec...
  * `linalg_cholesky` (Impact: 24.0)
    * *Intent:* //| """Linear algebra functions""" //| #if ULAB_MAX_DIMS > 1 //| def cholesky(A: ulab.numpy.ndarray)...
  * `linalg_det` (Impact: 21.3)
    * *Intent:* //| def det(m: ulab.numpy.ndarray) -> float: //| """ //| :param: m, a square matrix //| :return floa...
  * `linalg_eig` (Impact: 13.8)
    * *Intent:* #endif #if ULAB_MAX_DIMS > 1 //| def eig(m: ulab.numpy.ndarray) -> Tuple[ulab.numpy.ndarray, ulab.nu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 15`, `args: 39`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 124`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `import: 10`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ulab.h, ulab_tools.h, carray_tools.h, linalg.h, math.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/transform.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 443.4 | **LOC:** 457 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.4455%), Tech Debt (11.0727%)
**Top Internal Functions/Classes:**
  * `transform_delete` (Impact: 86.8)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_COMPRESS */ #if ULAB_NUMPY_HAS_DELETE
  * `transform_compress` (Impact: 60.7)
    * *Intent:* #include <math.h> #include <stdlib.h> #include <string.h> #include "py/obj.h" #include "py/runtime.h...
  * `transform_dot` (Impact: 27.0)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_DELETE */ #if ULAB_MAX_DIMS > 1 #if ULAB_NUMPY_HAS_DOT //| def dot(m1: ulab...
  * `transform_size` (Impact: 13.7)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_DOT */ #endif /* ULAB_MAX_DIMS > 1 */ #if ULAB_NUMPY_HAS_SIZE
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 10`, `args: 39`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 87`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ulab.h, ulab_tools.h, carray_tools.h, math.h, numerical.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/utils/utils.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 408.52 | **LOC:** 415 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `utils_from_intbuffer_helper` (Impact: 104.8)
    * *Intent:* #if ULAB_UTILS_HAS_FROM_INT16_BUFFER | ULAB_UTILS_HAS_FROM_UINT16_BUFFER | ULAB_UTILS_HAS_FROM_INT32...
  * `utils_spectrogram` (Impact: 100.6)
    * *Intent:* #endif /* ULAB_UTILS_HAS_FROM_INT16_BUFFER | ULAB_UTILS_HAS_FROM_UINT16_BUFFER | ULAB_UTILS_HAS_FROM...
  * `utils_from_int16_buffer` (Impact: 2.1)
    * *Intent:* #ifdef ULAB_UTILS_HAS_FROM_INT16_BUFFER
  * `utils_from_uint16_buffer` (Impact: 2.1)
    * *Intent:* #endif #ifdef ULAB_UTILS_HAS_FROM_UINT16_BUFFER
  * `utils_from_int32_buffer` (Impact: 2.1)
    * *Intent:* #endif #ifdef ULAB_UTILS_HAS_FROM_INT32_BUFFER
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 11`, `args: 34`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 62`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fft_tools.h, ulab_tools.h, math.h, misc.h, obj.h, runtime.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/fft/fft_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 326.48 | **LOC:** 267 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.4769%), Tech Debt (14.402%)
**Top Internal Functions/Classes:**
  * `fft_fft_ifft` (Impact: 48.3)
  * `fft_fft_ifft` (Impact: 26.7)
    * *Intent:* /* * The following function is a helper interface to the python side. * It has been factored out fro...
  * `fft_kernel` (Impact: 20.1)
    * *Intent:* #else /* ULAB_SUPPORTS_COMPLEX & ULAB_FFT_IS_NUMPY_COMPATIBLE */
  * `fft_kernel` (Impact: 18.2)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 6`, `args: 17`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 81`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ndarray.h, ulab_tools.h, carray_tools.h, fft_tools.h, math.h, runtime.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ulab_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 320.86 | **LOC:** 332 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1854%), Tech Debt (99.6643%)
**Top Internal Functions/Classes:**
  * `ndarray_upcast_dtype` (Impact: 43.1)
    * *Intent:* #if NDARRAY_BINARY_USES_FUN_POINTER | ULAB_NUMPY_HAS_WHERE
  * `ulab_tools_inspect_out` (Impact: 20.9)
  * `ndarray_get_float_index` (Impact: 18.7)
  * `ndarray_get_float_value` (Impact: 16.3)
  * `tools_reduce_axes` (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 68`, `args: 34`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 29`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ndarray.h, runtime.h, string.h, ulab.h, ulab_tools.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 319.48 | **LOC:** 809 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.2427%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 29`, `args: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 77`, `dead_code: 1`
* *Architecture:* `api: 62`, `import: 5`
* *Defense:* `safety: 94`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.433
  * `Choke Point (Betweenness):` 0.000262 | `Ripple Effect (Closeness):` 0.218347
  * `Imports (Out-Degree: 1):` binary.h, objarray.h, objlist.h, objstr.h, ulab.h
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `code/numpy/random/random.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 275.94 | **LOC:** 362 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4643%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `random_random` (Impact: 46.2)
    * *Intent:* #endif /* ULAB_NUMPY_RANDOM_HAS_NORMAL */ #if ULAB_NUMPY_RANDOM_HAS_RANDOM
  * `random_normal` (Impact: 29.6)
    * *Intent:* #endif #if ULAB_NUMPY_RANDOM_HAS_NORMAL
  * `random_generator_make_new` (Impact: 24.6)
  * `random_uniform` (Impact: 22.6)
    * *Intent:* #endif /* ULAB_NUMPY_RANDOM_HAS_RANDOM */ #if ULAB_NUMPY_RANDOM_HAS_UNIFORM
  * `pcg32_next` (Impact: 3.2)
    * *Intent:* // END OF GENERATOR COMPONENTS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 16`, `args: 29`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `dead_code: 3`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, builtin.h, obj.h, runtime.h, random.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/numerical.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 270.38 | **LOC:** 524 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.2685%), Tech Debt (10.1545%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 4`, `args: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 82`, `planned_debt: 2`
* *Architecture:* `import: 2`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.527
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.021505
  * `Imports (Out-Degree: 2):` ndarray.h, ulab.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `code/scipy/optimize/optimize.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 229.2 | **LOC:** 418 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.4207%), Tech Debt (16.9256%)
**Top Internal Functions/Classes:**
  * `optimize_fmin` (Impact: 44.5)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float x0: The initi...
  * `optimize_bisect` (Impact: 20.2)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float a: The left s...
  * `optimize_jacobi` (Impact: 17.5)
    * *Intent:* #endif #if ULAB_SCIPY_OPTIMIZE_HAS_CURVE_FIT
  * `optimize_curve_fit` (Impact: 15.2)
  * `optimize_newton` (Impact: 13.9)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float x0: The initi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 10`, `args: 44`, `func_start: 7`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ndarray.h, ulab.h, ulab_tools.h, math.h, optimize.h, misc.h, obj.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray_operators.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 228.22 | **LOC:** 714 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.2001%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `args: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 62`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 65`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.476
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.016129
  * `Imports (Out-Degree: 1):` ndarray.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `code/numpy/poly.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 226.9 | **LOC:** 219 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (16.9256%)
**Top Internal Functions/Classes:**
  * `poly_polyfit` (Impact: 43.9)
    * *Intent:* */ #include "py/obj.h" #include "py/runtime.h" #include "py/objarray.h" #include "../ulab.h" #includ...
  * `poly_polyval` (Impact: 20.3)
  * `poly_eval` (Impact: 4.4)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_POLYVAL
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 5`, `args: 27`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ulab.h, ulab_tools.h, carray_tools.h, linalg_tools.h, poly.h, obj.h, objarray.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/linalg/linalg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 223.14 | **LOC:** 282 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.7272%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `solve_triangular` (Impact: 30.9)
    * *Intent:* //| def solve_triangular(A: ulab.numpy.ndarray, b: ulab.numpy.ndarray, lower: bool) -> ulab.numpy.nd...
  * `cho_solve` (Impact: 23.8)
    * *Intent:* //| def cho_solve(L: ulab.numpy.ndarray, b: ulab.numpy.ndarray) -> ulab.numpy.ndarray: //| """ //| :...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 8`, `args: 30`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 73`
* *Architecture:* `import: 10`
* *Defense:* `safety: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` linalg_tools.h, ulab.h, ulab_tools.h, linalg.h, math.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 203.68 | **LOC:** 171 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1945%), Tech Debt (44.8577%)
**Top Internal Functions/Classes:**
  * `linalg_jacobi_rotations` (Impact: 34.2)
    * *Intent:* /* * The following function calculates the eigenvalues and eigenvectors of a symmetric * real matrix...
  * `linalg_invert_matrix` (Impact: 25.3)
    * *Intent:* */ #include <math.h> #include <string.h> #include "py/runtime.h" #include "linalg_tools.h" /* * The ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 9`, `args: 10`, `func_start: 2`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` linalg_tools.h, math.h, runtime.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `code/numpy/create.c` -> Churn: **63.09%** | Cog Load: 77.4382% | Debt: 8.8721%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/ndarray.c` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 2587.62
- `code/numpy/create.c` -> **Iyassou Shimels** (100.0% isolated ownership) | Magnitude: 1181.08
- `code/ndarray.h` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 319.48
- `code/ndarray_properties.c` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 106.68

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/ndarray.h` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 99.9978%)
- `code/ulab_tools.h` -> **Severity: 0.01** (Bridge: 0.0003 * Flux: 31.0026%)
- `code/numpy/vector.h` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 99.9942%)
- `code/numpy/numerical.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `code/ndarray_operators.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9857%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `code/ndarray.h` -> **Severity: 13.819** (Embedded: 0.2183 * Error Risk: 63.2898%)
- `code/ulab_tools.h` -> **Severity: 6.802** (Embedded: 0.1253 * Error Risk: 54.2752%)
- `code/numpy/numerical.h` -> **Severity: 1.93** (Embedded: 0.0215 * Error Risk: 89.7686%)
- `code/numpy/carray/carray.h` -> **Severity: 1.752** (Embedded: 0.0269 * Error Risk: 65.1871%)
- `code/numpy/vector.h` -> **Severity: 1.089** (Embedded: 0.0161 * Error Risk: 67.5392%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `snippets/numpy/core/overrides.py` -> **Severity: 797.8** (Blast Radius: 15.956 * Doc Risk: 50.0%)
- `code/ndarray.c` -> **Severity: 362.7** (Blast Radius: 3.627 * Doc Risk: 100.0%)
- `code/ndarray_operators.c` -> **Severity: 362.7** (Blast Radius: 3.627 * Doc Risk: 100.0%)
- `code/ndarray_properties.c` -> **Severity: 362.7** (Blast Radius: 3.627 * Doc Risk: 100.0%)
- `code/numpy/approx.c` -> **Severity: 362.7** (Blast Radius: 3.627 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
