# ARCHITECTURAL_BRIEF: HolyLang
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/chadsec1/HolyLang` |
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
- **Scope:** 107 analyzed artifact(s), 26438 LOC.
- **Load-bearing artifact:** `src/semantic/blackbox_tests.rs` -- 30 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/semantic/blackbox_tests.rs` -- pulls in 66 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/semantic.rs` at magnitude 529.84 (structural weight, not risk).
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
| Total Artifacts | 111 |
| Analyzed Artifacts (Scanned) | 107 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 26438 |
| Volatility Index | 0.056 |
| % Scanned of codebase = | 96.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5292 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6395 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 86.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7156 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 103 | 26355 | 96.3% |
| MARKDOWN | 2 | 0 | 1.9% |
| YAML | 2 | 83 | 1.9% |

## 4.1 SOURCE ENCODINGS
All 107 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 35%, Large Core Modules 28%, Large Core Modules (2) 8%, State Mutators Files 7%, Data / Markup / Trivial 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 105 | 98.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.toml`: 1x Unsupported Format (.toml)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 47.7 | 9.3 | 7.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.0 | 39.7 | 47.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 11.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 9.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 95.4 | 44.5 | 47.0 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.3 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.3 | 72.6 | 15.0 | 15.7 | 1.6 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 9.2 | 100.0 | 35.4 | 31.0 | 31.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 88.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1030 | 52 | 25 | `src/semantic/blackbox_tests/const_tests.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 750 | 58 | 17 | `src/parser/blackbox_tests/while_stmt_tests.rs` |
| danger | 2114 | 88 | 42 | `src/semantic/blackbox_tests/ownership_tests.rs` |
| concurrency | 149 | 9 | 0 | `src/parser/blackbox_tests/lock_stmt_tests.rs` |
| connectivity | 1251 | 103 | 26 | `src/semantic/blackbox_tests/const_tests.rs` |
| io | 5 | 2 | 0 | `src/compile.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 2 | 1 | 0 | `.github/workflows/codeql.yml` |
| tests | 4166 | 83 | 96 | `src/semantic/blackbox_tests/const_tests.rs` |
| docs | 237 | 30 | 5 | `src/semantic/blackbox_tests/if_stmt_tests.rs` |
| debt | 136 | 25 | 3 | `src/semantic/constants.rs` |
| mutation | 4493 | 95 | 99 | `src/semantic/blackbox_tests/const_tests.rs` |
| dead_code | 4 | 3 | 0 | `src/semantic/blackbox_tests/multi_return_tests.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 28 | 10 | 0 | `src/parser/parse_expr_tests/float64_literal_tests.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0606**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/compile.rs` (Hits: 4)
- `src/main.rs` (Hits: 1)
- `.github/ISSUE_TEMPLATE/general-bug-report.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **blackbox_tests.rs** (`src/semantic/blackbox_tests.rs`) — 30 inbound connections
2. **blackbox_tests.rs** (`src/parser/blackbox_tests.rs`) — 28 inbound connections
3. **parse_expr_tests.rs** (`src/parser/parse_expr_tests.rs`) — 15 inbound connections
4. **exprs.rs** (`src/ast/exprs.rs`) — 10 inbound connections
5. **types.rs** (`src/ast/types.rs`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blackbox_tests.rs** (`src/semantic/blackbox_tests.rs`) — 66 outbound dependencies
2. **blackbox_tests.rs** (`src/parser/blackbox_tests.rs`) — 35 outbound dependencies
3. **parse_expr_tests.rs** (`src/parser/parse_expr_tests.rs`) — 19 outbound dependencies
4. **semantic.rs** (`src/semantic.rs`) — 17 outbound dependencies
5. **ast.rs** (`src/ast.rs`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check_stmts` **(Many-Argument Workhorses)** (@ `src/semantic.rs`) -> Impact: **353.8** | LOC: 779
  * *Intent:* /// Parse holylang statements in a block, it does: /// Enforce language semantics, and ownership safety model, check function calls, etc.
- `infer_expr_type` **(Many-Argument Workhorses)** (@ `src/semantic/infer.rs`) -> Impact: **298.4** | LOC: 647
  * *Intent:* /// Infer the type of an expression, and update literal nodes (and nested nodes) where possible. /// Returns the deduced Type for the expression. /// ...
- `parse_expr` **(Many-Argument Workhorses)** (@ `src/parser/parse_expr.rs`) -> Impact: **196.1** | LOC: 528
  * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary operations (like negate, logical not, bitwise not ) ///...
- `eval_const_expr_and_fold_it_hazmat` **(Many-Argument Workhorses)** (@ `src/semantic/constants.rs`) -> Impact: **143.2** | LOC: 612
  * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call this function directly unless you 1000% know what yo...
- `parse_stmt_line` **(Many-Argument Workhorses)** (@ `src/parser.rs`) -> Impact: **96.7** | LOC: 236
  * *Intent:* /// Parse a single statement from a comments-removed trimmed line. `line_no` used for error messages.
- `return_branch_analysis` **(Many-Argument Workhorses)** (@ `src/semantic/branch_analysis.rs`) -> Impact: **87.3** | LOC: 181
- `parse_function` **(Many-Argument Workhorses)** (@ `src/parser.rs`) -> Impact: **61.6** | LOC: 123
  * *Intent:* /// Parse function starting at index `start_i`. /// Returns (Function, index after function end).
- `find_top_level_op_any` **(Defensive Guards)** (@ `src/parser/helpers.rs`) -> Impact: **57.6** | LOC: 105
- `dead_code_analysis` **(Many-Argument Workhorses)** (@ `src/semantic/branch_analysis.rs`) -> Impact: **49.8** | LOC: 129
- `transpile_stmt` **(Compute Cores)** (@ `src/transpiler.rs`) -> Impact: **47.1** | LOC: 207
  * *Intent:* /// Transpiles a statement into equivlent Rust code ///

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/parser/blackbox_tests` | 27 | 3135.84 | 11.43% | 4.8% |
| `src/semantic/blackbox_tests` | 29 | 2299.02 | 6.29% | 1.7% |
| `src` | 10 | 1479.08 | 12.19% | 27.74% |
| `src/semantic` | 7 | 1073.52 | 10.28% | 49.56% |
| `src/parser` | 5 | 921.36 | 18.05% | 17.27% |
| `src/parser/parse_expr_tests` | 14 | 545.08 | 8.82% | 0.65% |
| `src/ast` | 9 | 436.46 | 6.3% | 27.64% |
| `src/semantic/branch_analysis_tests` | 2 | 306.64 | 6.42% | 16.37% |
| `.github/workflows` | 2 | 12.36 | 3.97% | 0.0% |
| `__monolith__` | 1 | 4.9 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/ast/int_literal_value_tests.rs` -> **99.7943%** Exposure
- `src/semantic/branch_analysis.rs` -> **98.7639%** Exposure
- `src/semantic/constants.rs` -> **98.4529%** Exposure
- `src/semantic/helpers.rs` -> **82.0223%** Exposure
- `src/ast/int_literal_value.rs` -> **76.1067%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/transpiler.rs` -> **100.0%** Exposure
- `src/parser/helpers.rs` -> **99.9999%** Exposure
- `src/compile.rs` -> **99.9254%** Exposure
- `src/ast/types_tests.rs` -> **99.5773%** Exposure
- `src/parser.rs` -> **97.783%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/parser/blackbox_tests/lock_stmt_tests.rs` -> **0** Orphaned Functions | **2** Duplicates
- `src/parser/blackbox_tests/unlock_stmt_tests.rs` -> **0** Orphaned Functions | **2** Duplicates
- `src/main.rs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `305` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/semantic.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.209)
- **Top Global Matches:** file_cluster_6: 8.209, file_cluster_4: 10.614, file_cluster_9: 15.949
- **Magnitude:** 529.84 | **LOC:** 1098 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 80.5%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 9.544; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.8%), Debt Markers (formerly Tech Debt) (57.7%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_stmts` **(Many-Argument Workhorses)** (Impact: 353.8)
    * *Intent:* /// Parse holylang statements in a block, it does: /// Enforce language semantics, and ownership saf...
  * `check_call` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* /// Validate a call's arguments, infer literal arg types to parameter types, /// and apply move sema...
  * `check_function` **(Many-Argument Workhorses)** (Impact: 19.5)
    * *Intent:* /// Check single function, infer local var types where possible, check calls, returns.
  * `update_local_assignments_from_clone` **(Defensive Guards)** (Impact: 13.2)
  * `check_semantics` **(Generic / Templated Code)** (Impact: 11.2)
    * *Intent:* /// Checks semantics and fill in inferred types where possible. /// This mutates the AST, because in...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 193`, `args: 19`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `state_mutation: 31`, `fragile_debt: 14`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 25`, `doc: 14`, `test: 5`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.544
  * `Choke Point (Betweenness):` 0.074865 | `Ripple Effect (Closeness):` 0.204987
  * `Imports (Out-Degree: 13):` blackbox_tests, branch_analysis, branch_analysis_tests, constants, helpers, helpers_tests, infer, crate::ast::AST...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.378)
- **Top Global Matches:** file_cluster_8: 5.378, file_cluster_6: 12.732, file_cluster_4: 21.558
- **Magnitude:** 476.82 | **LOC:** 905 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 73.4%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 12.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_stmt_line` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* /// Parse a single statement from a comments-removed trimmed line. `line_no` used for error messages...
  * `parse_function` **(Many-Argument Workhorses)** (Impact: 61.6)
    * *Intent:* /// Parse function starting at index `start_i`. /// Returns (Function, index after function end).
  * `parse_block` **(Compute Cores)** (Impact: 36.1)
  * `parse_if_stmt` **(Compute Cores)** (Impact: 35.2)
  * `parse_for_stmt` **(Compute Cores)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 241`, `args: 35`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 7`, `state_mutation: 32`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 9`, `doc: 9`, `test: 3`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.35
  * `Choke Point (Betweenness):` 0.128669 | `Ripple Effect (Closeness):` 0.234153
  * `Imports (Out-Degree: 7):` blackbox_tests, helpers, helpers_tests, parse_expr, parse_expr_tests, crate::ast::*, crate::error::HolyError
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/semantic/blackbox_tests/const_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.749)
- **Top Global Matches:** file_cluster_7: 7.749, file_cluster_5: 8.054, file_cluster_12: 8.464
- **Magnitude:** 447.72 | **LOC:** 2269 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.0%), Guard Balance (formerly Safety Score) (49.1%), Mutation Surface (formerly State Flux) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `const_evaluated_numeric_comparison` **(Annotated & Test Methods)** (Impact: 12.7)
    * *Intent:* // This includes greater than/ less than
  * `const_evaluated_logical_and_with_equal_comparison` **(I/O & Config Routines)** (Impact: 12.6)
  * `const_all_arth_binop_on_literals` **(Annotated & Test Methods)** (Impact: 12.1)
  * `const_evaluated_equal_comparison` **(Annotated & Test Methods)** (Impact: 10.7)
  * `const_unary_negate_on_signed_consts` **(Annotated & Test Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 853`, `args: 112`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 111`, `high_risk_execution: 15`, `state_mutation: 1`
* *Architecture:* `api: 111`, `import: 6`
* *Defense:* `safety: 12`, `test: 378`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163057
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/while_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.971)
- **Top Global Matches:** file_cluster_4: 8.971, file_cluster_13: 11.383, file_cluster_9: 11.501
- **Magnitude:** 432.9 | **LOC:** 1181 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (62.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.0%), Guard Balance (formerly Safety Score) (37.5%), Mutation Surface (formerly State Flux) (36.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vars_and_literals_spaces_before_expr` **(Defensive Guards)** (Impact: 22.8)
    * *Intent:* // Same test as above, but before the expression, there is an `i` of spaces.
  * `vars_and_literals_spaces_after_expr` **(Defensive Guards)** (Impact: 22.8)
    * *Intent:* // Same test as above, but after the expression, there is an `i` of spaces.
  * `vars_and_literals` **(Defensive Guards)** (Impact: 21.4)
  * `vars_spaces_before_expr` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // Same test as above, but before the expression, there is an `i` of spaces.
  * `int_literals_spaces_before_expr` **(Defensive Guards)** (Impact: 12.6)
    * *Intent:* // Same test as above, but before the expression, there is an `i` of spaces.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 67 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 147`, `args: 43`, `func_start: 43`
* *Risk/State:* `high_risk_execution: 67`, `state_mutation: 16`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 67`, `test: 148`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/semantic/infer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.631)
- **Top Global Matches:** file_cluster_8: 8.631, file_cluster_6: 18.541, file_cluster_3: 20.141
- **Magnitude:** 393.88 | **LOC:** 775 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 2.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (67.7%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infer_expr_type` **(Many-Argument Workhorses)** (Impact: 298.4)
    * *Intent:* /// Infer the type of an expression, and update literal nodes (and nested nodes) where possible. ///...
  * `advanced_infer_2_types` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /// This takes 2 expressions, and tries to get types, and convert each other types to the same type ...
  * `check_usize_literal_to_src` **(Many-Argument Workhorses)** (Impact: 23.2)
    * *Intent:* // helper: check an expression that's allowed to be an IntLiteral::Usize
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 123`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 7`, `state_mutation: 9`, `planned_debt: 8`, `fragile_debt: 8`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 16`, `doc: 16`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.556
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.132862
  * `Imports (Out-Degree: 4):` crate::ast::ArraySliceRange, crate::ast::BinOpKind, crate::ast::FixedArraySize, crate::ast::IntLiteralValue, crate::ast::UnaryOpKind, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/semantic/blackbox_tests/ownership_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.114)
- **Top Global Matches:** file_cluster_12: 8.114, file_cluster_7: 8.74, file_cluster_5: 10.014
- **Magnitude:** 391.26 | **LOC:** 1733 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.3%), Guard Balance (formerly Safety Score) (40.1%), Complexity Load (formerly Cognitive Load) (7.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vardecl_in_if_else_branch_moves_upstream_var` **(I/O & Config Routines)** (Impact: 15.1)
  * `vardecl_in_if_elif_branch_moves_upstream_var` **(I/O & Config Routines)** (Impact: 15.1)
  * `vardecl_in_if_main_branch_does_not_move_upstream_const` **(I/O & Config Routines)** (Impact: 15.0)
  * `vardecl_moving_local_var_in_if_stmt_elif_branch` **(I/O & Config Routines)** (Impact: 12.8)
  * `vardecl_moving_local_var_in_if_stmt_else_branch` **(I/O & Config Routines)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 55 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 415`, `args: 46`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 55`
* *Architecture:* `api: 46`, `import: 2`
* *Defense:* `safety: 55`, `doc: 5`, `test: 330`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163057
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/transpiler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.517)
- **Top Global Matches:** file_cluster_6: 9.517, file_cluster_4: 11.157, file_cluster_12: 15.988
- **Magnitude:** 351.56 | **LOC:** 492 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 2.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.9%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transpile_stmt` **(Compute Cores)** (Impact: 47.1)
    * *Intent:* /// Transpiles a statement into equivlent Rust code ///
  * `holy_expr_to_rust_expr` **(Defensive Guards)** (Impact: 25.7)
    * *Intent:* /// Turns a HolyLang expression, into equvilent Rust expression ///
  * `transpile_function` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /// Transpiles a function and its inner statements into equvilent Rust code ///
  * `holy_type_to_rust_type_str` **(State Mutators)** (Impact: 5.5)
    * *Intent:* /// Turns a holylang type e.g. Int32, Int64, etc, into equvilent Rust type ///
  * `transpile` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /// Takes a reference to a Abstract Syntax Tree, and returns equvilent code in Rust as a string ///
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 74 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 84`, `args: 16`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 13`, `state_mutation: 92`, `planned_debt: 1`, `fragile_debt: 8`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 13`, `doc: 12`, `sync_locks: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.266
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.009434
  * `Imports (Out-Degree: 4):` crate::ast::AST, crate::ast::ArraySliceRange, crate::ast::BinOpKind, crate::ast::Constant, crate::ast::Expr, crate::ast::FixedArraySize, crate::ast::Function, crate::ast::GlobalStmt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/helpers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.962)
- **Top Global Matches:** file_cluster_6: 8.962, file_cluster_8: 10.619, file_cluster_4: 16.408
- **Magnitude:** 348.68 | **LOC:** 427 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 72.2%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 5.406; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_top_level_op_any` **(Defensive Guards)** (Impact: 57.6)
  * `split_char_top_level` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* /// Split "char"-separated args at top-level only. /// - respects nested (), [], {} /// - respects "...
  * `count_braces_outside_strings` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /// Count '{' and '}' that are outside string literals. /// Handles both single-quoted and double-qu...
  * `strip_inline_comment` **(Compute Cores)** (Impact: 21.5)
    * *Intent:* /// Remove an inline `#` comment from `s`, but only when the `#` is outside /// single- or double-qu...
  * `parse_format_string` **(Defensive Guards)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 83`, `args: 19`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 51`, `fragile_debt: 6`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 15`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.406
  * `Choke Point (Betweenness):` 0.004837 | `Ripple Effect (Closeness):` 0.156689
  * `Imports (Out-Degree: 2):` crate::consts, super::*
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/bin_op_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.504)
- **Top Global Matches:** file_cluster_6: 9.504, file_cluster_4: 11.385, file_cluster_9: 17.496
- **Magnitude:** 345.56 | **LOC:** 1078 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (65.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.0%), Guard Balance (formerly Safety Score) (43.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vars_and_unsigned_integer_literals_mixed` **(I/O & Config Routines)** (Impact: 24.9)
    * *Intent:* // Unsigned integer literals
  * `vars_and_signed_integer_literals_mixed_in_var_decl` **(I/O & Config Routines)** (Impact: 22.1)
    * *Intent:* // Signed integer literals
  * `vars_and_signed_integer_literals_mixed` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* // Signed integer literals
  * `unsigned_literals_only_in_var_decl` **(I/O & Config Routines)** (Impact: 19.6)
  * `unsigned_literals_only` **(I/O & Config Routines)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 37 instances
* *High Risk Execution (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 108`, `args: 34`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 54`
* *Architecture:* `api: 34`, `import: 3`
* *Defense:* `safety: 46`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/if_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.06)
- **Top Global Matches:** file_cluster_6: 11.06, file_cluster_8: 11.883, file_cluster_4: 17.855
- **Magnitude:** 303.6 | **LOC:** 878 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.5%), Guard Balance (formerly Safety Score) (28.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (18.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `if_statements_with_elif_vars_and_literals` **(Defensive Guards)** (Impact: 35.5)
  * `if_statements_vars_and_literals` **(Defensive Guards)** (Impact: 21.9)
  * `if_statements_with_else_elif` **(Defensive Guards)** (Impact: 18.4)
  * `if_statements_with_elif_literals` **(Defensive Guards)** (Impact: 18.3)
  * `if_statements_with_elif_vars` **(Defensive Guards)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 78 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 120`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 78`, `state_mutation: 2`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 78`, `test: 167`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/helpers_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.504)
- **Top Global Matches:** file_cluster_7: 7.504, file_cluster_5: 7.923, file_cluster_12: 8.709
- **Magnitude:** 259.2 | **LOC:** 1275 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 70.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.548; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.2%), Guard Balance (formerly Safety Score) (41.4%), Debt Markers (formerly Tech Debt) (12.9%)
- **Documentation Coverage:** 95.5801% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unescaped_inner_double_quote_is_error` **(Annotated & Test Methods)** (Impact: 10.5)
  * `empty_string_literal_as_arg` **(Annotated & Test Methods)** (Impact: 6.8)
  * `braces_inside_double_quotes_not_counted` **(Annotated & Test Methods)** (Impact: 4.0)
  * `backslash_escaped_quote_inside_string` **(Annotated & Test Methods)** (Impact: 3.0)
  * `unknown_escape_errors` **(Annotated & Test Methods)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 147`, `args: 167`, `func_start: 157`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 1`, `fragile_debt: 4`
* *Architecture:* `api: 89`, `import: 13`
* *Defense:* `doc: 5`, `test: 369`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.000427 | `Ripple Effect (Closeness):` 0.154368
  * `Imports (Out-Degree: 3):` crate::consts, crate::tests_consts::ALL_TYPES_NO_ARR, self::*, self::tests::*, self::tests::count_braces_outside_strings::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/parse_expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.333)
- **Top Global Matches:** file_cluster_1: 4.333, file_cluster_3: 48.116, file_cluster_8: 69.992
- **Magnitude:** 234.46 | **LOC:** 544 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 6.559; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.6%), Mutation Surface (formerly State Flux) (70.3%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_expr` **(Many-Argument Workhorses)** (Impact: 196.1)
    * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary opera...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 115`, `args: 8`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 17`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.559
  * `Choke Point (Betweenness):` 0.006402 | `Ripple Effect (Closeness):` 0.175123
  * `Imports (Out-Degree: 3):` crate::ast::*, super::HolyError, super::helpers
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/semantic/constants.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.488)
- **Top Global Matches:** file_cluster_8: 9.488, file_cluster_6: 11.222, file_cluster_4: 18.892
- **Magnitude:** 230.62 | **LOC:** 692 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 2.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.5%), Mutation Surface (formerly State Flux) (86.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eval_const_expr_and_fold_it_hazmat` **(Many-Argument Workhorses)** (Impact: 143.2)
    * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call th...
  * `eval_const_expr_and_fold_it` **(Generic / Templated Code)** (Impact: 13.4)
    * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// This is a safe wrapper around ...
  * `truncate_to_uint_type_hazmat` **(Type Conversions)** (Impact: 4.6)
    * *Intent:* /// Takes a `target` which is an uint128, and a type to try to coerce it to. /// The reason this fun...
  * `truncate_to_int_type_hazmat` **(Type Conversions)** (Impact: 4.5)
    * *Intent:* /// Takes a `target` which is an int128, and a type to try to coerce it to. /// The reason this func...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 21
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 120`, `args: 13`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 22`, `state_mutation: 25`, `fragile_debt: 22`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 10`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.556
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.132862
  * `Imports (Out-Degree: 4):` crate::ast::BinOpKind, crate::ast::Constant, crate::ast::IntLiteralValue, crate::ast::UnaryOpKind, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/var_decl_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.103)
- **Top Global Matches:** file_cluster_13: 7.103, file_cluster_0: 8.264, file_cluster_15: 8.998
- **Magnitude:** 215.32 | **LOC:** 609 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.0%), Guard Balance (formerly Safety Score) (37.5%), Mutation Surface (formerly State Flux) (19.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `variable_redeclaration_without_value_allowed` **(Annotated & Test Methods)** (Impact: 9.4)
    * *Intent:* // Same as above.
  * `variable_redeclaration_with_value_allowed` **(Annotated & Test Methods)** (Impact: 9.3)
    * *Intent:* // Not allowed in semantics phase, but, this is **syntactically** correct
  * `var_decl_array` **(Annotated & Test Methods)** (Impact: 8.2)
  * `var_decl_nested_array` **(Annotated & Test Methods)** (Impact: 8.2)
  * `var_decl_deeply_nested_array` **(Annotated & Test Methods)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 22 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 75`, `args: 39`, `func_start: 38`
* *Risk/State:* `high_risk_execution: 22`, `state_mutation: 4`
* *Architecture:* `api: 24`, `import: 3`
* *Defense:* `safety: 22`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/infinite_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.174)
- **Top Global Matches:** file_cluster_13: 7.174, file_cluster_0: 7.887, file_cluster_2: 8.796
- **Magnitude:** 198.7 | **LOC:** 703 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.9%), Guard Balance (formerly Safety Score) (42.5%), Mutation Surface (formerly State Flux) (22.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `after_var_decl_with_value` **(Annotated & Test Methods)** (Impact: 9.3)
  * `below_var_decl_with_value` **(Annotated & Test Methods)** (Impact: 9.2)
  * `with_var_decl_with_value` **(Annotated & Test Methods)** (Impact: 9.2)
  * `below_var_decl_without_value` **(Annotated & Test Methods)** (Impact: 8.1)
  * `after_var_decl_without_value` **(Annotated & Test Methods)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 17 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 73`, `args: 31`, `func_start: 31`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 6`
* *Architecture:* `api: 23`, `import: 3`
* *Defense:* `safety: 17`, `test: 70`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/semantic/blackbox_tests/locking_unlocking_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.867)
- **Top Global Matches:** file_cluster_7: 6.867, file_cluster_12: 8.02, file_cluster_5: 9.018
- **Magnitude:** 185.1 | **LOC:** 875 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (57.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.6%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_assign_locked_vars_errors` **(I/O & Config Routines)** (Impact: 8.8)
  * `unlock_func_arg_in_while_loop_errors` **(Annotated & Test Methods)** (Impact: 4.2)
  * `lock_func_arg_in_while_loop_errors` **(Annotated & Test Methods)** (Impact: 4.2)
  * `lock_literal_errors` **(Annotated & Test Methods)** (Impact: 3.9)
  * `unlock_literal_errors` **(Annotated & Test Methods)** (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 303`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 42`
* *Architecture:* `api: 41`, `import: 2`
* *Defense:* `doc: 2`, `test: 117`, `sync_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163057
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/int_literal_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.773)
- **Top Global Matches:** file_cluster_13: 7.773, file_cluster_15: 9.459, file_cluster_2: 9.766
- **Magnitude:** 176.92 | **LOC:** 455 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (16.6%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `integer_literal_int16_boundary` **(Defensive Guards)** (Impact: 11.4)
  * `integer_literal_int8_boundary` **(Defensive Guards)** (Impact: 11.3)
  * `integer_literal_int32_boundary` **(Defensive Guards)** (Impact: 11.3)
  * `integer_literal_int64_boundary` **(Defensive Guards)** (Impact: 11.3)
  * `integer_literal_int128_boundary` **(Defensive Guards)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 33 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 48`, `args: 37`, `func_start: 37`
* *Risk/State:* `high_risk_execution: 33`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `safety: 33`, `test: 127`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/function_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.767)
- **Top Global Matches:** file_cluster_7: 6.767, file_cluster_12: 8.799, file_cluster_5: 9.15
- **Magnitude:** 167.02 | **LOC:** 467 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.0%), Guard Balance (formerly Safety Score) (49.4%), Mutation Surface (formerly State Flux) (40.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `function_single_return_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 11.6)
  * `function_multiple_return_one_type_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 9.6)
  * `function_multiple_return_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 9.5)
  * `function_nested_array_return_type` **(Annotated & Test Methods)** (Impact: 5.3)
  * `function_unterminated_errors` **(I/O & Config Routines)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 7`
* *Architecture:* `api: 33`, `import: 2`
* *Defense:* `safety: 1`, `test: 112`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/array_slicing_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.156)
- **Top Global Matches:** file_cluster_0: 9.156, file_cluster_13: 10.157, file_cluster_12: 10.212
- **Magnitude:** 163.34 | **LOC:** 455 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.7%), Guard Balance (formerly Safety Score) (40.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `array_slice_both_bounds_in_const` **(Annotated & Test Methods)** (Impact: 9.2)
  * `array_slice_open_start_in_const` **(Annotated & Test Methods)** (Impact: 9.2)
  * `array_slice_open_end_in_const` **(Annotated & Test Methods)** (Impact: 9.2)
  * `array_slice_both_bounds_in_var_decl` **(Defensive Guards)** (Impact: 9.0)
  * `array_slice_open_start_in_var_decl` **(Defensive Guards)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 101`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 18`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 18`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ast/types_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.423)
- **Top Global Matches:** file_cluster_13: 6.423, file_cluster_10: 7.96, file_cluster_2: 8.355
- **Magnitude:** 161.7 | **LOC:** 412 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Connectivity (formerly Api Exposure) (53.6%), Guard Balance (formerly Safety Score) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_value_all_valid_variants` **(Annotated & Test Methods)** (Impact: 8.3)
    * *Intent:* // Type::get_default_value
  * `no_type_is_both_integer_and_float` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // A type cannot be both integer AND float, ever.
  * `no_type_is_both_integer_and_array` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // No type can be both an integer and an array. Ever. //
  * `no_type_is_both_float_and_array` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // No type can be both a float and an array. Ever. //
  * `fixed_array_to_dynamic_array_type_full_pass` **(Annotated & Test Methods)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 55`, `args: 22`, `func_start: 18`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.811
  * `Choke Point (Betweenness):` 0.000449 | `Ripple Effect (Closeness):` 0.232508
  * `Imports (Out-Degree: 2):` crate::tests_consts::ALL_TYPES_NO_ARR, crate::tests_consts::ALL_TYPES_NO_ARR_NO_FLOAT, self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/semantic/branch_analysis_tests/return_branch_analysis_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.135)
- **Top Global Matches:** file_cluster_7: 6.135, file_cluster_12: 7.983, file_cluster_5: 8.23
- **Magnitude:** 159.86 | **LOC:** 914 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.9%), Connectivity (formerly Api Exposure) (58.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.4%), Debt Markers (formerly Tech Debt) (23.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infinite_statement_while_statement_nested_branch_break` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* // Nested while loops inside infinite loops breaks shouldn't be counted as breaks upstream
  * `infinite_statement_for_statement_nested_branch_break` **(Annotated & Test Methods)** (Impact: 5.8)
    * *Intent:* // Nested for loops inside infinite loops breaks shouldn't be counted as breaks upstream
  * `infinite_statement_nested_branch_break` **(Annotated & Test Methods)** (Impact: 4.2)
    * *Intent:* // Nested infinite loops inside infinite loops breaks shouldn't be counted as breaks upstream
  * `if_statement_elif_branch_inside_infinite_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 3.5)
  * `infinite_statement_inside_if_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 140`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 5`, `fragile_debt: 6`
* *Architecture:* `api: 33`, `import: 2`
* *Defense:* `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.586
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.10105
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/semantic/branch_analysis.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.046)
- **Top Global Matches:** file_cluster_1: 5.046, file_cluster_3: 48.151, file_cluster_8: 69.997
- **Magnitude:** 155.46 | **LOC:** 316 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 76.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 3.63; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.8%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `return_branch_analysis` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `dead_code_analysis` **(Many-Argument Workhorses)** (Impact: 49.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 44`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 9`, `state_mutation: 4`, `fragile_debt: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.136658
  * `Imports (Out-Degree: 1):` super::*
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/semantic/blackbox_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_0: 7.466, file_cluster_11: 7.573, file_cluster_15: 7.999
- **Magnitude:** 149.94 | **LOC:** 668 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 76.1%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **66**; blast radius 76.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.5%), Connectivity (formerly Api Exposure) (61.8%), Guard Balance (formerly Safety Score) (50.8%), Mutation Surface (formerly State Flux) (15.2%)
- **Documentation Coverage:** 91.5493% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_non_boolean_conditions` **(I/O & Config Routines)** (Impact: 8.3)
  * `get_many_boolean_conditions` **(I/O & Config Routines)** (Impact: 7.7)
  * `get_many_boolean_conditions_no_dyn_arr` **(I/O & Config Routines)** (Impact: 7.7)
  * `void_func` **(Generic / Templated Code)** (Impact: 4.7)
    * *Intent:* /// Build a void function (no return type) with the given body.
  * `contains_array_literal` **(State Mutators)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 75`, `args: 46`, `func_start: 45`
* *Risk/State:* `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 76.378
  * `Choke Point (Betweenness):` 0.157435 | `Ripple Effect (Closeness):` 0.286981
  * `Imports (Out-Degree: 35):` array_tests, bin_op_tests, break_stmt_tests, const_tests, continue_stmt_tests, copy_tests, dyn_array_access_tests, dyn_array_slicing_tests...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/semantic/branch_analysis_tests/dead_code_analysis_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.808)
- **Top Global Matches:** file_cluster_5: 6.808, file_cluster_12: 7.694, file_cluster_7: 7.894
- **Magnitude:** 146.78 | **LOC:** 746 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.5%), Guard Balance (formerly Safety Score) (49.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.3%), Mutation Surface (formerly State Flux) (12.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `for_statement_branch_multiple_return_errors` **(Annotated & Test Methods)** (Impact: 4.7)
  * `if_statement_main_branch_multiple_return_errors` **(Annotated & Test Methods)** (Impact: 4.7)
  * `if_statement_else_branch_multiple_return_errors` **(Annotated & Test Methods)** (Impact: 4.7)
  * `if_statement_elif_branch_multiple_return_errors` **(Annotated & Test Methods)** (Impact: 4.7)
  * `while_statement_branch_multiple_return_errors` **(Annotated & Test Methods)** (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 120`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `import: 2`
* *Defense:* `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.586
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.10105
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/blackbox_tests/const_decl_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.615)
- **Top Global Matches:** file_cluster_13: 7.615, file_cluster_12: 8.855, file_cluster_0: 9.008
- **Magnitude:** 146.26 | **LOC:** 432 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (50.8%), Guard Balance (formerly Safety Score) (37.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `const_decl_in_if_else_branch` **(Annotated & Test Methods)** (Impact: 8.2)
  * `const_decl_in_if_main_branch` **(Annotated & Test Methods)** (Impact: 8.1)
  * `const_decl_in_if_elif_branch` **(Annotated & Test Methods)** (Impact: 8.1)
  * `const_decl_in_infinite_loop` **(Annotated & Test Methods)** (Impact: 8.0)
  * `const_decl_in_while_loop` **(Annotated & Test Methods)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 60`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 15`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `safety: 15`, `test: 68`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164092
  * `Imports (Out-Degree: 1):` self::*, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/semantic/blackbox_tests.rs` (RUST) | Magnitude: 149.94 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 370, structural_boundaries: 75, args: 46, func_start: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/parser/blackbox_tests.rs` (RUST) | Magnitude: 41.68 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 47, test: 23, args: 12
- `src/semantic/blackbox_tests/fixed_array_slicing_tests.rs` (RUST) | Magnitude: 30.76 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 51, core_var_decl: 36, design_snake_case: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/ast.rs` (RUST) | Magnitude: 24.56 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 16, api: 9, doc: 9, decorators: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/parser/parse_expr_tests/array_slicing_tests.rs` (RUST) | Magnitude: 41.34 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, branch: 19, test: 15, structural_boundaries: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/semantic.rs` -> Churn: **100.0%** | Cog Load: 14.5578% | Debt: 57.7189%
- `src/semantic/infer.rs` -> Churn: **87.37%** | Cog Load: 12.0709% | Debt: 67.6748%
- `src/semantic/branch_analysis.rs` -> Churn: **72.77%** | Cog Load: 18.3111% | Debt: 98.7639%
- `src/semantic/helpers.rs` -> Churn: **69.62%** | Cog Load: 9.7917% | Debt: 82.0223%
- `src/transpiler.rs` -> Churn: **60.48%** | Cog Load: 41.9212% | Debt: 74.8749%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/semantic.rs` -> **chadsec1** (80.5% isolated ownership) | Magnitude: 529.84
- `src/semantic/blackbox_tests/const_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 447.72
- `src/parser/blackbox_tests/while_stmt_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 432.9
- `src/semantic/blackbox_tests/ownership_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 391.26
- `src/transpiler.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 351.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/parser.rs` -> **Severity: 12.582** (Bridge: 0.1287 * Flux: 97.783%)
- `src/parser/parse_expr_tests.rs` -> **Severity: 10.541** (Bridge: 0.1145 * Flux: 92.0451%)
- `src/semantic.rs` -> **Severity: 5.228** (Bridge: 0.0749 * Flux: 69.8386%)
- `src/semantic/blackbox_tests.rs` -> **Severity: 2.399** (Bridge: 0.1574 * Flux: 15.2401%)
- `src/parser/helpers.rs` -> **Severity: 0.484** (Bridge: 0.0048 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/ast/types.rs` -> **Severity: 23.458** (Embedded: 0.3893 * Error Risk: 60.2551%)
- `src/ast/int_literal_value.rs` -> **Severity: 18.731** (Embedded: 0.3263 * Error Risk: 57.3963%)
- `src/semantic/blackbox_tests.rs` -> **Severity: 14.582** (Embedded: 0.287 * Error Risk: 50.8123%)
- `src/parser.rs` -> **Severity: 14.036** (Embedded: 0.2342 * Error Risk: 59.9449%)
- `src/parser/blackbox_tests.rs` -> **Severity: 12.101** (Embedded: 0.2573 * Error Risk: 47.0341%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/parser/blackbox_tests.rs` -> **Severity: 9225.147** (Blast Radius: 118.609 * Doc Risk: 77.7778%)
- `src/ast/types.rs` -> **Severity: 8199.089** (Blast Radius: 92.923 * Doc Risk: 88.2353%)
- `src/semantic/blackbox_tests.rs` -> **Severity: 6992.352** (Blast Radius: 76.378 * Doc Risk: 91.5493%)
- `src/parser/parse_expr_tests.rs` -> **Severity: 6374.4** (Blast Radius: 63.744 * Doc Risk: 100.0%)
- `src/ast/int_literal_value.rs` -> **Severity: 3092.7** (Blast Radius: 51.545 * Doc Risk: 60.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11727 call pairs -- scoped 30.6%, unique 0.0%, ambiguous 4.1%, external 65.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 11727 | 30.6% | 0.0% | 4.1% | 65.3% |

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
