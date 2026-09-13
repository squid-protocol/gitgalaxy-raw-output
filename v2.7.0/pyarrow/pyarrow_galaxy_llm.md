# ARCHITECTURAL_BRIEF: pyarrow
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
| Total Artifacts | 301 |
| Analyzed Artifacts (Scanned) | 238 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 63 |
| Total LOC | 89778 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5792 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2157 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1259 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 32 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 174 | 77904 | 73.1% |
| CPP | 57 | 11874 | 23.9% |
| PLAINTEXT | 5 | 0 | 2.1% |
| MARKDOWN | 2 | 0 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 230 | 96.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 63*

**Composition by Extension & Reason:**
- `.cmake`: 35x Excluded (Unsupported Extension: '.cmake')
- `.patch`: 4x Excluded (Unsupported Extension: '.patch')
- `.gz`: 4x Excluded (Explicitly Denied Extension: '.gz')
- `.orc`: 4x Excluded (Unsupported Extension: '.orc')
- `.parquet`: 4x Excluded (Unsupported Extension: '.parquet')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 35 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.pxd`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyx`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.feather`: 1x Excluded (Unsupported Extension: '.feather')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.8 | 24.8 | 22.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 49.4 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.4 | 18.9 | 9.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.2 | 1.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 68.2 | 95.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 85.6 | 0.4 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3290 | 119 | 34 | `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` |
| cleanup | 144 | 30 | 1 | `pyarrow-23.0.1/pyarrow/tests/test_flight.py` |
| guards | 10623 | 169 | 96 | `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` |
| danger | 1783 | 132 | 25 | `pyarrow-23.0.1/pyarrow/table.pxi` |
| concurrency | 248 | 58 | 3 | `pyarrow-23.0.1/pyarrow/tests/test_flight.py` |
| connectivity | 5354 | 163 | 70 | `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` |
| io | 454 | 57 | 6 | `pyarrow-23.0.1/pyarrow/tests/test_io.py` |
| crypto | 1 | 1 | 0 | `pyarrow-23.0.1/pyarrow/_fs.pyx` |
| ipc | 61 | 13 | 0 | `pyarrow-23.0.1/pyarrow/tests/test_gdb.py` |
| time | 250 | 28 | 1 | `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` |
| serialization | 2 | 2 | 0 | `pyarrow-23.0.1/pyarrow/pandas_compat.py` |
| regex | 22 | 11 | 0 | `pyarrow-23.0.1/pyarrow/tests/test_gdb.py` |
| events | 124 | 19 | 0 | `pyarrow-23.0.1/pyarrow/_fs.pyx` |
| tests | 5256 | 63 | 58 | `pyarrow-23.0.1/pyarrow/tests/test_array.py` |
| docs | 2532 | 127 | 22 | `pyarrow-23.0.1/pyarrow/types.pxi` |
| debt | 553 | 97 | 7 | `pyarrow-23.0.1/pyarrow/tensor.pxi` |
| mutation | 40978 | 179 | 419 | `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` |
| dead_code | 2675 | 114 | 25 | `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` |
| credential | 5 | 2 | 0 | `pyarrow-23.0.1/pyarrow/tests/test_fs.py` |
| threat | 1330 | 105 | 17 | `pyarrow-23.0.1/pyarrow/_flight.pyx` |
| ml_ai | 138 | 47 | 2 | `pyarrow-23.0.1/pyarrow/tests/test_table.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.4575**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyarrow-23.0.1/pyarrow/tests/test_io.py` (Hits: 85)
- `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` (Hits: 33)
- `pyarrow-23.0.1/setup.py` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.h** (`pyarrow-23.0.1/pyarrow/src/arrow/python/common.h`) — 26 inbound connections
2. **memory.pxi** (`pyarrow-23.0.1/pyarrow/memory.pxi`) — 25 inbound connections
3. **util.py** (`pyarrow-23.0.1/pyarrow/util.py`) — 21 inbound connections
4. **visibility.h** (`pyarrow-23.0.1/pyarrow/src/arrow/python/visibility.h`) — 21 inbound connections
5. **compute.py** (`pyarrow-23.0.1/pyarrow/compute.py`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **arrow_to_pandas.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) — 37 outbound dependencies
2. **numpy_to_arrow.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/numpy_to_arrow.cc`) — 37 outbound dependencies
3. **python_to_arrow.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc`) — 37 outbound dependencies
4. **test_dataset.py** (`pyarrow-23.0.1/pyarrow/tests/test_dataset.py`) — 29 outbound dependencies
5. **test_csv.py** (`pyarrow-23.0.1/pyarrow/tests/test_csv.py`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `GetPandasWriterType` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) -> Impact: **228.5** | LOC: 170
- `__init__` (@ `pyarrow-23.0.1/pyarrow/_s3fs.pyx`) -> Impact: **222.1** | LOC: 142
- `_perform_join` (@ `pyarrow-23.0.1/pyarrow/acero.py`) -> Impact: **185.6** | LOC: 179
- `array` (@ `pyarrow-23.0.1/pyarrow/array.pxi`) -> Impact: **173.8** | LOC: 251
- `write_dataset` (@ `pyarrow-23.0.1/pyarrow/dataset.py`) -> Impact: **130.5** | LOC: 195
- `arrays` (@ `pyarrow-23.0.1/pyarrow/tests/strategies.py`) -> Impact: **92.9** | LOC: 114
- `VisitSequenceGeneric` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/iterators.h`) -> Impact: **89.8** | LOC: 156
  * *Intent:* // Visit the Python sequence, calling the given callable on each element. If // the callable returns a non-OK status, iteration stops and the status i...
- `Visit` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/inference.cc`) -> Impact: **86.6** | LOC: 69
  * *Intent:* /// \param[in] obj a Python object in the sequence /// \param[out] keep_going if sufficient information has been gathered to /// attempt to begin conv...
- `__init__` (@ `pyarrow-23.0.1/pyarrow/parquet/core.py`) -> Impact: **85.0** | LOC: 91
- `dataframe_to_arrays` (@ `pyarrow-23.0.1/pyarrow/pandas_compat.py`) -> Impact: **79.0** | LOC: 98

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyarrow-23.0.1/pyarrow/tests` | 58 | 29540.86 | 25.22% | 0.0% |
| `pyarrow-23.0.1/pyarrow` | 73 | 26117.88 | 34.18% | 33.26% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python` | 57 | 6529.02 | 15.84% | 30.85% |
| `pyarrow-23.0.1/pyarrow/tests/parquet` | 14 | 3806.96 | 24.65% | 0.0% |
| `pyarrow-23.0.1/pyarrow/vendored` | 3 | 1292.24 | 53.31% | 38.44% |
| `pyarrow-23.0.1/pyarrow/parquet` | 3 | 1056.56 | 15.53% | 6.91% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored` | 2 | 851.36 | 35.28% | 0.0% |
| `pyarrow-23.0.1/pyarrow/interchange` | 5 | 721.32 | 31.67% | 9.91% |
| `pyarrow-23.0.1/pyarrow/includes` | 15 | 434.12 | 0.48% | 43.94% |
| `pyarrow-23.0.1` | 5 | 358.64 | 11.24% | 11.47% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyarrow-23.0.1/pyarrow/__init__.pxd` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_fs.pxd` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/builder.pxi` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/tensor.pxi` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/flight.cc` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyarrow-23.0.1/pyarrow/_azurefs.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_csv.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_dataset_parquet.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_gcsfs.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_json.pyx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` -> **279** Orphaned Functions | **2** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_array.py` -> **186** Orphaned Functions | **5** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` -> **179** Orphaned Functions | **0** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_compute.py` -> **150** Orphaned Functions | **6** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_table.py` -> **149** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `pyarrow-23.0.1/pyarrow/tests/test_fs.py` -> **85.6275%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1501` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyarrow-23.0.1/pyarrow/error.pxi` (PYTHON) -> Cumulative Risk: **808.01**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 162.6 | **LOC:** 275 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9923%), Concurrency (98.5546%), Tech Debt (97.4144%)
- **Heaviest Functions:** `convert_status` (Impact: 29.6), `__exit__` (Impact: 19.2), `__cinit__` (Impact: 8.2)

### 2. `pyarrow-23.0.1/pyarrow/vendored/version.py` (PYTHON) -> Cumulative Risk: **764.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 427.98 | **LOC:** 546 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.4867%), Documentation (96.5909%)
- **Heaviest Functions:** `_cmpkey` (Impact: 42.5), `__init__` (Impact: 34.5), `_parse_letter_version` (Impact: 17.2)

### 3. `pyarrow-23.0.1/pyarrow/public-api.pxi` (PYTHON) -> Cumulative Risk: **718.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 262.56 | **LOC:** 444 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8359%)
- **Heaviest Functions:** `pyarrow_wrap_data_type` (Impact: 47.5), `pyarrow_wrap_scalar` (Impact: 8.1), `pyarrow_wrap_chunked_array` (Impact: 4.9)

### 4. `pyarrow-23.0.1/pyarrow/src/arrow/python/datetime.cc` (CPP) -> Cumulative Risk: **684.97**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 412.28 | **LOC:** 666 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Safety Score (90.2727%)
- **Heaviest Functions:** `TzinfoToString` (Impact: 31.2), `PyTime_convert_int` (Impact: 30.5), `StringToTzinfo` (Impact: 21.7)

### 5. `pyarrow-23.0.1/pyarrow/src/arrow/python/inference.cc` (CPP) -> Cumulative Risk: **684.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 564.32 | **LOC:** 809 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9647%), Documentation (95.122%), Tech Debt (94.4424%)
- **Heaviest Functions:** `Visit` (Impact: 86.6), `GetType` (Impact: 78.4), `DatetimeUnitName` (Impact: 25.7)

### 6. `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` (CPP) -> Cumulative Risk: **684.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 121.62 | **LOC:** 247 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8294%), Cognitive Load (91.7665%)
- **Heaviest Functions:** `MapPyError` (Impact: 23.8), `PyBuffer::Init` (Impact: 4.8), `IsPyError` (Impact: 4.6)

### 7. `pyarrow-23.0.1/pyarrow/ipc.pxi` (PYTHON) -> Cumulative Risk: **676.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 650.74 | **LOC:** 1505 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.996%), Tech Debt (99.7845%), Safety Score (86.3259%)
- **Heaviest Functions:** `compression` (Impact: 21.6), `from_stream` (Impact: 14.2), `read_record_batch` (Impact: 12.1)

### 8. `pyarrow-23.0.1/pyarrow/pandas-shim.pxi` (PYTHON) -> Cumulative Risk: **664.71**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 179.0 | **LOC:** 284 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9896%), State Flux (99.6953%), Documentation (98.0392%)
- **Heaviest Functions:** `_import_pandas` (Impact: 16.7), `_check_import` (Impact: 9.3), `uses_string_dtype` (Impact: 6.1)

### 9. `pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc` (CPP) -> Cumulative Risk: **661.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 291.92 | **LOC:** 505 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.7478%), Verification (80.0%)
- **Heaviest Functions:** `UnboxIntegerAsInt64` (Impact: 50.3), `CIntFromPythonImpl` (Impact: 21.7), `CIntFromPythonImpl` (Impact: 17.6)

### 10. `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored/pythoncapi_compat.h` (CPP) -> Cumulative Risk: **656.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 850.36 | **LOC:** 1520 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.912%), Safety Score (81.1471%)
- **Heaviest Functions:** `PyObject_Vectorcall` (Impact: 43.7), `PyDict_Pop` (Impact: 28.1), `PyTime_PerfCounter` (Impact: 26.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3367.12 | **LOC:** 5942 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.4353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_partition_discovery` (Impact: 51.7)
  * `test_construct_from_invalid_sources_raise` (Impact: 31.5)
  * `test_make_fragment_with_size` (Impact: 16.8)
    * *Intent:* """ Test passing file_size to make_fragment. Not all FS implementations make use of the file size (b...
  * `test_partitioning` (Impact: 16.5)
  * `test_filesystem_dataset` (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 328 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 1955
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 1216`, `args: 248`, `func_start: 236`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1299`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 21`, `unreferenced_by_name: 179`
* *Architecture:* `io: 33`, `api: 212`, `concurrency: 4`, `import: 46`
* *Defense:* `safety: 690`, `doc: 8`, `test: 460`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` .test_fs, contextlib, datetime, itertools, numpy, os, pandas, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3302.82 | **LOC:** 5320 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1157%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_pandas_roundtrip` (Impact: 34.5)
  * `_check_array_roundtrip` (Impact: 16.8)
  * `check` (Impact: 14.9)
  * `test_dictionary_with_pandas` (Impact: 14.5)
    * *Intent:* # ---------------------------------------------------------------------- # DictionaryArray tests
  * `test_from_numpy_large` (Impact: 14.0)
    * *Intent:* # Exercise rechunking + nulls target_size = 3 * 1024**3 # 4GB dt = np.dtype([('x', np.float64), ('y'...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 277 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1930
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 1009`, `args: 311`, `func_start: 311`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 1376`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 279`
* *Architecture:* `io: 7`, `api: 299`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 382`, `doc: 11`, `test: 394`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .pandas_examples, collections, datetime, decimal, gc, hypothesis, hypothesis.strategies, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_compute.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2690.9 | **LOC:** 4102 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_partition_nth` (Impact: 39.0)
  * `test_cumulative_max` (Impact: 30.4)
    * *Intent:* # Exact tests (e.g., integral types) start_int = int(start) starts = [None, start_int, pa.scalar(sta...
  * `test_cumulative_min` (Impact: 30.4)
    * *Intent:* # Exact tests (e.g., integral types) start_int = int(start) starts = [None, start_int, pa.scalar(sta...
  * `test_cumulative_sum` (Impact: 30.2)
    * *Intent:* # Exact tests (e.g., integral types) start_int = int(start) starts = [None, start_int, pa.scalar(sta...
  * `test_cumulative_prod` (Impact: 30.2)
    * *Intent:* # Exact tests (e.g., integral types) start_int = int(start) starts = [None, start_int, pa.scalar(sta...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 1618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 1088`, `args: 180`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1004`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 6`, `unreferenced_by_name: 150`
* *Architecture:* `io: 2`, `api: 168`, `import: 21`
* *Defense:* `safety: 581`, `doc: 10`, `test: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections, datetime, decimal, functools, inspect, itertools, math, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2106.74 | **LOC:** 4401 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_numpy_binary_overflow_to_chunked` (Impact: 29.2)
    * *Intent:* # ARROW-3762, ARROW-5966, GH-35289 # 2^31 + 1 bytes values = [b'x'] unicode_values = ['x'] # Make 10...
  * `_check_cast_case` (Impact: 17.1)
  * `test_array_pickle_protocol5` (Impact: 16.8)
    * *Intent:* # Test zero-copy pickling with protocol 5 (PEP 574) array = pa.array(data, type=typ) addresses = [bu...
  * `test_map_from_arrays` (Impact: 12.9)
  * `test_array_slice_negative_step` (Impact: 9.6)
    * *Intent:* # ARROW-2714 values = list(range(20)) arr = pa.array(values) chunked_arr = pa.chunked_array([arr]) c...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 142 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 1204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 1351`, `args: 204`, `func_start: 204`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 1`, `state_mutation: 920`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 5`, `unreferenced_by_name: 186`
* *Architecture:* `io: 12`, `api: 197`, `import: 22`
* *Defense:* `safety: 572`, `doc: 8`, `test: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections.abc, datetime, dateutil.relativedelta, decimal, gc, hypothesis, hypothesis.strategies, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/table.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2085.6 | **LOC:** 6628 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4954%), Tech Debt (55.3706%)
**Top Internal Functions/Classes:**
  * `table` (Impact: 69.2)
    * *Intent:* """ Create a pyarrow.Table from a Python data structure or sequence of arrays. Parameters ----------...
  * `record_batch` (Impact: 51.2)
    * *Intent:* """ Create a pyarrow.RecordBatch from another Python data structure or sequence of arrays. Parameter...
  * `_schema_from_arrays` (Impact: 38.1)
  * `_from_pylist` (Impact: 33.2)
    * *Intent:* """ Construct a Table/RecordBatch from list of rows / dictionaries. Parameters ---------- cls : Clas...
  * `aggregate` (Impact: 28.3)
    * *Intent:* """ Perform an aggregation over the grouped columns of the table. Parameters ---------- aggregations...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 481`, `args: 178`, `func_start: 178`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 288`, `duplicate_logic: 6`, `unreferenced_by_name: 27`
* *Architecture:* `api: 118`, `import: 9`
* *Defense:* `safety: 60`, `doc: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cython, numpy, pandas, pyarrow, pyarrow.compute, pyarrow.interchange.dataframe, pyarrow.pandas_compat, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/array.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2082.22 | **LOC:** 5033 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1836%), Tech Debt (88.666%)
**Top Internal Functions/Classes:**
  * `array` (Impact: 173.8)
  * `from_arrays` (Impact: 78.6)
  * `from_arrays` (Impact: 34.7)
  * `from_buffers` (Impact: 32.0)
  * `_array_like_to_pandas` (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 739
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 654`, `args: 159`, `func_start: 159`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 285`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 51`
* *Architecture:* `api: 111`, `import: 6`
* *Defense:* `safety: 50`, `doc: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, cython, numpy, os, pandas, pyarrow, pyarrow.pandas_compat, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_dataset.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1810.78 | **LOC:** 4229 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.9002%), Tech Debt (67.0678%)
**Top Internal Functions/Classes:**
  * `_populate_builder` (Impact: 52.3)
  * `from_batches` (Impact: 36.4)
  * `__init__` (Impact: 31.9)
  * `_filesystemdataset_write` (Impact: 31.1)
  * `__init__` (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 425`, `args: 208`, `func_start: 208`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 310`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 103`, `import: 9`
* *Defense:* `safety: 45`, `doc: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` codecs, collections, issue, pyarrow, pyarrow._compute, pyarrow._dataset_orc, pyarrow._dataset_parquet, pyarrow.compute...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1735.82 | **LOC:** 2660 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.3048%), Tech Debt (29.7881%)
**Top Internal Functions/Classes:**
  * `GetPandasWriterType` (Impact: 228.5)
  * `ListTypeSupported` (Impact: 57.7)
  * `MakeWriter` (Impact: 48.8)
  * `ConvertListsLike` (Impact: 31.9)
  * `CopyInto` (Impact: 31.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 165 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 509`, `args: 323`, `func_start: 130`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 208`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 18`, `concurrency: 3`, `import: 37`
* *Defense:* `safety: 95`, `doc: 7`, `sync_locks: 18`, `immutability_locks: 213`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` array.h, buffer.h, api.h, datum.h, arrow_to_pandas.h, arrow_to_python_internal.h, common.h, datetime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_table.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1714.08 | **LOC:** 4067 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_table_non_cpu` (Impact: 22.6)
  * `test_recordbatch_non_cpu` (Impact: 17.7)
  * `test_table_group_by` (Impact: 13.7)
  * `test_chunked_array_equals` (Impact: 11.3)
  * `test_table_basics` (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 1108`, `args: 177`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 744`, `duplicate_logic: 2`, `unreferenced_by_name: 149`
* *Architecture:* `io: 2`, `api: 171`, `import: 23`
* *Defense:* `safety: 496`, `doc: 13`, `test: 415`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections, collections.abc, numpy, pandas, pandas.testing, pyarrow, pyarrow.compute, pyarrow.interchange...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/types.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1682.7 | **LOC:** 6104 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.7789%), Tech Debt (98.5723%)
**Top Internal Functions/Classes:**
  * `field` (Impact: 24.2)
    * *Intent:* # ----------------------------------------------------------- # Type factory functions """ Create a ...
  * `__init__` (Impact: 21.3)
  * `schema` (Impact: 20.1)
    * *Intent:* """ Construct pyarrow.Schema from collection of fields. Parameters ---------- fields : iterable of F...
  * `union` (Impact: 19.9)
    * *Intent:* """ Create UnionType from child fields. A union is a nested type where each logical value is taken f...
  * `fixed_shape_tensor` (Impact: 18.4)
    * *Intent:* """ Create instance of fixed shape tensor extension type with shape and optional names of tensor dim...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 103 instances
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 788`, `args: 315`, `func_start: 315`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 200`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 30`
* *Architecture:* `io: 2`, `api: 156`, `import: 10`
* *Defense:* `safety: 57`, `doc: 217`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` atexit, collections.abc, cython, datetime, decimal, json, numpy, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_flight.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1571.12 | **LOC:** 3296 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.9507%), Tech Debt (72.3035%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 48.6)
  * `__init__` (Impact: 39.5)
    * *Intent:* """Create a FlightEndpoint from a ticket and list of locations. Parameters ---------- ticket : Ticke...
  * `init` (Impact: 37.6)
  * `_data_stream_next` (Impact: 37.3)
    * *Intent:* """Callback for implementing FlightDataStream in Python."""
  * `__init__` (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 579`, `args: 226`, `func_start: 226`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 234`, `dead_code: 2`, `planned_debt: 10`, `duplicate_logic: 14`
* *Architecture:* `api: 134`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 93`, `doc: 190`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009644
  * `Imports (Out-Degree: 0):` asyncio, collections, enum, pyarrow.ipc, pyarrow.lib, re, time, warnings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_flight.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1537.04 | **LOC:** 2790 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `exchange_echo` (Impact: 21.0)
    * *Intent:* """Run a simple echo server."""
  * `do_exchange` (Impact: 17.9)
  * `do_put` (Impact: 17.8)
  * `start_call` (Impact: 15.2)
  * `do_action` (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 888`, `args: 225`, `func_start: 204`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 358`, `dead_code: 2`, `duplicate_logic: 17`, `unreferenced_by_name: 82`
* *Architecture:* `io: 5`, `api: 230`, `concurrency: 16`, `import: 22`
* *Defense:* `safety: 215`, `doc: 115`, `test: 167`, `sync_locks: 4`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ast, base64, datetime, itertools, json, numpy, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/io.pxi` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1441.18 | **LOC:** 2913 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4025%), Tech Debt (29.0784%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 38.5)
  * `download` (Impact: 32.9)
    * *Intent:* """ Read this file completely to a local path or destination stream. This method first seeks to the ...
  * `output_stream` (Impact: 28.4)
    * *Intent:* """ Create an Arrow output stream. Parameters ---------- source : str, Path, buffer, file-like objec...
  * `input_stream` (Impact: 28.2)
    * *Intent:* """ Create an Arrow input stream. Parameters ---------- source : str, Path, buffer, or file-like obj...
  * `upload` (Impact: 24.9)
    * *Intent:* """ Write from a source stream to this file. Parameters ---------- stream : file-like object Source ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 155 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 354`, `args: 155`, `func_start: 155`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 259`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 107`, `concurrency: 3`, `import: 10`
* *Defense:* `safety: 59`, `doc: 87`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codecs, gzip, io, pickle, pyarrow, pyarrow.util, queue, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/pandas_compat.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1394.14 | **LOC:** 1296 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.5212%), Tech Debt (11.0874%)
**Top Internal Functions/Classes:**
  * `dataframe_to_arrays` (Impact: 79.0)
  * `_get_extension_dtypes` (Impact: 70.2)
    * *Intent:* """ Based on the stored column pandas metadata and the extension types in the arrow schema, infer wh...
  * `construct_metadata` (Impact: 53.4)
  * `_reconstruct_columns_from_metadata` (Impact: 37.2)
    * *Intent:* """Construct a pandas MultiIndex from `columns` and column index metadata in `column_indexes`. Param...
  * `_add_any_metadata` (Impact: 34.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 239 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 181`, `args: 37`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 260`, `dead_code: 5`, `fragile_debt: 2`
* *Architecture:* `api: 15`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 59`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.398
  * `Choke Point (Betweenness):` 0.000286 | `Ripple Effect (Closeness):` 0.056259
  * `Imports (Out-Degree: 1):` ast, collections.abc, concurrent, concurrent.futures.thread, copy, decimal, itertools, json...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_csv.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1327.86 | **LOC:** 2068 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1336%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parse_options` (Impact: 29.8)
  * `test_row_number_offset_in_errors` (Impact: 24.9)
    * *Intent:* # Row numbers are only correctly counted in serial reads def format_msg(msg_format, row, *args): if ...
  * `test_read_options` (Impact: 21.0)
  * `test_cancellation` (Impact: 13.1)
  * `make_random_csv` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 125 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 751
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 453`, `args: 107`, `func_start: 102`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 501`, `fragile_debt: 13`, `duplicate_logic: 4`, `unreferenced_by_name: 56`
* *Architecture:* `io: 5`, `api: 110`, `concurrency: 8`, `import: 24`
* *Defense:* `safety: 217`, `doc: 8`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` abc, bz2, datetime, decimal, gc, gzip, io, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_compute.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1325.18 | **LOC:** 3480 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.9676%), Tech Debt (24.2315%)
**Top Internal Functions/Classes:**
  * `_register_user_defined_function` (Impact: 35.6)
  * `cast` (Impact: 26.2)
    * *Intent:* """ Explicitly set or change the expression's data type. This creates a new expression equivalent to...
  * `_set_options` (Impact: 22.0)
  * `_ensure_field_ref` (Impact: 21.0)
  * `_pack_compute_args` (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 518`, `args: 245`, `func_start: 244`, `class_start: 129`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 156`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 123`, `import: 9`
* *Defense:* `safety: 63`, `doc: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections, inspect, numpy, pyarrow, pyarrow.compute, pyarrow.lib, pyarrow.substrait, pyarrow.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1279.3 | **LOC:** 2624 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.1117%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_sequence_timestamp_with_timezone` (Impact: 18.8)
  * `test_sequence_numpy_double` (Impact: 16.7)
  * `test_array_accepts_pyarrow_scalar_errors` (Impact: 14.4)
  * `test_sequence_time_with_timezone` (Impact: 12.8)
  * `expected_datetime_value` (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 675
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 993`, `args: 149`, `func_start: 149`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 493`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 132`
* *Architecture:* `api: 145`, `import: 21`
* *Defense:* `safety: 456`, `doc: 1`, `test: 284`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections, datetime, decimal, gc, hypothesis, itertools, math, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_io.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1136.54 | **LOC:** 2213 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.6584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_non_cpu_buffer` (Impact: 20.4)
  * `test_compression_level` (Impact: 13.7)
  * `test_python_file_get_stream` (Impact: 12.4)
  * `check_large_seeks` (Impact: 8.0)
  * `check_transcoding` (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 584
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 840`, `args: 138`, `func_start: 138`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 408`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 85`, `api: 139`, `import: 21`
* *Defense:* `safety: 426`, `doc: 1`, `test: 230`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005626
  * `Imports (Out-Degree: 1):` bz2, contextlib, gc, gzip, io, itertools, math, numpy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_parquet.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1092.26 | **LOC:** 2422 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9636%), Tech Debt (79.7863%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 73.3)
  * `from_ordering` (Impact: 36.5)
    * *Intent:* """ Create a tuple of SortingColumn objects from the same arguments as :class:`pyarrow.compute.SortO...
  * `iter_batches` (Impact: 22.3)
  * `to_ordering` (Impact: 17.6)
    * *Intent:* """ Convert a tuple of SortingColumn objects to the same format as :class:`pyarrow.compute.SortOptio...
  * `__cinit__` (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 425`, `args: 179`, `func_start: 179`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 121`, `dead_code: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 1`, `api: 115`, `import: 4`
* *Defense:* `safety: 34`, `doc: 119`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections.abc, pyarrow, pyarrow.lib, pyarrow.parquet, textwrap, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/parquet/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1033.44 | **LOC:** 2455 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.575%), Tech Debt (20.7231%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 85.0)
  * `__init__` (Impact: 51.6)
  * `write_to_dataset` (Impact: 50.5)
  * `read_table` (Impact: 41.6)
  * `read` (Impact: 37.5)
    * *Intent:* """ Read (multiple) Parquet files as a single pyarrow.Table. Parameters ---------- columns : List[st...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 158`, `args: 52`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 151`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 40`, `import: 16`
* *Defense:* `safety: 28`, `doc: 44`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.999
  * `Choke Point (Betweenness):` 0.000197 | `Ripple Effect (Closeness):` 0.004219
  * `Imports (Out-Degree: 5):` collections, contextlib, functools, inspect, json, operator, os, pandas...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_extension_type.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1031.22 | **LOC:** 1970 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tensor_array_from_numpy` (Impact: 28.5)
  * `test_ext_scalar_from_array` (Impact: 15.8)
  * `test_json` (Impact: 9.4)
  * `test_ext_type_as_py` (Impact: 8.5)
  * `test_extension_to_pandas_storage_type` (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 764`, `args: 126`, `func_start: 122`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 446`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `io: 4`, `api: 97`, `import: 25`
* *Defense:* `safety: 387`, `doc: 1`, `test: 132`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.621
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.004219
  * `Imports (Out-Degree: 3):` .test_cython, base64, contextlib, extensions, numpy, numpy.lib.stride_tricks, os, pandas...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_fs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 911.54 | **LOC:** 2257 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.8702%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_get_file_info_with_selector` (Impact: 23.5)
  * `test_azurefs_options` (Impact: 14.4)
  * `get_file_info` (Impact: 12.9)
  * `test_get_file_info` (Impact: 11.5)
  * `test_s3fs_limited_permissions_create_bucket` (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 727`, `args: 122`, `func_start: 112`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 1`, `state_mutation: 283`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `io: 17`, `api: 113`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 381`, `doc: 4`, `test: 237`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.365
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.004219
  * `Imports (Out-Degree: 5):` datetime, fsspec.implementations.local, fsspec.implementations.memory, gzip, huggingface_hub, os, pathlib, pyarrow...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_csv.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 855.06 | **LOC:** 1559 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.9162%), Tech Debt (81.2416%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 55.8)
  * `__init__` (Impact: 24.9)
  * `equals` (Impact: 23.9)
    * *Intent:* """ Parameters ---------- other : pyarrow.csv.ConvertOptions Returns ------- bool """
  * `__init__` (Impact: 21.9)
  * `__init__` (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 188`, `args: 107`, `func_start: 107`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 114`, `duplicate_logic: 10`
* *Architecture:* `api: 74`, `import: 3`
* *Defense:* `safety: 15`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, collections.abc, io, pyarrow, pyarrow.lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/vendored/docscrape.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 853.74 | **LOC:** 717 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.3891%), Tech Debt (15.8459%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 63.5)
  * `_parse_see_also` (Impact: 37.3)
    * *Intent:* """ func_name : Descriptive text continued text another_func_name : Descriptive text func_name1, fun...
  * `get_doc_object` (Impact: 25.6)
  * `_parse` (Impact: 24.5)
  * `_str_see_also` (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 159`, `args: 54`, `func_start: 54`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 135`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 26`, `import: 10`
* *Defense:* `safety: 15`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, collections.abc, copy, inspect, pydoc, re, sphinx.ext.autodoc, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored/pythoncapi_compat.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 850.36 | **LOC:** 1520 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5669%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyObject_Vectorcall` (Impact: 43.7)
    * *Intent:* #endif // gh-105922 added PyObject_Vectorcall() to Python 3.9.0a4 #if PY_VERSION_HEX < 0x030900A4
  * `PyDict_Pop` (Impact: 28.1)
    * *Intent:* #endif // gh-111262 added PyDict_Pop() and PyDict_PopString() to Python 3.13.0a2 #if PY_VERSION_HEX ...
  * `PyTime_PerfCounter` (Impact: 26.0)
  * `PyUnicode_EqualToUTF8AndSize` (Impact: 25.1)
    * *Intent:* #endif // gh-110289 added PyUnicode_EqualToUTF8() and PyUnicode_EqualToUTF8AndSize() // to Python 3....
  * `PyDict_SetDefaultRef` (Impact: 21.9)
    * *Intent:* #endif // gh-114329 added PyList_GetItemRef() to Python 3.13.0a4 #if PY_VERSION_HEX < 0x030D00A4
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 266`, `args: 169`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 99`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.424
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016878
  * `Imports (Out-Degree: 0):` Python.h, frameobject.h
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

- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 0.222** (Bridge: 0.0022 * Flux: 100.0%)
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.h` -> **Severity: 0.121** (Bridge: 0.0012 * Flux: 97.1873%)
- `pyarrow-23.0.1/pyarrow/dataset.py` -> **Severity: 0.096** (Bridge: 0.001 * Flux: 99.9998%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 100.0%)
- `pyarrow-23.0.1/pyarrow/parquet/core.py` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyarrow-23.0.1/pyarrow/util.py` -> **Severity: 8.339** (Embedded: 0.1023 * Error Risk: 81.5235%)
- `pyarrow-23.0.1/pyarrow/compute.py` -> **Severity: 7.684** (Embedded: 0.0784 * Error Risk: 98.016%)
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.h` -> **Severity: 7.664** (Embedded: 0.1161 * Error Risk: 65.9948%)
- `pyarrow-23.0.1/pyarrow/memory.pxi` -> **Severity: 7.144** (Embedded: 0.1276 * Error Risk: 55.9714%)
- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 6.943** (Embedded: 0.0825 * Error Risk: 84.1391%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyarrow-23.0.1/pyarrow/src/arrow/python/datetime.h` -> **Severity: 4199.9** (Blast Radius: 41.999 * Doc Risk: 100.0%)
- `pyarrow-23.0.1/pyarrow/util.py` -> **Severity: 2353.5** (Blast Radius: 31.38 * Doc Risk: 75.0%)
- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 2256.516** (Blast Radius: 23.078 * Doc Risk: 97.7778%)
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.h` -> **Severity: 2021.856** (Blast Radius: 21.385 * Doc Risk: 94.5455%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 1586.403** (Blast Radius: 21.398 * Doc Risk: 74.1379%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
