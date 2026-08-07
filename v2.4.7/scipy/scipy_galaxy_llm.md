# ARCHITECTURAL_BRIEF: scipy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/scipy` |
| **Timestamp** | `2026-08-07T04:02:23.417608+00:00` |
| **Scan Duration** | `14.04s` |
| **Git Branch** | `main` |
| **Git Commit** | `355b747ccae64368a7dce38825361eca6055fcd1` |
| **Git Remote** | `https://github.com/scipy/scipy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1650 malicious artifacts.

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
| Total Artifacts | 3031 |
| Analyzed Artifacts (Scanned) | 1852 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1179 |
| Total LOC | 429737 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 61.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8091 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2015 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.3039 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 161 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1124 | 303515 | 60.7% |
| C | 393 | 94443 | 21.2% |
| PLAINTEXT | 148 | 0 | 8.0% |
| CPP | 109 | 24148 | 5.9% |
| MARKDOWN | 39 | 0 | 2.1% |
| SHELL | 9 | 216 | 0.5% |
| XML | 7 | 0 | 0.4% |
| JSON | 5 | 391 | 0.3% |
| FORTRAN | 5 | 6656 | 0.3% |
| MATLAB | 4 | 76 | 0.2% |
| MAKEFILE | 3 | 104 | 0.2% |
| CSS | 1 | 76 | 0.1% |
| HTML | 1 | 11 | 0.1% |
| YAML | 1 | 51 | 0.1% |
| M4 | 1 | 1 | 0.1% |
| OBJECTIVE-C | 1 | 18 | 0.1% |
| BATCH | 1 | 31 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.529`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1178 | 63.6% |
| file_cluster_13 | 349 | 18.8% |
| file_cluster_0 | 65 | 3.5% |
| file_cluster_9 | 27 | 1.5% |
| file_cluster_16 | 16 | 0.9% |
| file_cluster_17 | 12 | 0.6% |
| file_cluster_7 | 7 | 0.4% |
| file_cluster_11 | 7 | 0.4% |
| file_cluster_4 | 2 | 0.1% |
| file_cluster_6 | 1 | 0.1% |
| file_cluster_12 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 187 | 10.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1179*

**Composition by Extension & Reason:**
- `.rst`: 326x Excluded (Unsupported Extension: '.rst'), 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 140x Excluded (Unsupported Extension: '.npz'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mat`: 113x Excluded (Unsupported Extension: '.mat')
- `.build`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 118 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2273 LOC)
- `.txt`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 6631 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2305 LOC)
- `.sav`: 48x Excluded (Unsupported Extension: '.sav')
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 26x Excluded (Unsupported Extension: '.dat')
- `.wav`: 22x Excluded (Explicitly Denied Extension: '.wav')
- `.h`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 13276 commas in 4421 LOC), 1x Excluded (Machine-Generated Source Code Signature: 368 LOC)
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.arff`: 16x Excluded (Unsupported Extension: '.arff')
- `.src`: 14x Excluded (Unsupported Extension: '.src'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 24.6 | 9.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 44.1 | 48.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.3 | 5.2 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 37.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 74.1 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.8 | 1.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.9 | 16.4 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scipy/odr/odrpack/d_odr.f` (Hits: 372)
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/util.c` (Hits: 25)
- `tools/write_release_and_log.py` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **scipy.css** (`doc/source/_static/scipy.css`) — 183 inbound connections
2. **sparse.py** (`benchmarks/benchmarks/sparse.py`) — 146 inbound connections
3. **special.py** (`benchmarks/benchmarks/special.py`) — 105 inbound connections
4. **slu_ddefs.h** (`scipy/sparse/linalg/_dsolve/SuperLU/SRC/slu_ddefs.h`) — 50 inbound connections
5. **signal.py** (`benchmarks/benchmarks/signal.py`) — 42 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **xsf_wrappers.cpp** (`scipy/special/xsf_wrappers.cpp`) — 49 outbound dependencies
2. **releasing.rst.inc** (`doc/source/dev/core-dev/releasing.rst.inc`) — 45 outbound dependencies
3. **_special_ufuncs.cpp** (`scipy/special/_special_ufuncs.cpp`) — 36 outbound dependencies
4. **__init__.py** (`scipy/stats/__init__.py`) — 30 outbound dependencies
5. **_signaltools.py** (`scipy/signal/_signaltools.py`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_input_validation_edge_cases` (@ `scipy/stats/tests/test_stats.py`) -> Impact: **1754.1** | LOC: 8165
- `_kendalltau` (@ `scipy/stats/_stats_py.py`) -> Impact: **1318.8** | LOC: 2247
  * *Intent:* # no range given, so use values in `a`
- `test_funcs` (@ `scipy/stats/tests/test_continuous.py`) -> Impact: **994.1** | LOC: 2007
- `fpgrsp` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **733.9** | LOC: 436
  * *Intent:* // subroutine fpcyt2 solves a linear n x n system // a * c = b // where matrix a is a cyclic tridiagonal matrix, decomposed
- `nonlin_solve` (@ `scipy/optimize/_nonlin.py`) -> Impact: **675.8** | LOC: 1036
- `test_correlate_complex_kernel_cval` (@ `scipy/ndimage/tests/test_filters.py`) -> Impact: **656.7** | LOC: 2668
- `preproc` (@ `subprojects/pyprima/pyprima/pyprima/src/pyprima/common/preproc.py`) -> Impact: **644.8** | LOC: 257
- `plot` (@ `scipy/stats/_distribution_infrastructure.py`) -> Impact: **633.6** | LOC: 1719
- `_check` (@ `scipy/sparse/_coo.py`) -> Impact: **629.6** | LOC: 1265
- `fppara` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **590.8** | LOC: 533
  * *Intent:* // test whether there are non-zero values in the new row of (avv) // corresponding to the b-splines n(j;v),j=nv7+1,...,nv4.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scipy/sparse/linalg/_dsolve/SuperLU/SRC` | 193 | 57914.06 | 62.07% | 27.55% |
| `scipy/stats` | 68 | 23320.88 | 13.85% | 37.91% |
| `scipy/interpolate/src` | 6 | 21519.36 | 45.03% | 10.35% |
| `scipy/linalg` | 47 | 19268.72 | 11.6% | 26.64% |
| `scipy/stats/tests` | 41 | 18020.32 | 5.5% | 0.0% |
| `scipy/linalg/src` | 14 | 15216.56 | 68.65% | 17.61% |
| `scipy/optimize` | 69 | 14689.98 | 21.37% | 45.02% |
| `subprojects/qhull_r/libqhull_r` | 30 | 12889.34 | 49.39% | 17.14% |
| `scipy/integrate` | 20 | 12824.75 | 27.18% | 50.18% |
| `scipy/integrate/src` | 10 | 12720.42 | 21.17% | 3.91% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/benchmarks/array_api.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cluster_hierarchy_disjoint_set.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/fft_basic.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_A.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_A.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_I.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_K.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_L.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_funcs_M.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scipy/stats/_continuous_distns.py` -> **0** Orphaned Functions | **1074** Duplicates
- `scipy/stats/tests/test_distributions.py` -> **190** Orphaned Functions | **232** Duplicates
- `scipy/stats/tests/test_multivariate.py` -> **172** Orphaned Functions | **88** Duplicates
- `scipy/stats/tests/test_morestats.py` -> **168** Orphaned Functions | **91** Duplicates
- `scipy/special/xsf_wrappers.cpp` -> **259** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scipy/integrate/_odepackmodule.c`** -> AI Confidence: **99.48%**
2. **`scipy/ndimage/src/nd_image.c`** -> AI Confidence: **99.48%**
3. **`scipy/ndimage/src/ni_fourier.c`** -> AI Confidence: **99.48%**
4. **`scipy/sparse/linalg/_propack/PROPACK/src/lansvd.c`** -> AI Confidence: **99.48%**
5. **`scipy/sparse/linalg/_propack/PROPACK/src/lansvd_irl.c`** -> AI Confidence: **99.48%**
6. **`subprojects/qhull_r/libqhull_r/rboxlib_r.c`** -> AI Confidence: **99.48%**
7. **`scipy/linalg/src/_batched_linalg_module.cc`** -> AI Confidence: **99.48%**
8. **`scipy/sparse/sparsetools/sparsetools.cxx`** -> AI Confidence: **99.48%**
9. **`scipy/spatial/ckdtree/src/query_ball_point.cxx`** -> AI Confidence: **99.48%**
10. **`scipy/spatial/ckdtree/src/query_pairs.cxx`** -> AI Confidence: **99.48%**
11. **`scipy/spatial/ckdtree/src/sparse_distances.cxx`** -> AI Confidence: **99.48%**
12. **`scipy/special/wright.cc`** -> AI Confidence: **99.48%**
13. **`scipy/integrate/_tanhsinh.py`** -> AI Confidence: **99.39%**
14. **`scipy/interpolate/_fitpack_repro.py`** -> AI Confidence: **99.39%**
15. **`scipy/io/wavfile.py`** -> AI Confidence: **99.39%**
16. **`scipy/linalg/_decomp.py`** -> AI Confidence: **99.39%**
17. **`scipy/linalg/_decomp_qr.py`** -> AI Confidence: **99.39%**
18. **`scipy/optimize/_lsq/trf.py`** -> AI Confidence: **99.39%**
19. **`scipy/signal/_fir_filter_design.py`** -> AI Confidence: **99.39%**
20. **`scipy/signal/_spectral_py.py`** -> AI Confidence: **99.39%**
21. **`scipy/sparse/linalg/_isolve/lsmr.py`** -> AI Confidence: **99.39%**
22. **`scipy/sparse/linalg/_isolve/minres.py`** -> AI Confidence: **99.39%**
23. **`scipy/special/tests/test_support_alternative_backends.py`** -> AI Confidence: **99.39%**
24. **`scipy/stats/_binned_statistic.py`** -> AI Confidence: **99.39%**
25. **`scipy/stats/_quantile.py`** -> AI Confidence: **99.39%**
26. **`scipy/stats/tests/test_quantile.py`** -> AI Confidence: **99.39%**
27. **`scipy/integrate/_dzvodemodule.c`** -> AI Confidence: **99.39%**
28. **`scipy/io/_fast_matrix_market/fast_matrix_market/dependencies/ryu/ryu/d2fixed.c`** -> AI Confidence: **99.39%**
29. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/colamd.c`** -> AI Confidence: **99.39%**
30. **`scipy/linalg/src/_linalg_solve.hh`** -> AI Confidence: **99.39%**
31. **`scipy/spatial/ckdtree/src/query_ball_tree.cxx`** -> AI Confidence: **99.39%**
32. **`scipy/linalg/_basic.py`** -> AI Confidence: **99.35%**
33. **`scipy/ndimage/_filters.py`** -> AI Confidence: **99.35%**
34. **`scipy/ndimage/_interpolation.py`** -> AI Confidence: **99.35%**
35. **`scipy/signal/_signaltools.py`** -> AI Confidence: **99.35%**
36. **`scipy/ndimage/_morphology.py`** -> AI Confidence: **99.34%**
37. **`scipy/sparse/csgraph/_matching.pyx`** -> AI Confidence: **99.34%**
38. **`scipy/sparse/linalg/_isolve/_gcrotmk.py`** -> AI Confidence: **99.34%**
39. **`subprojects/pyprima/pyprima/pyprima/src/pyprima/cobyla/cobyla.py`** -> AI Confidence: **99.34%**
40. **`scipy/ndimage/src/ni_interpolation.c`** -> AI Confidence: **99.34%**
41. **`scipy/ndimage/src/ni_measure.c`** -> AI Confidence: **99.34%**
42. **`scipy/ndimage/src/ni_morphology.c`** -> AI Confidence: **99.34%**
43. **`scipy/optimize/tnc/tnc.c`** -> AI Confidence: **99.34%**
44. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dmach.c`** -> AI Confidence: **99.34%**
45. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/smach.c`** -> AI Confidence: **99.34%**
46. **`subprojects/qhull_r/libqhull_r/random_r.c`** -> AI Confidence: **99.34%**
47. **`subprojects/qhull_r/libqhull_r/userprintf_r.c`** -> AI Confidence: **99.34%**
48. **`scipy/linalg/src/_linalg_inv.hh`** -> AI Confidence: **99.34%**
49. **`scipy/signal/_sigtoolsmodule.cc`** -> AI Confidence: **99.34%**
50. **`scipy/special/sf_error.cc`** -> AI Confidence: **99.34%**
51. **`scipy/special/stirling2.h`** -> AI Confidence: **99.34%**
52. **`tools/pre-commit-hook.py`** -> AI Confidence: **99.32%**
53. **`scipy/fftpack/tests/fftw_dct.c`** -> AI Confidence: **99.32%**
54. **`scipy/integrate/src/lsoda.c`** -> AI Confidence: **99.32%**
55. **`scipy/interpolate/src/_fitpackmodule.c`** -> AI Confidence: **99.32%**
56. **`scipy/ndimage/src/ni_filters.c`** -> AI Confidence: **99.32%**
57. **`scipy/optimize/src/minpack.c`** -> AI Confidence: **99.32%**
58. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ccolumn_bmod.c`** -> AI Confidence: **99.32%**
59. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/clacon2.c`** -> AI Confidence: **99.32%**
60. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/cpanel_bmod.c`** -> AI Confidence: **99.32%**
61. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/cpivotL.c`** -> AI Confidence: **99.32%**
62. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/creadMM.c`** -> AI Confidence: **99.32%**
63. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/creadhb.c`** -> AI Confidence: **99.32%**
64. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/creadrb.c`** -> AI Confidence: **99.32%**
65. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dcolumn_bmod.c`** -> AI Confidence: **99.32%**
66. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dpanel_bmod.c`** -> AI Confidence: **99.32%**
67. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dpivotL.c`** -> AI Confidence: **99.32%**
68. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dreadMM.c`** -> AI Confidence: **99.32%**
69. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dreadhb.c`** -> AI Confidence: **99.32%**
70. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/dreadrb.c`** -> AI Confidence: **99.32%**
71. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_cdrop_row.c`** -> AI Confidence: **99.32%**
72. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_cpivotL.c`** -> AI Confidence: **99.32%**
73. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_ddrop_row.c`** -> AI Confidence: **99.32%**
74. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_dpivotL.c`** -> AI Confidence: **99.32%**
75. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_sdrop_row.c`** -> AI Confidence: **99.32%**
76. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_spivotL.c`** -> AI Confidence: **99.32%**
77. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_zdrop_row.c`** -> AI Confidence: **99.32%**
78. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_zpivotL.c`** -> AI Confidence: **99.32%**
79. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/scolumn_bmod.c`** -> AI Confidence: **99.32%**
80. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/sp_coletree.c`** -> AI Confidence: **99.32%**
81. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/spanel_bmod.c`** -> AI Confidence: **99.32%**
82. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/spivotL.c`** -> AI Confidence: **99.32%**
83. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/sreadMM.c`** -> AI Confidence: **99.32%**
84. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/sreadhb.c`** -> AI Confidence: **99.32%**
85. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/sreadrb.c`** -> AI Confidence: **99.32%**
86. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zcolumn_bmod.c`** -> AI Confidence: **99.32%**
87. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zlacon2.c`** -> AI Confidence: **99.32%**
88. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zpanel_bmod.c`** -> AI Confidence: **99.32%**
89. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zpivotL.c`** -> AI Confidence: **99.32%**
90. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zreadMM.c`** -> AI Confidence: **99.32%**
91. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zreadhb.c`** -> AI Confidence: **99.32%**
92. **`scipy/sparse/linalg/_dsolve/SuperLU/SRC/zreadrb.c`** -> AI Confidence: **99.32%**
93. **`scipy/sparse/linalg/_propack/PROPACK/src/lanbpro.c`** -> AI Confidence: **99.32%**
94. **`scipy/stats/biasedurn/wnchyppr.cpp`** -> AI Confidence: **99.32%**
95. **`scipy/_build_utils/tempita/_tempita.py`** -> AI Confidence: **99.31%**
96. **`scipy/cluster/hierarchy/_hierarchy_impl.py`** -> AI Confidence: **99.31%**
97. **`scipy/cluster/vq/_vq_impl.py`** -> AI Confidence: **99.31%**
98. **`scipy/differentiate/_differentiate.py`** -> AI Confidence: **99.31%**
99. **`scipy/fft/_pocketfft/helper.py`** -> AI Confidence: **99.31%**
100. **`scipy/integrate/_bvp.py`** -> AI Confidence: **99.31%**
101. **`scipy/integrate/_ivp/bdf.py`** -> AI Confidence: **99.31%**
102. **`scipy/integrate/_ivp/ivp.py`** -> AI Confidence: **99.31%**
103. **`scipy/integrate/_ivp/radau.py`** -> AI Confidence: **99.31%**
104. **`scipy/integrate/_ode.py`** -> AI Confidence: **99.31%**
105. **`scipy/integrate/_quad_vec.py`** -> AI Confidence: **99.31%**
106. **`scipy/integrate/_quadpack_py.py`** -> AI Confidence: **99.31%**
107. **`scipy/integrate/_quadrature.py`** -> AI Confidence: **99.31%**
108. **`scipy/integrate/tests/test_quadrature.py`** -> AI Confidence: **99.31%**
109. **`scipy/interpolate/_bary_rational.py`** -> AI Confidence: **99.31%**
110. **`scipy/interpolate/_bsplines.py`** -> AI Confidence: **99.31%**
111. **`scipy/interpolate/_cubic.py`** -> AI Confidence: **99.31%**
112. **`scipy/interpolate/_fitpack2.py`** -> AI Confidence: **99.31%**
113. **`scipy/interpolate/_interpolate.py`** -> AI Confidence: **99.31%**
114. **`scipy/interpolate/_ndbspline.py`** -> AI Confidence: **99.31%**
115. **`scipy/interpolate/_polyint.py`** -> AI Confidence: **99.31%**
116. **`scipy/interpolate/_rbfinterp.py`** -> AI Confidence: **99.31%**
117. **`scipy/interpolate/_rgi.py`** -> AI Confidence: **99.31%**
118. **`scipy/io/_harwell_boeing/hb.py`** -> AI Confidence: **99.31%**
119. **`scipy/io/_idl.py`** -> AI Confidence: **99.31%**
120. **`scipy/io/_mmio.py`** -> AI Confidence: **99.31%**
121. **`scipy/io/_netcdf.py`** -> AI Confidence: **99.31%**
122. **`scipy/io/arff/_arffread.py`** -> AI Confidence: **99.31%**
123. **`scipy/io/matlab/_mio.py`** -> AI Confidence: **99.31%**
124. **`scipy/io/matlab/_mio4.py`** -> AI Confidence: **99.31%**
125. **`scipy/io/matlab/_mio5.py`** -> AI Confidence: **99.31%**
126. **`scipy/linalg/_decomp_ldl.py`** -> AI Confidence: **99.31%**
127. **`scipy/linalg/_decomp_lu.py`** -> AI Confidence: **99.31%**
128. **`scipy/linalg/_decomp_schur.py`** -> AI Confidence: **99.31%**
129. **`scipy/linalg/_decomp_svd.py`** -> AI Confidence: **99.31%**
130. **`scipy/linalg/_matfuncs.py`** -> AI Confidence: **99.31%**
131. **`scipy/linalg/_matfuncs_inv_ssq.py`** -> AI Confidence: **99.31%**
132. **`scipy/linalg/_solvers.py`** -> AI Confidence: **99.31%**
133. **`scipy/linalg/_special_matrices.py`** -> AI Confidence: **99.31%**
134. **`scipy/linalg/blas.py`** -> AI Confidence: **99.31%**
135. **`scipy/linalg/lapack.py`** -> AI Confidence: **99.31%**
136. **`scipy/linalg/tests/test_decomp_cossin.py`** -> AI Confidence: **99.31%**
137. **`scipy/linalg/tests/test_lapack.py`** -> AI Confidence: **99.31%**
138. **`scipy/optimize/_chandrupatla.py`** -> AI Confidence: **99.31%**
139. **`scipy/optimize/_cobyla_py.py`** -> AI Confidence: **99.31%**
140. **`scipy/optimize/_constraints.py`** -> AI Confidence: **99.31%**
141. **`scipy/optimize/_differentiable_functions.py`** -> AI Confidence: **99.31%**
142. **`scipy/optimize/_differentialevolution.py`** -> AI Confidence: **99.31%**
143. **`scipy/optimize/_lbfgsb_py.py`** -> AI Confidence: **99.31%**
144. **`scipy/optimize/_linprog.py`** -> AI Confidence: **99.31%**
145. **`scipy/optimize/_linprog_highs.py`** -> AI Confidence: **99.31%**
146. **`scipy/optimize/_linprog_ip.py`** -> AI Confidence: **99.31%**
147. **`scipy/optimize/_lsq/least_squares.py`** -> AI Confidence: **99.31%**
148. **`scipy/optimize/_lsq/lsq_linear.py`** -> AI Confidence: **99.31%**
149. **`scipy/optimize/_lsq/trf_linear.py`** -> AI Confidence: **99.31%**
150. **`scipy/optimize/_milp.py`** -> AI Confidence: **99.31%**
151. **`scipy/optimize/_minimize.py`** -> AI Confidence: **99.31%**
152. **`scipy/optimize/_minpack_py.py`** -> AI Confidence: **99.31%**
153. **`scipy/optimize/_numdiff.py`** -> AI Confidence: **99.31%**
154. **`scipy/optimize/_optimize.py`** -> AI Confidence: **99.31%**
155. **`scipy/optimize/_shgo.py`** -> AI Confidence: **99.31%**
156. **`scipy/optimize/_slsqp_py.py`** -> AI Confidence: **99.31%**
157. **`scipy/optimize/_trustregion.py`** -> AI Confidence: **99.31%**
158. **`scipy/optimize/_trustregion_constr/minimize_trustregion_constr.py`** -> AI Confidence: **99.31%**
159. **`scipy/optimize/_zeros_py.py`** -> AI Confidence: **99.31%**
160. **`scipy/optimize/tests/test_hessian_update_strategy.py`** -> AI Confidence: **99.31%**
161. **`scipy/signal/_filter_design.py`** -> AI Confidence: **99.31%**
162. **`scipy/signal/_lti_conversion.py`** -> AI Confidence: **99.31%**
163. **`scipy/signal/_ltisys.py`** -> AI Confidence: **99.31%**
164. **`scipy/signal/_peak_finding.py`** -> AI Confidence: **99.31%**
165. **`scipy/signal/_polyutils.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6656` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benchmarks/benchmarks/fft_basic.py` (PYTHON) -> Cumulative Risk: **739.14**
- **Archetype:** `file_cluster_13` (Distance: 12.682 IQR)
- **Magnitude:** 341.4 | **LOC:** 355 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Documentation (97.6027%)
- **Heaviest Functions:** `setup` (Impact: 19.1), `setup` (Impact: 19.0), `setup` (Impact: 9.7)

### 2. `benchmarks/benchmarks/integrate.py` (PYTHON) -> Cumulative Risk: **735.78**
- **Archetype:** `file_cluster_8` (Distance: 11.012 IQR)
- **Magnitude:** 252.7 | **LOC:** 405 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.5163%)
- **Heaviest Functions:** `setup` (Impact: 30.4), `setup` (Impact: 8.5), `setup` (Impact: 6.3)

### 3. `scipy/sparse/linalg/_propack/PROPACK/src/gs.c` (C) -> Cumulative Risk: **678.49**
- **Archetype:** `file_cluster_8` (Distance: 14.331 IQR)
- **Magnitude:** 472.02 | **LOC:** 363 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8104%)
- **Heaviest Functions:** `smgs` (Impact: 10.4), `cmgs` (Impact: 10.3), `zmgs` (Impact: 10.3)

### 4. `scipy/sparse/linalg/_dsolve/SuperLU/SRC/qselect.c` (C) -> Cumulative Risk: **669.52**
- **Archetype:** `file_cluster_13` (Distance: 13.857 IQR)
- **Magnitude:** 174.14 | **LOC:** 85 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8546%)
- **Heaviest Functions:** `dqselect` (Impact: 27.5), `sqselect` (Impact: 27.5)

### 5. `scipy/sparse/linalg/_propack/PROPACK/src/ritzvec.c` (C) -> Cumulative Risk: **666.64**
- **Archetype:** `file_cluster_8` (Distance: 13.118 IQR)
- **Magnitude:** 200.78 | **LOC:** 179 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.3118%)
- **Heaviest Functions:** `critzvec` (Impact: 28.4), `zritzvec` (Impact: 23.9), `sritzvec` (Impact: 22.7)

### 6. `benchmarks/benchmarks/optimize_zeros.py` (PYTHON) -> Cumulative Risk: **659.0**
- **Archetype:** `file_cluster_13` (Distance: 12.222 IQR)
- **Magnitude:** 117.62 | **LOC:** 117 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9871%), Cognitive Load (91.5808%)
- **Heaviest Functions:** `setup` (Impact: 25.5), `setup` (Impact: 14.8), `time_array_newton` (Impact: 3.2)

### 7. `scipy/sparse/linalg/_propack/PROPACK/src/getu0.c` (C) -> Cumulative Risk: **657.77**
- **Archetype:** `file_cluster_8` (Distance: 14.518 IQR)
- **Magnitude:** 397.66 | **LOC:** 216 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9141%)
- **Heaviest Functions:** `cgetu0` (Impact: 32.3), `zgetu0` (Impact: 32.3), `sgetu0` (Impact: 32.2)

### 8. `scipy/sparse/linalg/_dsolve/SuperLU/SRC/dutil.c` (C) -> Cumulative Risk: **649.53**
- **Archetype:** `file_cluster_8` (Distance: 15.067 IQR)
- **Magnitude:** 717.74 | **LOC:** 480 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.912%)
- **Heaviest Functions:** `dPrint_SuperNode_Matrix` (Impact: 21.5), `dCompRow_to_CompCol` (Impact: 20.8), `dinf_norm_error` (Impact: 15.1)

### 9. `scipy/sparse/linalg/_dsolve/SuperLU/SRC/sutil.c` (C) -> Cumulative Risk: **649.53**
- **Archetype:** `file_cluster_8` (Distance: 15.067 IQR)
- **Magnitude:** 717.74 | **LOC:** 480 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.912%)
- **Heaviest Functions:** `sPrint_SuperNode_Matrix` (Impact: 21.5), `sCompRow_to_CompCol` (Impact: 20.8), `sinf_norm_error` (Impact: 15.1)

### 10. `scipy/sparse/linalg/_dsolve/SuperLU/SRC/cutil.c` (C) -> Cumulative Risk: **649.36**
- **Archetype:** `file_cluster_8` (Distance: 15.017 IQR)
- **Magnitude:** 721.72 | **LOC:** 484 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9085%)
- **Heaviest Functions:** `cPrint_SuperNode_Matrix` (Impact: 21.6), `cCompRow_to_CompCol` (Impact: 20.8), `cinf_norm_error` (Impact: 15.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scipy/interpolate/src/dfitpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.991 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_11: 16.991, file_cluster_0: 17.1, file_cluster_13: 17.103
- **Magnitude:** 15275.86 | **LOC:** 9383 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 93.1%
- **Risk Profile:** Cognitive Load (38.9225%), Tech Debt (11.7036%)
**Top Internal Functions/Classes:**
  * `fpgrsp` (Impact: 733.9)
    * *Intent:* // subroutine fpcyt2 solves a linear n x n system // a * c = b // where matrix a is a cyclic tridiag...
  * `fppara` (Impact: 590.8)
    * *Intent:* // test whether there are non-zero values in the new row of (avv) // corresponding to the b-splines ...
  * `fpclos` (Impact: 538.8)
  * `fpcurf` (Impact: 508.6)
  * `fpgrre` (Impact: 465.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1282`, `structural_boundaries: 333`, `args: 75`, `func_start: 44`
* *Risk/State:* `state_mutation: 8205`, `dead_code: 53`, `orphaned_logic: 20`
* *Architecture:* `api: 461`, `import: 1`
* *Defense:* `doc: 289`, `immutability_locks: 638`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dfitpack.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/linalg/_decomp_update.pyx.in` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.29 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.195 IQR)
- **Top Global Matches:** file_cluster_8: 9.29, file_cluster_7: 9.98, file_cluster_1: 10.219
- **Magnitude:** 13869.44 | **LOC:** 2351 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.3254%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 103`, `args: 8`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `dead_code: 9`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 8`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` scipy._lib._util, numpy.linalg, scipy, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/odr/odrpack/d_odr.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.933 IQR)
- **Top Global Matches:** file_cluster_8: 13.933, file_cluster_11: 14.199, file_cluster_13: 14.307
- **Magnitude:** 7997.3 | **LOC:** 10986 | **CtrlFlow:** 80.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.245%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DODMN` (Impact: 393.7)
  * `DODPC1` (Impact: 329.9)
  * `DODCHK` (Impact: 225.6)
  * `DODPC3` (Impact: 222.3)
  * `DODPE1` (Impact: 194.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1931`, `structural_boundaries: 461`, `args: 98`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 39`, `state_mutation: 4015`
* *Architecture:* `io: 372`, `api: 50`
* *Defense:* `safety: 31`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/__quadpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.979 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_11: 15.979, file_cluster_8: 16.021, file_cluster_0: 16.077
- **Magnitude:** 5184.48 | **LOC:** 6857 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.3307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dqelg` (Impact: 57.8)
    * *Intent:* // chebyshev series expansion // standard fortran subroutine // double precision version // // param...
  * `dqpsrt` (Impact: 46.1)
    * *Intent:* *result = 0.0; *abserr = 0.0;
  * `dqmomo` (Impact: 37.4)
  * `dqwgts` (Impact: 30.9)
    * *Intent:* // ***author piessens,robert,appl. math. & progr. div. - k.u.leuven // de doncker,elise,appl. math. ...
  * `dqcheb` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 99`, `args: 46`, `func_start: 7`
* *Risk/State:* `state_mutation: 4725`, `dead_code: 42`
* *Architecture:* `api: 191`, `import: 2`
* *Defense:* `doc: 11`, `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, __quadpack.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/linalg/src/_matfuncs_expm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.561 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.553 IQR)
- **Top Global Matches:** file_cluster_8: 15.561, file_cluster_11: 15.805, file_cluster_13: 15.813
- **Magnitude:** 5108.04 | **LOC:** 2912 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (72.7583%), Tech Debt (9.1962%)
**Top Internal Functions/Classes:**
  * `pick_pade_structure_s` (Impact: 118.1)
    * *Intent:* /*******************************************************************************
  * `pick_pade_structure_d` (Impact: 118.1)
  * `pade_UV_calc_d` (Impact: 84.3)
  * `pade_UV_calc_s` (Impact: 84.1)
  * `pade_UV_calc_c` (Impact: 71.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 122`, `args: 12`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3836`, `orphaned_logic: 4`
* *Architecture:* `api: 294`, `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 68`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _common_array_utils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_continuous_distns.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.7 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_8: 11.7, file_cluster_7: 11.95, file_cluster_0: 12.097
- **Magnitude:** 4572.86 | **LOC:** 12588 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 35.0%
- **Risk Profile:** Cognitive Load (5.6843%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 129.5)
    * *Intent:* %(example)s """
  * `fit` (Impact: 92.8)
    * *Intent:* # Naive implementation of first and second moment to address gh-18071. # https://variation.com/wp-co...
  * `_rvs_scalar` (Impact: 73.7)
  * `fit` (Impact: 65.5)
    * *Intent:* # fatiguelife.pdf(x, c) = # (x+1) / (2*c*sqrt(2*pi*x**3)) * exp(-(x-1)**2/(2*x*c**2)) return np.exp(...
  * `fit` (Impact: 59.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 2626`, `args: 1284`, `func_start: 1189`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 136`, `dead_code: 33`, `fragile_debt: 3`, `duplicate_logic: 1074`
* *Architecture:* `api: 281`, `import: 26`
* *Defense:* `safety: 25`, `doc: 324`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ._constants, ._ksstats, ._censored_data, scipy._external.array_api_extra, scipy.stats, scipy.optimize, scipy._lib._ccallback, operator...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/lsoda.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.579 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.795 IQR)
- **Top Global Matches:** file_cluster_11: 16.579, file_cluster_13: 16.64, file_cluster_0: 16.689
- **Magnitude:** 3853.34 | **LOC:** 2322 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (48.1368%), Tech Debt (8.5913%)
**Top Internal Functions/Classes:**
  * `stoda` (Impact: 408.1)
    * *Intent:* // 350
  * `lsoda` (Impact: 269.7)
  * `stoda_corrector_loop` (Impact: 143.7)
  * `prja` (Impact: 113.2)
  * `intdy` (Impact: 41.8)
    * *Intent:* // we are currently using a bdf method. consider switching to adams. // compute the step size we cou...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `structural_boundaries: 121`, `args: 14`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 2537`, `dead_code: 18`, `fragile_debt: 1`
* *Architecture:* `api: 143`, `import: 3`
* *Defense:* `doc: 118`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, stdio.h, lsoda.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/optimize/src/minpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.44 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.854 IQR)
- **Top Global Matches:** file_cluster_11: 16.44, file_cluster_0: 16.569, file_cluster_13: 16.638
- **Magnitude:** 3829.96 | **LOC:** 4267 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (85.6299%), Tech Debt (8.1866%)
**Top Internal Functions/Classes:**
  * `lmpar` (Impact: 154.7)
  * `qrfac` (Impact: 79.0)
  * `qrsolv` (Impact: 76.4)
  * `r1updt` (Impact: 66.6)
  * `dogleg` (Impact: 60.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 53`, `args: 28`, `func_start: 10`
* *Risk/State:* `state_mutation: 3048`, `dead_code: 36`, `orphaned_logic: 1`
* *Architecture:* `api: 118`, `import: 3`
* *Defense:* `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, minpack.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/optimize/tnc/tnc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.498 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.814 IQR)
- **Top Global Matches:** file_cluster_8: 14.498, file_cluster_13: 14.706, file_cluster_11: 14.733
- **Magnitude:** 3702.64 | **LOC:** 2065 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.3907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tnc_minimize` (Impact: 458.9)
  * `getptcIter` (Impact: 378.9)
  * `tnc` (Impact: 309.8)
  * `tnc_direction` (Impact: 198.6)
  * `linearSearch` (Impact: 100.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 70`, `args: 57`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 1539`, `dead_code: 1`
* *Architecture:* `api: 269`, `import: 5`
* *Defense:* `immutability_locks: 32`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tnc.h, stdio.h, float.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/src/zvode.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.524 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.698 IQR)
- **Top Global Matches:** file_cluster_8: 15.524, file_cluster_7: 15.586, file_cluster_13: 15.642
- **Magnitude:** 3185.68 | **LOC:** 2785 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (37.4547%), Tech Debt (9.3738%)
**Top Internal Functions/Classes:**
  * `zvode` (Impact: 174.6)
    * *Intent:* // Up to MAXCOR corrector iterations are taken. A convergence test is // made on the r.m.s. norm of ...
  * `zvjac` (Impact: 157.4)
  * `zvhin` (Impact: 107.7)
  * `zvnlsd` (Impact: 72.2)
    * *Intent:* // Inline DZSCAL: Multiply Jacobian by scalar -HRL1 (real scalar × complex vector) // Use scalar * c...
  * `zvjust` (Impact: 48.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 114`, `args: 7`, `func_start: 13`
* *Risk/State:* `state_mutation: 2232`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 230`, `import: 4`
* *Defense:* `doc: 119`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, float.h, stdlib.h, zvode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/tests/test_stats.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.174 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.548 IQR)
- **Top Global Matches:** file_cluster_8: 12.174, file_cluster_0: 12.308, file_cluster_7: 12.539
- **Magnitude:** 3030.56 | **LOC:** 9891 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 82.0%
- **Risk Profile:** Cognitive Load (5.05%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_input_validation_edge_cases` (Impact: 1754.1)
  * `test_near_constant_input` (Impact: 144.9)
  * `test_tmin_tmax_nanpolicy` (Impact: 11.7)
    * *Intent:* # check that if a full slice is masked, the output returns a
  * `test_alternative_nan_policy` (Impact: 10.0)
  * `test_resampling_exact_2x2` (Impact: 9.3)
    * *Intent:* # Compare against R fisher.exact # options(digits=16) # c(1, 2, 2, 1, 1, 0, 1), # c(2, 0, 0, 2, 3, 0...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 865`, `structural_boundaries: 909`, `args: 643`, `func_start: 640`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 31`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 90`
* *Architecture:* `io: 4`, `api: 704`, `import: 28`
* *Defense:* `safety: 149`, `doc: 56`, `test: 1142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` contextlib, scipy._external.array_api_extra, scipy.stats, scipy._lib._array_api_no_0d, os, hypothesis, scipy.special._testutils, scipy.stats._stats_py...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/special/tests/test_basic.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.757 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_8: 10.757, file_cluster_0: 11.052, file_cluster_7: 11.184
- **Magnitude:** 3015.46 | **LOC:** 4863 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (4.1333%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_factorial_array_corner_cases` (Impact: 105.3)
  * `test_factorial2_array_corner_cases` (Impact: 89.2)
    * *Intent:* # Reference values from mpmath for:
  * `test_factorialk_array_corner_cases` (Impact: 89.2)
    * *Intent:* # complex values
  * `test_factorialx_inf_nan` (Impact: 72.6)
  * `test_factorial_scalar_corner_cases` (Impact: 50.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 724`, `args: 519`, `func_start: 513`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 19`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 144`
* *Architecture:* `io: 9`, `api: 870`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 47`, `doc: 40`, `test: 684`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` threading, platform, operator, scipy.special._testutils, numpy.testing, itertools, numpy, scipy._lib._util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/tests/test_base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.098 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.337 IQR)
- **Top Global Matches:** file_cluster_8: 11.098, file_cluster_7: 11.572, file_cluster_0: 11.647
- **Magnitude:** 2961.28 | **LOC:** 5971 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (5.9671%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_set` (Impact: 122.0)
  * `test_scalar_assign_2` (Impact: 110.4)
  * `with_64bit_maxval_limit` (Impact: 65.5)
  * `test_argmax` (Impact: 44.1)
    * *Intent:* # We are only testing sparse matrices who have # implemented 'min' and 'max' because they are # the ...
  * `test_minmax_axis` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 679`, `args: 362`, `func_start: 360`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 52`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 134`
* *Architecture:* `io: 1`, `api: 531`, `import: 24`
* *Defense:* `safety: 194`, `doc: 28`, `test: 418`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` contextlib, platform, scipy.sparse._sputils, scipy.sparse._base, scipy.sparse.linalg, operator, types, scipy.linalg...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/vode.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.349 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.82 IQR)
- **Top Global Matches:** file_cluster_8: 15.349, file_cluster_7: 15.413, file_cluster_13: 15.487
- **Magnitude:** 2907.64 | **LOC:** 2452 | **CtrlFlow:** 74.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.732%), Tech Debt (10.3678%)
**Top Internal Functions/Classes:**
  * `dvjac` (Impact: 196.7)
  * `dvode` (Impact: 164.1)
    * *Intent:* // Up to MAXCOR corrector iterations are taken. A convergence test is // made on the r.m.s. norm of ...
  * `dvhin` (Impact: 90.4)
    * *Intent:* // Order increase
  * `dvjust` (Impact: 72.9)
  * `dvnlsd` (Impact: 49.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 111`, `args: 9`, `func_start: 13`
* *Risk/State:* `state_mutation: 1980`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 209`, `import: 2`
* *Defense:* `doc: 101`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vode.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_distribution_infrastructure.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.141 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.141 IQR)
- **Top Global Matches:** file_cluster_8: 12.141, file_cluster_0: 12.21, file_cluster_13: 12.373
- **Magnitude:** 2797.86 | **LOC:** 5777 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 70.0%
- **Risk Profile:** Cognitive Load (26.757%), Tech Debt (91.4911%)
**Top Internal Functions/Classes:**
  * `plot` (Impact: 633.6)
  * `filtered` (Impact: 100.2)
  * `_set_invalid_nan` (Impact: 80.7)
    * *Intent:* -------
  * `__str__` (Impact: 45.2)
    * *Intent:* # Floating point types are used for even integer parameters. # Convert to float here to ensure consi...
  * `_moment_central_dispatch` (Impact: 43.2)
    * *Intent:* # Improvements: # Lazy evaluation of cdf/ccdf only where needed # Stack x and y to reduce function c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 960`, `args: 459`, `func_start: 442`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 228`, `dead_code: 9`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 35`
* *Architecture:* `api: 126`, `import: 19`
* *Defense:* `safety: 59`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.446
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` types, matplotlib.pyplot, numpy, scipy._lib._util, scipy._lib._array_api, scipy.integrate, inspect, scipy.stats._probability_distribution...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/dop.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.703 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 14.703, file_cluster_13: 14.979, file_cluster_7: 15.015
- **Magnitude:** 2606.28 | **LOC:** 1121 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.0162%), Tech Debt (10.7449%)
**Top Internal Functions/Classes:**
  * `dp86co` (Impact: 293.9)
  * `dopcor` (Impact: 246.5)
  * `dopri5` (Impact: 133.5)
  * `dopri853` (Impact: 129.9)
  * `hinit` (Impact: 64.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 51`, `args: 11`, `func_start: 7`
* *Risk/State:* `state_mutation: 1372`, `orphaned_logic: 3`
* *Architecture:* `api: 272`, `import: 1`
* *Defense:* `immutability_locks: 263`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dop.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/interpolate/src/__fitpack.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.537 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.705 IQR)
- **Top Global Matches:** file_cluster_8: 15.537, file_cluster_13: 15.592, file_cluster_11: 15.612
- **Magnitude:** 2561.4 | **LOC:** 1887 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (67.0569%), Tech Debt (21.4871%)
**Top Internal Functions/Classes:**
  * `qr_reduce_periodic` (Impact: 213.5)
  * `init_augmented_matrices` (Impact: 89.7)
  * `_evaluate_ndbspline` (Impact: 79.9)
  * `_fpbacp` (Impact: 63.2)
  * `qr_reduce_augmented_matrices` (Impact: 59.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 95`, `args: 34`, `func_start: 15`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 1766`, `dead_code: 9`, `orphaned_logic: 11`
* *Architecture:* `import: 6`
* *Defense:* `doc: 4`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` algorithm, Python.h, vector, string, __fitpack.h, cstdint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/qhull_r/libqhull_r/io_r.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.053 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.402 IQR)
- **Top Global Matches:** file_cluster_8: 14.053, file_cluster_0: 14.388, file_cluster_13: 14.389
- **Magnitude:** 2552.94 | **LOC:** 4129 | **CtrlFlow:** 90.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.0979%), Tech Debt (15.6564%)
**Top Internal Functions/Classes:**
  * `qh_readpoints` (Impact: 255.8)
  * `qh_printfacetheader` (Impact: 75.8)
  * `qh_printfacets` (Impact: 44.6)
  * `qh_detvnorm` (Impact: 38.6)
  * `qh_printend` (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 67`, `args: 4`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1349`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 258`, `import: 1`
* *Defense:* `safety: 18`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/tests/test_distributions.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.84 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.603 IQR)
- **Top Global Matches:** file_cluster_0: 12.84, file_cluster_8: 13.107, file_cluster_9: 13.349
- **Magnitude:** 2384.16 | **LOC:** 10558 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 52.9%
- **Risk Profile:** Cognitive Load (3.0902%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fit_mm` (Impact: 29.7)
    * *Intent:* # Expected value computed with mpmath: # # >>> import mpmath # >>> mpmath.mp.dps = 150 # >>> cdf1 = ...
  * `test_fit_warnings` (Impact: 27.3)
    * *Intent:* # Numerical result may equal analytical result if some code path
  * `assert_fit_warnings` (Impact: 21.8)
  * `test_fit_MLE_comp_optimizer` (Impact: 18.3)
    * *Intent:* # reference values were computed via mpmath # from mpmath import mp # mp.dps = 100 # def halfnorm_cd...
  * `test_fit_MLE_comp_optimizer` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 1135`, `args: 802`, `func_start: 753`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 36`, `dead_code: 131`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 232`, `orphaned_logic: 190`
* *Architecture:* `io: 7`, `api: 848`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 197`, `doc: 58`, `test: 1157`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` threading, scipy.stats._continuous_distns, platform, pathlib, json, scipy.stats, scipy.optimize, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/linalg/_propack/PROPACK/src/lanbpro.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.724 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_8: 14.724, file_cluster_7: 15.0, file_cluster_13: 15.025
- **Magnitude:** 2289.38 | **LOC:** 1651 | **CtrlFlow:** 95.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.0347%), Tech Debt (11.4742%)
**Top Internal Functions/Classes:**
  * `slanbpro` (Impact: 115.3)
  * `dlanbpro` (Impact: 115.2)
  * `clanbpro` (Impact: 114.1)
  * `zlanbpro` (Impact: 114.1)
  * `ssafescal` (Impact: 3.8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 20`, `func_start: 8`
* *Risk/State:* `state_mutation: 1702`, `orphaned_logic: 5`
* *Architecture:* `api: 93`, `import: 3`
* *Defense:* `doc: 10`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, float.h, lanbpro.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/linalg/_eigen/arpack/arnaud/src/arnaud_n_double.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.733 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.469 IQR)
- **Top Global Matches:** file_cluster_8: 14.733, file_cluster_11: 14.862, file_cluster_13: 14.892
- **Magnitude:** 2204.18 | **LOC:** 2104 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (88.7775%), Tech Debt (9.7398%)
**Top Internal Functions/Classes:**
  * `ARNAUD_dneupd` (Impact: 380.1)
  * `dnaup2` (Impact: 252.8)
  * `dnaitr` (Impact: 135.1)
  * `dnapps` (Impact: 116.7)
  * `ARNAUD_dnaupd` (Impact: 92.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 78`, `args: 25`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 1008`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 69`, `import: 2`
* *Defense:* `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, arnaud_n_double.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/linalg/_eigen/arpack/arnaud/src/arnaud_n_single.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.727 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.473 IQR)
- **Top Global Matches:** file_cluster_8: 14.727, file_cluster_11: 14.867, file_cluster_13: 14.886
- **Magnitude:** 2204.18 | **LOC:** 2104 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (88.7775%), Tech Debt (9.7398%)
**Top Internal Functions/Classes:**
  * `ARNAUD_sneupd` (Impact: 380.1)
  * `snaup2` (Impact: 252.8)
  * `snaitr` (Impact: 135.1)
  * `snapps` (Impact: 116.7)
  * `ARNAUD_snaupd` (Impact: 92.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 78`, `args: 25`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 1008`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 69`, `import: 2`
* *Defense:* `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, arnaud_n_single.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_stats_py.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.01 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.531 IQR)
- **Top Global Matches:** file_cluster_8: 12.01, file_cluster_0: 12.2, file_cluster_7: 12.214
- **Magnitude:** 2189.22 | **LOC:** 11252 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 79.3%
- **Risk Profile:** Cognitive Load (13.2738%), Tech Debt (38.4387%)
**Top Internal Functions/Classes:**
  * `_kendalltau` (Impact: 1318.8)
    * *Intent:* # no range given, so use values in `a`
  * `_f_oneway_is_too_small` (Impact: 341.4)
  * `hmean` (Impact: 57.0)
  * `iqr` (Impact: 33.9)
    * *Intent:* # Calculate variance of sample, warning if precision is lost xp = array_namespace(x) if xp is None e...
  * `kendalltau` (Impact: 33.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 904`, `structural_boundaries: 450`, `args: 196`, `func_start: 158`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 54`, `dead_code: 11`, `planned_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 100`, `import: 29`
* *Defense:* `safety: 32`, `doc: 176`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.383
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` scipy.optimize.elementwise, scipy._external.array_api_extra, scipy.stats, scipy.optimize, ._stats, operator, jax.scipy.stats, dataclasses...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `scipy/sparse/sparsetools/csr.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.68 IQR)
- **Local Micro-Species:** `Cluster 1: Algorithmic Bitwise & Encapsulated Core` (Drift: 5.354 IQR)
- **Top Global Matches:** file_cluster_8: 14.68, file_cluster_11: 14.768, file_cluster_13: 14.791
- **Magnitude:** 1954.08 | **LOC:** 1747 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.7766%), Tech Debt (8.3105%)
**Top Internal Functions/Classes:**
  * `csr_sample_offsets` (Impact: 22.3)
  * `csr_sample_values` (Impact: 20.8)
    * *Intent:* /* * Sum together duplicate column entries in each row of CSR matrix A
  * `csr_binop_csr_canonical` (Impact: 18.6)
    * *Intent:* /* * Compute C = A*B for CSR matrices A,B * * * Input Arguments: * I n_row - number of rows in A * I...
  * `csr_binop_csr_general` (Impact: 11.6)
  * `get_csr_submatrix` (Impact: 11.6)
    * *Intent:* //tail
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 85`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 1254`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 441`, `import: 7`
* *Defense:* `safety: 2`, `test: 2`, `immutability_locks: 495`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.956
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, functional, dense.h, vector, set, numeric, util.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy/sparse/linalg/_eigen/arpack/arnaud/src/arnaud_s_single.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.472 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.148 IQR)
- **Top Global Matches:** file_cluster_8: 14.472, file_cluster_13: 14.73, file_cluster_11: 14.76
- **Magnitude:** 1887.42 | **LOC:** 2236 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.9885%)
**Top Internal Functions/Classes:**
  * `ARNAUD_sseupd` (Impact: 447.2)
  * `ssaitr` (Impact: 159.6)
    * *Intent:* // Back from computing user specified shifts
  * `sstqrb` (Impact: 93.0)
  * `ssesrt` (Impact: 50.5)
  * `ssortr` (Impact: 44.2)
    * *Intent:* // Move the NP shifts to the first NP locations of RITZ to
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 55`, `args: 21`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 998`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 58`, `import: 2`
* *Defense:* `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` arnaud_s_single.h, float.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `scipy/stats/_stats.pxd` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scipy/sparse/tests/test_dok.py` (PYTHON) | Magnitude: 194.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, test: 101, structural_boundaries: 98, safety: 54
- `scipy/interpolate/tests/test_fitpack.py` (PYTHON) | Magnitude: 246.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 342, structural_boundaries: 98, test: 61, api: 44
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/dgstrs.c` (C) | Magnitude: 568.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 397, pointers: 150, indent_tabs: 65, branch: 64
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/sgstrs.c` (C) | Magnitude: 568.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 397, pointers: 150, indent_tabs: 65, branch: 64
- `scipy/special/tests/test_dd.py` (PYTHON) | Magnitude: 4.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, encapsulation: 8, structural_boundaries: 7, test: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scipy/optimize/src/nnls.c` (C) | Magnitude: 442.14 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 362, indent_spaces: 176, branch: 55, pointers: 42
- `scipy/ndimage/src/ni_interpolation.c` (C) | Magnitude: 1502.42 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1060, indent_spaces: 881, branch: 330, api: 135
- `scipy/sparse/sparsetools/dense.h` (C) | Magnitude: 119.26 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 85, indent_spaces: 31, scientific: 24, immutability_locks: 21
- `scipy/integrate/__quadpack.c` (C) | Magnitude: 5184.48 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 4725, indent_spaces: 3056, pointers: 972, branch: 680
- `scipy/integrate/src/lsoda.c` (C) | Magnitude: 3853.34 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 2537, indent_spaces: 1403, pointers: 1124, branch: 470

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scipy/stats/biasedurn/randomc.h` (CPP) | Magnitude: 7.72 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 26, reflection_metaprogramming: 20, indent_spaces: 20, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scipy/special/ellint_carlson_cpp_lite/ellint_arithmetic.hh` (CPP) | Magnitude: 218.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 173, structural_boundaries: 82, indent_spaces: 78, indent_tabs: 75
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/read_body.hpp` (CPP) | Magnitude: 619.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 399, state_mutation: 353, branch: 118, structural_boundaries: 108
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_ddrop_row.c` (C) | Magnitude: 463.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 284, indent_tabs: 111, branch: 89, pointers: 73
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_sdrop_row.c` (C) | Magnitude: 463.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 284, indent_tabs: 111, branch: 89, pointers: 73
- `scipy/special/_ellip_harm.py` (PYTHON) | Magnitude: 21.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, encapsulation: 14, indent_spaces: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scipy/special/cython_special.pyi` (PYTHON) | Magnitude: 15.18 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, safety_bypasses: 2, args: 1, func_start: 1
- `scipy/spatial/distance.pyi` (PYTHON) | Magnitude: 69.58 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 39, api: 33, generics: 32
- `scipy/spatial/transform/_rigid_transform.py` (PYTHON) | Magnitude: 173.92 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, encapsulation: 129, structural_boundaries: 104, doc: 66
- `scipy/special/_orthogonal.pyi` (PYTHON) | Magnitude: 115.8 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 149, encapsulation: 143, structural_boundaries: 74, generics: 72
- `scipy/signal/_short_time_fft.py` (PYTHON) | Magnitude: 779.5 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 556, branch: 179, state_mutation: 151, structural_boundaries: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scipy/io/_harwell_boeing/hb.py` (PYTHON) | Magnitude: 325.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 315, structural_boundaries: 77, branch: 76, encapsulation: 69
- `scipy/spatial/_spherical_voronoi.py` (PYTHON) | Magnitude: 97.1 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 29, encapsulation: 25, branch: 20
- `scipy/io/matlab/tests/gen_mat5files.m` (MATLAB) | Magnitude: 34.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 6, io: 4, structural_boundaries: 3
- `scipy/special/_precompute/utils.py` (PYTHON) | Magnitude: 17.8 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, branch: 6, state_mutation: 6
- `subprojects/pyprima/pyprima/pyprima/src/pyprima/common/_nonlinear_constraints.py` (PYTHON) | Magnitude: 59.26 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, branch: 12, structural_boundaries: 10, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/read_body_threads.hpp` (CPP) | Magnitude: 112.4 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 96, indent_spaces: 85, branch: 25, structural_boundaries: 17
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/write_body_threads.hpp` (CPP) | Magnitude: 30.58 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 22, indent_spaces: 18, structural_boundaries: 8, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scipy/stats/_tukeylambda_stats.py` (PYTHON) | Magnitude: 19.5 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, encapsulation: 16, structural_boundaries: 10, dead_code: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scipy/sparse/linalg/_propack/PROPACK/src/include/lanbpro.h` (C) | Magnitude: 33.5 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 86, api: 18, indent_spaces: 14, structural_boundaries: 4
- `scipy/sparse/linalg/_propack/PROPACK/src/include/common.h` (C) | Magnitude: 31.42 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 124, immutability_locks: 76, structural_boundaries: 48, api: 16
- `scipy/sparse/linalg/_propack/PROPACK/src/include/gemm_overwrite.h` (C) | Magnitude: 21.2 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 72, immutability_locks: 26, structural_boundaries: 24, api: 6
- `scipy/integrate/src/dop.h` (C) | Magnitude: 23.26 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 57, sec_high_risk_execution: 10, api: 8, structural_boundaries: 6
- `benchmarks/benchmarks/linprog_benchmark_files/__init__.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, branch: 2, api: 1, comprehensions: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scipy/odr/_odrpack.py` (PYTHON) | Magnitude: 636.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 422, state_mutation: 222, branch: 174, structural_boundaries: 64
- `subprojects/pyprima/pyprima/pyprima/src/pyprima/cobyla/trustregion.py` (PYTHON) | Magnitude: 316.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, branch: 83, structural_boundaries: 64, sec_high_risk_execution: 35
- `scipy/optimize/_direct/DIRect.c` (C) | Magnitude: 236.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 142, pointers: 73, branch: 49
- `scipy/stats/_stats_pythran.py` (PYTHON) | Magnitude: 143.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 166, branch: 44, structural_boundaries: 28, encapsulation: 14
- `scipy/stats/tests/test_axis_nan_policy.py` (PYTHON) | Magnitude: 943.2 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 911, branch: 249, explicit_casts: 168, structural_boundaries: 152

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scipy/optimize/cython_optimize/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 6, dead_code: 1
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/dgsisx.c` (C) | Magnitude: 142.14 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 123, branch: 27, indent_tabs: 23, pointers: 17
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/sgsisx.c` (C) | Magnitude: 142.14 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 123, branch: 27, indent_tabs: 23, pointers: 17
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/cgsisx.c` (C) | Magnitude: 130.14 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 111, branch: 27, pointers: 25, indent_tabs: 23
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/zgsisx.c` (C) | Magnitude: 130.14 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 111, branch: 27, pointers: 25, indent_tabs: 23

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scipy/linalg/src/_common_array_utils.hh` -> Churn: **78.43%** | Cog Load: 79.1563% | Debt: 41.0929%
- `scipy/linalg/src/_batched_linalg_module.cc` -> Churn: **73.73%** | Cog Load: 77.5734% | Debt: 8.6775%
- `scipy/spatial/transform/_rotation.py` -> Churn: **71.92%** | Cog Load: 23.5792% | Debt: 54.0102%
- `scipy/linalg/src/_linalg_solve.hh` -> Churn: **68.23%** | Cog Load: 81.3926% | Debt: 20.3054%
- `scipy/stats/_continuous_distns.py` -> Churn: **67.2%** | Cog Load: 5.6843% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scipy/interpolate/src/dfitpack.c` -> **ilayn** (93.1% isolated ownership) | Magnitude: 15275.86
- `scipy/optimize/tnc/tnc.c` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 3702.64
- `scipy/stats/tests/test_stats.py` -> **Matt Haberland** (82.0% isolated ownership) | Magnitude: 3030.56
- `scipy/integrate/src/dop.c` -> **Ilhan Polat** (100.0% isolated ownership) | Magnitude: 2606.28
- `scipy/sparse/sparsetools/csr.h` -> **Dan Schult** (100.0% isolated ownership) | Magnitude: 1954.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scipy/stats/contingency.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 49.0001%)
- `benchmarks/benchmarks/integrate.py` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.5163%)
- `benchmarks/benchmarks/sparse.py` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 99.9292%)
- `scipy/optimize/_trustregion.py` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 96.6823%)
- `scipy/io/matlab/_mio.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 56.1269%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benchmarks/benchmarks/sparse.py` -> **Severity: 3020.8** (Blast Radius: 30.208 * Doc Risk: 100.0%)
- `benchmarks/benchmarks/special.py` -> **Severity: 2118.692** (Blast Radius: 21.187 * Doc Risk: 99.9996%)
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/slu_ddefs.h` -> **Severity: 1301.2** (Blast Radius: 13.012 * Doc Risk: 100.0%)
- `scipy/sparse/linalg/_dsolve/scipy_slu_config.h` -> **Severity: 1215.7** (Blast Radius: 12.157 * Doc Risk: 100.0%)
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/slu_sdefs.h` -> **Severity: 981.2** (Blast Radius: 9.812 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
