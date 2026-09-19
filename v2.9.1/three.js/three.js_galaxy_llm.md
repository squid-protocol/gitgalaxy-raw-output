# ARCHITECTURAL_BRIEF: three.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mrdoob/three.js.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2737 analyzed artifact(s), 447793 LOC.
- **Load-bearing artifact:** `manual/resources/lang.css` -- 269 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/jsm/Addons.js` -- pulls in 257 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `examples/jsm/libs/lottie_canvas.module.js` at magnitude 17620.3 (structural weight, not risk).
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
| Total Artifacts | 5861 |
| Analyzed Artifacts (Scanned) | 2737 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3124 |
| Total LOC | 447793 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 46.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7301 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2903 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2089 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 109 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 1513 | 244316 | 55.3% |
| HTML | 1017 | 198387 | 37.2% |
| XML | 76 | 19 | 2.8% |
| PLAINTEXT | 39 | 6 | 1.4% |
| MARKDOWN | 28 | 0 | 1.0% |
| JSON | 27 | 2207 | 1.0% |
| CSS | 20 | 2841 | 0.7% |
| BINARY_THREAT | 17 | 17 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.232`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.23; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 16%, Large Core Modules (3) 11%, Large Core Modules (2) 6%, Parameter Forwarders Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2622 | 95.8% |
| Unknown | 23 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 61 | 2.2% |
| Static: Minified & Vendor Opaque Mass | 31 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3124*

**Composition by Extension & Reason:**
- `.jpg`: 821x Excluded (Explicitly Denied Extension: '.jpg'), 7x Excluded (Explicitly Denied Extension: '.JPG')
- `.html`: 779x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 30 exceeds 500 chars), 3x Excluded (Saturation: Line 44 exceeds 500 chars)
- `.md`: 775x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 204x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.js`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Excluded (Saturation: Line 1 exceeds 500 chars), 3x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.glb`: 45x Excluded (Unsupported Extension: '.glb')
- `.mtlx`: 20x Excluded (Unsupported Extension: '.mtlx')
- `.ktx2`: 19x Excluded (Unsupported Extension: '.ktx2')
- `.pdb`: 18x Excluded (Unsupported Extension: '.pdb')
- `.hdr`: 18x Excluded (Unsupported Extension: '.hdr')
- `.gltf`: 16x Excluded (Explicitly Denied Extension: '.gltf')
- `.mpd`: 16x Excluded (Unsupported Extension: '.mpd')
- `.wrl`: 15x Excluded (Unsupported Extension: '.wrl')
- `.tmpl`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md2`: 14x Excluded (Unsupported Extension: '.md2')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 26.3 | 18.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 63.1 | 73.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.9 | 6.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.8 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.6 | 22.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 224 | 85 | 0 | `examples/jsm/controls/ArcballControls.js` |
| cleanup | 1036 | 344 | 1 | `src/renderers/common/Renderer.js` |
| guards | 15274 | 1637 | 9 | `examples/jsm/libs/lottie_canvas.module.js` |
| danger | 5801 | 912 | 4 | `editor/js/libs/codemirror/codemirror.js` |
| concurrency | 2214 | 508 | 2 | `examples/jsm/loaders/GLTFLoader.js` |
| connectivity | 12171 | 2493 | 7 | `src/Three.TSL.js` |
| io | 16713 | 906 | 9 | `manual/ko/fundamentals.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 78 | 19 | 0 | `examples/jsm/libs/lottie_canvas.module.js` |
| time | 380 | 206 | 0 | `editor/js/libs/codemirror/codemirror.js` |
| serialization | 151 | 50 | 0 | `test/unit/src/math/Interpolant.tests.js` |
| regex | 793 | 148 | 0 | `editor/js/libs/esprima.js` |
| events | 4879 | 1196 | 5 | `editor/js/libs/tern-threejs/threejs.js` |
| tests | 4223 | 215 | 0 | `test/unit/src/math/Vector3.tests.js` |
| docs | 11359 | 1927 | 10 | `examples/jsm/libs/opentype.module.js` |
| debt | 1666 | 430 | 1 | `examples/jsm/libs/opentype.module.js` |
| mutation | 183995 | 2443 | 140 | `examples/jsm/libs/lottie_canvas.module.js` |
| dead_code | 890 | 246 | 0 | `examples/jsm/loaders/TDSLoader.js` |
| credential | 49 | 26 | 0 | `examples/jsm/libs/opentype.module.js` |
| threat | 3962 | 575 | 2 | `examples/jsm/libs/lottie_canvas.module.js` |
| ml_ai | 1106 | 428 | 1 | `examples/webgl_multiple_elements_text.html` |
| ui | 3147 | 851 | 4 | `files/main.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `manual/ko/fundamentals.html` (Hits: 193)
- `manual/en/game.html` (Hits: 167)
- `manual/fr/game.html` (Hits: 161)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lang.css** (`manual/resources/lang.css`) — 269 inbound connections
2. **lesson.css** (`manual/resources/lesson.css`) — 269 inbound connections
3. **lesson.js** (`manual/resources/lesson.js`) — 269 inbound connections
4. **prettify.js** (`manual/resources/prettify.js`) — 269 inbound connections
5. **TSLBase.js** (`src/nodes/tsl/TSLBase.js`) — 120 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Addons.js** (`examples/jsm/Addons.js`) — 257 outbound dependencies
2. **Three.Core.js** (`src/Three.Core.js`) — 161 outbound dependencies
3. **TSL.js** (`src/nodes/TSL.js`) — 136 outbound dependencies
4. **ShaderChunk.js** (`src/renderers/shaders/ShaderChunk.js`) — 124 outbound dependencies
5. **ObjectLoader.js** (`src/loaders/ObjectLoader.js`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dispatchKey` **(Many-Argument Workhorses)** (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **1193.6** | LOC: 1377
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **857.4** | LOC: 2565
  * *Intent:* /** * Parses the given VRML data and returns the resulting scene. * */
- `createVisitor` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **763.7** | LOC: 2659
- `constructor` **(Many-Argument Workhorses)** (@ `src/renderers/WebGLRenderer.js`) -> Impact: **637.8** | LOC: 2545
  * *Intent:* /** * Constructs a new WebGL renderer. * */
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/SVGLoader.js`) -> Impact: **511.2** | LOC: 1852
  * *Intent:* /** * Parses the given SVG data and returns the resulting data. * * SVG XML document. */
- `WebGLProgram` **(Many-Argument Workhorses)** (@ `src/renderers/webgl/WebGLProgram.js`) -> Impact: **455.6** | LOC: 615
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/EXRLoader.js`) -> Impact: **441.6** | LOC: 2213
  * *Intent:* /** * Parses the given EXR texture data. * */
- `WebGLPrograms` **(Many-Argument Workhorses)** (@ `src/renderers/webgl/WebGLPrograms.js`) -> Impact: **432.3** | LOC: 655
- `sourceDecorator` **(Many-Argument Workhorses)** (@ `manual/resources/prettify.js`) -> Impact: **396.1** | LOC: 908
  * *Intent:* * * This code treats ", ', and ` as string delimiters, and \ as a string * escape. It does not recognize perl's qq() style strings. * It has no specia...
- `setProgram` **(Many-Argument Workhorses)** (@ `src/renderers/WebGLRenderer.js`) -> Impact: **374.1** | LOC: 428

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples` | 574 | 46774.09 | 41.83% | 0.0% |
| `examples/jsm/libs` | 11 | 34601.66 | 64.32% | 0.0% |
| `examples/jsm/loaders` | 48 | 32297.94 | 52.88% | 0.0% |
| `manual/examples/resources/data/gpw` | 7 | 30001.0 | 0.0% | 0.0% |
| `manual/examples` | 177 | 14303.04 | 38.43% | 0.0% |
| `manual/en` | 57 | 13346.19 | 0.17% | 3.06% |
| `editor/js/libs/codemirror` | 2 | 13114.97 | 51.69% | 5.08% |
| `manual/fr` | 47 | 8243.71 | 0.1% | 1.88% |
| `manual/zh` | 54 | 7767.78 | 0.18% | 2.59% |
| `editor/js` | 72 | 7499.56 | 45.13% | 0.95% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/renderers/common/nodes/NodeUniform.js` -> **100.0%** Exposure
- `editor/js/libs/ui.js` -> **99.8495%** Exposure
- `src/renderers/common/nodes/NodeBuilderState.js` -> **99.3307%** Exposure
- `src/nodes/gpgpu/WorkgroupInfoNode.js` -> **79.888%** Exposure
- `src/loaders/Loader.js` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `editor/js/Animation.js` -> **100.0%** Exposure
- `editor/js/AnimationResizer.js` -> **100.0%** Exposure
- `editor/js/Editor.js` -> **100.0%** Exposure
- `editor/js/EditorControls.js` -> **100.0%** Exposure
- `editor/js/History.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `editor/js/libs/ui.js` -> **0** Orphaned Functions | **25** Duplicates
- `src/renderers/common/nodes/NodeUniform.js` -> **0** Orphaned Functions | **24** Duplicates
- `examples/jsm/libs/tween.module.js` -> **23** Orphaned Functions | **0** Duplicates
- `examples/jsm/libs/lottie_canvas.module.js` -> **0** Orphaned Functions | **21** Duplicates
- `examples/jsm/libs/ecsy.module.js` -> **14** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `53` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1533` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `examples/jsm/libs/lottie_canvas.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 17620.3 | **LOC:** 14850 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.334; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (96.0%), Connectivity (formerly Api Exposure) (42.1%), Concurrency Surface (formerly Concurrency) (15.2%)
- **Documentation Coverage:** 98.7903% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMeasures` **(Many-Argument Workhorses)** (Impact: 307.4)
  * `workerStart` **(Defensive Guards)** (Impact: 202.7)
  * `setupWorker` **(I/O & Config Routines)** (Impact: 156.6)
  * `initiateExpression` **(Many-Argument Workhorses)** (Impact: 149.4)
  * `dataFunctionManager` **(I/O & Config Routines)** (Impact: 127.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 2758 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 9313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3178`, `structural_boundaries: 2639`, `args: 957`, `func_start: 867`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 3797`, `dead_code: 17`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 21`
* *Architecture:* `io: 12`, `api: 34`, `concurrency: 22`
* *Defense:* `safety: 875`, `doc: 13`, `sync_locks: 10`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.334
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000487
  * `Imports (Out-Degree: 0):` howler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 13114.46 | **LOC:** 9850 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (98.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchKey` **(Many-Argument Workhorses)** (Impact: 1193.6)
  * `insertLineContent` **(Compute Cores)** (Impact: 119.7)
    * *Intent:* // Outputs a number of spans to make up a line, taking highlighting // and marked text into account.
  * `drawSelectionRange` **(Compute Cores)** (Impact: 116.5)
    * *Intent:* // Draws the given range as a highlighted selection
  * `markText` **(Many-Argument Workhorses)** (Impact: 113.7)
    * *Intent:* // Create a marker, wire it up to the right lines, and
  * `buildToken` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* // Build up the DOM representation for a single token, and add it to // the line map. Takes care to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 1770 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 5601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3424`, `structural_boundaries: 2362`, `args: 968`, `func_start: 735`
* *Risk/State:* `safety_bypasses: 802`, `state_mutation: 2061`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 16`
* *Architecture:* `api: 42`, `concurrency: 31`
* *Defense:* `safety: 115`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000365
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/opentype.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 11001.36 | **LOC:** 14507 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.334; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.9%), Connectivity (formerly Api Exposure) (58.8%), Complexity Load (formerly Cognitive Load) (58.4%), Concurrency Surface (formerly Concurrency) (12.4%)
- **Documentation Coverage:** 56.172% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseCFFCharstring` **(Many-Argument Workhorses)** (Impact: 182.9)
    * *Intent:* // Take in charstring code and return a Glyph object. // The encoding is described in the Type 2 Cha...
  * `parse` **(Compute Cores)** (Impact: 125.4)
  * `parseBuffer` **(Many-Argument Workhorses)** (Impact: 100.6)
    * *Intent:* // Public API /////////////////////////////////////////////////////////// /** * Parse the OpenType f...
  * `parseGlyph` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* // Parse a TrueType glyph.
  * `getPath` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* /** * Convert the glyph to a Path we can draw on a drawing context. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1810 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 6060
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1751`, `structural_boundaries: 2599`, `args: 697`, `func_start: 635`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 2440`, `dead_code: 9`, `planned_debt: 27`, `fragile_debt: 5`
* *Architecture:* `io: 1`, `api: 140`, `concurrency: 1`
* *Defense:* `safety: 448`, `doc: 285`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.334
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000487
  * `Imports (Out-Degree: 0):` glyf
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `editor/js/libs/esprima.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5932.78 | **LOC:** 6401 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (86.5%), Connectivity (formerly Api Exposure) (62.2%)
- **Documentation Coverage:** 98.4756% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isKeyword` **(Defensive Guards)** (Impact: 66.4)
    * *Intent:* ; // ECMA-262 11.6.2.1 Keywords
  * `parseForStatement` **(I/O & Config Routines)** (Impact: 57.3)
    * *Intent:* // ECMA-262 13.7.4 The for Statement // ECMA-262 13.7.5 The for-in and for-of Statements
  * `scanPunctuator` **(Defensive Guards)** (Impact: 57.0)
    * *Intent:* ; // ECMA-262 11.7 Punctuators
  * `parseClassElement` **(Defensive Guards)** (Impact: 50.7)
    * *Intent:* // ECMA-262 14.5 Class Definitions
  * `parseObjectProperty` **(Defensive Guards)** (Impact: 45.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 903 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1444`, `structural_boundaries: 1305`, `args: 407`, `func_start: 298`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 8`, `state_mutation: 1472`, `dead_code: 9`
* *Architecture:* `api: 119`, `concurrency: 2`
* *Defense:* `safety: 499`, `doc: 65`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000365
  * `Imports (Out-Degree: 0):` foo
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/VRMLLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3784.14 | **LOC:** 3647 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.186; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.6%), Complexity Load (formerly Cognitive Load) (91.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.7%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 91.0714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 857.4)
    * *Intent:* /** * Parses the given VRML data and returns the resulting scene. * */
  * `createVisitor` **(Many-Argument Workhorses)** (Impact: 763.7)
  * `processField` **(Many-Argument Workhorses)** (Impact: 298.3)
  * `buildIndexedFaceSetNode` **(Compute Cores)** (Impact: 80.9)
  * `buildElevationGridNode` **(Compute Cores)** (Impact: 77.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 357 instances
* *State Mutation (weighted view):* 1102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 493`, `structural_boundaries: 365`, `args: 100`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `state_mutation: 388`, `dead_code: 22`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 80`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00073
  * `Imports (Out-Degree: 0):` chevrotain.module.min.js, three, VRMLLoader.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/usd/USDComposer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3284.86 | **LOC:** 4595 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 48.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.26; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.7%), Guard Balance (formerly Safety Score) (83.2%), Complexity Load (formerly Cognitive Load) (72.0%), Connectivity (formerly Api Exposure) (29.7%)
- **Documentation Coverage:** 63.0137% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_buildGeometryWithSubsets` **(Many-Argument Workhorses)** (Impact: 184.6)
  * `applyTransform` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /** * Apply USD transforms to a Three.js object. * Handles xformOpOrder with proper matrix compositi...
  * `_buildGeometry` **(Many-Argument Workhorses)** (Impact: 111.2)
  * `_buildHierarchy` **(Many-Argument Workhorses)** (Impact: 95.6)
    * *Intent:* /** * Build the scene hierarchy recursively. * Uses childrenByPath index for O(1) child lookup inste...
  * `applyTexture` **(Many-Argument Workhorses)** (Impact: 91.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 387 instances
* *State Mutation (weighted view):* 1202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 881`, `structural_boundaries: 282`, `args: 84`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `state_mutation: 428`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 257`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001015
  * `Imports (Out-Degree: 0):` three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/fflate.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3192.76 | **LOC:** 2673 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); blast radius 1.829; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Connectivity (formerly Api Exposure) (73.8%), Complexity Load (formerly Cognitive Load) (67.9%), Concurrency Surface (formerly Concurrency) (59.2%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflt` **(Many-Argument Workhorses)** (Impact: 138.7)
    * *Intent:* // expands raw DEFLATE data
  * `dflt` **(Many-Argument Workhorses)** (Impact: 104.2)
    * *Intent:* // compresses data into a raw DEFLATE buffer
  * `push` **(Compute Cores)** (Impact: 89.2)
    * *Intent:* /** * Pushes a chunk to be unzipped */
  * `wblk` **(Many-Argument Workhorses)** (Impact: 69.1)
    * *Intent:* // writes a block
  * `unzip` **(Many-Argument Workhorses)** (Impact: 60.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 449 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 1432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 662`, `args: 238`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 534`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 48`, `concurrency: 15`
* *Defense:* `safety: 33`, `doc: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005582
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/EXRLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3102.18 | **LOC:** 3434 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 0.424; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.8%), Complexity Load (formerly Cognitive Load) (87.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Connectivity (formerly Api Exposure) (29.2%)
- **Documentation Coverage:** 88.5057% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 441.6)
    * *Intent:* /** * Parses the given EXR texture data. * */
  * `setupDecoder` **(Many-Argument Workhorses)** (Impact: 240.4)
  * `parseValue` **(Many-Argument Workhorses)** (Impact: 89.3)
  * `lossyDctDecode` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `uncompressB44` **(Compute Cores)** (Impact: 55.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 423 instances
* *State Mutation (weighted view):* 1445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 290`, `args: 80`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 599`, `dead_code: 3`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 52`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.424
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003034
  * `Imports (Out-Degree: 1):` fflate.module.js, three, EXRLoader.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/SVGLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2948.88 | **LOC:** 3268 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.186; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (92.7%), Complexity Load (formerly Cognitive Load) (87.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.9%), Connectivity (formerly Api Exposure) (29.3%)
- **Documentation Coverage:** 73.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 511.2)
    * *Intent:* /** * Parses the given SVG data and returns the resulting data. * * SVG XML document. */
  * `pointsToStrokeWithBuffers` **(Many-Argument Workhorses)** (Impact: 313.6)
    * *Intent:* /** * Creates a stroke from an array of points. * */
  * `parsePathNode` **(Many-Argument Workhorses)** (Impact: 146.9)
  * `createShapes` **(Compute Cores)** (Impact: 122.4)
    * *Intent:* /** * Creates from the given shape path and array of shapes. * */
  * `parseFloats` **(Many-Argument Workhorses)** (Impact: 96.2)
    * *Intent:* // from https://github.com/ppvg/svg-numbers (MIT License)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 328 instances
* *State Mutation (weighted view):* 1013
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 233`, `args: 71`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 357`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `safety: 130`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00073
  * `Imports (Out-Degree: 0):` three, SVGLoader.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/renderers/WebGLRenderer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2928.16 | **LOC:** 3639 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.207; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.5%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 28.972% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 637.8)
    * *Intent:* /** * Constructs a new WebGL renderer. * */
  * `setProgram` **(Many-Argument Workhorses)** (Impact: 374.1)
  * `copyTextureToTexture` **(Many-Argument Workhorses)** (Impact: 141.4)
    * *Intent:* /** * Copies data of the given source texture into a destination texture. * * When using render targ...
  * `renderBufferDirect` **(Many-Argument Workhorses)** (Impact: 108.5)
    * *Intent:* // Buffer rendering
  * `render` **(Many-Argument Workhorses)** (Impact: 94.2)
    * *Intent:* /** * Renders the given scene (or other type of 3D object) using the given camera. * * or to the can...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 233 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 844
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 153`, `args: 83`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 378`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 31`, `concurrency: 5`, `import: 37`
* *Defense:* `safety: 204`, `doc: 78`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000487
  * `Imports (Out-Degree: 33):` constants.js, Color.js, ColorManagement.js, Frustum.js, Matrix4.js, Vector3.js, Vector4.js, utils.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/GLTFLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2910.26 | **LOC:** 4861 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 0.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Complexity Load (formerly Cognitive Load) (68.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.4%)
- **Documentation Coverage:** 55.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * Parses the given glTF data and returns the resulting group. * */
  * `_createAnimationTracks` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `loadMaterial` **(Defensive Guards)** (Impact: 50.1)
    * *Intent:* /** * Specification: https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#ma...
  * `loadMesh` **(Defensive Guards)** (Impact: 49.5)
    * *Intent:* /** * Specification: https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#me...
  * `getDependency` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* /** * Requests the specified dependency asynchronously, with caching. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 61 instances
* *Amplified Cascading Flux:* 331 instances
* *Concurrency (weighted view):* 400
* *State Mutation (weighted view):* 1091
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 578`, `structural_boundaries: 344`, `args: 207`, `func_start: 129`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 429`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 9`, `concurrency: 95`, `import: 3`
* *Defense:* `safety: 247`, `doc: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.003287
  * `Imports (Out-Degree: 2):` BufferGeometryUtils.js, SkeletonUtils.js, three, GLTFLoader.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/FBXLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2799.52 | **LOC:** 4463 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.5%), Complexity Load (formerly Cognitive Load) (71.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.4%), Connectivity (formerly Api Exposure) (14.9%)
- **Documentation Coverage:** 97.3451% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseParameters` **(Many-Argument Workhorses)** (Impact: 106.8)
    * *Intent:* // Parse FBX material and return parameters suitable for a three.js material // Also parse the textu...
  * `parseSubNode` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `genFace` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* // Generate data for a single face in a geometry. If the face is a quad then split it into 2 tris
  * `parseProperty` **(Compute Cores)** (Impact: 50.2)
  * `createLight` **(Defensive Guards)** (Impact: 38.6)
    * *Intent:* // Create a DirectionalLight, PointLight or SpotLight
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 416 instances
* *State Mutation (weighted view):* 1343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 605`, `structural_boundaries: 296`, `args: 163`, `func_start: 112`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 511`, `dead_code: 14`, `planned_debt: 5`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 216`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00073
  * `Imports (Out-Degree: 2):` NURBSCurve.js, fflate.module.js, three, FBXLoader.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/exporters/GLTFExporter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2671.72 | **LOC:** 3739 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.205; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Complexity Load (formerly Cognitive Load) (68.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.0%)
- **Documentation Coverage:** 36.7816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processMeshAsync` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* /** * Process mesh */
  * `processBufferView` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* /** * Process and generate a BufferView */
  * `processImage` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* /** * Process image */
  * `processAccessor` **(Many-Argument Workhorses)** (Impact: 55.9)
    * *Intent:* /** * Process attribute to generate an accessor */
  * `processMaterialAsync` **(Compute Cores)** (Impact: 46.7)
    * *Intent:* /** * Process material */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 372 instances
* *Concurrency (weighted view):* 318
* *State Mutation (weighted view):* 1208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 234`, `args: 109`, `func_start: 82`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 464`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 6`, `concurrency: 78`, `import: 1`
* *Defense:* `safety: 174`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000822
  * `Imports (Out-Degree: 0):` three, GLTFExporter.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `editor/js/libs/ternjs/infer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2095.54 | **LOC:** 1636 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 0.506; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `similarType` **(Compute Cores)** (Impact: 55.5)
  * `canonicalType` **(Defensive Guards)** (Impact: 42.6)
  * `maybeTagAsGeneric` **(Defensive Guards)** (Impact: 28.8)
  * `makePredicate` **(Defensive Guards)** (Impact: 26.6)
  * `addType` **(Defensive Guards)** (Impact: 23.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 239 instances
* *State Mutation (weighted view):* 771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 515`, `args: 233`, `func_start: 195`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 293`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 52`, `import: 5`
* *Defense:* `safety: 54`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.506
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001461
  * `Imports (Out-Degree: 2):` def, signal, acorn, acorn_loose, walk
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/collada/ColladaComposer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2050.82 | **LOC:** 3045 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.255; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (91.3%), Complexity Load (formerly Cognitive Load) (73.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.6%), Connectivity (formerly Api Exposure) (25.4%)
- **Documentation Coverage:** 97.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildMaterial` **(Compute Cores)** (Impact: 109.4)
  * `buildGeometryType` **(Many-Argument Workhorses)** (Impact: 94.0)
  * `buildGeometryData` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `setJointValue` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `buildObjects` **(Many-Argument Workhorses)** (Impact: 39.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 871
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 255`, `args: 84`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 321`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 99`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.255
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000835
  * `Imports (Out-Degree: 1):` ColladaParser.js, three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/LDrawLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1801.04 | **LOC:** 2519 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.186; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.2%), Concurrency Surface (formerly Concurrency) (94.6%), Complexity Load (formerly Cognitive Load) (85.3%), Connectivity (formerly Api Exposure) (34.9%)
- **Documentation Coverage:** 65.625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 122.0)
  * `getLocalMaterial` **(Many-Argument Workhorses)** (Impact: 103.3)
  * `createObject` **(Many-Argument Workhorses)** (Impact: 92.6)
  * `smoothNormals` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `parseColorMetaDirective` **(Compute Cores)** (Impact: 77.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 245 instances
* *Concurrency (weighted view):* 85
* *State Mutation (weighted view):* 822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 230`, `args: 72`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `state_mutation: 332`, `dead_code: 7`
* *Architecture:* `api: 10`, `concurrency: 25`, `import: 1`
* *Defense:* `safety: 67`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00073
  * `Imports (Out-Degree: 0):` three, LDrawLoader.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/renderers/common/Renderer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1626.34 | **LOC:** 3681 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 44.1%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **37**; blast radius 0.26; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (98.8%), Guard Balance (formerly Safety Score) (82.8%)
- **Documentation Coverage:** 6.962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_renderScene` **(Many-Argument Workhorses)** (Impact: 115.3)
    * *Intent:* /** * Renders the scene or 3D object with the given camera. * */
  * `_projectObject` **(Many-Argument Workhorses)** (Impact: 99.3)
    * *Intent:* /** * Analyzes the given 3D object's hierarchy and builds render lists from the * processed hierarch...
  * `renderObject` **(Many-Argument Workhorses)** (Impact: 87.0)
    * *Intent:* /** * This method represents the default render object function that manages the render lifecycle * ...
  * `compileAsync` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* * Compiles all materials in the given scene. This can be useful to avoid a * phenomenon which is cal...
  * `_getShadowNodes` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* /** * Retrieves shadow nodes for the given material. This is used to setup shadow passes. * The resu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 156 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 634
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 175`, `args: 110`, `func_start: 106`, `class_start: 1`
* *Risk/State:* `state_mutation: 322`, `planned_debt: 3`
* *Architecture:* `api: 53`, `concurrency: 47`, `import: 37`
* *Defense:* `safety: 129`, `doc: 178`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.001096
  * `Imports (Out-Degree: 33):` constants.js, RenderTarget.js, NodeMaterial.js, ColorManagement.js, Frustum.js, FrustumArray.js, Matrix4.js, Vector2.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/controls/ArcballControls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1592.86 | **LOC:** 3540 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.181; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.4%), Complexity Load (formerly Cognitive Load) (41.8%), Connectivity (formerly Api Exposure) (34.6%), Concurrency Surface (formerly Concurrency) (30.3%)
- **Documentation Coverage:** 33.7349% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onSinglePanMove` **(Many-Argument Workhorses)** (Impact: 65.1)
  * `onWheel` **(Compute Cores)** (Impact: 55.7)
  * `onPointerUp` **(Compute Cores)** (Impact: 40.3)
  * `onSinglePanStart` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `setMouseAction` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /** * Set a new mouse action by specifying the operation to be performed and a mouse/key combination...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 201 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 757
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 127`, `args: 78`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 355`, `dead_code: 4`
* *Architecture:* `api: 11`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 4`, `doc: 72`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000365
  * `Imports (Out-Degree: 0):` three, ArcballControls.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/3DMLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1494.62 | **LOC:** 1837 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Complexity Load (formerly Cognitive Load) (84.0%), Connectivity (formerly Api Exposure) (27.1%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Rhino3dmWorker` **(I/O & Config Routines)** (Impact: 118.1)
    * *Intent:* /* WEB WORKER */
  * `_createMaterial` **(Many-Argument Workhorses)** (Impact: 72.0)
  * `extractObjectData` **(Many-Argument Workhorses)** (Impact: 62.3)
  * `_createObject` **(Many-Argument Workhorses)** (Impact: 59.8)
  * `decodeObjects` **(Many-Argument Workhorses)** (Impact: 42.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 230 instances
* *Concurrency (weighted view):* 150
* *State Mutation (weighted view):* 777
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 170`, `args: 46`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 317`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 5`, `concurrency: 30`, `import: 2`
* *Defense:* `safety: 39`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00073
  * `Imports (Out-Degree: 1):` EXRLoader.js, three, 3DMLoader.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/renderers/common/Renderer.js` -> Churn: **100.0%** | Cog Load: 51.3797% | Debt: 8.8896%
- `examples/jsm/loaders/usd/USDComposer.js` -> Churn: **93.72%** | Cog Load: 72.0323% | Debt: 0.0%
- `src/renderers/WebGLRenderer.js` -> Churn: **90.54%** | Cog Load: 50.1669% | Debt: 8.1419%
- `src/renderers/webgpu/utils/WebGPUTextureUtils.js` -> Churn: **76.17%** | Cog Load: 63.404% | Debt: 9.5422%
- `src/loaders/ObjectLoader.js` -> Churn: **64.76%** | Cog Load: 87.4535% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `examples/jsm/loaders/VRMLLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 3784.14
- `examples/jsm/loaders/3DMLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 1494.62
- `examples/jsm/inspector/ui/Profiler.js` -> **sunag** (88.9% isolated ownership) | Magnitude: 1406.62
- `examples/jsm/loaders/VTKLoader.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 1324.62
- `manual/examples/resources/editor.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 1223.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/nodes/tsl/TSLCore.js` -> **Severity: 0.122** (Bridge: 0.0012 * Flux: 100.0%)
- `src/nodes/math/OperatorNode.js` -> **Severity: 0.061** (Bridge: 0.0006 * Flux: 99.9891%)
- `src/loaders/ObjectLoader.js` -> **Severity: 0.058** (Bridge: 0.0006 * Flux: 100.0%)
- `src/nodes/math/MathNode.js` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 99.9998%)
- `test/unit/utils/qunit-utils.js` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `manual/resources/prettify.js` -> **Severity: 8.96** (Embedded: 0.0982 * Error Risk: 91.1983%)
- `manual/resources/lesson.js` -> **Severity: 8.431** (Embedded: 0.0982 * Error Risk: 85.8149%)
- `src/math/Vector3.js` -> **Severity: 7.141** (Embedded: 0.0847 * Error Risk: 84.3572%)
- `src/math/Matrix3.js` -> **Severity: 7.0** (Embedded: 0.0756 * Error Risk: 92.5599%)
- `src/math/Quaternion.js` -> **Severity: 6.867** (Embedded: 0.0694 * Error Risk: 98.9335%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/nodes/tsl/TSLCore.js` -> **Severity: 1856.376** (Blast Radius: 19.724 * Doc Risk: 94.1176%)
- `src/nodes/math/OperatorNode.js` -> **Severity: 1080.17** (Blast Radius: 25.204 * Doc Risk: 42.8571%)
- `src/nodes/tsl/TSLBase.js` -> **Severity: 847.0** (Blast Radius: 8.47 * Doc Risk: 100.0%)
- `src/nodes/core/TempNode.js` -> **Severity: 591.166** (Blast Radius: 17.735 * Doc Risk: 33.3333%)
- `src/math/ColorManagement.js` -> **Severity: 533.545** (Blast Radius: 5.526 * Doc Risk: 96.5517%)

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
