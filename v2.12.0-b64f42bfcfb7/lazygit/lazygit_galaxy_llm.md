# ARCHITECTURAL_BRIEF: lazygit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jesseduffield/lazygit.git` |
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
- **Scope:** 1006 analyzed artifact(s), 100223 LOC.
- **Load-bearing artifact:** `pkg/config/app_config.go` -- 511 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/gui/gui.go` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pkg/i18n/english.go` at magnitude 1132.34 (structural weight, not risk).
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
| Total Artifacts | 2113 |
| Analyzed Artifacts (Scanned) | 1006 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1107 |
| Total LOC | 100223 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 47.6% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5814 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3998 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3277 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 54 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 939 | 95162 | 93.3% |
| MARKDOWN | 31 | 0 | 3.1% |
| SHELL | 13 | 168 | 1.3% |
| YAML | 11 | 539 | 1.1% |
| JSON | 7 | 4165 | 0.7% |
| NIX | 3 | 124 | 0.3% |
| DOCKERFILE | 1 | 13 | 0.1% |
| MAKEFILE | 1 | 52 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1006 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 47%, Callbacks & Closures Files 25%, Large Core Modules 7%, Data / Markup / Trivial 6%, Large Core Modules (3) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 975 | 96.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 31 | 3.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1107*

**Composition by Extension & Reason:**
- `.go`: 794x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 495 LOC)
- `.md`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Machine-Generated Source Code Signature: 420 LOC)
- `no_extension`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.s`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1054 LOC), 1x Excluded (Static Asset Blob without Intent: 2049 LOC)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bash`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 1x Unsupported Format (.mod)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 6.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.1 | 21.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.2 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.9 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 308 | 119 | 1 | `pkg/gui/presentation/graph/graph.go` |
| cleanup | 44 | 29 | 0 | `pkg/updates/updates.go` |
| guards | 2374 | 334 | 7 | `pkg/gui/controllers/files_controller.go` |
| danger | 459 | 100 | 0 | `pkg/app/entry_point.go` |
| concurrency | 382 | 78 | 0 | `pkg/tasks/tasks.go` |
| connectivity | 6235 | 909 | 13 | `pkg/i18n/english.go` |
| io | 138 | 46 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 11 | 0 | `pkg/gui/controllers/helpers/signal_handling.go` |
| time | 69 | 37 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| serialization | 6 | 4 | 0 | `pkg/app/daemon/daemon.go` |
| regex | 50 | 30 | 0 | `scripts/check_for_fixups.sh` |
| events | 29 | 10 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| tests | 1366 | 566 | 1 | `pkg/commands/hosting_service/hosting_service_test.go` |
| docs | 1696 | 366 | 4 | `pkg/config/user_config.go` |
| debt | 845 | 104 | 1 | `pkg/utils/rebase_todo_test.go` |
| mutation | 5120 | 788 | 14 | `pkg/gui/views.go` |
| dead_code | 2021 | 450 | 6 | `pkg/integration/components/shell.go` |
| credential | 65 | 1 | 0 | `pkg/i18n/translations/ja.json` |
| threat | 1 | 1 | 0 | `pkg/commands/models/commit.go` |
| ml_ai | 9 | 6 | 0 | `pkg/gui/controllers/workspace_reset_controller.go` |
| ui | 7 | 7 | 0 | `pkg/gui/controllers/helpers/refs_helper.go` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pkg/commands/oscommands/cmd_obj_runner.go` (Hits: 13)
- `demo/record_demo.sh` (Hits: 13)
- `scripts/bisect.sh` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app_config.go** (`pkg/config/app_config.go`) — 511 inbound connections
2. **alert_driver.go** (`pkg/integration/components/alert_driver.go`) — 472 inbound connections
3. **common.go** (`pkg/gui/types/common.go`) — 160 inbound connections
4. **author.go** (`pkg/commands/models/author.go`) — 118 inbound connections
5. **utils.go** (`pkg/utils/utils.go`) — 114 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gui.go** (`pkg/gui/gui.go`) — 48 outbound dependencies
2. **README.md** (`README.md`) — 22 outbound dependencies
3. **app.go** (`pkg/app/app.go`) — 22 outbound dependencies
4. **entry_point.go** (`pkg/app/entry_point.go`) — 22 outbound dependencies
5. **refresh_helper.go** (`pkg/gui/controllers/helpers/refresh_helper.go`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getBoxDrawingChars` **(Compute Cores)** (@ `pkg/gui/presentation/graph/cell.go`) -> Impact: **180.7** | LOC: 37
- `displayCommit` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/commits.go`) -> Impact: **125.3** | LOC: 115
- `getBranchDisplayStrings` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/branches.go`) -> Impact: **113.1** | LOC: 140
  * *Intent:* // getBranchDisplayStrings returns the display string of branch
- `GetCommitListDisplayStrings` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/commits.go`) -> Impact: **100.1** | LOC: 171
- `NewCmdTask` **(Many-Argument Workhorses)** (@ `pkg/tasks/tasks.go`) -> Impact: **95.6** | LOC: 213
- `renderPipeSet` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/graph/graph.go`) -> Impact: **69.2** | LOC: 103
- `layout` **(Compute Cores)** (@ `pkg/gui/layout.go`) -> Impact: **68.9** | LOC: 191
  * *Intent:* // layout is called for every screen re-render e.g. when the screen is resized
- `renderLayout` **(Compute Cores)** (@ `pkg/gui/controllers/helpers/window_arrangement_helper_test.go`) -> Impact: **68.2** | LOC: 147
- `getNextPipes` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/graph/graph.go`) -> Impact: **66.2** | LOC: 165
- `getFileLine` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/files.go`) -> Impact: **59.0** | LOC: 71

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pkg/gui/controllers` | 64 | 3971.84 | 8.13% | 54.93% |
| `pkg/commands/git_commands` | 58 | 3872.16 | 13.45% | 67.23% |
| `pkg/gui/controllers/helpers` | 43 | 3342.46 | 13.31% | 66.22% |
| `pkg/gui` | 25 | 2028.02 | 22.74% | 62.76% |
| `pkg/config` | 13 | 1536.62 | 10.76% | 32.02% |
| `pkg/gui/presentation` | 18 | 1484.6 | 25.12% | 32.91% |
| `pkg/integration/components` | 25 | 1469.42 | 5.88% | 74.15% |
| `pkg/gui/context` | 36 | 1450.26 | 9.46% | 78.8% |
| `pkg/utils` | 32 | 1275.98 | 10.05% | 59.32% |
| `pkg/i18n` | 3 | 1206.34 | 4.58% | 28.71% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pkg/commands/git_commands/bisect_info.go` -> **100.0%** Exposure
- `pkg/commands/models/commit.go` -> **100.0%** Exposure
- `pkg/commands/oscommands/cmd_obj.go` -> **100.0%** Exposure
- `pkg/gui/context/filtered_list.go` -> **100.0%** Exposure
- `pkg/gui/context/view_trait.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pkg/config/app_config.go` -> **100.0%** Exposure
- `pkg/config/editor_presets.go` -> **100.0%** Exposure
- `pkg/config/editor_presets_test.go` -> **100.0%** Exposure
- `pkg/config/user_config.go` -> **100.0%** Exposure
- `pkg/gui/controllers/helpers/branches_helper.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/integration/components/shell.go` -> **42** Orphaned Functions | **0** Duplicates
- `pkg/gui/gui.go` -> **37** Orphaned Functions | **0** Duplicates
- `pkg/gui/gui_common.go` -> **36** Orphaned Functions | **0** Duplicates
- `pkg/integration/components/views.go` -> **30** Orphaned Functions | **0** Duplicates
- `pkg/gui/context/base_context.go` -> **28** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3210` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pkg/i18n/english.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.362)
- **Top Global Matches:** file_cluster_2: 5.362, file_cluster_17: 7.143, file_cluster_15: 7.489
- **Magnitude:** 1132.34 | **LOC:** 2264 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 63.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 6.278; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (50.1%), Connectivity (formerly Api Exposure) (18.0%), Concurrency Surface (formerly Concurrency) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EnglishTranslationSet` **(I/O & Config Routines)** (Impact: 11.0)
    * *Intent:* // exporting this so we can use it in tests
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 1`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1073`, `concurrency: 1`
* *Defense:* `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.129622
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/gui.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.139)
- **Top Global Matches:** file_cluster_10: 7.139, file_cluster_15: 7.448, file_cluster_16: 8.417
- **Magnitude:** 535.04 | **LOC:** 1194 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **48**; blast radius 1.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (98.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.9%)
- **Documentation Coverage:** 97.7528% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onNewRepo` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `Run` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* // Run: setup the gui with keybindings and start the mainloop
  * `initialContext` **(Compute Cores)** (Impact: 18.4)
  * `checkForChangedConfigsThatDontAutoReload` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `RunAndHandleError` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 40 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 20
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 146`, `args: 57`, `func_start: 57`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 74`, `planned_debt: 3`, `unreferenced_by_name: 37`
* *Architecture:* `api: 71`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 27`, `doc: 18`, `sync_locks: 11`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.001825 | `Ripple Effect (Closeness):` 0.018657
  * `Imports (Out-Degree: 41):` context, errors, fmt, gocui, boxlayout, types, commands, git_commands...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `pkg/config/user_config.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.276)
- **Top Global Matches:** file_cluster_13: 7.276, file_cluster_10: 8.153, file_cluster_2: 8.348
- **Magnitude:** 517.68 | **LOC:** 1081 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 26.126; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.3%), Guard Balance (formerly Safety Score) (54.0%), Debt Markers (formerly Tech Debt) (26.5%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetDefaultConfig` **(I/O & Config Routines)** (Impact: 3.0)
  * `GetDescription` **(Callbacks & Closures)** (Impact: 2.4)
  * `JSONSchemaExtend` **(Generic / Templated Code)** (Impact: 1.8)
  * `RefreshIntervalDuration` **(Callbacks & Closures)** (Impact: 1.1)
  * `FetchIntervalDuration` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 88`, `args: 6`, `func_start: 6`, `class_start: 34`
* *Risk/State:* `state_mutation: 104`, `planned_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 388`, `import: 1`
* *Defense:* `doc: 206`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.315852
  * `Imports (Out-Degree: 0):` jsonschema, time
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/files_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.39)
- **Top Global Matches:** file_cluster_10: 7.39, file_cluster_15: 7.918, file_cluster_4: 8.515
- **Magnitude:** 502.48 | **LOC:** 1590 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.3%), Mutation Surface (formerly State Flux) (57.4%), Guard Balance (formerly Safety Score) (51.3%)
- **Documentation Coverage:** 97.4684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pressWithLock` **(Defensive Guards)** (Impact: 31.4)
  * `GetOnRenderToMain` **(I/O & Config Routines)** (Impact: 25.9)
  * `toggleStagedAllWithLock` **(Defensive Guards)** (Impact: 16.8)
  * `remove` **(Compute Cores)** (Impact: 15.6)
  * `openCopyMenu` **(I/O & Config Routines)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 244`, `args: 68`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 30`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 40`, `doc: 24`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` errors, fmt, set, gocui, git_commands, models, context, filetree...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/commits.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.958)
- **Top Global Matches:** file_cluster_8: 5.958, file_cluster_6: 14.49, file_cluster_3: 22.867
- **Magnitude:** 490.32 | **LOC:** 533 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.405; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.4%), Debt Markers (formerly Tech Debt) (48.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `displayCommit` **(Many-Argument Workhorses)** (Impact: 125.3)
  * `GetCommitListDisplayStrings` **(Many-Argument Workhorses)** (Impact: 100.1)
  * `getHashColor` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `getBisectStatus` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `getBisectStatusText` **(Compute Cores)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 61`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 41`, `planned_debt: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 4`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.405
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 9):` fmt, set, git_commands, models, common, authors, graph, icons...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/local_commits_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.41)
- **Top Global Matches:** file_cluster_10: 6.41, file_cluster_15: 7.178, file_cluster_16: 8.15
- **Magnitude:** 486.8 | **LOC:** 1560 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 0.518; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.3%), Debt Markers (formerly Tech Debt) (61.4%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revert` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `midRebaseMoveCommandEnabled` **(Compute Cores)** (Impact: 17.4)
    * *Intent:* // Ensures that if we are mid-rebase, we're only selecting commits that can be moved
  * `canDropCommits` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `drop` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `moveFixupCommitToOwnerStackedBranch` **(Compute Cores)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 230`, `args: 71`, `func_start: 71`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 19`, `planned_debt: 44`, `unreferenced_by_name: 4`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 27`, `doc: 18`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.518
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.00199
  * `Imports (Out-Degree: 11):` errors, gocui, git_commands, models, context, traits, helpers, keybindings...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/config/app_config.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.187)
- **Top Global Matches:** file_cluster_4: 6.187, file_cluster_15: 9.238, file_cluster_10: 9.896
- **Magnitude:** 431.04 | **LOC:** 737 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **511** in-repo importer(s); it depends on **14**; blast radius 89.497; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.1%)
- **Documentation Coverage:** 66.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadUserConfig` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `changeCustomCommandStreamAndOutputToOutputEnum` **(Compute Cores)** (Impact: 33.6)
  * `computeMigratedConfig` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* // A pure function helper for testing purposes
  * `NewAppConfig` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* // NewAppConfig makes a new app config
  * `migrateUserConfig` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* // Do any backward-compatibility migrations of things that have changed in the // config over time; ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 108`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 50`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 44`, `import: 1`
* *Defense:* `safety: 32`, `doc: 29`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.497
  * `Choke Point (Betweenness):` 0.002 | `Ripple Effect (Closeness):` 0.536626
  * `Imports (Out-Degree: 3):` errors, fmt, xdg, orderedset, utils, yaml_utils, lo, yaml.v3...
  * `Imported By (In-Degree: 511):` (Excluded from Brief to save tokens)

### `pkg/tasks/tasks.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.333)
- **Top Global Matches:** file_cluster_6: 8.333, file_cluster_4: 9.958, file_cluster_12: 16.313
- **Magnitude:** 393.16 | **LOC:** 432 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 4.525; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewCmdTask` **(Many-Argument Workhorses)** (Impact: 95.6)
  * `NewTask` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `ReadToEnd` **(Callbacks & Closures)** (Impact: 6.1)
  * `Close` **(Callbacks & Closures)** (Impact: 6.0)
    * *Intent:* // Close closes the task manager, killing whatever task may currently be running
  * `NewViewBufferManager` **(Many-Argument Workhorses)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 145
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 52`, `args: 7`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 18`, `concurrency: 25`, `import: 1`
* *Defense:* `safety: 3`, `doc: 16`, `sync_locks: 15`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.525
  * `Choke Point (Betweenness):` 0.000686 | `Ripple Effect (Closeness):` 0.165608
  * `Imports (Out-Degree: 3):` bufio, fmt, gocui, oscommands, utils, go-deadlock, logrus, io...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pkg/commands/git_commands/commit_loader.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.467)
- **Top Global Matches:** file_cluster_4: 6.467, file_cluster_9: 9.388, file_cluster_15: 10.297
- **Magnitude:** 360.2 | **LOC:** 609 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.396; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConflictedCommitImpl` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `getHydratedTodoCommits` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `GetCommits` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* // GetCommits obtains the commits of the current branch
  * `getRebasingCommits` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* // getRebasingCommits obtains the commits that we're in the process of rebasing // git-rebase-todo e...
  * `extractCommitFromLine` **(Many-Argument Workhorses)** (Impact: 19.1)
    * *Intent:* // extractCommitFromLine takes a line from a git log and extracts the hash, message, date, and tag i...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 71`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 38`, `planned_debt: 25`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 15`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 12`, `doc: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.396
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 11):` bytes, fmt, set, models, oscommands, common, utils, lo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/patch_exploring/state.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.93)
- **Top Global Matches:** file_cluster_10: 6.93, file_cluster_15: 7.973, file_cluster_16: 8.777
- **Magnitude:** 333.8 | **LOC:** 439 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.9%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 87.8378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewState` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `SelectPreviousHunk` **(I/O & Config Routines)** (Impact: 8.9)
  * `selectionRangeForCurrentBlockOfChanges` **(I/O & Config Routines)** (Impact: 8.2)
  * `SelectedViewRange` **(Callbacks & Closures)** (Impact: 7.8)
  * `CycleSelection` **(State Mutators)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 31`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `dead_code: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `doc: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` set, gocui, patch, utils, lo, strings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/refresh_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.968)
- **Top Global Matches:** file_cluster_4: 7.968, file_cluster_12: 9.588, file_cluster_10: 10.923
- **Magnitude:** 319.42 | **LOC:** 953 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **17**; blast radius 1.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.8%), Guard Balance (formerly Safety Score) (54.3%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Refresh` **(Compute Cores)** (Impact: 58.2)
  * `refreshStateFiles` **(I/O & Config Routines)** (Impact: 24.5)
  * `refreshBranches` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* // self.refreshStatus is called at the end of this because that's when we can // be sure there is a ...
  * `refreshReflogCommits` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* // the reflogs panel is the only panel where we cache data, in that we only // load entries that hav...
  * `promptForBaseGithubRepo` **(Defensive Guards)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 96`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 21`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 21`, `doc: 16`, `sync_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.256
  * `Choke Point (Betweenness):` 0.000778 | `Ripple Effect (Closeness):` 0.014696
  * `Imports (Out-Degree: 18):` fmt, set, gocui, git_commands, models, config, context, filetree...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pkg/gui/presentation/branches.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.401)
- **Top Global Matches:** file_cluster_6: 7.401, file_cluster_4: 7.798, file_cluster_9: 13.816
- **Magnitude:** 315.82 | **LOC:** 288 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **14**; blast radius 1.533; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (61.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBranchDisplayStrings` **(Many-Argument Workhorses)** (Impact: 113.1)
    * *Intent:* // getBranchDisplayStrings returns the display string of branch
  * `BranchStatus` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `divergenceStr` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `prColor` **(Compute Cores)** (Impact: 10.6)
  * `match` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.533
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.036344
  * `Imports (Out-Degree: 11):` fmt, git_commands, models, config, icons, style, types, i18n...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `pkg/commands/git_commands/working_tree.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.207)
- **Top Global Matches:** file_cluster_10: 7.207, file_cluster_15: 7.365, file_cluster_12: 8.183
- **Magnitude:** 307.7 | **LOC:** 610 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.3%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DiscardAllDirChanges` **(Compute Cores)** (Impact: 28.5)
  * `WorktreeFileDiffCmdObj` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* // WorktreeFileDiffCmdObj returns a command object for diffing a file or directory // in the working...
  * `DiscardAllFileChanges` **(Defensive Guards)** (Impact: 24.1)
    * *Intent:* // DiscardAllFileChanges directly
  * `removeEmptyDirs` **(Defensive Guards)** (Impact: 20.7)
    * *Intent:* // Removes empty directories left behind after deleting files, but only for directories that // are ...
  * `ShowFileDiffCmdObj` **(Many-Argument Workhorses)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 98`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `unreferenced_by_name: 25`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `safety: 20`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.627
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.010205
  * `Imports (Out-Degree: 6):` fmt, errors, set, models, oscommands, lo, os, path...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pkg/gui/presentation/files.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.489)
- **Top Global Matches:** file_cluster_4: 5.489, file_cluster_15: 9.917, file_cluster_9: 10.662
- **Magnitude:** 303.22 | **LOC:** 349 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFileLine` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `getCommitFileLine` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `renderAux` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `fileNameAtDepth` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `getColorForChangeStatus` **(Compute Cores)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 34`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 37`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.389
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 8):` color, models, patch, config, filetree, icons, style, theme...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/branches_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.197)
- **Top Global Matches:** file_cluster_10: 6.197, file_cluster_15: 6.772, file_cluster_16: 7.853
- **Magnitude:** 300.98 | **LOC:** 987 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (68.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.7%), Guard Balance (formerly Safety Score) (52.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `viewUpstreamOptions` **(Compute Cores)** (Impact: 25.5)
  * `delete` **(Compute Cores)** (Impact: 16.0)
  * `createPullRequestMenu` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `withPrFgColor` **(Compute Cores)** (Impact: 12.8)
  * `withPrBgColor` **(Compute Cores)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 134`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 13`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` errors, fmt, color, gocui, git_commands, models, context, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/graph/cell.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.735)
- **Top Global Matches:** file_cluster_4: 8.735, file_cluster_6: 11.082, file_cluster_12: 13.542
- **Magnitude:** 293.7 | **LOC:** 184 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.448; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.3%), Debt Markers (formerly Tech Debt) (93.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBoxDrawingChars` **(Compute Cores)** (Impact: 180.7)
  * `render` **(I/O & Config Routines)** (Impact: 14.4)
  * `cachedSprint` **(Compute Cores)** (Impact: 11.5)
  * `setRight` **(Callbacks & Closures)** (Impact: 5.5)
    * *Intent:* //nolint:unparam
  * `setLeft` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 28`, `unreferenced_by_name: 8`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `sync_locks: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01033
  * `Imports (Out-Degree: 1):` color, style, io, sync
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/integration/components/view_driver.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.614)
- **Top Global Matches:** file_cluster_10: 5.614, file_cluster_15: 7.41, file_cluster_16: 8.156
- **Magnitude:** 277.6 | **LOC:** 654 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 68.344; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 86.5854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertLines` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `NavigateToLine` **(Compute Cores)** (Impact: 17.5)
    * *Intent:* // this will look for a list item in the current panel and if it finds it, it will // enter the keyp...
  * `ContainsLines` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* // asserts that somewhere in the view there are consecutive lines matching the given matchers.
  * `Focus` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* // focus the view (assumes the view is a side-view)
  * `SelectedLines` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* // asserts on the lines that are selected in the view. Don't use the `IsSelected` matcher with this ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 98`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 30`, `unreferenced_by_name: 18`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 68.344
  * `Choke Point (Betweenness):` 0.018214 | `Ripple Effect (Closeness):` 0.245417
  * `Imports (Out-Degree: 8):` fmt, gocui, lo, strings
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pkg/gui/presentation/graph/graph.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.537)
- **Top Global Matches:** file_cluster_8: 8.537, file_cluster_6: 10.06, file_cluster_4: 18.0
- **Magnitude:** 271.82 | **LOC:** 388 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.477; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (55.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderPipeSet` **(Many-Argument Workhorses)** (Impact: 69.2)
  * `getNextPipes` **(Many-Argument Workhorses)** (Impact: 66.2)
  * `RenderAux` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `equalHashes` **(Compute Cores)** (Impact: 5.6)
  * `RenderCommitGraph` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 42`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.477
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.013858
  * `Imports (Out-Degree: 4):` cmp, set, models, style, utils, lo, runtime, slices...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/helpers/window_arrangement_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.199)
- **Top Global Matches:** file_cluster_4: 6.199, file_cluster_9: 9.855, file_cluster_15: 10.512
- **Magnitude:** 257.66 | **LOC:** 499 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infoSectionChildren` **(Compute Cores)** (Impact: 32.0)
  * `getMidSectionWeights` **(Compute Cores)** (Impact: 18.4)
  * `sidePanelChildren` **(Compute Cores)** (Impact: 18.0)
  * `splitMainPanelSideBySide` **(Compute Cores)** (Impact: 12.2)
  * `GetWindowDimensions` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 29`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 4):` fmt, boxlayout, config, types, utils, slices, maps, math...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/commands/git_commands/rebase.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.522)
- **Top Global Matches:** file_cluster_10: 6.522, file_cluster_15: 6.688, file_cluster_16: 8.32
- **Magnitude:** 253.7 | **LOC:** 591 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.472; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.5%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 68.1159% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DiscardOldFileChanges` **(Defensive Guards)** (Impact: 23.9)
    * *Intent:* // DiscardOldFileChanges discards changes to a file from an old commit
  * `GenericAmend` **(Defensive Guards)** (Impact: 16.9)
  * `GenericMergeOrRebaseAction` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* // GenericMerge takes a commandType of "merge" or "rebase" and a command of "abort", "skip" or "cont...
  * `BeginInteractiveRebaseForCommitRange` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `RewordCommit` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 88`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `state_mutation: 12`, `planned_debt: 17`, `unreferenced_by_name: 24`
* *Architecture:* `api: 34`, `import: 1`
* *Defense:* `safety: 16`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.006525
  * `Imports (Out-Degree: 11):` fmt, errors, daemon, models, oscommands, utils, lo, todo...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pkg/integration/components/shell.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.307)
- **Top Global Matches:** file_cluster_10: 6.307, file_cluster_15: 8.249, file_cluster_12: 9.068
- **Magnitude:** 243.86 | **LOC:** 526 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.545; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.7%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 88.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CopyFile` **(Defensive Guards)** (Impact: 12.0)
  * `CreateRepoHistory` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* // This creates a repo history of commits // It uses a branching strategy where each feature branch ...
  * `CreateFile` **(Defensive Guards)** (Impact: 6.0)
  * `RunShellCommand` **(Defensive Guards)** (Impact: 5.2)
  * `CreateNCommitsStartingAt` **(Callbacks & Closures)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 73`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 13`, `unreferenced_by_name: 42`
* *Architecture:* `io: 3`, `api: 60`, `import: 1`
* *Defense:* `safety: 13`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.545
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.002239
  * `Imports (Out-Degree: 1):` fmt, io, rand, os, exec, filepath, runtime, time
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/helpers/fixup_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.823)
- **Top Global Matches:** file_cluster_6: 5.823, file_cluster_4: 11.721, file_cluster_8: 13.556
- **Magnitude:** 236.2 | **LOC:** 413 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.1%)
- **Documentation Coverage:** 78.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blameAddedLines` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `parseDiff` **(Compute Cores)** (Impact: 27.9)
    * *Intent:* // Parse the diff output into hunks, and return two lists of hunks: the first // are ones that conta...
  * `HandleFindBaseCommitForFixupPress` **(I/O & Config Routines)** (Impact: 20.2)
  * `IsFixupCommit` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* // Check whether the given subject line is the subject of a fixup commit, and // returns (trimmedSub...
  * `removeFixupCommits` **(Compute Cores)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 55`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 6`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 5):` errors, fmt, set, models, types, utils, lo, errgroup...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/commands/oscommands/cmd_obj_runner.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.69)
- **Top Global Matches:** file_cluster_12: 7.69, file_cluster_10: 8.229, file_cluster_15: 8.877
- **Magnitude:** 234.02 | **LOC:** 476 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.4%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runAndStreamAux` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `RunAndProcessLines` **(Defensive Guards)** (Impact: 19.9)
  * `processOutput` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `getCheckForCredentialRequestFunc` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* // having a function that returns a function because we need to maintain some state inbetween calls ...
  * `getCredentialPromptFn` **(Callbacks & Closures)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`, `api: 16`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 12`, `doc: 5`, `sync_locks: 25`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000995
  * `Imports (Out-Degree: 3):` bufio, bytes, errors, utils, go-deadlock, logrus, io, exec...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/helpers/window_arrangement_helper_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.163)
- **Top Global Matches:** file_cluster_3: 7.163, file_cluster_8: 20.669, file_cluster_6: 33.462
- **Magnitude:** 226.98 | **LOC:** 730 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%), Complexity Load (formerly Cognitive Load) (19.5%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderLayout` **(Compute Cores)** (Impact: 68.2)
  * `TestGetWindowDimensions` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* // The best way to add test cases here is to set your args and then get the // test to fail and copy...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 16`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cmp, fmt, boxlayout, config, types, lo, slices, strings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/clients/tui.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.309)
- **Top Global Matches:** file_cluster_4: 7.309, file_cluster_10: 10.434, file_cluster_15: 10.661
- **Magnitude:** 226.0 | **LOC:** 409 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (75.1%), Guard Balance (formerly Safety Score) (54.3%), Debt Markers (formerly Tech Debt) (10.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RunTUI` **(Defensive Guards)** (Impact: 55.1)
  * `layout` **(Defensive Guards)** (Impact: 25.2)
  * `suspendAndRunTest` **(Defensive Guards)** (Impact: 8.0)
  * `runTuiTest` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `filterWithString` **(Callbacks & Closures)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 48`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 19`, `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 36`, `doc: 1`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` errors, fmt, gocui, utils, gui, style, components, tests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `pkg/integration/tests/branch/reset_to_duplicate_named_tag.go` (GO) | Magnitude: 16.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 39, closures: 3, structural_boundaries: 2, pointers: 2
- `pkg/integration/tests/interactive_rebase/move_across_branch_boundary_outside_rebase.go` (GO) | Magnitude: 16.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 39, closures: 3, structural_boundaries: 2, pointers: 2
- `pkg/integration/tests/staging/select_next_line_after_staging_isolated_added_line.go` (GO) | Magnitude: 16.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 39, closures: 3, structural_boundaries: 2, pointers: 2
- `pkg/integration/tests/sync/pull_rebase.go` (GO) | Magnitude: 16.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 39, closures: 3, structural_boundaries: 2, pointers: 2
- `pkg/integration/tests/file/discard_unstaged_dir_changes_when_filtering.go` (GO) | Magnitude: 17.28 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 59, closures: 5, structural_boundaries: 2, pointers: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `.github/workflows/ci.yml` (YAML) | Magnitude: 58.72 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 207, structural_boundaries: 27, branch: 25, args: 19
- `pkg/gui/types/search_state.go` (GO) | Magnitude: 16.08 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 9, api: 9, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/commands/patch/format.go` (GO) | Magnitude: 52.58 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 22, branch: 14, pointers: 9
- `pkg/gui/recent_repos_panel.go` (GO) | Magnitude: 18.12 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 8, branch: 5, args: 2
- `pkg/gui/presentation/graph/graph_test.go` (GO) | Magnitude: 85.72 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 563, pointers: 71, structural_boundaries: 23, branch: 14
- `pkg/gui/controllers/helpers/credentials_helper.go` (GO) | Magnitude: 34.34 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 16, branch: 6, pointers: 6
- `pkg/gui/controllers/helpers/cherry_pick_helper.go` (GO) | Magnitude: 51.38 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 21, branch: 16, pointers: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pkg/integration/tests/bisect/skip.go` (GO) | Magnitude: 17.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 78, closures: 7, doc: 4, structural_boundaries: 2
- `pkg/integration/tests/commit/search.go` (GO) | Magnitude: 19.04 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 147, closures: 15, structural_boundaries: 2, pointers: 2
- `pkg/integration/tests/file/stage_deleted_range_select.go` (GO) | Magnitude: 16.98 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 44, structural_boundaries: 4, closures: 3, doc: 2
- `pkg/integration/tests/patch_building/move_to_index_part_of_adjacent_added_lines.go` (GO) | Magnitude: 17.16 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 53, closures: 4, structural_boundaries: 3, pointers: 2
- `pkg/integration/tests/demo/rebase_onto.go` (GO) | Magnitude: 17.3 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 60, closures: 5, structural_boundaries: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pkg/commands/git_commands/status.go` (GO) | Magnitude: 35.18 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 19, pointers: 11, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/utils/yaml_utils/yaml_utils_test.go` (GO) | Magnitude: 89.96 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 313, branch: 27, test: 27, structural_boundaries: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pkg/gui/gui.go` -> Churn: **76.86%** | Cog Load: 40.7817% | Debt: 98.2836%
- `pkg/gui/controllers/local_commits_controller.go` -> Churn: **73.35%** | Cog Load: 8.3538% | Debt: 61.4384%
- `pkg/commands/git_commands/working_tree.go` -> Churn: **72.31%** | Cog Load: 14.0096% | Debt: 95.2325%
- `pkg/gui/background.go` -> Churn: **64.96%** | Cog Load: 67.0924% | Debt: 44.7711%
- `pkg/gui/menu_panel.go` -> Churn: **58.48%** | Cog Load: 54.9858% | Debt: 74.4868%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pkg/gui/presentation/commits.go` -> **Jesse Duffield** (100.0% isolated ownership) | Magnitude: 490.32
- `pkg/config/app_config.go` -> **Jesse Duffield** (100.0% isolated ownership) | Magnitude: 431.04
- `pkg/gui/patch_exploring/state.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 333.8
- `pkg/gui/controllers/branches_controller.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 300.98
- `pkg/commands/git_commands/rebase.go` -> **Jesse Duffield** (100.0% isolated ownership) | Magnitude: 253.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pkg/integration/components/view_driver.go` -> **Severity: 1.821** (Bridge: 0.0182 * Flux: 100.0%)
- `pkg/commands/patch/patch.go` -> **Severity: 0.681** (Bridge: 0.0069 * Flux: 98.6814%)
- `pkg/integration/components/alert_driver.go` -> **Severity: 0.63** (Bridge: 0.0185 * Flux: 34.1028%)
- `pkg/commands/patch/format.go` -> **Severity: 0.368** (Bridge: 0.0042 * Flux: 88.1182%)
- `pkg/integration/components/test_test.go` -> **Severity: 0.234** (Bridge: 0.0126 * Flux: 18.5607%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pkg/config/app_config.go` -> **Severity: 29.98** (Embedded: 0.5366 * Error Risk: 55.8672%)
- `pkg/integration/components/alert_driver.go` -> **Severity: 23.148** (Embedded: 0.4564 * Error Risk: 50.7142%)
- `pkg/utils/utils.go` -> **Severity: 20.73** (Embedded: 0.4077 * Error Risk: 50.851%)
- `pkg/config/user_config.go` -> **Severity: 17.063** (Embedded: 0.3159 * Error Risk: 54.0221%)
- `pkg/utils/yaml_utils/yaml_utils.go` -> **Severity: 16.965** (Embedded: 0.3152 * Error Risk: 53.8223%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pkg/integration/components/alert_driver.go` -> **Severity: 7187.7** (Blast Radius: 71.877 * Doc Risk: 100.0%)
- `pkg/integration/components/view_driver.go` -> **Severity: 5917.593** (Blast Radius: 68.344 * Doc Risk: 86.5854%)
- `pkg/config/app_config.go` -> **Severity: 5906.802** (Blast Radius: 89.497 * Doc Risk: 66.0%)
- `pkg/utils/utils.go` -> **Severity: 3775.68** (Blast Radius: 47.196 * Doc Risk: 80.0%)
- `pkg/gui/types/common.go` -> **Severity: 2163.001** (Blast Radius: 32.445 * Doc Risk: 66.6667%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14361 call pairs -- scoped 21.1%, unique 4.5%, ambiguous 40.5%, external 33.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 14324 | 21.1% | 4.5% | 40.6% | 33.8% |
| shell | 37 | 8.1% | 0.0% | 0.0% | 91.9% |

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
