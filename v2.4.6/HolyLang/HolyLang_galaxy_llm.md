# ARCHITECTURAL_BRIEF: HolyLang
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/HolyLang` |
| **Timestamp** | `2026-08-03T19:06:19.281929+00:00` |
| **Scan Duration** | `0.61s` |
| **Git Branch** | `main` |
| **Git Commit** | `48d8b0cf55e60b0aa77de02b9464d35a69a797b7` |
| **Git Remote** | `https://github.com/chadsec1/HolyLang` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 103 malicious artifacts.

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
| Total Artifacts | 111 |
| Analyzed Artifacts (Scanned) | 104 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 23016 |
| Volatility Index | 0.048 |
| % Scanned of codebase = | 93.7% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 103 | 23016 | 99.0% |
| MARKDOWN | 1 | 0 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.64`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 81 | 77.9% |
| file_cluster_17 | 10 | 9.6% |
| file_cluster_0 | 7 | 6.7% |
| file_cluster_13 | 3 | 2.9% |
| file_cluster_16 | 1 | 1.0% |
| file_cluster_6 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.toml`: 1x Unsupported Format (.toml)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 43.9 | 14.2 | 13.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 96.9 | 27.9 | 25.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 84.2 | 96.8 | 0.0 |
| Testing Exposure | 0.8 | 80.0 | 30.3 | 2.5 | 80.0 |
| API Exposure | 0.0 | 8.4 | 0.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 40.5 | 21.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.6 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 98.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 15.5 | 3.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Documentation Exposure | 4.8 | 100.0 | 75.8 | 100.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 26.7 | 3.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 11.2 | 19.8 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/compile.rs` (Hits: 4)
- `src/main.rs` (Hits: 1)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **ast.rs** (`src/ast.rs`) — 0 inbound connections
3. **exprs.rs** (`src/ast/exprs.rs`) — 0 inbound connections
4. **fmt_display.rs** (`src/ast/fmt_display.rs`) — 0 inbound connections
5. **fmt_display_tests.rs** (`src/ast/fmt_display_tests.rs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blackbox_tests.rs** (`src/semantic/blackbox_tests.rs`) — 37 outbound dependencies
2. **transpiler.rs** (`src/transpiler.rs`) — 11 outbound dependencies
3. **semantic.rs** (`src/semantic.rs`) — 10 outbound dependencies
4. **compile.rs** (`src/compile.rs`) — 9 outbound dependencies
5. **branch_analysis_tests.rs** (`src/semantic/branch_analysis_tests.rs`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `find_top_level_op_any` (@ `src/parser/helpers.rs`) -> Impact: **1433.0** | LOC: 379
- `eval_const_expr_and_fold_it_hazmat` (@ `src/semantic/constants.rs`) -> Impact: **1156.2** | LOC: 444
  * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call this function directly unless you 1000% know what yo...
- `parse_block` (@ `src/parser.rs`) -> Impact: **1048.2** | LOC: 352
- `return_branch_analysis` (@ `src/semantic/branch_analysis.rs`) -> Impact: **979.3** | LOC: 177
- `transpile_stmt` (@ `src/transpiler.rs`) -> Impact: **454.4** | LOC: 207
  * *Intent:* /// Transpiles a statement into equivlent Rust code ///
- `parse_expr` (@ `src/parser/parse_expr.rs`) -> Impact: **382.7** | LOC: 136
  * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary operations (like negate, logical not, bitwise not ) ///...
- `dead_code_analysis` (@ `src/semantic/branch_analysis.rs`) -> Impact: **358.1** | LOC: 129
- `holy_expr_to_rust_expr` (@ `src/transpiler.rs`) -> Impact: **237.3** | LOC: 146
  * *Intent:* /// Turns a HolyLang expression, into equvilent Rust expression ///
- `if_statements_trailing_kw_errors` (@ `src/parser/blackbox_tests/if_stmt_tests.rs`) -> Impact: **211.1** | LOC: 65
- `if_statements_invalid_construction_error` (@ `src/parser/blackbox_tests/if_stmt_tests.rs`) -> Impact: **208.5** | LOC: 83

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parse_block` (@ `src/parser.rs`) -> **O(2^N) [Recursive]**
- `find_top_level_op_any` (@ `src/parser/helpers.rs`) -> **O(2^N) [Recursive]**
- `parse_expr` (@ `src/parser/parse_expr.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary operations (like negate, logical not, bitwise not ) ///...
- `return_branch_analysis` (@ `src/semantic/branch_analysis.rs`) -> **O(2^N) [Recursive]**
- `dead_code_analysis` (@ `src/semantic/branch_analysis.rs`) -> **O(2^N) [Recursive]**
- `eval_const_expr_and_fold_it_hazmat` (@ `src/semantic/constants.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call this function directly unless you 1000% know what yo...
- `fixed_array_to_dynamic_array_type_full` (@ `src/ast/types.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Converts a fixed_array into dynamic array, and walks recursively into fixed_array type and /// does the same. ///
- `get_default_value` (@ `src/ast/types.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* // When variable is declared, e.g. // own VAR_NAME TYPE_NAME // // It has no value. So parser has to assign it a value. // Parser must use TYPE.get_de...
- `transpile_stmt` (@ `src/transpiler.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Transpiles a statement into equivlent Rust code ///
- `is_fully_fixed_array_type` (@ `src/ast/types.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `find_top_level_op_any` (@ `src/parser/helpers.rs`) -> DB Complexity: **17**
- `transpile_stmt` (@ `src/transpiler.rs`) -> DB Complexity: **15**
  * *Intent:* /// Transpiles a statement into equivlent Rust code ///
- `compile` (@ `src/compile.rs`) -> DB Complexity: **9**
- `parse_block` (@ `src/parser.rs`) -> DB Complexity: **8**
- `test_whitespace_and_newlines_errors` (@ `src/parser/parse_expr_tests.rs`) -> DB Complexity: **6**
- `test_non_boolean_binop_logical_errors` (@ `src/semantic/blackbox_tests/bin_op_tests.rs`) -> DB Complexity: **6**
  * *Intent:* // Non boolean left or right with logical "AND" or "OR" should error
- `test_dynmaic_array_element_type_mismatch` (@ `src/semantic/blackbox_tests/dyn_array_tests.rs`) -> DB Complexity: **6**
  * *Intent:* // Invalid array construction (element types mismatch)
- `with_literal_size_element_type_mismatch_` (@ `src/semantic/blackbox_tests/fixed_array_tests.rs`) -> DB Complexity: **6**
- `test_for_statements_with_dyn_array_holde` (@ `src/semantic/blackbox_tests/for_stmt_tests.rs`) -> DB Complexity: **6**
- `multi_assign_locked_vars_errors` (@ `src/semantic/blackbox_tests/locking_unlocking_tests.rs`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/parser/blackbox_tests` | 27 | 12910.0 | 15.98% | 96.46% |
| `src/semantic/blackbox_tests` | 29 | 7450.12 | 15.88% | 85.61% |
| `src/semantic` | 7 | 3312.16 | 12.03% | 93.93% |
| `src` | 10 | 2418.42 | 13.85% | 45.79% |
| `src/parser` | 5 | 2338.7 | 13.69% | 64.94% |
| `src/parser/parse_expr_tests` | 14 | 1377.5 | 13.28% | 97.63% |
| `src/ast` | 9 | 966.26 | 9.16% | 64.79% |
| `src/semantic/branch_analysis_tests` | 2 | 838.76 | 7.38% | 99.77% |
| `__monolith__` | 1 | 4.9 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/ast/int_literal_value_tests.rs` -> **100.0%** Exposure
- `src/parser/blackbox_tests/break_stmt_tests.rs` -> **100.0%** Exposure
- `src/semantic.rs` -> **100.0%** Exposure
- `src/semantic/infer.rs` -> **100.0%** Exposure
- `src/ast/int_literal_value.rs` -> **99.9995%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/semantic/blackbox_tests/int_literals_internal_inference_tests.rs` -> **99.9986%** Exposure
- `src/parser/parse_expr_tests/int_literal_tests.rs` -> **99.812%** Exposure
- `src/lib.rs` -> **99.7916%** Exposure
- `src/semantic.rs` -> **99.7786%** Exposure
- `src/error.rs` -> **99.6316%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/semantic/blackbox_tests/const_tests.rs` -> **111** Orphaned Functions | **0** Duplicates
- `src/parser/helpers_tests.rs` -> **55** Orphaned Functions | **0** Duplicates
- `src/semantic/blackbox_tests/ownership_tests.rs` -> **35** Orphaned Functions | **11** Duplicates
- `src/parser/blackbox_tests/while_stmt_tests.rs` -> **37** Orphaned Functions | **6** Duplicates
- `src/semantic/blackbox_tests/locking_unlocking_tests.rs` -> **41** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/consts.rs`** -> AI Confidence: **99.29%**
2. **`src/parser/blackbox_tests/for_stmt_tests.rs`** -> AI Confidence: **99.29%**
3. **`src/parser/parse_expr_tests/format_call_tests.rs`** -> AI Confidence: **99.29%**
4. **`src/transpiler.rs`** -> AI Confidence: **99.24%**
5. **`src/semantic/blackbox_tests.rs`** -> AI Confidence: **99.18%**
6. **`src/parser/blackbox_tests/bin_op_tests.rs`** -> AI Confidence: **99.17%**
7. **`src/parser/blackbox_tests/break_stmt_tests.rs`** -> AI Confidence: **99.17%**
8. **`src/parser/blackbox_tests/continue_stmt_tests.rs`** -> AI Confidence: **99.17%**
9. **`src/parser/blackbox_tests/if_stmt_tests.rs`** -> AI Confidence: **99.17%**
10. **`src/parser/blackbox_tests/while_stmt_tests.rs`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/ast/types_tests.rs` -> **20.0%** Exposure
- `src/parser.rs` -> **20.0%** Exposure
- `src/parser/blackbox_tests/array_slicing_tests.rs` -> **20.0%** Exposure
- `src/parser/blackbox_tests/bin_op_tests.rs` -> **20.0%** Exposure
- `src/parser/blackbox_tests/break_stmt_tests.rs` -> **20.0%** Exposure
### Raw Memory Manipulation
- `src/ast/types_tests.rs` -> **0.001%** Exposure
- `src/semantic/blackbox_tests/const_tests.rs` -> **0.0005%** Exposure
- `src/parser/blackbox_tests/bin_op_tests.rs` -> **0.0002%** Exposure
- `src/semantic/blackbox_tests/dyn_array_slicing_tests.rs` -> **0.0002%** Exposure
- `src/semantic/blackbox_tests/bin_op_tests.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `src/compile.rs` -> **100.0%** Exposure
- `src/parser.rs` -> **100.0%** Exposure
- `src/parser/helpers.rs` -> **100.0%** Exposure
- `src/parser/parse_expr.rs` -> **100.0%** Exposure
- `src/semantic/infer.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `217` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/transpiler.rs` (RUST) -> Cumulative Risk: **712.11**
- **Archetype:** `file_cluster_8` (Distance: 11.371 IQR)
- **Magnitude:** 852.96 | **LOC:** 492 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (98.1645%), Tech Debt (96.5074%)
- **Heaviest Functions:** `transpile_stmt` (Impact: 454.4), `holy_expr_to_rust_expr` (Impact: 237.3), `transpile_function` (Impact: 47.6)

### 2. `src/semantic/blackbox_tests/locking_unlocking_tests.rs` (RUST) -> Cumulative Risk: **662.89**
- **Archetype:** `file_cluster_8` (Distance: 10.111 IQR)
- **Magnitude:** 523.8 | **LOC:** 875 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9928%), Tech Debt (94.7586%)
- **Heaviest Functions:** `multi_assign_locked_vars_errors` (Impact: 22.1), `unlock_func_arg_in_while_loop_errors` (Impact: 19.3), `lock_func_arg_in_while_loop_errors` (Impact: 19.3)

### 3. `src/semantic/branch_analysis.rs` (RUST) -> Cumulative Risk: **657.15**
- **Archetype:** `file_cluster_8` (Distance: 10.674 IQR)
- **Magnitude:** 1349.76 | **LOC:** 316 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9962%), Tech Debt (98.7639%)
- **Heaviest Functions:** `return_branch_analysis` (Impact: 979.3), `dead_code_analysis` (Impact: 358.1)

### 4. `src/semantic/blackbox_tests/int_literals_internal_inference_tests.rs` (RUST) -> Cumulative Risk: **634.33**
- **Archetype:** `file_cluster_0` (Distance: 12.428 IQR)
- **Magnitude:** 263.5 | **LOC:** 474 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9986%), Tech Debt (99.6827%)
- **Heaviest Functions:** `test_integer_literal_out_of_range_for_by` (Impact: 18.5), `test_integer_literal_out_of_range_for_ui` (Impact: 18.5), `test_integer_literal_out_of_range_for_ui` (Impact: 18.5)

### 5. `src/compile.rs` (RUST) -> Cumulative Risk: **627.41**
- **Archetype:** `file_cluster_13` (Distance: 9.086 IQR)
- **Magnitude:** 30.36 | **LOC:** 62 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Safety Score (96.8967%)
- **Heaviest Functions:** `compile` (Impact: 23.4)

### 6. `src/semantic/infer.rs` (RUST) -> Cumulative Risk: **612.55**
- **Archetype:** `file_cluster_6` (Distance: 14.903 IQR)
- **Magnitude:** 196.22 | **LOC:** 775 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (80.1087%)
- **Heaviest Functions:** `infer_expr_type` (Impact: 111.7), `advanced_infer_2_types` (Impact: 69.2)

### 7. `src/ast/types.rs` (RUST) -> Cumulative Risk: **604.34**
- **Archetype:** `file_cluster_8` (Distance: 10.231 IQR)
- **Magnitude:** 208.28 | **LOC:** 190 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9995%), Tech Debt (98.0069%)
- **Heaviest Functions:** `is_fully_fixed_array_type` (Impact: 44.0), `get_array_inner_most_type` (Impact: 44.0), `fixed_array_to_dynamic_array_type_full` (Impact: 42.6)

### 8. `src/semantic/blackbox_tests/const_tests.rs` (RUST) -> Cumulative Risk: **602.83**
- **Archetype:** `file_cluster_0` (Distance: 12.581 IQR)
- **Magnitude:** 1268.62 | **LOC:** 2269 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), State Flux (98.1572%), Tech Debt (96.8227%)
- **Heaviest Functions:** `const_evaluated_logical_and_with_equal_c` (Impact: 69.2), `const_evaluated_numeric_comparison` (Impact: 64.0), `const_all_arth_binop_on_literals` (Impact: 59.2)

### 9. `src/semantic/blackbox_tests/multi_return_tests.rs` (RUST) -> Cumulative Risk: **594.6**
- **Archetype:** `file_cluster_17` (Distance: 9.704 IQR)
- **Magnitude:** 385.72 | **LOC:** 880 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.4657%), State Flux (88.329%)
- **Heaviest Functions:** `multi_return_assign` (Impact: 50.7), `test_multi_return_assign_type_mismatch_e` (Impact: 35.1), `test_multi_return_decl_correct` (Impact: 32.3)

### 10. `src/semantic/blackbox_tests/var_assign_tests.rs` (RUST) -> Cumulative Risk: **590.98**
- **Archetype:** `file_cluster_8` (Distance: 10.08 IQR)
- **Magnitude:** 98.22 | **LOC:** 141 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.1653%), State Flux (95.7598%)
- **Heaviest Functions:** `test_varassign` (Impact: 29.2), `test_varassign_type_mismatch_errors` (Impact: 14.0), `test_varassign_local_const_errors` (Impact: 7.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/parser/blackbox_tests/while_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.305 IQR)
- **Top Global Matches:** file_cluster_8: 11.305, file_cluster_0: 11.495, file_cluster_17: 11.679
- **Magnitude:** 2411.9 | **LOC:** 1181 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (36.1018%), Tech Debt (96.4772%)
**Top Internal Functions/Classes:**
  * `invalid_construction_errors` (Impact: 208.5 | O(N^3))
  * `invalid_construction_errors` (Impact: 205.0 | O(N^3))
  * `trailing_kw_errors` (Impact: 152.0 | O(N^3))
  * `vars_and_literals_spaces_before_expr` (Impact: 148.3 | O(N^6) | DB: 1)
    * *Intent:* // Same test as above, but before the expression, there is an `i` of spaces.
  * `vars_and_literals_spaces_after_expr` (Impact: 148.2 | O(N^6) | DB: 1)
    * *Intent:* // Same test as above, but after the expression, there is an `i` of spaces.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 147`, `args: 45`, `func_start: 43`
* *Risk/State:* `state_mutation: 48`, `duplicate_logic: 6`, `orphaned_logic: 37`
* *Architecture:* `import: 3`
* *Defense:* `safety: 67`, `test: 148`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/if_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.963 IQR)
- **Top Global Matches:** file_cluster_8: 10.963, file_cluster_0: 11.398, file_cluster_17: 11.475
- **Magnitude:** 1933.7 | **LOC:** 878 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (28.3367%), Tech Debt (69.1741%)
**Top Internal Functions/Classes:**
  * `if_statements_trailing_kw_errors` (Impact: 211.1 | O(N^4))
  * `if_statements_invalid_construction_error` (Impact: 208.5 | O(N^3))
  * `if_statements_with_elif_vars_and_literal` (Impact: 186.4 | O(N^5))
  * `if_statements_vars_and_literals` (Impact: 122.4 | O(N^5))
  * `if_statements_with_else_elif` (Impact: 101.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 120`, `args: 24`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `orphaned_logic: 22`
* *Architecture:* `import: 2`
* *Defense:* `safety: 78`, `test: 167`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/bin_op_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.468 IQR)
- **Top Global Matches:** file_cluster_8: 10.468, file_cluster_0: 10.974, file_cluster_17: 11.071
- **Magnitude:** 1791.46 | **LOC:** 1078 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.8591%), Tech Debt (88.035%)
**Top Internal Functions/Classes:**
  * `vars_and_unsigned_integer_literals_mixed` (Impact: 174.6 | O(N^6))
  * `vars_and_signed_integer_literals_mixed_i` (Impact: 173.8 | O(N^6))
  * `vars_and_signed_integer_literals_mixed` (Impact: 173.2 | O(N^6))
  * `unsigned_literals_only_in_var_decl` (Impact: 130.9 | O(N^6))
  * `unsigned_literals_only` (Impact: 130.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 108`, `args: 34`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 17`, `duplicate_logic: 2`, `orphaned_logic: 32`
* *Architecture:* `import: 3`
* *Defense:* `safety: 46`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/ownership_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.435 IQR)
- **Top Global Matches:** file_cluster_8: 11.435, file_cluster_17: 11.605, file_cluster_0: 11.686
- **Magnitude:** 1760.66 | **LOC:** 1733 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (14.6312%), Tech Debt (87.7683%)
**Top Internal Functions/Classes:**
  * `vardecl_in_if_else_branch_moves_upstream` (Impact: 106.2 | O(N^6) | DB: 2)
  * `vardecl_in_if_main_branch_does_not_move_` (Impact: 106.1 | O(N^6) | DB: 2)
  * `vardecl_in_if_elif_branch_moves_upstream` (Impact: 106.1 | O(N^6) | DB: 2)
  * `test_vardecl_moving_local_var_in_for_loo` (Impact: 93.5 | O(N^6) | DB: 2)
  * `vardecl_moving_local_var_in_if_stmt_elif` (Impact: 87.7 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 415`, `args: 46`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 96`, `duplicate_logic: 11`, `orphaned_logic: 35`
* *Architecture:* `import: 2`
* *Defense:* `safety: 102`, `doc: 5`, `test: 330`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/helpers.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.031 IQR)
- **Top Global Matches:** file_cluster_17: 14.031, file_cluster_0: 14.328, file_cluster_13: 14.348
- **Magnitude:** 1496.0 | **LOC:** 427 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (24.0226%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `find_top_level_op_any` (Impact: 1433.0 | O(2^N) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 70`, `args: 32`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `dead_code: 4`, `fragile_debt: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 94`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, crate::consts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/branch_analysis.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.674 IQR)
- **Top Global Matches:** file_cluster_8: 10.674, file_cluster_0: 11.064, file_cluster_17: 11.103
- **Magnitude:** 1349.76 | **LOC:** 316 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (24.1076%), Tech Debt (98.7639%)
**Top Internal Functions/Classes:**
  * `return_branch_analysis` (Impact: 979.3 | O(2^N))
  * `dead_code_analysis` (Impact: 358.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 44`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `dead_code: 2`, `fragile_debt: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.668 IQR)
- **Top Global Matches:** file_cluster_17: 11.668, file_cluster_8: 11.872, file_cluster_0: 11.949
- **Magnitude:** 1340.26 | **LOC:** 905 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (24.5973%), Tech Debt (96.4393%)
**Top Internal Functions/Classes:**
  * `parse_block` (Impact: 1048.2 | O(2^N) | DB: 8)
  * `parse_function` (Impact: 153.4 | O(N^4) | DB: 4)
    * *Intent:* /// Parse function starting at index `start_i`. /// Returns (Function, index after function end).
  * `parse` (Impact: 62.0 | O(N^4) | DB: 2)
    * *Intent:* /// Public parse entry
  * `parse_const_stmt` (Impact: 25.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 167`, `args: 23`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 9`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 55`, `doc: 9`, `test: 3`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ast::*, crate::error::HolyError
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/const_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.581 IQR)
- **Top Global Matches:** file_cluster_0: 12.581, file_cluster_8: 12.718, file_cluster_17: 12.867
- **Magnitude:** 1268.62 | **LOC:** 2269 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (30.482%), Tech Debt (96.8227%)
**Top Internal Functions/Classes:**
  * `const_evaluated_logical_and_with_equal_c` (Impact: 69.2 | O(N^6) | DB: 2)
  * `const_evaluated_numeric_comparison` (Impact: 64.0 | O(N^5) | DB: 2)
    * *Intent:* // This includes greater than/ less than
  * `const_all_arth_binop_on_literals` (Impact: 59.2 | O(N^5) | DB: 2)
  * `const_evaluated_equal_comparison` (Impact: 53.6 | O(N^5) | DB: 2)
  * `array_out_of_bounds_access_on_fixed_arra` (Impact: 38.1 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 853`, `args: 114`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 111`, `high_risk_execution: 4`, `state_mutation: 299`, `orphaned_logic: 111`
* *Architecture:* `import: 6`
* *Defense:* `safety: 225`, `test: 378`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/constants.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.307 IQR)
- **Top Global Matches:** file_cluster_8: 11.307, file_cluster_16: 11.645, file_cluster_7: 11.762
- **Magnitude:** 1214.62 | **LOC:** 692 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.0221%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `eval_const_expr_and_fold_it_hazmat` (Impact: 1156.2 | O(2^N) | DB: 3)
    * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call th...
  * `eval_const_expr_and_fold_it` (Impact: 35.3 | O(N^3) | DB: 3)
    * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// This is a safe wrapper around ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 89`, `args: 10`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 14`, `fragile_debt: 22`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 59`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, Constant, UnaryOpKind, BinOpKind, crate::ast::
    IntLiteralValue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/transpiler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.371 IQR)
- **Top Global Matches:** file_cluster_8: 11.371, file_cluster_7: 11.773, file_cluster_13: 11.852
- **Magnitude:** 852.96 | **LOC:** 492 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (23.078%), Tech Debt (96.5074%)
**Top Internal Functions/Classes:**
  * `transpile_stmt` (Impact: 454.4 | O(2^N) | DB: 15)
    * *Intent:* /// Transpiles a statement into equivlent Rust code ///
  * `holy_expr_to_rust_expr` (Impact: 237.3 | O(2^N) | DB: 3)
    * *Intent:* /// Turns a HolyLang expression, into equvilent Rust expression ///
  * `transpile_function` (Impact: 47.6 | O(N^4) | DB: 1)
    * *Intent:* /// Transpiles a function and its inner statements into equvilent Rust code ///
  * `holy_type_to_rust_type_str` (Impact: 31.3 | O(2^N))
    * *Intent:* /// Turns a holylang type e.g. Int32, Int64, etc, into equvilent Rust type ///
  * `transpile` (Impact: 9.8 | O(N^2) | DB: 1)
    * *Intent:* /// Takes a reference to a Abstract Syntax Tree, and returns equvilent code in Rust as a string ///
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 84`, `args: 17`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 5`, `state_mutation: 56`, `planned_debt: 1`, `fragile_debt: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 17`, `doc: 12`, `sync_locks: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Stmt, Constant, Type, Function, Expr, GlobalStmt, UnaryOpKind, crate::ast::
    AST...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/for_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.737 IQR)
- **Top Global Matches:** file_cluster_8: 9.737, file_cluster_0: 10.115, file_cluster_7: 10.527
- **Magnitude:** 822.38 | **LOC:** 469 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (30.9556%), Tech Debt (99.8856%)
**Top Internal Functions/Classes:**
  * `for_statements_invalid_construction_erro` (Impact: 168.1 | O(N^2))
  * `for_statements_trailing_kw_errors` (Impact: 152.0 | O(N^3))
  * `for_statements_trailing_types_errors` (Impact: 81.3 | O(N^3))
  * `for_statements_literal` (Impact: 75.6 | O(N^4))
  * `for_statements_trailing_exprs_errors` (Impact: 58.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 40`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `import: 2`
* *Defense:* `safety: 13`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/array_slicing_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.836 IQR)
- **Top Global Matches:** file_cluster_8: 9.836, file_cluster_0: 10.189, file_cluster_16: 10.229
- **Magnitude:** 631.04 | **LOC:** 455 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.9887%), Tech Debt (99.64%)
**Top Internal Functions/Classes:**
  * `array_slice_both_bounds_in_const` (Impact: 49.7 | O(N^6))
  * `array_slice_open_start_in_const` (Impact: 49.7 | O(N^6))
  * `array_slice_open_end_in_const` (Impact: 49.7 | O(N^6))
  * `array_slice_both_bounds_in_var_decl` (Impact: 49.5 | O(N^6))
  * `array_slice_open_start_in_var_decl` (Impact: 49.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 101`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `duplicate_logic: 4`, `orphaned_logic: 19`
* *Architecture:* `import: 3`
* *Defense:* `safety: 18`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/break_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.257 IQR)
- **Top Global Matches:** file_cluster_8: 9.257, file_cluster_0: 9.686, file_cluster_7: 10.109
- **Magnitude:** 613.56 | **LOC:** 493 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.5459%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `invalid_errors` (Impact: 120.3 | O(N^2))
  * `invalid_errors` (Impact: 120.3 | O(N^2))
  * `in_if_with_else_with_elif_stmt` (Impact: 25.3 | O(N^3))
  * `in_if_else_with_elif_stmt` (Impact: 25.2 | O(N^3))
  * `in_if_else_stmt` (Impact: 25.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 52`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `duplicate_logic: 26`, `orphaned_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/continue_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.448 IQR)
- **Top Global Matches:** file_cluster_8: 9.448, file_cluster_0: 9.849, file_cluster_7: 10.284
- **Magnitude:** 613.56 | **LOC:** 493 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.5791%), Tech Debt (99.8662%)
**Top Internal Functions/Classes:**
  * `invalid_errors` (Impact: 120.3 | O(N^2))
  * `invalid_errors` (Impact: 120.3 | O(N^2))
  * `in_if_with_else_with_elif_stmt` (Impact: 25.3 | O(N^3))
  * `in_if_else_with_elif_stmt` (Impact: 25.2 | O(N^3))
  * `in_if_else_stmt` (Impact: 25.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 52`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `duplicate_logic: 4`, `orphaned_logic: 24`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/const_decl_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.544 IQR)
- **Top Global Matches:** file_cluster_8: 9.544, file_cluster_0: 9.908, file_cluster_7: 10.42
- **Magnitude:** 578.16 | **LOC:** 432 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.8818%), Tech Debt (99.9982%)
**Top Internal Functions/Classes:**
  * `const_decl_in_if_else_branch` (Impact: 58.4 | O(N^5))
  * `const_decl_in_if_main_branch` (Impact: 53.1 | O(N^5))
  * `const_decl_in_if_elif_branch` (Impact: 53.1 | O(N^5))
  * `const_decl_in_for_branch` (Impact: 53.0 | O(N^5))
  * `const_decl_in_while_loop` (Impact: 47.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 60`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 12`, `orphaned_logic: 14`
* *Architecture:* `import: 3`
* *Defense:* `safety: 15`, `test: 68`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/continue_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.352 IQR)
- **Top Global Matches:** file_cluster_8: 11.352, file_cluster_0: 11.53, file_cluster_17: 11.564
- **Magnitude:** 568.68 | **LOC:** 683 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.9803%), Tech Debt (95.555%)
**Top Internal Functions/Classes:**
  * `test_continue_statement_in_if_statement_` (Impact: 81.6 | O(N^6) | DB: 2)
  * `test_continue_statement_in_if_statement_` (Impact: 63.4 | O(N^6) | DB: 2)
  * `test_continue_statement_in_for_statement` (Impact: 62.7 | O(N^6) | DB: 2)
  * `test_continue_statement_in_if_statement_` (Impact: 57.3 | O(N^6) | DB: 2)
  * `test_continue_statement_in_if_statement_` (Impact: 57.2 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 112`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 54`, `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `import: 2`
* *Defense:* `safety: 48`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/break_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.333 IQR)
- **Top Global Matches:** file_cluster_8: 11.333, file_cluster_0: 11.509, file_cluster_17: 11.542
- **Magnitude:** 543.74 | **LOC:** 679 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.8103%), Tech Debt (95.9149%)
**Top Internal Functions/Classes:**
  * `test_break_statement_in_if_statement_in_` (Impact: 81.6 | O(N^6) | DB: 2)
  * `test_break_statement_in_if_statement_in_` (Impact: 63.4 | O(N^6) | DB: 2)
  * `test_break_statement_in_for_statement_wi` (Impact: 62.7 | O(N^6) | DB: 2)
  * `test_break_statement_in_if_statement_in_` (Impact: 57.3 | O(N^6) | DB: 2)
  * `test_break_statement_in_if_statement_in_` (Impact: 57.2 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 112`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 54`, `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `import: 2`
* *Defense:* `safety: 47`, `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/infinite_stmt_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.751 IQR)
- **Top Global Matches:** file_cluster_8: 9.751, file_cluster_0: 10.09, file_cluster_17: 10.435
- **Magnitude:** 529.5 | **LOC:** 703 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.9274%), Tech Debt (99.5122%)
**Top Internal Functions/Classes:**
  * `with_var_decl_with_value` (Impact: 49.7 | O(N^6))
  * `after_var_decl_with_value` (Impact: 42.9 | O(N^5))
  * `below_var_decl_with_value` (Impact: 42.8 | O(N^5))
  * `with_var_decl_without_value` (Impact: 37.5 | O(N^5))
  * `below_var_decl_without_value` (Impact: 31.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 73`, `args: 31`, `func_start: 31`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 8`, `orphaned_logic: 23`
* *Architecture:* `import: 3`
* *Defense:* `safety: 17`, `test: 70`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/locking_unlocking_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.111 IQR)
- **Top Global Matches:** file_cluster_8: 10.111, file_cluster_17: 10.387, file_cluster_0: 10.402
- **Magnitude:** 523.8 | **LOC:** 875 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (13.2598%), Tech Debt (94.7586%)
**Top Internal Functions/Classes:**
  * `multi_assign_locked_vars_errors` (Impact: 22.1 | O(N^4) | DB: 6)
  * `unlock_func_arg_in_while_loop_errors` (Impact: 19.3 | O(N^6) | DB: 2)
  * `lock_func_arg_in_while_loop_errors` (Impact: 19.3 | O(N^6) | DB: 2)
  * `lock_literal_errors` (Impact: 13.8 | O(N^4) | DB: 2)
  * `unlock_literal_errors` (Impact: 13.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 303`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 86`, `orphaned_logic: 41`
* *Architecture:* `import: 2`
* *Defense:* `safety: 8`, `doc: 2`, `test: 117`, `sync_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/int_literal_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.852 IQR)
- **Top Global Matches:** file_cluster_8: 10.852, file_cluster_0: 11.009, file_cluster_7: 11.658
- **Magnitude:** 456.72 | **LOC:** 455 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.3581%), Tech Debt (99.9678%)
**Top Internal Functions/Classes:**
  * `integer_literal_int8_boundary` (Impact: 44.7 | O(N^4))
  * `integer_literal_int16_boundary` (Impact: 44.7 | O(N^4))
  * `integer_literal_int32_boundary` (Impact: 44.7 | O(N^4))
  * `integer_literal_int128_boundary` (Impact: 44.7 | O(N^4))
  * `integer_literal_int64_boundary` (Impact: 44.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 48`, `args: 37`, `func_start: 37`
* *Risk/State:* `orphaned_logic: 37`
* *Architecture:* `import: 2`
* *Defense:* `safety: 33`, `test: 127`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/branch_analysis_tests/dead_code_analysis_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.455 IQR)
- **Top Global Matches:** file_cluster_8: 9.455, file_cluster_0: 9.839, file_cluster_16: 10.136
- **Magnitude:** 451.88 | **LOC:** 746 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.3781%), Tech Debt (99.5511%)
**Top Internal Functions/Classes:**
  * `if_statement_elif_branch_has_empty_for_s` (Impact: 19.6 | O(N^6))
  * `if_statement_branch_has_empty_while_stmt` (Impact: 19.5 | O(N^6))
  * `if_statement_branch_has_empty_for_stmt_b` (Impact: 19.5 | O(N^6))
  * `if_statement_elif_branch_has_empty_infin` (Impact: 19.5 | O(N^6))
  * `if_statement_elif_branch_has_empty_while` (Impact: 19.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 120`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 21`, `fragile_debt: 1`, `orphaned_logic: 29`
* *Architecture:* `import: 2`
* *Defense:* `safety: 17`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast/types_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.681 IQR)
- **Top Global Matches:** file_cluster_0: 12.681, file_cluster_8: 12.944, file_cluster_13: 13.108
- **Magnitude:** 415.0 | **LOC:** 412 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (33.2577%), Tech Debt (95.3347%)
**Top Internal Functions/Classes:**
  * `no_type_is_both_integer_and_float` (Impact: 40.2 | O(N^4))
    * *Intent:* // A type cannot be both integer AND float, ever.
  * `no_type_is_both_integer_and_array` (Impact: 40.2 | O(N^4))
    * *Intent:* // No type can be both an integer and an array. Ever. //
  * `no_type_is_both_float_and_array` (Impact: 40.2 | O(N^4))
    * *Intent:* // No type can be both a float and an array. Ever. //
  * `default_value_all_valid_variants` (Impact: 36.9 | O(N^4) | DB: 2)
    * *Intent:* // Type::get_default_value
  * `fixed_array_to_dynamic_array_type_full` (Impact: 35.1 | O(2^N))
    * *Intent:* // We dont use should_panic here because we test multiple types //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 55`, `args: 22`, `func_start: 18`
* *Risk/State:* `state_mutation: 51`, `dead_code: 1`, `orphaned_logic: 16`
* *Architecture:* `import: 3`
* *Defense:* `safety: 52`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, ALL_TYPES_NO_ARR_NO_FLOAT, crate::tests_consts::
    ALL_TYPES_NO_ARR
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/parse_expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.29 IQR)
- **Top Global Matches:** file_cluster_8: 12.29, file_cluster_17: 12.537, file_cluster_13: 12.564
- **Magnitude:** 412.34 | **LOC:** 544 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (16.0855%), Tech Debt (27.064%)
**Top Internal Functions/Classes:**
  * `parse_expr` (Impact: 382.7 | O(2^N) | DB: 4)
    * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary opera...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 78`, `args: 8`, `func_start: 1`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 69`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ast::*, super::HolyError, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/branch_analysis_tests/return_branch_analysis_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.404 IQR)
- **Top Global Matches:** file_cluster_8: 9.404, file_cluster_0: 9.858, file_cluster_7: 10.291
- **Magnitude:** 386.88 | **LOC:** 914 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (6.3841%), Tech Debt (99.997%)
**Top Internal Functions/Classes:**
  * `if_statement_elif_branch_inside_infinite` (Impact: 31.8 | O(N^6))
  * `infinite_statement_inside_if_stmt_break_` (Impact: 31.8 | O(N^6))
  * `if_statement_main_branch_inside_infinite` (Impact: 31.7 | O(N^6))
  * `if_statement_else_branch_inside_infinite` (Impact: 31.7 | O(N^6))
  * `infinite_statement_while_statement_neste` (Impact: 26.0 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 106`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 3`, `fragile_debt: 6`, `duplicate_logic: 8`, `orphaned_logic: 17`
* *Architecture:* `import: 2`
* *Defense:* `safety: 42`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/multi_return_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_17` (Drift: 9.704 IQR)
- **Top Global Matches:** file_cluster_17: 9.704, file_cluster_8: 9.829, file_cluster_0: 10.201
- **Magnitude:** 385.72 | **LOC:** 880 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (13.7933%), Tech Debt (52.7813%)
**Top Internal Functions/Classes:**
  * `multi_return_assign` (Impact: 50.7 | O(N^4) | DB: 2)
    * *Intent:* // return statement with multiple values (aka multi-return) // with multi-assignments
  * `test_multi_return_assign_type_mismatch_e` (Impact: 35.1 | O(N^4) | DB: 6)
  * `test_multi_return_decl_correct` (Impact: 32.3 | O(N^4) | DB: 2)
    * *Intent:* // return statement with multiple values (aka multi-return) // with multi-declaration
  * `test_multi_return_decl_typemismatch_erro` (Impact: 27.8 | O(N^3) | DB: 6)
  * `test_multi_assign_undeclared_vars_errors` (Impact: 21.7 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 259`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 72`, `dead_code: 2`, `orphaned_logic: 17`
* *Architecture:* `import: 2`
* *Defense:* `safety: 6`, `test: 80`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/parser/parse_expr_tests/unary_op_tests.rs` (RUST) | Magnitude: 167.94 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 123, branch: 29, test: 19, structural_boundaries: 15
- `src/semantic/blackbox_tests/copy_tests.rs` (RUST) | Magnitude: 132.76 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 66, test: 22, safety: 21
- `src/semantic/blackbox_tests/const_tests.rs` (RUST) | Magnitude: 1268.62 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1869, structural_boundaries: 853, test: 378, state_mutation: 299
- `src/parser/parse_expr_tests/bool_literal_tests.rs` (RUST) | Magnitude: 13.34 | Delta: **0.209 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, test: 12, safety: 8, sec_high_risk_execution: 8
- `src/semantic.rs` (RUST) | Magnitude: 48.94 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, doc: 14, fragile_debt: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/error.rs` (RUST) | Magnitude: 18.5 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, branch: 3, state_mutation: 3
- `src/ast.rs` (RUST) | Magnitude: 24.56 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, api: 9, doc: 9, encapsulation: 9
- `src/compile.rs` (RUST) | Magnitude: 30.36 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 21, safety_bypasses: 10, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/ast/exprs.rs` (RUST) | Magnitude: 21.0 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, doc: 22, generics: 17, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/semantic/blackbox_tests/unary_op_tests.rs` (RUST) | Magnitude: 20.24 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, test: 5, state_mutation: 4
- `src/semantic/blackbox_tests/dyn_array_access_tests.rs` (RUST) | Magnitude: 52.28 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 31, safety: 12, memory_alloc: 9
- `src/semantic/blackbox_tests/fixed_array_access_tests.rs` (RUST) | Magnitude: 52.18 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 31, safety: 12, memory_alloc: 9
- `src/semantic/blackbox_tests/fixed_array_slicing_tests.rs` (RUST) | Magnitude: 115.76 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 51, safety: 29, memory_alloc: 24
- `src/semantic/blackbox_tests/multi_return_tests.rs` (RUST) | Magnitude: 385.72 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 647, structural_boundaries: 259, test: 80, comprehensions: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/semantic/infer.rs` (RUST) | Magnitude: 196.22 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 106, branch: 42, safety: 37, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/semantic/blackbox_tests/bin_op_tests.rs` (RUST) | Magnitude: 380.28 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 165, branch: 47, test: 46
- `src/semantic/blackbox_tests/for_stmt_tests.rs` (RUST) | Magnitude: 150.0 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 65, test: 21, sec_high_risk_execution: 21
- `src/semantic/blackbox_tests/function_tests.rs` (RUST) | Magnitude: 67.42 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 39, test: 17, state_mutation: 14
- `src/semantic/blackbox_tests/array_tests.rs` (RUST) | Magnitude: 66.1 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 35, test: 13, safety: 9
- `src/lib.rs` (RUST) | Magnitude: 44.56 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 14, api: 9, encapsulation: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/semantic/blackbox_tests/const_tests.rs` -> Churn: **100.0%** | Cog Load: 30.482% | Debt: 96.8227%
- `src/transpiler.rs` -> Churn: **90.4%** | Cog Load: 23.078% | Debt: 96.5074%
- `src/semantic/blackbox_tests/ownership_tests.rs` -> Churn: **82.95%** | Cog Load: 14.6312% | Debt: 87.7683%
- `src/semantic.rs` -> Churn: **80.04%** | Cog Load: 13.8695% | Debt: 100.0%
- `src/semantic/blackbox_tests.rs` -> Churn: **80.04%** | Cog Load: 7.24% | Debt: 92.6231%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/semantic/blackbox_tests/ownership_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 1760.66
- `src/semantic/branch_analysis.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 1349.76
- `src/parser.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 1340.26
- `src/semantic/blackbox_tests/const_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 1268.62
- `src/semantic/constants.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 1214.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ast/stmts.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/ast/types.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/compile.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/lib.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/parser/blackbox_tests/comment_tests.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
