# ARCHITECTURAL_BRIEF: tensorflow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/tensorflow` |
| **Timestamp** | `2026-08-03T21:39:41.321793+00:00` |
| **Scan Duration** | `67.13s` |
| **Git Branch** | `master` |
| **Git Commit** | `c21c40c048e9b35d032d31ce41809c2cadeb8fca` |
| **Git Remote** | `https://github.com/tensorflow/tensorflow.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19627 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 35746 |
| Analyzed Artifacts (Scanned) | 20498 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15248 |
| Total LOC | 1979629 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.3% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0938 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 603 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 8343 | 1071004 | 40.7% |
| PBTXT | 7579 | 472124 | 37.0% |
| PYTHON | 1778 | 307158 | 8.7% |
| MLIR | 912 | 60874 | 4.4% |
| MARKDOWN | 695 | 0 | 3.4% |
| SHELL | 198 | 9057 | 1.0% |
| PROTO | 194 | 5879 | 0.9% |
| JAVA | 175 | 17743 | 0.9% |
| BINARY_THREAT | 150 | 150 | 0.7% |
| TD | 117 | 21891 | 0.6% |
| OBJECTIVE-C | 70 | 4478 | 0.3% |
| XML | 69 | 4 | 0.3% |
| PLAINTEXT | 63 | 0 | 0.3% |
| DOCKERFILE | 37 | 1278 | 0.2% |
| JSON | 30 | 1743 | 0.1% |
| GO | 22 | 2044 | 0.1% |
| SWIFT | 17 | 1099 | 0.1% |
| BATCH | 12 | 400 | 0.1% |
| YAML | 9 | 613 | 0.0% |
| MAKEFILE | 9 | 1144 | 0.0% |
| GROOVY | 5 | 25 | 0.0% |
| M4 | 3 | 73 | 0.0% |
| PERL | 2 | 152 | 0.0% |
| CSV | 2 | 229 | 0.0% |
| RUBY | 2 | 8 | 0.0% |
| C | 2 | 39 | 0.0% |
| CSHARP | 2 | 273 | 0.0% |
| HTML | 1 | 147 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.848`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 12703 | 62.0% |
| file_cluster_13 | 6463 | 31.5% |
| Unknown | 150 | 0.7% |
| file_cluster_16 | 132 | 0.6% |
| file_cluster_9 | 81 | 0.4% |
| file_cluster_0 | 58 | 0.3% |
| file_cluster_12 | 57 | 0.3% |
| file_cluster_11 | 34 | 0.2% |
| file_cluster_4 | 24 | 0.1% |
| file_cluster_7 | 16 | 0.1% |
| file_cluster_6 | 9 | 0.0% |
| file_cluster_17 | 4 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 763 | 3.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15248*

**Composition by Extension & Reason:**
- `.cc`: 5620x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 141 LOC), 1x Excluded (Machine-Generated Source Code Signature: 187 LOC)
- `.h`: 2647x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 71 LOC), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC)
- `no_extension`: 1289x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Excluded (Binary Format Detected), 77x Unsupported Format (.undeterminable)
- `.py`: 1557x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 320 LOC), 1x Excluded (Machine-Generated Source Code Signature: 401 LOC)
- `.md`: 529x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2367 LOC), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC)
- `.mlir`: 444x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 4x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.hlo`: 281x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbtxt`: 203x Excluded: Neighborhood Micro-Mass Limit Exceeded, 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.html`: 233x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 255138 LOC exceeds safe regex boundaries)
- `.bzl`: 222x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 175 LOC), 1x Excluded (Machine-Generated Source Code Signature: 156 LOC)
- `.png`: 143x Excluded (Explicitly Denied Extension: '.png')
- `.proto`: 139x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC)
- `.build`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.build)
- `.tmpl`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.patch)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 23.4 | 8.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.0 | 0.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 34.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 42.4 | 28.6 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ci/official/utilities/generate_index_html.sh` (Hits: 133)
- `ci/official/utilities/code_check_full.bats` (Hits: 85)
- `tensorflow/tools/tf_sig_build_dockerfiles/devel.usertools/code_check_full.bats` (Hits: 84)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **string.bin** (`tensorflow/lite/java/src/testdata/string.bin`) — 2379 inbound connections
2. **op_kernel.h** (`tensorflow/core/framework/op_kernel.h`) — 940 inbound connections
3. **tensor.h** (`tensorflow/core/framework/tensor.h`) — 777 inbound connections
4. **types.h** (`tensorflow/core/platform/types.h`) — 712 inbound connections
5. **status.h** (`tensorflow/core/platform/status.h`) — 642 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **graph_to_tf_executor.cc** (`tensorflow/compiler/mlir/tf2xla/api/v2/graph_to_tf_executor.cc`) — 117 outbound dependencies
2. **flatbuffer_export.cc** (`tensorflow/compiler/mlir/lite/flatbuffer_export.cc`) — 116 outbound dependencies
3. **import_model.cc** (`tensorflow/compiler/mlir/tensorflow/translate/import_model.cc`) — 111 outbound dependencies
4. **graph_executor.cc** (`tensorflow/core/tfrt/graph_executor/graph_executor.cc`) — 104 outbound dependencies
5. **flatbuffer_import.cc** (`tensorflow/compiler/mlir/lite/flatbuffer_import.cc`) — 95 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pool` (@ `tensorflow/python/ops/nn_ops.py`) -> Impact: **7486.3** | LOC: 2301
- `split` (@ `tensorflow/python/ops/array_ops.py`) -> Impact: **4494.4** | LOC: 1412
- `is_uniform` (@ `tensorflow/python/ops/ragged/dynamic_ragged_shape.py`) -> Impact: **4166.1** | LOC: 1847
- `_shape_invariant_to_type_spec` (@ `tensorflow/python/ops/control_flow_ops.py`) -> Impact: **3656.0** | LOC: 1586
- `ParseOpDataTfLite` (@ `tensorflow/lite/core/api/flatbuffer_conversions.cc`) -> Impact: **3297.6** | LOC: 796
- `__init__` (@ `tensorflow/python/distribute/values.py`) -> Impact: **3233.4** | LOC: 1227
  * *Intent:* # ResourceVariable is a CompositeTensor. Attributes added to
- `__init__` (@ `tensorflow/tools/compatibility/tf_upgrade_v2.py`) -> Impact: **3182.1** | LOC: 2322
  * *Intent:* """List of maps that describe what changed in the API."""
- `_tpu_system_device_name` (@ `tensorflow/python/tpu/tpu.py`) -> Impact: **3178.3** | LOC: 1126
- `MaybeRaiseExceptionFromTFStatus` (@ `tensorflow/python/eager/pywrap_tfe_src.cc`) -> Impact: **3108.3** | LOC: 1544
- `model_iteration` (@ `tensorflow/python/keras/engine/training_generator_v1.py`) -> Impact: **3039.1** | LOC: 676

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parse_args` (@ `ci/official/utilities/extract_resultstore_links.py`) -> **O(2^N) [Recursive]**
- `main` (@ `configure.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Each instance of --test_tag_filters or --build_tag_filters overrides all # single list of filters for the .bazelrc file. # Filters to use with both ...
- `get_python_major_version` (@ `configure.py`) -> **O(2^N) [Recursive]**
- `sanitize_arg_name` (@ `tensorflow/core/function/polymorphism/function_type.py`) -> **O(2^N) [Recursive]**
- `from_proto` (@ `tensorflow/core/function/polymorphism/function_type.py`) -> **O(2^N) [Recursive]**
- `initialize_multi_client_cluster` (@ `tensorflow/dtensor/python/accelerator_util.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `tensorflow/dtensor/python/d_variable.py`) -> **O(2^N) [Recursive]**
- `_register_mesh` (@ `tensorflow/dtensor/python/dtensor_device.py`) -> **O(2^N) [Recursive]**
- `_validate_input` (@ `tensorflow/dtensor/python/input_util.py`) -> **O(2^N) [Recursive]**
- `_enumerate_cores` (@ `tensorflow/dtensor/python/tpu_util.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `LogSoftmax` (@ `tensorflow/lite/kernels/internal/optimized/optimized_ops.h`) -> DB Complexity: **613**
- `ConvGeneric::GenerateConv` (@ `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`) -> DB Complexity: **497**
- `ResizeBilinear888Uint8` (@ `tensorflow/lite/kernels/internal/optimized/resize_bilinear.h`) -> DB Complexity: **495**
- `GEMVForLstmCell` (@ `tensorflow/lite/kernels/internal/optimized/legacy_optimized_ops.h`) -> DB Complexity: **487**
- `EinsumShape` (@ `tensorflow/core/framework/common_shape_fns.cc`) -> DB Complexity: **441**
- `AbsorbInputByOptimizedNodesGroup` (@ `tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc`) -> DB Complexity: **412**
- `ConvertTFLMaxPool2DOp::matchAndRewrite` (@ `tensorflow/compiler/mlir/tosa/transforms/legalize_tfl.cc`) -> DB Complexity: **400**
- `ConvolutionTransposed::GenerateConvoluti` (@ `tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed.cc`) -> DB Complexity: **399**
- `ConvertTranspose` (@ `tensorflow/compiler/tf2tensorrt/convert/convert_nodes.cc`) -> DB Complexity: **397**
- `ValidateSignatureWithAttrs` (@ `tensorflow/core/framework/function.cc`) -> DB Complexity: **389**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tensorflow/core/kernels` | 997 | 154548.82 | 41.59% | 31.31% |
| `tensorflow/python/ops` | 138 | 95338.1 | 10.42% | 40.84% |
| `tensorflow/lite/kernels` | 199 | 69423.32 | 57.74% | 42.12% |
| `tensorflow/lite/delegates/gpu/common/tasks` | 166 | 53302.32 | 48.55% | 31.52% |
| `tensorflow/lite/kernels/internal/optimized` | 27 | 51510.32 | 52.63% | 50.15% |
| `tensorflow/core/framework` | 177 | 47713.2 | 45.09% | 45.38% |
| `tensorflow/core/common_runtime` | 218 | 44592.22 | 44.75% | 52.89% |
| `tensorflow/python/keras/engine` | 22 | 39868.3 | 28.55% | 58.09% |
| `tensorflow/python/framework` | 120 | 35844.13 | 24.25% | 50.72% |
| `tensorflow/compiler/mlir/tensorflow/transforms` | 180 | 33079.12 | 59.18% | 56.81% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `tensorflow/lite/tools/tflite-android.Dockerfile` -> **100.0%** Exposure
- `tensorflow/tools/ci_build/Dockerfile.android` -> **100.0%** Exposure
- `tensorflow/tools/ci_build/Dockerfile.cpu.arm64` -> **100.0%** Exposure
- `tensorflow/tools/ci_build/linux/mkl/Dockerfile.devel-mkl` -> **100.0%** Exposure
- `ci/official/any.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `tensorflow/lite/tools/tflite-android.Dockerfile` -> **100.0%** Exposure
- `tensorflow/tools/ci_build/Dockerfile.android` -> **100.0%** Exposure
- `tensorflow/tools/ci_build/Dockerfile.cpu.arm64` -> **100.0%** Exposure
- `ci/official/pycpp.sh` -> **100.0%** Exposure
- `ci/official/utilities/setup_docker.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tensorflow/core/distributed_runtime/message_wrappers.cc` -> **190** Orphaned Functions | **14** Duplicates
- `tensorflow/core/grappler/op_types.cc` -> **183** Orphaned Functions | **4** Duplicates
- `tensorflow/core/ir/tf_op_names.cc` -> **184** Orphaned Functions | **2** Duplicates
- `tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py` -> **139** Orphaned Functions | **44** Duplicates
- `tensorflow/compiler/tests/randomized_tests.cc` -> **29** Orphaned Functions | **126** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tensorflow/compiler/mlir/lite/tools/versioning/op_signature.cc`** -> AI Confidence: **99.48%**
2. **`tensorflow/compiler/tf2tensorrt/common/utils.cc`** -> AI Confidence: **99.48%**
3. **`tensorflow/compiler/tf2xla/kernels/case_op.cc`** -> AI Confidence: **99.48%**
4. **`tensorflow/compiler/tf2xla/kernels/while_op.cc`** -> AI Confidence: **99.48%**
5. **`tensorflow/core/common_runtime/function_body.cc`** -> AI Confidence: **99.48%**
6. **`tensorflow/core/common_runtime/graph_optimizer.cc`** -> AI Confidence: **99.48%**
7. **`tensorflow/core/common_runtime/ring_reducer.cc`** -> AI Confidence: **99.48%**
8. **`tensorflow/core/grappler/optimizers/debug_stripper.cc`** -> AI Confidence: **99.48%**
9. **`tensorflow/core/grappler/optimizers/dependency_optimizer.cc`** -> AI Confidence: **99.48%**
10. **`tensorflow/core/grappler/optimizers/shape_optimizer.cc`** -> AI Confidence: **99.48%**
11. **`tensorflow/core/grappler/utils/functions_test.cc`** -> AI Confidence: **99.48%**
12. **`tensorflow/core/kernels/cast_op.cc`** -> AI Confidence: **99.48%**
13. **`tensorflow/core/kernels/decode_csv_op.cc`** -> AI Confidence: **99.48%**
14. **`tensorflow/core/kernels/load_and_remap_matrix_op.cc`** -> AI Confidence: **99.48%**
15. **`tensorflow/core/kernels/resource_variable_ops.cc`** -> AI Confidence: **99.48%**
16. **`tensorflow/core/kernels/sparse/mat_mul_op.cc`** -> AI Confidence: **99.48%**
17. **`tensorflow/core/profiler/internal/tfprof_show.cc`** -> AI Confidence: **99.48%**
18. **`tensorflow/core/tpu/graph_rewrite/encapsulate_tpu_computations_pass.cc`** -> AI Confidence: **99.48%**
19. **`tensorflow/core/tpu/kernels/sparse_core_preprocess_ops.cc`** -> AI Confidence: **99.48%**
20. **`tensorflow/core/util/strided_slice_op.cc`** -> AI Confidence: **99.48%**
21. **`tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`** -> AI Confidence: **99.48%**
22. **`tensorflow/lite/delegates/gpu/common/tasks/conv_metal_simd.cc`** -> AI Confidence: **99.48%**
23. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed.cc`** -> AI Confidence: **99.48%**
24. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv.cc`** -> AI Confidence: **99.48%**
25. **`tensorflow/lite/delegates/gpu/common/tasks/pooling.cc`** -> AI Confidence: **99.48%**
26. **`tensorflow/lite/delegates/gpu/gl/kernels/elementwise.cc`** -> AI Confidence: **99.48%**
27. **`tensorflow/lite/delegates/xnnpack/binary_elementwise_tester.cc`** -> AI Confidence: **99.48%**
28. **`tensorflow/lite/delegates/xnnpack/conv_2d_tester.cc`** -> AI Confidence: **99.48%**
29. **`tensorflow/lite/delegates/xnnpack/depthwise_conv_2d_tester.cc`** -> AI Confidence: **99.48%**
30. **`tensorflow/lite/delegates/xnnpack/file_util.cc`** -> AI Confidence: **99.48%**
31. **`tensorflow/lite/delegates/xnnpack/fully_connected_tester.cc`** -> AI Confidence: **99.48%**
32. **`tensorflow/lite/delegates/xnnpack/transpose_conv_tester.cc`** -> AI Confidence: **99.48%**
33. **`tensorflow/lite/examples/label_image/bitmap_helpers.cc`** -> AI Confidence: **99.48%**
34. **`tensorflow/lite/experimental/acceleration/mini_benchmark/validator_runner.cc`** -> AI Confidence: **99.48%**
35. **`tensorflow/lite/kernels/arg_min_max.cc`** -> AI Confidence: **99.48%**
36. **`tensorflow/lite/kernels/bidirectional_sequence_rnn.cc`** -> AI Confidence: **99.48%**
37. **`tensorflow/lite/kernels/gradient/bcast_grad_args.cc`** -> AI Confidence: **99.48%**
38. **`tensorflow/lite/kernels/internal/optimized/integer_ops/pooling.h`** -> AI Confidence: **99.48%**
39. **`tensorflow/lite/kernels/lstm_eval.cc`** -> AI Confidence: **99.48%**
40. **`tensorflow/lite/toco/graph_transformations/ensure_uint8_weights_safe_for_fast_int8_kernels.cc`** -> AI Confidence: **99.48%**
41. **`tensorflow/lite/toco/toco_cmdline_flags.cc`** -> AI Confidence: **99.48%**
42. **`tensorflow/lite/tools/delegates/gpu_delegate_provider.cc`** -> AI Confidence: **99.48%**
43. **`tensorflow/lite/tools/optimize/calibration/custom_logging_ops/lstm.cc`** -> AI Confidence: **99.48%**
44. **`tensorflow/python/tfcompile_wrapper.cc`** -> AI Confidence: **99.48%**
45. **`tensorflow/tools/android/test/jni/object_tracking/optical_flow.cc`** -> AI Confidence: **99.48%**
46. **`tensorflow/tools/graph_transforms/insert_logging.cc`** -> AI Confidence: **99.48%**
47. **`tensorflow/lite/delegates/coreml/coreml_delegate.mm`** -> AI Confidence: **99.48%**
48. **`tensorflow/lite/delegates/coreml/coreml_delegate_kernel.mm`** -> AI Confidence: **99.48%**
49. **`tensorflow/lite/delegates/gpu/metal/benchmarking/main.mm`** -> AI Confidence: **99.48%**
50. **`tensorflow/lite/delegates/gpu/metal/buffer_convert.mm`** -> AI Confidence: **99.48%**
51. **`tensorflow/lite/delegates/gpu/metal/common.mm`** -> AI Confidence: **99.48%**
52. **`tensorflow/lite/delegates/gpu/metal_delegate.mm`** -> AI Confidence: **99.48%**
53. **`tensorflow/lite/examples/ios/simple/RunModelViewController.mm`** -> AI Confidence: **99.48%**
54. **`tensorflow/lite/examples/ios/simple/ios_image_load.mm`** -> AI Confidence: **99.48%**
55. **`tensorflow/lite/objc/sources/TFLInterpreter.mm`** -> AI Confidence: **99.48%**
56. **`tensorflow/lite/objc/sources/TFLSignatureRunner.mm`** -> AI Confidence: **99.48%**
57. **`tensorflow/lite/profiling/signpost_profiler.mm`** -> AI Confidence: **99.48%**
58. **`tensorflow/lite/tools/evaluation/tasks/ios/TFLiteEvaluation/TFLiteEvaluation/EvaluationViewController.mm`** -> AI Confidence: **99.48%**
59. **`tensorflow/core/common_runtime/optimized_function_graph_info.h`** -> AI Confidence: **99.43%**
60. **`tensorflow/c/kernels/ops/bitcast.cc`** -> AI Confidence: **99.39%**
61. **`tensorflow/compiler/jit/partially_decluster_pass.cc`** -> AI Confidence: **99.39%**
62. **`tensorflow/compiler/jit/shape_inference.cc`** -> AI Confidence: **99.39%**
63. **`tensorflow/compiler/jit/variable_info.cc`** -> AI Confidence: **99.39%**
64. **`tensorflow/compiler/mlir/lite/transforms/lower_quant_annotations_helper.cc`** -> AI Confidence: **99.39%**
65. **`tensorflow/compiler/mlir/quantization/common/ir/FakeQuantSupport.cc`** -> AI Confidence: **99.39%**
66. **`tensorflow/compiler/tf2tensorrt/utils/trt_engine_utils.cc`** -> AI Confidence: **99.39%**
67. **`tensorflow/compiler/tf2xla/functionalize_while.cc`** -> AI Confidence: **99.39%**
68. **`tensorflow/compiler/tf2xla/kernels/if_op.cc`** -> AI Confidence: **99.39%**
69. **`tensorflow/compiler/tf2xla/kernels/if_while_utils.cc`** -> AI Confidence: **99.39%**
70. **`tensorflow/compiler/tf2xla/kernels/image_resize_ops.cc`** -> AI Confidence: **99.39%**
71. **`tensorflow/compiler/tf2xla/kernels/quantize_and_dequantize_op.cc`** -> AI Confidence: **99.39%**
72. **`tensorflow/compiler/tf2xla/kernels/slice_op.cc`** -> AI Confidence: **99.39%**
73. **`tensorflow/compiler/tf2xla/rearrange_function_argument.cc`** -> AI Confidence: **99.39%**
74. **`tensorflow/compiler/tf2xla/resource_util.cc`** -> AI Confidence: **99.39%**
75. **`tensorflow/core/common_runtime/buf_rendezvous.cc`** -> AI Confidence: **99.39%**
76. **`tensorflow/core/common_runtime/gpu/gpu_process_state.cc`** -> AI Confidence: **99.39%**
77. **`tensorflow/core/common_runtime/graph_execution_state.cc`** -> AI Confidence: **99.39%**
78. **`tensorflow/core/common_runtime/graph_view.cc`** -> AI Confidence: **99.39%**
79. **`tensorflow/core/common_runtime/hierarchical_tree_broadcaster.cc`** -> AI Confidence: **99.39%**
80. **`tensorflow/core/common_runtime/immutable_executor_state.cc`** -> AI Confidence: **99.39%**
81. **`tensorflow/core/common_runtime/int32_fulltype.cc`** -> AI Confidence: **99.39%**
82. **`tensorflow/core/common_runtime/placer.cc`** -> AI Confidence: **99.39%**
83. **`tensorflow/core/common_runtime/ring_gatherer.cc`** -> AI Confidence: **99.39%**
84. **`tensorflow/core/common_runtime/single_threaded_executor.cc`** -> AI Confidence: **99.39%**
85. **`tensorflow/core/distributed_runtime/scheduler.cc`** -> AI Confidence: **99.39%**
86. **`tensorflow/core/framework/op_def_builder.cc`** -> AI Confidence: **99.39%**
87. **`tensorflow/core/graph/control_flow.cc`** -> AI Confidence: **99.39%**
88. **`tensorflow/core/grappler/optimizers/data/map_and_batch_fusion.cc`** -> AI Confidence: **99.39%**
89. **`tensorflow/core/grappler/optimizers/memory_optimizer.cc`** -> AI Confidence: **99.39%**
90. **`tensorflow/core/grappler/optimizers/meta_optimizer.cc`** -> AI Confidence: **99.39%**
91. **`tensorflow/core/grappler/optimizers/static_schedule.cc`** -> AI Confidence: **99.39%**
92. **`tensorflow/core/grappler/utils/scc_test.cc`** -> AI Confidence: **99.39%**
93. **`tensorflow/core/kernels/as_string_op.cc`** -> AI Confidence: **99.39%**
94. **`tensorflow/core/kernels/conv_ops_using_gemm.cc`** -> AI Confidence: **99.39%**
95. **`tensorflow/core/kernels/image/attention_ops.cc`** -> AI Confidence: **99.39%**
96. **`tensorflow/core/kernels/image/draw_bounding_box_op.cc`** -> AI Confidence: **99.39%**
97. **`tensorflow/core/kernels/image/encode_jpeg_op.cc`** -> AI Confidence: **99.39%**
98. **`tensorflow/core/kernels/partitioned_function_ops.cc`** -> AI Confidence: **99.39%**
99. **`tensorflow/core/kernels/quantized_matmul_op.cc`** -> AI Confidence: **99.39%**
100. **`tensorflow/core/profiler/internal/tfprof_show_multi.cc`** -> AI Confidence: **99.39%**
101. **`tensorflow/core/profiler/internal/tfprof_utils.cc`** -> AI Confidence: **99.39%**
102. **`tensorflow/core/profiler/profiler.cc`** -> AI Confidence: **99.39%**
103. **`tensorflow/core/tpu/kernels/tpu_functional_ops.cc`** -> AI Confidence: **99.39%**
104. **`tensorflow/core/transforms/utils/op_cat_helper.cc`** -> AI Confidence: **99.39%**
105. **`tensorflow/core/util/einsum_op_util.cc`** -> AI Confidence: **99.39%**
106. **`tensorflow/dtensor/cc/slice_util.cc`** -> AI Confidence: **99.39%**
107. **`tensorflow/dtensor/mlir/expansions/matmul_spmd_expander.cc`** -> AI Confidence: **99.39%**
108. **`tensorflow/examples/speech_commands/accuracy_utils.cc`** -> AI Confidence: **99.39%**
109. **`tensorflow/java/src/gen/cc/op_generator.cc`** -> AI Confidence: **99.39%**
110. **`tensorflow/java/src/gen/cc/source_writer.cc`** -> AI Confidence: **99.39%**
111. **`tensorflow/lite/delegates/flex/tflite_subgraph_execute.cc`** -> AI Confidence: **99.39%**
112. **`tensorflow/lite/delegates/gpu/common/memory_management/greedy_by_size_assignment.cc`** -> AI Confidence: **99.39%**
113. **`tensorflow/lite/delegates/gpu/common/task/util.cc`** -> AI Confidence: **99.39%**
114. **`tensorflow/lite/delegates/gpu/common/tasks/concat_xy.cc`** -> AI Confidence: **99.39%**
115. **`tensorflow/lite/delegates/gpu/common/tasks/conv_constants.cc`** -> AI Confidence: **99.39%**
116. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed_3x3_thin.cc`** -> AI Confidence: **99.39%**
117. **`tensorflow/lite/delegates/gpu/common/tasks/elementwise.cc`** -> AI Confidence: **99.39%**
118. **`tensorflow/lite/delegates/gpu/common/tasks/fully_connected.cc`** -> AI Confidence: **99.39%**
119. **`tensorflow/lite/delegates/gpu/common/tasks/gather.cc`** -> AI Confidence: **99.39%**
120. **`tensorflow/lite/delegates/gpu/common/tasks/reduce.cc`** -> AI Confidence: **99.39%**
121. **`tensorflow/lite/delegates/gpu/common/tasks/softmax1x1.cc`** -> AI Confidence: **99.39%**
122. **`tensorflow/lite/delegates/gpu/common/tasks/winograd.cc`** -> AI Confidence: **99.39%**
123. **`tensorflow/lite/delegates/gpu/common/tasks/winograd_test_util.cc`** -> AI Confidence: **99.39%**
124. **`tensorflow/lite/delegates/gpu/common/transformations/model_transformations.cc`** -> AI Confidence: **99.39%**
125. **`tensorflow/lite/delegates/gpu/gl/kernels/conv.cc`** -> AI Confidence: **99.39%**
126. **`tensorflow/lite/delegates/gpu/gl/kernels/pad.cc`** -> AI Confidence: **99.39%**
127. **`tensorflow/lite/delegates/nnapi/java/src/main/native/nnapi_delegate_impl_jni.cc`** -> AI Confidence: **99.39%**
128. **`tensorflow/lite/delegates/utils/experimental/sample_stable_delegate/sample_stable_delegate_with_control_flow_test.cc`** -> AI Confidence: **99.39%**
129. **`tensorflow/lite/delegates/xnnpack/prelu_tester.cc`** -> AI Confidence: **99.39%**
130. **`tensorflow/lite/delegates/xnnpack/unary_elementwise_tester.cc`** -> AI Confidence: **99.39%**
131. **`tensorflow/lite/delegates/xnnpack/xnnpack_delegate.cc`** -> AI Confidence: **99.39%**
132. **`tensorflow/lite/kernels/add.cc`** -> AI Confidence: **99.39%**
133. **`tensorflow/lite/kernels/bidirectional_sequence_lstm.cc`** -> AI Confidence: **99.39%**
134. **`tensorflow/lite/kernels/conv.cc`** -> AI Confidence: **99.39%**
135. **`tensorflow/lite/kernels/embedding_lookup_sparse.cc`** -> AI Confidence: **99.39%**
136. **`tensorflow/lite/kernels/mul.cc`** -> AI Confidence: **99.39%**
137. **`tensorflow/lite/kernels/pad.cc`** -> AI Confidence: **99.39%**
138. **`tensorflow/lite/kernels/reverse.cc`** -> AI Confidence: **99.39%**
139. **`tensorflow/lite/kernels/stablehlo_case.cc`** -> AI Confidence: **99.39%**
140. **`tensorflow/lite/kernels/strided_slice.cc`** -> AI Confidence: **99.39%**
141. **`tensorflow/lite/kernels/transpose_conv.cc`** -> AI Confidence: **99.39%**
142. **`tensorflow/lite/kernels/unidirectional_sequence_lstm.cc`** -> AI Confidence: **99.39%**
143. **`tensorflow/lite/testing/tflite_diff_flags.h`** -> AI Confidence: **99.39%**
144. **`tensorflow/lite/toco/graph_transformations/propagate_array_data_types.cc`** -> AI Confidence: **99.39%**
145. **`tensorflow/lite/toco/graph_transformations/resolve_constant_reshape.cc`** -> AI Confidence: **99.39%**
146. **`tensorflow/lite/toco/model_cmdline_flags.cc`** -> AI Confidence: **99.39%**
147. **`tensorflow/lite/toco/tensorflow_util.cc`** -> AI Confidence: **99.39%**
148. **`tensorflow/lite/tools/delegates/compatibility/nnapi/nnapi_delegate_compatibility_checker.cc`** -> AI Confidence: **99.39%**
149. **`tensorflow/python/util/stack_trace.cc`** -> AI Confidence: **99.39%**
150. **`tensorflow/tools/android/test/jni/object_tracking/object_tracker.cc`** -> AI Confidence: **99.39%**
151. **`tensorflow/tools/benchmark/benchmark_model.cc`** -> AI Confidence: **99.39%**
152. **`tensorflow/tools/graph_transforms/obfuscate_names.cc`** -> AI Confidence: **99.39%**
153. **`tensorflow/tools/graph_transforms/quantize_nodes.cc`** -> AI Confidence: **99.39%**
154. **`tensorflow/tools/graph_transforms/rename_attribute.cc`** -> AI Confidence: **99.39%**
155. **`tensorflow/tools/graph_transforms/strip_unused_nodes.cc`** -> AI Confidence: **99.39%**
156. **`tensorflow/lite/tools/benchmark/ios/TFLiteBenchmark/TFLiteBenchmark/BenchmarkViewController.mm`** -> AI Confidence: **99.39%**
157. **`tensorflow/compiler/tf2xla/kernels/strided_slice_op.cc`** -> AI Confidence: **99.35%**
158. **`tensorflow/compiler/tf2xla/tf2xla_util.cc`** -> AI Confidence: **99.35%**
159. **`tensorflow/core/common_runtime/function_utils.cc`** -> AI Confidence: **99.35%**
160. **`tensorflow/core/common_runtime/process_state.cc`** -> AI Confidence: **99.35%**
161. **`tensorflow/core/profiler/internal/tfprof_op.cc`** -> AI Confidence: **99.35%**
162. **`tensorflow/core/tpu/kernels/host_compute_ops.cc`** -> AI Confidence: **99.35%**
163. **`tensorflow/lite/arena_planner.cc`** -> AI Confidence: **99.35%**
164. **`tensorflow/lite/delegates/gpu/gl/kernels/mean.cc`** -> AI Confidence: **99.35%**
165. **`tensorflow/lite/kernels/comparisons.cc`** -> AI Confidence: **99.35%**
166. **`tensorflow/lite/tools/optimize/calibration/builtin_logging_ops/lstm.cc`** -> AI Confidence: **99.35%**
167. **`tensorflow/lite/tools/optimize/modify_model_interface.cc`** -> AI Confidence: **99.35%**
168. **`tensorflow/lite/tools/optimize/quantize_model.cc`** -> AI Confidence: **99.35%**
169. **`tensorflow/tools/ci_build/builds/pip_new.sh`** -> AI Confidence: **99.34%**
170. **`tensorflow/compiler/mlir/init_mlir.cc`** -> AI Confidence: **99.34%**
171. **`tensorflow/compiler/mlir/tensorflow/utils/cluster_util_test.cc`** -> AI Confidence: **99.34%**
172. **`tensorflow/core/grappler/utils/scc.cc`** -> AI Confidence: **99.34%**
173. **`tensorflow/core/kernels/collective_nccl_reducer.cc`** -> AI Confidence: **99.34%**
174. **`tensorflow/core/kernels/identity_op.cc`** -> AI Confidence: **99.34%**
175. **`tensorflow/core/kernels/mkl/mkl_matmul_op_fused.cc`** -> AI Confidence: **99.34%**
176. **`tensorflow/core/kernels/record_yielder.cc`** -> AI Confidence: **99.34%**
177. **`tensorflow/core/platform/platform_strings.cc`** -> AI Confidence: **99.34%**
178. **`tensorflow/core/tpu/graph_rewrite/tpu_embedding_rewrite_pass_utils.cc`** -> AI Confidence: **99.34%**
179. **`tensorflow/core/util/activation_mode.cc`** -> AI Confidence: **99.34%**
180. **`tensorflow/lite/delegates/gpu/common/task/weights_conversion.h`** -> AI Confidence: **99.34%**
181. **`tensorflow/lite/delegates/gpu/common/tasks/conv_constants.h`** -> AI Confidence: **99.34%**
182. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed_3x3.cc`** -> AI Confidence: **99.34%**
183. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed_4x4.cc`** -> AI Confidence: **99.34%**
184. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed_thin.cc`** -> AI Confidence: **99.34%**
185. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv_3x3.cc`** -> AI Confidence: **99.34%**
186. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv_3x3_stride_h2.cc`** -> AI Confidence: **99.34%**
187. **`tensorflow/lite/delegates/gpu/common/tasks/padding.cc`** -> AI Confidence: **99.34%**
188. **`tensorflow/lite/delegates/gpu/java/src/main/native/gpu_delegate_jni.cc`** -> AI Confidence: **99.34%**
189. **`tensorflow/lite/kernels/batch_to_space_nd.cc`** -> AI Confidence: **99.34%**
190. **`tensorflow/lite/kernels/dequantize.h`** -> AI Confidence: **99.34%**
191. **`tensorflow/lite/kernels/internal/reference/cumsum.h`** -> AI Confidence: **99.34%**
192. **`tensorflow/lite/kernels/internal/tensor_utils.cc`** -> AI Confidence: **99.34%**
193. **`tensorflow/lite/kernels/space_to_batch_nd.cc`** -> AI Confidence: **99.34%**
194. **`tensorflow/lite/tools/command_line_flags_test.cc`** -> AI Confidence: **99.34%**
195. **`tensorflow/lite/delegates/coreml/coreml_executor.mm`** -> AI Confidence: **99.34%**
196. **`tensorflow/lite/objc/sources/TFLCommonUtil.mm`** -> AI Confidence: **99.34%**
197. **`tensorflow/lite/delegates/gpu/metal/gpu_object.h`** -> AI Confidence: **99.33%**
198. **`tensorflow/tools/tf_sig_build_dockerfiles/Dockerfile`** -> AI Confidence: **99.32%**
199. **`tensorflow/tools/ci_build/builds/run_pip_tests.sh`** -> AI Confidence: **99.32%**
200. **`tensorflow/lite/core/api/tensor_utils.cc`** -> AI Confidence: **99.32%**
201. **`tensorflow/lite/delegates/gpu/common/tasks/select_v2.cc`** -> AI Confidence: **99.32%**
202. **`tensorflow/lite/kernels/internal/kernel_utils.cc`** -> AI Confidence: **99.32%**
203. **`tensorflow/lite/kernels/internal/reference/fully_connected.h`** -> AI Confidence: **99.32%**
204. **`tensorflow/python/framework/py_context_manager.cc`** -> AI Confidence: **99.32%**
205. **`tensorflow/lite/objc/apps/TestApp/TestApp/ViewController.m`** -> AI Confidence: **99.32%**
206. **`ci/official/utilities/setup.sh`** -> AI Confidence: **99.31%**
207. **`configure.py`** -> AI Confidence: **99.31%**
208. **`tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py`** -> AI Confidence: **99.31%**
209. **`tensorflow/core/function/capture/free_vars_detect.py`** -> AI Confidence: **99.31%**
210. **`tensorflow/core/function/polymorphism/function_type.py`** -> AI Confidence: **99.31%**
211. **`tensorflow/core/function/transform/transform.py`** -> AI Confidence: **99.31%**
212. **`tensorflow/dtensor/python/accelerator_util.py`** -> AI Confidence: **99.31%**
213. **`tensorflow/dtensor/python/mesh_util.py`** -> AI Confidence: **99.31%**
214. **`tensorflow/dtensor/python/tpu_util.py`** -> AI Confidence: **99.31%**
215. **`tensorflow/lite/python/convert.py`** -> AI Confidence: **99.31%**
216. **`tensorflow/lite/python/op_hint.py`** -> AI Confidence: **99.31%**
217. **`tensorflow/lite/python/tflite_convert.py`** -> AI Confidence: **99.31%**
218. **`tensorflow/lite/python/util.py`** -> AI Confidence: **99.31%**
219. **`tensorflow/lite/schema/upgrade_schema.py`** -> AI Confidence: **99.31%**
220. **`tensorflow/lite/testing/mlir_convert.py`** -> AI Confidence: **99.31%**
221. **`tensorflow/lite/testing/zip_test_utils.py`** -> AI Confidence: **99.31%**
222. **`tensorflow/lite/tools/evaluation/tasks/coco_object_detection/preprocess_coco_minival.py`** -> AI Confidence: **99.31%**
223. **`tensorflow/lite/tools/flatbuffer_utils.py`** -> AI Confidence: **99.31%**
224. **`tensorflow/lite/tools/optimize/debugging/python/debugger.py`** -> AI Confidence: **99.31%**
225. **`tensorflow/lite/tools/visualize.py`** -> AI Confidence: **99.31%**
226. **`tensorflow/python/autograph/operators/control_flow.py`** -> AI Confidence: **99.31%**
227. **`tensorflow/python/autograph/pyct/inspect_utils.py`** -> AI Confidence: **99.31%**
228. **`tensorflow/python/autograph/pyct/parser.py`** -> AI Confidence: **99.31%**
229. **`tensorflow/python/checkpoint/async_checkpoint_helper.py`** -> AI Confidence: **99.31%**
230. **`tensorflow/python/checkpoint/checkpoint.py`** -> AI Confidence: **99.31%**
231. **`tensorflow/python/checkpoint/restore.py`** -> AI Confidence: **99.31%**
232. **`tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py`** -> AI Confidence: **99.31%**
233. **`tensorflow/python/compiler/tensorrt/trt_convert.py`** -> AI Confidence: **99.31%**
234. **`tensorflow/python/data/experimental/ops/readers.py`** -> AI Confidence: **99.31%**
235. **`tensorflow/python/data/kernel_tests/tf_record_test_base.py`** -> AI Confidence: **99.31%**
236. **`tensorflow/python/data/ops/options.py`** -> AI Confidence: **99.31%**
237. **`tensorflow/python/distribute/coordinator/cluster_coordinator.py`** -> AI Confidence: **99.31%**
238. **`tensorflow/python/distribute/cross_device_ops.py`** -> AI Confidence: **99.31%**
239. **`tensorflow/python/distribute/distribute_coordinator.py`** -> AI Confidence: **99.31%**
240. **`tensorflow/python/distribute/failure_handling/failure_handling.py`** -> AI Confidence: **99.31%**
241. **`tensorflow/python/distribute/mirrored_run.py`** -> AI Confidence: **99.31%**
242. **`tensorflow/python/distribute/multi_process_runner.py`** -> AI Confidence: **99.31%**
243. **`tensorflow/python/distribute/tpu_strategy.py`** -> AI Confidence: **99.31%**
244. **`tensorflow/python/eager/backprop.py`** -> AI Confidence: **99.31%**
245. **`tensorflow/python/eager/polymorphic_function/concrete_function.py`** -> AI Confidence: **99.31%**
246. **`tensorflow/python/eager/remote.py`** -> AI Confidence: **99.31%**
247. **`tensorflow/python/framework/function.py`** -> AI Confidence: **99.31%**
248. **`tensorflow/python/framework/importer.py`** -> AI Confidence: **99.31%**
249. **`tensorflow/python/framework/meta_graph.py`** -> AI Confidence: **99.31%**
250. **`tensorflow/python/framework/tensor_util.py`** -> AI Confidence: **99.31%**
251. **`tensorflow/python/keras/backend.py`** -> AI Confidence: **99.31%**
252. **`tensorflow/python/keras/callbacks.py`** -> AI Confidence: **99.31%**
253. **`tensorflow/python/keras/callbacks_v1.py`** -> AI Confidence: **99.31%**
254. **`tensorflow/python/keras/distribute/distributed_training_utils_v1.py`** -> AI Confidence: **99.31%**
255. **`tensorflow/python/keras/engine/base_layer.py`** -> AI Confidence: **99.31%**
256. **`tensorflow/python/keras/engine/base_layer_v1.py`** -> AI Confidence: **99.31%**
257. **`tensorflow/python/keras/engine/functional.py`** -> AI Confidence: **99.31%**
258. **`tensorflow/python/keras/engine/input_layer.py`** -> AI Confidence: **99.31%**
259. **`tensorflow/python/keras/engine/sequential.py`** -> AI Confidence: **99.31%**
260. **`tensorflow/python/keras/engine/training.py`** -> AI Confidence: **99.31%**
261. **`tensorflow/python/keras/engine/training_arrays_v1.py`** -> AI Confidence: **99.31%**
262. **`tensorflow/python/keras/engine/training_eager_v1.py`** -> AI Confidence: **99.31%**
263. **`tensorflow/python/keras/engine/training_generator_v1.py`** -> AI Confidence: **99.31%**
264. **`tensorflow/python/keras/engine/training_utils_v1.py`** -> AI Confidence: **99.31%**
265. **`tensorflow/python/keras/engine/training_v1.py`** -> AI Confidence: **99.31%**
266. **`tensorflow/python/keras/layers/convolutional.py`** -> AI Confidence: **99.31%**
267. **`tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py`** -> AI Confidence: **99.31%**
268. **`tensorflow/python/keras/layers/recurrent.py`** -> AI Confidence: **99.31%**
269. **`tensorflow/python/keras/legacy_tf_layers/base.py`** -> AI Confidence: **99.31%**
270. **`tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py`** -> AI Confidence: **99.31%**
271. **`tensorflow/python/keras/optimizer_v1.py`** -> AI Confidence: **99.31%**
272. **`tensorflow/python/keras/optimizer_v2/optimizer_v2.py`** -> AI Confidence: **99.31%**
273. **`tensorflow/python/keras/saving/hdf5_format.py`** -> AI Confidence: **99.31%**
274. **`tensorflow/python/keras/saving/save.py`** -> AI Confidence: **99.31%**
275. **`tensorflow/python/keras/saving/saved_model/load.py`** -> AI Confidence: **99.31%**
276. **`tensorflow/python/keras/saving/utils_v1/export_utils.py`** -> AI Confidence: **99.31%**
277. **`tensorflow/python/keras/testing_utils.py`** -> AI Confidence: **99.31%**
278. **`tensorflow/python/keras/utils/generic_utils.py`** -> AI Confidence: **99.31%**
279. **`tensorflow/python/keras/utils/metrics_utils.py`** -> AI Confidence: **99.31%**
280. **`tensorflow/python/keras/utils/vis_utils.py`** -> AI Confidence: **99.31%**
281. **`tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py`** -> AI Confidence: **99.31%**
282. **`tensorflow/python/ops/array_ops.py`** -> AI Confidence: **99.31%**
283. **`tensorflow/python/ops/check_ops.py`** -> AI Confidence: **99.31%**
284. **`tensorflow/python/ops/cond.py`** -> AI Confidence: **99.31%**
285. **`tensorflow/python/ops/control_flow_ops.py`** -> AI Confidence: **99.31%**
286. **`tensorflow/python/ops/critical_section_ops.py`** -> AI Confidence: **99.31%**
287. **`tensorflow/python/ops/data_flow_ops.py`** -> AI Confidence: **99.31%**
288. **`tensorflow/python/ops/distributions/util.py`** -> AI Confidence: **99.31%**
289. **`tensorflow/python/ops/embedding_ops.py`** -> AI Confidence: **99.31%**
290. **`tensorflow/python/ops/functional_ops.py`** -> AI Confidence: **99.31%**
291. **`tensorflow/python/ops/gradients_util.py`** -> AI Confidence: **99.31%**
292. **`tensorflow/python/ops/linalg/linalg_impl.py`** -> AI Confidence: **99.31%**
293. **`tensorflow/python/ops/linalg_ops.py`** -> AI Confidence: **99.31%**
294. **`tensorflow/python/ops/lookup_ops.py`** -> AI Confidence: **99.31%**
295. **`tensorflow/python/ops/math_ops.py`** -> AI Confidence: **99.31%**
296. **`tensorflow/python/ops/metrics_impl.py`** -> AI Confidence: **99.31%**
297. **`tensorflow/python/ops/nn_ops.py`** -> AI Confidence: **99.31%**
298. **`tensorflow/python/ops/numpy_ops/np_array_ops.py`** -> AI Confidence: **99.31%**
299. **`tensorflow/python/ops/parsing_config.py`** -> AI Confidence: **99.31%**
300. **`tensorflow/python/ops/ragged/dynamic_ragged_shape.py`** -> AI Confidence: **99.31%**
301. **`tensorflow/python/ops/ragged/ragged_array_ops.py`** -> AI Confidence: **99.31%**
302. **`tensorflow/python/ops/ragged/ragged_factory_ops.py`** -> AI Confidence: **99.31%**
303. **`tensorflow/python/ops/ragged/ragged_getitem.py`** -> AI Confidence: **99.31%**
304. **`tensorflow/python/ops/ragged/ragged_math_ops.py`** -> AI Confidence: **99.31%**
305. **`tensorflow/python/ops/ragged/ragged_tensor.py`** -> AI Confidence: **99.31%**
306. **`tensorflow/python/ops/ragged/row_partition.py`** -> AI Confidence: **99.31%**
307. **`tensorflow/python/ops/sparse_ops.py`** -> AI Confidence: **99.31%**
308. **`tensorflow/python/ops/special_math_ops.py`** -> AI Confidence: **99.31%**
309. **`tensorflow/python/ops/structured/structured_tensor.py`** -> AI Confidence: **99.31%**
310. **`tensorflow/python/ops/tensor_getitem_override.py`** -> AI Confidence: **99.31%**
311. **`tensorflow/python/ops/variable_scope.py`** -> AI Confidence: **99.31%**
312. **`tensorflow/python/profiler/profile_context.py`** -> AI Confidence: **99.31%**
313. **`tensorflow/python/profiler/tfprof_logger.py`** -> AI Confidence: **99.31%**
314. **`tensorflow/python/saved_model/function_deserialization.py`** -> AI Confidence: **99.31%**
315. **`tensorflow/python/tools/api/generator/create_python_api.py`** -> AI Confidence: **99.31%**
316. **`tensorflow/python/tools/api/generator2/generator/generator.py`** -> AI Confidence: **99.31%**
317. **`tensorflow/python/tools/freeze_graph.py`** -> AI Confidence: **99.31%**
318. **`tensorflow/python/tools/inspect_checkpoint.py`** -> AI Confidence: **99.31%**
319. **`tensorflow/python/tools/optimize_for_inference_lib.py`** -> AI Confidence: **99.31%**
320. **`tensorflow/python/tools/saved_model_cli.py`** -> AI Confidence: **99.31%**
321. **`tensorflow/python/tools/selective_registration_header_lib.py`** -> AI Confidence: **99.31%**
322. **`tensorflow/python/tpu/device_assignment.py`** -> AI Confidence: **99.31%**
323. **`tensorflow/python/tpu/profiler/capture_tpu_profile.py`** -> AI Confidence: **99.31%**
324. **`tensorflow/python/tpu/tensor_tracer.py`** -> AI Confidence: **99.31%**
325. **`tensorflow/python/tpu/tpu.py`** -> AI Confidence: **99.31%**
326. **`tensorflow/python/tpu/tpu_embedding_v2.py`** -> AI Confidence: **99.31%**
327. **`tensorflow/python/tpu/tpu_feed.py`** -> AI Confidence: **99.31%**
328. **`tensorflow/python/tpu/tpu_strategy_util.py`** -> AI Confidence: **99.31%**
329. **`tensorflow/python/training/checkpoint_utils.py`** -> AI Confidence: **99.31%**
330. **`tensorflow/python/training/coordinator.py`** -> AI Confidence: **99.31%**
331. **`tensorflow/python/training/optimizer.py`** -> AI Confidence: **99.31%**
332. **`tensorflow/python/training/queue_runner_impl.py`** -> AI Confidence: **99.31%**
333. **`tensorflow/python/training/saver.py`** -> AI Confidence: **99.31%**
334. **`tensorflow/python/training/saving/saveable_object_util.py`** -> AI Confidence: **99.31%**
335. **`tensorflow/python/training/warm_starting_util.py`** -> AI Confidence: **99.31%**
336. **`tensorflow/python/util/deprecation.py`** -> AI Confidence: **99.31%**
337. **`tensorflow/python/util/lazy_loader.py`** -> AI Confidence: **99.31%**
338. **`tensorflow/python/util/nest_util.py`** -> AI Confidence: **99.31%**
339. **`tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py`** -> AI Confidence: **99.31%**
340. **`tensorflow/tools/compatibility/ast_edits.py`** -> AI Confidence: **99.31%**
341. **`tensorflow/tools/compatibility/tf_upgrade_v2.py`** -> AI Confidence: **99.31%**
342. **`tensorflow/tools/pip_package/build_pip_package.py`** -> AI Confidence: **99.31%**
343. **`tensorflow/tools/tensorflow_builder/config_detector/config_detector.py`** -> AI Confidence: **99.31%**
344. **`tensorflow/c/c_api.cc`** -> AI Confidence: **99.31%**
345. **`tensorflow/c/c_api_function.cc`** -> AI Confidence: **99.31%**
346. **`tensorflow/c/checkpoint_reader.cc`** -> AI Confidence: **99.31%**
347. **`tensorflow/c/eager/c_api_remote_test_util.cc`** -> AI Confidence: **99.31%**
348. **`tensorflow/c/eager/dlpack.cc`** -> AI Confidence: **99.31%**
349. **`tensorflow/c/eager/parallel_device/parallel_device.cc`** -> AI Confidence: **99.31%**
350. **`tensorflow/c/eager/unified_api_testutil.cc`** -> AI Confidence: **99.31%**
351. **`tensorflow/c/experimental/filesystem/modular_filesystem.cc`** -> AI Confidence: **99.31%**
352. **`tensorflow/c/experimental/filesystem/plugins/gcs/ram_file_block_cache.cc`** -> AI Confidence: **99.31%**
353. **`tensorflow/c/experimental/filesystem/plugins/posix/posix_filesystem.cc`** -> AI Confidence: **99.31%**
354. **`tensorflow/c/experimental/saved_model/core/revived_types/restored_resource.cc`** -> AI Confidence: **99.31%**
355. **`tensorflow/c/experimental/saved_model/core/revived_types/variable.cc`** -> AI Confidence: **99.31%**
356. **`tensorflow/c/experimental/saved_model/core/saved_model_utils.cc`** -> AI Confidence: **99.31%**
357. **`tensorflow/c/experimental/saved_model/core/test_utils.cc`** -> AI Confidence: **99.31%**
358. **`tensorflow/c/experimental/saved_model/internal/saved_model_api.cc`** -> AI Confidence: **99.31%**
359. **`tensorflow/c/kernels/bitcast_op.cc`** -> AI Confidence: **99.31%**
360. **`tensorflow/cc/framework/cc_op_gen_util.cc`** -> AI Confidence: **99.31%**
361. **`tensorflow/cc/framework/fuzzing/cc_op_fuzz_gen_main.cc`** -> AI Confidence: **99.31%**
362. **`tensorflow/cc/framework/gradients.cc`** -> AI Confidence: **99.31%**
363. **`tensorflow/cc/gradients/linalg_grad.cc`** -> AI Confidence: **99.31%**
364. **`tensorflow/cc/saved_model/bundle_v2.cc`** -> AI Confidence: **99.31%**
365. **`tensorflow/cc/saved_model/fingerprinting_utils.cc`** -> AI Confidence: **99.31%**
366. **`tensorflow/cc/saved_model/image_format/internal_api.cc`** -> AI Confidence: **99.31%**
367. **`tensorflow/cc/saved_model/reader.cc`** -> AI Confidence: **99.31%**
368. **`tensorflow/cc/saved_model/util.cc`** -> AI Confidence: **99.31%**
369. **`tensorflow/cc/tools/freeze_saved_model.cc`** -> AI Confidence: **99.31%**
370. **`tensorflow/cc/training/queue_runner.cc`** -> AI Confidence: **99.31%**
371. **`tensorflow/compiler/aot/benchmark.cc`** -> AI Confidence: **99.31%**
372. **`tensorflow/compiler/aot/compile.cc`** -> AI Confidence: **99.31%**
373. **`tensorflow/compiler/aot/tfcompile_main.cc`** -> AI Confidence: **99.31%**
374. **`tensorflow/compiler/aot/thunk_proto_execution_deserializer.cc`** -> AI Confidence: **99.31%**
375. **`tensorflow/compiler/jit/build_xla_ops_pass.cc`** -> AI Confidence: **99.31%**
376. **`tensorflow/compiler/jit/clone_constants_for_better_clustering.cc`** -> AI Confidence: **99.31%**
377. **`tensorflow/compiler/jit/compilability_check_util.cc`** -> AI Confidence: **99.31%**
378. **`tensorflow/compiler/jit/deadness_analysis.cc`** -> AI Confidence: **99.31%**
379. **`tensorflow/compiler/jit/encapsulate_subgraphs_pass.cc`** -> AI Confidence: **99.31%**
380. **`tensorflow/compiler/jit/encapsulate_util.cc`** -> AI Confidence: **99.31%**
381. **`tensorflow/compiler/jit/encapsulate_xla_computations_pass.cc`** -> AI Confidence: **99.31%**
382. **`tensorflow/compiler/jit/extract_outside_compilation_pass.cc`** -> AI Confidence: **99.31%**
383. **`tensorflow/compiler/jit/flags.cc`** -> AI Confidence: **99.31%**
384. **`tensorflow/compiler/jit/get_compiler_ir.cc`** -> AI Confidence: **99.31%**
385. **`tensorflow/compiler/jit/mark_for_compilation_pass.cc`** -> AI Confidence: **99.31%**
386. **`tensorflow/compiler/jit/mark_for_compilation_pass_test_helper.cc`** -> AI Confidence: **99.31%**
387. **`tensorflow/compiler/jit/node_matchers.cc`** -> AI Confidence: **99.31%**
388. **`tensorflow/compiler/jit/pjrt_device_context.cc`** -> AI Confidence: **99.31%**
389. **`tensorflow/compiler/jit/resource_operation_safety_analysis.cc`** -> AI Confidence: **99.31%**
390. **`tensorflow/compiler/jit/test_util.cc`** -> AI Confidence: **99.31%**
391. **`tensorflow/compiler/jit/tests/auto_clustering_test_helper.cc`** -> AI Confidence: **99.31%**
392. **`tensorflow/compiler/jit/tf_graph_to_hlo_compiler.cc`** -> AI Confidence: **99.31%**
393. **`tensorflow/compiler/jit/variable_info_util.cc`** -> AI Confidence: **99.31%**
394. **`tensorflow/compiler/jit/xla_cluster_util.cc`** -> AI Confidence: **99.31%**
395. **`tensorflow/compiler/jit/xla_compile_util.cc`** -> AI Confidence: **99.31%**
396. **`tensorflow/compiler/jit/xla_compiler_options_util.cc`** -> AI Confidence: **99.31%**
397. **`tensorflow/compiler/jit/xla_gpu_device.cc`** -> AI Confidence: **99.31%**
398. **`tensorflow/compiler/jit/xla_launch_util.cc`** -> AI Confidence: **99.31%**
399. **`tensorflow/compiler/mlir/lite/core/model_builder_base.cc`** -> AI Confidence: **99.31%**
400. **`tensorflow/compiler/mlir/lite/experimental/common/outline_operations.cc`** -> AI Confidence: **99.31%**
401. **`tensorflow/compiler/mlir/lite/experimental/tac/transforms/cost_model.cc`** -> AI Confidence: **99.31%**
402. **`tensorflow/compiler/mlir/lite/experimental/tac/transforms/target_annotation.cc`** -> AI Confidence: **99.31%**
403. **`tensorflow/compiler/mlir/lite/json_to_flatbuffer.cc`** -> AI Confidence: **99.31%**
404. **`tensorflow/compiler/mlir/lite/python/converter_python_api.cc`** -> AI Confidence: **99.31%**
405. **`tensorflow/compiler/mlir/lite/python/tf_tfl_flatbuffer_helpers.cc`** -> AI Confidence: **99.31%**
406. **`tensorflow/compiler/mlir/lite/quantization/lite/toco_legacy/quantization_utils.cc`** -> AI Confidence: **99.31%**
407. **`tensorflow/compiler/mlir/lite/quantization/lite/toco_legacy/quantize_weights.cc`** -> AI Confidence: **99.31%**
408. **`tensorflow/compiler/mlir/lite/quantization/lite/toco_legacy/quantize_weights_portable.cc`** -> AI Confidence: **99.31%**
409. **`tensorflow/compiler/mlir/lite/quantization/numerical_utils.cc`** -> AI Confidence: **99.31%**
410. **`tensorflow/compiler/mlir/lite/quantization/quantization_context.cc`** -> AI Confidence: **99.31%**
411. **`tensorflow/compiler/mlir/lite/quantization/tools/op_quant_spec_getters_gen.cc`** -> AI Confidence: **99.31%**
412. **`tensorflow/compiler/mlir/lite/quantization/tools/tflite_op_coverage_spec_getters_gen.cc`** -> AI Confidence: **99.31%**
413. **`tensorflow/compiler/mlir/lite/schema/schema_utils.cc`** -> AI Confidence: **99.31%**
414. **`tensorflow/compiler/mlir/lite/stablehlo/odml_converter/odml_converter_main.cc`** -> AI Confidence: **99.31%**
415. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/conv_util.cc`** -> AI Confidence: **99.31%**
416. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/gather.cc`** -> AI Confidence: **99.31%**
417. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/optimize.cc`** -> AI Confidence: **99.31%**
418. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/stablehlo_fuse_convolution_pass.cc`** -> AI Confidence: **99.31%**
419. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/tfl_stablehlo_pass.cc`** -> AI Confidence: **99.31%**
420. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/torch/build_stablehlo_composite_pass.cc`** -> AI Confidence: **99.31%**
421. **`tensorflow/compiler/mlir/lite/tf_tfl_passes.cc`** -> AI Confidence: **99.31%**
422. **`tensorflow/compiler/mlir/lite/tools/command_line_flags.cc`** -> AI Confidence: **99.31%**
423. **`tensorflow/compiler/mlir/lite/tools/versioning/op_version.cc`** -> AI Confidence: **99.31%**
424. **`tensorflow/compiler/mlir/lite/transforms/dense_to_sparse_pass.cc`** -> AI Confidence: **99.31%**
425. **`tensorflow/compiler/mlir/lite/transforms/modify_io_nodes.cc`** -> AI Confidence: **99.31%**
426. **`tensorflow/compiler/mlir/lite/transforms/optimize_broadcast_like_pass.cc`** -> AI Confidence: **99.31%**
427. **`tensorflow/compiler/mlir/lite/transforms/optimize_functional_ops.cc`** -> AI Confidence: **99.31%**
428. **`tensorflow/compiler/mlir/lite/transforms/prepare_quantize_dynamic_range.cc`** -> AI Confidence: **99.31%**
429. **`tensorflow/compiler/mlir/lite/transforms/quantize.cc`** -> AI Confidence: **99.31%**
430. **`tensorflow/compiler/mlir/lite/transforms/reduce_while_operands.cc`** -> AI Confidence: **99.31%**
431. **`tensorflow/compiler/mlir/lite/transforms/tf_legalizations/while_loop_outline_pass.cc`** -> AI Confidence: **99.31%**
432. **`tensorflow/compiler/mlir/lite/transforms/tflite_passes/optimize_batch_matmul_utils.cc`** -> AI Confidence: **99.31%**
433. **`tensorflow/compiler/mlir/lite/transforms/tflite_passes/split_merged_operands_pass.cc`** -> AI Confidence: **99.31%**
434. **`tensorflow/compiler/mlir/lite/utils/const_tensor_utils.cc`** -> AI Confidence: **99.31%**
435. **`tensorflow/compiler/mlir/lite/utils/constant_utils.cc`** -> AI Confidence: **99.31%**
436. **`tensorflow/compiler/mlir/lite/utils/convert_type.cc`** -> AI Confidence: **99.31%**
437. **`tensorflow/compiler/mlir/lite/utils/perception_ops_utils.cc`** -> AI Confidence: **99.31%**
438. **`tensorflow/compiler/mlir/lite/utils/shape_and_size_utils.cc`** -> AI Confidence: **99.31%**
439. **`tensorflow/compiler/mlir/lite/utils/variables_utils.cc`** -> AI Confidence: **99.31%**
440. **`tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc`** -> AI Confidence: **99.31%**
441. **`tensorflow/compiler/mlir/quantization/common/attrs_and_constraints.cc`** -> AI Confidence: **99.31%**
442. **`tensorflow/compiler/mlir/quantization/common/lift_as_function_call.cc`** -> AI Confidence: **99.31%**
443. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/insert_calibration_statistics_saver.cc`** -> AI Confidence: **99.31%**
444. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/replace_stablehlo_ops_in_main_function_with_xla_call_module_ops.cc`** -> AI Confidence: **99.31%**
445. **`tensorflow/compiler/mlir/quantization/stablehlo/python/pywrap_quantization.cc`** -> AI Confidence: **99.31%**
446. **`tensorflow/compiler/mlir/quantization/tensorflow/calibrator/calibration_statistics_saver_op.cc`** -> AI Confidence: **99.31%**
447. **`tensorflow/compiler/mlir/quantization/tensorflow/cc/constant_fold.cc`** -> AI Confidence: **99.31%**
448. **`tensorflow/compiler/mlir/quantization/tensorflow/cc/quantization_unit_loc.cc`** -> AI Confidence: **99.31%**
449. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/convert_tf_xla_op_to_tf_op.cc`** -> AI Confidence: **99.31%**
450. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/insert_custom_aggregation_ops.cc`** -> AI Confidence: **99.31%**
451. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/insert_main_function.cc`** -> AI Confidence: **99.31%**
452. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/replace_cast_hacks_with_tf_xla_ops.cc`** -> AI Confidence: **99.31%**
453. **`tensorflow/compiler/mlir/quantization/tensorflow/quantize_passes.cc`** -> AI Confidence: **99.31%**
454. **`tensorflow/compiler/mlir/quantization/tensorflow/utils/tf_to_uniform_attribute_utils.cc`** -> AI Confidence: **99.31%**
455. **`tensorflow/compiler/mlir/stablehlo/transforms/mhlo_passes/fuse_convolution_pass.cc`** -> AI Confidence: **99.31%**
456. **`tensorflow/compiler/mlir/tensorflow/analysis/resource_alias_analysis.cc`** -> AI Confidence: **99.31%**
457. **`tensorflow/compiler/mlir/tensorflow/analysis/side_effect_analysis.cc`** -> AI Confidence: **99.31%**
458. **`tensorflow/compiler/mlir/tensorflow/ir/host_runtime/tfrt_ops.cc`** -> AI Confidence: **99.31%**
459. **`tensorflow/compiler/mlir/tensorflow/ir/tf_executor.cc`** -> AI Confidence: **99.31%**
460. **`tensorflow/compiler/mlir/tensorflow/ir/tf_ops_tensor_helper.cc`** -> AI Confidence: **99.31%**
461. **`tensorflow/compiler/mlir/tensorflow/transforms/add_functions_for_exported_names.cc`** -> AI Confidence: **99.31%**
462. **`tensorflow/compiler/mlir/tensorflow/transforms/breakup-islands.cc`** -> AI Confidence: **99.31%**
463. **`tensorflow/compiler/mlir/tensorflow/transforms/cluster_ops_by_policy.cc`** -> AI Confidence: **99.31%**
464. **`tensorflow/compiler/mlir/tensorflow/transforms/constant_fold.cc`** -> AI Confidence: **99.31%**
465. **`tensorflow/compiler/mlir/tensorflow/transforms/einsum.cc`** -> AI Confidence: **99.31%**
466. **`tensorflow/compiler/mlir/tensorflow/transforms/executor_tpuv1_island_coarsening.cc`** -> AI Confidence: **99.31%**
467. **`tensorflow/compiler/mlir/tensorflow/transforms/executor_tpuv1_outline_tpu_island.cc`** -> AI Confidence: **99.31%**
468. **`tensorflow/compiler/mlir/tensorflow/transforms/freeze_global_tensors.cc`** -> AI Confidence: **99.31%**
469. **`tensorflow/compiler/mlir/tensorflow/transforms/host_runtime/tpu_merge_variables_with_execute.cc`** -> AI Confidence: **99.31%**
470. **`tensorflow/compiler/mlir/tensorflow/transforms/host_runtime/tpu_rewrite_pass.cc`** -> AI Confidence: **99.31%**
471. **`tensorflow/compiler/mlir/tensorflow/transforms/host_runtime/tpu_variable_runtime_reformatting.cc`** -> AI Confidence: **99.31%**
472. **`tensorflow/compiler/mlir/tensorflow/transforms/layout_optimization.cc`** -> AI Confidence: **99.31%**
473. **`tensorflow/compiler/mlir/tensorflow/transforms/mark_input_output_aliases.cc`** -> AI Confidence: **99.31%**
474. **`tensorflow/compiler/mlir/tensorflow/transforms/move_tpu_compile_to_front.cc`** -> AI Confidence: **99.31%**
475. **`tensorflow/compiler/mlir/tensorflow/transforms/promote_resources_to_args.cc`** -> AI Confidence: **99.31%**
476. **`tensorflow/compiler/mlir/tensorflow/transforms/remove_unused_arguments.cc`** -> AI Confidence: **99.31%**
477. **`tensorflow/compiler/mlir/tensorflow/transforms/remove_unused_while_results.cc`** -> AI Confidence: **99.31%**
478. **`tensorflow/compiler/mlir/tensorflow/transforms/replica_id_to_device_ordinal.cc`** -> AI Confidence: **99.31%**
479. **`tensorflow/compiler/mlir/tensorflow/transforms/resource_op_lifting_cleanup.cc`** -> AI Confidence: **99.31%**
480. **`tensorflow/compiler/mlir/tensorflow/transforms/sparsecore/embedding_pipelining.cc`** -> AI Confidence: **99.31%**
481. **`tensorflow/compiler/mlir/tensorflow/transforms/sparsecore/embedding_program_key.cc`** -> AI Confidence: **99.31%**
482. **`tensorflow/compiler/mlir/tensorflow/transforms/sparsecore/embedding_sequencing.cc`** -> AI Confidence: **99.31%**
483. **`tensorflow/compiler/mlir/tensorflow/transforms/tf_saved_model_freeze_utils.cc`** -> AI Confidence: **99.31%**
484. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_device_propagation.cc`** -> AI Confidence: **99.31%**
485. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_host_computation_expansion.cc`** -> AI Confidence: **99.31%**
486. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_partitioned_op_conversion.cc`** -> AI Confidence: **99.31%**
487. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_resource_partitioning.cc`** -> AI Confidence: **99.31%**
488. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_resource_read_for_write.cc`** -> AI Confidence: **99.31%**
489. **`tensorflow/compiler/mlir/tensorflow/translate/tools/file_tf_mlir_translate.cc`** -> AI Confidence: **99.31%**
490. **`tensorflow/compiler/mlir/tensorflow/translate/tools/parsers.cc`** -> AI Confidence: **99.31%**
491. **`tensorflow/compiler/mlir/tensorflow/utils/bridge_logger.cc`** -> AI Confidence: **99.31%**
492. **`tensorflow/compiler/mlir/tensorflow/utils/cluster_util.cc`** -> AI Confidence: **99.31%**
493. **`tensorflow/compiler/mlir/tensorflow/utils/convert_attr.cc`** -> AI Confidence: **99.31%**
494. **`tensorflow/compiler/mlir/tensorflow/utils/convert_type.cc`** -> AI Confidence: **99.31%**
495. **`tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc`** -> AI Confidence: **99.31%**
496. **`tensorflow/compiler/mlir/tensorflow/utils/export_utils.cc`** -> AI Confidence: **99.31%**
497. **`tensorflow/compiler/mlir/tensorflow/utils/tf_xla_mlir_translate.cc`** -> AI Confidence: **99.31%**
498. **`tensorflow/compiler/mlir/tensorflow/utils/topological_sort.cc`** -> AI Confidence: **99.31%**
499. **`tensorflow/compiler/mlir/tensorflow/utils/xla_rewrite_util.cc`** -> AI Confidence: **99.31%**
500. **`tensorflow/compiler/mlir/tensorflow/utils/xla_sharding_util.cc`** -> AI Confidence: **99.31%**
501. **`tensorflow/compiler/mlir/tensorflow_to_stablehlo/python/pywrap_tensorflow_to_stablehlo.cc`** -> AI Confidence: **99.31%**
502. **`tensorflow/compiler/mlir/tf2xla/api/v1/compile_mlir_util.cc`** -> AI Confidence: **99.31%**
503. **`tensorflow/compiler/mlir/tf2xla/internal/graph_to_tf_executor_util.cc`** -> AI Confidence: **99.31%**
504. **`tensorflow/compiler/mlir/tf2xla/internal/node_order.cc`** -> AI Confidence: **99.31%**
505. **`tensorflow/compiler/mlir/tf2xla/internal/passes/extract_head_tail_outside_compilation.cc`** -> AI Confidence: **99.31%**
506. **`tensorflow/compiler/mlir/tf2xla/internal/passes/extract_outside_compilation.cc`** -> AI Confidence: **99.31%**
507. **`tensorflow/compiler/mlir/tf2xla/transforms/xla_legalize_tf.cc`** -> AI Confidence: **99.31%**
508. **`tensorflow/compiler/mlir/tf_mlir_translate_main.cc`** -> AI Confidence: **99.31%**
509. **`tensorflow/compiler/mlir/tfr/passes/canonicalize.cc`** -> AI Confidence: **99.31%**
510. **`tensorflow/compiler/mlir/tfr/utils/utils.cc`** -> AI Confidence: **99.31%**
511. **`tensorflow/compiler/mlir/tfrt/ir/tfrt_fallback_common.cc`** -> AI Confidence: **99.31%**
512. **`tensorflow/compiler/mlir/tfrt/transforms/attr_lowering_utils.cc`** -> AI Confidence: **99.31%**
513. **`tensorflow/compiler/mlir/tfrt/transforms/cross_device_transfer.cc`** -> AI Confidence: **99.31%**
514. **`tensorflow/compiler/mlir/tfrt/transforms/insert_tensor_copy.cc`** -> AI Confidence: **99.31%**
515. **`tensorflow/compiler/mlir/tfrt/transforms/mlrt/async_while.cc`** -> AI Confidence: **99.31%**
516. **`tensorflow/compiler/mlir/tfrt/transforms/mlrt/parallelization.cc`** -> AI Confidence: **99.31%**
517. **`tensorflow/compiler/mlir/tfrt/transforms/mlrt/while_to_map_fn.cc`** -> AI Confidence: **99.31%**
518. **`tensorflow/compiler/mlir/tfrt/transforms/optimize_tf_control_flow_side_effect.cc`** -> AI Confidence: **99.31%**
519. **`tensorflow/compiler/mlir/tfrt/transforms/passes.cc`** -> AI Confidence: **99.31%**
520. **`tensorflow/compiler/mlir/tfrt/transforms/reconfig_batch_op.cc`** -> AI Confidence: **99.31%**
521. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/broadcast_propagation_pass.cc`** -> AI Confidence: **99.31%**
522. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/buffer_reuse_pass.cc`** -> AI Confidence: **99.31%**
523. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/copy_cleanup_pass.cc`** -> AI Confidence: **99.31%**
524. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/shape_simplification_pass.cc`** -> AI Confidence: **99.31%**
525. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/tensorflow_abi_knowledge_propagation.cc`** -> AI Confidence: **99.31%**
526. **`tensorflow/compiler/mlir/tools/optimize/quantization_utils.cc`** -> AI Confidence: **99.31%**
527. **`tensorflow/compiler/mlir/tosa/transforms/legalize_tfl_stateful.cc`** -> AI Confidence: **99.31%**
528. **`tensorflow/compiler/mlir/utils/name_utils.cc`** -> AI Confidence: **99.31%**
529. **`tensorflow/compiler/tf2tensorrt/convert/algorithm_selector.cc`** -> AI Confidence: **99.31%**
530. **`tensorflow/compiler/tf2tensorrt/convert/convert_graph.cc`** -> AI Confidence: **99.31%**
531. **`tensorflow/compiler/tf2tensorrt/convert/convert_nodes.cc`** -> AI Confidence: **99.31%**
532. **`tensorflow/compiler/tf2tensorrt/convert/ops/data_format_vec_permute.cc`** -> AI Confidence: **99.31%**
533. **`tensorflow/compiler/tf2tensorrt/convert/ops/einsum.cc`** -> AI Confidence: **99.31%**
534. **`tensorflow/compiler/tf2tensorrt/convert/ops/slice_ops.cc`** -> AI Confidence: **99.31%**
535. **`tensorflow/compiler/tf2tensorrt/convert/trt_optimization_pass.cc`** -> AI Confidence: **99.31%**
536. **`tensorflow/compiler/tf2tensorrt/convert/trt_parameters.cc`** -> AI Confidence: **99.31%**
537. **`tensorflow/compiler/tf2tensorrt/kernels/trt_engine_resource_ops.cc`** -> AI Confidence: **99.31%**
538. **`tensorflow/compiler/tf2tensorrt/trt_convert_api.cc`** -> AI Confidence: **99.31%**
539. **`tensorflow/compiler/tf2tensorrt/trt_convert_api.h`** -> AI Confidence: **99.31%**
540. **`tensorflow/compiler/tf2tensorrt/utils/trt_shape_optimization_profiles.cc`** -> AI Confidence: **99.31%**
541. **`tensorflow/compiler/tf2tensorrt/utils/trt_shape_optimization_profiles_test.cc`** -> AI Confidence: **99.31%**
542. **`tensorflow/compiler/tf2xla/allocator.cc`** -> AI Confidence: **99.31%**
543. **`tensorflow/compiler/tf2xla/const_analysis.cc`** -> AI Confidence: **99.31%**
544. **`tensorflow/compiler/tf2xla/functionalize_cond.cc`** -> AI Confidence: **99.31%**
545. **`tensorflow/compiler/tf2xla/functionalize_control_flow.cc`** -> AI Confidence: **99.31%**
546. **`tensorflow/compiler/tf2xla/graph_compiler.cc`** -> AI Confidence: **99.31%**
547. **`tensorflow/compiler/tf2xla/graph_compiler_util.cc`** -> AI Confidence: **99.31%**
548. **`tensorflow/compiler/tf2xla/kernels/batch_norm_op.cc`** -> AI Confidence: **99.31%**
549. **`tensorflow/compiler/tf2xla/kernels/bcast_ops.cc`** -> AI Confidence: **99.31%**
550. **`tensorflow/compiler/tf2xla/kernels/cast_op.cc`** -> AI Confidence: **99.31%**
551. **`tensorflow/compiler/tf2xla/kernels/conv_op_helpers.cc`** -> AI Confidence: **99.31%**
552. **`tensorflow/compiler/tf2xla/kernels/cwise_ops.cc`** -> AI Confidence: **99.31%**
553. **`tensorflow/compiler/tf2xla/kernels/data_format_ops.cc`** -> AI Confidence: **99.31%**
554. **`tensorflow/compiler/tf2xla/kernels/depthtospace_op.cc`** -> AI Confidence: **99.31%**
555. **`tensorflow/compiler/tf2xla/kernels/dynamic_stitch_op.cc`** -> AI Confidence: **99.31%**
556. **`tensorflow/compiler/tf2xla/kernels/extract_image_patches_op.cc`** -> AI Confidence: **99.31%**
557. **`tensorflow/compiler/tf2xla/kernels/fused_conv_ops.cc`** -> AI Confidence: **99.31%**
558. **`tensorflow/compiler/tf2xla/kernels/gather_op.cc`** -> AI Confidence: **99.31%**
559. **`tensorflow/compiler/tf2xla/kernels/listdiff_op.cc`** -> AI Confidence: **99.31%**
560. **`tensorflow/compiler/tf2xla/kernels/matmul_op.cc`** -> AI Confidence: **99.31%**
561. **`tensorflow/compiler/tf2xla/kernels/matrix_diag_ops.cc`** -> AI Confidence: **99.31%**
562. **`tensorflow/compiler/tf2xla/kernels/reshape_op.cc`** -> AI Confidence: **99.31%**
563. **`tensorflow/compiler/tf2xla/kernels/roll_op.cc`** -> AI Confidence: **99.31%**
564. **`tensorflow/compiler/tf2xla/kernels/scan_ops.cc`** -> AI Confidence: **99.31%**
565. **`tensorflow/compiler/tf2xla/kernels/sequence_ops.cc`** -> AI Confidence: **99.31%**
566. **`tensorflow/compiler/tf2xla/kernels/shape_util.cc`** -> AI Confidence: **99.31%**
567. **`tensorflow/compiler/tf2xla/kernels/sharding_util_ops.cc`** -> AI Confidence: **99.31%**
568. **`tensorflow/compiler/tf2xla/kernels/spacetodepth_op.cc`** -> AI Confidence: **99.31%**
569. **`tensorflow/compiler/tf2xla/kernels/sparse_to_dense_op.cc`** -> AI Confidence: **99.31%**
570. **`tensorflow/compiler/tf2xla/kernels/split_op.cc`** -> AI Confidence: **99.31%**
571. **`tensorflow/compiler/tf2xla/kernels/tensor_list_utils.cc`** -> AI Confidence: **99.31%**
572. **`tensorflow/compiler/tf2xla/kernels/transpose_op.cc`** -> AI Confidence: **99.31%**
573. **`tensorflow/compiler/tf2xla/kernels/xla_broadcast_helper_op.cc`** -> AI Confidence: **99.31%**
574. **`tensorflow/compiler/tf2xla/kernels/xla_call_module_loader.cc`** -> AI Confidence: **99.31%**
575. **`tensorflow/compiler/tf2xla/kernels/xla_call_module_op.cc`** -> AI Confidence: **99.31%**
576. **`tensorflow/compiler/tf2xla/mlir_xla_op_kernel.cc`** -> AI Confidence: **99.31%**
577. **`tensorflow/compiler/tf2xla/ops/xla_ops.cc`** -> AI Confidence: **99.31%**
578. **`tensorflow/compiler/tf2xla/shape_util.cc`** -> AI Confidence: **99.31%**
579. **`tensorflow/compiler/tf2xla/sharding_util.cc`** -> AI Confidence: **99.31%**
580. **`tensorflow/compiler/tf2xla/side_effect_util.cc`** -> AI Confidence: **99.31%**
581. **`tensorflow/compiler/tf2xla/test_util.h`** -> AI Confidence: **99.31%**
582. **`tensorflow/compiler/tf2xla/tf2xla.cc`** -> AI Confidence: **99.31%**
583. **`tensorflow/compiler/tf2xla/type_util.cc`** -> AI Confidence: **99.31%**
584. **`tensorflow/compiler/tf2xla/xla_compiler.cc`** -> AI Confidence: **99.31%**
585. **`tensorflow/compiler/tf2xla/xla_helpers.cc`** -> AI Confidence: **99.31%**
586. **`tensorflow/compiler/tf2xla/xla_op_registry.cc`** -> AI Confidence: **99.31%**
587. **`tensorflow/compiler/tf2xla/xla_resource.cc`** -> AI Confidence: **99.31%**
588. **`tensorflow/core/api_def/update_api_def.cc`** -> AI Confidence: **99.31%**
589. **`tensorflow/core/common_runtime/arg_ret_placement.cc`** -> AI Confidence: **99.31%**
590. **`tensorflow/core/common_runtime/base_collective_executor.cc`** -> AI Confidence: **99.31%**
591. **`tensorflow/core/common_runtime/collective_param_resolver_local.cc`** -> AI Confidence: **99.31%**
592. **`tensorflow/core/common_runtime/collective_test_util.cc`** -> AI Confidence: **99.31%**
593. **`tensorflow/core/common_runtime/collective_util.cc`** -> AI Confidence: **99.31%**
594. **`tensorflow/core/common_runtime/colocate_predecessor_trees_pass.cc`** -> AI Confidence: **99.31%**
595. **`tensorflow/core/common_runtime/colocation_graph.cc`** -> AI Confidence: **99.31%**
596. **`tensorflow/core/common_runtime/constant_folding.cc`** -> AI Confidence: **99.31%**
597. **`tensorflow/core/common_runtime/copy_tensor.cc`** -> AI Confidence: **99.31%**
598. **`tensorflow/core/common_runtime/device/device_event_mgr.cc`** -> AI Confidence: **99.31%**
599. **`tensorflow/core/common_runtime/device_propagation.cc`** -> AI Confidence: **99.31%**
600. **`tensorflow/core/common_runtime/direct_session.cc`** -> AI Confidence: **99.31%**
601. **`tensorflow/core/common_runtime/dynamic_device_mgr.cc`** -> AI Confidence: **99.31%**
602. **`tensorflow/core/common_runtime/eager/attr_builder.cc`** -> AI Confidence: **99.31%**
603. **`tensorflow/core/common_runtime/eager/context_distributed_manager.cc`** -> AI Confidence: **99.31%**
604. **`tensorflow/core/common_runtime/eager/copy_to_device_node.h`** -> AI Confidence: **99.31%**
605. **`tensorflow/core/common_runtime/eager/core.cc`** -> AI Confidence: **99.31%**
606. **`tensorflow/core/common_runtime/eager/custom_device_op_handler.cc`** -> AI Confidence: **99.31%**
607. **`tensorflow/core/common_runtime/eager/eager_executor.cc`** -> AI Confidence: **99.31%**
608. **`tensorflow/core/common_runtime/eager/execute.cc`** -> AI Confidence: **99.31%**
609. **`tensorflow/core/common_runtime/eager/kernel_and_device.cc`** -> AI Confidence: **99.31%**
610. **`tensorflow/core/common_runtime/eager/placement_utils.cc`** -> AI Confidence: **99.31%**
611. **`tensorflow/core/common_runtime/eager/summary_optimizer.cc`** -> AI Confidence: **99.31%**
612. **`tensorflow/core/common_runtime/eval_const_tensor.cc`** -> AI Confidence: **99.31%**
613. **`tensorflow/core/common_runtime/executor.cc`** -> AI Confidence: **99.31%**
614. **`tensorflow/core/common_runtime/function_def_utils.cc`** -> AI Confidence: **99.31%**
615. **`tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc`** -> AI Confidence: **99.31%**
616. **`tensorflow/core/common_runtime/gpu/gpu_device.cc`** -> AI Confidence: **99.31%**
617. **`tensorflow/core/common_runtime/gpu/gpu_util.cc`** -> AI Confidence: **99.31%**
618. **`tensorflow/core/common_runtime/gradients.cc`** -> AI Confidence: **99.31%**
619. **`tensorflow/core/common_runtime/graph_constructor_fuzz.cc`** -> AI Confidence: **99.31%**
620. **`tensorflow/core/common_runtime/inline_function_utils.cc`** -> AI Confidence: **99.31%**
621. **`tensorflow/core/common_runtime/isolate_placer_inspection_required_ops_pass.cc`** -> AI Confidence: **99.31%**
622. **`tensorflow/core/common_runtime/lower_function_call_op.cc`** -> AI Confidence: **99.31%**
623. **`tensorflow/core/common_runtime/mkl_layout_pass.cc`** -> AI Confidence: **99.31%**
624. **`tensorflow/core/common_runtime/node_file_writer.cc`** -> AI Confidence: **99.31%**
625. **`tensorflow/core/common_runtime/optimize_function_graph_utils.cc`** -> AI Confidence: **99.31%**
626. **`tensorflow/core/common_runtime/partitioning_utils.cc`** -> AI Confidence: **99.31%**
627. **`tensorflow/core/common_runtime/placer_inspection_required_ops_utils.cc`** -> AI Confidence: **99.31%**
628. **`tensorflow/core/common_runtime/pluggable_device/pluggable_device.cc`** -> AI Confidence: **99.31%**
629. **`tensorflow/core/common_runtime/pluggable_device/pluggable_device_bfc_allocator.cc`** -> AI Confidence: **99.31%**
630. **`tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc`** -> AI Confidence: **99.31%**
631. **`tensorflow/core/common_runtime/pool_allocator.cc`** -> AI Confidence: **99.31%**
632. **`tensorflow/core/common_runtime/process_function_library_runtime.cc`** -> AI Confidence: **99.31%**
633. **`tensorflow/core/common_runtime/process_util.cc`** -> AI Confidence: **99.31%**
634. **`tensorflow/core/common_runtime/propagator_debug_utils.cc`** -> AI Confidence: **99.31%**
635. **`tensorflow/core/common_runtime/propagator_state.cc`** -> AI Confidence: **99.31%**
636. **`tensorflow/core/common_runtime/quantize_training.cc`** -> AI Confidence: **99.31%**
637. **`tensorflow/core/common_runtime/rendezvous_mgr.cc`** -> AI Confidence: **99.31%**
638. **`tensorflow/core/common_runtime/replicate_constants_pass.cc`** -> AI Confidence: **99.31%**
639. **`tensorflow/core/common_runtime/replicate_per_replica_nodes.cc`** -> AI Confidence: **99.31%**
640. **`tensorflow/core/common_runtime/ring_alg.cc`** -> AI Confidence: **99.31%**
641. **`tensorflow/core/common_runtime/shape_refiner.cc`** -> AI Confidence: **99.31%**
642. **`tensorflow/core/common_runtime/simplify_ici_dummy_variables_pass.cc`** -> AI Confidence: **99.31%**
643. **`tensorflow/core/common_runtime/threadpool_device.cc`** -> AI Confidence: **99.31%**
644. **`tensorflow/core/common_runtime/threadpool_device_factory.cc`** -> AI Confidence: **99.31%**
645. **`tensorflow/core/common_runtime/type_inference.cc`** -> AI Confidence: **99.31%**
646. **`tensorflow/core/data/captured_function.cc`** -> AI Confidence: **99.31%**
647. **`tensorflow/core/data/compression_utils.cc`** -> AI Confidence: **99.31%**
648. **`tensorflow/core/data/dataset_utils.cc`** -> AI Confidence: **99.31%**
649. **`tensorflow/core/data/flat_map_utils.cc`** -> AI Confidence: **99.31%**
650. **`tensorflow/core/data/hash_utils.cc`** -> AI Confidence: **99.31%**
651. **`tensorflow/core/data/root_dataset.cc`** -> AI Confidence: **99.31%**
652. **`tensorflow/core/data/service/client/data_service_client.cc`** -> AI Confidence: **99.31%**
653. **`tensorflow/core/data/service/common.cc`** -> AI Confidence: **99.31%**
654. **`tensorflow/core/data/service/dispatcher_impl.cc`** -> AI Confidence: **99.31%**
655. **`tensorflow/core/data/service/snapshot/parallel_tfrecord_writer.cc`** -> AI Confidence: **99.31%**
656. **`tensorflow/core/data/service/snapshot/path_utils.cc`** -> AI Confidence: **99.31%**
657. **`tensorflow/core/data/service/snapshot/prefetched_split_provider.cc`** -> AI Confidence: **99.31%**
658. **`tensorflow/core/data/service/snapshot/snapshot_manager.cc`** -> AI Confidence: **99.31%**
659. **`tensorflow/core/data/service/snapshot/snapshot_split_provider.cc`** -> AI Confidence: **99.31%**
660. **`tensorflow/core/data/service/snapshot/test_utils.h`** -> AI Confidence: **99.31%**
661. **`tensorflow/core/data/service/task_runner.cc`** -> AI Confidence: **99.31%**
662. **`tensorflow/core/data/service/worker_impl.cc`** -> AI Confidence: **99.31%**
663. **`tensorflow/core/distributed_runtime/base_rendezvous_mgr.cc`** -> AI Confidence: **99.31%**
664. **`tensorflow/core/distributed_runtime/collective_param_resolver_distributed.cc`** -> AI Confidence: **99.31%**
665. **`tensorflow/core/distributed_runtime/collective_rma_distributed.cc`** -> AI Confidence: **99.31%**
666. **`tensorflow/core/distributed_runtime/coordination/coordination_service_barrier_proxy.cc`** -> AI Confidence: **99.31%**
667. **`tensorflow/core/distributed_runtime/eager/eager_service_impl.cc`** -> AI Confidence: **99.31%**
668. **`tensorflow/core/distributed_runtime/eager/remote_copy_node.cc`** -> AI Confidence: **99.31%**
669. **`tensorflow/core/distributed_runtime/graph_mgr.cc`** -> AI Confidence: **99.31%**
670. **`tensorflow/core/distributed_runtime/master.cc`** -> AI Confidence: **99.31%**
671. **`tensorflow/core/distributed_runtime/master_session.cc`** -> AI Confidence: **99.31%**
672. **`tensorflow/core/distributed_runtime/remote_device.cc`** -> AI Confidence: **99.31%**
673. **`tensorflow/core/distributed_runtime/rpc/eager/grpc_eager_service_impl.cc`** -> AI Confidence: **99.31%**
674. **`tensorflow/core/distributed_runtime/rpc/grpc_session.cc`** -> AI Confidence: **99.31%**
675. **`tensorflow/core/distributed_runtime/rpc/grpc_tensor_coding.cc`** -> AI Confidence: **99.31%**
676. **`tensorflow/core/distributed_runtime/rpc/grpc_tensorflow_server.cc`** -> AI Confidence: **99.31%**
677. **`tensorflow/core/distributed_runtime/rpc/grpc_testlib_server.cc`** -> AI Confidence: **99.31%**
678. **`tensorflow/core/distributed_runtime/rpc/grpc_worker_service.cc`** -> AI Confidence: **99.31%**
679. **`tensorflow/core/distributed_runtime/rpc/grpc_worker_service_impl.cc`** -> AI Confidence: **99.31%**
680. **`tensorflow/core/distributed_runtime/rpc_collective_executor_mgr.cc`** -> AI Confidence: **99.31%**
681. **`tensorflow/core/distributed_runtime/session_mgr.cc`** -> AI Confidence: **99.31%**
682. **`tensorflow/core/distributed_runtime/worker.cc`** -> AI Confidence: **99.31%**
683. **`tensorflow/core/distributed_runtime/worker_cache_partial.cc`** -> AI Confidence: **99.31%**
684. **`tensorflow/core/framework/attr_value_util.cc`** -> AI Confidence: **99.31%**
685. **`tensorflow/core/framework/common_shape_fns.cc`** -> AI Confidence: **99.31%**
686. **`tensorflow/core/framework/dataset.cc`** -> AI Confidence: **99.31%**
687. **`tensorflow/core/framework/function.cc`** -> AI Confidence: **99.31%**
688. **`tensorflow/core/framework/graph_def_util.cc`** -> AI Confidence: **99.31%**
689. **`tensorflow/core/framework/graph_to_functiondef.cc`** -> AI Confidence: **99.31%**
690. **`tensorflow/core/framework/local_rendezvous.cc`** -> AI Confidence: **99.31%**
691. **`tensorflow/core/framework/memory_types.cc`** -> AI Confidence: **99.31%**
692. **`tensorflow/core/framework/model.cc`** -> AI Confidence: **99.31%**
693. **`tensorflow/core/framework/node_def_builder.cc`** -> AI Confidence: **99.31%**
694. **`tensorflow/core/framework/op_def_util.cc`** -> AI Confidence: **99.31%**
695. **`tensorflow/core/framework/op_kernel.cc`** -> AI Confidence: **99.31%**
696. **`tensorflow/core/framework/op_kernel_test_base.h`** -> AI Confidence: **99.31%**
697. **`tensorflow/core/framework/op_segment.cc`** -> AI Confidence: **99.31%**
698. **`tensorflow/core/framework/ops_util.cc`** -> AI Confidence: **99.31%**
699. **`tensorflow/core/framework/reader_base.cc`** -> AI Confidence: **99.31%**
700. **`tensorflow/core/framework/run_handler.cc`** -> AI Confidence: **99.31%**
701. **`tensorflow/core/framework/shape_inference.cc`** -> AI Confidence: **99.31%**
702. **`tensorflow/core/framework/shape_inference_testutil.cc`** -> AI Confidence: **99.31%**
703. **`tensorflow/core/framework/tensor_shape.cc`** -> AI Confidence: **99.31%**
704. **`tensorflow/core/framework/tensor_shape_fuzz.cc`** -> AI Confidence: **99.31%**
705. **`tensorflow/core/framework/tensor_slice.cc`** -> AI Confidence: **99.31%**
706. **`tensorflow/core/graph/costmodel.cc`** -> AI Confidence: **99.31%**
707. **`tensorflow/core/graph/graph_debug_info_builder.cc`** -> AI Confidence: **99.31%**
708. **`tensorflow/core/graph/graph_partition.cc`** -> AI Confidence: **99.31%**
709. **`tensorflow/core/graph/node_builder.cc`** -> AI Confidence: **99.31%**
710. **`tensorflow/core/graph/optimizer_cse.cc`** -> AI Confidence: **99.31%**
711. **`tensorflow/core/graph/regularization/simple_delete.cc`** -> AI Confidence: **99.31%**
712. **`tensorflow/core/graph/subgraph.cc`** -> AI Confidence: **99.31%**
713. **`tensorflow/core/graph/validate.cc`** -> AI Confidence: **99.31%**
714. **`tensorflow/core/grappler/clusters/single_machine.cc`** -> AI Confidence: **99.31%**
715. **`tensorflow/core/grappler/clusters/utils.cc`** -> AI Confidence: **99.31%**
716. **`tensorflow/core/grappler/costs/analytical_cost_estimator.cc`** -> AI Confidence: **99.31%**
717. **`tensorflow/core/grappler/costs/graph_properties.cc`** -> AI Confidence: **99.31%**
718. **`tensorflow/core/grappler/costs/measuring_cost_estimator.cc`** -> AI Confidence: **99.31%**
719. **`tensorflow/core/grappler/costs/op_level_cost_estimator.cc`** -> AI Confidence: **99.31%**
720. **`tensorflow/core/grappler/costs/utils.cc`** -> AI Confidence: **99.31%**
721. **`tensorflow/core/grappler/graph_analyzer/gen_node.cc`** -> AI Confidence: **99.31%**
722. **`tensorflow/core/grappler/graph_analyzer/graph_analyzer.cc`** -> AI Confidence: **99.31%**
723. **`tensorflow/core/grappler/graph_analyzer/graph_analyzer_tool.cc`** -> AI Confidence: **99.31%**
724. **`tensorflow/core/grappler/graph_analyzer/sig_node.cc`** -> AI Confidence: **99.31%**
725. **`tensorflow/core/grappler/graph_topology_view.cc`** -> AI Confidence: **99.31%**
726. **`tensorflow/core/grappler/grappler_item.cc`** -> AI Confidence: **99.31%**
727. **`tensorflow/core/grappler/grappler_item_builder.cc`** -> AI Confidence: **99.31%**
728. **`tensorflow/core/grappler/inputs/file_input_yielder.cc`** -> AI Confidence: **99.31%**
729. **`tensorflow/core/grappler/inputs/trivial_test_graph_input_yielder.cc`** -> AI Confidence: **99.31%**
730. **`tensorflow/core/grappler/mutable_graph_view.cc`** -> AI Confidence: **99.31%**
731. **`tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc`** -> AI Confidence: **99.31%**
732. **`tensorflow/core/grappler/optimizers/auto_parallel.cc`** -> AI Confidence: **99.31%**
733. **`tensorflow/core/grappler/optimizers/common_subgraph_elimination.cc`** -> AI Confidence: **99.31%**
734. **`tensorflow/core/grappler/optimizers/constant_folding.cc`** -> AI Confidence: **99.31%**
735. **`tensorflow/core/grappler/optimizers/data/auto_shard.cc`** -> AI Confidence: **99.31%**
736. **`tensorflow/core/grappler/optimizers/data/autotune_buffer_sizes.cc`** -> AI Confidence: **99.31%**
737. **`tensorflow/core/grappler/optimizers/data/disable_prefetch_legacy_autotune.cc`** -> AI Confidence: **99.31%**
738. **`tensorflow/core/grappler/optimizers/data/make_deterministic.cc`** -> AI Confidence: **99.31%**
739. **`tensorflow/core/grappler/optimizers/data/make_sloppy.cc`** -> AI Confidence: **99.31%**
740. **`tensorflow/core/grappler/optimizers/data/map_fusion.cc`** -> AI Confidence: **99.31%**
741. **`tensorflow/core/grappler/optimizers/data/parallel_batch.cc`** -> AI Confidence: **99.31%**
742. **`tensorflow/core/grappler/optimizers/data/seq_interleave_prefetch.cc`** -> AI Confidence: **99.31%**
743. **`tensorflow/core/grappler/optimizers/data/shuffle_and_repeat_fusion.cc`** -> AI Confidence: **99.31%**
744. **`tensorflow/core/grappler/optimizers/generic_layout_optimizer.cc`** -> AI Confidence: **99.31%**
745. **`tensorflow/core/grappler/optimizers/generic_layout_optimizer_transposer.cc`** -> AI Confidence: **99.31%**
746. **`tensorflow/core/grappler/optimizers/loop_optimizer.cc`** -> AI Confidence: **99.31%**
747. **`tensorflow/core/grappler/optimizers/model_pruner.cc`** -> AI Confidence: **99.31%**
748. **`tensorflow/core/grappler/optimizers/pin_to_host_optimizer.cc`** -> AI Confidence: **99.31%**
749. **`tensorflow/core/grappler/optimizers/remapper.cc`** -> AI Confidence: **99.31%**
750. **`tensorflow/core/grappler/optimizers/scoped_allocator_optimizer.cc`** -> AI Confidence: **99.31%**
751. **`tensorflow/core/grappler/utils.cc`** -> AI Confidence: **99.31%**
752. **`tensorflow/core/grappler/utils/frame_test.cc`** -> AI Confidence: **99.31%**
753. **`tensorflow/core/grappler/utils/functions.cc`** -> AI Confidence: **99.31%**
754. **`tensorflow/core/grappler/utils/graph_view.cc`** -> AI Confidence: **99.31%**
755. **`tensorflow/core/grappler/utils/topological_sort.cc`** -> AI Confidence: **99.31%**
756. **`tensorflow/core/grappler/utils/topological_sort_test.cc`** -> AI Confidence: **99.31%**
757. **`tensorflow/core/ir/importexport/convert_attributes.cc`** -> AI Confidence: **99.31%**
758. **`tensorflow/core/ir/importexport/convert_tensor.cc`** -> AI Confidence: **99.31%**
759. **`tensorflow/core/ir/importexport/convert_types.cc`** -> AI Confidence: **99.31%**
760. **`tensorflow/core/ir/importexport/functiondef_export.cc`** -> AI Confidence: **99.31%**
761. **`tensorflow/core/ir/importexport/functiondef_import.cc`** -> AI Confidence: **99.31%**
762. **`tensorflow/core/ir/importexport/tests/roundtrip/roundtrip.cc`** -> AI Confidence: **99.31%**
763. **`tensorflow/core/ir/ops.cc`** -> AI Confidence: **99.31%**
764. **`tensorflow/core/ir/utils/shape_inference_utils.cc`** -> AI Confidence: **99.31%**
765. **`tensorflow/core/kernels/aggregate_ops.cc`** -> AI Confidence: **99.31%**
766. **`tensorflow/core/kernels/avgpooling_op.cc`** -> AI Confidence: **99.31%**
767. **`tensorflow/core/kernels/batch_kernels.cc`** -> AI Confidence: **99.31%**
768. **`tensorflow/core/kernels/batching_util/batch_resource_base.cc`** -> AI Confidence: **99.31%**
769. **`tensorflow/core/kernels/batchtospace_op.cc`** -> AI Confidence: **99.31%**
770. **`tensorflow/core/kernels/broadcast_to_op.cc`** -> AI Confidence: **99.31%**
771. **`tensorflow/core/kernels/checkpoint_callback_manager.cc`** -> AI Confidence: **99.31%**
772. **`tensorflow/core/kernels/clustering_ops.cc`** -> AI Confidence: **99.31%**
773. **`tensorflow/core/kernels/concat_op.cc`** -> AI Confidence: **99.31%**
774. **`tensorflow/core/kernels/constant_op.cc`** -> AI Confidence: **99.31%**
775. **`tensorflow/core/kernels/conv_grad_input_ops_3d.cc`** -> AI Confidence: **99.31%**
776. **`tensorflow/core/kernels/conv_ops_fused_image_transform.cc`** -> AI Confidence: **99.31%**
777. **`tensorflow/core/kernels/conv_ops_gpu.cc`** -> AI Confidence: **99.31%**
778. **`tensorflow/core/kernels/count_ops.cc`** -> AI Confidence: **99.31%**
779. **`tensorflow/core/kernels/data/batch_dataset_op.cc`** -> AI Confidence: **99.31%**
780. **`tensorflow/core/kernels/data/concatenate_dataset_op.cc`** -> AI Confidence: **99.31%**
781. **`tensorflow/core/kernels/data/dataset_ops.cc`** -> AI Confidence: **99.31%**
782. **`tensorflow/core/kernels/data/experimental/csv_dataset_op.cc`** -> AI Confidence: **99.31%**
783. **`tensorflow/core/kernels/data/experimental/data_service_dataset_op.cc`** -> AI Confidence: **99.31%**
784. **`tensorflow/core/kernels/data/experimental/data_service_ops.cc`** -> AI Confidence: **99.31%**
785. **`tensorflow/core/kernels/data/experimental/directed_interleave_dataset_op.cc`** -> AI Confidence: **99.31%**
786. **`tensorflow/core/kernels/data/experimental/distributed_save_op.cc`** -> AI Confidence: **99.31%**
787. **`tensorflow/core/kernels/data/experimental/group_by_reducer_dataset_op.cc`** -> AI Confidence: **99.31%**
788. **`tensorflow/core/kernels/data/experimental/group_by_window_dataset_op.cc`** -> AI Confidence: **99.31%**
789. **`tensorflow/core/kernels/data/experimental/map_and_batch_dataset_op.cc`** -> AI Confidence: **99.31%**
790. **`tensorflow/core/kernels/data/experimental/matching_files_dataset_op.cc`** -> AI Confidence: **99.31%**
791. **`tensorflow/core/kernels/data/experimental/parse_example_dataset_op.cc`** -> AI Confidence: **99.31%**
792. **`tensorflow/core/kernels/data/experimental/sliding_window_dataset_op.cc`** -> AI Confidence: **99.31%**
793. **`tensorflow/core/kernels/data/finalize_dataset_op.cc`** -> AI Confidence: **99.31%**
794. **`tensorflow/core/kernels/data/fixed_length_record_dataset_op.cc`** -> AI Confidence: **99.31%**
795. **`tensorflow/core/kernels/data/interleave_dataset_op.cc`** -> AI Confidence: **99.31%**
796. **`tensorflow/core/kernels/data/map_defun_op.cc`** -> AI Confidence: **99.31%**
797. **`tensorflow/core/kernels/data/padded_batch_dataset_op.cc`** -> AI Confidence: **99.31%**
798. **`tensorflow/core/kernels/data/parallel_batch_dataset_op.cc`** -> AI Confidence: **99.31%**
799. **`tensorflow/core/kernels/data/parallel_filter_dataset_op.cc`** -> AI Confidence: **99.31%**
800. **`tensorflow/core/kernels/data/parallel_interleave_dataset_op.cc`** -> AI Confidence: **99.31%**
801. **`tensorflow/core/kernels/data/parallel_map_dataset_op.cc`** -> AI Confidence: **99.31%**
802. **`tensorflow/core/kernels/data/prefetch_autotuner.cc`** -> AI Confidence: **99.31%**
803. **`tensorflow/core/kernels/data/prefetch_dataset_op.cc`** -> AI Confidence: **99.31%**
804. **`tensorflow/core/kernels/data/shuffle_dataset_op.cc`** -> AI Confidence: **99.31%**
805. **`tensorflow/core/kernels/data/tf_record_dataset_op.cc`** -> AI Confidence: **99.31%**
806. **`tensorflow/core/kernels/data/window_dataset_op.cc`** -> AI Confidence: **99.31%**
807. **`tensorflow/core/kernels/data/zip_dataset_op.cc`** -> AI Confidence: **99.31%**
808. **`tensorflow/core/kernels/data_format_ops.cc`** -> AI Confidence: **99.31%**
809. **`tensorflow/core/kernels/debug_ops.h`** -> AI Confidence: **99.31%**
810. **`tensorflow/core/kernels/decode_proto_op.cc`** -> AI Confidence: **99.31%**
811. **`tensorflow/core/kernels/decode_raw_op.cc`** -> AI Confidence: **99.31%**
812. **`tensorflow/core/kernels/decode_wav_op.cc`** -> AI Confidence: **99.31%**
813. **`tensorflow/core/kernels/depthwise_conv_op.cc`** -> AI Confidence: **99.31%**
814. **`tensorflow/core/kernels/dequantize_op.cc`** -> AI Confidence: **99.31%**
815. **`tensorflow/core/kernels/deserialize_sparse_string_op.cc`** -> AI Confidence: **99.31%**
816. **`tensorflow/core/kernels/deserialize_sparse_variant_op.cc`** -> AI Confidence: **99.31%**
817. **`tensorflow/core/kernels/dilation_ops.cc`** -> AI Confidence: **99.31%**
818. **`tensorflow/core/kernels/dynamic_stitch_op.cc`** -> AI Confidence: **99.31%**
819. **`tensorflow/core/kernels/edit_distance_op.cc`** -> AI Confidence: **99.31%**
820. **`tensorflow/core/kernels/example_parsing_ops.cc`** -> AI Confidence: **99.31%**
821. **`tensorflow/core/kernels/fft_ops.cc`** -> AI Confidence: **99.31%**
822. **`tensorflow/core/kernels/fifo_queue.cc`** -> AI Confidence: **99.31%**
823. **`tensorflow/core/kernels/fingerprint_op.cc`** -> AI Confidence: **99.31%**
824. **`tensorflow/core/kernels/fractional_avg_pool_op.cc`** -> AI Confidence: **99.31%**
825. **`tensorflow/core/kernels/fractional_max_pool_op.cc`** -> AI Confidence: **99.31%**
826. **`tensorflow/core/kernels/function_ops.cc`** -> AI Confidence: **99.31%**
827. **`tensorflow/core/kernels/functional_ops.cc`** -> AI Confidence: **99.31%**
828. **`tensorflow/core/kernels/gather_op.cc`** -> AI Confidence: **99.31%**
829. **`tensorflow/core/kernels/image/adjust_hue_op.cc`** -> AI Confidence: **99.31%**
830. **`tensorflow/core/kernels/image/adjust_saturation_op.cc`** -> AI Confidence: **99.31%**
831. **`tensorflow/core/kernels/image/decode_image_op.cc`** -> AI Confidence: **99.31%**
832. **`tensorflow/core/kernels/image/encode_png_op.cc`** -> AI Confidence: **99.31%**
833. **`tensorflow/core/kernels/image/mirror_pad_op.cc`** -> AI Confidence: **99.31%**
834. **`tensorflow/core/kernels/image/resize_area_op.cc`** -> AI Confidence: **99.31%**
835. **`tensorflow/core/kernels/image/sample_distorted_bounding_box_op.cc`** -> AI Confidence: **99.31%**
836. **`tensorflow/core/kernels/linalg/lu_op_gpu.cu.cc`** -> AI Confidence: **99.31%**
837. **`tensorflow/core/kernels/linalg/matrix_solve_op.cc`** -> AI Confidence: **99.31%**
838. **`tensorflow/core/kernels/linalg/self_adjoint_eig_v2_op_gpu.cc`** -> AI Confidence: **99.31%**
839. **`tensorflow/core/kernels/linalg/svd_op_gpu.cu.cc`** -> AI Confidence: **99.31%**
840. **`tensorflow/core/kernels/list_kernels.cc`** -> AI Confidence: **99.31%**
841. **`tensorflow/core/kernels/list_kernels.cu.cc`** -> AI Confidence: **99.31%**
842. **`tensorflow/core/kernels/logging_ops.cc`** -> AI Confidence: **99.31%**
843. **`tensorflow/core/kernels/lookup_util.cc`** -> AI Confidence: **99.31%**
844. **`tensorflow/core/kernels/matmul_op_fused.cc`** -> AI Confidence: **99.31%**
845. **`tensorflow/core/kernels/matmul_util.cc`** -> AI Confidence: **99.31%**
846. **`tensorflow/core/kernels/mfcc_op.cc`** -> AI Confidence: **99.31%**
847. **`tensorflow/core/kernels/mkl/mkl_concat_op.cc`** -> AI Confidence: **99.31%**
848. **`tensorflow/core/kernels/mkl/mkl_conv_ops.cc`** -> AI Confidence: **99.31%**
849. **`tensorflow/core/kernels/mkl/mkl_dequantize_op.cc`** -> AI Confidence: **99.31%**
850. **`tensorflow/core/kernels/mkl/mkl_fused_batch_norm_op.cc`** -> AI Confidence: **99.31%**
851. **`tensorflow/core/kernels/mkl/mkl_matmul_op.cc`** -> AI Confidence: **99.31%**
852. **`tensorflow/core/kernels/mkl/mkl_quantize_op.cc`** -> AI Confidence: **99.31%**
853. **`tensorflow/core/kernels/mkl/mkl_requantization_range_per_channel_op.cc`** -> AI Confidence: **99.31%**
854. **`tensorflow/core/kernels/pack_op.cc`** -> AI Confidence: **99.31%**
855. **`tensorflow/core/kernels/pad_op.cc`** -> AI Confidence: **99.31%**
856. **`tensorflow/core/kernels/padding_fifo_queue.cc`** -> AI Confidence: **99.31%**
857. **`tensorflow/core/kernels/parameterized_truncated_normal_op.cc`** -> AI Confidence: **99.31%**
858. **`tensorflow/core/kernels/parameterized_truncated_normal_op_gpu.cu.cc`** -> AI Confidence: **99.31%**
859. **`tensorflow/core/kernels/pooling_ops_common.cc`** -> AI Confidence: **99.31%**
860. **`tensorflow/core/kernels/priority_queue.cc`** -> AI Confidence: **99.31%**
861. **`tensorflow/core/kernels/quantize_op.cc`** -> AI Confidence: **99.31%**
862. **`tensorflow/core/kernels/quantized_conv_ops.cc`** -> AI Confidence: **99.31%**
863. **`tensorflow/core/kernels/quantized_instance_norm.cc`** -> AI Confidence: **99.31%**
864. **`tensorflow/core/kernels/queue_base.cc`** -> AI Confidence: **99.31%**
865. **`tensorflow/core/kernels/queue_op.cc`** -> AI Confidence: **99.31%**
866. **`tensorflow/core/kernels/ragged_range_op.cc`** -> AI Confidence: **99.31%**
867. **`tensorflow/core/kernels/ragged_tensor_from_variant_op.cc`** -> AI Confidence: **99.31%**
868. **`tensorflow/core/kernels/ragged_tensor_to_sparse_kernel.cc`** -> AI Confidence: **99.31%**
869. **`tensorflow/core/kernels/ragged_tensor_to_tensor_op.cc`** -> AI Confidence: **99.31%**
870. **`tensorflow/core/kernels/random_index_shuffle.cc`** -> AI Confidence: **99.31%**
871. **`tensorflow/core/kernels/random_index_shuffle_ops.cc`** -> AI Confidence: **99.31%**
872. **`tensorflow/core/kernels/random_shuffle_queue_op.cc`** -> AI Confidence: **99.31%**
873. **`tensorflow/core/kernels/range_sampler.cc`** -> AI Confidence: **99.31%**
874. **`tensorflow/core/kernels/reduce_join_op.cc`** -> AI Confidence: **99.31%**
875. **`tensorflow/core/kernels/reshape_util.cc`** -> AI Confidence: **99.31%**
876. **`tensorflow/core/kernels/reverse_op.cc`** -> AI Confidence: **99.31%**
877. **`tensorflow/core/kernels/roll_op.cc`** -> AI Confidence: **99.31%**
878. **`tensorflow/core/kernels/save_restore_tensor.cc`** -> AI Confidence: **99.31%**
879. **`tensorflow/core/kernels/save_restore_v2_ops.cc`** -> AI Confidence: **99.31%**
880. **`tensorflow/core/kernels/sdca_internal.cc`** -> AI Confidence: **99.31%**
881. **`tensorflow/core/kernels/slice_op.cc`** -> AI Confidence: **99.31%**
882. **`tensorflow/core/kernels/spacetobatch_op.cc`** -> AI Confidence: **99.31%**
883. **`tensorflow/core/kernels/sparse/kernels.cc`** -> AI Confidence: **99.31%**
884. **`tensorflow/core/kernels/sparse/nnz_op.cc`** -> AI Confidence: **99.31%**
885. **`tensorflow/core/kernels/sparse/sparse_mat_mul_op.cc`** -> AI Confidence: **99.31%**
886. **`tensorflow/core/kernels/sparse_add_op.cc`** -> AI Confidence: **99.31%**
887. **`tensorflow/core/kernels/sparse_concat_op.cc`** -> AI Confidence: **99.31%**
888. **`tensorflow/core/kernels/sparse_concat_op_gpu.cu.cc`** -> AI Confidence: **99.31%**
889. **`tensorflow/core/kernels/sparse_sparse_binary_op_shared.cc`** -> AI Confidence: **99.31%**
890. **`tensorflow/core/kernels/sparse_utils.cc`** -> AI Confidence: **99.31%**
891. **`tensorflow/core/kernels/spectrogram_op.cc`** -> AI Confidence: **99.31%**
892. **`tensorflow/core/kernels/spectrogram_test_utils.cc`** -> AI Confidence: **99.31%**
893. **`tensorflow/core/kernels/split_v_op.cc`** -> AI Confidence: **99.31%**
894. **`tensorflow/core/kernels/strided_slice_op.cc`** -> AI Confidence: **99.31%**
895. **`tensorflow/core/kernels/string_join_op.cc`** -> AI Confidence: **99.31%**
896. **`tensorflow/core/kernels/string_ngrams_op.cc`** -> AI Confidence: **99.31%**
897. **`tensorflow/core/kernels/substr_op.cc`** -> AI Confidence: **99.31%**
898. **`tensorflow/core/kernels/tensor_array_ops.cc`** -> AI Confidence: **99.31%**
899. **`tensorflow/core/kernels/transpose_functor_cpu.cc`** -> AI Confidence: **99.31%**
900. **`tensorflow/core/kernels/unicode_ops.cc`** -> AI Confidence: **99.31%**
901. **`tensorflow/core/kernels/unpack_op.cc`** -> AI Confidence: **99.31%**
902. **`tensorflow/core/kernels/variant_ops_util.cc`** -> AI Confidence: **99.31%**
903. **`tensorflow/core/nccl/nccl_manager.cc`** -> AI Confidence: **99.31%**
904. **`tensorflow/core/ops/array_ops.cc`** -> AI Confidence: **99.31%**
905. **`tensorflow/core/ops/math_ops.cc`** -> AI Confidence: **99.31%**
906. **`tensorflow/core/ops/nn_ops.cc`** -> AI Confidence: **99.31%**
907. **`tensorflow/core/ops/resource_variable_ops.cc`** -> AI Confidence: **99.31%**
908. **`tensorflow/core/ops/sparse_csr_matrix_ops.cc`** -> AI Confidence: **99.31%**
909. **`tensorflow/core/profiler/convert/xplane_to_step_stats.cc`** -> AI Confidence: **99.31%**
910. **`tensorflow/core/profiler/internal/print_model_analysis.cc`** -> AI Confidence: **99.31%**
911. **`tensorflow/core/profiler/internal/tfprof_code.cc`** -> AI Confidence: **99.31%**
912. **`tensorflow/core/profiler/internal/tfprof_graph.cc`** -> AI Confidence: **99.31%**
913. **`tensorflow/core/profiler/internal/tfprof_scope.cc`** -> AI Confidence: **99.31%**
914. **`tensorflow/core/profiler/internal/tfprof_stats.cc`** -> AI Confidence: **99.31%**
915. **`tensorflow/core/profiler/internal/tfprof_timeline.cc`** -> AI Confidence: **99.31%**
916. **`tensorflow/core/profiler/tfprof_options.cc`** -> AI Confidence: **99.31%**
917. **`tensorflow/core/runtime_fallback/kernel/attr_util.cc`** -> AI Confidence: **99.31%**
918. **`tensorflow/core/runtime_fallback/kernel/kernel_fallback_tensor.cc`** -> AI Confidence: **99.31%**
919. **`tensorflow/core/runtime_fallback/runtime/fallback_batch_kernel.cc`** -> AI Confidence: **99.31%**
920. **`tensorflow/core/runtime_fallback/util/attr_util.cc`** -> AI Confidence: **99.31%**
921. **`tensorflow/core/summary/loader.cc`** -> AI Confidence: **99.31%**
922. **`tensorflow/core/summary/summary_converter.cc`** -> AI Confidence: **99.31%**
923. **`tensorflow/core/summary/summary_db_writer.cc`** -> AI Confidence: **99.31%**
924. **`tensorflow/core/tfrt/gpu/kernel/gpu_runner.cc`** -> AI Confidence: **99.31%**
925. **`tensorflow/core/tfrt/graph_executor/graph_execution_options.cc`** -> AI Confidence: **99.31%**
926. **`tensorflow/core/tfrt/ifrt/ifrt_device_utils.cc`** -> AI Confidence: **99.31%**
927. **`tensorflow/core/tfrt/kernels/stream_ops.cc`** -> AI Confidence: **99.31%**
928. **`tensorflow/core/tfrt/kernels/stream_ops_util.cc`** -> AI Confidence: **99.31%**
929. **`tensorflow/core/tfrt/mlrt/interpreter/execute.cc`** -> AI Confidence: **99.31%**
930. **`tensorflow/core/tfrt/run_handler_thread_pool/run_handler.cc`** -> AI Confidence: **99.31%**
931. **`tensorflow/core/tfrt/run_handler_thread_pool/run_handler_util.cc`** -> AI Confidence: **99.31%**
932. **`tensorflow/core/tfrt/saved_model/saved_model.cc`** -> AI Confidence: **99.31%**
933. **`tensorflow/core/tfrt/saved_model/saved_model_testutil.cc`** -> AI Confidence: **99.31%**
934. **`tensorflow/core/tfrt/utils/graph_partition.cc`** -> AI Confidence: **99.31%**
935. **`tensorflow/core/tfrt/utils/graph_partition_test.cc`** -> AI Confidence: **99.31%**
936. **`tensorflow/core/tfrt/utils/tfrt_graph_execution_state.cc`** -> AI Confidence: **99.31%**
937. **`tensorflow/core/tpu/graph_rewrite/combine_tpu_embedding_load_retrieve_pass.cc`** -> AI Confidence: **99.31%**
938. **`tensorflow/core/tpu/graph_rewrite/configure_tpu_embedding_rewrite_pass.cc`** -> AI Confidence: **99.31%**
939. **`tensorflow/core/tpu/graph_rewrite/distributed_tpu_configuration_rewrite_pass.cc`** -> AI Confidence: **99.31%**
940. **`tensorflow/core/tpu/graph_rewrite/distributed_tpu_rewrite_helpers.cc`** -> AI Confidence: **99.31%**
941. **`tensorflow/core/tpu/graph_rewrite/host_training_loop_optimization_util.cc`** -> AI Confidence: **99.31%**
942. **`tensorflow/core/tpu/graph_rewrite/tpu_embedding_software_deduplication_rewrite_pass.cc`** -> AI Confidence: **99.31%**
943. **`tensorflow/core/tpu/graph_rewrite/update_tpu_embedding_ops_passes.cc`** -> AI Confidence: **99.31%**
944. **`tensorflow/core/tpu/graph_rewrite/variable_merger_pass.cc`** -> AI Confidence: **99.31%**
945. **`tensorflow/core/tpu/kernels/sparse_core_ops_utils.cc`** -> AI Confidence: **99.31%**
946. **`tensorflow/core/tpu/kernels/tpu_compilation_cache_interface.cc`** -> AI Confidence: **99.31%**
947. **`tensorflow/core/tpu/kernels/tpu_compilation_cache_service.cc`** -> AI Confidence: **99.31%**
948. **`tensorflow/core/tpu/kernels/tpu_compile_op.cc`** -> AI Confidence: **99.31%**
949. **`tensorflow/core/tpu/kernels/tpu_compile_op_common.cc`** -> AI Confidence: **99.31%**
950. **`tensorflow/core/tpu/kernels/tpu_compile_op_support.cc`** -> AI Confidence: **99.31%**
951. **`tensorflow/core/tpu/kernels/tpu_configuration_ops.cc`** -> AI Confidence: **99.31%**
952. **`tensorflow/core/tpu/kernels/tpu_embedding_enqueue_ops.cc`** -> AI Confidence: **99.31%**
953. **`tensorflow/core/tpu/kernels/tpu_embedding_load_retrieve_ops.cc`** -> AI Confidence: **99.31%**
954. **`tensorflow/core/tpu/kernels/tpu_execute_op.cc`** -> AI Confidence: **99.31%**
955. **`tensorflow/core/tpu/kernels/tpu_op_util.cc`** -> AI Confidence: **99.31%**
956. **`tensorflow/core/tpu/kernels/tpu_reshard_variables_op.cc`** -> AI Confidence: **99.31%**
957. **`tensorflow/core/tpu/kernels/xla/host_compute_ops.cc`** -> AI Confidence: **99.31%**
958. **`tensorflow/core/tpu/ops/host_compute_ops.cc`** -> AI Confidence: **99.31%**
959. **`tensorflow/core/tpu/ops/tpu_embedding_ops.cc`** -> AI Confidence: **99.31%**
960. **`tensorflow/core/tpu/ops/tpu_partitioned_input_op.cc`** -> AI Confidence: **99.31%**
961. **`tensorflow/core/tpu/ops/tpu_partitioned_output_op.cc`** -> AI Confidence: **99.31%**
962. **`tensorflow/core/tpu/tpu_compile.cc`** -> AI Confidence: **99.31%**
963. **`tensorflow/core/tpu/tpu_embedding_configuration_proto_rewrite.cc`** -> AI Confidence: **99.31%**
964. **`tensorflow/core/tpu/tpu_embedding_optimization_parameters_utils.cc`** -> AI Confidence: **99.31%**
965. **`tensorflow/core/tpu/tpu_embedding_output_layout_utils.cc`** -> AI Confidence: **99.31%**
966. **`tensorflow/core/tpu/tpu_embedding_spmd_sharding_utils.cc`** -> AI Confidence: **99.31%**
967. **`tensorflow/core/transforms/constant_folding/pass.cc`** -> AI Confidence: **99.31%**
968. **`tensorflow/core/transforms/graph_compactor/pass.cc`** -> AI Confidence: **99.31%**
969. **`tensorflow/core/transforms/remapper/pass.cc`** -> AI Confidence: **99.31%**
970. **`tensorflow/core/transforms/shape_inference/pass.cc`** -> AI Confidence: **99.31%**
971. **`tensorflow/core/transforms/toposort/pass.cc`** -> AI Confidence: **99.31%**
972. **`tensorflow/core/util/autotune_maps/autotune_serialize.cc`** -> AI Confidence: **99.31%**
973. **`tensorflow/core/util/debug_data_dumper.cc`** -> AI Confidence: **99.31%**
974. **`tensorflow/core/util/debug_events_writer.cc`** -> AI Confidence: **99.31%**
975. **`tensorflow/core/util/equal_graph_def.cc`** -> AI Confidence: **99.31%**
976. **`tensorflow/core/util/example_proto_fast_parsing.cc`** -> AI Confidence: **99.31%**
977. **`tensorflow/core/util/example_proto_helper.cc`** -> AI Confidence: **99.31%**
978. **`tensorflow/core/util/proto/proto_utils.cc`** -> AI Confidence: **99.31%**
979. **`tensorflow/core/util/quantization/uniform_quant_ops_params.cc`** -> AI Confidence: **99.31%**
980. **`tensorflow/core/util/ragged_to_dense_util.cc`** -> AI Confidence: **99.31%**
981. **`tensorflow/core/util/stat_summarizer.cc`** -> AI Confidence: **99.31%**
982. **`tensorflow/core/util/tensor_bundle/byte_swap_tensor.cc`** -> AI Confidence: **99.31%**
983. **`tensorflow/core/util/tensor_bundle/tensor_bundle.cc`** -> AI Confidence: **99.31%**
984. **`tensorflow/core/util/tensor_slice_reader.cc`** -> AI Confidence: **99.31%**
985. **`tensorflow/core/util/tensor_slice_set.cc`** -> AI Confidence: **99.31%**
986. **`tensorflow/core/util/tensor_slice_writer.cc`** -> AI Confidence: **99.31%**
987. **`tensorflow/dtensor/cc/dtensor_device.cc`** -> AI Confidence: **99.31%**
988. **`tensorflow/dtensor/cc/dtensor_device_util.cc`** -> AI Confidence: **99.31%**
989. **`tensorflow/dtensor/cc/small_constant_optimization.cc`** -> AI Confidence: **99.31%**
990. **`tensorflow/dtensor/mlir/collectives.cc`** -> AI Confidence: **99.31%**
991. **`tensorflow/dtensor/mlir/dtensor_allreduce_combine_optimization.cc`** -> AI Confidence: **99.31%**
992. **`tensorflow/dtensor/mlir/dtensor_allreduce_sum_optimization.cc`** -> AI Confidence: **99.31%**
993. **`tensorflow/dtensor/mlir/dtensor_multi_device_expansion.cc`** -> AI Confidence: **99.31%**
994. **`tensorflow/dtensor/mlir/dtensor_send_recv.cc`** -> AI Confidence: **99.31%**
995. **`tensorflow/dtensor/mlir/expansions/concat_spmd_expander.cc`** -> AI Confidence: **99.31%**
996. **`tensorflow/dtensor/mlir/expansions/conv_spmd_expander.cc`** -> AI Confidence: **99.31%**
997. **`tensorflow/dtensor/mlir/expansions/dataparallel_spmd_expander.cc`** -> AI Confidence: **99.31%**
998. **`tensorflow/dtensor/mlir/expansions/einsum_spmd_expander.cc`** -> AI Confidence: **99.31%**
999. **`tensorflow/dtensor/mlir/expansions/expanddims_spmd_expander.cc`** -> AI Confidence: **99.31%**
1000. **`tensorflow/dtensor/mlir/expansions/fft_spmd_expander.cc`** -> AI Confidence: **99.31%**
1001. **`tensorflow/dtensor/mlir/expansions/gather_spmd_expander.cc`** -> AI Confidence: **99.31%**
1002. **`tensorflow/dtensor/mlir/expansions/in_top_k_spmd_expander.cc`** -> AI Confidence: **99.31%**
1003. **`tensorflow/dtensor/mlir/expansions/reduce_spmd_expander.cc`** -> AI Confidence: **99.31%**
1004. **`tensorflow/dtensor/mlir/expansions/resource_spmd_expander.cc`** -> AI Confidence: **99.31%**
1005. **`tensorflow/dtensor/mlir/expansions/scatter_spmd_expander.cc`** -> AI Confidence: **99.31%**
1006. **`tensorflow/dtensor/mlir/expansions/slice_spmd_expander.cc`** -> AI Confidence: **99.31%**
1007. **`tensorflow/dtensor/mlir/expansions/softmax_spmd_expander.cc`** -> AI Confidence: **99.31%**
1008. **`tensorflow/dtensor/mlir/expansions/squeeze_spmd_expander.cc`** -> AI Confidence: **99.31%**
1009. **`tensorflow/dtensor/mlir/layout_propagation_v2.cc`** -> AI Confidence: **99.31%**
1010. **`tensorflow/dtensor/mlir/mesh_propagation.cc`** -> AI Confidence: **99.31%**
1011. **`tensorflow/dtensor/mlir/spmd_expander_common.cc`** -> AI Confidence: **99.31%**
1012. **`tensorflow/dtensor/mlir/utils/collective_lowering.cc`** -> AI Confidence: **99.31%**
1013. **`tensorflow/examples/speech_commands/recognize_commands.cc`** -> AI Confidence: **99.31%**
1014. **`tensorflow/java/src/gen/cc/op_gen_main.cc`** -> AI Confidence: **99.31%**
1015. **`tensorflow/java/src/gen/cc/op_specs.cc`** -> AI Confidence: **99.31%**
1016. **`tensorflow/java/src/main/native/graph_jni.cc`** -> AI Confidence: **99.31%**
1017. **`tensorflow/java/src/main/native/tensor_jni.cc`** -> AI Confidence: **99.31%**
1018. **`tensorflow/lite/acceleration/configuration/proto_to_flatbuffer.cc`** -> AI Confidence: **99.31%**
1019. **`tensorflow/lite/core/api/flatbuffer_conversions.cc`** -> AI Confidence: **99.31%**
1020. **`tensorflow/lite/core/async/interop/reconcile_fns.cc`** -> AI Confidence: **99.31%**
1021. **`tensorflow/lite/core/c/common.cc`** -> AI Confidence: **99.31%**
1022. **`tensorflow/lite/core/interpreter.cc`** -> AI Confidence: **99.31%**
1023. **`tensorflow/lite/core/interpreter_builder.cc`** -> AI Confidence: **99.31%**
1024. **`tensorflow/lite/core/subgraph.cc`** -> AI Confidence: **99.31%**
1025. **`tensorflow/lite/core/tools/verifier.cc`** -> AI Confidence: **99.31%**
1026. **`tensorflow/lite/delegates/coreml/builders/activation_layer_builder.cc`** -> AI Confidence: **99.31%**
1027. **`tensorflow/lite/delegates/coreml/builders/add_op_builder.cc`** -> AI Confidence: **99.31%**
1028. **`tensorflow/lite/delegates/coreml/builders/convolution_op_builder.cc`** -> AI Confidence: **99.31%**
1029. **`tensorflow/lite/delegates/coreml/builders/fully_connected_op_builder.cc`** -> AI Confidence: **99.31%**
1030. **`tensorflow/lite/delegates/coreml/builders/mul_op_builder.cc`** -> AI Confidence: **99.31%**
1031. **`tensorflow/lite/delegates/coreml/builders/pad_op_builder.cc`** -> AI Confidence: **99.31%**
1032. **`tensorflow/lite/delegates/coreml/builders/pooling_layer_builder.cc`** -> AI Confidence: **99.31%**
1033. **`tensorflow/lite/delegates/coreml/builders/reshape_op_builder.cc`** -> AI Confidence: **99.31%**
1034. **`tensorflow/lite/delegates/coreml/builders/util.cc`** -> AI Confidence: **99.31%**
1035. **`tensorflow/lite/delegates/delegate_test_util.cc`** -> AI Confidence: **99.31%**
1036. **`tensorflow/lite/delegates/flex/buffer_map_util.cc`** -> AI Confidence: **99.31%**
1037. **`tensorflow/lite/delegates/flex/delegate_data.cc`** -> AI Confidence: **99.31%**
1038. **`tensorflow/lite/delegates/flex/kernel.cc`** -> AI Confidence: **99.31%**
1039. **`tensorflow/lite/delegates/flex/util.cc`** -> AI Confidence: **99.31%**
1040. **`tensorflow/lite/delegates/gpu/cl/api.cc`** -> AI Confidence: **99.31%**
1041. **`tensorflow/lite/delegates/gpu/cl/cl_arguments.cc`** -> AI Confidence: **99.31%**
1042. **`tensorflow/lite/delegates/gpu/cl/cl_command_buffer.cc`** -> AI Confidence: **99.31%**
1043. **`tensorflow/lite/delegates/gpu/cl/cl_command_queue.cc`** -> AI Confidence: **99.31%**
1044. **`tensorflow/lite/delegates/gpu/cl/cl_device.cc`** -> AI Confidence: **99.31%**
1045. **`tensorflow/lite/delegates/gpu/cl/cl_program.cc`** -> AI Confidence: **99.31%**
1046. **`tensorflow/lite/delegates/gpu/cl/environment.cc`** -> AI Confidence: **99.31%**
1047. **`tensorflow/lite/delegates/gpu/cl/inference_context.cc`** -> AI Confidence: **99.31%**
1048. **`tensorflow/lite/delegates/gpu/cl/kernels/converter.cc`** -> AI Confidence: **99.31%**
1049. **`tensorflow/lite/delegates/gpu/cl/tensor.cc`** -> AI Confidence: **99.31%**
1050. **`tensorflow/lite/delegates/gpu/cl/testing/delegate_testing.cc`** -> AI Confidence: **99.31%**
1051. **`tensorflow/lite/delegates/gpu/cl/testing/internal_api_samples.cc`** -> AI Confidence: **99.31%**
1052. **`tensorflow/lite/delegates/gpu/cl/testing/memory_sharing_sample.cc`** -> AI Confidence: **99.31%**
1053. **`tensorflow/lite/delegates/gpu/cl/testing/performance_profiling.cc`** -> AI Confidence: **99.31%**
1054. **`tensorflow/lite/delegates/gpu/common/convert.cc`** -> AI Confidence: **99.31%**
1055. **`tensorflow/lite/delegates/gpu/common/gpu_info.cc`** -> AI Confidence: **99.31%**
1056. **`tensorflow/lite/delegates/gpu/common/gpu_model.cc`** -> AI Confidence: **99.31%**
1057. **`tensorflow/lite/delegates/gpu/common/memory_management/greedy_by_breadth_assignment.cc`** -> AI Confidence: **99.31%**
1058. **`tensorflow/lite/delegates/gpu/common/memory_management/greedy_in_order_assignment.h`** -> AI Confidence: **99.31%**
1059. **`tensorflow/lite/delegates/gpu/common/memory_management/min_cost_flow_assignment.cc`** -> AI Confidence: **99.31%**
1060. **`tensorflow/lite/delegates/gpu/common/model_builder.cc`** -> AI Confidence: **99.31%**
1061. **`tensorflow/lite/delegates/gpu/common/model_builder_helper.cc`** -> AI Confidence: **99.31%**
1062. **`tensorflow/lite/delegates/gpu/common/object_reader.cc`** -> AI Confidence: **99.31%**
1063. **`tensorflow/lite/delegates/gpu/common/selectors/default/convolution_selector.cc`** -> AI Confidence: **99.31%**
1064. **`tensorflow/lite/delegates/gpu/common/selectors/default/convolution_transposed_selector.cc`** -> AI Confidence: **99.31%**
1065. **`tensorflow/lite/delegates/gpu/common/selectors/default/dw_convolution_selector.cc`** -> AI Confidence: **99.31%**
1066. **`tensorflow/lite/delegates/gpu/common/selectors/operation_selector.cc`** -> AI Confidence: **99.31%**
1067. **`tensorflow/lite/delegates/gpu/common/selectors/special_selector.cc`** -> AI Confidence: **99.31%**
1068. **`tensorflow/lite/delegates/gpu/common/task/arguments.cc`** -> AI Confidence: **99.31%**
1069. **`tensorflow/lite/delegates/gpu/common/task/buffer_desc.cc`** -> AI Confidence: **99.31%**
1070. **`tensorflow/lite/delegates/gpu/common/task/gpu_operation.cc`** -> AI Confidence: **99.31%**
1071. **`tensorflow/lite/delegates/gpu/common/task/tensor_desc.cc`** -> AI Confidence: **99.31%**
1072. **`tensorflow/lite/delegates/gpu/common/tasks/fully_connected_test_util.cc`** -> AI Confidence: **99.31%**
1073. **`tensorflow/lite/delegates/gpu/common/tasks/gather_test_util.cc`** -> AI Confidence: **99.31%**
1074. **`tensorflow/lite/delegates/gpu/common/tasks/mean_stddev_normalization.cc`** -> AI Confidence: **99.31%**
1075. **`tensorflow/lite/delegates/gpu/common/tasks/prelu.cc`** -> AI Confidence: **99.31%**
1076. **`tensorflow/lite/delegates/gpu/common/tasks/resampler_test_util.cc`** -> AI Confidence: **99.31%**
1077. **`tensorflow/lite/delegates/gpu/common/tasks/special/dw7x7_conv2to6_concat_conv8to8.cc`** -> AI Confidence: **99.31%**
1078. **`tensorflow/lite/delegates/gpu/common/tasks/special/fc_fc_add.cc`** -> AI Confidence: **99.31%**
1079. **`tensorflow/lite/delegates/gpu/common/tasks/special/thin_pointwise_fuser.cc`** -> AI Confidence: **99.31%**
1080. **`tensorflow/lite/delegates/gpu/common/testing/feature_parity/utils.cc`** -> AI Confidence: **99.31%**
1081. **`tensorflow/lite/delegates/gpu/common/testing/interpreter_utils.cc`** -> AI Confidence: **99.31%**
1082. **`tensorflow/lite/delegates/gpu/common/transformations/fuse_add_to_conv.cc`** -> AI Confidence: **99.31%**
1083. **`tensorflow/lite/delegates/gpu/common/transformations/fuse_mul_to_conv.cc`** -> AI Confidence: **99.31%**
1084. **`tensorflow/lite/delegates/gpu/common/transformations/make_padding.cc`** -> AI Confidence: **99.31%**
1085. **`tensorflow/lite/delegates/gpu/common/transformations/merge_densify.cc`** -> AI Confidence: **99.31%**
1086. **`tensorflow/lite/delegates/gpu/common/winograd_util.cc`** -> AI Confidence: **99.31%**
1087. **`tensorflow/lite/delegates/gpu/gl/compiler.cc`** -> AI Confidence: **99.31%**
1088. **`tensorflow/lite/delegates/gpu/gl/compiler/fuse_auto_input.cc`** -> AI Confidence: **99.31%**
1089. **`tensorflow/lite/delegates/gpu/gl/compiler/fuse_inline.cc`** -> AI Confidence: **99.31%**
1090. **`tensorflow/lite/delegates/gpu/gl/converters/bhwc_to_phwc4.cc`** -> AI Confidence: **99.31%**
1091. **`tensorflow/lite/delegates/gpu/gl/gl_errors.cc`** -> AI Confidence: **99.31%**
1092. **`tensorflow/lite/delegates/gpu/gl/kernels/add.cc`** -> AI Confidence: **99.31%**
1093. **`tensorflow/lite/delegates/gpu/gl/kernels/concat.cc`** -> AI Confidence: **99.31%**
1094. **`tensorflow/lite/delegates/gpu/gl/kernels/depthwise_conv.cc`** -> AI Confidence: **99.31%**
1095. **`tensorflow/lite/delegates/gpu/gl/kernels/mul.cc`** -> AI Confidence: **99.31%**
1096. **`tensorflow/lite/delegates/gpu/gl/kernels/pooling.cc`** -> AI Confidence: **99.31%**
1097. **`tensorflow/lite/delegates/gpu/gl/kernels/resampler.cc`** -> AI Confidence: **99.31%**
1098. **`tensorflow/lite/delegates/gpu/gl/kernels/resize.cc`** -> AI Confidence: **99.31%**
1099. **`tensorflow/lite/delegates/gpu/gl/kernels/slice.cc`** -> AI Confidence: **99.31%**
1100. **`tensorflow/lite/delegates/gpu/gl/kernels/softmax.cc`** -> AI Confidence: **99.31%**
1101. **`tensorflow/lite/delegates/gpu/gl/object_manager.cc`** -> AI Confidence: **99.31%**
1102. **`tensorflow/lite/delegates/gpu/gl/request_gpu_info.cc`** -> AI Confidence: **99.31%**
1103. **`tensorflow/lite/delegates/gpu/gl/runtime.cc`** -> AI Confidence: **99.31%**
1104. **`tensorflow/lite/delegates/gpu/metal/compute_task.cc`** -> AI Confidence: **99.31%**
1105. **`tensorflow/lite/delegates/gpu/metal/inference_context.cc`** -> AI Confidence: **99.31%**
1106. **`tensorflow/lite/delegates/gpu/metal/kernels/test_util.cc`** -> AI Confidence: **99.31%**
1107. **`tensorflow/lite/delegates/gpu/metal/metal_arguments.cc`** -> AI Confidence: **99.31%**
1108. **`tensorflow/lite/delegates/hexagon/builders/conv_2d_builder.cc`** -> AI Confidence: **99.31%**
1109. **`tensorflow/lite/delegates/hexagon/builders/conv_2d_helpers.cc`** -> AI Confidence: **99.31%**
1110. **`tensorflow/lite/delegates/hexagon/hexagon_delegate_kernel.cc`** -> AI Confidence: **99.31%**
1111. **`tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`** -> AI Confidence: **99.31%**
1112. **`tensorflow/lite/delegates/utils/experimental/sample_stable_delegate/sample_stable_delegate.cc`** -> AI Confidence: **99.31%**
1113. **`tensorflow/lite/delegates/utils/experimental/sample_stable_delegate/sample_stable_delegate_test.cc`** -> AI Confidence: **99.31%**
1114. **`tensorflow/lite/delegates/utils/experimental/sample_stable_delegate/sample_stable_delegate_with_control_flow.cc`** -> AI Confidence: **99.31%**
1115. **`tensorflow/lite/delegates/utils/sync_fence.cc`** -> AI Confidence: **99.31%**
1116. **`tensorflow/lite/delegates/xnnpack/batch_matrix_multiply_tester.cc`** -> AI Confidence: **99.31%**
1117. **`tensorflow/lite/delegates/xnnpack/concatenation_tester.cc`** -> AI Confidence: **99.31%**
1118. **`tensorflow/lite/delegates/xnnpack/depth_to_space_tester.cc`** -> AI Confidence: **99.31%**
1119. **`tensorflow/lite/delegates/xnnpack/dynamically_quantized_fully_connected_tester.cc`** -> AI Confidence: **99.31%**
1120. **`tensorflow/lite/delegates/xnnpack/mmap_handle.cc`** -> AI Confidence: **99.31%**
1121. **`tensorflow/lite/delegates/xnnpack/pool_2d_tester.cc`** -> AI Confidence: **99.31%**
1122. **`tensorflow/lite/delegates/xnnpack/quantize_tester.cc`** -> AI Confidence: **99.31%**
1123. **`tensorflow/lite/delegates/xnnpack/quantized_binary_elementwise_tester.cc`** -> AI Confidence: **99.31%**
1124. **`tensorflow/lite/delegates/xnnpack/quantized_conv_2d_tester.cc`** -> AI Confidence: **99.31%**
1125. **`tensorflow/lite/delegates/xnnpack/quantized_depthwise_conv_2d_tester.cc`** -> AI Confidence: **99.31%**
1126. **`tensorflow/lite/delegates/xnnpack/quantized_pool_2d_tester.cc`** -> AI Confidence: **99.31%**
1127. **`tensorflow/lite/delegates/xnnpack/quantized_resize_bilinear_tester.cc`** -> AI Confidence: **99.31%**
1128. **`tensorflow/lite/delegates/xnnpack/quantized_variable_ops_tester.cc`** -> AI Confidence: **99.31%**
1129. **`tensorflow/lite/delegates/xnnpack/reshape_tester.cc`** -> AI Confidence: **99.31%**
1130. **`tensorflow/lite/delegates/xnnpack/space_to_depth_tester.cc`** -> AI Confidence: **99.31%**
1131. **`tensorflow/lite/delegates/xnnpack/split_tester.cc`** -> AI Confidence: **99.31%**
1132. **`tensorflow/lite/delegates/xnnpack/strided_slice_tester.cc`** -> AI Confidence: **99.31%**
1133. **`tensorflow/lite/delegates/xnnpack/transpose_tester.cc`** -> AI Confidence: **99.31%**
1134. **`tensorflow/lite/examples/minimal/minimal.cc`** -> AI Confidence: **99.31%**
1135. **`tensorflow/lite/experimental/acceleration/compatibility/json_to_fb.cc`** -> AI Confidence: **99.31%**
1136. **`tensorflow/lite/experimental/acceleration/mini_benchmark/blocking_validator_runner.cc`** -> AI Confidence: **99.31%**
1137. **`tensorflow/lite/experimental/acceleration/mini_benchmark/fb_storage.cc`** -> AI Confidence: **99.31%**
1138. **`tensorflow/lite/experimental/acceleration/mini_benchmark/mini_benchmark_implementation.cc`** -> AI Confidence: **99.31%**
1139. **`tensorflow/lite/experimental/acceleration/mini_benchmark/model_modifier/custom_validation_embedder.cc`** -> AI Confidence: **99.31%**
1140. **`tensorflow/lite/experimental/acceleration/mini_benchmark/model_modifier/embedder.cc`** -> AI Confidence: **99.31%**
1141. **`tensorflow/lite/experimental/acceleration/mini_benchmark/model_modifier/embedder_main.cc`** -> AI Confidence: **99.31%**
1142. **`tensorflow/lite/experimental/acceleration/mini_benchmark/model_modifier/validation_graph_builder.cc`** -> AI Confidence: **99.31%**
1143. **`tensorflow/lite/experimental/acceleration/mini_benchmark/runner.cc`** -> AI Confidence: **99.31%**
1144. **`tensorflow/lite/experimental/acceleration/mini_benchmark/validator.cc`** -> AI Confidence: **99.31%**
1145. **`tensorflow/lite/experimental/acceleration/mini_benchmark/validator_runner_entrypoint.cc`** -> AI Confidence: **99.31%**
1146. **`tensorflow/lite/experimental/acceleration/mini_benchmark/validator_runner_impl.cc`** -> AI Confidence: **99.31%**
1147. **`tensorflow/lite/experimental/microfrontend/ops/audio_microfrontend_op.cc`** -> AI Confidence: **99.31%**
1148. **`tensorflow/lite/experimental/resource/resource_variable.cc`** -> AI Confidence: **99.31%**
1149. **`tensorflow/lite/experimental/shlo/legacy/src/debug.cc`** -> AI Confidence: **99.31%**
1150. **`tensorflow/lite/kernels/acceleration_test_util_internal.cc`** -> AI Confidence: **99.31%**
1151. **`tensorflow/lite/kernels/activations.cc`** -> AI Confidence: **99.31%**
1152. **`tensorflow/lite/kernels/batch_matmul.cc`** -> AI Confidence: **99.31%**
1153. **`tensorflow/lite/kernels/concatenation.cc`** -> AI Confidence: **99.31%**
1154. **`tensorflow/lite/kernels/conv3d.cc`** -> AI Confidence: **99.31%**
1155. **`tensorflow/lite/kernels/cpu_backend_context.cc`** -> AI Confidence: **99.31%**
1156. **`tensorflow/lite/kernels/depth_to_space.cc`** -> AI Confidence: **99.31%**
1157. **`tensorflow/lite/kernels/detection_postprocess.cc`** -> AI Confidence: **99.31%**
1158. **`tensorflow/lite/kernels/div.cc`** -> AI Confidence: **99.31%**
1159. **`tensorflow/lite/kernels/dynamic_update_slice.cc`** -> AI Confidence: **99.31%**
1160. **`tensorflow/lite/kernels/embedding_lookup.cc`** -> AI Confidence: **99.31%**
1161. **`tensorflow/lite/kernels/expand_dims.cc`** -> AI Confidence: **99.31%**
1162. **`tensorflow/lite/kernels/fill.cc`** -> AI Confidence: **99.31%**
1163. **`tensorflow/lite/kernels/floor_mod.cc`** -> AI Confidence: **99.31%**
1164. **`tensorflow/lite/kernels/fully_connected.cc`** -> AI Confidence: **99.31%**
1165. **`tensorflow/lite/kernels/gather.cc`** -> AI Confidence: **99.31%**
1166. **`tensorflow/lite/kernels/gather_nd.cc`** -> AI Confidence: **99.31%**
1167. **`tensorflow/lite/kernels/hadamard_rotation.cc`** -> AI Confidence: **99.31%**
1168. **`tensorflow/lite/kernels/hashtable_lookup.cc`** -> AI Confidence: **99.31%**
1169. **`tensorflow/lite/kernels/if.cc`** -> AI Confidence: **99.31%**
1170. **`tensorflow/lite/kernels/internal/optimized/4bit/fully_connected_reference.cc`** -> AI Confidence: **99.31%**
1171. **`tensorflow/lite/kernels/internal/optimized/4bit/neon_fully_connected.cc`** -> AI Confidence: **99.31%**
1172. **`tensorflow/lite/kernels/internal/optimized/4bit/sse_fully_connected.cc`** -> AI Confidence: **99.31%**
1173. **`tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h`** -> AI Confidence: **99.31%**
1174. **`tensorflow/lite/kernels/internal/optimized/integer_ops/conv.h`** -> AI Confidence: **99.31%**
1175. **`tensorflow/lite/kernels/internal/optimized/integer_ops/depthwise_conv_hybrid.h`** -> AI Confidence: **99.31%**
1176. **`tensorflow/lite/kernels/internal/optimized/integer_ops/sub.h`** -> AI Confidence: **99.31%**
1177. **`tensorflow/lite/kernels/internal/optimized/neon_tensor_utils.cc`** -> AI Confidence: **99.31%**
1178. **`tensorflow/lite/kernels/internal/optimized/reduce.h`** -> AI Confidence: **99.31%**
1179. **`tensorflow/lite/kernels/internal/optimized/sse_tensor_utils.cc`** -> AI Confidence: **99.31%**
1180. **`tensorflow/lite/kernels/internal/reference/portable_tensor_utils.cc`** -> AI Confidence: **99.31%**
1181. **`tensorflow/lite/kernels/internal/reference/svdf.h`** -> AI Confidence: **99.31%**
1182. **`tensorflow/lite/kernels/internal/utils/sparsity_format_converter.cc`** -> AI Confidence: **99.31%**
1183. **`tensorflow/lite/kernels/irfft2d.cc`** -> AI Confidence: **99.31%**
1184. **`tensorflow/lite/kernels/kernel_util.cc`** -> AI Confidence: **99.31%**
1185. **`tensorflow/lite/kernels/l2norm.cc`** -> AI Confidence: **99.31%**
1186. **`tensorflow/lite/kernels/lsh_projection.cc`** -> AI Confidence: **99.31%**
1187. **`tensorflow/lite/kernels/lstm.cc`** -> AI Confidence: **99.31%**
1188. **`tensorflow/lite/kernels/mirror_pad.cc`** -> AI Confidence: **99.31%**
1189. **`tensorflow/lite/kernels/neg.cc`** -> AI Confidence: **99.31%**
1190. **`tensorflow/lite/kernels/pack.cc`** -> AI Confidence: **99.31%**
1191. **`tensorflow/lite/kernels/parse_example/parse_example.cc`** -> AI Confidence: **99.31%**
1192. **`tensorflow/lite/kernels/pooling3d.cc`** -> AI Confidence: **99.31%**
1193. **`tensorflow/lite/kernels/quantize.cc`** -> AI Confidence: **99.31%**
1194. **`tensorflow/lite/kernels/random_ops.cc`** -> AI Confidence: **99.31%**
1195. **`tensorflow/lite/kernels/random_uniform_custom.cc`** -> AI Confidence: **99.31%**
1196. **`tensorflow/lite/kernels/range.cc`** -> AI Confidence: **99.31%**
1197. **`tensorflow/lite/kernels/reduce.cc`** -> AI Confidence: **99.31%**
1198. **`tensorflow/lite/kernels/resize_bilinear.cc`** -> AI Confidence: **99.31%**
1199. **`tensorflow/lite/kernels/rfft2d.cc`** -> AI Confidence: **99.31%**
1200. **`tensorflow/lite/kernels/rng_bit_generator.cc`** -> AI Confidence: **99.31%**
1201. **`tensorflow/lite/kernels/roll.cc`** -> AI Confidence: **99.31%**
1202. **`tensorflow/lite/kernels/round.cc`** -> AI Confidence: **99.31%**
1203. **`tensorflow/lite/kernels/scatter_nd.cc`** -> AI Confidence: **99.31%**
1204. **`tensorflow/lite/kernels/select.cc`** -> AI Confidence: **99.31%**
1205. **`tensorflow/lite/kernels/shape.cc`** -> AI Confidence: **99.31%**
1206. **`tensorflow/lite/kernels/shim/test_util.cc`** -> AI Confidence: **99.31%**
1207. **`tensorflow/lite/kernels/skip_gram.cc`** -> AI Confidence: **99.31%**
1208. **`tensorflow/lite/kernels/slice.cc`** -> AI Confidence: **99.31%**
1209. **`tensorflow/lite/kernels/space_to_depth.cc`** -> AI Confidence: **99.31%**
1210. **`tensorflow/lite/kernels/sparse_to_dense.cc`** -> AI Confidence: **99.31%**
1211. **`tensorflow/lite/kernels/split.cc`** -> AI Confidence: **99.31%**
1212. **`tensorflow/lite/kernels/split_v.cc`** -> AI Confidence: **99.31%**
1213. **`tensorflow/lite/kernels/squeeze.cc`** -> AI Confidence: **99.31%**
1214. **`tensorflow/lite/kernels/stablehlo_composite.cc`** -> AI Confidence: **99.31%**
1215. **`tensorflow/lite/kernels/stablehlo_reduce_window_test_util.h`** -> AI Confidence: **99.31%**
1216. **`tensorflow/lite/kernels/sub.cc`** -> AI Confidence: **99.31%**
1217. **`tensorflow/lite/kernels/tile.cc`** -> AI Confidence: **99.31%**
1218. **`tensorflow/lite/kernels/topk_v2.cc`** -> AI Confidence: **99.31%**
1219. **`tensorflow/lite/kernels/transpose.cc`** -> AI Confidence: **99.31%**
1220. **`tensorflow/lite/kernels/unidirectional_sequence_rnn.cc`** -> AI Confidence: **99.31%**
1221. **`tensorflow/lite/kernels/unpack.cc`** -> AI Confidence: **99.31%**
1222. **`tensorflow/lite/kernels/variants/list_kernels/list_from_tensor.cc`** -> AI Confidence: **99.31%**
1223. **`tensorflow/lite/kernels/variants/list_kernels/list_stack.cc`** -> AI Confidence: **99.31%**
1224. **`tensorflow/lite/kernels/variants/list_kernels/test_util.cc`** -> AI Confidence: **99.31%**
1225. **`tensorflow/lite/kernels/variants/list_kernels/variant_add_n.cc`** -> AI Confidence: **99.31%**
1226. **`tensorflow/lite/kernels/where.cc`** -> AI Confidence: **99.31%**
1227. **`tensorflow/lite/kernels/while.cc`** -> AI Confidence: **99.31%**
1228. **`tensorflow/lite/nnapi/nnapi_implementation.cc`** -> AI Confidence: **99.31%**
1229. **`tensorflow/lite/optional_debug_tools.cc`** -> AI Confidence: **99.31%**
1230. **`tensorflow/lite/profiling/memory_info.cc`** -> AI Confidence: **99.31%**
1231. **`tensorflow/lite/profiling/memory_latency_logger.cc`** -> AI Confidence: **99.31%**
1232. **`tensorflow/lite/profiling/memory_usage_monitor.cc`** -> AI Confidence: **99.31%**
1233. **`tensorflow/lite/profiling/model_runtime_info.cc`** -> AI Confidence: **99.31%**
1234. **`tensorflow/lite/profiling/profile_buffer.cc`** -> AI Confidence: **99.31%**
1235. **`tensorflow/lite/profiling/profile_summary_formatter.cc`** -> AI Confidence: **99.31%**
1236. **`tensorflow/lite/python/analyzer_wrapper/model_analyzer.cc`** -> AI Confidence: **99.31%**
1237. **`tensorflow/lite/python/interpreter_wrapper/interpreter_wrapper.cc`** -> AI Confidence: **99.31%**
1238. **`tensorflow/lite/simple_memory_arena.cc`** -> AI Confidence: **99.31%**
1239. **`tensorflow/lite/simple_memory_arena_debug_dump.cc`** -> AI Confidence: **99.31%**
1240. **`tensorflow/lite/simple_planner.cc`** -> AI Confidence: **99.31%**
1241. **`tensorflow/lite/testing/nnapi_example.cc`** -> AI Confidence: **99.31%**
1242. **`tensorflow/lite/testing/parse_testdata.cc`** -> AI Confidence: **99.31%**
1243. **`tensorflow/lite/testing/result_expectations.cc`** -> AI Confidence: **99.31%**
1244. **`tensorflow/lite/testing/tf_driver.cc`** -> AI Confidence: **99.31%**
1245. **`tensorflow/lite/testing/tflite_diff_util.cc`** -> AI Confidence: **99.31%**
1246. **`tensorflow/lite/toco/dump_graphviz.cc`** -> AI Confidence: **99.31%**
1247. **`tensorflow/lite/toco/export_tensorflow.cc`** -> AI Confidence: **99.31%**
1248. **`tensorflow/lite/toco/graph_transformations/convert_expanddims_to_reshape.cc`** -> AI Confidence: **99.31%**
1249. **`tensorflow/lite/toco/graph_transformations/convert_trivial_tile_to_concat.cc`** -> AI Confidence: **99.31%**
1250. **`tensorflow/lite/toco/graph_transformations/create_im2col_arrays.cc`** -> AI Confidence: **99.31%**
1251. **`tensorflow/lite/toco/graph_transformations/dequantize.cc`** -> AI Confidence: **99.31%**
1252. **`tensorflow/lite/toco/graph_transformations/ensure_bias_vectors.cc`** -> AI Confidence: **99.31%**
1253. **`tensorflow/lite/toco/graph_transformations/fuse_activation_functions.cc`** -> AI Confidence: **99.31%**
1254. **`tensorflow/lite/toco/graph_transformations/fuse_binary_into_following_affine.cc`** -> AI Confidence: **99.31%**
1255. **`tensorflow/lite/toco/graph_transformations/fuse_binary_into_preceding_affine.cc`** -> AI Confidence: **99.31%**
1256. **`tensorflow/lite/toco/graph_transformations/fuse_broadcast_into_following_binary.cc`** -> AI Confidence: **99.31%**
1257. **`tensorflow/lite/toco/graph_transformations/graph_transformations.cc`** -> AI Confidence: **99.31%**
1258. **`tensorflow/lite/toco/graph_transformations/group_bidirectional_sequence_ops.cc`** -> AI Confidence: **99.31%**
1259. **`tensorflow/lite/toco/graph_transformations/hardcode_min_max.cc`** -> AI Confidence: **99.31%**
1260. **`tensorflow/lite/toco/graph_transformations/identify_dilated_conv.cc`** -> AI Confidence: **99.31%**
1261. **`tensorflow/lite/toco/graph_transformations/identify_l2_normalization.cc`** -> AI Confidence: **99.31%**
1262. **`tensorflow/lite/toco/graph_transformations/identify_nearest_upsample.cc`** -> AI Confidence: **99.31%**
1263. **`tensorflow/lite/toco/graph_transformations/identify_prelu.cc`** -> AI Confidence: **99.31%**
1264. **`tensorflow/lite/toco/graph_transformations/identify_relu1.cc`** -> AI Confidence: **99.31%**
1265. **`tensorflow/lite/toco/graph_transformations/merge_reshape_into_preceding_transpose.cc`** -> AI Confidence: **99.31%**
1266. **`tensorflow/lite/toco/graph_transformations/propagate_activation_function_into_constants.cc`** -> AI Confidence: **99.31%**
1267. **`tensorflow/lite/toco/graph_transformations/propagate_default_min_max.cc`** -> AI Confidence: **99.31%**
1268. **`tensorflow/lite/toco/graph_transformations/propagate_fake_quant_num_bits.cc`** -> AI Confidence: **99.31%**
1269. **`tensorflow/lite/toco/graph_transformations/propagate_fixed_sizes.cc`** -> AI Confidence: **99.31%**
1270. **`tensorflow/lite/toco/graph_transformations/quantization_util.cc`** -> AI Confidence: **99.31%**
1271. **`tensorflow/lite/toco/graph_transformations/quantize.cc`** -> AI Confidence: **99.31%**
1272. **`tensorflow/lite/toco/graph_transformations/remove_successive_transpose.cc`** -> AI Confidence: **99.31%**
1273. **`tensorflow/lite/toco/graph_transformations/remove_trivial_concatenation_input.cc`** -> AI Confidence: **99.31%**
1274. **`tensorflow/lite/toco/graph_transformations/remove_trivial_passthrough.cc`** -> AI Confidence: **99.31%**
1275. **`tensorflow/lite/toco/graph_transformations/remove_trivial_quantized_activation_func.cc`** -> AI Confidence: **99.31%**
1276. **`tensorflow/lite/toco/graph_transformations/remove_unused_op.cc`** -> AI Confidence: **99.31%**
1277. **`tensorflow/lite/toco/graph_transformations/reorder_elementwise_unary.cc`** -> AI Confidence: **99.31%**
1278. **`tensorflow/lite/toco/graph_transformations/reorder_reshape_transpose.cc`** -> AI Confidence: **99.31%**
1279. **`tensorflow/lite/toco/graph_transformations/resolve_constant_binary.cc`** -> AI Confidence: **99.31%**
1280. **`tensorflow/lite/toco/graph_transformations/resolve_constant_concatenation.cc`** -> AI Confidence: **99.31%**
1281. **`tensorflow/lite/toco/graph_transformations/resolve_constant_fill.cc`** -> AI Confidence: **99.31%**
1282. **`tensorflow/lite/toco/graph_transformations/resolve_constant_gather.cc`** -> AI Confidence: **99.31%**
1283. **`tensorflow/lite/toco/graph_transformations/resolve_constant_pack.cc`** -> AI Confidence: **99.31%**
1284. **`tensorflow/lite/toco/graph_transformations/resolve_constant_slice.cc`** -> AI Confidence: **99.31%**
1285. **`tensorflow/lite/toco/graph_transformations/resolve_constant_strided_slice.cc`** -> AI Confidence: **99.31%**
1286. **`tensorflow/lite/toco/graph_transformations/resolve_constant_tile.cc`** -> AI Confidence: **99.31%**
1287. **`tensorflow/lite/toco/graph_transformations/resolve_constant_transpose.cc`** -> AI Confidence: **99.31%**
1288. **`tensorflow/lite/toco/graph_transformations/resolve_constant_unary.cc`** -> AI Confidence: **99.31%**
1289. **`tensorflow/lite/toco/graph_transformations/resolve_tensorflow_matmul.cc`** -> AI Confidence: **99.31%**
1290. **`tensorflow/lite/toco/graph_transformations/shuffle_fc_weights.cc`** -> AI Confidence: **99.31%**
1291. **`tensorflow/lite/toco/graph_transformations/unfuse_activation_functions.cc`** -> AI Confidence: **99.31%**
1292. **`tensorflow/lite/toco/python/toco_python_api.cc`** -> AI Confidence: **99.31%**
1293. **`tensorflow/lite/toco/tensorflow_graph_matching/resolve_cluster.cc`** -> AI Confidence: **99.31%**
1294. **`tensorflow/lite/toco/tensorflow_graph_matching/resolve_svdf.cc`** -> AI Confidence: **99.31%**
1295. **`tensorflow/lite/toco/tflite/import.cc`** -> AI Confidence: **99.31%**
1296. **`tensorflow/lite/toco/toco_tooling.cc`** -> AI Confidence: **99.31%**
1297. **`tensorflow/lite/toco/tooling_util.cc`** -> AI Confidence: **99.31%**
1298. **`tensorflow/lite/tools/benchmark/benchmark_model.cc`** -> AI Confidence: **99.31%**
1299. **`tensorflow/lite/tools/benchmark/benchmark_performance_options.cc`** -> AI Confidence: **99.31%**
1300. **`tensorflow/lite/tools/benchmark/benchmark_tflite_model.cc`** -> AI Confidence: **99.31%**
1301. **`tensorflow/lite/tools/benchmark/experimental/delegate_performance/android/src/main/native/latency_benchmark.cc`** -> AI Confidence: **99.31%**
1302. **`tensorflow/lite/tools/command_line_flags.cc`** -> AI Confidence: **99.31%**
1303. **`tensorflow/lite/tools/delegates/compatibility/gpu/gpu_delegate_compatibility_checker.cc`** -> AI Confidence: **99.31%**
1304. **`tensorflow/lite/tools/delegates/compatibility/nnapi/nnapi_compatibility_lib.cc`** -> AI Confidence: **99.31%**
1305. **`tensorflow/lite/tools/evaluation/evaluation_delegate_provider.cc`** -> AI Confidence: **99.31%**
1306. **`tensorflow/lite/tools/evaluation/stages/image_classification_stage.cc`** -> AI Confidence: **99.31%**
1307. **`tensorflow/lite/tools/evaluation/stages/image_preprocessing_stage.cc`** -> AI Confidence: **99.31%**
1308. **`tensorflow/lite/tools/evaluation/stages/inference_profiler_stage.cc`** -> AI Confidence: **99.31%**
1309. **`tensorflow/lite/tools/evaluation/stages/object_detection_average_precision_stage.cc`** -> AI Confidence: **99.31%**
1310. **`tensorflow/lite/tools/evaluation/stages/tflite_inference_stage.cc`** -> AI Confidence: **99.31%**
1311. **`tensorflow/lite/tools/evaluation/stages/topk_accuracy_eval_stage.cc`** -> AI Confidence: **99.31%**
1312. **`tensorflow/lite/tools/evaluation/stages/utils/image_metrics.cc`** -> AI Confidence: **99.31%**
1313. **`tensorflow/lite/tools/evaluation/utils.cc`** -> AI Confidence: **99.31%**
1314. **`tensorflow/lite/tools/gen_op_registration_main.cc`** -> AI Confidence: **99.31%**
1315. **`tensorflow/lite/tools/list_flex_ops.cc`** -> AI Confidence: **99.31%**
1316. **`tensorflow/lite/tools/list_flex_ops_main.cc`** -> AI Confidence: **99.31%**
1317. **`tensorflow/lite/tools/model_loader.cc`** -> AI Confidence: **99.31%**
1318. **`tensorflow/lite/tools/optimize/calibration/calibration_logger.cc`** -> AI Confidence: **99.31%**
1319. **`tensorflow/lite/tools/optimize/calibration/calibration_reader.cc`** -> AI Confidence: **99.31%**
1320. **`tensorflow/lite/tools/optimize/calibration/logging_op_resolver.cc`** -> AI Confidence: **99.31%**
1321. **`tensorflow/lite/tools/optimize/quantization_utils.cc`** -> AI Confidence: **99.31%**
1322. **`tensorflow/lite/tools/optimize/quantization_wrapper_utils.cc`** -> AI Confidence: **99.31%**
1323. **`tensorflow/lite/tools/serialization/option_writer_generator.cc`** -> AI Confidence: **99.31%**
1324. **`tensorflow/lite/tools/strip_buffers/stripping_lib.cc`** -> AI Confidence: **99.31%**
1325. **`tensorflow/lite/tools/utils.cc`** -> AI Confidence: **99.31%**
1326. **`tensorflow/lite/tools/versioning/gpu_compatibility.cc`** -> AI Confidence: **99.31%**
1327. **`tensorflow/lite/tools/versioning/op_signature.cc`** -> AI Confidence: **99.31%**
1328. **`tensorflow/lite/util.cc`** -> AI Confidence: **99.31%**
1329. **`tensorflow/python/client/device_lib_wrapper.cc`** -> AI Confidence: **99.31%**
1330. **`tensorflow/python/client/session_ref.cc`** -> AI Confidence: **99.31%**
1331. **`tensorflow/python/client/tf_session_helper.cc`** -> AI Confidence: **99.31%**
1332. **`tensorflow/python/eager/pywrap_tensor.cc`** -> AI Confidence: **99.31%**
1333. **`tensorflow/python/eager/pywrap_tfe_src.cc`** -> AI Confidence: **99.31%**
1334. **`tensorflow/python/framework/offset_counter.cc`** -> AI Confidence: **99.31%**
1335. **`tensorflow/python/framework/op_def_library_pybind.cc`** -> AI Confidence: **99.31%**
1336. **`tensorflow/python/framework/op_def_util.cc`** -> AI Confidence: **99.31%**
1337. **`tensorflow/python/framework/python_api_dispatcher.cc`** -> AI Confidence: **99.31%**
1338. **`tensorflow/python/framework/python_api_info.cc`** -> AI Confidence: **99.31%**
1339. **`tensorflow/python/framework/python_api_parameter_converter.cc`** -> AI Confidence: **99.31%**
1340. **`tensorflow/python/framework/python_op_gen_main.cc`** -> AI Confidence: **99.31%**
1341. **`tensorflow/python/grappler/cluster_wrapper.cc`** -> AI Confidence: **99.31%**
1342. **`tensorflow/python/grappler/cost_analyzer.cc`** -> AI Confidence: **99.31%**
1343. **`tensorflow/python/grappler/item_wrapper.cc`** -> AI Confidence: **99.31%**
1344. **`tensorflow/python/grappler/model_analyzer.cc`** -> AI Confidence: **99.31%**
1345. **`tensorflow/python/grappler/tf_optimizer_wrapper.cc`** -> AI Confidence: **99.31%**
1346. **`tensorflow/python/profiler/internal/pywrap_profiler_plugin.cc`** -> AI Confidence: **99.31%**
1347. **`tensorflow/python/saved_model/pywrap_saved_model_fingerprinting.cc`** -> AI Confidence: **99.31%**
1348. **`tensorflow/python/saved_model/pywrap_saved_model_metrics.cc`** -> AI Confidence: **99.31%**
1349. **`tensorflow/python/tfe_wrapper.cc`** -> AI Confidence: **99.31%**
1350. **`tensorflow/python/util/function_parameter_canonicalizer.cc`** -> AI Confidence: **99.31%**
1351. **`tensorflow/python/util/transform_graph_wrapper.cc`** -> AI Confidence: **99.31%**
1352. **`tensorflow/python/util/util.cc`** -> AI Confidence: **99.31%**
1353. **`tensorflow/security/fuzzing/cc/arg_def_case_fuzz.cc`** -> AI Confidence: **99.31%**
1354. **`tensorflow/security/fuzzing/cc/checkpoint_reader_fuzz.cc`** -> AI Confidence: **99.31%**
1355. **`tensorflow/security/fuzzing/cc/consume_leading_digits_fuzz.cc`** -> AI Confidence: **99.31%**
1356. **`tensorflow/security/fuzzing/cc/parseURI_fuzz.cc`** -> AI Confidence: **99.31%**
1357. **`tensorflow/tools/android/test/jni/object_tracking/keypoint_detector.cc`** -> AI Confidence: **99.31%**
1358. **`tensorflow/tools/graph_transforms/fold_batch_norms.cc`** -> AI Confidence: **99.31%**
1359. **`tensorflow/tools/graph_transforms/fold_old_batch_norms.cc`** -> AI Confidence: **99.31%**
1360. **`tensorflow/tools/graph_transforms/inline_partitionedcall.cc`** -> AI Confidence: **99.31%**
1361. **`tensorflow/tools/graph_transforms/quantize_weights.cc`** -> AI Confidence: **99.31%**
1362. **`tensorflow/tools/graph_transforms/remove_attribute.cc`** -> AI Confidence: **99.31%**
1363. **`tensorflow/tools/graph_transforms/remove_nodes.cc`** -> AI Confidence: **99.31%**
1364. **`tensorflow/tools/graph_transforms/rename_op.cc`** -> AI Confidence: **99.31%**
1365. **`tensorflow/tools/graph_transforms/round_weights.cc`** -> AI Confidence: **99.31%**
1366. **`tensorflow/tools/graph_transforms/sparsify_gather.cc`** -> AI Confidence: **99.31%**
1367. **`tensorflow/tools/graph_transforms/sparsify_gather_test.cc`** -> AI Confidence: **99.31%**
1368. **`tensorflow/tools/graph_transforms/transform_graph.cc`** -> AI Confidence: **99.31%**
1369. **`tensorflow/tools/proto_splitter/cc/composable_splitter_base.cc`** -> AI Confidence: **99.31%**
1370. **`tensorflow/tools/proto_splitter/cc/graph_def_splitter_test.cc`** -> AI Confidence: **99.31%**
1371. **`tensorflow/tools/proto_splitter/cc/saved_model_splitter_test.cc`** -> AI Confidence: **99.31%**
1372. **`tensorflow/tools/proto_splitter/cc/util.cc`** -> AI Confidence: **99.31%**
1373. **`tensorflow/tools/proto_splitter/merge.cc`** -> AI Confidence: **99.31%**
1374. **`tensorflow/tools/proto_text/gen_proto_text_functions_lib.cc`** -> AI Confidence: **99.31%**
1375. **`tensorflow/tools/tfg_graph_transforms/tfg_graph_transforms_main.cc`** -> AI Confidence: **99.31%**
1376. **`tensorflow/go/genop/internal/genop.go`** -> AI Confidence: **99.31%**
1377. **`tensorflow/go/genop/main.go`** -> AI Confidence: **99.31%**
1378. **`tensorflow/go/tensor.go`** -> AI Confidence: **99.31%**
1379. **`tensorflow/java/src/test/java/org/tensorflow/GraphTest.java`** -> AI Confidence: **99.31%**
1380. **`tensorflow/java/src/test/java/org/tensorflow/TensorTest.java`** -> AI Confidence: **99.31%**
1381. **`tensorflow/lite/java/src/main/java/org/tensorflow/lite/NativeInterpreterWrapper.java`** -> AI Confidence: **99.31%**
1382. **`tensorflow/lite/java/src/main/java/org/tensorflow/lite/TensorImpl.java`** -> AI Confidence: **99.31%**
1383. **`tensorflow/lite/tools/benchmark/experimental/delegate_performance/android/src/main/java/org/tensorflow/lite/benchmark/delegateperformance/BenchmarkAccuracyImpl.java`** -> AI Confidence: **99.31%**
1384. **`tensorflow/lite/tools/benchmark/experimental/delegate_performance/android/src/main/java/org/tensorflow/lite/benchmark/delegateperformance/BenchmarkLatencyImpl.java`** -> AI Confidence: **99.31%**
1385. **`tensorflow/lite/tools/benchmark/experimental/firebase/android/src/org/tensorflow/lite/benchmark/firebase/BenchmarkModelActivity.java`** -> AI Confidence: **99.31%**
1386. **`tensorflow/tools/android/test/src/org/tensorflow/demo/tracking/MultiBoxTracker.java`** -> AI Confidence: **99.31%**
1387. **`tensorflow/lite/tools/pip_package/Dockerfile.py3`** -> AI Confidence: **99.29%**
1388. **`tensorflow/lite/tools/tflite-android.Dockerfile`** -> AI Confidence: **99.29%**
1389. **`tensorflow/tools/ci_build/Dockerfile.android`** -> AI Confidence: **99.29%**
1390. **`tensorflow/tools/ci_build/Dockerfile.cpu.arm64`** -> AI Confidence: **99.29%**
1391. **`tensorflow/tools/ci_build/Dockerfile.custom_op_ubuntu_16`** -> AI Confidence: **99.29%**
1392. **`tensorflow/tools/ci_build/Dockerfile.custom_op_ubuntu_16_cuda10.0`** -> AI Confidence: **99.29%**
1393. **`tensorflow/tools/ci_build/Dockerfile.custom_op_ubuntu_16_cuda10.1`** -> AI Confidence: **99.29%**
1394. **`tensorflow/tools/ci_build/Dockerfile.custom_op_ubuntu_16_cuda11.2`** -> AI Confidence: **99.29%**
1395. **`tensorflow/tools/ci_build/Dockerfile.debian.bullseye.cpu`** -> AI Confidence: **99.29%**
1396. **`tensorflow/tools/ci_build/Dockerfile.gpu`** -> AI Confidence: **99.29%**
1397. **`tensorflow/tools/ci_build/Dockerfile.local-toolchain-ubuntu18.04-manylinux2010`** -> AI Confidence: **99.29%**
1398. **`tensorflow/tools/ci_build/Dockerfile.local-toolchain-ubuntu20.04-manylinux2014`** -> AI Confidence: **99.29%**
1399. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda11.8-cudnn8.6-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1400. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.1-cudnn8.9-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1401. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.1-cudnn9.1-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1402. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.2-cudnn8.9-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1403. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.2-cudnn9.1-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1404. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.3-cudnn8.9-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1405. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.3-cudnn8.9-ubuntu22.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1406. **`tensorflow/tools/ci_build/Dockerfile.rbe.cuda12.3-cudnn9.1-ubuntu20.04-manylinux2014-multipython`** -> AI Confidence: **99.29%**
1407. **`tensorflow/tools/ci_build/Dockerfile.rbe.ubuntu16.04-manylinux2010`** -> AI Confidence: **99.29%**
1408. **`tensorflow/tools/ci_build/Dockerfile.rocm`** -> AI Confidence: **99.29%**
1409. **`tensorflow/tools/ci_build/linux/mkl/Dockerfile.devel-mkl`** -> AI Confidence: **99.29%**
1410. **`ci/official/libtensorflow.sh`** -> AI Confidence: **99.29%**
1411. **`ci/official/pycpp.sh`** -> AI Confidence: **99.29%**
1412. **`ci/official/utilities/setup_docker.sh`** -> AI Confidence: **99.29%**
1413. **`tensorflow/go/genop/generate.sh`** -> AI Confidence: **99.29%**
1414. **`tensorflow/lite/lib_package/concat_licenses.sh`** -> AI Confidence: **99.29%**
1415. **`tensorflow/tools/ci_build/builds/benchmark.sh`** -> AI Confidence: **99.29%**
1416. **`tensorflow/tools/ci_build/builds/builds_common.sh`** -> AI Confidence: **99.29%**
1417. **`tensorflow/tools/ci_build/builds/cmake.sh`** -> AI Confidence: **99.29%**
1418. **`tensorflow/tools/ci_build/install/install_clang_17.sh`** -> AI Confidence: **99.29%**
1419. **`tensorflow/tools/ci_build/install/install_deb_packages.sh`** -> AI Confidence: **99.29%**
1420. **`tensorflow/tools/ci_build/install/install_mpi.sh`** -> AI Confidence: **99.29%**
1421. **`tensorflow/tools/ci_build/install/install_patchelf.sh`** -> AI Confidence: **99.29%**
1422. **`tensorflow/tools/ci_build/install/install_pip_packages_by_version.sh`** -> AI Confidence: **99.29%**
1423. **`tensorflow/tools/ci_build/linux/cpu/run_mkl.sh`** -> AI Confidence: **99.29%**
1424. **`tensorflow/tools/ci_build/linux/mkl/build-dev-container.sh`** -> AI Confidence: **99.29%**
1425. **`tensorflow/tools/gcs_test/gcs_smoke_wrapper.sh`** -> AI Confidence: **99.29%**
1426. **`tensorflow/tools/lib_package/concat_licenses.sh`** -> AI Confidence: **99.29%**
1427. **`tensorflow/tools/toolchains/cross_compile/cc/cc_wrapper.sh`** -> AI Confidence: **99.29%**
1428. **`tensorflow/compiler/aot/tfcompile.bzl`** -> AI Confidence: **99.29%**
1429. **`tensorflow/compiler/mlir/lite/symlink_files.bzl`** -> AI Confidence: **99.29%**
1430. **`tensorflow/compiler/tests/build_defs.bzl`** -> AI Confidence: **99.29%**
1431. **`tensorflow/dtensor/build_defs.bzl`** -> AI Confidence: **99.29%**
1432. **`tensorflow/python/__init__.py`** -> AI Confidence: **99.29%**
1433. **`tensorflow/tools/compatibility/module_deprecations_v2.py`** -> AI Confidence: **99.29%**
1434. **`tensorflow/cc/framework/test_op.cc`** -> AI Confidence: **99.29%**
1435. **`tensorflow/compiler/mlir/lite/tools/optimize/operator_property.cc`** -> AI Confidence: **99.29%**
1436. **`tensorflow/core/kernels/cwise_op_add_2.cc`** -> AI Confidence: **99.29%**
1437. **`tensorflow/core/kernels/cwise_op_bitwise_or.cc`** -> AI Confidence: **99.29%**
1438. **`tensorflow/core/kernels/cwise_op_equal_to_2.cc`** -> AI Confidence: **99.29%**
1439. **`tensorflow/core/kernels/cwise_op_floor_div.cc`** -> AI Confidence: **99.29%**
1440. **`tensorflow/core/kernels/cwise_op_mul_1.cc`** -> AI Confidence: **99.29%**
1441. **`tensorflow/core/kernels/cwise_op_mul_2.cc`** -> AI Confidence: **99.29%**
1442. **`tensorflow/core/kernels/cwise_op_not_equal_to_2.cc`** -> AI Confidence: **99.29%**
1443. **`tensorflow/core/kernels/cwise_op_reciprocal.cc`** -> AI Confidence: **99.29%**
1444. **`tensorflow/core/kernels/cwise_op_rsqrt.cc`** -> AI Confidence: **99.29%**
1445. **`tensorflow/core/kernels/cwise_op_sigmoid.cc`** -> AI Confidence: **99.29%**
1446. **`tensorflow/core/kernels/cwise_op_sqrt.cc`** -> AI Confidence: **99.29%**
1447. **`tensorflow/core/kernels/cwise_op_sub.cc`** -> AI Confidence: **99.29%**
1448. **`tensorflow/core/kernels/cwise_op_tanh.cc`** -> AI Confidence: **99.29%**
1449. **`tensorflow/core/kernels/reshape_op.cc`** -> AI Confidence: **99.29%**
1450. **`tensorflow/core/kernels/strided_slice_op_define_grad.cc`** -> AI Confidence: **99.29%**
1451. **`tensorflow/core/kernels/strided_slice_op_inst_0.cc`** -> AI Confidence: **99.29%**
1452. **`tensorflow/core/kernels/strided_slice_op_inst_1.cc`** -> AI Confidence: **99.29%**
1453. **`tensorflow/core/kernels/strided_slice_op_inst_2.cc`** -> AI Confidence: **99.29%**
1454. **`tensorflow/core/kernels/strided_slice_op_inst_3.cc`** -> AI Confidence: **99.29%**
1455. **`tensorflow/core/kernels/strided_slice_op_inst_4.cc`** -> AI Confidence: **99.29%**
1456. **`tensorflow/core/kernels/strided_slice_op_inst_5.cc`** -> AI Confidence: **99.29%**
1457. **`tensorflow/core/kernels/strided_slice_op_inst_6.cc`** -> AI Confidence: **99.29%**
1458. **`tensorflow/core/kernels/strided_slice_op_inst_7.cc`** -> AI Confidence: **99.29%**
1459. **`tensorflow/core/kernels/strided_slice_op_inst_8.cc`** -> AI Confidence: **99.29%**
1460. **`tensorflow/core/kernels/tile_ops_gpu_impl_1.cu.cc`** -> AI Confidence: **99.29%**
1461. **`tensorflow/core/kernels/tile_ops_gpu_impl_2.cu.cc`** -> AI Confidence: **99.29%**
1462. **`tensorflow/core/kernels/tile_ops_gpu_impl_3.cu.cc`** -> AI Confidence: **99.29%**
1463. **`tensorflow/core/kernels/tile_ops_gpu_impl_4.cu.cc`** -> AI Confidence: **99.29%**
1464. **`tensorflow/core/kernels/tile_ops_gpu_impl_5.cu.cc`** -> AI Confidence: **99.29%**
1465. **`tensorflow/core/kernels/tile_ops_gpu_impl_6.cu.cc`** -> AI Confidence: **99.29%**
1466. **`tensorflow/core/kernels/tile_ops_gpu_impl_7.cu.cc`** -> AI Confidence: **99.29%**
1467. **`tensorflow/core/kernels/tile_ops_gpu_impl_8.cu.cc`** -> AI Confidence: **99.29%**
1468. **`tensorflow/core/ops/scoped_allocator_ops.cc`** -> AI Confidence: **99.29%**
1469. **`tensorflow/core/platform/png.h`** -> AI Confidence: **99.29%**
1470. **`tensorflow/core/profiler/internal/tfprof_tensor.cc`** -> AI Confidence: **99.29%**
1471. **`tensorflow/java/src/test/native/my_test_op.cc`** -> AI Confidence: **99.29%**
1472. **`tensorflow/lite/delegates/gpu/common/tasks/max_unpooling.cc`** -> AI Confidence: **99.29%**
1473. **`tensorflow/lite/kernels/internal/reference/conv3d.h`** -> AI Confidence: **99.29%**
1474. **`tensorflow/lite/kernels/internal/reference/conv3d_transpose.h`** -> AI Confidence: **99.29%**
1475. **`tensorflow/lite/kernels/internal/reference/integer_ops/depthwise_conv.h`** -> AI Confidence: **99.29%**
1476. **`tensorflow/core/runtime_fallback/util/attr_type.def`** -> AI Confidence: **99.29%**
1477. **`tensorflow/lite/examples/ios/simple/main.mm`** -> AI Confidence: **99.29%**
1478. **`tensorflow/lite/objc/apps/TestApp/TestApp/main.m`** -> AI Confidence: **99.29%**
1479. **`tensorflow/lite/tools/benchmark/ios/TFLiteBenchmark/TFLiteBenchmark/main.m`** -> AI Confidence: **99.29%**
1480. **`tensorflow/lite/tools/evaluation/tasks/ios/TFLiteEvaluation/TFLiteEvaluation/main.m`** -> AI Confidence: **99.29%**
1481. **`tensorflow/lite/java/demo/settings.gradle`** -> AI Confidence: **99.29%**
1482. **`tensorflow/lite/java/ovic/demo/settings.gradle`** -> AI Confidence: **99.29%**
1483. **`tensorflow/core/framework/register_types.h`** -> AI Confidence: **99.27%**
1484. **`tensorflow/lite/kernels/internal/optimized/reduce_utils.h`** -> AI Confidence: **99.26%**
1485. **`tensorflow/examples/speech_commands/input_data.py`** -> AI Confidence: **99.25%**
1486. **`tensorflow/python/compiler/xla/xla.py`** -> AI Confidence: **99.25%**
1487. **`tensorflow/python/keras/models.py`** -> AI Confidence: **99.25%**
1488. **`tensorflow/python/pywrap_tensorflow.py`** -> AI Confidence: **99.25%**
1489. **`tensorflow/c/experimental/saved_model/core/revived_types/asset.h`** -> AI Confidence: **99.25%**
1490. **`tensorflow/c/experimental/saved_model/core/revived_types/constant.h`** -> AI Confidence: **99.25%**
1491. **`tensorflow/c/experimental/saved_model/core/revived_types/restored_resource.h`** -> AI Confidence: **99.25%**
1492. **`tensorflow/c/experimental/saved_model/core/revived_types/variable.h`** -> AI Confidence: **99.25%**
1493. **`tensorflow/compiler/jit/device_compiler.h`** -> AI Confidence: **99.25%**
1494. **`tensorflow/compiler/mlir/lite/kernels/internal/runtime_shape.h`** -> AI Confidence: **99.25%**
1495. **`tensorflow/compiler/mlir/lite/transforms/dilated_conv.h`** -> AI Confidence: **99.25%**
1496. **`tensorflow/compiler/mlir/lite/utils/low_bit_utils.h`** -> AI Confidence: **99.25%**
1497. **`tensorflow/compiler/mlir/tensorflow/ir/tf_arith_ops_folder.h`** -> AI Confidence: **99.25%**
1498. **`tensorflow/core/common_runtime/eager/execute_node.h`** -> AI Confidence: **99.25%**
1499. **`tensorflow/core/kernels/batching_util/concat_split_util.h`** -> AI Confidence: **99.25%**
1500. **`tensorflow/core/kernels/conv_2d_gpu.h`** -> AI Confidence: **99.25%**
1501. **`tensorflow/core/kernels/conv_ops_fused_impl.h`** -> AI Confidence: **99.25%**
1502. **`tensorflow/core/kernels/conv_ops_impl.h`** -> AI Confidence: **99.25%**
1503. **`tensorflow/core/kernels/depthwise_conv_op_gpu.h`** -> AI Confidence: **99.25%**
1504. **`tensorflow/core/kernels/linalg/matrix_triangular_solve_op_impl.h`** -> AI Confidence: **99.25%**
1505. **`tensorflow/core/kernels/list_kernels.h`** -> AI Confidence: **99.25%**
1506. **`tensorflow/core/kernels/matmul_op_impl.h`** -> AI Confidence: **99.25%**
1507. **`tensorflow/core/kernels/mkl/mkl_conv_ops.h`** -> AI Confidence: **99.25%**
1508. **`tensorflow/core/kernels/mkl/mkl_matmul_ops_common.h`** -> AI Confidence: **99.25%**
1509. **`tensorflow/core/kernels/pooling_ops_common.h`** -> AI Confidence: **99.25%**
1510. **`tensorflow/core/kernels/reshape_op.h`** -> AI Confidence: **99.25%**
1511. **`tensorflow/core/kernels/sparse/mat_mul_op.h`** -> AI Confidence: **99.25%**
1512. **`tensorflow/core/kernels/tensor_to_hash_bucket_op.h`** -> AI Confidence: **99.25%**
1513. **`tensorflow/core/profiler/internal/advisor/tfprof_advisor.h`** -> AI Confidence: **99.25%**
1514. **`tensorflow/core/profiler/internal/tfprof_show_multi.h`** -> AI Confidence: **99.25%**
1515. **`tensorflow/core/profiler/internal/tfprof_tensor.h`** -> AI Confidence: **99.25%**
1516. **`tensorflow/core/tpu/kernels/sharding_utils.h`** -> AI Confidence: **99.25%**
1517. **`tensorflow/core/util/image_resizer_state.h`** -> AI Confidence: **99.25%**
1518. **`tensorflow/core/util/tensor_ops_util.h`** -> AI Confidence: **99.25%**
1519. **`tensorflow/dtensor/mlir/dtensor_send_recv.h`** -> AI Confidence: **99.25%**
1520. **`tensorflow/dtensor/mlir/expansions/gather_spmd_expander.h`** -> AI Confidence: **99.25%**
1521. **`tensorflow/lite/core/acceleration/configuration/nnapi_plugin.h`** -> AI Confidence: **99.25%**
1522. **`tensorflow/lite/delegates/gpu/common/memory_management/equality_assignment.h`** -> AI Confidence: **99.25%**
1523. **`tensorflow/lite/delegates/gpu/common/model_builder_helper.h`** -> AI Confidence: **99.25%**
1524. **`tensorflow/lite/delegates/gpu/common/object_reader.h`** -> AI Confidence: **99.25%**
1525. **`tensorflow/lite/delegates/gpu/common/tasks/convolution_transposed_thin.h`** -> AI Confidence: **99.25%**
1526. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv.h`** -> AI Confidence: **99.25%**
1527. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv_3x3.h`** -> AI Confidence: **99.25%**
1528. **`tensorflow/lite/delegates/gpu/common/tasks/fully_connected.h`** -> AI Confidence: **99.25%**
1529. **`tensorflow/lite/delegates/gpu/common/tasks/mean_stddev_normalization.h`** -> AI Confidence: **99.25%**
1530. **`tensorflow/lite/delegates/gpu/common/tasks/special/fc_fc_add.h`** -> AI Confidence: **99.25%**
1531. **`tensorflow/lite/experimental/acceleration/mini_benchmark/model_modifier/custom_validation_embedder.h`** -> AI Confidence: **99.25%**
1532. **`tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8.h`** -> AI Confidence: **99.25%**
1533. **`tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_3x3_filter.h`** -> AI Confidence: **99.25%**
1534. **`tensorflow/lite/kernels/internal/optimized/integer_ops/depthwise_conv.h`** -> AI Confidence: **99.25%**
1535. **`tensorflow/lite/kernels/internal/optimized/resize_bilinear.h`** -> AI Confidence: **99.25%**
1536. **`tensorflow/lite/kernels/stablehlo_elementwise.h`** -> AI Confidence: **99.25%**
1537. **`tensorflow/lite/tools/evaluation/utils.h`** -> AI Confidence: **99.25%**
1538. **`tensorflow/api_template_v1.__init__.py`** -> AI Confidence: **99.24%**
1539. **`tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py`** -> AI Confidence: **99.24%**
1540. **`tensorflow/dtensor/python/d_checkpoint.py`** -> AI Confidence: **99.24%**
1541. **`tensorflow/dtensor/python/dtensor_device.py`** -> AI Confidence: **99.24%**
1542. **`tensorflow/examples/speech_commands/freeze.py`** -> AI Confidence: **99.24%**
1543. **`tensorflow/examples/speech_commands/wav_to_features.py`** -> AI Confidence: **99.24%**
1544. **`tensorflow/lite/python/interpreter.py`** -> AI Confidence: **99.24%**
1545. **`tensorflow/lite/python/lite.py`** -> AI Confidence: **99.24%**
1546. **`tensorflow/lite/tools/flatbuffer_utils_test.py`** -> AI Confidence: **99.24%**
1547. **`tensorflow/lite/tools/optimize/debugging/python/debugger_test.py`** -> AI Confidence: **99.24%**
1548. **`tensorflow/python/checkpoint/checkpoint_management.py`** -> AI Confidence: **99.24%**
1549. **`tensorflow/python/checkpoint/functional_saver.py`** -> AI Confidence: **99.24%**
1550. **`tensorflow/python/checkpoint/sharding/sharding_policies.py`** -> AI Confidence: **99.24%**
1551. **`tensorflow/python/checkpoint/sharding/sharding_util.py`** -> AI Confidence: **99.24%**
1552. **`tensorflow/python/client/session.py`** -> AI Confidence: **99.24%**
1553. **`tensorflow/python/compiler/tensorrt/model_tests/run_models.py`** -> AI Confidence: **99.24%**
1554. **`tensorflow/python/data/kernel_tests/checkpoint_test_base.py`** -> AI Confidence: **99.24%**
1555. **`tensorflow/python/data/ops/structured_function.py`** -> AI Confidence: **99.24%**
1556. **`tensorflow/python/distribute/combinations.py`** -> AI Confidence: **99.24%**
1557. **`tensorflow/python/distribute/distribute_utils.py`** -> AI Confidence: **99.24%**
1558. **`tensorflow/python/distribute/mirrored_strategy.py`** -> AI Confidence: **99.24%**
1559. **`tensorflow/python/distribute/multi_worker_test_base.py`** -> AI Confidence: **99.24%**
1560. **`tensorflow/python/distribute/parameter_server_strategy_v2.py`** -> AI Confidence: **99.24%**
1561. **`tensorflow/python/distribute/sharded_variable.py`** -> AI Confidence: **99.24%**
1562. **`tensorflow/python/eager/context.py`** -> AI Confidence: **99.24%**
1563. **`tensorflow/python/eager/polymorphic_function/atomic_function.py`** -> AI Confidence: **99.24%**
1564. **`tensorflow/python/eager/polymorphic_function/polymorphic_function.py`** -> AI Confidence: **99.24%**
1565. **`tensorflow/python/eager/polymorphic_function/tracing_compilation.py`** -> AI Confidence: **99.24%**
1566. **`tensorflow/python/eager/wrap_function.py`** -> AI Confidence: **99.24%**
1567. **`tensorflow/python/framework/dtypes.py`** -> AI Confidence: **99.24%**
1568. **`tensorflow/python/framework/func_graph.py`** -> AI Confidence: **99.24%**
1569. **`tensorflow/python/framework/ops.py`** -> AI Confidence: **99.24%**
1570. **`tensorflow/python/framework/tensor_shape.py`** -> AI Confidence: **99.24%**
1571. **`tensorflow/python/framework/test_util.py`** -> AI Confidence: **99.24%**
1572. **`tensorflow/python/keras/engine/training_distributed_v1.py`** -> AI Confidence: **99.24%**
1573. **`tensorflow/python/keras/keras_parameterized.py`** -> AI Confidence: **99.24%**
1574. **`tensorflow/python/keras/mixed_precision/policy.py`** -> AI Confidence: **99.24%**
1575. **`tensorflow/python/keras/saving/saved_model/save_impl.py`** -> AI Confidence: **99.24%**
1576. **`tensorflow/python/keras/saving/saving_utils.py`** -> AI Confidence: **99.24%**
1577. **`tensorflow/python/keras/utils/data_utils.py`** -> AI Confidence: **99.24%**
1578. **`tensorflow/python/keras/utils/tf_utils.py`** -> AI Confidence: **99.24%**
1579. **`tensorflow/python/ops/batch_norm_benchmark.py`** -> AI Confidence: **99.24%**
1580. **`tensorflow/python/ops/concat_benchmark.py`** -> AI Confidence: **99.24%**
1581. **`tensorflow/python/ops/logging_ops.py`** -> AI Confidence: **99.24%**
1582. **`tensorflow/python/ops/losses/losses_impl.py`** -> AI Confidence: **99.24%**
1583. **`tensorflow/python/ops/nn_impl.py`** -> AI Confidence: **99.24%**
1584. **`tensorflow/python/ops/numpy_ops/np_utils.py`** -> AI Confidence: **99.24%**
1585. **`tensorflow/python/ops/numpy_ops/tests/extensions.py`** -> AI Confidence: **99.24%**
1586. **`tensorflow/python/ops/parallel_for/control_flow_ops.py`** -> AI Confidence: **99.24%**
1587. **`tensorflow/python/ops/parallel_for/pfor.py`** -> AI Confidence: **99.24%**
1588. **`tensorflow/python/ops/resource_variable_ops.py`** -> AI Confidence: **99.24%**
1589. **`tensorflow/python/ops/script_ops.py`** -> AI Confidence: **99.24%**
1590. **`tensorflow/python/ops/structured/structured_array_ops.py`** -> AI Confidence: **99.24%**
1591. **`tensorflow/python/ops/summary_ops_v2.py`** -> AI Confidence: **99.24%**
1592. **`tensorflow/python/ops/template.py`** -> AI Confidence: **99.24%**
1593. **`tensorflow/python/ops/tensor_array_ops.py`** -> AI Confidence: **99.24%**
1594. **`tensorflow/python/saved_model/builder_impl.py`** -> AI Confidence: **99.24%**
1595. **`tensorflow/python/saved_model/load.py`** -> AI Confidence: **99.24%**
1596. **`tensorflow/python/saved_model/model_utils/export_utils.py`** -> AI Confidence: **99.24%**
1597. **`tensorflow/python/saved_model/save.py`** -> AI Confidence: **99.24%**
1598. **`tensorflow/python/saved_model/signature_serialization.py`** -> AI Confidence: **99.24%**
1599. **`tensorflow/python/tools/saved_model_aot_compile.py`** -> AI Confidence: **99.24%**
1600. **`tensorflow/python/tools/saved_model_cli_test.py`** -> AI Confidence: **99.24%**
1601. **`tensorflow/python/tpu/async_checkpoint.py`** -> AI Confidence: **99.24%**
1602. **`tensorflow/python/tpu/client/client.py`** -> AI Confidence: **99.24%**
1603. **`tensorflow/python/tpu/feature_column_v2.py`** -> AI Confidence: **99.24%**
1604. **`tensorflow/python/tpu/tpu_embedding_v3.py`** -> AI Confidence: **99.24%**
1605. **`tensorflow/python/tpu/tpu_embedding_v3_checkpoint_adapter.py`** -> AI Confidence: **99.24%**
1606. **`tensorflow/python/tpu/tpu_replication.py`** -> AI Confidence: **99.24%**
1607. **`tensorflow/python/tpu/tpu_test_wrapper.py`** -> AI Confidence: **99.24%**
1608. **`tensorflow/python/training/basic_session_run_hooks.py`** -> AI Confidence: **99.24%**
1609. **`tensorflow/python/training/monitored_session.py`** -> AI Confidence: **99.24%**
1610. **`tensorflow/python/training/session_manager.py`** -> AI Confidence: **99.24%**
1611. **`tensorflow/python/training/supervisor.py`** -> AI Confidence: **99.24%**
1612. **`tensorflow/tools/api/tests/api_compatibility_test.py`** -> AI Confidence: **99.24%**
1613. **`tensorflow/tools/compatibility/update/generate_v2_reorders_map.py`** -> AI Confidence: **99.24%**
1614. **`tensorflow/tools/gcs_test/python/gcs_smoke.py`** -> AI Confidence: **99.24%**
1615. **`tensorflow/c/experimental/filesystem/plugins/gcs/gcs_filesystem.cc`** -> AI Confidence: **99.24%**
1616. **`tensorflow/c/experimental/grappler/grappler.cc`** -> AI Confidence: **99.24%**
1617. **`tensorflow/c/experimental/saved_model/core/revived_types/asset.cc`** -> AI Confidence: **99.24%**
1618. **`tensorflow/c/experimental/saved_model/core/revived_types/partially_revived_objects.cc`** -> AI Confidence: **99.24%**
1619. **`tensorflow/cc/tools/freeze_saved_model_test.cc`** -> AI Confidence: **99.24%**
1620. **`tensorflow/compiler/jit/increase_dynamism_for_auto_jit_pass.cc`** -> AI Confidence: **99.24%**
1621. **`tensorflow/compiler/jit/xla_device_context.cc`** -> AI Confidence: **99.24%**
1622. **`tensorflow/compiler/jit/xla_tpu_device.cc`** -> AI Confidence: **99.24%**
1623. **`tensorflow/compiler/mlir/lite/allocation.cc`** -> AI Confidence: **99.24%**
1624. **`tensorflow/compiler/mlir/lite/core/model_builder_base.h`** -> AI Confidence: **99.24%**
1625. **`tensorflow/compiler/mlir/lite/experimental/tac/transforms/fold_constants_to_subgraph.cc`** -> AI Confidence: **99.24%**
1626. **`tensorflow/compiler/mlir/lite/experimental/tac/transforms/get_alternative_subgraph.cc`** -> AI Confidence: **99.24%**
1627. **`tensorflow/compiler/mlir/lite/experimental/tac/transforms/tac_filter.cc`** -> AI Confidence: **99.24%**
1628. **`tensorflow/compiler/mlir/lite/flatbuffer_export.cc`** -> AI Confidence: **99.24%**
1629. **`tensorflow/compiler/mlir/lite/flatbuffer_import.cc`** -> AI Confidence: **99.24%**
1630. **`tensorflow/compiler/mlir/lite/flatbuffer_operator.cc`** -> AI Confidence: **99.24%**
1631. **`tensorflow/compiler/mlir/lite/ir/tfl_ops.cc`** -> AI Confidence: **99.24%**
1632. **`tensorflow/compiler/mlir/lite/metrics/error_collector_inst.cc`** -> AI Confidence: **99.24%**
1633. **`tensorflow/compiler/mlir/lite/metrics/types_util.cc`** -> AI Confidence: **99.24%**
1634. **`tensorflow/compiler/mlir/lite/python/saved_model_to_tfl_flatbuffer.cc`** -> AI Confidence: **99.24%**
1635. **`tensorflow/compiler/mlir/lite/quantization/device_target.cc`** -> AI Confidence: **99.24%**
1636. **`tensorflow/compiler/mlir/lite/quantization/import_quant_stats_pass.cc`** -> AI Confidence: **99.24%**
1637. **`tensorflow/compiler/mlir/lite/quantization/ir/QuantOps.cc`** -> AI Confidence: **99.24%**
1638. **`tensorflow/compiler/mlir/lite/quantization/lite/tfl_to_std.cc`** -> AI Confidence: **99.24%**
1639. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/hlo_matchers.cc`** -> AI Confidence: **99.24%**
1640. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo.cc`** -> AI Confidence: **99.24%**
1641. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/reduce.cc`** -> AI Confidence: **99.24%**
1642. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/reduce_window_util.cc`** -> AI Confidence: **99.24%**
1643. **`tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/scatter.cc`** -> AI Confidence: **99.24%**
1644. **`tensorflow/compiler/mlir/lite/tools/versioning/runtime_version.cc`** -> AI Confidence: **99.24%**
1645. **`tensorflow/compiler/mlir/lite/transforms/decompose_hybrid_quantization.cc`** -> AI Confidence: **99.24%**
1646. **`tensorflow/compiler/mlir/lite/transforms/lift_tflite_flex_ops.cc`** -> AI Confidence: **99.24%**
1647. **`tensorflow/compiler/mlir/lite/transforms/optimize_batch_matmul_pass.cc`** -> AI Confidence: **99.24%**
1648. **`tensorflow/compiler/mlir/lite/transforms/optimize_pass.cc`** -> AI Confidence: **99.24%**
1649. **`tensorflow/compiler/mlir/lite/transforms/partitioned_topological_sort.cc`** -> AI Confidence: **99.24%**
1650. **`tensorflow/compiler/mlir/lite/transforms/prepare_quantize.cc`** -> AI Confidence: **99.24%**
1651. **`tensorflow/compiler/mlir/lite/transforms/quantization/fuse_qdq_pass.cc`** -> AI Confidence: **99.24%**
1652. **`tensorflow/compiler/mlir/lite/transforms/quantize_variables.cc`** -> AI Confidence: **99.24%**
1653. **`tensorflow/compiler/mlir/lite/transforms/utilities/elements_attr_roundtrip_pass.cc`** -> AI Confidence: **99.24%**
1654. **`tensorflow/compiler/mlir/lite/utils/nms_utils.cc`** -> AI Confidence: **99.24%**
1655. **`tensorflow/compiler/mlir/lite/utils/tftext_utils.cc`** -> AI Confidence: **99.24%**
1656. **`tensorflow/compiler/mlir/quantization/common/ir/QuantOps.cc`** -> AI Confidence: **99.24%**
1657. **`tensorflow/compiler/mlir/quantization/common/uniform_quantized_types.cc`** -> AI Confidence: **99.24%**
1658. **`tensorflow/compiler/mlir/quantization/stablehlo/cc/calibration/representative_dataset.cc`** -> AI Confidence: **99.24%**
1659. **`tensorflow/compiler/mlir/quantization/stablehlo/instrumentations/save_report.cc`** -> AI Confidence: **99.24%**
1660. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/bridge/convert_tf_quant_types.cc`** -> AI Confidence: **99.24%**
1661. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/convert_func_to_bfloat16.cc`** -> AI Confidence: **99.24%**
1662. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/quantization_patterns.cc`** -> AI Confidence: **99.24%**
1663. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/quantize_weight.cc`** -> AI Confidence: **99.24%**
1664. **`tensorflow/compiler/mlir/quantization/stablehlo/passes/unwrap_xla_call_module_op.cc`** -> AI Confidence: **99.24%**
1665. **`tensorflow/compiler/mlir/quantization/tensorflow/calibrator/calibration_statistics_collector_histogram.cc`** -> AI Confidence: **99.24%**
1666. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/add_quantization_unit_loc.cc`** -> AI Confidence: **99.24%**
1667. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/cast_bf16_ops_to_f32.cc`** -> AI Confidence: **99.24%**
1668. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/lift_hashtable_ops_as_args.cc`** -> AI Confidence: **99.24%**
1669. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/lift_quantizable_spots_as_functions_drq.cc`** -> AI Confidence: **99.24%**
1670. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/merge_duplicate_resource_ops.cc`** -> AI Confidence: **99.24%**
1671. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/prepare_lifting.cc`** -> AI Confidence: **99.24%**
1672. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/prepare_quantize.cc`** -> AI Confidence: **99.24%**
1673. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/quantize.cc`** -> AI Confidence: **99.24%**
1674. **`tensorflow/compiler/mlir/quantization/tensorflow/passes/quantize_composite_functions.cc`** -> AI Confidence: **99.24%**
1675. **`tensorflow/compiler/mlir/quantization/tensorflow/python/pywrap_quantize_model.cc`** -> AI Confidence: **99.24%**
1676. **`tensorflow/compiler/mlir/quantization/tensorflow/quantize_preprocess.cc`** -> AI Confidence: **99.24%**
1677. **`tensorflow/compiler/mlir/tensorflow/c/c_api_unified_experimental_mlir.cc`** -> AI Confidence: **99.24%**
1678. **`tensorflow/compiler/mlir/tensorflow/ir/tf_arith_ops_folder.cc`** -> AI Confidence: **99.24%**
1679. **`tensorflow/compiler/mlir/tensorflow/ir/tf_device.cc`** -> AI Confidence: **99.24%**
1680. **`tensorflow/compiler/mlir/tensorflow/ir/tf_ops_a_m.cc`** -> AI Confidence: **99.24%**
1681. **`tensorflow/compiler/mlir/tensorflow/ir/tf_ops_n_z.cc`** -> AI Confidence: **99.24%**
1682. **`tensorflow/compiler/mlir/tensorflow/ir/tf_saved_model.cc`** -> AI Confidence: **99.24%**
1683. **`tensorflow/compiler/mlir/tensorflow/transforms/annotate_parameter_replication.cc`** -> AI Confidence: **99.24%**
1684. **`tensorflow/compiler/mlir/tensorflow/transforms/check_control_dependencies.cc`** -> AI Confidence: **99.24%**
1685. **`tensorflow/compiler/mlir/tensorflow/transforms/convert_control_to_data_outputs.cc`** -> AI Confidence: **99.24%**
1686. **`tensorflow/compiler/mlir/tensorflow/transforms/decompose_resource_ops.cc`** -> AI Confidence: **99.24%**
1687. **`tensorflow/compiler/mlir/tensorflow/transforms/decompose_resource_ops_pass.cc`** -> AI Confidence: **99.24%**
1688. **`tensorflow/compiler/mlir/tensorflow/transforms/fold_broadcast.cc`** -> AI Confidence: **99.24%**
1689. **`tensorflow/compiler/mlir/tensorflow/transforms/functional_control_flow_to_regions.cc`** -> AI Confidence: **99.24%**
1690. **`tensorflow/compiler/mlir/tensorflow/transforms/hoist_replicate_invariant_resource_writes.cc`** -> AI Confidence: **99.24%**
1691. **`tensorflow/compiler/mlir/tensorflow/transforms/host_runtime/tpu_metadata_utils.cc`** -> AI Confidence: **99.24%**
1692. **`tensorflow/compiler/mlir/tensorflow/transforms/order_by_dialect.cc`** -> AI Confidence: **99.24%**
1693. **`tensorflow/compiler/mlir/tensorflow/transforms/order_for_program_key.cc`** -> AI Confidence: **99.24%**
1694. **`tensorflow/compiler/mlir/tensorflow/transforms/parallel_execute_to_islands.cc`** -> AI Confidence: **99.24%**
1695. **`tensorflow/compiler/mlir/tensorflow/transforms/region_control_flow_to_functional.cc`** -> AI Confidence: **99.24%**
1696. **`tensorflow/compiler/mlir/tensorflow/transforms/remove_vars_in_session_initializer.cc`** -> AI Confidence: **99.24%**
1697. **`tensorflow/compiler/mlir/tensorflow/transforms/replicate_invariant_op_hoisting.cc`** -> AI Confidence: **99.24%**
1698. **`tensorflow/compiler/mlir/tensorflow/transforms/resource_op_lifting.cc`** -> AI Confidence: **99.24%**
1699. **`tensorflow/compiler/mlir/tensorflow/transforms/shape_inference.cc`** -> AI Confidence: **99.24%**
1700. **`tensorflow/compiler/mlir/tensorflow/transforms/stack_ops_decomposition.cc`** -> AI Confidence: **99.24%**
1701. **`tensorflow/compiler/mlir/tensorflow/transforms/tensor_array_ops_decomposition.cc`** -> AI Confidence: **99.24%**
1702. **`tensorflow/compiler/mlir/tensorflow/transforms/tensor_device_copy_conversion.cc`** -> AI Confidence: **99.24%**
1703. **`tensorflow/compiler/mlir/tensorflow/transforms/tf_saved_model_freeze_variables.cc`** -> AI Confidence: **99.24%**
1704. **`tensorflow/compiler/mlir/tensorflow/transforms/tfg-to-tfe.cc`** -> AI Confidence: **99.24%**
1705. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_annotate_dynamic_shape_inputs.cc`** -> AI Confidence: **99.24%**
1706. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_dynamic_layout_pass.cc`** -> AI Confidence: **99.24%**
1707. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_identity_pruning.cc`** -> AI Confidence: **99.24%**
1708. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_parallel_execute_sink_resource_write.cc`** -> AI Confidence: **99.24%**
1709. **`tensorflow/compiler/mlir/tensorflow/transforms/tpu_reorder_replicate_and_partitioned_inputs.cc`** -> AI Confidence: **99.24%**
1710. **`tensorflow/compiler/mlir/tensorflow/transforms/update_control_dependencies.cc`** -> AI Confidence: **99.24%**
1711. **`tensorflow/compiler/mlir/tensorflow/translate/tf_mlir_translate.cc`** -> AI Confidence: **99.24%**
1712. **`tensorflow/compiler/mlir/tensorflow/utils/attribute_utils.cc`** -> AI Confidence: **99.24%**
1713. **`tensorflow/compiler/mlir/tensorflow/utils/convert_tensor.cc`** -> AI Confidence: **99.24%**
1714. **`tensorflow/compiler/mlir/tensorflow/utils/device_util.cc`** -> AI Confidence: **99.24%**
1715. **`tensorflow/compiler/mlir/tensorflow/utils/tpu_rewrite_device_util.cc`** -> AI Confidence: **99.24%**
1716. **`tensorflow/compiler/mlir/tensorflow/utils/visitor.cc`** -> AI Confidence: **99.24%**
1717. **`tensorflow/compiler/mlir/tf2xla/api/v2/graph_to_tf_executor.cc`** -> AI Confidence: **99.24%**
1718. **`tensorflow/compiler/mlir/tf2xla/internal/mlir_bridge_pass_util.cc`** -> AI Confidence: **99.24%**
1719. **`tensorflow/compiler/mlir/tf2xla/internal/passes/hoist_broadcast_read.cc`** -> AI Confidence: **99.24%**
1720. **`tensorflow/compiler/mlir/tf2xla/internal/passes/tpu_cluster_formation.cc`** -> AI Confidence: **99.24%**
1721. **`tensorflow/compiler/mlir/tf2xla/internal/passes/tpu_validate_inputs.cc`** -> AI Confidence: **99.24%**
1722. **`tensorflow/compiler/mlir/tf2xla/transforms/legalize_tf_collective.cc`** -> AI Confidence: **99.24%**
1723. **`tensorflow/compiler/mlir/tf2xla/transforms/legalize_tf_with_tf2xla.cc`** -> AI Confidence: **99.24%**
1724. **`tensorflow/compiler/mlir/tf2xla/transforms/split_into_island_per_op_pass.cc`** -> AI Confidence: **99.24%**
1725. **`tensorflow/compiler/mlir/tf2xla/transforms/tf2xla_rewriter.cc`** -> AI Confidence: **99.24%**
1726. **`tensorflow/compiler/mlir/tf2xla/transforms/xla_legalize_targets.cc`** -> AI Confidence: **99.24%**
1727. **`tensorflow/compiler/mlir/tfr/ir/tfr_ops.cc`** -> AI Confidence: **99.24%**
1728. **`tensorflow/compiler/mlir/tfr/passes/decompose.cc`** -> AI Confidence: **99.24%**
1729. **`tensorflow/compiler/mlir/tfr/passes/raise_to_tf.cc`** -> AI Confidence: **99.24%**
1730. **`tensorflow/compiler/mlir/tfrt/function/function.cc`** -> AI Confidence: **99.24%**
1731. **`tensorflow/compiler/mlir/tfrt/transforms/fallback_converter.cc`** -> AI Confidence: **99.24%**
1732. **`tensorflow/compiler/mlir/tfrt/transforms/ifrt/lower_to_ifrt_restore_variable.cc`** -> AI Confidence: **99.24%**
1733. **`tensorflow/compiler/mlir/tfrt/transforms/ifrt/sink_variable_as_named_array.cc`** -> AI Confidence: **99.24%**
1734. **`tensorflow/compiler/mlir/tfrt/transforms/ifrt/tf2hlo.cc`** -> AI Confidence: **99.24%**
1735. **`tensorflow/compiler/mlir/tfrt/transforms/ifrt/tf_restore_merging.cc`** -> AI Confidence: **99.24%**
1736. **`tensorflow/compiler/mlir/tfrt/transforms/lower_saved_model.cc`** -> AI Confidence: **99.24%**
1737. **`tensorflow/compiler/mlir/tfrt/transforms/mlrt/ifrt_set_tpu_host_allocator.cc`** -> AI Confidence: **99.24%**
1738. **`tensorflow/compiler/mlir/tfrt/transforms/optimize.cc`** -> AI Confidence: **99.24%**
1739. **`tensorflow/compiler/mlir/tfrt/transforms/tf_to_tfrt.cc`** -> AI Confidence: **99.24%**
1740. **`tensorflow/compiler/mlir/tfrt/translate/import_model.cc`** -> AI Confidence: **99.24%**
1741. **`tensorflow/compiler/mlir/tfrt/translate/mlrt/test_utils.h`** -> AI Confidence: **99.24%**
1742. **`tensorflow/compiler/mlir/tools/kernel_gen/ir/tf_framework_ops.cc`** -> AI Confidence: **99.24%**
1743. **`tensorflow/compiler/mlir/tools/kernel_gen/tf_gpu_runtime_wrappers.cc`** -> AI Confidence: **99.24%**
1744. **`tensorflow/compiler/mlir/tools/kernel_gen/transforms/gpu_kernel_to_blob_pass.cc`** -> AI Confidence: **99.24%**
1745. **`tensorflow/compiler/mlir/tosa/transforms/convert_tfl_uint.cc`** -> AI Confidence: **99.24%**
1746. **`tensorflow/compiler/mlir/tosa/transforms/legalize_common.cc`** -> AI Confidence: **99.24%**
1747. **`tensorflow/compiler/mlir/tosa/transforms/legalize_utils.cc`** -> AI Confidence: **99.24%**
1748. **`tensorflow/compiler/mlir/utils/saved_model_converter_utils.cc`** -> AI Confidence: **99.24%**
1749. **`tensorflow/compiler/tf2tensorrt/convert/trt_layout_optimization_pass.cc`** -> AI Confidence: **99.24%**
1750. **`tensorflow/compiler/tf2tensorrt/kernels/trt_engine_op.cc`** -> AI Confidence: **99.24%**
1751. **`tensorflow/compiler/tf2tensorrt/segment/segment.cc`** -> AI Confidence: **99.24%**
1752. **`tensorflow/compiler/tf2tensorrt/utils/trt_lru_cache.cc`** -> AI Confidence: **99.24%**
1753. **`tensorflow/compiler/tf2tensorrt/utils/trt_shape_optimization_profiles.h`** -> AI Confidence: **99.24%**
1754. **`tensorflow/compiler/tf2xla/kernels/all_reduce_op.cc`** -> AI Confidence: **99.24%**
1755. **`tensorflow/compiler/tf2xla/kernels/arg_op.cc`** -> AI Confidence: **99.24%**
1756. **`tensorflow/compiler/tf2xla/kernels/batchtospace_op.cc`** -> AI Confidence: **99.24%**
1757. **`tensorflow/compiler/tf2xla/kernels/beta_op.cc`** -> AI Confidence: **99.24%**
1758. **`tensorflow/compiler/tf2xla/kernels/categorical_op.cc`** -> AI Confidence: **99.24%**
1759. **`tensorflow/compiler/tf2xla/kernels/const_op.cc`** -> AI Confidence: **99.24%**
1760. **`tensorflow/compiler/tf2xla/kernels/dynamic_partition_op.cc`** -> AI Confidence: **99.24%**
1761. **`tensorflow/compiler/tf2xla/kernels/mirror_pad_op.cc`** -> AI Confidence: **99.24%**
1762. **`tensorflow/compiler/tf2xla/kernels/pack_op.cc`** -> AI Confidence: **99.24%**
1763. **`tensorflow/compiler/tf2xla/kernels/pad_op.cc`** -> AI Confidence: **99.24%**
1764. **`tensorflow/compiler/tf2xla/kernels/random_ops_util.cc`** -> AI Confidence: **99.24%**
1765. **`tensorflow/compiler/tf2xla/kernels/reduction_ops_common.cc`** -> AI Confidence: **99.24%**
1766. **`tensorflow/compiler/tf2xla/kernels/reverse_op.cc`** -> AI Confidence: **99.24%**
1767. **`tensorflow/compiler/tf2xla/kernels/reverse_sequence_op.cc`** -> AI Confidence: **99.24%**
1768. **`tensorflow/compiler/tf2xla/kernels/shape_op.cc`** -> AI Confidence: **99.24%**
1769. **`tensorflow/compiler/tf2xla/kernels/spacetobatch_op.cc`** -> AI Confidence: **99.24%**
1770. **`tensorflow/compiler/tf2xla/kernels/training_ops.cc`** -> AI Confidence: **99.24%**
1771. **`tensorflow/compiler/tf2xla/kernels/where_op.cc`** -> AI Confidence: **99.24%**
1772. **`tensorflow/compiler/tf2xla/kernels/xla_custom_call_v2_op.cc`** -> AI Confidence: **99.24%**
1773. **`tensorflow/compiler/tf2xla/layout_util.cc`** -> AI Confidence: **99.24%**
1774. **`tensorflow/compiler/tf2xla/mlir_bridge_pass.cc`** -> AI Confidence: **99.24%**
1775. **`tensorflow/compiler/tf2xla/tf2xla_opset.cc`** -> AI Confidence: **99.24%**
1776. **`tensorflow/compiler/tf2xla/tf2xla_supported_ops.cc`** -> AI Confidence: **99.24%**
1777. **`tensorflow/core/common_runtime/all_to_all.cc`** -> AI Confidence: **99.24%**
1778. **`tensorflow/core/common_runtime/eager/context.cc`** -> AI Confidence: **99.24%**
1779. **`tensorflow/core/common_runtime/eager/small_constants_optimizer.cc`** -> AI Confidence: **99.24%**
1780. **`tensorflow/core/common_runtime/eager/tensor_handle.cc`** -> AI Confidence: **99.24%**
1781. **`tensorflow/core/common_runtime/graph_constructor.cc`** -> AI Confidence: **99.24%**
1782. **`tensorflow/core/common_runtime/graph_runner.cc`** -> AI Confidence: **99.24%**
1783. **`tensorflow/core/common_runtime/inspecting_placer.cc`** -> AI Confidence: **99.24%**
1784. **`tensorflow/core/common_runtime/local_device.cc`** -> AI Confidence: **99.24%**
1785. **`tensorflow/core/common_runtime/lower_while_op.cc`** -> AI Confidence: **99.24%**
1786. **`tensorflow/core/common_runtime/memory_types.cc`** -> AI Confidence: **99.24%**
1787. **`tensorflow/core/common_runtime/next_pluggable_device/next_pluggable_device.cc`** -> AI Confidence: **99.24%**
1788. **`tensorflow/core/common_runtime/pluggable_device/pluggable_device_util.cc`** -> AI Confidence: **99.24%**
1789. **`tensorflow/core/common_runtime/step_stats_collector.cc`** -> AI Confidence: **99.24%**
1790. **`tensorflow/core/data/global_shuffle_utils.cc`** -> AI Confidence: **99.24%**
1791. **`tensorflow/core/data/metric_utils.cc`** -> AI Confidence: **99.24%**
1792. **`tensorflow/core/data/rewrite_utils.cc`** -> AI Confidence: **99.24%**
1793. **`tensorflow/core/data/service/auto_scaler.cc`** -> AI Confidence: **99.24%**
1794. **`tensorflow/core/data/service/dispatcher_client.cc`** -> AI Confidence: **99.24%**
1795. **`tensorflow/core/data/service/dispatcher_state.cc`** -> AI Confidence: **99.24%**
1796. **`tensorflow/core/data/service/grpc_util.cc`** -> AI Confidence: **99.24%**
1797. **`tensorflow/core/data/service/journal.cc`** -> AI Confidence: **99.24%**
1798. **`tensorflow/core/data/service/snapshot/snapshot_stream_writer.cc`** -> AI Confidence: **99.24%**
1799. **`tensorflow/core/data/service/snapshot/test_utils.cc`** -> AI Confidence: **99.24%**
1800. **`tensorflow/core/data/service/split_provider.cc`** -> AI Confidence: **99.24%**
1801. **`tensorflow/core/data/service/test_cluster.cc`** -> AI Confidence: **99.24%**
1802. **`tensorflow/core/data/service/validate_utils.cc`** -> AI Confidence: **99.24%**
1803. **`tensorflow/core/data/service/worker_client.cc`** -> AI Confidence: **99.24%**
1804. **`tensorflow/core/data/snapshot_utils.cc`** -> AI Confidence: **99.24%**
1805. **`tensorflow/core/data/tf_data_memory_logger.cc`** -> AI Confidence: **99.24%**
1806. **`tensorflow/core/distributed_runtime/cluster_function_library_runtime.cc`** -> AI Confidence: **99.24%**
1807. **`tensorflow/core/distributed_runtime/eager/cluster_function_library_runtime.cc`** -> AI Confidence: **99.24%**
1808. **`tensorflow/core/distributed_runtime/eager/remote_mgr.cc`** -> AI Confidence: **99.24%**
1809. **`tensorflow/core/distributed_runtime/rpc/eager/grpc_eager_client.cc`** -> AI Confidence: **99.24%**
1810. **`tensorflow/core/example/example_parser_configuration.cc`** -> AI Confidence: **99.24%**
1811. **`tensorflow/core/framework/device_factory.cc`** -> AI Confidence: **99.24%**
1812. **`tensorflow/core/framework/full_type_inference_util.cc`** -> AI Confidence: **99.24%**
1813. **`tensorflow/core/framework/full_type_util.cc`** -> AI Confidence: **99.24%**
1814. **`tensorflow/core/framework/node_def_util.cc`** -> AI Confidence: **99.24%**
1815. **`tensorflow/core/framework/op.cc`** -> AI Confidence: **99.24%**
1816. **`tensorflow/core/framework/op_kernel_benchmark.cc`** -> AI Confidence: **99.24%**
1817. **`tensorflow/core/framework/rendezvous.cc`** -> AI Confidence: **99.24%**
1818. **`tensorflow/core/framework/resource_mgr.cc`** -> AI Confidence: **99.24%**
1819. **`tensorflow/core/framework/tensor_matcher.cc`** -> AI Confidence: **99.24%**
1820. **`tensorflow/core/framework/tensor_util.cc`** -> AI Confidence: **99.24%**
1821. **`tensorflow/core/framework/variant_op_registry.cc`** -> AI Confidence: **99.24%**
1822. **`tensorflow/core/function/runtime_client/runtime_client.cc`** -> AI Confidence: **99.24%**
1823. **`tensorflow/core/graph/graph.cc`** -> AI Confidence: **99.24%**
1824. **`tensorflow/core/grappler/clusters/virtual_cluster.cc`** -> AI Confidence: **99.24%**
1825. **`tensorflow/core/grappler/costs/virtual_scheduler.cc`** -> AI Confidence: **99.24%**
1826. **`tensorflow/core/grappler/graph_analyzer/subgraph.cc`** -> AI Confidence: **99.24%**
1827. **`tensorflow/core/grappler/grappler_item.h`** -> AI Confidence: **99.24%**
1828. **`tensorflow/core/grappler/optimizers/auto_mixed_precision.cc`** -> AI Confidence: **99.24%**
1829. **`tensorflow/core/grappler/optimizers/data/enable_gradient_descent.cc`** -> AI Confidence: **99.24%**
1830. **`tensorflow/core/grappler/optimizers/data/filter_fusion.cc`** -> AI Confidence: **99.24%**
1831. **`tensorflow/core/grappler/optimizers/data/filter_parallelization.cc`** -> AI Confidence: **99.24%**
1832. **`tensorflow/core/grappler/optimizers/data/inject_io_prefetch.cc`** -> AI Confidence: **99.24%**
1833. **`tensorflow/core/grappler/optimizers/data/inject_prefetch.cc`** -> AI Confidence: **99.24%**
1834. **`tensorflow/core/grappler/optimizers/data/map_and_filter_fusion.cc`** -> AI Confidence: **99.24%**
1835. **`tensorflow/core/grappler/optimizers/data/map_parallelization.cc`** -> AI Confidence: **99.24%**
1836. **`tensorflow/core/grappler/optimizers/data/meta_optimizer.cc`** -> AI Confidence: **99.24%**
1837. **`tensorflow/core/grappler/optimizers/data/noop_elimination.cc`** -> AI Confidence: **99.24%**
1838. **`tensorflow/core/grappler/optimizers/data/remove_compression_map.cc`** -> AI Confidence: **99.24%**
1839. **`tensorflow/core/grappler/optimizers/data/replicate_on_split.cc`** -> AI Confidence: **99.24%**
1840. **`tensorflow/core/grappler/optimizers/data/split_utils.cc`** -> AI Confidence: **99.24%**
1841. **`tensorflow/core/grappler/optimizers/evaluation_utils.cc`** -> AI Confidence: **99.24%**
1842. **`tensorflow/core/grappler/optimizers/function_optimizer.cc`** -> AI Confidence: **99.24%**
1843. **`tensorflow/core/ir/importexport/graphdef_import.cc`** -> AI Confidence: **99.24%**
1844. **`tensorflow/core/ir/interfaces.cc`** -> AI Confidence: **99.24%**
1845. **`tensorflow/core/ir/types/dialect.cc`** -> AI Confidence: **99.24%**
1846. **`tensorflow/core/ir/utility.cc`** -> AI Confidence: **99.24%**
1847. **`tensorflow/core/kernels/bincount_op.cc`** -> AI Confidence: **99.24%**
1848. **`tensorflow/core/kernels/bucketize_op_gpu.cu.cc`** -> AI Confidence: **99.24%**
1849. **`tensorflow/core/kernels/check_numerics_op.cc`** -> AI Confidence: **99.24%**
1850. **`tensorflow/core/kernels/conv_grad_filter_ops.cc`** -> AI Confidence: **99.24%**
1851. **`tensorflow/core/kernels/conv_grad_filter_ops_3d.cc`** -> AI Confidence: **99.24%**
1852. **`tensorflow/core/kernels/conv_grad_shape_utils.cc`** -> AI Confidence: **99.24%**
1853. **`tensorflow/core/kernels/data/cache_dataset_ops.cc`** -> AI Confidence: **99.24%**
1854. **`tensorflow/core/kernels/data/experimental/parallel_interleave_dataset_op.cc`** -> AI Confidence: **99.24%**
1855. **`tensorflow/core/kernels/data/experimental/snapshot_dataset_op.cc`** -> AI Confidence: **99.24%**
1856. **`tensorflow/core/kernels/data/experimental/sql_dataset_op.cc`** -> AI Confidence: **99.24%**
1857. **`tensorflow/core/kernels/data/experimental/unbatch_dataset_op.cc`** -> AI Confidence: **99.24%**
1858. **`tensorflow/core/kernels/data/experimental/unique_dataset_op.cc`** -> AI Confidence: **99.24%**
1859. **`tensorflow/core/kernels/data/experimental/weighted_flat_map_dataset_op.cc`** -> AI Confidence: **99.24%**
1860. **`tensorflow/core/kernels/data/iterator_ops.cc`** -> AI Confidence: **99.24%**
1861. **`tensorflow/core/kernels/data/repeat_dataset_op.cc`** -> AI Confidence: **99.24%**
1862. **`tensorflow/core/kernels/data/text_line_dataset_op.cc`** -> AI Confidence: **99.24%**
1863. **`tensorflow/core/kernels/decode_compressed_op.cc`** -> AI Confidence: **99.24%**
1864. **`tensorflow/core/kernels/depthtospace_op.cc`** -> AI Confidence: **99.24%**
1865. **`tensorflow/core/kernels/depthwise_conv_grad_op.cc`** -> AI Confidence: **99.24%**
1866. **`tensorflow/core/kernels/dynamic_partition_op.cc`** -> AI Confidence: **99.24%**
1867. **`tensorflow/core/kernels/encode_proto_op.cc`** -> AI Confidence: **99.24%**
1868. **`tensorflow/core/kernels/fixed_length_record_reader_op.cc`** -> AI Confidence: **99.24%**
1869. **`tensorflow/core/kernels/gpu_utils.cc`** -> AI Confidence: **99.24%**
1870. **`tensorflow/core/kernels/image/crop_and_resize_op.cc`** -> AI Confidence: **99.24%**
1871. **`tensorflow/core/kernels/image/resize_bicubic_op.cc`** -> AI Confidence: **99.24%**
1872. **`tensorflow/core/kernels/image/resize_nearest_neighbor_op.cc`** -> AI Confidence: **99.24%**
1873. **`tensorflow/core/kernels/linalg/banded_triangular_solve_op.cc`** -> AI Confidence: **99.24%**
1874. **`tensorflow/core/kernels/linalg/determinant_op.cc`** -> AI Confidence: **99.24%**
1875. **`tensorflow/core/kernels/linalg/matrix_diag_op.cc`** -> AI Confidence: **99.24%**
1876. **`tensorflow/core/kernels/linalg/matrix_inverse_op.cc`** -> AI Confidence: **99.24%**
1877. **`tensorflow/core/kernels/linalg/matrix_set_diag_op.cc`** -> AI Confidence: **99.24%**
1878. **`tensorflow/core/kernels/linalg/tridiagonal_solve_op.cc`** -> AI Confidence: **99.24%**
1879. **`tensorflow/core/kernels/lrn_op.cc`** -> AI Confidence: **99.24%**
1880. **`tensorflow/core/kernels/maxpooling_op.cc`** -> AI Confidence: **99.24%**
1881. **`tensorflow/core/kernels/mkl/mkl_batch_matmul_op.cc`** -> AI Confidence: **99.24%**
1882. **`tensorflow/core/kernels/mkl/mkl_softmax_op.cc`** -> AI Confidence: **99.24%**
1883. **`tensorflow/core/kernels/mkl/mkl_sparse_matrix_matmul_op.cc`** -> AI Confidence: **99.24%**
1884. **`tensorflow/core/kernels/mutex_ops.cc`** -> AI Confidence: **99.24%**
1885. **`tensorflow/core/kernels/parse_tensor_op.cc`** -> AI Confidence: **99.24%**
1886. **`tensorflow/core/kernels/ragged_cross_op.cc`** -> AI Confidence: **99.24%**
1887. **`tensorflow/core/kernels/random_binomial_op.cc`** -> AI Confidence: **99.24%**
1888. **`tensorflow/core/kernels/scatter_op.cc`** -> AI Confidence: **99.24%**
1889. **`tensorflow/core/kernels/sdca_ops.cc`** -> AI Confidence: **99.24%**
1890. **`tensorflow/core/kernels/sendrecv_ops.cc`** -> AI Confidence: **99.24%**
1891. **`tensorflow/core/kernels/sparse/add_op.cc`** -> AI Confidence: **99.24%**
1892. **`tensorflow/core/kernels/sparse_to_dense_op.cc`** -> AI Confidence: **99.24%**
1893. **`tensorflow/core/kernels/split_op.cc`** -> AI Confidence: **99.24%**
1894. **`tensorflow/core/kernels/stack.cc`** -> AI Confidence: **99.24%**
1895. **`tensorflow/core/kernels/string_split_op.cc`** -> AI Confidence: **99.24%**
1896. **`tensorflow/core/kernels/topk_op.cc`** -> AI Confidence: **99.24%**
1897. **`tensorflow/core/kernels/transpose_op.cc`** -> AI Confidence: **99.24%**
1898. **`tensorflow/core/kernels/word2vec_kernels.cc`** -> AI Confidence: **99.24%**
1899. **`tensorflow/core/ops/compat/update_ops_main.cc`** -> AI Confidence: **99.24%**
1900. **`tensorflow/core/runtime_fallback/kernel/kernel_fallback_execute.cc`** -> AI Confidence: **99.24%**
1901. **`tensorflow/core/runtime_fallback/runtime/kernel_utils.cc`** -> AI Confidence: **99.24%**
1902. **`tensorflow/core/runtime_fallback/runtime/runtime_fallback_kernels.cc`** -> AI Confidence: **99.24%**
1903. **`tensorflow/core/runtime_fallback/runtime/runtime_fallback_tensor.cc`** -> AI Confidence: **99.24%**
1904. **`tensorflow/core/runtime_fallback/tf_bef_executor_main.cc`** -> AI Confidence: **99.24%**
1905. **`tensorflow/core/tfrt/ifrt/checkpoint_loader.cc`** -> AI Confidence: **99.24%**
1906. **`tensorflow/core/tfrt/ifrt/ifrt_serving_executable.cc`** -> AI Confidence: **99.24%**
1907. **`tensorflow/core/tfrt/ifrt/sharding_utils.cc`** -> AI Confidence: **99.24%**
1908. **`tensorflow/core/tfrt/kernels/ifrt_program_ops.cc`** -> AI Confidence: **99.24%**
1909. **`tensorflow/core/tfrt/mlrt/attribute/attribute.cc`** -> AI Confidence: **99.24%**
1910. **`tensorflow/core/tpu/kernels/infeed_ops.cc`** -> AI Confidence: **99.24%**
1911. **`tensorflow/core/tpu/kernels/tpu_dummy_input_op.cc`** -> AI Confidence: **99.24%**
1912. **`tensorflow/core/tpu/kernels/tpu_reshard_variables_op_util.cc`** -> AI Confidence: **99.24%**
1913. **`tensorflow/core/tpu/kernels/xla/infeed_op.cc`** -> AI Confidence: **99.24%**
1914. **`tensorflow/core/tpu/ops/sparse_core_ops.cc`** -> AI Confidence: **99.24%**
1915. **`tensorflow/core/tpu/tpu_api_dlsym_initializer.cc`** -> AI Confidence: **99.24%**
1916. **`tensorflow/core/tpu/tpu_global_init.cc`** -> AI Confidence: **99.24%**
1917. **`tensorflow/core/transforms/func_to_graph/func_to_graph.cc`** -> AI Confidence: **99.24%**
1918. **`tensorflow/core/transforms/graph_to_func/graph_to_func.cc`** -> AI Confidence: **99.24%**
1919. **`tensorflow/core/transforms/utils/eval_utils.cc`** -> AI Confidence: **99.24%**
1920. **`tensorflow/core/util/batch_util.cc`** -> AI Confidence: **99.24%**
1921. **`tensorflow/core/util/dump_graph.cc`** -> AI Confidence: **99.24%**
1922. **`tensorflow/core/util/events_writer.cc`** -> AI Confidence: **99.24%**
1923. **`tensorflow/dtensor/cc/dtensor_tpu_kernels.cc`** -> AI Confidence: **99.24%**
1924. **`tensorflow/dtensor/cc/dtensor_utils.cc`** -> AI Confidence: **99.24%**
1925. **`tensorflow/dtensor/cc/xla_spmd/layout_to_xla_sharding.cc`** -> AI Confidence: **99.24%**
1926. **`tensorflow/dtensor/mlir/cluster_function_conversion.cc`** -> AI Confidence: **99.24%**
1927. **`tensorflow/dtensor/mlir/collectives_common.cc`** -> AI Confidence: **99.24%**
1928. **`tensorflow/dtensor/mlir/constant_folding.cc`** -> AI Confidence: **99.24%**
1929. **`tensorflow/dtensor/mlir/device_mesh_cluster_coarsening.cc`** -> AI Confidence: **99.24%**
1930. **`tensorflow/dtensor/mlir/dtensor_allreduce_scatter_optimization.cc`** -> AI Confidence: **99.24%**
1931. **`tensorflow/dtensor/mlir/dtensor_location.cc`** -> AI Confidence: **99.24%**
1932. **`tensorflow/dtensor/mlir/dtensor_mlir_passes.cc`** -> AI Confidence: **99.24%**
1933. **`tensorflow/dtensor/mlir/expansions/argmax_spmd_expander.cc`** -> AI Confidence: **99.24%**
1934. **`tensorflow/dtensor/mlir/expansions/bias_add_spmd_expander.cc`** -> AI Confidence: **99.24%**
1935. **`tensorflow/dtensor/mlir/expansions/broadcast_to_spmd_expander.cc`** -> AI Confidence: **99.24%**
1936. **`tensorflow/dtensor/mlir/expansions/meta_spmd_expander.cc`** -> AI Confidence: **99.24%**
1937. **`tensorflow/dtensor/mlir/expansions/nullary_spmd_expander.cc`** -> AI Confidence: **99.24%**
1938. **`tensorflow/dtensor/mlir/expansions/save_restore_spmd_expander.cc`** -> AI Confidence: **99.24%**
1939. **`tensorflow/dtensor/mlir/expansions/split_spmd_expander.cc`** -> AI Confidence: **99.24%**
1940. **`tensorflow/dtensor/mlir/expansions/strided_slice_spmd_expander.cc`** -> AI Confidence: **99.24%**
1941. **`tensorflow/dtensor/mlir/handle_cross_cluster_dependencies.cc`** -> AI Confidence: **99.24%**
1942. **`tensorflow/dtensor/mlir/handle_sparsetensors.cc`** -> AI Confidence: **99.24%**
1943. **`tensorflow/dtensor/mlir/merge_clusters.cc`** -> AI Confidence: **99.24%**
1944. **`tensorflow/dtensor/mlir/op_utils.cc`** -> AI Confidence: **99.24%**
1945. **`tensorflow/dtensor/mlir/topological_iterator.cc`** -> AI Confidence: **99.24%**
1946. **`tensorflow/dtensor/mlir/tpu_add_resource_device_attribute.cc`** -> AI Confidence: **99.24%**
1947. **`tensorflow/dtensor/mlir/utils/update_tpu_metadata.cc`** -> AI Confidence: **99.24%**
1948. **`tensorflow/dtensor/mlir/value_utils.cc`** -> AI Confidence: **99.24%**
1949. **`tensorflow/examples/custom_ops_doc/multiplex_3/multiplex_3_kernel.cc`** -> AI Confidence: **99.24%**
1950. **`tensorflow/lite/core/async/async_subgraph.cc`** -> AI Confidence: **99.24%**
1951. **`tensorflow/lite/delegates/coreml/builders/concatenation_op_builder.cc`** -> AI Confidence: **99.24%**
1952. **`tensorflow/lite/delegates/gpu/cl/gl_interop.cc`** -> AI Confidence: **99.24%**
1953. **`tensorflow/lite/delegates/gpu/cl/gpu_api_delegate.cc`** -> AI Confidence: **99.24%**
1954. **`tensorflow/lite/delegates/gpu/common/lstm_parser.cc`** -> AI Confidence: **99.24%**
1955. **`tensorflow/lite/delegates/gpu/common/memory_management.cc`** -> AI Confidence: **99.24%**
1956. **`tensorflow/lite/delegates/gpu/common/model.cc`** -> AI Confidence: **99.24%**
1957. **`tensorflow/lite/delegates/gpu/common/operations.cc`** -> AI Confidence: **99.24%**
1958. **`tensorflow/lite/delegates/gpu/common/task/serialization_base.cc`** -> AI Confidence: **99.24%**
1959. **`tensorflow/lite/delegates/gpu/common/tasks/conv_generic_test_util.cc`** -> AI Confidence: **99.24%**
1960. **`tensorflow/lite/delegates/gpu/common/tasks/depthwise_conv_test_util.cc`** -> AI Confidence: **99.24%**
1961. **`tensorflow/lite/delegates/gpu/common/tasks/elementwise_test_util.cc`** -> AI Confidence: **99.24%**
1962. **`tensorflow/lite/delegates/gpu/common/tasks/mean_stddev_normalization_test_util.cc`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tensorflow/core/util/gpu_device_functions.h` -> **0.0089%** Exposure
### Exploit Generation Surface
- `ci/official/utilities/convert_msys_paths_to_win_paths.py` -> **100.0%** Exposure
- `ci/official/utilities/extract_resultstore_links.py` -> **100.0%** Exposure
- `configure.py` -> **100.0%** Exposure
- `tensorflow/cc/saved_model/testdata/generate_saved_models.py` -> **100.0%** Exposure
- `tensorflow/compiler/aot/tests/make_test_graphs.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `ci/official/utilities/setup_macos.sh` -> **100.0%** Exposure
- `tensorflow/lite/ios/build_frameworks.sh` -> **100.0%** Exposure
- `tensorflow/lite/tools/build_aar.sh` -> **100.0%** Exposure
- `tensorflow/lite/tools/pip_package/build_pip_package_with_bazel.sh` -> **100.0%** Exposure
- `tensorflow/lite/tools/pip_package/build_pip_package_with_cmake.sh` -> **100.0%** Exposure
### Raw Memory Manipulation
- `tensorflow/c/c_api.cc` -> **10.0%** Exposure
- `tensorflow/core/common_runtime/mkl_layout_pass.cc` -> **10.0%** Exposure
- `tensorflow/core/framework/common_shape_fns.cc` -> **10.0%** Exposure
- `tensorflow/core/ops/array_ops.cc` -> **10.0%** Exposure
- `tensorflow/core/ops/data_flow_ops.cc` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `ci/official/utilities/code_check_changed_files.bats` -> **100.0%** Exposure
- `ci/official/utilities/code_check_full.bats` -> **100.0%** Exposure
- `tensorflow/lite/ios/hide_xcframework_symbols_with_allowlist.sh` -> **100.0%** Exposure
- `tensorflow/lite/java/demo/gradlew` -> **100.0%** Exposure
- `tensorflow/lite/java/ovic/demo/gradlew` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `69` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `93067` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tensorflow/python/distribute/coordinator/cluster_coordinator.py` (PYTHON) -> Cumulative Risk: **896.72**
- **Archetype:** `file_cluster_4` (Distance: 13.289 IQR)
- **Magnitude:** 2609.04 | **LOC:** 1853 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_raise_if_error` (Impact: 690.7), `__init__` (Impact: 622.5), `_log_ps_failure_and_raise` (Impact: 349.4)

### 2. `tensorflow/python/framework/stack.py` (PYTHON) -> Cumulative Risk: **887.6**
- **Archetype:** `file_cluster_13` (Distance: 12.49 IQR)
- **Magnitude:** 119.68 | **LOC:** 138 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9999%), Tech Debt (99.9955%), Documentation (99.989%)
- **Heaviest Functions:** `get_controller` (Impact: 70.7), `get_default` (Impact: 5.3), `__init__` (Impact: 3.7)

### 3. `tensorflow/python/distribute/coordinator/watchdog.py` (PYTHON) -> Cumulative Risk: **865.12**
- **Archetype:** `file_cluster_13` (Distance: 12.657 IQR)
- **Magnitude:** 82.98 | **LOC:** 64 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_watchdog_function` (Impact: 25.0), `__init__` (Impact: 20.8), `report_closure_done` (Impact: 3.6)

### 4. `tensorflow/python/summary/writer/event_file_writer.py` (PYTHON) -> Cumulative Risk: **840.88**
- **Archetype:** `file_cluster_4` (Distance: 12.848 IQR)
- **Magnitude:** 228.66 | **LOC:** 300 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `run` (Impact: 29.1), `put` (Impact: 21.4), `__init__` (Impact: 12.1)

### 5. `tensorflow/python/profiler/profile_context.py` (PYTHON) -> Cumulative Risk: **838.62**
- **Archetype:** `file_cluster_13` (Distance: 11.937 IQR)
- **Magnitude:** 505.06 | **LOC:** 357 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9971%)
- **Heaviest Functions:** `_should_trace` (Impact: 135.4), `_profiled_run` (Impact: 113.5), `__enter__` (Impact: 61.8)

### 6. `tensorflow/lite/profiling/memory_usage_monitor.cc` (CPP) -> Cumulative Risk: **836.2**
- **Archetype:** `file_cluster_13` (Distance: 11.868 IQR)
- **Magnitude:** 110.56 | **LOC:** 104 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9436%)
- **Heaviest Functions:** `MemoryUsageMonitor::Start` (Impact: 32.9), `MemoryUsageMonitor::MemoryUsageMonitor` (Impact: 18.8), `MemoryUsageMonitor::Stop` (Impact: 10.8)

### 7. `tensorflow/lite/delegates/gpu/gl/api.cc` (CPP) -> Cumulative Risk: **833.62**
- **Archetype:** `file_cluster_13` (Distance: 13.628 IQR)
- **Magnitude:** 549.44 | **LOC:** 424 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `NewRun` (Impact: 72.1), `Execute` (Impact: 67.5), `Serialize` (Impact: 37.0)

### 8. `tensorflow/python/distribute/ps_values.py` (PYTHON) -> Cumulative Risk: **832.25**
- **Archetype:** `file_cluster_13` (Distance: 11.992 IQR)
- **Magnitude:** 925.92 | **LOC:** 964 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_assign_func` (Impact: 58.1), `__setattr__` (Impact: 57.2), `_maybe_build_distributed_table` (Impact: 49.1)

### 9. `tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py` (PYTHON) -> Cumulative Risk: **825.43**
- **Archetype:** `file_cluster_13` (Distance: 11.209 IQR)
- **Magnitude:** 221.88 | **LOC:** 208 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `cluster_spec` (Impact: 92.6), `__init__` (Impact: 71.3), `task_type` (Impact: 5.4)

### 10. `tensorflow/python/ops/summary_ops_v2.py` (PYTHON) -> Cumulative Risk: **822.87**
- **Archetype:** `file_cluster_13` (Distance: 11.363 IQR)
- **Magnitude:** 1600.14 | **LOC:** 1494 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `flush` (Impact: 617.7), `write_raw_pb` (Impact: 155.7), `write` (Impact: 131.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.348 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.649 IQR)
- **Top Global Matches:** file_cluster_8: 14.348, file_cluster_7: 14.757, file_cluster_13: 14.805
- **Magnitude:** 11297.04 | **LOC:** 8130 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 367
- **Risk Profile:** Cognitive Load (74.9639%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `Run` (Impact: 579.7 | O(N^6) | DB: 139)
    * *Intent:* // Just use C model code for case of padding. Optimized versions merge the // modifications therein ...
  * `PackMacroBlockIntrinsics` (Impact: 528.8 | O(N^6) | DB: 205)
  * `PackMacroBlockIntrinsics` (Impact: 471.9 | O(N^6) | DB: 115)
  * `Run` (Impact: 265.0 | O(N^6) | DB: 105)
  * `Run` (Impact: 262.0 | O(N^6) | DB: 88)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 269`, `args: 185`, `func_start: 80`, `class_start: 24`
* *Risk/State:* `high_risk_execution: 102`, `state_mutation: 5820`, `fragile_debt: 9`, `duplicate_logic: 74`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 698`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` cpu_check.h, depthwiseconv_uint8_3x3_filter.h, depthwiseconv_uint8.h, types.h, depthwiseconv_uint8.h, compatibility.h, algorithm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.703 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.701 IQR)
- **Top Global Matches:** file_cluster_8: 14.703, file_cluster_13: 14.883, file_cluster_11: 14.924
- **Magnitude:** 10845.86 | **LOC:** 8165 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 613
- **Risk Profile:** Cognitive Load (71.6141%), Tech Debt (81.5361%)
**Top Internal Functions/Classes:**
  * `LogSoftmax` (Impact: 1883.5 | O(2^N) | DB: 613)
  * `AveragePool` (Impact: 332.7 | O(2^N) | DB: 77)
    * *Intent:* // In Tensorflow, the dimensions are canonically named (batch_number, row, // col, channel), with ex...
  * `ShuffledFullyConnectedWorkerImpl` (Impact: 326.9 | O(N^6) | DB: 133)
  * `Conv` (Impact: 307.6 | O(2^N) | DB: 52)
  * `Conv3D` (Impact: 306.8 | O(2^N) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 441`, `args: 214`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 4122`, `dead_code: 5`, `planned_debt: 23`, `fragile_debt: 7`, `duplicate_logic: 32`
* *Architecture:* `api: 8`, `import: 41`
* *Defense:* `safety: 3`, `immutability_locks: 1089`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Accelerate.h, limits, type_traits, im2col_utils.h, macros.h, stdint.h, types.h, memory...
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `tensorflow/python/ops/nn_ops.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.135 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.013 IQR)
- **Top Global Matches:** file_cluster_8: 11.135, file_cluster_0: 11.21, file_cluster_7: 11.331
- **Magnitude:** 9905.16 | **LOC:** 6703 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (10.3542%), Tech Debt (21.8586%)
**Top Internal Functions/Classes:**
  * `pool` (Impact: 7486.3 | O(2^N) | DB: 4)
  * `convolution_internal` (Impact: 913.3 | O(2^N))
  * `__init__` (Impact: 370.6 | O(N^6) | DB: 14)
  * `__init__` (Impact: 276.5 | O(N^6) | DB: 11)
  * `__init__` (Impact: 194.7 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 352`, `args: 113`, `func_start: 112`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 95`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 86`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 37`, `doc: 186`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` tensorflow.python.eager, numpy, tensorflow.python.util.deprecation, tensorflow.python.platform, tensorflow.python.util.tf_export, tensorflow, numbers, tensorflow.python.ops.gen_nn_ops...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.06 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.424 IQR)
- **Top Global Matches:** file_cluster_8: 15.06, file_cluster_13: 15.352, file_cluster_11: 15.425
- **Magnitude:** 8104.56 | **LOC:** 2055 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 497
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (47.6655%)
**Top Internal Functions/Classes:**
  * `ConvGeneric::GenerateConv` (Impact: 1788.7 | O(N^6) | DB: 497)
  * `ConvGeneric::GuessBestParams` (Impact: 1549.8 | O(N^5) | DB: 216)
  * `GetConvParamsForA7A8` (Impact: 306.9 | O(N^6) | DB: 65)
  * `GetConvParamsForA9AndHigher` (Impact: 270.0 | O(N^6) | DB: 62)
  * `ConvGeneric::GenerateCode` (Impact: 157.1 | O(N^6) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 66`, `args: 147`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `state_mutation: 3186`, `duplicate_logic: 13`, `orphaned_logic: 14`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 249`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` utility, work_group_picking.h, shape.h, substitute.h, data_type.h, conv_generic.h, status.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/keras/backend.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.394 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_0: 12.394, file_cluster_13: 12.584, file_cluster_8: 12.813
- **Magnitude:** 6958.72 | **LOC:** 6509 | **CtrlFlow:** 49.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (19.9941%), Tech Debt (31.6738%)
**Top Internal Functions/Classes:**
  * `_assert_same_graph` (Impact: 2966.0 | O(2^N) | DB: 21)
  * `__init__` (Impact: 2786.6 | O(N^6) | DB: 49)
  * `learning_phase_scope` (Impact: 52.6 | O(2^N))
  * `batch_set_value` (Impact: 44.9 | O(N^4) | DB: 1)
  * `deprecated_internal_learning_phase_scope` (Impact: 38.0 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 684`, `args: 226`, `func_start: 224`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 211`, `dead_code: 7`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 3`, `orphaned_logic: 18`
* *Architecture:* `io: 15`, `api: 180`, `concurrency: 8`, `import: 70`
* *Defense:* `safety: 111`, `doc: 392`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` tensorflow.python.platform, tensorflow.python.keras.distribute, numpy, tensorflow, os, threading, tensorflow.python.framework, tensorflow.core.protobuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/legacy_optimized_ops.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.289 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_8: 13.289, file_cluster_13: 13.673, file_cluster_11: 13.749
- **Magnitude:** 6551.4 | **LOC:** 5023 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 487
- **Risk Profile:** Cognitive Load (71.5995%), Tech Debt (99.972%)
**Top Internal Functions/Classes:**
  * `GEMVForLstmCell` (Impact: 1705.3 | O(2^N) | DB: 487)
  * `Softmax` (Impact: 233.1 | O(2^N) | DB: 100)
  * `DepthwiseConv` (Impact: 165.1 | O(2^N) | DB: 24)
  * `BroadcastAddFivefold` (Impact: 149.2 | O(2^N) | DB: 22)
  * `Tanh` (Impact: 144.6 | O(2^N) | DB: 67)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 442`, `args: 169`, `func_start: 148`, `class_start: 4`
* *Risk/State:* `state_mutation: 2095`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 3`, `duplicate_logic: 86`, `orphaned_logic: 9`
* *Architecture:* `import: 13`
* *Defense:* `safety: 15`, `immutability_locks: 976`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` cpu_check.h, stdint.h, types.h, types.h, fully_connected.h, gemmlowp.h, depthwiseconv_multithread.h, depthwise_conv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/delegates/xnnpack/xnnpack_delegate.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.5 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.39 IQR)
- **Top Global Matches:** file_cluster_8: 14.5, file_cluster_13: 14.873, file_cluster_7: 14.89
- **Magnitude:** 6443.74 | **LOC:** 7409 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 297
- **Risk Profile:** Cognitive Load (91.473%), Tech Debt (14.8142%)
**Top Internal Functions/Classes:**
  * `Invoke` (Impact: 1733.0 | O(N^6) | DB: 297)
    * *Intent:* #endif
  * `Delegate::PrepareOpsToDelegate` (Impact: 636.9 | O(N^6) | DB: 146)
  * `SetVarHandle` (Impact: 474.4 | O(N^6) | DB: 82)
  * `GetXNNPackDatatype` (Impact: 416.0 | O(N^6) | DB: 23)
  * `VisitFullyConnectedNode` (Impact: 349.8 | O(N^6) | DB: 83)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 250`, `args: 241`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 1995`, `planned_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 14`
* *Defense:* `safety: 4`, `sync_locks: 7`, `immutability_locks: 309`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` cstdlib, functional, limits, array.h, cinttypes, builtin_op_data.h, profiler.h, vector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/array_ops.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.05 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.469 IQR)
- **Top Global Matches:** file_cluster_0: 11.05, file_cluster_8: 11.208, file_cluster_13: 11.324
- **Magnitude:** 6209.54 | **LOC:** 6815 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.1204%), Tech Debt (11.8429%)
**Top Internal Functions/Classes:**
  * `split` (Impact: 4494.4 | O(2^N) | DB: 6)
  * `get_positive_axis` (Impact: 479.3 | O(2^N))
  * `_autopacking_helper` (Impact: 239.9 | O(2^N) | DB: 5)
  * `boolean_mask` (Impact: 82.9 | O(2^N))
  * `strided_slice` (Impact: 72.0 | O(2^N))
    * *Intent:* * Add an outer "batch" dimension to a single element. * Align axes for broadcasting. * To add an inn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 385`, `args: 115`, `func_start: 115`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 39`, `dead_code: 1`, `planned_debt: 17`
* *Architecture:* `api: 98`, `concurrency: 11`, `import: 34`
* *Defense:* `safety: 51`, `doc: 200`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tensorflow.python.eager, tensorflow.core.config, tensorflow.python.util.tf_export, numbers, tensorflow.python.types, tensorflow.python.framework, tensorflow.python.ops, tensorflow.python.util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/tf2tensorrt/convert/convert_nodes.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.799 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.256 IQR)
- **Top Global Matches:** file_cluster_8: 14.799, file_cluster_13: 14.853, file_cluster_11: 14.949
- **Magnitude:** 5774.6 | **LOC:** 6266 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 397
- **Risk Profile:** Cognitive Load (91.8231%), Tech Debt (40.1312%)
**Top Internal Functions/Classes:**
  * `ConvertTranspose` (Impact: 1731.3 | O(N^6) | DB: 397)
  * `TrtNodeValidator::ConvertToTensorOrWeigh` (Impact: 579.0 | O(N^6) | DB: 70)
    * *Intent:* // Remove batch dimension if it is implicit.
  * `ConvertConv2DHelper` (Impact: 302.1 | O(N^6) | DB: 42)
  * `GetTrtBroadcastShape` (Impact: 172.0 | O(N^6) | DB: 29)
  * `ConvertResize` (Impact: 168.6 | O(N^6) | DB: 34)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 530`, `structural_boundaries: 316`, `args: 257`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `state_mutation: 2044`, `dead_code: 3`, `planned_debt: 17`, `duplicate_logic: 2`, `orphaned_logic: 21`
* *Architecture:* `import: 61`
* *Defense:* `safety: 13`, `test: 1`, `sync_locks: 1`, `immutability_locks: 242`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` numbers.h, flat_hash_set.h, graph.h, graph_constructor.h, vector, grappler_item.h, memory, tensor_coding.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/eager/pywrap_tfe_src.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.987 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.395 IQR)
- **Top Global Matches:** file_cluster_8: 13.987, file_cluster_13: 14.008, file_cluster_11: 14.23
- **Magnitude:** 5700.7 | **LOC:** 4259 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 286
- **Risk Profile:** Cognitive Load (91.7236%), Tech Debt (19.1696%)
**Top Internal Functions/Classes:**
  * `MaybeRaiseExceptionFromTFStatus` (Impact: 3108.3 | O(2^N) | DB: 286)
  * `SetOpAttrList` (Impact: 394.3 | O(N^6) | DB: 31)
    * *Intent:* *value = absl::string_view(buf, size);
  * `SetOpAttrScalar` (Impact: 372.3 | O(N^6) | DB: 14)
  * `GetEagerContextThreadLocalData` (Impact: 123.0 | O(2^N) | DB: 9)
    * *Intent:* // We need to keep a reference to the weakref active if we want our callback
  * `SetOpAttrs` (Impact: 104.4 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 335`, `args: 264`, `func_start: 107`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1150`, `dead_code: 2`, `planned_debt: 6`, `orphaned_logic: 11`
* *Architecture:* `api: 7`, `import: 61`
* *Defense:* `safety: 15`, `sync_locks: 2`, `immutability_locks: 91`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` functional, limits, status.h, tf_status.h, tfe_context_internal.h, flat_hash_map.h, inlined_vector.h, status.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/ragged/dynamic_ragged_shape.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.946 IQR)
- **Top Global Matches:** file_cluster_8: 11.756, file_cluster_13: 11.881, file_cluster_16: 11.909
- **Magnitude:** 5476.98 | **LOC:** 3293 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (20.857%), Tech Debt (23.1119%)
**Top Internal Functions/Classes:**
  * `is_uniform` (Impact: 4166.1 | O(2^N) | DB: 18)
  * `__init__` (Impact: 263.2 | O(N^6) | DB: 9)
    * *Intent:* * `inner_shape`: An integer vector giving the shape of a dense tensor. * `row_partitions`: A list of...
  * `from_lengths` (Impact: 234.1 | O(N^5) | DB: 5)
  * `_slice_shape` (Impact: 212.5 | O(2^N))
  * `__getitem__` (Impact: 77.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 481`, `args: 142`, `func_start: 142`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 105`, `dead_code: 2`, `planned_debt: 17`, `orphaned_logic: 7`
* *Architecture:* `api: 70`, `concurrency: 13`, `import: 22`
* *Defense:* `safety: 75`, `doc: 208`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tensorflow.python.ops.ragged, typing, tensorflow.python.util.tf_export, tensorflow.python.ops.ragged.row_partition, tensorflow.python.types, tensorflow.python.framework, abc, tensorflow.python.ops...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/variable_scope.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.855 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.84 IQR)
- **Top Global Matches:** file_cluster_13: 11.855, file_cluster_8: 11.879, file_cluster_0: 11.917
- **Magnitude:** 5218.9 | **LOC:** 2786 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (27.8853%), Tech Debt (48.8881%)
**Top Internal Functions/Classes:**
  * `get_variable` (Impact: 2928.1 | O(2^N) | DB: 27)
  * `_get_partitioned_variable` (Impact: 1242.7 | O(N^6) | DB: 1)
  * `get_variable` (Impact: 395.7 | O(N^6))
  * `single_slice_dim` (Impact: 159.3 | O(2^N) | DB: 4)
  * `__init__` (Impact: 78.4 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 222`, `args: 90`, `func_start: 83`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 171`, `dead_code: 3`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 6`, `api: 60`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 44`, `doc: 112`, `test: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tensorflow.python.eager, sys, tensorflow.python.platform, tensorflow.python.util.tf_export, tensorflow.python.client, threading, traceback, tensorflow.python.types...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/python/keras/engine/training.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.942 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.718 IQR)
- **Top Global Matches:** file_cluster_13: 11.942, file_cluster_8: 12.188, file_cluster_0: 12.272
- **Magnitude:** 5172.44 | **LOC:** 3002 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (29.3986%), Tech Debt (20.9608%)
**Top Internal Functions/Classes:**
  * `evaluate` (Impact: 2199.8 | O(2^N) | DB: 18)
  * `fit` (Impact: 580.7 | O(2^N) | DB: 5)
  * `build` (Impact: 428.2 | O(2^N))
    * *Intent:* # stop_training is used by callback to stop training when error happens
  * `load_weights` (Impact: 362.8 | O(2^N))
  * `_assert_weights_created` (Impact: 187.2 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 363`, `args: 102`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 177`, `dead_code: 2`, `planned_debt: 11`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 70`, `concurrency: 3`, `import: 71`
* *Defense:* `safety: 45`, `doc: 126`, `test: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` tensorflow.python.checkpoint, tensorflow.python.platform, keras.models, tensorflow.python.data.ops, tensorflow.python.keras.utils.io_utils, tensorflow.python.keras.utils.mode_keys, tensorflow, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/lite/delegates/gpu/common/model_builder.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.763 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.721 IQR)
- **Top Global Matches:** file_cluster_8: 14.763, file_cluster_13: 14.837, file_cluster_11: 14.961
- **Magnitude:** 5164.74 | **LOC:** 3661 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (94.8994%), Tech Debt (99.9846%)
**Top Internal Functions/Classes:**
  * `NewOperationParser` (Impact: 289.4 | O(N^2) | DB: 4)
  * `Parse` (Impact: 176.5 | O(N^6) | DB: 25)
  * `ParseInputsWithConstTensorImpl` (Impact: 175.6 | O(N^6) | DB: 34)
  * `Parse` (Impact: 159.2 | O(N^5) | DB: 40)
  * `Parse` (Impact: 144.0 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 483`, `structural_boundaries: 363`, `args: 337`, `func_start: 110`, `class_start: 36`
* *Risk/State:* `state_mutation: 1758`, `dead_code: 3`, `planned_debt: 11`, `duplicate_logic: 72`, `orphaned_logic: 4`
* *Architecture:* `api: 36`, `import: 43`
* *Defense:* `safety: 71`, `immutability_locks: 386`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` model_transformer.h, operation_parser.h, flat_hash_set.h, operations.h, model_transformations.h, gpu_compatibility.h, flat_hash_map.h, model_builder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/keras/engine/training_v1.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.353 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.772 IQR)
- **Top Global Matches:** file_cluster_13: 12.353, file_cluster_0: 12.492, file_cluster_8: 12.512
- **Magnitude:** 4890.26 | **LOC:** 3215 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (36.279%), Tech Debt (94.6657%)
**Top Internal Functions/Classes:**
  * `_process_target_tensor_for_compile` (Impact: 1356.0 | O(N^6) | DB: 26)
  * `compile` (Impact: 938.6 | O(2^N) | DB: 30)
  * `_compile_from_inputs` (Impact: 297.2 | O(N^6) | DB: 10)
  * `train_on_batch` (Impact: 262.0 | O(2^N))
  * `test_on_batch` (Impact: 224.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 358`, `args: 115`, `func_start: 115`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 248`, `dead_code: 2`, `planned_debt: 14`, `duplicate_logic: 18`, `orphaned_logic: 8`
* *Architecture:* `api: 51`, `import: 51`
* *Defense:* `safety: 71`, `doc: 118`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` tensorflow.python.platform, tensorflow.python.data.ops, tensorflow.python.keras.utils.mode_keys, tensorflow.python.keras.distribute, numpy, tensorflow, tensorflow.python.framework, tensorflow.python.keras.saving.saved_model...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/parallel_for/pfor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.536 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.348 IQR)
- **Top Global Matches:** file_cluster_0: 11.536, file_cluster_8: 11.847, file_cluster_13: 11.876
- **Magnitude:** 4875.12 | **LOC:** 5227 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (16.8148%), Tech Debt (51.8584%)
**Top Internal Functions/Classes:**
  * `_convert_reduction` (Impact: 1042.5 | O(2^N) | DB: 5)
  * `__str__` (Impact: 451.0 | O(N^6) | DB: 18)
  * `_stack_handle_inside_pfor` (Impact: 299.8 | O(2^N) | DB: 1)
  * `reduce` (Impact: 156.1 | O(2^N) | DB: 3)
    * *Intent:* # We assume that shape input is loop invariant. Call to `unstacked_input` # asserts that and returns...
  * `__call__` (Impact: 153.3 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 788`, `args: 259`, `func_start: 249`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 231`, `dead_code: 4`, `planned_debt: 49`, `fragile_debt: 5`, `duplicate_logic: 11`
* *Architecture:* `io: 1`, `api: 174`, `concurrency: 14`, `import: 56`
* *Defense:* `safety: 129`, `doc: 148`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tensorflow.python.eager, sys, typing, tensorflow.core.framework, tensorflow.python.platform, collections, traceback, tensorflow.compiler.tf2xla.python...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/mlir/lite/transforms/optimize_pass.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.096 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.459 IQR)
- **Top Global Matches:** file_cluster_13: 14.096, file_cluster_8: 14.109, file_cluster_11: 14.323
- **Magnitude:** 4864.04 | **LOC:** 3364 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 240
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (61.7114%)
**Top Internal Functions/Classes:**
  * `matchAndRewrite` (Impact: 2470.4 | O(2^N) | DB: 240)
  * `GetBiasIn1D` (Impact: 207.8 | O(2^N) | DB: 14)
  * `matchAndRewrite` (Impact: 162.9 | O(N^6) | DB: 31)
  * `matchAndRewrite` (Impact: 107.6 | O(N^6) | DB: 31)
  * `matchAndRewrite` (Impact: 100.2 | O(N^6) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 488`, `args: 75`, `func_start: 53`, `class_start: 17`
* *Risk/State:* `state_mutation: 1175`, `dead_code: 3`, `planned_debt: 4`, `duplicate_logic: 8`, `orphaned_logic: 9`
* *Architecture:* `import: 48`
* *Defense:* `safety: 20`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Matchers.h, functional, LLVM.h, SmallSet.h, LogicalResult.h, validators.h, Builders.h, generated_optimize.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_3x3_filter.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.272 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.075 IQR)
- **Top Global Matches:** file_cluster_8: 12.272, file_cluster_7: 12.803, file_cluster_12: 13.005
- **Magnitude:** 4792.62 | **LOC:** 13443 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 205
- **Risk Profile:** Cognitive Load (37.6984%), Tech Debt (28.5748%)
**Top Internal Functions/Classes:**
  * `DepthwiseConvDotProduct3x3Impl` (Impact: 683.0 | O(N^6) | DB: 148)
    * *Intent:* // and the special code is not executed. // // Example: // Suppose that we characterize a size s as ...
  * `PackMacroBlockNeon` (Impact: 530.0 | O(N^6) | DB: 205)
  * `PackMacroBlockNeon` (Impact: 473.5 | O(N^6) | DB: 115)
  * `DepthwiseConv3x3Filter` (Impact: 300.0 | O(N^6) | DB: 90)
  * `PackMacroBlockNeon` (Impact: 232.9 | O(N^6) | DB: 58)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 183`, `args: 292`, `func_start: 53`, `class_start: 30`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 1820`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 48`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 50`, `immutability_locks: 376`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cpu_check.h, instrumentation.h, types.h, stddef.h, depthwiseconv_uint8.h, depthwiseconv_3x3_filter_common.h, memory, algorithm
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tensorflow/core/transforms/constant_folding/pass.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.612 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.449 IQR)
- **Top Global Matches:** file_cluster_13: 14.612, file_cluster_11: 14.702, file_cluster_8: 14.736
- **Magnitude:** 4676.06 | **LOC:** 3738 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 140
- **Risk Profile:** Cognitive Load (94.178%), Tech Debt (97.4586%)
**Top Internal Functions/Classes:**
  * `matchAndRewrite` (Impact: 1399.1 | O(2^N) | DB: 140)
  * `matchAndRewrite` (Impact: 228.8 | O(N^6) | DB: 39)
  * `matchAndRewrite` (Impact: 217.3 | O(N^6) | DB: 31)
  * `matchAndRewrite` (Impact: 197.2 | O(N^6) | DB: 22)
  * `matchAndRewrite` (Impact: 174.5 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 369`, `args: 168`, `func_start: 70`, `class_start: 36`
* *Risk/State:* `state_mutation: 1149`, `dead_code: 1`, `planned_debt: 13`, `duplicate_logic: 20`, `orphaned_logic: 5`
* *Architecture:* `api: 28`, `import: 59`
* *Defense:* `safety: 27`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` resource_mgr.h, LLVM.h, device_name_utils.h, flat_hash_set.h, LogicalResult.h, type_traits, utils.h, Builders.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/framework/test_util.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.664 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.742 IQR)
- **Top Global Matches:** file_cluster_13: 12.664, file_cluster_16: 12.701, file_cluster_0: 12.827
- **Magnitude:** 4589.04 | **LOC:** 4313 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (21.619%), Tech Debt (94.7943%)
**Top Internal Functions/Classes:**
  * `tearDown` (Impact: 2077.2 | O(2^N) | DB: 37)
  * `run_v2` (Impact: 358.5 | O(2^N) | DB: 3)
  * `pick_unused_port` (Impact: 337.0 | O(2^N) | DB: 8)
  * `assert_no_new_tensors` (Impact: 301.4 | O(N^6) | DB: 1)
  * `assert_no_garbage_created` (Impact: 101.5 | O(N^6))
    * *Intent:* # Make sure our collection checks don't show up as leaked memory by
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 573`, `structural_boundaries: 710`, `args: 232`, `func_start: 230`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 152`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 2`, `duplicate_logic: 11`, `orphaned_logic: 42`
* *Architecture:* `io: 17`, `api: 202`, `concurrency: 13`, `import: 86`
* *Defense:* `safety: 126`, `doc: 276`, `test: 25`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` unittest, tensorflow.python.platform, time, collections.abc, numpy, math, os, tensorflow.core.config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/toco/export_tensorflow.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.275 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.115 IQR)
- **Top Global Matches:** file_cluster_8: 14.275, file_cluster_13: 14.604, file_cluster_7: 14.698
- **Magnitude:** 4575.34 | **LOC:** 2564 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (89.4725%), Tech Debt (32.624%)
**Top Internal Functions/Classes:**
  * `ConvertOperator` (Impact: 1233.0 | O(N^6) | DB: 82)
  * `AddPlaceholder` (Impact: 115.7 | O(N^5) | DB: 2)
  * `ExportTensorFlowGraphDefImplementation` (Impact: 105.1 | O(N^6) | DB: 9)
  * `GetTensorFlowDataType` (Impact: 86.4 | O(N^6) | DB: 1)
  * `ConvertConvOperator` (Impact: 66.3 | O(N^6) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 236`, `args: 282`, `func_start: 103`, `class_start: 1`
* *Risk/State:* `state_mutation: 1504`, `planned_debt: 5`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `import: 22`
* *Defense:* `test: 34`, `immutability_locks: 418`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` map.h, vector, memory, attr_value.pb.h, model.h, tensor.pb.h, unordered_map, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/grappler/optimizers/remapper.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.286 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.482 IQR)
- **Top Global Matches:** file_cluster_8: 15.286, file_cluster_13: 15.304, file_cluster_11: 15.4
- **Magnitude:** 4571.52 | **LOC:** 5411 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 185
- **Risk Profile:** Cognitive Load (94.8931%), Tech Debt (47.6375%)
**Top Internal Functions/Classes:**
  * `Remapper::Optimize` (Impact: 593.1 | O(N^6) | DB: 185)
  * `RequiresInferredShapes` (Impact: 399.4 | O(N^6) | DB: 65)
  * `FindSigmoidAndMul` (Impact: 376.5 | O(N^6) | DB: 49)
  * `IsBiasSemanticAdd` (Impact: 226.8 | O(N^5) | DB: 43)
  * `IsGpuCompatible` (Impact: 213.6 | O(N^6) | DB: 60)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 243`, `args: 136`, `func_start: 48`, `class_start: 14`
* *Risk/State:* `state_mutation: 1836`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 3`, `orphaned_logic: 9`
* *Architecture:* `import: 31`
* *Defense:* `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` cstdlib, symbolic_shapes.h, flat_hash_set.h, remapper.h, rewriter_config.pb.h, grappler_item.h, vector, pattern_utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/control_flow_ops.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.297 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.714 IQR)
- **Top Global Matches:** file_cluster_13: 12.297, file_cluster_8: 12.348, file_cluster_0: 12.406
- **Magnitude:** 4530.76 | **LOC:** 2257 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (32.8765%), Tech Debt (11.2421%)
**Top Internal Functions/Classes:**
  * `_shape_invariant_to_type_spec` (Impact: 3656.0 | O(2^N) | DB: 80)
  * `_Enter` (Impact: 154.2 | O(2^N))
  * `merge` (Impact: 100.7 | O(2^N))
  * `_Identity` (Impact: 73.6 | O(2^N))
    * *Intent:* # pylint: disable=protected-access
  * `exit` (Impact: 73.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 319`, `args: 107`, `func_start: 105`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 184`, `dead_code: 1`, `planned_debt: 10`
* *Architecture:* `api: 75`, `import: 25`
* *Defense:* `safety: 57`, `doc: 140`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tensorflow.python.eager, tensorflow.core.framework, tensorflow.python.util.tf_export, tensorflow.python.framework, abc, tensorflow.core.protobuf, tensorflow.python.ops, tensorflow.python.util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/mlir/tosa/transforms/legalize_tfl.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.115 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.08 IQR)
- **Top Global Matches:** file_cluster_8: 14.115, file_cluster_13: 14.33, file_cluster_11: 14.531
- **Magnitude:** 4475.84 | **LOC:** 5174 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 400
- **Risk Profile:** Cognitive Load (94.9871%), Tech Debt (67.6469%)
**Top Internal Functions/Classes:**
  * `ConvertTFLMaxPool2DOp::matchAndRewrite` (Impact: 1031.9 | O(N^6) | DB: 400)
  * `matchAndRewriteAddSub` (Impact: 169.7 | O(N^6) | DB: 49)
  * `prepareMatchAndRewriteComparison` (Impact: 88.8 | O(N^6) | DB: 19)
  * `ConvertTFLLogOp::matchAndRewrite` (Impact: 76.0 | O(N^6) | DB: 13)
  * `ConvertTFLExpOp::matchAndRewrite` (Impact: 63.4 | O(N^6) | DB: 11)
    * *Intent:* // To perform an atan2 operation we make use of an atan lookup table,
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 568`, `args: 346`, `func_start: 96`, `class_start: 3`
* *Risk/State:* `state_mutation: 1929`, `planned_debt: 2`, `orphaned_logic: 62`
* *Architecture:* `api: 1`, `import: 44`
* *Defense:* `safety: 57`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Matchers.h, passes.h.inc, limits, LLVM.h, passes.h, LogicalResult.h, cfloat, Block.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/toco/import_tensorflow.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.29 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.67 IQR)
- **Top Global Matches:** file_cluster_8: 14.29, file_cluster_13: 14.411, file_cluster_11: 14.517
- **Magnitude:** 4432.58 | **LOC:** 2822 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 182
- **Risk Profile:** Cognitive Load (86.6816%), Tech Debt (22.7977%)
**Top Internal Functions/Classes:**
  * `ImportShape` (Impact: 893.1 | O(2^N) | DB: 182)
  * `ConvertOperatorSpecialCasedAsRNNBackEdge` (Impact: 318.2 | O(N^6) | DB: 72)
  * `ConvertConstOperator` (Impact: 167.1 | O(N^6) | DB: 34)
  * `ConvertConvOperator` (Impact: 97.8 | O(N^6) | DB: 35)
  * `ConditionallyConvertConstOperator` (Impact: 95.3 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 395`, `args: 282`, `func_start: 131`, `class_start: 8`
* *Risk/State:* `state_mutation: 1719`, `dead_code: 2`, `planned_debt: 11`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `import: 34`
* *Defense:* `safety: 6`, `test: 42`, `immutability_locks: 372`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` map.h, function.h, session_options.h, graph_constructor.h, vector, memory, attr_value.pb.h, model.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `tensorflow/python/tools/api/generator/api_init_files.bzl` (PYTHON) | **Drift Ratio: 1.57x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.79 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.952 IQR)
- `tensorflow/python/tools/api/generator/api_init_files_v1.bzl` (PYTHON) | **Drift Ratio: 1.53x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.818 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.855 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tensorflow/lite/java/src/main/java/org/tensorflow/lite/InterpreterFactoryImpl.java` (JAVA) | Magnitude: 28.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 19, args: 9, func_start: 7
- `tensorflow/python/training/session_run_hook.py` (PYTHON) | Magnitude: 52.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, doc: 30, structural_boundaries: 27, api: 20
- `tensorflow/java/src/test/java/org/tensorflow/EagerSessionTest.java` (JAVA) | Magnitude: 160.54 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 59, func_start: 46, branch: 21
- `tensorflow/python/ops/variables.py` (PYTHON) | Magnitude: 1177.0 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 637, structural_boundaries: 280, doc: 170, branch: 150
- `tensorflow/python/framework/memory_checker.py` (PYTHON) | Magnitude: 34.84 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 19, doc: 14, encapsulation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tensorflow/core/graph/optimizer_cse.cc` (CPP) | Magnitude: 303.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 134, state_mutation: 116, pointers: 55, branch: 35
- `tensorflow/core/kernels/fake_quant_ops_functor.h` (CPP) | Magnitude: 305.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 263, indent_spaces: 166, structural_boundaries: 78, immutability_locks: 54
- `tensorflow/core/kernels/matmul_op_impl.h` (CPP) | Magnitude: 3249.88 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 950, indent_spaces: 814, branch: 217, structural_boundaries: 207
- `tensorflow/core/kernels/debug_ops.h` (CPP) | Magnitude: 1500.54 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 666, state_mutation: 651, pointers: 232, structural_boundaries: 144
- `tensorflow/tools/ci_build/builds/pip_new.sh` (SHELL) | Magnitude: 1.0 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 359, branch: 337, state_mutation: 275, reflection_metaprogramming: 164

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tensorflow/tools/ci_build/builds/run_pip_tests.sh` (SHELL) | Magnitude: 0.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 114, branch: 83, indent_spaces: 54, reflection_metaprogramming: 38
- `tensorflow/tools/lib_package/libtensorflow_java_test.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 19, reflection_metaprogramming: 17, safety: 8, branch: 6
- `tensorflow/go/tensor.go` (GO) | Magnitude: 328.82 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 188, state_mutation: 146, api: 49, encapsulation: 46
- `tensorflow/tools/ci_build/builds/test_tutorials.sh` (SHELL) | Magnitude: 0.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 107, branch: 102, reflection_metaprogramming: 82, state_mutation: 72
- `tensorflow/tools/ci_build/linux/gpu/run_mkl.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 22, indent_spaces: 22, branch: 14, reflection_metaprogramming: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tensorflow/core/kernels/data/finalize_dataset_op.h` (CPP) | Magnitude: 16.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, immutability_locks: 15, structural_boundaries: 9, state_mutation: 6
- `tensorflow/core/kernels/edit_distance_op.cc` (CPP) | Magnitude: 513.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 221, state_mutation: 196, branch: 39, pointers: 39
- `tensorflow/core/tpu/graph_rewrite/configure_tpu_embedding_rewrite_pass.cc` (CPP) | Magnitude: 346.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 209, state_mutation: 98, pointers: 67, immutability_locks: 37
- `tensorflow/lite/delegates/xnnpack/quantized_resize_bilinear_tester.h` (CPP) | Magnitude: 81.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 50, structural_boundaries: 47, func_start: 22
- `tensorflow/lite/kernels/internal/reference/floor_div.h` (CPP) | Magnitude: 7.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, explicit_casts: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tensorflow/go/operation.go` (GO) | Magnitude: 165.76 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 76, state_mutation: 52, structural_boundaries: 32, doc: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tensorflow/java/src/gen/resources/Tensors.java.tmpl` (JAVA) | Magnitude: 13.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, doc: 6, args: 3
- `tensorflow/lite/core/async/interop/variant.h` (CPP) | Magnitude: 46.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 44, indent_spaces: 33, state_mutation: 30, immutability_locks: 21
- `tensorflow/python/util/tf_export.py` (PYTHON) | Magnitude: 83.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, encapsulation: 53, structural_boundaries: 49, state_mutation: 36
- `tensorflow/java/src/main/java/org/tensorflow/op/core/Zeros.java` (JAVA) | Magnitude: 21.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 16, generics: 11, doc: 8
- `tensorflow/lite/delegates/gpu/common/tensor.h` (CPP) | Magnitude: 27.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 50, indent_spaces: 25, state_mutation: 22, generics: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tensorflow/python/framework/auto_control_deps_utils.py` (PYTHON) | Magnitude: 127.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 73, branch: 34, structural_boundaries: 30, doc: 14
- `tensorflow/compiler/jit/resource_operation_safety_analysis.cc` (CPP) | Magnitude: 154.98 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 41, pointers: 33, branch: 12
- `tensorflow/python/__init__.py` (PYTHON) | Magnitude: 15.16 | Delta: **0.198 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: encapsulation: 8, indent_spaces: 5, branch: 3, doc: 2
- `tensorflow/lite/tools/pip_package/Makefile` (MAKEFILE) | Magnitude: 0.07 | Delta: **0.299 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 20, ipc_rpc_bridges: 14, indent_spaces: 13, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tensorflow/tools/ci_build/osx/cpu/run_py2_cc_core.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, reflection_metaprogramming: 5, indent_spaces: 5, api: 4
- `tensorflow/java/src/main/java/org/tensorflow/EagerSession.java` (JAVA) | Magnitude: 315.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 211, structural_boundaries: 57, func_start: 48, concurrency: 37
- `tensorflow/python/util/lock_util.py` (PYTHON) | Magnitude: 70.34 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, encapsulation: 41, structural_boundaries: 15, doc: 14
- `tensorflow/python/distribute/load_context.py` (PYTHON) | Magnitude: 43.82 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, encapsulation: 16, args: 8
- `tensorflow/tools/ci_build/linux/cpu/run_cc_core.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, api: 4, reflection_metaprogramming: 4, debug_prints: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tensorflow/compiler/mlir/lite/experimental/tac/hardwares/simple_hardware.h` (CPP) | Magnitude: 18.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 6, immutability_locks: 6, indent_spaces: 6, safety: 3
- `tensorflow/core/distributed_runtime/local_master.h` (CPP) | Magnitude: 10.14 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 40, args: 15, immutability_locks: 15, safety: 14
- `tensorflow/c/experimental/filesystem/filesystem_interface.h` (CPP) | Magnitude: 16.66 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 433, indent_spaces: 67, immutability_locks: 33, pointers: 28
- `tensorflow/compiler/mlir/lite/stablehlo/transforms/legalize_hlo_conversions/conv.h` (CPP) | Magnitude: 18.2 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 6, structural_boundaries: 3, state_mutation: 3, args: 2
- `tensorflow/go/genop/generate.go` (GO) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1, sec_dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tensorflow/lite/core/c/c_api_opaque.h` (CPP) | Magnitude: 21.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 217, indent_spaces: 86, args: 42, macros: 35
- `tensorflow/compiler/mlir/lite/core/special_rules.bzl` (PYTHON) | Magnitude: 2.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1
- `tensorflow/compiler/mlir/quantization/stablehlo/internal_visibility_allowlist.bzl` (PYTHON) | Magnitude: 2.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1
- `tensorflow/compiler/mlir/quantization/tensorflow/internal_visibility_allowlist.bzl` (PYTHON) | Magnitude: 2.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1
- `tensorflow/distribute/experimental/rpc/kernels/oss/defs.bzl` (PYTHON) | Magnitude: 2.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tensorflow/lite/tools/evaluation/tasks/ios/build_evaluation_framework.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, reflection_metaprogramming: 16, safety: 6, structural_boundaries: 5
- `tensorflow/lite/testing/op_tests/split.py` (PYTHON) | Magnitude: 9.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, import: 5, doc: 4
- `tensorflow/compiler/mlir/lite/experimental/remat/rematerializer.cc` (CPP) | Magnitude: 298.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 144, indent_spaces: 99, immutability_locks: 30, branch: 27
- `tensorflow/compiler/mlir/lite/python/converter_python_api.h` (CPP) | Magnitude: 26.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 11, args: 5, import: 4
- `tensorflow/core/grappler/costs/robust_stats.h` (CPP) | Magnitude: 15.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 10, indent_spaces: 10, structural_boundaries: 9, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tensorflow/compiler/tf2tensorrt/segment/union_find.h` (CPP) | Magnitude: 86.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 55, indent_spaces: 45, structural_boundaries: 26, immutability_locks: 20
- `tensorflow/core/framework/log_memory.h` (CPP) | Magnitude: 20.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, state_mutation: 5, immutability_locks: 5
- `tensorflow/tools/ci_build/Dockerfile.rocm` (DOCKERFILE) | Magnitude: 0.03 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 27, io: 18, globals: 13
- `tensorflow/c/ops.h` (CPP) | Magnitude: 15.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 6, class_start: 4, globals: 4
- `tensorflow/tools/tf_sig_build_dockerfiles/setup.packages.sh` (SHELL) | Magnitude: 0.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, sec_dead_code: 2, safety: 1, api: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tensorflow/core/tfrt/ifrt/ifrt_serving_executable.cc` -> Churn: **91.31%** | Cog Load: 61.1023% | Debt: 33.5038%
- `tensorflow/compiler/mlir/lite/flatbuffer_export.cc` -> Churn: **82.96%** | Cog Load: 90.1848% | Debt: 63.6736%
- `tensorflow/lite/delegates/xnnpack/weight_cache.cc` -> Churn: **76.02%** | Cog Load: 64.4348% | Debt: 99.8569%
- `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` -> Churn: **71.94%** | Cog Load: 70.8487% | Debt: 99.6705%
- `tensorflow/core/tfrt/ifrt/ifrt_serving_executable.h` -> Churn: **71.94%** | Cog Load: 70.2065% | Debt: 73.1441%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tensorflow/core/transforms/constant_folding/pass.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 4676.06
- `tensorflow/core/grappler/optimizers/remapper.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 4571.52
- `tensorflow/compiler/mlir/tosa/transforms/legalize_tfl.cc` -> **deeptanshusekhri** (100.0% isolated ownership) | Magnitude: 4475.84
- `tensorflow/python/feature_column/feature_column_v2.py` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 4430.98
- `tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 4303.16

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tensorflow/core/framework/op_kernel.h` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 92.2715%)
- `tensorflow/core/framework/resource_mgr.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9993%)
- `tensorflow/core/platform/types.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.4622%)
- `tensorflow/core/framework/node_def_util.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 98.272%)
- `tensorflow/core/framework/types.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 98.9457%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tensorflow/core/platform/types.h` -> **Severity: 412.371** (Blast Radius: 34.594 * Doc Risk: 11.9203%)
- `tensorflow/core/framework/tensor_shape.h` -> **Severity: 367.136** (Blast Radius: 4.658 * Doc Risk: 78.8183%)
- `tensorflow/python/util/tf_export.py` -> **Severity: 242.211** (Blast Radius: 6.496 * Doc Risk: 37.2862%)
- `tensorflow/core/framework/types.h` -> **Severity: 233.66** (Blast Radius: 5.408 * Doc Risk: 43.2064%)
- `tensorflow/core/ir/types/dialect.h` -> **Severity: 228.958** (Blast Radius: 2.297 * Doc Risk: 99.6771%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
