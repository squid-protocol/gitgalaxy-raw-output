# ARCHITECTURAL_BRIEF: rust-analyzer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/rust-analyzer.git` |
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
- **Scope:** 1427 analyzed artifact(s), 444290 LOC.
- **Load-bearing artifact:** `crates/syntax/src/ast.rs` -- 371 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/hir/src/lib.rs` -- pulls in 285 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/hir/src/lib.rs` at magnitude 3355.76 (structural weight, not risk).
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
| Total Artifacts | 2262 |
| Analyzed Artifacts (Scanned) | 1427 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 835 |
| Total LOC | 444290 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 63.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5173 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1456 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 42.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5377 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 36 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1238 | 436161 | 86.8% |
| PLAINTEXT | 103 | 0 | 7.2% |
| TYPESCRIPT | 27 | 6076 | 1.9% |
| MARKDOWN | 21 | 0 | 1.5% |
| YAML | 11 | 837 | 0.8% |
| HTML | 11 | 516 | 0.8% |
| JSON | 10 | 465 | 0.7% |
| XML | 2 | 0 | 0.1% |
| DOCKERFILE | 1 | 5 | 0.1% |
| JAVASCRIPT | 1 | 120 | 0.1% |
| SHELL | 1 | 21 | 0.1% |
| PYTHON | 1 | 89 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1427 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Large Core Modules (3) 18%, Generic / Templated Code Files 13%, State Mutators Files 8%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1303 | 91.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 124 | 8.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 835*

**Composition by Extension & Reason:**
- `.rast`: 507x Excluded (Unsupported Extension: '.rast')
- `.rs`: 193x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 3862 LOC), 1x Unrecognized Syntax (Dense Structure / Global Regex Timeout)
- `.toml`: 48x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 4x Excluded (Saturation: Line 53 exceeds 500 chars), 2x Excluded (Saturation: Line 54 exceeds 500 chars), 2x Excluded (Saturation: Line 44 exceeds 500 chars)
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Embedded Array/Matrix Payload: 8237 commas in 561 LOC)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6421 LOC), 1x Excluded (Massive Static Asset Blob: 12817 LOC)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.ungram`: 2x Excluded (Unsupported Extension: '.ungram')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.9 | 7.9 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.1 | 31.5 | 48.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.6 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 30.2 | 29.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.1 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1681 | 288 | 3 | `crates/ide-diagnostics/src/handlers/invalid_cast.rs` |
| cleanup | 204 | 80 | 0 | `crates/ide-db/src/text_edit.rs` |
| guards | 12572 | 882 | 24 | `crates/hir-ty/src/consteval/tests.rs` |
| danger | 6605 | 542 | 11 | `crates/ide/src/hover/tests.rs` |
| concurrency | 1978 | 208 | 2 | `editors/code/src/commands.ts` |
| connectivity | 23176 | 949 | 41 | `crates/hir/src/lib.rs` |
| io | 278 | 69 | 0 | `editors/code/src/bootstrap.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 11 | 11 | 0 | `.github/actions/github-release/Dockerfile` |
| time | 18 | 14 | 0 | `lib/lsp-server/src/lib.rs` |
| serialization | 54 | 22 | 0 | `lib/smol_str/tests/test.rs` |
| regex | 32 | 13 | 0 | `editors/code/src/commands.ts` |
| events | 706 | 124 | 0 | `crates/hir-ty/src/method_resolution/probe.rs` |
| tests | 10134 | 593 | 19 | `crates/ide/src/hover/tests.rs` |
| docs | 15241 | 722 | 29 | `crates/rust-analyzer/src/config.rs` |
| debt | 2926 | 468 | 5 | `crates/ide-assists/src/handlers/add_missing_match_arms.rs` |
| mutation | 46153 | 1011 | 83 | `crates/ide-assists/src/handlers/extract_function.rs` |
| dead_code | 1954 | 420 | 3 | `crates/parser/src/grammar/expressions/atom.rs` |
| credential | 2 | 1 | 0 | `.github/workflows/release.yaml` |
| threat | 12 | 5 | 0 | `crates/ide/src/hover/tests.rs` |
| ml_ai | 579 | 73 | 0 | `crates/hir-ty/src/tests/patterns.rs` |
| ui | 8 | 2 | 0 | `editors/code/src/commands.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editors/code/src/bootstrap.ts` (Hits: 32)
- `crates/ide-db/src/imports/insert_use/tests.rs` (Hits: 24)
- `editors/code/src/util.ts` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast.rs** (`crates/syntax/src/ast.rs`) — 371 inbound connections
2. **lib.rs** (`crates/ide-db/src/lib.rs`) — 208 inbound connections
3. **lib.rs** (`crates/syntax/src/lib.rs`) — 193 inbound connections
4. **lib.rs** (`crates/parser/src/lib.rs`) — 182 inbound connections
5. **assists.rs** (`crates/ide-db/src/assists.rs`) — 168 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/hir/src/lib.rs`) — 285 outbound dependencies
2. **lib.rs** (`crates/ide/src/lib.rs`) — 199 outbound dependencies
3. **interner.rs** (`crates/hir-ty/src/next_solver/interner.rs`) — 160 outbound dependencies
4. **lib.rs** (`crates/ide-assists/src/lib.rs`) — 152 outbound dependencies
5. **lower.rs** (`crates/hir-ty/src/lower.rs`) — 145 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `exec_intrinsic` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **624.1** | LOC: 783
- `classify_name_ref` **(Many-Argument Workhorses)** (@ `crates/ide-completion/src/context/analysis.rs`) -> Impact: **476.7** | LOC: 814
- `lower_expr_to_place_without_adjust` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/mir/lower.rs`) -> Impact: **424.1** | LOC: 925
- `hir_fmt` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/display.rs`) -> Impact: **319.4** | LOC: 533
- `eval_rvalue` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/mir/eval.rs`) -> Impact: **289.0** | LOC: 500
- `infer_expr_inner` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/infer/expr.rs`) -> Impact: **234.4** | LOC: 753
- `run_inference` **(Many-Argument Workhorses)** (@ `crates/rust-analyzer/src/cli/analysis_stats.rs`) -> Impact: **227.7** | LOC: 368
- `pattern_match_inner` **(Many-Argument Workhorses)** (@ `crates/hir-ty/src/mir/lower/pattern_matching.rs`) -> Impact: **205.0** | LOC: 395
- `match_loop_inner` **(Many-Argument Workhorses)** (@ `crates/mbe/src/expander/matcher.rs`) -> Impact: **175.7** | LOC: 258
  * *Intent:* /// comments of this function. /// /// # Parameters /// /// - `src`: the current token of the parser. /// - `stack`: the "parent" frames of the token ...
- `definition` **(Many-Argument Workhorses)** (@ `crates/ide/src/hover/render.rs`) -> Impact: **174.8** | LOC: 366

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/ide-assists/src/handlers` | 134 | 24060.66 | 9.34% | 12.64% |
| `crates/ide/src` | 43 | 10418.64 | 8.75% | 12.78% |
| `crates/hir/src` | 11 | 7988.74 | 11.39% | 27.94% |
| `crates/hir-ty/src` | 29 | 7285.74 | 8.96% | 17.75% |
| `crates/hir-def/src` | 20 | 6372.48 | 10.1% | 16.66% |
| `crates/ide-diagnostics/src/handlers` | 52 | 4217.4 | 7.6% | 7.64% |
| `editors/code/src` | 19 | 4073.56 | 51.33% | 24.24% |
| `crates/ide-db/src` | 23 | 3904.18 | 8.9% | 14.84% |
| `crates/hir-ty/src/mir` | 5 | 3845.18 | 17.64% | 7.47% |
| `crates/hir-ty/src/next_solver` | 21 | 3779.38 | 7.27% | 29.22% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/parser/test_data/parser/ok/0031_extern.rs` -> **100.0%** Exposure
- `crates/paths/src/lib.rs` -> **100.0%** Exposure
- `crates/syntax/src/ast/generated/tokens.rs` -> **100.0%** Exposure
- `crates/parser/test_data/parser/ok/0051_parameter_attrs.rs` -> **99.999%** Exposure
- `crates/syntax/test_data/parser/fuzz-failures/0000.rs` -> **99.9931%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/ide-assists/src/utils/gen_trait_fn_body.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/ref_field_expr.rs` -> **100.0%** Exposure
- `crates/syntax-bridge/src/prettify_macro_expansion.rs` -> **100.0%** Exposure
- `lib/smol_str/src/gdb_smolstr_printer.py` -> **100.0%** Exposure
- `crates/ide-db/src/syntax_helpers/format_string_exprs.rs` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/hir/src/lib.rs` -> **0** Orphaned Functions | **87** Duplicates
- `crates/hir-ty/src/next_solver/infer/mod.rs` -> **63** Orphaned Functions | **0** Duplicates
- `crates/syntax/src/ast/generated/tokens.rs` -> **0** Orphaned Functions | **60** Duplicates
- `crates/test-utils/src/minicore.rs` -> **37** Orphaned Functions | **18** Duplicates
- `crates/ide-assists/src/handlers/extract_struct_from_enum_variant.rs` -> **35** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19390` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/hir/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 10.169)
- **Top Global Matches:** file_cluster_0: 10.169, file_cluster_15: 12.007, file_cluster_12: 12.416
- **Magnitude:** 3355.76 | **LOC:** 7283 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 45.2%
- **Blast Radius:** changing it is visible to **116** in-repo importer(s); it depends on **285**; blast radius 6.183; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (98.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.5%)
- **Documentation Coverage:** 86.1671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagnostics` **(Many-Argument Workhorses)** (Impact: 144.6)
    * *Intent:* /// Fills `acc` with the module's diagnostics.
  * `diagnostics` **(Many-Argument Workhorses)** (Impact: 138.4)
  * `fn_ptr_type` **(Generic / Templated Code)** (Impact: 22.7)
  * `iterate_method_candidates_split_inherent` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /// Allows you to treat inherent and non-inherent methods differently. /// /// Note that inherent me...
  * `contains_reference` **(Generic / Templated Code)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 676`, `structural_boundaries: 1100`, `args: 819`, `func_start: 589`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 8`, `state_mutation: 101`, `fragile_debt: 33`, `duplicate_logic: 87`
* *Architecture:* `api: 592`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 66`, `doc: 181`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.183
  * `Choke Point (Betweenness):` 0.038679 | `Ripple Effect (Closeness):` 0.18835
  * `Imports (Out-Degree: 92):` attrs, db, diagnostics, display, from_id, has_source, semantics, source_analyzer...
  * `Imported By (In-Degree: 116):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/mir/eval.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.96)
- **Top Global Matches:** file_cluster_4: 7.96, file_cluster_6: 9.806, file_cluster_0: 14.012
- **Magnitude:** 2004.66 | **LOC:** 3193 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 52.9%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **127**; blast radius 0.545; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.8%), Guard Balance (formerly Safety Score) (53.8%)
- **Documentation Coverage:** 95.3271% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eval_rvalue` **(Many-Argument Workhorses)** (Impact: 289.0)
  * `rec` **(Many-Argument Workhorses)** (Impact: 103.3)
  * `create_memory_map` **(Many-Argument Workhorses)** (Impact: 91.3)
  * `interpret_mir` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `patch_addresses` **(Many-Argument Workhorses)** (Impact: 80.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 88 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 662`, `args: 193`, `func_start: 90`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 10`, `state_mutation: 106`, `dead_code: 1`, `fragile_debt: 12`
* *Architecture:* `api: 19`, `import: 26`
* *Defense:* `safety: 79`, `doc: 22`, `test: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.545
  * `Choke Point (Betweenness):` 0.006348 | `Ripple Effect (Closeness):` 0.154513
  * `Imports (Out-Degree: 42):` shim, tests, Address::*, IntervalOrOwned::*, base_db::Crate, base_db::target::TargetLoadError, crate::CallableDefId, crate::ComplexMemoryMap...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/display.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.505)
- **Top Global Matches:** file_cluster_4: 7.505, file_cluster_6: 11.647, file_cluster_0: 11.758
- **Magnitude:** 1631.82 | **LOC:** 2489 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 63.2%
- **Blast Radius:** changing it is visible to **74** in-repo importer(s); it depends on **114**; blast radius 1.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%), Connectivity (formerly Api Exposure) (57.5%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 80.4124% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hir_fmt` **(Many-Argument Workhorses)** (Impact: 319.4)
  * `write_bounds_like_dyn_trait` **(Many-Argument Workhorses)** (Impact: 157.2)
  * `render_const_scalar_inner` **(Many-Argument Workhorses)** (Impact: 148.4)
  * `hir_fmt` **(Many-Argument Workhorses)** (Impact: 132.1)
  * `hir_fmt` **(Many-Argument Workhorses)** (Impact: 129.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 426`, `args: 94`, `func_start: 70`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 11`, `state_mutation: 52`, `dead_code: 1`, `fragile_debt: 13`
* *Architecture:* `api: 49`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 35`, `doc: 47`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.749
  * `Choke Point (Betweenness):` 0.008364 | `Ripple Effect (Closeness):` 0.179811
  * `Imports (Out-Degree: 45):` TyKind, base_db::Crate, base_db::FxIndexMap, crate::CallableDefId, crate::FnAbi, crate::ImplTraitId, crate::InferenceResult, crate::MemoryMap...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `crates/ide-assists/src/handlers/extract_function.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.581)
- **Top Global Matches:** file_cluster_0: 7.581, file_cluster_13: 8.662, file_cluster_15: 9.083
- **Magnitude:** 1544.6 | **LOC:** 6541 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 0.202; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.0%), Connectivity (formerly Api Exposure) (65.4%), Guard Balance (formerly Safety Score) (48.7%), Mutation Surface (formerly State Flux) (19.6%)
- **Documentation Coverage:** 95.4315% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyze_container` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `extract_function` **(Many-Argument Workhorses)** (Impact: 55.7)
    * *Intent:* // -> // ``` // fn main() { // let n = 1; // fun_name(n); // let g = 3; // } // // fn $0fun_name(n: ...
  * `make_body` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `make_call` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `fix_param_usages` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* /// change all usages to account for added `&`/`&mut` for some params
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 1228`, `args: 685`, `func_start: 589`, `class_start: 100`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 82`, `dead_code: 11`, `fragile_debt: 10`
* *Architecture:* `api: 160`, `concurrency: 27`, `import: 14`
* *Defense:* `safety: 75`, `doc: 68`, `test: 153`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` ast::make, core::ops::ControlFlow, crate::AssistId, crate::assist_context::AssistContext, crate::assist_context::Assists, crate::assist_context::TreeMutator, crate::tests::check_assist, crate::tests::check_assist_not_applicable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.905)
- **Top Global Matches:** file_cluster_5: 7.905, file_cluster_12: 8.893, file_cluster_7: 9.408
- **Magnitude:** 1489.3 | **LOC:** 11407 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.21; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.7%), Concurrency Surface (formerly Concurrency) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drop_glue` **(I/O & Config Routines)** (Impact: 13.6)
  * `test_hover_self` **(I/O & Config Routines)** (Impact: 10.7)
  * `subst_field` **(I/O & Config Routines)** (Impact: 9.6)
  * `type_alias_without_docs` **(I/O & Config Routines)** (Impact: 9.2)
  * `hover_trait_show_assoc_items` **(I/O & Config Routines)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 1022`, `args: 677`, `func_start: 660`, `class_start: 356`
* *Risk/State:* `safety_bypasses: 486`, `state_mutation: 108`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 416`, `concurrency: 16`, `import: 32`
* *Defense:* `safety: 3`, `doc: 157`, `test: 283`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.000475 | `Ripple Effect (Closeness):` 0.068067
  * `Imports (Out-Degree: 14):` Option::Some, b::B, c::C, core::fmt::Debug, core::ops::Deref, crate::HoverConfig, crate::HoverDocFormat, crate::MemoryLayoutHoverConfig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/handlers/request.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.787)
- **Top Global Matches:** file_cluster_4: 5.787, file_cluster_6: 9.535, file_cluster_16: 11.861
- **Magnitude:** 1446.58 | **LOC:** 2712 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **112**; blast radius 0.218; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.5%), Guard Balance (formerly Safety Score) (51.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.6%)
- **Documentation Coverage:** 99.3289% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_rustfmt` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `handle_runnables` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `handle_will_rename_files` **(Compute Cores)** (Impact: 50.0)
  * `handle_completion_resolve` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `handle_workspace_symbol` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 669`, `args: 175`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 76`, `fragile_debt: 7`
* *Architecture:* `api: 65`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 69`, `doc: 13`, `test: 2`, `sync_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.000207 | `Ripple Effect (Closeness):` 0.063033
  * `Imports (Out-Degree: 35):` anyhow::Context, base64::Engine, base64::prelude::BASE64_STANDARD, crate::config::ClientCommandsConfig, crate::config::Config, crate::config::HoverActionsConfig, crate::config::RustfmtConfig, crate::config::WorkspaceSymbolConfig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/hir/src/semantics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.728)
- **Top Global Matches:** file_cluster_0: 7.728, file_cluster_15: 10.016, file_cluster_12: 10.653
- **Magnitude:** 1416.5 | **LOC:** 2786 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **97** in-repo importer(s); it depends on **140**; blast radius 2.389; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.6%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 75.8427% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `descend_into_macros_impl` **(Many-Argument Workhorses)** (Impact: 106.2)
  * `locals_used` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `is_inside_unsafe` **(Compute Cores)** (Impact: 33.5)
    * *Intent:* /// Returns `true` if the `node` is inside an `unsafe` context.
  * `lint_attrs` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `analyze_impl` **(Many-Argument Workhorses)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 521`, `args: 373`, `func_start: 196`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 49`, `dead_code: 2`, `fragile_debt: 23`
* *Architecture:* `api: 178`, `import: 15`
* *Defense:* `safety: 54`, `doc: 102`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.389
  * `Choke Point (Betweenness):` 0.010341 | `Ripple Effect (Closeness):` 0.172219
  * `Imports (Out-Degree: 45):` child_by_source, source_to_def, base_db::FxIndexSet, crate::Adjust, crate::Adjustment, crate::Adt, crate::AnyFunctionId, crate::AutoBorrow...
  * `Imported By (In-Degree: 97):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/mir/eval/shim.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.296)
- **Top Global Matches:** file_cluster_3: 8.296, file_cluster_8: 28.64, file_cluster_6: 41.73
- **Magnitude:** 1286.94 | **LOC:** 1525 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **43**; blast radius 0.296; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.3%), Guard Balance (formerly Safety Score) (51.6%), Debt Markers (formerly Tech Debt) (27.3%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec_intrinsic` **(Many-Argument Workhorses)** (Impact: 624.1)
  * `exec_extern_c` **(Many-Argument Workhorses)** (Impact: 172.2)
  * `exec_atomic_intrinsic` **(Many-Argument Workhorses)** (Impact: 138.7)
  * `detect_and_exec_special_function` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `exec_alloc_fn` **(Many-Argument Workhorses)** (Impact: 51.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 470`, `args: 46`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 12`, `planned_debt: 2`, `fragile_debt: 14`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 21`, `doc: 4`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.296
  * `Choke Point (Betweenness):` 0.000406 | `Ripple Effect (Closeness):` 0.114951
  * `Imports (Out-Degree: 18):` simd, EvalLangItem::*, crate::InferenceResult, crate::display::DisplayTarget, crate::drop::DropGlue, crate::drop::has_drop_glue, crate::mir::eval::Address, crate::mir::eval::AdtId...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/mir/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.993)
- **Top Global Matches:** file_cluster_4: 6.993, file_cluster_6: 11.622, file_cluster_0: 11.833
- **Magnitude:** 1193.02 | **LOC:** 2341 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 52.6%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **133**; blast radius 0.452; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%), Mutation Surface (formerly State Flux) (70.2%), Guard Balance (formerly Safety Score) (51.6%)
- **Documentation Coverage:** 87.3239% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lower_expr_to_place_without_adjust` **(Many-Argument Workhorses)** (Impact: 424.1)
  * `lower_block_to_place` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `lower_params_and_bindings` **(Many-Argument Workhorses)** (Impact: 48.4)
  * `pretty_print` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `mir_body_for_closure_query` **(Many-Argument Workhorses)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 50 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 464`, `args: 101`, `func_start: 60`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 3`, `state_mutation: 80`, `dead_code: 3`, `fragile_debt: 11`
* *Architecture:* `api: 12`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 81`, `doc: 21`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.001513 | `Ripple Effect (Closeness):` 0.156032
  * `Imports (Out-Degree: 44):` as_place, pattern_matching, tests, base_db::Crate, crate::Adjust, crate::Adjustment, crate::AutoBorrow, crate::CallableDefId...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `crates/hir/src/source_analyzer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.598)
- **Top Global Matches:** file_cluster_4: 8.598, file_cluster_0: 9.808, file_cluster_16: 10.075
- **Magnitude:** 1189.4 | **LOC:** 2014 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **113**; blast radius 0.255; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.3%), Guard Balance (formerly Safety Score) (48.2%), Connectivity (formerly Api Exposure) (30.5%)
- **Documentation Coverage:** 97.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_path` **(Many-Argument Workhorses)** (Impact: 162.9)
  * `resolve_hir_path_` **(Many-Argument Workhorses)** (Impact: 87.7)
  * `resolve_offset_of_field` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `resolve_hir_path_qualifier` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* /// Resolves a path where we know it is a qualifier of another path. /// /// For example, if we have...
  * `resolve_record_field` **(Stateful Encapsulated Methods)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 394`, `args: 183`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `dead_code: 5`, `fragile_debt: 12`
* *Architecture:* `api: 58`, `import: 13`
* *Defense:* `safety: 59`, `doc: 23`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.255
  * `Choke Point (Betweenness):` 0.000422 | `Ripple Effect (Closeness):` 0.13997
  * `Imports (Out-Degree: 39):` crate::Adt, crate::AnyFunctionId, crate::AssocItem, crate::BindingMode, crate::BuiltinAttr, crate::BuiltinType, crate::Callable, crate::Const...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-def/src/expr_store/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.074)
- **Top Global Matches:** file_cluster_4: 8.074, file_cluster_15: 8.93, file_cluster_0: 9.124
- **Magnitude:** 1156.38 | **LOC:** 2961 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 45.8%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **123**; blast radius 0.741; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (66.7%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybe_collect_expr` **(Many-Argument Workhorses)** (Impact: 113.9)
    * *Intent:* /// Returns `None` if and only if the expression is `#[cfg]`d out.
  * `collect_pat` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `lower_body` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `maybe_collect_expr_as_pat` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `lower_type_ref` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* /// Converts an `ast::TypeRef` to a `hir::TypeRef`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 734`, `args: 274`, `func_start: 103`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 114`, `dead_code: 4`, `fragile_debt: 14`
* *Architecture:* `api: 30`, `concurrency: 4`, `import: 14`
* *Defense:* `safety: 99`, `doc: 60`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.741
  * `Choke Point (Betweenness):` 0.001331 | `Ripple Effect (Closeness):` 0.139423
  * `Imports (Out-Degree: 36):` asm, format_args, generics, path, base_db::FxIndexSet, cfg::CfgOptions, crate::AdtId, crate::BlockId...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `crates/ide-completion/src/context/analysis.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.398)
- **Top Global Matches:** file_cluster_6: 7.398, file_cluster_4: 9.847, file_cluster_9: 16.972
- **Magnitude:** 1115.54 | **LOC:** 2116 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 84.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **64**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%), Guard Balance (formerly Safety Score) (48.6%), Mutation Surface (formerly State Flux) (29.6%)
- **Documentation Coverage:** 60.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `classify_name_ref` **(Many-Argument Workhorses)** (Impact: 476.7)
  * `expected_type_and_name` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /// Calculate the expected type and name of the cursor position.
  * `expand` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `analyze` **(Many-Argument Workhorses)** (Impact: 80.6)
    * *Intent:* /// Fill the completion context, this is what does semantic reasoning about the surrounding context ...
  * `pattern_context_for` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 418`, `args: 225`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`, `dead_code: 6`, `fragile_debt: 3`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 62`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.063284
  * `Imports (Out-Degree: 18):` crate::completions::postfix::is_in_condition, crate::context::AttrCtx, crate::context::BreakableKind, crate::context::COMPLETION_MARKER, crate::context::CompletionAnalysis, crate::context::DotAccess, crate::context::DotAccessExprCtx, crate::context::DotAccessKind...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.487)
- **Top Global Matches:** file_cluster_0: 7.487, file_cluster_16: 8.896, file_cluster_4: 9.907
- **Magnitude:** 1056.44 | **LOC:** 2681 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 62.2%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **145**; blast radius 1.13; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.2%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 87.027% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_type_param_assoc_type_shorthand` **(Many-Argument Workhorses)** (Impact: 78.6)
    * *Intent:* /// Predicates for `param_id` of the form `P: SomeTrait`. If /// `assoc_name` is provided, only retu...
  * `lower_dyn_trait` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `generic_predicates` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* /// Resolve the where clause(s) of an item with generics, /// with a given filter
  * `query` **(Compute Cores)** (Impact: 25.9)
  * `supertraits_info` **(Compute Cores)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 504`, `args: 197`, `func_start: 111`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 96`, `dead_code: 7`, `fragile_debt: 22`
* *Architecture:* `api: 100`, `import: 15`
* *Defense:* `safety: 31`, `doc: 93`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.13
  * `Choke Point (Betweenness):` 0.001172 | `Ripple Effect (Closeness):` 0.165243
  * `Imports (Out-Degree: 33):` diagnostics, path, arrayvec::ArrayVec, crate::FnAbi, crate::ImplTraitId, crate::TyLoweringDiagnostic, crate::TyLoweringDiagnosticKind, crate::consteval::intern_const_ref...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/lsp/to_proto.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.333)
- **Top Global Matches:** file_cluster_12: 7.333, file_cluster_16: 8.184, file_cluster_4: 8.8
- **Magnitude:** 1034.48 | **LOC:** 3091 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **95**; blast radius 0.26; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.8%), Mutation Surface (formerly State Flux) (47.4%), Connectivity (formerly Api Exposure) (34.5%)
- **Documentation Coverage:** 97.2028% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `completion_item` **(Many-Argument Workhorses)** (Impact: 142.3)
  * `code_lens` **(Many-Argument Workhorses)** (Impact: 58.1)
  * `merge_text_and_snippet_edits` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `semantic_tokens` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `inlay_hint` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 419`, `args: 174`, `func_start: 86`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 1`, `state_mutation: 76`, `fragile_debt: 1`
* *Architecture:* `api: 67`, `import: 23`
* *Defense:* `safety: 26`, `doc: 11`, `test: 33`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 0.000829 | `Ripple Effect (Closeness):` 0.063751
  * `Imports (Out-Degree: 35):` a, b, c, base64::Engine, base64::prelude::BASE64_STANDARD, crate::bar, crate::config::CallInfoConfig, crate::config::ClientCommandsConfig...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/infer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.456)
- **Top Global Matches:** file_cluster_0: 7.456, file_cluster_16: 10.189, file_cluster_15: 10.26
- **Magnitude:** 998.04 | **LOC:** 2254 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **128**; blast radius 1.299; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.9%)
- **Documentation Coverage:** 86.4734% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_variant` **(Many-Argument Workhorses)** (Impact: 117.2)
  * `resolve_all` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* // FIXME: This function should be private in module. It is currently only used in the consteval, sin...
  * `struct_tail_with_normalize` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* /// Returns the deeply last field of nested structures, or the same type if /// not a structure at a...
  * `infer_query_with_inspect` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `collect_fn` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 348`, `args: 180`, `func_start: 126`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 88`, `fragile_debt: 30`
* *Architecture:* `api: 130`, `import: 20`
* *Defense:* `safety: 43`, `doc: 230`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.299
  * `Choke Point (Betweenness):` 0.006149 | `Ripple Effect (Closeness):` 0.165052
  * `Imports (Out-Degree: 51):` autoderef, cast, closure, coerce, diagnostics, expr, fallback, mutability...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.01)
- **Top Global Matches:** file_cluster_0: 7.01, file_cluster_15: 9.115, file_cluster_13: 9.419
- **Magnitude:** 997.24 | **LOC:** 4368 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **79**; blast radius 0.539; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.0%), Guard Balance (formerly Safety Score) (47.8%)
- **Documentation Coverage:** 95.4023% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply_change_with_sink` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* // FIXME @alibektas : Server's health uses error sink but in other places it is not used atm. /// Ch...
  * `field_props` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `inlay_hints` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `cargo` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `lens` **(Compute Cores)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 514`, `args: 215`, `func_start: 149`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 51`, `planned_debt: 8`, `fragile_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 184`, `import: 25`
* *Defense:* `safety: 58`, `doc: 677`, `test: 29`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.539
  * `Choke Point (Betweenness):` 0.007532 | `Ripple Effect (Closeness):` 0.073955
  * `Imports (Out-Degree: 37):` patch_old_style, _config_data, _default_str, _default_val, _impl_for_config_data, cfg::CfgAtom, cfg::CfgDiff, crate::diagnostics::DiagnosticsMapConfig...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `crates/hir-def/src/nameres/collector.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.901)
- **Top Global Matches:** file_cluster_4: 6.901, file_cluster_6: 7.534, file_cluster_15: 14.165
- **Magnitude:** 989.92 | **LOC:** 2839 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 58.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **131**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.1%), Guard Balance (formerly Safety Score) (51.1%)
- **Documentation Coverage:** 77.0833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `push_res_and_update_glob_vis` **(Many-Argument Workhorses)** (Impact: 89.8)
  * `collect` **(Many-Argument Workhorses)** (Impact: 75.5)
  * `resolve_macros` **(Many-Argument Workhorses)** (Impact: 72.6)
  * `record_resolved_import` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `seed_with_top_level` **(Compute Cores)** (Impact: 42.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 62 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 448`, `args: 103`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 4`, `state_mutation: 102`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 16`
* *Architecture:* `api: 4`, `import: 18`
* *Defense:* `safety: 80`, `doc: 107`, `test: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.132933
  * `Imports (Out-Degree: 40):` base_db::BuiltDependency, base_db::Crate, base_db::CrateOrigin, base_db::LangCrateOrigin, cfg::CfgAtom, cfg::CfgExpr, cfg::CfgOptions, crate::AdtId...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/ide/src/goto_definition.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.825)
- **Top Global Matches:** file_cluster_0: 7.825, file_cluster_13: 8.366, file_cluster_15: 9.342
- **Magnitude:** 987.7 | **LOC:** 4103 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **67**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.3%), Guard Balance (formerly Safety Score) (48.0%), Concurrency Surface (formerly Concurrency) (13.6%)
- **Documentation Coverage:** 98.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goto_definition` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* // Feature: Go to Definition // // Navigates to the definition of an identifier. // // For outline m...
  * `find_definition_for_known_blanket_dual_impls` **(Compute Cores)** (Impact: 67.5)
    * *Intent:* // If the token is into(), try_into(), search the definition of From, TryFrom.
  * `nav_for_exit_points` **(Compute Cores)** (Impact: 38.3)
  * `goto_question_mark_conversions` **(Compute Cores)** (Impact: 31.3)
    * *Intent:* /// When the `?` operator is used on `Result`, go to the `From` impl if it exists as this provides m...
  * `find_branch_root` **(Stateful Encapsulated Methods)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 599`, `args: 473`, `func_start: 431`, `class_start: 168`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 7`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 222`, `concurrency: 7`, `import: 38`
* *Defense:* `safety: 14`, `doc: 26`, `test: 168`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.08023
  * `Imports (Out-Degree: 25):` a, b, m, Foo::str, a::Foo, a::column, alloc::string::ToString, core::format_args...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/cli/analysis_stats.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.894)
- **Top Global Matches:** file_cluster_6: 6.894, file_cluster_8: 12.363, file_cluster_4: 13.383
- **Magnitude:** 986.24 | **LOC:** 1651 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 43.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **80**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Mutation Surface (formerly State Flux) (81.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_inference` **(Many-Argument Workhorses)** (Impact: 227.7)
  * `run_body_lowering` **(Many-Argument Workhorses)** (Impact: 145.8)
  * `run_term_search` **(Many-Argument Workhorses)** (Impact: 119.9)
    * *Intent:* /// Invariant: `file_ids` must be sorted and deduped before passing into here
  * `run` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `run_mir_lowering` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 386`, `args: 105`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 65`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 1`, `import: 18`
* *Defense:* `safety: 38`, `doc: 4`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.05601
  * `Imports (Out-Degree: 40):` cfg::CfgAtom, cfg::CfgDiff, crate::cli::Verbosity, crate::cli::flags, crate::cli::flags::OutputFormat, crate::cli::full_name_of_item, crate::cli::print_memory_usage, crate::cli::progress_report::ProgressReport...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/hir-def/src/attrs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.323)
- **Top Global Matches:** file_cluster_4: 8.323, file_cluster_0: 8.403, file_cluster_15: 8.725
- **Magnitude:** 975.38 | **LOC:** 1695 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **67**; blast radius 1.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.8%), Connectivity (formerly Api Exposure) (62.4%)
- **Documentation Coverage:** 94.8454% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_repr_tt` **(Defensive Guards)** (Impact: 38.3)
  * `match_attr_flags` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `derive_info` **(Defensive Guards)** (Impact: 28.3)
  * `find_ast_range` **(Compute Cores)** (Impact: 27.0)
  * `derive_info` **(Defensive Guards)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 384`, `args: 134`, `func_start: 67`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 113`, `fragile_debt: 3`
* *Architecture:* `api: 39`, `import: 23`
* *Defense:* `safety: 43`, `doc: 48`, `test: 14`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.066
  * `Choke Point (Betweenness):` 0.005491 | `Ripple Effect (Closeness):` 0.178797
  * `Imports (Out-Degree: 29):` base_db::Crate, cfg::CfgExpr, cfg::CfgOptions, crate::AdtId, crate::AstIdLoc, crate::AttrDefId, crate::FieldId, crate::FunctionId...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `crates/ide/src/rename.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.006)
- **Top Global Matches:** file_cluster_12: 8.006, file_cluster_5: 8.825, file_cluster_0: 8.912
- **Magnitude:** 949.7 | **LOC:** 3934 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **68**; blast radius 0.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.6%), Guard Balance (formerly Safety Score) (50.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.9%), Mutation Surface (formerly State Flux) (17.9%)
- **Documentation Coverage:** 98.1132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transform_method_call_into_assoc_fn` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `find_definitions` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `transform_assoc_fn_into_method_call` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `rename_to_self` **(Defensive Guards)** (Impact: 35.2)
  * `rename` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* // Feature: Rename // // Renames the item below the cursor and all of its references // // | Editor ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 560`, `args: 415`, `func_start: 331`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 7`, `state_mutation: 40`, `dead_code: 8`, `fragile_debt: 13`
* *Architecture:* `api: 151`, `import: 43`
* *Defense:* `safety: 36`, `doc: 9`, `test: 122`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.08014
  * `Imports (Out-Degree: 26):` bar, corge, foo, module, quux, qux, Foo, core::hash::Hash...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/infer/expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.448)
- **Top Global Matches:** file_cluster_4: 6.448, file_cluster_6: 10.335, file_cluster_16: 12.102
- **Magnitude:** 919.38 | **LOC:** 2246 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **88**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (60.4%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 79.0698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infer_expr_inner` **(Many-Argument Workhorses)** (Impact: 234.4)
  * `check_call_arguments` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /// Generic function that factors out common logic from function calls, /// method calls and overloa...
  * `infer_block` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `infer_method_call` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `infer_call` **(Many-Argument Workhorses)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 362`, `args: 102`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 67`, `dead_code: 12`, `fragile_debt: 20`
* *Architecture:* `api: 11`, `import: 11`
* *Defense:* `safety: 82`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.120838
  * `Imports (Out-Degree: 29):` crate::Adjust, crate::Adjustment, crate::CallableDefId, crate::DeclContext, crate::DeclOrigin, crate::Rawness, crate::autoderef::InferenceContextAutoderef, crate::consteval...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/next_solver/interner.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.656)
- **Top Global Matches:** file_cluster_0: 6.656, file_cluster_5: 9.356, file_cluster_12: 9.677
- **Magnitude:** 900.48 | **LOC:** 2709 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 78.3%
- **Blast Radius:** changing it is visible to **71** in-repo importer(s); it depends on **160**; blast radius 3.72; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (85.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.1%)
- **Documentation Coverage:** 96.7262% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `for_each_relevant_impl` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `unsizing_params_for_adt` **(Compute Cores)** (Impact: 19.5)
  * `relate` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `attach` **(Generic / Templated Code)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 25
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 456`, `args: 286`, `func_start: 198`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 26`, `state_mutation: 23`, `planned_debt: 4`, `fragile_debt: 25`, `duplicate_logic: 10`
* *Architecture:* `api: 160`, `concurrency: 6`, `import: 33`
* *Defense:* `safety: 11`, `doc: 27`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.72
  * `Choke Point (Betweenness):` 0.006172 | `Ripple Effect (Closeness):` 0.171289
  * `Imports (Out-Degree: 31):` IntTy::*, UintTy::*, base_db::Crate, base_db::Nonce, crate::FnAbi, crate::db::HirDatabase, crate::db::InternedCoroutine, crate::db::InternedCoroutineId...
  * `Imported By (In-Degree: 71):` (Excluded from Brief to save tokens)

### `crates/ide-assists/src/handlers/generate_function.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.535)
- **Top Global Matches:** file_cluster_0: 6.535, file_cluster_13: 8.626, file_cluster_15: 9.153
- **Magnitude:** 892.38 | **LOC:** 3246 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **51**; blast radius 0.202; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.9%), Guard Balance (formerly Safety Score) (59.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.8%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn_generic_params` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /// Gets parameter bounds and where predicates in scope and filters out irrelevant ones. Returns ///...
  * `from_call` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /// Prepares a generated function that matches `call`. /// The function is generated in `target_modu...
  * `gen_method` **(Defensive Guards)** (Impact: 24.5)
  * `fn_arg_type` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `gen_fn` **(Compute Cores)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 76
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 536`, `args: 420`, `func_start: 365`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 79`, `state_mutation: 31`, `dead_code: 9`, `planned_debt: 81`, `fragile_debt: 7`
* *Architecture:* `api: 117`, `concurrency: 20`, `import: 10`
* *Defense:* `safety: 33`, `doc: 98`, `test: 77`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` foo, crate::AssistContext, crate::AssistId, crate::Assists, crate::tests::check_assist, crate::tests::check_assist_not_applicable, crate::utils::convert_reference_type, crate::utils::expr_fill_default...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/render.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.26)
- **Top Global Matches:** file_cluster_6: 7.26, file_cluster_4: 9.35, file_cluster_9: 16.352
- **Magnitude:** 888.48 | **LOC:** 1432 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **64**; blast radius 0.21; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.3%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 93.0233% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `definition` **(Many-Argument Workhorses)** (Impact: 174.8)
  * `render_memory_layout` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `try_expr` **(Many-Argument Workhorses)** (Impact: 70.8)
  * `literal` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `closure_ty` **(Many-Argument Workhorses)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 315`, `args: 125`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 57`
* *Architecture:* `api: 15`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 57`, `doc: 6`, `test: 8`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.068067
  * `Imports (Out-Degree: 26):` crate::HoverAction, crate::HoverConfig, crate::HoverResult, crate::Markup, crate::MemoryLayoutHoverConfig, crate::MemoryLayoutHoverRenderKind, crate::doc_links::remove_links, crate::doc_links::rewrite_links...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/ide-assists/src/handlers/generate_fn_type_alias.rs` (RUST) | Magnitude: 100.56 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 256, structural_boundaries: 103, pointers: 51, args: 45
- `crates/syntax/src/parsing/reparsing.rs` (RUST) | Magnitude: 129.3 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 329, structural_boundaries: 74, core_var_decl: 31, args: 29
- `crates/ide-ssr/src/resolving.rs` (RUST) | Magnitude: 155.7 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 66, branch: 51, generics: 29
- `crates/hir-ty/src/infer/cast.rs` (RUST) | Magnitude: 152.28 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 401, structural_boundaries: 61, branch: 41, generics: 38
- `crates/ide-diagnostics/src/handlers/type_mismatch.rs` (RUST) | Magnitude: 349.5 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 825, structural_boundaries: 189, args: 153, func_start: 148

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `editors/code/src/commands.ts` (TYPESCRIPT) | Magnitude: 869.94 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1074, structural_boundaries: 405, core_var_decl: 218, design_snake_case: 173

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/ide-assists/src/handlers/flip_comma.rs` (RUST) | Magnitude: 48.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 39, core_var_decl: 20, args: 19
- `crates/test-fixture/src/lib.rs` (RUST) | Magnitude: 376.34 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 861, structural_boundaries: 242, core_var_decl: 123, design_snake_case: 119
- `crates/hir-def/src/macro_expansion_tests/mbe/regression.rs` (RUST) | Magnitude: 140.68 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 661, structural_boundaries: 146, decorators: 100, args: 79
- `crates/hir-def/src/nameres/tests/incremental.rs` (RUST) | Magnitude: 89.2 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 404, structural_boundaries: 71, args: 34, api: 28
- `crates/ide/src/typing.rs` (RUST) | Magnitude: 429.44 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1170, structural_boundaries: 209, args: 186, func_start: 167

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/ide-assists/src/handlers/extract_variable.rs` (RUST) | Magnitude: 484.56 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1635, structural_boundaries: 387, func_start: 318, args: 244
- `crates/syntax/test_data/parser/validation/0037_visibility_in_traits.rs` (RUST) | Magnitude: 5.32 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, api: 3, structural_boundaries: 2, args: 2
- `crates/project-model/src/toolchain_info/target_data.rs` (RUST) | Magnitude: 29.96 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 31, core_var_decl: 10, design_snake_case: 10
- `crates/ide/src/inlay_hints/placeholders.rs` (RUST) | Magnitude: 26.62 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 17, args: 6, func_start: 6
- `crates/ide-assists/src/handlers/unwrap_return_type.rs` (RUST) | Magnitude: 395.92 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1623, structural_boundaries: 480, args: 245, func_start: 213

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/proc-macro-srv/proc-macro-test/build.rs` (RUST) | Magnitude: 28.86 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 34, core_var_decl: 21, design_snake_case: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/proc-macro-srv-cli/src/main_loop.rs` (RUST) | Magnitude: 175.42 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 468, structural_boundaries: 102, core_var_decl: 55, design_snake_case: 52
- `crates/rust-analyzer/src/cli.rs` (RUST) | Magnitude: 26.28 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 34, args: 8, api: 8
- `crates/hir-ty/src/layout/target.rs` (RUST) | Magnitude: 18.48 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 6, import: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/parser/test_data/parser/ok/0012_visibility.rs` (RUST) | Magnitude: 10.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 5, func_start: 5, api: 5, unreferenced_by_name: 5
- `crates/ide-completion/src/render/macro_.rs` (RUST) | Magnitude: 108.86 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 216, args: 39, structural_boundaries: 37, func_start: 34
- `crates/rust-analyzer/src/lsp/from_proto.rs` (RUST) | Magnitude: 90.56 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 93, branch: 31, structural_boundaries: 29, core_var_decl: 20
- `crates/hir-ty/src/utils.rs` (RUST) | Magnitude: 80.28 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 30, branch: 20, core_var_decl: 13
- `crates/proc-macro-api/src/pool.rs` (RUST) | Magnitude: 39.62 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 18, args: 13, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/parser/test_data/parser/inline/err/generic_arg_list_recover_expr.rs` (RUST) | Magnitude: 11.04 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 2
- `crates/parser/test_data/parser/inline/ok/array_attrs.rs` (RUST) | Magnitude: 10.52 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: test: 1, globals: 1, immutability_locks: 1
- `crates/parser/test_data/parser/inline/ok/assoc_item_list.rs` (RUST) | Magnitude: 2.72 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/parser/test_data/parser/inline/err/anonymous_static.rs` (RUST) | Magnitude: 10.52 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 1, core_var_decl: 1, design_snake_case: 1
- `crates/parser/test_data/parser/inline/err/generic_static.rs` (RUST) | Magnitude: 10.52 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 1, core_var_decl: 1, design_snake_case: 1
- `crates/parser/test_data/parser/inline/ok/anonymous_const.rs` (RUST) | Magnitude: 10.52 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 1, core_var_decl: 1, design_snake_case: 1
- `crates/hir-ty/src/lower/diagnostics.rs` (RUST) | Magnitude: 24.42 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, doc: 12, structural_boundaries: 8, api: 8
- `crates/parser/test_data/parser/err/0051_let_else_right_curly_brace_match.rs` (RUST) | Magnitude: 3.56 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, branch: 2, structural_boundaries: 2, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/hir-def/src/attrs.rs` (RUST) | Magnitude: 975.38 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1396, structural_boundaries: 384, branch: 222, core_var_decl: 205
- `crates/ide-completion/src/completions/attribute.rs` (RUST) | Magnitude: 105.04 | Delta: **0.183** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 351, structural_boundaries: 56, core_var_decl: 31, args: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/ide-completion/src/tests/flyimport.rs` (RUST) | Magnitude: 458.52 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1087, structural_boundaries: 433, api: 254, args: 250
- `crates/hir-ty/src/diagnostics/match_check/pat_analysis.rs` (RUST) | Magnitude: 190.22 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 403, structural_boundaries: 88, core_var_decl: 86, design_snake_case: 59
- `crates/hir-ty/src/tests/regression/new_solver.rs` (RUST) | Magnitude: 161.0 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 455, generics: 309, structural_boundaries: 222, args: 92
- `crates/profile/src/lib.rs` (RUST) | Magnitude: 14.0 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, doc: 30, structural_boundaries: 13, decorators: 7
- `crates/rust-analyzer/src/cli/lsif.rs` (RUST) | Magnitude: 98.64 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 91, core_var_decl: 44, design_snake_case: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/hir-def/src/macro_expansion_tests/builtin_fn_macro.rs` (RUST) | Magnitude: 66.42 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 196, args: 71, decorators: 70, func_start: 66
- `lib/lsp-server/examples/manual_test.sh` (SHELL) | Magnitude: 11.72 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: io: 7, structural_boundaries: 4, safety_bypasses: 3, debug_prints: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/syntax-bridge/src/tests.rs` (RUST) | Magnitude: 22.68 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 80, bitwise_ops: 24, structural_boundaries: 18, import: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/hir/src/lib.rs` -> Churn: **100.0%** | Cog Load: 8.672% | Debt: 98.1421%
- `crates/hir-ty/src/infer.rs` -> Churn: **87.63%** | Cog Load: 12.6465% | Debt: 52.2653%
- `crates/hir-ty/src/next_solver/interner.rs` -> Churn: **84.5%** | Cog Load: 9.9465% | Debt: 85.2534%
- `crates/proc-macro-srv/src/lib.rs` -> Churn: **79.41%** | Cog Load: 6.8965% | Debt: 68.1542%
- `crates/hir-def/src/resolver.rs` -> Churn: **72.0%** | Cog Load: 7.5549% | Debt: 86.6402%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ide-completion/src/context/analysis.rs` -> **A4-Tacks** (84.2% isolated ownership) | Magnitude: 1115.54
- `crates/syntax/src/ast/syntax_factory/constructors.rs` -> **bit-aloo** (82.9% isolated ownership) | Magnitude: 875.68
- `editors/code/src/commands.ts` -> **jackh726** (100.0% isolated ownership) | Magnitude: 869.94
- `crates/hir-def/src/find_path.rs` -> **Lukas Wirth** (100.0% isolated ownership) | Magnitude: 709.0
- `crates/hir-ty/src/infer/coerce.rs` -> **Chayim Refael Friedman** (81.8% isolated ownership) | Magnitude: 655.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/ide/src/syntax_highlighting.rs` -> **Severity: 2.675** (Bridge: 0.0274 * Flux: 97.6601%)
- `crates/test-fixture/src/lib.rs` -> **Severity: 1.275** (Bridge: 0.028 * Flux: 45.4561%)
- `crates/hir/src/lib.rs` -> **Severity: 1.109** (Bridge: 0.0387 * Flux: 28.675%)
- `crates/ide/src/syntax_highlighting/inject.rs` -> **Severity: 1.002** (Bridge: 0.0112 * Flux: 89.1852%)
- `crates/hir-ty/src/lib.rs` -> **Severity: 0.967** (Bridge: 0.0355 * Flux: 27.2722%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/syntax/src/ast.rs` -> **Severity: 25.021** (Embedded: 0.3128 * Error Risk: 80.0%)
- `crates/stdx/src/lib.rs` -> **Severity: 13.767** (Embedded: 0.272 * Error Risk: 50.6097%)
- `crates/test-utils/src/lib.rs` -> **Severity: 13.401** (Embedded: 0.2175 * Error Risk: 61.6051%)
- `crates/syntax/src/lib.rs` -> **Severity: 13.171** (Embedded: 0.2624 * Error Risk: 50.1923%)
- `crates/parser/src/lib.rs` -> **Severity: 12.793** (Embedded: 0.2773 * Error Risk: 46.1302%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/syntax/src/ast.rs` -> **Severity: 2657.13** (Blast Radius: 29.47 * Doc Risk: 90.1639%)
- `crates/syntax/src/syntax_node.rs` -> **Severity: 2127.2** (Blast Radius: 21.272 * Doc Risk: 100.0%)
- `crates/edition/src/lib.rs` -> **Severity: 2013.5** (Blast Radius: 20.135 * Doc Risk: 100.0%)
- `crates/syntax/src/lib.rs` -> **Severity: 1573.274** (Blast Radius: 25.959 * Doc Risk: 60.6061%)
- `crates/intern/src/symbol.rs` -> **Severity: 1570.678** (Blast Radius: 16.915 * Doc Risk: 92.8571%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 696 literal sites + 8 sites through wrappers = 704
- **`panics_and_aborts`:** 369 literal sites + 2 sites through wrappers = 371

- `error` (function, debug_prints, primitive): 3 call sites in 1 files -- `editors/code/tests/unit/index.ts`
- `ok` (function, debug_prints, primitive): 3 call sites in 1 files -- `editors/code/tests/unit/index.ts`
- `read_text` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `crates/syntax/src/tests.rs`
- `canttouchthis` (function, debug_prints, primitive): 1 call sites in 1 files -- `crates/parser/test_data/parser/ok/0035_weird_exprs.rs`
- `evil_lincoln` (function, debug_prints, primitive): 1 call sites in 1 files -- `crates/parser/test_data/parser/ok/0035_weird_exprs.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 107676 call pairs -- scoped 26.2%, unique 0.0%, ambiguous 25.9%, external 47.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 106566 | 26.2% | 0.0% | 26.1% | 47.7% |
| typescript | 1051 | 31.2% | 0.0% | 5.4% | 63.4% |
| javascript | 28 | 10.7% | 0.0% | 17.9% | 71.4% |
| python | 28 | 21.4% | 0.0% | 0.0% | 78.6% |
| shell | 3 | 33.3% | 0.0% | 0.0% | 66.7% |

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
