# ARCHITECTURAL_BRIEF: pandas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pandas` |
| **Timestamp** | `2026-08-03T21:18:36.093406+00:00` |
| **Scan Duration** | `12.04s` |
| **Git Branch** | `main` |
| **Git Commit** | `7629c655b22b998dd86bf98c2f1c721998e9e4f1` |
| **Git Remote** | `https://github.com/pandas-dev/pandas.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1588 malicious artifacts.

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
| Total Artifacts | 2632 |
| Analyzed Artifacts (Scanned) | 1817 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 815 |
| Total LOC | 441595 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 69.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4147 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2424 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2038 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 86 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1574 | 432800 | 86.6% |
| HTML | 111 | 6153 | 6.1% |
| XML | 44 | 5 | 2.4% |
| CSV | 25 | 1110 | 1.4% |
| MARKDOWN | 18 | 0 | 1.0% |
| YAML | 14 | 509 | 0.8% |
| BINARY_THREAT | 11 | 11 | 0.6% |
| JSON | 9 | 245 | 0.5% |
| PLAINTEXT | 4 | 0 | 0.2% |
| CSS | 4 | 529 | 0.2% |
| SHELL | 3 | 233 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.896`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1435 | 79.0% |
| file_cluster_13 | 242 | 13.3% |
| file_cluster_0 | 49 | 2.7% |
| file_cluster_16 | 48 | 2.6% |
| Unknown | 11 | 0.6% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_17 | 1 | 0.1% |
| file_cluster_2 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 1.2% |
| Static: Minified & Vendor Opaque Mass | 7 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 815*

**Composition by Extension & Reason:**
- `.rst`: 218x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dta`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 69x Excluded (Explicitly Denied Extension: '.png')
- `.xlsx`: 36x Excluded (Explicitly Denied Extension: '.xlsx')
- `.py`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ods`: 30x Excluded (Explicitly Denied Extension: '.ods')
- `.sas7bdat`: 30x Excluded (Unsupported Extension: '.sas7bdat')
- `.xls`: 26x Excluded (Explicitly Denied Extension: '.xls')
- `.xlsb`: 25x Excluded (Unsupported Extension: '.xlsb')
- `.xlsm`: 25x Excluded (Unsupported Extension: '.xlsm')
- `no_extension`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 5274 LOC), 1x Excluded (Static Asset Blob without Intent: 1037 LOC), 1x Excluded (Static Asset Blob without Intent: 2070 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 4.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.6 | 5.1 | 5.2 | 0.0 |
| Concurrency Exposure | 0.0 | 99.9 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 62.9 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.5 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 53.4 | 69.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pandas/tests/io/data/html/banklist.html` (Hits: 154)
- `pandas/tests/io/test_sql.py` (Hits: 102)
- `web/pandas/index.html` (Hits: 68)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **datetime.csv** (`pandas/tests/io/sas/data/datetime.csv`) — 318 inbound connections
2. **_typing.py** (`pandas/_typing.py`) — 202 inbound connections
3. **common.py** (`pandas/core/dtypes/common.py`) — 176 inbound connections
4. **dtypes.py** (`pandas/core/dtypes/dtypes.py`) — 130 inbound connections
5. **compat.py** (`pandas/_testing/compat.py`) — 110 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **frame.py** (`pandas/core/frame.py`) — 83 outbound dependencies
2. **generic.py** (`pandas/core/generic.py`) — 70 outbound dependencies
3. **series.py** (`pandas/core/series.py`) — 58 outbound dependencies
4. **base.py** (`pandas/core/indexes/base.py`) — 57 outbound dependencies
5. **array.py** (`pandas/core/arrays/arrow/array.py`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `select_dtypes` (@ `pandas/core/frame.py`) -> Impact: **8951.3** | LOC: 4026
- `to_csv` (@ `pandas/core/generic.py`) -> Impact: **5832.4** | LOC: 1003
- `__cinit__` (@ `pandas/_libs/parsers.pyx`) -> Impact: **5726.2** | LOC: 1037
- `sql_strings` (@ `pandas/tests/io/test_sql.py`) -> Impact: **4244.3** | LOC: 2440
- `__init__` (@ `pandas/io/stata.py`) -> Impact: **2616.4** | LOC: 1164
  * *Intent:* # off - int32 array (n elements)
- `get_engine` (@ `pandas/io/sql.py`) -> Impact: **2333.0** | LOC: 1020
- `where` (@ `pandas/core/internals/blocks.py`) -> Impact: **2277.7** | LOC: 1033
  * *Intent:* -------
- `shift` (@ `pandas/core/indexes/base.py`) -> Impact: **1811.4** | LOC: 1188
- `has_info_repr` (@ `pandas/tests/io/formats/test_format.py`) -> Impact: **1763.9** | LOC: 1330
- `_validate_sort_keyword` (@ `pandas/core/indexes/base.py`) -> Impact: **1640.8** | LOC: 566

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__floordiv__` (@ `pandas/_libs/tslibs/timedeltas.pyx`) -> **O(2^N) [Recursive]**
- `__rfloordiv__` (@ `pandas/_libs/tslibs/timedeltas.pyx`) -> **O(2^N) [Recursive]**
- `astype` (@ `pandas/core/arrays/categorical.py`) -> **O(2^N) [Recursive]**
- `_maybe_convert_setitem_value` (@ `pandas/core/arrays/string_arrow.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Fall back for types where PyArrow's string representation
- `_align_core` (@ `pandas/core/computation/align.py`) -> **O(2^N) [Recursive]**
- `create_valid_python_identifier` (@ `pandas/core/computation/parsing.py`) -> **O(2^N) [Recursive]**
- `select_dtypes` (@ `pandas/core/frame.py`) -> **O(2^N) [Recursive]**
- `to_csv` (@ `pandas/core/generic.py`) -> **O(2^N) [Recursive]**
- `asof` (@ `pandas/core/generic.py`) -> **O(2^N) [Recursive]**
- `size` (@ `pandas/core/groupby/groupby.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `sql_strings` (@ `pandas/tests/io/test_sql.py`) -> DB Complexity: **206**
- `__init__` (@ `pandas/io/stata.py`) -> DB Complexity: **113**
  * *Intent:* # off - int32 array (n elements)
- `test_sqlite_type_mapping` (@ `pandas/tests/io/test_sql.py`) -> DB Complexity: **92**
  * *Intent:* # GH 37157 conn_name = conn if conn_name == "sqlite_buildin": request.applymarker(pytest.mark.xfail(reason="Not Implemented")) conn = request.getfixtu...
- `_add_redirects` (@ `doc/make.py`) -> DB Complexity: **81**
- `Anonymous_Block_[Truncated]` (@ `ci/code_checks.sh`) -> DB Complexity: **59**
- `get_engine` (@ `pandas/io/sql.py`) -> DB Complexity: **56**
- `__cinit__` (@ `pandas/_libs/parsers.pyx`) -> DB Complexity: **47**
- `_verify_integrity` (@ `pandas/core/internals/managers.py`) -> DB Complexity: **43**
- `test_get_engine_auto_error_message` (@ `pandas/tests/io/test_parquet.py`) -> DB Complexity: **39**
- `setup_method` (@ `pandas/tests/test_nanops.py`) -> DB Complexity: **36**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pandas/core` | 22 | 30421.26 | 13.6% | 47.75% |
| `pandas/tests/io/xml` | 4 | 17307.72 | 3.13% | 0.0% |
| `pandas/core/indexes` | 14 | 16015.3 | 14.76% | 25.6% |
| `pandas/core/arrays` | 20 | 13774.46 | 15.57% | 19.31% |
| `pandas/_libs` | 52 | 13228.45 | 12.68% | 23.61% |
| `pandas/tests/frame/methods` | 80 | 12325.88 | 4.23% | 0.0% |
| `pandas/io` | 16 | 11777.24 | 14.02% | 28.41% |
| `pandas/tests/io` | 17 | 11578.86 | 4.08% | 0.0% |
| `pandas/tests/frame` | 21 | 9385.84 | 5.5% | 0.0% |
| `asv_bench/benchmarks` | 39 | 9035.78 | 41.4% | 92.19% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `asv_bench/benchmarks/algorithms.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/algos/isin.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/arithmetic.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/array.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/attrs_caching.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `asv_bench/benchmarks/attrs_caching.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/index_cached_properties.py` -> **100.0%** Exposure
- `pandas/util/_decorators.py` -> **100.0%** Exposure
- `pandas/util/version/__init__.py` -> **100.0%** Exposure
- `ci/run_tests.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pandas/tests/indexing/test_loc.py` -> **204** Orphaned Functions | **13** Duplicates
- `pandas/tests/extension/test_arrow.py` -> **178** Orphaned Functions | **4** Duplicates
- `asv_bench/benchmarks/frame_methods.py` -> **115** Orphaned Functions | **39** Duplicates
- `pandas/tests/series/test_constructors.py` -> **146** Orphaned Functions | **6** Duplicates
- `pandas/tests/groupby/test_groupby.py` -> **146** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pandas/tests/strings/test_find_replace.py`** -> AI Confidence: **99.39%**
2. **`pandas/_libs/parsers.pyx`** -> AI Confidence: **99.35%**
3. **`pandas/_libs/tslibs/strptime.pyx`** -> AI Confidence: **99.34%**
4. **`pandas/_libs/window/aggregations.pyx`** -> AI Confidence: **99.32%**
5. **`doc/make.py`** -> AI Confidence: **99.31%**
6. **`doc/source/conf.py`** -> AI Confidence: **99.31%**
7. **`pandas/_config/config.py`** -> AI Confidence: **99.31%**
8. **`pandas/_libs/internals.pyx`** -> AI Confidence: **99.31%**
9. **`pandas/_libs/tslibs/offsets.pyx`** -> AI Confidence: **99.31%**
10. **`pandas/_libs/tslibs/parsing.pyx`** -> AI Confidence: **99.31%**
11. **`pandas/_libs/tslibs/period.pyx`** -> AI Confidence: **99.31%**
12. **`pandas/_libs/tslibs/timedeltas.pyx`** -> AI Confidence: **99.31%**
13. **`pandas/_testing/_warnings.py`** -> AI Confidence: **99.31%**
14. **`pandas/_testing/asserters.py`** -> AI Confidence: **99.31%**
15. **`pandas/core/_numba/kernels/mean_.py`** -> AI Confidence: **99.31%**
16. **`pandas/core/_numba/kernels/sum_.py`** -> AI Confidence: **99.31%**
17. **`pandas/core/algorithms.py`** -> AI Confidence: **99.31%**
18. **`pandas/core/array_algos/putmask.py`** -> AI Confidence: **99.31%**
19. **`pandas/core/array_algos/replace.py`** -> AI Confidence: **99.31%**
20. **`pandas/core/array_algos/take.py`** -> AI Confidence: **99.31%**
21. **`pandas/core/arrays/_ranges.py`** -> AI Confidence: **99.31%**
22. **`pandas/core/arrays/_utils.py`** -> AI Confidence: **99.31%**
23. **`pandas/core/arrays/datetimes.py`** -> AI Confidence: **99.31%**
24. **`pandas/core/arrays/numeric.py`** -> AI Confidence: **99.31%**
25. **`pandas/core/arrays/string_arrow.py`** -> AI Confidence: **99.31%**
26. **`pandas/core/computation/eval.py`** -> AI Confidence: **99.31%**
27. **`pandas/core/computation/parsing.py`** -> AI Confidence: **99.31%**
28. **`pandas/core/config_init.py`** -> AI Confidence: **99.31%**
29. **`pandas/core/construction.py`** -> AI Confidence: **99.31%**
30. **`pandas/core/dtypes/astype.py`** -> AI Confidence: **99.31%**
31. **`pandas/core/dtypes/cast.py`** -> AI Confidence: **99.31%**
32. **`pandas/core/dtypes/concat.py`** -> AI Confidence: **99.31%**
33. **`pandas/core/frame.py`** -> AI Confidence: **99.31%**
34. **`pandas/core/generic.py`** -> AI Confidence: **99.31%**
35. **`pandas/core/groupby/groupby.py`** -> AI Confidence: **99.31%**
36. **`pandas/core/groupby/grouper.py`** -> AI Confidence: **99.31%**
37. **`pandas/core/groupby/indexing.py`** -> AI Confidence: **99.31%**
38. **`pandas/core/groupby/ops.py`** -> AI Confidence: **99.31%**
39. **`pandas/core/indexers/utils.py`** -> AI Confidence: **99.31%**
40. **`pandas/core/indexes/api.py`** -> AI Confidence: **99.31%**
41. **`pandas/core/indexes/base.py`** -> AI Confidence: **99.31%**
42. **`pandas/core/indexes/datetimes.py`** -> AI Confidence: **99.31%**
43. **`pandas/core/indexes/interval.py`** -> AI Confidence: **99.31%**
44. **`pandas/core/indexes/multi.py`** -> AI Confidence: **99.31%**
45. **`pandas/core/indexes/range.py`** -> AI Confidence: **99.31%**
46. **`pandas/core/indexing.py`** -> AI Confidence: **99.31%**
47. **`pandas/core/interchange/from_dataframe.py`** -> AI Confidence: **99.31%**
48. **`pandas/core/internals/blocks.py`** -> AI Confidence: **99.31%**
49. **`pandas/core/internals/concat.py`** -> AI Confidence: **99.31%**
50. **`pandas/core/internals/construction.py`** -> AI Confidence: **99.31%**
51. **`pandas/core/internals/managers.py`** -> AI Confidence: **99.31%**
52. **`pandas/core/methods/to_dict.py`** -> AI Confidence: **99.31%**
53. **`pandas/core/missing.py`** -> AI Confidence: **99.31%**
54. **`pandas/core/nanops.py`** -> AI Confidence: **99.31%**
55. **`pandas/core/ops/array_ops.py`** -> AI Confidence: **99.31%**
56. **`pandas/core/reshape/concat.py`** -> AI Confidence: **99.31%**
57. **`pandas/core/reshape/encoding.py`** -> AI Confidence: **99.31%**
58. **`pandas/core/reshape/melt.py`** -> AI Confidence: **99.31%**
59. **`pandas/core/reshape/merge.py`** -> AI Confidence: **99.31%**
60. **`pandas/core/reshape/pivot.py`** -> AI Confidence: **99.31%**
61. **`pandas/core/reshape/reshape.py`** -> AI Confidence: **99.31%**
62. **`pandas/core/reshape/tile.py`** -> AI Confidence: **99.31%**
63. **`pandas/core/sample.py`** -> AI Confidence: **99.31%**
64. **`pandas/core/sorting.py`** -> AI Confidence: **99.31%**
65. **`pandas/core/strings/accessor.py`** -> AI Confidence: **99.31%**
66. **`pandas/core/tools/datetimes.py`** -> AI Confidence: **99.31%**
67. **`pandas/core/tools/numeric.py`** -> AI Confidence: **99.31%**
68. **`pandas/core/tools/times.py`** -> AI Confidence: **99.31%**
69. **`pandas/core/window/common.py`** -> AI Confidence: **99.31%**
70. **`pandas/core/window/ewm.py`** -> AI Confidence: **99.31%**
71. **`pandas/core/window/numba_.py`** -> AI Confidence: **99.31%**
72. **`pandas/io/_util.py`** -> AI Confidence: **99.31%**
73. **`pandas/io/common.py`** -> AI Confidence: **99.31%**
74. **`pandas/io/excel/_base.py`** -> AI Confidence: **99.31%**
75. **`pandas/io/excel/_xlsxwriter.py`** -> AI Confidence: **99.31%**
76. **`pandas/io/formats/css.py`** -> AI Confidence: **99.31%**
77. **`pandas/io/formats/excel.py`** -> AI Confidence: **99.31%**
78. **`pandas/io/formats/format.py`** -> AI Confidence: **99.31%**
79. **`pandas/io/formats/html.py`** -> AI Confidence: **99.31%**
80. **`pandas/io/formats/printing.py`** -> AI Confidence: **99.31%**
81. **`pandas/io/formats/style.py`** -> AI Confidence: **99.31%**
82. **`pandas/io/formats/style_render.py`** -> AI Confidence: **99.31%**
83. **`pandas/io/json/_json.py`** -> AI Confidence: **99.31%**
84. **`pandas/io/json/_normalize.py`** -> AI Confidence: **99.31%**
85. **`pandas/io/json/_table_schema.py`** -> AI Confidence: **99.31%**
86. **`pandas/io/parquet.py`** -> AI Confidence: **99.31%**
87. **`pandas/io/parsers/arrow_parser_wrapper.py`** -> AI Confidence: **99.31%**
88. **`pandas/io/parsers/base_parser.py`** -> AI Confidence: **99.31%**
89. **`pandas/io/parsers/c_parser_wrapper.py`** -> AI Confidence: **99.31%**
90. **`pandas/io/parsers/python_parser.py`** -> AI Confidence: **99.31%**
91. **`pandas/io/parsers/readers.py`** -> AI Confidence: **99.31%**
92. **`pandas/io/pytables.py`** -> AI Confidence: **99.31%**
93. **`pandas/io/sql.py`** -> AI Confidence: **99.31%**
94. **`pandas/io/stata.py`** -> AI Confidence: **99.31%**
95. **`pandas/io/xml.py`** -> AI Confidence: **99.31%**
96. **`pandas/plotting/_core.py`** -> AI Confidence: **99.31%**
97. **`pandas/tests/apply/test_invalid_arg.py`** -> AI Confidence: **99.31%**
98. **`pandas/tests/apply/test_str.py`** -> AI Confidence: **99.31%**
99. **`pandas/tests/arithmetic/test_datetime64.py`** -> AI Confidence: **99.31%**
100. **`pandas/tests/arithmetic/test_period.py`** -> AI Confidence: **99.31%**
101. **`pandas/tests/arithmetic/test_string.py`** -> AI Confidence: **99.31%**
102. **`pandas/tests/arithmetic/test_timedelta64.py`** -> AI Confidence: **99.31%**
103. **`pandas/tests/arrays/categorical/test_constructors.py`** -> AI Confidence: **99.31%**
104. **`pandas/tests/arrays/integer/test_construction.py`** -> AI Confidence: **99.31%**
105. **`pandas/tests/arrays/period/test_constructors.py`** -> AI Confidence: **99.31%**
106. **`pandas/tests/arrays/string_/test_string.py`** -> AI Confidence: **99.31%**
107. **`pandas/tests/arrays/string_/test_string_arrow.py`** -> AI Confidence: **99.31%**
108. **`pandas/tests/base/test_value_counts.py`** -> AI Confidence: **99.31%**
109. **`pandas/tests/computation/test_eval.py`** -> AI Confidence: **99.31%**
110. **`pandas/tests/extension/test_arrow.py`** -> AI Confidence: **99.31%**
111. **`pandas/tests/extension/test_masked.py`** -> AI Confidence: **99.31%**
112. **`pandas/tests/frame/indexing/test_where.py`** -> AI Confidence: **99.31%**
113. **`pandas/tests/frame/methods/test_astype.py`** -> AI Confidence: **99.31%**
114. **`pandas/tests/frame/methods/test_between_time.py`** -> AI Confidence: **99.31%**
115. **`pandas/tests/frame/test_reductions.py`** -> AI Confidence: **99.31%**
116. **`pandas/tests/frame/test_stack_unstack.py`** -> AI Confidence: **99.31%**
117. **`pandas/tests/frame/test_ufunc.py`** -> AI Confidence: **99.31%**
118. **`pandas/tests/groupby/test_categorical.py`** -> AI Confidence: **99.31%**
119. **`pandas/tests/groupby/test_groupby_dropna.py`** -> AI Confidence: **99.31%**
120. **`pandas/tests/groupby/test_numeric_only.py`** -> AI Confidence: **99.31%**
121. **`pandas/tests/groupby/test_raises.py`** -> AI Confidence: **99.31%**
122. **`pandas/tests/groupby/test_reductions.py`** -> AI Confidence: **99.31%**
123. **`pandas/tests/groupby/transform/test_transform.py`** -> AI Confidence: **99.31%**
124. **`pandas/tests/indexes/interval/test_interval_range.py`** -> AI Confidence: **99.31%**
125. **`pandas/tests/indexes/period/test_constructors.py`** -> AI Confidence: **99.31%**
126. **`pandas/tests/indexes/test_indexing.py`** -> AI Confidence: **99.31%**
127. **`pandas/tests/indexes/test_old_base.py`** -> AI Confidence: **99.31%**
128. **`pandas/tests/indexes/test_setops.py`** -> AI Confidence: **99.31%**
129. **`pandas/tests/indexes/timedeltas/test_constructors.py`** -> AI Confidence: **99.31%**
130. **`pandas/tests/indexing/multiindex/test_slice.py`** -> AI Confidence: **99.31%**
131. **`pandas/tests/indexing/test_indexing.py`** -> AI Confidence: **99.31%**
132. **`pandas/tests/io/json/test_pandas.py`** -> AI Confidence: **99.31%**
133. **`pandas/tests/io/parser/common/test_chunksize.py`** -> AI Confidence: **99.31%**
134. **`pandas/tests/io/parser/common/test_common_basic.py`** -> AI Confidence: **99.31%**
135. **`pandas/tests/io/parser/common/test_read_errors.py`** -> AI Confidence: **99.31%**
136. **`pandas/tests/io/parser/test_compression.py`** -> AI Confidence: **99.31%**
137. **`pandas/tests/io/parser/test_dialect.py`** -> AI Confidence: **99.31%**
138. **`pandas/tests/io/parser/test_header.py`** -> AI Confidence: **99.31%**
139. **`pandas/tests/io/parser/test_quoting.py`** -> AI Confidence: **99.31%**
140. **`pandas/tests/io/parser/test_unsupported.py`** -> AI Confidence: **99.31%**
141. **`pandas/tests/io/pytables/test_append.py`** -> AI Confidence: **99.31%**
142. **`pandas/tests/io/pytables/test_errors.py`** -> AI Confidence: **99.31%**
143. **`pandas/tests/io/pytables/test_file_handling.py`** -> AI Confidence: **99.31%**
144. **`pandas/tests/io/test_stata.py`** -> AI Confidence: **99.31%**
145. **`pandas/tests/io/xml/test_xml.py`** -> AI Confidence: **99.31%**
146. **`pandas/tests/resample/test_base.py`** -> AI Confidence: **99.31%**
147. **`pandas/tests/reshape/merge/test_merge.py`** -> AI Confidence: **99.31%**
148. **`pandas/tests/reshape/test_get_dummies.py`** -> AI Confidence: **99.31%**
149. **`pandas/tests/series/accessors/test_cat_accessor.py`** -> AI Confidence: **99.31%**
150. **`pandas/tests/series/methods/test_astype.py`** -> AI Confidence: **99.31%**
151. **`pandas/tests/series/methods/test_convert_dtypes.py`** -> AI Confidence: **99.31%**
152. **`pandas/tests/series/methods/test_rank.py`** -> AI Confidence: **99.31%**
153. **`pandas/tests/series/test_logical_ops.py`** -> AI Confidence: **99.31%**
154. **`pandas/tests/strings/test_strings.py`** -> AI Confidence: **99.31%**
155. **`pandas/tests/tools/test_to_datetime.py`** -> AI Confidence: **99.31%**
156. **`pandas/tests/tseries/offsets/test_month.py`** -> AI Confidence: **99.31%**
157. **`pandas/tests/window/test_base_indexer.py`** -> AI Confidence: **99.31%**
158. **`pandas/util/_decorators.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pandas/tests/io/formats/style/test_html.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `asv_bench/benchmarks/algorithms.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/algos/isin.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/arithmetic.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/array.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/categoricals.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `asv_bench/benchmarks/eval.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/package.py` -> **100.0%** Exposure
- `doc/make.py` -> **100.0%** Exposure
- `doc/scripts/eval_performance.py` -> **100.0%** Exposure
- `pandas/tests/computation/test_eval.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `asv_bench/benchmarks/algorithms.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/algos/isin.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/arithmetic.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/array.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/attrs_caching.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10589` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `asv_bench/benchmarks/gil.py` (PYTHON) -> Cumulative Risk: **823.46**
- **Archetype:** `file_cluster_0` (Distance: 10.914 IQR)
- **Magnitude:** 264.76 | **LOC:** 328 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 54.4), `run_parallel` (Impact: 31.7), `setup` (Impact: 18.8)

### 2. `pandas/core/computation/pytables.py` (PYTHON) -> Cumulative Risk: **820.32**
- **Archetype:** `file_cluster_13` (Distance: 13.062 IQR)
- **Magnitude:** 986.24 | **LOC:** 675 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `prune` (Impact: 199.6), `convert_value` (Impact: 139.1), `prune` (Impact: 70.1)

### 3. `asv_bench/benchmarks/index_cached_properties.py` (PYTHON) -> Cumulative Risk: **819.66**
- **Archetype:** `file_cluster_8` (Distance: 11.793 IQR)
- **Magnitude:** 112.52 | **LOC:** 73 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 53.4), `time_values` (Impact: 2.7), `time_shape` (Impact: 2.7)

### 4. `pandas/core/apply.py` (PYTHON) -> Cumulative Risk: **813.7**
- **Archetype:** `file_cluster_13` (Distance: 12.38 IQR)
- **Magnitude:** 1385.14 | **LOC:** 2150 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 36.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `apply` (Impact: 148.2), `transform` (Impact: 132.4), `apply_empty_result` (Impact: 68.7)

### 5. `asv_bench/benchmarks/index_object.py` (PYTHON) -> Cumulative Risk: **809.75**
- **Archetype:** `file_cluster_8` (Distance: 11.869 IQR)
- **Magnitude:** 304.4 | **LOC:** 263 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9994%)
- **Heaviest Functions:** `setup` (Impact: 114.8), `peakmem_gc_instances` (Impact: 17.7), `setup` (Impact: 3.1)

### 6. `asv_bench/benchmarks/algos/isin.py` (PYTHON) -> Cumulative Risk: **804.84**
- **Archetype:** `file_cluster_8` (Distance: 11.713 IQR)
- **Magnitude:** 371.14 | **LOC:** 342 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 54.2), `setup` (Impact: 37.2), `setup` (Impact: 23.1)

### 7. `asv_bench/benchmarks/io/hdf.py` (PYTHON) -> Cumulative Risk: **799.59**
- **Archetype:** `file_cluster_8` (Distance: 11.615 IQR)
- **Magnitude:** 152.4 | **LOC:** 144 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 15.0), `setup` (Impact: 11.2), `time_query_store_table_wide` (Impact: 7.1)

### 8. `asv_bench/benchmarks/frame_ctor.py` (PYTHON) -> Cumulative Risk: **798.41**
- **Archetype:** `file_cluster_8` (Distance: 12.021 IQR)
- **Magnitude:** 199.06 | **LOC:** 202 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 16.1), `setup` (Impact: 14.6), `setup` (Impact: 5.4)

### 9. `asv_bench/benchmarks/categoricals.py` (PYTHON) -> Cumulative Risk: **792.43**
- **Archetype:** `file_cluster_8` (Distance: 12.24 IQR)
- **Magnitude:** 388.82 | **LOC:** 338 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup` (Impact: 22.8), `setup` (Impact: 18.1), `setup` (Impact: 11.1)

### 10. `asv_bench/benchmarks/eval.py` (PYTHON) -> Cumulative Risk: **787.11**
- **Archetype:** `file_cluster_13` (Distance: 11.795 IQR)
- **Magnitude:** 61.14 | **LOC:** 66 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup` (Impact: 8.4), `time_and` (Impact: 4.2), `time_add` (Impact: 3.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pandas/tests/io/xml/test_xml.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.111 IQR)
- **Top Global Matches:** file_cluster_8: 9.576, file_cluster_7: 10.14, file_cluster_13: 10.353
- **Magnitude:** 16712.32 | **LOC:** 2068 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.8243%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 168`, `args: 85`, `func_start: 85`
* *Risk/State:* None
* *Architecture:* `io: 14`, `api: 85`, `import: 20`
* *Defense:* `safety: 8`, `doc: 44`, `test: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pandas.compat._optional, __future__, lzma, numpy, pandas.io.common, io, tarfile, zipfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/frame.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.006 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.52 IQR)
- **Top Global Matches:** file_cluster_8: 13.006, file_cluster_16: 13.033, file_cluster_13: 13.075
- **Magnitude:** 10769.34 | **LOC:** 18736 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 15.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (9.558%), Tech Debt (46.2634%)
**Top Internal Functions/Classes:**
  * `select_dtypes` (Impact: 8951.3 | O(2^N) | DB: 27)
  * `__getitem__` (Impact: 149.2 | O(N^6))
  * `_setitem_array` (Impact: 145.8 | O(2^N))
  * `_set_item_frame_value` (Impact: 128.9 | O(N^5))
  * `dot` (Impact: 126.9 | O(2^N))
    * *Intent:* # used by repr_html under IPython notebook or scripts ignore terminal # dims if width is None or not...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 990`, `structural_boundaries: 845`, `args: 293`, `func_start: 291`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 3`, `state_mutation: 104`, `dead_code: 9`, `planned_debt: 12`, `duplicate_logic: 29`
* *Architecture:* `io: 2`, `api: 233`, `import: 95`
* *Defense:* `safety: 212`, `doc: 330`, `test: 15`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.493
  * `Choke Point (Betweenness):` 0.010579 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 54):` natsort, __future__, pandas._libs.internals, numpy, pandas.compat._constants, pyarrow, itertools, pandas.io.formats.style...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pandas/core/generic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.591 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_0: 12.591, file_cluster_8: 12.661, file_cluster_16: 12.709
- **Magnitude:** 7898.98 | **LOC:** 12805 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (13.0461%), Tech Debt (45.258%)
**Top Internal Functions/Classes:**
  * `to_csv` (Impact: 5832.4 | O(2^N) | DB: 8)
  * `asof` (Impact: 409.9 | O(2^N))
  * `_drop_labels_or_levels` (Impact: 110.5 | O(N^5))
    * *Intent:* *,
  * `__setstate__` (Impact: 86.6 | O(N^6) | DB: 2)
  * `_get_label_or_level_values` (Impact: 85.8 | O(N^5))
    * *Intent:* *,
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 832`, `structural_boundaries: 670`, `args: 227`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 114`, `dead_code: 10`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 8`, `api: 149`, `import: 69`
* *Defense:* `safety: 129`, `doc: 230`, `test: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.715
  * `Choke Point (Betweenness):` 0.00356 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` pandas.core.dtypes.dtypes, pandas.compat._optional, pandas.core.internals, natsort, __future__, pandas.core.indexers.objects, pandas.core.missing, pandas.io.formats.format...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.266 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.315 IQR)
- **Top Global Matches:** file_cluster_0: 13.266, file_cluster_13: 13.348, file_cluster_16: 13.404
- **Magnitude:** 6298.16 | **LOC:** 8145 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (18.2885%), Tech Debt (33.6102%)
**Top Internal Functions/Classes:**
  * `shift` (Impact: 1811.4 | O(N^5) | DB: 15)
  * `_validate_sort_keyword` (Impact: 1640.8 | O(2^N) | DB: 7)
  * `set_names` (Impact: 200.5 | O(N^5) | DB: 2)
  * `__getitem__` (Impact: 135.4 | O(2^N))
    * *Intent:* # Note: we do NOT call _dti_setop_align_tzs here, as there # is no requirement that .difference be c...
  * `astype` (Impact: 121.8 | O(2^N) | DB: 1)
    * *Intent:* # We need to keep M8/m8 dtype when initializing the Engine, # but don't want to change _get_engine_t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1022`, `structural_boundaries: 893`, `args: 235`, `func_start: 235`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 124`, `dead_code: 13`, `planned_debt: 26`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 128`, `import: 74`
* *Defense:* `safety: 243`, `doc: 330`, `test: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.569
  * `Choke Point (Betweenness):` 0.002586 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` pandas.core.dtypes.dtypes, pandas.core.ops, __future__, pandas._libs.internals, pandas.core.missing, pandas.io.formats.format, numpy, pandas._libs.join...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `pandas/_libs/parsers.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.043 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.817 IQR)
- **Top Global Matches:** file_cluster_8: 11.043, file_cluster_7: 11.56, file_cluster_13: 11.576
- **Magnitude:** 5906.42 | **LOC:** 2183 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(N^6) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (28.5053%), Tech Debt (9.018%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 5726.2 | O(N^6) | DB: 47)
  * `sanitize_objects` (Impact: 18.5 | O(N^3))
  * `_compute_na_values` (Impact: 3.8 | O(N^2))
  * `_maybe_upcast` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 168`, `args: 39`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 117`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 46`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pandas.errors, pandas._libs, pandas.core.dtypes.dtypes, pandas.util._exceptions, pyarrow, collections, pandas.core.dtypes.inference, pandas.core.arrays.boolean...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_sql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.765 IQR)
- **Top Global Matches:** file_cluster_0: 11.876, file_cluster_8: 11.948, file_cluster_13: 12.071
- **Magnitude:** 5620.5 | **LOC:** 4399 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 206
- **Risk Profile:** Cognitive Load (5.5401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sql_strings` (Impact: 4244.3 | O(2^N) | DB: 206)
  * `test_sqlite_type_mapping` (Impact: 969.1 | O(N^5) | DB: 92)
    * *Intent:* # GH 37157 conn_name = conn if conn_name == "sqlite_buildin": request.applymarker(pytest.mark.xfail(...
  * `test_sql_open_close` (Impact: 37.0 | O(N^3) | DB: 10)
  * `test_xsqlite_if_exists` (Impact: 24.8 | O(N^3))
  * `test_xsqlite_execute_closed_connection` (Impact: 18.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `structural_boundaries: 819`, `args: 220`, `func_start: 215`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 22`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 102`, `api: 217`, `import: 82`
* *Defense:* `safety: 313`, `doc: 42`, `test: 690`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pandas.compat._optional, sqlalchemy.schema, __future__, uuid, sqlalchemy.engine, adbc_driver_manager, numpy, sqlalchemy.sql...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/extension/test_arrow.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.419 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.621 IQR)
- **Top Global Matches:** file_cluster_8: 11.419, file_cluster_0: 11.712, file_cluster_7: 11.945
- **Magnitude:** 3839.88 | **LOC:** 3952 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.4073%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_get_arith_xfail_marker` (Impact: 497.1 | O(2^N))
  * `_cast_pointwise_result` (Impact: 261.7 | O(N^5))
  * `test_dt_strftime` (Impact: 155.3 | O(N^4) | DB: 3)
  * `test_quantile` (Impact: 143.3 | O(N^4))
    * *Intent:* # GH 56537
  * `_get_expected_reduction_dtype` (Impact: 136.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 508`, `args: 255`, `func_start: 251`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 178`
* *Architecture:* `io: 1`, `api: 244`, `import: 24`
* *Defense:* `safety: 152`, `doc: 16`, `test: 512`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` pandas.core.dtypes.dtypes, __future__, numpy, pandas.core.arrays.arrow.extension_types, datetime, pandas.core.arrays.arrow.array, pandas.api.extensions, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/io/stata.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.794 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.417 IQR)
- **Top Global Matches:** file_cluster_16: 12.794, file_cluster_8: 12.816, file_cluster_13: 12.89
- **Magnitude:** 3692.66 | **LOC:** 3939 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (33.0587%), Tech Debt (21.5707%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 2616.4 | O(2^N) | DB: 113)
    * *Intent:* # off - int32 array (n elements)
  * `_cast_to_stata_types` (Impact: 292.1 | O(N^6))
  * `_datetime_to_stata_elapsed_vec` (Impact: 130.0 | O(N^5))
  * `_maybe_convert_to_int_keys` (Impact: 30.9 | O(N^4))
  * `generate_value_label` (Impact: 26.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 387`, `args: 132`, `func_start: 130`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 427`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 27`, `import: 29`
* *Defense:* `safety: 46`, `doc: 144`, `test: 5`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.53
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` pandas.core.dtypes.dtypes, pandas._libs.writers, __future__, numpy, pandas.io.common, datetime, io, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/multi.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.569 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_13: 12.569, file_cluster_8: 12.614, file_cluster_16: 12.629
- **Magnitude:** 3446.8 | **LOC:** 4847 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 13.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (19.2455%), Tech Debt (20.1191%)
**Top Internal Functions/Classes:**
  * `_get_loc_level` (Impact: 693.2 | O(2^N))
  * `get_locs` (Impact: 199.1 | O(N^6))
  * `get_loc` (Impact: 177.5 | O(2^N))
  * `append` (Impact: 147.6 | O(2^N) | DB: 3)
  * `_union` (Impact: 127.8 | O(2^N) | DB: 1)
    * *Intent:* # codes get mapped from uniques to 0:len(uniques) # -1 (if present) is mapped to last position # ......
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 442`, `args: 118`, `func_start: 118`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 120`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 97`, `import: 38`
* *Defense:* `safety: 112`, `doc: 172`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.915
  * `Choke Point (Betweenness):` 0.000403 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` pandas.core.dtypes.dtypes, __future__, numpy, itertools, collections.abc, pandas.core.algorithms, pandas._typing, pandas...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/internals/blocks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.415 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.194 IQR)
- **Top Global Matches:** file_cluster_0: 12.415, file_cluster_11: 12.515, file_cluster_13: 12.526
- **Magnitude:** 3304.56 | **LOC:** 2396 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (19.1732%), Tech Debt (73.346%)
**Top Internal Functions/Classes:**
  * `where` (Impact: 2277.7 | O(2^N) | DB: 19)
    * *Intent:* -------
  * `setitem` (Impact: 184.2 | O(2^N) | DB: 2)
    * *Intent:* # NB: this cannot be made cache_readonly because in mgr.set_values we pin
  * `putmask` (Impact: 156.7 | O(2^N) | DB: 2)
    * *Intent:* """ Take values according to indexer and return them as a block. """
  * `coerce_to_target_dtype` (Impact: 92.5 | O(N^4))
    * *Intent:* """ assert self.ndim == 2 for i, ref_loc in enumerate(self._mgr_locs): vals = self.values[slice(i, i...
  * `convert` (Impact: 88.3 | O(2^N))
    * *Intent:* # In a future version of pandas, the default will be that # setting `nan` into an integer series won...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 353`, `args: 94`, `func_start: 94`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 114`, `dead_code: 5`, `planned_debt: 26`, `fragile_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 89`, `import: 38`
* *Defense:* `safety: 82`, `doc: 126`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.155
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` pandas.core.computation, inspect, pandas.core.dtypes.dtypes, __future__, pandas._libs.internals, numpy, pandas.core.base, pandas.core.api...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `pandas/core/indexing.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.227 IQR)
- **Top Global Matches:** file_cluster_13: 13.152, file_cluster_0: 13.19, file_cluster_8: 13.319
- **Magnitude:** 3289.1 | **LOC:** 3434 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (15.1105%), Tech Debt (99.9766%)
**Top Internal Functions/Classes:**
  * `_setitem_with_indexer_split_path` (Impact: 252.6 | O(N^5) | DB: 1)
    * *Intent:* # GH53533
  * `_convert_to_indexer` (Impact: 206.3 | O(N^6) | DB: 1)
  * `_align_frame` (Impact: 177.4 | O(N^6) | DB: 2)
  * `_setitem_with_indexer_missing` (Impact: 158.3 | O(N^6) | DB: 3)
  * `_maybe_mask_setitem_value` (Impact: 135.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 318`, `args: 85`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 58`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 33`
* *Architecture:* `io: 3`, `api: 17`, `import: 30`
* *Defense:* `safety: 134`, `doc: 106`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.544
  * `Choke Point (Betweenness):` 0.000877 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` pandas.core.dtypes.dtypes, pandas._libs.indexing, __future__, numpy, pandas.core.dtypes.concat, pandas.compat._constants, collections.abc, pandas.core.indexers...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pandas/io/sql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.652 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.827 IQR)
- **Top Global Matches:** file_cluster_13: 11.652, file_cluster_16: 11.819, file_cluster_0: 11.878
- **Magnitude:** 3095.74 | **LOC:** 2961 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (15.2246%), Tech Debt (79.1139%)
**Top Internal Functions/Classes:**
  * `get_engine` (Impact: 2333.0 | O(2^N) | DB: 56)
  * `_sqlalchemy_type` (Impact: 117.8 | O(N^5) | DB: 3)
  * `_index_name` (Impact: 92.5 | O(N^6))
    * *Intent:* -----
  * `insert_data` (Impact: 87.3 | O(N^6))
  * `_get_dtype` (Impact: 45.0 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 389`, `args: 101`, `func_start: 97`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 96`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 17`
* *Architecture:* `io: 33`, `api: 66`, `import: 58`
* *Defense:* `safety: 81`, `doc: 78`, `test: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` pandas.core.dtypes.dtypes, pandas.compat._optional, sqlalchemy.schema, __future__, sqlalchemy.engine, adbc_driver_manager, sqlalchemy.exc, numpy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pandas/core/arrays/arrow/array.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.94 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_8: 11.94, file_cluster_13: 12.027, file_cluster_16: 12.04
- **Magnitude:** 2722.24 | **LOC:** 3440 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 37.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (20.0347%), Tech Debt (12.1433%)
**Top Internal Functions/Classes:**
  * `_reduce_pyarrow` (Impact: 435.2 | O(N^6))
  * `_evaluate_op_method` (Impact: 207.2 | O(N^6))
  * `_cast_pointwise_result` (Impact: 175.6 | O(N^5))
  * `__getitem__` (Impact: 170.0 | O(N^5))
  * `_cmp_method` (Impact: 156.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 684`, `args: 180`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 21`, `dead_code: 2`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 120`, `import: 60`
* *Defense:* `safety: 114`, `doc: 98`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.123
  * `Choke Point (Betweenness):` 0.000939 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` pandas.core.dtypes.dtypes, __future__, numpy, pandas.core.nanops, datetime, pandas.core.tools.times, pyarrow, collections.abc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/core/reshape/merge.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.499 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.925 IQR)
- **Top Global Matches:** file_cluster_13: 12.499, file_cluster_8: 12.517, file_cluster_11: 12.606
- **Magnitude:** 2640.18 | **LOC:** 3139 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 11.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (34.806%), Tech Debt (11.2785%)
**Top Internal Functions/Classes:**
  * `_validate_validate_kwd` (Impact: 1536.5 | O(N^6) | DB: 16)
  * `_maybe_coerce_merge_keys` (Impact: 488.6 | O(N^6) | DB: 2)
    * *Intent:* # Overridden by AsOfMerge pass @final def _reindex_and_concat( self, join_index: Index, left_indexer...
  * `_validate_left_right_on` (Impact: 256.1 | O(N^6))
  * `_maybe_restore_index_levels` (Impact: 37.6 | O(N^5) | DB: 1)
  * `_indicator_name` (Impact: 30.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `structural_boundaries: 246`, `args: 59`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 175`, `dead_code: 10`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 37`
* *Defense:* `safety: 80`, `doc: 52`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.338
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` pandas.core.dtypes.dtypes, __future__, uuid, numpy, datetime, pyarrow, types, collections.abc...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/dtypes/dtypes.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.993 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.095 IQR)
- **Top Global Matches:** file_cluster_0: 12.993, file_cluster_13: 13.002, file_cluster_11: 13.084
- **Magnitude:** 2632.9 | **LOC:** 2497 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (31.6094%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `type` (Impact: 227.8 | O(2^N))
  * `__init__` (Impact: 163.7 | O(N^6) | DB: 8)
  * `construct_from_string` (Impact: 126.6 | O(2^N))
    * *Intent:* # We unwrap any masked dtypes, find the common dtype we would use # for that, then re-mask the resul...
  * `construct_from_string` (Impact: 94.9 | O(2^N))
  * `__new__` (Impact: 70.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 538`, `args: 127`, `func_start: 127`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 86`, `dead_code: 5`, `planned_debt: 12`, `duplicate_logic: 95`
* *Architecture:* `api: 81`, `import: 70`
* *Defense:* `safety: 106`, `doc: 134`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.154
  * `Choke Point (Betweenness):` 0.003066 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` pandas._libs.interval, __future__, pandas.core.arrays.boolean, numpy, datetime, pandas._libs.tslibs.dtypes, pyarrow, collections.abc...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/range.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.125 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.16 IQR)
- **Top Global Matches:** file_cluster_16: 11.125, file_cluster_13: 11.147, file_cluster_8: 11.213
- **Magnitude:** 2531.72 | **LOC:** 1585 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (20.258%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `_concat` (Impact: 437.9 | O(2^N) | DB: 1)
    * *Intent:* # calculate parameters for the RangeIndex describing the # intersection disregarding the lower bound...
  * `_difference` (Impact: 388.3 | O(2^N))
  * `_union` (Impact: 380.9 | O(2^N))
  * `_arith_method` (Impact: 207.4 | O(2^N))
    * *Intent:* # The difference is not range-like # e.g. range(1, 10, 1) and range(3, 7, 1)
  * `insert` (Impact: 157.2 | O(2^N) | DB: 1)
    * *Intent:* # -------------------------------------------------------------------- # Set Operations # caller is ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 297`, `args: 73`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 21`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 62`, `import: 24`
* *Defense:* `safety: 38`, `doc: 62`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.107
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` __future__, numpy, datetime, collections.abc, pandas.core.indexers, pandas._typing, pandas._libs.lib, pandas...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pandas/tests/io/formats/test_format.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.237 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.311 IQR)
- **Top Global Matches:** file_cluster_8: 11.237, file_cluster_7: 11.839, file_cluster_0: 11.865
- **Magnitude:** 2420.86 | **LOC:** 2303 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.8252%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `has_info_repr` (Impact: 1763.9 | O(2^N))
  * `test_east_asian_unicode_series` (Impact: 100.8 | O(N^5))
  * `test_format_percentiles_integer_idx` (Impact: 98.9 | O(N^4) | DB: 3)
  * `test_max_multi_index_display` (Impact: 40.0 | O(N^3))
  * `test_format_explicit` (Impact: 27.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 423`, `args: 106`, `func_start: 106`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `orphaned_logic: 32`
* *Architecture:* `io: 1`, `api: 111`, `import: 10`
* *Defense:* `safety: 277`, `doc: 6`, `test: 385`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pandas.io.formats.format, numpy, shutil, pytest, datetime, pandas, re, pandas.io.formats...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/_libs/window/aggregations.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.801 IQR)
- **Top Global Matches:** file_cluster_8: 9.035, file_cluster_7: 9.571, file_cluster_1: 9.843
- **Magnitude:** 2365.16 | **LOC:** 2119 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (9.5602%), Tech Debt (8.668%)
**Top Internal Functions/Classes:**
  * `roll_rank` (Impact: 351.7 | O(N^6))
  * `ewmcov` (Impact: 337.1 | O(N^6))
  * `roll_quantile` (Impact: 330.0 | O(N^6))
  * `ewm` (Impact: 313.8 | O(N^6))
  * `roll_median_c` (Impact: 200.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 80`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 4`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cython, pandas._libs.algos, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/internals/managers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.253 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_16: 12.253, file_cluster_11: 12.305, file_cluster_13: 12.329
- **Magnitude:** 2329.4 | **LOC:** 2557 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (23.9294%), Tech Debt (40.1312%)
**Top Internal Functions/Classes:**
  * `_verify_integrity` (Impact: 1247.3 | O(N^6) | DB: 43)
  * `setitem` (Impact: 268.6 | O(2^N) | DB: 1)
  * `copy` (Impact: 51.0 | O(2^N))
  * `_combine` (Impact: 49.5 | O(N^5) | DB: 2)
  * `equals` (Impact: 35.4 | O(2^N))
    * *Intent:* # Assumes we are 2D; overridden by SingleBlockManager
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 378`, `args: 132`, `func_start: 130`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 143`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 104`, `import: 30`
* *Defense:* `safety: 46`, `doc: 140`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.667
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` pandas.core.dtypes.dtypes, __future__, pandas._libs.internals, numpy, pandas.api.extensions, itertools, collections.abc, pandas.core.algorithms...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/tests/frame/test_constructors.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.609 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.66 IQR)
- **Top Global Matches:** file_cluster_8: 11.609, file_cluster_0: 11.914, file_cluster_7: 12.138
- **Magnitude:** 2110.34 | **LOC:** 3382 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (4.907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_constructor_dict_datetime64_index` (Impact: 1219.5 | O(N^5) | DB: 1)
    * *Intent:* # GH 10160 dates_as_str = ["1984-02-19", "1988-11-06", "1989-12-03", "1990-03-15"] def create_data(c...
  * `test_constructor_error_msgs` (Impact: 102.5 | O(N^4))
  * `test_constructor_mixed_dtypes` (Impact: 41.1 | O(N^4) | DB: 1)
  * `test_datetimelike_values_with_object_dty` (Impact: 25.6 | O(N^3))
    * *Intent:* # with dtype=object, we should cast dt64 values to Timestamps, not pydatetimes if kind == "M": dtype...
  * `test_constructor_list_of_2d_raises` (Impact: 24.9 | O(N^3))
    * *Intent:* # https://github.com/pandas-dev/pandas/issues/32289 a = DataFrame() b = np.empty((0, 0)) with pytest...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 545`, `args: 241`, `func_start: 232`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 10`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 4`, `orphaned_logic: 67`
* *Architecture:* `api: 238`, `import: 22`
* *Defense:* `safety: 236`, `test: 563`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pandas.core.dtypes.dtypes, numpy, datetime, numpy.dtypes, dataclasses, collections.abc, numpy.ma, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/arrays/datetimelike.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.731 IQR)
- **Top Global Matches:** file_cluster_13: 12.288, file_cluster_0: 12.321, file_cluster_16: 12.437
- **Magnitude:** 2048.58 | **LOC:** 2772 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 45.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.8385%), Tech Debt (47.985%)
**Top Internal Functions/Classes:**
  * `astype` (Impact: 182.8 | O(2^N))
  * `_validate_listlike` (Impact: 171.2 | O(N^6))
  * `_cmp_method` (Impact: 143.4 | O(N^6))
  * `_get_getitem_freq` (Impact: 115.6 | O(2^N))
    * *Intent:* -------
  * `__add__` (Impact: 89.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 465`, `args: 112`, `func_start: 112`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 25`, `dead_code: 3`, `planned_debt: 13`, `duplicate_logic: 6`
* *Architecture:* `api: 68`, `import: 55`
* *Defense:* `safety: 123`, `doc: 98`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.776
  * `Choke Point (Betweenness):` 0.000408 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` pandas.core.dtypes.dtypes, pandas._libs.tslibs.fields, __future__, pandas._libs.tslibs.np_datetime, numpy, datetime, pandas.tseries, pandas.core.arrays.arrow.array...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pandas/tests/indexing/test_loc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.833 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.644 IQR)
- **Top Global Matches:** file_cluster_8: 10.833, file_cluster_0: 11.267, file_cluster_7: 11.444
- **Magnitude:** 1994.22 | **LOC:** 3601 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.9299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loc_iloc_getitem_leading_ellipses` (Impact: 71.2 | O(N^4))
  * `test_loc_iloc_getitem_ellipses_only_one_` (Impact: 48.9 | O(N^3))
  * `test_loc_to_fail2` (Impact: 46.9 | O(N^3))
  * `test_loc_slice_disallows_positional` (Impact: 46.3 | O(N^3))
  * `test_loc_setitem_str_to_small_float_conv` (Impact: 40.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 344`, `args: 261`, `func_start: 220`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 13`, `orphaned_logic: 204`
* *Architecture:* `api: 232`, `import: 17`
* *Defense:* `safety: 74`, `doc: 4`, `test: 430`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pandas.errors, pandas.tests.indexing.common, pandas._libs, pyarrow, pandas._testing, collections, contextlib, dateutil.tz...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/frame/test_reductions.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.011 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.051 IQR)
- **Top Global Matches:** file_cluster_8: 11.011, file_cluster_0: 11.386, file_cluster_7: 11.571
- **Magnitude:** 1838.14 | **LOC:** 2235 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_min_max_dt64_with_NaT_skipna_false` (Impact: 636.0 | O(N^5))
  * `test_stat_op_api_float_string_frame` (Impact: 189.8 | O(N^6))
  * `test_any_all_np_func` (Impact: 106.1 | O(N^4))
  * `test_idxmin` (Impact: 89.1 | O(N^5))
  * `test_idxmax` (Impact: 67.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 230`, `args: 113`, `func_start: 108`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`, `fragile_debt: 3`, `orphaned_logic: 66`
* *Architecture:* `api: 112`, `import: 13`
* *Defense:* `safety: 126`, `doc: 8`, `test: 273`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pandas.compat.numpy, pandas._testing, dateutil.tz, pandas.util._test_decorators, numpy, pytest, pandas.core, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/io/pytables.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.772 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_0: 13.772, file_cluster_11: 13.777, file_cluster_13: 13.898
- **Magnitude:** 1837.38 | **LOC:** 5600 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 12.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (34.2486%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 169.8 | O(2^N) | DB: 9)
  * `remove` (Impact: 119.4 | O(2^N))
  * `write_data` (Impact: 110.8 | O(N^5) | DB: 2)
  * `_unconvert_index` (Impact: 68.6 | O(N^3))
  * `write` (Impact: 56.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 681`, `args: 245`, `func_start: 239`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 374`, `dead_code: 29`, `planned_debt: 17`, `fragile_debt: 3`, `duplicate_logic: 20`
* *Architecture:* `io: 7`, `api: 205`, `import: 41`
* *Defense:* `safety: 267`, `doc: 292`, `test: 47`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` pandas.core.dtypes.dtypes, pandas.compat._optional, pandas.core.internals, __future__, numpy, pandas.io.common, datetime, itertools...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pandas/_libs/tslibs/timedeltas.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.708 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.744 IQR)
- **Top Global Matches:** file_cluster_8: 11.708, file_cluster_0: 11.828, file_cluster_13: 11.879
- **Magnitude:** 1833.24 | **LOC:** 2781 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (22.7033%), Tech Debt (13.0821%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 369.8 | O(N^6))
    * *Intent:* # operate element-wise
  * `__floordiv__` (Impact: 220.9 | O(2^N))
  * `__rfloordiv__` (Impact: 123.1 | O(2^N))
  * `__richcmp__` (Impact: 122.7 | O(N^5) | DB: 1)
    * *Intent:* -------
  * `_repr_base` (Impact: 106.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 293`, `args: 65`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 92`, `dead_code: 7`, `planned_debt: 16`
* *Architecture:* `api: 45`, `import: 13`
* *Defense:* `safety: 51`, `doc: 78`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pandas.errors, pandas._libs.tslibs.timestamps, pandas.util._exceptions, pandas._libs.tslibs.fields, collections, pandas._libs.tslibs.np_datetime, pandas.util._decorators, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pandas/tests/dtypes/test_generic.py` (PYTHON) | Magnitude: 96.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 32, safety: 28, test: 25
- `pandas/io/pytables.py` (PYTHON) | Magnitude: 1837.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 3318, branch: 820, structural_boundaries: 681, encapsulation: 422
- `pandas/tests/util/test_deprecate_nonkeyword_arguments.py` (PYTHON) | Magnitude: 158.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 56, test: 39, branch: 28
- `pandas/core/dtypes/dtypes.py` (PYTHON) | Magnitude: 2632.9 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1189, structural_boundaries: 538, branch: 325, encapsulation: 195
- `pandas/_libs/tslibs/offsets.pyx` (PYTHON) | Magnitude: 538.2 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2509, encapsulation: 944, structural_boundaries: 665, branch: 589

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pandas/core/groupby/grouper.py` (PYTHON) | Magnitude: 383.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 462, branch: 142, structural_boundaries: 123, encapsulation: 97

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pandas/core/indexes/timedeltas.py` (PYTHON) | Magnitude: 65.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 61, encapsulation: 38, branch: 34
- `pandas/util/_validators.py` (PYTHON) | Magnitude: 334.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 144, branch: 70, structural_boundaries: 46, doc: 30
- `pandas/tests/arrays/string_/test_concat.py` (PYTHON) | Magnitude: 29.82 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 26, test: 15, safety: 9
- `pandas/io/formats/printing.py` (PYTHON) | Magnitude: 259.8 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 309, branch: 121, structural_boundaries: 90, encapsulation: 57
- `pandas/tests/frame/indexing/test_insert.py` (PYTHON) | Magnitude: 86.32 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 21, structural_boundaries: 17, test: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pandas/_testing/_warnings.py` (PYTHON) | Magnitude: 22.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, branch: 62, structural_boundaries: 41, generics: 20
- `pandas/_libs/reshape.pyi` (PYTHON) | Magnitude: 6.78 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 4, generics: 3
- `pandas/core/interchange/dataframe_protocol.py` (PYTHON) | Magnitude: 38.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 98, doc: 68, structural_boundaries: 45, decorators: 36
- `scripts/validate_min_versions_in_sync.py` (PYTHON) | Magnitude: 348.9 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 187, branch: 63, structural_boundaries: 45, generics: 24
- `pandas/_libs/join.pyi` (PYTHON) | Magnitude: 36.84 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, api: 22, generics: 20, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pandas/tests/indexes/datetimes/methods/test_to_julian_date.py` (PYTHON) | Magnitude: 47.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 17, branch: 10, safety: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `doc/source/user_guide/templates/html_table_structure.html` (HTML) | Magnitude: 15.68 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, ui_framework: 12, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pandas/tests/series/test_subclass.py` (PYTHON) | Magnitude: 46.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 28, test: 17, args: 10
- `pandas/tests/extension/base/casting.py` (PYTHON) | Magnitude: 77.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 37, test: 24, safety: 19
- `pandas/tests/test_common.py` (PYTHON) | Magnitude: 161.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 85, test: 62, safety: 28
- `pandas/tests/dtypes/test_common.py` (PYTHON) | Magnitude: 458.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 311, test: 283, safety: 190
- `pandas/tests/indexes/interval/test_indexing.py` (PYTHON) | Magnitude: 446.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 522, test: 130, structural_boundaries: 112, safety: 58

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pandas/core/series.py` -> Churn: **87.81%** | Cog Load: 6.6068% | Debt: 99.4783%
- `pandas/core/resample.py` -> Churn: **69.85%** | Cog Load: 16.722% | Debt: 99.9829%
- `pandas/core/arrays/masked.py` -> Churn: **66.45%** | Cog Load: 19.9054% | Debt: 50.6313%
- `pandas/core/arrays/base.py` -> Churn: **63.49%** | Cog Load: 22.7824% | Debt: 65.6141%
- `pandas/core/indexing.py` -> Churn: **62.95%** | Cog Load: 15.1105% | Debt: 99.9766%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pandas/tests/arithmetic/test_timedelta64.py` -> **jbrockmendel** (91.7% isolated ownership) | Magnitude: 1361.06
- `pandas/tests/arithmetic/test_datetime64.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 1274.02
- `scripts/check_test_naming.py` -> **Richard Shadrach** (100.0% isolated ownership) | Magnitude: 1197.35
- `asv_bench/benchmarks/groupby.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 992.48
- `asv_bench/benchmarks/frame_methods.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 874.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pandas/io/formats/format.py` -> **Severity: 0.357** (Bridge: 0.0036 * Flux: 97.9028%)
- `pandas/core/frame.py` -> **Severity: 0.197** (Bridge: 0.0106 * Flux: 18.622%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 0.19** (Bridge: 0.0031 * Flux: 61.8468%)
- `pandas/util/_decorators.py` -> **Severity: 0.189** (Bridge: 0.0019 * Flux: 100.0%)
- `pandas/io/sas/sas7bdat.py` -> **Severity: 0.178** (Bridge: 0.0018 * Flux: 99.9802%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pandas/_typing.py` -> **Severity: 5171.76** (Blast Radius: 63.929 * Doc Risk: 80.8985%)
- `pandas/util/_exceptions.py` -> **Severity: 3237.697** (Blast Radius: 33.187 * Doc Risk: 97.5592%)
- `pandas/util/_decorators.py` -> **Severity: 2748.3** (Blast Radius: 27.483 * Doc Risk: 100.0%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 2315.4** (Blast Radius: 23.154 * Doc Risk: 100.0%)
- `pandas/_testing/compat.py` -> **Severity: 1327.042** (Blast Radius: 14.222 * Doc Risk: 93.3091%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
