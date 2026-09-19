# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-hlasm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/eclipse-che4z/che-che4z-lsp-for-hlasm.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 849 analyzed artifact(s), 114047 LOC.
- **Load-bearing artifact:** `parser_library/test/common_testing.h` -- 89 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `parser_library/src/workspace_manager.cpp` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `parser_library/src/parsing/parser_impl.cpp` at magnitude 2299.46 (structural weight, not risk).
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
| Total Artifacts | 1090 |
| Analyzed Artifacts (Scanned) | 849 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 241 |
| Total LOC | 114047 |
| Volatility Index | 0.382 |
| % Scanned of codebase = | 77.9% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.57 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0981 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7214 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 67 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 623 | 103425 | 73.4% |
| TYPESCRIPT | 80 | 8683 | 9.4% |
| PLAINTEXT | 60 | 0 | 7.1% |
| HLASM | 34 | 352 | 4.0% |
| SHELL | 14 | 111 | 1.6% |
| JSON | 13 | 997 | 1.5% |
| M4 | 11 | 118 | 1.3% |
| MARKDOWN | 8 | 0 | 0.9% |
| LUA | 3 | 113 | 0.4% |
| JAVASCRIPT | 2 | 203 | 0.2% |
| YAML | 1 | 45 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.187`
> **Composition Archetype:** `Hub-Coupled App` (z +2.19; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 22%, Data / Markup / Trivial 15%, Large Core Modules (3) 14%, State Mutators Files 13%, Large Core Modules (2) 13%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 781 | 92.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 68 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 241*

**Composition by Extension & Reason:**
- `.snap`: 54x Unsupported Format (.snap)
- `.listing`: 44x Unsupported Format (.listing)
- `no_extension`: 29x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9592 LOC)
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.output`: 5x Excluded (Unsupported Extension: '.output')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 4x Excluded (Unsupported Extension: '.cmake')
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.cpp`: 1x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 100 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 2221 commas in 657 LOC)
- `.ts`: 1x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 34 exceeds 500 chars)
- `.lua`: 1x Excluded (Machine-Generated Source Code Signature: 34 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.2 | 6.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 28.1 | 4.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 37.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 11920 | 441 | 37 | `parser_library/test/parsing/string_test.cpp` |
| cleanup | 159 | 50 | 0 | `language_server/test/dap/dap_feature_test.cpp` |
| guards | 15826 | 613 | 48 | `parser_library/src/parsing/parser_impl.cpp` |
| danger | 380 | 86 | 1 | `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` |
| concurrency | 1326 | 92 | 1 | `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` |
| connectivity | 1007 | 304 | 3 | `clients/vscode-hlasmplugin/src/test/mocks.ts` |
| io | 361 | 43 | 0 | `utils/src/emscripten_path.cpp` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 5 | 0 | `scripts/toolchain.sh` |
| time | 37 | 15 | 0 | `clients/vscode-hlasmplugin/src/connectionPool.ts` |
| serialization | 825 | 82 | 0 | `language_server/test/dap/dap_feature_test.cpp` |
| regex | 227 | 44 | 0 | `parser_library/test/workspace/wildcard2regex_test.cpp` |
| events | 102 | 31 | 0 | `language_server/src/lsp/lsp_server.cpp` |
| tests | 7939 | 181 | 21 | `utils/test/resource_location_test.cpp` |
| docs | 306 | 27 | 0 | `utils/test/resource_location_test.cpp` |
| debt | 223 | 94 | 1 | `clients/vscode-hlasmplugin/src/test/suite/hlasmExternalFiles.test.ts` |
| mutation | 15488 | 571 | 48 | `parser_library/test/checking/asm_instr_check_test.cpp` |
| dead_code | 2324 | 264 | 7 | `parser_library/src/diagnostic_op.cpp` |
| credential | 10 | 9 | 0 | `utils/src/encoding.cpp` |
| threat | 434 | 307 | 1 | `parser_library/src/instructions/instruction.cpp` |
| ml_ai | 16 | 7 | 0 | `clients/vscode-hlasmplugin/src/customEditorCommands.ts` |
| ui | 24 | 2 | 0 | `clients/vscode-hlasmplugin/scripts/syntaxes/tmgrammarGenerator.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **5.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `utils/src/emscripten_path.cpp` (Hits: 48)
- `utils/src/native_path.cpp` (Hits: 39)
- `clients/vscode-hlasmplugin/src/hlasmExternalFiles.ts` (Hits: 31)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common_testing.h** (`parser_library/test/common_testing.h`) — 89 inbound connections
2. **hlasm_context.h** (`parser_library/src/context/hlasm_context.h`) — 67 inbound connections
3. **resource_location.h** (`utils/include/utils/resource_location.h`) — 61 inbound connections
4. **platform.h** (`utils/include/utils/platform.h`) — 34 inbound connections
5. **range.h** (`parser_library/include/range.h`) — 31 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **workspace_manager.cpp** (`parser_library/src/workspace_manager.cpp`) — 42 outbound dependencies
2. **debugger.cpp** (`parser_library/src/debugging/debugger.cpp`) — 41 outbound dependencies
3. **parser_impl.cpp** (`parser_library/src/parsing/parser_impl.cpp`) — 35 outbound dependencies
4. **db2_preprocessor.cpp** (`parser_library/src/processing/preprocessors/db2_preprocessor.cpp`) — 34 outbound dependencies
5. **asm_processor.cpp** (`parser_library/src/processing/instruction_sets/asm_processor.cpp`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processListing` **(Many-Argument Workhorses)** (@ `clients/vscode-hlasmplugin/src/hlasmListingServices.ts`) -> Impact: **194.7** | LOC: 293
- `check_nominal` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/data_definition/data_instruction.cpp`) -> Impact: **167.9** | LOC: 130
- `updateCommonSection` **(Many-Argument Workhorses)** (@ `clients/vscode-hlasmplugin/src/hlasmListingServices.ts`) -> Impact: **166.3** | LOC: 277
- `assembler_instruction::check_assembler_process_operand` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/asm_instr_class.cpp`) -> Impact: **164.0** | LOC: 301
- `splitFailed` **(Callbacks & Closures)** (@ `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts`) -> Impact: **154.9** | LOC: 559
- `opencode_provider::process_ordinary` **(Many-Argument Workhorses)** (@ `parser_library/src/processing/opencode_provider.cpp`) -> Impact: **106.6** | LOC: 123
- `using_collection::using_context::evaluate` **(Many-Argument Workhorses)** (@ `parser_library/src/context/using.cpp`) -> Impact: **103.8** | LOC: 119
- `ca_function::evaluate` **(Compute Cores)** (@ `parser_library/src/expressions/conditional_assembly/terms/ca_function.cpp`) -> Impact: **99.0** | LOC: 114
- `xattr::check` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/asm_instr_check.cpp`) -> Impact: **92.2** | LOC: 123
- `check_operands` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/machine_check.cpp`) -> Impact: **89.7** | LOC: 79

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `clients/vscode-hlasmplugin/src` | 45 | 5711.4 | 47.66% | 5.53% |
| `clients/vscode-hlasmplugin/src/test/suite` | 28 | 3597.2 | 42.86% | 0.0% |
| `parser_library/src/workspaces` | 25 | 2862.24 | 23.51% | 35.47% |
| `parser_library/src/parsing` | 3 | 2311.96 | 11.56% | 35.1% |
| `parser_library/src/checking` | 18 | 2273.96 | 10.04% | 21.14% |
| `parser_library/src/context/ordinary_assembly` | 33 | 2086.1 | 20.21% | 38.7% |
| `parser_library/src/context` | 34 | 1991.76 | 17.25% | 29.12% |
| `parser_library/src/processing/instruction_sets` | 16 | 1933.02 | 14.94% | 24.67% |
| `parser_library/src/lsp` | 19 | 1893.06 | 18.03% | 20.73% |
| `parser_library/test/processing` | 24 | 1856.9 | 1.34% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `language_server/src/native_server_streams.cpp` -> **100.0%** Exposure
- `parser_library/src/context/macro_param_data.cpp` -> **100.0%** Exposure
- `parser_library/src/context/ordinary_assembly/dependency_solver_redirect.cpp` -> **100.0%** Exposure
- `parser_library/src/diagnostic_op.cpp` -> **100.0%** Exposure
- `parser_library/src/error_messages.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `parser_library/src/config/b4g_config.cpp` -> **100.0%** Exposure
- `parser_library/src/config/pgm_conf.cpp` -> **100.0%** Exposure
- `parser_library/src/config/proc_grps.cpp` -> **100.0%** Exposure
- `parser_library/src/lexing/tools.cpp` -> **100.0%** Exposure
- `parser_library/src/workspaces/file.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `parser_library/src/diagnostic_op.cpp` -> **345** Orphaned Functions | **0** Duplicates
- `parser_library/src/parsing/parser_impl.cpp` -> **115** Orphaned Functions | **0** Duplicates
- `parser_library/src/semantics/operand_impls.cpp` -> **67** Orphaned Functions | **0** Duplicates
- `parser_library/src/context/hlasm_context.cpp` -> **63** Orphaned Functions | **0** Duplicates
- `parser_library/src/expressions/mach_expr_term.cpp` -> **62** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3559` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `parser_library/src/parsing/parser_impl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2299.46 | **LOC:** 4622 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.7%), Debt Markers (formerly Tech Debt) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.7%)
- **Documentation Coverage:** 98.3425% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parser2::lex_macro_operand` **(Many-Argument Workhorses)** (Impact: 86.0)
  * `parser2::try_model_ops` **(Compute Cores)** (Impact: 68.4)
  * `parser2::parse_self_def_term_in_mach` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `parser2::op_rem_body_deferred` **(Compute Cores)** (Impact: 53.5)
  * `parser2::macro_ops` **(Compute Cores)** (Impact: 52.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 613
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1032`, `structural_boundaries: 1024`, `args: 200`, `func_start: 180`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 229`, `planned_debt: 6`, `unreferenced_by_name: 115`
* *Architecture:* `api: 2`, `import: 35`
* *Defense:* `safety: 129`, `doc: 2`, `immutability_locks: 319`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` algorithm, charconv, data_def_type_base.h, concepts, hlasm_context.h, literal_pool.h, well_known.h, cstdint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/vscode-hlasmplugin/src/hlasmListingServices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1091.6 | **LOC:** 907 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 1.036; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Guard Balance (formerly Safety Score) (92.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processListing` **(Many-Argument Workhorses)** (Impact: 194.7)
  * `updateCommonSection` **(Many-Argument Workhorses)** (Impact: 166.3)
  * `createSectionMap` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `isolateSymbol` **(Compute Cores)** (Impact: 54.4)
  * `createListingServices` **(Defensive Guards)** (Impact: 41.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 140`, `args: 61`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.036
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00481
  * `Imports (Out-Degree: 1):` constants, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `parser_library/src/checking/asm_instr_check.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 979.22 | **LOC:** 1397 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xattr::check` **(Many-Argument Workhorses)** (Impact: 92.2)
  * `cattr::check` **(Many-Argument Workhorses)** (Impact: 71.3)
  * `acontrol::check` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `stack_instr::check` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `ictl::check` **(Many-Argument Workhorses)** (Impact: 47.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 244`, `args: 64`, `func_start: 61`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 2`, `unreferenced_by_name: 60`
* *Architecture:* `import: 7`
* *Defense:* `safety: 32`, `test: 1`, `immutability_locks: 216`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` array, asm_instr_check.h, checker_helper.h, diagnostic_collector.h, tools.h, regex, string_operations.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/preprocessors/db2_preprocessor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 975.5 | **LOC:** 1216 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_args` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `generate_replacement` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `process_sql_type_operands` **(Many-Argument Workhorses)** (Impact: 32.0)
  * `lob_info` **(Compute Cores)** (Impact: 31.2)
  * `find_start_of_line_comment` **(Compute Cores)** (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 167`, `args: 50`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `state_mutation: 242`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 34`
* *Defense:* `safety: 16`, `test: 3`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` algorithm, array, cassert, cctype, concepts, diagnostic_consumer.h, document.h, initializer_list...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/instruction_sets/asm_processor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 921.48 | **LOC:** 1614 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%), Mutation Surface (formerly State Flux) (36.6%), Debt Markers (formerly Tech Debt) (30.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asm_processor::process_ORG` **(Compute Cores)** (Impact: 60.2)
  * `asm_processor::handle_cattr_ops` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `asm_processor::process_EQU` **(Compute Cores)** (Impact: 52.7)
  * `asm_processor::process_data_instruction` **(Compute Cores)** (Impact: 51.4)
  * `asm_processor::process_MNOTE` **(Compute Cores)** (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 310`, `args: 57`, `func_start: 57`, `class_start: 3`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 7`, `unreferenced_by_name: 11`
* *Architecture:* `import: 33`
* *Defense:* `safety: 20`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` analyzing_context.h, asm_processor.h, charconv, asm_instr_check.h, diagnostic_collector.h, common_types.h, hlasm_context.h, literal_pool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/workspaces/workspace_configuration.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 919.32 | **LOC:** 1333 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Concurrency Surface (formerly Concurrency) (88.6%), Debt Markers (formerly Tech Debt) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `workspace_configuration::find_and_add_libs` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `workspace_configuration::load_proc_config` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `workspace_configuration::load_pgm_config` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `workspace_configuration::load_alternative_config_if_needed` **(Defensive Guards)** (Impact: 30.1)
  * `workspace_configuration::refresh_libraries` **(Compute Cores)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 91 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 216`, `args: 63`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `planned_debt: 3`, `unreferenced_by_name: 31`
* *Architecture:* `io: 2`, `concurrency: 17`, `import: 33`
* *Defense:* `safety: 47`, `immutability_locks: 166`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` algorithm, array, atomic, charconv, compare, compiler_options.h, deque, diagnostic_op.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 790.2 | **LOC:** 778 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.689; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (99.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitFailed` **(Callbacks & Closures)** (Impact: 154.9)
  * `adjustJobHeader` **(Compute Cores)** (Impact: 22.8)
  * `generateJobHeader` **(Compute Cores)** (Impact: 11.0)
  * `basicFtpJobClient` **(Callbacks & Closures)** (Impact: 10.9)
  * `prepareJobHeader` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 342
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 279`, `args: 118`, `func_start: 69`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 57`, `planned_debt: 1`
* *Architecture:* `io: 23`, `api: 17`, `concurrency: 132`, `import: 16`
* *Defense:* `safety: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.689
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.003681
  * `Imports (Out-Degree: 11):` FBStreamingConvertor, constants, eventsHandler, extension, helpers, mfCreds, serverFactory.common, telemetry...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `parser_library/src/diagnostic_op.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 774.84 | **LOC:** 2709 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Dead Code Surface (formerly Dead Code) (7.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagnostic_op::error_optional_number_of_operands` **(Compute Cores)** (Impact: 11.7)
  * `diagnostic_op::mnote_diagnostic` **(Compute Cores)** (Impact: 10.4)
  * `diagnostic_op::ext_diagnostic` **(Compute Cores)** (Impact: 9.4)
  * `diagnostic_op::error_U005_invalid_range` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `diagnostic_op::error_D008` **(Many-Argument Workhorses)** (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 361`, `args: 137`, `func_start: 347`
* *Risk/State:* `state_mutation: 1`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 345`
* *Architecture:* `import: 5`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` diagnostic_op.h, type_traits, concat.h, resource_location.h, unicode_text.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/vscode-hlasmplugin/src/test/suite/hlasmListingServices.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 771.11 | **LOC:** 259 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (44.4%), Guard Balance (formerly Safety Score) (43.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 16`, `func_start: 8`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `concurrency: 11`, `import: 3`
* *Defense:* `safety: 9`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hlasmListingServices, assert, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/workspaces/workspace.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 768.12 | **LOC:** 1154 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.3%), Mutation Surface (formerly State Flux) (98.3%), Concurrency Surface (formerly Concurrency) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter_and_emplace_mac_cpy_definitions` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `generate_merged_fade_messages` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `parse_library` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* // Inherited via parse_lib_provider
  * `workspace::did_close_file` **(Defensive Guards)** (Impact: 26.4)
  * `workspace::did_change_watched_files` **(Many-Argument Workhorses)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 235`, `args: 53`, `func_start: 55`, `class_start: 6`
* *Risk/State:* `state_mutation: 88`, `dead_code: 5`, `planned_debt: 6`, `unreferenced_by_name: 37`
* *Architecture:* `concurrency: 15`, `import: 31`
* *Defense:* `safety: 43`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` algorithm, analyzer.h, cassert, completion_item.h, completion_trigger_kind.h, hlasm_context.h, document_symbol_item.h, fade_messages.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/context/hlasm_context.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 726.32 | **LOC:** 1239 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (97.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_var_sym_value` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `hlasm_context::find_opcode_mnemo` **(Compute Cores)** (Impact: 35.9)
  * `hlasm_context::add_scoped_system_variables` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `hlasm_context::init_instruction_map` **(Compute Cores)** (Impact: 19.4)
  * `hlasm_context::get_attribute_value_ord` **(Compute Cores)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 354`, `args: 64`, `func_start: 117`, `class_start: 6`
* *Risk/State:* `state_mutation: 94`, `unreferenced_by_name: 63`
* *Architecture:* `api: 1`, `import: 25`
* *Defense:* `safety: 37`, `immutability_locks: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` id_storage.h, well_known.h, ctime, diagnostic_tools.h, ebcdic_encoding.h, evaluation_context.h, mach_expression.h, external_functions.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/vscode-hlasmplugin/src/hlasmExternalFiles.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 672.2 | **LOC:** 776 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 2.054; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (95.9%), Complexity Load (formerly Cognitive Load) (93.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearCache` **(Defensive Guards)** (Impact: 49.9)
  * `extractUriDetails` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `clearCacheByPredicate` **(Defensive Guards)** (Impact: 21.0)
  * `setClient` **(Defensive Guards)** (Impact: 19.2)
  * `getCachedResult` **(Stateful Encapsulated Methods)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 256`, `args: 111`, `func_start: 57`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 34`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 31`, `api: 19`, `concurrency: 88`, `import: 8`
* *Defense:* `safety: 43`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.054
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.009977
  * `Imports (Out-Degree: 5):` eventsHandler, helpers, serverFactory.common, tools, tools.common, uriUtils, vscode, vscode-languageclient
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `parser_library/src/expressions/conditional_assembly/terms/ca_function.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 653.72 | **LOC:** 758 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.1%), Guard Balance (formerly Safety Score) (89.4%), Complexity Load (formerly Cognitive Load) (84.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ca_function::evaluate` **(Compute Cores)** (Impact: 99.0)
  * `ca_function::get_undefined_attributed_symbols` **(Compute Cores)** (Impact: 20.4)
  * `ca_function::resolve_expression_tree` **(Compute Cores)** (Impact: 18.6)
  * `ca_function::B2C` **(Compute Cores)** (Impact: 15.6)
  * `ca_function::B2X` **(Compute Cores)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 134`, `args: 22`, `func_start: 45`
* *Risk/State:* `state_mutation: 74`, `unreferenced_by_name: 44`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` bitset, ca_function.h, ca_string.h, cassert, charconv, hlasm_context.h, ebcdic_encoding.h, ca_expr_visitor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/lsp/lsp_context.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 630.38 | **LOC:** 837 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.8%), Guard Balance (formerly Safety Score) (75.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lsp_context::document_symbol` **(Compute Cores)** (Impact: 87.5)
  * `lsp_context::find_hover` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `lsp_context::find_definition_location` **(Many-Argument Workhorses)** (Impact: 68.1)
  * `compute_reachable_symbol_set` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `lsp_context::completion` **(Many-Argument Workhorses)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 215`, `args: 26`, `func_start: 31`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 26`
* *Architecture:* `import: 18`
* *Defense:* `safety: 6`, `immutability_locks: 129`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` cassert, completion_trigger_kind.h, hlasm_context.h, macro.h, section.h, using.h, document_symbol_item.h, instruction.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/preprocessors/cics_preprocessor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 615.68 | **LOC:** 1403 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (48.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_and_substitute` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `process_asm_statement` **(Compute Cores)** (Impact: 31.4)
  * `generate_replacement` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* // Inherited via preprocessor
  * `try_dfh_lookup` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `try_exec_cics` **(Many-Argument Workhorses)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 112`, `args: 37`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `state_mutation: 108`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 3`, `import: 30`
* *Defense:* `safety: 10`, `immutability_locks: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` algorithm, array, cassert, charconv, diagnostic.h, diagnostic_consumer.h, document.h, logical_line.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/checking/data_definition/data_instruction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 615.6 | **LOC:** 678 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_nominal` **(Many-Argument Workhorses)** (Impact: 167.9)
  * `check_data_instruction_operands` **(Many-Argument Workhorses)** (Impact: 56.2)
  * `check_S_SY_operand` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `check_q_nominal` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `check_base` **(Many-Argument Workhorses)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 117`, `args: 12`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `import: 14`
* *Defense:* `safety: 13`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` data_check.h, asm_instr_check.h, checker_helper.h, diagnostic_collector.h, using_label_checker.h, compiler_options.h, section.h, symbol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/workspace_manager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 596.34 | **LOC:** 1229 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.6%), Mutation Surface (formerly State Flux) (94.2%), Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `idle_handler` **(Compute Cores)** (Impact: 31.1)
  * `list_directory_files_external` **(Defensive Guards)** (Impact: 18.3)
  * `perform_action` **(I/O & Config Routines)** (Impact: 14.8)
  * `did_change_watched_files` **(Defensive Guards)** (Impact: 13.6)
  * `did_change_file` **(Many-Argument Workhorses)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 277`, `args: 108`, `func_start: 81`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 90`, `planned_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 43`
* *Defense:* `safety: 77`, `immutability_locks: 110`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` algorithm, atomic, charconv, chrono, completion_item.h, debugger_configuration.h, deque, document_symbol_item.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/opencode_provider.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 579.96 | **LOC:** 954 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Debt Markers (formerly Tech Debt) (82.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `opencode_provider::process_ordinary` **(Many-Argument Workhorses)** (Impact: 106.6)
  * `opencode_provider::get_next` **(Compute Cores)** (Impact: 39.7)
  * `opencode_provider::process_lookahead` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `opencode_provider::extract_next_logical_line` **(I/O & Config Routines)** (Impact: 22.4)
  * `opencode_provider::suspend_copy_processing` **(Compute Cores)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 188`, `args: 30`, `func_start: 36`
* *Risk/State:* `state_mutation: 60`, `dead_code: 2`, `unreferenced_by_name: 31`
* *Architecture:* `concurrency: 4`, `import: 16`
* *Defense:* `safety: 12`, `immutability_locks: 81`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` algorithm, analyzer.h, hlasm_context.h, well_known.h, format, library_info_transitional.h, lsp_context.h, opencode_provider.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/debugging/debugger.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 543.9 | **LOC:** 809 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Debt Markers (formerly Tech Debt) (94.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyze` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `evaluate` **(Compute Cores)** (Impact: 55.2)
  * `evaluate_exact_match` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `to_string` **(Compute Cores)** (Impact: 24.8)
  * `scopes` **(Compute Cores)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 156`, `args: 46`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `state_mutation: 68`, `planned_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 41`
* *Defense:* `safety: 24`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` algorithm, analyzer.h, atomic, hlasm_context.h, ordinary_assembly_dependency_solver.h, system_variable.h, well_known.h, debug_lib_provider.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/statement_analyzers/lsp_analyzer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 507.7 | **LOC:** 676 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.7%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lsp_analyzer::analyze` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `lsp_analyzer::collect_branch_info` **(Compute Cores)** (Impact: 46.2)
  * `lsp_analyzer::collect_occurrence` **(Compute Cores)** (Impact: 37.3)
  * `get_branch_operand` **(Compute Cores)** (Impact: 23.2)
  * `lsp_analyzer::collect_occurrence` **(Compute Cores)** (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 137`, `args: 13`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `unreferenced_by_name: 21`
* *Architecture:* `import: 27`
* *Defense:* `safety: 9`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` algorithm, array, hlasm_context.h, ordinary_assembly_dependency_solver.h, postponed_statement.h, symbol_dependency_tables.h, source_context.h, special_instructions.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/context/ordinary_assembly/symbol_dependency_tables.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 503.5 | **LOC:** 882 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.8%), Complexity Load (formerly Cognitive Load) (65.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `symbol_dependency_tables::check_loctr_cycle` **(Compute Cores)** (Impact: 33.9)
  * `resolve_unknown_loctr_dependency` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `symbol_dependency_tables::update_dependencies` **(Compute Cores)** (Impact: 33.6)
  * `symbol_dependency_tables::has_cycle` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `symbol_dependency_tables::extract_dependencies` **(Many-Argument Workhorses)** (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 193`, `args: 39`, `func_start: 67`, `class_start: 6`
* *Risk/State:* `state_mutation: 70`, `planned_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `safety: 45`, `immutability_locks: 120`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` algorithm, array, cassert, cstddef, deque, diagnostic_tools.h, functional, location_counter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utils/src/resource_location.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 493.24 | **LOC:** 648 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Debt Markers (formerly Tech Debt) (92.3%), Guard Balance (formerly Safety Score) (86.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_path` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `remove_dot_segments` **(Compute Cores)** (Impact: 36.4)
    * *Intent:* // Algorithm from RFC 3986
  * `resource_location::relative_reference_resolution` **(Compute Cores)** (Impact: 36.0)
  * `resource_location::lexically_relative` **(Compute Cores)** (Impact: 25.5)
  * `windows_normalization_data` **(Defensive Guards)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 98`, `args: 31`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `planned_debt: 3`, `unreferenced_by_name: 15`
* *Architecture:* `import: 12`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` algorithm, array, assert.h, cstddef, iterator, regex, utility, encoding.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/checking/asm_instr_class.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 489.74 | **LOC:** 861 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.5%), Debt Markers (formerly Tech Debt) (36.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assembler_instruction::check_assembler_process_operand` **(Many-Argument Workhorses)** (Impact: 164.0)
  * `assembler_instruction::check_using_parameters` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `assembler_instruction::check_fail_parameters` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `assembler_instruction::check_codepage_parameter` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* // process instruction functions
  * `assembler_instruction::operands_size_corresponding` **(Compute Cores)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 112`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 15`
* *Architecture:* `import: 7`
* *Defense:* `safety: 13`, `test: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` array, asm_instr_class.h, charconv, checker_helper.h, diagnostic_collector.h, optional, string_view
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/test/checking/asm_instr_check_test.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 472.04 | **LOC:** 1087 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (1.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instruction_test` **(Type Conversions)** (Impact: 30.4)
  * `instruction_test` **(State Mutators)** (Impact: 2.9)
  * `instruction_test` **(State Mutators)** (Impact: 2.5)
  * `instruction_test` **(State Mutators)** (Impact: 2.5)
  * `instruction_test` **(State Mutators)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 74`, `args: 119`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 357`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 55`, `test: 150`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` diagnostic_collector.h, instr_operand.h, instruction_checker.h, gtest.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/lsp/item_convertors.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 455.9 | **LOC:** 680 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.544; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hover_text` **(Compute Cores)** (Impact: 55.0)
  * `append_hover_text` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `generate_completion` **(Compute Cores)** (Impact: 31.0)
  * `get_macro_documentation` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `generate_completion` **(Many-Argument Workhorses)** (Impact: 19.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 100`, `args: 22`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 2`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` completion_item.h, concepts, hlasm_context.h, section.h, symbol.h, sequence_symbol.h, using.h, ebcdic_encoding.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `benchmark/diagnostic_counter.h` -> Churn: **100.0%** | Cog Load: 57.9151% | Debt: 0.0%
- `language_server/src/base_protocol_channel.cpp` -> Churn: **100.0%** | Cog Load: 13.6108% | Debt: 75.026%
- `language_server/src/dap/dap_feature.cpp` -> Churn: **100.0%** | Cog Load: 23.4033% | Debt: 86.7227%
- `language_server/src/dap/dap_message_wrappers.cpp` -> Churn: **100.0%** | Cog Load: 6.9138% | Debt: 92.4142%
- `language_server/src/dap/dap_server.cpp` -> Churn: **100.0%** | Cog Load: 16.7041% | Debt: 99.9718%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `clients/vscode-hlasmplugin/src/hlasmListingServices.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 1091.6
- `parser_library/src/checking/asm_instr_check.cpp` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 979.22
- `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 790.2
- `clients/vscode-hlasmplugin/src/test/suite/hlasmListingServices.test.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 771.11
- `parser_library/src/context/hlasm_context.cpp` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 726.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `parser_library/src/context/ordinary_assembly/dependable.h` -> **Severity: 0.032** (Bridge: 0.0007 * Flux: 42.5%)
- `clients/vscode-hlasmplugin/src/extension.ts` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 99.9991%)
- `parser_library/include/analyzer.h` -> **Severity: 0.021** (Bridge: 0.0009 * Flux: 22.8429%)
- `parser_library/src/expressions/conditional_assembly/ca_expression.h` -> **Severity: 0.009** (Bridge: 0.0006 * Flux: 14.259%)
- `parser_library/src/context/source_snapshot.h` -> **Severity: 0.007** (Bridge: 0.0002 * Flux: 36.2818%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `parser_library/include/diagnostic.h` -> **Severity: 6.602** (Embedded: 0.1148 * Error Risk: 57.5183%)
- `parser_library/include/protocol.h` -> **Severity: 5.508** (Embedded: 0.1188 * Error Risk: 46.3773%)
- `parser_library/include/compiler_options.h` -> **Severity: 5.453** (Embedded: 0.0845 * Error Risk: 64.5656%)
- `utils/include/utils/resource_location.h` -> **Severity: 5.367** (Embedded: 0.1315 * Error Risk: 40.8058%)
- `parser_library/src/context/id_index.h` -> **Severity: 4.799** (Embedded: 0.1214 * Error Risk: 39.5374%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `parser_library/include/range.h` -> **Severity: 4114.0** (Blast Radius: 41.14 * Doc Risk: 100.0%)
- `parser_library/src/context/id_index.h` -> **Severity: 1669.9** (Blast Radius: 16.699 * Doc Risk: 100.0%)
- `parser_library/test/common_testing.h` -> **Severity: 1634.6** (Blast Radius: 16.346 * Doc Risk: 100.0%)
- `utils/include/utils/insist.h` -> **Severity: 1561.9** (Blast Radius: 15.619 * Doc Risk: 100.0%)
- `utils/include/utils/resource_location.h` -> **Severity: 1442.2** (Blast Radius: 14.422 * Doc Risk: 100.0%)

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
