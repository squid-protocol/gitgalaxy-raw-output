# ARCHITECTURAL_BRIEF: ruff
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1918 analyzed artifact(s), 255347 LOC.
- **Load-bearing artifact:** `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -- 705 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` -- pulls in 132 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` at magnitude 1418.08 (structural weight, not risk).
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
| Total Artifacts | 3289 |
| Analyzed Artifacts (Scanned) | 1918 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1371 |
| Total LOC | 255347 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 58.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2298 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4227 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0074 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 22 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1440 | 251443 | 75.1% |
| PYTHON | 442 | 3888 | 23.0% |
| XML | 23 | 16 | 1.2% |
| MARKDOWN | 11 | 0 | 0.6% |
| PLAINTEXT | 2 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `3.467`
> **Composition Archetype:** `Flat Modular Platform` (z +3.47; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 23%, Data / Markup / Trivial 22%, Declarative / Non-Code 14%, Large Core Modules (3) 14%, Generic / Templated Code Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1904 | 99.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1371*

**Composition by Extension & Reason:**
- `.snap`: 1142x Excluded (Unsupported Extension: '.snap'), 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 98x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 53x Excluded (Unsupported Extension: '.toml')
- `.rs`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1253 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1596 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.dot`: 1x Excluded (Unsupported Extension: '.dot')
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 469 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.4 | 4.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 22.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 36.4 | 25.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.1 | 2.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.6 | 44.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10235 | 1321 | 13 | `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` |
| cleanup | 10 | 5 | 0 | `ruff-0.15.9/crates/ruff_linter/src/rules/pandas_vet/mod.rs` |
| guards | 9040 | 1316 | 10 | `ruff-0.15.9/crates/ruff_python_codegen/src/generator.rs` |
| danger | 2210 | 405 | 2 | `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` |
| concurrency | 585 | 183 | 0 | `ruff-0.15.9/crates/ruff/src/cache.rs` |
| connectivity | 10487 | 1495 | 13 | `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` |
| io | 222 | 61 | 0 | `ruff-0.15.9/crates/ruff_db/src/system/os.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 9 | 0 | `ruff-0.15.9/python/ruff/__main__.py` |
| time | 9 | 7 | 0 | `ruff-0.15.9/crates/ruff/src/cache.rs` |
| serialization | 24 | 7 | 0 | `ruff-0.15.9/crates/ruff_workspace/src/pyproject.rs` |
| regex | 32 | 25 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/tests/normalizer.rs` |
| events | 214 | 54 | 0 | `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` |
| tests | 3704 | 270 | 1 | `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` |
| docs | 58305 | 1233 | 62 | `ruff-0.15.9/crates/ruff_formatter/src/builders.rs` |
| debt | 848 | 212 | 1 | `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` |
| mutation | 22554 | 1288 | 26 | `ruff-0.15.9/crates/ruff_workspace/src/options.rs` |
| dead_code | 5473 | 1172 | 5 | `ruff-0.15.9/crates/ruff_formatter/src/builders.rs` |
| credential | 1 | 1 | 0 | `ruff-0.15.9/crates/ruff_linter/src/rules/refurb/rules/hardcoded_string_charset.rs` |
| threat | 60 | 27 | 0 | `ruff-0.15.9/crates/ruff_cache/src/cache_key.rs` |
| ml_ai | 64 | 37 | 0 | `ruff-0.15.9/crates/ruff_linter/src/rules/refurb/rules/math_constant.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ruff-0.15.9/crates/ruff_db/src/system/os.rs` (Hits: 34)
- `ruff-0.15.9/crates/ruff_db/src/system/memory_fs.rs` (Hits: 20)
- `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **derive_message_formats.rs** (`ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs`) — 705 inbound connections
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

- `expression` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs`) -> Impact: **515.5** | LOC: 991
  * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
- `statement` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs`) -> Impact: **492.6** | LOC: 1087
  * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
- `format_line` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs`) -> Impact: **294.1** | LOC: 481
  * *Intent:* // Adapted from https://github.com/rust-lang/rust/blob/d371d17496f2ce3a56da76aa083f4ef157572c20/compiler/rustc_errors/src/emitter.rs#L706-L1211
- `visit_expr` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`) -> Impact: **219.1** | LOC: 607
- `fmt` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_python_formatter/src/statement/suite.rs`) -> Impact: **211.5** | LOC: 350
- `visit_stmt` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`) -> Impact: **195.9** | LOC: 697
- `check_noqa` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/noqa.rs`) -> Impact: **195.7** | LOC: 254
  * *Intent:* /// RUF100
- `definition` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_annotations/rules/definition.rs`) -> Impact: **183.3** | LOC: 346
  * *Intent:* /// Generate flake8-annotation checks for a given `Definition`. /// ANN001, ANN401
- `fmt` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_formatter/src/format_element/document.rs`) -> Impact: **172.4** | LOC: 400
- `path_exists_case_sensitive_fast` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_db/src/system/os.rs`) -> Impact: **170.2** | LOC: 667
  * *Intent:* /// Path sensitive testing if a path exists by canonicalization the path and comparing it with `path`. /// /// This is faster than the slow path, beca...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ruff-0.15.9/crates/ruff_python_ast/src` | 25 | 4336.98 | 7.32% | 31.53% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules` | 75 | 4276.58 | 5.83% | 54.13% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules` | 110 | 4182.2 | 5.27% | 65.72% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules` | 43 | 3034.78 | 7.01% | 63.47% |
| `ruff-0.15.9/crates/ruff_linter/src` | 21 | 2730.82 | 6.51% | 55.1% |
| `ruff-0.15.9/crates/ruff_python_parser/src` | 8 | 2472.76 | 9.3% | 52.63% |
| `ruff-0.15.9/crates/ruff_workspace/src` | 5 | 2426.12 | 9.85% | 9.78% |
| `ruff-0.15.9/crates/ruff_python_parser/src/parser` | 9 | 2402.1 | 7.92% | 24.27% |
| `ruff-0.15.9/crates/ty_module_resolver/src` | 11 | 2269.58 | 5.26% | 53.77% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules` | 43 | 2184.18 | 5.34% | 72.79% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ruff-0.15.9/crates/ruff_linter/src/preview.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_fixme/rules/todos.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_todos/rules/todos.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/violation.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/src/str_prefix.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ruff-0.15.9/crates/ruff_linter/src/rules/isort/format.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/settings/rule_table.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_number_literal.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_trivia/src/comment_ranges.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/generate.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ruff-0.15.9/crates/ruff/tests/cli/lint.rs` -> **95** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_python_semantic/src/model.rs` -> **85** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs` -> **77** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_python_parser/src/string.rs` -> **69** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_linter/src/preview.rs` -> **63** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18167` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1418.08 | **LOC:** 3764 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **132**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.0%), Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 35.6436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_expr` **(Many-Argument Workhorses)** (Impact: 219.1)
  * `visit_stmt` **(Many-Argument Workhorses)** (Impact: 195.9)
  * `handle_node_store` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `add_binding` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* /// Add a [`Binding`] to the current scope, bound to the given name.
  * `report_semantic_error` **(Many-Argument Workhorses)** (Impact: 31.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 396`, `args: 181`, `func_start: 124`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 126`, `dead_code: 12`, `planned_debt: 11`
* *Architecture:* `api: 86`, `concurrency: 1`, `import: 44`
* *Defense:* `safety: 71`, `doc: 391`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AnyParameterRef, ArgOrKeyword, BindingId, BindingKind, Comprehension, Diagnostic, DiagnosticTag, DunderAllFlags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/lexer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1248.2 | **LOC:** 3203 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (89.7%), Mutation Surface (formerly State Flux) (88.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%)
- **Documentation Coverage:** 73.4177% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consume_ascii_character` **(Many-Argument Workhorses)** (Impact: 139.1)
    * *Intent:* // Dispatch based on the given character.
  * `lex_interpolated_string_middle_or_end` **(Compute Cores)** (Impact: 66.8)
    * *Intent:* /// Lex an f-string or t-string middle or end token.
  * `lex_ipython_escape_command` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* /// Lex a single IPython escape command.
  * `lex_string` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /// Lex a string literal.
  * `test_fstring_escape` **(Annotated & Test Methods)** (Impact: 44.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 322`, `args: 218`, `func_start: 194`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 6`, `state_mutation: 132`, `dead_code: 9`, `planned_debt: 1`, `unreferenced_by_name: 77`
* *Architecture:* `api: 15`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 17`, `doc: 147`, `test: 159`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EOF_CHAR, Indentations, IndentationsCheckpoint, InterpolatedStringErrorType::
            SingleRbrace, InterpolatedStrings, InterpolatedStringsCheckpoint, IpyEscapeKind, LexicalError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1171.54 | **LOC:** 3855 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Connectivity (formerly Api Exposure) (80.3%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 51.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prefix` **(Compute Cores)** (Impact: 20.8)
  * `prefix` **(Compute Cores)** (Impact: 10.8)
  * `next` **(Defensive Guards)** (Impact: 9.3)
  * `next` **(Defensive Guards)** (Impact: 9.3)
  * `next` **(Defensive Guards)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 445`, `args: 339`, `func_start: 301`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 9`, `dead_code: 8`, `planned_debt: 3`, `duplicate_logic: 61`
* *Architecture:* `api: 336`, `import: 15`
* *Defense:* `safety: 22`, `doc: 657`, `test: 50`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ByteStringPrefix, DerefMut, ExprDict, ExprFString, ExprList, ExprName, ExprRef, ExprSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 1076.4 | **LOC:** 4638 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.7%), Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (46.6%)
- **Documentation Coverage:** 98.7552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defined_in_class` **(I/O & Config Routines)** (Impact: 13.2)
  * `undefined_in_gen_exp_nested` **(I/O & Config Routines)** (Impact: 9.7)
  * `f401_preview_refined_submodule_handling` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `defined_in_gen_exp` **(Annotated & Test Methods)** (Impact: 7.4)
  * `f401_preview_local_init_import` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* // Regression test for https://github.com/astral-sh/ruff/issues/12897
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 120`, `args: 246`, `func_start: 244`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 144`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 243`, `concurrency: 4`, `import: 21`
* *Defense:* `doc: 6`, `test: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Rule, anyhow::Result, assert_diagnostics, assert_diagnostics_diff, crate::Locator, crate::linter::check_path, crate::registry::Linter, crate::rules::isort...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1028.44 | **LOC:** 1955 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 95.122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format_line` **(Many-Argument Workhorses)** (Impact: 294.1)
    * *Intent:* // Adapted from https://github.com/rust-lang/rust/blob/d371d17496f2ce3a56da76aa083f4ef157572c20/comp...
  * `format_body` **(Many-Argument Workhorses)** (Impact: 126.6)
  * `format_annotation` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `format_header` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `format_raw_line` **(Many-Argument Workhorses)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 54 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 254`, `args: 84`, `func_start: 38`, `class_start: 18`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 92`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 38`, `import: 10`
* *Defense:* `safety: 48`, `doc: 77`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Margin, Style, crate::Id, crate::renderer::DEFAULT_TERM_WIDTH, crate::renderer::styled_buffer::StyledBuffer, fmt, max, min...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_semantic/src/model.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 978.96 | **LOC:** 2856 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 5.6537% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulate_runtime_load_at_location_in_scope` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /// analysis, however for speculative lookups this is not the case, /// since we're aiming to change...
  * `resolve_load` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* /// Resolve a `load` reference to an [`ast::ExprName`].
  * `resolve_qualified_name` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* /// Resolves the [`Expr`] to a fully-qualified symbol-name, if `value` resolves to an imported /// o...
  * `resolve_qualified_import_name` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /// Given a `module` and `member`, return the fully-qualified name of the binding in the current ///...
  * `lookup_symbol_in_scope` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /// Lookup a symbol in a certain scope /// /// This is a carbon copy of [`Self::resolve_load`], but ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 238`, `args: 192`, `func_start: 144`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 97`, `dead_code: 11`, `planned_debt: 9`, `unreferenced_by_name: 85`
* *Architecture:* `api: 157`, `import: 17`
* *Defense:* `safety: 21`, `doc: 809`, `test: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingFlags, BindingId, BindingKind, Bindings, Branches, DefinitionId, Definitions, Exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_formatter/src/printer/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 894.28 | **LOC:** 2097 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%), Connectivity (formerly Api Exposure) (55.6%)
- **Documentation Coverage:** 68.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_element` **(Many-Argument Workhorses)** (Impact: 120.1)
    * *Intent:* /// Prints a single element and push the following elements to queue
  * `fits_element` **(Many-Argument Workhorses)** (Impact: 76.9)
    * *Intent:* /// Tests if the passed element fits on the current line or not.
  * `print_fill_entries` **(Many-Argument Workhorses)** (Impact: 74.0)
    * *Intent:* /// the *item*s if the *item* or the *item* and the expanded *separator* don't fit on the line. /// ...
  * `fits_text` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `print_best_fitting` **(Many-Argument Workhorses)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 269`, `args: 55`, `func_start: 63`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 105`
* *Architecture:* `api: 24`, `import: 21`
* *Defense:* `safety: 25`, `doc: 97`, `test: 35`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BestFittingVariants, FitsCallStack, FitsEndPredicate, FitsQueue, FormatElement, FormatState, GroupId, GroupMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 874.78 | **LOC:** 4115 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (67.2%), Guard Balance (formerly Safety Score) (56.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 6.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_parameters` **(Many-Argument Workhorses)** (Impact: 69.0)
    * *Intent:* /// Parses a parameter list for the given function kind. /// /// See: <https://docs.python.org/3/ref...
  * `parse_type_param` **(Compute Cores)** (Impact: 40.3)
    * *Intent:* /// Parses a type parameter. /// /// See: <https://docs.python.org/3/reference/compound_stmts.html#g...
  * `parse_from_import_statement` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* /// Parses a `from` import statement. /// /// # Panics /// /// If the parser isn't positioned at a `...
  * `parse_simple_statement` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* /// Parses a simple statement. /// /// See: <https://docs.python.org/3/reference/simple_stmts.html>
  * `try_parse_parenthesized_with_items` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* /// first with item. The challenge here is that until the parser sees the matching `)` token, /// it...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 362`, `args: 95`, `func_start: 68`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 3`, `state_mutation: 43`, `dead_code: 152`, `planned_debt: 5`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 12`, `doc: 463`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicNodeIndex, ExceptHandler, Expr, ExprContext, IpyEscapeKind, Operator, ParseErrorType, ParsedExpr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff/tests/cli/lint.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 857.06 | **LOC:** 4440 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (14.0%), Complexity Load (formerly Cognitive Load) (6.4%)
- **Documentation Coverage:** 64.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `output_format` **(Compute Cores)** (Impact: 130.6)
  * `create_a005_module_structure` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* /// │ └── __init__.py /// ├── foobar /// │ ├── __init__.py /// │ ├── abc /// │ │ └── __init__.py ///...
  * `value_given_to_table_key_is_not_inline_table_1` **(I/O & Config Routines)** (Impact: 12.8)
  * `exclude` **(I/O & Config Routines)** (Impact: 11.4)
  * `match_before_py310` **(I/O & Config Routines)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 217`, `args: 93`, `func_start: 106`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 29`, `state_mutation: 55`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 95`
* *Architecture:* `io: 1`, `concurrency: 10`, `import: 12`
* *Defense:* `doc: 128`, `test: 102`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` anyhow::Result, crate::CliTest, get_cargo_bin, insta_cmd::assert_cmd_snapshot, std::fs, std::process::Command, std::str
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_workspace/src/configuration.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 846.28 | **LOC:** 2245 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **123**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.1%), Guard Balance (formerly Safety Score) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (23.9%)
- **Documentation Coverage:** 82.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as_rule_table` **(Many-Argument Workhorses)** (Impact: 116.8)
  * `warn_about_deprecated_top_level_lint_options` **(Many-Argument Workhorses)** (Impact: 95.8)
  * `into_settings` **(Defensive Guards)** (Impact: 76.2)
  * `from_options` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /// Convert the [`Options`] read from the given [`Path`] into a [`Configuration`]. /// If `None` is ...
  * `conflicting_import_settings` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /// Detect conflicts between I002 (missing-required-import) and ICN001 (unconventional-import-alias)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 226`, `args: 108`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 81`, `planned_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `api: 111`, `import: 43`
* *Defense:* `safety: 98`, `doc: 18`, `test: 36`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CompiledPerFileTargetVersionList, DUMMY_VARIABLE_RGX, Direction, DocstringCodeLineWidth, ExtensionMapping, FilePattern, FilePatternSet, FileResolverSettings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_workspace/src/options.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 835.06 | **LOC:** 4435 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **81**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (86.2%), Mutation Surface (formerly State Flux) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_into_settings` **(Defensive Guards)** (Impact: 53.8)
  * `try_into_settings` **(Defensive Guards)** (Impact: 14.1)
  * `try_into_settings` **(Defensive Guards)** (Impact: 9.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 8.2)
  * `deserialize` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 38 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 230`, `args: 87`, `func_start: 47`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 221`, `dead_code: 11`, `planned_debt: 8`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 288`, `concurrency: 1`, `import: 45`
* *Defense:* `safety: 113`, `doc: 1377`, `test: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ApiBan, BTreeSet, Deserializer, Flake8TidyImportsOptions, FxHashMap, FxHashSet, ImportSelection, ImportSelector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/expression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 789.92 | **LOC:** 3096 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (32.5%)
- **Documentation Coverage:** 13.7615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_interpolated_element` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* /// Parses an f/t-string expression element. /// /// # Panics /// /// If the parser isn't positioned...
  * `handle_implicitly_concatenated_strings` **(Many-Argument Workhorses)** (Impact: 45.4)
    * *Intent:* /// Handles implicitly concatenated strings. /// /// # Panics /// /// If the length of `strings` is ...
  * `parse_binary_expression_or_higher_recursive` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `parse_lhs_expression` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* /// Parses the left-hand side of an expression. /// /// This includes prefix expressions such as una...
  * `parse_arguments` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* /// Parses an argument list. /// /// # Panics /// /// If the parser isn't positioned at a `(` token....
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 332`, `args: 92`, `func_start: 78`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 13`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 38`, `import: 15`
* *Defense:* `safety: 11`, `doc: 361`, `test: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyStringFlags, AtomicNodeIndex, BoolOp, CmpOp, ConversionFlag, Expr, ExprContext, FString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 769.3 | **LOC:** 2953 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.6%), Guard Balance (formerly Safety Score) (75.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 61.3861% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_name_impl` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `from_settings` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /// Validate and normalize the raw settings given by the user /// into settings we can use for modul...
  * `check_pkgutil_extend_path` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* /// Check for `__path__ = pkgutil.extend_path(__path__, __name__)` or /// `__path__ = __import__("pk...
  * `absolute_desperate_search_paths` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* /// Get the search-paths for desperate resolution of absolute imports in this file. /// /// Currentl...
  * `dynamic_resolution_paths` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* /// Collect all dynamic search paths. For each `site-packages` path: /// - Collect that `site-packag...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 456`, `args: 124`, `func_start: 81`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 176`, `high_risk_execution: 2`, `state_mutation: 35`, `dead_code: 7`, `planned_debt: 21`, `fragile_debt: 2`, `unreferenced_by_name: 37`
* *Architecture:* `io: 16`, `api: 31`, `import: 30`
* *Defense:* `safety: 17`, `doc: 237`, `test: 146`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DbWithWritableSystem, FilePath, FileRootKind, FxHashSet, MockedTypeshed, ModuleKind, PySourceType, PythonVersion...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/noqa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 764.16 | **LOC:** 3024 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.7%), Guard Balance (formerly Safety Score) (49.1%)
- **Documentation Coverage:** 83.105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_noqa_comments` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `extract` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* /// Extract the [`FileNoqaDirectives`] for a given Python source file, enumerating any rules /// tha...
  * `lex_file_exemption` **(Compute Cores)** (Impact: 22.7)
  * `lex_code` **(Compute Cores)** (Impact: 18.4)
  * `build_noqa_edits_by_line` **(Many-Argument Workhorses)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 365`, `args: 145`, `func_start: 128`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 36`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 110`, `import: 33`
* *Defense:* `safety: 17`, `doc: 74`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cursor, LexicalError, LineRanges, NoqaLexerOutput, NoqaMapping, SecondaryCode, SourceFileBuilder, TextLen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_codegen/src/generator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 763.8 | **LOC:** 2153 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (47.6%), Guard Balance (formerly Safety Score) (46.6%)
- **Documentation Coverage:** 86.9565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unparse_stmt` **(Many-Argument Workhorses)** (Impact: 130.3)
  * `unparse_expr` **(Many-Argument Workhorses)** (Impact: 110.7)
  * `unparse` **(I/O & Config Routines)** (Impact: 39.1)
  * `quote` **(Annotated & Test Methods)** (Impact: 25.0)
  * `unparse_pattern` **(Many-Argument Workhorses)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 270`, `args: 56`, `func_start: 56`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 18`, `unreferenced_by_name: 11`
* *Architecture:* `api: 57`, `concurrency: 19`, `import: 13`
* *Defense:* `safety: 47`, `doc: 22`, `test: 37`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alias, AnyStringFlags, ArgOrKeyword, BoolOp, BytesLiteralFlags, CmpOp, Comprehension, ConversionFlag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 720.96 | **LOC:** 1928 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **54**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%)
- **Documentation Coverage:** 33.0357% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `any_over_stmt` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `from_expr` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* /// Return the truthiness of an expression.
  * `any_over_expr` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* /// Call `func` over every `Expr` in `expr`, returning `true` if any expression /// returns `true`..
  * `is_unpacking_assignment` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* /// Check if a node represents an unpacking assignment.
  * `contains_effect` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* /// Return `true` if the `Expr` contains an expression that appears to include a /// side-effect (li...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 135`, `args: 214`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `state_mutation: 30`, `dead_code: 5`
* *Architecture:* `api: 62`, `import: 19`
* *Defense:* `safety: 35`, `doc: 154`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arguments, AtomicNodeIndex, CmpOp, DictItem, ExceptHandler, Expr, ExprContext, ExprName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_ast/generate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 700.22 | **LOC:** 1106 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.7317% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 34.6)
  * `write_source_order` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* # ------------------------------------------------------------------------------ # Source order visi...
  * `write_node` **(Compute Cores)** (Impact: 27.9)
    * *Intent:* # ------------------------------------------------------------------------------ # Node structs
  * `fields_in_source_order` **(Type Conversions)** (Impact: 10.7)
  * `write_owned_enum` **(Many-Argument Workhorses)** (Impact: 10.6)
    * *Intent:* # ------------------------------------------------------------------------------ # Owned enum """ Cr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 485
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 62`, `args: 24`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 185`
* *Architecture:* `io: 2`, `api: 24`, `import: 7`
* *Defense:* `doc: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, dataclasses, pathlib, re, subprocess, tomllib, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 632.62 | **LOC:** 3123 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **47**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (55.8%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 35.5932% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replace_unprintable` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /// Given some source code and annotation ranges, this routine replaces /// unprintable characters w...
  * `to_renderable` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /// Create a diagnostic amenable for rendering. /// /// `context` refers to the number of lines both...
  * `fmt` **(Compute Cores)** (Impact: 23.0)
  * `context_after` **(Many-Argument Workhorses)** (Impact: 19.3)
    * *Intent:* /// Returns the line number accounting for the given `len` /// number of following context lines. //...
  * `context_before` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* /// Returns the line number accounting for the given `len` /// number of preceding context lines. //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 333`, `args: 263`, `func_start: 94`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 45`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 26`
* *Architecture:* `api: 36`, `import: 20`
* *Defense:* `safety: 20`, `doc: 334`, `test: 22`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Diagnostic, DiagnosticFormat, DiagnosticId, DiagnosticSource, DisplayDiagnosticConfig, Edit, Fix, IntoDiagnosticMessage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 612.12 | **LOC:** 2458 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (32.2%), Dead Code Surface (formerly Dead Code) (18.1%)
- **Documentation Coverage:** 2.3256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_enclosed_comment` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* /// Handle a comment that is enclosed by a node.
  * `handle_comprehension_comment` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /// ```python /// [ /// a /// for # dangling on the comprehension /// b /// # dangling on the compre...
  * `handle_lambda_comment` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* /// ``` /// /// For non-parameterized lambdas, all comments before the body are considered dangling,...
  * `handle_trailing_binary_expression_left_or_operator_comment` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* /// Handles comments between the left side and the operator of a binary expression (trailing comment...
  * `handle_own_line_comment_after_branch` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /// Determine where to attach an own line comment after a branch depending on its indentation
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 195`, `args: 92`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 30`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 25`, `doc: 552`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyNodeRef, CommentRanges, Comprehension, DecoratedComment, Expr, ModModule, Parameter, Parameters...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_parser/src/semantic_errors.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 597.06 | **LOC:** 2381 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (44.9%), Guard Balance (formerly Safety Score) (41.0%)
- **Documentation Coverage:** 44.6429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_stmt` **(Many-Argument Workhorses)** (Impact: 77.8)
  * `visit_pattern` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `check_annotation` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `visit_expr` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /// Check `expr` for semantic syntax errors and update the checker's internal state.
  * `fmt` **(Many-Argument Workhorses)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 152`, `args: 34`, `func_start: 52`, `class_start: 16`
* *Risk/State:* `state_mutation: 28`, `dead_code: 36`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`, `concurrency: 9`, `import: 7`
* *Defense:* `safety: 28`, `doc: 485`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Expr, ExprContext, FxHashSet, IrrefutablePatternKind, Pattern, PythonVersion, Stmt, StmtExpr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/string/docstring.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 567.24 | **LOC:** 1903 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 1.138; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 40.7407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* /// code requires adjusting which part of each line is used for the actual /// code bit. /// /// Thi...
  * `format` **(Many-Argument Workhorses)** (Impact: 41.5)
    * *Intent:* /// ``` /// Here line a is 3 columns negatively indented, so we pad all lines by an extra 3 spaces: ...
  * `print_one` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* /// Prints the single line given. /// /// This mostly just handles indentation and ensuring line bre...
  * `run_action_queue` **(Compute Cores)** (Impact: 33.0)
    * *Intent:* /// Process any actions in this printer's queue until the queue is empty.
  * `trim_start` **(Compute Cores)** (Impact: 32.6)
    * *Intent:* /// Trims the indent of `rhs` by `self`. /// /// Returns `None` if `self` is not a prefix of `rhs` o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 255`, `args: 81`, `func_start: 50`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`, `dead_code: 5`
* *Architecture:* `api: 5`, `import: 14`
* *Defense:* `safety: 19`, `doc: 523`, `test: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001192
  * `Imports (Out-Degree: 0):` FormatModuleError, IndentStyle, LineWidth, Printed, StringFlags, TextLen, TextRange, TextSize...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff/src/commands/format.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 557.36 | **LOC:** 1426 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **91**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (35.2%)
- **Documentation Coverage:** 32.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Many-Argument Workhorses)** (Impact: 99.2)
    * *Intent:* /// Format a set of files, and return the exit status.
  * `format_source` **(Many-Argument Workhorses)** (Impact: 61.8)
    * *Intent:* /// Format a [`SourceKind`], returning the transformed [`SourceKind`], or `None` if the source was /...
  * `warn_incompatible_formatter_settings` **(Compute Cores)** (Impact: 56.6)
  * `format_path` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* /// Format the file at the given [`Path`].
  * `fmt` **(Many-Argument Workhorses)** (Impact: 46.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 238`, `args: 46`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 21`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 5`, `api: 10`, `import: 52`
* *Defense:* `safety: 28`, `doc: 33`, `test: 5`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Diagnostic, DiagnosticId, DisplayDiagnosticConfig, FileCacheKey, Fix, FormatArguments, FormatMode, FormatRange...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 554.6 | **LOC:** 1950 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **51**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.7%), Connectivity (formerly Api Exposure) (6.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expression` **(Many-Argument Workhorses)** (Impact: 515.5)
    * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 24`, `args: 11`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Arguments, CFormatErrorType, Expr, ExprContext, Operator, crate::checkers::ast::Checker, crate::preview::
    is_future_required_preview_generics_enabled, crate::registry::Rule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_python_formatter/src/string/normalize.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 553.86 | **LOC:** 1155 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.388; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 46.9388% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_string` **(Many-Argument Workhorses)** (Impact: 63.3)
  * `preferred_quote_style` **(Many-Argument Workhorses)** (Impact: 47.2)
    * *Intent:* /// Determines the preferred quote style for `string`. /// The formatter should use the preferred qu...
  * `normalize` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* /// Normalises `\u..`, `\U..`, `\x..` and `\N{..}` escape sequences to: /// /// * `\u`, `\U'` and `\...
  * `raw` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* /// Computes if a raw string uses the preferred quote. If it does, then it's not possible /// to cha...
  * `triple_quoted` **(Many-Argument Workhorses)** (Impact: 25.3)
    * *Intent:* /// For triple quoted strings, the preferred quote style can't be used if the string contains /// a ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 145`, `args: 45`, `func_start: 35`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `dead_code: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 17`, `doc: 87`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ByteStringPrefix, BytesLiteral, FString, InterpolatedStringElement, InterpolatedStringElements, StringFlags, StringLikePart, StringLiteral...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 541.7 | **LOC:** 1668 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.388; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Complexity Load (formerly Cognitive Load) (12.9%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `statement` **(Many-Argument Workhorses)** (Impact: 492.6)
    * *Intent:* /// Run lint rules over a [`Stmt`] syntax node.
  * `bad_version_info_comparison` **(Many-Argument Workhorses)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 43`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 28`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Expr, Stmt, crate::checkers::ast::Checker, crate::preview::is_standalone_mock_non_existent_enabled, crate::registry::Rule, crate::rules::
    airflow, fastapi, flake8_async...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 21.243** (Embedded: 0.3678 * Error Risk: 57.7628%)
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` -> **Severity: 0.226** (Embedded: 0.0063 * Error Risk: 36.1758%)
- `ruff-0.15.9/crates/ruff_macros/src/newtype_index.rs` -> **Severity: 0.217** (Embedded: 0.0042 * Error Risk: 51.9191%)
- `ruff-0.15.9/crates/ruff_python_formatter/src/statement/clause.rs` -> **Severity: 0.2** (Embedded: 0.0047 * Error Risk: 42.5238%)
- `ruff-0.15.9/crates/ruff_db/src/system/os.rs` -> **Severity: 0.181** (Embedded: 0.0032 * Error Risk: 56.6959%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 23123.8** (Blast Radius: 231.238 * Doc Risk: 100.0%)
- `ruff-0.15.9/crates/ruff_db/src/diagnostic/render/pylint.rs` -> **Severity: 396.5** (Blast Radius: 3.965 * Doc Risk: 100.0%)
- `ruff-0.15.9/crates/ruff_macros/src/newtype_index.rs` -> **Severity: 302.9** (Blast Radius: 3.029 * Doc Risk: 100.0%)
- `ruff-0.15.9/crates/ruff_db/src/system/os.rs` -> **Severity: 219.738** (Blast Radius: 2.484 * Doc Risk: 88.4615%)
- `ruff-0.15.9/crates/ruff_linter/src/settings/flags.rs` -> **Severity: 137.9** (Blast Radius: 1.379 * Doc Risk: 100.0%)

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
