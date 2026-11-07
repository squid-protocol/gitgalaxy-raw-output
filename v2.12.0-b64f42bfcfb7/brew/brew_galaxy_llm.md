# ARCHITECTURAL_BRIEF: brew
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Homebrew/brew` |
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
- **Scope:** 1719 analyzed artifact(s), 163000 LOC.
- **Load-bearing artifact:** `Library/Homebrew/formula.rb` -- 327 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Library/Homebrew/formula.rb` -- pulls in 59 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Library/Homebrew/formula.rb` at magnitude 29190.3 (structural weight, not risk).
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
| Total Artifacts | 2828 |
| Analyzed Artifacts (Scanned) | 1719 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1109 |
| Total LOC | 163000 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 60.8% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5756 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2515 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.8807 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 135 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 1572 | 149701 | 91.4% |
| SHELL | 53 | 4760 | 3.1% |
| YAML | 28 | 2439 | 1.6% |
| RUST | 20 | 3037 | 1.2% |
| JSON | 14 | 2302 | 0.8% |
| MARKDOWN | 13 | 0 | 0.8% |
| PLAINTEXT | 6 | 0 | 0.3% |
| HTML | 4 | 187 | 0.2% |
| SWIFT | 3 | 127 | 0.2% |
| XML | 3 | 0 | 0.2% |
| DOCKERFILE | 1 | 78 | 0.1% |
| M4 | 1 | 1 | 0.1% |
| JAVASCRIPT | 1 | 368 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1719 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 36%, Data / Markup / Trivial 17%, Large Core Modules (2) 11%, Large Core Modules (3) 10%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1700 | 98.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1109*

**Composition by Extension & Reason:**
- `.rb`: 337x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 128 LOC), 1x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.rbi`: 35x Excluded (Machine-Generated Source Code Signature: 14 LOC), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `no_extension`: 76x Excluded: Neighborhood Micro-Mass Limit Exceeded, 51x Unsupported Format (.undeterminable), 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pc`: 91x Excluded (Unsupported Extension: '.pc')
- `.md`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 32x Excluded (Explicitly Denied Extension: '.gz')
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9119 LOC)
- `.txt`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 87 LOC)
- `.diff`: 5x Excluded (Unsupported Extension: '.diff')
- `.erb`: 1x Excluded (Machine-Generated Source Code Signature: 200 LOC), 1x Excluded (Machine-Generated Source Code Signature: 259 LOC), 1x Excluded (Machine-Generated Source Code Signature: 212 LOC)
- `.tbz`: 4x Excluded (Unsupported Extension: '.tbz')
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 13.9 | 6.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 37.3 | 49.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.4 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 80.8 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 112 | 60 | 0 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| cleanup | 91 | 19 | 0 | `Library/Homebrew/brew.sh` |
| guards | 6130 | 704 | 9 | `Library/Homebrew/formula.rb` |
| danger | 7021 | 776 | 11 | `Library/Homebrew/env_config.rb` |
| concurrency | 233 | 68 | 0 | `Library/Homebrew/cmd/update.sh` |
| connectivity | 2859 | 729 | 4 | `Library/Homebrew/formula.rb` |
| io | 2953 | 537 | 5 | `Library/Homebrew/shims/super/cc` |
| crypto | 0 | 0 | 0 | - |
| ipc | 98 | 49 | 0 | `Library/Homebrew/cmd/update.sh` |
| time | 135 | 61 | 0 | `Library/Homebrew/test/cleanup_spec.rb` |
| serialization | 94 | 58 | 0 | `Library/Homebrew/utils/shared_audits.rb` |
| regex | 977 | 306 | 2 | `Library/Homebrew/dev-cmd/bump-formula-pr.rb` |
| events | 69 | 30 | 0 | `Library/Homebrew/brew.sh` |
| tests | 19292 | 908 | 29 | `Library/Homebrew/test/formula_spec.rb` |
| docs | 6606 | 745 | 11 | `Library/Homebrew/formula.rb` |
| debt | 2061 | 455 | 3 | `Library/Homebrew/livecheck/livecheck.rb` |
| mutation | 29038 | 1016 | 49 | `Library/Homebrew/formula.rb` |
| dead_code | 109 | 62 | 0 | `Library/Homebrew/requirement.rb` |
| credential | 60 | 27 | 0 | `Library/Homebrew/data/spdx/spdx_exceptions.json` |
| threat | 9 | 6 | 0 | `Library/Homebrew/test/dev-cmd/bottle_spec.rb` |
| ml_ai | 18 | 8 | 0 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| ui | 152 | 11 | 0 | `Library/Homebrew/formula_creator.rb` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Library/Homebrew/shims/super/cc` (Hits: 176)
- `Library/Homebrew/brew.sh` (Hits: 148)
- `Library/Homebrew/cmd/update.sh` (Hits: 141)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **formula.rb** (`Library/Homebrew/formula.rb`) — 327 inbound connections
2. **sorbet.rb** (`Library/Homebrew/standalone/sorbet.rb`) — 283 inbound connections
3. **abstract_command.rb** (`Library/Homebrew/abstract_command.rb`) — 122 inbound connections
4. **output.rb** (`Library/Homebrew/utils/output.rb`) — 109 inbound connections
5. **args_parse.rb** (`Library/Homebrew/test/cmd/shared_examples/args_parse.rb`) — 108 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **formula.rb** (`Library/Homebrew/formula.rb`) — 59 outbound dependencies
2. **fetch.rs** (`Library/Homebrew/rust/brew-rs/src/commands/fetch.rs`) — 54 outbound dependencies
3. **all.rb** (`Library/Homebrew/rubocops/all.rb`) — 42 outbound dependencies
4. **unpack_strategy.rb** (`Library/Homebrew/unpack_strategy.rb`) — 41 outbound dependencies
5. **formula_installer.rb** (`Library/Homebrew/formula_installer.rb`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `new_cask?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/cask/audit.rb`) -> Impact: **834.5** | LOC: 1329
- `online?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/cask/audit.rb`) -> Impact: **834.3** | LOC: 1326
- `signing?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/cask/audit.rb`) -> Impact: **834.1** | LOC: 1323
- `strict?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/cask/audit.rb`) -> Impact: **834.0** | LOC: 1320
- `debug?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **605.6** | LOC: 1619
- `debug_symbols?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **605.5** | LOC: 1616
- `force?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **605.3** | LOC: 1613
- `force_bottle?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **605.2** | LOC: 1610
- `git?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **605.0** | LOC: 1607
- `ignore_deps?` **(Many-Argument Workhorses)** (@ `Library/Homebrew/formula_installer.rb`) -> Impact: **604.9** | LOC: 1604

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Library/Homebrew` | 160 | 68050.84 | 25.03% | 8.17% |
| `Library/Homebrew/cask` | 28 | 12910.9 | 24.71% | 4.59% |
| `Library/Homebrew/dev-cmd` | 56 | 6873.14 | 37.96% | 3.91% |
| `Library/Homebrew/utils` | 49 | 6448.18 | 31.28% | 6.0% |
| `Library/Homebrew/cmd` | 82 | 5570.88 | 22.9% | 6.95% |
| `Library/Homebrew/test` | 101 | 5441.26 | 7.06% | 0.0% |
| `Library/Homebrew/rubocops` | 40 | 2598.92 | 26.42% | 2.14% |
| `Library/Homebrew/test_bot` | 14 | 2307.66 | 31.0% | 8.17% |
| `Library/Homebrew/livecheck` | 8 | 1866.34 | 23.85% | 0.0% |
| `Library/Homebrew/bundle` | 16 | 1825.9 | 39.03% | 2.57% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Library/Homebrew/abstract_command.rb` -> **100.0%** Exposure
- `Library/Homebrew/dependencies.rbi` -> **100.0%** Exposure
- `Library/Homebrew/extend/blank.rb` -> **100.0%** Exposure
- `Library/Homebrew/extend/object/duplicable.rb` -> **100.0%** Exposure
- `Library/Homebrew/standalone/sorbet.rb` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Library/Homebrew/api/cask/cask_struct_generator.rb` -> **100.0%** Exposure
- `Library/Homebrew/api/formula/formula_struct_generator.rb` -> **100.0%** Exposure
- `Library/Homebrew/bottle_specification.rb` -> **100.0%** Exposure
- `Library/Homebrew/brew.rb` -> **100.0%** Exposure
- `Library/Homebrew/bundle.rb` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Library/Homebrew/standalone/sorbet.rb` -> **0** Orphaned Functions | **11** Duplicates
- `Library/Homebrew/requirement.rb` -> **10** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/utils/helpers.sh` -> **10** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/extend/blank.rb` -> **0** Orphaned Functions | **8** Duplicates
- `Library/Homebrew/os/mac/xcode.rb` -> **0** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Library/Homebrew/utils/analytics.rb` -> **80.7615%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3718` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Library/Homebrew/formula.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.98)
- **Top Global Matches:** file_cluster_6: 8.98, file_cluster_4: 10.051, file_cluster_12: 15.747
- **Magnitude:** 29190.3 | **LOC:** 4995 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **327** in-repo importer(s); it depends on **59**; blast radius 40.957; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (57.4%)
- **Documentation Coverage:** 28.2123% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_s` **(Many-Argument Workhorses)** (Impact: 492.0)
  * `bottle_prefix` **(Many-Argument Workhorses)** (Impact: 474.1)
    * *Intent:* # The directory where the formula's installation or test logs will be written. sig { returns(Pathnam...
  * `logs` **(Many-Argument Workhorses)** (Impact: 474.1)
    * *Intent:* # The prefix, if any, to use in filenames for logging current activity. sig { returns(String) } def ...
  * `pwsh_completion` **(Many-Argument Workhorses)** (Impact: 470.7)
    * *Intent:* # The directory used for as the prefix for {#etc} and {#var} files on # installation so, despite not...
  * `fish_completion` **(Many-Argument Workhorses)** (Impact: 468.9)
    * *Intent:* # The directory where the formula's PowerShell completion files should be # installed. # This is sym...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 216 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 544`, `args: 105`, `func_start: 278`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 20`, `state_mutation: 301`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `io: 19`, `api: 173`, `import: 47`
* *Defense:* `safety: 227`, `doc: 526`, `test: 97`, `sync_locks: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.957
  * `Choke Point (Betweenness):` 0.062183 | `Ripple Effect (Closeness):` 0.192574
  * `Imports (Out-Degree: 50):` APIHashable, BuildEnvironment::DSL, Cachable, Context, FileUtils, Forwardable, Homebrew::Livecheck::Constants, InstallRenamed...
  * `Imported By (In-Degree: 327):` (Excluded from Brief to save tokens)

### `Library/Homebrew/formula_installer.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.952)
- **Top Global Matches:** file_cluster_8: 6.952, file_cluster_6: 15.675, file_cluster_3: 22.264
- **Magnitude:** 12239.68 | **LOC:** 1774 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **31**; blast radius 1.072; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 1.8505% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `debug?` **(Many-Argument Workhorses)** (Impact: 605.6)
  * `debug_symbols?` **(Many-Argument Workhorses)** (Impact: 605.5)
  * `force?` **(Many-Argument Workhorses)** (Impact: 605.3)
  * `force_bottle?` **(Many-Argument Workhorses)** (Impact: 605.2)
  * `git?` **(Many-Argument Workhorses)** (Impact: 605.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 187 instances
* *High Risk Execution (weighted view):* 15
* *State Mutation (weighted view):* 634
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 237`, `args: 16`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 23`, `state_mutation: 260`
* *Architecture:* `io: 17`, `api: 22`, `import: 35`
* *Defense:* `safety: 70`, `doc: 91`, `test: 24`, `sync_locks: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.072
  * `Choke Point (Betweenness):` 0.018516 | `Ripple Effect (Closeness):` 0.087281
  * `Imports (Out-Degree: 39):` FormulaCellarChecks, Utils::Output::Mixin, attestation, cache_store, cask_loader, caveats, cleaner, install...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cask/audit.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.533)
- **Top Global Matches:** file_cluster_4: 7.533, file_cluster_6: 8.694, file_cluster_15: 14.468
- **Magnitude:** 4550.76 | **LOC:** 1403 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 31.2%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.375; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.9%)
- **Documentation Coverage:** 3.9683% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_cask?` **(Many-Argument Workhorses)** (Impact: 834.5)
  * `online?` **(Many-Argument Workhorses)** (Impact: 834.3)
  * `signing?` **(Many-Argument Workhorses)** (Impact: 834.1)
  * `strict?` **(Many-Argument Workhorses)** (Impact: 834.0)
  * `cask_bundle_min_os` **(Compute Cores)** (Impact: 248.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 138 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 287`, `args: 9`, `func_start: 84`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 9`, `state_mutation: 147`, `planned_debt: 1`
* *Architecture:* `io: 16`, `api: 49`, `import: 18`
* *Defense:* `safety: 53`, `doc: 86`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.001904
  * `Imports (Out-Degree: 21):` SystemCommand::Mixin, denylist, download, installer, quarantine, digest, formula_name_cask_token_auditor, livecheck...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cask/installer.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.093)
- **Top Global Matches:** file_cluster_6: 8.093, file_cluster_8: 10.344, file_cluster_4: 15.496
- **Magnitude:** 4110.7 | **LOC:** 923 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **11**; blast radius 3.876; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%), Connectivity (formerly Api Exposure) (64.0%)
- **Documentation Coverage:** 28.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adopt?` **(Compute Cores)** (Impact: 276.5)
  * `binaries?` **(Compute Cores)** (Impact: 276.4)
  * `force?` **(Compute Cores)** (Impact: 276.2)
  * `installed_as_dependency?` **(Compute Cores)** (Impact: 276.1)
  * `installed_on_request?` **(Compute Cores)** (Impact: 275.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 73 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 141`, `args: 10`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 10`, `state_mutation: 103`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 18`, `import: 13`
* *Defense:* `safety: 27`, `doc: 44`, `test: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.876
  * `Choke Point (Betweenness):` 0.005008 | `Ripple Effect (Closeness):` 0.082184
  * `Imports (Out-Degree: 15):` config, download, migrator, quarantine, tab, installer, formula_installer, unpack_strategy...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cleanup.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.191)
- **Top Global Matches:** file_cluster_4: 8.191, file_cluster_6: 8.644, file_cluster_9: 14.801
- **Magnitude:** 1348.06 | **LOC:** 813 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 0.429; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dry_run?` **(Many-Argument Workhorses)** (Impact: 249.7)
  * `prune?` **(Many-Argument Workhorses)** (Impact: 249.5)
  * `scrub?` **(Many-Argument Workhorses)** (Impact: 249.3)
  * `stale_formula?` **(Defensive Guards)** (Impact: 85.5)
  * `prune_prefix_symlinks_and_directories` **(I/O & Config Routines)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 151`, `args: 18`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 71`, `planned_debt: 1`
* *Architecture:* `io: 20`, `api: 5`, `import: 13`
* *Defense:* `safety: 30`, `doc: 45`, `test: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.429
  * `Choke Point (Betweenness):` 0.002853 | `Ripple Effect (Closeness):` 0.068203
  * `Imports (Out-Degree: 15):` ObserverPathnameExtension, Utils::Output::Mixin, cask_loader, caskroom, cleanup, formula, installed_dependents, uninstall...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Library/Homebrew/livecheck/livecheck.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.134)
- **Top Global Matches:** file_cluster_6: 7.134, file_cluster_4: 10.678, file_cluster_8: 16.335
- **Magnitude:** 1307.76 | **LOC:** 1067 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 0.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (74.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkable_urls` **(Many-Argument Workhorses)** (Impact: 300.5)
  * `run_checks` **(Many-Argument Workhorses)** (Impact: 295.3)
  * `resolve_livecheck_reference` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `status_hash` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `print_latest_version` **(Many-Argument Workhorses)** (Impact: 23.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 181 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 59`, `args: 14`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 191`
* *Architecture:* `io: 8`, `api: 2`, `import: 11`
* *Defense:* `safety: 42`, `doc: 16`, `test: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.627
  * `Choke Point (Betweenness):` 0.000217 | `Ripple Effect (Closeness):` 0.004223
  * `Imports (Out-Degree: 12):` Utils::Output::Mixin, addressable, constants, error, livecheck_version, skip_conditions, strategy, ruby-progressbar...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Library/Homebrew/tap.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.305)
- **Top Global Matches:** file_cluster_12: 8.305, file_cluster_5: 9.698, file_cluster_0: 10.162
- **Magnitude:** 1235.08 | **LOC:** 1613 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **16**; blast radius 10.859; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.5%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 0.6939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_s` **(Many-Argument Workhorses)** (Impact: 142.4)
    * *Intent:* # The full name of this {Tap}, including the `homebrew-` prefix. # It combines {#user} and 'homebrew...
  * `install` **(Many-Argument Workhorses)** (Impact: 116.0)
  * `fix_remote_configuration` **(Defensive Guards)** (Impact: 20.8)
  * `audit_exception` **(Compute Cores)** (Impact: 18.9)
  * `fetch` **(Defensive Guards)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 151 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 274`, `args: 35`, `func_start: 123`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 4`, `state_mutation: 186`, `planned_debt: 4`
* *Architecture:* `io: 7`, `api: 11`, `import: 14`
* *Defense:* `safety: 101`, `doc: 164`, `test: 58`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.859
  * `Choke Point (Betweenness):` 0.035936 | `Ripple Effect (Closeness):` 0.210537
  * `Imports (Out-Degree: 19):` Cachable, Enumerable, T::Generic, T::Helpers, Utils::Output::Mixin, api, commands, completions...
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `Library/Homebrew/formula_auditor.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.905)
- **Top Global Matches:** file_cluster_6: 6.905, file_cluster_4: 11.998, file_cluster_8: 14.403
- **Magnitude:** 1130.56 | **LOC:** 1250 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%), Guard Balance (formerly Safety Score) (79.3%)
- **Documentation Coverage:** 82.44% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `audit_text` **(Compute Cores)** (Impact: 77.6)
  * `audit_deps` **(I/O & Config Routines)** (Impact: 68.2)
  * `audit_specs` **(I/O & Config Routines)** (Impact: 53.5)
  * `audit_revision` **(I/O & Config Routines)** (Impact: 31.1)
  * `committed_version_info` **(Compute Cores)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 152 instances
* *High Risk Execution (weighted view):* 32
* *State Mutation (weighted view):* 485
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 222`, `args: 11`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 35`, `state_mutation: 181`, `planned_debt: 2`
* *Architecture:* `io: 10`, `api: 35`, `import: 8`
* *Defense:* `safety: 50`, `doc: 5`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.001551
  * `Imports (Out-Degree: 15):` FormulaCellarChecks, Utils::Curl, Utils::Output::Mixin, deprecate_disable, formula_name_cask_token_auditor, formula_versions, resource_auditor, git...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Library/Homebrew/keg.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.767)
- **Top Global Matches:** file_cluster_4: 6.767, file_cluster_6: 10.692, file_cluster_15: 12.268
- **Magnitude:** 1089.6 | **LOC:** 845 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 0.78; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.4%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 2.4757% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_s` **(Compute Cores)** (Impact: 254.8)
  * `require_relocation?` **(Compute Cores)** (Impact: 241.6)
  * `link_dir` **(Many-Argument Workhorses)** (Impact: 68.7)
  * `link` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `make_relative_symlink` **(Many-Argument Workhorses)** (Impact: 36.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 118`, `args: 15`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 69`
* *Architecture:* `io: 16`, `api: 20`, `import: 8`
* *Defense:* `safety: 32`, `doc: 61`, `test: 9`, `sync_locks: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.008347 | `Ripple Effect (Closeness):` 0.127507
  * `Imports (Out-Degree: 13):` Cachable, Forwardable, ObserverPathnameExtension, Utils::Output::Mixin, cachable, keg, keg_relocate, python...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cask/dsl.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.831)
- **Top Global Matches:** file_cluster_8: 9.831, file_cluster_3: 16.417, file_cluster_6: 21.388
- **Magnitude:** 1047.04 | **LOC:** 733 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 4.878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `depends_on_set_in_block?` **(Compute Cores)** (Impact: 139.1)
  * `deprecated?` **(Compute Cores)** (Impact: 138.9)
  * `disabled?` **(Compute Cores)** (Impact: 138.8)
  * `livecheck_defined?` **(Compute Cores)** (Impact: 138.6)
  * `on_system_blocks_exist?` **(Compute Cores)** (Impact: 138.5)
    * *Intent:* # Specifies the cask's name. # # NOTE: Multiple names can be specified. # # ### Example # # ```ruby ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 86`, `args: 24`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 89`, `planned_debt: 3`
* *Architecture:* `api: 1`, `import: 24`
* *Defense:* `safety: 66`, `doc: 38`, `test: 50`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000582
  * `Imports (Out-Degree: 17):` OnSystem::MacOSAndLinux, autobump_constants, artifact, artifact_set, caskroom, base, caveats, conflicts_with...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cask/cask.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.953)
- **Top Global Matches:** file_cluster_4: 6.953, file_cluster_6: 10.279, file_cluster_12: 11.465
- **Magnitude:** 1039.46 | **LOC:** 581 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 31.2%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 1.187; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.7%), Guard Balance (formerly Safety Score) (60.6%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `full_name` **(Many-Argument Workhorses)** (Impact: 178.9)
    * *Intent:* # Alias for {#full_token}. # # @api internal
  * `supports_macos?` **(Many-Argument Workhorses)** (Impact: 176.2)
  * `loaded_from_api?` **(Compute Cores)** (Impact: 144.3)
  * `caveats_object` **(Compute Cores)** (Impact: 136.7)
  * `to_s` **(Defensive Guards)** (Impact: 53.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 105`, `args: 12`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 55`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 14`, `import: 11`
* *Defense:* `safety: 22`, `doc: 30`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.187
  * `Choke Point (Betweenness):` 0.020912 | `Ripple Effect (Closeness):` 0.142719
  * `Imports (Out-Degree: 11):` APIHashable, Forwardable, Metadata, api_hashable, bundle_version, cask_loader, config, dsl...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Library/Homebrew/download_strategy.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.284)
- **Top Global Matches:** file_cluster_12: 6.284, file_cluster_15: 8.969, file_cluster_5: 9.076
- **Magnitude:** 988.76 | **LOC:** 1708 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 53.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **20**; blast radius 1.262; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.1%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_url_basename_time_file_size` **(Defensive Guards)** (Impact: 36.8)
  * `fetch` **(Defensive Guards)** (Impact: 27.7)
  * `detect_from_url` **(Compute Cores)** (Impact: 24.4)
  * `parse_basename` **(Defensive Guards)** (Impact: 21.1)
  * `detect_from_symbol` **(Compute Cores)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 112 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 252`, `args: 56`, `func_start: 135`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 13`, `state_mutation: 151`, `planned_debt: 19`, `fragile_debt: 1`
* *Architecture:* `io: 26`, `api: 2`, `import: 15`
* *Defense:* `safety: 102`, `doc: 190`, `test: 39`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.262
  * `Choke Point (Betweenness):` 0.010681 | `Ripple Effect (Closeness):` 0.130512
  * `Imports (Out-Degree: 15):` Context, FileUtils, SystemCommand::Mixin, T::Helpers, Utils::Curl, Utils::Output::Mixin, github_packages, json...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Library/Homebrew/diagnostic.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.639)
- **Top Global Matches:** file_cluster_15: 8.639, file_cluster_10: 8.987, file_cluster_12: 9.247
- **Magnitude:** 964.24 | **LOC:** 1209 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **15**; blast radius 0.574; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.8%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__check_stray_files` **(Many-Argument Workhorses)** (Impact: 406.9)
  * `checks` **(Defensive Guards)** (Impact: 14.7)
  * `examine_git_origin` **(Compute Cores)** (Impact: 11.6)
  * `check_cask_xattr` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* # If quarantine is not available, a warning is already shown by check_cask_quarantine_support so jus...
  * `check_git_status` **(I/O & Config Routines)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 85 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 177`, `args: 12`, `func_start: 73`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 16`, `state_mutation: 114`, `planned_debt: 1`
* *Architecture:* `io: 33`, `api: 34`, `import: 13`
* *Defense:* `safety: 26`, `doc: 73`, `test: 9`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.574
  * `Choke Point (Betweenness):` 0.003494 | `Ripple Effect (Closeness):` 0.085168
  * `Imports (Out-Degree: 20):` SystemCommand::Mixin, Utils::Output::Mixin, caskroom, quarantine, development_tools, diagnostic, formula, formulary...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/github.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.287)
- **Top Global Matches:** file_cluster_12: 7.287, file_cluster_4: 9.335, file_cluster_5: 9.545
- **Magnitude:** 891.58 | **LOC:** 1040 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **9**; blast radius 2.567; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%), Connectivity (formerly Api Exposure) (60.7%)
- **Documentation Coverage:** 48.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_bump_pr` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* # --write-only without --commit means don't take any git actions at all. return if args.write_only? ...
  * `check_for_duplicate_pull_requests` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `fetch_pull_requests` **(Many-Argument Workhorses)** (Impact: 23.0)
  * `repo_commits_for_user` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `organisation_repositories` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 111 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 393
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 98`, `args: 39`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 5`, `state_mutation: 171`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 28`, `import: 9`
* *Defense:* `safety: 34`, `doc: 29`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.567
  * `Choke Point (Betweenness):` 0.004428 | `Ripple Effect (Closeness):` 0.161746
  * `Imports (Out-Degree: 8):` SystemCommand::Mixin, Utils::Output::Mixin, system_command, uri, curl, actions, api, output...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `Library/Homebrew/brew.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.283)
- **Top Global Matches:** file_cluster_6: 9.283, file_cluster_8: 13.65, file_cluster_4: 15.173
- **Magnitude:** 871.38 | **LOC:** 1193 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 47.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.403; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.3%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (77.2%)
- **Documentation Coverage:** 85.0571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Compute Cores)** (Impact: 55.8)
  * `auto-update` **(Compute Cores)** (Impact: 41.7)
    * *Intent:* # These variables are set from various Homebrew scripts. # shellcheck disable=SC2154
  * `rust-frontend-enabled` **(Defensive Guards)** (Impact: 12.8)
  * `check-run-command-as-root` **(I/O & Config Routines)** (Impact: 10.3)
  * `setup_curl` **(I/O & Config Routines)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 115 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 360
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 659`, `args: 33`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 7`, `state_mutation: 130`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `io: 148`, `api: 78`, `concurrency: 10`, `import: 20`
* *Defense:* `safety: 14`, `doc: 22`, `test: 2`, `sync_locks: 2`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.403
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000582
  * `Imports (Out-Degree: 18):` $HOMEBREW_BASH_COMMAND, --taps.sh, --version.sh, casks.sh, formulae.sh, mcp-server.sh, setup-ruby.sh, shellenv.sh...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cli/parser.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.079)
- **Top Global Matches:** file_cluster_4: 8.079, file_cluster_6: 11.455, file_cluster_12: 12.184
- **Magnitude:** 793.72 | **LOC:** 766 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **11**; blast radius 4.747; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (45.8%)
- **Documentation Coverage:** 4.2553% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `option_to_name` **(Compute Cores)** (Impact: 175.0)
  * `switch` **(Many-Argument Workhorses)** (Impact: 75.5)
  * `named_args` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `parse` **(Many-Argument Workhorses)** (Impact: 27.2)
  * `generate_usage_banner` **(I/O & Config Routines)** (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 67 instances
* *High Risk Execution (weighted view):* 30
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 87`, `args: 26`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 36`, `state_mutation: 95`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 32`, `doc: 47`, `test: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.747
  * `Choke Point (Betweenness):` 0.008333 | `Ripple Effect (Closeness):` 0.138843
  * `Imports (Out-Degree: 9):` Utils::Output::Mixin, abstract_command, config, args, error, commands, env_config, optparse...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `Library/Homebrew/formulary.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.723)
- **Top Global Matches:** file_cluster_12: 7.723, file_cluster_15: 8.052, file_cluster_4: 8.157
- **Magnitude:** 793.34 | **LOC:** 1232 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **81** in-repo importer(s); it depends on **19**; blast radius 7.734; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.5%)
- **Documentation Coverage:** 26.5158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_formula_from_struct!` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `tap_formula_name_type` **(Compute Cores)** (Impact: 33.6)
  * `load_formula` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `resolve` **(Many-Argument Workhorses)** (Impact: 24.2)
  * `try_new` **(Compute Cores)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 170`, `args: 53`, `func_start: 71`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 130`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `io: 10`, `api: 5`, `import: 16`
* *Defense:* `safety: 52`, `doc: 74`, `test: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.016156 | `Ripple Effect (Closeness):` 0.177226
  * `Imports (Out-Degree: 19):` Cachable, Context, Utils::Output::Mixin, cachable, deprecate_disable, sha2, deep_transform_values, keys...
  * `Imported By (In-Degree: 81):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cmd/update.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.6)
- **Top Global Matches:** file_cluster_6: 8.6, file_cluster_8: 13.368, file_cluster_4: 14.596
- **Magnitude:** 792.8 | **LOC:** 1053 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.209; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (93.3%), Complexity Load (formerly Cognitive Load) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `homebrew-update_[Truncated]` **(Compute Cores)** (Impact: 262.6)
  * `merge_or_rebase` **(Many-Argument Workhorses)** (Impact: 91.3)
  * `fetch_api_file` **(Compute Cores)** (Impact: 42.4)
  * `simulate_from_current_branch` **(Many-Argument Workhorses)** (Impact: 10.1)
    * *Intent:* # Used for testing purposes, e.g. for testing formula migration after # renaming it in the currently...
  * `macos_version_name` **(I/O & Config Routines)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 73 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 650`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 90`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 141`, `api: 18`, `concurrency: 20`, `import: 2`
* *Defense:* `safety: 12`, `doc: 11`, `test: 3`, `sync_locks: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lock.sh, Hide
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/deprecate_disable.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.566)
- **Top Global Matches:** file_cluster_2: 4.566, file_cluster_17: 5.375, file_cluster_15: 5.992
- **Magnitude:** 775.34 | **LOC:** 132 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.593; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (26.4%), Connectivity (formerly Api Exposure) (19.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `doc: 5`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.593
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.137018
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/dev-cmd/bump.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.834)
- **Top Global Matches:** file_cluster_6: 6.834, file_cluster_4: 10.404, file_cluster_8: 16.227
- **Magnitude:** 736.34 | **LOC:** 846 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 47.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.235; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retrieve_and_display_info_and_open_pr` **(Many-Argument Workhorses)** (Impact: 171.9)
  * `run` **(I/O & Config Routines)** (Impact: 39.1)
  * `compare_versions` **(Many-Argument Workhorses)** (Impact: 29.3)
  * `livecheck_result` **(Compute Cores)** (Impact: 19.5)
  * `handle_formulae_and_casks` **(Defensive Guards)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 114 instances
* *High Risk Execution (weighted view):* 15
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 41`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 23`, `state_mutation: 139`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 14`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.235
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.000582
  * `Imports (Out-Degree: 15):` abstract_command, bump_version_parser, json, livecheck, repology
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/system_command.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.546)
- **Top Global Matches:** file_cluster_6: 8.546, file_cluster_4: 10.804, file_cluster_12: 17.184
- **Magnitude:** 719.18 | **LOC:** 579 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **10**; blast radius 10.775; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (94.1%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 18.32% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `must_succeed?` **(Defensive Guards)** (Impact: 70.1)
  * `reset_uid?` **(Defensive Guards)** (Impact: 70.0)
  * `run_as_real_uid?` **(Defensive Guards)** (Impact: 69.8)
  * `sudo?` **(Defensive Guards)** (Impact: 69.7)
  * `sudo_as_root?` **(Defensive Guards)** (Impact: 69.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 70`, `args: 8`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 11`, `state_mutation: 69`
* *Architecture:* `io: 12`, `api: 6`, `concurrency: 5`, `import: 8`
* *Defense:* `safety: 38`, `doc: 45`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.775
  * `Choke Point (Betweenness):` 0.011143 | `Ripple Effect (Closeness):` 0.176702
  * `Imports (Out-Degree: 5):` Context, Utils::Output::Mixin, context, ENV, plist, readline_nonblock, shellwords, uri...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `Library/Homebrew/dev-cmd/bump-formula-pr.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_4: 6.997, file_cluster_9: 10.414, file_cluster_6: 11.447
- **Magnitude:** 687.02 | **LOC:** 875 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.298; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 195.1)
  * `run_audit` **(Compute Cores)** (Impact: 29.5)
  * `update_resource_block!` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `check_new_version` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `fetch_resource_and_forced_version` **(Defensive Guards)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 105 instances
* *High Risk Execution (weighted view):* 25
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 51`, `args: 14`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 32`, `state_mutation: 127`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `import: 7`
* *Defense:* `safety: 17`, `doc: 15`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.298
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.000582
  * `Imports (Out-Degree: 10):` abstract_command, fileutils, formula, json, inreplace, pypi, tar
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/cmd/update-report.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.886)
- **Top Global Matches:** file_cluster_4: 7.886, file_cluster_6: 9.785, file_cluster_12: 13.534
- **Magnitude:** 679.36 | **LOC:** 1000 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.209; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(Compute Cores)** (Impact: 62.8)
  * `output_update_report` **(I/O & Config Routines)** (Impact: 53.4)
  * `migrate_tap_migration` **(I/O & Config Routines)** (Impact: 24.4)
  * `dump` **(Compute Cores)** (Impact: 19.5)
  * `tap_or_untap_core_taps_if_necessary` **(Defensive Guards)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 110 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 109`, `args: 16`, `func_start: 36`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 9`, `state_mutation: 129`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 15`
* *Defense:* `safety: 48`, `doc: 43`, `test: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` Utils::Output::Mixin, abstract_command, cask_loader, migrator, cleanup, description_cache_store, descriptions, update-report...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/pypi.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.656)
- **Top Global Matches:** file_cluster_4: 7.656, file_cluster_6: 9.687, file_cluster_15: 13.73
- **Magnitude:** 665.8 | **LOC:** 534 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 0.504; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (55.1%)
- **Documentation Coverage:** 13.0435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_python_resources!` **(Many-Argument Workhorses)** (Impact: 317.5)
  * `basic_metadata` **(Defensive Guards)** (Impact: 26.7)
  * `pypi_info` **(Compute Cores)** (Impact: 21.2)
  * `pip_report` **(Compute Cores)** (Impact: 12.9)
  * `resource_blocks_from_formula` **(Compute Cores)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 50`, `args: 10`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 81`
* *Architecture:* `io: 16`, `api: 6`, `import: 6`
* *Defense:* `safety: 25`, `doc: 19`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.000181 | `Ripple Effect (Closeness):` 0.00285
  * `Imports (Out-Degree: 4):` Utils::Output::Mixin, formula, ast, inreplace, output
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.027)
- **Top Global Matches:** file_cluster_0: 8.027, file_cluster_15: 8.922, file_cluster_16: 9.214
- **Magnitude:** 661.02 | **LOC:** 1329 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **54**; blast radius 0.471; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.8%), Mutation Surface (formerly State Flux) (49.7%), Guard Balance (formerly Safety Score) (49.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch_bottle` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `load_formula_json` **(Stateful Encapsulated Methods)** (Impact: 35.3)
  * `download_http_url` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `resolve_bottle` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `start` **(Compute Cores)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 235`, `args: 132`, `func_start: 66`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 31`
* *Architecture:* `io: 9`, `api: 58`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 27`, `test: 50`, `sync_locks: 18`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.081899
  * `Imports (Out-Degree: 4):` anyhow::Context, anyhow::anyhow, anyhow::bail, crate::BrewResult, crate::delegate, crate::homebrew, crate::utils::tty, rayon::prelude::*...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Library/Homebrew/cask/caskroom.rb` (RUBY) | Magnitude: 29.56 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 16, doc: 9, branch: 8
- `Library/Homebrew/services/formulae.rb` (RUBY) | Magnitude: 16.54 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, class_start: 3, state_mutation: 3
- `Library/Homebrew/extend/os/linux/dev-cmd/bottle.rb` (RUBY) | Magnitude: 20.24 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, state_mutation: 5, class_start: 4
- `Library/Homebrew/test_bot/test.rb` (RUBY) | Magnitude: 58.4 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 18, doc: 12, state_mutation: 10
- `Library/Homebrew/unpack_strategy/ttf.rb` (RUBY) | Magnitude: 7.68 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, func_start: 2, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Library/Homebrew/rubocops/cask/stanza_order.rb` (RUBY) | Magnitude: 44.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 14, state_mutation: 9, core_var_decl: 8
- `Library/Homebrew/test/support/fixtures/cask/Casks/with-uninstall-script-user-relative.rb` (RUBY) | Magnitude: 0.0 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, io: 3, bitwise_ops: 3, closures: 2
- `Library/Homebrew/test/support/fixtures/cask/Casks/placeholders.rb` (RUBY) | Magnitude: 0.0 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, io: 1, closures: 1
- `Library/Homebrew/cmd/--repository.rb` (RUBY) | Magnitude: 3.26 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, class_start: 3, high_risk_execution: 2
- `Library/Homebrew/test/cask/artifact/generated_completion_spec.rb` (RUBY) | Magnitude: 34.84 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 90, test: 31, closures: 18, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Library/Homebrew/cask/dsl/container.rb` (RUBY) | Magnitude: 19.68 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 12, doc: 6, func_start: 4
- `Library/Homebrew/unpack_strategy/executable.rb` (RUBY) | Magnitude: 6.18 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, func_start: 2, class_start: 2
- `Library/Homebrew/os/linux/libstdcxx.rb` (RUBY) | Magnitude: 40.86 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, branch: 10, structural_boundaries: 9, state_mutation: 7
- `Library/Homebrew/cask/dsl/conflicts_with.rb` (RUBY) | Magnitude: 10.4 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, func_start: 3, class_start: 3
- `Library/Homebrew/extend/os/linux/diagnostic.rb` (RUBY) | Magnitude: 92.82 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 49, branch: 36, func_start: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Library/Homebrew/livecheck/strategy/yaml.rb` (RUBY) | Magnitude: 59.38 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 17, doc: 16, branch: 11
- `Library/Homebrew/rubocops/dependency_order.rb` (RUBY) | Magnitude: 109.46 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 35, core_var_decl: 26, design_snake_case: 26
- `Library/Homebrew/test/test_bot/test_formulae_spec.rb` (RUBY) | Magnitude: 12.86 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, closures: 7, test: 5, structural_boundaries: 3
- `Library/Homebrew/on_system.rb` (RUBY) | Magnitude: 121.42 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 133, branch: 30, structural_boundaries: 25, state_mutation: 23
- `Library/Homebrew/formula_info.rb` (RUBY) | Magnitude: 39.84 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 17, doc: 11, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Library/Homebrew/cask/macos.rb` (RUBY) | Magnitude: 12.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 381, bitwise_ops: 135, structural_boundaries: 8, encapsulation: 5
- `Library/Homebrew/hardware.rb` (RUBY) | Magnitude: 132.04 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 223, branch: 57, structural_boundaries: 40, doc: 29
- `Library/Homebrew/extend/ENV.rb` (RUBY) | Magnitude: 20.84 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 21, func_start: 5, doc: 5
- `Library/Homebrew/options.rb` (RUBY) | Magnitude: 103.54 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 52, doc: 31, func_start: 28
- `Library/Homebrew/shims/utils.sh` (SHELL) | Magnitude: 77.24 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 51, core_var_decl: 18, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Library/Homebrew/test/support/lib/startup/config.rb` (RUBY) | Magnitude: 10.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 28, safety: 27, design_upper_case: 27, immutability_locks: 21
- `Library/Homebrew/shims/mac/super/make` (SHELL) | Magnitude: 3.0 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, api: 1, doc: 1
- `Library/Homebrew/startup/ruby_path.rb` (RUBY) | Magnitude: 1.24 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: safety: 2, immutability_locks: 2, core_var_decl: 2, design_upper_case: 2
- `Library/Homebrew/rubocops/all.rb` (RUBY) | Magnitude: 4.24 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 46, import: 42
- `Library/Homebrew/rust/brew-rs/src/commands/mod.rs` (RUST) | Magnitude: 23.68 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Library/Homebrew/extend/os/mac/utils/socket.rb` (RUBY) | Magnitude: 7.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, class_start: 4, branch: 1
- `Library/Homebrew/test.rb` (RUBY) | Magnitude: 54.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 22, branch: 17, import: 14
- `Library/Homebrew/test/support/fixtures/cask/Casks/hockeyapp-without-livecheck.rb` (RUBY) | Magnitude: 0.0 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 6, branch: 1, closures: 1, sec_entropy: 1
- `Library/Homebrew/shims/mac/super/ruby` (SHELL) | Magnitude: 6.46 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, branch: 2, args: 2, api: 1
- `Library/Homebrew/shims/mac/super/swift` (SHELL) | Magnitude: 6.36 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, branch: 2, args: 2, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Library/Homebrew/bundle/brew.rb` (RUBY) | Magnitude: 552.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 464, branch: 141, structural_boundaries: 116, state_mutation: 89
- `Library/Homebrew/bottle.rb` (RUBY) | Magnitude: 243.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 207, structural_boundaries: 53, doc: 34, state_mutation: 29
- `Library/Homebrew/cli/named_args.rb` (RUBY) | Magnitude: 443.14 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 488, branch: 123, safety: 69, structural_boundaries: 63
- `Library/Homebrew/dev-cmd/contributions.rb` (RUBY) | Magnitude: 232.28 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 241, branch: 68, state_mutation: 46, core_var_decl: 45
- `Library/Homebrew/github_packages.rb` (RUBY) | Magnitude: 449.34 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 453, core_var_decl: 91, state_mutation: 79, design_snake_case: 78

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `Library/Homebrew/unpack_strategy/uncompressed.rb` (RUBY) | Magnitude: 14.2 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 7, func_start: 4, api: 4
- `Library/Homebrew/lazy_object.rb` (RUBY) | Magnitude: 29.94 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, state_mutation: 8, func_start: 6
- `Library/Homebrew/cask/artifact.rb` (RUBY) | Magnitude: 3.76 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 32, import: 30, indent_spaces: 21, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `package/scripts/postinstall` (SHELL) | Magnitude: 54.2 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 70, indent_spaces: 29, core_var_decl: 14, branch: 12
- `Library/Homebrew/ignorable.rb` (RUBY) | Magnitude: 14.78 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, panics_and_aborts: 6, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Library/Homebrew/dev-cmd/generate-cask-api.rb` (RUBY) | Magnitude: 52.06 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 15, core_var_decl: 15, design_snake_case: 14
- `Library/Homebrew/rubocops/deprecate_disable.rb` (RUBY) | Magnitude: 50.88 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 66, branch: 12, structural_boundaries: 12, state_mutation: 11
- `Library/Homebrew/language/perl.rb` (RUBY) | Magnitude: 19.5 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 6, branch: 5, core_var_decl: 4
- `Library/Homebrew/dev-cmd/generate-formula-api.rb` (RUBY) | Magnitude: 51.06 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 14, core_var_decl: 14, design_snake_case: 13
- `Library/Homebrew/os/linux/ld.rb` (RUBY) | Magnitude: 107.9 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 88, state_mutation: 22, branch: 21, structural_boundaries: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Library/Homebrew/dev-cmd/bump.rb` -> Churn: **80.68%** | Cog Load: 63.6252% | Debt: 0.0%
- `Library/Homebrew/brew.sh` -> Churn: **80.33%** | Cog Load: 66.44% | Debt: 12.5569%
- `Library/Homebrew/bundle/commands/cleanup.rb` -> Churn: **74.71%** | Cog Load: 84.9535% | Debt: 9.7637%
- `Library/Homebrew/formula_auditor.rb` -> Churn: **69.06%** | Cog Load: 79.3402% | Debt: 8.3508%
- `bin/brew` -> Churn: **61.07%** | Cog Load: 70.2694% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Library/Homebrew/version.rb` -> **Michael Cho** (100.0% isolated ownership) | Magnitude: 631.04
- `Library/Homebrew/dev-cmd/bottle.rb` -> **Douglas Eichelberger** (100.0% isolated ownership) | Magnitude: 599.98
- `Library/Homebrew/service.rb` -> **Paul** (85.7% isolated ownership) | Magnitude: 598.02
- `Library/Homebrew/bundle/brew.rb` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 552.7
- `Library/Homebrew/bundle/extensions/flatpak.rb` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 444.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Library/Homebrew/formula.rb` -> **Severity: 6.218** (Bridge: 0.0622 * Flux: 99.9889%)
- `Library/Homebrew/tap.rb` -> **Severity: 3.594** (Bridge: 0.0359 * Flux: 99.9999%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 2.719** (Bridge: 0.0272 * Flux: 100.0%)
- `Library/Homebrew/cask/cask.rb` -> **Severity: 2.091** (Bridge: 0.0209 * Flux: 99.9908%)
- `Library/Homebrew/formula_installer.rb` -> **Severity: 1.852** (Bridge: 0.0185 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Library/Homebrew/env_config.rb` -> **Severity: 16.617** (Embedded: 0.1677 * Error Risk: 99.0959%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 16.161** (Embedded: 0.239 * Error Risk: 67.6267%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 13.932** (Embedded: 0.1639 * Error Risk: 84.9916%)
- `Library/Homebrew/cache_store.rb` -> **Severity: 13.87** (Embedded: 0.1734 * Error Risk: 80.0%)
- `Library/Homebrew/utils.rb` -> **Severity: 13.347** (Embedded: 0.2167 * Error Risk: 61.591%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Library/Homebrew/standalone/sorbet.rb` -> **Severity: 3061.6** (Blast Radius: 30.616 * Doc Risk: 100.0%)
- `Library/Homebrew/utils/popen.rb` -> **Severity: 1777.2** (Blast Radius: 17.772 * Doc Risk: 100.0%)
- `Library/Homebrew/formula.rb` -> **Severity: 1155.491** (Blast Radius: 40.957 * Doc Risk: 28.2123%)
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> **Severity: 584.1** (Blast Radius: 5.841 * Doc Risk: 100.0%)
- `Library/Homebrew/rust/brew-rs/src/lib.rs` -> **Severity: 575.5** (Blast Radius: 5.755 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1541 literal sites + 24 sites through wrappers = 1565

- `parse` (function, debug_prints, primitive): 4 call sites in 1 files -- `Library/Homebrew/PATH.rb`
- `timestamped_versions` (function, debug_prints, primitive): 4 call sites in 1 files -- `Library/Homebrew/cask/cask.rb`
- `exec_editor` (function, debug_prints, primitive): 3 call sites in 3 files -- `Library/Homebrew/extend/kernel.rb`
- `print_cask_cache` (function, debug_prints, primitive): 3 call sites in 1 files -- `Library/Homebrew/cmd/--cache.rb`
- `log` (function, debug_prints, primitive): 2 call sites in 1 files -- `Library/Homebrew/mcp_server.rb`
- `remove_nonexistent` (function, debug_prints, primitive): 2 call sites in 1 files -- `Library/Homebrew/cask/staged.rb`
- `replace_uuids` (function, debug_prints, primitive): 2 call sites in 1 files -- `Library/Homebrew/dev-cmd/generate-zap.rb`
- `homebrew_config` (function, debug_prints, primitive): 1 call sites in 1 files -- `Library/Homebrew/system_config.rb`
- `host_software_config` (function, debug_prints, primitive): 1 call sites in 1 files -- `Library/Homebrew/system_config.rb`
- `print_tap_json` (function, debug_prints, primitive): 1 call sites in 1 files -- `Library/Homebrew/cmd/tap-info.rb`
- `stdout_print_and_flush` (function, debug_prints, primitive): 1 call sites in 1 files -- `Library/Homebrew/download_queue.rb`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 69103 call pairs -- scoped 21.9%, unique 2.2%, ambiguous 32.0%, external 43.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| ruby | 67478 | 22.0% | 2.2% | 32.8% | 43.1% |
| rust | 1003 | 17.7% | 0.0% | 0.1% | 82.2% |
| shell | 505 | 26.1% | 2.4% | 3.6% | 67.9% |
| javascript | 115 | 11.3% | 0.0% | 0.0% | 88.7% |
| swift | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
