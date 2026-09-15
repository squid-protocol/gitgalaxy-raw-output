# ARCHITECTURAL_BRIEF: wasmtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bytecodealliance/wasmtime.git` |
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
| Total Artifacts | 6447 |
| Analyzed Artifacts (Scanned) | 2057 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4390 |
| Total LOC | 480307 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 31.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6725 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3102 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5553 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1763 | 464760 | 85.7% |
| CPP | 142 | 11958 | 6.9% |
| MARKDOWN | 73 | 0 | 3.5% |
| C | 29 | 2358 | 1.4% |
| SHELL | 17 | 491 | 0.8% |
| PLAINTEXT | 10 | 0 | 0.5% |
| DOCKERFILE | 8 | 58 | 0.4% |
| JAVASCRIPT | 5 | 564 | 0.2% |
| MAKEFILE | 2 | 36 | 0.1% |
| BINARY_THREAT | 2 | 2 | 0.1% |
| PYTHON | 1 | 14 | 0.0% |
| XML | 1 | 0 | 0.0% |
| JSON | 1 | 3 | 0.0% |
| YAML | 1 | 6 | 0.0% |
| CSS | 1 | 40 | 0.0% |
| M4 | 1 | 17 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.13; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 25%, State Mutators Files 16%, Generic / Templated Code Files 10%, Data / Markup / Trivial 9%, Tests & Verification Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1972 | 95.9% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 83 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4390*

**Composition by Extension & Reason:**
- `.wat`: 2249x Excluded (Unsupported Extension: '.wat'), 3x Unsupported Format (.wat)
- `.clif`: 1192x Excluded (Unsupported Extension: '.clif')
- `.wast`: 222x Excluded (Unsupported Extension: '.wast')
- `.rs`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Machine-Generated Source Code Signature: 205 LOC), 5x Excluded (Machine-Generated Source Code Signature: 243 LOC)
- `.isle`: 115x Unsupported Format (.isle)
- `.toml`: 102x Unsupported Format (.toml), 5x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wit`: 72x Excluded (Unsupported Extension: '.wit'), 25x Unsupported Format (.wit)
- `.md`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `no_extension`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.witx`: 23x Excluded (Unsupported Extension: '.witx')
- `.yml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1066 LOC)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 7x Excluded (Unsupported Extension: '.lock')
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.2 | 5.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 42.2 | 51.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 29.4 | 11.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.2 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.8 | 6.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 64.1 | 84.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 34303 | 1648 | 44 | `pulley/src/interp.rs` |
| cleanup | 686 | 220 | 1 | `crates/wasi/src/p1.rs` |
| guards | 10800 | 1194 | 13 | `tests/all/component_model/func.rs` |
| danger | 14258 | 1163 | 19 | `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` |
| concurrency | 8936 | 582 | 10 | `tests/all/component_model/async.rs` |
| connectivity | 19400 | 1397 | 25 | `winch/codegen/src/visitor.rs` |
| io | 991 | 276 | 1 | `tests/all/cli_tests.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 61 | 44 | 0 | `crates/wasi-http/tests/all/p3/mod.rs` |
| time | 93 | 56 | 0 | `crates/wasi-http/src/p2/types.rs` |
| serialization | 25 | 11 | 0 | `crates/cli-flags/src/lib.rs` |
| regex | 13 | 10 | 0 | `ci/print-current-version.sh` |
| events | 1268 | 220 | 1 | `crates/wasmtime/src/runtime/component/concurrent.rs` |
| tests | 15722 | 981 | 17 | `tests/all/cli_tests.rs` |
| docs | 69934 | 1159 | 88 | `crates/wasmtime/src/config.rs` |
| debt | 3132 | 736 | 4 | `crates/environ/src/fact/trampoline.rs` |
| mutation | 64861 | 1626 | 76 | `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` |
| dead_code | 10369 | 1290 | 12 | `pulley/src/interp.rs` |
| credential | 1 | 1 | 0 | `ci/build-release-artifacts.sh` |
| threat | 907 | 350 | 1 | `crates/c-api/include/wasmtime/component/types/val.h` |
| ml_ai | 1458 | 156 | 0 | `crates/fuzzing/src/generators/single_inst_module.rs` |
| ui | 5 | 2 | 0 | `crates/explorer/src/index.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1818**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/all/cli_tests.rs` (Hits: 50)
- `crates/wasi/src/p2/host/network.rs` (Hits: 42)
- `src/commands/serve.rs` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wasm.h** (`crates/c-api/include/wasm.h`) — 47 inbound connections
2. **conf.h.in** (`crates/c-api/include/wasmtime/conf.h.in`) — 37 inbound connections
3. **rex.rs** (`cranelift/assembler-x64/src/rex.rs`) — 33 inbound connections
4. **wasmtime.hh** (`crates/c-api/include/wasmtime.hh`) — 31 inbound connections
5. **vex.rs** (`cranelift/assembler-x64/src/vex.rs`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **concurrent.rs** (`crates/wasmtime/src/runtime/component/concurrent.rs`) — 114 outbound dependencies
2. **masm.rs** (`winch/codegen/src/isa/aarch64/masm.rs`) — 96 outbound dependencies
3. **masm.rs** (`winch/codegen/src/isa/x64/masm.rs`) — 96 outbound dependencies
4. **futures_and_streams.rs** (`crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs`) — 92 outbound dependencies
5. **vm.rs** (`crates/wasmtime/src/runtime/vm.rs`) — 90 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `step` **(Many-Argument Workhorses)** (@ `cranelift/interpreter/src/step.rs`) -> Impact: **818.8** | LOC: 1204
  * *Intent:* /// Interpret a single Cranelift instruction. Note that program traps and interpreter errors are /// distinct: a program trap results in `Ok(Flow::Tra...
- `parse_inst_operands` **(Many-Argument Workhorses)** (@ `cranelift/reader/src/parser.rs`) -> Impact: **365.5** | LOC: 422
  * *Intent:* // Parse the operands following the instruction opcode. // This depends on the format of the opcode.
- `try_emit_compressed` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/riscv64/inst/emit.rs`) -> Impact: **344.3** | LOC: 566
  * *Intent:* /// Tries to emit an instruction as compressed, if we can't return false.
- `translate_operator` **(Many-Argument Workhorses)** (@ `crates/cranelift/src/translate/code_translator.rs`) -> Impact: **333.2** | LOC: 1325
  * *Intent:* /// Translates wasm operators into Cranelift IR instructions.
- `emit` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/aarch64/inst/emit.rs`) -> Impact: **287.3** | LOC: 1274
- `emit_with_alloc_consumer` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/s390x/inst/emit.rs`) -> Impact: **254.9** | LOC: 1163
- `generate` **(Many-Argument Workhorses)** (@ `crates/fuzzing/src/generators/component_async.rs`) -> Impact: **253.8** | LOC: 694
- `emit` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/x64/inst/emit.rs`) -> Impact: **248.7** | LOC: 1575
  * *Intent:* /// and sil. /// /// For all instructions, also add a test that uses only low-half registers /// (rax .. rdi, xmm0 .. xmm7) etc, so as to check that a...
- `emit_block_contents` **(Many-Argument Workhorses)** (@ `cranelift/isle/isle/src/codegen.rs`) -> Impact: **236.9** | LOC: 240
- `translate_payload` **(Many-Argument Workhorses)** (@ `crates/environ/src/component/translate.rs`) -> Impact: **220.8** | LOC: 697

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/all` | 56 | 8671.58 | 7.09% | 0.0% |
| `crates/wasmtime/src/runtime` | 31 | 6926.8 | 7.39% | 38.89% |
| `crates/wasmtime/src/runtime/component` | 15 | 5505.12 | 10.29% | 42.04% |
| `crates/test-programs/src/bin` | 264 | 4718.16 | 12.26% | 34.92% |
| `crates/wasmtime/src/runtime/vm` | 31 | 4679.94 | 8.69% | 50.95% |
| `cranelift/codegen/src` | 31 | 4150.42 | 9.52% | 29.06% |
| `cranelift/codegen/src/machinst` | 12 | 4073.2 | 7.94% | 46.11% |
| `pulley/src` | 11 | 4049.1 | 7.3% | 43.63% |
| `cranelift/isle/isle/src` | 17 | 3956.2 | 13.16% | 29.08% |
| `tests/all/component_model` | 16 | 3792.92 | 7.58% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cranelift/codegen/src/ir/builder.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/ir/entities.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/ir/sourceloc.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/isa/riscv64/lower/isle.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/isa/s390x/lower/isle.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cranelift/codegen/meta/src/pulley.rs` -> **100.0%** Exposure
- `cranelift/codegen/meta/src/shared/immediates.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/opts/div_const.rs` -> **100.0%** Exposure
- `crates/environ/src/component/names.rs` -> **100.0%** Exposure
- `crates/environ/src/component/translate.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pulley/src/interp.rs` -> **523** Orphaned Functions | **3** Duplicates
- `cranelift/isle/veri/veri_engine/tests/veri.rs` -> **197** Orphaned Functions | **0** Duplicates
- `winch/codegen/src/isa/x64/asm.rs` -> **166** Orphaned Functions | **0** Duplicates
- `winch/codegen/src/masm.rs` -> **139** Orphaned Functions | **6** Duplicates
- `cranelift/codegen/src/isle_prelude.rs` -> **136** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20993` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/gdbstub-component/src/lib.rs` (RUST) -> Cumulative Risk: **750.17**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.12)
- **Magnitude:** 197.36 | **LOC:** 362 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9863%), State Flux (96.2224%)
- **Heaviest Functions:** `run` (Compute Cores, Impact: 40.2), `handle_event` (Many-Argument Workhorses, Impact: 28.2), `update_on_stop` (Defensive Guards, Impact: 6.6)

### 2. `crates/debugger/src/host/api.rs` (RUST) -> Cumulative Risk: **727.22**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.03)
- **Magnitude:** 1189.14 | **LOC:** 1056 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.7839%), Documentation (97.0%)
- **Heaviest Functions:** `make` (Generic / Templated Code, Impact: 16.4), `get_memory` (Generic / Templated Code, Impact: 14.1), `get_global` (Generic / Templated Code, Impact: 14.1)

### 3. `crates/wasi-tls/src/p2/io.rs` (RUST) -> Cumulative Risk: **708.74**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.32)
- **Magnitude:** 340.16 | **LOC:** 412 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (92.9042%)
- **Heaviest Functions:** `poll_read` (Many-Argument Workhorses, Impact: 18.5), `poll_write` (Many-Argument Workhorses, Impact: 14.3), `write` (Compute Cores, Impact: 11.7)

### 4. `crates/wit-bindgen/src/types.rs` (RUST) -> Cumulative Risk: **699.7**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.09)
- **Magnitude:** 135.38 | **LOC:** 203 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.437%), Concurrency (95.019%), Api Exposure (85.7261%)
- **Heaviest Functions:** `type_info_func` (Many-Argument Workhorses, Impact: 26.5), `type_id_info` (Many-Argument Workhorses, Impact: 14.6), `analyze` (Many-Argument Workhorses, Impact: 13.7)

### 5. `crates/core/src/error/error.rs` (RUST) -> Cumulative Risk: **682.37**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.86)
- **Magnitude:** 488.14 | **LOC:** 2025 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.3945%), Concurrency (98.7519%), Verification (80.0%)
- **Heaviest Functions:** `fmt` (Defensive Guards, Impact: 25.8), `fmt` (Defensive Guards, Impact: 11.1), `error_ext_chain_mut` (Defensive Guards, Impact: 8.2)

### 6. `crates/wasi/src/p2/host/filesystem/sync.rs` (RUST) -> Cumulative Risk: **673.0**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.34)
- **Magnitude:** 265.24 | **LOC:** 518 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8861%), Concurrency (99.7448%)
- **Heaviest Functions:** `from` (Compute Cores, Impact: 11.0), `from` (Compute Cores, Impact: 11.0), `from` (Compute Cores, Impact: 7.9)

### 7. `crates/wasi/src/p2/host/filesystem.rs` (RUST) -> Cumulative Risk: **671.56**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.60)
- **Magnitude:** 583.54 | **LOC:** 791 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.0332%), State Flux (84.9913%)
- **Heaviest Functions:** `read_directory` (Compute Cores, Impact: 29.1), `link_at` (Many-Argument Workhorses, Impact: 16.7), `set_times_at` (Many-Argument Workhorses, Impact: 16.6)

### 8. `crates/wasi/src/p2/filesystem.rs` (RUST) -> Cumulative Risk: **670.7**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.39)
- **Magnitude:** 255.7 | **LOC:** 421 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (93.2678%), Documentation (87.5%)
- **Heaviest Functions:** `blocking_write` (Many-Argument Workhorses, Impact: 21.8), `blocking_write_and_flush` (Compute Cores, Impact: 12.0), `read` (Compute Cores, Impact: 10.2)

### 9. `crates/wiggle/generate/src/funcs.rs` (RUST) -> Cumulative Risk: **654.61**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.50)
- **Magnitude:** 231.04 | **LOC:** 435 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9572%), Safety Score (93.2571%)
- **Heaviest Functions:** `emit` (Many-Argument Workhorses, Impact: 66.0), `_define_func` (Many-Argument Workhorses, Impact: 27.6), `finish_block` (Defensive Guards, Impact: 7.6)

### 10. `crates/wasmtime/src/runtime/store.rs` (RUST) -> Cumulative Risk: **653.24**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.33)
- **Magnitude:** 1018.3 | **LOC:** 3152 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.2567%), Api Exposure (91.7739%), Churn (87.25%)
- **Heaviest Functions:** `wasm_fault` (Many-Argument Workhorses, Impact: 26.8), `trace_wasm_stack_frame` (Many-Argument Workhorses, Impact: 18.3), `allocate_instance` (Many-Argument Workhorses, Impact: 17.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pulley/src/interp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2682.1 | **LOC:** 5631 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (8.734%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `push_frame_save` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `call_start` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /// Performs the initial part of [`Vm::call`] in setting up the `args` /// provided in registers acc...
  * `call_end` **(Generic / Templated Code)** (Impact: 11.6)
    * *Intent:* /// Performs the tail end of [`Vm::call`] by returning the values as /// determined by `rets` accord...
  * `xrem32_s` **(Defensive Guards)** (Impact: 9.5)
  * `xrem64_s` **(Defensive Guards)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 118 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 1748`, `args: 738`, `func_start: 649`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 10`, `state_mutation: 156`, `dead_code: 2`, `planned_debt: 6`, `duplicate_logic: 3`, `unreferenced_by_name: 523`
* *Architecture:* `api: 54`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 24`, `doc: 227`, `test: 15`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExecutingPcRef, IndexMut, Interpreter, MachineState, TrapKind, alloc::string::ToString, core::fmt, core::mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/concurrent.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2590.72 | **LOC:** 5493 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 76.9%
- **Risk Profile:** Cognitive Load (18.5201%), Tech Debt (25.0501%)
**Top Internal Functions/Classes:**
  * `queue_call` **(Many-Argument Workhorses)** (Impact: 138.9)
    * *Intent:* /// Add the specified guest call to the "high priority" work item queue, to /// be started as soon a...
  * `start_call` **(Many-Argument Workhorses)** (Impact: 134.3)
    * *Intent:* /// Start a guest->guest call previously prepared using /// `Self::prepare_call`. /// /// This is ca...
  * `prepare_call` **(Many-Argument Workhorses)** (Impact: 121.1)
    * *Intent:* /// Prepare (but do not start) a guest->guest call. /// /// This is called from fused adapter code g...
  * `subtask_cancel` **(Many-Argument Workhorses)** (Impact: 112.3)
    * *Intent:* /// Implements the `subtask.cancel` intrinsic.
  * `handle_callback_code` **(Many-Argument Workhorses)** (Impact: 72.2)
    * *Intent:* /// Handle the `CallbackCode` returned from an async-lifted export or its /// callback. /// /// If t...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 64 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 931`, `args: 245`, `func_start: 182`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 7`, `state_mutation: 72`, `dead_code: 17`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 25`
* *Architecture:* `api: 85`, `concurrency: 138`, `import: 41`
* *Defense:* `safety: 87`, `doc: 790`, `test: 30`, `immutability_locks: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsContextMut, BTreeSet, CanonicalOptions, CanonicalOptionsDataModel, ComponentInstance, DirectDestination, DirectSource, ErrorContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2542.5 | **LOC:** 4944 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 72.7%
- **Risk Profile:** Cognitive Load (20.199%), Tech Debt (69.8014%)
**Top Internal Functions/Classes:**
  * `copy` **(Many-Argument Workhorses)** (Impact: 191.0)
    * *Intent:* /// Copy `count` items from `read_address` to `write_address` for the /// specified stream or future...
  * `guest_read` **(Many-Argument Workhorses)** (Impact: 169.4)
    * *Intent:* /// Read from the specified stream or future from the guest.
  * `guest_write` **(Many-Argument Workhorses)** (Impact: 167.0)
    * *Intent:* /// Write to the specified stream or future from the guest.
  * `set_consumer` **(Many-Argument Workhorses)** (Impact: 101.6)
  * `new_transmit` **(Many-Argument Workhorses)** (Impact: 101.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 196
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 911`, `args: 250`, `func_start: 168`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 63`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 18`, `unreferenced_by_name: 31`
* *Architecture:* `io: 6`, `api: 97`, `concurrency: 146`, `import: 37`
* *Defense:* `safety: 73`, `doc: 623`, `test: 20`, `sync_locks: 10`, `immutability_locks: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsContextMut, ComponentInstanceId, ComponentType, ComponentTypes, DerefMut, FutureAny, GlobalErrorContextRefCount, HandleTable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wit-bindgen/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2300.82 | **LOC:** 3556 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (26.5034%), Tech Debt (9.4955%)
**Top Internal Functions/Classes:**
  * `generate_guest_import_closure` **(Many-Argument Workhorses)** (Impact: 113.4)
  * `generate_trait` **(Many-Argument Workhorses)** (Impact: 97.4)
  * `export` **(Many-Argument Workhorses)** (Impact: 75.0)
  * `define_rust_guest_export` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `world_add_to_linker` **(Many-Argument Workhorses)** (Impact: 64.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 238 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 112
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 811
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 416`, `structural_boundaries: 687`, `args: 165`, `func_start: 109`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 13`, `state_mutation: 335`, `dead_code: 4`, `planned_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 72`, `concurrency: 47`, `import: 22`
* *Defense:* `safety: 48`, `doc: 164`, `test: 7`, `immutability_locks: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BTreeSet, FunctionFilter, FunctionFlags, HashMap, HashSet, IndexSet, Stdio, TypeMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/visitor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2210.56 | **LOC:** 4688 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.9103%), Tech Debt (7.6749%)
**Top Internal Functions/Classes:**
  * `visit_br_table` **(Compute Cores)** (Impact: 41.2)
  * `visit_br_if` **(Compute Cores)** (Impact: 36.1)
  * `visit_call_indirect` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `visit_table_set` **(Compute Cores)** (Impact: 17.3)
  * `visit_memory_copy` **(Many-Argument Workhorses)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 873`, `args: 759`, `func_start: 511`
* *Risk/State:* `state_mutation: 36`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 508`, `import: 62`
* *Defense:* `safety: 2`, `doc: 11`, `sync_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BrTable, CodeGen, CodeGenError, ConditionalBranch, ControlStackFrame, DivKind, DivKind::*, Emission...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/reader/src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1824.5 | **LOC:** 3719 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.6167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_inst_operands` **(Many-Argument Workhorses)** (Impact: 365.5)
    * *Intent:* // Parse the operands following the instruction opcode. // This depends on the format of the opcode.
  * `parse_instruction` **(Many-Argument Workhorses)** (Impact: 98.7)
    * *Intent:* // Parse an instruction, append it to `block`. // // instruction ::= [inst-results "="] Opcode(opc) ...
  * `infer_typevar` **(Many-Argument Workhorses)** (Impact: 43.1)
    * *Intent:* // Type inference for polymorphic instructions. // // The controlling type variable can be specified...
  * `parse_exception_table` **(Compute Cores)** (Impact: 43.0)
    * *Intent:* // Parse an exception-table decl. // // exception-table ::= * SigRef(sig) "," BlockCall "," "[" (exc...
  * `parse_basic_block` **(Compute Cores)** (Impact: 37.9)
    * *Intent:* // Parse a basic block, add contents to `ctx`. // // extended-basic-block ::= * block-header { instr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 641`, `structural_boundaries: 656`, `args: 186`, `func_start: 142`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 3`, `state_mutation: 79`
* *Architecture:* `api: 37`, `import: 26`
* *Defense:* `safety: 63`, `doc: 83`, `test: 178`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ArgumentExtension, ArgumentPurpose, Block, BlockArg, CallConv, Constant, ConstantData, Details...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasi/src/p1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1515.34 | **LOC:** 2719 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.1373%), Tech Debt (9.1962%)
**Top Internal Functions/Classes:**
  * `poll_oneoff` **(Many-Argument Workhorses)** (Impact: 164.5)
  * `fd_read` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* /// Read from a file descriptor. /// NOTE: This is similar to `readv` in POSIX.
  * `fd_write_impl` **(Many-Argument Workhorses)** (Impact: 55.8)
    * *Intent:* /// Shared implementation of `fd_write` and `fd_pwrite`.
  * `fd_readdir` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `path_open` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* /// Open a file or directory. /// NOTE: This is similar to `openat` in POSIX.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 569`, `args: 141`, `func_start: 99`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `dead_code: 37`, `planned_debt: 9`
* *Architecture:* `io: 1`, `api: 28`, `concurrency: 77`, `import: 26`
* *Defense:* `safety: 32`, `doc: 343`, `test: 5`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, Config, Engine, GuestMemory, GuestPtr, GuestType, HashSet, IsATTY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1479.44 | **LOC:** 13968 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.9367%), Tech Debt (7.6365%)
**Top Internal Functions/Classes:**
  * `test_s390x_binemit` **(I/O & Config Routines)** (Impact: 2.5)
  * `simm20_zero` **(Tests & Verification)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 338`, `state_mutation: 1198`, `unreferenced_by_name: 1`
* *Architecture:* `import: 4`
* *Defense:* `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TrapCode, crate::ir::MemFlags, crate::isa::s390x::inst::*, crate::isa::s390x::settings, crate::settings::Configurable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cranelift/src/func_environ.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1420.28 | **LOC:** 4333 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.707%), Tech Debt (91.7294%)
**Top Internal Functions/Classes:**
  * `check_indirect_call_type_signature` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `make_table` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `translate_global_get` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `translate_global_set` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `translate_memory_size` **(Many-Argument Workhorses)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 1022`, `args: 242`, `func_start: 213`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 14`, `state_mutation: 43`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 109`
* *Architecture:* `api: 163`, `import: 23`
* *Defense:* `safety: 32`, `doc: 156`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BlockArg, ComponentPC, ConstantData, DataIndex, DefinedFuncIndex, ElemIndex, Endianness, EngineOrModuleTypeIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/isa/x64/masm.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1309.84 | **LOC:** 3598 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4012%), Tech Debt (94.4594%)
**Top Internal Functions/Classes:**
  * `v128_shift` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `wasm_load` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `splat` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `atomic_rmw` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `popcnt` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 336`, `args: 243`, `func_start: 148`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 99`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 13`, `doc: 22`, `test: 8`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CodeGenError, Emission, Extend, ExtendKind, ExtractLaneKind, FloatCmpKind, FloatScratch, FuncEnv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/component_model/func.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1288.34 | **LOC:** 4649 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (8.3393%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `integers` **(Compute Cores)** (Impact: 93.6)
  * `test_many_results` **(Many-Argument Workhorses)** (Impact: 92.3)
  * `test_many_parameters` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `option` **(Tests & Verification)** (Impact: 42.6)
  * `some_traps` **(I/O & Config Routines)** (Impact: 41.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 13
* *Concurrency (weighted view):* 151
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 1151`, `args: 144`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 32`, `state_mutation: 19`, `fragile_debt: 4`
* *Architecture:* `api: 64`, `concurrency: 141`, `import: 5`
* *Defense:* `safety: 8`, `doc: 12`, `test: 267`, `sync_locks: 1`, `immutability_locks: 228`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Engine, Ordering::SeqCst, REALLOC_AND_FREE, Store, StoreContextMut, Trap, atomic::AtomicBool, std::sync::
    Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/environ/src/fact/trampoline.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1253.84 | **LOC:** 4420 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (4.066%), Tech Debt (30.977%)
**Top Internal Functions/Classes:**
  * `translate_map` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* /// Translates a map from one component's memory to another. /// /// In the Component Model, a `map<...
  * `convert_variant` **(Many-Argument Workhorses)** (Impact: 48.8)
  * `compile_sync_to_sync_adapter` **(Many-Argument Workhorses)** (Impact: 45.7)
    * *Intent:* /// Compile an adapter function supporting a sync-lowered import to a /// sync-lifted export. /// //...
  * `translate` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `begin_translate_sequence` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* /// Shared preamble for translating list-like sequences (lists and maps). /// /// Emits: load ptr/le...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 92
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 538`, `args: 180`, `func_start: 128`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 97`, `state_mutation: 33`, `dead_code: 12`, `planned_debt: 105`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `concurrency: 10`, `import: 12`
* *Defense:* `safety: 28`, `doc: 198`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body, ComponentTypesBuilder, Encode, FLAG_MAY_LEAVE, FixedEncoding, FlagsSize, FlatType, Function...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/debugger/src/host/api.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1189.14 | **LOC:** 1056 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.8804%), Tech Debt (99.7839%)
**Top Internal Functions/Classes:**
  * `make` **(Generic / Templated Code)** (Impact: 16.4)
  * `get_memory` **(Generic / Templated Code)** (Impact: 14.1)
  * `get_global` **(Generic / Templated Code)** (Impact: 14.1)
  * `get_table` **(Generic / Templated Code)** (Impact: 14.1)
  * `get_func` **(Generic / Templated Code)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 320
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 345`, `args: 100`, `func_start: 97`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 44`, `planned_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `api: 11`, `concurrency: 150`, `import: 9`
* *Defense:* `safety: 20`, `doc: 33`, `sync_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExnRef, FrameHandle, Func, Global, Instance, Memory, Module, Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `winch/codegen/src/isa/x64/asm.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1128.4 | **LOC:** 2817 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4693%), Tech Debt (99.9879%)
**Top Internal Functions/Classes:**
  * `div` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* /// Signed/unsigned division. /// /// Emits a sequence of instructions to ensure the correctness of ...
  * `cmp_ir` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `rem` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* /// Signed/unsigned remainder. /// /// Emits a sequence of instructions to ensure the correctness of...
  * `movzx_mr` **(Many-Argument Workhorses)** (Impact: 11.5)
    * *Intent:* /// Zero-extend memory-to-register load.
  * `cmov` **(Many-Argument Workhorses)** (Impact: 11.5)
    * *Intent:* /// Integer register conditional move.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 599`, `args: 293`, `func_start: 202`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 130`, `planned_debt: 12`, `unreferenced_by_name: 166`
* *Architecture:* `api: 183`, `import: 18`
* *Defense:* `safety: 2`, `doc: 277`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Amode, CC, EmitInfo, EmitState, ExtMode, Extend, ExtendKind, ExtendType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/isle/veri/veri_engine/src/type_inference.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1120.52 | **LOC:** 2453 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.0077%), Tech Debt (15.6463%)
**Top Internal Functions/Classes:**
  * `add_rule_constraints` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `solve_constraints` **(Many-Argument Workhorses)** (Impact: 113.8)
    * *Intent:* // // t4 = bv // t1 = bv // t7 = bv // // would result in: // bv16 -> t2, t6, t1 // bv8 -> t3, t5, t...
  * `add_annotation_constraints` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `type_annotations_using_rule` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `create_parse_tree_pattern` **(Many-Argument Workhorses)** (Impact: 45.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 82 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 427`, `args: 20`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 363`, `dead_code: 14`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 23`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConcreteTest, Expr, FLAGS_WIDTH, HashSet, REG_WIDTH, TermEnv, TermId, TermSignature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/types.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1116.52 | **LOC:** 3654 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.5276%), Tech Debt (97.3942%)
**Top Internal Functions/Classes:**
  * `with_finality_and_supertype` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* /// Create a new function type with the given finality, supertype, parameter /// types, and result t...
  * `fmt` **(Compute Cores)** (Impact: 21.7)
  * `with_finality_and_supertype` **(Many-Argument Workhorses)** (Impact: 18.5)
    * *Intent:* /// fields. /// /// The result will be associated with the given engine, and attempts to use /// it ...
  * `validate` **(Defensive Guards)** (Impact: 16.2)
  * `_new` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 247`, `args: 309`, `func_start: 244`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 3`, `state_mutation: 15`, `dead_code: 9`, `planned_debt: 10`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 264`, `import: 12`
* *Defense:* `safety: 23`, `doc: 1016`, `test: 26`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Display, EntityType, Extern, Func, Global, HeapType::*, IndexType, Limits...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/interpreter/src/step.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1108.44 | **LOC:** 1656 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.617%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` **(Many-Argument Workhorses)** (Impact: 818.8)
    * *Intent:* /// Interpret a single Cranelift instruction. Note that program traps and interpreter errors are ///...
  * `fcmp` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* /// Compare two values using the given floating point condition `code`.
  * `icmp` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /// Compare two values using the given integer condition `code`.
  * `extractlanes` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* /// Converts a SIMD vector value into a Rust array of [Value] for processing. /// If `x` is a scalar...
  * `binary_arith` **(Generic / Templated Code)** (Impact: 12.2)
    * *Intent:* /// Performs the supplied binary arithmetic `op` on two values, either vector or scalar.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 27
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 315`, `args: 99`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 40`, `state_mutation: 25`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 13`, `doc: 35`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000486
  * `Imports (Out-Degree: 0):` AddressSize, AtomicRmwOp, Block, BlockArg, BlockCall, Endianness, ExternalName, FuncRef...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/wasi-common/src/snapshots/preview_1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1053.7 | **LOC:** 1571 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8026%), Tech Debt (94.3596%)
**Top Internal Functions/Classes:**
  * `poll_oneoff` **(Many-Argument Workhorses)** (Impact: 111.1)
  * `fd_pread` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `fd_read` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `sock_recv` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `path_open` **(Many-Argument Workhorses)** (Impact: 43.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 89
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 407`, `args: 102`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 25`, `planned_debt: 1`, `unreferenced_by_name: 47`
* *Architecture:* `io: 3`, `api: 4`, `concurrency: 84`, `import: 11`
* *Defense:* `safety: 17`, `test: 3`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorExt, FdFlags, FdStat, FileAccessMode, FileEntry, FileType, Filestat, I32Exit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/cli_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1028.72 | **LOC:** 3329 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (7.264%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `preview2_stdin` **(Tests & Verification)** (Impact: 27.1)
  * `cli_serve_sleep` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `cli_serve_hello_world` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `spawn` **(Compute Cores)** (Impact: 21.5)
  * `config_cli_flag` **(I/O & Config Routines)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 490`, `args: 192`, `func_start: 151`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 112`, `high_risk_execution: 4`, `state_mutation: 10`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 128`
* *Architecture:* `io: 50`, `api: 3`, `concurrency: 126`, `import: 19`
* *Defense:* `safety: 6`, `doc: 9`, `test: 337`, `immutability_locks: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufRead, BufReader, Command, ExitStatus, JoinHandle, Output, Read, Stdio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/store.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1018.3 | **LOC:** 3152 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (17.7464%), Tech Debt (43.1747%)
**Top Internal Functions/Classes:**
  * `wasm_fault` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /// Translates a WebAssembly fault at the native `pc` and native `addr` to a /// WebAssembly-relativ...
  * `trace_wasm_stack_frame` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `allocate_instance` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* /// from this store's own configuration. The `kind` provided is used to /// distinguish between "rea...
  * `try_new` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* /// Like `Store::new` but returns an error on allocation failure.
  * `allocate_gc_store` **(Generic / Templated Code)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 159
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 535`, `args: 199`, `func_start: 184`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 49`, `dead_code: 22`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 7`
* *Architecture:* `api: 154`, `concurrency: 99`, `import: 39`
* *Defense:* `safety: 14`, `doc: 823`, `test: 56`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DebugHandler, DefinedTableIndex, DerefMut, EntityRef, ExportMemory, FrameDataCache, GcStore, Imports...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/wasmtime/src/runtime/component/func/typed.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1015.66 | **LOC:** 3185 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (7.3199%), Tech Debt (75.8657%)
**Top Internal Functions/Classes:**
  * `lower_string` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `lift_try_map` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `lower_map_iter` **(Generic / Templated Code)** (Impact: 23.9)
  * `prepare_call` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /// Calls `concurrent::prepare_call` with monomorphized functions for /// lowering the parameters an...
  * `typecheck_variant` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* /// Verify that the given wasm type is a variant with the expected cases in the right order and with...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 483`, `args: 156`, `func_start: 127`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 43`, `dead_code: 13`, `planned_debt: 12`, `fragile_debt: 7`, `duplicate_logic: 8`, `unreferenced_by_name: 14`
* *Architecture:* `api: 33`, `concurrency: 25`, `import: 22`
* *Defense:* `safety: 20`, `doc: 551`, `test: 57`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsAccessor, ComponentTypes, InterfaceType, LiftContext, LowerContext, MAX_FLAT_PARAMS, MAX_FLAT_RESULTS, MaybeUninit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/codegen/src/verifier/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1008.06 | **LOC:** 2313 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.3306%), Tech Debt (18.7184%)
**Top Internal Functions/Classes:**
  * `verify_entity_references` **(Many-Argument Workhorses)** (Impact: 117.3)
  * `typecheck_variable_args` **(Many-Argument Workhorses)** (Impact: 40.5)
    * *Intent:* /// Typecheck both instructions that contain variable arguments like calls, and those that /// inclu...
  * `block_call_arg_ty` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `verify_global_values` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* // Check for: // - cycles in the global value declarations. // - use of 'vmctx' when no special para...
  * `verify_inst_arg` **(Many-Argument Workhorses)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 383`, `args: 99`, `func_start: 78`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 11`, `state_mutation: 19`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 20`, `import: 24`
* *Defense:* `safety: 19`, `doc: 113`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArgumentExtension, Block, BlockArg, Constant, ControlFlowGraph, Display, DynamicStackSlot, ExceptionTable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/test-util/src/component_fuzz.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 975.14 | **LOC:** 1919 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.678%), Tech Debt (11.6202%)
**Top Internal Functions/Classes:**
  * `make_import_and_export` **(Many-Argument Workhorses)** (Impact: 81.5)
    * *Intent:* /// Generates the internals of a core wasm module which imports a single /// component function `IMP...
  * `load_flat_helper` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /// Same as `store_flat_helper` but for loading the flat representation.
  * `generate` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `rust_type` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* /// Generate a [`TokenStream`] containing the rust type name for a type. /// /// The `name_counter` ...
  * `store_flat` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /// Generates text format wasm into `s` to store a value of this type, in /// its flat representatio...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 98 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 349`, `args: 105`, `func_start: 44`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 13`, `state_mutation: 154`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 35`, `concurrency: 18`, `import: 11`
* *Defense:* `safety: 19`, `doc: 79`, `test: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Debug, FlagsSize, Hasher, REALLOC_AND_FREE, TokenStream, Unstructured, Write, arbitrary::Arbitrary...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cranelift/codegen/src/opts/div_const.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 972.74 | **LOC:** 1215 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.1911%), Tech Debt (17.7846%)
**Top Internal Functions/Classes:**
  * `test_magic_generators_give_correct_numbers` **(Compute Cores)** (Impact: 77.2)
  * `test_magic_generators_dont_panic` **(Compute Cores)** (Impact: 37.4)
  * `test_magic_s32_inner` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* // Compute the magic numbers for `d` and then use them to compute and // check `n / d` for around 10...
  * `test_magic_s64_inner` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* // Compute the magic numbers for `d` and then use them to compute and // check `n / d` for around 10...
  * `magic_u32` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* // The actual "magic number" generators follow.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 224`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `state_mutation: 151`, `dead_code: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `doc: 17`, `test: 172`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MS64, MU32, MU64, magic_s64, magic_u32, magic_u64, proptest::strategy::Strategy, super::MS32...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/all/func.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 962.02 | **LOC:** 2356 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.6679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func_constructors` **(Compute Cores)** (Impact: 84.9)
  * `wrap_multiple_results` **(Tests & Verification)** (Impact: 77.5)
  * `calls_with_funcref_and_externref` **(Compute Cores)** (Impact: 41.3)
  * `get_from_wrapper` **(Tests & Verification)** (Impact: 37.8)
  * `typed_v128_imports` **(Compute Cores)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 1021`, `args: 211`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 6`, `state_mutation: 32`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 49`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 1`, `test: 277`, `sync_locks: 2`, `immutability_locks: 42`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicUsize, Ordering::SeqCst, std::sync::Arc, std::sync::atomic::AtomicBool, std::sync::atomic::Ordering, wasmtime::*, wasmtime::bail, wasmtime_test_macros::wasmtime_test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/cranelift/src/func_environ.rs` -> Churn: **97.19%** | Cog Load: 4.707% | Debt: 91.7294%
- `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` -> Churn: **94.16%** | Cog Load: 20.199% | Debt: 69.8014%
- `crates/environ/src/collections.rs` -> Churn: **81.31%** | Cog Load: 0.0% | Debt: 62.2459%
- `crates/wasmtime/src/runtime/component/func/typed.rs` -> Churn: **78.79%** | Cog Load: 7.3199% | Debt: 75.8657%
- `crates/environ/src/gc.rs` -> Churn: **73.74%** | Cog Load: 4.2464% | Debt: 76.3095%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `winch/codegen/src/visitor.rs` -> **r-near** (100.0% isolated ownership) | Magnitude: 2210.56
- `cranelift/reader/src/parser.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 1824.5
- `crates/wasi/src/p1.rs` -> **Alex Crichton** (100.0% isolated ownership) | Magnitude: 1515.34
- `crates/debugger/src/host/api.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 1189.14
- `crates/wasmtime/src/runtime/types.rs` -> **Nick Fitzgerald** (100.0% isolated ownership) | Magnitude: 1116.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/c-api/include/wasmtime/val.hh` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 97.9069%)
- `crates/c-api/include/wasmtime/extern.hh` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `crates/c-api/include/wasmtime/func.hh` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 53.6726%)
- `crates/c-api/include/wasmtime/component/val.hh` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `crates/c-api/include/wasmtime/config.hh` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 16.5448%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/c-api/include/wasm.h` -> **Severity: 1.919** (Embedded: 0.0309 * Error Risk: 62.1628%)
- `crates/c-api/include/wasmtime/store.h` -> **Severity: 1.863** (Embedded: 0.0218 * Error Risk: 85.6108%)
- `crates/c-api/include/wasi.h` -> **Severity: 1.405** (Embedded: 0.0185 * Error Risk: 75.8792%)
- `crates/c-api/include/wasmtime/module.h` -> **Severity: 1.147** (Embedded: 0.0174 * Error Risk: 65.7332%)
- `crates/c-api/include/wasmtime/store.hh` -> **Severity: 1.121** (Embedded: 0.0169 * Error Risk: 66.2319%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/c-api/include/wasm.h` -> **Severity: 1740.095** (Blast Radius: 18.097 * Doc Risk: 96.1538%)
- `crates/wasi/src/cli/stdout.rs` -> **Severity: 441.1** (Blast Radius: 4.411 * Doc Risk: 100.0%)
- `cranelift/codegen/meta/src/cdsl/isa.rs` -> **Severity: 197.5** (Blast Radius: 1.975 * Doc Risk: 100.0%)
- `cranelift/assembler-x64/src/vex.rs` -> **Severity: 180.3** (Blast Radius: 4.808 * Doc Risk: 37.5%)
- `cranelift/codegen/src/isa/riscv64/inst/vector.rs` -> **Severity: 174.829** (Blast Radius: 2.009 * Doc Risk: 87.0229%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
