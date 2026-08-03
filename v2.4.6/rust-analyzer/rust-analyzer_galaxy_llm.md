# ARCHITECTURAL_BRIEF: rust-analyzer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/rust-analyzer` |
| **Timestamp** | `2026-08-03T19:46:57.778492+00:00` |
| **Scan Duration** | `6.96s` |
| **Git Branch** | `master` |
| **Git Commit** | `9767050b2db436f5a770c5f91a548c88fd91ec71` |
| **Git Remote** | `https://github.com/rust-lang/rust-analyzer.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1244 malicious artifacts.

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
| Total Artifacts | 2262 |
| Analyzed Artifacts (Scanned) | 1374 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 888 |
| Total LOC | 400685 |
| Volatility Index | 0.011 |
| % Scanned of codebase = | 60.7% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7499 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3768 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7103 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 42 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1220 | 394709 | 88.8% |
| PLAINTEXT | 96 | 0 | 7.0% |
| TYPESCRIPT | 23 | 4531 | 1.7% |
| HTML | 15 | 924 | 1.1% |
| MARKDOWN | 10 | 0 | 0.7% |
| JSON | 9 | 432 | 0.7% |
| PYTHON | 1 | 89 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.392`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 680 | 49.5% |
| file_cluster_16 | 194 | 14.1% |
| file_cluster_0 | 184 | 13.4% |
| file_cluster_13 | 137 | 10.0% |
| file_cluster_17 | 42 | 3.1% |
| file_cluster_4 | 21 | 1.5% |
| file_cluster_11 | 7 | 0.5% |
| file_cluster_9 | 2 | 0.1% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 106 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 888*

**Composition by Extension & Reason:**
- `.rast`: 507x Excluded (Unsupported Extension: '.rast')
- `.rs`: 193x Excluded: Neighborhood Micro-Mass Limit Exceeded, 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.toml`: 48x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Embedded Array/Matrix Payload: 8237 commas in 561 LOC)
- `.html`: 4x Excluded (Saturation: Line 53 exceeds 500 chars), 2x Excluded (Saturation: Line 54 exceeds 500 chars), 2x Excluded (Saturation: Line 44 exceeds 500 chars)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6421 LOC), 1x Excluded (Massive Static Asset Blob: 12817 LOC)
- `.yaml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ungram`: 1x Excluded (Unsupported Extension: '.ungram'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 11.6 | 7.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 25.6 | 24.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 44.8 | 34.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 38.0 | 2.6 | 80.0 |
| API Exposure | 0.0 | 15.1 | 2.8 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 32.4 | 15.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 82.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 14.1 | 2.2 | 0.3 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 15.4 | 4.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.4 | 39.4 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 59.2 | 98.1 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editors/code/src/bootstrap.ts` (Hits: 32)
- `crates/ide-db/src/imports/insert_use/tests.rs` (Hits: 24)
- `crates/project-model/src/lib.rs` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast.rs** (`crates/syntax/src/ast.rs`) — 83 inbound connections
2. **make.rs** (`crates/syntax/src/ast/make.rs`) — 39 inbound connections
3. **iter.rs** (`crates/tt/src/iter.rs`) — 20 inbound connections
4. **lsp_ext.ts** (`editors/code/src/lsp_ext.ts`) — 18 inbound connections
5. **ted.rs** (`crates/syntax/src/ted.rs`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/hir/src/lib.rs`) — 197 outbound dependencies
2. **interner.rs** (`crates/hir-ty/src/next_solver/interner.rs`) — 159 outbound dependencies
3. **lib.rs** (`crates/ide/src/lib.rs`) — 157 outbound dependencies
4. **lower.rs** (`crates/hir-ty/src/lower.rs`) — 139 outbound dependencies
5. **semantics.rs** (`crates/hir/src/semantics.rs`) — 138 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `recursive_vars` (@ `crates/hir-ty/src/tests/regression.rs`) -> Impact: **7490.2** | LOC: 68
- `expand` (@ `crates/ide-completion/src/context/analysis.rs`) -> Impact: **4717.4** | LOC: 1109
- `replace_if_let_with_match` (@ `crates/ide-assists/src/handlers/replace_if_let_with_match.rs`) -> Impact: **3748.0** | LOC: 2214
  * *Intent:* // Assist: replace_if_let_with_match // // Replaces a `if let` expression with a `match` expression. // // ``` // enum Action { Move { distance: u32 }...
- `wrap_return_type` (@ `crates/ide-assists/src/handlers/wrap_return_type.rs`) -> Impact: **3650.3** | LOC: 2442
  * *Intent:* // Assist: wrap_return_type_in_option // // Wrap the function's return type into Option. // // ``` // # //- minicore: option // fn foo() -> i32$0 { 42...
- `name_like` (@ `crates/ide/src/syntax_highlighting/highlight.rs`) -> Impact: **3138.4** | LOC: 788
- `diagnostics` (@ `crates/hir/src/lib.rs`) -> Impact: **2708.8** | LOC: 1365
- `exec_intrinsic` (@ `crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **2330.2** | LOC: 783
- `delegate` (@ `crates/ide-assists/src/handlers/generate_delegate_trait.rs`) -> Impact: **2276.1** | LOC: 1696
- `merge_text_and_snippet_edits` (@ `crates/rust-analyzer/src/lsp/to_proto.rs`) -> Impact: **1836.3** | LOC: 1405
- `lower_expr_to_place_without_adjust` (@ `crates/hir-ty/src/mir/lower.rs`) -> Impact: **1654.8** | LOC: 1204

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `next_cfg_expr_from_ast` (@ `crates/cfg/src/cfg_expr.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `crates/cfg/src/cfg_expr.rs`) -> **O(2^N) [Recursive]**
- `remove_indent` (@ `crates/hir-def/src/attrs.rs`) -> **O(2^N) [Recursive]**
- `collect_pat` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `maybe_collect_expr` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `maybe_collect_expr_as_pat` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `lower_type_ref` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `lower_generic_args` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `collect_macro_as_stmt` (@ `crates/hir-def/src/expr_store/lower.rs`) -> **O(2^N) [Recursive]**
- `print_expr_in` (@ `crates/hir-def/src/expr_store/pretty.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `hints` (@ `crates/ide/src/inlay_hints/adjustment.rs`) -> DB Complexity: **87**
- `lex_format_specifiers` (@ `crates/ide-db/src/syntax_helpers/format_string.rs`) -> DB Complexity: **71**
  * *Intent:* // FIXME: Remove this, we can use rustc_format_parse instead
- `configureLanguage` (@ `editors/code/src/config.ts`) -> DB Complexity: **67**
  * *Intent:* /** * Sets up additional language configuration that's impossible to do via a * separate language-configuration.json file. See [1] for more informatio...
- `convert_closure_to_fn` (@ `crates/ide-assists/src/handlers/convert_closure_to_fn.rs`) -> DB Complexity: **66**
  * *Intent:* // Assist: convert_closure_to_fn // // This converts a closure to a freestanding function, changing all captures to parameters. // // ``` // # //- min...
- `locals_defined_in_body` (@ `crates/ide-assists/src/handlers/extract_function.rs`) -> DB Complexity: **66**
- `lower_expr_to_place_without_adjust` (@ `crates/hir-ty/src/mir/lower.rs`) -> DB Complexity: **55**
- `remove_indent` (@ `crates/hir-def/src/attrs.rs`) -> DB Complexity: **54**
- `complete_postfix` (@ `crates/ide-completion/src/completions/postfix.rs`) -> DB Complexity: **54**
- `extern_prelude_symbols` (@ `crates/ide-db/src/symbol_index.rs`) -> DB Complexity: **49**
- `wrap_return_type` (@ `crates/ide-assists/src/handlers/wrap_return_type.rs`) -> DB Complexity: **45**
  * *Intent:* // Assist: wrap_return_type_in_option // // Wrap the function's return type into Option. // // ``` // # //- minicore: option // fn foo() -> i32$0 { 42...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/ide-assists/src/handlers` | 134 | 71808.18 | 14.04% | 70.76% |
| `crates/ide/src` | 43 | 21503.76 | 10.47% | 52.69% |
| `crates/hir-ty/src/tests` | 14 | 17493.78 | 10.43% | 0.0% |
| `crates/hir/src` | 11 | 15058.18 | 13.06% | 61.24% |
| `crates/hir-ty/src` | 29 | 12951.4 | 10.69% | 46.07% |
| `crates/hir-def/src` | 20 | 12400.32 | 11.68% | 72.87% |
| `crates/hir-ty/src/mir` | 5 | 10316.8 | 23.55% | 30.78% |
| `crates/ide-diagnostics/src/handlers` | 52 | 9194.62 | 10.98% | 87.54% |
| `crates/ide-db/src` | 23 | 8954.32 | 10.38% | 71.33% |
| `crates/hir-ty/src/next_solver` | 21 | 8736.26 | 12.7% | 77.63% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/base-db/src/target.rs` -> **100.0%** Exposure
- `crates/hir-def/src/dyn_map.rs` -> **100.0%** Exposure
- `crates/hir-def/src/lib.rs` -> **100.0%** Exposure
- `crates/hir-def/src/macro_expansion_tests/builtin_fn_macro.rs` -> **100.0%** Exposure
- `crates/hir-def/src/macro_expansion_tests/mbe/tt_conversion.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/ide-assists/src/handlers/remove_mut.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/gen_trait_fn_body.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/ref_field_expr.rs` -> **100.0%** Exposure
- `crates/ide-db/src/syntax_helpers/format_string.rs` -> **100.0%** Exposure
- `crates/ide/src/inlay_hints/binding_mode.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/ide/src/hover/tests.rs` -> **236** Orphaned Functions | **2** Duplicates
- `crates/hir-ty/src/tests/traits.rs` -> **110** Orphaned Functions | **59** Duplicates
- `crates/hir-ty/src/tests/simple.rs` -> **32** Orphaned Functions | **121** Duplicates
- `crates/hir-ty/src/tests/regression.rs` -> **35** Orphaned Functions | **112** Duplicates
- `crates/ide-assists/src/handlers/extract_function.rs` -> **100** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/hir-ty/src/tests/regression.rs`** -> AI Confidence: **99.48%**
2. **`crates/ide-diagnostics/src/tests/overly_long_real_world_cases.rs`** -> AI Confidence: **99.48%**
3. **`crates/rust-analyzer/src/lsp/capabilities.rs`** -> AI Confidence: **99.48%**
4. **`crates/ide-assists/src/handlers/merge_nested_if.rs`** -> AI Confidence: **99.39%**
5. **`crates/ide-assists/src/handlers/move_guard.rs`** -> AI Confidence: **99.39%**
6. **`crates/ide-diagnostics/src/handlers/missing_match_arms.rs`** -> AI Confidence: **99.39%**
7. **`crates/ide-assists/src/handlers/add_label_to_loop.rs`** -> AI Confidence: **99.35%**
8. **`crates/hir-expand/src/inert_attr_macro.rs`** -> AI Confidence: **99.32%**
9. **`crates/cfg/src/cfg_expr.rs`** -> AI Confidence: **99.31%**
10. **`crates/cfg/src/dnf.rs`** -> AI Confidence: **99.31%**
11. **`crates/cfg/src/lib.rs`** -> AI Confidence: **99.31%**
12. **`crates/hir-def/src/expr_store/lower/asm.rs`** -> AI Confidence: **99.31%**
13. **`crates/hir-def/src/expr_store/lower/path.rs`** -> AI Confidence: **99.31%**
14. **`crates/hir-def/src/expr_store/path.rs`** -> AI Confidence: **99.31%**
15. **`crates/hir-def/src/expr_store/pretty.rs`** -> AI Confidence: **99.31%**
16. **`crates/hir-def/src/nameres/proc_macro.rs`** -> AI Confidence: **99.31%**
17. **`crates/hir-expand/src/fixup.rs`** -> AI Confidence: **99.31%**
18. **`crates/hir-ty/src/infer/op.rs`** -> AI Confidence: **99.31%**
19. **`crates/hir-ty/src/layout/target.rs`** -> AI Confidence: **99.31%**
20. **`crates/hir-ty/src/lib.rs`** -> AI Confidence: **99.31%**
21. **`crates/hir-ty/src/mir/eval.rs`** -> AI Confidence: **99.31%**
22. **`crates/hir-ty/src/mir/eval/shim.rs`** -> AI Confidence: **99.31%**
23. **`crates/hir-ty/src/mir/lower/pattern_matching.rs`** -> AI Confidence: **99.31%**
24. **`crates/hir-ty/src/mir/monomorphization.rs`** -> AI Confidence: **99.31%**
25. **`crates/hir-ty/src/next_solver/infer/relate/generalize.rs`** -> AI Confidence: **99.31%**
26. **`crates/hir-ty/src/next_solver/infer/resolve.rs`** -> AI Confidence: **99.31%**
27. **`crates/hir-ty/src/next_solver/infer/snapshot/fudge.rs`** -> AI Confidence: **99.31%**
28. **`crates/hir-ty/src/next_solver/solver.rs`** -> AI Confidence: **99.31%**
29. **`crates/hir-ty/src/next_solver/ty.rs`** -> AI Confidence: **99.31%**
30. **`crates/hir-ty/src/representability.rs`** -> AI Confidence: **99.31%**
31. **`crates/hir-ty/src/tests/patterns.rs`** -> AI Confidence: **99.31%**
32. **`crates/hir/src/display.rs`** -> AI Confidence: **99.31%**
33. **`crates/hir/src/from_id.rs`** -> AI Confidence: **99.31%**
34. **`crates/hir/src/source_analyzer.rs`** -> AI Confidence: **99.31%**
35. **`crates/ide-assists/src/handlers/add_return_type.rs`** -> AI Confidence: **99.31%**
36. **`crates/ide-assists/src/handlers/apply_demorgan.rs`** -> AI Confidence: **99.31%**
37. **`crates/ide-assists/src/handlers/convert_bool_then.rs`** -> AI Confidence: **99.31%**
38. **`crates/ide-assists/src/handlers/convert_let_else_to_match.rs`** -> AI Confidence: **99.31%**
39. **`crates/ide-assists/src/handlers/convert_range_for_to_while.rs`** -> AI Confidence: **99.31%**
40. **`crates/ide-assists/src/handlers/convert_to_guarded_return.rs`** -> AI Confidence: **99.31%**
41. **`crates/ide-assists/src/handlers/convert_two_arm_bool_match_to_matches_macro.rs`** -> AI Confidence: **99.31%**
42. **`crates/ide-assists/src/handlers/convert_while_to_loop.rs`** -> AI Confidence: **99.31%**
43. **`crates/ide-assists/src/handlers/extract_variable.rs`** -> AI Confidence: **99.31%**
44. **`crates/ide-assists/src/handlers/inline_const_as_literal.rs`** -> AI Confidence: **99.31%**
45. **`crates/ide-assists/src/handlers/invert_if.rs`** -> AI Confidence: **99.31%**
46. **`crates/ide-assists/src/handlers/pull_assignment_up.rs`** -> AI Confidence: **99.31%**
47. **`crates/ide-assists/src/handlers/remove_else_branches.rs`** -> AI Confidence: **99.31%**
48. **`crates/ide-assists/src/handlers/remove_parentheses.rs`** -> AI Confidence: **99.31%**
49. **`crates/ide-assists/src/handlers/replace_if_let_with_match.rs`** -> AI Confidence: **99.31%**
50. **`crates/ide-assists/src/handlers/toggle_macro_delimiter.rs`** -> AI Confidence: **99.31%**
51. **`crates/ide-assists/src/handlers/unwrap_block.rs`** -> AI Confidence: **99.31%**
52. **`crates/ide-completion/src/completions/attribute/lint.rs`** -> AI Confidence: **99.31%**
53. **`crates/ide-completion/src/completions/flyimport.rs`** -> AI Confidence: **99.31%**
54. **`crates/ide-completion/src/completions/keyword.rs`** -> AI Confidence: **99.31%**
55. **`crates/ide-completion/src/completions/lifetime.rs`** -> AI Confidence: **99.31%**
56. **`crates/ide-completion/src/completions/pattern.rs`** -> AI Confidence: **99.31%**
57. **`crates/ide-completion/src/context/analysis.rs`** -> AI Confidence: **99.31%**
58. **`crates/ide-db/src/defs.rs`** -> AI Confidence: **99.31%**
59. **`crates/ide-db/src/famous_defs.rs`** -> AI Confidence: **99.31%**
60. **`crates/ide-diagnostics/src/handlers/remove_unnecessary_else.rs`** -> AI Confidence: **99.31%**
61. **`crates/ide-ssr/src/matching.rs`** -> AI Confidence: **99.31%**
62. **`crates/ide/src/folding_ranges.rs`** -> AI Confidence: **99.31%**
63. **`crates/ide/src/inlay_hints/closing_brace.rs`** -> AI Confidence: **99.31%**
64. **`crates/ide/src/syntax_highlighting.rs`** -> AI Confidence: **99.31%**
65. **`crates/ide/src/syntax_highlighting/highlight.rs`** -> AI Confidence: **99.31%**
66. **`crates/parser/src/grammar/expressions.rs`** -> AI Confidence: **99.31%**
67. **`crates/parser/src/grammar/items.rs`** -> AI Confidence: **99.31%**
68. **`crates/parser/src/lexed_str.rs`** -> AI Confidence: **99.31%**
69. **`crates/proc-macro-srv/src/token_stream.rs`** -> AI Confidence: **99.31%**
70. **`crates/project-model/src/workspace.rs`** -> AI Confidence: **99.31%**
71. **`crates/rust-analyzer/src/bin/main.rs`** -> AI Confidence: **99.31%**
72. **`crates/syntax/src/ast/edit_in_place.rs`** -> AI Confidence: **99.31%**
73. **`crates/syntax/src/ast/expr_ext.rs`** -> AI Confidence: **99.31%**
74. **`crates/syntax/src/ast/prec.rs`** -> AI Confidence: **99.31%**
75. **`xtask/src/install.rs`** -> AI Confidence: **99.31%**
76. **`xtask/src/pgo.rs`** -> AI Confidence: **99.31%**
77. **`xtask/src/publish/notes.rs`** -> AI Confidence: **99.31%**
78. **`editors/code/src/client.ts`** -> AI Confidence: **99.31%**
79. **`editors/code/src/ctx.ts`** -> AI Confidence: **99.31%**
80. **`editors/code/src/debug.ts`** -> AI Confidence: **99.31%**
81. **`editors/code/src/run.ts`** -> AI Confidence: **99.31%**
82. **`crates/hir-def/src/macro_expansion_tests/mbe/meta_syntax.rs`** -> AI Confidence: **99.29%**
83. **`crates/ide-diagnostics/src/handlers/break_outside_of_loop.rs`** -> AI Confidence: **99.29%**
84. **`crates/parser/test_data/lexer/ok/symbols.rs`** -> AI Confidence: **99.29%**
85. **`crates/parser/test_data/parser/err/0008_item_block_recovery.rs`** -> AI Confidence: **99.29%**
86. **`crates/parser/test_data/parser/err/0010_unsafe_lambda_block.rs`** -> AI Confidence: **99.29%**
87. **`crates/parser/test_data/parser/err/0032_match_arms_inner_attrs.rs`** -> AI Confidence: **99.29%**
88. **`crates/parser/test_data/parser/err/0033_match_arms_outer_attrs.rs`** -> AI Confidence: **99.29%**
89. **`crates/parser/test_data/parser/inline/err/match_arms_recovery.rs`** -> AI Confidence: **99.29%**
90. **`crates/parser/test_data/parser/inline/ok/break_ambiguity.rs`** -> AI Confidence: **99.29%**
91. **`crates/parser/test_data/parser/inline/ok/break_expr.rs`** -> AI Confidence: **99.29%**
92. **`crates/parser/test_data/parser/inline/ok/closure_binder.rs`** -> AI Confidence: **99.29%**
93. **`crates/parser/test_data/parser/inline/ok/closure_body_underscore_assignment.rs`** -> AI Confidence: **99.29%**
94. **`crates/parser/test_data/parser/inline/ok/closure_range_method_call.rs`** -> AI Confidence: **99.29%**
95. **`crates/parser/test_data/parser/inline/ok/continue_expr.rs`** -> AI Confidence: **99.29%**
96. **`crates/parser/test_data/parser/inline/ok/exclusive_range_pat.rs`** -> AI Confidence: **99.29%**
97. **`crates/parser/test_data/parser/inline/ok/for_range_from.rs`** -> AI Confidence: **99.29%**
98. **`crates/parser/test_data/parser/inline/ok/if_expr.rs`** -> AI Confidence: **99.29%**
99. **`crates/parser/test_data/parser/inline/ok/label.rs`** -> AI Confidence: **99.29%**
100. **`crates/parser/test_data/parser/inline/ok/literal_pattern.rs`** -> AI Confidence: **99.29%**
101. **`crates/parser/test_data/parser/inline/ok/match_arm.rs`** -> AI Confidence: **99.29%**
102. **`crates/parser/test_data/parser/inline/ok/match_arms_commas.rs`** -> AI Confidence: **99.29%**
103. **`crates/parser/test_data/parser/inline/ok/match_arms_inner_attribute.rs`** -> AI Confidence: **99.29%**
104. **`crates/parser/test_data/parser/inline/ok/match_arms_outer_attributes.rs`** -> AI Confidence: **99.29%**
105. **`crates/parser/test_data/parser/inline/ok/match_expr.rs`** -> AI Confidence: **99.29%**
106. **`crates/parser/test_data/parser/inline/ok/no_semi_after_block.rs`** -> AI Confidence: **99.29%**
107. **`crates/parser/test_data/parser/inline/ok/or_pattern.rs`** -> AI Confidence: **99.29%**
108. **`crates/parser/test_data/parser/inline/ok/range_pat.rs`** -> AI Confidence: **99.29%**
109. **`crates/parser/test_data/parser/inline/ok/stmt_postfix_expr_ambiguity.rs`** -> AI Confidence: **99.29%**
110. **`crates/parser/test_data/parser/ok/0033_label_break.rs`** -> AI Confidence: **99.29%**
111. **`crates/parser/test_data/parser/ok/0052_for_range_block.rs`** -> AI Confidence: **99.29%**
112. **`crates/parser/test_data/parser/ok/0056_neq_in_type.rs`** -> AI Confidence: **99.29%**
113. **`crates/parser/test_data/parser/ok/0057_loop_in_call.rs`** -> AI Confidence: **99.29%**
114. **`crates/parser/test_data/parser/ok/0059_loops_in_parens.rs`** -> AI Confidence: **99.29%**
115. **`crates/parser/test_data/parser/ok/0071_stmt_attr_placement.rs`** -> AI Confidence: **99.29%**
116. **`crates/syntax/test_data/parser/fuzz-failures/0003.rs`** -> AI Confidence: **99.29%**
117. **`crates/ide/src/highlight_related.rs`** -> AI Confidence: **99.25%**
118. **`crates/rust-analyzer/src/lsp/from_proto.rs`** -> AI Confidence: **99.25%**
119. **`crates/rust-analyzer/src/reload.rs`** -> AI Confidence: **99.25%**
120. **`crates/syntax-bridge/src/prettify_macro_expansion.rs`** -> AI Confidence: **99.25%**
121. **`crates/syntax/src/validation.rs`** -> AI Confidence: **99.25%**
122. **`crates/hir-def/src/lang_item.rs`** -> AI Confidence: **99.24%**
123. **`crates/hir-def/src/lib.rs`** -> AI Confidence: **99.24%**
124. **`crates/hir-def/src/nameres/path_resolution.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `editors/code/src/bootstrap.ts` -> **100.0%** Exposure
- `editors/code/src/client.ts` -> **100.0%** Exposure
- `editors/code/src/commands.ts` -> **100.0%** Exposure
- `editors/code/src/config.ts` -> **100.0%** Exposure
- `editors/code/src/ctx.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `crates/hir-ty/src/utils.rs` -> **100.0%** Exposure
- `crates/ide/src/static_index.rs` -> **100.0%** Exposure
- `editors/code/src/util.ts` -> **100.0%** Exposure
- `crates/hir-def/src/import_map.rs` -> **99.8769%** Exposure
- `crates/cfg/src/cfg_expr.rs` -> **99.5158%** Exposure
### Raw Memory Manipulation
- `crates/paths/src/lib.rs` -> **0.0148%** Exposure
- `crates/rust-analyzer/src/config/patch_old_style.rs` -> **0.0143%** Exposure
- `lib/la-arena/src/lib.rs` -> **0.0138%** Exposure
- `lib/smol_str/src/lib.rs` -> **0.0009%** Exposure
- `lib/text-size/src/range.rs` -> **0.0009%** Exposure
### Algorithmic DoS Exposure
- `crates/base-db/src/change.rs` -> **100.0%** Exposure
- `crates/base-db/src/input.rs` -> **100.0%** Exposure
- `crates/base-db/src/lib.rs` -> **100.0%** Exposure
- `crates/cfg/src/cfg_expr.rs` -> **100.0%** Exposure
- `crates/cfg/src/lib.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19184` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editors/code/src/dependencies_provider.ts` (TYPESCRIPT) -> Cumulative Risk: **965.09**
- **Archetype:** `file_cluster_4` (Distance: 12.36 IQR)
- **Magnitude:** 21.33 | **LOC:** 155 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getChildren` (Impact: 37.6), `getRootDependencies` (Impact: 15.8), `constructor` (Impact: 15.5)

### 2. `editors/code/src/diagnostics.ts` (TYPESCRIPT) -> Cumulative Risk: **953.65**
- **Archetype:** `file_cluster_4` (Distance: 11.469 IQR)
- **Magnitude:** 18.49 | **LOC:** 213 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_getDecorations` (Impact: 28.1), `getRenderedDiagnostic` (Impact: 24.3), `provideDecorations` (Impact: 16.5)

### 3. `editors/code/src/util.ts` (TYPESCRIPT) -> Cumulative Risk: **904.11**
- **Archetype:** `file_cluster_4` (Distance: 12.806 IQR)
- **Magnitude:** 46.79 | **LOC:** 356 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `spawnAsync` (Impact: 41.4), `show` (Impact: 35.0), `findRustToolchainFiles` (Impact: 31.4)

### 4. `editors/code/src/ctx.ts` (TYPESCRIPT) -> Cumulative Risk: **901.88**
- **Archetype:** `file_cluster_4` (Distance: 13.544 IQR)
- **Magnitude:** 118.72 | **LOC:** 647 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `prepareSyntaxTreeView` (Impact: 97.7), `updateStatusBarItem` (Impact: 91.6), `getOrCreateClient` (Impact: 81.5)

### 5. `editors/code/src/syntax_tree_provider.ts` (TYPESCRIPT) -> Cumulative Risk: **844.96**
- **Archetype:** `file_cluster_8` (Distance: 11.218 IQR)
- **Magnitude:** 40.47 | **LOC:** 386 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getElementByRange` (Impact: 74.5), `refresh` (Impact: 70.1), `getRawChildren` (Impact: 46.0)

### 6. `editors/code/src/config.ts` (TYPESCRIPT) -> Cumulative Risk: **843.97**
- **Archetype:** `file_cluster_4` (Distance: 12.551 IQR)
- **Magnitude:** 82.93 | **LOC:** 614 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `configureLanguage` (Impact: 525.7), `onDidChangeConfiguration` (Impact: 35.4), `addExtensionConfiguration` (Impact: 24.6)

### 7. `crates/intern/src/gc.rs` (RUST) -> Cumulative Risk: **825.33**
- **Archetype:** `file_cluster_16` (Distance: 12.168 IQR)
- **Magnitude:** 211.2 | **LOC:** 336 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sweep` (Impact: 36.0), `sweep_storage` (Impact: 22.0), `collect` (Impact: 21.1)

### 8. `editors/code/src/bootstrap.ts` (TYPESCRIPT) -> Cumulative Risk: **809.57**
- **Archetype:** `file_cluster_4` (Distance: 10.194 IQR)
- **Magnitude:** 59.1 | **LOC:** 302 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getServer` (Impact: 152.8), `patchelf` (Impact: 128.2), `raVersionResolver` (Impact: 40.8)

### 9. `crates/proc-macro-srv-cli/src/main_loop.rs` (RUST) -> Cumulative Risk: **808.02**
- **Archetype:** `file_cluster_4` (Distance: 12.512 IQR)
- **Magnitude:** 529.7 | **LOC:** 565 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 83.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run_new` (Impact: 94.0), `run_old` (Impact: 63.2), `roundtrip` (Impact: 43.2)

### 10. `crates/stdx/src/lib.rs` (RUST) -> Cumulative Risk: **803.41**
- **Archetype:** `file_cluster_0` (Distance: 11.524 IQR)
- **Magnitude:** 458.62 | **LOC:** 463 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9892%)
- **Heaviest Functions:** `to_camel_case` (Impact: 80.3), `to_snake_case` (Impact: 57.0), `iter_eq_by` (Impact: 25.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/hir-ty/src/tests/regression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.742 IQR)
- **Top Global Matches:** file_cluster_16: 12.742, file_cluster_0: 12.887, file_cluster_8: 12.93
- **Magnitude:** 8526.78 | **LOC:** 2859 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 58.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (37.5368%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recursive_vars` (Impact: 7490.2 | O(N^4) | DB: 1)
  * `extra_compiler_flags` (Impact: 31.9 | O(N^5))
  * `foo` (Impact: 31.7 | O(2^N))
  * `my_clone` (Impact: 21.4 | O(2^N))
  * `encode` (Impact: 20.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2774`, `structural_boundaries: 505`, `args: 307`, `func_start: 298`, `class_start: 155`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 78`, `fragile_debt: 4`, `duplicate_logic: 112`, `orphaned_logic: 35`
* *Architecture:* `api: 83`, `concurrency: 60`, `import: 18`
* *Defense:* `safety: 69`, `test: 134`, `sync_locks: 10`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, expect_test::expect, core::ops::ControlFlow, super::check_infer, IndexMut, bindings::*, core::ops::Deref, core::marker::PhantomData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.083 IQR)
- **Top Global Matches:** file_cluster_8: 14.083, file_cluster_16: 14.25, file_cluster_0: 14.305
- **Magnitude:** 6598.72 | **LOC:** 3193 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (26.7432%), Tech Debt (55.3031%)
**Top Internal Functions/Classes:**
  * `eval_rvalue` (Impact: 1054.0 | O(N^6) | DB: 11)
  * `pretty_print` (Impact: 679.1 | O(2^N) | DB: 2)
  * `patch_addresses` (Impact: 625.9 | O(2^N) | DB: 1)
  * `create_memory_map` (Impact: 325.8 | O(N^6) | DB: 5)
  * `interpret_mir` (Impact: 305.5 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 611`, `structural_boundaries: 678`, `args: 179`, `func_start: 90`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 256`, `fragile_debt: 12`, `duplicate_logic: 12`, `orphaned_logic: 7`
* *Architecture:* `api: 14`, `import: 28`
* *Defense:* `safety: 531`, `doc: 22`, `test: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hir_expand::InFile, ComplexMemoryMap, ProjectionStore, Ty, FunctionId, try_const_usize, FxHashSet, base_db::Crate...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/context/analysis.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.851 IQR)
- **Top Global Matches:** file_cluster_17: 13.851, file_cluster_8: 13.895, file_cluster_0: 14.161
- **Magnitude:** 5270.42 | **LOC:** 2116 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (13.7493%), Tech Debt (11.5663%)
**Top Internal Functions/Classes:**
  * `expand` (Impact: 4717.4 | O(2^N) | DB: 13)
  * `pattern_context_for` (Impact: 134.6 | O(N^6) | DB: 2)
    * *Intent:* // A record expression in this position is usually a result of parsing recovery, so check that
  * `is_in_token_of_for_loop` (Impact: 41.0 | O(N^4))
  * `is_in_breakable` (Impact: 36.9 | O(N^5))
  * `has_in_newline_expr_first` (Impact: 28.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 395`, `args: 216`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 54`, `dead_code: 10`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 398`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasGenericArgs, LifetimeKind, SyntaxToken, TypeLocation, syntax_helpers::node_ext::find_loops, crate::
    completions::postfix::is_in_condition, T, NameRefKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.282 IQR)
- **Top Global Matches:** file_cluster_16: 14.282, file_cluster_8: 14.341, file_cluster_0: 14.447
- **Magnitude:** 4602.9 | **LOC:** 7283 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 44.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (7.9578%), Tech Debt (41.4829%)
**Top Internal Functions/Classes:**
  * `diagnostics` (Impact: 2708.8 | O(2^N) | DB: 10)
  * `ty` (Impact: 763.7 | O(N^6) | DB: 11)
  * `resolve_absolute_path` (Impact: 41.3 | O(N^6) | DB: 4)
    * *Intent:* // For non-phantom_data adts we check variants/fields as well as generic parameters
  * `query_external_importables` (Impact: 27.6 | O(2^N))
  * `krate` (Impact: 21.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 542`, `structural_boundaries: 880`, `args: 402`, `func_start: 468`, `class_start: 71`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 164`, `dead_code: 5`, `fragile_debt: 33`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 489`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 621`, `doc: 181`, `test: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` resolve_doc_path_on, attrs::AttrFlags, TyDefId, hir_ty::next_solver, Ty, FunctionId, GenericArgs, SpanMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval/shim.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.395 IQR)
- **Top Global Matches:** file_cluster_8: 12.395, file_cluster_17: 12.751, file_cluster_13: 12.826
- **Magnitude:** 4536.74 | **LOC:** 1525 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.0137%), Tech Debt (48.6416%)
**Top Internal Functions/Classes:**
  * `exec_intrinsic` (Impact: 2330.2 | O(N^6) | DB: 3)
  * `exec_extern_c` (Impact: 617.1 | O(N^6) | DB: 4)
  * `exec_atomic_intrinsic` (Impact: 428.8 | O(N^5) | DB: 1)
  * `exec_alloc_fn` (Impact: 199.4 | O(N^6) | DB: 1)
  * `exec_lang_item` (Impact: 191.6 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 472`, `args: 72`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 39`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 14`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 228`, `doc: 4`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TyKind, Ty, FunctionId, Ordering, GenericArgs, Result, HasModule, std::cmp::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/extract_function.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.327 IQR)
- **Top Global Matches:** file_cluster_8: 13.327, file_cluster_0: 13.361, file_cluster_17: 13.57
- **Magnitude:** 4375.94 | **LOC:** 6541 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 36.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (13.69%), Tech Debt (67.3336%)
**Top Internal Functions/Classes:**
  * `locals_defined_in_body` (Impact: 1281.9 | O(N^6) | DB: 66)
  * `extract_function` (Impact: 348.4 | O(2^N) | DB: 1)
    * *Intent:* // Assist: extract_function // // Extracts selected statements and comments into new function. // //...
  * `analyze_container` (Impact: 255.7 | O(N^6) | DB: 6)
  * `expr_require_exclusive_access` (Impact: 98.6 | O(2^N))
  * `external_control_flow` (Impact: 90.4 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 1231`, `args: 235`, `func_start: 586`, `class_start: 100`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 343`, `dead_code: 17`, `fragile_debt: 10`, `duplicate_logic: 4`, `orphaned_logic: 100`
* *Architecture:* `api: 13`, `concurrency: 28`, `import: 16`
* *Defense:* `safety: 600`, `doc: 68`, `test: 153`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core::ops::ControlFlow, ReferenceCategory, SyntaxToken, assists::GroupLabel, hir::
    HasSource, imports::insert_use::ImportScope, syntax::
    Edition, SyntaxKind::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/wrap_return_type.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.09 IQR)
- **Top Global Matches:** file_cluster_8: 13.09, file_cluster_0: 13.157, file_cluster_4: 13.429
- **Magnitude:** 3947.26 | **LOC:** 2563 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (16.2992%), Tech Debt (7.8885%)
**Top Internal Functions/Classes:**
  * `wrap_return_type` (Impact: 3650.3 | O(2^N) | DB: 45)
    * *Intent:* // Assist: wrap_return_type_in_option // // Wrap the function's return type into Option. // // ``` /...
  * `already_wrapped` (Impact: 25.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 417`, `args: 278`, `func_start: 236`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 133`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 11`, `concurrency: 80`, `import: 15`
* *Defense:* `safety: 441`, `test: 67`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasGenericArgs, some_module::*, AssistId, famous_defs::FamousDefs, syntax_factory::SyntaxFactory, syntax::
    AstNode, some_module::Result, crate::tests::check_assist_by_label...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/replace_if_let_with_match.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.688 IQR)
- **Top Global Matches:** file_cluster_8: 12.688, file_cluster_0: 12.857, file_cluster_17: 13.182
- **Magnitude:** 3834.34 | **LOC:** 2296 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (8.8463%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `replace_if_let_with_match` (Impact: 3748.0 | O(2^N) | DB: 8)
    * *Intent:* // Assist: replace_if_let_with_match // // Replaces a `if let` expression with a `match` expression....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 256`, `args: 208`, `func_start: 187`, `class_start: 12`
* *Risk/State:* `state_mutation: 22`, `dead_code: 6`
* *Architecture:* `api: 21`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 495`, `doc: 1`, `test: 47`, `immutability_locks: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::iter::successors, crate::
    AssistContext, AssistId, defs::NameClass, syntax_factory::SyntaxFactory, T, syntax::
    AstNode, ide_db::RootDatabase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-def/src/expr_store/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.196 IQR)
- **Top Global Matches:** file_cluster_17: 14.196, file_cluster_8: 14.399, file_cluster_0: 14.508
- **Magnitude:** 3541.42 | **LOC:** 2961 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 40.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (21.1979%), Tech Debt (31.2545%)
**Top Internal Functions/Classes:**
  * `collect_pat` (Impact: 749.5 | O(2^N) | DB: 30)
  * `maybe_collect_expr` (Impact: 725.4 | O(2^N) | DB: 7)
  * `maybe_collect_expr_as_pat` (Impact: 335.7 | O(2^N) | DB: 8)
  * `lower_type_ref` (Impact: 240.8 | O(2^N) | DB: 4)
  * `lower_generic_args` (Impact: 207.1 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 635`, `args: 235`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 285`, `dead_code: 10`, `fragile_debt: 14`, `orphaned_logic: 6`
* *Architecture:* `api: 21`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 445`, `doc: 60`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RecordLitField, HasGenericArgs, attrs::AttrFlags, smallvec::smallvec, RecordSpread, FunctionId, GenericArgs, Item...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/lsp/to_proto.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.464 IQR)
- **Top Global Matches:** file_cluster_8: 12.464, file_cluster_17: 12.834, file_cluster_0: 12.884
- **Magnitude:** 3399.86 | **LOC:** 3091 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 26.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (11.9391%), Tech Debt (15.0924%)
**Top Internal Functions/Classes:**
  * `merge_text_and_snippet_edits` (Impact: 1836.3 | O(2^N) | DB: 32)
  * `completion_item` (Impact: 425.3 | O(N^5) | DB: 9)
  * `semantic_tokens` (Impact: 209.3 | O(2^N) | DB: 4)
  * `inlay_hint` (Impact: 207.9 | O(2^N) | DB: 3)
  * `inlay_hint_label` (Impact: 96.6 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 389`, `args: 140`, `func_start: 79`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 141`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 62`, `import: 15`
* *Defense:* `safety: 358`, `doc: 11`, `test: 22`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.052
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001457
  * `Imports (Out-Degree: 3):` Assist, base64::Engine, ide_db::
    FxHasher, line_index::LineEndings, CompletionItem, source_change::ChangeAnnotationId, mem, ops::Not...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/ide/src/syntax_highlighting/highlight.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.662 IQR)
- **Top Global Matches:** file_cluster_8: 12.662, file_cluster_13: 13.069, file_cluster_16: 13.096
- **Magnitude:** 3381.1 | **LOC:** 891 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (15.4627%), Tech Debt (14.9249%)
**Top Internal Functions/Classes:**
  * `name_like` (Impact: 3138.4 | O(2^N) | DB: 21)
  * `token` (Impact: 166.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 134`, `args: 104`, `func_start: 12`
* *Risk/State:* `state_mutation: 57`, `fragile_debt: 4`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 131`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HlTag, SyntaxToken, HasVisibility, SyntaxKind::self, T, syntax::
    AstNode, NameRefClass, Semantics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/display.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.739 IQR)
- **Top Global Matches:** file_cluster_8: 13.739, file_cluster_16: 13.836, file_cluster_17: 13.911
- **Magnitude:** 3108.06 | **LOC:** 967 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 52.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (45.2229%), Tech Debt (99.9941%)
**Top Internal Functions/Classes:**
  * `write_function` (Impact: 342.1 | O(N^6) | DB: 4)
  * `hir_fmt` (Impact: 309.9 | O(2^N) | DB: 1)
  * `hir_fmt` (Impact: 281.9 | O(2^N) | DB: 2)
  * `write_generic_params_or_args` (Impact: 251.7 | O(N^6) | DB: 4)
  * `write_variants` (Impact: 214.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 214`, `args: 33`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 120`, `fragile_debt: 5`, `duplicate_logic: 25`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 155`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Static, EnumVariant, Const, GenericParam, rustc_type_ir::inherent::IntoKind, item_tree::FieldsShape, Enum, FunctionId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/syntax/src/ast/syntax_factory/constructors.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.705 IQR)
- **Top Global Matches:** file_cluster_17: 14.705, file_cluster_8: 14.749, file_cluster_0: 14.896
- **Magnitude:** 3107.86 | **LOC:** 2107 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 79.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (65.5382%), Tech Debt (8.6936%)
**Top Internal Functions/Classes:**
  * `record_expr_field` (Impact: 163.1 | O(2^N) | DB: 11)
  * `impl_trait` (Impact: 119.2 | O(2^N) | DB: 3)
  * `ty_alias` (Impact: 116.3 | O(2^N) | DB: 3)
  * `item_static` (Impact: 74.0 | O(2^N) | DB: 3)
  * `where_pred` (Impact: 70.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 573`, `args: 130`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 550`, `orphaned_logic: 2`
* *Architecture:* `api: 103`, `import: 4`
* *Defense:* `safety: 274`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HasGenericArgs, crate::
    AstNode, SyntaxToken, HasVisibility, HasTypeBounds, HasAttrs, Param, SyntaxNode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/tests/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.951 IQR)
- **Top Global Matches:** file_cluster_8: 11.951, file_cluster_0: 12.257, file_cluster_13: 12.348
- **Magnitude:** 3087.4 | **LOC:** 3697 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (12.0115%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `else_completion_after_if` (Impact: 1158.0 | O(N^3) | DB: 4)
  * `inside_faulty_format_args_completions_wo` (Impact: 589.8 | O(N^4) | DB: 30)
  * `completes_after_ref_expr` (Impact: 155.7 | O(N^3) | DB: 5)
  * `completes_let_else` (Impact: 100.9 | O(N^3))
  * `in_macro_expr_frag` (Impact: 80.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 872`, `args: 352`, `func_start: 310`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 135`, `fragile_debt: 1`, `orphaned_logic: 29`
* *Architecture:* `api: 22`, `concurrency: 44`, `import: 41`
* *Defense:* `safety: 263`, `doc: 2`, `test: 62`, `immutability_locks: 136`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TEST_CONFIG, check_with_base_items, proc_macros::identity, crate::
    CompletionConfig, completion_list_with_config, std::*, _69latrick::*, non_existent::Unresolved...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/source_analyzer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.788 IQR)
- **Top Global Matches:** file_cluster_8: 13.788, file_cluster_17: 13.801, file_cluster_16: 13.834
- **Magnitude:** 2958.04 | **LOC:** 2014 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 45.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (17.2902%), Tech Debt (85.8853%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 1383.2 | O(N^6) | DB: 9)
  * `resolve_offset_of_field` (Impact: 136.5 | O(N^6) | DB: 7)
  * `resolve_prefix_expr` (Impact: 135.2 | O(N^6))
  * `resolve_record_field` (Impact: 116.2 | O(N^5))
  * `resolve_await_to_poll` (Impact: 103.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 383`, `args: 141`, `func_start: 74`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 60`, `dead_code: 5`, `fragile_debt: 12`, `orphaned_logic: 31`
* *Architecture:* `api: 56`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 355`, `doc: 23`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ty, FunctionId, ValueNs, GenericArgs, crate::
    Adt, path, scope::ExprScopes, LifetimeElisionKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/render.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.933 IQR)
- **Top Global Matches:** file_cluster_17: 13.933, file_cluster_8: 13.945, file_cluster_0: 14.171
- **Magnitude:** 2878.02 | **LOC:** 1432 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 31.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (22.0978%), Tech Debt (12.9973%)
**Top Internal Functions/Classes:**
  * `definition` (Impact: 721.2 | O(N^6) | DB: 11)
  * `literal` (Impact: 518.3 | O(2^N) | DB: 1)
  * `try_expr` (Impact: 462.9 | O(2^N) | DB: 10)
  * `render_memory_layout` (Impact: 215.0 | O(N^4) | DB: 1)
  * `keyword_hints` (Impact: 101.6 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 318`, `args: 127`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 168`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 11`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 312`, `doc: 6`, `test: 8`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` algo, Name, Markup, walk_and_push_ty, SyntaxToken, MethodViolationCode, famous_defs::FamousDefs, T...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/cli/analysis_stats.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.251 IQR)
- **Top Global Matches:** file_cluster_17: 13.251, file_cluster_8: 13.303, file_cluster_13: 13.449
- **Magnitude:** 2780.38 | **LOC:** 1651 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 45.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (34.0666%), Tech Debt (55.7085%)
**Top Internal Functions/Classes:**
  * `run_inference` (Impact: 900.4 | O(N^6) | DB: 12)
  * `run_body_lowering` (Impact: 553.2 | O(N^6) | DB: 2)
  * `run_term_search` (Impact: 437.1 | O(N^6) | DB: 15)
  * `run_mir_lowering` (Impact: 164.1 | O(N^5) | DB: 4)
  * `run` (Impact: 140.4 | O(N^6) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 339`, `args: 103`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 153`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 1`, `import: 18`
* *Defense:* `safety: 130`, `doc: 4`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ops::AddAssign, AnnotationConfig, FxHashSet, GenericArgs, project_model::CargoConfig, BodySourceMap, print_memory_usage, load_workspace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/infer/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.03 IQR)
- **Top Global Matches:** file_cluster_17: 14.03, file_cluster_8: 14.11, file_cluster_0: 14.145
- **Magnitude:** 2665.18 | **LOC:** 2246 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 65.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (18.4355%), Tech Debt (35.7104%)
**Top Internal Functions/Classes:**
  * `infer_expr_coerce_never` (Impact: 1106.2 | O(2^N) | DB: 22)
  * `infer_block` (Impact: 864.7 | O(N^6) | DB: 21)
  * `write_fn_trait_method_resolution` (Impact: 87.0 | O(N^6) | DB: 2)
  * `demand_scrutinee_type` (Impact: 66.0 | O(N^5) | DB: 1)
  * `infer_expr_array` (Impact: 51.9 | O(N^6) | DB: 3)
    * *Intent:* // If this is an input value, we require its type to be fully resolved
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 308`, `args: 99`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 144`, `dead_code: 16`, `fragile_debt: 20`
* *Architecture:* `api: 16`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 245`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` RecordSpread, Ty, GenericArgs, ObligationCause, CoroutineArgsParts, InferTy, mem, TupleId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.26 IQR)
- **Top Global Matches:** file_cluster_8: 14.26, file_cluster_17: 14.336, file_cluster_0: 14.385
- **Magnitude:** 2557.68 | **LOC:** 2341 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 58.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (20.7967%), Tech Debt (28.4454%)
**Top Internal Functions/Classes:**
  * `lower_expr_to_place_without_adjust` (Impact: 1654.8 | O(N^6) | DB: 55)
  * `pretty_print` (Impact: 380.2 | O(2^N) | DB: 1)
    * *Intent:* // Uncomment this to make `DropScopeToken` a drop bomb. Unfortunately we can't do this in release, s...
  * `lower_expr_to_place_with_adjust` (Impact: 151.1 | O(2^N) | DB: 1)
  * `lower_body_to_mir` (Impact: 44.4 | O(N^2) | DB: 1)
  * `mir_body_query` (Impact: 41.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 359`, `args: 80`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 140`, `dead_code: 6`, `fragile_debt: 11`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* `safety: 409`, `doc: 21`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` RecordLitField, ProjectionStore, RecordSpread, Ty, std::fmt::Write, base_db::Crate, ValueNs, GenericArgs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/generate_delegate_trait.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.776 IQR)
- **Top Global Matches:** file_cluster_0: 12.776, file_cluster_16: 12.912, file_cluster_17: 12.959
- **Magnitude:** 2524.74 | **LOC:** 1985 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (11.5057%), Tech Debt (19.2033%)
**Top Internal Functions/Classes:**
  * `delegate` (Impact: 2276.1 | O(2^N) | DB: 22)
  * `new` (Impact: 75.4 | O(N^4) | DB: 1)
    * *Intent:* // } // ``` // -> // ``` // trait SomeTrait { // type T; // fn fn_(arg: u32) -> u32; // fn method_(&...
  * `generate_delegate_trait` (Impact: 32.1 | O(N^3) | DB: 1)
    * *Intent:* // Assist: generate_delegate_trait // // Generate delegate trait implementation for `StructField`s. ...
  * `signature` (Impact: 15.7 | O(N^4) | DB: 1)
  * `trait_` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 449`, `args: 188`, `func_start: 157`, `class_start: 147`
* *Risk/State:* `state_mutation: 67`, `dead_code: 18`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 100`, `doc: 12`, `test: 36`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasGenericArgs, hir::HasVisibility, HasVisibility, FxHashSet, crate::
    assist_context::AssistContext, syntax_factory::SyntaxFactory, syntax::
    AstNode, utils::convert_param_list_to_arg_list...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.588 IQR)
- **Top Global Matches:** file_cluster_8: 10.588, file_cluster_7: 11.146, file_cluster_16: 11.159
- **Magnitude:** 2487.16 | **LOC:** 11407 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 57.9%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.1658%), Tech Debt (78.3722%)
**Top Internal Functions/Classes:**
  * `hover_intra_inner_attr` (Impact: 61.9 | O(N^3))
    * *Intent:* *[`Foo`]*
  * `hover_intra_outer_attr` (Impact: 61.9 | O(N^3))
  * `hover_const_eval` (Impact: 43.2 | O(N^3))
  * `type_alias_without_docs` (Impact: 42.8 | O(N^3))
  * `hover_trait_show_assoc_items` (Impact: 37.5 | O(N^4))
    * *Intent:* *func*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 1023`, `args: 346`, `func_start: 655`, `class_start: 355`
* *Risk/State:* `safety_bypasses: 484`, `state_mutation: 48`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 236`
* *Architecture:* `api: 162`, `concurrency: 16`, `import: 31`
* *Defense:* `safety: 120`, `doc: 157`, `test: 282`, `immutability_locks: 202`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::path::Path, snapbox::Assert, Option::Some, ra_fixture::RaFixtureConfig, string::*, expect_test, core::fmt::Debug, MemoryLayoutHoverRenderKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.582 IQR)
- **Top Global Matches:** file_cluster_0: 13.582, file_cluster_16: 13.602, file_cluster_8: 13.686
- **Magnitude:** 2472.48 | **LOC:** 2681 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 53.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (10.5985%), Tech Debt (90.7131%)
**Top Internal Functions/Classes:**
  * `resolve_type_param_assoc_type_shorthand` (Impact: 572.8 | O(2^N) | DB: 3)
  * `lower_dyn_trait` (Impact: 231.6 | O(N^6) | DB: 10)
    * *Intent:* // Don't lower associated type bindings as the only possible relaxed trait bound // `?Sized` has no ...
  * `generic_predicates` (Impact: 178.0 | O(N^6) | DB: 8)
  * `query` (Impact: 138.5 | O(2^N) | DB: 3)
  * `lower_type_bound` (Impact: 97.7 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 575`, `args: 186`, `func_start: 110`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 180`, `dead_code: 9`, `fragile_debt: 22`, `duplicate_logic: 8`, `orphaned_logic: 22`
* *Architecture:* `api: 99`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 222`, `doc: 93`, `test: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ty, FunctionId, ValueNs, GenericArgs, InternedOpaqueTyId, TypeVisitableExt, HasModule, TypeAliasSignature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/tests/traits.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.309 IQR)
- **Top Global Matches:** file_cluster_16: 12.309, file_cluster_8: 12.423, file_cluster_0: 12.617
- **Magnitude:** 2210.28 | **LOC:** 5246 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 59.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (9.182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `i` (Impact: 274.0 | O(N^3) | DB: 4)
  * `iterator_chain` (Impact: 67.7 | O(N^3))
  * `proc_macro_server_types` (Impact: 51.0 | O(N^4))
  * `closure_as_argument_inference_order` (Impact: 49.1 | O(N^3))
  * `dyn_trait` (Impact: 47.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 1109`, `args: 608`, `func_start: 506`, `class_start: 286`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 41`, `dead_code: 3`, `fragile_debt: 8`, `duplicate_logic: 59`, `orphaned_logic: 110`
* *Architecture:* `api: 49`, `concurrency: 133`, `import: 25`
* *Defense:* `safety: 158`, `test: 271`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::tr::Tr, core::default::Default::default, core::ops::Index, check_types, m::Tr, crate::tests::infer_with_mismatches, check_infer_with_mismatches, check_infer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/goto_definition.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.242 IQR)
- **Top Global Matches:** file_cluster_8: 12.242, file_cluster_0: 12.364, file_cluster_16: 12.581
- **Magnitude:** 2125.56 | **LOC:** 4103 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.0457%), Tech Debt (11.4602%)
**Top Internal Functions/Classes:**
  * `find_definition_for_known_blanket_dual_i` (Impact: 258.4 | O(N^5))
    * *Intent:* // If the token is into(), try_into(), search the definition of From, TryFrom.
  * `nav_for_exit_points` (Impact: 160.2 | O(N^6) | DB: 1)
  * `find_branch_root` (Impact: 82.1 | O(N^5))
  * `nav_for_branch_exit_points` (Impact: 76.3 | O(N^5))
  * `handle_control_flow_keywords` (Impact: 63.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 604`, `args: 475`, `func_start: 430`, `class_start: 168`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `dead_code: 3`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 220`, `concurrency: 34`, `import: 38`
* *Defense:* `safety: 164`, `doc: 26`, `test: 168`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001655
  * `Imports (Out-Degree: 1):` SourceDatabase, SyntaxKind::*, ra_fixture::RaFixtureConfig, navigation_target::self, SyntaxToken, x, foo::buz, syntax_helpers::node_ext::find_loops...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-def/src/expr_store/pretty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.342 IQR)
- **Top Global Matches:** file_cluster_8: 12.342, file_cluster_13: 12.795, file_cluster_0: 12.842
- **Magnitude:** 2119.12 | **LOC:** 1377 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.454%), Tech Debt (14.7613%)
**Top Internal Functions/Classes:**
  * `print_expr_in` (Impact: 702.6 | O(2^N) | DB: 2)
  * `print_pat` (Impact: 371.1 | O(2^N) | DB: 3)
  * `print_type_ref` (Impact: 162.0 | O(2^N) | DB: 3)
  * `print_path` (Impact: 88.5 | O(N^6) | DB: 1)
  * `print_generic_params` (Impact: 67.9 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 167`, `args: 38`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 108`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 26`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 176`, `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syntax::ast::HasName, RangeOp, TraitBoundModifier, attrs::AttrFlags, expr_store::path::GenericArg, RecordSpread, FunctionId, TypeParamId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/hir-ty/src/diagnostics/decl_check/case_conv.rs` (RUST) | Magnitude: 88.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, safety_bypasses: 37, structural_boundaries: 14, safety: 13
- `crates/ide/src/folding_ranges.rs` (RUST) | Magnitude: 890.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 659, structural_boundaries: 127, safety: 120, branch: 111
- `crates/ide/src/inlay_hints/bind_pat.rs` (RUST) | Magnitude: 828.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 544, structural_boundaries: 220, bitwise_ops: 164, generics: 101
- `crates/edition/src/lib.rs` (RUST) | Magnitude: 82.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 14, safety: 11, api: 11
- `crates/ide-assists/src/handlers/remove_parentheses.rs` (RUST) | Magnitude: 386.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 316, args: 138, branch: 83, structural_boundaries: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/parser/src/grammar/items.rs` (RUST) | Magnitude: 528.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 302, structural_boundaries: 76, branch: 73, state_mutation: 49
- `crates/parser/src/grammar/items/traits.rs` (RUST) | Magnitude: 93.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 26, branch: 19, generics: 16
- `crates/parser/src/grammar/expressions/atom.rs` (RUST) | Magnitude: 1052.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 601, branch: 232, structural_boundaries: 124, dead_code: 100
- `crates/parser/src/grammar/items/adt.rs` (RUST) | Magnitude: 242.62 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 37, branch: 31, state_mutation: 17
- `crates/hir-ty/src/infer/coerce.rs` (RUST) | Magnitude: 318.88 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, doc: 157, structural_boundaries: 70, generics: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/rust-analyzer/src/cli/run_tests.rs` (RUST) | Magnitude: 75.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 37, state_mutation: 19, safety: 14
- `crates/proc-macro-srv/src/dylib.rs` (RUST) | Magnitude: 237.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 40, doc: 30, generics: 27
- `crates/ide-db/src/symbol_index.rs` (RUST) | Magnitude: 1668.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 714, structural_boundaries: 305, branch: 105, state_mutation: 104
- `crates/mbe/src/expander.rs` (RUST) | Magnitude: 44.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 67, indent_spaces: 51, structural_boundaries: 19, generics: 15
- `crates/ide-db/src/items_locator.rs` (RUST) | Magnitude: 224.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 33, branch: 17, state_mutation: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/hir-ty/src/tests/method_resolution.rs` (RUST) | Magnitude: 630.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 827, structural_boundaries: 355, bitwise_ops: 274, args: 266
- `crates/syntax/src/ast/syntax_factory.rs` (RUST) | Magnitude: 29.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, doc: 11, args: 8, safety: 7
- `crates/tt/src/storage.rs` (RUST) | Magnitude: 550.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 459, structural_boundaries: 107, state_mutation: 102, generics: 58
- `xtask/src/codegen/lints.rs` (RUST) | Magnitude: 261.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 435, structural_boundaries: 128, safety: 55, branch: 49
- `crates/parser/src/grammar.rs` (RUST) | Magnitude: 561.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 291, structural_boundaries: 93, state_mutation: 69, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/project-model/src/toolchain_info/target_tuple.rs` (RUST) | Magnitude: 126.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, safety: 41, structural_boundaries: 33, branch: 17
- `crates/ide-db/src/imports/merge_imports.rs` (RUST) | Magnitude: 844.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 335, structural_boundaries: 116, state_mutation: 95, branch: 91
- `crates/ide-completion/src/snippet.rs` (RUST) | Magnitude: 59.02 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, safety: 13, structural_boundaries: 12, args: 9
- `crates/ide/src/hover/render.rs` (RUST) | Magnitude: 2878.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1246, structural_boundaries: 318, safety: 312, branch: 259
- `crates/rust-analyzer/src/cli/unresolved_references.rs` (RUST) | Magnitude: 159.22 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 58, branch: 22, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/rust-analyzer/src/command.rs` (RUST) | Magnitude: 218.58 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 35, concurrency: 34, generics: 26
- `crates/ide-assists/src/handlers/unnecessary_async.rs` (RUST) | Magnitude: 395.82 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, args: 66, concurrency: 51, structural_boundaries: 48
- `crates/ide-diagnostics/src/handlers/expected_function.rs` (RUST) | Magnitude: 44.44 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, concurrency: 31, structural_boundaries: 18, args: 8
- `editors/code/src/dependencies_provider.ts` (TYPESCRIPT) | Magnitude: 21.33 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 69, structural_boundaries: 41, concurrency: 20
- `editors/code/src/util.ts` (TYPESCRIPT) | Magnitude: 46.79 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 211, structural_boundaries: 101, state_mutation: 59, args: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/vfs/src/anchored_path.rs` (RUST) | Magnitude: 16.12 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, api: 3, encapsulation: 3, sec_high_risk_execution: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/hir-ty/src/mir/eval/tests.rs` (RUST) | Magnitude: 604.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 216, args: 136, func_start: 117
- `crates/ide-assists/src/handlers/move_module_to_file.rs` (RUST) | Magnitude: 65.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 102, args: 40, func_start: 35
- `xtask/src/codegen/grammar.rs` (RUST) | Magnitude: 1193.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 996, structural_boundaries: 253, branch: 144, args: 125
- `crates/hir-ty/src/layout/target.rs` (RUST) | Magnitude: 81.88 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, safety: 15, branch: 10, structural_boundaries: 6
- `crates/rust-analyzer/src/cli/symbols.rs` (RUST) | Magnitude: 15.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, branch: 3, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/parser/src/grammar/items/use_item.rs` (RUST) | Magnitude: 102.68 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, dead_code: 22, structural_boundaries: 17, branch: 13
- `crates/parser/src/grammar/patterns.rs` (RUST) | Magnitude: 306.72 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 98, dead_code: 92, state_mutation: 57

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/hir-ty/src/next_solver/interner.rs` -> Churn: **92.18%** | Cog Load: 13.8912% | Debt: 99.887%
- `crates/hir-ty/src/lower.rs` -> Churn: **90.3%** | Cog Load: 10.5985% | Debt: 90.7131%
- `crates/hir-ty/src/infer.rs` -> Churn: **86.46%** | Cog Load: 11.9839% | Debt: 99.8517%
- `crates/hir-ty/src/display.rs` -> Churn: **85.51%** | Cog Load: 6.1262% | Debt: 99.9997%
- `crates/syntax/src/ast/syntax_factory/constructors.rs` -> Churn: **84.52%** | Cog Load: 65.5382% | Debt: 8.6936%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ide-completion/src/context/analysis.rs` -> **A4-Tacks** (83.3% isolated ownership) | Magnitude: 5270.42
- `crates/ide-assists/src/handlers/move_guard.rs` -> **A4-Tacks** (90.0% isolated ownership) | Magnitude: 1431.92
- `crates/hir-def/src/find_path.rs` -> **Lukas Wirth** (100.0% isolated ownership) | Magnitude: 1382.38
- `crates/ide-completion/src/completions/item_list/trait_impl.rs` -> **A4-Tacks** (100.0% isolated ownership) | Magnitude: 1265.38
- `crates/parser/src/grammar/expressions.rs` -> **A4-Tacks** (100.0% isolated ownership) | Magnitude: 1199.78

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `editors/code/src/ctx.ts` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 100.0%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 48.8964%)
- `crates/syntax/src/ted.rs` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 97.0181%)
- `editors/code/src/run.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 51.7523%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/syntax/src/ast.rs` -> **Severity: 5.916** (Embedded: 0.068 * Error Risk: 87.0118%)
- `crates/ide-completion/src/tests/use_tree.rs` -> **Severity: 1.157** (Embedded: 0.0165 * Error Risk: 70.1341%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 0.697** (Embedded: 0.0294 * Error Risk: 23.6706%)
- `editors/code/src/ctx.ts` -> **Severity: 0.554** (Embedded: 0.0058 * Error Risk: 95.0684%)
- `editors/code/src/dependencies_provider.ts` -> **Severity: 0.308** (Embedded: 0.0033 * Error Risk: 92.569%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/syntax/src/ast.rs` -> **Severity: 4140.013** (Blast Radius: 53.45 * Doc Risk: 77.4558%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 1988.7** (Blast Radius: 19.887 * Doc Risk: 100.0%)
- `crates/tt/src/iter.rs` -> **Severity: 1023.8** (Blast Radius: 10.238 * Doc Risk: 100.0%)
- `editors/code/src/lsp_ext.ts` -> **Severity: 797.0** (Blast Radius: 7.97 * Doc Risk: 100.0%)
- `crates/syntax/src/algo.rs` -> **Severity: 515.0** (Blast Radius: 5.15 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
