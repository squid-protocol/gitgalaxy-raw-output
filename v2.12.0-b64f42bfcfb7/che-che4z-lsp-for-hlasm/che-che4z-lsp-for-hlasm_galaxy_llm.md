# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-hlasm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/eclipse-che4z/che-che4z-lsp-for-hlasm.git` |
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
- **Scope:** 865 analyzed artifact(s), 116026 LOC.
- **Load-bearing artifact:** `parser_library/test/common_testing.h` -- 89 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `parser_library/src/workspace_manager.cpp` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `parser_library/src/parsing/parser_impl.cpp` at magnitude 2399.96 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 865 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 225 |
| Total LOC | 116026 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.4% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.555 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1122 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6824 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 39 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 626 | 104544 | 72.4% |
| TYPESCRIPT | 82 | 8802 | 9.5% |
| PLAINTEXT | 64 | 0 | 7.4% |
| HLASM | 34 | 352 | 3.9% |
| SHELL | 14 | 111 | 1.6% |
| JSON | 13 | 997 | 1.5% |
| M4 | 11 | 118 | 1.3% |
| MARKDOWN | 10 | 0 | 1.2% |
| YAML | 5 | 764 | 0.6% |
| LUA | 4 | 135 | 0.5% |
| JAVASCRIPT | 2 | 203 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 865 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 21%, Data / Markup / Trivial 16%, Large Core Modules (3) 14%, Large Core Modules (2) 13%, State Mutators Files 13%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 791 | 91.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 74 | 8.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 225*

**Composition by Extension & Reason:**
- `.snap`: 54x Unsupported Format (.snap)
- `.listing`: 44x Unsupported Format (.listing)
- `no_extension`: 29x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9592 LOC)
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.output`: 5x Excluded (Unsupported Extension: '.output')
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dict`: 1x Excluded (Unsupported Extension: '.dict')
- `.thh`: 1x Excluded (Embedded Array/Matrix Payload: 12808 commas in 2951 LOC)
- `.tokens`: 1x Unsupported Format (.tokens)
- `.in`: 1x Excluded (Embedded Array/Matrix Payload: 2012 commas in 526 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.8 | 6.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 25.9 | 29.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1809 | 232 | 4 | `parser_library/test/checking/asm_instr_check_test.cpp` |
| cleanup | 159 | 50 | 0 | `language_server/test/dap/dap_feature_test.cpp` |
| guards | 15865 | 618 | 48 | `parser_library/src/parsing/parser_impl.cpp` |
| danger | 389 | 90 | 1 | `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` |
| concurrency | 1329 | 93 | 1 | `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` |
| connectivity | 1015 | 312 | 3 | `clients/vscode-hlasmplugin/src/test/mocks.ts` |
| io | 370 | 46 | 0 | `utils/src/emscripten_path.cpp` |
| crypto | 1 | 1 | 0 | `clients/vscode-hlasmplugin/src/tools.ts` |
| ipc | 9 | 5 | 0 | `scripts/toolchain.sh` |
| time | 37 | 15 | 0 | `clients/vscode-hlasmplugin/src/connectionPool.ts` |
| serialization | 855 | 85 | 0 | `language_server/test/dap/dap_feature_test.cpp` |
| regex | 231 | 45 | 0 | `parser_library/test/workspace/wildcard2regex_test.cpp` |
| events | 113 | 33 | 0 | `language_server/src/lsp/lsp_server.cpp` |
| tests | 8062 | 186 | 22 | `utils/test/resource_location_test.cpp` |
| docs | 604 | 34 | 0 | `language_server/test/regress_test.cpp` |
| debt | 269 | 100 | 1 | `clients/vscode-hlasmplugin/src/test/suite/hlasmExternalConfigurationProvider.test.ts` |
| mutation | 15645 | 580 | 48 | `parser_library/test/checking/asm_instr_check_test.cpp` |
| dead_code | 4352 | 355 | 13 | `parser_library/src/diagnostic_op.cpp` |
| credential | 10 | 9 | 0 | `utils/src/encoding.cpp` |
| threat | 13 | 4 | 0 | `clients/vscode-hlasmplugin/src/branchDecorator.ts` |
| ml_ai | 19 | 9 | 0 | `clients/vscode-hlasmplugin/src/customEditorCommands.ts` |
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
2. **analyzer.h** (`parser_library/include/analyzer.h`) — 84 inbound connections
3. **range.h** (`parser_library/include/range.h`) — 80 inbound connections
4. **resource_location.h** (`utils/include/utils/resource_location.h`) — 71 inbound connections
5. **hlasm_context.h** (`parser_library/src/context/hlasm_context.h`) — 67 inbound connections

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
- `assembler_instruction::check_assembler_process_operand` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/asm_instr_class.cpp`) -> Impact: **164.0** | LOC: 301
- `opencode_provider::process_ordinary` **(Many-Argument Workhorses)** (@ `parser_library/src/processing/opencode_provider.cpp`) -> Impact: **106.6** | LOC: 123
- `using_collection::using_context::evaluate` **(Many-Argument Workhorses)** (@ `parser_library/src/context/using.cpp`) -> Impact: **103.8** | LOC: 119
- `ca_function::evaluate` **(Compute Cores)** (@ `parser_library/src/expressions/conditional_assembly/terms/ca_function.cpp`) -> Impact: **99.0** | LOC: 114
- `xattr::check` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/asm_instr_check.cpp`) -> Impact: **92.2** | LOC: 123
- `check_operands` **(Many-Argument Workhorses)** (@ `parser_library/src/checking/machine_check.cpp`) -> Impact: **89.7** | LOC: 79
- `lsp_context::document_symbol` **(Compute Cores)** (@ `parser_library/src/lsp/lsp_context.cpp`) -> Impact: **87.5** | LOC: 195
- `parser2::lex_macro_operand` **(Many-Argument Workhorses)** (@ `parser_library/src/parsing/parser_impl.cpp`) -> Impact: **86.0** | LOC: 79

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `clients/vscode-hlasmplugin/src` | 47 | 5328.18 | 47.57% | 5.75% |
| `clients/vscode-hlasmplugin/src/test/suite` | 28 | 3230.5 | 39.13% | 0.0% |
| `parser_library/src/workspaces` | 25 | 2846.04 | 22.74% | 33.68% |
| `parser_library/src/parsing` | 3 | 2412.46 | 11.56% | 33.46% |
| `parser_library/src/checking` | 18 | 2271.96 | 10.04% | 18.96% |
| `parser_library/src/context/ordinary_assembly` | 33 | 2088.5 | 20.21% | 38.46% |
| `parser_library/src/context` | 34 | 2004.06 | 17.27% | 27.07% |
| `parser_library/src/processing/instruction_sets` | 16 | 1967.22 | 14.94% | 25.7% |
| `parser_library/src/lsp` | 19 | 1891.36 | 18.02% | 19.04% |
| `parser_library/src` | 29 | 1835.62 | 9.35% | 38.38% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `language_server/src/feature.cpp` -> **100.0%** Exposure
- `language_server/src/native_server_streams.cpp` -> **100.0%** Exposure
- `parser_library/src/context/macro_param_data.cpp` -> **100.0%** Exposure
- `parser_library/src/context/ordinary_assembly/dependency_solver_redirect.cpp` -> **100.0%** Exposure
- `parser_library/src/diagnostic_op.cpp` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `parser_library/src/config/b4g_config.cpp` -> **100.0%** Exposure
- `parser_library/src/config/pgm_conf.cpp` -> **100.0%** Exposure
- `parser_library/src/config/proc_grps.cpp` -> **100.0%** Exposure
- `parser_library/src/lexing/tools.cpp` -> **100.0%** Exposure
- `parser_library/src/workspaces/file.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `parser_library/src/diagnostic_op.cpp` -> **345** Orphaned Functions | **0** Duplicates
- `parser_library/src/parsing/parser_impl.cpp` -> **116** Orphaned Functions | **0** Duplicates
- `parser_library/test/checking/asm_instr_diag_test.cpp` -> **105** Orphaned Functions | **0** Duplicates
- `parser_library/test/context/using_test.cpp` -> **93** Orphaned Functions | **0** Duplicates
- `parser_library/test/checking/data_definition/data_definition_check_test.cpp` -> **80** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3588` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `parser_library/src/parsing/parser_impl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.237)
- **Top Global Matches:** file_cluster_4: 6.237, file_cluster_6: 10.749, file_cluster_15: 11.539
- **Magnitude:** 2399.96 | **LOC:** 4622 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.507; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.7%), Debt Markers (formerly Tech Debt) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%)
- **Documentation Coverage:** 98.4925% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parser2::lex_macro_operand` **(Many-Argument Workhorses)** (Impact: 86.0)
  * `parser2::try_model_ops` **(Compute Cores)** (Impact: 68.4)
  * `parser2::with_model` **(Compute Cores)** (Impact: 55.8)
  * `parser2::parse_self_def_term_in_mach` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `parser2::op_rem_body_deferred` **(Compute Cores)** (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 613
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1032`, `structural_boundaries: 1024`, `args: 200`, `func_start: 192`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 229`, `dead_code: 1`, `planned_debt: 6`, `unreferenced_by_name: 116`
* *Architecture:* `api: 2`, `import: 35`
* *Defense:* `safety: 129`, `doc: 2`, `immutability_locks: 319`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.507
  * `Choke Point (Betweenness):` 0.000249 | `Ripple Effect (Closeness):` 0.002601
  * `Imports (Out-Degree: 43):` algorithm, charconv, data_def_type_base.h, concepts, hlasm_context.h, literal_pool.h, well_known.h, cstdint...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `parser_library/src/checking/asm_instr_check.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.202)
- **Top Global Matches:** file_cluster_6: 7.202, file_cluster_4: 9.387, file_cluster_15: 16.706
- **Magnitude:** 977.22 | **LOC:** 1397 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Structure:* `branch: 355`, `structural_boundaries: 244`, `args: 64`, `func_start: 61`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 2`, `unreferenced_by_name: 60`
* *Architecture:* `import: 7`
* *Defense:* `safety: 32`, `test: 1`, `immutability_locks: 216`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.582
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.001156
  * `Imports (Out-Degree: 8):` array, asm_instr_check.h, checker_helper.h, diagnostic_collector.h, tools.h, regex, string_operations.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `parser_library/src/processing/preprocessors/db2_preprocessor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.501)
- **Top Global Matches:** file_cluster_4: 5.501, file_cluster_15: 10.572, file_cluster_6: 10.888
- **Magnitude:** 957.8 | **LOC:** 1216 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.3%), Guard Balance (formerly Safety Score) (67.4%)
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
* *Structure:* `branch: 207`, `structural_boundaries: 167`, `args: 50`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `state_mutation: 242`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 34`
* *Defense:* `safety: 16`, `test: 3`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` algorithm, array, cassert, cctype, concepts, diagnostic_consumer.h, document.h, initializer_list...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/instruction_sets/asm_processor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_6: 6.639, file_cluster_4: 8.215, file_cluster_15: 15.568
- **Magnitude:** 921.48 | **LOC:** 1614 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.52; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (36.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.52
  * `Choke Point (Betweenness):` 0.000208 | `Ripple Effect (Closeness):` 0.002601
  * `Imports (Out-Degree: 38):` analyzing_context.h, asm_processor.h, charconv, asm_instr_check.h, diagnostic_collector.h, common_types.h, hlasm_context.h, literal_pool.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `clients/vscode-hlasmplugin/src/hlasmListingServices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.387)
- **Top Global Matches:** file_cluster_4: 7.387, file_cluster_6: 7.738, file_cluster_15: 14.503
- **Magnitude:** 916.3 | **LOC:** 907 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.926; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (69.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processListing` **(Many-Argument Workhorses)** (Impact: 194.7)
  * `createSectionMap` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `isolateSymbol` **(Compute Cores)** (Impact: 54.4)
  * `createListingServices` **(Defensive Guards)** (Impact: 35.6)
  * `listingAsSymbol` **(Compute Cores)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 140`, `args: 61`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004721
  * `Imports (Out-Degree: 1):` constants, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `parser_library/src/workspaces/workspace_configuration.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.886)
- **Top Global Matches:** file_cluster_4: 5.886, file_cluster_15: 9.674, file_cluster_16: 10.852
- **Magnitude:** 915.12 | **LOC:** 1333 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.533; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Concurrency Surface (formerly Concurrency) (88.6%), Debt Markers (formerly Tech Debt) (87.3%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 232`, `structural_boundaries: 216`, `args: 63`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `planned_debt: 3`, `unreferenced_by_name: 31`
* *Architecture:* `io: 2`, `concurrency: 17`, `import: 33`
* *Defense:* `safety: 47`, `immutability_locks: 166`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.533
  * `Choke Point (Betweenness):` 0.001425 | `Ripple Effect (Closeness):` 0.03295
  * `Imports (Out-Degree: 22):` algorithm, array, atomic, charconv, compare, compiler_options.h, deque, diagnostic_op.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `parser_library/src/workspaces/workspace.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.527)
- **Top Global Matches:** file_cluster_15: 6.527, file_cluster_16: 8.366, file_cluster_4: 8.587
- **Magnitude:** 768.12 | **LOC:** 1154 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **31**; blast radius 0.682; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Debt Markers (formerly Tech Debt) (98.2%), Concurrency Surface (formerly Concurrency) (93.3%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `state_mutation: 88`, `planned_debt: 6`, `unreferenced_by_name: 37`
* *Architecture:* `concurrency: 15`, `import: 31`
* *Defense:* `safety: 43`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.682
  * `Choke Point (Betweenness):` 0.001052 | `Ripple Effect (Closeness):` 0.008092
  * `Imports (Out-Degree: 34):` algorithm, analyzer.h, cassert, completion_item.h, completion_trigger_kind.h, hlasm_context.h, document_symbol_item.h, fade_messages.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `parser_library/src/diagnostic_op.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.294)
- **Top Global Matches:** file_cluster_15: 7.294, file_cluster_16: 9.157, file_cluster_11: 9.172
- **Magnitude:** 758.04 | **LOC:** 2709 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **5**; blast radius 2.477; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagnostic_op::error_optional_number_of_operands` **(Compute Cores)** (Impact: 11.7)
  * `diagnostic_op::mnote_diagnostic` **(Compute Cores)** (Impact: 10.4)
  * `diagnostic_op::ext_diagnostic` **(Compute Cores)** (Impact: 9.4)
  * `diagnostic_op::error_U005_invalid_range` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `diagnostic_op::error_D008` **(Many-Argument Workhorses)** (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 361`, `args: 137`, `func_start: 347`
* *Risk/State:* `state_mutation: 1`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 345`
* *Architecture:* `import: 5`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 353`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.477
  * `Choke Point (Betweenness):` 0.000551 | `Ripple Effect (Closeness):` 0.056333
  * `Imports (Out-Degree: 5):` diagnostic_op.h, type_traits, concat.h, resource_location.h, unicode_text.h
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `parser_library/src/context/hlasm_context.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.59)
- **Top Global Matches:** file_cluster_15: 6.59, file_cluster_11: 8.105, file_cluster_16: 8.789
- **Magnitude:** 726.32 | **LOC:** 1239 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **25**; blast radius 0.591; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.6%), Complexity Load (formerly Cognitive Load) (58.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.591
  * `Choke Point (Betweenness):` 0.000405 | `Ripple Effect (Closeness):` 0.007771
  * `Imports (Out-Degree: 30):` id_storage.h, well_known.h, ctime, diagnostic_tools.h, ebcdic_encoding.h, evaluation_context.h, mach_expression.h, external_functions.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `clients/vscode-hlasmplugin/src/hlasmExternalFiles.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.38)
- **Top Global Matches:** file_cluster_12: 9.38, file_cluster_5: 9.396, file_cluster_4: 10.134
- **Magnitude:** 655.3 | **LOC:** 776 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 1.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.9%), Complexity Load (formerly Cognitive Load) (92.6%), Debt Markers (formerly Tech Debt) (80.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearCache` **(Defensive Guards)** (Impact: 45.9)
  * `extractUriDetails` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `setClient` **(Defensive Guards)** (Impact: 19.2)
  * `clearCacheByPredicate` **(Defensive Guards)** (Impact: 19.2)
  * `getCachedResult` **(Stateful Encapsulated Methods)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 256`, `args: 111`, `func_start: 57`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 34`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 31`, `api: 19`, `concurrency: 88`, `import: 8`
* *Defense:* `safety: 43`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.621
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.009793
  * `Imports (Out-Degree: 6):` eventsHandler, helpers, serverFactory.common, tools, tools.common, uriUtils, vscode, vscode-languageclient
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `parser_library/src/expressions/conditional_assembly/terms/ca_function.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.993)
- **Top Global Matches:** file_cluster_15: 6.993, file_cluster_4: 8.702, file_cluster_16: 8.709
- **Magnitude:** 653.72 | **LOC:** 758 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.736; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.0%), Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 195`, `structural_boundaries: 134`, `args: 22`, `func_start: 45`
* *Risk/State:* `state_mutation: 74`, `unreferenced_by_name: 44`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.736
  * `Choke Point (Betweenness):` 0.001863 | `Ripple Effect (Closeness):` 0.012315
  * `Imports (Out-Degree: 12):` bitset, ca_function.h, ca_string.h, cassert, charconv, hlasm_context.h, ebcdic_encoding.h, ca_expr_visitor.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `parser_library/src/lsp/lsp_context.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.584)
- **Top Global Matches:** file_cluster_6: 7.584, file_cluster_4: 7.601, file_cluster_15: 14.582
- **Magnitude:** 630.38 | **LOC:** 837 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.497; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.6%), Complexity Load (formerly Cognitive Load) (70.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.497
  * `Choke Point (Betweenness):` 0.000135 | `Ripple Effect (Closeness):` 0.004933
  * `Imports (Out-Degree: 18):` cassert, completion_trigger_kind.h, hlasm_context.h, macro.h, section.h, using.h, document_symbol_item.h, instruction.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `parser_library/src/checking/data_definition/data_instruction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.597)
- **Top Global Matches:** file_cluster_6: 6.597, file_cluster_4: 8.56, file_cluster_15: 16.056
- **Magnitude:** 615.6 | **LOC:** 678 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (57.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` data_check.h, asm_instr_check.h, checker_helper.h, diagnostic_collector.h, using_label_checker.h, compiler_options.h, section.h, symbol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/processing/preprocessors/cics_preprocessor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.531)
- **Top Global Matches:** file_cluster_4: 5.531, file_cluster_15: 10.599, file_cluster_6: 10.686
- **Magnitude:** 604.78 | **LOC:** 1403 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **30**; blast radius 0.624; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_and_substitute` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `process_asm_statement` **(Compute Cores)** (Impact: 31.4)
  * `generate_replacement` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* // Inherited via preprocessor
  * `try_dfh_lookup` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `try_asm_xopts` **(Compute Cores)** (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 112`, `args: 37`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `state_mutation: 108`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 3`, `import: 30`
* *Defense:* `safety: 10`, `immutability_locks: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.624
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.005427
  * `Imports (Out-Degree: 21):` algorithm, array, cassert, charconv, diagnostic.h, diagnostic_consumer.h, document.h, logical_line.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `parser_library/src/workspace_manager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.79)
- **Top Global Matches:** file_cluster_15: 6.79, file_cluster_11: 8.52, file_cluster_10: 8.523
- **Magnitude:** 596.34 | **LOC:** 1229 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **42**; blast radius 1.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.3%), Mutation Surface (formerly State Flux) (94.2%), Guard Balance (formerly Safety Score) (51.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.253
  * `Choke Point (Betweenness):` 0.007061 | `Ripple Effect (Closeness):` 0.040899
  * `Imports (Out-Degree: 26):` algorithm, atomic, charconv, chrono, completion_item.h, debugger_configuration.h, deque, document_symbol_item.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `parser_library/src/processing/opencode_provider.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.098)
- **Top Global Matches:** file_cluster_4: 6.098, file_cluster_6: 10.642, file_cluster_15: 11.517
- **Magnitude:** 579.96 | **LOC:** 954 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Debt Markers (formerly Tech Debt) (81.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.8%)
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
* *Structure:* `branch: 194`, `structural_boundaries: 188`, `args: 30`, `func_start: 35`
* *Risk/State:* `state_mutation: 60`, `unreferenced_by_name: 31`
* *Architecture:* `concurrency: 4`, `import: 16`
* *Defense:* `safety: 12`, `immutability_locks: 81`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` algorithm, analyzer.h, hlasm_context.h, well_known.h, format, library_info_transitional.h, lsp_context.h, opencode_provider.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.569)
- **Top Global Matches:** file_cluster_12: 7.569, file_cluster_5: 9.093, file_cluster_10: 9.232
- **Magnitude:** 565.5 | **LOC:** 778 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.606; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Mutation Surface (formerly State Flux) (90.9%), Guard Balance (formerly Safety Score) (54.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adjustJobHeader` **(Compute Cores)** (Impact: 17.2)
  * `generateJobHeader` **(Compute Cores)** (Impact: 11.0)
  * `basicFtpJobClient` **(Callbacks & Closures)** (Impact: 10.9)
  * `prepareJobHeader` **(Compute Cores)** (Impact: 10.4)
  * `zoweJobMapper` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 342
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 279`, `args: 118`, `func_start: 69`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 57`, `planned_debt: 1`
* *Architecture:* `io: 23`, `api: 16`, `concurrency: 132`, `import: 16`
* *Defense:* `safety: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.606
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.003613
  * `Imports (Out-Degree: 10):` FBStreamingConvertor, constants, eventsHandler, extension, helpers, mfCreds, serverFactory.common, telemetry...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `clients/vscode-hlasmplugin/src/test/suite/hlasmListingServices.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.411)
- **Top Global Matches:** file_cluster_10: 4.411, file_cluster_2: 5.592, file_cluster_0: 6.352
- **Magnitude:** 564.95 | **LOC:** 259 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.497; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.4%), Complexity Load (formerly Cognitive Load) (41.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 20`, `args: 16`, `func_start: 8`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `concurrency: 11`, `import: 3`
* *Defense:* `safety: 9`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.497
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001156
  * `Imports (Out-Degree: 1):` hlasmListingServices, assert, vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `parser_library/src/debugging/debugger.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.488)
- **Top Global Matches:** file_cluster_4: 6.488, file_cluster_15: 9.71, file_cluster_11: 10.909
- **Magnitude:** 544.5 | **LOC:** 809 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Debt Markers (formerly Tech Debt) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.000258 | `Ripple Effect (Closeness):` 0.001156
  * `Imports (Out-Degree: 38):` algorithm, analyzer.h, atomic, hlasm_context.h, ordinary_assembly_dependency_solver.h, system_variable.h, well_known.h, debug_lib_provider.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `parser_library/src/processing/statement_analyzers/lsp_analyzer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.045)
- **Top Global Matches:** file_cluster_4: 6.045, file_cluster_15: 10.336, file_cluster_6: 11.085
- **Magnitude:** 507.7 | **LOC:** 676 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.2%), Guard Balance (formerly Safety Score) (58.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` algorithm, array, hlasm_context.h, ordinary_assembly_dependency_solver.h, postponed_statement.h, symbol_dependency_tables.h, source_context.h, special_instructions.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/context/ordinary_assembly/symbol_dependency_tables.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.807)
- **Top Global Matches:** file_cluster_15: 6.807, file_cluster_4: 8.337, file_cluster_11: 8.9
- **Magnitude:** 503.5 | **LOC:** 882 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.8%), Complexity Load (formerly Cognitive Load) (65.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` algorithm, array, cassert, cstddef, deque, diagnostic_tools.h, functional, location_counter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utils/src/resource_location.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.293)
- **Top Global Matches:** file_cluster_4: 6.293, file_cluster_6: 9.316, file_cluster_15: 12.17
- **Magnitude:** 491.54 | **LOC:** 648 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **12**; blast radius 17.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Debt Markers (formerly Tech Debt) (91.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_path` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `remove_dot_segments` **(Compute Cores)** (Impact: 36.4)
    * *Intent:* // Algorithm from RFC 3986
  * `resource_location::relative_reference_resolution` **(Compute Cores)** (Impact: 34.3)
  * `resource_location::lexically_relative` **(Compute Cores)** (Impact: 25.5)
  * `windows_normalization_data` **(Defensive Guards)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 98`, `args: 31`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `planned_debt: 3`, `unreferenced_by_name: 15`
* *Architecture:* `import: 12`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.004
  * `Choke Point (Betweenness):` 0.001035 | `Ripple Effect (Closeness):` 0.123818
  * `Imports (Out-Degree: 4):` algorithm, array, assert.h, cstddef, iterator, regex, utility, encoding.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `parser_library/src/checking/asm_instr_class.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_6: 6.671, file_cluster_8: 11.797, file_cluster_4: 13.684
- **Magnitude:** 489.74 | **LOC:** 861 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%), Debt Markers (formerly Tech Debt) (35.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, asm_instr_class.h, charconv, checker_helper.h, diagnostic_collector.h, optional, string_view
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/test/checking/asm_instr_check_test.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.303)
- **Top Global Matches:** file_cluster_15: 8.303, file_cluster_17: 8.916, file_cluster_13: 8.967
- **Magnitude:** 472.04 | **LOC:** 1087 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.5%), Connectivity (formerly Api Exposure) (1.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instruction_test` **(Type Conversions)** (Impact: 30.4)
  * `ccw` **(State Mutators)** (Impact: 2.9)
  * `process` **(State Mutators)** (Impact: 2.5)
  * `using_instr` **(State Mutators)** (Impact: 2.5)
  * `mnote` **(State Mutators)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 74`, `args: 119`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 357`, `unreferenced_by_name: 28`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 55`, `test: 150`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` diagnostic_collector.h, instr_operand.h, instruction_checker.h, gtest.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `parser_library/src/lsp/item_convertors.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.007)
- **Top Global Matches:** file_cluster_4: 6.007, file_cluster_6: 10.154, file_cluster_15: 11.134
- **Magnitude:** 455.9 | **LOC:** 680 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.537; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (62.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.537
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.004624
  * `Imports (Out-Degree: 19):` completion_item.h, concepts, hlasm_context.h, section.h, symbol.h, sequence_symbol.h, using.h, ebcdic_encoding.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `utils/include/utils/factory.h` (CPP) | Magnitude: 4.3 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, reflection_metaprogramming: 2, macros: 2
- `utils/include/utils/text_convertor.h` (CPP) | Magnitude: 15.88 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, immutability_locks: 17, structural_boundaries: 16, args: 12
- `utils/include/utils/transform_inserter.h` (CPP) | Magnitude: 14.36 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 19, pointers: 7, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `parser_library/src/checking/diagnostic_collector.cpp` (CPP) | Magnitude: 11.68 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, func_start: 5, import: 4
- `parser_library/src/diagnostic_op.h` (CPP) | Magnitude: 17.04 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 411, immutability_locks: 370, args: 136, pointers: 14
- `parser_library/src/analyzer.cpp` (CPP) | Magnitude: 77.2 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 32, pointers: 27, func_start: 20
- `language_server/src/blocking_queue.h` (CPP) | Magnitude: 42.98 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 21, immutability_locks: 12, branch: 11
- `language_server/test/dap/dap_sessions_test.cpp` (CPP) | Magnitude: 15.84 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 13, test: 10, serialization_parsing: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `clients/vscode-hlasmplugin/src/hlasmExternalFiles.ts` (TYPESCRIPT) | Magnitude: 655.3 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 572, structural_boundaries: 256, branch: 177, args: 111
- `clients/vscode-hlasmplugin/src/connectionPool.ts` (TYPESCRIPT) | Magnitude: 60.4 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 19, args: 10, concurrency: 10
- `clients/vscode-hlasmplugin/src/test/suite/codeActions.test.ts` (TYPESCRIPT) | Magnitude: 92.2 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 49, concurrency: 36, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `parser_library/test/expressions/ca_symbol_test.cpp` (CPP) | Magnitude: 7.34 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, test: 8, structural_boundaries: 6, import: 5
- `utils/test/path_test.cpp` (CPP) | Magnitude: 1.88 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, test: 2, import: 2, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `parser_library/test/expressions/ca_var_sym_test.cpp` (CPP) | Magnitude: 14.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, test: 11, structural_boundaries: 8, import: 8
- `parser_library/test/expressions/ca_expr_list_test.cpp` (CPP) | Magnitude: 55.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, args: 35, test: 32, structural_boundaries: 23
- `language_server/test/virtual_file_provider_test.cpp` (CPP) | Magnitude: 13.04 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 50, test: 17, structural_boundaries: 16, serialization_parsing: 10
- `utils/src/platform.cpp` (CPP) | Magnitude: 65.62 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 45, core_var_decl: 29, design_snake_case: 29
- `language_server/test/pseudo_convertors_test.cpp` (CPP) | Magnitude: 9.54 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, test: 13, immutability_locks: 9, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `parser_library/src/lsp/completion_item.cpp` (CPP) | Magnitude: 3.98 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, args: 6, immutability_locks: 2, branch: 1
- `example_workspace/forward_dependency.hlasm` (HLASM) | Magnitude: 14.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, immutability_locks: 2
- `parser_library/src/lsp/macro_info.h` (CPP) | Magnitude: 18.08 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 14, core_var_decl: 9, design_snake_case: 9
- `parser_library/test/workspace_manager_response_mock.h` (CPP) | Magnitude: 16.26 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, macros: 2, indent_spaces: 2
- `parser_library/src/processing/instruction_sets/ca_processor.h` (CPP) | Magnitude: 4.74 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 36, immutability_locks: 34, class_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `parser_library/src/semantics/statement.cpp` (CPP) | Magnitude: 11.12 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, args: 6, func_start: 3, unreferenced_by_name: 3
- `parser_library/test/processing/dc_test.cpp` (CPP) | Magnitude: 71.78 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 153, test: 81, args: 54, core_var_decl: 29
- `parser_library/src/processing/statement_processors/macrodef_processing_info.h` (CPP) | Magnitude: 3.6 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 11, design_snake_case: 11, import: 8
- `parser_library/src/processing/statement_processors/lookahead_processing_info.h` (CPP) | Magnitude: 11.56 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 5, args: 5, func_start: 4
- `utils/test/filter_vector_test.cpp` (CPP) | Magnitude: 53.48 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 108, test: 52, state_mutation: 26, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `parser_library/src/lsp/lsp_context.cpp` (CPP) | Magnitude: 630.38 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 568, structural_boundaries: 215, branch: 206, pointers: 168

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `clients/vscode-hlasmplugin/src/test/suite/asyncMutex.test.ts` (TYPESCRIPT) | Magnitude: 74.24 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 22, concurrency: 16, core_var_decl: 14
- `clients/vscode-hlasmplugin/src/continuationHandler.ts` (TYPESCRIPT) | Magnitude: 221.62 | Delta: **0.171** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 156, branch: 50, structural_boundaries: 40, core_var_decl: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `parser_library/src/lexing/tools.cpp` (CPP) | Magnitude: 50.72 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 10, branch: 9, structural_boundaries: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `parser_library/src/checking/asm_instr_check.cpp` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 977.22
- `clients/vscode-hlasmplugin/src/hlasmListingServices.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 916.3
- `parser_library/src/context/hlasm_context.cpp` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 726.32
- `clients/vscode-hlasmplugin/src/hlasmExternalFiles.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 655.3
- `parser_library/src/checking/data_definition/data_instruction.cpp` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 615.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `parser_library/src/workspace_manager.cpp` -> **Severity: 0.665** (Bridge: 0.0071 * Flux: 94.1593%)
- `parser_library/src/semantics/concatenation.cpp` -> **Severity: 0.3** (Bridge: 0.003 * Flux: 99.95%)
- `parser_library/src/expressions/conditional_assembly/terms/ca_function.cpp` -> **Severity: 0.186** (Bridge: 0.0019 * Flux: 99.9947%)
- `parser_library/src/expressions/conditional_assembly/terms/ca_string.cpp` -> **Severity: 0.164** (Bridge: 0.0017 * Flux: 99.2204%)
- `parser_library/src/workspaces/workspace_configuration.cpp` -> **Severity: 0.141** (Bridge: 0.0014 * Flux: 99.1784%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `utils/src/resource_location.cpp` -> **Severity: 8.018** (Embedded: 0.1238 * Error Risk: 64.7546%)
- `utils/include/utils/resource_location.h` -> **Severity: 7.612** (Embedded: 0.1695 * Error Risk: 44.9176%)
- `parser_library/include/diagnostic.h` -> **Severity: 6.511** (Embedded: 0.1289 * Error Risk: 50.505%)
- `parser_library/include/protocol.h` -> **Severity: 6.34** (Embedded: 0.1344 * Error Risk: 47.1804%)
- `parser_library/src/context/id_index.h` -> **Severity: 6.022** (Embedded: 0.1347 * Error Risk: 44.7101%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `parser_library/include/range.h` -> **Severity: 3866.1** (Blast Radius: 38.661 * Doc Risk: 100.0%)
- `utils/include/utils/insist.h` -> **Severity: 2215.1** (Blast Radius: 22.151 * Doc Risk: 100.0%)
- `utils/src/insist.cpp` -> **Severity: 1930.8** (Blast Radius: 19.308 * Doc Risk: 100.0%)
- `utils/include/utils/resource_location.h` -> **Severity: 1776.3** (Blast Radius: 17.763 * Doc Risk: 100.0%)
- `utils/src/resource_location.cpp` -> **Severity: 1700.4** (Blast Radius: 17.004 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 55 literal sites + 48 sites through wrappers = 103
- **`memory_alloc`:** 17 literal sites + 14 sites through wrappers = 31
- **`panics_and_aborts`:** 148 literal sites + 3 sites through wrappers = 151

- `log_i` (function, debug_prints, primitive): 30 call sites in 1 files -- `benchmark/benchmark.cpp`
- `create_workspace_manager` (function, memory_alloc, via create_workspace_manager_impl): 11 call sites in 3 files -- `parser_library/include/workspace_manager.h`
- `log_e` (function, debug_prints, primitive): 11 call sites in 1 files -- `benchmark/benchmark.cpp`
- `log_if` (function, debug_prints, primitive): 5 call sites in 1 files -- `benchmark/benchmark.cpp`
- `consume` (function, memory_alloc, primitive): 2 call sites in 1 files -- `language_server/src/emscripten_server_streams.cpp`
- `log_w` (function, debug_prints, primitive): 2 call sites in 1 files -- `benchmark/benchmark.cpp`
- `splitFailed` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.ts`
- `create_workspace_manager_impl` (function, memory_alloc, primitive): 1 call sites in 1 files -- `parser_library/src/workspace_manager.cpp`
- `downloadDependencies` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `clients/vscode-hlasmplugin/src/hlasmDownloadCommands.web.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 31886 call pairs -- scoped 23.5%, unique 7.8%, ambiguous 36.0%, external 32.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 30169 | 23.2% | 8.3% | 37.7% | 30.9% |
| typescript | 1628 | 29.1% | 0.0% | 7.0% | 63.9% |
| shell | 33 | 0.0% | 0.0% | 0.0% | 100.0% |
| lua | 26 | 0.0% | 0.0% | 0.0% | 100.0% |
| hlasm | 16 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 14 | 57.1% | 0.0% | 0.0% | 42.9% |

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
