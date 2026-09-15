# ARCHITECTURAL_BRIEF: scipy
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
| Total Artifacts | 4288 |
| Analyzed Artifacts (Scanned) | 3253 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1035 |
| Total LOC | 782964 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7586 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1583 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3311 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 192 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1175 | 313512 | 36.1% |
| PYTHON | 1116 | 304045 | 34.3% |
| C | 410 | 116060 | 12.6% |
| PLAINTEXT | 185 | 82 | 5.7% |
| JAVASCRIPT | 143 | 28583 | 4.4% |
| FORTRAN | 92 | 18367 | 2.8% |
| MARKDOWN | 48 | 0 | 1.5% |
| JSON | 42 | 424 | 1.3% |
| SHELL | 13 | 400 | 0.4% |
| XML | 7 | 0 | 0.2% |
| MAKEFILE | 5 | 239 | 0.2% |
| M4 | 4 | 56 | 0.1% |
| MATLAB | 4 | 76 | 0.1% |
| HTML | 2 | 23 | 0.1% |
| YAML | 2 | 19 | 0.1% |
| CSS | 1 | 76 | 0.0% |
| OBJECTIVE-C | 1 | 18 | 0.0% |
| NIX | 1 | 62 | 0.0% |
| CSHARP | 1 | 909 | 0.0% |
| BATCH | 1 | 13 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.14; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 22%, Large Core Modules 21%, Declarative / Non-Code 17%, Data / Markup / Trivial 13%, Interface Declarations Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2990 | 91.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 211 | 6.5% |
| Static: Minified & Vendor Opaque Mass | 52 | 1.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1035*

**Composition by Extension & Reason:**
- `.rst`: 323x Excluded (Unsupported Extension: '.rst'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 140x Excluded (Unsupported Extension: '.npz'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mat`: 113x Excluded (Unsupported Extension: '.mat')
- `.build`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 14x Excluded (Saturation: Line 25 exceeds 500 chars), 8x Excluded (Saturation: Line 34 exceeds 500 chars), 7x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.sav`: 47x Excluded (Unsupported Extension: '.sav')
- `no_extension`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.dat`: 26x Excluded (Unsupported Extension: '.dat')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 6631 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2305 LOC)
- `.wav`: 22x Excluded (Explicitly Denied Extension: '.wav')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2273 LOC)
- `.src`: 17x Excluded (Unsupported Extension: '.src'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hpp`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 31 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 19814 commas in 2003 LOC)
- `.arff`: 16x Excluded (Unsupported Extension: '.arff')
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 34.9 | 34.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 65.7 | 81.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.7 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.1 | 4.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.1 | 83.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 80.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.5 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 68.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 103521 | 1679 | 60 | `scipy-1.17.1/subprojects/qhull_r/libqhull_r/merge_r.c` |
| cleanup | 508 | 151 | 0 | `scipy-1.17.1/scipy/optimize/tnc/tnc.c` |
| guards | 58705 | 2067 | 49 | `scipy-1.17.1/scipy/_build_utils/src/npy_cblas_base.h` |
| danger | 10660 | 1045 | 7 | `scipy-1.17.1/subprojects/highs/highs/highspy/highs.py` |
| concurrency | 675 | 147 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |
| connectivity | 28348 | 1991 | 19 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| io | 1299 | 197 | 0 | `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` |
| crypto | 5 | 4 | 0 | `scipy-1.17.1/tools/write_release_and_log.py` |
| ipc | 88 | 29 | 0 | `scipy-1.17.1/tools/lint.py` |
| time | 162 | 40 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |
| serialization | 203 | 21 | 0 | `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` |
| regex | 490 | 67 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |
| events | 1154 | 124 | 0 | `scipy-1.17.1/scipy/integrate/__quadpack.h` |
| tests | 17847 | 326 | 1 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| docs | 8588 | 1334 | 7 | `scipy-1.17.1/scipy/special/cython_special.pyx` |
| debt | 4752 | 721 | 3 | `scipy-1.17.1/subprojects/highs/highs/highspy/_core/__init__.pyi` |
| mutation | 406074 | 2576 | 300 | `scipy-1.17.1/scipy/integrate/_lebedev.py` |
| dead_code | 16543 | 1555 | 10 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| credential | 1 | 1 | 0 | `scipy-1.17.1/tools/wheels/upload_wheels.sh` |
| threat | 5994 | 1357 | 3 | `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/cstdfloat/cstdfloat_cmath.hpp` |
| ml_ai | 8026 | 1217 | 6 | `scipy-1.17.1/subprojects/xsf/include/xsf/amos/amos.h` |
| ui | 57 | 19 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` (Hits: 372)
- `scipy-1.17.1/tools/wheels/gfortran_utils.sh` (Hits: 27)
- `scipy-1.17.1/scipy/io/matlab/tests/test_mio.py` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **numpy.h** (`scipy-1.17.1/subprojects/xsf/include/xsf/numpy.h`) — 791 inbound connections
2. **scipy.css** (`scipy-1.17.1/doc/source/_static/scipy.css`) — 183 inbound connections
3. **config.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/config.hpp`) — 168 inbound connections
4. **linalg.py** (`scipy-1.17.1/benchmarks/benchmarks/linalg.py`) — 164 inbound connections
5. **sparse.py** (`scipy-1.17.1/benchmarks/benchmarks/sparse.py`) — 151 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rational.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/rational.hpp`) — 119 outbound dependencies
2. **special_functions.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions.hpp`) — 66 outbound dependencies
3. **xsf_wrappers.cpp** (`scipy-1.17.1/scipy/special/xsf_wrappers.cpp`) — 49 outbound dependencies
4. **releasing.rst.inc** (`scipy-1.17.1/doc/source/dev/core-dev/releasing.rst.inc`) — 45 outbound dependencies
5. **distributions.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/distributions.hpp`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `trlib_krylov_min_internal` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/optimize/_trlib/trlib_krylov.c`) -> Impact: **1249.0** | LOC: 656
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `lsoda` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/lsoda.c`) -> Impact: **933.6** | LOC: 714
  * *Intent:* * @param itol Tolerance type indicator (1-4). * @param rtol Relative tolerance array. * @param atol Absolute tolerance array. * @param itask Task indi...
- `trlib_tri_factor_min` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/optimize/_trlib/trlib_tri_factor.c`) -> Impact: **765.4** | LOC: 390
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `writeGlpsolSolution` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsModelUtils.cpp`) -> Impact: **720.0** | LOC: 661
- `zvode` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/zvode.c`) -> Impact: **658.0** | LOC: 691
  * *Intent:* * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @param iopt Optional input flag * @param zwork Complex work array * @p...
- `qh_initflags` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/qhull_r/libqhull_r/global_r.c`) -> Impact: **652.0** | LOC: 916
  * *Intent:* */
- `writeMps` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/highs/highs/io/HMPSIO.cpp`) -> Impact: **620.4** | LOC: 407
- `fppola` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/interpolate/fitpack/fppola.f`) -> Impact: **602.5** | LOC: 840
- `dvode` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/vode.c`) -> Impact: **600.3** | LOC: 641
  * *Intent:* * @param rtol Relative tolerance * @param atol Absolute tolerance * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @par...
- `qh_rboxpoints2` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/qhull_r/libqhull_r/rboxlib_r.c`) -> Impact: **597.9** | LOC: 677
  * *Intent:* } /* rboxpoints */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC` | 195 | 65242.36 | 58.59% | 32.24% |
| `scipy-1.17.1/scipy/stats` | 69 | 46618.24 | 37.37% | 22.09% |
| `scipy-1.17.1/scipy/optimize` | 74 | 37433.76 | 41.41% | 21.65% |
| `scipy-1.17.1/scipy/stats/tests` | 41 | 35000.58 | 33.47% | 0.0% |
| `scipy-1.17.1/scipy/interpolate/fitpack` | 87 | 29726.72 | 67.65% | 47.42% |
| `scipy-1.17.1/subprojects/qhull_r/libqhull_r` | 30 | 28350.96 | 48.55% | 20.25% |
| `scipy-1.17.1/subprojects/highs/highs/mip` | 56 | 22555.82 | 48.05% | 27.39% |
| `scipy-1.17.1/subprojects/highs/highs/lp_data` | 36 | 21557.2 | 35.28% | 22.89% |
| `scipy-1.17.1/scipy/integrate` | 20 | 20885.28 | 46.56% | 27.87% |
| `scipy-1.17.1/scipy/signal` | 45 | 19790.9 | 35.81% | 29.39% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scipy-1.17.1/benchmarks/benchmarks/ndimage_interpolation.py` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/ndimage/_delegators.py` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/signal/_delegators.py` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/spatial/_qhull.pyi` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/special/cython_special.pxd` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scipy-1.17.1/benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cluster_hierarchy_disjoint_set.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cutest/calfun.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cutest/dfovec.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scipy-1.17.1/scipy/stats/tests/test_stats.py` -> **466** Orphaned Functions | **4** Duplicates
- `scipy-1.17.1/scipy/stats/tests/test_distributions.py` -> **412** Orphaned Functions | **7** Duplicates
- `scipy-1.17.1/scipy/special/tests/test_basic.py` -> **341** Orphaned Functions | **0** Duplicates
- `scipy-1.17.1/scipy/special/xsf_wrappers.cpp` -> **259** Orphaned Functions | **0** Duplicates
- `scipy-1.17.1/scipy/special/cython_special.pxd` -> **232** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `29` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11770` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scipy-1.17.1/benchmarks/benchmarks/fft_basic.py` (PYTHON) -> Cumulative Risk: **823.75**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.17)
- **Magnitude:** 460.8 | **LOC:** 355 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.6364%)
- **Heaviest Functions:** `setup` (Many-Argument Workhorses, Impact: 19.1), `setup` (Many-Argument Workhorses, Impact: 19.0), `setup` (Many-Argument Workhorses, Impact: 9.7)

### 2. `scipy-1.17.1/doc/source/_static/scipy-mathjax/jax/output/SVG/autoload/maction.js` (JAVASCRIPT) -> Cumulative Risk: **822.94**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.60)
- **Magnitude:** 169.26 | **LOC:** 202 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9561%)
- **Heaviest Functions:** `SVGtooltipPost` (Defensive Guards, Impact: 10.5), `SVGtooltipOver` (Callbacks & Closures, Impact: 7.7), `SVGclick` (Callbacks & Closures, Impact: 4.9)

### 3. `scipy-1.17.1/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/autoload/maction.js` (JAVASCRIPT) -> Cumulative Risk: **820.07**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.58)
- **Magnitude:** 169.98 | **LOC:** 179 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9665%)
- **Heaviest Functions:** `CHTMLtooltipOver` (Callbacks & Closures, Impact: 9.3), `CHTMLtooltipPost` (Defensive Guards, Impact: 8.8), `tooltip` (State Mutators, Impact: 7.4)

### 4. `scipy-1.17.1/benchmarks/benchmarks/integrate.py` (PYTHON) -> Cumulative Risk: **797.41**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.16)
- **Magnitude:** 300.0 | **LOC:** 405 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Cognitive Load (93.9464%)
- **Heaviest Functions:** `setup` (Many-Argument Workhorses, Impact: 30.4), `setup` (Compute Cores, Impact: 8.5), `setup` (Defensive Guards, Impact: 3.9)

### 5. `scipy-1.17.1/doc/source/_static/scipy-mathjax/extensions/MathEvents.js` (JAVASCRIPT) -> Cumulative Risk: **784.88**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.60)
- **Magnitude:** 483.96 | **LOC:** 620 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (94.5824%)
- **Heaviest Functions:** `ContextMenu` (Many-Argument Workhorses, Impact: 46.0), `Hover` (Compute Cores, Impact: 23.9), `AltContextMenu` (Defensive Guards, Impact: 21.4)

### 6. `scipy-1.17.1/benchmarks/benchmarks/sparse.py` (PYTHON) -> Cumulative Risk: **767.56**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.77)
- **Magnitude:** 722.5 | **LOC:** 612 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2072%), Documentation (96.0784%)
- **Heaviest Functions:** `setup` (Many-Argument Workhorses, Impact: 25.9), `setup` (Many-Argument Workhorses, Impact: 18.7), `_timeit` (Compute Cores, Impact: 17.1)

### 7. `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/quadrature/naive_monte_carlo.hpp` (CPP) -> Cumulative Risk: **766.84**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.16)
- **Magnitude:** 282.78 | **LOC:** 469 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.4985%)
- **Heaviest Functions:** `m_integrate` (Compute Cores, Impact: 26.2), `m_thread_monte` (Many-Argument Workhorses, Impact: 13.7), `naive_monte_carlo` (State Mutators, Impact: 2.7)

### 8. `scipy-1.17.1/benchmarks/benchmarks/signal.py` (PYTHON) -> Cumulative Risk: **756.89**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 279.74 | **LOC:** 246 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.9395%)
- **Heaviest Functions:** `time_convolve2d` (Compute Cores, Impact: 10.3), `time_correlate2d` (Compute Cores, Impact: 10.3), `time_convolve2d` (Compute Cores, Impact: 9.0)

### 9. `scipy-1.17.1/benchmarks/benchmarks/signal_filtering.py` (PYTHON) -> Cumulative Risk: **747.9**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -1.11)
- **Magnitude:** 100.62 | **LOC:** 121 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.6801%)
- **Heaviest Functions:** `time_sosfilt` (Parameter Forwarders, Impact: 4.3), `_medfilt2d` (Encapsulated Accessors, Impact: 3.6), `setup` (Type Conversions, Impact: 2.5)

### 10. `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/statistics/detail/single_pass.hpp` (CPP) -> Cumulative Risk: **736.77**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.29)
- **Magnitude:** 316.86 | **LOC:** 402 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9344%)
- **Heaviest Functions:** `gini_coefficient_parallel_impl` (Many-Argument Workhorses, Impact: 31.6), `first_four_moments_parallel_impl` (Many-Argument Workhorses, Impact: 23.2), `mode_impl` (Many-Argument Workhorses, Impact: 15.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scipy-1.17.1/subprojects/xsf/include/xsf/specfun/specfun.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 11762.3 | **LOC:** 6197 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.0621%), Tech Debt (7.7386%)
**Top Internal Functions/Classes:**
  * `cv0` **(Compute Cores)** (Impact: 268.9)
  * `hygfz` **(Many-Argument Workhorses)** (Impact: 265.1)
  * `mtu12` **(Many-Argument Workhorses)** (Impact: 199.4)
  * `fcoef` **(Many-Argument Workhorses)** (Impact: 198.4)
  * `rmn2sp` **(Many-Argument Workhorses)** (Impact: 118.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2595 instances
* *State Mutation (weighted view):* 7895
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1369`, `structural_boundaries: 345`, `args: 187`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `state_mutation: 2705`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `safety: 51`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001157
  * `Imports (Out-Degree: 0):` config.h, memory
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/xsf/include/xsf/amos/amos.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 9158.56 | **LOC:** 6595 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9057%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unk2` **(Many-Argument Workhorses)** (Impact: 289.5)
  * `unk1` **(Many-Argument Workhorses)** (Impact: 231.0)
  * `bknu` **(Many-Argument Workhorses)** (Impact: 228.5)
  * `unhj` **(Many-Argument Workhorses)** (Impact: 195.4)
  * `besh` **(Many-Argument Workhorses)** (Impact: 165.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1990 instances
* *State Mutation (weighted view):* 6241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 813`, `structural_boundaries: 293`, `args: 98`, `func_start: 29`
* *Risk/State:* `state_mutation: 2261`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 1`, `doc: 20`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000738
  * `Imports (Out-Degree: 0):` complex, math.h, memory, stdlib.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/integrate/__quadpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7383.18 | **LOC:** 6857 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.0914%), Tech Debt (8.8674%)
**Top Internal Functions/Classes:**
  * `dqawoe` **(Many-Argument Workhorses)** (Impact: 403.5)
  * `dqagpe` **(Many-Argument Workhorses)** (Impact: 402.6)
  * `dqagie` **(Many-Argument Workhorses)** (Impact: 285.5)
    * *Intent:* // Constants static const double uflow = 2.2250738585072014e-308; /* np.finfo(np.float64).tiny */ st...
  * `dqagse` **(Many-Argument Workhorses)** (Impact: 273.2)
  * `dqawfe` **(Many-Argument Workhorses)** (Impact: 189.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1409 instances
* *State Mutation (weighted view):* 4569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 139`, `args: 48`, `func_start: 26`
* *Risk/State:* `state_mutation: 1751`, `dead_code: 42`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __quadpack.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_continuous_distns.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 7175.3 | **LOC:** 12544 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.3036%), Tech Debt (99.8104%)
**Top Internal Functions/Classes:**
  * `fit` **(Many-Argument Workhorses)** (Impact: 127.2)
  * `fit` **(Many-Argument Workhorses)** (Impact: 92.8)
    * *Intent:* # Summary of the strategy: # # 1) If the scale and location are fixed, return the shape according # ...
  * `_rvs_scalar` **(Many-Argument Workhorses)** (Impact: 73.7)
    * *Intent:* # following [2], the quasi-pdf is used instead of the pdf for the # generation of rvs invert_res = F...
  * `fit` **(Many-Argument Workhorses)** (Impact: 65.5)
  * `fit` **(Many-Argument Workhorses)** (Impact: 57.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 670 instances
* *State Mutation (weighted view):* 2893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 2635`, `args: 1275`, `func_start: 1180`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1553`, `dead_code: 33`, `fragile_debt: 2`, `duplicate_logic: 126`
* *Architecture:* `api: 276`, `import: 26`
* *Defense:* `safety: 25`, `doc: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.194
  * `Choke Point (Betweenness):` 0.000251 | `Ripple Effect (Closeness):` 0.001826
  * `Imports (Out-Degree: 11):` , ._censored_data, ._constants, ._distn_infrastructure, ._ksstats, ._tukeylambda_stats, collections.abc, ctypes...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/special/cdflib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6733.06 | **LOC:** 5785 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.228%), Tech Debt (10.7977%)
**Top Internal Functions/Classes:**
  * `bratio` **(Many-Argument Workhorses)** (Impact: 232.0)
  * `gratio` **(Many-Argument Workhorses)** (Impact: 215.0)
  * `gaminv` **(Many-Argument Workhorses)** (Impact: 202.1)
  * `dinvr` **(Compute Cores)** (Impact: 120.1)
  * `dzror` **(Compute Cores)** (Impact: 73.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1427 instances
* *State Mutation (weighted view):* 4404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 892`, `structural_boundaries: 605`, `args: 128`, `func_start: 62`, `class_start: 66`
* *Risk/State:* `state_mutation: 1550`, `dead_code: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cdflib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/tests/test_stats.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 6637.7 | **LOC:** 9490 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.6395%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wkq` **(Compute Cores)** (Impact: 35.0)
    * *Intent:* # Trivial quadratic implementation, all parameters mandatory
  * `check_power_divergence` **(Many-Argument Workhorses)** (Impact: 28.6)
  * `test_kendalltau` **(I/O & Config Routines)** (Impact: 27.0)
    * *Intent:* # W.II.E. Tabulate X against X, using BIG as a case weight. The values # should appear on the diagon...
  * `test_input_validation` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* # test data not a 2d array with assert_raises(ValueError, match="`data` must be a 2d array."): stats...
  * `test_pval_ci_match` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* # Verify that the following statement holds: # The 95% confidence interval corresponding with altern...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 584 instances
* *State Mutation (weighted view):* 3467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 1086`, `args: 612`, `func_start: 609`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2299`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 466`
* *Architecture:* `io: 4`, `api: 662`, `import: 29`
* *Defense:* `safety: 97`, `doc: 28`, `test: 977`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` .common_tests, collections, contextlib, hypothesis, hypothesis.extra.numpy, itertools, math, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/subprojects/highs/highs/presolve/HPresolve.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 6099.42 | **LOC:** 7482 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (68.9302%)
**Top Internal Functions/Classes:**
  * `HPresolve::rowPresolve` **(Many-Argument Workhorses)** (Impact: 390.9)
  * `HPresolve::detectParallelRowsAndCols` **(Compute Cores)** (Impact: 350.1)
  * `HPresolve::computeColBounds` **(Many-Argument Workhorses)** (Impact: 184.0)
  * `HPresolve::dominatedColumns` **(Compute Cores)** (Impact: 158.4)
  * `HPresolve::sparsify` **(Compute Cores)** (Impact: 138.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 807 instances
* *State Mutation (weighted view):* 2522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1756`, `structural_boundaries: 490`, `args: 321`, `func_start: 120`, `class_start: 1`
* *Risk/State:* `state_mutation: 908`, `dead_code: 94`, `planned_debt: 10`, `unreferenced_by_name: 112`
* *Architecture:* `import: 26`
* *Defense:* `safety: 143`, `immutability_locks: 183`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` pdqsort.h, Highs.h, algorithm, atomic, cmath, HighsIO.h, limits, HConst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5946.02 | **LOC:** 10986 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DODMN` **(Compute Cores)** (Impact: 183.2)
    * *Intent:* *DODMN
  * `DODPC1` **(Compute Cores)** (Impact: 154.8)
    * *Intent:* *DODPC1
  * `DODPC3` **(Compute Cores)** (Impact: 113.0)
    * *Intent:* *DODPC3
  * `DODCHK` **(Compute Cores)** (Impact: 103.0)
    * *Intent:* *DODCHK
  * `DSOLVE` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* *DSOLVE
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 6 instances
* *Amplified Cascading Flux:* 1183 instances
* *Sec Tainted Injection (weighted view):* 6
* *State Mutation (weighted view):* 3761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1401`, `structural_boundaries: 466`, `args: 98`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 8`, `state_mutation: 1395`
* *Architecture:* `io: 372`, `api: 50`
* *Defense:* `safety: 31`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_stats_py.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5891.78 | **LOC:** 10841 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.1515%), Tech Debt (10.2021%)
**Top Internal Functions/Classes:**
  * `_xp_mean` **(Many-Argument Workhorses)** (Impact: 109.1)
  * `pearsonr` **(Many-Argument Workhorses)** (Impact: 94.3)
    * *Intent:* # Missing special.betainc on torch
  * `spearmanr` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `kendalltau` **(Many-Argument Workhorses)** (Impact: 79.1)
  * `ttest_ind` **(Many-Argument Workhorses)** (Impact: 69.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 926 instances
* *State Mutation (weighted view):* 3073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 805`, `structural_boundaries: 473`, `args: 187`, `func_start: 153`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1221`, `dead_code: 10`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 101`, `import: 28`
* *Defense:* `safety: 22`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.398
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.00503
  * `Imports (Out-Degree: 9):` , ._axis_nan_policy, ._binomtest, ._resampling, ._stats, ._stats_mstats_common, ._stats_pythran, collections...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/optimize/__minpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5633.66 | **LOC:** 4379 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2185%), Tech Debt (10.513%)
**Top Internal Functions/Classes:**
  * `LMSTR` **(Many-Argument Workhorses)** (Impact: 418.9)
  * `LMDIF` **(Many-Argument Workhorses)** (Impact: 393.5)
  * `LMDER` **(Many-Argument Workhorses)** (Impact: 392.9)
  * `HYBRD` **(Many-Argument Workhorses)** (Impact: 368.1)
  * `HYBRJ` **(Many-Argument Workhorses)** (Impact: 339.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 978 instances
* *State Mutation (weighted view):* 2966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 58`, `args: 28`, `func_start: 17`
* *Risk/State:* `state_mutation: 1010`, `dead_code: 36`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __minpack.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/tests/test_distributions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5426.36 | **LOC:** 10484 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fit` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `test_fit_mm` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `test_location_scale` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `test_pdf_nolan_samples` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `test_cdf_nolan_samples` **(Many-Argument Workhorses)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 274 instances
* *State Mutation (weighted view):* 2491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 1187`, `args: 797`, `func_start: 748`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 1943`, `dead_code: 130`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 7`, `unreferenced_by_name: 412`
* *Architecture:* `io: 7`, `api: 843`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 183`, `doc: 29`, `test: 991`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .test_discrete_basic, itertools, json, mpmath, numpy, numpy.lib.recfunctions, numpy.testing, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_distribution_infrastructure.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4980.14 | **LOC:** 5819 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.4504%), Tech Debt (29.9682%)
**Top Internal Functions/Classes:**
  * `plot` **(Many-Argument Workhorses)** (Impact: 141.8)
    * *Intent:* ### Convenience
  * `filtered` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `_set_invalid_nan` **(Compute Cores)** (Impact: 65.9)
    * *Intent:* # Wrapper for input / output validation and standardization of distribution # functions that accept ...
  * `_quadrature` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* ## Algorithms
  * `_make_distribution_rv_generic` **(Compute Cores)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 643 instances
* *State Mutation (weighted view):* 2265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 967`, `args: 450`, `func_start: 433`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 979`, `dead_code: 11`, `planned_debt: 12`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `api: 126`, `import: 20`
* *Defense:* `safety: 34`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000922
  * `Imports (Out-Degree: 7):` abc, functools, inspect, math, matplotlib.pyplot, numpy, scipy, scipy._lib._array_api...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/qhull_r/libqhull_r/merge_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4718.1 | **LOC:** 5591 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3343%), Tech Debt (8.3295%)
**Top Internal Functions/Classes:**
  * `qh_mergefacet` **(Many-Argument Workhorses)** (Impact: 203.1)
    * *Intent:* */
  * `qh_test_nonsimplicial_merge` **(Many-Argument Workhorses)** (Impact: 180.9)
    * *Intent:* */
  * `qh_all_merges` **(Many-Argument Workhorses)** (Impact: 117.5)
    * *Intent:* */
  * `qh_renamevertex` **(Many-Argument Workhorses)** (Impact: 93.8)
    * *Intent:* */
  * `qh_appendmergeset` **(Many-Argument Workhorses)** (Impact: 88.7)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 643 instances
* *State Mutation (weighted view):* 2014
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1022`, `structural_boundaries: 191`, `args: 234`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 728`, `dead_code: 9`, `unreferenced_by_name: 3`
* *Architecture:* `api: 92`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/sparse/tests/test_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4594.34 | **LOC:** 5909 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1759%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `with_64bit_maxval_limit` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `test_slicing_3` **(Compute Cores)** (Impact: 32.9)
  * `test_argmax` **(Compute Cores)** (Impact: 31.1)
  * `test_minmax_axis` **(Compute Cores)** (Impact: 29.1)
  * `sparse_test_class` **(Many-Argument Workhorses)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 461 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 786`, `args: 360`, `func_start: 358`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 1`, `state_mutation: 1522`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 23`
* *Architecture:* `io: 1`, `api: 353`, `import: 24`
* *Defense:* `safety: 176`, `doc: 14`, `test: 306`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000307
  * `Imports (Out-Degree: 5):` contextlib, functools, itertools, numpy, numpy.exceptions, numpy.testing, operator, pickle...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/qhull_r/libqhull_r/io_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4498.6 | **LOC:** 4129 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5995%), Tech Debt (12.3102%)
**Top Internal Functions/Classes:**
  * `qh_printbegin` **(Many-Argument Workhorses)** (Impact: 354.2)
    * *Intent:* */
  * `qh_readpoints` **(Many-Argument Workhorses)** (Impact: 321.3)
    * *Intent:* */
  * `qh_printafacet` **(Many-Argument Workhorses)** (Impact: 172.8)
    * *Intent:* */
  * `qh_printfacetheader` **(Many-Argument Workhorses)** (Impact: 144.8)
    * *Intent:* */
  * `qh_printfacets` **(Many-Argument Workhorses)** (Impact: 112.1)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 552 instances
* *State Mutation (weighted view):* 1705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1000`, `structural_boundaries: 186`, `args: 110`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 601`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 72`, `import: 1`
* *Defense:* `safety: 20`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/integrate/_lebedev.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4248.32 | **LOC:** 5454 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.7454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_lebedev_sphere` **(Many-Argument Workhorses)** (Impact: 69.0)
    * *Intent:* # getLebedevSphere # @author Rob Parrish, The Sherrill Group, CCMST Georgia Tech # @email robparrish...
  * `get_lebedev_recurrence_points` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `lebedev_rule` **(I/O & Config Routines)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 4035
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3735`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000307
  * `Imports (Out-Degree: 2):` matplotlib.pyplot, numpy, scipy._lib._array_api, scipy.integrate
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/optimize/__lbfgsb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4216.38 | **LOC:** 3768 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9163%), Tech Debt (8.2264%)
**Top Internal Functions/Classes:**
  * `cauchy` **(Many-Argument Workhorses)** (Impact: 329.0)
  * `mainlb` **(Many-Argument Workhorses)** (Impact: 267.4)
  * `subsm` **(Many-Argument Workhorses)** (Impact: 224.1)
  * `lnsrlb` **(Many-Argument Workhorses)** (Impact: 202.3)
  * `dcsrch` **(Many-Argument Workhorses)** (Impact: 186.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 724 instances
* *State Mutation (weighted view):* 2311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 76`, `args: 33`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 863`, `dead_code: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __lbfgsb.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/integrate/src/zvode.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4069.98 | **LOC:** 2785 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `zvode` **(Many-Argument Workhorses)** (Impact: 658.0)
    * *Intent:* * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @param iopt Optional...
  * `zvstep` **(Many-Argument Workhorses)** (Impact: 397.2)
    * *Intent:* * @param wm Complex work array for matrix operations * @param iwm Integer work array for matrix oper...
  * `zvjac` **(Many-Argument Workhorses)** (Impact: 288.4)
    * *Intent:* * @param wm Complex work space for matrices. On output contains the inverse * diagonal matrix if MIT...
  * `zvnlsd` **(Many-Argument Workhorses)** (Impact: 208.5)
    * *Intent:* * @param y Complex predicted solution vector, updated by corrector * @param yh Complex Nordsieck his...
  * `zvhin` **(Many-Argument Workhorses)** (Impact: 95.0)
    * *Intent:* * @param f User function for right-hand side f(t,y) * @param rpar User real work array * @param ipar...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 668 instances
* *State Mutation (weighted view):* 2104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 163`, `args: 165`, `func_start: 14`
* *Risk/State:* `state_mutation: 768`, `dead_code: 3`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 12`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, math.h, stdlib.h, zvode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/linalg/_matfuncs_expm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4066.28 | **LOC:** 2384 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.7996%), Tech Debt (11.8031%)
**Top Internal Functions/Classes:**
  * `pade_UV_calc_c` **(Many-Argument Workhorses)** (Impact: 144.5)
  * `pade_UV_calc_z` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `pick_pade_structure_z` **(Many-Argument Workhorses)** (Impact: 127.8)
  * `pick_pade_structure_c` **(Many-Argument Workhorses)** (Impact: 127.7)
  * `pick_pade_structure_s` **(Many-Argument Workhorses)** (Impact: 122.8)
    * *Intent:* /******************************************************************************* *******************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 914 instances
* *State Mutation (weighted view):* 2898
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 58`, `args: 133`, `func_start: 20`
* *Risk/State:* `state_mutation: 1070`, `unreferenced_by_name: 8`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matfuncs_expm.h, complex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsLpUtils.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4062.5 | **LOC:** 3770 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0323%), Tech Debt (35.3252%)
**Top Internal Functions/Classes:**
  * `readSolutionFile` **(Many-Argument Workhorses)** (Impact: 227.9)
  * `getSubVectorsTranspose` **(Many-Argument Workhorses)** (Impact: 138.5)
  * `lpDimensionsOk` **(Many-Argument Workhorses)** (Impact: 100.1)
  * `assessLpPrimalSolution` **(Many-Argument Workhorses)** (Impact: 95.0)
    * *Intent:* // Determine validity, primal feasibility and (when relevant) integer // feasibility of a solution
  * `assessSemiVariables` **(Many-Argument Workhorses)** (Impact: 89.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 596 instances
* *State Mutation (weighted view):* 1895
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 769`, `structural_boundaries: 209`, `args: 111`, `func_start: 77`
* *Risk/State:* `state_mutation: 703`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 11`, `import: 13`
* *Defense:* `safety: 97`, `doc: 1`, `immutability_locks: 338`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` HConfig.h, algorithm, cassert, Filereader.h, HMPSIO.h, HighsIO.h, HighsLpUtils.h, HighsModelUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/subprojects/highs/highs/simplex/HEkk.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4037.74 | **LOC:** 4369 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.7278%), Tech Debt (94.6558%)
**Top Internal Functions/Classes:**
  * `HEkk::proofOfPrimalInfeasibility` **(Many-Argument Workhorses)** (Impact: 105.7)
  * `HEkk::initialiseBound` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `HEkk::initialiseCost` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `HEkk::computeBasisCondition` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `HEkk::returnFromSolve` **(Compute Cores)** (Impact: 60.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 693 instances
* *State Mutation (weighted view):* 2451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 175`, `args: 124`, `func_start: 130`
* *Risk/State:* `state_mutation: 1065`, `dead_code: 22`, `planned_debt: 4`, `unreferenced_by_name: 121`
* *Architecture:* `import: 11`
* *Defense:* `safety: 97`, `doc: 1`, `immutability_locks: 272`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` HighsLpSolverObject.h, HighsLpUtils.h, HighsModelUtils.h, HighsSolutionDebug.h, HighsParallel.h, HEkk.h, HEkkDual.h, HEkkPrimal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3852.54 | **LOC:** 2741 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.0006%), Tech Debt (34.9232%)
**Top Internal Functions/Classes:**
  * `toCommonHTML` **(Defensive Guards)** (Impact: 72.5)
  * `CHTMLadjustVariant` **(Defensive Guards)** (Impact: 54.4)
  * `getCharList` **(Compute Cores)** (Impact: 54.3)
    * *Intent:* // // Get the list of actions for a given character in a given variant // (processing remaps, multi-...
  * `length2em` **(Defensive Guards)** (Impact: 53.2)
    * *Intent:* /********************************************************/ // // ### FIXME: Handle mu's //
  * `extendDelimiterH` **(Many-Argument Workhorses)** (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 699 instances
* *State Mutation (weighted view):* 2172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 756`, `structural_boundaries: 410`, `args: 144`, `func_start: 133`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 774`, `dead_code: 2`, `fragile_debt: 7`, `unreferenced_by_name: 16`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 142`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/subprojects/qhull_r/libqhull_r/poly2_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3821.74 | **LOC:** 3960 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6727%), Tech Debt (16.3354%)
**Top Internal Functions/Classes:**
  * `qh_checkfacet` **(Many-Argument Workhorses)** (Impact: 206.9)
    * *Intent:* */
  * `qh_matchdupridge` **(Many-Argument Workhorses)** (Impact: 197.7)
    * *Intent:* */
  * `qh_checkpolygon` **(Compute Cores)** (Impact: 123.7)
    * *Intent:* */
  * `qh_checklists` **(Compute Cores)** (Impact: 93.5)
    * *Intent:* */
  * `qh_check_maxout` **(Compute Cores)** (Impact: 88.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 568 instances
* *State Mutation (weighted view):* 1800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 131`, `args: 113`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 664`, `dead_code: 4`, `unreferenced_by_name: 23`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_multivariate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3775.48 | **LOC:** 8050 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.144%), Tech Debt (92.428%)
**Top Internal Functions/Classes:**
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 75.3)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure conformality. Par...
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure compatible dimens...
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* """ Infer dimensionality from location array and shape matrix, handle defaults, and ensure compatibl...
  * `_process_parameters_psd` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* # Try to infer dimensionality if dim is None: if mean is None: if cov is None: dim = 1 else: cov = n...
  * `_dirichlet_check_input` **(Compute Cores)** (Impact: 33.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 435 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1767
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 678`, `args: 309`, `func_start: 309`, `class_start: 39`
* *Risk/State:* `state_mutation: 897`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 205`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 9`, `doc: 216`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.181
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.00123
  * `Imports (Out-Degree: 10):` , ._continuous_distns, ._discrete_distns, ._morestats, ._qmvnt, math, matplotlib.colors, matplotlib.pyplot...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsInterface.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3734.68 | **LOC:** 4235 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1147%), Tech Debt (50.5617%)
**Top Internal Functions/Classes:**
  * `Highs::elasticityFilter` **(Many-Argument Workhorses)** (Impact: 256.1)
  * `Highs::computeIllConditioning` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `Highs::lpKktCheck` **(Many-Argument Workhorses)** (Impact: 107.8)
  * `Highs::setNonbasicStatusInterface` **(Many-Argument Workhorses)** (Impact: 90.2)
  * `Highs::multiobjectiveSolve` **(Compute Cores)** (Impact: 71.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 548 instances
* *State Mutation (weighted view):* 1902
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 175`, `args: 107`, `func_start: 61`
* *Risk/State:* `state_mutation: 806`, `dead_code: 4`, `planned_debt: 1`, `unreferenced_by_name: 57`
* *Architecture:* `import: 9`
* *Defense:* `safety: 133`, `doc: 1`, `immutability_locks: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Highs.h, HighsLpUtils.h, HighsModelUtils.h, HighsMipSolver.h, HighsHessianUtils.h, HSimplex.h, sstream, HighsMatrixUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/rational.hpp` -> **Severity: 0.16** (Bridge: 0.0018 * Flux: 87.8854%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/polynomial.hpp` -> **Severity: 0.068** (Bridge: 0.0007 * Flux: 99.8487%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/dual.h` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 100.0%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions/gamma.hpp` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 99.9991%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/binom.h` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scipy-1.17.1/subprojects/xsf/include/xsf/numpy.h` -> **Severity: 15.149** (Embedded: 0.2446 * Error Risk: 61.9323%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/dual.h` -> **Severity: 12.256** (Embedded: 0.1275 * Error Risk: 96.1034%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/utility.hpp` -> **Severity: 11.709** (Embedded: 0.1871 * Error Risk: 62.5811%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/error.h` -> **Severity: 9.284** (Embedded: 0.1438 * Error Risk: 64.5656%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/config.hpp` -> **Severity: 8.679** (Embedded: 0.1608 * Error Risk: 53.9717%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/config.hpp` -> **Severity: 9566.7** (Blast Radius: 95.667 * Doc Risk: 100.0%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/numpy.h` -> **Severity: 5919.4** (Blast Radius: 59.194 * Doc Risk: 100.0%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/utility.hpp` -> **Severity: 3059.3** (Blast Radius: 30.593 * Doc Risk: 100.0%)
- `scipy-1.17.1/subprojects/xsf/include/xsf/error.h` -> **Severity: 1691.4** (Blast Radius: 16.914 * Doc Risk: 100.0%)
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/tuple.hpp` -> **Severity: 1309.9** (Blast Radius: 13.099 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
