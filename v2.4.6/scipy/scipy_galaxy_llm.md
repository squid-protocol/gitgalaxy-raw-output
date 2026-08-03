# ARCHITECTURAL_BRIEF: scipy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/scipy` |
| **Timestamp** | `2026-08-03T19:41:12.530571+00:00` |
| **Scan Duration** | `14.43s` |
| **Git Branch** | `main` |
| **Git Commit** | `355b747ccae64368a7dce38825361eca6055fcd1` |
| **Git Remote** | `https://github.com/scipy/scipy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1650 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.538`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1180 | 63.7% |
| file_cluster_13 | 349 | 18.8% |
| file_cluster_0 | 63 | 3.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 24.9 | 9.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 27.8 | 4.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.3 | 5.2 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 37.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 74.1 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.0 | 1.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.8 | 48.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 64.4 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 38.4 | 20.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.4 | 0.0 | 0.0 |
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

- `test_input_validation_edge_cases` (@ `scipy/stats/tests/test_stats.py`) -> Impact: **5118.6** | LOC: 8165
- `nonlin_solve` (@ `scipy/optimize/_nonlin.py`) -> Impact: **4419.8** | LOC: 1036
- `_kendalltau` (@ `scipy/stats/_stats_py.py`) -> Impact: **4335.0** | LOC: 2247
  * *Intent:* # no range given, so use values in `a`
- `plot` (@ `scipy/stats/_distribution_infrastructure.py`) -> Impact: **3919.6** | LOC: 1719
- `eigh` (@ `scipy/linalg/_decomp.py`) -> Impact: **3782.0** | LOC: 429
- `test_funcs` (@ `scipy/stats/tests/test_continuous.py`) -> Impact: **3228.6** | LOC: 2007
- `_monte_carlo_test_iv` (@ `scipy/stats/_resampling.py`) -> Impact: **3101.3** | LOC: 707
- `_process_size` (@ `scipy/stats/_multivariate.py`) -> Impact: **2923.3** | LOC: 2451
- `_validate_mahalanobis_kwargs` (@ `scipy/spatial/distance.py`) -> Impact: **2568.2** | LOC: 963
- `_reduce_func` (@ `scipy/stats/_distn_infrastructure.py`) -> Impact: **2522.6** | LOC: 990

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__new__` (@ `benchmarks/benchmarks/cython_special.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_B.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_B.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_B.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_B.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_B.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_C.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_C.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_C.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `benchmarks/benchmarks/go_benchmark_functions/go_funcs_C.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `DODPC3` (@ `scipy/odr/odrpack/d_odr.f`) -> DB Complexity: **401**
- `lsoda` (@ `scipy/integrate/src/lsoda.c`) -> DB Complexity: **355**
- `qh_rboxpoints2` (@ `subprojects/qhull_r/libqhull_r/rboxlib_r.c`) -> DB Complexity: **333**
- `DODPC1` (@ `scipy/odr/odrpack/d_odr.f`) -> DB Complexity: **326**
- `dp86co` (@ `scipy/integrate/src/dop.c`) -> DB Complexity: **317**
- `DODPE1` (@ `scipy/odr/odrpack/d_odr.f`) -> DB Complexity: **292**
- `fpgrsp` (@ `scipy/interpolate/src/dfitpack.c`) -> DB Complexity: **265**
  * *Intent:* // subroutine fpcyt2 solves a linear n x n system // a * c = b // where matrix a is a cyclic tridiagonal matrix, decomposed
- `fppara` (@ `scipy/interpolate/src/dfitpack.c`) -> DB Complexity: **255**
  * *Intent:* // test whether there are non-zero values in the new row of (avv) // corresponding to the b-splines n(j;v),j=nv7+1,...,nv4.
- `fpclos` (@ `scipy/interpolate/src/dfitpack.c`) -> DB Complexity: **251**
- `zvode` (@ `scipy/integrate/src/zvode.c`) -> DB Complexity: **249**
  * *Intent:* // Up to MAXCOR corrector iterations are taken. A convergence test is // made on the r.m.s. norm of each correction, weighted by the error // weight v...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scipy/sparse/linalg/_dsolve/SuperLU/SRC` | 193 | 81478.66 | 62.07% | 27.55% |
| `scipy/stats` | 68 | 55862.88 | 13.37% | 35.01% |
| `scipy/optimize` | 69 | 36243.78 | 20.78% | 30.37% |
| `scipy/interpolate/src` | 6 | 36233.26 | 45.68% | 10.35% |
| `scipy/stats/tests` | 41 | 34895.02 | 5.39% | 0.0% |
| `scipy/linalg` | 47 | 32681.92 | 11.44% | 24.51% |
| `scipy/signal` | 45 | 29201.26 | 23.34% | 36.93% |
| `scipy/interpolate` | 33 | 21443.2 | 15.79% | 60.22% |
| `scipy/linalg/src` | 14 | 21140.96 | 69.35% | 17.61% |
| `subprojects/qhull_r/libqhull_r` | 30 | 20909.34 | 49.45% | 17.04% |

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
- `scipy/special/xsf_wrappers.cpp` -> **248** Orphaned Functions | **0** Duplicates
- `scipy/stats/tests/test_morestats.py` -> **166** Orphaned Functions | **78** Duplicates
- `scipy/stats/tests/test_distributions.py` -> **111** Orphaned Functions | **126** Duplicates
- `scipy/stats/tests/test_multivariate.py` -> **157** Orphaned Functions | **78** Duplicates
- `scipy/stats/_continuous_distns.py` -> **0** Orphaned Functions | **233** Duplicates

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

### Exploit Generation Surface
- `benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cython_special.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/fft_basic.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/fftpack_pseudo_diffs.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/go_benchmark_functions/go_benchmark.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/spatial.py` -> **100.0%** Exposure
- `scipy/datasets/_fetchers.py` -> **100.0%** Exposure
- `scipy/spatial/tests/test_kdtree.py` -> **100.0%** Exposure
- `tools/authors.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `scipy/integrate/__quadpack.c` -> **10.0%** Exposure
- `scipy/integrate/src/lsoda.c` -> **10.0%** Exposure
- `scipy/integrate/src/vode.c` -> **10.0%** Exposure
- `scipy/integrate/src/zvode.c` -> **10.0%** Exposure
- `scipy/optimize/_minpackmodule.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cluster_hierarchy_disjoint_set.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cython_special.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/fft_basic.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6656` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benchmarks/benchmarks/fft_basic.py` (PYTHON) -> Cumulative Risk: **898.4**
- **Archetype:** `file_cluster_13` (Distance: 12.682 IQR)
- **Magnitude:** 508.9 | **LOC:** 355 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup` (Impact: 46.0), `setup` (Impact: 45.9), `setup` (Impact: 22.9)

### 2. `benchmarks/benchmarks/integrate.py` (PYTHON) -> Cumulative Risk: **885.13**
- **Archetype:** `file_cluster_8` (Distance: 11.012 IQR)
- **Magnitude:** 356.6 | **LOC:** 405 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setup` (Impact: 59.8), `setup` (Impact: 19.3), `setup` (Impact: 16.5)

### 3. `benchmarks/benchmarks/signal_filtering.py` (PYTHON) -> Cumulative Risk: **864.53**
- **Archetype:** `file_cluster_8` (Distance: 10.448 IQR)
- **Magnitude:** 105.72 | **LOC:** 121 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `time_sosfilt` (Impact: 15.3), `_medfilt2d` (Impact: 10.5), `setup` (Impact: 3.6)

### 4. `benchmarks/benchmarks/spatial.py` (PYTHON) -> Cumulative Risk: **860.49**
- **Archetype:** `file_cluster_13` (Distance: 12.176 IQR)
- **Magnitude:** 557.22 | **LOC:** 565 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `time_count_neighbors` (Impact: 30.1), `setup` (Impact: 21.5), `setup` (Impact: 21.4)

### 5. `scipy/io/_harwell_boeing/_fortran_format_parser.py` (PYTHON) -> Cumulative Risk: **834.45**
- **Archetype:** `file_cluster_8` (Distance: 11.661 IQR)
- **Magnitude:** 343.82 | **LOC:** 317 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9703%)
- **Heaviest Functions:** `_parse_format` (Impact: 81.0), `python_format` (Impact: 44.2), `parse` (Impact: 32.1)

### 6. `benchmarks/benchmarks/optimize_zeros.py` (PYTHON) -> Cumulative Risk: **823.18**
- **Archetype:** `file_cluster_13` (Distance: 12.231 IQR)
- **Magnitude:** 197.92 | **LOC:** 117 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 85.5), `setup` (Impact: 35.8), `time_array_newton` (Impact: 5.2)

### 7. `scipy/sparse/linalg/_dsolve/_superluobject.c` (C) -> Cumulative Risk: **820.48**
- **Archetype:** `file_cluster_8` (Distance: 12.808 IQR)
- **Magnitude:** 1404.62 | **LOC:** 1134 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `LU_to_csc` (Impact: 153.0), `LU_to_csc_matrix` (Impact: 93.0), `SuperLU_solve` (Impact: 88.2)

### 8. `scipy/integrate/_ivp/base.py` (PYTHON) -> Cumulative Risk: **812.15**
- **Archetype:** `file_cluster_8` (Distance: 12.961 IQR)
- **Magnitude:** 376.58 | **LOC:** 306 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `step` (Impact: 110.4), `__init__` (Impact: 52.7), `check_arguments` (Impact: 43.1)

### 9. `scipy/sparse/linalg/_dsolve/_superlumodule.c` (C) -> Cumulative Risk: **810.35**
- **Archetype:** `file_cluster_8` (Distance: 12.258 IQR)
- **Magnitude:** 543.82 | **LOC:** 538 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Py_gstrs` (Impact: 110.1), `Py_gssv` (Impact: 62.5), `Py_gstrf` (Impact: 34.6)

### 10. `benchmarks/benchmarks/optimize_lap.py` (PYTHON) -> Cumulative Risk: **809.3**
- **Archetype:** `file_cluster_13` (Distance: 11.081 IQR)
- **Magnitude:** 60.7 | **LOC:** 69 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `time_evaluation` (Impact: 13.2), `setup` (Impact: 6.5), `setup` (Impact: 5.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scipy/interpolate/src/dfitpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.991 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_11: 16.991, file_cluster_0: 17.1, file_cluster_13: 17.103
- **Magnitude:** 27963.86 | **LOC:** 9383 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 93.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 265
- **Risk Profile:** Cognitive Load (38.9225%), Tech Debt (11.7036%)
**Top Internal Functions/Classes:**
  * `fpgrsp` (Impact: 2514.3 | O(N^6) | DB: 265)
    * *Intent:* // subroutine fpcyt2 solves a linear n x n system // a * c = b // where matrix a is a cyclic tridiag...
  * `fppara` (Impact: 2001.2 | O(N^6) | DB: 255)
    * *Intent:* // test whether there are non-zero values in the new row of (avv) // corresponding to the b-splines ...
  * `fpclos` (Impact: 1826.0 | O(N^6) | DB: 251)
  * `fpcurf` (Impact: 1729.7 | O(N^6) | DB: 209)
  * `fpperi` (Impact: 1439.2 | O(N^6) | DB: 193)
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

### `scipy/odr/odrpack/d_odr.f` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.933 IQR)
- **Top Global Matches:** file_cluster_8: 13.933, file_cluster_11: 14.199, file_cluster_13: 14.307
- **Magnitude:** 14658.0 | **LOC:** 10986 | **CtrlFlow:** 80.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 401
- **Risk Profile:** Cognitive Load (80.3596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DODMN` (Impact: 1121.1 | O(N^5) | DB: 137)
  * `DODPC1` (Impact: 1109.3 | O(N^6) | DB: 326)
  * `DODCHK` (Impact: 658.6 | O(N^5) | DB: 36)
  * `DODPC3` (Impact: 641.4 | O(N^5) | DB: 401)
  * `DODPE1` (Impact: 554.3 | O(N^5) | DB: 292)
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

### `scipy/linalg/_decomp_update.pyx.in` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.29 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.195 IQR)
- **Top Global Matches:** file_cluster_8: 9.29, file_cluster_7: 9.98, file_cluster_1: 10.219
- **Magnitude:** 13869.44 | **LOC:** 2351 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.3254%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 103`, `args: 8`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `dead_code: 9`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 8`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy.linalg, numpy, scipy._lib._util, scipy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/optimize/tnc/tnc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.498 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.814 IQR)
- **Top Global Matches:** file_cluster_8: 14.498, file_cluster_13: 14.706, file_cluster_11: 14.733
- **Magnitude:** 8726.74 | **LOC:** 2065 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (81.3907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tnc` (Impact: 1809.8 | O(2^N) | DB: 66)
  * `tnc_minimize` (Impact: 1555.2 | O(N^6) | DB: 113)
  * `getptcIter` (Impact: 1294.4 | O(N^6) | DB: 93)
  * `tnc_direction` (Impact: 674.9 | O(N^6) | DB: 41)
  * `linearSearch` (Impact: 335.4 | O(N^6) | DB: 41)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 70`, `args: 57`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 1539`, `dead_code: 1`
* *Architecture:* `api: 269`, `import: 5`
* *Defense:* `immutability_locks: 32`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, tnc.h, float.h, stdio.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_distribution_infrastructure.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.142 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.144 IQR)
- **Top Global Matches:** file_cluster_8: 12.142, file_cluster_0: 12.212, file_cluster_13: 12.375
- **Magnitude:** 8192.86 | **LOC:** 5777 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 70.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (26.6936%), Tech Debt (79.3931%)
**Top Internal Functions/Classes:**
  * `plot` (Impact: 3919.6 | O(2^N) | DB: 43)
  * `_set_invalid_nan` (Impact: 262.6 | O(N^6) | DB: 1)
    * *Intent:* -------
  * `draw` (Impact: 162.2 | O(2^N))
  * `_moment_central_dispatch` (Impact: 147.3 | O(N^6))
    * *Intent:* # Improvements: # Lazy evaluation of cdf/ccdf only where needed # Stack x and y to reduce function c...
  * `__str__` (Impact: 110.2 | O(N^4))
    * *Intent:* # Floating point types are used for even integer parameters. # Convert to float here to ensure consi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 960`, `args: 459`, `func_start: 442`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 228`, `dead_code: 9`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 27`
* *Architecture:* `api: 126`, `import: 19`
* *Defense:* `safety: 59`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.446
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math, scipy._lib._docscrape, scipy.integrate, scipy._external, scipy.stats, abc, scipy._lib._array_api, scipy._lib._util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy/stats/_stats_py.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.013 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.532 IQR)
- **Top Global Matches:** file_cluster_8: 12.013, file_cluster_0: 12.203, file_cluster_7: 12.217
- **Magnitude:** 7508.52 | **LOC:** 11252 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 79.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (13.2169%), Tech Debt (32.7743%)
**Top Internal Functions/Classes:**
  * `_kendalltau` (Impact: 4335.0 | O(N^6) | DB: 8)
    * *Intent:* # no range given, so use values in `a`
  * `_f_oneway_is_too_small` (Impact: 2153.4 | O(2^N) | DB: 12)
  * `hmean` (Impact: 191.7 | O(N^6))
  * `iqr` (Impact: 145.0 | O(2^N))
    * *Intent:* # Calculate variance of sample, warning if precision is lost xp = array_namespace(x) if xp is None e...
  * `kendalltau` (Impact: 96.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 904`, `structural_boundaries: 450`, `args: 196`, `func_start: 158`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 54`, `dead_code: 11`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 100`, `import: 29`
* *Defense:* `safety: 32`, `doc: 176`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.383
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` math, scipy.special, ._stats, ._resampling, scipy._external.array_api_extra, scipy.stats._quantile, warnings, scipy._lib._util...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `scipy/stats/tests/test_stats.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.174 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.548 IQR)
- **Top Global Matches:** file_cluster_8: 12.174, file_cluster_0: 12.308, file_cluster_7: 12.539
- **Magnitude:** 6911.36 | **LOC:** 9891 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 82.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (5.05%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_input_validation_edge_cases` (Impact: 5118.6 | O(N^6) | DB: 28)
  * `test_near_constant_input` (Impact: 439.9 | O(N^6) | DB: 2)
  * `test_alternative_nan_policy` (Impact: 31.7 | O(N^6))
  * `test_resampling_exact_2x2` (Impact: 31.0 | O(N^6))
    * *Intent:* # Compare against R fisher.exact # options(digits=16) # c(1, 2, 2, 1, 1, 0, 1), # c(2, 0, 0, 2, 3, 0...
  * `test_tmin_tmax_nanpolicy` (Impact: 22.9 | O(N^3))
    * *Intent:* # check that if a full slice is masked, the output returns a
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 865`, `structural_boundaries: 909`, `args: 643`, `func_start: 640`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 31`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 90`
* *Architecture:* `io: 4`, `api: 704`, `import: 28`
* *Defense:* `safety: 149`, `doc: 56`, `test: 1142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` math, numpy.testing, random, mpmath, scipy._lib._array_api_no_0d, pytest, scipy._external.array_api_extra, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/linalg/src/_matfuncs_expm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.573 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.552 IQR)
- **Top Global Matches:** file_cluster_8: 15.573, file_cluster_11: 15.816, file_cluster_13: 15.825
- **Magnitude:** 6657.44 | **LOC:** 2912 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 157
- **Risk Profile:** Cognitive Load (72.7583%), Tech Debt (9.1962%)
**Top Internal Functions/Classes:**
  * `pick_pade_structure_s` (Impact: 279.1 | O(N^4) | DB: 114)
    * *Intent:* /*******************************************************************************
  * `pick_pade_structure_d` (Impact: 279.1 | O(N^4) | DB: 114)
  * `pade_UV_calc_d` (Impact: 231.3 | O(N^5) | DB: 98)
  * `pade_UV_calc_s` (Impact: 231.1 | O(N^5) | DB: 98)
  * `pade_UV_calc_c` (Impact: 209.2 | O(N^6) | DB: 157)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 122`, `args: 22`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3836`, `orphaned_logic: 4`
* *Architecture:* `api: 294`, `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 68`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _common_array_utils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/src/lsoda.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.579 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.795 IQR)
- **Top Global Matches:** file_cluster_11: 16.579, file_cluster_13: 16.64, file_cluster_0: 16.689
- **Magnitude:** 6125.54 | **LOC:** 2322 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 355
- **Risk Profile:** Cognitive Load (48.1368%), Tech Debt (8.5913%)
**Top Internal Functions/Classes:**
  * `stoda` (Impact: 1363.6 | O(N^6) | DB: 209)
    * *Intent:* // 350
  * `lsoda` (Impact: 854.7 | O(N^6) | DB: 355)
  * `stoda_corrector_loop` (Impact: 415.6 | O(N^5) | DB: 52)
  * `prja` (Impact: 322.3 | O(N^5) | DB: 89)
  * `intdy` (Impact: 101.2 | O(N^4) | DB: 27)
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

### `scipy/integrate/__quadpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.979 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_11: 15.979, file_cluster_8: 16.021, file_cluster_0: 16.077
- **Magnitude:** 5342.58 | **LOC:** 6857 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (76.3307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dqelg` (Impact: 105.4 | O(N^3) | DB: 61)
    * *Intent:* // chebyshev series expansion // standard fortran subroutine // double precision version // // param...
  * `dqpsrt` (Impact: 85.7 | O(N^3) | DB: 28)
    * *Intent:* *result = 0.0; *abserr = 0.0;
  * `dqmomo` (Impact: 68.5 | O(N^3) | DB: 42)
  * `dqwgts` (Impact: 60.0 | O(N^3) | DB: 6)
    * *Intent:* // ***author piessens,robert,appl. math. & progr. div. - k.u.leuven // de doncker,elise,appl. math. ...
  * `dqcheb` (Impact: 26.1 | O(N^2) | DB: 90)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 99`, `args: 46`, `func_start: 7`
* *Risk/State:* `state_mutation: 4725`, `dead_code: 42`
* *Architecture:* `api: 191`, `import: 2`
* *Defense:* `doc: 11`, `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __quadpack.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_distn_infrastructure.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.452 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.711 IQR)
- **Top Global Matches:** file_cluster_8: 12.452, file_cluster_13: 12.509, file_cluster_7: 12.577
- **Magnitude:** 5153.92 | **LOC:** 4272 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (23.6925%), Tech Debt (99.9954%)
**Top Internal Functions/Classes:**
  * `_reduce_func` (Impact: 2522.6 | O(2^N) | DB: 37)
  * `__init__` (Impact: 257.8 | O(2^N) | DB: 13)
  * `stats` (Impact: 221.4 | O(N^6) | DB: 4)
  * `_construct_argparser` (Impact: 191.2 | O(N^6) | DB: 4)
  * `_construct_doc` (Impact: 135.2 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 449`, `args: 180`, `func_start: 175`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 2`, `state_mutation: 222`, `dead_code: 11`, `planned_debt: 2`, `duplicate_logic: 61`
* *Architecture:* `io: 4`, `api: 98`, `import: 22`
* *Defense:* `safety: 33`, `doc: 206`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` scipy.stats._distn_infrastructure, scipy.special, scipy._external.array_api_extra, warnings, problems, scipy._lib._util, ._constants, re...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `scipy/stats/_multivariate.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.633 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.565 IQR)
- **Top Global Matches:** file_cluster_8: 11.633, file_cluster_7: 11.731, file_cluster_1: 12.014
- **Magnitude:** 4962.58 | **LOC:** 8050 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (13.7069%), Tech Debt (99.984%)
**Top Internal Functions/Classes:**
  * `_process_size` (Impact: 2923.3 | O(2^N) | DB: 48)
  * `_process_parameters` (Impact: 216.8 | O(N^5))
  * `_process_parameters` (Impact: 206.6 | O(N^6))
    * *Intent:* %(_mvn_doc_callparams_note)s """
  * `_process_parameters_psd` (Impact: 182.7 | O(N^6))
    * *Intent:* """ return self._random_state @random_state.setter def random_state(self, seed): self._random_state ...
  * `_dirichlet_check_input` (Impact: 111.2 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 667`, `args: 309`, `func_start: 309`, `class_start: 39`
* *Risk/State:* `state_mutation: 95`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 75`
* *Architecture:* `api: 205`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 9`, `doc: 432`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` math, scipy.integrate, scipy.special, ._discrete_distns, scipy._external.array_api_extra, ._qmvnt, scipy._lib._util, scipy.linalg.blas...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scipy/optimize/src/minpack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.44 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.854 IQR)
- **Top Global Matches:** file_cluster_11: 16.44, file_cluster_0: 16.569, file_cluster_13: 16.638
- **Magnitude:** 4956.76 | **LOC:** 4267 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (85.6299%), Tech Debt (8.1866%)
**Top Internal Functions/Classes:**
  * `lmpar` (Impact: 435.9 | O(N^5) | DB: 85)
  * `qrsolv` (Impact: 242.4 | O(N^6) | DB: 52)
  * `qrfac` (Impact: 218.2 | O(N^5) | DB: 47)
  * `dogleg` (Impact: 187.7 | O(N^6) | DB: 62)
  * `r1updt` (Impact: 179.7 | O(N^5) | DB: 62)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 53`, `args: 28`, `func_start: 10`
* *Risk/State:* `state_mutation: 3048`, `dead_code: 36`, `orphaned_logic: 1`
* *Architecture:* `api: 118`, `import: 3`
* *Defense:* `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` minpack.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/tests/test_base.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.093 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.333 IQR)
- **Top Global Matches:** file_cluster_8: 11.093, file_cluster_7: 11.569, file_cluster_0: 11.653
- **Magnitude:** 4826.78 | **LOC:** 5971 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (5.9412%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scalar_assign_2` (Impact: 335.6 | O(N^6) | DB: 1)
  * `with_64bit_maxval_limit` (Impact: 218.6 | O(N^6) | DB: 2)
  * `test_argmax` (Impact: 123.8 | O(N^5))
    * *Intent:* # We are only testing sparse matrices who have # implemented 'min' and 'max' because they are # the ...
  * `test_setdiag_comprehensive` (Impact: 87.5 | O(N^6))
  * `sparse_test_class` (Impact: 79.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 679`, `args: 362`, `func_start: 360`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 52`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 57`
* *Architecture:* `io: 1`, `api: 518`, `import: 24`
* *Defense:* `safety: 194`, `doc: 28`, `test: 418`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` numpy.testing, numpy.exceptions, scipy.sparse._sputils, pytest, warnings, functools, platform, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy/optimize/_nonlin.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.471 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.266 IQR)
- **Top Global Matches:** file_cluster_13: 12.471, file_cluster_8: 12.558, file_cluster_7: 12.709
- **Magnitude:** 4710.66 | **LOC:** 1658 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (39.1933%), Tech Debt (13.5995%)
**Top Internal Functions/Classes:**
  * `nonlin_solve` (Impact: 4419.8 | O(2^N) | DB: 88)
  * `_as_inexact` (Impact: 5.5 | O(N^2))
    * *Intent:* """Return `x` as an array, of either floats or complex floats"""
  * `_set_doc_class` (Impact: 5.5 | O(N^2))
  * `_safe_norm` (Impact: 5.4 | O(N^2))
  * `_set_doc` (Impact: 5.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 231`, `args: 95`, `func_start: 87`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 177`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `io: 3`, `api: 73`, `import: 16`
* *Defense:* `safety: 28`, `doc: 60`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, difflib, scipy.sparse.linalg, scipy.linalg, sys, scipy._lib._util, scipy.sparse, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy/linalg/_decomp.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.844 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.462 IQR)
- **Top Global Matches:** file_cluster_8: 9.844, file_cluster_7: 10.191, file_cluster_13: 10.236
- **Magnitude:** 4703.5 | **LOC:** 1694 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 73.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (15.3244%), Tech Debt (25.5132%)
**Top Internal Functions/Classes:**
  * `eigh` (Impact: 3782.0 | O(2^N) | DB: 6)
  * `eig` (Impact: 529.9 | O(2^N))
  * `_check_info` (Impact: 300.3 | O(2^N))
  * `_make_eigvals` (Impact: 41.1 | O(N^4))
  * `_check_format_errors_warnings` (Impact: 10.7 | O(N^2))
    * *Intent:* # XXX: find a test case to cover this mesg = ( f"Internal {routine_name} return info = {[e['lapack_i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 79`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 7`, `doc: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.809
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .lapack, scipy.linalg, scipy._lib._util, scipy.linalg._misc, ._misc, , numpy, scipy
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `scipy/signal/_signaltools.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.028 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.029 IQR)
- **Top Global Matches:** file_cluster_8: 11.028, file_cluster_7: 11.342, file_cluster_13: 11.446
- **Magnitude:** 4599.46 | **LOC:** 5343 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (10.4889%), Tech Debt (10.5715%)
**Top Internal Functions/Classes:**
  * `correlate` (Impact: 379.7 | O(2^N))
  * `envelope` (Impact: 340.0 | O(N^6) | DB: 1)
  * `oaconvolve` (Impact: 311.8 | O(N^6) | DB: 2)
  * `convolve` (Impact: 268.4 | O(2^N))
    * *Intent:* # There cannot be a useful block size if s2 is more than half of s1.
  * `lfilter` (Impact: 252.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 228`, `args: 58`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 52`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 34`, `import: 24`
* *Defense:* `safety: 12`, `doc: 100`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` math, .windows, numpy._typing, timeit, scipy.special, ._filter_design, scipy._external.array_api_extra, warnings...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy/signal/_filter_design.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.445 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.067 IQR)
- **Top Global Matches:** file_cluster_8: 10.445, file_cluster_7: 10.787, file_cluster_1: 11.043
- **Magnitude:** 4537.1 | **LOC:** 6098 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 35.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.0206%), Tech Debt (12.021%)
**Top Internal Functions/Classes:**
  * `iirfilter` (Impact: 1112.5 | O(2^N))
  * `zpk2sos` (Impact: 711.0 | O(2^N))
  * `gammatone` (Impact: 362.4 | O(2^N))
  * `freqz` (Impact: 291.1 | O(N^6))
  * `iirdesign` (Impact: 275.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 254`, `args: 83`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 8`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `api: 58`, `import: 17`
* *Defense:* `safety: 29`, `doc: 142`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.807
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math, numpy.polynomial.polynomial, scipy.special, scipy._external.array_api_extra, warnings, matplotlib.ticker, scipy._lib._util, scipy.signal...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `subprojects/qhull_r/libqhull_r/io_r.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.054 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.402 IQR)
- **Top Global Matches:** file_cluster_8: 14.054, file_cluster_0: 14.388, file_cluster_13: 14.39
- **Magnitude:** 4456.34 | **LOC:** 4129 | **CtrlFlow:** 90.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (81.0979%), Tech Debt (15.6564%)
**Top Internal Functions/Classes:**
  * `qh_readpoints` (Impact: 1231.8 | O(2^N) | DB: 105)
  * `qh_detvnorm` (Impact: 230.6 | O(2^N) | DB: 54)
  * `qh_eachvoronoi` (Impact: 118.6 | O(2^N) | DB: 19)
  * `qh_printfacetheader` (Impact: 110.3 | O(N^2) | DB: 7)
  * `qh_printfacets` (Impact: 106.1 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 67`, `args: 5`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1349`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 258`, `import: 1`
* *Defense:* `safety: 18`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/src/zvode.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.524 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.698 IQR)
- **Top Global Matches:** file_cluster_8: 15.524, file_cluster_7: 15.586, file_cluster_13: 15.642
- **Magnitude:** 4392.98 | **LOC:** 2785 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 249
- **Risk Profile:** Cognitive Load (37.4547%), Tech Debt (9.3738%)
**Top Internal Functions/Classes:**
  * `zvode` (Impact: 524.5 | O(N^6) | DB: 249)
    * *Intent:* // Up to MAXCOR corrector iterations are taken. A convergence test is // made on the r.m.s. norm of ...
  * `zvjac` (Impact: 445.4 | O(N^5) | DB: 137)
  * `zvnlsd` (Impact: 222.2 | O(N^6) | DB: 96)
    * *Intent:* // Inline DZSCAL: Multiply Jacobian by scalar -HRL1 (real scalar × complex vector) // Use scalar * c...
  * `zvhin` (Impact: 209.5 | O(N^3) | DB: 45)
  * `zvjust` (Impact: 150.8 | O(N^6) | DB: 85)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 114`, `args: 7`, `func_start: 13`
* *Risk/State:* `state_mutation: 2232`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 230`, `import: 4`
* *Defense:* `doc: 119`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zvode.h, float.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/cluster/hierarchy/_hierarchy_impl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.535 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.656 IQR)
- **Top Global Matches:** file_cluster_8: 11.535, file_cluster_0: 11.563, file_cluster_13: 11.674
- **Magnitude:** 4281.8 | **LOC:** 4233 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (15.863%), Tech Debt (8.2642%)
**Top Internal Functions/Classes:**
  * `_dendrogram_calculate_info` (Impact: 1428.2 | O(2^N) | DB: 4)
  * `_plot_dendrogram` (Impact: 548.8 | O(N^6) | DB: 1)
  * `dendrogram` (Impact: 381.5 | O(N^6))
  * `optimal_leaf_ordering` (Impact: 197.9 | O(2^N))
  * `linkage` (Impact: 182.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 176`, `args: 66`, `func_start: 66`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 79`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 55`, `import: 12`
* *Defense:* `safety: 19`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, scipy._lib._array_api, bisect, matplotlib, numpy.random, matplotlib.pylab, scipy.cluster.hierarchy, matplotlib.patches...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scipy/stats/_resampling.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.401 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.591 IQR)
- **Top Global Matches:** file_cluster_13: 11.401, file_cluster_8: 11.415, file_cluster_0: 11.429
- **Magnitude:** 4135.72 | **LOC:** 2426 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (20.9069%), Tech Debt (93.0305%)
**Top Internal Functions/Classes:**
  * `_monte_carlo_test_iv` (Impact: 3101.3 | O(2^N) | DB: 11)
  * `_bootstrap_iv` (Impact: 434.3 | O(N^6) | DB: 1)
  * `bootstrap` (Impact: 305.0 | O(N^6) | DB: 2)
  * `_bca_interval` (Impact: 101.9 | O(N^6) | DB: 2)
  * `__init__` (Impact: 14.6 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 127`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 43`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 34`, `import: 15`
* *Defense:* `safety: 25`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.731
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` warnings, inspect, math, scipy._external, scipy.stats, collections.abc, scipy._lib._array_api, scipy._lib._util...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/vode.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.349 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.82 IQR)
- **Top Global Matches:** file_cluster_8: 15.349, file_cluster_7: 15.413, file_cluster_13: 15.487
- **Magnitude:** 4128.04 | **LOC:** 2452 | **CtrlFlow:** 74.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 233
- **Risk Profile:** Cognitive Load (36.732%), Tech Debt (10.3678%)
**Top Internal Functions/Classes:**
  * `dvjac` (Impact: 568.5 | O(N^5) | DB: 117)
  * `dvode` (Impact: 494.1 | O(N^6) | DB: 233)
    * *Intent:* // Up to MAXCOR corrector iterations are taken. A convergence test is // made on the r.m.s. norm of ...
  * `dvjust` (Impact: 240.6 | O(N^6) | DB: 72)
  * `dvhin` (Impact: 175.2 | O(N^3) | DB: 43)
    * *Intent:* // Order increase
  * `dvnlsd` (Impact: 129.7 | O(N^5) | DB: 70)
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

### `scipy/ndimage/_filters.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.87 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.896 IQR)
- **Top Global Matches:** file_cluster_8: 9.87, file_cluster_7: 10.192, file_cluster_0: 10.414
- **Magnitude:** 4082.16 | **LOC:** 2447 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.588%), Tech Debt (8.5003%)
**Top Internal Functions/Classes:**
  * `correlate1d` (Impact: 1124.9 | O(2^N))
  * `_vectorized_filter_iv` (Impact: 715.5 | O(N^6))
  * `_rank_filter` (Impact: 504.2 | O(N^6))
  * `_min_or_max_filter` (Impact: 492.0 | O(N^6))
  * `generic_filter` (Impact: 378.4 | O(2^N))
    * *Intent:* """N-D Laplace filter based on approximate second derivatives. Parameters ---------- %(input)s %(out...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 118`, `args: 40`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 4`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 12`
* *Defense:* `safety: 9`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, math, numpy.lib.stride_tricks, collections.abc, scipy._lib._array_api, scipy._lib._util, scipy.ndimage, matplotlib.pyplot...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/dop.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.708 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 14.708, file_cluster_13: 14.983, file_cluster_7: 15.02
- **Magnitude:** 3991.58 | **LOC:** 1121 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 317
- **Risk Profile:** Cognitive Load (69.0162%), Tech Debt (10.7449%)
**Top Internal Functions/Classes:**
  * `dp86co` (Impact: 839.5 | O(N^5) | DB: 317)
  * `dopcor` (Impact: 714.2 | O(N^5) | DB: 155)
  * `dopri5` (Impact: 261.5 | O(N^3) | DB: 40)
  * `dopri853` (Impact: 253.9 | O(N^3) | DB: 40)
  * `hinit` (Impact: 124.1 | O(N^3) | DB: 35)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `scipy/stats/_stats.pxd` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scipy/sparse/tests/test_dok.py` (PYTHON) | Magnitude: 247.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, test: 101, structural_boundaries: 98, safety: 54
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/dgstrs.c` (C) | Magnitude: 824.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 397, pointers: 150, indent_tabs: 65, branch: 64
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/sgstrs.c` (C) | Magnitude: 824.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 397, pointers: 150, indent_tabs: 65, branch: 64
- `scipy/special/tests/test_dd.py` (PYTHON) | Magnitude: 10.16 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, encapsulation: 8, structural_boundaries: 7, test: 4
- `scipy/signal/tests/test_signaltools.py` (PYTHON) | Magnitude: 429.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3507, test: 528, structural_boundaries: 514, branch: 356

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scipy/optimize/src/nnls.c` (C) | Magnitude: 582.24 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 362, indent_spaces: 176, branch: 55, pointers: 42
- `scipy/ndimage/src/ni_interpolation.c` (C) | Magnitude: 2281.62 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1060, indent_spaces: 881, branch: 330, api: 135
- `scipy/sparse/sparsetools/dense.h` (C) | Magnitude: 134.26 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 85, indent_spaces: 31, scientific: 24, immutability_locks: 21
- `scipy/integrate/__quadpack.c` (C) | Magnitude: 5342.58 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 4725, indent_spaces: 3056, pointers: 972, branch: 680
- `scipy/integrate/src/lsoda.c` (C) | Magnitude: 6125.54 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 2537, indent_spaces: 1403, pointers: 1124, branch: 470

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scipy/stats/biasedurn/randomc.h` (CPP) | Magnitude: 7.72 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 26, reflection_metaprogramming: 20, indent_spaces: 20, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_ddrop_row.c` (C) | Magnitude: 799.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 284, indent_tabs: 111, branch: 89, pointers: 73
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/ilu_sdrop_row.c` (C) | Magnitude: 799.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 284, indent_tabs: 111, branch: 89, pointers: 73
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/read_body.hpp` (CPP) | Magnitude: 1193.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 399, state_mutation: 353, branch: 118, structural_boundaries: 108
- `scipy/special/_ellip_harm.py` (PYTHON) | Magnitude: 26.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, encapsulation: 14, indent_spaces: 9, api: 6
- `scipy/optimize/tests/test_linear_assignment.py` (PYTHON) | Magnitude: 88.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 30, test: 23, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scipy/special/cython_special.pyi` (PYTHON) | Magnitude: 15.18 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, safety_bypasses: 2, args: 1, func_start: 1
- `scipy/spatial/distance.pyi` (PYTHON) | Magnitude: 70.58 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 39, api: 33, generics: 32
- `scipy/spatial/transform/_rigid_transform.py` (PYTHON) | Magnitude: 358.82 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, encapsulation: 129, structural_boundaries: 104, doc: 66
- `scipy/special/_orthogonal.pyi` (PYTHON) | Magnitude: 136.4 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 149, encapsulation: 143, structural_boundaries: 74, generics: 72
- `scipy/signal/_short_time_fft.py` (PYTHON) | Magnitude: 1981.2 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 556, branch: 179, state_mutation: 151, structural_boundaries: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scipy/io/_harwell_boeing/hb.py` (PYTHON) | Magnitude: 777.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 315, structural_boundaries: 77, branch: 76, encapsulation: 69
- `scipy/spatial/_spherical_voronoi.py` (PYTHON) | Magnitude: 211.1 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 29, encapsulation: 25, branch: 20
- `scipy/io/matlab/tests/gen_mat5files.m` (MATLAB) | Magnitude: 34.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 6, io: 4, structural_boundaries: 3
- `scipy/special/_precompute/utils.py` (PYTHON) | Magnitude: 22.1 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, branch: 6, state_mutation: 6
- `subprojects/pyprima/pyprima/pyprima/src/pyprima/common/_nonlinear_constraints.py` (PYTHON) | Magnitude: 87.86 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, branch: 12, structural_boundaries: 10, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/read_body_threads.hpp` (CPP) | Magnitude: 115.4 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 96, indent_spaces: 85, branch: 25, structural_boundaries: 17
- `scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/write_body_threads.hpp` (CPP) | Magnitude: 33.08 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 22, indent_spaces: 18, structural_boundaries: 8, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scipy/stats/_tukeylambda_stats.py` (PYTHON) | Magnitude: 40.3 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, encapsulation: 16, structural_boundaries: 10, dead_code: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scipy/sparse/linalg/_propack/PROPACK/src/include/lanbpro.h` (C) | Magnitude: 33.5 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 86, api: 18, indent_spaces: 14, structural_boundaries: 4
- `scipy/sparse/linalg/_propack/PROPACK/src/include/common.h` (C) | Magnitude: 31.42 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 124, immutability_locks: 76, structural_boundaries: 48, api: 16
- `scipy/sparse/linalg/_propack/PROPACK/src/include/gemm_overwrite.h` (C) | Magnitude: 21.2 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 72, immutability_locks: 26, structural_boundaries: 24, api: 6
- `scipy/integrate/src/dop.h` (C) | Magnitude: 23.26 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 57, sec_high_risk_execution: 10, api: 8, structural_boundaries: 6
- `benchmarks/benchmarks/linprog_benchmark_files/__init__.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, branch: 2, api: 1, comprehensions: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scipy/odr/_odrpack.py` (PYTHON) | Magnitude: 1388.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 422, state_mutation: 222, branch: 174, structural_boundaries: 64
- `subprojects/pyprima/pyprima/pyprima/src/pyprima/cobyla/trustregion.py` (PYTHON) | Magnitude: 810.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, branch: 83, structural_boundaries: 64, sec_high_risk_execution: 35
- `scipy/special/ellint_carlson_cpp_lite/ellint_arithmetic.hh` (CPP) | Magnitude: 228.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 173, structural_boundaries: 82, indent_spaces: 78, indent_tabs: 75
- `scipy/optimize/_direct/DIRect.c` (C) | Magnitude: 324.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 142, pointers: 73, branch: 49
- `scipy/stats/_stats_pythran.py` (PYTHON) | Magnitude: 291.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 166, branch: 44, structural_boundaries: 28, encapsulation: 14

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
- `scipy/linalg/src/_batched_linalg_module.cc` -> Churn: **73.73%** | Cog Load: 78.5753% | Debt: 8.6775%
- `scipy/spatial/transform/_rotation.py` -> Churn: **71.92%** | Cog Load: 23.5792% | Debt: 54.0102%
- `scipy/linalg/src/_linalg_solve.hh` -> Churn: **68.23%** | Cog Load: 81.3926% | Debt: 20.3054%
- `scipy/stats/_continuous_distns.py` -> Churn: **67.2%** | Cog Load: 5.6901% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scipy/interpolate/src/dfitpack.c` -> **ilayn** (93.1% isolated ownership) | Magnitude: 27963.86
- `scipy/optimize/tnc/tnc.c` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 8726.74
- `scipy/stats/tests/test_stats.py` -> **Matt Haberland** (82.0% isolated ownership) | Magnitude: 6911.36
- `scipy/integrate/src/dop.c` -> **Ilhan Polat** (100.0% isolated ownership) | Magnitude: 3991.58
- `scipy/signal/tests/test_filter_design.py` -> **steppi** (83.7% isolated ownership) | Magnitude: 3440.34

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
- `benchmarks/benchmarks/special.py` -> **Severity: 2118.7** (Blast Radius: 21.187 * Doc Risk: 100.0%)
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/slu_ddefs.h` -> **Severity: 1301.2** (Blast Radius: 13.012 * Doc Risk: 100.0%)
- `scipy/sparse/linalg/_dsolve/scipy_slu_config.h` -> **Severity: 1215.7** (Blast Radius: 12.157 * Doc Risk: 100.0%)
- `scipy/sparse/linalg/_dsolve/SuperLU/SRC/slu_sdefs.h` -> **Severity: 981.2** (Blast Radius: 9.812 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
