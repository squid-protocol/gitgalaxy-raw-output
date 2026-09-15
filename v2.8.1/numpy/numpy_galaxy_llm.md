# ARCHITECTURAL_BRIEF: numpy
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
| Total Artifacts | 3111 |
| Analyzed Artifacts (Scanned) | 2196 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 915 |
| Total LOC | 809711 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7434 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2988 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0702 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 92 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1002 | 250542 | 45.6% |
| C | 408 | 234521 | 18.6% |
| CPP | 197 | 59364 | 9.0% |
| JAVASCRIPT | 143 | 28583 | 6.5% |
| ASSEMBLY | 111 | 232245 | 5.1% |
| FORTRAN | 110 | 2316 | 5.0% |
| PLAINTEXT | 73 | 0 | 3.3% |
| JSON | 53 | 162 | 2.4% |
| MARKDOWN | 35 | 0 | 1.6% |
| SHELL | 22 | 613 | 1.0% |
| XML | 19 | 4 | 0.9% |
| MAKEFILE | 6 | 238 | 0.3% |
| YAML | 5 | 214 | 0.2% |
| M4 | 5 | 51 | 0.2% |
| BATCH | 2 | 66 | 0.1% |
| CSV | 2 | 629 | 0.1% |
| CSS | 1 | 70 | 0.0% |
| HTML | 1 | 21 | 0.0% |
| POWERSHELL | 1 | 72 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z -0.98; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 19%, Data / Markup / Trivial 16%, Large Core Modules 15%, Generic / Templated Code Files 12%, Interface Declarations Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2054 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 108 | 4.9% |
| Static: Minified & Vendor Opaque Mass | 34 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 915*

**Composition by Extension & Reason:**
- `.rst`: 383x Excluded (Unsupported Extension: '.rst'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 58x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 14x Excluded (Saturation: Line 25 exceeds 500 chars), 8x Excluded (Saturation: Line 34 exceeds 500 chars), 7x Excluded (Saturation: Line 28 exceeds 500 chars)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 1x Zero-Density Threshold (LOC: 96, Signals: 0)
- `.src`: 38x Excluded (Unsupported Extension: '.src')
- `.build`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 14x Excluded (Static Asset Blob without Intent: 1430 LOC), 10x Excluded (Static Asset Blob without Intent: 1002 LOC), 2x Excluded (Static Asset Blob without Intent: 1630 LOC)
- `.py`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 183 LOC), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC)
- `.pyf`: 18x Excluded (Unsupported Extension: '.pyf')
- `.dat`: 18x Excluded (Unsupported Extension: '.dat')
- `.svg`: 3x Excluded (Machine-Generated Source Code Signature: 4 LOC), 2x Excluded (Static Asset Blob without Intent: 1472 LOC), 1x Excluded (Static Asset Blob without Intent: 2213 LOC)
- `.wrap`: 10x Excluded (Unsupported Extension: '.wrap')
- `.patch`: 9x Excluded (Unsupported Extension: '.patch')
- `.tmpl`: 7x Excluded (Unsupported Extension: '.tmpl')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.0 | 7.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 53.5 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.0 | 5.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 1.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 74.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.2 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 62.1 | 97.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 68923 | 922 | 34 | `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c` |
| cleanup | 276 | 87 | 0 | `numpy-2.4.4/numpy/linalg/umath_linalg.cpp` |
| guards | 45379 | 1129 | 32 | `numpy-2.4.4/numpy/_core/src/highway/hwy/ops/x86_128-inl.h` |
| danger | 14355 | 912 | 16 | `numpy-2.4.4/numpy/__init__.pyi` |
| concurrency | 1281 | 158 | 0 | `numpy-2.4.4/numpy/random/tests/test_generator_mt19937.py` |
| connectivity | 27959 | 1468 | 30 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| io | 5356 | 394 | 4 | `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` |
| crypto | 17 | 16 | 0 | `numpy-2.4.4/vendored-meson/meson/mesonbuild/wrap/wrap.py` |
| ipc | 627 | 118 | 0 | `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` |
| time | 255 | 50 | 0 | `numpy-2.4.4/numpy/__init__.pyi` |
| serialization | 99 | 30 | 0 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| regex | 1048 | 172 | 0 | `numpy-2.4.4/numpy/f2py/crackfortran.py` |
| events | 155 | 34 | 0 | `numpy-2.4.4/numpy/_core/src/multiarray/alloc.c` |
| tests | 9626 | 232 | 1 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| docs | 5997 | 778 | 5 | `numpy-2.4.4/numpy/_core/_add_newdocs.py` |
| debt | 3912 | 574 | 4 | `numpy-2.4.4/numpy/__init__.pyi` |
| mutation | 222488 | 1555 | 218 | `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c` |
| dead_code | 8818 | 962 | 6 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| credential | 9 | 7 | 0 | `numpy-2.4.4/numpy/f2py/rules.py` |
| threat | 8028 | 677 | 6 | `numpy-2.4.4/numpy/__init__.pyi` |
| ml_ai | 4393 | 803 | 4 | `numpy-2.4.4/numpy/_core/tests/test_einsum.py` |
| ui | 75 | 23 | 0 | `numpy-2.4.4/doc/source/_static/scipy-mathjax/MathJax.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` (Hits: 540)
- `numpy-2.4.4/vendored-meson/meson/unittests/linuxliketests.py` (Hits: 270)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend/ninjabackend.py` (Hits: 176)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **numpy.css** (`numpy-2.4.4/doc/source/_static/numpy.css`) — 440 inbound connections
2. **mesonlib.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/mesonlib.py`) — 134 inbound connections
3. **options.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/options.py`) — 80 inbound connections
4. **compilers.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/compilers.py`) — 72 inbound connections
5. **_typing.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/_typing.py`) — 71 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **multiarraymodule.c** (`numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c`) — 60 outbound dependencies
2. **__init__.pyi** (`numpy-2.4.4/numpy/__init__.pyi`) — 54 outbound dependencies
3. **allplatformstests.py** (`numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py`) — 49 outbound dependencies
4. **__init__.py** (`numpy-2.4.4/numpy/__init__.py`) — 48 outbound dependencies
5. **universal.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/utils/universal.py`) — 43 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ilaenv_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_lapack.c`) -> Impact: **961.1** | LOC: 628
  * *Intent:* } /* iladlr_ */
- `cgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **774.5** | LOC: 2496
  * *Intent:* /* End of CGEQRF */ } /* cgeqrf_ */
- `zgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **774.5** | LOC: 2508
  * *Intent:* /* End of ZGEQRF */ } /* zgeqrf_ */
- `zlatrs_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **588.2** | LOC: 1164
  * *Intent:* /* End of ZLATRD */ } /* zlatrd_ */
- `clatrs_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **588.1** | LOC: 1161
  * *Intent:* /* End of CLATRD */ } /* clatrd_ */
- `claqr5_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **536.0** | LOC: 1346
  * *Intent:* } /* claqr4_ */
- `zlaqr5_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **536.0** | LOC: 1350
  * *Intent:* } /* zlaqr4_ */
- `zgemm_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_blas.c`) -> Impact: **516.1** | LOC: 668
  * *Intent:* } /* zdscal_ */
- `cgemm_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_blas.c`) -> Impact: **516.0** | LOC: 667
  * *Intent:* } /* cdotu_ */
- `analyzeline` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/f2py/crackfortran.py`) -> Impact: **514.3** | LOC: 566
  * *Intent:* """ Reads each line in the input file in sequence and updates global vars. Effectively reads and collects information from the input file to the globa...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `numpy-2.4.4/numpy/linalg/lapack_lite` | 13 | 112131.12 | 48.44% | 17.96% |
| `numpy-2.4.4/numpy/_core/src/multiarray` | 110 | 59448.12 | 36.65% | 18.99% |
| `numpy-2.4.4/numpy/_core/tests` | 67 | 39734.74 | 29.42% | 0.0% |
| `numpy-2.4.4/numpy/_core/src/umath` | 35 | 18428.34 | 43.94% | 16.03% |
| `numpy-2.4.4/vendored-meson/meson/mesonbuild` | 29 | 17187.38 | 63.64% | 22.05% |
| `numpy-2.4.4/numpy/_core` | 64 | 14181.12 | 19.03% | 10.28% |
| `numpy-2.4.4/numpy/f2py` | 35 | 14035.98 | 24.79% | 27.73% |
| `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend` | 12 | 13006.1 | 69.72% | 22.32% |
| `numpy-2.4.4/numpy/_core/src/highway/hwy/ops` | 18 | 11767.86 | 16.53% | 7.37% |
| `numpy-2.4.4/numpy/distutils` | 25 | 11370.88 | 37.02% | 39.46% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `numpy-2.4.4/benchmarks/benchmarks/bench_array_coercion.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_creation.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_linalg.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `numpy-2.4.4/benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_itemselection.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_ma.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_manipulate.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` -> **595** Orphaned Functions | **10** Duplicates
- `numpy-2.4.4/numpy/ma/tests/test_core.py` -> **315** Orphaned Functions | **6** Duplicates
- `numpy-2.4.4/numpy/_core/tests/test_regression.py` -> **278** Orphaned Functions | **0** Duplicates
- `numpy-2.4.4/numpy/_core/tests/test_numeric.py` -> **243** Orphaned Functions | **0** Duplicates
- `numpy-2.4.4/numpy/_core/tests/test_umath.py` -> **227** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7631` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/SVG/autoload/maction.js` (JAVASCRIPT) -> Cumulative Risk: **822.94**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.71)
- **Magnitude:** 169.26 | **LOC:** 202 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9561%)
- **Heaviest Functions:** `SVGtooltipPost` (Defensive Guards, Impact: 10.5), `SVGtooltipOver` (Callbacks & Closures, Impact: 7.7), `SVGclick` (Callbacks & Closures, Impact: 4.9)

### 2. `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/autoload/maction.js` (JAVASCRIPT) -> Cumulative Risk: **820.07**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.69)
- **Magnitude:** 169.98 | **LOC:** 179 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9665%)
- **Heaviest Functions:** `CHTMLtooltipOver` (Callbacks & Closures, Impact: 9.3), `CHTMLtooltipPost` (Defensive Guards, Impact: 8.8), `tooltip` (State Mutators, Impact: 7.4)

### 3. `numpy-2.4.4/vendored-meson/meson/mesonbuild/mtest.py` (PYTHON) -> Cumulative Risk: **814.8**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.57)
- **Magnitude:** 3238.86 | **LOC:** 2319 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.2663%)
- **Heaviest Functions:** `log` (Many-Argument Workhorses, Impact: 97.5), `parse_line` (Compute Cores, Impact: 88.3), `__init__` (Many-Argument Workhorses, Impact: 71.5)

### 4. `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/fortran.py` (PYTHON) -> Cumulative Risk: **795.55**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.44)
- **Magnitude:** 584.3 | **LOC:** 721 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Tech Debt (99.9746%), Documentation (98.5507%)
- **Heaviest Functions:** `cross_compute_int` (Many-Argument Workhorses, Impact: 59.4), `compute_int` (Many-Argument Workhorses, Impact: 16.8), `sizeof` (Many-Argument Workhorses, Impact: 14.4)

### 5. `numpy-2.4.4/doc/source/_static/scipy-mathjax/extensions/MathEvents.js` (JAVASCRIPT) -> Cumulative Risk: **784.88**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.72)
- **Magnitude:** 483.96 | **LOC:** 620 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (94.5824%)
- **Heaviest Functions:** `ContextMenu` (Many-Argument Workhorses, Impact: 46.0), `Hover` (Compute Cores, Impact: 23.9), `AltContextMenu` (Defensive Guards, Impact: 21.4)

### 6. `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/d.py` (PYTHON) -> Cumulative Risk: **783.1**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.19)
- **Magnitude:** 895.74 | **LOC:** 864 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.9467%)
- **Heaviest Functions:** `_translate_args_to_nongnu` (Many-Argument Workhorses, Impact: 89.0), `get_feature_args` (Many-Argument Workhorses, Impact: 47.0), `get_soname_args` (Many-Argument Workhorses, Impact: 23.8)

### 7. `numpy-2.4.4/vendored-meson/meson/mesonbuild/dependencies/qt.py` (PYTHON) -> Cumulative Risk: **782.03**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.29)
- **Magnitude:** 526.4 | **LOC:** 486 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9914%), Safety Score (99.0509%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 60.2), `__init__` (Many-Argument Workhorses, Impact: 38.4), `_get_modules_lib_suffix` (Compute Cores, Impact: 29.2)

### 8. `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/asm.py` (PYTHON) -> Cumulative Risk: **771.68**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.24)
- **Magnitude:** 322.56 | **LOC:** 345 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9676%)
- **Heaviest Functions:** `get_always_args` (Compute Cores, Impact: 12.1), `get_debug_args` (Generic / Templated Code, Impact: 10.8), `compute_parameters_with_absolute_paths` (Generic / Templated Code, Impact: 8.3)

### 9. `numpy-2.4.4/vendored-meson/meson/mesonbuild/linkers/linkers.py` (PYTHON) -> Cumulative Risk: **769.43**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.13)
- **Magnitude:** 1482.06 | **LOC:** 1784 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Api Exposure (100.0%), Spec Match (100.0%), State Flux (99.9926%)
- **Heaviest Functions:** `build_rpath_args` (Many-Argument Workhorses, Impact: 62.2), `build_rpath_args` (Many-Argument Workhorses, Impact: 35.8), `build_rpath_args` (Many-Argument Workhorses, Impact: 25.1)

### 10. `numpy-2.4.4/vendored-meson/meson/mesonbuild/msubprojects.py` (PYTHON) -> Cumulative Risk: **765.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.90)
- **Magnitude:** 685.34 | **LOC:** 772 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (97.0157%)
- **Heaviest Functions:** `update_git` (Defensive Guards, Impact: 47.7), `run` (Compute Cores, Impact: 35.0), `purge` (Defensive Guards, Impact: 23.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_blas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 37170.98 | **LOC:** 21604 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6706%), Tech Debt (13.4253%)
**Top Internal Functions/Classes:**
  * `zgemm_` **(Many-Argument Workhorses)** (Impact: 516.1)
    * *Intent:* } /* zdscal_ */
  * `cgemm_` **(Many-Argument Workhorses)** (Impact: 516.0)
    * *Intent:* } /* cdotu_ */
  * `ctrsm_` **(Many-Argument Workhorses)** (Impact: 470.0)
    * *Intent:* /* End of CTRMV . */ } /* ctrmv_ */
  * `ztrsm_` **(Many-Argument Workhorses)** (Impact: 470.0)
    * *Intent:* /* End of ZTRMV . */ } /* ztrmv_ */
  * `ctrmm_` **(Many-Argument Workhorses)** (Impact: 421.0)
    * *Intent:* } /* cswap_ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7726 instances
* *State Mutation (weighted view):* 24262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3409`, `structural_boundaries: 284`, `args: 175`, `func_start: 84`
* *Risk/State:* `state_mutation: 8810`, `unreferenced_by_name: 82`
* *Architecture:* `api: 103`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34592.18 | **LOC:** 29997 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.229%), Tech Debt (8.314%)
**Top Internal Functions/Classes:**
  * `zgesdd_` **(Many-Argument Workhorses)** (Impact: 774.5)
    * *Intent:* /* End of ZGEQRF */ } /* zgeqrf_ */
  * `zlatrs_` **(Many-Argument Workhorses)** (Impact: 588.2)
    * *Intent:* /* End of ZLATRD */ } /* zlatrd_ */
  * `zlaqr5_` **(Many-Argument Workhorses)** (Impact: 536.0)
    * *Intent:* } /* zlaqr4_ */
  * `zlals0_` **(Many-Argument Workhorses)** (Impact: 381.9)
    * *Intent:* /* End of ZLAHR2 */ } /* zlahr2_ */
  * `zlalsd_` **(Many-Argument Workhorses)** (Impact: 339.1)
    * *Intent:* /* End of ZLALSA */ } /* zlalsa_ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6562 instances
* *State Mutation (weighted view):* 21982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2854`, `structural_boundaries: 263`, `args: 352`, `func_start: 84`
* *Risk/State:* `state_mutation: 8858`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 294`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34590.7 | **LOC:** 29862 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3705%), Tech Debt (8.3198%)
**Top Internal Functions/Classes:**
  * `cgesdd_` **(Many-Argument Workhorses)** (Impact: 774.5)
    * *Intent:* /* End of CGEQRF */ } /* cgeqrf_ */
  * `clatrs_` **(Many-Argument Workhorses)** (Impact: 588.1)
    * *Intent:* /* End of CLATRD */ } /* clatrd_ */
  * `claqr5_` **(Many-Argument Workhorses)** (Impact: 536.0)
    * *Intent:* } /* claqr4_ */
  * `clals0_` **(Many-Argument Workhorses)** (Impact: 381.6)
    * *Intent:* /* End of CLAHR2 */ } /* clahr2_ */
  * `clasr_` **(Many-Argument Workhorses)** (Impact: 339.0)
    * *Intent:* /* End of CLASET */ } /* claset_ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6558 instances
* *State Mutation (weighted view):* 21971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2854`, `structural_boundaries: 263`, `args: 368`, `func_start: 84`
* *Risk/State:* `state_mutation: 8855`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 311`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 7892.16 | **LOC:** 11032 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `test_ufunc_binop_interaction` **(Compute Cores)** (Impact: 58.5)
    * *Intent:* # ndarray.__rop__ always calls ufunc # ndarray.__iop__ always calls ufunc # ndarray.__op__, __rop__:...
  * `test_order_mismatch` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* # The order is the main (python side) reason that can cause # a never-copy to fail. # Prepare C-orde...
  * `test_argsort` **(Compute Cores)** (Impact: 35.3)
    * *Intent:* # all c scalar argsorts use the same code with different types # so it suffices to run a quick check...
  * `test_np_argmin_argmax_keepdims` **(Many-Argument Workhorses)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 733 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 4116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 589`, `structural_boundaries: 1706`, `args: 842`, `func_start: 820`, `class_start: 147`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 21`, `state_mutation: 2650`, `dead_code: 10`, `planned_debt: 4`, `fragile_debt: 13`, `duplicate_logic: 10`, `unreferenced_by_name: 595`
* *Architecture:* `io: 81`, `api: 864`, `import: 53`
* *Defense:* `safety: 286`, `doc: 19`, `test: 971`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` _testbuffer, builtins, collections.abc, contextlib, ctypes, datetime, decimal, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/f2py/crackfortran.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5804.2 | **LOC:** 3726 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3171%), Tech Debt (12.923%)
**Top Internal Functions/Classes:**
  * `analyzeline` **(Many-Argument Workhorses)** (Impact: 514.3)
    * *Intent:* """ Reads each line in the input file in sequence and updates global vars. Effectively reads and col...
  * `analyzevars` **(Compute Cores)** (Impact: 241.5)
    * *Intent:* """ Sets correct dimension information for each variable/parameter """
  * `updatevars` **(Many-Argument Workhorses)** (Impact: 200.7)
    * *Intent:* """ Returns last_name, the variable name without special chars, parenthesis or dimension specifiers....
  * `readfortrancode` **(Many-Argument Workhorses)** (Impact: 177.2)
    * *Intent:* # Read fortran (77,90) code """ Read fortran codes from files and 1) Get rid of comments, line conti...
  * `vars2fortran` **(Many-Argument Workhorses)** (Impact: 165.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 999 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 3180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 428`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 171`, `high_risk_execution: 9`, `state_mutation: 1182`, `dead_code: 4`, `planned_debt: 7`, `fragile_debt: 9`
* *Architecture:* `io: 20`, `api: 59`, `import: 12`
* *Defense:* `safety: 59`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , .auxfuncs, charset_normalizer, codecs, copy, fileinput, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/umath/ufunc_object.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5594.42 | **LOC:** 6807 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0829%), Tech Debt (13.0095%)
**Top Internal Functions/Classes:**
  * `PyUFunc_GeneralizedFunctionInternal` **(Many-Argument Workhorses)** (Impact: 251.3)
  * `PyUFunc_GenericReduction` **(Many-Argument Workhorses)** (Impact: 200.1)
    * *Intent:* /* * This code handles reduce, reduceat, and accumulate * (accumulate and reduce are special cases o...
  * `PyUFunc_Reduceat` **(Many-Argument Workhorses)** (Impact: 168.2)
    * *Intent:* * * if indices[i+1] <= indices[i]+1 * then the result is array[indices[i]] for that value * * op.acc...
  * `ufunc_generic_fastcall` **(Many-Argument Workhorses)** (Impact: 166.3)
    * *Intent:* /* * Main ufunc call implementation. * * This implementation makes use of the "fastcall" way of pass...
  * `PyUFunc_Accumulate` **(Many-Argument Workhorses)** (Impact: 166.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 768 instances
* *State Mutation (weighted view):* 2387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1055`, `structural_boundaries: 331`, `args: 208`, `func_start: 86`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 851`, `dead_code: 4`, `planned_debt: 17`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 16`, `import: 34`
* *Defense:* `safety: 18`, `doc: 16`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` Python.h, abstractdtypes.h, alloc.h, arrayobject.h, arraywrap.h, common.h, conversion_utils.h, convert_datatype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/ma/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5412.16 | **LOC:** 8930 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.0459%), Tech Debt (10.3435%)
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 180.2)
  * `var` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* """ x.__getitem__(y) <==> x[y] Return the item described by i, as a masked array. """
  * `__setitem__` **(Many-Argument Workhorses)** (Impact: 47.4)
    * *Intent:* # setitem may put NaNs into integer arrays or occasionally overflow a # float. But this may happen i...
  * `__setmask__` **(Many-Argument Workhorses)** (Impact: 45.5)
    * *Intent:* """ Set the mask. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 796 instances
* *State Mutation (weighted view):* 2610
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 788`, `structural_boundaries: 787`, `args: 268`, `func_start: 267`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1018`, `dead_code: 8`, `planned_debt: 7`, `fragile_debt: 4`
* *Architecture:* `api: 186`, `import: 15`
* *Defense:* `safety: 131`, `doc: 204`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtins, copy, functools, inspect, numpy, numpy._core, numpy._core.numeric, numpy._core.numerictypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend/ninjabackend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4966.32 | **LOC:** 4107 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1108%), Tech Debt (34.0097%)
**Top Internal Functions/Classes:**
  * `generate_single_compile` **(Many-Argument Workhorses)** (Impact: 163.8)
  * `generate_target` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `generate_link` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `get_rust_compiler_deps_and_args` **(Many-Argument Workhorses)** (Impact: 92.1)
  * `generate_swift_target` **(Many-Argument Workhorses)** (Impact: 68.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 744 instances
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 2450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 907`, `structural_boundaries: 499`, `args: 164`, `func_start: 161`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 113`, `high_risk_execution: 4`, `state_mutation: 962`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 20`, `unreferenced_by_name: 3`
* *Architecture:* `io: 176`, `api: 153`, `import: 41`
* *Defense:* `safety: 117`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` , .., .._typing, ..arglist, ..build, ..compilers, ..compilers.c, ..compilers.cs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/fft/pocketfft/pocketfft_hdronly.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4054.78 | **LOC:** 3636 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6374%), Tech Debt (21.1887%)
**Top Internal Functions/Classes:**
  * `radbg` **(Many-Argument Workhorses)** (Impact: 105.7)
  * `radfg` **(Many-Argument Workhorses)** (Impact: 100.4)
    * *Intent:* #undef POCKETFFT_REARRANGE
  * `passg` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* #undef POCKETFFT_PARTSTEP11 #undef POCKETFFT_PARTSTEP11a0 #undef POCKETFFT_PARTSTEP11a #undef POCKET...
  * `exec` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `general_c2r` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 693 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 2153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 621`, `structural_boundaries: 781`, `args: 280`, `func_start: 192`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 767`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 35`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 31`, `doc: 1`, `sync_locks: 36`, `immutability_locks: 311`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.496
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00091
  * `Imports (Out-Degree: 0):` algorithm, array, atomic, cmath, complex, condition_variable, cstdlib, functional...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/interpreter/interpreter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4020.54 | **LOC:** 3612 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3757%), Tech Debt (10.2662%)
**Top Internal Functions/Classes:**
  * `build_target` **(Many-Argument Workhorses)** (Impact: 128.8)
  * `func_configure_file` **(Many-Argument Workhorses)** (Impact: 112.7)
  * `func_custom_target` **(Many-Argument Workhorses)** (Impact: 91.8)
  * `func_project` **(Many-Argument Workhorses)** (Impact: 86.3)
  * `run_command_impl` **(Many-Argument Workhorses)** (Impact: 73.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 473 instances
* *State Mutation (weighted view):* 1555
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 829`, `structural_boundaries: 526`, `args: 155`, `func_start: 150`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 609`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 88`, `api: 135`, `import: 62`
* *Defense:* `safety: 174`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` , .., ..ast, ..backend, ..backend.backends, ..cmake, ..dependencies, ..dependencies.pkgconfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/tests/test_umath.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4011.22 | **LOC:** 4976 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.6722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__array_ufunc__` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `test_division_int_boundary` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `test_ufunc_override_with_super` **(Compute Cores)** (Impact: 44.0)
    * *Intent:* # NOTE: this class is used in doc/source/user/basics.subclassing.rst # if you make any changes here,...
  * `test_out_wrap_subok` **(Defensive Guards)** (Impact: 32.0)
  * `test_loss_of_precision` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* """Check loss of precision in complex arc* functions"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 543 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 814`, `args: 380`, `func_start: 345`, `class_start: 97`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 1088`, `dead_code: 4`, `fragile_debt: 10`, `duplicate_logic: 14`, `unreferenced_by_name: 227`
* *Architecture:* `io: 9`, `api: 364`, `import: 20`
* *Defense:* `safety: 116`, `doc: 12`, `test: 414`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cmath, collections, decimal, fnmatch, fractions, functools, inspect, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/multiarray/datetime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3743.9 | **LOC:** 4376 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.2732%), Tech Debt (19.2793%)
**Top Internal Functions/Classes:**
  * `convert_pyobject_to_timedelta` **(Many-Argument Workhorses)** (Impact: 174.2)
    * *Intent:* * Converts a PyObject * into a timedelta, in any of the forms supported * * If the units metadata is...
  * `datetime_arange` **(Many-Argument Workhorses)** (Impact: 123.8)
  * `NpyDatetime_ConvertPyDateTimeToDatetimeStruct` **(Many-Argument Workhorses)** (Impact: 113.1)
    * *Intent:* * While the C API has PyDate_* and PyDateTime_* functions, the following * implementation just asks ...
  * `convert_pyobject_to_datetime` **(Many-Argument Workhorses)** (Impact: 109.6)
    * *Intent:* * Converts a PyObject * into a datetime, in any of the forms supported. * * If the units metadata is...
  * `compute_datetime_metadata_greatest_common_divisor` **(Many-Argument Workhorses)** (Impact: 98.1)
    * *Intent:* /* * Computes the GCD of the two date-time metadata values. Raises * an exception if there is no rea...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 529 instances
* *State Mutation (weighted view):* 1631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 813`, `structural_boundaries: 377`, `args: 126`, `func_start: 68`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 573`, `dead_code: 2`, `planned_debt: 6`, `unreferenced_by_name: 19`
* *Architecture:* `api: 51`, `import: 16`
* *Defense:* `safety: 14`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.399
  * `Choke Point (Betweenness):` 0.000115 | `Ripple Effect (Closeness):` 0.007301
  * `Imports (Out-Degree: 13):` Python.h, _datetime.h, array_method.h, common.h, convert_datatype.h, datetime.h, datetime_strings.h, dtype_transfer.h...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/__init__.pyi` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3609.92 | **LOC:** 6203 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.8603%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 1824`, `args: 1598`, `func_start: 1598`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 291`, `state_mutation: 97`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 212`
* *Architecture:* `io: 5`, `api: 381`, `import: 59`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ._expired_attrs_2_0, ._globals, _typeshed, abc, array, builtins, collections.abc, ctypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/MathJax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 3529.72 | **LOC:** 3314 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.1465%), Tech Debt (36.9255%)
**Top Internal Functions/Classes:**
  * `processString` **(Defensive Guards)** (Impact: 79.5)
  * `Set` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `USING` **(Defensive Guards)** (Impact: 48.3)
    * *Intent:* // // Create a callback from various types of data //
  * `Firefox` **(Defensive Guards)** (Impact: 42.2)
  * `Clear` **(Defensive Guards)** (Impact: 36.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 522 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 1662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 902`, `structural_boundaries: 535`, `args: 252`, `func_start: 227`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 8`, `state_mutation: 618`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `concurrency: 13`
* *Defense:* `safety: 244`, `doc: 13`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3503.74 | **LOC:** 5304 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.6394%), Tech Debt (13.1346%)
**Top Internal Functions/Classes:**
  * `_array_fromobject_generic` **(Many-Argument Workhorses)** (Impact: 115.2)
  * `PyArray_Where` **(Many-Argument Workhorses)** (Impact: 102.7)
    * *Intent:* /*NUMPY_API * Where */
  * `_multiarray_umath_exec` **(Compute Cores)** (Impact: 101.6)
  * `PyArray_MatrixProduct2` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* /*NUMPY_API * Numeric.matrixproduct2(a,v,out) * just like inner product but does the swapaxes stuff ...
  * `array_shares_memory_impl` **(Many-Argument Workhorses)** (Impact: 68.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 466 instances
* *State Mutation (weighted view):* 1444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 769`, `structural_boundaries: 384`, `args: 290`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 512`, `dead_code: 2`, `planned_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `api: 31`, `import: 61`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` Python.h, __multiarray_api.c, __ufunc_api.c, _datetime.h, abstractdtypes.h, alloc.h, array_assign.h, array_coercion.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3478.24 | **LOC:** 5458 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5214%), Tech Debt (18.4305%)
**Top Internal Functions/Classes:**
  * `test_compiler_detection` **(Compute Cores)** (Impact: 71.6)
    * *Intent:* ''' Test that automatic compiler detection and setting from the environment both work just fine. Thi...
  * `test_introspect_json_dump` **(Compute Cores)** (Impact: 67.1)
  * `test_always_prefer_c_compiler_for_asm` **(Compute Cores)** (Impact: 38.6)
  * `test_install_tag` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* ## And one that doesn't #with mock.patch.object(cc_type, 'INVOKES_LINKER', False): # env.coredata.ge...
  * `test_long_output` **(Compute Cores)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 8 instances
* *Amplified Cascading Flux:* 413 instances
* *High Risk Execution (weighted view):* 9
* *Sec Tainted Injection (weighted view):* 8
* *State Mutation (weighted view):* 1732
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 648`, `args: 247`, `func_start: 236`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 11`, `state_mutation: 906`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 13`, `duplicate_logic: 3`
* *Architecture:* `io: 540`, `api: 230`, `import: 46`
* *Defense:* `safety: 80`, `doc: 65`, `test: 201`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.292
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000455
  * `Imports (Out-Degree: 24):` .baseplatformtests, .helpers, contextlib, glob, json, library, libs, lxml.etree...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/SVG/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3416.32 | **LOC:** 2268 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3452%), Tech Debt (54.0049%)
**Top Internal Functions/Classes:**
  * `Add` **(Many-Argument Workhorses)** (Impact: 113.3)
  * `HandleVariant` **(Many-Argument Workhorses)** (Impact: 106.0)
  * `toSVG` **(Compute Cores)** (Impact: 75.1)
  * `length2em` **(Defensive Guards)** (Impact: 57.2)
  * `preTranslate` **(Compute Cores)** (Impact: 53.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 585 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 383`, `args: 116`, `func_start: 110`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 2`, `state_mutation: 677`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 4`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 138`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/npysort/timsort.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 3365.16 | **LOC:** 2927 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.1513%), Tech Debt (63.8275%)
**Top Internal Functions/Classes:**
  * `npy_atry_collapse` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `npy_try_collapse` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `npy_acount_run` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* /* argsort */
  * `npy_count_run` **(Many-Argument Workhorses)** (Impact: 48.0)
  * `atry_collapse_` **(Many-Argument Workhorses)** (Impact: 45.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 581 instances
* *State Mutation (weighted view):* 1766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 441`, `args: 73`, `func_start: 105`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 604`, `planned_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 54`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cstdlib, npy_sort.h, npysort_common.h, numpy_tag.h, utility
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/multiarray/ctors.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3261.52 | **LOC:** 4208 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8233%), Tech Debt (20.0854%)
**Top Internal Functions/Classes:**
  * `PyArray_NewFromDescr_int` **(Many-Argument Workhorses)** (Impact: 232.5)
    * *Intent:* /* * Generic new array creation routine. * Internal variant with calloc argument for PyArray_Zeros. ...
  * `PyArray_FromAny_int` **(Many-Argument Workhorses)** (Impact: 112.0)
    * *Intent:* /* * Internal version of PyArray_FromAny that accepts a dtypemeta. Borrows * references to the descr...
  * `PyArray_FromInterface` **(Compute Cores)** (Impact: 108.6)
    * *Intent:* /*NUMPY_API*/
  * `PyArray_NewLikeArrayWithShape` **(Many-Argument Workhorses)** (Impact: 98.9)
    * *Intent:* * ndim - If not -1, overrides the shape of the result. * dims - If ndim is not -1, overrides the sha...
  * `PyArray_ArangeObj` **(Many-Argument Workhorses)** (Impact: 95.5)
    * *Intent:* /*NUMPY_API * * ArangeObj, * * this doesn't change the references */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 416 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 703`, `structural_boundaries: 281`, `args: 160`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 432`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 45`, `import: 29`
* *Defense:* `safety: 17`, `doc: 3`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` Python.h, _datetime.h, alloc.h, array_assign.h, array_coercion.h, arrayobject.h, assert.h, common.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/mtest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3238.86 | **LOC:** 2319 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.6171%), Tech Debt (16.9045%)
**Top Internal Functions/Classes:**
  * `log` **(Many-Argument Workhorses)** (Impact: 97.5)
    * *Intent:* """Log a single test case."""
  * `parse_line` **(Compute Cores)** (Impact: 88.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `_run_tests` **(Defensive Guards)** (Impact: 51.6)
  * `parse` **(Defensive Guards)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 10 instances
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 352 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 452
* *Sec Tainted Injection (weighted view):* 10
* *State Mutation (weighted view):* 1178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 470`, `args: 149`, `func_start: 147`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 11`, `state_mutation: 474`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 47`, `api: 157`, `concurrency: 112`, `import: 33`
* *Defense:* `safety: 64`, `doc: 6`, `test: 4`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.000455
  * `Imports (Out-Degree: 7):` , .backend.backends, .coredata, .mesonlib, .options, .programs, __future__, argparse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/_core/src/multiarray/dtype_transfer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3182.76 | **LOC:** 3835 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.7201%), Tech Debt (22.547%)
**Top Internal Functions/Classes:**
  * `get_subarray_broadcast_transfer_function` **(Many-Argument Workhorses)** (Impact: 124.2)
  * `get_legacy_dtype_cast_function` **(Many-Argument Workhorses)** (Impact: 123.3)
  * `PyArray_PrepareThreeRawArrayIter` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* * operands instead of one. Any broadcasting of the three operands * should have already been done be...
  * `get_fields_transfer_function` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* /* * Handles fields transfer. To call this, at least one of the dtypes * must have fields. Does not ...
  * `define_cast_for_descrs` **(Many-Argument Workhorses)** (Impact: 74.0)
    * *Intent:* * NOTE: In theory casting errors here could be slightly misleading in case * of a multi-step casting...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 455 instances
* *State Mutation (weighted view):* 1535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 253`, `args: 118`, `func_start: 78`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 625`, `planned_debt: 7`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `api: 34`, `import: 19`
* *Defense:* `safety: 10`, `doc: 13`, `immutability_locks: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, _datetime.h, alloc.h, array_assign.h, array_coercion.h, array_method.h, convert_datatype.h, ctors.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/ma/tests/test_core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3175.06 | **LOC:** 6016 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3849%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pickling` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* # Tests pickling for dtype in (int, float, str, object): a = arange(10).astype(dtype) a.fill_value =...
  * `test_inplace_division_array_type` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* # Test of inplace division othertypes, uint8data = self._create_otherdata() with warnings.catch_warn...
  * `test_inplace_division_scalar_type` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* # Test of inplace division othertypes, uint8data = self._create_otherdata() with warnings.catch_warn...
  * `test_eq_ne_structured_extra` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* # ensure simple examples are symmetric and make sense. # from https://github.com/numpy/numpy/pull/85...
  * `test_ndarrayfuncs` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* # test axis arg behaves the same as ndarray (including multiple axes) d = np.arange(24.0).reshape((2...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 141 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 1839
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 559`, `args: 361`, `func_start: 354`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 1557`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 315`
* *Architecture:* `io: 1`, `api: 355`, `import: 26`
* *Defense:* `safety: 116`, `doc: 10`, `test: 383`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` copy, datetime, functools, inspect, io, itertools, numpy, numpy._core.fromnumeric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/multiarray/item_selection.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3080.5 | **LOC:** 3362 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.1562%), Tech Debt (19.9585%)
**Top Internal Functions/Classes:**
  * `_new_argsortlike` **(Many-Argument Workhorses)** (Impact: 156.9)
  * `_new_sortlike` **(Many-Argument Workhorses)** (Impact: 145.9)
    * *Intent:* /* * These algorithms use special sorting. They are not called unless the * underlying sort function...
  * `npy_fasttake_impl` **(Many-Argument Workhorses)** (Impact: 134.3)
    * *Intent:* #include "ctors.h" #include "lowlevel_strided_loops.h" #include "array_assign.h" #include "refcount....
  * `PyArray_PutTo` **(Many-Argument Workhorses)** (Impact: 131.7)
    * *Intent:* /*NUMPY_API * Put values into an array */
  * `PyArray_LexSort` **(Many-Argument Workhorses)** (Impact: 120.1)
    * *Intent:* /*NUMPY_API *LexSort an array providing indices that will sort a collection of arrays *lexicographic...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 458 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 159`, `args: 137`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 504`, `dead_code: 4`, `planned_debt: 3`, `unreferenced_by_name: 18`
* *Architecture:* `api: 20`, `import: 25`
* *Defense:* `safety: 3`, `immutability_locks: 62`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` Python.h, alloc.h, array_assign.h, array_coercion.h, arrayobject.h, arraytypes.h, common.h, ctors.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/distutils/system_info.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2959.06 | **LOC:** 3268 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.5236%), Tech Debt (24.2647%)
**Top Internal Functions/Classes:**
  * `get_paths` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `calc_info` **(Compute Cores)** (Impact: 38.5)
  * `_parse_env_order` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* """ Parse an environment variable `env` by splitting with "," and only returning elements from `base...
  * `calc_info` **(Compute Cores)** (Impact: 29.6)
    * *Intent:* # Make possible to enable/disable from config file/env var libraries = os.environ.get('ACCELERATE') ...
  * `calc_info` **(Compute Cores)** (Impact: 27.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 504 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 1792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 506`, `args: 113`, `func_start: 112`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 88`, `high_risk_execution: 1`, `state_mutation: 784`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 153`, `api: 171`, `import: 35`
* *Defense:* `safety: 50`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.008804
  * `Imports (Out-Degree: 7):` .cpuinfo, Numeric, configparser, copy, distutils.ccompiler, distutils.dist, distutils.errors, distutils.util...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `numpy-2.4.4/vendored-meson/meson/mesonbuild/utils/universal.py` -> **Severity: 0.075** (Bridge: 0.0008 * Flux: 100.0%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/linkers/linkers.py` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 99.9926%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/c.py` -> **Severity: 0.071** (Bridge: 0.0007 * Flux: 100.0%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/compilers.py` -> **Severity: 0.07** (Bridge: 0.0007 * Flux: 99.9997%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/coredata.py` -> **Severity: 0.045** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `numpy-2.4.4/vendored-meson/meson/mesonbuild/mesonlib.py` -> **Severity: 5.551** (Embedded: 0.0641 * Error Risk: 86.6293%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/_typing.py` -> **Severity: 4.27** (Embedded: 0.0471 * Error Risk: 90.7207%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/compilers.py` -> **Severity: 3.897** (Embedded: 0.0439 * Error Risk: 88.864%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/utils/core.py` -> **Severity: 3.722** (Embedded: 0.0386 * Error Risk: 96.508%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/utils/universal.py` -> **Severity: 3.717** (Embedded: 0.0387 * Error Risk: 96.0014%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `numpy-2.4.4/numpy/_core/src/highway/hwy/base.h` -> **Severity: 1045.6** (Blast Radius: 10.456 * Doc Risk: 100.0%)
- `numpy-2.4.4/numpy/_core/include/numpy/ndarraytypes.h` -> **Severity: 1037.0** (Blast Radius: 10.37 * Doc Risk: 100.0%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/compilers/compilers.py` -> **Severity: 968.278** (Blast Radius: 11.127 * Doc Risk: 87.0206%)
- `numpy-2.4.4/numpy/core/_utils.py` -> **Severity: 825.4** (Blast Radius: 8.254 * Doc Risk: 100.0%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/_typing.py` -> **Severity: 812.8** (Blast Radius: 8.128 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
