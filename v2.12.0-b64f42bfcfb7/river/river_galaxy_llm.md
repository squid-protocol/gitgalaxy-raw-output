# ARCHITECTURAL_BRIEF: river
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ifreund/river.git` |
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
- **Scope:** 70 analyzed artifact(s), 11165 LOC.
- **Load-bearing artifact:** `river/util.zig` -- 44 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `river/Seat.zig` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `river/Window.zig` at magnitude 586.84 (structural weight, not risk).
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
| Total Artifacts | 87 |
| Analyzed Artifacts (Scanned) | 70 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 11165 |
| Volatility Index | 0.1 |
| % Scanned of codebase = | 80.5% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3526 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 66.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.605 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 54 | 11137 | 77.1% |
| XML | 11 | 0 | 15.7% |
| MARKDOWN | 4 | 0 | 5.7% |
| C | 1 | 28 | 1.4% |

## 4.1 SOURCE ENCODINGS
All 70 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 40%, Data / Markup / Trivial 21%, State Mutators Files 20%, Large Core Modules (3) 7%, Type Conversions Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 66 | 94.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 5.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.desktop`: 1x Excluded (Unsupported Extension: '.desktop')
- `.scd`: 1x Excluded (Unsupported Extension: '.scd')
- `.xml`: 1x Excluded (Static Asset Blob without Intent: 1855 LOC)
- `.zon`: 1x Statistical Anomaly (Z-Score: -6.41 < -4.75)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 35.3 | 9.7 | 9.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 41.9 | 48.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.9 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 80.8 | 31.5 | 34.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 14.7 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.3 | 43.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 2.3 | 2.0 | 4.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 8.3 | 100.0 | 31.5 | 23.1 | 8.3 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.4 | 87.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 231 | 36 | 8 | `river/Cursor.zig` |
| cleanup | 338 | 50 | 10 | `river/Server.zig` |
| guards | 1153 | 54 | 45 | `river/Seat.zig` |
| danger | 441 | 50 | 18 | `river/LibinputDevice.zig` |
| concurrency | 41 | 5 | 0 | `river/LockManager.zig` |
| connectivity | 295 | 55 | 9 | `river/Window.zig` |
| io | 13 | 9 | 1 | `river/main.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 8 | 1 | `river/Cursor.zig` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 48 | 42 | 1 | `river/process.zig` |
| tests | 15 | 3 | 0 | `common/slotmap.zig` |
| docs | 345 | 34 | 15 | `common/deque.zig` |
| debt | 33 | 19 | 2 | `river/KeyboardGroup.zig` |
| mutation | 2133 | 55 | 72 | `river/Window.zig` |
| dead_code | 1 | 1 | 0 | `river/wlroots_log_wrapper.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 96 | 16 | 6 | `river/Cursor.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.9285**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `river/main.zig` (Hits: 5)
- `build.zig` (Hits: 1)
- `river/Cursor.zig` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.zig** (`river/util.zig`) — 44 inbound connections
2. **main.zig** (`river/main.zig`) — 42 inbound connections
3. **Seat.zig** (`river/Seat.zig`) — 21 inbound connections
4. **SceneNodeData.zig** (`river/SceneNodeData.zig`) — 15 inbound connections
5. **Output.zig** (`river/Output.zig`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Seat.zig** (`river/Seat.zig`) — 27 outbound dependencies
2. **Server.zig** (`river/Server.zig`) — 25 outbound dependencies
3. **Cursor.zig** (`river/Cursor.zig`) — 18 outbound dependencies
4. **Window.zig** (`river/Window.zig`) — 15 outbound dependencies
5. **InputManager.zig** (`river/InputManager.zig`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handleRequest` **(Many-Argument Workhorses)** (@ `river/LibinputDevice.zig`) -> Impact: **198.5** | LOC: 330
- `handleRequest` **(Many-Argument Workhorses)** (@ `river/Window.zig`) -> Impact: **76.3** | LOC: 167
- `createObject` **(Many-Argument Workhorses)** (@ `river/LibinputDevice.zig`) -> Impact: **63.7** | LOC: 130
- `manageStart` **(Defensive Guards)** (@ `river/Window.zig`) -> Impact: **55.5** | LOC: 149
  * *Intent:* /// Send dirty state as part of a manage sequence.
- `commitOutputState` **(Defensive Guards)** (@ `river/OutputManager.zig`) -> Impact: **49.8** | LOC: 147
- `manageStart` **(Defensive Guards)** (@ `river/Seat.zig`) -> Impact: **45.5** | LOC: 147
- `Deque` **(Compute Cores)** (@ `common/deque.zig`) -> Impact: **45.0** | LOC: 250
  * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the queue is O(1).
- `handleKey` **(Many-Argument Workhorses)** (@ `river/KeyboardGroup.zig`) -> Impact: **44.9** | LOC: 101
- `processButton` **(Many-Argument Workhorses)** (@ `river/Cursor.zig`) -> Impact: **36.4** | LOC: 104
- `build` **(I/O & Config Routines)** (@ `build.zig`) -> Impact: **36.0** | LOC: 240

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `river` | 51 | 4982.8 | 11.77% | 5.09% |
| `common` | 3 | 340.66 | 9.98% | 7.47% |
| `__monolith__` | 5 | 54.64 | 1.78% | 0.0% |
| `protocol` | 5 | 52.6 | 0.0% | 0.0% |
| `logo` | 3 | 31.56 | 0.0% | 0.0% |
| `protocol/upstream` | 3 | 31.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `river/wlroots_log_wrapper.c` -> **37.7541%** Exposure
- `river/TextInput.zig` -> **35.4054%** Exposure
- `river/Keyboard.zig` -> **18.5489%** Exposure
- `river/IdleInhibitManager.zig` -> **18.2426%** Exposure
- `river/KeyboardGroup.zig` -> **16.8487%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `common/deque.zig` -> **100.0%** Exposure
- `river/Window.zig` -> **99.8502%** Exposure
- `river/Keyboard.zig` -> **99.6869%** Exposure
- `river/XdgToplevel.zig` -> **99.5891%** Exposure
- `river/Decoration.zig` -> **98.9199%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `river/wlroots_log_wrapper.c` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `446` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `river/Window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.609)
- **Top Global Matches:** file_cluster_4: 7.609, file_cluster_12: 9.119, file_cluster_15: 11.391
- **Magnitude:** 586.84 | **LOC:** 1212 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 84.2%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **15**; blast radius 28.804; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (74.5%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 70.1754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `manageStart` **(Defensive Guards)** (Impact: 55.5)
    * *Intent:* /// Send dirty state as part of a manage sequence.
  * `manageFinish` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* /// Applies window management state from the window manager and sends a configure /// to the window ...
  * `renderStart` **(I/O & Config Routines)** (Impact: 17.7)
  * `applySurfaceClip` **(Many-Argument Workhorses)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 66 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 86`, `args: 29`, `func_start: 29`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 91`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 32`, `import: 16`
* *Defense:* `safety: 97`, `doc: 50`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.804
  * `Choke Point (Betweenness):` 0.062661 | `Ripple Effect (Closeness):` 0.347455
  * `Imports (Out-Degree: 11):` Decoration.zig, Output.zig, Scene.zig, SceneNodeData.zig, Seat.zig, WmNode.zig, XdgToplevel.zig, XwaylandWindow.zig...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `river/Seat.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.194)
- **Top Global Matches:** file_cluster_12: 7.194, file_cluster_4: 9.391, file_cluster_7: 9.606
- **Magnitude:** 422.7 | **LOC:** 1035 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 92.9%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **27**; blast radius 43.404; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.0%), Connectivity (formerly Api Exposure) (80.8%), Guard Balance (formerly Safety Score) (48.8%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `manageStart` **(Defensive Guards)** (Impact: 45.5)
  * `handleRequest` **(Defensive Guards)** (Impact: 23.1)
  * `manageFinish` **(Defensive Guards)** (Impact: 22.9)
  * `matchXkbBinding` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* /// Handle any user-defined mapping for passed keycode, modifiers and keyboard state /// Returns tru...
  * `focus` **(Defensive Guards)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 55`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 43`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 27`
* *Defense:* `safety: 98`, `doc: 15`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.404
  * `Choke Point (Betweenness):` 0.185478 | `Ripple Effect (Closeness):` 0.377857
  * `Imports (Out-Degree: 22):` Cursor.zig, DragIcon.zig, InputDevice.zig, InputManager.zig, InputRelay.zig, Keyboard.zig, KeyboardGroup.zig, LayerShellSeat.zig...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `river/Cursor.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.167)
- **Top Global Matches:** file_cluster_12: 7.167, file_cluster_7: 9.387, file_cluster_5: 10.069
- **Magnitude:** 316.6 | **LOC:** 928 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 9.183; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Mutation Surface (formerly State Flux) (73.4%), Guard Balance (formerly Safety Score) (50.3%), Connectivity (formerly Api Exposure) (45.8%)
- **Documentation Coverage:** 94.3396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processButton` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `processMotionRelative` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `handleRequestSetCursor` **(Defensive Guards)** (Impact: 15.7)
  * `updateHovered` **(Defensive Guards)** (Impact: 14.6)
  * `setTheme` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* /// Set the cursor theme for the given seat, as well as the xwayland theme if /// this is the defaul...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 27`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 12`, `import: 18`
* *Defense:* `safety: 60`, `doc: 26`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.183
  * `Choke Point (Betweenness):` 0.008544 | `Ripple Effect (Closeness):` 0.247775
  * `Imports (Out-Degree: 14):` DragIcon.zig, InputDevice.zig, LockSurface.zig, Output.zig, PointerBinding.zig, PointerConstraint.zig, Scene.zig, Seat.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LibinputDevice.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.438)
- **Top Global Matches:** file_cluster_8: 13.438, file_cluster_6: 14.231, file_cluster_4: 20.806
- **Magnitude:** 301.2 | **LOC:** 550 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 9.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.1%), Connectivity (formerly Api Exposure) (34.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.3%), Complexity Load (formerly Cognitive Load) (16.1%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 198.5)
  * `createObject` **(Many-Argument Workhorses)** (Impact: 63.7)
  * `send` **(Compute Cores)** (Impact: 5.6)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
  * `init` **(Defensive Guards)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 75`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 70`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.064
  * `Choke Point (Betweenness):` 0.004296 | `Ripple Effect (Closeness):` 0.209921
  * `Imports (Out-Degree: 5):` InputDevice.zig, LibinputAccelConfig.zig, c.zig, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/WindowManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.454)
- **Top Global Matches:** file_cluster_12: 7.454, file_cluster_4: 8.56, file_cluster_15: 9.407
- **Magnitude:** 224.66 | **LOC:** 563 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 90.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 6.537; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.4%), Guard Balance (formerly Safety Score) (51.1%), Connectivity (formerly Api Exposure) (43.1%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderFinish` **(Defensive Guards)** (Impact: 29.3)
    * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn wi...
  * `manageStart` **(Defensive Guards)** (Impact: 16.5)
  * `manageFinish` **(Defensive Guards)** (Impact: 11.7)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 10.8)
  * `handleDestroy` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 32`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `import: 13`
* *Defense:* `safety: 36`, `doc: 15`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.537
  * `Choke Point (Betweenness):` 0.001381 | `Ripple Effect (Closeness):` 0.219048
  * `Imports (Out-Degree: 9):` Output.zig, Scene.zig, Seat.zig, ShellSurface.zig, Window.zig, WmNode.zig, main.zig, slotmap...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Output.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.048)
- **Top Global Matches:** file_cluster_4: 7.048, file_cluster_12: 8.837, file_cluster_15: 9.979
- **Magnitude:** 223.32 | **LOC:** 549 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **9**; blast radius 26.968; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.2%), Connectivity (formerly Api Exposure) (56.3%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderAndCommit` **(Compute Cores)** (Impact: 25.8)
  * `manageStart` **(Defensive Guards)** (Impact: 22.6)
  * `create` **(Defensive Guards)** (Impact: 13.1)
  * `handleDestroy` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `handlePresent` **(Compute Cores)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 33`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 33`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 9`, `import: 9`
* *Defense:* `safety: 28`, `doc: 28`, `test: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.968
  * `Choke Point (Betweenness):` 0.016991 | `Ripple Effect (Closeness):` 0.339647
  * `Imports (Out-Degree: 6):` LayerShellOutput.zig, LockSurface.zig, SceneNodeData.zig, Window.zig, main.zig, std, util.zig, wayland...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `common/deque.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.423)
- **Top Global Matches:** file_cluster_12: 7.423, file_cluster_4: 7.661, file_cluster_15: 8.026
- **Magnitude:** 211.34 | **LOC:** 435 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 7.354; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.7%), Guard Balance (formerly Safety Score) (35.3%)
- **Documentation Coverage:** 6.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Deque` **(Compute Cores)** (Impact: 45.0)
    * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the...
  * `ensureTotalCapacityPrecise` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// If the current capacity is less than `new_capacity`, this function will /// modify the deque so ...
  * `fuzzAgainstArrayList` **(Defensive Guards)** (Impact: 19.3)
  * `bufferIndex` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /// Returns the index in `buffer` where the element at the given /// index in the logical deque is s...
  * `growCapacity` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// Called when memory growth is necessary. Returns a capacity larger than /// minimum that grows su...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 46`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 15`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 62`, `doc: 68`, `test: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248481
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/OutputManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.203)
- **Top Global Matches:** file_cluster_4: 9.203, file_cluster_12: 11.094, file_cluster_7: 12.418
- **Magnitude:** 208.62 | **LOC:** 455 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 6.537; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.4%), Guard Balance (formerly Safety Score) (53.7%), Connectivity (formerly Api Exposure) (33.3%)
- **Documentation Coverage:** 70.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commitOutputState` **(Defensive Guards)** (Impact: 49.8)
  * `handleManagerApply` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `validateConfigCoordinates` **(Compute Cores)** (Impact: 15.6)
  * `handlePowerManagerSetMode` **(Type Conversions)** (Impact: 13.3)
  * `autoLayout` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 25`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 39`, `doc: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.537
  * `Choke Point (Betweenness):` 0.00092 | `Ripple Effect (Closeness):` 0.219048
  * `Imports (Out-Degree: 8):` DragIcon.zig, LockSurface.zig, Output.zig, SceneNodeData.zig, Window.zig, XwaylandOverrideRedirect.zig, build_options, main.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/XdgToplevel.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.763)
- **Top Global Matches:** file_cluster_7: 7.763, file_cluster_12: 7.938, file_cluster_5: 9.69
- **Magnitude:** 198.1 | **LOC:** 475 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 10.993; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.3%)
- **Documentation Coverage:** 77.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /// Send a configure event, return true if the configure should be tracked /// and current surfaces ...
  * `handleCommit` **(Type Conversions)** (Impact: 19.0)
  * `needsConfigure` **(Compute Cores)** (Impact: 16.5)
  * `handleRequestFullscreen` **(Type Conversions)** (Impact: 7.8)
  * `handleAckConfigure` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 30`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 32`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 16`, `doc: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.993
  * `Choke Point (Betweenness):` 0.010342 | `Ripple Effect (Closeness):` 0.249823
  * `Imports (Out-Degree: 7):` Output.zig, Seat.zig, Window.zig, XdgDecoration.zig, XdgPopup.zig, main.zig, std, util.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/KeyboardGroup.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.756)
- **Top Global Matches:** file_cluster_4: 5.756, file_cluster_12: 9.707, file_cluster_15: 9.803
- **Magnitude:** 170.34 | **LOC:** 442 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 10.231; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.9%), Mutation Surface (formerly State Flux) (62.0%), Guard Balance (formerly Safety Score) (47.1%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleKey` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `processKey` **(Compute Cores)** (Impact: 15.5)
  * `match` **(Compute Cores)** (Impact: 13.6)
  * `unref` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `ledUpdate` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 39`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `safety: 25`, `doc: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.231
  * `Choke Point (Betweenness):` 0.000214 | `Ripple Effect (Closeness):` 0.247775
  * `Imports (Out-Degree: 6):` InputDevice.zig, Keyboard.zig, Seat.zig, XkbBinding.zig, main.zig, std, util.zig, wayland...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/Server.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.712)
- **Top Global Matches:** file_cluster_12: 6.712, file_cluster_7: 8.549, file_cluster_5: 9.72
- **Magnitude:** 150.12 | **LOC:** 573 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 21.255; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%), Guard Balance (formerly Safety Score) (41.1%), Mutation Surface (formerly State Flux) (35.3%), Connectivity (formerly Api Exposure) (24.8%)
- **Documentation Coverage:** 63.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allowlist` **(Defensive Guards)** (Impact: 16.3)
    * *Intent:* /// Returns true if the global is allowlisted for security contexts
  * `init` **(Defensive Guards)** (Impact: 15.9)
  * `globalFilter` **(Defensive Guards)** (Impact: 15.2)
  * `handleRequestSetCursorShape` **(Defensive Guards)** (Impact: 13.8)
  * `start` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* /// Create the socket, start the backend, and setup the environment
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 30`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 10`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 25`
* *Defense:* `safety: 77`, `doc: 5`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.255
  * `Choke Point (Betweenness):` 0.15832 | `Ripple Effect (Closeness):` 0.321581
  * `Imports (Out-Degree: 21):` IdleInhibitManager.zig, InputManager.zig, LayerShell.zig, LibinputConfig.zig, LockManager.zig, Output.zig, OutputManager.zig, Scene.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Keyboard.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.167)
- **Top Global Matches:** file_cluster_15: 7.167, file_cluster_11: 7.455, file_cluster_12: 7.524
- **Magnitude:** 134.62 | **LOC:** 251 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 16.923; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.4%), Connectivity (formerly Api Exposure) (61.4%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Defensive Guards)** (Impact: 20.3)
  * `processKey` **(Defensive Guards)** (Impact: 9.3)
  * `setGroup` **(Defensive Guards)** (Impact: 8.1)
  * `setKeymap` **(Defensive Guards)** (Impact: 7.6)
  * `maybeDestroy` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 16`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 25`, `doc: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.923
  * `Choke Point (Betweenness):` 0.004737 | `Ripple Effect (Closeness):` 0.265163
  * `Imports (Out-Degree: 5):` InputDevice.zig, KeyboardGroup.zig, Seat.zig, main.zig, std, util.zig, wayland, wlroots...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `river/InputDevice.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.673)
- **Top Global Matches:** file_cluster_12: 7.673, file_cluster_5: 7.999, file_cluster_7: 9.287
- **Magnitude:** 133.42 | **LOC:** 296 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **11**; blast radius 18.805; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%), Guard Balance (formerly Safety Score) (52.1%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `deinit` **(Defensive Guards)** (Impact: 8.4)
  * `handleRemove` **(Defensive Guards)** (Impact: 6.4)
  * `createObject` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 20`, `doc: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.805
  * `Choke Point (Betweenness):` 0.026611 | `Ripple Effect (Closeness):` 0.272329
  * `Imports (Out-Degree: 8):` Keyboard.zig, LibinputDevice.zig, Seat.zig, Tablet.zig, XkbKeyboard.zig, c.zig, main.zig, std...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `river/XwaylandWindow.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.645)
- **Top Global Matches:** file_cluster_15: 6.645, file_cluster_2: 7.527, file_cluster_16: 7.795
- **Magnitude:** 124.94 | **LOC:** 347 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 93.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 11.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /// Always returns false as we do not care about frame perfection for Xwayland windows.
  * `handleSetSizeHints` **(Defensive Guards)** (Impact: 9.4)
  * `create` **(Defensive Guards)** (Impact: 6.2)
  * `handleSetOverrideRedirect` **(Defensive Guards)** (Impact: 5.3)
  * `handleSetDecorations` **(State Mutators)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 6`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 12`, `doc: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.554
  * `Choke Point (Betweenness):` 0.000352 | `Ripple Effect (Closeness):` 0.247775
  * `Imports (Out-Degree: 5):` Output.zig, Window.zig, XwaylandOverrideRedirect.zig, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/TabletTool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.512)
- **Top Global Matches:** file_cluster_4: 6.512, file_cluster_12: 10.337, file_cluster_15: 10.494
- **Magnitude:** 110.8 | **LOC:** 271 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 7.095; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.1%), Connectivity (formerly Api Exposure) (42.3%), Mutation Surface (formerly State Flux) (34.4%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `axis` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `passthrough` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* /// Send a motion event for the surface under the tablet tool's cursor if any. /// Send a proximity_...
  * `tip` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `allowSetCursor` **(Compute Cores)** (Impact: 6.7)
  * `get` **(Type Conversions)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 12`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 11`, `doc: 7`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.095
  * `Choke Point (Betweenness):` 0.000714 | `Ripple Effect (Closeness):` 0.229004
  * `Imports (Out-Degree: 3):` Tablet.zig, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.578)
- **Top Global Matches:** file_cluster_6: 8.578, file_cluster_4: 10.12, file_cluster_12: 15.572
- **Magnitude:** 105.22 | **LOC:** 295 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **9**; blast radius 91.632; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.3%), Connectivity (formerly Api Exposure) (55.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.0%), Guard Balance (formerly Safety Score) (39.2%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 35.3)
  * `logFn` **(Defensive Guards)** (Impact: 11.9)
  * `defaultInitPath` **(Defensive Guards)** (Impact: 9.2)
  * `grepRiverctl` **(Defensive Guards)** (Impact: 8.0)
  * `detectClassic` **(Defensive Guards)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 33`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`
* *Architecture:* `io: 5`, `api: 5`, `import: 9`
* *Defense:* `safety: 45`, `doc: 2`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.632
  * `Choke Point (Betweenness):` 0.184441 | `Ripple Effect (Closeness):` 0.604571
  * `Imports (Out-Degree: 5):` Server.zig, build_options, builtin, c.zig, flags, process.zig, std, util.zig...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `river/XkbKeyboard.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_12: 7.466, file_cluster_9: 9.559, file_cluster_7: 9.704
- **Magnitude:** 97.66 | **LOC:** 208 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 9.527; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.8%), Connectivity (formerly Api Exposure) (36.7%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sendState` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `createObject` **(Defensive Guards)** (Impact: 19.2)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
  * `init` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 13`, `doc: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.527
  * `Choke Point (Betweenness):` 0.006405 | `Ripple Effect (Closeness):` 0.209921
  * `Imports (Out-Degree: 5):` InputDevice.zig, Keyboard.zig, XkbKeymap.zig, main.zig, std, util.zig, wayland, wlroots...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XkbBinding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.165)
- **Top Global Matches:** file_cluster_12: 7.165, file_cluster_7: 7.797, file_cluster_5: 9.417
- **Magnitude:** 87.54 | **LOC:** 229 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 10.193; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.9%), Guard Balance (formerly Safety Score) (54.9%), Connectivity (formerly Api Exposure) (45.7%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /// Compare binding with given keycode, modifiers and keyboard state
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `handleDestroy` **(Defensive Guards)** (Impact: 7.6)
  * `create` **(Many-Argument Workhorses)** (Impact: 4.4)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 12`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 10`, `doc: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.193
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.245761
  * `Imports (Out-Degree: 4):` Keyboard.zig, Seat.zig, main.zig, std, util.zig, wayland, wlroots, xkbcommon
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/LockManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.124)
- **Top Global Matches:** file_cluster_12: 7.124, file_cluster_15: 8.701, file_cluster_16: 9.896
- **Magnitude:** 83.84 | **LOC:** 246 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 6.537; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Guard Balance (formerly Safety Score) (50.2%), Connectivity (formerly Api Exposure) (33.3%), Complexity Load (formerly Cognitive Load) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybeLock` **(Defensive Guards)** (Impact: 13.0)
  * `handleLock` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `lockSurfaceFromOutput` **(Type Conversions)** (Impact: 7.6)
  * `handleUnlock` **(Defensive Guards)** (Impact: 4.0)
  * `handleDestroy` **(State Mutators)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 15`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 15`, `doc: 12`, `sync_locks: 32`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.537
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.219048
  * `Imports (Out-Degree: 4):` LockSurface.zig, Output.zig, build_options, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/InputManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.866)
- **Top Global Matches:** file_cluster_12: 6.866, file_cluster_7: 8.808, file_cluster_15: 9.853
- **Magnitude:** 81.36 | **LOC:** 288 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 8.214; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.3%), Guard Balance (formerly Safety Score) (44.4%), Connectivity (formerly Api Exposure) (34.6%), Mutation Surface (formerly State Flux) (17.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleRequest` **(Defensive Guards)** (Impact: 18.1)
  * `bind` **(Defensive Guards)** (Impact: 7.6)
  * `init` **(Defensive Guards)** (Impact: 6.1)
  * `handleNewVirtualPointer` **(State Mutators)** (Impact: 6.0)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 12`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 27`, `doc: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.214
  * `Choke Point (Betweenness):` 0.007826 | `Ripple Effect (Closeness):` 0.265163
  * `Imports (Out-Degree: 8):` InputDevice.zig, InputRelay.zig, Keyboard.zig, PointerConstraint.zig, Seat.zig, TextInput.zig, build_options, main.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LayerShell.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.176)
- **Top Global Matches:** file_cluster_12: 8.176, file_cluster_7: 9.173, file_cluster_5: 9.591
- **Magnitude:** 77.64 | **LOC:** 194 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 6.537; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.2%), Guard Balance (formerly Safety Score) (54.7%), Connectivity (formerly Api Exposure) (29.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleNewSurface` **(Many-Argument Workhorses)** (Impact: 16.2)
  * `checkExclusiveFocus` **(Defensive Guards)** (Impact: 14.3)
  * `handleRequest` **(Type Conversions)** (Impact: 13.7)
  * `supported` **(Defensive Guards)** (Impact: 6.1)
  * `bind` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 18`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.537
  * `Choke Point (Betweenness):` 0.002413 | `Ripple Effect (Closeness):` 0.219048
  * `Imports (Out-Degree: 9):` LayerShellOutput.zig, LayerShellSeat.zig, LayerSurface.zig, Output.zig, SceneNodeData.zig, Seat.zig, main.zig, slotmap...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Decoration.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.2)
- **Top Global Matches:** file_cluster_12: 7.2, file_cluster_7: 8.461, file_cluster_5: 9.87
- **Magnitude:** 75.46 | **LOC:** 166 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 7.902; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (54.5%), Connectivity (formerly Api Exposure) (35.8%), Complexity Load (formerly Cognitive Load) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderFinish` **(Compute Cores)** (Impact: 10.0)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 8.9)
  * `create` **(Many-Argument Workhorses)** (Impact: 6.6)
  * `clientCommit` **(Type Conversions)** (Impact: 6.1)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 9`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.232527
  * `Imports (Out-Degree: 3):` Scene.zig, build_options, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `common/slotmap.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.37)
- **Top Global Matches:** file_cluster_15: 6.37, file_cluster_12: 7.61, file_cluster_16: 8.385
- **Magnitude:** 74.16 | **LOC:** 272 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 11.213; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.5%), Mutation Surface (formerly State Flux) (51.8%), Guard Balance (formerly Safety Score) (18.6%), Debt Markers (formerly Tech Debt) (9.4%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SlotMap` **(Compute Cores)** (Impact: 17.0)
  * `getSlot` **(Compute Cores)** (Impact: 5.6)
  * `put` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `next` **(Defensive Guards)** (Impact: 4.7)
  * `remove` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 91`, `doc: 8`, `test: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.24654
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `river/PointerConstraint.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.212)
- **Top Global Matches:** file_cluster_7: 8.212, file_cluster_5: 9.53, file_cluster_14: 9.894
- **Magnitude:** 72.4 | **LOC:** 223 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 8.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (42.3%), Complexity Load (formerly Cognitive Load) (11.8%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybeActivate` **(Type Conversions)** (Impact: 10.0)
  * `updateState` **(Type Conversions)** (Impact: 8.7)
    * *Intent:* /// Called when the cursor position or content in the scene graph changes
  * `handleCommit` **(Type Conversions)** (Impact: 7.9)
    * *Intent:* // It is necessary to listen for the commit event rather than the set_region // event as the latter ...
  * `handleDestroy` **(Type Conversions)** (Impact: 6.2)
  * `create` **(Defensive Guards)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 10`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 6`, `doc: 3`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.247775
  * `Imports (Out-Degree: 3):` Seat.zig, main.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/InputRelay.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.782)
- **Top Global Matches:** file_cluster_12: 6.782, file_cluster_15: 7.91, file_cluster_2: 8.458
- **Magnitude:** 71.44 | **LOC:** 234 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 13.803; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.3%), Guard Balance (formerly Safety Score) (44.7%), Connectivity (formerly Api Exposure) (43.4%), Mutation Surface (formerly State Flux) (27.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `focus` **(Defensive Guards)** (Impact: 15.5)
  * `handleInputMethodCommit` **(Defensive Guards)** (Impact: 10.0)
  * `sendInputMethodState` **(Defensive Guards)** (Impact: 8.7)
  * `newInputMethod` **(Defensive Guards)** (Impact: 6.3)
  * `disableTextInput` **(Defensive Guards)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 8`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 15`, `doc: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.803
  * `Choke Point (Betweenness):` 0.010461 | `Ripple Effect (Closeness):` 0.262857
  * `Imports (Out-Degree: 4):` InputPopup.zig, Seat.zig, TextInput.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `river/XkbKeymap.zig` (ZIG) | Magnitude: 21.06 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 14, design_snake_case: 13, pointers: 12
- `river/process.zig` (ZIG) | Magnitude: 17.58 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, branch: 7, core_var_decl: 6, design_snake_case: 6
- `river/Tablet.zig` (ZIG) | Magnitude: 8.04 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 10, globals: 8, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `river/XkbConfig.zig` (ZIG) | Magnitude: 53.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, pointers: 21, core_var_decl: 21, structural_boundaries: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `river/Window.zig` -> **Isaac Freund** (84.2% isolated ownership) | Magnitude: 586.84
- `river/Seat.zig` -> **Isaac Freund** (92.9% isolated ownership) | Magnitude: 422.7
- `river/Cursor.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 316.6
- `river/LibinputDevice.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 301.2
- `river/WindowManager.zig` -> **Isaac Freund** (90.9% isolated ownership) | Magnitude: 224.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `river/Seat.zig` -> **Severity: 16.952** (Bridge: 0.1855 * Flux: 91.3962%)
- `river/main.zig` -> **Severity: 11.856** (Bridge: 0.1844 * Flux: 64.2803%)
- `river/Window.zig` -> **Severity: 6.257** (Bridge: 0.0627 * Flux: 99.8502%)
- `river/Server.zig` -> **Severity: 5.587** (Bridge: 0.1583 * Flux: 35.2909%)
- `river/SceneNodeData.zig` -> **Severity: 3.019** (Bridge: 0.0344 * Flux: 87.6926%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `river/util.zig` -> **Severity: 31.918** (Embedded: 0.6311 * Error Risk: 50.5714%)
- `river/main.zig` -> **Severity: 23.686** (Embedded: 0.6046 * Error Risk: 39.1777%)
- `river/LockSurface.zig` -> **Severity: 22.731** (Embedded: 0.3053 * Error Risk: 74.4444%)
- `river/SceneNodeData.zig` -> **Severity: 20.897** (Embedded: 0.3149 * Error Risk: 66.3636%)
- `river/PointerConstraint.zig` -> **Severity: 19.822** (Embedded: 0.2478 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `river/main.zig` -> **Severity: 6664.148** (Blast Radius: 91.632 * Doc Risk: 72.7273%)
- `river/SceneNodeData.zig` -> **Severity: 4110.0** (Blast Radius: 41.1 * Doc Risk: 100.0%)
- `river/Seat.zig` -> **Severity: 3978.701** (Blast Radius: 43.404 * Doc Risk: 91.6667%)
- `river/Output.zig` -> **Severity: 2472.068** (Blast Radius: 26.968 * Doc Risk: 91.6667%)
- `common/flags.zig` -> **Severity: 2125.5** (Blast Radius: 21.255 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2745 call pairs -- scoped 5.8%, unique 0.0%, ambiguous 3.6%, external 90.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 2737 | 5.8% | 0.0% | 3.7% | 90.5% |
| c | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
