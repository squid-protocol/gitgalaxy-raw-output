# ARCHITECTURAL_BRIEF: css_doom_pure
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/NielsLeenheer/cssDOOM.git` |
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
- **Scope:** 114 analyzed artifact(s), 6740 LOC.
- **Load-bearing artifact:** `src/game/state.js` -- 28 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `index.css` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `index.html` at magnitude 438.25 (structural weight, not risk).
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
| Total Artifacts | 1047 |
| Analyzed Artifacts (Scanned) | 114 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 933 |
| Total LOC | 6740 |
| Volatility Index | 0.018 |
| % Scanned of codebase = | 10.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3868 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4376 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6419 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 54 | 4728 | 47.4% |
| CSS | 27 | 1793 | 23.7% |
| JSON | 14 | 14 | 12.3% |
| XML | 14 | 0 | 12.3% |
| PLAINTEXT | 3 | 0 | 2.6% |
| MARKDOWN | 1 | 0 | 0.9% |
| HTML | 1 | 205 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 114 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Declarative / Non-Code 17%, Large Core Modules (2) 15%, Large Core Modules 10%, Interface Declarations Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 99 | 86.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 11 | 9.6% |
| Static: Literature & Documentation | 4 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 933*

**Composition by Extension & Reason:**
- `.png`: 874x Excluded (Explicitly Denied Extension: '.png')
- `.wav`: 55x Excluded (Explicitly Denied Extension: '.wav')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 76.2 | 17.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 33.8 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 42.4 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.4 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 28.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 11 | 7 | 0 | `src/game/mechanics/doors.js` |
| guards | 321 | 52 | 10 | `src/game/entities/ai.js` |
| danger | 125 | 18 | 2 | `src/ui/hud.css` |
| concurrency | 75 | 16 | 2 | `src/shared/maps.js` |
| connectivity | 481 | 69 | 7 | `index.html` |
| io | 139 | 18 | 2 | `index.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 32 | 17 | 1 | `src/game/mechanics/doors.js` |
| serialization | 2 | 1 | 0 | `src/ui/debug.js` |
| regex | 1 | 1 | 0 | `src/renderer/scene/scene.js` |
| events | 121 | 14 | 2 | `src/ui/spectator.js` |
| tests | 0 | 0 | 0 | - |
| docs | 201 | 55 | 6 | `src/renderer/scene/entities/sprites.js` |
| debt | 35 | 6 | 0 | `src/ui/debug.js` |
| mutation | 2160 | 53 | 70 | `src/renderer/scene/culling.js` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 15 | 4 | 0 | `src/ui/hud.css` |
| ui | 114 | 22 | 2 | `src/ui/menu.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `index.html` (Hits: 44)
- `src/ui/hud.css` (Hits: 24)
- `src/renderer/scene/mechanics/switches.css` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **state.js** (`src/game/state.js`) — 28 inbound connections
2. **constants.js** (`src/game/constants.js`) — 20 inbound connections
3. **dom.js** (`src/renderer/dom.js`) — 19 inbound connections
4. **maps.js** (`src/shared/maps.js`) — 19 inbound connections
5. **index.js** (`src/renderer/index.js`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.css** (`index.css`) — 26 outbound dependencies
2. **index.js** (`index.js`) — 13 outbound dependencies
3. **scene.js** (`src/renderer/scene/scene.js`) — 13 outbound dependencies
4. **weapons.js** (`src/game/entities/weapons.js`) — 12 outbound dependencies
5. **ai.js** (`src/game/entities/ai.js`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `updateSingleEnemy` **(Many-Argument Workhorses)** (@ `src/game/entities/ai.js`) -> Impact: **105.2** | LOC: 136
  * *Intent:* /** * Updates a single enemy's AI behavior for one frame. * */
- `canMoveTo` **(Many-Argument Workhorses)** (@ `src/game/physics.js`) -> Impact: **88.6** | LOC: 79
  * *Intent:* // ============================================================================ // Collision Detection // ============================================...
- `pickMoveDirection` **(Defensive Guards)** (@ `src/game/entities/ai.js`) -> Impact: **77.8** | LOC: 75
  * *Intent:* * 5. Exhaustive scan of all 8 directions (random forward/backward order) * 6. Last resort: try the turnaround direction * 7. Give up: set DI_NODIR (en...
- `updateCulling` **(I/O & Config Routines)** (@ `src/renderer/scene/culling.js`) -> Impact: **70.5** | LOC: 150
  * *Intent:* /** * Run culling checks on all scene elements. Called each frame from the game loop. * Elements are hidden/shown by toggling the `hidden` attribute w...
- `hasLineOfSight` **(Many-Argument Workhorses)** (@ `src/game/line-of-sight.js`) -> Impact: **66.8** | LOC: 83
- `rayHitPoint` **(Many-Argument Workhorses)** (@ `src/game/physics.js`) -> Impact: **59.2** | LOC: 57
  * *Intent:* // ============================================================================ // Ray Casting // ====================================================...
- `buildHorizontalSurface` **(Many-Argument Workhorses)** (@ `src/renderer/scene/surfaces/horizontal.js`) -> Impact: **58.4** | LOC: 95
  * *Intent:* /** * Builds a horizontal floor or ceiling surface for a sector. * * The sector's polygon shape is applied via CSS clip-path: * - Simple sectors use p...
- `initKeyboardInput` **(Compute Cores)** (@ `src/input/keyboard.js`) -> Impact: **56.5** | LOC: 91
  * *Intent:* /** * Initializes keyboard event listeners. * Should be called once during application startup. */
- `checkPickups` **(Defensive Guards)** (@ `src/game/player/pickups.js`) -> Impact: **43.0** | LOC: 99
- `moveEnemyToward` **(Many-Argument Workhorses)** (@ `src/game/entities/ai.js`) -> Impact: **38.1** | LOC: 47
  * *Intent:* /** * Moves an enemy toward a target position using DOOM-style cardinal movement. * Each frame, the enemy moves along its current direction at its con...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/game` | 9 | 889.46 | 30.28% | 0.0% |
| `src/game/entities` | 5 | 802.66 | 30.82% | 0.0% |
| `src/ui` | 10 | 609.49 | 21.58% | 0.0% |
| `src/renderer/scene` | 9 | 575.75 | 18.16% | 0.0% |
| `__monolith__` | 6 | 493.03 | 8.43% | 7.07% |
| `src/game/mechanics` | 5 | 388.7 | 40.12% | 0.0% |
| `src/renderer/scene/surfaces` | 7 | 379.35 | 21.36% | 0.0% |
| `src/input` | 5 | 364.16 | 43.74% | 0.0% |
| `src/renderer/scene/entities` | 9 | 319.04 | 11.11% | 0.0% |
| `src/game/player` | 2 | 271.74 | 54.37% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `index.html` -> **42.4365%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/game/mechanics/crushers.js` -> **100.0%** Exposure
- `src/game/mechanics/lifts.js` -> **100.0%** Exposure
- `src/game/movement.js` -> **100.0%** Exposure
- `src/game/player/damage.js` -> **100.0%** Exposure
- `src/game/player/pickups.js` -> **100.0%** Exposure

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
- **Unknown Dependencies:** `30` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.816)
- **Top Global Matches:** file_cluster_13: 5.816, file_cluster_10: 7.274, file_cluster_2: 7.358
- **Magnitude:** 438.25 | **LOC:** 230 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (90.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%), Debt Markers (formerly Tech Debt) (42.4%), Connectivity (formerly Api Exposure) (15.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 61`, `args: 78`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 44`, `api: 65`, `import: 2`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` favicon.svg, icon.png, index.css, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/culling.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.902)
- **Top Global Matches:** file_cluster_6: 6.902, file_cluster_8: 11.976, file_cluster_4: 13.717
- **Magnitude:** 407.66 | **LOC:** 450 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 7.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (59.9%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateCulling` **(I/O & Config Routines)** (Impact: 70.5)
    * *Intent:* /** * Run culling checks on all scene elements. Called each frame from the game loop. * Elements are...
  * `behindSkyWall` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from t...
  * `debugSkyTrace` **(Defensive Guards)** (Impact: 33.7)
    * *Intent:* /** Debug: trace sky culling for a wall by ID. Call via traceSky('ld489'). */
  * `surfaceInFrustum` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* /** * Tests whether a surface bounding box is within the frustum. * Checks corners, center, and whet...
  * `rayIntersectsAABB` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* /** * Tests whether a ray from (ox,oy) in direction (dx,dy) intersects an AABB. * Uses the slab meth...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 54`, `args: 11`, `func_start: 10`
* *Risk/State:* `state_mutation: 59`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 19`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.059
  * `Choke Point (Betweenness):` 0.002867 | `Ripple Effect (Closeness):` 0.098496
  * `Imports (Out-Degree: 4):` constants.js, state.js, spectator.js, dom.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/game/entities/ai.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_8: 6.608, file_cluster_6: 17.392, file_cluster_3: 19.747
- **Magnitude:** 388.96 | **LOC:** 491 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 5.963; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateSingleEnemy` **(Many-Argument Workhorses)** (Impact: 105.2)
    * *Intent:* /** * Updates a single enemy's AI behavior for one frame. * */
  * `pickMoveDirection` **(Defensive Guards)** (Impact: 77.8)
    * *Intent:* * 5. Exhaustive scan of all 8 directions (random forward/backward order) * 6. Last resort: try the t...
  * `moveEnemyToward` **(Many-Argument Workhorses)** (Impact: 38.1)
    * *Intent:* /** * Moves an enemy toward a target position using DOOM-style cardinal movement. * Each frame, the ...
  * `updateAllEnemies` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* /** * Main per-frame update for all enemies. Iterates all thing elements, skipping * dead/collected ...
  * `resolveTarget` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* /** * Resolves the current chase target's position. Returns {x, y} for wherever * the enemy should m...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 49`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 24`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.963
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.011799
  * `Imports (Out-Degree: 12):` audio.js, index.js, constants.js, line-of-sight.js, physics.js, damage.js, sound-propagation.js, state.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/spectator.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.963)
- **Top Global Matches:** file_cluster_10: 7.963, file_cluster_15: 8.471, file_cluster_16: 9.819
- **Magnitude:** 313.1 | **LOC:** 346 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 8.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spectatorLoop` **(I/O & Config Routines)** (Impact: 16.4)
  * `updatePlayerSprite` **(Defensive Guards)** (Impact: 15.5)
  * `transitionCeilings` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* /** * Fades ceiling elements in or out via inline transition+opacity. */
  * `switchSpectatorMode` **(Defensive Guards)** (Impact: 8.8)
  * `spectate` **(Callbacks & Closures)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 45`, `args: 37`, `func_start: 15`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 16`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.553
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.081915
  * `Imports (Out-Degree: 2):` state.js, dom.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/game/physics.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.361)
- **Top Global Matches:** file_cluster_8: 6.361, file_cluster_6: 17.337, file_cluster_3: 19.642
- **Magnitude:** 246.96 | **LOC:** 270 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **5**; blast radius 18.762; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (54.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canMoveTo` **(Many-Argument Workhorses)** (Impact: 88.6)
    * *Intent:* // ============================================================================ // Collision Detecti...
  * `rayHitPoint` **(Many-Argument Workhorses)** (Impact: 59.2)
    * *Intent:* // ============================================================================ // Ray Casting // ==...
  * `getFloorHeightAt` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* // ============================================================================ // Floor / Sector Lo...
  * `getSectorAt` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /** * Returns the sector polygon data at a world position, or null if not found. */
  * `getSectorLightAt` **(Defensive Guards)** (Impact: 5.4)
    * *Intent:* /** * Returns the light level of the sector at the given world position, * defaulting to 255 (full b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 58`, `args: 10`, `func_start: 6`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 10`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.762
  * `Choke Point (Betweenness):` 0.004496 | `Ripple Effect (Closeness):` 0.148948
  * `Imports (Out-Degree: 5):` constants.js, geometry.js, doors.js, spatial-grid.js, state.js
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/game/spatial-grid.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.418)
- **Top Global Matches:** file_cluster_4: 6.418, file_cluster_15: 10.541, file_cluster_6: 11.127
- **Magnitude:** 242.34 | **LOC:** 192 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 12.15; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (55.1%)
- **Documentation Coverage:** 41.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forEachSightLineInAABB` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* /** * Calls `callback(line)` for each unique sight line in cells overlapping the AABB. * Falls back ...
  * `buildSpatialGrid` **(I/O & Config Routines)** (Impact: 24.9)
    * *Intent:* /** * Builds the spatial grid from the current map data. Must be called after * the map is loaded an...
  * `forEachWallInAABB` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* // ============================================================================ // Query API // ====...
  * `forEachSectorAt` **(Defensive Guards)** (Impact: 22.8)
    * *Intent:* /** * Calls `callback(sector)` for each unique sector polygon whose bounding box * covers the given ...
  * `insertAABB` **(Many-Argument Workhorses)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 46`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 10`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.15
  * `Choke Point (Betweenness):` 0.002568 | `Ripple Effect (Closeness):` 0.128865
  * `Imports (Out-Degree: 1):` maps.js
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ui/debug.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.23)
- **Top Global Matches:** file_cluster_10: 8.23, file_cluster_15: 8.388, file_cluster_9: 8.693
- **Magnitude:** 220.38 | **LOC:** 372 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 5.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nearby` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* /** Dump all walls, doors, things, and projectiles near the player */
  * `initDebugMenu` **(I/O & Config Routines)** (Impact: 18.4)
  * `updateDebugStats` **(I/O & Config Routines)** (Impact: 8.9)
    * *Intent:* /** Update the stats text. Called each frame from the game loop. */
  * `load` **(Defensive Guards)** (Impact: 5.0)
  * `teleportTo` **(Callbacks & Closures)** (Impact: 4.7)
    * *Intent:* /** Teleport player to a thing by type name (e.g. teleportTo('spectre')) */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 35`, `args: 19`, `func_start: 8`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 5`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.772
  * `Choke Point (Betweenness):` 0.000292 | `Ripple Effect (Closeness):` 0.00885
  * `Imports (Out-Degree: 9):` constants.js, physics.js, spatial-grid.js, state.js, dom.js, camera.js, constants.js, culling.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/renderer/scene/entities/sprites.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.182)
- **Top Global Matches:** file_cluster_15: 6.182, file_cluster_10: 7.398, file_cluster_16: 8.244
- **Magnitude:** 199.54 | **LOC:** 248 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 13.611; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%)
- **Documentation Coverage:** 15.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateEnemyRotation` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* /** * Computes the DOOM sprite rotation frame (1-8) based on the viewing angle * from the player to ...
  * `resetEnemy` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* /** Resets sprite visuals and position for enemy respawn. */
  * `setEnemyState` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // ============================================================================ // Enemy sprite — hi...
  * `reparentThingToSector` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** * Reparent a thing's DOM element to a different sector container using moveBefore(). * This pres...
  * `setSpriteFrame` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* // ============================================================================ // Low-level helpers...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 31`, `args: 17`, `func_start: 14`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 12`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.611
  * `Choke Point (Betweenness):` 0.000509 | `Ripple Effect (Closeness):` 0.140873
  * `Imports (Out-Degree: 2):` state.js, dom.js
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/game/entities/weapons.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.238)
- **Top Global Matches:** file_cluster_4: 7.238, file_cluster_6: 9.756, file_cluster_9: 12.128
- **Magnitude:** 169.26 | **LOC:** 402 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **12**; blast radius 11.31; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fireWeapon` **(I/O & Config Routines)** (Impact: 19.4)
    * *Intent:* * * Firing mechanics: * 1. Checks preconditions: player alive, not already firing, not mid-switch, *...
  * `rocketExplosion` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* /** * Handles a player rocket explosion at a given position. Deals splash damage * to all shootable ...
  * `checkWeaponHit` **(I/O & Config Routines)** (Impact: 16.6)
    * *Intent:* /** * Performs weapon hit detection and damage for the current weapon shot. * * Weapon types handled...
  * `findHitscanTarget` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* // ============================================================================ // Player Hit Detect...
  * `rollWeaponDamage` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /** * Rolls random weapon damage matching original DOOM formulas. * * Based on: linuxdoom-1.10/p_psp...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 46`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 3`, `doc: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.31
  * `Choke Point (Betweenness):` 0.018294 | `Ripple Effect (Closeness):` 0.117031
  * `Imports (Out-Degree: 14):` audio.js, index.js, index.js, constants.js, line-of-sight.js, physics.js, damage.js, pickups.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.209)
- **Top Global Matches:** file_cluster_8: 8.209, file_cluster_6: 10.16, file_cluster_4: 18.271
- **Magnitude:** 167.5 | **LOC:** 230 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 15.48; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (55.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildSkyWalls` **(I/O & Config Routines)** (Impact: 35.5)
    * *Intent:* /** * Builds "sky walls" — tall occluder surfaces on the perimeter of sky-ceiling * sectors. These e...
  * `buildWalls` **(I/O & Config Routines)** (Impact: 15.7)
  * `createWallElement` **(Many-Argument Workhorses)** (Impact: 5.3)
    * *Intent:* /** Creates a wall DOM element from wall data with the given floor/ceiling heights. */
  * `setContainerLight` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /** Sets --light on a container from its sector's light level. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 25`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.48
  * `Choke Point (Betweenness):` 0.008588 | `Ripple Effect (Closeness):` 0.118237
  * `Imports (Out-Degree: 4):` maps.js, dom.js, constants.js, sectors.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/renderer/scene/surfaces/horizontal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.929)
- **Top Global Matches:** file_cluster_3: 6.929, file_cluster_8: 21.097, file_cluster_6: 33.983
- **Magnitude:** 148.5 | **LOC:** 131 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 8.913; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Complexity Load (formerly Cognitive Load) (41.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildHorizontalSurface` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* /** * Builds a horizontal floor or ceiling surface for a sector. * * The sector's polygon shape is a...
  * `isRectangular` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Checks if a polygon's vertices exactly match its bounding box corners, * meaning the polygon i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 13`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 11`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.913
  * `Choke Point (Betweenness):` 0.000625 | `Ripple Effect (Closeness):` 0.094008
  * `Imports (Out-Degree: 3):` dom.js, constants.js, sectors.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/game/player/damage.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.516)
- **Top Global Matches:** file_cluster_9: 7.516, file_cluster_15: 8.539, file_cluster_16: 9.527
- **Magnitude:** 144.94 | **LOC:** 197 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 15.177; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (54.1%)
- **Documentation Coverage:** 70.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSectorDamageAt` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* // A timer accumulates elapsed time while the player stands in a damaging // sector. Every 32 tics (...
  * `checkSectorDamage` **(Defensive Guards)** (Impact: 13.6)
  * `damagePlayer` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* // Damage flash overlay system: // When the player takes damage, the renderer shows a brief red flas...
  * `clearSceneState` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* // resetGameState (full reset): // Used when starting a new game or respawning after death. Resets A...
  * `resetGameState` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* // Full reset — new game or respawn after death
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 25`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.177
  * `Choke Point (Betweenness):` 0.025599 | `Ripple Effect (Closeness):` 0.15292
  * `Imports (Out-Degree: 11):` audio.js, hud.js, index.js, constants.js, weapons.js, geometry.js, spatial-grid.js, state.js
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/game/entities/combat.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.767)
- **Top Global Matches:** file_cluster_6: 6.767, file_cluster_4: 11.463, file_cluster_8: 14.997
- **Magnitude:** 132.34 | **LOC:** 281 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 7.577; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (54.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `damageEnemy` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* * The `source` parameter identifies who dealt the damage: * - 'player' — the player fired a weapon o...
  * `barrelExplosion` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* // ============================================================================ // Barrel Explosion ...
  * `enemyHitscanAttackEnemy` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /** * Hitscan attack against another enemy during infighting. * Same angular spread and damage rolls...
  * `enemyHitscanAttack` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* * Performs an enemy hitscan attack (used by Zombieman and Shotgun Guy). * * Based on: linuxdoom-1.10...
  * `checkMissileRange` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* /** * Distance-based attack probability check for ranged enemies. * * Based on: linuxdoom-1.10/p_ene...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 29`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.577
  * `Choke Point (Betweenness):` 0.003127 | `Ripple Effect (Closeness):` 0.091752
  * `Imports (Out-Degree: 11):` audio.js, index.js, maps.js, constants.js, line-of-sight.js, damage.js, pickups.js, state.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/game/player/pickups.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.428)
- **Top Global Matches:** file_cluster_6: 8.428, file_cluster_8: 13.097, file_cluster_4: 14.294
- **Magnitude:** 126.8 | **LOC:** 199 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 7.235; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (55.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (55.3%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkPickups` **(Defensive Guards)** (Impact: 43.0)
  * `updatePowerups` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Tick down all active powerup durations. Called each frame from the game loop. * Based on: linu...
  * `activatePowerup` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* // updatePowerups() decrements the timers and removes expired effects. // // Effects: // invulnerabi...
  * `hasPowerup` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** Returns true if the named powerup is currently active. */
  * `triggerPickupFlash` **(State Mutators)** (Impact: 1.2)
    * *Intent:* /** * Triggers a brief golden flash overlay when the player picks up an item. * Rapid successive pic...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 20`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 16`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.235
  * `Choke Point (Betweenness):` 0.000601 | `Ripple Effect (Closeness):` 0.091752
  * `Imports (Out-Degree: 8):` audio.js, index.js, constants.js, weapons.js, state.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/input/touch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.771)
- **Top Global Matches:** file_cluster_4: 8.771, file_cluster_6: 10.85, file_cluster_10: 13.27
- **Magnitude:** 125.24 | **LOC:** 262 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 5.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupPointerHandlers` **(Callbacks & Closures)** (Impact: 28.8)
    * *Intent:* // ============================================================================ // Pointer Handlers ...
  * `releaseJoystick` **(Defensive Guards)** (Impact: 4.7)
  * `releaseFire` **(Defensive Guards)** (Impact: 4.6)
  * `releaseLook` **(Defensive Guards)** (Impact: 4.5)
  * `initTouchInput` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* /** * Initialise touch input. Only creates UI and attaches handlers on * touch-capable devices. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 48`, `args: 18`, `func_start: 9`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.772
  * `Choke Point (Betweenness):` 0.00028 | `Ripple Effect (Closeness):` 0.00885
  * `Imports (Out-Degree: 8):` weapons.js, doors.js, lifts.js, switches.js, state.js, maps.js, menu.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/game/mechanics/doors.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.112)
- **Top Global Matches:** file_cluster_6: 8.112, file_cluster_4: 11.891, file_cluster_8: 15.885
- **Magnitude:** 123.3 | **LOC:** 203 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 12.968; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (47.7%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initDoors` **(Defensive Guards)** (Impact: 25.1)
    * *Intent:* /** * Initialize all doors from map data. * Creates container elements for door animation, moves rel...
  * `tryOpenDoor` **(I/O & Config Routines)** (Impact: 13.1)
    * *Intent:* /** * Attempt to open a door in front of the player (triggered by the "use" key). * Casts a point fo...
  * `toggleDoor` **(Callbacks & Closures)** (Impact: 9.9)
    * *Intent:* /** * Toggle a door open. If already open, reset the auto-close timer. * The renderer handles the op...
  * `closeDoor` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * Close a door by resetting its state and triggering the close animation. * If the player is ins...
  * `getDoorEntry` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* /** * Returns the door entry for a door wall, or null if not a door. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 37`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 17`, `doc: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.968
  * `Choke Point (Betweenness):` 0.007533 | `Ripple Effect (Closeness):` 0.133361
  * `Imports (Out-Degree: 7):` audio.js, index.js, maps.js, constants.js, physics.js, state.js
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/game/mechanics/lifts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.058)
- **Top Global Matches:** file_cluster_15: 7.058, file_cluster_9: 7.765, file_cluster_16: 8.263
- **Magnitude:** 115.1 | **LOC:** 212 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **5**; blast radius 9.874; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (76.9%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (54.6%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkWalkOverTriggers` **(I/O & Config Routines)** (Impact: 10.9)
    * *Intent:* /** * Check all walk-over trigger lines each frame. * For each trigger linedef, compute the closest ...
  * `tryUseLift` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Attempt to activate a lift in front of the player (triggered by the "use" key). * Checks nearb...
  * `updatePlayerFromLift` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* /** * Called each frame to interpolate lift heights in sync with the renderer animation. * Uses an e...
  * `initLifts` **(I/O & Config Routines)** (Impact: 6.5)
  * `activateLift` **(Defensive Guards)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 31`, `args: 8`, `func_start: 6`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 6`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.874
  * `Choke Point (Betweenness):` 0.003497 | `Ripple Effect (Closeness):` 0.10522
  * `Imports (Out-Degree: 6):` audio.js, index.js, maps.js, constants.js, state.js
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/input/keyboard.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.175)
- **Top Global Matches:** file_cluster_3: 9.175, file_cluster_8: 21.948, file_cluster_6: 34.518
- **Magnitude:** 98.82 | **LOC:** 159 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 5.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%), Complexity Load (formerly Cognitive Load) (52.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initKeyboardInput` **(Compute Cores)** (Impact: 56.5)
    * *Intent:* /** * Initializes keyboard event listeners. * Should be called once during application startup. */
  * `getInput` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* // ============================================================================ // Input Provider //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 43`, `args: 5`, `func_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 1`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.772
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.00885
  * `Imports (Out-Degree: 9):` constants.js, weapons.js, doors.js, lifts.js, switches.js, state.js, maps.js, menu.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/game/sound-propagation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.097)
- **Top Global Matches:** file_cluster_9: 7.097, file_cluster_15: 8.303, file_cluster_16: 9.67
- **Magnitude:** 98.66 | **LOC:** 167 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 12.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (52.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `propagateSound` **(I/O & Config Routines)** (Impact: 13.3)
    * *Intent:* /** * Floods sound from the player's current position through connected sectors. * Marks all reachab...
  * `getLineOpening` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* /** * Computes the vertical opening of a two-sided linedef, accounting for door state. * Based on: l...
  * `buildSectorAdjacency` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /** * Builds the sector adjacency graph from the current map's linedefs/sidedefs. * Called once per ...
  * `isSectorAlerted` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Returns true if the given sector index was reached by the last sound propagation. */
  * `clearSoundAlert` **(State Mutators)** (Impact: 1.2)
    * *Intent:* /** * Clears the alerted sectors (called on map clear/reset). */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 24`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 3`, `api: 4`, `import: 3`
* *Defense:* `safety: 6`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.445
  * `Choke Point (Betweenness):` 0.002291 | `Ripple Effect (Closeness):` 0.143363
  * `Imports (Out-Degree: 3):` maps.js, physics.js, state.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/shared/maps.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.375)
- **Top Global Matches:** file_cluster_11: 8.375, file_cluster_15: 8.6, file_cluster_10: 9.44
- **Magnitude:** 97.52 | **LOC:** 98 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **6**; blast radius 41.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (72.4%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadMap` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* /** * Fetches a map JSON and applies it to game state: sets player position, * resets game/level sta...
  * `getNextMap` **(Interface Declarations)** (Impact: 3.2)
  * `applyPlayerStart` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* /** * Sets player position and angle from the current map's start data. */
  * `clearMap` **(State Mutators)** (Impact: 1.1)
    * *Intent:* /** Clears the map data reference (for teardown/GC). */
  * `getSecretExitMap` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 9`, `import: 6`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.784
  * `Choke Point (Betweenness):` 0.055692 | `Ripple Effect (Closeness):` 0.204804
  * `Imports (Out-Degree: 6):` constants.js, damage.js, sound-propagation.js, state.js, scene.js, overlay.js
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/game/line-of-sight.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.516)
- **Top Global Matches:** file_cluster_1: 5.516, file_cluster_3: 48.228, file_cluster_8: 70.065
- **Magnitude:** 96.14 | **LOC:** 104 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 7.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.9%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hasLineOfSight` **(Many-Argument Workhorses)** (Impact: 66.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 26`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.655
  * `Choke Point (Betweenness):` 0.000807 | `Ripple Effect (Closeness):` 0.094008
  * `Imports (Out-Degree: 6):` constants.js, geometry.js, doors.js, physics.js, spatial-grid.js, state.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/renderer/scene/entities/things.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.544)
- **Top Global Matches:** file_cluster_1: 6.544, file_cluster_3: 48.357, file_cluster_8: 70.146
- **Magnitude:** 96.06 | **LOC:** 127 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 6.159; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (65.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (52.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildThings` **(I/O & Config Routines)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.159
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.092492
  * `Imports (Out-Degree: 7):` constants.js, physics.js, state.js, maps.js, dom.js, constants.js, sectors.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/game/entities/projectiles.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.544)
- **Top Global Matches:** file_cluster_8: 7.544, file_cluster_6: 17.539, file_cluster_3: 20.373
- **Magnitude:** 91.64 | **LOC:** 227 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 6.386; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (54.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateProjectiles` **(I/O & Config Routines)** (Impact: 25.4)
    * *Intent:* /** * Updates all active projectiles each frame. Position is calculated from * elapsed time since sp...
  * `spawnProjectile` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* /** * Spawns an enemy projectile (e.g. Imp fireball, Cacodemon lightning ball). * The projectile is ...
  * `spawnFireballExplosion` **(State Mutators)** (Impact: 2.1)
    * *Intent:* // ============================================================================ // Fireball Explosio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 23`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.386
  * `Choke Point (Betweenness):` 0.000371 | `Ripple Effect (Closeness):` 0.019912
  * `Imports (Out-Degree: 10):` audio.js, index.js, constants.js, line-of-sight.js, physics.js, damage.js, state.js, combat.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/renderer/scene/scene.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.68)
- **Top Global Matches:** file_cluster_15: 9.68, file_cluster_13: 10.243, file_cluster_10: 10.293
- **Magnitude:** 84.56 | **LOC:** 119 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 11.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.0%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `preloadTextures` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* /** * Collects all unique texture URLs used in the scene (wall textures, floor * flats, and sprite i...
  * `teardownScene` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* /** * Tears down the current scene, releasing DOM nodes and GPU resources. * Call before buildScene(...
  * `onComplete` **(State Mutators)** (Impact: 2.1)
  * `buildScene` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 20`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 13`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.336
  * `Choke Point (Betweenness):` 0.024568 | `Ripple Effect (Closeness):` 0.127434
  * `Imports (Out-Degree: 13):` crushers.js, doors.js, lifts.js, spatial-grid.js, dom.js, camera.js, culling.js, player.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/game/mechanics/crushers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.409)
- **Top Global Matches:** file_cluster_15: 6.409, file_cluster_16: 7.667, file_cluster_2: 7.726
- **Magnitude:** 78.98 | **LOC:** 135 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 7.468; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.7%), Connectivity (formerly Api Exposure) (36.0%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkCrusherDamage` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* /** * Checks if the player is standing in a crusher sector and being crushed. * Uses a simple AABB c...
  * `updateCrushers` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /** * Updates all active crushers each frame. Moves the ceiling height, updates * the renderer with ...
  * `initCrushers` **(I/O & Config Routines)** (Impact: 6.3)
  * `activateCrusher` **(Compute Cores)** (Impact: 4.5)
    * *Intent:* /** * Activates a crusher by sector index. Called when the player triggers the * switch or walk-over...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.468
  * `Choke Point (Betweenness):` 0.002522 | `Ripple Effect (Closeness):` 0.099731
  * `Imports (Out-Degree: 6):` index.js, maps.js, physics.js, damage.js, state.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/ui/debug.js` (JAVASCRIPT) | Magnitude: 220.38 | Delta: **0.158** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 264, state_mutation: 57, core_var_decl: 55, design_snake_case: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/renderer/scene/scene.css` (CSS) | Magnitude: 0.94 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, class_start: 5, structural_boundaries: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `index.js` (JAVASCRIPT) | Magnitude: 42.72 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 23, import: 14, concurrency: 9
- `src/renderer/scene/mechanics/switches.js` (JAVASCRIPT) | Magnitude: 8.48 | Delta: **0.188** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: events: 3, branch: 2, listeners: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/renderer/index.js` (JAVASCRIPT) | Magnitude: 25.3 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 10, indent_spaces: 4
- `index.css` (CSS) | Magnitude: 0.78 | Delta: **0.281** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 26

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/game/entities/ai.js` -> Churn: **94.64%** | Cog Load: 51.6375% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `index.html` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 438.25
- `src/game/entities/ai.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 388.96
- `src/game/physics.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 246.96
- `src/renderer/scene/entities/sprites.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 199.54
- `src/game/entities/weapons.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 169.26

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/shared/maps.js` -> **Severity: 5.569** (Bridge: 0.0557 * Flux: 100.0%)
- `src/game/player/damage.js` -> **Severity: 2.56** (Bridge: 0.0256 * Flux: 100.0%)
- `src/renderer/scene/scene.js` -> **Severity: 2.457** (Bridge: 0.0246 * Flux: 100.0%)
- `src/game/entities/weapons.js` -> **Severity: 1.828** (Bridge: 0.0183 * Flux: 99.9265%)
- `src/renderer/scene/surfaces/walls.js` -> **Severity: 0.859** (Bridge: 0.0086 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/shared/maps.js` -> **Severity: 13.024** (Embedded: 0.2048 * Error Risk: 63.5931%)
- `src/game/player/damage.js` -> **Severity: 11.636** (Embedded: 0.1529 * Error Risk: 76.0892%)
- `src/game/sound-propagation.js` -> **Severity: 9.869** (Embedded: 0.1434 * Error Risk: 68.8388%)
- `src/game/spatial-grid.js` -> **Severity: 9.864** (Embedded: 0.1289 * Error Risk: 76.5436%)
- `src/audio/audio.js` -> **Severity: 8.935** (Embedded: 0.1496 * Error Risk: 59.7388%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/shared/maps.js` -> **Severity: 1857.065** (Blast Radius: 41.784 * Doc Risk: 44.4444%)
- `src/audio/audio.js` -> **Severity: 1236.88** (Blast Radius: 15.461 * Doc Risk: 80.0%)
- `src/game/player/damage.js` -> **Severity: 1062.39** (Blast Radius: 15.177 * Doc Risk: 70.0%)
- `src/renderer/scene/sectors.js` -> **Severity: 945.375** (Blast Radius: 15.126 * Doc Risk: 62.5%)
- `src/renderer/scene/entities/player.js` -> **Severity: 818.08** (Blast Radius: 10.226 * Doc Risk: 80.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 844 call pairs -- scoped 40.5%, unique 0.0%, ambiguous 0.0%, external 59.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 844 | 40.5% | 0.0% | 0.0% | 59.5% |

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
