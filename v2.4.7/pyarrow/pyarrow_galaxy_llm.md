# ARCHITECTURAL_BRIEF: pyarrow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyarrow` |
| **Timestamp** | `2026-08-07T05:25:07.139377+00:00` |
| **Scan Duration** | `2.11s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 228 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Cognitive Load Exposure | 0.0 | 100.0 | 18.8 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.4 | 32.3 | 29.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.9 | 1.9 | 0.0 |
| API Exposure | 0.0 | 13.9 | 3.4 | 2.7 | 0.0 |
| Concurrency Exposure | 0.0 | 99.6 | 2.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.8 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 13.4 | 11.9 | 11.9 |
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

- `test_array_diff` (@ `pyarrow-23.0.1/pyarrow/tests/test_array.py`) -> Impact: **666.8** | LOC: 3741
- `__cinit__` (@ `pyarrow-23.0.1/pyarrow/io.pxi`) -> Impact: **363.9** | LOC: 1197
- `test_parse_options` (@ `pyarrow-23.0.1/pyarrow/tests/test_csv.py`) -> Impact: **340.5** | LOC: 1822
- `__init__` (@ `pyarrow-23.0.1/pyarrow/_s3fs.pyx`) -> Impact: **252.0** | LOC: 142
- `__getbuffer__` (@ `pyarrow-23.0.1/pyarrow/tensor.pxi`) -> Impact: **218.8** | LOC: 736
- `inspect` (@ `pyarrow-23.0.1/pyarrow/_dataset.pyx`) -> Impact: **204.4** | LOC: 689
- `ConvertListsLike` (@ `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc`) -> Impact: **191.7** | LOC: 353
- `_perform_join` (@ `pyarrow-23.0.1/pyarrow/acero.py`) -> Impact: **183.9** | LOC: 144
- `__repr__` (@ `pyarrow-23.0.1/pyarrow/scalar.pxi`) -> Impact: **180.8** | LOC: 498
  * *Intent:* """ Return this value as a Python Decimal. Parameters ---------- maps_as_pydicts : str, optional, default `None` Valid values are `None`, 'lossy', or ...
- `test_special_chars_filename` (@ `pyarrow-23.0.1/pyarrow/tests/parquet/test_basic.py`) -> Impact: **177.7** | LOC: 853

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyarrow-23.0.1/pyarrow` | 72 | 17494.46 | 19.15% | 48.84% |
| `pyarrow-23.0.1/pyarrow/tests` | 57 | 16996.0 | 5.03% | 0.0% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python` | 57 | 6687.64 | 38.72% | 44.56% |
| `pyarrow-23.0.1/pyarrow/tests/parquet` | 13 | 1969.46 | 3.77% | 0.0% |
| `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored` | 2 | 1466.16 | 40.68% | 0.0% |
| `pyarrow-23.0.1/pyarrow/vendored` | 3 | 899.0 | 42.42% | 60.01% |
| `pyarrow-23.0.1/pyarrow/parquet` | 3 | 410.86 | 9.49% | 2.85% |
| `pyarrow-23.0.1/pyarrow/includes` | 15 | 322.12 | 1.66% | 2.26% |
| `pyarrow-23.0.1` | 5 | 295.74 | 4.73% | 0.0% |
| `pyarrow-23.0.1/pyarrow/interchange` | 5 | 257.32 | 12.51% | 12.36% |

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
- `pyarrow-23.0.1/pyarrow/tests/test_flight.py` -> **80** Orphaned Functions | **98** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_table.py` -> **149** Orphaned Functions | **9** Duplicates
- `pyarrow-23.0.1/pyarrow/types.pxi` -> **0** Orphaned Functions | **144** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` -> **130** Orphaned Functions | **8** Duplicates
- `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` -> **126** Orphaned Functions | **10** Duplicates

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

### Hardcoded Payload Artifacts
- `pyarrow-23.0.1/pyarrow/tests/test_fs.py` -> **85.6275%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1462` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyarrow-23.0.1/pyarrow/error.pxi` (PYTHON) -> Cumulative Risk: **657.95**
- **Archetype:** `file_cluster_4` (Distance: 10.51 IQR)
- **Magnitude:** 99.7 | **LOC:** 275 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.7657%), State Flux (83.0752%), Verification (80.0%)
- **Heaviest Functions:** `__exit__` (Impact: 21.5), `__cinit__` (Impact: 9.8), `_init_signals` (Impact: 9.0)

### 2. `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` (CPP) -> Cumulative Risk: **650.92**
- **Archetype:** `file_cluster_13` (Distance: 13.036 IQR)
- **Magnitude:** 203.22 | **LOC:** 247 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.5588%)
- **Heaviest Functions:** `MapPyError` (Impact: 28.9), `IsPyError` (Impact: 6.4), `PyBuffer::Init` (Impact: 5.8)

### 3. `pyarrow-23.0.1/pyarrow/vendored/version.py` (PYTHON) -> Cumulative Risk: **644.18**
- **Archetype:** `file_cluster_0` (Distance: 11.242 IQR)
- **Magnitude:** 374.28 | **LOC:** 546 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (97.527%), Verification (80.0%)
- **Heaviest Functions:** `_cmpkey` (Impact: 42.5), `__init__` (Impact: 34.5), `_parse_letter_version` (Impact: 17.2)

### 4. `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` (CPP) -> Cumulative Risk: **639.01**
- **Archetype:** `file_cluster_13` (Distance: 14.302 IQR)
- **Magnitude:** 1536.8 | **LOC:** 2660 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.892%), Safety Score (96.1746%)
- **Heaviest Functions:** `ConvertListsLike` (Impact: 191.7), `ListTypeSupported` (Impact: 80.5), `Visit` (Impact: 54.9)

### 5. `pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc` (CPP) -> Cumulative Risk: **632.57**
- **Archetype:** `file_cluster_13` (Distance: 13.014 IQR)
- **Magnitude:** 285.42 | **LOC:** 505 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4383%)
- **Heaviest Functions:** `UnboxIntegerAsInt64` (Impact: 50.3), `PandasObjectIsNull` (Impact: 18.0), `PyFloat_AsHalf` (Impact: 11.0)

### 6. `pyarrow-23.0.1/pyarrow/src/arrow/python/numpy_convert.cc` (CPP) -> Cumulative Risk: **625.91**
- **Archetype:** `file_cluster_8` (Distance: 13.993 IQR)
- **Magnitude:** 501.02 | **LOC:** 564 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.2147%), Cognitive Load (96.89%)
- **Heaviest Functions:** `NumPyDtypeToArrow` (Impact: 39.4), `NdarraysToSparseCSFTensor` (Impact: 35.6), `TensorToNdarray` (Impact: 20.4)

### 7. `pyarrow-23.0.1/pyarrow/src/arrow/python/decimal.cc` (CPP) -> Cumulative Risk: **622.68**
- **Archetype:** `file_cluster_8` (Distance: 11.824 IQR)
- **Magnitude:** 138.0 | **LOC:** 266 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9996%), Cognitive Load (92.4639%)
- **Heaviest Functions:** `InternalDecimalFromPyObject` (Impact: 10.9), `DecimalFromStdString` (Impact: 7.3), `DecimalMetadata::Update` (Impact: 6.0)

### 8. `pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc` (CPP) -> Cumulative Risk: **620.2**
- **Archetype:** `file_cluster_13` (Distance: 13.347 IQR)
- **Magnitude:** 859.98 | **LOC:** 1306 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9994%), Safety Score (91.373%)
- **Heaviest Functions:** `Convert` (Impact: 52.9), `ConvertPySequence` (Impact: 29.5), `ConvertToSequenceAndInferSize` (Impact: 26.2)

### 9. `pyarrow-23.0.1/pyarrow/src/arrow/python/inference.cc` (CPP) -> Cumulative Risk: **603.97**
- **Archetype:** `file_cluster_13` (Distance: 12.45 IQR)
- **Magnitude:** 319.76 | **LOC:** 809 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (94.4589%), Safety Score (90.0919%)
- **Heaviest Functions:** `Visit` (Impact: 86.6), `DatetimeUnitName` (Impact: 31.1), `Observe` (Impact: 25.0)

### 10. `pyarrow-23.0.1/pyarrow/src/arrow/python/type_traits.h` (CPP) -> Cumulative Risk: **599.42**
- **Archetype:** `file_cluster_8` (Distance: 11.496 IQR)
- **Magnitude:** 154.42 | **LOC:** 354 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9031%), Tech Debt (99.8475%), Safety Score (81.7574%)
- **Heaviest Functions:** `NumPyTypeSize` (Impact: 32.8), `NumPyFrequency` (Impact: 12.8), `isnull` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyarrow-23.0.1/pyarrow/src/arrow/python/arrow_to_pandas.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.302 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.372 IQR)
- **Top Global Matches:** file_cluster_13: 14.302, file_cluster_8: 14.463, file_cluster_11: 14.519
- **Magnitude:** 1536.8 | **LOC:** 2660 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.9143%), Tech Debt (99.892%)
**Top Internal Functions/Classes:**
  * `ConvertListsLike` (Impact: 191.7)
  * `ListTypeSupported` (Impact: 80.5)
  * `Visit` (Impact: 54.9)
  * `ConvertChunkedArrayToPandas` (Impact: 30.2)
  * `GetWriter` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 233`, `args: 137`, `func_start: 61`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 826`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 8`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 37`
* *Defense:* `safety: 36`, `doc: 10`, `sync_locks: 11`, `immutability_locks: 78`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` macros.h, status.h, numpy_convert.h, iostream, numpy_interop.h, memory, datetime.h, array.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_dataset.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.222 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.059 IQR)
- **Top Global Matches:** file_cluster_8: 12.222, file_cluster_0: 12.287, file_cluster_13: 12.625
- **Magnitude:** 1488.52 | **LOC:** 5942 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6944%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dataset_factory_inspect_bad_params` (Impact: 80.0)
    * *Intent:* # Inspecting only one fragment should not promote the 'value' field
  * `test_construct_from_invalid_sources_rais` (Impact: 51.7)
  * `test_filesystem_dataset` (Impact: 24.2)
  * `multisourcefs` (Impact: 21.5)
  * `test_dataset_filter` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 1081`, `args: 248`, `func_start: 236`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 55`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 21`, `duplicate_logic: 8`, `orphaned_logic: 130`
* *Architecture:* `io: 33`, `api: 212`, `concurrency: 4`, `import: 46`
* *Defense:* `safety: 692`, `doc: 16`, `test: 1075`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` pyarrow.lib, pyarrow.fs, pyarrow.dataset, textwrap, pyarrow.parquet, contextlib, posixpath, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/vendored/pythoncapi_compat.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.909 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.315 IQR)
- **Top Global Matches:** file_cluster_8: 13.909, file_cluster_11: 14.258, file_cluster_13: 14.285
- **Magnitude:** 1465.16 | **LOC:** 1520 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyObject_Vectorcall` (Impact: 54.9)
    * *Intent:* #endif // gh-105922 added PyObject_Vectorcall() to Python 3.9.0a4 #if PY_VERSION_HEX < 0x030900A4
  * `PyUnicode_EqualToUTF8AndSize` (Impact: 33.1)
    * *Intent:* #endif // gh-110289 added PyUnicode_EqualToUTF8() and PyUnicode_EqualToUTF8AndSize() // to Python 3....
  * `Py_GetConstant` (Impact: 32.6)
    * *Intent:* // to Python 3.13.0a6 #if PY_VERSION_HEX < 0x030D00A6 && !defined(Py_CONSTANT_NONE) #define Py_CONST...
  * `PyTime_PerfCounter` (Impact: 31.1)
  * `PyDict_Pop` (Impact: 28.1)
    * *Intent:* #endif // gh-111262 added PyDict_Pop() and PyDict_PopString() to Python 3.13.0a2 #if PY_VERSION_HEX ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 251`, `args: 169`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 839`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Python.h, frameobject.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_flight.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.345 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.706 IQR)
- **Top Global Matches:** file_cluster_8: 12.345, file_cluster_0: 12.449, file_cluster_13: 12.521
- **Magnitude:** 1395.84 | **LOC:** 2790 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_large_metadata_client` (Impact: 25.7)
  * `test_write_error_propagation` (Impact: 24.0)
  * `test_roundtrip_errors` (Impact: 22.6)
  * `exchange_echo` (Impact: 21.0)
  * `test_middleware_mapping` (Impact: 19.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 742`, `args: 225`, `func_start: 204`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 57`, `dead_code: 2`, `duplicate_logic: 98`, `orphaned_logic: 80`
* *Architecture:* `io: 7`, `api: 230`, `concurrency: 16`, `import: 22`
* *Defense:* `safety: 216`, `doc: 230`, `test: 353`, `sync_locks: 4`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pyarrow.flight, pyarrow.lib, ast, pyarrow.tests, json, pytest, signal, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_compute.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.182 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.401 IQR)
- **Top Global Matches:** file_cluster_8: 12.182, file_cluster_0: 12.381, file_cluster_13: 12.67
- **Magnitude:** 1360.0 | **LOC:** 4102 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_random` (Impact: 145.2)
  * `test_option_class_equality` (Impact: 74.1)
  * `test_strftime` (Impact: 39.1)
    * *Intent:* # Allow the last digit to vary. The tolerance is higher for # the iterative algorithm (GH-35576). di...
  * `check_partition_nth` (Impact: 39.0)
    * *Intent:* # Check rounding with calendar_based_origin=True. # approximate this functionality and exclude unit ...
  * `test_cumulative_max` (Impact: 32.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 1000`, `args: 180`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 12`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 106`
* *Architecture:* `io: 2`, `api: 168`, `import: 21`
* *Defense:* `safety: 584`, `doc: 20`, `test: 872`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pyarrow.lib, decimal, textwrap, pyarrow.vendored.version, pytest, pyarrow.substrait, numpy, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/table.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.141 IQR)
- **Top Global Matches:** file_cluster_8: 11.841, file_cluster_7: 11.98, file_cluster_0: 12.021
- **Magnitude:** 1337.5 | **LOC:** 6628 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9398%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `table` (Impact: 63.7)
  * `record_batch` (Impact: 44.8)
  * `_from_pylist` (Impact: 32.4)
  * `__arrow_c_device_array__` (Impact: 26.2)
  * `chunked_array` (Impact: 24.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 423`, `args: 172`, `func_start: 169`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 88`, `duplicate_logic: 104`, `orphaned_logic: 20`
* *Architecture:* `api: 118`, `import: 9`
* *Defense:* `safety: 75`, `doc: 274`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cython, warnings, pyarrow.pandas_compat, pyarrow, numpy, pandas, pyarrow.interchange.dataframe, pyarrow.compute
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_table.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.882 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.551 IQR)
- **Top Global Matches:** file_cluster_8: 11.882, file_cluster_0: 12.107, file_cluster_13: 12.393
- **Magnitude:** 1301.08 | **LOC:** 4067 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_table_non_cpu` (Impact: 91.4)
    * *Intent:* # slice() test new_batch = cuda_recordbatch.slice(1, 3) verify_cuda_recordbatch(new_batch, expected_...
  * `test_chunked_array_non_cpu` (Impact: 71.8)
  * `test_recordbatch_non_cpu` (Impact: 69.1)
    * *Intent:* # slice() test cuda_chunked_array.slice(2, 2) # take() test with pytest.raises(NotImplementedError):...
  * `test_table_group_by` (Impact: 18.1)
  * `test_chunked_array_equals` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 934`, `args: 177`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 29`, `duplicate_logic: 9`, `orphaned_logic: 149`
* *Architecture:* `io: 2`, `api: 171`, `import: 23`
* *Defense:* `safety: 505`, `doc: 26`, `test: 896`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, sys, pandas.testing, numpy, with, collections.abc, pyarrow, weakref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/array.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.054 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.054 IQR)
- **Top Global Matches:** file_cluster_8: 11.054, file_cluster_7: 11.198, file_cluster_0: 11.266
- **Magnitude:** 1242.92 | **LOC:** 5033 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6682%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `array` (Impact: 171.6)
  * `from_arrays` (Impact: 77.5)
  * `from_arrays` (Impact: 39.1)
  * `from_buffers` (Impact: 30.7)
  * `from_buffers` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 603`, `args: 150`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 30`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 49`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 111`, `import: 6`
* *Defense:* `safety: 56`, `doc: 346`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cython, os, warnings, pyarrow.pandas_compat, collections.abc, pyarrow, numpy, pandas
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_array.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.013 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 12.013, file_cluster_0: 12.122, file_cluster_13: 12.489
- **Magnitude:** 1138.94 | **LOC:** 4401 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_array_diff` (Impact: 666.8)
  * `test_non_cpu_array` (Impact: 56.1)
  * `test_array_slice_negative_step` (Impact: 15.4)
  * `test_array_slice` (Impact: 12.3)
  * `test_to_numpy_unsupported_types` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 1183`, `args: 204`, `func_start: 204`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 11`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`, `orphaned_logic: 30`
* *Architecture:* `io: 12`, `api: 197`, `import: 22`
* *Defense:* `safety: 574`, `doc: 16`, `test: 1012`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hypothesis.strategies, decimal, gc, pandas.tseries.offsets, pyarrow.vendored.version, pytest, hypothesis, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/types.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.177 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.335 IQR)
- **Top Global Matches:** file_cluster_0: 12.177, file_cluster_8: 12.258, file_cluster_7: 12.337
- **Magnitude:** 1124.2 | **LOC:** 6104 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7768%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `field` (Impact: 21.9)
  * `__init__` (Impact: 21.3)
  * `union` (Impact: 18.9)
  * `schema` (Impact: 17.4)
  * `fixed_shape_tensor` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 765`, `args: 257`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 71`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 144`
* *Architecture:* `io: 2`, `api: 173`, `import: 10`
* *Defense:* `safety: 125`, `doc: 434`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cython, sys, decimal, atexit, warnings, pyarrow.pandas_compat, numpy, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_io.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.662 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.101 IQR)
- **Top Global Matches:** file_cluster_0: 12.662, file_cluster_8: 12.719, file_cluster_13: 12.955
- **Magnitude:** 1075.44 | **LOC:** 2213 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8841%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_non_cpu_buffer` (Impact: 41.5)
  * `test_compression_level` (Impact: 24.6)
  * `test_native_file_modes` (Impact: 23.8)
  * `test_buffer_slicing` (Impact: 18.0)
  * `check_large_seeks` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 683`, `args: 138`, `func_start: 138`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 24`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 85`, `api: 244`, `import: 21`
* *Defense:* `safety: 427`, `doc: 2`, `test: 621`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005698
  * `Imports (Out-Degree: 1):` gc, contextlib, pytest, tempfile, pathlib, numpy, pandas, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_dataset.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.965 IQR)
- **Top Global Matches:** file_cluster_8: 11.479, file_cluster_0: 11.646, file_cluster_7: 11.659
- **Magnitude:** 1067.68 | **LOC:** 4229 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9692%), Tech Debt (99.9941%)
**Top Internal Functions/Classes:**
  * `inspect` (Impact: 204.4)
  * `discover` (Impact: 62.8)
  * `__init__` (Impact: 31.9)
  * `__init__` (Impact: 28.2)
  * `from_paths` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 405`, `args: 185`, `func_start: 162`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 145`, `duplicate_logic: 92`
* *Architecture:* `io: 1`, `api: 110`, `import: 9`
* *Defense:* `safety: 49`, `doc: 194`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pyarrow._compute, pyarrow.compute, issue, pyarrow.lib, pyarrow.parquet, pyarrow.dataset, pyarrow.substrait, pyarrow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_flight.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.825 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 11.825, file_cluster_0: 11.888, file_cluster_7: 11.967
- **Magnitude:** 948.22 | **LOC:** 3296 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.2632%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 38.6)
  * `__init__` (Impact: 28.6)
    * *Intent:* # Override superclass method to use check_flight_status so we # can generate FlightWriteSizeExceeded...
  * `__init__` (Impact: 26.4)
  * `__init__` (Impact: 25.1)
  * `do_action` (Impact: 19.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 530`, `args: 181`, `func_start: 175`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 10`, `duplicate_logic: 105`
* *Architecture:* `api: 153`, `concurrency: 14`, `import: 11`
* *Defense:* `safety: 120`, `doc: 380`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.463
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007692
  * `Imports (Out-Degree: 0):` enum, pyarrow.lib, warnings, asyncio, re, weakref, collections, time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_parquet.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.325 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.908 IQR)
- **Top Global Matches:** file_cluster_8: 11.325, file_cluster_0: 11.348, file_cluster_7: 11.47
- **Magnitude:** 944.66 | **LOC:** 2422 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.1446%), Tech Debt (99.9976%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 86.9)
  * `from_ordering` (Impact: 37.9)
    * *Intent:* """Offset of data page relative to beginning of the file (int)."""
  * `__cinit__` (Impact: 31.2)
  * `iter_batches` (Impact: 29.1)
  * `read_row_groups` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 397`, `args: 175`, `func_start: 160`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 63`, `dead_code: 1`, `duplicate_logic: 75`
* *Architecture:* `io: 1`, `api: 138`, `import: 4`
* *Defense:* `safety: 39`, `doc: 238`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyarrow.lib, pyarrow.parquet, warnings, textwrap, collections.abc, pyarrow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/io.pxi` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.995 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_8: 11.995, file_cluster_0: 12.115, file_cluster_7: 12.14
- **Magnitude:** 917.46 | **LOC:** 2913 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.8301%), Tech Debt (57.4948%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 363.9)
  * `download` (Impact: 44.4)
  * `upload` (Impact: 32.5)
  * `_download_nothreads` (Impact: 22.6)
  * `read` (Impact: 15.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 319`, `args: 148`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 91`, `fragile_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `io: 6`, `api: 113`, `concurrency: 3`, `import: 10`
* *Defense:* `safety: 72`, `doc: 174`, `test: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyarrow.util, sys, threading, warnings, gzip, io, pyarrow, queue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/src/arrow/python/python_to_arrow.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.347 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.791 IQR)
- **Top Global Matches:** file_cluster_13: 13.347, file_cluster_8: 13.533, file_cluster_11: 13.674
- **Magnitude:** 859.98 | **LOC:** 1306 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7771%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `Convert` (Impact: 52.9)
  * `ConvertPySequence` (Impact: 29.5)
  * `ConvertToSequenceAndInferSize` (Impact: 26.2)
  * `Append` (Impact: 25.3)
  * `Convert` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 165`, `args: 92`, `func_start: 41`, `class_start: 14`
* *Risk/State:* `state_mutation: 411`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 27`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 37`
* *Defense:* `safety: 12`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 56`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inference.h, builder_dict.h, builder_primitive.h, chunked_array.h, sstream, builder_time.h, status.h, numpy_convert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/_compute.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.289 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.387 IQR)
- **Top Global Matches:** file_cluster_8: 11.289, file_cluster_7: 11.507, file_cluster_0: 11.61
- **Magnitude:** 846.88 | **LOC:** 3480 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2333%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 59.2)
  * `_register_user_defined_function` (Impact: 34.4)
  * `cast` (Impact: 25.4)
  * `_set_options` (Impact: 22.0)
    * *Intent:* """ Return all function names in the global registry. """
  * `call` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 512`, `args: 220`, `func_start: 201`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 38`, `planned_debt: 1`, `duplicate_logic: 107`
* *Architecture:* `io: 1`, `api: 134`, `import: 9`
* *Defense:* `safety: 83`, `doc: 212`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sys, pyarrow.lib, warnings, numpy, pyarrow.substrait, pyarrow, pyarrow.util, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.07 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.13 IQR)
- **Top Global Matches:** file_cluster_0: 12.07, file_cluster_8: 12.074, file_cluster_13: 12.517
- **Magnitude:** 840.6 | **LOC:** 2624 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.003%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_array_accepts_pyarrow_scalar_errors` (Impact: 34.6)
  * `test_sequence_timestamp_with_timezone` (Impact: 18.8)
  * `test_struct_from_list_of_pairs_errors` (Impact: 17.8)
  * `test_map_from_dicts` (Impact: 17.0)
  * `test_sequence_numpy_double` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 929`, `args: 149`, `func_start: 149`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 7`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 126`
* *Architecture:* `api: 145`, `import: 21`
* *Defense:* `safety: 462`, `doc: 2`, `test: 710`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, pyarrow.tests.strategies, hypothesis, decimal, gc, math, numpy, pyarrow.pandas_compat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_pandas.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.132 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.132, file_cluster_0: 11.6, file_cluster_7: 11.709
- **Magnitude:** 826.42 | **LOC:** 5320 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_pandas_roundtrip` (Impact: 37.5)
  * `test_timestamp_to_pandas_out_of_bounds` (Impact: 16.9)
  * `_check_array_roundtrip` (Impact: 16.8)
  * `test_integer_byteorder` (Impact: 12.8)
  * `test_arrow_time_to_pandas` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 950`, `args: 311`, `func_start: 311`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 15`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`, `orphaned_logic: 94`
* *Architecture:* `io: 7`, `api: 299`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 384`, `doc: 22`, `test: 734`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` hypothesis.strategies, decimal, gc, json, pandas.tseries.offsets, pyarrow.vendored.version, pytest, hypothesis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/pandas_compat.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.122 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.206 IQR)
- **Top Global Matches:** file_cluster_8: 12.122, file_cluster_13: 12.126, file_cluster_17: 12.163
- **Magnitude:** 776.24 | **LOC:** 1296 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.2325%), Tech Debt (11.0874%)
**Top Internal Functions/Classes:**
  * `dataframe_to_arrays` (Impact: 89.6)
  * `_get_extension_dtypes` (Impact: 77.0)
  * `construct_metadata` (Impact: 55.5)
  * `_reconstruct_columns_from_metadata` (Impact: 36.2)
  * `_add_any_metadata` (Impact: 34.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 179`, `args: 37`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 103`, `dead_code: 5`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 69`, `doc: 24`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.262
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.05698
  * `Imports (Out-Degree: 1):` copy, pandas.core.internals, pyarrow.lib, decimal, ast, pandas, threading, warnings...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_fs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.136 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_8: 12.136, file_cluster_0: 12.186, file_cluster_13: 12.376
- **Magnitude:** 773.44 | **LOC:** 2257 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0542%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_get_file_info_with_selector` (Impact: 32.1)
  * `test_azurefs_options` (Impact: 28.8)
  * `test_s3fs_limited_permissions_create_buc` (Impact: 24.2)
    * *Intent:* # It's an aware UTC datetime
  * `test_s3_options` (Impact: 22.4)
  * `test_open_append_stream` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 605`, `args: 122`, `func_start: 112`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 16`, `planned_debt: 3`, `fragile_debt: 5`
* *Architecture:* `io: 18`, `api: 161`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 381`, `doc: 8`, `test: 558`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.903
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.004274
  * `Imports (Out-Degree: 5):` pyarrow.fs, fsspec.implementations.local, urllib.request, huggingface_hub, pytest, pathlib, time, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/_csv.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.656 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.466 IQR)
- **Top Global Matches:** file_cluster_0: 12.656, file_cluster_8: 13.0, file_cluster_13: 13.054
- **Magnitude:** 722.16 | **LOC:** 1559 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1454%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 57.6)
  * `__init__` (Impact: 26.1)
  * `equals` (Impact: 23.5)
  * `__init__` (Impact: 23.0)
  * `__init__` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 182`, `args: 100`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 203`, `duplicate_logic: 88`
* *Architecture:* `api: 76`, `import: 3`
* *Defense:* `safety: 19`, `doc: 90`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyarrow.lib, collections.abc, pyarrow, collections, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_extension_type.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.116 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.945 IQR)
- **Top Global Matches:** file_cluster_8: 12.116, file_cluster_0: 12.134, file_cluster_13: 12.392
- **Magnitude:** 698.92 | **LOC:** 1970 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tensor_array_from_numpy` (Impact: 51.3)
  * `test_ext_scalar_from_array` (Impact: 25.3)
  * `test_bool8_from_numpy_conversion` (Impact: 15.6)
  * `test_ext_type_as_py` (Impact: 13.6)
  * `test_ext_array_wrap_array` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 726`, `args: 126`, `func_start: 122`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 7`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `io: 5`, `api: 165`, `import: 25`
* *Defense:* `safety: 389`, `doc: 2`, `test: 471`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.216
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.004274
  * `Imports (Out-Degree: 3):` subprocess, pytest, sys, shutil, numpy.lib.stride_tricks, os, pyarrow.parquet, .test_cython...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyarrow-23.0.1/pyarrow/tests/test_types.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.803 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.779 IQR)
- **Top Global Matches:** file_cluster_8: 12.803, file_cluster_0: 13.091, file_cluster_13: 13.116
- **Magnitude:** 644.54 | **LOC:** 1458 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_is_temporal_date_time_timestamp` (Impact: 68.1)
  * `test_struct_type` (Impact: 22.1)
  * `test_bit_and_byte_width` (Impact: 20.8)
  * `test_union_type` (Impact: 20.0)
    * *Intent:* # StructType::GetAllFieldIndices assert ty.get_all_field_indices('a') == [0, 2] def test_union_type(...
  * `test_key_value_metadata` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 519`, `args: 95`, `func_start: 95`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`, `duplicate_logic: 16`, `orphaned_logic: 77`
* *Architecture:* `io: 2`, `api: 94`, `import: 19`
* *Defense:* `safety: 377`, `doc: 10`, `test: 492`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, sys, hypothesis, hypothesis.strategies, hypothesis.extra.pytz, pyarrow.types, pyarrow.tests.strategies, weakref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyarrow-23.0.1/pyarrow/tests/test_csv.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.361 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.811 IQR)
- **Top Global Matches:** file_cluster_8: 11.361, file_cluster_13: 11.838, file_cluster_7: 11.844
- **Magnitude:** 597.46 | **LOC:** 2068 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parse_options` (Impact: 340.5)
  * `test_read_options` (Impact: 32.1)
  * `check_options_class` (Impact: 13.1)
    * *Intent:* """ Check setting and getting attributes of an *Options class. """
  * `make_random_csv` (Impact: 12.0)
  * `test_read_csv_gil_deadlock` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 390`, `args: 107`, `func_start: 102`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 4`, `fragile_debt: 13`, `orphaned_logic: 8`
* *Architecture:* `io: 5`, `api: 110`, `concurrency: 8`, `import: 24`
* *Defense:* `safety: 222`, `doc: 20`, `test: 330`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` select, decimal, gc, pyarrow.tests, abc, pytest, shutil, pyarrow.csv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyarrow-23.0.1/pyarrow/tests/test_convert_builtin.py` (PYTHON) | Magnitude: 840.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1687, structural_boundaries: 929, test: 710, safety: 462
- `pyarrow-23.0.1/pyarrow/tensor.pxi` (PYTHON) | Magnitude: 387.2 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 593, structural_boundaries: 225, doc: 120, branch: 101
- `pyarrow-23.0.1/pyarrow/tests/test_ipc.py` (PYTHON) | Magnitude: 574.52 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 880, structural_boundaries: 360, test: 300, safety: 179
- `pyarrow-23.0.1/pyarrow/_json.pyx` (PYTHON) | Magnitude: 148.12 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 48, state_mutation: 40, branch: 29
- `pyarrow-23.0.1/pyarrow/tests/test_io.py` (PYTHON) | Magnitude: 1075.44 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1388, structural_boundaries: 683, test: 621, safety: 427

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyarrow-23.0.1/pyarrow/src/arrow/python/flight.h` (CPP) | Magnitude: 83.18 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, safety: 61, immutability_locks: 53, state_mutation: 48
- `pyarrow-23.0.1/pyarrow/src/arrow/python/extension_type.cc` (CPP) | Magnitude: 133.2 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 52, structural_boundaries: 36, branch: 23
- `pyarrow-23.0.1/pyarrow/_pyarrow_cpp_tests.pyx` (PYTHON) | Magnitude: 17.84 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, args: 5, api: 5
- `pyarrow-23.0.1/pyarrow/src/arrow/python/common.cc` (CPP) | Magnitude: 203.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 111, branch: 28, structural_boundaries: 28
- `pyarrow-23.0.1/pyarrow/src/arrow/python/helpers.cc` (CPP) | Magnitude: 285.42 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 134, branch: 57, args: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pyarrow-23.0.1/pyarrow/interchange/column.py` (PYTHON) | Magnitude: 94.0 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 66, encapsulation: 50, branch: 40
- `pyarrow-23.0.1/pyarrow/interchange/dataframe.py` (PYTHON) | Magnitude: 67.16 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, encapsulation: 51, structural_boundaries: 36, doc: 28
- `pyarrow-23.0.1/pyarrow/interchange/buffer.py` (PYTHON) | Magnitude: 22.5 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, doc: 14, encapsulation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pyarrow-23.0.1/pyarrow/error.pxi` (PYTHON) | Magnitude: 99.7 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 67, branch: 42, encapsulation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyarrow-23.0.1/pyarrow/tests/test_flight_async.py` (PYTHON) | Magnitude: 54.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 23, test: 17, branch: 10
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` (PYTHON) | Magnitude: 776.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 781, branch: 242, structural_boundaries: 179, encapsulation: 120
- `pyarrow-23.0.1/pyarrow/compat.pxi` (PYTHON) | Magnitude: 20.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, branch: 7, safety: 4
- `pyarrow-23.0.1/pyarrow/builder.pxi` (PYTHON) | Magnitude: 59.26 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 21, doc: 16, branch: 12
- `pyarrow-23.0.1/pyarrow/tests/test_extension_type.py` (PYTHON) | Magnitude: 698.92 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1264, structural_boundaries: 726, test: 471, safety: 389

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

- `pyarrow-23.0.1/pyarrow/memory.pxi` -> **Severity: 5.151** (Embedded: 0.107 * Error Risk: 48.1409%)
- `pyarrow-23.0.1/pyarrow/compute.py` -> **Severity: 4.828** (Embedded: 0.078 * Error Risk: 61.9375%)
- `pyarrow-23.0.1/pyarrow/_azurefs.pyx` -> **Severity: 3.528** (Embedded: 0.0493 * Error Risk: 71.5978%)
- `pyarrow-23.0.1/pyarrow/util.py` -> **Severity: 3.431** (Embedded: 0.0944 * Error Risk: 36.3601%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 3.334** (Embedded: 0.057 * Error Risk: 58.5137%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyarrow-23.0.1/pyarrow/memory.pxi` -> **Severity: 4647.166** (Blast Radius: 55.461 * Doc Risk: 83.7916%)
- `pyarrow-23.0.1/pyarrow/util.py` -> **Severity: 2406.871** (Blast Radius: 34.513 * Doc Risk: 69.7381%)
- `pyarrow-23.0.1/pyarrow/fs.py` -> **Severity: 1434.144** (Blast Radius: 26.534 * Doc Risk: 54.0493%)
- `pyarrow-23.0.1/pyarrow/vendored/version.py` -> **Severity: 938.968** (Blast Radius: 12.229 * Doc Risk: 76.7821%)
- `pyarrow-23.0.1/pyarrow/pandas_compat.py` -> **Severity: 472.235** (Blast Radius: 26.262 * Doc Risk: 17.9817%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
