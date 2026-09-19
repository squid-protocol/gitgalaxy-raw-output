# ARCHITECTURAL_BRIEF: rapidfuzz
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2463 analyzed artifact(s), 449465 LOC.
- **Load-bearing artifact:** `rapidfuzz-3.14.3/extern/taskflow/taskflow/taskflow.hpp` -- 102 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/tbb.h` -- pulls in 52 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/stereo/lodepng.cpp` at magnitude 7863.56 (structural weight, not risk).
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
| Total Artifacts | 3240 |
| Analyzed Artifacts (Scanned) | 2463 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 777 |
| Total LOC | 449465 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7643 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1127 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.3753 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 151 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1995 | 368184 | 81.0% |
| PYTHON | 112 | 13696 | 4.5% |
| PLAINTEXT | 72 | 0 | 2.9% |
| MAKEFILE | 58 | 2399 | 2.4% |
| FORTRAN | 51 | 24137 | 2.1% |
| HTML | 51 | 14581 | 2.1% |
| C | 29 | 10152 | 1.2% |
| MARKDOWN | 20 | 0 | 0.8% |
| SHELL | 17 | 561 | 0.7% |
| XML | 17 | 13 | 0.7% |
| ASSEMBLY | 12 | 1031 | 0.5% |
| M4 | 10 | 191 | 0.4% |
| CSS | 7 | 13335 | 0.3% |
| OBJECTIVE-C | 5 | 192 | 0.2% |
| JAVASCRIPT | 3 | 921 | 0.1% |
| YAML | 2 | 57 | 0.1% |
| BATCH | 1 | 6 | 0.0% |
| JSON | 1 | 9 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `3.748`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.75; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 21%, Data / Markup / Trivial 17%, Declarative / Non-Code 14%, Many-Argument Workhorses Files 8%, Parameter Forwarders Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2360 | 95.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 92 | 3.7% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 777*

**Composition by Extension & Reason:**
- `.dox`: 165x Excluded (Unsupported Extension: '.dox')
- `no_extension`: 64x Unsupported Format (.undeterminable), 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.dot`: 81x Excluded (Unsupported Extension: '.dot')
- `.cmake`: 62x Excluded (Unsupported Extension: '.cmake')
- `.png`: 53x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 2x Excluded (Machine-Generated Source Code Signature: 203 LOC), 2x Excluded (Machine-Generated Source Code Signature: 220 LOC), 2x Excluded (Machine-Generated Source Code Signature: 156 LOC)
- `.cu`: 43x Excluded (Unsupported Extension: '.cu')
- `.vcxproj`: 29x Excluded (Unsupported Extension: '.vcxproj')
- `.sln`: 23x Excluded (Unsupported Extension: '.sln')
- `.windows`: 22x Excluded (Unsupported Extension: '.windows')
- `.dat`: 15x Excluded (Unsupported Extension: '.dat')
- `.cpp`: 11x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.pdf`: 10x Excluded (Explicitly Denied Extension: '.pdf')
- `.map`: 10x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.cxx`: 2x Excluded (Monolithic Amalgamation: 30465 LOC exceeds safe regex boundaries), 2x Excluded (Machine-Generated Source Code Signature: 16265 LOC), 1x Excluded (Machine-Generated Source Code Signature: 7891 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.5 | 14.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 53.5 | 66.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.4 | 93.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 61492 | 1427 | 59 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/stereo/lodepng.cpp` |
| cleanup | 695 | 225 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbbmalloc/frontend.cpp` |
| guards | 44257 | 1484 | 40 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/misc/lapacke.h` |
| danger | 5192 | 586 | 4 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/internal/_flow_graph_trace_impl.h` |
| concurrency | 2623 | 241 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/spdlog/details/registry-inl.h` |
| connectivity | 6723 | 1083 | 8 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/httplib/httplib.hpp` |
| io | 3182 | 174 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/cblat2.f` |
| crypto | 0 | 0 | 0 | - |
| ipc | 608 | 64 | 0 | `rapidfuzz-3.14.3/extern/taskflow/unittests/test_pipelines.cpp` |
| time | 91 | 28 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/spdlog/fmt/bundled/chrono.h` |
| serialization | 584 | 15 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/cblat2.f` |
| regex | 80 | 16 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/httplib/httplib.hpp` |
| events | 595 | 84 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/spdlog/fmt/bundled/format.h` |
| tests | 4458 | 62 | 0 | `rapidfuzz-3.14.3/extern/taskflow/unittests/test_data_pipelines.cpp` |
| docs | 13077 | 804 | 12 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/nlohmann/json.hpp` |
| debt | 4501 | 791 | 6 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` |
| mutation | 116506 | 1890 | 108 | `rapidfuzz-3.14.3/extern/taskflow/sandbox/fft/fft.c` |
| dead_code | 6062 | 1375 | 6 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbbmalloc/frontend.cpp` |
| credential | 1 | 1 | 0 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/httplib/httplib.hpp` |
| threat | 7936 | 1155 | 5 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/misc/lapacke.h` |
| ml_ai | 1867 | 261 | 1 | `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/bench/tensors/tensor_benchmarks.h` |
| ui | 796 | 52 | 0 | `rapidfuzz-3.14.3/extern/taskflow/tfprof/css/bootstrap/4.4.1/bootstrap.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/cblat2.f` (Hits: 212)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/zblat2.f` (Hits: 212)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/dblat2.f` (Hits: 211)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **taskflow.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/taskflow.hpp`) — 102 inbound connections
2. **algorithm.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/algorithm/algorithm.hpp`) — 86 inbound connections
3. **tbb_stddef.h** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/tbb_stddef.h`) — 68 inbound connections
4. **types.h** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/parallel_for/tachyon/src/types.h`) — 53 inbound connections
5. **utilities.h** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/bench/btl/generic_bench/utils/utilities.h`) — 51 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tbb.h** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/tbb.h`) — 52 outbound dependencies
2. **httplib.hpp** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/httplib/httplib.hpp`) — 49 outbound dependencies
3. **flow_graph.h** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/flow_graph.h`) — 39 outbound dependencies
4. **json.hpp** (`rapidfuzz-3.14.3/extern/taskflow/3rd-party/nlohmann/json.hpp`) — 33 outbound dependencies
5. **traits.hpp** (`rapidfuzz-3.14.3/extern/taskflow/sandbox/utility/traits.hpp`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_getopt_internal_r_a` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/ff/platforms/getopt.hpp`) -> Impact: **449.5** | LOC: 350
- `_getopt_internal_r_w` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/ff/platforms/getopt.hpp`) -> Impact: **449.5** | LOC: 350
- `parse_cbor_internal` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/nlohmann/json.hpp`) -> Impact: **447.8** | LOC: 434
  * *Intent:* */
- `EigenFloatContractionKernelInternal` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/unsupported/Eigen/CXX11/src/Tensor/TensorContractionCuda.h`) -> Impact: **353.2** | LOC: 365
- `ctbmv_` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/f2c/ctbmv.c`) -> Impact: **345.3** | LOC: 632
  * *Intent:* */ #include "datatypes.h"
- `ztbmv_` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/f2c/ztbmv.c`) -> Impact: **345.3** | LOC: 632
  * *Intent:* */ #include "datatypes.h"
- `Executor::_wait_for_task` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp`) -> Impact: **313.2** | LOC: 930
  * *Intent:* // Function: _wait_for_task
- `extract_iter` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp_impl.pyx`) -> Impact: **307.1** | LOC: 372
- `main` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/logic_sim/test_all.cpp`) -> Impact: **306.6** | LOC: 589
  * *Intent:* #endif // __TBB_FLOW_GRAPH_CPP11_FEATURES
- `parse_msgpack_internal` **(Compute Cores)** (@ `rapidfuzz-3.14.3/extern/taskflow/3rd-party/nlohmann/json.hpp`) -> Impact: **293.4** | LOC: 369
  * *Intent:* ///////////// // MsgPack // ///////////// /*! */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing` | 14 | 26575.34 | 47.55% | 0.0% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/ff` | 59 | 18175.32 | 46.33% | 35.61% |
| `rapidfuzz-3.14.3/extern/taskflow/unittests` | 30 | 15000.88 | 71.59% | 9.43% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/unsupported/Eigen/CXX11/src/Tensor` | 70 | 11932.5 | 30.63% | 60.6% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/f2c` | 21 | 10135.58 | 70.89% | 25.12% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbb` | 71 | 9991.32 | 40.85% | 54.83% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb` | 65 | 8983.84 | 18.06% | 25.89% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/products` | 21 | 8331.33 | 48.78% | 18.08% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/stereo` | 7 | 8258.3 | 24.69% | 0.0% |
| `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core` | 67 | 7815.98 | 13.33% | 59.3% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/_initialize.pyi` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/ArrayWrapper.h` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/DenseStorage.h` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/GenericPacketMath.h` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Householder/BlockHouseholder.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rapidfuzz-3.14.3/bench/benchmark.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_cdist.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_cpdist.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_fuzz.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_partial_ratio_long_needle.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` -> **18** Orphaned Functions | **138** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbbmalloc/frontend.cpp` -> **94** Orphaned Functions | **0** Duplicates
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/metrics.hpp` -> **90** Orphaned Functions | **0** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/unsupported/Eigen/CXX11/src/Tensor/TensorBase.h` -> **49** Orphaned Functions | **18** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/rml/server/rml_server.cpp` -> **55** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `21` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6181` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/stereo/lodepng.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7863.56 | **LOC:** 6224 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (93.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (2.4%)
- **Documentation Coverage:** 92.5439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lodepng_get_color_profile` **(Many-Argument Workhorses)** (Impact: 227.2)
    * *Intent:* /*profile must already have been inited with mode. It's ok to set some parameters of profile to done...
  * `encodeLZ77` **(Many-Argument Workhorses)** (Impact: 223.8)
    * *Intent:* */
  * `decodeGeneric` **(Many-Argument Workhorses)** (Impact: 208.4)
    * *Intent:* #endif /*LODEPNG_COMPILE_ANCILLARY_CHUNKS*/ /*read a PNG, the result will be in the same color type ...
  * `deflateDynamic` **(Many-Argument Workhorses)** (Impact: 183.2)
    * *Intent:* /*Deflate for a block of type "dynamic", that is, with freely, optimally, created huffman trees*/
  * `lodepng_error_text` **(Compute Cores)** (Impact: 173.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1198 instances
* *State Mutation (weighted view):* 3752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1420`, `structural_boundaries: 479`, `args: 244`, `func_start: 228`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1356`, `dead_code: 20`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 5`, `import: 4`
* *Defense:* `safety: 7`, `doc: 50`, `immutability_locks: 240`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` limits.h, lodepng.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/nlohmann/json.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7691.8 | **LOC:** 25534 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **33**; blast radius 0.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.7%), Guard Balance (formerly Safety Score) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 65.0815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_cbor_internal` **(Many-Argument Workhorses)** (Impact: 447.8)
    * *Intent:* */
  * `parse_msgpack_internal` **(Compute Cores)** (Impact: 293.4)
    * *Intent:* ///////////// // MsgPack // ///////////// /*! */
  * `scan_string` **(I/O & Config Routines)** (Impact: 269.2)
    * *Intent:* */
  * `write_msgpack` **(Compute Cores)** (Impact: 155.9)
    * *Intent:* /*! */
  * `write_cbor` **(Compute Cores)** (Impact: 146.6)
    * *Intent:* /*! */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 524 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1767
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3836`, `structural_boundaries: 3261`, `args: 1126`, `func_start: 648`, `class_start: 149`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 719`, `dead_code: 43`, `planned_debt: 7`, `fragile_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `api: 65`, `import: 161`
* *Defense:* `safety: 241`, `doc: 1284`, `immutability_locks: 975`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.002706
  * `Imports (Out-Degree: 8):` algorithm, array, cassert, cctype, clocale, cmath, cstddef, cstdint...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5653.9 | **LOC:** 11339 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Debt Markers (formerly Tech Debt) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 93.2182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `partial_ratio_impl` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `is_space_impl` **(Compute Cores)** (Impact: 55.5)
    * *Intent:* /* * Implementation of is_space for char types that are at least 2 Byte in size */
  * `levenshtein_mbleven2018` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `lcs_seq_mbleven2018` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `uniform_levenshtein_distance` **(Many-Argument Workhorses)** (Impact: 46.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 569 instances
* *State Mutation (weighted view):* 1989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 954`, `structural_boundaries: 3285`, `args: 1010`, `func_start: 795`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 851`, `dead_code: 3`, `planned_debt: 34`, `fragile_debt: 3`, `duplicate_logic: 138`, `unreferenced_by_name: 18`
* *Architecture:* `api: 22`, `import: 77`
* *Defense:* `safety: 322`, `doc: 88`, `immutability_locks: 1026`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` algorithm, array, bitset, cassert, cmath, cstddef, cstdint, cstring...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/httplib/httplib.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5051.16 | **LOC:** 7003 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **49**; blast radius 0.257; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (69.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 98.3)
  * `status_message` **(Compute Cores)** (Impact: 96.8)
  * `Server::apply_ranges` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `ClientImpl::send_with_content_provider` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `ClientImpl::write_request` **(Many-Argument Workhorses)** (Impact: 69.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 431 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 1477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1096`, `structural_boundaries: 1781`, `args: 820`, `func_start: 466`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 615`, `dead_code: 7`, `planned_debt: 9`, `fragile_debt: 5`
* *Architecture:* `io: 84`, `api: 211`, `concurrency: 27`, `import: 51`
* *Defense:* `safety: 98`, `doc: 1`, `sync_locks: 39`, `immutability_locks: 1077`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000406
  * `Imports (Out-Degree: 3):` algorithm, inet.h, array, atomic, decode.h, encode.h, cassert, cctype...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/fft/fft.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4104.46 | **LOC:** 5087 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fft_aux` **(Many-Argument Workhorses)** (Impact: 78.7)
    * *Intent:* * Recursive complex FFT on the n complex components of the array in: * basic Cooley-Tukey algorithm,...
  * `fft_aux_seq` **(Many-Argument Workhorses)** (Impact: 77.2)
  * `factor` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* /* * Determine (in a stupid way) if n is divisible by eight, then by four, else * find the smallest ...
  * `fft_twiddle_8` **(Many-Argument Workhorses)** (Impact: 18.5)
  * `fft_twiddle_8_seq` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 304 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3346
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 78`, `args: 292`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2738`, `unreferenced_by_name: 3`
* *Architecture:* `api: 40`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fft.h, math.h, stdio.h, stdlib.h, string.h, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/zblat2.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3446.26 | **LOC:** 3288 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.1%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZMAKE` **(Many-Argument Workhorses)** (Impact: 251.6)
  * `ZCHK3` **(Many-Argument Workhorses)** (Impact: 246.2)
  * `ZCHK2` **(Many-Argument Workhorses)** (Impact: 197.3)
  * `ZCHK6` **(Many-Argument Workhorses)** (Impact: 179.1)
  * `ZCHK1` **(Many-Argument Workhorses)** (Impact: 177.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 563 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 1824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 225`, `args: 19`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 14`, `state_mutation: 698`, `unreferenced_by_name: 1`
* *Architecture:* `io: 212`, `api: 11`
* *Defense:* `safety: 37`, `doc: 82`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/cblat2.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3445.5 | **LOC:** 3280 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (50.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.1%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CMAKE` **(Many-Argument Workhorses)** (Impact: 251.5)
  * `CCHK3` **(Many-Argument Workhorses)** (Impact: 246.1)
  * `CCHK2` **(Many-Argument Workhorses)** (Impact: 197.2)
  * `CCHK6` **(Many-Argument Workhorses)** (Impact: 179.0)
  * `CCHK1` **(Many-Argument Workhorses)** (Impact: 177.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 563 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 1824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 234`, `args: 19`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 14`, `state_mutation: 698`, `unreferenced_by_name: 1`
* *Architecture:* `io: 212`, `api: 11`
* *Defense:* `safety: 37`, `doc: 82`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/dblat2.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3351.64 | **LOC:** 3177 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DCHK3` **(Many-Argument Workhorses)** (Impact: 245.9)
  * `DMAKE` **(Many-Argument Workhorses)** (Impact: 237.4)
  * `DCHK2` **(Many-Argument Workhorses)** (Impact: 197.1)
  * `DCHK6` **(Many-Argument Workhorses)** (Impact: 178.8)
  * `DCHK1` **(Many-Argument Workhorses)** (Impact: 177.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 547 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 1771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 197`, `args: 19`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 14`, `state_mutation: 677`, `unreferenced_by_name: 1`
* *Architecture:* `io: 211`, `api: 11`
* *Defense:* `safety: 27`, `doc: 81`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/sblat2.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3351.64 | **LOC:** 3177 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SCHK3` **(Many-Argument Workhorses)** (Impact: 245.9)
  * `SMAKE` **(Many-Argument Workhorses)** (Impact: 237.4)
  * `SCHK2` **(Many-Argument Workhorses)** (Impact: 197.1)
  * `SCHK6` **(Many-Argument Workhorses)** (Impact: 178.8)
  * `SCHK1` **(Many-Argument Workhorses)** (Impact: 177.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 547 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 1771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 199`, `args: 19`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 14`, `state_mutation: 677`, `unreferenced_by_name: 1`
* *Architecture:* `io: 211`, `api: 11`
* *Defense:* `safety: 27`, `doc: 81`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/zblat3.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3042.48 | **LOC:** 3503 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.9%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZCHK5` **(Many-Argument Workhorses)** (Impact: 207.1)
  * `ZCHK4` **(Many-Argument Workhorses)** (Impact: 185.2)
  * `ZMMCH` **(Many-Argument Workhorses)** (Impact: 181.5)
  * `ZMAKE` **(Many-Argument Workhorses)** (Impact: 155.5)
  * `ZCHK3` **(Many-Argument Workhorses)** (Impact: 144.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 459 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 1726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 204`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 15`, `state_mutation: 808`, `unreferenced_by_name: 1`
* *Architecture:* `io: 161`, `api: 10`
* *Defense:* `safety: 33`, `doc: 65`, `immutability_locks: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/cblat3.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3042.04 | **LOC:** 3493 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.9%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CCHK5` **(Many-Argument Workhorses)** (Impact: 207.1)
  * `CCHK4` **(Many-Argument Workhorses)** (Impact: 185.2)
  * `CMMCH` **(Many-Argument Workhorses)** (Impact: 181.4)
  * `CMAKE` **(Many-Argument Workhorses)** (Impact: 155.4)
  * `CCHK3` **(Many-Argument Workhorses)** (Impact: 144.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 459 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 1726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 214`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 15`, `state_mutation: 808`, `unreferenced_by_name: 1`
* *Architecture:* `io: 161`, `api: 10`
* *Defense:* `safety: 33`, `doc: 64`, `immutability_locks: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/products/TriangularMatrixMatrix_BLAS.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 2607.01 | **LOC:** 316 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Complexity Load (formerly Cognitive Load) (64.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 29`, `args: 16`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `state_mutation: 42`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/dblat3.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2495.74 | **LOC:** 2874 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DCHK3` **(Many-Argument Workhorses)** (Impact: 144.5)
  * `DCHK5` **(Many-Argument Workhorses)** (Impact: 142.0)
  * `DMAKE` **(Many-Argument Workhorses)** (Impact: 131.5)
  * `DCHK1` **(Many-Argument Workhorses)** (Impact: 117.8)
  * `DCHK4` **(Many-Argument Workhorses)** (Impact: 117.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 401 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 1429
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 181`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 15`, `state_mutation: 627`, `unreferenced_by_name: 1`
* *Architecture:* `io: 153`, `api: 10`
* *Defense:* `safety: 24`, `doc: 61`, `immutability_locks: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/blas/testing/sblat3.f` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2495.74 | **LOC:** 2874 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SCHK3` **(Many-Argument Workhorses)** (Impact: 144.5)
  * `SCHK5` **(Many-Argument Workhorses)** (Impact: 142.0)
  * `SMAKE` **(Many-Argument Workhorses)** (Impact: 131.5)
  * `SCHK1` **(Many-Argument Workhorses)** (Impact: 117.8)
  * `SCHK4` **(Many-Argument Workhorses)** (Impact: 117.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 401 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 1429
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 181`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 15`, `state_mutation: 627`, `unreferenced_by_name: 1`
* *Architecture:* `io: 153`, `api: 10`
* *Defense:* `safety: 24`, `doc: 61`, `immutability_locks: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp_impl.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2346.04 | **LOC:** 2075 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.392; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 79.7468% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_iter` **(Many-Argument Workhorses)** (Impact: 307.1)
  * `extractOne_dict_i64` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `extractOne_dict_size_t` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `extractOne_list_f64` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `extractOne_list_i64` **(Many-Argument Workhorses)** (Impact: 66.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 870
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 169`, `args: 51`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 330`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 16`, `import: 6`
* *Defense:* `safety: 13`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.392
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000406
  * `Imports (Out-Degree: 0):` , array, heapq, numpy, rapidfuzz.fuzz, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/spdlog/fmt/bundled/format.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2046.48 | **LOC:** 3730 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **11**; blast radius 4.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 91.8256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_align` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* // Parses fill and alignment.
  * `prettify` **(Type Conversions)** (Impact: 45.9)
  * `parse_format_specs` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* // Parses standard format specifiers and sends notifications about parsed // components to handler.
  * `parse_arg_id` **(Compute Cores)** (Impact: 37.6)
  * `handle_int_type_spec` **(Compute Cores)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 1392`, `args: 266`, `func_start: 329`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 277`, `dead_code: 4`, `fragile_debt: 2`, `duplicate_logic: 11`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 8`, `doc: 28`, `immutability_locks: 224`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.111
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.019431
  * `Imports (Out-Degree: 3):` algorithm, cerrno, cmath, core.h, cstdint, format.h, format-inl.h, intrin.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/rml/server/rml_server.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2043.58 | **LOC:** 3306 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.9%), Complexity Load (formerly Cognitive Load) (91.2%), Guard Balance (formerly Safety Score) (88.9%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `thread_map::add_virtual_processors` **(Many-Argument Workhorses)** (Impact: 97.9)
  * `omp_connection_v2::get_threads` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `thread_map::wakeup_tbb_threads` **(Compute Cores)** (Impact: 34.1)
  * `connection_scavenger_thread::process_requests` **(Compute Cores)** (Impact: 33.1)
  * `thread_map::remove_virtual_processors` **(Many-Argument Workhorses)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 828
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 647`, `structural_boundaries: 557`, `args: 149`, `func_start: 172`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 294`, `dead_code: 10`, `fragile_debt: 7`, `duplicate_logic: 8`, `unreferenced_by_name: 55`
* *Architecture:* `api: 21`, `import: 17`
* *Defense:* `safety: 6`, `doc: 20`, `sync_locks: 1`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` concrt.h, concrtrm.h, job_automaton.h, rml_omp.h, rml_tbb.h, aligned_space.h, atomic.h, cache_aligned_allocator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbbmalloc/frontend.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1991.56 | **LOC:** 3292 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.1%), Guard Balance (formerly Safety Score) (92.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.4751% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reallocAligned` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `__TBB_malloc_safer_aligned_realloc` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `__TBB_malloc_safer_realloc` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* /* * A variant that provides additional memory safety, by checking whether the given address * was o...
  * `getIndexOrObjectSize` **(Compute Cores)** (Impact: 40.2)
    * *Intent:* /* * Depending on indexRequest, for a given size return either the index into the bin * for objects ...
  * `scalable_allocation_mode` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* /********* End code for scalable_msize ***********/
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 247 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 527`, `args: 227`, `func_start: 161`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 297`, `dead_code: 14`, `planned_debt: 20`, `unreferenced_by_name: 94`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `doc: 24`, `test: 92`, `sync_locks: 12`, `immutability_locks: 79`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` itt_notify.h, tbb_environment.h, tbb_version.h, errno.h, new, sched.h, string.h, tbbmalloc_internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/Assign_MKL.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 1829.48 | **LOC:** 179 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (70.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 23`, `args: 35`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/Eigen/src/Core/products/TriangularMatrixVector_BLAS.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 1819.34 | **LOC:** 256 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (60.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 29`, `args: 17`, `func_start: 2`, `class_start: 5`
* *Risk/State:* `state_mutation: 50`
* *Architecture:* None
* *Defense:* `doc: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/ff/platforms/getopt.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1765.42 | **LOC:** 978 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getopt_internal_r_a` **(Many-Argument Workhorses)** (Impact: 449.5)
  * `_getopt_internal_r_w` **(Many-Argument Workhorses)** (Impact: 449.5)
  * `_getopt_initialize_a` **(Compute Cores)** (Impact: 15.1)
  * `_getopt_initialize_w` **(Compute Cores)** (Impact: 15.1)
  * `exchange_a` **(Compute Cores)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 252 instances
* *State Mutation (weighted view):* 772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 312`, `structural_boundaries: 113`, `args: 20`, `func_start: 12`, `class_start: 8`
* *Risk/State:* `state_mutation: 268`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` getopt.h, malloc.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/graph/fgbzip2/blocksort.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1735.58 | **LOC:** 1143 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (95.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mainSort` **(Many-Argument Workhorses)** (Impact: 126.2)
    * *Intent:* */ #define BIGFREQ(b) (ftab[((b)+1) << 8] - ftab[(b) << 8]) #define SETMASK (1 << 21) #define CLEARM...
  * `fallbackSort` **(Many-Argument Workhorses)** (Impact: 103.9)
    * *Intent:* */ #define SET_BH(zz) bhtab[(zz) >> 5] |= (1 << ((zz) & 31)) #define CLEAR_BH(zz) bhtab[(zz) >> 5] &...
  * `mainGtU` **(Many-Argument Workhorses)** (Impact: 93.6)
    * *Intent:* #undef SET_BH #undef CLEAR_BH #undef ISSET_BH #undef WORD_BH #undef UNALIGNED_BH /*-----------------...
  * `mainQSort3` **(Many-Argument Workhorses)** (Impact: 88.9)
    * *Intent:* #define MAIN_QSORT_SMALL_THRESH 20 #define MAIN_QSORT_DEPTH_THRESH (BZ_N_RADIX + BZ_N_QSORT) #define...
  * `fallbackQSort3` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* #define FALLBACK_QSORT_SMALL_THRESH 10 #define FALLBACK_QSORT_STACK_SIZE 100
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 364 instances
* *State Mutation (weighted view):* 1121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 44`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 393`, `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bzlib_private.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_deferred_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1678.1 | **LOC:** 1871 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.212; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (76.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeline_3P_SPP_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 80.6)
    * *Intent:* // ---------------------------------------------------------------------------- // three pipes (SPP)...
  * `pipeline_2P_SS_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 64.9)
    * *Intent:* // ---------------------------------------------------------------------------- // two pipes (SS), L...
  * `pipeline_2P_SP_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 62.7)
    * *Intent:* // ---------------------------------------------------------------------------- // two pipes (SP), L...
  * `pipeline_1P_S_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* // ---------------------------------------------------------------------------- // one pipe (S), L l...
  * `pl` **(Many-Argument Workhorses)** (Impact: 56.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 165 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 54`, `args: 65`, `func_start: 182`, `class_start: 1`
* *Risk/State:* `state_mutation: 211`, `dead_code: 60`, `duplicate_logic: 4`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `test: 261`, `sync_locks: 43`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` algorithm, doctest.h, mutex, stdlib.h, pipeline.hpp, taskflow.hpp, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/eigen-3.3.7/unsupported/Eigen/CXX11/src/Tensor/TensorContractionCuda.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1619.66 | **LOC:** 1392 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EigenFloatContractionKernelInternal` **(Many-Argument Workhorses)** (Impact: 353.2)
  * `EigenFloatContractionKernelInternal16x16` **(Many-Argument Workhorses)** (Impact: 220.7)
  * `EigenContractionKernelInternal` **(Many-Argument Workhorses)** (Impact: 149.9)
  * `evalTo` **(Compute Cores)** (Impact: 23.1)
  * `EigenFloatContractionKernel` **(Many-Argument Workhorses)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 773
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 112`, `args: 21`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 349`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 131`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/flow_graph.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1552.66 | **LOC:** 4744 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **39**; blast radius 1.396; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.5%), Mutation Surface (formerly State Flux) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `internal_make_edge` **(Many-Argument Workhorses)** (Impact: 161.2)
    * *Intent:* #endif //variadic max 10 #if __TBB_PREVIEW_ASYNC_MSG
  * `handle_operations_impl` **(Compute Cores)** (Impact: 71.7)
  * `internal_remove_edge` **(Stateful Encapsulated Methods)** (Impact: 61.0)
    * *Intent:* #endif #if __TBB_PREVIEW_ASYNC_MSG
  * `internal_forward_task_impl` **(Compute Cores)** (Impact: 16.8)
  * `try_reserve_apply_body` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* // used by apply_body_bypass, can invoke body of node.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 139 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 1763`, `args: 215`, `func_start: 276`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 204`, `dead_code: 20`, `planned_debt: 10`, `fragile_debt: 5`, `duplicate_logic: 52`
* *Architecture:* `api: 78`, `import: 39`
* *Defense:* `safety: 4`, `doc: 14`, `sync_locks: 33`, `immutability_locks: 194`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.396
  * `Choke Point (Betweenness):` 0.000328 | `Ripple Effect (Closeness):` 0.008373
  * `Imports (Out-Degree: 28):` array, atomic.h, cache_aligned_allocator.h, tuple, _aggregator_impl.h, _flow_graph_async_msg_impl.h, _flow_graph_body_impl.h, _flow_graph_cache_impl.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/common/utility/utility.h` -> **Severity: 0.558** (Bridge: 0.0056 * Flux: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 0.45** (Bridge: 0.0046 * Flux: 98.5335%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/observer.hpp` -> **Severity: 0.418** (Bridge: 0.0042 * Flux: 99.9951%)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/src/tbb/condition_variable.cpp` -> **Severity: 0.382** (Bridge: 0.0038 * Flux: 99.9812%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/nonblocking_notifier.hpp` -> **Severity: 0.363** (Bridge: 0.0036 * Flux: 99.5057%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/common/utility/utility.h` -> **Severity: 4.497** (Embedded: 0.0633 * Error Risk: 71.0817%)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/parallel_for/tachyon/src/types.h` -> **Severity: 4.231** (Embedded: 0.0494 * Error Risk: 85.5921%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/observer.hpp` -> **Severity: 3.835** (Embedded: 0.0453 * Error Risk: 84.5777%)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/ff/parallel_for_internals.hpp` -> **Severity: 3.6** (Embedded: 0.0389 * Error Risk: 92.4293%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 3.575** (Embedded: 0.0536 * Error Risk: 66.6502%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/examples/common/utility/utility.h` -> **Severity: 1230.4** (Blast Radius: 12.304 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/details/type_traits.hpp` -> **Severity: 1218.7** (Blast Radius: 12.187 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 1155.6** (Blast Radius: 11.556 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/3rd-party/tbb/include/tbb/tbb_stddef.h` -> **Severity: 1001.625** (Blast Radius: 13.355 * Doc Risk: 75.0%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/iterator.hpp` -> **Severity: 707.2** (Blast Radius: 7.072 * Doc Risk: 100.0%)

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
