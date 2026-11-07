# ARCHITECTURAL_BRIEF: ruff
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 2414 analyzed artifact(s), 281340 LOC.
- **Load-bearing artifact:** `ruff-0.15.9/crates/ruff_python_ast/src/lib.rs` -- 840 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/mod.rs` -- pulls in 220 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` at magnitude 1395.68 (structural weight, not risk).
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
| Total Artifacts | 4049 |
| Analyzed Artifacts (Scanned) | 2414 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1635 |
| Total LOC | 281340 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 59.6% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4094 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2659 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 53.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.5608 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1478 | 258823 | 61.2% |
| PYTHON | 833 | 21857 | 34.5% |
| JSON | 64 | 644 | 2.7% |
| XML | 23 | 16 | 1.0% |
| MARKDOWN | 13 | 0 | 0.5% |
| PLAINTEXT | 3 | 0 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 2414 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 25%, State Mutators Files 19%, Declarative / Non-Code 15%, Large Core Modules (3) 11%, Generic / Templated Code Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2391 | 99.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 0.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1635*

**Composition by Extension & Reason:**
- `.snap`: 1163x Excluded (Unsupported Extension: '.snap')
- `.expect`: 208x Excluded (Unsupported Extension: '.expect')
- `.py`: 108x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.toml`: 57x Excluded (Unsupported Extension: '.toml')
- `.json`: 54x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ipynb`: 23x Excluded (Unsupported Extension: '.ipynb')
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rs`: 2x Unrecognized Syntax (Dense Structure / Global Regex Timeout), 1x Excluded (Machine-Generated Source Code Signature: 1596 LOC), 1x Excluded (Machine-Generated Source Code Signature: 10878 LOC)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.dot`: 1x Excluded (Unsupported Extension: '.dot')
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 469 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.1 | 4.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.3 | 24.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.2 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.7 | 14.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 53.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.9 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.1 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 714 | 214 | 0 | `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` |
| cleanup | 25 | 10 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/statement/delete.py` |
| guards | 9595 | 1406 | 9 | `ruff-0.15.9/crates/ruff_python_codegen/src/generator.rs` |
| danger | 3959 | 587 | 3 | `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` |
| concurrency | 901 | 233 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/remove_await_parens.py` |
| connectivity | 13734 | 1734 | 13 | `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` |
| io | 279 | 88 | 0 | `ruff-0.15.9/crates/ruff_db/src/system/memory_fs.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 12 | 0 | `ruff-0.15.9/python/ruff/__main__.py` |
| time | 18 | 11 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/conditional_expression.py` |
| serialization | 24 | 7 | 0 | `ruff-0.15.9/crates/ruff_workspace/src/pyproject.rs` |
| regex | 57 | 38 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/pattern_matching_generic.py` |
| events | 230 | 59 | 0 | `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` |
| tests | 3889 | 305 | 1 | `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` |
| docs | 60141 | 1351 | 53 | `ruff-0.15.9/crates/ruff_formatter/src/builders.rs` |
| debt | 1630 | 337 | 1 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/preview_long_strings__regression.py` |
| mutation | 27011 | 1531 | 26 | `ruff-0.15.9/crates/ruff_workspace/src/options.rs` |
| dead_code | 2021 | 357 | 1 | `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` |
| credential | 1 | 1 | 0 | `ruff-0.15.9/crates/ruff_linter/src/rules/refurb/rules/hardcoded_string_charset.rs` |
| threat | 7 | 4 | 0 | `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/bidirectional_unicode.rs` |
| ml_ai | 86 | 44 | 0 | `ruff-0.15.9/crates/ruff_server/resources/test/fixtures/pandas_html.py` |
| ui | 3 | 3 | 0 | `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/pep604_union_types_line_breaks.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ruff-0.15.9/crates/ruff_db/src/system/memory_fs.rs` (Hits: 20)
- `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (Hits: 16)
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/remove_with_brackets.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`ruff-0.15.9/crates/ruff_python_ast/src/lib.rs`) — 840 inbound connections
2. **lib.rs** (`ruff-0.15.9/crates/ruff_macros/src/lib.rs`) — 755 inbound connections
3. **traits.rs** (`ruff-0.15.9/crates/ruff_text_size/src/traits.rs`) — 735 inbound connections
4. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`) — 725 inbound connections
5. **violation.rs** (`ruff-0.15.9/crates/ruff_linter/src/violation.rs`) — 722 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/mod.rs`) — 220 outbound dependencies
2. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/mod.rs`) — 147 outbound dependencies
3. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs`) — 135 outbound dependencies
4. **configuration.rs** (`ruff-0.15.9/crates/ruff_workspace/src/configuration.rs`) — 119 outbound dependencies
5. **mod.rs** (`ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/mod.rs`) — 99 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `expression` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs`) -> Impact: **969.2** | LOC: 1925
  * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
- `statement` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs`) -> Impact: **768.3** | LOC: 1649
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
- `check_line` **(Many-Argument Workhorses)** (@ `ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/blank_lines.rs`) -> Impact: **164.6** | LOC: 250

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ruff-0.15.9/crates/ruff_python_ast/src` | 26 | 4401.24 | 7.16% | 16.46% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules` | 75 | 4363.28 | 5.81% | 3.44% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules` | 111 | 4274.02 | 5.12% | 3.07% |
| `ruff-0.15.9/crates/ruff_linter/src` | 24 | 3310.2 | 6.34% | 15.84% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules` | 43 | 3098.38 | 6.98% | 1.83% |
| `ruff-0.15.9/crates/ty_module_resolver/src` | 12 | 2388.9 | 5.24% | 12.58% |
| `ruff-0.15.9/crates/ruff_workspace/src` | 6 | 2376.98 | 7.79% | 11.76% |
| `ruff-0.15.9/crates/ruff_python_parser/src/parser` | 9 | 2351.2 | 4.38% | 8.52% |
| `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze` | 19 | 2295.74 | 8.42% | 0.47% |
| `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules` | 43 | 2228.98 | 5.27% | 20.34% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_fixme/rules/todos.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/violation.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/src/str_prefix.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/invalid_annotation_function.py` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_parser/resources/invalid/re_lex_logical_token.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ruff-0.15.9/crates/ruff_linter/src/rules/isort/format.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_linter/src/settings/rule_table.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_formatter/src/expression/expr_number_literal.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_trivia/src/comment_ranges.rs` -> **100.0%** Exposure
- `ruff-0.15.9/crates/ruff_python_ast/generate.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` -> **238** Orphaned Functions | **0** Duplicates
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/docstring_code_examples.py` -> **85** Orphaned Functions | **6** Duplicates
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/newlines.py` -> **21** Orphaned Functions | **41** Duplicates
- `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` -> **0** Orphaned Functions | **61** Duplicates
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/statement/function.py` -> **48** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18671` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.517)
- **Top Global Matches:** file_cluster_0: 8.517, file_cluster_16: 8.689, file_cluster_4: 9.299
- **Magnitude:** 1395.68 | **LOC:** 3764 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **725** in-repo importer(s); it depends on **135**; blast radius 7.948; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.0%), Guard Balance (formerly Safety Score) (51.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 29.5082% of unit weight undocumented
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
* *Structure:* `branch: 382`, `structural_boundaries: 396`, `args: 181`, `func_start: 124`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 126`, `dead_code: 2`, `planned_debt: 11`, `unreferenced_by_name: 40`
* *Architecture:* `api: 67`, `concurrency: 1`, `import: 44`
* *Defense:* `safety: 71`, `doc: 391`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.948
  * `Choke Point (Betweenness):` 0.123933 | `Ripple Effect (Closeness):` 0.186552
  * `Imports (Out-Degree: 66):` analyze, annotation, deferred, crate::Edit, crate::Locator, crate::Violation, crate::checkers::ast::annotation::AnnotationContext, crate::docstrings...
  * `Imported By (In-Degree: 725):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_ast/src/nodes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.668)
- **Top Global Matches:** file_cluster_0: 7.668, file_cluster_13: 10.484, file_cluster_15: 10.501
- **Magnitude:** 1171.54 | **LOC:** 3855 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **312** in-repo importer(s); it depends on **46**; blast radius 16.447; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Connectivity (formerly Api Exposure) (86.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Structure:* `branch: 248`, `structural_boundaries: 445`, `args: 339`, `func_start: 301`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 9`, `planned_debt: 3`, `duplicate_logic: 61`
* *Architecture:* `api: 336`, `import: 15`
* *Defense:* `safety: 22`, `doc: 657`, `test: 50`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.447
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.264163
  * `Imports (Out-Degree: 11):` bitflags::bitflags, crate::AtomicNodeIndex, crate::Expr, crate::ExprRef, crate::InterpolatedStringElement, crate::LiteralExpressionRef, crate::Mod, crate::OperatorPrecedence...
  * `Imported By (In-Degree: 312):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_annotate_snippets/src/renderer/display_list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.303)
- **Top Global Matches:** file_cluster_4: 7.303, file_cluster_0: 10.894, file_cluster_16: 11.853
- **Magnitude:** 1029.44 | **LOC:** 1955 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.232; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 92`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 39`, `import: 10`
* *Defense:* `safety: 48`, `doc: 77`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.082119
  * `Imports (Out-Degree: 5):` crate::Id, crate::renderer::DEFAULT_TERM_WIDTH, crate::renderer::Margin, crate::renderer::Style, crate::renderer::styled_buffer::StyledBuffer, crate::renderer::stylesheet::Stylesheet, crate::snippet, std::borrow::Cow...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/expression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.438)
- **Top Global Matches:** file_cluster_1: 5.438, file_cluster_3: 48.24, file_cluster_8: 70.087
- **Magnitude:** 1008.3 | **LOC:** 1950 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **51**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.7%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expression` **(Many-Argument Workhorses)** (Impact: 969.2)
    * *Intent:* /// Run lint rules over an [`Expr`] syntax node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 24`, `args: 11`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.009304 | `Ripple Effect (Closeness):` 0.10839
  * `Imports (Out-Degree: 46):` crate::checkers::ast::Checker, crate::preview::is_future_required_preview_generics_enabled, crate::preview::is_up006_future_annotations_fix_enabled, crate::registry::Rule, crate::rules::airflow, crate::rules::flake8_2020, crate::rules::flake8_async, crate::rules::flake8_bandit...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_semantic/src/model.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_0: 7.336, file_cluster_15: 8.721, file_cluster_12: 9.237
- **Magnitude:** 978.96 | **LOC:** 2856 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **213** in-repo importer(s); it depends on **50**; blast radius 3.258; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.4%), Mutation Surface (formerly State Flux) (63.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 97`, `planned_debt: 9`
* *Architecture:* `api: 157`, `import: 17`
* *Defense:* `safety: 21`, `doc: 809`, `test: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.258
  * `Choke Point (Betweenness):` 0.00599 | `Ripple Effect (Closeness):` 0.172652
  * `Imports (Out-Degree: 17):` all, bitflags::bitflags, crate::Imported, crate::analyze::visibility, crate::binding::Binding, crate::binding::BindingFlags, crate::binding::BindingId, crate::binding::BindingKind...
  * `Imported By (In-Degree: 213):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_formatter/src/printer/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.06)
- **Top Global Matches:** file_cluster_4: 8.06, file_cluster_0: 9.221, file_cluster_12: 9.259
- **Magnitude:** 875.28 | **LOC:** 2097 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **60**; blast radius 0.41; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 105`, `unreferenced_by_name: 19`
* *Architecture:* `api: 5`, `import: 21`
* *Defense:* `safety: 25`, `doc: 97`, `test: 35`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.41
  * `Choke Point (Betweenness):` 0.001028 | `Ripple Effect (Closeness):` 0.088326
  * `Imports (Out-Degree: 18):` call_stack, line_suffixes, printer_options, queue, stack, Tag::*, crate::ActualStart, crate::Document...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ty_site_packages/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.092)
- **Top Global Matches:** file_cluster_5: 7.092, file_cluster_12: 7.601, file_cluster_7: 9.769
- **Magnitude:** 869.22 | **LOC:** 3338 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 0.142; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (68.4%), Guard Balance (formerly Safety Score) (52.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 55.2239% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `site_packages_directories_from_sys_prefix` **(Many-Argument Workhorses)** (Impact: 44.9)
    * *Intent:* /// Attempt to retrieve the `site-packages` directories /// associated with a given Python installat...
  * `real_stdlib_directory_from_sys_prefix` **(Many-Argument Workhorses)** (Impact: 39.9)
    * *Intent:* /// Attempt to retrieve the real stdlib directory /// associated with a given Python installation. /...
  * `display_error` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `new` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `discover_package_dirs` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* /// Discover package directories under `prefix_dir` when the Python version is unknown. /// /// Scan...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 476`, `args: 182`, `func_start: 113`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 4`, `state_mutation: 24`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 49`
* *Architecture:* `io: 1`, `api: 33`, `import: 18`
* *Defense:* `safety: 21`, `doc: 261`, `test: 105`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.001414
  * `Imports (Out-Degree: 13):` version, camino::Utf8Component, indexmap::IndexSet, ruff_annotate_snippets::Level, ruff_annotate_snippets::Renderer, ruff_annotate_snippets::Snippet, ruff_db::system::System, ruff_db::system::SystemPath...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/statement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.64)
- **Top Global Matches:** file_cluster_4: 5.64, file_cluster_12: 8.735, file_cluster_15: 9.701
- **Magnitude:** 865.08 | **LOC:** 4115 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.132; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (40.8%)
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
* *Structure:* `branch: 267`, `structural_boundaries: 362`, `args: 95`, `func_start: 68`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 3`, `state_mutation: 43`, `dead_code: 9`, `planned_debt: 5`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 12`, `doc: 463`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.132
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.11992
  * `Imports (Out-Degree: 17):` compact_str::CompactString, crate::Mode, crate::ParseErrorType, crate::UnsupportedSyntaxErrorKind, crate::error::StarTupleKind, crate::parser::FunctionKind, crate::parser::Parser, crate::parser::RecoveryContext...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_workspace/src/configuration.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.911)
- **Top Global Matches:** file_cluster_4: 7.911, file_cluster_0: 11.701, file_cluster_6: 11.957
- **Magnitude:** 861.28 | **LOC:** 2245 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **119**; blast radius 0.249; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.1%), Connectivity (formerly Api Exposure) (70.9%), Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 86.8852% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 81`, `planned_debt: 1`
* *Architecture:* `api: 126`, `import: 43`
* *Defense:* `safety: 98`, `doc: 18`, `test: 36`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.000445 | `Ripple Effect (Closeness):` 0.062443
  * `Imports (Out-Degree: 24):` anyhow::Context, anyhow::Result, anyhow::anyhow, crate::configuration::LintConfiguration, crate::configuration::RuleSelection, crate::options::AnalyzeOptions, crate::options::Flake8AnnotationsOptions, crate::options::Flake8BanditOptions...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff/tests/cli/lint.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.227)
- **Top Global Matches:** file_cluster_13: 8.227, file_cluster_15: 8.303, file_cluster_2: 8.553
- **Magnitude:** 848.36 | **LOC:** 4440 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.512; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (66.3%), Guard Balance (formerly Safety Score) (53.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (14.0%)
- **Documentation Coverage:** 64.2487% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `output_format` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `create_a005_module_structure` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* /// │ └── __init__.py /// ├── foobar /// │ ├── __init__.py /// │ ├── abc /// │ │ └── __init__.py ///...
  * `exclude` **(I/O & Config Routines)** (Impact: 10.4)
  * `requires_python_extend_from_shared_config` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* /// ``` /// tmp /// ├── pyproject.toml <-- requires >=3.10 /// ├── ruff.toml <--- extends base /// ├...
  * `cookiecutter_globbing` **(I/O & Config Routines)** (Impact: 7.6)
    * *Intent:* /// Regression test for <https://github.com/astral-sh/ruff/issues/9381> with very helpful /// reprod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 217`, `args: 93`, `func_start: 106`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 29`, `state_mutation: 55`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 95`, `concurrency: 10`, `import: 12`
* *Defense:* `doc: 128`, `test: 102`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.512
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001151
  * `Imports (Out-Degree: 1):` anyhow::Result, crate::CliTest, insta_cmd::assert_cmd_snapshot, insta_cmd::get_cargo_bin, std::fs, std::process::Command, std::str
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/analyze/statement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.133)
- **Top Global Matches:** file_cluster_3: 6.133, file_cluster_8: 20.452, file_cluster_6: 33.413
- **Magnitude:** 817.4 | **LOC:** 1668 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **42**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (12.9%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `statement` **(Many-Argument Workhorses)** (Impact: 768.3)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.006468 | `Ripple Effect (Closeness):` 0.10839
  * `Imports (Out-Degree: 40):` crate::checkers::ast::Checker, crate::preview::is_standalone_mock_non_existent_enabled, crate::registry::Rule, crate::rules::airflow, crate::rules::fastapi, crate::rules::flake8_async, crate::rules::flake8_bandit, crate::rules::flake8_boolean_trap...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_ast/generate.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.453)
- **Top Global Matches:** file_cluster_4: 8.453, file_cluster_5: 11.432, file_cluster_6: 11.824
- **Magnitude:** 804.52 | **LOC:** 1106 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.7317% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_owned_enum` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* # ------------------------------------------------------------------------------ # Owned enum """ Cr...
  * `__init__` **(Compute Cores)** (Impact: 34.6)
  * `write_anynoderef` **(Many-Argument Workhorses)** (Impact: 32.6)
    * *Intent:* # ------------------------------------------------------------------------------ # AnyNodeRef """ Cr...
  * `write_source_order` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* # ------------------------------------------------------------------------------ # Source order visi...
  * `write_root_anynoderef` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* # ------------------------------------------------------------------------------ # AnyRootNodeRef ""...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 62`, `args: 24`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 185`
* *Architecture:* `io: 2`, `api: 24`, `import: 7`
* *Defense:* `doc: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, dataclasses, pathlib, re, subprocess, tomllib, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruff-0.15.9/crates/ty_module_resolver/src/resolve.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.561)
- **Top Global Matches:** file_cluster_5: 7.561, file_cluster_7: 9.935, file_cluster_12: 9.993
- **Magnitude:** 794.6 | **LOC:** 2953 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **43**; blast radius 0.354; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Connectivity (formerly Api Exposure) (53.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_name_impl` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `from_settings` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /// Validate and normalize the raw settings given by the user /// into settings we can use for modul...
  * `check_pkgutil_extend_path` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* /// Check for `__path__ = pkgutil.extend_path(__path__, __name__)` or /// `__path__ = __import__("pk...
  * `absolute_desperate_search_paths` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* /// Get the search-paths for desperate resolution of absolute imports in this file. /// /// Currentl...
  * `file_to_module_impl` **(Many-Argument Workhorses)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 456`, `args: 124`, `func_start: 81`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 176`, `high_risk_execution: 2`, `state_mutation: 35`, `planned_debt: 21`, `fragile_debt: 2`
* *Architecture:* `io: 16`, `api: 65`, `import: 30`
* *Defense:* `safety: 17`, `doc: 237`, `test: 146`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.354
  * `Choke Point (Betweenness):` 0.000354 | `Ripple Effect (Closeness):` 0.003355
  * `Imports (Out-Degree: 20):` anyhow::Context, crate::SearchPathSettings, crate::SearchPathSettingsError, crate::db::Db, crate::db::tests::TestDb, crate::module::Module, crate::module::ModuleKind, crate::module_name::ModuleName...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_parser/src/parser/expression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.686)
- **Top Global Matches:** file_cluster_4: 6.686, file_cluster_12: 7.184, file_cluster_16: 7.852
- **Magnitude:** 788.52 | **LOC:** 3096 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **49**; blast radius 0.159; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (32.5%)
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
* *Structure:* `branch: 214`, `structural_boundaries: 332`, `args: 92`, `func_start: 78`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 13`, `state_mutation: 40`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 38`, `import: 15`
* *Defense:* `safety: 11`, `doc: 361`, `test: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.159
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.119962
  * `Imports (Out-Degree: 17):` bitflags::bitflags, crate::InterpolatedStringErrorType, crate::Mode, crate::ParseErrorType, crate::UnsupportedSyntaxError, crate::UnsupportedSyntaxErrorKind, crate::error::FStringKind, crate::error::StarTupleKind...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_workspace/src/options.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.692)
- **Top Global Matches:** file_cluster_0: 7.692, file_cluster_13: 9.102, file_cluster_15: 9.703
- **Magnitude:** 771.16 | **LOC:** 4435 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **79**; blast radius 0.95; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.2%), Mutation Surface (formerly State Flux) (62.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_into_settings` **(Defensive Guards)** (Impact: 51.0)
  * `try_into_settings` **(Defensive Guards)** (Impact: 12.4)
  * `try_into_settings` **(Defensive Guards)** (Impact: 9.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 8.2)
  * `deserialize` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 230`, `args: 87`, `func_start: 47`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 221`, `planned_debt: 8`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 288`, `concurrency: 1`, `import: 45`
* *Defense:* `safety: 113`, `doc: 1377`, `test: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.95
  * `Choke Point (Betweenness):` 0.038246 | `Ripple Effect (Closeness):` 0.116044
  * `Imports (Out-Degree: 44):` anyhow::Result, anyhow::anyhow, crate::options::Flake8SelfOptions, crate::options::Flake8TidyImportsOptions, crate::settings::LineEnding, regex::Regex, ruff_formatter::IndentStyle, ruff_graph::Direction...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_linter/src/noqa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.861)
- **Top Global Matches:** file_cluster_0: 7.861, file_cluster_13: 8.457, file_cluster_16: 8.544
- **Magnitude:** 764.16 | **LOC:** 3024 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **44**; blast radius 0.521; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.521
  * `Choke Point (Betweenness):` 0.001937 | `Ripple Effect (Closeness):` 0.157113
  * `Imports (Out-Degree: 21):` anyhow::Result, crate::Edit, crate::Locator, crate::Violation, crate::fs::relativize_path, crate::generate_noqa_edits, crate::noqa::Directive, crate::noqa::LexicalError...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_ast/src/helpers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.131)
- **Top Global Matches:** file_cluster_4: 8.131, file_cluster_0: 8.916, file_cluster_15: 9.476
- **Magnitude:** 716.76 | **LOC:** 1928 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **138** in-repo importer(s); it depends on **49**; blast radius 3.921; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.6%)
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
* *Structure:* `branch: 213`, `structural_boundaries: 135`, `args: 214`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `api: 62`, `import: 19`
* *Defense:* `safety: 35`, `doc: 154`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.921
  * `Choke Point (Betweenness):` 0.000488 | `Ripple Effect (Closeness):` 0.239829
  * `Imports (Out-Degree: 15):` crate, crate::AnyNodeRef, crate::Arguments, crate::AtomicNodeIndex, crate::CmpOp, crate::DictItem, crate::ExceptHandler, crate::Expr...
  * `Imported By (In-Degree: 138):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_codegen/src/generator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_4: 7.633, file_cluster_15: 7.855, file_cluster_12: 8.431
- **Magnitude:** 678.8 | **LOC:** 2153 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **47**; blast radius 0.312; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.8%), Concurrency Surface (formerly Concurrency) (47.6%)
- **Documentation Coverage:** 88.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unparse_stmt` **(Many-Argument Workhorses)** (Impact: 113.0)
  * `unparse_expr` **(Many-Argument Workhorses)** (Impact: 106.7)
  * `unparse_pattern` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `unparse_interpolated_element` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `unparse_parameters` **(Defensive Guards)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 270`, `args: 56`, `func_start: 56`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `api: 68`, `concurrency: 19`, `import: 13`
* *Defense:* `safety: 47`, `doc: 22`, `test: 37`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.312
  * `Choke Point (Betweenness):` 0.000282 | `Ripple Effect (Closeness):` 0.138468
  * `Imports (Out-Degree: 8):` crate::stylist::Indentation, ruff_python_ast, ruff_python_ast::Alias, ruff_python_ast::AnyStringFlags, ruff_python_ast::ArgOrKeyword, ruff_python_ast::BoolOp, ruff_python_ast::BytesLiteralFlags, ruff_python_ast::CmpOp...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.659)
- **Top Global Matches:** file_cluster_13: 6.659, file_cluster_2: 8.216, file_cluster_15: 8.464
- **Magnitude:** 652.3 | **LOC:** 4638 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **33**; blast radius 0.293; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Mutation Surface (formerly State Flux) (27.2%)
- **Documentation Coverage:** 98.3607% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f401_preview_local_init_import` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* // Regression test for https://github.com/astral-sh/ruff/issues/12897
  * `rules_with_flake8_type_checking_settings_enabled` **(Compute Cores)** (Impact: 4.6)
  * `preview_rules` **(Annotated & Test Methods)** (Impact: 4.5)
  * `f401_deprecated_option` **(Annotated & Test Methods)** (Impact: 4.5)
  * `f401_stable` **(Annotated & Test Methods)** (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 120`, `args: 246`, `func_start: 244`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 144`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 238`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 21`
* *Defense:* `doc: 6`, `test: 237`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.293
  * `Choke Point (Betweenness):` 0.010656 | `Ripple Effect (Closeness):` 0.166278
  * `Imports (Out-Degree: 23):` cformat, fixes, format, rules, settings, anyhow::Result, crate::Locator, crate::assert_diagnostics...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_db/src/diagnostic/render.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.853)
- **Top Global Matches:** file_cluster_0: 6.853, file_cluster_16: 8.082, file_cluster_15: 8.585
- **Magnitude:** 624.62 | **LOC:** 3123 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **57**; blast radius 2.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (37.3%)
- **Documentation Coverage:** 44.2029% of unit weight undocumented
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
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 333`, `args: 263`, `func_start: 94`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 45`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 55`, `import: 20`
* *Defense:* `safety: 20`, `doc: 334`, `test: 22`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.811
  * `Choke Point (Betweenness):` 0.004884 | `Ripple Effect (Closeness):` 0.151675
  * `Imports (Out-Degree: 26):` azure, concise, full, github, gitlab, json, json_lines, junit...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_formatter/src/comments/placement.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.45)
- **Top Global Matches:** file_cluster_4: 8.45, file_cluster_0: 9.202, file_cluster_9: 9.791
- **Magnitude:** 609.42 | **LOC:** 2458 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.143; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.8%), Mutation Surface (formerly State Flux) (15.8%)
- **Documentation Coverage:** 4.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_enclosed_comment` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* /// Handle a comment that is enclosed by a node.
  * `handle_comprehension_comment` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /// ```python /// [ /// a /// for # dangling on the comprehension /// b /// # dangling on the compre...
  * `handle_lambda_comment` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* /// ``` /// /// For non-parameterized lambdas, all comments before the body are considered dangling,...
  * `handle_own_line_comment_after_branch` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /// Determine where to attach an own line comment after a branch depending on its indentation
  * `handle_trailing_binary_expression_left_or_operator_comment` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /// Handles comments between the left side and the operator of a binary expression (trailing comment...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 195`, `args: 92`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 13`
* *Defense:* `safety: 25`, `doc: 552`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 0.000202 | `Ripple Effect (Closeness):` 0.074229
  * `Imports (Out-Degree: 16):` ast::helpers::comment_indentation_after, crate::comments::placement::max_empty_lines, crate::comments::visitor::CommentPlacement, crate::comments::visitor::DecoratedComment, crate::expression::expr_slice::ExprSliceCommentSection, crate::expression::expr_slice::assign_comment_in_slice, crate::expression::parentheses::is_expression_parenthesized, crate::other::parameters::assign_argument_separator_comment_placement...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_parser/src/semantic_errors.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.306)
- **Top Global Matches:** file_cluster_4: 7.306, file_cluster_0: 9.139, file_cluster_15: 9.62
- **Magnitude:** 585.96 | **LOC:** 2381 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **22**; blast radius 0.499; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.0%), Mutation Surface (formerly State Flux) (44.9%)
- **Documentation Coverage:** 45.614% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_stmt` **(Many-Argument Workhorses)** (Impact: 77.8)
  * `visit_pattern` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `check_annotation` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `visit_expr` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /// Check `expr` for semantic syntax errors and update the checker's internal state.
  * `debug_shadowing` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* /// Check for [`SemanticSyntaxErrorKind::WriteToDebug`] in `stmt`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 152`, `args: 34`, `func_start: 52`, `class_start: 16`
* *Risk/State:* `state_mutation: 28`, `planned_debt: 1`
* *Architecture:* `api: 19`, `concurrency: 9`, `import: 7`
* *Defense:* `safety: 28`, `doc: 485`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.196819
  * `Imports (Out-Degree: 9):` ruff_python_ast, ruff_python_ast::Expr, ruff_python_ast::ExprContext, ruff_python_ast::IrrefutablePatternKind, ruff_python_ast::Pattern, ruff_python_ast::PythonVersion, ruff_python_ast::Stmt, ruff_python_ast::StmtExpr...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_python_formatter/src/string/normalize.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.435)
- **Top Global Matches:** file_cluster_4: 6.435, file_cluster_6: 10.638, file_cluster_16: 11.636
- **Magnitude:** 549.16 | **LOC:** 1155 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **28**; blast radius 0.293; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.9434% of unit weight undocumented
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
* *Structure:* `branch: 149`, `structural_boundaries: 145`, `args: 45`, `func_start: 35`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `import: 15`
* *Defense:* `safety: 17`, `doc: 87`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.293
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.073745
  * `Imports (Out-Degree: 13):` crate::QuoteStyle, crate::context::InterpolatedStringState, crate::prelude::*, crate::string::Quote, crate::string::StringQuotes, crate::string::TripleQuotes, crate::string::normalize_string, ruff_formatter::FormatContext...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff_linter/src/suppression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.929)
- **Top Global Matches:** file_cluster_0: 7.929, file_cluster_4: 9.062, file_cluster_15: 9.415
- **Magnitude:** 531.94 | **LOC:** 1973 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **52**; blast radius 0.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (41.6%)
- **Documentation Coverage:** 91.4894% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_suppressions` **(Many-Argument Workhorses)** (Impact: 61.6)
  * `load_from_tokens` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `delete_codes_or_comment` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `match_comments` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `eat_codes` **(Compute Cores)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 190`, `args: 84`, `func_start: 61`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 27`
* *Architecture:* `api: 42`, `import: 28`
* *Defense:* `safety: 13`, `doc: 24`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 0.001509 | `Ripple Effect (Closeness):` 0.132626
  * `Imports (Out-Degree: 23):` compact_str::CompactString, core::fmt, crate::Locator, crate::Violation, crate::checkers::ast::DiagnosticGuard, crate::checkers::ast::LintContext, crate::codes::Rule, crate::fix::edits::delete_comment...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ruff-0.15.9/crates/ruff/src/commands/format.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.981)
- **Top Global Matches:** file_cluster_8: 6.981, file_cluster_6: 10.561, file_cluster_4: 19.053
- **Magnitude:** 526.76 | **LOC:** 1426 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **88**; blast radius 0.188; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (33.7%)
- **Documentation Coverage:** 32.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Many-Argument Workhorses)** (Impact: 97.2)
    * *Intent:* /// Format a set of files, and return the exit status.
  * `format_source` **(Many-Argument Workhorses)** (Impact: 61.8)
    * *Intent:* /// Format a [`SourceKind`], returning the transformed [`SourceKind`], or `None` if the source was /...
  * `warn_incompatible_formatter_settings` **(Compute Cores)** (Impact: 53.8)
  * `write_summary` **(Compute Cores)** (Impact: 41.2)
    * *Intent:* /// Write a summary of the formatting results to the given writer.
  * `format_path` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* /// Format the file at the given [`Path`].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 238`, `args: 46`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 21`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 5`, `api: 10`, `import: 52`
* *Defense:* `safety: 28`, `doc: 33`, `test: 5`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 0.000363 | `Ripple Effect (Closeness):` 0.002209
  * `Imports (Out-Degree: 32):` anyhow::Result, colored::Colorize, crate::ExitStatus, crate::args::ConfigArguments, crate::args::FormatArguments, crate::args::FormatRange, crate::cache::Cache, crate::cache::FileCacheKey...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/rules/undefined_name.rs` (RUST) | Magnitude: 9.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 19, structural_boundaries: 7, api: 4
- `ruff-0.15.9/crates/ruff_python_ast/src/visitor/transformer.rs` (RUST) | Magnitude: 340.24 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 772, structural_boundaries: 133, branch: 84, args: 61
- `ruff-0.15.9/crates/ruff_linter/src/rules/ruff/rules/used_dummy_variable.rs` (RUST) | Magnitude: 54.08 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 115, doc: 59, structural_boundaries: 28, args: 18
- `ruff-0.15.9/crates/ruff_annotate_snippets/examples/format.rs` (RUST) | Magnitude: 4.92 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 11, core_var_decl: 6, design_snake_case: 5
- `ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/too_many_newlines_at_end_of_file.rs` (RUST) | Magnitude: 61.82 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 37, doc: 23, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/decorator_expression_eval_hack_py38.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, high_risk_execution: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/decorator_expression_py38.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/decorator_float_literal_py38.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/err/decorator_non_toplevel_call_expression_py38.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1
- `ruff-0.15.9/crates/ruff_python_parser/resources/inline/ok/decorator_expression_dotted_ident_py38.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ruff-0.15.9/crates/ruff_server/src/server/schedule.rs` (RUST) | Magnitude: 27.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 14, doc: 6, concurrency: 6
- `ruff-0.15.9/crates/ruff_server/src/format.rs` (RUST) | Magnitude: 186.26 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 596, structural_boundaries: 113, core_var_decl: 70, design_snake_case: 70
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/empty_comment.rs` (RUST) | Magnitude: 43.38 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 56, doc: 23, structural_boundaries: 19, branch: 13
- `ruff-0.15.9/crates/ruff_python_parser/src/parser/mod.rs` (RUST) | Magnitude: 361.36 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 926, doc: 172, structural_boundaries: 124, branch: 92
- `ruff-0.15.9/crates/ruff_linter/src/lib.rs` (RUST) | Magnitude: 32.72 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 52, api: 29, indent_spaces: 26, import: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/invalid_all_format.rs` (RUST) | Magnitude: 8.66 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 23, indent_spaces: 7, structural_boundaries: 6, import: 4
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/invalid_all_object.rs` (RUST) | Magnitude: 8.66 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 23, indent_spaces: 7, structural_boundaries: 6, import: 4
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pie/rules/unnecessary_range_start.rs` (RUST) | Magnitude: 22.3 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 37, doc: 21, structural_boundaries: 17, branch: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_async/rules/blocking_input.rs` (RUST) | Magnitude: 11.52 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 27, indent_spaces: 9, structural_boundaries: 7, import: 5
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/unnecessary_direct_lambda_call.rs` (RUST) | Magnitude: 9.18 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 20, structural_boundaries: 8, indent_spaces: 7, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/parentheses/opening_parentheses_comment_value.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 36, safety_bypasses: 20, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_comprehensions/rules/unnecessary_dict_comprehension_for_iterable.rs` (RUST) | Magnitude: 52.7 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, doc: 51, structural_boundaries: 34, branch: 18
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_quotes/rules/unnecessary_escaped_quote.rs` (RUST) | Magnitude: 47.44 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 83, doc: 30, structural_boundaries: 27, branch: 13
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pyi/rules/str_or_repr_defined_in_stub.rs` (RUST) | Magnitude: 26.86 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 26, doc: 15, branch: 9
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_simplify/rules/ast_unary_op.rs` (RUST) | Magnitude: 79.8 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 179, doc: 70, structural_boundaries: 47, branch: 22
- `ruff-0.15.9/crates/ruff_linter/src/rules/airflow/rules/suggested_to_update_3_0.rs` (RUST) | Magnitude: 71.5 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 285, doc: 52, structural_boundaries: 33, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_gettext/rules/format_in_gettext_func_call.rs` (RUST) | Magnitude: 23.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 41, indent_spaces: 25, structural_boundaries: 10, branch: 8
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_comprehensions/rules/unnecessary_list_comprehension_dict.rs` (RUST) | Magnitude: 26.76 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, doc: 21, structural_boundaries: 19, branch: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/airflow/rules/function_signature_change_in_3.rs` (RUST) | Magnitude: 62.68 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 32, doc: 30, branch: 19
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_comprehensions/rules/unnecessary_list_call.rs` (RUST) | Magnitude: 24.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, doc: 20, structural_boundaries: 19, branch: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_logging/rules/exception_without_exc_info.rs` (RUST) | Magnitude: 20.22 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, doc: 27, structural_boundaries: 15, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_builtins/rules/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, encapsulation: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_type_checking/rules/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, encapsulation: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/perflint/rules/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, encapsulation: 6
- `ruff-0.15.9/crates/ruff_python_semantic/src/analyze/mod.rs` (RUST) | Magnitude: 22.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8
- `ruff-0.15.9/crates/ruff_linter/src/checkers/mod.rs` (RUST) | Magnitude: 20.64 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, encapsulation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/preview_long_dict_values.py` (PYTHON) | Magnitude: 0.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 99, core_var_decl: 27, design_snake_case: 27, state_mutation: 20
- `ruff-0.15.9/crates/ruff_python_trivia/src/lib.rs` (RUST) | Magnitude: 22.26 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, api: 7, import: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/pygrep_hooks/rules/mod.rs` (RUST) | Magnitude: 20.2 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, api: 5, import: 5, encapsulation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `ruff-0.15.9/crates/ruff_linter/src/rules/flake8_pytest_style/rules/assertion.rs` (RUST) | Magnitude: 268.92 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 460, doc: 187, structural_boundaries: 120, branch: 83
- `ruff-0.15.9/crates/ruff_linter/src/rules/fastapi/rules/fastapi_unused_path_parameter.rs` (RUST) | Magnitude: 171.56 | Delta: **0.165** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 305, structural_boundaries: 92, doc: 86, branch: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ruff-0.15.9/crates/ruff_index/src/vec.rs` (RUST) | Magnitude: 72.26 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 117, generics: 64, structural_boundaries: 56, args: 24
- `ruff-0.15.9/crates/ruff_linter/src/rules/pycodestyle/rules/logical_lines/whitespace_before_parameters.rs` (RUST) | Magnitude: 28.5 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 24, doc: 20, core_var_decl: 13
- `ruff-0.15.9/crates/ruff_server/src/server/schedule/thread.rs` (RUST) | Magnitude: 35.28 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 19, doc: 16, generics: 15
- `ruff-0.15.9/crates/ruff_formatter/src/macros.rs` (RUST) | Magnitude: 18.96 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 285, indent_spaces: 175, structural_boundaries: 31, core_var_decl: 12
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/preview.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 8, api: 5, doc: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyupgrade/rules/deprecated_mock_import.rs` (RUST) | Magnitude: 188.8 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 65, branch: 51, doc: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/context_managers_39.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 42, safety_bypasses: 11, core_var_decl: 5
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/black/cases/context_managers_autodetect_311.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, safety: 2, safety_bypasses: 2
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/statement/assign.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 14, core_var_decl: 14, design_snake_case: 14
- `ruff-0.15.9/crates/ruff_annotate_snippets/tests/examples.rs` (RUST) | Magnitude: 8.06 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, core_var_decl: 9, design_snake_case: 9
- `ruff-0.15.9/crates/ruff_python_formatter/resources/test/fixtures/ruff/range_formatting/docstring_code_examples.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, args: 7, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ruff-0.15.9/crates/ruff_server/src/server/api/requests/format.rs` (RUST) | Magnitude: 69.34 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 39, core_var_decl: 19, design_snake_case: 17
- `ruff-0.15.9/crates/ruff_linter/src/rules/pyflakes/rules/unused_annotation.rs` (RUST) | Magnitude: 16.44 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 22, indent_spaces: 19, structural_boundaries: 9, branch: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/pandas_vet/rules/attr.rs` (RUST) | Magnitude: 17.52 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 27, indent_spaces: 27, structural_boundaries: 14, import: 7
- `ruff-0.15.9/crates/ruff_linter/src/rules/pylint/rules/return_in_init.rs` (RUST) | Magnitude: 16.78 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 27, indent_spaces: 21, structural_boundaries: 13, branch: 6
- `ruff-0.15.9/crates/ruff_linter/src/rules/pep8_naming/rules/lowercase_imported_as_non_lowercase.rs` (RUST) | Magnitude: 22.66 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 28, indent_spaces: 27, structural_boundaries: 13, import: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ruff-0.15.9/crates/ruff_linter/src/checkers/ast/mod.rs` -> **Severity: 9.542** (Bridge: 0.1239 * Flux: 76.9897%)
- `ruff-0.15.9/crates/ruff_workspace/src/options.rs` -> **Severity: 2.376** (Bridge: 0.0382 * Flux: 62.1372%)
- `ruff-0.15.9/crates/ruff_server/src/session/options.rs` -> **Severity: 1.316** (Bridge: 0.0835 * Flux: 15.7689%)
- `ruff-0.15.9/crates/ruff_linter/src/settings/mod.rs` -> **Severity: 1.082** (Bridge: 0.0795 * Flux: 13.6145%)
- `ruff-0.15.9/crates/ruff_formatter/src/lib.rs` -> **Severity: 0.487** (Bridge: 0.0288 * Flux: 16.8923%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ruff-0.15.9/crates/ruff_text_size/src/traits.rs` -> **Severity: 17.773** (Embedded: 0.344 * Error Risk: 51.666%)
- `ruff-0.15.9/crates/ruff_python_trivia/src/comment_ranges.rs` -> **Severity: 14.25** (Embedded: 0.2189 * Error Risk: 65.0972%)
- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 13.598** (Embedded: 0.2585 * Error Risk: 52.6063%)
- `ruff-0.15.9/crates/ruff_python_ast/src/relocate.rs` -> **Severity: 13.574** (Embedded: 0.2177 * Error Risk: 62.3625%)
- `ruff-0.15.9/crates/ruff_text_size/src/size.rs` -> **Severity: 12.66** (Embedded: 0.2689 * Error Risk: 47.0841%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ruff-0.15.9/crates/ruff_text_size/src/traits.rs` -> **Severity: 6554.35** (Blast Radius: 131.087 * Doc Risk: 50.0%)
- `ruff-0.15.9/crates/ruff_text_size/src/size.rs` -> **Severity: 5588.566** (Blast Radius: 130.4 * Doc Risk: 42.8571%)
- `ruff-0.15.9/crates/ruff_python_ast/src/lib.rs` -> **Severity: 3172.139** (Blast Radius: 46.362 * Doc Risk: 68.4211%)
- `ruff-0.15.9/crates/ruff_text_size/src/range.rs` -> **Severity: 1853.023** (Blast Radius: 70.851 * Doc Risk: 26.1538%)
- `ruff-0.15.9/crates/ruff_macros/src/derive_message_formats.rs` -> **Severity: 900.7** (Blast Radius: 9.007 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 64624 call pairs -- scoped 22.7%, unique 0.0%, ambiguous 16.5%, external 60.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 63008 | 23.2% | 0.0% | 16.7% | 60.2% |
| python | 1608 | 5.9% | 0.0% | 10.2% | 83.9% |
| embedded_python | 8 | 12.5% | 0.0% | 12.5% | 75.0% |

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
