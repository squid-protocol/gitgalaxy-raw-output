# ARCHITECTURAL_BRIEF: wgpu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/wgpu` |
| **Timestamp** | `2026-08-03T19:48:03.259717+00:00` |
| **Scan Duration** | `4.87s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `41bb9cbd25fca25b398c0ccb203164fe1ff8c0b8` |
| **Git Remote** | `https://github.com/gfx-rs/wgpu.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 810 malicious artifacts.

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
| Total Artifacts | 2230 |
| Analyzed Artifacts (Scanned) | 862 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1368 |
| Total LOC | 218916 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 38.7% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8646 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4424 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8667 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 750 | 216470 | 87.0% |
| GLSL | 51 | 1121 | 5.9% |
| MARKDOWN | 47 | 0 | 5.5% |
| JAVASCRIPT | 4 | 1005 | 0.5% |
| BINARY_THREAT | 4 | 4 | 0.5% |
| HTML | 2 | 186 | 0.2% |
| YAML | 1 | 13 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |
| SHELL | 1 | 21 | 0.1% |
| JSON | 1 | 96 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.787`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 439 | 50.9% |
| file_cluster_0 | 205 | 23.8% |
| file_cluster_16 | 97 | 11.3% |
| file_cluster_13 | 63 | 7.3% |
| file_cluster_4 | 4 | 0.5% |
| Unknown | 4 | 0.5% |
| file_cluster_17 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 48 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1368*

**Composition by Extension & Reason:**
- `.wgsl`: 197x Excluded (Unsupported Extension: '.wgsl'), 166x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 54x Unsupported Format (.wgsl)
- `.toml`: 164x Excluded (Unsupported Extension: '.toml'), 30x Unsupported Format (.toml), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.spvasm`: 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 30x Excluded (Unsupported Extension: '.spvasm')
- `.ron`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Unsupported Extension: '.ron')
- `.metal`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.metal'), 1x Unsupported Format (.metal)
- `.glsl`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hlsl`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.hlsl')
- `.png`: 40x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5504 LOC)
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.apache`: 9x Excluded (Unsupported Extension: '.APACHE'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mit`: 9x Excluded (Unsupported Extension: '.MIT'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4596 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ktx2`: 4x Excluded (Binary Format Detected)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.2 | 8.5 | 5.2 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 25.7 | 25.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.0 | 3.3 | 3.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.7 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 95.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.7 | 1.0 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 15.9 | 5.5 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.8 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 48.3 | 26.4 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 6.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cts_runner/src/main.rs` (Hits: 6)
- `tests/tests/wgpu-gpu/passthrough/mod.rs` (Hits: 6)
- `wgpu-core/src/device/trace/record.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **iter.rs** (`benches/src/iter.rs`) — 14 inbound connections
2. **format.rs** (`wgpu-types/src/texture/format.rs`) — 12 inbound connections
3. **id.rs** (`wgpu-core/src/id.rs`) — 8 inbound connections
4. **ir.rs** (`naga/fuzz/fuzz_targets/ir.rs`) — 7 inbound connections
5. **fs.rs** (`naga/xtask/src/fs.rs`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`wgpu/src/lib.rs`) — 140 outbound dependencies
2. **mod.rs** (`wgpu/src/backend/webgpu/webgpu_sys/mod.rs`) — 129 outbound dependencies
3. **resource.rs** (`wgpu-core/src/device/resource.rs`) — 117 outbound dependencies
4. **mod.rs** (`wgpu-core/src/command/mod.rs`) — 115 outbound dependencies
5. **render.rs** (`wgpu-core/src/command/render.rs`) — 103 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `variable_updating_statement` (@ `naga/src/front/wgsl/parse/mod.rs`) -> Impact: **7191.1** | LOC: 1267
- `write_stmt` (@ `naga/src/back/hlsl/writer.rs`) -> Impact: **7127.2** | LOC: 1049
- `write_function` (@ `naga/src/back/wgsl/writer.rs`) -> Impact: **4015.5** | LOC: 1265
  * *Intent:* /// Helper method used to write /// [functions](https://gpuweb.github.io/gpuweb/wgsl/#functions)
- `put_access_chain` (@ `naga/src/back/msl/writer.rs`) -> Impact: **3747.1** | LOC: 1212
- `binary` (@ `naga/src/front/wgsl/lower/mod.rs`) -> Impact: **3379.0** | LOC: 1172
- `write_function` (@ `naga/src/back/spv/writer.rs`) -> Impact: **3092.0** | LOC: 1256
- `validate_module_handles` (@ `naga/src/valid/handles.rs`) -> Impact: **2737.8** | LOC: 716
  * *Intent:* /// * Valid, in the sense that they contain indices within each arena structure inside the /// [`crate::Module`] type. /// * No arena contents contain...
- `try_eval_and_append` (@ `naga/src/proc/constant_evaluator.rs`) -> Impact: **2284.4** | LOC: 921
  * *Intent:* // "See through" the constant and use its initializer.
- `put_restricted_texel_address` (@ `naga/src/back/msl/writer.rs`) -> Impact: **2259.8** | LOC: 787
- `create_surface_from_context` (@ `wgpu/src/backend/webgpu.rs`) -> Impact: **1731.1** | LOC: 1358

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `new` (@ `benches/benches/wgpu-benchmark/computepass.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Create and prepare all the resources needed for the computepass benchmark.
- `new` (@ `benches/benches/wgpu-benchmark/renderpass.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Create and prepare all the resources needed for the renderpass benchmark.
- `fmt` (@ `naga/src/back/glsl/mod.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// List of immediate data items in the shader.
- `write_stmt` (@ `naga/src/back/hlsl/writer.rs`) -> **O(2^N) [Recursive]**
- `write` (@ `naga/src/back/hlsl/writer.rs`) -> **O(2^N) [Recursive]**
- `try_fmt` (@ `naga/src/back/msl/mod.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Four half-precision floats (no Rust equiv). `vec4<f32>` in shaders.
- `put_access_chain` (@ `naga/src/back/msl/writer.rs`) -> **O(2^N) [Recursive]**
- `filter_emits_in_block` (@ `naga/src/back/pipeline_constants.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* *expr = new_pos[*expr];
- `write_access_chain` (@ `naga/src/back/spv/block.rs`) -> **O(2^N) [Recursive]**
- `write_conditional_indexed_load` (@ `naga/src/back/spv/index.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ready_for_compaction` (@ `wgpu/src/backend/wgpu_core.rs`) -> DB Complexity: **120**
- `variable_updating_statement` (@ `naga/src/front/wgsl/parse/mod.rs`) -> DB Complexity: **119**
- `binary` (@ `naga/src/front/wgsl/lower/mod.rs`) -> DB Complexity: **78**
- `all_tests` (@ `tests/tests/wgpu-gpu/main.rs`) -> DB Complexity: **78**
- `adjust_stmt` (@ `naga/src/back/pipeline_constants.rs`) -> DB Complexity: **76**
- `adjust_body` (@ `naga/src/compact/statements.rs`) -> DB Complexity: **65**
  * *Intent:* /// Adjust statements in the body of `function`. /// /// Adjusts expressions using `self.expressions`, and adjusts calls to other /// functions using ...
- `create_image_without_memory` (@ `wgpu-hal/src/vulkan/device.rs`) -> DB Complexity: **65**
- `expose` (@ `wgpu-hal/src/dx12/adapter.rs`) -> DB Complexity: **64**
- `end_encoding` (@ `wgpu-hal/src/vulkan/command.rs`) -> DB Complexity: **64**
- `write_access_chain` (@ `naga/src/back/spv/block.rs`) -> DB Complexity: **61**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `naga/src/back/hlsl` | 8 | 19899.96 | 13.52% | 37.9% |
| `wgpu/src/backend/webgpu/webgpu_sys` | 128 | 10730.99 | 2.24% | 4.21% |
| `wgpu-core/src/command` | 20 | 10587.58 | 9.05% | 36.86% |
| `naga/src/front/wgsl/parse` | 6 | 10540.2 | 12.38% | 17.63% |
| `naga/src/back/spv` | 13 | 10165.16 | 14.23% | 53.79% |
| `naga/src/front/wgsl/lower` | 4 | 8844.8 | 18.26% | 37.35% |
| `naga/src/proc` | 10 | 8643.34 | 10.74% | 34.83% |
| `naga/src/back/msl` | 4 | 8516.9 | 8.48% | 50.57% |
| `wgpu-core/src` | 24 | 8502.24 | 9.6% | 51.33% |
| `naga/src/valid` | 8 | 7561.44 | 12.24% | 23.28% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `deno_webgpu/command_buffer.rs` -> **100.0%** Exposure
- `deno_webgpu/compute_pipeline.rs` -> **100.0%** Exposure
- `deno_webgpu/error.rs` -> **100.0%** Exposure
- `deno_webgpu/query_set.rs` -> **100.0%** Exposure
- `deno_webgpu/sampler.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `naga/src/back/continue_forward.rs` -> **100.0%** Exposure
- `naga/src/common/wgsl/types.rs` -> **100.0%** Exposure
- `naga/src/compact/functions.rs` -> **100.0%** Exposure
- `naga/src/proc/terminator.rs` -> **100.0%** Exposure
- `wgpu-core/src/command/encoder.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wgpu/src/backend/webgpu.rs` -> **27** Orphaned Functions | **71** Duplicates
- `naga/src/back/spv/instructions.rs` -> **89** Orphaned Functions | **3** Duplicates
- `deno_webgpu/01_webgpu.js` -> **17** Orphaned Functions | **45** Duplicates
- `examples/standalone/custom_backend/src/custom.rs` -> **54** Orphaned Functions | **6** Duplicates
- `wgpu-hal/src/noop/mod.rs` -> **60** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`naga/src/back/hlsl/ray.rs`** -> AI Confidence: **99.48%**
2. **`naga/src/back/glsl/features.rs`** -> AI Confidence: **99.39%**
3. **`naga/src/back/wgsl/writer.rs`** -> AI Confidence: **99.39%**
4. **`wgpu-info/src/human.rs`** -> AI Confidence: **99.39%**
5. **`naga/src/back/hlsl/help.rs`** -> AI Confidence: **99.35%**
6. **`lock-analyzer/src/main.rs`** -> AI Confidence: **99.31%**
7. **`naga/src/back/dot/mod.rs`** -> AI Confidence: **99.31%**
8. **`naga/src/back/glsl/conv.rs`** -> AI Confidence: **99.31%**
9. **`naga/src/back/glsl/mod.rs`** -> AI Confidence: **99.31%**
10. **`naga/src/back/hlsl/mesh_shader.rs`** -> AI Confidence: **99.31%**
11. **`naga/src/back/hlsl/storage.rs`** -> AI Confidence: **99.31%**
12. **`naga/src/back/hlsl/writer.rs`** -> AI Confidence: **99.31%**
13. **`naga/src/back/msl/mod.rs`** -> AI Confidence: **99.31%**
14. **`naga/src/back/msl/writer.rs`** -> AI Confidence: **99.31%**
15. **`naga/src/back/spv/f16_polyfill.rs`** -> AI Confidence: **99.31%**
16. **`naga/src/common/wgsl/to_wgsl.rs`** -> AI Confidence: **99.31%**
17. **`naga/src/common/wgsl/types.rs`** -> AI Confidence: **99.31%**
18. **`naga/src/front/glsl/builtins.rs`** -> AI Confidence: **99.31%**
19. **`naga/src/front/glsl/context.rs`** -> AI Confidence: **99.31%**
20. **`naga/src/front/glsl/parser/functions.rs`** -> AI Confidence: **99.31%**
21. **`naga/src/front/wgsl/parse/conv.rs`** -> AI Confidence: **99.31%**
22. **`naga/src/front/wgsl/parse/mod.rs`** -> AI Confidence: **99.31%**
23. **`naga/src/proc/typifier.rs`** -> AI Confidence: **99.31%**
24. **`naga/src/valid/expression.rs`** -> AI Confidence: **99.31%**
25. **`naga/src/valid/function.rs`** -> AI Confidence: **99.31%**
26. **`naga/src/valid/handles.rs`** -> AI Confidence: **99.31%**
27. **`naga/src/valid/interface.rs`** -> AI Confidence: **99.31%**
28. **`naga/src/valid/type.rs`** -> AI Confidence: **99.31%**
29. **`naga/xtask/src/validate.rs`** -> AI Confidence: **99.31%**
30. **`wgpu-core/src/binding_model.rs`** -> AI Confidence: **99.31%**
31. **`wgpu-core/src/command/draw.rs`** -> AI Confidence: **99.31%**
32. **`wgpu-core/src/command/transfer.rs`** -> AI Confidence: **99.31%**
33. **`wgpu-core/src/device/trace.rs`** -> AI Confidence: **99.31%**
34. **`wgpu-core/src/ray_tracing.rs`** -> AI Confidence: **99.31%**
35. **`wgpu-hal/src/auxil/dxgi/conv.rs`** -> AI Confidence: **99.31%**
36. **`wgpu-hal/src/dx12/conv.rs`** -> AI Confidence: **99.31%**
37. **`wgpu-hal/src/dx12/instance.rs`** -> AI Confidence: **99.31%**
38. **`wgpu-hal/src/gles/adapter.rs`** -> AI Confidence: **99.31%**
39. **`wgpu-hal/src/gles/conv.rs`** -> AI Confidence: **99.31%**
40. **`wgpu-hal/src/metal/adapter.rs`** -> AI Confidence: **99.31%**
41. **`wgpu-types/src/adapter.rs`** -> AI Confidence: **99.31%**
42. **`xtask/src/cts.rs`** -> AI Confidence: **99.31%**
43. **`xtask/src/run_wasm.rs`** -> AI Confidence: **99.31%**
44. **`wgpu-hal/src/vulkan/conv.rs`** -> AI Confidence: **99.29%**
45. **`wgpu/src/backend/webgpu/webgpu_sys/gen_GpuSupportedLimits.rs`** -> AI Confidence: **99.29%**
46. **`wgpu-core/src/validation.rs`** -> AI Confidence: **99.25%**
47. **`wgpu-types/src/texture/format.rs`** -> AI Confidence: **99.25%**
48. **`cts_runner/tests/integration.rs`** -> AI Confidence: **99.24%**
49. **`naga/src/common/diagnostic_debug.rs`** -> AI Confidence: **99.24%**
50. **`naga/src/front/glsl/functions.rs`** -> AI Confidence: **99.24%**
51. **`naga/src/front/glsl/parser/declarations.rs`** -> AI Confidence: **99.24%**
52. **`naga/src/front/glsl/parser/expressions.rs`** -> AI Confidence: **99.24%**
53. **`naga/src/front/glsl/types.rs`** -> AI Confidence: **99.24%**
54. **`naga/src/front/spv/error.rs`** -> AI Confidence: **99.24%**
55. **`naga/src/front/spv/next_block.rs`** -> AI Confidence: **99.24%**
56. **`naga/src/front/wgsl/lower/mod.rs`** -> AI Confidence: **99.24%**
57. **`naga/src/proc/constant_evaluator.rs`** -> AI Confidence: **99.24%**
58. **`naga/src/proc/index.rs`** -> AI Confidence: **99.24%**
59. **`naga/src/proc/layouter.rs`** -> AI Confidence: **99.24%**
60. **`naga/src/proc/namer.rs`** -> AI Confidence: **99.24%**
61. **`player/tests/player/main.rs`** -> AI Confidence: **99.24%**
62. **`tests/src/init.rs`** -> AI Confidence: **99.24%**
63. **`tests/tests/wgpu-gpu/clear_texture.rs`** -> AI Confidence: **99.24%**
64. **`wgpu-core/src/command/bind.rs`** -> AI Confidence: **99.24%**
65. **`wgpu-core/src/command/clear.rs`** -> AI Confidence: **99.24%**
66. **`wgpu-core/src/command/query.rs`** -> AI Confidence: **99.24%**
67. **`wgpu-core/src/command/render.rs`** -> AI Confidence: **99.24%**
68. **`wgpu-core/src/command/transition_resources.rs`** -> AI Confidence: **99.24%**
69. **`wgpu-core/src/device/mod.rs`** -> AI Confidence: **99.24%**
70. **`wgpu-core/src/device/ray_tracing.rs`** -> AI Confidence: **99.24%**
71. **`wgpu-core/src/device/resource.rs`** -> AI Confidence: **99.24%**
72. **`wgpu-core/src/instance.rs`** -> AI Confidence: **99.24%**
73. **`wgpu-core/src/pipeline.rs`** -> AI Confidence: **99.24%**
74. **`wgpu-hal/src/dx12/device.rs`** -> AI Confidence: **99.24%**
75. **`wgpu-hal/src/gles/command.rs`** -> AI Confidence: **99.24%**
76. **`wgpu-hal/src/gles/egl.rs`** -> AI Confidence: **99.24%**
77. **`wgpu-hal/src/gles/queue.rs`** -> AI Confidence: **99.24%**
78. **`wgpu-hal/src/lib.rs`** -> AI Confidence: **99.24%**
79. **`wgpu-hal/src/metal/conv.rs`** -> AI Confidence: **99.24%**
80. **`wgpu-hal/src/metal/device.rs`** -> AI Confidence: **99.24%**
81. **`wgpu-hal/src/vulkan/adapter.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `benches/benches/wgpu-benchmark/computepass.rs` -> **20.0%** Exposure
- `benches/benches/wgpu-benchmark/renderpass.rs` -> **20.0%** Exposure
- `benches/benches/wgpu-benchmark/shader.rs` -> **20.0%** Exposure
- `benches/src/lib.rs` -> **20.0%** Exposure
- `deno_webgpu/device.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `tests/tests/wgpu-gpu/passthrough/mod.rs` -> **100.0%** Exposure
- `wgpu-core/src/binding_model.rs` -> **100.0%** Exposure
- `wgpu-core/src/command/query.rs` -> **100.0%** Exposure
- `wgpu-core/src/device/queue.rs` -> **100.0%** Exposure
- `wgpu-core/src/instance.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `naga/src/arena/mod.rs` -> **0.0002%** Exposure
- `wgpu-hal/src/metal/library_from_metallib.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `benches/benches/wgpu-benchmark/bind_groups.rs` -> **100.0%** Exposure
- `benches/benches/wgpu-benchmark/computepass.rs` -> **100.0%** Exposure
- `benches/benches/wgpu-benchmark/renderpass.rs` -> **100.0%** Exposure
- `benches/benches/wgpu-benchmark/shader.rs` -> **100.0%** Exposure
- `benches/src/lib.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7857` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wgpu-hal/src/noop/command.rs` (RUST) -> Cumulative Risk: **782.52**
- **Archetype:** `file_cluster_16` (Distance: 10.923 IQR)
- **Magnitude:** 312.2 | **LOC:** 337 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.5763%)
- **Heaviest Functions:** `execute` (Impact: 19.5), `execute` (Impact: 14.1), `new` (Impact: 7.2)

### 2. `wgpu-core/src/resource.rs` (RUST) -> Cumulative Risk: **761.02**
- **Archetype:** `file_cluster_0` (Distance: 13.108 IQR)
- **Magnitude:** 1594.82 | **LOC:** 2426 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 47.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `map_async` (Impact: 130.2), `get_mapped_range` (Impact: 97.9), `map` (Impact: 75.3)

### 3. `wgpu-core/src/command/query.rs` (RUST) -> Cumulative Risk: **753.89**
- **Archetype:** `file_cluster_0` (Distance: 12.036 IQR)
- **Magnitude:** 445.18 | **LOC:** 526 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `resolve_query_set` (Impact: 90.1), `reset_queries` (Impact: 49.5), `validate_and_begin_pipeline_statistics_q` (Impact: 33.5)

### 4. `wgpu/src/backend/webgpu.rs` (RUST) -> Cumulative Risk: **741.63**
- **Archetype:** `file_cluster_8` (Distance: 12.605 IQR)
- **Magnitude:** 3719.82 | **LOC:** 4059 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 22.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9049%), Documentation (98.275%)
- **Heaviest Functions:** `create_surface_from_context` (Impact: 1731.1), `begin_render_pass` (Impact: 172.8), `pop_error_scope` (Impact: 118.9)

### 5. `wgpu-hal/src/dx12/mod.rs` (RUST) -> Cumulative Risk: **725.33**
- **Archetype:** `file_cluster_0` (Distance: 12.892 IQR)
- **Magnitude:** 709.08 | **LOC:** 1700 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.3352%), Documentation (98.8956%)
- **Heaviest Functions:** `debug_interface1` (Impact: 44.6), `present` (Impact: 37.0), `serialize_root_signature` (Impact: 35.4)

### 6. `naga/src/arena/handle_set.rs` (RUST) -> Cumulative Risk: **717.99**
- **Archetype:** `file_cluster_16` (Distance: 13.05 IQR)
- **Magnitude:** 124.88 | **LOC:** 133 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9983%)
- **Heaviest Functions:** `pop` (Impact: 15.7), `len` (Impact: 10.8), `new` (Impact: 7.3)

### 7. `wgpu-core/src/binding_model.rs` (RUST) -> Cumulative Risk: **711.31**
- **Archetype:** `file_cluster_0` (Distance: 11.881 IQR)
- **Magnitude:** 1074.98 | **LOC:** 1377 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 35.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `drop` (Impact: 525.9), `validate` (Impact: 106.7), `add_binding` (Impact: 76.1)

### 8. `naga/src/error.rs` (RUST) -> Cumulative Risk: **708.37**
- **Archetype:** `file_cluster_0` (Distance: 11.188 IQR)
- **Magnitude:** 210.32 | **LOC:** 197 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (96.6038%)
- **Heaviest Functions:** `emit_to_self` (Impact: 40.5), `emit_to_writer` (Impact: 32.8), `new` (Impact: 27.0)

### 9. `wgpu-core/src/pipeline.rs` (RUST) -> Cumulative Risk: **707.71**
- **Archetype:** `file_cluster_0` (Distance: 11.988 IQR)
- **Magnitude:** 256.72 | **LOC:** 854 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%), Tech Debt (98.0946%)
- **Heaviest Functions:** `webgpu_error_type` (Impact: 15.4), `webgpu_error_type` (Impact: 14.4), `webgpu_error_type` (Impact: 14.3)

### 10. `naga/xtask/src/validate.rs` (RUST) -> Cumulative Risk: **702.87**
- **Archetype:** `file_cluster_8` (Distance: 12.389 IQR)
- **Magnitude:** 797.7 | **LOC:** 429 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `collect_validation_jobs` (Impact: 259.9), `validate` (Impact: 184.5), `validate_spirv` (Impact: 103.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `naga/src/back/hlsl/writer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.176 IQR)
- **Top Global Matches:** file_cluster_8: 13.176, file_cluster_0: 13.476, file_cluster_13: 13.477
- **Magnitude:** 13916.04 | **LOC:** 5021 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (24.3128%), Tech Debt (12.5855%)
**Top Internal Functions/Classes:**
  * `write_stmt` (Impact: 7127.2 | O(2^N) | DB: 5)
  * `write_function` (Impact: 1662.0 | O(N^6) | DB: 12)
  * `write` (Impact: 1315.8 | O(2^N) | DB: 5)
  * `write_global` (Impact: 550.0 | O(N^6) | DB: 1)
  * `write_struct` (Impact: 383.0 | O(N^6) | DB: 2)
    * *Intent:* /// Helper method used to write global constants /// /// # Notes /// Ends in a newline
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1095`, `structural_boundaries: 494`, `args: 89`, `func_start: 44`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 170`, `dead_code: 11`, `planned_debt: 6`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 63`, `import: 13`
* *Defense:* `safety: 467`, `doc: 96`, `test: 3`, `sync_locks: 23`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Module, ShaderModel, Options, NameKey, get_entry_points, ShaderStage, crate::MathFunction, mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/wgsl/parse/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.425 IQR)
- **Top Global Matches:** file_cluster_16: 14.425, file_cluster_8: 14.472, file_cluster_13: 14.577
- **Magnitude:** 9350.42 | **LOC:** 2409 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 61.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 119
- **Risk Profile:** Cognitive Load (38.1459%), Tech Debt (9.4663%)
**Top Internal Functions/Classes:**
  * `variable_updating_statement` (Impact: 7191.1 | O(2^N) | DB: 119)
  * `parse` (Impact: 313.3 | O(N^6) | DB: 4)
  * `struct_body` (Impact: 198.2 | O(N^6) | DB: 9)
  * `lhs_expression` (Impact: 191.6 | O(2^N) | DB: 3)
  * `arguments` (Impact: 175.8 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 475`, `structural_boundaries: 530`, `args: 77`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 390`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `import: 14`
* *Defense:* `safety: 360`, `doc: 90`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Handle, crate::Arena, crate::front::wgsl::parse::directive::language_extension::LanguageExtension, FastHashSet, ExpectedToken, ShaderStage, EnableExtensions, TokenSpan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/wgsl/lower/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.86 IQR)
- **Top Global Matches:** file_cluster_16: 14.86, file_cluster_8: 14.863, file_cluster_13: 14.93
- **Magnitude:** 8061.32 | **LOC:** 4879 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (33.0834%), Tech Debt (30.3846%)
**Top Internal Functions/Classes:**
  * `binary` (Impact: 3379.0 | O(N^6) | DB: 78)
  * `expression_for_reference` (Impact: 733.0 | O(2^N) | DB: 4)
  * `function` (Impact: 643.7 | O(2^N) | DB: 24)
  * `logical` (Impact: 304.6 | O(N^6) | DB: 4)
  * `type_specifier` (Impact: 254.0 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 1017`, `args: 125`, `func_start: 73`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 711`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 8`
* *Architecture:* `api: 15`, `import: 22`
* *Defense:* `safety: 616`, `doc: 321`, `test: 2`, `sync_locks: 14`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crate::Arena, crate::
    common::wgsl::TryToWgsl, crate::common::ForDebugWithTypes, core::num::NonZeroU32, boxed::Box, ExpectedToken, proc, Span...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/msl/writer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.86 IQR)
- **Top Global Matches:** file_cluster_8: 13.86, file_cluster_0: 14.055, file_cluster_13: 14.077
- **Magnitude:** 7837.5 | **LOC:** 8257 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (15.6409%), Tech Debt (18.5219%)
**Top Internal Functions/Classes:**
  * `put_access_chain` (Impact: 3747.1 | O(2^N) | DB: 19)
  * `put_restricted_texel_address` (Impact: 2259.8 | O(N^6) | DB: 13)
  * `put_image_size_query` (Impact: 209.2 | O(N^5) | DB: 1)
  * `fmt` (Impact: 184.1 | O(N^6) | DB: 1)
  * `put_bounds_checks` (Impact: 150.4 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1126`, `structural_boundaries: 700`, `args: 156`, `func_start: 73`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 311`, `dead_code: 27`, `planned_debt: 10`, `fragile_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 13`, `import: 18`
* *Defense:* `safety: 488`, `doc: 364`, `test: 8`, `sync_locks: 2`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` proc::
        self, core::ptr, core::
    cmp::Ordering, Options, LocationMode, NameKey, crate::ScalarKind::*, FastHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/proc/constant_evaluator.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.299 IQR)
- **Top Global Matches:** file_cluster_8: 13.299, file_cluster_0: 13.423, file_cluster_16: 13.465
- **Magnitude:** 5699.3 | **LOC:** 4774 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 35.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (9.7179%), Tech Debt (43.8573%)
**Top Internal Functions/Classes:**
  * `try_eval_and_append` (Impact: 2284.4 | O(2^N) | DB: 14)
    * *Intent:* // "See through" the constant and use its initializer.
  * `binary_op` (Impact: 1310.9 | O(2^N) | DB: 5)
  * `select` (Impact: 153.6 | O(N^6) | DB: 3)
  * `unary_op` (Impact: 149.7 | O(2^N) | DB: 3)
  * `binary_op_compose` (Impact: 130.6 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 459`, `structural_boundaries: 677`, `args: 184`, `func_start: 85`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 57`, `high_risk_execution: 2`, `state_mutation: 265`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 16`, `orphaned_logic: 14`
* *Architecture:* `api: 16`, `import: 16`
* *Defense:* `safety: 411`, `doc: 230`, `test: 55`, `sync_locks: 3`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::proc::type_methods::IntFloatLimits, num_traits::real::Real, VectorSize, Zero, Span, Constant, One, ConstantEvaluator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/wgsl/writer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.336 IQR)
- **Top Global Matches:** file_cluster_8: 12.336, file_cluster_7: 12.641, file_cluster_13: 12.652
- **Magnitude:** 5097.1 | **LOC:** 2170 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 35.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (18.4704%), Tech Debt (13.5036%)
**Top Internal Functions/Classes:**
  * `write_function` (Impact: 4015.5 | O(N^6) | DB: 15)
    * *Intent:* /// Helper method used to write /// [functions](https://gpuweb.github.io/gpuweb/wgsl/#functions)
  * `write` (Impact: 483.1 | O(2^N) | DB: 4)
  * `write_enable_declarations` (Impact: 215.3 | O(N^6) | DB: 7)
  * `write_global` (Impact: 125.4 | O(N^4) | DB: 1)
  * `write_override` (Impact: 41.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 598`, `structural_boundaries: 222`, `args: 58`, `func_start: 27`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 72`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 17`
* *Defense:* `safety: 157`, `doc: 117`, `sync_locks: 12`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Module, NameKey, wgsl::address_space_str, ToWgsl, ShaderStage, crate::MathFunction, crate::RelationalFunction, crate::SampleLevel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/spv/writer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.332 IQR)
- **Top Global Matches:** file_cluster_8: 13.332, file_cluster_13: 13.528, file_cluster_7: 13.586
- **Magnitude:** 4631.66 | **LOC:** 3849 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (15.5857%), Tech Debt (8.5444%)
**Top Internal Functions/Classes:**
  * `write_function` (Impact: 3092.0 | O(2^N) | DB: 57)
  * `write_logical_layout` (Impact: 399.8 | O(N^5) | DB: 18)
  * `write_global_variable` (Impact: 235.6 | O(N^6) | DB: 7)
    * *Intent:* /// /// When `handle` refers to a [`TypeInner::Matrix`] with 2 rows, the /// declared type will be a...
  * `to_words` (Impact: 105.4 | O(2^N) | DB: 1)
  * `write_wrapped_convert_from_std140_compat` (Impact: 66.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 495`, `args: 84`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 294`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 62`, `import: 15`
* *Defense:* `safety: 266`, `doc: 162`, `test: 4`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LocalType, Options, helpers::contains_builtin, LocalVariable, valid::FunctionInfo, hashbrown::hash_map::Entry, global_needs_wrapper, Instruction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu/src/backend/webgpu.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.605 IQR)
- **Top Global Matches:** file_cluster_8: 12.605, file_cluster_0: 12.788, file_cluster_13: 12.868
- **Magnitude:** 3719.82 | **LOC:** 4059 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 22.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (12.1489%), Tech Debt (99.9049%)
**Top Internal Functions/Classes:**
  * `create_surface_from_context` (Impact: 1731.1 | O(2^N) | DB: 9)
  * `begin_render_pass` (Impact: 172.8 | O(2^N) | DB: 1)
  * `pop_error_scope` (Impact: 118.9 | O(2^N) | DB: 1)
  * `configure` (Impact: 52.0 | O(2^N))
  * `set_bind_group` (Impact: 45.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 557`, `args: 103`, `func_start: 216`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 26`, `state_mutation: 140`, `dead_code: 3`, `planned_debt: 11`, `duplicate_logic: 71`, `orphaned_logic: 27`
* *Architecture:* `api: 51`, `concurrency: 25`, `import: 35`
* *Defense:* `safety: 324`, `doc: 81`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Blas, BlasCompactCallback, OnceCell, wgt::Face, SurfaceTargetUnsafe, defined_non_null_js_value::DefinedNonNullJsValue, webgpu_sys::GpuBlendOperation, sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/command/render.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.332 IQR)
- **Top Global Matches:** file_cluster_0: 13.332, file_cluster_8: 13.349, file_cluster_16: 13.505
- **Magnitude:** 2919.56 | **LOC:** 3865 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 45.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (8.8868%), Tech Debt (90.7142%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 1103.5 | O(2^N) | DB: 22)
  * `multi_draw_indirect_count` (Impact: 354.2 | O(2^N) | DB: 1)
  * `command_encoder_begin_render_pass` (Impact: 300.0 | O(N^6) | DB: 4)
  * `execute_bundle` (Impact: 165.5 | O(2^N) | DB: 2)
    * *Intent:* /// Creates a render pass. /// /// If creation fails, an invalid pass is returned. Attempting to rec...
  * `is_ready` (Impact: 75.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 322`, `args: 59`, `func_start: 72`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 131`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 38`
* *Architecture:* `api: 75`, `import: 11`
* *Defense:* `safety: 292`, `doc: 90`, `test: 1`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BindGroupStateChange, init_tracker::MemoryInitKind, binding_model::BindError, sync::Arc, QuerySet, validate_and_begin_occlusion_query, pass::self, ArcPassTimestampWrites...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/valid/handles.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.637 IQR)
- **Top Global Matches:** file_cluster_8: 11.637, file_cluster_7: 12.008, file_cluster_0: 12.033
- **Magnitude:** 2779.66 | **LOC:** 1177 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (9.0692%), Tech Debt (8.7506%)
**Top Internal Functions/Classes:**
  * `validate_module_handles` (Impact: 2737.8 | O(2^N) | DB: 10)
    * *Intent:* /// * Valid, in the sense that they contain indices within each arena structure inside the /// [`cra...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 94`, `args: 33`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 81`, `doc: 42`, `test: 1`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::Arena, crate::non_max_u32::NonMaxU32, Span, EntryPoint, Scalar, crate::Constant, core::convert::TryInto, TypeInner...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu/src/backend/wgpu_core.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.308 IQR)
- **Top Global Matches:** file_cluster_8: 13.308, file_cluster_0: 13.432, file_cluster_17: 13.47
- **Magnitude:** 2686.04 | **LOC:** 4037 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 120
- **Risk Profile:** Cognitive Load (18.0343%), Tech Debt (17.1375%)
**Top Internal Functions/Classes:**
  * `ready_for_compaction` (Impact: 1144.6 | O(2^N) | DB: 120)
  * `handle_error_or_return_handler` (Impact: 575.7 | O(N^6) | DB: 16)
    * *Intent:* /// Deliver the error to /// /// * the innermost error scope, if any, or /// * the uncaptured error ...
  * `map_async` (Impact: 45.6 | O(2^N))
  * `handle_error_inner` (Impact: 36.3 | O(N^5) | DB: 1)
  * `create_device_from_hal` (Impact: 25.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 562`, `args: 271`, `func_start: 198`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 342`, `duplicate_logic: 13`
* *Architecture:* `api: 78`, `concurrency: 12`, `import: 16`
* *Defense:* `safety: 437`, `doc: 23`, `test: 1`, `sync_locks: 20`, `immutability_locks: 10`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.945
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.002323
  * `Imports (Out-Degree: 1):` wgc::
    command::bundle_ffi::*, Label, wgc::naga::front::wgsl::ImplementedLanguageExtension, LoadOp, Blas, BlasCompactCallback, ShaderSource, resource::BlasPrepareCompactResult...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `naga/src/front/spv/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.322 IQR)
- **Top Global Matches:** file_cluster_8: 13.322, file_cluster_0: 13.389, file_cluster_13: 13.461
- **Magnitude:** 2487.78 | **LOC:** 3275 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (15.0367%), Tech Debt (36.0726%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 801.0 | O(N^6) | DB: 43)
  * `patch_statements` (Impact: 295.9 | O(2^N) | DB: 13)
  * `insert_composite` (Impact: 231.8 | O(2^N) | DB: 2)
  * `parse_expr_binary_op_sign_adjusted` (Impact: 127.0 | O(N^5) | DB: 4)
  * `parse_expr_int_comparison` (Impact: 126.9 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 424`, `args: 42`, `func_start: 38`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 204`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 11`, `import: 12`
* *Defense:* `safety: 206`, `doc: 241`, `test: 3`, `sync_locks: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` petgraph::graphmap::GraphMap, FastHashSet, num::NonZeroU32, function::*, mem, crate::Statement, spirv::Op, Layouter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/device/global.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.704 IQR)
- **Top Global Matches:** file_cluster_0: 13.704, file_cluster_8: 13.743, file_cluster_16: 13.826
- **Magnitude:** 2430.96 | **LOC:** 2127 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 56.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (8.7611%), Tech Debt (58.4847%)
**Top Internal Functions/Classes:**
  * `device_create_shader_module` (Impact: 1266.5 | O(N^6) | DB: 19)
  * `device_create_bind_group` (Impact: 188.7 | O(N^6) | DB: 1)
  * `create_texture_from_hal` (Impact: 97.2 | O(2^N) | DB: 1)
    * *Intent:* /// # Safety ///
  * `device_create_pipeline_layout` (Impact: 88.9 | O(N^6) | DB: 1)
  * `device_create_external_texture` (Impact: 76.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 438`, `args: 53`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 91`, `planned_debt: 2`, `orphaned_logic: 29`
* *Architecture:* `api: 62`, `import: 9`
* *Defense:* `safety: 394`, `doc: 106`, `test: 1`, `sync_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DeviceLostClosure, instance::self, crate::device::trace::DataKind, ResolvedBindingResource, pipeline::
        self, super::UserClosures, resource::
        self, ResolvedBufferBinding...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/hlsl/help.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.257 IQR)
- **Top Global Matches:** file_cluster_8: 11.257, file_cluster_0: 11.514, file_cluster_7: 11.558
- **Magnitude:** 2413.02 | **LOC:** 2333 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.1764%), Tech Debt (32.8653%)
**Top Internal Functions/Classes:**
  * `write_wrapped_image_query_function` (Impact: 555.3 | O(N^6) | DB: 1)
  * `write_wrapped_image_sample_function` (Impact: 461.2 | O(N^6) | DB: 1)
  * `write_wrapped_image_load_function` (Impact: 299.8 | O(N^5) | DB: 1)
    * *Intent:* // Apply the inverse of the source transfer function to convert to // linear RGB in the source color...
  * `write_texture_coordinates` (Impact: 191.6 | O(N^6) | DB: 1)
  * `write_wrapped_binary_ops` (Impact: 168.8 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 142`, `args: 15`, `func_start: 18`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 35`, `dead_code: 3`, `planned_debt: 3`, `orphaned_logic: 10`
* *Architecture:* `api: 50`, `import: 9`
* *Defense:* `safety: 65`, `doc: 73`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` INSERT_BITS_FUNCTION, EXTRACT_BITS_FUNCTION, ImageDimension, INDENT, WrappedType, NEG_FUNCTION, IMAGE_SAMPLE_BASE_CLAMP_TO_EDGE_FUNCTION, writer::
        ABS_FUNCTION...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/tests/naga/wgsl_errors.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.502 IQR)
- **Top Global Matches:** file_cluster_8: 11.502, file_cluster_7: 12.03, file_cluster_0: 12.041
- **Magnitude:** 2216.12 | **LOC:** 5255 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 35.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.0758%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` (Impact: 1200.6 | O(N^6))
  * `bad_for_initializer` (Impact: 572.0 | O(N^6) | DB: 1)
  * `check_with_capabilities` (Impact: 26.0 | O(N^4) | DB: 2)
  * `check` (Impact: 22.5 | O(N^4))
  * `test_break_if_bad_condition` (Impact: 21.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 388`, `args: 171`, `func_start: 308`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 8`, `dead_code: 6`, `planned_debt: 2`, `duplicate_logic: 27`, `orphaned_logic: 27`
* *Architecture:* `concurrency: 4`, `import: 3`
* *Defense:* `safety: 146`, `doc: 63`, `test: 166`, `sync_locks: 11`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` naga::valid::TypeError, ValidationError, Capabilities, ImplementedEnableExtension, naga::
    compact::KeepUnused, front::wgsl::EnableExtension, VaryingError, valid::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-hal/src/vulkan/device.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.388 IQR)
- **Top Global Matches:** file_cluster_8: 12.388, file_cluster_17: 12.715, file_cluster_13: 12.747
- **Magnitude:** 2108.1 | **LOC:** 2827 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (13.6414%), Tech Debt (8.1244%)
**Top Internal Functions/Classes:**
  * `create_image_without_memory` (Impact: 1052.6 | O(N^6) | DB: 65)
  * `get_acceleration_structure_build_sizes` (Impact: 195.3 | O(2^N) | DB: 7)
  * `create_acceleration_structure` (Impact: 159.6 | O(2^N))
  * `make_render_pass` (Impact: 98.8 | O(N^6) | DB: 8)
  * `wait_for_fence` (Impact: 79.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 416`, `args: 64`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 165`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 26`, `import: 10`
* *Defense:* `safety: 283`, `doc: 48`, `sync_locks: 16`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mem::self, MaybeUninit, RawTlasInstance, hashbrown::hash_map::Entry, num::NonZeroU32, sync::Arc, collections::BTreeMap, time::Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/hlsl/ray.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.091 IQR)
- **Top Global Matches:** file_cluster_8: 10.091, file_cluster_13: 10.748, file_cluster_7: 10.751
- **Magnitude:** 2073.04 | **LOC:** 565 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (37.8197%), Tech Debt (53.8332%)
**Top Internal Functions/Classes:**
  * `write_initialize_function` (Impact: 914.7 | O(N^6) | DB: 4)
  * `write_generate_intersection` (Impact: 250.2 | O(N^4) | DB: 2)
  * `write_candidate_intersection_function` (Impact: 220.1 | O(N^4) | DB: 2)
  * `write_committed_intersection_function` (Impact: 204.6 | O(N^4) | DB: 2)
  * `write_proceed` (Impact: 167.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 38`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 38`, `fragile_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Level, TypeInner, string::String, Baked, crate::
    back::hlsl::BackendResult, ToString, core::fmt::Write, alloc::
    format...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu/src/backend/webgpu/webgpu_sys/gen_GpuSupportedLimits.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.354 IQR)
- **Top Global Matches:** file_cluster_0: 11.354, file_cluster_8: 11.431, file_cluster_7: 11.533
- **Magnitude:** 2012.75 | **LOC:** 382 | **CtrlFlow:** 91.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.7256%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 3`, `args: 31`, `func_start: 31`
* *Risk/State:* None
* *Architecture:* `api: 32`, `import: 2`
* *Defense:* `doc: 256`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasm_bindgen::prelude::*, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/validation.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.221 IQR)
- **Top Global Matches:** file_cluster_8: 12.221, file_cluster_0: 12.278, file_cluster_13: 12.607
- **Magnitude:** 1966.72 | **LOC:** 2004 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 51.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (11.4589%), Tech Debt (51.4583%)
**Top Internal Functions/Classes:**
  * `check_stage` (Impact: 1066.4 | O(N^6) | DB: 10)
  * `new` (Impact: 229.8 | O(2^N) | DB: 8)
  * `check_binding_use` (Impact: 191.8 | O(N^6) | DB: 1)
  * `derive_binding_type` (Impact: 95.2 | O(N^6))
  * `finalize_entry_point_name` (Impact: 27.8 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 214`, `args: 73`, `func_start: 26`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 11`
* *Architecture:* `api: 38`, `import: 12`
* *Defense:* `safety: 207`, `doc: 26`, `test: 4`, `sync_locks: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wgpu_naga_bridge::map_storage_format_to_naga, FastHashSet, hashbrown::hash_map::Entry, VectorSize, sync::Arc, crate::
    command::ColorAttachmentError, resource::InvalidResourceError, BindingType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/device/queue.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.086 IQR)
- **Top Global Matches:** file_cluster_0: 13.086, file_cluster_8: 13.137, file_cluster_16: 13.226
- **Magnitude:** 1853.48 | **LOC:** 1884 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (13.6505%), Tech Debt (11.3207%)
**Top Internal Functions/Classes:**
  * `drop` (Impact: 1636.5 | O(2^N) | DB: 59)
  * `new` (Impact: 33.9 | O(2^N) | DB: 1)
  * `maintain` (Impact: 5.7 | O(N^3) | DB: 1)
  * `raw` (Impact: 5.3 | O(2^N))
  * `label` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 213`, `args: 31`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 113`, `planned_debt: 9`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 146`, `doc: 45`, `test: 2`, `sync_locks: 21`, `immutability_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RwLock, id::self, sync::Arc, TrackingData, CommandBuffer, super::life::LifetimeTracker, AccelerationStructureFlags, Snatchable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/spv/block.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.276 IQR)
- **Top Global Matches:** file_cluster_8: 13.276, file_cluster_0: 13.454, file_cluster_13: 13.461
- **Magnitude:** 1798.16 | **LOC:** 4232 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (9.1919%), Tech Debt (10.2222%)
**Top Internal Functions/Classes:**
  * `write_access_chain` (Impact: 1381.6 | O(2^N) | DB: 61)
  * `write_entry_point_return` (Impact: 219.6 | O(N^6) | DB: 6)
  * `get_dimension` (Impact: 6.5 | O(N^2))
  * `write_epilogue_position_y_flip` (Impact: 6.0 | O(N^3) | DB: 2)
    * *Intent:* /// What code generation did with a provided [`BlockExit`] value. ///
  * `write_epilogue_frag_depth_clamp` (Impact: 5.9 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 252`, `args: 24`, `func_start: 13`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 141`, `dead_code: 11`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 213`, `doc: 212`, `test: 1`, `sync_locks: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LocalType, IdGenerator, back::spv::helpers::is_uniform_matcx2_struct_member_access, crate::MathFunction, Instruction, proc::index::GuardedIndex, alloc::vec::Vec, Block...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-hal/src/vulkan/adapter.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.285 IQR)
- **Top Global Matches:** file_cluster_8: 13.285, file_cluster_13: 13.461, file_cluster_0: 13.475
- **Magnitude:** 1796.84 | **LOC:** 3366 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 17.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (11.4251%), Tech Debt (9.5879%)
**Top Internal Functions/Classes:**
  * `device_from_raw` (Impact: 546.7 | O(N^5) | DB: 4)
  * `inspect` (Impact: 394.9 | O(N^6) | DB: 9)
  * `expose_adapter` (Impact: 181.4 | O(N^6) | DB: 2)
  * `get_required_extensions` (Impact: 141.8 | O(N^6) | DB: 16)
  * `add_to_device_create` (Impact: 108.1 | O(N^3) | DB: 27)
    * *Intent:* /// Add the members of `self` into `info.enabled_features` and its `p_next` chain.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 293`, `args: 77`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 166`, `dead_code: 8`, `planned_debt: 9`
* *Architecture:* `api: 30`, `import: 9`
* *Defense:* `safety: 185`, `doc: 196`, `test: 2`, `sync_locks: 7`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` google, marker::PhantomData, boxed::Box, sync::Arc, crate::TextureFormatCapabilities, collections::BTreeMap, crate::vulkan::semaphore_list::SemaphoreList, Features...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/glsl/functions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.504 IQR)
- **Top Global Matches:** file_cluster_8: 12.504, file_cluster_16: 12.782, file_cluster_13: 12.81
- **Magnitude:** 1786.8 | **LOC:** 1624 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (8.3222%), Tech Debt (10.6035%)
**Top Internal Functions/Classes:**
  * `matrix_one_arg` (Impact: 816.5 | O(N^6) | DB: 20)
  * `constructor_single` (Impact: 385.4 | O(N^6) | DB: 11)
  * `arg_type_walker` (Impact: 333.3 | O(2^N) | DB: 5)
    * *Intent:* // Reprocess argument in LHS position
  * `builtin_required_variations` (Impact: 78.0 | O(N^5) | DB: 1)
  * `function_or_constructor_call` (Impact: 43.7 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 152`, `args: 18`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `dead_code: 1`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 110`, `doc: 58`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LocalVariable, Span, Block, ScalarKind::*, Frontend, EntryPoint, Scalar, ScalarKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/spv/image.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.423 IQR)
- **Top Global Matches:** file_cluster_8: 11.423, file_cluster_0: 11.878, file_cluster_13: 11.907
- **Magnitude:** 1784.02 | **LOC:** 933 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (14.1258%), Tech Debt (8.0133%)
**Top Internal Functions/Classes:**
  * `parse_image_sample` (Impact: 758.7 | O(N^6) | DB: 9)
  * `parse_image_load` (Impact: 310.6 | O(N^6) | DB: 8)
  * `parse_image_write` (Impact: 242.4 | O(N^6) | DB: 4)
  * `extract_image_coordinates` (Impact: 99.0 | O(N^6) | DB: 3)
    * *Intent:* /// Return the texture coordinates separated from the array layer, /// and/or divided by the project...
  * `parse_image_query_size` (Impact: 92.8 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 213`, `args: 16`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 64`, `planned_debt: 1`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 113`, `doc: 13`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LookupExpression, Scalar, LookupHelper, UniqueArena, crate::SwizzleComponent, crate::
    arena::Handle, alloc::vec::Vec, super::Error
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/command/ray_tracing.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.288 IQR)
- **Top Global Matches:** file_cluster_8: 12.288, file_cluster_17: 12.561, file_cluster_13: 12.655
- **Magnitude:** 1739.86 | **LOC:** 1149 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (15.0044%), Tech Debt (9.8645%)
**Top Internal Functions/Classes:**
  * `iter_blas` (Impact: 637.2 | O(N^6) | DB: 7)
    * *Intent:* ///iterates over the blas iterator, and it's geometry, pushing the buffers into a storage vector (an...
  * `build_acceleration_structures` (Impact: 420.4 | O(2^N) | DB: 21)
  * `set_acceleration_structure_dependencies` (Impact: 135.6 | O(2^N) | DB: 2)
  * `command_encoder_build_acceleration_struc` (Impact: 133.1 | O(N^6) | DB: 1)
  * `validate_acceleration_structure_actions` (Impact: 105.4 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 203`, `args: 33`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 102`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 124`, `doc: 1`, `sync_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BlasBuildEntry, ArcTlasPackage, init_tracker::MemoryInitKind, snatch::SnatchGuard, BufferUsages, crate::
    command::ArcCommand, ops::Deref, ArcTlasInstance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `naga/src/back/spv/index.rs` (RUST) | Magnitude: 216.86 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 196, doc: 138, structural_boundaries: 40, safety: 35
- `wgpu-core/src/registry.rs` (RUST) | Magnitude: 60.1 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 57, generics: 16, structural_boundaries: 15, doc: 14
- `wgpu-hal/src/dx12/mod.rs` (RUST) | Magnitude: 709.08 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 897, structural_boundaries: 282, safety: 149, state_mutation: 128
- `wgpu-core/src/init_tracker/mod.rs` (RUST) | Magnitude: 370.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 71, test: 51, safety: 39
- `wgpu-core/src/command/render.rs` (RUST) | Magnitude: 2919.56 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1857, structural_boundaries: 322, safety: 292, branch: 210

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `naga/src/back/spv/reclaimable.rs` (RUST) | Magnitude: 36.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, doc: 23, structural_boundaries: 15, generics: 13
- `naga/src/compact/types.rs` (RUST) | Magnitude: 92.2 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 32, state_mutation: 30, args: 14
- `wgpu-hal/src/vulkan/semaphore_list.rs` (RUST) | Magnitude: 118.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 102, doc: 47, state_mutation: 28, structural_boundaries: 24
- `wgpu-core/src/track/blas.rs` (RUST) | Magnitude: 40.84 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, doc: 13, structural_boundaries: 8, api: 6
- `naga-cli/src/bin/naga.rs` (RUST) | Magnitude: 829.04 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 541, structural_boundaries: 140, branch: 104, safety: 104

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `naga/src/front/wgsl/parse/directive/language_extension.rs` (RUST) | Magnitude: 75.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, immutability_locks: 17, doc: 15, generics: 13
- `naga/src/front/wgsl/lower/mod.rs` (RUST) | Magnitude: 8061.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3418, structural_boundaries: 1017, state_mutation: 711, branch: 670
- `wgpu-hal/src/auxil/dxgi/result.rs` (RUST) | Magnitude: 33.9 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, generics: 6, safety: 4, structural_boundaries: 3
- `wgpu-types/src/error.rs` (RUST) | Magnitude: 21.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 28, indent_spaces: 5, structural_boundaries: 2, class_start: 2
- `wgpu-core/src/command/bundle.rs` (RUST) | Magnitude: 541.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 479, doc: 132, structural_boundaries: 85, safety: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `wgpu-hal/src/vulkan/swapchain/native.rs` (RUST) | Magnitude: 470.54 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 307, doc: 144, safety: 78, structural_boundaries: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/tests/wgpu-gpu/oom.rs` (RUST) | Magnitude: 70.16 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 52, concurrency: 42, safety: 26
- `wgpu/src/util/init.rs` (RUST) | Magnitude: 123.16 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, doc: 22, safety: 18, concurrency: 18
- `tests/tests/wgpu-gpu/shader_primitive_index/mod.rs` (RUST) | Magnitude: 47.04 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 30, safety: 22, concurrency: 21
- `examples/features/src/repeated_compute/mod.rs` (RUST) | Magnitude: 89.5 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 99, concurrency: 24, structural_boundaries: 20, safety: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `wgpu-types/src/limits.rs` (RUST) | Magnitude: 209.6 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 510, indent_spaces: 381, api: 63, encapsulation: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `benches/benches/wgpu-benchmark/resource_creation.rs` (RUST) | Magnitude: 37.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 11, args: 5, branch: 4
- `wgpu-hal/src/vulkan/instance.rs` (RUST) | Magnitude: 419.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 114, branch: 72, safety: 64
- `wgpu-core/src/command/compute.rs` (RUST) | Magnitude: 1094.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1069, structural_boundaries: 165, safety: 133, branch: 102
- `wgpu/src/backend/webgpu/webgpu_sys/gen_GpuCanvasAlphaMode.rs` (RUST) | Magnitude: 16.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 10, doc: 6, structural_boundaries: 3, indent_spaces: 2
- `wgpu/src/backend/webgpu/webgpu_sys/gen_GpuCanvasToneMappingMode.rs` (RUST) | Magnitude: 16.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 10, doc: 6, structural_boundaries: 3, indent_spaces: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `wgpu-core/src/validation.rs` -> Churn: **90.26%** | Cog Load: 11.4589% | Debt: 51.4583%
- `wgpu-hal/src/metal/mod.rs` -> Churn: **85.67%** | Cog Load: 10.0158% | Debt: 59.9784%
- `naga/src/valid/mod.rs` -> Churn: **82.06%** | Cog Load: 2.6606% | Debt: 99.8629%
- `wgpu-core/src/device/global.rs` -> Churn: **82.06%** | Cog Load: 8.7611% | Debt: 58.4847%
- `deno_webgpu/device.rs` -> Churn: **77.85%** | Cog Load: 7.4445% | Debt: 52.7147%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `naga/src/back/hlsl/ray.rs` -> **Vecvec** (100.0% isolated ownership) | Magnitude: 2073.04
- `naga/src/front/glsl/parser/declarations.rs` -> **06wj** (100.0% isolated ownership) | Magnitude: 1369.96
- `naga/src/front/glsl/parser/expressions.rs` -> **Jan** (100.0% isolated ownership) | Magnitude: 1218.9
- `naga/src/proc/typifier.rs` -> **Dzmitry Malyshau** (100.0% isolated ownership) | Magnitude: 988.5
- `naga/src/back/hlsl/mesh_shader.rs` -> **Inner Daemons** (100.0% isolated ownership) | Magnitude: 979.3

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wgpu/src/backend/wgpu_core.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 80.7339%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `benches/src/iter.rs` -> **Severity: 0.954** (Embedded: 0.0163 * Error Risk: 58.65%)
- `wgpu-core/src/id.rs` -> **Severity: 0.46** (Embedded: 0.0097 * Error Risk: 47.5021%)
- `naga/fuzz/fuzz_targets/ir.rs` -> **Severity: 0.443** (Embedded: 0.0081 * Error Risk: 54.533%)
- `wgpu-types/src/texture/format.rs` -> **Severity: 0.319** (Embedded: 0.0142 * Error Risk: 22.4458%)
- `tests/src/isolation.rs` -> **Severity: 0.107** (Embedded: 0.0012 * Error Risk: 91.8714%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benches/src/iter.rs` -> **Severity: 1406.9** (Blast Radius: 14.069 * Doc Risk: 100.0%)
- `wgpu-core/src/id.rs` -> **Severity: 1008.3** (Blast Radius: 10.083 * Doc Risk: 100.0%)
- `naga/fuzz/fuzz_targets/ir.rs` -> **Severity: 419.508** (Blast Radius: 7.58 * Doc Risk: 55.3441%)
- `wgpu-core/src/present.rs` -> **Severity: 294.5** (Blast Radius: 2.945 * Doc Risk: 100.0%)
- `wgpu-hal/src/dx12/shader_compilation.rs` -> **Severity: 232.7** (Blast Radius: 2.327 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
