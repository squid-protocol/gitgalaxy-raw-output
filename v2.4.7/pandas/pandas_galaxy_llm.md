# ARCHITECTURAL_BRIEF: pandas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pandas` |
| **Timestamp** | `2026-08-07T05:20:39.815636+00:00` |
| **Scan Duration** | `11.49s` |
| **Git Branch** | `main` |
| **Git Commit** | `7629c655b22b998dd86bf98c2f1c721998e9e4f1` |
| **Git Remote** | `https://github.com/pandas-dev/pandas.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1588 malicious artifacts.

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
| Modularity | 0.4117 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Error & Exception Exposure | 0.0 | 99.7 | 15.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.6 | 5.1 | 5.2 | 0.0 |
| Concurrency Exposure | 0.0 | 59.2 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 62.9 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.4 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
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

- `__cinit__` (@ `pandas/_libs/parsers.pyx`) -> Impact: **1651.6** | LOC: 1037
- `select_dtypes` (@ `pandas/core/frame.py`) -> Impact: **1451.3** | LOC: 4026
- `to_csv` (@ `pandas/core/generic.py`) -> Impact: **860.1** | LOC: 1003
- `sql_strings` (@ `pandas/tests/io/test_sql.py`) -> Impact: **710.9** | LOC: 2440
- `shift` (@ `pandas/core/indexes/base.py`) -> Impact: **643.4** | LOC: 1188
- `test_datetime_invalid_scalar` (@ `pandas/tests/tools/test_to_datetime.py`) -> Impact: **525.2** | LOC: 2225
- `test_constructor_dict_datetime64_index` (@ `pandas/tests/frame/test_constructors.py`) -> Impact: **488.6** | LOC: 2463
  * *Intent:* # GH 10160 dates_as_str = ["1984-02-19", "1988-11-06", "1989-12-03", "1990-03-15"] def create_data(constructor): return {i: {constructor(s): 2 * i} fo...
- `_validate_validate_kwd` (@ `pandas/core/reshape/merge.py`) -> Impact: **475.6** | LOC: 1025
- `test_literal_json_raises` (@ `pandas/tests/io/json/test_pandas.py`) -> Impact: **433.3** | LOC: 1876
  * *Intent:* # PR 53409 jsonl = """{"a": 1, "b": 2} {"a": 3, "b": 4} {"a": 5, "b": 6} {"a": 7, "b": 8}"""
- `__init__` (@ `pandas/io/stata.py`) -> Impact: **423.7** | LOC: 1164
  * *Intent:* # off - int32 array (n elements)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pandas/tests/io/xml` | 4 | 17138.62 | 3.13% | 0.0% |
| `pandas/core` | 22 | 9797.06 | 13.58% | 50.64% |
| `pandas/tests/frame/methods` | 80 | 7522.38 | 4.2% | 0.0% |
| `asv_bench/benchmarks` | 39 | 6560.98 | 40.66% | 92.19% |
| `pandas/_libs` | 52 | 5831.15 | 12.68% | 24.22% |
| `pandas/core/arrays` | 20 | 5594.26 | 15.54% | 20.4% |
| `pandas/core/indexes` | 14 | 5523.9 | 14.76% | 25.79% |
| `pandas/tests/frame` | 21 | 5265.54 | 5.15% | 0.0% |
| `pandas/tests/io` | 17 | 4730.26 | 4.1% | 0.0% |
| `pandas/tests/groupby` | 23 | 4453.1 | 6.59% | 0.0% |

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
- `pandas/tests/series/test_constructors.py` -> **147** Orphaned Functions | **6** Duplicates
- `pandas/tests/groupby/test_groupby.py` -> **146** Orphaned Functions | **5** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10589` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `asv_bench/benchmarks/index_object.py` (PYTHON) -> Cumulative Risk: **661.5**
- **Archetype:** `file_cluster_8` (Distance: 11.869 IQR)
- **Magnitude:** 197.5 | **LOC:** 263 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9992%), State Flux (99.9989%), Documentation (99.9786%)
- **Heaviest Functions:** `setup` (Impact: 34.3), `peakmem_gc_instances` (Impact: 7.3), `setup` (Impact: 2.3)

### 2. `asv_bench/benchmarks/algos/isin.py` (PYTHON) -> Cumulative Risk: **654.47**
- **Archetype:** `file_cluster_8` (Distance: 11.713 IQR)
- **Magnitude:** 258.74 | **LOC:** 342 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Documentation (97.0719%)
- **Heaviest Functions:** `setup` (Impact: 19.6), `setup` (Impact: 19.2), `setup` (Impact: 11.9)

### 3. `asv_bench/benchmarks/io/hdf.py` (PYTHON) -> Cumulative Risk: **654.24**
- **Archetype:** `file_cluster_8` (Distance: 11.615 IQR)
- **Magnitude:** 118.2 | **LOC:** 144 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9993%), Documentation (99.6566%)
- **Heaviest Functions:** `setup` (Impact: 7.2), `setup` (Impact: 6.0), `time_query_store_table_wide` (Impact: 3.7)

### 4. `asv_bench/benchmarks/frame_ctor.py` (PYTHON) -> Cumulative Risk: **653.81**
- **Archetype:** `file_cluster_8` (Distance: 12.021 IQR)
- **Magnitude:** 159.46 | **LOC:** 202 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.999%), Documentation (99.8782%)
- **Heaviest Functions:** `setup` (Impact: 10.9), `setup` (Impact: 7.6), `setup` (Impact: 3.7)

### 5. `asv_bench/benchmarks/categoricals.py` (PYTHON) -> Cumulative Risk: **648.77**
- **Archetype:** `file_cluster_8` (Distance: 12.24 IQR)
- **Magnitude:** 300.22 | **LOC:** 338 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9912%)
- **Heaviest Functions:** `setup` (Impact: 9.8), `setup` (Impact: 9.5), `setup` (Impact: 5.9)

### 6. `asv_bench/benchmarks/gil.py` (PYTHON) -> Cumulative Risk: **641.52**
- **Archetype:** `file_cluster_0` (Distance: 11.056 IQR)
- **Magnitude:** 215.96 | **LOC:** 328 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.7468%), State Flux (93.291%)
- **Heaviest Functions:** `run_parallel` (Impact: 13.5), `setup` (Impact: 12.8), `wrapper` (Impact: 11.3)

### 7. `asv_bench/benchmarks/reindex.py` (PYTHON) -> Cumulative Risk: **640.74**
- **Archetype:** `file_cluster_8` (Distance: 11.431 IQR)
- **Magnitude:** 110.42 | **LOC:** 149 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9933%), Documentation (99.7138%)
- **Heaviest Functions:** `setup` (Impact: 8.0), `setup` (Impact: 6.2), `setup` (Impact: 3.9)

### 8. `asv_bench/benchmarks/array.py` (PYTHON) -> Cumulative Risk: **640.52**
- **Archetype:** `file_cluster_8` (Distance: 11.663 IQR)
- **Magnitude:** 146.24 | **LOC:** 141 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.999%), State Flux (99.9722%)
- **Heaviest Functions:** `setup` (Impact: 18.9), `setup` (Impact: 10.9), `setup` (Impact: 3.8)

### 9. `pandas/util/version/__init__.py` (PYTHON) -> Cumulative Risk: **636.85**
- **Archetype:** `file_cluster_16` (Distance: 11.279 IQR)
- **Magnitude:** 244.76 | **LOC:** 456 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 34.3), `__str__` (Impact: 15.2), `_parse_local_version` (Impact: 12.6)

### 10. `asv_bench/benchmarks/indexing.py` (PYTHON) -> Cumulative Risk: **628.96**
- **Archetype:** `file_cluster_8` (Distance: 11.652 IQR)
- **Magnitude:** 458.58 | **LOC:** 585 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.8517%)
- **Heaviest Functions:** `setup` (Impact: 16.9), `setup` (Impact: 7.4), `setup` (Impact: 6.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pandas/tests/io/xml/test_xml.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.111 IQR)
- **Top Global Matches:** file_cluster_8: 9.576, file_cluster_7: 10.14, file_cluster_13: 10.353
- **Magnitude:** 16712.32 | **LOC:** 2068 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (2.8243%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 168`, `args: 85`, `func_start: 85`
* *Risk/State:* None
* *Architecture:* `io: 14`, `api: 85`, `import: 20`
* *Defense:* `safety: 8`, `doc: 44`, `test: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pytest, pandas._testing, lzma, io, pandas.util._test_decorators, pandas.errors, os, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/frame.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.007 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.52 IQR)
- **Top Global Matches:** file_cluster_8: 13.007, file_cluster_16: 13.034, file_cluster_13: 13.077
- **Magnitude:** 2439.14 | **LOC:** 18736 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 15.8%
- **Risk Profile:** Cognitive Load (9.3922%), Tech Debt (46.2634%)
**Top Internal Functions/Classes:**
  * `select_dtypes` (Impact: 1451.3)
  * `__getitem__` (Impact: 45.3)
  * `_set_item_frame_value` (Impact: 44.9)
  * `__setitem__` (Impact: 27.7)
  * `_iset_not_inplace` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 990`, `structural_boundaries: 845`, `args: 293`, `func_start: 291`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 3`, `state_mutation: 104`, `dead_code: 9`, `planned_debt: 12`, `duplicate_logic: 29`
* *Architecture:* `io: 2`, `api: 233`, `import: 95`
* *Defense:* `safety: 212`, `doc: 330`, `test: 15`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.493
  * `Choke Point (Betweenness):` 0.010579 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 54):` typing, datetime, pandas.core.arrays.sparse, pyarrow, pandas.core.arrays.string_, pandas.core.internals.managers, pandas.core.construction, pandas.core.dtypes.concat...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.265 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_0: 13.265, file_cluster_13: 13.348, file_cluster_16: 13.404
- **Magnitude:** 2145.46 | **LOC:** 8145 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 21.4%
- **Risk Profile:** Cognitive Load (18.297%), Tech Debt (36.1927%)
**Top Internal Functions/Classes:**
  * `shift` (Impact: 643.4)
  * `_validate_sort_keyword` (Impact: 258.7)
  * `set_names` (Impact: 68.2)
  * `__array_ufunc__` (Impact: 38.7)
  * `_convert_slice_indexer` (Impact: 36.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1022`, `structural_boundaries: 893`, `args: 235`, `func_start: 235`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 124`, `dead_code: 13`, `planned_debt: 26`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 128`, `import: 74`
* *Defense:* `safety: 243`, `doc: 330`, `test: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.569
  * `Choke Point (Betweenness):` 0.002586 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` datetime, typing, pandas._libs, pandas.core.dtypes.inference, collections.abc, pandas.core.arrays, pandas._libs.lib, pandas.core.dtypes.missing...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `pandas/core/generic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.585 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.844 IQR)
- **Top Global Matches:** file_cluster_0: 12.585, file_cluster_8: 12.655, file_cluster_16: 12.703
- **Magnitude:** 1831.18 | **LOC:** 12805 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 14.5%
- **Risk Profile:** Cognitive Load (13.0204%), Tech Debt (50.0159%)
**Top Internal Functions/Classes:**
  * `to_csv` (Impact: 860.1)
  * `asof` (Impact: 61.9)
  * `_drop_labels_or_levels` (Impact: 38.5)
    * *Intent:* *,
  * `_clip_with_one_bound` (Impact: 33.4)
  * `_get_label_or_level_values` (Impact: 29.9)
    * *Intent:* *,
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 832`, `structural_boundaries: 670`, `args: 227`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 114`, `dead_code: 10`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `io: 8`, `api: 149`, `import: 69`
* *Defense:* `safety: 129`, `doc: 230`, `test: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.715
  * `Choke Point (Betweenness):` 0.00356 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` datetime, typing, pandas._libs, pandas.core.dtypes.inference, collections.abc, pandas.core.arrays, sqlalchemy.dialects.mysql, adbc_driver_sqlite...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pandas/_libs/parsers.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.039 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.817 IQR)
- **Top Global Matches:** file_cluster_8: 11.039, file_cluster_7: 11.556, file_cluster_13: 11.571
- **Magnitude:** 1822.22 | **LOC:** 2183 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (28.5053%), Tech Debt (9.018%)
**Top Internal Functions/Classes:**
  * `__cinit__` (Impact: 1651.6)
  * `sanitize_objects` (Impact: 9.8)
  * `_compute_na_values` (Impact: 2.9)
  * `_maybe_upcast` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 168`, `args: 39`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 117`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 46`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pandas.core.arrays.boolean, collections, pandas.core.dtypes.inference, pandas._libs, pandas, pandas.errors, pandas.core.arrays, pandas._config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/extension/test_arrow.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.41 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.621 IQR)
- **Top Global Matches:** file_cluster_8: 11.41, file_cluster_0: 11.703, file_cluster_7: 11.936
- **Magnitude:** 1692.38 | **LOC:** 3952 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (6.4092%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_cast_pointwise_result` (Impact: 90.3)
  * `test_dt_strftime` (Impact: 77.3)
  * `_get_arith_xfail_marker` (Impact: 77.0)
  * `test_quantile` (Impact: 59.5)
    * *Intent:* # GH 56537
  * `_get_expected_reduction_dtype` (Impact: 46.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 508`, `args: 255`, `func_start: 251`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 178`
* *Architecture:* `io: 1`, `api: 244`, `import: 24`
* *Defense:* `safety: 152`, `doc: 16`, `test: 512`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` datetime, pandas._libs, pytest, pandas._testing, pandas.api.extensions, pandas.api.types, io, pandas.core.arrays.arrow.array...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_sql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.861 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.765 IQR)
- **Top Global Matches:** file_cluster_0: 11.861, file_cluster_8: 11.933, file_cluster_13: 12.056
- **Magnitude:** 1451.4 | **LOC:** 4399 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (5.5401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sql_strings` (Impact: 710.9)
  * `test_sqlite_type_mapping` (Impact: 376.8)
    * *Intent:* # GH 37157 conn_name = conn if conn_name == "sqlite_buildin": request.applymarker(pytest.mark.xfail(...
  * `test_sql_open_close` (Impact: 19.7)
  * `test_xsqlite_if_exists` (Impact: 14.4)
  * `test_xsqlite_execute_closed_connection` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `structural_boundaries: 819`, `args: 220`, `func_start: 215`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 22`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 102`, `api: 217`, `import: 82`
* *Defense:* `safety: 313`, `doc: 42`, `test: 690`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` datetime, typing, pandas._libs, sqlalchemy.dialects.mysql, adbc_driver_sqlite, pytest, pandas._testing, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/indexing/test_loc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.833 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.644 IQR)
- **Top Global Matches:** file_cluster_8: 10.833, file_cluster_0: 11.267, file_cluster_7: 11.444
- **Magnitude:** 1235.52 | **LOC:** 3601 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 35.7%
- **Risk Profile:** Cognitive Load (3.9299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loc_iloc_getitem_leading_ellipses` (Impact: 29.1)
  * `test_loc_iloc_getitem_ellipses_only_one_` (Impact: 24.9)
  * `test_loc_to_fail2` (Impact: 24.4)
  * `test_loc_slice_disallows_positional` (Impact: 23.8)
  * `test_loc_getitem_listlike_of_datetimelik` (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 344`, `args: 261`, `func_start: 220`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 13`, `orphaned_logic: 204`
* *Architecture:* `api: 232`, `import: 17`
* *Defense:* `safety: 74`, `doc: 4`, `test: 430`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` collections, datetime, pandas._libs, pandas.errors, pandas, pytest, pandas._testing, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/indexes/multi.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.56 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_13: 12.56, file_cluster_8: 12.604, file_cluster_16: 12.62
- **Magnitude:** 1232.3 | **LOC:** 4847 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (19.1388%), Tech Debt (20.1191%)
**Top Internal Functions/Classes:**
  * `_get_loc_level` (Impact: 105.2)
  * `get_locs` (Impact: 60.6)
  * `get_loc` (Impact: 38.9)
  * `_set_names` (Impact: 37.5)
  * `_partial_tup_index` (Impact: 30.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 442`, `args: 118`, `func_start: 118`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 120`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 97`, `import: 38`
* *Defense:* `safety: 112`, `doc: 172`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.915
  * `Choke Point (Betweenness):` 0.000403 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` typing, pandas.core.dtypes.inference, pandas._libs, collections.abc, pandas.core.arrays, pandas.core.sorting, pandas.core.dtypes.missing, pandas.core.array_algos.putmask...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/indexing.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.142 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.227 IQR)
- **Top Global Matches:** file_cluster_13: 13.142, file_cluster_0: 13.18, file_cluster_8: 13.309
- **Magnitude:** 1230.1 | **LOC:** 3434 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 19.0%
- **Risk Profile:** Cognitive Load (15.1105%), Tech Debt (99.9766%)
**Top Internal Functions/Classes:**
  * `_setitem_with_indexer_split_path` (Impact: 87.1)
    * *Intent:* # GH53533
  * `_convert_to_indexer` (Impact: 61.4)
  * `_align_frame` (Impact: 52.4)
  * `_setitem_with_indexer_missing` (Impact: 48.3)
  * `_validate_key` (Impact: 42.2)
    * *Intent:* # e.g. if we are doing df.loc[:, ["A", "B"]] = 7 and "B" # is a new column, add the new columns with...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 318`, `args: 85`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 58`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 33`
* *Architecture:* `io: 3`, `api: 17`, `import: 30`
* *Defense:* `safety: 134`, `doc: 106`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.544
  * `Choke Point (Betweenness):` 0.000877 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` typing, collections.abc, pandas.core.arrays, contextlib, pandas._libs.lib, pandas.core.dtypes.missing, pandas.core.construction, pandas.errors.cow...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `scripts/check_test_naming.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.254 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.988 IQR)
- **Top Global Matches:** file_cluster_13: 12.254, file_cluster_0: 12.596, file_cluster_9: 12.629
- **Magnitude:** 1197.35 | **LOC:** 157 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.8939%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `dead_code: 3`
* *Architecture:* `io: 6`, `api: 3`, `import: 8`
* *Defense:* `safety: 11`, `doc: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, pathlib, ast, os, argparse, __future__, collections.abc, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pandas/tests/io/json/test_pandas.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.772 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.663 IQR)
- **Top Global Matches:** file_cluster_8: 10.772, file_cluster_0: 11.017, file_cluster_7: 11.231
- **Magnitude:** 1177.34 | **LOC:** 2388 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 64.3%
- **Risk Profile:** Cognitive Load (4.3%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_literal_json_raises` (Impact: 433.3)
    * *Intent:* # PR 53409 jsonl = """{"a": 1, "b": 2} {"a": 3, "b": 4} {"a": 5, "b": 6} {"a": 7, "b": 8}"""
  * `test_date_index_and_values` (Impact: 23.9)
  * `test_roundtrip_str_axes` (Impact: 23.8)
  * `test_frame_non_unique_columns` (Impact: 21.6)
  * `test_timedelta_to_json` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 243`, `args: 136`, `func_start: 135`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 102`
* *Architecture:* `io: 5`, `api: 133`, `import: 19`
* *Defense:* `safety: 66`, `doc: 22`, `test: 314`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, uuid, os, pandas.errors, pytest, pandas, json, pandas._testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/arrays/arrow/array.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.939 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.356 IQR)
- **Top Global Matches:** file_cluster_8: 11.939, file_cluster_13: 12.025, file_cluster_16: 12.039
- **Magnitude:** 1174.14 | **LOC:** 3440 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 37.1%
- **Risk Profile:** Cognitive Load (20.0078%), Tech Debt (20.1239%)
**Top Internal Functions/Classes:**
  * `_reduce_pyarrow` (Impact: 129.0)
  * `_evaluate_op_method` (Impact: 61.9)
  * `_cast_pointwise_result` (Impact: 61.3)
  * `__getitem__` (Impact: 59.2)
  * `_cmp_method` (Impact: 46.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 684`, `args: 180`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 21`, `dead_code: 2`, `planned_debt: 16`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 120`, `import: 60`
* *Defense:* `safety: 114`, `doc: 98`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.123
  * `Choke Point (Betweenness):` 0.000939 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` datetime, typing, pandas._libs, collections.abc, pandas._typing, pandas.core.dtypes.missing, pyarrow, pandas.core.arrays.string_...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/tests/groupby/test_groupby.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.949 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.375 IQR)
- **Top Global Matches:** file_cluster_8: 10.949, file_cluster_0: 11.434, file_cluster_7: 11.566
- **Magnitude:** 1162.24 | **LOC:** 3020 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (5.8891%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_groupby` (Impact: 124.9)
  * `test_groupby_level_nonmulti` (Impact: 32.7)
    * *Intent:* # GH 1313, GH 13901 s = Series([1, 2, 3, 10, 4, 5, 20, 6], Index([1, 2, 3, 1, 4, 5, 2, 6], name="foo...
  * `test_indices_concatenation_order` (Impact: 28.6)
    * *Intent:* # GH 2808 def f1(x): y = x[(x.b % 2) == 1] ** 2 if y.empty: multiindex = MultiIndex(levels=[[]] * 2,...
  * `test_omit_nuisance_agg` (Impact: 28.3)
    * *Intent:* # GH 38774, GH 38815 grouped = df.groupby("A") no_drop_nuisance = ("var", "std", "sem", "mean", "pro...
  * `test_len_categorical` (Impact: 23.0)
    * *Intent:* # GH#57595 df = DataFrame( { "a": Categorical([1, 1, 2, np.nan], categories=[1, 2, 3]), "b": Categor...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 316`, `args: 214`, `func_start: 169`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 14`, `planned_debt: 3`, `duplicate_logic: 5`, `orphaned_logic: 146`
* *Architecture:* `io: 1`, `api: 161`, `import: 13`
* *Defense:* `safety: 130`, `doc: 2`, `test: 318`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, pandas.errors, pandas, pytest, pandas._testing, pandas.core.arrays, numpy, decimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/io/stata.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.795 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.417 IQR)
- **Top Global Matches:** file_cluster_16: 12.795, file_cluster_8: 12.817, file_cluster_13: 12.891
- **Magnitude:** 1145.06 | **LOC:** 3939 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (33.3898%), Tech Debt (21.5707%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 423.7)
    * *Intent:* # off - int32 array (n elements)
  * `_cast_to_stata_types` (Impact: 87.2)
  * `_datetime_to_stata_elapsed_vec` (Impact: 46.9)
  * `_dtype_to_stata_type` (Impact: 14.9)
  * `generate_value_label` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 387`, `args: 132`, `func_start: 130`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 427`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 27`, `import: 29`
* *Defense:* `safety: 46`, `doc: 144`, `test: 5`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.53
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` datetime, typing, pandas._libs, collections.abc, pandas._libs.lib, pandas._libs.writers, struct, io...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pandas/io/pytables.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.772 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_0: 13.772, file_cluster_11: 13.777, file_cluster_13: 13.898
- **Magnitude:** 1115.78 | **LOC:** 5600 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 12.5%
- **Risk Profile:** Cognitive Load (34.2486%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `write_data` (Impact: 38.9)
  * `_unconvert_index` (Impact: 35.1)
  * `_convert_index` (Impact: 27.7)
  * `_dtype_to_kind` (Impact: 27.5)
    * *Intent:* # add the rows
  * `open` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 681`, `args: 245`, `func_start: 239`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 374`, `dead_code: 29`, `planned_debt: 17`, `fragile_debt: 3`, `duplicate_logic: 20`
* *Architecture:* `io: 7`, `api: 205`, `import: 41`
* *Defense:* `safety: 267`, `doc: 292`, `test: 47`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` datetime, typing, pandas._libs, collections.abc, pandas.core.arrays, contextlib, pandas.core.computation.pytables, tables...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pandas/tests/frame/test_constructors.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.618 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.663 IQR)
- **Top Global Matches:** file_cluster_8: 11.618, file_cluster_0: 11.922, file_cluster_7: 12.146
- **Magnitude:** 1105.54 | **LOC:** 3382 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (4.9058%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_constructor_dict_datetime64_index` (Impact: 488.6)
    * *Intent:* # GH 10160 dates_as_str = ["1984-02-19", "1988-11-06", "1989-12-03", "1990-03-15"] def create_data(c...
  * `test_constructor_error_msgs` (Impact: 42.8)
  * `test_constructor_mixed_dtypes` (Impact: 17.1)
  * `test_datetimelike_values_with_object_dty` (Impact: 13.6)
    * *Intent:* # with dtype=object, we should cast dt64 values to Timestamps, not pydatetimes if kind == "M": dtype...
  * `test_constructor_list_of_2d_raises` (Impact: 12.8)
    * *Intent:* # https://github.com/pandas-dev/pandas/issues/32289 a = DataFrame() b = np.empty((0, 0)) with pytest...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 545`, `args: 252`, `func_start: 232`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 10`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 4`, `orphaned_logic: 67`
* *Architecture:* `api: 238`, `import: 22`
* *Defense:* `safety: 236`, `test: 563`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, pandas._libs, collections.abc, pytest, pandas._testing, array, re, pandas.core.dtypes.dtypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/dtypes/dtypes.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.979 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.095 IQR)
- **Top Global Matches:** file_cluster_0: 12.979, file_cluster_13: 12.988, file_cluster_11: 13.069
- **Magnitude:** 1018.3 | **LOC:** 2497 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (31.6094%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 48.6)
  * `type` (Impact: 47.6)
  * `__eq__` (Impact: 28.5)
  * `_get_common_dtype` (Impact: 27.4)
  * `_get_common_dtype` (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 538`, `args: 127`, `func_start: 127`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 86`, `dead_code: 5`, `planned_debt: 12`, `duplicate_logic: 95`
* *Architecture:* `api: 81`, `import: 70`
* *Defense:* `safety: 106`, `doc: 134`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.154
  * `Choke Point (Betweenness):` 0.003066 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` typing, datetime, pandas._libs, pandas.core.dtypes.inference, collections.abc, pandas._config.config, pandas.core.arrays, pandas.core.arrays.integer...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `pandas/core/reshape/merge.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.492 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.925 IQR)
- **Top Global Matches:** file_cluster_13: 12.492, file_cluster_8: 12.51, file_cluster_11: 12.6
- **Magnitude:** 1006.68 | **LOC:** 3139 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 11.1%
- **Risk Profile:** Cognitive Load (34.8325%), Tech Debt (11.2785%)
**Top Internal Functions/Classes:**
  * `_validate_validate_kwd` (Impact: 475.6)
  * `_maybe_coerce_merge_keys` (Impact: 146.5)
    * *Intent:* # Overridden by AsOfMerge pass @final def _reindex_and_concat( self, join_index: Index, left_indexer...
  * `_validate_left_right_on` (Impact: 76.0)
  * `_maybe_restore_index_levels` (Impact: 13.4)
  * `_indicator_name` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `structural_boundaries: 246`, `args: 59`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 175`, `dead_code: 10`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 37`
* *Defense:* `safety: 80`, `doc: 52`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.338
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` typing, datetime, pandas._libs, collections.abc, pandas.core.arrays, pandas.core.sorting, pandas._libs.lib, pandas.core.dtypes.missing...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/tests/io/formats/test_format.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.289 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.383 IQR)
- **Top Global Matches:** file_cluster_8: 11.289, file_cluster_7: 11.887, file_cluster_0: 11.902
- **Magnitude:** 972.96 | **LOC:** 2303 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (4.7469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `has_info_repr` (Impact: 309.0)
  * `test_east_asian_unicode_series` (Impact: 41.9)
  * `test_format_percentiles_integer_idx` (Impact: 41.7)
  * `test_to_string_truncate_indices` (Impact: 30.1)
  * `test_max_multi_index_display` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 423`, `args: 108`, `func_start: 106`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 64`
* *Architecture:* `io: 1`, `api: 111`, `import: 10`
* *Defense:* `safety: 277`, `doc: 6`, `test: 385`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, pandas, pytest, pandas.io.formats.format, numpy, shutil, re, pandas.io.formats...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/internals/managers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.253 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_16: 12.253, file_cluster_11: 12.305, file_cluster_13: 12.329
- **Magnitude:** 943.4 | **LOC:** 2557 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (23.9294%), Tech Debt (40.1312%)
**Top Internal Functions/Classes:**
  * `_verify_integrity` (Impact: 402.9)
  * `setitem` (Impact: 40.6)
  * `_combine` (Impact: 17.5)
  * `get_bool_data` (Impact: 11.1)
    * *Intent:* # this method is only called if there is a single block -> hardcoded 0
  * `copy` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 378`, `args: 132`, `func_start: 130`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 143`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 104`, `import: 30`
* *Defense:* `safety: 46`, `doc: 140`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.667
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` typing, pandas._libs, collections.abc, pandas._config.config, pandas.core.arrays, pandas.api.extensions, pandas.core.dtypes.missing, pandas.core.construction...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pandas/io/formats/format.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.282 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.978 IQR)
- **Top Global Matches:** file_cluster_13: 12.282, file_cluster_16: 12.375, file_cluster_11: 12.441
- **Magnitude:** 937.36 | **LOC:** 2077 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (18.2919%), Tech Debt (94.9141%)
**Top Internal Functions/Classes:**
  * `get_result_as_array` (Impact: 70.5)
  * `_format_strings` (Impact: 50.2)
  * `_get_footer` (Impact: 29.8)
  * `_get_strcols_without_index` (Impact: 24.8)
  * `to_string` (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 298`, `args: 96`, `func_start: 90`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 201`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 16`
* *Architecture:* `io: 1`, `api: 55`, `import: 36`
* *Defense:* `safety: 33`, `doc: 76`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.882
  * `Choke Point (Betweenness):` 0.003645 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` typing, pandas._libs, collections.abc, pandas._config.config, pandas.core.arrays, contextlib, pandas.core.dtypes.missing, io...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `pandas/tests/series/indexing/test_setitem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.68 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.979 IQR)
- **Top Global Matches:** file_cluster_8: 10.68, file_cluster_0: 10.742, file_cluster_7: 11.184
- **Magnitude:** 887.62 | **LOC:** 1846 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (4.2815%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_int_key` (Impact: 56.0)
  * `test_slice_key` (Impact: 37.2)
  * `test_20643` (Impact: 34.7)
  * `test_series_where` (Impact: 29.6)
  * `test_mask_key` (Impact: 29.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 348`, `args: 151`, `func_start: 149`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 79`, `orphaned_logic: 67`
* *Architecture:* `api: 183`, `import: 12`
* *Defense:* `safety: 59`, `doc: 16`, `test: 362`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` datetime, pandas.errors, pandas.core.dtypes.common, pandas, pytest, pandas._testing, contextlib, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/frame/test_reductions.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.006 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.024 IQR)
- **Top Global Matches:** file_cluster_8: 11.006, file_cluster_0: 11.377, file_cluster_7: 11.566
- **Magnitude:** 883.84 | **LOC:** 2235 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.2901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_min_max_dt64_with_NaT_skipna_false` (Impact: 232.0)
  * `test_stat_op_api_float_string_frame` (Impact: 55.7)
  * `test_any_all_np_func` (Impact: 43.6)
  * `test_idxmin` (Impact: 30.3)
  * `test_idxmax` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 230`, `args: 113`, `func_start: 108`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 66`
* *Architecture:* `api: 112`, `import: 13`
* *Defense:* `safety: 126`, `doc: 8`, `test: 273`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, pandas, pytest, pandas._testing, dateutil.tz, numpy, decimal, pandas.compat.numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/plotting/frame/test_frame.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.138 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.581 IQR)
- **Top Global Matches:** file_cluster_8: 11.138, file_cluster_0: 11.295, file_cluster_7: 11.659
- **Magnitude:** 874.0 | **LOC:** 2659 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (4.6935%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unordered_ts` (Impact: 197.7)
  * `test_plain_axes_make_inset_axes` (Impact: 86.0)
  * `test_invalid_logscale` (Impact: 10.9)
  * `test_bar_barwidth` (Impact: 9.5)
  * `test_boxplot_vertical_subplots` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 343`, `args: 184`, `func_start: 181`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `orphaned_logic: 101`
* *Architecture:* `api: 173`, `import: 16`
* *Defense:* `safety: 149`, `doc: 4`, `test: 456`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` datetime, pandas.tests.plotting.common, mpl_toolkits.axes_grid1, pandas, mpl_toolkits.axes_grid1.inset_locator, pytest, pandas._testing, pandas.io.formats.printing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pandas/tests/dtypes/test_generic.py` (PYTHON) | Magnitude: 53.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 32, safety: 28, test: 25
- `pandas/io/pytables.py` (PYTHON) | Magnitude: 1115.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 3318, branch: 820, structural_boundaries: 681, encapsulation: 422
- `pandas/tests/util/test_deprecate_nonkeyword_arguments.py` (PYTHON) | Magnitude: 120.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 56, test: 39, branch: 28
- `pandas/core/dtypes/dtypes.py` (PYTHON) | Magnitude: 1018.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1189, structural_boundaries: 538, branch: 325, encapsulation: 195
- `pandas/_libs/tslibs/offsets.pyx` (PYTHON) | Magnitude: 506.2 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2509, encapsulation: 944, structural_boundaries: 665, branch: 589

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pandas/core/groupby/grouper.py` (PYTHON) | Magnitude: 205.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 462, branch: 142, structural_boundaries: 123, encapsulation: 97

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pandas/core/indexes/timedeltas.py` (PYTHON) | Magnitude: 38.9 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 61, encapsulation: 38, branch: 34
- `pandas/util/_validators.py` (PYTHON) | Magnitude: 161.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 144, branch: 70, structural_boundaries: 46, doc: 30
- `pandas/tests/arrays/string_/test_concat.py` (PYTHON) | Magnitude: 21.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 26, test: 15, safety: 9
- `pandas/io/formats/printing.py` (PYTHON) | Magnitude: 159.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 309, branch: 121, structural_boundaries: 90, encapsulation: 57
- `pandas/tests/frame/indexing/test_insert.py` (PYTHON) | Magnitude: 61.32 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 21, structural_boundaries: 17, test: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pandas/_testing/_warnings.py` (PYTHON) | Magnitude: 21.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, branch: 62, structural_boundaries: 41, generics: 20
- `pandas/_libs/reshape.pyi` (PYTHON) | Magnitude: 6.78 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 4, generics: 3
- `pandas/core/interchange/dataframe_protocol.py` (PYTHON) | Magnitude: 35.2 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 98, doc: 68, structural_boundaries: 45, decorators: 36
- `scripts/validate_min_versions_in_sync.py` (PYTHON) | Magnitude: 120.5 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 187, branch: 63, structural_boundaries: 45, generics: 24
- `pandas/_libs/join.pyi` (PYTHON) | Magnitude: 36.84 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, api: 22, generics: 20, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pandas/tests/indexes/datetimes/methods/test_to_julian_date.py` (PYTHON) | Magnitude: 34.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 17, branch: 10, safety: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `doc/source/user_guide/templates/html_table_structure.html` (HTML) | Magnitude: 15.68 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, ui_framework: 12, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pandas/tests/extension/base/casting.py` (PYTHON) | Magnitude: 57.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 37, test: 24, safety: 19
- `pandas/tests/series/test_subclass.py` (PYTHON) | Magnitude: 38.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 28, test: 17, args: 10
- `pandas/tests/test_common.py` (PYTHON) | Magnitude: 107.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 85, test: 62, safety: 28
- `pandas/tests/dtypes/test_common.py` (PYTHON) | Magnitude: 345.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 311, test: 283, safety: 190
- `pandas/tests/indexes/interval/test_indexing.py` (PYTHON) | Magnitude: 234.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 522, test: 130, structural_boundaries: 112, safety: 58

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pandas/core/series.py` -> Churn: **87.81%** | Cog Load: 6.6068% | Debt: 99.4783%
- `pandas/core/generic.py` -> Churn: **85.31%** | Cog Load: 13.0204% | Debt: 50.0159%
- `pandas/core/resample.py` -> Churn: **69.05%** | Cog Load: 16.7109% | Debt: 99.9829%
- `pandas/core/arrays/masked.py` -> Churn: **65.51%** | Cog Load: 19.8326% | Debt: 50.6313%
- `pandas/core/groupby/groupby.py` -> Churn: **64.42%** | Cog Load: 9.0678% | Debt: 74.5934%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/check_test_naming.py` -> **Richard Shadrach** (100.0% isolated ownership) | Magnitude: 1197.35
- `pandas/tests/arithmetic/test_timedelta64.py` -> **jbrockmendel** (91.7% isolated ownership) | Magnitude: 780.66
- `pandas/tests/arithmetic/test_datetime64.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 717.42
- `asv_bench/benchmarks/groupby.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 679.68
- `asv_bench/benchmarks/frame_methods.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 646.64

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

- `pandas/_typing.py` -> **Severity: 4948.61** (Blast Radius: 63.929 * Doc Risk: 77.4079%)
- `pandas/util/_exceptions.py` -> **Severity: 1500.152** (Blast Radius: 33.187 * Doc Risk: 45.203%)
- `pandas/_testing/compat.py` -> **Severity: 1197.62** (Blast Radius: 14.222 * Doc Risk: 84.209%)
- `pandas/core/common.py` -> **Severity: 548.9** (Blast Radius: 5.489 * Doc Risk: 100.0%)
- `asv_bench/benchmarks/pandas_vb_common.py` -> **Severity: 443.415** (Blast Radius: 6.366 * Doc Risk: 69.6536%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
