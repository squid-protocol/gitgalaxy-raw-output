# ARCHITECTURAL_BRIEF: wasmtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/wasmtime` |
| **Timestamp** | `2026-08-07T04:08:43.947679+00:00` |
| **Scan Duration** | `10.84s` |
| **Git Branch** | `main` |
| **Git Commit** | `5b5e3573d7de1314c6fcd0d327d4e3640ce58138` |
| **Git Remote** | `https://github.com/bytecodealliance/wasmtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1925 malicious artifacts.

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
| Total Artifacts | 6447 |
| Analyzed Artifacts (Scanned) | 2003 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4444 |
| Total LOC | 392346 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 31.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8549 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3474 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2791 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 35 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1731 | 378456 | 86.4% |
| CPP | 142 | 11228 | 7.1% |
| MARKDOWN | 65 | 0 | 3.2% |
| C | 29 | 2159 | 1.4% |
| PLAINTEXT | 9 | 0 | 0.4% |
| DOCKERFILE | 8 | 58 | 0.4% |
| SHELL | 7 | 126 | 0.3% |
| JAVASCRIPT | 3 | 221 | 0.1% |
| BINARY_THREAT | 2 | 2 | 0.1% |
| PYTHON | 1 | 14 | 0.0% |
| XML | 1 | 0 | 0.0% |
| JSON | 1 | 3 | 0.0% |
| YAML | 1 | 6 | 0.0% |
| CSS | 1 | 40 | 0.0% |
| M4 | 1 | 17 | 0.0% |
| MAKEFILE | 1 | 16 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.937`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 737 | 36.8% |
| file_cluster_13 | 502 | 25.1% |
| file_cluster_0 | 258 | 12.9% |
| file_cluster_16 | 205 | 10.2% |
| file_cluster_4 | 182 | 9.1% |
| file_cluster_7 | 14 | 0.7% |
| file_cluster_17 | 13 | 0.6% |
| file_cluster_6 | 10 | 0.5% |
| file_cluster_11 | 6 | 0.3% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 74 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4444*

**Composition by Extension & Reason:**
- `.wat`: 2222x Excluded (Unsupported Extension: '.wat'), 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.wat)
- `.clif`: 1190x Excluded (Unsupported Extension: '.clif'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wast`: 218x Excluded (Unsupported Extension: '.wast'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Machine-Generated Source Code Signature: 205 LOC), 5x Excluded (Machine-Generated Source Code Signature: 243 LOC)
- `.isle`: 115x Unsupported Format (.isle)
- `.toml`: 102x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.wit`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Unsupported Format (.wit), 11x Excluded (Unsupported Extension: '.wit')
- `no_extension`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.witx`: 23x Excluded (Unsupported Extension: '.witx')
- `.yml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 89 LOC), 1x Excluded (Machine-Generated Source Code Signature: 117 LOC)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1066 LOC)
- `.js`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 20.6 | 10.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 37.8 | 34.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.2 | 23.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.9 | 3.3 | 3.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 42.7 | 27.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.6 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/wasi/src/p2/host/network.rs` (Hits: 42)
- `crates/wasi-http/tests/all/p2.rs` (Hits: 26)
- `src/commands/serve.rs` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wasm.h** (`crates/c-api/include/wasm.h`) — 47 inbound connections
2. **rex.rs** (`cranelift/assembler-x64/src/rex.rs`) — 33 inbound connections
3. **wasmtime.hh** (`crates/c-api/include/wasmtime.hh`) — 31 inbound connections
4. **vex.rs** (`cranelift/assembler-x64/src/vex.rs`) — 26 inbound connections
5. **wasmtime.h** (`crates/c-api/include/wasmtime.h`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **concurrent.rs** (`crates/wasmtime/src/runtime/component/concurrent.rs`) — 114 outbound dependencies
2. **masm.rs** (`winch/codegen/src/isa/aarch64/masm.rs`) — 96 outbound dependencies
3. **masm.rs** (`winch/codegen/src/isa/x64/masm.rs`) — 96 outbound dependencies
4. **futures_and_streams.rs** (`crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`) — 92 outbound dependencies
5. **vm.rs** (`crates/wasmtime/src/runtime/vm.rs`) — 90 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `validate_signature_params` (@ `cranelift/interpreter/src/step.rs`) -> Impact: **811.1** | LOC: 1188
  * *Intent:* /// Ensures that all types in args are the same as expected by the signature
- `parse_instruction` (@ `cranelift/reader/src/parser.rs`) -> Impact: **805.4** | LOC: 1344
- `parse_target_specs` (@ `cranelift/reader/src/parser.rs`) -> Impact: **618.5** | LOC: 1389
- `poll_produce` (@ `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`) -> Impact: **545.1** | LOC: 1510
- `new` (@ `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`) -> Impact: **493.9** | LOC: 1517
- `validate_memory_inbounds` (@ `crates/environ/src/fact/trampoline.rs`) -> Impact: **462.4** | LOC: 1470
- `emit` (@ `cranelift/codegen/src/isa/riscv64/inst/emit.rs`) -> Impact: **445.4** | LOC: 1440
- `calculate_list_byte_len` (@ `crates/environ/src/fact/trampoline.rs`) -> Impact: **413.0** | LOC: 1451
  * *Intent:* // Assert that the untagged code unit length is the same as the
- `parse_u64` (@ `cranelift/codegen/src/ir/immediates.rs`) -> Impact: **390.4** | LOC: 1409
- `setup_guest_profiler` (@ `src/commands/run.rs`) -> Impact: **386.5** | LOC: 546

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/wasmtime/src/runtime/vm` | 31 | 21469.02 | 19.27% | 53.53% |
| `tests/all` | 56 | 21041.18 | 28.69% | 0.0% |
| `tests/all/component_model` | 15 | 8631.4 | 34.78% | 0.0% |
| `crates/test-programs/src/bin` | 264 | 6283.0 | 20.96% | 58.7% |
| `crates/wasmtime/src/runtime` | 31 | 6261.04 | 19.09% | 69.46% |
| `crates/wasmtime/src/runtime/component` | 15 | 4568.36 | 26.12% | 68.02% |
| `crates/wasmtime/src/runtime/component/concurrent` | 6 | 4392.98 | 23.55% | 66.38% |
| `pulley/src` | 11 | 4315.08 | 17.36% | 62.27% |
| `cranelift/codegen/src` | 31 | 4142.7 | 15.66% | 47.27% |
| `crates/cranelift/src` | 10 | 4035.68 | 11.95% | 48.04% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cranelift/assembler-x64/meta/src/dsl/custom.rs` -> **100.0%** Exposure
- `cranelift/assembler-x64/meta/src/instructions/abs.rs` -> **100.0%** Exposure
- `cranelift/assembler-x64/src/imm.rs` -> **100.0%** Exposure
- `cranelift/bforest/src/lib.rs` -> **100.0%** Exposure
- `cranelift/bforest/src/map.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cranelift/assembler-x64/src/api.rs` -> **100.0%** Exposure
- `cranelift/codegen/meta/src/shared/mod.rs` -> **100.0%** Exposure
- `cranelift/codegen/shared/src/constant_hash.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/ir/atomic_rmw_op.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/print_errors.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pulley/src/interp.rs` -> **476** Orphaned Functions | **29** Duplicates
- `cranelift/isle/veri/veri_engine/tests/veri.rs` -> **188** Orphaned Functions | **9** Duplicates
- `winch/codegen/src/isa/x64/asm.rs` -> **158** Orphaned Functions | **24** Duplicates
- `cranelift/codegen/src/isle_prelude.rs` -> **131** Orphaned Functions | **0** Duplicates
- `cranelift/codegen/src/isa/x64/lower/isle.rs` -> **104** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/explorer/src/lib.rs`** -> AI Confidence: **99.48%**
2. **`crates/wast/src/component.rs`** -> AI Confidence: **99.48%**
3. **`cranelift/codegen/src/ir/types.rs`** -> AI Confidence: **99.39%**
4. **`crates/wasi/src/p2/mod.rs`** -> AI Confidence: **99.39%**
5. **`examples/wasip1/main.c`** -> AI Confidence: **99.34%**
6. **`cranelift/assembler-x64/src/gpr.rs`** -> AI Confidence: **99.33%**
7. **`ci/docker/x86_64-musl/Dockerfile`** -> AI Confidence: **99.32%**
8. **`cranelift/assembler-x64/src/mem.rs`** -> AI Confidence: **99.31%**
9. **`cranelift/codegen/src/cfg_printer.rs`** -> AI Confidence: **99.31%**
10. **`cranelift/codegen/src/data_value.rs`** -> AI Confidence: **99.31%**
11. **`cranelift/codegen/src/inst_predicates.rs`** -> AI Confidence: **99.31%**
12. **`cranelift/codegen/src/ir/globalvalue.rs`** -> AI Confidence: **99.31%**
13. **`cranelift/codegen/src/ir/immediates.rs`** -> AI Confidence: **99.31%**
14. **`cranelift/codegen/src/ir/memflags.rs`** -> AI Confidence: **99.31%**
15. **`cranelift/codegen/src/isa/aarch64/lower/isle.rs`** -> AI Confidence: **99.31%**
16. **`cranelift/codegen/src/isa/mod.rs`** -> AI Confidence: **99.31%**
17. **`cranelift/codegen/src/isa/riscv64/inst/args.rs`** -> AI Confidence: **99.31%**
18. **`cranelift/codegen/src/isa/riscv64/inst/emit.rs`** -> AI Confidence: **99.31%**
19. **`cranelift/codegen/src/isa/unwind/winx64.rs`** -> AI Confidence: **99.31%**
20. **`cranelift/filetests/src/subtest.rs`** -> AI Confidence: **99.31%**
21. **`cranelift/filetests/src/test_domtree.rs`** -> AI Confidence: **99.31%**
22. **`cranelift/filetests/src/test_inline.rs`** -> AI Confidence: **99.31%**
23. **`cranelift/filetests/src/test_unwind.rs`** -> AI Confidence: **99.31%**
24. **`cranelift/fuzzgen/src/cranelift_arbitrary.rs`** -> AI Confidence: **99.31%**
25. **`cranelift/interpreter/src/step.rs`** -> AI Confidence: **99.31%**
26. **`cranelift/interpreter/src/value.rs`** -> AI Confidence: **99.31%**
27. **`cranelift/isle/isle/src/codegen.rs`** -> AI Confidence: **99.31%**
28. **`cranelift/reader/src/parser.rs`** -> AI Confidence: **99.31%**
29. **`cranelift/src/cat.rs`** -> AI Confidence: **99.31%**
30. **`crates/cache/src/config.rs`** -> AI Confidence: **99.31%**
31. **`crates/cli-flags/src/opt.rs`** -> AI Confidence: **99.31%**
32. **`crates/cranelift/src/lib.rs`** -> AI Confidence: **99.31%**
33. **`crates/fuzzing/src/oom.rs`** -> AI Confidence: **99.31%**
34. **`crates/fuzzing/tests/oom/vec.rs`** -> AI Confidence: **99.31%**
35. **`crates/test-macros/src/wasmtime_test.rs`** -> AI Confidence: **99.31%**
36. **`crates/test-programs/src/bin/p2_api_read_only.rs`** -> AI Confidence: **99.31%**
37. **`crates/test-programs/src/bin/p2_tls_sample_application.rs`** -> AI Confidence: **99.31%**
38. **`crates/wasi-common/src/lib.rs`** -> AI Confidence: **99.31%**
39. **`crates/wasi-common/src/sync/file.rs`** -> AI Confidence: **99.31%**
40. **`crates/wasi-common/src/sync/net.rs`** -> AI Confidence: **99.31%**
41. **`crates/wasi-common/src/sync/sched/unix.rs`** -> AI Confidence: **99.31%**
42. **`crates/wasi-nn/src/witx.rs`** -> AI Confidence: **99.31%**
43. **`crates/wasi-nn/tests/check/onnx.rs`** -> AI Confidence: **99.31%**
44. **`crates/wasi-nn/tests/check/openvino.rs`** -> AI Confidence: **99.31%**
45. **`crates/wasi-nn/tests/check/pytorch.rs`** -> AI Confidence: **99.31%**
46. **`crates/wasi/src/filesystem.rs`** -> AI Confidence: **99.31%**
47. **`crates/wasi/src/p3/cli/mod.rs`** -> AI Confidence: **99.31%**
48. **`crates/wasi/src/p3/filesystem/mod.rs`** -> AI Confidence: **99.31%**
49. **`crates/wasi/src/p3/sockets/conv.rs`** -> AI Confidence: **99.31%**
50. **`crates/wasmtime/src/profiling_agent.rs`** -> AI Confidence: **99.31%**
51. **`crates/wasmtime/src/runtime/component/values.rs`** -> AI Confidence: **99.31%**
52. **`crates/wasmtime/src/runtime/gc/disabled/anyref.rs`** -> AI Confidence: **99.31%**
53. **`crates/wasmtime/src/runtime/gc/disabled/eqref.rs`** -> AI Confidence: **99.31%**
54. **`crates/wasmtime/src/runtime/types/matching.rs`** -> AI Confidence: **99.31%**
55. **`crates/wasmtime/src/runtime/values.rs`** -> AI Confidence: **99.31%**
56. **`crates/wasmtime/src/runtime/vm/component/handle_table.rs`** -> AI Confidence: **99.31%**
57. **`crates/wasmtime/src/runtime/vm/instance/allocator/pooling/decommit_queue.rs`** -> AI Confidence: **99.31%**
58. **`crates/wasmtime/src/runtime/vm/instance/allocator/pooling/memory_pool.rs`** -> AI Confidence: **99.31%**
59. **`crates/wasmtime/src/runtime/vm/memory.rs`** -> AI Confidence: **99.31%**
60. **`crates/wasmtime/src/runtime/vm/memory/shared_memory_disabled.rs`** -> AI Confidence: **99.31%**
61. **`crates/wasmtime/src/runtime/vm/provenance.rs`** -> AI Confidence: **99.31%**
62. **`crates/wasmtime/src/runtime/wave/component.rs`** -> AI Confidence: **99.31%**
63. **`crates/wast/src/core.rs`** -> AI Confidence: **99.31%**
64. **`crates/wiggle/generate/src/config.rs`** -> AI Confidence: **99.31%**
65. **`crates/wizer/src/component/parse.rs`** -> AI Confidence: **99.31%**
66. **`examples/min-platform/src/main.rs`** -> AI Confidence: **99.31%**
67. **`src/commands/objdump.rs`** -> AI Confidence: **99.31%**
68. **`src/common.rs`** -> AI Confidence: **99.31%**
69. **`tests/all/cli_tests.rs`** -> AI Confidence: **99.31%**
70. **`tests/all/native_debug/lldb.rs`** -> AI Confidence: **99.31%**
71. **`tests/wasi.rs`** -> AI Confidence: **99.31%**
72. **`winch/codegen/src/codegen/bounds.rs`** -> AI Confidence: **99.31%**
73. **`winch/codegen/src/codegen/call.rs`** -> AI Confidence: **99.31%**
74. **`winch/codegen/src/codegen/mod.rs`** -> AI Confidence: **99.31%**
75. **`winch/codegen/src/isa/x64/masm.rs`** -> AI Confidence: **99.31%**
76. **`crates/c-api/include/wasmtime/extern.hh`** -> AI Confidence: **99.31%**
77. **`examples/async.cc`** -> AI Confidence: **99.31%**
78. **`cranelift/tests/filetests.rs`** -> AI Confidence: **99.29%**
79. **`cranelift/tests/logged-filetests.rs`** -> AI Confidence: **99.29%**
80. **`crates/test-programs/src/bin/p2_cli_large_env.rs`** -> AI Confidence: **99.29%**
81. **`benches/wasmtime-serve-rps.sh`** -> AI Confidence: **99.29%**
82. **`ci/docker/aarch64-linux/Dockerfile`** -> AI Confidence: **99.29%**
83. **`ci/docker/aarch64-musl/Dockerfile`** -> AI Confidence: **99.29%**
84. **`ci/docker/armv7-linux/Dockerfile`** -> AI Confidence: **99.29%**
85. **`ci/docker/riscv64gc-linux/Dockerfile`** -> AI Confidence: **99.29%**
86. **`ci/docker/s390x-linux/Dockerfile`** -> AI Confidence: **99.29%**
87. **`crates/c-api/include/wasmtime/conf.h.in`** -> AI Confidence: **99.29%**
88. **`cranelift/codegen/src/isa/riscv64/inst/vector.rs`** -> AI Confidence: **99.25%**
89. **`crates/component-macro/src/bindgen.rs`** -> AI Confidence: **99.25%**
90. **`crates/wasmtime/src/runtime/vm/stack_switching/stack/unix.rs`** -> AI Confidence: **99.25%**
91. **`src/commands/run.rs`** -> AI Confidence: **99.25%**
92. **`cranelift/assembler-x64/meta/src/dsl/format.rs`** -> AI Confidence: **99.24%**
93. **`cranelift/codegen/meta/src/gen_asm.rs`** -> AI Confidence: **99.24%**
94. **`cranelift/codegen/meta/src/gen_inst.rs`** -> AI Confidence: **99.24%**
95. **`cranelift/codegen/src/ir/exception_table.rs`** -> AI Confidence: **99.24%**
96. **`cranelift/codegen/src/ir/extfunc.rs`** -> AI Confidence: **99.24%**
97. **`cranelift/codegen/src/isa/call_conv.rs`** -> AI Confidence: **99.24%**
98. **`cranelift/codegen/src/isa/pulley_shared/inst/args.rs`** -> AI Confidence: **99.24%**
99. **`cranelift/codegen/src/isa/s390x/abi.rs`** -> AI Confidence: **99.24%**
100. **`cranelift/codegen/src/isa/x64/abi.rs`** -> AI Confidence: **99.24%**
101. **`cranelift/codegen/src/isa/x64/inst/args.rs`** -> AI Confidence: **99.24%**
102. **`cranelift/codegen/src/machinst/reg.rs`** -> AI Confidence: **99.24%**
103. **`cranelift/codegen/src/remove_constant_phis.rs`** -> AI Confidence: **99.24%**
104. **`cranelift/codegen/src/settings.rs`** -> AI Confidence: **99.24%**
105. **`cranelift/codegen/src/verifier/mod.rs`** -> AI Confidence: **99.24%**
106. **`cranelift/filetests/src/runner.rs`** -> AI Confidence: **99.24%**
107. **`cranelift/filetests/src/test_verifier.rs`** -> AI Confidence: **99.24%**
108. **`cranelift/isle/isle/src/overlap.rs`** -> AI Confidence: **99.24%**
109. **`cranelift/isle/veri/veri_engine/src/verify.rs`** -> AI Confidence: **99.24%**
110. **`cranelift/object/src/backend.rs`** -> AI Confidence: **99.24%**
111. **`cranelift/reader/src/isaspec.rs`** -> AI Confidence: **99.24%**
112. **`cranelift/reader/src/lexer.rs`** -> AI Confidence: **99.24%**
113. **`cranelift/reader/src/sourcemap.rs`** -> AI Confidence: **99.24%**
114. **`cranelift/src/run.rs`** -> AI Confidence: **99.24%**
115. **`crates/c-api/src/vec.rs`** -> AI Confidence: **99.24%**
116. **`crates/cache/src/lib.rs`** -> AI Confidence: **99.24%**
117. **`crates/cache/src/worker.rs`** -> AI Confidence: **99.24%**
118. **`crates/cli-flags/src/lib.rs`** -> AI Confidence: **99.24%**
119. **`crates/debugger/src/host/api.rs`** -> AI Confidence: **99.24%**
120. **`crates/environ/examples/factc.rs`** -> AI Confidence: **99.24%**
121. **`crates/environ/src/compile/module_environ.rs`** -> AI Confidence: **99.24%**
122. **`crates/environ/src/fact/signature.rs`** -> AI Confidence: **99.24%**
123. **`crates/environ/src/module_artifacts.rs`** -> AI Confidence: **99.24%**
124. **`crates/environ/src/types.rs`** -> AI Confidence: **99.24%**
125. **`crates/fuzzing/src/generators/config.rs`** -> AI Confidence: **99.24%**
126. **`crates/fuzzing/src/generators/gc_ops/mutator.rs`** -> AI Confidence: **99.24%**
127. **`crates/fuzzing/tests/oom/caller.rs`** -> AI Confidence: **99.24%**
128. **`crates/fuzzing/tests/oom/types.rs`** -> AI Confidence: **99.24%**
129. **`crates/gdbstub-component/src/lib.rs`** -> AI Confidence: **99.24%**
130. **`crates/jit-icache-coherence/src/libc.rs`** -> AI Confidence: **99.24%**
131. **`crates/misc/component-async-tests/tests/scenario/util.rs`** -> AI Confidence: **99.24%**
132. **`crates/test-programs/src/bin/p3_http_proxy.rs`** -> AI Confidence: **99.24%**
133. **`crates/test-programs/src/sockets.rs`** -> AI Confidence: **99.24%**
134. **`crates/test-util/src/wast.rs`** -> AI Confidence: **99.24%**
135. **`crates/unwinder/src/arch/mod.rs`** -> AI Confidence: **99.24%**
136. **`crates/wasi-common/src/snapshots/preview_1.rs`** -> AI Confidence: **99.24%**
137. **`crates/wasi-common/src/sync/dir.rs`** -> AI Confidence: **99.24%**
138. **`crates/wasi-common/src/sync/sched/windows.rs`** -> AI Confidence: **99.24%**
139. **`crates/wasi-http/src/field_map.rs`** -> AI Confidence: **99.24%**
140. **`crates/wasi-http/src/p2/types.rs`** -> AI Confidence: **99.24%**
141. **`crates/wasi-http/src/p2/types_impl.rs`** -> AI Confidence: **99.24%**
142. **`crates/wasi-io/src/lib.rs`** -> AI Confidence: **99.24%**
143. **`crates/wasi-keyvalue/src/lib.rs`** -> AI Confidence: **99.24%**
144. **`crates/wasi-nn/src/backend/onnx.rs`** -> AI Confidence: **99.24%**
145. **`crates/wasi-nn/src/backend/openvino.rs`** -> AI Confidence: **99.24%**
146. **`crates/wasi-nn/src/backend/pytorch.rs`** -> AI Confidence: **99.24%**
147. **`crates/wasi-threads/src/lib.rs`** -> AI Confidence: **99.24%**
148. **`crates/wasi/src/p1.rs`** -> AI Confidence: **99.24%**
149. **`crates/wasi/src/p2/host/filesystem.rs`** -> AI Confidence: **99.24%**
150. **`crates/wasi/src/p2/host/network.rs`** -> AI Confidence: **99.24%**
151. **`crates/wasi/src/p2/stdio.rs`** -> AI Confidence: **99.24%**
152. **`crates/wasi/src/p3/sockets/host/types/udp.rs`** -> AI Confidence: **99.24%**
153. **`crates/wasi/src/sockets/util.rs`** -> AI Confidence: **99.24%**
154. **`crates/wasmtime/src/engine.rs`** -> AI Confidence: **99.24%**
155. **`crates/wasmtime/src/engine/serialization.rs`** -> AI Confidence: **99.24%**
156. **`crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`** -> AI Confidence: **99.24%**
157. **`crates/wasmtime/src/runtime/component/matching.rs`** -> AI Confidence: **99.24%**
158. **`crates/wasmtime/src/runtime/coredump.rs`** -> AI Confidence: **99.24%**
159. **`crates/wasmtime/src/runtime/gc/disabled/arrayref.rs`** -> AI Confidence: **99.24%**
160. **`crates/wasmtime/src/runtime/gc/enabled/eqref.rs`** -> AI Confidence: **99.24%**
161. **`crates/wasmtime/src/runtime/linker.rs`** -> AI Confidence: **99.24%**
162. **`crates/wasmtime/src/runtime/module/registry.rs`** -> AI Confidence: **99.24%**
163. **`crates/wasmtime/src/runtime/vm/gc/enabled/structref.rs`** -> AI Confidence: **99.24%**
164. **`crates/wasmtime/tests/host_segfault.rs`** -> AI Confidence: **99.24%**
165. **`crates/wiggle/generate/src/names.rs`** -> AI Confidence: **99.24%**
166. **`examples/min-platform/embedding/src/lib.rs`** -> AI Confidence: **99.24%**
167. **`pulley/src/profile.rs`** -> AI Confidence: **99.24%**
168. **`scripts/publish.rs`** -> AI Confidence: **99.24%**
169. **`src/commands/wast.rs`** -> AI Confidence: **99.24%**
170. **`src/commands/wizer.rs`** -> AI Confidence: **99.24%**
171. **`tests/all/guest_debug/mod.rs`** -> AI Confidence: **99.24%**
172. **`winch/codegen/src/codegen/context.rs`** -> AI Confidence: **99.24%**
173. **`winch/codegen/src/codegen/control.rs`** -> AI Confidence: **99.24%**
174. **`winch/codegen/src/isa/aarch64/address.rs`** -> AI Confidence: **99.24%**
175. **`winch/codegen/src/isa/x64/abi.rs`** -> AI Confidence: **99.24%**
176. **`winch/codegen/src/stack.rs`** -> AI Confidence: **99.24%**
177. **`examples/interrupt.c`** -> AI Confidence: **99.24%**
178. **`cranelift/codegen/src/ir/entities.rs`** -> AI Confidence: **99.23%**
179. **`cranelift/codegen/src/opts/div_const.rs`** -> AI Confidence: **99.23%**
180. **`cranelift/codegen/src/scoped_hash_map.rs`** -> AI Confidence: **99.23%**
181. **`cranelift/src/print_cfg.rs`** -> AI Confidence: **99.23%**
182. **`crates/environ/src/module.rs`** -> AI Confidence: **99.23%**
183. **`crates/fuzzing/src/generators/component_async.rs`** -> AI Confidence: **99.23%**
184. **`crates/fuzzing/tests/oom/func_type.rs`** -> AI Confidence: **99.23%**
185. **`crates/test-programs/src/p3/sockets.rs`** -> AI Confidence: **99.23%**
186. **`crates/wasmtime/src/runtime/vm/sys/windows/vectored_exceptions.rs`** -> AI Confidence: **99.23%**
187. **`crates/wizer/src/component/rewrite.rs`** -> AI Confidence: **99.23%**
188. **`fuzz/fuzz_targets/instantiate.rs`** -> AI Confidence: **99.23%**
189. **`examples/threads.c`** -> AI Confidence: **99.23%**
190. **`examples/linking.c`** -> AI Confidence: **99.22%**
191. **`crates/fuzzing/src/generators/pooling_config.rs`** -> AI Confidence: **99.2%**
192. **`benches/call.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20793` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/wasmtime/src/runtime/component/store.rs` (RUST) -> Cumulative Risk: **729.71**
- **Archetype:** `file_cluster_4` (Distance: 13.719 IQR)
- **Magnitude:** 332.86 | **LOC:** 537 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9938%), State Flux (84.9907%)
- **Heaviest Functions:** `assert_instance_states_empty` (Impact: 10.9), `drop_fibers_and_futures` (Impact: 8.0), `concurrent_resource_table` (Impact: 6.4)

### 2. `crates/wasmtime/src/runtime/component/concurrent_disabled.rs` (RUST) -> Cumulative Risk: **680.36**
- **Archetype:** `file_cluster_4` (Distance: 14.003 IQR)
- **Magnitude:** 173.8 | **LOC:** 198 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `linear_lower_to_flat` (Impact: 3.9), `linear_lower_to_memory` (Impact: 3.9), `linear_lower_to_flat` (Impact: 3.9)

### 3. `crates/wasi/src/random.rs` (RUST) -> Cumulative Risk: **655.13**
- **Archetype:** `file_cluster_4` (Distance: 20.022 IQR)
- **Magnitude:** 70.24 | **LOC:** 145 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Tech Debt (99.9871%), Concurrency (99.9628%)
- **Heaviest Functions:** `random` (Impact: 4.4), `deterministic` (Impact: 3.9), `fill_bytes` (Impact: 3.7)

### 4. `crates/explorer/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **640.69**
- **Archetype:** `file_cluster_4` (Distance: 12.759 IQR)
- **Magnitude:** 188.18 | **LOC:** 312 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9992%), Concurrency (92.0247%)
- **Heaviest Functions:** `linkElements` (Impact: 14.8), `linkElements` (Impact: 9.2), `renderBytes` (Impact: 7.5)

### 5. `crates/wizer/src/component/wasmtime.rs` (RUST) -> Cumulative Risk: **635.69**
- **Archetype:** `file_cluster_4` (Distance: 12.346 IQR)
- **Magnitude:** 225.28 | **LOC:** 145 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (90.9258%)
- **Heaviest Functions:** `run_component` (Impact: 18.3), `validate_component_init_func` (Impact: 13.1), `initialize_component` (Impact: 8.1)

### 6. `crates/wasi-common/src/sched.rs` (RUST) -> Cumulative Risk: **633.36**
- **Archetype:** `file_cluster_4` (Distance: 12.317 IQR)
- **Magnitude:** 87.88 | **LOC:** 92 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9975%), Cognitive Load (99.7527%)
- **Heaviest Functions:** `sleep` (Impact: 4.0), `earliest_clock_deadline` (Impact: 3.9), `subscribe_monotonic_clock` (Impact: 2.5)

### 7. `crates/misc/component-async-tests/src/resource_stream.rs` (RUST) -> Cumulative Risk: **620.07**
- **Archetype:** `file_cluster_13` (Distance: 12.541 IQR)
- **Magnitude:** 37.0 | **LOC:** 53 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.998%), State Flux (99.9599%), Concurrency (99.921%)
- **Heaviest Functions:** `foo` (Impact: 6.7), `foo` (Impact: 3.7), `drop` (Impact: 3.7)

### 8. `crates/wasmtime/src/runtime/vm/instance/allocator.rs` (RUST) -> Cumulative Risk: **617.5**
- **Archetype:** `file_cluster_4` (Distance: 14.316 IQR)
- **Magnitude:** 499.44 | **LOC:** 863 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), State Flux (99.998%), Tech Debt (98.762%)
- **Heaviest Functions:** `initialize_memories` (Impact: 44.6), `write` (Impact: 36.6), `default` (Impact: 21.3)

### 9. `crates/wasi-common/src/tokio/mod.rs` (RUST) -> Cumulative Risk: **615.66**
- **Archetype:** `file_cluster_13` (Distance: 14.097 IQR)
- **Magnitude:** 152.32 | **LOC:** 136 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.4451%), Tech Debt (98.3882%)
- **Heaviest Functions:** `inherit_env` (Impact: 6.3), `inherit_args` (Impact: 6.3), `envs` (Impact: 5.5)

### 10. `crates/wasmtime/src/runtime/linker.rs` (RUST) -> Cumulative Risk: **613.03**
- **Archetype:** `file_cluster_4` (Distance: 19.153 IQR)
- **Magnitude:** 977.6 | **LOC:** 1531 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9994%), State Flux (98.0291%), Tech Debt (93.9653%)
- **Heaviest Functions:** `module` (Impact: 281.3), `command` (Impact: 81.8), `get_default` (Impact: 25.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/wasmtime/src/runtime/vm/libcalls.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.455 IQR)
- **Top Global Matches:** file_cluster_4: 13.455, file_cluster_8: 13.484, file_cluster_0: 13.507
- **Magnitude:** 18952.84 | **LOC:** 1764 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.2626%), Tech Debt (10.8243%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 458`, `args: 113`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 270`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `concurrency: 121`, `import: 34`
* *Defense:* `safety: 131`, `doc: 124`, `test: 5`, `sync_locks: 3`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::runtime::vm::
    self, vm::SendSyncPtr, crate::runtime::vm::vmcontext::VMFuncRef, f64x2, crate::prelude::*, RootedGcRefImpl, Val, StoreInstanceId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.612 IQR)
- **Top Global Matches:** file_cluster_16: 14.612, file_cluster_4: 14.755, file_cluster_8: 14.786
- **Magnitude:** 4033.92 | **LOC:** 4944 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 72.7%
- **Risk Profile:** Cognitive Load (40.3864%), Tech Debt (99.3484%)
**Top Internal Functions/Classes:**
  * `poll_produce` (Impact: 545.1)
  * `new` (Impact: 493.9)
  * `copy` (Impact: 200.9)
  * `guest_read` (Impact: 180.4)
  * `guest_write` (Impact: 177.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 676`, `structural_boundaries: 912`, `args: 232`, `func_start: 151`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 456`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 66`, `orphaned_logic: 25`
* *Architecture:* `io: 6`, `api: 83`, `concurrency: 375`, `import: 38`
* *Defense:* `safety: 560`, `doc: 623`, `test: 19`, `sync_locks: 18`, `immutability_locks: 48`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::Event, ComponentTypes, super::table::TableDebug, Instance, bail, crate::
    Error, SliceBuffer, tls...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pulley/src/interp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.692 IQR)
- **Top Global Matches:** file_cluster_16: 13.692, file_cluster_0: 13.745, file_cluster_8: 13.823
- **Magnitude:** 3264.82 | **LOC:** 5631 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (19.5802%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `push_frame_save` (Impact: 16.4)
  * `xrem32_s` (Impact: 9.5)
  * `xrem64_s` (Impact: 9.5)
  * `xselect32` (Impact: 8.7)
  * `xselect64` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 1652`, `args: 656`, `func_start: 590`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1210`, `dead_code: 2`, `planned_debt: 6`, `duplicate_logic: 29`, `orphaned_logic: 476`
* *Architecture:* `api: 30`, `import: 20`
* *Defense:* `safety: 76`, `doc: 227`, `test: 14`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IndexMut, pulley_macros::interp_disable_if_cfg, crate::profile::ExecutingPc, core::fmt, wasmtime_core::math::WasmFloat, core::mem, core::ptr::NonNull, crate::regs::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/visitor.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.539 IQR)
- **Top Global Matches:** file_cluster_8: 14.539, file_cluster_11: 14.567, file_cluster_13: 14.612
- **Magnitude:** 3060.78 | **LOC:** 4688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.5585%), Tech Debt (7.6977%)
**Top Internal Functions/Classes:**
  * `visit_call_indirect` (Impact: 17.6)
  * `visit_select` (Impact: 14.9)
  * `visit_v128_bitselect` (Impact: 12.9)
  * `visit_table_init` (Impact: 12.8)
  * `visit_table_copy` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 758`, `args: 733`, `func_start: 493`
* *Risk/State:* `state_mutation: 863`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 490`, `import: 51`
* *Defense:* `safety: 308`, `doc: 11`, `sync_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MemArg, V128ExtAddKind, bail, DivKind, RoundingMode, Ieee32, Emission, ValType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/func.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.993 IQR)
- **Top Global Matches:** file_cluster_0: 14.993, file_cluster_11: 15.057, file_cluster_8: 15.338
- **Magnitude:** 2749.42 | **LOC:** 2356 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.7295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func_constructors` (Impact: 142.7)
  * `wrap_multiple_results` (Impact: 117.8)
  * `calls_with_funcref_and_externref` (Impact: 61.8)
  * `get_from_wrapper` (Impact: 61.2)
  * `typed_v128_imports` (Impact: 41.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 1007`, `args: 209`, `func_start: 62`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1417`, `dead_code: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 48`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 299`, `test: 272`, `sync_locks: 2`, `immutability_locks: 45`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::*, std::sync::atomic::AtomicBool, wasmtime::bail, std::sync::atomic::Ordering, Ordering::SeqCst, wasmtime_test_macros::wasmtime_test, AtomicUsize, std::sync::Arc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cranelift/src/func_environ.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.221 IQR)
- **Top Global Matches:** file_cluster_8: 13.221, file_cluster_0: 13.318, file_cluster_13: 13.341
- **Magnitude:** 2740.56 | **LOC:** 4333 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.1755%), Tech Debt (92.7968%)
**Top Internal Functions/Classes:**
  * `check_and_load_code_and_callee_vmctx` (Impact: 270.1)
  * `fuel_before_op` (Impact: 265.8)
    * *Intent:* /// A `GlobalValue` in CLIF which represents the stack limit.
  * `translate_ref_is_null` (Impact: 256.7)
  * `call_ref` (Impact: 228.9)
  * `translate_loop_header` (Impact: 106.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 879`, `args: 175`, `func_start: 169`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 530`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 89`
* *Architecture:* `api: 137`, `import: 24`
* *Defense:* `safety: 155`, `doc: 156`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FrameStateSlotBuilder, FrameValType, MemFlags, cranelift_codegen::ir::Block, EngineOrModuleTypeIndex, PrimaryMap, cranelift_frontend::Variable, DataIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/environ/src/fact/trampoline.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.914 IQR)
- **Top Global Matches:** file_cluster_8: 12.914, file_cluster_11: 13.001, file_cluster_6: 13.035
- **Magnitude:** 2659.22 | **LOC:** 4420 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (10.2849%), Tech Debt (76.7991%)
**Top Internal Functions/Classes:**
  * `validate_memory_inbounds` (Impact: 462.4)
  * `calculate_list_byte_len` (Impact: 413.0)
    * *Intent:* // Assert that the untagged code unit length is the same as the
  * `translate` (Impact: 279.1)
  * `convert_variant` (Impact: 244.6)
  * `compile` (Impact: 221.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 489`, `args: 165`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 6`, `state_mutation: 260`, `dead_code: 12`, `planned_debt: 105`, `fragile_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 180`, `doc: 198`, `test: 43`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, std::collections::HashMap, Module, Function, crate::component::
    CanonicalAbiInfo, crate::prelude::*, crate::fact::signature::Signature, std::mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/func.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.141 IQR)
- **Top Global Matches:** file_cluster_4: 13.141, file_cluster_8: 13.211, file_cluster_0: 13.324
- **Magnitude:** 2624.74 | **LOC:** 4649 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (45.222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `integers` (Impact: 151.4)
  * `drop_call_async_future` (Impact: 143.7)
  * `test_many_results` (Impact: 92.3)
  * `test_many_parameters` (Impact: 63.4)
  * `strings` (Impact: 49.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 952`, `args: 119`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1091`, `fragile_debt: 4`
* *Architecture:* `api: 51`, `concurrency: 335`, `import: 6`
* *Defense:* `safety: 196`, `doc: 12`, `test: 206`, `sync_locks: 1`, `immutability_locks: 192`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Trap, Engine, StoreContextMut, Store, std::sync::
    Arc, Ordering::SeqCst, super::ApiStyle, atomic::AtomicBool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/reader/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.564 IQR)
- **Top Global Matches:** file_cluster_8: 13.564, file_cluster_0: 13.715, file_cluster_13: 13.715
- **Magnitude:** 2324.86 | **LOC:** 3719 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.9535%), Tech Debt (9.251%)
**Top Internal Functions/Classes:**
  * `parse_instruction` (Impact: 805.4)
  * `parse_target_specs` (Impact: 618.5)
  * `parse_basic_block` (Impact: 37.9)
  * `parse_literals_to_constant_data` (Impact: 22.1)
  * `parse_value_alias` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 481`, `args: 148`, `func_start: 122`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 291`, `duplicate_logic: 2`
* *Architecture:* `api: 30`, `import: 25`
* *Defense:* `safety: 273`, `doc: 83`, `test: 174`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cranelift_codegen::ir::DebugTag, ArgumentExtension, cranelift_codegen::isa::self, StackSlotData, LocatedError, MemFlags, FuncRef, crate::isaspec::IsaSpec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/debugger/src/host/api.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.083 IQR)
- **Top Global Matches:** file_cluster_4: 15.083, file_cluster_16: 15.53, file_cluster_11: 15.677
- **Magnitude:** 1704.18 | **LOC:** 1056 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.888%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `make` (Impact: 17.9)
  * `get_memory` (Impact: 15.4)
  * `get_global` (Impact: 15.4)
  * `get_table` (Impact: 15.4)
  * `get_func` (Impact: 15.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 346`, `args: 100`, `func_start: 97`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 254`, `planned_debt: 1`, `duplicate_logic: 35`, `orphaned_logic: 47`
* *Architecture:* `api: 10`, `concurrency: 669`, `import: 10`
* *Defense:* `safety: 258`, `doc: 33`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` host::bindings::wasm_type_to_val_type, Memory, Module, Val, Pollable, Ordering, Instance, wasmtime::
    Engine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cranelift/src/translate/code_translator.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.515 IQR)
- **Top Global Matches:** file_cluster_8: 13.515, file_cluster_16: 13.52, file_cluster_17: 13.554
- **Magnitude:** 1658.12 | **LOC:** 4498 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (17.6034%), Tech Debt (30.1482%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 88`, `args: 19`, `func_start: 12`
* *Risk/State:* `state_mutation: 56`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 12`, `doc: 124`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blocktype_params_results, smallvec::SmallVec, JumpTableData, std::collections::HashMap, Operator, crate::bounds_checks::BoundsCheck, f64_translation, MemArg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cache/src/worker.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.075 IQR)
- **Top Global Matches:** file_cluster_0: 11.075, file_cluster_8: 11.266, file_cluster_13: 11.383
- **Magnitude:** 1654.49 | **LOC:** 897 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6809%), Tech Debt (13.4584%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 53`, `args: 14`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 16`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 18`, `doc: 19`, `test: 6`, `sync_locks: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` info, std::collections::HashMap, sync_channel, std::ffi::OsStr, trace, tests::system_time_stub::SystemTimeStub, windows_sys::Win32::System::Threading::*, std::sync::mpsc::Receiver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasi-common/src/snapshots/preview_1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.268 IQR)
- **Top Global Matches:** file_cluster_4: 13.268, file_cluster_8: 13.542, file_cluster_17: 13.658
- **Magnitude:** 1603.24 | **LOC:** 1571 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.7721%), Tech Debt (99.5656%)
**Top Internal Functions/Classes:**
  * `fd_readdir` (Impact: 220.2)
  * `poll_oneoff` (Impact: 120.5)
    * *Intent:* // Like posix readlink(2), silently truncate links when they are larger than the // destination buff...
  * `random_get` (Impact: 117.4)
  * `sock_recv` (Impact: 109.4)
  * `fd_allocate` (Impact: 99.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 325`, `args: 93`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 144`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 37`
* *Architecture:* `io: 3`, `api: 4`, `concurrency: 314`, `import: 11`
* *Defense:* `safety: 160`, `test: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` an intermediate buffer, std::io::SeekFrom, FdStat, ReaddirEntity, std::io::IoSlice, wiggle::GuestType, TableDirExt, std::ops::Deref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasi/src/p1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.105 IQR)
- **Top Global Matches:** file_cluster_4: 15.105, file_cluster_0: 15.16, file_cluster_11: 15.307
- **Magnitude:** 1557.82 | **LOC:** 2719 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.8847%), Tech Debt (91.2206%)
**Top Internal Functions/Classes:**
  * `poll_oneoff` (Impact: 120.8)
  * `new` (Impact: 53.0)
  * `fd_read` (Impact: 45.4)
  * `fd_write_impl` (Impact: 44.2)
  * `fd_readdir` (Impact: 36.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 561`, `args: 133`, `func_start: 91`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 298`, `dead_code: 37`, `planned_debt: 9`, `duplicate_logic: 27`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 275`, `import: 7`
* *Defense:* `safety: 299`, `doc: 343`, `test: 5`, `sync_locks: 1`, `immutability_locks: 5`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` btree_map, Module, HashSet, std::mem::self, error::Context, streams::HostOutputStream, std::future::Future, wiggle::GuestError::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/isa/x64/asm.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.253 IQR)
- **Top Global Matches:** file_cluster_8: 13.253, file_cluster_17: 13.359, file_cluster_13: 13.447
- **Magnitude:** 1500.94 | **LOC:** 2817 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2721%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `div` (Impact: 12.5)
    * *Intent:* /// Signed/unsigned division. /// /// Emits a sequence of instructions to ensure the correctness of
  * `cmp_ir` (Impact: 12.5)
  * `movzx_mr` (Impact: 12.2)
    * *Intent:* /// Zero-extend memory-to-register load.
  * `rem` (Impact: 11.9)
    * *Intent:* /// Signed/unsigned remainder. /// /// Emits a sequence of instructions to ensure the correctness of...
  * `cmov` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 597`, `args: 293`, `func_start: 202`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 8`, `state_mutation: 343`, `planned_debt: 12`, `duplicate_logic: 24`, `orphaned_logic: 158`
* *Architecture:* `api: 183`, `import: 18`
* *Defense:* `safety: 157`, `doc: 277`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smallvec::SmallVec, Final, ExtMode, RemKind, crate::
    constant_pool::ConstantPool, ir::ExternalName, x64::
            AtomicRmwSeqOp, GprMem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/async_functions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.366 IQR)
- **Top Global Matches:** file_cluster_4: 13.366, file_cluster_0: 14.02, file_cluster_11: 14.227
- **Magnitude:** 1486.42 | **LOC:** 1145 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recursive_async` (Impact: 111.8)
  * `cancel_during_run` (Impact: 48.1)
  * `async_gc_with_func_new_and_func_wrap` (Impact: 41.5)
  * `non_stacky_async_activations` (Impact: 32.8)
  * `gc_preserves_externref_on_historical_asy` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 449`, `args: 61`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 306`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `api: 3`, `concurrency: 783`, `import: 7`
* *Defense:* `safety: 143`, `doc: 2`, `test: 36`, `sync_locks: 7`, `immutability_locks: 16`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::*, std::future::Future, std::sync::atomic::AtomicUsize, Mutex, std::task::Context, std::sync::atomic::Ordering, Poll, std::sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/resources.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.686 IQR)
- **Top Global Matches:** file_cluster_0: 13.686, file_cluster_4: 13.697, file_cluster_8: 13.736
- **Magnitude:** 1448.96 | **LOC:** 1806 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.8589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `manually_destroy` (Impact: 380.4)
  * `resource_any` (Impact: 53.9)
  * `drop_in_different_places` (Impact: 25.1)
  * `drop_guest_twice` (Impact: 14.0)
  * `mismatch_resource_types` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 705`, `args: 66`, `func_start: 30`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 825`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 67`, `import: 4`
* *Defense:* `safety: 112`, `test: 125`, `immutability_locks: 15`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Trap, Engine, Store, wasmtime::Config, wasmtime::component::*, wasmtime::Result
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/concurrent.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.329 IQR)
- **Top Global Matches:** file_cluster_13: 15.329, file_cluster_4: 15.345, file_cluster_16: 15.354
- **Magnitude:** 1386.5 | **LOC:** 5493 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 76.9%
- **Risk Profile:** Cognitive Load (38.2454%), Tech Debt (96.7173%)
**Top Internal Functions/Classes:**
  * `waitable_set_wait` (Impact: 276.9)
  * `suspension_intrinsic` (Impact: 142.2)
  * `subtask_cancel` (Impact: 50.3)
  * `join` (Impact: 25.4)
  * `take_fibers_and_futures` (Impact: 25.1)
    * *Intent:* /// Return a closure which will call the specified function in the scope /// of the specified task. ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 433`, `args: 128`, `func_start: 96`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 235`, `dead_code: 17`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 23`, `orphaned_logic: 12`
* *Architecture:* `api: 47`, `concurrency: 186`, `import: 39`
* *Defense:* `safety: 267`, `doc: 790`, `test: 10`, `immutability_locks: 42`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NonNull, std::future::Future, table::TableDebug, Instance, bail, MAX_FLAT_PARAMS, StoreOpaque, GuardedFutureReader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/debugger/src/host/opaque.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.79 IQR)
- **Top Global Matches:** file_cluster_4: 15.79, file_cluster_17: 16.501, file_cluster_16: 16.525
- **Magnitude:** 1375.76 | **LOC:** 583 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.2386%), Tech Debt (18.1538%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 153.5)
  * `memory_read_u64` (Impact: 18.9)
  * `frame_locals` (Impact: 11.2)
  * `frame_stack` (Impact: 11.2)
  * `memory_read_u32` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 291`, `args: 150`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 227`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 751`, `import: 3`
* *Defense:* `safety: 164`, `doc: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Memory, Module, Val, Instance, wasmtime::
    Engine, Tag, ExnRefPre, Table...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/isa/x64/masm.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.867 IQR)
- **Top Global Matches:** file_cluster_8: 13.867, file_cluster_11: 14.175, file_cluster_16: 14.194
- **Magnitude:** 1270.44 | **LOC:** 3598 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.957%), Tech Debt (94.7617%)
**Top Internal Functions/Classes:**
  * `atomic_rmw` (Impact: 248.1)
  * `wasm_load` (Impact: 41.1)
  * `v128_shift` (Impact: 27.8)
  * `popcnt` (Impact: 27.5)
  * `v128_mul` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 218`, `args: 153`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 229`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 60`
* *Architecture:* `import: 9`
* *Defense:* `safety: 294`, `doc: 22`, `test: 4`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` VroundMode, wasmtime_environ::PtrSize, vmctx, V128ExtAddKind, bail, RegClass, RoundingMode, crate::
    abi::ABI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/debug.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.585 IQR)
- **Top Global Matches:** file_cluster_4: 13.585, file_cluster_0: 13.915, file_cluster_8: 14.13
- **Magnitude:** 1253.76 | **LOC:** 1628 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.2928%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stack_values_two_activations` (Impact: 53.1)
  * `stack_values_two_frames` (Impact: 31.8)
  * `private_entity_access` (Impact: 28.1)
  * `component_module_relative_breakpoint_pcs` (Impact: 27.5)
  * `invalidated_frame_handles` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 514`, `args: 50`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 581`
* *Architecture:* `api: 23`, `concurrency: 292`, `import: 7`
* *Defense:* `safety: 83`, `doc: 1`, `test: 146`, `sync_locks: 14`, `immutability_locks: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ModulePC, wasmtime::
    AsContextMut, Module, Val, StoreContextMut, Ordering, Instance, Linker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/run.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.07 IQR)
- **Top Global Matches:** file_cluster_0: 14.07, file_cluster_13: 14.28, file_cluster_4: 14.283
- **Magnitude:** 1201.02 | **LOC:** 1615 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (36.8259%), Tech Debt (27.6307%)
**Top Internal Functions/Classes:**
  * `setup_guest_profiler` (Impact: 386.5)
  * `populate_with_wasi` (Impact: 127.0)
  * `instantiate_and_run` (Impact: 63.4)
    * *Intent:* /// Executes the `main` after instantiating it within `store`. /// /// This applies all configuratio...
  * `execute` (Impact: 50.7)
    * *Intent:* /// Executes the command.
  * `debugger_run` (Impact: 49.2)
    * *Intent:* /// Split off a sub-command representing the invocation of a /// debugger component side-car to this...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 251`, `args: 68`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 191`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 7`, `api: 21`, `concurrency: 77`, `import: 23`
* *Defense:* `safety: 244`, `doc: 71`, `test: 1`, `sync_locks: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RunCommon, RunTarget, WasiKeyValueCtx, WasiKeyValueCtxBuilder, Module, error::Context, WasiConfigVariables, Val...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/limits.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.757 IQR)
- **Top Global Matches:** file_cluster_4: 13.757, file_cluster_0: 14.159, file_cluster_8: 14.38
- **Magnitude:** 1175.28 | **LOC:** 1167 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8258%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_limits_async` (Impact: 28.7)
  * `test_limits` (Impact: 28.6)
  * `test_custom_memory_limiter_async` (Impact: 28.3)
  * `test_custom_memory_limiter` (Impact: 28.2)
  * `test_limits_memory_only` (Impact: 26.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 387`, `args: 71`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 487`, `duplicate_logic: 20`
* *Architecture:* `api: 19`, `concurrency: 310`, `import: 1`
* *Defense:* `safety: 149`, `doc: 4`, `test: 90`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/traps.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.711 IQR)
- **Top Global Matches:** file_cluster_0: 13.711, file_cluster_8: 13.817, file_cluster_4: 13.855
- **Magnitude:** 1170.84 | **LOC:** 1876 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.6421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `div_plus_load_reported_right` (Impact: 30.6)
    * *Intent:* #[test]
  * `sync_then_async_trap` (Impact: 19.7)
  * `catch_trap_calling_across_stores` (Impact: 19.5)
  * `parse_dwarf_info` (Impact: 19.1)
  * `async_then_sync_trap` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 618`, `args: 80`, `func_start: 44`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 111`, `high_risk_execution: 1`, `state_mutation: 640`, `duplicate_logic: 2`, `orphaned_logic: 37`
* *Architecture:* `io: 2`, `concurrency: 45`, `import: 8`
* *Defense:* `safety: 158`, `test: 124`, `sync_locks: 7`, `immutability_locks: 13`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::*, crate::ErrorExt, std::panic::self, Mutex, std::process::Command, AssertUnwindSafe, wasmtime::bail, wasmtime_test_macros::wasmtime_test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/async.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.121 IQR)
- **Top Global Matches:** file_cluster_4: 12.121, file_cluster_8: 12.723, file_cluster_0: 12.727
- **Magnitude:** 1143.36 | **LOC:** 1327 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (41.3723%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sync_lower_async_host_does_not_leak` (Impact: 87.4)
  * `task_deletion` (Impact: 53.8)
    * *Intent:* /// Test task deletion in three situations, for every combination of lift/lower/(guest/host): /// 1....
  * `cancel_host_future` (Impact: 28.9)
  * `poll_through_wasm_activation` (Impact: 24.0)
    * *Intent:* // This test is intended to stress TLS management in the component model around // the management of...
  * `cancel_host_task_does_not_leak` (Impact: 23.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 493`, `args: 31`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 263`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 4`, `orphaned_logic: 11`
* *Architecture:* `concurrency: 551`, `import: 8`
* *Defense:* `safety: 76`, `doc: 19`, `test: 25`, `sync_locks: 5`, `immutability_locks: 56`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` execute_across_threads, component::*, Trap, std::task::Context, Engine, wasmtime::AsContextMut, StoreContextMut, Store...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/wasmtime/src/runtime/vm/sys/custom/vm.rs` (RUST) | Magnitude: 71.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, api: 25, structural_boundaries: 22, safety: 21
- `winch/codegen/src/stack.rs` (RUST) | Magnitude: 250.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 292, doc: 92, args: 57, api: 53
- `cranelift/assembler-x64/src/rex.rs` (RUST) | Magnitude: 52.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 76, indent_spaces: 49, safety: 14, api: 11
- `cranelift/codegen/src/ir/known_symbol.rs` (RUST) | Magnitude: 11.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 10, safety: 10, decorators: 5
- `cranelift/codegen/src/isa/riscv64/inst/imms.rs` (RUST) | Magnitude: 211.82 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 65, branch: 44, safety: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/wasmtime/src/runtime/func.rs` (RUST) | Magnitude: 836.82 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 1295, indent_spaces: 670, structural_boundaries: 211, generics: 183
- `crates/wasi-http/src/p2/mod.rs` (RUST) | Magnitude: 107.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 435, indent_spaces: 169, structural_boundaries: 83, sec_dead_code: 46
- `crates/wasmtime/src/runtime/gc/enabled/rooting.rs` (RUST) | Magnitude: 355.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 1053, indent_spaces: 577, structural_boundaries: 187, generics: 171
- `crates/fuzzing/src/oracles/diff_v8.rs` (RUST) | Magnitude: 213.68 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 145, state_mutation: 132, safety: 32
- `crates/wasmtime/src/runtime/vm/provenance.rs` (RUST) | Magnitude: 12.2 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 128, generics: 33, structural_boundaries: 21, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/wasmtime/src/runtime/component/resources/host.rs` (RUST) | Magnitude: 180.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 114, doc: 40, concurrency: 36, structural_boundaries: 35
- `crates/wasmtime/src/runtime/module/registry.rs` (RUST) | Magnitude: 197.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 247, doc: 93, structural_boundaries: 75, safety: 57
- `crates/wiggle/generate/src/module_trait.rs` (RUST) | Magnitude: 59.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 26, safety: 17, branch: 13
- `cranelift/entity/src/sparse.rs` (RUST) | Magnitude: 54.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 159, doc: 75, test: 71, structural_boundaries: 56
- `crates/wasi-http/src/p2/types.rs` (RUST) | Magnitude: 190.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 169, safety: 52, api: 52, structural_boundaries: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/wasmtime/src/compile.rs` (RUST) | Magnitude: 452.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 837, structural_boundaries: 206, state_mutation: 127, branch: 126
- `crates/wasi-nn/src/wit.rs` (RUST) | Magnitude: 200.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 249, structural_boundaries: 86, safety: 83, generics: 55
- `crates/environ/src/component/translate.rs` (RUST) | Magnitude: 370.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 778, doc: 171, structural_boundaries: 146, state_mutation: 79
- `crates/unwinder/src/stackwalk.rs` (RUST) | Magnitude: 44.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 128, indent_spaces: 72, pointers: 14, structural_boundaries: 13
- `crates/wasmtime/src/runtime/vm/module_id.rs` (RUST) | Magnitude: 7.12 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, doc: 5, structural_boundaries: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/wasi-nn/src/backend/onnx.rs` (RUST) | Magnitude: 258.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 346, structural_boundaries: 110, safety: 98, branch: 83
- `crates/wasi/src/p3/filesystem/mod.rs` (RUST) | Magnitude: 123.32 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, doc: 51, branch: 47, structural_boundaries: 33
- `examples/async.cc` (CPP) | Magnitude: 39.82 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 24, sec_high_risk_execution: 7, branch: 6
- `crates/fuzzing/src/generators/gc_ops/mutator.rs` (RUST) | Magnitude: 370.28 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 377, structural_boundaries: 167, state_mutation: 142, safety: 112
- `cranelift/isle/isle/src/recursion.rs` (RUST) | Magnitude: 46.22 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 21, safety: 17, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/wasi/src/p3/clocks/host.rs` (RUST) | Magnitude: 42.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 20, safety: 12, state_mutation: 9
- `crates/wasmtime/src/runtime/vm/sys/unix/signals.rs` (RUST) | Magnitude: 87.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, doc: 44, state_mutation: 39, structural_boundaries: 35
- `src/commands/serve.rs` (RUST) | Magnitude: 643.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 746, structural_boundaries: 251, safety: 155, state_mutation: 138
- `crates/wasi/src/sockets/mod.rs` (RUST) | Magnitude: 73.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, doc: 53, structural_boundaries: 30, concurrency: 25
- `crates/wizer/tests/all/tests.rs` (RUST) | Magnitude: 480.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 734, structural_boundaries: 189, concurrency: 172, immutability_locks: 108

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `cranelift/codegen/src/cursor.rs` (RUST) | Magnitude: 169.36 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 306, indent_spaces: 161, structural_boundaries: 58, state_mutation: 53
- `crates/wasi-preview1-component-adapter/provider/src/lib.rs` (RUST) | Magnitude: 17.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 40, sec_dead_code: 5, api: 4, immutability_locks: 4
- `crates/wasi/src/p2/bindings.rs` (RUST) | Magnitude: 13.04 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 405, dead_code: 80, structural_boundaries: 2, api: 2
- `cranelift/codegen/src/take_and_replace.rs` (RUST) | Magnitude: 14.14 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 52, indent_spaces: 11, structural_boundaries: 9, state_mutation: 8
- `crates/c-api/src/lib.rs` (RUST) | Magnitude: 11.04 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 26, planned_debt: 2, high_risk_execution: 1, panics_and_aborts: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/c-api/include/wasmtime/config.hh` (CPP) | Magnitude: 163.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 173, indent_spaces: 165, structural_boundaries: 70, state_mutation: 42
- `crates/c-api/include/wasmtime/val.h` (CPP) | Magnitude: 22.92 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 129, pointers: 39, indent_spaces: 39, structural_boundaries: 38
- `winch/codegen/src/isa/aarch64/regs.rs` (RUST) | Magnitude: 48.56 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 91, indent_spaces: 40, immutability_locks: 21, args: 19
- `cranelift/codegen/src/isa/x64/inst/stack_switch.rs` (RUST) | Magnitude: 10.32 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, indent_spaces: 9, api: 6, encapsulation: 6
- `cranelift/codegen/src/ir/user_stack_maps.rs` (RUST) | Magnitude: 7.7 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 111, indent_spaces: 35, structural_boundaries: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `benches/trap.rs` (RUST) | Magnitude: 137.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 84, state_mutation: 73, safety_bypasses: 21
- `crates/cranelift/src/lib.rs` (RUST) | Magnitude: 23.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 75, indent_spaces: 31, safety: 6, branch: 5
- `crates/wasmtime/src/runtime/vm/instance/allocator/pooling/unix_stack_pool.rs` (RUST) | Magnitude: 114.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 41, doc: 36, test: 20
- `crates/wasi/src/cli/mem.rs` (RUST) | Magnitude: 16.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, safety: 8, args: 6
- `cranelift/codegen/src/egraph/cost.rs` (RUST) | Magnitude: 48.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, doc: 36, args: 20, structural_boundaries: 18

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/wasmtime/src/runtime/component/concurrent.rs` -> Churn: **100.0%** | Cog Load: 38.2454% | Debt: 96.7173%
- `crates/cranelift/src/func_environ.rs` -> Churn: **97.19%** | Cog Load: 19.1755% | Debt: 92.7968%
- `crates/core/src/alloc/vec.rs` -> Churn: **94.16%** | Cog Load: 30.1087% | Debt: 78.5409%
- `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` -> Churn: **94.16%** | Cog Load: 40.3864% | Debt: 99.3484%
- `crates/wasmtime/src/runtime/debug.rs` -> Churn: **94.16%** | Cog Load: 9.8047% | Debt: 86.1962%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/wasmtime/src/runtime/vm/libcalls.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 18952.84
- `winch/codegen/src/visitor.rs` -> **r-near** (100.0% isolated ownership) | Magnitude: 3060.78
- `cranelift/reader/src/parser.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 2324.86
- `crates/debugger/src/host/api.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 1704.18
- `crates/wasi/src/p1.rs` -> **Alex Crichton** (100.0% isolated ownership) | Magnitude: 1557.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/c-api/include/wasm.h` -> **Severity: 339.245** (Blast Radius: 18.973 * Doc Risk: 17.8804%)
- `crates/core/src/error/ptr.rs` -> **Severity: 297.6** (Blast Radius: 2.976 * Doc Risk: 100.0%)
- `crates/wasi/src/cli/stdout.rs` -> **Severity: 180.193** (Blast Radius: 4.896 * Doc Risk: 36.8042%)
- `crates/c-api/include/wasmtime.hh` -> **Severity: 176.54** (Blast Radius: 11.848 * Doc Risk: 14.9004%)
- `cranelift/codegen/src/isa/riscv64/inst/vector.rs` -> **Severity: 157.363** (Blast Radius: 3.158 * Doc Risk: 49.8301%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
