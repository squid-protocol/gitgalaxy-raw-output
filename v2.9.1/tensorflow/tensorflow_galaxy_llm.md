# ARCHITECTURAL_BRIEF: tensorflow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tensorflow/tensorflow.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 20571 analyzed artifact(s), 2256008 LOC.
- **Load-bearing artifact:** `tensorflow/lite/java/src/testdata/string.bin` -- 2398 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tensorflow/compiler/mlir/tf2xla/api/v2/graph_to_tf_executor.cc` -- pulls in 117 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc` at magnitude 5198.34 (structural weight, not risk).
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
| Total Artifacts | 35746 |
| Analyzed Artifacts (Scanned) | 20571 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15175 |
| Total LOC | 2256008 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6309 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0798 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2894 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 577 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 8383 | 1328046 | 40.8% |
| PBTXT | 7587 | 472234 | 36.9% |
| PYTHON | 1785 | 308163 | 8.7% |
| MLIR | 918 | 69689 | 4.5% |
| MARKDOWN | 697 | 0 | 3.4% |
| SHELL | 198 | 9196 | 1.0% |
| PROTO | 196 | 6881 | 1.0% |
| JAVA | 175 | 20100 | 0.9% |
| BINARY_THREAT | 150 | 150 | 0.7% |
| TD | 117 | 27159 | 0.6% |
| XML | 72 | 4 | 0.4% |
| OBJECTIVE-C | 72 | 5194 | 0.4% |
| PLAINTEXT | 65 | 0 | 0.3% |
| DOCKERFILE | 34 | 1129 | 0.2% |
| JSON | 30 | 1743 | 0.1% |
| GO | 22 | 2457 | 0.1% |
| SWIFT | 18 | 1348 | 0.1% |
| BATCH | 12 | 308 | 0.1% |
| YAML | 9 | 615 | 0.0% |
| MAKEFILE | 8 | 316 | 0.0% |
| RUBY | 6 | 219 | 0.0% |
| GROOVY | 5 | 146 | 0.0% |
| M4 | 3 | 73 | 0.0% |
| PERL | 2 | 152 | 0.0% |
| CSV | 2 | 229 | 0.0% |
| C | 2 | 39 | 0.0% |
| CSHARP | 2 | 272 | 0.0% |
| HTML | 1 | 146 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.224`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.22; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 44%, Data / Markup / Trivial 19%, Large Core Modules (3) 9%, Parameter Forwarders Files 6%, Many-Argument Workhorses Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19651 | 95.5% |
| Unknown | 150 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 767 | 3.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15175*

**Composition by Extension & Reason:**
- `.cc`: 5598x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 141 LOC), 1x Excluded (Machine-Generated Source Code Signature: 187 LOC)
- `.h`: 2628x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 71 LOC), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC)
- `no_extension`: 1288x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Excluded (Binary Format Detected), 77x Unsupported Format (.undeterminable)
- `.py`: 1552x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 320 LOC), 1x Excluded (Machine-Generated Source Code Signature: 401 LOC)
- `.md`: 527x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2367 LOC), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC)
- `.mlir`: 438x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 4x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.hlo`: 281x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbtxt`: 204x Excluded: Neighborhood Micro-Mass Limit Exceeded, 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.html`: 233x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 255138 LOC exceeds safe regex boundaries)
- `.bzl`: 222x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 175 LOC), 1x Excluded (Machine-Generated Source Code Signature: 156 LOC)
- `.png`: 143x Excluded (Explicitly Denied Extension: '.png')
- `.proto`: 137x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC)
- `.build`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.build)
- `.tmpl`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.patch)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 23.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 257763 | 6410 | 25 | `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc` |
| cleanup | 1459 | 578 | 0 | `tensorflow/core/kernels/mkl/mkl_matmul_ops_common.h` |
| guards | 190994 | 8224 | 24 | `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` |
| danger | 17940 | 2007 | 0 | `tensorflow/tensorflow.bzl` |
| concurrency | 3205 | 924 | 0 | `tensorflow/tools/android/test/src/org/tensorflow/demo/tracking/ObjectTracker.java` |
| connectivity | 31439 | 5075 | 3 | `tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py` |
| io | 3635 | 598 | 0 | `ci/official/utilities/generate_index_html.sh` |
| crypto | 14 | 13 | 0 | `tensorflow/python/pywrap_tensorflow.py` |
| ipc | 241 | 102 | 0 | `tensorflow/lite/tools/pip_package/Makefile` |
| time | 262 | 85 | 0 | `tensorflow/python/distribute/coordinator/fault_tolerance_test_base.py` |
| serialization | 337 | 172 | 0 | `tensorflow/core/tpu/kernels/tpu_embedding_ops.cc` |
| regex | 451 | 176 | 0 | `tensorflow/java/src/gen/perl/tftypes.pl` |
| events | 1518 | 326 | 0 | `tensorflow/python/keras/callbacks.py` |
| tests | 11053 | 721 | 0 | `tensorflow/lite/tools/optimize/quantize_model_test.cc` |
| docs | 24941 | 2228 | 1 | `tensorflow/c/experimental/filesystem/filesystem_interface.h` |
| debt | 10860 | 2974 | 1 | `tensorflow/python/ops/parallel_for/pfor.py` |
| mutation | 435373 | 8512 | 48 | `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h` |
| dead_code | 28235 | 5556 | 3 | `tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py` |
| credential | 55 | 26 | 0 | `tensorflow/workspace2.bzl` |
| threat | 14272 | 5536 | 1 | `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_3x3_filter.h` |
| ml_ai | 19624 | 2409 | 1 | `tensorflow/core/kernels/cwise_ops.h` |
| ui | 37 | 23 | 0 | `tensorflow/lite/toco/logging/template.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ci/official/utilities/generate_index_html.sh` (Hits: 138)
- `ci/official/utilities/code_check_full.bats` (Hits: 86)
- `tensorflow/tools/tf_sig_build_dockerfiles/devel.usertools/code_check_full.bats` (Hits: 85)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **string.bin** (`tensorflow/lite/java/src/testdata/string.bin`) — 2398 inbound connections
2. **errors.h** (`tensorflow/core/platform/errors.h`) — 1071 inbound connections
3. **op_kernel.h** (`tensorflow/core/framework/op_kernel.h`) — 942 inbound connections
4. **tensor.h** (`tensorflow/core/framework/tensor.h`) — 780 inbound connections
5. **types.h** (`tensorflow/core/platform/types.h`) — 719 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **graph_to_tf_executor.cc** (`tensorflow/compiler/mlir/tf2xla/api/v2/graph_to_tf_executor.cc`) — 117 outbound dependencies
2. **flatbuffer_export.cc** (`tensorflow/compiler/mlir/lite/flatbuffer_export.cc`) — 116 outbound dependencies
3. **import_model.cc** (`tensorflow/compiler/mlir/tensorflow/translate/import_model.cc`) — 111 outbound dependencies
4. **graph_executor.cc** (`tensorflow/core/tfrt/graph_executor/graph_executor.cc`) — 104 outbound dependencies
5. **flatbuffer_import.cc** (`tensorflow/compiler/mlir/lite/flatbuffer_import.cc`) — 95 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `NNAPIDelegateKernel::Validate` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **828.0** | LOC: 1060
  * *Intent:* // Return a function that knows how to translate a node into its operands // when called. You can use this function to see if a node is supported // (...
- `NNAPIDelegateKernel::Map` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **718.8** | LOC: 912
- `ParseOpDataTfLite` **(Many-Argument Workhorses)** (@ `tensorflow/lite/core/api/flatbuffer_conversions.cc`) -> Impact: **690.3** | LOC: 872
  * *Intent:* #ifndef TF_LITE_STATIC_MEMORY
- `GetBuiltinOperatorVersion` **(Compute Cores)** (@ `tensorflow/compiler/mlir/lite/tools/versioning/op_version.cc`) -> Impact: **669.6** | LOC: 1089
- `ParseOpDataTfLite` **(Many-Argument Workhorses)** (@ `tensorflow/compiler/mlir/lite/core/api/flatbuffer_conversions.cc`) -> Impact: **633.0** | LOC: 854
  * *Intent:* #ifndef TF_LITE_STATIC_MEMORY
- `DistributedTPURewritePass::BuildExecuteNodes` **(Many-Argument Workhorses)** (@ `tensorflow/core/tpu/graph_rewrite/distributed_tpu_rewrite_pass.cc`) -> Impact: **579.1** | LOC: 684
- `ConvGeneric::GenerateConv` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`) -> Impact: **538.6** | LOC: 773
- `ConvGeneric::GuessBestParams` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`) -> Impact: **529.9** | LOC: 397
- `NNAPIDelegateKernel::AddOpsAndTensors` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **515.8** | LOC: 675
- `BaseGPUDevice::Init` **(Many-Argument Workhorses)** (@ `tensorflow/core/common_runtime/gpu/gpu_device.cc`) -> Impact: **466.5** | LOC: 1397
  * *Intent:* #ifdef TF_GPU_USE_PJRT

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tensorflow/core/kernels` | 997 | 70616.14 | 16.95% | 18.72% |
| `tensorflow/python/ops` | 138 | 54155.78 | 30.72% | 41.52% |
| `tensorflow/lite/kernels` | 201 | 28456.76 | 26.86% | 31.68% |
| `tensorflow/core/ops/compat/ops_history_v2` | 1563 | 26543.62 | 0.0% | 0.0% |
| `tensorflow/lite/kernels/internal/optimized` | 27 | 23744.18 | 32.53% | 11.83% |
| `tensorflow/lite/delegates/gpu/common/tasks` | 166 | 23302.5 | 36.41% | 26.42% |
| `tensorflow/core/api_def/base_api` | 1534 | 23110.3 | 0.0% | 0.0% |
| `tensorflow/core/common_runtime` | 222 | 22499.54 | 17.5% | 41.97% |
| `tensorflow/core/framework` | 179 | 22006.72 | 16.84% | 32.02% |
| `tensorflow/lite/testdata` | 50 | 22000.12 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tensorflow/compiler/mlir/python/mlir_wrapper/mlir_wrapper.pyi` -> **100.0%** Exposure
- `tensorflow/core/function/polymorphism/function_cache.py` -> **100.0%** Exposure
- `tensorflow/core/function/polymorphism/type_dispatch.py` -> **100.0%** Exposure
- `tensorflow/core/function/runtime_client/runtime_client_pybind.pyi` -> **100.0%** Exposure
- `tensorflow/core/function/trace_type/util.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ci/official/utilities/setup_docker.sh` -> **100.0%** Exposure
- `tensorflow/go/genop/generate.sh` -> **100.0%** Exposure
- `tensorflow/lite/delegates/gpu/cl/run_tests.sh` -> **100.0%** Exposure
- `tensorflow/lite/ios/hide_symbols_with_allowlist.sh` -> **100.0%** Exposure
- `tensorflow/lite/ios/hide_xcframework_symbols_with_allowlist.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py` -> **216** Orphaned Functions | **8** Duplicates
- `tensorflow/core/distributed_runtime/message_wrappers.cc` -> **193** Orphaned Functions | **0** Duplicates
- `tensorflow/core/ir/tf_op_names.cc` -> **186** Orphaned Functions | **0** Duplicates
- `tensorflow/core/grappler/op_types.cc` -> **183** Orphaned Functions | **0** Duplicates
- `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` -> **152** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `93630` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5198.34 | **LOC:** 7098 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NNAPIDelegateKernel::Validate` **(Many-Argument Workhorses)** (Impact: 828.0)
    * *Intent:* // Return a function that knows how to translate a node into its operands // when called. You can us...
  * `NNAPIDelegateKernel::Map` **(Many-Argument Workhorses)** (Impact: 718.8)
  * `NNAPIDelegateKernel::AddOpsAndTensors` **(Many-Argument Workhorses)** (Impact: 515.8)
  * `NNAPIDelegateKernel::Invoke` **(Many-Argument Workhorses)** (Impact: 235.2)
  * `AddTensor` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* // Adds a new NN API tensor that shadows the TF Lite tensor `tensor_index`. // This returns the NN A...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 393 instances
* *State Mutation (weighted view):* 1286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1458`, `structural_boundaries: 538`, `args: 270`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 500`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 4`, `import: 46`
* *Defense:* `safety: 7`, `test: 32`, `immutability_locks: 461`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` Core, algorithm, cinttypes, cstdarg, cstddef, cstdint, cstdio, cstring...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5153.94 | **LOC:** 8130 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Run` **(Many-Argument Workhorses)** (Impact: 140.1)
  * `PackMacroBlockIntrinsics` **(Many-Argument Workhorses)** (Impact: 132.4)
    * *Intent:* /*max_padding=*/1> {
  * `PackMacroBlockIntrinsics` **(Many-Argument Workhorses)** (Impact: 118.6)
    * *Intent:* /*max_padding=*/1> {
  * `Run` **(Many-Argument Workhorses)** (Impact: 66.7)
  * `Run` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* /*max_padding=*/0> {
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 616 instances
* *State Mutation (weighted view):* 3558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 269`, `args: 77`, `func_start: 80`, `class_start: 24`
* *Risk/State:* `state_mutation: 2326`, `fragile_debt: 9`, `duplicate_logic: 43`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 698`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` algorithm, compatibility.h, cpu_check.h, depthwiseconv_uint8.h, depthwiseconv_uint8_3x3_filter.h, depthwiseconv_uint8.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4858.72 | **LOC:** 8165 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **41**; blast radius 0.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ShuffledFullyConnectedWorkerImpl` **(Many-Argument Workhorses)** (Impact: 123.1)
    * *Intent:* // Internal function doing the actual arithmetic work for // ShuffledFullyConnected. // May be calle...
  * `HybridConvPerChannel` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `Col2im` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* // Returns in 'im_data' (assumed to be zero-initialized) image patch in storage // order (planes, he...
  * `ShuffledFullyConnected` **(Many-Argument Workhorses)** (Impact: 58.4)
  * `AveragePool` **(Many-Argument Workhorses)** (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 582 instances
* *State Mutation (weighted view):* 2373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 749`, `args: 221`, `func_start: 174`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1209`, `dead_code: 6`, `planned_debt: 36`, `fragile_debt: 9`
* *Architecture:* `api: 32`, `import: 41`
* *Defense:* `safety: 4`, `immutability_locks: 1937`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.003408
  * `Imports (Out-Degree: 25):` Accelerate.h, Core, algorithm, assert.h, cmath, cstdint, cstring, fixedpoint.h...
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `tensorflow/lite/delegates/xnnpack/xnnpack_delegate.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4551.58 | **LOC:** 7409 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Mutation Surface (formerly State Flux) (65.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisitUnaryNode` **(Many-Argument Workhorses)** (Impact: 316.4)
  * `VisitNode` **(Many-Argument Workhorses)** (Impact: 237.4)
  * `Create` **(Many-Argument Workhorses)** (Impact: 180.2)
  * `VisitBinaryNode` **(Many-Argument Workhorses)** (Impact: 177.5)
  * `Delegate::PrepareOpsToDelegate` **(Many-Argument Workhorses)** (Impact: 169.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 260 instances
* *State Mutation (weighted view):* 830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1172`, `structural_boundaries: 587`, `args: 413`, `func_start: 142`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`, `planned_debt: 8`, `unreferenced_by_name: 18`
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 48`
* *Defense:* `safety: 13`, `sync_locks: 8`, `immutability_locks: 670`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Core, algorithm, array, cassert, cinttypes, cmath, cstddef, cstdint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/parallel_for/pfor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4499.84 | **LOC:** 5227 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_convert_helper` **(Many-Argument Workhorses)** (Impact: 140.5)
  * `_process_body` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `__call__` **(Compute Cores)** (Impact: 40.3)
    * *Intent:* """Converter for the V2 while_loop. The conversion of a while_loop is another while_loop. The argume...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 37.7)
  * `_process_cond_stacked` **(Many-Argument Workhorses)** (Impact: 32.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 674 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 2515
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 806`, `args: 280`, `func_start: 249`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 1167`, `dead_code: 4`, `planned_debt: 49`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 181`, `concurrency: 9`, `import: 56`
* *Defense:* `safety: 126`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 6.5e-05
  * `Imports (Out-Degree: 3):` collections, functools, string, sys, tensorflow.compiler.tf2xla.python, tensorflow.core.framework, tensorflow.python.eager, tensorflow.python.framework...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/python/keras/backend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4365.92 | **LOC:** 6509 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Debt Markers (formerly Tech Debt) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 21.7623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rnn` **(Many-Argument Workhorses)** (Impact: 228.4)
    * *Intent:* # CONTROL FLOW
  * `batch_dot` **(Many-Argument Workhorses)** (Impact: 81.2)
    * *Intent:* """Batchwise dot product. `batch_dot` is used to compute dot product of `x` and `y` when `x` and `y`...
  * `placeholder` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `sparse_categorical_crossentropy` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* """Categorical crossentropy with integer targets. Args: target: An integer tensor. output: A tensor ...
  * `conv2d_transpose` **(Many-Argument Workhorses)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 608 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 1972
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 640`, `structural_boundaries: 719`, `args: 226`, `func_start: 224`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 2`, `state_mutation: 756`, `dead_code: 7`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 92`
* *Architecture:* `io: 12`, `api: 180`, `concurrency: 8`, `import: 70`
* *Defense:* `safety: 98`, `doc: 196`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` collections, itertools, json, numpy, os, sys, tensorflow, tensorflow.core.protobuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/compiler/tf2tensorrt/convert/convert_nodes.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3382.18 | **LOC:** 6266 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%), Complexity Load (formerly Cognitive Load) (33.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvertGraphDefToEngine` **(Many-Argument Workhorses)** (Impact: 167.1)
  * `Converter::BuildCudaEngine` **(Many-Argument Workhorses)** (Impact: 142.7)
  * `ConvertConv2DHelper` **(Many-Argument Workhorses)** (Impact: 124.1)
  * `ConvertConv3DHelper` **(Many-Argument Workhorses)** (Impact: 81.4)
  * `ConvertSegmentToGraphDef` **(Many-Argument Workhorses)** (Impact: 78.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 289 instances
* *State Mutation (weighted view):* 931
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 960`, `structural_boundaries: 642`, `args: 470`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `state_mutation: 353`, `dead_code: 8`, `planned_debt: 39`, `unreferenced_by_name: 30`
* *Architecture:* `import: 61`
* *Defense:* `safety: 27`, `doc: 2`, `test: 1`, `sync_locks: 1`, `immutability_locks: 474`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` container.h, flat_hash_set.h, memory.h, match.h, str_cat.h, str_format.h, string_view.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/tpu/graph_rewrite/distributed_tpu_rewrite_pass.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3297.04 | **LOC:** 5137 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **94**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%), Complexity Load (formerly Cognitive Load) (43.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DistributedTPURewritePass::BuildExecuteNodes` **(Many-Argument Workhorses)** (Impact: 579.1)
  * `DistributedTPURewritePass::AssignArgsAndRetvalsToCores` **(Many-Argument Workhorses)** (Impact: 365.5)
  * `DistributedTPURewritePass::BuildCompileNode` **(Many-Argument Workhorses)** (Impact: 124.0)
    * *Intent:* // Builds a TPUCompile node that compiles the bodies of the function call // `nodes`.
  * `DistributedTPURewritePass::LowerOutsideCompilationFunctionalNodes` **(Many-Argument Workhorses)** (Impact: 97.3)
  * `DistributedTPURewritePass::CopyOutsideCompilationEdges` **(Many-Argument Workhorses)** (Impact: 73.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 693`, `structural_boundaries: 312`, `args: 284`, `func_start: 120`, `class_start: 14`
* *Risk/State:* `state_mutation: 258`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 2`, `unreferenced_by_name: 37`
* *Architecture:* `api: 3`, `import: 94`
* *Defense:* `safety: 32`, `immutability_locks: 424`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` container.h, btree_map.h, flat_hash_map.h, flat_hash_set.h, check.h, log.h, status.h, statusor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/framework/ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3227.36 | **LOC:** 6233 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.4%), Guard Balance (formerly Safety Score) (92.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 47.046% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_node_def` **(Many-Argument Workhorses)** (Impact: 78.6)
  * `_as_graph_element_locked` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `_as_graph_def` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `enable_eager_execution_internal` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `_create_op_helper` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* """Common logic for creating an op in this graph."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 353 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 543`, `structural_boundaries: 868`, `args: 301`, `func_start: 299`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 531`, `dead_code: 11`, `planned_debt: 23`, `fragile_debt: 4`, `duplicate_logic: 7`, `unreferenced_by_name: 97`
* *Architecture:* `io: 1`, `api: 150`, `concurrency: 3`, `import: 64`
* *Defense:* `safety: 187`, `doc: 204`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` absl, collections, collections.abc, contextlib, copy, dependency, dependency., enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/nn_ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3141.56 | **LOC:** 6703 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.5%)
- **Documentation Coverage:** 62.6214% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convolution_internal` **(Many-Argument Workhorses)** (Impact: 127.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 100.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 93.5)
  * `pool` **(Many-Argument Workhorses)** (Impact: 84.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 81.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 363 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 410`, `args: 113`, `func_start: 112`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 504`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 90`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 34`, `doc: 93`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4.9e-05
  * `Imports (Out-Degree: 5):` functools, numbers, numpy, tensorflow, tensorflow.python.eager, tensorflow.python.framework, tensorflow.python.ops, tensorflow.python.ops.gen_nn_ops...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3141.56 | **LOC:** 6120 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **89**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Debt Markers (formerly Tech Debt) (96.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.9%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetReshapeOutputType` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `FullyConnectedOp::fold` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `Conv2DOp::inferReturnTypes` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `VerifyConcatenationOpTypes` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* // Verify operand types and the result type: // // 1. Operand type ranks must be equal to the output...
  * `UnidirectionalSequenceLSTMOp::inferReturnTypes` **(Many-Argument Workhorses)** (Impact: 48.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 716
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1075`, `structural_boundaries: 1297`, `args: 325`, `func_start: 228`, `class_start: 23`
* *Risk/State:* `state_mutation: 254`, `dead_code: 3`, `planned_debt: 35`, `unreferenced_by_name: 152`
* *Architecture:* `api: 1`, `import: 91`
* *Defense:* `safety: 41`, `doc: 29`, `sync_locks: 3`, `immutability_locks: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Core, const_init.h, flat_hash_map.h, flat_hash_set.h, status.h, statusor.h, escaping.h, mutex.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/grappler/optimizers/constant_folding.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3134.36 | **LOC:** 4134 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Debt Markers (formerly Tech Debt) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConstantFolding::SimplifyArithmeticOperations` **(Many-Argument Workhorses)** (Impact: 172.7)
  * `ConstantFolding::ConstantPushDown` **(Many-Argument Workhorses)** (Impact: 127.7)
  * `ConstantFolding::MaterializeShapes` **(Compute Cores)** (Impact: 87.8)
    * *Intent:* // Materialize the shapes using constants whenever possible.
  * `ConstantFolding::MulConvPushDown` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `ConstantFolding::SimplifyStridedSlice` **(Many-Argument Workhorses)** (Impact: 71.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 220 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1049`, `structural_boundaries: 434`, `args: 269`, `func_start: 87`
* *Risk/State:* `state_mutation: 238`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `unreferenced_by_name: 69`
* *Architecture:* `import: 44`
* *Defense:* `test: 3`, `immutability_locks: 351`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` status.h, str_cat.h, string_view.h, substitute.h, algorithm, cmath, limits, allocator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3048.16 | **LOC:** 2055 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvGeneric::GenerateConv` **(Many-Argument Workhorses)** (Impact: 538.6)
  * `ConvGeneric::GuessBestParams` **(Many-Argument Workhorses)** (Impact: 529.9)
  * `GetConvParamsForA7A8` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `GetConvParamsForA9AndHigher` **(Many-Argument Workhorses)** (Impact: 80.2)
  * `GenerateBlockCoords` **(Many-Argument Workhorses)** (Impact: 76.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 445 instances
* *State Mutation (weighted view):* 1412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 66`, `args: 96`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `state_mutation: 522`, `unreferenced_by_name: 14`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 249`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` substitute.h, algorithm, string, data_type.h, shape.h, status.h, util.h, work_group_picking.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/framework/test_util.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2950.56 | **LOC:** 4313 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.5%), Guard Balance (formerly Safety Score) (91.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 56.6079% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_reference_cycle` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `_assertAllCloseRecursive` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `assertAllEqual` **(Many-Argument Workhorses)** (Impact: 43.1)
    * *Intent:* """Asserts that two numpy arrays or Tensors have the same values. Args: a: the expected numpy ndarra...
  * `assertAllInRange` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `_assertArrayLikeAllClose` **(Many-Argument Workhorses)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 262 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 757`, `args: 232`, `func_start: 230`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 331`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 2`, `unreferenced_by_name: 88`
* *Architecture:* `io: 5`, `api: 202`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 112`, `doc: 138`, `test: 18`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` absl.testing, collections, collections.abc, contextlib, functools, gc, google.protobuf, is...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/eager/pywrap_tfe_src.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2918.8 | **LOC:** 4259 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Debt Markers (formerly Tech Debt) (56.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MakeIntList` **(Compute Cores)** (Impact: 457.1)
  * `SetOpAttrList` **(Many-Argument Workhorses)** (Impact: 135.3)
  * `TFE_Py_FastPathExecute_C` **(Compute Cores)** (Impact: 112.0)
  * `SetOpAttrScalar` **(Many-Argument Workhorses)** (Impact: 103.8)
  * `SetOpAttrListDefault` **(Many-Argument Workhorses)** (Impact: 89.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 203 instances
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 622
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 677`, `structural_boundaries: 549`, `args: 291`, `func_start: 191`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 216`, `dead_code: 2`, `planned_debt: 11`, `unreferenced_by_name: 59`
* *Architecture:* `api: 10`, `import: 61`
* *Defense:* `safety: 38`, `test: 3`, `sync_locks: 3`, `immutability_locks: 174`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` flat_hash_map.h, leak_check.h, status.h, str_cat.h, string_view.h, span.h, atomic, cstdint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/compiler/mlir/tosa/transforms/legalize_common.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2876.16 | **LOC:** 5064 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertStridedSliceOp` **(Many-Argument Workhorses)** (Impact: 234.5)
    * *Intent:* // Lowers StridedSlice to a sequence of TOSA ops.
  * `convertResizeOp` **(Many-Argument Workhorses)** (Impact: 136.2)
    * *Intent:* // Lowers ResizeBilinear and ResizeNearestNeighbor to TOSA resize.
  * `convertPackOp` **(Many-Argument Workhorses)** (Impact: 92.9)
    * *Intent:* // Lowers the Pack operator to TOSA.
  * `convertGatherOp` **(Many-Argument Workhorses)** (Impact: 89.0)
    * *Intent:* // Lowers Gather operators to a sequence of TOSA ops.
  * `convertReduceOpCommon` **(Many-Argument Workhorses)** (Impact: 85.7)
    * *Intent:* // Common function for lowering reduce operations to TOSA ops. // Nan propagation mode is only appli...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 322 instances
* *State Mutation (weighted view):* 1039
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 693`, `args: 74`, `func_start: 57`
* *Risk/State:* `state_mutation: 395`, `dead_code: 13`, `planned_debt: 2`, `unreferenced_by_name: 42`
* *Architecture:* `import: 38`
* *Defense:* `safety: 66`, `doc: 6`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` algorithm, climits, cmath, cstddef, cstdint, iterator, limits, ArrayRef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/util/example_proto_fast_parsing.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2847.06 | **LOC:** 3108 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FastParseSerializedExample` **(Many-Argument Workhorses)** (Impact: 392.1)
  * `FastParseSingleExample` **(Many-Argument Workhorses)** (Impact: 219.9)
  * `FastParseExample` **(Many-Argument Workhorses)** (Impact: 145.5)
  * `ParseSequenceRaggedFeatures` **(Many-Argument Workhorses)** (Impact: 137.2)
    * *Intent:* // Parses ragged features in `sequence_features`, and writes their parsed // values to `sequence_res...
  * `ParseSequenceDenseFeatures` **(Many-Argument Workhorses)** (Impact: 136.6)
    * *Intent:* // Parses dense features in `sequence_features`, and writes their parsed // values to `sequence_resu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 832
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 714`, `structural_boundaries: 397`, `args: 96`, `func_start: 71`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 314`, `dead_code: 5`, `planned_debt: 15`, `unreferenced_by_name: 6`
* *Architecture:* `api: 3`, `import: 27`
* *Defense:* `safety: 1`, `immutability_locks: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` casts.h, flat_hash_map.h, status.h, substitute.h, algorithm, functional, optional, example.pb.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/grappler/optimizers/remapper.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2752.68 | **LOC:** 5411 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.1%), Mutation Surface (formerly State Flux) (22.4%), Complexity Load (formerly Cognitive Load) (19.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Remapper::Optimize` **(Many-Argument Workhorses)** (Impact: 183.2)
  * `FindMatMulBiasAddAndGelu` **(Many-Argument Workhorses)** (Impact: 126.9)
    * *Intent:* // Gelu in python api generates a number of nodes in the graph. Depending on the // parmeter `approx...
  * `RequiresInferredShapes` **(Many-Argument Workhorses)** (Impact: 119.5)
    * *Intent:* // Check if a node is a candidate to one of the patterns that require inferred // shapes: // (1) Spl...
  * `FindMklLayerNorm` **(Many-Argument Workhorses)** (Impact: 95.6)
    * *Intent:* // Keras LayerNormalization api uses multiple TensorFlow ops. Current fusion // pattern is only for ...
  * `FindFusedBatchNormEx` **(Many-Argument Workhorses)** (Impact: 92.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 906`, `structural_boundaries: 737`, `args: 226`, `func_start: 109`, `class_start: 14`
* *Risk/State:* `state_mutation: 133`, `dead_code: 5`, `planned_debt: 20`, `unreferenced_by_name: 1`
* *Architecture:* `import: 31`
* *Defense:* `immutability_locks: 428`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` flat_hash_set.h, algorithm, cstdlib, map, set, string, tensor_shape.h, versions.pb.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/delegates/gpu/common/model_builder.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2687.62 | **LOC:** 3661 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.4%), Complexity Load (formerly Cognitive Load) (85.2%), Guard Balance (formerly Safety Score) (82.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewOperationParser` **(Type Conversions)** (Impact: 196.4)
  * `GetOpsToReplace` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* // TODO(impjdi): Check number of input/output tensors and their dimensions. // TODO(impjdi): Check o...
  * `Parse` **(Many-Argument Workhorses)** (Impact: 56.3)
  * `Parse` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `ParseInputsWithConstTensorImpl` **(Many-Argument Workhorses)** (Impact: 47.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 265 instances
* *State Mutation (weighted view):* 1004
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 563`, `structural_boundaries: 444`, `args: 364`, `func_start: 138`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 474`, `dead_code: 3`, `planned_debt: 13`, `duplicate_logic: 37`, `unreferenced_by_name: 4`
* *Architecture:* `api: 45`, `import: 43`
* *Defense:* `safety: 91`, `immutability_locks: 493`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` flat_hash_map.h, flat_hash_set.h, status.h, str_cat.h, str_join.h, string_view.h, algorithm, cstddef...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/compiler/mlir/tf2xla/transforms/legalize_tf.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2584.86 | **LOC:** 7050 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.5%)
- **Documentation Coverage:** 95.8084% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `rewriteWithUnknownBegin` **(Many-Argument Workhorses)** (Impact: 43.7)
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `GetPaddingValues` **(Many-Argument Workhorses)** (Impact: 36.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 1102`, `args: 193`, `func_start: 153`, `class_start: 86`
* *Risk/State:* `state_mutation: 353`, `dead_code: 9`, `planned_debt: 37`, `duplicate_logic: 7`, `unreferenced_by_name: 23`
* *Architecture:* `api: 76`, `import: 67`
* *Defense:* `safety: 85`, `doc: 37`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` status.h, algorithm, cassert, cmath, cstddef, cstdint, functional, iterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/compiler/mlir/stablehlo/transforms/legalize_tf.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2578.5 | **LOC:** 7023 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **64**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%), Debt Markers (formerly Tech Debt) (33.5%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `rewriteWithUnknownBegin` **(Many-Argument Workhorses)** (Impact: 43.7)
  * `matchAndRewrite` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `GetPaddingValues` **(Many-Argument Workhorses)** (Impact: 36.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 1108`, `args: 188`, `func_start: 154`, `class_start: 87`
* *Risk/State:* `state_mutation: 352`, `dead_code: 9`, `planned_debt: 37`, `duplicate_logic: 7`, `unreferenced_by_name: 23`
* *Architecture:* `api: 77`, `import: 64`
* *Defense:* `safety: 86`, `doc: 37`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` status.h, algorithm, cassert, cmath, cstddef, cstdint, functional, iterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/c/c_api.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2533.4 | **LOC:** 2825 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **63**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.0%)
- **Documentation Coverage:** 90.46% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TF_OperationGetAttrMetadata` **(Many-Argument Workhorses)** (Impact: 83.3)
  * `TF_AddGradientsWithPrefix` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `TF_Run_Helper` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `TF_LoadSessionFromSavedModel` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `TF_NewWhile` **(Many-Argument Workhorses)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 319 instances
* *State Mutation (weighted view):* 1010
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 407`, `args: 239`, `func_start: 183`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 372`, `planned_debt: 14`, `fragile_debt: 8`
* *Architecture:* `api: 141`, `import: 63`
* *Defense:* `safety: 4`, `test: 1`, `sync_locks: 6`, `immutability_locks: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` match.h, algorithm, cstring, limits, memory, optional, c_api.h, c_api_internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/ops/ragged/dynamic_ragged_shape.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2492.08 | **LOC:** 3293 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (75.3%)
- **Documentation Coverage:** 53.8095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 79.2)
  * `ragged_binary_elementwise_op_impl` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* """Binary elementwise api handler for RaggedTensors."""
  * `from_lengths` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `ragged_binary_elementwise_assert_op_impl` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* """Binary elementwise assert api handler for RaggedTensors. This handles binary assert operations fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 300 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 1024
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 484`, `args: 142`, `func_start: 142`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 424`, `dead_code: 2`, `planned_debt: 17`, `duplicate_logic: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 70`, `concurrency: 13`, `import: 22`
* *Defense:* `safety: 75`, `doc: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` abc, numpy, tensorflow.python.framework, tensorflow.python.ops, tensorflow.python.ops.ragged, tensorflow.python.ops.ragged.row_partition, tensorflow.python.types, tensorflow.python.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2483.1 | **LOC:** 4519 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.8%), Guard Balance (formerly Safety Score) (65.6%), Complexity Load (formerly Cognitive Load) (32.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetStridedSliceAxis` **(Many-Argument Workhorses)** (Impact: 88.5)
  * `ArithmeticOptimizer::SimplifyArithmeticOps` **(Type Conversions)** (Impact: 77.2)
  * `GetSimpleSliceAxis` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `GetCommonFactors` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* // Determine the set of common factors if the input nodes are all Mul or // Div nodes.
  * `TrySimplify` **(Many-Argument Workhorses)** (Impact: 48.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 177 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 510`, `args: 399`, `func_start: 188`, `class_start: 38`
* *Risk/State:* `state_mutation: 212`, `dead_code: 2`, `planned_debt: 25`, `duplicate_logic: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 34`, `import: 42`
* *Defense:* `safety: 101`, `doc: 1`, `test: 2`, `immutability_locks: 506`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` flat_hash_map.h, flat_hash_set.h, str_join.h, algorithm, deque, limits, attr_value.pb.h, attr_value_util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/legacy_optimized_ops.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2476.06 | **LOC:** 5023 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Conv` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `ShuffledFullyConnected` **(Many-Argument Workhorses)** (Impact: 58.2)
  * `LegacyFullyConnectedAsGEMVWorkerImpl` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* #ifdef USE_NEON
  * `LstmCell` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `LegacyInt8FullyConnectedAsGEMVWorkerImpl` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* #ifdef USE_NEON
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 1008
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 491`, `args: 208`, `func_start: 162`, `class_start: 7`
* *Risk/State:* `state_mutation: 708`, `dead_code: 3`, `planned_debt: 10`, `fragile_debt: 6`, `unreferenced_by_name: 23`
* *Architecture:* `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 1185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` algorithm, gemmlowp.h, stdint.h, types.h, cpu_backend_context.h, cpu_check.h, depthwiseconv_multithread.h, depthwise_conv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tensorflow/lite/delegates/xnnpack/weight_cache.cc` -> Churn: **76.02%** | Cog Load: 22.2311% | Debt: 95.1684%
- `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` -> Churn: **71.94%** | Cog Load: 35.2588% | Debt: 96.8089%
- `tensorflow/core/kernels/batching_util/batch_resource_base.cc` -> Churn: **61.99%** | Cog Load: 37.1962% | Debt: 57.065%
- `tensorflow/python/framework/test_util.py` -> Churn: **59.58%** | Cog Load: 38.5267% | Debt: 98.5055%
- `tensorflow/core/framework/op_kernel.cc` -> Churn: **58.45%** | Cog Load: 23.2582% | Debt: 90.8723%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tensorflow/core/grappler/optimizers/constant_folding.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 3134.36
- `tensorflow/core/grappler/optimizers/remapper.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2752.68
- `tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2483.1
- `tensorflow/python/ops/image_ops_impl.py` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2233.06
- `tensorflow/core/common_runtime/gpu/gpu_device.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2131.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tensorflow/compiler/mlir/tensorflow/ir/tf_traits.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 89.9867%)
- `tensorflow/core/util/gpu_kernel_helper.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `tensorflow/core/util/gpu_launch_config.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.7685%)
- `tensorflow/lite/kernels/internal/reference/reference_ops.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9979%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tensorflow/core/framework/tensor_types.h` -> **Severity: 4.514** (Embedded: 0.066 * Error Risk: 68.3938%)
- `tensorflow/core/framework/tensor_shape.h` -> **Severity: 4.349** (Embedded: 0.0775 * Error Risk: 56.128%)
- `tensorflow/core/framework/tensor.h` -> **Severity: 3.872** (Embedded: 0.0763 * Error Risk: 50.7631%)
- `tensorflow/core/framework/types.h` -> **Severity: 3.79** (Embedded: 0.0726 * Error Risk: 52.2099%)
- `tensorflow/core/tfrt/mlrt/bytecode/span.h` -> **Severity: 3.714** (Embedded: 0.0601 * Error Risk: 61.7748%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tensorflow/lite/core/c/common.h` -> **Severity: 734.3** (Blast Radius: 7.343 * Doc Risk: 100.0%)
- `tensorflow/core/framework/op_kernel.h` -> **Severity: 528.4** (Blast Radius: 5.284 * Doc Risk: 100.0%)
- `tensorflow/core/tfrt/mlrt/bytecode/bytecode.h` -> **Severity: 464.6** (Blast Radius: 4.646 * Doc Risk: 100.0%)
- `tensorflow/core/framework/types.h` -> **Severity: 444.3** (Blast Radius: 4.443 * Doc Risk: 100.0%)
- `tensorflow/core/framework/tensor_types.h` -> **Severity: 385.3** (Blast Radius: 3.853 * Doc Risk: 100.0%)

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
