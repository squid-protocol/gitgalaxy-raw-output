# ARCHITECTURAL_BRIEF: vyre
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/vyre` |
| **Timestamp** | `2026-08-03T21:40:32.272051+00:00` |
| **Scan Duration** | `14.77s` |
| **Git Branch** | `main` |
| **Git Commit** | `4d759595a12966433d417fea8fc54558253b834f` |
| **Git Remote** | `https://github.com/santhsecurity/vyre` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3744 malicious artifacts.

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
> **Architectural Drift Z-Score:** `6.062`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2798 | 70.6% |
| file_cluster_13 | 407 | 10.3% |
| file_cluster_0 | 327 | 8.3% |
| file_cluster_16 | 106 | 2.7% |
| file_cluster_7 | 58 | 1.5% |
| file_cluster_4 | 37 | 0.9% |
| file_cluster_17 | 27 | 0.7% |
| file_cluster_12 | 3 | 0.1% |
| file_cluster_6 | 2 | 0.1% |
| file_cluster_11 | 2 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 9.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 29.9 | 31.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 14.9 | 2.4 | 1.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 42.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.2 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 43.6 | 10.4 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
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

- `flush_active_macro_segment_inner` (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_expansion/flush.rs`) -> Impact: **1674.7** | LOC: 574
- `fill_upload_resident_many_repeated_seque` (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **1512.8** | LOC: 475
- `tokenize_preproc_expr_inner` (@ `vyre-frontend-c/src/tu_host/preprocess/expr/tokenize.rs`) -> Impact: **1253.4** | LOC: 250
- `walk` (@ `xtask/src/lego_audit.rs`) -> Impact: **1214.2** | LOC: 903
- `simplify_binop` (@ `vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`) -> Impact: **1213.8** | LOC: 617
  * *Intent:* /// Algebraic identity simplifications for binary operators. /// These rewrites are always valid and don't require literal operands - /// they fire wh...
- `dispatch_resident_async_concrete_with_pt` (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **1185.5** | LOC: 432
- `emit_op` (@ `vyre-emit-ptx/src/emitter.rs`) -> Impact: **1066.5** | LOC: 470
- `run_semantic_requirement_checks` (@ `xtask/src/vyre_weir_release_gate.rs`) -> Impact: **1017.2** | LOC: 1091
- `dispatch_borrowed_async_with_ptx_concret` (@ `vyre-driver-cuda/src/backend/host_dispatch.rs`) -> Impact: **983.0** | LOC: 339
- `build_vast_and_pg` (@ `vyre-frontend-c/src/pipeline/vast_pg.rs`) -> Impact: **964.5** | LOC: 250

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `convergence` (@ `conform/vyre-test-harness/src/lens.rs`) -> **O(2^N) [Recursive]**
- `fixpoint` (@ `conform/vyre-test-harness/src/lens.rs`) -> **O(2^N) [Recursive]**
- `check_body` (@ `vyre-debug/src/dangling.rs`) -> **O(2^N) [Recursive]**
- `clear` (@ `vyre-driver-cuda/src/backend/allocations.rs`) -> **O(2^N) [Recursive]**
- `plan` (@ `vyre-driver-cuda/src/backend/capabilities.rs`) -> **O(2^N) [Recursive]**
- `dispatch_with_device_buffers` (@ `vyre-driver-cuda/src/lib.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Bytes of transient CUDA device memory currently owned by the transient pool. /// /// This includes checked-out dispatch allocations, compiled-pipe...
- `dispatch_with_device_buffers` (@ `vyre-driver-wgpu/src/backend_impl.rs`) -> **O(2^N) [Recursive]**
- `dispatch_borrowed_batch` (@ `vyre-driver-wgpu/src/backend_impl.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Dispatch a batch of borrowed `(Program, inputs, config)` triples.
- `acquire` (@ `vyre-driver-wgpu/src/buffer/pool.rs`) -> **O(2^N) [Recursive]**
- `dispatch_borrowed_batch` (@ `vyre-driver-wgpu/src/engine/multi_gpu.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Dispatch a borrowed batch across selected adapters without cloning /// input buffers into owned work packets. /// /// Each adapter receives one ba...

### Highest Data Gravity (Database Complexity)
- `check_forbidden_dep_[Truncated]` (@ `scripts/check_ownership_boundaries.sh`) -> DB Complexity: **437**
- `require_dir_file_count_[Truncated]` (@ `scripts/check_repo_hygiene.sh`) -> DB Complexity: **192**
- `Anonymous_Block` (@ `scripts/bench_index.sh`) -> DB Complexity: **182**
  * *Intent:* # Process each codebase and inject dynamic HTML cards
- `Anonymous_Block_[Truncated]` (@ `scripts/check_no_string_wgsl.sh`) -> DB Complexity: **162**
- `check_one` (@ `scripts/check_primitive_contract.sh`) -> DB Complexity: **108**
- `Anonymous_Block` (@ `scripts/check_unsafe_justifications.sh`) -> DB Complexity: **105**
  * *Intent:* # Find every `unsafe {` occurrence in production source (not tests, # not docs, not target/).
- `Anonymous_Block_[Truncated]` (@ `scripts/check_no_closed_ir_enums.sh`) -> DB Complexity: **98**
- `Anonymous_Block_[Truncated]` (@ `scripts/check_consistency_contracts.sh`) -> DB Complexity: **97**
  * *Intent:* # We allow 0 op ids because we have successfully purged all legacy string ops # and shrunk the registry back to native IR built-ins.
- `pass` (@ `scripts/check_base_monument.sh`) -> DB Complexity: **96**
- `Anonymous_Block_[Truncated]` (@ `scripts/final-launch.sh`) -> DB Complexity: **91**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `xtask/src` | 56 | 39194.72 | 13.46% | 10.55% |
| `vyre-driver/src` | 58 | 17511.3 | 8.57% | 57.94% |
| `vyre-primitives/src/graph` | 36 | 16448.78 | 6.88% | 41.73% |
| `vyre-driver-cuda/src/backend` | 25 | 14834.68 | 15.3% | 49.82% |
| `vyre-driver-cuda/src` | 33 | 11601.04 | 6.64% | 64.58% |
| `vyre-driver-wgpu/tests` | 166 | 10457.04 | 3.12% | 0.0% |
| `vyre-primitives/src/math` | 43 | 10440.42 | 10.47% | 57.99% |
| `vyre-driver-cuda/tests` | 98 | 10047.39 | 2.7% | 0.0% |
| `vyre-driver-wgpu/tests/__split` | 137 | 9085.36 | 2.64% | 0.0% |
| `vyre-libs/src/parsing/c/preprocess/gpu_pipeline` | 29 | 8851.92 | 16.6% | 41.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `conform/vyre-conform-generate/src/minimizer.rs` -> **100.0%** Exposure
- `vyre-bench/src/cases/c_parser/syntax_corpus.rs` -> **100.0%** Exposure
- `vyre-driver/src/strategy/mod.rs` -> **100.0%** Exposure
- `vyre-emit-naga/src/program/mod_tests.rs` -> **100.0%** Exposure
- `vyre-foundation/src/optimizer/scheduler/tests.rs` -> **100.0%** Exposure
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
- `vyre-lower/src/descriptor.rs` -> **43** Orphaned Functions | **2** Duplicates

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
18. **`vyre-driver-cuda/src/backend/host_dispatch.rs`** -> AI Confidence: **99.31%**
19. **`vyre-driver-cuda/src/backend/resident.rs`** -> AI Confidence: **99.31%**
20. **`vyre-driver-cuda/src/backend/resident_io.rs`** -> AI Confidence: **99.31%**
21. **`vyre-driver-cuda/src/codegen/descriptor_gate.rs`** -> AI Confidence: **99.31%**
22. **`vyre-driver-cuda/src/egraph_device_image.rs`** -> AI Confidence: **99.31%**
23. **`vyre-driver-cuda/src/lib.rs`** -> AI Confidence: **99.31%**
24. **`vyre-driver-cuda/src/pipeline/compiled_dispatch.rs`** -> AI Confidence: **99.31%**
25. **`vyre-driver-cuda/src/pipeline/materialized_cache.rs`** -> AI Confidence: **99.31%**
26. **`vyre-driver-cuda/tests/module_cache_contracts.rs`** -> AI Confidence: **99.31%**
27. **`vyre-driver-wgpu/src/async_dispatch.rs`** -> AI Confidence: **99.31%**
28. **`vyre-driver-wgpu/src/engine/record_and_readback/bind_groups.rs`** -> AI Confidence: **99.31%**
29. **`vyre-driver-wgpu/src/pipeline/compiled_dispatch.rs`** -> AI Confidence: **99.31%**
30. **`vyre-driver-wgpu/src/pipeline/descriptor_metadata.rs`** -> AI Confidence: **99.31%**
31. **`vyre-driver-wgpu/src/pipeline/persistent.rs`** -> AI Confidence: **99.31%**
32. **`vyre-driver-wgpu/src/pipeline/persistent_resources.rs`** -> AI Confidence: **99.31%**
33. **`vyre-driver-wgpu/src/runtime/prerecorded.rs`** -> AI Confidence: **99.31%**
34. **`vyre-driver-wgpu/tests/__split/op_pairwise_chunk1.rs`** -> AI Confidence: **99.31%**
35. **`vyre-driver-wgpu/tests/c_preprocess_gpu_if_expression.rs`** -> AI Confidence: **99.31%**
36. **`vyre-driver-wgpu/tests/cat_a_conform.rs`** -> AI Confidence: **99.31%**
37. **`vyre-driver-wgpu/tests/naga_loop_region_followup.rs`** -> AI Confidence: **99.31%**
38. **`vyre-driver/src/megakernel_execution.rs`** -> AI Confidence: **99.31%**
39. **`vyre-driver/src/pipeline/compiler.rs`** -> AI Confidence: **99.31%**
40. **`vyre-emit-naga/src/emitter/binding_helpers.rs`** -> AI Confidence: **99.31%**
41. **`vyre-emit-naga/src/emitter/binop.rs`** -> AI Confidence: **99.31%**
42. **`vyre-emit-naga/src/emitter/op_lookup.rs`** -> AI Confidence: **99.31%**
43. **`vyre-emit-naga/tests/adversarial_emit_program_matrix.rs`** -> AI Confidence: **99.31%**
44. **`vyre-emit-ptx/src/emitter.rs`** -> AI Confidence: **99.31%**
45. **`vyre-emit-ptx/src/emitter/body.rs`** -> AI Confidence: **99.31%**
46. **`vyre-emit-ptx/src/emitter/mma.rs`** -> AI Confidence: **99.31%**
47. **`vyre-emit-ptx/src/emitter/vector.rs`** -> AI Confidence: **99.31%**
48. **`vyre-emit-ptx/src/patterns/vec_memory_fusion.rs`** -> AI Confidence: **99.31%**
49. **`vyre-emit-ptx/tests/cross_emitter_parity.rs`** -> AI Confidence: **99.31%**
50. **`vyre-foundation/src/ir_inner/model/node_kind.rs`** -> AI Confidence: **99.31%**
51. **`vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`** -> AI Confidence: **99.31%**
52. **`vyre-foundation/src/optimizer/passes/algebraic/strength_reduce/mod.rs`** -> AI Confidence: **99.31%**
53. **`vyre-foundation/src/optimizer/passes/fusion_cse/fusion_tests.rs`** -> AI Confidence: **99.31%**
54. **`vyre-foundation/src/optimizer/passes/loops/loop_lower_bound_normalize.rs`** -> AI Confidence: **99.31%**
55. **`vyre-foundation/src/optimizer/passes/loops/loop_unroll.rs`** -> AI Confidence: **99.31%**
56. **`vyre-foundation/src/optimizer/passes/memory/store_to_load_forward.rs`** -> AI Confidence: **99.31%**
57. **`vyre-foundation/src/optimizer/scheduler/run.rs`** -> AI Confidence: **99.31%**
58. **`vyre-foundation/src/serial/wire/decode/impl_reader.rs`** -> AI Confidence: **99.31%**
59. **`vyre-foundation/src/serial/wire/encode/put_expr.rs`** -> AI Confidence: **99.31%**
60. **`vyre-foundation/src/serial/wire/tags/data_type_tag.rs`** -> AI Confidence: **99.31%**
61. **`vyre-foundation/src/transform/compiler/dominator_tree.rs`** -> AI Confidence: **99.31%**
62. **`vyre-foundation/src/transform/inline/expand/impl_calleeexpander/composition.rs`** -> AI Confidence: **99.31%**
63. **`vyre-foundation/src/validate/typecheck.rs`** -> AI Confidence: **99.31%**
64. **`vyre-foundation/src/vast/validate.rs`** -> AI Confidence: **99.31%**
65. **`vyre-foundation/tests/autodiff_transform_contracts.rs`** -> AI Confidence: **99.31%**
66. **`vyre-foundation/tests/extern_registry_adversarial.rs`** -> AI Confidence: **99.31%**
67. **`vyre-frontend-c/src/megakernel_workspace/workspace.rs`** -> AI Confidence: **99.31%**
68. **`vyre-frontend-c/src/pipeline/semantic_fast_path.rs`** -> AI Confidence: **99.31%**
69. **`vyre-harness/src/lib.rs`** -> AI Confidence: **99.31%**
70. **`vyre-libs/src/math/algebra.rs`** -> AI Confidence: **99.31%**
71. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/cache/payload_codec.rs`** -> AI Confidence: **99.31%**
72. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_table.rs`** -> AI Confidence: **99.31%**
73. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/segments.rs`** -> AI Confidence: **99.31%**
74. **`vyre-libs/src/parsing/c/preprocess/synthesis.rs`** -> AI Confidence: **99.31%**
75. **`vyre-libs/src/parsing/c/sema/registry/reference.rs`** -> AI Confidence: **99.31%**
76. **`vyre-libs/src/primitive_catalog.rs`** -> AI Confidence: **99.31%**
77. **`vyre-libs/src/rule/ast.rs`** -> AI Confidence: **99.31%**
78. **`vyre-libs/tests/gpu_if_expression_roundtrip.rs`** -> AI Confidence: **99.31%**
79. **`vyre-libs/tests/op_boundaries.rs`** -> AI Confidence: **99.31%**
80. **`vyre-libs/tests/sweep_text_utf8_oracle_matrix.rs`** -> AI Confidence: **99.31%**
81. **`vyre-lints/src/gpu_skip_guards.rs`** -> AI Confidence: **99.31%**
82. **`vyre-lints/src/main.rs`** -> AI Confidence: **99.31%**
83. **`vyre-lints/src/module_forks.rs`** -> AI Confidence: **99.31%**
84. **`vyre-lower/examples/optimize.rs`** -> AI Confidence: **99.31%**
85. **`vyre-lower/src/rewrites/branch_collapse/mod.rs`** -> AI Confidence: **99.31%**
86. **`vyre-lower/tests/egraph_pipeline_integration.rs`** -> AI Confidence: **99.31%**
87. **`vyre-primitives/examples/wire_harness_smoke.rs`** -> AI Confidence: **99.31%**
88. **`vyre-primitives/src/graph/vast_tree_walk.rs`** -> AI Confidence: **99.31%**
89. **`vyre-primitives/src/text/line_index.rs`** -> AI Confidence: **99.31%**
90. **`vyre-primitives/src/text/utf8_validate.rs`** -> AI Confidence: **99.31%**
91. **`vyre-reference/src/execution/expr.rs`** -> AI Confidence: **99.31%**
92. **`vyre-reference/src/execution/hashmap/node_step.rs`** -> AI Confidence: **99.31%**
93. **`vyre-reference/src/execution/typed_ops/mod.rs`** -> AI Confidence: **99.31%**
94. **`vyre-reference/src/workgroup.rs`** -> AI Confidence: **99.31%**
95. **`vyre-runtime/src/megakernel/io/complete.rs`** -> AI Confidence: **99.31%**
96. **`vyre-runtime/src/megakernel/io/poll.rs`** -> AI Confidence: **99.31%**
97. **`vyre-runtime/src/megakernel/protocol/codec.rs`** -> AI Confidence: **99.31%**
98. **`vyre-runtime/src/uring/io_loop.rs`** -> AI Confidence: **99.31%**
99. **`vyre-self-substrate/src/graph/csr_frontier_queue_batch_resident/dispatch.rs`** -> AI Confidence: **99.31%**
100. **`xtask/src/bin/vyre_new_op/run.rs`** -> AI Confidence: **99.31%**
101. **`xtask/src/c_parser_bench.rs`** -> AI Confidence: **99.31%**
102. **`xtask/src/conformance_matrix.rs`** -> AI Confidence: **99.31%**
103. **`xtask/src/heuristic_audit.rs`** -> AI Confidence: **99.31%**
104. **`xtask/src/hygiene_matrix.rs`** -> AI Confidence: **99.31%**
105. **`xtask/src/lego_audit.rs`** -> AI Confidence: **99.31%**
106. **`xtask/src/metadata_matrix.rs`** -> AI Confidence: **99.31%**
107. **`xtask/src/op_matrix.rs`** -> AI Confidence: **99.31%**
108. **`xtask/src/release_completion_audit.rs`** -> AI Confidence: **99.31%**
109. **`xtask/src/source_similar.rs`** -> AI Confidence: **99.31%**
110. **`xtask/src/test_matrix.rs`** -> AI Confidence: **99.31%**
111. **`xtask/src/vyre_weir_release_gate.rs`** -> AI Confidence: **99.31%**
112. **`vyre-aot/examples/vyre_aot_release_surface.rs`** -> AI Confidence: **99.29%**
113. **`vyre-debug/examples/vyre_debug_release_surface.rs`** -> AI Confidence: **99.29%**
114. **`vyre-driver-reference/examples/vyre_driver_reference_release_surface.rs`** -> AI Confidence: **99.29%**
115. **`vyre-driver-wgpu/src/descriptor_mapping.rs`** -> AI Confidence: **99.29%**
116. **`vyre-driver/examples/vyre_driver_release_surface.rs`** -> AI Confidence: **99.29%**
117. **`vyre-driver/src/bindless_policy.rs`** -> AI Confidence: **99.29%**
118. **`vyre-emit-naga/examples/vyre_emit_naga_release_surface.rs`** -> AI Confidence: **99.29%**
119. **`vyre-emit-ptx/examples/vyre_emit_ptx_release_surface.rs`** -> AI Confidence: **99.29%**
120. **`vyre-emit-spirv/examples/vyre_emit_spirv_release_surface.rs`** -> AI Confidence: **99.29%**
121. **`vyre-foundation/examples/vyre_foundation_release_surface.rs`** -> AI Confidence: **99.29%**
122. **`vyre-foundation/src/execution_plan/fusion/divergence.rs`** -> AI Confidence: **99.29%**
123. **`vyre-foundation/src/optimizer/passes/algebraic/const_fold/tests/helpers.rs`** -> AI Confidence: **99.29%**
124. **`vyre-foundation/src/optimizer/passes/fusion_cse/cse/expr_has_effect.rs`** -> AI Confidence: **99.29%**
125. **`vyre-frontend-c/src/pipeline/vast_pg/fusion.rs`** -> AI Confidence: **99.29%**
126. **`vyre-frontend-c/src/tu_host/preprocess/ident.rs`** -> AI Confidence: **99.29%**
127. **`vyre-harness/examples/vyre_harness_release_surface.rs`** -> AI Confidence: **99.29%**
128. **`vyre-intrinsics/examples/vyre_intrinsics_release_surface.rs`** -> AI Confidence: **99.29%**
129. **`vyre-libs/src/buffer_names.rs`** -> AI Confidence: **99.29%**
130. **`vyre-libs/src/parsing/c/parse/vast_kinds.rs`** -> AI Confidence: **99.29%**
131. **`vyre-libs/src/parsing/c/source_bytes.rs`** -> AI Confidence: **99.29%**
132. **`vyre-libs/src/security/catalog.rs`** -> AI Confidence: **99.29%**
133. **`vyre-lints/examples/vyre_lints_release_surface.rs`** -> AI Confidence: **99.29%**
134. **`vyre-macros/examples/vyre_macros_release_surface.rs`** -> AI Confidence: **99.29%**
135. **`vyre-primitives/examples/vyre_primitives_release_surface.rs`** -> AI Confidence: **99.29%**
136. **`vyre-reference/examples/vyre_reference_release_surface.rs`** -> AI Confidence: **99.29%**
137. **`vyre-reference/src/dual_impls/bitwise/and/mod.rs`** -> AI Confidence: **99.29%**
138. **`vyre-reference/src/dual_impls/bitwise/or/mod.rs`** -> AI Confidence: **99.29%**
139. **`vyre-runtime/examples/vyre_runtime_release_surface.rs`** -> AI Confidence: **99.29%**
140. **`vyre-self-substrate/examples/vyre_self_substrate_release_surface.rs`** -> AI Confidence: **99.29%**
141. **`vyre-self-substrate/src/optimizer/dead_branch.rs`** -> AI Confidence: **99.29%**
142. **`xtask/src/bin/vyre_new_op/allowed_archetypes.rs`** -> AI Confidence: **99.29%**
143. **`xtask/src/bin/vyre_new_op/generate_readme.rs`** -> AI Confidence: **99.29%**
144. **`xtask/src/quick/eval_xor.rs`** -> AI Confidence: **99.29%**
145. **`xtask/src/quick_cache/eval_and.rs`** -> AI Confidence: **99.29%**
146. **`scripts/bench_index.sh`** -> AI Confidence: **99.29%**
147. **`scripts/check_architectural_invariants.sh`** -> AI Confidence: **99.29%**
148. **`scripts/check_base_monument.sh`** -> AI Confidence: **99.29%**
149. **`scripts/check_crate_metadata_normalized.sh`** -> AI Confidence: **99.29%**
150. **`scripts/check_dialect_coverage.sh`** -> AI Confidence: **99.29%**
151. **`scripts/check_lib_rs_headers.sh`** -> AI Confidence: **99.29%**
152. **`scripts/check_no_closed_ir_enums.sh`** -> AI Confidence: **99.29%**
153. **`scripts/check_parity_testing_not_leaked.sh`** -> AI Confidence: **99.29%**
154. **`scripts/check_publish_gate.sh`** -> AI Confidence: **99.29%**
155. **`scripts/check_release_signoff.sh`** -> AI Confidence: **99.29%**
156. **`scripts/check_required_ci_jobs.sh`** -> AI Confidence: **99.29%**
157. **`scripts/check_roadmap_status_split.sh`** -> AI Confidence: **99.29%**
158. **`scripts/check_substrate_layout.sh`** -> AI Confidence: **99.29%**
159. **`scripts/check_trait_freeze.sh`** -> AI Confidence: **99.29%**
160. **`scripts/docs.sh`** -> AI Confidence: **99.29%**
161. **`scripts/laws/check_layout.sh`** -> AI Confidence: **99.29%**
162. **`scripts/laws/check_readmes.sh`** -> AI Confidence: **99.29%**
163. **`scripts/prove-release-shards.sh`** -> AI Confidence: **99.29%**
164. **`scripts/publish-dryrun.sh`** -> AI Confidence: **99.29%**
165. **`scripts/wait-crates-index.sh`** -> AI Confidence: **99.29%**
166. **`vyre-harness/src/fp_contract.rs`** -> AI Confidence: **99.25%**
167. **`vyre-self-substrate/src/optimizer/licm.rs`** -> AI Confidence: **99.25%**
168. **`conform/vyre-conform-enforce/tests/op_matrix_truth.rs`** -> AI Confidence: **99.24%**
169. **`conform/vyre-conform-runner/src/main.rs`** -> AI Confidence: **99.24%**
170. **`vyre-aot/src/bundle.rs`** -> AI Confidence: **99.24%**
171. **`vyre-aot/src/compile.rs`** -> AI Confidence: **99.24%**
172. **`vyre-aot/tests/generated_artifact_manifest_matrix.rs`** -> AI Confidence: **99.24%**
173. **`vyre-bench/src/api/resident.rs`** -> AI Confidence: **99.24%**
174. **`vyre-bench/src/cases/c_parser/support.rs`** -> AI Confidence: **99.24%**
175. **`vyre-bench/src/cases/nvme_gpu_ingest.rs`** -> AI Confidence: **99.24%**
176. **`vyre-bench/src/cases/release_workloads.rs`** -> AI Confidence: **99.24%**
177. **`vyre-core/tests/wire_malformed_adversarial.rs`** -> AI Confidence: **99.24%**
178. **`vyre-driver-cuda/src/backend/dispatch.rs`** -> AI Confidence: **99.24%**
179. **`vyre-driver-cuda/src/backend/resident_dispatch.rs`** -> AI Confidence: **99.24%**
180. **`vyre-driver-cuda/src/optimizer.rs`** -> AI Confidence: **99.24%**
181. **`vyre-driver-cuda/src/resident_graph_session.rs`** -> AI Confidence: **99.24%**
182. **`vyre-driver-cuda/src/stream.rs`** -> AI Confidence: **99.24%**
183. **`vyre-driver-cuda/tests/self_optimizer_pattern_match_extended.rs`** -> AI Confidence: **99.24%**
184. **`vyre-driver-reference/src/lib.rs`** -> AI Confidence: **99.24%**
185. **`vyre-driver-wgpu/src/backend_impl.rs`** -> AI Confidence: **99.24%**
186. **`vyre-driver-wgpu/src/bin/vyre.rs`** -> AI Confidence: **99.24%**
187. **`vyre-driver-wgpu/src/engine/record_and_readback.rs`** -> AI Confidence: **99.24%**
188. **`vyre-driver-wgpu/src/engine/record_and_readback/staging.rs`** -> AI Confidence: **99.24%**
189. **`vyre-driver-wgpu/src/engine/record_and_readback/submit.rs`** -> AI Confidence: **99.24%**
190. **`vyre-driver-wgpu/src/engine/streaming/async_copy.rs`** -> AI Confidence: **99.24%**
191. **`vyre-driver-wgpu/src/megakernel.rs`** -> AI Confidence: **99.24%**
192. **`vyre-driver-wgpu/src/megakernel/dispatcher.rs`** -> AI Confidence: **99.24%**
193. **`vyre-driver-wgpu/src/pipeline/compound.rs`** -> AI Confidence: **99.24%**
194. **`vyre-driver-wgpu/src/pipeline/disk_cache.rs`** -> AI Confidence: **99.24%**
195. **`vyre-driver-wgpu/src/runtime/cache/pipeline.rs`** -> AI Confidence: **99.24%**
196. **`vyre-driver-wgpu/src/runtime/readback_ring.rs`** -> AI Confidence: **99.24%**
197. **`vyre-driver-wgpu/src/runtime/shader.rs`** -> AI Confidence: **99.24%**
198. **`vyre-driver-wgpu/tests/__split/c_ast_statement_construct_gaps_e2e_chunk1.rs`** -> AI Confidence: **99.24%**
199. **`vyre-driver-wgpu/tests/binding_layout_drift.rs`** -> AI Confidence: **99.24%**
200. **`vyre-driver-wgpu/tests/cat_a_gpu_differential.rs`** -> AI Confidence: **99.24%**
201. **`vyre-driver-wgpu/tests/pipeline_cache_persistence.rs`** -> AI Confidence: **99.24%**
202. **`vyre-driver/src/backend/registry/acquire.rs`** -> AI Confidence: **99.24%**
203. **`vyre-driver/src/backend/vyre_backend.rs`** -> AI Confidence: **99.24%**
204. **`vyre-driver/src/device_signature.rs`** -> AI Confidence: **99.24%**
205. **`vyre-driver/src/launch.rs`** -> AI Confidence: **99.24%**
206. **`vyre-driver/src/resident_transfer_fusion.rs`** -> AI Confidence: **99.24%**
207. **`vyre-driver/src/validation.rs`** -> AI Confidence: **99.24%**
208. **`vyre-driver/tests/sweep_numeric_oracle_matrix.rs`** -> AI Confidence: **99.24%**
209. **`vyre-emit-naga/src/emitter/op_dispatch.rs`** -> AI Confidence: **99.24%**
210. **`vyre-emit-naga/src/patterns/vec_pack/analysis.rs`** -> AI Confidence: **99.24%**
211. **`vyre-emit-ptx/src/index_facts.rs`** -> AI Confidence: **99.24%**
212. **`vyre-emit-spirv/tests/generated_emit_descriptor_matrix.rs`** -> AI Confidence: **99.24%**
213. **`vyre-foundation/src/dispatch/extension.rs`** -> AI Confidence: **99.24%**
214. **`vyre-foundation/src/lower/subgroup_lowering.rs`** -> AI Confidence: **99.24%**
215. **`vyre-foundation/src/optimizer/passes/algebraic/canonicalize_engine.rs`** -> AI Confidence: **99.24%**
216. **`vyre-foundation/src/optimizer/passes/cleanup/region_fusion_hint.rs`** -> AI Confidence: **99.24%**
217. **`vyre-foundation/src/optimizer/passes/cleanup/rematerialize_cheap_let.rs`** -> AI Confidence: **99.24%**
218. **`vyre-foundation/src/optimizer/passes/loops/loop_licm.rs`** -> AI Confidence: **99.24%**
219. **`vyre-foundation/src/optimizer/passes/loops/loop_var_range_fold.rs`** -> AI Confidence: **99.24%**
220. **`vyre-foundation/src/optimizer/passes/memory/dead_store_elim.rs`** -> AI Confidence: **99.24%**
221. **`vyre-foundation/src/serial/wire/decode/from_wire.rs`** -> AI Confidence: **99.24%**
222. **`vyre-foundation/src/serial/wire/encode/to_wire.rs`** -> AI Confidence: **99.24%**
223. **`vyre-foundation/src/transform/inline/impl_inlinectx.rs`** -> AI Confidence: **99.24%**
224. **`vyre-frontend-c/src/api/lex_index.rs`** -> AI Confidence: **99.24%**
225. **`vyre-frontend-c/src/api/object_decode/abi.rs`** -> AI Confidence: **99.24%**
226. **`vyre-frontend-c/src/api/resident_syntax.rs`** -> AI Confidence: **99.24%**
227. **`vyre-frontend-c/src/pipeline/buffers/abi.rs`** -> AI Confidence: **99.24%**
228. **`vyre-frontend-c/src/pipeline/sema.rs`** -> AI Confidence: **99.24%**
229. **`vyre-frontend-c/tests/megakernel_workspace_contracts.rs`** -> AI Confidence: **99.24%**
230. **`vyre-frontend-c/tests/preprocess_token_spelling_parity.rs`** -> AI Confidence: **99.24%**
231. **`vyre-libs/src/compiler/regalloc.rs`** -> AI Confidence: **99.24%**
232. **`vyre-libs/src/math/conv/im2col.rs`** -> AI Confidence: **99.24%**
233. **`vyre-libs/src/nn/linear/inner/tiled.rs`** -> AI Confidence: **99.24%**
234. **`vyre-libs/src/parsing/c/parse/gnu_builtin_catalog.rs`** -> AI Confidence: **99.24%**
235. **`vyre-libs/src/parsing/c/parse/inline_asm.rs`** -> AI Confidence: **99.24%**
236. **`vyre-libs/src/parsing/c/preprocess/effects.rs`** -> AI Confidence: **99.24%**
237. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/directives.rs`** -> AI Confidence: **99.24%**
238. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/conditional_directives.rs`** -> AI Confidence: **99.24%**
239. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/directive_walk.rs`** -> AI Confidence: **99.24%**
240. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/file_inputs.rs`** -> AI Confidence: **99.24%**
241. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/scan.rs`** -> AI Confidence: **99.24%**
242. **`vyre-libs/src/parsing/c/preprocess/mod.rs`** -> AI Confidence: **99.24%**
243. **`vyre-libs/src/scan/regex_dfa.rs`** -> AI Confidence: **99.24%**
244. **`vyre-libs/src/substrate_catalog.rs`** -> AI Confidence: **99.24%**
245. **`vyre-libs/src/visual/blur/mod.rs`** -> AI Confidence: **99.24%**
246. **`vyre-libs/tests/buffer_name_cross_family.rs`** -> AI Confidence: **99.24%**
247. **`vyre-libs/tests/surface_contracts.rs`** -> AI Confidence: **99.24%**
248. **`vyre-lower/src/lower.rs`** -> AI Confidence: **99.24%**
249. **`vyre-lower/src/rewrites/bank_conflict_pad/mod.rs`** -> AI Confidence: **99.24%**
250. **`vyre-lower/src/rewrites/body_index.rs`** -> AI Confidence: **99.24%**
251. **`vyre-lower/src/rewrites/descriptor_const_fold/mod.rs`** -> AI Confidence: **99.24%**
252. **`vyre-lower/src/rewrites/identity_elim/mod.rs`** -> AI Confidence: **99.24%**
253. **`vyre-lower/src/verify/mod.rs`** -> AI Confidence: **99.24%**
254. **`vyre-macros/src/algebraic_laws.rs`** -> AI Confidence: **99.24%**
255. **`vyre-macros/src/define_op.rs`** -> AI Confidence: **99.24%**
256. **`vyre-primitives/src/graph/exploded.rs`** -> AI Confidence: **99.24%**
257. **`vyre-primitives/src/graph/matroid.rs`** -> AI Confidence: **99.24%**
258. **`vyre-primitives/src/graph/tensor_flow_forward.rs`** -> AI Confidence: **99.24%**
259. **`vyre-primitives/src/graph/toposort.rs`** -> AI Confidence: **99.24%**
260. **`vyre-primitives/src/math/dot_partial.rs`** -> AI Confidence: **99.24%**
261. **`vyre-primitives/tests/sweep_hash_crc_oracle_matrix.rs`** -> AI Confidence: **99.24%**
262. **`vyre-reference/src/execution/call.rs`** -> AI Confidence: **99.24%**
263. **`vyre-reference/src/execution/hashmap/mod.rs`** -> AI Confidence: **99.24%**
264. **`vyre-reference/src/execution/hashmap/state.rs`** -> AI Confidence: **99.24%**
265. **`vyre-reference/src/execution/node.rs`** -> AI Confidence: **99.24%**
266. **`vyre-reference/tests/gap_transcendentals_parity.rs`** -> AI Confidence: **99.24%**
267. **`vyre-runtime/src/megakernel/execution.rs`** -> AI Confidence: **99.24%**
268. **`vyre-runtime/src/megakernel/execution/persistent_handles.rs`** -> AI Confidence: **99.24%**
269. **`vyre-runtime/src/megakernel/io/helpers.rs`** -> AI Confidence: **99.24%**
270. **`vyre-runtime/src/megakernel/planner/barriers.rs`** -> AI Confidence: **99.24%**
271. **`vyre-runtime/src/megakernel/telemetry.rs`** -> AI Confidence: **99.24%**
272. **`vyre-runtime/src/uring/driver.rs`** -> AI Confidence: **99.24%**
273. **`vyre-self-substrate/src/graph/csr_frontier_queue_resident/query.rs`** -> AI Confidence: **99.24%**
274. **`vyre-self-substrate/src/optimizer/pipeline_resident.rs`** -> AI Confidence: **99.24%**
275. **`xtask/src/dep_drift.rs`** -> AI Confidence: **99.24%**
276. **`xtask/src/lint_shape_tests.rs`** -> AI Confidence: **99.24%**
277. **`xtask/src/package_readiness.rs`** -> AI Confidence: **99.24%**
278. **`xtask/src/recursion_gate.rs`** -> AI Confidence: **99.24%**
279. **`xtask/src/release_benchmarks.rs`** -> AI Confidence: **99.24%**
280. **`conform/vyre-conform-runner/tests/lens_parity.rs`** -> AI Confidence: **99.23%**
281. **`vyre-bench/src/evolve/server.rs`** -> AI Confidence: **99.23%**
282. **`vyre-debug/src/dangling.rs`** -> AI Confidence: **99.23%**
283. **`vyre-driver-cuda/src/device.rs`** -> AI Confidence: **99.23%**
284. **`vyre-driver-cuda/src/pipeline/static_params.rs`** -> AI Confidence: **99.23%**
285. **`vyre-driver-wgpu/src/pipeline/binding.rs`** -> AI Confidence: **99.23%**
286. **`vyre-driver-wgpu/tests/gap_transcendentals_parity.rs`** -> AI Confidence: **99.23%**
287. **`vyre-driver/src/benchmark_pass_selection.rs`** -> AI Confidence: **99.23%**
288. **`vyre-driver/src/megakernel_barrier.rs`** -> AI Confidence: **99.23%**
289. **`vyre-driver/src/program_walks/outputs.rs`** -> AI Confidence: **99.23%**
290. **`vyre-emit-ptx/src/emitter/atomic.rs`** -> AI Confidence: **99.23%**
291. **`vyre-emit-ptx/src/emitter/control.rs`** -> AI Confidence: **99.23%**
292. **`vyre-foundation/src/optimizer/passes/fusion_cse/cse/impl_csectx.rs`** -> AI Confidence: **99.23%**
293. **`vyre-foundation/src/transform/autodiff/grad/expr.rs`** -> AI Confidence: **99.23%**
294. **`vyre-frontend-c/src/pipeline/buffers/lexer_diagnostic_report.rs`** -> AI Confidence: **99.23%**
295. **`vyre-libs/src/math/atomic/atomic_lru_update.rs`** -> AI Confidence: **99.23%**
296. **`vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/ifdef_truth_batch.rs`** -> AI Confidence: **99.23%**
297. **`vyre-lints/src/consumer_coupling.rs`** -> AI Confidence: **99.23%**
298. **`vyre-lints/src/raw_ir_in_libs.rs`** -> AI Confidence: **99.23%**
299. **`vyre-primitives/src/graph/dominator_tree.rs`** -> AI Confidence: **99.23%**
300. **`vyre-primitives/src/nn/quest_paging_passes.rs`** -> AI Confidence: **99.23%**
301. **`vyre-runtime/src/megakernel/protocol_api/publish.rs`** -> AI Confidence: **99.23%**
302. **`vyre-self-substrate/src/graph/dispatch_bridge/resident.rs`** -> AI Confidence: **99.23%**
303. **`xtask/src/feature_matrix.rs`** -> AI Confidence: **99.23%**
304. **`xtask/src/measurement_gate.rs`** -> AI Confidence: **99.23%**
305. **`xtask/src/quick_cache/eval_or.rs`** -> AI Confidence: **99.23%**
306. **`xtask/src/release_conformance.rs`** -> AI Confidence: **99.23%**
307. **`scripts/laws/run_all.sh`** -> AI Confidence: **99.23%**
308. **`vyre-harness/src/region.rs`** -> AI Confidence: **99.22%**
309. **`scripts/lib/cargo_runner.sh`** -> AI Confidence: **99.22%**
310. **`conform/vyre-conform-enforce/tests/__split/composition_discipline_chunk1.rs`** -> AI Confidence: **99.2%**
311. **`conform/vyre-conform-runner/src/bundle_cert.rs`** -> AI Confidence: **99.18%**
312. **`vyre-bench/src/cases/adaptive_routing.rs`** -> AI Confidence: **99.18%**
313. **`vyre-bench/src/cases/adversarial.rs`** -> AI Confidence: **99.18%**
314. **`vyre-bench/src/cases/alias_aware_optimizations.rs`** -> AI Confidence: **99.18%**
315. **`vyre-bench/src/cases/bigint.rs`** -> AI Confidence: **99.18%**
316. **`vyre-bench/src/cases/c_parser/single_syntax.rs`** -> AI Confidence: **99.18%**
317. **`vyre-bench/src/cases/crypto.rs`** -> AI Confidence: **99.18%**
318. **`vyre-bench/src/cases/elementwise.rs`** -> AI Confidence: **99.18%**
319. **`vyre-bench/src/cases/hashtable.rs`** -> AI Confidence: **99.18%**
320. **`vyre-bench/src/cases/quantized_linear.rs`** -> AI Confidence: **99.18%**
321. **`vyre-bench/src/cases/regex_bt.rs`** -> AI Confidence: **99.18%**
322. **`vyre-bench/src/report/flame.rs`** -> AI Confidence: **99.18%**
323. **`vyre-bench/src/report/kernel_time_table.rs`** -> AI Confidence: **99.18%**
324. **`vyre-bench/tests/cross_emitter_property.rs`** -> AI Confidence: **99.18%**
325. **`vyre-driver-cuda/src/backend/telemetry.rs`** -> AI Confidence: **99.18%**
326. **`vyre-driver-cuda/src/megakernel_barrier_planner.rs`** -> AI Confidence: **99.18%**
327. **`vyre-driver-cuda/src/token_fact_frontier_execution.rs`** -> AI Confidence: **99.18%**
328. **`vyre-driver-cuda/tests/capability_contracts.rs`** -> AI Confidence: **99.18%**
329. **`vyre-driver-cuda/tests/common/mod.rs`** -> AI Confidence: **99.18%**
330. **`vyre-driver-cuda/tests/generated_atomic_cuda_reference_matrix.rs`** -> AI Confidence: **99.18%**
331. **`vyre-driver-cuda/tests/generated_i32_cuda_reference_matrix.rs`** -> AI Confidence: **99.18%**
332. **`vyre-driver-cuda/tests/i3_i4_integration.rs`** -> AI Confidence: **99.18%**
333. **`vyre-driver-cuda/tests/multi_block_prefix_scan_gpu_parity.rs`** -> AI Confidence: **99.18%**
334. **`vyre-driver-cuda/tests/resident_dispatch_contracts.rs`** -> AI Confidence: **99.18%**
335. **`vyre-driver-cuda/tests/self_optimizer_licm_e2e.rs`** -> AI Confidence: **99.18%**
336. **`vyre-driver-cuda/tests/vectorized_memory_live_cuda.rs`** -> AI Confidence: **99.18%**
337. **`vyre-driver-reference/tests/generated_boundary_matrix.rs`** -> AI Confidence: **99.18%**
338. **`vyre-driver-spirv/examples/vulkan_probe.rs`** -> AI Confidence: **99.18%**
339. **`vyre-driver-wgpu/src/engine/persistent.rs`** -> AI Confidence: **99.18%**
340. **`vyre-driver-wgpu/src/engine/streaming.rs`** -> AI Confidence: **99.18%**
341. **`vyre-driver-wgpu/src/megakernel/dispatch_plan.rs`** -> AI Confidence: **99.18%**
342. **`vyre-driver-wgpu/src/runtime/router.rs`** -> AI Confidence: **99.18%**
343. **`vyre-driver-wgpu/src/spirv_backend.rs`** -> AI Confidence: **99.18%**
344. **`vyre-driver-wgpu/src/thread_pool.rs`** -> AI Confidence: **99.18%**
345. **`vyre-driver-wgpu/tests/__split/c_ast_property_typedef_annotation_contracts_chunk1.rs`** -> AI Confidence: **99.18%**
346. **`vyre-driver-wgpu/tests/c_ast_declaration_container_nodes/gpu.rs`** -> AI Confidence: **99.18%**
347. **`vyre-driver-wgpu/tests/c_ast_gpu_parity_support/mod.rs`** -> AI Confidence: **99.18%**
348. **`vyre-driver-wgpu/tests/c_ast_preprocessor_token_stream_e2e.rs`** -> AI Confidence: **99.18%**
349. **`vyre-driver-wgpu/tests/c_ast_property_graph_consistency_contracts.rs`** -> AI Confidence: **99.18%**
350. **`vyre-driver-wgpu/tests/c_ast_property_span_monotonicity_contracts.rs`** -> AI Confidence: **99.18%**
351. **`vyre-driver-wgpu/tests/c_ast_semantic_edge_expectations_gnu_and_control_flow.rs`** -> AI Confidence: **99.18%**
352. **`vyre-driver-wgpu/tests/c_ast_string_init_e2e.rs`** -> AI Confidence: **99.18%**
353. **`vyre-driver-wgpu/tests/c_lower_ast_to_pg_nodes.rs`** -> AI Confidence: **99.18%**
354. **`vyre-driver-wgpu/tests/live_capability_honesty.rs`** -> AI Confidence: **99.18%**
355. **`vyre-driver-wgpu/tests/naga_deeper_regressions.rs`** -> AI Confidence: **99.18%**
356. **`vyre-driver-wgpu/tests/naga_findings_followup.rs`** -> AI Confidence: **99.18%**
357. **`vyre-driver-wgpu/tests/resident_timed_outputs.rs`** -> AI Confidence: **99.18%**
358. **`vyre-driver-wgpu/tests/self_optimizer_const_fold_e2e.rs`** -> AI Confidence: **99.18%**
359. **`vyre-driver-wgpu/tests/self_optimizer_pattern_match_e2e.rs`** -> AI Confidence: **99.18%**
360. **`vyre-driver-wgpu/tests/self_optimizer_scaling_bench.rs`** -> AI Confidence: **99.18%**
361. **`vyre-driver-wgpu/tests/trap_propagation.rs`** -> AI Confidence: **99.18%**
362. **`vyre-driver/src/backend.rs`** -> AI Confidence: **99.18%**
363. **`vyre-driver/src/backend/typed_dispatch.rs`** -> AI Confidence: **99.18%**
364. **`vyre-driver/src/device_extraction.rs`** -> AI Confidence: **99.18%**
365. **`vyre-driver/src/dispatch_policy.rs`** -> AI Confidence: **99.18%**
366. **`vyre-driver/src/graph_capture.rs`** -> AI Confidence: **99.18%**
367. **`vyre-driver/src/pipeline/hashing.rs`** -> AI Confidence: **99.18%**
368. **`vyre-driver/src/registry/registry.rs`** -> AI Confidence: **99.18%**
369. **`vyre-driver/src/shadow.rs`** -> AI Confidence: **99.18%**
370. **`vyre-driver/src/specialization.rs`** -> AI Confidence: **99.18%**
371. **`vyre-driver/src/speculate.rs`** -> AI Confidence: **99.18%**
372. **`vyre-driver/tests/backend_capability_negotiation.rs`** -> AI Confidence: **99.18%**
373. **`vyre-driver/tests/backend_validation_defaults.rs`** -> AI Confidence: **99.18%**
374. **`vyre-driver/tests/driver_lifecycle_e2e.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `vyre-libs/tests/gpu_pipeline_driver_roundtrip.rs` -> **99.9956%** Exposure
- `vyre-frontend-c/src/tu_host/preprocess/expr/tests.rs` -> **0.4523%** Exposure
- `vyre-frontend-c/src/pipeline/lexer_plan/source_scan.rs` -> **0.0013%** Exposure
- `vyre-driver-cuda/tests/__split/ptx_codegen_smoke_part1.rs` -> **0.0001%** Exposure
### Exploit Generation Surface
- `scripts/check_self_consumer_coverage.py` -> **100.0%** Exposure
- `tools/divergence-gate.py` -> **100.0%** Exposure
- `vyre-libs/tests/fixtures/go/worker_pool.go` -> **100.0%** Exposure
- `scripts/check_no_raw_unwrap.py` -> **34.3428%** Exposure
- `conform/vyre-conform-enforce/tests/__split/composition_discipline_chunk2.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `conform/vyre-conform-enforce/tests/op_matrix_truth.rs` -> **100.0%** Exposure
- `conform/vyre-conform-runner/tests/release_gate_contracts.rs` -> **100.0%** Exposure
- `vyre-bench/tests/release_matrix_contracts.rs` -> **100.0%** Exposure
- `vyre-frontend-c/src/tu_host/include_loader.rs` -> **100.0%** Exposure
- `vyre-frontend-c/src/tu_host/tests.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `vyre-foundation/src/ir_inner/model/expr.rs` -> **0.0902%** Exposure
- `vyre-primitives/src/dnnf/compile.rs` -> **0.0628%** Exposure
- `vyre-reference/tests/oracle_program_edges.rs` -> **0.0019%** Exposure
- `vyre-foundation/src/ir_inner/model/node/impl_node.rs` -> **0.0017%** Exposure
- `vyre-foundation/src/optimizer/scheduler/tests.rs` -> **0.0014%** Exposure
### Hardcoded Payload Artifacts
- `vyre-libs/src/scan/test_fixtures.rs` -> **100.0%** Exposure
- `vyre-libs/tests/cache_key_collision.rs` -> **99.9995%** Exposure
### Algorithmic DoS Exposure
- `benches/competition/scripts/check_corpora.py` -> **100.0%** Exposure
- `scripts/check_no_raw_unwrap.py` -> **100.0%** Exposure
- `scripts/check_no_under_reserve.py` -> **100.0%** Exposure
- `scripts/check_self_consumer_coverage.py` -> **100.0%** Exposure
- `tools/divergence-gate.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28172` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/check_no_string_wgsl.sh` (SHELL) -> Cumulative Risk: **924.9**
- **Archetype:** `file_cluster_4` (Distance: 12.883 IQR)
- **Magnitude:** 12.79 | **LOC:** 130 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 79.4), `__global_context__` (Impact: 4.1)

### 2. `scripts/check_tests_can_fail.sh` (SHELL) -> Cumulative Risk: **924.08**
- **Archetype:** `file_cluster_4` (Distance: 14.122 IQR)
- **Magnitude:** 7.69 | **LOC:** 45 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 18.6), `Anonymous_Block` (Impact: 7.3), `Anonymous_Block` (Impact: 5.2)

### 3. `vyre-bench/src/cases/cpu_baselines.rs` (RUST) -> Cumulative Risk: **917.28**
- **Archetype:** `file_cluster_8` (Distance: 11.042 IQR)
- **Magnitude:** 340.4 | **LOC:** 282 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `histogram_u32_256_bytes` (Impact: 43.6), `baseline_pool` (Impact: 37.9), `elementwise_add_f32_bytes_into` (Impact: 37.0)

### 4. `vyre-driver/src/persistent.rs` (RUST) -> Cumulative Risk: **914.55**
- **Archetype:** `file_cluster_0` (Distance: 12.873 IQR)
- **Magnitude:** 610.56 | **LOC:** 616 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9129%)
- **Heaviest Functions:** `multi_producer_single_consumer_no_item_l` (Impact: 87.4), `claim` (Impact: 62.6), `enqueue` (Impact: 50.2)

### 5. `scripts/check_public_api.sh` (SHELL) -> Cumulative Risk: **911.23**
- **Archetype:** `file_cluster_4` (Distance: 13.46 IQR)
- **Magnitude:** 5.58 | **LOC:** 45 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 11.4), `Anonymous_Block_[Truncated]` (Impact: 7.9), `__global_context__` (Impact: 2.9)

### 6. `scripts/check_test_coverage_per_crate.sh` (SHELL) -> Cumulative Risk: **910.48**
- **Archetype:** `file_cluster_4` (Distance: 14.125 IQR)
- **Magnitude:** 13.46 | **LOC:** 91 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Stability (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 54.0), `__global_context__` (Impact: 5.4)

### 7. `scripts/check_public_api_snapshot.sh` (SHELL) -> Cumulative Risk: **899.15**
- **Archetype:** `file_cluster_4` (Distance: 12.629 IQR)
- **Magnitude:** 22.15 | **LOC:** 81 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `extract_api` (Impact: 137.2), `Anonymous_Block` (Impact: 9.2), `Anonymous_Block` (Impact: 7.8)

### 8. `vyre-emit-ptx/src/emitter/results.rs` (RUST) -> Cumulative Risk: **898.82**
- **Archetype:** `file_cluster_13` (Distance: 11.801 IQR)
- **Magnitude:** 110.28 | **LOC:** 82 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `bind_consecutive_results` (Impact: 40.2), `alloc_literal` (Impact: 18.4), `finish_with_return` (Impact: 15.7)

### 9. `scripts/check_tier_b_rule_contracts.sh` (SHELL) -> Cumulative Risk: **896.81**
- **Archetype:** `file_cluster_4` (Distance: 12.236 IQR)
- **Magnitude:** 8.92 | **LOC:** 83 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 33.0), `Anonymous_Block_[Truncated]` (Impact: 17.6), `Anonymous_Block` (Impact: 10.8)

### 10. `scripts/check_examples_public_facade.sh` (SHELL) -> Cumulative Risk: **893.04**
- **Archetype:** `file_cluster_4` (Distance: 13.206 IQR)
- **Magnitude:** 10.09 | **LOC:** 80 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 68.0), `__global_context__` (Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `xtask/src/release_completion_audit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.25 IQR)
- **Top Global Matches:** file_cluster_8: 11.25, file_cluster_7: 11.915, file_cluster_17: 12.058
- **Magnitude:** 6762.02 | **LOC:** 6411 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.998%), Tech Debt (8.2198%)
**Top Internal Functions/Classes:**
  * `inspect_json_evidence` (Impact: 366.6 | O(N^4) | DB: 3)
  * `inspect_pass_family_benchmark_manifest_s` (Impact: 337.1 | O(N^6) | DB: 1)
  * `inspect_backend_suite_semantics` (Impact: 334.0 | O(N^6) | DB: 1)
  * `run` (Impact: 318.9 | O(N^6) | DB: 9)
  * `inspect_backend_matrix_semantics` (Impact: 270.2 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 902`, `structural_boundaries: 497`, `args: 293`, `func_start: 87`, `class_start: 6`
* *Risk/State:* `state_mutation: 179`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 11`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 319`, `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::path::Path, std::fs, serde::Deserialize, std::collections::BTreeSet, PathBuf, Serialize, Read, std::io::self
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xtask/src/vyre_weir_release_gate.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.133 IQR)
- **Top Global Matches:** file_cluster_8: 11.133, file_cluster_7: 11.799, file_cluster_17: 12.0
- **Magnitude:** 5038.3 | **LOC:** 6940 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (8.8717%), Tech Debt (9.644%)
**Top Internal Functions/Classes:**
  * `run_semantic_requirement_checks` (Impact: 1017.2 | O(N^6) | DB: 1)
  * `check_backend_suite_report` (Impact: 534.1 | O(N^6) | DB: 3)
  * `check_workload_matrix_artifact_coverage` (Impact: 338.5 | O(N^6) | DB: 7)
  * `run` (Impact: 247.9 | O(N^6) | DB: 6)
  * `check_single_benchmark_report` (Impact: 226.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 893`, `structural_boundaries: 554`, `args: 278`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 128`, `planned_debt: 7`, `fragile_debt: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 364`, `doc: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::path::Path, std::fs, serde::Deserialize, std::collections::BTreeSet, PathBuf, Read, std::io::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/resident_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.113 IQR)
- **Top Global Matches:** file_cluster_8: 13.113, file_cluster_13: 13.288, file_cluster_0: 13.333
- **Magnitude:** 5021.12 | **LOC:** 2201 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.6496%), Tech Debt (24.4855%)
**Top Internal Functions/Classes:**
  * `fill_upload_resident_many_repeated_seque` (Impact: 1512.8 | O(N^6) | DB: 48)
  * `dispatch_resident_async_concrete_with_pt` (Impact: 1185.5 | O(N^6) | DB: 32)
  * `dispatch_resident_batch_async_concrete_w` (Impact: 723.8 | O(N^6) | DB: 38)
  * `dispatch_resident_via_borrowed_into` (Impact: 198.3 | O(N^6) | DB: 8)
  * `dispatch_resident_timed` (Impact: 88.4 | O(N^4))
    * *Intent:* /// Dispatch with CUDA-resident buffers and return ordered output readbacks.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 488`, `args: 71`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 506`, `dead_code: 2`, `duplicate_logic: 4`, `orphaned_logic: 19`
* *Architecture:* `api: 20`, `concurrency: 2`, `import: 26`
* *Defense:* `safety: 175`, `doc: 4`, `test: 35`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_driver::BackendError, ResidentUploadCopy, CudaResidentDispatch, super::ordering::sort_unstable_by_key_if_needed, super::prepare_resident_sequence_fills, super::launch_params::launch_param_byte_len, super::borrow_resident_sequence_output_slots, ResidentReadbackCopy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `conform/vyre-conform-runner/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.53 IQR)
- **Top Global Matches:** file_cluster_8: 12.53, file_cluster_17: 12.742, file_cluster_13: 12.835
- **Magnitude:** 2581.6 | **LOC:** 1952 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (20.6241%), Tech Debt (7.9768%)
**Top Internal Functions/Classes:**
  * `merge_certificates` (Impact: 360.3 | O(N^6) | DB: 17)
  * `prove` (Impact: 278.2 | O(2^N) | DB: 9)
  * `read_and_verify_shard` (Impact: 208.9 | O(N^5) | DB: 5)
  * `compare_backend_against_reference` (Impact: 131.0 | O(N^6) | DB: 3)
  * `backend_dispatch_plan` (Impact: 107.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 401`, `args: 141`, `func_start: 47`, `class_start: 15`
* *Risk/State:* `state_mutation: 200`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `concurrency: 28`, `import: 22`
* *Defense:* `safety: 193`, `doc: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Verifier, vyre_driver_wgpu, vyre_conform_runner::dispatch_grid, vyre_driver_reference, ed25519_dalek::Signature, Signer, vyre_driver::
    backend::backend_dispatches, rand_core::RngCore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/release_benchmarks.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.321 IQR)
- **Top Global Matches:** file_cluster_8: 12.321, file_cluster_17: 12.623, file_cluster_0: 12.767
- **Magnitude:** 2265.96 | **LOC:** 2236 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (13.8406%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 408.1 | O(2^N) | DB: 6)
  * `inspect_backend_suite_artifact` (Impact: 371.6 | O(N^6) | DB: 39)
  * `inspect_optimization_benchmark_artifact` (Impact: 210.5 | O(N^5) | DB: 31)
  * `write_cpu_100x_proof` (Impact: 169.2 | O(N^6) | DB: 30)
  * `parse_args` (Impact: 109.4 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 362`, `args: 144`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 202`
* *Architecture:* `io: 10`, `api: 1`, `import: 6`
* *Defense:* `safety: 324`, `doc: 5`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::process::Command, std::io::Read, std::path::Path, std::fs, serde::Deserialize, serde_json::json, PathBuf, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/c_parser_bench.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.976 IQR)
- **Top Global Matches:** file_cluster_8: 11.976, file_cluster_0: 12.286, file_cluster_17: 12.43
- **Magnitude:** 1943.88 | **LOC:** 1933 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (19.8739%), Tech Debt (20.405%)
**Top Internal Functions/Classes:**
  * `run_inner` (Impact: 318.9 | O(N^5) | DB: 19)
  * `parse_args` (Impact: 283.1 | O(N^6) | DB: 13)
  * `is_release_evidence_valid` (Impact: 209.1 | O(N^2))
  * `inspect_vyrecob2_sections` (Impact: 142.8 | O(N^4) | DB: 6)
  * `run_vyre_parser_file_range` (Impact: 102.9 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 278`, `args: 85`, `func_start: 54`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 140`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `safety: 180`, `doc: 1`, `test: 33`, `sync_locks: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` walkdir::WalkDir, vyre_driver_wgpu, std::time::Instant, VYRECOB2_MAGIC, vyre_frontend_c::api::
    parse_source, repro_command, std::path::PathBuf, Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-primitives/src/graph/exploded.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.752 IQR)
- **Top Global Matches:** file_cluster_8: 11.752, file_cluster_7: 11.956, file_cluster_0: 11.992
- **Magnitude:** 1933.58 | **LOC:** 2317 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (9.6862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_build_cpu_reference_into` (Impact: 549.3 | O(N^4) | DB: 9)
  * `validate_ifds_csr_inputs` (Impact: 140.6 | O(N^4) | DB: 1)
  * `ifds_program_cache_key_from_program` (Impact: 123.8 | O(N^3))
  * `build_ifds_csr_program` (Impact: 99.5 | O(N^6) | DB: 6)
  * `validate_ifds_csr_readback` (Impact: 76.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 283`, `args: 105`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 180`
* *Architecture:* `api: 143`, `import: 9`
* *Defense:* `safety: 65`, `doc: 254`, `test: 116`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Node, Program, vyre_foundation::ir::BinOp, vyre_foundation::transform::visit::walk_nodes, std::sync::Arc, super::*, vyre_foundation::ir::model::expr::Ident, vyre_foundation::transform::visit::walk_exprs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-driver-cuda/src/backend/resident_io.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.757 IQR)
- **Top Global Matches:** file_cluster_8: 12.757, file_cluster_13: 12.918, file_cluster_0: 13.049
- **Magnitude:** 1831.36 | **LOC:** 1060 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (22.1466%), Tech Debt (34.085%)
**Top Internal Functions/Classes:**
  * `download_resident_ranges_into` (Impact: 246.1 | O(N^6) | DB: 9)
    * *Intent:* /// Download selected byte ranges from resident buffers into caller-owned /// output slots with one ...
  * `download_resident_readback_batches_many_` (Impact: 237.4 | O(N^6) | DB: 12)
    * *Intent:* /// Download selected byte ranges from several resident-output batches into /// caller-owned output ...
  * `download_resident_readbacks_many_into` (Impact: 175.9 | O(N^6) | DB: 8)
    * *Intent:* /// Download selected byte ranges from several CUDA-resident buffers into /// caller-owned output sl...
  * `upload_resident_async_at` (Impact: 113.7 | O(N^6) | DB: 1)
    * *Intent:* /// Async H2D copy from a pinned host pointer into a CUDA-resident buffer. /// /// # Safety /// /// ...
  * `download_resident_fused_copy_batches_man` (Impact: 112.8 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 193`, `args: 63`, `func_start: 40`
* *Risk/State:* `state_mutation: 211`, `orphaned_logic: 18`
* *Architecture:* `api: 22`, `concurrency: 10`, `import: 13`
* *Defense:* `safety: 77`, `doc: 44`, `test: 13`, `sync_locks: 4`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_driver::BackendError, ResidentUploadCopy, ResidentReadbackCopy, reserved_vec, super::dispatch::CudaBackend, OutputBuffers, super::allocations::HostTransferAllocations, cuda_resident_total_budget_bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_expansion/flush.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.043 IQR)
- **Top Global Matches:** file_cluster_8: 10.043, file_cluster_7: 10.766, file_cluster_17: 10.846
- **Magnitude:** 1743.82 | **LOC:** 608 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (15.5769%), Tech Debt (8.8377%)
**Top Internal Functions/Classes:**
  * `flush_active_macro_segment_inner` (Impact: 1674.7 | O(2^N) | DB: 17)
  * `flush_active_macro_segment` (Impact: 7.1 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 90`, `args: 11`, `func_start: 2`
* *Risk/State:* `state_mutation: 48`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-bench/src/cases/release_workloads.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.23 IQR)
- **Top Global Matches:** file_cluster_8: 11.23, file_cluster_16: 11.791, file_cluster_7: 11.796
- **Magnitude:** 1689.2 | **LOC:** 2595 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (10.8003%), Tech Debt (73.5866%)
**Top Internal Functions/Classes:**
  * `callgraph_witness_digest` (Impact: 95.4 | O(N^5) | DB: 2)
  * `release_benchmark_csr_forward_baseline` (Impact: 87.5 | O(N^4) | DB: 1)
  * `run` (Impact: 69.8 | O(N^4) | DB: 7)
  * `run` (Impact: 68.7 | O(2^N) | DB: 4)
  * `run` (Impact: 47.0 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 254`, `args: 103`, `func_start: 110`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 201`, `duplicate_logic: 32`, `orphaned_logic: 6`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 69`, `doc: 21`, `test: 4`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Program, DeterminismClass, PerformanceContract, BufferDecl, vyre::ir::BufferAccess, BenchMetadata, PreparedCase, MetricPoint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/host_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.372 IQR)
- **Top Global Matches:** file_cluster_8: 12.372, file_cluster_13: 12.431, file_cluster_0: 12.619
- **Magnitude:** 1686.34 | **LOC:** 862 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (32.0003%), Tech Debt (54.6223%)
**Top Internal Functions/Classes:**
  * `dispatch_borrowed_async_with_ptx_concret` (Impact: 983.0 | O(N^6) | DB: 23)
  * `dispatch_borrowed_async` (Impact: 164.0 | O(2^N))
    * *Intent:* /// Dispatch a vyre Program asynchronously on this CUDA device with borrowed inputs.
  * `dispatch` (Impact: 105.2 | O(2^N) | DB: 2)
    * *Intent:* /// Dispatch a vyre Program on this CUDA device.
  * `dispatch_prepared_borrowed_timed_with_pt` (Impact: 54.5 | O(N^4))
  * `dispatch_borrowed_timed` (Impact: 37.7 | O(N^5))
    * *Intent:* /// Dispatch with backend-owned wall and CUDA event timing.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 165`, `args: 38`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 91`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 9`, `import: 25`
* *Defense:* `safety: 94`, `doc: 6`, `test: 6`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_driver::BackendError, super::launch_params::launch_param_byte_len, reserved_vec, super::host_transfer_capacities, crate::backend::CudaDispatchPlan, crate::CUDA_BACKEND_ID, std::ffi::c_void, super::dispatch::CudaBackend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-wgpu/src/megakernel.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.223 IQR)
- **Top Global Matches:** file_cluster_8: 12.223, file_cluster_0: 12.35, file_cluster_13: 12.483
- **Magnitude:** 1675.38 | **LOC:** 1498 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (18.5438%), Tech Debt (56.1996%)
**Top Internal Functions/Classes:**
  * `dispatch_megakernel_with_io_queue_ref` (Impact: 513.6 | O(N^6) | DB: 18)
  * `megakernel_report_telemetry` (Impact: 129.7 | O(N^4) | DB: 2)
  * `ensure_resident_megakernel_buffers` (Impact: 123.5 | O(N^6) | DB: 2)
  * `strict_done_ring_slots_from_outputs` (Impact: 49.8 | O(N^3) | DB: 2)
  * `ensure_empty_io_queue_bytes` (Impact: 40.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 240`, `args: 106`, `func_start: 60`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 117`, `duplicate_logic: 15`
* *Architecture:* `api: 30`, `import: 15`
* *Defense:* `safety: 129`, `doc: 15`, `test: 67`, `sync_locks: 15`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::time::Instant, crate::numeric::usize_to_u64, vyre_runtime::megakernel::protocol, FILE_METADATA_WORDS, BatchFile, CrossArmRedundancy, FileBatch, MegakernelConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/src/tu_host/preprocess/expr/tokenize.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.421 IQR)
- **Top Global Matches:** file_cluster_8: 10.421, file_cluster_13: 10.889, file_cluster_17: 11.038
- **Magnitude:** 1574.6 | **LOC:** 413 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (25.8021%), Tech Debt (9.5084%)
**Top Internal Functions/Classes:**
  * `tokenize_preproc_expr_inner` (Impact: 1253.4 | O(2^N) | DB: 6)
  * `substitute_expr_macro_params` (Impact: 178.6 | O(N^6) | DB: 2)
  * `parse_expr_macro_args` (Impact: 74.9 | O(N^6) | DB: 4)
  * `is_plain_identifier` (Impact: 9.3 | O(N^2))
  * `is_preprocessor_probe_builtin` (Impact: 4.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 56`, `args: 18`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 36`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-wgpu/src/backend_impl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.017 IQR)
- **Top Global Matches:** file_cluster_8: 12.017, file_cluster_16: 12.368, file_cluster_0: 12.41
- **Magnitude:** 1540.3 | **LOC:** 1354 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (9.4339%), Tech Debt (63.7161%)
**Top Internal Functions/Classes:**
  * `dispatch_with_device_buffers` (Impact: 299.3 | O(2^N) | DB: 3)
  * `dispatch_borrowed_batch` (Impact: 242.6 | O(2^N) | DB: 5)
    * *Intent:* /// Dispatch a batch of borrowed `(Program, inputs, config)` triples.
  * `record_borrowed_batch_job` (Impact: 73.8 | O(N^5))
  * `try_recover` (Impact: 58.8 | O(N^4))
  * `dispatch_borrowed_into` (Impact: 48.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 145`, `args: 101`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 49`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `safety: 162`, `doc: 29`, `test: 13`, `sync_locks: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::
    atomic::AtomicBool, Ordering, crate::staging_reserve::reserve_backend_vec, std::time::Instant, vyre_driver::speculate::SpeculationMode, vyre_foundation::ir::Program, std::hash::BuildHasherDefault, Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/pipeline/compiled_dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.867 IQR)
- **Top Global Matches:** file_cluster_8: 12.867, file_cluster_13: 13.133, file_cluster_17: 13.235
- **Magnitude:** 1506.64 | **LOC:** 861 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (35.8088%), Tech Debt (21.823%)
**Top Internal Functions/Classes:**
  * `dispatch_borrowed_batched_via_cuda_graph` (Impact: 281.6 | O(N^6) | DB: 13)
  * `dispatch_borrowed_into` (Impact: 120.1 | O(N^5) | DB: 3)
  * `dispatch_borrowed_batched_into` (Impact: 120.1 | O(N^5) | DB: 3)
  * `dispatch_persistent_resource_outputs` (Impact: 117.2 | O(N^5) | DB: 4)
  * `materialized_output_batch_cache_partitio` (Impact: 104.6 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 185`, `args: 35`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `state_mutation: 171`, `orphaned_logic: 10`
* *Architecture:* `import: 10`
* *Defense:* `safety: 111`, `doc: 5`, `sync_locks: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::backend::CachedCudaGraph, crate::backend::cuda_graph_replay::CudaGraphReplayStats, MaterializedPipelineOutputCache, BackendError, reserved_vec, OutputBuffers, crate::pipeline::
    cuda_graph_lane_count_for_batch, crate::pipeline::materialized_cache::materialized_input_key...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/segments.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.187 IQR)
- **Top Global Matches:** file_cluster_8: 12.187, file_cluster_13: 12.347, file_cluster_0: 12.468
- **Magnitude:** 1491.82 | **LOC:** 780 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (31.549%), Tech Debt (48.2295%)
**Top Internal Functions/Classes:**
  * `function_argument_prescan_macros` (Impact: 322.2 | O(N^6) | DB: 2)
  * `macro_use_statement_ranges` (Impact: 220.9 | O(N^6) | DB: 6)
  * `refresh` (Impact: 163.0 | O(N^6) | DB: 1)
  * `macro_segment_shard_ranges` (Impact: 133.4 | O(N^5) | DB: 7)
  * `has_live_macro_for_segment_excluding` (Impact: 130.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 166`, `args: 73`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 90`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 9`, `import: 19`
* *Defense:* `safety: 87`, `test: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TOK_RPAREN, super::source_spans::checked_source_range, MacroDef, crate::parsing::c::lex::tokens::
    TOK_IDENTIFIER, super::*, rustc_hash::FxHashMap, super::buffers::checked_gpu_u32, FxHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.236 IQR)
- **Top Global Matches:** file_cluster_8: 12.236, file_cluster_13: 12.665, file_cluster_7: 12.705
- **Magnitude:** 1459.54 | **LOC:** 842 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (20.7262%), Tech Debt (8.7525%)
**Top Internal Functions/Classes:**
  * `simplify_binop` (Impact: 1213.8 | O(N^6))
    * *Intent:* /// Algebraic identity simplifications for binary operators. /// These rewrites are always valid and...
  * `fold_mod_lookbehind` (Impact: 116.8 | O(2^N) | DB: 3)
    * *Intent:* // ─── ROADMAP A35: stronger range fold ───────────────────────────── // Mod(x, N) where x.max < N -...
  * `rewrite_expr_for_mod` (Impact: 44.2 | O(N^6) | DB: 3)
  * `is_float_expr` (Impact: 24.9 | O(2^N))
    * *Intent:* /// Check if an expression is known to produce a float type. /// Used by FMA synthesis to avoid inte...
  * `mul_operands` (Impact: 8.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 97`, `args: 28`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 219`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Node, IdentityReplacement, crate::ir::BinOp, std::sync::Arc, ScalarLiteral, rustc_hash::FxHashMap, crate::optimizer::algebraic_rules::
    binop_identity_replacement, Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/lego_audit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.084 IQR)
- **Top Global Matches:** file_cluster_8: 12.084, file_cluster_7: 12.367, file_cluster_13: 12.382
- **Magnitude:** 1455.08 | **LOC:** 1352 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (11.4774%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk` (Impact: 1214.2 | O(N^6) | DB: 51)
  * `run` (Impact: 74.2 | O(2^N) | DB: 1)
    * *Intent:* //! failing the LEGO pattern. //! 3. **Primitive-coverage** - every Tier 2.5 primitive should have /...
  * `buffer_signature` (Impact: 25.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 149`, `args: 44`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 118`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 4`, `import: 6`
* *Defense:* `safety: 54`, `doc: 87`, `test: 7`, `sync_locks: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Node, Program, BTreeSet, HashMap, std::process, super::*, Read, std::collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/tests/cuda_graph_dispatch_parity.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.706 IQR)
- **Top Global Matches:** file_cluster_8: 9.706, file_cluster_17: 10.023, file_cluster_0: 10.27
- **Magnitude:** 1430.09 | **LOC:** 853 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.8904%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 189`, `args: 17`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 52`
* *Architecture:* `import: 6`
* *Defense:* `safety: 15`, `doc: 15`, `test: 77`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vyre_driver_cuda::CudaBackend, vyre_driver::BackendError, Node, Program, bytes_u32, std::time::Instant, std::sync::Arc, common::bool_bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-runtime/src/megakernel/planner/fusion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.191 IQR)
- **Top Global Matches:** file_cluster_8: 12.191, file_cluster_0: 12.402, file_cluster_7: 12.435
- **Magnitude:** 1428.98 | **LOC:** 836 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (35.7169%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `select_ordered_maximal` (Impact: 669.2 | O(N^6) | DB: 35)
  * `plan_compact_fusion_into` (Impact: 247.2 | O(N^6) | DB: 9)
    * *Intent:* /// Build the compact megakernel fusion plan for one work batch. /// /// Returns the selector's 0/1 ...
  * `fmt` (Impact: 44.1 | O(2^N) | DB: 1)
  * `select_fused_subset_checked_into` (Impact: 36.1 | O(N^3) | DB: 4)
    * *Intent:* /// Checked selector variant that reports malformed planner input.
  * `select_fused_subset_compact_checked_into` (Impact: 36.1 | O(N^3) | DB: 4)
    * *Intent:* /// Checked compact selector variant that reports malformed planner input.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 184`, `args: 74`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 178`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `safety: 26`, `doc: 79`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` prologue::shared_prologue_length, super::MegakernelWorkItem
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_values.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.753 IQR)
- **Top Global Matches:** file_cluster_8: 12.753, file_cluster_0: 13.012, file_cluster_17: 13.041
- **Magnitude:** 1410.16 | **LOC:** 642 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (60.1385%), Tech Debt (18.2925%)
**Top Internal Functions/Classes:**
  * `macro_integer_values` (Impact: 186.2 | O(N^6) | DB: 14)
  * `consume_integer` (Impact: 116.3 | O(N^5) | DB: 2)
  * `parse_multiplicative_expression` (Impact: 85.2 | O(N^5) | DB: 2)
  * `collect_macro_body_identifiers` (Impact: 77.3 | O(N^3) | DB: 2)
  * `parse_relational_expression` (Impact: 75.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 149`, `args: 41`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 155`, `orphaned_logic: 6`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 71`, `doc: 5`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rustc_hash::FxHashMap, crate::parsing::c::preprocess::gpu_pipeline::MacroDef, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.988 IQR)
- **Top Global Matches:** file_cluster_8: 12.988, file_cluster_16: 13.146, file_cluster_7: 13.286
- **Magnitude:** 1390.38 | **LOC:** 1272 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.9595%), Tech Debt (33.2%)
**Top Internal Functions/Classes:**
  * `dispatch_with_device_buffers` (Impact: 281.2 | O(2^N) | DB: 4)
    * *Intent:* /// Bytes of transient CUDA device memory currently owned by the transient pool. /// /// This includ...
  * `dispatch_resident_repeated_sequence_read` (Impact: 87.6 | O(N^5) | DB: 2)
  * `public_cuda_execution_entrypoints_share_` (Impact: 49.2 | O(N^4))
  * `dispatch_resident_sequence_read_ranges_i` (Impact: 45.7 | O(N^5) | DB: 2)
  * `upload_device_buffer` (Impact: 41.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 120`, `args: 100`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `orphaned_logic: 17`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 78`, `doc: 88`, `test: 12`, `sync_locks: 1`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CudaDeviceWorkQueueBackpressurePlan, CudaMegakernelSpeedupGateError, CudaResidentGraphSessionEvidenceError, cuda_egraph_structural_equivalence_kernel_ptx, launch_fusion::
    plan_cuda_launch_fusion, CudaEGraphKernelWorkPlan, megakernel_barrier_planner::
    plan_cuda_frontier_megakernel_execution, plan_cuda_frontier_megakernel_execution_with_scratch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver/src/grid_sync.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.754 IQR)
- **Top Global Matches:** file_cluster_8: 12.754, file_cluster_0: 12.989, file_cluster_16: 12.996
- **Magnitude:** 1390.34 | **LOC:** 1470 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (21.0248%), Tech Debt (97.5148%)
**Top Internal Functions/Classes:**
  * `hoist_grid_sync_barriers` (Impact: 186.6 | O(2^N) | DB: 5)
  * `dispatch_with_grid_sync_split_into` (Impact: 88.7 | O(N^4) | DB: 8)
    * *Intent:* /// [`VyreBackend::supports_grid_sync`]) bypass the split - the /// program is dispatched once. Back...
  * `dispatch_resident_with_grid_sync_split_t` (Impact: 75.6 | O(N^4) | DB: 4)
  * `refresh_readwrite_inputs` (Impact: 69.4 | O(N^4) | DB: 4)
  * `try_split_on_grid_sync` (Impact: 69.3 | O(N^5) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 210`, `args: 49`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 228`, `fragile_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 15`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 86`, `doc: 124`, `test: 66`, `sync_locks: 10`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Program, OutputBuffers, BufferDecl, vyre_foundation::ir::Expr, Ordering, vyre_foundation::ir::Ident, super::*, vyre_foundation::memory_model::MemoryOrdering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/hygiene_matrix.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.708 IQR)
- **Top Global Matches:** file_cluster_8: 11.708, file_cluster_17: 12.1, file_cluster_11: 12.129
- **Magnitude:** 1388.7 | **LOC:** 1196 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (27.1706%), Tech Debt (18.3078%)
**Top Internal Functions/Classes:**
  * `scan_file` (Impact: 227.0 | O(N^5) | DB: 6)
  * `scan_root` (Impact: 87.2 | O(N^4) | DB: 2)
  * `scan_audit_report_locations` (Impact: 86.2 | O(N^4) | DB: 2)
  * `scan_test_file` (Impact: 72.9 | O(N^4) | DB: 2)
  * `scan_release_tooling` (Impact: 68.8 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 187`, `args: 128`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 176`, `planned_debt: 8`, `fragile_debt: 5`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 65`, `doc: 3`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` walkdir::WalkDir, std::path::Path, std::fs, serde::Serialize, PathBuf, Read, std::io::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/source_similar.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.438 IQR)
- **Top Global Matches:** file_cluster_8: 11.438, file_cluster_0: 11.675, file_cluster_17: 11.769
- **Magnitude:** 1385.58 | **LOC:** 1168 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (16.8468%), Tech Debt (21.3116%)
**Top Internal Functions/Classes:**
  * `normalize_tokens` (Impact: 244.2 | O(N^5) | DB: 2)
  * `collect_rust_files_recursive` (Impact: 148.6 | O(2^N) | DB: 2)
  * `parse_args` (Impact: 88.0 | O(N^5) | DB: 7)
  * `source_shape` (Impact: 77.0 | O(N^4) | DB: 4)
  * `candidate_pairs` (Impact: 67.5 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 227`, `args: 116`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 94`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 57`, `doc: 7`, `test: 46`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashSet, std::path::Path, std::fs, std::process, alpha::alpha, delta::delta, super::*, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `vyre-foundation/tests/__split/wire_adversarial_chunk1.rs` (RUST) | Magnitude: 270.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 96, state_mutation: 47, func_start: 38
- `vyre-frontend-c/src/pipeline/token_materialize.rs` (RUST) | Magnitude: 308.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 69, state_mutation: 43, branch: 36
- `vyre-foundation/src/serial/wire/framing/put_u8.rs` (RUST) | Magnitude: 4.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, api: 2, structural_boundaries: 1, args: 1
- `vyre-frontend-c/src/tu_host/include_loader_cache.rs` (RUST) | Magnitude: 592.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 102, args: 61, test: 51
- `vyre-primitives/src/math/mori_zwanzig.rs` (RUST) | Magnitude: 169.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 55, doc: 55, test: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/check_no_default_feature_megacrate.sh` (SHELL) | Magnitude: 4.18 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 17, structural_boundaries: 10, indent_spaces: 10
- `scripts/check_readme_claims.sh` (SHELL) | Magnitude: 14.02 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 52, branch: 46, io: 44, indent_spaces: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/check_wire_version_migration.sh` (SHELL) | Magnitude: 5.86 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 21, io: 20, indent_spaces: 17, state_mutation: 15
- `scripts/rebuild_status.sh` (SHELL) | Magnitude: 5.51 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 29, structural_boundaries: 25, io: 25, reflection_metaprogramming: 17
- `scripts/install_wire_precommit_hook.sh` (SHELL) | Magnitude: 2.39 | Delta: **0.292 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 13, state_mutation: 12, safety: 9, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `vyre-driver-reference/tests/support/mod.rs` (RUST) | Magnitude: 12.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 3, func_start: 3
- `vyre-self-substrate/src/graph/exploded/mod.rs` (RUST) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 18, doc: 16, structural_boundaries: 11, decorators: 7
- `scripts/check_feature_msrv.sh` (SHELL) | Magnitude: 8.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, io: 36, structural_boundaries: 35, branch: 24
- `vyre-driver-spirv/src/lib.rs` (RUST) | Magnitude: 113.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 170, doc: 38, args: 27, func_start: 25
- `vyre-reference/src/execution/call.rs` (RUST) | Magnitude: 213.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 38, branch: 25, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `scripts/check_no_under_reserve.py` (PYTHON) | Magnitude: 124.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, branch: 12, structural_boundaries: 11, state_mutation: 6
- `vyre-foundation/src/serial/envelope.rs` (RUST) | Magnitude: 178.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, doc: 178, structural_boundaries: 41, branch: 23
- `vyre-driver-wgpu/src/engine/graph.rs` (RUST) | Magnitude: 68.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, doc: 24, structural_boundaries: 19, api: 12
- `vyre-self-substrate/src/graph/dominator_frontier/mod.rs` (RUST) | Magnitude: 8.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 10, decorators: 6
- `xtask/src/quick_cache/quick_mutation.rs` (RUST) | Magnitude: 20.32 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, api: 5, encapsulation: 5, generics: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/check_no_hot_path_vec_vec.sh` (SHELL) | Magnitude: 8.97 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 39, io: 36, branch: 33, indent_spaces: 28
- `vyre-foundation/tests/analyze_skip_audit.rs` (RUST) | Magnitude: 125.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, doc: 34, structural_boundaries: 31, branch: 17
- `vyre-self-substrate/src/optimizer/pipeline_resident.rs` (RUST) | Magnitude: 315.06 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 241, structural_boundaries: 51, state_mutation: 38, doc: 36
- `vyre-bench/src/probes/nvml.rs` (RUST) | Magnitude: 201.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 52, state_mutation: 38, branch: 30
- `vyre-lower/src/rewrites/cmp_self_false/mod.rs` (RUST) | Magnitude: 173.58 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 76, state_mutation: 45, doc: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/check_unsafe_justifications.sh` (SHELL) | Magnitude: 7.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 42, indent_spaces: 33, branch: 31, state_mutation: 27
- `scripts/check_repo_split_readiness.sh` (SHELL) | Magnitude: 22.35 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, branch: 71, state_mutation: 53, io: 26
- `scripts/wait-crates-index.sh` (SHELL) | Magnitude: 6.55 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 29, indent_spaces: 20, state_mutation: 18, io: 13
- `vyre-runtime/tests/socket_ingest.rs` (RUST) | Magnitude: 71.86 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 29, state_mutation: 12, concurrency: 12
- `scripts/check_gap_tests_fail_for_reason.sh` (SHELL) | Magnitude: 8.46 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 31, indent_spaces: 20, io: 16, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vyre-reference/src/dual.rs` (RUST) | Magnitude: 21.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 20, dead_code: 4, pointers: 3, structural_boundaries: 2
- `vyre-libs/src/visual/byte_helpers.rs` (RUST) | Magnitude: 3.28 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 8, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `vyre-foundation/src/optimizer/passes/cleanup/branch_coalesce.rs` (RUST) | Magnitude: 25.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 65, indent_spaces: 45, structural_boundaries: 9, args: 8
- `vyre-foundation/src/serial/wire/framing/put_u32.rs` (RUST) | Magnitude: 4.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 17, api: 2, structural_boundaries: 1, args: 1
- `vyre-libs/src/parsing/core/ast/node.rs` (RUST) | Magnitude: 36.42 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 26, api: 21, immutability_locks: 21, encapsulation: 21
- `vyre-foundation/src/serial.rs` (RUST) | Magnitude: 17.6 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 26, structural_boundaries: 5, api: 5, encapsulation: 5
- `vyre-driver/src/extraction_cost.rs` (RUST) | Magnitude: 33.6 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 77, indent_spaces: 43, test: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `vyre-driver/src/backend/registry/mod.rs` (RUST) | Magnitude: 17.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 5, indent_spaces: 3, api: 2
- `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/live_state.rs` (RUST) | Magnitude: 625.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 443, structural_boundaries: 124, state_mutation: 112, branch: 75
- `vyre-emit-ptx/src/emitter/control.rs` (RUST) | Magnitude: 458.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 75, branch: 61, safety: 37
- `vyre-foundation/src/optimizer/passes/loops/loop_lower_bound_normalize.rs` (RUST) | Magnitude: 8.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 74, indent_spaces: 13, sec_high_risk_execution: 9, branch: 2
- `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/token_provenance/replacement_cache.rs` (RUST) | Magnitude: 92.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 29, args: 18, safety: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `vyre-libs/src/descriptor.rs` (RUST) | Magnitude: 12.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 33, indent_spaces: 4, test: 2, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `vyre-lints/src/lib.rs` -> Churn: **69.9%** | Cog Load: 13.164% | Debt: 99.9991%
- `vyre-driver-cuda/src/backend/host_dispatch.rs` -> Churn: **60.21%** | Cog Load: 32.0003% | Debt: 54.6223%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `vyre-driver-cuda/src/backend/resident_dispatch.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 5021.12
- `conform/vyre-conform-runner/src/main.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 2581.6
- `vyre-primitives/src/graph/exploded.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1933.58
- `vyre-driver-cuda/src/backend/resident_io.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1831.36
- `vyre-bench/src/cases/release_workloads.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1689.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/lib/cargo_runner.sh` -> **Severity: 517.76** (Blast Radius: 6.472 * Doc Risk: 80.0%)
- `vyre-driver/src/transfer_accounting.rs` -> **Severity: 287.51** (Blast Radius: 3.047 * Doc Risk: 94.3585%)
- `vyre-runtime/src/megakernel/protocol/slot.rs` -> **Severity: 240.067** (Blast Radius: 2.77 * Doc Risk: 86.6667%)
- `vyre-runtime/src/megakernel/protocol/opcode.rs` -> **Severity: 88.378** (Blast Radius: 0.902 * Doc Risk: 97.98%)
- `vyre-runtime/src/megakernel/protocol.rs` -> **Severity: 80.457** (Blast Radius: 0.971 * Doc Risk: 82.8598%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
