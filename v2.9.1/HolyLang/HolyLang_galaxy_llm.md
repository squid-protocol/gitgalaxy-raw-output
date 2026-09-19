# ARCHITECTURAL_BRIEF: HolyLang
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/chadsec1/HolyLang` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 104 analyzed artifact(s), 26355 LOC.
- **Load-bearing artifact:** none identifiable. No file in this repository is imported by another that GitGalaxy could resolve, so there is no dependency hierarchy to report. That is itself a finding: either this is a collection of independent scripts/documents rather than a coupled system, or the import style is one the engine does not resolve for these languages.
- **Top orchestrator:** `src/semantic/blackbox_tests.rs` -- pulls in 37 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/parser/blackbox_tests/while_stmt_tests.rs` at magnitude 637.9 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 104 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 26355 |
| Volatility Index | 0.058 |
| % Scanned of codebase = | 93.7% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 103 | 26355 | 99.0% |
| MARKDOWN | 1 | 0 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `2.27`
> **Composition Archetype:** `Small Flat Repo` (z +2.27; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 36%, Large Core Modules 29%, Large Core Modules (2) 9%, State Mutators Files 7%, Large Core Modules (3) 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 103 | 99.0% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 47.7 | 10.6 | 7.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 40.3 | 44.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 78.0 | 92.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 9.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 45.0 | 2.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.6 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.3 | 40.9 | 14.4 | 15.5 | 1.6 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 9.2 | 100.0 | 35.5 | 31.0 | 31.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1179 | 60 | 26 | `src/semantic/blackbox_tests/const_tests.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 745 | 57 | 21 | `src/parser/blackbox_tests/while_stmt_tests.rs` |
| danger | 2113 | 87 | 44 | `src/semantic/blackbox_tests/ownership_tests.rs` |
| concurrency | 149 | 9 | 0 | `src/parser/blackbox_tests/lock_stmt_tests.rs` |
| connectivity | 142 | 20 | 3 | `src/ast/stmts.rs` |
| io | 5 | 2 | 0 | `src/compile.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 4166 | 83 | 96 | `src/semantic/blackbox_tests/const_tests.rs` |
| docs | 234 | 28 | 6 | `src/semantic/blackbox_tests/if_stmt_tests.rs` |
| debt | 133 | 24 | 3 | `src/semantic/constants.rs` |
| mutation | 4493 | 95 | 109 | `src/semantic/blackbox_tests/const_tests.rs` |
| dead_code | 1148 | 94 | 27 | `src/semantic/blackbox_tests/const_tests.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 28 | 10 | 0 | `src/parser/parse_expr_tests/float64_literal_tests.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0625**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/compile.rs` (Hits: 4)
- `src/main.rs` (Hits: 1)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blackbox_tests.rs** (`src/semantic/blackbox_tests.rs`) — 37 outbound dependencies
2. **transpiler.rs** (`src/transpiler.rs`) — 11 outbound dependencies
3. **semantic.rs** (`src/semantic.rs`) — 10 outbound dependencies
4. **compile.rs** (`src/compile.rs`) — 9 outbound dependencies
5. **branch_analysis_tests.rs** (`src/semantic/branch_analysis_tests.rs`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check_stmts` **(Many-Argument Workhorses)** (@ `src/semantic.rs`) -> Impact: **393.5** | LOC: 779
  * *Intent:* /// Parse holylang statements in a block, it does: /// Enforce language semantics, and ownership safety model, check function calls, etc.
- `infer_expr_type` **(Many-Argument Workhorses)** (@ `src/semantic/infer.rs`) -> Impact: **311.9** | LOC: 647
  * *Intent:* /// Infer the type of an expression, and update literal nodes (and nested nodes) where possible. /// Returns the deduced Type for the expression. /// ...
- `parse_expr` **(Many-Argument Workhorses)** (@ `src/parser/parse_expr.rs`) -> Impact: **199.6** | LOC: 528
  * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary operations (like negate, logical not, bitwise not ) ///...
- `eval_const_expr_and_fold_it_hazmat` **(Many-Argument Workhorses)** (@ `src/semantic/constants.rs`) -> Impact: **143.2** | LOC: 612
  * *Intent:* /// Evaluate a constant expression and fold it into a literal /// /// IMPORTANT NOTE: Do NOT call this function directly unless you 1000% know what yo...
- `return_branch_analysis` **(Many-Argument Workhorses)** (@ `src/semantic/branch_analysis.rs`) -> Impact: **123.1** | LOC: 181
- `parse_stmt_line` **(Many-Argument Workhorses)** (@ `src/parser.rs`) -> Impact: **100.1** | LOC: 236
  * *Intent:* /// Parse a single statement from a comments-removed trimmed line. `line_no` used for error messages.
- `for_statements_invalid_construction_errors` **(I/O & Config Routines)** (@ `src/parser/blackbox_tests/for_stmt_tests.rs`) -> Impact: **67.4** | LOC: 88
- `parse_function` **(Many-Argument Workhorses)** (@ `src/parser.rs`) -> Impact: **65.0** | LOC: 123
  * *Intent:* /// Parse function starting at index `start_i`. /// Returns (Function, index after function end).
- `if_statements_invalid_construction_errors` **(I/O & Config Routines)** (@ `src/parser/blackbox_tests/if_stmt_tests.rs`) -> Impact: **63.1** | LOC: 83
- `invalid_construction_errors` **(I/O & Config Routines)** (@ `src/parser/blackbox_tests/while_stmt_tests.rs`) -> Impact: **63.1** | LOC: 83

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/parser/blackbox_tests` | 27 | 3658.44 | 14.76% | 88.59% |
| `src/semantic/blackbox_tests` | 29 | 2003.02 | 6.45% | 77.75% |
| `src` | 10 | 1602.48 | 14.21% | 36.56% |
| `src/semantic` | 7 | 1101.12 | 11.45% | 89.66% |
| `src/parser` | 5 | 868.06 | 17.54% | 64.56% |
| `src/parser/parse_expr_tests` | 14 | 441.48 | 8.99% | 99.05% |
| `src/ast` | 9 | 403.46 | 6.57% | 53.9% |
| `src/semantic/branch_analysis_tests` | 2 | 273.44 | 6.97% | 99.71% |
| `__monolith__` | 1 | 4.9 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/ast/int_literal_value_tests.rs` -> **100.0%** Exposure
- `src/ast/int_literal_value.rs` -> **99.9995%** Exposure
- `src/parser/parse_expr_tests/float64_literal_tests.rs` -> **99.9992%** Exposure
- `src/parser/helpers_tests.rs` -> **99.9991%** Exposure
- `src/parser/parse_expr_tests/format_call_tests.rs` -> **99.9968%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/transpiler.rs` -> **100.0%** Exposure
- `src/parser/helpers.rs` -> **99.9999%** Exposure
- `src/compile.rs` -> **99.9254%** Exposure
- `src/ast/types_tests.rs` -> **99.6789%** Exposure
- `src/parser.rs` -> **97.783%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/semantic/blackbox_tests/const_tests.rs` -> **111** Orphaned Functions | **0** Duplicates
- `src/parser/helpers_tests.rs` -> **89** Orphaned Functions | **0** Duplicates
- `src/semantic/blackbox_tests/ownership_tests.rs` -> **46** Orphaned Functions | **0** Duplicates
- `src/semantic/blackbox_tests/locking_unlocking_tests.rs` -> **41** Orphaned Functions | **0** Duplicates
- `src/parser/blackbox_tests/int_literal_tests.rs` -> **37** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `217` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/parser/blackbox_tests/while_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 637.9 | **LOC:** 1181 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (83.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.0%), Mutation Surface (formerly State Flux) (36.2%), Complexity Load (formerly Cognitive Load) (36.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_construction_errors` **(I/O & Config Routines)** (Impact: 63.1)
  * `invalid_construction_errors` **(I/O & Config Routines)** (Impact: 62.0)
  * `trailing_kw_errors` **(I/O & Config Routines)** (Impact: 46.0)
  * `vars_and_literals_spaces_before_expr` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* // Same test as above, but before the expression, there is an `i` of spaces.
  * `vars_and_literals_spaces_after_expr` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* // Same test as above, but after the expression, there is an `i` of spaces.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 67 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 147`, `args: 43`, `func_start: 43`
* *Risk/State:* `high_risk_execution: 67`, `state_mutation: 16`, `unreferenced_by_name: 37`
* *Architecture:* `import: 3`
* *Defense:* `safety: 67`, `test: 148`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 578.84 | **LOC:** 1098 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 80.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (87.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.2%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_stmts` **(Many-Argument Workhorses)** (Impact: 393.5)
    * *Intent:* /// Parse holylang statements in a block, it does: /// Enforce language semantics, and ownership saf...
  * `check_call` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /// Validate a call's arguments, infer literal arg types to parameter types, /// and apply move sema...
  * `check_function` **(Many-Argument Workhorses)** (Impact: 19.5)
    * *Intent:* /// Check single function, infer local var types where possible, check calls, returns.
  * `update_local_assignments_from_clone` **(Defensive Guards)** (Impact: 13.2)
  * `check_semantics` **(Generic / Templated Code)** (Impact: 11.2)
    * *Intent:* /// Checks semantics and fill in inferred types where possible. /// This mutates the AST, because in...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 193`, `args: 19`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `state_mutation: 31`, `dead_code: 4`, `fragile_debt: 14`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 25`, `doc: 14`, `test: 5`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Constant, Expr, Function, GlobalStmt, Span, Stmt, Type, crate::ast::
    AST...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 519.82 | **LOC:** 905 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 73.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_stmt_line` **(Many-Argument Workhorses)** (Impact: 100.1)
    * *Intent:* /// Parse a single statement from a comments-removed trimmed line. `line_no` used for error messages...
  * `parse_function` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* /// Parse function starting at index `start_i`. /// Returns (Function, index after function end).
  * `parse_block` **(Compute Cores)** (Impact: 43.0)
  * `parse_if_stmt` **(Compute Cores)** (Impact: 42.1)
  * `parse_for_stmt` **(Compute Cores)** (Impact: 38.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 241`, `args: 35`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 7`, `state_mutation: 32`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 9`, `doc: 9`, `test: 3`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ast::*, crate::error::HolyError
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/if_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 466.5 | **LOC:** 878 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (69.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.5%), Complexity Load (formerly Cognitive Load) (28.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (18.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `if_statements_invalid_construction_errors` **(I/O & Config Routines)** (Impact: 63.1)
  * `if_statements_trailing_kw_errors` **(I/O & Config Routines)** (Impact: 51.2)
  * `if_statements_with_elif_vars_and_literals` **(Defensive Guards)** (Impact: 39.5)
  * `if_statements_vars_and_literals` **(Defensive Guards)** (Impact: 25.9)
  * `if_statements_trailing_types_errors` **(I/O & Config Routines)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 78 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 120`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 78`, `state_mutation: 2`, `unreferenced_by_name: 22`
* *Architecture:* `import: 2`
* *Defense:* `safety: 78`, `test: 167`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/infer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 411.78 | **LOC:** 775 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (67.7%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infer_expr_type` **(Many-Argument Workhorses)** (Impact: 311.9)
    * *Intent:* /// Infer the type of an expression, and update literal nodes (and nested nodes) where possible. ///...
  * `advanced_infer_2_types` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /// This takes 2 expressions, and tries to get types, and convert each other types to the same type ...
  * `check_usize_literal_to_src` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* // helper: check an expression that's allowed to be an IntLiteral::Usize
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 123`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 7`, `state_mutation: 9`, `dead_code: 3`, `planned_debt: 8`, `fragile_debt: 8`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 16`, `doc: 16`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArraySliceRange, BinOpKind, FixedArraySize, UnaryOpKind, crate::ast::
    IntLiteralValue, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/transpiler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 382.96 | **LOC:** 492 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Debt Markers (formerly Tech Debt) (96.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transpile_stmt` **(Compute Cores)** (Impact: 59.8)
    * *Intent:* /// Transpiles a statement into equivlent Rust code ///
  * `holy_expr_to_rust_expr` **(Defensive Guards)** (Impact: 38.4)
    * *Intent:* /// Turns a HolyLang expression, into equvilent Rust expression ///
  * `transpile_function` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /// Transpiles a function and its inner statements into equvilent Rust code ///
  * `holy_type_to_rust_type_str` **(State Mutators)** (Impact: 5.5)
    * *Intent:* /// Turns a holylang type e.g. Int32, Int64, etc, into equvilent Rust type ///
  * `transpile` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /// Takes a reference to a Abstract Syntax Tree, and returns equvilent code in Rust as a string ///
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 77 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 84`, `args: 16`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 13`, `state_mutation: 92`, `planned_debt: 1`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 13`, `doc: 12`, `sync_locks: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArraySliceRange, BinOpKind, Constant, Expr, FixedArraySize, Function, GlobalStmt, Stmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/const_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 367.72 | **LOC:** 2269 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.0%), Guard Balance (formerly Safety Score) (47.3%), Mutation Surface (formerly State Flux) (8.8%)
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
* *Structure:* `branch: 112`, `structural_boundaries: 853`, `args: 112`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 111`, `high_risk_execution: 15`, `state_mutation: 1`, `unreferenced_by_name: 111`
* *Architecture:* `import: 6`
* *Defense:* `safety: 12`, `test: 378`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/ownership_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 355.26 | **LOC:** 1733 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (68.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.3%), Guard Balance (formerly Safety Score) (23.0%), Complexity Load (formerly Cognitive Load) (7.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vardecl_in_if_else_branch_moves_upstream_var` **(I/O & Config Routines)** (Impact: 16.1)
  * `vardecl_in_if_elif_branch_moves_upstream_var` **(I/O & Config Routines)** (Impact: 16.1)
  * `vardecl_in_if_main_branch_does_not_move_upstream_const` **(I/O & Config Routines)** (Impact: 16.0)
  * `vardecl_moving_local_var_in_if_stmt_elif_branch` **(I/O & Config Routines)** (Impact: 13.8)
  * `vardecl_moving_local_var_in_if_stmt_else_branch` **(I/O & Config Routines)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 55 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 415`, `args: 46`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 55`, `unreferenced_by_name: 46`
* *Architecture:* `import: 2`
* *Defense:* `safety: 55`, `doc: 5`, `test: 330`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/helpers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 348.68 | **LOC:** 427 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 72.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.2%)
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
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 51`, `dead_code: 4`, `fragile_debt: 6`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 15`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::consts, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/bin_op_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 311.56 | **LOC:** 1078 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (83.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.0%), Guard Balance (formerly Safety Score) (32.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
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
* *Risk/State:* `high_risk_execution: 54`, `unreferenced_by_name: 34`
* *Architecture:* `import: 3`
* *Defense:* `safety: 46`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/for_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 286.68 | **LOC:** 469 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.8%), Complexity Load (formerly Cognitive Load) (31.0%), Guard Balance (formerly Safety Score) (25.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `for_statements_invalid_construction_errors` **(I/O & Config Routines)** (Impact: 67.4)
  * `for_statements_trailing_kw_errors` **(I/O & Config Routines)** (Impact: 46.0)
  * `for_statements_trailing_types_errors` **(I/O & Config Routines)** (Impact: 24.6)
  * `for_statements_trailing_exprs_errors` **(I/O & Config Routines)** (Impact: 23.6)
  * `for_statements_literal` **(Defensive Guards)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 40`, `args: 22`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 3`, `planned_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `import: 2`
* *Defense:* `safety: 13`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/parse_expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 237.96 | **LOC:** 544 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.6%), Mutation Surface (formerly State Flux) (70.3%), Guard Balance (formerly Safety Score) (50.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_expr` **(Many-Argument Workhorses)** (Impact: 199.6)
    * *Intent:* /// Expression parser: /// - handles binary operations (left-associative), /// - handles unary opera...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 115`, `args: 8`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 17`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ast::*, helpers, super::HolyError
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/break_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 232.06 | **LOC:** 493 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.2%), Complexity Load (formerly Cognitive Load) (24.5%), Guard Balance (formerly Safety Score) (21.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_errors` **(I/O & Config Routines)** (Impact: 48.4)
  * `invalid_errors` **(I/O & Config Routines)** (Impact: 48.4)
  * `in_if_with_else_with_elif_stmt` **(Annotated & Test Methods)** (Impact: 8.1)
  * `in_if_else_with_elif_stmt` **(Annotated & Test Methods)** (Impact: 8.0)
  * `in_if_with_else_stmt` **(Annotated & Test Methods)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *High Risk Execution (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 52`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 11`, `unreferenced_by_name: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/continue_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 232.06 | **LOC:** 493 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.1%), Complexity Load (formerly Cognitive Load) (24.5%), Guard Balance (formerly Safety Score) (23.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_errors` **(I/O & Config Routines)** (Impact: 48.4)
  * `invalid_errors` **(I/O & Config Routines)** (Impact: 48.4)
  * `in_if_with_else_with_elif_stmt` **(Annotated & Test Methods)** (Impact: 8.1)
  * `in_if_else_with_elif_stmt` **(Annotated & Test Methods)** (Impact: 8.0)
  * `in_if_with_else_stmt` **(Annotated & Test Methods)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *High Risk Execution (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 52`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 11`, `unreferenced_by_name: 24`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/constants.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 230.62 | **LOC:** 692 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (90.9%), Mutation Surface (formerly State Flux) (86.7%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `high_risk_execution: 22`, `state_mutation: 25`, `fragile_debt: 22`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 10`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BinOpKind, Constant, UnaryOpKind, crate::ast::
    IntLiteralValue, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/helpers_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 207.2 | **LOC:** 1275 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 70.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.2%), Guard Balance (formerly Safety Score) (26.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (12.5%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unescaped_inner_double_quote_is_error` **(Annotated & Test Methods)** (Impact: 36.5)
  * `empty_string_literal_as_arg` **(Annotated & Test Methods)** (Impact: 13.8)
  * `whitespace_only_placeholder_is_captured` **(Annotated & Test Methods)** (Impact: 4.5)
  * `braces_inside_double_quotes_not_counted` **(Annotated & Test Methods)** (Impact: 4.0)
  * `backslash_escaped_quote_inside_string` **(Annotated & Test Methods)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 147`, `args: 167`, `func_start: 157`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 1`, `fragile_debt: 4`, `unreferenced_by_name: 89`
* *Architecture:* `import: 13`
* *Defense:* `doc: 5`, `test: 369`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::consts, crate::tests_consts::
    ALL_TYPES_NO_ARR, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/branch_analysis.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 198.16 | **LOC:** 316 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 76.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `return_branch_analysis` **(Many-Argument Workhorses)** (Impact: 123.1)
  * `dead_code_analysis` **(Many-Argument Workhorses)** (Impact: 56.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 44`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 9`, `state_mutation: 4`, `dead_code: 2`, `fragile_debt: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/var_decl_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 191.32 | **LOC:** 609 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.0%), Mutation Surface (formerly State Flux) (19.9%), Guard Balance (formerly Safety Score) (17.7%)
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
* *Risk/State:* `high_risk_execution: 22`, `state_mutation: 4`, `unreferenced_by_name: 24`
* *Architecture:* `import: 3`
* *Defense:* `safety: 22`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/infinite_stmt_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 175.7 | **LOC:** 703 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (84.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.9%), Guard Balance (formerly Safety Score) (28.8%), Mutation Surface (formerly State Flux) (22.5%)
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
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 6`, `unreferenced_by_name: 23`
* *Architecture:* `import: 3`
* *Defense:* `safety: 17`, `test: 70`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast/types_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 151.7 | **LOC:** 412 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Debt Markers (formerly Tech Debt) (95.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.5%), Guard Balance (formerly Safety Score) (37.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_value_all_valid_variants` **(Annotated & Test Methods)** (Impact: 9.3)
    * *Intent:* // Type::get_default_value
  * `no_type_is_both_integer_and_float` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // A type cannot be both integer AND float, ever.
  * `no_type_is_both_integer_and_array` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // No type can be both an integer and an array. Ever. //
  * `no_type_is_both_float_and_array` **(Annotated & Test Methods)** (Impact: 7.2)
    * *Intent:* // No type can be both a float and an array. Ever. //
  * `fixed_array_to_dynamic_array_type_full_pass` **(Annotated & Test Methods)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 55`, `args: 22`, `func_start: 18`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `import: 3`
* *Defense:* `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ALL_TYPES_NO_ARR_NO_FLOAT, crate::tests_consts::
    ALL_TYPES_NO_ARR, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/const_decl_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 149.26 | **LOC:** 432 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (85.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%), Guard Balance (formerly Safety Score) (17.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `const_decl_in_if_else_branch` **(Annotated & Test Methods)** (Impact: 11.2)
  * `const_decl_in_if_main_branch` **(Annotated & Test Methods)** (Impact: 10.1)
  * `const_decl_in_if_elif_branch` **(Annotated & Test Methods)** (Impact: 10.1)
  * `const_decl_in_while_loop` **(Annotated & Test Methods)** (Impact: 10.0)
  * `const_decl_in_for_branch` **(Annotated & Test Methods)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 60`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 15`, `unreferenced_by_name: 14`
* *Architecture:* `import: 3`
* *Defense:* `safety: 15`, `test: 68`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/function_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 148.02 | **LOC:** 467 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (48.1%), Mutation Surface (formerly State Flux) (40.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `function_unterminated_errors` **(I/O & Config Routines)** (Impact: 14.2)
  * `function_single_return_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 13.6)
  * `function_multiple_return_one_type_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 9.6)
  * `function_multiple_return_invalid_type_errors` **(Annotated & Test Methods)** (Impact: 9.5)
  * `function_nested_array_return_type` **(Annotated & Test Methods)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 7`, `unreferenced_by_name: 33`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 112`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/branch_analysis_tests/return_branch_analysis_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 145.86 | **LOC:** 914 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (65.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.4%), Mutation Surface (formerly State Flux) (14.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `if_statement_elif_branch_inside_infinite_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 6.5)
  * `infinite_statement_inside_if_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 6.5)
  * `if_statement_main_branch_inside_infinite_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 6.4)
    * *Intent:* // Same as above, but this is an if statement, inside infinite statement..
  * `if_statement_else_branch_inside_infinite_stmt_break_errors` **(Annotated & Test Methods)** (Impact: 6.4)
  * `infinite_statement_while_statement_nested_branch_break` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* // Nested while loops inside infinite loops breaks shouldn't be counted as breaks upstream
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 140`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 5`, `fragile_debt: 6`, `unreferenced_by_name: 33`
* *Architecture:* `import: 2`
* *Defense:* `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/blackbox_tests/array_slicing_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 144.34 | **LOC:** 455 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%), Guard Balance (formerly Safety Score) (23.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.7%)
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 18`, `unreferenced_by_name: 19`
* *Architecture:* `import: 3`
* *Defense:* `safety: 18`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/semantic/blackbox_tests/locking_unlocking_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 144.1 | **LOC:** 875 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.615; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.8%), Guard Balance (formerly Safety Score) (57.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.6%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_assign_locked_vars_errors` **(I/O & Config Routines)** (Impact: 8.8)
  * `unlock_func_arg_in_while_loop_errors` **(Annotated & Test Methods)** (Impact: 4.2)
  * `lock_func_arg_in_while_loop_errors` **(Annotated & Test Methods)** (Impact: 4.2)
  * `lock_literal_errors` **(Annotated & Test Methods)** (Impact: 3.9)
  * `unlock_literal_errors` **(Annotated & Test Methods)** (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 303`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 42`, `unreferenced_by_name: 41`
* *Architecture:* `import: 2`
* *Defense:* `doc: 2`, `test: 117`, `sync_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/semantic.rs` -> Churn: **100.0%** | Cog Load: 24.8228% | Debt: 87.1878%
- `src/semantic/blackbox_tests.rs` -> Churn: **95.52%** | Cog Load: 6.7829% | Debt: 93.8854%
- `src/semantic/infer.rs` -> Churn: **87.37%** | Cog Load: 12.7266% | Debt: 67.6748%
- `src/semantic/branch_analysis_tests.rs` -> Churn: **83.65%** | Cog Load: 5.3298% | Debt: 84.1131%
- `src/parser/blackbox_tests.rs` -> Churn: **75.07%** | Cog Load: 5.0487% | Debt: 70.0417%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/parser/blackbox_tests/while_stmt_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 637.9
- `src/semantic.rs` -> **chadsec1** (80.5% isolated ownership) | Magnitude: 578.84
- `src/parser/blackbox_tests/if_stmt_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 466.5
- `src/transpiler.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 382.96
- `src/semantic/blackbox_tests/const_tests.rs` -> **ChadSec** (100.0% isolated ownership) | Magnitude: 367.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ast/fmt_display.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/ast/fmt_display_tests.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/ast/int_literal_value_tests.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/ast/types_tests.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)
- `src/compile.rs` -> **Severity: 961.5** (Blast Radius: 9.615 * Doc Risk: 100.0%)

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
