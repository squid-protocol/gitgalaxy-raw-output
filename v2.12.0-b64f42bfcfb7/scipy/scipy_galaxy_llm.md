# ARCHITECTURAL_BRIEF: scipy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3912 analyzed artifact(s), 908260 LOC.
- **Load-bearing artifact:** `scipy-1.17.1/scipy/_lib/_array_api.py` -- 178 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/rational.hpp` -- pulls in 119 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `scipy-1.17.1/subprojects/xsf/include/xsf/specfun/specfun.h` at magnitude 11762.3 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 4953 |
| Analyzed Artifacts (Scanned) | 3912 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1041 |
| Total LOC | 908260 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8407 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1495 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.2316 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 247 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1316 | 332030 | 33.6% |
| CPP | 1305 | 365870 | 33.4% |
| C | 649 | 155724 | 16.6% |
| PLAINTEXT | 219 | 82 | 5.6% |
| JAVASCRIPT | 144 | 30163 | 3.7% |
| FORTRAN | 93 | 20031 | 2.4% |
| MARKDOWN | 63 | 0 | 1.6% |
| JSON | 45 | 519 | 1.2% |
| YAML | 32 | 1703 | 0.8% |
| SHELL | 17 | 457 | 0.4% |
| XML | 7 | 0 | 0.2% |
| MAKEFILE | 6 | 251 | 0.2% |
| M4 | 4 | 252 | 0.1% |
| MATLAB | 4 | 76 | 0.1% |
| HTML | 2 | 23 | 0.1% |
| CSS | 1 | 76 | 0.0% |
| BMS | 1 | 1 | 0.0% |
| OBJECTIVE-C | 1 | 18 | 0.0% |
| NIX | 1 | 62 | 0.0% |
| CSHARP | 1 | 909 | 0.0% |
| BATCH | 1 | 13 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3911 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 20%, Declarative / Non-Code 17%, Data / Markup / Trivial 15%, Large Core Modules (3) 13%, Parameter Forwarders Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3599 | 92.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 260 | 6.6% |
| Static: Minified & Vendor Opaque Mass | 53 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1041*

**Composition by Extension & Reason:**
- `.rst`: 346x Excluded (Unsupported Extension: '.rst')
- `.npz`: 141x Excluded (Unsupported Extension: '.npz')
- `.mat`: 113x Excluded (Unsupported Extension: '.mat')
- `.build`: 101x Excluded (Unsupported Extension: '.build')
- `.js`: 14x Excluded (Saturation: Line 25 exceeds 500 chars), 8x Excluded (Saturation: Line 34 exceeds 500 chars), 7x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.sav`: 47x Excluded (Unsupported Extension: '.sav')
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.dat`: 26x Excluded (Unsupported Extension: '.dat')
- `.txt`: 2x Excluded (Lexical Monotony: High structural repetition detected in 6631 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2305 LOC), 1x Excluded (Machine-Generated Source Code Signature: 7 LOC)
- `.wav`: 22x Excluded (Explicitly Denied Extension: '.wav')
- `.src`: 18x Excluded (Unsupported Extension: '.src')
- `.arff`: 16x Excluded (Unsupported Extension: '.arff')
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 11x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2273 LOC), 1x Excluded (Machine-Generated Source Code Signature: 521 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 32.9 | 31.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 52.1 | 59.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.1 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.2 | 6.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.3 | 69.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.6 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 28376 | 1466 | 14 | `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions/lanczos.hpp` |
| cleanup | 886 | 260 | 0 | `scipy-1.17.1/subprojects/highs/extern/catch.hpp` |
| guards | 68587 | 2496 | 46 | `scipy-1.17.1/subprojects/highs/extern/catch.hpp` |
| danger | 11661 | 1190 | 6 | `scipy-1.17.1/subprojects/highs/highs/highspy/highs.py` |
| concurrency | 901 | 186 | 0 | `scipy-1.17.1/scipy/_lib/pocketfft/pocketfft_hdronly.h` |
| connectivity | 33263 | 2474 | 19 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| io | 1560 | 236 | 0 | `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` |
| crypto | 2 | 1 | 0 | `scipy-1.17.1/tools/write_release_and_log.py` |
| ipc | 107 | 37 | 0 | `scipy-1.17.1/tools/lint.py` |
| time | 184 | 45 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |
| serialization | 230 | 24 | 0 | `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` |
| regex | 528 | 78 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |
| events | 1303 | 149 | 0 | `scipy-1.17.1/scipy/integrate/__quadpack.h` |
| tests | 19384 | 392 | 1 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| docs | 11220 | 1812 | 8 | `scipy-1.17.1/scipy/special/cython_special.pyx` |
| debt | 6590 | 875 | 3 | `scipy-1.17.1/subprojects/highs/highs/highspy/_core/__init__.pyi` |
| mutation | 449458 | 2992 | 273 | `scipy-1.17.1/scipy/integrate/_lebedev.py` |
| dead_code | 17374 | 1539 | 8 | `scipy-1.17.1/scipy/stats/tests/test_distributions.py` |
| credential | 103 | 1 | 0 | `scipy-1.17.1/tools/wheels/upload_wheels.sh` |
| threat | 57 | 10 | 0 | `scipy-1.17.1/scipy/io/tests/test_netcdf.py` |
| ml_ai | 9244 | 1437 | 6 | `scipy-1.17.1/subprojects/xsf/include/xsf/amos/amos.h` |
| ui | 57 | 19 | 0 | `scipy-1.17.1/doc/source/_static/scipy-mathjax/MathJax.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` (Hits: 372)
- `scipy-1.17.1/scipy/odr/odrpack/d_test.f` (Hits: 81)
- `scipy-1.17.1/scipy/special/_generate_pyx.py` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_array_api.py** (`scipy-1.17.1/scipy/_lib/_array_api.py`) — 178 inbound connections
2. **config.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/config.hpp`) — 172 inbound connections
3. **error.c** (`scipy-1.17.1/scipy/_lib/unuran/unuran/src/utils/error.c`) — 151 inbound connections
4. **unur_source.h** (`scipy-1.17.1/scipy/_lib/unuran/unuran/src/unur_source.h`) — 145 inbound connections
5. **__init__.py** (`scipy-1.17.1/scipy/__init__.py`) — 142 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rational.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/rational.hpp`) — 119 outbound dependencies
2. **special_functions.hpp** (`scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions.hpp`) — 66 outbound dependencies
3. **catch.hpp** (`scipy-1.17.1/subprojects/highs/extern/catch.hpp`) — 54 outbound dependencies
4. **stringparser.c** (`scipy-1.17.1/scipy/_lib/unuran/unuran/src/parser/stringparser.c`) — 53 outbound dependencies
5. **xsf_wrappers.cpp** (`scipy-1.17.1/scipy/special/xsf_wrappers.cpp`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_unur_str_par_set` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/_lib/unuran/unuran/src/parser/stringparser_lists.h`) -> Impact: **1306.5** | LOC: 1087
  * *Intent:* } /* end of _unur_str_par_new() */ /*---------------------------------------------------------------------------*/
- `trlib_krylov_min_internal` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/optimize/_trlib/trlib_krylov.c`) -> Impact: **1198.1** | LOC: 656
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `lsoda` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/lsoda.c`) -> Impact: **933.6** | LOC: 714
  * *Intent:* * @param itol Tolerance type indicator (1-4). * @param rtol Relative tolerance array. * @param atol Absolute tolerance array. * @param itask Task indi...
- `preproc` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/_lib/pyprima/pyprima/src/pyprima/common/preproc.py`) -> Impact: **669.4** | LOC: 258
- `writeGlpsolSolution` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsModelUtils.cpp`) -> Impact: **669.0** | LOC: 661
- `trlib_tri_factor_min` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/optimize/_trlib/trlib_tri_factor.c`) -> Impact: **660.6** | LOC: 390
  * *Intent:* * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILI...
- `zvode` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/zvode.c`) -> Impact: **648.4** | LOC: 691
  * *Intent:* * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @param iopt Optional input flag * @param zwork Complex work array * @p...
- `fppola` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/interpolate/fitpack/fppola.f`) -> Impact: **602.5** | LOC: 840
- `writeMps` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/subprojects/highs/highs/io/HMPSIO.cpp`) -> Impact: **600.4** | LOC: 407
- `dvode` **(Many-Argument Workhorses)** (@ `scipy-1.17.1/scipy/integrate/src/vode.c`) -> Impact: **600.3** | LOC: 641
  * *Intent:* * @param rtol Relative tolerance * @param atol Absolute tolerance * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @par...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC` | 195 | 63577.66 | 57.15% | 23.24% |
| `scipy-1.17.1/scipy/stats` | 72 | 47962.84 | 37.68% | 11.28% |
| `scipy-1.17.1/scipy/optimize` | 74 | 37387.96 | 41.26% | 7.66% |
| `scipy-1.17.1/scipy/stats/tests` | 41 | 35000.58 | 33.47% | 0.0% |
| `scipy-1.17.1/scipy/interpolate/fitpack` | 87 | 29728.02 | 67.65% | 25.61% |
| `scipy-1.17.1/scipy/_lib/unuran/unuran/src/methods` | 156 | 29650.46 | 17.99% | 7.61% |
| `scipy-1.17.1/subprojects/qhull_r/libqhull_r` | 30 | 27129.06 | 37.2% | 18.24% |
| `scipy-1.17.1/subprojects/highs/highs/mip` | 56 | 22539.52 | 47.36% | 24.33% |
| `scipy-1.17.1/subprojects/highs/highs/lp_data` | 36 | 21014.8 | 33.72% | 21.3% |
| `scipy-1.17.1/scipy/integrate` | 20 | 20873.88 | 46.45% | 8.06% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scipy-1.17.1/benchmarks/benchmarks/ndimage_interpolation.py` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/spatial/_qhull.pyi` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/special/cython_special.pxd` -> **100.0%** Exposure
- `scipy-1.17.1/scipy/stats/_unuran/unuran_wrapper.pyi` -> **100.0%** Exposure
- `scipy-1.17.1/subprojects/highs/highs/highspy/_core/__init__.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scipy-1.17.1/benchmarks/benchmarks/cluster.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cluster_hierarchy_disjoint_set.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/common.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cutest/calfun.py` -> **100.0%** Exposure
- `scipy-1.17.1/benchmarks/benchmarks/cutest/dfovec.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scipy-1.17.1/subprojects/highs/extern/catch.hpp` -> **500** Orphaned Functions | **26** Duplicates
- `scipy-1.17.1/scipy/stats/tests/test_stats.py` -> **466** Orphaned Functions | **4** Duplicates
- `scipy-1.17.1/scipy/stats/tests/test_distributions.py` -> **412** Orphaned Functions | **7** Duplicates
- `scipy-1.17.1/scipy/special/tests/test_basic.py` -> **341** Orphaned Functions | **0** Duplicates
- `scipy-1.17.1/scipy/special/xsf_wrappers.cpp` -> **259** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `scipy-1.17.1/tools/wheels/upload_wheels.sh` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13347` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `scipy-1.17.1/subprojects/xsf/include/xsf/specfun/specfun.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.546)
- **Top Global Matches:** file_cluster_3: 6.546, file_cluster_8: 19.072, file_cluster_6: 32.004
- **Magnitude:** 11762.3 | **LOC:** 6197 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 0.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cv0` **(Many-Argument Workhorses)** (Impact: 268.9)
  * `hygfz` **(Many-Argument Workhorses)** (Impact: 265.1)
  * `mtu12` **(Many-Argument Workhorses)** (Impact: 199.4)
  * `fcoef` **(Many-Argument Workhorses)** (Impact: 198.4)
  * `rmn2sp` **(Many-Argument Workhorses)** (Impact: 118.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2595 instances
* *State Mutation (weighted view):* 7895
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1369`, `structural_boundaries: 345`, `args: 187`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `state_mutation: 2705`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `safety: 51`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001416
  * `Imports (Out-Degree: 1):` config.h, memory
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/xsf/include/xsf/amos/amos.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 20.93)
- **Top Global Matches:** file_cluster_3: 20.93, file_cluster_1: 27.773, file_cluster_8: 42.544
- **Magnitude:** 9158.56 | **LOC:** 6595 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.165; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 2261`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 1`, `doc: 20`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001065
  * `Imports (Out-Degree: 0):` complex, math.h, memory, stdlib.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/integrate/__quadpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.863)
- **Top Global Matches:** file_cluster_3: 11.863, file_cluster_8: 14.011, file_cluster_6: 26.427
- **Magnitude:** 7383.18 | **LOC:** 6857 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.207; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1751`, `dead_code: 21`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 1):` __quadpack.h, math.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/stats/_continuous_distns.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 10.716)
- **Top Global Matches:** file_cluster_16: 10.716, file_cluster_15: 11.922, file_cluster_12: 12.738
- **Magnitude:** 7175.3 | **LOC:** 12544 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **25**; blast radius 0.218; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (73.7%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 96.3997% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1553`, `dead_code: 7`, `fragile_debt: 2`, `duplicate_logic: 126`
* *Architecture:* `api: 276`, `import: 26`
* *Defense:* `safety: 25`, `doc: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.000315 | `Ripple Effect (Closeness):` 0.015074
  * `Imports (Out-Degree: 24):` ._censored_data, ._constants, ._distn_infrastructure, ._ksstats, ._stats, ._tukeylambda_stats, collections.abc, ctypes...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/special/cdflib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.437)
- **Top Global Matches:** file_cluster_8: 5.437, file_cluster_6: 15.985, file_cluster_3: 20.681
- **Magnitude:** 6733.06 | **LOC:** 5785 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bratio` **(Many-Argument Workhorses)** (Impact: 232.0)
  * `gratio` **(Many-Argument Workhorses)** (Impact: 215.0)
  * `gaminv` **(Many-Argument Workhorses)** (Impact: 202.1)
  * `dinvr` **(Many-Argument Workhorses)** (Impact: 120.1)
  * `dzror` **(Compute Cores)** (Impact: 73.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1427 instances
* *State Mutation (weighted view):* 4404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 892`, `structural_boundaries: 605`, `args: 128`, `func_start: 62`, `class_start: 66`
* *Risk/State:* `state_mutation: 1550`, `unreferenced_by_name: 14`
* *Architecture:* `api: 62`, `import: 1`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cdflib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/tests/test_stats.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.899)
- **Top Global Matches:** file_cluster_15: 6.899, file_cluster_16: 8.785, file_cluster_12: 8.799
- **Magnitude:** 6637.7 | **LOC:** 9490 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.6%), Connectivity (formerly Api Exposure) (14.0%)
- **Documentation Coverage:** 98.2829% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2299`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 466`
* *Architecture:* `io: 4`, `api: 662`, `import: 29`
* *Defense:* `safety: 97`, `doc: 28`, `test: 977`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` .common_tests, collections, contextlib, hypothesis, hypothesis.extra.numpy, itertools, math, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/subprojects/highs/extern/catch.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.54)
- **Top Global Matches:** file_cluster_15: 10.54, file_cluster_11: 11.438, file_cluster_0: 11.661
- **Magnitude:** 6293.78 | **LOC:** 18862 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **54**; blast radius 0.523; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 99.3553% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConsoleAssertionPrinter` **(Many-Argument Workhorses)** (Impact: 67.4)
  * `makeCommandLineParser` **(Compute Cores)** (Impact: 65.9)
  * `XmlEncode::encodeTo` **(Compute Cores)** (Impact: 65.6)
  * `Capturer::Capturer` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `XmlReporter::assertionEnded` **(Compute Cores)** (Impact: 40.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 505 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 1898
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1423`, `structural_boundaries: 4462`, `args: 2086`, `func_start: 1290`, `class_start: 444`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 888`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 26`, `unreferenced_by_name: 500`
* *Architecture:* `io: 3`, `api: 124`, `concurrency: 1`, `import: 293`
* *Defense:* `safety: 536`, `doc: 66`, `test: 321`, `immutability_locks: 2105`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.523
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.002823
  * `Imports (Out-Degree: 1):` AfxWin.h, TargetConditionals.h, algorithm, log.h, atomic, cassert, cctype, cerrno...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/highs/highs/presolve/HPresolve.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.226)
- **Top Global Matches:** file_cluster_6: 7.226, file_cluster_8: 10.602, file_cluster_4: 14.667
- **Magnitude:** 6072.32 | **LOC:** 7482 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HPresolve::rowPresolve` **(Many-Argument Workhorses)** (Impact: 390.9)
  * `HPresolve::detectParallelRowsAndCols` **(Many-Argument Workhorses)** (Impact: 347.3)
  * `HPresolve::computeColBounds` **(Many-Argument Workhorses)** (Impact: 184.0)
  * `HPresolve::dominatedColumns` **(Compute Cores)** (Impact: 158.4)
  * `HPresolve::sparsify` **(Compute Cores)** (Impact: 138.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 803 instances
* *State Mutation (weighted view):* 2514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1741`, `structural_boundaries: 490`, `args: 321`, `func_start: 120`, `class_start: 1`
* *Risk/State:* `state_mutation: 908`, `dead_code: 72`, `planned_debt: 10`, `unreferenced_by_name: 112`
* *Architecture:* `import: 26`
* *Defense:* `safety: 143`, `immutability_locks: 183`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` pdqsort.h, Highs.h, algorithm, atomic, cmath, HighsIO.h, limits, HConst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/odr/odrpack/d_odr.f` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.669)
- **Top Global Matches:** file_cluster_3: 6.669, file_cluster_8: 21.717, file_cluster_6: 34.582
- **Magnitude:** 5981.22 | **LOC:** 10986 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.132; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DODMN` **(I/O & Config Routines)** (Impact: 183.3)
    * *Intent:* *DODMN
  * `DODPC1` **(I/O & Config Routines)** (Impact: 164.1)
    * *Intent:* *DODPC1
  * `DODPC3` **(I/O & Config Routines)** (Impact: 125.2)
    * *Intent:* *DODPC3
  * `DODCHK` **(I/O & Config Routines)** (Impact: 103.1)
    * *Intent:* *DODCHK
  * `DSOLVE` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* *DSOLVE
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 1183 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 3761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1401`, `structural_boundaries: 466`, `args: 98`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 8`, `state_mutation: 1395`
* *Architecture:* `io: 372`, `api: 50`
* *Defense:* `safety: 31`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.132
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/stats/_stats_py.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.86)
- **Top Global Matches:** file_cluster_4: 5.86, file_cluster_6: 8.683, file_cluster_16: 12.537
- **Magnitude:** 5891.78 | **LOC:** 10841 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **24**; blast radius 0.521; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.2%)
- **Documentation Coverage:** 62.6984% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1221`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 101`, `import: 28`
* *Defense:* `safety: 22`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.521
  * `Choke Point (Betweenness):` 0.000778 | `Ripple Effect (Closeness):` 0.019209
  * `Imports (Out-Degree: 23):` ._axis_nan_policy, ._binomtest, ._mstats_basic, ._resampling, ._stats, ._stats_mstats_common, ._stats_pythran, .distributions...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/optimize/__minpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 14.008)
- **Top Global Matches:** file_cluster_3: 14.008, file_cluster_8: 35.103, file_cluster_1: 35.478
- **Magnitude:** 5633.66 | **LOC:** 4379 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.207; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1010`, `dead_code: 6`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `immutability_locks: 166`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 1):` __minpack.h, math.h, stdlib.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/stats/tests/test_distributions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.52)
- **Top Global Matches:** file_cluster_15: 7.52, file_cluster_11: 8.882, file_cluster_16: 9.05
- **Magnitude:** 5426.36 | **LOC:** 10484 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.4%), Connectivity (formerly Api Exposure) (14.0%)
- **Documentation Coverage:** 97.1793% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 1943`, `dead_code: 115`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 7`, `unreferenced_by_name: 412`
* *Architecture:* `io: 7`, `api: 843`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 183`, `doc: 29`, `test: 991`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` .test_discrete_basic, itertools, json, numpy, numpy.lib.recfunctions, numpy.testing, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_distribution_infrastructure.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.55)
- **Top Global Matches:** file_cluster_12: 8.55, file_cluster_16: 8.845, file_cluster_15: 9.953
- **Magnitude:** 4980.14 | **LOC:** 5819 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **18**; blast radius 0.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 98.308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `plot` **(Many-Argument Workhorses)** (Impact: 141.8)
    * *Intent:* ### Convenience
  * `filtered` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `_set_invalid_nan` **(Compute Cores)** (Impact: 65.9)
    * *Intent:* # Wrapper for input / output validation and standardization of distribution # functions that accept ...
  * `_quadrature` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* ## Algorithms
  * `_make_distribution_rv_generic` **(Stateful Encapsulated Methods)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 643 instances
* *State Mutation (weighted view):* 2265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 967`, `args: 450`, `func_start: 433`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 979`, `dead_code: 4`, `planned_debt: 12`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `api: 126`, `import: 20`
* *Defense:* `safety: 34`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 0.000745 | `Ripple Effect (Closeness):` 0.022488
  * `Imports (Out-Degree: 14):` abc, functools, inspect, math, matplotlib.pyplot, numpy, scipy, scipy._lib._array_api...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/sparse/tests/test_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.836)
- **Top Global Matches:** file_cluster_15: 6.836, file_cluster_12: 7.238, file_cluster_16: 8.034
- **Magnitude:** 4594.34 | **LOC:** 5909 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.4%), Guard Balance (formerly Safety Score) (69.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 98.3471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `with_64bit_maxval_limit` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `test_slicing_3` **(Compute Cores)** (Impact: 32.9)
  * `test_argmax` **(Compute Cores)** (Impact: 31.1)
  * `test_minmax_axis` **(I/O & Config Routines)** (Impact: 29.1)
  * `sparse_test_class` **(Many-Argument Workhorses)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 461 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 786`, `args: 360`, `func_start: 358`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 1`, `state_mutation: 1522`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 23`
* *Architecture:* `io: 1`, `api: 353`, `import: 24`
* *Defense:* `safety: 176`, `doc: 14`, `test: 306`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 14):` contextlib, functools, itertools, numpy, numpy.exceptions, numpy.testing, operator, pickle...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/qhull_r/libqhull_r/merge_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.145)
- **Top Global Matches:** file_cluster_6: 6.145, file_cluster_8: 12.078, file_cluster_4: 13.096
- **Magnitude:** 4475.9 | **LOC:** 5591 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.155; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (75.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qh_test_nonsimplicial_merge` **(Many-Argument Workhorses)** (Impact: 178.5)
    * *Intent:* */
  * `qh_mergefacet` **(Many-Argument Workhorses)** (Impact: 163.5)
    * *Intent:* */
  * `qh_all_merges` **(Many-Argument Workhorses)** (Impact: 105.5)
    * *Intent:* */
  * `qh_renamevertex` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* */
  * `qh_appendmergeset` **(Many-Argument Workhorses)** (Impact: 80.7)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 629 instances
* *State Mutation (weighted view):* 1986
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 924`, `structural_boundaries: 191`, `args: 234`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 728`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 92`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001728
  * `Imports (Out-Degree: 12):` qhull_ra.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/qhull_r/libqhull_r/io_r.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.831)
- **Top Global Matches:** file_cluster_6: 6.831, file_cluster_8: 10.933, file_cluster_4: 14.371
- **Magnitude:** 4437.7 | **LOC:** 4129 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 0.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qh_printbegin` **(Many-Argument Workhorses)** (Impact: 338.3)
    * *Intent:* */
  * `qh_readpoints` **(Many-Argument Workhorses)** (Impact: 307.9)
    * *Intent:* */
  * `qh_printafacet` **(Many-Argument Workhorses)** (Impact: 170.4)
    * *Intent:* */
  * `qh_printfacetheader` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* */
  * `qh_printfacets` **(Many-Argument Workhorses)** (Impact: 106.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 551 instances
* *State Mutation (weighted view):* 1703
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 974`, `structural_boundaries: 186`, `args: 110`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 601`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 72`, `import: 1`
* *Defense:* `safety: 20`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002161
  * `Imports (Out-Degree: 13):` qhull_ra.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/integrate/_lebedev.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.761)
- **Top Global Matches:** file_cluster_8: 7.761, file_cluster_6: 17.898, file_cluster_3: 20.12
- **Magnitude:** 4248.32 | **LOC:** 5454 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 3735`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015587
  * `Imports (Out-Degree: 1):` numpy, scipy._lib._array_api
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/optimize/__lbfgsb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.944)
- **Top Global Matches:** file_cluster_3: 7.944, file_cluster_8: 18.116, file_cluster_6: 30.94
- **Magnitude:** 4216.38 | **LOC:** 3768 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.607; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 863`, `dead_code: 26`, `unreferenced_by_name: 1`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.607
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000511
  * `Imports (Out-Degree: 1):` __lbfgsb.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/_lib/pocketfft/pocketfft_hdronly.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.422)
- **Top Global Matches:** file_cluster_4: 7.422, file_cluster_15: 9.611, file_cluster_12: 10.026
- **Magnitude:** 4038.58 | **LOC:** 3636 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%), Guard Balance (formerly Safety Score) (78.8%)
- **Documentation Coverage:** 49.7537% of unit weight undocumented
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
* *Amplified Cascading Flux:* 689 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 2145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 598`, `structural_boundaries: 774`, `args: 278`, `func_start: 190`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 767`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 35`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 31`, `doc: 1`, `sync_locks: 36`, `immutability_locks: 311`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.000511
  * `Imports (Out-Degree: 1):` algorithm, array, atomic, cmath, complex, condition_variable, cstdlib, functional...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsLpUtils.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.18)
- **Top Global Matches:** file_cluster_6: 6.18, file_cluster_4: 9.767, file_cluster_8: 15.942
- **Magnitude:** 4034.6 | **LOC:** 3770 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **13**; blast radius 0.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSolutionFile` **(Many-Argument Workhorses)** (Impact: 222.6)
  * `getSubVectorsTranspose` **(Many-Argument Workhorses)** (Impact: 138.5)
  * `lpDimensionsOk` **(Many-Argument Workhorses)** (Impact: 100.1)
  * `assessLpPrimalSolution` **(Many-Argument Workhorses)** (Impact: 95.0)
    * *Intent:* // Determine validity, primal feasibility and (when relevant) integer // feasibility of a solution
  * `assessSemiVariables` **(Many-Argument Workhorses)** (Impact: 89.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 595 instances
* *State Mutation (weighted view):* 1893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 756`, `structural_boundaries: 209`, `args: 111`, `func_start: 77`
* *Risk/State:* `state_mutation: 703`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 11`, `import: 13`
* *Defense:* `safety: 97`, `doc: 1`, `immutability_locks: 338`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.011996
  * `Imports (Out-Degree: 18):` HConfig.h, algorithm, cassert, Filereader.h, HMPSIO.h, HighsIO.h, HighsLpUtils.h, HighsModelUtils.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/subprojects/highs/highs/simplex/HEkk.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.22)
- **Top Global Matches:** file_cluster_4: 7.22, file_cluster_6: 8.117, file_cluster_15: 14.084
- **Magnitude:** 4015.84 | **LOC:** 4369 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.5%), Debt Markers (formerly Tech Debt) (94.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HEkk::proofOfPrimalInfeasibility` **(Many-Argument Workhorses)** (Impact: 105.7)
  * `HEkk::initialiseBound` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `HEkk::initialiseCost` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `HEkk::returnFromSolve` **(Defensive Guards)** (Impact: 60.8)
  * `HEkk::updateDualSteepestEdgeWeights` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* // Update the DSE weights
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 693 instances
* *State Mutation (weighted view):* 2451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 743`, `structural_boundaries: 175`, `args: 124`, `func_start: 130`
* *Risk/State:* `state_mutation: 1065`, `dead_code: 38`, `planned_debt: 4`, `unreferenced_by_name: 121`
* *Architecture:* `import: 11`
* *Defense:* `safety: 97`, `doc: 1`, `immutability_locks: 272`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 21):` HighsLpSolverObject.h, HighsLpUtils.h, HighsModelUtils.h, HighsSolutionDebug.h, HighsParallel.h, HEkk.h, HEkkDual.h, HEkkPrimal.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/linalg/_matfuncs_expm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.314)
- **Top Global Matches:** file_cluster_8: 11.314, file_cluster_3: 13.474, file_cluster_6: 23.73
- **Magnitude:** 3913.18 | **LOC:** 2384 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pick_pade_structure_z` **(Many-Argument Workhorses)** (Impact: 123.3)
  * `pick_pade_structure_c` **(Many-Argument Workhorses)** (Impact: 123.2)
  * `pick_pade_structure_s` **(Many-Argument Workhorses)** (Impact: 122.8)
    * *Intent:* /******************************************************************************* *******************...
  * `pick_pade_structure_d` **(Many-Argument Workhorses)** (Impact: 122.8)
  * `pade_UV_calc_c` **(Many-Argument Workhorses)** (Impact: 106.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 880 instances
* *State Mutation (weighted view):* 2830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 58`, `args: 133`, `func_start: 20`
* *Risk/State:* `state_mutation: 1070`, `unreferenced_by_name: 8`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.2
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 5):` _matfuncs_expm.h, complex.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.988)
- **Top Global Matches:** file_cluster_4: 7.988, file_cluster_6: 8.871, file_cluster_12: 14.136
- **Magnitude:** 3790.24 | **LOC:** 2741 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 73.5294% of unit weight undocumented
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
* *Structure:* `branch: 755`, `structural_boundaries: 410`, `args: 144`, `func_start: 133`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 774`, `fragile_debt: 7`, `unreferenced_by_name: 16`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 142`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scipy-1.17.1/scipy/stats/_multivariate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.928)
- **Top Global Matches:** file_cluster_16: 6.928, file_cluster_15: 7.41, file_cluster_4: 9.248
- **Magnitude:** 3775.58 | **LOC:** 8050 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **19**; blast radius 0.236; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.2%), Guard Balance (formerly Safety Score) (79.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 51.1156% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 75.3)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure conformality. Par...
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* """ Infer dimensionality from mean or covariance matrices. Handle defaults. Ensure compatible dimens...
  * `_process_parameters` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* """ Infer dimensionality from location array and shape matrix, handle defaults, and ensure compatibl...
  * `_process_parameters_psd` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* # Try to infer dimensionality if dim is None: if mean is None: if cov is None: dim = 1 else: cov = n...
  * `_dirichlet_check_input` **(Stateful Encapsulated Methods)** (Impact: 33.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 435 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1767
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 678`, `args: 309`, `func_start: 309`, `class_start: 39`
* *Risk/State:* `state_mutation: 897`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 205`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 9`, `doc: 216`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.236
  * `Choke Point (Betweenness):` 0.000343 | `Ripple Effect (Closeness):` 0.018105
  * `Imports (Out-Degree: 19):` ._continuous_distns, ._covariance, ._discrete_distns, ._morestats, ._qmvnt, ._rcont, math, numpy...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `scipy-1.17.1/scipy/integrate/src/zvode.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.33)
- **Top Global Matches:** file_cluster_3: 6.33, file_cluster_8: 20.468, file_cluster_6: 33.366
- **Magnitude:** 3741.98 | **LOC:** 2785 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.108; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.2%)
- **Documentation Coverage:** 13.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zvode` **(Many-Argument Workhorses)** (Impact: 648.4)
    * *Intent:* * @param itask Task indicator (1-5) * @param istate State flag (input/output) * @param iopt Optional...
  * `zvstep` **(Many-Argument Workhorses)** (Impact: 335.3)
    * *Intent:* * @param wm Complex work array for matrix operations * @param iwm Integer work array for matrix oper...
  * `zvjac` **(Many-Argument Workhorses)** (Impact: 203.2)
    * *Intent:* * @param wm Complex work space for matrices. On output contains the inverse * diagonal matrix if MIT...
  * `zvnlsd` **(Many-Argument Workhorses)** (Impact: 154.3)
    * *Intent:* * @param y Complex predicted solution vector, updated by corrector * @param yh Complex Nordsieck his...
  * `zvhin` **(Many-Argument Workhorses)** (Impact: 78.0)
    * *Intent:* * @param f User function for right-hand side f(t,y) * @param rpar User real work array * @param ipar...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 645 instances
* *State Mutation (weighted view):* 2058
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 163`, `args: 165`, `func_start: 14`
* *Risk/State:* `state_mutation: 768`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 12`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000256
  * `Imports (Out-Degree: 2):` float.h, math.h, stdlib.h, zvode.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/test_value.hpp` (CPP) | Magnitude: 0.01 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 30, macros: 23, structural_boundaries: 17, immutability_locks: 11
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/detail/rational_horner3_7.hpp` (CPP) | Magnitude: 0.16 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 84, structural_boundaries: 55, immutability_locks: 32
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/ccmath/fmax.hpp` (CPP) | Magnitude: 31.4 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 23, branch: 9, immutability_locks: 7
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/ccmath/fmin.hpp` (CPP) | Magnitude: 31.4 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 23, branch: 9, immutability_locks: 7
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/ccmath/ilogb.hpp` (CPP) | Magnitude: 18.08 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, branch: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `scipy-1.17.1/scipy/io/_fast_matrix_market/fast_matrix_market/include/fast_matrix_market/write_body_threads.hpp` (CPP) | Magnitude: 17.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, branch: 4, core_var_decl: 4
- `scipy-1.17.1/scipy/optimize/tests/test_bracket.py` (PYTHON) | Magnitude: 628.8 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 641, core_var_decl: 235, design_snake_case: 235, structural_boundaries: 178
- `scipy-1.17.1/subprojects/highs/highs/mip/HighsGFkSolve.cpp` (CPP) | Magnitude: 118.28 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 30, structural_boundaries: 26, args: 16
- `scipy-1.17.1/doc/source/_static/scipy-mathjax/jax/output/SVG/autoload/maction.js` (JAVASCRIPT) | Magnitude: 169.26 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 121, state_mutation: 41, core_var_decl: 29, structural_boundaries: 26
- `scipy-1.17.1/doc/source/_static/scipy-mathjax/extensions/TeX/extpfeil.js` (JAVASCRIPT) | Magnitude: 20.06 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 8, core_var_decl: 6, regex_execution: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scipy-1.17.1/subprojects/highs/highs/mip/HighsSearch.h` (CPP) | Magnitude: 53.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 46, immutability_locks: 30, args: 26
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/interpolators/whittaker_shannon.hpp` (CPP) | Magnitude: 12.86 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 15, args: 5, func_start: 5
- `scipy-1.17.1/scipy/_lib/array_api_extra/tests/test_version.py` (PYTHON) | Magnitude: 2.18 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 2, args: 1, func_start: 1
- `scipy-1.17.1/scipy/special/tests/test_boost_ufuncs.py` (PYTHON) | Magnitude: 48.72 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 22, design_snake_case: 21, state_mutation: 19
- `scipy-1.17.1/subprojects/highs/highs/mip/HighsCliqueTable.h` (CPP) | Magnitude: 93.8 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 66, immutability_locks: 53, args: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scipy-1.17.1/scipy/integrate/_dopmodule.c` (C) | Magnitude: 214.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 189, pointers: 85, state_mutation: 39, branch: 37
- `scipy-1.17.1/scipy/optimize/tests/test_linesearch.py` (PYTHON) | Magnitude: 310.72 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 233, structural_boundaries: 83, core_var_decl: 75, design_snake_case: 72
- `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC/memory.c` (C) | Magnitude: 131.42 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 57, pointers: 45, state_mutation: 29, structural_boundaries: 20
- `scipy-1.17.1/subprojects/qhull_r/libqhull_r/mem_r.h` (C) | Magnitude: 48.14 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 52, pointers: 49, structural_boundaries: 30, macros: 29
- `scipy-1.17.1/scipy/sparse/csgraph/tests/test_graph_laplacian.py` (PYTHON) | Magnitude: 276.16 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 269, core_var_decl: 126, design_snake_case: 110, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scipy-1.17.1/scipy/interpolate/_fitpack_py.py` (PYTHON) | Magnitude: 149.78 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 44, core_var_decl: 29, design_snake_case: 29
- `scipy-1.17.1/scipy/spatial/transform/tests/test_rotation_groups.py` (PYTHON) | Magnitude: 112.48 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 55, core_var_decl: 39, test: 32
- `scipy-1.17.1/scipy/ndimage/tests/test_datatypes.py` (PYTHON) | Magnitude: 37.58 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, core_var_decl: 20, design_snake_case: 20, state_mutation: 19
- `scipy-1.17.1/scipy/sparse/_matrix.py` (PYTHON) | Magnitude: 66.68 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 60, api: 22, args: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scipy-1.17.1/scipy/optimize/__init__.py` (PYTHON) | Magnitude: 22.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 55, import: 27, safety_bypasses: 7, indent_spaces: 4
- `scipy-1.17.1/scipy/stats/__init__.py` (PYTHON) | Magnitude: 22.82 | Delta: **0.307** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 65, import: 32, safety_bypasses: 10, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `scipy-1.17.1/scipy/stats/_levy_stable/levyst.pyx` (PYTHON) | Magnitude: 21.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 17, args: 8, func_start: 8
- `scipy-1.17.1/subprojects/xsf/include/xsf/cephes/fresnl.h` (CPP) | Magnitude: 73.66 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 24, core_var_decl: 22, design_snake_case: 22
- `scipy-1.17.1/scipy/_lib/pyprima/pyprima/src/pyprima/common/_linear_constraints.py` (PYTHON) | Magnitude: 62.18 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 22, core_var_decl: 22, design_snake_case: 14
- `scipy-1.17.1/scipy/special/_lambertw.py` (PYTHON) | Magnitude: 7.12 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 3, import: 2, core_var_decl: 2
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/ccmath/scalbln.hpp` (CPP) | Magnitude: 20.9 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, import: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scipy-1.17.1/scipy/integrate/src/lsoda.h` (C) | Magnitude: 11.56 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 12, pointers: 10, immutability_locks: 7
- `scipy-1.17.1/scipy/spatial/_spherical_voronoi.py` (PYTHON) | Magnitude: 146.8 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 44, core_var_decl: 32, design_snake_case: 32
- `scipy-1.17.1/scipy/integrate/src/vode.h` (C) | Magnitude: 11.58 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, pointers: 10, api: 6
- `scipy-1.17.1/scipy/integrate/_ivp/lsoda.py` (PYTHON) | Magnitude: 103.88 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 26, core_var_decl: 22, design_snake_case: 22
- `scipy-1.17.1/subprojects/highs/highs/ipm/basiclu/lu_def.h` (C) | Magnitude: 10.86 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 8, macros: 5, state_mutation: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions/detail/hypergeometric_rational.hpp` (CPP) | Magnitude: 125.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 111, core_var_decl: 64, design_snake_case: 64, state_mutation: 54
- `scipy-1.17.1/subprojects/highs/highs/util/HighsHash.cpp` (CPP) | Magnitude: 11.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 1, immutability_locks: 1
- `scipy-1.17.1/scipy/io/_fast_matrix_market/src/_fmm_core_read_coo.cpp` (CPP) | Magnitude: 13.26 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, pointers: 17, structural_boundaries: 9, scientific: 6
- `scipy-1.17.1/subprojects/highs/extern/filereaderlp/model.hpp` (CPP) | Magnitude: 3.7 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 31, safety: 12, core_var_decl: 12, design_snake_case: 12
- `scipy-1.17.1/scipy/stats/_result_classes.py` (PYTHON) | Magnitude: 16.24 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8, indent_spaces: 3, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/color_maps.hpp` (CPP) | Magnitude: 0.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1839, structural_boundaries: 53, core_var_decl: 23, generics: 16
- `scipy-1.17.1/scipy/special/_ndtri_exp.pxd` (PYTHON) | Magnitude: 36.24 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 9, branch: 8, state_mutation: 6
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/detail/rational_horner3_11.hpp` (CPP) | Magnitude: 0.47 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 404, state_mutation: 308, explicit_casts: 118, structural_boundaries: 83
- `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC/mark_relax.c` (C) | Magnitude: 41.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 11, state_mutation: 8, indent_spaces: 7, pointers: 6
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/special_functions/detail/hypergeometric_1F1_addition_theorems_on_z.hpp` (CPP) | Magnitude: 39.66 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, core_var_decl: 50, design_snake_case: 20, design_upper_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scipy-1.17.1/subprojects/highs/highs/ipm/ipx/sparse_matrix.cc` (CPP) | Magnitude: 501.88 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 282, state_mutation: 97, core_var_decl: 87, design_snake_case: 80
- `scipy-1.17.1/scipy/sparse/_data.py` (PYTHON) | Magnitude: 453.8 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 226, structural_boundaries: 90, core_var_decl: 76, branch: 74
- `scipy-1.17.1/scipy/_lib/tests/test_array_api.py` (PYTHON) | Magnitude: 386.52 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 112, core_var_decl: 109, design_snake_case: 109
- `scipy-1.17.1/scipy/_lib/unuran/unuran/src/parser/functparser_parser.h` (CPP) | Magnitude: 727.92 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 468, pointers: 261, branch: 171, state_mutation: 123
- `scipy-1.17.1/scipy/sparse/linalg/_isolve/tests/test_iterative.py` (PYTHON) | Magnitude: 730.36 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 506, core_var_decl: 253, state_mutation: 216, design_snake_case: 197

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `scipy-1.17.1/scipy/_lib/array_api_extra/tests/test_testing.py` (PYTHON) | Magnitude: 413.98 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 264, core_var_decl: 126, structural_boundaries: 123, design_snake_case: 118
- `scipy-1.17.1/scipy/_lib/array_api_extra/tests/conftest.py` (PYTHON) | Magnitude: 148.88 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 65, branch: 29, core_var_decl: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scipy-1.17.1/scipy/sparse/csgraph/_flow.pyx` (PYTHON) | Magnitude: 353.46 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 248, core_var_decl: 86, design_snake_case: 85, state_mutation: 73
- `scipy-1.17.1/subprojects/highs/extern/pdqsort/pdqsort.h` (CPP) | Magnitude: 567.4 | Delta: **0.164** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 311, state_mutation: 138, structural_boundaries: 117, branch: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scipy-1.17.1/scipy/special/_precompute/lambertw.py` (PYTHON) | Magnitude: 47.36 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, core_var_decl: 26, design_snake_case: 26, state_mutation: 18
- `scipy-1.17.1/subprojects/highs/build_webdemo.sh` (SHELL) | Magnitude: 55.1 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 6, io: 6, branch: 5, state_mutation: 5
- `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC/cutil.c` (C) | Magnitude: 641.68 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 247, indent_spaces: 242, state_mutation: 177, core_var_decl: 57
- `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC/zutil.c` (C) | Magnitude: 641.68 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 247, indent_spaces: 242, state_mutation: 177, core_var_decl: 57
- `scipy-1.17.1/scipy/sparse/linalg/_eigen/__init__.py` (PYTHON) | Magnitude: 18.22 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 11, import: 5, safety_bypasses: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scipy-1.17.1/scipy/sparse/linalg/_dsolve/SuperLU/SRC/colamd.c` (C) | Magnitude: 2012.62 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 721, indent_tabs: 554, state_mutation: 386, branch: 240

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scipy-1.17.1/scipy/_lib/unuran/unuran/src/distributions/vc_multistudent.c` (C) | Magnitude: 275.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 132, state_mutation: 69, pointers: 54, branch: 25
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/ccmath/fdim.hpp` (CPP) | Magnitude: 36.88 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 24, branch: 12, immutability_locks: 7
- `scipy-1.17.1/scipy/linalg/blas.py` (PYTHON) | Magnitude: 229.96 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 46, core_var_decl: 46, design_snake_case: 45
- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/distributions/detail/generic_mode.hpp` (CPP) | Magnitude: 102.24 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 33, core_var_decl: 19, design_snake_case: 19
- `scipy-1.17.1/scipy/stats/_stats_mstats_common.py` (PYTHON) | Magnitude: 155.08 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 81, core_var_decl: 50, design_snake_case: 46, state_mutation: 33

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scipy-1.17.1/subprojects/highs/highs/lp_data/Highs.cpp` -> **Severity: 0.388** (Bridge: 0.0039 * Flux: 99.9952%)
- `scipy-1.17.1/subprojects/highs/highs/lp_data/HighsCallback.cpp` -> **Severity: 0.369** (Bridge: 0.0037 * Flux: 100.0%)
- `scipy-1.17.1/scipy/_lib/unuran/unuran/src/distributions/d_poisson_gen.c` -> **Severity: 0.329** (Bridge: 0.0033 * Flux: 100.0%)
- `scipy-1.17.1/scipy/optimize/__init__.py` -> **Severity: 0.282** (Bridge: 0.0031 * Flux: 91.6827%)
- `scipy-1.17.1/scipy/stats/__init__.py` -> **Severity: 0.215** (Bridge: 0.0023 * Flux: 91.6827%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scipy-1.17.1/scipy/_lib/_testutils.py` -> **Severity: 7.035** (Embedded: 0.0951 * Error Risk: 73.978%)
- `scipy-1.17.1/scipy/_lib/_util.py` -> **Severity: 6.78** (Embedded: 0.0837 * Error Risk: 80.9712%)
- `scipy-1.17.1/scipy/_lib/_array_api.py` -> **Severity: 6.309** (Embedded: 0.0849 * Error Risk: 74.2919%)
- `scipy-1.17.1/scipy/_lib/_docscrape.py` -> **Severity: 6.216** (Embedded: 0.0794 * Error Risk: 78.3172%)
- `scipy-1.17.1/scipy/_lib/deprecation.py` -> **Severity: 5.595** (Embedded: 0.071 * Error Risk: 78.7721%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scipy-1.17.1/subprojects/boost_math/math/include/boost/math/tools/config.hpp` -> **Severity: 2186.3** (Blast Radius: 21.863 * Doc Risk: 100.0%)
- `scipy-1.17.1/scipy/_lib/_docscrape.py` -> **Severity: 1922.791** (Blast Radius: 20.996 * Doc Risk: 91.5789%)
- `scipy-1.17.1/scipy/_lib/_testutils.py` -> **Severity: 1890.583** (Blast Radius: 24.723 * Doc Risk: 76.4706%)
- `scipy-1.17.1/scipy/_lib/deprecation.py` -> **Severity: 1497.972** (Blast Radius: 17.833 * Doc Risk: 84.0%)
- `scipy-1.17.1/scipy/__init__.py` -> **Severity: 1373.1** (Blast Radius: 13.731 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3958 literal sites + 8 sites through wrappers = 3966
- **`memory_alloc`:** 1163 literal sites + 239 sites through wrappers = 1402
- **`panics_and_aborts`:** 5964 literal sites + 69 sites through wrappers = 6033

- `raises` (function, panics_and_aborts, primitive): 40 call sites in 4 files -- `scipy-1.17.1/scipy/_lib/array_api_extra/tests/test_lazy.py`
- `cupdlp_init_zero_vec_double` (macro, memory_alloc, primitive): 34 call sites in 2 files -- `scipy-1.17.1/subprojects/highs/highs/pdlp/cupdlp/glbopts.h`
- `qh_free` (function, memory_alloc, primitive): 21 call sites in 7 files -- `scipy-1.17.1/subprojects/qhull_r/libqhull_r/usermem_r.c`
- `qh_malloc` (function, memory_alloc, primitive): 15 call sites in 5 files -- `scipy-1.17.1/subprojects/qhull_r/libqhull_r/usermem_r.c`
- `CUPDLP_INIT_CUPDLP_VEC` (macro, memory_alloc, primitive): 13 call sites in 1 files -- `scipy-1.17.1/subprojects/highs/highs/pdlp/cupdlp/glbopts.h`
- `_unur_distr_clone` (macro, memory_alloc, via clone): 13 call sites in 6 files -- `scipy-1.17.1/scipy/_lib/unuran/unuran/src/distr/distr_source.h`
- `vec_Alloc` (function, memory_alloc, via cupdlp_init_zero_vec_double): 13 call sites in 1 files -- `scipy-1.17.1/subprojects/highs/highs/pdlp/cupdlp/cupdlp_utils.c`
- `assert_fp_equal` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `scipy-1.17.1/scipy/optimize/tests/test_linesearch.py`
- `qh_exit` (function, panics_and_aborts, primitive): 11 call sites in 5 files -- `scipy-1.17.1/subprojects/qhull_r/libqhull_r/usermem_r.c`
- `CASE_VALUEINDICES_MAKEHISTOGRAM` (macro, memory_alloc, primitive): 10 call sites in 1 files -- `scipy-1.17.1/scipy/ndimage/src/nd_image.c`
- `lu_free` (function, memory_alloc, primitive): 10 call sites in 1 files -- `scipy-1.17.1/subprojects/highs/highs/ipm/basiclu/basiclu_object.c`
- `cupdlp_init_zero_vec_int` (macro, memory_alloc, primitive): 8 call sites in 1 files -- `scipy-1.17.1/subprojects/highs/highs/pdlp/cupdlp/glbopts.h`
*(+52 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 175811 call pairs -- scoped 24.7%, unique 4.2%, ambiguous 22.4%, external 48.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 107591 | 26.6% | 0.0% | 20.1% | 53.3% |
| cpp | 45078 | 27.6% | 5.3% | 36.1% | 31.0% |
| c | 17762 | 12.5% | 27.0% | 8.0% | 52.5% |
| javascript | 4707 | 0.6% | 0.0% | 0.1% | 99.3% |
| fortran | 325 | 26.5% | 55.7% | 0.0% | 17.8% |
| csharp | 175 | 43.4% | 0.0% | 0.0% | 56.6% |
| shell | 139 | 7.2% | 0.0% | 0.0% | 92.8% |
| matlab | 34 | 0.0% | 11.8% | 0.0% | 88.2% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
