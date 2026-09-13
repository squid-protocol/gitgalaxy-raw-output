# ARCHITECTURAL_BRIEF: pandas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pandas-dev/pandas.git` |
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
| Total Artifacts | 2632 |
| Analyzed Artifacts (Scanned) | 1897 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 735 |
| Total LOC | 454772 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 72.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4125 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2336 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1957 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 88 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1614 | 443956 | 85.1% |
| HTML | 113 | 6247 | 6.0% |
| XML | 44 | 5 | 2.3% |
| MARKDOWN | 35 | 0 | 1.8% |
| CSV | 25 | 1110 | 1.3% |
| YAML | 23 | 904 | 1.2% |
| C | 12 | 1525 | 0.6% |
| BINARY_THREAT | 11 | 11 | 0.6% |
| JSON | 9 | 250 | 0.5% |
| PLAINTEXT | 4 | 0 | 0.2% |
| CSS | 4 | 529 | 0.2% |
| SHELL | 3 | 235 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1840 | 97.0% |
| Unknown | 11 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 7 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 735*

**Composition by Extension & Reason:**
- `.rst`: 219x Excluded (Unsupported Extension: '.rst')
- `.dta`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 69x Excluded (Explicitly Denied Extension: '.png')
- `.xlsx`: 36x Excluded (Explicitly Denied Extension: '.xlsx')
- `.ods`: 30x Excluded (Explicitly Denied Extension: '.ods')
- `.sas7bdat`: 30x Excluded (Unsupported Extension: '.sas7bdat')
- `.xls`: 26x Excluded (Explicitly Denied Extension: '.xls')
- `.xlsb`: 25x Excluded (Unsupported Extension: '.xlsb')
- `.xlsm`: 25x Excluded (Unsupported Extension: '.xlsm')
- `no_extension`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 5274 LOC), 1x Excluded (Static Asset Blob without Intent: 1037 LOC), 1x Excluded (Static Asset Blob without Intent: 2070 LOC)
- `.c`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 9x Excluded (Unsupported Extension: '.tpl')
- `.pickle`: 9x Excluded (Unsupported Extension: '.pickle')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.8 | 27.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 56.9 | 67.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.0 | 9.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 55.3 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 62.9 | 1.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 70.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6448 | 752 | 10 | `pandas/_libs/include/pandas/skiplist.h` |
| cleanup | 127 | 35 | 0 | `pandas/tests/io/pytables/test_file_handling.py` |
| guards | 28870 | 1168 | 41 | `pandas/tests/dtypes/test_inference.py` |
| danger | 7028 | 640 | 8 | `pandas/tests/computation/test_eval.py` |
| concurrency | 411 | 110 | 0 | `pandas/io/sql.py` |
| connectivity | 31337 | 1502 | 44 | `pandas/tests/extension/test_arrow.py` |
| io | 1227 | 175 | 0 | `pandas/tests/io/data/html/banklist.html` |
| crypto | 1 | 1 | 0 | `pandas/tests/io/pytables/test_store.py` |
| ipc | 52 | 10 | 0 | `pandas/io/clipboard/__init__.py` |
| time | 1033 | 205 | 1 | `pandas/_libs/tslibs/offsets.pyx` |
| serialization | 15 | 9 | 0 | `pandas/tests/copy_view/test_astype.py` |
| regex | 146 | 57 | 0 | `pandas/tests/strings/test_find_replace.py` |
| events | 45 | 13 | 0 | `pandas/tests/io/data/html/banklist.html` |
| tests | 36302 | 1034 | 53 | `pandas/tests/io/test_sql.py` |
| docs | 6400 | 731 | 7 | `pandas/core/indexes/base.py` |
| debt | 1770 | 451 | 3 | `pandas/_libs/tslibs/offsets.pyx` |
| mutation | 267301 | 1599 | 391 | `pandas/core/frame.py` |
| dead_code | 20216 | 1196 | 29 | `pandas/tests/extension/test_arrow.py` |
| credential | 45 | 9 | 0 | `doc/source/_static/schemas/03_subset_rows.svg` |
| threat | 3744 | 550 | 5 | `pandas/io/pytables.py` |
| ml_ai | 8212 | 1445 | 9 | `pandas/core/frame.py` |
| ui | 221 | 40 | 0 | `doc/source/whatsnew/whatsnew_0171_html_table.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pandas/tests/io/data/html/banklist.html` (Hits: 154)
- `pandas/tests/io/test_sql.py` (Hits: 102)
- `web/pandas/index.html` (Hits: 68)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **datetime.csv** (`pandas/tests/io/sas/data/datetime.csv`) — 326 inbound connections
2. **_typing.py** (`pandas/_typing.py`) — 211 inbound connections
3. **common.py** (`pandas/core/dtypes/common.py`) — 182 inbound connections
4. **dtypes.py** (`pandas/core/dtypes/dtypes.py`) — 132 inbound connections
5. **compat.py** (`pandas/_testing/compat.py`) — 114 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **frame.py** (`pandas/core/frame.py`) — 83 outbound dependencies
2. **generic.py** (`pandas/core/generic.py`) — 70 outbound dependencies
3. **series.py** (`pandas/core/series.py`) — 58 outbound dependencies
4. **base.py** (`pandas/core/indexes/base.py`) — 57 outbound dependencies
5. **array.py** (`pandas/core/arrays/arrow/array.py`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `maybe_convert_objects` (@ `pandas/_libs/lib.pyx`) -> Impact: **401.0** | LOC: 384
- `assert_series_equal` (@ `pandas/_testing/asserters.py`) -> Impact: **268.8** | LOC: 285
  * *Intent:* # This could be refactored to use the NDFrame.equals method
- `__new__` (@ `pandas/_libs/tslibs/period.pyx`) -> Impact: **242.5** | LOC: 138
- `__new__` (@ `pandas/_libs/tslibs/timestamps.pyx`) -> Impact: **236.9** | LOC: 168
- `to_latex` (@ `pandas/core/generic.py`) -> Impact: **234.9** | LOC: 286
- `maybe_convert_numeric` (@ `pandas/_libs/lib.pyx`) -> Impact: **218.4** | LOC: 253
- `__cinit__` (@ `pandas/_libs/parsers.pyx`) -> Impact: **217.7** | LOC: 218
- `convert_dtypes` (@ `pandas/core/dtypes/cast.py`) -> Impact: **207.2** | LOC: 184
- `json_normalize` (@ `pandas/io/json/_normalize.py`) -> Impact: **194.3** | LOC: 347
- `get_grouper` (@ `pandas/core/groupby/grouper.py`) -> Impact: **191.8** | LOC: 215

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pandas/core` | 22 | 25770.76 | 42.54% | 11.68% |
| `pandas/_libs` | 57 | 17135.66 | 24.96% | 11.46% |
| `pandas/_libs/tslibs` | 47 | 15798.12 | 17.86% | 10.1% |
| `pandas/tests/frame/methods` | 80 | 15743.28 | 29.33% | 0.0% |
| `pandas/core/arrays` | 20 | 14258.26 | 56.23% | 6.4% |
| `pandas/io` | 16 | 13107.94 | 39.72% | 5.22% |
| `pandas/core/indexes` | 14 | 12898.4 | 44.39% | 11.96% |
| `pandas/tests/frame` | 22 | 11019.12 | 29.57% | 0.0% |
| `pandas/tests/groupby` | 24 | 10636.88 | 34.88% | 0.0% |
| `pandas/tests/io` | 19 | 9285.32 | 24.23% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `asv_bench/benchmarks/categoricals.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/frame_methods.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/index_object.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/io/hdf.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/strftime.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `asv_bench/benchmarks/algorithms.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/algos/isin.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/array.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/attrs_caching.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/categoricals.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pandas/tests/extension/test_arrow.py` -> **238** Orphaned Functions | **0** Duplicates
- `pandas/tests/frame/test_constructors.py` -> **222** Orphaned Functions | **0** Duplicates
- `pandas/tests/tools/test_to_datetime.py` -> **217** Orphaned Functions | **0** Duplicates
- `pandas/tests/indexing/test_loc.py` -> **215** Orphaned Functions | **0** Duplicates
- `pandas/tests/plotting/frame/test_frame.py` -> **172** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10967` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pandas/util/version/__init__.py` (PYTHON) -> Cumulative Risk: **741.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 333.16 | **LOC:** 456 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2394%)
- **Heaviest Functions:** `_cmpkey` (Impact: 42.7), `__init__` (Impact: 34.3), `_parse_letter_version` (Impact: 17.2)

### 2. `asv_bench/benchmarks/gil.py` (PYTHON) -> Cumulative Risk: **723.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 313.36 | **LOC:** 328 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.7778%), Safety Score (95.2355%)
- **Heaviest Functions:** `run_parallel` (Impact: 14.4), `setup` (Impact: 11.6), `inner` (Impact: 11.1)

### 3. `pandas/core/frame.py` (PYTHON) -> Cumulative Risk: **693.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6455.44 | **LOC:** 18736 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 17.6%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.6358%), Churn (90.08%)
- **Heaviest Functions:** `__init__` (Impact: 153.0), `from_records` (Impact: 146.7), `set_index` (Impact: 99.4)

### 4. `pandas/_libs/index.pyx` (PYTHON) -> Cumulative Risk: **691.85**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1103.8 | **LOC:** 1326 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.7513%), Tech Debt (91.5252%)
- **Heaviest Functions:** `get_indexer_non_unique` (Impact: 79.3), `get_indexer_non_unique` (Impact: 42.0), `_get_bool_indexer` (Impact: 25.9)

### 5. `asv_bench/benchmarks/indexing.py` (PYTHON) -> Cumulative Risk: **689.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 573.98 | **LOC:** 585 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `setup` (Impact: 16.9), `setup` (Impact: 6.0), `setup` (Impact: 5.8)

### 6. `pandas/_libs/tslibs/offsets.pyx` (PYTHON) -> Cumulative Risk: **689.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3492.2 | **LOC:** 7801 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 80.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.0275%), Churn (94.26%)
- **Heaviest Functions:** `to_offset` (Impact: 66.8), `_apply` (Impact: 46.4), `wrapper` (Impact: 37.3)

### 7. `pandas/core/arrays/arrow/extension_types.py` (PYTHON) -> Cumulative Risk: **688.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 96.36 | **LOC:** 175 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9921%), Tech Debt (93.0383%)
- **Heaviest Functions:** `__eq__` (Impact: 9.1), `__eq__` (Impact: 7.2), `patch_pyarrow` (Impact: 4.7)

### 8. `asv_bench/benchmarks/series_methods.py` (PYTHON) -> Cumulative Risk: **686.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 443.56 | **LOC:** 428 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9874%)
- **Heaviest Functions:** `setup` (Impact: 13.2), `setup` (Impact: 12.0), `setup` (Impact: 11.1)

### 9. `pandas/core/apply.py` (PYTHON) -> Cumulative Risk: **685.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1692.74 | **LOC:** 2150 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4741%), Api Exposure (81.886%)
- **Heaviest Functions:** `compute_dict_like` (Impact: 46.3), `reconstruct_func` (Impact: 39.6), `wrap_results_dict_like` (Impact: 38.7)

### 10. `asv_bench/benchmarks/algorithms.py` (PYTHON) -> Cumulative Risk: **685.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 238.8 | **LOC:** 211 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2255%)
- **Heaviest Functions:** `setup` (Impact: 28.1), `setup` (Impact: 23.4), `setup` (Impact: 9.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pandas/core/frame.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6455.44 | **LOC:** 18736 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 17.6%
- **Risk Profile:** Cognitive Load (61.832%), Tech Debt (8.5405%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 153.0)
    * *Intent:* # ---------------------------------------------------------------------- # Constructors
  * `from_records` (Impact: 146.7)
  * `set_index` (Impact: 99.4)
  * `select_dtypes` (Impact: 95.1)
    * *Intent:* """ Return a subset of the DataFrame's columns based on the column dtypes. This method allows for fi...
  * `_align_for_op` (Impact: 90.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 718 instances
* *Amplified Sql Injection:* 4 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 2264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 955`, `structural_boundaries: 866`, `args: 293`, `func_start: 291`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 6`, `state_mutation: 828`, `dead_code: 9`, `planned_debt: 12`
* *Architecture:* `io: 2`, `api: 237`, `import: 95`
* *Defense:* `safety: 200`, `doc: 164`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.379
  * `Choke Point (Betweenness):` 0.010105 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` __future__, bodo, collections, collections.abc, dataclasses, datetime, functools, io...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pandas/core/generic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5149.68 | **LOC:** 12805 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (66.3773%), Tech Debt (8.6273%)
**Top Internal Functions/Classes:**
  * `to_latex` (Impact: 234.9)
  * `replace` (Impact: 185.5)
  * `fillna` (Impact: 127.1)
  * `_where` (Impact: 125.0)
  * `_rename` (Impact: 99.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 549 instances
* *State Mutation (weighted view):* 1711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 679`, `args: 227`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 613`, `dead_code: 10`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 162`, `import: 69`
* *Defense:* `safety: 117`, `doc: 115`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.08
  * `Choke Point (Betweenness):` 0.003191 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` __future__, adbc_driver_sqlite, collections, collections.abc, copy, datetime, functools, json...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pandas/io/pytables.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5048.88 | **LOC:** 5600 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (55.7885%), Tech Debt (22.2133%)
**Top Internal Functions/Classes:**
  * `_create_axes` (Impact: 108.2)
  * `read` (Impact: 76.1)
  * `_create_storer` (Impact: 75.9)
  * `_maybe_convert_for_string_atom` (Impact: 72.8)
  * `read_hdf` (Impact: 70.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 712 instances
* *State Mutation (weighted view):* 2284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 703`, `args: 245`, `func_start: 239`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 860`, `dead_code: 29`, `planned_debt: 17`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 7`, `api: 200`, `import: 41`
* *Defense:* `safety: 178`, `doc: 146`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` __future__, collections.abc, contextlib, copy, datetime, itertools, numpy, os...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4925.96 | **LOC:** 8145 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (39.7256%), Tech Debt (11.3012%)
**Top Internal Functions/Classes:**
  * `join` (Impact: 96.2)
  * `_join_level` (Impact: 85.7)
  * `__new__` (Impact: 82.1)
    * *Intent:* # -------------------------------------------------------------------- # Constructors
  * `get_values_for_csv` (Impact: 66.3)
  * `set_names` (Impact: 65.3)
    * *Intent:* """ Set Index or MultiIndex name. Able to set new names partially and by level. Parameters ---------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 605 instances
* *State Mutation (weighted view):* 1910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 980`, `structural_boundaries: 914`, `args: 235`, `func_start: 235`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 700`, `dead_code: 13`, `planned_debt: 25`, `fragile_debt: 1`
* *Architecture:* `api: 132`, `import: 74`
* *Defense:* `safety: 232`, `doc: 165`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.347
  * `Choke Point (Betweenness):` 0.002747 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` __future__, collections, collections.abc, copy, datetime, for, functools, itertools...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `pandas/_libs/tslibs/offsets.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3492.2 | **LOC:** 7801 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 80.7%
- **Risk Profile:** Cognitive Load (47.5726%), Tech Debt (79.2787%)
**Top Internal Functions/Classes:**
  * `to_offset` (Impact: 66.8)
    * *Intent:* """ Return DateOffset object from string or datetime.timedelta object. Parameters ---------- freq : ...
  * `_apply` (Impact: 46.4)
    * *Intent:* # used for detecting edge condition nanosecond = getattr(other, "nanosecond", 0) # reset timezone an...
  * `wrapper` (Impact: 37.3)
    * *Intent:* # Note: normally we would use `@functools.wraps(func)`, but this does # not play nicely with cython ...
  * `_next_opening_time` (Impact: 37.1)
    * *Intent:* """ If self._n and sign have the same sign, return the earliest opening time later than or equal to ...
  * `__init__` (Impact: 36.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 435 instances
* *State Mutation (weighted view):* 1642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 680`, `args: 243`, `func_start: 243`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 772`, `dead_code: 6`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 103`, `import: 23`
* *Defense:* `safety: 64`, `doc: 150`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .timedeltas, .timestamps, datetime, dateutil.easter, dateutil.relativedelta, numpy, pandas._libs.properties, pandas._libs.tslibs.ccalendar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/arrays/arrow/array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3201.04 | **LOC:** 3440 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (74.5346%), Tech Debt (12.1433%)
**Top Internal Functions/Classes:**
  * `_reduce_pyarrow` (Impact: 112.6)
    * *Intent:* """ Return a pyarrow scalar result of performing the reduction operation. Parameters ---------- name...
  * `_box_pa_array` (Impact: 96.9)
  * `to_numpy` (Impact: 64.5)
  * `__getitem__` (Impact: 60.2)
    * *Intent:* """Select a subset of self. Parameters ---------- item : int, slice, or ndarray * int: The position ...
  * `_evaluate_op_method` (Impact: 55.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 447 instances
* *State Mutation (weighted view):* 1459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 693`, `args: 180`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 565`, `dead_code: 2`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 124`, `import: 60`
* *Defense:* `safety: 103`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.000909 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` __future__, collections.abc, datetime, functools, numpy, operator, pandas, pandas._config...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/io/stata.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3119.36 | **LOC:** 3939 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (49.8365%), Tech Debt (10.5106%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 141.7)
  * `_cast_to_stata_types` (Impact: 64.3)
    * *Intent:* """ Checks the dtypes of the columns of a pandas DataFrame for compatibility with the data types and...
  * `_datetime_to_stata_elapsed_vec` (Impact: 47.3)
    * *Intent:* """ Convert from datetime to SIF. https://www.stata.com/help.cgi?datetime Parameters ---------- date...
  * `_read_old_header` (Impact: 46.1)
  * `_do_convert_categoricals` (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 517 instances
* *State Mutation (weighted view):* 1682
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 391`, `args: 132`, `func_start: 130`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 648`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 30`, `import: 29`
* *Defense:* `safety: 43`, `doc: 72`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.507
  * `Choke Point (Betweenness):` 0.000816 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, collections, collections.abc, datetime, io, numpy, os, pandas...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/multi.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3113.4 | **LOC:** 4847 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (43.8726%), Tech Debt (11.8125%)
**Top Internal Functions/Classes:**
  * `_get_loc_level` (Impact: 97.4)
    * *Intent:* """ get_loc_level but with `level` known to be positional, not name-based. """
  * `_get_level_indexer` (Impact: 74.9)
  * `_reorder_indexer` (Impact: 60.4)
    * *Intent:* # --------------------------------------------------------------------
  * `get_locs` (Impact: 57.1)
    * *Intent:* """ Get location for a sequence of labels. This method returns the integer positions in the index th...
  * `_verify_integrity` (Impact: 53.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 442 instances
* *State Mutation (weighted view):* 1416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 552`, `structural_boundaries: 445`, `args: 118`, `func_start: 118`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 532`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 85`, `import: 38`
* *Defense:* `safety: 103`, `doc: 86`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.000375 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` __future__, collections.abc, copy, functools, itertools, numpy, pandas, pandas._config...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/tests/extension/test_arrow.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3109.48 | **LOC:** 3952 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 38.1%
- **Risk Profile:** Cognitive Load (44.0854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_cast_pointwise_result` (Impact: 90.3)
    * *Intent:* # TODO: use EA._cast_pointwise_result, same with other test files that # override this # BaseOpsUtil...
  * `test_quantile` (Impact: 57.2)
  * `_get_expected_reduction_dtype` (Impact: 46.6)
  * `_supports_reduction` (Impact: 40.1)
  * `_get_arith_xfail_marker` (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 311 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 556`, `args: 255`, `func_start: 251`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 908`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 1`, `unreferenced_by_name: 238`
* *Architecture:* `io: 1`, `api: 244`, `import: 24`
* *Defense:* `safety: 118`, `doc: 8`, `test: 417`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, datetime, decimal, io, numpy, operator, pandas, pandas._libs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_sql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2918.1 | **LOC:** 4399 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (28.5273%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func` (Impact: 19.9)
  * `test_api_timedelta` (Impact: 17.8)
    * *Intent:* # see #6921 conn_name = conn conn = request.getfixturevalue(conn) if sql.has_table("test_timedelta",...
  * `get_all_views` (Impact: 16.7)
  * `get_all_tables` (Impact: 16.7)
  * `test_read_sql_dtype_backend_table` (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 347 instances
* *Amplified Sql Injection:* 14 instances
* *State Mutation (weighted view):* 1494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 1015`, `args: 220`, `func_start: 215`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 800`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 145`
* *Architecture:* `io: 102`, `api: 217`, `import: 82`
* *Defense:* `safety: 306`, `doc: 21`, `test: 485`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, adbc_driver_manager, adbc_driver_postgresql, adbc_driver_sqlite, contextlib, csv, datetime, decimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/_libs/lib.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2622.88 | **LOC:** 3326 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (72.5813%), Tech Debt (17.9406%)
**Top Internal Functions/Classes:**
  * `maybe_convert_objects` (Impact: 401.0)
  * `maybe_convert_numeric` (Impact: 218.4)
  * `infer_dtype` (Impact: 117.4)
    * *Intent:* """ Return a string label of the type of the elements in a list-like input. This method inspects the...
  * `generate_bins_dt64` (Impact: 43.2)
    * *Intent:* # ------------------------------------------------------------------------------ # Groupby-related f...
  * `array_equivalent_object` (Impact: 37.8)
    * *Intent:* """ Perform an element by element comparison on N-d object arrays taking into account nan positions....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 342 instances
* *State Mutation (weighted view):* 1069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 427`, `args: 112`, `func_start: 112`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 385`, `dead_code: 3`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 47`, `import: 27`
* *Defense:* `safety: 53`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` collections, datetime, decimal, enum, for, fractions, isn, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/frame/test_constructors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2614.84 | **LOC:** 3382 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (42.2255%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dict_nocopy` (Impact: 46.6)
  * `test_constructor_data_aware_dtype_naive` (Impact: 19.6)
    * *Intent:* # GH#25843, GH#41555, GH#33401 tz = tz_aware_fixture ts = Timestamp("2019", tz=tz) if pydt: ts = ts....
  * `test_constructor_error_msgs` (Impact: 18.5)
  * `test_constructor_mixed_dtypes` (Impact: 17.1)
  * `constructor` (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 1417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 630`, `args: 252`, `func_start: 232`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 883`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 4`, `unreferenced_by_name: 222`
* *Architecture:* `api: 238`, `import: 22`
* *Defense:* `safety: 234`, `test: 348`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` array, collections, collections.abc, dataclasses, datetime, functools, numpy, numpy.dtypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/_libs/groupby.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2499.5 | **LOC:** 2347 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (63.2265%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `group_sum` (Impact: 129.1)
  * `group_quantile` (Impact: 103.9)
  * `group_var` (Impact: 98.6)
  * `group_mean` (Impact: 95.6)
  * `group_cummin_max` (Impact: 81.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 112`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 362`, `dead_code: 2`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 11`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, pandas._libs.algos
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/series.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2452.5 | **LOC:** 9949 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 20.4%
- **Risk Profile:** Cognitive Load (43.4122%), Tech Debt (8.7536%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 155.7)
    * *Intent:* # ---------------------------------------------------------------------- # Constructors
  * `reset_index` (Impact: 44.5)
  * `sort_values` (Impact: 42.6)
  * `_flex_method` (Impact: 36.3)
  * `case_when` (Impact: 33.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 232 instances
* *State Mutation (weighted view):* 776
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 533`, `args: 180`, `func_start: 179`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 312`, `dead_code: 4`, `planned_debt: 6`
* *Architecture:* `io: 3`, `api: 158`, `import: 59`
* *Defense:* `safety: 78`, `doc: 127`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.378
  * `Choke Point (Betweenness):` 0.002906 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` __future__, collections, collections.abc, functools, io, numpy, operator, pandas._libs...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `pandas/tests/indexing/test_loc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2438.22 | **LOC:** 3601 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (41.1716%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loc_iloc_getitem_leading_ellipses` (Impact: 25.1)
  * `test_loc_getitem_listlike_of_datetimelike_keys` (Impact: 19.3)
    * *Intent:* # GH#11497 idx = date_range("2011-01-01", "2011-01-02", freq="D", name="idx") if to_period: idx = id...
  * `test_loc_setitem_with_expansion_nonunique_index` (Impact: 18.5)
    * *Intent:* # GH#40096 if not len(index): pytest.skip("Not relevant for empty Index") index = index.repeat(2) # ...
  * `test_loc_iloc_getitem_ellipses_only_one_ellipsis` (Impact: 16.9)
    * *Intent:* # GH37750 key = 0 if (indexer is tm.iloc or len(obj) == 0) else obj.index[0] with pytest.raises(Inde...
  * `test_loc_setitem_str_to_small_float_conversion_type` (Impact: 15.0)
    * *Intent:* # GH#20388 col_data = [str(np.random.default_rng(2).random() * 1e-12) for _ in range(5)] result = Da...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 1409
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 427`, `args: 261`, `func_start: 220`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1005`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 215`
* *Architecture:* `api: 232`, `import: 17`
* *Defense:* `safety: 72`, `doc: 2`, `test: 361`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` collections, contextlib, datetime, dateutil.tz, numpy, pandas, pandas._libs, pandas._testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/reshape/merge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2435.58 | **LOC:** 3139 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 11.8%
- **Risk Profile:** Cognitive Load (65.3648%), Tech Debt (11.2785%)
**Top Internal Functions/Classes:**
  * `_maybe_coerce_merge_keys` (Impact: 118.5)
    * *Intent:* # we have valid merges but we may have to further # coerce these if they are originally incompatible...
  * `_maybe_add_join_keys` (Impact: 108.7)
  * `_factorize_keys` (Impact: 95.3)
  * `_validate_left_right_on` (Impact: 86.0)
  * `_validate_left_right_on` (Impact: 76.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 369 instances
* *State Mutation (weighted view):* 1163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 250`, `args: 59`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 425`, `dead_code: 10`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 37`
* *Defense:* `safety: 79`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.274
  * `Choke Point (Betweenness):` 0.000697 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` __future__, collections.abc, datetime, functools, numpy, pandas, pandas._libs, pandas._libs.lib...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/groupby/groupby.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2432.76 | **LOC:** 6037 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 20.8%
- **Risk Profile:** Cognitive Load (45.9737%), Tech Debt (9.8701%)
**Top Internal Functions/Classes:**
  * `quantile` (Impact: 91.4)
  * `_value_counts` (Impact: 67.0)
  * `shift` (Impact: 51.2)
  * `apply` (Impact: 45.0)
    * *Intent:* # ----------------------------------------------------------------- # apply/agg/transform """ Apply ...
  * `_concat_objects` (Impact: 38.9)
    * *Intent:* # ----------------------------------------------------------------- # Dispatch/Wrapping
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 320 instances
* *State Mutation (weighted view):* 1040
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 402`, `args: 116`, `func_start: 102`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 400`, `dead_code: 7`, `planned_debt: 10`
* *Architecture:* `io: 1`, `api: 76`, `import: 56`
* *Defense:* `safety: 65`, `doc: 65`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.971
  * `Choke Point (Betweenness):` 0.001193 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` __future__, collections.abc, datetime, functools, numpy, pandas._libs, pandas._libs.algos, pandas._libs.groupby...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pandas/plotting/_matplotlib/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2427.52 | **LOC:** 2222 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (73.5269%), Tech Debt (33.9335%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 160.0)
  * `_validate_color_args` (Impact: 50.0)
  * `_parse_errorbars` (Impact: 49.4)
    * *Intent:* # TODO: tighter typing for first return?
  * `_make_plot` (Impact: 40.2)
  * `_adorn_subplots` (Impact: 37.9)
    * *Intent:* """Common post process unrelated to data"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 320`, `args: 106`, `func_start: 106`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 413`, `dead_code: 8`, `planned_debt: 26`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `import: 34`
* *Defense:* `safety: 57`, `doc: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.257
  * `Choke Point (Betweenness):` 0.002126 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` __future__, abc, collections.abc, matplotlib, matplotlib.artist, matplotlib.axes, matplotlib.axis, matplotlib.figure...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `pandas/_libs/window/aggregations.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2415.06 | **LOC:** 2119 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (61.3262%), Tech Debt (8.668%)
**Top Internal Functions/Classes:**
  * `roll_rank` (Impact: 98.7)
  * `ewmcov` (Impact: 97.7)
  * `roll_quantile` (Impact: 93.2)
  * `ewm` (Impact: 90.2)
    * *Intent:* # ---------------------------------------------------------------------- # Exponentially weighted mo...
  * `_roll_min_max` (Impact: 81.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 414 instances
* *State Mutation (weighted view):* 1271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 95`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 443`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cython, numpy, pandas._libs.algos
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/groupby/test_groupby.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2329.54 | **LOC:** 3020 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (43.8378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_groupby` (Impact: 116.4)
    * *Intent:* # GH8093 & GH26411 override_dtype = None if isinstance(values, BooleanArray) and op in ["sum", "prod...
  * `test_omit_nuisance_agg` (Impact: 26.1)
    * *Intent:* # GH 38774, GH 38815 grouped = df.groupby("A") no_drop_nuisance = ("var", "std", "sem", "mean", "pro...
  * `test_len_categorical` (Impact: 23.0)
    * *Intent:* # GH#57595 df = DataFrame( { "a": Categorical([1, 1, 2, np.nan], categories=[1, 2, 3]), "b": Categor...
  * `test_groups_sort_dropna` (Impact: 18.7)
    * *Intent:* # GH#56966, GH#56851 df = DataFrame([[2.0, 1.0], [np.nan, 4.0], [0.0, 3.0]]) keys = [(2.0, 1.0), (np...
  * `test_indices_concatenation_order` (Impact: 13.7)
    * *Intent:* # GH 2808 def f1(x): y = x[(x.b % 2) == 1] ** 2 if y.empty: multiindex = MultiIndex(levels=[[]] * 2,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 1400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 367`, `args: 214`, `func_start: 169`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 834`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 146`
* *Architecture:* `io: 1`, `api: 161`, `import: 13`
* *Defense:* `safety: 106`, `doc: 1`, `test: 233`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, decimal, numpy, pandas, pandas._testing, pandas.core.arrays, pandas.core.common, pandas.errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/internals/managers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2265.6 | **LOC:** 2557 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (50.1648%), Tech Debt (19.258%)
**Top Internal Functions/Classes:**
  * `_slice_take_blocks_ax0` (Impact: 86.3)
  * `iset` (Impact: 71.1)
  * `reindex_indexer` (Impact: 46.3)
  * `as_array` (Impact: 46.2)
  * `setitem` (Impact: 38.8)
    * *Intent:* """ Set values with indexer. For SingleBlockManager, this backs s[indexer] = value """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 348 instances
* *State Mutation (weighted view):* 1117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 382`, `args: 132`, `func_start: 130`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 421`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 2`
* *Architecture:* `api: 100`, `import: 30`
* *Defense:* `safety: 44`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.626
  * `Choke Point (Betweenness):` 0.000328 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` __future__, collections.abc, itertools, numpy, pandas._config.config, pandas._libs, pandas._libs.internals, pandas._libs.tslibs...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/_libs/parsers.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2103.22 | **LOC:** 2183 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (69.5573%), Tech Debt (9.018%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 217.7)
  * `_try_double_nogil` (Impact: 108.2)
  * `_convert_with_dtype` (Impact: 108.0)
  * `_get_header` (Impact: 107.5)
    * *Intent:* # header is now a list of lists, so field_count should use header[0] # # modifies: # self.parser att...
  * `_convert_tokens` (Impact: 70.8)
    * *Intent:* # -> tuple["ArrayLike", int]:
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 177`, `args: 51`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 330`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 9`, `import: 15`
* *Defense:* `safety: 46`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` collections, csv, numpy, pandas, pandas._config, pandas._libs, pandas.core.arrays, pandas.core.arrays.boolean...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/indexing.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2059.0 | **LOC:** 3434 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 17.6%
- **Risk Profile:** Cognitive Load (48.6727%), Tech Debt (13.4703%)
**Top Internal Functions/Classes:**
  * `_align_series` (Impact: 96.5)
  * `_setitem_with_indexer_split_path` (Impact: 80.4)
    * *Intent:* """ Setitem column-wise. """
  * `_convert_to_indexer` (Impact: 58.0)
    * *Intent:* """ Convert indexing key into something we can use to do actual fancy indexing on an ndarray. Exampl...
  * `_align_frame` (Impact: 48.4)
  * `_setitem_with_indexer_missing` (Impact: 44.4)
    * *Intent:* """ Insert new row(s) or column(s) into the Series or DataFrame. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 480`, `structural_boundaries: 340`, `args: 85`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 289`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 3`, `api: 17`, `import: 30`
* *Defense:* `safety: 129`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.376
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` __future__, collections.abc, contextlib, numpy, pandas, pandas._libs.indexing, pandas._libs.lib, pandas._typing...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pandas/tests/arithmetic/test_timedelta64.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2009.56 | **LOC:** 2332 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (30.4533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_td64arr_div_numeric_array` (Impact: 29.4)
  * `test_subtraction_ops_with_tz` (Impact: 28.4)
    * *Intent:* # check that dt/dti subtraction ops with tz are validated dti = pd.date_range("20130101", periods=3)...
  * `test_td64arr_add_sub_datetimelike_scalar` (Impact: 24.5)
    * *Intent:* # ------------------------------------------------------------- # Binary operations td64 arraylike a...
  * `test_td64arr_mod_tdscalar` (Impact: 19.6)
    * *Intent:* # ------------------------------------------------------------------ # mod, divmod # TODO: operation...
  * `test_timedelta_ops_with_missing_values` (Impact: 14.5)
    * *Intent:* # TODO: moved from tests.indexes.timedeltas.test_arithmetic; needs # parametrization+de-duplication ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 1263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 287`, `args: 92`, `func_start: 88`, `class_start: 7`
* *Risk/State:* `state_mutation: 745`, `planned_debt: 13`, `fragile_debt: 1`, `unreferenced_by_name: 85`
* *Architecture:* `api: 94`, `import: 12`
* *Defense:* `safety: 62`, `doc: 1`, `test: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` datetime, numpy, pandas, pandas._libs.tslibs, pandas._testing, pandas.compat, pandas.core.arrays, pandas.errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_stata.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2006.78 | **LOC:** 2629 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (27.787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_compression` (Impact: 36.8)
  * `test_big_dates` (Impact: 19.6)
  * `test_categorical_order` (Impact: 13.7)
    * *Intent:* # Directly construct using expected codes # Format is is_cat, col_name, labels (in order), underlyin...
  * `test_stata_compression` (Impact: 13.4)
  * `test_write_variable_label_errors` (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 1254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 350`, `args: 118`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 740`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 111`
* *Architecture:* `io: 15`, `api: 116`, `import: 21`
* *Defense:* `safety: 60`, `doc: 4`, `test: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bz2, datetime, gzip, io, itertools, numpy, os, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pandas/_libs/tslibs/offsets.pyx` -> Churn: **94.26%** | Cog Load: 47.5726% | Debt: 79.2787%
- `pandas/core/frame.py` -> Churn: **90.08%** | Cog Load: 61.832% | Debt: 8.5405%
- `pandas/core/generic.py` -> Churn: **82.8%** | Cog Load: 66.3773% | Debt: 8.6273%
- `pandas/core/arrays/arrow/array.py` -> Churn: **70.12%** | Cog Load: 74.5346% | Debt: 12.1433%
- `pandas/_libs/tslibs/timedeltas.pyx` -> Churn: **64.77%** | Cog Load: 68.9339% | Debt: 13.0821%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pandas/_libs/tslibs/offsets.pyx` -> **Tuhin Sharma** (80.7% isolated ownership) | Magnitude: 3492.2
- `pandas/tests/arithmetic/test_timedelta64.py` -> **jbrockmendel** (90.0% isolated ownership) | Magnitude: 2009.56
- `pandas/tests/arithmetic/test_datetime64.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 1782.62
- `pandas/tests/frame/test_stack_unstack.py` -> **Álvaro Kothe** (100.0% isolated ownership) | Magnitude: 1726.86
- `pandas/tests/plotting/test_datetimelike.py` -> **jbrockmendel** (87.5% isolated ownership) | Magnitude: 1253.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pandas/core/frame.py` -> **Severity: 1.01** (Bridge: 0.0101 * Flux: 100.0%)
- `pandas/_typing.py` -> **Severity: 0.846** (Bridge: 0.0204 * Flux: 41.5116%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 0.472** (Bridge: 0.0047 * Flux: 100.0%)
- `pandas/core/dtypes/common.py` -> **Severity: 0.416** (Bridge: 0.0042 * Flux: 99.7492%)
- `pandas/util/_test_decorators.py` -> **Severity: 0.352** (Bridge: 0.0035 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pandas/_typing.py` -> **Severity: 6349.1** (Blast Radius: 63.491 * Doc Risk: 100.0%)
- `pandas/util/_decorators.py` -> **Severity: 2186.96** (Blast Radius: 27.337 * Doc Risk: 80.0%)
- `pandas/core/dtypes/generic.py` -> **Severity: 1574.2** (Blast Radius: 15.742 * Doc Risk: 100.0%)
- `pandas/core/generic.py` -> **Severity: 1406.57** (Blast Radius: 20.08 * Doc Risk: 70.0483%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 1147.173** (Blast Radius: 22.831 * Doc Risk: 50.2463%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
