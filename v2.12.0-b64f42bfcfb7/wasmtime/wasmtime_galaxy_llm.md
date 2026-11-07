# ARCHITECTURAL_BRIEF: wasmtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bytecodealliance/wasmtime.git` |
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
- **Scope:** 2097 analyzed artifact(s), 483559 LOC.
- **Load-bearing artifact:** `crates/wasmtime/src/lib.rs` -- 431 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/wasmtime/src/runtime/vm.rs` -- pulls in 124 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pulley/src/interp.rs` at magnitude 3201.1 (structural weight, not risk).
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
| Total Artifacts | 6447 |
| Analyzed Artifacts (Scanned) | 2097 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4350 |
| Total LOC | 483559 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 32.5% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7087 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1817 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 37.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9938 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 66 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1767 | 465997 | 84.3% |
| CPP | 144 | 12035 | 6.9% |
| MARKDOWN | 82 | 0 | 3.9% |
| C | 29 | 2358 | 1.4% |
| YAML | 20 | 1872 | 1.0% |
| SHELL | 17 | 491 | 0.8% |
| PLAINTEXT | 12 | 0 | 0.6% |
| DOCKERFILE | 8 | 58 | 0.4% |
| JAVASCRIPT | 7 | 628 | 0.3% |
| JSON | 3 | 11 | 0.1% |
| MAKEFILE | 2 | 36 | 0.1% |
| BINARY_THREAT | 2 | 2 | 0.1% |
| PYTHON | 1 | 14 | 0.0% |
| XML | 1 | 0 | 0.0% |
| CSS | 1 | 40 | 0.0% |
| M4 | 1 | 17 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2095 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 18%, Large Core Modules (3) 18%, Generic / Templated Code Files 16%, Data / Markup / Trivial 10%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2001 | 95.4% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 94 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4350*

**Composition by Extension & Reason:**
- `.wat`: 2249x Excluded (Unsupported Extension: '.wat'), 3x Unsupported Format (.wat)
- `.clif`: 1192x Excluded (Unsupported Extension: '.clif')
- `.wast`: 222x Excluded (Unsupported Extension: '.wast')
- `.rs`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Machine-Generated Source Code Signature: 205 LOC), 5x Excluded (Machine-Generated Source Code Signature: 243 LOC)
- `.isle`: 115x Unsupported Format (.isle)
- `.toml`: 102x Unsupported Format (.toml), 5x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wit`: 72x Excluded (Unsupported Extension: '.wit'), 25x Unsupported Format (.wit)
- `.md`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `no_extension`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.witx`: 23x Excluded (Unsupported Extension: '.witx')
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 7x Excluded (Unsupported Extension: '.lock')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1066 LOC)
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (Machine-Generated Source Code Signature: 89 LOC), 1x Excluded (Machine-Generated Source Code Signature: 117 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.9 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.8 | 38.9 | 50.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.6 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 30.6 | 28.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 54.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 64.7 | 84.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4851 | 773 | 6 | `cranelift/codegen/src/opts/div_const.rs` |
| cleanup | 687 | 221 | 1 | `crates/wasi/src/p1.rs` |
| guards | 10816 | 1200 | 13 | `tests/all/component_model/func.rs` |
| danger | 14324 | 1180 | 19 | `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` |
| concurrency | 8945 | 587 | 10 | `tests/all/component_model/async.rs` |
| connectivity | 23863 | 1478 | 30 | `pulley/src/interp.rs` |
| io | 1049 | 285 | 1 | `tests/all/cli_tests.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 73 | 46 | 0 | `crates/wizer/.github/actions/binary-compatible-builds/main.js` |
| time | 93 | 56 | 0 | `crates/wasi-http/src/p2/types.rs` |
| serialization | 25 | 11 | 0 | `crates/cli-flags/src/lib.rs` |
| regex | 14 | 11 | 0 | `ci/print-current-version.sh` |
| events | 1279 | 225 | 1 | `crates/wasmtime/src/runtime/component/concurrent.rs` |
| tests | 15819 | 985 | 17 | `tests/all/cli_tests.rs` |
| docs | 70295 | 1181 | 88 | `crates/wasmtime/src/config.rs` |
| debt | 3242 | 748 | 4 | `crates/environ/src/fact/trampoline.rs` |
| mutation | 65132 | 1644 | 75 | `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` |
| dead_code | 1963 | 580 | 1 | `cranelift/isle/veri/veri_engine/tests/veri.rs` |
| credential | 1 | 1 | 0 | `ci/build-release-artifacts.sh` |
| threat | 1 | 1 | 0 | `crates/wasi-preview1-component-adapter/byte-array-literals/src/lib.rs` |
| ml_ai | 1470 | 158 | 0 | `crates/fuzzing/src/generators/single_inst_module.rs` |
| ui | 5 | 2 | 0 | `crates/explorer/src/index.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/all/cli_tests.rs` (Hits: 50)
- `crates/wasi/src/p2/host/network.rs` (Hits: 42)
- `src/commands/serve.rs` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`crates/wasmtime/src/lib.rs`) — 431 inbound connections
2. **lib.rs** (`crates/environ/src/lib.rs`) — 304 inbound connections
3. **prelude.rs** (`crates/environ/src/prelude.rs`) — 181 inbound connections
4. **mod.rs** (`crates/core/src/error/mod.rs`) — 137 inbound connections
5. **engine.rs** (`crates/wasmtime/src/engine.rs`) — 132 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **vm.rs** (`crates/wasmtime/src/runtime/vm.rs`) — 124 outbound dependencies
2. **concurrent.rs** (`crates/wasmtime/src/runtime/component/concurrent.rs`) — 120 outbound dependencies
3. **mod.rs** (`cranelift/codegen/src/ir/mod.rs`) — 103 outbound dependencies
4. **mod.rs** (`crates/wasmtime/src/runtime/component/mod.rs`) — 100 outbound dependencies
5. **masm.rs** (`winch/codegen/src/isa/x64/masm.rs`) — 97 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `step` **(Many-Argument Workhorses)** (@ `cranelift/interpreter/src/step.rs`) -> Impact: **856.8** | LOC: 1306
  * *Intent:* /// Interpret a single Cranelift instruction. Note that program traps and interpreter errors are /// distinct: a program trap results in `Ok(Flow::Tra...
- `translate_operator` **(Many-Argument Workhorses)** (@ `crates/cranelift/src/translate/code_translator.rs`) -> Impact: **801.6** | LOC: 3197
  * *Intent:* /// Translates wasm operators into Cranelift IR instructions.
- `emit` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/aarch64/inst/emit.rs`) -> Impact: **644.3** | LOC: 2913
- `emit_with_alloc_consumer` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/s390x/inst/emit.rs`) -> Impact: **471.4** | LOC: 2227
- `print_with_state` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/s390x/inst/mod.rs`) -> Impact: **412.9** | LOC: 2265
- `parse_inst_operands` **(Many-Argument Workhorses)** (@ `cranelift/reader/src/parser.rs`) -> Impact: **363.2** | LOC: 422
  * *Intent:* // Parse the operands following the instruction opcode. // This depends on the format of the opcode.
- `try_emit_compressed` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/riscv64/inst/emit.rs`) -> Impact: **344.3** | LOC: 566
  * *Intent:* /// Tries to emit an instruction as compressed, if we can't return false.
- `emit_uncompressed` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/riscv64/inst/emit.rs`) -> Impact: **265.4** | LOC: 1928
- `generate` **(Many-Argument Workhorses)** (@ `crates/fuzzing/src/generators/component_async.rs`) -> Impact: **253.8** | LOC: 694
- `emit` **(Many-Argument Workhorses)** (@ `cranelift/codegen/src/isa/x64/inst/emit.rs`) -> Impact: **247.6** | LOC: 1688
  * *Intent:* /// and sil. /// /// For all instructions, also add a test that uses only low-half registers /// (rax .. rdi, xmm0 .. xmm7) etc, so as to check that a...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/all` | 56 | 9112.48 | 6.99% | 0.0% |
| `crates/wasmtime/src/runtime` | 31 | 6855.1 | 7.35% | 17.96% |
| `crates/wasmtime/src/runtime/component` | 15 | 5441.92 | 9.4% | 29.78% |
| `crates/wasmtime/src/runtime/vm` | 31 | 4731.74 | 7.85% | 10.99% |
| `crates/test-programs/src/bin` | 264 | 4619.46 | 12.11% | 39.1% |
| `pulley/src` | 11 | 4567.7 | 7.28% | 31.38% |
| `cranelift/codegen/src` | 31 | 4284.62 | 9.49% | 5.74% |
| `cranelift/codegen/src/machinst` | 12 | 4144.9 | 7.83% | 17.06% |
| `cranelift/codegen/src/ir` | 27 | 4095.52 | 6.45% | 15.18% |
| `cranelift/isle/isle/src` | 17 | 3882.0 | 13.56% | 7.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cranelift/codegen/src/ir/builder.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/ir/entities.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/ir/sourceloc.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/machinst/mod.rs` -> **100.0%** Exposure
- `cranelift/entity/src/iter.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cranelift/codegen/meta/src/pulley.rs` -> **100.0%** Exposure
- `cranelift/codegen/meta/src/shared/immediates.rs` -> **100.0%** Exposure
- `cranelift/codegen/src/opts/div_const.rs` -> **100.0%** Exposure
- `crates/environ/src/component/names.rs` -> **100.0%** Exposure
- `crates/environ/src/component/translate.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cranelift/isle/veri/veri_engine/tests/veri.rs` -> **197** Orphaned Functions | **0** Duplicates
- `crates/c-api/src/ref.rs` -> **60** Orphaned Functions | **0** Duplicates
- `cranelift/codegen/src/isa/x64/inst/mod.rs` -> **58** Orphaned Functions | **0** Duplicates
- `cranelift/codegen/src/machinst/mod.rs` -> **50** Orphaned Functions | **0** Duplicates
- `cranelift/module/src/module.rs` -> **0** Orphaned Functions | **40** Duplicates

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
- **Unknown Dependencies:** `20686` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pulley/src/interp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.467)
- **Top Global Matches:** file_cluster_0: 6.467, file_cluster_5: 9.562, file_cluster_15: 10.028
- **Magnitude:** 3201.1 | **LOC:** 5631 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **28**; blast radius 0.517; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (72.4%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 95.5409% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 10`, `state_mutation: 156`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 573`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 24`, `doc: 227`, `test: 15`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.517
  * `Choke Point (Betweenness):` 0.001347 | `Ripple Effect (Closeness):` 0.073269
  * `Imports (Out-Degree: 12):` debug, match_loop, tail_loop, alloc::string::ToString, core::fmt, core::mem, core::ops::ControlFlow, core::ops::Index...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/wasmtime/src/runtime/component/concurrent.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.163)
- **Top Global Matches:** file_cluster_4: 7.163, file_cluster_0: 10.52, file_cluster_16: 11.676
- **Magnitude:** 2549.62 | **LOC:** 5493 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 76.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **120**; blast radius 0.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.6%)
- **Documentation Coverage:** 32.9218% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `queue_call` **(Many-Argument Workhorses)** (Impact: 138.9)
    * *Intent:* /// Add the specified guest call to the "high priority" work item queue, to /// be started as soon a...
  * `start_call` **(Many-Argument Workhorses)** (Impact: 124.8)
    * *Intent:* /// Start a guest->guest call previously prepared using /// `Self::prepare_call`. /// /// This is ca...
  * `prepare_call` **(Many-Argument Workhorses)** (Impact: 121.1)
    * *Intent:* /// Prepare (but do not start) a guest->guest call. /// /// This is called from fused adapter code g...
  * `subtask_cancel` **(Many-Argument Workhorses)** (Impact: 107.4)
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
* *Structure:* `branch: 653`, `structural_boundaries: 931`, `args: 245`, `func_start: 182`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 7`, `state_mutation: 72`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 85`, `concurrency: 138`, `import: 41`
* *Defense:* `safety: 87`, `doc: 790`, `test: 30`, `immutability_locks: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.076513
  * `Imports (Out-Degree: 15):` abort, error_contexts, future_stream_any, futures_and_streams, table, tls, abort::JoinHandle, crate::AsContext...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/wasmtime/src/runtime/component/concurrent/futures_and_streams.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.207)
- **Top Global Matches:** file_cluster_4: 8.207, file_cluster_0: 9.03, file_cluster_16: 10.697
- **Magnitude:** 2524.8 | **LOC:** 4944 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 72.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **93**; blast radius 0.198; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 39.5062% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy` **(Many-Argument Workhorses)** (Impact: 187.1)
    * *Intent:* /// Copy `count` items from `read_address` to `write_address` for the /// specified stream or future...
  * `guest_read` **(Many-Argument Workhorses)** (Impact: 166.3)
    * *Intent:* /// Read from the specified stream or future from the guest.
  * `guest_write` **(Many-Argument Workhorses)** (Impact: 163.8)
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
* *Structure:* `branch: 624`, `structural_boundaries: 911`, `args: 250`, `func_start: 168`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 63`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 18`
* *Architecture:* `io: 6`, `api: 101`, `concurrency: 146`, `import: 37`
* *Defense:* `safety: 73`, `doc: 623`, `test: 20`, `sync_locks: 10`, `immutability_locks: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.198
  * `Choke Point (Betweenness):` 0.000124 | `Ripple Effect (Closeness):` 0.072753
  * `Imports (Out-Degree: 9):` buffers, buffers::Extender, buffers::ReadBuffer, buffers::SliceBuffer, buffers::UntypedWriteBuffer, buffers::VecBuffer, buffers::WriteBuffer, core::fmt...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `winch/codegen/src/visitor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.59)
- **Top Global Matches:** file_cluster_10: 9.59, file_cluster_15: 9.664, file_cluster_0: 9.954
- **Magnitude:** 2210.56 | **LOC:** 4688 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **84**; blast radius 0.141; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_br_table` **(Compute Cores)** (Impact: 41.2)
  * `visit_br_if` **(Compute Cores)** (Impact: 36.1)
  * `visit_call_indirect` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `visit_table_set` **(Compute Cores)** (Impact: 17.3)
  * `visit_memory_copy` **(Compute Cores)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 873`, `args: 759`, `func_start: 511`
* *Risk/State:* `state_mutation: 36`, `planned_debt: 1`
* *Architecture:* `api: 508`, `import: 62`
* *Defense:* `safety: 2`, `doc: 11`, `sync_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.000477
  * `Imports (Out-Degree: 14):` DivKind::*, OperandSize::*, RemKind::*, ShiftKind::*, WasmValType::*, crate::Result, crate::abi::RetArea, crate::bail...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/wit-bindgen/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.944)
- **Top Global Matches:** file_cluster_4: 6.944, file_cluster_12: 10.425, file_cluster_0: 10.678
- **Magnitude:** 2070.22 | **LOC:** 3556 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **34**; blast radius 0.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (71.3%), Guard Balance (formerly Safety Score) (61.7%)
- **Documentation Coverage:** 91.3978% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_guest_import_closure` **(Many-Argument Workhorses)** (Impact: 106.7)
  * `generate_trait` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `define_rust_guest_export` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `world_add_to_linker` **(Many-Argument Workhorses)** (Impact: 55.8)
  * `export` **(Many-Argument Workhorses)** (Impact: 48.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 112
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 687`, `args: 165`, `func_start: 109`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 13`, `state_mutation: 335`, `planned_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 72`, `concurrency: 47`, `import: 22`
* *Defense:* `safety: 48`, `doc: 164`, `test: 7`, `immutability_locks: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.655
  * `Choke Point (Betweenness):` 0.000511 | `Ripple Effect (Closeness):` 0.060118
  * `Imports (Out-Degree: 6):` config, rust, source, types, anyhow::bail, config::FunctionConfig, config::FunctionFilter, config::FunctionFlags...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cranelift/reader/src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.7)
- **Top Global Matches:** file_cluster_4: 9.7, file_cluster_12: 10.393, file_cluster_5: 10.807
- **Magnitude:** 1801.2 | **LOC:** 3719 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **80**; blast radius 0.551; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.0%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (48.8%)
- **Documentation Coverage:** 80.6818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_inst_operands` **(Many-Argument Workhorses)** (Impact: 363.2)
    * *Intent:* // Parse the operands following the instruction opcode. // This depends on the format of the opcode.
  * `parse_instruction` **(Many-Argument Workhorses)** (Impact: 98.7)
    * *Intent:* // Parse an instruction, append it to `block`. // // instruction ::= [inst-results "="] Opcode(opc) ...
  * `parse_exception_table` **(Compute Cores)** (Impact: 39.5)
    * *Intent:* // Parse an exception-table decl. // // exception-table ::= * SigRef(sig) "," BlockCall "," "[" (exc...
  * `parse_basic_block` **(Compute Cores)** (Impact: 37.9)
    * *Intent:* // Parse a basic block, add contents to `ctx`. // // extended-basic-block ::= * block-header { instr...
  * `parse_target_specs` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /// Parse a list of target specs. /// /// Accept a mix of `target` and `set` command lines. The `set...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 656`, `args: 186`, `func_start: 142`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 3`, `state_mutation: 79`
* *Architecture:* `api: 37`, `import: 26`
* *Defense:* `safety: 63`, `doc: 83`, `test: 178`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.000464 | `Ripple Effect (Closeness):` 0.009935
  * `Imports (Out-Degree: 30):` cranelift_codegen::data_value::DataValue, cranelift_codegen::entity::EntityRef, cranelift_codegen::entity::PrimaryMap, cranelift_codegen::ir, cranelift_codegen::ir::AbiParam, cranelift_codegen::ir::ArgumentExtension, cranelift_codegen::ir::ArgumentPurpose, cranelift_codegen::ir::Block...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `crates/wasi/src/p1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.961)
- **Top Global Matches:** file_cluster_4: 7.961, file_cluster_0: 9.518, file_cluster_15: 10.32
- **Magnitude:** 1512.74 | **LOC:** 2719 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **52**; blast radius 0.583; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (84.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.0%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 55.2% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_oneoff` **(Many-Argument Workhorses)** (Impact: 164.5)
  * `fd_read` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* /// Read from a file descriptor. /// NOTE: This is similar to `readv` in POSIX.
  * `fd_write_impl` **(Many-Argument Workhorses)** (Impact: 55.8)
    * *Intent:* /// Shared implementation of `fd_write` and `fd_pwrite`.
  * `path_open` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* /// Open a file or directory. /// NOTE: This is similar to `openat` in POSIX.
  * `fd_readdir` **(Many-Argument Workhorses)** (Impact: 49.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 569`, `args: 141`, `func_start: 99`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `planned_debt: 9`
* *Architecture:* `io: 1`, `api: 28`, `concurrency: 77`, `import: 26`
* *Defense:* `safety: 32`, `doc: 343`, `test: 5`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.000835 | `Ripple Effect (Closeness):` 0.019054
  * `Imports (Out-Degree: 17):` crate::ResourceTable, crate::WasiCtx, crate::WasiCtxView, crate::WasiView, crate::cli::WasiCliView, crate::clocks::WasiClocksView, crate::filesystem::WasiFilesystemView, crate::p2::FsError...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `cranelift/codegen/src/isa/s390x/inst/emit_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.161)
- **Top Global Matches:** file_cluster_12: 8.161, file_cluster_7: 9.252, file_cluster_2: 9.388
- **Magnitude:** 1493.44 | **LOC:** 13968 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.142; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (74.1%), Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (9.9%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_s390x_binemit` **(I/O & Config Routines)** (Impact: 15.5)
  * `simm20_zero` **(Annotated & Test Methods)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 338`, `state_mutation: 1198`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.057868
  * `Imports (Out-Degree: 6):` crate::ir::MemFlags, crate::ir::TrapCode, crate::isa::s390x::inst::*, crate::isa::s390x::settings, crate::settings::Configurable
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/cranelift/src/func_environ.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.047)
- **Top Global Matches:** file_cluster_12: 7.047, file_cluster_15: 8.1, file_cluster_0: 8.418
- **Magnitude:** 1418.08 | **LOC:** 4333 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **87**; blast radius 0.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.1%), Guard Balance (formerly Safety Score) (52.5%)
- **Documentation Coverage:** 81.3889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_indirect_call_type_signature` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `make_table` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `translate_global_get` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `translate_memory_size` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `convert_pointer_to_index_type` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /// Convert the target pointer-sized integer `val` into the memory/table's index type. /// /// For m...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 1022`, `args: 242`, `func_start: 213`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 14`, `state_mutation: 43`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 167`, `import: 23`
* *Defense:* `safety: 32`, `doc: 156`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.003116 | `Ripple Effect (Closeness):` 0.007822
  * `Imports (Out-Degree: 40):` gc, stack_switching, cranelift_codegen::cursor::FuncCursor, cranelift_codegen::ir, cranelift_codegen::ir::ArgumentPurpose, cranelift_codegen::ir::Block, cranelift_codegen::ir::BlockArg, cranelift_codegen::ir::ConstantData...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `winch/codegen/src/isa/x64/masm.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.185)
- **Top Global Matches:** file_cluster_15: 7.185, file_cluster_0: 7.485, file_cluster_16: 8.734
- **Magnitude:** 1406.04 | **LOC:** 3598 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **97**; blast radius 0.143; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.4%), Guard Balance (formerly Safety Score) (51.5%), Mutation Surface (formerly State Flux) (15.2%)
- **Documentation Coverage:** 97.1774% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `v128_shift` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `wasm_load` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `splat` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `atomic_rmw` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `popcnt` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 336`, `args: 243`, `func_start: 148`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 25`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 101`, `import: 9`
* *Defense:* `safety: 13`, `doc: 22`, `test: 8`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.00403
  * `Imports (Out-Degree: 29):` IntCmpKind::*, cranelift_codegen::Final, cranelift_codegen::MachBufferFinalized, cranelift_codegen::MachLabel, cranelift_codegen::binemit::CodeOffset, cranelift_codegen::ir::MemFlags, cranelift_codegen::ir::RelSourceLoc, cranelift_codegen::ir::SourceLoc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/all/component_model/func.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.095)
- **Top Global Matches:** file_cluster_4: 9.095, file_cluster_6: 9.732, file_cluster_12: 14.569
- **Magnitude:** 1260.94 | **LOC:** 4649 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.141; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.2%), Concurrency Surface (formerly Concurrency) (70.3%), Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.6%)
- **Documentation Coverage:** 91.8919% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `integers` **(I/O & Config Routines)** (Impact: 93.6)
  * `test_many_results` **(Many-Argument Workhorses)** (Impact: 92.3)
  * `test_many_parameters` **(Many-Argument Workhorses)** (Impact: 61.7)
  * `option` **(I/O & Config Routines)** (Impact: 42.6)
  * `some_traps` **(I/O & Config Routines)** (Impact: 39.2)
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
* *Structure:* `branch: 515`, `structural_boundaries: 1151`, `args: 144`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 32`, `state_mutation: 19`, `fragile_debt: 4`
* *Architecture:* `api: 64`, `concurrency: 141`, `import: 5`
* *Defense:* `safety: 8`, `doc: 12`, `test: 267`, `sync_locks: 1`, `immutability_locks: 228`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002907
  * `Imports (Out-Degree: 6):` std::sync::Arc, std::sync::atomic::AtomicBool, std::sync::atomic::Ordering::SeqCst, super::ApiStyle, super::REALLOC_AND_FREE, wasmtime::Config, wasmtime::Engine, wasmtime::Result...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/environ/src/fact/trampoline.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.066)
- **Top Global Matches:** file_cluster_12: 8.066, file_cluster_0: 8.403, file_cluster_15: 8.713
- **Magnitude:** 1253.84 | **LOC:** 4420 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **56**; blast radius 0.154; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.9%), Guard Balance (formerly Safety Score) (61.5%), Debt Markers (formerly Tech Debt) (31.0%)
- **Documentation Coverage:** 78.626% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 97`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 105`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `concurrency: 10`, `import: 12`
* *Defense:* `safety: 28`, `doc: 198`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.100333
  * `Imports (Out-Degree: 11):` crate::FuncIndex, crate::GlobalIndex, crate::Trap, crate::component::CanonicalAbiInfo, crate::component::ComponentTypesBuilder, crate::component::FLAG_MAY_LEAVE, crate::component::FixedEncoding, crate::component::FlatType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/cranelift/src/translate/code_translator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.872)
- **Top Global Matches:** file_cluster_4: 7.872, file_cluster_15: 8.337, file_cluster_12: 9.065
- **Magnitude:** 1239.66 | **LOC:** 4498 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **54**; blast radius 0.158; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.9%), Guard Balance (formerly Safety Score) (53.3%), Mutation Surface (formerly State Flux) (23.8%)
- **Documentation Coverage:** 48.4848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translate_operator` **(Many-Argument Workhorses)** (Impact: 801.6)
    * *Intent:* /// Translates wasm operators into Cranelift IR instructions.
  * `translate_unreachable_operator` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /// Deals with a Wasm instruction located in an unreachable portion of the code. Most of them /// ar...
  * `create_catch_block` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `translate_atomic_cas` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `translate_atomic_rmw` **(Many-Argument Workhorses)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 17
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 969`, `args: 176`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 18`, `state_mutation: 49`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 2`, `import: 20`
* *Defense:* `safety: 4`, `doc: 124`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.005454
  * `Imports (Out-Degree: 21):` cranelift_codegen::ir, cranelift_codegen::ir::AtomicRmwOp, cranelift_codegen::ir::BlockArg, cranelift_codegen::ir::ExceptionTag, cranelift_codegen::ir::InstBuilder, cranelift_codegen::ir::JumpTableData, cranelift_codegen::ir::MemFlags, cranelift_codegen::ir::Value...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/debugger/src/host/api.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.097)
- **Top Global Matches:** file_cluster_0: 6.097, file_cluster_5: 9.072, file_cluster_12: 9.881
- **Magnitude:** 1237.44 | **LOC:** 1056 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.174; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.4%)
- **Documentation Coverage:** 98.0% of unit weight undocumented
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
* *Structure:* `branch: 253`, `structural_boundaries: 345`, `args: 100`, `func_start: 97`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 44`, `planned_debt: 1`
* *Architecture:* `api: 61`, `concurrency: 150`, `import: 9`
* *Defense:* `safety: 20`, `doc: 33`, `sync_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.001073
  * `Imports (Out-Degree: 8):` crate::DebugRunResult, crate::host::bindings::wasm_type_to_val_type, crate::host::opaque::OpaqueDebugger, crate::host::wit, std::pin::Pin, std::sync::Arc, std::sync::atomic::AtomicBool, std::sync::atomic::Ordering...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/all/cli_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.679)
- **Top Global Matches:** file_cluster_12: 7.679, file_cluster_5: 8.177, file_cluster_7: 8.915
- **Magnitude:** 1147.82 | **LOC:** 3329 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 88.9%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **28**; blast radius 0.234; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.2%), Concurrency Surface (formerly Concurrency) (85.6%), Connectivity (formerly Api Exposure) (68.5%), Guard Balance (formerly Safety Score) (50.8%)
- **Documentation Coverage:** 97.8723% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `preview2_stdin` **(I/O & Config Routines)** (Impact: 27.1)
  * `cli_serve_sleep` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `cli_serve_hello_world` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `spawn` **(Compute Cores)** (Impact: 20.1)
  * `config_cli_flag` **(I/O & Config Routines)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 490`, `args: 192`, `func_start: 151`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 112`, `high_risk_execution: 4`, `state_mutation: 10`, `planned_debt: 2`
* *Architecture:* `io: 50`, `api: 131`, `concurrency: 126`, `import: 19`
* *Defense:* `safety: 6`, `doc: 9`, `test: 337`, `immutability_locks: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.004239
  * `Imports (Out-Degree: 3):` http_body_util::BodyExt, hyper::header::HeaderValue, self::get_wasmtime_command, self::run_wasmtime, std::fs::File, std::io, std::io::BufRead, std::io::BufReader...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cranelift/interpreter/src/step.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.11)
- **Top Global Matches:** file_cluster_6: 10.11, file_cluster_4: 10.209, file_cluster_5: 14.849
- **Magnitude:** 1146.44 | **LOC:** 1656 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **36**; blast radius 0.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Mutation Surface (formerly State Flux) (41.6%), Complexity Load (formerly Cognitive Load) (31.6%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `step` **(Many-Argument Workhorses)** (Impact: 856.8)
    * *Intent:* /// Interpret a single Cranelift instruction. Note that program traps and interpreter errors are ///...
  * `fcmp` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* /// Compare two values using the given floating point condition `code`.
  * `icmp` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /// Compare two values using the given integer condition `code`.
  * `extractlanes` **(Stateful Encapsulated Methods)** (Impact: 19.1)
    * *Intent:* /// Converts a SIMD vector value into a Rust array of [Value] for processing. /// If `x` is a scalar...
  * `binary_arith` **(Generic / Templated Code)** (Impact: 12.2)
    * *Intent:* /// Performs the supplied binary arithmetic `op` on two values, either vector or scalar.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 27
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 315`, `args: 99`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 40`, `state_mutation: 25`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 13`, `doc: 35`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.005537
  * `Imports (Out-Degree: 16):` cranelift_codegen::data_value::DataValue, cranelift_codegen::ir::AbiParam, cranelift_codegen::ir::AtomicRmwOp, cranelift_codegen::ir::Block, cranelift_codegen::ir::BlockArg, cranelift_codegen::ir::BlockCall, cranelift_codegen::ir::Endianness, cranelift_codegen::ir::ExternalName...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `winch/codegen/src/isa/x64/asm.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.376)
- **Top Global Matches:** file_cluster_12: 7.376, file_cluster_15: 7.582, file_cluster_0: 8.376
- **Magnitude:** 1128.4 | **LOC:** 2817 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **67**; blast radius 0.145; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.9%), Guard Balance (formerly Safety Score) (71.3%), Debt Markers (formerly Tech Debt) (9.7%)
- **Documentation Coverage:** 21.372% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 130`, `planned_debt: 12`
* *Architecture:* `api: 183`, `import: 18`
* *Defense:* `safety: 2`, `doc: 277`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 0.000109 | `Ripple Effect (Closeness):` 0.004133
  * `Imports (Out-Degree: 26):` IntCmpKind::*, MulWideKind::*, OperandSize::*, cranelift_assembler_x64, cranelift_codegen::CallInfo, cranelift_codegen::Final, cranelift_codegen::MachBuffer, cranelift_codegen::MachBufferFinalized...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cranelift/isle/veri/veri_engine/src/type_inference.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.216)
- **Top Global Matches:** file_cluster_6: 6.216, file_cluster_4: 12.487, file_cluster_8: 13.084
- **Magnitude:** 1114.02 | **LOC:** 2453 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **22**; blast radius 0.325; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Connectivity (formerly Api Exposure) (45.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_rule_constraints` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `solve_constraints` **(Many-Argument Workhorses)** (Impact: 113.8)
    * *Intent:* // // t4 = bv // t1 = bv // t7 = bv // // would result in: // bv16 -> t2, t6, t1 // bv8 -> t3, t5, t...
  * `add_annotation_constraints` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `type_annotations_using_rule` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `create_parse_tree_pattern` **(Many-Argument Workhorses)** (Impact: 45.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 82 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 427`, `args: 20`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 363`, `dead_code: 9`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `api: 21`, `import: 10`
* *Defense:* `safety: 23`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.003838
  * `Imports (Out-Degree: 6):` cranelift_isle, crate::Config, crate::FLAGS_WIDTH, crate::REG_WIDTH, crate::annotations::AnnotationEnv, crate::termname::pattern_contains_termname, isle::sema::Pattern, isle::sema::TermEnv...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/wasmtime/src/runtime/types.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.703)
- **Top Global Matches:** file_cluster_0: 8.703, file_cluster_12: 9.642, file_cluster_16: 9.723
- **Magnitude:** 1101.22 | **LOC:** 3654 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **41**; blast radius 0.207; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.4%), Connectivity (formerly Api Exposure) (85.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.9%)
- **Documentation Coverage:** 26.9147% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `with_finality_and_supertype` **(Many-Argument Workhorses)** (Impact: 51.6)
    * *Intent:* /// Create a new function type with the given finality, supertype, parameter /// types, and result t...
  * `fmt` **(Compute Cores)** (Impact: 21.7)
  * `with_finality_and_supertype` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* /// fields. /// /// The result will be associated with the given engine, and attempts to use /// it ...
  * `validate` **(Defensive Guards)** (Impact: 13.4)
  * `_new` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 247`, `args: 309`, `func_start: 244`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 3`, `state_mutation: 15`, `planned_debt: 10`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 264`, `import: 12`
* *Defense:* `safety: 23`, `doc: 1016`, `test: 26`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 0.000439 | `Ripple Effect (Closeness):` 0.090108
  * `Imports (Out-Degree: 11):` matching, HeapType::*, Mutability, core::fmt, core::fmt::Display, core::fmt::Write, crate::AsContextMut, crate::Engine...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/wasi-common/src/snapshots/preview_1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.681)
- **Top Global Matches:** file_cluster_4: 7.681, file_cluster_12: 10.638, file_cluster_5: 10.855
- **Magnitude:** 1099.3 | **LOC:** 1571 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **41**; blast radius 2.008; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.7%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 294`, `structural_boundaries: 407`, `args: 102`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 25`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 51`, `concurrency: 84`, `import: 11`
* *Defense:* `safety: 17`, `test: 3`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.008
  * `Choke Point (Betweenness):` 0.002506 | `Ripple Effect (Closeness):` 0.00815
  * `Imports (Out-Degree: 11):` error, cap_std::time::Duration, cap_std::time::SystemClock, crate::EnvError, crate::I32Exit, crate::SystemTimeSpec, crate::WasiCtx, crate::dir::DirEntry...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cranelift/codegen/src/isa/s390x/inst/emit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.578)
- **Top Global Matches:** file_cluster_15: 8.578, file_cluster_4: 8.702, file_cluster_12: 9.015
- **Magnitude:** 1060.52 | **LOC:** 3707 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.154; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Mutation Surface (formerly State Flux) (50.6%), Connectivity (formerly Api Exposure) (42.9%)
- **Documentation Coverage:** 42.2535% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_with_alloc_consumer` **(Many-Argument Workhorses)** (Impact: 471.4)
  * `mem_finalize` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* /// Memory addressing mode finalization: convert "special" modes (e.g., /// generic arbitrary stack ...
  * `mem_emit` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `mem_rs_emit` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `mem_imm8_emit` **(Many-Argument Workhorses)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 53
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 662`, `args: 94`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 56`, `state_mutation: 173`, `planned_debt: 1`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* `safety: 15`, `doc: 252`, `test: 48`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.066231
  * `Imports (Out-Degree: 9):` cranelift_control::ControlPlane, crate::ir, crate::ir::LibCall, crate::ir::MemFlags, crate::ir::TrapCode, crate::isa::CallConv, crate::isa::s390x::abi::REG_SAVE_AREA_SIZE, crate::isa::s390x::inst::*...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/wasmtime/src/runtime/component/func/typed.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.986)
- **Top Global Matches:** file_cluster_0: 6.986, file_cluster_5: 9.222, file_cluster_12: 10.026
- **Magnitude:** 1013.66 | **LOC:** 3185 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **38**; blast radius 0.22; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.8%), Debt Markers (formerly Tech Debt) (53.4%), Connectivity (formerly Api Exposure) (49.9%)
- **Documentation Coverage:** 67.5325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lower_string` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `lift_try_map` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `lower_map_iter` **(Generic / Templated Code)** (Impact: 23.9)
  * `prepare_call` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /// Calls `concurrent::prepare_call` with monomorphized functions for /// lowering the parameters an...
  * `call_async` **(Generic / Templated Code)** (Impact: 19.6)
    * *Intent:* /// Exactly like [`Self::call`], except for invoking WebAssembly /// [asynchronously](crate#async). ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 483`, `args: 156`, `func_start: 127`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 43`, `planned_debt: 12`, `fragile_debt: 7`, `duplicate_logic: 8`
* *Architecture:* `api: 35`, `concurrency: 25`, `import: 22`
* *Defense:* `safety: 20`, `doc: 551`, `test: 57`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.000259 | `Ripple Effect (Closeness):` 0.07194
  * `Imports (Out-Degree: 7):` alloc::borrow::Cow, core::fmt, core::hash::Hash, core::iter, core::marker, core::mem, core::mem::MaybeUninit, core::ptr::NonNull...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/wasmtime/src/runtime/store.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.813)
- **Top Global Matches:** file_cluster_0: 7.813, file_cluster_5: 9.124, file_cluster_12: 9.339
- **Magnitude:** 1004.9 | **LOC:** 3152 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **76**; blast radius 0.438; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.7%)
- **Documentation Coverage:** 51.5625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wasm_fault` **(Many-Argument Workhorses)** (Impact: 24.8)
    * *Intent:* /// Translates a WebAssembly fault at the native `pc` and native `addr` to a /// WebAssembly-relativ...
  * `allocate_instance` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* /// from this store's own configuration. The `kind` provided is used to /// distinguish between "rea...
  * `try_new` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* /// Like `Store::new` but returns an error on allocation failure.
  * `trace_wasm_stack_frame` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `allocate_gc_store` **(Generic / Templated Code)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 159
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 535`, `args: 199`, `func_start: 184`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 49`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 7`
* *Architecture:* `api: 154`, `concurrency: 99`, `import: 39`
* *Defense:* `safety: 14`, `doc: 823`, `test: 56`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.438
  * `Choke Point (Betweenness):` 0.002517 | `Ripple Effect (Closeness):` 0.093374
  * `Imports (Out-Degree: 29):` async_, context, data, func_refs, gc, token, core::convert::Infallible, core::fmt...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `cranelift/codegen/src/verifier/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.219)
- **Top Global Matches:** file_cluster_4: 7.219, file_cluster_15: 9.56, file_cluster_0: 9.787
- **Magnitude:** 983.46 | **LOC:** 2313 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **55**; blast radius 1.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.3%), Mutation Surface (formerly State Flux) (19.8%)
- **Documentation Coverage:** 76.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_entity_references` **(Many-Argument Workhorses)** (Impact: 117.3)
  * `typecheck_variable_args` **(Many-Argument Workhorses)** (Impact: 38.5)
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
* *Structure:* `branch: 315`, `structural_boundaries: 383`, `args: 99`, `func_start: 78`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 11`, `state_mutation: 19`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 20`, `import: 24`
* *Defense:* `safety: 19`, `doc: 113`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.014
  * `Choke Point (Betweenness):` 0.000496 | `Ripple Effect (Closeness):` 0.089394
  * `Imports (Out-Degree: 19):` alloc::collections::BTreeSet, alloc::string::String, alloc::string::ToString, alloc::vec::Vec, core::fmt, core::fmt::Display, core::fmt::Formatter, cranelift_entity::packed_option::ReservedValue...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `cranelift/codegen/src/opts/div_const.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.3)
- **Top Global Matches:** file_cluster_4: 8.3, file_cluster_15: 9.61, file_cluster_9: 10.357
- **Magnitude:** 982.74 | **LOC:** 1215 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.14; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_magic_generators_give_correct_numbers` **(I/O & Config Routines)** (Impact: 77.2)
  * `test_magic_generators_dont_panic` **(I/O & Config Routines)** (Impact: 37.4)
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
* *Risk/State:* `state_mutation: 151`
* *Architecture:* `api: 28`, `import: 3`
* *Defense:* `doc: 17`, `test: 172`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.073466
  * `Imports (Out-Degree: 0):` proptest::strategy::Strategy, self::MS32, self::MS64, self::MU32, self::MU64, self::magic_s32, self::magic_s64, self::magic_u32...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/all/missing_async.rs` (RUST) | Magnitude: 190.68 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 220, core_var_decl: 87, design_snake_case: 86
- `crates/environ/src/trap_encoding.rs` (RUST) | Magnitude: 39.66 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 107, doc: 80, core_var_decl: 55, design_pascal_case: 46
- `crates/test-programs/src/bin/async_error_context.rs` (RUST) | Magnitude: 10.66 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, import: 3, args: 2
- `winch/codegen/src/isa/aarch64/address.rs` (RUST) | Magnitude: 60.48 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, doc: 35, structural_boundaries: 16, branch: 13
- `cranelift/assembler-x64/meta/src/generate/inst.rs` (RUST) | Magnitude: 132.14 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 80, args: 42, branch: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `cranelift/isle/islec/src/main.rs` (RUST) | Magnitude: 7.06 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, core_var_decl: 7, design_snake_case: 5
- `cranelift/isle/fuzz/fuzz_targets/compile.rs` (RUST) | Magnitude: 15.6 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 14, core_var_decl: 8, design_snake_case: 7
- `winch/codegen/src/visitor.rs` (RUST) | Magnitude: 2210.56 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 3927, structural_boundaries: 873, args: 759, pointers: 512
- `examples/hello.rs` (RUST) | Magnitude: 8.26 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, debug_prints: 9, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/serialize.rs` (RUST) | Magnitude: 18.18 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 16, debug_prints: 12, core_var_decl: 9
- `crates/test-programs/src/bin/async_error_context_caller.rs` (RUST) | Magnitude: 14.78 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, concurrency: 3, branch: 2
- `cranelift/codegen/src/isa/riscv64/inst/emit_tests.rs` (RUST) | Magnitude: 282.18 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2166, state_mutation: 202, structural_boundaries: 45, sync_locks: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cranelift/codegen/src/machinst/vcode.rs` (RUST) | Magnitude: 844.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1205, structural_boundaries: 359, doc: 229, branch: 194
- `crates/wasmtime/build.rs` (RUST) | Magnitude: 31.94 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 55, branch: 18, structural_boundaries: 16, core_var_decl: 13
- `cranelift/reader/src/sourcemap.rs` (RUST) | Magnitude: 113.2 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 149, doc: 34, args: 32, api: 25
- `crates/wizer/.github/workflows/release.yml` (YAML) | Magnitude: 29.98 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 113, args: 21, branch: 14, import: 13
- `crates/wasi-nn/tests/exec/witx.rs` (RUST) | Magnitude: 29.38 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 36, indent_spaces: 30, core_var_decl: 12, design_snake_case: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cranelift/assembler-x64/meta/src/instructions/atomic.rs` (RUST) | Magnitude: 3.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 3, import: 2, args: 1
- `crates/c-api/tests/table_type.cc` (CPP) | Magnitude: 3.56 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, test: 7, pointers: 6, args: 3
- `crates/wasi/tests/all/p3/mod.rs` (RUST) | Magnitude: 106.92 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: concurrency: 57, indent_spaces: 54, test: 50, structural_boundaries: 48
- `crates/jit-icache-coherence/src/lib.rs` (RUST) | Magnitude: 5.38 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 91, indent_spaces: 12, structural_boundaries: 7, branch: 4
- `crates/test-programs/src/bin/p2_cli_serve_sleep.rs` (RUST) | Magnitude: 4.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/cache/tests/cache_write_default_config.rs` (RUST) | Magnitude: 1.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, test: 4, core_var_decl: 3
- `crates/test-programs/src/bin/p3_sockets_tcp_bind.rs` (RUST) | Magnitude: 38.48 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 47, core_var_decl: 33, design_snake_case: 31
- `crates/test-programs/src/bin/p1_symlink_filestat.rs` (RUST) | Magnitude: 12.92 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 17, safety_bypasses: 15, core_var_decl: 14
- `crates/test-programs/src/bin/p1_path_open_lots.rs` (RUST) | Magnitude: 17.98 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 26, core_var_decl: 21, design_snake_case: 21
- `crates/wasmtime/tests/unload-engine.rs` (RUST) | Magnitude: 6.48 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, safety_bypasses: 5, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cranelift/codegen/src/timing.rs` (RUST) | Magnitude: 94.36 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 54, doc: 51, args: 26
- `crates/component-util/src/lib.rs` (RUST) | Magnitude: 39.34 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, doc: 21, branch: 17, structural_boundaries: 10
- `examples/threads.cc` (CPP) | Magnitude: 49.6 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 57, core_var_decl: 19, structural_boundaries: 18, sync_locks: 17
- `examples/wasip1/main.cc` (CPP) | Magnitude: 6.7 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 9, import: 5, args: 3
- `crates/c-api/include/wasmtime/types/memory.hh` (CPP) | Magnitude: 64.94 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 117, doc: 48, pointers: 42, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cranelift/codegen/meta/src/isa/pulley.rs` (RUST) | Magnitude: 3.28 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 3, args: 1, func_start: 1
- `crates/c-api/src/types/val.rs` (RUST) | Magnitude: 35.8 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 26, api: 23, design_snake_case: 17
- `examples/hello.c` (C) | Magnitude: 43.62 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 84, pointers: 38, structural_boundaries: 13, debug_prints: 12
- `tests/all/main.rs` (RUST) | Magnitude: 28.6 | Delta: **0.264** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 75, indent_spaces: 41, core_var_decl: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `cranelift/interpreter/src/lib.rs` (RUST) | Magnitude: 22.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, doc: 3
- `crates/cranelift/src/translate/mod.rs` (RUST) | Magnitude: 21.26 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, doc: 11, api: 6, import: 6
- `crates/wasmtime/src/runtime/gc/enabled.rs` (RUST) | Magnitude: 23.32 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, api: 8, import: 8, doc: 2
- `cranelift/isle/isle/src/log.rs` (RUST) | Magnitude: 15.24 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: decorators: 4, indent_spaces: 4, doc: 3, reflection_metaprogramming: 2
- `crates/wasi-preview1-component-adapter/provider/src/lib.rs` (RUST) | Magnitude: 17.64 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 40, api: 4, globals: 4, immutability_locks: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/c-api/tests/global.cc` (CPP) | Magnitude: 2.98 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, test: 6, args: 5, import: 3
- `cranelift/assembler-x64/meta/src/instructions/unpack.rs` (RUST) | Magnitude: 3.08 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 2, import: 2, args: 1
- `crates/c-api/tests/table.cc` (CPP) | Magnitude: 3.02 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, test: 8, args: 3, import: 3
- `examples/fast_compilation.rs` (RUST) | Magnitude: 4.3 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, doc: 4, core_var_decl: 3
- `crates/c-api/tests/component/utils.h` (CPP) | Magnitude: 16.62 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 73, immutability_locks: 9, structural_boundaries: 4, memory_alloc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `cranelift/isle/isle/src/sema.rs` (RUST) | Magnitude: 910.64 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2050, structural_boundaries: 416, doc: 289, branch: 212
- `crates/wiggle/generate/src/funcs.rs` (RUST) | Magnitude: 228.74 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 358, structural_boundaries: 110, core_var_decl: 71, design_snake_case: 66
- `cranelift/codegen/src/isa/s390x/abi.rs` (RUST) | Magnitude: 615.18 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1121, doc: 146, structural_boundaries: 135, branch: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/gdbstub-component/src/target.rs` (RUST) | Magnitude: 224.48 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 360, structural_boundaries: 134, branch: 50, generics: 49
- `cranelift/codegen/src/isa/riscv64/inst/regs.rs` (RUST) | Magnitude: 63.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, decorators: 28, args: 27, func_start: 27
- `cranelift/codegen/src/isa/riscv64/inst/unwind/systemv.rs` (RUST) | Magnitude: 43.06 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 51, core_var_decl: 24, design_snake_case: 22
- `crates/wasmtime/src/runtime/gc/enabled/anyref.rs` (RUST) | Magnitude: 266.68 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 383, doc: 338, structural_boundaries: 102, generics: 98
- `crates/wasmtime/src/runtime/vm/debug_builtins.rs` (RUST) | Magnitude: 11.62 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 10, pointers: 10, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `cranelift/interpreter/src/step.rs` (RUST) | Magnitude: 1146.44 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1386, branch: 526, structural_boundaries: 315, core_var_decl: 258
- `crates/wasmtime/src/runtime/vm/gc/enabled/arrayref.rs` (RUST) | Magnitude: 157.14 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 261, doc: 85, structural_boundaries: 67, core_var_decl: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/test-programs/src/bin/p3_http_outbound_request_put.rs` (RUST) | Magnitude: 6.3 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 9, safety_bypasses: 6, test: 4
- `crates/test-programs/src/bin/p3_sockets_udp_connect.rs` (RUST) | Magnitude: 48.08 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 137, core_var_decl: 40, structural_boundaries: 39, design_snake_case: 33
- `crates/wasi/tests/all/p2/async_.rs` (RUST) | Magnitude: 337.4 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: test: 151, concurrency: 151, indent_spaces: 132, structural_boundaries: 98
- `crates/test-programs/src/bin/p1_directory_seek.rs` (RUST) | Magnitude: 8.32 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 9, safety_bypasses: 6, core_var_decl: 6
- `crates/wasi-common/tests/all/sync.rs` (RUST) | Magnitude: 155.18 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 106, args: 56, safety_bypasses: 56, func_start: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/fuzzing/tests/oom/table.rs` (RUST) | Magnitude: 63.84 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 74, core_var_decl: 43, design_snake_case: 43
- `crates/fuzzing/src/generators/memory.rs` (RUST) | Magnitude: 107.64 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 119, branch: 39, structural_boundaries: 38, generics: 20
- `examples/fib-debug/main.c` (C) | Magnitude: 38.74 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, pointers: 32, structural_boundaries: 18, debug_prints: 14
- `crates/environ/fuzz/fuzz_targets/fact-valid-module.rs` (RUST) | Magnitude: 22.32 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 31, core_var_decl: 15, design_snake_case: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/environ/src/collections.rs` -> Churn: **81.31%** | Cog Load: 0.0% | Debt: 62.2459%
- `crates/wasmtime/src/runtime/component/func/typed.rs` -> Churn: **78.79%** | Cog Load: 7.2955% | Debt: 53.3635%
- `crates/wasi-http/tests/all/p3/mod.rs` -> Churn: **73.74%** | Cog Load: 69.379% | Debt: 0.0%
- `crates/wasmtime/src/runtime/func.rs` -> Churn: **73.74%** | Cog Load: 12.6398% | Debt: 53.2273%
- `crates/wasmtime/src/runtime/types.rs` -> Churn: **67.89%** | Cog Load: 4.4445% | Debt: 97.3942%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `winch/codegen/src/visitor.rs` -> **r-near** (100.0% isolated ownership) | Magnitude: 2210.56
- `cranelift/reader/src/parser.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 1801.2
- `crates/wasi/src/p1.rs` -> **Alex Crichton** (100.0% isolated ownership) | Magnitude: 1512.74
- `crates/debugger/src/host/api.rs` -> **Chris Fallin** (100.0% isolated ownership) | Magnitude: 1237.44
- `tests/all/cli_tests.rs` -> **Alex Crichton** (88.9% isolated ownership) | Magnitude: 1147.82

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/unwinder/src/exception_table.rs` -> **Severity: 1.993** (Bridge: 0.0291 * Flux: 68.5423%)
- `crates/wasmtime/src/config.rs` -> **Severity: 1.492** (Bridge: 0.0169 * Flux: 88.2048%)
- `crates/wasmtime/src/runtime/code_memory.rs` -> **Severity: 0.831** (Bridge: 0.021 * Flux: 39.4564%)
- `crates/wasmtime/src/lib.rs` -> **Severity: 0.723** (Bridge: 0.0588 * Flux: 12.2904%)
- `cranelift/codegen/src/machinst/buffer.rs` -> **Severity: 0.396** (Bridge: 0.007 * Flux: 56.9391%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/environ/src/ext.rs` -> **Severity: 11.28** (Embedded: 0.141 * Error Risk: 80.0%)
- `cranelift/entity/src/boxed_slice.rs` -> **Severity: 9.522** (Embedded: 0.1407 * Error Risk: 67.656%)
- `crates/core/src/alloc/vec.rs` -> **Severity: 8.936** (Embedded: 0.1643 * Error Risk: 54.3887%)
- `cranelift/entity/src/primary.rs` -> **Severity: 8.857** (Embedded: 0.1467 * Error Risk: 60.3606%)
- `crates/environ/src/tunables.rs` -> **Severity: 8.738** (Embedded: 0.1693 * Error Risk: 51.6134%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/test-programs/src/p3/mod.rs` -> **Severity: 2901.7** (Blast Radius: 29.017 * Doc Risk: 100.0%)
- `crates/core/src/error/error.rs` -> **Severity: 2194.983** (Blast Radius: 31.885 * Doc Risk: 68.8406%)
- `crates/test-programs/src/lib.rs` -> **Severity: 1746.7** (Blast Radius: 17.467 * Doc Risk: 100.0%)
- `crates/wasmtime/src/lib.rs` -> **Severity: 1674.8** (Blast Radius: 33.496 * Doc Risk: 50.0%)
- `crates/test-programs/src/p3/http.rs` -> **Severity: 1211.7** (Blast Radius: 12.117 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1254 literal sites + 16 sites through wrappers = 1270
- **`panics_and_aborts`:** 1121 literal sites + 34 sites through wrappers = 1155

- `bad_type_info` (function, panics_and_aborts, primitive): 23 call sites in 4 files -- `crates/wasmtime/src/runtime/component/func/typed.rs`
- `connect` (function, debug_prints, primitive): 4 call sites in 1 files -- `crates/test-programs/src/bin/p3_sockets_udp_connect.rs`
- `drop` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `crates/wasmtime/tests/engine_across_forks.rs`
- `fail_at_runtime` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `crates/fuzzing/wasm-spec-interpreter/src/without_library.rs`
- `overrun_the_stack` (function, debug_prints, primitive): 3 call sites in 1 files -- `crates/wasmtime/tests/host_segfault.rs`
- `run_instance` (function, debug_prints, primitive): 3 call sites in 1 files -- `tests/all/async_functions.rs`
- `segfault` (function, debug_prints, primitive): 3 call sites in 1 files -- `crates/wasmtime/tests/host_segfault.rs`
- `abort_stack_overflow` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/wasmtime/src/runtime/vm/sys/unix/signals.rs`
- `store_id_mismatch` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/wasmtime/src/runtime/store/data.rs`
- `test_aarch64_with_config` (function, debug_prints, primitive): 1 call sites in 1 files -- `cranelift/isle/veri/veri_engine/tests/utils/mod.rs`
- `test_from_file_with_config` (function, debug_prints, primitive): 1 call sites in 1 files -- `cranelift/isle/veri/veri_engine/tests/utils/mod.rs`
- `unwrap_failed` (function, debug_prints, primitive): 1 call sites in 1 files -- `crates/c-api/include/wasmtime/error.hh`
*(+1 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 126104 call pairs -- scoped 20.0%, unique 0.0%, ambiguous 29.5%, external 50.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 121865 | 20.1% | 0.0% | 29.4% | 50.5% |
| cpp | 3435 | 20.7% | 1.8% | 40.2% | 37.3% |
| c | 642 | 11.4% | 0.2% | 0.0% | 88.5% |
| shell | 96 | 6.2% | 0.0% | 0.0% | 93.8% |
| javascript | 62 | 21.0% | 0.0% | 4.8% | 74.2% |
| python | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
