# ARCHITECTURAL_BRIEF: nushell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/nushell` |
| **Timestamp** | `2026-08-03T19:44:21.582132+00:00` |
| **Scan Duration** | `5.8s` |
| **Git Branch** | `main` |
| **Git Commit** | `8a5a9ae1f8707658d96ddb695f7703e838b33ded` |
| **Git Remote** | `https://github.com/nushell/nushell.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1621 malicious artifacts.

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
| Total Artifacts | 2227 |
| Analyzed Artifacts (Scanned) | 1724 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 503 |
| Total LOC | 260083 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 77.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8431 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1495 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0754 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1607 | 258728 | 93.2% |
| MARKDOWN | 53 | 0 | 3.1% |
| PLAINTEXT | 25 | 0 | 1.5% |
| YAML | 15 | 234 | 0.9% |
| JSON | 6 | 172 | 0.3% |
| SHELL | 5 | 92 | 0.3% |
| CSV | 3 | 71 | 0.2% |
| DOCKERFILE | 2 | 80 | 0.1% |
| POWERSHELL | 2 | 25 | 0.1% |
| NIX | 2 | 285 | 0.1% |
| JAVASCRIPT | 1 | 182 | 0.1% |
| PYTHON | 1 | 189 | 0.1% |
| BATCH | 1 | 25 | 0.1% |
| XML | 1 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.696`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1140 | 66.1% |
| file_cluster_13 | 257 | 14.9% |
| file_cluster_0 | 119 | 6.9% |
| file_cluster_16 | 89 | 5.2% |
| file_cluster_17 | 30 | 1.7% |
| file_cluster_4 | 5 | 0.3% |
| file_cluster_11 | 3 | 0.2% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 78 | 4.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 503*

**Composition by Extension & Reason:**
- `.nu`: 156x Unsupported Format (.nu), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 29x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.blockcommandparser')
- `.hjson`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 43x Unsupported Format (.toml), 7x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 39 exceeds 500 chars), 1x Excluded (Saturation: Line 43 exceeds 500 chars)
- `.json`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nuon`: 3x Excluded (Unsupported Extension: '.nuon')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 2x Excluded (Explicitly Denied Extension: '.exe')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.ods`: 2x Excluded (Explicitly Denied Extension: '.ods')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.3 | 10.1 | 7.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.5 | 20.3 | 19.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 41.6 | 31.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 30.6 | 2.5 | 80.0 |
| API Exposure | 0.0 | 12.5 | 2.6 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.1 | 12.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.7 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 23.1 | 21.6 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 64.2 | 99.5 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 58.7 | 87.5 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/nu-protocol/src/errors/shell_error/io.rs` (Hits: 46)
- `crates/nu_plugin_python/nu_plugin_python_example.py` (Hits: 15)
- `crates/nu-cli/src/repl.rs` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **col.rs** (`crates/nu_plugin_polars/src/dataframe/command/data/col.rs`) — 16 inbound connections
2. **lit.rs** (`crates/nu_plugin_polars/src/dataframe/command/data/lit.rs`) — 9 inbound connections
3. **io.rs** (`crates/nu-protocol/src/errors/shell_error/io.rs`) — 7 inbound connections
4. **nu.rs** (`crates/nu-explore/src/explore/commands/nu.rs`) — 6 inbound connections
5. **ast.rs** (`crates/nu-lsp/src/ast.rs`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **repl.rs** (`crates/nu-cli/src/repl.rs`) — 95 outbound dependencies
2. **windows.rs** (`crates/nu-system/src/windows.rs`) — 83 outbound dependencies
3. **lib.rs** (`crates/nu-lsp/src/lib.rs`) — 79 outbound dependencies
4. **parse_keywords.rs** (`crates/nu-parser/src/parse_keywords.rs`) — 79 outbound dependencies
5. **engine_state.rs** (`crates/nu-protocol/src/engine/engine_state.rs`) — 77 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `from_nu_config` (@ `crates/nu-command/src/platform/input/list.rs`) -> Impact: **3836.9** | LOC: 1293
- `parse_export_in_module` (@ `crates/nu-parser/src/parse_keywords.rs`) -> Impact: **2406.9** | LOC: 1156
- `eval_instruction` (@ `crates/nu-engine/src/eval_ir.rs`) -> Impact: **1922.2** | LOC: 1034
- `spawn_engine_call_handler` (@ `crates/nu-plugin-engine/src/interface/mod.rs`) -> Impact: **1791.2** | LOC: 824
- `series_to_values` (@ `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs`) -> Impact: **1774.9** | LOC: 520
- `run` (@ `crates/nu-command/src/filesystem/save.rs`) -> Impact: **1764.9** | LOC: 479
- `compile_expression` (@ `crates/nu-engine/src/compile/expression.rs`) -> Impact: **1285.3** | LOC: 363
- `to_debug_string` (@ `crates/nu-protocol/src/value/mod.rs`) -> Impact: **1250.5** | LOC: 1246
- `eval` (@ `crates/nu-protocol/src/eval_base.rs`) -> Impact: **1190.1** | LOC: 324
  * *Intent:* /// State that needs to be mutated. /// This is the stack for regular eval, and unused by const eval
- `flatten_expression_into` (@ `crates/nu-parser/src/flatten.rs`) -> Impact: **1166.4** | LOC: 351

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `complete_rec` (@ `crates/nu-cli/src/completions/completion_common.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Recursively goes through paths that match a given `partial`. /// * `built_paths`: State struct for a valid matching path built so far. /// * `want...
- `matches_aux` (@ `crates/nu-cli/src/completions/completion_options.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Returns whether or not the haystack matches the needle. If it does, `item` is added /// to the list of matches (if given). /// /// Helper to avoid...
- `new` (@ `crates/nu-cli/src/completions/completion_options.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// # Arguments /// /// * `needle` - The text to search for /// * `should_sort` - Should results be sorted?
- `fetch` (@ `crates/nu-cli/src/completions/custom_completions.rs`) -> **O(2^N) [Recursive]**
- `convert_to_suggestions` (@ `crates/nu-cli/src/menus/menu_completions.rs`) -> **O(2^N) [Recursive]**
- `get_prompt_string` (@ `crates/nu-cli/src/prompt_update.rs`) -> **O(2^N) [Recursive]**
- `describe_value_inner` (@ `crates/nu-cmd-lang/src/core_commands/describe.rs`) -> **O(2^N) [Recursive]**
- `labeled` (@ `crates/nu-cmd-lang/src/core_commands/error_make.rs`) -> **O(2^N) [Recursive]**
- `run` (@ `crates/nu-cmd-lang/src/core_commands/overlay/use_.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `crates/nu-command/src/conversions/into/datetime.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `compare_rhs_binary_op` (@ `crates/nu-parser/tests/test_parser.rs`) -> DB Complexity: **101**
- `render_ui` (@ `crates/nu-explore/src/explore/pager/mod.rs`) -> DB Complexity: **62**
- `run` (@ `crates/nu-command/src/filesystem/save.rs`) -> DB Complexity: **45**
- `get_command_finished_marker` (@ `crates/nu-cli/src/repl.rs`) -> DB Complexity: **38**
- `from_nu_config` (@ `crates/nu-command/src/platform/input/list.rs`) -> DB Complexity: **37**
- `eval_instruction` (@ `crates/nu-engine/src/eval_ir.rs`) -> DB Complexity: **37**
- `parse_export_in_module` (@ `crates/nu-parser/src/parse_keywords.rs`) -> DB Complexity: **36**
- `render_table_horizontal` (@ `crates/nu-explore/src/explore/views/record/table_widget.rs`) -> DB Complexity: **35**
  * *Intent:* // header at the top; header is always 1 line
- `rm` (@ `crates/nu-command/src/filesystem/rm.rs`) -> DB Complexity: **30**
- `hide_decl` (@ `crates/nu-protocol/src/engine/state_working_set.rs`) -> DB Complexity: **30**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/nu-command/src/filters` | 53 | 15095.16 | 14.56% | 50.53% |
| `crates/nu-parser/src` | 12 | 10190.26 | 15.03% | 31.09% |
| `crates/nu-protocol/src/value` | 10 | 8420.3 | 7.41% | 75.08% |
| `crates/nu-command/tests/commands` | 121 | 8047.98 | 3.16% | 0.0% |
| `crates/nu-engine/src` | 13 | 6669.94 | 15.03% | 30.28% |
| `crates/nu-command/src/filesystem` | 16 | 6182.84 | 14.56% | 44.26% |
| `crates/nu-protocol/src/engine` | 20 | 5557.3 | 13.49% | 60.85% |
| `crates/nu_plugin_polars/src/dataframe/command/data` | 46 | 5421.72 | 8.27% | 38.32% |
| `crates/nu-command/src/platform/input` | 6 | 5320.14 | 15.38% | 40.9% |
| `crates/nu-protocol/src/ast` | 17 | 4988.41 | 7.49% | 36.06% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/nu-cmd-lang/src/core_commands/attr/complete.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/is_admin.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_describe.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_flush.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_id.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/nu-command/src/platform/clip/clipboard/arboard_provider.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/cursor/mod.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/cursor/window_cursor.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/cursor/window_cursor_2d.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/mod.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/repl/test_parser.rs` -> **152** Orphaned Functions | **9** Duplicates
- `tests/integration/cli.rs` -> **106** Orphaned Functions | **0** Duplicates
- `tests/overlays/mod.rs` -> **93** Orphaned Functions | **0** Duplicates
- `crates/nu-parser/tests/test_parser.rs` -> **26** Orphaned Functions | **65** Duplicates
- `crates/nu-json/src/ser.rs` -> **8** Orphaned Functions | **75** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/nu-command/src/strings/detect_type.rs`** -> AI Confidence: **99.39%**
2. **`crates/nu_plugin_polars/src/dataframe/command/data/sql_expr.rs`** -> AI Confidence: **99.35%**
3. **`tests/repl/test_cell_path.rs`** -> AI Confidence: **99.32%**
4. **`crates/nu-cli/src/commands/keybindings_listen.rs`** -> AI Confidence: **99.31%**
5. **`crates/nu-cli/src/menus/menu_completions.rs`** -> AI Confidence: **99.31%**
6. **`crates/nu-cli/src/syntax_highlight.rs`** -> AI Confidence: **99.31%**
7. **`crates/nu-cmd-base/src/util.rs`** -> AI Confidence: **99.31%**
8. **`crates/nu-cmd-lang/src/core_commands/if_.rs`** -> AI Confidence: **99.31%**
9. **`crates/nu-cmd-lang/src/example_support.rs`** -> AI Confidence: **99.31%**
10. **`crates/nu-cmd-plugin/src/util.rs`** -> AI Confidence: **99.31%**
11. **`crates/nu-command/src/date/parser.rs`** -> AI Confidence: **99.31%**
12. **`crates/nu-command/src/filesystem/glob.rs`** -> AI Confidence: **99.31%**
13. **`crates/nu-command/src/filesystem/rm.rs`** -> AI Confidence: **99.31%**
14. **`crates/nu-command/src/filesystem/save.rs`** -> AI Confidence: **99.31%**
15. **`crates/nu-command/src/filesystem/ucp.rs`** -> AI Confidence: **99.31%**
16. **`crates/nu-command/src/filesystem/util.rs`** -> AI Confidence: **99.31%**
17. **`crates/nu-command/src/filesystem/utouch.rs`** -> AI Confidence: **99.31%**
18. **`crates/nu-command/src/filesystem/watch.rs`** -> AI Confidence: **99.31%**
19. **`crates/nu-command/src/filters/default.rs`** -> AI Confidence: **99.31%**
20. **`crates/nu-command/src/filters/find.rs`** -> AI Confidence: **99.31%**
21. **`crates/nu-command/src/filters/interleave.rs`** -> AI Confidence: **99.31%**
22. **`crates/nu-command/src/formats/from/json.rs`** -> AI Confidence: **99.31%**
23. **`crates/nu-command/src/formats/to/msgpack.rs`** -> AI Confidence: **99.31%**
24. **`crates/nu-command/src/generators/seq_date.rs`** -> AI Confidence: **99.31%**
25. **`crates/nu-command/src/help/help_operators.rs`** -> AI Confidence: **99.31%**
26. **`crates/nu-command/src/network/http/get.rs`** -> AI Confidence: **99.31%**
27. **`crates/nu-command/src/network/http/head.rs`** -> AI Confidence: **99.31%**
28. **`crates/nu-command/src/network/http/options.rs`** -> AI Confidence: **99.31%**
29. **`crates/nu-command/src/network/http/post.rs`** -> AI Confidence: **99.31%**
30. **`crates/nu-command/src/network/url/query.rs`** -> AI Confidence: **99.31%**
31. **`crates/nu-command/src/platform/clear.rs`** -> AI Confidence: **99.31%**
32. **`crates/nu-command/src/platform/input/input_listen.rs`** -> AI Confidence: **99.31%**
33. **`crates/nu-command/src/platform/input/legacy_input.rs`** -> AI Confidence: **99.31%**
34. **`crates/nu-command/src/platform/input/list.rs`** -> AI Confidence: **99.31%**
35. **`crates/nu-command/src/strings/char_.rs`** -> AI Confidence: **99.31%**
36. **`crates/nu-command/src/strings/detect_columns.rs`** -> AI Confidence: **99.31%**
37. **`crates/nu-command/src/strings/format/date.rs`** -> AI Confidence: **99.31%**
38. **`crates/nu-command/src/strings/parse.rs`** -> AI Confidence: **99.31%**
39. **`crates/nu-command/src/strings/str_/replace.rs`** -> AI Confidence: **99.31%**
40. **`crates/nu-command/src/system/run_external.rs`** -> AI Confidence: **99.31%**
41. **`crates/nu-command/tests/format_conversions/msgpack.rs`** -> AI Confidence: **99.31%**
42. **`crates/nu-engine/src/compile/call.rs`** -> AI Confidence: **99.31%**
43. **`crates/nu-engine/src/compile/expression.rs`** -> AI Confidence: **99.31%**
44. **`crates/nu-engine/src/compile/keyword.rs`** -> AI Confidence: **99.31%**
45. **`crates/nu-engine/src/compile/mod.rs`** -> AI Confidence: **99.31%**
46. **`crates/nu-engine/src/compile/operator.rs`** -> AI Confidence: **99.31%**
47. **`crates/nu-engine/src/compile/redirect.rs`** -> AI Confidence: **99.31%**
48. **`crates/nu-engine/src/env.rs`** -> AI Confidence: **99.31%**
49. **`crates/nu-engine/src/eval.rs`** -> AI Confidence: **99.31%**
50. **`crates/nu-engine/src/eval_ir.rs`** -> AI Confidence: **99.31%**
51. **`crates/nu-experimental/src/parse.rs`** -> AI Confidence: **99.31%**
52. **`crates/nu-explore/src/explore_config/input.rs`** -> AI Confidence: **99.31%**
53. **`crates/nu-parser/src/flatten.rs`** -> AI Confidence: **99.31%**
54. **`crates/nu-parser/src/parser.rs`** -> AI Confidence: **99.31%**
55. **`crates/nu-parser/src/type_check.rs`** -> AI Confidence: **99.31%**
56. **`crates/nu-path/src/helpers.rs`** -> AI Confidence: **99.31%**
57. **`crates/nu-plugin-core/src/interface/stream/mod.rs`** -> AI Confidence: **99.31%**
58. **`crates/nu-plugin-engine/src/interface/mod.rs`** -> AI Confidence: **99.31%**
59. **`crates/nu-plugin/src/plugin/interface/mod.rs`** -> AI Confidence: **99.31%**
60. **`crates/nu-protocol/src/ast/cell_path.rs`** -> AI Confidence: **99.31%**
61. **`crates/nu-protocol/src/ast/expression.rs`** -> AI Confidence: **99.31%**
62. **`crates/nu-protocol/src/engine/call.rs`** -> AI Confidence: **99.31%**
63. **`crates/nu-protocol/src/engine/pattern_match.rs`** -> AI Confidence: **99.31%**
64. **`crates/nu-protocol/src/eval_base.rs`** -> AI Confidence: **99.31%**
65. **`crates/nu-protocol/src/ir/display.rs`** -> AI Confidence: **99.31%**
66. **`crates/nu-protocol/src/value/from_value.rs`** -> AI Confidence: **99.31%**
67. **`crates/nu-protocol/src/value/mod.rs`** -> AI Confidence: **99.31%**
68. **`crates/nu-protocol/src/value/range.rs`** -> AI Confidence: **99.31%**
69. **`crates/nu-utils/src/utils.rs`** -> AI Confidence: **99.31%**
70. **`crates/nu_plugin_custom_values/src/cool_custom_value.rs`** -> AI Confidence: **99.31%**
71. **`crates/nu_plugin_example/src/commands/call_decl.rs`** -> AI Confidence: **99.31%**
72. **`crates/nu_plugin_example/src/commands/disable_gc.rs`** -> AI Confidence: **99.31%**
73. **`crates/nu_plugin_example/src/commands/env.rs`** -> AI Confidence: **99.31%**
74. **`crates/nu_plugin_example/src/commands/for_each.rs`** -> AI Confidence: **99.31%**
75. **`crates/nu_plugin_formats/src/from/ini.rs`** -> AI Confidence: **99.31%**
76. **`crates/nu_plugin_gstat/src/gstat.rs`** -> AI Confidence: **99.31%**
77. **`crates/nu_plugin_polars/src/dataframe/command/computation/math.rs`** -> AI Confidence: **99.31%**
78. **`crates/nu_plugin_polars/src/dataframe/command/core/to_df.rs`** -> AI Confidence: **99.31%**
79. **`crates/nu_plugin_polars/src/dataframe/command/core/to_nu.rs`** -> AI Confidence: **99.31%**
80. **`crates/nu_plugin_polars/src/dataframe/command/data/pivot.rs`** -> AI Confidence: **99.31%**
81. **`crates/nu_plugin_polars/src/dataframe/command/data/replace.rs`** -> AI Confidence: **99.31%**
82. **`crates/nu_plugin_polars/src/dataframe/command/index/arg_sort.rs`** -> AI Confidence: **99.31%**
83. **`crates/nu_plugin_polars/src/dataframe/command/string/str_replace.rs`** -> AI Confidence: **99.31%**
84. **`crates/nu_plugin_polars/src/dataframe/command/string/str_replace_all.rs`** -> AI Confidence: **99.31%**
85. **`crates/nu_plugin_polars/src/dataframe/values/nu_expression/mod.rs`** -> AI Confidence: **99.31%**
86. **`crates/nu_plugin_stress_internals/src/main.rs`** -> AI Confidence: **99.31%**
87. **`crates/nuon/src/from.rs`** -> AI Confidence: **99.31%**
88. **`crates/nuon/src/to.rs`** -> AI Confidence: **99.31%**
89. **`crates/nu-explore/src/explore_regex/quick_ref.rs`** -> AI Confidence: **99.29%**
90. **`crates/nu-system/src/os_info.rs`** -> AI Confidence: **99.29%**
91. **`crates/nu-utils/src/emoji.rs`** -> AI Confidence: **99.29%**
92. **`tests/repl/test_conditionals.rs`** -> AI Confidence: **99.29%**
93. **`crates/nu_plugin_javascript/nu_plugin_node_example.js`** -> AI Confidence: **99.29%**
94. **`docker/Dockerfile`** -> AI Confidence: **99.29%**
95. **`docker/debian.Dockerfile`** -> AI Confidence: **99.29%**
96. **`scripts/uninstall-all.sh`** -> AI Confidence: **99.29%**
97. **`tests/fixtures/formats/script.nu`** -> AI Confidence: **99.29%**
98. **`scripts/install-all.ps1`** -> AI Confidence: **99.29%**
99. **`crates/nu-lsp/src/ast.rs`** -> AI Confidence: **99.25%**
100. **`src/terminal.rs`** -> AI Confidence: **99.25%**
101. **`crates/nu-cli/src/completions/cell_path_completions.rs`** -> AI Confidence: **99.24%**
102. **`crates/nu-cli/src/eval_file.rs`** -> AI Confidence: **99.24%**
103. **`crates/nu-cmd-extra/src/extra/bits/mod.rs`** -> AI Confidence: **99.24%**
104. **`crates/nu-cmd-extra/src/extra/formats/to/html/mod.rs`** -> AI Confidence: **99.24%**
105. **`crates/nu-cmd-extra/src/extra/strings/format/bits.rs`** -> AI Confidence: **99.24%**
106. **`crates/nu-cmd-extra/src/extra/strings/format/command.rs`** -> AI Confidence: **99.24%**
107. **`crates/nu-cmd-lang/src/core_commands/do_.rs`** -> AI Confidence: **99.24%**
108. **`crates/nu-cmd-plugin/src/commands/plugin/add.rs`** -> AI Confidence: **99.24%**
109. **`crates/nu-command/src/conversions/into/duration.rs`** -> AI Confidence: **99.24%**
110. **`crates/nu-command/src/conversions/into/int.rs`** -> AI Confidence: **99.24%**
111. **`crates/nu-command/src/conversions/into/string.rs`** -> AI Confidence: **99.24%**
112. **`crates/nu-command/src/database/values/sqlite.rs`** -> AI Confidence: **99.24%**
113. **`crates/nu-command/src/filesystem/du.rs`** -> AI Confidence: **99.24%**
114. **`crates/nu-command/src/filesystem/open.rs`** -> AI Confidence: **99.24%**
115. **`crates/nu-command/src/filesystem/umv.rs`** -> AI Confidence: **99.24%**
116. **`crates/nu-command/src/filters/group_by.rs`** -> AI Confidence: **99.24%**
117. **`crates/nu-command/src/filters/select.rs`** -> AI Confidence: **99.24%**
118. **`crates/nu-command/src/filters/utils.rs`** -> AI Confidence: **99.24%**
119. **`crates/nu-command/src/formats/to/json.rs`** -> AI Confidence: **99.24%**
120. **`crates/nu-command/src/formats/to/md.rs`** -> AI Confidence: **99.24%**
121. **`crates/nu-command/src/math/utils.rs`** -> AI Confidence: **99.24%**
122. **`crates/nu-command/src/misc/source.rs`** -> AI Confidence: **99.24%**
123. **`crates/nu-command/src/path/exists.rs`** -> AI Confidence: **99.24%**
124. **`crates/nu-command/src/path/self_.rs`** -> AI Confidence: **99.24%**
125. **`crates/nu-command/src/strings/ansi/ansi_.rs`** -> AI Confidence: **99.24%**
126. **`crates/nu-command/src/strings/mod.rs`** -> AI Confidence: **99.24%**
127. **`crates/nu-command/src/strings/str_/length.rs`** -> AI Confidence: **99.24%**
128. **`crates/nu-command/src/viewers/griddle.rs`** -> AI Confidence: **99.24%**
129. **`crates/nu-command/src/viewers/table.rs`** -> AI Confidence: **99.24%**
130. **`crates/nu-derive-value/src/attributes.rs`** -> AI Confidence: **99.24%**
131. **`crates/nu-engine/src/call_ext.rs`** -> AI Confidence: **99.24%**
132. **`crates/nu-engine/src/compile/builder.rs`** -> AI Confidence: **99.24%**
133. **`crates/nu-engine/src/eval_helpers.rs`** -> AI Confidence: **99.24%**
134. **`crates/nu-explore/src/explore/nu_common/value.rs`** -> AI Confidence: **99.24%**
135. **`crates/nu-explore/src/explore_config/app.rs`** -> AI Confidence: **99.24%**
136. **`crates/nu-explore/src/explore_config/tui.rs`** -> AI Confidence: **99.24%**
137. **`crates/nu-explore/src/explore_regex/ui.rs`** -> AI Confidence: **99.24%**
138. **`crates/nu-json/src/de.rs`** -> AI Confidence: **99.24%**
139. **`crates/nu-parser/src/parse_keywords.rs`** -> AI Confidence: **99.24%**
140. **`crates/nu-parser/src/parse_patterns.rs`** -> AI Confidence: **99.24%**
141. **`crates/nu-parser/src/parse_shape_specs.rs`** -> AI Confidence: **99.24%**
142. **`crates/nu-plugin-core/src/communication_mode/mod.rs`** -> AI Confidence: **99.24%**
143. **`crates/nu-plugin-engine/src/interface/tests.rs`** -> AI Confidence: **99.24%**
144. **`crates/nu-plugin/src/plugin/command.rs`** -> AI Confidence: **99.24%**
145. **`crates/nu-protocol/src/ast/block.rs`** -> AI Confidence: **99.24%**
146. **`crates/nu-protocol/src/ast/unit.rs`** -> AI Confidence: **99.24%**
147. **`crates/nu-protocol/src/engine/stack.rs`** -> AI Confidence: **99.24%**
148. **`crates/nu-protocol/src/errors/parse_error.rs`** -> AI Confidence: **99.24%**
149. **`crates/nu-protocol/src/errors/shell_error/mod.rs`** -> AI Confidence: **99.24%**
150. **`crates/nu-protocol/src/pipeline/pipeline_data.rs`** -> AI Confidence: **99.24%**
151. **`crates/nu-protocol/src/process/child.rs`** -> AI Confidence: **99.24%**
152. **`crates/nu-protocol/src/signature.rs`** -> AI Confidence: **99.24%**
153. **`crates/nu-protocol/src/span.rs`** -> AI Confidence: **99.24%**
154. **`crates/nu-protocol/src/value/filesize.rs`** -> AI Confidence: **99.24%**
155. **`crates/nu-table/src/types/general.rs`** -> AI Confidence: **99.24%**
156. **`crates/nu-test-support-macros/src/test.rs`** -> AI Confidence: **99.24%**
157. **`crates/nu-test-support/src/harness/group.rs`** -> AI Confidence: **99.24%**
158. **`crates/nu-utils/src/strings/unique.rs`** -> AI Confidence: **99.24%**
159. **`crates/nu_plugin_custom_values/src/generate2.rs`** -> AI Confidence: **99.24%**
160. **`crates/nu_plugin_custom_values/src/handle_get.rs`** -> AI Confidence: **99.24%**
161. **`crates/nu_plugin_custom_values/src/handle_update.rs`** -> AI Confidence: **99.24%**
162. **`crates/nu_plugin_example/src/commands/arg_completion.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `crates/nu-command/tests/commands/find.rs` -> **100.0%** Exposure
- `crates/nu-command/tests/commands/run_external.rs` -> **0.0001%** Exposure
### Exploit Generation Surface
- `crates/nu_plugin_python/nu_plugin_python_example.py` -> **100.0%** Exposure
- `benches/benchmarks.rs` -> **20.0%** Exposure
- `crates/nu-cli/src/commands/history/history_import.rs` -> **20.0%** Exposure
- `crates/nu-cli/src/completions/arg_value_completion.rs` -> **20.0%** Exposure
- `crates/nu-cli/src/completions/command_completions.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `crates/nu-protocol/src/errors/shell_error/io.rs` -> **100.0%** Exposure
- `crates/nu-test-support/src/playground/nu_process.rs` -> **100.0%** Exposure
- `crates/nu_plugin_query/src/web_tables.rs` -> **100.0%** Exposure
- `crates/nu-plugin/src/plugin/mod.rs` -> **99.9998%** Exposure
- `src/terminal.rs` -> **99.9985%** Exposure
### Raw Memory Manipulation
- `tests/repl/test_parser.rs` -> **0.8781%** Exposure
- `tests/repl/test_custom_commands.rs` -> **0.0038%** Exposure
- `crates/nu-protocol/src/value/record.rs` -> **0.0007%** Exposure
- `crates/nu-experimental/src/lib.rs` -> **0.0005%** Exposure
- `crates/nu-system/src/netbsd.rs` -> **0.0005%** Exposure
### Algorithmic DoS Exposure
- `crates/nu-cli/src/commands/history/history_.rs` -> **100.0%** Exposure
- `crates/nu-cli/src/commands/history/history_import.rs` -> **100.0%** Exposure
- `crates/nu-cli/src/commands/keybindings_listen.rs` -> **100.0%** Exposure
- `crates/nu-cli/src/completions/arg_value_completion.rs` -> **100.0%** Exposure
- `crates/nu-cli/src/completions/attribute_completions.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15919` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/nu-test-support/src/playground/nu_process.rs` (RUST) -> Cumulative Risk: **780.91**
- **Archetype:** `file_cluster_0` (Distance: 12.289 IQR)
- **Magnitude:** 102.68 | **LOC:** 100 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `fmt` (Impact: 28.2), `construct` (Impact: 22.2), `arg` (Impact: 5.4)

### 2. `crates/nu-protocol/src/pipeline/byte_stream.rs` (RUST) -> Cumulative Risk: **776.72**
- **Archetype:** `file_cluster_0` (Distance: 14.376 IQR)
- **Magnitude:** 1505.88 | **LOC:** 1301 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9989%)
- **Heaviest Functions:** `next_string` (Impact: 200.3), `fill_buf` (Impact: 101.5), `read` (Impact: 63.2)

### 3. `crates/nu-command/src/formats/from/msgpack.rs` (RUST) -> Cumulative Risk: **773.17**
- **Archetype:** `file_cluster_16` (Distance: 12.445 IQR)
- **Magnitude:** 512.52 | **LOC:** 560 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (94.1788%), Concurrency (85.2876%)
- **Heaviest Functions:** `read_msgpack` (Impact: 309.5), `run` (Impact: 48.3), `from` (Impact: 36.6)

### 4. `crates/nu-test-support/src/playground/play.rs` (RUST) -> Cumulative Risk: **772.37**
- **Archetype:** `file_cluster_0` (Distance: 11.17 IQR)
- **Magnitude:** 242.18 | **LOC:** 245 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9939%)
- **Heaviest Functions:** `symlink` (Impact: 51.4), `with_files` (Impact: 20.2), `glob_vec` (Impact: 18.6)

### 5. `crates/nu-command/src/network/http/interruptible_unix.rs` (RUST) -> Cumulative Risk: **771.84**
- **Archetype:** `file_cluster_13` (Distance: 12.831 IQR)
- **Magnitude:** 298.44 | **LOC:** 320 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9831%)
- **Heaviest Functions:** `connect` (Impact: 55.3), `transmit_output` (Impact: 37.0), `make_on_connect_unix` (Impact: 36.5)

### 6. `src/test_bins.rs` (RUST) -> Cumulative Risk: **767.5**
- **Archetype:** `file_cluster_17` (Distance: 13.044 IQR)
- **Magnitude:** 407.3 | **LOC:** 552 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `nu_repl` (Impact: 62.4), `did_chop_arguments` (Impact: 22.8), `run` (Impact: 21.8)

### 7. `crates/nu-explore/src/explore/commands/expand.rs` (RUST) -> Cumulative Risk: **757.39**
- **Archetype:** `file_cluster_13` (Distance: 12.288 IQR)
- **Magnitude:** 87.8 | **LOC:** 77 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (99.7635%), Algorithmic Dos (98.5528%)
- **Heaviest Functions:** `convert_value_to_string` (Impact: 36.8), `spawn` (Impact: 21.9), `new` (Impact: 2.7)

### 8. `crates/nu-plugin-test-support/src/spawn_fake_plugin.rs` (RUST) -> Cumulative Risk: **740.46**
- **Archetype:** `file_cluster_13` (Distance: 12.389 IQR)
- **Magnitude:** 89.08 | **LOC:** 93 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (94.0431%), Algorithmic Dos (92.16%)
- **Heaviest Functions:** `spawn_fake_plugin` (Impact: 42.5), `write` (Impact: 4.7), `read` (Impact: 3.1)

### 9. `crates/nu-protocol/src/value/record.rs` (RUST) -> Cumulative Risk: **739.18**
- **Archetype:** `file_cluster_0` (Distance: 17.736 IQR)
- **Magnitude:** 691.24 | **LOC:** 958 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (96.18%)
- **Heaviest Functions:** `visit_map` (Impact: 26.8), `from_raw_cols_vals` (Impact: 19.2), `insert` (Impact: 16.4)

### 10. `crates/nu-protocol/src/config/helper.rs` (RUST) -> Cumulative Risk: **733.03**
- **Archetype:** `file_cluster_16` (Distance: 13.645 IQR)
- **Magnitude:** 275.26 | **LOC:** 172 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9974%)
- **Heaviest Functions:** `update` (Impact: 45.0), `update` (Impact: 28.5), `config_update_string_enum` (Impact: 20.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/nu-protocol/src/value/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.709 IQR)
- **Top Global Matches:** file_cluster_8: 13.709, file_cluster_7: 13.982, file_cluster_16: 13.989
- **Magnitude:** 5000.96 | **LOC:** 4827 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (5.4396%), Tech Debt (50.7892%)
**Top Internal Functions/Classes:**
  * `to_debug_string` (Impact: 1250.5 | O(N^6) | DB: 10)
  * `modulo` (Impact: 790.8 | O(2^N))
  * `floor_div` (Impact: 368.1 | O(N^6))
  * `div` (Impact: 248.7 | O(N^6))
  * `add` (Impact: 176.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 401`, `args: 272`, `func_start: 160`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 45`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 51`
* *Architecture:* `api: 133`, `import: 37`
* *Defense:* `safety: 1104`, `doc: 323`, `test: 83`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fmt::Debug, custom_value::CustomValue, Serialize, ops::Bound, glob::*, into_value::IntoValue, Math, crate::Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/platform/input/list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.886 IQR)
- **Top Global Matches:** file_cluster_8: 12.886, file_cluster_17: 13.248, file_cluster_7: 13.278
- **Magnitude:** 4290.74 | **LOC:** 3702 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (34.3381%), Tech Debt (8.2584%)
**Top Internal Functions/Classes:**
  * `from_nu_config` (Impact: 3836.9 | O(2^N) | DB: 37)
  * `default` (Impact: 7.9 | O(2^N))
  * `table_mode_to_separator` (Impact: 7.0 | O(N^2))
    * *Intent:* /// Maps TableMode to the appropriate vertical separator character
  * `table_mode_to_header_separator` (Impact: 7.0 | O(N^2))
    * *Intent:* /// Maps TableMode to (horizontal_line_char, intersection_char) for header separator
  * `test_examples` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 571`, `args: 134`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 365`, `orphaned_logic: 3`
* *Architecture:* `import: 15`
* *Defense:* `safety: 230`, `doc: 98`, `test: 18`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` terminal::
        self, std::
    collections::HashSet, nu_ansi_term::Style, ClearType, disable_raw_mode, nu_color_config::Alignment, UnicodeWidthStr, ansi::RESET...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.872 IQR)
- **Top Global Matches:** file_cluster_8: 12.872, file_cluster_17: 13.18, file_cluster_0: 13.196
- **Magnitude:** 3378.22 | **LOC:** 7520 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (14.746%), Tech Debt (37.8761%)
**Top Internal Functions/Classes:**
  * `parse_unit_value` (Impact: 412.2 | O(2^N) | DB: 1)
  * `find_longest_decl_with_prefix` (Impact: 352.1 | O(N^6) | DB: 5)
  * `parse_short_flags` (Impact: 160.8 | O(N^6) | DB: 4)
  * `parse_full_cell_path` (Impact: 160.5 | O(N^5) | DB: 5)
  * `parse_cell_path` (Impact: 155.5 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 466`, `args: 107`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 194`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 9`, `orphaned_logic: 15`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 342`, `doc: 30`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` parse_shape_name, parse_patterns::parse_pattern, parse_shape_specs::parse_completer, lite_parser::LiteCommand, sync::Arc, is_assignment_operator, itertools::Itertools, TokenContents...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/parse_keywords.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.723 IQR)
- **Top Global Matches:** file_cluster_8: 12.723, file_cluster_17: 12.843, file_cluster_0: 12.951
- **Magnitude:** 3023.94 | **LOC:** 4122 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (12.7966%), Tech Debt (22.3117%)
**Top Internal Functions/Classes:**
  * `parse_export_in_module` (Impact: 2406.9 | O(2^N) | DB: 36)
  * `parse_alias` (Impact: 357.2 | O(N^6) | DB: 1)
  * `parse_export_in_block` (Impact: 44.1 | O(N^5) | DB: 2)
  * `warp_export_call` (Impact: 26.3 | O(N^4) | DB: 4)
  * `parse_keyword` (Impact: 11.2 | O(N^3) | DB: 1)
    * *Intent:* /// This is a new more compact method of calling parse_xxx() functions without repeating the /// par...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 364`, `args: 42`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 121`, `dead_code: 8`, `planned_debt: 5`, `fragile_debt: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 208`, `doc: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parse_call, parser::
        ArgumentParsingLevel, nu_protocol::FromValue, sync::Arc, TokenContents, PluginRegistryFile, known_external::KnownExternal, HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.064 IQR)
- **Top Global Matches:** file_cluster_8: 13.064, file_cluster_17: 13.197, file_cluster_0: 13.323
- **Magnitude:** 2544.8 | **LOC:** 1957 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.6068%), Tech Debt (23.1068%)
**Top Internal Functions/Classes:**
  * `series_to_values` (Impact: 1774.9 | O(2^N) | DB: 1)
  * `input_type_list_to_series` (Impact: 303.3 | O(2^N) | DB: 4)
  * `any_value_to_value` (Impact: 98.3 | O(2^N) | DB: 2)
  * `test_any_value_to_value` (Impact: 85.1 | O(N^3))
  * `datetime_from_epoch_nanos` (Impact: 23.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 255`, `args: 94`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`, `dead_code: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 2`, `import: 25`
* *Defense:* `safety: 354`, `test: 53`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` polars::prelude::Field, polars::datatypes::AnyValue, StructChunked, NuDataFrame, polars_io::prelude::StructArray, polars::prelude::
    CatSize, Value, ListBuilderTrait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/ast/traverse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.538 IQR)
- **Top Global Matches:** file_cluster_16: 11.538, file_cluster_8: 11.771, file_cluster_17: 11.983
- **Magnitude:** 2351.11 | **LOC:** 302 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.2391%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 40`, `args: 38`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 26`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::
    Block, Expr, ListItem, crate::engine::StateWorkingSet, PipelineRedirection, Expression, MatchPattern, RecordItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/eval_ir.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.361 IQR)
- **Top Global Matches:** file_cluster_8: 13.361, file_cluster_0: 13.526, file_cluster_17: 13.569
- **Magnitude:** 2297.98 | **LOC:** 1838 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (19.2963%), Tech Debt (15.531%)
**Top Internal Functions/Classes:**
  * `eval_instruction` (Impact: 1922.2 | O(N^6) | DB: 37)
  * `eval_ir_block_impl` (Impact: 105.2 | O(N^5) | DB: 3)
  * `eval_ir_block` (Impact: 55.6 | O(N^5) | DB: 6)
  * `prepare_error_handler` (Impact: 32.8 | O(N^6) | DB: 1)
  * `clone_reg` (Impact: 18.6 | O(N^5) | DB: 1)
    * *Intent:* /// Clone data from a register. Must be collected first.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 250`, `args: 44`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 117`, `planned_debt: 2`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 9`
* *Defense:* `safety: 240`, `doc: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Redirection, nu_utils::IgnoreCaseExt, Closure, PipelineData, sync::Arc, Math, ir::Call, crate::
    ENV_CONVERSIONS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-plugin-engine/src/interface/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.621 IQR)
- **Top Global Matches:** file_cluster_16: 13.621, file_cluster_8: 13.643, file_cluster_13: 13.777
- **Magnitude:** 2088.88 | **LOC:** 1482 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (17.7187%), Tech Debt (14.6604%)
**Top Internal Functions/Classes:**
  * `spawn_engine_call_handler` (Impact: 1791.2 | O(2^N) | DB: 22)
  * `get_signals` (Impact: 37.8 | O(N^5) | DB: 2)
  * `recv_stream_ended` (Impact: 32.0 | O(N^5) | DB: 2)
  * `drop` (Impact: 24.4 | O(2^N) | DB: 1)
    * *Intent:* /// Channel for plugin custom values that should be kept alive for the duration of the plugin /// ca...
  * `receive_plugin_call_subscriptions` (Impact: 20.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 151`, `args: 41`, `func_start: 36`, `class_start: 6`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 17`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 193`, `doc: 110`, `test: 1`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PipelineData, EngineCallId, util::Waitable, DynamicSuggestion, sync::Arc, btree_map, GetCompletionInfo, with_custom_values_in...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/tests/test_parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.267 IQR)
- **Top Global Matches:** file_cluster_0: 12.267, file_cluster_8: 12.686, file_cluster_11: 12.864
- **Magnitude:** 2026.46 | **LOC:** 3252 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 101
- **Risk Profile:** Cognitive Load (9.5345%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare_rhs_binary_op` (Impact: 846.3 | O(N^6) | DB: 101)
  * `test_int` (Impact: 44.9 | O(N^4) | DB: 2)
  * `parse_right_unbounded_range` (Impact: 42.5 | O(N^5) | DB: 2)
  * `parse_left_unbounded_range` (Impact: 42.5 | O(N^5) | DB: 2)
  * `parse_float_range` (Impact: 42.5 | O(N^5) | DB: 2)
    * *Intent:* #[case(b"-10..-3", RangeInclusion::Inclusive, "negative inclusive")] #[case(b"-10..=-3", RangeInclus...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 670`, `args: 71`, `func_start: 148`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 7`, `state_mutation: 244`, `dead_code: 4`, `planned_debt: 14`, `duplicate_logic: 65`, `orphaned_logic: 26`
* *Architecture:* `api: 61`, `import: 18`
* *Defense:* `safety: 268`, `doc: 4`, `test: 348`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PipelineData, Mut, ExternalArgument, nu_parser::*, nu_protocol::ast::RecordItem, Type, StateWorkingSet, Let...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/filesystem/save.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.754 IQR)
- **Top Global Matches:** file_cluster_8: 12.754, file_cluster_17: 12.89, file_cluster_13: 12.921
- **Magnitude:** 1828.28 | **LOC:** 584 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (20.7482%), Tech Debt (17.083%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 1764.9 | O(2^N) | DB: 45)
  * `signature` (Impact: 5.1 | O(N^4))
  * `search_terms` (Impact: 4.1 | O(N^3))
  * `name` (Impact: 2.7 | O(N^2))
  * `description` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 81`, `args: 28`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 106`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DataSource, nu_engine::command_prelude::*, std::
    borrow::Cow, BufRead, shell_error::io::IoError, path::Path, OutDest, Read...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/database/values/sqlite.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.873 IQR)
- **Top Global Matches:** file_cluster_8: 12.873, file_cluster_0: 12.9, file_cluster_16: 12.959
- **Magnitude:** 1508.0 | **LOC:** 1591 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (7.6167%), Tech Debt (99.8372%)
**Top Internal Functions/Classes:**
  * `prepared_statement_to_nu_list` (Impact: 79.8 | O(N^5) | DB: 2)
  * `split_select_expressions` (Impact: 74.2 | O(N^5) | DB: 4)
    * *Intent:* /// Parses a SELECT projection list into `(output_name, expression)` entries. /// /// Input is the t...
  * `open_connection` (Impact: 73.7 | O(2^N))
  * `count` (Impact: 53.4 | O(2^N) | DB: 2)
  * `nu_value_to_params` (Impact: 49.1 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 239`, `args: 115`, `func_start: 90`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 2`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 18`, `orphaned_logic: 30`
* *Architecture:* `io: 1`, `api: 55`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 209`, `doc: 60`, `test: 46`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PipelineData, db_index::DbIndex, Serialize, tempfile::NamedTempFile, Spanned, shell_error::io::IoError, path::Path, Record...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/pipeline/byte_stream.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.376 IQR)
- **Top Global Matches:** file_cluster_0: 14.376, file_cluster_16: 14.505, file_cluster_13: 14.561
- **Magnitude:** 1505.88 | **LOC:** 1301 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (27.5541%), Tech Debt (99.9989%)
**Top Internal Functions/Classes:**
  * `next_string` (Impact: 200.3 | O(2^N) | DB: 7)
  * `fill_buf` (Impact: 101.5 | O(2^N) | DB: 13)
  * `read` (Impact: 63.2 | O(2^N) | DB: 2)
  * `into_bytes` (Impact: 61.8 | O(2^N) | DB: 6)
  * `copy_with_signals` (Impact: 60.7 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 221`, `args: 34`, `func_start: 71`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 173`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 27`, `orphaned_logic: 17`
* *Architecture:* `io: 3`, `api: 52`, `concurrency: 25`, `import: 10`
* *Defense:* `safety: 207`, `doc: 178`, `test: 17`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorKind, PipelineData, Serialize, crate::
    IntRange, BufRead, Type, Read, std::os::windows::io::OwnedHandle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/flatten.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.763 IQR)
- **Top Global Matches:** file_cluster_8: 11.763, file_cluster_17: 12.164, file_cluster_0: 12.221
- **Magnitude:** 1488.38 | **LOC:** 701 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.097%), Tech Debt (13.1644%)
**Top Internal Functions/Classes:**
  * `flatten_expression_into` (Impact: 1166.4 | O(2^N) | DB: 6)
  * `flatten_pattern_into` (Impact: 156.8 | O(2^N) | DB: 1)
  * `flatten_pipeline_element_into` (Impact: 68.0 | O(N^5) | DB: 1)
  * `flatten_positional_arg_into` (Impact: 16.6 | O(N^2) | DB: 1)
  * `flatten_block_into` (Impact: 7.8 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 85`, `args: 14`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fmt::Display, ExternalArgument, PipelineRedirection, engine::StateWorkingSet, Block, Result, PipelineElement, nu_protocol::
    DeclId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore/pager/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.418 IQR)
- **Top Global Matches:** file_cluster_8: 13.418, file_cluster_0: 13.424, file_cluster_13: 13.483
- **Magnitude:** 1388.56 | **LOC:** 1135 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (58.0562%), Tech Debt (22.4524%)
**Top Internal Functions/Classes:**
  * `render_ui` (Impact: 1099.5 | O(N^6) | DB: 62)
  * `run` (Impact: 44.3 | O(N^3) | DB: 7)
  * `new` (Impact: 7.0 | O(N^3))
  * `new` (Impact: 4.4 | O(N^3))
  * `show_message` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 210`, `args: 45`, `func_start: 32`, `class_start: 11`
* *Risk/State:* `state_mutation: 182`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 143`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` title_bar::TitleBar, crossterm::
    event::KeyCode, ClearType, disable_raw_mode, UnicodeWidthStr, ratatui::backend::CrosstermBackend, execute, nu_protocol::
    Value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore_config/tree.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.124 IQR)
- **Top Global Matches:** file_cluster_8: 11.124, file_cluster_0: 11.384, file_cluster_16: 11.447
- **Magnitude:** 1308.0 | **LOC:** 700 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (5.9964%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filter_tree_items_recursive` (Impact: 1063.3 | O(2^N) | DB: 13)
    * *Intent:* /// 1. Have an identifier that contains the query string (case-insensitive match) /// 2. Have descen...
  * `print_json_tree` (Impact: 189.8 | O(2^N) | DB: 1)
    * *Intent:* /// Print a JSON tree structure to stdout (for CLI mode)
  * `is_leaf` (Impact: 4.2 | O(N^1))
    * *Intent:* /// Check if a JSON value is a leaf node (not an object or array)
  * `render_leaf` (Impact: 2.1 | O(N^1) | DB: 2)
    * *Intent:* /// Render a leaf value as a string
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 105`, `args: 47`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* `safety: 34`, `doc: 52`, `test: 54`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::HashMap, tui_tree_widget::TreeItem, serde_json::Value, crate::explore_config::types::NodeInfo, NuValueType, super::*, ValueType
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/compile/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.701 IQR)
- **Top Global Matches:** file_cluster_8: 10.701, file_cluster_7: 11.404, file_cluster_13: 11.418
- **Magnitude:** 1307.1 | **LOC:** 609 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.6816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compile_expression` (Impact: 1285.3 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 36`, `args: 10`, `func_start: 2`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` compile_block, engine::StateWorkingSet, CompileError, ir::DataSlice, compile_load_env, RedirectModes, compile_call, Expression...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/value/range.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.052 IQR)
- **Top Global Matches:** file_cluster_8: 12.052, file_cluster_16: 12.256, file_cluster_13: 12.272
- **Magnitude:** 1250.64 | **LOC:** 711 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.8216%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 179.8 | O(N^6))
  * `new` (Impact: 123.3 | O(N^6))
  * `cmp` (Impact: 110.7 | O(2^N))
  * `cmp` (Impact: 62.6 | O(N^6))
  * `contains` (Impact: 58.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 102`, `args: 38`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `planned_debt: 1`, `duplicate_logic: 36`
* *Architecture:* `api: 45`, `import: 14`
* *Defense:* `safety: 119`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Serialize, ops::Bound, crate::IntRange, crate::ShellError, fmt::Display, core::ops::Bound, Range, ast::RangeInclusion...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/eval_base.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.493 IQR)
- **Top Global Matches:** file_cluster_16: 12.493, file_cluster_8: 12.548, file_cluster_17: 12.662
- **Magnitude:** 1227.78 | **LOC:** 419 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (13.4526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `eval` (Impact: 1190.1 | O(2^N) | DB: 7)
    * *Intent:* /// State that needs to be mutated. /// This is the stack for regular eval, and unused by const eval
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 69`, `args: 23`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 29`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 75`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ast::
        Assignment, sync::Arc, Math, ExternalArgument, Operator, nu_path::expand_path, Range, Record...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/documentation.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.083 IQR)
- **Top Global Matches:** file_cluster_8: 12.083, file_cluster_0: 12.193, file_cluster_13: 12.228
- **Magnitude:** 1203.98 | **LOC:** 991 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (8.0877%), Tech Debt (8.0808%)
**Top Internal Functions/Classes:**
  * `highlight_capture_group` (Impact: 772.6 | O(2^N) | DB: 10)
    * *Intent:* /// Apply code highlighting to code in a capture group
  * `get_full_help` (Impact: 82.1 | O(2^N) | DB: 7)
  * `write_positional` (Impact: 79.1 | O(N^5) | DB: 2)
  * `write_flag_to_long_desc` (Impact: 55.4 | O(N^4) | DB: 2)
  * `update_ansi_from_config` (Impact: 49.3 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 120`, `args: 35`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 68`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 52`, `doc: 30`, `test: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fancy_regex::Captures, PipelineData, sync::Arc, std::
    borrow::Cow, crate::eval_call, UNKNOWN_SPAN_ID, Spanned, Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/conversions/into/datetime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.35 IQR)
- **Top Global Matches:** file_cluster_8: 11.35, file_cluster_0: 11.655, file_cluster_13: 11.975
- **Magnitude:** 1168.2 | **LOC:** 1188 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.5144%), Tech Debt (10.9411%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 1140.5 | O(2^N) | DB: 3)
  * `take_cell_paths` (Impact: 3.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 164`, `args: 37`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 6`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 188`, `test: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nu_engine::command_prelude::*, Utc, NaiveDateTime, chrono::
    DateTime, IntoDatetime, Timelike, NaiveDate, TimeZone...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/compile/keyword.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.251 IQR)
- **Top Global Matches:** file_cluster_8: 11.251, file_cluster_7: 11.643, file_cluster_13: 11.716
- **Magnitude:** 1153.42 | **LOC:** 1131 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.8076%), Tech Debt (8.2866%)
**Top Internal Functions/Classes:**
  * `compile_if` (Impact: 901.2 | O(N^6) | DB: 3)
    * *Intent:* /// Compile a call to `if` as a branch-if
  * `compile_while` (Impact: 88.4 | O(N^2) | DB: 1)
  * `compile_loop` (Impact: 70.6 | O(N^2) | DB: 1)
  * `compile_closure_call` (Impact: 65.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 69`, `args: 15`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 67`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` compile_expression, RedirectModes, ir::Instruction, ast::Block, Call, Expr, VarId, Expression...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/command.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.592 IQR)
- **Top Global Matches:** file_cluster_0: 12.592, file_cluster_8: 12.594, file_cluster_16: 12.711
- **Magnitude:** 1153.24 | **LOC:** 1567 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (21.3921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_cli_args` (Impact: 392.3 | O(N^6) | DB: 27)
    * *Intent:* // Parse CLI args into nushell options and script details.
  * `parse_experimental_options` (Impact: 136.7 | O(N^5) | DB: 3)
    * *Intent:* // Parse experimental options, allowing bracketed and comma-delimited forms.
  * `parse_log_filters` (Impact: 105.6 | O(N^6) | DB: 1)
    * *Intent:* // Parse log filters and ensure they match known log levels. // Supports multiple formats: [error,wa...
  * `prevalidate_short_groups_before_lexopt` (Impact: 57.2 | O(N^4) | DB: 2)
    * *Intent:* // Validate combined short flags and reject unsupported inline values.
  * `parse_validated_option` (Impact: 44.2 | O(N^4) | DB: 1)
    * *Intent:* // Parse and validate a string value against a list of allowed values. // Returns the normalized (tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 193`, `args: 65`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 121`
* *Architecture:* `api: 41`, `import: 12`
* *Defense:* `safety: 178`, `test: 24`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std::
    ffi::OsString, ShellError, fmt::self, std::ffi::OsString, nu_experimental, nu_protocol::
    LabeledError, Spanned, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/ty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.938 IQR)
- **Top Global Matches:** file_cluster_0: 11.938, file_cluster_8: 11.963, file_cluster_13: 12.005
- **Magnitude:** 1146.8 | **LOC:** 735 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (8.913%), Tech Debt (12.7519%)
**Top Internal Functions/Classes:**
  * `follow_cell_path_recursive` (Impact: 1077.4 | O(2^N) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 113`, `args: 32`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 61`, `doc: 21`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ast::PathMember, std::collections::HashMap, super::Type, Serialize, strum::IntoEnumIterator, serde::Deserialize, std::fmt::Write, std::borrow::Cow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/engine_state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.816 IQR)
- **Top Global Matches:** file_cluster_0: 13.816, file_cluster_13: 14.032, file_cluster_16: 14.039
- **Magnitude:** 1098.52 | **LOC:** 1444 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (18.0495%), Tech Debt (99.7806%)
**Top Internal Functions/Classes:**
  * `cwd` (Impact: 168.3 | O(2^N))
  * `update_plugin_file` (Impact: 49.0 | O(N^5) | DB: 15)
  * `merge_env` (Impact: 43.0 | O(N^5) | DB: 7)
  * `find_decl_name` (Impact: 35.9 | O(N^6) | DB: 1)
  * `which_module_has_decl` (Impact: 27.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 223`, `args: 126`, `func_start: 99`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 131`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 48`
* *Architecture:* `io: 6`, `api: 90`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 158`, `doc: 95`, `test: 33`, `sync_locks: 11`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HistoryConfig, OverlayId, DEFAULT_OVERLAY_NAME, EnvName, ThreadJob, std::
    collections::HashMap, Value, Variable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/pattern_match.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.019 IQR)
- **Top Global Matches:** file_cluster_8: 11.019, file_cluster_11: 11.521, file_cluster_13: 11.564
- **Magnitude:** 1087.58 | **LOC:** 260 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (28.9144%), Tech Debt (99.5398%)
**Top Internal Functions/Classes:**
  * `match_value` (Impact: 1044.4 | O(2^N) | DB: 6)
  * `match_value` (Impact: 13.8 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 43`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RangeInclusion, VarId, crate::
    Span, ast::Expr, Value, MatchPattern, Pattern
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/command.rs` (RUST) | Magnitude: 1153.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1147, structural_boundaries: 193, safety: 178, branch: 147
- `crates/nu-command/src/network/mod.rs` (RUST) | Magnitude: 20.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, decorators: 7, api: 5, encapsulation: 5
- `crates/nu-command/tests/commands/path/parse.rs` (RUST) | Magnitude: 43.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, test: 20, args: 19, structural_boundaries: 14
- `crates/nu-command/tests/commands/network/http/post.rs` (RUST) | Magnitude: 131.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 72, test: 33, safety: 31
- `crates/nu-plugin/src/plugin/mod.rs` (RUST) | Magnitude: 288.38 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 532, doc: 156, structural_boundaries: 120, safety: 78

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/nu-command/src/viewers/table.rs` (RUST) | Magnitude: 653.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 441, structural_boundaries: 114, safety: 75, branch: 74
- `crates/nu-utils/src/downcast.rs` (RUST) | Magnitude: 21.38 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, indent_spaces: 11, safety: 10, structural_boundaries: 9
- `crates/nu-command/src/network/http/timeout_extractor_reader.rs` (RUST) | Magnitude: 51.06 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, io: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/nu-cli/tests/completions/support/completions_helpers.rs` (RUST) | Magnitude: 191.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 208, structural_boundaries: 55, args: 23, safety: 21
- `crates/nu-plugin-test-support/src/spawn_fake_plugin.rs` (RUST) | Magnitude: 89.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 27, concurrency: 27, generics: 20
- `crates/nu-protocol/src/engine/jobs.rs` (RUST) | Magnitude: 480.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 69, safety: 66, state_mutation: 52
- `crates/nu_plugin_polars/src/dataframe/values/nu_selector/custom_value.rs` (RUST) | Magnitude: 57.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 15, args: 10, func_start: 10
- `crates/nu-protocol/src/module.rs` (RUST) | Magnitude: 96.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 86, api: 33, encapsulation: 26, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/nu-protocol/src/pipeline/metadata.rs` (RUST) | Magnitude: 58.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, doc: 21, api: 14, encapsulation: 10
- `crates/nu-protocol/src/ast/range.rs` (RUST) | Magnitude: 19.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 5, encapsulation: 5, indent_spaces: 4, structural_boundaries: 3
- `crates/nu-mcp/src/history.rs` (RUST) | Magnitude: 62.58 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 17, doc: 13, safety: 12
- `crates/nu-experimental/src/options/mod.rs` (RUST) | Magnitude: 8.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 36, indent_spaces: 20, structural_boundaries: 9, immutability_locks: 6
- `crates/nu-command/src/database/values/definitions/db_table.rs` (RUST) | Magnitude: 20.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 6, encapsulation: 6, indent_spaces: 5, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/nu-cmd-plugin/src/util.rs` (RUST) | Magnitude: 203.84 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 25, safety: 24, branch: 23
- `crates/nu-derive-value/src/from.rs` (RUST) | Magnitude: 194.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 357, indent_spaces: 166, structural_boundaries: 45, safety: 35
- `crates/nu-cli/src/completions/completer.rs` (RUST) | Magnitude: 781.84 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 619, structural_boundaries: 159, branch: 74, state_mutation: 74
- `crates/nu-protocol/src/errors/labeled_error.rs` (RUST) | Magnitude: 134.24 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 115, doc: 101, generics: 46, safety: 32
- `crates/nu-utils/src/split_read.rs` (RUST) | Magnitude: 111.6 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 119, safety: 49, structural_boundaries: 48, test: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/nu-command/src/experimental/job_spawn.rs` (RUST) | Magnitude: 128.5 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 27, safety: 22, concurrency: 16
- `crates/nu-plugin-core/src/serializers/mod.rs` (RUST) | Magnitude: 67.06 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 17, doc: 17, concurrency: 12
- `crates/nu-plugin-core/src/interface/stream/tests.rs` (RUST) | Magnitude: 165.82 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 120, concurrency: 54, safety: 51, structural_boundaries: 43
- `crates/nu-test-support/src/deprecated/commands.rs` (RUST) | Magnitude: 52.58 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 20, structural_boundaries: 17, safety: 7
- `scripts/coverage-local.sh` (SHELL) | Magnitude: 1.23 | Delta: **0.486 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 6, indent_spaces: 6, structural_boundaries: 4, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/nu-plugin-test-support/src/lib.rs` (RUST) | Magnitude: 14.12 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 102, structural_boundaries: 6, api: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/nu-cli/src/completions/env_var_completions.rs` (RUST) | Magnitude: 23.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 11, import: 4, generics: 3
- `crates/nu-explore/src/explore/pager/mod.rs` (RUST) | Magnitude: 1388.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 707, structural_boundaries: 210, state_mutation: 182, safety: 143
- `crates/nu-protocol/src/plugin/identity.rs` (RUST) | Magnitude: 95.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 113, doc: 21, branch: 16, structural_boundaries: 16
- `crates/nu-protocol/src/syntax_shape.rs` (RUST) | Magnitude: 173.96 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 127, doc: 58, branch: 15, structural_boundaries: 13
- `crates/nu-command/tests/commands/network/http/patch.rs` (RUST) | Magnitude: 76.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 46, test: 21, safety: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/nu-utils/src/flatten_json.rs` (RUST) | Magnitude: 500.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 163, doc: 74, branch: 34, structural_boundaries: 28

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/nu-test-support/src/tester/mod.rs` -> Churn: **93.15%** | Cog Load: 4.8483% | Debt: 80.6218%
- `crates/nu-protocol/src/errors/shell_error/mod.rs` -> Churn: **84.76%** | Cog Load: 3.7999% | Debt: 98.0069%
- `crates/nu-command/src/network/http/client.rs` -> Churn: **84.51%** | Cog Load: 11.8748% | Debt: 63.3853%
- `crates/nu-cli/src/util.rs` -> Churn: **69.9%** | Cog Load: 7.2819% | Debt: 96.3358%
- `crates/nu-command/src/filters/default.rs` -> Churn: **69.9%** | Cog Load: 17.2178% | Debt: 77.9209%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/nu-protocol/src/value/mod.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 5000.96
- `crates/nu-protocol/src/pipeline/byte_stream.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 1505.88
- `crates/nu-engine/src/compile/expression.rs` -> **Ray** (100.0% isolated ownership) | Magnitude: 1307.1
- `crates/nu-engine/src/compile/keyword.rs` -> **Wind** (100.0% isolated ownership) | Magnitude: 1153.42
- `crates/nu-protocol/src/engine/engine_state.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 1098.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/nu_plugin_polars/src/dataframe/command/data/col.rs` -> **Severity: 771.4** (Blast Radius: 7.714 * Doc Risk: 100.0%)
- `crates/nu_plugin_polars/src/dataframe/command/data/lit.rs` -> **Severity: 437.075** (Blast Radius: 4.376 * Doc Risk: 99.8801%)
- `crates/nu-protocol/src/did_you_mean.rs` -> **Severity: 279.475** (Blast Radius: 2.945 * Doc Risk: 94.8981%)
- `crates/nu-test-support/src/fs.rs` -> **Severity: 175.3** (Blast Radius: 1.753 * Doc Risk: 100.0%)
- `crates/nu-explore/src/explore/commands/nu.rs` -> **Severity: 136.029** (Blast Radius: 3.422 * Doc Risk: 39.7514%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
