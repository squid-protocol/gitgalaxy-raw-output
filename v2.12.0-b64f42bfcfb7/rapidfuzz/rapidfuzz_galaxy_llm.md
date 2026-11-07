# ARCHITECTURAL_BRIEF: rapidfuzz
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
- **Scope:** 620 analyzed artifact(s), 113400 LOC.
- **Load-bearing artifact:** `rapidfuzz-3.14.3/extern/taskflow/taskflow/taskflow.hpp` -- 111 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rapidfuzz-3.14.3/extern/taskflow/sandbox/utility/traits.hpp` -- pulls in 31 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` at magnitude 5792.9 (structural weight, not risk).
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
| Total Artifacts | 997 |
| Analyzed Artifacts (Scanned) | 620 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 377 |
| Total LOC | 113400 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.2% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7669 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2254 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.6926 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 72 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 400 | 81170 | 64.5% |
| PYTHON | 108 | 13121 | 17.4% |
| XML | 47 | 13 | 7.6% |
| PLAINTEXT | 35 | 0 | 5.6% |
| MARKDOWN | 10 | 0 | 1.6% |
| SHELL | 5 | 103 | 0.8% |
| CSS | 5 | 13128 | 0.8% |
| C | 3 | 4963 | 0.5% |
| YAML | 2 | 57 | 0.3% |
| JAVASCRIPT | 2 | 719 | 0.3% |
| MAKEFILE | 1 | 60 | 0.2% |
| HTML | 1 | 57 | 0.2% |
| JSON | 1 | 9 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 620 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, Large Core Modules (3) 14%, Many-Argument Workhorses Files 13%, Generic / Templated Code Files 9%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 564 | 91.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 45 | 7.3% |
| Static: Minified & Vendor Opaque Mass | 11 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 377*

**Composition by Extension & Reason:**
- `.dox`: 107x Excluded (Unsupported Extension: '.dox')
- `.dot`: 81x Excluded (Unsupported Extension: '.dot')
- `.png`: 50x Excluded (Explicitly Denied Extension: '.png')
- `.cu`: 41x Excluded (Unsupported Extension: '.cu')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 2x Excluded (Binary Format Detected)
- `.svg`: 2x Excluded (Machine-Generated Source Code Signature: 220 LOC), 2x Excluded (Machine-Generated Source Code Signature: 142 LOC), 1x Excluded (Machine-Generated Source Code Signature: 111 LOC)
- `.pdf`: 10x Excluded (Explicitly Denied Extension: '.pdf')
- `.map`: 10x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.cxx`: 2x Excluded (Machine-Generated Source Code Signature: 30465 LOC), 2x Excluded (Machine-Generated Source Code Signature: 16265 LOC), 1x Excluded (Machine-Generated Source Code Signature: 7891 LOC)
- `.js`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.css`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pptx`: 4x Excluded (Explicitly Denied Extension: '.pptx')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.8 | 17.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.3 | 44.3 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.6 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.6 | 48.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2171 | 223 | 8 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` |
| cleanup | 159 | 49 | 0 | `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_pipeline/gold.cpp` |
| guards | 9251 | 373 | 27 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` |
| danger | 676 | 138 | 2 | `rapidfuzz-3.14.3/src/rapidfuzz/process.pyi` |
| concurrency | 1264 | 61 | 0 | `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-module-opt.hpp` |
| connectivity | 2003 | 265 | 11 | `rapidfuzz-3.14.3/src/rapidfuzz/distance/metrics_cpp.pyx` |
| io | 193 | 34 | 0 | `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_pipeline/gold.cpp` |
| crypto | 0 | 0 | 0 | - |
| ipc | 384 | 22 | 0 | `rapidfuzz-3.14.3/extern/taskflow/unittests/test_pipelines.cpp` |
| time | 40 | 15 | 0 | `rapidfuzz-3.14.3/extern/taskflow/examples/reduce.cpp` |
| serialization | 2 | 2 | 0 | `rapidfuzz-3.14.3/extern/taskflow/tfprof/server/tfprof.cpp` |
| regex | 17 | 6 | 0 | `rapidfuzz-3.14.3/extern/taskflow/tfprof/js/index.js` |
| events | 195 | 24 | 0 | `rapidfuzz-3.14.3/extern/taskflow/tfprof/js/index.js` |
| tests | 4662 | 63 | 1 | `rapidfuzz-3.14.3/extern/taskflow/unittests/test_data_pipelines.cpp` |
| docs | 1739 | 148 | 7 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` |
| debt | 1007 | 182 | 5 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` |
| mutation | 31084 | 470 | 117 | `rapidfuzz-3.14.3/extern/taskflow/sandbox/fft/fft.c` |
| dead_code | 2036 | 272 | 8 | `rapidfuzz-3.14.3/src/rapidfuzz/distance/metrics.hpp` |
| credential | 0 | 0 | 0 | - |
| threat | 3 | 3 | 0 | `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/bench/bench-jarowinkler.cpp` |
| ml_ai | 99 | 25 | 0 | `rapidfuzz-3.14.3/extern/taskflow/benchmarks/mnist/dnn.hpp` |
| ui | 360 | 6 | 0 | `rapidfuzz-3.14.3/extern/taskflow/tfprof/css/bootstrap/4.4.1/bootstrap.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_pipeline/gold.cpp` (Hits: 32)
- `rapidfuzz-3.14.3/extern/taskflow/benchmarks/hetero_traversal/run.sh` (Hits: 32)
- `rapidfuzz-3.14.3/extern/taskflow/unittests/test_scan.cpp` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **taskflow.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/taskflow.hpp`) — 111 inbound connections
2. **Range.hpp** (`rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/details/Range.hpp`) — 22 inbound connections
3. **__init__.py** (`rapidfuzz-3.14.3/src/rapidfuzz/__init__.py`) — 21 inbound connections
4. **__init__.py** (`rapidfuzz-3.14.3/src/rapidfuzz/distance/__init__.py`) — 19 inbound connections
5. **pipeline.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/algorithm/pipeline.hpp`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **traits.hpp** (`rapidfuzz-3.14.3/extern/taskflow/sandbox/utility/traits.hpp`) — 31 outbound dependencies
2. **traits.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/traits.hpp`) — 30 outbound dependencies
3. **rapidfuzz_amalgamated.hpp** (`rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp`) — 26 outbound dependencies
4. **serializer.hpp** (`rapidfuzz-3.14.3/extern/taskflow/sandbox/utility/serializer.hpp`) — 25 outbound dependencies
5. **serializer.hpp** (`rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/serializer.hpp`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `extract_iter` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp_impl.pyx`) -> Impact: **307.1** | LOC: 372
- `Executor::_wait_for_task` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp`) -> Impact: **297.6** | LOC: 930
  * *Intent:* // Function: _wait_for_task
- `cdist_two_lists_impl` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp.hpp`) -> Impact: **138.4** | LOC: 136
- `traverse_regular_graph_omp` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_traversal/omp.cpp`) -> Impact: **115.0** | LOC: 257
  * *Intent:* #include <iostream> #include <chrono> #include <omp.h> #include "levelgraph.hpp"
- `Executor::_invoke` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-module-opt.hpp`) -> Impact: **97.6** | LOC: 186
  * *Intent:* // Procedure: _invoke
- `run_omp` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/benchmarks/mnist/omp.cpp`) -> Impact: **94.3** | LOC: 188
  * *Intent:* #include "dnn.hpp" #include <omp.h>
- `Executor::_invoke` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-dl.hpp`) -> Impact: **90.1** | LOC: 174
  * *Intent:* // Procedure: _invoke
- `Executor::_invoke` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-no-waiter.hpp`) -> Impact: **90.1** | LOC: 174
  * *Intent:* // Procedure: _invoke
- `Executor::_invoke` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-tw.hpp`) -> Impact: **90.1** | LOC: 174
  * *Intent:* // Procedure: _invoke
- `measure_time_tbb` **(Many-Argument Workhorses)** (@ `rapidfuzz-3.14.3/extern/taskflow/benchmarks/data_pipeline/tbb.cpp`) -> Impact: **86.9** | LOC: 128

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rapidfuzz-3.14.3/extern/taskflow/unittests` | 30 | 14646.18 | 70.97% | 7.92% |
| `rapidfuzz-3.14.3/src/rapidfuzz/distance` | 43 | 5799.74 | 27.45% | 11.67% |
| `rapidfuzz-3.14.3/src/rapidfuzz` | 31 | 5796.68 | 28.98% | 18.85% |
| `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras` | 1 | 5792.9 | 46.6% | 99.29% |
| `rapidfuzz-3.14.3/extern/taskflow/sandbox/fft` | 3 | 4224.32 | 53.19% | 11.65% |
| `rapidfuzz-3.14.3/extern/taskflow/taskflow/algorithm` | 11 | 3490.84 | 47.89% | 5.06% |
| `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/distance` | 20 | 3292.18 | 26.14% | 6.41% |
| `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor` | 4 | 3246.32 | 34.23% | 100.0% |
| `rapidfuzz-3.14.3/extern/taskflow/taskflow/core` | 19 | 3108.9 | 18.06% | 7.23% |
| `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_pipeline` | 7 | 2520.9 | 64.33% | 10.73% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/_initialize.pyi` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/cublas_core/cublas_helper.hpp` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/cublas_core/cublas_level1.hpp` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/cublas_core/cublas_level2.hpp` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-dl.hpp` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rapidfuzz-3.14.3/bench/benchmark.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_cdist.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_cpdist.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_fuzz.py` -> **100.0%** Exposure
- `rapidfuzz-3.14.3/bench/benchmark_partial_ratio_long_needle.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` -> **43** Orphaned Functions | **138** Duplicates
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/metrics.hpp` -> **90** Orphaned Functions | **0** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-module-opt.hpp` -> **54** Orphaned Functions | **0** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-dl.hpp` -> **46** Orphaned Functions | **0** Duplicates
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-no-waiter.hpp` -> **46** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1869` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/extras/rapidfuzz_amalgamated.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.05)
- **Top Global Matches:** file_cluster_0: 9.05, file_cluster_15: 9.956, file_cluster_16: 10.911
- **Magnitude:** 5792.9 | **LOC:** 11339 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.656; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 93.2544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `levenshtein_hyrroe2003_block` **(Many-Argument Workhorses)** (Impact: 66.4)
    * *Intent:* /** * @param stop_row specifies the row to record when using RecordBitRow */
  * `partial_ratio_impl` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `is_space_impl` **(Compute Cores)** (Impact: 55.5)
    * *Intent:* /* * Implementation of is_space for char types that are at least 2 Byte in size */
  * `uniform_levenshtein_distance` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `flag_similar_characters_step` **(Many-Argument Workhorses)** (Impact: 38.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 567 instances
* *State Mutation (weighted view):* 1985
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 869`, `structural_boundaries: 3283`, `args: 1009`, `func_start: 826`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 851`, `dead_code: 2`, `planned_debt: 34`, `fragile_debt: 3`, `duplicate_logic: 138`, `unreferenced_by_name: 43`
* *Architecture:* `api: 22`, `import: 77`
* *Defense:* `safety: 322`, `doc: 88`, `immutability_locks: 1026`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` algorithm, array, bitset, cassert, cmath, cstddef, cstdint, cstring...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/fft/fft.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.677)
- **Top Global Matches:** file_cluster_4: 6.677, file_cluster_15: 8.01, file_cluster_16: 8.74
- **Magnitude:** 4104.46 | **LOC:** 5087 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (59.6%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2738`, `dead_code: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 40`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.936
  * `Choke Point (Betweenness):` 0.000209 | `Ripple Effect (Closeness):` 0.001616
  * `Imports (Out-Degree: 2):` fft.h, math.h, stdio.h, stdlib.h, string.h, taskflow.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp_impl.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.584)
- **Top Global Matches:** file_cluster_6: 6.584, file_cluster_8: 10.5, file_cluster_4: 14.265
- **Magnitude:** 2346.04 | **LOC:** 2075 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%), Guard Balance (formerly Safety Score) (73.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .process_py, array, heapq, numpy, rapidfuzz.fuzz, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.109)
- **Top Global Matches:** file_cluster_10: 8.109, file_cluster_15: 8.59, file_cluster_2: 8.993
- **Magnitude:** 1493.8 | **LOC:** 2929 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeline_in_pipeline` **(Many-Argument Workhorses)** (Impact: 41.2)
    * *Intent:* // ---------------------------------------------------------------------------- // pipeline in pipel...
  * `three_parallel_pipelines` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* // ---------------------------------------------------------------------------- // three parallel pi...
  * `three_concatenated_pipelines` **(Many-Argument Workhorses)** (Impact: 33.1)
    * *Intent:* // ---------------------------------------------------------------------------- // three concatenate...
  * `ifelse_pipeline` **(Compute Cores)** (Impact: 24.5)
  * `looping_pipelines` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* // ---------------------------------------------------------------------------- // pipeline (SPSP) a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 142 instances
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 135`, `args: 122`, `func_start: 351`
* *Risk/State:* `state_mutation: 254`, `dead_code: 26`
* *Architecture:* `concurrency: 22`, `import: 5`
* *Defense:* `safety: 16`, `test: 541`, `sync_locks: 53`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest.h, stdlib.h, pipeline.hpp, taskflow.hpp, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_deferred_scalable_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.816)
- **Top Global Matches:** file_cluster_15: 8.816, file_cluster_4: 8.864, file_cluster_10: 9.054
- **Magnitude:** 1469.44 | **LOC:** 1964 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Guard Balance (formerly Safety Score) (60.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scalable_pipeline_3P_SPP_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 81.0)
    * *Intent:* // ---------------------------------------------------------------------------- // three pipes (SPP)...
  * `scalable_pipeline_2P_SS_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 65.3)
    * *Intent:* // ---------------------------------------------------------------------------- // two pipes (SS), L...
  * `scalable_pipeline_2P_SP_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* // ---------------------------------------------------------------------------- // two pipes (SP), L...
  * `scalable_pipeline_1P_S_264VideoFormat` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* // ---------------------------------------------------------------------------- // one pipe (S), L l...
  * `construct_video` **(Compute Cores)** (Impact: 36.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 183 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 608
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 65`, `args: 80`, `func_start: 173`, `class_start: 1`
* *Risk/State:* `state_mutation: 242`, `dead_code: 50`, `planned_debt: 1`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `test: 280`, `sync_locks: 43`, `immutability_locks: 11`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, doctest.h, mutex, stdlib.h, pipeline.hpp, taskflow.hpp, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_deferred_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.874)
- **Top Global Matches:** file_cluster_15: 8.874, file_cluster_4: 8.919, file_cluster_10: 9.108
- **Magnitude:** 1369.5 | **LOC:** 1871 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Guard Balance (formerly Safety Score) (59.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
  * `construct_video` **(Many-Argument Workhorses)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 165 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 54`, `args: 65`, `func_start: 172`, `class_start: 1`
* *Risk/State:* `state_mutation: 211`, `dead_code: 60`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `test: 261`, `sync_locks: 43`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, doctest.h, mutex, stdlib.h, pipeline.hpp, taskflow.hpp, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_data_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.98)
- **Top Global Matches:** file_cluster_10: 8.98, file_cluster_15: 9.405, file_cluster_2: 9.89
- **Magnitude:** 1190.7 | **LOC:** 2872 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.6%), Complexity Load (formerly Cognitive Load) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeline_in_pipeline` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* // ---------------------------------------------------------------------------- // pipeline in pipel...
  * `ifelse_data_pipeline` **(Compute Cores)** (Impact: 24.8)
  * `three_parallel_data_pipelines` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* // ---------------------------------------------------------------------------- // three parallel pi...
  * `three_concatenated_data_pipelines` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* // ---------------------------------------------------------------------------- // three concatenate...
  * `looping_data_pipelines` **(Many-Argument Workhorses)** (Impact: 12.3)
    * *Intent:* // ---------------------------------------------------------------------------- // pipeline (SPSP) a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 170`, `args: 106`, `func_start: 351`
* *Risk/State:* `state_mutation: 181`, `dead_code: 78`
* *Architecture:* `concurrency: 22`, `import: 5`
* *Defense:* `safety: 16`, `test: 541`, `sync_locks: 53`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest.h, stdlib.h, data_pipeline.hpp, taskflow.hpp, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein_impl.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.901)
- **Top Global Matches:** file_cluster_4: 6.901, file_cluster_6: 9.194, file_cluster_15: 13.142
- **Magnitude:** 1036.08 | **LOC:** 1261 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 2.921; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Complexity Load (formerly Cognitive Load) (54.1%)
- **Documentation Coverage:** 87.8049% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `levenshtein_hyrroe2003_block` **(Many-Argument Workhorses)** (Impact: 66.4)
    * *Intent:* /** * @param stop_row specifies the row to record when using RecordBitRow */
  * `uniform_levenshtein_distance` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `uniform_levenshtein_distance` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `levenshtein_hyrroe2003_small_band` **(Many-Argument Workhorses)** (Impact: 37.9)
    * *Intent:* #endif
  * `levenshtein_mbleven2018` **(Many-Argument Workhorses)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 186`, `args: 75`, `func_start: 37`, `class_start: 7`
* *Risk/State:* `state_mutation: 214`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 19`, `doc: 5`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.921
  * `Choke Point (Betweenness):` 0.000532 | `Ripple Effect (Closeness):` 0.050374
  * `Imports (Out-Degree: 8):` cstddef, cstdint, limits, GrowingHashmap.hpp, Matrix.hpp, PatternMatchVector.hpp, common.hpp, distance.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.655)
- **Top Global Matches:** file_cluster_4: 8.655, file_cluster_15: 9.315, file_cluster_0: 9.854
- **Magnitude:** 1010.64 | **LOC:** 2296 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 20.41; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.0%), Guard Balance (formerly Safety Score) (55.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Executor::_wait_for_task` **(Many-Argument Workhorses)** (Impact: 297.6)
    * *Intent:* // Function: _wait_for_task
  * `Executor::_invoke` **(Many-Argument Workhorses)** (Impact: 84.5)
    * *Intent:* // Procedure: _invoke
  * `Executor::_corun_until` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* // Function: _corun_until
  * `Executor::_set_up_graph` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* // Function: _set_up_graph
  * `Executor::_explore_task` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* // Function: _explore_task
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 376`, `args: 151`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`, `dead_code: 26`, `planned_debt: 1`
* *Architecture:* `io: 13`, `api: 41`, `concurrency: 17`, `import: 4`
* *Defense:* `safety: 24`, `doc: 38`, `sync_locks: 30`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.41
  * `Choke Point (Betweenness):` 0.019445 | `Ripple Effect (Closeness):` 0.099507
  * `Imports (Out-Degree: 12):` async_task.hpp, freelist.hpp, observer.hpp, taskflow.hpp
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-module-opt.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.262)
- **Top Global Matches:** file_cluster_15: 8.262, file_cluster_0: 9.845, file_cluster_16: 9.896
- **Magnitude:** 873.78 | **LOC:** 2026 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 0.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Executor::_invoke` **(Many-Argument Workhorses)** (Impact: 97.6)
    * *Intent:* // Procedure: _invoke
  * `Executor::_wait_for_task` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* // Function: _wait_for_task
  * `Executor::_invoke_dynamic_task_external` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* // Procedure: _invoke_dynamic_task_external
  * `Executor::_consume_task` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* // Function: _consume_task
  * `Executor::named_async` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* // Function: named_async
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 66 instances
* *Concurrency (weighted view):* 110
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 368`, `args: 153`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`, `dead_code: 17`, `planned_debt: 2`, `unreferenced_by_name: 54`
* *Architecture:* `api: 1`, `concurrency: 30`, `import: 2`
* *Defense:* `safety: 28`, `doc: 28`, `sync_locks: 63`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.936
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.004847
  * `Imports (Out-Degree: 5):` observer.hpp, taskflow.hpp
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-dl.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_15: 8.644, file_cluster_0: 9.514, file_cluster_4: 10.012
- **Magnitude:** 797.5 | **LOC:** 2519 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Executor::_invoke` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* // Procedure: _invoke
  * `Executor::_wait_for_task` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* // Function: _wait_for_task
  * `Executor::_corun_until` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* // Function: _corun_until
  * `Executor::_explore_task` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* // Function: _explore_task
  * `Executor::_tear_down_topology` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* // Function: _tear_down_topology
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 394`, `args: 176`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `dead_code: 35`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 24`, `doc: 40`, `sync_locks: 56`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` async_task.hpp, observer.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_basics.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.689)
- **Top Global Matches:** file_cluster_10: 7.689, file_cluster_15: 9.191, file_cluster_4: 9.431
- **Magnitude:** 796.9 | **LOC:** 1022 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.843; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (63.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Callbacks & Closures)** (Impact: 50.6)
    * *Intent:* // -------------------------------------------------------- // Testcase: Iterators // --------------...
  * `TEST_CASE` **(Callbacks & Closures)** (Impact: 39.1)
    * *Intent:* // -------------------------------------------------------- // Testcase: Builder // ----------------...
  * `SUBCASE` **(Callbacks & Closures)** (Impact: 32.1)
  * `SUBCASE` **(Callbacks & Closures)** (Impact: 19.7)
  * `sequential_runs` **(Callbacks & Closures)** (Impact: 13.0)
    * *Intent:* // -------------------------------------------------------- // Testcase: SequentialRuns // ---------...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 77`, `args: 119`, `func_start: 74`, `class_start: 3`
* *Risk/State:* `state_mutation: 167`, `dead_code: 3`
* *Architecture:* `concurrency: 7`, `import: 4`
* *Defense:* `safety: 7`, `test: 171`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001616
  * `Imports (Out-Degree: 3):` doctest.h, for_each.hpp, reduce.hpp, taskflow.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-tw.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.642)
- **Top Global Matches:** file_cluster_15: 8.642, file_cluster_0: 9.487, file_cluster_4: 10.029
- **Magnitude:** 791.62 | **LOC:** 2500 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Executor::_invoke` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* // Procedure: _invoke
  * `Executor::_wait_for_task` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* // Function: _wait_for_task
  * `Executor::_corun_until` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* // Function: _corun_until
  * `Executor::_explore_task` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* // Function: _explore_task
  * `Executor::_tear_down_topology` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* // Function: _tear_down_topology
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 394`, `args: 172`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `dead_code: 33`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 24`, `doc: 40`, `sync_locks: 56`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` async_task.hpp, observer.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/sandbox/executor/executor-no-waiter.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.661)
- **Top Global Matches:** file_cluster_15: 8.661, file_cluster_0: 9.485, file_cluster_16: 10.048
- **Magnitude:** 783.42 | **LOC:** 2493 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Executor::_invoke` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* // Procedure: _invoke
  * `Executor::_corun_until` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* // Function: _corun_until
  * `Executor::_wait_for_task` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* // Function: _wait_for_task
  * `Executor::_explore_task` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* // Function: _explore_task
  * `Executor::_tear_down_topology` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* // Function: _tear_down_topology
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 394`, `args: 172`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `dead_code: 33`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 24`, `doc: 40`, `sync_locks: 56`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` async_task.hpp, observer.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/src/rapidfuzz/distance/metrics_cpp.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.279)
- **Top Global Matches:** file_cluster_15: 5.279, file_cluster_2: 7.487, file_cluster_11: 7.595
- **Magnitude:** 771.58 | **LOC:** 1192 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jaro_winkler_distance` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* ############################################### # JaroWinkler ######################################...
  * `jaro_winkler_similarity` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `jaro_winkler_normalized_distance` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `jaro_winkler_normalized_similarity` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `levenshtein_normalized_distance` **(Many-Argument Workhorses)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 177`, `args: 89`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 140`
* *Architecture:* `io: 1`, `api: 48`, `import: 4`
* *Defense:* `safety: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._initialize_cpp, .metrics_py, array, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_reduce.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.567)
- **Top Global Matches:** file_cluster_10: 6.567, file_cluster_15: 7.547, file_cluster_2: 7.933
- **Magnitude:** 757.82 | **LOC:** 1629 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `move_only_transform_reduce` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* // ---------------------------------------------------------------------------- // Transform & Reduc...
  * `binary_transform_reduce` **(Callbacks & Closures)** (Impact: 9.6)
    * *Intent:* // ---------------------------------------------------------------------------- // binary_transform_...
  * `binary_transform_reduce_sum` **(Callbacks & Closures)** (Impact: 9.5)
    * *Intent:* // ---------------------------------------------------------------------------- // binary_transform_...
  * `reduce` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* // -------------------------------------------------------- // Testcase: reduce // -----------------...
  * `reduce_sum` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* // -------------------------------------------------------- // Testcase: reduce_sum // -------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 108`, `args: 87`, `func_start: 241`, `class_start: 3`
* *Risk/State:* `state_mutation: 89`, `duplicate_logic: 8`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `test: 265`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest.h, reduce.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_scalable_pipelines.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_10: 7.336, file_cluster_15: 7.529, file_cluster_16: 8.389
- **Magnitude:** 754.02 | **LOC:** 1388 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.0%), Guard Balance (formerly Safety Score) (57.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spipeline_in_spipeline` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* // ---------------------------------------------------------------------------- // ScalablePipeline ...
  * `snig_spipeline` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* // -----> p p p p | // | | | | | | // ----- c c c c | // | | | | | // o o o o | // \ \ | / | // \||/...
  * `spawn` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* // ---------------------------------------------------------------------- // Subflow pipeline // ---...
  * `ifelse_spipeline` **(Compute Cores)** (Impact: 24.7)
  * `scalable_pipeline_iterative_reset` **(Compute Cores)** (Impact: 20.0)
    * *Intent:* // ---------------------------------------------------------------------------- // Scalable Pipeline...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 96`, `args: 101`, `func_start: 86`
* *Risk/State:* `state_mutation: 161`, `dead_code: 4`
* *Architecture:* `import: 3`
* *Defense:* `safety: 13`, `test: 181`, `immutability_locks: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest.h, pipeline.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/src/rapidfuzz/distance/_initialize_py.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.15)
- **Top Global Matches:** file_cluster_12: 7.15, file_cluster_4: 7.942, file_cluster_15: 8.46
- **Magnitude:** 753.54 | **LOC:** 885 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 2.417; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%)
- **Documentation Coverage:** 60.6383% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_list_to_opcodes` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `_list_to_editops` **(Stateful Encapsulated Methods)** (Impact: 34.1)
  * `as_opcodes` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* """ Convert to Opcodes Returns ------- opcodes : Opcodes Editops converted to Opcodes """
  * `remove_subsequence` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* """ remove a subsequence Parameters ---------- subsequence : Editops subsequence to remove (has to b...
  * `as_matching_blocks` **(Compute Cores)** (Impact: 17.3)
    * *Intent:* """ Convert to matching blocks Returns ------- matching blocks : list[MatchingBlock] Editops convert...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 146`, `args: 62`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 139`, `duplicate_logic: 16`
* *Architecture:* `api: 30`, `import: 1`
* *Defense:* `safety: 12`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02586
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/benchmarks/graph_pipeline/omp.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.866)
- **Top Global Matches:** file_cluster_3: 5.866, file_cluster_8: 23.12, file_cluster_6: 36.095
- **Magnitude:** 734.3 | **LOC:** 1420 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `measure_time_omp` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `graph_pipeline_omp_16_pipes` **(Compute Cores)** (Impact: 53.2)
    * *Intent:* // 16 pipes
  * `graph_pipeline_omp_15_pipes` **(Compute Cores)** (Impact: 49.8)
    * *Intent:* // 15 pipes
  * `graph_pipeline_omp_14_pipes` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* // 14 pipes
  * `graph_pipeline_omp_13_pipes` **(Compute Cores)** (Impact: 43.4)
    * *Intent:* // 13 pipes
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 22`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 49`, `dead_code: 47`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fstream, levelgraph.hpp, omp.h, thread
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/distance/Jaro_impl.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.337)
- **Top Global Matches:** file_cluster_4: 6.337, file_cluster_6: 10.622, file_cluster_15: 11.673
- **Magnitude:** 689.52 | **LOC:** 864 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.846; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (52.7%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flag_similar_characters_step` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `jaro_similarity` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `jaro_similarity` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `jaro_similarity_simd_long_s2` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `jaro_similarity_simd_short_s2` **(Many-Argument Workhorses)** (Impact: 27.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 153`, `args: 149`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 148`, `planned_debt: 6`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.846
  * `Choke Point (Betweenness):` 0.000265 | `Ripple Effect (Closeness):` 0.047593
  * `Imports (Out-Degree: 4):` cstddef, cstdint, PatternMatchVector.hpp, common.hpp, distance.hpp, intrinsics.hpp, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_control_flow.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_10: 6.438, file_cluster_15: 8.294, file_cluster_13: 8.965
- **Magnitude:** 662.84 | **LOC:** 1065 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.8%), Guard Balance (formerly Safety Score) (66.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multiple_loops` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* // ---------------------------------------------------------------------------- // Testcase: Multipl...
  * `TEST_CASE` **(Compute Cores)** (Impact: 16.1)
    * *Intent:* // ---------------------------------------------------------------------------- // BTreeCond // ----...
  * `conditional_spawn` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `hierarchical_condition` **(Callbacks & Closures)** (Impact: 11.4)
  * `multiple_branches` **(Callbacks & Closures)** (Impact: 10.2)
    * *Intent:* // ---------------------------------------------------------------------------- // Testcase: Multipl...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 126`, `args: 143`, `func_start: 88`
* *Risk/State:* `state_mutation: 168`, `dead_code: 6`
* *Architecture:* `import: 2`
* *Defense:* `safety: 10`, `test: 124`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` doctest.h, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/unittests/test_dependent_asyncs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_10: 7.289, file_cluster_15: 8.238, file_cluster_4: 9.059
- **Magnitude:** 654.48 | **LOC:** 1251 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.4%), Guard Balance (formerly Safety Score) (60.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simple_graph_2` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* // task dependence : // ---------------------------- // | |--> 3 --| | // | | --> 7 --->| // 0 ---| ...
  * `make_complex_graph` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* // | . | . | . | // ---> 100 --> . ---> 10200 --- // | . | // ---> 10100 -- // // level 0 : task 0 h...
  * `simple_graph` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* // ---------------------------------------------------------------------------- // Simple Graph // -...
  * `complete_linear_chain` **(Compute Cores)** (Impact: 16.0)
    * *Intent:* // ---------------------------------------------------------------------------- // Linear Chain with...
  * `parallel_graph_construction` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* // ---------------------------------------------------------------------------- // Parallel Graph Co...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 94 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 95`, `args: 115`, `func_start: 83`
* *Risk/State:* `state_mutation: 126`, `dead_code: 1`
* *Architecture:* `concurrency: 1`, `import: 8`
* *Defense:* `safety: 1`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doctest.h, for_each.hpp, module.hpp, reduce.hpp, scan.hpp, sort.hpp, transform.hpp, taskflow.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/extern/taskflow/taskflow/algorithm/sort.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.004)
- **Top Global Matches:** file_cluster_6: 8.004, file_cluster_4: 9.354, file_cluster_9: 15.008
- **Magnitude:** 653.68 | **LOC:** 650 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 1.48; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parallel_pdqsort` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `partition_right_branchless` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* // Partitions [begin, end) around pivot *begin using comparison function comp. Elements equal // to ...
  * `parallel_3wqsort` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* // ---------------------------------------------------------------------------- // 3-way quick sort ...
  * `partition_right` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* // Partitions [begin, end) around pivot *begin using comparison function comp. // Elements equal to ...
  * `partition_left` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* // Similar function to the one above, except elements equal to the pivot // are put to the left of t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 346
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 121`, `args: 24`, `func_start: 15`
* *Risk/State:* `state_mutation: 142`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.48
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.006462
  * `Imports (Out-Degree: 4):` taskflow.hpp
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `rapidfuzz-3.14.3/src/rapidfuzz/process_cpp.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.111)
- **Top Global Matches:** file_cluster_4: 7.111, file_cluster_15: 8.298, file_cluster_12: 8.844
- **Magnitude:** 623.84 | **LOC:** 719 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.656; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.2%), Guard Balance (formerly Safety Score) (60.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cdist_two_lists_impl` **(Many-Argument Workhorses)** (Impact: 138.4)
  * `set` **(Type Conversions)** (Impact: 48.9)
  * `run_parallel` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `cdist_single_list_impl` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `cpdist_cpp_impl` **(Many-Argument Workhorses)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 112`, `args: 60`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 48`, `planned_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `concurrency: 1`, `import: 9`
* *Defense:* `safety: 9`, `immutability_locks: 52`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` atomic, chrono, cpp_common.hpp, exception, rapidfuzz.h, stdexcept, for_each.hpp, taskflow.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rapidfuzz-3.14.3/src/rapidfuzz/fuzz_py.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.733)
- **Top Global Matches:** file_cluster_9: 6.733, file_cluster_16: 7.745, file_cluster_15: 7.94
- **Magnitude:** 602.78 | **LOC:** 878 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `partial_ratio_alignment` **(Many-Argument Workhorses)** (Impact: 35.4)
  * `token_set_ratio` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `_partial_ratio_impl` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* """ implementation of partial_ratio. This assumes len(s1) <= len(s2). """
  * `WRatio` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `partial_token_ratio` **(Many-Argument Workhorses)** (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 81`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 113`, `planned_debt: 5`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 4`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.494
  * `Choke Point (Betweenness):` 0.000139 | `Ripple Effect (Closeness):` 0.003231
  * `Imports (Out-Degree: 4):` __future__, math, rapidfuzz._common_py, rapidfuzz._utils, rapidfuzz.distance, rapidfuzz.distance.Indel_py
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/iterator.hpp` (CPP) | Magnitude: 27.12 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 11, branch: 10, indent_spaces: 8, args: 2
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/async.hpp` (CPP) | Magnitude: 170.34 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 86, branch: 53, args: 36
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/topology.hpp` (CPP) | Magnitude: 19.7 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 29, branch: 6, api: 4
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/cublas_core/cublas_level3.hpp` (CPP) | Magnitude: 311.7 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 356, pointers: 102, immutability_locks: 92, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `rapidfuzz-3.14.3/extern/taskflow/examples/sycl/sycl_device.cpp` (CPP) | Magnitude: 6.48 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 4, debug_prints: 3, listeners: 3
- `rapidfuzz-3.14.3/extern/taskflow/examples/sycl/sycl_reduce.cpp` (CPP) | Magnitude: 23.4 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 6, core_var_decl: 6, state_mutation: 5
- `rapidfuzz-3.14.3/extern/taskflow/examples/corun.cpp` (CPP) | Magnitude: 19.68 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, pointers: 6, state_mutation: 5, core_var_decl: 4
- `rapidfuzz-3.14.3/extern/taskflow/examples/sycl/sycl_transform.cpp` (CPP) | Magnitude: 29.52 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, args: 7, core_var_decl: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `rapidfuzz-3.14.3/extern/taskflow/examples/reduce.cpp` (CPP) | Magnitude: 37.44 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 23, core_var_decl: 15, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/cuda/algorithm/merge.hpp` (CPP) | Magnitude: 213.8 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 165, core_var_decl: 56, design_snake_case: 50
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/macros.hpp` (CPP) | Magnitude: 15.78 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 32, reflection_metaprogramming: 18, indent_spaces: 18, structural_boundaries: 2
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/sycl/algorithm/reduce.hpp` (CPP) | Magnitude: 143.64 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 93, core_var_decl: 37, design_snake_case: 32
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/task.hpp` (CPP) | Magnitude: 245.1 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 185, pointers: 90, immutability_locks: 85
- `rapidfuzz-3.14.3/src/rapidfuzz/cpp_common.pxd` (PYTHON) | Magnitude: 248.28 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 348, branch: 54, state_mutation: 46, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `rapidfuzz-3.14.3/tests/test_fuzz.py` (PYTHON) | Magnitude: 176.66 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 157, safety: 83, core_var_decl: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `rapidfuzz-3.14.3/extern/taskflow/benchmarks/hetero_traversal/graph.hpp` (CPP) | Magnitude: 87.42 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 22, structural_boundaries: 19, branch: 13
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/freelist.hpp` (CPP) | Magnitude: 14.66 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, args: 5, func_start: 5
- `rapidfuzz-3.14.3/extern/taskflow/unittests/test_deferred_pipelines.cpp` (CPP) | Magnitude: 1369.5 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1097, test: 261, branch: 236, state_mutation: 211
- `rapidfuzz-3.14.3/extern/taskflow/unittests/test_deferred_scalable_pipelines.cpp` (CPP) | Magnitude: 1469.44 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1132, test: 280, state_mutation: 242, branch: 237
- `rapidfuzz-3.14.3/tests/distance/test_Indel.py` (PYTHON) | Magnitude: 12.26 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 29, safety: 19, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/test/distance/examples/ocr.hpp` (CPP) | Magnitude: 12.6 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 2, import: 2, macros: 1
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/taskflow.hpp` (CPP) | Magnitude: 2.4 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 12, macros: 5, reflection_metaprogramming: 4, import: 4
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/__init__.pyi` (PYTHON) | Magnitude: 15.42 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 16, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `rapidfuzz-3.14.3/src/rapidfuzz/distance/__init__.py` (PYTHON) | Magnitude: 17.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 6, import: 3, api: 1
- `rapidfuzz-3.14.3/tests/distance/test_LCSseq.py` (PYTHON) | Magnitude: 9.62 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 22, safety: 13, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `rapidfuzz-3.14.3/tools/test_submodules.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, state_mutation: 8, core_var_decl: 8
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/bench/bench-lcs.cpp` (CPP) | Magnitude: 137.98 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 35, pointers: 31, args: 26
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/bench/bench-jarowinkler.cpp` (CPP) | Magnitude: 138.22 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 103, args: 38, state_mutation: 35, pointers: 32

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 1.913** (Bridge: 0.0194 * Flux: 98.3997%)
- `rapidfuzz-3.14.3/src/rapidfuzz/cpp_common.hpp` -> **Severity: 1.793** (Bridge: 0.0182 * Flux: 98.4087%)
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/distance.hpp` -> **Severity: 1.098** (Bridge: 0.011 * Flux: 99.9976%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/taskflow.hpp` -> **Severity: 0.594** (Bridge: 0.0061 * Flux: 96.8838%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/math.hpp` -> **Severity: 0.282** (Bridge: 0.0028 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/error.hpp` -> **Severity: 5.782** (Embedded: 0.1038 * Error Risk: 55.6895%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 5.515** (Embedded: 0.0995 * Error Risk: 55.4233%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/async.hpp` -> **Severity: 5.49** (Embedded: 0.0997 * Error Risk: 55.0518%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/runtime.hpp` -> **Severity: 5.274** (Embedded: 0.1004 * Error Risk: 52.5192%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/observer.hpp` -> **Severity: 4.75** (Embedded: 0.0748 * Error Risk: 63.5015%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/executor.hpp` -> **Severity: 2041.0** (Blast Radius: 20.41 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/utility/stream.hpp` -> **Severity: 1905.5** (Blast Radius: 19.055 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/taskflow/core/runtime.hpp` -> **Severity: 1803.06** (Blast Radius: 20.034 * Doc Risk: 90.0%)
- `rapidfuzz-3.14.3/extern/rapidfuzz-cpp/rapidfuzz/details/type_traits.hpp` -> **Severity: 1798.9** (Blast Radius: 17.989 * Doc Risk: 100.0%)
- `rapidfuzz-3.14.3/extern/taskflow/sandbox/seismic/video.h` -> **Severity: 1694.2** (Blast Radius: 16.942 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 519 literal sites + 3 sites through wrappers = 522
- **`memory_alloc`:** 139 literal sites + 8 sites through wrappers = 147
- **`panics_and_aborts`:** 260 literal sites + 1 sites through wrappers = 261

- `alloc_matrix` (function, memory_alloc, primitive): 4 call sites in 2 files -- `rapidfuzz-3.14.3/extern/taskflow/sandbox/strassen/strassen.hpp`
- `allocate_matrix` (function, memory_alloc, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/benchmarks/matrix_multiplication/matrix_multiplication.hpp`
- `f1` (function, debug_prints, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/examples/parallel_graph_pipeline.cpp`
- `f2` (function, debug_prints, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/examples/parallel_graph_pipeline.cpp`
- `f3` (function, debug_prints, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/examples/parallel_graph_pipeline.cpp`
- `init_ABC` (function, memory_alloc, via alloc_matrix): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/sandbox/strassen/strassen.hpp`
- `instance` (function, memory_alloc, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/benchmarks/thread_pool/ThreadPool.hpp`
- `lsremote` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/tools/test_submodules.py`
- `strassen_tbb` (function, memory_alloc, primitive): 1 call sites in 1 files -- `rapidfuzz-3.14.3/extern/taskflow/sandbox/strassen/tbb.cpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24837 call pairs -- scoped 28.7%, unique 1.2%, ambiguous 29.0%, external 41.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 21770 | 29.6% | 1.3% | 31.5% | 37.6% |
| python | 2672 | 23.1% | 0.0% | 12.8% | 64.1% |
| javascript | 272 | 13.2% | 0.0% | 0.0% | 86.8% |
| c | 106 | 41.5% | 0.0% | 4.7% | 53.8% |
| shell | 17 | 5.9% | 0.0% | 0.0% | 94.1% |

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
