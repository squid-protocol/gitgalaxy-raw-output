# ARCHITECTURAL_BRIEF: opencv
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/opencv` |
| **Timestamp** | `2026-08-07T05:20:18.244278+00:00` |
| **Scan Duration** | `30.19s` |
| **Git Branch** | `4.x` |
| **Git Commit** | `69bdcc93861cda196df935dd2975e6f1384ceced` |
| **Git Remote** | `https://github.com/opencv/opencv.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4318 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Total Artifacts | 7688 |
| Analyzed Artifacts (Scanned) | 4789 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2899 |
| Total LOC | 1024032 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 62.3% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8124 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1675 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1307 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 337 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 2927 | 722181 | 61.1% |
| C | 712 | 197723 | 14.9% |
| PYTHON | 287 | 32443 | 6.0% |
| PLAINTEXT | 177 | 6 | 3.7% |
| JAVA | 142 | 15682 | 3.0% |
| OBJECTIVE-C | 124 | 10132 | 2.6% |
| ASSEMBLY | 95 | 28962 | 2.0% |
| MARKDOWN | 79 | 0 | 1.6% |
| XML | 57 | 0 | 1.2% |
| JSON | 27 | 2368 | 0.6% |
| JAVASCRIPT | 23 | 3065 | 0.5% |
| HTML | 21 | 1445 | 0.4% |
| SHELL | 20 | 844 | 0.4% |
| M4 | 18 | 1015 | 0.4% |
| SWIFT | 12 | 1074 | 0.3% |
| CSHARP | 12 | 442 | 0.3% |
| YAML | 11 | 1006 | 0.2% |
| PROTO | 10 | 718 | 0.2% |
| BATCH | 9 | 581 | 0.2% |
| GLSL | 6 | 701 | 0.1% |
| MAKEFILE | 4 | 104 | 0.1% |
| SCALA | 4 | 72 | 0.1% |
| KOTLIN | 3 | 145 | 0.1% |
| POWERSHELL | 2 | 249 | 0.0% |
| PERL | 2 | 496 | 0.0% |
| CSS | 2 | 183 | 0.0% |
| DOCKERFILE | 1 | 11 | 0.0% |
| GROOVY | 1 | 16 | 0.0% |
| PBTXT | 1 | 2368 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.408`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2823 | 58.9% |
| file_cluster_13 | 1319 | 27.5% |
| file_cluster_9 | 148 | 3.1% |
| file_cluster_16 | 87 | 1.8% |
| file_cluster_12 | 41 | 0.9% |
| file_cluster_4 | 31 | 0.6% |
| file_cluster_7 | 30 | 0.6% |
| file_cluster_11 | 28 | 0.6% |
| file_cluster_17 | 13 | 0.3% |
| file_cluster_0 | 12 | 0.3% |
| Unknown | 6 | 0.1% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 250 | 5.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2899*

**Composition by Extension & Reason:**
- `.jpg`: 579x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.png`: 443x Excluded (Explicitly Denied Extension: '.png')
- `.cpp`: 366x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 20 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 2204 commas in 662 LOC)
- `.markdown`: 272x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 173x Excluded (Unsupported Extension: '.cmake'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.cmake)
- `.c`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 3538 hex tokens in 518 LOC), 1x Excluded (Embedded Array/Matrix Payload: 65538 commas in 4135 LOC)
- `.h`: 72x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4666 LOC), 1x Excluded (Machine-Generated Source Code Signature: 180 LOC)
- `.py`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 259 LOC)
- `.hpp`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4496 LOC), 1x Excluded (Embedded Array/Matrix Payload: 14225 commas in 2019 LOC)
- `.html`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Documentation Signature)
- `.xml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1506 LOC), 1x Excluded (Massive Static Asset Blob: 12214 LOC)
- `no_extension`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 7x Excluded (Unsupported Extension: '.appxmanifest')
- `.java`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 43x Excluded (Unsupported Extension: '.patch'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 40.4 | 37.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 68.1 | 82.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 40.9 | 21.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.2 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.4 | 3.1 | 0.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 70.9 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 96.9 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.8 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.9 | 15.8 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `platforms/android/build_sdk.py` (Hits: 119)
- `platforms/ios/build_framework.py` (Hits: 108)
- `modules/objc/generator/gen_objc.py` (Hits: 80)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **string.h** (`3rdparty/flatbuffers/include/flatbuffers/string.h`) — 320 inbound connections
2. **vector.h** (`3rdparty/flatbuffers/include/flatbuffers/vector.h`) — 268 inbound connections
3. **algorithm.cpp** (`modules/core/src/algorithm.cpp`) — 174 inbound connections
4. **ImfNamespace.h** (`3rdparty/openexr/IlmImf/ImfNamespace.h`) — 154 inbound connections
5. **jpeglib.h** (`3rdparty/libjpeg-turbo/src/jpeglib.h`) — 111 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ts_gtest.cpp** (`modules/ts/src/ts_gtest.cpp`) — 63 outbound dependencies
2. **system.cpp** (`modules/core/src/system.cpp`) — 46 outbound dependencies
3. **opj_includes.h** (`3rdparty/openjpeg/openjp2/opj_includes.h`) — 42 outbound dependencies
4. **descriptor.cc** (`3rdparty/protobuf/src/google/protobuf/descriptor.cc`) — 36 outbound dependencies
5. **parallel.cpp** (`modules/core/src/parallel.cpp`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `AGAST_7_12s` (@ `modules/features2d/src/agast.cpp`) -> Impact: **2046.0** | LOC: 1040
- `AGAST_7_12d` (@ `modules/features2d/src/agast.cpp`) -> Impact: **2007.0** | LOC: 1021
- `OAST_9_16` (@ `modules/features2d/src/agast.cpp`) -> Impact: **2006.5** | LOC: 1089
- `AGAST_5_8` (@ `modules/features2d/src/agast.cpp`) -> Impact: **1400.1** | LOC: 762
- `cv::fisheye::undistortPoints` (@ `modules/calib3d/src/fisheye.cpp`) -> Impact: **899.7** | LOC: 1306
- `DescriptorBuilder::BuildFieldOrExtension` (@ `3rdparty/protobuf/src/google/protobuf/descriptor.cc`) -> Impact: **886.5** | LOC: 1451
- `ovx_hal_mul` (@ `hal/openvx/hal/openvx_hal.cpp`) -> Impact: **857.3** | LOC: 892
- `CvCaptureCAM_XIMEA::getProperty` (@ `modules/videoio/src/cap_ximea.cpp`) -> Impact: **734.2** | LOC: 642
  * *Intent:* /**********************************************************************************/
- `throwErrnoExc` (@ `3rdparty/openexr/Iex/IexThrowErrnoExc.cpp`) -> Impact: **594.6** | LOC: 807
  * *Intent:* // Exceptions that correspond to "errno" error codes, // and a function to make throwing those exceptions easy. // //---------------------------------...
- `stereoCalibrateImpl` (@ `modules/calib3d/src/calibration.cpp`) -> Impact: **592.7** | LOC: 521

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `modules/core/src` | 109 | 191574.31 | 54.57% | 54.73% |
| `modules/imgproc/src` | 102 | 123626.54 | 46.28% | 40.21% |
| `modules/calib3d/src` | 47 | 46180.88 | 43.34% | 36.28% |
| `hal/carotene/src` | 57 | 42388.04 | 64.22% | 50.8% |
| `modules/videoio/src` | 63 | 30599.12 | 52.39% | 61.61% |
| `modules/dnn/src/layers` | 57 | 29712.1 | 58.63% | 33.01% |
| `3rdparty/libjasper` | 63 | 29566.18 | 35.69% | 26.23% |
| `3rdparty/libwebp/src/dsp` | 76 | 26072.55 | 64.31% | 4.54% |
| `3rdparty/openexr/IlmImf` | 200 | 25812.1 | 17.17% | 47.48% |
| `3rdparty/openjpeg/openjp2` | 66 | 24024.7 | 28.62% | 35.86% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `3rdparty/libjasper/jas_version.c` -> **100.0%** Exposure
- `3rdparty/libtiff/tif_version.c` -> **100.0%** Exposure
- `3rdparty/libtiff/tiffconf.h.cmake.in` -> **100.0%** Exposure
- `3rdparty/openjpeg/openjp2/j2k.h` -> **100.0%** Exposure
- `3rdparty/openjpeg/openjp2/jp2.h` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `3rdparty/cpufeatures/cpu-features.c` -> **100.0%** Exposure
- `3rdparty/cpufeatures/cpu-features.h` -> **100.0%** Exposure
- `3rdparty/ittnotify/src/ittnotify/jitprofiling.c` -> **100.0%** Exposure
- `3rdparty/libjasper/jas_cm.c` -> **100.0%** Exposure
- `3rdparty/libjasper/jas_debug.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `hal/carotene/src/vtransform.hpp` -> **0** Orphaned Functions | **367** Duplicates
- `modules/core/include/opencv2/core/hal/intrin_rvv071.hpp` -> **0** Orphaned Functions | **357** Duplicates
- `modules/core/include/opencv2/core/hal/intrin_avx512.hpp` -> **0** Orphaned Functions | **350** Duplicates
- `modules/core/include/opencv2/core/hal/intrin_lasx.hpp` -> **0** Orphaned Functions | **342** Duplicates
- `modules/core/include/opencv2/core/hal/intrin_avx.hpp` -> **0** Orphaned Functions | **334** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`3rdparty/libjasper/jas_cm.c`** -> AI Confidence: **99.48%**
2. **`3rdparty/libjasper/jp2_dec.c`** -> AI Confidence: **99.48%**
3. **`3rdparty/libjasper/jp2_enc.c`** -> AI Confidence: **99.48%**
4. **`3rdparty/libjasper/jpc_enc.c`** -> AI Confidence: **99.48%**
5. **`3rdparty/libjasper/jpc_qmfb.c`** -> AI Confidence: **99.48%**
6. **`3rdparty/libjasper/jpc_t1cod.c`** -> AI Confidence: **99.48%**
7. **`3rdparty/libjasper/jpc_t1dec.c`** -> AI Confidence: **99.48%**
8. **`3rdparty/libjasper/jpc_t1enc.c`** -> AI Confidence: **99.48%**
9. **`3rdparty/libjasper/jpc_t2enc.c`** -> AI Confidence: **99.48%**
10. **`3rdparty/libjpeg-turbo/simd/arm/aarch64/jchuff-neon.c`** -> AI Confidence: **99.48%**
11. **`3rdparty/libjpeg-turbo/simd/arm/jccolor-neon.c`** -> AI Confidence: **99.48%**
12. **`3rdparty/libjpeg-turbo/simd/arm/jcphuff-neon.c`** -> AI Confidence: **99.48%**
13. **`3rdparty/libjpeg-turbo/simd/arm/jcsample-neon.c`** -> AI Confidence: **99.48%**
14. **`3rdparty/libjpeg-turbo/simd/arm/jidctred-neon.c`** -> AI Confidence: **99.48%**
15. **`3rdparty/libjpeg-turbo/src/jcphuff.c`** -> AI Confidence: **99.48%**
16. **`3rdparty/libjpeg-turbo/src/jdapistd.c`** -> AI Confidence: **99.48%**
17. **`3rdparty/libtiff/tif_luv.c`** -> AI Confidence: **99.48%**
18. **`3rdparty/libwebp/src/dec/frame_dec.c`** -> AI Confidence: **99.48%**
19. **`3rdparty/libwebp/src/enc/picture_tools_enc.c`** -> AI Confidence: **99.48%**
20. **`3rdparty/libwebp/src/enc/quant_enc.c`** -> AI Confidence: **99.48%**
21. **`3rdparty/libwebp/src/enc/vp8l_enc.c`** -> AI Confidence: **99.48%**
22. **`3rdparty/libwebp/src/mux/muxread.c`** -> AI Confidence: **99.48%**
23. **`3rdparty/libwebp/src/utils/huffman_encode_utils.c`** -> AI Confidence: **99.48%**
24. **`3rdparty/libwebp/src/utils/rescaler_utils.c`** -> AI Confidence: **99.48%**
25. **`3rdparty/include/opencl/1.2/CL/opencl.h`** -> AI Confidence: **99.48%**
26. **`3rdparty/openexr/IlmImf/ImfDwaCompressor.cpp`** -> AI Confidence: **99.48%**
27. **`3rdparty/openexr/IlmImf/ImfMisc.cpp`** -> AI Confidence: **99.48%**
28. **`3rdparty/protobuf/src/google/protobuf/descriptor.cc`** -> AI Confidence: **99.48%**
29. **`3rdparty/protobuf/src/google/protobuf/reflection_ops.cc`** -> AI Confidence: **99.48%**
30. **`apps/annotation/opencv_annotation.cpp`** -> AI Confidence: **99.48%**
31. **`apps/createsamples/utility.cpp`** -> AI Confidence: **99.48%**
32. **`apps/interactive-calibration/frameProcessor.cpp`** -> AI Confidence: **99.48%**
33. **`modules/calib3d/src/calibinit.cpp`** -> AI Confidence: **99.48%**
34. **`modules/calib3d/src/calibration.cpp`** -> AI Confidence: **99.48%**
35. **`modules/calib3d/src/calibration_base.cpp`** -> AI Confidence: **99.48%**
36. **`modules/calib3d/src/solvepnp.cpp`** -> AI Confidence: **99.48%**
37. **`modules/core/src/directx.cpp`** -> AI Confidence: **99.48%**
38. **`modules/core/src/directx.inc.hpp`** -> AI Confidence: **99.48%**
39. **`modules/core/src/matmul.dispatch.cpp`** -> AI Confidence: **99.48%**
40. **`modules/dnn/src/int8layers/convolution_layer.cpp`** -> AI Confidence: **99.48%**
41. **`modules/dnn/src/int8layers/pooling_layer.cpp`** -> AI Confidence: **99.48%**
42. **`modules/dnn/src/layers/eltwise_layer.cpp`** -> AI Confidence: **99.48%**
43. **`modules/dnn/src/precomp.hpp`** -> AI Confidence: **99.48%**
44. **`modules/dnn/src/tensorflow/tf_importer.cpp`** -> AI Confidence: **99.48%**
45. **`modules/gapi/src/backends/fluid/gfluidcore_simd_sse41.hpp`** -> AI Confidence: **99.48%**
46. **`modules/gapi/src/precomp.hpp`** -> AI Confidence: **99.48%**
47. **`modules/gapi/src/streaming/onevpl/cfg_param_device_selector.cpp`** -> AI Confidence: **99.48%**
48. **`modules/imgcodecs/src/grfmt_avif.cpp`** -> AI Confidence: **99.48%**
49. **`modules/imgcodecs/src/grfmt_exr.cpp`** -> AI Confidence: **99.48%**
50. **`modules/imgcodecs/src/grfmt_jpeg2000.cpp`** -> AI Confidence: **99.48%**
51. **`modules/imgcodecs/src/grfmt_tiff.cpp`** -> AI Confidence: **99.48%**
52. **`modules/imgcodecs/src/grfmt_webp.cpp`** -> AI Confidence: **99.48%**
53. **`modules/imgcodecs/src/precomp.hpp`** -> AI Confidence: **99.48%**
54. **`modules/imgproc/src/imgwarp.cpp`** -> AI Confidence: **99.48%**
55. **`modules/imgproc/src/morph.dispatch.cpp`** -> AI Confidence: **99.48%**
56. **`modules/videoio/src/precomp.hpp`** -> AI Confidence: **99.48%**
57. **`samples/cpp/calibration.cpp`** -> AI Confidence: **99.48%**
58. **`samples/cpp/detect_mser.cpp`** -> AI Confidence: **99.48%**
59. **`samples/cpp/stereo_match.cpp`** -> AI Confidence: **99.48%**
60. **`samples/cpp/stitching_detailed.cpp`** -> AI Confidence: **99.48%**
61. **`samples/cpp/tutorial_code/calib3d/camera_calibration/camera_calibration.cpp`** -> AI Confidence: **99.48%**
62. **`samples/dnn/yolo_detector.cpp`** -> AI Confidence: **99.48%**
63. **`samples/gpu/cascadeclassifier.cpp`** -> AI Confidence: **99.48%**
64. **`samples/gpu/hog.cpp`** -> AI Confidence: **99.48%**
65. **`samples/gpu/stereo_match.cpp`** -> AI Confidence: **99.48%**
66. **`samples/gpu/video_reader.cpp`** -> AI Confidence: **99.48%**
67. **`samples/tapi/bgfg_segm.cpp`** -> AI Confidence: **99.48%**
68. **`samples/tapi/camshift.cpp`** -> AI Confidence: **99.48%**
69. **`modules/core/misc/objc/common/Converters.mm`** -> AI Confidence: **99.48%**
70. **`modules/core/misc/objc/common/Mat.mm`** -> AI Confidence: **99.48%**
71. **`modules/core/misc/objc/common/MatOfRotatedRect.mm`** -> AI Confidence: **99.48%**
72. **`modules/videoio/src/cap_avfoundation.mm`** -> AI Confidence: **99.48%**
73. **`modules/ts/misc/chart.py`** -> AI Confidence: **99.48%**
74. **`modules/ts/misc/report.py`** -> AI Confidence: **99.48%**
75. **`modules/ts/misc/run.py`** -> AI Confidence: **99.48%**
76. **`modules/ts/misc/summary.py`** -> AI Confidence: **99.48%**
77. **`modules/core/include/opencv2/core/cv_cpu_dispatch.h`** -> AI Confidence: **99.44%**
78. **`3rdparty/libjpeg-turbo/simd/powerpc/jsimd_altivec.h`** -> AI Confidence: **99.43%**
79. **`modules/java/generator/src/cpp/common.h`** -> AI Confidence: **99.43%**
80. **`hal/riscv-rvv/rvv_hal.hpp`** -> AI Confidence: **99.42%**
81. **`3rdparty/cpufeatures/cpu-features.c`** -> AI Confidence: **99.39%**
82. **`3rdparty/ittnotify/src/ittnotify/ittnotify_static.c`** -> AI Confidence: **99.39%**
83. **`3rdparty/libjasper/jas_icc.c`** -> AI Confidence: **99.39%**
84. **`3rdparty/libjasper/jas_image.c`** -> AI Confidence: **99.39%**
85. **`3rdparty/libjasper/jpc_mqenc.c`** -> AI Confidence: **99.39%**
86. **`3rdparty/libjasper/jpc_t2dec.c`** -> AI Confidence: **99.39%**
87. **`3rdparty/libjasper/jpc_util.c`** -> AI Confidence: **99.39%**
88. **`3rdparty/libjpeg-turbo/simd/arm/aarch32/jchuff-neon.c`** -> AI Confidence: **99.39%**
89. **`3rdparty/libjpeg-turbo/simd/arm/jidctfst-neon.c`** -> AI Confidence: **99.39%**
90. **`3rdparty/libjpeg-turbo/simd/arm/jquanti-neon.c`** -> AI Confidence: **99.39%**
91. **`3rdparty/libwebp/src/dec/alpha_dec.c`** -> AI Confidence: **99.39%**
92. **`3rdparty/libwebp/src/dec/io_dec.c`** -> AI Confidence: **99.39%**
93. **`3rdparty/libwebp/src/dsp/lossless_avx2.c`** -> AI Confidence: **99.39%**
94. **`3rdparty/libwebp/src/dsp/lossless_enc_avx2.c`** -> AI Confidence: **99.39%**
95. **`3rdparty/libwebp/src/dsp/lossless_enc_sse2.c`** -> AI Confidence: **99.39%**
96. **`3rdparty/libwebp/src/dsp/rescaler_sse2.c`** -> AI Confidence: **99.39%**
97. **`3rdparty/libwebp/src/enc/analysis_enc.c`** -> AI Confidence: **99.39%**
98. **`3rdparty/libwebp/src/enc/backward_references_cost_enc.c`** -> AI Confidence: **99.39%**
99. **`3rdparty/libwebp/src/enc/backward_references_enc.c`** -> AI Confidence: **99.39%**
100. **`3rdparty/libwebp/src/enc/filter_enc.c`** -> AI Confidence: **99.39%**
101. **`3rdparty/libwebp/src/enc/frame_enc.c`** -> AI Confidence: **99.39%**
102. **`3rdparty/libwebp/src/enc/histogram_enc.c`** -> AI Confidence: **99.39%**
103. **`3rdparty/libwebp/src/enc/picture_psnr_enc.c`** -> AI Confidence: **99.39%**
104. **`3rdparty/libwebp/src/enc/predictor_enc.c`** -> AI Confidence: **99.39%**
105. **`3rdparty/libwebp/src/enc/webp_enc.c`** -> AI Confidence: **99.39%**
106. **`3rdparty/flatbuffers/include/flatbuffers/base.h`** -> AI Confidence: **99.39%**
107. **`3rdparty/libjasper/jasper/jas_types.h`** -> AI Confidence: **99.39%**
108. **`3rdparty/openexr/IlmImf/ImfB44Compressor.cpp`** -> AI Confidence: **99.39%**
109. **`3rdparty/openexr/IlmImf/ImfDeepScanLineInputFile.cpp`** -> AI Confidence: **99.39%**
110. **`3rdparty/openexr/IlmImf/ImfDeepTiledOutputFile.cpp`** -> AI Confidence: **99.39%**
111. **`3rdparty/openexr/IlmImf/ImfGenericOutputFile.cpp`** -> AI Confidence: **99.39%**
112. **`3rdparty/openexr/IlmImf/ImfMultiPartInputFile.cpp`** -> AI Confidence: **99.39%**
113. **`3rdparty/openexr/IlmImf/ImfPizCompressor.cpp`** -> AI Confidence: **99.39%**
114. **`3rdparty/openexr/IlmImf/ImfTiledMisc.cpp`** -> AI Confidence: **99.39%**
115. **`3rdparty/openexr/IlmImf/ImfZip.cpp`** -> AI Confidence: **99.39%**
116. **`3rdparty/protobuf/src/google/protobuf/io/tokenizer.cc`** -> AI Confidence: **99.39%**
117. **`3rdparty/protobuf/src/google/protobuf/stubs/int128.cc`** -> AI Confidence: **99.39%**
118. **`3rdparty/protobuf/src/google/protobuf/stubs/strutil.cc`** -> AI Confidence: **99.39%**
119. **`3rdparty/protobuf/src/google/protobuf/text_format.cc`** -> AI Confidence: **99.39%**
120. **`3rdparty/protobuf/src/google/protobuf/wire_format.cc`** -> AI Confidence: **99.39%**
121. **`apps/interactive-calibration/calibController.cpp`** -> AI Confidence: **99.39%**
122. **`apps/visualisation/opencv_visualisation.cpp`** -> AI Confidence: **99.39%**
123. **`modules/calib3d/src/stereobm.cpp`** -> AI Confidence: **99.39%**
124. **`modules/core/src/mathfuncs.cpp`** -> AI Confidence: **99.39%**
125. **`modules/core/src/persistence.cpp`** -> AI Confidence: **99.39%**
126. **`modules/core/src/system.cpp`** -> AI Confidence: **99.39%**
127. **`modules/core/src/utils/datafile.cpp`** -> AI Confidence: **99.39%**
128. **`modules/core/src/utils/filesystem.cpp`** -> AI Confidence: **99.39%**
129. **`modules/core/src/va_intel.cpp`** -> AI Confidence: **99.39%**
130. **`modules/dnn/src/caffe/caffe_importer.cpp`** -> AI Confidence: **99.39%**
131. **`modules/dnn/src/cuda4dnn/primitives/convolution.hpp`** -> AI Confidence: **99.39%**
132. **`modules/dnn/src/layers/pooling_layer.cpp`** -> AI Confidence: **99.39%**
133. **`modules/dnn/src/op_webnn.cpp`** -> AI Confidence: **99.39%**
134. **`modules/dnn/src/registry.cpp`** -> AI Confidence: **99.39%**
135. **`modules/features2d/src/fast.cpp`** -> AI Confidence: **99.39%**
136. **`modules/features2d/src/kaze/AKAZEFeatures.cpp`** -> AI Confidence: **99.39%**
137. **`modules/gapi/src/backends/fluid/gfluidimgproc_simd_avx2.hpp`** -> AI Confidence: **99.39%**
138. **`modules/gapi/src/streaming/onevpl/engine/decode/decode_engine_legacy.cpp`** -> AI Confidence: **99.39%**
139. **`modules/gapi/src/streaming/onevpl/engine/preproc/preproc_engine.cpp`** -> AI Confidence: **99.39%**
140. **`modules/imgcodecs/src/loadsave.cpp`** -> AI Confidence: **99.39%**
141. **`modules/imgproc/src/featureselect.cpp`** -> AI Confidence: **99.39%**
142. **`modules/imgproc/src/filter.dispatch.cpp`** -> AI Confidence: **99.39%**
143. **`modules/imgproc/src/smooth.dispatch.cpp`** -> AI Confidence: **99.39%**
144. **`modules/objdetect/src/hog.cpp`** -> AI Confidence: **99.39%**
145. **`modules/objdetect/src/qrcode.cpp`** -> AI Confidence: **99.39%**
146. **`modules/ts/src/ts.cpp`** -> AI Confidence: **99.39%**
147. **`modules/ts/src/ts_perf.cpp`** -> AI Confidence: **99.39%**
148. **`modules/video/src/lkpyramid.cpp`** -> AI Confidence: **99.39%**
149. **`modules/videoio/src/cap_android_mediandk.cpp`** -> AI Confidence: **99.39%**
150. **`modules/videoio/src/cap_dc1394_v2.cpp`** -> AI Confidence: **99.39%**
151. **`modules/videoio/src/cap_obsensor/obsensor_uvc_stream_channel.cpp`** -> AI Confidence: **99.39%**
152. **`samples/cpp/3calibration.cpp`** -> AI Confidence: **99.39%**
153. **`samples/cpp/asift.cpp`** -> AI Confidence: **99.39%**
154. **`samples/cpp/audio_spectrogram.cpp`** -> AI Confidence: **99.39%**
155. **`samples/cpp/detect_blob.cpp`** -> AI Confidence: **99.39%**
156. **`samples/cpp/intelligent_scissors.cpp`** -> AI Confidence: **99.39%**
157. **`samples/cpp/qrcode.cpp`** -> AI Confidence: **99.39%**
158. **`samples/cpp/select3dobj.cpp`** -> AI Confidence: **99.39%**
159. **`samples/cpp/train_HOG.cpp`** -> AI Confidence: **99.39%**
160. **`samples/cpp/tutorial_code/calib3d/real_time_pose_estimation/src/main_detection.cpp`** -> AI Confidence: **99.39%**
161. **`samples/cpp/tutorial_code/calib3d/real_time_pose_estimation/src/main_registration.cpp`** -> AI Confidence: **99.39%**
162. **`samples/cpp/tutorial_code/objectDetection/calibrate_camera.cpp`** -> AI Confidence: **99.39%**
163. **`samples/cpp/tutorial_code/objectDetection/calibrate_camera_charuco.cpp`** -> AI Confidence: **99.39%**
164. **`samples/cpp/tutorial_code/videoio/openni_orbbec_astra/openni_orbbec_astra.cpp`** -> AI Confidence: **99.39%**
165. **`samples/directx/d3d11_interop.cpp`** -> AI Confidence: **99.39%**
166. **`samples/dnn/classification.cpp`** -> AI Confidence: **99.39%**
167. **`samples/dnn/object_detection.cpp`** -> AI Confidence: **99.39%**
168. **`samples/gpu/bgfg_segm.cpp`** -> AI Confidence: **99.39%**
169. **`samples/openvx/no_wrappers.cpp`** -> AI Confidence: **99.39%**
170. **`samples/tapi/pyrlk_optical_flow.cpp`** -> AI Confidence: **99.39%**
171. **`samples/tapi/video_acceleration.cpp`** -> AI Confidence: **99.39%**
172. **`modules/ts/misc/perf_tests_timing.py`** -> AI Confidence: **99.39%**
173. **`platforms/apple/build_xcframework.py`** -> AI Confidence: **99.39%**
174. **`platforms/js/build_js.py`** -> AI Confidence: **99.39%**
175. **`modules/java/generator/android-21/java/org/opencv/android/CameraRenderer.java`** -> AI Confidence: **99.39%**
176. **`3rdparty/libwebp/src/mux/anim_encode.c`** -> AI Confidence: **99.35%**
177. **`3rdparty/openexr/IlmImf/ImfDeepTiledInputFile.cpp`** -> AI Confidence: **99.35%**
178. **`3rdparty/openexr/IlmImf/ImfPxr24Compressor.cpp`** -> AI Confidence: **99.35%**
179. **`3rdparty/openexr/IlmImf/dwaLookups.cpp`** -> AI Confidence: **99.35%**
180. **`samples/tapi/hog.cpp`** -> AI Confidence: **99.35%**
181. **`3rdparty/libjasper/jpc_t2cod.c`** -> AI Confidence: **99.34%**
182. **`3rdparty/libjpeg-turbo/src/jccolor.c`** -> AI Confidence: **99.34%**
183. **`3rdparty/libjpeg-turbo/src/jchuff.c`** -> AI Confidence: **99.34%**
184. **`3rdparty/libjpeg-turbo/src/jdcolor.c`** -> AI Confidence: **99.34%**
185. **`3rdparty/libjpeg-turbo/src/jddctmgr.c`** -> AI Confidence: **99.34%**
186. **`3rdparty/libjpeg-turbo/src/jdhuff.c`** -> AI Confidence: **99.34%**
187. **`3rdparty/libjpeg-turbo/src/jdmerge.c`** -> AI Confidence: **99.34%**
188. **`3rdparty/libjpeg-turbo/src/jmemmgr.c`** -> AI Confidence: **99.34%**
189. **`3rdparty/libpng/pngpriv.h`** -> AI Confidence: **99.34%**
190. **`3rdparty/libtiff/tif_pixarlog.c`** -> AI Confidence: **99.34%**
191. **`3rdparty/libwebp/src/dec/quant_dec.c`** -> AI Confidence: **99.34%**
192. **`3rdparty/libwebp/src/dsp/cpu.h`** -> AI Confidence: **99.34%**
193. **`3rdparty/libwebp/src/dsp/upsampling_neon.c`** -> AI Confidence: **99.34%**
194. **`3rdparty/libwebp/src/enc/cost_enc.c`** -> AI Confidence: **99.34%**
195. **`3rdparty/libwebp/src/enc/token_enc.c`** -> AI Confidence: **99.34%**
196. **`3rdparty/libwebp/src/utils/bit_writer_utils.c`** -> AI Confidence: **99.34%**
197. **`3rdparty/libwebp/src/utils/filters_utils.c`** -> AI Confidence: **99.34%**
198. **`3rdparty/openjpeg/openjp2/bench_dwt.c`** -> AI Confidence: **99.34%**
199. **`3rdparty/openjpeg/openjp2/ht_dec.c`** -> AI Confidence: **99.34%**
200. **`3rdparty/openjpeg/openjp2/t1.c`** -> AI Confidence: **99.34%**
201. **`3rdparty/libjasper/jasper/jas_fix.h`** -> AI Confidence: **99.34%**
202. **`3rdparty/openexr/Iex/IexThrowErrnoExc.cpp`** -> AI Confidence: **99.34%**
203. **`3rdparty/openexr/IlmImf/ImfFastHuf.cpp`** -> AI Confidence: **99.34%**
204. **`3rdparty/openexr/IlmImf/ImfHuf.cpp`** -> AI Confidence: **99.34%**
205. **`3rdparty/openexr/IlmImf/ImfRleCompressor.cpp`** -> AI Confidence: **99.34%**
206. **`apps/createsamples/createsamples.cpp`** -> AI Confidence: **99.34%**
207. **`apps/traincascade/boost.cpp`** -> AI Confidence: **99.34%**
208. **`hal/carotene/hal/tegra_hal.hpp`** -> AI Confidence: **99.34%**
209. **`modules/calib3d/src/undistort.dispatch.cpp`** -> AI Confidence: **99.34%**
210. **`modules/core/include/opencv2/core/fast_math.hpp`** -> AI Confidence: **99.34%**
211. **`modules/core/src/count_non_zero.dispatch.cpp`** -> AI Confidence: **99.34%**
212. **`modules/core/src/lapack.cpp`** -> AI Confidence: **99.34%**
213. **`modules/core/src/mean.dispatch.cpp`** -> AI Confidence: **99.34%**
214. **`modules/core/src/minmax.cpp`** -> AI Confidence: **99.34%**
215. **`modules/core/src/norm.dispatch.cpp`** -> AI Confidence: **99.34%**
216. **`modules/core/src/sum.dispatch.cpp`** -> AI Confidence: **99.34%**
217. **`modules/core/src/trace.cpp`** -> AI Confidence: **99.34%**
218. **`modules/dnn/src/cuda4dnn/primitives/eltwise.hpp`** -> AI Confidence: **99.34%**
219. **`modules/dnn/src/int8layers/eltwise_layer.cpp`** -> AI Confidence: **99.34%**
220. **`modules/dnn/src/layers/cpu_kernels/convolution.cpp`** -> AI Confidence: **99.34%**
221. **`modules/dnn/src/layers/recurrent_layers.cpp`** -> AI Confidence: **99.34%**
222. **`modules/dnn/src/layers/resize_layer.cpp`** -> AI Confidence: **99.34%**
223. **`modules/dnn/src/net_impl_backend.cpp`** -> AI Confidence: **99.34%**
224. **`modules/flann/include/opencv2/flann/kmeans_index.h`** -> AI Confidence: **99.34%**
225. **`modules/gapi/samples/api_example.cpp`** -> AI Confidence: **99.34%**
226. **`modules/gapi/src/3rdparty/vasot/src/components/ot/mtt/hungarian_wrap.cpp`** -> AI Confidence: **99.34%**
227. **`modules/imgcodecs/src/grfmt_gdal.cpp`** -> AI Confidence: **99.34%**
228. **`modules/imgcodecs/src/grfmt_jpeg.cpp`** -> AI Confidence: **99.34%**
229. **`modules/imgcodecs/src/grfmt_pam.cpp`** -> AI Confidence: **99.34%**
230. **`modules/imgcodecs/src/grfmt_spng.cpp`** -> AI Confidence: **99.34%**
231. **`modules/imgproc/src/box_filter.dispatch.cpp`** -> AI Confidence: **99.34%**
232. **`modules/imgproc/src/color_lab.cpp`** -> AI Confidence: **99.34%**
233. **`modules/imgproc/src/connectedcomponents.cpp`** -> AI Confidence: **99.34%**
234. **`modules/imgproc/src/contours_approx.cpp`** -> AI Confidence: **99.34%**
235. **`modules/imgproc/src/contours_new.cpp`** -> AI Confidence: **99.34%**
236. **`modules/imgproc/src/histogram.cpp`** -> AI Confidence: **99.34%**
237. **`modules/imgproc/src/hough.cpp`** -> AI Confidence: **99.34%**
238. **`modules/imgproc/src/sumpixels.dispatch.cpp`** -> AI Confidence: **99.34%**
239. **`modules/ml/src/data.cpp`** -> AI Confidence: **99.34%**
240. **`modules/objdetect/src/aruco/aruco_detector.cpp`** -> AI Confidence: **99.34%**
241. **`samples/cpp/cloning_demo.cpp`** -> AI Confidence: **99.34%**
242. **`samples/cpp/distrans.cpp`** -> AI Confidence: **99.34%**
243. **`samples/cpp/matchmethod_orb_akaze_brisk.cpp`** -> AI Confidence: **99.34%**
244. **`samples/cpp/tutorial_code/photo/seamless_cloning/cloning_demo.cpp`** -> AI Confidence: **99.34%**
245. **`samples/tapi/ufacedetect.cpp`** -> AI Confidence: **99.34%**
246. **`modules/core/misc/objc/common/MatOfDMatch.mm`** -> AI Confidence: **99.34%**
247. **`modules/core/misc/objc/common/MatOfKeyPoint.mm`** -> AI Confidence: **99.34%**
248. **`modules/core/misc/objc/common/MatOfPoint2f.mm`** -> AI Confidence: **99.34%**
249. **`modules/core/misc/objc/common/MatOfPoint2i.mm`** -> AI Confidence: **99.34%**
250. **`modules/core/misc/objc/common/MatOfPoint3.mm`** -> AI Confidence: **99.34%**
251. **`modules/core/misc/objc/common/MatOfPoint3f.mm`** -> AI Confidence: **99.34%**
252. **`modules/core/misc/objc/common/MatOfRect2d.mm`** -> AI Confidence: **99.34%**
253. **`modules/core/misc/objc/common/MatOfRect2i.mm`** -> AI Confidence: **99.34%**
254. **`modules/core/misc/objc/common/RotatedRect.mm`** -> AI Confidence: **99.34%**
255. **`modules/highgui/src/window_cocoa.mm`** -> AI Confidence: **99.34%**
256. **`modules/imgcodecs/misc/objc/ios/MatQuickLook.mm`** -> AI Confidence: **99.34%**
257. **`modules/imgcodecs/misc/objc/macosx/MatQuickLook.mm`** -> AI Confidence: **99.34%**
258. **`modules/videoio/src/cap_avfoundation_mac.mm`** -> AI Confidence: **99.34%**
259. **`modules/python/src2/hdr_parser.py`** -> AI Confidence: **99.33%**
260. **`3rdparty/libjpeg-turbo/src/jcapistd.c`** -> AI Confidence: **99.32%**
261. **`3rdparty/libjpeg-turbo/src/jccoefct.c`** -> AI Confidence: **99.32%**
262. **`3rdparty/libjpeg-turbo/src/jcicc.c`** -> AI Confidence: **99.32%**
263. **`3rdparty/libjpeg-turbo/src/jcinit.c`** -> AI Confidence: **99.32%**
264. **`3rdparty/libjpeg-turbo/src/jclossls.c`** -> AI Confidence: **99.32%**
265. **`3rdparty/libjpeg-turbo/src/jcmainct.c`** -> AI Confidence: **99.32%**
266. **`3rdparty/libjpeg-turbo/src/jcparam.c`** -> AI Confidence: **99.32%**
267. **`3rdparty/libjpeg-turbo/src/jctrans.c`** -> AI Confidence: **99.32%**
268. **`3rdparty/libjpeg-turbo/src/jdapimin.c`** -> AI Confidence: **99.32%**
269. **`3rdparty/libjpeg-turbo/src/jdicc.c`** -> AI Confidence: **99.32%**
270. **`3rdparty/libjpeg-turbo/src/jdpostct.c`** -> AI Confidence: **99.32%**
271. **`3rdparty/libjpeg-turbo/src/jdtrans.c`** -> AI Confidence: **99.32%**
272. **`3rdparty/libjpeg-turbo/src/jfdctfst.c`** -> AI Confidence: **99.32%**
273. **`3rdparty/libjpeg-turbo/src/jfdctint.c`** -> AI Confidence: **99.32%**
274. **`3rdparty/libjpeg-turbo/src/jidctflt.c`** -> AI Confidence: **99.32%**
275. **`3rdparty/libjpeg-turbo/src/jidctfst.c`** -> AI Confidence: **99.32%**
276. **`3rdparty/libjpeg-turbo/src/jidctint.c`** -> AI Confidence: **99.32%**
277. **`3rdparty/libjpeg-turbo/src/jidctred.c`** -> AI Confidence: **99.32%**
278. **`3rdparty/libjpeg-turbo/src/jquant2.c`** -> AI Confidence: **99.32%**
279. **`3rdparty/libjpeg/jcdctmgr.c`** -> AI Confidence: **99.32%**
280. **`3rdparty/libjpeg/jddctmgr.c`** -> AI Confidence: **99.32%**
281. **`3rdparty/libjpeg/jfdctfst.c`** -> AI Confidence: **99.32%**
282. **`3rdparty/libjpeg/jidctflt.c`** -> AI Confidence: **99.32%**
283. **`3rdparty/libjpeg/jidctfst.c`** -> AI Confidence: **99.32%**
284. **`3rdparty/libjpeg/jmemmgr.c`** -> AI Confidence: **99.32%**
285. **`3rdparty/libpng/mips/mips_init.c`** -> AI Confidence: **99.32%**
286. **`3rdparty/libpng/pngrtran.c`** -> AI Confidence: **99.32%**
287. **`3rdparty/libpng/powerpc/powerpc_init.c`** -> AI Confidence: **99.32%**
288. **`3rdparty/libtiff/tif_getimage.c`** -> AI Confidence: **99.32%**
289. **`3rdparty/libtiff/tif_print.c`** -> AI Confidence: **99.32%**
290. **`3rdparty/libwebp/src/dsp/dec_clip_tables.c`** -> AI Confidence: **99.32%**
291. **`3rdparty/libwebp/src/dsp/lossless_msa.c`** -> AI Confidence: **99.32%**
292. **`3rdparty/libwebp/src/dsp/msa_macro.h`** -> AI Confidence: **99.32%**
293. **`3rdparty/libwebp/src/dsp/neon.h`** -> AI Confidence: **99.32%**
294. **`3rdparty/libwebp/src/dsp/rescaler_mips_dsp_r2.c`** -> AI Confidence: **99.32%**
295. **`3rdparty/openexr/IlmImf/ImfRle.cpp`** -> AI Confidence: **99.32%**
296. **`3rdparty/protobuf/src/google/protobuf/extension_set_inl.h`** -> AI Confidence: **99.32%**
297. **`hal/carotene/src/fast.cpp`** -> AI Confidence: **99.32%**
298. **`hal/carotene/src/laplacian.cpp`** -> AI Confidence: **99.32%**
299. **`hal/ipp/src/norm_ipp.cpp`** -> AI Confidence: **99.32%**
300. **`hal/ndsrvp/src/bilateralFilter.cpp`** -> AI Confidence: **99.32%**
301. **`hal/ndsrvp/src/filter.cpp`** -> AI Confidence: **99.32%**
302. **`hal/ndsrvp/src/remap.cpp`** -> AI Confidence: **99.32%**
303. **`modules/calib3d/src/fisheye.cpp`** -> AI Confidence: **99.32%**
304. **`modules/core/src/kmeans.cpp`** -> AI Confidence: **99.32%**
305. **`modules/dnn/src/net_impl_fuse.cpp`** -> AI Confidence: **99.32%**
306. **`modules/dnn/src/vkcom/src/op_conv.cpp`** -> AI Confidence: **99.32%**
307. **`modules/gapi/src/executor/gabstractstreamingexecutor.cpp`** -> AI Confidence: **99.32%**
308. **`modules/gapi/src/streaming/onevpl/onevpl_export.hpp`** -> AI Confidence: **99.32%**
309. **`modules/imgcodecs/src/grfmt_bmp.cpp`** -> AI Confidence: **99.32%**
310. **`modules/imgcodecs/src/grfmt_gif.cpp`** -> AI Confidence: **99.32%**
311. **`modules/imgproc/src/color.cpp`** -> AI Confidence: **99.32%**
312. **`modules/imgproc/src/contours.cpp`** -> AI Confidence: **99.32%**
313. **`modules/imgproc/src/deriv.cpp`** -> AI Confidence: **99.32%**
314. **`modules/imgproc/src/grabcut.cpp`** -> AI Confidence: **99.32%**
315. **`modules/imgproc/src/phasecorr.cpp`** -> AI Confidence: **99.32%**
316. **`modules/imgproc/src/thresh.cpp`** -> AI Confidence: **99.32%**
317. **`modules/ml/src/tree.cpp`** -> AI Confidence: **99.32%**
318. **`modules/photo/perf/perf_main.cpp`** -> AI Confidence: **99.32%**
319. **`modules/photo/src/inpaint.cpp`** -> AI Confidence: **99.32%**
320. **`modules/stitching/src/seam_finders.cpp`** -> AI Confidence: **99.32%**
321. **`modules/stitching/src/util_log.hpp`** -> AI Confidence: **99.32%**
322. **`modules/video/src/tracking/detail/tracking_feature.cpp`** -> AI Confidence: **99.32%**
323. **`modules/videoio/src/cap_ximea.cpp`** -> AI Confidence: **99.32%**
324. **`modules/core/misc/objc/common/Point2i.mm`** -> AI Confidence: **99.32%**
325. **`modules/core/misc/objc/common/Point3i.mm`** -> AI Confidence: **99.32%**
326. **`modules/core/misc/objc/common/Rect2d.mm`** -> AI Confidence: **99.32%**
327. **`modules/core/misc/objc/common/Rect2f.mm`** -> AI Confidence: **99.32%**
328. **`modules/core/misc/objc/common/Rect2i.mm`** -> AI Confidence: **99.32%**
329. **`modules/core/misc/objc/common/Size2i.mm`** -> AI Confidence: **99.32%**
330. **`modules/imgcodecs/src/ios_conversions.mm`** -> AI Confidence: **99.32%**
331. **`modules/videoio/misc/objc/ios/CvVideoCamera2.mm`** -> AI Confidence: **99.32%**
332. **`modules/videoio/src/cap_ios_video_camera.mm`** -> AI Confidence: **99.32%**
333. **`3rdparty/ittnotify/src/ittnotify/jitprofiling.c`** -> AI Confidence: **99.31%**
334. **`3rdparty/libjasper/jas_stream.c`** -> AI Confidence: **99.31%**
335. **`3rdparty/libjasper/jas_tvp.c`** -> AI Confidence: **99.31%**
336. **`3rdparty/libjasper/jasper/jas_stream.h`** -> AI Confidence: **99.31%**
337. **`3rdparty/libjasper/jpc_bs.c`** -> AI Confidence: **99.31%**
338. **`3rdparty/libjasper/jpc_dec.c`** -> AI Confidence: **99.31%**
339. **`3rdparty/libjasper/jpc_math.c`** -> AI Confidence: **99.31%**
340. **`3rdparty/libjasper/jpc_mqdec.c`** -> AI Confidence: **99.31%**
341. **`3rdparty/libjasper/jpc_tsfb.c`** -> AI Confidence: **99.31%**
342. **`3rdparty/libjpeg-turbo/simd/arm/aarch32/jsimd.c`** -> AI Confidence: **99.31%**
343. **`3rdparty/libjpeg-turbo/simd/arm/aarch64/jsimd.c`** -> AI Confidence: **99.31%**
344. **`3rdparty/libjpeg-turbo/simd/arm/jdsample-neon.c`** -> AI Confidence: **99.31%**
345. **`3rdparty/libjpeg-turbo/simd/arm/jfdctint-neon.c`** -> AI Confidence: **99.31%**
346. **`3rdparty/libjpeg-turbo/simd/arm/jidctint-neon.c`** -> AI Confidence: **99.31%**
347. **`3rdparty/libjpeg-turbo/simd/mips/jsimd.c`** -> AI Confidence: **99.31%**
348. **`3rdparty/libjpeg-turbo/simd/mips64/jsimd.c`** -> AI Confidence: **99.31%**
349. **`3rdparty/libjpeg-turbo/simd/powerpc/jsimd.c`** -> AI Confidence: **99.31%**
350. **`3rdparty/libjpeg-turbo/src/jinclude.h`** -> AI Confidence: **99.31%**
351. **`3rdparty/libspng/spng.c`** -> AI Confidence: **99.31%**
352. **`3rdparty/libwebp/sharpyuv/sharpyuv.c`** -> AI Confidence: **99.31%**
353. **`3rdparty/libwebp/src/dec/buffer_dec.c`** -> AI Confidence: **99.31%**
354. **`3rdparty/libwebp/src/dec/idec_dec.c`** -> AI Confidence: **99.31%**
355. **`3rdparty/libwebp/src/dec/vp8_dec.c`** -> AI Confidence: **99.31%**
356. **`3rdparty/libwebp/src/dec/webp_dec.c`** -> AI Confidence: **99.31%**
357. **`3rdparty/libwebp/src/demux/anim_decode.c`** -> AI Confidence: **99.31%**
358. **`3rdparty/libwebp/src/demux/demux.c`** -> AI Confidence: **99.31%**
359. **`3rdparty/libwebp/src/dsp/cost.c`** -> AI Confidence: **99.31%**
360. **`3rdparty/libwebp/src/dsp/cpu.c`** -> AI Confidence: **99.31%**
361. **`3rdparty/libwebp/src/dsp/dec.c`** -> AI Confidence: **99.31%**
362. **`3rdparty/libwebp/src/dsp/dec_sse2.c`** -> AI Confidence: **99.31%**
363. **`3rdparty/libwebp/src/dsp/enc.c`** -> AI Confidence: **99.31%**
364. **`3rdparty/libwebp/src/dsp/filters_sse2.c`** -> AI Confidence: **99.31%**
365. **`3rdparty/libwebp/src/dsp/lossless.c`** -> AI Confidence: **99.31%**
366. **`3rdparty/libwebp/src/dsp/lossless_enc.c`** -> AI Confidence: **99.31%**
367. **`3rdparty/libwebp/src/dsp/lossless_enc_mips32.c`** -> AI Confidence: **99.31%**
368. **`3rdparty/libwebp/src/dsp/lossless_enc_sse41.c`** -> AI Confidence: **99.31%**
369. **`3rdparty/libwebp/src/dsp/lossless_sse2.c`** -> AI Confidence: **99.31%**
370. **`3rdparty/libwebp/src/dsp/upsampling.c`** -> AI Confidence: **99.31%**
371. **`3rdparty/libwebp/src/dsp/upsampling_sse2.c`** -> AI Confidence: **99.31%**
372. **`3rdparty/libwebp/src/dsp/upsampling_sse41.c`** -> AI Confidence: **99.31%**
373. **`3rdparty/libwebp/src/dsp/yuv.c`** -> AI Confidence: **99.31%**
374. **`3rdparty/libwebp/src/dsp/yuv_sse2.c`** -> AI Confidence: **99.31%**
375. **`3rdparty/libwebp/src/dsp/yuv_sse41.c`** -> AI Confidence: **99.31%**
376. **`3rdparty/libwebp/src/enc/alpha_enc.c`** -> AI Confidence: **99.31%**
377. **`3rdparty/libwebp/src/enc/near_lossless_enc.c`** -> AI Confidence: **99.31%**
378. **`3rdparty/libwebp/src/enc/picture_csp_enc.c`** -> AI Confidence: **99.31%**
379. **`3rdparty/libwebp/src/enc/picture_enc.c`** -> AI Confidence: **99.31%**
380. **`3rdparty/libwebp/src/enc/picture_rescale_enc.c`** -> AI Confidence: **99.31%**
381. **`3rdparty/libwebp/src/enc/syntax_enc.c`** -> AI Confidence: **99.31%**
382. **`3rdparty/libwebp/src/mux/muxedit.c`** -> AI Confidence: **99.31%**
383. **`3rdparty/libwebp/src/mux/muxinternal.c`** -> AI Confidence: **99.31%**
384. **`3rdparty/libwebp/src/utils/bit_reader_utils.c`** -> AI Confidence: **99.31%**
385. **`3rdparty/libwebp/src/utils/huffman_utils.c`** -> AI Confidence: **99.31%**
386. **`3rdparty/libwebp/src/utils/palette.c`** -> AI Confidence: **99.31%**
387. **`3rdparty/libwebp/src/utils/thread_utils.c`** -> AI Confidence: **99.31%**
388. **`3rdparty/libwebp/src/utils/utils.c`** -> AI Confidence: **99.31%**
389. **`3rdparty/libwebp/src/utils/bit_reader_inl_utils.h`** -> AI Confidence: **99.31%**
390. **`3rdparty/openexr/IlmImf/ImfCompositeDeepScanLine.cpp`** -> AI Confidence: **99.31%**
391. **`3rdparty/openexr/IlmImf/ImfCompressor.cpp`** -> AI Confidence: **99.31%**
392. **`3rdparty/openexr/IlmImf/ImfHeader.cpp`** -> AI Confidence: **99.31%**
393. **`3rdparty/openexr/IlmImf/ImfMultiPartOutputFile.cpp`** -> AI Confidence: **99.31%**
394. **`3rdparty/openexr/IlmImf/ImfPartHelper.h`** -> AI Confidence: **99.31%**
395. **`3rdparty/openexr/IlmImf/ImfRgbaFile.cpp`** -> AI Confidence: **99.31%**
396. **`3rdparty/openexr/IlmImf/ImfTiledInputFile.cpp`** -> AI Confidence: **99.31%**
397. **`3rdparty/openexr/IlmImf/ImfTiledOutputFile.cpp`** -> AI Confidence: **99.31%**
398. **`3rdparty/openexr/IlmThread/IlmThreadPool.cpp`** -> AI Confidence: **99.31%**
399. **`3rdparty/protobuf/src/google/protobuf/arenastring.cc`** -> AI Confidence: **99.31%**
400. **`3rdparty/protobuf/src/google/protobuf/dynamic_message.cc`** -> AI Confidence: **99.31%**
401. **`3rdparty/protobuf/src/google/protobuf/extension_set.cc`** -> AI Confidence: **99.31%**
402. **`3rdparty/protobuf/src/google/protobuf/extension_set_heavy.cc`** -> AI Confidence: **99.31%**
403. **`3rdparty/protobuf/src/google/protobuf/generated_message_reflection.cc`** -> AI Confidence: **99.31%**
404. **`3rdparty/protobuf/src/google/protobuf/io/coded_stream.cc`** -> AI Confidence: **99.31%**
405. **`3rdparty/protobuf/src/google/protobuf/io/io_win32.cc`** -> AI Confidence: **99.31%**
406. **`3rdparty/protobuf/src/google/protobuf/io/strtod.cc`** -> AI Confidence: **99.31%**
407. **`3rdparty/protobuf/src/google/protobuf/message.cc`** -> AI Confidence: **99.31%**
408. **`3rdparty/protobuf/src/google/protobuf/repeated_ptr_field.cc`** -> AI Confidence: **99.31%**
409. **`3rdparty/protobuf/src/google/protobuf/stubs/stringpiece.cc`** -> AI Confidence: **99.31%**
410. **`3rdparty/protobuf/src/google/protobuf/stubs/stringprintf.cc`** -> AI Confidence: **99.31%**
411. **`3rdparty/protobuf/src/google/protobuf/unknown_field_set.cc`** -> AI Confidence: **99.31%**
412. **`apps/interactive-calibration/main.cpp`** -> AI Confidence: **99.31%**
413. **`apps/traincascade/imagestorage.cpp`** -> AI Confidence: **99.31%**
414. **`cmake/checks/webnn.cpp`** -> AI Confidence: **99.31%**
415. **`hal/openvx/hal/openvx_hal.cpp`** -> AI Confidence: **99.31%**
416. **`modules/core/include/opencv2/core/private.hpp`** -> AI Confidence: **99.31%**
417. **`modules/core/src/async.cpp`** -> AI Confidence: **99.31%**
418. **`modules/core/src/hal_internal.cpp`** -> AI Confidence: **99.31%**
419. **`modules/core/src/logger.cpp`** -> AI Confidence: **99.31%**
420. **`modules/core/src/ocl.cpp`** -> AI Confidence: **99.31%**
421. **`modules/core/src/opencl/runtime/opencl_core.cpp`** -> AI Confidence: **99.31%**
422. **`modules/core/src/opengl.cpp`** -> AI Confidence: **99.31%**
423. **`modules/core/src/parallel.cpp`** -> AI Confidence: **99.31%**
424. **`modules/core/src/parallel/parallel.cpp`** -> AI Confidence: **99.31%**
425. **`modules/core/src/parallel_impl.cpp`** -> AI Confidence: **99.31%**
426. **`modules/dnn/src/cuda4dnn/primitives/matmul.hpp`** -> AI Confidence: **99.31%**
427. **`modules/dnn/src/cuda4dnn/primitives/scale_shift.hpp`** -> AI Confidence: **99.31%**
428. **`modules/dnn/src/darknet/darknet_importer.cpp`** -> AI Confidence: **99.31%**
429. **`modules/dnn/src/ie_ngraph.cpp`** -> AI Confidence: **99.31%**
430. **`modules/dnn/src/layers/batch_norm_layer.cpp`** -> AI Confidence: **99.31%**
431. **`modules/dnn/src/layers/concat_layer.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `114` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `17775` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `3rdparty/libwebp/src/utils/thread_utils.c` (C) -> Cumulative Risk: **704.94**
- **Archetype:** `file_cluster_4` (Distance: 12.637 IQR)
- **Magnitude:** 250.28 | **LOC:** 371 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `pthread_cond_wait` (Impact: 48.3), `Reset` (Impact: 14.9), `WebPSetWorkerInterface` (Impact: 8.5)

### 2. `samples/android/tutorial-4-opencl/src/org/opencv/samples/tutorial4/Tutorial4Activity.java` (JAVA) -> Cumulative Risk: **696.28**
- **Archetype:** `file_cluster_13` (Distance: 11.325 IQR)
- **Magnitude:** 99.24 | **LOC:** 101 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Concurrency (92.3153%), Safety Score (90.3374%)
- **Heaviest Functions:** `onOptionsItemSelected` (Impact: 30.6), `onCreate` (Impact: 6.2), `onCreateOptionsMenu` (Impact: 5.4)

### 3. `modules/gapi/src/executor/gasync.cpp` (CPP) -> Cumulative Risk: **693.8**
- **Archetype:** `file_cluster_4` (Distance: 14.857 IQR)
- **Magnitude:** 664.46 | **LOC:** 281 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `add_task` (Impact: 15.1), `call_with_future` (Impact: 10.5), `async_apply` (Impact: 10.5)

### 4. `hal/riscv-rvv/src/imgproc/moments.cpp` (CPP) -> Cumulative Risk: **691.5**
- **Archetype:** `file_cluster_4` (Distance: 13.47 IQR)
- **Magnitude:** 289.88 | **LOC:** 190 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), Safety Score (99.3236%)
- **Heaviest Functions:** `imageMoments` (Impact: 31.4), `imageMoments` (Impact: 15.5), `invoke` (Impact: 4.3)

### 5. `samples/android/tutorial-4-opencl/src/org/opencv/samples/tutorial4/MyGLSurfaceView.java` (JAVA) -> Cumulative Risk: **687.68**
- **Archetype:** `file_cluster_13` (Distance: 9.772 IQR)
- **Magnitude:** 99.68 | **LOC:** 116 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9988%), Concurrency (99.9692%), Documentation (96.9801%)
- **Heaviest Functions:** `onCameraTexture` (Impact: 17.2), `setProcessingMode` (Impact: 11.8), `onTouchEvent` (Impact: 5.2)

### 6. `platforms/osx/build_framework.py` (PYTHON) -> Cumulative Risk: **685.94**
- **Archetype:** `file_cluster_4` (Distance: 11.605 IQR)
- **Magnitude:** 99.66 | **LOC:** 133 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.877%), Concurrency (99.7439%)
- **Heaviest Functions:** `getBuildCommand` (Impact: 42.5), `getObjcTarget` (Impact: 5.5), `checkCMakeVersion` (Impact: 3.6)

### 7. `3rdparty/libtiff/tif_open.c` (C) -> Cumulative Risk: **684.39**
- **Archetype:** `file_cluster_8` (Distance: 13.11 IQR)
- **Magnitude:** 905.96 | **LOC:** 946 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.4539%)
- **Heaviest Functions:** `TIFFClientOpenExt` (Impact: 421.6), `_TIFFcallocExt` (Impact: 13.6), `_TIFFreallocExt` (Impact: 12.9)

### 8. `3rdparty/libpng/pngget.c` (C) -> Cumulative Risk: **679.34**
- **Archetype:** `file_cluster_8` (Distance: 12.746 IQR)
- **Magnitude:** 1077.72 | **LOC:** 1371 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Tech Debt (99.6451%)
- **Heaviest Functions:** `png_get_cHRM_XYZ` (Impact: 21.6), `png_get_mDCV` (Impact: 21.2), `png_get_cHRM_XYZ_fixed` (Impact: 15.4)

### 9. `modules/dnn/src/op_halide.cpp` (CPP) -> Cumulative Risk: **675.93**
- **Archetype:** `file_cluster_8` (Distance: 13.304 IQR)
- **Magnitude:** 454.38 | **LOC:** 430 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9694%), Safety Score (96.4208%)
- **Heaviest Functions:** `Layer::applyHalideScheduler` (Impact: 59.7), `Net::Impl::compileHalide` (Impact: 15.0), `getCanonicalSize` (Impact: 10.7)

### 10. `3rdparty/libwebp/src/dec/webp_dec.c` (C) -> Cumulative Risk: **671.31**
- **Archetype:** `file_cluster_13` (Distance: 14.028 IQR)
- **Magnitude:** 608.66 | **LOC:** 932 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (91.5405%)
- **Heaviest Functions:** `ParseOptionalChunks` (Impact: 163.7), `WebPValidateDecoderConfig` (Impact: 22.5), `WebPCheckCropDimensions` (Impact: 18.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `modules/core/src/ocl.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.713 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.344 IQR)
- **Top Global Matches:** file_cluster_8: 14.713, file_cluster_13: 14.907, file_cluster_7: 14.965
- **Magnitude:** 95471.86 | **LOC:** 7665 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.4624%), Tech Debt (8.464%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 362`, `args: 256`, `func_start: 244`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 2`, `state_mutation: 2241`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 4`, `import: 27`
* *Defense:* `safety: 43`, `doc: 231`, `sync_locks: 18`, `immutability_locks: 267`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` precomp.hpp, opencl_clblas.hpp, filesystem.hpp, configuration.private.hpp, ocl_disabled.impl.hpp, allocator_stats.impl.hpp, set, opencl_core.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/openjpeg/openjp2/j2k.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.786 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.788 IQR)
- **Top Global Matches:** file_cluster_8: 14.786, file_cluster_0: 14.952, file_cluster_11: 14.957
- **Magnitude:** 8533.02 | **LOC:** 13596 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4553%), Tech Debt (21.8504%)
**Top Internal Functions/Classes:**
  * `opj_j2k_setup_encoder` (Impact: 217.3)
    * *Intent:* 2); /* Isot */
  * `opj_j2k_is_imf_compliant` (Impact: 174.9)
  * `opj_j2k_build_tp_index_from_tlm` (Impact: 108.6)
  * `opj_j2k_read_siz` (Impact: 96.0)
    * *Intent:* /** * Reads a POC marker (Progression Order Change) * * @param p_header_data the data contained in t...
  * `opj_j2k_decode_tiles` (Impact: 64.7)
    * *Intent:* /* Codeblock style: no mode switch enabled */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1423`, `structural_boundaries: 608`, `args: 17`, `func_start: 131`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 5118`, `dead_code: 10`, `planned_debt: 12`, `fragile_debt: 13`, `orphaned_logic: 33`
* *Architecture:* `io: 23`, `api: 1279`
* *Defense:* `safety: 222`, `doc: 67`, `test: 211`, `immutability_locks: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` opj_includes.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/features2d/src/agast.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.558 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.564 IQR)
- **Top Global Matches:** file_cluster_8: 11.558, file_cluster_7: 12.108, file_cluster_1: 12.334
- **Magnitude:** 8433.36 | **LOC:** 8200 | **CtrlFlow:** 99.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.562%), Tech Debt (8.2646%)
**Top Internal Functions/Classes:**
  * `AGAST_7_12s` (Impact: 2046.0)
  * `AGAST_7_12d` (Impact: 2007.0)
  * `OAST_9_16` (Impact: 2006.5)
  * `AGAST_5_8` (Impact: 1400.1)
  * `AGAST` (Impact: 125.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7058`, `structural_boundaries: 29`, `args: 33`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 663`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` precomp.hpp, agast_score.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/histogram.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.636 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.617 IQR)
- **Top Global Matches:** file_cluster_8: 15.636, file_cluster_7: 15.845, file_cluster_13: 15.907
- **Magnitude:** 7759.16 | **LOC:** 3658 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.3163%), Tech Debt (35.1076%)
**Top Internal Functions/Classes:**
  * `calcHist_` (Impact: 335.7)
  * `calcHist_8u` (Impact: 170.3)
  * `calcBackProj_` (Impact: 157.0)
  * `cv::calcHist` (Impact: 139.4)
    * *Intent:* #endif
  * `cv::compareHist` (Impact: 116.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 848`, `structural_boundaries: 125`, `args: 88`, `func_start: 51`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 5233`, `planned_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 11`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 3`, `doc: 119`, `sync_locks: 5`, `immutability_locks: 241`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` precomp.hpp, opencl_kernels_imgproc.hpp, ovx_defs.hpp, intrin.hpp, tls.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/ts/src/ts_func.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.289 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.346 IQR)
- **Top Global Matches:** file_cluster_8: 15.289, file_cluster_11: 15.582, file_cluster_13: 15.622
- **Magnitude:** 7439.54 | **LOC:** 3322 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.3498%), Tech Debt (63.7775%)
**Top Internal Functions/Classes:**
  * `threshold` (Impact: 190.8)
  * `cmpEps` (Impact: 160.4)
    * *Intent:* #define CMP_EPS_OK 0 #define CMP_EPS_BIG_DIFF -1 #define CMP_EPS_INVALID_TEST_DATA -2 // there is Na...
  * `muldiv` (Impact: 96.2)
  * `copyMakeBorder` (Impact: 80.0)
  * `transform` (Impact: 77.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1065`, `structural_boundaries: 172`, `args: 99`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 4784`, `dead_code: 1`, `duplicate_logic: 26`, `orphaned_logic: 25`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 406`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` precomp.hpp, limits.h, float.h, types_c.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/traincascade/old_ml_tree.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.621 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.452 IQR)
- **Top Global Matches:** file_cluster_8: 15.621, file_cluster_7: 15.88, file_cluster_13: 15.882
- **Magnitude:** 6808.74 | **LOC:** 4154 | **CtrlFlow:** 89.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1943%), Tech Debt (81.441%)
**Top Internal Functions/Classes:**
  * `CvDTreeTrainData::set_data` (Impact: 484.4)
  * `CvDTree::split_node_data` (Impact: 121.4)
  * `CvDTreeTrainData::subsample_data` (Impact: 115.4)
  * `CvDTree::find_split_cat_class` (Impact: 107.3)
  * `CvDTreeTrainData::get_vectors` (Impact: 82.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 646`, `structural_boundaries: 78`, `args: 110`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 10`, `state_mutation: 4920`, `dead_code: 6`, `planned_debt: 3`, `duplicate_logic: 10`, `orphaned_logic: 46`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `doc: 48`, `immutability_locks: 141`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` old_ml_precomp.hpp, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/imgwarp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.364 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.2 IQR)
- **Top Global Matches:** file_cluster_8: 15.364, file_cluster_11: 15.607, file_cluster_13: 15.614
- **Magnitude:** 6053.8 | **LOC:** 3324 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.3193%), Tech Debt (34.8645%)
**Top Internal Functions/Classes:**
  * `remapBilinear` (Impact: 317.5)
  * `cv::convertMaps` (Impact: 240.1)
  * `remapLanczos4` (Impact: 125.5)
  * `ocl_warpTransform` (Impact: 122.2)
  * `cv::remap` (Impact: 115.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 648`, `structural_boundaries: 145`, `args: 214`, `func_start: 48`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 4179`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 4`, `orphaned_logic: 19`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `doc: 55`, `immutability_locks: 260`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` precomp.hpp, opencl_kernels_imgproc.hpp, imgwarp.hpp, hal_replacement.hpp, configuration.private.hpp, intrin.hpp, softfloat.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/resize.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.23 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.847 IQR)
- **Top Global Matches:** file_cluster_8: 15.23, file_cluster_13: 15.446, file_cluster_11: 15.464
- **Magnitude:** 5697.84 | **LOC:** 4261 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.3459%), Tech Debt (28.5034%)
**Top Internal Functions/Classes:**
  * `ocl_resize` (Impact: 290.8)
  * `resizeNN` (Impact: 54.0)
  * `hlineResize` (Impact: 40.8)
    * *Intent:* // Third party copyrights are property of their respective owners. // // Redistribution and use in s...
  * `cv::resize` (Impact: 31.4)
  * `resize_bitExact` (Impact: 28.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 636`, `structural_boundaries: 460`, `args: 377`, `func_start: 58`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 4845`, `dead_code: 4`, `duplicate_logic: 18`, `orphaned_logic: 7`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `doc: 53`, `immutability_locks: 314`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` precomp.hpp, resize.hpp, opencl_kernels_imgproc.hpp, hal_replacement.hpp, intrin.hpp, ovx_defs.hpp, softfloat.hpp, buffer_area.private.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/src/matmul.simd.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.278 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.335 IQR)
- **Top Global Matches:** file_cluster_8: 15.278, file_cluster_7: 15.542, file_cluster_11: 15.576
- **Magnitude:** 5407.66 | **LOC:** 2630 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gemmImpl` (Impact: 414.5)
  * `GEMMSingleMul` (Impact: 221.2)
  * `MulTransposedR` (Impact: 95.3)
  * `getMulTransposedFunc` (Impact: 76.5)
  * `perspectiveTransform_` (Impact: 73.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 142`, `args: 86`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 3802`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 36`, `immutability_locks: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.201
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` precomp.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hal/riscv-rvv/include/types.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.18 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.081 IQR)
- **Top Global Matches:** file_cluster_8: 11.18, file_cluster_16: 11.548, file_cluster_7: 11.859
- **Magnitude:** 5366.71 | **LOC:** 879 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.7472%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 397`, `args: 351`, `func_start: 79`, `class_start: 16`
* *Risk/State:* `state_mutation: 120`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type_traits, riscv_vector.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/smooth.simd.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.063 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.59 IQR)
- **Top Global Matches:** file_cluster_8: 15.063, file_cluster_11: 15.339, file_cluster_13: 15.344
- **Magnitude:** 5307.36 | **LOC:** 2736 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.6444%), Tech Debt (10.4697%)
**Top Internal Functions/Classes:**
  * `fixedSmoothInvoker` (Impact: 275.4)
  * `hlineSmooth5N14641` (Impact: 89.3)
    * *Intent:* #endif
  * `hlineSmooth5Nabcba` (Impact: 83.2)
  * `hlineSmooth5N` (Impact: 83.1)
  * `hlineSmooth` (Impact: 62.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 196`, `args: 48`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4236`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `doc: 29`, `immutability_locks: 250`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` precomp.hpp, filter.hpp, vector, intrin.hpp, softfloat.hpp, fixedpoint.inl.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `3rdparty/libjasper/jpc_qmfb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.187 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.608 IQR)
- **Top Global Matches:** file_cluster_8: 15.187, file_cluster_13: 15.467, file_cluster_7: 15.503
- **Magnitude:** 5163.72 | **LOC:** 3145 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.2707%), Tech Debt (8.2699%)
**Top Internal Functions/Classes:**
  * `jpc_ns_fwdlift_colgrp` (Impact: 45.4)
  * `jpc_ns_fwdlift_colres` (Impact: 45.4)
  * `jpc_ns_invlift_colgrp` (Impact: 45.4)
  * `jpc_ns_invlift_colres` (Impact: 45.4)
  * `jpc_ns_fwdlift_col` (Impact: 28.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 50`, `args: 8`, `func_start: 28`
* *Risk/State:* `state_mutation: 4192`, `orphaned_logic: 2`
* *Architecture:* `api: 298`, `import: 7`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jas_math.h, jpc_math.h, assert.h, jas_malloc.h, jas_fix.h, jpc_qmfb.h, jpc_tsfb.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/calib3d/src/chessboard.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.038 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.592 IQR)
- **Top Global Matches:** file_cluster_8: 15.038, file_cluster_7: 15.28, file_cluster_13: 15.321
- **Magnitude:** 5155.32 | **LOC:** 3976 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (51.3323%), Tech Debt (87.8838%)
**Top Internal Functions/Classes:**
  * `Chessboard::Board::PointIter::left` (Impact: 52.1)
  * `Chessboard::Board::PointIter::top` (Impact: 52.1)
  * `Chessboard::Board::PointIter::right` (Impact: 52.1)
  * `Chessboard::Board::PointIter::bottom` (Impact: 52.1)
  * `findChessboardCornersSB` (Impact: 48.7)
    * *Intent:* // public API
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 264`, `args: 187`, `func_start: 83`
* *Risk/State:* `state_mutation: 3909`, `dead_code: 9`, `planned_debt: 6`, `duplicate_logic: 21`, `orphaned_logic: 48`
* *Architecture:* `import: 5`
* *Defense:* `doc: 125`, `immutability_locks: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` flann.hpp, precomp.hpp, math.h, highgui.hpp, chessboard.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/FaceDetection/FaceDetection/FaceDetection_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/ImageManipulations/MediaCapture_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/JavaScript/MediaCaptureJavaScript_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt/OcvImageProcessing/OcvImageProcessing/OcvImageProcessing_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt_universal/VideoCaptureXAML/video_capture_xaml/video_capture_xaml.Windows/video_capture_xaml.Windows_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/winrt_universal/VideoCaptureXAML/video_capture_xaml/video_capture_xaml.WindowsPhone/video_capture_xaml.WindowsPhone_TemporaryKey.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/filter.simd.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.058 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_8: 15.058, file_cluster_7: 15.291, file_cluster_13: 15.368
- **Magnitude:** 4844.36 | **LOC:** 3258 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.9227%), Tech Debt (74.9698%)
**Top Internal Functions/Classes:**
  * `getLinearColumnFilter` (Impact: 149.0)
  * `getLinearFilter` (Impact: 90.8)
  * `FilterEngine__proceed` (Impact: 79.1)
  * `getLinearRowFilter` (Impact: 73.7)
  * `FilterEngine__start` (Impact: 70.1)
    * *Intent:* // (including, but not limited to, procurement of substitute goods or services; // loss of use, data...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 193`, `args: 258`, `func_start: 56`, `class_start: 29`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 4162`, `dead_code: 1`, `duplicate_logic: 42`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 143`, `immutability_locks: 236`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.201
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` precomp.hpp, intrin.hpp, filter.hpp, cstddef
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hal/carotene/src/colorconvert.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.893 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.655 IQR)
- **Top Global Matches:** file_cluster_8: 14.893, file_cluster_7: 15.261, file_cluster_13: 15.283
- **Magnitude:** 4764.68 | **LOC:** 2841 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8852%), Tech Debt (31.1635%)
**Top Internal Functions/Classes:**
  * `rgb2gray` (Impact: 51.9)
  * `rgbx2gray` (Impact: 51.9)
  * `bgr2gray` (Impact: 51.9)
  * `bgrx2gray` (Impact: 51.9)
  * `rgb2hsv` (Impact: 47.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 493`, `structural_boundaries: 288`, `args: 115`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `state_mutation: 3534`, `duplicate_logic: 4`, `orphaned_logic: 32`
* *Architecture:* `io: 16`, `import: 3`
* *Defense:* `doc: 8`, `immutability_locks: 216`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vround_helper.hpp, saturate_cast.hpp, common.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/objdetect/src/qrcode.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.639 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_8: 14.639, file_cluster_13: 14.987, file_cluster_7: 15.03
- **Magnitude:** 4669.26 | **LOC:** 4744 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (68.2208%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `QRDetect::getQuadrilateral` (Impact: 98.5)
  * `ImplContour::decodeMulti` (Impact: 61.0)
  * `QRDetectMulti::computeTransformationPoin` (Impact: 52.8)
  * `QRDetect::extractVerticalLines` (Impact: 52.1)
  * `QRDecode::findTempPatternsAddingPoints` (Impact: 51.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 617`, `structural_boundaries: 217`, `args: 94`, `func_start: 95`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3426`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 10`, `orphaned_logic: 55`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 8`, `doc: 7`, `immutability_locks: 178`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` precomp.hpp, logger.hpp, limits, map, graphical_code_detector_impl.hpp, quirc.h, calib3d.hpp, array...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hal/riscv-rvv/src/imgproc/color.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.429 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.52 IQR)
- **Top Global Matches:** file_cluster_8: 14.429, file_cluster_11: 14.736, file_cluster_13: 14.778
- **Magnitude:** 4634.04 | **LOC:** 3160 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0207%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `Tab` (Impact: 51.6)
    * *Intent:* // the algorithm is copied from imgproc/src/color_lab.cpp, // in the function static bool createLabT...
  * `cvtBGRtoLab_f` (Impact: 51.4)
  * `cvtBGRtoMultiPlaneYUV` (Impact: 51.0)
    * *Intent:* // the algorithm is copied from imgproc/src/color_yuv.simd.cpp, // in the functor struct RGB8toYUV42...
  * `cvtMultiPlaneYUVtoBGR` (Impact: 45.7)
    * *Intent:* // the algorithm is copied from imgproc/src/color_yuv.simd.cpp, // in the functor struct YUV420sp2RG...
  * `cvtYUVtoBGR` (Impact: 38.5)
    * *Intent:* // the algorithm is copied from imgproc/src/color_yuv.simd.cpp, // in the functor struct YCrCb2RGB_f...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 385`, `structural_boundaries: 940`, `args: 265`, `func_start: 234`, `class_start: 35`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3318`, `duplicate_logic: 188`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` rvv_hal.hpp, limits
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/connectedcomponents.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.549 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.46 IQR)
- **Top Global Matches:** file_cluster_8: 14.549, file_cluster_11: 14.923, file_cluster_7: 14.928
- **Magnitude:** 4384.08 | **LOC:** 5800 | **CtrlFlow:** 90.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.0662%), Tech Debt (33.3331%)
**Top Internal Functions/Classes:**
  * `mergeLabels` (Impact: 53.2)
  * `mergeLabels` (Impact: 52.8)
  * `mergeLabels8Connectivity` (Impact: 20.2)
    * *Intent:* #undef condition_q
  * `cv::connectedComponentsWithStats` (Impact: 15.0)
  * `cv::connectedComponents` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1530`, `structural_boundaries: 159`, `args: 352`, `func_start: 48`, `class_start: 20`
* *Risk/State:* `state_mutation: 3996`, `dead_code: 4`, `duplicate_logic: 33`, `orphaned_logic: 1`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `doc: 29`, `immutability_locks: 416`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` precomp.hpp, ccl_bolelli_forest_lastline.inc.hpp, ccl_bolelli_forest.inc.hpp, vector, ccl_bolelli_forest_singleline.inc.hpp, ccl_bolelli_forest_firstline.inc.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/src/array.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.84 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.752 IQR)
- **Top Global Matches:** file_cluster_8: 14.84, file_cluster_7: 15.093, file_cluster_11: 15.169
- **Magnitude:** 4352.02 | **LOC:** 3255 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.4953%), Tech Debt (9.6996%)
**Top Internal Functions/Classes:**
  * `cvReshapeMatND` (Impact: 145.2)
  * `cvInitNArrayIterator` (Impact: 114.0)
  * `cvInitImageHeader` (Impact: 72.0)
  * `cvGetMat` (Impact: 70.7)
  * `cvScalarToRawData` (Impact: 68.4)
    * *Intent:* *data = mat->data.ptr;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 644`, `structural_boundaries: 100`, `args: 98`, `func_start: 70`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 11`, `state_mutation: 2551`, `planned_debt: 11`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `doc: 59`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `3rdparty/openjpeg/openjp2/ht_dec.c` (C) | Magnitude: 2596.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 2118, indent_spaces: 1746, bitwise_ops: 566, branch: 403
- `3rdparty/protobuf/src/google/protobuf/descriptor_database.h` (CPP) | Magnitude: 40.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 94, args: 44, immutability_locks: 38, state_mutation: 31
- `modules/videoio/misc/objc/ios/CvCamera2.h` (OBJECTIVE-C) | Magnitude: 82.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 50, explicit_casts: 28, api: 23, func_start: 22
- `modules/imgcodecs/src/bitstrm.hpp` (CPP) | Magnitude: 31.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 39, args: 17, class_start: 7
- `modules/calib3d/src/usac.hpp` (CPP) | Magnitude: 705.82 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 593, state_mutation: 586, indent_spaces: 371, immutability_locks: 306

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `3rdparty/openjpeg/openjp2/t2.c` (C) | Magnitude: 1316.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 875, indent_spaces: 769, pointers: 432, branch: 189
- `modules/gapi/misc/python/python_bridge.hpp` (CPP) | Magnitude: 200.44 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 123, structural_boundaries: 66, args: 47
- `modules/videoio/src/cap_obsensor/obsensor_uvc_stream_channel.cpp` (CPP) | Magnitude: 909.94 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 704, indent_spaces: 365, branch: 86, pointers: 81
- `modules/python/src2/typing_stubs_generation/generation.py` (PYTHON) | Magnitude: 332.4 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 357, branch: 93, structural_boundaries: 87, encapsulation: 52
- `modules/gapi/src/streaming/onevpl/accelerators/surface/surface.cpp` (CPP) | Magnitude: 64.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 43, indent_spaces: 28, structural_boundaries: 14, pointers: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `3rdparty/libjasper/jasper/jas_fix.h` (CPP) | Magnitude: 25.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 78, macros: 77, reflection_metaprogramming: 53, indent_spaces: 50
- `modules/core/src/opencl/split_merge.cl` (C) | Magnitude: 74.98 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 56, indent_spaces: 32, doc: 29, api: 14
- `samples/cpp/example_cmake/Makefile` (MAKEFILE) | Magnitude: 17.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 3, api: 2, state_mutation: 2, reflection_metaprogramming: 2
- `platforms/maven/opencv/scripts/execstack_check` (SHELL) | Magnitude: 17.8 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 7, state_mutation: 6, branch: 5, io: 5
- `modules/imgproc/src/opencl/filter2D.cl` (C) | Magnitude: 218.04 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 170, indent_spaces: 111, macros: 50, branch: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `3rdparty/openexr/Imath/ImathInterval.h` (CPP) | Magnitude: 88.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: state_mutation: 70, structural_boundaries: 59, doc: 50, indent_spaces: 34
- `3rdparty/libjasper/jas_stream.c` (C) | Magnitude: 1005.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 620, state_mutation: 550, pointers: 367, branch: 164
- `3rdparty/libjpeg-turbo/simd/arm/jdsample-neon.c` (C) | Magnitude: 376.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 248, indent_spaces: 229, api: 85, globals: 50
- `3rdparty/libjpeg-turbo/simd/arm/jidctfst-neon.c` (C) | Magnitude: 515.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 318, indent_spaces: 314, api: 166, globals: 163
- `modules/dnn/src/cuda4dnn/kernels/activation_eltwise.hpp` (CPP) | Magnitude: 22.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 14, state_mutation: 7, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `modules/python/src2/typing_stubs_generation/nodes/type_node.py` (PYTHON) | Magnitude: 541.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 565, structural_boundaries: 273, generics: 172, api: 124
- `modules/core/misc/objc/common/ArrayUtil.h` (OBJECTIVE-C) | Magnitude: 15.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, args: 1, func_start: 1, generics: 1
- `modules/python/src2/cv2_convert.hpp` (CPP) | Magnitude: 561.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 363, indent_spaces: 266, structural_boundaries: 212, immutability_locks: 99
- `modules/core/misc/objc/common/RotatedRect.h` (OBJECTIVE-C) | Magnitude: 83.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: explicit_casts: 14, macros: 13, func_start: 11, doc: 10
- `modules/core/include/opencv2/core/dualquaternion.inl.hpp` (CPP) | Magnitude: 298.5 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 259, structural_boundaries: 195, indent_spaces: 183, immutability_locks: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `modules/python/src2/hdr_parser.py` (PYTHON) | Magnitude: 948.28 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 896, branch: 347, state_mutation: 180, structural_boundaries: 99
- `modules/calib3d/src/usac/quality.cpp` (CPP) | Magnitude: 980.18 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 634, indent_spaces: 445, immutability_locks: 125, branch: 94
- `modules/ts/misc/report.py` (PYTHON) | Magnitude: 34.8 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, branch: 52, state_mutation: 18, io: 11
- `samples/dnn/js_face_recognition.html` (HTML) | Magnitude: 237.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 172, state_mutation: 76, structural_boundaries: 51, branch: 44
- `modules/objc/generator/gen_objc.py` (PYTHON) | Magnitude: 1677.06 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1339, branch: 571, state_mutation: 451, structural_boundaries: 284

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `modules/gapi/src/executor/gtbbexecutor.cpp` (CPP) | Magnitude: 294.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 192, structural_boundaries: 98, branch: 36
- `modules/core/include/opencv2/core/async.hpp` (CPP) | Magnitude: 52.68 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 30, structural_boundaries: 27, immutability_locks: 13
- `samples/cpp/tutorial_code/videoio/openni_orbbec_astra/openni_orbbec_astra.cpp` (CPP) | Magnitude: 86.2 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 50, concurrency: 32, branch: 28
- `modules/gapi/src/executor/gstreamingexecutor.cpp` (CPP) | Magnitude: 1825.64 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 765, state_mutation: 699, branch: 209, structural_boundaries: 175
- `modules/videoio/src/cap_obsensor/obsensor_stream_channel_v4l2.cpp` (CPP) | Magnitude: 429.34 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, state_mutation: 265, branch: 57, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `modules/gapi/src/api/render.cpp` (CPP) | Magnitude: 77.5 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 60, indent_spaces: 45, planned_debt: 21, immutability_locks: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `modules/core/src/opencl/cvtclr_dx.cl` (C) | Magnitude: 142.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 79, api: 51, doc: 29
- `modules/calib3d/src/sqpnp.hpp` (CPP) | Magnitude: 28.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 52, indent_spaces: 49, state_mutation: 25, immutability_locks: 24
- `modules/dnn/src/darknet/darknet_io.hpp` (CPP) | Magnitude: 31.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 58, indent_spaces: 33, structural_boundaries: 20, immutability_locks: 15
- `modules/imgproc/src/opencl/laplacian5.cl` (C) | Magnitude: 226.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 177, indent_spaces: 113, doc: 90, api: 40
- `modules/imgproc/src/opencl/gftt.cl` (C) | Magnitude: 145.7 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 106, indent_spaces: 74, doc: 29, api: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `modules/gapi/src/backends/fluid/gfluidbuffer_priv.hpp` (CPP) | Magnitude: 186.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 159, indent_spaces: 137, state_mutation: 113, immutability_locks: 82
- `modules/stitching/perf/opencl/perf_warpers.cpp` (CPP) | Magnitude: 57.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, doc: 46, state_mutation: 33, explicit_casts: 14
- `3rdparty/libwebp/src/dsp/alpha_processing_neon.c` (C) | Magnitude: 268.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 184, indent_spaces: 102, api: 40, immutability_locks: 28
- `samples/cpp/tutorial_code/gapi/doc_snippets/dynamic_graph_snippets.cpp` (CPP) | Magnitude: 77.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 58, indent_spaces: 43, structural_boundaries: 9, branch: 8
- `3rdparty/libtiff/tif_pixarlog.c` (C) | Magnitude: 1374.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1118, indent_spaces: 673, pointers: 173, branch: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `3rdparty/libjasper/jpc_t2enc.h` (C) | Magnitude: 22.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 12, pointers: 10, api: 7, import: 4
- `modules/imgproc/src/opencl/threshold.cl` (C) | Magnitude: 67.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 32, doc: 29, macros: 11
- `samples/winrt_universal/VideoCaptureXAML/video_capture_xaml/video_capture_xaml.Shared/App.xaml.h` (CPP) | Magnitude: 16.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, bitwise_ops: 8, structural_boundaries: 7, ownership: 6
- `modules/dnn/src/opencl/ocl4dnn_lrn.cl` (C) | Magnitude: 108.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 70, indent_spaces: 44, doc: 29, api: 22
- `3rdparty/openexr/IlmImf/ImfDeepImageStateAttribute.h` (CPP) | Magnitude: 17.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 50, structural_boundaries: 6, ownership: 5, generics: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `modules/imgproc/include/opencv2/imgproc.hpp` -> Churn: **92.51%** | Cog Load: 33.9216% | Debt: 81.6804%
- `modules/imgcodecs/src/grfmt_webp.cpp` -> Churn: **73.25%** | Cog Load: 52.522% | Debt: 38.335%
- `modules/videoio/src/cap_ffmpeg_impl.hpp` -> Churn: **69.08%** | Cog Load: 58.4551% | Debt: 21.9866%
- `hal/ipp/src/warp_ipp.cpp` -> Churn: **63.09%** | Cog Load: 91.8692% | Debt: 33.8922%
- `modules/dnn/src/onnx/onnx_importer.cpp` -> Churn: **62.83%** | Cog Load: 90.2811% | Debt: 92.5976%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `modules/core/src/ocl.cpp` -> **kallaballa** (100.0% isolated ownership) | Magnitude: 95471.86
- `modules/features2d/src/agast.cpp` -> **pratham-mcw** (100.0% isolated ownership) | Magnitude: 8433.36
- `modules/imgproc/src/smooth.simd.hpp` -> **Madan mohan Manokar** (100.0% isolated ownership) | Magnitude: 5307.36
- `modules/core/src/dxt.cpp` -> **eplankin** (100.0% isolated ownership) | Magnitude: 4208.52
- `modules/calib3d/src/fisheye.cpp` -> **MaximSmolskiy** (100.0% isolated ownership) | Magnitude: 3935.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `3rdparty/openexr/IlmImf/ImfHeader.h` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.9345%)
- `3rdparty/openexr/IlmImf/ImfAttribute.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 91.483%)
- `3rdparty/openexr/Imath/ImathVec.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `3rdparty/openexr/IlmImf/ImfXdr.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `modules/flann/include/opencv2/flann/kmeans_index.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `3rdparty/flatbuffers/include/flatbuffers/string.h` -> **Severity: 3309.3** (Blast Radius: 33.093 * Doc Risk: 100.0%)
- `3rdparty/flatbuffers/include/flatbuffers/vector.h` -> **Severity: 2626.7** (Blast Radius: 26.267 * Doc Risk: 100.0%)
- `3rdparty/libjpeg-turbo/src/jpeglib.h` -> **Severity: 1101.669** (Blast Radius: 11.017 * Doc Risk: 99.9972%)
- `3rdparty/libjpeg-turbo/simd/nasm/jsimdext.inc` -> **Severity: 600.954** (Blast Radius: 6.328 * Doc Risk: 94.9675%)
- `3rdparty/libtiff/tiffiop.h` -> **Severity: 458.9** (Blast Radius: 4.589 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
