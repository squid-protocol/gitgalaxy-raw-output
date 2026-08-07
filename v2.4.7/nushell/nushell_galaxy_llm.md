# ARCHITECTURAL_BRIEF: nushell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/nushell` |
| **Timestamp** | `2026-08-07T04:05:21.668002+00:00` |
| **Scan Duration** | `5.67s` |
| **Git Branch** | `main` |
| **Git Commit** | `8a5a9ae1f8707658d96ddb695f7703e838b33ded` |
| **Git Remote** | `https://github.com/nushell/nushell.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1621 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.699`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1141 | 66.2% |
| file_cluster_13 | 257 | 14.9% |
| file_cluster_0 | 118 | 6.8% |
| file_cluster_16 | 88 | 5.1% |
| file_cluster_17 | 31 | 1.8% |
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
| Cognitive Load Exposure | 0.0 | 92.8 | 10.0 | 7.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.5 | 20.5 | 19.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.0 | 34.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.4 | 2.4 | 0.0 |
| API Exposure | 0.0 | 12.5 | 2.6 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.0 | 12.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.7 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 23.1 | 21.6 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.8 | 18.3 | 0.0 |
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

- `from_nu_config` (@ `crates/nu-command/src/platform/input/list.rs`) -> Impact: **603.5** | LOC: 1293
- `upsert_data_at_cell_path` (@ `crates/nu-protocol/src/value/mod.rs`) -> Impact: **477.2** | LOC: 1226
- `to_debug_string` (@ `crates/nu-protocol/src/value/mod.rs`) -> Impact: **398.3** | LOC: 1246
- `parse_export_in_module` (@ `crates/nu-parser/src/parse_keywords.rs`) -> Impact: **393.4** | LOC: 1156
- `eval_instruction` (@ `crates/nu-engine/src/eval_ir.rs`) -> Impact: **337.4** | LOC: 1034
- `parse_module_block` (@ `crates/nu-parser/src/parse_keywords.rs`) -> Impact: **317.8** | LOC: 1035
- `spawn_engine_call_handler` (@ `crates/nu-plugin-engine/src/interface/mod.rs`) -> Impact: **283.2** | LOC: 824
- `series_to_values` (@ `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs`) -> Impact: **273.4** | LOC: 520
- `compile_if` (@ `crates/nu-engine/src/compile/keyword.rs`) -> Impact: **271.8** | LOC: 402
  * *Intent:* /// Compile a call to `if` as a branch-if
- `run` (@ `crates/nu-command/src/filesystem/save.rs`) -> Impact: **267.4** | LOC: 479

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/nu-command/src/filters` | 53 | 5403.06 | 14.54% | 50.53% |
| `crates/nu-command/tests/commands` | 121 | 5277.18 | 3.08% | 0.0% |
| `crates/nu-protocol/src/value` | 10 | 4260.9 | 7.55% | 76.73% |
| `crates/nu-parser/src` | 12 | 4005.06 | 15.47% | 31.7% |
| `crates/nu-protocol/src/ast` | 17 | 3373.66 | 7.46% | 36.06% |
| `crates/nu-protocol/src/engine` | 20 | 2904.6 | 13.06% | 64.44% |
| `crates/nu-engine/src` | 13 | 2683.54 | 14.88% | 37.37% |
| `crates/nu_plugin_polars/src/dataframe/command/data` | 46 | 2475.12 | 8.2% | 38.32% |
| `crates/nu-command/src/filesystem` | 16 | 2229.94 | 14.3% | 45.46% |
| `tests/repl` | 28 | 2206.32 | 3.97% | 0.0% |

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
- `crates/nu-parser/tests/test_parser.rs` -> **67** Orphaned Functions | **68** Duplicates
- `tests/integration/cli.rs` -> **106** Orphaned Functions | **0** Duplicates
- `tests/overlays/mod.rs` -> **93** Orphaned Functions | **0** Duplicates
- `crates/nu-json/src/ser.rs` -> **8** Orphaned Functions | **75** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tests/repl/test_cell_path.rs`** -> AI Confidence: **99.32%**
2. **`crates/nu-cli/src/commands/keybindings_listen.rs`** -> AI Confidence: **99.31%**
3. **`crates/nu-cli/src/menus/menu_completions.rs`** -> AI Confidence: **99.31%**
4. **`crates/nu-cli/src/syntax_highlight.rs`** -> AI Confidence: **99.31%**
5. **`crates/nu-cmd-base/src/util.rs`** -> AI Confidence: **99.31%**
6. **`crates/nu-cmd-lang/src/core_commands/if_.rs`** -> AI Confidence: **99.31%**
7. **`crates/nu-cmd-plugin/src/util.rs`** -> AI Confidence: **99.31%**
8. **`crates/nu-command/src/date/parser.rs`** -> AI Confidence: **99.31%**
9. **`crates/nu-command/src/filesystem/glob.rs`** -> AI Confidence: **99.31%**
10. **`crates/nu-command/src/filesystem/rm.rs`** -> AI Confidence: **99.31%**
11. **`crates/nu-command/src/filesystem/save.rs`** -> AI Confidence: **99.31%**
12. **`crates/nu-command/src/filesystem/ucp.rs`** -> AI Confidence: **99.31%**
13. **`crates/nu-command/src/filesystem/util.rs`** -> AI Confidence: **99.31%**
14. **`crates/nu-command/src/filesystem/utouch.rs`** -> AI Confidence: **99.31%**
15. **`crates/nu-command/src/filesystem/watch.rs`** -> AI Confidence: **99.31%**
16. **`crates/nu-command/src/filters/default.rs`** -> AI Confidence: **99.31%**
17. **`crates/nu-command/src/filters/find.rs`** -> AI Confidence: **99.31%**
18. **`crates/nu-command/src/filters/interleave.rs`** -> AI Confidence: **99.31%**
19. **`crates/nu-command/src/formats/from/json.rs`** -> AI Confidence: **99.31%**
20. **`crates/nu-command/src/formats/to/msgpack.rs`** -> AI Confidence: **99.31%**
21. **`crates/nu-command/src/generators/seq_date.rs`** -> AI Confidence: **99.31%**
22. **`crates/nu-command/src/help/help_operators.rs`** -> AI Confidence: **99.31%**
23. **`crates/nu-command/src/network/http/get.rs`** -> AI Confidence: **99.31%**
24. **`crates/nu-command/src/network/http/head.rs`** -> AI Confidence: **99.31%**
25. **`crates/nu-command/src/network/http/options.rs`** -> AI Confidence: **99.31%**
26. **`crates/nu-command/src/network/http/post.rs`** -> AI Confidence: **99.31%**
27. **`crates/nu-command/src/network/url/query.rs`** -> AI Confidence: **99.31%**
28. **`crates/nu-command/src/platform/clear.rs`** -> AI Confidence: **99.31%**
29. **`crates/nu-command/src/platform/input/legacy_input.rs`** -> AI Confidence: **99.31%**
30. **`crates/nu-command/src/platform/input/list.rs`** -> AI Confidence: **99.31%**
31. **`crates/nu-command/src/strings/char_.rs`** -> AI Confidence: **99.31%**
32. **`crates/nu-command/src/strings/detect_columns.rs`** -> AI Confidence: **99.31%**
33. **`crates/nu-command/src/strings/detect_type.rs`** -> AI Confidence: **99.31%**
34. **`crates/nu-command/src/strings/format/date.rs`** -> AI Confidence: **99.31%**
35. **`crates/nu-command/src/strings/str_/replace.rs`** -> AI Confidence: **99.31%**
36. **`crates/nu-command/src/system/run_external.rs`** -> AI Confidence: **99.31%**
37. **`crates/nu-command/tests/format_conversions/msgpack.rs`** -> AI Confidence: **99.31%**
38. **`crates/nu-engine/src/compile/call.rs`** -> AI Confidence: **99.31%**
39. **`crates/nu-engine/src/compile/expression.rs`** -> AI Confidence: **99.31%**
40. **`crates/nu-engine/src/compile/keyword.rs`** -> AI Confidence: **99.31%**
41. **`crates/nu-engine/src/compile/mod.rs`** -> AI Confidence: **99.31%**
42. **`crates/nu-engine/src/compile/operator.rs`** -> AI Confidence: **99.31%**
43. **`crates/nu-engine/src/compile/redirect.rs`** -> AI Confidence: **99.31%**
44. **`crates/nu-engine/src/env.rs`** -> AI Confidence: **99.31%**
45. **`crates/nu-engine/src/eval.rs`** -> AI Confidence: **99.31%**
46. **`crates/nu-engine/src/eval_ir.rs`** -> AI Confidence: **99.31%**
47. **`crates/nu-experimental/src/parse.rs`** -> AI Confidence: **99.31%**
48. **`crates/nu-explore/src/explore_config/input.rs`** -> AI Confidence: **99.31%**
49. **`crates/nu-parser/src/flatten.rs`** -> AI Confidence: **99.31%**
50. **`crates/nu-parser/src/parser.rs`** -> AI Confidence: **99.31%**
51. **`crates/nu-parser/src/type_check.rs`** -> AI Confidence: **99.31%**
52. **`crates/nu-path/src/helpers.rs`** -> AI Confidence: **99.31%**
53. **`crates/nu-plugin-core/src/interface/stream/mod.rs`** -> AI Confidence: **99.31%**
54. **`crates/nu-plugin-engine/src/interface/mod.rs`** -> AI Confidence: **99.31%**
55. **`crates/nu-plugin/src/plugin/interface/mod.rs`** -> AI Confidence: **99.31%**
56. **`crates/nu-protocol/src/ast/cell_path.rs`** -> AI Confidence: **99.31%**
57. **`crates/nu-protocol/src/ast/expression.rs`** -> AI Confidence: **99.31%**
58. **`crates/nu-protocol/src/engine/call.rs`** -> AI Confidence: **99.31%**
59. **`crates/nu-protocol/src/engine/pattern_match.rs`** -> AI Confidence: **99.31%**
60. **`crates/nu-protocol/src/eval_base.rs`** -> AI Confidence: **99.31%**
61. **`crates/nu-protocol/src/value/mod.rs`** -> AI Confidence: **99.31%**
62. **`crates/nu-protocol/src/value/range.rs`** -> AI Confidence: **99.31%**
63. **`crates/nu-utils/src/utils.rs`** -> AI Confidence: **99.31%**
64. **`crates/nu_plugin_custom_values/src/cool_custom_value.rs`** -> AI Confidence: **99.31%**
65. **`crates/nu_plugin_example/src/commands/call_decl.rs`** -> AI Confidence: **99.31%**
66. **`crates/nu_plugin_example/src/commands/disable_gc.rs`** -> AI Confidence: **99.31%**
67. **`crates/nu_plugin_example/src/commands/env.rs`** -> AI Confidence: **99.31%**
68. **`crates/nu_plugin_example/src/commands/for_each.rs`** -> AI Confidence: **99.31%**
69. **`crates/nu_plugin_formats/src/from/ini.rs`** -> AI Confidence: **99.31%**
70. **`crates/nu_plugin_gstat/src/gstat.rs`** -> AI Confidence: **99.31%**
71. **`crates/nu_plugin_polars/src/dataframe/command/computation/math.rs`** -> AI Confidence: **99.31%**
72. **`crates/nu_plugin_polars/src/dataframe/command/core/to_df.rs`** -> AI Confidence: **99.31%**
73. **`crates/nu_plugin_polars/src/dataframe/command/core/to_nu.rs`** -> AI Confidence: **99.31%**
74. **`crates/nu_plugin_polars/src/dataframe/command/data/pivot.rs`** -> AI Confidence: **99.31%**
75. **`crates/nu_plugin_polars/src/dataframe/command/data/sql_expr.rs`** -> AI Confidence: **99.31%**
76. **`crates/nu_plugin_polars/src/dataframe/command/index/arg_sort.rs`** -> AI Confidence: **99.31%**
77. **`crates/nu_plugin_polars/src/dataframe/command/string/str_replace.rs`** -> AI Confidence: **99.31%**
78. **`crates/nu_plugin_polars/src/dataframe/command/string/str_replace_all.rs`** -> AI Confidence: **99.31%**
79. **`crates/nu_plugin_polars/src/dataframe/values/nu_expression/mod.rs`** -> AI Confidence: **99.31%**
80. **`crates/nu_plugin_stress_internals/src/main.rs`** -> AI Confidence: **99.31%**
81. **`crates/nuon/src/from.rs`** -> AI Confidence: **99.31%**
82. **`crates/nuon/src/to.rs`** -> AI Confidence: **99.31%**
83. **`crates/nu-system/src/os_info.rs`** -> AI Confidence: **99.29%**
84. **`crates/nu-utils/src/emoji.rs`** -> AI Confidence: **99.29%**
85. **`tests/repl/test_conditionals.rs`** -> AI Confidence: **99.29%**
86. **`crates/nu_plugin_javascript/nu_plugin_node_example.js`** -> AI Confidence: **99.29%**
87. **`docker/Dockerfile`** -> AI Confidence: **99.29%**
88. **`docker/debian.Dockerfile`** -> AI Confidence: **99.29%**
89. **`scripts/uninstall-all.sh`** -> AI Confidence: **99.29%**
90. **`tests/fixtures/formats/script.nu`** -> AI Confidence: **99.29%**
91. **`scripts/install-all.ps1`** -> AI Confidence: **99.29%**
92. **`crates/nu-lsp/src/ast.rs`** -> AI Confidence: **99.25%**
93. **`src/terminal.rs`** -> AI Confidence: **99.25%**
94. **`crates/nu-cli/src/completions/cell_path_completions.rs`** -> AI Confidence: **99.24%**
95. **`crates/nu-cli/src/eval_file.rs`** -> AI Confidence: **99.24%**
96. **`crates/nu-cmd-extra/src/extra/bits/mod.rs`** -> AI Confidence: **99.24%**
97. **`crates/nu-cmd-extra/src/extra/strings/format/bits.rs`** -> AI Confidence: **99.24%**
98. **`crates/nu-cmd-extra/src/extra/strings/format/command.rs`** -> AI Confidence: **99.24%**
99. **`crates/nu-cmd-lang/src/core_commands/do_.rs`** -> AI Confidence: **99.24%**
100. **`crates/nu-cmd-plugin/src/commands/plugin/add.rs`** -> AI Confidence: **99.24%**
101. **`crates/nu-command/src/conversions/into/duration.rs`** -> AI Confidence: **99.24%**
102. **`crates/nu-command/src/conversions/into/int.rs`** -> AI Confidence: **99.24%**
103. **`crates/nu-command/src/conversions/into/string.rs`** -> AI Confidence: **99.24%**
104. **`crates/nu-command/src/database/commands/into_sqlite.rs`** -> AI Confidence: **99.24%**
105. **`crates/nu-command/src/database/values/sqlite.rs`** -> AI Confidence: **99.24%**
106. **`crates/nu-command/src/filesystem/du.rs`** -> AI Confidence: **99.24%**
107. **`crates/nu-command/src/filesystem/open.rs`** -> AI Confidence: **99.24%**
108. **`crates/nu-command/src/filesystem/umv.rs`** -> AI Confidence: **99.24%**
109. **`crates/nu-command/src/filters/group_by.rs`** -> AI Confidence: **99.24%**
110. **`crates/nu-command/src/filters/select.rs`** -> AI Confidence: **99.24%**
111. **`crates/nu-command/src/filters/utils.rs`** -> AI Confidence: **99.24%**
112. **`crates/nu-command/src/formats/to/json.rs`** -> AI Confidence: **99.24%**
113. **`crates/nu-command/src/formats/to/md.rs`** -> AI Confidence: **99.24%**
114. **`crates/nu-command/src/math/utils.rs`** -> AI Confidence: **99.24%**
115. **`crates/nu-command/src/misc/source.rs`** -> AI Confidence: **99.24%**
116. **`crates/nu-command/src/path/exists.rs`** -> AI Confidence: **99.24%**
117. **`crates/nu-command/src/path/self_.rs`** -> AI Confidence: **99.24%**
118. **`crates/nu-command/src/platform/input/input_listen.rs`** -> AI Confidence: **99.24%**
119. **`crates/nu-command/src/strings/ansi/ansi_.rs`** -> AI Confidence: **99.24%**
120. **`crates/nu-command/src/strings/mod.rs`** -> AI Confidence: **99.24%**
121. **`crates/nu-command/src/strings/parse.rs`** -> AI Confidence: **99.24%**
122. **`crates/nu-command/src/strings/str_/length.rs`** -> AI Confidence: **99.24%**
123. **`crates/nu-command/src/viewers/griddle.rs`** -> AI Confidence: **99.24%**
124. **`crates/nu-command/src/viewers/table.rs`** -> AI Confidence: **99.24%**
125. **`crates/nu-derive-value/src/attributes.rs`** -> AI Confidence: **99.24%**
126. **`crates/nu-engine/src/call_ext.rs`** -> AI Confidence: **99.24%**
127. **`crates/nu-engine/src/compile/builder.rs`** -> AI Confidence: **99.24%**
128. **`crates/nu-engine/src/eval_helpers.rs`** -> AI Confidence: **99.24%**
129. **`crates/nu-explore/src/explore/nu_common/value.rs`** -> AI Confidence: **99.24%**
130. **`crates/nu-explore/src/explore_config/app.rs`** -> AI Confidence: **99.24%**
131. **`crates/nu-explore/src/explore_config/tui.rs`** -> AI Confidence: **99.24%**
132. **`crates/nu-explore/src/explore_regex/ui.rs`** -> AI Confidence: **99.24%**
133. **`crates/nu-json/src/de.rs`** -> AI Confidence: **99.24%**
134. **`crates/nu-parser/src/parse_keywords.rs`** -> AI Confidence: **99.24%**
135. **`crates/nu-parser/src/parse_patterns.rs`** -> AI Confidence: **99.24%**
136. **`crates/nu-parser/src/parse_shape_specs.rs`** -> AI Confidence: **99.24%**
137. **`crates/nu-plugin-core/src/communication_mode/mod.rs`** -> AI Confidence: **99.24%**
138. **`crates/nu-plugin/src/plugin/command.rs`** -> AI Confidence: **99.24%**
139. **`crates/nu-protocol/src/ast/block.rs`** -> AI Confidence: **99.24%**
140. **`crates/nu-protocol/src/ast/unit.rs`** -> AI Confidence: **99.24%**
141. **`crates/nu-protocol/src/engine/stack.rs`** -> AI Confidence: **99.24%**
142. **`crates/nu-protocol/src/errors/parse_error.rs`** -> AI Confidence: **99.24%**
143. **`crates/nu-protocol/src/errors/shell_error/mod.rs`** -> AI Confidence: **99.24%**
144. **`crates/nu-protocol/src/ir/display.rs`** -> AI Confidence: **99.24%**
145. **`crates/nu-protocol/src/pipeline/pipeline_data.rs`** -> AI Confidence: **99.24%**
146. **`crates/nu-protocol/src/process/child.rs`** -> AI Confidence: **99.24%**
147. **`crates/nu-protocol/src/signature.rs`** -> AI Confidence: **99.24%**
148. **`crates/nu-protocol/src/span.rs`** -> AI Confidence: **99.24%**
149. **`crates/nu-protocol/src/value/filesize.rs`** -> AI Confidence: **99.24%**
150. **`crates/nu-protocol/src/value/from_value.rs`** -> AI Confidence: **99.24%**
151. **`crates/nu-table/src/types/general.rs`** -> AI Confidence: **99.24%**
152. **`crates/nu-test-support-macros/src/test.rs`** -> AI Confidence: **99.24%**
153. **`crates/nu-test-support/src/harness/group.rs`** -> AI Confidence: **99.24%**
154. **`crates/nu-utils/src/strings/unique.rs`** -> AI Confidence: **99.24%**
155. **`crates/nu_plugin_custom_values/src/generate2.rs`** -> AI Confidence: **99.24%**
156. **`crates/nu_plugin_custom_values/src/handle_get.rs`** -> AI Confidence: **99.24%**
157. **`crates/nu_plugin_custom_values/src/handle_update.rs`** -> AI Confidence: **99.24%**
158. **`crates/nu_plugin_example/src/commands/arg_completion.rs`** -> AI Confidence: **99.24%**
159. **`crates/nu_plugin_example/src/commands/one.rs`** -> AI Confidence: **99.24%**
160. **`crates/nu_plugin_example/src/commands/sum.rs`** -> AI Confidence: **99.24%**
161. **`crates/nu_plugin_formats/src/from/eml.rs`** -> AI Confidence: **99.24%**
162. **`crates/nu_plugin_inc/src/nu/mod.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15919` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/nu-test-support/src/playground/play.rs` (RUST) -> Cumulative Risk: **649.46**
- **Archetype:** `file_cluster_0` (Distance: 11.168 IQR)
- **Magnitude:** 132.38 | **LOC:** 245 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9939%), State Flux (98.6594%)
- **Heaviest Functions:** `symlink` (Impact: 11.3), `with_files` (Impact: 7.2), `glob_vec` (Impact: 6.7)

### 2. `crates/nu-explore/src/explore/commands/try.rs` (RUST) -> Cumulative Risk: **563.36**
- **Archetype:** `file_cluster_13` (Distance: 12.092 IQR)
- **Magnitude:** 30.7 | **LOC:** 56 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8323%), Concurrency (99.2287%), State Flux (88.5385%)
- **Heaviest Functions:** `spawn` (Impact: 6.0), `new` (Impact: 2.0), `parse` (Impact: 2.0)

### 3. `crates/nu-explore/src/explore/views/cursor/window_cursor.rs` (RUST) -> Cumulative Risk: **554.04**
- **Archetype:** `file_cluster_13` (Distance: 12.836 IQR)
- **Magnitude:** 97.26 | **LOC:** 147 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9932%), Documentation (87.3455%)
- **Heaviest Functions:** `next` (Impact: 8.6), `prev` (Impact: 6.3), `set_window_size` (Impact: 5.6)

### 4. `crates/nu-explore/src/explore/commands/mod.rs` (RUST) -> Cumulative Risk: **522.82**
- **Archetype:** `file_cluster_13` (Distance: 12.712 IQR)
- **Magnitude:** 25.38 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.3012%), Documentation (95.2574%), State Flux (89.5243%)
- **Heaviest Functions:** `react` (Impact: 3.5)

### 5. `crates/nu-explore/src/explore/views/cursor/window_cursor_2d.rs` (RUST) -> Cumulative Risk: **518.76**
- **Archetype:** `file_cluster_8` (Distance: 12.606 IQR)
- **Magnitude:** 157.04 | **LOC:** 306 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6707%), Verification (80.0%)
- **Heaviest Functions:** `handle_input_key` (Impact: 8.6), `set_window_size` (Impact: 6.2), `new` (Impact: 5.5)

### 6. `crates/nu-explore/src/explore/commands/expand.rs` (RUST) -> Cumulative Risk: **513.79**
- **Archetype:** `file_cluster_13` (Distance: 12.261 IQR)
- **Magnitude:** 56.1 | **LOC:** 77 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.4762%), Concurrency (96.5555%), State Flux (78.4538%)
- **Heaviest Functions:** `convert_value_to_string` (Impact: 18.9), `spawn` (Impact: 11.3), `new` (Impact: 1.9)

### 7. `src/test_bins.rs` (RUST) -> Cumulative Risk: **513.27**
- **Archetype:** `file_cluster_17` (Distance: 13.096 IQR)
- **Magnitude:** 263.0 | **LOC:** 552 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (95.7135%), Churn (69.9%)
- **Heaviest Functions:** `nu_repl` (Impact: 24.3), `did_chop_arguments` (Impact: 9.8), `run` (Impact: 7.5)

### 8. `crates/nu-plugin-core/src/interface/stream/tests.rs` (RUST) -> Cumulative Risk: **511.49**
- **Archetype:** `file_cluster_4` (Distance: 13.241 IQR)
- **Magnitude:** 129.22 | **LOC:** 554 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9909%), Cognitive Load (92.8074%)
- **Heaviest Functions:** `wait_for_condition` (Impact: 9.9), `reader_recv_end_of_stream` (Impact: 7.7), `stream_manager_drop_writers_on_drop` (Impact: 7.6)

### 9. `crates/nu-command/src/experimental/job_spawn.rs` (RUST) -> Cumulative Risk: **503.54**
- **Archetype:** `file_cluster_4` (Distance: 12.143 IQR)
- **Magnitude:** 71.2 | **LOC:** 149 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (93.0862%), Tech Debt (76.6765%), Cognitive Load (73.8219%)
- **Heaviest Functions:** `run` (Impact: 22.6), `signature` (Impact: 4.3), `examples` (Impact: 2.1)

### 10. `crates/nu-protocol/src/engine/error_handler.rs` (RUST) -> Cumulative Risk: **500.72**
- **Archetype:** `file_cluster_0` (Distance: 14.315 IQR)
- **Magnitude:** 33.66 | **LOC:** 56 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.937%), State Flux (98.8366%), Documentation (87.1445%)
- **Heaviest Functions:** `leave_frame` (Impact: 5.7), `pop` (Impact: 5.5), `new` (Impact: 1.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/nu-protocol/src/value/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.706 IQR)
- **Top Global Matches:** file_cluster_8: 13.706, file_cluster_7: 13.98, file_cluster_16: 13.987
- **Magnitude:** 2688.26 | **LOC:** 4827 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.5159%), Tech Debt (67.3411%)
**Top Internal Functions/Classes:**
  * `upsert_data_at_cell_path` (Impact: 477.2)
  * `to_debug_string` (Impact: 398.3)
  * `modulo` (Impact: 120.0)
  * `floor_div` (Impact: 111.0)
  * `insert_data_at_cell_path` (Impact: 82.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 401`, `args: 265`, `func_start: 161`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 45`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 11`, `orphaned_logic: 60`
* *Architecture:* `api: 133`, `import: 37`
* *Defense:* `safety: 1104`, `doc: 323`, `test: 83`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Display, duration::*, TryIntoValue, record::Record, range::FloatRange, ControlFlow, did_you_mean, locale::LOCALE_OVERRIDE_ENV_VAR...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/ast/traverse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.52 IQR)
- **Top Global Matches:** file_cluster_16: 11.52, file_cluster_8: 11.753, file_cluster_17: 11.966
- **Magnitude:** 2265.36 | **LOC:** 302 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2391%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 40`, `args: 35`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 26`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PipelineRedirection, ListItem, super::
    Block, MatchPattern, Expression, Expr, Pattern, crate::engine::StateWorkingSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/tests/test_parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.257 IQR)
- **Top Global Matches:** file_cluster_0: 12.257, file_cluster_8: 12.669, file_cluster_11: 12.878
- **Magnitude:** 1386.96 | **LOC:** 3252 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.874%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare_rhs_binary_op` (Impact: 242.5)
  * `parse_attribute_block_check_spans` (Impact: 201.7)
  * `parse_cell_path_optional` (Impact: 19.6)
  * `parse_cell_path` (Impact: 17.8)
  * `test_int` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 670`, `args: 176`, `func_start: 148`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 8`, `state_mutation: 230`, `dead_code: 4`, `planned_debt: 14`, `duplicate_logic: 68`, `orphaned_logic: 67`
* *Architecture:* `api: 61`, `import: 18`
* *Defense:* `safety: 268`, `doc: 4`, `test: 348`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nu_protocol::Span, ExternalArgument, Mut, ParseError, PipelineData, nu_protocol::
    DeclId, RangeOperator, nu_engine::CallExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/parse_keywords.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.729 IQR)
- **Top Global Matches:** file_cluster_8: 12.729, file_cluster_17: 12.852, file_cluster_0: 12.957
- **Magnitude:** 1366.04 | **LOC:** 4122 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (18.204%), Tech Debt (29.6873%)
**Top Internal Functions/Classes:**
  * `parse_export_in_module` (Impact: 393.4)
  * `parse_module_block` (Impact: 317.8)
  * `parse_use` (Impact: 157.0)
  * `parse_alias` (Impact: 111.2)
  * `parse_module_file` (Impact: 79.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 359`, `args: 56`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 119`, `dead_code: 8`, `planned_debt: 5`, `fragile_debt: 5`, `orphaned_logic: 7`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 208`, `doc: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parser::
        ParsedInternalCall, parse_block, ParseError, parse_string, type_compatible, ImportPatternMember, lite_parser::LiteCommand, ImportPattern...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.857 IQR)
- **Top Global Matches:** file_cluster_8: 12.857, file_cluster_17: 13.166, file_cluster_0: 13.182
- **Magnitude:** 1355.02 | **LOC:** 7520 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (14.5317%), Tech Debt (37.8761%)
**Top Internal Functions/Classes:**
  * `find_longest_decl_with_prefix` (Impact: 70.0)
  * `parse_unit_value` (Impact: 60.4)
  * `parse_string_strict` (Impact: 59.9)
    * *Intent:* // If we're empty, that means an empty record or closure
  * `parse_full_cell_path` (Impact: 55.4)
  * `parse_short_flags` (Impact: 48.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 466`, `args: 103`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 194`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 9`, `orphaned_logic: 15`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 342`, `doc: 30`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` nu_protocol::
    BlockId, log::trace, DidYouMean, nu_engine::DIR_VAR_PARSER_INFO, HashSet, crate::
    Token, TokenContents, parse_shape_name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/platform/input/list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.896 IQR)
- **Top Global Matches:** file_cluster_8: 12.896, file_cluster_17: 13.258, file_cluster_7: 13.287
- **Magnitude:** 1048.14 | **LOC:** 3702 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.3381%), Tech Debt (8.2584%)
**Top Internal Functions/Classes:**
  * `from_nu_config` (Impact: 603.5)
  * `table_mode_to_separator` (Impact: 5.0)
    * *Intent:* /// Maps TableMode to the appropriate vertical separator character
  * `table_mode_to_header_separator` (Impact: 5.0)
    * *Intent:* /// Maps TableMode to (horizontal_line_char, intersection_char) for header separator
  * `default` (Impact: 2.7)
  * `test_examples` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 571`, `args: 147`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 365`, `orphaned_logic: 3`
* *Architecture:* `import: 15`
* *Defense:* `safety: 230`, `doc: 98`, `test: 18`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` style::Print, nu_engine::ClosureEval, MoveUp, std::
    collections::HashSet, KeyCode, skim::SkimMatcherV2, MoveDown, Stderr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/eval_ir.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.294 IQR)
- **Top Global Matches:** file_cluster_8: 13.294, file_cluster_0: 13.464, file_cluster_17: 13.509
- **Magnitude:** 914.68 | **LOC:** 1838 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (18.0677%), Tech Debt (19.0709%)
**Top Internal Functions/Classes:**
  * `eval_instruction` (Impact: 337.4)
  * `find_named_var_id` (Impact: 169.8)
  * `binary_op` (Impact: 63.5)
  * `literal_value` (Impact: 29.4)
  * `eval_ir_block_impl` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 250`, `args: 45`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 113`, `planned_debt: 2`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 1`, `import: 9`
* *Defense:* `safety: 240`, `doc: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nu_path::expand_path, std::borrow::Cow, Literal, ENV_VARIABLE_ID, nu_protocol::
    DeclId, OutDest, PipelineData, shell_error::generic::GenericError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/state_working_set.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.488 IQR)
- **Top Global Matches:** file_cluster_0: 13.488, file_cluster_17: 13.556, file_cluster_8: 13.581
- **Magnitude:** 840.06 | **LOC:** 1241 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.5397%), Tech Debt (99.4397%)
**Top Internal Functions/Classes:**
  * `hide_decl` (Impact: 193.2)
  * `get_span_for_filename` (Impact: 133.0)
  * `add_overlay` (Impact: 15.5)
  * `read_span` (Impact: 15.3)
  * `remove_overlay` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 161`, `args: 87`, `func_start: 69`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 95`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 31`
* *Architecture:* `api: 75`, `import: 5`
* *Defense:* `safety: 99`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CompileError, HashSet, SpanId, description::build_desc, OverlayId, Variable, core::panic, ParseError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore/pager/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.287 IQR)
- **Top Global Matches:** file_cluster_8: 13.287, file_cluster_0: 13.3, file_cluster_16: 13.359
- **Magnitude:** 785.96 | **LOC:** 1135 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9481%), Tech Debt (63.6736%)
**Top Internal Functions/Classes:**
  * `render_ui` (Impact: 253.7)
  * `search_input_key_event` (Impact: 37.7)
  * `handle_general_key_events2` (Impact: 35.2)
  * `cmd_input_key_event` (Impact: 28.2)
  * `render_cmd_bar_cmd` (Impact: 23.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 210`, `args: 41`, `func_start: 32`, `class_start: 11`
* *Risk/State:* `state_mutation: 172`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 143`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EnterAlternateScreen, Severity, crossterm::
    event::KeyCode, Stack, LeaveAlternateScreen, io::self, self::
    command_bar::CommandBar, lscolors::LsColors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/integration/cli.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.918 IQR)
- **Top Global Matches:** file_cluster_8: 11.918, file_cluster_0: 11.947, file_cluster_13: 12.523
- **Magnitude:** 745.62 | **LOC:** 1931 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (8.2248%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `help_lists_all_flags` (Impact: 9.7)
  * `stdin_flag_with_commands_receives_input` (Impact: 9.7)
  * `table_mode_accepts_all_valid_modes` (Impact: 8.9)
  * `log_level_accepts_all_valid_levels` (Impact: 8.1)
  * `error_style_accepts_all_valid_styles` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 408`, `args: 108`, `func_start: 107`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 200`, `orphaned_logic: 106`
* *Architecture:* `io: 9`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 110`, `test: 290`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert_cmd::cargo_bin, std::io::Write, std::process::Command
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-json/src/ser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.261 IQR)
- **Top Global Matches:** file_cluster_0: 14.261, file_cluster_16: 14.332, file_cluster_11: 14.531
- **Magnitude:** 744.48 | **LOC:** 1041 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5841%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `escape_bytes` (Impact: 21.0)
    * *Intent:* /// Serializes and escapes a `&[u8]` into a Hjson string.
  * `open` (Impact: 14.7)
  * `serialize_newtype_variant` (Impact: 14.3)
  * `serialize_tuple_variant` (Impact: 11.9)
  * `serialize_struct_variant` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 251`, `args: 107`, `func_start: 107`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 280`, `duplicate_logic: 75`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 22`, `import: 6`
* *Defense:* `safety: 184`, `doc: 34`, `immutability_locks: 26`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorCode, serde::ser, Result, std::fmt::Display, std::io, super::error::Error, std::num::FpCategory, LowerExp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/database/values/sqlite.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.876 IQR)
- **Top Global Matches:** file_cluster_8: 12.876, file_cluster_0: 12.906, file_cluster_16: 12.963
- **Magnitude:** 728.0 | **LOC:** 1591 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (7.2161%), Tech Debt (99.8372%)
**Top Internal Functions/Classes:**
  * `prepared_statement_to_nu_list` (Impact: 27.3)
  * `split_select_expressions` (Impact: 26.2)
    * *Intent:* /// Parses a SELECT projection list into `(output_name, expression)` entries. /// /// Input is the t...
  * `split_alias` (Impact: 19.1)
    * *Intent:* // Explicit alias wins and represents the user-visible output column name.
  * `nu_value_to_params` (Impact: 17.8)
  * `read_entire_sqlite_db` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 238`, `args: 129`, `func_start: 90`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 2`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 18`, `orphaned_logic: 30`
* *Architecture:* `io: 1`, `api: 55`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 209`, `doc: 60`, `test: 46`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types::ValueRef, db_index::DbIndex, std::
    collections::BTreeMap, Statement, PipelineData, shell_error::generic::GenericError, rusqlite::
    Connection, serde::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/pipeline/byte_stream.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.491 IQR)
- **Top Global Matches:** file_cluster_0: 14.491, file_cluster_16: 14.62, file_cluster_13: 14.675
- **Magnitude:** 664.58 | **LOC:** 1301 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.3833%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `next_string` (Impact: 32.4)
  * `generic_copy` (Impact: 23.3)
  * `copy_with_signals` (Impact: 21.5)
  * `slice` (Impact: 21.4)
  * `fill_buf` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 221`, `args: 89`, `func_start: 71`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 173`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 28`, `orphaned_logic: 22`
* *Architecture:* `io: 3`, `api: 52`, `concurrency: 25`, `import: 10`
* *Defense:* `safety: 207`, `doc: 178`, `test: 17`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufReader, PipelineData, std::
    fmt::Debug, shell_error::bridge::ShellErrorBridge, io::self, serde::Deserialize, process::Stdio, crate::process::ChildPipe...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore_config/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.627 IQR)
- **Top Global Matches:** file_cluster_8: 11.627, file_cluster_13: 11.825, file_cluster_17: 11.985
- **Magnitude:** 596.44 | **LOC:** 880 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8677%), Tech Debt (15.78%)
**Top Internal Functions/Classes:**
  * `draw_path_widget` (Impact: 152.9)
  * `draw_description_widget` (Impact: 50.4)
  * `draw_editor_widget` (Impact: 50.2)
  * `apply_edit` (Impact: 37.6)
  * `draw_type_widget` (Impact: 31.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 161`, `args: 31`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 66`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 10`, `import: 18`
* *Defense:* `safety: 68`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rect, ratatui::layout::Constraint, Layout, std::io::self, calculate_cursor_position, ValueType, Borders, filter_tree_items...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/engine_state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.802 IQR)
- **Top Global Matches:** file_cluster_0: 13.802, file_cluster_13: 14.018, file_cluster_16: 14.024
- **Magnitude:** 591.72 | **LOC:** 1444 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.8083%), Tech Debt (99.7806%)
**Top Internal Functions/Classes:**
  * `cwd` (Impact: 28.0)
  * `update_plugin_file` (Impact: 17.8)
  * `merge_env` (Impact: 15.3)
  * `find_decl_name` (Impact: 10.8)
  * `which_module_has_decl` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 223`, `args: 126`, `func_start: 99`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 131`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 48`
* *Architecture:* `io: 6`, `api: 90`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 158`, `doc: 95`, `test: 33`, `sync_locks: 11`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HistoryConfig, ScopeFrame, num::NonZeroUsize, MutexGuard, sync::
        Arc, ast::Block, Path, Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-system/src/windows.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.531 IQR)
- **Top Global Matches:** file_cluster_13: 13.531, file_cluster_8: 13.624, file_cluster_0: 13.708
- **Magnitude:** 574.4 | **LOC:** 1068 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.2954%), Tech Debt (30.1%)
**Top Internal Functions/Classes:**
  * `collect_proc` (Impact: 47.1)
  * `get_process_params` (Impact: 21.1)
  * `get_groups` (Impact: 14.9)
  * `get_command` (Impact: 13.1)
  * `get_user` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 330`, `args: 53`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 216`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 53`, `concurrency: 1`, `import: 29`
* *Defense:* `safety: 140`, `doc: 8`, `test: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::ptr, windows::Win32::Foundation::
    CloseHandle, SE_PRIVILEGE_ENABLED, nu_utils::time::Instant, PROCESSENTRY32, STATUS_BUFFER_OVERFLOW, HMODULE, LookupPrivilegeValueW...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.068 IQR)
- **Top Global Matches:** file_cluster_8: 13.068, file_cluster_17: 13.202, file_cluster_0: 13.329
- **Magnitude:** 566.6 | **LOC:** 1957 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.3386%), Tech Debt (23.1068%)
**Top Internal Functions/Classes:**
  * `series_to_values` (Impact: 273.4)
  * `test_any_value_to_value` (Impact: 47.0)
  * `input_type_list_to_series` (Impact: 46.1)
  * `any_value_to_value` (Impact: 18.7)
  * `datetime_from_epoch_nanos` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 255`, `args: 103`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`, `dead_code: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 2`, `import: 25`
* *Defense:* `safety: 354`, `test: 53`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UInt64Type, Utc, NaiveDateTime, polars::chunked_array::builder::AnonymousOwnedListBuilder, PlSmallStr, DataFrame, std::ops::Deref, ListPrimitiveChunkedBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/command.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.569 IQR)
- **Top Global Matches:** file_cluster_0: 12.569, file_cluster_8: 12.58, file_cluster_16: 12.69
- **Magnitude:** 557.54 | **LOC:** 1567 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_cli_args` (Impact: 120.3)
    * *Intent:* // Parse CLI args into nushell options and script details.
  * `parse_experimental_options` (Impact: 47.2)
    * *Intent:* // Parse experimental options, allowing bracketed and comma-delimited forms.
  * `prevalidate_short_groups_before_lexopt` (Impact: 30.2)
    * *Intent:* // Validate combined short flags and reject unsupported inline values.
  * `parse_log_filters` (Impact: 28.5)
    * *Intent:* // Parse log filters and ensure they match known log levels. // Supports multiple formats: [error,wa...
  * `parse_validated_option` (Impact: 16.0)
    * *Intent:* // Parse and validate a string value against a list of allowed values. // Returns the normalized (tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 193`, `args: 68`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 121`
* *Architecture:* `api: 50`, `import: 12`
* *Defense:* `safety: 178`, `test: 24`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Span, Spanned, Write, nu_parser::escape_for_script_arg, path::Path, std::ffi::OsString, nu_protocol::
    LabeledError, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-json/src/value.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.59 IQR)
- **Top Global Matches:** file_cluster_16: 13.59, file_cluster_0: 13.614, file_cluster_8: 13.924
- **Magnitude:** 524.58 | **LOC:** 1159 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.7224%), Tech Debt (99.5556%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 23.1)
  * `deserialize_enum` (Impact: 11.9)
  * `parse_index` (Impact: 8.3)
  * `visit_seq` (Impact: 7.7)
  * `serialize_bytes` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 219`, `args: 114`, `func_start: 108`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 79`, `fragile_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `io: 1`, `api: 84`, `import: 12`
* *Defense:* `safety: 267`, `doc: 71`, `test: 8`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::str, ErrorCode, crate::error::Error, super::Value, serde::ser, btree_map, std::fmt, serde::de...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/filesystem/save.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.761 IQR)
- **Top Global Matches:** file_cluster_8: 12.761, file_cluster_17: 12.903, file_cluster_13: 12.933
- **Magnitude:** 505.38 | **LOC:** 584 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (19.4298%), Tech Debt (34.085%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 267.4)
  * `stream_to_file` (Impact: 53.8)
  * `open_file` (Impact: 27.4)
  * `get_files` (Impact: 23.0)
  * `write_or_consume_stderr` (Impact: 20.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 81`, `args: 31`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `planned_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 106`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PipelineMetadata, BufReader, time::Duration, nu_utils::time::Instant, nu_protocol::
    ByteStreamSource, shell_error::generic::GenericError, OutDest, io::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-plugin/src/plugin/interface/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.211 IQR)
- **Top Global Matches:** file_cluster_0: 16.211, file_cluster_11: 16.323, file_cluster_13: 16.332
- **Magnitude:** 496.82 | **LOC:** 1162 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.8433%), Tech Debt (99.7705%)
**Top Internal Functions/Classes:**
  * `get_current_dir` (Impact: 82.1)
  * `consume` (Impact: 26.9)
  * `write_response` (Impact: 19.3)
    * *Intent:* /// Deserialize custom values in call arguments
  * `write_engine_call` (Impact: 17.9)
  * `eval_closure_with_stream` (Impact: 15.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 107`, `args: 69`, `func_start: 48`, `class_start: 5`
* *Risk/State:* `state_mutation: 50`, `dead_code: 14`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 25`
* *Architecture:* `io: 1`, `api: 30`, `concurrency: 22`, `import: 8`
* *Defense:* `safety: 148`, `doc: 320`, `test: 1`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nu_protocol::
    BlockId, PluginCall, PluginCallResponse, std::
    collections::BTreeMap, btree_map, EvaluatedCall, PipelineData, EngineCallResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/repl/test_parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.872 IQR)
- **Top Global Matches:** file_cluster_8: 10.872, file_cluster_0: 10.966, file_cluster_16: 11.556
- **Magnitude:** 489.46 | **LOC:** 1330 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (3.8824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `not_panic_with_recursive_call` (Impact: 19.2)
  * `reserved_variable_name_checking` (Impact: 13.8)
    * *Intent:* #[rstest] #[case::piped_let_assignment("null | let nu: nothing")] #[case::piped_let_assignment("null...
  * `assignment_with_no_var` (Impact: 11.6)
  * `record_quotes_with_equals` (Impact: 10.9)
  * `external_argument_with_subexpressions` (Impact: 7.3)
    * *Intent:* // https://github.com/nushell/nushell/issues/16040
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 116`, `args: 172`, `func_start: 161`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 3`, `duplicate_logic: 9`, `orphaned_logic: 152`
* *Architecture:* `import: 9`
* *Defense:* `safety: 13`, `test: 178`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::HashMap, nu_test_support::nu, super::*, run_test, crate::repl::tests::TestResult, rstest::rstest, run_test_contains, nu_repl_code...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/conversions/into/datetime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.374 IQR)
- **Top Global Matches:** file_cluster_8: 11.374, file_cluster_0: 11.664, file_cluster_13: 11.994
- **Magnitude:** 486.0 | **LOC:** 1188 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.8115%), Tech Debt (78.4202%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 204.6)
  * `merge_record` (Impact: 76.5)
  * `action` (Impact: 36.8)
  * `run` (Impact: 26.0)
  * `interpret_wall_clock_datetime` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 164`, `args: 35`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 6`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `import: 8`
* *Defense:* `safety: 188`, `test: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Utc, operate, super::DatetimeFormat, NaiveDateTime, chrono::
    DateTime, NaiveTime, nu_protocol::Type::Error, nu_cmd_base::input_handler::CmdArgument...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-plugin-engine/src/interface/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.655 IQR)
- **Top Global Matches:** file_cluster_16: 13.655, file_cluster_8: 13.676, file_cluster_13: 13.811
- **Magnitude:** 478.08 | **LOC:** 1482 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (17.4117%), Tech Debt (14.6604%)
**Top Internal Functions/Classes:**
  * `spawn_engine_call_handler` (Impact: 283.2)
  * `get_signals` (Impact: 13.5)
  * `recv_stream_ended` (Impact: 11.2)
  * `recv_stream_started` (Impact: 8.6)
  * `receive_plugin_call_subscriptions` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 151`, `args: 60`, `func_start: 36`, `class_start: 6`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 17`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 193`, `doc: 110`, `test: 1`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PluginCall, PluginCallResponse, std::
    collections::BTreeMap, btree_map, PluginGc, EvaluatedCall, PipelineData, shell_error::generic::GenericError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/formats/to/md.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.987 IQR)
- **Top Global Matches:** file_cluster_8: 10.987, file_cluster_0: 11.424, file_cluster_16: 11.46
- **Magnitude:** 469.44 | **LOC:** 1548 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.197%), Tech Debt (32.924%)
**Top Internal Functions/Classes:**
  * `get_output_string` (Impact: 84.9)
  * `table` (Impact: 61.3)
    * *Intent:* // SAFETY: is_special_markdown_record already validated the header matches one of these
  * `run` (Impact: 36.6)
  * `group_by` (Impact: 23.6)
  * `fragment` (Impact: 19.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 140`, `args: 135`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 56`, `orphaned_logic: 24`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 91`, `doc: 8`, `test: 51`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` indexmap::IndexMap, nu_protocol::Config, nu_engine::command_prelude::*, crate::Get, IntoPipelineData, casing::Casing, record, nu_cmd_base::formats::to::delimited::merge_descriptors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/nu-command/src/network/mod.rs` (RUST) | Magnitude: 20.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, decorators: 7, api: 5, encapsulation: 5
- `crates/nu-command/tests/commands/path/parse.rs` (RUST) | Magnitude: 36.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, test: 20, args: 18, structural_boundaries: 14
- `crates/nu-protocol/src/ast/pipeline.rs` (RUST) | Magnitude: 131.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, state_mutation: 32, structural_boundaries: 29, safety: 29
- `crates/nu-command/tests/commands/random/int.rs` (RUST) | Magnitude: 9.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: test: 7, indent_spaces: 5, safety: 4, args: 3
- `crates/nu-plugin/src/plugin/mod.rs` (RUST) | Magnitude: 156.78 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 532, doc: 156, structural_boundaries: 120, safety: 78

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/nu-command/src/viewers/table.rs` (RUST) | Magnitude: 263.84 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 441, structural_boundaries: 114, safety: 75, branch: 74
- `crates/nu-utils/src/downcast.rs` (RUST) | Magnitude: 15.18 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, indent_spaces: 11, safety: 10, structural_boundaries: 9
- `crates/nu-command/src/network/http/timeout_extractor_reader.rs` (RUST) | Magnitude: 16.46 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, io: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/nu-plugin-test-support/src/spawn_fake_plugin.rs` (RUST) | Magnitude: 58.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 27, concurrency: 27, generics: 20
- `crates/nu-protocol/src/engine/jobs.rs` (RUST) | Magnitude: 229.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 69, safety: 66, state_mutation: 52
- `crates/nu-cli/tests/completions/support/completions_helpers.rs` (RUST) | Magnitude: 107.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 208, structural_boundaries: 55, args: 23, safety: 21
- `crates/nu_plugin_polars/src/dataframe/values/nu_selector/custom_value.rs` (RUST) | Magnitude: 33.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 15, args: 10, func_start: 10
- `crates/nu-protocol/src/module.rs` (RUST) | Magnitude: 69.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 86, api: 33, encapsulation: 26, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/nu-protocol/src/pipeline/metadata.rs` (RUST) | Magnitude: 34.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, doc: 21, api: 14, encapsulation: 10
- `crates/nu-protocol/src/ast/range.rs` (RUST) | Magnitude: 19.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 5, encapsulation: 5, indent_spaces: 4, structural_boundaries: 3
- `crates/nu-mcp/src/history.rs` (RUST) | Magnitude: 39.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 17, doc: 13, safety: 12
- `crates/nu-experimental/src/options/mod.rs` (RUST) | Magnitude: 6.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 36, indent_spaces: 20, structural_boundaries: 9, immutability_locks: 6
- `crates/nu-command/src/database/values/definitions/db_table.rs` (RUST) | Magnitude: 20.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 6, encapsulation: 6, indent_spaces: 5, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/nu-engine/src/call_ext.rs` (RUST) | Magnitude: 302.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 328, safety: 92, generics: 60, structural_boundaries: 56
- `crates/nu-cmd-plugin/src/util.rs` (RUST) | Magnitude: 94.94 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 25, safety: 24, branch: 23
- `crates/nu-cli/src/completions/completer.rs` (RUST) | Magnitude: 319.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 619, structural_boundaries: 159, state_mutation: 74, branch: 73
- `crates/nu-derive-value/src/from.rs` (RUST) | Magnitude: 113.86 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 357, indent_spaces: 166, structural_boundaries: 45, safety: 35
- `crates/nu-protocol/src/errors/labeled_error.rs` (RUST) | Magnitude: 62.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 115, doc: 101, generics: 46, safety: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/nu-command/src/experimental/job_spawn.rs` (RUST) | Magnitude: 71.2 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 27, safety: 22, concurrency: 16
- `crates/nu-plugin-core/src/serializers/mod.rs` (RUST) | Magnitude: 42.86 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 17, doc: 17, concurrency: 12
- `crates/nu-plugin-core/src/interface/stream/tests.rs` (RUST) | Magnitude: 129.22 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 120, concurrency: 54, safety: 51, structural_boundaries: 43
- `crates/nu-test-support/src/deprecated/commands.rs` (RUST) | Magnitude: 42.18 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 20, structural_boundaries: 17, safety: 7
- `scripts/coverage-local.sh` (SHELL) | Magnitude: 1.23 | Delta: **0.486 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 6, indent_spaces: 6, structural_boundaries: 4, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/nu-plugin-test-support/src/lib.rs` (RUST) | Magnitude: 14.12 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 102, structural_boundaries: 6, api: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/nu-cli/src/completions/env_var_completions.rs` (RUST) | Magnitude: 11.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 11, import: 4, generics: 3
- `crates/nu-protocol/src/plugin/identity.rs` (RUST) | Magnitude: 53.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 113, doc: 21, branch: 16, structural_boundaries: 16
- `crates/nu-command/tests/commands/network/http/post.rs` (RUST) | Magnitude: 81.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 72, test: 33, safety: 31
- `crates/nu-protocol/src/syntax_shape.rs` (RUST) | Magnitude: 38.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 127, doc: 58, branch: 15, structural_boundaries: 13
- `crates/nu-command/tests/commands/network/http/patch.rs` (RUST) | Magnitude: 49.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 46, test: 21, safety: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/nu-utils/src/flatten_json.rs` (RUST) | Magnitude: 126.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 163, doc: 74, branch: 34, structural_boundaries: 28

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/nu-test-support/src/tester/mod.rs` -> Churn: **93.15%** | Cog Load: 4.6704% | Debt: 92.1194%
- `crates/nu-cli/src/repl.rs` -> Churn: **90.31%** | Cog Load: 8.9023% | Debt: 79.4743%
- `crates/nu-protocol/src/pipeline/pipeline_data.rs` -> Churn: **90.31%** | Cog Load: 9.0756% | Debt: 99.4401%
- `crates/nu-protocol/src/errors/shell_error/mod.rs` -> Churn: **84.76%** | Cog Load: 3.8481% | Debt: 98.0069%
- `crates/nu-command/src/network/http/client.rs` -> Churn: **84.51%** | Cog Load: 11.3731% | Debt: 88.8268%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/nu-protocol/src/value/mod.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 2688.26
- `crates/nu-protocol/src/engine/state_working_set.rs` -> **Daniil Sivak** (100.0% isolated ownership) | Magnitude: 840.06
- `crates/nu-protocol/src/pipeline/byte_stream.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 664.58
- `crates/nu-protocol/src/engine/engine_state.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 591.72
- `crates/nu-system/src/windows.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 574.4

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/nu_plugin_polars/src/dataframe/command/data/col.rs` -> **Severity: 271.605** (Blast Radius: 7.714 * Doc Risk: 35.2093%)
- `crates/nu_plugin_polars/src/dataframe/command/data/lit.rs` -> **Severity: 198.964** (Blast Radius: 4.376 * Doc Risk: 45.467%)
- `crates/nu-test-support/src/fs.rs` -> **Severity: 175.3** (Blast Radius: 1.753 * Doc Risk: 100.0%)
- `crates/nu-cli/src/prompt_update.rs` -> **Severity: 103.8** (Blast Radius: 1.038 * Doc Risk: 100.0%)
- `crates/nu-command/src/system/registry.rs` -> **Severity: 103.8** (Blast Radius: 1.038 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
