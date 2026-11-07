# ARCHITECTURAL_BRIEF: ripgrep
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/BurntSushi/ripgrep` |
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
- **Scope:** 161 analyzed artifact(s), 41900 LOC.
- **Load-bearing artifact:** `crates/matcher/src/lib.rs` -- 18 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/printer/src/standard.rs` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/core/flags/defs.rs` at magnitude 1289.82 (structural weight, not risk).
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
| Total Artifacts | 220 |
| Analyzed Artifacts (Scanned) | 161 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 59 |
| Total LOC | 41900 |
| Volatility Index | 0.019 |
| % Scanned of codebase = | 73.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6858 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2154 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0687 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 100 | 37566 | 62.1% |
| MARKDOWN | 21 | 0 | 13.0% |
| PLAINTEXT | 15 | 0 | 9.3% |
| CSV | 9 | 2283 | 5.6% |
| SHELL | 7 | 590 | 4.3% |
| YAML | 5 | 612 | 3.1% |
| PYTHON | 2 | 830 | 1.2% |
| RUBY | 1 | 19 | 0.6% |
| XML | 1 | 0 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 161 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Large Core Modules (3) 14%, Declarative / Non-Code 12%, Encapsulated Accessors Files 9%, State Mutators Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 125 | 77.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36 | 22.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 59*

**Composition by Extension & Reason:**
- `no_extension`: 12x Unresolved Ambiguity (No Retainable Structure), 11x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 11x Unsupported Format (.toml), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1612 LOC), 1x Excluded (Embedded Array/Matrix Payload: 5642 commas in 807 LOC), 1x Excluded (Embedded Array/Matrix Payload: 4697 commas in 672 LOC)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.setup`: 2x Excluded (Unsupported Extension: '.SETUP')
- `.help`: 2x Excluded (Unsupported Extension: '.help')
- `.gitignore`: 2x Excluded (Unsupported Extension: '.gitignore')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2134 LOC)
- `.z`: 1x Excluded (Unsupported Extension: '.Z')
- `.br`: 1x Excluded (Unsupported Extension: '.br')
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.lz4`: 1x Excluded (Unsupported Extension: '.lz4')
- `.lzma`: 1x Excluded (Unsupported Extension: '.lzma')
- `.xz`: 1x Excluded (Explicitly Denied Extension: '.xz')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.3 | 8.8 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.6 | 37.7 | 49.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.7 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 73.3 | 20.8 | 11.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.1 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.9 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.5 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 33.9 | 19.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 143 | 29 | 2 | `crates/printer/src/standard.rs` |
| cleanup | 11 | 8 | 0 | `crates/cli/src/process.rs` |
| guards | 912 | 82 | 17 | `crates/core/flags/lowargs.rs` |
| danger | 1372 | 71 | 15 | `crates/core/flags/defs.rs` |
| concurrency | 109 | 22 | 1 | `crates/ignore/src/walk.rs` |
| connectivity | 1470 | 84 | 32 | `crates/core/flags/lowargs.rs` |
| io | 200 | 34 | 4 | `crates/core/flags/complete/rg.zsh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 7 | 0 | `benchsuite/benchsuite` |
| time | 10 | 5 | 0 | `crates/core/main.rs` |
| serialization | 6 | 1 | 0 | `crates/globset/src/serde_impl.rs` |
| regex | 9 | 5 | 0 | `scripts/copy-examples` |
| events | 80 | 25 | 1 | `crates/core/flags/hiargs.rs` |
| tests | 2467 | 57 | 29 | `crates/core/flags/defs.rs` |
| docs | 7335 | 80 | 157 | `crates/matcher/src/lib.rs` |
| debt | 265 | 40 | 3 | `crates/core/flags/defs.rs` |
| mutation | 4892 | 96 | 72 | `crates/core/flags/defs.rs` |
| dead_code | 140 | 19 | 1 | `benchsuite/benchsuite` |
| credential | 3 | 3 | 0 | `.github/workflows/ci.yml` |
| threat | 6 | 2 | 0 | `tests/feature.rs` |
| ml_ai | 9 | 3 | 0 | `crates/core/flags/parse.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0259**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/core/flags/complete/rg.zsh` (Hits: 34)
- `ci/test-complete` (Hits: 27)
- `benchsuite/benchsuite` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`crates/matcher/src/lib.rs`) — 18 inbound connections
2. **mod.rs** (`crates/searcher/src/searcher/mod.rs`) — 14 inbound connections
3. **sink.rs** (`crates/searcher/src/sink.rs`) — 10 inbound connections
4. **mod.rs** (`crates/core/flags/mod.rs`) — 8 inbound connections
5. **glob.rs** (`crates/globset/src/glob.rs`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **standard.rs** (`crates/printer/src/standard.rs`) — 42 outbound dependencies
2. **walk.rs** (`crates/ignore/src/walk.rs`) — 39 outbound dependencies
3. **defs.rs** (`crates/core/flags/defs.rs`) — 38 outbound dependencies
4. **lib.rs** (`crates/cli/src/lib.rs`) — 36 outbound dependencies
5. **hiargs.rs** (`crates/core/flags/hiargs.rs`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `doc_long` **(Many-Argument Workhorses)** (@ `crates/core/flags/defs.rs`) -> Impact: **443.6** | LOC: 5252
- `_rg` **(I/O & Config Routines)** (@ `crates/core/flags/complete/rg.zsh`) -> Impact: **96.8** | LOC: 396
  * *Intent:* #compdef rg ## # zsh completion function for ripgrep # # Run ci/test-complete after building to ensure that the options supported by # this function s...
- `from_low_args` **(Compute Cores)** (@ `crates/core/flags/hiargs.rs`) -> Impact: **77.0** | LOC: 210
  * *Intent:* /// Convert low level arguments into high level arguments. /// /// This process can fail for a variety of reasons. For example, invalid /// globs or s...
- `matched_ignore` **(Many-Argument Workhorses)** (@ `crates/ignore/src/dir.rs`) -> Impact: **66.3** | LOC: 126
  * *Intent:* /// Performs matching only on the ignore files for this directory and /// all parent directories.
- `write_exceeded_line` **(Many-Argument Workhorses)** (@ `crates/printer/src/standard.rs`) -> Impact: **64.4** | LOC: 63
- `write_colored_matches` **(Many-Argument Workhorses)** (@ `crates/printer/src/standard.rs`) -> Impact: **51.1** | LOC: 42
  * *Intent:* /// Write the `line` portion of `bytes`, with appropriate coloring for /// each `match`, starting at `match_index`. /// /// This accounts for trimming...
- `generate_work` **(Many-Argument Workhorses)** (@ `crates/ignore/src/walk.rs`) -> Impact: **50.1** | LOC: 71
  * *Intent:* /// Decides whether to submit the given directory entry as a file to /// search. /// /// If the entry is a path that should be ignored, then this is a...
- `parse` **(Many-Argument Workhorses)** (@ `crates/core/flags/parse.rs`) -> Impact: **49.5** | LOC: 70
  * *Intent:* /// Parse the given CLI arguments into a low level representation. /// /// The iterator given should *not* start with the binary name.
- `parse_star` **(Defensive Guards)** (@ `crates/globset/src/glob.rs`) -> Impact: **44.0** | LOC: 60
- `match_by_line_fast` **(Compute Cores)** (@ `crates/searcher/src/searcher/core.rs`) -> Impact: **43.7** | LOC: 43

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/printer/src` | 11 | 2397.94 | 6.69% | 11.59% |
| `crates/core/flags` | 6 | 2231.8 | 5.91% | 32.43% |
| `crates/ignore/src` | 8 | 2101.1 | 7.53% | 14.79% |
| `crates/searcher/src/searcher` | 4 | 1156.44 | 11.12% | 17.63% |
| `crates/globset/src` | 5 | 1045.66 | 8.82% | 9.3% |
| `crates/regex/src` | 9 | 922.94 | 7.59% | 5.9% |
| `crates/searcher/src` | 6 | 884.3 | 6.87% | 16.67% |
| `benchsuite` | 1 | 661.84 | 42.68% | 99.97% |
| `crates/core` | 6 | 458.16 | 7.08% | 4.7% |
| `crates/matcher/src` | 2 | 449.36 | 8.49% | 90.13% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/core/flags/mod.rs` -> **100.0%** Exposure
- `crates/searcher/src/sink.rs` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.9997%** Exposure
- `benchsuite/benchsuite` -> **99.9656%** Exposure
- `crates/matcher/src/interpolate.rs` -> **99.8857%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/copy-examples` -> **100.0%** Exposure
- `crates/core/flags/complete/bash.rs` -> **100.0%** Exposure
- `crates/core/flags/complete/fish.rs` -> **100.0%** Exposure
- `benchsuite/benchsuite` -> **99.999%** Exposure
- `ci/test-complete` -> **99.9988%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/core/flags/defs.rs` -> **0** Orphaned Functions | **62** Duplicates
- `benchsuite/benchsuite` -> **28** Orphaned Functions | **11** Duplicates
- `crates/searcher/src/sink.rs` -> **0** Orphaned Functions | **18** Duplicates
- `crates/ignore/src/lib.rs` -> **17** Orphaned Functions | **0** Duplicates
- `crates/core/flags/mod.rs` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `954` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/core/flags/defs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.565)
- **Top Global Matches:** file_cluster_5: 10.565, file_cluster_12: 12.777, file_cluster_7: 12.95
- **Magnitude:** 1289.82 | **LOC:** 7780 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 3.582; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (72.8%), Guard Balance (formerly Safety Score) (69.9%), Connectivity (formerly Api Exposure) (38.0%)
- **Documentation Coverage:** 89.2989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doc_long` **(Many-Argument Workhorses)** (Impact: 443.6)
  * `update` **(Compute Cores)** (Impact: 10.9)
  * `update` **(Compute Cores)** (Impact: 6.6)
  * `update` **(Compute Cores)** (Impact: 6.6)
  * `update` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 1131`, `args: 900`, `func_start: 878`, `class_start: 104`
* *Risk/State:* `safety_bypasses: 535`, `high_risk_execution: 3`, `state_mutation: 124`, `fragile_debt: 1`, `duplicate_logic: 62`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 62`
* *Defense:* `safety: 2`, `doc: 109`, `test: 857`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.582
  * `Choke Point (Betweenness):` 0.000987 | `Ripple Effect (Closeness):` 0.027685
  * `Imports (Out-Degree: 4):` anyhow::Context, bstr::BString, bstr::ByteVec, crate::flags::Category, crate::flags::Flag, crate::flags::FlagValue, crate::flags::lowargs::BinaryMode, crate::flags::lowargs::BoundaryMode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/printer/src/standard.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.498)
- **Top Global Matches:** file_cluster_5: 7.498, file_cluster_12: 8.043, file_cluster_7: 9.001
- **Magnitude:** 1138.9 | **LOC:** 3988 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **42**; blast radius 3.53; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (57.5%), Mutation Surface (formerly State Flux) (34.9%)
- **Documentation Coverage:** 63.8783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_exceeded_line` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `write_colored_matches` **(Many-Argument Workhorses)** (Impact: 51.1)
    * *Intent:* /// Write the `line` portion of `bytes`, with appropriate coloring for /// each `match`, starting at...
  * `sink_slow_multi_per_match` **(Compute Cores)** (Impact: 35.3)
  * `sink_slow_multi_line_only_matching` **(Compute Cores)** (Impact: 25.1)
  * `write_binary_message` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 759`, `args: 184`, `func_start: 170`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 177`, `state_mutation: 68`, `fragile_debt: 4`
* *Architecture:* `api: 96`, `import: 11`
* *Defense:* `safety: 20`, `doc: 419`, `test: 102`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.53
  * `Choke Point (Betweenness):` 0.000524 | `Ripple Effect (Closeness):` 0.041292
  * `Imports (Out-Degree: 10):` bstr::ByteSlice, crate::color::ColorSpecs, crate::counter::CounterWriter, crate::hyperlink, crate::hyperlink::HyperlinkConfig, crate::stats::Stats, crate::util::DecimalFormatter, crate::util::PrinterPath...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/ignore/src/walk.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.863)
- **Top Global Matches:** file_cluster_0: 7.863, file_cluster_12: 7.893, file_cluster_5: 8.063
- **Magnitude:** 855.1 | **LOC:** 2495 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **39**; blast radius 25.797; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (62.0%), Connectivity (formerly Api Exposure) (58.3%), Guard Balance (formerly Safety Score) (51.3%)
- **Documentation Coverage:** 41.8367% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_work` **(Many-Argument Workhorses)** (Impact: 50.1)
    * *Intent:* /// Decides whether to submit the given directory entry as a file to /// search. /// /// If the entr...
  * `run_one` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `visit` **(Compute Cores)** (Impact: 29.8)
    * *Intent:* /// The builder given is used to construct a visitor for every thread /// used by this traversal. Th...
  * `next` **(Compute Cores)** (Impact: 24.6)
  * `skip_entry` **(Defensive Guards)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 386`, `args: 192`, `func_start: 145`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 57`
* *Architecture:* `io: 6`, `api: 58`, `concurrency: 18`, `import: 25`
* *Defense:* `safety: 33`, `doc: 477`, `test: 25`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.797
  * `Choke Point (Betweenness):` 0.001167 | `Ripple Effect (Closeness):` 0.038547
  * `Imports (Out-Degree: 5):` crate::Error, crate::PartialErrorBuilder, crate::dir::Ignore, crate::dir::IgnoreBuilder, crate::gitignore::GitignoreBuilder, crate::overrides::Override, crate::tests::TempDir, crate::types::Types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `benchsuite/benchsuite` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.522)
- **Top Global Matches:** file_cluster_15: 6.522, file_cluster_12: 7.611, file_cluster_16: 8.65
- **Magnitude:** 661.84 | **LOC:** 1314 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.79; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 41.7323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 39.2)
  * `collect_benchmarks` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `download` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* ''' Download choices into suite_dir. Specifically, choices specifies a list of corpora to fetch. :pa...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `run` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* ''' Runs this benchmark and returns the results. :rtype: Result :raises: MissingCommands if any comm...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 159`, `args: 70`, `func_start: 67`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 6`, `state_mutation: 154`, `planned_debt: 1`, `duplicate_logic: 11`, `unreferenced_by_name: 28`
* *Architecture:* `io: 22`, `api: 65`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 7`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.79
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, csv, multiprocessing, os, os.path, re, shutil, statistics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/globset/src/glob.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.594)
- **Top Global Matches:** file_cluster_12: 8.594, file_cluster_5: 8.775, file_cluster_0: 8.9
- **Magnitude:** 600.3 | **LOC:** 1687 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **13**; blast radius 25.309; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Connectivity (formerly Api Exposure) (44.8%)
- **Documentation Coverage:** 42.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_star` **(Defensive Guards)** (Impact: 44.0)
  * `tokens_to_regex` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `parse_class` **(Compute Cores)** (Impact: 35.7)
  * `suffix` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /// Returns a literal suffix of this pattern if the entire pattern matches /// if the literal suffix...
  * `ext` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* /// Returns an extension if this pattern matches a file path if and only /// if the file path has th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 225`, `args: 62`, `func_start: 59`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 61`, `fragile_debt: 1`
* *Architecture:* `api: 23`, `import: 7`
* *Defense:* `safety: 34`, `doc: 186`, `test: 29`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.309
  * `Choke Point (Betweenness):` 0.000136 | `Ripple Effect (Closeness):` 0.063314
  * `Imports (Out-Degree: 1):` crate::Candidate, crate::Error, crate::ErrorKind, crate::GlobSetBuilder, crate::new_regex, regex_automata::meta::Regex, self::Glob, self::GlobBuilder...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/core/flags/hiargs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.784)
- **Top Global Matches:** file_cluster_16: 7.784, file_cluster_0: 8.233, file_cluster_4: 8.561
- **Magnitude:** 488.34 | **LOC:** 1481 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **36**; blast radius 5.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.7%), Mutation Surface (formerly State Flux) (34.4%), Connectivity (formerly Api Exposure) (24.1%)
- **Documentation Coverage:** 1.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_low_args` **(Compute Cores)** (Impact: 77.0)
    * *Intent:* /// Convert low level arguments into high level arguments. /// /// This process can fail for a varie...
  * `from_low_args` **(Compute Cores)** (Impact: 26.0)
    * *Intent:* /// Pulls the patterns out of the low arguments. /// /// This includes collecting patterns from -e/-...
  * `from_low_args` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* /// Drain the search paths out of the given low arguments.
  * `matcher_rust` **(Defensive Guards)** (Impact: 21.1)
    * *Intent:* /// Build a matcher using Rust's regex engine. /// /// If there was a problem building the matcher (...
  * `walk_builder` **(Stateful Encapsulated Methods)** (Impact: 17.8)
    * *Intent:* /// Create a new builder for recursive directory traversal. /// /// The builder returned can be used...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 205`, `args: 68`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 19`
* *Architecture:* `io: 4`, `api: 21`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 19`, `doc: 249`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.154
  * `Choke Point (Betweenness):` 0.009306 | `Ripple Effect (Closeness):` 0.033499
  * `Imports (Out-Degree: 6):` bstr::BString, crate::flags::lowargs::BinaryMode, crate::flags::lowargs::BoundaryMode, crate::flags::lowargs::BufferMode, crate::flags::lowargs::CaseMode, crate::flags::lowargs::ColorChoice, crate::flags::lowargs::ContextMode, crate::flags::lowargs::ContextSeparator...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/ignore/src/dir.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.127)
- **Top Global Matches:** file_cluster_4: 9.127, file_cluster_5: 9.441, file_cluster_0: 9.534
- **Magnitude:** 462.28 | **LOC:** 1306 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 9.706; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.3%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (37.5%)
- **Documentation Coverage:** 45.1923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matched_ignore` **(Many-Argument Workhorses)** (Impact: 66.3)
    * *Intent:* /// Performs matching only on the ignore files for this directory and /// all parent directories.
  * `add_child_path` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* /// Like add_child, but takes a full path and returns an IgnoreInner.
  * `add_parents` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* /// Create a new `Ignore` matcher with the parent directories of `dir`. /// /// Note that this can o...
  * `matched` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* /// Returns a match indicating whether the given file path should be /// ignored or not. /// /// The...
  * `resolve_git_commondir` **(Defensive Guards)** (Impact: 21.3)
    * *Intent:* /// Find the GIT_COMMON_DIR for the given git worktree. /// /// This is the directory that may conta...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 206`, `args: 80`, `func_start: 62`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 36`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 46`, `import: 4`
* *Defense:* `safety: 13`, `doc: 191`, `test: 98`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.706
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.037026
  * `Imports (Out-Degree: 6):` crate::Error, crate::Match, crate::PartialErrorBuilder, crate::dir::IgnoreBuilder, crate::gitignore, crate::gitignore::Gitignore, crate::gitignore::GitignoreBuilder, crate::overrides...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/searcher/src/searcher/core.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.604)
- **Top Global Matches:** file_cluster_4: 5.604, file_cluster_16: 9.097, file_cluster_9: 9.928
- **Magnitude:** 434.22 | **LOC:** 714 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 3.844; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (75.4%), Guard Balance (formerly Safety Score) (51.7%), Connectivity (formerly Api Exposure) (25.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_by_line_fast` **(Compute Cores)** (Impact: 43.7)
  * `match_by_line_slow` **(Compute Cores)** (Impact: 40.8)
  * `after_context_by_line` **(Stateful Encapsulated Methods)** (Impact: 27.7)
  * `match_by_line_fast_invert` **(Compute Cores)** (Impact: 23.0)
  * `before_context_by_line` **(Stateful Encapsulated Methods)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 146`, `args: 34`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `fragile_debt: 2`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 12`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.844
  * `Choke Point (Betweenness):` 0.0001 | `Ripple Effect (Closeness):` 0.064712
  * `Imports (Out-Degree: 5):` FastMatchResult::*, bstr::ByteSlice, crate::line_buffer::BinaryDetection, crate::lines, crate::lines::LineStep, crate::searcher::Config, crate::searcher::Range, crate::searcher::Searcher...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/searcher/src/searcher/glue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.304)
- **Top Global Matches:** file_cluster_12: 7.304, file_cluster_13: 8.407, file_cluster_15: 8.492
- **Magnitude:** 390.14 | **LOC:** 1550 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 5.944; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Connectivity (formerly Api Exposure) (49.9%), Mutation Surface (formerly State Flux) (47.0%), Debt Markers (formerly Tech Debt) (17.1%)
- **Documentation Coverage:** 98.9691% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Stateful Encapsulated Methods)** (Impact: 27.5)
  * `sink_context` **(Compute Cores)** (Impact: 16.3)
  * `fill` **(Compute Cores)** (Impact: 15.7)
  * `sink` **(Compute Cores)** (Impact: 15.3)
  * `sink_matched_inverted` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 287`, `args: 69`, `func_start: 55`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 30`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 46`, `import: 12`
* *Defense:* `safety: 6`, `doc: 4`, `test: 101`, `sync_locks: 23`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.944
  * `Choke Point (Betweenness):` 0.002029 | `Ripple Effect (Closeness):` 0.064016
  * `Imports (Out-Degree: 8):` crate::SearcherBuilder, crate::line_buffer::DEFAULT_BUFFER_CAPACITY, crate::line_buffer::LineBufferReader, crate::lines, crate::lines::LineStep, crate::searcher::BinaryDetection, crate::searcher::Config, crate::searcher::Range...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/globset/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.526)
- **Top Global Matches:** file_cluster_5: 7.526, file_cluster_0: 8.403, file_cluster_12: 8.514
- **Magnitude:** 370.64 | **LOC:** 1140 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 37.145; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Debt Markers (formerly Tech Debt) (38.1%)
- **Documentation Coverage:** 73.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /// Adds the sequence number of every glob pattern that matches the given /// path to the vec given....
  * `matches_into` **(Defensive Guards)** (Impact: 10.8)
  * `is_match` **(Defensive Guards)** (Impact: 9.5)
  * `is_match_candidate` **(Generic / Templated Code)** (Impact: 7.5)
    * *Intent:* /// Create an empty `GlobSet`. An empty set matches nothing.
  * `matches_candidate_into` **(Generic / Templated Code)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 170`, `args: 76`, `func_start: 69`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 32`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 8`, `doc: 130`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.145
  * `Choke Point (Betweenness):` 0.003332 | `Ripple Effect (Closeness):` 0.062687
  * `Imports (Out-Degree: 4):` fnv, glob, pathutil, serde_impl, aho_corasick::AhoCorasick, bstr::B, bstr::ByteSlice, bstr::ByteVec...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/matcher/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.239)
- **Top Global Matches:** file_cluster_0: 7.239, file_cluster_5: 8.921, file_cluster_13: 9.43
- **Magnitude:** 349.96 | **LOC:** 1380 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **2**; blast radius 48.54; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (80.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.3%), Mutation Surface (formerly State Flux) (46.2%)
- **Documentation Coverage:** 30.6306% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_captures_iter_at` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /// Executes the given function over successive non-overlapping matches /// in `haystack` with captu...
  * `try_find_iter_at` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* /// Executes the given function over successive non-overlapping matches /// in `haystack`. If no mat...
  * `replace_with_captures_at` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Replaces every match in the given haystack with the result of calling /// `append` with the matc...
  * `interpolate` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* /// replaced with the empty string. /// /// The longest possible name is used. e.g., `$1a` looks up ...
  * `fmt` **(Generic / Templated Code)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 132`, `args: 97`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 14`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `io: 2`, `api: 31`, `import: 1`
* *Defense:* `safety: 3`, `doc: 480`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.54
  * `Choke Point (Betweenness):` 0.00153 | `Ripple Effect (Closeness):` 0.133787
  * `Imports (Out-Degree: 1):` interpolate, crate::interpolate::interpolate
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `crates/printer/src/summary.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.673)
- **Top Global Matches:** file_cluster_5: 6.673, file_cluster_12: 7.989, file_cluster_7: 9.231
- **Magnitude:** 331.76 | **LOC:** 1151 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 3.715; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.2%), Guard Balance (formerly Safety Score) (54.4%), Mutation Surface (formerly State Flux) (39.6%)
- **Documentation Coverage:** 45.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finish` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `matched` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `sink_with_path` **(Generic / Templated Code)** (Impact: 13.6)
    * *Intent:* /// Return an implementation of `Sink` associated with a file path. /// /// When the printer is asso...
  * `write_path_line` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* /// If this printer has a file path associated with it, then this will /// write that path to the un...
  * `write_path_field` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* /// If this printer has a file path associated with it, then this will /// write that path to the un...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 188`, `args: 60`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 24`, `fragile_debt: 2`
* *Architecture:* `api: 46`, `import: 10`
* *Defense:* `safety: 5`, `doc: 268`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.715
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.041292
  * `Imports (Out-Degree: 9):` crate::color::ColorSpecs, crate::counter::CounterWriter, crate::hyperlink, crate::hyperlink::HyperlinkConfig, crate::stats::Stats, crate::util::PrinterPath, crate::util::find_iter_at_in_context, grep_matcher::Matcher...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/regex/src/literal.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.843)
- **Top Global Matches:** file_cluster_15: 7.843, file_cluster_0: 7.997, file_cluster_13: 8.184
- **Magnitude:** 323.66 | **LOC:** 1017 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 3.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.3%), Connectivity (formerly Api Exposure) (39.6%), Guard Balance (formerly Safety Score) (38.4%)
- **Documentation Coverage:** 69.5122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `choose` **(Compute Cores)** (Impact: 27.9)
    * *Intent:* /// Compare the two sequences and return the one that is believed to be /// best according to a hodg...
  * `extract_repetition` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* /// best, Some examples: /// /// 'a*' => [inexact(a), exact("")] /// 'a*?' => [exact(""), inexact(a)...
  * `extract_concat` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* /// Extract a sequence from the given concatenation. Sequences from each of /// the child HIR expres...
  * `new` **(Stateful Encapsulated Methods)** (Impact: 10.6)
    * *Intent:* /// Create a set of inner literals from the given HIR expression. /// /// If no line terminator was ...
  * `union` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* /// Union the two sequences if the result would be within configured /// limits. Otherwise, make `se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 145`, `args: 71`, `func_start: 65`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`
* *Architecture:* `api: 18`, `import: 5`
* *Defense:* `safety: 9`, `doc: 107`, `test: 184`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.749
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.056977
  * `Imports (Out-Degree: 2):` crate::config::ConfiguredHIR, crate::error::Error, regex_automata::meta::Regex, regex_syntax::hir, regex_syntax::hir::Hir, regex_syntax::hir::HirKind::*, regex_syntax::hir::literal::Literal, regex_syntax::hir::literal::Seq...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/searcher/src/line_buffer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.542)
- **Top Global Matches:** file_cluster_5: 7.542, file_cluster_12: 9.056, file_cluster_7: 9.339
- **Magnitude:** 305.46 | **LOC:** 966 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 9.336; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (62.6%), Connectivity (formerly Api Exposure) (41.6%), Complexity Load (formerly Cognitive Load) (18.0%)
- **Documentation Coverage:** 49.4382% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /// reader. /// /// Callers should provide the same reader to this line buffer in /// subsequent cal...
  * `replace_bytes` **(Many-Argument Workhorses)** (Impact: 11.3)
    * *Intent:* /// Replaces `src` with `replacement` in bytes, and return the offset of the /// first replacement, ...
  * `ensure_capacity` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* /// Ensures that the internal buffer has a non-zero amount of free space /// in which to read more d...
  * `roll` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /// Roll the unconsumed parts of the buffer to the front. /// /// This operation is idempotent. /// ...
  * `is_quit` **(State Mutators)** (Impact: 3.1)
    * *Intent:* /// Returns true if and only if the detection heuristic demands that /// the line buffer stop read d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 198`, `args: 54`, `func_start: 54`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 76`
* *Architecture:* `io: 1`, `api: 41`, `import: 4`
* *Defense:* `safety: 5`, `doc: 200`, `test: 148`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071948
  * `Imports (Out-Degree: 0):` bstr::ByteSlice, bstr::ByteVec, self::*, std::io
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `crates/searcher/src/searcher/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.718)
- **Top Global Matches:** file_cluster_0: 6.718, file_cluster_15: 7.394, file_cluster_13: 8.079
- **Magnitude:** 304.98 | **LOC:** 1089 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **29**; blast radius 19.482; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.2%), Guard Balance (formerly Safety Score) (45.9%), Debt Markers (formerly Tech Debt) (41.8%)
- **Documentation Coverage:** 6.5217% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill_multi_line_buffer_from_reader` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* /// Fill the buffer for use with multi-line searching from the given /// reader. This reads from the...
  * `search_reader` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /// Execute a search over any implementation of `std::io::Read` and write /// the results to the giv...
  * `search_file_maybe_path` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `search_slice` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* /// Execute a search over the given slice and write the results to the /// given sink.
  * `multi_line_with_matcher` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* /// Returns true if and only if this searcher will choose a multi-line /// strategy given the provid...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 149`, `args: 56`, `func_start: 53`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 46`, `import: 6`
* *Defense:* `safety: 9`, `doc: 384`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.482
  * `Choke Point (Betweenness):` 0.007363 | `Ripple Effect (Closeness):` 0.096024
  * `Imports (Out-Degree: 7):` core, glue, mmap, crate::line_buffer, crate::line_buffer::BufferAllocation, crate::line_buffer::DEFAULT_BUFFER_CAPACITY, crate::line_buffer::LineBuffer, crate::line_buffer::LineBufferBuilder...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `crates/ignore/src/gitignore.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.615)
- **Top Global Matches:** file_cluster_5: 7.615, file_cluster_12: 7.686, file_cluster_0: 8.829
- **Magnitude:** 294.78 | **LOC:** 850 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **22**; blast radius 18.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.0%), Guard Balance (formerly Safety Score) (52.6%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_line` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* /// Add a line from a gitignore file to this builder. /// /// If this line came from a particular `g...
  * `add` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* /// Add each glob from the file path given. /// /// The file given should be formatted as a `gitigno...
  * `matched_stripped` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /// Like matched, but takes a path that has already been stripped.
  * `strip` **(Defensive Guards)** (Impact: 11.9)
    * *Intent:* /// Strips the given path such that it's suitable for matching with this /// gitignore matcher.
  * `matched_path_or_any_parents` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* /// /// `is_dir` should be true if the path refers to a directory and false /// otherwise. /// /// T...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 112`, `args: 65`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 23`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 32`, `import: 7`
* *Defense:* `safety: 15`, `doc: 157`, `test: 23`, `sync_locks: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.225
  * `Choke Point (Betweenness):` 0.003386 | `Ripple Effect (Closeness):` 0.048516
  * `Imports (Out-Degree: 4):` crate::Error, crate::Match, crate::PartialErrorBuilder, crate::pathutil::is_file_name, crate::pathutil::strip_prefix, globset::Candidate, globset::GlobBuilder, globset::GlobSet...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/searcher/src/testutil.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.759)
- **Top Global Matches:** file_cluster_12: 6.759, file_cluster_5: 7.68, file_cluster_16: 8.19
- **Magnitude:** 274.82 | **LOC:** 798 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 5.426; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.1%), Guard Balance (formerly Safety Score) (51.0%), Connectivity (formerly Api Exposure) (37.6%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configs` **(Compute Cores)** (Impact: 26.5)
    * *Intent:* /// Configs generates a set of all search configurations that should be /// tested. The configs gene...
  * `test` **(Stateful Encapsulated Methods)** (Impact: 20.6)
    * *Intent:* /// Execute the test. If the test succeeds, then this returns successfully. /// If the test fails, t...
  * `minimal_heap_limit` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* /// Return the minimum size of a buffer required for a successful search. /// /// Generally, this co...
  * `matched` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `context` **(Defensive Guards)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 135`, `args: 47`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 32`
* *Architecture:* `io: 1`, `api: 38`, `import: 4`
* *Defense:* `safety: 12`, `doc: 117`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.426
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.068431
  * `Imports (Out-Degree: 3):` bstr::ByteSlice, crate::searcher::BinaryDetection, crate::searcher::Searcher, crate::searcher::SearcherBuilder, crate::sink::Sink, crate::sink::SinkContext, crate::sink::SinkFinish, crate::sink::SinkMatch...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/printer/src/util.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.082)
- **Top Global Matches:** file_cluster_0: 7.082, file_cluster_5: 8.051, file_cluster_16: 9.144
- **Magnitude:** 272.78 | **LOC:** 609 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **23**; blast radius 13.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Guard Balance (formerly Safety Score) (54.5%), Connectivity (formerly Api Exposure) (36.5%), Debt Markers (formerly Tech Debt) (10.5%)
- **Documentation Coverage:** 45.9016% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replace_all` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* /// Executes a replacement on the given haystack string by replacing all /// matches with the given ...
  * `replace_with_captures_in_context` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* /// Like `Matcher::replace_with_captures_at`, but accepts an end bound. /// /// See also: `find_iter...
  * `find_iter_at_in_context` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `trim_line_terminator` **(Stateful Encapsulated Methods)** (Impact: 12.9)
    * *Intent:* /// Given a buf and some bounds, if there is a line terminator at the end of /// the given bounds in...
  * `with_separator` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* /// Set the separator on this path. /// /// When set, `PrinterPath::as_bytes` will return the path p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 94`, `args: 45`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`, `fragile_debt: 1`
* *Architecture:* `api: 32`, `import: 6`
* *Defense:* `safety: 5`, `doc: 103`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.57
  * `Choke Point (Betweenness):` 0.004581 | `Ripple Effect (Closeness):` 0.04845
  * `Imports (Out-Degree: 6):` bstr::ByteVec, crate::MAX_LOOK_AHEAD, crate::hyperlink::HyperlinkPath, grep_matcher::Captures, grep_matcher::LineTerminator, grep_matcher::Match, grep_matcher::Matcher, grep_searcher::LineIter...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/printer/src/hyperlink/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.661)
- **Top Global Matches:** file_cluster_5: 6.661, file_cluster_12: 8.156, file_cluster_7: 9.888
- **Magnitude:** 271.88 | **LOC:** 1166 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 18.306; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.3%), Mutation Surface (formerly State Flux) (35.6%), Debt Markers (formerly Tech Debt) (31.0%)
- **Documentation Coverage:** 19.1781% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_str` **(Compute Cores)** (Impact: 30.5)
  * `begin` **(Stateful Encapsulated Methods)** (Impact: 13.0)
    * *Intent:* /// Start interpolation with the given values by writing a hyperlink /// to `wtr`. Subsequent writes...
  * `validate` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* /// Validate that the format is well-formed.
  * `validate_scheme` **(Generic / Templated Code)** (Impact: 9.7)
    * *Intent:* /// Validate that the format starts with a valid scheme. Validation is done /// according to how a s...
  * `from_path` **(I/O & Config Routines)** (Impact: 8.7)
    * *Intent:* /// Returns a hyperlink path from an OS path.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 125`, `args: 65`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 22`, `unreferenced_by_name: 13`
* *Architecture:* `api: 33`, `import: 12`
* *Defense:* `safety: 8`, `doc: 210`, `test: 52`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.306
  * `Choke Point (Betweenness):` 0.001802 | `Ripple Effect (Closeness):` 0.047812
  * `Imports (Out-Degree: 2):` aliases, bstr::ByteSlice, crate::util::DecimalFormatter, self::*, self::HyperlinkFormatErrorKind::*, self::aliases::HYPERLINK_PATTERN_ALIASES, std::cell::RefCell, std::io...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/core/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_8: 7.19, file_cluster_6: 12.013, file_cluster_4: 20.502
- **Magnitude:** 230.6 | **LOC:** 484 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.79; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.7%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search_parallel` **(Defensive Guards)** (Impact: 34.7)
    * *Intent:* /// The top-level entry point for multi-threaded search. /// /// The parallelism is itself achieved ...
  * `search` **(Compute Cores)** (Impact: 33.4)
    * *Intent:* /// The top-level entry point for single-threaded search. /// /// This recursively steps through the...
  * `run` **(Compute Cores)** (Impact: 23.9)
    * *Intent:* /// The main entry point for ripgrep. /// /// The given parse result determines ripgrep's behavior. ...
  * `files_parallel` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /// The top-level entry point for multi-threaded file listing without /// searching. /// /// This re...
  * `types` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* /// The top-level entry point for `--type-list`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 115`, `args: 18`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 10`, `doc: 71`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.79
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` flags, haystack, logger, messages, search, crate::flags::GenerateMode, crate::flags::HiArgs, crate::flags::Mode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/core/flags/complete/rg.zsh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 14.862)
- **Top Global Matches:** file_cluster_6: 14.862, file_cluster_4: 17.212, file_cluster_14: 18.348
- **Magnitude:** 218.28 | **LOC:** 692 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Mutation Surface (formerly State Flux) (97.5%), Complexity Load (formerly Cognitive Load) (81.1%), Guard Balance (formerly Safety Score) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_rg` **(I/O & Config Routines)** (Impact: 96.8)
    * *Intent:* #compdef rg ## # zsh completion function for ripgrep # # Run ci/test-complete after building to ensu...
  * `_rg_hyperlink_format_strings` **(I/O & Config Routines)** (Impact: 5.2)
  * `_rg_types` **(Compute Cores)** (Impact: 4.8)
  * `_rg_encodings` **(Parameter Forwarders)** (Impact: 1.9)
  * `_rg_hyperlink_format_aliases` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 65`, `args: 4`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 19`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 34`, `concurrency: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.79
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/printer/src/json.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.873)
- **Top Global Matches:** file_cluster_5: 5.873, file_cluster_12: 8.337, file_cluster_7: 9.445
- **Magnitude:** 214.92 | **LOC:** 1058 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 3.53; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (58.4%), Connectivity (formerly Api Exposure) (57.7%), Guard Balance (formerly Safety Score) (49.3%)
- **Documentation Coverage:** 36.2069% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `context` **(Many-Argument Workhorses)** (Impact: 15.4)
  * `record_matches` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* /// Execute the matcher over the given bytes and record the match /// locations if the current confi...
  * `matched` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `write_message` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* /// Write the given message followed by a new line. The new line is /// determined from the configur...
  * `new` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* /// Create a new set of match ranges from a set of matches and the /// corresponding bytes that thos...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 105`, `args: 39`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 16`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `safety: 1`, `doc: 478`, `test: 18`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.53
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.041292
  * `Imports (Out-Degree: 8):` crate::counter::CounterWriter, crate::jsont, crate::stats::Stats, crate::util::Replacer, crate::util::find_iter_at_in_context, grep_matcher::LineTerminator, grep_matcher::Match, grep_matcher::Matcher...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/core/flags/lowargs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.427)
- **Top Global Matches:** file_cluster_0: 7.427, file_cluster_16: 7.781, file_cluster_13: 8.575
- **Magnitude:** 199.98 | **LOC:** 724 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 14.468; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.2%), Connectivity (formerly Api Exposure) (41.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `supported` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* /// Checks whether the selected sort mode is supported. If it isn't, an /// error (hopefully explain...
  * `update` **(Stateful Encapsulated Methods)** (Impact: 5.9)
    * *Intent:* /// Update this mode to the new mode while implementing various override /// semantics. For example,...
  * `get` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* /// Returns the specific number of contextual lines that should be shown /// around each match. This...
  * `set_before` **(Stateful Encapsulated Methods)** (Impact: 4.2)
    * *Intent:* /// Set the "before" context. /// /// If this was set to "passthru" context, then it is overridden i...
  * `set_after` **(Stateful Encapsulated Methods)** (Impact: 4.2)
    * *Intent:* /// Set the "after" context. /// /// If this was set to "passthru" context, then it is overridden in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 69`, `args: 28`, `func_start: 20`, `class_start: 23`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 114`, `import: 5`
* *Defense:* `safety: 3`, `doc: 258`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.468
  * `Choke Point (Betweenness):` 0.004356 | `Ripple Effect (Closeness):` 0.039867
  * `Imports (Out-Degree: 1):` bstr::BString, bstr::ByteVec, grep::printer::HyperlinkFormat, grep::printer::UserColorSpec, std::ffi::OsStr, std::ffi::OsString, std::path::PathBuf
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/regex/src/matcher.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.473)
- **Top Global Matches:** file_cluster_5: 6.473, file_cluster_12: 9.068, file_cluster_7: 9.121
- **Magnitude:** 196.6 | **LOC:** 671 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **15**; blast radius 6.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.7%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 42.6829% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_many` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* /// Build a new matcher using the current configuration for the provided /// patterns. The resulting...
  * `try_find_iter` **(Generic / Templated Code)** (Impact: 8.9)
  * `find_candidate_line` **(Defensive Guards)** (Impact: 6.0)
  * `crlf` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /// This method sets two distinct settings: /// /// 1. It causes the line terminator for the matcher...
  * `candidate_lines` **(Annotated & Test Methods)** (Impact: 4.6)
    * *Intent:* // Test that finding candidate lines works as expected. // FIXME: Re-enable this test once inner lit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 83`, `args: 50`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 22`, `fragile_debt: 1`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 1`, `doc: 225`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.326
  * `Choke Point (Betweenness):` 0.003899 | `Ripple Effect (Closeness):` 0.062812
  * `Imports (Out-Degree: 4):` crate::config::Config, crate::error::Error, crate::literal::InnerLiterals, grep_matcher::ByteSet, grep_matcher::Captures, grep_matcher::LineMatchKind, grep_matcher::LineTerminator, grep_matcher::Match...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/ignore/src/types.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.513)
- **Top Global Matches:** file_cluster_12: 7.513, file_cluster_5: 7.651, file_cluster_0: 7.946
- **Magnitude:** 182.8 | **LOC:** 585 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 8.144; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.3%), Connectivity (formerly Api Exposure) (56.0%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 62.069% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matched` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `add_def` **(Compute Cores)** (Impact: 21.0)
  * `build` **(Compute Cores)** (Impact: 11.9)
  * `add` **(Compute Cores)** (Impact: 8.8)
  * `select` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 80`, `args: 36`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 11`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 3`, `doc: 85`, `test: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.144
  * `Choke Point (Betweenness):` 0.00062 | `Ripple Effect (Closeness):` 0.037519
  * `Imports (Out-Degree: 5):` crate::Error, crate::Match, crate::default_types::DEFAULT_TYPES, crate::pathutil::file_name, globset::GlobBuilder, globset::GlobSet, globset::GlobSetBuilder, regex_automata::util::pool::Pool...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/ignore/src/walk.rs` (RUST) | Magnitude: 855.1 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1610, doc: 477, structural_boundaries: 386, args: 192

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/ignore/src/types.rs` (RUST) | Magnitude: 182.8 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 332, doc: 85, structural_boundaries: 80, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/grep/src/lib.rs` (RUST) | Magnitude: 19.64 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 6, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/regex/src/non_matching.rs` (RUST) | Magnitude: 64.46 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 22, test: 18, args: 16
- `crates/regex/src/literal.rs` (RUST) | Magnitude: 323.66 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 682, test: 184, structural_boundaries: 145, doc: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/core/haystack.rs` (RUST) | Magnitude: 48.38 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 73, doc: 37, structural_boundaries: 15, branch: 13
- `crates/searcher/src/searcher/mmap.rs` (RUST) | Magnitude: 27.1 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 44, doc: 37, structural_boundaries: 9, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/ignore/src/gitignore.rs` (RUST) | Magnitude: 294.78 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 541, doc: 157, structural_boundaries: 112, core_var_decl: 68

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/core/flags/defs.rs` -> Churn: **100.0%** | Cog Load: 6.1029% | Debt: 72.81%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/core/flags/defs.rs` -> **Waldir Pimenta** (100.0% isolated ownership) | Magnitude: 1289.82
- `crates/core/flags/lowargs.rs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 199.98
- `tests/util.rs` -> **Sungjoon Moon** (100.0% isolated ownership) | Magnitude: 168.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/searcher/src/searcher/mod.rs` -> **Severity: 0.539** (Bridge: 0.0074 * Flux: 73.2173%)
- `crates/core/flags/doc/version.rs` -> **Severity: 0.487** (Bridge: 0.0067 * Flux: 73.0316%)
- `crates/printer/src/util.rs` -> **Severity: 0.444** (Bridge: 0.0046 * Flux: 96.9094%)
- `crates/core/flags/hiargs.rs` -> **Severity: 0.32** (Bridge: 0.0093 * Flux: 34.3831%)
- `crates/regex/src/matcher.rs` -> **Severity: 0.318** (Bridge: 0.0039 * Flux: 81.5434%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/matcher/src/lib.rs` -> **Severity: 6.463** (Embedded: 0.1338 * Error Risk: 48.3079%)
- `crates/matcher/src/interpolate.rs` -> **Severity: 4.923** (Embedded: 0.0918 * Error Risk: 53.6208%)
- `crates/searcher/src/line_buffer.rs` -> **Severity: 4.506** (Embedded: 0.0719 * Error Risk: 62.6264%)
- `crates/searcher/src/searcher/mod.rs` -> **Severity: 4.408** (Embedded: 0.096 * Error Risk: 45.9058%)
- `crates/regex/src/matcher.rs` -> **Severity: 4.038** (Embedded: 0.0628 * Error Risk: 64.2857%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/globset/src/lib.rs` -> **Severity: 2745.498** (Blast Radius: 37.145 * Doc Risk: 73.913%)
- `crates/matcher/src/interpolate.rs` -> **Severity: 1888.07** (Blast Radius: 44.055 * Doc Risk: 42.8571%)
- `crates/matcher/src/lib.rs` -> **Severity: 1486.809** (Blast Radius: 48.54 * Doc Risk: 30.6306%)
- `crates/ignore/src/lib.rs` -> **Severity: 1142.739** (Blast Radius: 23.671 * Doc Risk: 48.2759%)
- `crates/ignore/src/walk.rs` -> **Severity: 1079.261** (Blast Radius: 25.797 * Doc Risk: 41.8367%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 83 literal sites + 6 sites through wrappers = 89

- `eprint` (function, debug_prints, primitive): 6 call sites in 1 files -- `benchsuite/benchsuite`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9088 call pairs -- scoped 20.7%, unique 0.0%, ambiguous 13.4%, external 65.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 8824 | 20.1% | 0.0% | 13.8% | 66.1% |
| python | 210 | 47.6% | 0.0% | 1.4% | 51.0% |
| shell | 54 | 9.3% | 0.0% | 0.0% | 90.7% |

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
