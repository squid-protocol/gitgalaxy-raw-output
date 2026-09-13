# ARCHITECTURAL_BRIEF: opencv
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/opencv/opencv.git` |
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
| Total Artifacts | 7688 |
| Analyzed Artifacts (Scanned) | 5656 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2032 |
| Total LOC | 1418919 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 73.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1074 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 411 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 3387 | 993785 | 59.9% |
| C | 838 | 289574 | 14.8% |
| PYTHON | 371 | 40869 | 6.6% |
| JAVA | 204 | 25910 | 3.6% |
| PLAINTEXT | 181 | 6 | 3.2% |
| OBJECTIVE-C | 126 | 11349 | 2.2% |
| MARKDOWN | 109 | 0 | 1.9% |
| ASSEMBLY | 95 | 30704 | 1.7% |
| XML | 80 | 0 | 1.4% |
| JAVASCRIPT | 36 | 5690 | 0.6% |
| JSON | 33 | 2713 | 0.6% |
| SWIFT | 32 | 6125 | 0.6% |
| HTML | 31 | 2408 | 0.5% |
| SHELL | 26 | 982 | 0.5% |
| GROOVY | 19 | 672 | 0.3% |
| M4 | 17 | 658 | 0.3% |
| CSHARP | 12 | 592 | 0.2% |
| MAKEFILE | 10 | 629 | 0.2% |
| PROTO | 10 | 1165 | 0.2% |
| BATCH | 9 | 550 | 0.2% |
| YAML | 7 | 160 | 0.1% |
| GLSL | 6 | 701 | 0.1% |
| SCALA | 5 | 95 | 0.1% |
| KOTLIN | 3 | 145 | 0.1% |
| POWERSHELL | 2 | 350 | 0.0% |
| DOCKERFILE | 2 | 42 | 0.0% |
| PERL | 2 | 496 | 0.0% |
| CSS | 2 | 181 | 0.0% |
| PBTXT | 1 | 2368 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5366 | 94.9% |
| Unknown | 6 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 284 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2032*

**Composition by Extension & Reason:**
- `.jpg`: 579x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.png`: 443x Excluded (Explicitly Denied Extension: '.png')
- `.markdown`: 248x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 180x Excluded (Unsupported Extension: '.cmake'), 1x Unsupported Format (.cmake)
- `.html`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Documentation Signature)
- `no_extension`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Unsupported Format (.undeterminable), 7x Excluded (Unsupported Extension: '.appxmanifest')
- `.patch`: 46x Excluded (Unsupported Extension: '.patch')
- `.xml`: 3x Excluded (Massive Static Asset Blob: 24351 LOC), 3x Excluded (Static Asset Blob without Intent: 1506 LOC), 1x Excluded (Massive Static Asset Blob: 12214 LOC)
- `.cu`: 30x Unsupported Format (.cu), 2x Excluded (Unsupported Extension: '.cu')
- `.h`: 2x Excluded (Embedded Hex Payload: 37664 hex tokens in 9447 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 4666 LOC), 1x Excluded (Machine-Generated Source Code Signature: 180 LOC)
- `.gz`: 21x Excluded (Explicitly Denied Extension: '.gz')
- `.hpp`: 1x Excluded (Lexical Monotony: High structural repetition detected in 4496 LOC), 1x Excluded (Embedded Array/Matrix Payload: 14225 commas in 2019 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3442 LOC)
- `.xaml`: 21x Excluded (Unsupported Extension: '.xaml')
- `.cc`: 1x Excluded (Machine-Generated Source Code Signature: 11126 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2664 commas in 616 LOC), 1x Excluded (Monolithic Amalgamation: 34121 LOC exceeds safe regex boundaries)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31794 LOC exceeds safe regex boundaries), 1x Zero-Density Threshold (LOC: 166, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 31.2 | 19.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 56.2 | 68.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.5 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.6 | 0.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 46.7 | 23.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.7 | 2.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 80.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 238439 | 3809 | 106 | `3rdparty/openjpeg/openjp2/j2k.c` |
| cleanup | 1363 | 386 | 0 | `modules/java/test/android_test/src/org/opencv/test/OpenCVTestCase.java` |
| guards | 127590 | 3917 | 53 | `3rdparty/include/vulkan/vulkan_core.h` |
| danger | 12947 | 1649 | 5 | `3rdparty/include/vulkan/vulkan_core.h` |
| concurrency | 2153 | 341 | 0 | `modules/gapi/test/streaming/gapi_streaming_utils_test.cpp` |
| connectivity | 21048 | 2758 | 10 | `3rdparty/libtiff/tiffio.h` |
| io | 2161 | 445 | 0 | `platforms/android/build_sdk.py` |
| crypto | 3 | 3 | 0 | `modules/python/test/tests_common.py` |
| ipc | 128 | 46 | 0 | `modules/gapi/test/streaming/gapi_streaming_tests.cpp` |
| time | 92 | 41 | 0 | `hal/openvx/hal/openvx_hal.cpp` |
| serialization | 26 | 10 | 0 | `3rdparty/protobuf/src/google/protobuf/descriptor.cc` |
| regex | 269 | 63 | 0 | `modules/objc/generator/gen_objc.py` |
| events | 1393 | 200 | 0 | `modules/gapi/src/api/kernels_core.cpp` |
| tests | 15856 | 562 | 0 | `modules/core/test/test_mat.cpp` |
| docs | 16311 | 2020 | 4 | `3rdparty/openjpeg/openjp2/openjpeg.h` |
| debt | 9606 | 1629 | 4 | `hal/riscv-rvv/src/imgproc/color.cpp` |
| mutation | 475521 | 4173 | 220 | `3rdparty/libjpeg/jidctint.c` |
| dead_code | 20021 | 2770 | 9 | `modules/ts/src/ts_gtest.cpp` |
| credential | 21 | 13 | 0 | `modules/imgproc/src/hershey_fonts.cpp` |
| threat | 15217 | 2180 | 4 | `3rdparty/include/vulkan/vulkan_core.h` |
| ml_ai | 3641 | 487 | 0 | `3rdparty/libjpeg-turbo/simd/mips64/loongson-mmintrin.h` |
| ui | 542 | 99 | 0 | `modules/highgui/src/window_QT.h` |

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

1. **core.hpp** (`modules/core/include/opencv2/core.hpp`) — 353 inbound connections
2. **string.h** (`3rdparty/flatbuffers/include/flatbuffers/string.h`) — 335 inbound connections
3. **imgproc.hpp** (`modules/imgproc/include/opencv2/imgproc.hpp`) — 308 inbound connections
4. **highgui.hpp** (`modules/highgui/include/opencv2/highgui.hpp`) — 290 inbound connections
5. **vector.h** (`3rdparty/flatbuffers/include/flatbuffers/vector.h`) — 281 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ts_gtest.cpp** (`modules/ts/src/ts_gtest.cpp`) — 63 outbound dependencies
2. **system.cpp** (`modules/core/src/system.cpp`) — 46 outbound dependencies
3. **opj_includes.h** (`3rdparty/openjpeg/openjp2/opj_includes.h`) — 42 outbound dependencies
4. **descriptor.cc** (`3rdparty/protobuf/src/google/protobuf/descriptor.cc`) — 36 outbound dependencies
5. **parallel.cpp** (`modules/core/src/parallel.cpp`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `OAST_9_16` (@ `modules/features2d/src/agast.cpp`) -> Impact: **2006.5** | LOC: 1089
- `AGAST_7_12s` (@ `modules/features2d/src/agast.cpp`) -> Impact: **1390.0** | LOC: 1040
- `AGAST_7_12d` (@ `modules/features2d/src/agast.cpp`) -> Impact: **1365.0** | LOC: 1021
- `AGAST_5_8` (@ `modules/features2d/src/agast.cpp`) -> Impact: **952.1** | LOC: 762
  * *Intent:* #if (defined __i386__ || defined(_M_IX86) || defined __x86_64__ || defined(_M_X64) || defined(_M_ARM64) || defined(__aarch64__) || defined(__arm__))
- `opj_t1_ht_decode_cblk` (@ `3rdparty/openjpeg/openjp2/ht_dec.c`) -> Impact: **868.2** | LOC: 1525
  * *Intent:* //************************************************************************/ /** @brief Decodes one codeblock, processing the cleanup, siginificance * ...
- `copyIntoDeepFrameBuffer` (@ `3rdparty/openexr/IlmImf/ImfMisc.cpp`) -> Impact: **786.5** | LOC: 700
- `operator()` (@ `modules/imgproc/src/connectedcomponents.cpp`) -> Impact: **784.0** | LOC: 788
- `packInputData` (@ `modules/dnn/src/layers/cpu_kernels/convolution.cpp`) -> Impact: **782.2** | LOC: 498
- `TIFFFetchNormalTag` (@ `3rdparty/libtiff/tif_dirread.c`) -> Impact: **772.2** | LOC: 1365
  * *Intent:* /* * Fetch a tag that is not handled by special case code. */
- `Reflection::Swap` (@ `3rdparty/protobuf/src/google/protobuf/generated_message_reflection.cc`) -> Impact: **614.5** | LOC: 1413

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `modules/imgproc/src` | 102 | 93006.64 | 54.82% | 22.5% |
| `modules/core/src` | 109 | 81706.38 | 56.74% | 32.71% |
| `3rdparty/libtiff` | 60 | 38916.5 | 45.88% | 30.29% |
| `3rdparty/openjpeg/openjp2` | 66 | 36181.14 | 27.46% | 35.41% |
| `modules/calib3d/src` | 47 | 30510.22 | 47.84% | 19.54% |
| `3rdparty/libjasper` | 63 | 28655.66 | 31.45% | 25.52% |
| `hal/carotene/src` | 57 | 28326.04 | 52.65% | 10.78% |
| `modules/videoio/src` | 63 | 26472.56 | 43.0% | 44.38% |
| `3rdparty/libpng` | 24 | 24791.64 | 46.89% | 37.21% |
| `3rdparty/openexr/IlmImf` | 200 | 23374.4 | 14.9% | 36.43% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `3rdparty/openjpeg/openjp2/jp2.h` -> **100.0%** Exposure
- `3rdparty/openjpeg/openjp2/pi.h` -> **100.0%** Exposure
- `samples/hal/c_hal/impl.c` -> **100.0%** Exposure
- `3rdparty/openexr/IlmImf/ImfIO.cpp` -> **100.0%** Exposure
- `3rdparty/openexr/Imath/ImathLimits.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `3rdparty/cpufeatures/cpu-features.c` -> **100.0%** Exposure
- `3rdparty/cpufeatures/cpu-features.h` -> **100.0%** Exposure
- `3rdparty/libjasper/jas_cm.c` -> **100.0%** Exposure
- `3rdparty/libjasper/jas_getopt.c` -> **100.0%** Exposure
- `3rdparty/libjasper/jas_icc.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `modules/ts/src/ts_gtest.cpp` -> **255** Orphaned Functions | **10** Duplicates
- `3rdparty/protobuf/src/google/protobuf/descriptor.cc` -> **226** Orphaned Functions | **0** Duplicates
- `modules/highgui/src/window_QT.cpp` -> **197** Orphaned Functions | **0** Duplicates
- `modules/core/src/ocl.cpp` -> **178** Orphaned Functions | **2** Duplicates
- `modules/imgproc/misc/java/test/ImgprocTest.java` -> **172** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `66` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20431` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `modules/videoio/src/cap_obsensor_liborbbec.cpp` (CPP) -> Cumulative Risk: **733.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 245.2 | **LOC:** 272 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Safety Score (90.4914%)
- **Heaviest Functions:** `VideoCapture_obsensor::getProperty` (Impact: 53.0), `VideoCapture_obsensor::VideoCapture_obsensor` (Impact: 37.0), `VideoCapture_obsensor::retrieveFrame` (Impact: 22.7)

### 2. `samples/android/15-puzzle/src/org/opencv/samples/puzzle15/Puzzle15Processor.java` (JAVA) -> Cumulative Risk: **729.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 195.38 | **LOC:** 196 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.2313%)
- **Heaviest Functions:** `deliverTouchEvent` (Impact: 21.1), `puzzleFrame` (Impact: 13.3), `prepareGameSize` (Impact: 7.8)

### 3. `samples/python/digits.py` (PYTHON) -> Cumulative Risk: **727.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 164.92 | **LOC:** 195 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.708%)
- **Heaviest Functions:** `evaluate_model` (Impact: 9.9), `split2d` (Impact: 6.4), `preprocess_hog` (Impact: 5.3)

### 4. `modules/java/generator/android-24/java/org/opencv/android/NativeCameraView.java` (JAVA) -> Cumulative Risk: **722.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 185.48 | **LOC:** 231 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9937%), Cognitive Load (94.1027%)
- **Heaviest Functions:** `initializeCamera` (Impact: 42.0), `synchronized` (Impact: 25.6), `run` (Impact: 4.5)

### 5. `platforms/ios/build_visionos_framework.py` (PYTHON) -> Cumulative Risk: **717.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 80.22 | **LOC:** 117 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9939%)
- **Heaviest Functions:** `getBuildCommand` (Impact: 6.6), `checkCMakeVersion` (Impact: 2.9), `getCMakeArgs` (Impact: 2.3)

### 6. `samples/cpp/tutorial_code/calib3d/real_time_pose_estimation/src/RobustMatcher.cpp` (CPP) -> Cumulative Risk: **715.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 101.1 | **LOC:** 155 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.997%), Tech Debt (99.9965%)
- **Heaviest Functions:** `RobustMatcher::symmetryTest` (Impact: 25.6), `RobustMatcher::fastRobustMatch` (Impact: 13.9), `RobustMatcher::robustMatch` (Impact: 9.0)

### 7. `modules/video/src/tracking/detail/tracking_online_mil.cpp` (CPP) -> Cumulative Risk: **713.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 317.44 | **LOC:** 357 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5398%)
- **Heaviest Functions:** `ClfMilBoost::update` (Impact: 30.4), `ClfOnlineStump::update` (Impact: 23.2), `ClfMilBoost::classify` (Impact: 13.7)

### 8. `modules/videoio/misc/objc/ios/CvVideoCamera2.mm` (OBJECTIVE-C) -> Cumulative Risk: **712.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 404.84 | **LOC:** 576 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `captureOutput` (Impact: 63.5), `adjustLayoutToInterfaceOrientation` (Impact: 27.2), `layoutPreviewLayer` (Impact: 22.1)

### 9. `modules/js/src/loader.js` (JAVASCRIPT) -> Cumulative Risk: **712.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 129.72 | **LOC:** 101 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (98.8865%)
- **Heaviest Functions:** `loadOpenCV` (Impact: 83.0)

### 10. `modules/videoio/src/cap_obsensor/obsensor_stream_channel_v4l2.cpp` (CPP) -> Cumulative Risk: **711.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 251.84 | **LOC:** 381 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9976%), Concurrency (94.4878%)
- **Heaviest Functions:** `V4L2Context::queryUvcDeviceInfoList` (Impact: 25.9), `xioctl` (Impact: 14.8), `V4L2StreamChannel::start` (Impact: 13.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `3rdparty/openjpeg/openjp2/j2k.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10182.02 | **LOC:** 13596 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.0415%), Tech Debt (23.1751%)
**Top Internal Functions/Classes:**
  * `opj_j2k_setup_encoder` (Impact: 426.9)
  * `opj_j2k_is_imf_compliant` (Impact: 307.9)
  * `opj_j2k_read_tile_header` (Impact: 283.8)
  * `opj_j2k_read_siz` (Impact: 188.9)
    * *Intent:* /** * Reads a SIZ marker (image and tile size) * @param p_j2k the jpeg2000 file codec. * @param p_he...
  * `opj_j2k_read_sot` (Impact: 122.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1629 instances
* *State Mutation (weighted view):* 5442
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1675`, `structural_boundaries: 894`, `args: 345`, `func_start: 173`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 2184`, `dead_code: 12`, `planned_debt: 16`, `fragile_debt: 37`, `unreferenced_by_name: 21`
* *Architecture:* `api: 32`, `import: 1`
* *Defense:* `safety: 298`, `doc: 140`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` opj_includes.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/libtiff/tif_dirread.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7975.08 | **LOC:** 8448 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.7941%), Tech Debt (11.746%)
**Top Internal Functions/Classes:**
  * `TIFFFetchNormalTag` (Impact: 772.2)
    * *Intent:* /* * Fetch a tag that is not handled by special case code. */
  * `TIFFReadDirectory` (Impact: 368.1)
    * *Intent:* } /*-- CalcFinalIFDdatasizeReading() --*/ /* * Read the next TIFF directory from a file and convert ...
  * `TIFFFetchDirectory` (Impact: 162.1)
    * *Intent:* /* * Read IFD structure from the specified offset. If the pointer to * nextdiroff variable has been ...
  * `TIFFReadDirEntryFloatArray` (Impact: 135.8)
  * `TIFFReadDirEntryDoubleArray` (Impact: 129.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1201 instances
* *State Mutation (weighted view):* 3662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1845`, `structural_boundaries: 1070`, `args: 213`, `func_start: 120`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 1260`, `dead_code: 5`, `fragile_debt: 12`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 140`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` float.h, limits.h, stdlib.h, string.h, tiffconf.h, tiffiop.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/libspng/spng.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7542.42 | **LOC:** 6981 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.4309%), Tech Debt (37.9034%)
**Top Internal Functions/Classes:**
  * `spng_decode_image` (Impact: 391.8)
  * `read_non_idat_chunks` (Impact: 385.1)
  * `write_chunks_before_idat` (Impact: 157.1)
  * `spng_strerror` (Impact: 143.3)
  * `spng_encode_image` (Impact: 141.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1132 instances
* *State Mutation (weighted view):* 3695
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1699`, `structural_boundaries: 1214`, `args: 259`, `func_start: 171`, `class_start: 85`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1431`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 59`
* *Architecture:* `io: 2`, `api: 65`, `import: 14`
* *Defense:* `safety: 134`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` arm64_neon.h, arm_neon.h, immintrin.h, inttypes.h, limits.h, math.h, miniz.h, pthread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/features2d/src/agast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6513.86 | **LOC:** 8200 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.1992%), Tech Debt (7.9867%)
**Top Internal Functions/Classes:**
  * `OAST_9_16` (Impact: 2006.5)
  * `AGAST_7_12s` (Impact: 1390.0)
  * `AGAST_7_12d` (Impact: 1365.0)
  * `AGAST_5_8` (Impact: 952.1)
    * *Intent:* #if (defined __i386__ || defined(_M_IX86) || defined __x86_64__ || defined(_M_X64) || defined(_M_ARM...
  * `AGAST` (Impact: 125.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5377`, `structural_boundaries: 1710`, `args: 33`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 138`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` agast_score.hpp, precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/traincascade/old_ml_tree.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5584.32 | **LOC:** 4154 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.9138%), Tech Debt (56.3455%)
**Top Internal Functions/Classes:**
  * `CvDTreeTrainData::set_data` (Impact: 484.4)
  * `CvDTree::predict` (Impact: 115.7)
  * `CvDTree::find_split_cat_class` (Impact: 107.3)
  * `CvDTreeTrainData::get_vectors` (Impact: 82.4)
  * `CvDTree::split_node_data` (Impact: 82.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1117 instances
* *State Mutation (weighted view):* 3473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 837`, `structural_boundaries: 98`, `args: 115`, `func_start: 80`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1239`, `dead_code: 8`, `planned_debt: 3`, `unreferenced_by_name: 59`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 165`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, old_ml_precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/ts/src/ts_func.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5560.94 | **LOC:** 3322 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.3086%), Tech Debt (18.7429%)
**Top Internal Functions/Classes:**
  * `threshold` (Impact: 190.8)
  * `cmpEps` (Impact: 160.4)
    * *Intent:* #define CMP_EPS_OK 0 #define CMP_EPS_BIG_DIFF -1 #define CMP_EPS_INVALID_TEST_DATA -2 // there is Na...
  * `muldiv` (Impact: 96.2)
  * `copyMakeBorder` (Impact: 80.0)
  * `transform` (Impact: 77.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 849 instances
* *State Mutation (weighted view):* 2559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1065`, `structural_boundaries: 172`, `args: 99`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 861`, `dead_code: 1`, `unreferenced_by_name: 30`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 406`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, limits.h, types_c.h, precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/libjasper/jpc_qmfb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5445.52 | **LOC:** 3145 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9832%), Tech Debt (8.2699%)
**Top Internal Functions/Classes:**
  * `jpc_ns_fwdlift_colres` (Impact: 96.1)
  * `jpc_ns_invlift_colres` (Impact: 96.1)
  * `jpc_ns_fwdlift_colgrp` (Impact: 88.6)
  * `jpc_ns_invlift_colgrp` (Impact: 88.6)
  * `jpc_ns_fwdlift_col` (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1383 instances
* *State Mutation (weighted view):* 4168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 50`, `args: 134`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 1402`, `unreferenced_by_name: 2`
* *Architecture:* `api: 54`, `import: 7`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assert.h, jas_fix.h, jas_malloc.h, jas_math.h, jpc_math.h, jpc_qmfb.h, jpc_tsfb.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hal/riscv-rvv/include/types.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5260.71 | **LOC:** 879 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7856%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 397`, `args: 351`, `func_start: 79`, `class_start: 16`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` riscv_vector.h, type_traits
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/imgproc/src/histogram.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5206.54 | **LOC:** 3658 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.8008%), Tech Debt (15.5726%)
**Top Internal Functions/Classes:**
  * `calcHist_` (Impact: 335.7)
    * *Intent:* ////////////////////////////////// C A L C U L A T E H I S T O G R A M /////////////////////////////...
  * `calcHist_8u` (Impact: 170.3)
  * `calcBackProj_` (Impact: 157.0)
  * `cv::calcHist` (Impact: 139.4)
    * *Intent:* #endif
  * `cv::compareHist` (Impact: 116.8)
    * *Intent:* ////////////////// C O M P A R E H I S T O G R A M S ////////////////////////
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 866 instances
* *State Mutation (weighted view):* 2692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 841`, `structural_boundaries: 121`, `args: 83`, `func_start: 50`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 960`, `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 3`, `doc: 6`, `sync_locks: 5`, `immutability_locks: 239`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` opencl_kernels_imgproc.hpp, intrin.hpp, ovx_defs.hpp, tls.hpp, precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/color_lab.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5157.4 | **LOC:** 4854 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.4784%), Tech Debt (28.5767%)
**Top Internal Functions/Classes:**
  * `cvtBGRtoLab` (Impact: 167.5)
    * *Intent:* // 8u, 32f
  * `cvtLabtoBGR` (Impact: 160.6)
    * *Intent:* // 8u, 32f
  * `cvtBGRtoXYZ` (Impact: 91.0)
  * `cvtXYZtoBGR` (Impact: 87.8)
  * `operator()` (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 857 instances
* *State Mutation (weighted view):* 3047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 658`, `structural_boundaries: 182`, `args: 285`, `func_start: 87`, `class_start: 24`
* *Risk/State:* `state_mutation: 1333`, `dead_code: 13`, `planned_debt: 3`, `duplicate_logic: 11`, `unreferenced_by_name: 12`
* *Architecture:* `import: 5`
* *Defense:* `doc: 4`, `immutability_locks: 278`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` color.hpp, opencl_kernels_imgproc.hpp, intrin.hpp, softfloat.hpp, precomp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/libpng/pngrtran.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5128.22 | **LOC:** 5160 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.8686%), Tech Debt (17.9362%)
**Top Internal Functions/Classes:**
  * `png_do_compose` (Impact: 322.8)
    * *Intent:* /* Replace any alpha or transparency with the supplied background color. * "background" is already i...
  * `png_set_quantize` (Impact: 183.6)
  * `png_init_read_transformations` (Impact: 176.2)
    * *Intent:* #endif /* READ_GAMMA */
  * `png_do_read_transformations` (Impact: 120.6)
    * *Intent:* #endif /* READ_QUANTIZE */ /* Transform the row. The order of transformations is significant, * and ...
  * `png_do_expand` (Impact: 111.2)
    * *Intent:* /* If the bit depth < 8, it is expanded to 8. Also, if the already * expanded transparency value is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 990 instances
* *State Mutation (weighted view):* 3166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 147`, `args: 75`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `state_mutation: 1186`, `dead_code: 11`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` arm64_neon.h, arm_neon.h, pngpriv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/protobuf/src/google/protobuf/descriptor.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5068.02 | **LOC:** 8026 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.6204%), Tech Debt (97.0801%)
**Top Internal Functions/Classes:**
  * `DescriptorBuilder::BuildFieldOrExtension` (Impact: 239.6)
  * `DescriptorBuilder::OptionInterpreter::SetOptionValue` (Impact: 158.2)
  * `DescriptorBuilder::CrossLinkField` (Impact: 111.7)
  * `DescriptorBuilder::BuildFileImpl` (Impact: 94.2)
  * `DescriptorBuilder::OptionInterpreter::InterpretSingleOption` (Impact: 82.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 536 instances
* *State Mutation (weighted view):* 1713
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1387`, `structural_boundaries: 846`, `args: 478`, `func_start: 348`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 641`, `dead_code: 16`, `planned_debt: 12`, `fragile_debt: 5`, `unreferenced_by_name: 226`
* *Architecture:* `api: 10`, `import: 36`
* *Defense:* `safety: 13`, `sync_locks: 11`, `immutability_locks: 800`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` algorithm, array, functional, any.h, descriptor.h, descriptor.pb.h, descriptor_database.h, dynamic_message.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/src/dxt.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5009.7 | **LOC:** 4722 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2641%), Tech Debt (14.6041%)
**Top Internal Functions/Classes:**
  * `DFT` (Impact: 144.2)
    * *Intent:* // mixed-radix complex discrete Fourier transform: double-precision version
  * `DFTInit` (Impact: 128.7)
  * `init` (Impact: 119.5)
  * `init` (Impact: 102.3)
  * `ippi_DCT_32f` (Impact: 86.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 837 instances
* *State Mutation (weighted view):* 2828
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 793`, `structural_boundaries: 366`, `args: 171`, `func_start: 123`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 1154`, `dead_code: 3`, `planned_debt: 4`, `unreferenced_by_name: 17`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `doc: 3`, `immutability_locks: 282`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` map, opencl_kernels_core.hpp, opencl_clfft.hpp, opencl_core.hpp, precomp.hpp
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/imgproc/src/resize.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4649.58 | **LOC:** 4261 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.1587%), Tech Debt (9.3516%)
**Top Internal Functions/Classes:**
  * `resize` (Impact: 288.9)
  * `ocl_resize` (Impact: 127.1)
  * `ipp_resize` (Impact: 120.5)
    * *Intent:* #endif
  * `operator()` (Impact: 90.7)
  * `resize_bitExact` (Impact: 67.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 897 instances
* *State Mutation (weighted view):* 2874
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 490`, `args: 384`, `func_start: 101`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1080`, `dead_code: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 327`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fixedpoint.inl.hpp, hal_replacement.hpp, opencl_kernels_imgproc.hpp, intrin.hpp, ovx_defs.hpp, softfloat.hpp, buffer_area.private.hpp, precomp.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/objdetect/src/qrcode.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4410.12 | **LOC:** 4744 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (69.4194%), Tech Debt (61.7186%)
**Top Internal Functions/Classes:**
  * `QRDetect::getQuadrilateral` (Impact: 98.5)
  * `QRDetectMulti::findNumberLocalizationPoints` (Impact: 80.1)
  * `ImplContour::decodeMulti` (Impact: 61.0)
  * `QRDecode::findTempPatternsAddingPoints` (Impact: 51.5)
  * `QRDetectMulti::ParallelSearch::operator()` (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 828 instances
* *State Mutation (weighted view):* 2620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 313`, `args: 142`, `func_start: 137`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 964`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 78`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 8`, `doc: 4`, `immutability_locks: 294`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` array, cmath, graphical_code_detector_impl.hpp, limits, map, calib3d.hpp, logger.hpp, objdetect.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/src/ocl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4390.78 | **LOC:** 7665 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.2052%), Tech Debt (86.4381%)
**Top Internal Functions/Classes:**
  * `selectOpenCLDevice` (Impact: 151.0)
  * `Kernel::Impl::run` (Impact: 84.0)
  * `convertFromImage` (Impact: 67.7)
    * *Intent:* /* // Convert OpenCL image2d_t memory to UMat */
  * `checkContinuous` (Impact: 65.6)
  * `deallocate_` (Impact: 64.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 551 instances
* *State Mutation (weighted view):* 1904
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1177`, `structural_boundaries: 700`, `args: 507`, `func_start: 402`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 86`, `high_risk_execution: 1`, `state_mutation: 802`, `dead_code: 6`, `planned_debt: 11`, `duplicate_logic: 2`, `unreferenced_by_name: 178`
* *Architecture:* `io: 7`, `api: 15`, `import: 27`
* *Defense:* `safety: 72`, `doc: 13`, `sync_locks: 37`, `immutability_locks: 487`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` deque, fstream, inttypes.h, list, map, ocl_disabled.impl.hpp, opencl_kernels_core.hpp, bufferpool.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/ts/src/ts_gtest.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4383.46 | **LOC:** 11449 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8534%), Tech Debt (98.5461%)
**Top Internal Functions/Classes:**
  * `IsValidUTF8` (Impact: 55.4)
  * `PrintAsCharLiteralTo` (Impact: 45.7)
    * *Intent:* // Prints a wide or narrow char c as a character literal without the // quotes, escaping it when nec...
  * `CreateUnifiedDiff` (Impact: 45.0)
    * *Intent:* // Create a list of diff hunks in Unified diff format. // Each hunk has a header generated by PrintH...
  * `DefaultDeathTestFactory::Create` (Impact: 42.1)
    * *Intent:* # endif // !GTEST_OS_WINDOWS // Creates a concrete DeathTest-derived class that depends on the // --...
  * `XmlUnitTestResultPrinter::EscapeXml` (Impact: 41.9)
    * *Intent:* // Returns an XML-escaped copy of the input string str. If is_attribute // is true, the text is mean...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 355 instances
* *Amplified Sql Injection:* 2 instances
* *Memory Alloc (weighted view):* 41
* *State Mutation (weighted view):* 1162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1370`, `structural_boundaries: 1098`, `args: 670`, `func_start: 619`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 6`, `state_mutation: 452`, `dead_code: 26`, `planned_debt: 2`, `fragile_debt: 26`, `duplicate_logic: 10`, `unreferenced_by_name: 255`
* *Architecture:* `io: 5`, `api: 36`, `import: 39`
* *Defense:* `safety: 7`, `doc: 3`, `test: 18`, `sync_locks: 32`, `immutability_locks: 1100`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` failure_signal_handler.h, stacktrace.h, symbolize.h, str_cat.h, algorithm, inet.h, cctype, climits...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `3rdparty/openjpeg/openjp2/dwt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4089.2 | **LOC:** 3980 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.3532%), Tech Debt (34.531%)
**Top Internal Functions/Classes:**
  * `opj_dwt_encode_and_deinterleave_v` (Impact: 157.0)
    * *Intent:* /* Forward 5-3 transform, for the vertical pass, processing cols columns */ /* where cols <= NB_ELTS...
  * `opj_dwt_decode_partial_1_parallel` (Impact: 101.9)
    * *Intent:* #define OPJ_S_off(i,off) a[(OPJ_UINT32)(i)*2*4+off] #define OPJ_D_off(i,off) a[(1+(OPJ_UINT32)(i)*2)...
  * `opj_dwt_decode_tile_97` (Impact: 73.1)
    * *Intent:* /* <summary> */ /* Inverse 9-7 wavelet transform in 2-D. */ /* </summary> */...
  * `opj_dwt_encode_procedure` (Impact: 64.9)
    * *Intent:* /* <summary> */ /* Forward 5-3 wavelet transform in 2-D. */ /* </summary> */...
  * `opj_dwt_decode_tile` (Impact: 58.1)
    * *Intent:* /* <summary> */ /* Inverse wavelet transform in 2-D. */ /* </summary> */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 784 instances
* *State Mutation (weighted view):* 2566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 523`, `structural_boundaries: 173`, `args: 154`, `func_start: 62`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 998`, `dead_code: 2`, `fragile_debt: 22`, `unreferenced_by_name: 6`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 46`, `doc: 18`, `immutability_locks: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, emmintrin.h, immintrin.h, opj_includes.h, tmmintrin.h, xmmintrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/core/src/matmul.simd.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4084.66 | **LOC:** 2630 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9281%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gemmImpl` (Impact: 417.6)
  * `GEMMSingleMul` (Impact: 221.2)
  * `MulTransposedR` (Impact: 95.3)
    * *Intent:* #if !defined(CV_MULTRANSPOSED_BASELINE_ONLY) || defined(CV_CPU_BASELINE_MODE) /*********************...
  * `getMulTransposedFunc` (Impact: 76.5)
  * `perspectiveTransform_` (Impact: 73.0)
    * *Intent:* /****************************************************************************************\ * Perspec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 743 instances
* *State Mutation (weighted view):* 2357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 142`, `args: 86`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 871`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`, `immutability_locks: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` precomp.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `hal/ipp/src/warp_ipp.cpp` -> Churn: **77.55%** | Cog Load: 58.0365% | Debt: 21.1709%
- `modules/dnn/src/onnx/onnx_importer.cpp` -> Churn: **77.23%** | Cog Load: 68.8442% | Debt: 17.5391%
- `modules/imgcodecs/src/utils.cpp` -> Churn: **73.33%** | Cog Load: 69.2287% | Debt: 0.0%
- `modules/videoio/src/cap_msmf.cpp` -> Churn: **65.71%** | Cog Load: 74.0722% | Debt: 39.0088%
- `modules/imgcodecs/src/grfmt_bmp.cpp` -> Churn: **64.5%** | Cog Load: 79.9948% | Debt: 43.507%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `3rdparty/libtiff/tif_dirread.c` -> **Kumataro** (100.0% isolated ownership) | Magnitude: 7975.08
- `3rdparty/libpng/pngrtran.c` -> **Alexander Smorkalov** (100.0% isolated ownership) | Magnitude: 5128.22
- `apps/pattern-tools/svgfig.py` -> **Alexander Smorkalov** (100.0% isolated ownership) | Magnitude: 3854.42
- `modules/dnn/src/layers/cpu_kernels/convolution.cpp` -> **Jie Pan** (100.0% isolated ownership) | Magnitude: 3592.54
- `modules/imgproc/src/smooth.simd.hpp` -> **Madan mohan Manokar** (100.0% isolated ownership) | Magnitude: 3566.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `modules/core/include/opencv2/core/utility.hpp` -> **Severity: 0.074** (Bridge: 0.0007 * Flux: 99.5502%)
- `modules/core/include/opencv2/core/base.hpp` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 99.9738%)
- `modules/core/include/opencv2/core/cvdef.h` -> **Severity: 0.034** (Bridge: 0.0006 * Flux: 61.7204%)
- `modules/core/include/opencv2/core/types.hpp` -> **Severity: 0.032** (Bridge: 0.0005 * Flux: 62.3308%)
- `modules/flann/include/opencv2/flann/random.h` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.9624%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `3rdparty/flatbuffers/include/flatbuffers/vector.h` -> **Severity: 2661.1** (Blast Radius: 26.611 * Doc Risk: 100.0%)
- `3rdparty/flatbuffers/include/flatbuffers/string.h` -> **Severity: 2072.2** (Blast Radius: 20.722 * Doc Risk: 100.0%)
- `modules/core/include/opencv2/core/cvdef.h` -> **Severity: 1954.0** (Blast Radius: 24.425 * Doc Risk: 80.0%)
- `3rdparty/flatbuffers/include/flatbuffers/base.h` -> **Severity: 1924.371** (Blast Radius: 20.724 * Doc Risk: 92.8571%)
- `modules/core/src/algorithm.cpp` -> **Severity: 1474.7** (Blast Radius: 14.747 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
