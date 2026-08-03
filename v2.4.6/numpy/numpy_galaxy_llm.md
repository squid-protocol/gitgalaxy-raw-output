# ARCHITECTURAL_BRIEF: numpy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/numpy` |
| **Timestamp** | `2026-08-03T19:39:31.127625+00:00` |
| **Scan Duration** | `9.38s` |
| **Git Branch** | `main` |
| **Git Commit** | `5bceafeb63c6049a579d8163bd9d6b54171731a8` |
| **Git Remote** | `https://github.com/numpy/numpy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1242 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 21.0 | 5.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 25.7 | 7.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.1 | 1.7 | 0.0 |
| API Exposure | 0.0 | 19.5 | 5.6 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 42.5 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 39.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
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

- `min_scalar_type_num` (@ `numpy/_core/src/multiarray/convert_datatype.c`) -> Impact: **5883.2** | LOC: 1744
- `PyArray_NewFromDescr_int` (@ `numpy/_core/src/multiarray/ctors.c`) -> Impact: **5856.6** | LOC: 1616
  * *Intent:* /* * Assuming that the separator is the next bit in the string (file), skip it. * * Single spaces in the separator are matched to arbitrary-long seque...
- `_parse_axis_arg` (@ `numpy/_core/src/umath/ufunc_object.c`) -> Impact: **4876.1** | LOC: 1761
- `clarfb_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **4507.2** | LOC: 2304
- `tofile` (@ `numpy/ma/core.py`) -> Impact: **3017.2** | LOC: 1177
- `randint` (@ `numpy/random/mtrand.pyx`) -> Impact: **2744.4** | LOC: 1049
  * *Intent:* """ st = self._bit_generator.state if st['bit_generator'] != 'MT19937' and legacy: warnings.warn('get_state and legacy can only be used with the ' 'MT...
- `normalize` (@ `numpy/f2py/symbolic.py`) -> Impact: **2497.0** | LOC: 715
- `substitute` (@ `numpy/_build_utils/tempita/_tempita.py`) -> Impact: **2491.9** | LOC: 559
- `BigInt_Add` (@ `numpy/_core/src/multiarray/dragon4.c`) -> Impact: **2446.9** | LOC: 1493
- `scaninputline` (@ `numpy/f2py/f2py2e.py`) -> Impact: **2379.1** | LOC: 539
  * *Intent:* # outmess=sys.stdout.write show = pprint.pprint outmess = auxfuncs.outmess __usage__ =\ f"""Usage: 1) To construct extension module sources:

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `setup` (@ `benchmarks/benchmarks/bench_io.py`) -> **O(2^N) [Recursive]**
- `substitute` (@ `numpy/_build_utils/tempita/_tempita.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `numpy/_core/arrayprint.py`) -> **O(2^N) [Recursive]**
- `__new__` (@ `numpy/_core/defchararray.py`) -> **O(2^N) [Recursive]**
  * *Intent:* --------
- `einsum_path` (@ `numpy/_core/einsumfunc.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # If we still did not find any remaining contractions,
- `clip` (@ `numpy/_core/fromnumeric.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Repeat each element of an array after themselves Parameters ---------- a : array_like Input array. repeats : int or array of ints The number of re...
- `mean` (@ `numpy/_core/fromnumeric.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ x = asanyarray(x) if x.ndim < 2: raise ValueError( f"Input array must be at least 2-dimensional, but it is {x.ndim}" ) return swapaxes(x, -1, -2)
- `prod` (@ `numpy/_core/fromnumeric.py`) -> **O(2^N) [Recursive]**
- `any` (@ `numpy/_core/fromnumeric.py`) -> **O(2^N) [Recursive]**
- `all` (@ `numpy/_core/fromnumeric.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `clahqr_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> DB Complexity: **1071**
  * *Intent:* /*
- `zlahqr_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> DB Complexity: **1069**
- `zlaqr4_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> DB Complexity: **998**
- `clarfb_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> DB Complexity: **981**
- `cgesdd_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> DB Complexity: **527**
  * *Intent:* /* If INFO > 0 from CHSEQR, then quit */
- `zgesdd_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> DB Complexity: **527**
- `string_to_fixed_width_resolve_descriptor` (@ `numpy/_core/src/multiarray/stringdtype/casts.cpp`) -> DB Complexity: **465**
- `PyArray_Choose` (@ `numpy/_core/src/multiarray/item_selection.c`) -> DB Complexity: **444**
- `_parse_axis_arg` (@ `numpy/_core/src/umath/ufunc_object.c`) -> DB Complexity: **426**
- `all_strings_promoter` (@ `numpy/_core/src/umath/stringdtype_ufuncs.cpp`) -> DB Complexity: **417**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `numpy/_core/src/multiarray` | 110 | 80332.14 | 40.74% | 16.15% |
| `numpy/linalg/lapack_lite` | 13 | 54996.04 | 45.47% | 25.25% |
| `numpy/_core/tests` | 67 | 38544.2 | 6.68% | 0.0% |
| `numpy/_core/src/umath` | 37 | 31103.18 | 47.23% | 17.52% |
| `numpy/_core` | 61 | 20277.6 | 9.88% | 29.66% |
| `numpy/f2py` | 34 | 18818.53 | 11.13% | 8.5% |
| `numpy/ma` | 11 | 15003.48 | 7.21% | 32.97% |
| `numpy/_core/src/npysort` | 18 | 10564.86 | 55.31% | 35.54% |
| `numpy/_core/src/common` | 54 | 10278.72 | 36.12% | 24.5% |
| `numpy/random` | 27 | 8609.48 | 6.71% | 25.59% |

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
- `numpy/ma/tests/test_core.py` -> **232** Orphaned Functions | **10** Duplicates
- `numpy/_core/tests/test_multiarray.py` -> **215** Orphaned Functions | **20** Duplicates
- `numpy/_core/tests/test_umath.py` -> **180** Orphaned Functions | **46** Duplicates
- `numpy/_core/tests/test_numeric.py` -> **173** Orphaned Functions | **4** Duplicates
- `numpy/_core/tests/test_regression.py` -> **177** Orphaned Functions | **0** Duplicates

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

### Exploit Generation Surface
- `benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_creation.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_function_base.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `benchmarks/asv_pip_nopep517.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_import.py` -> **100.0%** Exposure
- `numpy/_build_utils/gitversion.py` -> **100.0%** Exposure
- `numpy/f2py/f2py2e.py` -> **100.0%** Exposure
- `numpy/f2py/tests/test_f2py2e.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `numpy/linalg/umath_linalg.cpp` -> **10.0%** Exposure
- `numpy/_core/src/multiarray/datetime.c` -> **10.0%** Exposure
- `numpy/_core/src/multiarray/dtype_transfer.c` -> **10.0%** Exposure
- `numpy/_core/src/multiarray/dtype_transfer.h` -> **10.0%** Exposure
- `numpy/_core/src/multiarray/dtype_traversal.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/benchmarks/__init__.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_array_coercion.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_creation.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4607` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `numpy/_core/src/common/npy_import.c` (C) -> Cumulative Risk: **839.58**
- **Archetype:** `file_cluster_4` (Distance: 12.206 IQR)
- **Magnitude:** 136.14 | **LOC:** 89 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `npy_import_entry_point` (Impact: 33.6), `npy_cache_import_runtime` (Impact: 33.2), `init_import_mutex` (Impact: 6.9)

### 2. `tools/wheels/cibw_before_build.sh` (SHELL) -> Cumulative Risk: **817.34**
- **Archetype:** `file_cluster_8` (Distance: 12.14 IQR)
- **Magnitude:** 0.06 | **LOC:** 54 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 42.8), `__global_context__` (Impact: 1.8)

### 3. `numpy/_core/src/multiarray/nditer_api.c` (C) -> Cumulative Risk: **802.68**
- **Archetype:** `file_cluster_0` (Distance: 15.156 IQR)
- **Magnitude:** 2602.12 | **LOC:** 2327 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8207%)
- **Heaviest Functions:** `npyiter_fill_buffercopy_params` (Impact: 1397.7), `NpyIter_GetInnerFixedStrideArray` (Impact: 123.0), `npyiter_coalesce_axes` (Impact: 51.2)

### 4. `numpy/_core/src/common/npy_argparse.c` (C) -> Cumulative Risk: **800.37**
- **Archetype:** `file_cluster_13` (Distance: 13.588 IQR)
- **Magnitude:** 911.4 | **LOC:** 416 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_npy_parse_arguments` (Impact: 363.5), `initialize_keywords` (Impact: 193.6), `PyArray_PythonPyIntFromInt` (Impact: 25.7)

### 5. `numpy/_core/src/npysort/quicksort.cpp` (CPP) -> Cumulative Risk: **799.48**
- **Archetype:** `file_cluster_8` (Distance: 14.184 IQR)
- **Magnitude:** 1793.76 | **LOC:** 1024 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `npy_aquicksort_impl` (Impact: 203.0), `string_quicksort_` (Impact: 158.7), `aquicksort_` (Impact: 151.8)

### 6. `numpy/_core/code_generators/genapi.py` (PYTHON) -> Cumulative Risk: **796.43**
- **Archetype:** `file_cluster_13` (Distance: 11.92 IQR)
- **Magnitude:** 690.86 | **LOC:** 560 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `find_functions` (Impact: 142.9), `check_api_dict` (Impact: 62.5), `__init__` (Impact: 51.9)

### 7. `numpy/_core/src/npysort/mergesort.cpp` (CPP) -> Cumulative Risk: **794.65**
- **Archetype:** `file_cluster_8` (Distance: 13.267 IQR)
- **Magnitude:** 1012.84 | **LOC:** 755 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `npy_mergesort0` (Impact: 143.6), `mergesort0_` (Impact: 102.2), `amergesort0_` (Impact: 85.3)

### 8. `benchmarks/benchmarks/bench_manipulate.py` (PYTHON) -> Cumulative Risk: **790.08**
- **Archetype:** `file_cluster_8` (Distance: 11.711 IQR)
- **Magnitude:** 147.18 | **LOC:** 112 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup` (Impact: 33.8), `setup` (Impact: 8.3), `setup` (Impact: 8.2)

### 9. `numpy/linalg/umath_linalg.cpp` (CPP) -> Cumulative Risk: **789.21**
- **Archetype:** `file_cluster_8` (Distance: 13.987 IQR)
- **Magnitude:** 5076.18 | **LOC:** 4812 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `svd_wrapper` (Impact: 145.3), `eig_wrapper` (Impact: 124.8), `eigh_wrapper` (Impact: 88.9)

### 10. `numpy/_core/src/npysort/radixsort.cpp` (CPP) -> Cumulative Risk: **786.95**
- **Archetype:** `file_cluster_8` (Distance: 13.427 IQR)
- **Magnitude:** 490.98 | **LOC:** 357 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.2618%)
- **Heaviest Functions:** `aradixsort0` (Impact: 42.5), `radixsort0` (Impact: 38.2), `aradixsort_` (Impact: 34.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `numpy/linalg/lapack_lite/f2c_c_lapack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.931 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.139 IQR)
- **Top Global Matches:** file_cluster_8: 15.931, file_cluster_7: 16.228, file_cluster_13: 16.276
- **Magnitude:** 21896.28 | **LOC:** 29862 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1071
- **Risk Profile:** Cognitive Load (69.1508%), Tech Debt (8.7195%)
**Top Internal Functions/Classes:**
  * `clarfb_` (Impact: 4507.2 | O(2^N) | DB: 981)
  * `cgehd2_` (Impact: 1302.4 | O(2^N) | DB: 375)
  * `cgesdd_` (Impact: 1108.0 | O(N^2) | DB: 527)
    * *Intent:* /* If INFO > 0 from CHSEQR, then quit */
  * `cunml2_` (Impact: 945.9 | O(2^N) | DB: 200)
  * `clahqr_` (Impact: 893.0 | O(2^N) | DB: 1071)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 147`, `args: 175`, `func_start: 47`
* *Risk/State:* `state_mutation: 11299`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 415`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` f2c.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_z_lapack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.904 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.132 IQR)
- **Top Global Matches:** file_cluster_8: 15.904, file_cluster_7: 16.204, file_cluster_13: 16.252
- **Magnitude:** 20104.76 | **LOC:** 29997 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1069
- **Risk Profile:** Cognitive Load (68.9803%), Tech Debt (8.858%)
**Top Internal Functions/Classes:**
  * `zlahqr_` (Impact: 1869.7 | O(2^N) | DB: 1069)
  * `zlaqr4_` (Impact: 1408.8 | O(N^2) | DB: 998)
  * `zgehd2_` (Impact: 1303.1 | O(2^N) | DB: 375)
  * `zgesdd_` (Impact: 1108.6 | O(N^2) | DB: 527)
  * `zunml2_` (Impact: 946.0 | O(2^N) | DB: 200)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 147`, `args: 165`, `func_start: 47`
* *Risk/State:* `state_mutation: 11299`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 434`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` f2c.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/ufunc_object.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.752 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.704 IQR)
- **Top Global Matches:** file_cluster_8: 14.752, file_cluster_13: 14.818, file_cluster_11: 14.834
- **Magnitude:** 10376.46 | **LOC:** 6804 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 426
- **Risk Profile:** Cognitive Load (93.4463%), Tech Debt (14.534%)
**Top Internal Functions/Classes:**
  * `_parse_axis_arg` (Impact: 4876.1 | O(2^N) | DB: 426)
  * `ufunc_at` (Impact: 981.1 | O(2^N) | DB: 96)
  * `ufunc_generic_fastcall` (Impact: 500.1 | O(N^6) | DB: 53)
  * `convert_ufunc_arguments` (Impact: 372.3 | O(N^6) | DB: 88)
  * `_get_fixed_signature` (Impact: 150.2 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 851`, `structural_boundaries: 216`, `args: 6`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 2356`, `dead_code: 3`, `planned_debt: 16`, `orphaned_logic: 8`
* *Architecture:* `api: 680`, `import: 34`
* *Defense:* `safety: 15`, `doc: 15`, `test: 13`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` conversion_utils.h, npy_pycompat.h, npy_hashtable.h, lowlevel_strided_loops.h, scalartypes.h, ufuncobject.h, ctors.h, arrayscalars.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/ma/core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.892 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 12.892, file_cluster_7: 12.985, file_cluster_13: 13.061
- **Magnitude:** 9960.0 | **LOC:** 8995 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 22.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (27.3977%), Tech Debt (62.7219%)
**Top Internal Functions/Classes:**
  * `tofile` (Impact: 3017.2 | O(2^N) | DB: 14)
  * `_check_fill_value` (Impact: 893.2 | O(N^6) | DB: 19)
  * `__new__` (Impact: 637.8 | O(N^6))
  * `var` (Impact: 379.3 | O(2^N))
    * *Intent:* # Case 1. : no mask in input. # Erase the current mask ? # With a reduced version if shrink: _data._...
  * `__getitem__` (Impact: 309.0 | O(2^N))
    * *Intent:* # Bas les masques !
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 773`, `args: 269`, `func_start: 268`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 204`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 20`
* *Architecture:* `api: 187`, `import: 16`
* *Defense:* `safety: 177`, `doc: 410`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` operator, numpy._core.numerictypes, inspect, numpy.ma, times., problems, warnings, builtins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_blas.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_8: 15.653, file_cluster_7: 15.987, file_cluster_13: 15.99
- **Magnitude:** 9488.12 | **LOC:** 21604 | **CtrlFlow:** 91.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 129
- **Risk Profile:** Cognitive Load (79.3568%), Tech Debt (16.7056%)
**Top Internal Functions/Classes:**
  * `ssyr2k_` (Impact: 418.2 | O(N^2) | DB: 129)
  * `dsyr2k_` (Impact: 418.1 | O(N^2) | DB: 129)
  * `dsymv_` (Impact: 165.4 | O(N^1) | DB: 109)
    * *Intent:* /* Form C := alpha*conjg( A' )*conjg( B' ) + beta*C. */
  * `ssymv_` (Impact: 165.4 | O(N^1) | DB: 109)
  * `dsyr2_` (Impact: 146.9 | O(N^1) | DB: 73)
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

### `numpy/_core/src/multiarray/convert_datatype.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.089 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.057 IQR)
- **Top Global Matches:** file_cluster_8: 14.089, file_cluster_13: 14.091, file_cluster_11: 14.253
- **Magnitude:** 7767.8 | **LOC:** 3582 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 341
- **Risk Profile:** Cognitive Load (85.8726%), Tech Debt (14.338%)
**Top Internal Functions/Classes:**
  * `min_scalar_type_num` (Impact: 5883.2 | O(2^N) | DB: 341)
  * `ensure_castingimpl_exists` (Impact: 40.4 | O(N^6) | DB: 6)
  * `void_to_void_get_loop` (Impact: 27.1 | O(N^4) | DB: 1)
  * `initialize_void_and_object_globals` (Impact: 24.6 | O(N^5) | DB: 36)
  * `PyArray_GetCastingImpl` (Impact: 22.0 | O(N^6) | DB: 2)
    * *Intent:* /* Create a cast using the state of the legacy casting setup defined * during the setup of the DType...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 220`, `args: 17`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1200`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 479`, `import: 30`
* *Defense:* `safety: 11`, `doc: 23`, `test: 11`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` npy_math.h, scalartypes.h, npy_pycompat.h, lowlevel_strided_loops.h, ctors.h, arrayscalars.h, arrayobject.h, convert_datatype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/ctors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.935 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.312 IQR)
- **Top Global Matches:** file_cluster_13: 13.935, file_cluster_8: 13.971, file_cluster_11: 14.057
- **Magnitude:** 7060.66 | **LOC:** 4208 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 261
- **Risk Profile:** Cognitive Load (95.651%), Tech Debt (11.9806%)
**Top Internal Functions/Classes:**
  * `PyArray_NewFromDescr_int` (Impact: 5856.6 | O(2^N) | DB: 261)
    * *Intent:* /* * Assuming that the separator is the next bit in the string (file), skip it. * * Single spaces in...
  * `fromstr_next_element` (Impact: 41.3 | O(N^5) | DB: 4)
    * *Intent:* * so the semantics for fromstring and fromfile are the same, especially with * regards to the handli...
  * `swab_separator` (Impact: 12.9 | O(N^2) | DB: 6)
  * `string_is_fully_read` (Impact: 8.2 | O(N^2) | DB: 1)
    * *Intent:* /* * Reading from a file or a string. * * As much as possible, we try to use the same code for both ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 145`, `args: 9`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 823`, `dead_code: 3`, `planned_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 289`, `import: 29`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` npy_math.h, npy_pycompat.h, lowlevel_strided_loops.h, ctors.h, arrayscalars.h, refcount.h, arrayobject.h, convert_datatype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/item_selection.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.536 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.351 IQR)
- **Top Global Matches:** file_cluster_8: 14.536, file_cluster_13: 14.599, file_cluster_11: 14.653
- **Magnitude:** 5849.72 | **LOC:** 3377 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 444
- **Risk Profile:** Cognitive Load (83.5518%), Tech Debt (10.8571%)
**Top Internal Functions/Classes:**
  * `PyArray_Choose` (Impact: 1899.0 | O(N^6) | DB: 444)
  * `npy_fasttake_impl` (Impact: 548.7 | O(N^6) | DB: 34)
    * *Intent:* #include "ctors.h" #include "lowlevel_strided_loops.h" #include "array_assign.h" #include "refcount....
  * `PyArray_PutTo` (Impact: 255.9 | O(N^6) | DB: 55)
  * `PyArray_TakeFrom` (Impact: 126.1 | O(N^6) | DB: 36)
  * `PyArray_PutMask` (Impact: 101.0 | O(N^6) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 120`, `args: 11`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1889`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 540`, `import: 25`
* *Defense:* `safety: 3`, `test: 3`, `immutability_locks: 59`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` simd.h, npy_math.h, lowlevel_strided_loops.h, ctors.h, arrayscalars.h, refcount.h, arrayobject.h, array_assign.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/umath_linalg.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.987 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.659 IQR)
- **Top Global Matches:** file_cluster_8: 13.987, file_cluster_13: 14.342, file_cluster_11: 14.357
- **Magnitude:** 5076.18 | **LOC:** 4812 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (88.6898%), Tech Debt (99.5834%)
**Top Internal Functions/Classes:**
  * `svd_wrapper` (Impact: 145.3 | O(N^6) | DB: 40)
  * `eig_wrapper` (Impact: 124.8 | O(N^6) | DB: 42)
  * `eigh_wrapper` (Impact: 88.9 | O(N^6) | DB: 25)
  * `init_gesdd` (Impact: 86.3 | O(N^5) | DB: 50)
  * `compute_urows_vtcolumns` (Impact: 78.6 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 616`, `args: 133`, `func_start: 151`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 30`, `state_mutation: 2713`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 78`, `orphaned_logic: 9`
* *Architecture:* `import: 14`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 146`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cstdio, npy_math.h, cassert, ufuncobject.h, libunwind.h, cmath, utility, arrayobject.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/f2py/symbolic.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.571 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.618 IQR)
- **Top Global Matches:** file_cluster_8: 11.571, file_cluster_7: 11.86, file_cluster_17: 11.949
- **Magnitude:** 5060.4 | **LOC:** 1519 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (21.6741%), Tech Debt (26.3708%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 2497.0 | O(2^N) | DB: 10)
  * `tostring` (Impact: 959.2 | O(2^N) | DB: 5)
  * `substitute` (Impact: 403.7 | O(2^N))
    * *Intent:* # In Fortran, parenthesis () are use for both function call as # # TODO: implement a method for deci...
  * `traverse` (Impact: 346.8 | O(2^N))
  * `__init__` (Impact: 153.2 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 350`, `args: 78`, `func_start: 78`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 11`, `duplicate_logic: 2`
* *Architecture:* `api: 80`, `import: 4`
* *Defense:* `safety: 108`, `doc: 76`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, math, enum, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/stringdtype_ufuncs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.553 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.359 IQR)
- **Top Global Matches:** file_cluster_8: 14.553, file_cluster_13: 14.776, file_cluster_11: 14.927
- **Magnitude:** 4554.48 | **LOC:** 3133 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 417
- **Risk Profile:** Cognitive Load (89.2775%), Tech Debt (8.2245%)
**Top Internal Functions/Classes:**
  * `all_strings_promoter` (Impact: 1516.4 | O(2^N) | DB: 417)
  * `add_strided_loop` (Impact: 245.4 | O(N^6) | DB: 33)
  * `string_comparison_strided_loop` (Impact: 201.7 | O(N^6) | DB: 41)
  * `multiply_loop_core` (Impact: 175.2 | O(N^6) | DB: 33)
  * `string_startswith_endswith_strided_loop` (Impact: 124.2 | O(N^6) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 124`, `args: 124`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 5`, `state_mutation: 1661`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `import: 19`
* *Defense:* `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` npy_math.h, ufuncobject.h, dtype.h, arrayobject.h, utf8_utils.h, Python.h, abstractdtypes.h, templ_common.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/testing/_private/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.731 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_13: 12.731, file_cluster_8: 13.047, file_cluster_0: 13.085
- **Magnitude:** 4321.22 | **LOC:** 2868 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (14.2222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_array_almost_equal` (Impact: 1693.0 | O(N^6) | DB: 85)
  * `assert_array_compare` (Impact: 903.2 | O(N^6) | DB: 7)
  * `assert_equal` (Impact: 690.8 | O(2^N))
  * `assert_almost_equal` (Impact: 570.9 | O(2^N))
  * `build_err_msg` (Impact: 80.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 282`, `args: 80`, `func_start: 77`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 145`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 26`, `api: 60`, `concurrency: 8`, `import: 57`
* *Defense:* `safety: 97`, `doc: 96`, `test: 20`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` os, numpy.testing, tempfile, operator, numpy._core.numerictypes, inspect, to, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_umath.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.118 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.566 IQR)
- **Top Global Matches:** file_cluster_8: 11.118, file_cluster_0: 11.451, file_cluster_7: 11.582
- **Magnitude:** 4210.64 | **LOC:** 5150 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.8087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_against_cmath` (Impact: 576.8 | O(N^6) | DB: 9)
  * `test_division_int_boundary` (Impact: 198.8 | O(N^6))
    * *Intent:* # divisors # scalar divisors "range(fo.min, fo.min + 15)" ), ( # dividend "np.array(range(fo.max-lsi...
  * `test_ufunc_override_with_super` (Impact: 160.2 | O(N^6) | DB: 6)
  * `test_out_wrap_subok` (Impact: 94.6 | O(N^4))
  * `test_division_int_reduce` (Impact: 92.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 675`, `args: 374`, `func_start: 343`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 34`, `dead_code: 4`, `fragile_debt: 10`, `duplicate_logic: 46`, `orphaned_logic: 180`
* *Architecture:* `io: 9`, `api: 361`, `import: 20`
* *Defense:* `safety: 118`, `doc: 24`, `test: 488`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy._core.umath, platform, pytest, itertools, warnings, cmath, numpy.testing, fnmatch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dragon4.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.338 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.433 IQR)
- **Top Global Matches:** file_cluster_8: 14.338, file_cluster_13: 14.394, file_cluster_11: 14.4
- **Magnitude:** 3869.34 | **LOC:** 3215 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 380
- **Risk Profile:** Cognitive Load (90.9527%), Tech Debt (9.8104%)
**Top Internal Functions/Classes:**
  * `BigInt_Add` (Impact: 2446.9 | O(N^6) | DB: 380)
  * `BigInt_Set_2x_uint64` (Impact: 29.6 | O(N^3) | DB: 9)
    * *Intent:* /* * Dummy implementation of a memory manager for BigInts. Currently, only * supports a single call ...
  * `BigInt_Compare` (Impact: 17.4 | O(N^3) | DB: 3)
  * `BigInt_Set_uint64` (Impact: 8.3 | O(N^2) | DB: 6)
    * *Intent:* #endif /* HAVE_LDOUBLE_IEEE_QUAD_LE */ /*
  * `LogBase2_32` (Impact: 8.1 | O(N^2) | DB: 4)
    * *Intent:* * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING * FROM, OUT OF OR IN CONNE...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 78`, `args: 3`, `func_start: 32`, `class_start: 8`
* *Risk/State:* `state_mutation: 1043`, `dead_code: 12`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 269`, `import: 6`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, string.h, math.h, npy_common.h, stdio.h, dragon4.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/npysort/timsort.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.114 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.393 IQR)
- **Top Global Matches:** file_cluster_8: 14.114, file_cluster_13: 14.435, file_cluster_11: 14.436
- **Magnitude:** 3669.22 | **LOC:** 2927 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (72.7587%), Tech Debt (99.7065%)
**Top Internal Functions/Classes:**
  * `npy_try_collapse` (Impact: 161.3 | O(N^6) | DB: 21)
  * `npy_count_run` (Impact: 115.5 | O(N^4) | DB: 23)
  * `try_collapse_` (Impact: 110.1 | O(N^5) | DB: 21)
  * `acount_run_` (Impact: 102.4 | O(N^4) | DB: 28)
  * `count_run_` (Impact: 102.2 | O(N^4) | DB: 23)
    * *Intent:* /* For string sorts and generic sort, element comparisons are very expensive, * and the time cost of...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 351`, `args: 132`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 94`, `high_risk_execution: 16`, `state_mutation: 1513`, `planned_debt: 1`, `duplicate_logic: 16`, `orphaned_logic: 49`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` numpy_tag.h, utility, npysort_common.h, cstdlib, npy_sort.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_multiarray.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.063 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.812 IQR)
- **Top Global Matches:** file_cluster_8: 12.063, file_cluster_0: 12.365, file_cluster_7: 12.513
- **Magnitude:** 3622.58 | **LOC:** 11172 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 11.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (4.7933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ufunc_binop_interaction` (Impact: 221.2 | O(N^6) | DB: 1)
  * `test_argsort` (Impact: 146.5 | O(N^6))
  * `test_partition` (Impact: 93.4 | O(N^6))
    * *Intent:* # check axis handling for multidimensional empty arrays
  * `test_put` (Impact: 44.9 | O(N^6))
    * *Intent:* # The class would need to overwrite trace to ensure single-element # output also has the right subcl...
  * `test_set_stridesattr` (Impact: 44.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 1512`, `args: 839`, `func_start: 826`, `class_start: 148`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 8`, `state_mutation: 73`, `dead_code: 10`, `planned_debt: 4`, `fragile_debt: 10`, `duplicate_logic: 20`, `orphaned_logic: 215`
* *Architecture:* `io: 80`, `api: 871`, `import: 53`
* *Defense:* `safety: 312`, `doc: 40`, `test: 1188`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` os, itertools, numpy.testing, numpy._core.arrayprint, tempfile, operator, inspect, numpy.lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_numeric.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.17 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.524 IQR)
- **Top Global Matches:** file_cluster_8: 11.17, file_cluster_0: 11.484, file_cluster_7: 11.526
- **Magnitude:** 3521.38 | **LOC:** 4264 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (4.2834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tst_none_isclose` (Impact: 1666.8 | O(2^N) | DB: 30)
  * `test_count_nonzero_axis_all_dtypes` (Impact: 95.9 | O(N^6))
  * `test_floating_exceptions` (Impact: 63.9 | O(N^6) | DB: 6)
    * *Intent:* # Test for all real and complex float types
  * `test_promote_types_metadata` (Impact: 52.0 | O(N^4))
    * *Intent:* """Metadata handling in promotion does not appear formalized right now in NumPy. This test should th...
  * `test_clip_min_max_args` (Impact: 43.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 614`, `args: 324`, `func_start: 309`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `dead_code: 4`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 173`
* *Architecture:* `io: 11`, `api: 334`, `import: 21`
* *Defense:* `safety: 150`, `doc: 14`, `test: 462`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` itertools, numpy.testing, numpy._core.numerictypes, inspect, pytest, math, warnings, numbers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/methods.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.447 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.95 IQR)
- **Top Global Matches:** file_cluster_8: 13.447, file_cluster_13: 13.519, file_cluster_0: 13.718
- **Magnitude:** 3391.12 | **LOC:** 3063 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (67.7938%), Tech Debt (9.4001%)
**Top Internal Functions/Classes:**
  * `array_reduce_ex` (Impact: 925.5 | O(2^N) | DB: 105)
  * `_deepcopy_call` (Impact: 225.3 | O(2^N) | DB: 5)
  * `array_reduce_ex_picklebuffer` (Impact: 75.4 | O(N^6) | DB: 24)
  * `PyArray_GetField` (Impact: 73.3 | O(2^N) | DB: 5)
  * `array_deepcopy` (Impact: 67.3 | O(N^6) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 232`, `args: 1`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 941`, `dead_code: 7`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 473`, `import: 32`
* *Defense:* `safety: 2`, `test: 2`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` conversion_utils.h, npy_pycompat.h, ctors.h, arrayscalars.h, arrayobject.h, ufunc_override.h, convert_datatype.h, array_assign.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_build_utils/tempita/_tempita.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.243 IQR)
- **Top Global Matches:** file_cluster_8: 11.407, file_cluster_13: 11.674, file_cluster_17: 11.771
- **Magnitude:** 3320.46 | **LOC:** 1117 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (55.1343%), Tech Debt (13.272%)
**Top Internal Functions/Classes:**
  * `substitute` (Impact: 2491.9 | O(2^N) | DB: 22)
  * `parse_default` (Impact: 459.6 | O(N^6) | DB: 31)
  * `parse_for` (Impact: 77.3 | O(N^3) | DB: 1)
    * *Intent:* """ # noqa: E501 if delimiters is None: delimiters = ( Template.default_namespace["start_braces"], T...
  * `parse_one_cond` (Impact: 77.2 | O(N^3) | DB: 1)
  * `parse_cond` (Impact: 24.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 188`, `args: 57`, `func_start: 57`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 103`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 28`, `import: 10`
* *Defense:* `safety: 50`, `doc: 14`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000762
  * `Imports (Out-Degree: 1):` os, pkg_resources, re, ._looper, io, sys, tokenize, optparse
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy/_core/src/multiarray/stringdtype/casts.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.946 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.201 IQR)
- **Top Global Matches:** file_cluster_8: 13.946, file_cluster_13: 14.082, file_cluster_11: 14.223
- **Magnitude:** 3301.26 | **LOC:** 2371 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 465
- **Risk Profile:** Cognitive Load (75.3415%), Tech Debt (10.4147%)
**Top Internal Functions/Classes:**
  * `string_to_fixed_width_resolve_descriptor` (Impact: 1925.8 | O(2^N) | DB: 465)
  * `typenum_to_cstr` (Impact: 110.5 | O(N^3))
  * `string_to_string` (Impact: 97.1 | O(N^6) | DB: 23)
  * `unicode_to_string` (Impact: 63.5 | O(N^6) | DB: 26)
  * `string_to_string_resolve_descriptors` (Impact: 38.0 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 151`, `args: 107`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 8`, `state_mutation: 1008`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` npy_math.h, dtype.h, ufuncobject.h, casts.h, arrayobject.h, common.h, umathmodule.h, Python.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/random/_generator.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.834 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.363 IQR)
- **Top Global Matches:** file_cluster_8: 10.834, file_cluster_7: 10.976, file_cluster_13: 11.169
- **Magnitude:** 3267.22 | **LOC:** 5087 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 46.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.3685%), Tech Debt (8.2873%)
**Top Internal Functions/Classes:**
  * `standard_gamma` (Impact: 1645.1 | O(N^6) | DB: 1)
  * `integers` (Impact: 1402.6 | O(2^N))
  * `random` (Impact: 76.0 | O(N^5))
  * `spawn` (Impact: 21.1 | O(2^N))
  * `__init__` (Impact: 12.6 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 170`, `args: 52`, `func_start: 52`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`, `dead_code: 8`, `planned_debt: 1`
* *Architecture:* `api: 53`, `import: 10`
* *Defense:* `safety: 26`, `doc: 102`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` matplotlib.pyplot, scipy, warnings, numpy.lib.array_utils, numpy.random, numpy.linalg, operator, ._pcg64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/descriptor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.604 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.43 IQR)
- **Top Global Matches:** file_cluster_8: 13.604, file_cluster_13: 13.667, file_cluster_11: 13.733
- **Magnitude:** 3251.4 | **LOC:** 3868 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 243
- **Risk Profile:** Cognitive Load (80.2639%), Tech Debt (15.6769%)
**Top Internal Functions/Classes:**
  * `_try_convert_from_inherit_tuple` (Impact: 1170.0 | O(N^6) | DB: 243)
  * `_convert_from_array_descr` (Impact: 247.4 | O(N^6) | DB: 33)
  * `_convert_from_tuple` (Impact: 139.9 | O(N^6) | DB: 25)
  * `_check_for_commastring` (Impact: 121.7 | O(N^5) | DB: 5)
    * *Intent:* /* * Sets the global typeDict object, which is a dictionary mapping * dtype names to numpy scalar ty...
  * `_convert_from_list` (Impact: 64.8 | O(N^4) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 201`, `args: 2`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 975`, `dead_code: 9`, `planned_debt: 6`, `orphaned_logic: 8`
* *Architecture:* `api: 368`, `import: 23`
* *Defense:* `safety: 2`, `doc: 2`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` npy_math.h, conversion_utils.h, npy_pycompat.h, arrayscalars.h, dtype.h, arrayobject.h, common.h, structmember.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/random/mtrand.pyx` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.376 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.37 IQR)
- **Top Global Matches:** file_cluster_8: 10.376, file_cluster_7: 10.596, file_cluster_13: 10.906
- **Magnitude:** 3188.56 | **LOC:** 4977 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.5967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `randint` (Impact: 2744.4 | O(2^N) | DB: 1)
    * *Intent:* """ st = self._bit_generator.state if st['bit_generator'] != 'MT19937' and legacy: warnings.warn('ge...
  * `set_state` (Impact: 146.8 | O(2^N))
    * *Intent:* # The third argument containing the state is required here since # RandomState contains state inform...
  * `get_state` (Impact: 110.2 | O(2^N))
  * `tomaxint` (Impact: 22.6 | O(N^4))
  * `seed` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 161`, `args: 62`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `dead_code: 5`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* `safety: 21`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` matplotlib.pyplot, scipy, warnings, numpy.random, numpy.linalg, operator, scipy.special, ._mt19937...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dtype_transfer.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.017 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.685 IQR)
- **Top Global Matches:** file_cluster_8: 14.017, file_cluster_13: 14.118, file_cluster_7: 14.275
- **Magnitude:** 3137.82 | **LOC:** 3835 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (61.8159%), Tech Debt (27.5523%)
**Top Internal Functions/Classes:**
  * `PyArray_PrepareThreeRawArrayIter` (Impact: 280.5 | O(N^6) | DB: 71)
  * `PyArray_PrepareOneRawArrayIter` (Impact: 182.9 | O(N^6) | DB: 41)
  * `get_subarray_transfer_function` (Impact: 136.8 | O(N^6) | DB: 9)
  * `get_n_to_n_transfer_function` (Impact: 118.8 | O(N^6) | DB: 12)
    * *Intent:* /* * The metadata for when dealing with Months or Years * which behave non-linearly with respect to ...
  * `PyArray_GetStridedZeroPadCopyFn` (Impact: 95.8 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 161`, `args: 9`, `func_start: 31`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 1294`, `planned_debt: 5`, `fragile_debt: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 475`, `import: 19`
* *Defense:* `safety: 6`, `doc: 11`, `test: 5`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` npy_math.h, lowlevel_strided_loops.h, ctors.h, arrayobject.h, convert_datatype.h, array_assign.h, structmember.h, umathmodule.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/multiarraymodule.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.084 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.614 IQR)
- **Top Global Matches:** file_cluster_8: 14.084, file_cluster_13: 14.123, file_cluster_11: 14.338
- **Magnitude:** 2855.48 | **LOC:** 5317 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 27.8%
- **Algorithmic:** O(N^6) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (77.5395%), Tech Debt (18.1356%)
**Top Internal Functions/Classes:**
  * `_multiarray_umath_exec` (Impact: 227.5 | O(N^6) | DB: 28)
    * *Intent:* *str_obj = NULL;
  * `PyArray_Where` (Impact: 221.3 | O(N^6) | DB: 55)
  * `PyArray_AsCArray` (Impact: 99.9 | O(N^6) | DB: 19)
  * `einsum_list_to_subscripts` (Impact: 81.2 | O(N^6) | DB: 24)
  * `einsum_sub_op_from_lists` (Impact: 70.5 | O(N^6) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 261`, `args: 12`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1295`, `dead_code: 2`, `planned_debt: 4`, `orphaned_logic: 15`
* *Architecture:* `api: 495`, `import: 61`
* *Defense:* `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` npy_math.h, scalartypes.h, npy_pycompat.h, conversion_utils.h, lowlevel_strided_loops.h, ctors.h, arrayscalars.h, dtype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `numpy/random/_bounded_integers.pyi` (PYTHON) | **Drift Ratio: 1.52x**
  * **Global Archetype:** `file_cluster_16` (Drift: 5.417 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 8.222 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `numpy/_core/tests/test_errstate.py` (PYTHON) | Magnitude: 144.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 39, test: 28, branch: 22
- `numpy/tests/test_configtool.py` (PYTHON) | Magnitude: 22.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 20, test: 16, import: 9
- `numpy/_core/src/multiarray/nditer_api.c` (C) | Magnitude: 2602.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 652, indent_spaces: 580, api: 178, pointers: 135
- `numpy/_core/tests/test_casting_unittests.py` (PYTHON) | Magnitude: 122.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 626, structural_boundaries: 206, test: 180, branch: 131
- `numpy/random/tests/test_extending.py` (PYTHON) | Magnitude: 71.76 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 41, branch: 19, import: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `numpy/_core/src/npymath/ieee754.cpp` (CPP) | Magnitude: 713.26 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 276, state_mutation: 259, branch: 88, structural_boundaries: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `numpy/_core/src/umath/fast_loop_macros.h` (C) | Magnitude: 358.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 299, indent_spaces: 192, branch: 91, api: 51
- `tools/rebase_installed_dlls_cygwin.sh` (SHELL) | Magnitude: 0.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, state_mutation: 2, args: 1, orphaned_logic: 1
- `numpy/_core/src/multiarray/nditer_impl.h` (C) | Magnitude: 73.94 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 106, macros: 88, reflection_metaprogramming: 62, pointers: 44
- `numpy/_core/src/common/npdef.hpp` (CPP) | Magnitude: 18.32 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 15, branch: 6, doc: 5, reflection_metaprogramming: 5
- `tools/list_numpy_dlls.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, io: 5, reflection_metaprogramming: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `numpy/_pyinstaller/tests/test_pyinstaller.py` (PYTHON) | Magnitude: 10.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, test: 8, structural_boundaries: 6, explicit_casts: 5
- `numpy/_core/src/npysort/binsearch.cpp` (CPP) | Magnitude: 684.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 321, indent_spaces: 228, structural_boundaries: 81, immutability_locks: 49
- `numpy/f2py/tests/test_callback.py` (PYTHON) | Magnitude: 153.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 81, test: 46, safety: 35
- `numpy/_core/src/common/npy_cpu_dispatch.c` (C) | Magnitude: 123.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 39, structural_boundaries: 14, branch: 13
- `tools/swig/test/ArrayZ.h` (CPP) | Magnitude: 0.03 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 10, immutability_locks: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `numpy/_typing/_ufunc.pyi` (PYTHON) | Magnitude: 258.72 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 853, encapsulation: 209, structural_boundaries: 196, generics: 186
- `numpy/ma/testutils.pyi` (PYTHON) | Magnitude: 21.04 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, generics: 15, api: 14
- `numpy/ma/core.pyi` (PYTHON) | Magnitude: 1157.28 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3032, encapsulation: 2209, structural_boundaries: 876, generics: 874
- `numpy/testing/_private/utils.pyi` (PYTHON) | Magnitude: 127.12 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 261, structural_boundaries: 109, generics: 92, encapsulation: 92
- `numpy/typing/tests/data/reveal/lib_function_base.pyi` (PYTHON) | Magnitude: 0.05 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 116, indent_spaces: 47, safety_bypasses: 19, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `numpy/f2py/tests/src/return_logical/foo77.f` (FORTRAN) | Magnitude: 33.8 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, args: 24, safety: 24, structural_boundaries: 23
- `doc/source/f2py/code/common.f` (FORTRAN) | Magnitude: 6.4 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, debug_prints: 6, state_mutation: 3, comprehensions: 3
- `doc/source/f2py/code/moddata.f90` (FORTRAN) | Magnitude: 8.44 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, debug_prints: 7, state_mutation: 3
- `doc/source/f2py/code/allocarr.f90` (FORTRAN) | Magnitude: 28.7 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, structural_boundaries: 5, debug_prints: 4
- `numpy/f2py/tests/src/parameter/constant_array.f90` (FORTRAN) | Magnitude: 29.12 | Delta: **0.635 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 28, safety: 22, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `numpy/_core/tests/test_multithreading.py` (PYTHON) | Magnitude: 379.64 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 247, structural_boundaries: 86, branch: 54, test: 44
- `numpy/_core/tests/test_hashtable.py` (PYTHON) | Magnitude: 176.72 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 41, branch: 38, test: 31
- `numpy/_core/src/common/npy_import.c` (C) | Magnitude: 136.14 | Delta: **0.266 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 33, branch: 16, concurrency: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `numpy/f2py/cfuncs.py` (PYTHON) | Magnitude: 27.74 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 140, indent_spaces: 129, branch: 49, dead_code: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `numpy/exceptions.py` (PYTHON) | Magnitude: 64.88 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 18, structural_boundaries: 17, doc: 16
- `doc/source/dev/examples/doxy_func.h` (C) | Magnitude: 11.52 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, args: 1, api: 1, pointers: 1
- `numpy/_core/tests/test_casting_floatingpoint_errors.py` (PYTHON) | Magnitude: 115.46 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, lazy_evaluation: 28, structural_boundaries: 23, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `numpy/f2py/tests/test_pyf_src.py` (PYTHON) | Magnitude: 6.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 7, indent_spaces: 5, args: 2
- `numpy/_core/src/_simd/checks/cpu_lsx.c` (C) | Magnitude: 5.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 3, structural_boundaries: 2, macros: 2, indent_spaces: 2
- `numpy/_core/src/multiarray/convert_datatype.c` (C) | Magnitude: 7767.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1735, state_mutation: 1200, pointers: 546, branch: 511
- `numpy/_core/src/common/binop_override.h` (C) | Magnitude: 103.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, branch: 21, api: 8, structural_boundaries: 7
- `numpy/f2py/tests/test_routines.py` (PYTHON) | Magnitude: 9.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, test: 9, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `numpy/f2py/tests/src/callback/gh18335.f90` (FORTRAN) | Magnitude: 9.76 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
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
- `numpy/_core/src/umath/ufunc_object.c` -> Churn: **65.5%** | Cog Load: 93.4463% | Debt: 14.534%
- `numpy/ma/core.py` -> Churn: **63.49%** | Cog Load: 27.3977% | Debt: 62.7219%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `numpy/linalg/umath_linalg.cpp` -> **Evgeni Burovski** (100.0% isolated ownership) | Magnitude: 5076.18
- `numpy/_core/src/npysort/timsort.cpp` -> **Moritz Groß** (100.0% isolated ownership) | Magnitude: 3669.22
- `numpy/_build_utils/tempita/_tempita.py` -> **Noxaster** (100.0% isolated ownership) | Magnitude: 3320.46
- `numpy/_core/src/multiarray/stringdtype/casts.cpp` -> **Warren Weckesser** (100.0% isolated ownership) | Magnitude: 3301.26
- `numpy/_core/src/multiarray/dtype_transfer.c` -> **Matti Picus** (100.0% isolated ownership) | Magnitude: 3137.82

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

- `numpy/_core/src/common/npy_cpu_features.h` -> **Severity: 2.707** (Embedded: 0.0372 * Error Risk: 72.7469%)
- `numpy/_core/src/common/lowlevel_strided_loops.h` -> **Severity: 1.497** (Embedded: 0.0234 * Error Risk: 63.9713%)
- `numpy/_core/src/multiarray/alloc.h` -> **Severity: 1.34** (Embedded: 0.0168 * Error Risk: 80.0%)
- `numpy/_core/src/multiarray/datetime.c` -> **Severity: 1.015** (Embedded: 0.0129 * Error Risk: 78.3784%)
- `numpy/_core/src/umath/_rational_tests.c` -> **Severity: 0.605** (Embedded: 0.0076 * Error Risk: 79.4067%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `numpy/core/_utils.py` -> **Severity: 1313.125** (Blast Radius: 14.571 * Doc Risk: 90.1191%)
- `numpy/_core/src/multiarray/array_method.h` -> **Severity: 1234.1** (Blast Radius: 12.341 * Doc Risk: 100.0%)
- `numpy/_core/src/multiarray/dtypemeta.h` -> **Severity: 569.6** (Blast Radius: 5.696 * Doc Risk: 100.0%)
- `numpy/_core/src/common/npy_import.h` -> **Severity: 358.8** (Blast Radius: 3.588 * Doc Risk: 100.0%)
- `numpy/_core/src/multiarray/npy_static_data.h` -> **Severity: 352.1** (Blast Radius: 3.521 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
