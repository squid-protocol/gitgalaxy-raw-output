# ARCHITECTURAL_BRIEF: tensorflow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tensorflow/tensorflow.git` |
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
- **Scope:** 24370 analyzed artifact(s), 3587986 LOC.
- **Load-bearing artifact:** `tensorflow/core/framework/op_kernel.h` -- 1070 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tensorflow/lite/testing/generate_examples_lib.py` -- pulls in 163 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc` at magnitude 5281.54 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 24370 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11376 |
| Total LOC | 3587986 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.2% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6729 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0594 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.9373 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 620 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 10551 | 1844687 | 43.3% |
| PBTXT | 7606 | 803346 | 31.2% |
| PYTHON | 3192 | 747137 | 13.1% |
| MLIR | 941 | 77747 | 3.9% |
| MARKDOWN | 723 | 0 | 3.0% |
| SHELL | 211 | 9533 | 0.9% |
| PROTO | 201 | 7001 | 0.8% |
| JAVA | 180 | 20572 | 0.7% |
| PLAINTEXT | 126 | 0 | 0.5% |
| TD | 120 | 45563 | 0.5% |
| OBJECTIVE-C | 105 | 7016 | 0.4% |
| XML | 77 | 8 | 0.3% |
| HTML | 57 | 9876 | 0.2% |
| C | 47 | 1851 | 0.2% |
| GO | 40 | 5817 | 0.2% |
| DOCKERFILE | 34 | 1155 | 0.1% |
| JSON | 33 | 1848 | 0.1% |
| BINARY_THREAT | 33 | 33 | 0.1% |
| YAML | 28 | 1437 | 0.1% |
| SWIFT | 18 | 1348 | 0.1% |
| BATCH | 12 | 308 | 0.0% |
| GROOVY | 9 | 343 | 0.0% |
| MAKEFILE | 8 | 316 | 0.0% |
| RUBY | 6 | 219 | 0.0% |
| CSV | 3 | 230 | 0.0% |
| M4 | 2 | 63 | 0.0% |
| PERL | 2 | 152 | 0.0% |
| CSHARP | 2 | 272 | 0.0% |
| CSS | 2 | 72 | 0.0% |
| JAVASCRIPT | 1 | 36 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 24332 |
| unknown | unknown | 33 |
| latin-1 | latin-1-fallback | 3 |
| utf-8 | bom | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 38%, Data / Markup / Trivial 16%, Large Core Modules (3) 10%, Parameter Forwarders Files 9%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 23475 | 96.3% |
| Unknown | 33 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 854 | 3.5% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11376*

**Composition by Extension & Reason:**
- `.cc`: 3678x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 90 LOC), 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.h`: 2398x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 673 LOC), 1x Excluded (Machine-Generated Source Code Signature: 25638 LOC)
- `no_extension`: 1272x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 206x Excluded (Binary Format Detected), 85x Unsupported Format (.undeterminable)
- `.md`: 130x Excluded (Machine-Generated Source Code Signature: 39 LOC), 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 23x Excluded (Machine-Generated Source Code Signature: 96 LOC)
- `.mlir`: 422x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 4x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.hlo`: 281x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbtxt`: 204x Excluded: Neighborhood Micro-Mass Limit Exceeded, 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.bzl`: 214x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 175 LOC)
- `.html`: 7x Excluded (Machine-Generated Source Code Signature: 311 LOC), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.py`: 169x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 122 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1512 LOC)
- `.png`: 143x Excluded (Explicitly Denied Extension: '.png')
- `.build`: 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.build), 2x Excluded (Unsupported Extension: '.BUILD')
- `.proto`: 133x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 106x Excluded (Unsupported Extension: '.tmpl')
- `.bin`: 89x Excluded (Unsupported Extension: '.bin'), 12x Excluded (Binary Format Detected), 1x Unsupported Format (.bin)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.7 | 22.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 80415 | 6811 | 7 | `tensorflow/core/kernels/image/non_max_suppression_op_test.cc` |
| cleanup | 2093 | 775 | 0 | `tensorflow/core/kernels/mkl/mkl_matmul_ops_common.h` |
| guards | 232597 | 10867 | 24 | `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` |
| danger | 24051 | 2900 | 1 | `tensorflow/tensorflow.bzl` |
| concurrency | 5007 | 1229 | 0 | `tensorflow/python/ops/parallel_for/control_flow_ops_test.py` |
| connectivity | 69513 | 7311 | 5 | `tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py` |
| io | 7363 | 938 | 0 | `tensorflow/lite/g3doc/api_docs/c/group/c-api.html` |
| crypto | 15 | 14 | 0 | `tensorflow/python/pywrap_tensorflow.py` |
| ipc | 309 | 119 | 0 | `tensorflow/lite/tools/pip_package/Makefile` |
| time | 598 | 179 | 0 | `tensorflow/python/distribute/coordinator/fault_tolerance_test_base.py` |
| serialization | 671 | 290 | 0 | `tensorflow/core/common_runtime/graph_constructor_test.cc` |
| regex | 567 | 220 | 0 | `tensorflow/java/src/gen/perl/tftypes.pl` |
| events | 1955 | 411 | 0 | `tensorflow/python/keras/callbacks.py` |
| tests | 82815 | 3624 | 3 | `tensorflow/core/grappler/optimizers/arithmetic_optimizer_test.cc` |
| docs | 30351 | 3707 | 1 | `tensorflow/c/experimental/filesystem/filesystem_interface.h` |
| debt | 16041 | 3909 | 1 | `tensorflow/python/saved_model/load_test.py` |
| mutation | 786131 | 11878 | 74 | `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h` |
| dead_code | 64164 | 8287 | 7 | `tensorflow/compiler/tests/randomized_tests.cc` |
| credential | 93 | 28 | 0 | `tensorflow/core/grappler/mutable_graph_view_test.cc` |
| threat | 89 | 29 | 0 | `tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py` |
| ml_ai | 36530 | 3904 | 4 | `tensorflow/lite/testing/generate_examples_lib.py` |
| ui | 189 | 48 | 0 | `tensorflow/lite/g3doc/api_docs/swift/Enums/InterpreterError.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tensorflow/lite/g3doc/api_docs/c/group/c-api.html` (Hits: 452)
- `tensorflow/lite/g3doc/api_docs/cc/class/tflite/impl/interpreter.html` (Hits: 152)
- `ci/official/utilities/generate_index_html.sh` (Hits: 138)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **op_kernel.h** (`tensorflow/core/framework/op_kernel.h`) — 1070 inbound connections
2. **tensor.h** (`tensorflow/core/framework/tensor.h`) — 1054 inbound connections
3. **tensor_shape.h** (`tensorflow/core/framework/tensor_shape.h`) — 900 inbound connections
4. **test.h** (`tensorflow/core/platform/test.h`) — 898 inbound connections
5. **types.h** (`tensorflow/core/platform/types.h`) — 895 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **generate_examples_lib.py** (`tensorflow/lite/testing/generate_examples_lib.py`) — 163 outbound dependencies
2. **graph_to_tf_executor.cc** (`tensorflow/compiler/mlir/tf2xla/api/v2/graph_to_tf_executor.cc`) — 117 outbound dependencies
3. **flatbuffer_export.cc** (`tensorflow/compiler/mlir/lite/flatbuffer_export.cc`) — 116 outbound dependencies
4. **import_model.cc** (`tensorflow/compiler/mlir/tensorflow/translate/import_model.cc`) — 111 outbound dependencies
5. **graph_executor.cc** (`tensorflow/core/tfrt/graph_executor/graph_executor.cc`) — 104 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `NNAPIDelegateKernel::Validate` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **955.9** | LOC: 1299
  * *Intent:* // Return a function that knows how to translate a node into its operands // when called. You can use this function to see if a node is supported // (...
- `NNAPIDelegateKernel::Map` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **718.8** | LOC: 912
- `ParseOpDataTfLite` **(Many-Argument Workhorses)** (@ `tensorflow/lite/core/api/flatbuffer_conversions.cc`) -> Impact: **685.4** | LOC: 872
  * *Intent:* #ifndef TF_LITE_STATIC_MEMORY
- `GetBuiltinOperatorVersion` **(Compute Cores)** (@ `tensorflow/compiler/mlir/lite/tools/versioning/op_version.cc`) -> Impact: **669.6** | LOC: 1089
- `ParseOpDataTfLite` **(Many-Argument Workhorses)** (@ `tensorflow/compiler/mlir/lite/core/api/flatbuffer_conversions.cc`) -> Impact: **628.5** | LOC: 854
  * *Intent:* #ifndef TF_LITE_STATIC_MEMORY
- `DistributedTPURewritePass::BuildExecuteNodes` **(Many-Argument Workhorses)** (@ `tensorflow/core/tpu/graph_rewrite/distributed_tpu_rewrite_pass.cc`) -> Impact: **548.6** | LOC: 684
- `ConvGeneric::GuessBestParams` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`) -> Impact: **529.9** | LOC: 397
- `NNAPIDelegateKernel::AddOpsAndTensors` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc`) -> Impact: **513.8** | LOC: 675
- `ConvGeneric::GenerateConv` **(Many-Argument Workhorses)** (@ `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc`) -> Impact: **492.6** | LOC: 773
- `MakeIntList` **(Compute Cores)** (@ `tensorflow/python/eager/pywrap_tfe_src.cc`) -> Impact: **440.1** | LOC: 1476

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tensorflow/core/kernels` | 1156 | 82972.34 | 13.32% | 19.61% |
| `tensorflow/python/ops` | 203 | 76235.58 | 35.77% | 50.99% |
| `tensorflow/lite/kernels` | 362 | 49129.48 | 20.1% | 47.14% |
| `tensorflow/python/framework` | 188 | 38613.76 | 24.06% | 53.1% |
| `tensorflow/python/distribute` | 102 | 34643.54 | 41.38% | 77.65% |
| `tensorflow/core/common_runtime` | 295 | 29362.12 | 15.82% | 41.47% |
| `tensorflow/core/framework` | 232 | 28981.52 | 14.64% | 38.79% |
| `tensorflow/core/grappler/optimizers` | 87 | 27042.76 | 18.83% | 36.02% |
| `tensorflow/core/ops/compat/ops_history_v2` | 1563 | 26543.62 | 0.0% | 0.0% |
| `tensorflow/lite/kernels/internal/optimized` | 30 | 23927.66 | 29.18% | 16.27% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tensorflow/compiler/mlir/python/mlir_wrapper/mlir_wrapper.pyi` -> **100.0%** Exposure
- `tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py` -> **100.0%** Exposure
- `tensorflow/core/function/capture/free_vars_detect_test.py` -> **100.0%** Exposure
- `tensorflow/core/function/integration_test/side_inputs_manual_api_test.py` -> **100.0%** Exposure
- `tensorflow/core/function/integration_test/side_inputs_test.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ci/official/utilities/setup_docker.sh` -> **100.0%** Exposure
- `tensorflow/go/genop/generate.sh` -> **100.0%** Exposure
- `tensorflow/lite/delegates/gpu/cl/run_tests.sh` -> **100.0%** Exposure
- `tensorflow/lite/ios/hide_symbols_with_allowlist.sh` -> **100.0%** Exposure
- `tensorflow/lite/ios/hide_xcframework_symbols_with_allowlist.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py` -> **239** Orphaned Functions | **71** Duplicates
- `tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py` -> **242** Orphaned Functions | **34** Duplicates
- `tensorflow/python/ops/image_ops_test.py` -> **203** Orphaned Functions | **64** Duplicates
- `tensorflow/compiler/tests/randomized_tests.cc` -> **255** Orphaned Functions | **0** Duplicates
- `tensorflow/tools/ci_build/osx/arm64/tensorflow_metal_plugin_test.py` -> **216** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `53` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `126653` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tensorflow/lite/delegates/nnapi/nnapi_delegate.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.259)
- **Top Global Matches:** file_cluster_4: 6.259, file_cluster_6: 10.2, file_cluster_15: 12.25
- **Magnitude:** 5281.54 | **LOC:** 7098 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **46**; blast radius 0.04; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.1%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NNAPIDelegateKernel::Validate` **(Many-Argument Workhorses)** (Impact: 955.9)
    * *Intent:* // Return a function that knows how to translate a node into its operands // when called. You can us...
  * `NNAPIDelegateKernel::Map` **(Many-Argument Workhorses)** (Impact: 718.8)
  * `NNAPIDelegateKernel::AddOpsAndTensors` **(Many-Argument Workhorses)** (Impact: 513.8)
  * `NNAPIDelegateKernel::Invoke` **(Many-Argument Workhorses)** (Impact: 225.2)
  * `AddTensor` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* // Adds a new NN API tensor that shadows the TF Lite tensor `tensor_index`. // This returns the NN A...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1418`, `structural_boundaries: 538`, `args: 270`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 500`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 4`, `import: 46`
* *Defense:* `safety: 7`, `test: 32`, `immutability_locks: 461`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.002183
  * `Imports (Out-Degree: 26):` Core, algorithm, cinttypes, cstdarg, cstddef, cstdint, cstdio, cstring...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tensorflow/lite/kernels/internal/optimized/depthwiseconv_uint8_transitional.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.853)
- **Top Global Matches:** file_cluster_6: 6.853, file_cluster_4: 11.35, file_cluster_8: 14.817
- **Magnitude:** 5153.94 | **LOC:** 8130 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (70.4%)
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
* *Risk/State:* `state_mutation: 2326`, `dead_code: 2`, `fragile_debt: 9`, `duplicate_logic: 43`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 698`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 4.1e-05
  * `Imports (Out-Degree: 7):` algorithm, compatibility.h, cpu_check.h, depthwiseconv_uint8.h, depthwiseconv_uint8_3x3_filter.h, depthwiseconv_uint8.h, types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/python/ops/image_ops_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.449)
- **Top Global Matches:** file_cluster_15: 6.449, file_cluster_16: 7.081, file_cluster_12: 7.572
- **Magnitude:** 5137.28 | **LOC:** 6803 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (76.6%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 91.9137% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDecodeImageShapeInferenceInDataPipeline` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* """Test that decode_image sets proper shape inference in tf.data pipelines. This test verifies the f...
  * `testRandomFlipStatelessWithBatch` **(Compute Cores)** (Impact: 23.2)
  * `testReturnDtypeV2` **(Compute Cores)** (Impact: 18.7)
  * `testDataTypes` **(Compute Cores)** (Impact: 17.6)
    * *Intent:* # Test case for GitHub issue 20199. boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9], [...
  * `testRandomFlipStateless` **(Compute Cores)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 569 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 3030
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 963`, `args: 409`, `func_start: 408`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 4`, `state_mutation: 1892`, `planned_debt: 13`, `fragile_debt: 2`, `duplicate_logic: 64`, `unreferenced_by_name: 203`
* *Architecture:* `io: 37`, `api: 383`, `concurrency: 2`, `import: 39`
* *Defense:* `safety: 1`, `doc: 41`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` absl.testing, colorsys, contextlib, functools, itertools, math, numpy, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/kernels/internal/optimized/optimized_ops.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.427)
- **Top Global Matches:** file_cluster_15: 8.427, file_cluster_16: 9.433, file_cluster_4: 9.462
- **Magnitude:** 4771.22 | **LOC:** 8165 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **76** in-repo importer(s); it depends on **41**; blast radius 0.197; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.3%), Guard Balance (formerly Safety Score) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ShuffledFullyConnectedWorkerImpl` **(Many-Argument Workhorses)** (Impact: 116.5)
    * *Intent:* // Internal function doing the actual arithmetic work for // ShuffledFullyConnected. // May be calle...
  * `HybridConvPerChannel` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `Col2im` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* // Returns in 'im_data' (assumed to be zero-initialized) image patch in storage // order (planes, he...
  * `PadImpl` **(Many-Argument Workhorses)** (Impact: 51.6)
    * *Intent:* // This makes heavy use of Offset, along with conditional branches. There may be // opportunities fo...
  * `ShuffledFullyConnected` **(Many-Argument Workhorses)** (Impact: 51.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 564 instances
* *State Mutation (weighted view):* 2337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 536`, `structural_boundaries: 749`, `args: 221`, `func_start: 174`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1209`, `dead_code: 20`, `planned_debt: 36`, `fragile_debt: 9`
* *Architecture:* `api: 32`, `import: 41`
* *Defense:* `safety: 4`, `immutability_locks: 1937`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.007896
  * `Imports (Out-Degree: 26):` Accelerate.h, Core, algorithm, assert.h, cmath, cstdint, cstring, fixedpoint.h...
  * `Imported By (In-Degree: 76):` (Excluded from Brief to save tokens)

### `tensorflow/python/ops/parallel_for/pfor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.0)
- **Top Global Matches:** file_cluster_12: 9.0, file_cluster_5: 10.568, file_cluster_16: 10.972
- **Magnitude:** 4499.84 | **LOC:** 5227 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.027; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%)
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
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 1167`, `planned_debt: 49`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 181`, `concurrency: 9`, `import: 56`
* *Defense:* `safety: 126`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 5.5e-05
  * `Imports (Out-Degree: 1):` collections, functools, string, sys, tensorflow.compiler.tf2xla.python, tensorflow.core.framework, tensorflow.python.eager, tensorflow.python.framework...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/lite/delegates/xnnpack/xnnpack_delegate.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_6: 6.869, file_cluster_4: 8.3, file_cluster_15: 16.007
- **Magnitude:** 4433.08 | **LOC:** 7409 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **117** in-repo importer(s); it depends on **48**; blast radius 0.436; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.1%), Guard Balance (formerly Safety Score) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisitUnaryNode` **(Many-Argument Workhorses)** (Impact: 316.4)
  * `VisitNode` **(Many-Argument Workhorses)** (Impact: 234.4)
  * `VisitBinaryNode` **(Many-Argument Workhorses)** (Impact: 177.5)
  * `Create` **(Many-Argument Workhorses)** (Impact: 176.2)
  * `Delegate::PrepareOpsToDelegate` **(Many-Argument Workhorses)** (Impact: 165.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1117`, `structural_boundaries: 587`, `args: 413`, `func_start: 142`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`, `dead_code: 1`, `planned_debt: 8`, `unreferenced_by_name: 18`
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 48`
* *Defense:* `safety: 13`, `sync_locks: 8`, `immutability_locks: 670`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.004559
  * `Imports (Out-Degree: 28):` Core, algorithm, array, cassert, cinttypes, cmath, cstddef, cstdint...
  * `Imported By (In-Degree: 117):` (Excluded from Brief to save tokens)

### `tensorflow/python/keras/backend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.194)
- **Top Global Matches:** file_cluster_12: 8.194, file_cluster_4: 9.261, file_cluster_15: 10.106
- **Magnitude:** 4365.92 | **LOC:** 6509 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.9%), Guard Balance (formerly Safety Score) (80.2%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 2`, `state_mutation: 756`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 92`
* *Architecture:* `io: 12`, `api: 180`, `concurrency: 8`, `import: 70`
* *Defense:* `safety: 98`, `doc: 196`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` collections, itertools, json, numpy, os, sys, tensorflow.core.protobuf, tensorflow.python...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/lite/python/lite_v2_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.067)
- **Top Global Matches:** file_cluster_15: 7.067, file_cluster_16: 8.074, file_cluster_11: 8.48
- **Magnitude:** 3326.28 | **LOC:** 5586 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.6%), Complexity Load (formerly Cognitive Load) (71.2%), Guard Balance (formerly Safety Score) (70.5%)
- **Documentation Coverage:** 78.4017% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testQATLowBitKerasModel` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `testMlirDynamicRangeQuantization` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `testMlirDynamicRangeQuantization` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `testMultipleFunctionQuantizedModel` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `testIntegerQuantizationWithUnsupportedOps` **(Many-Argument Workhorses)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 237 instances
* *State Mutation (weighted view):* 1928
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 540`, `args: 257`, `func_start: 240`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1454`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 21`, `unreferenced_by_name: 118`
* *Architecture:* `io: 43`, `api: 238`, `concurrency: 1`, `import: 36`
* *Defense:* `safety: 9`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` absl.testing, ctypes, functools, itertools, jax, numpy, os, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.081)
- **Top Global Matches:** file_cluster_10: 8.081, file_cluster_15: 8.525, file_cluster_12: 8.755
- **Magnitude:** 3320.74 | **LOC:** 5175 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (85.9%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 98.9899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testNestedWhileLoopWithMaxItersFromOuterContextInXLAContext` **(Compute Cores)** (Impact: 22.6)
  * `_testWhileGrad_ColocateGradients` **(Stateful Encapsulated Methods)** (Impact: 20.8)
  * `testGuardedAssertDoesNotCopyWhenTrue` **(Compute Cores)** (Impact: 19.0)
  * `_runOneBenchmark` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `testInvalidMaximumIterationsWhileLoopGradientInXLAContext` **(Callbacks & Closures)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 101 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 1542
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 1232`, `args: 836`, `func_start: 476`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 15`, `state_mutation: 1340`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 34`, `unreferenced_by_name: 242`
* *Architecture:* `io: 12`, `api: 421`, `concurrency: 12`, `import: 70`
* *Defense:* `safety: 10`, `doc: 8`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` absl.testing, collections, math, numpy, re, sys, tensorflow.core.protobuf, tensorflow.python...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/framework/ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.404)
- **Top Global Matches:** file_cluster_5: 7.404, file_cluster_12: 9.228, file_cluster_0: 10.658
- **Magnitude:** 3275.36 | **LOC:** 6233 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **112** in-repo importer(s); it depends on **27**; blast radius 1.357; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 46.7327% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 531`, `dead_code: 3`, `planned_debt: 23`, `fragile_debt: 4`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 198`, `concurrency: 3`, `import: 64`
* *Defense:* `safety: 187`, `doc: 204`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.357
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.010526
  * `Imports (Out-Degree: 7):` absl, collections, collections.abc, contextlib, copy, enum, google.protobuf, numpy...
  * `Imported By (In-Degree: 112):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/tf2tensorrt/convert/convert_nodes.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.584)
- **Top Global Matches:** file_cluster_6: 6.584, file_cluster_4: 7.722, file_cluster_15: 15.349
- **Magnitude:** 3265.08 | **LOC:** 6266 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **61**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (31.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvertGraphDefToEngine` **(Many-Argument Workhorses)** (Impact: 162.8)
  * `Converter::BuildCudaEngine` **(Many-Argument Workhorses)** (Impact: 132.1)
  * `ConvertConv2DHelper` **(Many-Argument Workhorses)** (Impact: 118.1)
  * `ConvertConv3DHelper` **(Many-Argument Workhorses)** (Impact: 77.4)
  * `ConvertSegmentToGraphDef` **(Many-Argument Workhorses)** (Impact: 69.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 287 instances
* *State Mutation (weighted view):* 927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 887`, `structural_boundaries: 642`, `args: 470`, `func_start: 131`, `class_start: 1`
* *Risk/State:* `state_mutation: 353`, `dead_code: 1`, `planned_debt: 39`, `unreferenced_by_name: 30`
* *Architecture:* `import: 61`
* *Defense:* `safety: 27`, `doc: 2`, `test: 1`, `sync_locks: 1`, `immutability_locks: 474`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000632
  * `Imports (Out-Degree: 55):` container.h, flat_hash_set.h, memory.h, match.h, str_cat.h, str_format.h, string_view.h, algorithm...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tensorflow/core/tpu/graph_rewrite/distributed_tpu_rewrite_pass.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.159)
- **Top Global Matches:** file_cluster_4: 6.159, file_cluster_15: 9.813, file_cluster_16: 10.922
- **Magnitude:** 3222.54 | **LOC:** 5137 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **94**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (42.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DistributedTPURewritePass::BuildExecuteNodes` **(Many-Argument Workhorses)** (Impact: 548.6)
  * `DistributedTPURewritePass::AssignArgsAndRetvalsToCores` **(Many-Argument Workhorses)** (Impact: 357.7)
  * `DistributedTPURewritePass::BuildCompileNode` **(Many-Argument Workhorses)** (Impact: 124.0)
    * *Intent:* // Builds a TPUCompile node that compiles the bodies of the function call // `nodes`.
  * `DistributedTPURewritePass::LowerOutsideCompilationFunctionalNodes` **(Many-Argument Workhorses)** (Impact: 97.3)
  * `DistributedTPURewritePass::CopyOutsideCompilationEdges` **(Many-Argument Workhorses)** (Impact: 66.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 658
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 312`, `args: 284`, `func_start: 120`, `class_start: 14`
* *Risk/State:* `state_mutation: 258`, `planned_debt: 9`, `fragile_debt: 2`, `unreferenced_by_name: 37`
* *Architecture:* `api: 3`, `import: 94`
* *Defense:* `safety: 32`, `immutability_locks: 424`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 4.1e-05
  * `Imports (Out-Degree: 66):` container.h, btree_map.h, flat_hash_map.h, flat_hash_set.h, check.h, log.h, status.h, statusor.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/python/ops/nn_ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.917)
- **Top Global Matches:** file_cluster_4: 5.917, file_cluster_12: 10.196, file_cluster_6: 11.012
- **Magnitude:** 3141.56 | **LOC:** 6703 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Complexity Load (formerly Cognitive Load) (56.5%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 8.2e-05
  * `Imports (Out-Degree: 3):` functools, numbers, numpy, tensorflow.python.eager, tensorflow.python.framework, tensorflow.python.ops, tensorflow.python.ops.gen_nn_ops, tensorflow.python.platform...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.877)
- **Top Global Matches:** file_cluster_4: 5.877, file_cluster_6: 10.563, file_cluster_15: 11.202
- **Magnitude:** 3138.36 | **LOC:** 6120 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **89**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Debt Markers (formerly Tech Debt) (96.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.9%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetReshapeOutputType` **(Many-Argument Workhorses)** (Impact: 62.0)
  * `FullyConnectedOp::fold` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `Conv2DOp::inferReturnTypes` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `VerifyConcatenationOpTypes` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* // Verify operand types and the result type: // // 1. Operand type ranks must be equal to the output...
  * `UnidirectionalSequenceLSTMOp::inferReturnTypes` **(Many-Argument Workhorses)** (Impact: 48.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 716
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1073`, `structural_boundaries: 1297`, `args: 325`, `func_start: 228`, `class_start: 23`
* *Risk/State:* `state_mutation: 254`, `planned_debt: 35`, `unreferenced_by_name: 152`
* *Architecture:* `api: 1`, `import: 91`
* *Defense:* `safety: 41`, `doc: 29`, `sync_locks: 3`, `immutability_locks: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000131
  * `Imports (Out-Degree: 20):` Core, const_init.h, flat_hash_map.h, flat_hash_set.h, status.h, statusor.h, escaping.h, mutex.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tensorflow/core/grappler/optimizers/constant_folding.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.802)
- **Top Global Matches:** file_cluster_8: 6.802, file_cluster_6: 12.259, file_cluster_4: 20.75
- **Magnitude:** 3107.46 | **LOC:** 4134 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **44**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.0%), Guard Balance (formerly Safety Score) (59.7%)
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
* *Amplified Cascading Flux:* 214 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 666
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1036`, `structural_boundaries: 434`, `args: 269`, `func_start: 87`
* *Risk/State:* `state_mutation: 238`, `planned_debt: 11`, `fragile_debt: 1`, `unreferenced_by_name: 69`
* *Architecture:* `import: 44`
* *Defense:* `test: 3`, `immutability_locks: 351`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.027705
  * `Imports (Out-Degree: 41):` status.h, str_cat.h, string_view.h, substitute.h, algorithm, cmath, limits, allocator.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.192)
- **Top Global Matches:** file_cluster_12: 8.192, file_cluster_15: 9.685, file_cluster_13: 10.198
- **Magnitude:** 3060.14 | **LOC:** 5054 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (63.5%)
- **Documentation Coverage:** 99.7115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testConcreteFunctionStructuredSignatureError` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* # pylint: enable=g-long-lambda
  * `testConcreteFunctionFlatSignatureError` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* # pylint: enable=g-long-lambda
  * `testClone` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `testCapturesVariables` **(Compute Cores)** (Impact: 9.6)
  * `testImplementsAttributeAsNameAttrList` **(Compute Cores)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 158 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 1055
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 1249`, `args: 672`, `func_start: 570`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 1`, `state_mutation: 739`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 71`, `unreferenced_by_name: 239`
* *Architecture:* `io: 7`, `api: 487`, `concurrency: 9`, `import: 75`
* *Defense:* `safety: 5`, `doc: 6`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 8.2e-05
  * `Imports (Out-Degree: 15):` absl.testing, collections, dataclasses, functools, itertools, multiprocessing.pool, numpy, pickle...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tensorflow/lite/delegates/gpu/common/tasks/conv_generic.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.522)
- **Top Global Matches:** file_cluster_6: 6.522, file_cluster_4: 9.804, file_cluster_8: 16.102
- **Magnitude:** 2989.16 | **LOC:** 2055 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvGeneric::GuessBestParams` **(Many-Argument Workhorses)** (Impact: 529.9)
  * `ConvGeneric::GenerateConv` **(Many-Argument Workhorses)** (Impact: 492.6)
  * `GetConvParamsForA7A8` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `GetConvParamsForA9AndHigher` **(Many-Argument Workhorses)** (Impact: 80.2)
  * `GenerateBlockCoords` **(Many-Argument Workhorses)** (Impact: 76.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 440 instances
* *State Mutation (weighted view):* 1402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 66`, `args: 96`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `state_mutation: 522`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 249`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000124
  * `Imports (Out-Degree: 11):` substitute.h, algorithm, string, data_type.h, shape.h, status.h, util.h, work_group_picking.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tensorflow/python/framework/test_util.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.122)
- **Top Global Matches:** file_cluster_5: 7.122, file_cluster_12: 9.286, file_cluster_7: 11.363
- **Magnitude:** 2953.56 | **LOC:** 4313 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **118** in-repo importer(s); it depends on **40**; blast radius 0.996; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%), Connectivity (formerly Api Exposure) (65.1%)
- **Documentation Coverage:** 56.8928% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 331`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 205`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 112`, `doc: 138`, `test: 18`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.996
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.00506
  * `Imports (Out-Degree: 14):` absl.testing, collections, collections.abc, contextlib, functools, gc, google.protobuf, itertools...
  * `Imported By (In-Degree: 118):` (Excluded from Brief to save tokens)

### `tensorflow/compiler/tf2tensorrt/convert/convert_nodes_test.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.758)
- **Top Global Matches:** file_cluster_4: 6.758, file_cluster_15: 10.955, file_cluster_16: 11.995
- **Magnitude:** 2926.06 | **LOC:** 9952 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **63**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.5%), Guard Balance (formerly Safety Score) (53.8%), Debt Markers (formerly Tech Debt) (30.4%), Complexity Load (formerly Cognitive Load) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OpConverter_Select::RunTest` **(Many-Argument Workhorses)** (Impact: 173.4)
  * `ConvertRange` **(Many-Argument Workhorses)** (Impact: 96.0)
  * `TestMatMulHelper` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* // Helper function for testing MatMul and BatchMatMul. get_matmul is a function // used to generate ...
  * `ConvertPool` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `RunTests` **(Compute Cores)** (Impact: 46.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 872
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 681`, `structural_boundaries: 706`, `args: 383`, `func_start: 172`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 354`, `planned_debt: 12`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 65`
* *Architecture:* `api: 11`, `import: 63`
* *Defense:* `safety: 23`, `test: 187`, `immutability_locks: 363`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` Core, container.h, call_once.h, inlined_vector.h, match.h, numbers.h, str_cat.h, str_format.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/compiler/mlir/tosa/transforms/legalize_common.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.704)
- **Top Global Matches:** file_cluster_6: 5.704, file_cluster_8: 12.31, file_cluster_4: 12.476
- **Magnitude:** 2864.76 | **LOC:** 5064 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **37**; blast radius 0.024; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (56.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertStridedSliceOp` **(Many-Argument Workhorses)** (Impact: 234.5)
    * *Intent:* // Lowers StridedSlice to a sequence of TOSA ops.
  * `convertResizeOp` **(Many-Argument Workhorses)** (Impact: 133.4)
    * *Intent:* // Lowers ResizeBilinear and ResizeNearestNeighbor to TOSA resize.
  * `convertPackOp` **(Many-Argument Workhorses)** (Impact: 92.9)
    * *Intent:* // Lowers the Pack operator to TOSA.
  * `convertReduceOpCommon` **(Many-Argument Workhorses)** (Impact: 85.7)
    * *Intent:* // Common function for lowering reduce operations to TOSA ops. // Nan propagation mode is only appli...
  * `convertGatherOp` **(Many-Argument Workhorses)** (Impact: 83.4)
    * *Intent:* // Lowers Gather operators to a sequence of TOSA ops.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 322 instances
* *State Mutation (weighted view):* 1039
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 693`, `args: 74`, `func_start: 57`
* *Risk/State:* `state_mutation: 395`, `dead_code: 24`, `planned_debt: 2`, `unreferenced_by_name: 42`
* *Architecture:* `import: 38`
* *Defense:* `safety: 66`, `doc: 6`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000147
  * `Imports (Out-Degree: 5):` algorithm, climits, cmath, cstddef, cstdint, iterator, limits, ArrayRef.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tensorflow/python/feature_column/feature_column_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.042)
- **Top Global Matches:** file_cluster_15: 9.042, file_cluster_16: 9.231, file_cluster_12: 9.742
- **Magnitude:** 2855.92 | **LOC:** 6662 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (99.5%), Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 94.1846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_dense_tensor` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `test_get_dense_tensor` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `_test_input_layer` **(Stateful Encapsulated Methods)** (Impact: 14.3)
  * `test_linear_model` **(I/O & Config Routines)** (Impact: 8.7)
  * `test_keras_linear_model` **(I/O & Config Routines)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 1297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 1108`, `args: 416`, `func_start: 412`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 53`, `state_mutation: 1225`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 61`, `unreferenced_by_name: 135`
* *Architecture:* `api: 375`, `import: 33`
* *Defense:* `safety: 2`, `doc: 23`, `test: 354`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` absl.testing, collections, copy, numpy, tensorflow.core.example, tensorflow.core.protobuf, tensorflow.python.client, tensorflow.python.eager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/python/saved_model/load_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.916)
- **Top Global Matches:** file_cluster_15: 6.916, file_cluster_12: 7.016, file_cluster_16: 7.66
- **Magnitude:** 2843.76 | **LOC:** 3587 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (64.0%)
- **Documentation Coverage:** 49.5876% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_deferred_init_module_variables` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* """Defer initialization of variables in a module to the load stage."""
  * `test_concrete_function_captures` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* # TODO(b/264869228) Fix LoadTest if use_cpp_bindings: self.skipTest("Not implemented for cpp.") clas...
  * `test_functions_list` **(Stateful Encapsulated Methods)** (Impact: 15.2)
    * *Intent:* # TODO(b/264869228) Fix LoadTest if use_cpp_bindings: self.skipTest("Not implemented for cpp.") root...
  * `test_positional_arguments` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* # TODO(b/264869228) Fix LoadTest if use_cpp_bindings: self.skipTest("Not implemented for cpp.") def ...
  * `test_function_with_default_none_input` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* # imported.signatures with defaults are not supported. # TODO(b/277814477) support defaults in loade...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 274 instances
* *State Mutation (weighted view):* 1235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 634`, `args: 297`, `func_start: 260`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 687`, `planned_debt: 126`, `duplicate_logic: 26`, `unreferenced_by_name: 123`
* *Architecture:* `io: 33`, `api: 220`, `import: 61`
* *Defense:* `safety: 5`, `doc: 5`, `test: 132`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` absl.testing, collections, contextlib, functools, gc, io, numpy, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tensorflow/core/util/example_proto_fast_parsing.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.98)
- **Top Global Matches:** file_cluster_6: 5.98, file_cluster_4: 11.733, file_cluster_8: 13.588
- **Magnitude:** 2812.96 | **LOC:** 3108 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **27**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FastParseSerializedExample` **(Many-Argument Workhorses)** (Impact: 392.1)
  * `FastParseSingleExample` **(Many-Argument Workhorses)** (Impact: 215.9)
  * `FastParseExample` **(Many-Argument Workhorses)** (Impact: 143.0)
  * `ParseSequenceDenseFeatures` **(Many-Argument Workhorses)** (Impact: 133.6)
    * *Intent:* // Parses dense features in `sequence_features`, and writes their parsed // values to `sequence_resu...
  * `ParseSequenceRaggedFeatures` **(Many-Argument Workhorses)** (Impact: 125.9)
    * *Intent:* // Parses ragged features in `sequence_features`, and writes their parsed // values to `sequence_res...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 832
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 703`, `structural_boundaries: 397`, `args: 96`, `func_start: 71`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 314`, `planned_debt: 15`, `unreferenced_by_name: 6`
* *Architecture:* `api: 3`, `import: 27`
* *Defense:* `safety: 1`, `immutability_locks: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.025159
  * `Imports (Out-Degree: 17):` casts.h, flat_hash_map.h, status.h, substitute.h, algorithm, functional, optional, example.pb.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tensorflow/python/eager/pywrap_tfe_src.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.045)
- **Top Global Matches:** file_cluster_4: 8.045, file_cluster_15: 10.178, file_cluster_16: 11.4
- **Magnitude:** 2779.0 | **LOC:** 4259 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **61**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.6%), Debt Markers (formerly Tech Debt) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MakeIntList` **(Compute Cores)** (Impact: 440.1)
  * `SetOpAttrList` **(Many-Argument Workhorses)** (Impact: 118.4)
  * `TFE_Py_FastPathExecute_C` **(Compute Cores)** (Impact: 104.9)
  * `SetOpAttrScalar` **(Many-Argument Workhorses)** (Impact: 101.0)
  * `RecordGradient` **(Many-Argument Workhorses)** (Impact: 88.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 199 instances
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 549`, `args: 291`, `func_start: 190`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 216`, `planned_debt: 11`, `unreferenced_by_name: 59`
* *Architecture:* `api: 10`, `import: 61`
* *Defense:* `safety: 38`, `test: 3`, `sync_locks: 3`, `immutability_locks: 174`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000281
  * `Imports (Out-Degree: 44):` flat_hash_map.h, leak_check.h, status.h, str_cat.h, string_view.h, span.h, atomic, cstdint...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tensorflow/core/grappler/optimizers/remapper.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.83)
- **Top Global Matches:** file_cluster_6: 5.83, file_cluster_4: 10.908, file_cluster_8: 14.369
- **Magnitude:** 2737.48 | **LOC:** 5411 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Mutation Surface (formerly State Flux) (22.4%), Complexity Load (formerly Cognitive Load) (18.8%)
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
* *Structure:* `branch: 896`, `structural_boundaries: 737`, `args: 226`, `func_start: 109`, `class_start: 14`
* *Risk/State:* `state_mutation: 133`, `planned_debt: 20`, `unreferenced_by_name: 1`
* *Architecture:* `import: 31`
* *Defense:* `immutability_locks: 428`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 4.1e-05
  * `Imports (Out-Degree: 27):` flat_hash_set.h, algorithm, cstdlib, map, set, string, tensor_shape.h, versions.pb.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tensorflow/lite/delegates/gpu/common/task/tensor_desc.h` (CPP) | Magnitude: 214.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 296, immutability_locks: 139, structural_boundaries: 77, args: 59
- `tensorflow/core/kernels/dense_update_functor_gpu.cu.cc` (CPP) | Magnitude: 7.62 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 27, args: 15, indent_spaces: 15, macros: 7
- `tensorflow/core/util/ragged_to_dense_util.h` (CPP) | Magnitude: 3.88 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, args: 7, immutability_locks: 7, import: 6
- `tensorflow/core/kernels/population_count_op.h` (CPP) | Magnitude: 15.3 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, import: 3, macros: 2, indent_spaces: 2
- `tensorflow/core/kernels/relu_op.cc` (CPP) | Magnitude: 7.38 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 80, args: 42, explicit_casts: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tensorflow/core/common_runtime/request_cost_accessor_registry_test.cc` (CPP) | Magnitude: 7.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, test: 5, args: 4
- `tensorflow/lite/kernels/internal/quantization_util_test.cc` (CPP) | Magnitude: 111.32 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 392, test: 212, explicit_casts: 111, args: 109
- `tensorflow/compiler/mlir/quantization/stablehlo/cc/calibration/statistics.cc` (CPP) | Magnitude: 23.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, import: 20, structural_boundaries: 15, core_var_decl: 9
- `tensorflow/core/kernels/numeric_options_utils.h` (CPP) | Magnitude: 5.44 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, import: 4, core_var_decl: 3
- `tensorflow/lite/kernels/eigen_support_test.cc` (CPP) | Magnitude: 41.08 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 103, pointers: 48, test: 38, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tensorflow/core/tpu/kernels/tpu_program_group.h` (CPP) | Magnitude: 26.14 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 81, immutability_locks: 45, args: 25, structural_boundaries: 22
- `tensorflow/lite/delegates/telemetry_test.cc` (CPP) | Magnitude: 46.68 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 73, test: 24, pointers: 17, core_var_decl: 15
- `tensorflow/core/distributed_runtime/eager/remote_mgr_test.cc` (CPP) | Magnitude: 33.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 113, pointers: 30, core_var_decl: 25, design_snake_case: 25
- `tensorflow/lite/kernels/hashtable_find.cc` (CPP) | Magnitude: 14.26 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, pointers: 24, structural_boundaries: 10, immutability_locks: 10
- `tensorflow/c/experimental/gradients/nn_grad_test.cc` (CPP) | Magnitude: 44.98 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 135, args: 25, test: 16, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tensorflow/python/framework/extension_type.py` (PYTHON) | Magnitude: 754.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 679, structural_boundaries: 241, branch: 149, state_mutation: 120
- `tensorflow/lite/kernels/ctc/ctc_beam_search_decoder.cc` (CPP) | Magnitude: 120.88 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 165, core_var_decl: 45, design_snake_case: 43, pointers: 35
- `tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py` (PYTHON) | Magnitude: 139.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 234, core_var_decl: 78, design_snake_case: 72, state_mutation: 67
- `tensorflow/lite/java/ovic/demo/app/OvicBenchmarkerActivity.java` (JAVA) | Magnitude: 118.78 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 62, core_var_decl: 54, design_camel_case: 38
- `tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py` (PYTHON) | Magnitude: 74.9 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 38, core_var_decl: 29, design_snake_case: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tensorflow/python/data/experimental/kernel_tests/wrap_unwrap_test.py` (PYTHON) | Magnitude: 28.98 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 21, state_mutation: 14, core_var_decl: 14
- `tensorflow/tools/graph_transforms/flatten_atrous_test.cc` (CPP) | Magnitude: 0.01 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 61, pointers: 14, args: 11, import: 11
- `tensorflow/lite/delegates/gpu/gl/kernels/max_unpooling_test.cc` (CPP) | Magnitude: 17.06 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 13, structural_boundaries: 6, import: 6
- `tensorflow/compiler/mlir/tf2xla/internal/clustering_bridge_passes_test.cc` (CPP) | Magnitude: 4.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, test: 4, import: 3
- `tensorflow/lite/g3doc/api_docs/c/struct/tf-lite-dimension-metadata.html` (HTML) | Magnitude: 22.64 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 25, io: 20, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tensorflow/python/types/distribute.py` (PYTHON) | Magnitude: 38.44 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 25, doc: 15, api: 14
- `tensorflow/tools/ci_build/linux/rocm/run_gpu_single.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, core_var_decl: 9, design_upper_case: 9
- `tensorflow/python/dlpack/dlpack.py` (PYTHON) | Magnitude: 7.0 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 3, import: 3, indent_spaces: 3
- `tensorflow/compiler/tests/listdiff_op_test.py` (PYTHON) | Magnitude: 82.48 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 26, core_var_decl: 23, design_snake_case: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tensorflow/core/distributed_runtime/worker_interface.h` (CPP) | Magnitude: 54.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 66, args: 33, immutability_locks: 32
- `tensorflow/core/graph/graph.h` (CPP) | Magnitude: 288.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 420, structural_boundaries: 240, immutability_locks: 237, func_start: 125
- `tensorflow/lite/kernels/cpu_backend_gemm_ruy.h` (CPP) | Magnitude: 35.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 35, pointers: 23, immutability_locks: 14
- `tensorflow/python/ops/control_flow_ops_benchmark.py` (PYTHON) | Magnitude: 59.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 40, state_mutation: 20, core_var_decl: 16
- `tensorflow/compiler/mlir/tensorflow/transforms/replicate_to_island.cc` (CPP) | Magnitude: 140.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 50, branch: 34, import: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tensorflow/python/ops/ragged/ragged_tensor.py` (PYTHON) | Magnitude: 1664.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1195, core_var_decl: 429, design_snake_case: 426, structural_boundaries: 378
- `tensorflow/python/framework/constant_tensor_conversion.py` (PYTHON) | Magnitude: 3.96 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, core_var_decl: 3, import: 2
- `tensorflow/python/checkpoint/benchmarks_test.py` (PYTHON) | Magnitude: 60.4 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 42, core_var_decl: 15, design_snake_case: 15
- `tensorflow/python/data/experimental/benchmarks/csv_dataset_benchmark.py` (PYTHON) | Magnitude: 94.02 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 80, core_var_decl: 42, design_snake_case: 40, structural_boundaries: 26
- `tensorflow/compiler/tests/rmsprop_test.py` (PYTHON) | Magnitude: 71.1 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, core_var_decl: 37, design_snake_case: 37, state_mutation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tensorflow/core/profiler/lib/context_types.h` (CPP) | Magnitude: 5.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, import: 3, func_start: 2
- `tensorflow/lite/profiling/telemetry/telemetry_test.cc` (CPP) | Magnitude: 17.1 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, args: 14, test: 12, import: 10
- `tensorflow/lite/delegates/coreml/builders/softmax_op_builder.h` (CPP) | Magnitude: 3.0 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, import: 5, safety: 4
- `tensorflow/core/grappler/optimizers/evaluation_utils_test.cc` (CPP) | Magnitude: 10.44 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, test: 9, import: 7, structural_boundaries: 4
- `tensorflow/lite/delegates/gpu/gl/kernels/test_util.h` (CPP) | Magnitude: 4.46 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, import: 11, immutability_locks: 8, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tensorflow/core/common_runtime/next_pluggable_device/direct_plugin_variable.cc` (CPP) | Magnitude: 3.38 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 3, indent_spaces: 2, structural_boundaries: 1, args: 1
- `tensorflow/core/tpu/kernels/sparse_core_ops_utils_test.cc` (CPP) | Magnitude: 7.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 15, design_snake_case: 15, test: 6
- `tensorflow/core/grappler/utils/tpu_test.cc` (CPP) | Magnitude: 7.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, pointers: 9, args: 6, test: 6
- `tensorflow/compiler/mlir/lite/utils/stateful_ops_utils.cc` (CPP) | Magnitude: 7.22 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 5, indent_spaces: 5, branch: 1
- `tensorflow/core/kernels/mfcc_dct_test.cc` (CPP) | Magnitude: 10.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, test: 9, import: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tensorflow/core/kernels/random_binomial_op.cc` (CPP) | Magnitude: 292.12 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 356, core_var_decl: 85, design_snake_case: 80, structural_boundaries: 60
- `tensorflow/core/kernels/linalg/matrix_diag_op.cc` (CPP) | Magnitude: 212.82 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 403, core_var_decl: 95, design_snake_case: 93, immutability_locks: 71
- `tensorflow/lite/java/src/main/native/nativeinterpreterwrapper_jni.cc` (CPP) | Magnitude: 351.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 427, structural_boundaries: 116, branch: 98, pointers: 81
- `tensorflow/core/kernels/segment_reduction_ops_impl.h` (CPP) | Magnitude: 602.94 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 982, structural_boundaries: 370, core_var_decl: 207, design_snake_case: 189
- `tensorflow/lite/kernels/add_test.cc` (CPP) | Magnitude: 696.6 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 843, core_var_decl: 207, design_snake_case: 187, explicit_casts: 176

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tensorflow/lite/tools/benchmark/experimental/delegate_performance/android/src/main/java/org/tensorflow/lite/benchmark/delegateperformance/ModelBenchmarkReport.java` (JAVA) | Magnitude: 0.11 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 35, core_var_decl: 28, state_mutation: 21
- `tensorflow/lite/delegates/gpu/gl/gl_buffer.h` (CPP) | Magnitude: 78.58 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 68, args: 44, immutability_locks: 35
- `tensorflow/dtensor/python/dtensor_device.py` (PYTHON) | Magnitude: 222.86 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 208, structural_boundaries: 74, branch: 36, state_mutation: 36
- `tensorflow/java/src/main/java/org/tensorflow/op/NameScope.java` (JAVA) | Magnitude: 49.9 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 18, safety_bypasses: 11, branch: 10
- `ci/official/utilities/convert_msys_paths_to_win_paths.py` (PYTHON) | Magnitude: 38.52 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, branch: 11, structural_boundaries: 9, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tensorflow/lite/kernels/transpose_conv.cc` (CPP) | Magnitude: 550.48 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 714, pointers: 317, branch: 118, state_mutation: 113
- `tensorflow/lite/tools/optimize/calibration/builtin_logging_ops/lstm.cc` (CPP) | Magnitude: 0.37 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 506, immutability_locks: 136, core_var_decl: 79, design_snake_case: 79
- `tensorflow/python/framework/graph_to_function_def.py` (PYTHON) | Magnitude: 216.86 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 96, branch: 40, state_mutation: 36, structural_boundaries: 29
- `tensorflow/lite/delegates/gpu/common/tasks/conv_constants.cc` (CPP) | Magnitude: 314.36 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 224, branch: 55, state_mutation: 53, core_var_decl: 45
- `tensorflow/lite/tools/utils.cc` (CPP) | Magnitude: 0.17 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 163, branch: 50, structural_boundaries: 50, explicit_casts: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tensorflow/lite/java/ovic/src/main/java/org/tensorflow/ovic/OvicBenchmarker.java` (JAVA) | Magnitude: 55.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 56, api: 19, structural_boundaries: 18, core_var_decl: 18
- `tensorflow/python/autograph/utils/testing.py` (PYTHON) | Magnitude: 161.32 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 40, state_mutation: 26, args: 18
- `tensorflow/core/common_runtime/next_pluggable_device/c/tf_device_context_c_api_helper.cc` (CPP) | Magnitude: 20.48 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 47, pointers: 16, structural_boundaries: 15, import: 13
- `tensorflow/tools/ci_build/builds/with_the_same_user` (SHELL) | Magnitude: 0.03 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 23, branch: 11, io: 7
- `tensorflow/python/feature_column/feature_column_v2_types.py` (PYTHON) | Magnitude: 38.9 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 26, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tensorflow/python/checkpoint/checkpoint_options.py` (PYTHON) | Magnitude: 40.96 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 16, state_mutation: 9, core_var_decl: 8
- `tensorflow/lite/kernels/internal/reference/log_softmax.h` (CPP) | Magnitude: 136.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 170, core_var_decl: 71, design_snake_case: 58, immutability_locks: 57
- `tensorflow/lite/experimental/shlo/ops/benchmark_util.h` (CPP) | Magnitude: 13.84 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, args: 9, structural_boundaries: 8, import: 8
- `tensorflow/lite/testing/generate_testspec.cc` (CPP) | Magnitude: 102.46 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 31, branch: 25, immutability_locks: 25
- `tensorflow/lite/kernels/internal/strided_slice_logic.h` (CPP) | Magnitude: 242.32 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 164, state_mutation: 51, core_var_decl: 45, design_snake_case: 45

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tensorflow/lite/delegates/xnnpack/weight_cache.cc` -> Churn: **76.02%** | Cog Load: 21.6143% | Debt: 94.8113%
- `tensorflow/compiler/mlir/lite/ir/tfl_ops.cc` -> Churn: **71.94%** | Cog Load: 35.2159% | Debt: 96.7547%
- `tensorflow/core/kernels/batching_util/batch_resource_base.cc` -> Churn: **61.99%** | Cog Load: 57.4866% | Debt: 55.576%
- `tensorflow/core/framework/op_kernel.cc` -> Churn: **58.45%** | Cog Load: 22.8177% | Debt: 90.4784%
- `tensorflow/lite/core/api/flatbuffer_conversions.cc` -> Churn: **55.68%** | Cog Load: 84.8128% | Debt: 32.9851%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tensorflow/python/ops/image_ops_test.py` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 5137.28
- `tensorflow/core/grappler/optimizers/constant_folding.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 3107.46
- `tensorflow/core/grappler/optimizers/remapper.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2737.48
- `tensorflow/core/grappler/optimizers/arithmetic_optimizer.cc` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2475.5
- `tensorflow/python/ops/image_ops_impl.py` -> **A. Unique TensorFlower** (100.0% isolated ownership) | Magnitude: 2233.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tensorflow/core/framework/types.cc` -> **Severity: 5.191** (Embedded: 0.0803 * Error Risk: 64.605%)
- `tensorflow/core/framework/tensor_shape.h` -> **Severity: 4.889** (Embedded: 0.0955 * Error Risk: 51.1698%)
- `tensorflow/core/tfrt/mlrt/bytecode/span.h` -> **Severity: 4.834** (Embedded: 0.0942 * Error Risk: 51.333%)
- `tensorflow/tools/android/test/jni/object_tracking/logging.cc` -> **Severity: 4.728** (Embedded: 0.0717 * Error Risk: 65.9421%)
- `tensorflow/core/framework/tensor.h` -> **Severity: 4.626** (Embedded: 0.0926 * Error Risk: 49.9364%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tensorflow/lite/core/c/common.h` -> **Severity: 747.3** (Blast Radius: 7.473 * Doc Risk: 100.0%)
- `tensorflow/core/ir/types/dialect.h` -> **Severity: 543.1** (Blast Radius: 5.431 * Doc Risk: 100.0%)
- `tensorflow/core/framework/op_kernel.h` -> **Severity: 432.9** (Blast Radius: 4.329 * Doc Risk: 100.0%)
- `tensorflow/core/framework/types.h` -> **Severity: 392.8** (Blast Radius: 3.928 * Doc Risk: 100.0%)
- `tensorflow/compiler/mlir/tf2xla/internal/test_matchers_test.cc` -> **Severity: 355.5** (Blast Radius: 3.555 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2409 literal sites + 38 sites through wrappers = 2447
- **`memory_alloc`:** 4806 literal sites + 1708 sites through wrappers = 6514
- **`panics_and_aborts`:** 7499 literal sites + 16 sites through wrappers = 7515

- `ScheduleTask` (function, memory_alloc, primitive): 150 call sites in 1 files -- `tensorflow/core/kernels/batching_util/shared_batch_scheduler_test.cc`
- `TFE_NewContextOptions` (function, memory_alloc, primitive): 112 call sites in 25 files -- `tensorflow/c/eager/c_api.cc`
- `TfLiteModelCreateFromFile` (function, memory_alloc, primitive): 56 call sites in 11 files -- `tensorflow/lite/core/c/c_api.cc`
- `TF_NewBuffer` (function, memory_alloc, primitive): 44 call sites in 16 files -- `tensorflow/c/tf_buffer.cc`
- `TF_NewGraph` (function, memory_alloc, primitive): 38 call sites in 11 files -- `tensorflow/c/c_api.cc`
- `VALIDATE` (macro, memory_alloc, primitive): 35 call sites in 1 files -- `tensorflow/core/framework/op_def_util.cc`
- `TF_TensorFromTensor` (function, memory_alloc, primitive): 34 call sites in 9 files -- `tensorflow/c/tf_tensor.cc`
- `ScheduleTask` (function, memory_alloc, primitive): 33 call sites in 1 files -- `tensorflow/core/kernels/batching_util/adaptive_shared_batch_scheduler_test.cc`
- `SetGraph` (function, memory_alloc, primitive): 33 call sites in 1 files -- `tensorflow/lite/arena_planner_test.cc`
- `TF_NewOperation` (function, memory_alloc, via TF_NewOperationLocked): 30 call sites in 11 files -- `tensorflow/c/c_api.cc`
- `KeyFoo` (function, memory_alloc, primitive): 29 call sites in 1 files -- `tensorflow/core/framework/rendezvous_test.cc`
- `AssignCustomAllocForTensor` (function, memory_alloc, via NewCustomAlloc): 21 call sites in 1 files -- `tensorflow/lite/interpreter_test.cc`
*(+386 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 832736 call pairs -- scoped 19.9%, unique 3.7%, ambiguous 33.6%, external 42.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 561999 | 19.7% | 5.3% | 33.1% | 41.9% |
| python | 257564 | 20.2% | 0.0% | 35.5% | 44.4% |
| java | 6425 | 32.6% | 1.9% | 20.6% | 45.0% |
| objective-c | 2261 | 8.5% | 13.1% | 38.2% | 40.1% |
| shell | 2150 | 8.0% | 0.4% | 1.4% | 90.1% |
| go | 1510 | 23.2% | 11.9% | 8.8% | 56.1% |
| swift | 332 | 9.6% | 12.3% | 14.5% | 63.6% |
| c | 313 | 8.0% | 54.0% | 1.3% | 36.7% |
| csharp | 94 | 37.2% | 0.0% | 13.8% | 48.9% |
| ruby | 64 | 0.0% | 0.0% | 0.0% | 100.0% |

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
