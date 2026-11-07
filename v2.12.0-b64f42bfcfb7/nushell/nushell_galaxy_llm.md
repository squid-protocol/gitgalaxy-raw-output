# ARCHITECTURAL_BRIEF: nushell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nushell/nushell.git` |
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
- **Scope:** 1788 analyzed artifact(s), 289492 LOC.
- **Load-bearing artifact:** `crates/nu-protocol/src/lib.rs` -- 687 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/nu-command/tests/commands/mod.rs` -- pulls in 139 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/nu-parser/src/parser.rs` at magnitude 4019.1 (structural weight, not risk).
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
| Total Artifacts | 2227 |
| Analyzed Artifacts (Scanned) | 1788 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 439 |
| Total LOC | 289492 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 80.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5463 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2063 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 31.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0905 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1609 | 286527 | 90.0% |
| MARKDOWN | 60 | 0 | 3.4% |
| YAML | 39 | 1413 | 2.2% |
| JSON | 38 | 598 | 2.1% |
| PLAINTEXT | 25 | 3 | 1.4% |
| SHELL | 4 | 90 | 0.2% |
| CSV | 3 | 71 | 0.2% |
| DOCKERFILE | 2 | 80 | 0.1% |
| POWERSHELL | 2 | 25 | 0.1% |
| NIX | 2 | 289 | 0.1% |
| JAVASCRIPT | 1 | 182 | 0.1% |
| PYTHON | 1 | 189 | 0.1% |
| BATCH | 1 | 25 | 0.1% |
| XML | 1 | 0 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1788 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 37%, Declarative / Non-Code 19%, Data / Markup / Trivial 15%, Large Core Modules (3) 12%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1701 | 95.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 84 | 4.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 439*

**Composition by Extension & Reason:**
- `.nu`: 157x Unsupported Format (.nu), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 31x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.blockcommandparser')
- `.hjson`: 59x Excluded (Unsupported Extension: '.hjson')
- `.toml`: 40x Unsupported Format (.toml), 7x Excluded (Unsupported Extension: '.toml'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 14x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nuon`: 3x Excluded (Unsupported Extension: '.nuon')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.exe`: 2x Excluded (Explicitly Denied Extension: '.exe')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.ods`: 2x Excluded (Explicitly Denied Extension: '.ods')
- `.xlsx`: 2x Excluded (Explicitly Denied Extension: '.xlsx')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.6 | 7.1 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 24.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 98.8 | 38.6 | 43.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.7 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 22.5 | 20.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2520 | 527 | 3 | `crates/nu-cli/tests/completions/mod.rs` |
| cleanup | 75 | 32 | 0 | `crates/nu-plugin-core/src/interface/stream/tests.rs` |
| guards | 4871 | 825 | 6 | `crates/nu-parser/src/parser.rs` |
| danger | 3442 | 511 | 3 | `crates/nu-parser/tests/test_parser.rs` |
| concurrency | 904 | 151 | 0 | `crates/nu-protocol/src/process/child.rs` |
| connectivity | 14227 | 1547 | 17 | `tests/repl/test_parser.rs` |
| io | 501 | 151 | 0 | `crates/nu-protocol/src/errors/shell_error/io.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 79 | 36 | 0 | `crates/nu-plugin-core/src/interface/stream/tests.rs` |
| time | 43 | 32 | 0 | `crates/nu-cli/src/commands/history/history_import.rs` |
| serialization | 23 | 14 | 0 | `crates/nu_plugin_javascript/nu_plugin_node_example.js` |
| regex | 41 | 20 | 0 | `crates/nu-command/src/strings/detect_type.rs` |
| events | 304 | 74 | 0 | `crates/nu-parser/src/parser.rs` |
| tests | 14715 | 932 | 20 | `crates/nu-parser/tests/test_parser.rs` |
| docs | 12049 | 418 | 9 | `crates/nu-path/src/path.rs` |
| debt | 1185 | 389 | 1 | `crates/nu-parser/tests/test_parser.rs` |
| mutation | 32084 | 1343 | 43 | `crates/nu-parser/src/parser.rs` |
| dead_code | 1277 | 161 | 0 | `tests/overlays/mod.rs` |
| credential | 10 | 8 | 0 | `tests/assets/nu_json/charset_result.json` |
| threat | 34 | 5 | 0 | `tests/repl/test_commandline.rs` |
| ml_ai | 362 | 101 | 0 | `crates/nu-protocol/src/value/mod.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/nu-protocol/src/errors/shell_error/io.rs` (Hits: 44)
- `crates/nu-command/src/strings/guess_width.rs` (Hits: 37)
- `crates/nu-command/src/network/http/interruptible_tcp.rs` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`crates/nu-protocol/src/lib.rs`) — 687 inbound connections
2. **command_prelude.rs** (`crates/nu-engine/src/command_prelude.rs`) — 456 inbound connections
3. **mod.rs** (`crates/nu-protocol/src/value/mod.rs`) — 352 inbound connections
4. **lib.rs** (`crates/nu-test-support/src/lib.rs`) — 275 inbound connections
5. **signature.rs** (`crates/nu-protocol/src/signature.rs`) — 218 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`crates/nu-command/tests/commands/mod.rs`) — 139 outbound dependencies
2. **mod.rs** (`crates/nu-command/src/filters/mod.rs`) — 113 outbound dependencies
3. **repl.rs** (`crates/nu-cli/src/repl.rs`) — 93 outbound dependencies
4. **windows.rs** (`crates/nu-system/src/windows.rs`) — 83 outbound dependencies
5. **mod.rs** (`crates/nu_plugin_polars/src/dataframe/command/data/mod.rs`) — 78 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `compile_expression` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/compile/expression.rs`) -> Impact: **306.4** | LOC: 571
- `eval_instruction` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/eval_ir.rs`) -> Impact: **301.4** | LOC: 640
  * *Intent:* /// Perform an instruction
- `series_to_values` **(Many-Argument Workhorses)** (@ `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs`) -> Impact: **245.1** | LOC: 520
- `parse_signature_helper` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **221.2** | LOC: 704
- `rm` **(Many-Argument Workhorses)** (@ `crates/nu-command/src/filesystem/rm.rs`) -> Impact: **211.8** | LOC: 395
- `discover_captures_in_expr` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **198.3** | LOC: 292
  * *Intent:* // Closes over captured variables
- `lex_item` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/lex.rs`) -> Impact: **197.4** | LOC: 297
- `compile_try` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/compile/keyword.rs`) -> Impact: **194.5** | LOC: 292
  * *Intent:* /// Compile a call to `try`, setting an error handler over the evaluated block
- `parse_internal_call` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **180.5** | LOC: 377
- `run` **(Many-Argument Workhorses)** (@ `crates/nu-command/src/filters/last.rs`) -> Impact: **174.4** | LOC: 255

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/nu-parser/src` | 12 | 7904.6 | 28.85% | 6.52% |
| `crates/nu-command/tests/commands` | 121 | 5242.52 | 1.22% | 0.0% |
| `crates/nu-command/src/filters` | 53 | 4724.54 | 11.03% | 4.03% |
| `crates/nu-protocol/src/value` | 10 | 3338.74 | 7.8% | 54.43% |
| `crates/nu-protocol/src/engine` | 20 | 2966.08 | 10.59% | 24.96% |
| `crates/nu-command/src/platform/input` | 6 | 2749.82 | 12.89% | 6.4% |
| `crates/nu-engine/src` | 13 | 2672.12 | 9.41% | 11.19% |
| `crates/nu-command/src/filesystem` | 16 | 2465.78 | 13.81% | 9.48% |
| `crates/nu-cli/src` | 13 | 2321.8 | 10.07% | 5.17% |
| `crates/nu_plugin_polars/src/dataframe/command/data` | 46 | 2206.38 | 7.34% | 1.27% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/nu-explore/src/explore/commands/mod.rs` -> **100.0%** Exposure
- `crates/nu-plugin/src/plugin/command.rs` -> **100.0%** Exposure
- `crates/nu-protocol/src/value/record.rs` -> **100.0%** Exposure
- `crates/nu_plugin_query/src/query_webpage_info.rs` -> **99.9998%** Exposure
- `crates/nu-explore/src/explore/views/binary/mod.rs` -> **99.9992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/nu-command/src/env/config/config_reset.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/binary/binary_widget.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/colored_text_widget.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/cursor/mod.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/record/table_widget.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/overlays/mod.rs` -> **98** Orphaned Functions | **0** Duplicates
- `crates/nu-protocol/src/value/mod.rs` -> **81** Orphaned Functions | **0** Duplicates
- `tests/eval/mod.rs` -> **68** Orphaned Functions | **0** Duplicates
- `crates/nu-cli/tests/completions/mod.rs` -> **67** Orphaned Functions | **0** Duplicates
- `tests/parsing/mod.rs` -> **50** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15336` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/nu-parser/src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.15)
- **Top Global Matches:** file_cluster_6: 6.15, file_cluster_8: 11.48, file_cluster_4: 13.506
- **Magnitude:** 4019.1 | **LOC:** 7520 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **51**; blast radius 0.714; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.3%)
- **Documentation Coverage:** 90.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_signature_helper` **(Many-Argument Workhorses)** (Impact: 221.2)
  * `discover_captures_in_expr` **(Many-Argument Workhorses)** (Impact: 198.3)
    * *Intent:* // Closes over captured variables
  * `parse_internal_call` **(Many-Argument Workhorses)** (Impact: 180.5)
  * `parse_record` **(Many-Argument Workhorses)** (Impact: 106.5)
  * `parse_string_interpolation` **(Many-Argument Workhorses)** (Impact: 100.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 284 instances
* *State Mutation (weighted view):* 960
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1166`, `structural_boundaries: 1326`, `args: 225`, `func_start: 104`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 6`, `state_mutation: 392`, `dead_code: 2`, `planned_debt: 10`, `fragile_debt: 9`
* *Architecture:* `api: 79`, `import: 7`
* *Defense:* `safety: 170`, `doc: 30`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.002349 | `Ripple Effect (Closeness):` 0.066331
  * `Imports (Out-Degree: 19):` crate::Token, crate::TokenContents, crate::lex::LexState, crate::lex::is_assignment_operator, crate::lex::lex, crate::lex::lex_n_tokens, crate::lex::lex_signature, crate::lite_parser::LiteCommand...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/platform/input/list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.648)
- **Top Global Matches:** file_cluster_6: 7.648, file_cluster_4: 7.716, file_cluster_15: 15.165
- **Magnitude:** 2285.78 | **LOC:** 3702 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **41**; blast radius 0.167; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.9%), Guard Balance (formerly Safety Score) (56.7%), Connectivity (formerly Api Exposure) (37.1%)
- **Documentation Coverage:** 42.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 164.6)
  * `render_table_cells` **(Many-Argument Workhorses)** (Impact: 159.6)
    * *Intent:* /// Render table cells with proper alignment and optional fuzzy highlighting
  * `run` **(Many-Argument Workhorses)** (Impact: 131.3)
  * `render_truncated_fuzzy_text` **(Many-Argument Workhorses)** (Impact: 87.4)
    * *Intent:* /// Render fuzzy-highlighted text, truncating with ellipsis if needed. /// The ellipsis is highlight...
  * `handle_fuzzy_multi_key` **(Many-Argument Workhorses)** (Impact: 67.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 746`, `structural_boundaries: 556`, `args: 151`, `func_start: 101`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 194`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 34`, `doc: 98`, `test: 16`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.167
  * `Choke Point (Betweenness):` 0.000195 | `Ripple Effect (Closeness):` 0.02734
  * `Imports (Out-Degree: 8):` crossterm::cursor::Hide, crossterm::cursor::MoveDown, crossterm::cursor::MoveToColumn, crossterm::cursor::MoveUp, crossterm::cursor::Show, crossterm::event, crossterm::event::Event, crossterm::event::KeyCode...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/nu-protocol/src/value/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.458)
- **Top Global Matches:** file_cluster_4: 7.458, file_cluster_0: 9.844, file_cluster_15: 10.051
- **Magnitude:** 1854.14 | **LOC:** 4827 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **352** in-repo importer(s); it depends on **68**; blast radius 30.241; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (61.4%), Guard Balance (formerly Safety Score) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.6%)
- **Documentation Coverage:** 52.7586% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `modulo` **(Many-Argument Workhorses)** (Impact: 120.0)
  * `floor_div` **(Many-Argument Workhorses)** (Impact: 111.0)
  * `get_value_member` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `insert_data_at_cell_path` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `div` **(Many-Argument Workhorses)** (Impact: 75.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 413`, `args: 274`, `func_start: 164`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 19`, `planned_debt: 2`, `unreferenced_by_name: 81`
* *Architecture:* `api: 137`, `import: 32`
* *Defense:* `safety: 115`, `doc: 323`, `test: 79`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.241
  * `Choke Point (Betweenness):` 0.010617 | `Ripple Effect (Closeness):` 0.441537
  * `Imports (Out-Degree: 23):` custom_value, duration, filesize, from_value, glob, into_value, range, record...
  * `Imported By (In-Degree: 352):` (Excluded from Brief to save tokens)

### `crates/nu-parser/src/parse_keywords.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.376)
- **Top Global Matches:** file_cluster_8: 8.376, file_cluster_3: 16.476, file_cluster_6: 20.401
- **Magnitude:** 1679.94 | **LOC:** 4122 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **76**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%), Guard Balance (formerly Safety Score) (49.2%), Connectivity (formerly Api Exposure) (48.6%)
- **Documentation Coverage:** 85.9155% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_alias` **(Many-Argument Workhorses)** (Impact: 94.8)
  * `parse_def_inner` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* // Returns also the parsed command name and ID
  * `parse_overlay_use` **(Many-Argument Workhorses)** (Impact: 79.4)
  * `parse_export_in_module` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* // This one will trigger only in a module
  * `parse_module_block` **(Many-Argument Workhorses)** (Impact: 73.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 805`, `args: 97`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 91`, `dead_code: 7`, `planned_debt: 5`, `fragile_debt: 5`
* *Architecture:* `api: 34`, `import: 8`
* *Defense:* `safety: 144`, `doc: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.000338 | `Ripple Effect (Closeness):` 0.053202
  * `Imports (Out-Degree: 27):` crate::Token, crate::TokenContents, crate::exportable::Exportable, crate::is_math_expression_like, crate::known_external::KnownExternal, crate::lex, crate::lite_parser::LiteCommand, crate::lite_parser::lite_parse...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `crates/nu-engine/src/eval_ir.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.599)
- **Top Global Matches:** file_cluster_4: 8.599, file_cluster_6: 8.812, file_cluster_0: 14.885
- **Magnitude:** 970.52 | **LOC:** 1838 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **60**; blast radius 0.195; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (75.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.9%), Guard Balance (formerly Safety Score) (50.9%)
- **Documentation Coverage:** 21.2121% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eval_instruction` **(Many-Argument Workhorses)** (Impact: 301.4)
    * *Intent:* /// Perform an instruction
  * `binary_op` **(Many-Argument Workhorses)** (Impact: 107.0)
  * `gather_arguments` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* /// Move arguments from the stack into variables for a custom command
  * `literal_value` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `eval_ir_block_impl` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /// Eval an IR block on the provided slice of registers.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 327`, `args: 76`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 62`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 1`, `import: 8`
* *Defense:* `safety: 55`, `doc: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.00224 | `Ripple Effect (Closeness):` 0.132553
  * `Imports (Out-Degree: 27):` crate::ENV_CONVERSIONS, crate::convert_env_vars, crate::eval::is_automatic_env_var, crate::eval_block_with_early_return, nu_path::expand_path, nu_path::expand_path_with, nu_protocol::DeclId, nu_protocol::ENV_VARIABLE_ID...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/nu-engine/src/compile/keyword.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.541)
- **Top Global Matches:** file_cluster_3: 6.541, file_cluster_8: 20.881, file_cluster_6: 33.792
- **Magnitude:** 817.16 | **LOC:** 1131 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.147; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.4%), Complexity Load (formerly Cognitive Load) (22.1%)
- **Documentation Coverage:** 4.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile_try` **(Many-Argument Workhorses)** (Impact: 194.5)
    * *Intent:* /// Compile a call to `try`, setting an error handler over the evaluated block
  * `compile_match` **(Many-Argument Workhorses)** (Impact: 86.9)
    * *Intent:* /// Compile a call to `match`
  * `compile_for` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /// Compile a call to `for` (via `iterate`)
  * `compile_if` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* /// Compile a call to `if` as a branch-if
  * `compile_let` **(Many-Argument Workhorses)** (Impact: 55.6)
    * *Intent:* /// 1. `let var = expr` - Evaluates expr and stores result in variable (no output) /// 2. `input | l...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 125`, `args: 29`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 44`, `planned_debt: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 45`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.084513
  * `Imports (Out-Degree: 13):` nu_protocol::IntoSpanned, nu_protocol::RegId, nu_protocol::Span, nu_protocol::Type, nu_protocol::VarId, nu_protocol::ast::Block, nu_protocol::ast::Call, nu_protocol::ast::Expr...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/nu-cli/src/reedline_config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.438)
- **Top Global Matches:** file_cluster_4: 7.438, file_cluster_6: 9.743, file_cluster_12: 13.315
- **Magnitude:** 761.0 | **LOC:** 1777 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **51**; blast radius 0.228; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (65.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `edit_from_record` **(Many-Argument Workhorses)** (Impact: 133.5)
  * `add_ide_menu` **(Many-Argument Workhorses)** (Impact: 123.7)
    * *Intent:* // Adds an IDE menu to the line editor
  * `add_description_menu` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* // Adds a description menu to the line editor
  * `add_parsed_keybinding` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `add_columnar_menu` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* // Adds a columnar menu to the editor engine
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 282`, `args: 62`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 43`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `concurrency: 5`, `import: 15`
* *Defense:* `safety: 46`, `test: 23`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.002109
  * `Imports (Out-Degree: 14):` EditCommandDiscriminants, ReedlineEventDiscriminants, crate::NuHelpCompleter, crate::menus::NuMenuCompleter, crossterm::event::KeyCode, crossterm::event::KeyModifiers, nu_ansi_term::Style, nu_color_config::color_record_to_nustyle...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/nu-table/src/table.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.697)
- **Top Global Matches:** file_cluster_0: 7.697, file_cluster_15: 7.858, file_cluster_4: 8.538
- **Magnitude:** 740.64 | **LOC:** 1384 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **37**; blast radius 0.373; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.8%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 85.2632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `truncate_columns_by_content` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* // VERSION where we are showing AS LITTLE COLUMNS AS POSSIBLE but WITH AS MUCH CONTENT AS POSSIBLE.
  * `truncate_columns_by_head` **(Many-Argument Workhorses)** (Impact: 44.9)
    * *Intent:* // VERSION where we are showing AS MANY COLUMNS AS POSSIBLE solely based on first column.
  * `truncate_columns_by_columns` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* // VERSION where we are showing AS MANY COLUMNS AS POSSIBLE but as a side affect they MIGHT CONTAIN ...
  * `width_ctrl_truncate` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `load_theme` **(Many-Argument Workhorses)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 326`, `args: 71`, `func_start: 68`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 111`, `dead_code: 7`, `planned_debt: 13`, `fragile_debt: 3`
* *Architecture:* `api: 31`, `import: 6`
* *Defense:* `safety: 12`, `doc: 11`, `test: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.373
  * `Choke Point (Betweenness):` 0.000168 | `Ripple Effect (Closeness):` 0.030627
  * `Imports (Out-Degree: 4):` crate::convert_style, crate::is_color_empty, crate::table_theme::TableTheme, nu_ansi_term::Style, nu_color_config::TextStyle, nu_protocol::TableIndent, nu_protocol::TrimStrategy, std::cmp::max...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/filesystem/ls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.378)
- **Top Global Matches:** file_cluster_6: 7.378, file_cluster_4: 8.857, file_cluster_15: 16.208
- **Magnitude:** 692.48 | **LOC:** 1170 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **48**; blast radius 0.143; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_entry_dict` **(Many-Argument Workhorses)** (Impact: 158.0)
  * `ls_for_one_pattern` **(Many-Argument Workhorses)** (Impact: 157.8)
  * `run` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `get_file_type` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `dir_entry_dict_windows_fallback` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /// A secondary way to get file info on Windows, for when std::fs::symlink_metadata() fails. /// dir...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 207`, `args: 57`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 9`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 33`, `doc: 16`, `test: 6`, `sync_locks: 4`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.026998
  * `Imports (Out-Degree: 6):` chrono::DateTime, chrono::Local, chrono::LocalResult, chrono::TimeZone, chrono::Utc, crate::DirBuilder, crate::DirInfo, nu_engine::command_prelude::*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/nu-parser/tests/test_parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.983)
- **Top Global Matches:** file_cluster_13: 7.983, file_cluster_0: 8.205, file_cluster_12: 8.718
- **Magnitude:** 687.16 | **LOC:** 3252 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.133; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (65.0%), Guard Balance (formerly Safety Score) (55.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%), Complexity Load (formerly Cognitive Load) (3.1%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_int` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `parse_variable_range` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `parse_bounded_range` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `parse_right_unbounded_range` **(Annotated & Test Methods)** (Impact: 12.2)
  * `parse_left_unbounded_range` **(Annotated & Test Methods)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 83
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 716`, `args: 183`, `func_start: 155`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 93`, `state_mutation: 2`, `planned_debt: 14`, `duplicate_logic: 18`
* *Architecture:* `api: 100`, `import: 18`
* *Defense:* `safety: 24`, `doc: 4`, `test: 380`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` mock::*, mock::Alias, mock::AttrEcho, mock::Const, mock::Def, mock::IfMocked, mock::Let, mock::Mut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore/pager/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.177)
- **Top Global Matches:** file_cluster_0: 7.177, file_cluster_15: 8.5, file_cluster_4: 9.064
- **Magnitude:** 685.72 | **LOC:** 1135 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **46**; blast radius 0.757; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.2%), Complexity Load (formerly Cognitive Load) (35.9%)
- **Documentation Coverage:** 95.3488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_ui` **(Many-Argument Workhorses)** (Impact: 64.8)
  * `search_input_key_event` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `handle_general_key_events2` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `render_cmd_bar_cmd` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `cmd_input_key_event` **(Many-Argument Workhorses)** (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 261`, `args: 48`, `func_start: 36`, `class_start: 11`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 83`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 25`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.000375 | `Ripple Effect (Closeness):` 0.007966
  * `Imports (Out-Degree: 15):` command_bar, events, report, status_bar, title_bar, anyhow::Result, crossterm::event::KeyCode, crossterm::event::KeyEvent...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.273)
- **Top Global Matches:** file_cluster_4: 8.273, file_cluster_0: 11.858, file_cluster_6: 12.156
- **Magnitude:** 685.08 | **LOC:** 1957 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **73**; blast radius 0.487; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.7%), Guard Balance (formerly Safety Score) (46.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `series_to_values` **(Many-Argument Workhorses)** (Impact: 245.1)
  * `typed_column_to_series` **(Many-Argument Workhorses)** (Impact: 86.7)
  * `input_type_list_to_series` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `test_any_value_to_value` **(I/O & Config Routines)** (Impact: 30.9)
  * `insert_value` **(Many-Argument Workhorses)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 316`, `args: 174`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 28`, `import: 25`
* *Defense:* `safety: 59`, `test: 53`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.487
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.042988
  * `Imports (Out-Degree: 5):` chrono::DateTime, chrono::Duration, chrono::FixedOffset, chrono::NaiveDate, chrono::NaiveDateTime, chrono::NaiveTime, chrono::TimeZone, chrono::Utc...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `crates/nu-protocol/src/engine/state_working_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.225)
- **Top Global Matches:** file_cluster_12: 7.225, file_cluster_15: 7.823, file_cluster_0: 8.089
- **Magnitude:** 672.4 | **LOC:** 1241 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **115** in-repo importer(s); it depends on **40**; blast radius 7.594; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.7%), Connectivity (formerly Api Exposure) (72.6%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 77.5148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_span` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `find_decl_name` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /// Find the name of the declaration corresponding to `decl_id`. /// /// Extends [`EngineState::find...
  * `find_decl` **(Compute Cores)** (Impact: 20.8)
    * *Intent:* /// Find the [`DeclId`](crate::DeclId) corresponding to a declaration with `name`. /// /// Extends [...
  * `hide_decl` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `add_overlay` **(Many-Argument Workhorses)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 240`, `args: 108`, `func_start: 85`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 42`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 93`, `import: 5`
* *Defense:* `safety: 28`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.594
  * `Choke Point (Betweenness):` 0.001917 | `Ripple Effect (Closeness):` 0.324746
  * `Imports (Out-Degree: 15):` core::panic, crate::BlockId, crate::Category, crate::CompileError, crate::Config, crate::DeclId, crate::FileId, crate::GetSpan...
  * `Imported By (In-Degree: 115):` (Excluded from Brief to save tokens)

### `crates/nu-protocol/src/engine/engine_state.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_5: 6.755, file_cluster_12: 8.911, file_cluster_7: 10.097
- **Magnitude:** 668.3 | **LOC:** 1444 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **118** in-repo importer(s); it depends on **76**; blast radius 10.085; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.3%), Guard Balance (formerly Safety Score) (59.2%)
- **Documentation Coverage:** 69.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge_delta` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* /// Merges a `StateDelta` onto the current state. These deltas come from a system, like the parser, ...
  * `cwd` **(Defensive Guards)** (Impact: 28.0)
    * *Intent:* /// Returns the current working directory, which is guaranteed to be an /// absolute path without tr...
  * `update_plugin_file` **(Compute Cores)** (Impact: 17.8)
  * `merge_env` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /// Merge the environment from the runtime Stack into the engine state
  * `find_decl_name` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* /// Find the name of the declaration corresponding to `decl_id`. /// /// Searches within active over...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 240`, `args: 141`, `func_start: 110`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 53`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 128`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 20`, `doc: 95`, `test: 33`, `sync_locks: 20`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.085
  * `Choke Point (Betweenness):` 0.004972 | `Ripple Effect (Closeness):` 0.354643
  * `Imports (Out-Degree: 22):` crate::BlockId, crate::Config, crate::DeclId, crate::FileId, crate::GetSpan, crate::Handlers, crate::HistoryConfig, crate::JobId...
  * `Imported By (In-Degree: 118):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/database/values/sqlite.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.306)
- **Top Global Matches:** file_cluster_5: 6.306, file_cluster_12: 7.547, file_cluster_7: 9.67
- **Magnitude:** 662.7 | **LOC:** 1591 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **37**; blast radius 1.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.3%), Guard Balance (formerly Safety Score) (54.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%)
- **Documentation Coverage:** 91.7808% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepared_statement_to_nu_list` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `split_select_expressions` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /// Splits a SELECT projection list on top-level commas. /// /// We only split commas that are outsi...
  * `nu_value_to_params` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `read_entire_sqlite_db` **(Compute Cores)** (Impact: 15.3)
  * `convert_sqlite_value_to_nu_value_with_adapter` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 23 instances
* *Api Near Db Sink:* 1 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 239`, `args: 131`, `func_start: 92`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 8`, `state_mutation: 30`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `api: 72`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 21`, `doc: 60`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.000714 | `Ripple Effect (Closeness):` 0.030666
  * `Imports (Out-Degree: 11):` nu_protocol::CustomValue, nu_protocol::IntoPipelineData, nu_protocol::PipelineData, nu_protocol::Record, nu_protocol::ShellError, nu_protocol::Signals, nu_protocol::Span, nu_protocol::Spanned...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `crates/nu-plugin-engine/src/interface/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.063)
- **Top Global Matches:** file_cluster_0: 7.063, file_cluster_15: 8.723, file_cluster_10: 9.519
- **Magnitude:** 588.64 | **LOC:** 1482 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **57**; blast radius 0.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (51.6%), Guard Balance (formerly Safety Score) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%)
- **Documentation Coverage:** 15.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consume` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `handle_engine_call` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /// Handle an engine call.
  * `receive_plugin_call_response` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /// Read the channel for plugin call messages and handle them until the response is received.
  * `write_plugin_call` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /// Write a plugin call message. Returns the writer for the stream.
  * `spawn_engine_call_handler` **(Defensive Guards)** (Impact: 24.6)
    * *Intent:* /// Spawn a handler for engine calls for a plugin, in case we need to handle engine calls /// after ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 206`, `args: 96`, `func_start: 54`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 15`, `fragile_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 26`, `concurrency: 21`, `import: 6`
* *Defense:* `safety: 46`, `doc: 110`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.000438 | `Ripple Effect (Closeness):` 0.035709
  * `Imports (Out-Degree: 22):` tests, crate::PluginCustomValueWithSource, crate::PluginExecutionContext, crate::PluginGc, crate::PluginSource, crate::process::PluginProcess, nu_plugin_core::Interface, nu_plugin_core::InterfaceManager...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `crates/nu-cli/src/repl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.882)
- **Top Global Matches:** file_cluster_12: 8.882, file_cluster_4: 9.204, file_cluster_5: 9.339
- **Magnitude:** 585.82 | **LOC:** 1773 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **93**; blast radius 0.147; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.3%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.4%), Guard Balance (formerly Safety Score) (54.6%)
- **Documentation Coverage:** 65.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop_iteration` **(Many-Argument Workhorses)** (Impact: 75.8)
    * *Intent:* /// Perform one iteration of the REPL loop /// Result is bool: continue loop, current reedline
  * `evaluate_repl` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* /// The main REPL loop, including spinning up the prompt itself.
  * `do_auto_cd` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* /// /// Execute an "auto-cd" operation, changing the current working directory. ///
  * `do_run_cmd` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* /// /// Run a command as received from reedline. This is where we are actually /// running a thing! ...
  * `get_command_finished_marker` **(Many-Argument Workhorses)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 332`, `args: 72`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 2`, `state_mutation: 56`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 7`, `import: 30`
* *Defense:* `safety: 43`, `doc: 51`, `test: 40`, `sync_locks: 7`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.001259
  * `Imports (Out-Degree: 28):` crate::NuHighlighter, crate::NuValidator, crate::NushellPrompt, crate::completions::NuCompleter, crate::hints::ExternalHinter, crate::nu_highlight::NoOpHighlighter, crate::prompt_update, crate::prompt_update::POST_EXECUTION_MARKER_PREFIX...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/nu-parser/src/lex.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.818)
- **Top Global Matches:** file_cluster_6: 6.818, file_cluster_4: 10.947, file_cluster_8: 15.346
- **Magnitude:** 556.28 | **LOC:** 700 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 0.477; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.2%), Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lex_item` **(Many-Argument Workhorses)** (Impact: 197.4)
  * `lex_internal` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `lex_raw_string` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `is_item_terminator` **(Many-Argument Workhorses)** (Impact: 20.9)
    * *Intent:* // A baseline token is terminated if it's not nested inside of a paired // delimiter and the next ch...
  * `lex_n_tokens` **(Many-Argument Workhorses)** (Impact: 6.2)
    * *Intent:* /// Lex until the output is `max_tokens` longer than before the call, or until the input is exhauste...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 97`, `args: 28`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 17`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.477
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.051927
  * `Imports (Out-Degree: 1):` nu_protocol::ParseError, nu_protocol::Span
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/network/http/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.651)
- **Top Global Matches:** file_cluster_0: 7.651, file_cluster_12: 8.798, file_cluster_16: 9.148
- **Magnitude:** 548.58 | **LOC:** 1313 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **57**; blast radius 1.08; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Connectivity (formerly Api Exposure) (47.4%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transform_response_using_content_type` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `send_request` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* // remove once all commands have been migrated
  * `send_form_request` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `request_add_custom_headers` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `send_json_request` **(Many-Argument Workhorses)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 226`, `args: 96`, `func_start: 39`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 25`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 37`, `concurrency: 10`, `import: 19`
* *Defense:* `safety: 31`, `doc: 4`, `test: 12`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.08
  * `Choke Point (Betweenness):` 0.001639 | `Ripple Effect (Closeness):` 0.023861
  * `Imports (Out-Degree: 9):` base64::Engine, base64::alphabet, base64::engine::GeneralPurpose, base64::engine::general_purpose::PAD, crate::formats::value_to_json_value, crate::network::http::interruptible_tcp::InterruptibleTcpConnector, crate::network::http::interruptible_tcp::make_on_connect, crate::network::http::interruptible_unix::InterruptibleUnixSocketConnector...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/viewers/table.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.282)
- **Top Global Matches:** file_cluster_0: 7.282, file_cluster_15: 8.424, file_cluster_4: 8.691
- **Magnitude:** 544.64 | **LOC:** 1369 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **39**; blast radius 0.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.4%), Guard Balance (formerly Safety Score) (52.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_row_stream` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `handle_record` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `get_cli_args` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `stream_collect_abbreviated` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `render_path_name` **(Many-Argument Workhorses)** (Impact: 25.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 232`, `args: 57`, `func_start: 41`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 45`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 33`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.29
  * `Choke Point (Betweenness):` 0.001052 | `Ripple Effect (Closeness):` 0.028283
  * `Imports (Out-Degree: 19):` devicons::icon_for_file, lscolors::LsColors, lscolors::Style, nu_color_config::StyleComputer, nu_color_config::TextStyle, nu_color_config::color_from_hex, nu_color_config::lookup_ansi_color_style, nu_engine::command_prelude::*...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/formats/to/md.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.833)
- **Top Global Matches:** file_cluster_12: 8.833, file_cluster_4: 9.057, file_cluster_5: 9.097
- **Magnitude:** 541.2 | **LOC:** 1548 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.2%), Guard Balance (formerly Safety Score) (55.0%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_output_string` **(Many-Argument Workhorses)** (Impact: 79.0)
  * `table` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `run` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `group_by` **(Defensive Guards)** (Impact: 23.6)
  * `to_md` **(Many-Argument Workhorses)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 147`, `args: 138`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 47`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 11`, `doc: 8`, `test: 51`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.000169 | `Ripple Effect (Closeness):` 0.023497
  * `Imports (Out-Degree: 9):` crate::Get, crate::Metadata, indexmap::IndexMap, nu_cmd_base::formats::to::delimited::merge_descriptors, nu_cmd_lang::eval_pipeline_without_terminal_expression, nu_engine::command_prelude::*, nu_protocol::Config, nu_protocol::IntoPipelineData...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/command.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.384)
- **Top Global Matches:** file_cluster_4: 8.384, file_cluster_5: 11.314, file_cluster_0: 11.597
- **Magnitude:** 535.0 | **LOC:** 1567 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 0.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.2%), Guard Balance (formerly Safety Score) (54.5%)
- **Documentation Coverage:** 93.829% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_cli_args` **(Compute Cores)** (Impact: 85.0)
    * *Intent:* // Parse CLI args into nushell options and script details.
  * `prevalidate_short_groups_before_lexopt` **(Compute Cores)** (Impact: 63.8)
    * *Intent:* // Validate combined short flags and reject unsupported inline values.
  * `parse_experimental_options` **(Defensive Guards)** (Impact: 30.8)
    * *Intent:* // Parse experimental options, allowing bracketed and comma-delimited forms.
  * `parse_log_filters` **(Defensive Guards)** (Impact: 25.1)
    * *Intent:* // Parse log filters and ensure they match known log levels. // Supports multiple formats: [error,wa...
  * `cli_help_text` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* // Generate help text with the legacy layout and default help colors.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 217`, `args: 93`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 48`
* *Architecture:* `api: 47`, `import: 15`
* *Defense:* `safety: 22`, `test: 24`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.001679
  * `Imports (Out-Degree: 9):` crate::test_bins, lexopt::prelude::*, nu_experimental, nu_parser::escape_for_script_arg, nu_protocol::LabeledError, nu_protocol::ShellError, nu_protocol::Span, nu_protocol::Spanned...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/strings/detect_columns.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.647)
- **Top Global Matches:** file_cluster_4: 7.647, file_cluster_0: 10.358, file_cluster_15: 11.058
- **Magnitude:** 516.4 | **LOC:** 1069 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.1%), Guard Balance (formerly Safety Score) (52.5%)
- **Documentation Coverage:** 57.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_with_box_filter` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /// Process input when ignore_box_chars is enabled. /// Handles both position-based and whitespace-b...
  * `baseline` **(Compute Cores)** (Impact: 55.8)
    * *Intent:* /// Tokenizes a single "baseline" token from the input stream. /// A baseline token is a sequence of...
  * `guess_width` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `process_standard` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* /// Process input with standard whitespace-based column detection.
  * `run` **(Many-Argument Workhorses)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 170`, `args: 61`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 24`, `doc: 55`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.027736
  * `Imports (Out-Degree: 4):` itertools::Itertools, nu_engine::command_prelude::*, nu_protocol::Config, nu_protocol::Range, self::*, std::io::Cursor, std::iter::Peekable, std::str::CharIndices...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/nu-protocol/src/pipeline/byte_stream.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.969)
- **Top Global Matches:** file_cluster_0: 6.969, file_cluster_12: 8.563, file_cluster_5: 8.71
- **Magnitude:** 514.52 | **LOC:** 1301 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.746; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.2%), Guard Balance (formerly Safety Score) (51.0%), Mutation Surface (formerly State Flux) (47.6%)
- **Documentation Coverage:** 45.0382% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generic_copy` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* // Copied from [`std::io::copy`]
  * `next` **(Compute Cores)** (Impact: 20.9)
  * `copy_with_signals` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `slice` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `next_string` **(Compute Cores)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 230`, `args: 96`, `func_start: 77`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 23`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 61`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 8`, `doc: 178`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.746
  * `Choke Point (Betweenness):` 0.000407 | `Ripple Effect (Closeness):` 0.227128
  * `Imports (Out-Degree: 6):` crate::IntRange, crate::PipelineData, crate::ShellError, crate::Signals, crate::Span, crate::Type, crate::Value, crate::process::ChildPipe...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/nu-path/src/path.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_0: 6.975, file_cluster_13: 10.949, file_cluster_10: 12.002
- **Magnitude:** 503.5 | **LOC:** 3098 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **34**; blast radius 8.218; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.0%), Guard Balance (formerly Safety Score) (41.4%)
- **Documentation Coverage:** 45.2107% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cow_to_box` **(Generic / Templated Code)** (Impact: 4.9)
  * `try_absolute` **(State Mutators)** (Impact: 4.6)
    * *Intent:* /// Returns an `Ok` [`AbsolutePath`] if the [`Path`] is absolute. /// Otherwise, returns an `Err` [`...
  * `try_relative` **(State Mutators)** (Impact: 4.6)
    * *Intent:* /// Returns an `Ok` [`RelativePath`] if the [`Path`] is relative. /// Otherwise, returns an `Err` [`...
  * `canonicalize` **(Generic / Templated Code)** (Impact: 4.6)
    * *Intent:* /// normalized and symbolic links resolved. /// /// On Windows, this will also simplify to a winuser...
  * `try_into_relative` **(Generic / Templated Code)** (Impact: 4.6)
    * *Intent:* /// Consumes a [`PathBuf`], returning an `Ok` [`RelativePathBuf`] if the [`PathBuf`] /// is relative...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 241`, `args: 232`, `func_start: 182`, `class_start: 5`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 36`
* *Architecture:* `api: 88`, `import: 4`
* *Defense:* `doc: 1288`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.218
  * `Choke Point (Betweenness):` 0.000121 | `Ripple Effect (Closeness):` 0.272399
  * `Imports (Out-Degree: 1):` crate::form::Absolute, crate::form::Any, crate::form::Canonical, crate::form::IsAbsolute, crate::form::MaybeRelative, crate::form::PathCast, crate::form::PathForm, crate::form::PathJoin...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_day.rs` (RUST) | Magnitude: 48.88 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 25, args: 13, core_var_decl: 13
- `crates/nu-cmd-lang/src/core_commands/if_.rs` (RUST) | Magnitude: 63.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 19, branch: 14, generics: 13
- `crates/nu-command/src/filters/every.rs` (RUST) | Magnitude: 31.84 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 11, args: 7, branch: 6
- `crates/nu_plugin_polars/src/dataframe/command/stub.rs` (RUST) | Magnitude: 19.58 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 7, api: 6, args: 5
- `crates/nu-command/src/math/sqrt.rs` (RUST) | Magnitude: 53.4 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 28, args: 13, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_minute.rs` (RUST) | Magnitude: 43.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 25, core_var_decl: 13, args: 11
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_month.rs` (RUST) | Magnitude: 43.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 25, core_var_decl: 13, args: 11
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_nanosecond.rs` (RUST) | Magnitude: 43.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 25, core_var_decl: 13, args: 11
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_second.rs` (RUST) | Magnitude: 43.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 25, core_var_decl: 13, args: 11
- `crates/nu_plugin_polars/src/dataframe/command/datetime/get_week.rs` (RUST) | Magnitude: 43.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 25, core_var_decl: 13, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/nu_plugin_formats/src/main.rs` (RUST) | Magnitude: 2.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, args: 1, func_start: 1
- `crates/nu_plugin_gstat/src/main.rs` (RUST) | Magnitude: 2.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, args: 1, func_start: 1
- `crates/nu_plugin_inc/src/main.rs` (RUST) | Magnitude: 2.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, args: 1, func_start: 1
- `crates/nu_plugin_query/src/main.rs` (RUST) | Magnitude: 2.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, args: 1, func_start: 1
- `crates/nu-command/src/bytes/build_.rs` (RUST) | Magnitude: 37.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 14, args: 8, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/nu-command/tests/commands/utouch.rs` (RUST) | Magnitude: 112.84 | Delta: **0.186** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 496, test: 194, safety_bypasses: 128, structural_boundaries: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/nu_plugin_polars/src/dataframe/command/selector/mod.rs` (RUST) | Magnitude: 3.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 17, memory_alloc: 15, import: 2
- `crates/nu_plugin_polars/src/dataframe/command/aggregation/mod.rs` (RUST) | Magnitude: 13.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 22, memory_alloc: 20, import: 19
- `crates/nu_plugin_custom_values/src/handle_make.rs` (RUST) | Magnitude: 19.42 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 9, args: 5, func_start: 4
- `crates/nu-command/src/strings/guess_width.rs` (RUST) | Magnitude: 311.64 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 469, structural_boundaries: 167, core_var_decl: 126, design_snake_case: 126
- `crates/nu-command/src/filters/slice.rs` (RUST) | Magnitude: 52.96 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 20, branch: 13, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/nu-cmd-plugin/src/util.rs` (RUST) | Magnitude: 77.14 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 25, branch: 23, args: 20
- `crates/nu_plugin_polars/src/dataframe/command/core/mod.rs` (RUST) | Magnitude: 11.36 | Delta: **0.205** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 16, memory_alloc: 14, import: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/nu-cmd-extra/src/extra/mod.rs` (RUST) | Magnitude: 14.42 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 17, api: 6, import: 6
- `crates/nu-command/src/network/url/mod.rs` (RUST) | Magnitude: 22.3 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 15, api: 7, import: 7
- `crates/nu-command/src/random/mod.rs` (RUST) | Magnitude: 22.3 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 15, api: 7, import: 7
- `crates/nu-explore/src/explore_config/mod.rs` (RUST) | Magnitude: 16.2 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 4, api: 1, import: 1
- `tests/plugins/mod.rs` (RUST) | Magnitude: 15.22 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/nu-command/src/date/utils.rs` (RUST) | Magnitude: 29.36 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 291, structural_boundaries: 11, core_var_decl: 9, generics: 8
- `crates/nu-protocol/src/pipeline/mod.rs` (RUST) | Magnitude: 24.28 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 14, api: 9, import: 7
- `crates/nu-cmd-lang/src/core_commands/scope/mod.rs` (RUST) | Magnitude: 22.28 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 14, api: 7, import: 7
- `crates/nu-table/tests/style.rs` (RUST) | Magnitude: 37.48 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 440, test: 84, args: 23, func_start: 14
- `crates/nu-cmd-lang/src/core_commands/attr/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/nu-command/src/platform/input/input_listen.rs` (RUST) | Magnitude: 193.88 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 369, structural_boundaries: 75, branch: 52, args: 37
- `crates/nu_plugin_polars/src/dataframe/command/data/replace.rs` (RUST) | Magnitude: 91.04 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 275, structural_boundaries: 37, branch: 24, args: 23
- `crates/nu_plugin_polars/src/dataframe/values/nu_dtype/mod.rs` (RUST) | Magnitude: 116.72 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 284, structural_boundaries: 55, branch: 37, core_var_decl: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/nu-test-support/src/deprecated/macros.rs` (RUST) | Magnitude: 87.74 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 57, doc: 51, core_var_decl: 39
- `crates/nu-experimental/src/options/mod.rs` (RUST) | Magnitude: 20.94 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, doc: 36, structural_boundaries: 24, test: 11
- `crates/nu_plugin_polars/src/cache/mod.rs` (RUST) | Magnitude: 114.96 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 51, sync_locks: 29, generics: 23
- `crates/nu_plugin_polars/src/dataframe/command/aggregation/var.rs` (RUST) | Magnitude: 33.0 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 17, args: 12, import: 9
- `crates/nu-command/src/experimental/job_describe.rs` (RUST) | Magnitude: 27.96 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 14, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `crates/nu-command/src/platform/input/list.rs` (RUST) | Magnitude: 2285.78 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 2872, branch: 746, structural_boundaries: 556, core_var_decl: 374

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/nu-explore/src/explore_regex/ui.rs` (RUST) | Magnitude: 258.24 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 488, structural_boundaries: 102, branch: 72, core_var_decl: 49

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/nu-protocol/src/errors/shell_error/mod.rs` -> Churn: **84.76%** | Cog Load: 3.3189% | Debt: 78.8301%
- `crates/nu-plugin/src/plugin/interface/mod.rs` -> Churn: **60.21%** | Cog Load: 5.9283% | Debt: 94.9682%
- `crates/nu_plugin_polars/src/dataframe/values/mod.rs` -> Churn: **60.21%** | Cog Load: 7.6581% | Debt: 85.8677%
- `crates/nu_plugin_polars/src/dataframe/values/nu_schema/mod.rs` -> Churn: **60.21%** | Cog Load: 9.9659% | Debt: 71.599%
- `crates/nu-command/src/database/values/sqlite.rs` -> Churn: **54.58%** | Cog Load: 6.8527% | Debt: 50.7183%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/nu-protocol/src/value/mod.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 1854.14
- `crates/nu-engine/src/compile/keyword.rs` -> **Wind** (100.0% isolated ownership) | Magnitude: 817.16
- `crates/nu-cli/src/reedline_config.rs` -> **Juhan** (100.0% isolated ownership) | Magnitude: 761.0
- `crates/nu-table/src/table.rs` -> **Maxim Zhiburt** (100.0% isolated ownership) | Magnitude: 740.64
- `crates/nu-protocol/src/engine/state_working_set.rs` -> **Daniil Sivak** (100.0% isolated ownership) | Magnitude: 672.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/nu_plugin_polars/src/cache/mod.rs` -> **Severity: 1.585** (Bridge: 0.023 * Flux: 68.7995%)
- `crates/nu-protocol/src/lib.rs` -> **Severity: 0.83** (Bridge: 0.0568 * Flux: 14.6155%)
- `crates/nu_plugin_polars/src/lib.rs` -> **Severity: 0.819** (Bridge: 0.0211 * Flux: 38.8241%)
- `crates/nu-protocol/src/config/mod.rs` -> **Severity: 0.606** (Bridge: 0.0087 * Flux: 69.3501%)
- `crates/nu-protocol/src/engine/engine_state.rs` -> **Severity: 0.446** (Bridge: 0.005 * Flux: 89.7413%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/nu-protocol/src/lib.rs` -> **Severity: 25.405** (Embedded: 0.5155 * Error Risk: 49.2772%)
- `crates/nu-test-support/src/fs.rs` -> **Severity: 21.095** (Embedded: 0.2637 * Error Risk: 80.0%)
- `crates/nu-protocol/src/engine/engine_state.rs` -> **Severity: 20.986** (Embedded: 0.3546 * Error Risk: 59.1742%)
- `crates/nu-protocol/src/value/mod.rs` -> **Severity: 20.598** (Embedded: 0.4415 * Error Risk: 46.6501%)
- `crates/nu-protocol/src/signature.rs` -> **Severity: 19.338** (Embedded: 0.376 * Error Risk: 51.4333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/nu-protocol/src/ty.rs` -> **Severity: 1905.382** (Blast Radius: 28.825 * Doc Risk: 66.1017%)
- `crates/nu-protocol/src/value/mod.rs` -> **Severity: 1595.473** (Blast Radius: 30.241 * Doc Risk: 52.7586%)
- `crates/nu-protocol/src/ast/cell_path.rs` -> **Severity: 1546.297** (Blast Radius: 17.957 * Doc Risk: 86.1111%)
- `crates/nu-protocol/src/ast/expression.rs` -> **Severity: 906.9** (Blast Radius: 9.069 * Doc Risk: 100.0%)
- `crates/nu-protocol/src/example.rs` -> **Severity: 866.0** (Blast Radius: 8.66 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 286 literal sites + 10 sites through wrappers = 296
- **`panics_and_aborts`:** 401 literal sites + 11 sites through wrappers = 412

- `_print_lines` (function, debug_prints, primitive): 9 call sites in 1 files -- `crates/nu-command/tests/commands/table.rs`
- `outcome_err` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `src/test_bins.rs`
- `fail` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/test_bins.rs`
- `outcome_ok` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/test_bins.rs`
- `outcome_ok` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/test_bins.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 80882 call pairs -- scoped 13.6%, unique 0.0%, ambiguous 18.8%, external 67.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 80813 | 13.6% | 0.0% | 18.8% | 67.6% |
| python | 30 | 36.7% | 0.0% | 0.0% | 63.3% |
| javascript | 26 | 38.5% | 0.0% | 0.0% | 61.5% |
| shell | 13 | 0.0% | 0.0% | 0.0% | 100.0% |

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
