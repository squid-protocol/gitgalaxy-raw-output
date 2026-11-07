# ARCHITECTURAL_BRIEF: zellij
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/zellij-org/zellij.git` |
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
- **Scope:** 383 analyzed artifact(s), 246075 LOC.
- **Load-bearing artifact:** `zellij-utils/src/data.rs` -- 100 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `zellij-utils/src/plugin_api/plugin_command.rs` -- pulls in 270 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `zellij-server/src/screen.rs` at magnitude 4992.42 (structural weight, not risk).
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
| Total Artifacts | 1571 |
| Analyzed Artifacts (Scanned) | 383 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1188 |
| Total LOC | 246075 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 24.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5406 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1017 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 55.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2836 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 298 | 239336 | 77.8% |
| MARKDOWN | 28 | 0 | 7.3% |
| YAML | 18 | 1529 | 4.7% |
| PROTO | 17 | 3646 | 4.4% |
| JAVASCRIPT | 10 | 1227 | 2.6% |
| SHELL | 7 | 95 | 1.8% |
| CSS | 2 | 162 | 0.5% |
| XML | 1 | 0 | 0.3% |
| JSON | 1 | 50 | 0.3% |
| HTML | 1 | 30 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 383 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 28%, Data / Markup / Trivial 18%, Declarative / Non-Code 9%, State Mutators Files 9%, Generic / Templated Code Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 355 | 92.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1188*

**Composition by Extension & Reason:**
- `.snap`: 901x Unsupported Format (.snap), 6x Excluded (Saturation: Line 5 exceeds 500 chars), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `no_extension`: 38x Unsupported Format (.undeterminable), 19x Excluded (Binary Format Detected), 13x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.kdl`: 62x Excluded (Unsupported Extension: '.kdl'), 22x Unsupported Format (.kdl)
- `.toml`: 20x Unsupported Format (.toml), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.wasm`: 17x Excluded (Unsupported Extension: '.wasm')
- `.yaml`: 3x Zero-Density Threshold (LOC: 557, Signals: 0), 1x Zero-Density Threshold (LOC: 251, Signals: 0), 1x Zero-Density Threshold (LOC: 569, Signals: 0)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars), 1x Excluded (Saturation: Line 30 exceeds 500 chars)
- `.rs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.six`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.bmp`: 2x Excluded (Explicitly Denied Extension: '.bmp')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.8 | 9.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 36.5 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 33.1 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.3 | 33.0 | 31.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.9 | 17.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.4 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.0 | 0.9 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 82.9 | 15.9 | 6.7 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 73.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.6 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3666 | 127 | 12 | `zellij-server/src/panes/unit/grid_tests.rs` |
| cleanup | 125 | 32 | 0 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| guards | 4420 | 225 | 32 | `zellij-utils/src/kdl/mod.rs` |
| danger | 7348 | 128 | 16 | `zellij-server/src/tab/unit/tab_tests.rs` |
| concurrency | 3185 | 75 | 8 | `zellij-server/src/unit/screen_tests.rs` |
| connectivity | 9131 | 296 | 51 | `zellij-utils/assets/prost_ipc/client_server_contract.rs` |
| io | 365 | 78 | 3 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `zellij-client/src/lib.rs` |
| time | 561 | 43 | 1 | `zellij-server/src/unit/screen_tests.rs` |
| serialization | 46 | 15 | 0 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| regex | 21 | 10 | 0 | `zellij-client/src/stdin_ansi_parser.rs` |
| events | 597 | 80 | 3 | `zellij-server/src/screen.rs` |
| tests | 5623 | 83 | 14 | `zellij-server/src/tab/unit/tab_tests.rs` |
| docs | 2932 | 122 | 16 | `zellij-tile/src/shim.rs` |
| debt | 702 | 116 | 5 | `src/commands.rs` |
| mutation | 39699 | 302 | 255 | `zellij-server/src/tab/unit/tab_integration_tests.rs` |
| dead_code | 529 | 47 | 1 | `zellij-server/src/tab/mod.rs` |
| credential | 6 | 4 | 0 | `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 132 | 32 | 0 | `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` |
| ui | 22 | 7 | 0 | `zellij-client/assets/xterm.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `zellij-client/src/web_client/unit/web_client_tests.rs` (Hits: 28)
- `zellij-client/assets/index.html` (Hits: 19)
- `zellij-utils/src/consts.rs` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **data.rs** (`zellij-utils/src/data.rs`) — 100 inbound connections
2. **errors.rs** (`zellij-utils/src/errors.rs`) — 75 inbound connections
3. **prelude.rs** (`zellij-tile/src/prelude.rs`) — 64 inbound connections
4. **pane_size.rs** (`zellij-utils/src/pane_size.rs`) — 51 inbound connections
5. **layout.rs** (`zellij-utils/src/input/layout.rs`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin_command.rs** (`zellij-utils/src/plugin_api/plugin_command.rs`) — 270 outbound dependencies
2. **protobuf_conversion.rs** (`zellij-utils/src/ipc/protobuf_conversion.rs`) — 229 outbound dependencies
3. **zellij_exports.rs** (`zellij-server/src/plugins/zellij_exports.rs`) — 203 outbound dependencies
4. **action.rs** (`zellij-utils/src/plugin_api/action.rs`) — 118 outbound dependencies
5. **screen.rs** (`zellij-server/src/screen.rs`) — 104 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `screen_thread_main` **(Many-Argument Workhorses)** (@ `zellij-server/src/screen.rs`) -> Impact: **2392.3** | LOC: 4192
  * *Intent:* // The box is here in order to make the // NewClient enum smaller
- `route_action` **(Many-Argument Workhorses)** (@ `zellij-server/src/route.rs`) -> Impact: **1091.6** | LOC: 1926
- `try_from` **(Many-Argument Workhorses)** (@ `zellij-utils/src/plugin_api/plugin_command.rs`) -> Impact: **585.6** | LOC: 2039
- `actions_from_cli` **(Many-Argument Workhorses)** (@ `zellij-utils/src/input/actions.rs`) -> Impact: **473.4** | LOC: 1508
- `csi_dispatch` **(Many-Argument Workhorses)** (@ `zellij-server/src/panes/grid.rs`) -> Impact: **427.1** | LOC: 605
- `plugin_thread_main` **(Many-Argument Workhorses)** (@ `zellij-server/src/plugins/mod.rs`) -> Impact: **377.6** | LOC: 1014
- `update` **(Many-Argument Workhorses)** (@ `default-plugins/fixture-plugin-for-tests/src/main.rs`) -> Impact: **308.3** | LOC: 866
- `try_from` **(Many-Argument Workhorses)** (@ `zellij-utils/src/ipc/protobuf_conversion.rs`) -> Impact: **299.1** | LOC: 919
- `try_from` **(Many-Argument Workhorses)** (@ `zellij-utils/src/plugin_api/action.rs`) -> Impact: **261.2** | LOC: 954
- `start_client` **(Many-Argument Workhorses)** (@ `zellij-client/src/lib.rs`) -> Impact: **212.7** | LOC: 585

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `zellij-server/src` | 15 | 10668.12 | 15.91% | 9.46% |
| `zellij-server/src/panes` | 12 | 7244.42 | 27.48% | 4.88% |
| `zellij-server/src/tab` | 6 | 5613.8 | 20.92% | 19.16% |
| `zellij-utils/src/kdl` | 2 | 4764.68 | 23.72% | 5.47% |
| `zellij-utils/src` | 23 | 4252.5 | 7.59% | 4.29% |
| `zellij-server/src/panes/tiled_panes` | 4 | 4089.78 | 27.47% | 34.1% |
| `zellij-server/src/plugins` | 9 | 3771.18 | 12.1% | 5.41% |
| `zellij-utils/src/input` | 13 | 3693.36 | 16.18% | 6.92% |
| `zellij-server/src/tab/unit` | 3 | 3426.08 | 5.14% | 4.42% |
| `zellij-utils/src/plugin_api` | 27 | 3223.1 | 4.11% | 0.85% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `zellij-utils/assets/completions/comp.bash` -> **99.999%** Exposure
- `zellij-utils/assets/completions/comp.zsh` -> **99.999%** Exposure
- `.github/workflows/release.yml` -> **98.6527%** Exposure
- `zellij-server/src/panes/floating_panes/mod.rs` -> **97.8089%** Exposure
- `zellij-server/src/tab/mod.rs` -> **97.5406%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `default-plugins/layout-manager/src/screens/layout_list/mod.rs` -> **100.0%** Exposure
- `default-plugins/layout-manager/src/screens/layout_list/search.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/nested_list.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/table.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/text.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `zellij-server/src/tab/mod.rs` -> **216** Orphaned Functions | **0** Duplicates
- `zellij-server/src/panes/tiled_panes/mod.rs` -> **66** Orphaned Functions | **0** Duplicates
- `zellij-server/src/panes/floating_panes/mod.rs` -> **52** Orphaned Functions | **0** Duplicates
- `default-plugins/status-bar/src/main.rs` -> **28** Orphaned Functions | **0** Duplicates
- `zellij-server/src/output/mod.rs` -> **22** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` -> **68.6348%** Exposure
- `zellij-client/src/web_client/unit/web_client_tests.rs` -> **10.5012%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5149` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `zellij-server/src/screen.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.835)
- **Top Global Matches:** file_cluster_4: 7.835, file_cluster_6: 12.064, file_cluster_15: 13.038
- **Magnitude:** 4992.42 | **LOC:** 9125 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 87.8%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **104**; blast radius 1.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.6%), Connectivity (formerly Api Exposure) (54.2%)
- **Documentation Coverage:** 82.243% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `screen_thread_main` **(Many-Argument Workhorses)** (Impact: 2392.3)
    * *Intent:* // The box is here in order to make the // NewClient enum smaller
  * `apply_layout` **(Many-Argument Workhorses)** (Impact: 102.1)
  * `render_to_clients` **(Compute Cores)** (Impact: 68.5)
  * `reconfigure` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `focus_plugin_pane` **(Many-Argument Workhorses)** (Impact: 60.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 629
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1468`, `structural_boundaries: 1316`, `args: 404`, `func_start: 131`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 251`, `dead_code: 1`, `planned_debt: 9`
* *Architecture:* `io: 5`, `api: 102`, `import: 30`
* *Defense:* `safety: 288`, `doc: 109`, `test: 7`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.164
  * `Choke Point (Betweenness):` 0.00336 | `Ripple Effect (Closeness):` 0.067301
  * `Imports (Out-Degree: 33):` screen_tests.rs, crate::ClientId, crate::ServerInstruction, crate::background_jobs::BackgroundJob, crate::os_input_output::ResizeCache, crate::output::Output, crate::pane_groups::PaneGroups, crate::panes::PaneId...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `zellij-server/src/tab/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.413)
- **Top Global Matches:** file_cluster_15: 7.413, file_cluster_0: 7.859, file_cluster_16: 9.05
- **Magnitude:** 3661.3 | **LOC:** 6061 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 93.1%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **96**; blast radius 1.884; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.4%), Mutation Surface (formerly State Flux) (54.3%)
- **Documentation Coverage:** 99.6974% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_to_pane_id` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `suppress_pane_and_replace_with_pid` **(Many-Argument Workhorses)** (Impact: 58.3)
  * `new_no_preference_pane` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `new_stacked_pane` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `extract_pane` **(Many-Argument Workhorses)** (Impact: 49.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 96 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 916`, `structural_boundaries: 1040`, `args: 663`, `func_start: 420`, `class_start: 4`
* *Risk/State:* `state_mutation: 173`, `planned_debt: 25`, `fragile_debt: 3`, `unreferenced_by_name: 216`
* *Architecture:* `io: 1`, `api: 259`, `import: 31`
* *Defense:* `safety: 207`, `doc: 5`, `test: 3`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.884
  * `Choke Point (Betweenness):` 0.013588 | `Ripple Effect (Closeness):` 0.07799
  * `Imports (Out-Degree: 38):` clipboard, copy_command, layout_applier, mouse_handler, swap_layouts, layout_applier_tests.rs, tab_integration_tests.rs, tab_tests.rs...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `zellij-server/src/panes/grid.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.492)
- **Top Global Matches:** file_cluster_4: 8.492, file_cluster_15: 10.555, file_cluster_12: 11.156
- **Magnitude:** 3528.12 | **LOC:** 4798 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 85.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **58**; blast radius 1.631; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.5%)
- **Documentation Coverage:** 92.7928% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `csi_dispatch` **(Many-Argument Workhorses)** (Impact: 427.1)
  * `osc_dispatch` **(Many-Argument Workhorses)** (Impact: 113.2)
  * `change_size` **(Many-Argument Workhorses)** (Impact: 93.3)
  * `compute_plugin_highlight_selections` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* /// Pre-compute plugin highlight selections across all logical line groups in /// the viewport. Hove...
  * `get_selected_text` **(Compute Cores)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 279 instances
* *State Mutation (weighted view):* 1025
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 896`, `structural_boundaries: 959`, `args: 274`, `func_start: 194`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 467`, `planned_debt: 17`, `fragile_debt: 4`
* *Architecture:* `api: 194`, `import: 26`
* *Defense:* `safety: 113`, `doc: 61`, `test: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.631
  * `Choke Point (Betweenness):` 0.00727 | `Ripple Effect (Closeness):` 0.085537
  * `Imports (Out-Degree: 17):` grid_tests.rs, crate::output::CharacterChunk, crate::output::HighlightSelection, crate::output::OutputBuffer, crate::output::SixelImageChunk, crate::panes::Selection, crate::panes::alacritty_functions::parse_number, crate::panes::alacritty_functions::xparse_color...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `zellij-utils/src/kdl/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.252)
- **Top Global Matches:** file_cluster_4: 8.252, file_cluster_12: 11.8, file_cluster_9: 12.161
- **Magnitude:** 2974.6 | **LOC:** 7185 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 81.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **67**; blast radius 1.288; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.5%), Guard Balance (formerly Safety Score) (55.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_kdl` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `try_from` **(Many-Argument Workhorses)** (Impact: 111.5)
  * `to_kdl` **(Defensive Guards)** (Impact: 87.1)
  * `from_kdl` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `from_string` **(Defensive Guards)** (Impact: 56.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 798`, `structural_boundaries: 1618`, `args: 520`, `func_start: 129`
* *Risk/State:* `safety_bypasses: 136`, `state_mutation: 448`, `dead_code: 4`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `io: 3`, `api: 44`, `concurrency: 3`, `import: 28`
* *Defense:* `safety: 310`, `doc: 6`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 0.002158 | `Ripple Effect (Closeness):` 0.169205
  * `Imports (Out-Degree: 14):` kdl_layout_parser, crate::data::BareKey, crate::data::DEFAULT_STYLES, crate::data::Direction, crate::data::FloatingPaneCoordinates, crate::data::InputMode, crate::data::KeyWithModifier, crate::data::LayoutInfo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/plugins/unit/plugin_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.997)
- **Top Global Matches:** file_cluster_12: 7.997, file_cluster_7: 8.672, file_cluster_5: 8.878
- **Magnitude:** 1823.1 | **LOC:** 12897 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **43**; blast radius 0.693; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.0%), Guard Balance (formerly Safety Score) (54.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mode_update_payload_is_lightweight_for_opted_in_plugins` **(I/O & Config Routines)** (Impact: 21.8)
  * `create_plugin_thread_with_pty_receiver` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `reconfiguration_resends_keybinds_to_opted_in_plugins` **(I/O & Config Routines)** (Impact: 14.1)
  * `create_plugin_thread` **(Generic / Templated Code)** (Impact: 13.8)
  * `create_plugin_thread_with_background_jobs_receiver` **(Generic / Templated Code)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 207
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 2924`, `args: 324`, `func_start: 150`
* *Risk/State:* `safety_bypasses: 496`, `state_mutation: 43`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `io: 3`, `api: 146`, `concurrency: 197`, `import: 25`
* *Defense:* `safety: 153`, `test: 167`, `sync_locks: 328`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.693
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.051993
  * `Imports (Out-Degree: 18):` crate::ServerInstruction, crate::background_jobs::BackgroundJob, crate::channels::SenderWithContext, crate::panes::PaneId, crate::plugins::PluginInstruction, crate::pty::PtyInstruction, crate::pty_writer::PtyWriteInstruction, crate::screen::ScreenInstruction...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-utils/src/kdl/kdl_layout_parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.696)
- **Top Global Matches:** file_cluster_6: 6.696, file_cluster_4: 12.868, file_cluster_8: 13.081
- **Magnitude:** 1790.08 | **LOC:** 2602 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.713; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_floating_pane_node_with_template` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `populate_layout_child` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `differentiate_pane_and_floating_pane_template` **(Compute Cores)** (Impact: 57.9)
  * `parse_pane_node_with_template` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `layout_with_one_pane` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 611`, `structural_boundaries: 529`, `args: 225`, `func_start: 69`, `class_start: 2`
* *Risk/State:* `state_mutation: 97`
* *Architecture:* `io: 2`, `api: 9`, `import: 7`
* *Defense:* `safety: 128`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.713
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.132523
  * `Imports (Out-Degree: 4):` crate::input::command::RunCommand, crate::input::config::ConfigError, crate::input::layout::FloatingPaneLayout, crate::input::layout::Layout, crate::input::layout::LayoutConstraint, crate::input::layout::PercentOrFixed, crate::input::layout::PluginUserConfiguration, crate::input::layout::Run...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/route.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.435)
- **Top Global Matches:** file_cluster_4: 7.435, file_cluster_15: 9.098, file_cluster_12: 9.556
- **Magnitude:** 1789.38 | **LOC:** 3192 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 82.8%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **55**; blast radius 1.025; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.4%), Mutation Surface (formerly State Flux) (72.2%), Guard Balance (formerly Safety Score) (52.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `route_action` **(Many-Argument Workhorses)** (Impact: 1091.6)
  * `route_thread_main` **(Many-Argument Workhorses)** (Impact: 174.6)
  * `build_tabs_table_row` **(Many-Argument Workhorses)** (Impact: 14.6)
  * `build_table_row` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `build_tabs_table_header` **(Many-Argument Workhorses)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 283`, `args: 83`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 91`
* *Architecture:* `api: 23`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 72`, `test: 13`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.025
  * `Choke Point (Betweenness):` 0.002775 | `Ripple Effect (Closeness):` 0.076197
  * `Imports (Out-Degree: 18):` crate::ClientId, crate::ServerInstruction, crate::SessionMetaData, crate::SessionState, crate::global_async_runtime::get_tokio_runtime, crate::os_input_output::ServerOsApi, crate::panes::PaneId, crate::plugins::PluginInstruction...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `zellij-server/src/tab/unit/tab_integration_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.707)
- **Top Global Matches:** file_cluster_7: 7.707, file_cluster_5: 9.577, file_cluster_14: 9.635
- **Magnitude:** 1731.38 | **LOC:** 14801 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **65**; blast radius 0.689; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.3%), Connectivity (formerly Api Exposure) (64.4%), Mutation Surface (formerly State Flux) (12.5%)
- **Documentation Coverage:** 99.5781% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_new_tab_with_swap_layouts` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `focus_follows_mouse_skips_stacked_one_liner_pane` **(I/O & Config Routines)** (Impact: 10.3)
  * `render_stacks_without_pane_frames` **(I/O & Config Routines)** (Impact: 9.7)
  * `start` **(Compute Cores)** (Impact: 8.2)
  * `non_overlapping_highlights_from_different_layers_coexist` **(I/O & Config Routines)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 3086`, `args: 256`, `func_start: 247`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1565`, `high_risk_execution: 16`, `state_mutation: 111`
* *Architecture:* `io: 2`, `api: 228`, `concurrency: 6`, `import: 44`
* *Defense:* `safety: 15`, `doc: 4`, `test: 434`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.689
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.055243
  * `Imports (Out-Degree: 21):` crate::Arc, crate::ClientId, crate::ServerInstruction, crate::os_input_output::AsyncReader, crate::os_input_output::ServerOsApi, crate::pane_groups::PaneGroups, crate::panes::PaneId, crate::panes::grid::Grid...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/unit/screen_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.904)
- **Top Global Matches:** file_cluster_7: 7.904, file_cluster_12: 8.17, file_cluster_5: 8.663
- **Magnitude:** 1685.7 | **LOC:** 8080 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 86.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **80**; blast radius 0.681; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.4%), Connectivity (formerly Api Exposure) (67.7%), Guard Balance (formerly Safety Score) (62.8%), Mutation Surface (formerly State Flux) (27.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_with_alias` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* // same as the above function, but starts a plugin with a plugin alias
  * `run` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `new` **(Compute Cores)** (Impact: 12.3)
  * `background_plugin_receives_broadcasts_regardless_of_active_tab` **(I/O & Config Routines)** (Impact: 12.3)
  * `integration_scrollback_from_pre_subscription_pty_bytes` **(I/O & Config Routines)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 24
* *Concurrency (weighted view):* 298
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 2153`, `args: 254`, `func_start: 199`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 463`, `high_risk_execution: 26`, `state_mutation: 212`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 209`, `concurrency: 238`, `import: 36`
* *Defense:* `safety: 32`, `test: 411`, `sync_locks: 236`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.681
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.049657
  * `Imports (Out-Degree: 25):` crate::ClientId, crate::ServerInstruction, crate::SessionMetaData, crate::ThreadSenders, crate::background_jobs::BackgroundJob, crate::channels::SenderWithContext, crate::os_input_output::AsyncReader, crate::os_input_output::ServerOsApi...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.94)
- **Top Global Matches:** file_cluster_4: 6.94, file_cluster_6: 10.012, file_cluster_12: 12.747
- **Magnitude:** 1504.0 | **LOC:** 2362 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 0.736; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.0%), Connectivity (formerly Api Exposure) (52.5%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `change_pane_size` **(Many-Argument Workhorses)** (Impact: 166.6)
    * *Intent:* /// Change a tiled panes size based on the given strategy. /// /// Returns true upon successful resi...
  * `contiguous_panes_with_alignment` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* /// Searches for contiguous panes
  * `can_change_pane_size` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* // Check if panes in the desired direction can be resized. Returns the maximum resize that's // poss...
  * `fill_geom_holes_horizontally_downwards` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `fill_geom_holes_vertically_to_the_right` **(Many-Argument Workhorses)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 549`, `args: 240`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 35`, `import: 17`
* *Defense:* `safety: 70`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046849
  * `Imports (Out-Degree: 9):` Direction, Direction::Down, Direction::Left, Direction::Right, Direction::Up, crate::panes::PaneId, crate::tab::MIN_TERMINAL_HEIGHT, crate::tab::MIN_TERMINAL_WIDTH...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tests/e2e/cases.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.005)
- **Top Global Matches:** file_cluster_8: 9.005, file_cluster_6: 12.858, file_cluster_4: 20.765
- **Magnitude:** 1452.92 | **LOC:** 2955 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 2.355; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Connectivity (formerly Api Exposure) (64.3%), Guard Balance (formerly Safety Score) (56.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mirrored_sessions` **(I/O & Config Routines)** (Impact: 36.5)
  * `multiple_users_in_different_tabs` **(I/O & Config Routines)** (Impact: 28.9)
  * `watcher_client_functionality` **(I/O & Config Routines)** (Impact: 28.6)
  * `multiple_users_in_different_panes_and_same_tab` **(I/O & Config Routines)** (Impact: 26.8)
  * `multiple_users_in_same_pane_and_tab` **(I/O & Config Routines)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 100 instances
* *Concurrency (weighted view):* 269
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 665`, `args: 172`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `fragile_debt: 1`
* *Architecture:* `api: 90`, `concurrency: 79`, `import: 8`
* *Defense:* `test: 48`, `sync_locks: 13`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.355
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.005846
  * `Imports (Out-Degree: 4):` crate::tests::e2e::steps::check_focus_on_second_tab, crate::tests::e2e::steps::check_second_tab_opened, crate::tests::e2e::steps::check_third_tab_is_left_wrapped, crate::tests::e2e::steps::check_third_tab_is_right_wrapped, crate::tests::e2e::steps::check_third_tab_moved_left, crate::tests::e2e::steps::check_third_tab_moved_to_beginning, crate::tests::e2e::steps::check_third_tab_opened, crate::tests::e2e::steps::move_tab_left...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `zellij-server/src/plugins/zellij_exports.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.35)
- **Top Global Matches:** file_cluster_15: 8.35, file_cluster_12: 9.678, file_cluster_0: 9.707
- **Magnitude:** 1424.16 | **LOC:** 5353 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 84.6%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **203**; blast radius 1.039; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.1%), Guard Balance (formerly Safety Score) (49.8%), Connectivity (formerly Api Exposure) (23.8%)
- **Documentation Coverage:** 99.5516% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `host_run_plugin_command` **(I/O & Config Routines)** (Impact: 70.6)
  * `switch_session` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `try_save_layout` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `load_new_plugin` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `translate_plugin_path` **(Defensive Guards)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 889`, `args: 609`, `func_start: 218`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 20`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 5`, `concurrency: 7`, `import: 52`
* *Defense:* `safety: 50`, `doc: 2`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.039
  * `Choke Point (Betweenness):` 0.002944 | `Ripple Effect (Closeness):` 0.053461
  * `Imports (Out-Degree: 27):` crate::ServerInstruction, crate::background_jobs::BackgroundJob, crate::global_async_runtime::get_tokio_runtime, crate::panes::PaneId, crate::plugins::DumpSessionLayoutResponse, crate::plugins::plugin_map::PluginEnv, crate::plugins::wasm_bridge::handle_plugin_crash, crate::pty::ClientTabIndexOrPaneId...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `zellij-server/src/panes/tiled_panes/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.451)
- **Top Global Matches:** file_cluster_12: 7.451, file_cluster_5: 8.414, file_cluster_4: 9.998
- **Magnitude:** 1407.76 | **LOC:** 2800 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **44**; blast radius 0.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (62.6%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 118.0)
  * `stacked_resize_pane_with_id` **(Many-Argument Workhorses)** (Impact: 96.1)
  * `set_pane_frames` **(Compute Cores)** (Impact: 30.7)
  * `toggle_pane_fullscreen` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `add_pane_with_stacked_resize` **(Many-Argument Workhorses)** (Impact: 23.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 642`, `args: 200`, `func_start: 128`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 92`, `planned_debt: 7`, `unreferenced_by_name: 66`
* *Architecture:* `api: 114`, `import: 6`
* *Defense:* `safety: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.975
  * `Choke Point (Betweenness):` 0.003659 | `Ripple Effect (Closeness):` 0.062539
  * `Imports (Out-Degree: 17):` pane_resizer, stacked_panes, tiled_pane_grid, crate::ClientId, crate::os_input_output::ServerOsApi, crate::output::Output, crate::panes::ActivePanes, crate::panes::PaneId...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `zellij-utils/src/data.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.336)
- **Top Global Matches:** file_cluster_0: 6.336, file_cluster_15: 8.312, file_cluster_13: 9.236
- **Magnitude:** 1349.7 | **LOC:** 3612 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 82.1%
- **Blast Radius:** changing it is visible to **100** in-repo importer(s); it depends on **43**; blast radius 83.757; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.7%), Guard Balance (formerly Safety Score) (51.1%), Mutation Surface (formerly State Flux) (36.4%)
- **Documentation Coverage:** 96.8153% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `from_cli` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `from_config` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `extract_text_by_columns` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /// Extract text from a line between two column positions, accounting for wide characters
  * `eq` **(Compute Cores)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 426`, `args: 216`, `func_start: 181`, `class_start: 75`
* *Risk/State:* `state_mutation: 75`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 465`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 27`, `doc: 142`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.757
  * `Choke Point (Betweenness):` 0.050661 | `Ripple Effect (Closeness):` 0.360037
  * `Imports (Out-Degree: 11):` clap::ArgEnum, crate::home::default_layout_dir, crate::input::actions::Action, crate::input::actions::RunCommandAction, crate::input::config::ConversionError, crate::input::config::KdlError, crate::input::keybinds::Keybinds, crate::input::layout::Layout...
  * `Imported By (In-Degree: 100):` (Excluded from Brief to save tokens)

### `zellij-utils/src/input/layout.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.483)
- **Top Global Matches:** file_cluster_0: 7.483, file_cluster_15: 8.927, file_cluster_12: 9.015
- **Magnitude:** 1223.26 | **LOC:** 2104 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **34**; blast radius 44.268; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.8%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `split_space` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `position_panes_in_space` **(Many-Argument Workhorses)** (Impact: 34.7)
  * `adjust_geoms_for_rounding_errors` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `list_available_layouts` **(Defensive Guards)** (Impact: 27.0)
  * `truncate` **(Compute Cores)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 344`, `args: 179`, `func_start: 118`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 107`, `planned_debt: 9`
* *Architecture:* `io: 7`, `api: 162`, `import: 12`
* *Defense:* `safety: 56`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.268
  * `Choke Point (Betweenness):` 0.005657 | `Ripple Effect (Closeness):` 0.268514
  * `Imports (Out-Degree: 9):` layout_test.rs, crate::data::Direction, crate::data::LayoutInfo, crate::data::LayoutMetadata, crate::data::LayoutParsingError, crate::data::LayoutWithError, crate::downloader::Downloader, crate::home::default_layout_dir...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `zellij-utils/src/plugin_api/plugin_command.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.587)
- **Top Global Matches:** file_cluster_0: 9.587, file_cluster_12: 10.191, file_cluster_15: 10.333
- **Magnitude:** 1122.4 | **LOC:** 4886 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 88.2%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **270**; blast radius 6.025; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.8%), Guard Balance (formerly Safety Score) (48.4%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_from` **(Many-Argument Workhorses)** (Impact: 585.6)
  * `try_from` **(Many-Argument Workhorses)** (Impact: 152.4)
  * `into` **(Type Conversions)** (Impact: 9.6)
  * `into` **(Type Conversions)** (Impact: 9.6)
  * `key_to_rebind_to_plugin_command_assets` **(State Mutators)** (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 271`, `args: 276`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 24`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 113`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.025
  * `Choke Point (Betweenness):` 0.000127 | `Ripple Effect (Closeness):` 0.166846
  * `Imports (Out-Degree: 4):` crate::data::BreakPanesToNewTabResponse, crate::data::BreakPanesToTabWithIdResponse, crate::data::BreakPanesToTabWithIndexResponse, crate::data::ConnectToSession, crate::data::DeleteLayoutResponse, crate::data::EditLayoutResponse, crate::data::FloatingPaneCoordinates, crate::data::FocusOrCreateTabResponse...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `zellij-server/src/pty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_6: 6.609, file_cluster_4: 11.244, file_cluster_8: 14.812
- **Magnitude:** 1056.52 | **LOC:** 2262 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **47**; blast radius 1.192; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.7%), Mutation Surface (formerly State Flux) (50.3%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pty_thread_main` **(Many-Argument Workhorses)** (Impact: 178.1)
  * `spawn_terminals_for_layout` **(Many-Argument Workhorses)** (Impact: 173.0)
  * `spawn_terminals_for_layout_override` **(Many-Argument Workhorses)** (Impact: 120.6)
  * `apply_run_instruction` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `spawn_terminal` **(Many-Argument Workhorses)** (Impact: 40.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 40 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 339`, `args: 122`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 49`, `planned_debt: 1`
* *Architecture:* `api: 29`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 79`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.192
  * `Choke Point (Betweenness):` 0.000777 | `Ripple Effect (Closeness):` 0.067301
  * `Imports (Out-Degree: 17):` crate::ClientId, crate::ServerInstruction, crate::background_jobs::BackgroundJob, crate::background_jobs::write_session_state_to_disk, crate::global_async_runtime::get_tokio_runtime, crate::os_input_output::AsyncReader, crate::os_input_output::NullAsyncReader, crate::panes::PaneId...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `zellij-utils/src/input/actions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.315)
- **Top Global Matches:** file_cluster_12: 8.315, file_cluster_5: 9.484, file_cluster_7: 10.557
- **Magnitude:** 1042.88 | **LOC:** 3874 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 86.4%
- **Blast Radius:** changing it is visible to **38** in-repo importer(s); it depends on **43**; blast radius 12.47; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.5%), Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (53.5%), Mutation Surface (formerly State Flux) (12.7%)
- **Documentation Coverage:** 98.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `actions_from_cli` **(Many-Argument Workhorses)** (Impact: 473.4)
  * `suggest_key_fix` **(Compute Cores)** (Impact: 12.6)
  * `populate_originating_plugin` **(Compute Cores)** (Impact: 10.3)
  * `test_send_keys_multiple_keys` **(Annotated & Test Methods)** (Impact: 5.1)
  * `test_new_pane_tiled_with_tab_id` **(I/O & Config Routines)** (Impact: 5.1)
    * *Intent:* // Tab-targeting for pane creation commands
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 494`, `args: 263`, `func_start: 99`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 86`, `high_risk_execution: 54`, `state_mutation: 24`, `planned_debt: 4`
* *Architecture:* `api: 96`, `import: 20`
* *Defense:* `safety: 57`, `doc: 74`, `test: 358`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.47
  * `Choke Point (Betweenness):` 0.008286 | `Ripple Effect (Closeness):` 0.283903
  * `Imports (Out-Degree: 9):` crate::cli::CliAction, crate::data::BareKey, crate::data::CommandOrPlugin, crate::data::Direction, crate::data::FloatingPaneCoordinates, crate::data::InputMode, crate::data::KeyModifier, crate::data::KeyWithModifier...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.72)
- **Top Global Matches:** file_cluster_4: 6.72, file_cluster_9: 9.243, file_cluster_15: 10.216
- **Magnitude:** 1000.72 | **LOC:** 1234 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.872; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Connectivity (formerly Api Exposure) (53.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `combine_horizontally_aligned_panes_to_stack` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `combine_vertically_aligned_panes_to_stack` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `expand_pane` **(Compute Cores)** (Impact: 35.9)
  * `fill_space_over_visible_stacked_pane` **(Compute Cores)** (Impact: 28.2)
  * `resize_panes_in_stack` **(Many-Argument Workhorses)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 401`, `args: 115`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.872
  * `Choke Point (Betweenness):` 0.000466 | `Ripple Effect (Closeness):` 0.047864
  * `Imports (Out-Degree: 5):` stacked_panes_tests.rs, crate::panes::PaneId, crate::tab::MIN_TERMINAL_HEIGHT, crate::tab::Pane, std::cell::RefCell, std::collections::HashMap, std::collections::HashSet, std::rc::Rc...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `zellij-server/src/tab/unit/tab_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.317)
- **Top Global Matches:** file_cluster_7: 8.317, file_cluster_12: 10.237, file_cluster_14: 10.351
- **Magnitude:** 993.72 | **LOC:** 15590 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.689; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (59.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.0%), Debt Markers (formerly Tech Debt) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `close_pane_with_multiple_panes_to_the_left_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 8.0)
  * `close_pane_with_multiple_panes_to_the_right_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 8.0)
  * `create_new_tab_with_layout` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `close_pane_with_multiple_panes_above_it_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 7.0)
  * `close_pane_with_multiple_panes_below_it_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 894`, `args: 158`, `func_start: 157`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1632`, `high_risk_execution: 15`, `state_mutation: 28`, `fragile_debt: 60`
* *Architecture:* `io: 1`, `api: 149`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 1`, `test: 1326`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.689
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.055243
  * `Imports (Out-Degree: 12):` crate::ClientId, crate::os_input_output::AsyncReader, crate::os_input_output::ServerOsApi, crate::pane_groups::PaneGroups, crate::panes::PaneId, crate::panes::sixel::SixelImageStore, crate::screen::CopyOptions, crate::thread_bus::ThreadSenders...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/output/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.076)
- **Top Global Matches:** file_cluster_4: 7.076, file_cluster_0: 10.95, file_cluster_15: 11.292
- **Magnitude:** 993.7 | **LOC:** 1327 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **26**; blast radius 2.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (63.7%), Guard Balance (formerly Safety Score) (57.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove_covered_sixel_parts` **(Many-Argument Workhorses)** (Impact: 97.4)
  * `serialize_chunks` **(Many-Argument Workhorses)** (Impact: 75.9)
  * `remove_covered_parts` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `serialize_chunks_with_newlines` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `serialize_with_size` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 304`, `args: 83`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `state_mutation: 109`, `dead_code: 1`, `planned_debt: 6`, `unreferenced_by_name: 22`
* *Architecture:* `api: 68`, `import: 12`
* *Defense:* `safety: 38`, `doc: 1`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.619
  * `Choke Point (Betweenness):` 0.006179 | `Ripple Effect (Closeness):` 0.087803
  * `Imports (Out-Degree: 11):` unit, crate::ClientId, crate::panes::DEFAULT_STYLES, crate::panes::EMPTY_TERMINAL_CHARACTER, crate::panes::LinkHandler, crate::panes::PaneId, crate::panes::Row, crate::panes::Selection...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `default-plugins/session-manager/src/ui/components.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_4: 7.155, file_cluster_15: 9.088, file_cluster_0: 9.799
- **Magnitude:** 986.08 | **LOC:** 1848 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 3.568; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.8%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 96.1905% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_unified_results` **(Many-Argument Workhorses)** (Impact: 169.7)
  * `render_controls_line` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `render_new_session_block` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `render_new_session_folder_prompt` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `rebuild` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* /// Rebuild the cache from the current `unified_results`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 353`, `args: 64`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `state_mutation: 72`, `planned_debt: 1`
* *Architecture:* `api: 88`, `import: 11`
* *Defense:* `safety: 15`, `doc: 18`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.568
  * `Choke Point (Betweenness):` 0.000459 | `Ripple Effect (Closeness):` 0.01023
  * `Imports (Out-Degree: 5):` crate::ActiveScreen, crate::NewSessionInfo, crate::single_screen::UnifiedSearchResult, crate::ui::PaneUiInfo, crate::ui::SessionUiInfo, crate::ui::TabUiInfo, humantime::format_duration, self::*...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `zellij-utils/assets/prost_ipc/client_server_contract.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_0: 7.049, file_cluster_13: 8.015, file_cluster_2: 9.482
- **Magnitude:** 974.18 | **LOC:** 3175 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 89.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.4%), Complexity Load (formerly Cognitive Load) (2.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as_str_name` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
  * `from_str_name` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* /// Creates an enum from field names used in the ProtoBuf definition.
  * `as_str_name` **(State Mutators)** (Impact: 3.9)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
  * `from_str_name` **(State Mutators)** (Impact: 3.9)
    * *Intent:* /// Creates an enum from field names used in the ProtoBuf definition.
  * `as_str_name` **(State Mutators)** (Impact: 3.8)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 289`, `args: 36`, `func_start: 36`, `class_start: 257`
* *Risk/State:* None
* *Architecture:* `api: 792`
* *Defense:* `doc: 144`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mouse_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.337)
- **Top Global Matches:** file_cluster_6: 6.337, file_cluster_4: 10.964, file_cluster_8: 15.017
- **Magnitude:** 959.66 | **LOC:** 1689 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.765; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (55.2%), Guard Balance (formerly Safety Score) (49.0%), Connectivity (formerly Api Exposure) (42.3%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `determine_mouse_action` **(Many-Argument Workhorses)** (Impact: 137.3)
  * `edge_and_delta_to_strategies` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `execute_send_to_terminal` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `execute_mouse_action` **(Many-Argument Workhorses)** (Impact: 47.7)
  * `execute_update_hover` **(Many-Argument Workhorses)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 313`, `args: 84`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 63`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.765
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055014
  * `Imports (Out-Degree: 9):` Direction::*, Resize::*, crate::ClientId, crate::background_jobs::BackgroundJob, crate::panes::PaneId, crate::plugins::PluginInstruction, std::time::Instant, super::Pane...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-utils/src/ipc/protobuf_conversion.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.191)
- **Top Global Matches:** file_cluster_4: 9.191, file_cluster_15: 10.223, file_cluster_0: 10.476
- **Magnitude:** 959.44 | **LOC:** 4458 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **229**; blast radius 1.041; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.5%), Complexity Load (formerly Cognitive Load) (8.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_from` **(Many-Argument Workhorses)** (Impact: 299.1)
  * `try_from` **(Defensive Guards)** (Impact: 42.7)
  * `try_from` **(Defensive Guards)** (Impact: 33.1)
  * `try_from` **(Compute Cores)** (Impact: 26.4)
  * `try_from` **(Defensive Guards)** (Impact: 20.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 265`, `args: 437`, `func_start: 94`
* *Risk/State:* None
* *Architecture:* `import: 53`
* *Defense:* `safety: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.041
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.148557
  * `Imports (Out-Degree: 6):` crate::client_server_contract::client_server_contract::ActionMsg, crate::client_server_contract::client_server_contract::AreFloatingPanesVisibleAction, crate::client_server_contract::client_server_contract::AttachClientMsg, crate::client_server_contract::client_server_contract::AttachWatcherClientMsg, crate::client_server_contract::client_server_contract::BackgroundColorMsg, crate::client_server_contract::client_server_contract::BreakPaneAction, crate::client_server_contract::client_server_contract::BreakPaneLeftAction, crate::client_server_contract::client_server_contract::BreakPaneRightAction...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `default-plugins/strider/src/file_list_view.rs` (RUST) | Magnitude: 138.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 50, branch: 25, api: 24
- `default-plugins/session-manager/src/new_session_info.rs` (RUST) | Magnitude: 242.98 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 406, structural_boundaries: 67, args: 56, api: 47
- `zellij-server/src/panes/tiled_panes/unit/stacked_panes_tests.rs` (RUST) | Magnitude: 277.7 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1096, structural_boundaries: 188, args: 102, func_start: 74
- `default-plugins/status-bar/src/main.rs` (RUST) | Magnitude: 333.18 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 737, structural_boundaries: 152, core_var_decl: 119, design_snake_case: 113
- `default-plugins/session-manager/src/ui/mod.rs` (RUST) | Magnitude: 158.32 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 86, branch: 34, core_var_decl: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `zellij-client/assets/modals.js` (JAVASCRIPT) | Magnitude: 22.1 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 500, core_var_decl: 64, state_mutation: 43, design_camel_case: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `zellij-server/src/panes/search.rs` (RUST) | Magnitude: 503.42 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 504, structural_boundaries: 127, branch: 121, core_var_decl: 65
- `zellij-server/src/plugins/wasm_bridge.rs` (RUST) | Magnitude: 953.24 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 2071, structural_boundaries: 441, core_var_decl: 225, branch: 205
- `default-plugins/link/src/main.rs` (RUST) | Magnitude: 250.18 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 349, structural_boundaries: 97, branch: 65, core_var_decl: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `zellij-utils/assets/prost/api.input_mode.rs` (RUST) | Magnitude: 13.76 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 53, doc: 21, core_var_decl: 15, design_pascal_case: 14
- `zellij-server/src/pane_groups.rs` (RUST) | Magnitude: 186.26 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 409, structural_boundaries: 155, core_var_decl: 112, design_snake_case: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `default-plugins/share/src/token_management_screen.rs` (RUST) | Magnitude: 254.88 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 522, structural_boundaries: 131, core_var_decl: 100, design_snake_case: 97
- `zellij-server/src/plugins/pipes.rs` (RUST) | Magnitude: 156.2 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 60, branch: 26, core_var_decl: 25
- `default-plugins/layout-manager/src/screens/rename_layout.rs` (RUST) | Magnitude: 53.42 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 38, core_var_decl: 26, design_snake_case: 26
- `default-plugins/about/src/pages.rs` (RUST) | Magnitude: 455.1 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1002, structural_boundaries: 151, args: 97, branch: 91
- `zellij-client/assets/utils.js` (JAVASCRIPT) | Magnitude: 1.98 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, branch: 10, globals: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `default-plugins/status-bar/src/tip/mod.rs` (RUST) | Magnitude: 24.24 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 9, structural_boundaries: 8, indent_spaces: 3, import: 2
- `zellij-server/src/panes/mod.rs` (RUST) | Magnitude: 35.48 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, api: 20, import: 11, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `zellij-tile/src/prelude.rs` (RUST) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6
- `.github/workflows/release.yml` (YAML) | Magnitude: 119.56 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 365, branch: 56, args: 44, func_start: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `zellij-server/src/os_input_output_unix.rs` (RUST) | Magnitude: 243.4 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 415, structural_boundaries: 110, branch: 70, core_var_decl: 61
- `src/tests/e2e/remote_runner.rs` (RUST) | Magnitude: 370.44 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 923, structural_boundaries: 283, core_var_decl: 150, design_snake_case: 148

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zellij-server/src/tab/mod.rs` -> Churn: **75.4%** | Cog Load: 19.3547% | Debt: 97.5406%
- `zellij-server/src/panes/grid.rs` -> Churn: **67.49%** | Cog Load: 57.5363% | Debt: 10.2919%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `zellij-server/src/screen.rs` -> **Aram Drevekenin** (87.8% isolated ownership) | Magnitude: 4992.42
- `zellij-server/src/tab/mod.rs` -> **Aram Drevekenin** (93.1% isolated ownership) | Magnitude: 3661.3
- `zellij-server/src/panes/grid.rs` -> **Aram Drevekenin** (85.0% isolated ownership) | Magnitude: 3528.12
- `zellij-utils/src/kdl/mod.rs` -> **Aram Drevekenin** (81.8% isolated ownership) | Magnitude: 2974.6
- `zellij-server/src/plugins/unit/plugin_tests.rs` -> **Aram Drevekenin** (100.0% isolated ownership) | Magnitude: 1823.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `zellij-utils/src/data.rs` -> **Severity: 1.843** (Bridge: 0.0507 * Flux: 36.3724%)
- `zellij-server/src/panes/terminal_pane.rs` -> **Severity: 0.893** (Bridge: 0.0126 * Flux: 71.1419%)
- `zellij-server/src/tab/mod.rs` -> **Severity: 0.737** (Bridge: 0.0136 * Flux: 54.269%)
- `zellij-server/src/panes/grid.rs` -> **Severity: 0.726** (Bridge: 0.0073 * Flux: 99.9136%)
- `zellij-server/src/output/mod.rs` -> **Severity: 0.616** (Bridge: 0.0062 * Flux: 99.7507%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `zellij-utils/src/data.rs` -> **Severity: 18.381** (Embedded: 0.36 * Error Risk: 51.0536%)
- `zellij-utils/src/errors.rs` -> **Severity: 16.625** (Embedded: 0.3379 * Error Risk: 49.2052%)
- `zellij-utils/src/input/actions.rs` -> **Severity: 15.178** (Embedded: 0.2839 * Error Risk: 53.4602%)
- `zellij-utils/src/input/layout.rs` -> **Severity: 14.532** (Embedded: 0.2685 * Error Risk: 54.1189%)
- `zellij-utils/src/pane_size.rs` -> **Severity: 14.34** (Embedded: 0.267 * Error Risk: 53.7063%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zellij-utils/src/data.rs` -> **Severity: 8108.959** (Blast Radius: 83.757 * Doc Risk: 96.8153%)
- `zellij-utils/src/input/layout.rs` -> **Severity: 4426.8** (Blast Radius: 44.268 * Doc Risk: 100.0%)
- `zellij-utils/src/channels.rs` -> **Severity: 3648.25** (Blast Radius: 72.965 * Doc Risk: 50.0%)
- `zellij-utils/src/errors.rs` -> **Severity: 2674.711** (Blast Radius: 82.673 * Doc Risk: 32.3529%)
- `zellij-utils/src/consts.rs` -> **Severity: 2009.464** (Blast Radius: 32.786 * Doc Risk: 61.2903%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 399 literal sites + 207 sites through wrappers = 606

- `object_to_stdout` (function, debug_prints, primitive): 195 call sites in 1 files -- `zellij-tile/src/shim.rs`
- `print_text` (function, debug_prints, primitive): 4 call sites in 1 files -- `zellij-tile/src/ui_components/text.rs`
- `render_text_with_underline` (function, debug_prints, primitive): 3 call sites in 2 files -- `default-plugins/share/src/ui_components.rs`
- `render_search_term` (function, debug_prints, primitive): 2 call sites in 1 files -- `default-plugins/strider/src/shared.rs`
- `print_conversion_title_message` (function, debug_prints, primitive): 1 call sites in 1 files -- `zellij-client/src/old_config_converter/convert_old_yaml_files.rs`
- `print_converting_config_message` (function, debug_prints, primitive): 1 call sites in 1 files -- `zellij-client/src/old_config_converter/convert_old_yaml_files.rs`
- `status` (function, debug_prints, primitive): 1 call sites in 1 files -- `xtask/src/main.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 57622 call pairs -- scoped 17.8%, unique 0.0%, ambiguous 8.9%, external 73.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 57425 | 17.8% | 0.0% | 8.9% | 73.3% |
| javascript | 168 | 24.4% | 0.0% | 3.0% | 72.6% |
| shell | 29 | 0.0% | 0.0% | 0.0% | 100.0% |

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
