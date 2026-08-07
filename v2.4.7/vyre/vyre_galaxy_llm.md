# ARCHITECTURAL_BRIEF: vyre
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/vyre` |
| **Timestamp** | `2026-08-07T05:40:51.358368+00:00` |
| **Scan Duration** | `14.39s` |
| **Git Branch** | `main` |
| **Git Commit** | `4d759595a12966433d417fea8fc54558253b834f` |
| **Git Remote** | `https://github.com/santhsecurity/vyre` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3744 malicious artifacts.

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
| Total Artifacts | 4674 |
| Analyzed Artifacts (Scanned) | 3962 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 712 |
| Total LOC | 679257 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 84.8% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.874 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3753 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1161 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 51 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 3604 | 667030 | 91.0% |
| MARKDOWN | 187 | 0 | 4.7% |
| SHELL | 119 | 6071 | 3.0% |
| JSON | 24 | 4729 | 0.6% |
| C | 11 | 159 | 0.3% |
| PLAINTEXT | 7 | 0 | 0.2% |
| PYTHON | 6 | 753 | 0.2% |
| GO | 4 | 515 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.07`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2802 | 70.7% |
| file_cluster_13 | 405 | 10.2% |
| file_cluster_0 | 323 | 8.2% |
| file_cluster_16 | 105 | 2.7% |
| file_cluster_7 | 58 | 1.5% |
| file_cluster_4 | 40 | 1.0% |
| file_cluster_17 | 26 | 0.7% |
| file_cluster_11 | 3 | 0.1% |
| file_cluster_12 | 3 | 0.1% |
| file_cluster_6 | 2 | 0.1% |
| file_cluster_9 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 194 | 4.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 712*

**Composition by Extension & Reason:**
- `.md`: 220x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2191 LOC), 1x Excluded (Machine-Generated Source Code Signature: 145 LOC)
- `.json`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4672 LOC)
- `.rs`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 41x Unsupported Format (.toml), 18x Excluded (Unsupported Extension: '.toml'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 28x Excluded (Unsupported Extension: '.stderr')
- `no_extension`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wgsl`: 10x Unsupported Format (.wgsl)
- `.lock`: 7x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.tmpl`: 3x Excluded (Unsupported Extension: '.tmpl')
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.tsv`: 1x Excluded (Static Asset Blob without Intent: 1835 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 30.7 | 32.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.2 | 2.3 | 0.0 |
| API Exposure | 0.0 | 14.9 | 2.4 | 1.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 42.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.6 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/check_ownership_boundaries.sh` (Hits: 144)
- `scripts/bench_index.sh` (Hits: 121)
- `scripts/check_no_string_wgsl.sh` (Hits: 71)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cargo_runner.sh** (`scripts/lib/cargo_runner.sh`) — 30 inbound connections
2. **slot.rs** (`vyre-runtime/src/megakernel/protocol/slot.rs`) — 18 inbound connections
3. **transfer_accounting.rs** (`vyre-driver/src/transfer_accounting.rs`) — 15 inbound connections
4. **debug.rs** (`vyre-runtime/src/megakernel/protocol/debug.rs`) — 9 inbound connections
5. **opcode.rs** (`vyre-runtime/src/megakernel/protocol/opcode.rs`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`vyre-driver-cuda/src/lib.rs`) — 197 outbound dependencies
2. **mod.rs** (`vyre-runtime/src/megakernel/mod.rs`) — 166 outbound dependencies
3. **mod.rs** (`vyre-libs/src/parsing/c/parse/vast/mod.rs`) — 150 outbound dependencies
4. **lib.rs** (`vyre-driver/src/lib.rs`) — 135 outbound dependencies
5. **lib.rs** (`vyre-foundation/src/lib.rs`) — 133 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fill_upload_resident_many_repeated_seque` (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **396.9** | LOC: 475
- `simplify_binop` (@ `vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`) -> Impact: **368.9** | LOC: 617
  * *Intent:* /// Algebraic identity simplifications for binary operators. /// These rewrites are always valid and don't require literal operands - /// they fire wh...
- `walk` (@ `xtask/src/lego_audit.rs`) -> Impact: **365.1** | LOC: 903
- `flush_active_macro_segment_inner` (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_expansion/flush.rs`) -> Impact: **354.0** | LOC: 574
- `reference_typed_kind` (@ `vyre-libs/src/parsing/c/parse/vast/ref_typedef/typed_kind.rs`) -> Impact: **348.4** | LOC: 351
- `dispatch_resident_async_concrete_with_pt` (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **343.8** | LOC: 432
- `run_semantic_requirement_checks` (@ `xtask/src/vyre_weir_release_gate.rs`) -> Impact: **329.6** | LOC: 1091
- `emit_op` (@ `vyre-emit-ptx/src/emitter.rs`) -> Impact: **321.5** | LOC: 470
- `dispatch_borrowed_async_with_ptx_concret` (@ `vyre-driver-cuda/src/backend/host_dispatch.rs`) -> Impact: **283.9** | LOC: 339
- `emit_main` (@ `vyre-driver-cuda/src/aot_launcher.rs`) -> Impact: **259.9** | LOC: 439

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `xtask/src` | 56 | 16993.12 | 12.51% | 10.89% |
| `vyre-driver/src` | 58 | 9844.5 | 8.41% | 58.09% |
| `vyre-primitives/src/graph` | 36 | 9132.28 | 6.62% | 43.43% |
| `vyre-driver-cuda/src/backend` | 25 | 6906.78 | 15.11% | 52.04% |
| `vyre-driver-cuda/tests` | 98 | 6590.79 | 2.58% | 0.0% |
| `vyre-driver-wgpu/tests` | 166 | 6493.52 | 2.97% | 0.0% |
| `vyre-driver-wgpu/tests/__split` | 137 | 6158.46 | 2.59% | 0.0% |
| `vyre-driver-cuda/src` | 33 | 5988.44 | 6.57% | 64.58% |
| `vyre-primitives/src/math` | 43 | 5670.52 | 9.9% | 57.99% |
| `vyre-bench/src/cases` | 39 | 4775.42 | 12.35% | 43.95% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `conform/vyre-conform-generate/src/minimizer.rs` -> **100.0%** Exposure
- `vyre-bench/src/cases/c_parser/syntax_corpus.rs` -> **100.0%** Exposure
- `vyre-driver/src/backend/capability.rs` -> **100.0%** Exposure
- `vyre-driver/src/strategy/mod.rs` -> **100.0%** Exposure
- `vyre-emit-naga/src/program/mod_tests.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `vyre-driver-cuda/src/egraph_kernel_plan/args.rs` -> **100.0%** Exposure
- `vyre-driver-wgpu/tests/common/c_fixture.rs` -> **100.0%** Exposure
- `vyre-foundation/src/execution_plan/fusion/fuse.rs` -> **100.0%** Exposure
- `vyre-foundation/src/serial/wire/tags/atomic_op_tag.rs` -> **100.0%** Exposure
- `vyre-frontend-c/src/pipeline/compile_unit.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `vyre-foundation/src/optimizer/eqsat_gpu.rs` -> **21** Orphaned Functions | **35** Duplicates
- `vyre-driver/src/numeric.rs` -> **15** Orphaned Functions | **40** Duplicates
- `vyre-foundation/src/optimizer/scheduler/tests.rs` -> **13** Orphaned Functions | **36** Duplicates
- `vyre-libs/tests/gpu_if_expression_roundtrip.rs` -> **47** Orphaned Functions | **0** Duplicates
- `vyre-driver/src/pipeline/tests/passthrough.rs` -> **19** Orphaned Functions | **27** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`vyre-foundation/src/optimizer/pass_catalog.rs`** -> AI Confidence: **99.48%**
2. **`vyre-foundation/src/serial/wire/encode/put_node.rs`** -> AI Confidence: **99.48%**
3. **`vyre-foundation/src/optimizer/dsl.rs`** -> AI Confidence: **99.32%**
4. **`vyre-primitives/tests/proptest_reduce_any_all.rs`** -> AI Confidence: **99.32%**
5. **`tools/divergence-gate.py`** -> AI Confidence: **99.31%**
6. **`conform/vyre-conform-runner/tests/ulp_audit.rs`** -> AI Confidence: **99.31%**
7. **`vyre-aot/src/launcher.rs`** -> AI Confidence: **99.31%**
8. **`vyre-bench/src/cases/cuda_ptx_patterns.rs`** -> AI Confidence: **99.31%**
9. **`vyre-bench/src/cli.rs`** -> AI Confidence: **99.31%**
10. **`vyre-bench/src/release_matrix.rs`** -> AI Confidence: **99.31%**
11. **`vyre-bench/src/runner/execute/collect.rs`** -> AI Confidence: **99.31%**
12. **`vyre-bench/src/runner/execute/run_case.rs`** -> AI Confidence: **99.31%**
13. **`vyre-debug/src/bin/vyre_dbg.rs`** -> AI Confidence: **99.31%**
14. **`vyre-driver-cuda/src/aot_launcher.rs`** -> AI Confidence: **99.31%**
15. **`vyre-driver-cuda/src/backend/capabilities.rs`** -> AI Confidence: **99.31%**
16. **`vyre-driver-cuda/src/backend/cuda_graph.rs`** -> AI Confidence: **99.31%**
17. **`vyre-driver-cuda/src/backend/cuda_graph_replay.rs`** -> AI Confidence: **99.31%**
18. **`vyre-driver-cuda/src/backend/resident.rs`** -> AI Confidence: **99.31%**
19. **`vyre-driver-cuda/src/backend/resident_io.rs`** -> AI Confidence: **99.31%**
20. **`vyre-driver-cuda/src/egraph_device_image.rs`** -> AI Confidence: **99.31%**
21. **`vyre-driver-cuda/src/lib.rs`** -> AI Confidence: **99.31%**
22. **`vyre-driver-cuda/src/pipeline/compiled_dispatch.rs`** -> AI Confidence: **99.31%**
23. **`vyre-driver-cuda/src/pipeline/materialized_cache.rs`** -> AI Confidence: **99.31%**
24. **`vyre-driver-cuda/tests/module_cache_contracts.rs`** -> AI Confidence: **99.31%**
25. **`vyre-driver-wgpu/src/engine/record_and_readback/bind_groups.rs`** -> AI Confidence: **99.31%**
26. **`vyre-driver-wgpu/src/pipeline/compiled_dispatch.rs`** -> AI Confidence: **99.31%**
27. **`vyre-driver-wgpu/src/pipeline/descriptor_metadata.rs`** -> AI Confidence: **99.31%**
28. **`vyre-driver-wgpu/src/pipeline/persistent.rs`** -> AI Confidence: **99.31%**
29. **`vyre-driver-wgpu/src/pipeline/persistent_resources.rs`** -> AI Confidence: **99.31%**
30. **`vyre-driver-wgpu/src/runtime/prerecorded.rs`** -> AI Confidence: **99.31%**
31. **`vyre-driver-wgpu/tests/__split/op_pairwise_chunk1.rs`** -> AI Confidence: **99.31%**
32. **`vyre-driver-wgpu/tests/c_preprocess_gpu_if_expression.rs`** -> AI Confidence: **99.31%**
33. **`vyre-driver-wgpu/tests/naga_loop_region_followup.rs`** -> AI Confidence: **99.31%**
34. **`vyre-driver/src/megakernel_execution.rs`** -> AI Confidence: **99.31%**
35. **`vyre-driver/src/pipeline/compiler.rs`** -> AI Confidence: **99.31%**
36. **`vyre-emit-naga/src/emitter/binop.rs`** -> AI Confidence: **99.31%**
37. **`vyre-emit-naga/tests/adversarial_emit_program_matrix.rs`** -> AI Confidence: **99.31%**
38. **`vyre-emit-ptx/src/emitter.rs`** -> AI Confidence: **99.31%**
39. **`vyre-emit-ptx/src/emitter/body.rs`** -> AI Confidence: **99.31%**
40. **`vyre-emit-ptx/src/emitter/mma.rs`** -> AI Confidence: **99.31%**
41. **`vyre-emit-ptx/src/emitter/vector.rs`** -> AI Confidence: **99.31%**
42. **`vyre-emit-ptx/src/patterns/vec_memory_fusion.rs`** -> AI Confidence: **99.31%**
43. **`vyre-foundation/src/ir_inner/model/node_kind.rs`** -> AI Confidence: **99.31%**
44. **`vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`** -> AI Confidence: **99.31%**
45. **`vyre-foundation/src/optimizer/passes/algebraic/strength_reduce/mod.rs`** -> AI Confidence: **99.31%**
46. **`vyre-foundation/src/optimizer/passes/loops/loop_lower_bound_normalize.rs`** -> AI Confidence: **99.31%**
47. **`vyre-foundation/src/optimizer/passes/loops/loop_unroll.rs`** -> AI Confidence: **99.31%**
48. **`vyre-foundation/src/optimizer/passes/memory/store_to_load_forward.rs`** -> AI Confidence: **99.31%**
49. **`vyre-foundation/src/optimizer/scheduler/run.rs`** -> AI Confidence: **99.31%**
50. **`vyre-foundation/src/serial/wire/decode/impl_reader.rs`** -> AI Confidence: **99.31%**
51. **`vyre-foundation/src/serial/wire/encode/put_expr.rs`** -> AI Confidence: **99.31%**
52. **`vyre-foundation/src/transform/compiler/dominator_tree.rs`** -> AI Confidence: **99.31%**
53. **`vyre-foundation/src/transform/inline/expand/impl_calleeexpander/composition.rs`** -> AI Confidence: **99.31%**
54. **`vyre-foundation/src/vast/validate.rs`** -> AI Confidence: **99.31%**
55. **`vyre-foundation/tests/autodiff_transform_contracts.rs`** -> AI Confidence: **99.31%**
56. **`vyre-foundation/tests/extern_registry_adversarial.rs`** -> AI Confidence: **99.31%**
57. **`vyre-frontend-c/src/megakernel_workspace/workspace.rs`** -> AI Confidence: **99.31%**
58. **`vyre-frontend-c/src/pipeline/semantic_fast_path.rs`** -> AI Confidence: **99.31%**
59. **`vyre-harness/src/lib.rs`** -> AI Confidence: **99.31%**
60. **`vyre-libs/src/math/algebra.rs`** -> AI Confidence: **99.31%**
61. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/cache/payload_codec.rs`** -> AI Confidence: **99.31%**
62. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_table.rs`** -> AI Confidence: **99.31%**
63. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/segments.rs`** -> AI Confidence: **99.31%**
64. **`vyre-libs/src/parsing/c/preprocess/synthesis.rs`** -> AI Confidence: **99.31%**
65. **`vyre-libs/src/parsing/c/sema/registry/reference.rs`** -> AI Confidence: **99.31%**
66. **`vyre-libs/src/primitive_catalog.rs`** -> AI Confidence: **99.31%**
67. **`vyre-libs/src/rule/ast.rs`** -> AI Confidence: **99.31%**
68. **`vyre-libs/tests/gpu_if_expression_roundtrip.rs`** -> AI Confidence: **99.31%**
69. **`vyre-libs/tests/op_boundaries.rs`** -> AI Confidence: **99.31%**
70. **`vyre-libs/tests/sweep_text_utf8_oracle_matrix.rs`** -> AI Confidence: **99.31%**
71. **`vyre-lints/src/gpu_skip_guards.rs`** -> AI Confidence: **99.31%**
72. **`vyre-lints/src/main.rs`** -> AI Confidence: **99.31%**
73. **`vyre-lints/src/module_forks.rs`** -> AI Confidence: **99.31%**
74. **`vyre-lower/src/rewrites/branch_collapse/mod.rs`** -> AI Confidence: **99.31%**
75. **`vyre-primitives/examples/wire_harness_smoke.rs`** -> AI Confidence: **99.31%**
76. **`vyre-primitives/src/graph/vast_tree_walk.rs`** -> AI Confidence: **99.31%**
77. **`vyre-primitives/src/text/line_index.rs`** -> AI Confidence: **99.31%**
78. **`vyre-primitives/src/text/utf8_validate.rs`** -> AI Confidence: **99.31%**
79. **`vyre-reference/src/execution/expr.rs`** -> AI Confidence: **99.31%**
80. **`vyre-reference/src/execution/typed_ops/mod.rs`** -> AI Confidence: **99.31%**
81. **`vyre-reference/src/workgroup.rs`** -> AI Confidence: **99.31%**
82. **`vyre-runtime/src/megakernel/io/complete.rs`** -> AI Confidence: **99.31%**
83. **`vyre-runtime/src/megakernel/io/poll.rs`** -> AI Confidence: **99.31%**
84. **`vyre-runtime/src/megakernel/protocol/codec.rs`** -> AI Confidence: **99.31%**
85. **`vyre-runtime/src/uring/io_loop.rs`** -> AI Confidence: **99.31%**
86. **`vyre-self-substrate/src/graph/csr_frontier_queue_batch_resident/dispatch.rs`** -> AI Confidence: **99.31%**
87. **`xtask/src/c_parser_bench.rs`** -> AI Confidence: **99.31%**
88. **`xtask/src/conformance_matrix.rs`** -> AI Confidence: **99.31%**
89. **`xtask/src/heuristic_audit.rs`** -> AI Confidence: **99.31%**
90. **`xtask/src/hygiene_matrix.rs`** -> AI Confidence: **99.31%**
91. **`xtask/src/lego_audit.rs`** -> AI Confidence: **99.31%**
92. **`xtask/src/metadata_matrix.rs`** -> AI Confidence: **99.31%**
93. **`xtask/src/op_matrix.rs`** -> AI Confidence: **99.31%**
94. **`xtask/src/release_completion_audit.rs`** -> AI Confidence: **99.31%**
95. **`xtask/src/source_similar.rs`** -> AI Confidence: **99.31%**
96. **`xtask/src/test_matrix.rs`** -> AI Confidence: **99.31%**
97. **`xtask/src/vyre_weir_release_gate.rs`** -> AI Confidence: **99.31%**
98. **`vyre-aot/examples/vyre_aot_release_surface.rs`** -> AI Confidence: **99.29%**
99. **`vyre-debug/examples/vyre_debug_release_surface.rs`** -> AI Confidence: **99.29%**
100. **`vyre-driver-reference/examples/vyre_driver_reference_release_surface.rs`** -> AI Confidence: **99.29%**
101. **`vyre-driver-wgpu/src/descriptor_mapping.rs`** -> AI Confidence: **99.29%**
102. **`vyre-driver/examples/vyre_driver_release_surface.rs`** -> AI Confidence: **99.29%**
103. **`vyre-driver/src/bindless_policy.rs`** -> AI Confidence: **99.29%**
104. **`vyre-emit-naga/examples/vyre_emit_naga_release_surface.rs`** -> AI Confidence: **99.29%**
105. **`vyre-emit-ptx/examples/vyre_emit_ptx_release_surface.rs`** -> AI Confidence: **99.29%**
106. **`vyre-emit-spirv/examples/vyre_emit_spirv_release_surface.rs`** -> AI Confidence: **99.29%**
107. **`vyre-foundation/examples/vyre_foundation_release_surface.rs`** -> AI Confidence: **99.29%**
108. **`vyre-foundation/src/execution_plan/fusion/divergence.rs`** -> AI Confidence: **99.29%**
109. **`vyre-foundation/src/optimizer/passes/algebraic/const_fold/tests/helpers.rs`** -> AI Confidence: **99.29%**
110. **`vyre-foundation/src/optimizer/passes/fusion_cse/cse/expr_has_effect.rs`** -> AI Confidence: **99.29%**
111. **`vyre-frontend-c/src/pipeline/vast_pg/fusion.rs`** -> AI Confidence: **99.29%**
112. **`vyre-frontend-c/src/tu_host/preprocess/ident.rs`** -> AI Confidence: **99.29%**
113. **`vyre-harness/examples/vyre_harness_release_surface.rs`** -> AI Confidence: **99.29%**
114. **`vyre-intrinsics/examples/vyre_intrinsics_release_surface.rs`** -> AI Confidence: **99.29%**
115. **`vyre-libs/src/buffer_names.rs`** -> AI Confidence: **99.29%**
116. **`vyre-libs/src/parsing/c/parse/vast_kinds.rs`** -> AI Confidence: **99.29%**
117. **`vyre-libs/src/parsing/c/source_bytes.rs`** -> AI Confidence: **99.29%**
118. **`vyre-libs/src/security/catalog.rs`** -> AI Confidence: **99.29%**
119. **`vyre-lints/examples/vyre_lints_release_surface.rs`** -> AI Confidence: **99.29%**
120. **`vyre-macros/examples/vyre_macros_release_surface.rs`** -> AI Confidence: **99.29%**
121. **`vyre-primitives/examples/vyre_primitives_release_surface.rs`** -> AI Confidence: **99.29%**
122. **`vyre-reference/examples/vyre_reference_release_surface.rs`** -> AI Confidence: **99.29%**
123. **`vyre-reference/src/dual_impls/bitwise/and/mod.rs`** -> AI Confidence: **99.29%**
124. **`vyre-reference/src/dual_impls/bitwise/or/mod.rs`** -> AI Confidence: **99.29%**
125. **`vyre-runtime/examples/vyre_runtime_release_surface.rs`** -> AI Confidence: **99.29%**
126. **`vyre-self-substrate/examples/vyre_self_substrate_release_surface.rs`** -> AI Confidence: **99.29%**
127. **`vyre-self-substrate/src/optimizer/dead_branch.rs`** -> AI Confidence: **99.29%**
128. **`xtask/src/bin/vyre_new_op/allowed_archetypes.rs`** -> AI Confidence: **99.29%**
129. **`xtask/src/bin/vyre_new_op/generate_readme.rs`** -> AI Confidence: **99.29%**
130. **`xtask/src/quick/eval_xor.rs`** -> AI Confidence: **99.29%**
131. **`xtask/src/quick_cache/eval_and.rs`** -> AI Confidence: **99.29%**
132. **`scripts/bench_index.sh`** -> AI Confidence: **99.29%**
133. **`scripts/check_architectural_invariants.sh`** -> AI Confidence: **99.29%**
134. **`scripts/check_base_monument.sh`** -> AI Confidence: **99.29%**
135. **`scripts/check_ci_matrix.sh`** -> AI Confidence: **99.29%**
136. **`scripts/check_crate_metadata_normalized.sh`** -> AI Confidence: **99.29%**
137. **`scripts/check_dialect_coverage.sh`** -> AI Confidence: **99.29%**
138. **`scripts/check_doc_claim_to_test.sh`** -> AI Confidence: **99.29%**
139. **`scripts/check_lib_rs_headers.sh`** -> AI Confidence: **99.29%**
140. **`scripts/check_max_public_module_surface.sh`** -> AI Confidence: **99.29%**
141. **`scripts/check_no_closed_ir_enums.sh`** -> AI Confidence: **99.29%**
142. **`scripts/check_no_hot_path_vec_vec.sh`** -> AI Confidence: **99.29%**
143. **`scripts/check_parity_testing_not_leaked.sh`** -> AI Confidence: **99.29%**
144. **`scripts/check_publish_gate.sh`** -> AI Confidence: **99.29%**
145. **`scripts/check_release_signoff.sh`** -> AI Confidence: **99.29%**
146. **`scripts/check_required_ci_jobs.sh`** -> AI Confidence: **99.29%**
147. **`scripts/check_roadmap_status_split.sh`** -> AI Confidence: **99.29%**
148. **`scripts/check_substrate_layout.sh`** -> AI Confidence: **99.29%**
149. **`scripts/check_trait_freeze.sh`** -> AI Confidence: **99.29%**
150. **`scripts/docs.sh`** -> AI Confidence: **99.29%**
151. **`scripts/install_wire_precommit_hook.sh`** -> AI Confidence: **99.29%**
152. **`scripts/laws/check_layout.sh`** -> AI Confidence: **99.29%**
153. **`scripts/laws/check_readmes.sh`** -> AI Confidence: **99.29%**
154. **`scripts/prove-release-shards.sh`** -> AI Confidence: **99.29%**
155. **`scripts/publish-dryrun.sh`** -> AI Confidence: **99.29%**
156. **`scripts/wait-crates-index.sh`** -> AI Confidence: **99.29%**
157. **`vyre-harness/src/fp_contract.rs`** -> AI Confidence: **99.25%**
158. **`vyre-self-substrate/src/optimizer/licm.rs`** -> AI Confidence: **99.25%**
159. **`conform/vyre-conform-runner/src/main.rs`** -> AI Confidence: **99.24%**
160. **`vyre-aot/src/bundle.rs`** -> AI Confidence: **99.24%**
161. **`vyre-aot/tests/generated_artifact_manifest_matrix.rs`** -> AI Confidence: **99.24%**
162. **`vyre-bench/src/api/resident.rs`** -> AI Confidence: **99.24%**
163. **`vyre-bench/src/cases/c_parser/support.rs`** -> AI Confidence: **99.24%**
164. **`vyre-bench/src/cases/nvme_gpu_ingest.rs`** -> AI Confidence: **99.24%**
165. **`vyre-bench/src/cases/release_workloads.rs`** -> AI Confidence: **99.24%**
166. **`vyre-core/tests/wire_malformed_adversarial.rs`** -> AI Confidence: **99.24%**
167. **`vyre-debug/src/dangling.rs`** -> AI Confidence: **99.24%**
168. **`vyre-driver-cuda/src/backend/dispatch.rs`** -> AI Confidence: **99.24%**
169. **`vyre-driver-cuda/src/backend/host_dispatch.rs`** -> AI Confidence: **99.24%**
170. **`vyre-driver-cuda/src/backend/resident_dispatch.rs`** -> AI Confidence: **99.24%**
171. **`vyre-driver-cuda/src/optimizer.rs`** -> AI Confidence: **99.24%**
172. **`vyre-driver-cuda/src/resident_graph_session.rs`** -> AI Confidence: **99.24%**
173. **`vyre-driver-cuda/src/stream.rs`** -> AI Confidence: **99.24%**
174. **`vyre-driver-reference/src/lib.rs`** -> AI Confidence: **99.24%**
175. **`vyre-driver-wgpu/src/backend_impl.rs`** -> AI Confidence: **99.24%**
176. **`vyre-driver-wgpu/src/bin/vyre.rs`** -> AI Confidence: **99.24%**
177. **`vyre-driver-wgpu/src/engine/record_and_readback.rs`** -> AI Confidence: **99.24%**
178. **`vyre-driver-wgpu/src/engine/record_and_readback/staging.rs`** -> AI Confidence: **99.24%**
179. **`vyre-driver-wgpu/src/engine/record_and_readback/submit.rs`** -> AI Confidence: **99.24%**
180. **`vyre-driver-wgpu/src/engine/streaming/async_copy.rs`** -> AI Confidence: **99.24%**
181. **`vyre-driver-wgpu/src/megakernel.rs`** -> AI Confidence: **99.24%**
182. **`vyre-driver-wgpu/src/megakernel/dispatcher.rs`** -> AI Confidence: **99.24%**
183. **`vyre-driver-wgpu/src/runtime/cache/pipeline.rs`** -> AI Confidence: **99.24%**
184. **`vyre-driver-wgpu/src/runtime/readback_ring.rs`** -> AI Confidence: **99.24%**
185. **`vyre-driver-wgpu/src/runtime/shader.rs`** -> AI Confidence: **99.24%**
186. **`vyre-driver-wgpu/tests/__split/c_ast_statement_construct_gaps_e2e_chunk1.rs`** -> AI Confidence: **99.24%**
187. **`vyre-driver/src/backend/registry/acquire.rs`** -> AI Confidence: **99.24%**
188. **`vyre-driver/src/backend/vyre_backend.rs`** -> AI Confidence: **99.24%**
189. **`vyre-driver/src/device_signature.rs`** -> AI Confidence: **99.24%**
190. **`vyre-driver/src/launch.rs`** -> AI Confidence: **99.24%**
191. **`vyre-driver/src/resident_transfer_fusion.rs`** -> AI Confidence: **99.24%**
192. **`vyre-driver/src/validation.rs`** -> AI Confidence: **99.24%**
193. **`vyre-driver/tests/sweep_numeric_oracle_matrix.rs`** -> AI Confidence: **99.24%**
194. **`vyre-emit-naga/src/emitter/binding_helpers.rs`** -> AI Confidence: **99.24%**
195. **`vyre-emit-naga/src/emitter/op_dispatch.rs`** -> AI Confidence: **99.24%**
196. **`vyre-emit-naga/src/emitter/op_lookup.rs`** -> AI Confidence: **99.24%**
197. **`vyre-emit-naga/src/patterns/vec_pack/analysis.rs`** -> AI Confidence: **99.24%**
198. **`vyre-emit-ptx/src/index_facts.rs`** -> AI Confidence: **99.24%**
199. **`vyre-emit-ptx/tests/cross_emitter_parity.rs`** -> AI Confidence: **99.24%**
200. **`vyre-foundation/src/dispatch/extension.rs`** -> AI Confidence: **99.24%**
201. **`vyre-foundation/src/lower/subgroup_lowering.rs`** -> AI Confidence: **99.24%**
202. **`vyre-foundation/src/optimizer/passes/cleanup/region_fusion_hint.rs`** -> AI Confidence: **99.24%**
203. **`vyre-foundation/src/optimizer/passes/cleanup/rematerialize_cheap_let.rs`** -> AI Confidence: **99.24%**
204. **`vyre-foundation/src/optimizer/passes/fusion_cse/fusion_tests.rs`** -> AI Confidence: **99.24%**
205. **`vyre-foundation/src/optimizer/passes/loops/loop_licm.rs`** -> AI Confidence: **99.24%**
206. **`vyre-foundation/src/optimizer/passes/loops/loop_var_range_fold.rs`** -> AI Confidence: **99.24%**
207. **`vyre-foundation/src/optimizer/passes/memory/dead_store_elim.rs`** -> AI Confidence: **99.24%**
208. **`vyre-foundation/src/serial/wire/decode/from_wire.rs`** -> AI Confidence: **99.24%**
209. **`vyre-foundation/src/serial/wire/encode/to_wire.rs`** -> AI Confidence: **99.24%**
210. **`vyre-foundation/src/transform/inline/impl_inlinectx.rs`** -> AI Confidence: **99.24%**
211. **`vyre-foundation/src/validate/typecheck.rs`** -> AI Confidence: **99.24%**
212. **`vyre-frontend-c/src/api/lex_index.rs`** -> AI Confidence: **99.24%**
213. **`vyre-frontend-c/src/api/object_decode/abi.rs`** -> AI Confidence: **99.24%**
214. **`vyre-frontend-c/src/api/resident_syntax.rs`** -> AI Confidence: **99.24%**
215. **`vyre-frontend-c/src/pipeline/buffers/abi.rs`** -> AI Confidence: **99.24%**
216. **`vyre-frontend-c/src/pipeline/sema.rs`** -> AI Confidence: **99.24%**
217. **`vyre-frontend-c/tests/megakernel_workspace_contracts.rs`** -> AI Confidence: **99.24%**
218. **`vyre-libs/src/compiler/regalloc.rs`** -> AI Confidence: **99.24%**
219. **`vyre-libs/src/math/conv/im2col.rs`** -> AI Confidence: **99.24%**
220. **`vyre-libs/src/nn/linear/inner/tiled.rs`** -> AI Confidence: **99.24%**
221. **`vyre-libs/src/parsing/c/parse/gnu_builtin_catalog.rs`** -> AI Confidence: **99.24%**
222. **`vyre-libs/src/parsing/c/parse/inline_asm.rs`** -> AI Confidence: **99.24%**
223. **`vyre-libs/src/parsing/c/preprocess/effects.rs`** -> AI Confidence: **99.24%**
224. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/directives.rs`** -> AI Confidence: **99.24%**
225. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/conditional_directives.rs`** -> AI Confidence: **99.24%**
226. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/directive_walk.rs`** -> AI Confidence: **99.24%**
227. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/file_inputs.rs`** -> AI Confidence: **99.24%**
228. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/scan.rs`** -> AI Confidence: **99.24%**
229. **`vyre-libs/src/parsing/c/preprocess/mod.rs`** -> AI Confidence: **99.24%**
230. **`vyre-libs/src/scan/regex_dfa.rs`** -> AI Confidence: **99.24%**
231. **`vyre-libs/src/substrate_catalog.rs`** -> AI Confidence: **99.24%**
232. **`vyre-libs/src/visual/blur/mod.rs`** -> AI Confidence: **99.24%**
233. **`vyre-libs/tests/surface_contracts.rs`** -> AI Confidence: **99.24%**
234. **`vyre-lower/examples/optimize.rs`** -> AI Confidence: **99.24%**
235. **`vyre-lower/src/lower.rs`** -> AI Confidence: **99.24%**
236. **`vyre-lower/src/rewrites/bank_conflict_pad/mod.rs`** -> AI Confidence: **99.24%**
237. **`vyre-lower/src/rewrites/body_index.rs`** -> AI Confidence: **99.24%**
238. **`vyre-lower/src/rewrites/descriptor_const_fold/mod.rs`** -> AI Confidence: **99.24%**
239. **`vyre-lower/src/rewrites/identity_elim/mod.rs`** -> AI Confidence: **99.24%**
240. **`vyre-lower/src/verify/mod.rs`** -> AI Confidence: **99.24%**
241. **`vyre-macros/src/algebraic_laws.rs`** -> AI Confidence: **99.24%**
242. **`vyre-macros/src/define_op.rs`** -> AI Confidence: **99.24%**
243. **`vyre-primitives/src/graph/exploded.rs`** -> AI Confidence: **99.24%**
244. **`vyre-primitives/src/graph/matroid.rs`** -> AI Confidence: **99.24%**
245. **`vyre-primitives/src/graph/tensor_flow_forward.rs`** -> AI Confidence: **99.24%**
246. **`vyre-primitives/src/graph/toposort.rs`** -> AI Confidence: **99.24%**
247. **`vyre-primitives/src/math/dot_partial.rs`** -> AI Confidence: **99.24%**
248. **`vyre-primitives/tests/sweep_hash_crc_oracle_matrix.rs`** -> AI Confidence: **99.24%**
249. **`vyre-reference/src/execution/call.rs`** -> AI Confidence: **99.24%**
250. **`vyre-reference/src/execution/hashmap/mod.rs`** -> AI Confidence: **99.24%**
251. **`vyre-reference/src/execution/hashmap/node_step.rs`** -> AI Confidence: **99.24%**
252. **`vyre-reference/src/execution/hashmap/state.rs`** -> AI Confidence: **99.24%**
253. **`vyre-reference/src/execution/node.rs`** -> AI Confidence: **99.24%**
254. **`vyre-runtime/src/megakernel/execution.rs`** -> AI Confidence: **99.24%**
255. **`vyre-runtime/src/megakernel/execution/persistent_handles.rs`** -> AI Confidence: **99.24%**
256. **`vyre-runtime/src/megakernel/io/helpers.rs`** -> AI Confidence: **99.24%**
257. **`vyre-runtime/src/megakernel/planner/barriers.rs`** -> AI Confidence: **99.24%**
258. **`vyre-runtime/src/megakernel/telemetry.rs`** -> AI Confidence: **99.24%**
259. **`vyre-runtime/src/uring/driver.rs`** -> AI Confidence: **99.24%**
260. **`vyre-self-substrate/src/graph/csr_frontier_queue_resident/query.rs`** -> AI Confidence: **99.24%**
261. **`xtask/src/bin/vyre_new_op/run.rs`** -> AI Confidence: **99.24%**
262. **`xtask/src/dep_drift.rs`** -> AI Confidence: **99.24%**
263. **`xtask/src/lint_shape_tests.rs`** -> AI Confidence: **99.24%**
264. **`xtask/src/package_readiness.rs`** -> AI Confidence: **99.24%**
265. **`xtask/src/recursion_gate.rs`** -> AI Confidence: **99.24%**
266. **`xtask/src/release_benchmarks.rs`** -> AI Confidence: **99.24%**
267. **`conform/vyre-conform-runner/tests/lens_parity.rs`** -> AI Confidence: **99.23%**
268. **`vyre-bench/src/evolve/server.rs`** -> AI Confidence: **99.23%**
269. **`vyre-driver-cuda/src/codegen/descriptor_gate.rs`** -> AI Confidence: **99.23%**
270. **`vyre-driver-cuda/src/device.rs`** -> AI Confidence: **99.23%**
271. **`vyre-driver-cuda/src/pipeline/static_params.rs`** -> AI Confidence: **99.23%**
272. **`vyre-driver-wgpu/src/async_dispatch.rs`** -> AI Confidence: **99.23%**
273. **`vyre-driver-wgpu/src/pipeline/binding.rs`** -> AI Confidence: **99.23%**
274. **`vyre-driver-wgpu/tests/cat_a_conform.rs`** -> AI Confidence: **99.23%**
275. **`vyre-driver/src/benchmark_pass_selection.rs`** -> AI Confidence: **99.23%**
276. **`vyre-driver/src/megakernel_barrier.rs`** -> AI Confidence: **99.23%**
277. **`vyre-driver/src/program_walks/outputs.rs`** -> AI Confidence: **99.23%**
278. **`vyre-emit-ptx/src/emitter/atomic.rs`** -> AI Confidence: **99.23%**
279. **`vyre-emit-ptx/src/emitter/control.rs`** -> AI Confidence: **99.23%**
280. **`vyre-foundation/src/optimizer/passes/fusion_cse/cse/impl_csectx.rs`** -> AI Confidence: **99.23%**
281. **`vyre-foundation/src/serial/wire/tags/data_type_tag.rs`** -> AI Confidence: **99.23%**
282. **`vyre-foundation/src/transform/autodiff/grad/expr.rs`** -> AI Confidence: **99.23%**
283. **`vyre-frontend-c/src/pipeline/buffers/lexer_diagnostic_report.rs`** -> AI Confidence: **99.23%**
284. **`vyre-libs/src/math/atomic/atomic_lru_update.rs`** -> AI Confidence: **99.23%**
285. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/ifdef_truth_batch.rs`** -> AI Confidence: **99.23%**
286. **`vyre-lints/src/consumer_coupling.rs`** -> AI Confidence: **99.23%**
287. **`vyre-lints/src/raw_ir_in_libs.rs`** -> AI Confidence: **99.23%**
288. **`vyre-primitives/src/graph/dominator_tree.rs`** -> AI Confidence: **99.23%**
289. **`vyre-primitives/src/nn/quest_paging_passes.rs`** -> AI Confidence: **99.23%**
290. **`vyre-runtime/src/megakernel/protocol_api/publish.rs`** -> AI Confidence: **99.23%**
291. **`xtask/src/feature_matrix.rs`** -> AI Confidence: **99.23%**
292. **`xtask/src/measurement_gate.rs`** -> AI Confidence: **99.23%**
293. **`xtask/src/quick_cache/eval_or.rs`** -> AI Confidence: **99.23%**
294. **`xtask/src/release_conformance.rs`** -> AI Confidence: **99.23%**
295. **`scripts/laws/run_all.sh`** -> AI Confidence: **99.23%**
296. **`vyre-harness/src/region.rs`** -> AI Confidence: **99.22%**
297. **`scripts/lib/cargo_runner.sh`** -> AI Confidence: **99.22%**
298. **`conform/vyre-conform-enforce/tests/__split/composition_discipline_chunk1.rs`** -> AI Confidence: **99.2%**
299. **`conform/vyre-conform-runner/src/bundle_cert.rs`** -> AI Confidence: **99.18%**
300. **`vyre-bench/src/cases/adaptive_routing.rs`** -> AI Confidence: **99.18%**
301. **`vyre-bench/src/cases/adversarial.rs`** -> AI Confidence: **99.18%**
302. **`vyre-bench/src/cases/alias_aware_optimizations.rs`** -> AI Confidence: **99.18%**
303. **`vyre-bench/src/cases/bigint.rs`** -> AI Confidence: **99.18%**
304. **`vyre-bench/src/cases/c_parser/single_syntax.rs`** -> AI Confidence: **99.18%**
305. **`vyre-bench/src/cases/crypto.rs`** -> AI Confidence: **99.18%**
306. **`vyre-bench/src/cases/elementwise.rs`** -> AI Confidence: **99.18%**
307. **`vyre-bench/src/cases/hashtable.rs`** -> AI Confidence: **99.18%**
308. **`vyre-bench/src/cases/quantized_linear.rs`** -> AI Confidence: **99.18%**
309. **`vyre-bench/src/cases/regex_bt.rs`** -> AI Confidence: **99.18%**
310. **`vyre-bench/src/report/flame.rs`** -> AI Confidence: **99.18%**
311. **`vyre-bench/src/report/kernel_time_table.rs`** -> AI Confidence: **99.18%**
312. **`vyre-bench/tests/cross_emitter_property.rs`** -> AI Confidence: **99.18%**
313. **`vyre-driver-cuda/src/backend/telemetry.rs`** -> AI Confidence: **99.18%**
314. **`vyre-driver-cuda/src/megakernel_barrier_planner.rs`** -> AI Confidence: **99.18%**
315. **`vyre-driver-cuda/src/token_fact_frontier_execution.rs`** -> AI Confidence: **99.18%**
316. **`vyre-driver-cuda/tests/autodiff_cuda_parity.rs`** -> AI Confidence: **99.18%**
317. **`vyre-driver-cuda/tests/common/mod.rs`** -> AI Confidence: **99.18%**
318. **`vyre-driver-cuda/tests/generated_atomic_cuda_reference_matrix.rs`** -> AI Confidence: **99.18%**
319. **`vyre-driver-cuda/tests/generated_i32_cuda_reference_matrix.rs`** -> AI Confidence: **99.18%**
320. **`vyre-driver-cuda/tests/i3_i4_integration.rs`** -> AI Confidence: **99.18%**
321. **`vyre-driver-cuda/tests/multi_block_prefix_scan_gpu_parity.rs`** -> AI Confidence: **99.18%**
322. **`vyre-driver-cuda/tests/resident_dispatch_contracts.rs`** -> AI Confidence: **99.18%**
323. **`vyre-driver-cuda/tests/self_optimizer_const_fold_extended.rs`** -> AI Confidence: **99.18%**
324. **`vyre-driver-cuda/tests/self_optimizer_const_prop_e2e.rs`** -> AI Confidence: **99.18%**
325. **`vyre-driver-cuda/tests/self_optimizer_cse_let_dedupe_e2e.rs`** -> AI Confidence: **99.18%**
326. **`vyre-driver-cuda/tests/self_optimizer_dead_branch_e2e.rs`** -> AI Confidence: **99.18%**
327. **`vyre-driver-cuda/tests/vectorized_memory_live_cuda.rs`** -> AI Confidence: **99.18%**
328. **`vyre-driver-reference/tests/generated_boundary_matrix.rs`** -> AI Confidence: **99.18%**
329. **`vyre-driver-wgpu/src/engine/persistent.rs`** -> AI Confidence: **99.18%**
330. **`vyre-driver-wgpu/src/engine/streaming.rs`** -> AI Confidence: **99.18%**
331. **`vyre-driver-wgpu/src/megakernel/dispatch_plan.rs`** -> AI Confidence: **99.18%**
332. **`vyre-driver-wgpu/src/runtime/router.rs`** -> AI Confidence: **99.18%**
333. **`vyre-driver-wgpu/src/spirv_backend.rs`** -> AI Confidence: **99.18%**
334. **`vyre-driver-wgpu/src/thread_pool.rs`** -> AI Confidence: **99.18%**
335. **`vyre-driver-wgpu/tests/__split/c_ast_property_typedef_annotation_contracts_chunk1.rs`** -> AI Confidence: **99.18%**
336. **`vyre-driver-wgpu/tests/async_capability_innovation.rs`** -> AI Confidence: **99.18%**
337. **`vyre-driver-wgpu/tests/c_ast_declaration_container_nodes/gpu.rs`** -> AI Confidence: **99.18%**
338. **`vyre-driver-wgpu/tests/c_ast_gnu_extensions_e2e.rs`** -> AI Confidence: **99.18%**
339. **`vyre-driver-wgpu/tests/c_ast_gpu_parity_support/mod.rs`** -> AI Confidence: **99.18%**
340. **`vyre-driver-wgpu/tests/c_ast_preprocessor_token_stream_e2e.rs`** -> AI Confidence: **99.18%**
341. **`vyre-driver-wgpu/tests/c_ast_property_graph_consistency_contracts.rs`** -> AI Confidence: **99.18%**
342. **`vyre-driver-wgpu/tests/c_ast_property_span_monotonicity_contracts.rs`** -> AI Confidence: **99.18%**
343. **`vyre-driver-wgpu/tests/c_ast_semantic_edge_expectations_gnu_and_control_flow.rs`** -> AI Confidence: **99.18%**
344. **`vyre-driver-wgpu/tests/c_ast_string_init_e2e.rs`** -> AI Confidence: **99.18%**
345. **`vyre-driver-wgpu/tests/c_lower_ast_to_pg_nodes.rs`** -> AI Confidence: **99.18%**
346. **`vyre-driver-wgpu/tests/determinism_contract.rs`** -> AI Confidence: **99.18%**
347. **`vyre-driver-wgpu/tests/naga_findings_followup.rs`** -> AI Confidence: **99.18%**
348. **`vyre-driver-wgpu/tests/resident_timed_outputs.rs`** -> AI Confidence: **99.18%**
349. **`vyre-driver-wgpu/tests/self_optimizer_pipeline_e2e.rs`** -> AI Confidence: **99.18%**
350. **`vyre-driver-wgpu/tests/self_optimizer_scaling_bench.rs`** -> AI Confidence: **99.18%**
351. **`vyre-driver-wgpu/tests/trap_propagation.rs`** -> AI Confidence: **99.18%**
352. **`vyre-driver/src/backend.rs`** -> AI Confidence: **99.18%**
353. **`vyre-driver/src/backend/typed_dispatch.rs`** -> AI Confidence: **99.18%**
354. **`vyre-driver/src/device_extraction.rs`** -> AI Confidence: **99.18%**
355. **`vyre-driver/src/dispatch_policy.rs`** -> AI Confidence: **99.18%**
356. **`vyre-driver/src/graph_capture.rs`** -> AI Confidence: **99.18%**
357. **`vyre-driver/src/pipeline/hashing.rs`** -> AI Confidence: **99.18%**
358. **`vyre-driver/src/registry/registry.rs`** -> AI Confidence: **99.18%**
359. **`vyre-driver/src/shadow.rs`** -> AI Confidence: **99.18%**
360. **`vyre-driver/src/speculate.rs`** -> AI Confidence: **99.18%**
361. **`vyre-driver/tests/backend_capability_negotiation.rs`** -> AI Confidence: **99.18%**
362. **`vyre-driver/tests/backend_validation_defaults.rs`** -> AI Confidence: **99.18%**
363. **`vyre-driver/tests/driver_lifecycle_e2e.rs`** -> AI Confidence: **99.18%**
364. **`vyre-driver/tests/organization_contracts.rs`** -> AI Confidence: **99.18%**
365. **`vyre-emit-naga/src/tests.rs`** -> AI Confidence: **99.18%**
366. **`vyre-emit-ptx/src/emitter/async_copy.rs`** -> AI Confidence: **99.18%**
367. **`vyre-emit-ptx/src/emitter/scalar.rs`** -> AI Confidence: **99.18%**
368. **`vyre-emit-ptx/src/patterns/tensor_core_fragment/mod.rs`** -> AI Confidence: **99.18%**
369. **`vyre-foundation/src/allocation.rs`** -> AI Confidence: **99.18%**
370. **`vyre-foundation/src/analysis/graph_view.rs`** -> AI Confidence: **99.18%**
371. **`vyre-foundation/src/execution_plan/fusion/fuse.rs`** -> AI Confidence: **99.18%**
372. **`vyre-foundation/src/execution_plan/memory_budget.rs`** -> AI Confidence: **99.18%**
373. **`vyre-foundation/src/ir_inner/model/expr.rs`** -> AI Confidence: **99.18%**
374. **`vyre-foundation/src/ir_inner/model/node.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `vyre-libs/src/scan/test_fixtures.rs` -> **100.0%** Exposure
- `vyre-libs/tests/cache_key_collision.rs` -> **99.9995%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28172` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/check_registry_consistency.sh` (SHELL) -> Cumulative Risk: **810.06**
- **Archetype:** `file_cluster_4` (Distance: 12.566 IQR)
- **Magnitude:** 11.64 | **LOC:** 87 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 55.3)

### 2. `scripts/check_no_string_wgsl.sh` (SHELL) -> Cumulative Risk: **806.62**
- **Archetype:** `file_cluster_4` (Distance: 12.895 IQR)
- **Magnitude:** 10.29 | **LOC:** 130 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Concurrency (99.9775%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 54.4), `__global_context__` (Impact: 4.1)

### 3. `scripts/check_tests_can_fail.sh` (SHELL) -> Cumulative Risk: **795.56**
- **Archetype:** `file_cluster_4` (Distance: 14.122 IQR)
- **Magnitude:** 7.09 | **LOC:** 45 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 12.6), `Anonymous_Block` (Impact: 7.3), `Anonymous_Block` (Impact: 5.2)

### 4. `scripts/check_invariant_paths_exist.sh` (SHELL) -> Cumulative Risk: **794.27**
- **Archetype:** `file_cluster_4` (Distance: 11.751 IQR)
- **Magnitude:** 2.9 | **LOC:** 33 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Tech Debt (99.9999%), State Flux (99.995%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 15.0), `__global_context__` (Impact: 1.6)

### 5. `scripts/check_public_api.sh` (SHELL) -> Cumulative Risk: **790.31**
- **Archetype:** `file_cluster_4` (Distance: 13.503 IQR)
- **Magnitude:** 5.38 | **LOC:** 45 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 9.9), `Anonymous_Block_[Truncated]` (Impact: 7.4), `__global_context__` (Impact: 2.9)

### 6. `scripts/laws/check_mod_rs_size.sh` (SHELL) -> Cumulative Risk: **789.58**
- **Archetype:** `file_cluster_4` (Distance: 13.344 IQR)
- **Magnitude:** 4.28 | **LOC:** 44 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Tech Debt (99.9889%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 8.7), `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 4.2)

### 7. `scripts/check_audit_status_tags.sh` (SHELL) -> Cumulative Risk: **789.24**
- **Archetype:** `file_cluster_4` (Distance: 12.867 IQR)
- **Magnitude:** 5.6 | **LOC:** 48 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 16.9), `Anonymous_Block` (Impact: 5.2), `Anonymous_Block` (Impact: 5.2)

### 8. `scripts/check_trait_freeze.sh` (SHELL) -> Cumulative Risk: **785.27**
- **Archetype:** `file_cluster_4` (Distance: 12.918 IQR)
- **Magnitude:** 13.89 | **LOC:** 110 | **CtrlFlow:** 84.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Concurrency (99.7268%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 58.9), `extract_block` (Impact: 15.2), `__global_context__` (Impact: 4.1)

### 9. `scripts/check_bench_baselines.sh` (SHELL) -> Cumulative Risk: **784.01**
- **Archetype:** `file_cluster_4` (Distance: 12.407 IQR)
- **Magnitude:** 3.24 | **LOC:** 39 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Stability (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 8.7), `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 2.9)

### 10. `scripts/laws/check_file_sizes.sh` (SHELL) -> Cumulative Risk: **782.23**
- **Archetype:** `file_cluster_4` (Distance: 13.378 IQR)
- **Magnitude:** 4.3 | **LOC:** 49 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Tech Debt (99.9835%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 8.8), `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 4.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `xtask/src/release_completion_audit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.266 IQR)
- **Top Global Matches:** file_cluster_8: 11.266, file_cluster_7: 11.93, file_cluster_17: 12.073
- **Magnitude:** 2784.52 | **LOC:** 6411 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.998%), Tech Debt (8.2198%)
**Top Internal Functions/Classes:**
  * `inspect_json_evidence` (Impact: 153.7)
  * `inspect_backend_suite_semantics` (Impact: 104.8)
  * `inspect_pass_family_benchmark_manifest_s` (Impact: 104.4)
  * `run` (Impact: 99.0)
  * `inspect_release_workload_matrix_semantic` (Impact: 97.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 902`, `structural_boundaries: 497`, `args: 334`, `func_start: 87`, `class_start: 6`
* *Risk/State:* `state_mutation: 179`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 11`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 319`, `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io::self, PathBuf, std::collections::BTreeSet, serde::Deserialize, Read, std::fs, Serialize, std::path::Path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xtask/src/vyre_weir_release_gate.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.13 IQR)
- **Top Global Matches:** file_cluster_8: 11.13, file_cluster_7: 11.797, file_cluster_17: 11.998
- **Magnitude:** 1969.5 | **LOC:** 6940 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8199%), Tech Debt (9.644%)
**Top Internal Functions/Classes:**
  * `run_semantic_requirement_checks` (Impact: 329.6)
  * `check_backend_suite_report` (Impact: 161.8)
  * `check_workload_matrix_artifact_coverage` (Impact: 105.8)
  * `run` (Impact: 78.0)
  * `check_parser_contract_evidence` (Impact: 76.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 887`, `structural_boundaries: 554`, `args: 280`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 128`, `planned_debt: 7`, `fragile_debt: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 364`, `doc: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io::self, PathBuf, std::collections::BTreeSet, serde::Deserialize, Read, std::fs, std::path::Path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/resident_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.078 IQR)
- **Top Global Matches:** file_cluster_8: 13.078, file_cluster_13: 13.254, file_cluster_0: 13.3
- **Magnitude:** 1929.42 | **LOC:** 2201 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.4503%), Tech Debt (24.4855%)
**Top Internal Functions/Classes:**
  * `fill_upload_resident_many_repeated_seque` (Impact: 396.9)
  * `dispatch_resident_async_concrete_with_pt` (Impact: 343.8)
  * `dispatch_resident_batch_async_concrete_w` (Impact: 217.8)
  * `dispatch_resident_via_borrowed_into` (Impact: 59.4)
  * `dispatch_resident_timed` (Impact: 36.9)
    * *Intent:* /// Dispatch with CUDA-resident buffers and return ordered output readbacks.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 488`, `args: 70`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 506`, `dead_code: 2`, `duplicate_logic: 4`, `orphaned_logic: 19`
* *Architecture:* `api: 20`, `concurrency: 2`, `import: 26`
* *Defense:* `safety: 175`, `doc: 4`, `test: 35`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FxHashSet, super::launch_params::launch_param_byte_len, std::ffi::c_void, super::ordering::sort_unstable_by_key_if_needed, CudaResidentDispatchStep, resize_vec_slots, DispatchConfig, super::plan::CudaDispatchPlan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/tests/cuda_graph_dispatch_parity.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.69 IQR)
- **Top Global Matches:** file_cluster_8: 9.69, file_cluster_17: 10.009, file_cluster_0: 10.257
- **Magnitude:** 1346.59 | **LOC:** 853 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.8683%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 189`, `args: 16`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 52`
* *Architecture:* `import: 6`
* *Defense:* `safety: 15`, `doc: 15`, `test: 77`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::Arc, common::bool_bytes, Node, DataType, DispatchConfig, vyre_foundation::ir::BufferAccess, std::time::Instant, u32_bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `conform/vyre-conform-runner/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.525 IQR)
- **Top Global Matches:** file_cluster_8: 12.525, file_cluster_17: 12.737, file_cluster_13: 12.831
- **Magnitude:** 1056.9 | **LOC:** 1952 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.6241%), Tech Debt (7.9768%)
**Top Internal Functions/Classes:**
  * `merge_certificates` (Impact: 108.9)
  * `read_and_verify_shard` (Impact: 73.0)
  * `prove` (Impact: 53.3)
  * `compare_backend_against_reference` (Impact: 41.5)
  * `backend_dispatch_plan` (Impact: 32.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 401`, `args: 147`, `func_start: 47`, `class_start: 15`
* *Risk/State:* `state_mutation: 200`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `concurrency: 28`, `import: 22`
* *Defense:* `safety: 193`, `doc: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_conform_runner::dispatch_grid, vyre_driver_cuda, vyre_driver_reference, BufferParity, VerifyingKey, serde::Serialize, SigningKey, ed25519_dalek::Signature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-primitives/src/graph/exploded.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.694 IQR)
- **Top Global Matches:** file_cluster_8: 11.694, file_cluster_7: 11.9, file_cluster_0: 11.937
- **Magnitude:** 1013.18 | **LOC:** 2317 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.5747%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_build_cpu_reference_into` (Impact: 173.7)
  * `ifds_program_cache_key_from_program` (Impact: 63.2)
  * `build_ifds_csr_program` (Impact: 44.1)
  * `validate_ifds_csr_inputs` (Impact: 41.7)
  * `validate_ifds_csr_layout` (Impact: 39.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 283`, `args: 92`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 180`
* *Architecture:* `api: 143`, `import: 9`
* *Defense:* `safety: 65`, `doc: 254`, `test: 116`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::Arc, vyre_foundation::ir::model::expr::Ident, Node, vyre_foundation::transform::visit::walk_exprs, DataType, vyre_foundation::ir::BufferAccess, vyre_foundation::ir::BinOp, vyre_foundation::transform::visit::walk_nodes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-bench/src/cases/release_workloads.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.256 IQR)
- **Top Global Matches:** file_cluster_8: 11.256, file_cluster_16: 11.816, file_cluster_7: 11.821
- **Magnitude:** 970.6 | **LOC:** 2595 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.8003%), Tech Debt (73.5866%)
**Top Internal Functions/Classes:**
  * `release_benchmark_csr_forward_baseline` (Impact: 36.5)
  * `callgraph_witness_digest` (Impact: 33.2)
  * `run` (Impact: 29.5)
  * `run` (Impact: 17.7)
  * `run_string_bitmap_scatter` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 254`, `args: 127`, `func_start: 110`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 201`, `duplicate_logic: 32`, `orphaned_logic: 6`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 69`, `doc: 21`, `test: 4`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_primitives::graph::program_graph::ProgramGraphShape, PreparedCase, MetricPoint, BenchRun, vyre::ir::BufferAccess, DeterminismClass, BenchMetadata, crate::api::case::
    BenchCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/c_parser_bench.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.992 IQR)
- **Top Global Matches:** file_cluster_8: 11.992, file_cluster_0: 12.303, file_cluster_17: 12.447
- **Magnitude:** 960.18 | **LOC:** 1933 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.6534%), Tech Debt (20.405%)
**Top Internal Functions/Classes:**
  * `is_release_evidence_valid` (Impact: 140.3)
  * `run_inner` (Impact: 110.9)
  * `parse_args` (Impact: 88.2)
  * `inspect_vyrecob2_sections` (Impact: 58.8)
  * `run_vyre_parser_file_range` (Impact: 42.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 278`, `args: 104`, `func_start: 54`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 140`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `safety: 180`, `doc: 1`, `test: 33`, `sync_locks: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` walkdir::WalkDir, vyre_frontend_c::api::
    parse_source, VyreCompileOptions, std::fs, vyre_driver_cuda, std::sync::atomic::AtomicU64, CParseSummary, std::path::PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/release_benchmarks.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.313 IQR)
- **Top Global Matches:** file_cluster_8: 12.313, file_cluster_17: 12.616, file_cluster_0: 12.76
- **Magnitude:** 924.76 | **LOC:** 2236 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.6889%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `inspect_backend_suite_artifact` (Impact: 115.6)
  * `run` (Impact: 78.2)
  * `inspect_optimization_benchmark_artifact` (Impact: 78.2)
  * `write_cpu_100x_proof` (Impact: 56.6)
  * `benchmark_artifact_is_reusable` (Impact: 40.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 362`, `args: 143`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 202`
* *Architecture:* `io: 10`, `api: 1`, `import: 6`
* *Defense:* `safety: 324`, `doc: 5`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PathBuf, std::process::Command, serde::Deserialize, Serialize, std::fs, Value, serde_json::json, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/lego_audit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.986 IQR)
- **Top Global Matches:** file_cluster_8: 11.986, file_cluster_7: 12.274, file_cluster_13: 12.298
- **Magnitude:** 893.48 | **LOC:** 1352 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2642%), Tech Debt (9.2205%)
**Top Internal Functions/Classes:**
  * `walk` (Impact: 365.1)
  * `check_4_cross_dialect_reachthrough` (Impact: 55.6)
  * `check_10_operand_shape_duplicate` (Impact: 48.8)
  * `check_5_god_files` (Impact: 30.7)
  * `check_9_name_stem_collision` (Impact: 28.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 149`, `args: 44`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 110`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 4`, `import: 6`
* *Defense:* `safety: 54`, `doc: 87`, `test: 7`, `sync_locks: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io::self, vyre::ir::Expr, Node, std::collections::BTreeMap, Read, HashMap, syn::spanned::Spanned, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/resident_io.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.751 IQR)
- **Top Global Matches:** file_cluster_8: 12.751, file_cluster_13: 12.913, file_cluster_0: 13.044
- **Magnitude:** 808.56 | **LOC:** 1060 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.1466%), Tech Debt (34.085%)
**Top Internal Functions/Classes:**
  * `download_resident_readback_batches_many_` (Impact: 72.0)
    * *Intent:* /// Download selected byte ranges from several resident-output batches into /// caller-owned output ...
  * `download_resident_ranges_into` (Impact: 63.5)
    * *Intent:* /// Download selected byte ranges from resident buffers into caller-owned /// output slots with one ...
  * `download_resident_readbacks_many_into` (Impact: 53.4)
    * *Intent:* /// Download selected byte ranges from several CUDA-resident buffers into /// caller-owned output sl...
  * `download_resident_fused_copy_batches_man` (Impact: 39.3)
  * `upload_resident_async_at` (Impact: 34.3)
    * *Intent:* /// Async H2D copy from a pinned host pointer into a CUDA-resident buffer. /// /// # Safety /// /// ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 193`, `args: 63`, `func_start: 40`
* *Risk/State:* `state_mutation: 211`, `orphaned_logic: 18`
* *Architecture:* `api: 22`, `concurrency: 10`, `import: 13`
* *Defense:* `safety: 77`, `doc: 44`, `test: 13`, `sync_locks: 4`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FusedResidentReadbacks, resize_vec_slots, reserved_vec, super::resident::CudaResidentBuffer, super::resident_readback_fusion::
    fuse_resident_readback_copies, crate::numeric::CUDA_NUMERIC, push_resident_upload_copy, super::capabilities::cuda_live_free_memory_bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-lower/src/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.676 IQR)
- **Top Global Matches:** file_cluster_8: 12.676, file_cluster_13: 12.872, file_cluster_0: 12.954
- **Magnitude:** 757.3 | **LOC:** 1928 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3846%), Tech Debt (18.8121%)
**Top Internal Functions/Classes:**
  * `lower_node` (Impact: 220.6)
  * `lower_expr` (Impact: 80.6)
  * `walk` (Impact: 37.7)
  * `collect_carrier_names` (Impact: 31.6)
  * `lower_child_node` (Impact: 30.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 170`, `args: 67`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 118`, `dead_code: 1`, `orphaned_logic: 11`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 135`, `doc: 70`, `test: 34`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FxHashSet, BufferAccess, super::*, vyre_foundation::ir::BufferDecl, Dispatch, OpaqueNodeData, KernelOp, MemoryKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/hygiene_matrix.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.688 IQR)
- **Top Global Matches:** file_cluster_8: 11.688, file_cluster_17: 12.081, file_cluster_11: 12.11
- **Magnitude:** 750.2 | **LOC:** 1196 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.4932%), Tech Debt (18.3078%)
**Top Internal Functions/Classes:**
  * `scan_file` (Impact: 79.0)
  * `scan_root` (Impact: 36.1)
  * `scan_audit_report_locations` (Impact: 35.9)
  * `run` (Impact: 33.1)
  * `scan_test_file` (Impact: 30.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 187`, `args: 118`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 176`, `planned_debt: 8`, `fragile_debt: 5`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 65`, `doc: 3`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io::self, walkdir::WalkDir, serde::Serialize, PathBuf, Read, std::fs, std::path::Path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-wgpu/src/megakernel.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.217 IQR)
- **Top Global Matches:** file_cluster_8: 12.217, file_cluster_0: 12.344, file_cluster_13: 12.477
- **Magnitude:** 738.08 | **LOC:** 1498 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.4753%), Tech Debt (56.1996%)
**Top Internal Functions/Classes:**
  * `dispatch_megakernel_with_io_queue_ref` (Impact: 134.3)
  * `megakernel_report_telemetry` (Impact: 54.0)
  * `ensure_resident_megakernel_buffers` (Impact: 35.0)
  * `strict_done_ring_slots_from_outputs` (Impact: 25.8)
  * `same_dispatch_shape` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 240`, `args: 106`, `func_start: 60`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 117`, `duplicate_logic: 15`
* *Architecture:* `api: 30`, `import: 15`
* *Defense:* `safety: 129`, `doc: 15`, `test: 67`, `sync_locks: 15`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MegakernelDispatch, Resource, MegakernelLaunchRecommendation, BatchDispatchSummary, HIT_RECORD_WORDS, DispatchConfig, super::*, WorkTriple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/source_similar.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.46 IQR)
- **Top Global Matches:** file_cluster_8: 11.46, file_cluster_0: 11.697, file_cluster_17: 11.791
- **Magnitude:** 712.88 | **LOC:** 1168 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.5946%), Tech Debt (21.3116%)
**Top Internal Functions/Classes:**
  * `normalize_tokens` (Impact: 84.2)
  * `has_control_flow_keyword` (Impact: 40.6)
  * `parse_args` (Impact: 31.9)
  * `source_shape` (Impact: 31.9)
  * `collect_rust_files_recursive` (Impact: 31.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 227`, `args: 130`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 94`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 57`, `doc: 7`, `test: 46`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` delta::delta, PathBuf, std::fs, HashSet, std::collections::HashMap, alpha::alpha, gamma::gamma, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-primitives/src/graph/persistent_bfs.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.939 IQR)
- **Top Global Matches:** file_cluster_8: 10.939, file_cluster_0: 11.135, file_cluster_7: 11.197
- **Magnitude:** 708.36 | **LOC:** 2349 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8818%), Tech Debt (70.6701%)
**Top Internal Functions/Classes:**
  * `try_cpu_ref_into_with_scratch` (Impact: 36.4)
    * *Intent:* /// CPU reference into caller-owned output storage. /// /// Runs BFS up to `max_iters` steps, accumu...
  * `validate_persistent_bfs_graph_layout` (Impact: 34.8)
  * `generated_try_cpu_ref_into_with_scratch_` (Impact: 32.4)
  * `try_persistent_bfs_batch` (Impact: 15.9)
  * `persistent_bfs` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 247`, `args: 104`, `func_start: 83`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 128`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 125`, `import: 8`
* *Defense:* `safety: 46`, `doc: 221`, `test: 128`, `sync_locks: 5`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::Arc, vyre_foundation::ir::model::expr::Ident, Node, fnv1a64_update_byte, DataType, vyre_foundation::ir::BufferAccess, crate::graph::program_graph::ProgramGraphShape, super::*...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `vyre-primitives/src/graph/dominator_tree.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.69 IQR)
- **Top Global Matches:** file_cluster_0: 12.69, file_cluster_8: 12.866, file_cluster_13: 13.053
- **Magnitude:** 688.42 | **LOC:** 1306 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.4867%), Tech Debt (39.0349%)
**Top Internal Functions/Classes:**
  * `try_lengauer_tarjan_idoms_into` (Impact: 120.2)
    * *Intent:* /// Construct empty dominator-tree CPU scratch. #[must_use]
  * `cooper_harvey_kennedy_idoms` (Impact: 95.9)
  * `validate_dominator_tree_inputs` (Impact: 46.9)
  * `try_compress_with_stack` (Impact: 28.6)
  * `try_idoms_to_dominator_sets` (Impact: 21.5)
    * *Intent:* /// Convert an idom array to per-node dominator sets (sorted). #[must_use]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 192`, `args: 55`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 176`, `dead_code: 3`, `orphaned_logic: 22`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `safety: 104`, `doc: 95`, `test: 76`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::Arc, vyre_foundation::ir::model::expr::Ident, Node, DataType, vyre_foundation::ir::BufferAccess, super::*, Expr, BufferDecl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/pipeline/compiled_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.86 IQR)
- **Top Global Matches:** file_cluster_8: 12.86, file_cluster_13: 13.126, file_cluster_17: 13.228
- **Magnitude:** 678.94 | **LOC:** 861 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.8088%), Tech Debt (21.823%)
**Top Internal Functions/Classes:**
  * `dispatch_borrowed_batched_via_cuda_graph` (Impact: 85.7)
  * `dispatch_borrowed_into` (Impact: 41.7)
  * `dispatch_borrowed_batched_into` (Impact: 41.7)
  * `dispatch_persistent_resource_outputs` (Impact: 41.2)
  * `dispatch_borrowed_timed` (Impact: 39.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 185`, `args: 33`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `state_mutation: 171`, `orphaned_logic: 10`
* *Architecture:* `import: 10`
* *Defense:* `safety: 111`, `doc: 5`, `sync_locks: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Resource, crate::backend::cuda_graph_replay::CudaGraphReplayStats, resize_vec_slots, crate::pipeline::materialized_cache::materialized_input_key, BindingRole, DispatchConfig, reserved_vec, crate::pipeline::
    cuda_graph_lane_count_for_batch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver/src/grid_sync.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.778 IQR)
- **Top Global Matches:** file_cluster_8: 12.778, file_cluster_0: 13.012, file_cluster_16: 13.019
- **Magnitude:** 662.84 | **LOC:** 1470 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.0248%), Tech Debt (97.5148%)
**Top Internal Functions/Classes:**
  * `dispatch_with_grid_sync_split_into` (Impact: 37.1)
    * *Intent:* /// [`VyreBackend::supports_grid_sync`]) bypass the split - the /// program is dispatched once. Back...
  * `dispatch_resident_with_grid_sync_split_t` (Impact: 31.5)
  * `hoist_grid_sync_barriers` (Impact: 30.6)
  * `refresh_readwrite_inputs` (Impact: 26.3)
  * `try_split_on_grid_sync` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 210`, `args: 62`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 228`, `fragile_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 15`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 86`, `doc: 124`, `test: 66`, `sync_locks: 10`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Resource, DispatchConfig, vyre_foundation::ir::Ident, super::*, OutputBuffers, std::sync::atomic::AtomicUsize, Ordering, vyre_foundation::ir::Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-foundation/src/optimizer/eqsat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.333 IQR)
- **Top Global Matches:** file_cluster_0: 13.333, file_cluster_16: 13.415, file_cluster_8: 13.539
- **Magnitude:** 658.62 | **LOC:** 1442 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.876%), Tech Debt (92.2218%)
**Top Internal Functions/Classes:**
  * `try_rebuild` (Impact: 34.3)
    * *Intent:* /// Equate two `EClasses`. The returned id is the canonical class for /// both inputs after the unio...
  * `try_saturate` (Impact: 33.1)
  * `try_add` (Impact: 30.5)
  * `try_union` (Impact: 28.1)
  * `try_dedup_enodes_by_hash` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 346`, `args: 102`, `func_start: 77`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 206`, `dead_code: 3`, `duplicate_logic: 10`, `orphaned_logic: 30`
* *Architecture:* `io: 1`, `api: 25`, `import: 8`
* *Defense:* `safety: 116`, `doc: 180`, `test: 88`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::error::Error, Hasher, smallvec::SmallVec, rustc_hash::FxHasher, rustc_hash::FxHashSet, std::fmt, rustc_hash::FxHashMap, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_values.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.771 IQR)
- **Top Global Matches:** file_cluster_8: 12.771, file_cluster_0: 13.032, file_cluster_17: 13.061
- **Magnitude:** 645.86 | **LOC:** 642 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.1612%), Tech Debt (18.2925%)
**Top Internal Functions/Classes:**
  * `macro_integer_values` (Impact: 52.2)
  * `consume_integer` (Impact: 40.3)
  * `collect_macro_body_identifiers` (Impact: 35.3)
  * `parse_relational_expression` (Impact: 30.9)
  * `parse_multiplicative_expression` (Impact: 29.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 149`, `args: 50`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 155`, `orphaned_logic: 6`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 71`, `doc: 5`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::parsing::c::preprocess::gpu_pipeline::MacroDef, rustc_hash::FxHashMap, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver/src/accounting.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.59 IQR)
- **Top Global Matches:** file_cluster_8: 13.59, file_cluster_0: 13.592, file_cluster_16: 13.605
- **Magnitude:** 631.76 | **LOC:** 1441 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.9191%), Tech Debt (54.992%)
**Top Internal Functions/Classes:**
  * `repair_atomic_sub_usize_fetch_with_order` (Impact: 21.3)
    * *Intent:* /// Subtract `value` from a `usize` counter, repairing underflow to zero and /// returning the obser...
  * `checked_atomic_add_u64_guarded_with_orde` (Impact: 19.1)
    * *Intent:* /// Add `value` to a `u64` counter with overflow checking and a pre-CAS next-value guard. /// /// # ...
  * `checked_atomic_add_usize_guarded_with_or` (Impact: 19.1)
    * *Intent:* /// Add `value` to a `usize` counter with overflow checking and a pre-CAS next-value guard. /// /// ...
  * `rebasing_atomic_next_u64` (Impact: 18.2)
    * *Intent:* /// Allocate the current `u64` atomic sequence value and publish the next value. /// /// When increm...
  * `checked_atomic_sub_u64_with_order` (Impact: 18.1)
    * *Intent:* /// Subtract `value` from a `u64` counter with caller-selected atomic orderings. /// /// # Errors //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 196`, `args: 136`, `func_start: 72`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 149`, `orphaned_logic: 31`
* *Architecture:* `api: 42`, `import: 8`
* *Defense:* `safety: 146`, `doc: 185`, `test: 147`, `sync_locks: 15`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checked_mul_usize_lazy, checked_mul_u64_count, repair_atomic_sub_usize_with_order, checked_sub_u64_lazy, checked_atomic_sub_u64_with_order, checked_atomic_add_usize_guarded_with_order, pinning_increment_u64, checked_atomic_add_usize_with_order...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-runtime/src/megakernel/planner/fusion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.144 IQR)
- **Top Global Matches:** file_cluster_8: 12.144, file_cluster_0: 12.355, file_cluster_7: 12.388
- **Magnitude:** 628.08 | **LOC:** 836 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.1503%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `select_ordered_maximal` (Impact: 199.6)
  * `plan_compact_fusion_into` (Impact: 68.0)
    * *Intent:* /// Build the compact megakernel fusion plan for one work batch. /// /// Returns the selector's 0/1 ...
  * `select_fused_subset_checked_into` (Impact: 19.0)
    * *Intent:* /// Checked selector variant that reports malformed planner input.
  * `select_fused_subset_compact_checked_into` (Impact: 19.0)
    * *Intent:* /// Checked compact selector variant that reports malformed planner input.
  * `select_fused_subset_into` (Impact: 13.1)
    * *Intent:* /// Compute the optimal fusion subset into reusable scratch buffers.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 184`, `args: 56`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 178`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `safety: 26`, `doc: 79`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::MegakernelWorkItem, prologue::shared_prologue_length
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/egraph_kernel_plan.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.764 IQR)
- **Top Global Matches:** file_cluster_0: 12.764, file_cluster_8: 12.796, file_cluster_16: 12.823
- **Magnitude:** 603.3 | **LOC:** 2930 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.9612%), Tech Debt (80.4246%)
**Top Internal Functions/Classes:**
  * `plan_cuda_egraph_signature_buckets_from_` (Impact: 79.7)
    * *Intent:* /// Plan structural-signature candidate buckets from a lightweight /// CUDA-resident signature snaps...
  * `plan_cuda_egraph_kernel_work` (Impact: 33.2)
  * `append_pass_waves` (Impact: 28.0)
  * `cuda_egraph_signature_pair_rows` (Impact: 27.5)
  * `append_signature_pair_waves` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 171`, `args: 51`, `func_start: 32`, `class_start: 29`
* *Risk/State:* `state_mutation: 89`, `dead_code: 1`, `duplicate_logic: 13`, `orphaned_logic: 8`
* *Architecture:* `api: 178`, `import: 15`
* *Defense:* `safety: 63`, `doc: 434`, `test: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_foundation::optimizer::eqsat_gpu::Equivalence, crate::backend::ordering::sort_unstable_by_key_if_needed, egraph_column_snapshot_spans, ptx::
    cuda_egraph_canonical_rewrite_kernel_ptx, vyre_driver::LaunchPlan, CudaStorageReserveFailure, sort_unstable_if_needed, crate::numeric::CUDA_NUMERIC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/host_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.365 IQR)
- **Top Global Matches:** file_cluster_8: 12.365, file_cluster_13: 12.425, file_cluster_0: 12.613
- **Magnitude:** 601.14 | **LOC:** 862 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.4974%), Tech Debt (54.6223%)
**Top Internal Functions/Classes:**
  * `dispatch_borrowed_async_with_ptx_concret` (Impact: 283.9)
  * `dispatch_borrowed_async` (Impact: 29.2)
    * *Intent:* /// Dispatch a vyre Program asynchronously on this CUDA device with borrowed inputs.
  * `dispatch_prepared_borrowed_timed_with_pt` (Impact: 23.0)
  * `dispatch` (Impact: 19.5)
    * *Intent:* /// Dispatch a vyre Program on this CUDA device.
  * `dispatch_borrowed_timed` (Impact: 13.2)
    * *Intent:* /// Dispatch with backend-owned wall and CUDA event timing.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 165`, `args: 38`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 91`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 9`, `import: 25`
* *Defense:* `safety: 94`, `doc: 6`, `test: 6`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::launch_params::launch_param_byte_len, vyre_driver::binding::Binding, std::ffi::c_void, super::host_transfer_capacities, BindingRole, DispatchConfig, super::plan::CudaDispatchPlan, reserved_vec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `vyre-foundation/tests/__split/wire_adversarial_chunk1.rs` (RUST) | Magnitude: 183.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 96, args: 59, state_mutation: 47
- `vyre-frontend-c/src/pipeline/token_materialize.rs` (RUST) | Magnitude: 174.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 69, state_mutation: 43, branch: 36
- `vyre-foundation/src/serial/wire/framing/put_u8.rs` (RUST) | Magnitude: 4.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, api: 2, structural_boundaries: 1, args: 1
- `vyre-frontend-c/src/pipeline/buffers/program_outputs.rs` (RUST) | Magnitude: 125.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 54, state_mutation: 50, args: 23
- `vyre-primitives/src/math/mori_zwanzig.rs` (RUST) | Magnitude: 107.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 55, doc: 55, test: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/check_bench_budgets.sh` (SHELL) | Magnitude: 11.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, branch: 46, state_mutation: 36, io: 21
- `scripts/check_no_default_feature_megacrate.sh` (SHELL) | Magnitude: 4.18 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 17, structural_boundaries: 10, indent_spaces: 10
- `scripts/check_readme_claims.sh` (SHELL) | Magnitude: 10.77 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 52, branch: 46, io: 44, indent_spaces: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/check_wire_version_migration.sh` (SHELL) | Magnitude: 4.16 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 21, io: 20, indent_spaces: 17, state_mutation: 15
- `scripts/rebuild_status.sh` (SHELL) | Magnitude: 5.51 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 29, io: 25, structural_boundaries: 22, reflection_metaprogramming: 17
- `scripts/install_wire_precommit_hook.sh` (SHELL) | Magnitude: 3.0 | Delta: **0.312 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 13, reflection_metaprogramming: 13, state_mutation: 12, safety: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `vyre-driver-reference/tests/support/mod.rs` (RUST) | Magnitude: 10.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 3, func_start: 3
- `vyre-self-substrate/src/graph/exploded/mod.rs` (RUST) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 18, doc: 16, structural_boundaries: 11, decorators: 7
- `vyre-driver-spirv/src/lib.rs` (RUST) | Magnitude: 73.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 170, doc: 38, args: 27, func_start: 25
- `vyre-reference/src/execution/call.rs` (RUST) | Magnitude: 109.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 38, branch: 25, state_mutation: 24
- `vyre-lower/src/rewrites/sub_combine/mod.rs` (RUST) | Magnitude: 23.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, doc: 20, structural_boundaries: 16, test: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `vyre-libs/src/scan/regex_dfa.rs` (RUST) | Magnitude: 56.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, doc: 97, structural_boundaries: 17, test: 17
- `scripts/check_no_under_reserve.py` (PYTHON) | Magnitude: 34.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, branch: 12, structural_boundaries: 11, state_mutation: 6
- `vyre-driver-wgpu/src/engine/graph.rs` (RUST) | Magnitude: 42.18 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, doc: 24, structural_boundaries: 19, api: 12
- `vyre-self-substrate/src/graph/dominator_frontier/mod.rs` (RUST) | Magnitude: 8.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 10, decorators: 6
- `xtask/src/quick_cache/quick_mutation.rs` (RUST) | Magnitude: 20.32 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, api: 5, encapsulation: 5, generics: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `vyre-foundation/tests/analyze_skip_audit.rs` (RUST) | Magnitude: 62.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, doc: 34, structural_boundaries: 31, branch: 17
- `vyre-self-substrate/src/optimizer/pipeline_resident.rs` (RUST) | Magnitude: 126.06 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 241, structural_boundaries: 51, state_mutation: 38, doc: 36
- `vyre-bench/src/probes/nvml.rs` (RUST) | Magnitude: 131.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 52, state_mutation: 38, branch: 30
- `vyre-lower/src/rewrites/cmp_self_false/mod.rs` (RUST) | Magnitude: 103.28 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 76, state_mutation: 45, doc: 29
- `vyre-primitives/benches/wire_throughput.rs` (RUST) | Magnitude: 57.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 24, structural_boundaries: 21, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/check_unsafe_justifications.sh` (SHELL) | Magnitude: 7.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 42, indent_spaces: 33, branch: 31, state_mutation: 27
- `scripts/wait-crates-index.sh` (SHELL) | Magnitude: 5.75 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 29, indent_spaces: 20, state_mutation: 18, io: 13
- `vyre-runtime/tests/socket_ingest.rs` (RUST) | Magnitude: 45.86 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 29, state_mutation: 12, concurrency: 12
- `scripts/check_repo_split_readiness.sh` (SHELL) | Magnitude: 17.42 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 77, indent_spaces: 72, branch: 71, io: 26
- `scripts/publish-release.sh` (SHELL) | Magnitude: 7.6 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, branch: 32, state_mutation: 24, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vyre-reference/src/dual.rs` (RUST) | Magnitude: 21.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 20, dead_code: 4, pointers: 3, structural_boundaries: 2
- `vyre-libs/src/visual/byte_helpers.rs` (RUST) | Magnitude: 3.28 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 8, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `vyre-foundation/src/optimizer/passes/cleanup/branch_coalesce.rs` (RUST) | Magnitude: 19.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 65, indent_spaces: 45, structural_boundaries: 9, args: 8
- `vyre-foundation/src/serial/wire/framing/put_u32.rs` (RUST) | Magnitude: 4.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 17, api: 2, structural_boundaries: 1, args: 1
- `vyre-libs/src/parsing/core/ast/node.rs` (RUST) | Magnitude: 36.42 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 26, api: 21, immutability_locks: 21, encapsulation: 21
- `vyre-foundation/src/serial.rs` (RUST) | Magnitude: 17.6 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 26, structural_boundaries: 5, api: 5, encapsulation: 5
- `vyre-driver/src/extraction_cost.rs` (RUST) | Magnitude: 24.9 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 77, indent_spaces: 43, test: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `vyre-driver/src/backend/registry/mod.rs` (RUST) | Magnitude: 17.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 5, indent_spaces: 3, api: 2
- `vyre-emit-ptx/src/emitter/control.rs` (RUST) | Magnitude: 202.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 75, branch: 61, safety: 37
- `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/token_provenance/replacement_cache.rs` (RUST) | Magnitude: 61.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 29, args: 18, safety: 18
- `vyre-primitives/src/parsing/ast_ops.rs` (RUST) | Magnitude: 19.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 7, api: 6, immutability_locks: 6, encapsulation: 6
- `vyre-libs/tests/c_preprocess_lru_index_allocation_contract.rs` (RUST) | Magnitude: 19.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, branch: 5, structural_boundaries: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `vyre-libs/src/descriptor.rs` (RUST) | Magnitude: 12.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 33, indent_spaces: 4, test: 2, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `vyre-lints/src/lib.rs` -> Churn: **69.9%** | Cog Load: 13.164% | Debt: 99.9991%
- `vyre-driver-cuda/src/backend/host_dispatch.rs` -> Churn: **60.21%** | Cog Load: 31.4974% | Debt: 54.6223%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `vyre-driver-cuda/src/backend/resident_dispatch.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1929.42
- `vyre-driver-cuda/tests/cuda_graph_dispatch_parity.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1346.59
- `conform/vyre-conform-runner/src/main.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1056.9
- `vyre-primitives/src/graph/exploded.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1013.18
- `vyre-bench/src/cases/release_workloads.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 970.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/lib/cargo_runner.sh` -> **Severity: 517.76** (Blast Radius: 6.472 * Doc Risk: 80.0%)
- `vyre-runtime/src/megakernel/protocol/slot.rs` -> **Severity: 240.019** (Blast Radius: 2.77 * Doc Risk: 86.6494%)
- `vyre-runtime/src/megakernel/protocol/opcode.rs` -> **Severity: 83.9** (Blast Radius: 0.902 * Doc Risk: 93.0151%)
- `vyre-bench/src/api/metric.rs` -> **Severity: 76.3** (Blast Radius: 0.763 * Doc Risk: 100.0%)
- `vyre-driver/src/transfer_accounting.rs` -> **Severity: 54.482** (Blast Radius: 3.047 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
