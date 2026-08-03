# ARCHITECTURAL_BRIEF: ruff
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/ruff` |
| **Timestamp** | `2026-08-03T21:25:05.408536+00:00` |
| **Scan Duration** | `7.32s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1830 malicious artifacts.

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
| Total Artifacts | 3237 |
| Analyzed Artifacts (Scanned) | 1866 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1371 |
| Total LOC | 204117 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.6% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2421 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4271 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0261 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1388 | 200193 | 74.4% |
| PYTHON | 442 | 3908 | 23.7% |
| XML | 23 | 16 | 1.2% |
| MARKDOWN | 11 | 0 | 0.6% |
| PLAINTEXT | 2 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.969`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 866 | 46.4% |
| file_cluster_8 | 656 | 35.2% |
| file_cluster_0 | 138 | 7.4% |
| file_cluster_16 | 133 | 7.1% |
| file_cluster_17 | 23 | 1.2% |
| file_cluster_4 | 21 | 1.1% |
| file_cluster_9 | 5 | 0.3% |
| file_cluster_6 | 4 | 0.2% |
| file_cluster_15 | 4 | 0.2% |
| file_cluster_11 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1371*

**Composition by Extension & Reason:**
- `.snap`: 1138x Excluded (Unsupported Extension: '.snap'), 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 98x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 51x Excluded (Unsupported Extension: '.toml')
- `.rs`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1253 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1596 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.dot`: 1x Excluded (Unsupported Extension: '.dot')
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 469 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.3 | 20.3 | 15.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 39.6 | 21.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 28.9 | 2.6 | 80.0 |
| API Exposure | 0.0 | 14.9 | 2.7 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 27.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 38.8 | 20.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 43.6 | 21.6 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (Hits: 16)
- `ruff-0.15.9/crates/ruff_db/src/system/memory_fs.rs` (Hits: 15)
- `ruff-0.15.9/python/ruff/_find_ruff.py` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **derive_message_formats.rs** (`ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs`) — 672 inbound connections
2. **pylint.rs** (`ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs`) — 12 inbound connections
3. **clause.rs** (`ruff-0.15.9/crates/ruff_python_formatter/src/statement/clause.rs`) — 9 inbound connections
4. **newtype_index.rs** (`ruff-0.15.9/crates/ruff_macros/src/newtype_index.rs`) — 8 inbound connections
5. **visibility.rs** (`ruff-0.15.9/crates/ruff_python_semantic/src/analyze/visibility.rs`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`) — 132 outbound dependencies
2. **configuration.rs** (`ruff-0.15.9/crates/ruff_workspace/src/configuration.rs`) — 123 outbound dependencies
3. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/mod.rs`) — 110 outbound dependencies
4. **format.rs** (`ruff-0.15.9/crates/ruff/src/commands/format.rs`) — 91 outbound dependencies
5. **options.rs** (`ruff-0.15.9/crates/ruff_workspace/src/options.rs`) — 81 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format` (@ `ruff-0.15.9/crates/ruff/src/commands/format.rs`) -> Impact: **2382.1** | LOC: 997
  * *Intent:* /// Format a set of files, and return the exit status.
- `write_suppressed_statements_starting_wit` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/verbatim.rs`) -> Impact: **1942.9** | LOC: 793
- `expression` (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs`) -> Impact: **1680.3** | LOC: 991
  * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
- `statement` (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs`) -> Impact: **1588.1** | LOC: 1087
  * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
- `quote_str` (@ `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs`) -> Impact: **1519.0** | LOC: 1525
- `any_over_expr` (@ `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs`) -> Impact: **1436.0** | LOC: 1076
  * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
- `fmt` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs`) -> Impact: **1176.0** | LOC: 281
  * *Intent:* /// Whether this suite is the last suite in the current statement. /// /// Below, `last_suite_in_statement` is `false` for the suite containing `foo10...
- `resolve_configuration` (@ `ruff-0.15.9/crates/ruff_workspace/src/resolver.rs`) -> Impact: **1010.7** | LOC: 805
  * *Intent:* /// Recursively resolve a [`Configuration`] from a `pyproject.toml` file at the /// specified [`Path`]. // TODO(charlie): This whole system could do w...
- `parse` (@ `ruff-0.15.9/crates/ruff_python_literal/src/format.rs`) -> Impact: **917.1** | LOC: 702
- `handle_own_line_comment_between_statemen` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs`) -> Impact: **823.4** | LOC: 1168

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `persist` (@ `ruff-0.15.9/crates/ruff/src/cache.rs`) -> **O(2^N) [Recursive]**
- `check` (@ `ruff-0.15.9/crates/ruff/src/commands/check.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Run the linter over a collection of files.
- `format` (@ `ruff-0.15.9/crates/ruff/src/commands/format.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Format a set of files, and return the exit status.
- `linter` (@ `ruff-0.15.9/crates/ruff/src/commands/linter.rs`) -> **O(2^N) [Recursive]**
- `fold_body` (@ `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/full.rs`) -> **O(2^N) [Recursive]**
- `system` (@ `ruff-0.15.9/crates/ruff_db/src/files.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Lookup table that maps [file paths](`FilePath`) to salsa interned [`File`] instances. #[derive(Default, Clone)]
- `vendored` (@ `ruff-0.15.9/crates/ruff_db/src/files.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `ruff-0.15.9/crates/ruff_db/src/panic.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `resolve_name_impl` (@ `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs`) -> DB Complexity: **72**
  * *Intent:* // Regular packages and modules are both terminal. A `foo.py` // in a higher-priority search path is not shadowed by // `foo/__init__.py` in a lower-p...
- `parse_simple_statement` (@ `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs`) -> DB Complexity: **64**
  * *Intent:* // test_err simple_and_compound_stmt_on_same_line
- `any_over_expr` (@ `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs`) -> DB Complexity: **46**
  * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
- `quote_str` (@ `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs`) -> DB Complexity: **46**
- `resolve_configuration` (@ `ruff-0.15.9/crates/ruff_workspace/src/resolver.rs`) -> DB Complexity: **44**
  * *Intent:* /// Recursively resolve a [`Configuration`] from a `pyproject.toml` file at the /// specified [`Path`]. // TODO(charlie): This whole system could do w...
- `parse_toml` (@ `ruff-0.15.9/crates/ruff_workspace/src/pyproject.rs`) -> DB Complexity: **40**
- `fmt` (@ `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/full.rs`) -> DB Complexity: **37**
- `format` (@ `ruff-0.15.9/crates/ruff/src/commands/format.rs`) -> DB Complexity: **32**
  * *Intent:* /// Format a set of files, and return the exit status.
- `write_suppressed_statements_starting_wit` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/verbatim.rs`) -> DB Complexity: **26**
- `simplify_ignore_verbatim` (@ `ruff-0.15.9/crates/ruff_db/src/system/os.rs`) -> DB Complexity: **22**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ruff-0.15.9/crates/ruff_python_ast/src` | 25 | 9699.34 | 9.56% | 44.93% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules` | 110 | 8566.68 | 5.93% | 71.66% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules` | 75 | 7211.92 | 6.46% | 52.42% |
| `ruff-0.15.9/crates/ruff_linter/src` | 21 | 6098.78 | 6.88% | 57.15% |
| `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze` | 19 | 5690.64 | 12.86% | 16.84% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules` | 43 | 5337.44 | 8.28% | 64.06% |
| `ruff-0.15.9/crates/ruff_python_formatter/src/expression` | 37 | 5205.82 | 13.57% | 64.42% |
| `ruff-0.15.9/crates/ty_module_resolver/src` | 11 | 4458.54 | 6.11% | 47.67% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/isort` | 13 | 4401.06 | 12.56% | 38.15% |
| `ruff-0.15.9/crates/ruff/src/commands` | 15 | 4251.54 | 13.38% | 24.85% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ruff-0.15.9/crates/ruff_cache/src/cache_key.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_cache/src/globset.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/mod.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_db/src/file_revision.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_db/src/system/path.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ruff-0.15.9/crates/ruff/src/stdin.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/src/node_index.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/generate.py` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ann_assign_stmt_invalid_value.py` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/assign_stmt_invalid_value_expr.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` -> **0** Orphaned Functions | **94** Duplicates
- `ruff-0.15.9/crates/ruff_linter/src/preview.rs` -> **63** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_python_ast/src/name.rs` -> **0** Orphaned Functions | **51** Duplicates
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` -> **19** Orphaned Functions | **27** Duplicates
- `ruff-0.15.9/crates/ruff_python_ast/src/comparable.rs` -> **0** Orphaned Functions | **46** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/bindings.rs`** -> AI Confidence: **99.48%**
2. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/deferred_scopes.rs`** -> AI Confidence: **99.48%**
3. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs`** -> AI Confidence: **99.48%**
4. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs`** -> AI Confidence: **99.48%**
5. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/string_like.rs`** -> AI Confidence: **99.39%**
6. **`ruff-0.15.9/crates/ruff_linter/src/rules/isort/format.rs`** -> AI Confidence: **99.39%**
7. **`ruff-0.15.9/crates/ruff/src/printer.rs`** -> AI Confidence: **99.31%**
8. **`ruff-0.15.9/crates/ruff/tests/analyze_graph.rs`** -> AI Confidence: **99.31%**
9. **`ruff-0.15.9/crates/ruff/tests/cli/lint.rs`** -> AI Confidence: **99.31%**
10. **`ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs`** -> AI Confidence: **99.31%**
11. **`ruff-0.15.9/crates/ruff_formatter/src/format_element/document.rs`** -> AI Confidence: **99.31%**
12. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/deferred_for_loops.rs`** -> AI Confidence: **99.31%**
13. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/definitions.rs`** -> AI Confidence: **99.31%**
14. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/except_handler.rs`** -> AI Confidence: **99.31%**
15. **`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`** -> AI Confidence: **99.31%**
16. **`ruff-0.15.9/crates/ruff_linter/src/checkers/noqa.rs`** -> AI Confidence: **99.31%**
17. **`ruff-0.15.9/crates/ruff_linter/src/checkers/tokens.rs`** -> AI Confidence: **99.31%**
18. **`ruff-0.15.9/crates/ruff_linter/src/cst/helpers.rs`** -> AI Confidence: **99.31%**
19. **`ruff-0.15.9/crates/ruff_linter/src/docstrings/extraction.rs`** -> AI Confidence: **99.31%**
20. **`ruff-0.15.9/crates/ruff_linter/src/rules/airflow/rules/runtime_value_in_dag_or_task.rs`** -> AI Confidence: **99.31%**
21. **`ruff-0.15.9/crates/ruff_linter/src/rules/eradicate/detection.rs`** -> AI Confidence: **99.31%**
22. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_2020/rules/compare.rs`** -> AI Confidence: **99.31%**
23. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bandit/rules/bad_file_permissions.rs`** -> AI Confidence: **99.31%**
24. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bandit/rules/hardcoded_bind_all_interfaces.rs`** -> AI Confidence: **99.31%**
25. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bandit/rules/jinja2_autoescape_false.rs`** -> AI Confidence: **99.31%**
26. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bandit/rules/shell_injection.rs`** -> AI Confidence: **99.31%**
27. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bandit/rules/suspicious_imports.rs`** -> AI Confidence: **99.31%**
28. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_blind_except/rules/blind_except.rs`** -> AI Confidence: **99.31%**
29. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/abstract_base_class.rs`** -> AI Confidence: **99.31%**
30. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/assert_raises_exception.rs`** -> AI Confidence: **99.31%**
31. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/class_as_data_structure.rs`** -> AI Confidence: **99.31%**
32. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/function_uses_loop_variable.rs`** -> AI Confidence: **99.31%**
33. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/jump_statement_in_finally.rs`** -> AI Confidence: **99.31%**
34. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_bugbear/rules/reuse_of_groupby_generator.rs`** -> AI Confidence: **99.31%**
35. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_django/rules/all_with_model_form.rs`** -> AI Confidence: **99.31%**
36. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_django/rules/exclude_with_model_form.rs`** -> AI Confidence: **99.31%**
37. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_django/rules/model_without_dunder_str.rs`** -> AI Confidence: **99.31%**
38. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_executable/rules/shebang_missing_python.rs`** -> AI Confidence: **99.31%**
39. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_logging_format/rules/logging_call.rs`** -> AI Confidence: **99.31%**
40. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pie/rules/unnecessary_dict_kwargs.rs`** -> AI Confidence: **99.31%**
41. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pie/rules/unnecessary_spread.rs`** -> AI Confidence: **99.31%**
42. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/exit_annotations.rs`** -> AI Confidence: **99.31%**
43. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/unused_private_type_definition.rs`** -> AI Confidence: **99.31%**
44. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/raises.rs`** -> AI Confidence: **99.31%**
45. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/unittest_assert.rs`** -> AI Confidence: **99.31%**
46. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/warns.rs`** -> AI Confidence: **99.31%**
47. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/settings.rs`** -> AI Confidence: **99.31%**
48. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_return/rules/function.rs`** -> AI Confidence: **99.31%**
49. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/ast_ifexp.rs`** -> AI Confidence: **99.31%**
50. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/collapsible_if.rs`** -> AI Confidence: **99.31%**
51. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_tidy_imports/rules/lazy_import_mismatch.rs`** -> AI Confidence: **99.31%**
52. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_unused_arguments/rules/unused_arguments.rs`** -> AI Confidence: **99.31%**
53. **`ruff-0.15.9/crates/ruff_linter/src/rules/isort/block.rs`** -> AI Confidence: **99.31%**
54. **`ruff-0.15.9/crates/ruff_linter/src/rules/isort/helpers.rs`** -> AI Confidence: **99.31%**
55. **`ruff-0.15.9/crates/ruff_linter/src/rules/pep8_naming/settings.rs`** -> AI Confidence: **99.31%**
56. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/indentation.rs`** -> AI Confidence: **99.31%**
57. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/missing_whitespace_around_operator.rs`** -> AI Confidence: **99.31%**
58. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/whitespace_around_named_parameter_equals.rs`** -> AI Confidence: **99.31%**
59. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/type_comparison.rs`** -> AI Confidence: **99.31%**
60. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydoclint/rules/check_docstring.rs`** -> AI Confidence: **99.31%**
61. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydocstyle/rules/backslashes.rs`** -> AI Confidence: **99.31%**
62. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydocstyle/rules/not_missing.rs`** -> AI Confidence: **99.31%**
63. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/assert_on_string_literal.rs`** -> AI Confidence: **99.31%**
64. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/comparison_with_itself.rs`** -> AI Confidence: **99.31%**
65. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/continue_in_finally.rs`** -> AI Confidence: **99.31%**
66. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/import_private_name.rs`** -> AI Confidence: **99.31%**
67. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/magic_value_comparison.rs`** -> AI Confidence: **99.31%**
68. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/missing_maxsplit_arg.rs`** -> AI Confidence: **99.31%**
69. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/no_method_decorator.rs`** -> AI Confidence: **99.31%**
70. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/redefined_argument_from_local.rs`** -> AI Confidence: **99.31%**
71. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/single_string_slots.rs`** -> AI Confidence: **99.31%**
72. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/too_many_branches.rs`** -> AI Confidence: **99.31%**
73. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/too_many_nested_blocks.rs`** -> AI Confidence: **99.31%**
74. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/unexpected_special_method_signature.rs`** -> AI Confidence: **99.31%**
75. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/unspecified_encoding.rs`** -> AI Confidence: **99.31%**
76. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/useless_else_on_loop.rs`** -> AI Confidence: **99.31%**
77. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/deprecated_c_element_tree.rs`** -> AI Confidence: **99.31%**
78. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/extraneous_parentheses.rs`** -> AI Confidence: **99.31%**
79. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/pep695/mod.rs`** -> AI Confidence: **99.31%**
80. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/timeout_error_alias.rs`** -> AI Confidence: **99.31%**
81. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/unnecessary_default_type_args.rs`** -> AI Confidence: **99.31%**
82. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/use_pep604_annotation.rs`** -> AI Confidence: **99.31%**
83. **`ruff-0.15.9/crates/ruff_linter/src/rules/refurb/rules/slice_to_remove_prefix_or_suffix.rs`** -> AI Confidence: **99.31%**
84. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/helpers.rs`** -> AI Confidence: **99.31%**
85. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/asyncio_dangling_task.rs`** -> AI Confidence: **99.31%**
86. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/float_equality_comparison.rs`** -> AI Confidence: **99.31%**
87. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/function_call_in_dataclass_default.rs`** -> AI Confidence: **99.31%**
88. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/incorrectly_parenthesized_tuple_in_subscript.rs`** -> AI Confidence: **99.31%**
89. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/logging_eager_conversion.rs`** -> AI Confidence: **99.31%**
90. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/mutable_class_default.rs`** -> AI Confidence: **99.31%**
91. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/unnecessary_regular_expression.rs`** -> AI Confidence: **99.31%**
92. **`ruff-0.15.9/crates/ruff_macros/src/config.rs`** -> AI Confidence: **99.31%**
93. **`ruff-0.15.9/crates/ruff_macros/src/violation_metadata.rs`** -> AI Confidence: **99.31%**
94. **`ruff-0.15.9/crates/ruff_python_ast/src/expression.rs`** -> AI Confidence: **99.31%**
95. **`ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs`** -> AI Confidence: **99.31%**
96. **`ruff-0.15.9/crates/ruff_python_ast/src/token.rs`** -> AI Confidence: **99.31%**
97. **`ruff-0.15.9/crates/ruff_python_ast/src/visitor.rs`** -> AI Confidence: **99.31%**
98. **`ruff-0.15.9/crates/ruff_python_formatter/src/cli.rs`** -> AI Confidence: **99.31%**
99. **`ruff-0.15.9/crates/ruff_python_formatter/src/comments/format.rs`** -> AI Confidence: **99.31%**
100. **`ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs`** -> AI Confidence: **99.31%**
101. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_attribute.rs`** -> AI Confidence: **99.31%**
102. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_bin_op.rs`** -> AI Confidence: **99.31%**
103. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_lambda.rs`** -> AI Confidence: **99.31%**
104. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_named.rs`** -> AI Confidence: **99.31%**
105. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_slice.rs`** -> AI Confidence: **99.31%**
106. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_yield.rs`** -> AI Confidence: **99.31%**
107. **`ruff-0.15.9/crates/ruff_python_formatter/src/main.rs`** -> AI Confidence: **99.31%**
108. **`ruff-0.15.9/crates/ruff_python_formatter/src/other/with_item.rs`** -> AI Confidence: **99.31%**
109. **`ruff-0.15.9/crates/ruff_python_formatter/src/pattern/pattern_match_as.rs`** -> AI Confidence: **99.31%**
110. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_ann_assign.rs`** -> AI Confidence: **99.31%**
111. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_assign.rs`** -> AI Confidence: **99.31%**
112. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_aug_assign.rs`** -> AI Confidence: **99.31%**
113. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_expr.rs`** -> AI Confidence: **99.31%**
114. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs`** -> AI Confidence: **99.31%**
115. **`ruff-0.15.9/crates/ruff_python_formatter/src/string/normalize.rs`** -> AI Confidence: **99.31%**
116. **`ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs`** -> AI Confidence: **99.31%**
117. **`ruff-0.15.9/crates/ruff_python_parser/src/semantic_errors.rs`** -> AI Confidence: **99.31%**
118. **`ruff-0.15.9/crates/ruff_python_parser/tests/generate_inline_tests.rs`** -> AI Confidence: **99.31%**
119. **`ruff-0.15.9/crates/ruff_python_semantic/src/analyze/function_type.rs`** -> AI Confidence: **99.31%**
120. **`ruff-0.15.9/crates/ruff_python_semantic/src/binding.rs`** -> AI Confidence: **99.31%**
121. **`ruff-0.15.9/crates/ruff_python_trivia/src/tokenizer.rs`** -> AI Confidence: **99.31%**
122. **`ruff-0.15.9/crates/ruff_server/src/edit.rs`** -> AI Confidence: **99.31%**
123. **`ruff-0.15.9/crates/ruff_python_ast/generate.py`** -> AI Confidence: **99.31%**
124. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ann_assign_stmt_invalid_value.py`** -> AI Confidence: **99.29%**
125. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/args_unparenthesized_generator.py`** -> AI Confidence: **99.29%**
126. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/backslash_continuation_indentation_error.py`** -> AI Confidence: **99.29%**
127. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/debug_shadow_match.py`** -> AI Confidence: **99.29%**
128. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/different_match_pattern_bindings.py`** -> AI Confidence: **99.29%**
129. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/duplicate_match_class_attr.py`** -> AI Confidence: **99.29%**
130. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/duplicate_match_key.py`** -> AI Confidence: **99.29%**
131. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/except_star_py310.py`** -> AI Confidence: **99.29%**
132. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/f_string_invalid_starred_expr.py`** -> AI Confidence: **99.29%**
133. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_iter_unpack_py38.py`** -> AI Confidence: **99.29%**
134. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_iter_expr.py`** -> AI Confidence: **99.29%**
135. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target.py`** -> AI Confidence: **99.29%**
136. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target_binary_expr.py`** -> AI Confidence: **99.29%**
137. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target_in_keyword.py`** -> AI Confidence: **99.29%**
138. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_1.py`** -> AI Confidence: **99.29%**
139. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_2.py`** -> AI Confidence: **99.29%**
140. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_3.py`** -> AI Confidence: **99.29%**
141. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/irrefutable_case_pattern.py`** -> AI Confidence: **99.29%**
142. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/lambda_body_with_starred_expr.py`** -> AI Confidence: **99.29%**
143. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_expected_colon.py`** -> AI Confidence: **99.29%**
144. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_expected_case_block.py`** -> AI Confidence: **99.29%**
145. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_invalid_guard_expr.py`** -> AI Confidence: **99.29%**
146. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_invalid_subject_expr.py`** -> AI Confidence: **99.29%**
147. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/multiple_assignment_in_case_pattern.py`** -> AI Confidence: **99.29%**
148. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/rebound_comprehension_variable.py`** -> AI Confidence: **99.29%**
149. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/starred_list_comp_py314.py`** -> AI Confidence: **99.29%**
150. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/t_string_invalid_starred_expr.py`** -> AI Confidence: **99.29%**
151. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/tuple_context_manager_py38.py`** -> AI Confidence: **99.29%**
152. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/unparenthesized_named_expr_set_comp_py38.py`** -> AI Confidence: **99.29%**
153. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/while_stmt_invalid_test_expr.py`** -> AI Confidence: **99.29%**
154. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/ambiguous_lpar_with_items_binary_expr.py`** -> AI Confidence: **99.29%**
155. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/ambiguous_lpar_with_items_if_expr.py`** -> AI Confidence: **99.29%**
156. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/args_unparenthesized_generator.py`** -> AI Confidence: **99.29%**
157. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/async_with_statement.py`** -> AI Confidence: **99.29%**
158. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/backslash_continuation_indentation.py`** -> AI Confidence: **99.29%**
159. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/different_match_pattern_bindings.py`** -> AI Confidence: **99.29%**
160. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/duplicate_match_key_attr.py`** -> AI Confidence: **99.29%**
161. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/except_star_py311.py`** -> AI Confidence: **99.29%**
162. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_in_target_valid_expr.py`** -> AI Confidence: **99.29%**
163. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_iter_unpack_py38.py`** -> AI Confidence: **99.29%**
164. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_iter_unpack_py39.py`** -> AI Confidence: **99.29%**
165. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/irrefutable_case_pattern_at_end.py`** -> AI Confidence: **99.29%**
166. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_as_pattern.py`** -> AI Confidence: **99.29%**
167. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_as_pattern_soft_keyword.py`** -> AI Confidence: **99.29%**
168. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_attr_pattern_soft_keyword.py`** -> AI Confidence: **99.29%**
169. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_identifier_1.py`** -> AI Confidence: **99.29%**
170. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_identifier_2.py`** -> AI Confidence: **99.29%**
171. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_1.py`** -> AI Confidence: **99.29%**
172. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_2.py`** -> AI Confidence: **99.29%**
173. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_or_identifier.py`** -> AI Confidence: **99.29%**
174. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_sequence_pattern_parentheses_terminator.py`** -> AI Confidence: **99.29%**
175. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_sequence_pattern_terminator.py`** -> AI Confidence: **99.29%**
176. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_stmt_subject_expr.py`** -> AI Confidence: **99.29%**
177. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_stmt_valid_guard_expr.py`** -> AI Confidence: **99.29%**
178. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/nested_alternative_patterns.py`** -> AI Confidence: **99.29%**
179. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/parenthesized_named_expr_py38.py`** -> AI Confidence: **99.29%**
180. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/parenthesized_star_index_py310.py`** -> AI Confidence: **99.29%**
181. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/starred_list_comp_py315.py`** -> AI Confidence: **99.29%**
182. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/unparenthesized_named_expr_py39.py`** -> AI Confidence: **99.29%**
183. **`ruff-0.15.9/crates/ruff_python_parser/resources/invalid/expressions/bool_op/invalid_rhs_expression.py`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `ruff-0.15.9/crates/ruff_linter/src/rules/eradicate/detection.rs` -> **100.0%** Exposure
### Exploit Generation Surface
- `ruff-0.15.9/crates/ruff_python_ast/generate.py` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/class.py` -> **100.0%** Exposure
- `ruff-0.15.9/python/ruff/__main__.py` -> **99.9682%** Exposure
- `ruff-0.15.9/python/ruff/_find_ruff.py` -> **99.8611%** Exposure
- `ruff-0.15.9/crates/ruff_python_formatter/generate.py` -> **70.7054%** Exposure
### Weaponizable Injection Vectors
- `ruff-0.15.9/crates/ruff_notebook/src/cell.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_server/src/server/api/requests/format.rs` -> **100.0%** Exposure
- `ruff-0.15.9/python/ruff/__main__.py` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_server/src/server/api/diagnostics.rs` -> **99.9996%** Exposure
- `ruff-0.15.9/crates/ruff_notebook/src/schema.rs` -> **99.9992%** Exposure
### Raw Memory Manipulation
- `ruff-0.15.9/crates/ruff_db/src/system/path.rs` -> **0.0028%** Exposure
- `ruff-0.15.9/crates/ruff_text_size/src/range.rs` -> **0.0025%** Exposure
- `ruff-0.15.9/crates/ruff_source_file/src/line_ranges.rs` -> **0.0017%** Exposure
- `ruff-0.15.9/crates/ruff_python_semantic/src/reference.rs` -> **0.0008%** Exposure
- `ruff-0.15.9/crates/ruff_formatter/src/buffer.rs` -> **0.0002%** Exposure
### Algorithmic DoS Exposure
- `ruff-0.15.9/crates/ruff/src/args.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff/src/cache.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff/src/commands/analyze_graph.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff/src/commands/check.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff/src/commands/check_stdin.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `17644` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ruff-0.15.9/crates/ruff_python_ast/src/visitor/source_order.rs` (RUST) -> Cumulative Risk: **773.09**
- **Archetype:** `file_cluster_16` (Distance: 11.955 IQR)
- **Magnitude:** 603.46 | **LOC:** 624 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9608%), Tech Debt (97.5669%)
- **Heaviest Functions:** `walk_interpolated_string_element` (Impact: 23.1), `walk_except_handler` (Impact: 20.7), `walk_expr` (Impact: 18.2)

### 2. `ruff-0.15.9/crates/ruff_db/src/system/walk_directory.rs` (RUST) -> Cumulative Risk: **754.61**
- **Archetype:** `file_cluster_16` (Distance: 12.312 IQR)
- **Magnitude:** 260.1 | **LOC:** 319 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9549%), Documentation (99.5763%)
- **Heaviest Functions:** `fmt` (Impact: 42.6), `fmt` (Impact: 35.1), `write_entry` (Impact: 15.2)

### 3. `ruff-0.15.9/crates/ruff_index/src/slice.rs` (RUST) -> Cumulative Risk: **747.75**
- **Archetype:** `file_cluster_0` (Distance: 11.78 IQR)
- **Magnitude:** 150.36 | **LOC:** 214 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9994%), Algorithmic Dos (99.986%), State Flux (96.3199%)
- **Heaviest Functions:** `binary_search` (Impact: 10.9), `clone_into` (Impact: 6.2), `fmt` (Impact: 5.3)

### 4. `ruff-0.15.9/crates/ruff_python_formatter/src/comments/debug.rs` (RUST) -> Cumulative Risk: **735.12**
- **Archetype:** `file_cluster_16` (Distance: 10.871 IQR)
- **Magnitude:** 266.3 | **LOC:** 247 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8828%), Tech Debt (99.8073%)
- **Heaviest Functions:** `fmt` (Impact: 137.2), `debug` (Impact: 30.3), `fmt` (Impact: 21.9)

### 5. `ruff-0.15.9/crates/ruff_index/src/vec.rs` (RUST) -> Cumulative Risk: **731.34**
- **Archetype:** `file_cluster_16` (Distance: 10.929 IQR)
- **Magnitude:** 124.76 | **LOC:** 197 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.434%), Algorithmic Dos (97.6861%), State Flux (96.6653%)
- **Heaviest Functions:** `with_capacity` (Impact: 6.3), `new` (Impact: 5.5), `from_iter` (Impact: 5.5)

### 6. `ruff-0.15.9/crates/ruff_linter/src/rules/numpy/helpers.rs` (RUST) -> Cumulative Risk: **728.99**
- **Archetype:** `file_cluster_16` (Distance: 10.572 IQR)
- **Magnitude:** 106.68 | **LOC:** 105 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `visit_stmt` (Impact: 22.4), `visit_expr` (Impact: 18.1), `visit_body` (Impact: 13.4)

### 7. `ruff-0.15.9/crates/ruff_python_ast/generate.py` (PYTHON) -> Cumulative Risk: **726.84**
- **Archetype:** `file_cluster_16` (Distance: 13.918 IQR)
- **Magnitude:** 931.72 | **LOC:** 1106 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `write_node` (Impact: 186.4), `__init__` (Impact: 122.9), `write_owned_enum` (Impact: 45.6)

### 8. `ruff-0.15.9/crates/ruff_linter/src/message/grouped.rs` (RUST) -> Cumulative Risk: **724.1**
- **Archetype:** `file_cluster_13` (Distance: 10.974 IQR)
- **Magnitude:** 307.46 | **LOC:** 269 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.5347%), Tech Debt (98.5606%)
- **Heaviest Functions:** `fmt` (Impact: 98.7), `fmt` (Impact: 75.1), `emit` (Impact: 62.3)

### 9. `ruff-0.15.9/crates/ruff_python_literal/src/escape.rs` (RUST) -> Cumulative Risk: **723.11**
- **Archetype:** `file_cluster_0` (Distance: 12.223 IQR)
- **Magnitude:** 480.96 | **LOC:** 418 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7341%)
- **Heaviest Functions:** `output_layout_with_checker` (Impact: 88.2), `write_char` (Impact: 60.8), `output_layout_with_checker` (Impact: 48.8)

### 10. `ruff-0.15.9/crates/ruff_notebook/src/cell.rs` (RUST) -> Cumulative Risk: **717.58**
- **Archetype:** `file_cluster_13` (Distance: 12.622 IQR)
- **Magnitude:** 202.36 | **LOC:** 359 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (99.5097%)
- **Heaviest Functions:** `fmt` (Impact: 42.1), `push` (Impact: 17.8), `containing_range` (Impact: 17.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.507 IQR)
- **Top Global Matches:** file_cluster_16: 13.507, file_cluster_0: 13.557, file_cluster_8: 13.825
- **Magnitude:** 3077.74 | **LOC:** 3855 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (8.1863%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `quote_str` (Impact: 1519.0 | O(2^N) | DB: 46)
  * `irrefutable_pattern` (Impact: 49.9 | O(2^N))
  * `next` (Impact: 41.1 | O(2^N) | DB: 1)
  * `next_back` (Impact: 41.1 | O(2^N) | DB: 1)
  * `next` (Impact: 24.9 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 424`, `args: 255`, `func_start: 256`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 182`, `dead_code: 8`, `planned_debt: 3`, `duplicate_logic: 94`
* *Architecture:* `api: 325`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 236`, `doc: 657`, `test: 48`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bitflags::bitflags, crate::Mod, PatternMatchOr, StmtClassDef, ExprName, Pattern, ExprStringLiteral, crate::generated::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.188 IQR)
- **Top Global Matches:** file_cluster_8: 12.188, file_cluster_16: 12.232, file_cluster_0: 12.333
- **Magnitude:** 2652.44 | **LOC:** 1955 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (12.2331%), Tech Debt (51.7304%)
**Top Internal Functions/Classes:**
  * `fold_body` (Impact: 773.8 | O(2^N) | DB: 17)
  * `format_line` (Impact: 750.2 | O(N^6) | DB: 10)
  * `format_annotation` (Impact: 262.7 | O(N^6) | DB: 1)
  * `fmt` (Impact: 135.4 | O(2^N) | DB: 3)
  * `format_header` (Impact: 123.8 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 227`, `args: 95`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `state_mutation: 106`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 38`, `import: 12`
* *Defense:* `safety: 123`, `doc: 77`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` max, std::cmp, fmt, std::ops::Range, min, std::collections::HashMap, crate::renderer::DEFAULT_TERM_WIDTH, crate::renderer::styled_buffer::StyledBuffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff/src/commands/format.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.059 IQR)
- **Top Global Matches:** file_cluster_13: 12.059, file_cluster_8: 12.209, file_cluster_0: 12.354
- **Magnitude:** 2485.56 | **LOC:** 1426 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (9.7926%), Tech Debt (12.4958%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 2382.1 | O(2^N) | DB: 32)
    * *Intent:* /// Format a set of files, and return the exit status.
  * `from_cli` (Impact: 20.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 184`, `args: 30`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 58`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 5`, `api: 7`, `import: 53`
* *Defense:* `safety: 95`, `doc: 33`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Right, ModifiedRange, ruff_linter::message::EmitterContext, Formatter, std::fmt::Display, ruff_text_size::TextLen, std::io, Fix...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/verbatim.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.09 IQR)
- **Top Global Matches:** file_cluster_16: 12.09, file_cluster_8: 12.112, file_cluster_13: 12.172
- **Magnitude:** 2040.62 | **LOC:** 958 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (7.7477%), Tech Debt (15.8715%)
**Top Internal Functions/Classes:**
  * `write_suppressed_statements_starting_wit` (Impact: 1942.9 | O(2^N) | DB: 26)
  * `write_suppressed_statements_starting_wit` (Impact: 11.8 | O(N^3) | DB: 3)
  * `ends_suppression` (Impact: 2.5 | O(N^1) | DB: 1)
    * *Intent:* /// Returns `true` if the statements coming after `leading_or_trailing_comments` are suppressed. ///...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 142`, `args: 19`, `func_start: 20`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 62`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 18`
* *Defense:* `safety: 60`, `doc: 84`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::comments::SourceComment, ruff_python_ast::AnyNodeRef, format_comment, itertools::PeekingNext, crate::statement::clause::ClauseHeader, crate::statement::trailing_semicolon, TokenKind, trailing_comments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/noqa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.695 IQR)
- **Top Global Matches:** file_cluster_8: 11.695, file_cluster_0: 11.866, file_cluster_16: 12.04
- **Magnitude:** 1810.64 | **LOC:** 3024 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.24%), Tech Debt (43.1605%)
**Top Internal Functions/Classes:**
  * `find_noqa_comments` (Impact: 212.1 | O(N^6) | DB: 1)
  * `extract` (Impact: 89.4 | O(N^6) | DB: 1)
    * *Intent:* /// Extract the [`FileNoqaDirectives`] for a given Python source file, enumerating any rules /// tha...
  * `lex_code` (Impact: 81.1 | O(N^6) | DB: 1)
  * `lex_file_exemption` (Impact: 73.0 | O(N^4) | DB: 1)
  * `lex_directive` (Impact: 51.4 | O(N^6) | DB: 1)
    * *Intent:* /// Collect codes in `noqa` comment.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 365`, `args: 119`, `func_start: 128`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 79`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 112`, `import: 33`
* *Defense:* `safety: 282`, `doc: 74`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::Locator, SourceFileBuilder, crate::rules::pycodestyle::rules::AmbiguousVariableName, anyhow::Result, ruff_python_trivia::CommentRanges, crate::registry::Rule, crate::rule_redirects::get_redirect_target, lex_inline_noqa...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.798 IQR)
- **Top Global Matches:** file_cluster_8: 9.798, file_cluster_7: 10.531, file_cluster_1: 10.74
- **Magnitude:** 1720.4 | **LOC:** 1950 | **CtrlFlow:** 95.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.7027%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expression` (Impact: 1680.3 | O(N^6))
    * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 24`, `args: 12`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` flake8_pyi, pep8_naming, pycodestyle, crate::registry::Rule, flake8_logging, flake8_logging_format, flake8_simplify, flake8_type_checking...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.861 IQR)
- **Top Global Matches:** file_cluster_0: 11.861, file_cluster_8: 11.952, file_cluster_13: 12.13
- **Magnitude:** 1661.14 | **LOC:** 3203 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (7.5594%), Tech Debt (34.8151%)
**Top Internal Functions/Classes:**
  * `consume_ascii_character` (Impact: 467.3 | O(N^6) | DB: 1)
    * *Intent:* // Form feed
  * `lex_identifier` (Impact: 264.5 | O(N^6) | DB: 7)
  * `lex_string` (Impact: 184.5 | O(N^6) | DB: 2)
  * `lex_token` (Impact: 123.2 | O(N^6) | DB: 1)
  * `bom_with_offset_edge` (Impact: 119.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 216`, `args: 56`, `func_start: 129`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 78`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 6`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 70`, `doc: 147`, `test: 124`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ruff_python_ast::str_prefix::AnyStringPrefix, crate::lexer::indentation::Indentation, crate::string::InterpolatedStringKind, LexicalErrorType, EOF_CHAR, ruff_python_ast::name::Name, ruff_text_size::TextLen, TokenKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.197 IQR)
- **Top Global Matches:** file_cluster_13: 13.197, file_cluster_16: 13.215, file_cluster_8: 13.234
- **Magnitude:** 1642.72 | **LOC:** 1928 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (9.0416%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `any_over_expr` (Impact: 1436.0 | O(2^N) | DB: 46)
    * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
  * `contains_effect` (Impact: 52.6 | O(N^6))
    * *Intent:* /// Return `true` if the `Expr` contains an expression that appears to include a /// side-effect (li...
  * `is_compound_statement` (Impact: 4.7 | O(N^3))
    * *Intent:* /// Return `true` if the `Stmt` is a compound statement (as opposed to a simple statement).
  * `is_iterable_initializer` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 121`, `args: 116`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `state_mutation: 81`, `dead_code: 5`
* *Architecture:* `api: 44`, `import: 15`
* *Defense:* `safety: 114`, `doc: 154`, `test: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` QualifiedNameBuilder, ExprNumberLiteral, ruff_python_trivia::SimpleTokenKind, Identifier, TypeParams, crate::AnyNodeRef, QualifiedName, any_over_type_param...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.975 IQR)
- **Top Global Matches:** file_cluster_8: 9.975, file_cluster_7: 10.706, file_cluster_1: 10.929
- **Magnitude:** 1626.1 | **LOC:** 1668 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.7162%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `statement` (Impact: 1588.1 | O(N^6) | DB: 1)
    * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 43`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 53`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` flake8_pyi, flake8_errmsg, pep8_naming, pycodestyle, flake8_return, crate::registry::Rule, flake8_type_checking, flake8_simplify...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/rules/isort/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.989 IQR)
- **Top Global Matches:** file_cluster_8: 10.989, file_cluster_0: 11.016, file_cluster_13: 11.435
- **Magnitude:** 1623.32 | **LOC:** 1672 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (7.5302%), Tech Debt (7.812%)
**Top Internal Functions/Classes:**
  * `format_import_block` (Impact: 328.5 | O(N^6) | DB: 10)
  * `format_imports` (Impact: 161.4 | O(N^5) | DB: 1)
  * `import_heading_wrong_heading` (Impact: 29.9 | O(2^N))
  * `required_imports` (Impact: 29.5 | O(2^N))
  * `import_heading_partial` (Impact: 29.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 183`, `args: 59`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `api: 36`, `concurrency: 7`, `import: 32`
* *Defense:* `safety: 128`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::Locator, anyhow::Result, ImportFrom, crate::registry::Rule, ruff_python_ast::PySourceType, TrailingComma, ruff_python_semantic::MemberNameImport, crate::assert_diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.936 IQR)
- **Top Global Matches:** file_cluster_11: 14.936, file_cluster_13: 14.968, file_cluster_17: 14.978
- **Magnitude:** 1617.06 | **LOC:** 1102 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (9.9665%), Tech Debt (12.1325%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 1176.0 | O(2^N) | DB: 12)
    * *Intent:* /// Whether this suite is the last suite in the current statement. /// /// Below, `last_suite_in_sta...
  * `should_insert_blank_line_after_class_in_` (Impact: 267.6 | O(N^5) | DB: 6)
  * `stub_file_empty_lines` (Impact: 86.8 | O(N^4) | DB: 1)
  * `trailing_function_or_class_def` (Impact: 10.2 | O(N^3))
    * *Intent:* // Insert the appropriate number of empty lines based on the node level, e.g.: // * [`NodeLevel::Mod...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 122`, `args: 37`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 55`, `dead_code: 21`, `planned_debt: 7`
* *Architecture:* `api: 8`, `import: 19`
* *Defense:* `safety: 54`, `doc: 77`, `test: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ruff_python_ast::AnyNodeRef, FormatOwnedWithRule, ruff_python_trivia::CommentRanges, crate::comments::
    Comments, crate::context::NodeLevel, crate::statement::trailing_semicolon, has_skip_comment, crate::comments::Comments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.392 IQR)
- **Top Global Matches:** file_cluster_0: 12.392, file_cluster_16: 12.422, file_cluster_11: 12.481
- **Magnitude:** 1614.7 | **LOC:** 2953 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (6.9538%), Tech Debt (45.2934%)
**Top Internal Functions/Classes:**
  * `resolve_name_impl` (Impact: 525.4 | O(N^6) | DB: 72)
    * *Intent:* // Regular packages and modules are both terminal. A `foo.py` // in a higher-priority search path is...
  * `from_settings` (Impact: 191.7 | O(N^5) | DB: 3)
  * `dynamic_resolution_paths` (Impact: 139.3 | O(N^6) | DB: 3)
  * `next` (Impact: 133.9 | O(2^N) | DB: 1)
    * *Intent:* /// Iterator that yields a [`PthFile`] instance for every `.pth` file /// found in a given `site-pac...
  * `absolute_desperate_search_paths` (Impact: 93.9 | O(N^4) | DB: 1)
    * *Intent:* // This path is for a module with the same name but with a different precedence. For example: // ```...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 342`, `args: 75`, `func_start: 55`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 72`, `dead_code: 7`, `planned_debt: 25`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 16`, `api: 23`, `import: 23`
* *Defense:* `safety: 130`, `doc: 237`, `test: 82`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::module::Module, ruff_db::Db, SystemPath, crate::strategy::FallibleStrategy, FilePath, system_path_to_file, super::*, crate::typeshed::TypeshedVersions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_workspace/src/resolver.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.929 IQR)
- **Top Global Matches:** file_cluster_13: 12.929, file_cluster_16: 13.076, file_cluster_0: 13.095
- **Magnitude:** 1463.66 | **LOC:** 1188 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (15.6425%), Tech Debt (52.5033%)
**Top Internal Functions/Classes:**
  * `resolve_configuration` (Impact: 1010.7 | O(N^6) | DB: 44)
    * *Intent:* /// Recursively resolve a [`Configuration`] from a `pyproject.toml` file at the /// specified [`Path...
  * `package_roots` (Impact: 199.3 | O(2^N) | DB: 4)
    * *Intent:* /// Return a mapping from Python package to its package root.
  * `add` (Impact: 17.9 | O(N^4) | DB: 1)
    * *Intent:* /// Add a resolved [`Settings`] under a given [`PathBuf`] scope.
  * `detect_package_root_with_cache` (Impact: 15.4 | O(N^3) | DB: 2)
    * *Intent:* /// A wrapper around `detect_package_root` to cache filesystem lookups.
  * `resolve_with_path` (Impact: 11.3 | O(N^5))
    * *Intent:* /// Return the appropriate [`Settings`] and config file path for a given [`Path`].
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 223`, `args: 60`, `func_start: 43`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 79`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 7`, `api: 37`, `concurrency: 15`, `import: 37`
* *Defense:* `safety: 137`, `doc: 78`, `test: 16`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyhow::Result, Match, types::FilePattern, PyprojectDiscoveryStrategy, std::sync::RwLock, PathBuf, ignore::DirEntry, std::ffi::OsStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_6` (Drift: 21.153 IQR)
- **Top Global Matches:** file_cluster_6: 21.153, file_cluster_17: 21.169, file_cluster_11: 21.175
- **Magnitude:** 1356.6 | **LOC:** 4115 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (10.6708%), Tech Debt (9.2416%)
**Top Internal Functions/Classes:**
  * `parse_simple_statement` (Impact: 794.1 | O(N^6) | DB: 64)
    * *Intent:* // test_err simple_and_compound_stmt_on_same_line
  * `parse_parameters` (Impact: 191.5 | O(N^6) | DB: 19)
    * *Intent:* // for (x in y).attr in iter: ... // test_err for_stmt_invalid_target_in_keyword // for d(x in y) in...
  * `parse_simple_statements` (Impact: 80.3 | O(N^6) | DB: 3)
  * `fmt` (Impact: 42.4 | O(2^N) | DB: 1)
    * *Intent:* /// Parses a `with` statement /// /// The given `start` offset is the start of either the `with` tok...
  * `parse_single_simple_statement` (Impact: 37.5 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 213`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 149`, `dead_code: 152`, `planned_debt: 5`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 99`, `doc: 463`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ParsedExpr, crate::parser::progress::ParserProgress, Parser, ExprContext, std::fmt::Display, Stmt, WithItem, crate::error::StarTupleKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/suppression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.108 IQR)
- **Top Global Matches:** file_cluster_8: 11.108, file_cluster_16: 11.371, file_cluster_0: 11.386
- **Magnitude:** 1318.26 | **LOC:** 1973 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (9.1843%), Tech Debt (27.8218%)
**Top Internal Functions/Classes:**
  * `check_suppressions` (Impact: 196.7 | O(N^6) | DB: 4)
  * `load_from_tokens` (Impact: 124.7 | O(N^6) | DB: 6)
  * `delete_codes_or_comment` (Impact: 83.7 | O(N^5) | DB: 1)
  * `eat_codes` (Impact: 74.0 | O(N^5) | DB: 2)
  * `match_comments` (Impact: 73.2 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 190`, `args: 48`, `func_start: 61`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 44`, `import: 28`
* *Defense:* `safety: 96`, `doc: 24`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smallvec::SmallVec, crate::Locator, thiserror::Error, TextSlice, InvalidSuppressionCommentKind, crate::rule_redirects::get_redirect_target, Formatter, ruff_text_size::TextLen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_formatter/src/format_element/document.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.628 IQR)
- **Top Global Matches:** file_cluster_8: 11.628, file_cluster_13: 11.864, file_cluster_16: 11.871
- **Magnitude:** 1273.96 | **LOC:** 946 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (24.1%), Tech Debt (55.9646%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 626.2 | O(N^6) | DB: 7)
  * `propagate_expands` (Impact: 244.4 | O(2^N) | DB: 3)
  * `will_break` (Impact: 98.6 | O(2^N) | DB: 1)
  * `start_tag` (Impact: 81.2 | O(N^6) | DB: 3)
  * `escapes_quotes` (Impact: 22.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 104`, `args: 32`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 57`, `duplicate_logic: 6`, `orphaned_logic: 7`
* *Architecture:* `api: 3`, `import: 17`
* *Defense:* `safety: 67`, `doc: 11`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::source_code::SourceCode, format, Formatter, FormatOptions, Tag::EndGroup, EndIndent, IndentStyle, ruff_text_size::TextRange...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_literal/src/format.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.186 IQR)
- **Top Global Matches:** file_cluster_0: 13.186, file_cluster_8: 13.294, file_cluster_16: 13.328
- **Magnitude:** 1268.78 | **LOC:** 1098 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (12.8154%), Tech Debt (49.0428%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 917.1 | O(2^N) | DB: 18)
  * `parse_precision` (Impact: 36.9 | O(N^5) | DB: 1)
  * `parse_fill_and_align` (Impact: 28.9 | O(N^3))
  * `parse_nested_placeholders` (Impact: 23.0 | O(N^3) | DB: 2)
  * `from` (Impact: 17.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 159`, `args: 61`, `func_start: 50`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `dead_code: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 277`, `doc: 31`, `test: 58`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PeekingNext, crate::Case, std::error::Error, std::str::FromStr, super::*, itertools::Itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.137 IQR)
- **Top Global Matches:** file_cluster_8: 12.137, file_cluster_16: 12.227, file_cluster_7: 12.387
- **Magnitude:** 1174.62 | **LOC:** 3123 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.5965%), Tech Debt (98.8858%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 126.9 | O(2^N) | DB: 1)
  * `new` (Impact: 90.3 | O(2^N) | DB: 1)
  * `replace_unprintable` (Impact: 73.3 | O(N^4) | DB: 6)
  * `from_diagnostic` (Impact: 56.2 | O(N^5))
  * `context_before` (Impact: 54.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 262`, `args: 218`, `func_start: 69`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 106`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 27`, `orphaned_logic: 19`
* *Architecture:* `api: 23`, `import: 21`
* *Defense:* `safety: 53`, `doc: 334`, `test: 15`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` source::SourceText, IntoDiagnosticMessage, ruff_annotate_snippets::
    Annotation, SystemPath, Message, DiagnosticSource, Severity, ruff_text_size::TextLen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.8 IQR)
- **Top Global Matches:** file_cluster_16: 14.8, file_cluster_13: 14.875, file_cluster_11: 14.926
- **Magnitude:** 1116.28 | **LOC:** 2458 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.8116%), Tech Debt (10.254%)
**Top Internal Functions/Classes:**
  * `handle_own_line_comment_between_statemen` (Impact: 823.4 | O(N^4) | DB: 9)
  * `handle_parenthesized_comment` (Impact: 237.3 | O(N^5) | DB: 1)
    * *Intent:* /// Default handling can get parenthesized comments wrong in a number of ways. For example, the /// ...
  * `place_comment` (Impact: 3.9 | O(N^2))
    * *Intent:* /// Manually attach comments to nodes that the default placement gets wrong.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 145`, `args: 67`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `dead_code: 30`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 60`, `doc: 552`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ruff_python_trivia::
    BackwardsTokenizer, crate::expression::parentheses::is_expression_parenthesized, CommentRanges, first_non_trivia_token, crate::expression::expr_slice::ExprSliceCommentSection, crate::comments::placement::max_empty_lines, StringLike, Parameter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/rules/pydoclint/rules/check_docstring.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.805 IQR)
- **Top Global Matches:** file_cluster_0: 14.805, file_cluster_13: 14.871, file_cluster_11: 14.879
- **Magnitude:** 1088.6 | **LOC:** 1427 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (12.5116%), Tech Debt (97.9712%)
**Top Internal Functions/Classes:**
  * `parse_raises_google` (Impact: 780.5 | O(N^6) | DB: 13)
    * *Intent:* /// /// Args: /// distance: Distance traveled. /// time: Time spent traveling. /// /// Returns: /// ...
  * `parse_parameters_numpy` (Impact: 63.2 | O(N^6) | DB: 4)
    * *Intent:* /// distance: Distance traveled. /// time: Time spent traveling. /// /// Returns: /// Speed as dista...
  * `parse_parameters_google` (Impact: 56.7 | O(N^6) | DB: 2)
  * `from_sections` (Impact: 25.3 | O(N^6) | DB: 1)
  * `parse_parameters` (Impact: 23.3 | O(N^4))
    * *Intent:* /// This rule is not enforced for abstract methods. It is also ignored for /// "stub functions": fun...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 161`, `args: 58`, `func_start: 43`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `dead_code: 14`, `planned_debt: 6`, `duplicate_logic: 13`
* *Architecture:* `api: 5`, `import: 19`
* *Defense:* `safety: 126`, `doc: 388`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` visibility, ruff_python_ast::visitor::Visitor, SectionKind, crate::registry::Rule, ruff_python_semantic::analyze::function_type, crate::checkers::ast::Checker, map_subscript, ruff_python_semantic::Definition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.9 IQR)
- **Top Global Matches:** file_cluster_8: 12.9, file_cluster_13: 13.013, file_cluster_7: 13.016
- **Magnitude:** 1053.56 | **LOC:** 3096 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (18.6729%), Tech Debt (18.6297%)
**Top Internal Functions/Classes:**
  * `parse_arguments` (Impact: 119.0 | O(N^6) | DB: 11)
  * `parse_slice` (Impact: 80.5 | O(N^6) | DB: 2)
  * `parse_comparison_expression` (Impact: 57.9 | O(N^5) | DB: 5)
  * `parse_atom` (Impact: 53.9 | O(N^6) | DB: 9)
  * `parse_parenthesized_expression` (Impact: 45.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 192`, `args: 58`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 197`, `dead_code: 1`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 7`, `import: 16`
* *Defense:* `safety: 60`, `doc: 361`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bitflags::bitflags, crate::parser::progress::ParserProgress, StringType, parse_string_literal, AnyStringFlags, TString, crate::error::FStringKind, Parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/settings/types.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.573 IQR)
- **Top Global Matches:** file_cluster_16: 12.573, file_cluster_0: 12.676, file_cluster_13: 12.746
- **Magnitude:** 1034.98 | **LOC:** 951 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (6.9589%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `iter_matches` (Impact: 225.5 | O(N^6))
  * `fmt` (Impact: 69.9 | O(2^N) | DB: 1)
  * `fmt` (Impact: 69.9 | O(2^N) | DB: 1)
    * *Intent:* // Construct absolute path matcher.
  * `resolve` (Impact: 64.7 | O(N^5))
    * *Intent:* /// Pattern to match an identifier.
  * `from_str` (Impact: 50.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 154`, `args: 60`, `func_start: 54`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 44`, `planned_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 54`, `import: 21`
* *Defense:* `safety: 98`, `doc: 61`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ruff_db::diagnostic::DiagnosticFormat, GlobMatcher, Formatter, PathBuf, Hasher, std::fmt::Display, crate::Applicability, serde::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff/src/printer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.609 IQR)
- **Top Global Matches:** file_cluster_8: 10.609, file_cluster_13: 10.757, file_cluster_0: 11.053
- **Magnitude:** 1003.12 | **LOC:** 529 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.44%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_summary_text` (Impact: 419.1 | O(N^6) | DB: 1)
  * `write_once` (Impact: 174.4 | O(N^6) | DB: 1)
  * `write_statistics` (Impact: 170.1 | O(N^6) | DB: 2)
  * `write_continuously` (Impact: 75.6 | O(N^4) | DB: 1)
  * `try_from` (Impact: 55.9 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 80`, `args: 24`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 1`, `api: 13`, `import: 18`
* *Defense:* `safety: 33`, `doc: 6`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bitflags::bitflags, ruff_linter::message::EmitterContext, anyhow::Result, UnsafeFixes, SecondaryCode, FixMap, PreviewMode, std::io::Write...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_workspace/src/configuration.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.597 IQR)
- **Top Global Matches:** file_cluster_8: 11.597, file_cluster_13: 11.82, file_cluster_17: 11.898
- **Magnitude:** 958.16 | **LOC:** 2245 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.7527%), Tech Debt (10.2567%)
**Top Internal Functions/Classes:**
  * `into_settings` (Impact: 440.0 | O(2^N) | DB: 1)
  * `apply_fallbacks` (Impact: 264.7 | O(N^4) | DB: 3)
  * `from_options` (Impact: 162.6 | O(2^N) | DB: 1)
    * *Intent:* /// Convert the [`Options`] read from the given [`Path`] into a [`Configuration`]. /// If `None` is ...
  * `combine` (Impact: 8.4 | O(2^N))
  * `selectors_by_kind` (Impact: 6.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 138`, `args: 64`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 13`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 40`, `import: 43`
* *Defense:* `safety: 132`, `doc: 18`, `test: 36`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Flake8BugbearOptions, ruff_python_ast, ruff_linter::rules::pydocstyle::settings::Convention, ruff_linter::registry::INCOMPATIBLE_CODES, Flake8ImplicitStrConcatOptions, warn_user_once_by_message, crate::settings::
    EXCLUDE, regex::Regex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/string/normalize.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.012 IQR)
- **Top Global Matches:** file_cluster_13: 12.012, file_cluster_16: 12.043, file_cluster_8: 12.071
- **Magnitude:** 958.14 | **LOC:** 1155 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (10.7495%), Tech Debt (16.6544%)
**Top Internal Functions/Classes:**
  * `merge` (Impact: 795.1 | O(2^N) | DB: 12)
    * *Intent:* /// The quote style in the source.
  * `choose` (Impact: 37.7 | O(N^5))
  * `from_str` (Impact: 20.7 | O(N^3))
  * `from_part` (Impact: 15.1 | O(N^5))
  * `normalize` (Impact: 14.1 | O(N^4))
    * *Intent:* // ... unless we're formatting a code snippet inside a docstring, // then we specifically want to in...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 98`, `args: 20`, `func_start: 21`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 32`, `dead_code: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 12`, `import: 16`
* *Defense:* `safety: 51`, `doc: 87`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ruff_formatter::FormatContext, TextSlice, str_prefix::AnyStringPrefix, crate::string::Quote, InterpolatedStringElements, TripleQuotes, BytesLiteral, ruff_python_ast::
    AnyStringFlags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/debug_shadow_match.py` (PYTHON) | **Drift Ratio: 1.61x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.327 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.36 IQR)
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/debug_shadow_with.py` (PYTHON) | **Drift Ratio: 1.53x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.554 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.966 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ruff-0.15.9/crates/ruff_cache/tests/cache_key.rs` (RUST) | Magnitude: 59.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 58, state_mutation: 33, test: 14
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/self_or_cls_assignment.rs` (RUST) | Magnitude: 113.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, doc: 44, structural_boundaries: 24, branch: 13
- `ruff-0.15.9/crates/ty_module_resolver/src/module.rs` (RUST) | Magnitude: 425.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 318, structural_boundaries: 57, api: 44, branch: 43
- `ruff-0.15.9/crates/ruff_graph/src/settings.rs` (RUST) | Magnitude: 87.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, api: 12, encapsulation: 12
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/decorator_missing_newline.py` (PYTHON) | Magnitude: 19.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, decorators: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs` (RUST) | Magnitude: 1617.06 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 566, branch: 141, structural_boundaries: 122, doc: 77
- `ruff-0.15.9/crates/ruff_formatter/src/format_extensions.rs` (RUST) | Magnitude: 33.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 105, dead_code: 24, safety: 21, indent_spaces: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/type_alias_naming.rs` (RUST) | Magnitude: 48.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 53, indent_spaces: 43, structural_boundaries: 17, safety: 10
- `ruff-0.15.9/crates/ruff_python_formatter/src/pattern/pattern_match_as.rs` (RUST) | Magnitude: 115.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, branch: 19, structural_boundaries: 15, import: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_print/rules/print_call.rs` (RUST) | Magnitude: 57.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 79, indent_spaces: 50, structural_boundaries: 22, branch: 8
- `ruff-0.15.9/crates/ruff_server/src/session/index/ruff_settings.rs` (RUST) | Magnitude: 884.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 435, structural_boundaries: 77, safety: 66, branch: 57
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/collection_literal_concatenation.rs` (RUST) | Magnitude: 135.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, doc: 38, structural_boundaries: 28, safety: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/assign_stmt_invalid_value_expr.py` (PYTHON) | Magnitude: 15.6 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, lazy_evaluation: 2, branch: 1, structural_boundaries: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/aug_assign_stmt_invalid_value.py` (PYTHON) | Magnitude: 15.6 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, lazy_evaluation: 2, branch: 1, structural_boundaries: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/lambda_with_valid_body.py` (PYTHON) | Magnitude: 14.12 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 7, closures: 7, branch: 2, structural_boundaries: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/expressions/named.py` (PYTHON) | Magnitude: 38.16 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, branch: 2, lazy_evaluation: 2, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/redundant_numeric_union.rs` (RUST) | Magnitude: 122.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, doc: 62, structural_boundaries: 36, branch: 26
- `ruff-0.15.9/crates/ruff_linter/src/rules/isort/block.rs` (RUST) | Magnitude: 390.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 226, branch: 38, generics: 35, structural_boundaries: 31
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` (RUST) | Magnitude: 55.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 17, args: 9, doc: 9
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/test_rules.rs` (RUST) | Magnitude: 137.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 211, indent_spaces: 158, structural_boundaries: 52, decorators: 39
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/unnecessary_regular_expression.rs` (RUST) | Magnitude: 490.0 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 288, safety: 78, branch: 69, structural_boundaries: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/ambiguous_lpar_with_items.py` (PYTHON) | Magnitude: 70.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: branch: 77, state_mutation: 48, structural_boundaries: 32, comprehensions: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/rules/unused_import.rs` (RUST) | Magnitude: 645.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 383, doc: 238, structural_boundaries: 100, branch: 78
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/needless_bool.rs` (RUST) | Magnitude: 211.22 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 222, structural_boundaries: 49, doc: 47, safety: 39
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/assert_invalid_msg_expr.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, safety: 5, test: 5, sec_high_risk_execution: 5
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/assert_invalid_test_expr.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, safety: 5, test: 5, sec_high_risk_execution: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/while.py` (PYTHON) | Magnitude: 27.46 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 16, indent_spaces: 12, state_mutation: 6, concurrency: 6
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/nested_async_comprehension_py310.py` (PYTHON) | Magnitude: 331.03 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 12, structural_boundaries: 10, concurrency: 10, comprehensions: 7
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/invalid_annotation_function_py314.py` (PYTHON) | Magnitude: 11.3 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, args: 10, func_start: 10, indent_spaces: 6
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/valid_annotation_function_py313.py` (PYTHON) | Magnitude: 11.3 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, args: 10, func_start: 10, indent_spaces: 6
- `ruff-0.15.9/crates/ruff_python_parser/resources/invalid/expressions/await/recover.py` (PYTHON) | Magnitude: 24.68 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, concurrency: 10, args: 1, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/quoted_annotation_in_stub.rs` (RUST) | Magnitude: 11.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 12, structural_boundaries: 8, import: 4
- `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST) | Magnitude: 1356.6 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1132, doc: 463, structural_boundaries: 213, branch: 156
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_type_checking/rules/type_alias_quotes.rs` (RUST) | Magnitude: 13.58 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 110, indent_spaces: 79, structural_boundaries: 29, branch: 14
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_todos/rules/todos.rs` (RUST) | Magnitude: 66.38 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 140, indent_spaces: 71, planned_debt: 49, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/bad_string_format_character.rs` (RUST) | Magnitude: 99.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 18, doc: 17, branch: 13
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_gettext/mod.rs` (RUST) | Magnitude: 70.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 28, import: 12, branch: 11
- `ruff-0.15.9/crates/ruff_python_formatter/src/other/except_handler_except_handler.rs` (RUST) | Magnitude: 102.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 22, branch: 12, safety: 9
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/rdjson.rs` (RUST) | Magnitude: 87.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 50, generics: 44, args: 18
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/mod.rs` (RUST) | Magnitude: 228.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 463, decorators: 146, structural_boundaries: 32, safety: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/param_with_invalid_star_annotation.py` (PYTHON) | Magnitude: 50.8 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, func_start: 4, api: 4
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/with.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 12, structural_boundaries: 6, io: 2, dead_code: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/invalid/statements/match/as_pattern_0.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, indent_spaces: 2, safety_bypasses: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/debug_shadow_class.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, class_start: 2, encapsulation: 2, dead_code: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/params_multiple_varargs.py` (PYTHON) | Magnitude: 24.56 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 3, args: 3, func_start: 3, api: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 22591.002** (Blast Radius: 227.321 * Doc Risk: 99.3793%)
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` -> **Severity: 401.186** (Blast Radius: 4.091 * Doc Risk: 98.0655%)
- `ruff-0.15.9/crates/ruff_macros/src/newtype_index.rs` -> **Severity: 217.47** (Blast Radius: 3.125 * Doc Risk: 69.5903%)
- `ruff-0.15.9/crates/ruff_db/src/system/os.rs` -> **Severity: 188.858** (Blast Radius: 2.563 * Doc Risk: 73.6863%)
- `ruff-0.15.9/crates/ruff_linter/src/fs.rs` -> **Severity: 167.207** (Blast Radius: 1.706 * Doc Risk: 98.0114%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
