# ARCHITECTURAL_BRIEF: element
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ElemeFE/element.git` |
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
- **Scope:** 774 analyzed artifact(s), 84822 LOC.
- **Load-bearing artifact:** `packages/theme-chalk/src/common/var.scss` -- 88 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/index.js` -- pulls in 91 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/utils/lodash.js` at magnitude 11369.84 (structural weight, not risk).
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
| Total Artifacts | 1144 |
| Analyzed Artifacts (Scanned) | 774 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 370 |
| Total LOC | 84822 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6816 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4061 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6942 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 84 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 320 | 43832 | 41.3% |
| CSS | 165 | 12864 | 21.3% |
| HTML | 151 | 24996 | 19.5% |
| TYPESCRIPT | 91 | 1768 | 11.8% |
| MARKDOWN | 14 | 0 | 1.8% |
| XML | 13 | 27 | 1.7% |
| JSON | 12 | 1170 | 1.6% |
| YAML | 5 | 132 | 0.6% |
| PLAINTEXT | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 33 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 773 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Declarative / Non-Code 33%, Interface Declarations Files 5%, Large Core Modules (2) 5%, Callbacks & Closures Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 753 | 97.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 370*

**Composition by Extension & Reason:**
- `.md`: 264x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 46x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.tpl`: 11x Excluded (Unsupported Extension: '.tpl')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vue`: 4x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 2x Excluded (Explicitly Denied Extension: '.woff')
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1275 LOC), 1x Excluded (Massive Static Asset Blob: 4196 LOC)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.0 | 5.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.3 | 27.0 | 42.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.8 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.3 | 79.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 64 | 30 | 0 | `test/unit/specs/date-picker.spec.js` |
| cleanup | 112 | 55 | 0 | `packages/notification/src/main.vue` |
| guards | 2322 | 227 | 8 | `src/utils/lodash.js` |
| danger | 425 | 75 | 0 | `src/utils/lodash.js` |
| concurrency | 1924 | 108 | 2 | `test/unit/specs/date-picker.spec.js` |
| connectivity | 2065 | 496 | 5 | `packages/theme-chalk/src/common/var.scss` |
| io | 128 | 29 | 0 | `examples/components/footer.vue` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1023 | 85 | 1 | `test/unit/specs/date-picker.spec.js` |
| serialization | 35 | 13 | 0 | `test/unit/specs/upload.spec.js` |
| regex | 197 | 52 | 0 | `src/utils/lodash.js` |
| events | 1709 | 192 | 7 | `packages/date-picker/src/panel/date.vue` |
| tests | 2968 | 65 | 0 | `test/unit/specs/date-picker.spec.js` |
| docs | 1797 | 116 | 3 | `src/utils/lodash.js` |
| debt | 438 | 81 | 1 | `test/unit/specs/table.spec.js` |
| mutation | 15111 | 441 | 49 | `src/utils/lodash.js` |
| dead_code | 196 | 66 | 0 | `src/utils/date-util.js` |
| credential | 5 | 2 | 0 | `examples/components/footer.vue` |
| threat | 34 | 4 | 0 | `src/locale/lang/lo-LA.js` |
| ml_ai | 23 | 6 | 0 | `packages/empty/src/img-empty.vue` |
| ui | 874 | 185 | 3 | `packages/table/src/store/watcher.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/components/footer.vue` (Hits: 34)
- `examples/components/header.vue` (Hits: 12)
- `packages/date-picker/src/basic/year-table.vue` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **var.scss** (`packages/theme-chalk/src/common/var.scss`) — 88 inbound connections
2. **mixins.scss** (`packages/theme-chalk/src/mixins/mixins.scss`) — 79 inbound connections
3. **util.js** (`test/unit/util.js`) — 62 inbound connections
4. **date.vue** (`packages/date-picker/src/panel/date.vue`) — 24 inbound connections
5. **picker.vue** (`packages/date-picker/src/picker.vue`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`src/index.js`) — 91 outbound dependencies
2. **element-ui.d.ts** (`types/element-ui.d.ts`) — 90 outbound dependencies
3. **index.scss** (`packages/theme-chalk/src/index.scss`) — 87 outbound dependencies
4. **index.scss** (`examples/demo-styles/index.scss`) — 48 outbound dependencies
5. **entry.js** (`examples/entry.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `orderBy` **(Defensive Guards)** (@ `packages/table/src/util.js`) -> Impact: **66.5** | LOC: 56
- `created` **(Defensive Guards)** (@ `packages/tree/src/tree.vue`) -> Impact: **61.1** | LOC: 163
- `wrappedRowRender` **(Defensive Guards)** (@ `packages/table/src/table-body.js`) -> Impact: **54.7** | LOC: 90
- `fromString` **(Defensive Guards)** (@ `packages/color-picker/src/color.js`) -> Impact: **52.1** | LOC: 81
- `fromString` **(Defensive Guards)** (@ `examples/components/theme-configurator/editor/color-picker/src/color.js`) -> Impact: **49.3** | LOC: 80
- `setChecked` **(Many-Argument Workhorses)** (@ `packages/tree/src/model/node.js`) -> Impact: **40.6** | LOC: 52
- `constructor` **(Defensive Guards)** (@ `packages/tree/src/model/node.js`) -> Impact: **37.5** | LOC: 71
- `openModal` **(Many-Argument Workhorses)** (@ `src/utils/popup/popup-manager.js`) -> Impact: **36.4** | LOC: 42
- `getCellClasses` **(Defensive Guards)** (@ `packages/date-picker/src/basic/date-table.vue`) -> Impact: **34.9** | LOC: 48
- `visible` **(Compute Cores)** (@ `packages/select/src/select.vue`) -> Impact: **33.9** | LOC: 56

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/utils` | 18 | 14225.2 | 43.02% | 34.54% |
| `test/unit/specs` | 63 | 6242.42 | 7.79% | 0.0% |
| `packages/table/src` | 12 | 2084.7 | 51.18% | 13.33% |
| `packages/date-picker/src/panel` | 6 | 1288.88 | 41.02% | 6.16% |
| `packages/tree/src/model` | 3 | 843.58 | 52.58% | 32.46% |
| `packages/select/src` | 5 | 802.82 | 41.87% | 16.11% |
| `packages/date-picker/src/basic` | 4 | 733.88 | 49.28% | 6.7% |
| `packages/table/src/store` | 6 | 681.82 | 73.08% | 24.4% |
| `packages/date-picker/src` | 1 | 607.26 | 44.83% | 0.0% |
| `packages/cascader-panel/src` | 5 | 562.82 | 43.13% | 19.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `types/tree.d.ts` -> **100.0%** Exposure
- `src/utils/date-util.js` -> **99.9997%** Exposure
- `src/transitions/collapse-transition.js` -> **99.9818%** Exposure
- `src/utils/types.js` -> **99.9447%** Exposure
- `types/upload.d.ts` -> **99.708%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/footer-nav.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/alpha-slider.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/hue-slider.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/sv-panel.vue` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/specs/table.spec.js` -> **0** Orphaned Functions | **48** Duplicates
- `test/unit/specs/autocomplete.spec.js` -> **0** Orphaned Functions | **42** Duplicates
- `test/unit/specs/date-picker.spec.js` -> **2** Orphaned Functions | **40** Duplicates
- `test/unit/specs/form.spec.js` -> **0** Orphaned Functions | **23** Duplicates
- `src/utils/date-util.js` -> **22** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `401` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/utils/lodash.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.555)
- **Top Global Matches:** file_cluster_7: 5.555, file_cluster_12: 5.999, file_cluster_5: 8.516
- **Magnitude:** 11369.84 | **LOC:** 18076 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.78; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.2%), Concurrency Surface (formerly Concurrency) (22.8%), Complexity Load (formerly Cognitive Load) (16.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 1394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 1564`, `args: 689`, `func_start: 512`
* *Risk/State:* `safety_bypasses: 258`, `state_mutation: 1368`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 370`, `doc: 676`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/date.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.441)
- **Top Global Matches:** file_cluster_10: 5.441, file_cluster_12: 7.242, file_cluster_2: 7.435
- **Magnitude:** 1067.94 | **LOC:** 369 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.112; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (25.3%), Connectivity (formerly Api Exposure) (3.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 77`, `args: 57`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 53`
* *Architecture:* `api: 2`
* *Defense:* `safety: 19`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.112
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001294
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/specs/date-picker.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.746)
- **Top Global Matches:** file_cluster_10: 6.746, file_cluster_11: 8.151, file_cluster_15: 9.53
- **Magnitude:** 911.52 | **LOC:** 2856 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.4%), Complexity Load (formerly Cognitive Load) (32.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testWeek` **(Callbacks & Closures)** (Impact: 2.3)
  * `keyDown` **(Callbacks & Closures)** (Impact: 2.0)
  * `handleChange` **(State Mutators)** (Impact: 1.6)
  * `handleInput` **(State Mutators)** (Impact: 1.6)
  * `handleInput` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 599
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 498`, `args: 401`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 141`, `planned_debt: 2`, `duplicate_logic: 40`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 239`, `import: 2`
* *Defense:* `safety: 6`, `test: 415`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util, date-picker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/table.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.822)
- **Top Global Matches:** file_cluster_10: 7.822, file_cluster_11: 8.934, file_cluster_15: 9.198
- **Magnitude:** 687.6 | **LOC:** 2258 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.5%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tableRowClassName` **(Defensive Guards)** (Impact: 6.1)
  * `sortMethod` **(Compute Cores)** (Impact: 5.7)
  * `getSummary` **(Callbacks & Closures)** (Impact: 5.1)
  * `createInstance` **(Callbacks & Closures)** (Impact: 4.3)
  * `createTable` **(Many-Argument Workhorses)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 403
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 352`, `args: 329`, `func_start: 93`
* *Risk/State:* `state_mutation: 90`, `fragile_debt: 11`, `duplicate_logic: 48`
* *Architecture:* `concurrency: 143`, `import: 1`
* *Defense:* `safety: 9`, `test: 299`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/popper.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.558)
- **Top Global Matches:** file_cluster_10: 7.558, file_cluster_15: 7.598, file_cluster_12: 8.177
- **Magnitude:** 637.18 | **LOC:** 1277 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.436; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (46.3%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Popper` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* * then, if even in its new placement, the popper is overlapping its reference element, it will be mo...
  * `_getBoundaries` **(Defensive Guards)** (Impact: 24.9)
    * *Intent:* /** * Computed the boundaries limits and return them */
  * `parse` **(Defensive Guards)** (Impact: 24.3)
    * *Intent:* /** * Helper used to generate poppers from a configuration file */
  * `flip` **(Defensive Guards)** (Impact: 22.7)
    * *Intent:* /** * Modifier used to flip the placement of the popper when the latter is starting overlapping its ...
  * `arrow` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* /** * Modifier used to move the arrows on the edge of the popper to make sure them are always betwee...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 164`, `args: 55`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 130`, `fragile_debt: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 66`, `doc: 39`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.436
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002911
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/select/src/select.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.49)
- **Top Global Matches:** file_cluster_4: 8.49, file_cluster_15: 8.553, file_cluster_10: 9.305
- **Magnitude:** 631.8 | **LOC:** 901 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.94; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (71.9%), Guard Balance (formerly Safety Score) (57.5%), Concurrency Surface (formerly Concurrency) (29.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visible` **(Compute Cores)** (Impact: 33.9)
  * `handleQueryChange` **(Defensive Guards)** (Impact: 28.7)
  * `value` **(Compute Cores)** (Impact: 21.8)
  * `handleOptionSelect` **(Compute Cores)** (Impact: 20.5)
  * `emptyText` **(Defensive Guards)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 103`, `args: 85`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `state_mutation: 83`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 55`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.003327
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/date-picker/src/picker.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.436)
- **Top Global Matches:** file_cluster_15: 7.436, file_cluster_11: 8.551, file_cluster_4: 8.665
- **Magnitude:** 607.26 | **LOC:** 957 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); blast radius 19.384; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (49.6%), Complexity Load (formerly Cognitive Load) (44.8%), Concurrency Surface (formerly Concurrency) (19.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mountPicker` **(Defensive Guards)** (Impact: 21.2)
  * `handleKeydown` **(Defensive Guards)** (Impact: 19.6)
  * `valueEquals` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /* * Considers: * 1. Date object * 2. date string * 3. array of 1 or 2 */
  * `displayValue` **(Defensive Guards)** (Impact: 16.9)
  * `selectionMode` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 125`, `args: 97`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 90`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.384
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.033002
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `packages/tree/src/model/node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.56)
- **Top Global Matches:** file_cluster_4: 7.56, file_cluster_9: 10.303, file_cluster_15: 10.842
- **Magnitude:** 533.64 | **LOC:** 485 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.112; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setChecked` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `constructor` **(Defensive Guards)** (Impact: 37.5)
  * `insertChild` **(Defensive Guards)** (Impact: 25.6)
  * `expand` **(Defensive Guards)** (Impact: 18.7)
  * `reInitChecked` **(Defensive Guards)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 64`, `args: 38`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.112
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001294
  * `Imports (Out-Degree: 3):` util, merge, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/date-picker/src/panel/date-range.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.045)
- **Top Global Matches:** file_cluster_15: 8.045, file_cluster_11: 8.095, file_cluster_13: 8.528
- **Magnitude:** 488.58 | **LOC:** 681 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.148; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.1%), Guard Balance (formerly Safety Score) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleDateInput` **(Defensive Guards)** (Impact: 20.3)
  * `value` **(Defensive Guards)** (Impact: 19.7)
  * `handleMinTimePick` **(Compute Cores)** (Impact: 14.7)
  * `handleMaxTimePick` **(Compute Cores)** (Impact: 14.7)
  * `isValidValue` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 71`, `args: 101`, `func_start: 49`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 83`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0023
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/table/src/table-header.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.851)
- **Top Global Matches:** file_cluster_15: 6.851, file_cluster_10: 7.745, file_cluster_11: 8.035
- **Magnitude:** 409.42 | **LOC:** 512 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleSortClick` **(Defensive Guards)** (Impact: 32.2)
  * `handleMouseMove` **(Compute Cores)** (Impact: 27.4)
  * `getHeaderCellClass` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `render` **(Compute Cores)** (Impact: 18.0)
  * `handleFilterClick` **(Compute Cores)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 86`, `args: 50`, `func_start: 32`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 8`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` filter-panel.vue, layout-observer, helper, checkbox, dom, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/basic/date-table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.72)
- **Top Global Matches:** file_cluster_6: 7.72, file_cluster_4: 9.251, file_cluster_15: 15.985
- **Magnitude:** 355.48 | **LOC:** 442 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.5%), Guard Balance (formerly Safety Score) (53.4%), Debt Markers (formerly Tech Debt) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCellClasses` **(Defensive Guards)** (Impact: 34.9)
  * `rows` **(Defensive Guards)** (Impact: 32.3)
  * `handleClick` **(Defensive Guards)** (Impact: 30.8)
  * `markRange` **(Defensive Guards)** (Impact: 20.2)
  * `isWeekActive` **(Defensive Guards)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 46`, `args: 27`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table-body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.254)
- **Top Global Matches:** file_cluster_4: 6.254, file_cluster_15: 9.322, file_cluster_11: 10.22
- **Magnitude:** 350.28 | **LOC:** 470 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (83.5%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (55.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrappedRowRender` **(Defensive Guards)** (Impact: 54.7)
  * `traverse` **(Defensive Guards)** (Impact: 29.5)
  * `getRowClass` **(Defensive Guards)** (Impact: 22.5)
  * `handleCellMouseEnter` **(Compute Cores)** (Impact: 20.8)
  * `getCellClass` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 73`, `args: 40`, `func_start: 28`
* *Risk/State:* `state_mutation: 36`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` layout-observer, helper, table-row.js, util, checkbox, tooltip, dom, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/panel/date.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.921)
- **Top Global Matches:** file_cluster_15: 7.921, file_cluster_11: 7.996, file_cluster_10: 8.057
- **Magnitude:** 338.54 | **LOC:** 610 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); blast radius 44.028; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (34.3%), Debt Markers (formerly Tech Debt) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectionMode` **(Defensive Guards)** (Impact: 14.8)
  * `value` **(Defensive Guards)** (Impact: 13.2)
  * `emit` **(Defensive Guards)** (Impact: 12.7)
  * `handleDatePick` **(Defensive Guards)** (Impact: 12.2)
  * `handleTimePick` **(Many-Argument Workhorses)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 61`, `args: 74`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 45`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052393
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `packages/color-picker/src/color.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.127)
- **Top Global Matches:** file_cluster_4: 7.127, file_cluster_15: 9.156, file_cluster_10: 9.839
- **Magnitude:** 332.28 | **LOC:** 318 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (80.0%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromString` **(Defensive Guards)** (Impact: 52.1)
  * `rgb2hsv` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* // `rgbToHsv` // Converts an RGB color value to HSV // *Assumes:* r, g, and b are contained in the s...
  * `doOnChange` **(I/O & Config Routines)** (Impact: 13.7)
  * `set` **(Defensive Guards)** (Impact: 9.4)
  * `toHex` **(Callbacks & Closures)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 44`, `args: 24`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/components/theme-configurator/editor/color-picker/src/color.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.122)
- **Top Global Matches:** file_cluster_4: 7.122, file_cluster_15: 9.137, file_cluster_10: 9.812
- **Magnitude:** 329.46 | **LOC:** 317 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.5%), Guard Balance (formerly Safety Score) (66.4%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromString` **(Defensive Guards)** (Impact: 49.3)
  * `rgb2hsv` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* // `rgbToHsv` // Converts an RGB color value to HSV // *Assumes:* r, g, and b are contained in the s...
  * `doOnChange` **(I/O & Config Routines)** (Impact: 13.7)
  * `set` **(Defensive Guards)** (Impact: 9.4)
  * `toHex` **(Callbacks & Closures)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 43`, `args: 24`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cascader/src/cascader.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.068)
- **Top Global Matches:** file_cluster_15: 7.068, file_cluster_11: 7.962, file_cluster_10: 8.079
- **Magnitude:** 308.84 | **LOC:** 664 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.731; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Guard Balance (formerly Safety Score) (56.0%), Complexity Load (formerly Cognitive Load) (29.9%), Concurrency Surface (formerly Concurrency) (22.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleSuggestionKeyDown` **(Compute Cores)** (Impact: 13.7)
  * `mounted` **(I/O & Config Routines)** (Impact: 13.5)
  * `handleInput` **(Compute Cores)** (Impact: 10.9)
  * `checkedValue` **(State Mutators)** (Impact: 9.3)
  * `handleKeyDown` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 76`, `args: 63`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.731
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.002329
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/table/src/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.162)
- **Top Global Matches:** file_cluster_4: 8.162, file_cluster_10: 8.724, file_cluster_15: 8.914
- **Magnitude:** 295.9 | **LOC:** 274 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 4.11; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `orderBy` **(Defensive Guards)** (Impact: 66.5)
  * `toggleRowStatus` **(Defensive Guards)** (Impact: 21.4)
  * `walkTreeNode` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `getRowIdentity` **(Defensive Guards)** (Impact: 12.9)
  * `parseHeight` **(Defensive Guards)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 83`, `args: 34`, `func_start: 22`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.11
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.008745
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `test/unit/specs/select.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.481)
- **Top Global Matches:** file_cluster_10: 6.481, file_cluster_11: 8.019, file_cluster_15: 9.01
- **Magnitude:** 292.36 | **LOC:** 911 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.3%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSelectVm` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `data` **(I/O & Config Routines)** (Impact: 4.9)
  * `getSelectComponentVm` **(Callbacks & Closures)** (Impact: 3.0)
  * `data` **(I/O & Config Routines)** (Impact: 2.0)
  * `data` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 158
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 124`, `args: 96`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `planned_debt: 4`
* *Architecture:* `concurrency: 38`, `import: 2`
* *Defense:* `safety: 3`, `test: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util, select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/tree.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.769)
- **Top Global Matches:** file_cluster_10: 6.769, file_cluster_15: 8.761, file_cluster_12: 9.142
- **Magnitude:** 288.84 | **LOC:** 894 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.5%), Complexity Load (formerly Cognitive Load) (33.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.8)
  * `loadNode` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 119`, `args: 101`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 39`, `import: 1`
* *Defense:* `safety: 6`, `test: 154`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/tree-store.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.095)
- **Top Global Matches:** file_cluster_10: 7.095, file_cluster_15: 7.114, file_cluster_11: 8.106
- **Magnitude:** 283.96 | **LOC:** 341 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setCheckedKeys` **(Compute Cores)** (Impact: 24.1)
  * `filter` **(Defensive Guards)** (Impact: 15.6)
  * `traverse` **(Defensive Guards)** (Impact: 15.3)
  * `getCheckedNodes` **(Compute Cores)** (Impact: 14.8)
  * `traverse` **(Callbacks & Closures)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 43`, `args: 47`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` node, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/tree.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.403)
- **Top Global Matches:** file_cluster_15: 7.403, file_cluster_11: 7.669, file_cluster_10: 8.633
- **Magnitude:** 277.18 | **LOC:** 497 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.45; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (56.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `created` **(Defensive Guards)** (Impact: 61.1)
  * `handleKeydown` **(Defensive Guards)** (Impact: 15.4)
  * `getNodePath` **(Defensive Guards)** (Impact: 7.7)
  * `setCheckedNodes` **(State Mutators)** (Impact: 3.7)
  * `setCheckedKeys` **(State Mutators)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 45`, `args: 44`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.45
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001725
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/table/src/store/watcher.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.546)
- **Top Global Matches:** file_cluster_15: 7.546, file_cluster_10: 7.556, file_cluster_11: 8.388
- **Magnitude:** 273.92 | **LOC:** 382 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.591; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.7%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearFilter` **(Defensive Guards)** (Impact: 15.0)
  * `updateAllSelected` **(Defensive Guards)** (Impact: 14.9)
  * `_toggleAllSelection` **(I/O & Config Routines)** (Impact: 11.4)
  * `updateColumns` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* // 更新列
  * `toggleRowSelection` **(State Mutators)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 49`, `args: 40`, `func_start: 23`
* *Risk/State:* `state_mutation: 47`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.591
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.002695
  * `Imports (Out-Degree: 5):` util, current, expand, tree, merge, vue
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/specs/form.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.283)
- **Top Global Matches:** file_cluster_10: 6.283, file_cluster_11: 7.693, file_cluster_2: 8.602
- **Magnitude:** 270.88 | **LOC:** 994 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (20.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkName` **(Callbacks & Closures)** (Impact: 6.3)
  * `checkName` **(Callbacks & Closures)** (Impact: 6.3)
  * `checkName` **(Callbacks & Closures)** (Impact: 6.3)
  * `validator` **(Callbacks & Closures)** (Impact: 4.2)
  * `data` **(Callbacks & Closures)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 99
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 130`, `args: 100`, `func_start: 40`
* *Risk/State:* `state_mutation: 56`, `duplicate_logic: 23`
* *Architecture:* `concurrency: 24`, `import: 2`
* *Defense:* `safety: 4`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util, es6-promise
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/cascader.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.378)
- **Top Global Matches:** file_cluster_11: 6.378, file_cluster_10: 6.992, file_cluster_15: 7.422
- **Magnitude:** 250.14 | **LOC:** 417 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (45.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filterMethod` **(Parameter Forwarders)** (Impact: 3.7)
  * `getOptions` **(Parameter Forwarders)** (Impact: 1.8)
  * `getMenus` **(Parameter Forwarders)** (Impact: 1.5)
  * `getCloseButton` **(Parameter Forwarders)** (Impact: 1.5)
  * `data` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Concurrency (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 62`, `args: 31`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`, `duplicate_logic: 7`
* *Architecture:* `concurrency: 43`, `import: 2`
* *Defense:* `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util, cascader
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table-layout.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.808)
- **Top Global Matches:** file_cluster_6: 7.808, file_cluster_4: 12.556, file_cluster_8: 14.608
- **Magnitude:** 237.16 | **LOC:** 250 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateColumnsWidth` **(Defensive Guards)** (Impact: 32.4)
  * `updateElsHeight` **(Compute Cores)** (Impact: 21.4)
  * `setHeight` **(Defensive Guards)** (Impact: 14.7)
  * `constructor` **(Compute Cores)** (Impact: 8.9)
  * `notifyObservers` **(Callbacks & Closures)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 39`, `args: 25`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util, scrollbar-width, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/menu/src/menu-item-group.vue` (HTML) | Magnitude: 17.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 9, branch: 6, core_var_decl: 6
- `types/tooltip.d.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 16, indent_spaces: 15, structural_boundaries: 8, api: 2
- `packages/empty/src/index.vue` (HTML) | Magnitude: 11.26 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 10, branch: 8, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/tree/src/model/tree-store.js` (JAVASCRIPT) | Magnitude: 283.96 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 274, branch: 72, core_var_decl: 59, args: 47
- `src/utils/aria-utils.js` (JAVASCRIPT) | Magnitude: 94.98 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 64, branch: 28, structural_boundaries: 20, state_mutation: 14
- `src/utils/popper.js` (JAVASCRIPT) | Magnitude: 637.18 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 641, structural_boundaries: 164, branch: 139, core_var_decl: 132
- `test/unit/specs/calendar.spec.js` (JAVASCRIPT) | Magnitude: 36.54 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 94, test: 30, core_var_decl: 18, structural_boundaries: 14
- `src/index.js` (JAVASCRIPT) | Magnitude: 31.34 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 93, import: 91, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/components/theme-configurator/editor/color-picker/src/components/sv-panel.vue` (HTML) | Magnitude: 25.18 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, core_var_decl: 17, design_snake_case: 17, structural_boundaries: 14
- `packages/color-picker/src/components/sv-panel.vue` (HTML) | Magnitude: 25.18 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, core_var_decl: 17, design_snake_case: 17, structural_boundaries: 14
- `packages/date-picker/src/panel/month-range.vue` (HTML) | Magnitude: 182.76 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 254, branch: 51, args: 35, structural_boundaries: 32
- `examples/app.vue` (HTML) | Magnitude: 33.24 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 20, branch: 19, args: 9
- `packages/skeleton/src/index.vue` (HTML) | Magnitude: 32.12 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 70, branch: 12, decorators: 8, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `types/upload.d.ts` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 47, doc: 28, args: 15
- `examples/demo-styles/container.scss` (CSS) | Magnitude: 0.79 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, class_start: 14, closures: 3, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/select/src/option-group.vue` (HTML) | Magnitude: 15.3 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 8, args: 6, func_start: 6
- `packages/alert/src/main.vue` (HTML) | Magnitude: 25.32 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 82, branch: 18, decorators: 17, structural_boundaries: 12
- `packages/message/src/main.vue` (HTML) | Magnitude: 45.58 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 105, args: 13, branch: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/table/src/store/watcher.js` (JAVASCRIPT) | Magnitude: 273.92 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 299, branch: 67, core_var_decl: 63, structural_boundaries: 49
- `examples/extension/src/editor/editor.vue` (HTML) | Magnitude: 135.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 168, class_start: 32, core_var_decl: 30, state_mutation: 27
- `packages/table/src/table.vue` (HTML) | Magnitude: 220.62 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 617, branch: 84, decorators: 66, core_var_decl: 66
- `packages/radio/src/radio-group.vue` (HTML) | Magnitude: 46.58 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 100, branch: 22, core_var_decl: 14, structural_boundaries: 11
- `packages/date-picker/src/panel/date-range.vue` (HTML) | Magnitude: 488.58 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 610, branch: 124, args: 101, state_mutation: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/theme-chalk/src/index.scss` (CSS) | Magnitude: 0.84 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 87
- `examples/demo-styles/index.scss` (CSS) | Magnitude: 0.8 | Delta: **0.165** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/theme-chalk/src/descriptions-item.scss` (CSS) | Magnitude: 0.79 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, class_start: 6, closures: 4, ui_framework: 3
- `packages/theme-chalk/src/date-picker/year-table.scss` (CSS) | Magnitude: 0.79 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 39, class_start: 9, closures: 5, branch: 1
- `packages/theme-chalk/src/breadcrumb.scss` (CSS) | Magnitude: 0.8 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, closures: 5, class_start: 4, import: 3
- `packages/theme-chalk/src/date-picker.scss` (CSS) | Magnitude: 0.76 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/select/src/select.vue` (HTML) | Magnitude: 631.8 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 821, branch: 228, structural_boundaries: 103, args: 85

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `types/tabs.d.ts` (TYPESCRIPT) | Magnitude: 0.96 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 11, doc: 9, indent_spaces: 8, api: 3
- `types/option.d.ts` (TYPESCRIPT) | Magnitude: 0.71 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 4, indent_spaces: 3, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `types/select.d.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 27, indent_spaces: 26, structural_boundaries: 10, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/locale/index.js` (JAVASCRIPT) | Magnitude: 0.05 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 19, core_var_decl: 18, design_snake_case: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/utils/popup/index.js` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/main/index.js` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 50.0%)
- `src/utils/util.js` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/pagination/src/pagination.js` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.8931%)
- `packages/table/src/store/index.js` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 84.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/unit/util.js` -> **Severity: 4.468** (Embedded: 0.0802 * Error Risk: 55.7067%)
- `packages/main/index.js` -> **Severity: 2.451** (Embedded: 0.047 * Error Risk: 52.1415%)
- `src/utils/util.js` -> **Severity: 1.385** (Embedded: 0.0268 * Error Risk: 51.5832%)
- `src/utils/dom.js` -> **Severity: 1.109** (Embedded: 0.0205 * Error Risk: 54.0388%)
- `src/utils/merge.js` -> **Severity: 0.788** (Embedded: 0.0149 * Error Risk: 52.854%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/main/index.js` -> **Severity: 2797.8** (Blast Radius: 27.978 * Doc Risk: 100.0%)
- `src/utils/util.js` -> **Severity: 1287.7** (Blast Radius: 12.877 * Doc Risk: 100.0%)
- `src/utils/types.js` -> **Severity: 1175.382** (Blast Radius: 13.321 * Doc Risk: 88.2353%)
- `src/utils/dom.js` -> **Severity: 696.4** (Blast Radius: 6.964 * Doc Risk: 100.0%)
- `packages/table/src/util.js` -> **Severity: 411.0** (Blast Radius: 4.11 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 52 literal sites + 2 sites through wrappers = 54

- `loadFromLocal` (function, debug_prints, primitive): 2 call sites in 1 files -- `examples/components/theme/localstorage.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6643 call pairs -- scoped 7.9%, unique 0.7%, ambiguous 1.2%, external 90.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| html | 4528 | 1.7% | 1.1% | 0.0% | 97.3% |
| javascript | 2114 | 21.2% | 0.0% | 3.7% | 75.1% |
| typescript | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
