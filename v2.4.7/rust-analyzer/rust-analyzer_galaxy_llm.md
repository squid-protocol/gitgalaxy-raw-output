# ARCHITECTURAL_BRIEF: rust-analyzer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/rust-analyzer` |
| **Timestamp** | `2026-08-07T04:07:51.320679+00:00` |
| **Scan Duration** | `6.79s` |
| **Git Branch** | `master` |
| **Git Commit** | `9767050b2db436f5a770c5f91a548c88fd91ec71` |
| **Git Remote** | `https://github.com/rust-lang/rust-analyzer.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1244 malicious artifacts.

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
| Total Artifacts | 2262 |
| Analyzed Artifacts (Scanned) | 1374 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 888 |
| Total LOC | 400685 |
| Volatility Index | 0.01 |
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
> **Architectural Drift Z-Score:** `4.408`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 684 | 49.8% |
| file_cluster_16 | 194 | 14.1% |
| file_cluster_0 | 182 | 13.2% |
| file_cluster_13 | 134 | 9.8% |
| file_cluster_17 | 43 | 3.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 11.4 | 7.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 25.5 | 24.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 48.1 | 47.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.4 | 2.3 | 80.0 |
| API Exposure | 0.0 | 15.1 | 2.8 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 32.1 | 15.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 82.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 14.1 | 2.2 | 0.3 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 15.3 | 4.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.0 | 15.9 | 0.0 |
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

- `replace_if_let_with_match` (@ `crates/ide-assists/src/handlers/replace_if_let_with_match.rs`) -> Impact: **630.3** | LOC: 2214
  * *Intent:* // Assist: replace_if_let_with_match // // Replaces a `if let` expression with a `match` expression. // // ``` // enum Action { Move { distance: u32 }...
- `wrap_return_type` (@ `crates/ide-assists/src/handlers/wrap_return_type.rs`) -> Impact: **626.1** | LOC: 2442
  * *Intent:* // Assist: wrap_return_type_in_option // // Wrap the function's return type into Option. // // ``` // # //- minicore: option // fn foo() -> i32$0 { 42...
- `else_completion_after_if` (@ `crates/ide-completion/src/tests/expression.rs`) -> Impact: **605.5** | LOC: 1059
- `lower_expr_to_place_without_adjust` (@ `crates/hir-ty/src/mir/lower.rs`) -> Impact: **510.9** | LOC: 1204
- `exec_intrinsic` (@ `crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **453.1** | LOC: 783
- `diagnostics` (@ `crates/hir/src/lib.rs`) -> Impact: **405.9** | LOC: 1365
- `delegate` (@ `crates/ide-assists/src/handlers/generate_delegate_trait.rs`) -> Impact: **397.8** | LOC: 1696
- `complete_postfix` (@ `crates/ide-completion/src/completions/postfix.rs`) -> Impact: **384.6** | LOC: 1293
- `expected_type_and_name` (@ `crates/ide-completion/src/context/analysis.rs`) -> Impact: **374.4** | LOC: 1067
- `expand` (@ `crates/ide-completion/src/context/analysis.rs`) -> Impact: **369.4** | LOC: 1109

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/ide-assists/src/handlers` | 134 | 32423.28 | 13.67% | 75.66% |
| `crates/ide/src` | 43 | 10580.56 | 9.83% | 59.28% |
| `crates/hir/src` | 11 | 6487.18 | 13.47% | 67.57% |
| `crates/hir-def/src` | 20 | 6164.12 | 11.28% | 79.85% |
| `crates/hir-ty/src` | 29 | 5790.8 | 10.43% | 57.14% |
| `crates/ide-diagnostics/src/handlers` | 52 | 5584.12 | 11.03% | 90.04% |
| `crates/hir-ty/src/tests` | 14 | 5559.28 | 6.11% | 0.0% |
| `crates/hir-ty/src/next_solver` | 21 | 4510.36 | 11.74% | 83.92% |
| `crates/ide-completion/src/tests` | 15 | 3970.44 | 3.75% | 0.0% |
| `crates/hir-ty/src/mir` | 5 | 3806.2 | 22.71% | 35.44% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/base-db/src/target.rs` -> **100.0%** Exposure
- `crates/hir-def/src/dyn_map.rs` -> **100.0%** Exposure
- `crates/hir-def/src/lib.rs` -> **100.0%** Exposure
- `crates/hir-def/src/macro_expansion_tests/builtin_fn_macro.rs` -> **100.0%** Exposure
- `crates/hir-def/src/macro_expansion_tests/mbe/matching.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/ide-assists/src/handlers/remove_mut.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/gen_trait_fn_body.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/ref_field_expr.rs` -> **100.0%** Exposure
- `crates/ide-db/src/syntax_helpers/format_string.rs` -> **100.0%** Exposure
- `crates/ide/src/inlay_hints/binding_mode.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/ide/src/hover/tests.rs` -> **252** Orphaned Functions | **2** Duplicates
- `crates/hir-ty/src/tests/traits.rs` -> **113** Orphaned Functions | **100** Duplicates
- `crates/hir/src/lib.rs` -> **53** Orphaned Functions | **128** Duplicates
- `crates/hir-ty/src/tests/regression.rs` -> **37** Orphaned Functions | **126** Duplicates
- `crates/hir-ty/src/tests/simple.rs` -> **32** Orphaned Functions | **122** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/rust-analyzer/src/lsp/capabilities.rs`** -> AI Confidence: **99.48%**
2. **`crates/ide-assists/src/handlers/merge_nested_if.rs`** -> AI Confidence: **99.39%**
3. **`crates/ide-assists/src/handlers/move_guard.rs`** -> AI Confidence: **99.39%**
4. **`crates/ide-diagnostics/src/handlers/missing_match_arms.rs`** -> AI Confidence: **99.39%**
5. **`crates/ide-assists/src/handlers/add_label_to_loop.rs`** -> AI Confidence: **99.35%**
6. **`crates/hir-expand/src/inert_attr_macro.rs`** -> AI Confidence: **99.32%**
7. **`crates/cfg/src/cfg_expr.rs`** -> AI Confidence: **99.31%**
8. **`crates/cfg/src/dnf.rs`** -> AI Confidence: **99.31%**
9. **`crates/cfg/src/lib.rs`** -> AI Confidence: **99.31%**
10. **`crates/hir-def/src/expr_store/lower/asm.rs`** -> AI Confidence: **99.31%**
11. **`crates/hir-def/src/expr_store/lower/path.rs`** -> AI Confidence: **99.31%**
12. **`crates/hir-def/src/expr_store/path.rs`** -> AI Confidence: **99.31%**
13. **`crates/hir-def/src/expr_store/pretty.rs`** -> AI Confidence: **99.31%**
14. **`crates/hir-def/src/nameres/proc_macro.rs`** -> AI Confidence: **99.31%**
15. **`crates/hir-expand/src/fixup.rs`** -> AI Confidence: **99.31%**
16. **`crates/hir-ty/src/layout/target.rs`** -> AI Confidence: **99.31%**
17. **`crates/hir-ty/src/mir/eval.rs`** -> AI Confidence: **99.31%**
18. **`crates/hir-ty/src/mir/eval/shim.rs`** -> AI Confidence: **99.31%**
19. **`crates/hir-ty/src/mir/lower/pattern_matching.rs`** -> AI Confidence: **99.31%**
20. **`crates/hir-ty/src/mir/monomorphization.rs`** -> AI Confidence: **99.31%**
21. **`crates/hir-ty/src/next_solver/infer/resolve.rs`** -> AI Confidence: **99.31%**
22. **`crates/hir-ty/src/next_solver/infer/snapshot/fudge.rs`** -> AI Confidence: **99.31%**
23. **`crates/hir-ty/src/next_solver/ty.rs`** -> AI Confidence: **99.31%**
24. **`crates/hir-ty/src/representability.rs`** -> AI Confidence: **99.31%**
25. **`crates/hir/src/display.rs`** -> AI Confidence: **99.31%**
26. **`crates/hir/src/from_id.rs`** -> AI Confidence: **99.31%**
27. **`crates/hir/src/source_analyzer.rs`** -> AI Confidence: **99.31%**
28. **`crates/ide-assists/src/handlers/add_return_type.rs`** -> AI Confidence: **99.31%**
29. **`crates/ide-assists/src/handlers/apply_demorgan.rs`** -> AI Confidence: **99.31%**
30. **`crates/ide-assists/src/handlers/convert_bool_then.rs`** -> AI Confidence: **99.31%**
31. **`crates/ide-assists/src/handlers/convert_let_else_to_match.rs`** -> AI Confidence: **99.31%**
32. **`crates/ide-assists/src/handlers/convert_range_for_to_while.rs`** -> AI Confidence: **99.31%**
33. **`crates/ide-assists/src/handlers/convert_to_guarded_return.rs`** -> AI Confidence: **99.31%**
34. **`crates/ide-assists/src/handlers/convert_two_arm_bool_match_to_matches_macro.rs`** -> AI Confidence: **99.31%**
35. **`crates/ide-assists/src/handlers/convert_while_to_loop.rs`** -> AI Confidence: **99.31%**
36. **`crates/ide-assists/src/handlers/extract_variable.rs`** -> AI Confidence: **99.31%**
37. **`crates/ide-assists/src/handlers/inline_const_as_literal.rs`** -> AI Confidence: **99.31%**
38. **`crates/ide-assists/src/handlers/invert_if.rs`** -> AI Confidence: **99.31%**
39. **`crates/ide-assists/src/handlers/pull_assignment_up.rs`** -> AI Confidence: **99.31%**
40. **`crates/ide-assists/src/handlers/remove_else_branches.rs`** -> AI Confidence: **99.31%**
41. **`crates/ide-assists/src/handlers/remove_parentheses.rs`** -> AI Confidence: **99.31%**
42. **`crates/ide-assists/src/handlers/replace_if_let_with_match.rs`** -> AI Confidence: **99.31%**
43. **`crates/ide-assists/src/handlers/toggle_macro_delimiter.rs`** -> AI Confidence: **99.31%**
44. **`crates/ide-assists/src/handlers/unwrap_block.rs`** -> AI Confidence: **99.31%**
45. **`crates/ide-completion/src/completions/attribute/lint.rs`** -> AI Confidence: **99.31%**
46. **`crates/ide-completion/src/completions/keyword.rs`** -> AI Confidence: **99.31%**
47. **`crates/ide-completion/src/completions/lifetime.rs`** -> AI Confidence: **99.31%**
48. **`crates/ide-completion/src/completions/pattern.rs`** -> AI Confidence: **99.31%**
49. **`crates/ide-completion/src/context/analysis.rs`** -> AI Confidence: **99.31%**
50. **`crates/ide-db/src/defs.rs`** -> AI Confidence: **99.31%**
51. **`crates/ide-db/src/famous_defs.rs`** -> AI Confidence: **99.31%**
52. **`crates/ide-diagnostics/src/handlers/remove_unnecessary_else.rs`** -> AI Confidence: **99.31%**
53. **`crates/ide-diagnostics/src/tests/overly_long_real_world_cases.rs`** -> AI Confidence: **99.31%**
54. **`crates/ide/src/folding_ranges.rs`** -> AI Confidence: **99.31%**
55. **`crates/ide/src/inlay_hints/closing_brace.rs`** -> AI Confidence: **99.31%**
56. **`crates/ide/src/syntax_highlighting.rs`** -> AI Confidence: **99.31%**
57. **`crates/ide/src/syntax_highlighting/highlight.rs`** -> AI Confidence: **99.31%**
58. **`crates/parser/src/grammar/expressions.rs`** -> AI Confidence: **99.31%**
59. **`crates/parser/src/grammar/items.rs`** -> AI Confidence: **99.31%**
60. **`crates/parser/src/lexed_str.rs`** -> AI Confidence: **99.31%**
61. **`crates/proc-macro-srv/src/token_stream.rs`** -> AI Confidence: **99.31%**
62. **`crates/rust-analyzer/src/bin/main.rs`** -> AI Confidence: **99.31%**
63. **`crates/syntax/src/ast/edit_in_place.rs`** -> AI Confidence: **99.31%**
64. **`crates/syntax/src/ast/expr_ext.rs`** -> AI Confidence: **99.31%**
65. **`crates/syntax/src/ast/prec.rs`** -> AI Confidence: **99.31%**
66. **`xtask/src/install.rs`** -> AI Confidence: **99.31%**
67. **`xtask/src/pgo.rs`** -> AI Confidence: **99.31%**
68. **`xtask/src/publish/notes.rs`** -> AI Confidence: **99.31%**
69. **`editors/code/src/client.ts`** -> AI Confidence: **99.31%**
70. **`editors/code/src/ctx.ts`** -> AI Confidence: **99.31%**
71. **`editors/code/src/debug.ts`** -> AI Confidence: **99.31%**
72. **`editors/code/src/run.ts`** -> AI Confidence: **99.31%**
73. **`crates/hir-def/src/macro_expansion_tests/mbe/meta_syntax.rs`** -> AI Confidence: **99.29%**
74. **`crates/ide-diagnostics/src/handlers/break_outside_of_loop.rs`** -> AI Confidence: **99.29%**
75. **`crates/parser/test_data/parser/err/0008_item_block_recovery.rs`** -> AI Confidence: **99.29%**
76. **`crates/parser/test_data/parser/err/0010_unsafe_lambda_block.rs`** -> AI Confidence: **99.29%**
77. **`crates/parser/test_data/parser/err/0032_match_arms_inner_attrs.rs`** -> AI Confidence: **99.29%**
78. **`crates/parser/test_data/parser/err/0033_match_arms_outer_attrs.rs`** -> AI Confidence: **99.29%**
79. **`crates/parser/test_data/parser/inline/err/match_arms_recovery.rs`** -> AI Confidence: **99.29%**
80. **`crates/parser/test_data/parser/inline/ok/break_ambiguity.rs`** -> AI Confidence: **99.29%**
81. **`crates/parser/test_data/parser/inline/ok/break_expr.rs`** -> AI Confidence: **99.29%**
82. **`crates/parser/test_data/parser/inline/ok/closure_binder.rs`** -> AI Confidence: **99.29%**
83. **`crates/parser/test_data/parser/inline/ok/closure_body_underscore_assignment.rs`** -> AI Confidence: **99.29%**
84. **`crates/parser/test_data/parser/inline/ok/closure_range_method_call.rs`** -> AI Confidence: **99.29%**
85. **`crates/parser/test_data/parser/inline/ok/continue_expr.rs`** -> AI Confidence: **99.29%**
86. **`crates/parser/test_data/parser/inline/ok/exclusive_range_pat.rs`** -> AI Confidence: **99.29%**
87. **`crates/parser/test_data/parser/inline/ok/for_range_from.rs`** -> AI Confidence: **99.29%**
88. **`crates/parser/test_data/parser/inline/ok/if_expr.rs`** -> AI Confidence: **99.29%**
89. **`crates/parser/test_data/parser/inline/ok/label.rs`** -> AI Confidence: **99.29%**
90. **`crates/parser/test_data/parser/inline/ok/literal_pattern.rs`** -> AI Confidence: **99.29%**
91. **`crates/parser/test_data/parser/inline/ok/match_arm.rs`** -> AI Confidence: **99.29%**
92. **`crates/parser/test_data/parser/inline/ok/match_arms_commas.rs`** -> AI Confidence: **99.29%**
93. **`crates/parser/test_data/parser/inline/ok/match_arms_inner_attribute.rs`** -> AI Confidence: **99.29%**
94. **`crates/parser/test_data/parser/inline/ok/match_arms_outer_attributes.rs`** -> AI Confidence: **99.29%**
95. **`crates/parser/test_data/parser/inline/ok/match_expr.rs`** -> AI Confidence: **99.29%**
96. **`crates/parser/test_data/parser/inline/ok/no_semi_after_block.rs`** -> AI Confidence: **99.29%**
97. **`crates/parser/test_data/parser/inline/ok/or_pattern.rs`** -> AI Confidence: **99.29%**
98. **`crates/parser/test_data/parser/inline/ok/range_pat.rs`** -> AI Confidence: **99.29%**
99. **`crates/parser/test_data/parser/inline/ok/stmt_postfix_expr_ambiguity.rs`** -> AI Confidence: **99.29%**
100. **`crates/parser/test_data/parser/ok/0033_label_break.rs`** -> AI Confidence: **99.29%**
101. **`crates/parser/test_data/parser/ok/0052_for_range_block.rs`** -> AI Confidence: **99.29%**
102. **`crates/parser/test_data/parser/ok/0056_neq_in_type.rs`** -> AI Confidence: **99.29%**
103. **`crates/parser/test_data/parser/ok/0057_loop_in_call.rs`** -> AI Confidence: **99.29%**
104. **`crates/parser/test_data/parser/ok/0059_loops_in_parens.rs`** -> AI Confidence: **99.29%**
105. **`crates/parser/test_data/parser/ok/0071_stmt_attr_placement.rs`** -> AI Confidence: **99.29%**
106. **`crates/syntax/test_data/parser/fuzz-failures/0003.rs`** -> AI Confidence: **99.29%**
107. **`crates/ide/src/highlight_related.rs`** -> AI Confidence: **99.25%**
108. **`crates/rust-analyzer/src/lsp/from_proto.rs`** -> AI Confidence: **99.25%**
109. **`crates/rust-analyzer/src/reload.rs`** -> AI Confidence: **99.25%**
110. **`crates/syntax-bridge/src/prettify_macro_expansion.rs`** -> AI Confidence: **99.25%**
111. **`crates/syntax/src/validation.rs`** -> AI Confidence: **99.25%**
112. **`crates/hir-def/src/lang_item.rs`** -> AI Confidence: **99.24%**
113. **`crates/hir-def/src/lib.rs`** -> AI Confidence: **99.24%**
114. **`crates/hir-def/src/nameres/path_resolution.rs`** -> AI Confidence: **99.24%**
115. **`crates/hir-def/src/resolver.rs`** -> AI Confidence: **99.24%**
116. **`crates/hir-def/src/visibility.rs`** -> AI Confidence: **99.24%**
117. **`crates/hir-expand/src/attrs.rs`** -> AI Confidence: **99.24%**
118. **`crates/hir-expand/src/lib.rs`** -> AI Confidence: **99.24%**
119. **`crates/hir-expand/src/mod_path.rs`** -> AI Confidence: **99.24%**
120. **`crates/hir-expand/src/span_map.rs`** -> AI Confidence: **99.24%**
121. **`crates/hir-ty/src/dyn_compatibility.rs`** -> AI Confidence: **99.24%**
122. **`crates/hir-ty/src/infer/cast.rs`** -> AI Confidence: **99.24%**
123. **`crates/hir-ty/src/infer/mutability.rs`** -> AI Confidence: **99.24%**
124. **`crates/hir-ty/src/infer/op.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19184` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editors/code/src/dependencies_provider.ts` (TYPESCRIPT) -> Cumulative Risk: **748.57**
- **Archetype:** `file_cluster_4` (Distance: 12.349 IQR)
- **Magnitude:** 16.02 | **LOC:** 155 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9621%), Tech Debt (99.8674%)
- **Heaviest Functions:** `getChildren` (Impact: 11.6), `constructor` (Impact: 8.1), `getRootDependencies` (Impact: 6.8)

### 2. `editors/code/src/diagnostics.ts` (TYPESCRIPT) -> Cumulative Risk: **691.39**
- **Archetype:** `file_cluster_4` (Distance: 11.469 IQR)
- **Magnitude:** 13.12 | **LOC:** 213 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9593%), State Flux (99.8289%), Tech Debt (99.4472%)
- **Heaviest Functions:** `getRenderedDiagnostic` (Impact: 16.5), `_getDecorations` (Impact: 10.8), `provideDecorations` (Impact: 8.5)

### 3. `crates/test-utils/src/minicore.rs` (RUST) -> Cumulative Risk: **658.29**
- **Archetype:** `file_cluster_0` (Distance: 13.187 IQR)
- **Magnitude:** 1062.02 | **LOC:** 2234 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (86.5465%)
- **Heaviest Functions:** `drop` (Impact: 23.1), `async_call_once` (Impact: 14.1), `call_once` (Impact: 13.6)

### 4. `editors/code/src/test_explorer.ts` (TYPESCRIPT) -> Cumulative Risk: **651.1**
- **Archetype:** `file_cluster_4` (Distance: 11.474 IQR)
- **Magnitude:** 34.27 | **LOC:** 213 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9422%), Safety Score (80.1445%)
- **Heaviest Functions:** `prepareTestExplorer` (Impact: 117.6), `addTestGroup` (Impact: 34.2), `addTest` (Impact: 28.1)

### 5. `crates/stdx/src/lib.rs` (RUST) -> Cumulative Risk: **628.84**
- **Archetype:** `file_cluster_0` (Distance: 11.407 IQR)
- **Magnitude:** 275.02 | **LOC:** 463 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9835%), Documentation (96.1664%), State Flux (88.9216%)
- **Heaviest Functions:** `to_camel_case` (Impact: 28.4), `to_snake_case` (Impact: 21.1), `iter_eq_by` (Impact: 11.2)

### 6. `crates/intern/src/gc.rs` (RUST) -> Cumulative Risk: **627.45**
- **Archetype:** `file_cluster_16` (Distance: 11.942 IQR)
- **Magnitude:** 132.1 | **LOC:** 336 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.581%), Concurrency (94.7294%)
- **Heaviest Functions:** `collect` (Impact: 11.1), `sweep_storage` (Impact: 8.9), `sweep` (Impact: 8.3)

### 7. `editors/code/src/ctx.ts` (TYPESCRIPT) -> Cumulative Risk: **618.25**
- **Archetype:** `file_cluster_4` (Distance: 13.544 IQR)
- **Magnitude:** 78.09 | **LOC:** 647 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.0684%)
- **Heaviest Functions:** `prepareSyntaxTreeView` (Impact: 40.7), `updateStatusBarItem` (Impact: 32.7), `getOrCreateClient` (Impact: 26.4)

### 8. `editors/code/src/config.ts` (TYPESCRIPT) -> Cumulative Risk: **610.92**
- **Archetype:** `file_cluster_4` (Distance: 12.531 IQR)
- **Magnitude:** 64.83 | **LOC:** 614 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9961%), State Flux (99.9835%), Safety Score (81.2355%)
- **Heaviest Functions:** `configureLanguage` (Impact: 162.0), `substituteVariablesInEnv` (Impact: 45.6), `toggleCheckOnSave` (Impact: 36.3)

### 9. `editors/code/src/util.ts` (TYPESCRIPT) -> Cumulative Risk: **610.45**
- **Archetype:** `file_cluster_4` (Distance: 12.775 IQR)
- **Magnitude:** 31.53 | **LOC:** 356 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.0728%), Concurrency (98.6548%)
- **Heaviest Functions:** `resolve` (Impact: 15.6), `spawnAsync` (Impact: 13.4), `findRustToolchainFiles` (Impact: 13.2)

### 10. `crates/ide-db/src/source_change.rs` (RUST) -> Cumulative Risk: **577.65**
- **Archetype:** `file_cluster_16` (Distance: 12.937 IQR)
- **Magnitude:** 320.78 | **LOC:** 573 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9965%), State Flux (98.8786%)
- **Heaviest Functions:** `commit` (Impact: 28.9), `insert_source_and_snippet_edit` (Impact: 15.8), `new` (Impact: 9.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/ide-assists/src/handlers/extract_function.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.471 IQR)
- **Top Global Matches:** file_cluster_8: 13.471, file_cluster_0: 13.502, file_cluster_17: 13.711
- **Magnitude:** 2406.34 | **LOC:** 6541 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 38.9%
- **Risk Profile:** Cognitive Load (13.7082%), Tech Debt (88.8658%)
**Top Internal Functions/Classes:**
  * `locals_defined_in_body` (Impact: 313.7)
  * `extract_function` (Impact: 57.4)
    * *Intent:* // Assist: extract_function // // Extracts selected statements and comments into new function. // //...
  * `analyze_container` (Impact: 52.5)
  * `make_call` (Impact: 34.3)
  * `make_body` (Impact: 33.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 1231`, `args: 681`, `func_start: 586`, `class_start: 100`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 343`, `dead_code: 17`, `fragile_debt: 10`, `duplicate_logic: 7`, `orphaned_logic: 145`
* *Architecture:* `api: 13`, `concurrency: 28`, `import: 16`
* *Defense:* `safety: 600`, `doc: 68`, `test: 153`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ops::RangeInclusive, insert_use, Local, SyntaxToken, std::iter, InFile, walk_patterns_in_expr, WalkEvent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.339 IQR)
- **Top Global Matches:** file_cluster_16: 14.339, file_cluster_8: 14.396, file_cluster_0: 14.485
- **Magnitude:** 2392.8 | **LOC:** 7283 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 44.8%
- **Risk Profile:** Cognitive Load (7.7457%), Tech Debt (99.997%)
**Top Internal Functions/Classes:**
  * `diagnostics` (Impact: 405.9)
  * `ty` (Impact: 253.6)
  * `diagnostics` (Impact: 138.4)
  * `eval` (Impact: 18.0)
  * `as_local` (Impact: 15.4)
    * *Intent:* // Get the type for the trait function, as we can't get the type for the impl function // because it...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 880`, `args: 634`, `func_start: 468`, `class_start: 71`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 158`, `dead_code: 5`, `fragile_debt: 33`, `duplicate_logic: 128`, `orphaned_logic: 53`
* *Architecture:* `api: 489`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 621`, `doc: 181`, `test: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smallvec::SmallVec, BindingId, syntax::
    AstNode, TargetDataLayout, LifetimeParamData, is_inherent_impl_coherent, EnumId, hir_expand::
        name::AsName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/tests/expression.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.961 IQR)
- **Top Global Matches:** file_cluster_8: 11.961, file_cluster_0: 12.263, file_cluster_13: 12.356
- **Magnitude:** 1999.5 | **LOC:** 3697 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (11.8436%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `else_completion_after_if` (Impact: 605.5)
  * `inside_faulty_format_args_completions_wo` (Impact: 272.0)
  * `completes_after_ref_expr` (Impact: 81.2)
  * `completes_let_else` (Impact: 54.2)
  * `let_in_previous_line_of_ambiguous_expr` (Impact: 49.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 689`, `structural_boundaries: 872`, `args: 352`, `func_start: 310`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 135`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 51`
* *Architecture:* `api: 22`, `concurrency: 44`, `import: 41`
* *Defense:* `safety: 263`, `doc: 2`, `test: 62`, `immutability_locks: 136`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` check_with_base_items, std::*, TEST_CONFIG, check_edit, expect_test::Expect, _69latrick::*, config::AutoImportExclusionType, proc_macros::identity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.057 IQR)
- **Top Global Matches:** file_cluster_8: 14.057, file_cluster_16: 14.225, file_cluster_0: 14.282
- **Magnitude:** 1910.12 | **LOC:** 3193 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.9471%), Tech Debt (55.3031%)
**Top Internal Functions/Classes:**
  * `eval_rvalue` (Impact: 297.0)
  * `interpret_mir` (Impact: 90.9)
  * `pretty_print` (Impact: 82.6)
  * `create_memory_map` (Impact: 82.6)
  * `rec` (Impact: 80.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 589`, `structural_boundaries: 678`, `args: 193`, `func_start: 90`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 256`, `fragile_debt: 12`, `duplicate_logic: 12`, `orphaned_logic: 7`
* *Architecture:* `api: 14`, `import: 28`
* *Defense:* `safety: 531`, `doc: 22`, `test: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mod_path::path, return_slot, OperandKind, stdx::never, ConstKind, Quad, ConstEvalError, StaticSignature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.62 IQR)
- **Top Global Matches:** file_cluster_8: 10.62, file_cluster_7: 11.176, file_cluster_16: 11.19
- **Magnitude:** 1666.76 | **LOC:** 11407 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 61.1%
- **Risk Profile:** Cognitive Load (5.1248%), Tech Debt (82.2713%)
**Top Internal Functions/Classes:**
  * `hover_intra_inner_attr` (Impact: 32.4)
    * *Intent:* *[`Foo`]*
  * `hover_intra_outer_attr` (Impact: 32.4)
  * `hover_const_eval` (Impact: 27.6)
  * `type_alias_without_docs` (Impact: 25.5)
  * `drop_glue` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 1023`, `args: 675`, `func_start: 658`, `class_start: 355`
* *Risk/State:* `safety_bypasses: 484`, `state_mutation: 48`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 252`
* *Architecture:* `api: 162`, `concurrency: 16`, `import: 31`
* *Defense:* `safety: 120`, `doc: 157`, `test: 282`, `immutability_locks: 202`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils::expect_test::expect, ra_fixture::RaFixtureConfig, super::*, string::*, Option::Some, expect, hir::setup_tracing, t2::T2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/wrap_return_type.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.103 IQR)
- **Top Global Matches:** file_cluster_8: 13.103, file_cluster_0: 13.149, file_cluster_4: 13.424
- **Magnitude:** 1612.16 | **LOC:** 2563 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.6022%), Tech Debt (94.7146%)
**Top Internal Functions/Classes:**
  * `wrap_return_type` (Impact: 626.1)
    * *Intent:* // Assist: wrap_return_type_in_option // // Wrap the function's return type into Option. // // ``` /...
  * `wrap_return_type_in_option_simple_with_w` (Impact: 65.9)
  * `wrap_return_type_in_result_simple_with_w` (Impact: 65.9)
  * `wrap_return_type_in_option_simple_with_c` (Impact: 37.0)
  * `wrap_return_type_in_result_simple_with_c` (Impact: 37.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 417`, `args: 275`, `func_start: 236`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 133`, `dead_code: 4`, `duplicate_logic: 40`, `orphaned_logic: 27`
* *Architecture:* `api: 11`, `concurrency: 80`, `import: 15`
* *Defense:* `safety: 441`, `test: 67`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syntax::
    AstNode, syntax_factory::SyntaxFactory, std::iter, hir::HasSource, check_assist_not_applicable_by_label, super::*, some_module::Result, some_module::Option...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/context/analysis.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.791 IQR)
- **Top Global Matches:** file_cluster_17: 13.791, file_cluster_8: 13.833, file_cluster_0: 14.102
- **Magnitude:** 1410.42 | **LOC:** 2116 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 82.5%
- **Risk Profile:** Cognitive Load (13.7712%), Tech Debt (11.5663%)
**Top Internal Functions/Classes:**
  * `expected_type_and_name` (Impact: 374.4)
  * `expand` (Impact: 369.4)
  * `classify_name_ref` (Impact: 309.4)
  * `analyze` (Impact: 53.4)
    * *Intent:* // Proc macros can make the same span with different text, we don't // want them to participate in c...
  * `pattern_context_for` (Impact: 27.2)
    * *Intent:* // A record expression in this position is usually a result of parsing recovery, so check that
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 395`, `args: 208`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 54`, `dead_code: 10`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 398`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SyntaxToken, syntax::
    AstNode, HasArgList, ItemListKind, std::iter, Direction, InFile, LifetimeKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/tests/traits.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.05 IQR)
- **Top Global Matches:** file_cluster_16: 12.05, file_cluster_8: 12.14, file_cluster_0: 12.387
- **Magnitude:** 1401.28 | **LOC:** 5246 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 59.1%
- **Risk Profile:** Cognitive Load (7.3532%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `i` (Impact: 89.5)
  * `foo` (Impact: 59.9)
  * `iterator_chain` (Impact: 29.6)
  * `proc_macro_server_types` (Impact: 20.7)
  * `closure_as_argument_inference_order` (Impact: 19.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 1108`, `args: 618`, `func_start: 506`, `class_start: 298`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 23`, `dead_code: 3`, `fragile_debt: 8`, `duplicate_logic: 100`, `orphaned_logic: 113`
* *Architecture:* `api: 49`, `concurrency: 133`, `import: 25`
* *Defense:* `safety: 158`, `test: 271`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` check_types, core::marker::PhantomData, super::check, check_no_mismatches, check_infer, serde::Deserialize, foo::Bar, check_infer_with_mismatches...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/replace_if_let_with_match.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.732 IQR)
- **Top Global Matches:** file_cluster_8: 12.732, file_cluster_0: 12.887, file_cluster_17: 13.221
- **Magnitude:** 1349.44 | **LOC:** 2296 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (11.0918%), Tech Debt (40.749%)
**Top Internal Functions/Classes:**
  * `replace_if_let_with_match` (Impact: 630.3)
    * *Intent:* // Assist: replace_if_let_with_match // // Replaces a `if let` expression with a `match` expression....
  * `replace_match_with_if_let` (Impact: 56.8)
  * `test_if_let_with_match_let_chain` (Impact: 51.9)
  * `nested_indent` (Impact: 33.3)
  * `test_if_let_with_match_nested_slice` (Impact: 29.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 256`, `args: 206`, `func_start: 187`, `class_start: 12`
* *Risk/State:* `state_mutation: 22`, `dead_code: 6`, `orphaned_logic: 45`
* *Architecture:* `api: 21`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 495`, `doc: 1`, `test: 47`, `immutability_locks: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` defs::NameClass, syntax::
    AstNode, syntax_factory::SyntaxFactory, unwrap_trivial_block, Edition, super::*, IndentLevel, crate::
    AssistContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.226 IQR)
- **Top Global Matches:** file_cluster_8: 14.226, file_cluster_17: 14.306, file_cluster_0: 14.351
- **Magnitude:** 1343.68 | **LOC:** 2341 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 58.1%
- **Risk Profile:** Cognitive Load (19.9387%), Tech Debt (51.7271%)
**Top Internal Functions/Classes:**
  * `lower_expr_to_place_without_adjust` (Impact: 510.9)
  * `lower_loop` (Impact: 161.8)
  * `lower_block_to_place` (Impact: 60.4)
  * `pretty_print` (Impact: 51.6)
    * *Intent:* // Uncomment this to make `DropScopeToken` a drop bomb. Unfortunately we can't do this in release, s...
  * `lower_params_and_bindings` (Impact: 48.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 359`, `args: 87`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 136`, `dead_code: 6`, `fragile_debt: 11`, `orphaned_logic: 12`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* `safety: 409`, `doc: 21`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BindingId, Local, return_slot, PointerCast, BinaryOp, LocalFieldId, StaticSignature, ExprId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/lsp/to_proto.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.466 IQR)
- **Top Global Matches:** file_cluster_8: 12.466, file_cluster_17: 12.836, file_cluster_0: 12.878
- **Magnitude:** 1341.26 | **LOC:** 3091 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 26.7%
- **Risk Profile:** Cognitive Load (11.6732%), Tech Debt (21.1907%)
**Top Internal Functions/Classes:**
  * `merge_text_and_snippet_edits` (Impact: 312.7)
  * `completion_item` (Impact: 148.2)
  * `code_lens` (Impact: 64.0)
  * `semantic_tokens` (Impact: 37.3)
  * `inlay_hint` (Impact: 33.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 389`, `args: 161`, `func_start: 79`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 139`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 75`, `import: 15`
* *Defense:* `safety: 358`, `doc: 11`, `test: 22`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.052
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001457
  * `Imports (Out-Degree: 3):` serde_json::to_value, lsp_ext::self, lsp::to_proto::location, AssistKind, Cancellable, AnnotationKind, paths::Utf8Component, ops::Not...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/syntax/src/ast/syntax_factory/constructors.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.7 IQR)
- **Top Global Matches:** file_cluster_17: 14.7, file_cluster_8: 14.744, file_cluster_0: 14.889
- **Magnitude:** 1291.96 | **LOC:** 2107 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 81.0%
- **Risk Profile:** Cognitive Load (65.5382%), Tech Debt (11.3559%)
**Top Internal Functions/Classes:**
  * `record_expr_field` (Impact: 37.9)
  * `impl_trait` (Impact: 22.4)
  * `ty_alias` (Impact: 20.4)
  * `item_static` (Impact: 13.9)
  * `block_expr` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 573`, `args: 130`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 550`, `orphaned_logic: 6`
* *Architecture:* `api: 103`, `import: 4`
* *Defense:* `safety: 274`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` SyntaxToken, HasArgList, HasGenericArgs, HasVisibility, HasGenericParams, either::Either, SyntaxNode, super::SyntaxFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/source_analyzer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.797 IQR)
- **Top Global Matches:** file_cluster_8: 13.797, file_cluster_17: 13.808, file_cluster_16: 13.844
- **Magnitude:** 1265.04 | **LOC:** 2014 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 45.2%
- **Risk Profile:** Cognitive Load (16.7701%), Tech Debt (96.998%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 341.1)
  * `resolve_hir_path_` (Impact: 74.5)
  * `resolve_offset_of_field` (Impact: 32.9)
  * `resolve_prefix_expr` (Impact: 31.6)
  * `resolve_record_field` (Impact: 31.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 383`, `args: 169`, `func_start: 74`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 60`, `dead_code: 5`, `fragile_debt: 12`, `duplicate_logic: 4`, `orphaned_logic: 40`
* *Architecture:* `api: 56`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 355`, `doc: 23`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smallvec::SmallVec, Local, Macro, Function, resolver_for_scope, stdx::never, resolver::Resolver, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/goto_definition.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.216 IQR)
- **Top Global Matches:** file_cluster_8: 12.216, file_cluster_0: 12.34, file_cluster_16: 12.556
- **Magnitude:** 1235.36 | **LOC:** 4103 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 26.7%
- **Risk Profile:** Cognitive Load (11.0192%), Tech Debt (11.4602%)
**Top Internal Functions/Classes:**
  * `find_definition_for_known_blanket_dual_i` (Impact: 57.2)
    * *Intent:* // If the token is into(), try_into(), search the definition of From, TryFrom.
  * `nav_for_exit_points` (Impact: 31.9)
  * `goto_question_mark_conversions` (Impact: 25.9)
    * *Intent:* /// When the `?` operator is used on `Result`, go to the `From` impl if it exists as this provides m...
  * `handle_control_flow_keywords` (Impact: 20.6)
  * `find_branch_root` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 604`, `args: 472`, `func_start: 430`, `class_start: 168`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `dead_code: 3`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 220`, `concurrency: 34`, `import: 38`
* *Defense:* `safety: 164`, `doc: 26`, `test: 168`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001655
  * `Imports (Out-Degree: 1):` crate::
    FilePosition, SyntaxToken, NavigationTarget, syntax::
    AstNode, std::iter, foo::u8, InFile, base_db::AnchoredPath...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-def/src/expr_store/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.19 IQR)
- **Top Global Matches:** file_cluster_17: 14.19, file_cluster_8: 14.393, file_cluster_0: 14.503
- **Magnitude:** 1233.52 | **LOC:** 2961 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 40.7%
- **Risk Profile:** Cognitive Load (20.7387%), Tech Debt (32.6325%)
**Top Internal Functions/Classes:**
  * `collect_pat` (Impact: 125.5)
  * `maybe_collect_expr` (Impact: 122.6)
  * `maybe_collect_expr_as_pat` (Impact: 55.1)
  * `lower_type_ref` (Impact: 36.0)
  * `lower_generic_args` (Impact: 29.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 635`, `args: 250`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 283`, `dead_code: 10`, `fragile_debt: 14`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 445`, `doc: 60`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingId, syntax::
    AstNode, TraitBoundModifier, lang_item::LangItemTarget, span_map::SpanMapRef, GenericArg, stdx::never, BlockId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/syntax/src/ast/make.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.184 IQR)
- **Top Global Matches:** file_cluster_8: 13.184, file_cluster_16: 13.248, file_cluster_13: 13.314
- **Magnitude:** 1149.58 | **LOC:** 1564 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (14.1671%), Tech Debt (93.9983%)
**Top Internal Functions/Classes:**
  * `fn_` (Impact: 50.7)
  * `impl_trait` (Impact: 47.0)
  * `item_static` (Impact: 20.8)
  * `impl_` (Impact: 18.2)
  * `hacky_block_expr` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 271`, `args: 274`, `func_start: 175`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 3`, `state_mutation: 80`, `planned_debt: 2`, `fragile_debt: 6`, `duplicate_logic: 13`
* *Architecture:* `api: 283`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 201`, `doc: 29`, `test: 9`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.887
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.02944
  * `Imports (Out-Degree: 2):` SyntaxToken, super::*, stdx::format_to, SyntaxKind::*, std::sync::LazyLock, crate::AstNode, ast::self, SourceFile...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `crates/ide/src/highlight_related.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.899 IQR)
- **Top Global Matches:** file_cluster_8: 12.899, file_cluster_0: 12.988, file_cluster_17: 13.199
- **Magnitude:** 1113.34 | **LOC:** 2552 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (16.1358%), Tech Debt (12.8582%)
**Top Internal Functions/Classes:**
  * `highlight_break_points` (Impact: 40.1)
  * `hl` (Impact: 33.2)
  * `test_hl_break_for_but_not_continue` (Impact: 32.9)
  * `test_hl_continue_for_but_not_break` (Impact: 32.9)
  * `test_hl_break_and_continue` (Impact: 31.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 324`, `args: 255`, `func_start: 185`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 123`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 89`, `concurrency: 45`, `import: 14`
* *Defense:* `safety: 183`, `doc: 3`, `test: 72`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.713
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001092
  * `Imports (Out-Degree: 1):` SyntaxToken, syntax::
    AstNode, std::iter, InFile, WalkEvent, crate::fixture, super::*, preorder_expr_with_ctx_checker...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/lower.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.554 IQR)
- **Top Global Matches:** file_cluster_0: 13.554, file_cluster_16: 13.573, file_cluster_8: 13.655
- **Magnitude:** 1068.48 | **LOC:** 2681 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 53.6%
- **Risk Profile:** Cognitive Load (10.2219%), Tech Debt (92.649%)
**Top Internal Functions/Classes:**
  * `resolve_type_param_assoc_type_shorthand` (Impact: 87.8)
  * `lower_dyn_trait` (Impact: 74.0)
    * *Intent:* // Don't lower associated type bindings as the only possible relaxed trait bound // `?Sized` has no ...
  * `generic_predicates` (Impact: 51.6)
  * `query` (Impact: 25.9)
  * `supertraits_info` (Impact: 25.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 575`, `args: 195`, `func_start: 110`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 178`, `dead_code: 9`, `fragile_debt: 22`, `duplicate_logic: 8`, `orphaned_logic: 26`
* *Architecture:* `api: 99`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 222`, `doc: 93`, `test: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` smallvec::SmallVec, TypeAliasFlags, TraitBoundModifier, EnumId, LifetimeNs, GenericArg, TypeVisitableExt, ConstKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/test-utils/src/minicore.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.187 IQR)
- **Top Global Matches:** file_cluster_0: 13.187, file_cluster_16: 13.234, file_cluster_13: 13.475
- **Magnitude:** 1062.02 | **LOC:** 2234 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (23.5804%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `drop` (Impact: 23.1)
  * `async_call_once` (Impact: 14.1)
  * `call_once` (Impact: 13.6)
  * `borrow_mut` (Impact: 9.2)
  * `const_panic_fmt` (Impact: 8.4)
    * *Intent:* // This function is used instead of panic_fmt in const eval.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 506`, `args: 165`, `func_start: 165`, `class_start: 100`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 162`, `planned_debt: 4`, `duplicate_logic: 105`
* *Architecture:* `api: 283`, `concurrency: 85`, `import: 47`
* *Defense:* `safety: 141`, `doc: 84`, `immutability_locks: 88`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PointeeSized, Poll, super::*, FromResidual, RangeFull, self::unsize::CoerceUnsized, IntoIterator, AsyncFnMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.109 IQR)
- **Top Global Matches:** file_cluster_0: 14.109, file_cluster_16: 14.205, file_cluster_8: 14.31
- **Magnitude:** 1032.74 | **LOC:** 4368 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 30.6%
- **Risk Profile:** Cognitive Load (4.4013%), Tech Debt (93.8612%)
**Top Internal Functions/Classes:**
  * `apply_change_with_sink` (Impact: 47.0)
    * *Intent:* /// Show experimental rust-analyzer diagnostics that might have more false positives than
  * `inlay_hints` (Impact: 23.8)
    * *Intent:* // references
  * `lens` (Impact: 21.7)
  * `cargo` (Impact: 19.8)
  * `flycheck` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 381`, `args: 206`, `func_start: 140`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 131`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 6`, `duplicate_logic: 31`
* *Architecture:* `api: 234`, `import: 24`
* *Defense:* `safety: 386`, `doc: 677`, `test: 28`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CfgDiff, ide::
    AnnotationConfig, GotoImplementationConfig, AssistConfig, WorkspaceSymbolSearchScope, HoverConfig, de::DeserializeOwned, SnippetScope...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/rename.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.603 IQR)
- **Top Global Matches:** file_cluster_8: 11.603, file_cluster_0: 11.655, file_cluster_13: 11.929
- **Magnitude:** 1030.28 | **LOC:** 3934 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (10.4149%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `no_type_value_ns_confuse` (Impact: 94.2)
  * `transform_method_call_into_assoc_fn` (Impact: 52.9)
  * `transform_assoc_fn_into_method_call` (Impact: 43.8)
  * `rename` (Impact: 36.1)
    * *Intent:* // Feature: Rename // // Renames the item below the cursor and all of its references // // | Editor ...
  * `rename_to_self` (Impact: 33.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 508`, `args: 376`, `func_start: 292`, `class_start: 88`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 2`, `state_mutation: 89`, `dead_code: 10`, `fragile_debt: 13`, `duplicate_logic: 105`
* *Architecture:* `api: 95`, `import: 41`
* *Defense:* `safety: 146`, `doc: 9`, `test: 108`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syntax::
    AstNode, HasArgList, super::RangeInfo, InFile, crate::fixture, RenameError, super::X, crate::foo::Foo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval/shim.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.259 IQR)
- **Top Global Matches:** file_cluster_8: 12.259, file_cluster_17: 12.622, file_cluster_13: 12.698
- **Magnitude:** 996.44 | **LOC:** 1525 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (16.9361%), Tech Debt (48.6416%)
**Top Internal Functions/Classes:**
  * `exec_intrinsic` (Impact: 453.1)
  * `exec_extern_c` (Impact: 124.2)
  * `exec_atomic_intrinsic` (Impact: 99.8)
  * `exec_lang_item` (Impact: 51.2)
  * `exec_alloc_fn` (Impact: 48.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 472`, `args: 46`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 39`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 14`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 228`, `doc: 4`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mir::eval::
        Address, intern::sym, pad16, hir_def::attrs::AttrFlags, MirEvalError, signatures::FunctionSignature, IntervalOrOwned, Locals...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/tests/simple.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.338 IQR)
- **Top Global Matches:** file_cluster_16: 12.338, file_cluster_8: 12.4, file_cluster_0: 12.511
- **Magnitude:** 989.48 | **LOC:** 4151 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 63.2%
- **Risk Profile:** Cognitive Load (6.951%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `infer_field_autoderef` (Impact: 41.8)
  * `foo` (Impact: 23.2)
  * `infer_binary_op` (Impact: 19.8)
  * `f` (Impact: 18.5)
  * `foo` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 713`, `args: 418`, `func_start: 314`, `class_start: 116`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 225`, `fragile_debt: 4`, `duplicate_logic: 122`, `orphaned_logic: 32`
* *Architecture:* `api: 19`, `concurrency: 28`, `import: 18`
* *Defense:* `safety: 198`, `doc: 1`, `test: 173`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::a::*, DerefMut, core::ops::Deref, expect_test::expect, super::proc_macro, super::b::foo, Option::*, check_no_mismatches...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-def/src/resolver.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.558 IQR)
- **Top Global Matches:** file_cluster_16: 13.558, file_cluster_8: 13.633, file_cluster_0: 13.657
- **Magnitude:** 983.12 | **LOC:** 1477 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 58.8%
- **Risk Profile:** Cognitive Load (10.2794%), Tech Debt (99.8488%)
**Top Internal Functions/Classes:**
  * `rename_will_conflict_with_renamed` (Impact: 270.0)
  * `resolve_path_in_value_ns_with_prefix_inf` (Impact: 88.5)
  * `resolve_path_in_type_ns_with_prefix_info` (Impact: 54.1)
  * `rename_will_conflict_with_another_variab` (Impact: 38.3)
  * `process_names` (Impact: 22.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 251`, `args: 124`, `func_start: 78`, `class_start: 12`
* *Risk/State:* `state_mutation: 86`, `dead_code: 3`, `fragile_debt: 6`, `duplicate_logic: 27`
* *Architecture:* `api: 66`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 222`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smallvec::SmallVec, BuiltinShadowMode, EnumId, lang_item::LangItemTarget, ExprId, FunctionId, intern::Symbol, ExternBlockId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/infer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.513 IQR)
- **Top Global Matches:** file_cluster_16: 14.513, file_cluster_0: 14.646, file_cluster_13: 14.662
- **Magnitude:** 973.42 | **LOC:** 2254 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 48.9%
- **Risk Profile:** Cognitive Load (11.5652%), Tech Debt (99.9535%)
**Top Internal Functions/Classes:**
  * `resolve_variant` (Impact: 245.8)
  * `struct_tail_with_normalize` (Impact: 24.8)
  * `collect_fn` (Impact: 18.5)
  * `infer_query_with_inspect` (Impact: 16.4)
  * `make_ty` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 348`, `args: 170`, `func_start: 117`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 170`, `dead_code: 5`, `fragile_debt: 30`, `duplicate_logic: 4`, `orphaned_logic: 59`
* *Architecture:* `api: 75`, `import: 21`
* *Defense:* `safety: 268`, `doc: 230`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BindingId, CapturedItemWithoutTy, GenericArg, layout::Integer, stdx::never, LocalFieldId, StaticSignature, IncorrectGenericsLenKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/hir-ty/src/diagnostics/decl_check/case_conv.rs` (RUST) | Magnitude: 42.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, safety_bypasses: 37, structural_boundaries: 14, safety: 13
- `crates/hir-ty/src/upvars.rs` (RUST) | Magnitude: 240.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 244, structural_boundaries: 62, state_mutation: 42, args: 34
- `crates/ide/src/folding_ranges.rs` (RUST) | Magnitude: 397.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 659, structural_boundaries: 127, safety: 120, branch: 111
- `crates/ide-assists/src/handlers/remove_parentheses.rs` (RUST) | Magnitude: 212.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 316, args: 126, branch: 82, structural_boundaries: 82
- `crates/ide-diagnostics/src/handlers/unlinked_file.rs` (RUST) | Magnitude: 190.92 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 323, structural_boundaries: 117, branch: 60, safety: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/parser/src/grammar/items.rs` (RUST) | Magnitude: 287.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 302, structural_boundaries: 76, branch: 73, state_mutation: 47
- `crates/parser/src/grammar/items/traits.rs` (RUST) | Magnitude: 60.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 26, branch: 19, generics: 16
- `crates/parser/src/grammar/expressions/atom.rs` (RUST) | Magnitude: 523.22 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 601, branch: 232, structural_boundaries: 124, dead_code: 100
- `crates/hir-ty/src/infer/coerce.rs` (RUST) | Magnitude: 247.98 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, doc: 157, structural_boundaries: 70, generics: 50
- `crates/parser/src/grammar/items/adt.rs` (RUST) | Magnitude: 131.82 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 37, branch: 31, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/rust-analyzer/src/cli/run_tests.rs` (RUST) | Magnitude: 45.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 37, state_mutation: 19, safety: 14
- `crates/proc-macro-srv/src/dylib.rs` (RUST) | Magnitude: 92.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 40, doc: 30, generics: 27
- `crates/mbe/src/expander.rs` (RUST) | Magnitude: 31.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 67, indent_spaces: 51, structural_boundaries: 19, generics: 15
- `xtask/src/codegen/feature_docs.rs` (RUST) | Magnitude: 55.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 25, branch: 14, safety: 11
- `crates/hir-expand/src/eager.rs` (RUST) | Magnitude: 110.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 226, structural_boundaries: 50, safety: 39, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/tt/src/storage.rs` (RUST) | Magnitude: 330.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 459, structural_boundaries: 107, state_mutation: 102, generics: 58
- `crates/hir-ty/src/tests/patterns.rs` (RUST) | Magnitude: 289.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1010, generics: 301, structural_boundaries: 156, safety: 115
- `crates/syntax/src/ast/syntax_factory.rs` (RUST) | Magnitude: 19.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, doc: 11, args: 8, safety: 7
- `xtask/src/codegen/lints.rs` (RUST) | Magnitude: 188.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 435, structural_boundaries: 128, safety: 55, branch: 48
- `crates/hir-ty/src/lib.rs` (RUST) | Magnitude: 348.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 460, structural_boundaries: 110, branch: 95, generics: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/project-model/src/toolchain_info/target_tuple.rs` (RUST) | Magnitude: 48.08 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, safety: 41, structural_boundaries: 33, branch: 15
- `xtask/src/codegen/grammar.rs` (RUST) | Magnitude: 649.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 996, structural_boundaries: 253, args: 142, branch: 141
- `crates/ide-db/src/imports/merge_imports.rs` (RUST) | Magnitude: 432.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 335, structural_boundaries: 116, branch: 91, state_mutation: 91
- `crates/ide-completion/src/snippet.rs` (RUST) | Magnitude: 35.02 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, safety: 13, structural_boundaries: 12, args: 9
- `crates/ide/src/hover/render.rs` (RUST) | Magnitude: 832.32 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1246, structural_boundaries: 318, safety: 312, branch: 250

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/rust-analyzer/src/command.rs` (RUST) | Magnitude: 95.58 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 35, concurrency: 34, generics: 26
- `crates/ide-assists/src/handlers/unnecessary_async.rs` (RUST) | Magnitude: 184.22 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, args: 66, concurrency: 51, structural_boundaries: 48
- `crates/ide-diagnostics/src/handlers/expected_function.rs` (RUST) | Magnitude: 41.54 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, concurrency: 31, structural_boundaries: 18, args: 8
- `editors/code/src/dependencies_provider.ts` (TYPESCRIPT) | Magnitude: 16.02 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 69, structural_boundaries: 41, concurrency: 20
- `crates/hir-ty/src/mir/lower/tests.rs` (RUST) | Magnitude: 66.3 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 38, branch: 13, concurrency: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/vfs/src/anchored_path.rs` (RUST) | Magnitude: 16.12 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, api: 3, encapsulation: 3, sec_high_risk_execution: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/hir-ty/src/mir/eval/tests.rs` (RUST) | Magnitude: 377.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 216, args: 135, func_start: 117
- `crates/hir-ty/src/tests/method_resolution.rs` (RUST) | Magnitude: 592.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 827, structural_boundaries: 355, bitwise_ops: 274, args: 266
- `crates/hir-ty/src/layout/target.rs` (RUST) | Magnitude: 26.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, safety: 15, branch: 10, structural_boundaries: 6
- `crates/ide-assists/src/handlers/move_module_to_file.rs` (RUST) | Magnitude: 53.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 93, args: 40, func_start: 35
- `crates/proc-macro-srv/src/server_impl.rs` (RUST) | Magnitude: 19.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, doc: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/parser/src/grammar/items/use_item.rs` (RUST) | Magnitude: 43.18 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, dead_code: 22, structural_boundaries: 17, branch: 13
- `crates/parser/src/grammar/patterns.rs` (RUST) | Magnitude: 254.62 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 98, dead_code: 92, state_mutation: 51

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/hir/src/lib.rs` -> Churn: **100.0%** | Cog Load: 7.7457% | Debt: 99.997%
- `crates/hir-ty/src/next_solver/interner.rs` -> Churn: **92.18%** | Cog Load: 12.0425% | Debt: 99.9433%
- `crates/hir-ty/src/lower.rs` -> Churn: **90.3%** | Cog Load: 10.2219% | Debt: 92.649%
- `crates/hir-ty/src/infer.rs` -> Churn: **86.46%** | Cog Load: 11.5652% | Debt: 99.9535%
- `crates/hir-ty/src/display.rs` -> Churn: **85.51%** | Cog Load: 6.1262% | Debt: 99.9997%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ide-completion/src/context/analysis.rs` -> **A4-Tacks** (82.5% isolated ownership) | Magnitude: 1410.42
- `crates/syntax/src/ast/syntax_factory/constructors.rs` -> **bit-aloo** (81.0% isolated ownership) | Magnitude: 1291.96
- `crates/syntax/src/ast/make.rs` -> **A4-Tacks** (87.5% isolated ownership) | Magnitude: 1149.58
- `crates/ide-assists/src/handlers/move_guard.rs` -> **A4-Tacks** (90.0% isolated ownership) | Magnitude: 611.32
- `crates/hir-def/src/find_path.rs` -> **Lukas Wirth** (100.0% isolated ownership) | Magnitude: 598.28

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `editors/code/src/ctx.ts` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 100.0%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 48.8964%)
- `crates/syntax/src/ted.rs` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 97.0181%)
- `editors/code/src/run.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 43.8167%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/syntax/src/ast.rs` -> **Severity: 5.916** (Embedded: 0.068 * Error Risk: 87.0118%)
- `crates/ide-completion/src/tests/use_tree.rs` -> **Severity: 1.157** (Embedded: 0.0165 * Error Risk: 70.1341%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 0.697** (Embedded: 0.0294 * Error Risk: 23.6706%)
- `editors/code/src/ctx.ts` -> **Severity: 0.554** (Embedded: 0.0058 * Error Risk: 95.0684%)
- `editors/code/src/dependencies_provider.ts` -> **Severity: 0.308** (Embedded: 0.0033 * Error Risk: 92.569%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/syntax/src/ast.rs` -> **Severity: 3258.691** (Blast Radius: 53.45 * Doc Risk: 60.9671%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 1988.7** (Blast Radius: 19.887 * Doc Risk: 100.0%)
- `crates/tt/src/iter.rs` -> **Severity: 1023.8** (Blast Radius: 10.238 * Doc Risk: 100.0%)
- `editors/code/src/lsp_ext.ts` -> **Severity: 797.0** (Blast Radius: 7.97 * Doc Risk: 100.0%)
- `crates/syntax/src/algo.rs` -> **Severity: 515.0** (Blast Radius: 5.15 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
