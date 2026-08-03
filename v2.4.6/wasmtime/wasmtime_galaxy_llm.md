# ARCHITECTURAL_BRIEF: wasmtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/wasmtime` |
| **Timestamp** | `2026-08-03T19:47:53.590999+00:00` |
| **Scan Duration** | `11.23s` |
| **Git Branch** | `main` |
| **Git Commit** | `5b5e3573d7de1314c6fcd0d327d4e3640ce58138` |
| **Git Remote** | `https://github.com/bytecodealliance/wasmtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1925 malicious artifacts.

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
| Modularity | 0.8552 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `3.92`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 729 | 36.4% |
| file_cluster_13 | 504 | 25.2% |
| file_cluster_0 | 261 | 13.0% |
| file_cluster_16 | 204 | 10.2% |
| file_cluster_4 | 184 | 9.2% |
| file_cluster_17 | 15 | 0.7% |
| file_cluster_7 | 14 | 0.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 20.8 | 11.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 35.0 | 30.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 40.7 | 19.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.2 | 2.4 | 80.0 |
| API Exposure | 0.0 | 15.9 | 3.2 | 3.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.1 | 28.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.3 | 24.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 54.9 | 85.6 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 81.1 | 8.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
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

- `validate_signature_params` (@ `cranelift/interpreter/src/step.rs`) -> Impact: **5345.6** | LOC: 1188
  * *Intent:* /// Ensures that all types in args are the same as expected by the signature
- `new` (@ `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`) -> Impact: **3503.7** | LOC: 1517
- `validate_memory_inbounds` (@ `crates/environ/src/fact/trampoline.rs`) -> Impact: **2870.1** | LOC: 1470
- `emit` (@ `cranelift/codegen/src/isa/riscv64/inst/emit.rs`) -> Impact: **2701.6** | LOC: 1440
- `from_ast` (@ `cranelift/isle/isle/src/sema.rs`) -> Impact: **2354.6** | LOC: 1171
- `parse_u64` (@ `cranelift/codegen/src/ir/immediates.rs`) -> Impact: **2310.4** | LOC: 1409
- `parse_target_specs` (@ `cranelift/reader/src/parser.rs`) -> Impact: **2003.3** | LOC: 1389
- `translate_exn_unbox` (@ `crates/cranelift/src/func_environ/gc/enabled.rs`) -> Impact: **1813.8** | LOC: 955
- `module` (@ `crates/wasmtime/src/runtime/linker.rs`) -> Impact: **1795.1** | LOC: 580
  * *Intent:* /// Asynchronous analog of [`Linker::func_wrap`]. #[cfg(feature = "async")]
- `solve_constraints` (@ `cranelift/isle/veri/veri_engine/src/type_inference.rs`) -> Impact: **1568.2** | LOC: 704

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `next` (@ `cranelift/bforest/src/map.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// An immutable iterator over a range of values, returned by `Map::range`.
- `operands` (@ `cranelift/codegen/meta/src/pulley.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `cranelift/codegen/meta/src/shared/entities.rs`) -> **O(2^N) [Recursive]**
- `start_block` (@ `cranelift/codegen/src/egraph/elaborate.rs`) -> **O(2^N) [Recursive]**
- `parse_u64` (@ `cranelift/codegen/src/ir/immediates.rs`) -> **O(2^N) [Recursive]**
- `emit` (@ `cranelift/codegen/src/isa/aarch64/inst/emit.rs`) -> **O(2^N) [Recursive]**
- `mem_finalize` (@ `cranelift/codegen/src/isa/aarch64/inst/emit.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Memory addressing mode finalization: convert "special" modes (e.g., /// generic arbitrary stack offset) into real addressing modes, possibly by //...
- `aarch64_get_operands` (@ `cranelift/codegen/src/isa/aarch64/inst/mod.rs`) -> **O(2^N) [Recursive]**
- `gen_load` (@ `cranelift/codegen/src/isa/aarch64/inst/mod.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Generic constructor for a load (zero-extending where appropriate).
- `gen_store` (@ `cranelift/codegen/src/isa/aarch64/inst/mod.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Generic constructor for a store.

### Highest Data Gravity (Database Complexity)
- `manually_destroy` (@ `tests/all/component_model/resources.rs`) -> DB Complexity: **202**
- `seal_all_blocks` (@ `cranelift/frontend/src/ssa.rs`) -> DB Complexity: **193**
- `data` (@ `crates/wasmtime/src/runtime/store.rs`) -> DB Complexity: **187**
- `translate_ref_is_null` (@ `crates/cranelift/src/func_environ.rs`) -> DB Complexity: **180**
- `wasm_load` (@ `winch/codegen/src/isa/aarch64/masm.rs`) -> DB Complexity: **128**
- `finish` (@ `crates/debugger/src/host/opaque.rs`) -> DB Complexity: **109**
- `fuel_before_op` (@ `crates/cranelift/src/func_environ.rs`) -> DB Complexity: **106**
  * *Intent:* /// A `GlobalValue` in CLIF which represents the stack limit.
- `handle_fixup` (@ `cranelift/codegen/src/machinst/buffer.rs`) -> DB Complexity: **94**
  * *Intent:* /// Add a slice of bytes.
- `run` (@ `cranelift/frontend/src/frontend/safepoints.rs`) -> DB Complexity: **90**
- `utf16_to_utf8` (@ `crates/wasmtime/src/runtime/vm/component/libcalls.rs`) -> DB Complexity: **89**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/all` | 56 | 30910.68 | 28.82% | 0.0% |
| `crates/wasmtime/src/runtime/vm` | 31 | 25526.52 | 19.9% | 51.74% |
| `tests/all/component_model` | 15 | 13967.9 | 35.13% | 0.0% |
| `crates/wasmtime/src/runtime/component/concurrent` | 6 | 12628.18 | 25.37% | 47.64% |
| `crates/wasmtime/src/runtime` | 31 | 12070.94 | 19.29% | 59.94% |
| `cranelift/isle/isle/src` | 17 | 10860.5 | 16.48% | 47.08% |
| `crates/test-programs/src/bin` | 264 | 9468.3 | 21.1% | 57.81% |
| `crates/wasmtime/src/runtime/component` | 15 | 9148.16 | 26.69% | 53.33% |
| `cranelift/codegen/src` | 31 | 7888.5 | 16.71% | 44.14% |
| `cranelift/codegen/src/ir` | 26 | 7815.82 | 8.6% | 60.93% |

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
- `pulley/src/interp.rs` -> **177** Orphaned Functions | **28** Duplicates
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
20. **`cranelift/codegen/src/isa/x64/inst/args.rs`** -> AI Confidence: **99.31%**
21. **`cranelift/filetests/src/subtest.rs`** -> AI Confidence: **99.31%**
22. **`cranelift/filetests/src/test_domtree.rs`** -> AI Confidence: **99.31%**
23. **`cranelift/filetests/src/test_inline.rs`** -> AI Confidence: **99.31%**
24. **`cranelift/filetests/src/test_unwind.rs`** -> AI Confidence: **99.31%**
25. **`cranelift/fuzzgen/src/cranelift_arbitrary.rs`** -> AI Confidence: **99.31%**
26. **`cranelift/interpreter/src/step.rs`** -> AI Confidence: **99.31%**
27. **`cranelift/interpreter/src/value.rs`** -> AI Confidence: **99.31%**
28. **`cranelift/isle/isle/src/codegen.rs`** -> AI Confidence: **99.31%**
29. **`cranelift/reader/src/parser.rs`** -> AI Confidence: **99.31%**
30. **`cranelift/src/cat.rs`** -> AI Confidence: **99.31%**
31. **`crates/cache/src/config.rs`** -> AI Confidence: **99.31%**
32. **`crates/cli-flags/src/lib.rs`** -> AI Confidence: **99.31%**
33. **`crates/cli-flags/src/opt.rs`** -> AI Confidence: **99.31%**
34. **`crates/cranelift/src/lib.rs`** -> AI Confidence: **99.31%**
35. **`crates/fuzzing/src/oom.rs`** -> AI Confidence: **99.31%**
36. **`crates/fuzzing/tests/oom/func_type.rs`** -> AI Confidence: **99.31%**
37. **`crates/fuzzing/tests/oom/vec.rs`** -> AI Confidence: **99.31%**
38. **`crates/test-macros/src/wasmtime_test.rs`** -> AI Confidence: **99.31%**
39. **`crates/test-programs/src/bin/p2_api_read_only.rs`** -> AI Confidence: **99.31%**
40. **`crates/test-programs/src/bin/p2_tls_sample_application.rs`** -> AI Confidence: **99.31%**
41. **`crates/wasi-common/src/lib.rs`** -> AI Confidence: **99.31%**
42. **`crates/wasi-common/src/sync/file.rs`** -> AI Confidence: **99.31%**
43. **`crates/wasi-common/src/sync/net.rs`** -> AI Confidence: **99.31%**
44. **`crates/wasi-common/src/sync/sched/unix.rs`** -> AI Confidence: **99.31%**
45. **`crates/wasi-nn/src/witx.rs`** -> AI Confidence: **99.31%**
46. **`crates/wasi-nn/tests/check/onnx.rs`** -> AI Confidence: **99.31%**
47. **`crates/wasi-nn/tests/check/openvino.rs`** -> AI Confidence: **99.31%**
48. **`crates/wasi-nn/tests/check/pytorch.rs`** -> AI Confidence: **99.31%**
49. **`crates/wasi/src/filesystem.rs`** -> AI Confidence: **99.31%**
50. **`crates/wasi/src/p3/cli/mod.rs`** -> AI Confidence: **99.31%**
51. **`crates/wasi/src/p3/filesystem/mod.rs`** -> AI Confidence: **99.31%**
52. **`crates/wasi/src/p3/sockets/conv.rs`** -> AI Confidence: **99.31%**
53. **`crates/wasmtime/src/engine.rs`** -> AI Confidence: **99.31%**
54. **`crates/wasmtime/src/profiling_agent.rs`** -> AI Confidence: **99.31%**
55. **`crates/wasmtime/src/runtime/component/values.rs`** -> AI Confidence: **99.31%**
56. **`crates/wasmtime/src/runtime/gc/disabled/anyref.rs`** -> AI Confidence: **99.31%**
57. **`crates/wasmtime/src/runtime/gc/disabled/eqref.rs`** -> AI Confidence: **99.31%**
58. **`crates/wasmtime/src/runtime/types/matching.rs`** -> AI Confidence: **99.31%**
59. **`crates/wasmtime/src/runtime/values.rs`** -> AI Confidence: **99.31%**
60. **`crates/wasmtime/src/runtime/vm/component/handle_table.rs`** -> AI Confidence: **99.31%**
61. **`crates/wasmtime/src/runtime/vm/instance/allocator/pooling/decommit_queue.rs`** -> AI Confidence: **99.31%**
62. **`crates/wasmtime/src/runtime/vm/instance/allocator/pooling/memory_pool.rs`** -> AI Confidence: **99.31%**
63. **`crates/wasmtime/src/runtime/vm/memory.rs`** -> AI Confidence: **99.31%**
64. **`crates/wasmtime/src/runtime/vm/memory/shared_memory_disabled.rs`** -> AI Confidence: **99.31%**
65. **`crates/wasmtime/src/runtime/vm/provenance.rs`** -> AI Confidence: **99.31%**
66. **`crates/wasmtime/src/runtime/wave/component.rs`** -> AI Confidence: **99.31%**
67. **`crates/wast/src/core.rs`** -> AI Confidence: **99.31%**
68. **`crates/wiggle/generate/src/config.rs`** -> AI Confidence: **99.31%**
69. **`crates/wizer/src/component/parse.rs`** -> AI Confidence: **99.31%**
70. **`examples/min-platform/src/main.rs`** -> AI Confidence: **99.31%**
71. **`scripts/publish.rs`** -> AI Confidence: **99.31%**
72. **`src/commands/objdump.rs`** -> AI Confidence: **99.31%**
73. **`src/common.rs`** -> AI Confidence: **99.31%**
74. **`tests/all/cli_tests.rs`** -> AI Confidence: **99.31%**
75. **`tests/all/native_debug/lldb.rs`** -> AI Confidence: **99.31%**
76. **`tests/wasi.rs`** -> AI Confidence: **99.31%**
77. **`winch/codegen/src/codegen/bounds.rs`** -> AI Confidence: **99.31%**
78. **`winch/codegen/src/codegen/call.rs`** -> AI Confidence: **99.31%**
79. **`winch/codegen/src/codegen/mod.rs`** -> AI Confidence: **99.31%**
80. **`winch/codegen/src/isa/x64/masm.rs`** -> AI Confidence: **99.31%**
81. **`winch/codegen/src/stack.rs`** -> AI Confidence: **99.31%**
82. **`crates/c-api/include/wasmtime/extern.hh`** -> AI Confidence: **99.31%**
83. **`examples/async.cc`** -> AI Confidence: **99.31%**
84. **`cranelift/tests/filetests.rs`** -> AI Confidence: **99.29%**
85. **`cranelift/tests/logged-filetests.rs`** -> AI Confidence: **99.29%**
86. **`crates/test-programs/src/bin/p2_cli_large_env.rs`** -> AI Confidence: **99.29%**
87. **`benches/wasmtime-serve-rps.sh`** -> AI Confidence: **99.29%**
88. **`ci/docker/aarch64-linux/Dockerfile`** -> AI Confidence: **99.29%**
89. **`ci/docker/aarch64-musl/Dockerfile`** -> AI Confidence: **99.29%**
90. **`ci/docker/armv7-linux/Dockerfile`** -> AI Confidence: **99.29%**
91. **`ci/docker/riscv64gc-linux/Dockerfile`** -> AI Confidence: **99.29%**
92. **`ci/docker/s390x-linux/Dockerfile`** -> AI Confidence: **99.29%**
93. **`crates/c-api/include/wasmtime/conf.h.in`** -> AI Confidence: **99.29%**
94. **`cranelift/codegen/src/isa/riscv64/inst/vector.rs`** -> AI Confidence: **99.25%**
95. **`crates/component-macro/src/bindgen.rs`** -> AI Confidence: **99.25%**
96. **`crates/wasmtime/src/runtime/vm/stack_switching/stack/unix.rs`** -> AI Confidence: **99.25%**
97. **`crates/winch/src/builder.rs`** -> AI Confidence: **99.25%**
98. **`src/commands/run.rs`** -> AI Confidence: **99.25%**
99. **`cranelift/assembler-x64/meta/src/dsl/format.rs`** -> AI Confidence: **99.24%**
100. **`cranelift/codegen/meta/src/gen_asm.rs`** -> AI Confidence: **99.24%**
101. **`cranelift/codegen/meta/src/gen_inst.rs`** -> AI Confidence: **99.24%**
102. **`cranelift/codegen/src/alias_analysis.rs`** -> AI Confidence: **99.24%**
103. **`cranelift/codegen/src/egraph/elaborate.rs`** -> AI Confidence: **99.24%**
104. **`cranelift/codegen/src/ir/exception_table.rs`** -> AI Confidence: **99.24%**
105. **`cranelift/codegen/src/ir/extfunc.rs`** -> AI Confidence: **99.24%**
106. **`cranelift/codegen/src/isa/aarch64/inst/regs.rs`** -> AI Confidence: **99.24%**
107. **`cranelift/codegen/src/isa/call_conv.rs`** -> AI Confidence: **99.24%**
108. **`cranelift/codegen/src/isa/pulley_shared/inst/args.rs`** -> AI Confidence: **99.24%**
109. **`cranelift/codegen/src/isa/s390x/abi.rs`** -> AI Confidence: **99.24%**
110. **`cranelift/codegen/src/isa/x64/abi.rs`** -> AI Confidence: **99.24%**
111. **`cranelift/codegen/src/isa/x64/inst/regs.rs`** -> AI Confidence: **99.24%**
112. **`cranelift/codegen/src/machinst/compile.rs`** -> AI Confidence: **99.24%**
113. **`cranelift/codegen/src/machinst/reg.rs`** -> AI Confidence: **99.24%**
114. **`cranelift/codegen/src/machinst/vcode.rs`** -> AI Confidence: **99.24%**
115. **`cranelift/codegen/src/remove_constant_phis.rs`** -> AI Confidence: **99.24%**
116. **`cranelift/codegen/src/settings.rs`** -> AI Confidence: **99.24%**
117. **`cranelift/codegen/src/verifier/mod.rs`** -> AI Confidence: **99.24%**
118. **`cranelift/filetests/src/runner.rs`** -> AI Confidence: **99.24%**
119. **`cranelift/isle/isle/src/overlap.rs`** -> AI Confidence: **99.24%**
120. **`cranelift/isle/isle/src/sema.rs`** -> AI Confidence: **99.24%**
121. **`cranelift/isle/veri/veri_engine/src/annotations.rs`** -> AI Confidence: **99.24%**
122. **`cranelift/isle/veri/veri_engine/src/verify.rs`** -> AI Confidence: **99.24%**
123. **`cranelift/object/src/backend.rs`** -> AI Confidence: **99.24%**
124. **`cranelift/reader/src/isaspec.rs`** -> AI Confidence: **99.24%**
125. **`cranelift/reader/src/lexer.rs`** -> AI Confidence: **99.24%**
126. **`cranelift/reader/src/sourcemap.rs`** -> AI Confidence: **99.24%**
127. **`cranelift/src/run.rs`** -> AI Confidence: **99.24%**
128. **`cranelift/src/souper_harvest.rs`** -> AI Confidence: **99.24%**
129. **`crates/c-api/src/vec.rs`** -> AI Confidence: **99.24%**
130. **`crates/cache/src/lib.rs`** -> AI Confidence: **99.24%**
131. **`crates/cache/src/worker.rs`** -> AI Confidence: **99.24%**
132. **`crates/debugger/src/host/api.rs`** -> AI Confidence: **99.24%**
133. **`crates/environ/examples/factc.rs`** -> AI Confidence: **99.24%**
134. **`crates/environ/src/compile/module_environ.rs`** -> AI Confidence: **99.24%**
135. **`crates/environ/src/fact/signature.rs`** -> AI Confidence: **99.24%**
136. **`crates/environ/src/module_artifacts.rs`** -> AI Confidence: **99.24%**
137. **`crates/environ/src/string_pool.rs`** -> AI Confidence: **99.24%**
138. **`crates/environ/src/tunables.rs`** -> AI Confidence: **99.24%**
139. **`crates/environ/src/types.rs`** -> AI Confidence: **99.24%**
140. **`crates/fuzzing/src/generators/config.rs`** -> AI Confidence: **99.24%**
141. **`crates/fuzzing/src/generators/gc_ops/mutator.rs`** -> AI Confidence: **99.24%**
142. **`crates/fuzzing/src/oracles.rs`** -> AI Confidence: **99.24%**
143. **`crates/fuzzing/src/oracles/engine.rs`** -> AI Confidence: **99.24%**
144. **`crates/fuzzing/tests/oom/caller.rs`** -> AI Confidence: **99.24%**
145. **`crates/fuzzing/tests/oom/types.rs`** -> AI Confidence: **99.24%**
146. **`crates/gdbstub-component/src/lib.rs`** -> AI Confidence: **99.24%**
147. **`crates/jit-icache-coherence/src/libc.rs`** -> AI Confidence: **99.24%**
148. **`crates/misc/component-async-tests/tests/scenario/util.rs`** -> AI Confidence: **99.24%**
149. **`crates/test-programs/src/bin/p3_http_proxy.rs`** -> AI Confidence: **99.24%**
150. **`crates/test-programs/src/sockets.rs`** -> AI Confidence: **99.24%**
151. **`crates/test-util/src/wast.rs`** -> AI Confidence: **99.24%**
152. **`crates/unwinder/src/arch/mod.rs`** -> AI Confidence: **99.24%**
153. **`crates/wasi-common/src/snapshots/preview_1.rs`** -> AI Confidence: **99.24%**
154. **`crates/wasi-common/src/sync/dir.rs`** -> AI Confidence: **99.24%**
155. **`crates/wasi-common/src/sync/sched/windows.rs`** -> AI Confidence: **99.24%**
156. **`crates/wasi-http/src/field_map.rs`** -> AI Confidence: **99.24%**
157. **`crates/wasi-http/src/p2/types.rs`** -> AI Confidence: **99.24%**
158. **`crates/wasi-http/src/p2/types_impl.rs`** -> AI Confidence: **99.24%**
159. **`crates/wasi-io/src/impls.rs`** -> AI Confidence: **99.24%**
160. **`crates/wasi-io/src/lib.rs`** -> AI Confidence: **99.24%**
161. **`crates/wasi-keyvalue/src/lib.rs`** -> AI Confidence: **99.24%**
162. **`crates/wasi-nn/src/backend/onnx.rs`** -> AI Confidence: **99.24%**
163. **`crates/wasi-nn/src/backend/openvino.rs`** -> AI Confidence: **99.24%**
164. **`crates/wasi-nn/src/backend/pytorch.rs`** -> AI Confidence: **99.24%**
165. **`crates/wasi-threads/src/lib.rs`** -> AI Confidence: **99.24%**
166. **`crates/wasi/src/p1.rs`** -> AI Confidence: **99.24%**
167. **`crates/wasi/src/p2/host/filesystem.rs`** -> AI Confidence: **99.24%**
168. **`crates/wasi/src/p2/host/network.rs`** -> AI Confidence: **99.24%**
169. **`crates/wasi/src/p2/stdio.rs`** -> AI Confidence: **99.24%**
170. **`crates/wasi/src/p3/sockets/host/types/udp.rs`** -> AI Confidence: **99.24%**
171. **`crates/wasi/src/sockets/util.rs`** -> AI Confidence: **99.24%**
172. **`crates/wasmtime/src/compile.rs`** -> AI Confidence: **99.24%**
173. **`crates/wasmtime/src/engine/serialization.rs`** -> AI Confidence: **99.24%**
174. **`crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`** -> AI Confidence: **99.24%**
175. **`crates/wasmtime/src/runtime/component/matching.rs`** -> AI Confidence: **99.24%**
176. **`crates/wasmtime/src/runtime/coredump.rs`** -> AI Confidence: **99.24%**
177. **`crates/wasmtime/src/runtime/gc/disabled/arrayref.rs`** -> AI Confidence: **99.24%**
178. **`crates/wasmtime/src/runtime/gc/enabled/eqref.rs`** -> AI Confidence: **99.24%**
179. **`crates/wasmtime/src/runtime/linker.rs`** -> AI Confidence: **99.24%**
180. **`crates/wasmtime/src/runtime/module/registry.rs`** -> AI Confidence: **99.24%**
181. **`crates/wasmtime/src/runtime/type_registry.rs`** -> AI Confidence: **99.24%**
182. **`crates/wasmtime/src/runtime/vm/gc/enabled/structref.rs`** -> AI Confidence: **99.24%**
183. **`crates/wasmtime/tests/engine_across_forks.rs`** -> AI Confidence: **99.24%**
184. **`crates/wasmtime/tests/host_segfault.rs`** -> AI Confidence: **99.24%**
185. **`crates/wiggle/generate/src/names.rs`** -> AI Confidence: **99.24%**
186. **`examples/min-platform/embedding/src/lib.rs`** -> AI Confidence: **99.24%**
187. **`pulley/src/profile.rs`** -> AI Confidence: **99.24%**
188. **`pulley/tests/all/interp.rs`** -> AI Confidence: **99.24%**
189. **`src/commands/wast.rs`** -> AI Confidence: **99.24%**
190. **`src/commands/wizer.rs`** -> AI Confidence: **99.24%**
191. **`tests/all/guest_debug/mod.rs`** -> AI Confidence: **99.24%**
192. **`winch/codegen/src/codegen/context.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `ci/run-tests.py` -> **81.0806%** Exposure
- `benches/call.rs` -> **20.0%** Exposure
- `benches/compile_time_builtins.rs` -> **20.0%** Exposure
- `benches/instantiation.rs` -> **20.0%** Exposure
- `benches/trap.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `cranelift/bforest/src/set.rs` -> **100.0%** Exposure
- `crates/cranelift/src/func_environ.rs` -> **100.0%** Exposure
- `crates/environ/src/frame_table.rs` -> **100.0%** Exposure
- `crates/fiber/src/unix.rs` -> **100.0%** Exposure
- `crates/jit-icache-coherence/src/libc.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `crates/fuzzing/src/generators/single_inst_module.rs` -> **10.0%** Exposure
- `examples/multimemory.c` -> **10.0%** Exposure
- `crates/c-api/include/wasm.hh` -> **9.9998%** Exposure
- `examples/memory.c` -> **9.9989%** Exposure
- `examples/min-platform/embedding/wasmtime-platform.c` -> **9.5513%** Exposure
### Algorithmic DoS Exposure
- `benches/call.rs` -> **100.0%** Exposure
- `benches/compile_time_builtins.rs` -> **100.0%** Exposure
- `benches/trap.rs` -> **100.0%** Exposure
- `cranelift/assembler-x64/meta/src/generate.rs` -> **100.0%** Exposure
- `cranelift/assembler-x64/meta/src/generate/features.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20793` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/fiber/src/nostd.rs` (RUST) -> Cumulative Risk: **905.99**
- **Archetype:** `file_cluster_16` (Distance: 13.86 IQR)
- **Magnitude:** 165.54 | **LOC:** 204 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9522%)
- **Heaviest Functions:** `new` (Impact: 21.5), `new` (Impact: 20.4), `take_resume` (Impact: 10.4)

### 2. `crates/gdbstub-component/src/lib.rs` (RUST) -> Cumulative Risk: **886.29**
- **Archetype:** `file_cluster_4` (Distance: 13.072 IQR)
- **Magnitude:** 740.0 | **LOC:** 362 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9941%)
- **Heaviest Functions:** `run` (Impact: 396.9), `handle_event` (Impact: 132.9), `update_on_stop` (Impact: 20.9)

### 3. `crates/wasi-io/src/impls.rs` (RUST) -> Cumulative Risk: **879.82**
- **Archetype:** `file_cluster_4` (Distance: 13.965 IQR)
- **Magnitude:** 733.78 | **LOC:** 293 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9984%)
- **Heaviest Functions:** `poll` (Impact: 148.1), `blocking_write_and_flush` (Impact: 45.5), `splice` (Impact: 45.5)

### 4. `crates/wasmtime/src/runtime/component/store.rs` (RUST) -> Cumulative Risk: **875.19**
- **Archetype:** `file_cluster_4` (Distance: 13.72 IQR)
- **Magnitude:** 461.06 | **LOC:** 537 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `assert_instance_states_empty` (Impact: 30.9), `current_call_context_scope_id` (Impact: 21.1), `call_context` (Impact: 14.2)

### 5. `crates/wasi-tls/src/p2/io.rs` (RUST) -> Cumulative Risk: **858.33**
- **Archetype:** `file_cluster_4` (Distance: 13.443 IQR)
- **Magnitude:** 783.46 | **LOC:** 412 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `flush` (Impact: 85.6), `poll_read` (Impact: 65.1), `write` (Impact: 53.3)

### 6. `benches/instantiation.rs` (RUST) -> Cumulative Risk: **854.28**
- **Archetype:** `file_cluster_13` (Distance: 11.729 IQR)
- **Magnitude:** 243.36 | **LOC:** 231 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9727%), Concurrency (99.9343%), Algorithmic Dos (99.8795%)
- **Heaviest Functions:** `bench_parallel` (Impact: 88.9), `bench_sequential` (Impact: 32.2), `bench_deserialize_module` (Impact: 15.2)

### 7. `crates/misc/component-async-tests/src/util.rs` (RUST) -> Cumulative Risk: **839.67**
- **Archetype:** `file_cluster_4` (Distance: 13.535 IQR)
- **Magnitude:** 263.42 | **LOC:** 164 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9996%)
- **Heaviest Functions:** `poll_consume` (Impact: 94.4), `poll_produce` (Impact: 37.3), `poll_produce` (Impact: 20.2)

### 8. `crates/wasi/src/p2/host/io.rs` (RUST) -> Cumulative Risk: **834.84**
- **Archetype:** `file_cluster_4` (Distance: 13.017 IQR)
- **Magnitude:** 257.48 | **LOC:** 129 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `flush` (Impact: 14.2), `subscribe` (Impact: 12.3), `write` (Impact: 12.2)

### 9. `crates/wasi-tls/src/p3/host.rs` (RUST) -> Cumulative Risk: **834.36**
- **Archetype:** `file_cluster_4` (Distance: 14.409 IQR)
- **Magnitude:** 808.2 | **LOC:** 291 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `receive` (Impact: 225.5), `send` (Impact: 225.3), `connect` (Impact: 122.3)

### 10. `crates/wasi/src/p2/host/filesystem.rs` (RUST) -> Cumulative Risk: **820.67**
- **Archetype:** `file_cluster_4` (Distance: 12.719 IQR)
- **Magnitude:** 728.72 | **LOC:** 791 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `read_directory` (Impact: 93.9), `read` (Impact: 53.2), `set_times` (Impact: 37.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/wasmtime/src/runtime/vm/libcalls.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.482 IQR)
- **Top Global Matches:** file_cluster_4: 13.482, file_cluster_8: 13.512, file_cluster_0: 13.534
- **Magnitude:** 20694.84 | **LOC:** 1764 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (28.4971%), Tech Debt (10.8243%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 458`, `args: 127`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 270`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `concurrency: 121`, `import: 34`
* *Defense:* `safety: 131`, `doc: 124`, `test: 5`, `sync_locks: 3`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vm::const_expr::ConstEvalContext, packed_option::ReservedValue, Val, core::ptr::NonNull, InvalidWrite, ConstExprEvaluator, ArrayType, super::stack_switching::VMContObj...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.675 IQR)
- **Top Global Matches:** file_cluster_16: 14.675, file_cluster_4: 14.815, file_cluster_8: 14.855
- **Magnitude:** 11956.52 | **LOC:** 4944 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 72.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (42.1897%), Tech Debt (60.7732%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 3503.7 | O(2^N) | DB: 83)
  * `copy` (Impact: 1409.0 | O(2^N) | DB: 6)
  * `guest_read` (Impact: 1357.8 | O(2^N) | DB: 4)
  * `guest_write` (Impact: 1335.3 | O(2^N) | DB: 4)
  * `write` (Impact: 782.8 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 723`, `structural_boundaries: 912`, `args: 121`, `func_start: 151`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 500`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 21`, `orphaned_logic: 18`
* *Architecture:* `io: 6`, `api: 83`, `concurrency: 380`, `import: 38`
* *Defense:* `safety: 560`, `doc: 623`, `test: 19`, `sync_locks: 18`, `immutability_locks: 48`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GlobalErrorContextRefCount, core::marker::PhantomData, core::pin::pin, crate::Engine, crate::vm::component::ComponentInstance, core::future::pending, Poll, std::any::Any...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/interpreter/src/step.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.193 IQR)
- **Top Global Matches:** file_cluster_8: 12.193, file_cluster_17: 12.448, file_cluster_16: 12.482
- **Magnitude:** 5774.92 | **LOC:** 1656 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (34.676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validate_signature_params` (Impact: 5345.6 | O(2^N) | DB: 27)
    * *Intent:* /// Ensures that all types in args are the same as expected by the signature
  * `icmp` (Impact: 112.7 | O(N^5))
  * `fcmp` (Impact: 57.9 | O(N^2))
  * `extractlanes` (Impact: 41.8 | O(N^3) | DB: 2)
  * `vectorizelanes_all` (Impact: 21.9 | O(N^3) | DB: 1)
    * *Intent:* /// Jump to another block with the given parameters, e.g.: in /// `brif v0, block42(v1, v2), block97...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 284`, `args: 116`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 1`, `state_mutation: 85`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 107`, `doc: 35`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.841
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cranelift_codegen::ir::
    AbiParam, InstructionData, types, crate::value::DataValueExt, TrapCode, AtomicRmwOp, FuncRef, thiserror::Error...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/all/func.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.014 IQR)
- **Top Global Matches:** file_cluster_0: 15.014, file_cluster_11: 15.075, file_cluster_8: 15.357
- **Magnitude:** 4312.22 | **LOC:** 2356 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (36.8622%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrap_multiple_results` (Impact: 391.7 | O(N^6) | DB: 48)
  * `func_constructors` (Impact: 211.1 | O(N^2) | DB: 50)
  * `calls_with_funcref_and_externref` (Impact: 173.6 | O(N^5) | DB: 29)
  * `call_wasm_getting_subtype_func_return` (Impact: 128.8 | O(N^6) | DB: 17)
  * `get_from_wrapper` (Impact: 116.6 | O(N^3) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 483`, `structural_boundaries: 1007`, `args: 207`, `func_start: 62`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1427`, `dead_code: 1`
* *Architecture:* `api: 48`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 299`, `test: 272`, `sync_locks: 2`, `immutability_locks: 45`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::Arc, wasmtime::bail, wasmtime::*, Ordering::SeqCst, AtomicUsize, std::sync::atomic::AtomicBool, std::sync::atomic::Ordering, wasmtime_test_macros::wasmtime_test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/environ/src/fact/trampoline.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.908 IQR)
- **Top Global Matches:** file_cluster_8: 12.908, file_cluster_11: 12.991, file_cluster_6: 13.027
- **Magnitude:** 4234.72 | **LOC:** 4420 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (11.1746%), Tech Debt (67.5166%)
**Top Internal Functions/Classes:**
  * `validate_memory_inbounds` (Impact: 2870.1 | O(2^N) | DB: 77)
  * `compile` (Impact: 699.9 | O(N^6) | DB: 37)
  * `payload_src` (Impact: 38.0 | O(N^5))
  * `payload_dst` (Impact: 38.0 | O(N^5))
  * `string_to_compact` (Impact: 28.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 489`, `args: 121`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 6`, `state_mutation: 264`, `dead_code: 12`, `planned_debt: 105`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 180`, `doc: 198`, `test: 43`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TypeVariantIndex, TypeTupleIndex, MAX_FLAT_ASYNC_PARAMS, std::collections::HashMap, InterfaceType, HelperLocation, HelperType, wasm_encoder::BlockType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/func.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.152 IQR)
- **Top Global Matches:** file_cluster_4: 13.152, file_cluster_8: 13.222, file_cluster_0: 13.335
- **Magnitude:** 4135.84 | **LOC:** 4649 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (45.1893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `integers` (Impact: 425.1 | O(N^5) | DB: 70)
  * `drop_call_async_future` (Impact: 394.8 | O(N^6) | DB: 55)
  * `test_many_results` (Impact: 282.0 | O(N^6) | DB: 12)
  * `test_many_parameters` (Impact: 201.1 | O(N^6) | DB: 14)
  * `strings` (Impact: 157.7 | O(N^6) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 952`, `args: 127`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1091`, `fragile_debt: 4`
* *Architecture:* `api: 51`, `concurrency: 335`, `import: 6`
* *Defense:* `safety: 196`, `doc: 12`, `test: 206`, `sync_locks: 1`, `immutability_locks: 192`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::component::*, Engine, wasmtime::Config, Trap, std::sync::
    Arc, atomic::AtomicBool, StoreContextMut, Ordering::SeqCst...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasi/src/p1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.125 IQR)
- **Top Global Matches:** file_cluster_4: 15.125, file_cluster_0: 15.177, file_cluster_11: 15.323
- **Magnitude:** 3980.72 | **LOC:** 2719 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (28.9065%), Tech Debt (84.138%)
**Top Internal Functions/Classes:**
  * `poll_oneoff` (Impact: 1144.8 | O(2^N) | DB: 12)
  * `fd_write_impl` (Impact: 217.4 | O(N^6) | DB: 3)
  * `fd_read` (Impact: 209.6 | O(N^6) | DB: 7)
  * `new` (Impact: 151.4 | O(N^5) | DB: 5)
  * `fd_readdir` (Impact: 132.2 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 561`, `args: 107`, `func_start: 91`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 298`, `dead_code: 37`, `planned_debt: 9`, `duplicate_logic: 23`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 275`, `import: 7`
* *Defense:* `safety: 299`, `doc: 343`, `test: 5`, `sync_locks: 1`, `immutability_locks: 5`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clocks::monotonic_clock, crate::cli::WasiCliView, StreamResult, wasmtime_wasi_io::
    bindings::wasi::io::streams, streams::StreamError, streams::HostOutputStream, BTreeSet, WasiCtx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/reader/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.569 IQR)
- **Top Global Matches:** file_cluster_8: 13.569, file_cluster_13: 13.722, file_cluster_0: 13.723
- **Magnitude:** 3390.76 | **LOC:** 3719 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (26.6484%), Tech Debt (9.251%)
**Top Internal Functions/Classes:**
  * `parse_target_specs` (Impact: 2003.3 | O(N^6) | DB: 49)
  * `token` (Impact: 99.2 | O(2^N) | DB: 1)
    * *Intent:* /// Set a block as cold.
  * `optional_debug_tags` (Impact: 64.5 | O(N^6) | DB: 2)
  * `parse_literals_to_constant_data` (Impact: 63.7 | O(N^5) | DB: 2)
  * `parse_cmdline_target` (Impact: 56.7 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 481`, `args: 154`, `func_start: 122`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 291`, `duplicate_logic: 2`
* *Architecture:* `api: 28`, `import: 25`
* *Defense:* `safety: 273`, `doc: 83`, `test: 174`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CallConv, std::str::FromStr, InstructionFormat, Token, TestFile, std::mem, BlockArg, GlobalValueData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/isle/veri/veri_engine/src/type_inference.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.949 IQR)
- **Top Global Matches:** file_cluster_8: 11.949, file_cluster_0: 12.12, file_cluster_17: 12.248
- **Magnitude:** 3134.78 | **LOC:** 2453 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (11.8965%), Tech Debt (15.2636%)
**Top Internal Functions/Classes:**
  * `solve_constraints` (Impact: 1568.2 | O(2^N) | DB: 21)
  * `add_rule_constraints` (Impact: 812.0 | O(2^N) | DB: 10)
  * `type_annotations_using_rule` (Impact: 250.8 | O(N^6) | DB: 22)
  * `add_annotation_constraints` (Impact: 154.9 | O(2^N) | DB: 4)
  * `type_rules_with_term_and_types` (Impact: 73.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 407`, `args: 20`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 146`, `dead_code: 14`, `planned_debt: 5`, `fragile_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 218`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::termname::pattern_contains_termname, std::collections::HashMap, TypeContext, TypeEnv, Expr, std::hash::Hash, VarId, veri_ir::annotation_ir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/isle/isle/src/sema.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.682 IQR)
- **Top Global Matches:** file_cluster_8: 12.682, file_cluster_13: 12.752, file_cluster_16: 12.785
- **Magnitude:** 3059.68 | **LOC:** 2751 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (9.8835%), Tech Debt (34.3899%)
**Top Internal Functions/Classes:**
  * `from_ast` (Impact: 2354.6 | O(2^N) | DB: 39)
  * `visit` (Impact: 122.6 | O(2^N) | DB: 2)
  * `visit` (Impact: 95.5 | O(2^N) | DB: 2)
  * `constructor_sig` (Impact: 44.2 | O(N^6))
    * *Intent:* /// A term that defines an "extractor macro" in the LHS of a pattern. Its
  * `extractor_sig` (Impact: 37.8 | O(N^6))
    * *Intent:* /// Which variant of the enum: e.g. for enum type `A` if a term is /// `(A.A1 ...)` then the variant...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 327`, `args: 69`, `func_start: 48`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 124`, `dead_code: 6`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 81`, `import: 16`
* *Defense:* `safety: 189`, `doc: 289`, `test: 9`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ast, std::collections::BTreeSet, crate::stablemapset::StableMap, std::collections::BTreeMap, std::fmt, crate::ast::Ident, super::*, crate::log...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cranelift/codegen/src/isa/riscv64/inst/emit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.76 IQR)
- **Top Global Matches:** file_cluster_8: 11.76, file_cluster_17: 11.955, file_cluster_0: 12.094
- **Magnitude:** 2983.62 | **LOC:** 2888 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (22.5843%), Tech Debt (24.4521%)
**Top Internal Functions/Classes:**
  * `emit` (Impact: 2701.6 | O(2^N) | DB: 61)
  * `return_call_emit_impl` (Impact: 40.1 | O(N^4) | DB: 3)
  * `load_int_mask` (Impact: 22.0 | O(N^5) | DB: 1)
    * *Intent:* /// Load int mask. /// If ty is int then 0xff in rd.
  * `expected_vstate` (Impact: 8.9 | O(N^3) | DB: 4)
    * *Intent:* /// Returns Some(VState) if this instruction is expecting a specific vector state /// before emissio...
  * `frame_layout` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 205`, `args: 95`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 131`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 108`, `doc: 15`, `test: 4`, `sync_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::isa::riscv64::inst::*, CiOp, CiwOp, FpuOPWidth, crate::isa::riscv64::lower::isle::generated_code::
    CaOp, ClOp, CsznOp, crate::ir::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/visitor.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.78 IQR)
- **Top Global Matches:** file_cluster_8: 14.78, file_cluster_11: 14.797, file_cluster_13: 14.853
- **Magnitude:** 2892.08 | **LOC:** 4688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (77.7281%), Tech Debt (7.6977%)
**Top Internal Functions/Classes:**
  * `visit_call_indirect` (Impact: 33.5 | O(N^3) | DB: 3)
  * `visit_select` (Impact: 28.9 | O(N^3) | DB: 1)
  * `visit_table_init` (Impact: 24.8 | O(N^3) | DB: 3)
  * `visit_table_copy` (Impact: 24.8 | O(N^3) | DB: 3)
  * `visit_global_set` (Impact: 21.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 758`, `args: 762`, `func_start: 493`
* *Risk/State:* `state_mutation: 1111`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 249`, `import: 51`
* *Defense:* `safety: 308`, `doc: 11`, `sync_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WasmValType, VectorCompareKind, FnCall, V128MaxKind, V128AddKind, ValType, bail, ShiftKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pulley/src/interp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.607 IQR)
- **Top Global Matches:** file_cluster_16: 13.607, file_cluster_0: 13.668, file_cluster_8: 13.741
- **Magnitude:** 2878.32 | **LOC:** 5631 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (32.4282%), Tech Debt (99.7459%)
**Top Internal Functions/Classes:**
  * `push_frame_save` (Impact: 44.4 | O(N^5) | DB: 2)
  * `new` (Impact: 38.2 | O(2^N) | DB: 4)
  * `addr` (Impact: 31.1 | O(2^N) | DB: 2)
    * *Intent:* /// Returns a pointer to the base of the stack (the lowest address). /// /// Note that the returned ...
  * `addr` (Impact: 30.9 | O(2^N) | DB: 2)
  * `addr` (Impact: 24.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 1652`, `args: 652`, `func_start: 590`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1250`, `dead_code: 2`, `planned_debt: 6`, `duplicate_logic: 28`, `orphaned_logic: 177`
* *Architecture:* `api: 30`, `import: 20`
* *Defense:* `safety: 76`, `doc: 227`, `test: 14`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::ptr::NonNull, crate::profile::ExecutingPc, core::ops::ControlFlow, TrapKind, crate::decode::*, crate::encode::Encode, wasmtime_core::alloc::TryVec, alloc::string::ToString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/isle/isle/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.927 IQR)
- **Top Global Matches:** file_cluster_8: 13.927, file_cluster_17: 14.1, file_cluster_16: 14.139
- **Magnitude:** 2871.44 | **LOC:** 983 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (49.985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_spec_expr` (Impact: 506.9 | O(2^N) | DB: 3)
  * `parse_pattern` (Impact: 434.4 | O(2^N) | DB: 3)
  * `parse_model_type` (Impact: 162.6 | O(N^6) | DB: 1)
  * `parse_model` (Impact: 156.8 | O(N^6) | DB: 4)
  * `parse_spec` (Impact: 142.4 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 254`, `args: 79`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 186`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 247`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lexer::Lexer, Token, Pos, crate::error::Error, crate::ast::*, Span
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/func/typed.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.613 IQR)
- **Top Global Matches:** file_cluster_16: 14.613, file_cluster_0: 14.656, file_cluster_11: 14.715
- **Magnitude:** 2852.88 | **LOC:** 3185 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (13.8264%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `lower_args` (Impact: 457.6 | O(2^N) | DB: 14)
    * *Intent:* /// Unlike [`Self::call`] and [`Self::call_async`] (both of which require /// exclusive access to th...
  * `linear_lower_to_memory` (Impact: 112.7 | O(2^N) | DB: 1)
  * `linear_lower_to_flat` (Impact: 95.8 | O(2^N) | DB: 2)
  * `typecheck_variant` (Impact: 85.5 | O(N^6))
    * *Intent:* /// Get access to the raw underlying memory for this list. /// /// This method will return a direct ...
  * `typecheck` (Impact: 84.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 456`, `args: 134`, `func_start: 113`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 222`, `dead_code: 13`, `planned_debt: 12`, `fragile_debt: 7`, `duplicate_logic: 69`, `orphaned_logic: 9`
* *Architecture:* `api: 26`, `concurrency: 60`, `import: 25`
* *Defense:* `safety: 359`, `doc: 551`, `test: 54`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::ptr::NonNull, core::hash::Hash, InterfaceType, core::str, StringEncoding, crate::component::matching::InstanceType, crate::component::storage::storage_as_slice, MaybeUninit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/values.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.252 IQR)
- **Top Global Matches:** file_cluster_8: 13.252, file_cluster_16: 13.26, file_cluster_13: 13.427
- **Magnitude:** 2676.0 | **LOC:** 1299 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (21.8431%), Tech Debt (99.5601%)
**Top Internal Functions/Classes:**
  * `lift` (Impact: 589.3 | O(2^N) | DB: 4)
  * `load` (Impact: 496.4 | O(2^N) | DB: 9)
  * `store` (Impact: 415.5 | O(2^N) | DB: 6)
  * `lower` (Impact: 364.2 | O(2^N) | DB: 3)
  * `store` (Impact: 95.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 208`, `args: 67`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 4`, `state_mutation: 100`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 8`, `duplicate_logic: 18`, `orphaned_logic: 2`
* *Architecture:* `api: 10`, `concurrency: 40`, `import: 9`
* *Defense:* `safety: 200`, `doc: 67`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::slice::Iter, InterfaceType, TypeEnum, wasmtime_component_util::DiscriminantSize, desc, TypeOption, IterMut, TypeMapIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cranelift/src/func_environ.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.245 IQR)
- **Top Global Matches:** file_cluster_8: 13.245, file_cluster_0: 13.346, file_cluster_13: 13.361
- **Magnitude:** 2660.86 | **LOC:** 4333 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 180
- **Risk Profile:** Cognitive Load (20.6433%), Tech Debt (17.7886%)
**Top Internal Functions/Classes:**
  * `fuel_before_op` (Impact: 821.6 | O(N^6) | DB: 106)
    * *Intent:* /// A `GlobalValue` in CLIF which represents the stack limit.
  * `translate_ref_is_null` (Impact: 740.4 | O(N^6) | DB: 180)
  * `translate_table_set` (Impact: 48.9 | O(N^6) | DB: 2)
  * `translate_table_fill` (Impact: 35.8 | O(N^5) | DB: 11)
    * *Intent:* // Then append the regular call arguments.
  * `translate_array_init_data` (Impact: 17.4 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 879`, `args: 166`, `func_start: 169`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 554`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 16`
* *Architecture:* `api: 137`, `import: 24`
* *Defense:* `safety: 155`, `doc: 156`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WasmValType, WasmCompositeInnerType, ComponentPC, DataIndex, EngineOrModuleTypeIndex, std::mem, cranelift_codegen::ir::
    self, BlockArg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasi-common/src/snapshots/preview_1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.6 IQR)
- **Top Global Matches:** file_cluster_4: 13.6, file_cluster_8: 13.956, file_cluster_17: 14.027
- **Magnitude:** 2619.04 | **LOC:** 1571 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (99.7334%), Tech Debt (54.7579%)
**Top Internal Functions/Classes:**
  * `fd_readdir` (Impact: 1102.2 | O(N^6) | DB: 41)
  * `fd_allocate` (Impact: 348.1 | O(N^4) | DB: 20)
  * `fd_pread` (Impact: 154.2 | O(N^5) | DB: 7)
    * *Intent:* // If the first iov structure is from shared memory we can safely assume // all the rest will be. We...
  * `fd_pwrite` (Impact: 67.7 | O(N^4) | DB: 2)
  * `fd_write` (Impact: 62.7 | O(N^4) | DB: 2)
    * *Intent:* // If the first iov structure is from shared memory we can safely assume // all the rest will be. We...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 325`, `args: 83`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 208`, `planned_debt: 1`, `orphaned_logic: 19`
* *Architecture:* `io: 3`, `api: 4`, `concurrency: 369`, `import: 11`
* *Defense:* `safety: 160`, `test: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wiggle::GuestMemory, FileAccessMode, ErrorExt, sched::
        Poll, RoFlags, I32Exit, subscription::RwEventFlags, SubscriptionResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/run.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.087 IQR)
- **Top Global Matches:** file_cluster_0: 14.087, file_cluster_13: 14.296, file_cluster_4: 14.299
- **Magnitude:** 2615.32 | **LOC:** 1615 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (37.4775%), Tech Debt (16.7517%)
**Top Internal Functions/Classes:**
  * `setup_guest_profiler` (Impact: 1381.8 | O(N^6) | DB: 36)
  * `debugger_run` (Impact: 225.2 | O(2^N) | DB: 11)
    * *Intent:* /// Split off a sub-command representing the invocation of a /// debugger component side-car to this...
  * `instantiate_and_run` (Impact: 218.1 | O(N^6) | DB: 4)
    * *Intent:* /// Executes the `main` after instantiating it within `store`. /// /// This applies all configuratio...
  * `execute` (Impact: 165.7 | O(N^6) | DB: 13)
    * *Intent:* /// Executes the command.
  * `setup_epoch_handler` (Impact: 81.8 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 251`, `args: 60`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 195`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 21`, `concurrency: 77`, `import: 23`
* *Defense:* `safety: 244`, `doc: 71`, `test: 1`, `sync_locks: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PathBuf, Val, clap::Parser, wasmtime_wasi_config::WasiConfig, WasiKeyValueCtx, WasiCtxBuilder, RunCommon, ambient_authority...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/resources.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.702 IQR)
- **Top Global Matches:** file_cluster_0: 13.702, file_cluster_4: 13.712, file_cluster_8: 13.754
- **Magnitude:** 2559.16 | **LOC:** 1806 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 202
- **Risk Profile:** Cognitive Load (47.0172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `manually_destroy` (Impact: 1226.5 | O(N^6) | DB: 202)
  * `resource_any` (Impact: 150.9 | O(N^5) | DB: 33)
  * `drop_in_different_places` (Impact: 81.4 | O(N^6) | DB: 12)
  * `drop_guest_twice` (Impact: 38.2 | O(N^5) | DB: 7)
  * `mismatch_resource_types` (Impact: 33.0 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 705`, `args: 66`, `func_start: 30`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 825`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 67`, `import: 4`
* *Defense:* `safety: 112`, `test: 125`, `immutability_locks: 15`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wasmtime::component::*, Engine, wasmtime::Config, Trap, wasmtime::Result, Store
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/isa/x64/masm.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.805 IQR)
- **Top Global Matches:** file_cluster_8: 13.805, file_cluster_11: 14.116, file_cluster_16: 14.134
- **Magnitude:** 2530.04 | **LOC:** 3598 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (29.8221%), Tech Debt (73.5477%)
**Top Internal Functions/Classes:**
  * `atomic_rmw` (Impact: 758.1 | O(N^6) | DB: 42)
  * `popcnt` (Impact: 171.5 | O(2^N) | DB: 2)
  * `wasm_load` (Impact: 136.1 | O(N^6) | DB: 1)
  * `mul_wide` (Impact: 72.2 | O(N^6) | DB: 2)
  * `branch` (Impact: 69.2 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 218`, `args: 122`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 229`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 39`
* *Architecture:* `import: 9`
* *Defense:* `safety: 294`, `doc: 22`, `test: 4`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WasmValType, VectorCompareKind, FloatScratch, Imm, V128MaxKind, args::CC, V128AddKind, WritableReg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/codegen/src/ir/immediates.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.827 IQR)
- **Top Global Matches:** file_cluster_16: 11.827, file_cluster_8: 12.111, file_cluster_0: 12.238
- **Magnitude:** 2505.8 | **LOC:** 1962 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (6.3176%), Tech Debt (35.4344%)
**Top Internal Functions/Classes:**
  * `parse_u64` (Impact: 2310.4 | O(2^N) | DB: 11)
  * `fmt` (Impact: 28.2 | O(2^N) | DB: 1)
  * `write_hex` (Impact: 10.8 | O(N^2) | DB: 2)
  * `fcvt_to_sint_negative_overflow_ieee128` (Impact: 8.1 | O(N^3))
  * `fcvt_to_sint_negative_overflow_ieee64` (Impact: 7.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 156`, `args: 96`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`, `dead_code: 2`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 100`, `doc: 120`, `test: 164`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mul, f64, Display, libm::Libm, alloc::string::ToString, u32, super::*, core::str::FromStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/linker.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 19.198 IQR)
- **Top Global Matches:** file_cluster_4: 19.198, file_cluster_11: 19.268, file_cluster_0: 19.334
- **Magnitude:** 2455.2 | **LOC:** 1531 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (48.0922%), Tech Debt (19.8498%)
**Top Internal Functions/Classes:**
  * `module` (Impact: 1795.1 | O(2^N) | DB: 32)
    * *Intent:* /// Asynchronous analog of [`Linker::func_wrap`]. #[cfg(feature = "async")]
  * `instance` (Impact: 74.7 | O(2^N) | DB: 5)
    * *Intent:* /// Define a host function within this linker. /// /// For information about how the host function o...
  * `define_unknown_imports_as_default_values` (Impact: 64.1 | O(N^6) | DB: 4)
  * `define_unknown_imports_as_traps` (Impact: 31.1 | O(N^6) | DB: 1)
    * *Intent:* /// By default a [`Linker`] will disallow duplicate definitions of the same /// signature. This meth...
  * `func_new_async` (Impact: 16.9 | O(N^3) | DB: 3)
    * *Intent:* /// Same as [`Linker::define`], except only the name of the import is /// provided, not a module nam...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 213`, `args: 59`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 146`, `dead_code: 48`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 40`, `concurrency: 148`, `import: 14`
* *Defense:* `safety: 144`, `doc: 663`, `test: 2`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Val, PanicOnOom, StringPool, crate::instance::InstancePre, prelude::*, IntoFunc, AsContextMut, core::future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/debugger/src/host/api.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.088 IQR)
- **Top Global Matches:** file_cluster_4: 15.088, file_cluster_16: 15.536, file_cluster_11: 15.682
- **Magnitude:** 2411.88 | **LOC:** 1056 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (63.888%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 41.2 | O(N^5) | DB: 2)
  * `all_instances` (Impact: 40.6 | O(2^N) | DB: 2)
  * `all_modules` (Impact: 35.1 | O(2^N) | DB: 2)
  * `exit_frames` (Impact: 35.1 | O(2^N) | DB: 2)
  * `make` (Impact: 35.0 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 346`, `args: 103`, `func_start: 97`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 254`, `planned_debt: 1`, `duplicate_logic: 35`, `orphaned_logic: 47`
* *Architecture:* `api: 10`, `concurrency: 669`, `import: 10`
* *Defense:* `safety: 258`, `doc: 33`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::DebugRunResult, Val, wasmtime_wasi::p2::DynPollable, component::Resource, wasmtime::
    Engine, Tag, crate::host::wit, std::sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cranelift/src/func_environ/gc/enabled.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.424 IQR)
- **Top Global Matches:** file_cluster_8: 12.424, file_cluster_16: 12.526, file_cluster_13: 12.555
- **Magnitude:** 2405.8 | **LOC:** 1698 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (16.7941%), Tech Debt (12.2242%)
**Top Internal Functions/Classes:**
  * `translate_exn_unbox` (Impact: 1813.8 | O(2^N) | DB: 67)
  * `read_field_at_addr` (Impact: 87.4 | O(N^6) | DB: 3)
    * *Intent:* /// Read a struct field or array element from its raw address in the GC heap. /// /// The given addr...
  * `translate_struct_get` (Impact: 81.7 | O(2^N) | DB: 2)
  * `translate_struct_set` (Impact: 81.6 | O(2^N) | DB: 2)
  * `write_field_at_addr` (Impact: 41.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 297`, `args: 48`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 154`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 71`, `doc: 62`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StructFieldsVec, WasmCompositeInnerType, cranelift_codegen::ir::immediates::Offset32, WasmValType, cranelift_entity::packed_option::ReservedValue, wasmtime_environ::
    Collector, crate::Reachability, WasmResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `winch/codegen/src/stack.rs` (RUST) | Magnitude: 425.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 292, doc: 92, args: 59, api: 53
- `crates/wasmtime/src/runtime/vm/sys/custom/vm.rs` (RUST) | Magnitude: 93.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, api: 25, structural_boundaries: 22, safety: 21
- `cranelift/assembler-x64/src/rex.rs` (RUST) | Magnitude: 87.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 76, indent_spaces: 49, safety: 14, api: 11
- `cranelift/isle/isle/isle_examples/link/multi_extractor_main.rs` (RUST) | Magnitude: 61.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 30, state_mutation: 25, branch: 9
- `cranelift/codegen/src/ir/known_symbol.rs` (RUST) | Magnitude: 19.34 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 10, safety: 10, decorators: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/wasmtime/src/runtime/gc/enabled/rooting.rs` (RUST) | Magnitude: 560.32 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 1053, indent_spaces: 577, structural_boundaries: 187, generics: 171
- `crates/wasi-http/src/p2/mod.rs` (RUST) | Magnitude: 112.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 435, indent_spaces: 169, structural_boundaries: 83, sec_dead_code: 46
- `crates/wasmtime/src/runtime/func.rs` (RUST) | Magnitude: 906.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 1295, indent_spaces: 670, structural_boundaries: 211, generics: 183
- `crates/fuzzing/src/oracles/diff_v8.rs` (RUST) | Magnitude: 278.68 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 145, state_mutation: 136, safety: 32
- `crates/wasmtime/src/runtime/vm/provenance.rs` (RUST) | Magnitude: 15.2 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 128, generics: 33, structural_boundaries: 21, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cranelift/entity/src/sparse.rs` (RUST) | Magnitude: 77.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 159, doc: 75, test: 71, structural_boundaries: 56
- `crates/wasi-nn/src/wit.rs` (RUST) | Magnitude: 528.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 249, structural_boundaries: 86, safety: 83, branch: 55
- `crates/wasmtime/src/runtime/module/registry.rs` (RUST) | Magnitude: 402.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 247, doc: 93, structural_boundaries: 75, safety: 57
- `crates/wasi-http/src/p2/types.rs` (RUST) | Magnitude: 287.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 169, safety: 52, api: 52, structural_boundaries: 50
- `crates/fuzzing/tests/oom/instance_pre.rs` (RUST) | Magnitude: 84.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 18, state_mutation: 15, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/wasmtime/src/compile.rs` (RUST) | Magnitude: 1385.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 837, structural_boundaries: 206, branch: 138, state_mutation: 129
- `crates/wasmtime/src/runtime/vm/module_id.rs` (RUST) | Magnitude: 8.82 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, doc: 5, structural_boundaries: 3, api: 3
- `crates/unwinder/src/stackwalk.rs` (RUST) | Magnitude: 56.86 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 128, indent_spaces: 72, pointers: 14, structural_boundaries: 13
- `cranelift/entity/src/list.rs` (RUST) | Magnitude: 454.04 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 538, structural_boundaries: 181, doc: 136, test: 131
- `fuzz/fuzz_targets/cranelift-icache.rs` (RUST) | Magnitude: 73.6 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 53, branch: 32, safety: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/test-programs/src/bin/nn_wit_image_classification_pytorch.rs` (RUST) | Magnitude: 21.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, scientific: 6, branch: 5
- `crates/test-programs/src/bin/nn_witx_image_classification_pytorch.rs` (RUST) | Magnitude: 21.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, scientific: 6, branch: 5
- `crates/wasi-nn/src/backend/onnx.rs` (RUST) | Magnitude: 608.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 346, structural_boundaries: 110, safety: 98, branch: 92
- `crates/wasi/src/p3/filesystem/mod.rs` (RUST) | Magnitude: 225.32 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, doc: 51, branch: 47, structural_boundaries: 33
- `examples/async.cc` (CPP) | Magnitude: 39.82 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 24, sec_high_risk_execution: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/wasmtime/src/runtime/vm/sys/unix/signals.rs` (RUST) | Magnitude: 129.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, doc: 44, state_mutation: 39, structural_boundaries: 35
- `crates/wasmtime/src/runtime/component/resources/host.rs` (RUST) | Magnitude: 313.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, doc: 40, concurrency: 36, structural_boundaries: 35
- `crates/wiggle/generate/src/module_trait.rs` (RUST) | Magnitude: 121.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 26, safety: 17, branch: 14
- `crates/wasi/src/p3/clocks/host.rs` (RUST) | Magnitude: 71.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 20, safety: 12, state_mutation: 9
- `crates/wasi/src/sockets/mod.rs` (RUST) | Magnitude: 119.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, doc: 53, structural_boundaries: 30, concurrency: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `cranelift/codegen/src/cursor.rs` (RUST) | Magnitude: 208.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 306, indent_spaces: 161, state_mutation: 69, structural_boundaries: 58
- `crates/wasi-preview1-component-adapter/provider/src/lib.rs` (RUST) | Magnitude: 17.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 40, sec_dead_code: 5, api: 4, immutability_locks: 4
- `crates/wasi/src/p2/bindings.rs` (RUST) | Magnitude: 13.04 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 405, dead_code: 80, structural_boundaries: 2, api: 2
- `cranelift/codegen/src/take_and_replace.rs` (RUST) | Magnitude: 17.24 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 52, indent_spaces: 11, structural_boundaries: 9, state_mutation: 8
- `crates/c-api/src/lib.rs` (RUST) | Magnitude: 11.04 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 26, planned_debt: 2, high_risk_execution: 1, panics_and_aborts: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/c-api/include/wasmtime/config.hh` (CPP) | Magnitude: 181.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 173, indent_spaces: 165, structural_boundaries: 70, state_mutation: 42
- `crates/c-api/include/wasmtime/val.h` (CPP) | Magnitude: 17.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 129, pointers: 39, indent_spaces: 39, structural_boundaries: 38
- `winch/codegen/src/isa/aarch64/regs.rs` (RUST) | Magnitude: 51.76 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 91, indent_spaces: 40, immutability_locks: 21, args: 19
- `cranelift/codegen/src/isa/x64/inst/stack_switch.rs` (RUST) | Magnitude: 11.12 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, indent_spaces: 9, api: 6, encapsulation: 6
- `cranelift/codegen/src/ir/user_stack_maps.rs` (RUST) | Magnitude: 8.6 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 111, indent_spaces: 35, structural_boundaries: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `benches/trap.rs` (RUST) | Magnitude: 244.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 84, state_mutation: 73, safety_bypasses: 21
- `crates/cranelift/src/lib.rs` (RUST) | Magnitude: 38.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 75, indent_spaces: 31, safety: 6, branch: 5
- `crates/wasi/src/cli/mem.rs` (RUST) | Magnitude: 20.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, safety: 8, args: 6
- `cranelift/codegen/src/egraph/cost.rs` (RUST) | Magnitude: 80.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, doc: 36, args: 22, structural_boundaries: 18
- `cranelift/interpreter/src/value.rs` (RUST) | Magnitude: 873.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 741, pointers: 140, func_start: 138, safety: 137

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/wasmtime/src/runtime/component/concurrent.rs` -> Churn: **100.0%** | Cog Load: 41.6241% | Debt: 66.7035%
- `crates/core/src/alloc/vec.rs` -> Churn: **94.16%** | Cog Load: 31.1163% | Debt: 78.5409%
- `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` -> Churn: **94.16%** | Cog Load: 42.1897% | Debt: 60.7732%
- `crates/wasmtime/src/runtime/debug.rs` -> Churn: **94.16%** | Cog Load: 10.65% | Debt: 86.1962%
- `crates/environ/src/collections.rs` -> Churn: **81.31%** | Cog Load: 2.3713% | Debt: 93.5379%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/wasmtime/src/runtime/vm/libcalls.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 20694.84
- `crates/wasi/src/p1.rs` -> **Alex Crichton** (100.0% isolated ownership) | Magnitude: 3980.72
- `cranelift/reader/src/parser.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 3390.76
- `cranelift/isle/isle/src/sema.rs` -> **Michael McLoughlin** (100.0% isolated ownership) | Magnitude: 3059.68
- `winch/codegen/src/visitor.rs` -> **r-near** (100.0% isolated ownership) | Magnitude: 2892.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/wasi/src/cli/stdout.rs` -> **Severity: 488.448** (Blast Radius: 4.896 * Doc Risk: 99.7647%)
- `crates/c-api/include/wasm.h` -> **Severity: 339.245** (Blast Radius: 18.973 * Doc Risk: 17.8804%)
- `cranelift/codegen/src/isa/riscv64/inst/vector.rs` -> **Severity: 315.8** (Blast Radius: 3.158 * Doc Risk: 100.0%)
- `cranelift/assembler-x64/src/vex.rs` -> **Severity: 312.419** (Blast Radius: 5.3 * Doc Risk: 58.9469%)
- `crates/core/src/error/ptr.rs` -> **Severity: 297.6** (Blast Radius: 2.976 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
