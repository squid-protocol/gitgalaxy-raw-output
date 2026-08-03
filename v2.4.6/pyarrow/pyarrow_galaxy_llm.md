# ARCHITECTURAL_BRIEF: pyarrow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyarrow` |
| **Timestamp** | `2026-08-03T21:23:37.848458+00:00` |
| **Scan Duration** | `2.06s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 228 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 301 |
| Analyzed Artifacts (Scanned) | 235 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 66 |
| Total LOC | 85483 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6397 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1841 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0084 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 171 | 77328 | 72.8% |
| CPP | 57 | 8155 | 24.3% |
| PLAINTEXT | 5 | 0 | 2.1% |
| MARKDOWN | 2 | 0 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.589`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 144 | 61.3% |
| file_cluster_13 | 61 | 26.0% |
| file_cluster_0 | 18 | 7.7% |
| file_cluster_16 | 3 | 1.3% |
| file_cluster_4 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 66*

**Composition by Extension & Reason:**
- `.cmake`: 35x Excluded (Unsupported Extension: '.cmake')
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.patch`: 4x Excluded (Unsupported Extension: '.patch')
- `.gz`: 4x Excluded (Explicitly Denied Extension: '.gz')
- `.orc`: 4x Excluded (Unsupported Extension: '.orc')
- `.parquet`: 4x Excluded (Unsupported Extension: '.parquet')
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.pxd`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyx`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.feather`: 1x Excluded (Unsupported Extension: '.feather')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 18.6 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.6 | 10.6 | 2.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.3 | 1.9 | 0.0 |
| API Exposure | 0.0 | 13.9 | 3.3 | 2.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.8 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.9 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 57.4 | 99.6 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 46.2 | 20.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 9.6 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 85.6 | 0.4 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyarrow-23.0.1/pyarrow/tests/test_io.py` (Hits: 85)
- `pyarrow-23.0.1/setup.py` (Hits: 41)
- `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` (Hits: 33)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **memory.pxi** (`pyarrow-23.0.1/pyarrow/memory.pxi`) — 25 inbound connections
2. **util.py** (`pyarrow-23.0.1/pyarrow/util.py`) — 19 inbound connections
3. **compute.py** (`pyarrow-23.0.1/pyarrow/compute.py`) — 17 inbound connections
4. **fs.py** (`pyarrow-23.0.1/pyarrow/fs.py`) — 14 inbound connections
5. **pandas_compat.py** (`pyarrow-23.0.1/pyarrow/pandas_compat.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **arrow_to_pandas.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) — 37 outbound dependencies
2. **numpy_to_arrow.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/numpy_to_arrow.cc`) — 37 outbound dependencies
3. **python_to_arrow.cc** (`pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc`) — 37 outbound dependencies
4. **test_dataset.py** (`pyarrow-23.0.1/pyarrow/tests/test_dataset.py`) — 29 outbound dependencies
5. **test_csv.py** (`pyarrow-23.0.1/pyarrow/tests/test_csv.py`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__cinit__` (@ `pyarrow-23.0.1/pyarrow/io.pxi`) -> Impact: **2187.8** | LOC: 1197
- `test_array_diff` (@ `pyarrow-23.0.1/pyarrow/tests/test_array.py`) -> Impact: **1866.3** | LOC: 3741
- `array` (@ `pyarrow-23.0.1/pyarrow/array.pxi`) -> Impact: **1155.9** | LOC: 151
- `__repr__` (@ `pyarrow-23.0.1/pyarrow/scalar.pxi`) -> Impact: **1116.1** | LOC: 498
  * *Intent:* """ Return this value as a Python Decimal. Parameters ---------- maps_as_pydicts : str, optional, default `None` Valid values are `None`, 'lossy', or ...
- `test_parse_options` (@ `pyarrow-23.0.1/pyarrow/tests/test_csv.py`) -> Impact: **964.1** | LOC: 1822
- `strtobool` (@ `pyarrow-23.0.1/setup.py`) -> Impact: **865.7** | LOC: 339
  * *Intent:* """Convert a string representation of truth to true (1) or false (0). True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values are 'n', 'n...
- `__init__` (@ `pyarrow-23.0.1/pyarrow/_s3fs.pyx`) -> Impact: **864.4** | LOC: 142
- `_resolve_filesystem_and_path` (@ `pyarrow-23.0.1/pyarrow/fs.py`) -> Impact: **731.8** | LOC: 235
- `__getbuffer__` (@ `pyarrow-23.0.1/pyarrow/tensor.pxi`) -> Impact: **673.8** | LOC: 736
- `arrays` (@ `pyarrow-23.0.1/pyarrow/tests/strategies.py`) -> Impact: **631.8** | LOC: 114

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__init__` (@ `pyarrow-23.0.1/pyarrow/_compute.pyx`) -> **O(2^N) [Recursive]**
- `cast` (@ `pyarrow-23.0.1/pyarrow/_compute.pyx`) -> **O(2^N) [Recursive]**
- `invalid_row_handler` (@ `pyarrow-23.0.1/pyarrow/_csv.pyx`) -> **O(2^N) [Recursive]**
- `to_numba` (@ `pyarrow-23.0.1/pyarrow/_cuda.pyx`) -> **O(2^N) [Recursive]**
- `discover` (@ `pyarrow-23.0.1/pyarrow/_dataset.pyx`) -> **O(2^N) [Recursive]**
- `make_fragment` (@ `pyarrow-23.0.1/pyarrow/_dataset_parquet.pyx`) -> **O(2^N) [Recursive]**
  * *Intent:* ----------
- `make_write_options` (@ `pyarrow-23.0.1/pyarrow/_dataset_parquet.pyx`) -> **O(2^N) [Recursive]**
  * *Intent:* # Read options getter/setter works with strings so setting # the private property which uses the C Type parquet_read_options._coerce_int96_timestamp_u...
- `authenticate` (@ `pyarrow-23.0.1/pyarrow/_flight.pyx`) -> **O(2^N) [Recursive]**
- `custom_kms_conf` (@ `pyarrow-23.0.1/pyarrow/_parquet_encryption.pyx`) -> **O(2^N) [Recursive]**
- `file_encryption_properties` (@ `pyarrow-23.0.1/pyarrow/_parquet_encryption.pyx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `strtobool` (@ `pyarrow-23.0.1/setup.py`) -> DB Complexity: **127**
  * *Intent:* """Convert a string representation of truth to true (1) or false (0). True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values are 'n', 'n...
- `ConvertListsLike` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) -> DB Complexity: **123**
- `TestSession` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/gdb.cc`) -> DB Complexity: **102**
- `test_cython_api` (@ `pyarrow-23.0.1/pyarrow/tests/test_cython.py`) -> DB Complexity: **50**
- `VisitSequenceGeneric` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/iterators.h`) -> DB Complexity: **45**
- `__cinit__` (@ `pyarrow-23.0.1/pyarrow/io.pxi`) -> DB Complexity: **43**
- `Visit` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/inference.cc`) -> DB Complexity: **32**
- `MakeBlock1D` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) -> DB Complexity: **31**
- `download_tzdata_on_windows` (@ `pyarrow-23.0.1/pyarrow/util.py`) -> DB Complexity: **30**
- `test_array_diff` (@ `pyarrow-23.0.1/pyarrow/tests/test_array.py`) -> DB Complexity: **28**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyarrow-23.0.1/pyarrow` | 72 | 43659.36 | 19.16% | 47.54% |
| `pyarrow-23.0.1/pyarrow/tests` | 57 | 31246.6 | 5.05% | 0.0% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python` | 57 | 9924.74 | 38.32% | 44.53% |
| `pyarrow-23.0.1/pyarrow/tests/parquet` | 13 | 3565.26 | 3.76% | 0.0% |
| `pyarrow-23.0.1/pyarrow/vendored` | 3 | 2441.6 | 36.73% | 53.79% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored` | 2 | 2041.86 | 40.68% | 0.0% |
| `pyarrow-23.0.1` | 5 | 1025.84 | 4.73% | 0.0% |
| `pyarrow-23.0.1/pyarrow/parquet` | 3 | 779.16 | 13.13% | 2.85% |
| `pyarrow-23.0.1/pyarrow/interchange` | 5 | 467.12 | 12.51% | 12.36% |
| `pyarrow-23.0.1/pyarrow/includes` | 15 | 322.12 | 1.66% | 2.26% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyarrow-23.0.1/pyarrow/_compute.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_csv.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_dataset_parquet.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_flight.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_json.pyx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_python_internal.h` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/async.h` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/benchmark.cc` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyarrow-23.0.1/pyarrow/tests/test_flight.py` -> **80** Orphaned Functions | **87** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_table.py` -> **149** Orphaned Functions | **2** Duplicates
- `pyarrow-23.0.1/pyarrow/types.pxi` -> **0** Orphaned Functions | **143** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` -> **126** Orphaned Functions | **8** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` -> **130** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyarrow-23.0.1/pyarrow/compute.py`** -> AI Confidence: **99.31%**
2. **`pyarrow-23.0.1/pyarrow/dataset.py`** -> AI Confidence: **99.31%**
3. **`pyarrow-23.0.1/pyarrow/interchange/from_dataframe.py`** -> AI Confidence: **99.31%**
4. **`pyarrow-23.0.1/pyarrow/pandas_compat.py`** -> AI Confidence: **99.31%**
5. **`pyarrow-23.0.1/pyarrow/parquet/core.py`** -> AI Confidence: **99.31%**
6. **`pyarrow-23.0.1/pyarrow/table.pxi`** -> AI Confidence: **99.31%**
7. **`pyarrow-23.0.1/pyarrow/tests/strategies.py`** -> AI Confidence: **99.31%**
8. **`pyarrow-23.0.1/pyarrow/tests/test_cython.py`** -> AI Confidence: **99.31%**
9. **`pyarrow-23.0.1/pyarrow/vendored/docscrape.py`** -> AI Confidence: **99.31%**
10. **`pyarrow-23.0.1/setup.py`** -> AI Confidence: **99.31%**
11. **`pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`** -> AI Confidence: **99.31%**
12. **`pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc`** -> AI Confidence: **99.31%**
13. **`pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc`** -> AI Confidence: **99.31%**
14. **`pyarrow-23.0.1/pyarrow/src/arrow/python/inference.cc`** -> AI Confidence: **99.31%**
15. **`pyarrow-23.0.1/pyarrow/src/arrow/python/numpy_convert.cc`** -> AI Confidence: **99.31%**
16. **`pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc`** -> AI Confidence: **99.31%**
17. **`pyarrow-23.0.1/pyarrow/src/arrow/python/platform.h`** -> AI Confidence: **99.29%**
18. **`pyarrow-23.0.1/pyarrow/src/arrow/python/visibility.h`** -> AI Confidence: **99.29%**
19. **`pyarrow-23.0.1/pyarrow/array.pxi`** -> AI Confidence: **99.24%**
20. **`pyarrow-23.0.1/pyarrow/io.pxi`** -> AI Confidence: **99.24%**
21. **`pyarrow-23.0.1/pyarrow/src/arrow/python/datetime.cc`** -> AI Confidence: **99.24%**
22. **`pyarrow-23.0.1/pyarrow/fs.py`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pyarrow-23.0.1/pyarrow/tests/test_substrait.py` -> **0.0003%** Exposure
### Exploit Generation Surface
- `pyarrow-23.0.1/pyarrow/__init__.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_acero.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_compute.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_csv.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_cuda.pyx` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `pyarrow-23.0.1/pyarrow/tests/test_fs.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/tests/test_memory.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/tests/test_misc.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/tests/test_orc.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/tests/test_gandiva.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored/pythoncapi_compat.h` -> **9.6344%** Exposure
- `pyarrow-23.0.1/pyarrow/src/arrow/python/gdb.cc` -> **0.0003%** Exposure
### Hardcoded Payload Artifacts
- `pyarrow-23.0.1/pyarrow/tests/test_fs.py` -> **85.6275%** Exposure
### Algorithmic DoS Exposure
- `pyarrow-23.0.1/pyarrow/__init__.py` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_azurefs.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_compute.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_csv.pyx` -> **100.0%** Exposure
- `pyarrow-23.0.1/pyarrow/_cuda.pyx` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1462` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyarrow-23.0.1/pyarrow/error.pxi` (PYTHON) -> Cumulative Risk: **902.18**
- **Archetype:** `file_cluster_4` (Distance: 10.51 IQR)
- **Magnitude:** 200.0 | **LOC:** 275 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__exit__` (Impact: 71.8), `_init_signals` (Impact: 30.7), `__cinit__` (Impact: 22.8)

### 2. `pyarrow-23.0.1/pyarrow/vendored/version.py` (PYTHON) -> Cumulative Risk: **816.71**
- **Archetype:** `file_cluster_0` (Distance: 11.242 IQR)
- **Magnitude:** 740.68 | **LOC:** 546 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_cmpkey` (Impact: 141.7), `__init__` (Impact: 100.3), `_legacy_cmpkey` (Impact: 42.8)

### 3. `pyarrow-23.0.1/pyarrow/pandas-shim.pxi` (PYTHON) -> Cumulative Risk: **806.65**
- **Archetype:** `file_cluster_0` (Distance: 11.974 IQR)
- **Magnitude:** 142.7 | **LOC:** 284 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9982%), State Flux (99.8471%)
- **Heaviest Functions:** `uses_string_dtype` (Impact: 22.1), `get_rangeindex_attribute` (Impact: 8.3), `series` (Impact: 3.1)

### 4. `pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc` (CPP) -> Cumulative Risk: **798.14**
- **Archetype:** `file_cluster_13` (Distance: 13.067 IQR)
- **Magnitude:** 360.82 | **LOC:** 505 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `UnboxIntegerAsInt64` (Impact: 50.3), `PyFloat_AsHalf` (Impact: 37.0), `IntegerScalarToDoubleSafe` (Impact: 18.9)

### 5. `pyarrow-23.0.1/pyarrow/src/arrow/python/numpy_convert.cc` (CPP) -> Cumulative Risk: **795.16**
- **Archetype:** `file_cluster_8` (Distance: 14.012 IQR)
- **Magnitude:** 851.62 | **LOC:** 564 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9295%)
- **Heaviest Functions:** `NdarraysToSparseCSFTensor` (Impact: 118.2), `TensorToNdarray` (Impact: 65.5), `SparseCSXMatrixToNdarray` (Impact: 61.9)

### 6. `pyarrow-23.0.1/pyarrow/src/arrow/python/decimal.cc` (CPP) -> Cumulative Risk: **780.38**
- **Archetype:** `file_cluster_8` (Distance: 11.834 IQR)
- **Magnitude:** 224.6 | **LOC:** 266 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `InternalDecimalFromPyObject` (Impact: 35.9), `DecimalFromStdString` (Impact: 22.2), `DecimalMetadata::Update` (Impact: 11.3)

### 7. `pyarrow-23.0.1/pyarrow/_dataset_parquet.pyx` (PYTHON) -> Cumulative Risk: **777.03**
- **Archetype:** `file_cluster_0` (Distance: 11.402 IQR)
- **Magnitude:** 1262.48 | **LOC:** 1114 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 183.3), `subset` (Impact: 95.7), `make_fragment` (Impact: 80.2)

### 8. `pyarrow-23.0.1/pyarrow/vendored/docscrape.py` (PYTHON) -> Cumulative Risk: **761.15**
- **Archetype:** `file_cluster_8` (Distance: 10.826 IQR)
- **Magnitude:** 1690.4 | **LOC:** 717 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9776%)
- **Heaviest Functions:** `_is_at_section` (Impact: 517.4), `__str__` (Impact: 331.5), `_parse` (Impact: 273.6)

### 9. `pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc` (CPP) -> Cumulative Risk: **760.66**
- **Archetype:** `file_cluster_13` (Distance: 13.382 IQR)
- **Magnitude:** 1424.58 | **LOC:** 1306 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9994%)
- **Heaviest Functions:** `Convert` (Impact: 177.9), `Append` (Impact: 110.3), `ConvertPySequence` (Impact: 96.6)

### 10. `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` (CPP) -> Cumulative Risk: **759.64**
- **Archetype:** `file_cluster_13` (Distance: 13.117 IQR)
- **Magnitude:** 247.52 | **LOC:** 247 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `MapPyError` (Impact: 56.6), `FormatImpl` (Impact: 11.6), `FromPyError` (Impact: 9.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyarrow-23.0.1/pyarrow/array.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.054 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.054 IQR)
- **Top Global Matches:** file_cluster_8: 11.054, file_cluster_7: 11.198, file_cluster_0: 11.266
- **Magnitude:** 4009.52 | **LOC:** 5033 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (18.6682%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `array` (Impact: 1155.9 | O(2^N))
  * `from_arrays` (Impact: 225.6 | O(N^5) | DB: 1)
  * `to_numpy` (Impact: 141.8 | O(2^N))
  * `from_arrays` (Impact: 131.0 | O(N^6))
  * `from_buffers` (Impact: 103.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 603`, `args: 150`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 30`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 49`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 111`, `import: 6`
* *Defense:* `safety: 56`, `doc: 346`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyarrow, numpy, os, cython, pandas, pyarrow.pandas_compat, warnings, collections.abc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/table.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.141 IQR)
- **Top Global Matches:** file_cluster_8: 11.841, file_cluster_7: 11.98, file_cluster_0: 12.021
- **Magnitude:** 3544.6 | **LOC:** 6628 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (19.9398%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `table` (Impact: 431.1 | O(2^N))
  * `record_batch` (Impact: 151.0 | O(N^6))
  * `cast` (Impact: 95.0 | O(2^N) | DB: 1)
  * `cast` (Impact: 94.9 | O(2^N) | DB: 1)
  * `__arrow_c_device_array__` (Impact: 86.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 423`, `args: 172`, `func_start: 169`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 88`, `duplicate_logic: 104`, `orphaned_logic: 20`
* *Architecture:* `api: 118`, `import: 9`
* *Defense:* `safety: 75`, `doc: 274`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` numpy, cython, pyarrow.compute, pandas, pyarrow.pandas_compat, warnings, pyarrow, pyarrow.interchange.dataframe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/io.pxi` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.998 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.833 IQR)
- **Top Global Matches:** file_cluster_8: 11.998, file_cluster_0: 12.123, file_cluster_7: 12.144
- **Magnitude:** 3293.36 | **LOC:** 2913 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (20.8328%), Tech Debt (18.445%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 2187.8 | O(2^N) | DB: 43)
  * `download` (Impact: 144.3 | O(N^6) | DB: 6)
  * `upload` (Impact: 107.5 | O(N^6) | DB: 3)
  * `read` (Impact: 98.8 | O(2^N) | DB: 1)
  * `_download_nothreads` (Impact: 72.7 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 319`, `args: 148`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 91`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 113`, `concurrency: 3`, `import: 10`
* *Defense:* `safety: 72`, `doc: 174`, `test: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyarrow, codecs, re, threading, io, pyarrow.util, sys, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_compute.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.18 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.421 IQR)
- **Top Global Matches:** file_cluster_8: 12.18, file_cluster_0: 12.383, file_cluster_13: 12.671
- **Magnitude:** 2922.4 | **LOC:** 4102 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (5.2016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_random` (Impact: 439.7 | O(N^6) | DB: 4)
  * `test_option_class_equality` (Impact: 199.7 | O(N^6) | DB: 2)
  * `test_cumulative_sum` (Impact: 105.6 | O(N^6))
  * `test_cumulative_prod` (Impact: 105.6 | O(N^6))
  * `test_select_k_table` (Impact: 99.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 1000`, `args: 177`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 12`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`, `orphaned_logic: 106`
* *Architecture:* `io: 2`, `api: 168`, `import: 21`
* *Defense:* `safety: 584`, `doc: 20`, `test: 872`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` functools, math, os, pandas, textwrap, pytest, numpy, inspect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_dataset.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.965 IQR)
- **Top Global Matches:** file_cluster_8: 11.479, file_cluster_0: 11.646, file_cluster_7: 11.659
- **Magnitude:** 2747.48 | **LOC:** 4229 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (20.9692%), Tech Debt (99.9941%)
**Top Internal Functions/Classes:**
  * `inspect` (Impact: 629.2 | O(N^6) | DB: 16)
  * `discover` (Impact: 386.1 | O(2^N) | DB: 2)
  * `__init__` (Impact: 106.9 | O(N^6) | DB: 2)
  * `__init__` (Impact: 95.6 | O(N^6) | DB: 5)
  * `from_paths` (Impact: 70.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 405`, `args: 185`, `func_start: 162`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 145`, `duplicate_logic: 92`
* *Architecture:* `io: 1`, `api: 110`, `import: 9`
* *Defense:* `safety: 49`, `doc: 194`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pyarrow._dataset_orc, codecs, issue, pyarrow.lib, collections, pyarrow.parquet, pyarrow._compute, pyarrow.substrait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.227 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.072 IQR)
- **Top Global Matches:** file_cluster_8: 12.227, file_cluster_0: 12.292, file_cluster_13: 12.629
- **Magnitude:** 2663.32 | **LOC:** 5942 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (3.7069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dataset_factory_inspect_bad_params` (Impact: 240.2 | O(N^6))
    * *Intent:* # Inspecting only one fragment should not promote the 'value' field
  * `test_filesystem_dataset` (Impact: 76.2 | O(N^6))
  * `test_construct_from_invalid_sources_rais` (Impact: 75.9 | O(N^2))
  * `_do_list_all_dirs` (Impact: 50.5 | O(2^N) | DB: 10)
  * `test_dataset` (Impact: 45.6 | O(N^6))
    * *Intent:* # scanning does raise
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 1081`, `args: 244`, `func_start: 236`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 57`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 21`, `orphaned_logic: 130`
* *Architecture:* `io: 33`, `api: 212`, `concurrency: 4`, `import: 46`
* *Defense:* `safety: 692`, `doc: 16`, `test: 1075`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` tempfile, threading, os, pyarrow.csv, pyarrow.fs, urllib.parse, .test_fs, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_flight.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.355 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.698 IQR)
- **Top Global Matches:** file_cluster_8: 12.355, file_cluster_0: 12.453, file_cluster_13: 12.525
- **Magnitude:** 2659.24 | **LOC:** 2790 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (2.9024%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_large_metadata_client` (Impact: 86.4 | O(N^6))
  * `test_write_error_propagation` (Impact: 65.6 | O(N^5))
  * `test_roundtrip_errors` (Impact: 64.2 | O(N^5))
  * `resource_root` (Impact: 61.8 | O(2^N) | DB: 12)
    * *Intent:* """Get the path to the test resources directory."""
  * `exchange_echo` (Impact: 51.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 742`, `args: 204`, `func_start: 204`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 61`, `dead_code: 2`, `duplicate_logic: 87`, `orphaned_logic: 80`
* *Architecture:* `io: 7`, `api: 230`, `concurrency: 16`, `import: 22`
* *Defense:* `safety: 216`, `doc: 230`, `test: 353`, `sync_locks: 4`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` signal, tempfile, threading, pyarrow.flight, os, pathlib, pytest, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_array.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.013 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 12.013, file_cluster_0: 12.122, file_cluster_13: 12.489
- **Magnitude:** 2447.54 | **LOC:** 4401 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (4.2852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_array_diff` (Impact: 1866.3 | O(N^6) | DB: 28)
  * `test_non_cpu_array` (Impact: 82.1 | O(N^2))
  * `test_array_slice` (Impact: 27.9 | O(N^4))
  * `test_array_slice_negative_step` (Impact: 22.3 | O(N^2))
  * `test_array_getitem` (Impact: 21.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 1183`, `args: 204`, `func_start: 204`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 11`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`, `orphaned_logic: 30`
* *Architecture:* `io: 12`, `api: 197`, `import: 22`
* *Defense:* `safety: 574`, `doc: 16`, `test: 1012`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` weakref, dateutil.relativedelta, pandas, pytest, subprocess, numpy, pandas.tseries.offsets, pyarrow.vendored.version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.321 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.386 IQR)
- **Top Global Matches:** file_cluster_13: 14.321, file_cluster_8: 14.479, file_cluster_11: 14.538
- **Magnitude:** 2435.6 | **LOC:** 2660 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 123
- **Risk Profile:** Cognitive Load (93.4185%), Tech Debt (97.6888%)
**Top Internal Functions/Classes:**
  * `ConvertListsLike` (Impact: 626.6 | O(N^6) | DB: 123)
  * `ListTypeSupported` (Impact: 158.5 | O(2^N) | DB: 7)
  * `CreateBlocks` (Impact: 134.9 | O(N^6) | DB: 18)
    * *Intent:* // Use a native pydict
  * `MakeBlock1D` (Impact: 119.5 | O(N^6) | DB: 31)
  * `ConvertChunkedArrayToPandas` (Impact: 97.3 | O(N^6) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 233`, `args: 151`, `func_start: 61`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 826`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 37`
* *Defense:* `safety: 36`, `doc: 10`, `sync_locks: 11`, `immutability_locks: 78`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` int_util.h, cstdint, macros.h, decimal.h, api.h, numpy_interop.h, common.h, type_traits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_table.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.883 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.567 IQR)
- **Top Global Matches:** file_cluster_8: 11.883, file_cluster_0: 12.112, file_cluster_13: 12.397
- **Magnitude:** 2369.98 | **LOC:** 4067 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.9677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_table_non_cpu` (Impact: 255.4 | O(N^5) | DB: 4)
    * *Intent:* # slice() test new_batch = cuda_recordbatch.slice(1, 3) verify_cuda_recordbatch(new_batch, expected_...
  * `test_chunked_array_non_cpu` (Impact: 233.9 | O(N^6))
  * `test_recordbatch_non_cpu` (Impact: 222.2 | O(N^6) | DB: 4)
    * *Intent:* # slice() test cuda_chunked_array.slice(2, 2) # take() test with pytest.raises(NotImplementedError):...
  * `test_table_basics` (Impact: 51.9 | O(N^6) | DB: 4)
  * `test_table_from_pydict` (Impact: 39.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 934`, `args: 177`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 29`, `duplicate_logic: 2`, `orphaned_logic: 149`
* *Architecture:* `io: 2`, `api: 171`, `import: 23`
* *Defense:* `safety: 505`, `doc: 26`, `test: 896`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` numpy, pandas.testing, collections, weakref, pyarrow.compute, pyarrow.vendored.version, with, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/types.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.334 IQR)
- **Top Global Matches:** file_cluster_0: 12.176, file_cluster_8: 12.256, file_cluster_7: 12.335
- **Magnitude:** 2194.5 | **LOC:** 6104 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (22.7425%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `field` (Impact: 102.4 | O(2^N))
  * `union` (Impact: 72.9 | O(2^N))
  * `__init__` (Impact: 71.3 | O(N^6) | DB: 2)
  * `wrap_array` (Impact: 56.0 | O(N^6))
  * `field_by_name` (Impact: 49.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 765`, `args: 257`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 71`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 143`
* *Architecture:* `io: 2`, `api: 170`, `import: 10`
* *Defense:* `safety: 125`, `doc: 434`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` atexit, pyarrow, json, pickle, decimal, numpy, re, cython...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_flight.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.826 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 11.826, file_cluster_0: 11.889, file_cluster_7: 11.967
- **Magnitude:** 2159.02 | **LOC:** 3296 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (22.3026%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 130.5 | O(N^6))
  * `__init__` (Impact: 97.9 | O(N^6))
    * *Intent:* # Override superclass method to use check_flight_status so we # can generate FlightWriteSizeExceeded...
  * `__init__` (Impact: 90.0 | O(N^6) | DB: 1)
  * `__init__` (Impact: 85.1 | O(N^6))
  * `do_action` (Impact: 64.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 530`, `args: 181`, `func_start: 175`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 10`, `duplicate_logic: 105`
* *Architecture:* `api: 153`, `concurrency: 14`, `import: 11`
* *Defense:* `safety: 120`, `doc: 380`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.463
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007692
  * `Imports (Out-Degree: 0):` enum, re, pyarrow.lib, collections, asyncio, weakref, time, pyarrow.ipc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_parquet.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.325 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.908 IQR)
- **Top Global Matches:** file_cluster_8: 11.325, file_cluster_0: 11.348, file_cluster_7: 11.47
- **Magnitude:** 2118.46 | **LOC:** 2422 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (28.1446%), Tech Debt (99.9976%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 293.1 | O(N^6) | DB: 5)
  * `from_ordering` (Impact: 109.4 | O(N^5) | DB: 1)
    * *Intent:* """Offset of data page relative to beginning of the file (int)."""
  * `__cinit__` (Impact: 99.7 | O(N^6) | DB: 4)
  * `iter_batches` (Impact: 96.5 | O(N^6))
  * `read_row_groups` (Impact: 56.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 397`, `args: 175`, `func_start: 160`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 63`, `dead_code: 1`, `duplicate_logic: 75`
* *Architecture:* `io: 1`, `api: 138`, `import: 4`
* *Defense:* `safety: 39`, `doc: 238`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyarrow, pyarrow.lib, pyarrow.parquet, textwrap, warnings, collections.abc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_compute.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.289 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.387 IQR)
- **Top Global Matches:** file_cluster_8: 11.289, file_cluster_7: 11.508, file_cluster_0: 11.611
- **Magnitude:** 2081.48 | **LOC:** 3480 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (13.2333%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 341.4 | O(2^N))
  * `cast` (Impact: 173.0 | O(2^N))
  * `_register_user_defined_function` (Impact: 112.1 | O(N^6))
  * `_set_options` (Impact: 64.0 | O(N^5) | DB: 6)
    * *Intent:* """ Return all function names in the global registry. """
  * `call` (Impact: 52.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 512`, `args: 220`, `func_start: 201`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 38`, `planned_debt: 1`, `duplicate_logic: 107`
* *Architecture:* `io: 1`, `api: 134`, `import: 9`
* *Defense:* `safety: 83`, `doc: 212`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` numpy, warnings, pyarrow.lib, collections, inspect, pyarrow.substrait, pyarrow.compute, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored/pythoncapi_compat.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.914 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.317 IQR)
- **Top Global Matches:** file_cluster_8: 13.914, file_cluster_11: 14.263, file_cluster_13: 14.29
- **Magnitude:** 2040.86 | **LOC:** 1520 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (81.353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyObject_Vectorcall` (Impact: 157.8 | O(N^5) | DB: 23)
    * *Intent:* #endif // gh-105922 added PyObject_Vectorcall() to Python 3.9.0a4 #if PY_VERSION_HEX < 0x030900A4
  * `Py_GetConstant` (Impact: 122.6 | O(2^N) | DB: 11)
    * *Intent:* // to Python 3.13.0a6 #if PY_VERSION_HEX < 0x030D00A6 && !defined(Py_CONSTANT_NONE) #define Py_CONST...
  * `PyModule_AddObjectRef` (Impact: 71.0 | O(2^N) | DB: 3)
    * *Intent:* #endif // bpo-1635741 added PyModule_AddObjectRef() to Python 3.10.0a3 #if PY_VERSION_HEX < 0x030A00...
  * `PyUnicode_EqualToUTF8AndSize` (Impact: 63.1 | O(N^3) | DB: 18)
    * *Intent:* #endif // gh-110289 added PyUnicode_EqualToUTF8() and PyUnicode_EqualToUTF8AndSize() // to Python 3....
  * `PyDict_SetDefaultRef` (Impact: 62.2 | O(N^5) | DB: 5)
    * *Intent:* #endif // gh-114329 added PyList_GetItemRef() to Python 3.13.0a4 #if PY_VERSION_HEX < 0x030D00A4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 251`, `args: 174`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 839`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` frameobject.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/pandas_compat.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.123 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.206 IQR)
- **Top Global Matches:** file_cluster_8: 12.123, file_cluster_13: 12.127, file_cluster_17: 12.164
- **Magnitude:** 1869.44 | **LOC:** 1296 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (25.2325%), Tech Debt (11.0874%)
**Top Internal Functions/Classes:**
  * `dataframe_to_arrays` (Impact: 301.2 | O(N^6) | DB: 4)
  * `_get_extension_dtypes` (Impact: 260.7 | O(N^6))
  * `construct_metadata` (Impact: 183.1 | O(N^6) | DB: 4)
  * `_add_any_metadata` (Impact: 112.1 | O(N^6) | DB: 4)
  * `_reconstruct_index` (Impact: 96.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 179`, `args: 37`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 103`, `dead_code: 5`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 69`, `doc: 24`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.262
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.05698
  * `Imports (Out-Degree: 1):` json, pyarrow, numpy, decimal, concurrent.futures.thread, collections.abc, threading, copy...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/scalar.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.569 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.109 IQR)
- **Top Global Matches:** file_cluster_8: 10.569, file_cluster_7: 10.671, file_cluster_1: 10.975
- **Magnitude:** 1834.96 | **LOC:** 1686 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.1592%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 1116.1 | O(2^N))
    * *Intent:* """ Return this value as a Python Decimal. Parameters ---------- maps_as_pydicts : str, optional, de...
  * `scalar` (Impact: 68.6 | O(2^N))
  * `_datetime_from_int` (Impact: 51.4 | O(N^4))
  * `validate` (Impact: 25.4 | O(N^4))
  * `as_py` (Impact: 18.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 362`, `args: 105`, `func_start: 104`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 4`, `duplicate_logic: 48`, `orphaned_logic: 5`
* *Architecture:* `api: 65`, `import: 4`
* *Defense:* `safety: 18`, `doc: 200`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, collections, pyarrow, collections.abc, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/vendored/docscrape.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.826 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.398 IQR)
- **Top Global Matches:** file_cluster_8: 10.826, file_cluster_13: 10.933, file_cluster_7: 11.122
- **Magnitude:** 1690.4 | **LOC:** 717 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (32.6565%), Tech Debt (61.3717%)
**Top Internal Functions/Classes:**
  * `_is_at_section` (Impact: 517.4 | O(2^N) | DB: 4)
  * `__str__` (Impact: 331.5 | O(2^N) | DB: 8)
  * `_parse` (Impact: 273.6 | O(N^6) | DB: 3)
    * *Intent:* # If several signatures present, take the last one
  * `__init__` (Impact: 74.0 | O(2^N) | DB: 2)
  * `get_doc_object` (Impact: 50.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 159`, `args: 54`, `func_start: 54`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 53`, `dead_code: 1`, `duplicate_logic: 5`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 26`, `import: 10`
* *Defense:* `safety: 18`, `doc: 18`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sphinx.ext.autodoc, re, inspect, collections, copy, textwrap, sys, pydoc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_io.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.673 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.134 IQR)
- **Top Global Matches:** file_cluster_0: 12.673, file_cluster_8: 12.721, file_cluster_13: 12.964
- **Magnitude:** 1550.14 | **LOC:** 2213 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (4.8841%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_compression_level` (Impact: 76.6 | O(N^6))
  * `test_non_cpu_buffer` (Impact: 60.6 | O(N^2))
  * `test_python_file_get_stream` (Impact: 50.5 | O(N^6))
  * `check_large_seeks` (Impact: 40.0 | O(N^4) | DB: 9)
  * `test_native_file_modes` (Impact: 34.2 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 683`, `args: 138`, `func_start: 138`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 24`, `fragile_debt: 1`
* *Architecture:* `io: 85`, `api: 243`, `import: 21`
* *Defense:* `safety: 427`, `doc: 2`, `test: 621`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005698
  * `Imports (Out-Degree: 1):` tempfile, math, os, weakref, contextlib, pandas, pathlib, gzip...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_csv.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.656 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.466 IQR)
- **Top Global Matches:** file_cluster_0: 12.656, file_cluster_8: 13.0, file_cluster_13: 13.054
- **Magnitude:** 1466.86 | **LOC:** 1559 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (48.1454%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 141.6 | O(N^4) | DB: 13)
  * `__init__` (Impact: 64.1 | O(N^4) | DB: 7)
  * `__init__` (Impact: 56.2 | O(N^4) | DB: 7)
  * `timestamp_parsers` (Impact: 52.6 | O(2^N))
  * `invalid_row_handler` (Impact: 48.8 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 182`, `args: 100`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 203`, `duplicate_logic: 88`
* *Architecture:* `api: 76`, `import: 3`
* *Defense:* `safety: 19`, `doc: 90`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io, pyarrow.lib, collections, pyarrow, collections.abc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_fs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.135 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_8: 12.135, file_cluster_0: 12.185, file_cluster_13: 12.375
- **Magnitude:** 1428.34 | **LOC:** 2257 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.0542%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_get_file_info_with_selector` (Impact: 105.8 | O(N^6))
  * `test_azurefs_options` (Impact: 89.4 | O(N^6))
  * `test_s3fs_limited_permissions_create_buc` (Impact: 80.5 | O(N^6))
    * *Intent:* # It's an aware UTC datetime
  * `test_open_append_stream` (Impact: 70.4 | O(N^6) | DB: 3)
  * `test_s3_options` (Impact: 65.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 605`, `args: 121`, `func_start: 112`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 16`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `io: 18`, `api: 161`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 381`, `doc: 8`, `test: 558`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.903
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.004274
  * `Imports (Out-Degree: 5):` threading, os, weakref, pyarrow.fs, urllib.request, fsspec.implementations.memory, pyarrow.tests.test_io, huggingface_hub...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.382 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.802 IQR)
- **Top Global Matches:** file_cluster_13: 13.382, file_cluster_8: 13.567, file_cluster_11: 13.708
- **Magnitude:** 1424.58 | **LOC:** 1306 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (78.7771%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `Convert` (Impact: 177.9 | O(N^6) | DB: 13)
  * `Append` (Impact: 110.3 | O(2^N))
  * `ConvertPySequence` (Impact: 96.6 | O(N^6) | DB: 11)
  * `Field` (Impact: 64.5 | O(N^6) | DB: 8)
  * `Append` (Impact: 61.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 165`, `args: 111`, `func_start: 41`, `class_start: 14`
* *Risk/State:* `state_mutation: 411`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 27`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 37`
* *Defense:* `safety: 12`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 56`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` decimal.h, decimal.h, datetime.h, numpy_interop.h, type_traits.h, scalar.h, iterators.h, array.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.132 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.132, file_cluster_0: 11.6, file_cluster_7: 11.709
- **Magnitude:** 1400.32 | **LOC:** 5320 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.5466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_pandas_roundtrip` (Impact: 127.5 | O(N^6))
  * `_check_array_roundtrip` (Impact: 55.9 | O(N^6))
  * `test_timestamp_to_pandas_out_of_bounds` (Impact: 48.1 | O(N^5))
  * `test_integer_byteorder` (Impact: 43.1 | O(N^6))
  * `test_arrow_time_to_pandas` (Impact: 38.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 950`, `args: 311`, `func_start: 311`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 15`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`, `orphaned_logic: 94`
* *Architecture:* `io: 7`, `api: 299`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 384`, `doc: 22`, `test: 734`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` numpy.testing, warnings, pyarrow.tests.util, pandas, multiprocessing, numpy.exceptions, pytest, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/dataset.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.131 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.543 IQR)
- **Top Global Matches:** file_cluster_8: 10.131, file_cluster_13: 10.65, file_cluster_7: 10.655
- **Magnitude:** 1392.08 | **LOC:** 1041 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.4131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_dataset` (Impact: 437.5 | O(N^6))
    * *Intent:* # fall back to local file system as the default
  * `dataset` (Impact: 287.1 | O(2^N))
  * `partitioning` (Impact: 210.8 | O(N^5))
    * *Intent:* """ Specify a partitioning scheme. The supported schemes include: - "DirectoryPartitioning": this sc...
  * `_filesystem_dataset` (Impact: 96.2 | O(N^6))
  * `_ensure_multiple_sources` (Impact: 80.3 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 93`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 39`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.46
  * `Choke Point (Betweenness):` 0.000932 | `Ripple Effect (Closeness):` 0.03885
  * `Imports (Out-Degree: 5):` pyarrow._dataset_orc, pyarrow.parquet, pyarrow._dataset, pyarrow.util, pyarrow.compute, pyarrow.dataset, pyarrow._dataset_parquet, pyarrow.fs...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_csv.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.355 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.809 IQR)
- **Top Global Matches:** file_cluster_8: 11.355, file_cluster_13: 11.832, file_cluster_7: 11.838
- **Magnitude:** 1352.26 | **LOC:** 2068 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (5.1601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parse_options` (Impact: 964.1 | O(N^6) | DB: 16)
  * `test_read_options` (Impact: 105.7 | O(N^6))
  * `check_options_class` (Impact: 25.2 | O(N^3))
    * *Intent:* """ Check setting and getting attributes of an *Options class. """
  * `make_random_csv` (Impact: 23.2 | O(N^3))
  * `check_options_class_pickling` (Impact: 14.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 390`, `args: 102`, `func_start: 102`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 4`, `fragile_debt: 13`, `orphaned_logic: 8`
* *Architecture:* `io: 5`, `api: 110`, `concurrency: 8`, `import: 24`
* *Defense:* `safety: 222`, `doc: 20`, `test: 330`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` signal, tempfile, threading, os, weakref, pyarrow.csv, abc, gzip...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` (PYTHON) | Magnitude: 1268.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1687, structural_boundaries: 929, test: 710, safety: 462
- `pyarrow-23.0.1/pyarrow/tensor.pxi` (PYTHON) | Magnitude: 943.9 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 593, structural_boundaries: 225, doc: 120, branch: 101
- `pyarrow-23.0.1/pyarrow/tests/test_ipc.py` (PYTHON) | Magnitude: 946.02 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 880, structural_boundaries: 360, test: 300, safety: 179
- `pyarrow-23.0.1/pyarrow/_json.pyx` (PYTHON) | Magnitude: 325.52 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 48, state_mutation: 40, branch: 29
- `pyarrow-23.0.1/pyarrow/tests/test_io.py` (PYTHON) | Magnitude: 1550.14 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1388, structural_boundaries: 683, test: 621, safety: 427

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyarrow-23.0.1/pyarrow/src/arrow/python/flight.h` (CPP) | Magnitude: 83.18 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, safety: 61, immutability_locks: 53, state_mutation: 48
- `pyarrow-23.0.1/pyarrow/src/arrow/python/extension_type.cc` (CPP) | Magnitude: 180.0 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 52, structural_boundaries: 36, branch: 23
- `pyarrow-23.0.1/pyarrow/_pyarrow_cpp_tests.pyx` (PYTHON) | Magnitude: 24.84 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, args: 5, api: 5
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` (CPP) | Magnitude: 247.52 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 111, branch: 28, structural_boundaries: 28
- `pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc` (CPP) | Magnitude: 360.82 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 134, args: 69, branch: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pyarrow-23.0.1/pyarrow/interchange/column.py` (PYTHON) | Magnitude: 165.5 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 66, encapsulation: 50, branch: 40
- `pyarrow-23.0.1/pyarrow/interchange/dataframe.py` (PYTHON) | Magnitude: 137.66 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, encapsulation: 51, structural_boundaries: 36, doc: 28
- `pyarrow-23.0.1/pyarrow/interchange/buffer.py` (PYTHON) | Magnitude: 47.9 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, doc: 14, encapsulation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pyarrow-23.0.1/pyarrow/error.pxi` (PYTHON) | Magnitude: 200.0 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 67, branch: 42, encapsulation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` (PYTHON) | Magnitude: 1869.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 781, branch: 242, structural_boundaries: 179, encapsulation: 120
- `pyarrow-23.0.1/pyarrow/compat.pxi` (PYTHON) | Magnitude: 29.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, branch: 7, safety: 4
- `pyarrow-23.0.1/pyarrow/builder.pxi` (PYTHON) | Magnitude: 101.06 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 21, doc: 16, branch: 12
- `pyarrow-23.0.1/pyarrow/tests/test_extension_type.py` (PYTHON) | Magnitude: 1184.42 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1264, structural_boundaries: 726, test: 471, safety: 389
- `pyarrow-23.0.1/pyarrow/src/arrow/python/ipc.h` (CPP) | Magnitude: 17.72 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 20, indent_spaces: 17, args: 6, import: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 0.187** (Bridge: 0.0021 * Flux: 87.7822%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 93.3537%)
- `pyarrow-23.0.1/pyarrow/parquet/core.py` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 98.291%)
- `pyarrow-23.0.1/pyarrow/interchange/column.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 65.2283%)
- `pyarrow-23.0.1/pyarrow/feather.py` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 92.4584%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 3.139** (Embedded: 0.057 * Error Risk: 55.0896%)
- `pyarrow-23.0.1/pyarrow/interchange/column.py` -> **Severity: 0.805** (Embedded: 0.0153 * Error Risk: 52.7273%)
- `pyarrow-23.0.1/pyarrow/compute.py` -> **Severity: 0.794** (Embedded: 0.078 * Error Risk: 10.1844%)
- `pyarrow-23.0.1/pyarrow/_azurefs.pyx` -> **Severity: 0.723** (Embedded: 0.0493 * Error Risk: 14.674%)
- `pyarrow-23.0.1/pyarrow/memory.pxi` -> **Severity: 0.512** (Embedded: 0.107 * Error Risk: 4.7861%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyarrow-23.0.1/pyarrow/memory.pxi` -> **Severity: 5546.089** (Blast Radius: 55.461 * Doc Risk: 99.9998%)
- `pyarrow-23.0.1/pyarrow/util.py` -> **Severity: 3443.483** (Blast Radius: 34.513 * Doc Risk: 99.7735%)
- `pyarrow-23.0.1/pyarrow/_substrait.pyx` -> **Severity: 2711.497** (Blast Radius: 27.618 * Doc Risk: 98.1786%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 2583.892** (Blast Radius: 26.262 * Doc Risk: 98.389%)
- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 2576.136** (Blast Radius: 26.534 * Doc Risk: 97.0881%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
