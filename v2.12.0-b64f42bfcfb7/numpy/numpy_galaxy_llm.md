# ARCHITECTURAL_BRIEF: numpy
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
- **Scope:** 5091 analyzed artifact(s), 948029 LOC.
- **Load-bearing artifact:** `numpy-2.4.4/numpy/__init__.py` -- 491 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c` -- pulls in 60 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_d_lapack.c` at magnitude 47303.74 (structural weight, not risk).
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
| Total Artifacts | 7702 |
| Analyzed Artifacts (Scanned) | 5091 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2611 |
| Total LOC | 948029 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7923 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2052 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.918 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 185 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 1492 | 283201 | 29.3% |
| PYTHON | 1403 | 292986 | 27.6% |
| CPP | 616 | 94357 | 12.1% |
| JSON | 399 | 4589 | 7.8% |
| PLAINTEXT | 302 | 0 | 5.9% |
| FORTRAN | 166 | 2110 | 3.3% |
| JAVASCRIPT | 149 | 30188 | 2.9% |
| ASSEMBLY | 137 | 232524 | 2.7% |
| RUST | 79 | 480 | 1.6% |
| YAML | 64 | 4799 | 1.3% |
| M4 | 45 | 188 | 0.9% |
| MARKDOWN | 39 | 0 | 0.8% |
| SHELL | 35 | 794 | 0.7% |
| XML | 33 | 4 | 0.6% |
| MAKEFILE | 25 | 303 | 0.5% |
| SWIFT | 25 | 76 | 0.5% |
| JAVA | 21 | 168 | 0.4% |
| OBJECTIVE-C | 19 | 140 | 0.4% |
| BATCH | 8 | 102 | 0.2% |
| CSHARP | 8 | 62 | 0.2% |
| TYPESCRIPT | 6 | 72 | 0.1% |
| YACC | 5 | 30 | 0.1% |
| BMS | 4 | 25 | 0.1% |
| PROTO | 4 | 20 | 0.1% |
| HTML | 2 | 29 | 0.0% |
| CSV | 2 | 629 | 0.0% |
| POWERSHELL | 2 | 83 | 0.0% |
| CSS | 1 | 70 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 5088 |
| cp1252 | cp1252-fallback | 2 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Declarative / Non-Code 13%, Parameter Forwarders Files 7%, Generic / Templated Code Files 7%, Interface Declarations Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4714 | 92.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 342 | 6.7% |
| Static: Minified & Vendor Opaque Mass | 35 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2611*

**Composition by Extension & Reason:**
- `.build`: 1426x Excluded (Unsupported Extension: '.build'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 391x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 54x Unsupported Format (.undeterminable), 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 62x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 14x Excluded (Saturation: Line 25 exceeds 500 chars), 8x Excluded (Saturation: Line 34 exceeds 500 chars), 7x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.dat`: 54x Excluded (Unsupported Extension: '.dat')
- `.vala`: 48x Excluded (Unsupported Extension: '.vala')
- `.wrap`: 42x Excluded (Unsupported Extension: '.wrap')
- `.src`: 38x Excluded (Unsupported Extension: '.src')
- `.d`: 29x Excluded (Unsupported Extension: '.d'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 14x Excluded (Static Asset Blob without Intent: 1430 LOC), 10x Excluded (Static Asset Blob without Intent: 1002 LOC), 2x Excluded (Static Asset Blob without Intent: 1630 LOC)
- `.cu`: 22x Excluded (Unsupported Extension: '.cu')
- `.ini`: 19x Excluded (Unsupported Extension: '.ini'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyf`: 18x Excluded (Unsupported Extension: '.pyf')
- `.meson`: 15x Excluded (Unsupported Extension: '.meson')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 26.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.6 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15246 | 958 | 3 | `numpy-2.4.4/numpy/_core/src/highway/hwy/ops/x86_512-inl.h` |
| cleanup | 375 | 133 | 0 | `numpy-2.4.4/numpy/linalg/umath_linalg.cpp` |
| guards | 49512 | 1776 | 15 | `numpy-2.4.4/numpy/_core/src/highway/hwy/ops/x86_128-inl.h` |
| danger | 16372 | 1240 | 6 | `numpy-2.4.4/numpy/__init__.pyi` |
| concurrency | 1444 | 220 | 0 | `numpy-2.4.4/numpy/random/tests/test_generator_mt19937.py` |
| connectivity | 34047 | 2871 | 12 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| io | 6682 | 667 | 2 | `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` |
| crypto | 18 | 17 | 0 | `numpy-2.4.4/vendored-meson/meson/mesonbuild/wrap/wrap.py` |
| ipc | 807 | 172 | 0 | `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` |
| time | 258 | 53 | 0 | `numpy-2.4.4/numpy/__init__.pyi` |
| serialization | 111 | 37 | 0 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| regex | 1094 | 187 | 0 | `numpy-2.4.4/numpy/f2py/crackfortran.py` |
| events | 213 | 57 | 0 | `numpy-2.4.4/numpy/_core/src/multiarray/alloc.c` |
| tests | 11706 | 311 | 0 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| docs | 6947 | 968 | 2 | `numpy-2.4.4/numpy/_core/_add_newdocs.py` |
| debt | 5427 | 1109 | 2 | `numpy-2.4.4/numpy/__init__.pyi` |
| mutation | 288379 | 2281 | 88 | `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_d_lapack.c` |
| dead_code | 10687 | 2005 | 3 | `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` |
| credential | 20 | 12 | 0 | `numpy-2.4.4/vendored-meson/meson/ci/intel-scripts/cache_exclude_windows.sh` |
| threat | 49 | 21 | 0 | `numpy-2.4.4/doc/source/_static/scipy-mathjax/MathJax.js` |
| ml_ai | 4864 | 910 | 2 | `numpy-2.4.4/numpy/_core/tests/test_einsum.py` |
| ui | 99 | 40 | 0 | `numpy-2.4.4/doc/source/_static/scipy-mathjax/MathJax.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` (Hits: 540)
- `numpy-2.4.4/vendored-meson/meson/unittests/linuxliketests.py` (Hits: 270)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend/ninjabackend.py` (Hits: 176)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`numpy-2.4.4/numpy/__init__.py`) — 491 inbound connections
2. **core.py** (`numpy-2.4.4/numpy/ma/core.py`) — 206 inbound connections
3. **mesonlib.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/mesonlib.py`) — 173 inbound connections
4. **__init__.py** (`numpy-2.4.4/numpy/testing/__init__.py`) — 157 inbound connections
5. **base.h** (`numpy-2.4.4/numpy/_core/src/highway/hwy/base.h`) — 142 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **multiarraymodule.c** (`numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c`) — 60 outbound dependencies
2. **__init__.pyi** (`numpy-2.4.4/numpy/__init__.pyi`) — 54 outbound dependencies
3. **interpreter.py** (`numpy-2.4.4/vendored-meson/meson/mesonbuild/interpreter/interpreter.py`) — 49 outbound dependencies
4. **allplatformstests.py** (`numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py`) — 47 outbound dependencies
5. **__init__.py** (`numpy-2.4.4/numpy/__init__.py`) — 46 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `genfromtxt` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/lib/_npyio_impl.py`) -> Impact: **980.7** | LOC: 748
  * *Intent:* #####-------------------------------------------------------------------------- #---- --- ASCII functions --- #####-----------------------------------...
- `ilaenv_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_lapack.c`) -> Impact: **961.1** | LOC: 628
  * *Intent:* } /* iladlr_ */
- `cgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **774.5** | LOC: 2496
  * *Intent:* /* End of CGEQRF */ } /* cgeqrf_ */
- `zgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **774.5** | LOC: 2508
  * *Intent:* /* End of ZGEQRF */ } /* zgeqrf_ */
- `dgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_d_lapack.c`) -> Impact: **616.8** | LOC: 1730
  * *Intent:* /* End of DGEQRF */ } /* dgeqrf_ */
- `sgesdd_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_s_lapack.c`) -> Impact: **616.8** | LOC: 1732
  * *Intent:* /* End of SGEQRF */ } /* sgeqrf_ */
- `dtrevc_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_d_lapack.c`) -> Impact: **615.1** | LOC: 1225
  * *Intent:* /* End of DSYTRD */ } /* dsytrd_ */
- `strevc_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_s_lapack.c`) -> Impact: **614.8** | LOC: 1220
  * *Intent:* /* End of SSYTRD */ } /* ssytrd_ */
- `zlatrs_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c`) -> Impact: **588.2** | LOC: 1164
  * *Intent:* /* End of ZLATRD */ } /* zlatrd_ */
- `clatrs_` **(Many-Argument Workhorses)** (@ `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c`) -> Impact: **588.1** | LOC: 1161
  * *Intent:* /* End of CLATRD */ } /* clatrd_ */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `numpy-2.4.4/numpy/linalg/lapack_lite` | 15 | 206699.84 | 51.37% | 15.93% |
| `numpy-2.4.4/numpy/_core/src/multiarray` | 110 | 58731.12 | 35.18% | 16.63% |
| `numpy-2.4.4/numpy/_core/tests` | 68 | 40811.08 | 29.32% | 0.0% |
| `numpy-2.4.4/numpy/_core/src/highway/hwy/ops` | 18 | 27247.06 | 35.76% | 8.77% |
| `numpy-2.4.4/vendored-meson/meson/mesonbuild` | 31 | 21056.58 | 64.29% | 17.12% |
| `numpy-2.4.4/numpy/lib` | 64 | 19051.88 | 17.04% | 5.97% |
| `numpy-2.4.4/numpy/_core/src/umath` | 35 | 18234.74 | 43.27% | 13.74% |
| `numpy-2.4.4/numpy/_core` | 65 | 14270.58 | 18.73% | 6.52% |
| `numpy-2.4.4/numpy/f2py` | 35 | 14067.48 | 24.79% | 5.62% |
| `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend` | 12 | 13064.6 | 69.72% | 10.68% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `numpy-2.4.4/numpy/_core/src/highway/.github/workflows/meson_build_test.yml` -> **100.0%** Exposure
- `numpy-2.4.4/numpy/_core/src/npysort/x86-simd-sort/.github/workflows/build-numpy.yml` -> **100.0%** Exposure
- `numpy-2.4.4/numpy/_core/src/npysort/x86-simd-sort/.github/workflows/c-cpp.yml` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_array_coercion.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_core.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `numpy-2.4.4/benchmarks/benchmarks/bench_app.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_indexing.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_itemselection.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_ma.py` -> **100.0%** Exposure
- `numpy-2.4.4/benchmarks/benchmarks/bench_manipulate.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` -> **595** Orphaned Functions | **10** Duplicates
- `numpy-2.4.4/numpy/ma/tests/test_core.py` -> **315** Orphaned Functions | **6** Duplicates
- `numpy-2.4.4/numpy/_core/tests/test_regression.py` -> **277** Orphaned Functions | **0** Duplicates
- `numpy-2.4.4/numpy/lib/tests/test_function_base.py` -> **238** Orphaned Functions | **9** Duplicates
- `numpy-2.4.4/numpy/_core/tests/test_numeric.py` -> **243** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10761` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_d_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 22.944)
- **Top Global Matches:** file_cluster_3: 22.944, file_cluster_1: 26.316, file_cluster_8: 44.436
- **Magnitude:** 47303.74 | **LOC:** 41865 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 68.2% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dgesdd_` **(Many-Argument Workhorses)** (Impact: 616.8)
    * *Intent:* /* End of DGEQRF */ } /* dgeqrf_ */
  * `dtrevc_` **(Many-Argument Workhorses)** (Impact: 615.1)
    * *Intent:* /* End of DSYTRD */ } /* dsytrd_ */
  * `dbdsqr_` **(Many-Argument Workhorses)** (Impact: 533.5)
    * *Intent:* /* End of DBDSDC */ } /* dbdsdc_ */
  * `dlaqr5_` **(Many-Argument Workhorses)** (Impact: 515.9)
    * *Intent:* } /* dlaqr4_ */
  * `dlasd4_` **(Many-Argument Workhorses)** (Impact: 477.3)
    * *Intent:* /* End of DLASD3 */ } /* dlasd3_ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8940 instances
* *State Mutation (weighted view):* 28480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4293`, `structural_boundaries: 391`, `args: 486`, `func_start: 124`
* *Risk/State:* `state_mutation: 10600`, `dead_code: 8`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 369`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000196
  * `Imports (Out-Degree: 6):` config.h, f2c.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_s_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 22.945)
- **Top Global Matches:** file_cluster_3: 22.945, file_cluster_1: 26.316, file_cluster_8: 44.437
- **Magnitude:** 47275.28 | **LOC:** 41692 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%)
- **Documentation Coverage:** 68.2% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sgesdd_` **(Many-Argument Workhorses)** (Impact: 616.8)
    * *Intent:* /* End of SGEQRF */ } /* sgeqrf_ */
  * `strevc_` **(Many-Argument Workhorses)** (Impact: 614.8)
    * *Intent:* /* End of SSYTRD */ } /* ssytrd_ */
  * `sbdsqr_` **(Many-Argument Workhorses)** (Impact: 533.5)
    * *Intent:* /* End of SBDSDC */ } /* sbdsdc_ */
  * `slaqr5_` **(Many-Argument Workhorses)** (Impact: 515.9)
    * *Intent:* } /* slaqr4_ */
  * `slasd4_` **(Many-Argument Workhorses)** (Impact: 477.2)
    * *Intent:* /* End of SLASD3 */ } /* slasd3_ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8920 instances
* *State Mutation (weighted view):* 28422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4293`, `structural_boundaries: 392`, `args: 516`, `func_start: 124`
* *Risk/State:* `state_mutation: 10582`, `dead_code: 8`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 407`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000196
  * `Imports (Out-Degree: 6):` config.h, f2c.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_blas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.364)
- **Top Global Matches:** file_cluster_3: 6.364, file_cluster_8: 23.204, file_cluster_6: 36.16
- **Magnitude:** 37170.98 | **LOC:** 21604 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 68.2% of unit weight undocumented
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
* *Structure:* `branch: 3407`, `structural_boundaries: 284`, `args: 175`, `func_start: 84`
* *Risk/State:* `state_mutation: 8810`, `unreferenced_by_name: 82`
* *Architecture:* `api: 103`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000785
  * `Imports (Out-Degree: 4):` config.h, f2c.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_z_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 23.262)
- **Top Global Matches:** file_cluster_1: 23.262, file_cluster_3: 26.091, file_cluster_8: 47.644
- **Magnitude:** 34592.18 | **LOC:** 29997 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.2%)
- **Documentation Coverage:** 68.2% of unit weight undocumented
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
* *Structure:* `branch: 2852`, `structural_boundaries: 263`, `args: 352`, `func_start: 84`
* *Risk/State:* `state_mutation: 8858`, `dead_code: 6`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 294`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/linalg/lapack_lite/f2c_c_lapack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 23.261)
- **Top Global Matches:** file_cluster_1: 23.261, file_cluster_3: 26.09, file_cluster_8: 47.643
- **Magnitude:** 34590.7 | **LOC:** 29862 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 68.2% of unit weight undocumented
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
* *Structure:* `branch: 2852`, `structural_boundaries: 263`, `args: 368`, `func_start: 84`
* *Risk/State:* `state_mutation: 8855`, `dead_code: 6`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 311`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` config.h, f2c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/tests/test_multiarray.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.419)
- **Top Global Matches:** file_cluster_15: 9.419, file_cluster_12: 10.29, file_cluster_16: 10.655
- **Magnitude:** 7895.76 | **LOC:** 11032 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.0%), Connectivity (formerly Api Exposure) (14.1%)
- **Documentation Coverage:** 98.811% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 21`, `state_mutation: 2650`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 13`, `duplicate_logic: 10`, `unreferenced_by_name: 595`
* *Architecture:* `io: 81`, `api: 864`, `import: 53`
* *Defense:* `safety: 286`, `doc: 19`, `test: 971`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` _testbuffer, builtins, collections.abc, contextlib, ctypes, datetime, decimal, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/f2py/crackfortran.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.12)
- **Top Global Matches:** file_cluster_6: 11.12, file_cluster_8: 12.74, file_cluster_4: 17.74
- **Magnitude:** 5804.2 | **LOC:** 3726 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 0.338; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Complexity Load (formerly Cognitive Load) (89.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 76.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyzeline` **(Many-Argument Workhorses)** (Impact: 514.3)
    * *Intent:* """ Reads each line in the input file in sequence and updates global vars. Effectively reads and col...
  * `analyzevars` **(Many-Argument Workhorses)** (Impact: 241.5)
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
* *Risk/State:* `safety_bypasses: 171`, `high_risk_execution: 9`, `state_mutation: 1182`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 9`
* *Architecture:* `io: 20`, `api: 59`, `import: 12`
* *Defense:* `safety: 59`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.03574
  * `Imports (Out-Degree: 3):` .__version__, .auxfuncs, .symbolic, charset_normalizer, codecs, copy, fileinput, os...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/_core/src/umath/ufunc_object.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.991)
- **Top Global Matches:** file_cluster_8: 6.991, file_cluster_6: 10.959, file_cluster_4: 19.501
- **Magnitude:** 5499.32 | **LOC:** 6807 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 0.204; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyUFunc_GeneralizedFunctionInternal` **(Many-Argument Workhorses)** (Impact: 245.0)
  * `PyUFunc_GenericReduction` **(Many-Argument Workhorses)** (Impact: 192.8)
    * *Intent:* /* * This code handles reduce, reduceat, and accumulate * (accumulate and reduce are special cases o...
  * `ufunc_generic_fastcall` **(Many-Argument Workhorses)** (Impact: 163.9)
    * *Intent:* /* * Main ufunc call implementation. * * This implementation makes use of the "fastcall" way of pass...
  * `PyUFunc_Reduceat` **(Many-Argument Workhorses)** (Impact: 162.9)
    * *Intent:* * * if indices[i+1] <= indices[i]+1 * then the result is array[indices[i]] for that value * * op.acc...
  * `PyUFunc_Accumulate` **(Many-Argument Workhorses)** (Impact: 156.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 760 instances
* *State Mutation (weighted view):* 2371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1017`, `structural_boundaries: 331`, `args: 208`, `func_start: 86`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 851`, `planned_debt: 17`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 16`, `import: 34`
* *Defense:* `safety: 18`, `doc: 16`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.204
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.006293
  * `Imports (Out-Degree: 62):` Python.h, abstractdtypes.h, alloc.h, arrayobject.h, arraywrap.h, common.h, conversion_utils.h, convert_datatype.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/ma/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.863)
- **Top Global Matches:** file_cluster_12: 7.863, file_cluster_4: 8.256, file_cluster_15: 9.437
- **Magnitude:** 5412.16 | **LOC:** 8930 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **206** in-repo importer(s); it depends on **14**; blast radius 9.081; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.7%)
- **Documentation Coverage:** 16.9216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 180.2)
  * `var` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* """ x.__getitem__(y) <==> x[y] Return the item described by i, as a masked array. """
  * `__setitem__` **(Stateful Encapsulated Methods)** (Impact: 47.4)
    * *Intent:* # setitem may put NaNs into integer arrays or occasionally overflow a # float. But this may happen i...
  * `__setmask__` **(Many-Argument Workhorses)** (Impact: 45.5)
    * *Intent:* """ Set the mask. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 796 instances
* *State Mutation (weighted view):* 2610
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 788`, `structural_boundaries: 787`, `args: 268`, `func_start: 267`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1018`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 4`
* *Architecture:* `api: 186`, `import: 15`
* *Defense:* `safety: 131`, `doc: 204`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.081
  * `Choke Point (Betweenness):` 0.000385 | `Ripple Effect (Closeness):` 0.070618
  * `Imports (Out-Degree: 13):` builtins, copy, functools, inspect, numpy, numpy._core, numpy._core.numeric, numpy._core.numerictypes...
  * `Imported By (In-Degree: 206):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/backend/ninjabackend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.67)
- **Top Global Matches:** file_cluster_4: 9.67, file_cluster_5: 12.088, file_cluster_6: 12.315
- **Magnitude:** 5024.82 | **LOC:** 4107 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.271; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%)
- **Documentation Coverage:** 93.1373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_single_compile` **(Many-Argument Workhorses)** (Impact: 163.8)
  * `generate_target` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `generate_link` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `get_rust_compiler_deps_and_args` **(Many-Argument Workhorses)** (Impact: 92.1)
  * `generate_swift_target` **(Many-Argument Workhorses)** (Impact: 68.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 744 instances
* *State Mutation (weighted view):* 2450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 907`, `structural_boundaries: 499`, `args: 164`, `func_start: 161`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 113`, `high_risk_execution: 4`, `state_mutation: 962`, `planned_debt: 7`, `fragile_debt: 20`
* *Architecture:* `io: 176`, `api: 154`, `import: 41`
* *Defense:* `safety: 117`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.012056
  * `Imports (Out-Degree: 20):` .._typing, ..arglist, ..build, ..compilers, ..compilers.c, ..compilers.cs, ..compilers.fortran, ..compilers.rust...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/interpreter/interpreter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.996)
- **Top Global Matches:** file_cluster_4: 8.996, file_cluster_6: 11.819, file_cluster_5: 12.463
- **Magnitude:** 4042.84 | **LOC:** 3612 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **49**; blast radius 1.207; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (97.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%)
- **Documentation Coverage:** 96.8198% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 609`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 88`, `api: 135`, `import: 62`
* *Defense:* `safety: 174`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.207
  * `Choke Point (Betweenness):` 0.000305 | `Ripple Effect (Closeness):` 0.017663
  * `Imports (Out-Degree: 45):` ..ast, ..backend, ..backend.backends, ..build, ..cargo, ..cmake, ..compilers, ..coredata...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/fft/pocketfft/pocketfft_hdronly.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.423)
- **Top Global Matches:** file_cluster_4: 7.423, file_cluster_15: 9.613, file_cluster_12: 10.028
- **Magnitude:** 4038.58 | **LOC:** 3636 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **16**; blast radius 0.773; role: Pure Producer (Foundation)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002118
  * `Imports (Out-Degree: 0):` algorithm, array, atomic, cmath, complex, condition_variable, cstdlib, functional...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/_core/tests/test_umath.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.871)
- **Top Global Matches:** file_cluster_15: 6.871, file_cluster_12: 7.857, file_cluster_11: 8.551
- **Magnitude:** 4011.22 | **LOC:** 4976 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.7%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 96.7213% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__array_ufunc__` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `test_division_int_boundary` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `test_ufunc_override_with_super` **(Compute Cores)** (Impact: 44.0)
    * *Intent:* # NOTE: this class is used in doc/source/user/basics.subclassing.rst # if you make any changes here,...
  * `test_out_wrap_subok` **(Defensive Guards)** (Impact: 32.0)
  * `test_loss_of_precision` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* """Check loss of precision in complex arc* functions"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 543 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 2174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 814`, `args: 380`, `func_start: 345`, `class_start: 97`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 1088`, `dead_code: 1`, `fragile_debt: 10`, `duplicate_logic: 14`, `unreferenced_by_name: 227`
* *Architecture:* `io: 9`, `api: 364`, `import: 20`
* *Defense:* `safety: 116`, `doc: 12`, `test: 414`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` cmath, collections, decimal, fnmatch, fractions, functools, inspect, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/CommonHTML/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/highway/hwy/ops/x86_128-inl.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 13.022)
- **Top Global Matches:** file_cluster_0: 13.022, file_cluster_15: 14.049, file_cluster_16: 14.557
- **Magnitude:** 3741.5 | **LOC:** 14090 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.268; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsConstantRawX86Vec` **(Compute Cores)** (Impact: 56.4)
    * *Intent:* #if HWY_TARGET <= HWY_AVX2
  * `InsertLane` **(Compute Cores)** (Impact: 40.1)
  * `SlideUpLanes` **(Compute Cores)** (Impact: 35.2)
  * `SlideDownLanes` **(Compute Cores)** (Impact: 35.2)
  * `ExtractLane` **(Compute Cores)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 4572`, `args: 2888`, `func_start: 1296`, `class_start: 27`
* *Risk/State:* `state_mutation: 48`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 10`, `duplicate_logic: 10`
* *Architecture:* `api: 72`, `import: 8`
* *Defense:* `safety: 58`, `doc: 128`, `immutability_locks: 2036`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.268
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.013245
  * `Imports (Out-Degree: 4):` emmintrin.h, base.h, inside-inl.h, shared-inl.h, smmintrin.h, stdio.h, tmmintrin.h, wmmintrin.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/_core/src/multiarray/datetime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.056)
- **Top Global Matches:** file_cluster_8: 6.056, file_cluster_6: 10.224, file_cluster_4: 19.009
- **Magnitude:** 3720.6 | **LOC:** 4376 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **16**; blast radius 0.192; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_pyobject_to_timedelta` **(Many-Argument Workhorses)** (Impact: 174.2)
    * *Intent:* * Converts a PyObject * into a timedelta, in any of the forms supported * * If the units metadata is...
  * `datetime_arange` **(Many-Argument Workhorses)** (Impact: 121.6)
  * `NpyDatetime_ConvertPyDateTimeToDatetimeStruct` **(Many-Argument Workhorses)** (Impact: 110.9)
    * *Intent:* * While the C API has PyDate_* and PyDateTime_* functions, the following * implementation just asks ...
  * `convert_pyobject_to_datetime` **(Many-Argument Workhorses)** (Impact: 109.6)
    * *Intent:* * Converts a PyObject * into a datetime, in any of the forms supported. * * If the units metadata is...
  * `compute_datetime_metadata_greatest_common_divisor` **(Many-Argument Workhorses)** (Impact: 93.2)
    * *Intent:* /* * Computes the GCD of the two date-time metadata values. Raises * an exception if there is no rea...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 529 instances
* *State Mutation (weighted view):* 1631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 802`, `structural_boundaries: 377`, `args: 126`, `func_start: 68`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 573`, `dead_code: 1`, `planned_debt: 6`, `unreferenced_by_name: 19`
* *Architecture:* `api: 51`, `import: 16`
* *Defense:* `safety: 14`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.192
  * `Choke Point (Betweenness):` 9.1e-05 | `Ripple Effect (Closeness):` 0.008108
  * `Imports (Out-Degree: 24):` Python.h, _datetime.h, array_method.h, common.h, convert_datatype.h, datetime.h, datetime_strings.h, dtype_transfer.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/__init__.pyi` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.272)
- **Top Global Matches:** file_cluster_5: 7.272, file_cluster_7: 11.321, file_cluster_0: 11.423
- **Magnitude:** 3609.92 | **LOC:** 6203 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **54**; blast radius 4.651; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `std` **(Many-Argument Workhorses)** (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 1824`, `args: 1598`, `func_start: 1598`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 291`, `state_mutation: 97`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 212`
* *Architecture:* `io: 5`, `api: 381`, `import: 59`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.651
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.0537
  * `Imports (Out-Degree: 8):` ._expired_attrs_2_0, ._globals, _typeshed, abc, array, builtins, collections.abc, ctypes...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/unittests/allplatformstests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.226)
- **Top Global Matches:** file_cluster_15: 8.226, file_cluster_12: 8.266, file_cluster_4: 9.027
- **Magnitude:** 3516.24 | **LOC:** 5458 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **47**; blast radius 0.115; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%), Connectivity (formerly Api Exposure) (69.9%)
- **Documentation Coverage:** 81.9355% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_compiler_detection` **(Defensive Guards)** (Impact: 71.6)
    * *Intent:* ''' Test that automatic compiler detection and setting from the environment both work just fine. Thi...
  * `test_introspect_json_dump` **(Compute Cores)** (Impact: 67.1)
  * `test_always_prefer_c_compiler_for_asm` **(Compute Cores)** (Impact: 38.6)
  * `test_install_tag` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* ## And one that doesn't #with mock.patch.object(cc_type, 'INVOKES_LINKER', False): # env.coredata.ge...
  * `test_long_output` **(Compute Cores)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 413 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 1732
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 648`, `args: 247`, `func_start: 236`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 11`, `state_mutation: 906`, `planned_debt: 2`, `fragile_debt: 13`, `duplicate_logic: 3`
* *Architecture:* `io: 540`, `api: 230`, `import: 46`
* *Defense:* `safety: 80`, `doc: 65`, `test: 201`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000196
  * `Imports (Out-Degree: 31):` .baseplatformtests, .helpers, contextlib, glob, json, lxml.etree, mesonbuild, mesonbuild.build...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/build.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.726)
- **Top Global Matches:** file_cluster_5: 8.726, file_cluster_12: 10.888, file_cluster_0: 11.625
- **Magnitude:** 3479.6 | **LOC:** 3364 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **31**; blast radius 1.845; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_kwargs` **(Defensive Guards)** (Impact: 93.2)
  * `post_init` **(Compute Cores)** (Impact: 64.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `process_compilers` **(Defensive Guards)** (Impact: 48.4)
    * *Intent:* ''' Populate self.compilers, which is the list of compilers that this target will use for compiling ...
  * `process_files` **(Many-Argument Workhorses)** (Impact: 46.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 406 instances
* *State Mutation (weighted view):* 1362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 673`, `structural_boundaries: 710`, `args: 293`, `func_start: 291`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 550`, `planned_debt: 4`, `fragile_debt: 9`, `duplicate_logic: 30`
* *Architecture:* `io: 54`, `api: 285`, `import: 33`
* *Defense:* `safety: 143`, `doc: 47`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.845
  * `Choke Point (Betweenness):` 0.000397 | `Ripple Effect (Closeness):` 0.022383
  * `Imports (Out-Degree: 21):` ._typing, .backend.backends, .compilers, .coredata, .dependencies, .environment, .interpreter.interpreter, .interpreter.interpreterobjects...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.644)
- **Top Global Matches:** file_cluster_6: 6.644, file_cluster_4: 10.192, file_cluster_8: 16.343
- **Magnitude:** 3434.84 | **LOC:** 5304 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **38** in-repo importer(s); it depends on **60**; blast radius 0.377; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.0%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 98.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_array_fromobject_generic` **(Many-Argument Workhorses)** (Impact: 112.2)
  * `PyArray_Where` **(Many-Argument Workhorses)** (Impact: 102.7)
    * *Intent:* /*NUMPY_API * Where */
  * `_multiarray_umath_exec` **(Compute Cores)** (Impact: 96.0)
  * `PyArray_MatrixProduct2` **(Many-Argument Workhorses)** (Impact: 76.2)
    * *Intent:* /*NUMPY_API * Numeric.matrixproduct2(a,v,out) * just like inner product but does the swapaxes stuff ...
  * `array_shares_memory_impl` **(Many-Argument Workhorses)** (Impact: 66.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 455 instances
* *State Mutation (weighted view):* 1422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 730`, `structural_boundaries: 384`, `args: 290`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 512`, `planned_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `api: 31`, `import: 61`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.377
  * `Choke Point (Betweenness):` 0.000636 | `Ripple Effect (Closeness):` 0.007961
  * `Imports (Out-Degree: 96):` Python.h, __multiarray_api.c, __ufunc_api.c, _datetime.h, abstractdtypes.h, alloc.h, array_assign.h, array_coercion.h...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/MathJax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.87)
- **Top Global Matches:** file_cluster_12: 8.87, file_cluster_4: 9.739, file_cluster_10: 10.22
- **Magnitude:** 3425.02 | **LOC:** 3314 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 94.5341% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processString` **(Defensive Guards)** (Impact: 61.5)
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
* *Structure:* `branch: 874`, `structural_boundaries: 535`, `args: 252`, `func_start: 227`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 8`, `state_mutation: 618`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 22`
* *Architecture:* `io: 2`, `concurrency: 13`
* *Defense:* `safety: 244`, `doc: 13`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/SVG/jax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.891)
- **Top Global Matches:** file_cluster_4: 8.891, file_cluster_6: 10.302, file_cluster_12: 13.448
- **Magnitude:** 3407.42 | **LOC:** 2268 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Guard Balance (formerly Safety Score) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Add` **(Many-Argument Workhorses)** (Impact: 113.3)
  * `HandleVariant` **(Many-Argument Workhorses)** (Impact: 106.0)
  * `toSVG` **(Compute Cores)** (Impact: 75.1)
  * `length2em` **(Defensive Guards)** (Impact: 57.2)
  * `preTranslate` **(Compute Cores)** (Impact: 53.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 584 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1845
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 737`, `structural_boundaries: 383`, `args: 116`, `func_start: 110`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 2`, `state_mutation: 677`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 4`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 138`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `numpy-2.4.4/numpy/_core/src/npysort/timsort.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.814)
- **Top Global Matches:** file_cluster_12: 8.814, file_cluster_4: 9.851, file_cluster_5: 10.212
- **Magnitude:** 3365.16 | **LOC:** 2927 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%)
- **Documentation Coverage:** 99.0476% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000196
  * `Imports (Out-Degree: 4):` cstdlib, npy_sort.h, npysort_common.h, numpy_tag.h, utility
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/numpy/lib/_function_base_impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.844)
- **Top Global Matches:** file_cluster_4: 5.844, file_cluster_6: 9.176, file_cluster_16: 11.882
- **Magnitude:** 3273.28 | **LOC:** 5761 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **16**; blast radius 1.104; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.1%)
- **Documentation Coverage:** 50.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cov` **(Many-Argument Workhorses)** (Impact: 127.8)
  * `_quantile` **(Many-Argument Workhorses)** (Impact: 111.3)
  * `gradient` **(Many-Argument Workhorses)** (Impact: 102.4)
    * *Intent:* """ Return the gradient of an N-dimensional array. The gradient is computed using second order accur...
  * `delete` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* """ Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this retu...
  * `insert` **(Many-Argument Workhorses)** (Impact: 53.8)
    * *Intent:* """ Insert values along the given axis before the given indices. Parameters ---------- arr : array_l...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 532 instances
* *State Mutation (weighted view):* 1673
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 473`, `structural_boundaries: 293`, `args: 122`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 609`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 42`, `import: 17`
* *Defense:* `safety: 27`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.104
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.057408
  * `Imports (Out-Degree: 14):` builtins, collections.abc, functools, numpy, numpy._core, numpy._core._multiarray_umath, numpy._core.fromnumeric, numpy._core.multiarray...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `numpy-2.4.4/vendored-meson/meson/mesonbuild/mtest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.701)
- **Top Global Matches:** file_cluster_4: 9.701, file_cluster_5: 9.8, file_cluster_12: 10.905
- **Magnitude:** 3238.86 | **LOC:** 2319 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **32**; blast radius 0.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.1631% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log` **(Many-Argument Workhorses)** (Impact: 97.5)
    * *Intent:* """Log a single test case."""
  * `parse_line` **(Many-Argument Workhorses)** (Impact: 88.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `_run_tests` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `parse` **(Defensive Guards)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 352 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 452
* *State Mutation (weighted view):* 1178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 470`, `args: 149`, `func_start: 147`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 11`, `state_mutation: 474`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 47`, `api: 157`, `concurrency: 112`, `import: 33`
* *Defense:* `safety: 64`, `doc: 6`, `test: 4`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.000874
  * `Imports (Out-Degree: 8):` .backend.backends, .build, .coredata, .environment, .mesonlib, .mlog, .options, .programs...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `numpy-2.4.4/numpy/_core/src/highway/hwy/contrib/algo/transform-inl.h` (CPP) | Magnitude: 1.26 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 108, core_var_decl: 52, immutability_locks: 46, structural_boundaries: 44
- `numpy-2.4.4/numpy/_core/src/highway/hwy/tests/shift_test.cc` (CPP) | Magnitude: 296.2 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 500, structural_boundaries: 178, core_var_decl: 176, design_snake_case: 141
- `numpy-2.4.4/numpy/_core/src/highway/hwy/tests/cast_test.cc` (CPP) | Magnitude: 38.48 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 156, args: 71, structural_boundaries: 53, macros: 42
- `numpy-2.4.4/vendored-meson/meson/test cases/common/138 C and CPP link/foo.cpp` (CPP) | Magnitude: 3.58 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 7, args: 3, indent_spaces: 3, immutability_locks: 2
- `numpy-2.4.4/numpy/_core/src/highway/hwy/tests/reverse_test.cc` (CPP) | Magnitude: 146.08 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 86, core_var_decl: 58, args: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `numpy-2.4.4/doc/source/_static/scipy-mathjax/jax/output/SVG/autoload/maction.js` (JAVASCRIPT) | Magnitude: 169.26 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 121, state_mutation: 41, core_var_decl: 29, structural_boundaries: 26
- `numpy-2.4.4/doc/source/_static/scipy-mathjax/extensions/TeX/extpfeil.js` (JAVASCRIPT) | Magnitude: 20.06 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 8, core_var_decl: 6, regex_execution: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `numpy-2.4.4/numpy/_core/tests/test_longdouble.py` (PYTHON) | Magnitude: 153.48 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 195, structural_boundaries: 124, core_var_decl: 81, design_snake_case: 80
- `numpy-2.4.4/numpy/_core/src/highway/hwy/tests/swizzle_block_test.cc` (CPP) | Magnitude: 119.92 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 186, structural_boundaries: 83, core_var_decl: 62, pointers: 55
- `numpy-2.4.4/numpy/_core/src/highway/hwy/stats.h` (CPP) | Magnitude: 108.36 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 36, immutability_locks: 30, core_var_decl: 30
- `numpy-2.4.4/numpy/_core/src/highway/hwy/tests/minmax128_test.cc` (CPP) | Magnitude: 104.46 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 111, core_var_decl: 32, structural_boundaries: 30, design_snake_case: 28
- `numpy-2.4.4/numpy/_core/src/highway/hwy/bit_set.h` (CPP) | Magnitude: 148.4 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 258, pointers: 81, immutability_locks: 80, structural_boundaries: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `numpy-2.4.4/numpy/typing/tests/data/pass/array_constructors.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: core_var_decl: 37, design_snake_case: 33, structural_boundaries: 13, state_mutation: 5
- `numpy-2.4.4/numpy/_core/src/common/npy_hashtable.h` (CPP) | Magnitude: 15.68 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: pointers: 12, macros: 7, indent_spaces: 6, args: 5
- `numpy-2.4.4/numpy/_core/src/highway/hwy/profiler.h` (CPP) | Magnitude: 250.36 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 400, structural_boundaries: 108, core_var_decl: 85, immutability_locks: 84
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/scripts/clangtidy.py` (PYTHON) | Magnitude: 70.42 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 25, branch: 15, core_var_decl: 15
- `numpy-2.4.4/numpy/_core/src/multiarray/abstractdtypes.c` (C) | Magnitude: 213.82 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 294, pointers: 88, branch: 74, structural_boundaries: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `numpy-2.4.4/numpy/distutils/tests/test_build_ext.py` (PYTHON) | Magnitude: 18.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, io: 8, core_var_decl: 8
- `numpy-2.4.4/vendored-meson/meson/test cases/csharp/3 resource/resprog.cs` (CSHARP) | Magnitude: 4.4 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, api: 3, class_start: 2
- `numpy-2.4.4/numpy/lib/_ufunclike_impl.py` (PYTHON) | Magnitude: 38.3 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 16, core_var_decl: 15, design_snake_case: 15
- `numpy-2.4.4/numpy/f2py/tests/test_regression.py` (PYTHON) | Magnitude: 92.78 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 59, core_var_decl: 37, design_snake_case: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `numpy-2.4.4/numpy/f2py/tests/src/regression/lower_f2py_fortran.f90` (FORTRAN) | Magnitude: 2.78 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, args: 1, func_start: 1
- `numpy-2.4.4/numpy/_utils/_convertions.py` (PYTHON) | Magnitude: 12.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 3, branch: 2
- `numpy-2.4.4/numpy/polynomial/tests/test_symbol.py` (PYTHON) | Magnitude: 139.74 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 47, state_mutation: 43, core_var_decl: 42
- `numpy-2.4.4/numpy/_core/src/npysort/x86-simd-sort/tests/test-objqsort.cpp` (CPP) | Magnitude: 33.84 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 13, pointers: 9, state_mutation: 7
- `numpy-2.4.4/numpy/_core/src/umath/svml/linux/avx512/svml_z0_expm1_h_la.s` (ASSEMBLY) | Magnitude: 19.1 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 16, indent_tabs: 15, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `numpy-2.4.4/vendored-meson/meson/test cases/common/282 test args and depends in path/test.c` (C) | Magnitude: 14.62 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, pointers: 16, structural_boundaries: 10, args: 6
- `numpy-2.4.4/numpy/f2py/tests/test_string.py` (PYTHON) | Magnitude: 71.2 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 25, core_var_decl: 22, design_snake_case: 22
- `numpy-2.4.4/vendored-meson/meson/test cases/java/9 jni/src/com/mesonbuild/JniTest.java` (JAVA) | Magnitude: 6.44 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, args: 2, func_start: 2
- `numpy-2.4.4/numpy/lib/mixins.py` (PYTHON) | Magnitude: 61.54 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 58, core_var_decl: 28, design_snake_case: 28, structural_boundaries: 27
- `numpy-2.4.4/numpy/_core/src/_simd/_simd_vector.inc` (C) | Magnitude: 109.86 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 117, pointers: 50, branch: 26, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `numpy-2.4.4/numpy/_core/src/common/simd/neon/math.h` (C) | Magnitude: 73.92 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 227, macros: 110, core_var_decl: 86, design_snake_case: 86
- `numpy-2.4.4/numpy/_core/src/multiarray/conversion_utils.h` (C) | Magnitude: 30.3 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: pointers: 38, api: 27, args: 23, structural_boundaries: 9
- `numpy-2.4.4/vendored-meson/meson/test cases/unit/88 multiple envvars/prog.cpp` (CPP) | Magnitude: 2.18 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: macros: 6, indent_spaces: 2, structural_boundaries: 1, args: 1
- `numpy-2.4.4/numpy/_core/src/highway/hwy/contrib/thread_pool/topology.h` (CPP) | Magnitude: 0.04 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, core_var_decl: 21, design_snake_case: 18, structural_boundaries: 10
- `numpy-2.4.4/numpy/f2py/tests/src/crackfortran/privatemod.f90` (FORTRAN) | Magnitude: 4.9 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, args: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `numpy-2.4.4/numpy/_core/src/multiarray/calculation.h` (C) | Magnitude: 36.96 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 21, api: 21, pointers: 9, indent_spaces: 3
- `numpy-2.4.4/numpy/random/src/pcg64/pcg64.orig.c` (C) | Magnitude: 19.68 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 5, api: 5, structural_boundaries: 4, pointers: 3
- `numpy-2.4.4/vendored-meson/meson/test cases/rust/28 mixed/main.cc` (CPP) | Magnitude: 2.16 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, state_mutation: 1
- `numpy-2.4.4/numpy/_core/src/common/npy_cpu_features.h` (C) | Magnitude: 22.92 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 70, core_var_decl: 69, design_upper_case: 69, design_long_vars: 20
- `numpy-2.4.4/vendored-meson/meson/test cases/fortran/7 generated/prog.f90` (FORTRAN) | Magnitude: 2.52 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, safety: 2, import: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/machinefile.py` (PYTHON) | Magnitude: 127.34 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 48, branch: 33, safety: 22
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/mtest.py` (PYTHON) | Magnitude: 3238.86 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1726, branch: 571, state_mutation: 474, structural_boundaries: 470
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/scripts/symbolextractor.py` (PYTHON) | Magnitude: 308.92 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 221, structural_boundaries: 81, branch: 73, core_var_decl: 56
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/modules/python.py` (PYTHON) | Magnitude: 664.52 | Delta: **0.169** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 404, state_mutation: 142, structural_boundaries: 129, branch: 113
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/modules/gnome.py` (PYTHON) | Magnitude: 2164.38 | Delta: **0.176** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1864, core_var_decl: 499, design_snake_case: 493, state_mutation: 485

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `numpy-2.4.4/vendored-meson/meson/run_unittests.py` (PYTHON) | Magnitude: 127.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 33, branch: 26, state_mutation: 26
- `numpy-2.4.4/numpy/typing/tests/data/pass/literal.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, import: 6, state_mutation: 5
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/mconf.py` (PYTHON) | Magnitude: 468.52 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 283, branch: 107, structural_boundaries: 89, state_mutation: 74
- `numpy-2.4.4/numpy/_core/src/npysort/x86-simd-sort/src/avx2-emu-funcs.hpp` (CPP) | Magnitude: 185.58 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 256, structural_boundaries: 143, core_var_decl: 72, design_snake_case: 63
- `numpy-2.4.4/numpy/typing/tests/data/reveal/polynomial_series.pyi` (PYTHON) | Magnitude: 0.02 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, core_var_decl: 10, safety_bypasses: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `numpy-2.4.4/numpy/f2py/src/fortranobject.c` (C) | Magnitude: 1276.66 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 989, branch: 261, pointers: 231, state_mutation: 201

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `numpy-2.4.4/doc/Makefile` (MAKEFILE) | Magnitude: 46.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 99, debug_prints: 37, func_start: 24, io: 22
- `numpy-2.4.4/numpy/polynomial/laguerre.pyi` (PYTHON) | Magnitude: 19.86 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, immutability_locks: 30, structural_boundaries: 13, import: 5
- `numpy-2.4.4/numpy/polynomial/legendre.pyi` (PYTHON) | Magnitude: 19.86 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, immutability_locks: 30, structural_boundaries: 13, import: 5
- `numpy-2.4.4/numpy/_core/src/umath/_struct_ufunc_tests.c` (C) | Magnitude: 66.32 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, state_mutation: 25, pointers: 23, core_var_decl: 16
- `numpy-2.4.4/numpy/_typing/_scalars.py` (PYTHON) | Magnitude: 15.24 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: core_var_decl: 10, design_pascal_case: 10, structural_boundaries: 4, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `numpy-2.4.4/numpy/_core/src/highway/hwy/contrib/math/math_tan_test.cc` (CPP) | Magnitude: 2.46 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 337, core_var_decl: 113, design_snake_case: 102, immutability_locks: 87
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/scripts/pycompile.py` (PYTHON) | Magnitude: 53.32 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, core_var_decl: 15, design_snake_case: 15, branch: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `numpy-2.4.4/numpy/__init__.py` -> **Severity: 0.3** (Bridge: 0.0037 * Flux: 81.3464%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/utils/universal.py` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 100.0%)
- `numpy-2.4.4/numpy/f2py/__init__.py` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 91.6827%)
- `numpy-2.4.4/numpy/f2py/f2py2e.py` -> **Severity: 0.066** (Bridge: 0.0007 * Flux: 100.0%)
- `numpy-2.4.4/numpy/_core/src/multiarray/multiarraymodule.c` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 99.9976%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `numpy-2.4.4/numpy/ma/core.py` -> **Severity: 5.933** (Embedded: 0.0706 * Error Risk: 84.0153%)
- `numpy-2.4.4/numpy/lib/_npyio_impl.py` -> **Severity: 5.093** (Embedded: 0.0629 * Error Risk: 81.0403%)
- `numpy-2.4.4/numpy/distutils/misc_util.py` -> **Severity: 5.036** (Embedded: 0.0596 * Error Risk: 84.5428%)
- `numpy-2.4.4/numpy/lib/_function_base_impl.py` -> **Severity: 4.975** (Embedded: 0.0574 * Error Risk: 86.6618%)
- `numpy-2.4.4/numpy/lib/_arraypad_impl.py` -> **Severity: 4.971** (Embedded: 0.0572 * Error Risk: 86.9707%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `numpy-2.4.4/numpy/__init__.py` -> **Severity: 2105.001** (Blast Radius: 29.47 * Doc Risk: 71.4286%)
- `numpy-2.4.4/numpy/_core/__init__.py` -> **Severity: 965.5** (Blast Radius: 9.655 * Doc Risk: 100.0%)
- `numpy-2.4.4/numpy/_utils/_convertions.py` -> **Severity: 943.1** (Blast Radius: 9.431 * Doc Risk: 100.0%)
- `numpy-2.4.4/vendored-meson/meson/mesonbuild/mlog.py` -> **Severity: 833.048** (Blast Radius: 8.628 * Doc Risk: 96.5517%)
- `numpy-2.4.4/numpy/_core/src/highway/hwy/base.h` -> **Severity: 758.3** (Blast Radius: 7.583 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2245 literal sites + 31 sites through wrappers = 2276
- **`memory_alloc`:** 192 literal sites + 87 sites through wrappers = 279
- **`panics_and_aborts`:** 4979 literal sites + 103 sites through wrappers = 5082

- `assert_poly_almost_equal` (function, panics_and_aborts, primitive): 72 call sites in 1 files -- `numpy-2.4.4/numpy/polynomial/tests/test_classes.py`
- `NPY_AUXDATA_FREE` (macro, memory_alloc, primitive): 45 call sites in 10 files -- `numpy-2.4.4/numpy/_core/include/numpy/ndarraytypes.h`
- `NPY_traverse_info_xfree` (function, memory_alloc, via NPY_AUXDATA_FREE): 15 call sites in 5 files -- `numpy-2.4.4/numpy/_core/src/multiarray/dtype_traversal.h`
- `PyDataMem_FREE` (function, memory_alloc, primitive): 14 call sites in 3 files -- `numpy-2.4.4/numpy/_core/src/multiarray/alloc.c`
- `verbose_git` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `numpy-2.4.4/vendored-meson/meson/mesonbuild/wrap/wrap.py`
- `f1` (function, debug_prints, primitive): 4 call sites in 2 files -- `numpy-2.4.4/doc/source/f2py/code/extcallback.f`
- `f1` (function, panics_and_aborts, primitive): 4 call sites in 2 files -- `numpy-2.4.4/doc/source/f2py/code/extcallback.f`
- `func2` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `numpy-2.4.4/numpy/_core/tests/test_errstate.py`
- `subprocess_call` (function, debug_prints, primitive): 4 call sites in 1 files -- `numpy-2.4.4/vendored-meson/meson/run_tests.py`
- `_kind_name` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `numpy-2.4.4/numpy/_core/_dtype.py`
- `_subarray_broadcast_data_free` (function, memory_alloc, via NPY_traverse_info_xfree): 3 call sites in 1 files -- `numpy-2.4.4/numpy/_core/src/multiarray/dtype_transfer.c`
- `alexandria_visit` (function, debug_prints, primitive): 3 call sites in 3 files -- `numpy-2.4.4/vendored-meson/meson/test cases/unit/17 prebuilt shared/alexandria.c`
*(+28 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 146064 call pairs -- scoped 30.1%, unique 4.9%, ambiguous 23.3%, external 41.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 79370 | 36.2% | 0.0% | 28.7% | 35.1% |
| cpp | 40330 | 28.6% | 5.5% | 27.3% | 38.6% |
| c | 21161 | 17.1% | 23.1% | 1.3% | 58.5% |
| javascript | 4708 | 0.6% | 0.0% | 0.1% | 99.3% |
| shell | 269 | 5.9% | 0.0% | 0.0% | 94.1% |
| rust | 117 | 23.1% | 0.0% | 5.1% | 71.8% |
| fortran | 51 | 21.6% | 9.8% | 17.6% | 51.0% |
| java | 28 | 32.1% | 0.0% | 14.3% | 53.6% |
| csharp | 12 | 16.7% | 16.7% | 0.0% | 66.7% |
| objective-c | 10 | 20.0% | 0.0% | 10.0% | 70.0% |

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
