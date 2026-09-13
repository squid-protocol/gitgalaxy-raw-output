# ARCHITECTURAL_BRIEF: numpy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/numpy/numpy.git` |
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
| Total Artifacts | 2334 |
| Analyzed Artifacts (Scanned) | 1436 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 898 |
| Total LOC | 367295 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 61.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5876 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4155 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.871 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 49 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 777 | 186345 | 54.1% |
| C | 379 | 153021 | 26.4% |
| FORTRAN | 115 | 2374 | 8.0% |
| CPP | 81 | 24307 | 5.6% |
| PLAINTEXT | 33 | 0 | 2.3% |
| XML | 15 | 4 | 1.0% |
| MARKDOWN | 13 | 0 | 0.9% |
| SHELL | 7 | 91 | 0.5% |
| MAKEFILE | 4 | 217 | 0.3% |
| YAML | 3 | 120 | 0.2% |
| JSON | 3 | 35 | 0.2% |
| CSV | 2 | 629 | 0.1% |
| BATCH | 1 | 52 | 0.1% |
| CSS | 1 | 73 | 0.1% |
| HTML | 1 | 21 | 0.1% |
| M4 | 1 | 6 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1386 | 96.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 3.2% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 898*

**Composition by Extension & Reason:**
- `.rst`: 389x Excluded (Unsupported Extension: '.rst'), 174x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 57x Excluded (Explicitly Denied Extension: '.png')
- `.src`: 37x Unsupported Format (.src), 1x Excluded (Embedded Hex Payload: 1098 hex tokens in 716 LOC)
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 14x Excluded (Static Asset Blob without Intent: 1430 LOC), 10x Excluded (Static Asset Blob without Intent: 1002 LOC), 2x Excluded (Static Asset Blob without Intent: 1630 LOC)
- `.build`: 20x Excluded (Unsupported Extension: '.build')
- `.pyf`: 10x Unsupported Format (.pyf), 9x Excluded (Unsupported Extension: '.pyf')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.dat`: 17x Excluded (Unsupported Extension: '.dat')
- `.svg`: 3x Excluded (Machine-Generated Source Code Signature: 4 LOC), 2x Excluded (Static Asset Blob without Intent: 1472 LOC), 1x Excluded (Static Asset Blob without Intent: 2213 LOC)
- `.patch`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.i`: 9x Unsupported Format (.i)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 183 LOC), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC)
- `.tmpl`: 7x Excluded (Unsupported Extension: '.tmpl')
- `.toml`: 7x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.4 | 20.0 | 5.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 54.9 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.3 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.0 | 7.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 73.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 58.6 | 92.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 57656 | 641 | 42 | `numpy/linalg/lapack_lite/f2c_z_lapack.c` |
| cleanup | 179 | 51 | 0 | `numpy/linalg/umath_linalg.cpp` |
| guards | 17400 | 776 | 29 | `numpy/_core/src/common/npy_cblas_base.h` |
| danger | 9885 | 667 | 16 | `numpy/typing/tests/data/reveal/random.pyi` |
| concurrency | 727 | 91 | 0 | `numpy/random/tests/test_generator_mt19937.py` |
| connectivity | 22200 | 1044 | 37 | `numpy/_core/tests/test_multiarray.py` |
| io | 1309 | 195 | 2 | `numpy/_core/tests/test_multiarray.py` |
| crypto | 5 | 5 | 0 | `numpy/_core/code_generators/genapi.py` |
| ipc | 136 | 37 | 0 | `numpy/_core/tests/test_cpu_features.py` |
| time | 204 | 33 | 0 | `numpy/__init__.pyi` |
| serialization | 95 | 26 | 0 | `numpy/_core/tests/test_multiarray.py` |
| regex | 144 | 41 | 0 | `numpy/f2py/symbolic.py` |
| events | 104 | 19 | 0 | `numpy/_core/src/multiarray/alloc.cpp` |
| tests | 10282 | 213 | 8 | `numpy/_core/tests/test_multiarray.py` |
| docs | 3962 | 450 | 7 | `numpy/_core/_add_newdocs.py` |
| debt | 2009 | 318 | 3 | `numpy/__init__.pyi` |
| mutation | 167637 | 1085 | 225 | `numpy/linalg/lapack_lite/f2c_z_lapack.c` |
| dead_code | 8472 | 635 | 12 | `numpy/_core/tests/test_multiarray.py` |
| credential | 7 | 5 | 0 | `numpy/f2py/rules.py` |
| threat | 5453 | 439 | 7 | `numpy/__init__.pyi` |
| ml_ai | 3318 | 718 | 4 | `numpy/_core/tests/test_einsum.py` |
| ui | 10 | 2 | 0 | `doc/neps/tools/build_index.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `numpy/_core/tests/test_multiarray.py` (Hits: 80)
- `numpy/linalg/lapack_lite/make_lite.py` (Hits: 37)
- `numpy/_core/tests/test_nditer.py` (Hits: 36)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **numpy.css** (`doc/source/_static/numpy.css`) — 518 inbound connections
2. **arrayobject.h** (`numpy/_core/include/numpy/arrayobject.h`) — 71 inbound connections
3. **ndarraytypes.h** (`numpy/_core/include/numpy/ndarraytypes.h`) — 60 inbound connections
4. **_utils.py** (`numpy/core/_utils.py`) — 54 inbound connections
5. **npy_config.h** (`numpy/_core/src/common/npy_config.h`) — 53 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **multiarraymodule.c** (`numpy/_core/src/multiarray/multiarraymodule.c`) — 60 outbound dependencies
2. **__init__.pyi** (`numpy/__init__.pyi`) — 54 outbound dependencies
3. **__init__.py** (`numpy/__init__.py`) — 47 outbound dependencies
4. **test_multiarray.py** (`numpy/_core/tests/test_multiarray.py`) — 41 outbound dependencies
5. **utils.py** (`numpy/testing/_private/utils.py`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `genfromtxt` (@ `numpy/lib/_npyio_impl.py`) -> Impact: **981.0** | LOC: 754
  * *Intent:* #####-------------------------------------------------------------------------- #---- --- ASCII functions --- #####-----------------------------------...
- `ilaenv_` (@ `numpy/linalg/lapack_lite/f2c_lapack.c`) -> Impact: **961.1** | LOC: 628
  * *Intent:* } /* iladlr_ */
- `cgesdd_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **774.5** | LOC: 2496
  * *Intent:* /* End of CGEQRF */ } /* cgeqrf_ */
- `zgesdd_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **774.5** | LOC: 2508
  * *Intent:* /* End of ZGEQRF */ } /* zgeqrf_ */
- `zlatrs_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **588.2** | LOC: 1164
  * *Intent:* /* End of ZLATRD */ } /* zlatrd_ */
- `clatrs_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **588.1** | LOC: 1161
  * *Intent:* /* End of CLATRD */ } /* clatrd_ */
- `claqr5_` (@ `numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **536.0** | LOC: 1346
  * *Intent:* } /* claqr4_ */
- `zlaqr5_` (@ `numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **536.0** | LOC: 1350
  * *Intent:* } /* zlaqr4_ */
- `zgemm_` (@ `numpy/linalg/lapack_lite/f2c_blas.c`) -> Impact: **516.1** | LOC: 668
  * *Intent:* } /* zdscal_ */
- `cgemm_` (@ `numpy/linalg/lapack_lite/f2c_blas.c`) -> Impact: **516.0** | LOC: 667
  * *Intent:* } /* cdotu_ */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `numpy/linalg/lapack_lite` | 13 | 112131.12 | 48.44% | 17.96% |
| `numpy/_core/src/multiarray` | 110 | 59521.76 | 33.97% | 18.48% |
| `numpy/_core/tests` | 67 | 40230.1 | 29.86% | 0.0% |
| `numpy/lib` | 63 | 18938.48 | 17.44% | 6.67% |
| `numpy/_core/src/umath` | 37 | 18622.7 | 39.44% | 15.22% |
| `numpy/_core` | 62 | 14273.26 | 19.66% | 13.43% |
| `numpy/lib/tests` | 25 | 12559.04 | 27.54% | 0.0% |
| `numpy/ma` | 11 | 10775.08 | 15.24% | 1.84% |
| `numpy/f2py` | 34 | 8241.18 | 23.0% | 28.02% |
| `numpy/_core/src/npysort` | 18 | 7558.36 | 48.81% | 27.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks/bench_array_coercion.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_creation.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_linalg.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_itemselection.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_ma.py` -> **100.0%** Exposure
- `benchmarks/benchmarks/bench_manipulate.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `numpy/_core/tests/test_multiarray.py` -> **601** Orphaned Functions | **10** Duplicates
- `numpy/ma/tests/test_core.py` -> **321** Orphaned Functions | **6** Duplicates
- `numpy/__init__.pyi` -> **105** Orphaned Functions | **208** Duplicates
- `numpy/_core/tests/test_regression.py` -> **276** Orphaned Functions | **0** Duplicates
- `numpy/lib/tests/test_function_base.py` -> **240** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5239` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `numpy/_core/src/multiarray/hashdescr.c` (C) -> Cumulative Risk: **711.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 256.94 | **LOC:** 319 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9985%), Concurrency (98.4539%)
- **Heaviest Functions:** `_array_descr_walk_fields` (Impact: 80.0), `_array_descr_walk_subarray` (Impact: 26.0), `_array_descr_walk` (Impact: 15.1)

### 2. `numpy/_core/_methods.py` (PYTHON) -> Cumulative Risk: **680.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 360.32 | **LOC:** 253 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.992%)
- **Heaviest Functions:** `_var` (Impact: 63.4), `_mean` (Impact: 38.6), `_clip` (Impact: 27.8)

### 3. `benchmarks/benchmarks/bench_ma.py` (PYTHON) -> Cumulative Risk: **679.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 378.24 | **LOC:** 313 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.885%)
- **Heaviest Functions:** `setup` (Impact: 20.7), `setup` (Impact: 11.1), `setup` (Impact: 7.3)

### 4. `benchmarks/benchmarks/bench_indexing.py` (PYTHON) -> Cumulative Risk: **679.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 181.12 | **LOC:** 181 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setup` (Impact: 4.3), `time_index` (Impact: 3.8), `time_assign` (Impact: 3.8)

### 5. `numpy/_core/src/npysort/quicksort.cpp` (CPP) -> Cumulative Risk: **675.34**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1117.42 | **LOC:** 1024 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.7507%), Documentation (98.2143%)
- **Heaviest Functions:** `npy_aquicksort_impl` (Impact: 68.1), `npy_quicksort_impl` (Impact: 66.3), `string_aquicksort_` (Impact: 53.8)

### 6. `numpy/_core/src/npysort/mergesort.cpp` (CPP) -> Cumulative Risk: **673.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 769.04 | **LOC:** 755 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9793%), Safety Score (99.8732%)
- **Heaviest Functions:** `npy_amergesort0` (Impact: 36.1), `amergesort0_` (Impact: 31.6), `npy_mergesort0` (Impact: 30.5)

### 7. `benchmarks/benchmarks/bench_io.py` (PYTHON) -> Cumulative Risk: **672.82**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 166.62 | **LOC:** 255 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.9985%)
- **Heaviest Functions:** `setup` (Impact: 4.2), `time_loadtxt_dtypes_csv` (Impact: 2.5), `time_comment_loadtxt_csv` (Impact: 2.4)

### 8. `benchmarks/benchmarks/bench_manipulate.py` (PYTHON) -> Cumulative Risk: **671.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.18 | **LOC:** 112 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setup` (Impact: 11.5), `setup` (Impact: 4.3), `setup` (Impact: 4.2)

### 9. `benchmarks/benchmarks/bench_ufunc.py` (PYTHON) -> Cumulative Risk: **666.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 546.1 | **LOC:** 618 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setup` (Impact: 10.4), `time_methods_getitem` (Impact: 6.3), `time_methods_setitem` (Impact: 6.3)

### 10. `numpy/_core/src/multiarray/datetime.c` (C) -> Cumulative Risk: **664.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3785.68 | **LOC:** 4398 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.8203%)
- **Heaviest Functions:** `convert_pyobject_to_timedelta` (Impact: 188.6), `datetime_arange` (Impact: 123.8), `NpyDatetime_ConvertPyDateTimeToDatetimeStruct` (Impact: 113.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `numpy/linalg/lapack_lite/f2c_blas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 37170.98 | **LOC:** 21604 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6706%), Tech Debt (13.4253%)
**Top Internal Functions/Classes:**
  * `zgemm_` (Impact: 516.1)
    * *Intent:* } /* zdscal_ */
  * `cgemm_` (Impact: 516.0)
    * *Intent:* } /* cdotu_ */
  * `ctrsm_` (Impact: 470.0)
    * *Intent:* /* End of CTRMV . */ } /* ctrmv_ */
  * `ztrsm_` (Impact: 470.0)
    * *Intent:* /* End of ZTRMV . */ } /* ztrmv_ */
  * `ctrmm_` (Impact: 421.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_z_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34592.18 | **LOC:** 29997 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.229%), Tech Debt (8.314%)
**Top Internal Functions/Classes:**
  * `zgesdd_` (Impact: 774.5)
    * *Intent:* /* End of ZGEQRF */ } /* zgeqrf_ */
  * `zlatrs_` (Impact: 588.2)
    * *Intent:* /* End of ZLATRD */ } /* zlatrd_ */
  * `zlaqr5_` (Impact: 536.0)
    * *Intent:* } /* zlaqr4_ */
  * `zlals0_` (Impact: 381.9)
    * *Intent:* /* End of ZLAHR2 */ } /* zlahr2_ */
  * `zlalsd_` (Impact: 339.1)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/lapack_lite/f2c_c_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34590.7 | **LOC:** 29862 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3705%), Tech Debt (8.3198%)
**Top Internal Functions/Classes:**
  * `cgesdd_` (Impact: 774.5)
    * *Intent:* /* End of CGEQRF */ } /* cgeqrf_ */
  * `clatrs_` (Impact: 588.1)
    * *Intent:* /* End of CLATRD */ } /* clatrd_ */
  * `claqr5_` (Impact: 536.0)
    * *Intent:* } /* claqr4_ */
  * `clals0_` (Impact: 381.6)
    * *Intent:* /* End of CLAHR2 */ } /* clahr2_ */
  * `clasr_` (Impact: 339.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_multiarray.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7941.58 | **LOC:** 11172 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 13.2%
- **Risk Profile:** Cognitive Load (41.9795%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 73.0)
  * `test_ufunc_binop_interaction` (Impact: 58.5)
    * *Intent:* # ndarray.__rop__ always calls ufunc # ndarray.__iop__ always calls ufunc # ndarray.__op__, __rop__:...
  * `test_order_mismatch` (Impact: 38.0)
    * *Intent:* # The order is the main (python side) reason that can cause # a never-copy to fail. # Prepare C-orde...
  * `test_argsort` (Impact: 35.3)
    * *Intent:* # all c scalar argsorts use the same code with different types # so it suffices to run a quick check...
  * `test_np_argmin_argmax_keepdims` (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 735 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 4136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 1719`, `args: 848`, `func_start: 826`, `class_start: 148`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 21`, `state_mutation: 2666`, `dead_code: 10`, `planned_debt: 4`, `fragile_debt: 10`, `duplicate_logic: 10`, `unreferenced_by_name: 601`
* *Architecture:* `io: 80`, `api: 871`, `import: 53`
* *Defense:* `safety: 289`, `doc: 20`, `test: 968`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` _testbuffer, builtins, collections.abc, contextlib, ctypes, datetime, decimal, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/umath/ufunc_object.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5579.8 | **LOC:** 6804 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 23.5%
- **Risk Profile:** Cognitive Load (79.8519%), Tech Debt (13.0108%)
**Top Internal Functions/Classes:**
  * `PyUFunc_GeneralizedFunctionInternal` (Impact: 251.3)
  * `PyUFunc_Reduceat` (Impact: 168.2)
    * *Intent:* * * if indices[i+1] <= indices[i]+1 * then the result is array[indices[i]] for that value * * op.acc...
  * `PyUFunc_Accumulate` (Impact: 166.2)
  * `ufunc_generic_fastcall` (Impact: 166.2)
    * *Intent:* /* * Main ufunc call implementation. * * This implementation makes use of the "fastcall" way of pass...
  * `PyUFunc_GenericReduction` (Impact: 145.8)
    * *Intent:* /* * This code handles reduce, reduceat, and accumulate * (accumulate and reduce are special cases o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 766 instances
* *State Mutation (weighted view):* 2380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1055`, `structural_boundaries: 337`, `args: 209`, `func_start: 87`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 848`, `dead_code: 4`, `planned_debt: 17`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 16`, `import: 34`
* *Defense:* `safety: 18`, `doc: 16`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` Python.h, abstractdtypes.h, alloc.h, arrayobject.h, arraywrap.h, common.h, conversion_utils.h, convert_datatype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/ma/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5442.6 | **LOC:** 8995 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 23.8%
- **Risk Profile:** Cognitive Load (42.0271%), Tech Debt (10.1697%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 180.2)
  * `var` (Impact: 57.4)
  * `__getitem__` (Impact: 49.5)
    * *Intent:* """ x.__getitem__(y) <==> x[y] Return the item described by i, as a masked array. """
  * `__setitem__` (Impact: 47.4)
    * *Intent:* # setitem may put NaNs into integer arrays or occasionally overflow a # float. But this may happen i...
  * `__setmask__` (Impact: 45.5)
    * *Intent:* """ Set the mask. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 801 instances
* *State Mutation (weighted view):* 2625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 793`, `structural_boundaries: 791`, `args: 269`, `func_start: 268`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 1023`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 187`, `import: 16`
* *Defense:* `safety: 133`, `doc: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtins, copy, datetime, functools, inspect, numpy, numpy._core, numpy._core.numeric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_umath.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4003.34 | **LOC:** 5150 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (42.5481%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__array_ufunc__` (Impact: 60.7)
  * `test_division_int_boundary` (Impact: 44.9)
  * `test_ufunc_override_with_super` (Impact: 44.0)
    * *Intent:* # NOTE: this class is used in doc/source/user/basics.subclassing.rst # if you make any changes here,...
  * `test_out_wrap_subok` (Impact: 32.0)
  * `test_loss_of_precision` (Impact: 30.5)
    * *Intent:* """Check loss of precision in complex arc* functions"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 538 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 810`, `args: 378`, `func_start: 343`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 1088`, `dead_code: 4`, `fragile_debt: 10`, `duplicate_logic: 14`, `unreferenced_by_name: 225`
* *Architecture:* `io: 9`, `api: 361`, `import: 20`
* *Defense:* `safety: 116`, `doc: 12`, `test: 409`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cmath, collections, decimal, fnmatch, fractions, functools, inspect, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/datetime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3785.68 | **LOC:** 4398 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (77.5676%), Tech Debt (8.3946%)
**Top Internal Functions/Classes:**
  * `convert_pyobject_to_timedelta` (Impact: 188.6)
    * *Intent:* * Converts a PyObject * into a timedelta, in any of the forms supported * * If the units metadata is...
  * `datetime_arange` (Impact: 123.8)
  * `NpyDatetime_ConvertPyDateTimeToDatetimeStruct` (Impact: 113.1)
    * *Intent:* * While the C API has PyDate_* and PyDateTime_* functions, the following * implementation just asks ...
  * `convert_pyobject_to_datetime` (Impact: 109.6)
    * *Intent:* * Converts a PyObject * into a datetime, in any of the forms supported. * * If the units metadata is...
  * `compute_datetime_metadata_greatest_common_divisor` (Impact: 98.1)
    * *Intent:* /* * Computes the GCD of the two date-time metadata values. Raises * an exception if there is no rea...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 530 instances
* *State Mutation (weighted view):* 1634
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 821`, `structural_boundaries: 379`, `args: 126`, `func_start: 68`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 574`, `dead_code: 2`, `planned_debt: 6`
* *Architecture:* `api: 70`, `import: 16`
* *Defense:* `safety: 14`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.386
  * `Choke Point (Betweenness):` 0.000223 | `Ripple Effect (Closeness):` 0.014593
  * `Imports (Out-Degree: 13):` Python.h, _datetime.h, array_method.h, common.h, convert_datatype.h, datetime.h, datetime_strings.h, dtype_transfer.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `numpy/_core/src/multiarray/multiarraymodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3505.7 | **LOC:** 5317 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 29.4%
- **Risk Profile:** Cognitive Load (72.8568%), Tech Debt (13.1298%)
**Top Internal Functions/Classes:**
  * `_array_fromobject_generic` (Impact: 115.2)
  * `PyArray_Where` (Impact: 111.5)
    * *Intent:* /*NUMPY_API * Where */
  * `_multiarray_umath_exec` (Impact: 103.4)
  * `PyArray_MatrixProduct2` (Impact: 78.1)
    * *Intent:* /*NUMPY_API * Numeric.matrixproduct2(a,v,out) * just like inner product but does the swapaxes stuff ...
  * `array_shares_memory_impl` (Impact: 68.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 460 instances
* *State Mutation (weighted view):* 1426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 778`, `structural_boundaries: 385`, `args: 295`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 506`, `dead_code: 2`, `planned_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `api: 31`, `import: 61`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` Python.h, __multiarray_api.c, __ufunc_api.c, _datetime.h, abstractdtypes.h, alloc.h, array_assign.h, array_coercion.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/__init__.pyi` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3411.8 | **LOC:** 6069 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 59.7%
- **Risk Profile:** Cognitive Load (10.6167%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `std` (Impact: 3.8)
  * `std[ArrayT` (Impact: 3.8)
  * `std[ArrayT` (Impact: 3.8)
  * `var` (Impact: 3.8)
  * `var[ArrayT` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 1786`, `args: 1532`, `func_start: 1532`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 74`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 208`, `unreferenced_by_name: 105`
* *Architecture:* `io: 2`, `api: 313`, `import: 56`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ._expired_attrs_2_0, ._globals, _typeshed, abc, builtins, collections.abc, ctypes, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/npysort/timsort.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3365.16 | **LOC:** 2927 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2285%), Tech Debt (63.8275%)
**Top Internal Functions/Classes:**
  * `npy_atry_collapse` (Impact: 51.0)
  * `npy_try_collapse` (Impact: 48.2)
  * `npy_acount_run` (Impact: 48.2)
    * *Intent:* /* argsort */
  * `npy_count_run` (Impact: 48.0)
  * `atry_collapse_` (Impact: 45.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 581 instances
* *State Mutation (weighted view):* 1766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 441`, `args: 73`, `func_start: 105`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 604`, `planned_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 54`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cstdlib, npy_sort.h, npysort_common.h, numpy_tag.h, utility
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/lib/_function_base_impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3277.96 | **LOC:** 5765 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 9.7%
- **Risk Profile:** Cognitive Load (64.1523%), Tech Debt (8.2134%)
**Top Internal Functions/Classes:**
  * `cov` (Impact: 127.8)
  * `_quantile` (Impact: 111.3)
  * `gradient` (Impact: 102.4)
    * *Intent:* """ Return the gradient of an N-dimensional array. The gradient is computed using second order accur...
  * `delete` (Impact: 74.8)
    * *Intent:* """ Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this retu...
  * `insert` (Impact: 53.8)
    * *Intent:* """ Insert values along the given axis before the given indices. Parameters ---------- arr : array_l...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 532 instances
* *State Mutation (weighted view):* 1673
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 475`, `structural_boundaries: 294`, `args: 122`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 609`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 42`, `import: 17`
* *Defense:* `safety: 27`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` builtins, collections.abc, functools, matplotlib.pyplot, numpy, numpy._core, numpy._core._multiarray_umath, numpy._core.fromnumeric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/ctors.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3261.52 | **LOC:** 4208 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 11.1%
- **Risk Profile:** Cognitive Load (81.6576%), Tech Debt (20.0854%)
**Top Internal Functions/Classes:**
  * `PyArray_NewFromDescr_int` (Impact: 232.5)
    * *Intent:* /* * Generic new array creation routine. * Internal variant with calloc argument for PyArray_Zeros. ...
  * `PyArray_FromAny_int` (Impact: 112.0)
    * *Intent:* /* * Internal version of PyArray_FromAny that accepts a dtypemeta. Borrows * references to the descr...
  * `PyArray_FromInterface` (Impact: 108.6)
    * *Intent:* /*NUMPY_API*/
  * `PyArray_NewLikeArrayWithShape` (Impact: 98.9)
    * *Intent:* * ndim - If not -1, overrides the shape of the result. * dims - If ndim is not -1, overrides the sha...
  * `PyArray_ArangeObj` (Impact: 95.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` Python.h, _datetime.h, alloc.h, array_assign.h, array_coercion.h, arrayobject.h, assert.h, common.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/ma/tests/test_core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3242.34 | **LOC:** 6090 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (40.4614%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_match_sequence_pattern_3d` (Impact: 13.8)
  * `test_pickling` (Impact: 9.5)
    * *Intent:* # Tests pickling for dtype in (int, float, str, object): a = arange(10).astype(dtype) a.fill_value =...
  * `test_inplace_division_array_type` (Impact: 9.1)
    * *Intent:* # Test of inplace division othertypes, uint8data = self._create_otherdata() with warnings.catch_warn...
  * `test_inplace_division_scalar_type` (Impact: 8.9)
    * *Intent:* # Test of inplace division othertypes, uint8data = self._create_otherdata() with warnings.catch_warn...
  * `test_eq_ne_structured_extra` (Impact: 8.7)
    * *Intent:* # ensure simple examples are symmetric and make sense. # from https://github.com/numpy/numpy/pull/85...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 146 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 1861
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 578`, `args: 368`, `func_start: 361`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 1569`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 321`
* *Architecture:* `io: 1`, `api: 363`, `import: 27`
* *Defense:* `safety: 126`, `doc: 11`, `test: 390`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` copy, datetime, functools, inspect, io, itertools, numpy, numpy._core.fromnumeric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/lib/tests/test_function_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3228.08 | **LOC:** 4768 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (40.9383%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_quantile_add_and_multiply_constant` (Impact: 50.1)
    * *Intent:* # Test that # 1. quantile(c + x) = c + quantile(x) # 2. quantile(c * x) = c * quantile(x) # 3. quant...
  * `construct_input_output` (Impact: 43.1)
    * *Intent:* """Construct an input/output test pair for trim_zeros"""
  * `test_linear_interpolation` (Impact: 31.8)
  * `test_percentile_out` (Impact: 24.5)
  * `test_quantile_identification_equation` (Impact: 21.8)
    * *Intent:* # Test that the identification equation holds for the empirical # CDF: # E[V(x, Y)] = 0 <=> x is qua...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 1582
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 686`, `args: 408`, `func_start: 376`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1160`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 9`, `unreferenced_by_name: 240`
* *Architecture:* `io: 10`, `api: 412`, `import: 20`
* *Defense:* `safety: 109`, `doc: 11`, `test: 450`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` decimal, fractions, functools, gc, hypothesis, hypothesis.extra.numpy, hypothesis.strategies, math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dtype_transfer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3182.76 | **LOC:** 3835 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (64.291%), Tech Debt (22.547%)
**Top Internal Functions/Classes:**
  * `get_subarray_broadcast_transfer_function` (Impact: 124.2)
  * `get_legacy_dtype_cast_function` (Impact: 123.3)
  * `PyArray_PrepareThreeRawArrayIter` (Impact: 84.7)
    * *Intent:* * operands instead of one. Any broadcasting of the three operands * should have already been done be...
  * `get_fields_transfer_function` (Impact: 76.1)
    * *Intent:* /* * Handles fields transfer. To call this, at least one of the dtypes * must have fields. Does not ...
  * `define_cast_for_descrs` (Impact: 74.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, _datetime.h, alloc.h, array_assign.h, array_coercion.h, array_method.h, convert_datatype.h, ctors.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/item_selection.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3098.88 | **LOC:** 3377 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (81.1169%), Tech Debt (19.8671%)
**Top Internal Functions/Classes:**
  * `_new_argsortlike` (Impact: 156.9)
  * `_new_sortlike` (Impact: 145.9)
    * *Intent:* /* * These algorithms use special sorting. They are not called unless the * underlying sort function...
  * `npy_fasttake_impl` (Impact: 134.3)
    * *Intent:* #include "ctors.h" #include "lowlevel_strided_loops.h" #include "array_assign.h" #include "refcount....
  * `PyArray_PutTo` (Impact: 131.7)
    * *Intent:* /*NUMPY_API * Put values into an array */
  * `PyArray_LexSort` (Impact: 120.1)
    * *Intent:* /*NUMPY_API *LexSort an array providing indices that will sort a collection of arrays *lexicographic...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 461 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 159`, `args: 137`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 508`, `dead_code: 4`, `planned_debt: 3`, `unreferenced_by_name: 18`
* *Architecture:* `api: 20`, `import: 25`
* *Defense:* `safety: 3`, `immutability_locks: 62`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` Python.h, alloc.h, array_assign.h, array_coercion.h, arrayobject.h, arraytypes.h, common.h, ctors.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/mapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2928.76 | **LOC:** 3486 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (75.3928%), Tech Debt (15.563%)
**Top Internal Functions/Classes:**
  * `prepare_index_noarray` (Impact: 322.7)
    * *Intent:* * Checks everything but the bounds. * * @param array_ndims The number of dimensions of the array bei...
  * `PyArray_MapIterNew` (Impact: 313.0)
    * *Intent:* * @param Operand iteration flags for the extra operand, this must not be * 0 if an extra operand sho...
  * `array_assign_subscript` (Impact: 175.1)
    * *Intent:* /* * General assignment with python indexing objects. */
  * `array_subscript` (Impact: 90.2)
    * *Intent:* /* * General function for indexing a NumPy array with a Python object. */
  * `mapiter_fill_info` (Impact: 78.8)
    * *Intent:* * * mit-> fancy_dims: the dimension of `arr` along the indexed dimension * for each fancy index. * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 447 instances
* *State Mutation (weighted view):* 1405
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 513`, `structural_boundaries: 145`, `args: 95`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 511`, `dead_code: 2`, `planned_debt: 11`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 19`, `import: 20`
* *Defense:* `safety: 1`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, array_assign.h, array_coercion.h, arrayobject.h, common.h, ctors.h, descriptor.h, item_selection.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/nditer_constr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2857.64 | **LOC:** 3556 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (74.2083%), Tech Debt (10.0564%)
**Top Internal Functions/Classes:**
  * `npyiter_fill_axisdata` (Impact: 327.6)
    * *Intent:* /* * Fills in the AXISDATA for the 'nop' operands, broadcasting * the dimensionas as necessary. Also...
  * `NpyIter_AdvancedNew` (Impact: 185.2)
    * *Intent:* /*NUMPY_API * Allocate a new iterator for multiple array objects, and advanced * options for control...
  * `npyiter_allocate_arrays` (Impact: 162.6)
  * `npyiter_find_buffering_setup` (Impact: 125.4)
    * *Intent:* * (1 + n_buffers) / min(core_size * outer_dim_size, buffersize) * * And when comparing two options m...
  * `npyiter_new_temp_array` (Impact: 114.8)
    * *Intent:* /* * Allocates a temporary array which can be used to replace op * in the iteration. Its dtype will ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 392 instances
* *State Mutation (weighted view):* 1210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 163`, `args: 123`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 426`, `dead_code: 3`, `planned_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` alloc.h, array_assign.h, array_coercion.h, arrayobject.h, dtype_traversal.h, nditer_impl.h, templ_common.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/tests/test_numeric.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2619.68 | **LOC:** 4264 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (41.9104%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_like_function` (Impact: 64.2)
  * `check_function` (Impact: 42.5)
  * `tst_isclose_allclose` (Impact: 20.4)
  * `test_promote_types_metadata` (Impact: 20.2)
    * *Intent:* """Metadata handling in promotion does not appear formalized right now in NumPy. This test should th...
  * `test_floating_exceptions` (Impact: 18.8)
    * *Intent:* # Test for all real and complex float types
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 173 instances
* *State Mutation (weighted view):* 1242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 672`, `args: 324`, `func_start: 309`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 896`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 243`
* *Architecture:* `io: 11`, `api: 334`, `import: 21`
* *Defense:* `safety: 149`, `doc: 7`, `test: 335`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` decimal, fractions, hypothesis, hypothesis.extra, inspect, itertools, math, numbers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/convert_datatype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2565.44 | **LOC:** 3582 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (68.2478%), Tech Debt (35.9985%)
**Top Internal Functions/Classes:**
  * `min_scalar_type_num` (Impact: 255.8)
    * *Intent:* /* * NOTE: While this is unlikely to be a performance problem, if * it is it could be reverted to a ...
  * `cast_to_string_resolve_descriptors` (Impact: 103.5)
  * `void_to_void_resolve_descriptors` (Impact: 89.1)
  * `PyArray_ResultType` (Impact: 64.3)
    * *Intent:* * * Produces the result type of a bunch of inputs, using the same rules * as `np.result_type`. * * N...
  * `nonstructured_to_structured_resolve_descriptors` (Impact: 59.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 879
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 338`, `args: 158`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 319`, `dead_code: 1`, `planned_debt: 13`, `fragile_debt: 4`, `unreferenced_by_name: 20`
* *Architecture:* `api: 43`, `import: 30`
* *Defense:* `safety: 15`, `doc: 10`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` Python.h, _datetime.h, abstractdtypes.h, alloc.h, array_coercion.h, array_method.h, arrayobject.h, can_cast_table.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/lib/_npyio_impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2504.16 | **LOC:** 2492 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (74.3183%), Tech Debt (10.957%)
**Top Internal Functions/Classes:**
  * `genfromtxt` (Impact: 981.0)
    * *Intent:* #####-------------------------------------------------------------------------- #---- --- ASCII func...
  * `_read` (Impact: 196.1)
  * `savetxt` (Impact: 128.5)
  * `load` (Impact: 46.3)
  * `loadtxt` (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 281 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 860
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 168`, `args: 44`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 2`, `state_mutation: 298`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 20`, `api: 34`, `import: 24`
* *Defense:* `safety: 80`, `doc: 23`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , ._datasource, ._format_impl, ._iotools, collections.abc, contextlib, functools, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/dragon4.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2458.3 | **LOC:** 3215 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.6836%), Tech Debt (19.1578%)
**Top Internal Functions/Classes:**
  * `FormatPositional` (Impact: 217.0)
    * *Intent:* * NUL) is returned. * * Arguments: * buffer - buffer to output into * bufferSize - maximum character...
  * `Dragon4` (Impact: 195.0)
    * *Intent:* * * bigints - memory to store all bigints needed (7) for dragon4 computation. * The first BigInt sho...
  * `FormatScientific` (Impact: 177.7)
    * *Intent:* * The output is always NUL terminated and the output length (not including the * NUL) is returned. *...
  * `Dragon4_PrintFloat_IBM_double_double` (Impact: 41.5)
    * *Intent:* * more than 106 bits (53+53), so we can drop bits from the second double which * would be pushed pas...
  * `BigInt_DivideWithRemainder_MaxQuotient9` (Impact: 31.0)
    * *Intent:* * result is within the range [0,10) and the input numbers have been shifted * to satisfy: * - The hi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 419 instances
* *State Mutation (weighted view):* 1338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 104`, `args: 73`, `func_start: 42`, `class_start: 14`
* *Risk/State:* `state_mutation: 500`, `dead_code: 19`, `planned_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, dragon4.h, math.h, npy_common.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/_core/src/multiarray/descriptor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2431.94 | **LOC:** 3868 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (70.7596%), Tech Debt (15.5631%)
**Top Internal Functions/Classes:**
  * `arraydescr_setstate` (Impact: 163.8)
    * *Intent:* /* * state is at least byteorder, subarray, and fields but could include elsize * and alignment for ...
  * `_convert_from_dict` (Impact: 138.9)
    * *Intent:* /* * Creates a struct dtype object from a Python dictionary. */
  * `_convert_from_str` (Impact: 103.1)
    * *Intent:* /** Convert a bytestring specification into a dtype */
  * `_convert_from_array_descr` (Impact: 94.5)
    * *Intent:* /* * obj is a list. Each item is a tuple with * * (field-name, data-type (either a list or a string)...
  * `_convert_from_tuple` (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 939
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 674`, `structural_boundaries: 333`, `args: 202`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 325`, `dead_code: 9`, `planned_debt: 10`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 23`
* *Defense:* `safety: 4`, `doc: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Python.h, _datetime.h, alloc.h, array_coercion.h, assert.h, common.h, conversion_utils.h, descriptor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy/linalg/umath_linalg.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2425.78 | **LOC:** 4812 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.1599%), Tech Debt (12.6725%)
**Top Internal Functions/Classes:**
  * `svd_wrapper` (Impact: 44.8)
  * `eig_wrapper` (Impact: 39.0)
  * `eigh_wrapper` (Impact: 27.7)
  * `compute_urows_vtcolumns` (Impact: 23.4)
  * `init_gesdd` (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 441 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 1467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 654`, `args: 125`, `func_start: 150`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 585`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 9`
* *Architecture:* `import: 14`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 146`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Python.h, cassert, cmath, cstddef, cstdio, execinfo.h, libunwind.h, npy_cblas.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `numpy/__init__.pyi` -> Churn: **100.0%** | Cog Load: 10.6167% | Debt: 100.0%
- `numpy/lib/_function_base_impl.py` -> Churn: **80.71%** | Cog Load: 64.1523% | Debt: 8.2134%
- `numpy/_core/src/multiarray/multiarraymodule.c` -> Churn: **67.62%** | Cog Load: 72.8568% | Debt: 13.1298%
- `numpy/_core/src/umath/ufunc_object.c` -> Churn: **67.62%** | Cog Load: 79.8519% | Debt: 13.0108%
- `doc/source/conf.py` -> Churn: **57.79%** | Cog Load: 60.8194% | Debt: 92.1064%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `numpy/_core/src/multiarray/dtype_transfer.c` -> **Matti Picus** (100.0% isolated ownership) | Magnitude: 3182.76
- `numpy/linalg/umath_linalg.cpp` -> **Evgeni Burovski** (100.0% isolated ownership) | Magnitude: 2425.78
- `numpy/_core/src/multiarray/datetime_strings.c` -> **Matti Picus** (100.0% isolated ownership) | Magnitude: 1764.14
- `numpy/_build_utils/tempita/_tempita.py` -> **Noxaster** (100.0% isolated ownership) | Magnitude: 1489.06
- `numpy/random/tests/test_randomstate.py` -> **Britney Whittington** (100.0% isolated ownership) | Magnitude: 1400.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `numpy/_core/src/multiarray/common.h` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 99.9033%)
- `numpy/_core/src/multiarray/datetime.c` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `numpy/_core/include/numpy/ndarraytypes.h` -> **Severity: 0.019** (Bridge: 0.0003 * Flux: 67.8123%)
- `numpy/_core/src/common/lowlevel_strided_loops.h` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 100.0%)
- `numpy/_core/src/umath/_rational_tests.c` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.9997%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `numpy/_core/include/numpy/ndarraytypes.h` -> **Severity: 4.387** (Embedded: 0.065 * Error Risk: 67.5161%)
- `numpy/_core/include/numpy/_neighborhood_iterator_imp.h` -> **Severity: 4.208** (Embedded: 0.0437 * Error Risk: 96.2929%)
- `numpy/_core/src/multiarray/common.h` -> **Severity: 3.338** (Embedded: 0.0414 * Error Risk: 80.6391%)
- `numpy/core/_utils.py` -> **Severity: 3.337** (Embedded: 0.0418 * Error Risk: 79.7611%)
- `numpy/_core/include/numpy/ndarrayobject.h` -> **Severity: 2.902** (Embedded: 0.0405 * Error Risk: 71.6575%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `numpy/_core/include/numpy/ndarraytypes.h` -> **Severity: 1803.8** (Blast Radius: 18.038 * Doc Risk: 100.0%)
- `numpy/core/_utils.py` -> **Severity: 1462.2** (Blast Radius: 14.622 * Doc Risk: 100.0%)
- `numpy/_core/include/numpy/npy_math.h` -> **Severity: 779.9** (Blast Radius: 7.799 * Doc Risk: 100.0%)
- `numpy/_core/include/numpy/ndarrayobject.h` -> **Severity: 620.5** (Blast Radius: 6.205 * Doc Risk: 100.0%)
- `numpy/_core/include/numpy/dtype_api.h` -> **Severity: 557.4** (Blast Radius: 5.574 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
