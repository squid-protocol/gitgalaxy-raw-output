# ARCHITECTURAL_BRIEF: scipy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/scipy/scipy.git` |
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
| Total Artifacts | 3031 |
| Analyzed Artifacts (Scanned) | 1992 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1039 |
| Total LOC | 486134 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 65.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7326 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1834 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.2823 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 191 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1203 | 316000 | 60.4% |
| C | 415 | 125551 | 20.8% |
| PLAINTEXT | 174 | 82 | 8.7% |
| CPP | 116 | 34961 | 5.8% |
| MARKDOWN | 43 | 0 | 2.2% |
| SHELL | 9 | 216 | 0.5% |
| XML | 7 | 0 | 0.4% |
| FORTRAN | 6 | 8433 | 0.3% |
| JSON | 5 | 399 | 0.3% |
| MAKEFILE | 4 | 234 | 0.2% |
| MATLAB | 4 | 76 | 0.2% |
| CSS | 1 | 76 | 0.1% |
| HTML | 1 | 11 | 0.1% |
| YAML | 1 | 51 | 0.1% |
| M4 | 1 | 1 | 0.1% |
| OBJECTIVE-C | 1 | 18 | 0.1% |
| BATCH | 1 | 25 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1775 | 89.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 195 | 9.8% |
| Static: Minified & Vendor Opaque Mass | 22 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1039*

**Composition by Extension & Reason:**
- `.rst`: 329x Excluded (Unsupported Extension: '.rst'), 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 141x Excluded (Unsupported Extension: '.npz')
- `.mat`: 113x Excluded (Unsupported Extension: '.mat')
- `.build`: 105x Excluded (Unsupported Extension: '.build')
- `.sav`: 48x Excluded (Unsupported Extension: '.sav')
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 26x Excluded (Unsupported Extension: '.dat')
- `.txt`: 2x Excluded (Lexical Monotony: High structural repetition detected in 6631 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2305 LOC), 1x Excluded (Machine-Generated Source Code Signature: 7 LOC)
- `.wav`: 22x Excluded (Explicitly Denied Extension: '.wav')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 118 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2273 LOC)
- `.arff`: 16x Excluded (Unsupported Extension: '.arff')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.src`: 15x Excluded (Unsupported Extension: '.src')
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.npy`: 6x Excluded (Unsupported Extension: '.npy')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 35.5 | 38.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 73.8 | 89.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.2 | 9.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 54.6 | 98.2 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 74.1 | 2.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.5 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 69.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 66778 | 935 | 53 | `subprojects/qhull_r/libqhull_r/merge_r.c` |
| cleanup | 483 | 106 | 0 | `scipy/interpolate/src/_fitpackmodule.c` |
| guards | 24277 | 1056 | 30 | `scipy/stats/_continuous_distns.py` |
| danger | 9473 | 880 | 12 | `scipy/interpolate/src/_fitpackmodule.c` |
| concurrency | 442 | 123 | 0 | `scipy/optimize/_shgo_lib/_complex.py` |
| connectivity | 26423 | 1491 | 31 | `scipy/stats/tests/test_distributions.py` |
| io | 1319 | 189 | 0 | `scipy/odr/odrpack/d_odr.f` |
| crypto | 5 | 4 | 0 | `tools/write_release_and_log.py` |
| ipc | 96 | 30 | 0 | `tools/lint.py` |
| time | 65 | 21 | 0 | `benchmarks/benchmarks/optimize.py` |
| serialization | 229 | 23 | 0 | `scipy/odr/odrpack/d_odr.f` |
| regex | 98 | 31 | 0 | `scipy/io/arff/_arffread.py` |
| events | 1189 | 115 | 0 | `scipy/integrate/__quadpack.h` |
| tests | 18700 | 354 | 14 | `scipy/stats/tests/test_stats.py` |
| docs | 7636 | 1037 | 9 | `scipy/special/cython_special.pyx` |
| debt | 2907 | 516 | 3 | `scipy/stats/_continuous_distns.py` |
| mutation | 307460 | 1559 | 358 | `scipy/integrate/_lebedev.py` |
| dead_code | 12001 | 1037 | 11 | `scipy/stats/tests/test_distributions.py` |
| credential | 1 | 1 | 0 | `tools/wheels/cibw_before_build.sh` |
| threat | 3563 | 548 | 4 | `scipy/interpolate/src/_fitpackmodule.c` |
| ml_ai | 8449 | 1226 | 9 | `scipy/sparse/sparsetools/csr.h` |
| ui | 3 | 1 | 0 | `doc/source/_static/scipy.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scipy/odr/odrpack/d_odr.f` (Hits: 372)
- `scipy/odr/odrpack/d_test.f` (Hits: 81)
- `scipy/io/matlab/tests/test_mio.py` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **scipy.css** (`doc/source/_static/scipy.css`) — 195 inbound connections
2. **_array_api.py** (`scipy/_lib/_array_api.py`) — 192 inbound connections
3. **sparse.py** (`benchmarks/benchmarks/sparse.py`) — 154 inbound connections
4. **_util.py** (`scipy/_lib/_util.py`) — 117 inbound connections
5. **deprecation.py** (`scipy/_lib/deprecation.py`) — 117 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **xsf_wrappers.cpp** (`scipy/special/xsf_wrappers.cpp`) — 49 outbound dependencies
2. **releasing.rst.inc** (`doc/source/dev/core-dev/releasing.rst.inc`) — 45 outbound dependencies
3. **_special_ufuncs.cpp** (`scipy/special/_special_ufuncs.cpp`) — 36 outbound dependencies
4. **conftest.py** (`scipy/conftest.py`) — 30 outbound dependencies
5. **__init__.py** (`scipy/stats/__init__.py`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `trlib_krylov_min_internal` (@ `scipy/optimize/_trlib/trlib_krylov.c`) -> Impact: **1249.0** | LOC: 656
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `fpsphe` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **1154.0** | LOC: 808
- `fpgrsp` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **1135.5** | LOC: 736
- `fpsurf` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **1073.4** | LOC: 821
- `lsoda` (@ `scipy/integrate/src/lsoda.c`) -> Impact: **933.6** | LOC: 714
  * *Intent:* * @param itol Tolerance type indicator (1-4). * @param rtol Relative tolerance array. * @param atol Absolute tolerance array. * @param itask Task indi...
- `fpclos` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **865.7** | LOC: 883
- `trlib_tri_factor_min` (@ `scipy/optimize/_trlib/trlib_tri_factor.c`) -> Impact: **765.4** | LOC: 390
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `fpperi` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **726.2** | LOC: 806
- `fpspgr` (@ `scipy/interpolate/src/dfitpack.c`) -> Impact: **712.6** | LOC: 482
- `preproc` (@ `subprojects/pyprima/pyprima/pyprima/src/pyprima/common/preproc.py`) -> Impact: **669.4** | LOC: 258

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scipy/sparse/linalg/_dsolve/SuperLU/SRC` | 193 | 64902.98 | 59.2% | 32.55% |
| `scipy/stats` | 71 | 48289.72 | 37.87% | 22.28% |
| `scipy/stats/tests` | 41 | 37102.62 | 33.69% | 0.0% |
| `subprojects/qhull_r/libqhull_r` | 30 | 28350.96 | 48.55% | 20.25% |
| `scipy/interpolate/src` | 5 | 27751.62 | 50.05% | 12.91% |
| `scipy/optimize` | 69 | 25526.58 | 39.05% | 23.21% |
| `scipy/integrate` | 20 | 20889.52 | 46.57% | 27.87% |
| `scipy/signal` | 45 | 19778.7 | 35.77% | 29.42% |
| `scipy/special` | 76 | 19473.48 | 24.01% | 40.63% |
| `scipy/optimize/tests` | 45 | 16610.28 | 27.69% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks/ndimage_interpolation.py` -> **100.0%** Exposure
- `scipy/_external/packaging_version/src/_structures.py` -> **100.0%** Exposure
- `scipy/ndimage/_delegators.py` -> **100.0%** Exposure
- `scipy/signal/_delegators.py` -> **100.0%** Exposure
- `scipy/spatial/_qhull.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cluster_hierarchy_disjoint_set.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cutest/calfun.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/cutest/dfovec.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scipy/stats/tests/test_stats.py` -> **481** Orphaned Functions | **0** Duplicates
- `scipy/stats/tests/test_distributions.py` -> **417** Orphaned Functions | **7** Duplicates
- `scipy/special/xsf_wrappers.cpp` -> **259** Orphaned Functions | **0** Duplicates
- `scipy/special/cython_special.pxd` -> **232** Orphaned Functions | **0** Duplicates
- `scipy/special/cython_special.pyx` -> **217** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `7102` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benchmarks/benchmarks/fft_basic.py` (PYTHON) -> Cumulative Risk: **773.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 460.8 | **LOC:** 355 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.6364%)
- **Heaviest Functions:** `setup` (Impact: 19.1), `setup` (Impact: 19.0), `setup` (Impact: 9.7)

### 2. `benchmarks/benchmarks/integrate.py` (PYTHON) -> Cumulative Risk: **758.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 300.0 | **LOC:** 405 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Cognitive Load (93.9464%)
- **Heaviest Functions:** `setup` (Impact: 30.4), `setup` (Impact: 8.5), `setup` (Impact: 3.9)

### 3. `benchmarks/benchmarks/sparse.py` (PYTHON) -> Cumulative Risk: **727.5**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 722.5 | **LOC:** 612 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2072%), Documentation (96.0784%)
- **Heaviest Functions:** `setup` (Impact: 25.9), `setup` (Impact: 18.7), `_timeit` (Impact: 17.1)

### 4. `benchmarks/benchmarks/linalg.py` (PYTHON) -> Cumulative Risk: **727.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 479.68 | **LOC:** 422 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.0155%)
- **Heaviest Functions:** `setup` (Impact: 30.7), `setup` (Impact: 12.4), `setup` (Impact: 12.0)

### 5. `benchmarks/benchmarks/signal.py` (PYTHON) -> Cumulative Risk: **706.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 279.74 | **LOC:** 246 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.9395%)
- **Heaviest Functions:** `time_convolve2d` (Impact: 10.3), `time_correlate2d` (Impact: 10.3), `time_convolve2d` (Impact: 9.0)

### 6. `benchmarks/benchmarks/signal_filtering.py` (PYTHON) -> Cumulative Risk: **697.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 100.62 | **LOC:** 121 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.6801%)
- **Heaviest Functions:** `time_sosfilt` (Impact: 4.3), `_medfilt2d` (Impact: 3.6), `setup` (Impact: 2.5)

### 7. `scipy/linalg/src/_common_array_utils.hh` (CPP) -> Cumulative Risk: **697.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 996.42 | **LOC:** 1586 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 74.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (96.5517%), Safety Score (96.1982%)
- **Heaviest Functions:** `bandwidth_strided` (Impact: 38.1), `bandwidth` (Impact: 33.3), `swap_cf` (Impact: 21.2)

### 8. `benchmarks/benchmarks/stats.py` (PYTHON) -> Cumulative Risk: **696.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 755.48 | **LOC:** 833 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9972%)
- **Heaviest Functions:** `setup` (Impact: 53.1), `setup` (Impact: 42.9), `time_distribution` (Impact: 33.4)

### 9. `scipy/fft/_basic_backend.py` (PYTHON) -> Cumulative Risk: **680.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 196.38 | **LOC:** 198 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.3791%)
- **Heaviest Functions:** `_execute_1D` (Impact: 13.8), `_execute_nD` (Impact: 13.8), `hfftn` (Impact: 9.0)

### 10. `scipy/spatial/_ckdtree.pyx` (PYTHON) -> Cumulative Risk: **679.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 915.46 | **LOC:** 1688 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 38.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1451%), Documentation (93.3333%)
- **Heaviest Functions:** `count_neighbors` (Impact: 86.7), `__init__` (Impact: 57.8), `query_ball_point` (Impact: 45.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scipy/interpolate/src/dfitpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 23760.5 | **LOC:** 9383 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 93.1%
- **Risk Profile:** Cognitive Load (73.8359%), Tech Debt (9.8653%)
**Top Internal Functions/Classes:**
  * `fpsphe` (Impact: 1154.0)
  * `fpgrsp` (Impact: 1135.5)
  * `fpsurf` (Impact: 1073.4)
  * `fpclos` (Impact: 865.7)
  * `fpperi` (Impact: 726.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4138 instances
* *State Mutation (weighted view):* 12705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1910`, `structural_boundaries: 568`, `args: 83`, `func_start: 52`
* *Risk/State:* `state_mutation: 4429`, `dead_code: 112`, `unreferenced_by_name: 20`
* *Architecture:* `api: 21`, `import: 1`
* *Defense:* `doc: 33`, `immutability_locks: 711`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dfitpack.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/__quadpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7383.18 | **LOC:** 6857 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.0914%), Tech Debt (8.8674%)
**Top Internal Functions/Classes:**
  * `dqawoe` (Impact: 403.5)
  * `dqagpe` (Impact: 402.6)
  * `dqagie` (Impact: 285.5)
    * *Intent:* // Constants static const double uflow = 2.2250738585072014e-308; /* np.finfo(np.float64).tiny */ st...
  * `dqagse` (Impact: 273.2)
  * `dqawfe` (Impact: 189.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1409 instances
* *State Mutation (weighted view):* 4569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 139`, `args: 48`, `func_start: 26`
* *Risk/State:* `state_mutation: 1751`, `dead_code: 42`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __quadpack.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/tests/test_stats.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7270.96 | **LOC:** 9891 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 82.0%
- **Risk Profile:** Cognitive Load (41.1364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_against_reference` (Impact: 66.0)
  * `wkq` (Impact: 35.0)
    * *Intent:* # Trivial quadratic implementation, all parameters mandatory
  * `test_quantile_test_iv` (Impact: 30.0)
  * `check_equal_xmean` (Impact: 29.1)
  * `check_power_divergence` (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 632 instances
* *State Mutation (weighted view):* 3718
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 1180`, `args: 643`, `func_start: 640`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2454`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 481`
* *Architecture:* `io: 4`, `api: 704`, `import: 28`
* *Defense:* `safety: 120`, `doc: 28`, `test: 1034`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .common_tests, collections, contextlib, hypothesis, hypothesis.extra.numpy, itertools, math, mpmath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_continuous_distns.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7209.56 | **LOC:** 12588 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 36.8%
- **Risk Profile:** Cognitive Load (62.4298%), Tech Debt (99.8097%)
**Top Internal Functions/Classes:**
  * `fit` (Impact: 127.2)
  * `fit` (Impact: 92.8)
    * *Intent:* # Summary of the strategy: # # 1) If the scale and location are fixed, return the shape according # ...
  * `_rvs_scalar` (Impact: 73.7)
    * *Intent:* # following [2], the quasi-pdf is used instead of the pdf for the # generation of rvs invert_res = F...
  * `fit` (Impact: 65.5)
  * `fit` (Impact: 57.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 668 instances
* *State Mutation (weighted view):* 2896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 2653`, `args: 1284`, `func_start: 1189`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1560`, `dead_code: 33`, `fragile_debt: 3`, `duplicate_logic: 126`
* *Architecture:* `api: 283`, `import: 26`
* *Defense:* `safety: 25`, `doc: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` , ._censored_data, ._constants, ._distn_infrastructure, ._ksstats, ._tukeylambda_stats, collections.abc, ctypes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scipy/stats/_stats_py.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6400.42 | **LOC:** 11252 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 81.2%
- **Risk Profile:** Cognitive Load (53.8929%), Tech Debt (9.9475%)
**Top Internal Functions/Classes:**
  * `_xp_mean` (Impact: 121.2)
  * `pearsonr` (Impact: 99.4)
  * `spearmanr` (Impact: 81.9)
  * `quantile_test_iv` (Impact: 69.4)
  * `_histogram` (Impact: 68.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1007 instances
* *State Mutation (weighted view):* 3371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 861`, `structural_boundaries: 491`, `args: 196`, `func_start: 158`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1357`, `dead_code: 11`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 101`, `import: 29`
* *Defense:* `safety: 22`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.828
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` , ._axis_nan_policy, ._binomtest, ._resampling, ._stats, ._stats_pythran, collections, collections.abc...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `scipy/special/cdflib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6331.3 | **LOC:** 5296 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (71.574%), Tech Debt (9.975%)
**Top Internal Functions/Classes:**
  * `bratio` (Impact: 232.0)
  * `gratio` (Impact: 215.0)
  * `gaminv` (Impact: 202.1)
  * `dinvr` (Impact: 120.1)
  * `dzror` (Impact: 73.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1379 instances
* *State Mutation (weighted view):* 4244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 808`, `structural_boundaries: 530`, `args: 120`, `func_start: 57`, `class_start: 53`
* *Risk/State:* `state_mutation: 1486`, `dead_code: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 57`, `import: 1`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cdflib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/odr/odrpack/d_odr.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5946.02 | **LOC:** 10986 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DODMN` (Impact: 183.2)
    * *Intent:* *DODMN
  * `DODPC1` (Impact: 154.8)
    * *Intent:* *DODPC1
  * `DODPC3` (Impact: 113.0)
    * *Intent:* *DODPC3
  * `DODCHK` (Impact: 103.0)
    * *Intent:* *DODCHK
  * `DSOLVE` (Impact: 89.1)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/optimize/src/minpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5633.66 | **LOC:** 4267 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (84.2185%), Tech Debt (10.513%)
**Top Internal Functions/Classes:**
  * `LMSTR` (Impact: 418.9)
  * `LMDIF` (Impact: 393.5)
  * `LMDER` (Impact: 392.9)
  * `HYBRD` (Impact: 368.1)
  * `HYBRJ` (Impact: 339.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 978 instances
* *State Mutation (weighted view):* 2966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 58`, `args: 28`, `func_start: 17`
* *Risk/State:* `state_mutation: 1010`, `dead_code: 36`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, minpack.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/tests/test_distributions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5458.16 | **LOC:** 10558 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (39.3585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fit` (Impact: 28.1)
  * `test_fit_mm` (Impact: 26.9)
  * `test_location_scale` (Impact: 26.1)
  * `test_pdf_nolan_samples` (Impact: 22.2)
  * `test_cdf_nolan_samples` (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 274 instances
* *State Mutation (weighted view):* 2504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 1195`, `args: 802`, `func_start: 753`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 1956`, `dead_code: 131`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 7`, `unreferenced_by_name: 417`
* *Architecture:* `io: 7`, `api: 848`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 186`, `doc: 29`, `test: 1004`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .test_discrete_basic, itertools, json, mpmath, numpy, numpy.lib.recfunctions, numpy.testing, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_distribution_infrastructure.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4989.56 | **LOC:** 5777 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 68.4%
- **Risk Profile:** Cognitive Load (76.5788%), Tech Debt (27.6781%)
**Top Internal Functions/Classes:**
  * `plot` (Impact: 141.8)
    * *Intent:* ### Convenience
  * `filtered` (Impact: 98.0)
  * `_set_invalid_nan` (Impact: 65.9)
    * *Intent:* # Wrapper for input / output validation and standardization of distribution # functions that accept ...
  * `_make_distribution_rv_generic` (Impact: 41.8)
  * `_moment_central_dispatch` (Impact: 39.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 633 instances
* *State Mutation (weighted view):* 2237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 654`, `structural_boundaries: 983`, `args: 459`, `func_start: 442`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 971`, `dead_code: 9`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `api: 126`, `import: 19`
* *Defense:* `safety: 34`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` abc, functools, inspect, math, matplotlib.pyplot, numpy, scipy, scipy._external...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `subprojects/qhull_r/libqhull_r/merge_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4718.1 | **LOC:** 5591 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3343%), Tech Debt (8.3295%)
**Top Internal Functions/Classes:**
  * `qh_mergefacet` (Impact: 203.1)
    * *Intent:* */
  * `qh_test_nonsimplicial_merge` (Impact: 180.9)
    * *Intent:* */
  * `qh_all_merges` (Impact: 117.5)
    * *Intent:* */
  * `qh_renamevertex` (Impact: 93.8)
    * *Intent:* */
  * `qh_appendmergeset` (Impact: 88.7)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/sparse/tests/test_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4642.98 | **LOC:** 5971 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (42.1671%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `with_64bit_maxval_limit` (Impact: 60.7)
  * `test_slicing_3` (Impact: 32.9)
  * `test_argmax` (Impact: 31.1)
  * `test_minmax_axis` (Impact: 29.1)
  * `sparse_test_class` (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 469 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 792`, `args: 362`, `func_start: 360`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 1`, `state_mutation: 1536`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 23`
* *Architecture:* `io: 1`, `api: 355`, `import: 24`
* *Defense:* `safety: 177`, `doc: 14`, `test: 308`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.344
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` contextlib, functools, itertools, numpy, numpy.exceptions, numpy.testing, operator, pickle...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy/linalg/src/_matfuncs_expm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4605.94 | **LOC:** 2912 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (72.3885%), Tech Debt (9.1962%)
**Top Internal Functions/Classes:**
  * `pade_UV_calc_c` (Impact: 151.4)
  * `pade_UV_calc_z` (Impact: 151.1)
  * `pick_pade_structure_z` (Impact: 123.2)
  * `pick_pade_structure_c` (Impact: 123.1)
  * `pick_pade_structure_s` (Impact: 118.1)
    * *Intent:* /******************************************************************************* *******************...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 36 instances
* *Amplified Cascading Flux:* 994 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 126`, `args: 188`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1182`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 68`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _common_array_utils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/qhull_r/libqhull_r/io_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4498.6 | **LOC:** 4129 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5995%), Tech Debt (12.3102%)
**Top Internal Functions/Classes:**
  * `qh_printbegin` (Impact: 354.2)
    * *Intent:* */
  * `qh_readpoints` (Impact: 321.3)
    * *Intent:* */
  * `qh_printafacet` (Impact: 172.8)
    * *Intent:* */
  * `qh_printfacetheader` (Impact: 144.8)
    * *Intent:* */
  * `qh_printfacets` (Impact: 112.1)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/_lebedev.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4248.32 | **LOC:** 5454 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.7454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_lebedev_sphere` (Impact: 69.0)
    * *Intent:* # getLebedevSphere # @author Rob Parrish, The Sherrill Group, CCMST Georgia Tech # @email robparrish...
  * `get_lebedev_recurrence_points` (Impact: 32.3)
  * `lebedev_rule` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 4035
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3735`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` matplotlib.pyplot, numpy, scipy._lib._array_api, scipy.integrate
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy/optimize/src/lbfgsb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4228.2 | **LOC:** 3769 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (68.6281%), Tech Debt (8.1911%)
**Top Internal Functions/Classes:**
  * `cauchy` (Impact: 339.9)
  * `mainlb` (Impact: 273.8)
  * `subsm` (Impact: 224.1)
  * `lnsrlb` (Impact: 202.4)
  * `dcsrch` (Impact: 178.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 712 instances
* *State Mutation (weighted view):* 2289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 92`, `args: 38`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 865`, `dead_code: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lbfgsb.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/integrate/src/zvode.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4059.98 | **LOC:** 2785 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (68.5177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `zvode` (Impact: 658.0)
    * *Intent:* * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @param iopt Optional...
  * `zvstep` (Impact: 397.2)
    * *Intent:* * @param wm Complex work array for matrix operations * @param iwm Integer work array for matrix oper...
  * `zvjac` (Impact: 288.4)
    * *Intent:* * @param wm Complex work space for matrices. On output contains the inverse * diagonal matrix if MIT...
  * `zvnlsd` (Impact: 208.5)
    * *Intent:* * @param y Complex predicted solution vector, updated by corrector * @param yh Complex Nordsieck his...
  * `zvhin` (Impact: 95.0)
    * *Intent:* * @param f User function for right-hand side f(t,y) * @param rpar User real work array * @param ipar...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 663 instances
* *State Mutation (weighted view):* 2094
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 163`, `args: 165`, `func_start: 14`
* *Risk/State:* `state_mutation: 768`, `dead_code: 3`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 12`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, math.h, stdlib.h, zvode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/qhull_r/libqhull_r/poly2_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3821.74 | **LOC:** 3960 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (78.6727%), Tech Debt (16.3354%)
**Top Internal Functions/Classes:**
  * `qh_checkfacet` (Impact: 206.9)
    * *Intent:* */
  * `qh_matchdupridge` (Impact: 197.7)
    * *Intent:* */
  * `qh_checkpolygon` (Impact: 123.7)
    * *Intent:* */
  * `qh_checklists` (Impact: 93.5)
    * *Intent:* */
  * `qh_check_maxout` (Impact: 88.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qhull_ra.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/stats/_multivariate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3776.08 | **LOC:** 8050 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (47.1538%), Tech Debt (92.4969%)
**Top Internal Functions/Classes:**
  * `_process_parameters` (Impact: 75.3)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure conformality. Par...
  * `_process_parameters` (Impact: 61.4)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure compatible dimens...
  * `_process_parameters` (Impact: 54.3)
    * *Intent:* """ Infer dimensionality from location array and shape matrix, handle defaults, and ensure compatibl...
  * `_process_parameters_psd` (Impact: 54.1)
    * *Intent:* # Try to infer dimensionality if dim is None: if mean is None: if cov is None: dim = 1 else: cov = n...
  * `_dirichlet_check_input` (Impact: 33.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 435 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1765
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 677`, `args: 309`, `func_start: 309`, `class_start: 39`
* *Risk/State:* `state_mutation: 895`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 205`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 9`, `doc: 216`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.386
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` , ._continuous_distns, ._discrete_distns, ._morestats, ._qmvnt, math, matplotlib.colors, matplotlib.pyplot...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scipy/integrate/src/lsoda.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3702.74 | **LOC:** 2322 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (81.7993%), Tech Debt (8.5913%)
**Top Internal Functions/Classes:**
  * `lsoda` (Impact: 933.6)
    * *Intent:* * @param itol Tolerance type indicator (1-4). * @param rtol Relative tolerance array. * @param atol ...
  * `stoda` (Impact: 343.2)
    * *Intent:* * * @param neq Pointer to the number of equations. * @param y Array containing the current solution ...
  * `stoda_corrector_loop` (Impact: 131.7)
    * *Intent:* /** * @brief Main corrector loop factored out from stoda code. Implements (roughly) labels 200-410 *...
  * `prja` (Impact: 113.2)
    * *Intent:* * @param savf Array containing f evaluated at predicted y. * @param wm Real work space for matrices....
  * `intdy` (Impact: 41.8)
    * *Intent:* * @brief Computes interpolated values of y and its derivatives. * * This function computes the k-th ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 616 instances
* *State Mutation (weighted view):* 1937
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 157`, `args: 107`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 705`, `dead_code: 18`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 21`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, lsoda.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/signal/tests/test_signaltools.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3699.3 | **LOC:** 4783 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 52.9%
- **Risk Profile:** Cognitive Load (40.2788%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_resample_methods` (Impact: 43.1)
    * *Intent:* # Test resampling of sinusoids and random noise (1-sec) rate = 100 rates_to = [49, 50, 51, 99, 100, ...
  * `test_convolve_method` (Impact: 26.1)
    * *Intent:* # this types data structure was manually encoded instead of # using custom filters on the soon-to-be...
  * `test_invalid_flags` (Impact: 23.4)
  * `test_envelope_invalid_parameters` (Impact: 22.1)
    * *Intent:* """For `envelope()` Raise all exceptions that are used to verify function parameters. """
  * `test_detrend_array_bp` (Impact: 19.0)
    * *Intent:* # regression test for https://github.com/scipy/scipy/issues/18675 rng = np.random.RandomState(12345)...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 398 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 2031
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 573`, `args: 285`, `func_start: 283`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1235`, `dead_code: 7`, `planned_debt: 3`, `fragile_debt: 33`, `duplicate_logic: 4`, `unreferenced_by_name: 200`
* *Architecture:* `io: 1`, `api: 311`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 154`, `doc: 28`, `test: 411`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` concurrent.futures, itertools, math, numpy, numpy.exceptions, pytest, scipy, scipy._lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/optimize/_optimize.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3678.56 | **LOC:** 4170 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (73.8776%), Tech Debt (8.6513%)
**Top Internal Functions/Classes:**
  * `_minimize_neldermead` (Impact: 257.4)
  * `_minimize_powell` (Impact: 169.1)
  * `_minimize_newtoncg` (Impact: 125.0)
  * `_minimize_bfgs` (Impact: 118.1)
  * `_minimize_scalar_bounded` (Impact: 106.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 578 instances
* *State Mutation (weighted view):* 1840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 248`, `args: 69`, `func_start: 68`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 2`, `state_mutation: 684`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 46`, `import: 16`
* *Defense:* `safety: 22`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.49
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ._linesearch, ._numdiff, math, matplotlib.pyplot, mpl_toolkits.mplot3d, numpy, scipy, scipy._external...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `scipy/special/tests/test_basic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3494.86 | **LOC:** 4863 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (35.1972%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_factorial_array_corner_cases` (Impact: 94.7)
  * `test_factorial2_array_corner_cases` (Impact: 81.2)
    * *Intent:* # get dtype without calling array constructor (that might fail or mutate) if dtype == np.int64 and a...
  * `test_factorialk_array_corner_cases` (Impact: 81.2)
    * *Intent:* # get dtype without calling array constructor (that might fail or mutate) if dtype == np.int64 and a...
  * `test_factorialx_inf_nan` (Impact: 67.7)
    * *Intent:* # NaNs not allowed (by dtype) for exact=True kw = {"exact": False, "extend": extend} if factorialx =...
  * `test_factorial_scalar_corner_cases` (Impact: 41.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 1117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 780`, `args: 519`, `func_start: 513`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 727`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 539`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 47`, `doc: 20`, `test: 640`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` functools, itertools, math, mpmath, numpy, numpy.testing, operator, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy/signal/_signaltools.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3487.16 | **LOC:** 5343 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 23.8%
- **Risk Profile:** Cognitive Load (53.4%), Tech Debt (10.5715%)
**Top Internal Functions/Classes:**
  * `envelope` (Impact: 127.6)
  * `oaconvolve` (Impact: 97.6)
    * *Intent:* """Convolve two N-dimensional arrays using the overlap-add method. Convolve `in1` and `in2` using th...
  * `lfilter` (Impact: 81.3)
    * *Intent:* """ Filter data along one-dimension with an IIR or FIR filter. Filter a data sequence, `x`, using a ...
  * `resample` (Impact: 80.9)
  * `resample_poly` (Impact: 75.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 599 instances
* *State Mutation (weighted view):* 1856
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 231`, `args: 59`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 658`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 34`, `import: 24`
* *Defense:* `safety: 12`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.884
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` , ._arraytools, ._filter_design, ._fir_filter_design, ._ltisys, ._sosfilt, ._upfirdn, .windows...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy/stats/tests/test_multivariate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3476.14 | **LOC:** 5053 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (40.5189%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pmf_logpmf` (Impact: 35.9)
    * *Intent:* # The pmf is tested through random sample generation # with Boyett's algorithm, whose implementation...
  * `test_bad_input` (Impact: 34.3)
    * *Intent:* # Check that bad inputs raise errors num_rows = 4 num_cols = 3 df = 5 M = np.full((num_rows, num_col...
  * `test_marginal_distribution` (Impact: 18.2)
  * `test_covariance` (Impact: 16.3)
  * `test_cdf_vs_univariate_singular` (Impact: 14.7)
    * *Intent:* # NB: ndim = 2, 3 has much poorer accuracy than ndim > 3 for many seeds. # No idea why. rng = np.ran...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 296 instances
* *State Mutation (weighted view):* 2106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 548`, `args: 286`, `func_start: 280`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1514`, `dead_code: 18`, `duplicate_logic: 4`, `unreferenced_by_name: 172`
* *Architecture:* `api: 294`, `import: 23`
* *Defense:* `safety: 92`, `doc: 20`, `test: 421`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .common_tests, .data._mvt, .test_continuous_basic, dataclasses, matplotlib, mpmath, numpy, numpy.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scipy/stats/_stats_py.py` -> Churn: **100.0%** | Cog Load: 53.8929% | Debt: 9.9475%
- `scipy/stats/_morestats.py` -> Churn: **86.62%** | Cog Load: 63.6388% | Debt: 30.8684%
- `scipy/linalg/_basic.py` -> Churn: **83.37%** | Cog Load: 58.0807% | Debt: 22.0646%
- `scipy/linalg/src/_common_array_utils.hh` -> Churn: **78.87%** | Cog Load: 78.4376% | Debt: 9.0103%
- `scipy/linalg/src/_batched_linalg_module.cc` -> Churn: **74.14%** | Cog Load: 75.1811% | Debt: 8.6775%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scipy/interpolate/src/dfitpack.c` -> **ilayn** (93.1% isolated ownership) | Magnitude: 23760.5
- `scipy/stats/tests/test_stats.py` -> **Matt Haberland** (82.0% isolated ownership) | Magnitude: 7270.96
- `scipy/stats/_stats_py.py` -> **Matt Haberland** (81.2% isolated ownership) | Magnitude: 6400.42
- `subprojects/qhull_r/libqhull_r/poly2_r.c` -> **Lucas Roberts** (100.0% isolated ownership) | Magnitude: 3821.74
- `scipy/optimize/tnc/tnc.c` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 3057.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scipy/_lib/_array_api.py` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `scipy/_lib/_util.py` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `scipy/optimize/_minimize.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `scipy/stats/_stats_py.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `scipy/sparse/linalg/_interface.py` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scipy/_lib/_docscrape.py` -> **Severity: 3263.323** (Blast Radius: 35.634 * Doc Risk: 91.5789%)
- `benchmarks/benchmarks/sparse.py` -> **Severity: 3146.568** (Blast Radius: 32.75 * Doc Risk: 96.0784%)
- `scipy/_lib/deprecation.py` -> **Severity: 2110.08** (Blast Radius: 25.12 * Doc Risk: 84.0%)
- `scipy/_lib/_array_api.py` -> **Severity: 1570.689** (Blast Radius: 26.285 * Doc Risk: 59.7561%)
- `benchmarks/benchmarks/special.py` -> **Severity: 1444.9** (Blast Radius: 14.449 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
