# ARCHITECTURAL_BRIEF: numpy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/numpy` |
| **Timestamp** | `2026-08-07T04:00:49.771245+00:00` |
| **Scan Duration** | `8.75s` |
| **Git Branch** | `main` |
| **Git Commit** | `5bceafeb63c6049a579d8163bd9d6b54171731a8` |
| **Git Remote** | `https://github.com/numpy/numpy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1242 malicious artifacts.

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
| Total Artifacts | 2334 |
| Analyzed Artifacts (Scanned) | 1312 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1022 |
| Total LOC | 280716 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 56.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6092 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4069 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9603 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 56 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 657 | 153292 | 50.1% |
| C | 377 | 103738 | 28.7% |
| FORTRAN | 114 | 2338 | 8.7% |
| CPP | 81 | 20104 | 6.2% |
| PLAINTEXT | 32 | 0 | 2.4% |
| XML | 15 | 4 | 1.1% |
| MARKDOWN | 13 | 0 | 1.0% |
| SHELL | 7 | 91 | 0.5% |
| MAKEFILE | 4 | 213 | 0.3% |
| YAML | 3 | 120 | 0.2% |
| JSON | 3 | 26 | 0.2% |
| CSV | 2 | 629 | 0.2% |
| BATCH | 1 | 61 | 0.1% |
| CSS | 1 | 73 | 0.1% |
| HTML | 1 | 21 | 0.1% |
| M4 | 1 | 6 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.758`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 860 | 65.5% |
| file_cluster_13 | 257 | 19.6% |
| file_cluster_16 | 83 | 6.3% |
| file_cluster_0 | 38 | 2.9% |
| file_cluster_12 | 6 | 0.5% |
| file_cluster_9 | 6 | 0.5% |
| file_cluster_17 | 5 | 0.4% |
| file_cluster_7 | 3 | 0.2% |
| file_cluster_4 | 3 | 0.2% |
| file_cluster_6 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 45 | 3.4% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1022*

**Composition by Extension & Reason:**
- `.rst`: 379x Excluded (Unsupported Extension: '.rst'), 184x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 183 LOC), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC)
- `.png`: 57x Excluded (Explicitly Denied Extension: '.png')
- `.pyi`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.src`: 37x Unsupported Format (.src), 1x Excluded (Embedded Hex Payload: 1098 hex tokens in 716 LOC)
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 14x Excluded (Static Asset Blob without Intent: 1430 LOC), 10x Excluded (Static Asset Blob without Intent: 1002 LOC), 2x Excluded (Static Asset Blob without Intent: 1630 LOC)
- `.build`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyf`: 10x Unsupported Format (.pyf), 9x Excluded (Unsupported Extension: '.pyf')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.dat`: 17x Excluded (Unsupported Extension: '.dat')
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1472 LOC), 1x Excluded (Static Asset Blob without Intent: 2213 LOC)
- `.patch`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.i`: 9x Unsupported Format (.i)
- `.tmpl`: 7x Excluded (Unsupported Extension: '.tmpl')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.0 | 5.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 45.3 | 56.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.3 | 1.7 | 0.0 |
| API Exposure | 0.0 | 19.5 | 5.6 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.5 | 14.4 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `numpy/_core/tests/test_multiarray.py` (Hits: 80)
- `numpy/f2py/f2py2e.py` (Hits: 55)
- `numpy/linalg/lapack_lite/make_lite.py` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **numpy.css** (`doc/source/_static/numpy.css`) — 431 inbound connections
2. **npy_config.h** (`numpy/_core/src/common/npy_config.h`) — 53 inbound connections
3. **common.h** (`numpy/_core/src/multiarray/common.h`) — 46 inbound connections
4. **dtypemeta.h** (`numpy/_core/src/multiarray/dtypemeta.h`) — 42 inbound connections
5. **_utils.py** (`numpy/core/_utils.py`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **multiarraymodule.c** (`numpy/_core/src/multiarray/multiarraymodule.c`) — 60 outbound dependencies
2. **__init__.pyi** (`numpy/__init__.pyi`) — 54 outbound dependencies
3. **__init__.py** (`numpy/__init__.py`) — 47 outbound dependencies
4. **test_multiarray.py** (`numpy/_core/tests/test_multiarray.py`) — 41 outbound dependencies
5. **utils.py** (`numpy/testing/_private/utils.py`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `clarfb_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **1579.2** | LOC: 2304
- `zlarfb_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **1571.6** | LOC: 2312
- `zungbr_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **1217.0** | LOC: 1455
  * *Intent:* */
- `cungbr_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **1216.7** | LOC: 1450
- `test_tofile_format` (@ `numpy/_core/tests/test_multiarray.py`) -> Impact: **1010.3** | LOC: 4822
- `zlahqr_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **986.6** | LOC: 2072
- `zlaqr4_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **976.1** | LOC: 2212
- `claqr4_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **975.8** | LOC: 2206
- `min_scalar_type_num` (@ `numpy/_core/src/multiarray/convert_datatype.c`) -> Impact: **915.2** | LOC: 1744
- `PyArray_NewFromDescr_int` (@ `numpy/_core/src/multiarray/ctors.c`) -> Impact: **905.9** | LOC: 1616
  * *Intent:* /* * Assuming that the separator is the next bit in the string (file), skip it. * * Single spaces in the separator are matched to arbitrary-long seque...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `numpy/linalg/lapack_lite` | 13 | 54008.34 | 45.47% | 25.41% |
| `numpy/_core/src/multiarray` | 110 | 51199.04 | 40.99% | 17.7% |
| `numpy/_core/tests` | 67 | 22816.7 | 6.81% | 0.0% |
| `numpy/_core/src/umath` | 37 | 19388.58 | 46.62% | 18.97% |
| `numpy/f2py` | 34 | 8713.43 | 12.19% | 10.16% |
| `numpy/_core` | 61 | 8671.3 | 9.88% | 31.28% |
| `numpy/_core/src/common` | 54 | 7185.42 | 36.16% | 25.13% |
| `numpy/_core/src/npysort` | 18 | 6862.76 | 54.98% | 35.54% |
| `numpy/ma` | 11 | 5182.88 | 7.2% | 41.77% |
| `numpy/linalg` | 8 | 5030.7 | 16.88% | 26.33% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_array_coercion.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_clip.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_creation.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/benchmarks/bench_itemselection.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_records.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_strings.py` -> **100.0%** Exposure
- `numpy/dtypes.py` -> **100.0%** Exposure
- `numpy/exceptions.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `numpy/_core/tests/test_multiarray.py` -> **299** Orphaned Functions | **86** Duplicates
- `numpy/ma/tests/test_core.py` -> **261** Orphaned Functions | **16** Duplicates
- `numpy/_core/tests/test_umath.py` -> **188** Orphaned Functions | **87** Duplicates
- `numpy/_core/tests/test_numeric.py` -> **175** Orphaned Functions | **12** Duplicates
- `numpy/_core/tests/test_regression.py` -> **180** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`numpy/f2py/f2py2e.py`** -> AI Confidence: **99.48%**
2. **`numpy/_core/src/multiarray/einsum.cpp`** -> AI Confidence: **99.48%**
3. **`meson_cpu/x86/test_x86_v2.c`** -> AI Confidence: **99.48%**
4. **`numpy/_core/src/common/cblasfuncs.c`** -> AI Confidence: **99.48%**
5. **`numpy/_core/src/multiarray/array_assign_array.c`** -> AI Confidence: **99.48%**
6. **`numpy/_core/src/multiarray/arraywrap.c`** -> AI Confidence: **99.48%**
7. **`numpy/_core/src/multiarray/common_dtype.c`** -> AI Confidence: **99.48%**
8. **`numpy/_core/src/multiarray/compiled_base.c`** -> AI Confidence: **99.48%**
9. **`numpy/_core/src/multiarray/datetime_busday.c`** -> AI Confidence: **99.48%**
10. **`numpy/_core/src/multiarray/datetime_busdaycal.c`** -> AI Confidence: **99.48%**
11. **`numpy/_core/src/multiarray/datetime_strings.c`** -> AI Confidence: **99.48%**
12. **`numpy/_core/src/multiarray/item_selection.c`** -> AI Confidence: **99.48%**
13. **`numpy/_core/src/multiarray/mapping.c`** -> AI Confidence: **99.48%**
14. **`numpy/_core/src/multiarray/nditer_constr.c`** -> AI Confidence: **99.48%**
15. **`numpy/_core/src/multiarray/textreading/rows.c`** -> AI Confidence: **99.48%**
16. **`numpy/_core/src/umath/override.c`** -> AI Confidence: **99.48%**
17. **`numpy/_core/src/umath/reduction.c`** -> AI Confidence: **99.48%**
18. **`numpy/_core/src/umath/ufunc_object.c`** -> AI Confidence: **99.48%**
19. **`numpy/_core/src/multiarray/common.h`** -> AI Confidence: **99.42%**
20. **`numpy/_core/src/common/lowlevel_strided_loops.h`** -> AI Confidence: **99.42%**
21. **`numpy/_core/src/common/npy_config.h`** -> AI Confidence: **99.42%**
22. **`numpy/_core/einsumfunc.py`** -> AI Confidence: **99.39%**
23. **`numpy/f2py/capi_maps.py`** -> AI Confidence: **99.39%**
24. **`numpy/f2py/rules.py`** -> AI Confidence: **99.39%**
25. **`numpy/_core/src/common/npy_argparse.c`** -> AI Confidence: **99.39%**
26. **`numpy/_core/src/common/npy_cpu_features.c`** -> AI Confidence: **99.39%**
27. **`numpy/_core/src/common/numpyos.c`** -> AI Confidence: **99.39%**
28. **`numpy/_core/src/multiarray/array_assign_scalar.c`** -> AI Confidence: **99.39%**
29. **`numpy/_core/src/multiarray/arrayobject.c`** -> AI Confidence: **99.39%**
30. **`numpy/_core/src/multiarray/common.c`** -> AI Confidence: **99.39%**
31. **`numpy/_core/src/multiarray/ctors.c`** -> AI Confidence: **99.39%**
32. **`numpy/_core/src/multiarray/descriptor.c`** -> AI Confidence: **99.39%**
33. **`numpy/_core/src/multiarray/dlpack.c`** -> AI Confidence: **99.39%**
34. **`numpy/_core/src/multiarray/iterators.c`** -> AI Confidence: **99.39%**
35. **`numpy/_core/src/multiarray/legacy_dtype_implementation.c`** -> AI Confidence: **99.39%**
36. **`numpy/_core/src/multiarray/shape.c`** -> AI Confidence: **99.39%**
37. **`numpy/_core/src/multiarray/temp_elide.c`** -> AI Confidence: **99.39%**
38. **`numpy/_core/src/multiarray/usertypes.c`** -> AI Confidence: **99.39%**
39. **`numpy/_core/src/multiarray/buffer.c`** -> AI Confidence: **99.35%**
40. **`numpy/_core/src/multiarray/convert_datatype.c`** -> AI Confidence: **99.35%**
41. **`numpy/_core/src/multiarray/textreading/readtext.c`** -> AI Confidence: **99.35%**
42. **`numpy/_core/src/umath/special_integer_comparisons.cpp`** -> AI Confidence: **99.34%**
43. **`numpy/_core/src/multiarray/array_method.c`** -> AI Confidence: **99.34%**
44. **`numpy/_core/src/multiarray/datetime.c`** -> AI Confidence: **99.34%**
45. **`numpy/_core/src/umath/extobj.c`** -> AI Confidence: **99.34%**
46. **`numpy/random/src/pcg64/pcg64-benchmark.c`** -> AI Confidence: **99.34%**
47. **`numpy/_core/src/common/npy_cpuinfo_parser.h`** -> AI Confidence: **99.34%**
48. **`numpy/_core/src/common/python_xerbla.c`** -> AI Confidence: **99.32%**
49. **`numpy/linalg/lapack_lite/python_xerbla.c`** -> AI Confidence: **99.32%**
50. **`numpy/random/src/distributions/random_hypergeometric.c`** -> AI Confidence: **99.32%**
51. **`numpy/random/src/mt19937/mt19937-test-data-gen.c`** -> AI Confidence: **99.32%**
52. **`numpy/random/src/pcg64/pcg64-test-data-gen.c`** -> AI Confidence: **99.32%**
53. **`doc/source/conf.py`** -> AI Confidence: **99.31%**
54. **`numpy/_build_utils/tempita/_tempita.py`** -> AI Confidence: **99.31%**
55. **`numpy/_core/_internal.py`** -> AI Confidence: **99.31%**
56. **`numpy/_core/_methods.py`** -> AI Confidence: **99.31%**
57. **`numpy/_core/arrayprint.py`** -> AI Confidence: **99.31%**
58. **`numpy/_core/function_base.py`** -> AI Confidence: **99.31%**
59. **`numpy/_core/memmap.py`** -> AI Confidence: **99.31%**
60. **`numpy/_core/records.py`** -> AI Confidence: **99.31%**
61. **`numpy/_core/tests/test_cpu_features.py`** -> AI Confidence: **99.31%**
62. **`numpy/_core/tests/test_extint128.py`** -> AI Confidence: **99.31%**
63. **`numpy/_core/tests/test_nditer.py`** -> AI Confidence: **99.31%**
64. **`numpy/_core/tests/test_stringdtype.py`** -> AI Confidence: **99.31%**
65. **`numpy/_core/tests/test_strings.py`** -> AI Confidence: **99.31%**
66. **`numpy/f2py/_backends/_meson.py`** -> AI Confidence: **99.31%**
67. **`numpy/fft/_pocketfft.py`** -> AI Confidence: **99.31%**
68. **`numpy/linalg/_linalg.py`** -> AI Confidence: **99.31%**
69. **`numpy/ma/core.py`** -> AI Confidence: **99.31%**
70. **`numpy/ma/extras.py`** -> AI Confidence: **99.31%**
71. **`numpy/random/_generator.pyx`** -> AI Confidence: **99.31%**
72. **`numpy/random/mtrand.pyx`** -> AI Confidence: **99.31%**
73. **`numpy/testing/_private/utils.py`** -> AI Confidence: **99.31%**
74. **`numpy/tests/test_public_api.py`** -> AI Confidence: **99.31%**
75. **`tools/c_coverage/c_coverage_report.py`** -> AI Confidence: **99.31%**
76. **`tools/check_python_h_first.py`** -> AI Confidence: **99.31%**
77. **`tools/ci/check_c_api_usage.py`** -> AI Confidence: **99.31%**
78. **`tools/refguide_check.py`** -> AI Confidence: **99.31%**
79. **`numpy/_core/src/multiarray/stringdtype/casts.cpp`** -> AI Confidence: **99.31%**
80. **`numpy/_core/src/umath/dispatching.cpp`** -> AI Confidence: **99.31%**
81. **`numpy/_core/src/umath/real_imag_ufuncs.cpp`** -> AI Confidence: **99.31%**
82. **`numpy/_core/src/umath/string_ufuncs.cpp`** -> AI Confidence: **99.31%**
83. **`numpy/_core/src/umath/stringdtype_ufuncs.cpp`** -> AI Confidence: **99.31%**
84. **`numpy/_core/tests/data/generate_umath_validation_data.cpp`** -> AI Confidence: **99.31%**
85. **`numpy/_core/src/common/array_assign.c`** -> AI Confidence: **99.31%**
86. **`numpy/_core/src/common/mem_overlap.c`** -> AI Confidence: **99.31%**
87. **`numpy/_core/src/common/ufunc_override.c`** -> AI Confidence: **99.31%**
88. **`numpy/_core/src/multiarray/abstractdtypes.c`** -> AI Confidence: **99.31%**
89. **`numpy/_core/src/multiarray/array_coercion.c`** -> AI Confidence: **99.31%**
90. **`numpy/_core/src/multiarray/array_converter.c`** -> AI Confidence: **99.31%**
91. **`numpy/_core/src/multiarray/arrayfunction_override.c`** -> AI Confidence: **99.31%**
92. **`numpy/_core/src/multiarray/calculation.c`** -> AI Confidence: **99.31%**
93. **`numpy/_core/src/multiarray/conversion_utils.c`** -> AI Confidence: **99.31%**
94. **`numpy/_core/src/multiarray/convert.c`** -> AI Confidence: **99.31%**
95. **`numpy/_core/src/multiarray/dtype_transfer.c`** -> AI Confidence: **99.31%**
96. **`numpy/_core/src/multiarray/dtypemeta.c`** -> AI Confidence: **99.31%**
97. **`numpy/_core/src/multiarray/flagsobject.c`** -> AI Confidence: **99.31%**
98. **`numpy/_core/src/multiarray/getset.c`** -> AI Confidence: **99.31%**
99. **`numpy/_core/src/multiarray/methods.c`** -> AI Confidence: **99.31%**
100. **`numpy/_core/src/multiarray/multiarraymodule.c`** -> AI Confidence: **99.31%**
101. **`numpy/_core/src/multiarray/nditer_pywrap.c`** -> AI Confidence: **99.31%**
102. **`numpy/_core/src/multiarray/npy_static_data.c`** -> AI Confidence: **99.31%**
103. **`numpy/_core/src/multiarray/number.c`** -> AI Confidence: **99.31%**
104. **`numpy/_core/src/multiarray/public_dtype_api.c`** -> AI Confidence: **99.31%**
105. **`numpy/_core/src/multiarray/refcount.c`** -> AI Confidence: **99.31%**
106. **`numpy/_core/src/multiarray/scalarapi.c`** -> AI Confidence: **99.31%**
107. **`numpy/_core/src/multiarray/sequence.c`** -> AI Confidence: **99.31%**
108. **`numpy/_core/src/multiarray/stringdtype/dtype.c`** -> AI Confidence: **99.31%**
109. **`numpy/_core/src/multiarray/stringdtype/static_string.c`** -> AI Confidence: **99.31%**
110. **`numpy/_core/src/umath/_rational_tests.c`** -> AI Confidence: **99.31%**
111. **`numpy/_core/src/umath/legacy_array_method.c`** -> AI Confidence: **99.31%**
112. **`numpy/_core/src/umath/ufunc_type_resolution.c`** -> AI Confidence: **99.31%**
113. **`numpy/_core/src/umath/wrapping_array_method.c`** -> AI Confidence: **99.31%**
114. **`numpy/random/src/mt19937/randomkit.c`** -> AI Confidence: **99.31%**
115. **`numpy/_core/src/common/simd/simd.h`** -> AI Confidence: **99.31%**
116. **`numpy/__init__.pxd`** -> AI Confidence: **99.29%**
117. **`numpy/f2py/_isocbind.py`** -> AI Confidence: **99.29%**
118. **`numpy/random/_bounded_integers.pyx.in`** -> AI Confidence: **99.29%**
119. **`tools/swig/Makefile`** -> AI Confidence: **99.29%**
120. **`tools/swig/test/SuperTensor.cxx`** -> AI Confidence: **99.29%**
121. **`tools/swig/test/Tensor.cxx`** -> AI Confidence: **99.29%**
122. **`numpy/f2py/tests/src/crackfortran/gh23533.f`** -> AI Confidence: **99.29%**
123. **`meson_cpu/x86/test_x86_v3.c`** -> AI Confidence: **99.29%**
124. **`meson_cpu/x86/test_x86_v4.c`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4607` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `numpy/_core/src/multiarray/hashdescr.c` (C) -> Cumulative Risk: **696.14**
- **Archetype:** `file_cluster_8` (Distance: 11.861 IQR)
- **Magnitude:** 230.64 | **LOC:** 319 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Concurrency (98.6795%)
- **Heaviest Functions:** `_array_descr_walk_fields` (Impact: 41.9), `_array_descr_walk_subarray` (Impact: 15.7), `_normalize_byteorder` (Impact: 11.1)

### 2. `numpy/_core/src/common/npy_import.c` (C) -> Cumulative Risk: **692.4**
- **Archetype:** `file_cluster_4` (Distance: 12.206 IQR)
- **Magnitude:** 102.04 | **LOC:** 89 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9988%)
- **Heaviest Functions:** `npy_import_entry_point` (Impact: 17.6), `npy_cache_import_runtime` (Impact: 17.2), `init_import_mutex` (Impact: 4.8)

### 3. `numpy/_core/src/common/npy_argparse.c` (C) -> Cumulative Risk: **686.51**
- **Archetype:** `file_cluster_13` (Distance: 13.588 IQR)
- **Magnitude:** 482.1 | **LOC:** 416 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.2929%)
- **Heaviest Functions:** `_npy_parse_arguments` (Impact: 108.9), `initialize_keywords` (Impact: 59.5), `raise_incorrect_number_of_positional_arg` (Impact: 8.9)

### 4. `numpy/random/src/distributions/distributions.c` (C) -> Cumulative Risk: **683.59**
- **Archetype:** `file_cluster_8` (Distance: 13.6 IQR)
- **Magnitude:** 1031.68 | **LOC:** 1747 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3703%)
- **Heaviest Functions:** `random_bounded_uint64` (Impact: 55.0), `random_buffered_bounded_uint8` (Impact: 21.6), `random_standard_gamma` (Impact: 19.2)

### 5. `numpy/_core/src/multiarray/nditer_api.c` (C) -> Cumulative Risk: **680.08**
- **Archetype:** `file_cluster_0` (Distance: 15.161 IQR)
- **Magnitude:** 1227.42 | **LOC:** 2327 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5091%), Documentation (95.1135%)
- **Heaviest Functions:** `npyiter_fill_buffercopy_params` (Impact: 212.5), `npyiter_copy_to_buffers` (Impact: 30.9), `NpyIter_GetInnerFixedStrideArray` (Impact: 21.0)

### 6. `numpy/_core/src/umath/ufunc_object.c` (C) -> Cumulative Risk: **671.89**
- **Archetype:** `file_cluster_8` (Distance: 14.75 IQR)
- **Magnitude:** 5025.46 | **LOC:** 6804 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 22.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.1585%)
- **Heaviest Functions:** `_parse_axis_arg` (Impact: 772.0), `ufunc_at` (Impact: 160.1), `convert_ufunc_arguments` (Impact: 122.3)

### 7. `numpy/_core/src/multiarray/ctors.c` (C) -> Cumulative Risk: **670.55**
- **Archetype:** `file_cluster_13` (Distance: 13.906 IQR)
- **Magnitude:** 3410.56 | **LOC:** 4208 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 18.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.2441%), Safety Score (93.8846%)
- **Heaviest Functions:** `PyArray_NewFromDescr_int` (Impact: 905.9), `PyArray_NewLikeArrayWithShape` (Impact: 759.3), `_dtype_from_buffer_3118` (Impact: 194.2)

### 8. `numpy/_core/src/multiarray/calculation.c` (C) -> Cumulative Risk: **658.0**
- **Archetype:** `file_cluster_8` (Distance: 13.016 IQR)
- **Magnitude:** 818.6 | **LOC:** 882 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.8542%)
- **Heaviest Functions:** `PyArray_Round` (Impact: 45.1), `__New_PyArray_Std` (Impact: 43.8), `_PyArray_ArgMinMaxCommon` (Impact: 39.6)

### 9. `numpy/_core/src/multiarray/convert.c` (C) -> Cumulative Risk: **654.98**
- **Archetype:** `file_cluster_13` (Distance: 12.419 IQR)
- **Magnitude:** 315.4 | **LOC:** 571 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (89.9725%)
- **Heaviest Functions:** `PyArray_ToFile` (Impact: 34.4), `PyArray_ToString` (Impact: 17.8), `PyArray_View` (Impact: 8.1)

### 10. `numpy/_core/src/multiarray/multiarraymodule.c` (C) -> Cumulative Risk: **653.32**
- **Archetype:** `file_cluster_8` (Distance: 14.081 IQR)
- **Magnitude:** 2198.18 | **LOC:** 5317 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 27.8%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.0016%)
- **Heaviest Functions:** `_multiarray_umath_exec` (Impact: 77.5), `PyArray_Where` (Impact: 71.3), `einsum_list_to_subscripts` (Impact: 26.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `numpy/linalg/lapack_lite/f2c_z_lapack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.91 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.13 IQR)
- **Top Global Matches:** file_cluster_8: 15.91, file_cluster_7: 16.207, file_cluster_13: 16.255
- **Magnitude:** 21264.96 | **LOC:** 29997 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9803%), Tech Debt (9.8101%)
**Top Internal Functions/Classes:**
  * `zlarfb_` (Impact: 1571.6)
  * `zungbr_` (Impact: 1217.0)
    * *Intent:* */
  * `zlahqr_` (Impact: 986.6)
  * `zlaqr4_` (Impact: 976.1)
  * `zgesdd_` (Impact: 768.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 147`, `args: 165`, `func_start: 47`
* *Risk/State:* `state_mutation: 11299`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 434`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` f2c.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_c_lapack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.932 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.138 IQR)
- **Top Global Matches:** file_cluster_8: 15.932, file_cluster_7: 16.228, file_cluster_13: 16.276
- **Magnitude:** 20848.98 | **LOC:** 29862 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1508%), Tech Debt (9.835%)
**Top Internal Functions/Classes:**
  * `clarfb_` (Impact: 1579.2)
  * `cungbr_` (Impact: 1216.7)
  * `claqr4_` (Impact: 975.8)
  * `cgesdd_` (Impact: 768.0)
    * *Intent:* /* If INFO > 0 from CHSEQR, then quit */
  * `clahqr_` (Impact: 498.1)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 147`, `args: 175`, `func_start: 47`
* *Risk/State:* `state_mutation: 11293`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 415`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` f2c.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_blas.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_8: 15.653, file_cluster_7: 15.987, file_cluster_13: 15.99
- **Magnitude:** 9072.62 | **LOC:** 21604 | **CtrlFlow:** 91.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3568%), Tech Debt (16.7056%)
**Top Internal Functions/Classes:**
  * `ssyr2k_` (Impact: 283.0)
  * `dsyr2k_` (Impact: 282.9)
  * `dsymv_` (Impact: 165.4)
    * *Intent:* /* Form C := alpha*conjg( A' )*conjg( B' ) + beta*C. */
  * `ssymv_` (Impact: 165.4)
  * `dsyr2_` (Impact: 146.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1060`, `structural_boundaries: 99`, `args: 47`, `func_start: 32`
* *Risk/State:* `state_mutation: 6824`, `orphaned_logic: 31`
* *Architecture:* `api: 185`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` f2c.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/ufunc_object.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.75 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.703 IQR)
- **Top Global Matches:** file_cluster_8: 14.75, file_cluster_13: 14.817, file_cluster_11: 14.833
- **Magnitude:** 5025.46 | **LOC:** 6804 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (92.9427%), Tech Debt (16.2574%)
**Top Internal Functions/Classes:**
  * `_parse_axis_arg` (Impact: 772.0)
  * `ufunc_at` (Impact: 160.1)
  * `convert_ufunc_arguments` (Impact: 122.3)
  * `PyUFunc_GeneralizedFunctionInternal` (Impact: 105.2)
  * `ufunc_generic_fastcall` (Impact: 95.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 851`, `structural_boundaries: 216`, `args: 5`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 2356`, `dead_code: 3`, `planned_debt: 16`, `orphaned_logic: 11`
* *Architecture:* `api: 680`, `import: 34`
* *Defense:* `safety: 15`, `doc: 15`, `test: 13`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` conversion_utils.h, scalartypes.h, dispatching.h, extobj.h, ufuncobject.h, mapping.h, reduction.h, arraywrap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/item_selection.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.504 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.347 IQR)
- **Top Global Matches:** file_cluster_8: 14.504, file_cluster_13: 14.569, file_cluster_11: 14.624
- **Magnitude:** 4197.12 | **LOC:** 3377 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (83.5518%), Tech Debt (21.144%)
**Top Internal Functions/Classes:**
  * `PyArray_Choose` (Impact: 819.4)
  * `npy_fasttake_impl` (Impact: 161.4)
    * *Intent:* #include "ctors.h" #include "lowlevel_strided_loops.h" #include "array_assign.h" #include "refcount....
  * `PyArray_LexSort` (Impact: 89.5)
  * `PyArray_PutTo` (Impact: 81.0)
  * `PyArray_Nonzero` (Impact: 66.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 120`, `args: 10`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1885`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 540`, `import: 25`
* *Defense:* `safety: 3`, `test: 3`, `immutability_locks: 59`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` methods.h, structmember.h, string.h, npy_sort.h, dtypemeta.h, refcount.h, npy_binsearch.h, common.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_multiarray.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.244 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.844 IQR)
- **Top Global Matches:** file_cluster_8: 12.244, file_cluster_0: 12.5, file_cluster_7: 12.64
- **Magnitude:** 4118.08 | **LOC:** 11172 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 11.6%
- **Risk Profile:** Cognitive Load (4.8151%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tofile_format` (Impact: 1010.3)
  * `check` (Impact: 73.0)
  * `test_ufunc_binop_interaction` (Impact: 69.6)
  * `test_argsort` (Impact: 46.9)
  * `test_np_argmin_argmax_keepdims` (Impact: 41.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 1512`, `args: 849`, `func_start: 826`, `class_start: 148`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 12`, `state_mutation: 73`, `dead_code: 10`, `planned_debt: 4`, `fragile_debt: 10`, `duplicate_logic: 86`, `orphaned_logic: 299`
* *Architecture:* `io: 80`, `api: 871`, `import: 53`
* *Defense:* `safety: 312`, `doc: 40`, `test: 1188`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` numpy.lib.recfunctions, subprocess, fractions, mmap, decimal, numpy._core, numpy._core.tests._locales, builtins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/umath_linalg.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.982 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.66 IQR)
- **Top Global Matches:** file_cluster_8: 13.982, file_cluster_13: 14.338, file_cluster_11: 14.352
- **Magnitude:** 3701.68 | **LOC:** 4812 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.4236%), Tech Debt (99.5834%)
**Top Internal Functions/Classes:**
  * `svd_wrapper` (Impact: 44.7)
  * `eig_wrapper` (Impact: 39.0)
  * `init_gesdd` (Impact: 32.4)
  * `init_gesdd` (Impact: 29.5)
  * `init_geev` (Impact: 28.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 616`, `args: 126`, `func_start: 151`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 30`, `state_mutation: 2713`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 78`, `orphaned_logic: 9`
* *Architecture:* `import: 14`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 146`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` npy_math.h, execinfo.h, utility, cmath, type_traits, ufuncobject.h, cstdio, npy_cblas.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/ctors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.906 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.306 IQR)
- **Top Global Matches:** file_cluster_13: 13.906, file_cluster_8: 13.94, file_cluster_11: 14.028
- **Magnitude:** 3410.56 | **LOC:** 4208 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (96.2441%), Tech Debt (33.6403%)
**Top Internal Functions/Classes:**
  * `PyArray_NewFromDescr_int` (Impact: 905.9)
    * *Intent:* /* * Assuming that the separator is the next bit in the string (file), skip it. * * Single spaces in...
  * `PyArray_NewLikeArrayWithShape` (Impact: 759.3)
  * `_dtype_from_buffer_3118` (Impact: 194.2)
  * `PyArray_FromInterface` (Impact: 102.4)
    * *Intent:* /* * Unless explicitly asked not to, we do replace dtypes in some cases. * This mainly means that we...
  * `PyArray_Arange` (Impact: 46.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 145`, `args: 9`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 823`, `dead_code: 3`, `planned_debt: 5`, `orphaned_logic: 15`
* *Architecture:* `io: 1`, `api: 289`, `import: 29`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` mapping.h, npy_ctypes.h, structmember.h, dtypemeta.h, refcount.h, shape.h, common.h, npy_config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dragon4.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.347 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_8: 14.347, file_cluster_13: 14.401, file_cluster_11: 14.407
- **Magnitude:** 3089.14 | **LOC:** 3215 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.971%), Tech Debt (34.4819%)
**Top Internal Functions/Classes:**
  * `BigInt_Add` (Impact: 752.4)
  * `Dragon4` (Impact: 594.4)
  * `FormatPositional` (Impact: 205.4)
  * `PrintInfNan` (Impact: 26.6)
    * *Intent:* * 2. The approximate value of k found is offset by a different amount * (0.69), in order to hit the ...
  * `BigInt_DivideWithRemainder_MaxQuotient9` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 78`, `args: 3`, `func_start: 32`, `class_start: 8`
* *Risk/State:* `state_mutation: 1027`, `dead_code: 12`, `planned_debt: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 269`, `import: 6`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` npy_common.h, dragon4.h, stdio.h, math.h, assert.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/convert_datatype.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.089 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.055 IQR)
- **Top Global Matches:** file_cluster_8: 14.089, file_cluster_13: 14.091, file_cluster_11: 14.253
- **Magnitude:** 3076.0 | **LOC:** 3582 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (84.954%), Tech Debt (26.1633%)
**Top Internal Functions/Classes:**
  * `min_scalar_type_num` (Impact: 915.2)
  * `void_to_void_resolve_descriptors` (Impact: 39.3)
  * `PyArray_ResultType` (Impact: 38.6)
  * `can_cast_fields_safety` (Impact: 27.0)
    * *Intent:* /* End deprecated */
  * `PyArray_ConvertToCommonType` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 220`, `args: 17`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1200`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 3`, `orphaned_logic: 11`
* *Architecture:* `api: 479`, `import: 30`
* *Defense:* `safety: 11`, `doc: 23`, `test: 11`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` dtype.h, can_cast_table.h, scalartypes.h, mapping.h, structmember.h, dtypemeta.h, abstractdtypes.h, array_method.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/f2py/rules.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.715 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.887 IQR)
- **Top Global Matches:** file_cluster_8: 9.715, file_cluster_7: 10.127, file_cluster_1: 10.395
- **Magnitude:** 2841.82 | **LOC:** 1642 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (4.8155%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 37`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 48`, `dead_code: 4`
* *Architecture:* `io: 13`, `api: 2`, `import: 7`
* *Defense:* `safety: 5`, `doc: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, copy, time, os, numpy, sys, , .auxfuncs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/ma/core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.392 IQR)
- **Top Global Matches:** file_cluster_8: 12.89, file_cluster_7: 12.984, file_cluster_13: 13.06
- **Magnitude:** 2715.1 | **LOC:** 8995 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 22.7%
- **Risk Profile:** Cognitive Load (27.3056%), Tech Debt (68.441%)
**Top Internal Functions/Classes:**
  * `tofile` (Impact: 481.5)
  * `_check_fill_value` (Impact: 282.7)
  * `__new__` (Impact: 187.1)
  * `var` (Impact: 56.9)
    * *Intent:* # Case 1. : no mask in input. # Erase the current mask ? # With a reduced version if shrink: _data._...
  * `__getitem__` (Impact: 49.2)
    * *Intent:* # Bas les masques !
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 773`, `args: 269`, `func_start: 268`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 204`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 22`
* *Architecture:* `api: 187`, `import: 16`
* *Defense:* `safety: 177`, `doc: 410`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` numpy._core, builtins, time., copy, numpy, re, operator, textwrap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/stringdtype_ufuncs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.495 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.354 IQR)
- **Top Global Matches:** file_cluster_8: 14.495, file_cluster_13: 14.719, file_cluster_11: 14.871
- **Magnitude:** 2679.38 | **LOC:** 3133 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (67.2287%), Tech Debt (8.6771%)
**Top Internal Functions/Classes:**
  * `all_strings_promoter` (Impact: 259.0)
  * `init_stringdtype_ufuncs` (Impact: 104.1)
  * `add_strided_loop` (Impact: 73.9)
  * `slice_strided_loop` (Impact: 62.8)
  * `string_comparison_strided_loop` (Impact: 60.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 124`, `args: 77`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 5`, `state_mutation: 1657`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `import: 19`
* *Defense:* `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` vector, dtype.h, string_ufuncs.h, dispatching.h, string_buffer.h, ufuncobject.h, string_fastsearch.h, dtypemeta.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/descriptor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.596 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.428 IQR)
- **Top Global Matches:** file_cluster_8: 13.596, file_cluster_13: 13.66, file_cluster_11: 13.727
- **Magnitude:** 2340.1 | **LOC:** 3868 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (94.9571%), Tech Debt (19.8117%)
**Top Internal Functions/Classes:**
  * `_try_convert_from_inherit_tuple` (Impact: 392.4)
  * `arraydescr_setstate` (Impact: 111.3)
  * `_convert_from_array_descr` (Impact: 77.5)
  * `_convert_from_tuple` (Impact: 44.9)
  * `_check_for_commastring` (Impact: 42.0)
    * *Intent:* /* * Sets the global typeDict object, which is a dictionary mapping * dtype names to numpy scalar ty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 201`, `args: 2`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 969`, `dead_code: 9`, `planned_debt: 6`, `orphaned_logic: 12`
* *Architecture:* `api: 368`, `import: 23`
* *Defense:* `safety: 2`, `doc: 2`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` conversion_utils.h, dtype.h, npy_ctypes.h, structmember.h, dtypemeta.h, common.h, npy_config.h, npy_pycompat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/npysort/timsort.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.001 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.388 IQR)
- **Top Global Matches:** file_cluster_8: 14.001, file_cluster_13: 14.325, file_cluster_11: 14.327
- **Magnitude:** 2265.92 | **LOC:** 2927 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.7301%), Tech Debt (99.7065%)
**Top Internal Functions/Classes:**
  * `npy_try_collapse` (Impact: 48.2)
  * `npy_count_run` (Impact: 48.0)
  * `npy_gallop_left` (Impact: 34.0)
  * `npy_gallop_right` (Impact: 33.9)
  * `npy_force_collapse` (Impact: 24.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 351`, `args: 62`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 94`, `high_risk_execution: 16`, `state_mutation: 1513`, `planned_debt: 1`, `duplicate_logic: 16`, `orphaned_logic: 49`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` npy_sort.h, cstdlib, utility, numpy_tag.h, npysort_common.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dtype_transfer.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.012 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_8: 14.012, file_cluster_13: 14.113, file_cluster_7: 14.27
- **Magnitude:** 2255.12 | **LOC:** 3835 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.8159%), Tech Debt (27.5523%)
**Top Internal Functions/Classes:**
  * `PyArray_PrepareThreeRawArrayIter` (Impact: 84.7)
  * `PyArray_PrepareOneRawArrayIter` (Impact: 55.5)
  * `get_subarray_transfer_function` (Impact: 41.9)
  * `get_n_to_n_transfer_function` (Impact: 35.9)
    * *Intent:* /* * The metadata for when dealing with Months or Years * which behave non-linearly with respect to ...
  * `get_one_to_n_transfer_function` (Impact: 29.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 161`, `args: 9`, `func_start: 31`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 1294`, `planned_debt: 5`, `fragile_debt: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 475`, `import: 19`
* *Defense:* `safety: 6`, `doc: 11`, `test: 5`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` structmember.h, dtypemeta.h, array_method.h, shape.h, dtype_traversal.h, descriptor.h, npy_math.h, lowlevel_strided_loops.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_umath.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.133 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.575 IQR)
- **Top Global Matches:** file_cluster_8: 11.133, file_cluster_0: 11.458, file_cluster_7: 11.595
- **Magnitude:** 2219.54 | **LOC:** 5150 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (5.8737%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_against_cmath` (Impact: 187.1)
  * `__array_ufunc__` (Impact: 60.7)
    * *Intent:* # wrong number of arguments in the tuple is an error too. assert_raises(TypeError, inner1d, a, out='...
  * `test_division_int_boundary` (Impact: 58.9)
    * *Intent:* # divisors # scalar divisors "range(fo.min, fo.min + 15)" ), ( # dividend "np.array(range(fo.max-lsi...
  * `test_ufunc_override_with_super` (Impact: 51.9)
  * `test_out_wrap_subok` (Impact: 40.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 675`, `args: 378`, `func_start: 343`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 34`, `dead_code: 4`, `fragile_debt: 10`, `duplicate_logic: 87`, `orphaned_logic: 188`
* *Architecture:* `io: 9`, `api: 361`, `import: 20`
* *Defense:* `safety: 118`, `doc: 24`, `test: 488`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections, itertools, fractions, inspect, functools, pytest, numpy, numpy._core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/multiarraymodule.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.081 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.615 IQR)
- **Top Global Matches:** file_cluster_8: 14.081, file_cluster_13: 14.12, file_cluster_11: 14.336
- **Magnitude:** 2198.18 | **LOC:** 5317 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 27.8%
- **Risk Profile:** Cognitive Load (77.5395%), Tech Debt (18.1356%)
**Top Internal Functions/Classes:**
  * `_multiarray_umath_exec` (Impact: 77.5)
    * *Intent:* *str_obj = NULL;
  * `PyArray_Where` (Impact: 71.3)
  * `einsum_list_to_subscripts` (Impact: 26.2)
  * `einsum_sub_op_from_lists` (Impact: 22.9)
  * `PyArray_AsCArray` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 261`, `args: 10`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1295`, `dead_code: 2`, `planned_debt: 4`, `orphaned_logic: 15`
* *Architecture:* `api: 495`, `import: 61`
* *Defense:* `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` conversion_utils.h, dtype.h, scalartypes.h, datetime_busdaycal.h, unique.h, dragon4.h, methods.h, nditer_pywrap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/methods.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.447 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.948 IQR)
- **Top Global Matches:** file_cluster_8: 13.447, file_cluster_13: 13.519, file_cluster_0: 13.718
- **Magnitude:** 2070.02 | **LOC:** 3063 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (88.7873%), Tech Debt (10.6038%)
**Top Internal Functions/Classes:**
  * `array_reduce_ex` (Impact: 175.4)
  * `_deepcopy_call` (Impact: 34.2)
  * `array_setflags` (Impact: 28.5)
  * `array_reduce_ex_picklebuffer` (Impact: 25.4)
  * `array_deepcopy` (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 232`, `args: 1`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 941`, `dead_code: 7`, `planned_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 473`, `import: 32`
* *Defense:* `safety: 2`, `test: 2`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` conversion_utils.h, methods.h, calculation.h, structmember.h, stdarg.h, strfuncs.h, dtypemeta.h, npy_argparse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/string_ufuncs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.84 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.177 IQR)
- **Top Global Matches:** file_cluster_8: 13.84, file_cluster_13: 14.12, file_cluster_11: 14.222
- **Magnitude:** 2008.6 | **LOC:** 2067 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (63.5841%), Tech Debt (11.8731%)
**Top Internal Functions/Classes:**
  * `init_string_ufuncs` (Impact: 113.1)
  * `_umath_strings_richcompare` (Impact: 52.4)
  * `init_ufunc` (Impact: 47.3)
  * `string_comparison_loop` (Impact: 39.2)
  * `init_mixed_type_ufunc` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 209`, `args: 70`, `func_start: 48`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1327`, `dead_code: 1`, `planned_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `import: 15`
* *Defense:* `safety: 2`, `immutability_locks: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` npy_math.h, dtypemeta.h, gil_utils.h, dispatching.h, string_buffer.h, templ_common.h, ufuncobject.h, string_fastsearch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/stringdtype/casts.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.907 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.176 IQR)
- **Top Global Matches:** file_cluster_8: 13.907, file_cluster_13: 14.042, file_cluster_11: 14.183
- **Magnitude:** 1845.76 | **LOC:** 2371 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.3392%), Tech Debt (20.7525%)
**Top Internal Functions/Classes:**
  * `string_to_fixed_width_resolve_descriptor` (Impact: 329.8)
  * `typenum_to_cstr` (Impact: 56.8)
  * `datetime_to_string` (Impact: 45.6)
  * `string_to_timedelta` (Impact: 45.4)
  * `string_to_datetime` (Impact: 37.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 151`, `args: 81`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 8`, `state_mutation: 1008`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` casts.h, ufuncobject.h, dtypemeta.h, type_traits, utf8_utils.h, dtype.h, common.h, npy_math.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/mapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.141 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.392 IQR)
- **Top Global Matches:** file_cluster_8: 14.141, file_cluster_13: 14.176, file_cluster_11: 14.255
- **Magnitude:** 1729.8 | **LOC:** 3486 | **CtrlFlow:** 87.0% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (74.465%), Tech Debt (22.4217%)
**Top Internal Functions/Classes:**
  * `array_boolean_subscript` (Impact: 149.4)
  * `PyArray_MapIterNew` (Impact: 123.0)
  * `array_assign_subscript` (Impact: 67.2)
  * `get_view_from_index` (Impact: 26.1)
  * `PyArray_MapIterArrayCopyIfOverlap` (Impact: 25.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 59`, `args: 2`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 1011`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 231`, `import: 20`
* *Defense:* `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` mapping.h, structmember.h, nditer_impl.h, common.h, npy_pycompat.h, npy_config.h, descriptor.h, npy_math.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/include/numpy/libdivide/libdivide.h` (C | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.235 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.804 IQR)
- **Top Global Matches:** file_cluster_13: 14.235, file_cluster_8: 14.302, file_cluster_7: 14.366
- **Magnitude:** 1696.84 | **LOC:** 2080 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8692%), Tech Debt (10.8687%)
**Top Internal Functions/Classes:**
  * `libdivide_128_div_128_to_64` (Impact: 263.9)
    * *Intent:* *u0 >>= shift;
  * `libdivide_count_leading_zeros32` (Impact: 9.3)
  * `libdivide_count_leading_zeros64` (Impact: 7.9)
  * `libdivide_mullhi_u64` (Impact: 5.3)
  * `libdivide_mullhi_s64` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 225`, `args: 11`, `func_start: 66`, `class_start: 23`
* *Risk/State:* `state_mutation: 863`, `dead_code: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 505`, `import: 10`
* *Defense:* `doc: 51`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cstdlib, stdlib.h, type_traits, cstdio, stdio.h, stdint.h, immintrin.h, intrin.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/iterators.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.752 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 13.752, file_cluster_13: 13.882, file_cluster_11: 14.054
- **Magnitude:** 1514.1 | **LOC:** 1784 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.1799%), Tech Debt (15.6715%)
**Top Internal Functions/Classes:**
  * `iter_ass_subscript` (Impact: 57.6)
  * `iter_subscript` (Impact: 47.6)
  * `multiiter_new_impl` (Impact: 39.8)
  * `PyArray_NeighborhoodIterNew` (Impact: 25.4)
  * `PyArray_Broadcast` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 95`, `args: 3`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 889`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 270`, `import: 17`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` conversion_utils.h, iterators.h, npy_math.h, dtypemeta.h, arrayobject.h, array_coercion.h, lowlevel_strided_loops.h, item_selection.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/testing/_private/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.717 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.854 IQR)
- **Top Global Matches:** file_cluster_13: 12.717, file_cluster_8: 13.032, file_cluster_0: 13.072
- **Magnitude:** 1504.52 | **LOC:** 2868 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (14.3091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_array_almost_equal` (Impact: 517.3)
  * `assert_array_compare` (Impact: 257.9)
  * `func_assert_same_pos` (Impact: 157.9)
  * `assert_equal` (Impact: 103.5)
  * `assert_almost_equal` (Impact: 85.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 282`, `args: 83`, `func_start: 77`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 145`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 26`, `api: 60`, `concurrency: 8`, `import: 57`
* *Defense:* `safety: 97`, `doc: 96`, `test: 20`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` shutil, pprint, json, subprocess, numpy._core, packaging.tags, unittest.case, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `numpy/random/_bounded_integers.pyi` (PYTHON) | **Drift Ratio: 1.52x**
  * **Global Archetype:** `file_cluster_16` (Drift: 5.417 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 8.222 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `numpy/tests/test_configtool.py` (PYTHON) | Magnitude: 19.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 20, test: 16, import: 9
- `numpy/_core/src/multiarray/nditer_api.c` (C) | Magnitude: 1227.42 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 652, indent_spaces: 580, api: 178, pointers: 135
- `numpy/_core/tests/test_casting_unittests.py` (PYTHON) | Magnitude: 86.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 626, structural_boundaries: 206, test: 180, branch: 131
- `numpy/random/tests/test_extending.py` (PYTHON) | Magnitude: 28.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 41, branch: 19, import: 19
- `numpy/_core/numerictypes.py` (PYTHON) | Magnitude: 115.9 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 55, branch: 34, safety: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `numpy/_core/src/npymath/ieee754.cpp` (CPP) | Magnitude: 411.96 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 276, state_mutation: 261, branch: 88, structural_boundaries: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `numpy/_core/src/umath/fast_loop_macros.h` (C) | Magnitude: 358.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 299, indent_spaces: 192, branch: 91, api: 51
- `tools/rebase_installed_dlls_cygwin.sh` (SHELL) | Magnitude: 0.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, state_mutation: 2, args: 1, orphaned_logic: 1
- `numpy/_core/src/multiarray/nditer_impl.h` (C) | Magnitude: 69.44 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 106, macros: 88, reflection_metaprogramming: 62, pointers: 44
- `numpy/_core/src/common/npdef.hpp` (CPP) | Magnitude: 18.32 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 15, branch: 6, doc: 5, reflection_metaprogramming: 5
- `tools/list_numpy_dlls.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, io: 5, reflection_metaprogramming: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `numpy/_pyinstaller/tests/test_pyinstaller.py` (PYTHON) | Magnitude: 7.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, test: 8, structural_boundaries: 6, explicit_casts: 5
- `numpy/f2py/tests/test_callback.py` (PYTHON) | Magnitude: 112.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 81, test: 46, safety: 35
- `numpy/_core/src/npysort/binsearch.cpp` (CPP) | Magnitude: 486.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 321, indent_spaces: 228, structural_boundaries: 81, immutability_locks: 49
- `numpy/_core/src/common/npy_cpu_dispatch.c` (C) | Magnitude: 81.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 39, structural_boundaries: 14, branch: 13
- `tools/swig/test/ArrayZ.h` (CPP) | Magnitude: 0.03 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 10, immutability_locks: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `numpy/_typing/_ufunc.pyi` (PYTHON) | Magnitude: 217.22 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 853, encapsulation: 209, structural_boundaries: 196, generics: 186
- `numpy/ma/testutils.pyi` (PYTHON) | Magnitude: 21.04 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, generics: 15, api: 14
- `numpy/ma/core.pyi` (PYTHON) | Magnitude: 951.98 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3032, encapsulation: 2209, structural_boundaries: 876, generics: 874
- `numpy/testing/_private/utils.pyi` (PYTHON) | Magnitude: 113.72 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 261, structural_boundaries: 109, generics: 92, encapsulation: 92
- `numpy/_core/src/common/meta.hpp` (CPP) | Magnitude: 21.78 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 14, class_start: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `numpy/f2py/tests/src/return_logical/foo77.f` (FORTRAN) | Magnitude: 28.9 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, args: 24, safety: 24, structural_boundaries: 23
- `doc/source/f2py/code/common.f` (FORTRAN) | Magnitude: 6.4 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, debug_prints: 6, state_mutation: 3, comprehensions: 3
- `doc/source/f2py/code/moddata.f90` (FORTRAN) | Magnitude: 6.84 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, debug_prints: 7, state_mutation: 3
- `doc/source/f2py/code/allocarr.f90` (FORTRAN) | Magnitude: 14.9 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, structural_boundaries: 5, debug_prints: 4
- `numpy/f2py/tests/src/parameter/constant_array.f90` (FORTRAN) | Magnitude: 29.12 | Delta: **0.635 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 28, safety: 22, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `numpy/_core/tests/test_multithreading.py` (PYTHON) | Magnitude: 307.64 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 247, structural_boundaries: 86, branch: 54, test: 44
- `numpy/_core/tests/test_hashtable.py` (PYTHON) | Magnitude: 144.02 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 41, branch: 38, test: 31
- `numpy/_core/src/common/npy_import.c` (C) | Magnitude: 102.04 | Delta: **0.266 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 33, branch: 16, concurrency: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `numpy/f2py/cfuncs.py` (PYTHON) | Magnitude: 25.74 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 140, indent_spaces: 129, branch: 49, dead_code: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `numpy/exceptions.py` (PYTHON) | Magnitude: 45.18 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 18, structural_boundaries: 17, doc: 16
- `doc/source/dev/examples/doxy_func.h` (C) | Magnitude: 11.52 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, args: 1, api: 1, pointers: 1
- `numpy/_core/tests/test_casting_floatingpoint_errors.py` (PYTHON) | Magnitude: 81.16 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, lazy_evaluation: 28, structural_boundaries: 23, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `numpy/f2py/tests/test_pyf_src.py` (PYTHON) | Magnitude: 6.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 7, indent_spaces: 5, args: 2
- `numpy/_core/src/_simd/checks/cpu_lsx.c` (C) | Magnitude: 5.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 3, structural_boundaries: 2, macros: 2, indent_spaces: 2
- `numpy/_core/src/multiarray/convert_datatype.c` (C) | Magnitude: 3076.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1735, state_mutation: 1200, pointers: 546, branch: 511
- `numpy/_core/src/common/binop_override.h` (C) | Magnitude: 37.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, branch: 21, api: 8, structural_boundaries: 7
- `numpy/f2py/tests/test_routines.py` (PYTHON) | Magnitude: 8.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, test: 9, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `numpy/f2py/tests/src/callback/gh18335.f90` (FORTRAN) | Magnitude: 8.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, state_mutation: 3, args: 2
- `tools/swig/test/Flat.h` (CPP) | Magnitude: 0.02 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 14, macros: 3, dead_code: 2, reflection_metaprogramming: 2
- `tools/swig/test/Vector.h` (CPP) | Magnitude: 0.02 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: args: 22, dead_code: 7, structural_boundaries: 6, macros: 3
- `tools/swig/test/Matrix.h` (CPP) | Magnitude: 0.02 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: args: 20, dead_code: 5, structural_boundaries: 4, macros: 3
- `tools/swig/test/SuperTensor.h` (CPP) | Magnitude: 0.02 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: args: 20, dead_code: 5, structural_boundaries: 4, macros: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `numpy/__init__.pyi` -> Churn: **100.0%** | Cog Load: 9.6147% | Debt: 74.4484%
- `numpy/ma/core.pyi` -> Churn: **71.19%** | Cog Load: 5.6887% | Debt: 99.9996%
- `numpy/_core/src/multiarray/multiarraymodule.c` -> Churn: **65.5%** | Cog Load: 77.5395% | Debt: 18.1356%
- `numpy/_core/src/umath/ufunc_object.c` -> Churn: **65.5%** | Cog Load: 92.9427% | Debt: 16.2574%
- `numpy/ma/core.py` -> Churn: **63.49%** | Cog Load: 27.3056% | Debt: 68.441%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `numpy/linalg/umath_linalg.cpp` -> **Evgeni Burovski** (100.0% isolated ownership) | Magnitude: 3701.68
- `numpy/_core/src/npysort/timsort.cpp` -> **Moritz Groß** (100.0% isolated ownership) | Magnitude: 2265.92
- `numpy/_core/src/multiarray/dtype_transfer.c` -> **Matti Picus** (100.0% isolated ownership) | Magnitude: 2255.12
- `numpy/_core/src/multiarray/stringdtype/casts.cpp` -> **Warren Weckesser** (100.0% isolated ownership) | Magnitude: 1845.76
- `numpy/_core/src/umath/string_buffer.h` -> **Sayed Awad** (100.0% isolated ownership) | Magnitude: 1294.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `numpy/_core/src/multiarray/datetime.c` -> **Severity: 0.015** (Bridge: 0.0001 * Flux: 100.0%)
- `numpy/_core/src/common/lowlevel_strided_loops.h` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)
- `numpy/_core/src/common/npy_config.h` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 36.1141%)
- `numpy/_core/src/multiarray/dtypemeta.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 18.0203%)
- `numpy/_core/include/numpy/numpyconfig.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.5598%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `numpy/_core/src/common/npy_cpu_features.h` -> **Severity: 3.543** (Embedded: 0.0372 * Error Risk: 95.1954%)
- `numpy/_core/src/common/npy_config.h` -> **Severity: 2.874** (Embedded: 0.0457 * Error Risk: 62.8789%)
- `numpy/_core/src/common/npy_cpu_dispatch.h` -> **Severity: 2.703** (Embedded: 0.0417 * Error Risk: 64.7615%)
- `numpy/_core/src/multiarray/dtypemeta.h` -> **Severity: 2.238** (Embedded: 0.0381 * Error Risk: 58.7752%)
- `numpy/_core/src/common/lowlevel_strided_loops.h` -> **Severity: 2.189** (Embedded: 0.0234 * Error Risk: 93.5067%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `numpy/_core/src/multiarray/array_method.h` -> **Severity: 1234.1** (Blast Radius: 12.341 * Doc Risk: 100.0%)
- `numpy/core/_utils.py` -> **Severity: 747.227** (Blast Radius: 14.571 * Doc Risk: 51.2818%)
- `numpy/_core/src/multiarray/dtypemeta.h` -> **Severity: 569.6** (Blast Radius: 5.696 * Doc Risk: 100.0%)
- `numpy/_core/src/common/npy_import.h` -> **Severity: 358.8** (Blast Radius: 3.588 * Doc Risk: 100.0%)
- `numpy/_core/src/multiarray/npy_static_data.h` -> **Severity: 352.1** (Blast Radius: 3.521 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
