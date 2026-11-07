# ARCHITECTURAL_BRIEF: Excalibur
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/excaliburjs/Excalibur.git` |
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
- **Scope:** 752 analyzed artifact(s), 80925 LOC.
- **Load-bearing artifact:** `src/engine/math/vector.ts` -- 101 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/engine/index.ts` -- pulls in 65 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1797 |
| Analyzed Artifacts (Scanned) | 752 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1045 |
| Total LOC | 80925 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 41.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5139 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2183 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 26.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1808 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 32 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 548 | 71326 | 72.9% |
| HTML | 119 | 1810 | 15.8% |
| JSON | 19 | 604 | 2.5% |
| GLSL | 19 | 459 | 2.5% |
| MARKDOWN | 12 | 0 | 1.6% |
| JAVASCRIPT | 10 | 5951 | 1.3% |
| YAML | 9 | 282 | 1.2% |
| PLAINTEXT | 6 | 1 | 0.8% |
| XML | 4 | 1 | 0.5% |
| CSS | 4 | 434 | 0.5% |
| PYTHON | 2 | 57 | 0.3% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 722 |
| utf-8 | bom | 29 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Declarative / Non-Code 25%, Large Core Modules (3) 15%, Callbacks & Closures Files 9%, State Mutators Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 733 | 97.5% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 2.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1045*

**Composition by Extension & Reason:**
- `.png`: 597x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 73x Excluded (Explicitly Denied Extension: '.gif')
- `.ts`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14105 LOC), 1x Excluded (Static Asset Blob without Intent: 2081 LOC)
- `.md`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3214 LOC)
- `.mp3`: 18x Excluded (Explicitly Denied Extension: '.mp3')
- `.jpg`: 13x Excluded (Explicitly Denied Extension: '.jpg')
- `.mp4`: 12x Excluded (Explicitly Denied Extension: '.mp4')
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 9x Excluded (Explicitly Denied Extension: '.woff2')
- `.css`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.8 | 39.0 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.1 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 30.7 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 210 | 68 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| cleanup | 268 | 71 | 0 | `src/spec/vitest/engine-spec.ts` |
| guards | 3164 | 286 | 13 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| danger | 1370 | 214 | 4 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| concurrency | 1721 | 159 | 6 | `src/spec/vitest/coroutine-spec.ts` |
| connectivity | 4601 | 479 | 14 | `src/engine/events.ts` |
| io | 463 | 168 | 1 | `sandbox/index.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 3 | 0 | `scripts/apidocs.js` |
| time | 53 | 26 | 0 | `src/engine/entity-component-system/system-manager.ts` |
| serialization | 17 | 9 | 0 | `src/engine/util/serializer.ts` |
| regex | 41 | 12 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| events | 2490 | 304 | 7 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| tests | 7439 | 133 | 24 | `src/spec/vitest/action-spec.ts` |
| docs | 2722 | 350 | 10 | `src/engine/engine.ts` |
| debt | 601 | 148 | 2 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| mutation | 21928 | 661 | 79 | `sandbox/excalibur-dev-tools/dev-tools.js` |
| dead_code | 349 | 90 | 1 | `sandbox/src/game.ts` |
| credential | 2 | 1 | 0 | `src/spec/vitest/image-source-spec.ts` |
| threat | 1 | 1 | 0 | `playground/src/main.ts` |
| ml_ai | 1035 | 159 | 3 | `src/spec/vitest/action-spec.ts` |
| ui | 192 | 35 | 0 | `sandbox/excalibur-dev-tools/dev-tools.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sandbox/index.html` (Hits: 132)
- `src/spec/vitest/graph-spec.ts` (Hits: 25)
- `playground/index.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vector.ts** (`src/engine/math/vector.ts`) — 101 inbound connections
2. **color.ts** (`src/engine/color.ts`) — 54 inbound connections
3. **log.ts** (`src/engine/util/log.ts`) — 48 inbound connections
4. **entity.ts** (`src/engine/entity-component-system/entity.ts`) — 46 inbound connections
5. **test-utils.ts** (`src/spec/__util__/test-utils.ts`) — 45 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/engine/index.ts`) — 65 outbound dependencies
2. **index.ts** (`src/engine/graphics/index.ts`) — 46 outbound dependencies
3. **index.ts** (`src/engine/collision/index.ts`) — 37 outbound dependencies
4. **engine.ts** (`src/engine/engine.ts`) — 37 outbound dependencies
5. **excalibur-graphics-context-webgl.ts** (`src/engine/graphics/context/excalibur-graphics-context-webgl.ts`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/material-renderer/material-renderer.ts`) -> Impact: **134.4** | LOC: 158
- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/image-renderer/image-renderer.ts`) -> Impact: **109.0** | LOC: 157
- `draw` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/image-renderer-v2/image-renderer-v2.ts`) -> Impact: **105.9** | LOC: 95
- `constructor` **(Many-Argument Workhorses)** (@ `src/engine/engine.ts`) -> Impact: **98.4** | LOC: 270
  * *Intent:* * height: 0, // the height of the canvas * enableCanvasTransparency: true, // the transparencySection of the canvas * canvasElementId: '', // the DOM ...
- `rayCast` **(Many-Argument Workhorses)** (@ `src/engine/collision/detection/sparse-hash-grid-collision-processor.ts`) -> Impact: **71.8** | LOC: 119
- `glTypeToUniformTypeName` **(Compute Cores)** (@ `src/engine/graphics/context/shader.ts`) -> Impact: **71.4** | LOC: 112
  * *Intent:* /** * */
- `drawImage` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/excalibur-graphics-context-webgl.ts`) -> Impact: **68.4** | LOC: 39
- `constructor` **(Defensive Guards)** (@ `src/engine/graphics/font.ts`) -> Impact: **58.3** | LOC: 34
- `FindContactSeparation` **(Many-Argument Workhorses)** (@ `src/engine/collision/colliders/collision-jump-table.ts`) -> Impact: **58.0** | LOC: 86
- `drawImage` **(Many-Argument Workhorses)** (@ `src/engine/graphics/context/excalibur-graphics-context-2d-canvas.ts`) -> Impact: **55.1** | LOC: 27

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/spec/vitest` | 127 | 13392.13 | 4.66% | 0.0% |
| `__monolith__` | 17 | 5177.32 | 2.55% | 7.38% |
| `src/engine` | 24 | 4500.16 | 25.34% | 12.85% |
| `src/engine/graphics` | 33 | 3530.54 | 32.15% | 3.07% |
| `sandbox/excalibur-dev-tools` | 2 | 3307.82 | 29.01% | 100.0% |
| `src/engine/graphics/context` | 19 | 2393.92 | 28.05% | 17.09% |
| `src/engine/math` | 19 | 2325.3 | 26.59% | 1.8% |
| `src/engine/util` | 28 | 1937.23 | 33.88% | 8.05% |
| `src/engine/actions/action` | 22 | 1854.62 | 45.04% | 0.0% |
| `src/engine/collision/detection` | 11 | 1691.32 | 28.39% | 6.96% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `sandbox/excalibur-dev-tools/dev-tools.d.ts` -> **100.0%** Exposure
- `sandbox/tests/postprocessor/main.ts` -> **100.0%** Exposure
- `sandbox/tests/transition/index.ts` -> **100.0%** Exposure
- `src/engine/interfaces/lifecycle-events.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `sandbox/stats/stats.js` -> **100.0%** Exposure
- `src/engine/camera.ts` -> **100.0%** Exposure
- `src/engine/collision/colliders/polygon-collider.ts` -> **100.0%** Exposure
- `src/engine/collision/colliders/separating-axis.ts` -> **100.0%** Exposure
- `src/engine/collision/detection/collision-contact.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **0** Orphaned Functions | **103** Duplicates
- `src/engine/events.ts` -> **0** Orphaned Functions | **32** Duplicates
- `src/engine/interfaces/lifecycle-events.ts` -> **0** Orphaned Functions | **23** Duplicates
- `src/engine/input/gamepad.ts` -> **0** Orphaned Functions | **20** Duplicates
- `src/engine/tile-map/tile-map.ts` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `299` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.52)
- **Top Global Matches:** file_cluster_12: 8.52, file_cluster_7: 10.239, file_cluster_5: 11.004
- **Magnitude:** 3307.44 | **LOC:** 5255 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.817; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_processPointerToEntity` **(Defensive Guards)** (Impact: 32.5)
  * `createMonitor` **(Defensive Guards)** (Impact: 23.9)
  * `vn` **(Compute Cores)** (Impact: 23.2)
  * `rgb` **(Compute Cores)** (Impact: 23.2)
  * `S` **(Defensive Guards)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 826
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 1053`, `args: 981`, `func_start: 708`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 212`, `high_risk_execution: 2`, `state_mutation: 424`, `duplicate_logic: 103`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 353`, `test: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.817
  * `Choke Point (Betweenness):` 0.000472 | `Ripple Effect (Closeness):` 0.001332
  * `Imports (Out-Degree: 1):` excalibur
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/spec/vitest/excalibur-graphics-context-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.206)
- **Top Global Matches:** file_cluster_10: 4.206, file_cluster_2: 5.543, file_cluster_13: 6.569
- **Magnitude:** 1964.3 | **LOC:** 1223 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.637; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (46.2%), Dead Code Surface (formerly Dead Code) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 53 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 332
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 101`, `args: 63`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `concurrency: 67`, `import: 2`
* *Defense:* `safety: 5`, `test: 128`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/engine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.806)
- **Top Global Matches:** file_cluster_12: 7.806, file_cluster_5: 9.089, file_cluster_0: 9.428
- **Magnitude:** 881.04 | **LOC:** 1906 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **37**; blast radius 11.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.5%), Connectivity (formerly Api Exposure) (90.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 21.9895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 98.4)
    * *Intent:* * height: 0, // the height of the canvas * enableCanvasTransparency: true, // the transparencySectio...
  * `start` **(Defensive Guards)** (Impact: 17.2)
  * `_initialize` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* /** * Initializes the internal canvas, rendering context, display mode, and native event listeners *...
  * `_monitorPerformanceThresholdAndTriggerFallback` **(I/O & Config Routines)** (Impact: 14.6)
  * `useCanvas2DFallback` **(I/O & Config Routines)** (Impact: 12.1)
    * *Intent:* /** * Switches the engine's graphics context to the 2D Canvas. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 92
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 198`, `args: 113`, `func_start: 99`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 123`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 122`, `concurrency: 37`, `import: 47`
* *Defense:* `safety: 34`, `doc: 135`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.126
  * `Choke Point (Betweenness):` 0.037161 | `Ripple Effect (Closeness):` 0.121941
  * `Imports (Out-Degree: 40):` , actor, physics-config, color, context, debug-config, default-loader, director...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/spec/vitest/sound-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.326)
- **Top Global Matches:** file_cluster_10: 7.326, file_cluster_12: 8.125, file_cluster_7: 9.363
- **Magnitude:** 777.57 | **LOC:** 612 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.637; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.5%), Guard Balance (formerly Safety Score) (43.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 272
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 174`, `args: 118`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 41`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 67`, `import: 6`
* *Defense:* `safety: 6`, `test: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sound, util, web-audio, test-utils, @excalibur, context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/tile-map/tile-map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.42)
- **Top Global Matches:** file_cluster_12: 7.42, file_cluster_5: 7.804, file_cluster_0: 9.817
- **Magnitude:** 719.98 | **LOC:** 1004 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.949; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.5%)
- **Documentation Coverage:** 63.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_updateColliders` **(I/O & Config Routines)** (Impact: 30.6)
    * *Intent:* /** * Tiles colliders based on the solid tiles in the tilemap. */
  * `debug` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `draw` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* /** */
  * `constructor` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* /** */
  * `checkAndCombine` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* /** * Potentially merges the current collider into a list of previous ones, mutating the list * If c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 148`, `args: 87`, `func_start: 84`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 109`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `api: 100`, `concurrency: 13`, `import: 29`
* *Defense:* `safety: 23`, `doc: 48`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.949
  * `Choke Point (Betweenness):` 0.000325 | `Ripple Effect (Closeness):` 0.077524
  * `Imports (Out-Degree: 27):` body-component, bounding-box, collider-component, collider, composite-collider, shape, collision-type, debug...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/screen.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.641)
- **Top Global Matches:** file_cluster_12: 6.641, file_cluster_11: 7.373, file_cluster_16: 7.376
- **Magnitude:** 656.76 | **LOC:** 1232 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 2.517; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Connectivity (formerly Api Exposure) (59.6%)
- **Documentation Coverage:** 52.2059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enterFullscreen` **(Defensive Guards)** (Impact: 29.5)
    * *Intent:* /** * Requests to enter fullscreen using the browser fullscreen api, requires user interaction to be...
  * `_computeFitAndZoom` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `_setResolutionAndViewportByDisplayMode` **(I/O & Config Routines)** (Impact: 15.4)
    * *Intent:* /** * Sets the resolution and viewport based on the selected display mode. */
  * `applyResolutionAndViewport` **(I/O & Config Routines)** (Impact: 15.2)
  * `_computeFitAndFill` **(Many-Argument Workhorses)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 125`, `args: 77`, `func_start: 76`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 132`
* *Architecture:* `io: 2`, `api: 74`, `concurrency: 9`, `import: 10`
* *Defense:* `safety: 24`, `doc: 63`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.517
  * `Choke Point (Betweenness):` 0.015805 | `Ripple Effect (Closeness):` 0.126711
  * `Imports (Out-Degree: 11):` camera, index, event-emitter, excalibur-graphics-context, excalibur-graphics-context-2d-canvas, excalibur-graphics-context-webgl, vector, browser...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/engine/camera.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_12: 7.429, file_cluster_5: 7.803, file_cluster_0: 8.602
- **Magnitude:** 609.34 | **LOC:** 901 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **17**; blast radius 1.223; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 33.8028% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `action` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `move` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* /** * This moves the camera focal point to the specified position using specified easing function. C...
  * `zoomOverTime` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* /** * Zooms the camera in or out by the specified scale over the specified duration. * If no duratio...
  * `_initialize` **(I/O & Config Routines)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 70 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 123`, `args: 78`, `func_start: 71`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 100`
* *Architecture:* `api: 95`, `concurrency: 15`, `import: 20`
* *Defense:* `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.223
  * `Choke Point (Betweenness):` 0.005728 | `Ripple Effect (Closeness):` 0.106199
  * `Imports (Out-Degree: 19):` actor, bounding-box, engine, event-emitter, events, graphics, excalibur-graphics-context, lifecycle-events...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.787)
- **Top Global Matches:** file_cluster_4: 7.787, file_cluster_12: 8.435, file_cluster_5: 9.509
- **Magnitude:** 576.64 | **LOC:** 861 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **32**; blast radius 4.967; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.1%), Connectivity (formerly Api Exposure) (65.6%)
- **Documentation Coverage:** 86.4583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `flush` **(I/O & Config Routines)** (Impact: 30.7)
    * *Intent:* /** * Flushes all batched rendering to the screen */
  * `constructor` **(Defensive Guards)** (Impact: 27.0)
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `draw` **(Many-Argument Workhorses)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 122`, `args: 70`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 90`, `fragile_debt: 2`
* *Architecture:* `api: 57`, `import: 35`
* *Defense:* `safety: 21`, `doc: 13`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.967
  * `Choke Point (Betweenness):` 0.011345 | `Ripple Effect (Closeness):` 0.114911
  * `Imports (Out-Degree: 32):` color, flags, garbage-collector, affine-matrix, matrix, vector, screen, log...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/engine/resources/gif.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.75)
- **Top Global Matches:** file_cluster_12: 6.75, file_cluster_7: 7.834, file_cluster_5: 8.306
- **Magnitude:** 559.5 | **LOC:** 635 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.788; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (93.2%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `arrayToImage` **(Defensive Guards)** (Impact: 28.1)
  * `lzwDecode` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `toAnimation` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * Transform the GIF into an animation with duration per frame */
  * `parseBlocks` **(I/O & Config Routines)** (Impact: 10.4)
  * `parseHeader` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 98`, `args: 41`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 139`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 25`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 11`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.788
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.069054
  * `Imports (Out-Degree: 6):` animation, image-source, sprite, sprite-sheet, index, resource
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/spec/vitest/coroutine-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.129)
- **Top Global Matches:** file_cluster_10: 4.129, file_cluster_2: 6.283, file_cluster_13: 6.958
- **Magnitude:** 556.46 | **LOC:** 377 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.637; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.5%), Guard Balance (formerly Safety Score) (42.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 196
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 57`, `args: 32`, `func_start: 8`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `concurrency: 41`, `import: 2`
* *Defense:* `test: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/collision/detection/dynamic-tree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.196)
- **Top Global Matches:** file_cluster_4: 8.196, file_cluster_6: 9.602, file_cluster_9: 13.532
- **Magnitude:** 509.66 | **LOC:** 503 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.783; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.3%)
- **Documentation Coverage:** 30.303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_balance` **(Compute Cores)** (Impact: 32.5)
    * *Intent:* /** * Balances the tree about a node */
  * `_insert` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* /** * Inserts a node into the dynamic tree */
  * `updateCollider` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* /** * Updates the dynamic tree given the current bounds of each body being tracked */
  * `rayCastQuery` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /** * Queries the Dynamic Axis Aligned Tree for bodies that could be intersecting. By default the ra...
  * `query` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* /** * Queries the Dynamic Axis Aligned Tree for bodies that could be colliding with the provided bod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 54`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 106`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `safety: 2`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.783
  * `Choke Point (Betweenness):` 0.000431 | `Ripple Effect (Closeness):` 0.085449
  * `Imports (Out-Degree: 8):` .., entity, id, ray, log, body-component, bounding-box, physics-config
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/engine/collision/colliders/polygon-collider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.371)
- **Top Global Matches:** file_cluster_15: 6.371, file_cluster_11: 7.233, file_cluster_16: 7.351
- **Magnitude:** 503.08 | **LOC:** 739 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 1.376; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%), Connectivity (formerly Api Exposure) (52.6%)
- **Documentation Coverage:** 18.9189% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `triangulate` **(I/O & Config Routines)** (Impact: 27.9)
    * *Intent:* /** * Triangulate the polygon collider using the "Ear Clipping" algorithm. */
  * `isConvex` **(I/O & Config Routines)** (Impact: 13.9)
    * *Intent:* /** * Returns if the polygon collider is convex, Excalibur does not handle non-convex collision shap...
  * `rayCast` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* /** * Casts a ray into the polygon and returns a vector representing the point of contact (in world ...
  * `findEarTip` **(I/O & Config Routines)** (Impact: 13.1)
    * *Intent:* /** * Calculate the area of the triangle */ // function triangleArea(a: Vector, b: Vector, c: Vector...
  * `getClosestLineBetween` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 86`, `args: 46`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `state_mutation: 90`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 35`, `import: 18`
* *Defense:* `safety: 3`, `doc: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.376
  * `Choke Point (Betweenness):` 0.002157 | `Ripple Effect (Closeness):` 0.086447
  * `Imports (Out-Degree: 20):` .., color, line-segment, projection, ray, transform, vector, bounding-box...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/engine/actions/action-context.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.123)
- **Top Global Matches:** file_cluster_12: 6.123, file_cluster_15: 8.891, file_cluster_7: 9.056
- **Magnitude:** 489.76 | **LOC:** 575 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **26**; blast radius 1.735; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Connectivity (formerly Api Exposure) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 4.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `moveBy` **(Compute Cores)** (Impact: 23.1)
  * `moveTo` **(Compute Cores)** (Impact: 22.9)
  * `scaleTo` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `meet` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * This method will cause the entity to move towards another until they * collide "meet" at a spe...
  * `scaleBy` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 85`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 76`, `planned_debt: 1`
* *Architecture:* `api: 47`, `concurrency: 2`, `import: 36`
* *Defense:* `safety: 5`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.735
  * `Choke Point (Betweenness):` 0.001677 | `Ripple Effect (Closeness):` 0.072079
  * `Imports (Out-Degree: 26):` color, entity, math, easing-functions, action, action-queue, blink, call-method...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/engine/actor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.735)
- **Top Global Matches:** file_cluster_12: 7.735, file_cluster_15: 8.699, file_cluster_11: 8.989
- **Magnitude:** 445.46 | **LOC:** 1130 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **30**; blast radius 2.733; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Connectivity (formerly Api Exposure) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.3%)
- **Documentation Coverage:** 28.3133% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 51.3)
    * *Intent:* // #endregion /** * */
  * `draggable` **(Compute Cores)** (Impact: 10.7)
  * `contains` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* // #region Collision /** * Tests whether the x/y specified are contained in the actor */
  * `clone` **(I/O & Config Routines)** (Impact: 6.0)
  * `within` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* /** * Returns true if the two actor.collider's surfaces are less than or equal to the distance speci...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 134`, `args: 91`, `func_start: 86`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 46`
* *Architecture:* `api: 95`, `concurrency: 7`, `import: 33`
* *Defense:* `safety: 16`, `doc: 94`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.733
  * `Choke Point (Betweenness):` 0.009232 | `Ripple Effect (Closeness):` 0.107521
  * `Imports (Out-Degree: 31):` actions-component, body-component, collider-component, shape, collision-type, index, color, engine...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/spec/vitest/arcade-solver-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.826)
- **Top Global Matches:** file_cluster_10: 3.826, file_cluster_2: 4.163, file_cluster_17: 5.76
- **Magnitude:** 437.52 | **LOC:** 369 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.637; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (80.3%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (8.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `args: 12`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `concurrency: 4`, `import: 3`
* *Defense:* `safety: 2`, `test: 31`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` physics-config, test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/math/graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.964)
- **Top Global Matches:** file_cluster_5: 8.964, file_cluster_0: 10.151, file_cluster_4: 10.248
- **Magnitude:** 434.88 | **LOC:** 775 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.149; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (45.4%)
- **Documentation Coverage:** 36.1702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aStar` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* * * This method calculates the shortest path from the specified start node to the * specified end no...
  * `dijkstra` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* * Finds the shortest path between two nodes in the graph using Dijkstra's algorithm. * * This method...
  * `addEdge` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /** * Adds a new edge between two nodes in the graph. If the edge already exists, it does not add a ...
  * `constructor` **(Generic / Templated Code)** (Impact: 16.6)
  * `shortestPathDijkstra` **(Generic / Templated Code)** (Impact: 13.4)
    * *Intent:* /** * Finds the shortest path between two nodes in the graph using the Dijkstra method * * This meth...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 87`, `args: 55`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 79`, `planned_debt: 2`
* *Architecture:* `io: 13`, `api: 17`, `import: 2`
* *Defense:* `safety: 10`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.096572
  * `Imports (Out-Degree: 2):` random, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/entity-component-system/entity.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.522)
- **Top Global Matches:** file_cluster_5: 7.522, file_cluster_12: 7.854, file_cluster_0: 8.17
- **Magnitude:** 430.74 | **LOC:** 709 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **9**; blast radius 19.21; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (64.4%)
- **Documentation Coverage:** 30.8943% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 20.1)
  * `removeComponent` **(Generic / Templated Code)** (Impact: 15.6)
    * *Intent:* /** * Removes a component from the entity, by default removals are deferred to the end of entity upd...
  * `addComponent` **(Type Conversions)** (Impact: 15.4)
    * *Intent:* /** * Adds a component to the entity */
  * `hasChild` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** * Check if a child entity exists on the parent entity */
  * `_getClassHierarchyRoot` **(Stateful Encapsulated Methods)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 125`, `args: 63`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 41`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 79`, `concurrency: 14`, `import: 13`
* *Defense:* `safety: 5`, `doc: 49`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.21
  * `Choke Point (Betweenness):` 0.015974 | `Ripple Effect (Closeness):` 0.109105
  * `Imports (Out-Degree: 9):` engine, event-emitter, events, lifecycle-events, scene, observable, util, component...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/engine/director/director.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.006)
- **Top Global Matches:** file_cluster_12: 9.006, file_cluster_4: 9.092, file_cluster_5: 9.31
- **Magnitude:** 423.34 | **LOC:** 632 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.98; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 35.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goToScene` **(Defensive Guards)** (Impact: 38.2)
    * *Intent:* /** * Go to a specific scene, and optionally override loaders and transitions */
  * `configureStart` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* /** * Configures the start scene, and optionally the transition & loader for the director * * Typica...
  * `getSceneName` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Returns the name of the registered scene, null if none can be found */
  * `remove` **(Compute Cores)** (Impact: 18.9)
  * `playTransition` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /** * Plays a transition in the current scene and does book keeping for input. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 85`, `args: 25`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 42`
* *Architecture:* `api: 19`, `concurrency: 20`, `import: 10`
* *Defense:* `safety: 31`, `doc: 39`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.98
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.092051
  * `Imports (Out-Degree: 8):` engine, event-emitter, events, scene, log, default-loader, loader, transition
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/graphics-component.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.329)
- **Top Global Matches:** file_cluster_15: 7.329, file_cluster_11: 8.005, file_cluster_4: 8.148
- **Magnitude:** 410.04 | **LOC:** 581 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **14**; blast radius 2.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.4%), Guard Balance (formerly Safety Score) (67.4%)
- **Documentation Coverage:** 16.3934% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 26.4)
  * `add` **(Compute Cores)** (Impact: 23.2)
  * `deserialize` **(Defensive Guards)** (Impact: 21.3)
    * *Intent:* /** * Custom deserialization * NOTE - This only restores the component's settings, it does NOT resto...
  * `recalculateBounds` **(Defensive Guards)** (Impact: 12.4)
  * `serialize` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* /** * Custom serialization - stores graphic references instead of graphic data */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 73`, `args: 43`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 71`
* *Architecture:* `api: 45`, `import: 14`
* *Defense:* `safety: 25`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.186
  * `Choke Point (Betweenness):` 0.001661 | `Ripple Effect (Closeness):` 0.08974
  * `Imports (Out-Degree: 15):` index, color, entity-component-system, component, graphics-group, vector, watch-vector, log...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/shader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.43)
- **Top Global Matches:** file_cluster_12: 7.43, file_cluster_4: 7.483, file_cluster_15: 9.595
- **Magnitude:** 390.96 | **LOC:** 940 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **5**; blast radius 3.282; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%), Connectivity (formerly Api Exposure) (49.1%)
- **Documentation Coverage:** 23.8095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `glTypeToUniformTypeName` **(Compute Cores)** (Impact: 71.4)
    * *Intent:* /** * */
  * `_setUniforms` **(Stateful Encapsulated Methods)** (Impact: 22.8)
  * `setUniform` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* /** * Set any available uniform type in webgl * * For example setUniform('uniformMatrix2fv', 'u_my2x...
  * `trySetUniform` **(Many-Argument Workhorses)** (Impact: 11.3)
    * *Intent:* /** * Set any available uniform type in webgl. Will try to set the uniform, will return false if the...
  * `constructor` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /** * Create a shader program in excalibur */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 128`, `args: 51`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 37`
* *Architecture:* `io: 1`, `api: 30`, `import: 6`
* *Defense:* `safety: 9`, `doc: 44`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.282
  * `Choke Point (Betweenness):` 0.009553 | `Ripple Effect (Closeness):` 0.105335
  * `Imports (Out-Degree: 10):` .., matrix, watch, uniform-buffer, webgl-util
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/engine/resources/sound/sound.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.548)
- **Top Global Matches:** file_cluster_12: 7.548, file_cluster_5: 7.843, file_cluster_0: 9.748
- **Magnitude:** 385.26 | **LOC:** 555 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 1.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.7%)
- **Documentation Coverage:** 60.4396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `play` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /** * Play the sound, returns a promise that resolves when the sound is done playing * An optional v...
  * `constructor` **(Defensive Guards)** (Impact: 18.9)
  * `wireEngine` **(Callbacks & Closures)** (Impact: 9.9)
  * `load` **(Defensive Guards)** (Impact: 5.5)
  * `_resumePlayback` **(Stateful Encapsulated Methods)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 75
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 101`, `args: 59`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 42`
* *Architecture:* `io: 19`, `api: 51`, `concurrency: 30`, `import: 12`
* *Defense:* `safety: 23`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.308
  * `Choke Point (Betweenness):` 0.001974 | `Ripple Effect (Closeness):` 0.077582
  * `Imports (Out-Degree: 11):` engine, event-emitter, media-events, audio, audio-implementation, index, log, sound...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/engine/color.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.221)
- **Top Global Matches:** file_cluster_15: 5.221, file_cluster_11: 5.672, file_cluster_16: 6.994
- **Magnitude:** 373.08 | **LOC:** 677 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **1**; blast radius 18.327; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 13.5593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromRGBA` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `fromRGBString` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* /** * Creates a new instance of Color from a rgb string */
  * `hue2rgb` **(Compute Cores)** (Impact: 12.9)
  * `lerp` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* /** * Lerp between two colors different modes: * - hsl (default) - a compromise between speed and na...
  * `fromHex` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * Creates a new instance of Color from a hex string */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 76`, `args: 63`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `api: 68`, `import: 1`
* *Defense:* `safety: 4`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.327
  * `Choke Point (Betweenness):` 0.006424 | `Ripple Effect (Closeness):` 0.16584
  * `Imports (Out-Degree: 2):` math
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `src/engine/input/pointer-event-receiver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.62)
- **Top Global Matches:** file_cluster_4: 7.62, file_cluster_12: 10.803, file_cluster_5: 11.749
- **Magnitude:** 369.24 | **LOC:** 583 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **14**; blast radius 1.887; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.4%), Guard Balance (formerly Safety Score) (61.1%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* /** * Initializes the pointer event receiver so that it can start listening to native * browser even...
  * `_handle` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* /** * Responsible for handling and parsing pointer events */
  * `_handleWheel` **(Stateful Encapsulated Methods)** (Impact: 24.6)
  * `update` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* /** * Called internally by excalibur * * Updates the current frame pointer info and emits raw pointe...
  * `_nativeButtonToPointerButton` **(Stateful Encapsulated Methods)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 101`, `args: 38`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 39`, `fragile_debt: 1`
* *Architecture:* `api: 49`, `concurrency: 7`, `import: 17`
* *Defense:* `safety: 6`, `doc: 18`, `immutability_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.887
  * `Choke Point (Betweenness):` 0.001689 | `Ripple Effect (Closeness):` 0.09705
  * `Imports (Out-Degree: 14):` engine, event-emitter, global-coordinates, vector, iframe, util, native-pointer-button, pointer-abstraction...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-2d-canvas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_12: 6.438, file_cluster_15: 7.124, file_cluster_11: 7.912
- **Magnitude:** 368.26 | **LOC:** 409 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 1.17; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.0%), Guard Balance (formerly Safety Score) (61.9%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 55.1)
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* /** * * Draw an image to the Excalibur Graphics context specifying the source image coordinates (sx,...
  * `drawCircle` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `drawCircle` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `drawLine` **(Defensive Guards)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 54`, `args: 45`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 37`
* *Architecture:* `api: 40`, `import: 10`
* *Defense:* `safety: 7`, `doc: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.17
  * `Choke Point (Betweenness):` 0.000488 | `Ripple Effect (Closeness):` 0.109335
  * `Imports (Out-Degree: 10):` color, affine-matrix, vector, screen, graphics-diagnostics, post-processor, debug-text, excalibur-graphics-context...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/engine/collision/detection/quad-tree.ts` (TYPESCRIPT) | Magnitude: 144.54 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 183, branch: 35, state_mutation: 27, structural_boundaries: 24
- `src/engine/tile-map/isometric-entity-system.ts` (TYPESCRIPT) | Magnitude: 24.24 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, core_var_decl: 9, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `sandbox/tests/parallax/index.ts` (TYPESCRIPT) | Magnitude: 25.8 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 5, state_mutation: 4, core_var_decl: 3
- `src/engine/math/vector-view.ts` (TYPESCRIPT) | Magnitude: 20.88 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 20, args: 13, api: 7
- `sandbox/tests/collisionvelocity/vel.ts` (TYPESCRIPT) | Magnitude: 36.4 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 11, structural_boundaries: 5, branch: 3
- `src/engine/timer.ts` (TYPESCRIPT) | Magnitude: 196.16 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 51, state_mutation: 37, branch: 36
- `sandbox/tests/gotoscene/index.ts` (TYPESCRIPT) | Magnitude: 34.58 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 11, concurrency: 11, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/engine/graphics/context/material.ts` (TYPESCRIPT) | Magnitude: 98.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 139, branch: 28, structural_boundaries: 28, safety: 16
- `src/engine/graphics/graphic.ts` (TYPESCRIPT) | Magnitude: 161.04 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 162, branch: 34, state_mutation: 29, structural_boundaries: 28
- `src/engine/graphics/post-processor/color-blindness-post-processor.ts` (TYPESCRIPT) | Magnitude: 38.02 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 19, args: 8, func_start: 8
- `src/engine/graphics/polygon.ts` (TYPESCRIPT) | Magnitude: 35.46 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 22, args: 12, api: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/spec/vitest/graphics-group-spec.ts` (TYPESCRIPT) | Magnitude: 104.65 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 96, test: 22, core_var_decl: 17, structural_boundaries: 15
- `src/engine/graphics/context/shader.ts` (TYPESCRIPT) | Magnitude: 390.96 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 611, structural_boundaries: 128, branch: 116, core_var_decl: 71
- `src/engine/graphics/sprite-font.ts` (TYPESCRIPT) | Magnitude: 150.5 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 127, branch: 36, core_var_decl: 32, structural_boundaries: 29
- `src/engine/director/director.ts` (TYPESCRIPT) | Magnitude: 423.34 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 371, branch: 129, structural_boundaries: 85, core_var_decl: 57
- `src/spec/vitest/quad-index-buffer-spec.ts` (TYPESCRIPT) | Magnitude: 16.84 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 39, test: 17, structural_boundaries: 10, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/engine/interfaces/lifecycle-events.ts` (TYPESCRIPT) | Magnitude: 181.94 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 214, indent_spaces: 77, args: 72, func_start: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/engine/math/line-segment.ts` (TYPESCRIPT) | Magnitude: 150.1 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 146, core_var_decl: 40, design_snake_case: 36, branch: 35
- `src/engine/graphics/transform-interpolation.ts` (TYPESCRIPT) | Magnitude: 39.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, core_var_decl: 23, design_camel_case: 17, state_mutation: 15
- `sandbox/tests/input/gamepad.ts` (TYPESCRIPT) | Magnitude: 74.22 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 25, state_mutation: 25, core_var_decl: 18
- `sandbox/vite.config.ts` (TYPESCRIPT) | Magnitude: 10.32 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 6, io: 5, import: 4
- `src/engine/collision/integrator.ts` (TYPESCRIPT) | Magnitude: 8.7 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 9, core_var_decl: 9, encapsulation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `sandbox/tests/graphics/index.ts` (TYPESCRIPT) | Magnitude: 36.22 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 7, state_mutation: 5, core_var_decl: 5
- `src/engine/graphics/nine-slice.ts` (TYPESCRIPT) | Magnitude: 209.48 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 407, state_mutation: 47, branch: 37, structural_boundaries: 30
- `src/engine/graphics/context/render-source.ts` (TYPESCRIPT) | Magnitude: 8.6 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, api: 4, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/engine/collision/solver/contact-bias.ts` (TYPESCRIPT) | Magnitude: 21.42 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, core_var_decl: 6, design_pascal_case: 6
- `src/engine/director/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `src/engine/graphics/index.ts` (TYPESCRIPT) | Magnitude: 61.94 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 49, api: 46, import: 46, planned_debt: 1
- `src/engine/collision/index.ts` (TYPESCRIPT) | Magnitude: 53.76 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 43, api: 38, import: 38
- `src/engine/interfaces/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 7, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `sandbox/tests/memory-leaker/index.ts` (TYPESCRIPT) | Magnitude: 9.62 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 5, dead_code: 4, core_var_decl: 4
- `sandbox/tests/sound-manager/main.ts` (TYPESCRIPT) | Magnitude: 19.32 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 11, core_var_decl: 8, branch: 7
- `src/engine/util/index.ts` (TYPESCRIPT) | Magnitude: 19.64 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, api: 6, import: 6, explicit_casts: 1
- `vitest.config.ts` (TYPESCRIPT) | Magnitude: 17.68 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 13, io: 6, import: 6
- `src/engine/director/Loader.css` (CSS) | Magnitude: 0.25 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 88, class_start: 7, ui_framework: 7, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `sandbox/tests/loader-scene/index.ts` (TYPESCRIPT) | Magnitude: 4.06 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 5, core_var_decl: 4, design_snake_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sandbox/tests/drawcalls/index.ts` (TYPESCRIPT) | Magnitude: 43.98 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 13, core_var_decl: 12, design_snake_case: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/spec/vitest/sound-spec.ts` -> **Girts Silis** (100.0% isolated ownership) | Magnitude: 777.57
- `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` -> **keasy9** (100.0% isolated ownership) | Magnitude: 576.64
- `src/engine/actor.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 445.46
- `src/engine/math/graph.ts` -> **THEVENOUX Jean-Philippe** (100.0% isolated ownership) | Magnitude: 434.88
- `src/engine/graphics/graphics-component.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 410.04

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/engine/engine.ts` -> **Severity: 3.716** (Bridge: 0.0372 * Flux: 99.9882%)
- `src/engine/graphics/debug.ts` -> **Severity: 2.207** (Bridge: 0.0226 * Flux: 97.8741%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 1.597** (Bridge: 0.016 * Flux: 99.9826%)
- `src/engine/screen.ts` -> **Severity: 1.58** (Bridge: 0.0158 * Flux: 99.9998%)
- `src/engine/util/log.ts` -> **Severity: 1.284** (Bridge: 0.0128 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/engine/math/vector.ts` -> **Severity: 12.104** (Embedded: 0.2046 * Error Risk: 59.1653%)
- `src/engine/util/log.ts` -> **Severity: 11.027** (Embedded: 0.1378 * Error Risk: 80.0%)
- `src/engine/color.ts` -> **Severity: 10.009** (Embedded: 0.1658 * Error Risk: 60.3556%)
- `src/engine/event-emitter.ts` -> **Severity: 9.785** (Embedded: 0.1306 * Error Risk: 74.9209%)
- `src/engine/math/random.ts` -> **Severity: 9.699** (Embedded: 0.136 * Error Risk: 71.3173%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/engine/graphics/debug.ts` -> **Severity: 1405.0** (Blast Radius: 14.05 * Doc Risk: 100.0%)
- `src/engine/interfaces/clonable.ts` -> **Severity: 1269.6** (Blast Radius: 12.696 * Doc Risk: 100.0%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 593.48** (Blast Radius: 19.21 * Doc Risk: 30.8943%)
- `src/engine/event-emitter.ts` -> **Severity: 444.563** (Blast Radius: 7.502 * Doc Risk: 59.2593%)
- `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` -> **Severity: 429.438** (Blast Radius: 4.967 * Doc Risk: 86.4583%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 173 literal sites + 1 sites through wrappers = 174

- `fail` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/engine/util/util.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7881 call pairs -- scoped 45.0%, unique 0.0%, ambiguous 24.1%, external 30.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 6194 | 44.1% | 0.0% | 24.0% | 31.9% |
| javascript | 1675 | 48.8% | 0.0% | 24.7% | 26.5% |
| python | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
