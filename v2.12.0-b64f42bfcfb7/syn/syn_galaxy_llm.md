# ARCHITECTURAL_BRIEF: syn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dtolnay/syn.git` |
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
- **Scope:** 144 analyzed artifact(s), 53010 LOC.
- **Load-bearing artifact:** `src/parse.rs` -- 40 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/lib.rs` -- pulls in 258 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/expr.rs` at magnitude 2068.46 (structural weight, not risk).
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
| Total Artifacts | 165 |
| Analyzed Artifacts (Scanned) | 144 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 53010 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 87.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3437 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1841 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 26.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8177 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 130 | 52190 | 90.3% |
| MARKDOWN | 8 | 0 | 5.6% |
| YAML | 2 | 183 | 1.4% |
| PLAINTEXT | 2 | 0 | 1.4% |
| SHELL | 1 | 10 | 0.7% |
| CSS | 1 | 627 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 144 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 23%, State Mutators Files 15%, Data / Markup / Trivial 13%, Generic / Templated Code Files 12%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 134 | 93.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 6.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
- `.toml`: 14x Unsupported Format (.toml)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unrecognized Syntax (Dense Structure / Global Regex Timeout)
- `.json`: 1x Excluded (Massive Static Asset Blob: 5687 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 62.7 | 9.0 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.1 | 36.9 | 49.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.4 | 7.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.7 | 24.1 | 19.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.9 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.9 | 1.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 79.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 293 | 40 | 4 | `src/gen/fold.rs` |
| cleanup | 7 | 6 | 0 | `tests/test_punctuated.rs` |
| guards | 703 | 86 | 12 | `src/gen/visit.rs` |
| danger | 355 | 75 | 6 | `tests/test_pat.rs` |
| concurrency | 168 | 18 | 1 | `tests/repo/mod.rs` |
| connectivity | 2223 | 92 | 34 | `src/item.rs` |
| io | 27 | 16 | 1 | `dev/import.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `tests/test_round_trip.rs` |
| serialization | 2 | 2 | 0 | `codegen/src/json.rs` |
| regex | 1 | 1 | 0 | `examples/lazy-static/example/src/main.rs` |
| events | 69 | 11 | 0 | `tests/test_receiver.rs` |
| tests | 346 | 42 | 9 | `tests/test_parse_stream.rs` |
| docs | 5778 | 56 | 119 | `src/parse.rs` |
| debt | 273 | 38 | 5 | `src/lit.rs` |
| mutation | 3040 | 120 | 48 | `src/item.rs` |
| dead_code | 219 | 46 | 6 | `tests/test_receiver.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `src/lib.rs` |
| ml_ai | 4 | 1 | 0 | `tests/test_lit.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dev/import.sh` (Hits: 8)
- `codegen/src/file.rs` (Hits: 2)
- `examples/dump-syntax/src/main.rs` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **parse.rs** (`src/parse.rs`) — 40 inbound connections
2. **error.rs** (`src/error.rs`) — 37 inbound connections
3. **expr.rs** (`src/expr.rs`) — 28 inbound connections
4. **token.rs** (`src/token.rs`) — 26 inbound connections
5. **punctuated.rs** (`src/punctuated.rs`) — 21 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`src/lib.rs`) — 258 outbound dependencies
2. **eq.rs** (`tests/common/eq.rs`) — 213 outbound dependencies
3. **expr.rs** (`src/expr.rs`) — 100 outbound dependencies
4. **item.rs** (`src/item.rs`) — 94 outbound dependencies
5. **test_precedence.rs** (`tests/test_precedence.rs`) — 71 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ambig_ty` **(Many-Argument Workhorses)** (@ `src/ty.rs`) -> Impact: **256.7** | LOC: 294
- `parse_rest_of_item` **(Many-Argument Workhorses)** (@ `src/item.rs`) -> Impact: **236.8** | LOC: 176
- `scan_right` **(Many-Argument Workhorses)** (@ `src/fixup.rs`) -> Impact: **212.5** | LOC: 282
- `atom_expr` **(Compute Cores)** (@ `src/expr.rs`) -> Impact: **149.3** | LOC: 76
  * *Intent:* // Parse all atomic expressions which don't have to worry about precedence // interactions, as they are fully contained.
- `expand_impl_body` **(Many-Argument Workhorses)** (@ `codegen/src/snapshot.rs`) -> Impact: **118.1** | LOC: 170
- `parse_stmt` **(Compute Cores)** (@ `src/stmt.rs`) -> Impact: **103.8** | LOC: 67
- `parse` **(Compute Cores)** (@ `src/op.rs`) -> Impact: **86.5** | LOC: 61
- `parse_expr` **(Many-Argument Workhorses)** (@ `src/expr.rs`) -> Impact: **84.5** | LOC: 80
- `parse_impl` **(Many-Argument Workhorses)** (@ `src/item.rs`) -> Impact: **84.4** | LOC: 95
- `parse_with_earlier_boundary_rule` **(Compute Cores)** (@ `src/expr.rs`) -> Impact: **76.5** | LOC: 60

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 48 | 10747.42 | 10.9% | 14.02% |
| `src/gen` | 8 | 6721.32 | 6.6% | 19.1% |
| `codegen/src` | 20 | 1627.48 | 18.12% | 1.89% |
| `tests` | 27 | 1062.56 | 2.26% | 0.0% |
| `tests/common` | 4 | 292.7 | 14.54% | 0.0% |
| `tests/repo` | 2 | 260.56 | 21.79% | 0.0% |
| `examples/trace-var/trace-var/src` | 1 | 59.48 | 4.72% | 0.0% |
| `benches` | 2 | 59.12 | 7.68% | 10.94% |
| `.github/workflows` | 1 | 57.34 | 7.35% | 0.0% |
| `examples/dump-syntax/src` | 1 | 40.6 | 9.3% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/punctuated.rs` -> **99.432%** Exposure
- `src/lit.rs` -> **99.4054%** Exposure
- `src/token.rs` -> **91.8797%** Exposure
- `src/attr.rs` -> **79.7344%** Exposure
- `src/gen/eq.rs` -> **70.3132%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `codegen/src/css.rs` -> **100.0%** Exposure
- `src/bigint.rs` -> **100.0%** Exposure
- `src/whitespace.rs` -> **100.0%** Exposure
- `tests/common/visit.rs` -> **100.0%** Exposure
- `codegen/src/gen.rs` -> **99.8887%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/lit.rs` -> **0** Orphaned Functions | **48** Duplicates
- `src/gen/eq.rs` -> **0** Orphaned Functions | **31** Duplicates
- `src/gen/hash.rs` -> **0** Orphaned Functions | **31** Duplicates
- `src/punctuated.rs` -> **0** Orphaned Functions | **26** Duplicates
- `tests/test_receiver.rs` -> **20** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2136` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.987)
- **Top Global Matches:** file_cluster_4: 7.987, file_cluster_6: 11.518, file_cluster_0: 12.688
- **Magnitude:** 2068.46 | **LOC:** 4180 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **100**; blast radius 21.226; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.8%), Guard Balance (formerly Safety Score) (50.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 96.5116% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `atom_expr` **(Compute Cores)** (Impact: 149.3)
    * *Intent:* // Parse all atomic expressions which don't have to worry about precedence // interactions, as they ...
  * `parse_expr` **(Many-Argument Workhorses)** (Impact: 84.5)
  * `parse_with_earlier_boundary_rule` **(Compute Cores)** (Impact: 76.5)
  * `trailer_helper` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `parse_range_end` **(Compute Cores)** (Impact: 55.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 850`, `structural_boundaries: 694`, `args: 270`, `func_start: 159`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 4`, `state_mutation: 49`, `dead_code: 6`
* *Architecture:* `api: 237`, `concurrency: 11`, `import: 68`
* *Defense:* `safety: 32`, `doc: 382`, `test: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.226
  * `Choke Point (Betweenness):` 0.036832 | `Ripple Effect (Closeness):` 0.260982
  * `Imports (Out-Degree: 20):` alloc::boxed::Box, alloc::format, alloc::string::ToString, alloc::vec::Vec, core::fmt, core::fmt::Display, core::hash::Hash, core::hash::Hasher...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `src/item.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.415)
- **Top Global Matches:** file_cluster_4: 8.415, file_cluster_6: 10.569, file_cluster_0: 13.871
- **Magnitude:** 1944.04 | **LOC:** 3519 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **94**; blast radius 7.836; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.8%), Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.6%)
- **Documentation Coverage:** 98.1481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_rest_of_item` **(Many-Argument Workhorses)** (Impact: 236.8)
  * `parse_impl` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `parse` **(Compute Cores)** (Impact: 75.5)
  * `parse_use_tree` **(Compute Cores)** (Impact: 74.8)
  * `parse` **(Compute Cores)** (Impact: 66.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 743`, `args: 156`, `func_start: 104`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 39`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 261`, `concurrency: 4`, `import: 53`
* *Defense:* `safety: 30`, `doc: 135`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.836
  * `Choke Point (Betweenness):` 0.030287 | `Ripple Effect (Closeness):` 0.168007
  * `Imports (Out-Degree: 21):` alloc::boxed::Box, alloc::vec::Vec, core::mem, crate::attr, crate::attr::Attribute, crate::attr::FilterAttrs, crate::data::Fields, crate::data::FieldsNamed...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/gen/visit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.656)
- **Top Global Matches:** file_cluster_0: 5.656, file_cluster_13: 9.71, file_cluster_15: 10.822
- **Magnitude:** 1498.46 | **LOC:** 3942 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (5.9%)
- **Documentation Coverage:** 99.8221% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_item_trait` **(Generic / Templated Code)** (Impact: 10.1)
  * `visit_type_bare_fn` **(Defensive Guards)** (Impact: 9.9)
  * `visit_expr_struct` **(Generic / Templated Code)** (Impact: 9.8)
  * `visit_pat_struct` **(Generic / Templated Code)** (Impact: 9.8)
  * `visit_expr_closure` **(Generic / Templated Code)** (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 655`, `args: 375`, `func_start: 375`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 188`, `import: 1`
* *Defense:* `safety: 59`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.093138
  * `Imports (Out-Degree: 1):` crate::punctuated::Punctuated
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/gen/visit_mut.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.715)
- **Top Global Matches:** file_cluster_0: 6.715, file_cluster_13: 8.475, file_cluster_15: 9.969
- **Magnitude:** 1329.04 | **LOC:** 3762 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 3.132; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.7%), Guard Balance (formerly Safety Score) (48.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.7%)
- **Documentation Coverage:** 99.8224% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_type_bare_fn_mut` **(Defensive Guards)** (Impact: 9.9)
  * `visit_item_trait_mut` **(Generic / Templated Code)** (Impact: 8.2)
  * `visit_signature_mut` **(Defensive Guards)** (Impact: 8.2)
  * `visit_expr_struct_mut` **(Defensive Guards)** (Impact: 8.0)
  * `visit_pat_struct_mut` **(Defensive Guards)** (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 1484`, `args: 376`, `func_start: 376`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 188`, `import: 2`
* *Defense:* `safety: 59`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.132
  * `Choke Point (Betweenness):` 0.000259 | `Ripple Effect (Closeness):` 0.100199
  * `Imports (Out-Degree: 1):` alloc::vec::Vec, crate::punctuated::Punctuated
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/gen/fold.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.583)
- **Top Global Matches:** file_cluster_0: 6.583, file_cluster_13: 8.23, file_cluster_15: 9.864
- **Magnitude:** 1169.06 | **LOC:** 3907 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 3.112; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.3%), Guard Balance (formerly Safety Score) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.7%)
- **Documentation Coverage:** 99.8227% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fold_expr` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `fold_type` **(Many-Argument Workhorses)** (Impact: 6.0)
  * `fold_item` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `fold_bin_op` **(Generic / Templated Code)** (Impact: 5.3)
  * `fold_pat` **(Generic / Templated Code)** (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 594`, `args: 433`, `func_start: 377`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 188`, `import: 2`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.112
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.094728
  * `Imports (Out-Degree: 0):` alloc::boxed::Box, alloc::vec::Vec
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/gen/eq.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.913)
- **Top Global Matches:** file_cluster_0: 7.913, file_cluster_13: 9.491, file_cluster_15: 10.234
- **Magnitude:** 991.6 | **LOC:** 2309 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.181; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.3%), Complexity Load (formerly Cognitive Load) (14.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eq` **(Compute Cores)** (Impact: 17.7)
  * `eq` **(Compute Cores)** (Impact: 15.9)
  * `eq` **(Compute Cores)** (Impact: 15.9)
  * `eq` **(Compute Cores)** (Impact: 12.4)
  * `eq` **(Compute Cores)** (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 699`, `structural_boundaries: 359`, `args: 175`, `func_start: 175`
* *Risk/State:* `duplicate_logic: 31`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` alloc::string::ToString, crate::tt::TokenStreamHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.848)
- **Top Global Matches:** file_cluster_0: 7.848, file_cluster_12: 9.197, file_cluster_15: 9.467
- **Magnitude:** 860.2 | **LOC:** 1929 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **55**; blast radius 9.496; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Mutation Surface (formerly State Flux) (93.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.9%)
- **Documentation Coverage:** 93.0348% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_lit_float` **(Compute Cores)** (Impact: 44.1)
    * *Intent:* // Returns base 10 digits and suffix.
  * `parse_lit_int` **(Compute Cores)** (Impact: 41.2)
    * *Intent:* // Returns base 10 digits and suffix.
  * `parse_lit_c_str_cooked` **(Compute Cores)** (Impact: 29.3)
  * `from_str` **(Defensive Guards)** (Impact: 28.4)
  * `parse_lit_str_cooked` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 66 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 382`, `args: 130`, `func_start: 126`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 7`, `state_mutation: 70`, `duplicate_logic: 48`
* *Architecture:* `api: 89`, `import: 41`
* *Defense:* `safety: 19`, `doc: 119`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.496
  * `Choke Point (Betweenness):` 0.004518 | `Ripple Effect (Closeness):` 0.220488
  * `Imports (Out-Degree: 7):` alloc::borrow::ToOwned, alloc::boxed::Box, alloc::ffi::CString, alloc::format, alloc::rc::Rc, alloc::string::String, alloc::string::ToString, alloc::vec::Vec...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/gen/debug.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.983)
- **Top Global Matches:** file_cluster_15: 6.983, file_cluster_0: 7.221, file_cluster_13: 7.719
- **Magnitude:** 806.6 | **LOC:** 3239 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.181; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Debt Markers (formerly Tech Debt) (15.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `fmt` **(Annotated & Test Methods)** (Impact: 8.9)
  * `fmt` **(Compute Cores)** (Impact: 6.9)
  * `fmt` **(Compute Cores)** (Impact: 6.7)
  * `fmt` **(Compute Cores)** (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 1009`, `args: 282`, `func_start: 282`
* *Risk/State:* `high_risk_execution: 2`, `duplicate_logic: 10`
* *Architecture:* `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::fmt, core::fmt::Debug
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/generics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.068)
- **Top Global Matches:** file_cluster_6: 9.068, file_cluster_4: 9.649, file_cluster_0: 15.524
- **Magnitude:** 719.18 | **LOC:** 1483 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **50**; blast radius 11.32; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.2%), Guard Balance (formerly Safety Score) (49.9%), Debt Markers (formerly Tech Debt) (21.8%)
- **Documentation Coverage:** 76.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 51.3)
  * `do_parse` **(Compute Cores)** (Impact: 49.6)
  * `parse_multiple` **(Stateful Encapsulated Methods)** (Impact: 37.1)
  * `parse` **(Compute Cores)** (Impact: 35.5)
  * `parse` **(Compute Cores)** (Impact: 29.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 287`, `args: 91`, `func_start: 59`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 13`, `duplicate_logic: 6`
* *Architecture:* `api: 85`, `import: 36`
* *Defense:* `safety: 19`, `doc: 83`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.32
  * `Choke Point (Betweenness):` 0.004406 | `Ripple Effect (Closeness):` 0.210009
  * `Imports (Out-Degree: 14):` alloc::vec::Vec, core::fmt, core::fmt::Debug, core::hash::Hash, core::hash::Hasher, crate::attr::Attribute, crate::attr::FilterAttrs, crate::error...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/ty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.245)
- **Top Global Matches:** file_cluster_4: 8.245, file_cluster_0: 9.764, file_cluster_15: 11.134
- **Magnitude:** 685.9 | **LOC:** 1276 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **51**; blast radius 11.204; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.4%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (32.9%)
- **Documentation Coverage:** 96.4912% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ambig_ty` **(Many-Argument Workhorses)** (Impact: 256.7)
  * `parse_bare_fn_arg` **(Compute Cores)** (Impact: 52.6)
  * `parse` **(Compute Cores)** (Impact: 30.4)
  * `parse` **(Stateful Encapsulated Methods)** (Impact: 16.3)
  * `parse_bare_variadic` **(Generic / Templated Code)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 272`, `args: 71`, `func_start: 49`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 17`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 74`, `import: 37`
* *Defense:* `safety: 9`, `doc: 55`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.204
  * `Choke Point (Betweenness):` 0.003986 | `Ripple Effect (Closeness):` 0.222158
  * `Imports (Out-Degree: 15):` alloc::boxed::Box, alloc::vec::Vec, crate::attr::Attribute, crate::attr::FilterAttrs, crate::error, crate::error::Result, crate::expr::Expr, crate::ext::IdentExt...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/gen/hash.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.342)
- **Top Global Matches:** file_cluster_0: 5.342, file_cluster_13: 9.197, file_cluster_2: 10.08
- **Magnitude:** 513.5 | **LOC:** 2879 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.181; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (54.9%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hash` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `hash` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `hash` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `hash` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `hash` **(Many-Argument Workhorses)** (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 528`, `args: 175`, `func_start: 175`
* *Risk/State:* `high_risk_execution: 2`, `duplicate_logic: 31`
* *Architecture:* `import: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` alloc::string::ToString, core::hash::Hash, core::hash::Hasher, crate::tt::TokenStreamHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pat.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.946)
- **Top Global Matches:** file_cluster_4: 7.946, file_cluster_6: 11.65, file_cluster_0: 11.705
- **Magnitude:** 439.08 | **LOC:** 960 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **47**; blast radius 6.071; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.6%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (11.7%)
- **Documentation Coverage:** 83.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_single` **(Compute Cores)** (Impact: 57.4)
    * *Intent:* /// ```compile_fail /// fn f(Some(_) | None: Option<T>) { /// let _ = |Some(_) | None: Option<T>| {}...
  * `pat_range_bound` **(Compute Cores)** (Impact: 37.0)
  * `field_pat` **(Compute Cores)** (Impact: 29.2)
  * `multi_pat_impl` **(Compute Cores)** (Impact: 23.6)
  * `pat_struct` **(Many-Argument Workhorses)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 159`, `args: 63`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 62`, `import: 34`
* *Defense:* `safety: 4`, `doc: 116`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.071
  * `Choke Point (Betweenness):` 0.000915 | `Ripple Effect (Closeness):` 0.193389
  * `Imports (Out-Degree: 14):` alloc::boxed::Box, alloc::vec::Vec, crate::attr::Attribute, crate::attr::FilterAttrs, crate::error, crate::error::Result, crate::expr::Expr, crate::expr::ExprConst...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/gen/clone.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.645)
- **Top Global Matches:** file_cluster_0: 6.645, file_cluster_13: 7.321, file_cluster_2: 8.762
- **Magnitude:** 411.68 | **LOC:** 2268 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%), Debt Markers (formerly Tech Debt) (12.5%), Complexity Load (formerly Cognitive Load) (7.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clone` **(Annotated & Test Methods)** (Impact: 4.3)
  * `clone` **(State Mutators)** (Impact: 3.9)
  * `clone` **(State Mutators)** (Impact: 3.8)
  * `clone` **(State Mutators)** (Impact: 3.8)
  * `clone` **(State Mutators)** (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 182`, `args: 177`, `func_start: 177`
* *Risk/State:* `high_risk_execution: 2`, `duplicate_logic: 5`
* *Architecture:* None
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.868)
- **Top Global Matches:** file_cluster_4: 7.868, file_cluster_6: 11.184, file_cluster_0: 12.219
- **Magnitude:** 399.62 | **LOC:** 966 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **35**; blast radius 15.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.0%), Guard Balance (formerly Safety Score) (49.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%)
- **Documentation Coverage:** 82.7586% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 49.7)
  * `parse_helper` **(Compute Cores)** (Impact: 34.4)
  * `qpath` **(Stateful Encapsulated Methods)** (Impact: 33.7)
  * `parse_mod_style` **(Compute Cores)** (Impact: 24.2)
    * *Intent:* /// struct SingleUse { /// use_token: Token![use], /// path: Path, /// } /// /// impl Parse for Sing...
  * `do_parse` **(Stateful Encapsulated Methods)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 177`, `args: 52`, `func_start: 41`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 6`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 58`, `import: 33`
* *Defense:* `safety: 13`, `doc: 123`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.952
  * `Choke Point (Betweenness):` 0.008146 | `Ripple Effect (Closeness):` 0.213342
  * `Imports (Out-Degree: 14):` alloc::boxed::Box, alloc::vec::Vec, core::cmp, crate::error::Result, crate::expr::Expr, crate::expr::ExprBlock, crate::expr::ExprPath, crate::ext::IdentExt...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/punctuated.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.316)
- **Top Global Matches:** file_cluster_0: 6.316, file_cluster_15: 10.702, file_cluster_13: 10.728
- **Magnitude:** 391.36 | **LOC:** 1171 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **24**; blast radius 19.342; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.4%), Guard Balance (formerly Safety Score) (49.7%)
- **Documentation Coverage:** 49.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_terminated_with` **(Generic / Templated Code)** (Impact: 15.2)
    * *Intent:* /// Parses zero or more occurrences of `T` using the given parse function, /// separated by punctuat...
  * `parse_separated_nonempty_with` **(Generic / Templated Code)** (Impact: 11.5)
    * *Intent:* /// Parses one or more occurrences of `T` using the given parse function, /// separated by punctuati...
  * `fold` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `get_mut` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* /// Mutably borrows the element at the given index.
  * `get` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* /// Borrows the element at the given index.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 224`, `args: 117`, `func_start: 94`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 18`, `duplicate_logic: 26`
* *Architecture:* `api: 49`, `import: 16`
* *Defense:* `safety: 9`, `doc: 182`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.342
  * `Choke Point (Betweenness):` 0.004893 | `Ripple Effect (Closeness):` 0.28894
  * `Imports (Out-Degree: 4):` alloc::boxed::Box, alloc::collections::VecDeque, alloc::vec, alloc::vec::Vec, core::fmt, core::fmt::Debug, core::hash::Hash, core::hash::Hasher...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/fixup.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.619)
- **Top Global Matches:** file_cluster_4: 8.619, file_cluster_6: 9.014, file_cluster_13: 15.043
- **Magnitude:** 351.7 | **LOC:** 774 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 3.332; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (40.5%), Dead Code Surface (formerly Dead Code) (20.9%), Debt Markers (formerly Tech Debt) (16.2%)
- **Documentation Coverage:** 42.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scan_right` **(Many-Argument Workhorses)** (Impact: 212.5)
  * `parenthesize` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* /// Determine whether parentheses are needed around the given expression to /// head off the early t...
  * `precedence` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /// Determines the effective precedence of a subexpression. Some expressions /// have higher or lowe...
  * `rightmost_subexpression_precedence` **(Defensive Guards)** (Impact: 13.3)
  * `leftmost_subexpression_precedence` **(Defensive Guards)** (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 65`, `args: 45`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `dead_code: 11`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 12`, `doc: 40`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.332
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.18041
  * `Imports (Out-Degree: 4):` crate::classify, crate::expr::Expr, crate::expr::ExprBreak, crate::expr::ExprRange, crate::expr::ExprRawAddr, crate::expr::ExprReference, crate::expr::ExprReturn, crate::expr::ExprUnary...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/token.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.435)
- **Top Global Matches:** file_cluster_0: 6.435, file_cluster_13: 8.544, file_cluster_15: 9.262
- **Magnitude:** 343.74 | **LOC:** 1095 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **30**; blast radius 42.987; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (91.9%), Connectivity (formerly Api Exposure) (76.4%), Guard Balance (formerly Safety Score) (47.5%), Mutation Surface (formerly State Flux) (16.6%)
- **Documentation Coverage:** 83.5616% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `punct_helper` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `peek_punct` **(Defensive Guards)** (Impact: 20.0)
  * `parse` **(Defensive Guards)** (Impact: 7.8)
  * `keyword` **(Stateful Encapsulated Methods)** (Impact: 5.7)
  * `peek_keyword` **(Stateful Encapsulated Methods)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 292`, `args: 66`, `func_start: 61`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `duplicate_logic: 16`
* *Architecture:* `api: 142`, `concurrency: 4`, `import: 27`
* *Defense:* `safety: 8`, `doc: 242`, `test: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.987
  * `Choke Point (Betweenness):` 0.004936 | `Ripple Effect (Closeness):` 0.313456
  * `Imports (Out-Degree: 6):` alloc::format, core::cmp, core::fmt, core::fmt::Debug, core::hash::Hash, core::hash::Hasher, core::ops::Deref, core::ops::DerefMut...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `codegen/src/parse.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.885)
- **Top Global Matches:** file_cluster_5: 8.885, file_cluster_12: 8.928, file_cluster_4: 9.238
- **Magnitude:** 339.12 | **LOC:** 672 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **45**; blast radius 2.326; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Connectivity (formerly Api Exposure) (54.4%), Mutation Surface (formerly State Flux) (50.8%)
- **Documentation Coverage:** 94.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_load_file` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `parse_features` **(Compute Cores)** (Impact: 18.3)
  * `introspect_type` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `ast_enum_of_structs` **(Compute Cores)** (Impact: 14.5)
  * `load_token_file` **(Defensive Guards)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 142`, `args: 42`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 12`, `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 15`, `import: 18`
* *Defense:* `safety: 7`, `doc: 2`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.326
  * `Choke Point (Betweenness):` 0.009281 | `Ripple Effect (Closeness):` 0.022886
  * `Imports (Out-Degree: 18):` anyhow::Result, anyhow::bail, crate::version, crate::workspace_path, indexmap::IndexMap, proc_macro2::TokenStream, quote::quote, self::AstItem...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_precedence.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.047)
- **Top Global Matches:** file_cluster_4: 7.047, file_cluster_15: 8.292, file_cluster_0: 9.06
- **Magnitude:** 281.58 | **LOC:** 557 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **71**; blast radius 2.181; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.8%), Complexity Load (formerly Cognitive Load) (6.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.6%)
- **Documentation Coverage:** 97.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `librustc_parenthesize` **(Compute Cores)** (Impact: 37.3)
  * `test_expressions` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `syn_parenthesize` **(Compute Cores)** (Impact: 21.7)
  * `make_parens_invisible` **(Defensive Guards)** (Impact: 9.0)
  * `flat_map_assoc_item` **(Generic / Templated Code)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 137`, `args: 42`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 12`, `duplicate_logic: 2`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `import: 27`
* *Defense:* `safety: 8`, `doc: 1`, `test: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` scan_expr.rs, common, macros, repo, crate::common::eq::SpanlessEq, crate::common::parse, quote::ToTokens, rustc_ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/stmt.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.667)
- **Top Global Matches:** file_cluster_6: 7.667, file_cluster_4: 12.565, file_cluster_8: 14.488
- **Magnitude:** 271.2 | **LOC:** 489 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **31**; blast radius 6.297; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.8%), Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (36.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_stmt` **(Compute Cores)** (Impact: 103.8)
  * `stmt_local` **(Compute Cores)** (Impact: 33.7)
  * `stmt_expr` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `parse_within` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /// Ok(MiniFunction { /// attrs: { /// let mut attrs = outer_attrs; /// attrs.extend(inner_attrs); /...
  * `to_tokens` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 112`, `args: 60`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `state_mutation: 6`, `dead_code: 3`
* *Architecture:* `api: 22`, `concurrency: 3`, `import: 32`
* *Defense:* `safety: 5`, `doc: 71`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.297
  * `Choke Point (Betweenness):` 0.020308 | `Ripple Effect (Closeness):` 0.199119
  * `Imports (Out-Degree: 13):` alloc::boxed::Box, alloc::vec::Vec, crate::attr::Attribute, crate::classify, crate::error::Result, crate::expr, crate::expr::Expr, crate::expr::ExprBlock...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `tests/repo/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.445)
- **Top Global Matches:** file_cluster_9: 8.445, file_cluster_12: 9.496, file_cluster_15: 10.588
- **Magnitude:** 240.8 | **LOC:** 631 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 4.416; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (57.9%), Connectivity (formerly Api Exposure) (36.8%), Complexity Load (formerly Cognitive Load) (36.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `download_and_unpack` **(Compute Cores)** (Impact: 15.4)
  * `for_each_rust_file` **(Compute Cores)** (Impact: 14.3)
  * `clone_rust` **(I/O & Config Routines)** (Impact: 14.2)
  * `base_dir_filter` **(Defensive Guards)** (Impact: 12.6)
  * `edition` **(Generic / Templated Code)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 191`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 5`, `state_mutation: 11`, `planned_debt: 24`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 124`, `import: 12`
* *Defense:* `safety: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.416
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.034965
  * `Imports (Out-Degree: 1):` progress, anyhow::Result, flate2::read::GzDecoder, rayon::ThreadPoolBuilder, rayon::iter::IntoParallelRefIterator, rayon::iter::ParallelIterator, self::progress::Progress, std::collections::BTreeSet...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `codegen/src/snapshot.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.943)
- **Top Global Matches:** file_cluster_4: 5.943, file_cluster_15: 10.626, file_cluster_6: 11.01
- **Magnitude:** 220.18 | **LOC:** 374 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 2.326; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (23.9%), Connectivity (formerly Api Exposure) (18.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand_impl_body` **(Many-Argument Workhorses)** (Impact: 118.1)
  * `format_field` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `syntax_tree_enum` **(Generic / Templated Code)** (Impact: 11.0)
  * `fmt` **(Defensive Guards)** (Impact: 9.2)
  * `expand_impl` **(Generic / Templated Code)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 88`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.326
  * `Choke Point (Betweenness):` 0.000251 | `Ripple Effect (Closeness):` 0.019425
  * `Imports (Out-Degree: 6):` anyhow::Result, core::fmt, core::fmt::Debug, core::fmt::Display, crate::file, crate::lookup, crate::operand::Borrowed, crate::operand::Operand...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/attr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.489)
- **Top Global Matches:** file_cluster_5: 7.489, file_cluster_0: 7.539, file_cluster_12: 8.757
- **Magnitude:** 211.64 | **LOC:** 842 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **31**; blast radius 11.161; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.7%), Connectivity (formerly Api Exposure) (51.2%), Guard Balance (formerly Safety Score) (43.1%)
- **Documentation Coverage:** 52.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_meta_name_value_after_path` **(Defensive Guards)** (Impact: 16.6)
  * `parse_meta_after_path` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `fmt` **(Compute Cores)** (Impact: 10.8)
  * `parse_inner` **(Stateful Encapsulated Methods)** (Impact: 7.2)
  * `single_parse_inner` **(Stateful Encapsulated Methods)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 88`, `args: 39`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 38`, `import: 29`
* *Defense:* `safety: 2`, `doc: 395`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.161
  * `Choke Point (Betweenness):` 0.00593 | `Ripple Effect (Closeness):` 0.216783
  * `Imports (Out-Degree: 8):` alloc::format, alloc::vec::Vec, core::fmt, core::fmt::Display, core::iter, core::slice, crate::attr::AttrStyle, crate::attr::Attribute...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/parse.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.125)
- **Top Global Matches:** file_cluster_0: 6.125, file_cluster_5: 10.399, file_cluster_15: 10.407
- **Magnitude:** 197.24 | **LOC:** 1421 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **34**; blast radius 77.266; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (55.7%), Connectivity (formerly Api Exposure) (54.5%), Guard Balance (formerly Safety Score) (28.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__parse_scoped` **(Defensive Guards)** (Impact: 10.8)
  * `span_of_unexpected_ignoring_nones` **(Defensive Guards)** (Impact: 9.3)
  * `parse2` **(Defensive Guards)** (Impact: 9.3)
  * `step` **(Generic / Templated Code)** (Impact: 6.6)
    * *Intent:* /// # /// # fn remainder_after_skipping_past_next_at( /// # input: ParseStream, /// # ) -> Result<pr...
  * `parse` **(Generic / Templated Code)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 105`, `args: 58`, `func_start: 53`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 34`, `import: 19`
* *Defense:* `safety: 13`, `doc: 894`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 77.266
  * `Choke Point (Betweenness):` 0.011148 | `Ripple Effect (Closeness):` 0.354248
  * `Imports (Out-Degree: 6):` discouraged.rs, alloc::boxed::Box, alloc::rc::Rc, core::cell::Cell, core::fmt, core::fmt::Debug, core::fmt::Display, core::hash::Hash...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/buffer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.989)
- **Top Global Matches:** file_cluster_0: 5.989, file_cluster_16: 8.474, file_cluster_15: 8.805
- **Magnitude:** 178.8 | **LOC:** 438 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **17**; blast radius 55.6; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Connectivity (formerly Api Exposure) (46.2%)
- **Documentation Coverage:** 32.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `skip` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* /// Skip over the next token that is not a None-delimited group, without /// cloning it. Returns `No...
  * `group` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* /// If the cursor is pointing at a `Group` with the given delimiter, returns /// a cursor into that ...
  * `create` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /// This create method intelligently exits non-explicitly-entered /// `None`-delimited scopes when t...
  * `lifetime` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* /// If the cursor is pointing at a `Lifetime`, returns it along with a /// cursor pointing at the ne...
  * `ignore_none` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /// While the cursor is looking at a `None`-delimited group, move it to look /// at the first token ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 72`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `api: 25`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 7`, `doc: 68`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.6
  * `Choke Point (Betweenness):` 0.000713 | `Ripple Effect (Closeness):` 0.251069
  * `Imports (Out-Degree: 2):` alloc::boxed::Box, alloc::vec::Vec, core::cmp::Ordering, core::marker::PhantomData, core::ptr, crate::Lifetime, crate::ext::TokenStreamExt, proc_macro2::Delimiter...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/common/eq.rs` (RUST) | Magnitude: 176.28 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 425, structural_boundaries: 239, import: 186, branch: 78
- `src/lib.rs` (RUST) | Magnitude: 82.0 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 619, indent_spaces: 131, decorators: 121, structural_boundaries: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `fuzz/fuzz_targets/create_token_buffer.rs` (RUST) | Magnitude: 1.9 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, import: 4, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/custom_keyword.rs` (RUST) | Magnitude: 34.12 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 103, doc: 97, decorators: 30, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/precedence.rs` (RUST) | Magnitude: 38.02 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 154, args: 40, structural_boundaries: 16, decorators: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/ci.yml` (YAML) | Magnitude: 57.34 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 177, func_start: 37, structural_boundaries: 34, import: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `codegen/src/parse.rs` (RUST) | Magnitude: 339.12 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 511, structural_boundaries: 142, branch: 131, core_var_decl: 84
- `src/attr.rs` (RUST) | Magnitude: 211.64 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 395, indent_spaces: 352, structural_boundaries: 88, branch: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `benches/file.rs` (RUST) | Magnitude: 16.16 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, decorators: 10, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `codegen/src/clone.rs` (RUST) | Magnitude: 72.04 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 34, branch: 25, core_var_decl: 21

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/gen/fold.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 1169.06
- `src/gen/eq.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 991.6
- `src/gen/debug.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 806.6
- `src/ty.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 685.9
- `src/gen/hash.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 513.5

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/lib.rs` -> **Severity: 2.219** (Bridge: 0.0525 * Flux: 42.3005%)
- `src/expr.rs` -> **Severity: 1.066** (Bridge: 0.0368 * Flux: 28.9385%)
- `src/item.rs` -> **Severity: 0.739** (Bridge: 0.0303 * Flux: 24.39%)
- `src/stmt.rs` -> **Severity: 0.739** (Bridge: 0.0203 * Flux: 36.4035%)
- `tests/common/visit.rs` -> **Severity: 0.737** (Bridge: 0.0074 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/error.rs` -> **Severity: 15.428** (Embedded: 0.3567 * Error Risk: 43.2518%)
- `src/lifetime.rs` -> **Severity: 14.884** (Embedded: 0.2639 * Error Risk: 56.404%)
- `src/token.rs` -> **Severity: 14.875** (Embedded: 0.3135 * Error Risk: 47.4541%)
- `src/punctuated.rs` -> **Severity: 14.374** (Embedded: 0.2889 * Error Risk: 49.7465%)
- `src/buffer.rs` -> **Severity: 13.257** (Embedded: 0.2511 * Error Risk: 52.8035%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ext.rs` -> **Severity: 6199.694** (Blast Radius: 80.596 * Doc Risk: 76.9231%)
- `src/error.rs` -> **Severity: 5126.319** (Blast Radius: 86.338 * Doc Risk: 59.375%)
- `src/parse.rs` -> **Severity: 3863.3** (Blast Radius: 77.266 * Doc Risk: 50.0%)
- `src/token.rs` -> **Severity: 3592.062** (Blast Radius: 42.987 * Doc Risk: 83.5616%)
- `src/lookahead.rs` -> **Severity: 3054.43** (Blast Radius: 42.762 * Doc Risk: 71.4286%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 29 literal sites + 2 sites through wrappers = 31

- `validate` (function, debug_prints, primitive): 2 call sites in 1 files -- `examples/lazy-static/example/src/main.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9629 call pairs -- scoped 37.0%, unique 0.0%, ambiguous 5.3%, external 57.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 9627 | 37.1% | 0.0% | 5.3% | 57.6% |
| shell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
