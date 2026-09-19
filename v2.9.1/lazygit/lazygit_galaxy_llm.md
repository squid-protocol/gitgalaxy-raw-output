# ARCHITECTURAL_BRIEF: lazygit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jesseduffield/lazygit.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 985 analyzed artifact(s), 97028 LOC.
- **Load-bearing artifact:** `pkg/gui/services/custom_commands/models.go` -- 117 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/gui/presentation/icons/file_icons.go` -- pulls in 723 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pkg/integration/components/random.go` at magnitude 1491.04 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 985 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1128 |
| Total LOC | 97028 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 46.6% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4674 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.306 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1485 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 934 | 92442 | 94.8% |
| MARKDOWN | 24 | 0 | 2.4% |
| SHELL | 13 | 168 | 1.3% |
| JSON | 7 | 4165 | 0.7% |
| NIX | 3 | 124 | 0.3% |
| YAML | 2 | 64 | 0.2% |
| DOCKERFILE | 1 | 13 | 0.1% |
| MAKEFILE | 1 | 52 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.219`
> **Composition Archetype:** `Hub-Coupled App` (z +3.22; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 49%, Callbacks & Closures Files 20%, Encapsulated Accessors Files 8%, Large Core Modules 6%, Data / Markup / Trivial 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 961 | 97.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1128*

**Composition by Extension & Reason:**
- `.go`: 795x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 242 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2264 LOC)
- `.md`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Machine-Generated Source Code Signature: 420 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1213 LOC)
- `no_extension`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.s`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 6.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 24.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.4 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.0 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 95.2 | 6.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6702 | 848 | 19 | `pkg/integration/components/shell.go` |
| cleanup | 43 | 28 | 0 | `pkg/updates/updates.go` |
| guards | 2340 | 329 | 7 | `pkg/gui/controllers/files_controller.go` |
| danger | 419 | 94 | 0 | `pkg/app/entry_point.go` |
| concurrency | 378 | 74 | 0 | `pkg/tasks/tasks.go` |
| connectivity | 5138 | 900 | 13 | `pkg/config/user_config.go` |
| io | 130 | 42 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 11 | 0 | `pkg/gui/controllers/helpers/signal_handling.go` |
| time | 69 | 37 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| serialization | 6 | 4 | 0 | `pkg/app/daemon/daemon.go` |
| regex | 49 | 30 | 0 | `scripts/check_for_fixups.sh` |
| events | 27 | 9 | 0 | `pkg/commands/oscommands/cmd_obj_runner.go` |
| tests | 1364 | 564 | 1 | `pkg/commands/hosting_service/hosting_service_test.go` |
| docs | 1666 | 355 | 4 | `pkg/config/user_config.go` |
| debt | 810 | 98 | 0 | `pkg/utils/rebase_todo_test.go` |
| mutation | 5018 | 780 | 14 | `pkg/gui/views.go` |
| dead_code | 2020 | 447 | 6 | `pkg/gui/gui.go` |
| credential | 65 | 1 | 0 | `pkg/i18n/translations/ja.json` |
| threat | 31 | 9 | 0 | `pkg/jsonschema/generate.go` |
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

1. **models.go** (`pkg/gui/services/custom_commands/models.go`) — 117 inbound connections
2. **utils.go** (`pkg/utils/utils.go`) — 117 inbound connections
3. **gocui.go** (`pkg/theme/gocui.go`) — 100 inbound connections
4. **os.go** (`pkg/commands/oscommands/os.go`) — 55 inbound connections
5. **style.go** (`pkg/theme/style.go`) — 49 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **file_icons.go** (`pkg/gui/presentation/icons/file_icons.go`) — 723 outbound dependencies
2. **gui.go** (`pkg/gui/gui.go`) — 61 outbound dependencies
3. **random.go** (`pkg/integration/components/random.go`) — 52 outbound dependencies
4. **lines_test.go** (`pkg/utils/lines_test.go`) — 32 outbound dependencies
5. **app.go** (`pkg/app/app.go`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getBoxDrawingChars` **(Compute Cores)** (@ `pkg/gui/presentation/graph/cell.go`) -> Impact: **180.7** | LOC: 37
- `displayCommit` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/commits.go`) -> Impact: **125.3** | LOC: 115
- `getBranchDisplayStrings` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/branches.go`) -> Impact: **113.1** | LOC: 140
  * *Intent:* // getBranchDisplayStrings returns the display string of branch
- `GetCommitListDisplayStrings` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/commits.go`) -> Impact: **100.1** | LOC: 171
- `NewCmdTask` **(Many-Argument Workhorses)** (@ `pkg/tasks/tasks.go`) -> Impact: **95.6** | LOC: 213
- `getPreset` **(Many-Argument Workhorses)** (@ `pkg/config/editor_presets.go`) -> Impact: **78.3** | LOC: 126
  * *Intent:* // IF YOU ADD A PRESET TO THIS FUNCTION YOU MUST UPDATE THE `Supported presets` SECTION OF docs/Config.md
- `renderPipeSet` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/graph/graph.go`) -> Impact: **69.2** | LOC: 103
- `layout` **(Compute Cores)** (@ `pkg/gui/layout.go`) -> Impact: **68.9** | LOC: 191
  * *Intent:* // layout is called for every screen re-render e.g. when the screen is resized
- `renderLayout` **(Compute Cores)** (@ `pkg/gui/controllers/helpers/window_arrangement_helper_test.go`) -> Impact: **68.2** | LOC: 147
- `getNextPipes` **(Many-Argument Workhorses)** (@ `pkg/gui/presentation/graph/graph.go`) -> Impact: **66.2** | LOC: 165

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pkg/gui/controllers` | 64 | 3982.94 | 8.15% | 58.46% |
| `pkg/commands/git_commands` | 58 | 3959.66 | 13.63% | 60.56% |
| `pkg/gui/controllers/helpers` | 43 | 3371.86 | 13.39% | 69.44% |
| `pkg/integration/components` | 25 | 2857.62 | 6.13% | 62.66% |
| `pkg/gui` | 25 | 2045.22 | 22.89% | 66.16% |
| `pkg/config` | 13 | 1678.82 | 12.57% | 37.09% |
| `pkg/gui/presentation` | 18 | 1494.2 | 25.13% | 31.56% |
| `pkg/gui/context` | 36 | 1451.66 | 9.47% | 81.46% |
| `pkg/utils` | 32 | 1301.18 | 10.09% | 60.97% |
| `pkg/integration/tests/interactive_rebase` | 60 | 1199.4 | 0.16% | 0.0% |

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
- `pkg/gui/gui.go` -> **37** Orphaned Functions | **0** Duplicates
- `pkg/gui/gui_common.go` -> **36** Orphaned Functions | **0** Duplicates
- `pkg/integration/components/views.go` -> **30** Orphaned Functions | **0** Duplicates
- `pkg/gui/context/base_context.go` -> **28** Orphaned Functions | **0** Duplicates
- `pkg/commands/oscommands/cmd_obj.go` -> **26** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3706` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pkg/integration/components/random.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1491.04 | **LOC:** 498 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **52**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.9%), Debt Markers (formerly Tech Debt) (31.3%), Concurrency Surface (formerly Concurrency) (15.9%), Mutation Surface (formerly State Flux) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 212`, `args: 8`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 3`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 20`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 7`, `doc: 9`, `test: 4`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` resolve-crash, bytes, update-dependencies, aes, cipher, rand, add-readme, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/config/user_config.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 542.68 | **LOC:** 1081 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 61.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.596; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.2%), Guard Balance (formerly Safety Score) (66.1%), Debt Markers (formerly Tech Debt) (27.5%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetDefaultConfig` **(I/O & Config Routines)** (Impact: 6.0)
  * `GetDescription` **(Callbacks & Closures)** (Impact: 2.4)
  * `JSONSchemaExtend` **(Generic / Templated Code)** (Impact: 1.8)
  * `RefreshIntervalDuration` **(Callbacks & Closures)** (Impact: 1.1)
  * `FetchIntervalDuration` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 88`, `args: 6`, `func_start: 6`, `class_start: 34`
* *Risk/State:* `state_mutation: 104`, `planned_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 388`, `import: 1`
* *Defense:* `doc: 206`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` diff-so-fancy, jsonschema, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/gui.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 535.04 | **LOC:** 1194 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 70.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **61**; blast radius 0.818; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (98.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.7528% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onNewRepo` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `Run` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* // Run: setup the gui with keybindings and start the mainloop
  * `initialContext` **(Stateful Encapsulated Methods)** (Impact: 18.4)
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
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 74`, `dead_code: 6`, `planned_debt: 3`, `unreferenced_by_name: 37`
* *Architecture:* `api: 71`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 27`, `doc: 18`, `sync_locks: 11`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.818
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.003659
  * `Imports (Out-Degree: 23):` Git.AutoFetch, Git.AutoRefresh, Refresher.FetchInterval, Refresher.RefreshInterval, Update.Days, Update.Method, branches, commits...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/files_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 503.88 | **LOC:** 1590 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 61.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (57.4%), Guard Balance (formerly Safety Score) (54.2%)
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
* *Structure:* `branch: 171`, `structural_boundaries: 244`, `args: 68`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 30`, `dead_code: 4`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 40`, `doc: 24`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AM, AU, DD, DU, MD, MM, errors, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/commits.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 490.32 | **LOC:** 533 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.626; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `displayCommit` **(Many-Argument Workhorses)** (Impact: 125.3)
  * `GetCommitListDisplayStrings` **(Many-Argument Workhorses)** (Impact: 100.1)
  * `getHashColor` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `getBisectStatus` **(Stateful Encapsulated Methods)** (Impact: 28.3)
  * `getBisectStatusText` **(Stateful Encapsulated Methods)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 61`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 41`, `planned_debt: 12`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 4`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.626
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002929
  * `Imports (Out-Degree: 7):` fmt, set, git_commands, models, common, authors, graph, icons...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/local_commits_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 489.8 | **LOC:** 1560 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.1%), Guard Balance (formerly Safety Score) (51.1%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revert` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `midRebaseMoveCommandEnabled` **(Stateful Encapsulated Methods)** (Impact: 17.4)
    * *Intent:* // Ensures that if we are mid-rebase, we're only selecting commits that can be moved
  * `canDropCommits` **(Stateful Encapsulated Methods)** (Impact: 17.4)
  * `drop` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `moveFixupCommitToOwnerStackedBranch` **(Stateful Encapsulated Methods)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 230`, `args: 71`, `func_start: 71`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 19`, `dead_code: 1`, `planned_debt: 44`, `unreferenced_by_name: 4`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 27`, `doc: 18`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` editKey, errors, gocui, git_commands, models, context, traits, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/config/app_config.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 434.74 | **LOC:** 737 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 66.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadUserConfig` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `computeMigratedConfig` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* // A pure function helper for testing purposes
  * `changeCustomCommandStreamAndOutputToOutputEnum` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `NewAppConfig` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* // NewAppConfig makes a new app config
  * `migrateUserConfig` **(Stateful Encapsulated Methods)** (Impact: 15.8)
    * *Intent:* // Do any backward-compatibility migrations of things that have changed in the // config over time; ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 108`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 50`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 44`, `import: 1`
* *Defense:* `safety: 32`, `doc: 29`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` errors, fmt, xdg, orderedset, utils, yaml_utils, lo, yaml.v3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/tasks/tasks.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 393.16 | **LOC:** 432 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 1.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Concurrency Surface (formerly Concurrency) (85.0%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `dead_code: 3`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 18`, `concurrency: 25`, `import: 1`
* *Defense:* `safety: 3`, `doc: 16`, `sync_locks: 15`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.006652
  * `Imports (Out-Degree: 4):` bufio, fmt, gocui, oscommands, utils, go-deadlock, logrus, io...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pkg/commands/git_commands/commit_loader.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 361.6 | **LOC:** 609 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConflictedCommitImpl` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `getHydratedTodoCommits` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `GetCommits` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* // GetCommits obtains the commits of the current branch
  * `getRebasingCommits` **(Stateful Encapsulated Methods)** (Impact: 21.3)
    * *Intent:* // getRebasingCommits obtains the commits that we're in the process of rebasing // git-rebase-todo e...
  * `extractCommitFromLine` **(Many-Argument Workhorses)** (Impact: 19.1)
    * *Intent:* // extractCommitFromLine takes a line from a git log and extracts the hash, message, date, and tag i...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 71`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 38`, `planned_debt: 25`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 15`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 12`, `doc: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bytes, fmt, set, models, oscommands, common, utils, lo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/patch_exploring/state.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 333.8 | **LOC:** 439 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.9%), Guard Balance (formerly Safety Score) (89.0%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.8378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewState` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `SelectPreviousHunk` **(I/O & Config Routines)** (Impact: 8.9)
  * `selectionRangeForCurrentBlockOfChanges` **(Stateful Encapsulated Methods)** (Impact: 8.2)
  * `SelectedViewRange` **(Callbacks & Closures)** (Impact: 7.8)
  * `CycleSelection` **(State Mutators)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 31`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `dead_code: 3`, `unreferenced_by_name: 23`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `doc: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` set, gocui, patch, utils, lo, strings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/refresh_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 319.42 | **LOC:** 953 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Refresh` **(Compute Cores)** (Impact: 58.2)
  * `refreshStateFiles` **(I/O & Config Routines)** (Impact: 24.5)
  * `refreshBranches` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* // self.refreshStatus is called at the end of this because that's when we can // be sure there is a ...
  * `refreshReflogCommits` **(I/O & Config Routines)** (Impact: 13.0)
    * *Intent:* // the reflogs panel is the only panel where we cache data, in that we only // load entries that hav...
  * `promptForBaseGithubRepo` **(Stateful Encapsulated Methods)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 96`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 21`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 21`, `doc: 16`, `sync_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` HEAD, async, block-ui, fmt, set, gocui, git_commands, models...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/branches.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 315.82 | **LOC:** 288 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.677; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBranchDisplayStrings` **(Many-Argument Workhorses)** (Impact: 113.1)
    * *Intent:* // getBranchDisplayStrings returns the display string of branch
  * `BranchStatus` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `divergenceStr` **(Stateful Encapsulated Methods)** (Impact: 14.4)
  * `prColor` **(Stateful Encapsulated Methods)** (Impact: 10.6)
  * `match` **(Stateful Encapsulated Methods)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.677
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003613
  * `Imports (Out-Degree: 7):` CLOSED, DRAFT, MERGED, OPEN, fmt, git_commands, models, config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/commands/git_commands/working_tree.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 309.1 | **LOC:** 610 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 63.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.5%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DiscardAllDirChanges` **(Compute Cores)** (Impact: 28.5)
  * `WorktreeFileDiffCmdObj` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* // WorktreeFileDiffCmdObj returns a command object for diffing a file or directory // in the working...
  * `DiscardAllFileChanges` **(Defensive Guards)** (Impact: 24.1)
    * *Intent:* // DiscardAllFileChanges directly
  * `removeEmptyDirs` **(Stateful Encapsulated Methods)** (Impact: 20.7)
    * *Intent:* // Removes empty directories left behind after deleting files, but only for directories that // are ...
  * `ShowFileDiffCmdObj` **(Many-Argument Workhorses)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 98`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `dead_code: 2`, `unreferenced_by_name: 25`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `safety: 20`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , fmt, errors, set, models, oscommands, lo, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/files.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 303.22 | **LOC:** 349 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.677; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFileLine` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `getCommitFileLine` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `renderAux` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `fileNameAtDepth` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `getColorForChangeStatus` **(Stateful Encapsulated Methods)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 34`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 37`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.677
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003613
  * `Imports (Out-Degree: 5):` , A, C, D, M, T, color, models...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/branches_controller.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 300.98 | **LOC:** 987 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%), Mutation Surface (formerly State Flux) (68.3%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `viewUpstreamOptions` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `delete` **(Compute Cores)** (Impact: 16.0)
  * `createPullRequestMenu` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `withPrFgColor` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `withPrBgColor` **(Stateful Encapsulated Methods)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 134`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 13`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` CLOSED, DRAFT, MERGED, OPEN, errors, fmt, color, gocui...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/config/editor_presets.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 296.78 | **LOC:** 199 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.9%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPreset` **(Many-Argument Workhorses)** (Impact: 78.3)
    * *Intent:* // IF YOU ADD A PRESET TO THIS FUNCTION YOU MUST UPDATE THE `Supported presets` SECTION OF docs/Conf...
  * `GetEditTemplate` **(Callbacks & Closures)** (Impact: 4.5)
  * `GetEditAtLineTemplate` **(Callbacks & Closures)** (Impact: 4.4)
  * `GetEditAtLineAndWaitTemplate` **(Callbacks & Closures)** (Impact: 4.4)
  * `GetOpenDirInEditorTemplate` **(Callbacks & Closures)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` acme, bbedit, code, emacs, helix, hx, kak, kakoune...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/graph/cell.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 293.7 | **LOC:** 184 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.3%), Debt Markers (formerly Tech Debt) (94.4%), Guard Balance (formerly Safety Score) (93.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBoxDrawingChars` **(Compute Cores)** (Impact: 180.7)
  * `render` **(Stateful Encapsulated Methods)** (Impact: 14.4)
  * `cachedSprint` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `setRight` **(Stateful Encapsulated Methods)** (Impact: 5.5)
    * *Intent:* //nolint:unparam
  * `setLeft` **(Stateful Encapsulated Methods)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 28`, `unreferenced_by_name: 8`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `sync_locks: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` color, style, io, sync
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/components/view_driver.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 280.4 | **LOC:** 654 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 86.5854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertLines` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `NavigateToLine` **(Compute Cores)** (Impact: 18.9)
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
* *Structure:* `branch: 52`, `structural_boundaries: 98`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 30`, `dead_code: 3`, `unreferenced_by_name: 18`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fmt, gocui, lo, strings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/graph/graph.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 271.82 | **LOC:** 388 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.702; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderPipeSet` **(Many-Argument Workhorses)** (Impact: 69.2)
  * `getNextPipes` **(Many-Argument Workhorses)** (Impact: 66.2)
  * `RenderAux` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `equalHashes` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `RenderCommitGraph` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 42`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.702
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003613
  * `Imports (Out-Degree: 4):` cmp, set, models, style, utils, lo, runtime, slices...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/helpers/window_arrangement_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 257.66 | **LOC:** 499 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infoSectionChildren` **(Compute Cores)** (Impact: 32.0)
  * `getMidSectionWeights` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `sidePanelChildren` **(Compute Cores)** (Impact: 18.0)
  * `splitMainPanelSideBySide` **(Stateful Encapsulated Methods)** (Impact: 12.2)
  * `GetWindowDimensions` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 29`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` always, fmt, boxlayout, config, types, utils, slices, horizontal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/commands/git_commands/rebase.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 253.7 | **LOC:** 591 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.5%), Guard Balance (formerly Safety Score) (50.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` --root, baseCommit, fmt, errors, daemon, models, oscommands, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/components/shell.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 243.86 | **LOC:** 526 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.7%), Connectivity (formerly Api Exposure) (72.3%), Guard Balance (formerly Safety Score) (54.9%)
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
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 13`
* *Architecture:* `io: 3`, `api: 60`, `import: 1`
* *Defense:* `safety: 13`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.632
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001016
  * `Imports (Out-Degree: 2):` fmt, git, io, rand, os, exec, filepath, runtime...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/commands/oscommands/cmd_obj_runner.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 239.02 | **LOC:** 476 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runAndStreamAux` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `RunAndProcessLines` **(Defensive Guards)** (Impact: 19.9)
  * `processOutput` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `getCheckForCredentialRequestFunc` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* // having a function that returns a function because we need to maintain some state inbetween calls ...
  * `getCredentialPromptFn` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `dead_code: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`, `api: 16`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 12`, `doc: 5`, `sync_locks: 25`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bufio, bytes, errors, utils, go-deadlock, logrus, io, exec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/window_arrangement_helper_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 238.88 | **LOC:** 730 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.596; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (21.1%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderLayout` **(Compute Cores)** (Impact: 68.2)
  * `TestGetWindowDimensions` **(I/O & Config Routines)** (Impact: 12.1)
    * *Intent:* // The best way to add test cases here is to set your args and then get the // test to fail and copy...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 16`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cmp, fmt, boxlayout, config, types, lo, slices, strings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/fixup_helper.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 236.2 | **LOC:** 413 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%)
- **Documentation Coverage:** 78.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blameAddedLines` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `parseDiff` **(Compute Cores)** (Impact: 27.9)
    * *Intent:* // Parse the diff output into hunks, and return two lists of hunks: the first // are ones that conta...
  * `HandleFindBaseCommitForFixupPress` **(I/O & Config Routines)** (Impact: 20.2)
  * `IsFixupCommit` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* // Check whether the given subject line is the subject of a fixup commit, and // returns (trimmedSub...
  * `removeFixupCommits` **(Stateful Encapsulated Methods)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 55`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 6`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` errors, fmt, set, models, types, utils, lo, errgroup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pkg/gui/gui.go` -> Churn: **86.49%** | Cog Load: 40.7817% | Debt: 98.3539%
- `pkg/commands/git_commands/working_tree.go` -> Churn: **84.61%** | Cog Load: 14.1317% | Debt: 95.4759%
- `pkg/gui/controllers/local_commits_controller.go` -> Churn: **83.05%** | Cog Load: 8.4229% | Debt: 62.1118%
- `pkg/gui/background.go` -> Churn: **70.18%** | Cog Load: 67.0924% | Debt: 49.5229%
- `pkg/gui/controllers/helpers/merge_and_rebase_helper.go` -> Churn: **64.62%** | Cog Load: 14.8767% | Debt: 56.3985%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pkg/gui/presentation/commits.go` -> **Jesse Duffield** (100.0% isolated ownership) | Magnitude: 490.32
- `pkg/gui/patch_exploring/state.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 333.8
- `pkg/gui/controllers/branches_controller.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 300.98
- `pkg/config/editor_presets.go` -> **baiyei_dk** (100.0% isolated ownership) | Magnitude: 296.78
- `pkg/commands/oscommands/cmd_obj_runner.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 239.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pkg/commands/oscommands/os.go` -> **Severity: 0.049** (Bridge: 0.0006 * Flux: 87.0519%)
- `pkg/utils/utils.go` -> **Severity: 0.034** (Bridge: 0.0009 * Flux: 36.187%)
- `pkg/theme/gocui.go` -> **Severity: 0.029** (Bridge: 0.0006 * Flux: 50.0%)
- `pkg/theme/style.go` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)
- `pkg/gui/gui.go` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 98.9661%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pkg/utils/utils.go` -> **Severity: 8.738** (Embedded: 0.1568 * Error Risk: 55.7195%)
- `pkg/theme/gocui.go` -> **Severity: 8.281** (Embedded: 0.1386 * Error Risk: 59.7314%)
- `pkg/commands/oscommands/os.go` -> **Severity: 6.418** (Embedded: 0.1162 * Error Risk: 55.2404%)
- `pkg/utils/io.go` -> **Severity: 4.758** (Embedded: 0.0844 * Error Risk: 56.3934%)
- `pkg/theme/style.go` -> **Severity: 4.654** (Embedded: 0.0504 * Error Risk: 92.3134%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pkg/utils/utils.go` -> **Severity: 6810.24** (Blast Radius: 85.128 * Doc Risk: 80.0%)
- `pkg/commands/oscommands/os.go` -> **Severity: 3277.187** (Blast Radius: 60.862 * Doc Risk: 53.8462%)
- `pkg/utils/regexp.go` -> **Severity: 3016.4** (Blast Radius: 30.164 * Doc Risk: 100.0%)
- `pkg/utils/io.go` -> **Severity: 2339.6** (Blast Radius: 23.396 * Doc Risk: 100.0%)
- `pkg/commands/git_commands/sync.go` -> **Severity: 2268.5** (Blast Radius: 22.685 * Doc Risk: 100.0%)

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
