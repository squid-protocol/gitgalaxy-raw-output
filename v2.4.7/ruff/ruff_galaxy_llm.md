# ARCHITECTURAL_BRIEF: ruff
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/ruff` |
| **Timestamp** | `2026-08-07T05:26:25.366832+00:00` |
| **Scan Duration** | `7.06s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1830 malicious artifacts.

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
| file_cluster_0 | 137 | 7.3% |
| file_cluster_16 | 134 | 7.2% |
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
| Error & Exception Exposure | 0.0 | 99.5 | 23.0 | 17.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 41.1 | 26.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 2.4 | 80.0 |
| API Exposure | 0.0 | 14.9 | 2.7 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.1 | 11.9 | 11.9 |
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

- `expression` (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs`) -> Impact: **515.5** | LOC: 991
  * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
- `statement` (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs`) -> Impact: **492.6** | LOC: 1087
  * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
- `format` (@ `ruff-0.15.9/crates/ruff/src/commands/format.rs`) -> Impact: **383.0** | LOC: 997
  * *Intent:* /// Format a set of files, and return the exit status.
- `resolve_configuration` (@ `ruff-0.15.9/crates/ruff_workspace/src/resolver.rs`) -> Impact: **301.9** | LOC: 805
  * *Intent:* /// Recursively resolve a [`Configuration`] from a `pyproject.toml` file at the /// specified [`Path`]. // TODO(charlie): This whole system could do w...
- `quote_str` (@ `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs`) -> Impact: **282.4** | LOC: 1525
- `parse_simple_statement` (@ `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs`) -> Impact: **282.1** | LOC: 1603
  * *Intent:* // test_err simple_and_compound_stmt_on_same_line
- `handle_own_line_comment_between_statemen` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs`) -> Impact: **273.4** | LOC: 1168
- `write_suppressed_statements_starting_wit` (@ `ruff-0.15.9/crates/ruff_python_formatter/src/verbatim.rs`) -> Impact: **261.6** | LOC: 793
- `any_over_expr` (@ `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs`) -> Impact: **251.3** | LOC: 1076
  * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
- `parse_raises_google` (@ `ruff-0.15.9/crates/ruff_linter/src/rules/pydoclint/rules/check_docstring.rs`) -> Impact: **245.6** | LOC: 631
  * *Intent:* /// /// Args: /// distance: Distance traveled. /// time: Time spent traveling. /// /// Returns: /// Speed as distance divided by time. /// /// Raises:...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ruff-0.15.9/crates/ruff_python_ast/src` | 25 | 4619.64 | 9.22% | 51.45% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules` | 110 | 3986.48 | 5.92% | 71.78% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules` | 75 | 3568.32 | 6.48% | 53.26% |
| `ruff-0.15.9/crates/ruff_linter/src` | 21 | 2859.48 | 6.91% | 72.89% |
| `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err` | 154 | 2619.65 | 5.88% | 2.6% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules` | 43 | 2525.44 | 8.13% | 64.06% |
| `ruff-0.15.9/crates/ruff_python_formatter/src/comments` | 7 | 2476.02 | 8.97% | 86.76% |
| `ruff-0.15.9/crates/ty_module_resolver/src` | 11 | 2278.24 | 5.61% | 71.9% |
| `ruff-0.15.9/crates/ruff_python_formatter/src/expression` | 37 | 2206.22 | 13.58% | 67.21% |
| `ruff-0.15.9/crates/ruff_python_parser/src/parser` | 9 | 2141.96 | 8.13% | 38.27% |

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
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` -> **19** Orphaned Functions | **32** Duplicates
- `ruff-0.15.9/crates/ruff_python_ast/src/name.rs` -> **0** Orphaned Functions | **51** Duplicates
- `ruff-0.15.9/crates/ruff_python_ast/src/comparable.rs` -> **0** Orphaned Functions | **48** Duplicates

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
38. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_logging_format/rules/logging_call.rs`** -> AI Confidence: **99.31%**
39. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pie/rules/unnecessary_dict_kwargs.rs`** -> AI Confidence: **99.31%**
40. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pie/rules/unnecessary_spread.rs`** -> AI Confidence: **99.31%**
41. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/exit_annotations.rs`** -> AI Confidence: **99.31%**
42. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/unused_private_type_definition.rs`** -> AI Confidence: **99.31%**
43. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/raises.rs`** -> AI Confidence: **99.31%**
44. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/unittest_assert.rs`** -> AI Confidence: **99.31%**
45. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/warns.rs`** -> AI Confidence: **99.31%**
46. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/settings.rs`** -> AI Confidence: **99.31%**
47. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_return/rules/function.rs`** -> AI Confidence: **99.31%**
48. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/ast_ifexp.rs`** -> AI Confidence: **99.31%**
49. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/collapsible_if.rs`** -> AI Confidence: **99.31%**
50. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_tidy_imports/rules/lazy_import_mismatch.rs`** -> AI Confidence: **99.31%**
51. **`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_unused_arguments/rules/unused_arguments.rs`** -> AI Confidence: **99.31%**
52. **`ruff-0.15.9/crates/ruff_linter/src/rules/isort/block.rs`** -> AI Confidence: **99.31%**
53. **`ruff-0.15.9/crates/ruff_linter/src/rules/isort/helpers.rs`** -> AI Confidence: **99.31%**
54. **`ruff-0.15.9/crates/ruff_linter/src/rules/pep8_naming/settings.rs`** -> AI Confidence: **99.31%**
55. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/indentation.rs`** -> AI Confidence: **99.31%**
56. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/missing_whitespace_around_operator.rs`** -> AI Confidence: **99.31%**
57. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/whitespace_around_named_parameter_equals.rs`** -> AI Confidence: **99.31%**
58. **`ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/type_comparison.rs`** -> AI Confidence: **99.31%**
59. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydoclint/rules/check_docstring.rs`** -> AI Confidence: **99.31%**
60. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydocstyle/rules/backslashes.rs`** -> AI Confidence: **99.31%**
61. **`ruff-0.15.9/crates/ruff_linter/src/rules/pydocstyle/rules/not_missing.rs`** -> AI Confidence: **99.31%**
62. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/assert_on_string_literal.rs`** -> AI Confidence: **99.31%**
63. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/comparison_with_itself.rs`** -> AI Confidence: **99.31%**
64. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/continue_in_finally.rs`** -> AI Confidence: **99.31%**
65. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/import_private_name.rs`** -> AI Confidence: **99.31%**
66. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/magic_value_comparison.rs`** -> AI Confidence: **99.31%**
67. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/missing_maxsplit_arg.rs`** -> AI Confidence: **99.31%**
68. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/no_method_decorator.rs`** -> AI Confidence: **99.31%**
69. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/redefined_argument_from_local.rs`** -> AI Confidence: **99.31%**
70. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/single_string_slots.rs`** -> AI Confidence: **99.31%**
71. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/too_many_branches.rs`** -> AI Confidence: **99.31%**
72. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/too_many_nested_blocks.rs`** -> AI Confidence: **99.31%**
73. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/unexpected_special_method_signature.rs`** -> AI Confidence: **99.31%**
74. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/unspecified_encoding.rs`** -> AI Confidence: **99.31%**
75. **`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/useless_else_on_loop.rs`** -> AI Confidence: **99.31%**
76. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/deprecated_c_element_tree.rs`** -> AI Confidence: **99.31%**
77. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/extraneous_parentheses.rs`** -> AI Confidence: **99.31%**
78. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/pep695/mod.rs`** -> AI Confidence: **99.31%**
79. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/timeout_error_alias.rs`** -> AI Confidence: **99.31%**
80. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/unnecessary_default_type_args.rs`** -> AI Confidence: **99.31%**
81. **`ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/use_pep604_annotation.rs`** -> AI Confidence: **99.31%**
82. **`ruff-0.15.9/crates/ruff_linter/src/rules/refurb/rules/slice_to_remove_prefix_or_suffix.rs`** -> AI Confidence: **99.31%**
83. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/helpers.rs`** -> AI Confidence: **99.31%**
84. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/asyncio_dangling_task.rs`** -> AI Confidence: **99.31%**
85. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/float_equality_comparison.rs`** -> AI Confidence: **99.31%**
86. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/function_call_in_dataclass_default.rs`** -> AI Confidence: **99.31%**
87. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/incorrectly_parenthesized_tuple_in_subscript.rs`** -> AI Confidence: **99.31%**
88. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/logging_eager_conversion.rs`** -> AI Confidence: **99.31%**
89. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/mutable_class_default.rs`** -> AI Confidence: **99.31%**
90. **`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/unnecessary_regular_expression.rs`** -> AI Confidence: **99.31%**
91. **`ruff-0.15.9/crates/ruff_macros/src/config.rs`** -> AI Confidence: **99.31%**
92. **`ruff-0.15.9/crates/ruff_macros/src/violation_metadata.rs`** -> AI Confidence: **99.31%**
93. **`ruff-0.15.9/crates/ruff_python_ast/src/expression.rs`** -> AI Confidence: **99.31%**
94. **`ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs`** -> AI Confidence: **99.31%**
95. **`ruff-0.15.9/crates/ruff_python_ast/src/token.rs`** -> AI Confidence: **99.31%**
96. **`ruff-0.15.9/crates/ruff_python_ast/src/visitor.rs`** -> AI Confidence: **99.31%**
97. **`ruff-0.15.9/crates/ruff_python_formatter/src/comments/format.rs`** -> AI Confidence: **99.31%**
98. **`ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs`** -> AI Confidence: **99.31%**
99. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_attribute.rs`** -> AI Confidence: **99.31%**
100. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_bin_op.rs`** -> AI Confidence: **99.31%**
101. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_lambda.rs`** -> AI Confidence: **99.31%**
102. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_named.rs`** -> AI Confidence: **99.31%**
103. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_slice.rs`** -> AI Confidence: **99.31%**
104. **`ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_yield.rs`** -> AI Confidence: **99.31%**
105. **`ruff-0.15.9/crates/ruff_python_formatter/src/main.rs`** -> AI Confidence: **99.31%**
106. **`ruff-0.15.9/crates/ruff_python_formatter/src/other/with_item.rs`** -> AI Confidence: **99.31%**
107. **`ruff-0.15.9/crates/ruff_python_formatter/src/pattern/pattern_match_as.rs`** -> AI Confidence: **99.31%**
108. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_ann_assign.rs`** -> AI Confidence: **99.31%**
109. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_assign.rs`** -> AI Confidence: **99.31%**
110. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_aug_assign.rs`** -> AI Confidence: **99.31%**
111. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/stmt_expr.rs`** -> AI Confidence: **99.31%**
112. **`ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs`** -> AI Confidence: **99.31%**
113. **`ruff-0.15.9/crates/ruff_python_formatter/src/string/normalize.rs`** -> AI Confidence: **99.31%**
114. **`ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs`** -> AI Confidence: **99.31%**
115. **`ruff-0.15.9/crates/ruff_python_parser/src/semantic_errors.rs`** -> AI Confidence: **99.31%**
116. **`ruff-0.15.9/crates/ruff_python_parser/tests/generate_inline_tests.rs`** -> AI Confidence: **99.31%**
117. **`ruff-0.15.9/crates/ruff_python_semantic/src/analyze/function_type.rs`** -> AI Confidence: **99.31%**
118. **`ruff-0.15.9/crates/ruff_python_semantic/src/binding.rs`** -> AI Confidence: **99.31%**
119. **`ruff-0.15.9/crates/ruff_python_trivia/src/tokenizer.rs`** -> AI Confidence: **99.31%**
120. **`ruff-0.15.9/crates/ruff_server/src/edit.rs`** -> AI Confidence: **99.31%**
121. **`ruff-0.15.9/crates/ruff_python_ast/generate.py`** -> AI Confidence: **99.31%**
122. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ann_assign_stmt_invalid_value.py`** -> AI Confidence: **99.29%**
123. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/args_unparenthesized_generator.py`** -> AI Confidence: **99.29%**
124. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/backslash_continuation_indentation_error.py`** -> AI Confidence: **99.29%**
125. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/debug_shadow_match.py`** -> AI Confidence: **99.29%**
126. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/different_match_pattern_bindings.py`** -> AI Confidence: **99.29%**
127. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/duplicate_match_class_attr.py`** -> AI Confidence: **99.29%**
128. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/duplicate_match_key.py`** -> AI Confidence: **99.29%**
129. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/except_star_py310.py`** -> AI Confidence: **99.29%**
130. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/f_string_invalid_starred_expr.py`** -> AI Confidence: **99.29%**
131. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_iter_unpack_py38.py`** -> AI Confidence: **99.29%**
132. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_iter_expr.py`** -> AI Confidence: **99.29%**
133. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target.py`** -> AI Confidence: **99.29%**
134. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target_binary_expr.py`** -> AI Confidence: **99.29%**
135. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/for_stmt_invalid_target_in_keyword.py`** -> AI Confidence: **99.29%**
136. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_1.py`** -> AI Confidence: **99.29%**
137. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_2.py`** -> AI Confidence: **99.29%**
138. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/ipython_help_escape_command_error_recovery_3.py`** -> AI Confidence: **99.29%**
139. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/irrefutable_case_pattern.py`** -> AI Confidence: **99.29%**
140. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/lambda_body_with_starred_expr.py`** -> AI Confidence: **99.29%**
141. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_expected_colon.py`** -> AI Confidence: **99.29%**
142. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_expected_case_block.py`** -> AI Confidence: **99.29%**
143. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_invalid_guard_expr.py`** -> AI Confidence: **99.29%**
144. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/match_stmt_invalid_subject_expr.py`** -> AI Confidence: **99.29%**
145. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/multiple_assignment_in_case_pattern.py`** -> AI Confidence: **99.29%**
146. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/rebound_comprehension_variable.py`** -> AI Confidence: **99.29%**
147. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/starred_list_comp_py314.py`** -> AI Confidence: **99.29%**
148. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/t_string_invalid_starred_expr.py`** -> AI Confidence: **99.29%**
149. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/tuple_context_manager_py38.py`** -> AI Confidence: **99.29%**
150. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/unparenthesized_named_expr_set_comp_py38.py`** -> AI Confidence: **99.29%**
151. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/while_stmt_invalid_test_expr.py`** -> AI Confidence: **99.29%**
152. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/ambiguous_lpar_with_items_binary_expr.py`** -> AI Confidence: **99.29%**
153. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/ambiguous_lpar_with_items_if_expr.py`** -> AI Confidence: **99.29%**
154. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/args_unparenthesized_generator.py`** -> AI Confidence: **99.29%**
155. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/async_with_statement.py`** -> AI Confidence: **99.29%**
156. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/backslash_continuation_indentation.py`** -> AI Confidence: **99.29%**
157. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/different_match_pattern_bindings.py`** -> AI Confidence: **99.29%**
158. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/duplicate_match_key_attr.py`** -> AI Confidence: **99.29%**
159. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/except_star_py311.py`** -> AI Confidence: **99.29%**
160. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_in_target_valid_expr.py`** -> AI Confidence: **99.29%**
161. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_iter_unpack_py38.py`** -> AI Confidence: **99.29%**
162. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/for_iter_unpack_py39.py`** -> AI Confidence: **99.29%**
163. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/irrefutable_case_pattern_at_end.py`** -> AI Confidence: **99.29%**
164. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_as_pattern.py`** -> AI Confidence: **99.29%**
165. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_as_pattern_soft_keyword.py`** -> AI Confidence: **99.29%**
166. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_attr_pattern_soft_keyword.py`** -> AI Confidence: **99.29%**
167. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_identifier_1.py`** -> AI Confidence: **99.29%**
168. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_identifier_2.py`** -> AI Confidence: **99.29%**
169. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_1.py`** -> AI Confidence: **99.29%**
170. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_2.py`** -> AI Confidence: **99.29%**
171. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_classify_as_keyword_or_identifier.py`** -> AI Confidence: **99.29%**
172. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_sequence_pattern_parentheses_terminator.py`** -> AI Confidence: **99.29%**
173. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_sequence_pattern_terminator.py`** -> AI Confidence: **99.29%**
174. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_stmt_subject_expr.py`** -> AI Confidence: **99.29%**
175. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/match_stmt_valid_guard_expr.py`** -> AI Confidence: **99.29%**
176. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/nested_alternative_patterns.py`** -> AI Confidence: **99.29%**
177. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/parenthesized_named_expr_py38.py`** -> AI Confidence: **99.29%**
178. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/parenthesized_star_index_py310.py`** -> AI Confidence: **99.29%**
179. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/starred_list_comp_py315.py`** -> AI Confidence: **99.29%**
180. **`ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/unparenthesized_named_expr_py39.py`** -> AI Confidence: **99.29%**
181. **`ruff-0.15.9/crates/ruff_python_parser/resources/invalid/expressions/bool_op/invalid_rhs_expression.py`** -> AI Confidence: **99.29%**
182. **`ruff-0.15.9/crates/ruff_python_parser/resources/invalid/expressions/bool_op/missing_lhs.py`** -> AI Confidence: **99.29%**
183. **`ruff-0.15.9/crates/ruff_python_parser/resources/invalid/expressions/bool_op/missing_rhs.py`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `17644` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ruff-0.15.9/crates/ruff_index/src/slice.rs` (RUST) -> Cumulative Risk: **642.62**
- **Archetype:** `file_cluster_0` (Distance: 11.779 IQR)
- **Magnitude:** 108.16 | **LOC:** 214 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9994%), State Flux (96.3199%), Documentation (82.6145%)
- **Heaviest Functions:** `binary_search` (Impact: 4.0), `from_raw_mut` (Impact: 2.7), `from_raw` (Impact: 2.5)

### 2. `ruff-0.15.9/crates/ruff_python_ast/src/visitor/source_order.rs` (RUST) -> Cumulative Risk: **609.79**
- **Archetype:** `file_cluster_16` (Distance: 11.614 IQR)
- **Magnitude:** 375.36 | **LOC:** 624 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.888%), Tech Debt (97.5669%), Verification (80.0%)
- **Heaviest Functions:** `walk_expr` (Impact: 7.4), `walk_pattern` (Impact: 6.1), `walk_module` (Impact: 5.9)

### 3. `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/while.py` (PYTHON) -> Cumulative Risk: **568.69**
- **Archetype:** `file_cluster_4` (Distance: 10.221 IQR)
- **Magnitude:** 27.46 | **LOC:** 29 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Concurrency (99.9714%), State Flux (99.9713%)

### 4. `ruff-0.15.9/crates/ruff_formatter/src/buffer.rs` (RUST) -> Cumulative Risk: **564.29**
- **Archetype:** `file_cluster_0` (Distance: 16.373 IQR)
- **Magnitude:** 267.42 | **LOC:** 679 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.1466%), Verification (80.0%)
- **Heaviest Functions:** `clean_interned` (Impact: 29.7), `should_drop` (Impact: 16.2), `unwrap_any` (Impact: 6.8)

### 5. `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/invalid_annotation_function_py314.py` (PYTHON) -> Cumulative Risk: **560.08**
- **Archetype:** `file_cluster_4` (Distance: 11.812 IQR)
- **Magnitude:** 11.3 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (99.6731%), Concurrency (99.342%), Safety Score (71.095%)
- **Heaviest Functions:** `outer` (Impact: 2.1), `outer` (Impact: 2.0)

### 6. `ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/valid_annotation_function_py313.py` (PYTHON) -> Cumulative Risk: **560.08**
- **Archetype:** `file_cluster_4` (Distance: 11.812 IQR)
- **Magnitude:** 11.3 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (99.6731%), Concurrency (99.342%), Safety Score (71.095%)
- **Heaviest Functions:** `outer` (Impact: 2.1), `outer` (Impact: 2.0)

### 7. `ruff-0.15.9/crates/ruff_cache/src/cache_key.rs` (RUST) -> Cumulative Risk: **558.29**
- **Archetype:** `file_cluster_0` (Distance: 12.92 IQR)
- **Magnitude:** 189.32 | **LOC:** 471 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.6631%), Verification (80.0%)
- **Heaviest Functions:** `cache_key` (Impact: 4.0), `cache_key` (Impact: 4.0), `cache_key_slice` (Impact: 3.9)

### 8. `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/invalid_annotation_function.py` (PYTHON) -> Cumulative Risk: **554.68**
- **Archetype:** `file_cluster_4` (Distance: 12.121 IQR)
- **Magnitude:** 98.23 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.994%)

### 9. `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/ambiguous_lpar_with_items.py` (PYTHON) -> Cumulative Risk: **553.43**
- **Archetype:** `file_cluster_17` (Distance: 11.519 IQR)
- **Magnitude:** 70.4 | **LOC:** 105 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (96.1307%)

### 10. `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/if.py` (PYTHON) -> Cumulative Risk: **553.41**
- **Archetype:** `file_cluster_4` (Distance: 9.498 IQR)
- **Magnitude:** 33.64 | **LOC:** 38 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.4622%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.763 IQR)
- **Top Global Matches:** file_cluster_16: 14.763, file_cluster_13: 14.839, file_cluster_11: 14.891
- **Magnitude:** 1486.38 | **LOC:** 2458 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6096%), Tech Debt (18.1245%)
**Top Internal Functions/Classes:**
  * `handle_own_line_comment_between_statemen` (Impact: 273.4)
  * `handle_trailing_binary_expression_left_o` (Impact: 216.8)
  * `handle_slice_comments` (Impact: 192.7)
    * *Intent:* // The comment belongs to the last statement, unless the preceding branch has a body. // ```python /...
  * `handle_dict_unpacking_comment` (Impact: 170.1)
    * *Intent:* // There a three cases: // ```python
  * `handle_attribute_comment` (Impact: 158.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 145`, `args: 70`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `dead_code: 30`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 60`, `doc: 552`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::pattern::pattern_match_sequence::SequenceType, StringLike, AnyNodeRef, SimpleToken, find_only_token_in_range, Parameter, DecoratedComment, Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.516 IQR)
- **Top Global Matches:** file_cluster_16: 13.516, file_cluster_0: 13.567, file_cluster_8: 13.833
- **Magnitude:** 1261.24 | **LOC:** 3855 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.058%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `quote_str` (Impact: 282.4)
  * `next` (Impact: 12.8)
  * `next` (Impact: 12.8)
    * *Intent:* /// Returns an iterator over all parameters in source order. /// /// This differs from [`Parameters:...
  * `next` (Impact: 11.2)
  * `next_back` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 424`, `args: 287`, `func_start: 256`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 182`, `dead_code: 8`, `planned_debt: 3`, `duplicate_logic: 94`
* *Architecture:* `api: 325`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 236`, `doc: 657`, `test: 48`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crate::generated::
    ExprBytesLiteral, TypeParam, std::slice::Iter, str::Quote, ExprList, crate::str_prefix::
    AnyStringPrefix, TripleQuotes, PatternMatchAs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_6` (Drift: 21.144 IQR)
- **Top Global Matches:** file_cluster_6: 21.144, file_cluster_11: 21.166, file_cluster_17: 21.174
- **Magnitude:** 948.9 | **LOC:** 4115 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5233%), Tech Debt (9.2416%)
**Top Internal Functions/Classes:**
  * `parse_simple_statement` (Impact: 282.1)
    * *Intent:* // test_err simple_and_compound_stmt_on_same_line
  * `parse_parameters` (Impact: 65.9)
    * *Intent:* // for (x in y).attr in iter: ... // test_err for_stmt_invalid_target_in_keyword // for d(x in y) in...
  * `parse_type_param` (Impact: 53.1)
  * `parse_try_statement` (Impact: 37.1)
  * `parse_from_import_statement` (Impact: 36.8)
    * *Intent:* /// Parses a delete statement. ///
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 213`, `args: 40`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 147`, `dead_code: 152`, `planned_debt: 5`
* *Architecture:* `api: 12`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 99`, `doc: 463`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UnsupportedSyntaxErrorKind, IpyEscapeKind, crate::parser::progress::ParserProgress, RecoveryContextKind, Expr, ruff_text_size::Ranged, super::expression::ExpressionContext, RecoveryContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff/src/commands/format.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.043 IQR)
- **Top Global Matches:** file_cluster_13: 12.043, file_cluster_8: 12.21, file_cluster_0: 12.332
- **Magnitude:** 914.76 | **LOC:** 1426 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0512%), Tech Debt (30.1773%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 383.0)
    * *Intent:* /// Format a set of files, and return the exit status.
  * `to_diagnostics` (Impact: 177.4)
  * `warn_incompatible_formatter_settings` (Impact: 76.2)
  * `format_source` (Impact: 66.9)
  * `write_summary` (Impact: 41.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 184`, `args: 33`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 58`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 12`, `import: 53`
* *Defense:* `safety: 95`, `doc: 33`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` catch_unwind, DiagnosticId, FormatArguments, stdout, rayon::iter::Either::Left, std::fs::File, FormatMode, ruff_linter::source_kind::SourceError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/noqa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.716 IQR)
- **Top Global Matches:** file_cluster_8: 11.716, file_cluster_0: 11.887, file_cluster_16: 12.061
- **Magnitude:** 845.64 | **LOC:** 3024 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.24%), Tech Debt (43.1605%)
**Top Internal Functions/Classes:**
  * `find_noqa_comments` (Impact: 51.2)
  * `lex_file_exemption` (Impact: 30.9)
  * `lex_code` (Impact: 26.1)
  * `extract` (Impact: 17.8)
    * *Intent:* /// Extract the [`FileNoqaDirectives`] for a given Python source file, enumerating any rules /// tha...
  * `lex_directive` (Impact: 16.4)
    * *Intent:* /// Collect codes in `noqa` comment.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 365`, `args: 145`, `func_start: 128`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 79`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 112`, `import: 33`
* *Defense:* `safety: 282`, `doc: 74`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lex_codes, crate::Edit, crate::fs::relativize_path, ruff_db::diagnostic::Diagnostic, generate_noqa_edits, crate::registry::Rule, NoqaMapping, std::collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_workspace/src/resolver.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.87 IQR)
- **Top Global Matches:** file_cluster_13: 12.87, file_cluster_16: 13.015, file_cluster_0: 13.033
- **Magnitude:** 758.06 | **LOC:** 1188 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.2235%), Tech Debt (84.8817%)
**Top Internal Functions/Classes:**
  * `resolve_configuration` (Impact: 301.9)
    * *Intent:* /// Recursively resolve a [`Configuration`] from a `pyproject.toml` file at the /// specified [`Path...
  * `visit` (Impact: 48.5)
  * `match_any_exclusion` (Impact: 28.7)
  * `package_roots` (Impact: 27.6)
    * *Intent:* /// Return a mapping from Python package to its package root.
  * `project_file_at_path` (Impact: 19.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 223`, `args: 59`, `func_start: 43`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 75`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 7`, `api: 45`, `concurrency: 15`, `import: 37`
* *Defense:* `safety: 137`, `doc: 78`, `test: 16`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyhow::anyhow, ignore::DirEntry, anyhow::Context, log::debug, path_absolutize::path_dedot, bail, ParallelVisitor, tempfile::TempDir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.149 IQR)
- **Top Global Matches:** file_cluster_13: 13.149, file_cluster_16: 13.17, file_cluster_8: 13.207
- **Magnitude:** 745.52 | **LOC:** 1928 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9131%), Tech Debt (30.9466%)
**Top Internal Functions/Classes:**
  * `any_over_expr` (Impact: 251.3)
    * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
  * `is_unpacking_assignment` (Impact: 58.9)
  * `contains_effect` (Impact: 18.0)
    * *Intent:* /// Return `true` if the `Expr` contains an expression that appears to include a /// side-effect (li...
  * `extract_handled_exceptions` (Impact: 14.9)
  * `generate_comparison` (Impact: 13.4)
    * *Intent:* /// Format the call path for a relative import. /// /// # Examples /// /// ```rust /// # use ruff_py...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 121`, `args: 96`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `state_mutation: 77`, `dead_code: 5`, `duplicate_logic: 7`
* *Architecture:* `api: 70`, `import: 15`
* *Defense:* `safety: 114`, `doc: 154`, `test: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arguments, ruff_python_ast::helpers::format_import_from, TypeParam, crate::statement_visitor::StatementVisitor, TypeParamParamSpec, ExprNoneLiteral, crate::name::Name, Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.416 IQR)
- **Top Global Matches:** file_cluster_0: 12.416, file_cluster_16: 12.453, file_cluster_11: 12.51
- **Magnitude:** 741.8 | **LOC:** 2953 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0924%), Tech Debt (84.7419%)
**Top Internal Functions/Classes:**
  * `resolve_name_impl` (Impact: 170.6)
    * *Intent:* // Regular packages and modules are both terminal. A `foo.py` // in a higher-priority search path is...
  * `from_settings` (Impact: 69.2)
  * `absolute_desperate_search_paths` (Impact: 39.3)
    * *Intent:* // This path is for a module with the same name but with a different precedence. For example: // ```...
  * `dynamic_resolution_paths` (Impact: 39.2)
  * `file_to_module_impl` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 342`, `args: 92`, `func_start: 55`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 72`, `dead_code: 7`, `planned_debt: 25`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 26`
* *Architecture:* `io: 16`, `api: 23`, `import: 23`
* *Defense:* `safety: 130`, `doc: 237`, `test: 82`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FilePath, system_path_to_file, anyhow::Context, SearchPathSettingsError, PySourceType, crate::db::Db, ruff_db::vendored::VendoredFileSystem, MockedTypeshed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.052 IQR)
- **Top Global Matches:** file_cluster_8: 12.052, file_cluster_16: 12.101, file_cluster_0: 12.208
- **Magnitude:** 738.74 | **LOC:** 1955 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.687%), Tech Debt (58.4814%)
**Top Internal Functions/Classes:**
  * `format_line` (Impact: 134.0)
  * `fold_body` (Impact: 123.8)
  * `format_annotation` (Impact: 57.4)
  * `format_header` (Impact: 32.5)
  * `format_raw_line` (Impact: 22.9)
    * *Intent:* // In the hide-severity case, we need a space instead of the colon and space below.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 227`, `args: 68`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `state_mutation: 100`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 38`, `import: 12`
* *Defense:* `safety: 123`, `doc: 77`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::renderer::DEFAULT_TERM_WIDTH, Margin, crate::renderer::styled_buffer::StyledBuffer, max, stylesheet::Stylesheet, std::collections::HashMap, std::cmp::Reverse, std::cmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff/tests/cli/lint.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.522 IQR)
- **Top Global Matches:** file_cluster_8: 10.522, file_cluster_7: 10.989, file_cluster_0: 11.069
- **Magnitude:** 711.24 | **LOC:** 4440 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `output_format` (Impact: 170.1)
  * `cookiecutter_globbing` (Impact: 163.1)
    * *Intent:* #[test]
  * `value_given_to_table_key_is_not_inline_t` (Impact: 20.9)
  * `exclude` (Impact: 17.3)
  * `cache_syntax_errors` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 149`, `args: 45`, `func_start: 51`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 16`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 37`
* *Architecture:* `io: 1`, `concurrency: 10`, `import: 11`
* *Defense:* `safety: 97`, `doc: 128`, `test: 48`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` insta_cmd::assert_cmd_snapshot, std::fs, get_cargo_bin, std::str, std::process::Command, crate::CliTest, anyhow::Result
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.964 IQR)
- **Top Global Matches:** file_cluster_0: 11.964, file_cluster_8: 12.056, file_cluster_13: 12.234
- **Magnitude:** 707.44 | **LOC:** 3203 | **CtrlFlow:** 49.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3001%), Tech Debt (49.5645%)
**Top Internal Functions/Classes:**
  * `consume_ascii_character` (Impact: 139.1)
    * *Intent:* // Form feed
  * `lex_identifier` (Impact: 82.6)
  * `bom_with_offset_edge` (Impact: 71.5)
  * `lex_string` (Impact: 52.0)
  * `test_tstring_escape` (Impact: 42.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 216`, `args: 137`, `func_start: 129`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 78`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 13`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 70`, `doc: 147`, `test: 124`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::error::InterpolatedStringErrorType, LexicalErrorType, IpyEscapeKind, ruff_python_trivia::is_python_whitespace, crate::lexer::cursor::Cursor, ruff_python_ast::Int, Indentations, IndentationsCheckpoint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/rules/pydoclint/rules/check_docstring.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.796 IQR)
- **Top Global Matches:** file_cluster_0: 14.796, file_cluster_13: 14.866, file_cluster_11: 14.876
- **Magnitude:** 668.1 | **LOC:** 1427 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0505%), Tech Debt (99.7812%)
**Top Internal Functions/Classes:**
  * `parse_raises_google` (Impact: 245.6)
    * *Intent:* /// /// Args: /// distance: Distance traveled. /// time: Time spent traveling. /// /// Returns: /// ...
  * `check_docstring` (Impact: 120.1)
  * `visit_stmt` (Impact: 32.7)
    * *Intent:* /// Parses Google-style "Args" sections of the form: /// /// ```python /// Args: /// a (int): The fi...
  * `parse_parameters_numpy` (Impact: 19.9)
    * *Intent:* /// distance: Distance traveled. /// time: Time spent traveling. /// /// Returns: /// Speed as dista...
  * `parse_parameters_google` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 161`, `args: 60`, `func_start: 43`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `dead_code: 14`, `planned_debt: 6`, `duplicate_logic: 16`, `orphaned_logic: 5`
* *Architecture:* `api: 5`, `import: 19`
* *Defense:* `safety: 126`, `doc: 388`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` NewlineWithTrailingNewline, crate::docstrings::sections::SectionContext, crate::checkers::ast::Checker, crate::rules::pydocstyle::settings::Convention, crate::registry::Rule, ruff_python_ast::self, crate::docstrings::Docstring, Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_trivia/src/tokenizer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.348 IQR)
- **Top Global Matches:** file_cluster_8: 11.348, file_cluster_16: 11.438, file_cluster_7: 11.53
- **Magnitude:** 625.44 | **LOC:** 1042 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7188%), Tech Debt (89.6181%)
**Top Internal Functions/Classes:**
  * `to_keyword_or_other` (Impact: 182.6)
  * `lines_after_ignoring_trivia` (Impact: 179.1)
    * *Intent:* /// Counts the empty lines after `offset`, ignoring any trailing trivia: end-of-line comments, /// o...
  * `next_token_inner` (Impact: 108.6)
    * *Intent:* /// `}`
  * `next_token` (Impact: 23.1)
  * `lines_before` (Impact: 11.6)
    * *Intent:* /// Returns the number of newlines between `offset` and the first non whitespace character in the so...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 62`, `args: 46`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 30`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `api: 14`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 23`, `doc: 123`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TextRange, is_python_whitespace, TextSize, is_xid_start, crate::Cursor, unicode_ident::is_xid_continue, TextLen, ruff_text_size::Ranged
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/generate.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.914 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.287 IQR)
- **Top Global Matches:** file_cluster_16: 13.914, file_cluster_13: 13.996, file_cluster_8: 14.097
- **Magnitude:** 617.62 | **LOC:** 1106 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.7297%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `write_node` (Impact: 56.5)
  * `__init__` (Impact: 36.3)
  * `write_owned_enum` (Impact: 19.6)
    * *Intent:* # ------------------------------------------------------------------------------ # Owned enum def wr...
  * `fields_in_source_order` (Impact: 13.0)
  * `extract_type_argument` (Impact: 10.7)
    * *Intent:* # Extracts the type argument from the given rust type with AST field type syntax. # Box<str> -> str ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 60`, `args: 24`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 389`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 24`, `import: 7`
* *Defense:* `safety: 11`, `doc: 164`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dataclasses, re, tomllib, __future__, typing, pathlib, subprocess
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.889 IQR)
- **Top Global Matches:** file_cluster_8: 12.889, file_cluster_13: 13.002, file_cluster_7: 13.005
- **Magnitude:** 598.36 | **LOC:** 3096 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5658%), Tech Debt (18.6297%)
**Top Internal Functions/Classes:**
  * `parse_arguments` (Impact: 39.0)
  * `parse_slice` (Impact: 25.4)
  * `parse_comparison_expression` (Impact: 20.8)
  * `parse_atom` (Impact: 18.9)
  * `parse_parenthesized_expression` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 192`, `args: 55`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 197`, `dead_code: 1`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 7`, `import: 16`
* *Defense:* `safety: 60`, `doc: 361`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UnsupportedSyntaxErrorKind, IpyEscapeKind, Mode, crate::string::
    InterpolatedStringKind, crate::parser::progress::ParserProgress, RecoveryContextKind, parse_string_literal, Expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_literal/src/format.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.162 IQR)
- **Top Global Matches:** file_cluster_0: 13.162, file_cluster_8: 13.304, file_cluster_16: 13.316
- **Magnitude:** 597.28 | **LOC:** 1098 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2579%), Tech Debt (83.2416%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 161.1)
  * `parse_spec` (Impact: 25.7)
  * `parse_part` (Impact: 22.6)
  * `parse` (Impact: 19.1)
  * `parse_literal` (Impact: 19.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 159`, `args: 58`, `func_start: 50`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `dead_code: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 40`, `import: 5`
* *Defense:* `safety: 277`, `doc: 31`, `test: 58`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, std::error::Error, std::str::FromStr, PeekingNext, crate::Case, itertools::Itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/suppression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.165 IQR)
- **Top Global Matches:** file_cluster_8: 11.165, file_cluster_16: 11.427, file_cluster_0: 11.441
- **Magnitude:** 583.16 | **LOC:** 1973 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1618%), Tech Debt (27.8218%)
**Top Internal Functions/Classes:**
  * `check_suppressions` (Impact: 61.6)
  * `load_from_tokens` (Impact: 39.7)
  * `eat_codes` (Impact: 26.0)
  * `match_comments` (Impact: 23.2)
  * `eat_action` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 190`, `args: 84`, `func_start: 61`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 44`, `import: 28`
* *Defense:* `safety: 96`, `doc: 24`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ParseOptions, crate::fix::edits::delete_comment, InvalidRuleCodeKind, ruff_python_parser::Mode, ParseError, Fix, std::fmt::self, smallvec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_semantic/src/analyze/typing.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.849 IQR)
- **Top Global Matches:** file_cluster_16: 12.849, file_cluster_8: 13.046, file_cluster_13: 13.055
- **Magnitude:** 563.06 | **LOC:** 1333 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9536%), Tech Debt (82.7075%)
**Top Internal Functions/Classes:**
  * `to_pep604_operator` (Impact: 230.7)
    * *Intent:* /// Return the PEP 604 operator variant to which the given subscript [`Expr`] corresponds, if any.
  * `inner` (Impact: 36.9)
    * *Intent:* // If any of the elements are starred expressions, we can't rewrite the subscript:
  * `match_annotated_subscript` (Impact: 28.6)
  * `find_binding_value` (Impact: 14.3)
  * `match_target` (Impact: 14.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 135`, `args: 83`, `func_start: 43`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `dead_code: 5`, `duplicate_logic: 12`
* *Architecture:* `api: 45`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 107`, `doc: 147`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is_pep_593_generic_member, Modules, ruff_python_stdlib::typing::
    as_pep_585_generic, ExprCall, crate::Binding, StmtAssign, smallvec, ResolvedPythonType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.796 IQR)
- **Top Global Matches:** file_cluster_8: 9.796, file_cluster_7: 10.53, file_cluster_1: 10.739
- **Magnitude:** 555.6 | **LOC:** 1950 | **CtrlFlow:** 95.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.7027%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expression` (Impact: 515.5)
    * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 24`, `args: 11`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Arguments, flake8_print, flake8_simplify, crate::rules::
    airflow, flake8_logging_format, crate::checkers::ast::Checker, ruff_python_ast::types::Node, crate::registry::Rule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/visitor/transformer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.444 IQR)
- **Top Global Matches:** file_cluster_8: 12.444, file_cluster_16: 12.851, file_cluster_0: 12.92
- **Magnitude:** 547.64 | **LOC:** 875 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.7636%), Tech Debt (8.467%)
**Top Internal Functions/Classes:**
  * `walk_expr` (Impact: 55.4)
  * `walk_stmt` (Impact: 49.0)
  * `walk_parameters` (Impact: 22.5)
  * `walk_pattern` (Impact: 13.9)
  * `walk_type_param` (Impact: 12.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 133`, `args: 61`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `state_mutation: 204`, `orphaned_logic: 1`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 71`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arguments, TypeParam, TypeParamParamSpec, PatternKeyword, Parameter, Expr, ElifElseClause, TypeParamTypeVar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.009 IQR)
- **Top Global Matches:** file_cluster_8: 10.009, file_cluster_7: 10.737, file_cluster_1: 10.959
- **Magnitude:** 540.6 | **LOC:** 1668 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.7162%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `statement` (Impact: 492.6)
    * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
  * `bad_version_info_comparison` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 43`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 53`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ruff_python_ast::helpers, flake8_simplify, crate::rules::
    airflow, crate::checkers::ast::Checker, ruff_python_ast::types::Node, crate::registry::Rule, ruff_python_ast::self, flake8_import_conventions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.05 IQR)
- **Top Global Matches:** file_cluster_8: 12.05, file_cluster_16: 12.141, file_cluster_7: 12.302
- **Magnitude:** 522.42 | **LOC:** 3123 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4012%), Tech Debt (99.5794%)
**Top Internal Functions/Classes:**
  * `replace_unprintable` (Impact: 27.5)
  * `fmt` (Impact: 23.0)
  * `context_after` (Impact: 21.0)
    * *Intent:* /// An abstraction over a unit of user input. ///
  * `context_before` (Impact: 20.9)
  * `sub_diag_repeats_snippet` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 262`, `args: 145`, `func_start: 69`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 106`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 32`, `orphaned_logic: 19`
* *Architecture:* `api: 23`, `import: 21`
* *Defense:* `safety: 53`, `doc: 334`, `test: 15`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` NotebookIndex, UnifiedFile, DiagnosticId, SubDiagnostic, super::
    Annotation, crate::system::DbWithWritableSystem, Fix, crate::diagnostic::
        Annotation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/rules/isort/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.987 IQR)
- **Top Global Matches:** file_cluster_8: 10.987, file_cluster_0: 11.014, file_cluster_13: 11.432
- **Magnitude:** 511.22 | **LOC:** 1672 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5302%), Tech Debt (7.812%)
**Top Internal Functions/Classes:**
  * `format_import_block` (Impact: 84.3)
  * `format_imports` (Impact: 46.2)
  * `import_heading_wrong_heading` (Impact: 5.8)
  * `required_import_unused` (Impact: 5.7)
  * `default_section_can_map_to_user_defined_` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 183`, `args: 60`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `api: 36`, `concurrency: 7`, `import: 32`
* *Defense:* `safety: 128`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` settings::Settings, crate::assert_diagnostics, categorize::categorize, LineWidthBuilder, crate::line_width::LineLength, NameImport, crate::registry::Rule, test_resource_path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/semantic_errors.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 18.022 IQR)
- **Top Global Matches:** file_cluster_0: 18.022, file_cluster_17: 18.103, file_cluster_11: 18.109
- **Magnitude:** 510.34 | **LOC:** 2381 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3598%), Tech Debt (95.5821%)
**Top Internal Functions/Classes:**
  * `yield_outside_function` (Impact: 169.0)
  * `visit_stmt` (Impact: 102.5)
    * *Intent:* // test_ok valid_annotation_py313 // # parse_options: {"target-version": "3.13"} // a: (x := 1) // d...
  * `visit_pattern` (Impact: 63.1)
    * *Intent:* // # parse_options: {"target-version": "3.13"} // a: (x := 1) // def outer(): // b: (yield 1) // c: ...
  * `visit_expr` (Impact: 31.6)
  * `await_outside_async_function` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 70`, `args: 12`, `func_start: 31`, `class_start: 9`
* *Risk/State:* `state_mutation: 45`, `dead_code: 36`, `planned_debt: 1`, `duplicate_logic: 7`, `orphaned_logic: 4`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 66`, `doc: 485`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` walk_expr, Expr, ruff_text_size::Ranged, visitor::Visitor, walk_stmt, std::fmt::Display, StmtExpr, ruff_python_ast::
    self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/verbatim.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.984 IQR)
- **Top Global Matches:** file_cluster_16: 11.984, file_cluster_8: 12.0, file_cluster_13: 12.069
- **Magnitude:** 491.72 | **LOC:** 958 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1647%), Tech Debt (58.4985%)
**Top Internal Functions/Classes:**
  * `write_suppressed_statements_starting_wit` (Impact: 261.6)
  * `fmt` (Impact: 30.0)
  * `next` (Impact: 22.4)
  * `next` (Impact: 21.9)
    * *Intent:* /// A `fmt: on` comment inside a suppressed range.
  * `trim_indent` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 142`, `args: 25`, `func_start: 20`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 56`, `duplicate_logic: 7`, `orphaned_logic: 3`
* *Architecture:* `api: 7`, `import: 18`
* *Defense:* `safety: 60`, `doc: 84`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::comments::format::empty_lines, std::slice::Iter, ruff_formatter::FormatError, trailing_comments, write, itertools::PeekingNext, ruff_python_trivia::lines_before, ruff_text_size::Ranged...
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
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/self_or_cls_assignment.rs` (RUST) | Magnitude: 42.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, doc: 44, structural_boundaries: 24, branch: 13
- `ruff-0.15.9/crates/ruff_graph/src/settings.rs` (RUST) | Magnitude: 40.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, api: 12, encapsulation: 12
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/decorator_missing_newline.py` (PYTHON) | Magnitude: 19.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, decorators: 3, args: 2, func_start: 2
- `ruff-0.15.9/crates/ruff_db/src/files/path.rs` (RUST) | Magnitude: 21.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, sec_high_risk_execution: 34, doc: 23, safety: 9
- `ruff-0.15.9/crates/ruff_python_parser/src/token.rs` (RUST) | Magnitude: 16.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, indent_spaces: 7, safety: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs` (RUST) | Magnitude: 471.76 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 566, branch: 141, structural_boundaries: 122, doc: 77
- `ruff-0.15.9/crates/ruff_formatter/src/format_extensions.rs` (RUST) | Magnitude: 20.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 105, dead_code: 24, safety: 21, indent_spaces: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/type_alias_naming.rs` (RUST) | Magnitude: 29.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 53, indent_spaces: 43, structural_boundaries: 17, safety: 10
- `ruff-0.15.9/crates/ruff_python_formatter/src/pattern/pattern_match_as.rs` (RUST) | Magnitude: 44.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, branch: 19, structural_boundaries: 15, import: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_print/rules/print_call.rs` (RUST) | Magnitude: 29.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 79, indent_spaces: 50, structural_boundaries: 22, branch: 8
- `ruff-0.15.9/crates/ruff_server/src/session/index/ruff_settings.rs` (RUST) | Magnitude: 202.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 435, structural_boundaries: 77, safety: 66, branch: 53
- `ruff-0.15.9/crates/ruff/tests/cli/main.rs` (RUST) | Magnitude: 59.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 70, indent_spaces: 62, structural_boundaries: 26, generics: 13

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
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/test_rules.rs` (RUST) | Magnitude: 93.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 211, indent_spaces: 158, structural_boundaries: 52, decorators: 39
- `ruff-0.15.9/crates/ty_module_resolver/src/module.rs` (RUST) | Magnitude: 192.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 318, structural_boundaries: 57, api: 44, branch: 41
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/redundant_numeric_union.rs` (RUST) | Magnitude: 63.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, doc: 62, structural_boundaries: 36, branch: 26
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` (RUST) | Magnitude: 31.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 17, args: 9, doc: 9
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/unnecessary_regular_expression.rs` (RUST) | Magnitude: 174.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 288, safety: 78, branch: 69, structural_boundaries: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ruff-0.15.9/crates/ruff_python_parser/resources/valid/statement/ambiguous_lpar_with_items.py` (PYTHON) | Magnitude: 70.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: branch: 77, state_mutation: 48, structural_boundaries: 32, comprehensions: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/rules/unused_import.rs` (RUST) | Magnitude: 308.06 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 383, doc: 238, structural_boundaries: 100, branch: 78
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/needless_bool.rs` (RUST) | Magnitude: 96.92 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
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
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/quoted_annotation_in_stub.rs` (RUST) | Magnitude: 9.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 12, structural_boundaries: 8, import: 4
- `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST) | Magnitude: 948.9 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1132, doc: 463, structural_boundaries: 213, branch: 155
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_type_checking/rules/type_alias_quotes.rs` (RUST) | Magnitude: 12.78 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 110, indent_spaces: 79, structural_boundaries: 29, branch: 14
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_todos/rules/todos.rs` (RUST) | Magnitude: 47.58 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 140, indent_spaces: 71, planned_debt: 49, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ruff-0.15.9/crates/ruff_linter/src/rules/isort/block.rs` (RUST) | Magnitude: 117.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 226, branch: 38, generics: 35, structural_boundaries: 31
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/bad_string_format_character.rs` (RUST) | Magnitude: 37.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 18, doc: 17, branch: 13
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_gettext/mod.rs` (RUST) | Magnitude: 42.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 28, import: 12, branch: 11
- `ruff-0.15.9/crates/ruff_python_formatter/src/other/except_handler_except_handler.rs` (RUST) | Magnitude: 40.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 22, branch: 12, safety: 9
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/rdjson.rs` (RUST) | Magnitude: 51.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 50, generics: 44, args: 18

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

- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 6051.626** (Blast Radius: 227.321 * Doc Risk: 26.6215%)
- `ruff-0.15.9/crates/ruff_python_semantic/src/analyze/visibility.rs` -> **Severity: 154.239** (Blast Radius: 1.593 * Doc Risk: 96.8232%)
- `ruff-0.15.9/crates/ruff_linter/src/fs.rs` -> **Severity: 150.715** (Blast Radius: 1.706 * Doc Risk: 88.3438%)
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` -> **Severity: 135.16** (Blast Radius: 4.091 * Doc Risk: 33.0383%)
- `ruff-0.15.9/crates/ruff_linter/src/settings/flags.rs` -> **Severity: 108.104** (Blast Radius: 1.366 * Doc Risk: 79.1391%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
