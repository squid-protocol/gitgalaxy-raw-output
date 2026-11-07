# ARCHITECTURAL_BRIEF: cytoscape.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cytoscape/cytoscape.js.git` |
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
- **Scope:** 642 analyzed artifact(s), 109774 LOC.
- **Load-bearing artifact:** `src/util/index.mjs` -- 85 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/collection/index.mjs` -- pulls in 21 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `documentation/js/cytoscape.umd.js` at magnitude 28837.12 (structural weight, not risk).
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
| Total Artifacts | 772 |
| Analyzed Artifacts (Scanned) | 642 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 130 |
| Total LOC | 109774 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 83.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5181 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3324 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4943 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 277 | 96033 | 43.1% |
| MARKDOWN | 218 | 331 | 34.0% |
| CSS | 80 | 7734 | 12.5% |
| HTML | 37 | 851 | 5.8% |
| JSON | 17 | 2517 | 2.6% |
| YAML | 5 | 233 | 0.8% |
| SHELL | 4 | 193 | 0.6% |
| XML | 2 | 0 | 0.3% |
| TYPESCRIPT | 1 | 1882 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 639 |
| utf-8 | bom | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Callbacks & Closures Files 21%, Declarative / Non-Code 18%, Large Core Modules (3) 6%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 423 | 65.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 218 | 34.0% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 130*

**Composition by Extension & Reason:**
- `.png`: 56x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 12896 LOC), 2x Excluded (Massive Static Asset Blob: 5251 LOC)
- `.js`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.cycss`: 1x Excluded (Unsupported Extension: '.cycss')
- `.otf`: 1x Excluded (Explicitly Denied Extension: '.otf')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.1 | 4.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.0 | 37.8 | 51.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.4 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 37.0 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 26 | 13 | 0 | `documentation/js/cytoscape.umd.js` |
| cleanup | 58 | 18 | 0 | `documentation/js/cytoscape.cjs.js` |
| guards | 3701 | 186 | 6 | `documentation/js/cytoscape.umd.js` |
| danger | 1851 | 155 | 3 | `documentation/js/cytoscape.umd.js` |
| concurrency | 651 | 60 | 0 | `tests-examples/demo-todo-app.spec.js` |
| connectivity | 1159 | 253 | 4 | `documentation/template.html` |
| io | 318 | 75 | 1 | `documentation/template.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 179 | 11 | 0 | `documentation/js/cytoscape.cjs.js` |
| time | 118 | 19 | 0 | `documentation/js/cytoscape.cjs.js` |
| serialization | 24 | 9 | 0 | `.github/workflows/scripts/merge_unstable_to_master.sh` |
| regex | 184 | 27 | 0 | `documentation/js/cytoscape.cjs.js` |
| events | 1300 | 96 | 1 | `documentation/js/cytoscape.cjs.js` |
| tests | 5129 | 142 | 4 | `test/core-graph-manipulation.mjs` |
| docs | 1498 | 62 | 0 | `index.d.ts` |
| debt | 471 | 47 | 0 | `documentation/js/cytoscape.cjs.js` |
| mutation | 39471 | 310 | 70 | `documentation/js/cytoscape.umd.js` |
| dead_code | 820 | 94 | 1 | `documentation/js/cytoscape.cjs.js` |
| credential | 1 | 1 | 0 | `documentation/demos/wine-cheese-map/index.html` |
| threat | 3 | 3 | 0 | `documentation/js/cytoscape.cjs.js` |
| ml_ai | 35 | 10 | 0 | `src/extensions/renderer/canvas/webgl/fxaa-upscaler.mjs` |
| ui | 228 | 85 | 1 | `documentation/js/cytoscape.cjs.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/template.html` (Hits: 28)
- `documentation/demos/fcose-gene/index.html` (Hits: 22)
- `documentation/demos/colajs-graph/index.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.mjs** (`src/util/index.mjs`) — 85 inbound connections
2. **is.mjs** (`src/is.mjs`) — 66 inbound connections
3. **math.mjs** (`src/math.mjs`) — 36 inbound connections
4. **test.mjs** (`src/test.mjs`) — 30 inbound connections
5. **index.js** (`benchmark/suite/index.js`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.mjs** (`src/collection/index.mjs`) — 21 outbound dependencies
2. **index.mjs** (`src/collection/algorithms/index.mjs`) — 19 outbound dependencies
3. **index.mjs** (`src/core/index.mjs`) — 16 outbound dependencies
4. **index.mjs** (`src/extensions/renderer/canvas/index.mjs`) — 16 outbound dependencies
5. **index.html** (`documentation/demos/fcose-gene/index.html`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `load` **(I/O & Config Routines)** (@ `src/extensions/renderer/base/load-listeners.mjs`) -> Impact: **548.0** | LOC: 2101
- `load` **(I/O & Config Routines)** (@ `documentation/js/cytoscape.cjs.js`) -> Impact: **511.7** | LOC: 1874
- `load` **(I/O & Config Routines)** (@ `documentation/js/cytoscape.umd.js`) -> Impact: **511.7** | LOC: 1874
- `drawNode` **(Many-Argument Workhorses)** (@ `src/extensions/renderer/canvas/drawing-nodes.mjs`) -> Impact: **375.0** | LOC: 569
- `drawNode` **(Many-Argument Workhorses)** (@ `documentation/js/cytoscape.cjs.js`) -> Impact: **314.4** | LOC: 449
- `drawNode` **(Many-Argument Workhorses)** (@ `documentation/js/cytoscape.umd.js`) -> Impact: **314.4** | LOC: 449
- `parseImpl` **(Many-Argument Workhorses)** (@ `src/style/parse.mjs`) -> Impact: **309.3** | LOC: 373
  * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name : the name of the property // - value : the parsed...
- `parseImpl` **(Many-Argument Workhorses)** (@ `documentation/js/cytoscape.cjs.js`) -> Impact: **308.1** | LOC: 349
  * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name : the name of the property // - value : the parsed...
- `parseImpl` **(Many-Argument Workhorses)** (@ `documentation/js/cytoscape.umd.js`) -> Impact: **308.1** | LOC: 349
  * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name : the name of the property // - value : the parsed...
- `drawText` **(Many-Argument Workhorses)** (@ `src/extensions/renderer/canvas/drawing-label-text.mjs`) -> Impact: **192.4** | LOC: 223

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `documentation/js` | 3 | 57466.64 | 73.65% | 15.85% |
| `src/extensions/renderer/canvas` | 15 | 4888.46 | 70.14% | 0.0% |
| `src/collection/algorithms` | 20 | 3300.36 | 71.95% | 3.14% |
| `src` | 17 | 2970.48 | 57.34% | 0.58% |
| `src/extensions/renderer/base` | 6 | 2803.62 | 63.96% | 12.85% |
| `documentation` | 4 | 2757.66 | 24.84% | 0.0% |
| `src/extensions/renderer/base/coord-ele-math` | 10 | 2756.16 | 73.31% | 0.0% |
| `src/collection` | 18 | 2706.34 | 51.74% | 0.0% |
| `src/style` | 9 | 2064.74 | 63.21% | 0.0% |
| `src/extensions/renderer/canvas/webgl` | 7 | 1805.58 | 42.54% | 18.38% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `index.d.ts` -> **100.0%** Exposure
- `benchmark/suite/index.js` -> **99.9447%** Exposure
- `documentation/demos/multiple-instances/code.js` -> **94.6665%** Exposure
- `src/selector/state.mjs` -> **74.4868%** Exposure
- `tests-examples/demo-todo-app.spec.js` -> **59.0551%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmark/graphs/random.js` -> **100.0%** Exposure
- `benchmark/suite/index.js` -> **100.0%** Exposure
- `documentation/docmaker.mjs` -> **100.0%** Exposure
- `documentation/js/cytoscape.cjs.js` -> **100.0%** Exposure
- `documentation/js/cytoscape.umd.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `index.d.ts` -> **180** Orphaned Functions | **71** Duplicates
- `documentation/js/cytoscape.cjs.js` -> **70** Orphaned Functions | **54** Duplicates
- `documentation/js/cytoscape.umd.js` -> **0** Orphaned Functions | **54** Duplicates
- `test/collection-algorithms.mjs` -> **1** Orphaned Functions | **29** Duplicates
- `test/events.mjs` -> **0** Orphaned Functions | **21** Duplicates

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
- **Unknown Dependencies:** `245` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `documentation/js/cytoscape.umd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 15.771)
- **Top Global Matches:** file_cluster_4: 15.771, file_cluster_12: 17.806, file_cluster_15: 18.862
- **Magnitude:** 28837.12 | **LOC:** 32410 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.72; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%)
- **Documentation Coverage:** 95.388% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(I/O & Config Routines)** (Impact: 511.7)
  * `drawNode` **(Many-Argument Workhorses)** (Impact: 314.4)
  * `parseImpl` **(Many-Argument Workhorses)** (Impact: 308.1)
    * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name ...
  * `render` **(Compute Cores)** (Impact: 173.1)
  * `touchmoveHandler` **(Compute Cores)** (Impact: 165.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 3729 instances
* *Concurrency (weighted view):* 154
* *State Mutation (weighted view):* 12283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5823`, `structural_boundaries: 8341`, `args: 1896`, `func_start: 2618`
* *Risk/State:* `safety_bypasses: 489`, `state_mutation: 4825`, `dead_code: 141`, `planned_debt: 9`, `duplicate_logic: 54`
* *Architecture:* `api: 73`, `concurrency: 39`
* *Defense:* `safety: 1190`, `doc: 186`, `test: 367`, `sync_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.72
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00312
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `documentation/js/cytoscape.cjs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 15.635)
- **Top Global Matches:** file_cluster_4: 15.635, file_cluster_12: 17.708, file_cluster_15: 18.775
- **Magnitude:** 28511.84 | **LOC:** 31815 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); blast radius 23.787; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%)
- **Documentation Coverage:** 95.8716% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(I/O & Config Routines)** (Impact: 511.7)
  * `drawNode` **(Many-Argument Workhorses)** (Impact: 314.4)
  * `parseImpl` **(Many-Argument Workhorses)** (Impact: 308.1)
    * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name ...
  * `render` **(Compute Cores)** (Impact: 173.1)
  * `touchmoveHandler` **(Compute Cores)** (Impact: 165.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 3744 instances
* *Concurrency (weighted view):* 159
* *State Mutation (weighted view):* 12184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5782`, `structural_boundaries: 8281`, `args: 1858`, `func_start: 2570`
* *Risk/State:* `safety_bypasses: 486`, `state_mutation: 4696`, `dead_code: 155`, `planned_debt: 10`, `duplicate_logic: 54`, `unreferenced_by_name: 70`
* *Architecture:* `api: 4`, `concurrency: 39`
* *Defense:* `safety: 1171`, `doc: 170`, `test: 367`, `sync_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `documentation/template.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_13: 7.155, file_cluster_10: 8.476, file_cluster_2: 8.647
- **Magnitude:** 2346.1 | **LOC:** 303 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Guard Balance (formerly Safety Score) (56.9%), Complexity Load (formerly Cognitive Load) (28.2%), Connectivity (formerly Api Exposure) (11.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 100`, `args: 47`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `io: 28`, `api: 29`, `concurrency: 2`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.007
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` font-awesome.css, github.css, reset.css, style.css, js.cytoscape.org, classList.min.js, cytoscape-logo.png, cytoscape-logo.svg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/base/load-listeners.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.465)
- **Top Global Matches:** file_cluster_4: 8.465, file_cluster_12: 11.431, file_cluster_6: 12.433
- **Magnitude:** 1903.1 | **LOC:** 2203 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(I/O & Config Routines)** (Impact: 548.0)
  * `mousemoveHandler` **(Compute Cores)** (Impact: 120.8)
  * `mouseupHandler` **(Compute Cores)** (Impact: 85.3)
  * `wheelHandler` **(Compute Cores)** (Impact: 48.1)
  * `mousedownHandler` **(Compute Cores)** (Impact: 40.2)
    * *Intent:* // Primary key
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 231 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 745
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 368`, `args: 88`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 283`, `dead_code: 12`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 48`, `test: 82`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.164
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 3):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/math.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.22)
- **Top Global Matches:** file_cluster_12: 7.22, file_cluster_15: 8.035, file_cluster_4: 8.631
- **Magnitude:** 1452.22 | **LOC:** 1479 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); blast radius 16.097; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `roundRectangleIntersectLine` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `finiteLinesIntersect` **(Many-Argument Workhorses)** (Impact: 53.8)
    * *Intent:* // (x1,y1)=>(x2,y2) intersect with (x3,y3)=>(x4,y4)
  * `polygonIntersectLine` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* // math.polygonIntersectLine( x, y, basePoints, centerX, centerY, width, height, padding ) // inters...
  * `intersectLineCircle` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* // Returns intersections of increasing distance from line's start point
  * `median` **(Many-Argument Workhorses)** (Impact: 33.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 466`, `args: 89`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 251`, `dead_code: 6`
* *Architecture:* `api: 72`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053223
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `src/collection/dimensions/bounds.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.349)
- **Top Global Matches:** file_cluster_6: 7.349, file_cluster_8: 11.908, file_cluster_4: 14.168
- **Magnitude:** 1115.62 | **LOC:** 1045 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.196; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `boundingBoxImpl` **(Many-Argument Workhorses)** (Impact: 134.8)
    * *Intent:* // get the bounding box of the elements (in raw model position)
  * `updateBoundsFromLabel` **(Many-Argument Workhorses)** (Impact: 68.8)
  * `updateCompoundBounds` **(Defensive Guards)** (Impact: 67.9)
  * `update` **(Defensive Guards)** (Impact: 55.3)
  * `computePaddingValues` **(Defensive Guards)** (Impact: 50.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 258`, `args: 33`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 201`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 36`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.011353
  * `Imports (Out-Degree: 5):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-nodes.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.681)
- **Top Global Matches:** file_cluster_6: 6.681, file_cluster_8: 11.986, file_cluster_4: 13.593
- **Magnitude:** 952.28 | **LOC:** 805 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawNode` **(Many-Argument Workhorses)** (Impact: 375.0)
  * `drawOutline` **(I/O & Config Routines)** (Impact: 68.2)
  * `drawPie` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `drawStripe` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `drawBorder` **(I/O & Config Routines)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 171`, `args: 22`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 110`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 5):` is.mjs, math.mjs, round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/layout/cose.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.897)
- **Top Global Matches:** file_cluster_4: 6.897, file_cluster_6: 10.663, file_cluster_12: 11.942
- **Magnitude:** 865.8 | **LOC:** 1341 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (92.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 39.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createLayoutInfo` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* /** * used in the layout process */
  * `findClippingPoint` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /** * the rectangular bounding box of it's source/target node */
  * `run` **(I/O & Config Routines)** (Impact: 28.0)
    * *Intent:* /** */
  * `findLCA_aux` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* /** * * * X is the number of ancestors (max: 2) found in * graphIx (and it's subgraphs), * Y is the ...
  * `nodeRepulsion` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 283`, `args: 40`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 181`, `dead_code: 76`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 30`, `doc: 22`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.179
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.010109
  * `Imports (Out-Degree: 4):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/edge-control-points.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.963)
- **Top Global Matches:** file_cluster_6: 5.963, file_cluster_8: 11.814, file_cluster_4: 13.013
- **Magnitude:** 800.66 | **LOC:** 1058 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.9%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findTaxiPoints` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `findEdgeControlPoints` **(Compute Cores)** (Impact: 92.6)
  * `tryToCorrectInvalidPoints` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `storeAllpts` **(Defensive Guards)** (Impact: 34.9)
  * `findBezierPoints` **(Many-Argument Workhorses)** (Impact: 34.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 389
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 207`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 151`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 49`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.106
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.008192
  * `Imports (Out-Degree: 6):` is.mjs, map.mjs, math.mjs, round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-redraw.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.376)
- **Top Global Matches:** file_cluster_6: 6.376, file_cluster_4: 10.612, file_cluster_8: 15.274
- **Magnitude:** 745.74 | **LOC:** 722 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Compute Cores)** (Impact: 171.7)
  * `createGradientStyleFor` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `drawSelectionRectangle` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `setContextTransform` **(Defensive Guards)** (Impact: 24.5)
  * `matchCanvasSize` **(Defensive Guards)** (Impact: 14.5)
    * *Intent:* // Resize canvas
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 109 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 121`, `args: 19`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 129`, `dead_code: 11`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 26`, `test: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 2):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/style/apply.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.257)
- **Top Global Matches:** file_cluster_6: 9.257, file_cluster_4: 11.74, file_cluster_12: 17.004
- **Magnitude:** 731.7 | **LOC:** 850 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.7%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyParsedProperty` **(Many-Argument Workhorses)** (Impact: 116.8)
    * *Intent:* // // now, this function flattens the property, and here's how: // // for parsedProp:{ bypass: true,...
  * `updateStyleHints` **(Defensive Guards)** (Impact: 46.9)
  * `updateTransitions` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* // diffProps : { name => { prev, next } }
  * `getPropertiesDiff` **(Defensive Guards)** (Impact: 36.0)
  * `applyContextStyle` **(Many-Argument Workhorses)** (Impact: 32.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 237`, `args: 39`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 122`, `dead_code: 4`
* *Architecture:* `api: 4`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 25`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.013022
  * `Imports (Out-Degree: 4):` is.mjs, promise.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/index.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.98)
- **Top Global Matches:** file_cluster_6: 9.98, file_cluster_4: 11.531, file_cluster_12: 16.026
- **Magnitude:** 710.88 | **LOC:** 839 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 2.498; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `restore` **(Many-Argument Workhorses)** (Impact: 103.0)
  * `remove` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `Collection` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* // represents a set of nodes, edges, or both together
  * `json` **(Compute Cores)** (Impact: 45.4)
  * `move` **(Defensive Guards)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 194`, `args: 38`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 119`
* *Architecture:* `api: 9`, `import: 21`
* *Defense:* `safety: 14`, `test: 23`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.498
  * `Choke Point (Betweenness):` 0.004163 | `Ripple Effect (Closeness):` 0.01618
  * `Imports (Out-Degree: 21):` is.mjs, map.mjs, set.mjs, index.mjs, index.mjs, animation.mjs, class.mjs, comparators.mjs...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.252)
- **Top Global Matches:** file_cluster_12: 8.252, file_cluster_7: 8.607, file_cluster_5: 10.268
- **Magnitude:** 646.9 | **LOC:** 1154 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.192; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawNode` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* /** * Draw a node using either a texture or a "simple shape". */
  * `drawTexture` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* /** * Draws a texture using the texture atlas. */
  * `drawEdgeArrow` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* /** * Only supports drawing triangles at the moment. */
  * `drawEdgeLine` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /** * Draw straight-line or bezier curve edges. */
  * `_getAdjustedBB` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* /** * Adjusts a node or label BB to accomodate padding and split for wrapped textures. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 73`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 185`, `planned_debt: 4`
* *Architecture:* `api: 16`, `import: 6`
* *Defense:* `safety: 13`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.192
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.008192
  * `Imports (Out-Degree: 6):` math.mjs, index.mjs, atlas.mjs, shader-sdf.mjs, webgl-util.mjs, gl-matrix
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/coords.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.926)
- **Top Global Matches:** file_cluster_6: 7.926, file_cluster_4: 11.84, file_cluster_8: 15.997
- **Magnitude:** 611.54 | **LOC:** 581 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getAllInBox` **(Many-Argument Workhorses)** (Impact: 185.0)
    * *Intent:* // 'Give me everything from this box'
  * `findNearestElements` **(Many-Argument Workhorses)** (Impact: 150.7)
  * `checkEdge` **(Defensive Guards)** (Impact: 34.9)
  * `addEle` **(Defensive Guards)** (Impact: 27.6)
  * `checkLabel` **(Compute Cores)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 182`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 51`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 31`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008192
  * `Imports (Out-Degree: 2):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/viewport.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.91)
- **Top Global Matches:** file_cluster_6: 8.91, file_cluster_4: 9.179, file_cluster_12: 14.645
- **Magnitude:** 545.36 | **LOC:** 610 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.268; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFitViewport` **(Compute Cores)** (Impact: 44.6)
  * `getZoomedViewport` **(Compute Cores)** (Impact: 31.5)
  * `viewport` **(Compute Cores)** (Impact: 29.5)
  * `zoomRange` **(Defensive Guards)** (Impact: 23.6)
  * `panBy` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 125`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 79`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.268
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.014588
  * `Imports (Out-Degree: 2):` is.mjs, math.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/layered-texture-cache.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.897)
- **Top Global Matches:** file_cluster_4: 7.897, file_cluster_15: 9.003, file_cluster_10: 9.188
- **Magnitude:** 532.44 | **LOC:** 669 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (78.5%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLayers` **(Many-Argument Workhorses)** (Impact: 91.6)
  * `drawEleInLayer` **(Defensive Guards)** (Impact: 18.9)
  * `dequeue` **(Defensive Guards)** (Impact: 18.8)
  * `updateElementsInLayers` **(Compute Cores)** (Impact: 16.9)
  * `validateLayersElesOrdering` **(Defensive Guards)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 176`, `args: 29`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `dead_code: 29`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 14`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 5):` heap.mjs, is.mjs, math.mjs, index.mjs, texture-cache-defs.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/algorithms/k-clustering.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.236)
- **Top Global Matches:** file_cluster_15: 7.236, file_cluster_10: 8.241, file_cluster_9: 8.512
- **Magnitude:** 524.56 | **LOC:** 469 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.057; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kMeans` **(Defensive Guards)** (Impact: 25.4)
  * `kMedoids` **(Defensive Guards)** (Impact: 23.4)
  * `fuzzyCMeans` **(Compute Cores)** (Impact: 19.2)
  * `updateCentroids` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `assign` **(Many-Argument Workhorses)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 146`, `args: 20`, `func_start: 18`
* *Risk/State:* `state_mutation: 116`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 14`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.057
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.011353
  * `Imports (Out-Degree: 2):` index.mjs, clustering-distances.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/coord-ele-math/labels.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.924)
- **Top Global Matches:** file_cluster_6: 5.924, file_cluster_4: 11.303, file_cluster_8: 14.167
- **Magnitude:** 477.94 | **LOC:** 566 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.534; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%), Guard Balance (formerly Safety Score) (69.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLabelText` **(Many-Argument Workhorses)** (Impact: 58.1)
  * `recalculateEdgeLabelProjections` **(Compute Cores)** (Impact: 56.8)
  * `calculateEndProjection` **(Compute Cores)** (Impact: 36.9)
  * `recalculateNodeLabelProjection` **(Compute Cores)** (Impact: 16.6)
  * `calculateLabelAngle` **(Defensive Guards)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 185`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 79`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.534
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.008597
  * `Imports (Out-Degree: 4):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/style/parse.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.199)
- **Top Global Matches:** file_cluster_8: 9.199, file_cluster_6: 11.282, file_cluster_4: 19.273
- **Magnitude:** 473.04 | **LOC:** 436 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.225; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseImpl` **(Many-Argument Workhorses)** (Impact: 309.3)
    * *Intent:* // parse a property; return null on invalid; return parsed property otherwise // fields : // - name ...
  * `parse` **(Defensive Guards)** (Impact: 28.4)
    * *Intent:* // a caching layer for property parsing
  * `parseImplWarn` **(Defensive Guards)** (Impact: 16.3)
  * `checkEnums` **(Callbacks & Closures)** (Impact: 3.8)
    * *Intent:* // several types also allow enums
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 94`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 36`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.013022
  * `Imports (Out-Degree: 5):` is.mjs, math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests-examples/demo-todo-app.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_10: 6.263, file_cluster_15: 9.204, file_cluster_13: 9.835
- **Magnitude:** 463.58 | **LOC:** 450 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.007; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (90.4%), Mutation Surface (formerly State Flux) (59.9%), Debt Markers (formerly Tech Debt) (59.1%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createDefaultTodos` **(Parameter Forwarders)** (Impact: 3.3)
  * `checkNumberOfTodosInLocalStorage` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** */
  * `checkNumberOfCompletedTodosInLocalStorage` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** */
  * `checkTodosInLocalStorage` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 47 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 426
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 207`, `args: 50`, `func_start: 4`
* *Risk/State:* `state_mutation: 14`, `planned_debt: 18`
* *Architecture:* `io: 3`, `concurrency: 191`, `import: 1`
* *Defense:* `safety: 2`, `doc: 3`, `test: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.007
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extensions/renderer/canvas/ele-texture-cache.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.818)
- **Top Global Matches:** file_cluster_4: 7.818, file_cluster_10: 7.896, file_cluster_15: 8.154
- **Magnitude:** 456.82 | **LOC:** 556 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.27; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getElement` **(Many-Argument Workhorses)** (Impact: 136.4)
  * `invalidateElement` **(Compute Cores)** (Impact: 10.4)
  * `shouldRedraw` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `dequeue` **(Compute Cores)** (Impact: 8.7)
  * `removeFromQueue` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 129`, `args: 26`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 83`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.27
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.009465
  * `Imports (Out-Degree: 6):` heap.mjs, math.mjs, index.mjs, ele-texture-cache-lookup.mjs, texture-cache-defs.mjs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-label-text.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.018)
- **Top Global Matches:** file_cluster_8: 8.018, file_cluster_6: 9.68, file_cluster_4: 17.953
- **Magnitude:** 456.18 | **LOC:** 403 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawText` **(Many-Argument Workhorses)** (Impact: 192.4)
  * `drawElementText` **(Many-Argument Workhorses)** (Impact: 61.4)
  * `getTextAngle` **(Defensive Guards)** (Impact: 13.0)
  * `getFontCache` **(Defensive Guards)** (Impact: 6.7)
  * `eleTextBiggerThanMin` **(Compute Cores)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 98`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 54`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 2):` math.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/base/node-shapes.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.303)
- **Top Global Matches:** file_cluster_10: 7.303, file_cluster_15: 7.412, file_cluster_16: 8.688
- **Magnitude:** 436.44 | **LOC:** 659 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkPoint` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `checkPoint` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `checkPoint` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `generateBarrel` **(Callbacks & Closures)** (Impact: 22.4)
  * `checkPoint` **(Many-Argument Workhorses)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 137`, `args: 37`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.164
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 2):` math.mjs, round.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extensions/renderer/canvas/drawing-edges.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.663)
- **Top Global Matches:** file_cluster_6: 8.663, file_cluster_8: 9.78, file_cluster_4: 16.432
- **Magnitude:** 423.3 | **LOC:** 432 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawArrowShape` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `drawEdgePath` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `drawEdge` **(Many-Argument Workhorses)** (Impact: 59.7)
  * `drawArrowhead` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `drawEdgeOverlayUnderlay` **(Defensive Guards)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 96`, `args: 14`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 46`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.009011
  * `Imports (Out-Degree: 3):` round.mjs, index.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/collection/algorithms/affinity-propagation.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.399)
- **Top Global Matches:** file_cluster_4: 6.399, file_cluster_6: 9.353, file_cluster_12: 12.515
- **Magnitude:** 396.64 | **LOC:** 330 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.057; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `affinityPropagation` **(Compute Cores)** (Impact: 58.3)
  * `getPreference` **(Defensive Guards)** (Impact: 16.4)
  * `assign` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `assignClusters` **(Compute Cores)** (Impact: 13.3)
  * `setOptions` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 104`, `args: 14`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 87`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 11`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.057
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.011353
  * `Imports (Out-Degree: 4):` is.mjs, math.mjs, index.mjs, clustering-distances.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/extensions/renderer/base/node-shapes.mjs` (JAVASCRIPT) | Magnitude: 436.44 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 477, structural_boundaries: 137, core_var_decl: 98, design_camel_case: 52
- `src/extensions/renderer/base/coord-ele-math/index.mjs` (JAVASCRIPT) | Magnitude: 16.5 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, import: 10, indent_spaces: 10, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/collection-style.mjs` (JAVASCRIPT) | Magnitude: 125.82 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1012, test: 496, args: 180, closures: 179

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 16.22 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, import: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/collection/algorithms/index.mjs` (JAVASCRIPT) | Magnitude: 16.86 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, import: 19, indent_spaces: 19, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/extensions/layout/index.mjs` (JAVASCRIPT) | Magnitude: 16.36 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, import: 8, indent_spaces: 8, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/extensions/renderer/canvas/ele-texture-cache.mjs` (JAVASCRIPT) | Magnitude: 456.82 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 129, core_var_decl: 124, branch: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/extensions/renderer/canvas/webgl/shader-sdf.mjs` (JAVASCRIPT) | Magnitude: 24.74 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, core_var_decl: 15, design_snake_case: 11, design_short_vars: 11

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/extensions/renderer/canvas/webgl/drawing-elements-webgl.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 646.9
- `src/extensions/renderer/canvas/webgl/webgl-util.mjs` -> **Mike Kucera** (100.0% isolated ownership) | Magnitude: 250.14

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/index.mjs` -> **Severity: 1.232** (Bridge: 0.0123 * Flux: 99.9849%)
- `src/test.mjs` -> **Severity: 1.066** (Bridge: 0.0116 * Flux: 91.6827%)
- `src/extension.mjs` -> **Severity: 0.638** (Bridge: 0.0064 * Flux: 99.9994%)
- `src/core/index.mjs` -> **Severity: 0.417** (Bridge: 0.0042 * Flux: 99.9889%)
- `src/collection/index.mjs` -> **Severity: 0.416** (Bridge: 0.0042 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util/index.mjs` -> **Severity: 8.624** (Embedded: 0.1318 * Error Risk: 65.4502%)
- `src/util/maps.mjs` -> **Severity: 6.093** (Embedded: 0.0825 * Error Risk: 73.8699%)
- `src/util/hash.mjs` -> **Severity: 5.527** (Embedded: 0.0846 * Error Risk: 65.3091%)
- `src/util/colors.mjs` -> **Severity: 5.22** (Embedded: 0.0827 * Error Risk: 63.1059%)
- `src/util/extend.mjs` -> **Severity: 5.039** (Embedded: 0.0832 * Error Risk: 60.5532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/util/index.mjs` -> **Severity: 4466.8** (Blast Radius: 44.668 * Doc Risk: 100.0%)
- `src/is.mjs` -> **Severity: 4129.1** (Blast Radius: 41.291 * Doc Risk: 100.0%)
- `src/index.mjs` -> **Severity: 2454.5** (Blast Radius: 24.545 * Doc Risk: 100.0%)
- `documentation/js/cytoscape.cjs.js` -> **Severity: 2280.498** (Blast Radius: 23.787 * Doc Risk: 95.8716%)
- `src/math.mjs` -> **Severity: 1609.7** (Blast Radius: 16.097 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 74 literal sites + 48 sites through wrappers = 122

- `error` (function, panics_and_aborts, primitive): 23 call sites in 1 files -- `documentation/js/cytoscape.cjs.js`
- `error` (function, panics_and_aborts, primitive): 23 call sites in 1 files -- `documentation/js/cytoscape.umd.js`
- `_nonIterableRest` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `documentation/js/cytoscape.cjs.js`
- `_nonIterableRest` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `documentation/js/cytoscape.umd.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14209 call pairs -- scoped 23.8%, unique 0.0%, ambiguous 5.0%, external 71.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 14201 | 23.8% | 0.0% | 5.0% | 71.2% |
| shell | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
