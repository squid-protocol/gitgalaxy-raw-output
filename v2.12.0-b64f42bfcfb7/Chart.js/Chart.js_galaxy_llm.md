# ARCHITECTURAL_BRIEF: Chart.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/chartjs/Chart.js.git` |
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
- **Scope:** 905 analyzed artifact(s), 68775 LOC.
- **Load-bearing artifact:** `src/types.ts` -- 45 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/index.umd.ts` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/core/core.scale.js` at magnitude 1416.52 (structural weight, not risk).
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
| Total Artifacts | 1750 |
| Analyzed Artifacts (Scanned) | 905 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 845 |
| Total LOC | 68775 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 51.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4366 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3984 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2381 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 646 | 55596 | 71.4% |
| JSON | 146 | 6970 | 16.1% |
| TYPESCRIPT | 84 | 5716 | 9.3% |
| YAML | 10 | 372 | 1.1% |
| PLAINTEXT | 8 | 0 | 0.9% |
| MARKDOWN | 5 | 0 | 0.6% |
| SHELL | 4 | 80 | 0.4% |
| HTML | 2 | 41 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 905 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 50%, Data / Markup / Trivial 21%, Callbacks & Closures Files 9%, Large Core Modules (2) 6%, Large Core Modules (3) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 892 | 98.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 845*

**Composition by Extension & Reason:**
- `.png`: 679x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 138x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 45 exceeds 500 chars), 1x Excluded (Saturation: Line 31 exceeds 500 chars)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.styl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.drawio`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 17244 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 75.7 | 4.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.4 | 38.3 | 50.7 | 50.7 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 89.8 | 6.3 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 33.5 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 43 | 16 | 0 | `src/helpers/helpers.dom.ts` |
| cleanup | 43 | 15 | 0 | `test/specs/core.controller.tests.js` |
| guards | 890 | 130 | 2 | `src/core/core.scale.js` |
| danger | 171 | 57 | 0 | `scripts/deploy-docs.sh` |
| concurrency | 254 | 40 | 0 | `test/specs/plugin.tooltip.tests.js` |
| connectivity | 1417 | 629 | 1 | `src/types/index.d.ts` |
| io | 13 | 4 | 0 | `test/types/autogen.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 2 | 0 | `test/BasicChartWebWorker.js` |
| time | 32 | 14 | 0 | `test/specs/core.animations.tests.js` |
| serialization | 9 | 6 | 0 | `src/helpers/helpers.segment.js` |
| regex | 19 | 14 | 0 | `karma.conf.cjs` |
| events | 103 | 30 | 0 | `test/specs/plugin.tooltip.tests.js` |
| tests | 4075 | 58 | 0 | `test/specs/core.controller.tests.js` |
| docs | 1101 | 78 | 0 | `src/types/index.d.ts` |
| debt | 151 | 49 | 0 | `src/types/index.d.ts` |
| mutation | 9325 | 714 | 16 | `src/core/core.scale.js` |
| dead_code | 333 | 122 | 1 | `src/types/index.d.ts` |
| credential | 2 | 2 | 0 | `test/specs/helpers.color.tests.js` |
| threat | 1 | 1 | 0 | `test/fixtures/core.scale/label-offset-vertical-axes.json` |
| ml_ai | 124 | 10 | 0 | `src/helpers/helpers.canvas.ts` |
| ui | 22 | 9 | 0 | `test/specs/platform.dom.tests.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/types/autogen.js` (Hits: 8)
- `scripts/sample-redirect-template.html` (Hits: 3)
- `rollup.config.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.ts** (`src/types.ts`) — 45 inbound connections
2. **helpers.core.ts** (`src/helpers/helpers.core.ts`) — 41 inbound connections
3. **helpers.math.ts** (`src/helpers/helpers.math.ts`) — 29 inbound connections
4. **index.ts** (`src/helpers/index.ts`) — 26 inbound connections
5. **helpers.options.ts** (`src/helpers/helpers.options.ts`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.umd.ts** (`src/index.umd.ts`) — 18 outbound dependencies
2. **index.ts** (`src/helpers/index.ts`) — 16 outbound dependencies
3. **index.ts** (`src/core/index.ts`) — 14 outbound dependencies
4. **core.controller.js** (`src/core/core.controller.js`) — 12 outbound dependencies
5. **index.d.ts** (`src/types/index.d.ts`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `drawPointLegend` **(Many-Argument Workhorses)** (@ `src/helpers/helpers.canvas.ts`) -> Impact: **100.2** | LOC: 142
  * *Intent:* // eslint-disable-next-line complexity
- `_computeLabelItems` **(Defensive Guards)** (@ `src/core/core.scale.js`) -> Impact: **96.8** | LOC: 183
  * *Intent:* /** */
- `generateTicks` **(Many-Argument Workhorses)** (@ `src/scales/scale.linearbase.js`) -> Impact: **75.3** | LOC: 121
  * *Intent:* * * 2. If generationOptions.min, generationOptions.max, and generationOptions.count is defined * spacing = (max - min) / count * Ticks are generated a...
- `_longestText` **(Many-Argument Workhorses)** (@ `src/helpers/helpers.canvas.ts`) -> Impact: **49.6** | LOC: 52
  * *Intent:* /** */ // eslint-disable-next-line complexity
- `updateElements` **(Many-Argument Workhorses)** (@ `src/controllers/controller.line.js`) -> Impact: **47.0** | LOC: 45
- `drawBorder` **(Many-Argument Workhorses)** (@ `src/elements/element.arc.ts`) -> Impact: **44.1** | LOC: 50
- `_computeGridLineItems` **(Defensive Guards)** (@ `src/core/core.scale.js`) -> Impact: **43.3** | LOC: 130
  * *Intent:* /** */
- `updateElements` **(Many-Argument Workhorses)** (@ `src/controllers/controller.scatter.js`) -> Impact: **42.3** | LOC: 41
- `_getYAxisLabelAlignment` **(Defensive Guards)** (@ `src/core/core.scale.js`) -> Impact: **38.7** | LOC: 67
- `_calculatePadding` **(Many-Argument Workhorses)** (@ `src/core/core.scale.js`) -> Impact: **38.2** | LOC: 49

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/core` | 21 | 4881.5 | 30.49% | 1.02% |
| `src/helpers` | 18 | 2841.15 | 29.33% | 1.59% |
| `test/specs` | 54 | 2397.98 | 2.1% | 0.0% |
| `src/plugins` | 7 | 1869.56 | 39.49% | 3.7% |
| `src/scales` | 8 | 1547.72 | 37.05% | 0.0% |
| `src/controllers` | 9 | 1365.68 | 29.52% | 0.0% |
| `src/elements` | 5 | 800.66 | 31.82% | 0.0% |
| `src/plugins/plugin.filler` | 8 | 621.94 | 40.24% | 2.28% |
| `src/platform` | 4 | 261.46 | 10.77% | 0.0% |
| `test/types` | 16 | 247.56 | 2.56% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/types/animation.d.ts` -> **100.0%** Exposure
- `src/types/index.d.ts` -> **99.9968%** Exposure
- `src/types/layout.d.ts` -> **99.9447%** Exposure
- `.github/release-drafter.yml` -> **97.0688%** Exposure
- `rollup.config.js` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/controllers/controller.bar.js` -> **100.0%** Exposure
- `src/controllers/controller.line.js` -> **100.0%** Exposure
- `src/core/core.animation.js` -> **100.0%** Exposure
- `src/core/core.animator.js` -> **100.0%** Exposure
- `src/core/core.layouts.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/types/index.d.ts` -> **157** Orphaned Functions | **22** Duplicates
- `src/types/animation.d.ts` -> **11** Orphaned Functions | **0** Duplicates
- `test/specs/plugin.tooltip.tests.js` -> **3** Orphaned Functions | **6** Duplicates
- `test/specs/scale.radialLinear.tests.js` -> **0** Orphaned Functions | **8** Duplicates
- `test/specs/core.plugin.tests.js` -> **3** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `58` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/core/core.scale.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.263)
- **Top Global Matches:** file_cluster_4: 7.263, file_cluster_15: 8.338, file_cluster_11: 9.94
- **Magnitude:** 1416.52 | **LOC:** 1713 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 3.345; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.5%), Connectivity (formerly Api Exposure) (57.0%)
- **Documentation Coverage:** 40.1869% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_computeLabelItems` **(Defensive Guards)** (Impact: 96.8)
    * *Intent:* /** */
  * `_computeGridLineItems` **(Defensive Guards)** (Impact: 43.3)
    * *Intent:* /** */
  * `_getYAxisLabelAlignment` **(Defensive Guards)** (Impact: 38.7)
  * `_calculatePadding` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `titleArgs` **(Many-Argument Workhorses)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 131`, `args: 89`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `state_mutation: 308`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 80`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.345
  * `Choke Point (Betweenness):` 0.000215 | `Ripple Effect (Closeness):` 0.026141
  * `Imports (Out-Degree: 7):` helpers.canvas.js, helpers.core.js, helpers.extras.js, helpers.math.js, helpers.options.js, core.element.js, core.scale.autoskip.js
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/plugins/plugin.tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.74)
- **Top Global Matches:** file_cluster_15: 5.74, file_cluster_11: 7.855, file_cluster_16: 8.062
- **Magnitude:** 924.38 | **LOC:** 1351 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.378; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%), Complexity Load (formerly Cognitive Load) (55.6%)
- **Documentation Coverage:** 58.9744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_drawColorBox` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* /** */
  * `getCaretPosition` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `getBackgroundPoint` **(Defensive Guards)** (Impact: 21.4)
    * *Intent:* /** * Helper to get the location a tooltip needs to be placed at given the initial position (via the...
  * `drawBackground` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `handleEvent` **(Many-Argument Workhorses)** (Impact: 19.7)
    * *Intent:* /** * Handle an event */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 113`, `args: 69`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 193`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 50`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.378
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.019935
  * `Imports (Out-Degree: 8):` core.animations.js, core.element.js, helpers.canvas.js, helpers.core.js, helpers.math.js, helpers.options.js, helpers.rtl.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/core.datasetController.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.781)
- **Top Global Matches:** file_cluster_15: 5.781, file_cluster_11: 7.804, file_cluster_16: 8.119
- **Magnitude:** 797.26 | **LOC:** 1078 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **5**; blast radius 4.049; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.5%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 51.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Defensive Guards)** (Impact: 29.7)
    * *Intent:* /** */
  * `applyStack` **(Defensive Guards)** (Impact: 26.1)
  * `getMinMax` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* /** */
  * `clearStacks` **(Defensive Guards)** (Impact: 18.3)
  * `getLastIndexInStack` **(Compute Cores)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 93`, `args: 80`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 38`, `doc: 42`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.049
  * `Choke Point (Betweenness):` 0.000485 | `Ripple Effect (Closeness):` 0.025449
  * `Imports (Out-Degree: 6):` helpers.collection.js, helpers.core.js, index.js, core.animations.js, core.defaults.js
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/core/core.controller.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.504)
- **Top Global Matches:** file_cluster_15: 6.504, file_cluster_10: 7.32, file_cluster_11: 7.556
- **Magnitude:** 704.0 | **LOC:** 1270 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Connectivity (formerly Api Exposure) (45.8%)
- **Documentation Coverage:** 55.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* // eslint-disable-next-line max-statements
  * `update` **(Compute Cores)** (Impact: 15.9)
  * `buildOrUpdateScales` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* /** * Builds a map of scale ID to scale object for future lookup. */
  * `_resize` **(Compute Cores)** (Impact: 13.4)
  * `updateHoverStyle` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 136`, `args: 114`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 114`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 43`, `doc: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.00102 | `Ripple Effect (Closeness):` 0.028003
  * `Imports (Out-Degree: 17):` package.json, helpers.core.js, helpers.extras.js, index.js, index.js, core.animator.js, core.config.js, core.defaults.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/controllers/controller.bar.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.067)
- **Top Global Matches:** file_cluster_4: 6.067, file_cluster_15: 7.829, file_cluster_11: 9.311
- **Magnitude:** 571.26 | **LOC:** 683 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.306; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 51.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateElements` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `_getStacks` **(Defensive Guards)** (Impact: 26.5)
    * *Intent:* /** * Returns the stacks based on groups and bar visibility. */
  * `setBorderSkipped` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `_calculateBarValuePixels` **(Defensive Guards)** (Impact: 26.1)
    * *Intent:* /** * Note: pixel values are not clamped to the scale area. */
  * `computeFlexCategoryTraits` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* /** * Computes an "optimal" category that globally arranges bars side by side (no gap when * percent...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 68`, `args: 40`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 44`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.306
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.020079
  * `Imports (Out-Degree: 4):` core.datasetController.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.canvas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.37)
- **Top Global Matches:** file_cluster_4: 7.37, file_cluster_6: 8.094, file_cluster_9: 13.674
- **Magnitude:** 507.74 | **LOC:** 528 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **4**; blast radius 6.732; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%), Connectivity (formerly Api Exposure) (56.5%)
- **Documentation Coverage:** 29.0323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawPointLegend` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* // eslint-disable-next-line complexity
  * `_longestText` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* /** */ // eslint-disable-next-line complexity
  * `renderText` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /** * Render text onto the canvas */
  * `_steppedLineTo` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** */
  * `_isPointInArea` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * Returns true if the point is inside the rectangle */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 49`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.732
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.035088
  * `Imports (Out-Degree: 2):` geometric.js, index.js, helpers.core.js, helpers.math.js
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/plugins/plugin.legend.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.679)
- **Top Global Matches:** file_cluster_15: 6.679, file_cluster_4: 7.881, file_cluster_16: 8.708
- **Magnitude:** 501.9 | **LOC:** 721 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.378; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (54.4%)
- **Documentation Coverage:** 74.4186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_draw` **(I/O & Config Routines)** (Impact: 32.8)
    * *Intent:* /** */
  * `drawLegendBox` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* // current position
  * `handleEvent` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* /** * Handle an event */
  * `isListened` **(Defensive Guards)** (Impact: 14.3)
  * `_getLegendItemAt` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 73`, `args: 44`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 23`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.378
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.019935
  * `Imports (Out-Degree: 10):` core.defaults.js, core.element.js, core.layouts.js, helpers.canvas.js, helpers.extras.js, helpers.options.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/scales/scale.radialLinear.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.129)
- **Top Global Matches:** file_cluster_15: 5.129, file_cluster_11: 7.656, file_cluster_16: 7.803
- **Magnitude:** 401.8 | **LOC:** 685 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.473; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.1%), Connectivity (formerly Api Exposure) (48.3%)
- **Documentation Coverage:** 62.963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawRadiusLine` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `updateLimits` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `determineLimits` **(Defensive Guards)** (Impact: 15.6)
  * `drawGrid` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* /** */
  * `yForAngle` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 61`, `args: 42`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `safety: 14`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.473
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.020251
  * `Imports (Out-Degree: 8):` core.defaults.js, core.ticks.js, helpers.canvas.js, helpers.core.js, helpers.math.js, helpers.options.js, scale.linearbase.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/scales/scale.time.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.615)
- **Top Global Matches:** file_cluster_15: 5.615, file_cluster_11: 7.65, file_cluster_12: 7.774
- **Magnitude:** 400.12 | **LOC:** 676 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.89; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.5%), Connectivity (formerly Api Exposure) (46.5%)
- **Documentation Coverage:** 19.5122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_tickFormatFunction` **(Compute Cores)** (Impact: 21.0)
    * *Intent:* /** * Function to format an individual tick mark */
  * `parse` **(Defensive Guards)** (Impact: 18.9)
    * *Intent:* /** */
  * `determineDataLimits` **(I/O & Config Routines)** (Impact: 15.9)
  * `_generate` **(Defensive Guards)** (Impact: 14.0)
    * *Intent:* /** * Generates a maximum of `capacity` timestamps between min and max, rounded to the * `minor` uni...
  * `determineUnitForFormatting` **(Many-Argument Workhorses)** (Impact: 12.7)
    * *Intent:* /** * Figures out what unit to format a set of ticks with */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 63`, `args: 33`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 23`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.89
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.020665
  * `Imports (Out-Degree: 5):` core.adapters.js, core.scale.js, helpers.collection.js, helpers.core.js, helpers.math.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_5: 7.431, file_cluster_12: 8.134, file_cluster_0: 8.393
- **Magnitude:** 340.38 | **LOC:** 417 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **41** in-repo importer(s); it depends on **2**; blast radius 38.758; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (89.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.9%)
- **Documentation Coverage:** 37.234% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `each` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `merge` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `_elementsEqual` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* /** * Returns true if the `a0` and `a1` arrays have the same content, else returns false. */
  * `_mergerIf` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* /** * Merges source[key] in target[key] only if target[key] is undefined. */
  * `_merger` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* /** * The default merger when Chart.helpers.merge is called without merger option. * Note(SB): also ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 123`, `args: 51`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`
* *Architecture:* `api: 45`, `import: 2`
* *Defense:* `safety: 5`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.758
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.046371
  * `Imports (Out-Degree: 1):` basic.js, index.js
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.segment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.376)
- **Top Global Matches:** file_cluster_15: 6.376, file_cluster_10: 7.956, file_cluster_16: 8.2
- **Magnitude:** 337.12 | **LOC:** 365 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 1.923; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (51.7%)
- **Documentation Coverage:** 52.1739% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_boundSegment` **(Defensive Guards)** (Impact: 32.6)
    * *Intent:* /** * Returns the sub-segment(s) of a line segment that fall in the given bounds **/
  * `doSplitByStyles` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /** */
  * `findStartAndEnd` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /** * Find start and end index of a line. */
  * `solidSegments` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /** * Compute solid segments from Points, when spanGaps === false */
  * `addStyle` **(Defensive Guards)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 53`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 46`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 16`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.923
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.026687
  * `Imports (Out-Degree: 3):` helpers.color.js, helpers.math.js, helpers.options.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/core/core.layouts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.047)
- **Top Global Matches:** file_cluster_15: 6.047, file_cluster_10: 8.041, file_cluster_16: 8.18
- **Magnitude:** 327.36 | **LOC:** 456 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 2.189; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 58.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `placeBoxes` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `fitBoxes` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `update` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* /** * Fits boxes of the given chart into the given size by having each box measure itself * then run...
  * `updateDims` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `setLayoutDims` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * store dimensions used instead of available chartArea in fitBoxes **/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 32`, `args: 31`, `func_start: 22`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.189
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.025959
  * `Imports (Out-Degree: 2):` helpers.core.js, helpers.options.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.39)
- **Top Global Matches:** file_cluster_15: 6.39, file_cluster_0: 7.661, file_cluster_10: 8.011
- **Magnitude:** 320.48 | **LOC:** 457 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.52; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (36.2%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addScopes` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `_createResolver` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* /** * Creates a Proxy for resolving raw values for options. */
  * `_resolveArray` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `_attachContext` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* /** * Returns an Proxy for resolving option values with context. */
  * `_resolveWithContext` **(Many-Argument Workhorses)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 85`, `args: 44`, `func_start: 37`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.52
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.026878
  * `Imports (Out-Degree: 3):` basic.js, index.js, helpers.config.types.js, helpers.core.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/elements/element.line.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.884)
- **Top Global Matches:** file_cluster_15: 5.884, file_cluster_11: 7.461, file_cluster_16: 8.015
- **Magnitude:** 312.32 | **LOC:** 446 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 2.595; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%), Connectivity (formerly Api Exposure) (41.6%)
- **Documentation Coverage:** 53.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fastPathSegment` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* * Create path from points, grouping by truncated x-coordinate * Points need to be in order by x-coor...
  * `pathSegment` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* * Create path from points, grouping by truncated x-coordinate * Points need to be in order by x-coor...
  * `draw` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* /** * Draw */
  * `pathVars` **(Compute Cores)** (Impact: 12.8)
  * `_getSegmentMethod` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 43`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 12`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.595
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.021359
  * `Imports (Out-Degree: 7):` core.element.js, helpers.canvas.js, helpers.curve.js, helpers.interpolation.js, helpers.segment.js, index.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/core/core.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.345)
- **Top Global Matches:** file_cluster_15: 6.345, file_cluster_10: 7.536, file_cluster_11: 7.717
- **Magnitude:** 306.4 | **LOC:** 419 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.926; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Connectivity (formerly Api Exposure) (49.7%)
- **Documentation Coverage:** 67.3469% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mergeScaleConfig` **(Compute Cores)** (Impact: 22.9)
  * `needContext` **(Compute Cores)** (Impact: 16.3)
  * `getOptionScopes` **(Many-Argument Workhorses)** (Impact: 13.5)
    * *Intent:* /** * Resolves the objects from options and defaults for option value resolution. */
  * `determineAxis` **(Compute Cores)** (Impact: 12.8)
  * `getIndexAxis` **(Compute Cores)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 67`, `args: 54`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 16`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.022135
  * `Imports (Out-Degree: 3):` helpers.config.js, helpers.core.js, core.defaults.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/scales/scale.linearbase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.623)
- **Top Global Matches:** file_cluster_4: 5.623, file_cluster_15: 10.356, file_cluster_6: 10.645
- **Magnitude:** 291.48 | **LOC:** 314 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 1.379; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (63.4%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateTicks` **(Many-Argument Workhorses)** (Impact: 75.3)
    * *Intent:* * * 2. If generationOptions.min, generationOptions.max, and generationOptions.count is defined * spa...
  * `handleTickRangeOptions` **(Defensive Guards)** (Impact: 13.6)
  * `parse` **(Defensive Guards)** (Impact: 9.2)
  * `buildTicks` **(I/O & Config Routines)** (Impact: 8.2)
  * `getTickLimit` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 32`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `dead_code: 2`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `safety: 11`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.379
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.017673
  * `Imports (Out-Degree: 4):` core.scale.js, helpers.core.js, helpers.intl.js, helpers.math.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/core/core.interaction.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.61)
- **Top Global Matches:** file_cluster_15: 6.61, file_cluster_9: 7.215, file_cluster_16: 8.445
- **Magnitude:** 260.92 | **LOC:** 388 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 1.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Complexity Load (formerly Cognitive Load) (24.1%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `binarySearch` **(Many-Argument Workhorses)** (Impact: 35.7)
    * *Intent:* */ /** * Helper function to do binary search when possible */
  * `getNearestCartesianItems` **(Many-Argument Workhorses)** (Impact: 25.3)
    * *Intent:* /** * Helper function to get the items nearest to the event position for a cartesian chart */
  * `evaluationFunc` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `getAxisItems` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* /** * Helper function to get the items matching along the given X or Y axis */
  * `index` **(Many-Argument Workhorses)** (Impact: 17.0)
    * *Intent:* /** * Returns items at the same index. If the options.intersect parameter is true, we only return it...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 40`, `args: 22`, `func_start: 17`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 9`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.248
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.024772
  * `Imports (Out-Degree: 6):` helpers.collection.js, helpers.dom.js, helpers.math.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.dom.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.368)
- **Top Global Matches:** file_cluster_15: 6.368, file_cluster_11: 8.012, file_cluster_16: 8.336
- **Magnitude:** 249.6 | **LOC:** 287 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 3.065; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMaximumSize` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* // eslint-disable-next-line complexity
  * `retinaScale` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /** */
  * `getContainerSize` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `getPositionedStyle` **(Type Conversions)** (Impact: 10.6)
  * `getRelativePosition` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Gets an event's x, y coordinates, relative to the chart area */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 34`, `args: 15`, `func_start: 14`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.065
  * `Choke Point (Betweenness):` 0.002587 | `Ripple Effect (Closeness):` 0.031359
  * `Imports (Out-Degree: 3):` core.controller.js, types.js, index.js, helpers.math.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/helpers/helpers.curve.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_15: 6.526, file_cluster_9: 6.531, file_cluster_16: 8.068
- **Magnitude:** 242.18 | **LOC:** 224 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.5%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_updateBezierControlPoints` **(Many-Argument Workhorses)** (Impact: 21.5)
    * *Intent:* /** */
  * `splineCurveMonotone` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /** * This function calculates Bézier control points in a similar way than |splineCurve|, * but pres...
  * `monotoneAdjust` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* /** * Adjust tangents to ensure monotonic properties */
  * `splineCurve` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `monotoneCompute` **(Many-Argument Workhorses)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 21`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026604
  * `Imports (Out-Degree: 2):` geometric.js, index.js, helpers.canvas.js, helpers.math.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/controllers/controller.doughnut.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.827)
- **Top Global Matches:** file_cluster_15: 4.827, file_cluster_11: 6.716, file_cluster_16: 7.646
- **Magnitude:** 242.12 | **LOC:** 400 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 2.416; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.3%), Connectivity (formerly Api Exposure) (46.9%)
- **Documentation Coverage:** 67.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateElements` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `getMaxBorderWidth` **(Compute Cores)** (Impact: 14.2)
  * `_circumference` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** */
  * `parse` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* /** * Override data parsing, since we are not using scales */
  * `getRatioAndOffset` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 54`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.416
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.020471
  * `Imports (Out-Degree: 4):` core.datasetController.js, helpers.core.js, helpers.intl.js, helpers.math.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/elements/element.arc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.144)
- **Top Global Matches:** file_cluster_4: 6.144, file_cluster_15: 8.959, file_cluster_16: 10.41
- **Magnitude:** 236.06 | **LOC:** 422 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.992; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%), Connectivity (formerly Api Exposure) (39.2%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawBorder` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `pathArc` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* /** * Path the arc, respecting border radius by separating into left and right halves. * * Start End...
  * `draw` **(Compute Cores)** (Impact: 14.1)
  * `clipSelf` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `drawArc` **(Many-Argument Workhorses)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 24`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.992
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.02109
  * `Imports (Out-Degree: 5):` core.element.js, helpers.math.js, helpers.options.js, index.js, index.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/specs/plugin.tooltip.tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.794)
- **Top Global Matches:** file_cluster_10: 5.794, file_cluster_11: 7.236, file_cluster_2: 8.12
- **Magnitude:** 229.1 | **LOC:** 1952 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.4%), Guard Balance (formerly Safety Score) (45.4%), Complexity Load (formerly Cognitive Load) (8.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSlice` **(Defensive Guards)** (Impact: 8.4)
  * `recursive` **(Defensive Guards)** (Impact: 6.7)
  * `makeView` **(Many-Argument Workhorses)** (Impact: 5.0)
  * `itemSort` **(Callbacks & Closures)** (Impact: 3.6)
  * `filter` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 183`, `args: 92`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `duplicate_logic: 6`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 63`
* *Defense:* `safety: 7`, `test: 166`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.805
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/plugins/plugin.decimation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.367)
- **Top Global Matches:** file_cluster_15: 7.367, file_cluster_10: 7.621, file_cluster_9: 7.981
- **Magnitude:** 225.22 | **LOC:** 288 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.378; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%), Complexity Load (formerly Cognitive Load) (69.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `minMaxDecimation` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `beforeElementsUpdate` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `lttbDecimation` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `getStartAndCountOfVisiblePointsSimplified` **(Compute Cores)** (Impact: 7.9)
  * `cleanDecimatedDataset` **(Compute Cores)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 34`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 9`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.378
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.019935
  * `Imports (Out-Degree: 5):` index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/specs/core.controller.tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.623)
- **Top Global Matches:** file_cluster_10: 5.623, file_cluster_11: 8.127, file_cluster_2: 8.303
- **Magnitude:** 214.68 | **LOC:** 2340 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.2%), Concurrency Surface (formerly Concurrency) (36.6%), Complexity Load (formerly Cognitive Load) (5.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `color` **(Callbacks & Closures)** (Impact: 3.1)
  * `iterateOptions` **(I/O & Config Routines)** (Impact: 2.3)
  * `onResize` **(Defensive Guards)** (Impact: 2.0)
  * `beforeDatasetDraw` **(Callbacks & Closures)** (Impact: 1.9)
  * `afterDatasetDraw` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 183`, `args: 166`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 113`, `fragile_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 22`
* *Defense:* `safety: 6`, `test: 365`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.805
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/platform/platform.dom.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.032)
- **Top Global Matches:** file_cluster_15: 6.032, file_cluster_10: 7.422, file_cluster_11: 7.919
- **Magnitude:** 204.98 | **LOC:** 390 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.1%), Connectivity (formerly Api Exposure) (34.2%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initCanvas` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* /** * Initializes the canvas style and render size without modifying the canvas display size, * sinc...
  * `createResizeObserver` **(Many-Argument Workhorses)** (Impact: 13.9)
  * `createAttachObserver` **(Compute Cores)** (Impact: 10.8)
  * `createDetachObserver` **(Compute Cores)** (Impact: 10.8)
  * `acquireContext` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 39`, `args: 29`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 15`, `doc: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.627
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.022092
  * `Imports (Out-Degree: 4):` helpers.core.js, helpers.dom.js, helpers.extras.js, platform.base.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/types/extensions/scale.ts` (TYPESCRIPT) | Magnitude: 4.96 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, generics: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/fixtures/controller.line/cubicInterpolationMode/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 44, branch: 2, structural_boundaries: 2, args: 2
- `test/fixtures/controller.radar/borderDash/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 43, branch: 2, structural_boundaries: 2, args: 2
- `test/specs/core.layouts.tests.js` (JAVASCRIPT) | Magnitude: 23.84 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 508, test: 126, core_var_decl: 32, structural_boundaries: 30
- `test/fixtures/controller.radar/borderColor/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 51, branch: 4, structural_boundaries: 4, safety: 4
- `test/fixtures/core.layouts/hidden-vertical-boxes.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/specs/helpers.collection.tests.js` (JAVASCRIPT) | Magnitude: 15.82 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 38, test: 31, args: 6, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/integration/react-browser/public/index.html` (HTML) | Magnitude: 19.34 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 7, design_snake_case: 7, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/helpers/helpers.curve.ts` (TYPESCRIPT) | Magnitude: 242.18 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 150, core_var_decl: 52, state_mutation: 47, branch: 36
- `test/fixtures/core.interaction/nearest-point-behind-scale.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 43, concurrency: 2, structural_boundaries: 1, args: 1
- `src/scales/scale.linear.js` (JAVASCRIPT) | Magnitude: 24.14 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 10, branch: 7, core_var_decl: 7
- `test/fixtures/scale.time/labels-date.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 2, structural_boundaries: 1, args: 1
- `test/fixtures/core.interaction/nearest-partial-bar.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 40, concurrency: 2, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/plugins/index.js` (JAVASCRIPT) | Magnitude: 20.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 7, structural_boundaries: 7, api: 7, import: 7
- `src/core/index.ts` (TYPESCRIPT) | Magnitude: 30.3 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 16, api: 15, import: 15, branch: 14
- `src/controllers/index.js` (JAVASCRIPT) | Magnitude: 22.16 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 8, structural_boundaries: 8, api: 8, import: 8
- `src/helpers/index.ts` (TYPESCRIPT) | Magnitude: 31.32 | Delta: **0.186** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, api: 16, import: 16, branch: 1
- `src/index.umd.ts` (TYPESCRIPT) | Magnitude: 40.78 | Delta: **0.285** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, import: 18, state_mutation: 16, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/fixtures/controller.line/borderJoinStyle/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 54, branch: 4, structural_boundaries: 4, safety: 4
- `test/fixtures/controller.line/borderColor/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, branch: 4, structural_boundaries: 4, safety: 4
- `test/fixtures/controller.radar/backgroundColor/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, branch: 4, structural_boundaries: 4, safety: 4
- `test/fixtures/controller.line/borderDash/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, branch: 2, structural_boundaries: 2, args: 2
- `test/fixtures/controller.radar/fill/scriptable.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, branch: 2, structural_boundaries: 2, args: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/helpers/helpers.dom.ts` -> **Josh Kelley** (100.0% isolated ownership) | Magnitude: 249.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/helpers/helpers.dom.ts` -> **Severity: 0.259** (Bridge: 0.0026 * Flux: 100.0%)
- `src/core/core.controller.js` -> **Severity: 0.102** (Bridge: 0.001 * Flux: 99.9967%)
- `src/plugins/plugin.filler/index.js` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 100.0%)
- `src/core/core.datasetController.js` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 99.9999%)
- `src/core/core.defaults.js` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 99.9694%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/helpers/helpers.core.ts` -> **Severity: 2.87** (Embedded: 0.0464 * Error Risk: 61.885%)
- `src/helpers/helpers.math.ts` -> **Severity: 2.593** (Embedded: 0.0414 * Error Risk: 62.5994%)
- `src/helpers/helpers.canvas.ts` -> **Severity: 2.499** (Embedded: 0.0351 * Error Risk: 71.2145%)
- `src/helpers/helpers.options.ts` -> **Severity: 2.279** (Embedded: 0.0341 * Error Risk: 66.8519%)
- `src/core/core.defaults.js` -> **Severity: 2.171** (Embedded: 0.0372 * Error Risk: 58.3027%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/helpers/helpers.core.ts` -> **Severity: 1443.115** (Blast Radius: 38.758 * Doc Risk: 37.234%)
- `src/helpers/helpers.math.ts` -> **Severity: 585.017** (Blast Radius: 17.063 * Doc Risk: 34.2857%)
- `src/platform/index.js` -> **Severity: 484.3** (Blast Radius: 4.843 * Doc Risk: 100.0%)
- `src/helpers/helpers.intl.ts` -> **Severity: 342.6** (Blast Radius: 3.426 * Doc Risk: 100.0%)
- `src/helpers/helpers.color.ts` -> **Severity: 305.9** (Blast Radius: 3.059 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 25 literal sites + 7 sites through wrappers = 32

- `abstract` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `src/core/core.adapters.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3177 call pairs -- scoped 46.2%, unique 0.0%, ambiguous 12.0%, external 41.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 2694 | 47.7% | 0.0% | 13.2% | 39.1% |
| typescript | 465 | 37.8% | 0.0% | 5.4% | 56.8% |
| shell | 18 | 33.3% | 0.0% | 0.0% | 66.7% |

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
