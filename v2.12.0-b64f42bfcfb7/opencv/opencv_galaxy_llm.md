# ARCHITECTURAL_BRIEF: opencv
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/opencv/opencv.git` |
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
- **Scope:** 4351 analyzed artifact(s), 1007428 LOC.
- **Load-bearing artifact:** `modules/core/include/opencv2/core.hpp` -- 390 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `modules/ts/src/ts_gtest.cpp` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `modules/features2d/src/agast.cpp` at magnitude 11746.16 (structural weight, not risk).
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
| Total Artifacts | 7688 |
| Analyzed Artifacts (Scanned) | 4351 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3337 |
| Total LOC | 1007428 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 56.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6368 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.057 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.5865 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 186 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 2871 | 880690 | 66.0% |
| PYTHON | 372 | 41060 | 8.5% |
| PLAINTEXT | 322 | 6 | 7.4% |
| JAVA | 203 | 25839 | 4.7% |
| OBJECTIVE-C | 124 | 11132 | 2.8% |
| C | 112 | 23861 | 2.6% |
| XML | 80 | 0 | 1.8% |
| MARKDOWN | 35 | 0 | 0.8% |
| JAVASCRIPT | 35 | 5661 | 0.8% |
| SWIFT | 32 | 6125 | 0.7% |
| JSON | 31 | 2696 | 0.7% |
| SHELL | 26 | 982 | 0.6% |
| HTML | 21 | 1521 | 0.5% |
| GROOVY | 19 | 672 | 0.4% |
| CSHARP | 12 | 592 | 0.3% |
| PROTO | 10 | 1165 | 0.2% |
| BATCH | 9 | 550 | 0.2% |
| YAML | 8 | 426 | 0.2% |
| GLSL | 6 | 701 | 0.1% |
| SCALA | 5 | 95 | 0.1% |
| MAKEFILE | 4 | 105 | 0.1% |
| M4 | 4 | 71 | 0.1% |
| KOTLIN | 3 | 145 | 0.1% |
| PERL | 2 | 496 | 0.0% |
| CSS | 2 | 181 | 0.0% |
| DOCKERFILE | 1 | 11 | 0.0% |
| POWERSHELL | 1 | 277 | 0.0% |
| PBTXT | 1 | 2368 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4266 |
| utf-8 | bom | 79 |
| unknown | unknown | 6 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 20%, Data / Markup / Trivial 16%, Declarative / Non-Code 14%, Many-Argument Workhorses Files 12%, Parameter Forwarders Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3994 | 91.8% |
| Unknown | 6 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 351 | 8.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3337*

**Composition by Extension & Reason:**
- `.jpg`: 579x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.h`: 555x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 635 LOC), 1x Excluded (Machine-Generated Source Code Signature: 44946 LOC)
- `.c`: 529x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 443x Excluded (Explicitly Denied Extension: '.png')
- `.markdown`: 300x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 125x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.asm`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 7x Excluded (Unsupported Extension: '.appxmanifest')
- `.cc`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 34121 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5847 LOC)
- `.patch`: 41x Excluded (Unsupported Extension: '.patch'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 3x Excluded (Massive Static Asset Blob: 24351 LOC), 3x Excluded (Static Asset Blob without Intent: 1506 LOC), 1x Excluded (Massive Static Asset Blob: 12214 LOC)
- `.txt`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cu`: 30x Unsupported Format (.cu), 2x Excluded (Unsupported Extension: '.cu')
- `.in`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 29.1 | 16.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.9 | 45.5 | 54.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.4 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 46.1 | 21.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 43515 | 2202 | 26 | `modules/calib3d/src/dls.cpp` |
| cleanup | 1153 | 315 | 0 | `modules/java/test/android_test/src/org/opencv/test/OpenCVTestCase.java` |
| guards | 90456 | 2860 | 47 | `modules/ts/include/opencv2/ts/ts_gtest.h` |
| danger | 8062 | 1221 | 4 | `modules/core/src/opencl/runtime/autogenerated/opencl_core_impl.hpp` |
| concurrency | 1642 | 273 | 0 | `modules/gapi/test/streaming/gapi_streaming_utils_test.cpp` |
| connectivity | 14269 | 1866 | 8 | `modules/ts/include/opencv2/ts/ts_gtest.h` |
| io | 2062 | 390 | 0 | `platforms/android/build_sdk.py` |
| crypto | 3 | 3 | 0 | `modules/python/test/tests_common.py` |
| ipc | 127 | 44 | 0 | `modules/gapi/test/streaming/gapi_streaming_tests.cpp` |
| time | 71 | 33 | 0 | `hal/openvx/hal/openvx_hal.cpp` |
| serialization | 4 | 2 | 0 | `modules/ts/misc/xls-report.py` |
| regex | 269 | 63 | 0 | `modules/objc/generator/gen_objc.py` |
| events | 1324 | 177 | 0 | `modules/gapi/src/api/kernels_core.cpp` |
| tests | 16041 | 565 | 3 | `modules/core/test/test_mat.cpp` |
| docs | 12483 | 1557 | 5 | `modules/core/include/opencv2/core/core_c.h` |
| debt | 8251 | 1369 | 4 | `hal/riscv-rvv/src/imgproc/color.cpp` |
| mutation | 350030 | 3201 | 207 | `modules/imgproc/src/color_lab.cpp` |
| dead_code | 18755 | 2120 | 11 | `modules/ts/src/ts_gtest.cpp` |
| credential | 24 | 12 | 0 | `samples/dnn/models.yml` |
| threat | 25 | 16 | 0 | `modules/gapi/test/render/gapi_render_tests_ocv.cpp` |
| ml_ai | 2317 | 409 | 0 | `modules/core/misc/objc/test/CoreTest.swift` |
| ui | 480 | 87 | 0 | `modules/highgui/src/window_QT.h` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `platforms/android/build_sdk.py` (Hits: 98)
- `platforms/ios/build_framework.py` (Hits: 97)
- `modules/objc/generator/gen_objc.py` (Hits: 81)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.hpp** (`modules/core/include/opencv2/core.hpp`) — 390 inbound connections
2. **imgproc.hpp** (`modules/imgproc/include/opencv2/imgproc.hpp`) — 313 inbound connections
3. **highgui.hpp** (`modules/highgui/include/opencv2/highgui.hpp`) — 291 inbound connections
4. **ts_gtest.h** (`modules/ts/include/opencv2/ts/ts_gtest.h`) — 270 inbound connections
5. **scalar.hpp** (`modules/gapi/include/opencv2/gapi/own/scalar.hpp`) — 267 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ts_gtest.cpp** (`modules/ts/src/ts_gtest.cpp`) — 63 outbound dependencies
2. **system.cpp** (`modules/core/src/system.cpp`) — 46 outbound dependencies
3. **ts_gtest.h** (`modules/ts/include/opencv2/ts/ts_gtest.h`) — 44 outbound dependencies
4. **parallel.cpp** (`modules/core/src/parallel.cpp`) — 36 outbound dependencies
5. **gapi_streaming_vpp_preproc_test.cpp** (`modules/gapi/test/streaming/gapi_streaming_vpp_preproc_test.cpp`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `OAST_9_16` **(Many-Argument Workhorses)** (@ `modules/features2d/src/agast.cpp`) -> Impact: **3921.1** | LOC: 2102
- `AGAST_7_12d` **(Many-Argument Workhorses)** (@ `modules/features2d/src/agast.cpp`) -> Impact: **3276.2** | LOC: 2443
- `AGAST_7_12s` **(Many-Argument Workhorses)** (@ `modules/features2d/src/agast.cpp`) -> Impact: **2774.0** | LOC: 2080
- `operator()` **(Many-Argument Workhorses)** (@ `modules/imgproc/src/connectedcomponents.cpp`) -> Impact: **1140.2** | LOC: 1338
- `AGAST_5_8` **(Many-Argument Workhorses)** (@ `modules/features2d/src/agast.cpp`) -> Impact: **952.1** | LOC: 762
  * *Intent:* #if (defined __i386__ || defined(_M_IX86) || defined __x86_64__ || defined(_M_X64) || defined(_M_ARM64) || defined(__aarch64__) || defined(__arm__))
- `packInputData` **(Many-Argument Workhorses)** (@ `modules/dnn/src/layers/cpu_kernels/convolution.cpp`) -> Impact: **782.2** | LOC: 498
- `operator()` **(Many-Argument Workhorses)** (@ `modules/imgproc/src/connectedcomponents.cpp`) -> Impact: **635.1** | LOC: 1048
- `stereoCalibrateImpl` **(Many-Argument Workhorses)** (@ `modules/calib3d/src/calibration.cpp`) -> Impact: **593.2** | LOC: 531
  * *Intent:* //////////////////////////////// Stereo Calibration ///////////////////////////////////
- `CvCaptureCAM_XIMEA::setProperty` **(Many-Argument Workhorses)** (@ `modules/videoio/src/cap_ximea.cpp`) -> Impact: **580.9** | LOC: 706
  * *Intent:* /**********************************************************************************/
- `calibrateCameraInternal` **(Many-Argument Workhorses)** (@ `modules/calib3d/src/calibration.cpp`) -> Impact: **545.7** | LOC: 457

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `modules/imgproc/src` | 104 | 94706.62 | 53.05% | 22.53% |
| `modules/core/src` | 110 | 80944.24 | 54.39% | 33.43% |
| `modules/calib3d/src` | 48 | 31339.38 | 47.82% | 22.67% |
| `modules/videoio/src` | 63 | 27280.86 | 39.83% | 47.36% |
| `hal/carotene/src` | 57 | 26862.14 | 49.17% | 9.74% |
| `modules/features2d/src` | 28 | 22212.44 | 50.4% | 46.73% |
| `modules/dnn/src/layers` | 57 | 20936.38 | 52.35% | 64.5% |
| `modules/imgproc/test` | 46 | 18812.36 | 24.98% | 0.0% |
| `modules/imgcodecs/src` | 55 | 17143.0 | 34.87% | 31.21% |
| `modules/core/test` | 39 | 16438.18 | 17.69% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `apps/traincascade/features.cpp` -> **100.0%** Exposure
- `hal/riscv-rvv/src/core/sqrt.cpp` -> **100.0%** Exposure
- `modules/core/include/opencv2/core/cuda/border_interpolate.hpp` -> **100.0%** Exposure
- `modules/dnn/src/cuda/block_stride_range.hpp` -> **100.0%** Exposure
- `modules/dnn/src/cuda/functors.hpp` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/annotation/opencv_annotation.cpp` -> **100.0%** Exposure
- `apps/createsamples/createsamples.cpp` -> **100.0%** Exposure
- `apps/createsamples/utility.cpp` -> **100.0%** Exposure
- `apps/interactive-calibration/calibController.cpp` -> **100.0%** Exposure
- `apps/interactive-calibration/frameProcessor.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `modules/ts/src/ts_gtest.cpp` -> **262** Orphaned Functions | **10** Duplicates
- `modules/dnn/test/test_onnx_importer.cpp` -> **263** Orphaned Functions | **0** Duplicates
- `modules/highgui/src/window_QT.cpp` -> **197** Orphaned Functions | **0** Duplicates
- `modules/core/src/ocl.cpp` -> **190** Orphaned Functions | **2** Duplicates
- `modules/imgproc/misc/java/test/ImgprocTest.java` -> **172** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14701` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `modules/features2d/src/agast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.517)
- **Top Global Matches:** file_cluster_8: 10.517, file_cluster_6: 10.521, file_cluster_4: 17.731
- **Magnitude:** 11746.16 | **LOC:** 8200 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.109; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.9%), Guard Balance (formerly Safety Score) (52.3%), Mutation Surface (formerly State Flux) (33.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OAST_9_16` **(Many-Argument Workhorses)** (Impact: 3921.1)
  * `AGAST_7_12d` **(Many-Argument Workhorses)** (Impact: 3276.2)
  * `AGAST_7_12s` **(Many-Argument Workhorses)** (Impact: 2774.0)
  * `AGAST_5_8` **(Many-Argument Workhorses)** (Impact: 952.1)
    * *Intent:* #if (defined __i386__ || defined(_M_IX86) || defined __x86_64__ || defined(_M_X64) || defined(_M_ARM...
  * `AGAST` **(Many-Argument Workhorses)** (Impact: 125.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5369`, `structural_boundaries: 1710`, `args: 33`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 138`, `unreferenced_by_name: 13`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000918
  * `Imports (Out-Degree: 6):` agast_score.hpp, precomp.hpp
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `apps/traincascade/old_ml_tree.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.869)
- **Top Global Matches:** file_cluster_8: 7.869, file_cluster_6: 10.55, file_cluster_4: 18.683
- **Magnitude:** 5571.02 | **LOC:** 4154 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.9%), Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.7654% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvDTreeTrainData::set_data` **(Many-Argument Workhorses)** (Impact: 477.4)
  * `CvDTree::predict` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `CvDTree::find_split_cat_class` **(Many-Argument Workhorses)** (Impact: 107.3)
  * `CvDTreeTrainData::get_vectors` **(Many-Argument Workhorses)** (Impact: 82.4)
  * `CvDTree::split_node_data` **(Many-Argument Workhorses)** (Impact: 82.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1115 instances
* *State Mutation (weighted view):* 3469
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 833`, `structural_boundaries: 98`, `args: 115`, `func_start: 81`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1239`, `dead_code: 9`, `planned_debt: 3`, `unreferenced_by_name: 60`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 165`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000459
  * `Imports (Out-Degree: 14):` ctype.h, old_ml_precomp.hpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/connectedcomponents.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.228)
- **Top Global Matches:** file_cluster_6: 7.228, file_cluster_4: 11.629, file_cluster_8: 14.979
- **Magnitude:** 5570.54 | **LOC:** 5800 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 0.133; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `operator()` **(Many-Argument Workhorses)** (Impact: 1140.2)
  * `operator()` **(Many-Argument Workhorses)** (Impact: 635.1)
  * `operator()` **(Many-Argument Workhorses)** (Impact: 224.6)
  * `operator()` **(Many-Argument Workhorses)** (Impact: 224.6)
  * `connectedComponents_sub1` **(Many-Argument Workhorses)** (Impact: 139.8)
    * *Intent:* //L's type must have an appropriate depth for the number of pixels in I
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 789 instances
* *State Mutation (weighted view):* 2421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1458`, `structural_boundaries: 209`, `args: 359`, `func_start: 68`, `class_start: 20`
* *Risk/State:* `state_mutation: 843`, `dead_code: 13`, `duplicate_logic: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `doc: 1`, `immutability_locks: 420`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.133
  * `Choke Point (Betweenness):` 0.000201 | `Ripple Effect (Closeness):` 0.004979
  * `Imports (Out-Degree: 6):` ccl_bolelli_forest.inc.hpp, ccl_bolelli_forest_firstline.inc.hpp, ccl_bolelli_forest_lastline.inc.hpp, ccl_bolelli_forest_singleline.inc.hpp, precomp.hpp, vector
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `modules/ts/src/ts_func.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.83)
- **Top Global Matches:** file_cluster_8: 6.83, file_cluster_6: 17.294, file_cluster_3: 20.001
- **Magnitude:** 5559.14 | **LOC:** 3322 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.086; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Complexity Load (formerly Cognitive Load) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `threshold` **(Many-Argument Workhorses)** (Impact: 190.8)
  * `cmpEps` **(Many-Argument Workhorses)** (Impact: 160.4)
    * *Intent:* #define CMP_EPS_OK 0 #define CMP_EPS_BIG_DIFF -1 #define CMP_EPS_INVALID_TEST_DATA -2 // there is Na...
  * `muldiv` **(Many-Argument Workhorses)** (Impact: 96.2)
  * `copyMakeBorder` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `transform` **(Many-Argument Workhorses)** (Impact: 77.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 849 instances
* *State Mutation (weighted view):* 2559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1064`, `structural_boundaries: 172`, `args: 99`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 861`, `dead_code: 3`, `unreferenced_by_name: 30`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 406`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.086
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.04442
  * `Imports (Out-Degree: 10):` float.h, limits.h, types_c.h, precomp.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/histogram.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_8: 6.477, file_cluster_6: 16.319, file_cluster_3: 21.058
- **Magnitude:** 5204.44 | **LOC:** 3658 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **5**; blast radius 0.325; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 92.4528% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calcHist_` **(Many-Argument Workhorses)** (Impact: 335.7)
    * *Intent:* ////////////////////////////////// C A L C U L A T E H I S T O G R A M /////////////////////////////...
  * `calcHist_8u` **(Many-Argument Workhorses)** (Impact: 170.3)
  * `calcBackProj_` **(Many-Argument Workhorses)** (Impact: 157.0)
  * `cv::calcHist` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* #endif
  * `calcBackProj_8u` **(Many-Argument Workhorses)** (Impact: 100.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 859 instances
* *State Mutation (weighted view):* 2678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 823`, `structural_boundaries: 121`, `args: 83`, `func_start: 53`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 960`, `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 3`, `doc: 6`, `sync_locks: 5`, `immutability_locks: 239`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.010593 | `Ripple Effect (Closeness):` 0.077619
  * `Imports (Out-Degree: 18):` opencl_kernels_imgproc.hpp, intrin.hpp, ovx_defs.hpp, tls.hpp, precomp.hpp
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `modules/core/src/dxt.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.499)
- **Top Global Matches:** file_cluster_6: 6.499, file_cluster_4: 8.333, file_cluster_15: 16.281
- **Magnitude:** 5164.4 | **LOC:** 4722 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 0.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DFT` **(Many-Argument Workhorses)** (Impact: 144.2)
    * *Intent:* // mixed-radix complex discrete Fourier transform: double-precision version
  * `DFTInit` **(Many-Argument Workhorses)** (Impact: 128.7)
  * `init` **(Many-Argument Workhorses)** (Impact: 119.5)
  * `init` **(Many-Argument Workhorses)** (Impact: 99.4)
  * `colDft` **(Many-Argument Workhorses)** (Impact: 77.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 829 instances
* *State Mutation (weighted view):* 2812
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 763`, `structural_boundaries: 366`, `args: 171`, `func_start: 132`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 1154`, `dead_code: 4`, `planned_debt: 4`, `unreferenced_by_name: 17`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `doc: 3`, `immutability_locks: 282`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.001335
  * `Imports (Out-Degree: 8):` map, opencl_kernels_core.hpp, opencl_clfft.hpp, opencl_core.hpp, precomp.hpp
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `samples/winrt/FaceDetection/FaceDetection/FaceDetection_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/ImageManipulations/MediaCapture_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/JavaScript/MediaCaptureJavaScript_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/OcvImageProcessing/OcvImageProcessing/OcvImageProcessing_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt_universal/VideoCaptureXAML/video_capture_xaml/video_capture_xaml.Windows/video_capture_xaml.Windows_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt_universal/VideoCaptureXAML/video_capture_xaml/video_capture_xaml.WindowsPhone/video_capture_xaml.WindowsPhone_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/color_lab.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.745)
- **Top Global Matches:** file_cluster_8: 8.745, file_cluster_6: 9.078, file_cluster_4: 17.055
- **Magnitude:** 4983.4 | **LOC:** 4854 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.3; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cvtBGRtoLab` **(Many-Argument Workhorses)** (Impact: 160.6)
    * *Intent:* // 8u, 32f
  * `cvtLabtoBGR` **(Many-Argument Workhorses)** (Impact: 153.7)
    * *Intent:* // 8u, 32f
  * `cvtBGRtoXYZ` **(Many-Argument Workhorses)** (Impact: 81.5)
  * `cvtXYZtoBGR` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `operator()` **(Many-Argument Workhorses)** (Impact: 71.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 825 instances
* *State Mutation (weighted view):* 2983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 182`, `args: 285`, `func_start: 87`, `class_start: 24`
* *Risk/State:* `state_mutation: 1333`, `dead_code: 51`, `planned_debt: 3`, `duplicate_logic: 11`, `unreferenced_by_name: 12`
* *Architecture:* `import: 5`
* *Defense:* `doc: 4`, `immutability_locks: 278`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.3
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.064836
  * `Imports (Out-Degree: 7):` color.hpp, opencl_kernels_imgproc.hpp, intrin.hpp, softfloat.hpp, precomp.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/core/src/ocl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.357)
- **Top Global Matches:** file_cluster_4: 8.357, file_cluster_12: 8.629, file_cluster_15: 9.375
- **Magnitude:** 4878.78 | **LOC:** 7665 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **91** in-repo importer(s); it depends on **27**; blast radius 3.772; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (89.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.1%)
- **Documentation Coverage:** 97.9955% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectOpenCLDevice` **(Many-Argument Workhorses)** (Impact: 148.3)
  * `copy` **(Many-Argument Workhorses)** (Impact: 139.2)
  * `upload` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `Kernel::Impl::run` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `convertFromImage` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* /* // Convert OpenCL image2d_t memory to UMat */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 533 instances
* *State Mutation (weighted view):* 1868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1089`, `structural_boundaries: 700`, `args: 507`, `func_start: 445`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 86`, `high_risk_execution: 1`, `state_mutation: 802`, `dead_code: 9`, `planned_debt: 11`, `duplicate_logic: 2`, `unreferenced_by_name: 190`
* *Architecture:* `io: 7`, `api: 15`, `import: 27`
* *Defense:* `safety: 72`, `doc: 13`, `sync_locks: 37`, `immutability_locks: 487`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.772
  * `Choke Point (Betweenness):` 0.00748 | `Ripple Effect (Closeness):` 0.152137
  * `Imports (Out-Degree: 28):` deque, fstream, inttypes.h, list, map, ocl_disabled.impl.hpp, opencl_kernels_core.hpp, bufferpool.hpp...
  * `Imported By (In-Degree: 91):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/resize.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.97)
- **Top Global Matches:** file_cluster_4: 5.97, file_cluster_6: 10.309, file_cluster_15: 11.93
- **Magnitude:** 4681.28 | **LOC:** 4261 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **9**; blast radius 0.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.6%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.0826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resize` **(Many-Argument Workhorses)** (Impact: 288.9)
  * `ocl_resize` **(Many-Argument Workhorses)** (Impact: 127.1)
  * `ipp_resize` **(Many-Argument Workhorses)** (Impact: 113.1)
    * *Intent:* #endif
  * `operator()` **(Many-Argument Workhorses)** (Impact: 90.7)
  * `resize_bitExact` **(Many-Argument Workhorses)** (Impact: 67.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 856 instances
* *State Mutation (weighted view):* 2792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 587`, `structural_boundaries: 490`, `args: 384`, `func_start: 109`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1080`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 327`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.392
  * `Choke Point (Betweenness):` 0.000535 | `Ripple Effect (Closeness):` 0.010689
  * `Imports (Out-Degree: 12):` fixedpoint.inl.hpp, hal_replacement.hpp, opencl_kernels_imgproc.hpp, intrin.hpp, ovx_defs.hpp, softfloat.hpp, buffer_area.private.hpp, precomp.hpp...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `modules/objdetect/src/qrcode.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.461)
- **Top Global Matches:** file_cluster_6: 6.461, file_cluster_4: 9.856, file_cluster_8: 15.991
- **Magnitude:** 4422.72 | **LOC:** 4744 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `QRDetect::getQuadrilateral` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `QRDetectMulti::findNumberLocalizationPoints` **(Compute Cores)** (Impact: 80.1)
  * `ImplContour::decodeMulti` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `QRDecode::findTempPatternsAddingPoints` **(Compute Cores)** (Impact: 51.5)
  * `QRDetectMulti::ParallelSearch::operator()` **(Compute Cores)** (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 828 instances
* *State Mutation (weighted view):* 2620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 883`, `structural_boundaries: 313`, `args: 142`, `func_start: 138`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 964`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 78`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 8`, `doc: 4`, `immutability_locks: 294`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` array, cmath, graphical_code_detector_impl.hpp, limits, map, calib3d.hpp, logger.hpp, objdetect.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/ts/src/ts_gtest.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_15: 7.664, file_cluster_11: 9.018, file_cluster_16: 9.336
- **Magnitude:** 4098.76 | **LOC:** 11449 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **249** in-repo importer(s); it depends on **63**; blast radius 5.76; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (68.9%), Guard Balance (formerly Safety Score) (58.1%)
- **Documentation Coverage:** 99.8374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsValidUTF8` **(Compute Cores)** (Impact: 55.4)
  * `PrintAsCharLiteralTo` **(Compute Cores)** (Impact: 45.7)
    * *Intent:* // Prints a wide or narrow char c as a character literal without the // quotes, escaping it when nec...
  * `CreateUnifiedDiff` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* // Create a list of diff hunks in Unified diff format. // Each hunk has a header generated by PrintH...
  * `XmlUnitTestResultPrinter::EscapeXml` **(Compute Cores)** (Impact: 41.9)
    * *Intent:* // Returns an XML-escaped copy of the input string str. If is_attribute // is true, the text is mean...
  * `DefaultDeathTestFactory::Create` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* # endif // !GTEST_OS_WINDOWS // Creates a concrete DeathTest-derived class that depends on the // --...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 335 instances
* *Memory Alloc (weighted view):* 41
* *State Mutation (weighted view):* 1122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1041`, `structural_boundaries: 1098`, `args: 670`, `func_start: 619`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 6`, `state_mutation: 452`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 26`, `duplicate_logic: 10`, `unreferenced_by_name: 262`
* *Architecture:* `io: 5`, `api: 36`, `import: 39`
* *Defense:* `safety: 7`, `doc: 3`, `test: 18`, `sync_locks: 32`, `immutability_locks: 1100`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.76
  * `Choke Point (Betweenness):` 0.013442 | `Ripple Effect (Closeness):` 0.149999
  * `Imports (Out-Degree: 3):` failure_signal_handler.h, stacktrace.h, symbolize.h, str_cat.h, algorithm, inet.h, cctype, climits...
  * `Imported By (In-Degree: 249):` (Excluded from Brief to save tokens)

### `modules/core/src/matmul.simd.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_6: 6.71, file_cluster_4: 8.859, file_cluster_15: 16.597
- **Magnitude:** 3971.56 | **LOC:** 2630 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.104; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%)
- **Documentation Coverage:** 88.5246% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gemmImpl` **(Many-Argument Workhorses)** (Impact: 417.6)
  * `GEMMSingleMul` **(Many-Argument Workhorses)** (Impact: 217.5)
  * `MulTransposedR` **(Many-Argument Workhorses)** (Impact: 88.6)
    * *Intent:* #if !defined(CV_MULTRANSPOSED_BASELINE_ONLY) || defined(CV_CPU_BASELINE_MODE) /*********************...
  * `getMulTransposedFunc` **(Many-Argument Workhorses)** (Impact: 76.5)
  * `perspectiveTransform_` **(Many-Argument Workhorses)** (Impact: 73.0)
    * *Intent:* /****************************************************************************************\ * Perspec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 742 instances
* *State Mutation (weighted view):* 2355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 142`, `args: 86`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 871`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`, `immutability_locks: 229`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.096556
  * `Imports (Out-Degree: 3):` precomp.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/core/src/softfloat.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.182)
- **Top Global Matches:** file_cluster_4: 6.182, file_cluster_6: 8.024, file_cluster_15: 12.907
- **Magnitude:** 3905.78 | **LOC:** 4298 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 0.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.2754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `softfloat_mulAddF64` **(Many-Argument Workhorses)** (Impact: 103.7)
  * `softfloat_mulAddF32` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `f32_roundToInt` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `f64_roundToInt` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `f64_rem` **(Many-Argument Workhorses)** (Impact: 57.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 704 instances
* *State Mutation (weighted view):* 2273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 653`, `structural_boundaries: 429`, `args: 172`, `func_start: 138`, `class_start: 33`
* *Risk/State:* `state_mutation: 865`, `dead_code: 1`, `unreferenced_by_name: 28`
* *Architecture:* `import: 2`
* *Defense:* `doc: 3`, `immutability_locks: 122`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.006607
  * `Imports (Out-Degree: 2):` softfloat.hpp, precomp.hpp
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `apps/pattern-tools/svgfig.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.413)
- **Top Global Matches:** file_cluster_4: 8.413, file_cluster_12: 10.319, file_cluster_15: 12.546
- **Magnitude:** 3854.42 | **LOC:** 3692 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.148; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.4%)
- **Documentation Coverage:** 33.7079% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SVG` **(Many-Argument Workhorses)** (Impact: 214.1)
    * *Intent:* """Apply the transformation "trans" and return an SVG object."""
  * `Path` **(Many-Argument Workhorses)** (Impact: 124.8)
    * *Intent:* """Apply the transformation "trans" and return a Path object in global coordinates. If local=True, r...
  * `compute_ticks` **(Many-Argument Workhorses)** (Impact: 68.5)
    * *Intent:* """Return less than -N or exactly N optimal linear ticks. Normally only used internally. """
  * `SVG` **(Many-Argument Workhorses)** (Impact: 67.8)
    * *Intent:* """Apply the transformation "trans" and return an SVG object."""
  * `window` **(Many-Argument Workhorses)** (Impact: 66.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 530 instances
* *State Mutation (weighted view):* 1882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 711`, `structural_boundaries: 418`, `args: 191`, `func_start: 161`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 62`, `high_risk_execution: 9`, `state_mutation: 822`, `dead_code: 1`, `fragile_debt: 5`, `duplicate_logic: 8`
* *Architecture:* `io: 15`, `api: 128`, `import: 5`
* *Defense:* `safety: 77`, `doc: 114`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000306
  * `Imports (Out-Degree: 0):` _winreg, cmath, codecs, copy, gzip, itertools, math, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/filter.simd.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.729)
- **Top Global Matches:** file_cluster_6: 6.729, file_cluster_4: 9.307, file_cluster_8: 16.663
- **Magnitude:** 3681.46 | **LOC:** 3258 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.11; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%)
- **Documentation Coverage:** 91.8605% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `operator()` **(Many-Argument Workhorses)** (Impact: 171.1)
  * `getLinearColumnFilter` **(Many-Argument Workhorses)** (Impact: 149.0)
  * `getLinearFilter` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `operator()` **(Many-Argument Workhorses)** (Impact: 90.7)
  * `FilterEngine__proceed` **(Many-Argument Workhorses)** (Impact: 79.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 615 instances
* *State Mutation (weighted view):* 2112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 193`, `args: 258`, `func_start: 85`, `class_start: 29`
* *Risk/State:* `state_mutation: 882`, `dead_code: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 7`, `immutability_locks: 236`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.00014 | `Ripple Effect (Closeness):` 0.00239
  * `Imports (Out-Degree: 7):` cstddef, filter.hpp, intrin.hpp, precomp.hpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/imgwarp.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_8: 7.429, file_cluster_6: 10.296, file_cluster_4: 18.635
- **Magnitude:** 3630.58 | **LOC:** 3324 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **7**; blast radius 0.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remapBilinear` **(Many-Argument Workhorses)** (Impact: 314.5)
    * *Intent:* #endif
  * `cv::convertMaps` **(Many-Argument Workhorses)** (Impact: 216.3)
  * `remapLanczos4` **(Many-Argument Workhorses)** (Impact: 125.5)
  * `ocl_warpTransform` **(Many-Argument Workhorses)** (Impact: 122.2)
  * `cv::remap` **(Many-Argument Workhorses)** (Impact: 115.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 490 instances
* *State Mutation (weighted view):* 1697
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 144`, `args: 211`, `func_start: 54`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 717`, `dead_code: 1`, `planned_debt: 9`, `unreferenced_by_name: 12`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `doc: 6`, `immutability_locks: 259`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.000221 | `Ripple Effect (Closeness):` 0.005597
  * `Imports (Out-Degree: 20):` hal_replacement.hpp, imgwarp.hpp, opencl_kernels_imgproc.hpp, intrin.hpp, softfloat.hpp, configuration.private.hpp, precomp.hpp
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/smooth.simd.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.919)
- **Top Global Matches:** file_cluster_8: 6.919, file_cluster_6: 17.264, file_cluster_3: 20.137
- **Magnitude:** 3622.56 | **LOC:** 2736 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.075; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fixedSmoothInvoker` **(Many-Argument Workhorses)** (Impact: 275.4)
  * `hlineSmooth5N14641` **(Many-Argument Workhorses)** (Impact: 89.3)
  * `hlineSmooth5Nabcba` **(Many-Argument Workhorses)** (Impact: 83.2)
  * `hlineSmooth5N` **(Many-Argument Workhorses)** (Impact: 83.1)
  * `operator()` **(Compute Cores)** (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 764 instances
* *State Mutation (weighted view):* 2495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 196`, `args: 48`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 967`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `doc: 1`, `immutability_locks: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000703
  * `Imports (Out-Degree: 8):` filter.hpp, fixedpoint.inl.hpp, intrin.hpp, softfloat.hpp, precomp.hpp, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hal/riscv-rvv/src/imgproc/color.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_15: 7.624, file_cluster_16: 9.096, file_cluster_11: 9.183
- **Magnitude:** 3572.34 | **LOC:** 3160 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cvtBGRtoLab_f` **(Many-Argument Workhorses)** (Impact: 51.4)
  * `cvtBGRtoMultiPlaneYUV` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* // the algorithm is copied from imgproc/src/color_yuv.simd.cpp, // in the functor struct RGB8toYUV42...
  * `cvtBGRtoLab` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `cvtMultiPlaneYUVtoBGR` **(Many-Argument Workhorses)** (Impact: 45.7)
    * *Intent:* // the algorithm is copied from imgproc/src/color_yuv.simd.cpp, // in the functor struct YUV420sp2RG...
  * `Tab` **(I/O & Config Routines)** (Impact: 39.2)
    * *Intent:* // the algorithm is copied from imgproc/src/color_lab.cpp, // in the function static bool createLabT...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 522 instances
* *State Mutation (weighted view):* 1890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 940`, `args: 265`, `func_start: 236`, `class_start: 35`
* *Risk/State:* `state_mutation: 846`, `duplicate_logic: 148`, `unreferenced_by_name: 13`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` limits, rvv_hal.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/test/test_math.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.051)
- **Top Global Matches:** file_cluster_4: 7.051, file_cluster_15: 9.257, file_cluster_16: 10.571
- **Magnitude:** 3567.24 | **LOC:** 4234 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (41.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.5%), Dead Code Surface (formerly Dead Code) (8.7%)
- **Documentation Coverage:** 97.7654% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Core_PowTest::prepare_to_validation` **(Compute Cores)** (Impact: 107.4)
  * `cvTsPerspectiveTransform` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `cvTsLU` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* // LU method that chooses the optimal in a column pivot element
  * `Core_SolvePolyTest::run` **(Compute Cores)** (Impact: 59.2)
  * `Core_SVDTest::get_test_array_types_and_sizes` **(Many-Argument Workhorses)** (Impact: 47.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 629 instances
* *State Mutation (weighted view):* 2032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 228`, `args: 320`, `func_start: 179`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 774`, `dead_code: 12`, `planned_debt: 1`, `unreferenced_by_name: 121`
* *Architecture:* `api: 21`, `import: 4`
* *Defense:* `doc: 27`, `test: 300`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` float.h, math.h, softfloat.hpp, test_precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `modules/core/misc/objc/common/CvType.h` (OBJECTIVE-C) | Magnitude: 18.16 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: explicit_casts: 15, doc: 8, args: 7, func_start: 7
- `modules/dnn/misc/java/test/DnnForwardAndRetrieve.java` (JAVA) | Magnitude: 9.46 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 18, import: 10, core_var_decl: 10
- `modules/core/misc/objc/common/Mat.mm` (OBJECTIVE-C) | Magnitude: 832.26 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 556, explicit_casts: 296, pointers: 175, core_var_decl: 141
- `hal/carotene/src/add_weighted.cpp` (CPP) | Magnitude: 70.66 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 142, structural_boundaries: 82, immutability_locks: 42, core_var_decl: 35
- `modules/core/include/opencv2/core/eigen.hpp` (CPP) | Magnitude: 148.58 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 203, structural_boundaries: 64, scientific: 48, branch: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `modules/features2d/test/ocl/test_feature2d.cpp` (CPP) | Magnitude: 17.94 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, args: 7, structural_boundaries: 6, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `modules/core/src/ovx.cpp` (CPP) | Magnitude: 36.52 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 10, core_var_decl: 9, branch: 8
- `modules/gapi/test/internal/gapi_transactions_test.cpp` (CPP) | Magnitude: 82.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 175, test: 72, structural_boundaries: 43, explicit_casts: 36
- `modules/gapi/src/api/garray.cpp` (CPP) | Magnitude: 18.46 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, func_start: 8, structural_boundaries: 6, args: 6
- `modules/imgproc/misc/java/src/java/imgproc+Moments.java` (JAVA) | Magnitude: 307.78 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 211, state_mutation: 89, api: 79, args: 54
- `modules/videoio/src/cap_mfx_common.cpp` (CPP) | Magnitude: 96.34 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 125, pointers: 28, structural_boundaries: 27, core_var_decl: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `modules/videoio/src/cap_mfx_reader.hpp` (CPP) | Magnitude: 16.64 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, pointers: 8, class_start: 7
- `modules/core/misc/objc/common/Double2.mm` (OBJECTIVE-C) | Magnitude: 64.72 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 29, explicit_casts: 16, structural_boundaries: 12, branch: 11
- `modules/objdetect/include/opencv2/objdetect/detection_based_tracker.hpp` (CPP) | Magnitude: 39.52 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 43, immutability_locks: 20, func_start: 13
- `modules/core/include/opencv2/core/async.hpp` (CPP) | Magnitude: 25.78 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 27, immutability_locks: 11, args: 10
- `modules/gapi/src/streaming/onevpl/accelerators/surface/dx11_frame_adapter.cpp` (CPP) | Magnitude: 72.7 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 125, branch: 30, structural_boundaries: 30, pointers: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `modules/imgcodecs/test/test_bmp.cpp` (CPP) | Magnitude: 10.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, test: 10, args: 4, state_mutation: 4
- `modules/ml/test/test_lr.cpp` (CPP) | Magnitude: 13.12 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 47, pointers: 22, test: 13, core_var_decl: 13
- `modules/features2d/test/test_detectors_regression.cpp` (CPP) | Magnitude: 23.42 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, args: 12, func_start: 11, test: 11
- `modules/photo/test/test_decolor.cpp` (CPP) | Magnitude: 3.18 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 7, design_snake_case: 7, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `samples/dnn/dnn_model_runner/dnn_conversion/common/abstract_model.py` (PYTHON) | Magnitude: 13.1 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, api: 5, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `samples/java/tutorial_code/features2D/feature_homography/SURFFLANNMatchingHomographyDemo.java` (JAVA) | Magnitude: 44.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 56, core_var_decl: 29, import: 20
- `modules/video/src/tracking/detail/tracker_sampler.cpp` (CPP) | Magnitude: 27.96 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, func_start: 7, state_mutation: 7
- `modules/ts/include/opencv2/ts/ts_gtest.h` (CPP) | Magnitude: 3491.8 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11012, structural_boundaries: 9354, immutability_locks: 3247, explicit_casts: 1451
- `modules/core/perf/perf_allocation.cpp` (CPP) | Magnitude: 19.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 4, immutability_locks: 4, core_var_decl: 4
- `modules/imgproc/perf/opencl/perf_filters.cpp` (CPP) | Magnitude: 60.34 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 171, core_var_decl: 51, immutability_locks: 49, design_snake_case: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `samples/java/tutorial_code/ImgTrans/canny_detector/CannyDetectorDemo.java` (JAVA) | Magnitude: 48.3 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 43, import: 19, core_var_decl: 19
- `samples/java/tutorial_code/TrackingMotion/generic_corner_detector/CornerDetectorDemo.java` (JAVA) | Magnitude: 92.88 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 61, core_var_decl: 44, state_mutation: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `modules/dnn/src/cuda4dnn/primitives/depth_space_ops.hpp` (CPP) | Magnitude: 23.0 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, pointers: 17, structural_boundaries: 16, core_var_decl: 12
- `modules/gapi/src/api/kernels_ot.cpp` (CPP) | Magnitude: 6.28 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, immutability_locks: 6, structural_boundaries: 5, import: 3
- `hal/openvx/include/ivx_lib_debug.hpp` (CPP) | Magnitude: 4.78 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, macros: 3, func_start: 2, immutability_locks: 2
- `modules/imgproc/perf/perf_histogram.cpp` (CPP) | Magnitude: 11.82 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 100, args: 23, core_var_decl: 21, design_snake_case: 15
- `modules/dnn/src/opencl/pooling.cl` (C) | Magnitude: 94.62 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 36, design_snake_case: 36, immutability_locks: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `modules/core/perf/perf_io_base64.cpp` (CPP) | Magnitude: 5.6 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 54, args: 12, core_var_decl: 12, design_snake_case: 12
- `modules/core/test/test_lpsolver.cpp` (CPP) | Magnitude: 37.44 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 69, core_var_decl: 26, args: 24, explicit_casts: 22
- `samples/winrt/ImageManipulations/pch.h` (CPP) | Magnitude: 13.64 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 6, macros: 1
- `modules/gapi/include/opencv2/gapi/own/exports.hpp` (CPP) | Magnitude: 15.58 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 4, reflection_metaprogramming: 1
- `modules/photo/perf/opencl/perf_denoising.cpp` (CPP) | Magnitude: 27.54 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 10, design_snake_case: 10, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `modules/imgproc/src/min_enclosing_convex_polygon.cpp` (CPP) | Magnitude: 632.72 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 551, state_mutation: 129, core_var_decl: 129, design_snake_case: 128
- `modules/dnn/src/net_impl.cpp` (CPP) | Magnitude: 1884.42 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1751, branch: 542, core_var_decl: 408, state_mutation: 296
- `modules/videoio/src/cap_mfx_common.hpp` (CPP) | Magnitude: 135.9 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 83, branch: 37, args: 36
- `samples/cpp/tutorial_code/calib3d/real_time_pose_estimation/src/Utils.cpp` (CPP) | Magnitude: 234.18 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 219, core_var_decl: 99, design_snake_case: 90, state_mutation: 50
- `modules/videoio/src/cap_images.cpp` (CPP) | Magnitude: 277.54 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 267, branch: 60, state_mutation: 51, structural_boundaries: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `modules/core/misc/objc/common/DMatch.h` (OBJECTIVE-C) | Magnitude: 27.78 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: explicit_casts: 18, api: 14, doc: 10, func_start: 9
- `samples/android/tutorial-3-cameracontrol/src/org/opencv/samples/tutorial3/Tutorial3View.java` (JAVA) | Magnitude: 52.62 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 37, import: 19, args: 12
- `modules/core/src/precomp.hpp` (CPP) | Magnitude: 105.54 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 166, indent_spaces: 114, immutability_locks: 55, macros: 41
- `samples/android/tutorial-3-cameracontrol/src/org/opencv/samples/tutorial3/Tutorial3Activity.java` (JAVA) | Magnitude: 100.94 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 54, import: 28, core_var_decl: 24
- `modules/core/misc/java/src/java/core+MatOfByte.java` (JAVA) | Magnitude: 66.82 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 27, branch: 13, api: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `modules/dnn/src/int8layers/convolution_layer.cpp` (CPP) | Magnitude: 1509.74 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1274, core_var_decl: 412, state_mutation: 392, design_snake_case: 328

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `samples/cpp/tutorial_code/TrackingMotion/cornerDetector_Demo.cpp` (CPP) | Magnitude: 63.8 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, core_var_decl: 20, structural_boundaries: 14, state_mutation: 13
- `platforms/android/build_aar.sh` (SHELL) | Magnitude: 19.38 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 22, debug_prints: 13, core_var_decl: 9, design_upper_case: 9
- `modules/core/src/buffer_area.cpp` (CPP) | Magnitude: 101.5 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 26, pointers: 26, branch: 19
- `modules/videoio/src/plugin_writer_api.hpp` (CPP) | Magnitude: 16.28 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 19, indent_spaces: 19, structural_boundaries: 18, doc: 14
- `modules/core/perf/perf_umat.cpp` (CPP) | Magnitude: 6.3 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, core_var_decl: 11, structural_boundaries: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `modules/features2d/src/agast.cpp` (CPP) | Magnitude: 11746.16 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 8007, branch: 5369, structural_boundaries: 1710, core_var_decl: 168
- `modules/core/src/matrix_transform.cpp` (CPP) | Magnitude: 1194.62 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 756, state_mutation: 248, core_var_decl: 222, design_snake_case: 210

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `modules/video/misc/python/test/test_lk_homography.py` (PYTHON) | Magnitude: 92.82 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 33, core_var_decl: 31, design_snake_case: 20
- `samples/cpp/convexhull.cpp` (CPP) | Magnitude: 47.3 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 9, branch: 8, structural_boundaries: 7
- `modules/videoio/src/cap_xine.cpp` (CPP) | Magnitude: 201.94 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 245, branch: 64, structural_boundaries: 42, state_mutation: 25
- `modules/features2d/test/ocl/test_brute_force_matcher.cpp` (CPP) | Magnitude: 96.82 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 92, core_var_decl: 25, branch: 20, state_mutation: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `modules/dnn/src/onnx/onnx_importer.cpp` -> Churn: **87.21%** | Cog Load: 68.5215% | Debt: 17.2283%
- `modules/videoio/src/cap_msmf.cpp` -> Churn: **74.2%** | Cog Load: 72.907% | Debt: 45.8066%
- `hal/ipp/src/warp_ipp.cpp` -> Churn: **69.4%** | Cog Load: 54.6036% | Debt: 19.4283%
- `modules/objdetect/src/aruco/aruco_detector.cpp` -> Churn: **65.07%** | Cog Load: 61.9439% | Debt: 65.1355%
- `modules/core/src/system.cpp` -> Churn: **62.74%** | Cog Load: 74.5804% | Debt: 85.5425%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `modules/imgproc/src/smooth.simd.hpp` -> **Madan mohan Manokar** (100.0% isolated ownership) | Magnitude: 3622.56
- `modules/core/src/arithm.cpp` -> **Alexander Smorkalov** (100.0% isolated ownership) | Magnitude: 2730.16
- `modules/calib3d/src/usac/ransac_solvers.cpp` -> **Vincent Rabaud** (100.0% isolated ownership) | Magnitude: 2464.14
- `modules/java/generator/gen_java.py` -> **Alexander Smorkalov** (100.0% isolated ownership) | Magnitude: 2381.6
- `modules/videoio/src/cap_dshow.cpp` -> **satyam yadav** (100.0% isolated ownership) | Magnitude: 2252.9

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `modules/imgproc/src/drawing.cpp` -> **Severity: 1.171** (Bridge: 0.0117 * Flux: 100.0%)
- `modules/imgproc/src/histogram.cpp` -> **Severity: 1.059** (Bridge: 0.0106 * Flux: 100.0%)
- `modules/core/misc/objc/common/Mat.mm` -> **Severity: 1.048** (Bridge: 0.0105 * Flux: 100.0%)
- `modules/core/src/system.cpp` -> **Severity: 1.047** (Bridge: 0.0105 * Flux: 99.9611%)
- `modules/core/include/opencv2/core/utility.hpp` -> **Severity: 0.95** (Bridge: 0.0095 * Flux: 99.4814%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `modules/core/include/opencv2/core/utility.hpp` -> **Severity: 14.528** (Embedded: 0.2192 * Error Risk: 66.2767%)
- `modules/core/include/opencv2/core/hal/hal.hpp` -> **Severity: 14.227** (Embedded: 0.1564 * Error Risk: 90.9736%)
- `modules/core/src/system.cpp` -> **Severity: 13.431** (Embedded: 0.2016 * Error Risk: 66.6281%)
- `modules/core/src/matrix.cpp` -> **Severity: 13.214** (Embedded: 0.1702 * Error Risk: 77.6356%)
- `modules/core/include/opencv2/core/base.hpp` -> **Severity: 13.161** (Embedded: 0.2001 * Error Risk: 65.7761%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `modules/core/include/opencv2/core/cvdef.h` -> **Severity: 3203.52** (Blast Radius: 40.044 * Doc Risk: 80.0%)
- `modules/python/package/cv2/__init__.py` -> **Severity: 1406.2** (Blast Radius: 14.062 * Doc Risk: 100.0%)
- `modules/core/include/opencv2/core/base.hpp` -> **Severity: 1141.884** (Blast Radius: 15.497 * Doc Risk: 73.6842%)
- `modules/core/include/opencv2/core/cvstd.hpp` -> **Severity: 1128.7** (Blast Radius: 11.287 * Doc Risk: 100.0%)
- `modules/core/include/opencv2/core/utility.hpp` -> **Severity: 1103.492** (Blast Radius: 14.814 * Doc Risk: 74.4898%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3228 literal sites + 21 sites through wrappers = 3249
- **`memory_alloc`:** 2214 literal sites + 411 sites through wrappers = 2625
- **`panics_and_aborts`:** 1991 literal sites + 2 sites through wrappers = 1993

- `CV_OCL_RUN` (macro, memory_alloc, via CV_OCL_RUN_): 75 call sites in 52 files -- `modules/core/include/opencv2/core/opencl/ocl_defs.hpp`
- `getWindowMutex` (function, memory_alloc, primitive): 46 call sites in 3 files -- `modules/highgui/src/window.cpp`
- `CV_IMPL_ADD` (macro, memory_alloc, via useCollection): 45 call sites in 15 files -- `modules/core/include/opencv2/core/utils/instrumentation.hpp`
- `CV_LOCK_MUTEX` (macro, memory_alloc, via getWindowMutex): 24 call sites in 1 files -- `modules/highgui/src/window_gtk.cpp`
- `setIppErrorStatus` (macro, memory_alloc, via setIppStatus): 24 call sites in 7 files -- `modules/core/include/opencv2/core/private.hpp`
- `CHK` (macro, memory_alloc, primitive): 22 call sites in 3 files -- `modules/videoio/src/cap_winrt/MFIncludes.hpp`
- `cvGetWindow` (function, memory_alloc, primitive): 22 call sites in 1 files -- `modules/highgui/src/window_cocoa.mm`
- `_VerifyNotShutdown` (function, memory_alloc, via CHK): 18 call sites in 1 files -- `modules/videoio/src/cap_winrt/MediaSink.hpp`
- `getImplData` (function, memory_alloc, primitive): 18 call sites in 1 files -- `modules/core/src/system.cpp`
- `getIPPSingleton` (function, memory_alloc, primitive): 16 call sites in 1 files -- `modules/core/src/system.cpp`
- `getCoreTlsData` (function, memory_alloc, via getCoreTlsDataTLS): 8 call sites in 3 files -- `modules/core/src/system.cpp`
- `CV_OCL_RUN_` (macro, memory_alloc, via CV_IMPL_ADD): 7 call sites in 5 files -- `modules/core/include/opencv2/core/opencl/ocl_defs.hpp`
*(+62 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 217926 call pairs -- scoped 17.4%, unique 5.4%, ambiguous 38.0%, external 39.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 185351 | 16.8% | 6.1% | 42.1% | 35.1% |
| python | 14042 | 16.5% | 0.0% | 9.6% | 73.9% |
| java | 9837 | 31.8% | 0.4% | 24.9% | 42.9% |
| swift | 2834 | 5.3% | 10.5% | 6.7% | 77.6% |
| objective-c | 2713 | 29.0% | 3.7% | 21.2% | 46.0% |
| c | 1962 | 5.1% | 2.2% | 11.6% | 81.1% |
| javascript | 759 | 32.7% | 0.0% | 0.0% | 67.3% |
| shell | 157 | 15.9% | 0.0% | 0.0% | 84.1% |
| kotlin | 81 | 3.7% | 11.1% | 22.2% | 63.0% |
| html | 76 | 10.5% | 0.0% | 0.0% | 89.5% |

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
